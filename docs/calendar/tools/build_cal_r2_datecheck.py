#!/usr/bin/env python3
"""TASK-CAL-001 / R2 — 廠商 2027 日期素材 vs 人事總處 116 年辦公日曆表，逐月並排比對圖。

每列：官方參考（由 DGPA xlsx 現算，紅＝放假日，小字＝官方表上的農曆／節氣字樣）｜廠商橫式大日期-正面滿版｜
廠商範本小月曆（祥羊迎春範本同頁的前後月小月曆）｜廠商直式大日期｜廠商橫式大日期-背面。
判讀是目視（理由：素材是點陣字，OCR 與幾何偵測都漏字，見 CAL_08 §方法）。
用法：python3 docs/calendar/tools/build_cal_r2_datecheck.py <廠商素材資料夾>
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(__file__))
from cal_dates import CAL, f, FONT_CJK, reference_month  # noqa: E402

OUT = os.path.join(CAL, 'r2', 'dates')


def flat(path, maxw):
    im = Image.open(path).convert('RGBA')
    a = np.asarray(im)[:, :, 3]
    ys, xs = np.where(a > 10)
    if len(xs):
        im = im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255))
    im = Image.alpha_composite(bg, im).convert('RGB')
    im.thumbnail((maxw, maxw))
    return im


def cell(im, label, w):
    c = Image.new('RGB', (w, im.height + 30), 'white')
    c.paste(im, (0, 30))
    ImageDraw.Draw(c).text((4, 4), label, fill='black', font=f(FONT_CJK, 18))
    return c


def main():
    vd = sys.argv[1]
    os.makedirs(OUT, exist_ok=True)
    W = 520
    rows = []
    for m in range(1, 13):
        cells = [cell(reference_month(2027, m, 900, 700).resize((W, int(W * 700 / 900))), f'{m} 月｜官方（DGPA）', W)]
        for tag, name in (('Hfull', f'Hfull_2027{m:02d}_0.png'), ('tplmini', f'tpl8385_m{m:02d}_1.png'),
                          ('Vbig', f'Vbig_2027{m:02d}_0.png'), ('Hback', f'Hback_2027{m:02d}_0.png')):
            p = os.path.join(vd, name)
            lab = {'Hfull': '廠商｜橫式大日期-正面滿版', 'tplmini': '廠商｜範本小月曆（前月／次月）',
                   'Vbig': '廠商｜直式大日期', 'Hback': '廠商｜橫式大日期-背面'}[tag]
            if os.path.exists(p):
                cells.append(cell(flat(p, W if tag != 'Vbig' else int(W * 0.75)), lab, W))
        h = max(c.height for c in cells)
        row = Image.new('RGB', (sum(c.width + 6 for c in cells), h), '#ddd')
        x = 0
        for c in cells:
            row.paste(c, (x, 0))
            x += c.width + 6
        rows.append(row)
    for i in range(0, 12, 2):
        pair = rows[i:i + 2]
        S = Image.new('RGB', (max(r.width for r in pair), sum(r.height + 10 for r in pair)), '#999')
        y = 0
        for r in pair:
            S.paste(r, (0, y))
            y += r.height + 10
        hi = os.path.join(OUT, f'CAL_R2_datecheck_{i + 1:02d}-{i + 2:02d}_hires.jpg')
        S.save(hi, quality=90)
        S.thumbnail((2000, 2000))
        S.save(hi.replace('_hires', ''), quality=82)
    # 全年年曆
    yr = [cell(flat(os.path.join(vd, n), 1300), lab, 1300) for n, lab in
          (('Hyear_202712_0.png', '廠商｜橫式年曆 2027'), ('Vyear_202712_0.png', '廠商｜直式年曆 2027'),
           ('Vbig_直式桌曆_年曆2027_0.png', '廠商｜直式大日期-年曆 2027')) if os.path.exists(os.path.join(vd, n))]
    for k, c in enumerate(yr, 1):
        c.save(os.path.join(OUT, f'CAL_R2_vendor_year_{k}.jpg'), quality=85)
    print('ok')


if __name__ == '__main__':
    main()
