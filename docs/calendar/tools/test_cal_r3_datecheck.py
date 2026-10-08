#!/usr/bin/env python3
"""TASK-CAL-001 / R3 — 日期輸出核對的負向測試：故意改壞一張輸出頁，確認核對程式會抓到。

把 H_A_01（2027 年 1 月）的 300 dpi 輸出複製到暫存資料夾後：1/4 改成紅字、1/15 擦掉、1/10 改寫成 9。
預期核對報出這三格、且只報這三格。不改 repo 內任何檔案。
用法：python3 docs/calendar/tools/test_cal_r3_datecheck.py
"""
import json
import os
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(__file__))
import build_cal_r3_pages as B  # noqa: E402


def main():
    rep = next(p for p in json.load(open(os.path.join(B.CAL, 'data', 'cal_r3_layout_report.json')))['pages'] if p['id'] == 'H_A_01_iris-chen')
    L = rep['lattices'][0]
    x0, y0, x1, y1 = L['box']
    cw, rh, hh = (x1 - x0) / 7, (y1 - y0 - L['head_h']) / 6, L['head_h']

    def cell(r, k):
        return B.px(x0 + k * cw), B.px(y0 + hh + r * rh), B.px(x0 + (k + 1) * cw), B.px(y0 + hh + (r + 1) * rh)
    a = np.asarray(Image.open(os.path.join(B.CAL, rep['hires'])).convert('RGB')).copy()
    X0, Y0, X1, Y1 = cell(1, 1)  # 1/4（一）
    sub = a[Y0:Y1, X0:X1]
    sub[sub.min(-1) < 140] = B.RED
    X0, Y0, X1, Y1 = cell(2, 5)  # 1/15（五）
    a[Y0:Y1, X0:X1] = 255
    X0, Y0, X1, Y1 = cell(2, 0)  # 1/10（日）
    a[Y0:Y1, X0:X1] = 255
    im = Image.fromarray(a)
    ImageDraw.Draw(im).text(((X0 + X1) // 2, (Y0 + Y1) // 2), '9', fill=B.RED, font=B.font(B.FONT_LAT, L['digit_mm']), anchor='mm')
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, 'corrupt.jpg')
        im.save(p, quality=90)
        r = B.verify_dates(rep, p)
    got = sorted(f['cell'] for f in r['failures'])
    assert got == ['r1c1', 'r2c0', 'r2c5'], got
    print('ok: 三處錯誤都抓到，沒有誤報', got)


if __name__ == '__main__':
    main()
