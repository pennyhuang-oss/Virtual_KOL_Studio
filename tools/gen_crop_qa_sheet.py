#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生人工 QA 印樣：每個來源一列、四槽並排，標出 QA 狀態與理由。

ChatGPT J-02.5：由程式產生，人只做 QA。這是給人看的那一張。
"""
import json, sys
from PIL import Image, ImageDraw

M = json.load(open('pilot/face_crops_manifest.json', encoding='utf-8'))
A = M['artifacts']
V = M['crop_spec_version']
SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
OUT = sys.argv[1] if len(sys.argv) > 1 else 'review/batch3_crop_qa_sheet.jpg'
only_pass = '--pass-only' in sys.argv

refs = sorted({a['source_ref_id'] for a in A.values()})
CW, RH, PAD = 300, 250, 8
rows = []
for r in refs:
    cells = []
    for s in SL:
        k = f'{r}__{s}__{V}'
        cells.append(A.get(k))
    if only_pass and not any(c and c['qa_status'] != 'fail' for c in cells):
        continue
    rows.append((r, cells))

W = CW * 4 + 120
H = RH * len(rows) + 40
canvas = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(canvas)
d.text((10, 12), f'部件裁切 QA 印樣 · crop_spec {V} · 綠=pass 紅=fail', fill='black')
for j, (r, cells) in enumerate(rows):
    y = 40 + j * RH
    d.text((8, y + RH // 2), r, fill='black')
    for i, c in enumerate(cells):
        x = 110 + i * CW
        if not c:
            d.rectangle([x, y + 4, x + CW - PAD, y + RH - PAD], outline=(200, 200, 200))
            d.text((x + 8, y + RH // 2), '（未產生）', fill=(150, 150, 150))
            continue
        im = Image.open(c['out_path']).convert('RGB')
        im.thumbnail((CW - PAD * 2, RH - 34))
        canvas.paste(im, (x + PAD, y + 22))
        ok = c['qa_status'] != 'fail'
        col = (30, 120, 60) if ok else (170, 40, 30)
        d.rectangle([x + 2, y + 2, x + CW - PAD, y + RH - PAD], outline=col, width=2)
        d.text((x + 6, y + 6), f"{SL[i][:12]} {c['qa_status']}", fill=col)
        if not ok:
            d.text((x + 6, y + RH - 16), c['qa_reasons'][0][:36], fill=col)
canvas.save(OUT, quality=88)
print(f'{OUT}  {canvas.size}  {len(rows)} 列')
