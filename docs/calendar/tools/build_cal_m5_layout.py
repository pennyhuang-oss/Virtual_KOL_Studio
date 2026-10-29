#!/usr/bin/env python3
"""TASK-CAL-001／M-5 R26 — 兩款桌曆排版預覽（工作版；非交印核准、未經廠商確認）。

照片：唯一來源 docs/calendar/data/cal_m4_final_r25.json（成果 commit 62b87c0）的 24 張定案圖；每張從記錄的 commit 讀原檔、核對 sha256，
      以原生像素放進 PDF（JPEG q95、4:4:4，不帶中繼資料；不放大、不改 dpi 標記、不調色）。封面小圖只縮小。
頁序：廠商 2027 範本（CAL_01 §3.2）＋CAL_10 §4「照片面在前、大格面在後」：
      橫式 28 面＝封面、12 個月 ×（照片面＋大格面）、MEMO ×2、條碼頁；直式 32 面＝封面、12 個月 × 2、MEMO ×5、全年年曆、條碼頁。
      紙張正反面拼版、背面是否旋轉未經廠商確認：PDF 一律單面正向逐面排列，不自行旋轉。
日期：只用人事總處 116 年辦公日曆表（data/cal_r2_official_2027_dgpa.json）；紅字＝表上放假日（含週末與補假）；週日起始；不加農曆與節日名稱。
      產生後把 PDF 以 300 dpi 點陣化，依格線幾何逐格讀回字形與顏色，與另行推算的期望值比對（不是只核對輸入資料）。
橫式照片框：推薦「完整 16:9（192×108 mm，不裁切）」；另做 R6 接受的 192×104 mm 套框版本供比較（裁切位置依實圖判讀，見 H_EDGE）。

用法：python3 docs/calendar/tools/build_cal_m5_layout.py            # 產生 PDF、頁面圖、比較圖與資料
      python3 docs/calendar/tools/build_cal_m5_layout.py --check    # 重建到暫存資料夾，逐檔比對 sha256（含日期讀回核對）
"""
import argparse
import calendar
import datetime as dt
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageFont
from reportlab import rl_config
from reportlab.lib.units import mm as MMPT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cal_seg import categories  # noqa: E402

ROUND = 'M-5 R26'
FINAL_FILE = 'docs/calendar/data/cal_m4_final_r25.json'
FINAL_COMMIT = '62b87c00802efabc67ab57d46edae1f1d6bdccbb'   # R25 成果 commit：唯一定案清單
DGPA_FILE = 'docs/calendar/data/cal_r2_official_2027_dgpa.json'
PUB_REL = 'docs/calendar/decision_site/public/layout'
DATA_REL = 'docs/calendar/data/cal_m5_layout_r26.json'
DOC_REL = 'docs/calendar/CAL_28_M5_R26_LAYOUT.generated.md'
DPI = 300
VIEW_DPI = 150
PT = 72 / 25.4   # 每 mm 的 pt

FONTS = {  # 名稱：(檔案, TTC 索引)。預覽用開放授權字型（可嵌入）；正式字型未定。
    'CJK': ('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 0),
    'LAT': ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 0),
    'LATB': ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 0),
}
FONT_NOTE = '預覽用字型：中文 文泉驛正黑（WenQuanYi Zen Hei）、數字與英文 DejaVu Sans／Sans Bold；皆為開放授權、已嵌入 PDF（子集）。正式字型未定。'
INK, MUTED, RED, LINE = (0.13, 0.13, 0.15), (0.45, 0.45, 0.48), (0.77, 0.12, 0.16), (0.80, 0.80, 0.82)
EN = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
WEEK = '日一二三四五六'   # 週日起始（台灣慣例；廠商台灣日期素材同樣週日起始，CAL_01 §4）
HOLIDAY_NOTE = '紅字＝行政院人事行政總處 116 年辦公日曆表放假日（含週末與補假）'
BRAND = '［品牌名稱 佔位］'

# 幾何（含 2 mm 出血的畫布座標，mm，左上為原點）
FMT = {
    'H': {'zh': '橫式', 'sku': 'YFP-CA01', 'W': 204, 'H': 155, 'faces': 28, 'trim': 2,
          'vendor_safe': (4, 12, 200, 151), 'text_safe': (4, 12, 200, 151),
          'text_safe_note': '廠商編輯器安全框（裁切線內上 10、其餘 2 mm）',
          'coil_assumed': 12, 'coil_measured': 8.9,
          'photo': {'B': (6, 14, 198, 122), 'A': (6, 14, 198, 118)}},
    'V': {'zh': '直式', 'sku': 'YFP-CA08', 'W': 144, 'H': 204, 'faces': 32, 'trim': 2,
          'vendor_safe': (2, 2, 142, 202), 'text_safe': (5, 12, 139, 199),
          'text_safe_note': '廠商安全框為 0；本案自訂文字安全區：裁切線內 3 mm、上緣避開 12 mm 線圈假設區',
          'coil_assumed': 12, 'coil_measured': 9.7,
          'photo': {'V': (12, 16, 132, 176)}},
}
NEED_H = 43   # 2048×1152 放入 192×104：高度 1152 − round(2048 × 104 / 192)＝43 px

# 橫式 12 張下緣的實圖判讀（R26 逐張看原尺寸下緣 160 列）：cut＝人物在原圖下緣已被截斷（Owner 已接受的原圖構圖，不重開）；whole＝腳與鞋底完整在畫面內
H_EDGE = {
    'H-yuna-kim': ('cut', '靴子在原圖下緣已被截斷'),
    'H-rin-ayase': ('whole', '斜躺在沙發上，腳在畫面內、下方空間充足'),
    'H-miu-shiraishi': ('cut', '趴在床上，枕頭與身體在原圖下緣已被截斷'),
    'H-tammy-chou': ('cut', '跪姿的腿在原圖下緣已被截斷'),
    'H-yerin-han': ('whole', '坐姿，球鞋完整在畫面內'),
    'H-coco-wu': ('cut', '膝蓋以下與草帽在原圖下緣已被截斷'),
    'H-mia-huang': ('whole', '坐在沙灘，赤腳完整在畫面內'),
    'H-iris-chen': ('cut', '雙腳在原圖下緣已被截斷'),
    'H-jia-seo': ('whole', '坐姿，涼鞋完整在畫面內'),
    'H-luna-tanaka': ('cut', '前腳完整；後腳在原圖下緣已被截掉一部分'),
    'H-somi-oh': ('cut', '靴子在原圖下緣已被截斷（R25 記的「下方約 6.7% 空間」有誤：分割遮罩漏了靴底）'),
    'H-rainie-hsu': ('whole', '站姿，涼鞋鞋底離原圖下緣約 5 px'),
}
KEEP_TOP = 33   # 套框時髮頂上方至少留 3%（33 px／1109 px），沿用企劃規則（cal_m3_shoot_plan.json printing.rules）
RAINIE_ALT = 'H-rainie-hsu'   # 只有這張在 192×104 框內放不下完整人物（上下空白合計 41 px < 43 px）


# ---------- 基本工具 ----------
def git(*a, binary=False):
    return subprocess.check_output(['git', '-C', ROOT, *a], text=not binary)


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def jpeg_bytes(im, q, sub=0):
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=q, subsampling=sub, optimize=False)
    return b.getvalue()


_PIL = {}


def pil_font(name, px):
    k = (name, px)
    if k not in _PIL:
        _PIL[k] = ImageFont.truetype(FONTS[name][0], px, index=FONTS[name][1])
    return _PIL[k]


_MET = {}


def ink_box(name, s):
    """字串的墨跡範圍（以字級 em 為單位；x 從起點、y 從基線往下為正）。"""
    k = (name, s)
    if k not in _MET:
        b = pil_font(name, 1000).getbbox(s, anchor='ls')
        _MET[k] = tuple(v / 1000 for v in b)
    return _MET[k]


def register_fonts():
    rl_config.useA85 = 0   # 影像串流不另做 ASCII85 編碼（JPEG 原樣嵌入，檔案較小）
    for n, (p, i) in FONTS.items():
        if n not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(n, p, subfontIndex=i))


# ---------- 頁面 ----------
class Doc:
    def __init__(self, kind, path, title):
        self.kind, self.f = kind, FMT[kind]
        self.W, self.H = self.f['W'], self.f['H']
        self.c = rl_canvas.Canvas(path, pagesize=(self.W * MMPT, self.H * MMPT), invariant=1, pageCompression=1,
                                  initialFontName='LAT', initialFontSize=8)
        t = self.f['trim']
        self.c.setTrimBox((t * MMPT, t * MMPT, (self.W - t) * MMPT, (self.H - t) * MMPT))
        self.c.setBleedBox((0, 0, self.W * MMPT, self.H * MMPT))
        self.c.setTitle(title)
        self.c.setSubject('版面預覽｜非交印核准｜未經廠商確認｜工作版（TASK-CAL-001 M-5 R26）')
        self.c.setAuthor('Virtual KOL Studio')
        self.c.setCreator('docs/calendar/tools/build_cal_m5_layout.py')
        self.c.setKeywords('preview only; not approved for print; vendor specs unconfirmed')
        self.pages = []


class Page:
    def __init__(self, doc, face, role, month=None, sid=None, variant=None):
        self.doc, self.face, self.role, self.month, self.sid, self.variant = doc, face, role, month, sid, variant
        self.texts, self.photos, self.lattices = [], [], []

    @property
    def c(self):
        return self.doc.c

    def Y(self, y):
        return (self.doc.H - y) * MMPT

    def text(self, x, y, s, font, em, color=INK, ha='l', va='base', role='text'):
        """x, y：mm；va＝base（y 為基線）／mid（y 為墨跡中心）／top（y 為墨跡上緣）；ha＝l／c／r（依字寬）。"""
        b = ink_box(font, s)
        base = y if va == 'base' else (y - (b[1] + b[3]) / 2 * em if va == 'mid' else y - b[1] * em)
        adv = pdfmetrics.stringWidth(s, font, 1.0) * em
        x0 = x - adv / 2 if ha == 'c' else (x - adv if ha == 'r' else x)
        self.c.setFillColorRGB(*color)
        self.c.setFont(font, em * PT)
        self.c.drawString(x0 * MMPT, self.Y(base), s)
        bbox = [round(x0 + b[0] * em, 3), round(base + b[1] * em, 3), round(x0 + b[2] * em, 3), round(base + b[3] * em, 3)]
        self.texts.append({'text': s, 'role': role, 'font': font, 'em_mm': em, 'em_pt': round(em * PT, 2), 'bbox_mm': bbox,
                           'red': color == RED})
        return adv, bbox

    def line(self, x0, y0, x1, y1, w=0.35, color=LINE):
        self.c.setStrokeColorRGB(*color)
        self.c.setLineWidth(w)
        self.c.line(x0 * MMPT, self.Y(y0), x1 * MMPT, self.Y(y1))

    def rect(self, x0, y0, x1, y1, fill=None, stroke=None, w=0.35, dash=None):
        if fill:
            self.c.setFillColorRGB(*fill)
        if stroke:
            self.c.setStrokeColorRGB(*stroke)
            self.c.setLineWidth(w)
        self.c.setDash(*(dash or ([], 0)))
        self.c.rect(x0 * MMPT, self.Y(y1), (x1 - x0) * MMPT, (y1 - y0) * MMPT, fill=1 if fill else 0, stroke=1 if stroke else 0)
        self.c.setDash([], 0)

    def image(self, path, box, rec):
        x0, y0, x1, y1 = box
        # 以工作資料夾內的檔名嵌入：reportlab 用檔名產生影像物件名稱，用完整暫存路徑會讓每次重建的 PDF 位元組不同
        assert os.path.realpath(os.path.dirname(path)) == os.path.realpath(os.getcwd())
        self.c.drawImage(os.path.basename(path), x0 * MMPT, self.Y(y1), (x1 - x0) * MMPT, (y1 - y0) * MMPT)
        self.photos.append({'box_mm': list(box), **rec})

    def marker(self):
        f = self.doc.f
        em = 1.7 if self.doc.kind == 'H' else 1.45
        right = 198 if self.doc.kind == 'H' else (132 if self.role == 'photo' else 136)
        y = f['text_safe'][3] - 0.6
        self.text(right, y, f'版面預覽 R26｜非交印核准｜面 {self.face}／{f["faces"]}', 'CJK', em, MUTED, 'r', 'base', 'marker')

    def finish(self):
        self.marker()
        self.c.showPage()
        self.doc.pages.append(self)

    def issues(self):
        f = self.doc.f
        s = f['text_safe']
        out = []
        for t in self.texts:
            x0, y0, x1, y1 = t['bbox_mm']
            if x0 < s[0] - 1e-6 or y0 < s[1] - 1e-6 or x1 > s[2] + 1e-6 or y1 > s[3] + 1e-6:
                out.append(f'文字超出安全區：{t["text"]} {t["bbox_mm"]}')
            for p in self.photos:
                if p.get('role') == 'photo':
                    px0, py0, px1, py1 = p['box_mm']
                    if x0 < px1 and x1 > px0 and y0 < py1 and y1 > py0:
                        out.append(f'文字壓到照片：{t["text"]}')
        for p in self.photos:
            x0, y0, x1, y1 = p['box_mm']
            if y0 < f['coil_assumed'] or x0 < f['trim'] or x1 > f['W'] - f['trim'] or y1 > f['H'] - f['trim']:
                out.append(f'照片框進入線圈假設區或超出裁切線：{p["box_mm"]}')
        return out

    def record(self):
        dates = [t for t in self.texts if t['role'] in ('date', 'strip_date', 'mini_date')]
        return {'face': self.face, 'role': self.role, 'month': self.month, 'set': self.sid, 'variant': self.variant,
                'photos': self.photos, 'lattices': self.lattices, 'n_texts': len(self.texts),
                'min_text_pt': min(t['em_pt'] for t in self.texts) if self.texts else None,
                'min_date_pt': min(t['em_pt'] for t in dates) if dates else None,
                'issues': self.issues()}


# ---------- 日期 ----------
class Dates:
    def __init__(self):
        D = json.loads(git('show', f'HEAD:{DGPA_FILE}'))
        self.off = {d['date']: d['off'] for d in D['days']}
        self.source = D['source']
        assert len(self.off) == 365 and sum(self.off.values()) == 121, '人事總處 116 年：365 天、放假 121 天'

    def is_off(self, m, d):
        return self.off[f'2027-{m:02d}-{d:02d}']


def first_col(m):
    return (dt.date(2027, m, 1).weekday() + 1) % 7   # 週日＝0


def ndays(m):
    return calendar.monthrange(2027, m)[1]


def draw_grid(pg, D, box, m, head_h, digit_em, head_em, align, role, pad=(1.5, 1.3)):
    """月曆格：7 欄 × 固定 6 列；align＝tl（數字在格子左上，可寫字）／c（置中，年曆小月曆用）。"""
    x0, y0, x1, y1 = box
    cw = (x1 - x0) / 7
    rh = (y1 - y0 - head_h) / 6
    for k, ch in enumerate(WEEK):
        pg.text(x0 + (k + .5) * cw, y0 + head_h / 2, ch, 'CJK', head_em, RED if k in (0, 6) else INK, 'c', 'mid', 'weekday')
    lw = 0.35 if align == 'tl' else 0.25
    if align == 'tl':
        for r in range(7):
            pg.line(x0, y0 + head_h + r * rh, x1, y0 + head_h + r * rh, lw)
        for k in range(8):
            pg.line(x0 + k * cw, y0 + head_h, x0 + k * cw, y1, lw)
    else:
        pg.line(x0, y0 + head_h, x1, y0 + head_h, lw)
    f = first_col(m)
    for d in range(1, ndays(m) + 1):
        r, k = divmod(f + d - 1, 7)
        col = RED if D.is_off(m, d) else INK
        if align == 'tl':
            pg.text(x0 + k * cw + pad[0], y0 + head_h + r * rh + pad[1], str(d), 'LAT', digit_em, col, 'l', 'top', role)
        else:
            pg.text(x0 + (k + .5) * cw, y0 + head_h + (r + .5) * rh, str(d), 'LAT', digit_em, col, 'c', 'mid', role)
    pg.lattices.append({'type': 'grid', 'm': m, 'box': [round(v, 3) for v in box], 'head_h': head_h, 'cols': 7, 'rows': 6,
                        'digit_em': digit_em, 'head_em': head_em, 'align': align})


def draw_strip(pg, D, x0, x1, m, wd_y, d_y, wd_em, d_em):
    """單行日期條：每天一格（週幾＋日期），格寬固定＝(x1−x0)/31，短月份靠左。"""
    cw = (x1 - x0) / 31
    for d in range(1, ndays(m) + 1):
        dow = (dt.date(2027, m, d).weekday() + 1) % 7
        col = RED if D.is_off(m, d) else INK
        cx = x0 + (d - .5) * cw
        pg.text(cx, wd_y, WEEK[dow], 'CJK', wd_em, col, 'c', 'mid', 'strip_weekday')
        pg.text(cx, d_y, str(d), 'LAT', d_em, col, 'c', 'mid', 'strip_date')
    pg.lattices.append({'type': 'strip', 'm': m, 'x0': x0, 'cw': round(cw, 4), 'n': ndays(m),
                        'wd_band': [round(wd_y - wd_em * 0.75, 3), round(wd_y + wd_em * 0.75, 3)],
                        'd_band': [round(d_y - d_em * 0.65, 3), round(d_y + d_em * 0.65, 3)], 'wd_em': wd_em, 'd_em': d_em})


# ---------- 照片 ----------
class Photo:
    def __init__(self, s, name, work):
        b = git('cat-file', 'blob', f'{s["commit"]}:{s["file"]}', binary=True)
        assert sha256(b) == s['sha256'] and len(b) == s['bytes'], f'{s["set"]}：原檔與定案清單不符'
        im = Image.open(io.BytesIO(b))
        assert list(im.size) == s['px'] and im.mode == 'RGB', s['set']
        self.s, self.name, self.work = s, name, work
        self.rgb = im.convert('RGB')
        self.W, self.H = self.rgb.size

    def native(self, t=0, b=0):
        """原生像素（只裁上下 t、b px），存成不帶中繼資料的 JPEG 供 PDF 嵌入；回傳路徑。"""
        p = os.path.join(self.work, f'{self.s["set"]}_t{t}_b{b}.jpg')
        if not os.path.exists(p):
            im = self.rgb.crop((0, t, self.W, self.H - b)) if (t or b) else self.rgb
            open(p, 'wb').write(jpeg_bytes(im, 95))
        return p

    def thumb(self, w_mm):
        w = int(round(w_mm / 25.4 * DPI))
        p = os.path.join(self.work, f'{self.s["set"]}_thumb{w}.jpg')
        if not os.path.exists(p):
            assert w < self.W, '封面小圖只縮小'
            im = self.rgb.resize((w, int(round(w * self.H / self.W))), Image.LANCZOS)
            open(p, 'wb').write(jpeg_bytes(im, 90))
        return p

    def rec(self, box, t=0, b=0, role='photo'):
        fw, fh = box[2] - box[0], box[3] - box[1]
        h = self.H - t - b
        assert abs(self.W / h - fw / fh) / (fw / fh) < 0.001, f'{self.s["set"]}：照片比例與框不符'
        return {'role': role, 'set': self.s['set'], 'img_id': self.s['img_id'], 'source_px': [self.W, self.H],
                'crop_px': {'top': t, 'bottom': b, 'left': 0, 'right': 0}, 'native_px': [self.W, h],
                'eff_ppi': round(self.W / (fw / 25.4), 1), 'resampled_up': False}


def subject_rows(ph):
    """人物（分割模型類別 1–5 的最大連通區塊）上緣列與下方空白列數；只作輔助，最後以目視判讀為準。"""
    import cv2
    a = np.asarray(ph.rgb)
    cat = categories(a)
    n, lab, st, _ = cv2.connectedComponentsWithStats((cat > 0).astype(np.uint8), connectivity=8)
    m = lab == (1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])))
    rows = np.where(m.any(1))[0]
    return int(rows.min()), int(ph.H - 1 - rows.max())


def crop_plan(sid, top, bottom_gap):
    """192×104 套框要去掉 43 px：先用髮頂上方超過 3% 的空白；下緣已截斷的照片其餘從下緣裁；
    腳完整的照片其餘先用腳下空白、再用髮頂上方剩下的空白；仍不夠才切到人物（只有 H-Rainie）。"""
    edge = H_EDGE[sid][0]
    t = min(NEED_H, max(0, top - KEEP_TOP))
    rem = NEED_H - t
    if edge == 'cut':
        return {'top': t, 'bottom': rem, 'cuts_subject_px': 0, 'extra_on_truncated_px': rem}
    b = min(rem, bottom_gap)
    rem -= b
    t2 = min(rem, top - t)
    t += t2
    rem -= t2
    return {'top': t + rem, 'bottom': b, 'cuts_subject_px': rem, 'extra_on_truncated_px': 0,
            'alt': {'top': t, 'bottom': b + rem} if rem else None}


# ---------- 各種面 ----------
def photo_face_H(doc, D, ph, M, face, frame='B', crop=(0, 0), variant=None):
    pg = Page(doc, face, 'photo', M['month'], M['set'], variant or frame)
    box = FMT['H']['photo'][frame]
    pg.image(ph.native(*crop), box, ph.rec(box, *crop))
    top = box[3] + 4
    adv, _ = pg.text(6, top, f'{M["month"]:02d}', 'LATB', 10, INK, 'l', 'top', 'month_no')
    pg.text(6 + adv + 2.2, top + 0.2, EN[M['month'] - 1], 'LAT', 2.8, INK, 'l', 'top', 'month_en')
    pg.text(6 + adv + 2.2, top + 4.4, '2027', 'LAT', 2.8, MUTED, 'l', 'top', 'year')
    pg.text(6, top + 11.6, M['person'], 'LAT', 2.6, MUTED, 'l', 'top', 'name')
    draw_strip(pg, D, 52, 198, M['month'], top + 1.7, top + 6.2, 2.3, 3.0)
    pg.finish()
    return pg


def photo_face_V(doc, D, ph, M, face):
    pg = Page(doc, face, 'photo', M['month'], M['set'], 'V')
    box = FMT['V']['photo']['V']
    pg.image(ph.native(), box, ph.rec(box))
    adv, bb = pg.text(12, 180, f'{M["month"]:02d}', 'LATB', 6.2, INK, 'l', 'top', 'month_no')
    base = bb[3]
    pg.text(12 + adv + 1.6, base, f'{EN[M["month"] - 1]}  2027', 'LAT', 2.4, INK, 'l', 'base', 'month_en')
    pg.text(132, base, M['person'], 'LAT', 2.4, MUTED, 'r', 'base', 'name')
    draw_strip(pg, D, 12, 132, M['month'], 188.7, 193.3, 1.9, 2.45)
    pg.finish()
    return pg


def grid_face(doc, D, M, face):
    k = doc.kind
    pg = Page(doc, face, 'grid', M['month'], M['set'])
    right = 196 if k == 'H' else 136
    adv, bb = pg.text(8, 15, f'{M["month"]:02d}', 'LATB', 11, INK, 'l', 'top', 'month_no')
    pg.text(8 + adv + 2.6, 15.4, f'{EN[M["month"] - 1]}  2027', 'LAT', 3.3 if k == 'H' else 3.0, INK, 'l', 'top', 'month_en')
    pg.text(8 + adv + 2.6, 20.6, f'2027 年 {M["month"]} 月', 'CJK', 3.0 if k == 'H' else 2.8, MUTED, 'l', 'top', 'month_zh')
    pg.text(right, bb[3], M['person'], 'LAT', 2.8 if k == 'H' else 2.5, MUTED, 'r', 'base', 'name')
    if k == 'H':
        draw_grid(pg, D, (8, 28, 196, 146), M['month'], 6.5, 4.3, 2.9, 'tl', 'date')
        pg.text(8, 149.8, HOLIDAY_NOTE, 'CJK', 1.7, MUTED, 'l', 'base', 'note')
    else:
        draw_grid(pg, D, (8, 28, 136, 193), M['month'], 6.0, 4.0, 2.7, 'tl', 'date')
        pg.text(8, 196.2, HOLIDAY_NOTE, 'CJK', 1.45, MUTED, 'l', 'base', 'note')
    pg.finish()
    return pg


def cover(doc, photos, months, face=1):
    k = doc.kind
    pg = Page(doc, face, 'cover')
    adv, bb = pg.text(8, 15, '2027', 'LATB', 15 if k == 'H' else 13, INK, 'l', 'top', 'title')
    pg.text(8 + adv + 4, 15.6, 'DESK CALENDAR', 'LAT', 3.4 if k == 'H' else 2.9, INK, 'l', 'top', 'title_en')
    pg.text(8 + adv + 4, bb[3], BRAND, 'CJK', 3.0 if k == 'H' else 2.6, MUTED, 'l', 'base', 'brand_placeholder')
    x0, x1 = 8, (196 if k == 'H' else 136)
    gap, lab = 3.0, (3.6 if k == 'H' else 3.4)
    tw = (x1 - x0 - 3 * gap) / 4
    th = tw * (9 / 16 if k == 'H' else 4 / 3)
    pitch = th + lab + 2.6
    area_top, area_bot = 30, (146 if k == 'H' else 194)
    y0 = area_top + (area_bot - area_top - (3 * pitch - 2.6)) / 2
    for i, M in enumerate(months):
        ph = photos[M['set']]
        x, y = x0 + (i % 4) * (tw + gap), y0 + (i // 4) * pitch
        rec = ph.rec((x, y, x + tw, y + th), role='cover_thumb')
        rec['eff_ppi'] = None
        rec['thumb_px'] = int(round(tw / 25.4 * DPI))
        pg.image(ph.thumb(tw), (x, y, x + tw, y + th), rec)
        pg.text(x, y + th + 0.9, f'{M["month"]:02d}  {M["person"]}', 'LAT', 2.1 if k == 'H' else 1.8, INK, 'l', 'top', 'cover_name')
    pg.finish()
    return pg


def memo(doc, face):
    k = doc.kind
    pg = Page(doc, face, 'memo')
    pg.text(8, 15, 'MEMO', 'LATB', 6, INK, 'l', 'top', 'title')
    x1, yb = (196, 142) if k == 'H' else (136, 190)
    y = 32
    while y <= yb:
        pg.line(8, y, x1, y, 0.35)
        y += 8
    pg.finish()
    return pg


def year_page(doc, D, face):
    pg = Page(doc, face, 'year')
    adv, bb = pg.text(8, 15, '2027', 'LATB', 11, INK, 'l', 'top', 'title')
    pg.text(8 + adv + 3, bb[3], '全年年曆', 'CJK', 3.2, MUTED, 'l', 'base', 'title_zh')
    cw, gap, pitch = 40.0, 4.0, 40.0
    for i in range(12):
        bx, by = 8 + (i % 3) * (cw + gap), 30 + (i // 3) * pitch
        pg.text(bx, by, f'{i + 1} 月', 'CJK', 2.6, INK, 'l', 'top', 'mini_title')
        draw_grid(pg, D, (bx, by + 4.0, bx + cw, by + 36.0), i + 1, 3.6, 2.3, 2.0, 'c', 'mini_date')
    pg.text(8, 196.2, HOLIDAY_NOTE, 'CJK', 1.45, MUTED, 'l', 'base', 'note')
    pg.finish()
    return pg


def barcode(doc, face):
    f = doc.f
    pg = Page(doc, face, 'barcode')
    cx, cy = f['W'] / 2, f['H'] / 2
    pg.text(cx, cy - 4, '最後一面＝條碼頁（廠商固定、不可編輯）', 'CJK', 3.4, MUTED, 'c', 'mid', 'barcode_note')
    pg.text(cx, cy + 3, '本面由廠商產生，此處只是預覽佔位', 'CJK', 2.4, MUTED, 'c', 'mid', 'barcode_note')
    pg.rect(cx - 18, f['H'] - 34, cx + 18, f['H'] - 20, stroke=MUTED, w=0.5, dash=([2, 2], 0))
    pg.text(cx, f['H'] - 27, '條碼位置（示意）', 'CJK', 2.2, MUTED, 'c', 'mid', 'barcode_note')
    pg.finish()
    return pg


# ---------- 點陣化與日期讀回 ----------
def rasterize(pdf, outdir, dpi):
    os.makedirs(outdir, exist_ok=True)
    subprocess.check_call(['pdftoppm', '-r', str(dpi), '-png', pdf, os.path.join(outdir, 'p')])
    fs = sorted(f for f in os.listdir(outdir) if f.startswith('p-') and f.endswith('.png'))
    return [os.path.join(outdir, f) for f in fs]


REFS = {}


def build_refs(docs, work):
    """參考字形：用與正式頁面相同的流程（reportlab 嵌入同一字型 → pdftoppm 300 dpi）畫出每個候選字，再切出墨跡。
    讀回比對因此不受 FreeType 與 Poppler 渲染差異（含小字級內嵌點陣字）影響。"""
    combos = set()
    for d in docs:
        for pg in d.pages:
            for L in pg.lattices:
                if L['type'] == 'grid':
                    combos |= {('CJK', L['head_em'], 'w'), ('LAT', L['digit_em'], 'd')}
                else:
                    combos |= {('CJK', L['wd_em'], 'w'), ('LAT', L['d_em'], 'd')}
    combos = sorted(combos)
    path = os.path.join(work, 'glyph_refs.pdf')
    c = rl_canvas.Canvas(path, pagesize=(200 * MMPT, 200 * MMPT), invariant=1, initialFontName='LAT', initialFontSize=8)
    for font, em, kind in combos:
        texts = list(WEEK) if kind == 'w' else [str(i) for i in range(1, 32)]
        c.setFillColorRGB(0, 0, 0)
        c.setFont(font, em * PT)
        step = max(4 * em, 6)
        for i, t in enumerate(texts):
            x, base = 5 + (i % 8) * step, 5 + em + (i // 8) * step
            c.drawString(x * MMPT, (200 - base) * MMPT, t)
        c.showPage()
    c.save()
    pngs = rasterize(path, os.path.join(work, 'glyph_refs'), DPI)
    k = DPI / 25.4
    pi = 0
    for font, em, kind in combos:
        arr = np.asarray(Image.open(pngs[pi]).convert('L'))
        pi += 1
        texts = list(WEEK) if kind == 'w' else [str(i) for i in range(1, 32)]
        step = max(4 * em, 6)
        for i, t in enumerate(texts):
            x, base = 5 + (i % 8) * step, 5 + em + (i // 8) * step
            sub = arr[int((base - 1.6 * em) * k):int((base + 0.6 * em) * k), int((x - 0.3 * em) * k):int((x + step - 0.5) * k)] < 140
            ys, xs = np.where(sub)
            REFS[(font, em, t)] = sub[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    return len(combos)


def read_cell(arr, box_mm, cands, font, em_mm):
    k = DPI / 25.4
    x0, y0, x1, y1 = [int(round(v * k)) for v in box_mm]
    c = arr[y0:y1, x0:x1].astype(int)
    ink = c.min(-1) < 140
    if ink.sum() < 6:
        return None, 0.0, None
    ys, xs = np.where(ink)
    g = ink[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    core = c[ink]
    color = 'red' if float(core[:, 0].mean() - core[:, 1].mean()) > 60 else 'ink'
    best, score = None, 0.0
    for t in cands:
        r = REFS[(font, em_mm, t)]
        if abs(r.shape[0] - g.shape[0]) > 3 or abs(r.shape[1] - g.shape[1]) > 3:
            continue
        H, W = max(r.shape[0], g.shape[0]) + 2, max(r.shape[1], g.shape[1]) + 2
        G = np.zeros((H, W), bool)
        G[1:1 + g.shape[0], 1:1 + g.shape[1]] = g
        for dy in range(3):
            for dx in range(3):
                Rr = np.zeros((H, W), bool)
                Rr[dy:dy + r.shape[0], dx:dx + r.shape[1]] = r
                inter = (Rr & G).sum()
                uni = (Rr | G).sum()
                sc = inter / uni if uni else 0
                if sc > score:
                    best, score = t, sc
    return best, round(float(score), 3), color


def verify_dates(rec, png, D):
    """讀回實際輸出（PDF→300 dpi）的每一格；期望值用 calendar.monthdayscalendar 另行推算（渲染用的是 datetime）。"""
    arr = np.asarray(Image.open(png).convert('RGB'))
    res = {'face': rec['face'], 'cells': 0, 'dates_read': 0, 'min_score': 1.0, 'failures': []}
    days = [str(i) for i in range(1, 32)]
    for L in rec['lattices']:
        m = L['m']
        if L['type'] == 'grid':
            x0, y0, x1, y1 = L['box']
            cw, hh = (x1 - x0) / 7, L['head_h']
            rh = (y1 - y0 - hh) / 6
            ins = 0.4
            weeks = calendar.Calendar(firstweekday=6).monthdayscalendar(2027, m)
            weeks += [[0] * 7] * (6 - len(weeks))
            for k in range(7):
                t, s, col = read_cell(arr, (x0 + k * cw + ins, y0 + 0.2, x0 + (k + 1) * cw - ins, y0 + hh - 0.2), list(WEEK), 'CJK', L['head_em'])
                res['cells'] += 1
                if t != WEEK[k] or (col == 'red') != (k in (0, 6)):
                    res['failures'].append({'m': m, 'cell': f'header {k}', 'expected': WEEK[k], 'read': t, 'score': s, 'color': col})
            for r in range(6):
                for k in range(7):
                    exp = weeks[r][k]
                    t, s, col = read_cell(arr, (x0 + k * cw + ins, y0 + hh + r * rh + ins, x0 + (k + 1) * cw - ins, y0 + hh + (r + 1) * rh - ins),
                                          days, 'LAT', L['digit_em'])
                    res['cells'] += 1
                    want_red = bool(exp) and D.is_off(m, exp)
                    ok = (t is None and not exp) or (exp and t == str(exp) and s >= 0.6 and (col == 'red') == want_red)
                    if ok and exp:
                        res['dates_read'] += 1
                        res['min_score'] = min(res['min_score'], s)
                    if not ok:
                        res['failures'].append({'m': m, 'cell': f'r{r}c{k}', 'expected': exp or '空白', 'read': t, 'score': s,
                                                'color': col, 'want_red': want_red})
        else:
            x0, cw = L['x0'], L['cw']
            for i in range(31):
                day = i + 1
                bx = (x0 + i * cw + 0.15, x0 + (i + 1) * cw - 0.15)
                t1, s1, c1 = read_cell(arr, (bx[0], L['wd_band'][0], bx[1], L['wd_band'][1]), list(WEEK), 'CJK', L['wd_em'])
                t2, s2, c2 = read_cell(arr, (bx[0], L['d_band'][0], bx[1], L['d_band'][1]), days, 'LAT', L['d_em'])
                res['cells'] += 2
                if day > L['n']:
                    if t1 is not None or t2 is not None:
                        res['failures'].append({'m': m, 'cell': f'day {day}（本月沒有這天）', 'read': [t1, t2]})
                    continue
                dow = WEEK[calendar.weekday(2027, m, day) - 6]
                want_red = D.is_off(m, day)
                if t2 == str(day) and s2 >= 0.6:
                    res['dates_read'] += 1
                    res['min_score'] = min(res['min_score'], s2)
                if t1 != dow or t2 != str(day) or s2 < 0.6 or (c1 == 'red') != want_red or (c2 == 'red') != want_red:
                    res['failures'].append({'m': m, 'cell': f'day {day}', 'expected': [dow, day, want_red], 'read': [t1, t2, c1, c2], 'score': [s1, s2]})
    return res


def negative_test(rec, png, D):
    """負向測試：把一個面的輸出改壞三處（一個黑字塗紅、一格擦掉、一格換成別的數字），核對程式都抓得到。"""
    from PIL import ImageDraw
    im = Image.open(png).convert('RGB')
    L = next(x for x in rec['lattices'] if x['type'] == 'grid')
    m = L['m']
    x0, y0, x1, y1 = L['box']
    cw, hh = (x1 - x0) / 7, L['head_h']
    rh = (y1 - y0 - hh) / 6
    f = first_col(m)
    k = DPI / 25.4
    work = [d for d in range(1, ndays(m) + 1) if not D.is_off(m, d)]
    a, b, c = work[1], work[5], work[9]

    def cell(d):
        r, kk = divmod(f + d - 1, 7)
        return [int(round(v * k)) for v in (x0 + kk * cw + 0.4, y0 + hh + r * rh + 0.4, x0 + (kk + 1) * cw - 0.4, y0 + hh + (r + 1) * rh - 0.4)]
    arr = np.asarray(im).copy()
    bx = cell(a)
    sub = arr[bx[1]:bx[3], bx[0]:bx[2]]
    mask = sub.min(-1) < 140
    sub[mask] = [196, 31, 41]
    bx = cell(b)
    arr[bx[1]:bx[3], bx[0]:bx[2]] = 255
    im = Image.fromarray(arr)
    bx = cell(c)
    dr = ImageDraw.Draw(im)
    dr.rectangle(bx, fill=(255, 255, 255))
    em = int(round(L['digit_em'] * k))
    b_ = pil_font('LAT', em).getbbox(str(c + 1), anchor='ls')
    dr.text((bx[0] + int(1.5 * k) - b_[0], bx[1] + int(1.3 * k) - b_[1] - int(0.4 * k)), str(c + 1), fill=(33, 33, 38), font=pil_font('LAT', em), anchor='ls')
    p2 = png + '.neg.png'
    im.save(p2)
    r = verify_dates(rec, p2, D)
    os.remove(p2)
    got = {f['cell'] for f in r['failures']}
    want = set()
    for d in (a, b, c):
        rr, kk = divmod(f + d - 1, 7)
        want.add(f'r{rr}c{kk}')
    return {'face': rec['face'], 'month': m, 'tampered': {'black_to_red': a, 'erased': b, 'replaced': [c, c + 1]},
            'caught': sorted(got & want), 'missed': sorted(want - got), 'false_alarms': sorted(got - want), 'pass': got == want}


# ---------- 輸出 ----------
def save_jpeg(im, path, q):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'wb').write(jpeg_bytes(im, q, 2))
    return path


def page_images(png, out_base):
    im = Image.open(png).convert('RGB')
    full = save_jpeg(im, out_base + '_f.jpg', 85)
    v = im.resize((int(round(im.width * VIEW_DPI / DPI)), int(round(im.height * VIEW_DPI / DPI))), Image.LANCZOS)
    view = save_jpeg(v, out_base + '_v.jpg', 85)
    return view, full


def zoom_crop(png, box_mm, out):
    """局部放大用：從 300 dpi 輸出直接切一塊（不縮放），網站以像素放大顯示。"""
    k = DPI / 25.4
    im = Image.open(png).convert('RGB').crop(tuple(int(round(v * k)) for v in box_mm))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out, optimize=False)
    return out


def pdf_info(path):
    from pypdf import PdfReader
    r = PdfReader(path)
    pages = []
    for p in r.pages:
        mb, tb, bb = p.mediabox, p.trimbox, p.bleedbox
        imgs = []
        res = p.get('/Resources') or {}
        xo = res.get('/XObject') or {}
        for k in xo:
            o = xo[k].get_object()
            if o.get('/Subtype') == '/Image':
                imgs.append({'w': int(o['/Width']), 'h': int(o['/Height']), 'filter': str(o.get('/Filter')), 'cs': str(o.get('/ColorSpace'))})
        pages.append({'media_mm': [round(float(mb.width) / PT, 2), round(float(mb.height) / PT, 2)],
                      'trim_mm': [round(float(v) / PT, 2) for v in (tb.left, tb.bottom, tb.right, tb.top)],
                      'bleed_mm': [round(float(v) / PT, 2) for v in (bb.left, bb.bottom, bb.right, bb.top)], 'images': imgs})
    fonts = subprocess.check_output(['pdffonts', path], text=True).splitlines()[2:]
    meta = {k: str(v) for k, v in (r.metadata or {}).items()}
    return {'pages': len(r.pages), 'page_info': pages, 'fonts': [' '.join(l.split()) for l in fonts], 'meta': meta}


# ---------- 主流程 ----------
def build(pub, work):
    os.makedirs(work, exist_ok=True)
    register_fonts()
    D = Dates()
    fin_head = git('show', f'{FINAL_COMMIT}:{FINAL_FILE}')
    assert open(os.path.join(ROOT, FINAL_FILE), encoding='utf-8').read() == fin_head, '工作目錄的定案清單與 R25 成果 commit 不同'
    FIN = json.loads(fin_head)
    sets = FIN['sets']
    assert len(sets) == 24 and [(s['book'], s['month']) for s in sets] == [(b, m) for b in 'HV' for m in range(1, 13)]
    assert len({s['sha256'] for s in sets}) == 24 and len({s['img_id'] for s in sets}) == 24
    names = {}
    for s in sets:
        pid = s['set'].split('-', 1)[1]
        names[s['set']] = json.loads(git('show', f'HEAD:kols/{pid}/profile.json'))['identity']['name']
    photos = {s['set']: Photo(s, names[s['set']], work) for s in sets}
    months = {b: [{'month': s['month'], 'set': s['set'], 'person': names[s['set']], 'img_id': s['img_id']} for s in sets if s['book'] == b] for b in 'HV'}

    # 橫式：實圖判讀＋裁切計畫（192×104 比較版）
    crops = {}
    for M in months['H']:
        ph = photos[M['set']]
        top, gap = subject_rows(ph)
        plan = crop_plan(M['set'], top, gap)
        crops[M['set']] = {'month': M['month'], 'subject_top_px': top, 'subject_bottom_gap_px': gap if H_EDGE[M['set']][0] == 'whole' else 0,
                           'seg_bottom_gap_px': gap, 'bottom_edge': H_EDGE[M['set']][0], 'visual_note': H_EDGE[M['set']][1], 'A': plan}
    os.makedirs(pub, exist_ok=True)
    pub = os.path.abspath(pub)
    cwd = os.getcwd()
    os.chdir(work)
    try:
        docs = make_pdfs(pub, work, D, photos, months, crops)
    finally:
        os.chdir(cwd)
    pH, pV, pA = (os.path.join(pub, 'cal2027_H_layout_preview_R26.pdf'), os.path.join(pub, 'cal2027_V_layout_preview_R26.pdf'),
                  os.path.join(work, 'H_compare_A.pdf'))
    return finish(pub, work, D, docs, crops, sets, names, pH, pV, pA)


def make_pdfs(pub, work, D, photos, months, crops):
    docs = {}
    # 橫式（推薦：完整 16:9）
    pH = os.path.join(pub, 'cal2027_H_layout_preview_R26.pdf')
    d = Doc('H', pH, '2027 橫式桌曆（200×151 mm）版面預覽 R26｜非交印核准')
    cover(d, photos, months['H'])
    for M in months['H']:
        photo_face_H(d, D, photos[M['set']], M, 2 * M['month'], 'B')
        grid_face(d, D, M, 2 * M['month'] + 1)
    memo(d, 26)
    memo(d, 27)
    barcode(d, 28)
    d.c.save()
    docs['H'] = d
    # 直式
    pV = os.path.join(pub, 'cal2027_V_layout_preview_R26.pdf')
    d = Doc('V', pV, '2027 直式桌曆（140×200 mm）版面預覽 R26｜非交印核准')
    cover(d, photos, months['V'])
    for M in months['V']:
        photo_face_V(d, D, photos[M['set']], M, 2 * M['month'])
        grid_face(d, D, M, 2 * M['month'] + 1)
    for f in range(26, 31):
        memo(d, f)
    year_page(d, D, 31)
    barcode(d, 32)
    d.c.save()
    docs['V'] = d
    # 橫式比較版（192×104 套框；不發佈 PDF，只發佈頁面圖）
    pA = os.path.join(work, 'H_compare_A.pdf')
    d = Doc('H', pA, '比較用：192×104 套框')
    for M in months['H']:
        c = crops[M['set']]['A']
        photo_face_H(d, D, photos[M['set']], M, 2 * M['month'], 'A', (c['top'], c['bottom']), 'A')
    ca = crops[RAINIE_ALT]['A']['alt']
    M12 = next(M for M in months['H'] if M['set'] == RAINIE_ALT)
    photo_face_H(d, D, photos[RAINIE_ALT], M12, 24, 'A', (ca['top'], ca['bottom']), 'A2')
    d.c.save()
    docs['A'] = d
    return docs


def finish(pub, work, D, docs, crops, sets, names, pH, pV, pA):
    for k in docs:
        for p in docs[k].pages:
            assert not p.issues(), (k, p.face, p.issues())
    assert [p.face for p in docs['H'].pages] == list(range(1, 29)) and [p.face for p in docs['V'].pages] == list(range(1, 33))

    # 點陣化、頁面圖、日期讀回
    n_refs = build_refs(docs.values(), work)
    out = {'H': [], 'V': [], 'A': []}
    checks = []
    rasters = {}
    for k, pdf in (('H', pH), ('V', pV), ('A', pA)):
        pngs = rasterize(pdf, os.path.join(work, 'r_' + k), DPI)
        assert len(pngs) == len(docs[k].pages)
        rasters[k] = pngs
        for pg, png in zip(docs[k].pages, pngs):
            rec = pg.record()
            if k == 'A':
                base = os.path.join(pub, 'cmp', f'H_m{pg.month:02d}_{pg.variant}')
            else:
                base = os.path.join(pub, k, f'f{pg.face:02d}')
            view, full = page_images(png, base)
            rec['view'], rec['full'] = os.path.relpath(view, pub), os.path.relpath(full, pub)
            if rec['lattices']:
                c = verify_dates(rec, png, D)
                c['book'] = k
                checks.append(c)
            out[k].append(rec)
    neg = negative_test(next(r for r in out['H'] if r['role'] == 'grid'), rasters['H'][2], D)

    # H-Rainie、H-Somi 上下緣局部放大（推薦版 B／套框 A；Rainie 另有 A2）
    zooms = []
    k = 192 / 2048
    for sid, xs in ((RAINIE_ALT, (930, 1130)), ('H-somi-oh', (860, 1100))):
        m = crops[sid]['month']
        for var, png, fb in (('B', rasters['H'][2 * m - 1], 'B'), ('A', rasters['A'][m - 1], 'A')) + ((('A2', rasters['A'][12], 'A'),) if sid == RAINIE_ALT else ()):
            box = FMT['H']['photo'][fb]
            xa, xb = 6 + xs[0] * k, 6 + xs[1] * k
            for edge, yy in (('top', (box[1] - 1.5, box[1] + 8)), ('bottom', (box[3] - 8, box[3] + 1.5))):
                if sid == 'H-somi-oh' and edge == 'bottom':
                    xa2, xb2 = 6 + 880 * k, 6 + 1060 * k
                elif sid == RAINIE_ALT and edge == 'bottom':
                    xa2, xb2 = 6 + 960 * k, 6 + 1100 * k
                else:
                    xa2, xb2 = xa, xb
                p = zoom_crop(png, (xa2, yy[0], xb2, yy[1]), os.path.join(pub, 'cmp', f'zoom_{sid.split("-")[1]}_{var}_{edge}.png'))
                zooms.append({'set': sid, 'variant': var, 'edge': edge, 'file': os.path.relpath(p, pub), 'box_mm': [round(xa2, 2), yy[0], round(xb2, 2), yy[1]]})

    info = {'H': pdf_info(pH), 'V': pdf_info(pV)}
    for k in 'HV':
        I = info[k]
        f = FMT[k]
        assert I['pages'] == f['faces']
        for pi in I['page_info']:
            assert pi['media_mm'] == [f['W'], f['H']] and pi['trim_mm'] == [2, 2, f['W'] - 2, f['H'] - 2]
        assert all(' yes yes ' in l for l in I['fonts']), I['fonts']
    files = []
    for dp, _, fs in os.walk(pub):
        for fn in sorted(fs):
            p = os.path.join(dp, fn)
            files.append({'path': os.path.relpath(p, pub), 'bytes': os.path.getsize(p), 'sha256': sha256(open(p, 'rb').read())})
    files.sort(key=lambda x: x['path'])
    return {'out': out, 'checks': checks, 'neg': neg, 'zooms': zooms, 'crops': crops, 'info': info, 'files': files,
            'sources': [{**{k: s[k] for k in ('book', 'month', 'set', 'img_id', 'commit', 'file', 'sha256', 'px')}, 'person': names[s['set']]} for s in sets],
            'names': names, 'dgpa_source': D.source, 'n_refs': n_refs}


SPEC = {
    'official': [
        {'k': '成品尺寸（裁切線）', 'H': '200×151 mm', 'V': '140×200 mm', 'src': '商品頁（2026-10-29 唯讀重查仍相同）；CAL_01 §1'},
        {'k': '頁數', 'H': '14 張／28 面', 'V': '16 張／32 面', 'src': '商品頁（2026-10-29 重查相同）；編輯器 no_of_side'},
        {'k': '最後一面', 'H': '條碼頁，不可編輯', 'V': '條碼頁，不可編輯', 'src': '商品頁「請注意」第 2 點'},
        {'k': '出血', 'H': '四邊各 2 mm（含出血畫布 204×155 mm）', 'V': '四邊各 2 mm（144×204 mm）', 'src': '編輯器設定 bleedMargin（2026-10-08 擷取）'},
        {'k': '編輯器安全框', 'H': '裁切線內 上 10、右 2、下 2、左 2 mm', 'V': '0 mm', 'src': '編輯器設定 safeMargin'},
        {'k': '裝訂', 'H': '黑色雙環線圈（上緣）、黑底板', 'V': '黑色雙環線圈（上緣）、黃褐色底板', 'src': '商品頁規格'},
        {'k': '設計稿要求', 'H': '重要文字／圖放在安全框內；圖面超出裁切線並延伸到出血線', 'V': '同左', 'src': '客製編輯須知 Q1（2026-10-29 重讀）'},
        {'k': '檔案格式', 'H': 'JPG、JPEG、PNG、AI、PDF', 'V': '同左', 'src': '客製編輯須知 Q3'},
        {'k': '解析度', 'H': '編輯器設定 imageDPI 300；只顯示「好／標準／差」三級，沒有公開數字門檻', 'V': '同左', 'src': '編輯器設定；客製編輯須知 Q2'},
        {'k': '色彩', 'H': '成品以 CMYK 四色印刷，色差 ±10% 內為合格（參照 ISO 12647-2）；上傳 RGB 如何轉換沒有說明、沒有指定 ICC', 'V': '同左', 'src': '客製編輯須知 Q3（只答格式）、Q10'},
        {'k': '單檔上限', 'H': '說明頁 300MB；編輯器設定值 30（未標單位）', 'V': '同左', 'src': '客製編輯須知 Q7；編輯器設定（兩處不一致）'},
        {'k': '範本頁序', 'H': '面 1 封面；面 2–25 每月兩面；26–27 MEMO；28 條碼', 'V': '面 1 封面；2–25 每月兩面（照片面→大格面）；26–30 MEMO；31 全年年曆；32 條碼', 'src': '廠商 2027 範本 8385／8364／8404（CAL_01 §3.2）'},
    ],
    'owner': [
        {'k': '照片', 'v': '24 張定案（R25 cal_m4_final_r25.json，Penny 選定）；本輪不重開選片、不換版本'},
        {'k': '月份與人選', 'v': '兩本月份排序維持既定（R6）'},
        {'k': '工作照片框', 'v': 'R6 接受：橫式 192×104 mm（生成 16:9）、直式 120×160 mm（生成 3:4）；是工作版型，不是廠商規格或印刷核准'},
        {'k': '已接受的調色', 'v': '5 張衍生檔（H-Coco、V-Luna、H-Luna、V-Miu、H-Somi）定案的是調色／修正版本身，本輪原樣使用'},
    ],
    'defaults': [
        {'k': '日期資料', 'v': '自繪；只用人事總處 116 年辦公日曆表；紅字含補假；不加農曆；不用廠商日期素材（CAL_10 §4 技術預設，Penny 知悉、未另行表示意見）'},
        {'k': '頁序', 'v': '照片面在前、大格面在後（同範本 8364／8404）；整本一致（CAL_10 §4）'},
        {'k': '週起始', 'v': '週日起始（台灣慣例、廠商台灣日期素材同樣週日起始；Owner 未另定）'},
        {'k': '線圈區', 'v': '畫布上緣 0–12 mm 不放臉與文字（假設；編輯器線圈示意量得 8.9／9.7 mm，不是書面規格）'},
        {'k': '品牌', 'v': '封面品牌名稱、Logo、QR 未定（決策 D 未回答）→ 佔位'},
    ],
    'assumed': [
        {'k': '紙張正反面拼版', 'v': '假設 H1：第 k 張＝面 2k−1（正）／面 2k（背）——符合 14／16 張；若成立，照片面會在紙張背面（CAL_13）。PDF 單面正向逐面排列，不旋轉'},
        {'k': '背面是否自動旋轉 180°', 'v': '未知；未自行旋轉任何面'},
        {'k': '直式文字安全區', 'v': '廠商安全框 0；本案自訂裁切線內 3 mm、上緣 12 mm'},
        {'k': '色彩', 'v': '來源 PNG 沒有 ICC／gAMA／sRGB 標記（未標記 RGB），以 sRGB 顯示；PDF 照片為 DeviceRGB，沒有轉 CMYK'},
    ],
    'unknown': [
        '線圈實際寬度、打孔位置與裝訂區（書面規格）',
        '編輯器面號與實體紙張正反面的對應、背面是否自動旋轉',
        '「好／標準／差」對應的 ppi 門檻（橫式約 271 ppi 能否歸為好或標準）',
        'RGB→CMYK 由誰轉、用哪個描述檔；實際色差與暗部（要打樣）',
        '交件方式（編輯器逐面上傳或整份 PDF）、單檔上限 300MB 或 30',
        '試做紙材、數量、交件期限（Penny 已知有免費試做；細節待廠商）',
    ],
}


def make_data(R):
    out = R['out']
    crops = R['crops']
    total_fail = sum(len(c['failures']) for c in R['checks'])
    data = {
        'note': '程式產生（docs/calendar/tools/build_cal_m5_layout.py），請勿手改。兩款桌曆排版預覽：工作版、非交印核准、未經廠商確認。',
        'round': ROUND,
        'status': {'owner_selection': 'complete（R25，24／24）', 'layout_preview': 'ready_for_owner_review（R26 工作版，待 Penny 看）',
                   'layout_acceptance': 'not_given（排版接受與照片接受分開記錄）', 'prepress_check': 'in_progress（R26 已做尺寸、裁切、ppi、日期、PDF 核對；廠商項目未確認）',
                   'print_approval': 'not_given（未製作交印檔、未聯絡廠商、未打樣）'},
        'photo_source': {'final_list': FINAL_FILE, 'commit': FINAL_COMMIT, 'sets': R['sources']},
        'spec': SPEC,
        'fonts': FONT_NOTE,
        'dates': {'source': R['dgpa_source'], 'week_start': '週日', 'red': HOLIDAY_NOTE, 'lunar': '不加（CAL_10 §4）',
                  'holiday_names': '不加（只用紅字；本輪不擴充）', 'makeup_workdays': '116 年辦公日曆表沒有補班日'},
        'formats': {k: {kk: FMT[k][kk] for kk in ('zh', 'sku', 'W', 'H', 'faces', 'trim', 'vendor_safe', 'text_safe', 'text_safe_note', 'coil_assumed', 'coil_measured', 'photo')} for k in 'HV'},
        'recommendation': {
            'H_frame': 'B',
            'H_frame_text': '橫式照片框推薦改為完整 16:9（192×108 mm）：12 張都不裁切、構圖與人體完整，日期條區從 27 mm 縮為 23 mm；有效解析度不變（約 271 ppi）。R6 接受的 192×104 mm 套框版本並列比較，待 Penny 決定，未悄悄定案。',
            'layout': '兩款整本一致：照片面＝照片＋月份＋單行日期條；大格面＝月份標題＋7×6 大格（數字在格子左上、留書寫空間）；週日起始、放假日紅字；封面為 12 張縮圖＋品牌佔位；MEMO 與條碼頁依範本。',
        },
        'crops_H': crops,
        'pages': {k: out[k] for k in 'HV'},
        'compare_A': out['A'],
        'zooms': R['zooms'],
        'date_check': {'method': '把兩份 PDF 用 pdftoppm 以 300 dpi 點陣化，依格線幾何切出每一格（不用渲染時記下的文字位置），以同字型字形比對讀出數字／星期，以墨色判定紅黑；'
                                 '期望值用 calendar.monthdayscalendar 另行推算（渲染用 datetime），紅字依人事總處放假日。日期條另核對本月沒有的日子為空白。',
                       'faces': len(R['checks']), 'cells': sum(c['cells'] for c in R['checks']), 'dates_read': sum(c['dates_read'] for c in R['checks']),
                       'min_score': min(c['min_score'] for c in R['checks']), 'failures': total_fail, 'per_face': R['checks'], 'negative_test': R['neg']},
        'pdf': R['info'],
        'files': R['files'],
    }
    return json.loads(json.dumps(data, ensure_ascii=False))


def write_doc(d):
    L = ['# CAL_28 — M-5 R26 兩款桌曆排版預覽（程式產生，請勿手改）', '',
         f'> 由 `docs/calendar/tools/build_cal_m5_layout.py` 產生；原始資料 `{DATA_REL}`。**工作版預覽、非交印核准、未經廠商確認。**', '',
         '## 1. 規格：官方／Owner 已定／技術預設／工作假設', '', '| 項目 | 橫式 | 直式 | 來源 |', '|---|---|---|---|']
    for x in d['spec']['official']:
        L.append(f"| {x['k']} | {x['H']} | {x['V']} | {x['src']} |")
    L += ['', '**Owner 已定**', ''] + [f"- {x['k']}：{x['v']}" for x in d['spec']['owner']]
    L += ['', '**技術預設（沿用 CAL_10 §4；Owner 未另定）**', ''] + [f"- {x['k']}：{x['v']}" for x in d['spec']['defaults']]
    L += ['', '**工作假設（未經廠商確認）**', ''] + [f"- {x['k']}：{x['v']}" for x in d['spec']['assumed']]
    L += ['', '**尚無依據（不填成已確認）**', ''] + [f'- {x}' for x in d['spec']['unknown']]
    L += ['', f"- 字型：{d['fonts']}", '',
          '## 2. 橫式照片框：完整 16:9（推薦）與 192×104 套框（比較）', '',
          d['recommendation']['H_frame_text'], '',
          '| 月 | 套別 | 髮頂上方空白（px） | 下緣 | 目視判讀 | 192×104 套框：上裁／下裁（px） | 切到人物 |', '|---|---|---|---|---|---|---|']
    for sid, c in d['crops_H'].items():
        a = c['A']
        cut = f"{a['cuts_subject_px']} px（另一排法：上 {a['alt']['top']}／下 {a['alt']['bottom']}）" if a['cuts_subject_px'] else (f"0（原圖已截斷處再多裁 {a['extra_on_truncated_px']} px）" if a['extra_on_truncated_px'] else '0')
        low = '原圖已截斷' if c['bottom_edge'] == 'cut' else f"腳下空白 {c['subject_bottom_gap_px']} px"
        L.append(f"| {c['month']} | {sid} | {c['subject_top_px']} | {low} | {c['visual_note']} | {a['top']}／{a['bottom']} | {cut} |")
    L += ['', '## 3. 頁面', '']
    for k in 'HV':
        f = d['formats'][k]
        L += [f"### {f['zh']}（{f['W']}×{f['H']} mm 含出血，{f['faces']} 面）", '', '| 面 | 角色 | 月 | 套別 | 照片框（mm） | 原生 px | 有效 ppi | 最小字（pt） | 最小日期字（pt） | 問題 |', '|---|---|---|---|---|---|---|---|---|---|']
        for p in d['pages'][k]:
            ph = [x for x in p['photos'] if x['role'] == 'photo']
            q = ph[0] if ph else None
            L.append(f"| {p['face']} | {p['role']} | {p['month'] or '—'} | {p['set'] or '—'} | {q['box_mm'] if q else '—'} | "
                     f"{'×'.join(map(str, q['native_px'])) if q else '—'} | {q['eff_ppi'] if q else '—'} | {p['min_text_pt']} | {p['min_date_pt'] or '—'} | {'；'.join(p['issues']) or '無'} |")
        L.append('')
    dc = d['date_check']
    neg = dc['negative_test']
    L += ['## 4. 日期讀回核對', '', dc['method'], '',
          f"- 合計：{dc['faces']} 面、{dc['cells']} 格、讀到 {dc['dates_read']} 個日期、最低比對分數 {dc['min_score']}、失敗 {dc['failures']}。",
          f"- 負向測試（面 {neg['face']}，{neg['month']} 月）：改壞 3 處，抓到 {len(neg['caught'])}、漏掉 {len(neg['missed'])}、誤報 {len(neg['false_alarms'])} → {'通過' if neg['pass'] else '未通過'}。", '',
          '## 5. PDF', '']
    for k in 'HV':
        I = d['pdf'][k]
        pi = I['page_info'][0]
        L.append(f"- {d['formats'][k]['zh']}：{I['pages']} 頁；MediaBox {pi['media_mm'][0]}×{pi['media_mm'][1]} mm；TrimBox {pi['trim_mm']}；字型 {len(I['fonts'])} 個皆嵌入子集")
    L.append('')
    open(os.path.join(ROOT, DOC_REL), 'w', encoding='utf-8').write('\n'.join(L))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    pub = os.path.join(ROOT, PUB_REL)
    if a.check:
        old = json.load(open(os.path.join(ROOT, DATA_REL), encoding='utf-8'))
        with tempfile.TemporaryDirectory() as tmp:
            R = build(os.path.join(tmp, 'pub'), os.path.join(tmp, 'work'))
        bad = 0
        want = {x['path']: x['sha256'] for x in old['files']}
        got = {x['path']: x['sha256'] for x in R['files']}
        if want != got:
            print('重建結果與已記錄的檔案不同：', sorted(set(want.items()) ^ set(got.items()))[:10]); bad += 1
        disk = {}
        for dp, _, fs in os.walk(pub):
            for fn in fs:
                p = os.path.join(dp, fn)
                disk[os.path.relpath(p, pub)] = sha256(open(p, 'rb').read())
        if disk != want:
            print('發佈資料夾與紀錄不同：', sorted(set(disk.items()) ^ set(want.items()))[:10]); bad += 1
        if make_data(R) != old:
            print('重建的排版資料與已記錄的 data JSON 不同'); bad += 1
        fails = sum(len(c['failures']) for c in R['checks'])
        if fails or not R['neg']['pass']:
            print('日期讀回核對失敗：', fails, R['neg']); bad += 1
        print(f'{"FAIL" if bad else "PASS"}: {len(got)} 檔可重現；日期讀回 {len(R["checks"])} 面、失敗 {fails}；負向測試 {"通過" if R["neg"]["pass"] else "未通過"}')
        return 1 if bad else 0
    work = tempfile.mkdtemp(prefix='cal_m5_')
    try:
        if os.path.isdir(pub):
            shutil.rmtree(pub)
        R = build(pub, work)
        d = make_data(R)
        with open(os.path.join(ROOT, DATA_REL), 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
            f.write('\n')
        write_doc(d)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    dc = d['date_check']
    print(f"ok: H {d['pdf']['H']['pages']} 面、V {d['pdf']['V']['pages']} 面；日期讀回 {dc['faces']} 面 {dc['cells']} 格、失敗 {dc['failures']}；負向測試 {'通過' if dc['negative_test']['pass'] else '未通過'}；發佈 {len(d['files'])} 檔")
    return 0


if __name__ == '__main__':
    sys.exit(main())
