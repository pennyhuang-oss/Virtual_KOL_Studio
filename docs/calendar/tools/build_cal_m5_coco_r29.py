"""TASK-CAL-001 M-5 R29：Coco 單人校正的本機膚色修正版（免費、不生成、不上傳）。從 R28 結果另存，不覆蓋 R28。

- 起點：build_cal_m5_coco_r28.compose() 重建的 R28 無損合成圖（R27 H-A 原圖＋R28 編輯結果，sha256 皆核對）。
- 只改 Coco 可見的身體皮膚：脖子＋胸口、右手、雙腿。臉不動（不把臉壓暗）；頭髮、衣服、鞋、背景與其他人不動。
- 皮膚遮罩：在每塊範圍的子圖上跑 mediapipe 分割（類別 2＝身體皮膚），只取 R28 回填多邊形內、屬於 Coco 的連通區塊，
  再用影像本身當引導做邊緣保留的柔化（guided filter），避免顏色滲到衣領、頭髮、鞋口。遮罩存成 PNG（review/calendar/m5_r29/masks/），
  之後的建置只讀遮罩，可重現。
- 調整（CIELAB）：
  · 色相與飽和度（a、b）：把皮膚的「大範圍色偏」換成目標值，細部變化（膚質、紅潤、陰影裡的色差）原樣保留——
    a' = a + w·(目標 − 低頻 a)，低頻＝遮罩內加權高斯平均（σ 見 PARTS）。
  · 明暗（L）：整塊加同一個小幅度，不壓平受光方向與陰影：L' = L + w·ΔL。
  · 目標值依據：同一張照片裡相近光線的白皙角色（Rainie、Somi、Mia、Iris）臉與胸口／手／腿的關係，再對齊 Coco 自己的臉。
- 不銳化、不全圖提亮。輸出到 docs/calendar/decision_site/public/cover29/，資料 docs/calendar/data/cal_m5_r29_skin.json。
用法：python3 -I docs/calendar/tools/build_cal_m5_coco_r29.py --raw-dir DIR --edit FILE [--make-masks] [--check]
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_cal_m5_coco_r28 as R28  # noqa: E402

ROUND = 'M-5 R29'
PUB_REL = 'docs/calendar/decision_site/public/cover29'
DATA_REL = 'docs/calendar/data/cal_m5_r29_skin.json'
MASK_DIR = 'review/calendar/m5_r29/masks'
CJK_FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
TOL = 3
# 每塊：分割用子圖（全圖像素座標）、R28 回填多邊形、目標 a/b、明暗小幅提升、低頻 σ（px）
PARTS = {
    'neck_chest': {'box': (3530, 1700, 4000, 2110), 'poly': 'head_hair_neck_chest', 'ab': (15.0, 22.5), 'dL': 4.5, 'sigma': 22,
                   'drop_centroid_right_of': 3900},   # Coco 頭髮後方的 Rainie 前臂落在 R28 頭部範圍內，不能動
    'hand': {'box': (3640, 2170, 3960, 2390), 'poly': 'right_hand', 'ab': (17.0, 22.5), 'dL': 5.0, 'sigma': 14},
    'legs': {'box': (3760, 2540, 4330, 3160), 'poly': 'legs_feet', 'ab': (17.0, 23.0), 'dL': 6.0, 'sigma': 26,
             'extra_seg': [(3820, 2820, 4080, 3150)]},   # 左小腿下段在陰影裡，大子圖分不出來；用小子圖補分割
    # 左小腿下段與腳踝：R28 回填範圍沒有完全蓋到，這一截仍是 R27 原圖的膚色。仍是 Coco 可見皮膚，所以一起調；
    # 明暗以交界處（已修正的腿）為準只整塊平移，不壓平小腿內部的陰影
    'lower_shin': {'box': (3900, 2840, 4080, 3110), 'rect': (3925, 2860, 4078, 3100), 'ab': (17.0, 23.0), 'dL': 'match', 'sigma': 20,
                   'seg_box': (3820, 2820, 4080, 3150), 'exclude': 'legs', 'match_box': (3900, 2840, 4080, 2930)},
}
# 比較用局部（全圖像素座標）
VIEWS = {'face': (3600, 1560, 3920, 1900), 'neck_chest': (3600, 1820, 3960, 2110), 'hand': (3650, 2180, 3940, 2380), 'legs': (3780, 2560, 4320, 3150)}
VIEW_ZH = {'face': '臉', 'neck_chest': '脖子與胸口', 'hand': '右手', 'legs': '腿'}


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def to_lab(rgb):
    import cv2
    return cv2.cvtColor(rgb.astype(np.float32) / 255, cv2.COLOR_RGB2LAB)


def to_rgb(lab):
    import cv2
    return (cv2.cvtColor(lab.astype(np.float32), cv2.COLOR_LAB2RGB) * 255).round().clip(0, 255).astype(np.uint8)


def guided(I, p, r, eps):
    """灰階引導濾波（He et al.）；I、p 皆為 0–1 浮點。"""
    import cv2
    k = (2 * r + 1, 2 * r + 1)
    mI, mp = cv2.blur(I, k), cv2.blur(p, k)
    cov = cv2.blur(I * p, k) - mI * mp
    var = cv2.blur(I * I, k) - mI * mI
    a = cov / (var + eps)
    b = mp - a * mI
    return cv2.blur(a, k) * I + cv2.blur(b, k)


def make_masks(result):
    """在 R28 結果上產生 3 塊身體皮膚的柔邊遮罩（0–255），存成 PNG。只需要做一次；之後建置只讀檔。"""
    import cv2
    from cal_seg import categories
    Rg = json.load(open(os.path.join(ROOT, R28.REGION), encoding='utf-8'))
    os.makedirs(os.path.join(ROOT, MASK_DIR), exist_ok=True)
    rec = {}
    for k, p in PARTS.items():
        x0, y0, x1, y1 = p['box']
        sub = np.ascontiguousarray(result[y0:y1, x0:x1])
        if 'seg_box' in p:
            sx0, sy0, sx1, sy1 = p['seg_box']
            cs = categories(np.ascontiguousarray(result[sy0:sy1, sx0:sx1]))
            cat = cs[y0 - sy0:y1 - sy0, x0 - sx0:x1 - sx0]
        else:
            cat = categories(sub)
        poly = np.zeros(cat.shape, np.uint8)
        if 'rect' in p:
            rx0, ry0, rx1, ry1 = p['rect']
            poly[ry0 - y0:ry1 - y0, rx0 - x0:rx1 - x0] = 1
        else:
            cv2.fillPoly(poly, [np.array([(x - x0, y - y0) for x, y in Rg['parts'][p['poly']]], np.int32)], 1)
        sk = cat == 2
        for ex0, ey0, ex1, ey1 in p.get('extra_seg', []):
            c2 = categories(np.ascontiguousarray(result[ey0:ey1, ex0:ex1]))
            sk[ey0 - y0:ey1 - y0, ex0 - x0:ex1 - x0] |= c2 == 2
        skin = (sk & (poly == 1)).astype(np.uint8)
        n, lab, st, _ = cv2.connectedComponentsWithStats(skin, connectivity=8)
        keep = np.zeros_like(skin)
        big = int(np.argmax(st[1:, cv2.CC_STAT_AREA])) + 1 if n > 1 else 0
        dropped = []
        for i in range(1, n):
            comp = (lab == i).astype(np.uint8)
            ring = (cv2.dilate(comp, np.ones((7, 7), np.uint8)) == 1) & (comp == 0)
            out_frac = float((ring & (poly == 0)).sum()) / max(int(ring.sum()), 1)
            # 被 Coco 範圍邊界切到的區塊＝從外面伸進來的別人（例如 Mia 的腳背、Rainie 的手臂）→ 丟掉；完全在範圍內的都保留（例如被鞋子隔開的小腿下段）
            cx = float(np.mean(np.where(lab == i)[1])) + x0
            if (i == big or out_frac < 0.15) and cx <= p.get('drop_centroid_right_of', 1e9):
                keep[lab == i] = 1
            else:
                dropped.append({'px': int(st[i, cv2.CC_STAT_AREA]), 'bbox_full': [int(st[i, 0] + x0), int(st[i, 1] + y0), int(st[i, 0] + st[i, 2] + x0), int(st[i, 1] + st[i, 3] + y0)], 'outside_ring': round(out_frac, 2)})
        gray = cv2.cvtColor(sub, cv2.COLOR_RGB2GRAY).astype(np.float32) / 255
        soft = guided(gray, keep.astype(np.float32), 4, 1e-3)
        soft = np.clip(soft, 0, 1) * poly   # 不超出該塊範圍（R28 回填多邊形，或補漏的矩形）
        if 'exclude' in p:   # 和已處理的塊不重疊：權重相加不超過 1
            ex = PARTS[p['exclude']]['box']
            em = np.asarray(Image.open(os.path.join(ROOT, MASK_DIR, f"{p['exclude']}.png")), np.float32) / 255
            other = np.zeros(soft.shape, np.float32)
            ox0, oy0 = max(x0, ex[0]), max(y0, ex[1])
            ox1, oy1 = min(x1, ex[2]), min(y1, ex[3])
            other[oy0 - y0:oy1 - y0, ox0 - x0:ox1 - x0] = em[oy0 - ex[1]:oy1 - ex[1], ox0 - ex[0]:ox1 - ex[0]]
            soft = np.clip(soft - other, 0, 1)
        m = (soft * 255).round().astype(np.uint8)
        path = os.path.join(ROOT, MASK_DIR, f'{k}.png')
        Image.fromarray(m).save(path, optimize=False)
        rec[k] = {'box': list(p['box']), 'px_any': int((m > 0).sum()), 'components_kept': int(len(np.unique(lab[keep == 1]))), 'dropped': dropped, 'sha256': sha256(open(path, 'rb').read())}
    return rec


def masked_blur(x, w, sigma):
    import cv2
    num = cv2.GaussianBlur(x * w, (0, 0), sigma)
    den = cv2.GaussianBlur(w, (0, 0), sigma)
    return num / np.maximum(den, 1e-4)


def stats(lab, w):
    m = w > 0.5
    v = lab[m]
    return [round(float(t), 1) for t in v.mean(0)] if len(v) else None


def correct(result):
    out = result.copy()
    rec = {}
    import cv2
    for k, p in PARTS.items():
        x0, y0, x1, y1 = p['box']
        mpath = os.path.join(ROOT, MASK_DIR, f'{k}.png')
        w = np.asarray(Image.open(mpath), np.float32) / 255
        sub = out[y0:y1, x0:x1].copy()   # 累積結果（前面的塊已修正的部分不會被蓋回去）
        L = to_lab(sub)
        before = stats(L, w)
        dL = p['dL']
        if dL == 'match':   # 以交界帶裡已修正的相鄰塊為準，只算一個整塊平移量
            jx0, jy0, jx1, jy1 = p['match_box']
            ex = PARTS[p['exclude']]['box']
            we = np.asarray(Image.open(os.path.join(ROOT, MASK_DIR, f"{p['exclude']}.png")), np.float32) / 255
            ref = to_lab(out[jy0:jy1, jx0:jx1])[..., 0][we[jy0 - ex[1]:jy1 - ex[1], jx0 - ex[0]:jx1 - ex[0]] > 0.5]
            mine = L[jy0 - y0:jy1 - y0, jx0 - x0:jx1 - x0][..., 0][w[jy0 - y0:jy1 - y0, jx0 - x0:jx1 - x0] > 0.5]
            dL = round(float(ref.mean() - mine.mean()), 2)
        lowa = masked_blur(L[..., 1], w, p['sigma'])
        lowb = masked_blur(L[..., 2], w, p['sigma'])
        N = L.copy()
        N[..., 0] = L[..., 0] + w * dL
        N[..., 1] = L[..., 1] + w * (p['ab'][0] - lowa)
        N[..., 2] = L[..., 2] + w * (p['ab'][1] - lowb)
        rgb = to_rgb(N)
        keep = (w <= 0)[..., None]
        rgb = np.where(keep, sub, rgb)
        out[y0:y1, x0:x1] = rgb
        rec[k] = {'before_Lab': before, 'after_Lab': stats(to_lab(rgb), w), 'target_ab': list(p['ab']), 'dL': dL, 'sigma_px': p['sigma'],
                  'mask_sha256': sha256(open(mpath, 'rb').read()), 'mask_px': int((w > 0).sum())}
    return out, rec


def jpeg(im, q=90):
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=q, subsampling=2, optimize=False)
    return b.getvalue()


def lbl(im, text, h=34):
    W = Image.new('RGB', (im.width, im.height + h), (255, 255, 255))
    W.paste(im, (0, h))
    ImageDraw.Draw(W).text((6, h - 8), text, font=ImageFont.truetype(CJK_FONT, 21), fill=(30, 30, 34), anchor='ls')
    return W


def row(ims, gap=10):
    H = max(i.height for i in ims)
    o = Image.new('RGB', (sum(i.width for i in ims) + gap * (len(ims) - 1), H), (255, 255, 255))
    x = 0
    for i in ims:
        o.paste(i, (x, 0))
        x += i.width + gap
    return o


def build(raw_dir, edit_path, pub, data_path):
    if os.path.isdir(pub):
        shutil.rmtree(pub)
    os.makedirs(pub)
    K = R28.compose(raw_dir, edit_path, R28.EDIT_SHA)
    r28 = np.asarray(K['result'])
    r29, rec = correct(r28)
    # 差異：R29 對 R28（只應在皮膚遮罩內）、R29 對 R27 原圖（只應在 R28 回填範圍內）
    W = np.zeros(r28.shape[:2], np.float32)
    for k, p in PARTS.items():
        x0, y0, x1, y1 = p['box']
        W[y0:y1, x0:x1] = np.maximum(W[y0:y1, x0:x1], np.asarray(Image.open(os.path.join(ROOT, MASK_DIR, f'{k}.png')), np.float32) / 255)
    ch = np.abs(r29.astype(int) - r28.astype(int)).max(axis=2) > TOL
    orig = np.asarray(K['orig'])
    ch27 = np.abs(r29.astype(int) - orig.astype(int)).max(axis=2) > TOL
    x0, y0, x1, y1 = K['R']['crop']
    inside = np.zeros(ch.shape, bool)
    inside[y0:y1, x0:x1] = True
    m28 = np.zeros(ch.shape, np.float32)
    m28[y0:y1, x0:x1] = K['mask']
    diff = {'tolerance': f'任一通道差 > {TOL}（0–255）才算改動',
            'vs_r28_changed_px': int(ch.sum()), 'vs_r28_changed_outside_skin_mask_px': int((ch & (W == 0)).sum()), 'skin_mask_px': int((W > 0).sum()),
            'vs_r27_changed_outside_r28_region_px': int((ch27 & (m28 == 0)).sum()), 'vs_r27_changed_outside_crop_px': int((ch27 & ~inside).sum())}
    R28im, R29im = Image.fromarray(r28), Image.fromarray(r29)
    files = {}

    def save(name, data):
        open(os.path.join(pub, name), 'wb').write(data)
        files[name] = sha256(data)
    vw = 1600
    vh = round(R29im.height * vw / R29im.width)
    save('r29_after_f.jpg', jpeg(R29im))
    save('r29_after_v.jpg', jpeg(R29im.resize((vw, vh), Image.LANCZOS), 88))
    # 局部：原尺寸（R28｜R29）
    for k, b in VIEWS.items():
        a, c = R28im.crop(b), R29im.crop(b)
        save(f'r29_part_{k}.jpg', jpeg(row([lbl(a, f'R28｜{VIEW_ZH[k]}'), lbl(c, f'R29 修正版｜{VIEW_ZH[k]}')]), 92))
    # 封面尺寸（成品 200 mm 寬、300 dpi ≈ 2440 px 寬）的 Coco 周圍
    cw = 2440
    s = cw / R29im.width
    cb = (3380, 1450, 4420, 3200)
    sb = tuple(round(v * s) for v in cb)
    a = R28im.resize((cw, round(R29im.height * s)), Image.LANCZOS).crop(sb)
    c = R29im.resize((cw, round(R29im.height * s)), Image.LANCZOS).crop(sb)
    save('r29_coverscale.jpg', jpeg(row([lbl(a, 'R28｜封面尺寸'), lbl(c, 'R29 修正版｜封面尺寸')]), 92))
    # 臉部與身分基準（臉未改動，仍附對照）
    ref = Image.open(os.path.join(ROOT, R28.REF)).convert('RGB')
    rbox = json.load(open(os.path.join(ROOT, R28.BOXES), encoding='utf-8'))['refs']['coco-wu']
    fb = json.load(open(os.path.join(ROOT, R28.BOXES), encoding='utf-8'))['covers']['H-A']['people']['coco-wu']['face']
    T = 360
    save('r29_face_cmp.jpg', jpeg(row([lbl(ref.crop(tuple(rbox)).resize((T, T), Image.LANCZOS), '身分基準（Coco）'),
                                       lbl(R28.face_crop(R29im, fb).resize((T, T), Image.LANCZOS), 'R29 修正版')]), 90))
    # 修正範圍與差異（收合在技術區）
    mv = (np.dstack([W * 255] * 3)).astype(np.uint8)
    save('r29_mask_v.jpg', jpeg(Image.fromarray(mv).crop((3380, 1450, 4420, 3200)).resize((520, 875), Image.LANCZOS), 88))
    dm = Image.fromarray((ch * 255).astype(np.uint8)).resize((vw, vh), Image.BOX)
    save('r29_diff_v.jpg', jpeg(Image.merge('RGB', (dm, dm, dm)), 88))
    out = []
    for name, h in sorted(files.items()):
        im = Image.open(os.path.join(pub, name))
        out.append({'path': name, 'sha256': h, 'px': [im.width, im.height], 'bytes': os.path.getsize(os.path.join(pub, name))})
    D = {'round': ROUND,
         'note': 'Coco 單人校正的本機膚色修正版（從 R28 結果另存，不覆蓋 R28）。只改脖子＋胸口、右手、雙腿的皮膚；臉、頭髮、衣服、背景、其他人不動。生成 0、付費 0、上傳 0。',
         'source': {'r27_sha256': R28.SRC_SHA, 'r28_edit_sha256': R28.EDIT_SHA},
         'method': '分割遮罩（mediapipe 身體皮膚）∩ R28 回填範圍 → 只留 Coco 的大塊 → 引導濾波柔邊；CIELAB：a/b 的低頻色偏換成目標、細部保留；L 整塊小幅提升；不銳化',
         'parts': rec, 'diff': diff, 'files': out}
    with open(data_path, 'w', encoding='utf-8') as fh:
        json.dump(D, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    return D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw-dir', required=True)
    ap.add_argument('--edit', required=True)
    ap.add_argument('--make-masks', action='store_true')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.make_masks:
        K = R28.compose(a.raw_dir, a.edit, R28.EDIT_SHA)
        print(json.dumps(make_masks(np.asarray(K['result'])), ensure_ascii=False))
        return
    if a.check:
        old = json.load(open(os.path.join(ROOT, DATA_REL), encoding='utf-8'))
        with tempfile.TemporaryDirectory() as tmp:
            D = build(a.raw_dir, a.edit, os.path.join(tmp, 'p'), os.path.join(tmp, 'd.json'))
            same = json.loads(json.dumps(D, ensure_ascii=False)) == old
            pub = os.path.join(ROOT, PUB_REL)
            diff = [x['path'] for x in D['files'] if not os.path.exists(os.path.join(pub, x['path'])) or sha256(open(os.path.join(pub, x['path']), 'rb').read()) != x['sha256']]
            extra = sorted(set(os.listdir(pub)) - {x['path'] for x in D['files']})
        ok = same and not diff and not extra
        print(json.dumps({'check': 'PASS' if ok else 'FAIL', 'data_same': same, 'files': len(D['files']), 'diff': diff, 'extra': extra}, ensure_ascii=False))
        sys.exit(0 if ok else 1)
    D = build(a.raw_dir, a.edit, os.path.join(ROOT, PUB_REL), os.path.join(ROOT, DATA_REL))
    print(json.dumps({k: D[k] for k in ('parts', 'diff')}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
