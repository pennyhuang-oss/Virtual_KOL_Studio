"""M-5 R27：逐人身分對照圖（左＝送入的身分參考臉、右＝封面上的臉，原圖像素只裁切與等比縮放）。人工判讀用，不改圖。"""
import json
import os
import sys

from PIL import Image, ImageDraw

ROOT = '/home/user/Virtual_KOL_Studio'
R = json.load(open(f'{ROOT}/review/calendar/m5_r27/refs.json'))['refs']
AUTO = json.load(open(f'{ROOT}/review/calendar/m5_r27/faces_auto.json'))
# 臉框指派（依畫面目視；auto＝自動偵測序號，manual＝人工補框 [cx, cy, w]）
ASSIGN = json.load(open(f'{ROOT}/review/calendar/m5_r27/faces_assign.json'))


def face_box(c, who):
    a = ASSIGN[c][who]
    if 'auto' in a:
        x0, y0, x1, y1 = AUTO[c]['faces'][a['auto']]
    else:
        cx, cy, w = a['manual']
        x0, y0, x1, y1 = cx - w / 2, cy - w * 0.6, cx + w / 2, cy + w * 0.6
    cx, cy, w, h = (x0 + x1) / 2, (y0 + y1) / 2, x1 - x0, y1 - y0
    s = max(w, h) * 1.7
    return [int(cx - s / 2), int(cy - s * 0.55), int(cx + s / 2), int(cy + s * 0.45)]


def ref_face(r):
    sys.path.insert(0, f'{ROOT}/docs/calendar/tools')
    from cal_face_lib import landmarks
    P, _ = landmarks(f'{ROOT}/{r["file"]}')
    x0, y0 = P.min(0)
    x1, y1 = P.max(0)
    cx, cy, s = (x0 + x1) / 2, (y0 + y1) / 2, max(x1 - x0, y1 - y0) * 1.7
    return Image.open(f'{ROOT}/{r["file"]}').convert('RGB').crop((int(cx - s / 2), int(cy - s * 0.55), int(cx + s / 2), int(cy + s * 0.45)))


def sheet(c, out, raw_dir):
    im = Image.open(os.path.join(raw_dir, f'cover_{c}.png')).convert('RGB')
    T = 300
    cols = 3
    W = cols * (2 * T + 30)
    rows = (len(R) + cols - 1) // cols
    S = Image.new('RGB', (W, rows * (T + 28)), 'white')
    d = ImageDraw.Draw(S)
    for i, r in enumerate(R):
        x, y = (i % cols) * (2 * T + 30), (i // cols) * (T + 28)
        a = ref_face(r).resize((T, T))
        b = im.crop(face_box(c, r['set'])).resize((T, T), Image.LANCZOS)
        S.paste(a, (x, y + 24))
        S.paste(b, (x + T + 4, y + 24))
        bw = face_box(c, r['set'])
        d.text((x + 4, y + 4), f"{r['image_no']} {r['name']} | ref  vs  {c} (face {bw[2]-bw[0]}px box)", fill=(0, 0, 0))
    S.save(out, quality=88)


if __name__ == '__main__':
    # 用法：python3 -I idsheet.py <輸出資料夾> <原圖資料夾（私有，不進 git）> H-A H-B V-A V-B（公開版對照圖改由 build_cal_m5_cover.py 產生）
    for c in sys.argv[3:]:
        sheet(c, os.path.join(sys.argv[1], f'idsheet_{c}.jpg'), sys.argv[2])
