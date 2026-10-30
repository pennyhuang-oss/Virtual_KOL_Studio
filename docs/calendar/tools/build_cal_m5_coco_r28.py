"""TASK-CAL-001 M-5 R28：H-A 裡 Coco 的單人身分校正測試——把編輯結果回填到同一張照片，並產生比較圖與差異紀錄。

- 輸入（私有、不進 git，用參數指定）：R27 H-A 原圖 cover_H-A.png、本輪編輯結果 coco_edit.png（sha256 都必須與紀錄相同）。
- 編輯方式：從 H-A 裁出 Coco 周圍 9:16 範圍（review/calendar/m5_r28/region.json 的 crop）送去編輯；
  拿回的結果等比縮回裁切尺寸，只在 Coco 本人的範圍（region.json 的 parts：頭髮臉部到胸口、右手、雙腿與鞋）
  用羽化遮罩回填到同一張照片的原位置；裁切範圍外、遮罩外都用原圖像素。不放大其他人、不剪貼獨立人物。
- 對位：編輯結果先等比縮回裁切尺寸，再用 OpenCV ECC 仿射對位（只看遮罩外的區域）修正模型造成的微小位移／縮放，矩陣照實記錄。
- 差異紀錄：全圖逐像素與原圖比，分「裁切範圍外」「裁切內遮罩外」「遮罩內」；另記編輯結果在遮罩外
  （其他人與背景）被模型改了多少——這些像素沒有用到，只當作工具漂移的證據。
- 輸出（docs/calendar/decision_site/public/cover28/，皆不帶中繼資料）與資料 docs/calendar/data/cal_m5_r28_coco_test.json。
用法：python3 -I docs/calendar/tools/build_cal_m5_coco_r28.py --raw-dir DIR --edit FILE [--check]
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
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
ROUND = 'M-5 R28'
PUB_REL = 'docs/calendar/decision_site/public/cover28'
DATA_REL = 'docs/calendar/data/cal_m5_r28_coco_test.json'
REGION = 'review/calendar/m5_r28/region.json'
REF = 'review/calendar/m5_r27/refs/ref06_coco-wu.jpg'
REF_SHA = 'bcfe9fed346c55584db1c86e2308abbdb79135bb5212c97c721eb72d82308c36'
BOXES = 'review/calendar/m5_r27/face_boxes.json'
SRC_SHA = '278ce0954d3a5527c418a25de527a0cb82fe9f5e958ea27eede2c9ce38aae6f5'   # R27 H-A 原圖
EDIT_SHA = '724d675fbc9baf50d827539f90951f422343e77080a00af76a71c008de377e5d'   # 本輪唯一一次編輯結果（1536×2752）
VIEW_W = 1600
CJK_FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
TOL = 3   # 逐像素差異門檻（0–255，任一通道超過才算改動；JPEG 以外的原生像素比對）


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def jpeg(im, q=90, sub=2):
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=q, subsampling=sub, optimize=False)
    return b.getvalue()


def load(path, want):
    b = open(path, 'rb').read()
    if want:
        assert sha256(b) == want, f'{os.path.basename(path)}：sha256 與紀錄不同'
    im = Image.open(io.BytesIO(b))
    im.load()
    return im.convert('RGB'), sha256(b)


def register(a, b, mask):
    """估計把 b 對齊到 a 的仿射轉換（OpenCV ECC），只用目標遮罩外（再外擴 40 px）的區域；回傳轉換後的 b 與矩陣。"""
    import cv2
    ga = np.asarray(a.convert('L'), np.float32) / 255
    gb = np.asarray(b.convert('L'), np.float32) / 255
    keep = (cv2.dilate((mask > 0.02).astype(np.uint8), np.ones((81, 81), np.uint8)) == 0).astype(np.uint8)
    M = np.eye(2, 3, dtype=np.float32)
    cc, M = cv2.findTransformECC(ga, gb, M, cv2.MOTION_AFFINE, (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 1e-6), keep, 5)
    w = cv2.warpAffine(np.asarray(b), M, (a.width, a.height), flags=cv2.INTER_LANCZOS4 + cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
    return Image.fromarray(w), M, float(cc), float(keep.mean())


def build_mask(size, region, x0, y0):
    m = Image.new('L', size, 0)
    d = ImageDraw.Draw(m)
    for poly in region['parts'].values():
        d.polygon([(x - x0, y - y0) for x, y in poly], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(region['feather_px'] / 2))
    return np.asarray(m, float) / 255


def changed(a, b):
    return np.abs(a.astype(int) - b.astype(int)).max(axis=2) > TOL


def face_crop(im, box, s=1.7):
    x0, y0, x1, y1 = box
    cx, cy, z = (x0 + x1) / 2, (y0 + y1) / 2, max(x1 - x0, y1 - y0) * s
    return im.crop((int(cx - z / 2), int(cy - z * 0.55), int(cx + z / 2), int(cy + z * 0.45)))


def label(im, text, h=36):
    W = Image.new('RGB', (im.width, im.height + h), (255, 255, 255))
    W.paste(im, (0, h))
    ImageDraw.Draw(W).text((6, h - 8), text, font=ImageFont.truetype(CJK_FONT, 22), fill=(30, 30, 34), anchor='ls')
    return W


def row(ims, gap=10):
    H = max(i.height for i in ims)
    out = Image.new('RGB', (sum(i.width for i in ims) + gap * (len(ims) - 1), H), (255, 255, 255))
    x = 0
    for i in ims:
        out.paste(i, (x, 0))
        x += i.width + gap
    return out


def build(raw_dir, edit_path, edit_sha, pub, data_path):
    if os.path.isdir(pub):
        shutil.rmtree(pub)
    os.makedirs(pub)
    R = json.load(open(os.path.join(ROOT, REGION), encoding='utf-8'))
    orig, _ = load(os.path.join(raw_dir, 'cover_H-A.png'), SRC_SHA)
    edit_raw, esha = load(edit_path, edit_sha)
    ref, _ = load(os.path.join(ROOT, REF), REF_SHA)
    x0, y0, x1, y1 = R['crop']
    cw, ch = x1 - x0, y1 - y0
    oc = orig.crop((x0, y0, x1, y1))
    ed = edit_raw.resize((cw, ch), Image.LANCZOS)
    mask = build_mask((cw, ch), R, x0, y0)
    ed, M, cc, keep_share = register(oc, ed, mask)   # 輸出比例不是精確 9:16，且模型可能微幅位移／縮放，回填前先對位
    O = np.asarray(oc).astype(float)
    E = np.asarray(ed).astype(float)
    comp_c = (O * (1 - mask[..., None]) + E * mask[..., None]).round().clip(0, 255).astype(np.uint8)
    result = orig.copy()
    result.paste(Image.fromarray(comp_c), (x0, y0))
    # 差異紀錄（原生像素）
    A, B = np.asarray(orig), np.asarray(result)
    ch_all = changed(A, B)
    inside = np.zeros(ch_all.shape, bool)
    inside[y0:y1, x0:x1] = True
    mfull = np.zeros(ch_all.shape)
    mfull[y0:y1, x0:x1] = mask
    diff = {
        'tolerance': f'任一通道差 > {TOL}（0–255）才算改動',
        'outside_crop_changed_px': int((ch_all & ~inside).sum()), 'outside_crop_px': int((~inside).sum()),
        'crop_outside_mask_changed_px': int((ch_all & inside & (mfull == 0)).sum()), 'crop_outside_mask_px': int((inside & (mfull == 0)).sum()),
        'mask_px': int((mfull > 0).sum()), 'mask_changed_px': int((ch_all & (mfull > 0)).sum()),
        'mask_share_of_image': round(float((mfull > 0).sum() / mfull.size), 5),
    }
    # 模型在遮罩外改了多少（沒有用到的像素，只記錄工具漂移）
    out_m = mask < 0.02
    dmean = np.abs(O - E).mean(axis=2)
    F = json.load(open(os.path.join(ROOT, BOXES), encoding='utf-8'))['covers']['H-A']['people']
    drift = {'crop_outside_mask_mean_abs_diff': round(float(dmean[out_m].mean()), 2),
             'crop_outside_mask_share_over_20': round(float((dmean[out_m] > 20).mean()), 4)}
    for pid in ('mia-huang', 'rainie-hsu'):
        bx = F[pid]['face']
        a, b = max(bx[0] - x0, 0), max(bx[1] - y0, 0)
        c, d = min(bx[2] - x0, cw), min(bx[3] - y0, ch)
        if c > a and d > b:
            drift[f'{pid}_face_mean_abs_diff_in_edit'] = round(float(dmean[b:d, a:c].mean()), 2)
    # 輸出
    files = {}

    def save(name, data):
        open(os.path.join(pub, name), 'wb').write(data)
        files[name] = sha256(data)
    vw = VIEW_W
    vh = round(orig.height * vw / orig.width)
    save('r28_before_f.jpg', jpeg(orig, 90))
    save('r28_after_f.jpg', jpeg(result, 90))
    save('r28_before_v.jpg', jpeg(orig.resize((vw, vh), Image.LANCZOS), 88))
    save('r28_after_v.jpg', jpeg(result.resize((vw, vh), Image.LANCZOS), 88))
    # 編輯範圍：原圖上的裁切框（藍）與遮罩範圍（紅）
    rv = orig.resize((vw, vh), Image.LANCZOS)
    dr = ImageDraw.Draw(rv)
    k = vw / orig.width
    dr.rectangle([x0 * k, y0 * k, x1 * k, y1 * k], outline=(29, 78, 216), width=3)
    for poly in R['parts'].values():
        dr.line([(x * k, y * k) for x, y in poly] + [(poly[0][0] * k, poly[0][1] * k)], fill=(200, 30, 30), width=3)
    save('r28_region_v.jpg', jpeg(rv, 88))
    # 裁切範圍前後
    save('r28_crop_before.jpg', jpeg(oc, 90))
    save('r28_crop_after.jpg', jpeg(Image.fromarray(comp_c), 90))
    # 臉部：身分基準｜原本｜結果
    fb = F['coco-wu']['face']
    T = 360
    fa = face_crop(orig, fb).resize((T, T), Image.LANCZOS)
    fr = face_crop(result, fb).resize((T, T), Image.LANCZOS)
    rbox = json.load(open(os.path.join(ROOT, 'review/calendar/m5_r27/face_boxes.json'), encoding='utf-8'))['refs']['coco-wu']
    rf = ref.crop(tuple(rbox)).resize((T, T), Image.LANCZOS)
    save('r28_face_cmp.jpg', jpeg(row([label(rf, '身分基準（Coco）'), label(fa, 'R27 原本'), label(fr, 'R28 結果')]), 90))
    # 差異圖：全圖改動的像素（白＝有改動）
    dm = Image.fromarray((ch_all * 255).astype(np.uint8)).resize((vw, vh), Image.BOX)
    save('r28_diff_v.jpg', jpeg(Image.merge('RGB', (dm, dm, dm)), 88))
    out = []
    for name, h in sorted(files.items()):
        im = Image.open(os.path.join(pub, name))
        out.append({'path': name, 'sha256': h, 'px': [im.width, im.height], 'bytes': os.path.getsize(os.path.join(pub, name))})
    D = {'round': ROUND,
         'note': 'H-A 裡 Coco 的單人身分校正測試（裁切編輯→只在 Coco 本人範圍回填同一張照片）。不是完成的封面，也不代表 Penny 接受 H-A。',
         'source_sha256': SRC_SHA, 'edit_sha256': esha, 'edit_px': list(edit_raw.size), 'crop': R['crop'], 'crop_px': [cw, ch],
         'parts': R['parts'], 'feather_px': R['feather_px'],
         'alignment': {'method': 'OpenCV ECC 仿射對位（只看目標遮罩外擴 40 px 以外的區域）', 'matrix': [[round(float(v), 5) for v in r] for r in M],
                       'correlation': round(cc, 4), 'region_used_share': round(keep_share, 3)},
         'diff': diff, 'model_drift_unused': drift,
         'files': out}
    with open(data_path, 'w', encoding='utf-8') as fh:
        json.dump(D, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    return D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw-dir', required=True)
    ap.add_argument('--edit', required=True)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.check:
        old = json.load(open(os.path.join(ROOT, DATA_REL), encoding='utf-8'))
        with tempfile.TemporaryDirectory() as tmp:
            assert old['edit_sha256'] == EDIT_SHA
            D = build(a.raw_dir, a.edit, EDIT_SHA, os.path.join(tmp, 'p'), os.path.join(tmp, 'd.json'))
            same = json.loads(json.dumps(D, ensure_ascii=False)) == old
            pub = os.path.join(ROOT, PUB_REL)
            diff = [x['path'] for x in D['files'] if not os.path.exists(os.path.join(pub, x['path'])) or sha256(open(os.path.join(pub, x['path']), 'rb').read()) != x['sha256']]
            extra = sorted(set(os.listdir(pub)) - {x['path'] for x in D['files']})
        ok = same and not diff and not extra
        print(json.dumps({'check': 'PASS' if ok else 'FAIL', 'data_same': same, 'files': len(D['files']), 'diff': diff, 'extra': extra}, ensure_ascii=False))
        sys.exit(0 if ok else 1)
    D = build(a.raw_dir, a.edit, EDIT_SHA, os.path.join(ROOT, PUB_REL), os.path.join(ROOT, DATA_REL))
    print(json.dumps({k: D[k] for k in ('edit_px', 'alignment', 'diff', 'model_drift_unused')}, ensure_ascii=False, indent=1))
    print('files', len(D['files']), round(sum(x['bytes'] for x in D['files']) / 1048576, 1), 'MB')


if __name__ == '__main__':
    main()
