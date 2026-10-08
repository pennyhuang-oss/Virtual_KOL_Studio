#!/usr/bin/env python3
"""TASK-CAL-001 / R3 — 主推薦圖的本機局部清理（不花 credits、不生成、不 AI 增強）。

輸入：data/cal_r3_cleanup.json（人寫：哪張圖、哪個區域、什麼操作、為什麼）
操作：inpaint＝OpenCV Telea 修補（小面積字樣／道具）；blur＝主角以外的高斯模糊（排除主角像素的正規化卷積，避免主角顏色暈開）；
      blur_dim＝模糊＋減光（降低路人顯著度，不刪除）。
保護：主角遮罩（cal_seg.subject_mask）外擴後，任何操作都不寫入；程式最後核對主角遮罩內像素與原圖逐一相同。
輸出：<cache>/clean/<cid>.png（完整清理圖，不進 repo；原圖不動）、data/cal_r3_cleanup_report.json、
      r3/cleanup/<cid>_overview.jpg（修前／修後全圖）。區域 100% 對照與版面實際大小對照由 build_cal_r3_pages.py 產生。
用法：python3 docs/calendar/tools/build_cal_r3_cleanup.py --hf-dir <原圖快取> --cache <清理輸出資料夾>
"""
import argparse
import hashlib
import json
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from cal_face_lib import geometry  # noqa: E402
from cal_seg import categories, subject_mask  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
OUT = os.path.join(CAL, 'r3', 'cleanup')
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'


def src_path(cid, J, R, hf):
    s = J[cid]['src']
    if s.startswith('hf:'):
        return os.path.join(hf, next(r for r in R if r['job_id'] == s[3:])['local'])
    return os.path.join(ROOT, s)


def box_px(b, W, H):
    return int(b[0] * W), int(b[1] * H), int(np.ceil(b[2] * W)), int(np.ceil(b[3] * H))


def feather_mask(shape, box, feather):
    m = np.zeros(shape, np.float32)
    x0, y0, x1, y1 = box
    m[y0:y1, x0:x1] = 1
    if feather > 0:
        m = cv2.GaussianBlur(m, (0, 0), feather)
        m[y0 + int(2 * feather):y1 - int(2 * feather), x0 + int(2 * feather):x1 - int(2 * feather)] = 1
    return m


def masked_blur(img, valid, sigma):
    """只用 valid 像素做高斯模糊（正規化卷積），主角像素不會被抹進背景。"""
    v = valid.astype(np.float32)
    num = cv2.GaussianBlur(img.astype(np.float32) * v[..., None], (0, 0), sigma)
    den = cv2.GaussianBlur(v, (0, 0), sigma)[..., None]
    return np.where(den > 1e-3, num / np.maximum(den, 1e-3), img.astype(np.float32))


def add_grain(out, m, ring_px, seed):
    """在填補區加上與周圍相同強度的細顆粒（避免填補區比四周「太乾淨」）。"""
    ring = (cv2.dilate(m, np.ones((2 * ring_px + 1, 2 * ring_px + 1), np.uint8)) > 0) & (m == 0)
    hp = out - cv2.GaussianBlur(out, (0, 0), 1.5)
    std = float(hp[ring].std()) if ring.any() else 0.0
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, std, m.shape).astype(np.float32)
    noise = noise - cv2.GaussianBlur(noise, (0, 0), 1.5)
    return np.where(m[..., None] > 0, out + noise[..., None], out)


def harmonic_fill(out, m, iters=3000):
    """邊界值固定、內部解拉普拉斯方程（平滑薄膜），只在 m 的外接矩形內迭代。"""
    ys, xs = np.where(m > 0)
    y0, y1, x0, x1 = max(ys.min() - 2, 0), ys.max() + 3, max(xs.min() - 2, 0), xs.max() + 3
    roi = out[y0:y1, x0:x1].copy()
    mm = m[y0:y1, x0:x1] > 0
    init = cv2.inpaint(np.clip(roi, 0, 255).astype(np.uint8), mm.astype(np.uint8), 5, cv2.INPAINT_TELEA).astype(np.float32)
    u = np.where(mm[..., None], init, roi)
    for _ in range(iters):
        avg = (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1)) / 4
        u = np.where(mm[..., None], avg, roi)
    out = out.copy()
    out[y0:y1, x0:x1] = u
    return out


def vertical_fill(out, m):
    """逐欄在缺口上下最近的有效像素之間線性內插（保留直向邊緣，例如鏡框）。"""
    out = out.copy()
    H = m.shape[0]
    for x in np.where(m.any(0))[0]:
        col = m[:, x] > 0
        y = 0
        while y < H:
            if not col[y]:
                y += 1
                continue
            s = y
            while y < H and col[y]:
                y += 1
            e = y  # [s, e) 缺口
            top = out[s - 1, x] if s > 0 else out[e, x]
            bot = out[e, x] if e < H else top
            t = (np.arange(s, e) - (s - 1)) / (e - s + 1)
            out[s:e, x] = top[None, :] * (1 - t[:, None]) + bot[None, :] * t[:, None]
    return out


def poly_mask(shape, op, W, H):
    m = np.zeros(shape, np.uint8)
    for poly in op.get('polys', []):
        cv2.fillPoly(m, [np.round(np.array(poly) * [W, H]).astype(np.int32)], 1)
    for cx, cy, r in op.get('circles', []):
        cv2.circle(m, (int(cx * W), int(cy * H)), int(r * W), 1, -1)
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hf-dir', required=True)
    ap.add_argument('--cache', required=True)
    a = ap.parse_args()
    spec = json.load(open(os.path.join(CAL, 'data', 'cal_r3_cleanup.json')))
    J = {c['cid']: c for c in json.load(open(os.path.join(CAL, 'data', 'cal_r2_judgments.json')))['candidates']}
    R = json.load(open(os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')))['items']
    os.makedirs(os.path.join(a.cache, 'clean'), exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    report = []
    for item in spec['items']:
        cid = item['cid']
        p = src_path(cid, J, R, a.hf_dir)
        rgb = np.asarray(Image.open(p).convert('RGB'))
        H, W = rgb.shape[:2]
        g = geometry(p)
        subj = subject_mask(rgb, g['P'])
        d = max(3, int(spec['protect_dilate_frac'] * W))
        kern = np.ones((2 * d + 1, 2 * d + 1), np.uint8)
        protect_all = cv2.dilate(subj.astype(np.uint8), kern) > 0
        # 只在明示 allow_on_clothes 的操作（壓在衣服上的假字戳）才放行衣服像素；臉、皮膚、頭髮、配件永遠保護
        not_clothes = subj & (categories(rgb) != 4)
        protect_noclothes = cv2.dilate(not_clothes.astype(np.uint8), kern) > 0
        allowed = np.zeros((H, W), bool)
        out = rgb.astype(np.float32).copy()
        ops = []
        for op in item['ops']:
            bx = box_px(op['box'], W, H)
            protect = protect_noclothes if op.get('allow_on_clothes') else protect_all
            if op['op'] == 'inpaint':
                m = np.zeros((H, W), np.uint8)
                x0, y0, x1, y1 = bx
                reg = np.clip(out[y0:y1, x0:x1], 0, 255).astype(np.uint8)
                if op.get('select') == 'contrast':
                    # 字樣＋外框：與局部中值背景差異大的像素（中值濾波保留背景的直邊，例如鏡框）
                    bg = cv2.medianBlur(reg, op.get('k', 31))
                    sel = np.abs(reg.astype(int) - bg.astype(int)).max(-1) > op.get('thr', 28)
                    if op.get('warm'):
                        sel |= (reg[..., 0].astype(int) > 140) & (reg[..., 0].astype(int) - reg[..., 2].astype(int) > 70)
                elif op.get('select') == 'non_light':
                    # 淺色布面（枕頭）以外的東西：最大連通區塊取凸包（物件本體），再加上其他非淺色像素（陰影、反光、線）
                    hsv = cv2.cvtColor(reg, cv2.COLOR_RGB2HSV)
                    light = (hsv[..., 1] < op.get('s_max', 40)) & (hsv[..., 2] > op.get('v_min', 150))
                    sel = (~light).astype(np.uint8)
                    sel[protect[y0:y1, x0:x1]] = 0
                    n, lab, st, _ = cv2.connectedComponentsWithStats(sel, connectivity=8)
                    if n > 1:
                        big = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
                        hull = cv2.convexHull(np.argwhere(lab == big)[:, ::-1].astype(np.int32))
                        cv2.fillPoly(sel, [hull], 1)
                    sel = sel.astype(bool)
                elif op.get('select') == 'poly':
                    sel = poly_mask((H, W), op, W, H)[y0:y1, x0:x1].astype(bool)
                else:
                    sel = np.ones(reg.shape[:2], bool)
                m[y0:y1, x0:x1] = sel.astype(np.uint8)
                g = op.get('grow', 3)
                if g:
                    m = cv2.dilate(m, np.ones((2 * g + 1, 2 * g + 1), np.uint8))
                m[:y0], m[y1:], m[:, :x0], m[:, x1:] = 0, 0, 0, 0
                m[protect] = 0
                if op.get('allow_on_clothes'):
                    allowed |= (m > 0) & subj
                if op.get('method') == 'clone':
                    # Poisson 無縫複製（OpenCV seamlessClone，梯度域融合）：用 offset 位置的同材質（枕頭）紋理填補，再對齊邊界亮度
                    dx, dy = int(round(op['offset'][0] * W)), int(round(op['offset'][1] * H))
                    src = np.roll(np.roll(np.clip(out, 0, 255).astype(np.uint8), -dy, 0), -dx, 1)
                    ys, xs = np.where(m > 0)
                    c = (int((xs.min() + xs.max()) // 2), int((ys.min() + ys.max()) // 2))
                    res = cv2.seamlessClone(src[..., ::-1].copy(), np.clip(out, 0, 255).astype(np.uint8)[..., ::-1].copy(),
                                            m * 255, c, cv2.NORMAL_CLONE)[..., ::-1].astype(np.float32)
                elif op.get('method') == 'vertical':
                    res = vertical_fill(out, m)
                elif op.get('method') == 'harmonic':
                    res = harmonic_fill(out, m)
                else:
                    res = cv2.inpaint(np.clip(out, 0, 255).astype(np.uint8)[..., ::-1], m, op.get('radius', 7), cv2.INPAINT_TELEA)[..., ::-1].astype(np.float32)
                res = np.where(m[..., None] > 0, res, out)
                if op.get('grain'):
                    res = add_grain(res, m, op.get('ring', 12), seed=len(cid))
                out = res
                changed = int(m.sum())
            else:
                sigma = op['sigma'] * W
                fm = feather_mask((H, W), bx, op.get('feather', 0.01) * W)
                # 保護區邊緣羽化：越靠近主角，修改量越小，避免在主角輪廓外出現一圈硬邊
                soft = cv2.GaussianBlur(protect.astype(np.float32), (0, 0), d)
                fm = fm * np.clip(1 - 1.6 * soft, 0, 1)
                fm[protect] = 0
                bl = masked_blur(out, ~protect, sigma)
                if op['op'] == 'blur_dim':
                    bl = bl * op.get('dim', 0.85)
                out = out * (1 - fm[..., None]) + bl * fm[..., None]
                changed = int((fm > 0.02).sum())
            ops.append({**op, 'box_px': list(bx), 'pixels_changed': changed})
        res = np.clip(np.round(out), 0, 255).astype(np.uint8)
        keep = subj & ~allowed
        res[keep] = rgb[keep]  # 保險：主角像素一律回寫原值（明示放行的衣服上字戳除外）
        diff_in_subject = int(np.abs(res[keep].astype(int) - rgb[keep].astype(int)).max()) if keep.any() else 0
        face_skin_hair = subj & (categories(rgb) != 4)
        diff_face_skin_hair = int(np.abs(res[face_skin_hair].astype(int) - rgb[face_skin_hair].astype(int)).max()) if face_skin_hair.any() else 0
        dst = os.path.join(a.cache, 'clean', f'{cid}.png')
        Image.fromarray(res).save(dst)
        report.append({'cid': cid, 'why': item['why'], 'src': J[cid]['src'],
                       'src_sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest(),
                       'clean_file': f'clean/{cid}.png', 'clean_sha256': hashlib.sha256(open(dst, 'rb').read()).hexdigest(),
                       'size': [W, H], 'subject_pixels': int(subj.sum()), 'protect_dilate_px': d,
                       'max_abs_diff_inside_subject_except_allowed': diff_in_subject,
                       'max_abs_diff_face_skin_hair_accessory': diff_face_skin_hair,
                       'clothes_pixels_changed_by_allowed_ops': int(allowed.sum()), 'ops': ops})
        # 修前／修後全圖
        A, B = Image.fromarray(rgb), Image.fromarray(res)
        for im in (A, B):
            im.thumbnail((700, 900))
        S = Image.new('RGB', (A.width * 2 + 30, A.height + 60), 'white')
        dr = ImageDraw.Draw(S)
        dr.text((8, 8), f'{cid}｜左：原圖　右：清理後（{item["why"]}）', fill='black', font=ImageFont.truetype(FONT, 20))
        S.paste(A, (0, 50))
        S.paste(B, (A.width + 30, 50))
        k = A.width / W
        for op in ops:
            x0, y0, x1, y1 = op['box_px']
            for off in (0, A.width + 30):
                dr.rectangle((off + x0 * k, 50 + y0 * k, off + x1 * k, 50 + y1 * k), outline=(255, 0, 0), width=2)
        S.save(os.path.join(OUT, f'{cid}_overview.jpg'), quality=86)
        print(cid, [o['pixels_changed'] for o in ops], 'subject diff', diff_in_subject, 'face/skin/hair diff', diff_face_skin_hair, 'clothes changed', int(allowed.sum()))
    json.dump({'generated_by': 'docs/calendar/tools/build_cal_r3_cleanup.py', 'spec': 'data/cal_r3_cleanup.json',
               'note': '清理後完整圖存在本機快取（不進 repo）；clean_sha256 用來核對樣張實際使用的是哪一版。',
               'items': report, 'evaluated_no_op': spec.get('evaluated_no_op', [])},
              open(os.path.join(CAL, 'data', 'cal_r3_cleanup_report.json'), 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
