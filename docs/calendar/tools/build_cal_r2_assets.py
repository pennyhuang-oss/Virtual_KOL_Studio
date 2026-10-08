#!/usr/bin/env python3
"""TASK-CAL-001 / R2 — 候選圖技術量測、裁切預覽、原圖 100% 細節圖、角色一致性對照。

只讀原圖、只做裁切／縮放／加參考線；不修圖、不生成。
輸入：data/cal_r2_judgments.json（人寫的判斷與細節框）、data/cal_r2_hf_retrieved.json（Higgsfield 既有 job 的本機檔名）
輸出：data/cal_r2_asset_metrics.json（程式量測）、r2/assets/*（預覽、細節圖、一致性對照）、CAL_11b_ASSET_TABLE.generated.md
用法：python3 docs/calendar/tools/build_cal_r2_assets.py --hf-dir <取回原圖的資料夾>
"""
import argparse
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from cal_face_lib import geometry, masked_face  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
OUT = os.path.join(CAL, 'r2', 'assets')
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'

# 本輪樣張實際使用的照片框（mm，含出血的畫布座標）。coil = 線圈保留區（畫布上緣起算）。
FRAMES = {
    'H_split': {'w': 104, 'h': 155, 'top': 0, 'coil': 12, 'fy': 0.30, 'label': '橫式半版照片框 104×155（日期在另一半）'},
    'V_big':   {'w': 144, 'h': 150, 'top': 0, 'coil': 12, 'fy': 0.36, 'label': '直式大照片 144×150（日期在下方白底）'},
    'V_inset': {'w': 124, 'h': 132, 'top': 16, 'coil': 12, 'fy': 0.36, 'label': '直式縮框 124×132（四周留白）'},
    'H_wide':  {'w': 204, 'h': 112, 'top': 0, 'coil': 12, 'fy': 0.40, 'label': '橫式大照片 204×112（日期在下方）'},
}
BANDS = ((300, '充裕'), (250, '可'), (200, '邊緣'), (0, '不足'))  # 本專案工作判準，非廠商要求


def font(n):
    return ImageFont.truetype(FONT, n)


def band(p):
    return next(b for t, b in BANDS if p >= t)


def resolve(src, hf_dir, retrieved):
    if src.startswith('hf:'):
        x = next(r for r in retrieved if r['job_id'] == src[3:])
        return os.path.join(hf_dir, x['local'])
    return os.path.join(ROOT, src)


def crop_box(W, H, cx, cy, F):
    a = F['w'] / F['h']
    if W / H > a:
        ch, cw = H, round(H * a)
        x0 = min(max(round(cx - cw / 2), 0), W - cw)
        y0 = 0
    else:
        cw, ch = W, round(W / a)
        x0 = 0
        y0 = min(max(round(cy - F['fy'] * ch), 0), H - ch)
    return x0, y0, cw, ch


def measure(path, F, g, anchor):
    im = Image.open(path)
    W, H = im.size
    if g:
        P = g['P']
        top = float(P[10][1])
        chin = float(P[152][1])
        cx = float(g['mid'][0])
        cy = (top + chin) / 2
        hair_top = top - 0.45 * (chin - top)  # 粗估頭頂（含頭髮），只用來檢查線圈
    else:
        cx, cy = anchor[0] * W, anchor[1] * H
        top = chin = hair_top = None
    x0, y0, cw, ch = crop_box(W, H, cx, cy, F)
    k = F['h'] / ch  # mm per px
    res = {'src_px': [W, H], 'crop_px': [x0, y0, cw, ch], 'keeps_pct': round(cw * ch / (W * H) * 100),
           'effective_ppi': round(cw / (F['w'] / 25.4)), 'face_detected': bool(g)}
    res['ppi_band'] = band(res['effective_ppi'])
    if g:
        res['face_height_mm'] = round((chin - top) * k, 1)
        res['forehead_y_mm'] = round(F['top'] + (top - y0) * k, 1)
        res['head_top_y_mm_est'] = round(F['top'] + (hair_top - y0) * k, 1)
        res['chin_y_mm'] = round(F['top'] + (chin - y0) * k, 1)
        inside = top >= y0 and chin <= y0 + ch and x0 <= cx <= x0 + cw
        res['face_inside_frame'] = bool(inside)
        res['forehead_clear_of_coil'] = res['forehead_y_mm'] >= F['coil'] + 3
    return res, (x0, y0, cw, ch)


def preview(path, box, F, out, label):
    im = Image.open(path).convert('RGB')
    x0, y0, cw, ch = box
    pv = im.crop((x0, y0, x0 + cw, y0 + ch))
    pv.thumbnail((380, 380))
    pw, ph = pv.size
    k = ph / F['h']
    ov = Image.new('RGBA', pv.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    coil_in = max(0, F['coil'] - F['top'])
    if coil_in:
        d.rectangle((0, 0, pw, coil_in * k), fill=(255, 0, 0, 90))
    d.rectangle((2 * k, 2 * k, pw - 2 * k, ph - 2 * k), outline=(255, 255, 255, 230), width=1)
    pv = Image.alpha_composite(pv.convert('RGBA'), ov).convert('RGB')
    dd = ImageDraw.Draw(pv)
    dd.rectangle((0, ph - 22, pw, ph), fill='black')
    dd.text((3, ph - 21), label, fill='yellow', font=font(15))
    pv.save(out, quality=84)


def save_small(img, out, max_w=2000):
    hi = out.replace('.jpg', '_hires.jpg')
    img.save(hi, quality=90)
    img = img.copy()
    img.thumbnail((max_w, max_w * 4))
    q = 85
    while True:
        img.save(out, quality=q)
        if os.path.getsize(out) < 1_000_000 or q <= 55:
            break
        q -= 5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hf-dir', required=True)
    a = ap.parse_args()
    J = json.load(open(os.path.join(CAL, 'data', 'cal_r2_judgments.json')))
    retrieved = json.load(open(os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')))['items']
    for sub in ('crops', 'details', 'consistency'):
        os.makedirs(os.path.join(OUT, sub), exist_ok=True)

    metrics = {}
    for c in J['candidates']:
        p = resolve(c['src'], a.hf_dir, retrieved)
        g = geometry(p)
        m = {'frames': {}}
        for fname, F in FRAMES.items():
            r, box = measure(p, F, g, c.get('anchor', [0.5, 0.25]))
            pv = os.path.join(OUT, 'crops', f"{c['cid']}_{fname}.jpg")
            preview(p, box, F, pv, f"{fname} {r['effective_ppi']}ppi")
            r['preview'] = os.path.relpath(pv, CAL)
            m['frames'][fname] = r
        # 100% 細節圖：臉（自動）＋人工框
        im = Image.open(p).convert('RGB')
        W, H = im.size
        dets = []
        if g:
            P = g['P']
            fx0, fx1 = P[:, 0].min(), P[:, 0].max()
            fy0, fy1 = P[:, 1].min(), P[:, 1].max()
            pad = 0.25 * (fx1 - fx0)
            dets.append(('臉', (fx0 - pad, fy0 - pad, fx1 + pad, fy1 + pad)))
        for d in c.get('details', []):
            x0, y0, x1, y1 = d['box']
            dets.append((d['what'], (x0 * W, y0 * H, x1 * W, y1 * H)))
        m['details'] = []
        for i, (what, b) in enumerate(dets):
            b = tuple(int(max(0, v)) for v in b)
            b = (b[0], b[1], min(b[2], W), min(b[3], H))
            crop = im.crop(b)
            if crop.width > 640 or crop.height > 640:
                crop.thumbnail((640, 640))  # 超過 640 px 才縮；標記實際倍率
            scale = round(crop.width / max(1, b[2] - b[0]) * 100)
            out = os.path.join(OUT, 'details', f"{c['cid']}_{i}.jpg")
            crop.save(out, quality=90)
            m['details'].append({'what': what, 'box_px': list(b), 'shown_at_pct': scale, 'file': os.path.relpath(out, CAL)})
        # 一致性：候選臉 vs 該角色參考臉（遮髮）
        if g and c.get('ref'):
            rp = resolve(c['ref'], a.hf_dir, retrieved)
            rg = geometry(rp)
            if rg:
                o1 = os.path.join(OUT, 'consistency', f"{c['cid']}_cand.jpg")
                o2 = os.path.join(OUT, 'consistency', f"{c['cid']}_ref.jpg")
                masked_face(p, g, o1, w=260, h=320, iod_px=90)
                masked_face(rp, rg, o2, w=260, h=320, iod_px=90)
                m['consistency_pair'] = [os.path.relpath(o1, CAL), os.path.relpath(o2, CAL)]
        metrics[c['cid']] = m

    json.dump({'generated_by': 'docs/calendar/tools/build_cal_r2_assets.py', 'frames': FRAMES,
               'ppi_bands': '≥300 充裕｜250–299 可｜200–249 邊緣｜<200 不足（本專案工作判準，非廠商要求）',
               'head_top_note': 'head_top_y_mm_est = 額頭點往上加 0.45×臉高的粗估，只用來看頭髮會不會被線圈壓到',
               'metrics': metrics}, open(os.path.join(CAL, 'data', 'cal_r2_asset_metrics.json'), 'w'), ensure_ascii=False, indent=1)
    sheets(J, metrics)
    table(J, metrics)
    print('ok', len(metrics))


def sheets(J, M):
    f = font(18)
    persons = []
    for c in J['candidates']:
        if c['pid'] not in persons:
            persons.append(c['pid'])
    # 每人一張：候選 × 四種框的預覽 ＋ 細節圖
    for pid in persons:
        cs = [c for c in J['candidates'] if c['pid'] == pid]
        rows = []
        for c in cs:
            m = M[c['cid']]
            ims = [Image.open(os.path.join(CAL, m['frames'][k]['preview'])) for k in FRAMES]
            dets = [Image.open(os.path.join(CAL, d['file'])) for d in m['details']]
            for d in dets:
                d.thumbnail((300, 300))
            h = max([i.height for i in ims] + [d.height for d in dets] + [60]) + 34
            w = 10 + sum(i.width + 6 for i in ims) + sum(d.width + 6 for d in dets)
            row = Image.new('RGB', (max(w, 900), h), 'white')
            dr = ImageDraw.Draw(row)
            dr.text((6, 4), f"{c['cid']}｜{c['role_zh']}｜{c['src']}", fill='black', font=f)
            x = 6
            for i in ims:
                row.paste(i, (x, 30))
                x += i.width + 6
            for d, meta in zip(dets, m['details']):
                row.paste(d, (x, 30))
                dr.rectangle((x, 30, x + d.width, 50), fill='black')
                dr.text((x + 3, 31), f"{meta['what']} {meta['shown_at_pct']}%", fill='yellow', font=font(14))
                x += d.width + 6
            rows.append(row)
        W = max(r.width for r in rows)
        S = Image.new('RGB', (W, sum(r.height + 8 for r in rows) + 40), '#bbb')
        ImageDraw.Draw(S).text((8, 8), f'{pid}｜裁切預覽（紅＝線圈區、白框＝裁切線）＋原圖細節（百分比＝顯示倍率）', fill='black', font=font(22))
        y = 40
        for r in rows:
            S.paste(r, (0, y))
            y += r.height + 8
        save_small(S, os.path.join(OUT, f'CAL_R2_assets_{pid}.jpg'))
    # 一致性總表
    cells = []
    for c in J['candidates']:
        m = M[c['cid']]
        if 'consistency_pair' not in m:
            continue
        a, b = (Image.open(os.path.join(CAL, p)) for p in m['consistency_pair'])
        cell = Image.new('RGB', (a.width + b.width + 6, a.height + 52), 'white')
        cell.paste(a, (0, 26))
        cell.paste(b, (a.width + 6, 26))
        d = ImageDraw.Draw(cell)
        d.text((2, 2), c['cid'], fill='black', font=font(17))
        d.text((2, a.height + 28), '候選', fill='#333', font=font(15))
        d.text((a.width + 8, a.height + 28), f"參考：{c['ref_zh']}", fill='#333', font=font(15))
        cells.append(cell)
    cols = 4
    cw = max(c.width for c in cells) + 8
    chh = max(c.height for c in cells) + 8
    for part in range(0, len(cells), 16):
        g = cells[part:part + 16]
        S = Image.new('RGB', (cols * cw, ((len(g) + cols - 1) // cols) * chh + 40), '#ccc')
        ImageDraw.Draw(S).text((8, 8), '角色一致性：候選臉 vs 該角色參考臉（皆遮髮遮衣，以眼距等比縮放，未旋轉）', fill='black', font=font(22))
        for i, cimg in enumerate(g):
            S.paste(cimg, ((i % cols) * cw, 40 + (i // cols) * chh))
        save_small(S, os.path.join(OUT, f'CAL_R2_consistency_{part // 16 + 1}.jpg'))


def table(J, M):
    L = ['# CAL_11b — 候選圖逐張分欄（程式產生，請勿手改）', '',
         '> 由 `docs/calendar/tools/build_cal_r2_assets.py` 產生。技術欄由程式從原圖現算；角色一致性、美感、動作來自 `data/cal_r2_judgments.json`（人寫）。',
         '> ppi＝裁切後實際像素 ÷ 照片框寬（英吋），未放大。分級為本專案工作判準：≥300 充裕｜250–299 可｜200–249 邊緣｜<200 不足。',
         '> 日期遮擋：本輪 H_split／V_big／V_inset／H_wide 四種框的日期都不在照片上（另一半或下方白底），所以「照片被日期遮」一律不適用；表內只看線圈。', '']
    for c in J['candidates']:
        m = M[c['cid']]
        L.append(f"## {c['cid']}（{c['pid']}｜{c['role_zh']}）")
        L.append('')
        L.append(f"- 來源：`{c['src']}`　原圖 {m['frames']['H_split']['src_px'][0]}×{m['frames']['H_split']['src_px'][1]}　狀態：{c['status']}")
        L.append('')
        L.append('| 框 | 有效 ppi | 保留原圖 | 臉高 mm | 額頭 y mm | 頭頂估 y mm | 額頭避開線圈 | 臉在框內 |')
        L.append('|---|---|---|---|---|---|---|---|')
        for k, r in m['frames'].items():
            L.append(f"| {k} | {r['effective_ppi']}（{r['ppi_band']}） | {r['keeps_pct']}% | {r.get('face_height_mm', '—')} | {r.get('forehead_y_mm', '—')} | "
                     f"{r.get('head_top_y_mm_est', '—')} | {'是' if r.get('forehead_clear_of_coil') else ('否' if r.get('face_detected') else '未偵測')} | "
                     f"{'是' if r.get('face_inside_frame') else ('否' if r.get('face_detected') else '未偵測')} |")
        L.append('')
        L.append(f"- 預定用途：{c['use_for']}")
        L.append(f"- 技術判讀：{c['tech']}")
        L.append(f"- 角色一致性：{c['consistency']}")
        L.append(f"- 美感：{c['aesthetic']}")
        L.append(f"- 瑕疵（看過原圖 100% 細節）：{c['defects']}")
        L.append(f"- 動作：**{c['action']}**　｜　採用層級：{c['adoption']}")
        if c.get('h_wide_note'):
            L.append(f"- 橫式大照片（H_wide）：{c['h_wide_note']}")
        L.append('')
    open(os.path.join(CAL, 'CAL_11b_ASSET_TABLE.generated.md'), 'w').write('\n'.join(L))


if __name__ == '__main__':
    main()
