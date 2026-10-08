"""2027 日期渲染：資料只來自人事總處 116 年辦公日曆表（data/cal_r2_official_2027_dgpa.json）。
紅字＝官方「放假日」（含週末、國定假日、補假）；不加農曆（是否加農曆待 Penny 決定，見 CAL_08）。"""
import calendar
import datetime as dt
import json
import os

from PIL import Image, ImageDraw, ImageFont

CAL = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OFF = {d['date']: d for d in json.load(open(os.path.join(CAL, 'data', 'cal_r2_official_2027_dgpa.json')))['days']}
EN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
FONT_CJK = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
FONT_LAT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_LAT_B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
RED = (200, 30, 40)
INK = (40, 40, 45)
MUTED = (120, 120, 125)


def f(path, size):
    return ImageFont.truetype(path, max(6, int(size)))


def is_off(y, m, d):
    return OFF[f'{y}-{m:02d}-{d:02d}']['off']


def weeks(y, m):
    c = calendar.Calendar(firstweekday=6)  # Sunday first, as the official table
    return c.monthdayscalendar(y, m)


def draw_grid(draw, box, y, m, px_per_mm, title=True, lunar=False, header='zh'):
    """大格月曆，畫在 box=(x0,y0,x1,y1) 像素範圍內。"""
    x0, y0, x1, y1 = box
    W, H = x1 - x0, y1 - y0
    mm = px_per_mm
    top = y0
    if title:
        draw.text((x0, top), f'{m:02d}', fill=INK, font=f(FONT_LAT_B, 14 * mm))
        draw.text((x0 + 22 * mm, top + 6.5 * mm), f'{EN[m - 1]} 2027', fill=MUTED, font=f(FONT_LAT, 5.2 * mm))
        top += 19 * mm
    heads = ['日', '一', '二', '三', '四', '五', '六'] if header == 'zh' else ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    cw = W / 7
    for k, hname in enumerate(heads):
        draw.text((x0 + k * cw + cw * 0.12, top), hname, fill=RED if k in (0, 6) else MUTED, font=f(FONT_CJK, 3.6 * mm))
    top += 6.5 * mm
    draw.line((x0, top - 1.2 * mm, x1, top - 1.2 * mm), fill=(200, 200, 205), width=max(1, int(0.25 * mm)))
    wk = weeks(y, m)
    rh = (y1 - top) / len(wk)
    for r, week in enumerate(wk):
        for k, d in enumerate(week):
            if not d:
                continue
            col = RED if is_off(y, m, d) else INK
            draw.text((x0 + k * cw + cw * 0.12, top + r * rh + rh * 0.08), str(d), fill=col, font=f(FONT_LAT, min(rh * 0.42, cw * 0.42)))
            if lunar:
                draw.text((x0 + k * cw + cw * 0.12, top + r * rh + rh * 0.58), OFF[f'{y}-{m:02d}-{d:02d}']['lunar_label'][:4],
                          fill=col, font=f(FONT_CJK, min(rh * 0.2, cw * 0.2)))


def draw_strip(draw, box, y, m, px_per_mm):
    """單行日期條：星期在上、日期在下，兩行。"""
    x0, y0, x1, y1 = box
    n = calendar.monthrange(y, m)[1]
    cw = (x1 - x0) / n
    fs = min(cw * 0.64, (y1 - y0) * 0.34)
    for d in range(1, n + 1):
        dow = (dt.date(y, m, d).weekday() + 1) % 7
        col = RED if is_off(y, m, d) else INK
        cx = x0 + (d - 0.5) * cw
        w1 = '日一二三四五六'[dow]
        draw.text((cx, y0 + (y1 - y0) * 0.18), w1, fill=col, font=f(FONT_CJK, fs * 0.8), anchor='mm')
        draw.text((cx, y0 + (y1 - y0) * 0.62), str(d), fill=col, font=f(FONT_LAT, fs), anchor='mm')


def reference_month(y, m, w=900, h=700):
    im = Image.new('RGB', (w, h), 'white')
    d = ImageDraw.Draw(im)
    draw_grid(d, (30, 20, w - 30, h - 20), y, m, px_per_mm=w / 160, lunar=True)
    return im
