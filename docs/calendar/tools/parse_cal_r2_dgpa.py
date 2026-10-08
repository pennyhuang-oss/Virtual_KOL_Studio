#!/usr/bin/env python3
"""TASK-CAL-001 / R2 — 解析人事總處《116 年政府行政機關辦公日曆表》xlsx → data/cal_r2_official_2027_dgpa.json。

表的版面：每一段以「日 一 二 三 四 五 六」星期列開頭，橫向每 7 欄是一個月；之後一列日期、一列農曆／節氣字樣交替。
放假日＝儲存格底色 FFFF99FF（官方表的放假底色）。
驗證：每天的欄位星期必須等於 Python datetime 的星期；365 天不缺不重。
用法：python3 docs/calendar/tools/parse_cal_r2_dgpa.py
"""
import datetime as dt
import json
import os
import unicodedata

import openpyxl

CAL = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC = os.path.join(CAL, 'data', 'sources', 'dgpa_116_calendar_downloaded_2026-10-08.xlsx')
OUT = os.path.join(CAL, 'data', 'cal_r2_official_2027_dgpa.json')
WEEK = '日一二三四五六'
OFF_FILL = 'FFFF99FF'


def norm(v):
    """表頭有相容字（例：第一段的「六」是 U+F9D1），先做 NFKC 再比對。"""
    return unicodedata.normalize('NFKC', v) if isinstance(v, str) else v


def main():
    ws = openpyxl.load_workbook(SRC).active
    rows = list(ws.iter_rows())
    heads = [i for i, r in enumerate(rows) if [norm(c.value) for c in r[1:8]] == list(WEEK)]
    days, month = [], 0
    for bi, h in enumerate(heads):
        end = heads[bi + 1] - 1 if bi + 1 < len(heads) else len(rows)
        ncol = len(rows[h])
        for c0 in range(1, ncol - 6, 7):
            if [norm(rows[h][c0 + k].value) for k in range(7)] != list(WEEK):
                continue
            month += 1
            for r in range(h + 1, end, 2):
                for k in range(7):
                    cell = rows[r][c0 + k]
                    if not isinstance(cell.value, int):
                        continue
                    d = dt.date(2027, month, cell.value)
                    assert WEEK[(d.weekday() + 1) % 7] == WEEK[k], d
                    lab = rows[r + 1][c0 + k].value if r + 1 < len(rows) else ''
                    off = bool(cell.fill and cell.fill.fill_type and cell.fill.fgColor.rgb == OFF_FILL)
                    days.append({'date': d.isoformat(), 'dow': WEEK[k], 'lunar_label': (lab or '').replace('\n', '／'), 'off': off})
    days.sort(key=lambda x: x['date'])
    assert len(days) == 365 and len({x['date'] for x in days}) == 365, len(days)
    json.dump({'source': '行政院人事行政總處《中華民國116年（西元2027年）政府行政機關辦公日曆表》xlsx'
                         '（https://www.dgpa.gov.tw/information?uid=30&pid=12982），下載 2026-10-08',
               'days': days}, open(OUT, 'w'), ensure_ascii=False, indent=1)
    print('ok', len(days), 'off', sum(x['off'] for x in days))


if __name__ == '__main__':
    main()
