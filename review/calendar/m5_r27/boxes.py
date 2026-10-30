"""M-5 R27：把逐人臉框定下來，存成 face_boxes.json，讓封面排版工具（build_cal_m5_cover.py）不用再跑偵測就能重現。
- refs：身分參考圖的臉部裁切框（mediapipe 臉部特徵點範圍 ×1.7，與 idsheet.py 相同）
- covers：封面原圖上每位的臉框（faces_auto 自動偵測＋faces_assign 人工指派／補框）與對照用裁切框
只讀像素、不改圖；不含任何平台 ID。用法：python3 -I review/calendar/m5_r27/boxes.py"""
import json
import os
import sys

ROOT = '/home/user/Virtual_KOL_Studio'
D = f'{ROOT}/review/calendar/m5_r27'
sys.path.insert(0, f'{ROOT}/docs/calendar/tools')
from cal_face_lib import landmarks  # noqa: E402

R = json.load(open(f'{D}/refs.json'))['refs']
AUTO = json.load(open(f'{D}/faces_auto.json'))
ASSIGN = json.load(open(f'{D}/faces_assign.json'))


def sq(x0, y0, x1, y1):
    cx, cy, s = (x0 + x1) / 2, (y0 + y1) / 2, max(x1 - x0, y1 - y0) * 1.7
    return [int(cx - s / 2), int(cy - s * 0.55), int(cx + s / 2), int(cy + s * 0.45)]


def face(c, who):
    a = ASSIGN[c][who]
    if 'auto' in a:
        return [int(v) for v in AUTO[c]['faces'][a['auto']]], 'auto'
    cx, cy, w = a['manual']
    return [int(cx - w / 2), int(cy - w * 0.6), int(cx + w / 2), int(cy + w * 0.6)], 'manual'


out = {'note': '臉框（像素，原圖座標）。refs＝身分參考圖裁切框；covers＝封面原圖臉框 face 與對照裁切框 crop；source＝auto（自動偵測）或 manual（側臉／遮擋時人工補框）。',
       'refs': {}, 'covers': {}}
for r in R:
    P, _ = landmarks(f'{ROOT}/{r["file"]}')
    x0, y0 = P.min(0)
    x1, y1 = P.max(0)
    out['refs'][r['set']] = sq(x0, y0, x1, y1)
for c in ('H-A', 'H-B', 'V-A', 'V-B'):
    assert sorted(ASSIGN[c]) == sorted(r['set'] for r in R), c
    autos = [a['auto'] for a in ASSIGN[c].values() if 'auto' in a]
    assert len(autos) == len(set(autos)) == len(AUTO[c]['faces']), f'{c}：每個自動偵測的臉都指派給一個人、沒有重複'
    out['covers'][c] = {'size': AUTO[c]['size'], 'people': {}}
    for r in R:
        f, src = face(c, r['set'])
        out['covers'][c]['people'][r['set']] = {'face': f, 'crop': sq(*f), 'source': src}
json.dump(out, open(f'{D}/face_boxes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print({c: sum(v['source'] == 'manual' for v in out['covers'][c]['people'].values()) for c in out['covers']})
