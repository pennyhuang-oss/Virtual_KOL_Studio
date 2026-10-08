#!/usr/bin/env python3
"""TASK-CAL-001 / R3 — 暫定工作稿：12 個月 × 橫直照片面（24 面）、兩款封面、兩款代表大格月曆面、一面年曆，
外加比較樣張（直式原直 A、橫式 B 192×104、Kanon 直式重查）。全部是草稿，未經 Penny 核准、未經廠商確認。

量測來源＝實際樣張：每個照片框、座標、圖片 ID、裁切位置都在渲染時記錄（data/cal_r3_layout_report.json），
有效 ppi＝裁切後的原圖原生像素 ÷ 照片框英吋（不是 300 dpi 輸出像素，也不是放大後像素）。
日期：資料只來自人事總處 116 年辦公日曆表；渲染後重新讀取「實際輸出的 300 dpi 檔案」，依格線位置逐格比對字形與顏色
（data/cal_r3_date_check.json），不只核對輸入資料。
用法：python3 docs/calendar/tools/build_cal_r3_pages.py --hf-dir <原圖快取> --cache <清理輸出資料夾>
"""
import argparse
import calendar
import datetime as dt
import hashlib
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from cal_face_lib import geometry  # noqa: E402
from cal_seg import hair_top  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
OUT = os.path.join(CAL, 'r3')
DPI = 300
MM = DPI / 25.4
COIL = 12.0
TRIM = 2.0
FONT_CJK = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
FONT_LAT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_LAT_B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
RED, INK, MUTED = (200, 30, 40), (40, 40, 45), (120, 120, 125)
EN = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
WEEK = '日一二三四五六'
BRAND = '［品牌名稱 佔位］'
DRAFT = '草稿 R3｜未經 Penny 核准'
SRC_NOTE = '紅字＝行政院人事行政總處 116 年辦公日曆表放假日'
OFF = {d['date']: d['off'] for d in json.load(open(os.path.join(CAL, 'data', 'cal_r2_official_2027_dgpa.json')))['days']}

FORMATS = {
    'H': {'W': 204, 'H': 155, 'safe': (4, 12, 200, 151), 'safe_note': '廠商安全框：裁切線內上 10 mm、其餘 2 mm'},
    'V': {'W': 144, 'H': 204, 'safe': (5, 12, 139, 199), 'safe_note': '廠商安全框為 0；本專案自訂：裁切線內 3 mm、上緣 12 mm 線圈假設'},
}
FRAMES = {  # 畫布座標（含 2 mm 出血），mm
    'H_A': ('H', (0, 0, 104, 155), '橫 A 半版直幅照片（主推薦）'),
    'H_B': ('H', (6, 14, 198, 118), '橫 B 大照片 192×104（比較）'),
    'V_U': ('V', (12, 16, 132, 144), '直式統一框 120×128（主推薦）'),
    'V_A': ('V', (0, 0, 144, 150), '原直 A 大照片 144×150（比較）'),
    'V_B_R2': ('V', (10, 16, 134, 148), 'R2 直 B 縮框 124×132（只用於 Kanon 重查）'),
}
_FONTS = {}


def px(v):
    return int(round(v * MM))


def font(path, size_mm):
    k = (path, int(round(size_mm * MM)))
    if k not in _FONTS:
        _FONTS[k] = ImageFont.truetype(path, k[1])
    return _FONTS[k]


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


class Source:
    """一張候選圖：原圖路徑、實際使用的檔案（清理版或原圖）、特徵點、髮頂。"""

    def __init__(self, cid, J, R, clean, hf, cache):
        self.cid = cid
        s = J[cid]['src']
        self.ref = s
        self.orig = os.path.join(hf, next(r for r in R if r['job_id'] == s[3:])['local']) if s.startswith('hf:') else os.path.join(ROOT, s)
        self.used = os.path.join(cache, clean[cid]['clean_file']) if cid in clean else self.orig
        self.cleaned = cid in clean
        self.used_sha = sha(self.used)
        if self.cleaned:
            assert self.used_sha == clean[cid]['clean_sha256'], f'{cid}: cleaned file differs from cleanup report'
        self.orig_sha = sha(self.orig)
        self.img = Image.open(self.used).convert('RGB')
        self.W, self.H = self.img.size
        self.g = geometry(self.orig)
        rgb = np.asarray(Image.open(self.orig).convert('RGB'))
        self.hair = hair_top(rgb, self.g['P']) if self.g else (None, False, 0)


def crop_box(src, fw, fh, frame_top_mm, fy=0.38, keep_hair=True, cy0_frac=None):
    """裁切位置：先讓臉中心落在框高 fy，再盡量讓髮頂進框且離開線圈區，最後確保下巴在框內。回傳 (x0, y0, w, h) 原圖像素。"""
    W, H = src.W, src.H
    a = fw / fh
    P = src.g['P'] if src.g is not None else None
    cx = float(P[:, 0].mean()) if P is not None else W / 2
    cy = float((P[10][1] + P[152][1]) / 2) if P is not None else H * 0.3
    if W / H > a:
        ch, cw = H, int(round(H * a))
        x0 = min(max(int(round(cx - cw / 2)), 0), W - cw)
        return x0, 0, cw, ch
    cw, ch = W, int(round(W / a))
    if cy0_frac is not None:
        return 0, min(max(int(round(cy0_frac * H)), 0), H - ch), cw, ch
    y0 = cy - fy * ch
    k = fh / ch  # mm / px
    if keep_hair and src.hair[0] is not None and not src.hair[1]:
        need_mm = max(COIL + 1.0 - frame_top_mm, 1.0)  # 髮頂離開線圈區（框從線圈區內開始時）或至少離框頂 1 mm
        y0 = min(y0, src.hair[0] - need_mm / k)
    if P is not None:
        chin = float(P[152][1])
        y0 = max(y0, chin + 0.04 * ch - ch)  # 下巴留 4% 框高
    return 0, min(max(int(round(y0)), 0), H - ch), cw, ch


class Page:
    def __init__(self, page_id, kind, role, face_no=None):
        f = FORMATS[kind]
        self.id, self.kind, self.role, self.face_no = page_id, kind, role, face_no
        self.Wmm, self.Hmm = f['W'], f['H']
        self.img = Image.new('RGB', (px(self.Wmm), px(self.Hmm)), 'white')
        self.d = ImageDraw.Draw(self.img)
        self.texts, self.photos, self.lattices = [], [], []

    def text(self, xy, s, size_mm, path=FONT_CJK, fill=INK, anchor='la', role='text'):
        f = font(path, size_mm)
        x, y = px(xy[0]), px(xy[1])
        self.d.text((x, y), s, fill=fill, font=f, anchor=anchor)
        bb = self.d.textbbox((x, y), s, font=f, anchor=anchor)
        self.texts.append({'text': s, 'role': role, 'font': os.path.basename(path), 'em_px': f.size,
                           'em_pt': round(f.size * 72 / DPI, 1), 'em_mm': round(f.size / MM, 2), 'bbox_mm': [round(v / MM, 2) for v in bb]})

    def photo(self, src, frame_key=None, box=None, crop=None, note=None, **kw):
        if frame_key:
            kind, box, label = FRAMES[frame_key]
        else:
            label = 'custom'
        x0m, y0m, x1m, y1m = box
        fw, fh = x1m - x0m, y1m - y0m
        cb = crop or crop_box(src, fw, fh, y0m, **kw)
        cx0, cy0, cw, ch = cb
        tile = src.img.crop((cx0, cy0, cx0 + cw, cy0 + ch)).resize((px(x1m) - px(x0m), px(y1m) - px(y0m)), Image.LANCZOS)
        self.img.paste(tile, (px(x0m), px(y0m)))
        k = fh / ch
        rec = {'frame': frame_key or 'custom', 'frame_label': label, 'frame_mm': [x0m, y0m, x1m, y1m], 'frame_size_mm': [fw, fh],
               'cid': src.cid, 'source_ref': src.ref, 'source_px': [src.W, src.H], 'used_file': 'clean' if src.cleaned else 'original',
               'used_sha256': src.used_sha, 'original_sha256': src.orig_sha, 'crop_px': [cx0, cy0, cw, ch],
               'native_px': [cw, ch], 'ppi_w': round(cw / (fw / 25.4)), 'ppi_h': round(ch / (fh / 25.4)),
               'upscaled_in_render': bool(cw < px(x1m) - px(x0m)), 'trim_mm': TRIM, 'coil_mm': COIL, 'note': note}
        if src.g is not None:
            P = src.g['P']
            inside = (P[:, 0] >= cx0) & (P[:, 0] < cx0 + cw) & (P[:, 1] >= cy0) & (P[:, 1] < cy0 + ch)
            fy = lambda v: round(float(y0m + (v - cy0) * k), 1)  # noqa: E731
            rec['face'] = {'top_mm': fy(P[:, 1].min()), 'forehead_mm': fy(P[10][1]), 'chin_mm': fy(P[152][1]),
                           'left_mm': round(float(x0m + (P[:, 0].min() - cx0) * k), 1), 'right_mm': round(float(x0m + (P[:, 0].max() - cx0) * k), 1),
                           'complete_in_frame': bool(inside.all()), 'clear_of_coil': bool(fy(P[:, 1].min()) >= COIL)}
        ht, touch, cols = src.hair
        if ht is None:
            hs = '無法判定（偵測不到頭髮）'
            hmm = None
        else:
            hmm = round(float(y0m + (ht - cy0) * k), 1)
            if touch:
                hs = f'原圖已缺髮頂（頭髮碰到原圖上緣 {cols} 欄）'
            elif ht < cy0:
                hs = '髮頂被照片框裁掉'
            elif hmm < TRIM:
                hs = '髮頂在出血區（裁切後會被切掉）'
            elif hmm < COIL:
                hs = '髮頂在線圈區內（臉不受影響）'
            else:
                hs = '髮頂完整、在線圈區外'
        rec['hair'] = {'top_src_px': ht, 'top_mm_est': hmm, 'touches_source_top': bool(touch), 'status_auto': hs,
                       'method': 'selfie_multiclass 頭髮類別最上緣（程式判定，需目視確認）'}
        self.photos.append(rec)
        return rec

    def month_grid(self, box, m, digit_mm, head_mm, role='grid'):
        x0, y0, x1, y1 = box
        cw = (x1 - x0) / 7
        hh = head_mm * 1.7
        rh = (y1 - y0 - hh) / 6
        for k, ch in enumerate(WEEK):
            self.text((x0 + (k + .5) * cw, y0 + hh * 0.45), ch, head_mm, FONT_CJK, RED if k in (0, 6) else MUTED, 'mm', 'weekday')
        self.d.line((px(x0), px(y0 + hh), px(x1), px(y0 + hh)), fill=(205, 205, 210), width=max(1, px(0.2)))
        first = (dt.date(2027, m, 1).weekday() + 1) % 7
        for day in range(1, calendar.monthrange(2027, m)[1] + 1):
            r, k = divmod(first + day - 1, 7)
            col = RED if OFF[f'2027-{m:02d}-{day:02d}'] else INK
            self.text((x0 + (k + .5) * cw, y0 + hh + (r + .5) * rh), str(day), digit_mm, FONT_LAT, col, 'mm', 'date')
        self.lattices.append({'type': 'month', 'role': role, 'm': m, 'box': list(box), 'head_h': hh, 'cols': 7, 'rows': 6,
                              'digit_mm': digit_mm, 'head_mm': head_mm})

    def strip(self, box, m, digit_mm):
        x0, y0, x1, y1 = box
        n = calendar.monthrange(2027, m)[1]
        cw = (x1 - x0) / n
        hrow = (y1 - y0) / 2
        for day in range(1, n + 1):
            dow = (dt.date(2027, m, day).weekday() + 1) % 7
            col = RED if OFF[f'2027-{m:02d}-{day:02d}'] else INK
            cx = x0 + (day - .5) * cw
            self.text((cx, y0 + hrow * .5), WEEK[dow], digit_mm * 0.8, FONT_CJK, col, 'mm', 'weekday')
            self.text((cx, y0 + hrow * 1.5), str(day), digit_mm, FONT_LAT, col, 'mm', 'date')
        self.lattices.append({'type': 'strip', 'm': m, 'box': list(box), 'n': n, 'digit_mm': digit_mm})

    def save(self, sub='pages', guides=True):
        os.makedirs(os.path.join(OUT, sub, 'hires'), exist_ok=True)
        hi = os.path.join(OUT, sub, 'hires', f'{self.id}.jpg')
        self.img.save(hi, quality=90, dpi=(DPI, DPI))
        pv = self.img.copy()
        pv.thumbnail((1400, 1400))
        pv.save(os.path.join(OUT, sub, f'{self.id}.jpg'), quality=86)
        if guides:
            g = self.img.copy().convert('RGBA')
            ov = Image.new('RGBA', g.size, (0, 0, 0, 0))
            d = ImageDraw.Draw(ov)
            d.rectangle((0, 0, px(self.Wmm), px(COIL)), fill=(255, 0, 0, 70))
            d.rectangle((px(TRIM), px(TRIM), px(self.Wmm - TRIM), px(self.Hmm - TRIM)), outline=(0, 90, 255, 255), width=5)
            s = FORMATS[self.kind]['safe']
            d.rectangle(tuple(px(v) for v in s), outline=(0, 170, 60, 255), width=4)
            for p in self.photos:
                b = [px(v) for v in p['frame_mm']]
                d.rectangle(b, outline=(255, 140, 0, 255), width=4)
                d.text((b[0] + 12, b[3] - 70), f"{p['cid']}｜{p['ppi_w']} ppi｜{'清理版' if p['used_file'] == 'clean' else '原圖'}",
                       fill=(255, 140, 0, 255), font=font(FONT_CJK, 4.0))
            gi = Image.alpha_composite(g, ov).convert('RGB')
            gi.thumbnail((1400, 1400))
            os.makedirs(os.path.join(OUT, sub, 'guides'), exist_ok=True)
            gi.save(os.path.join(OUT, sub, 'guides', f'{self.id}_guides.jpg'), quality=84)
        return hi

    def report(self):
        s = FORMATS[self.kind]['safe']
        issues = []
        for t in self.texts:
            x0, y0, x1, y1 = t['bbox_mm']
            if x0 < s[0] or y0 < s[1] or x1 > s[2] or y1 > s[3]:
                issues.append(f"文字超出安全區：{t['text']} {t['bbox_mm']}")
            if y0 < COIL:
                issues.append(f"文字進線圈區：{t['text']}")
            for p in self.photos:
                fx0, fy0, fx1, fy1 = p['frame_mm']
                if x0 < fx1 and x1 > fx0 and y0 < fy1 and y1 > fy0:
                    issues.append(f"文字壓到照片：{t['text']}")
        for p in self.photos:
            f = p.get('face')
            if f and not f['clear_of_coil']:
                issues.append(f"臉進線圈區：{p['cid']} 臉最上緣 {f['top_mm']} mm")
            if f and not f['complete_in_frame']:
                issues.append(f"臉不完整：{p['cid']}")
        dates = [t for t in self.texts if t['role'] == 'date']
        return {'id': self.id, 'kind': self.kind, 'role': self.role, 'face_no': self.face_no, 'size_mm': [self.Wmm, self.Hmm],
                'safe_mm': list(s), 'safe_note': FORMATS[self.kind]['safe_note'], 'photos': self.photos,
                'min_text_em_pt': min(t['em_pt'] for t in self.texts) if self.texts else None,
                'min_date_em_pt': min(t['em_pt'] for t in dates) if dates else None,
                'min_date_em_mm': min(t['em_mm'] for t in dates) if dates else None,
                'texts': self.texts, 'lattices': self.lattices, 'issues': issues}


# ---------- 版面 ----------
def head_block(pg, x, y, M, s, scale=1.0):
    pg.text((x, y), f'{M["m"]:02d}', 15 * scale, FONT_LAT_B, INK, 'la', 'month_no')
    pg.text((x + 24 * scale, y + 2.0 * scale), EN[M['m'] - 1], 4.2 * scale, FONT_LAT, MUTED, 'la', 'month_en')
    pg.text((x + 24 * scale, y + 8.2 * scale), f'2027 · {M["m"]} 月', 3.8 * scale, FONT_CJK, MUTED, 'la', 'month_zh')
    pg.text((x, y + 20 * scale), f'{M["en"]}  {M["zh"]}', 4.4 * scale, FONT_CJK, INK, 'la', 'name')
    pg.text((x, y + 26.5 * scale), M['tag'], 3.2 * scale, FONT_CJK, MUTED, 'la', 'tag')


def page_H_A(M, src, face_no):
    pg = Page(f'H_A_{M["m"]:02d}_{M["pid"]}', 'H', '橫式照片面（主推薦：橫 A）', face_no)
    pg.photo(src, 'H_A', fy=0.34)
    head_block(pg, 112, 16, M, 1.0)
    pg.month_grid((112, 52, 198, 140), M['m'], 4.6, 3.3)
    pg.text((112, 148.5), DRAFT, 2.4, FONT_CJK, MUTED, 'ls', 'draft')
    pg.text((198, 148.5), BRAND, 2.6, FONT_CJK, MUTED, 'rs', 'brand')
    return pg


def lower_block_V(pg, M, y0):
    pg.text((12, y0), f'{M["m"]:02d}', 11, FONT_LAT_B, INK, 'la', 'month_no')
    pg.text((31, y0 + 1.2), EN[M['m'] - 1], 3.3, FONT_LAT, MUTED, 'la', 'month_en')
    pg.text((31, y0 + 6.0), f'2027 · {M["m"]} 月', 3.0, FONT_CJK, MUTED, 'la', 'month_zh')
    pg.text((12, y0 + 15.5), M['en'], 3.4, FONT_LAT, INK, 'la', 'name')
    pg.text((12, y0 + 20.8), M['zh'], 3.4, FONT_CJK, INK, 'la', 'name')
    pg.text((12, y0 + 26.2), M['tag'], 2.8, FONT_CJK, MUTED, 'la', 'tag')


def page_V(M, src, frame, face_no, page_id=None, note=None, **kw):
    pg = Page(page_id or f'{frame}_{M["m"]:02d}_{M["pid"]}', 'V', FRAMES[frame][2], face_no)
    pg.photo(src, frame, note=note, **kw)
    top = FRAMES[frame][1][3] + 4
    lower_block_V(pg, M, top + 1)
    pg.month_grid((60, top, 134, 196), M['m'], 3.3, 2.5)
    pg.text((12, 192.5), DRAFT, 2.2, FONT_CJK, MUTED, 'ls', 'draft')
    pg.text((12, 197.5), BRAND, 2.4, FONT_CJK, MUTED, 'ls', 'brand')
    return pg


def page_H_B(M, src):
    pg = Page(f'H_B_{M["m"]:02d}_{M["pid"]}', 'H', FRAMES['H_B'][2])
    pg.photo(src, 'H_B', fy=0.42)
    pg.text((8, 122), f'{M["m"]:02d}', 9, FONT_LAT_B, INK, 'la', 'month_no')
    pg.text((8, 133.5), f'{EN[M["m"] - 1]} 2027', 2.8, FONT_LAT, MUTED, 'la', 'month_en')
    pg.text((8, 138), f'{M["en"]} {M["zh"]}', 3.0, FONT_CJK, INK, 'la', 'name')
    pg.strip((46, 122, 198, 141), M['m'], 3.0)
    pg.text((8, 148.5), DRAFT, 2.2, FONT_CJK, MUTED, 'ls', 'draft')
    pg.text((198, 148.5), BRAND, 2.6, FONT_CJK, MUTED, 'rs', 'brand')
    return pg


def page_grid_H(M, small, spec, face_no):
    pg = Page(f'H_grid_{M["m"]:02d}_{M["pid"]}', 'H', '橫式大格月曆面（代表；含柔和近照小框）', face_no)
    fx0, fy0, fx1, fy1 = spec['small_frame_mm']
    c = spec['small_crop_frac']
    W, H = small.W, small.H
    x0, y0 = int(c[0] * W), int(c[1] * H)
    cw = int((c[2] - c[0]) * W)
    ch = int(round(cw * (fy1 - fy0) / (fx1 - fx0)))
    pg.photo(small, box=(fx0, fy0, fx1, fy1), crop=(x0, y0, cw, ch), note='柔和近照小框（裁到肩上，避開毛衣假字）')
    pg.text((fx0, fy1 + 5), f'{M["en"]}  {M["zh"]}', 3.6, FONT_CJK, INK, 'la', 'name')
    pg.text((fx0, fy1 + 10.5), M['tag'], 2.8, FONT_CJK, MUTED, 'la', 'tag')
    pg.text((68, 15), f'{M["m"]:02d}', 13, FONT_LAT_B, INK, 'la', 'month_no')
    pg.text((90, 17), f'{EN[M["m"] - 1]} 2027', 3.8, FONT_LAT, MUTED, 'la', 'month_en')
    pg.text((90, 23), f'2027 · {M["m"]} 月', 3.4, FONT_CJK, MUTED, 'la', 'month_zh')
    pg.month_grid((68, 34, 196, 142), M['m'], 5.2, 3.6, 'big_grid')
    pg.text((12, 143), DRAFT, 2.2, FONT_CJK, MUTED, 'ls', 'draft')
    pg.text((12, 148.5), BRAND, 2.6, FONT_CJK, MUTED, 'ls', 'brand')
    pg.text((196, 148.5), SRC_NOTE, 2.2, FONT_CJK, MUTED, 'rs', 'source_note')
    return pg


def page_grid_V(M, face_no):
    pg = Page(f'V_grid_{M["m"]:02d}_{M["pid"]}', 'V', '直式大格月曆面（代表）', face_no)
    pg.text((10, 15), f'{M["m"]:02d}', 13, FONT_LAT_B, INK, 'la', 'month_no')
    pg.text((32, 17), f'{EN[M["m"] - 1]} 2027', 3.8, FONT_LAT, MUTED, 'la', 'month_en')
    pg.text((32, 23), f'{M["en"]}  {M["zh"]}', 3.4, FONT_CJK, INK, 'la', 'name')
    pg.month_grid((8, 38, 136, 184), M['m'], 5.4, 3.8, 'big_grid')
    pg.text((8, 191.5), DRAFT, 2.2, FONT_CJK, MUTED, 'ls', 'draft')
    pg.text((8, 197.5), BRAND, 2.4, FONT_CJK, MUTED, 'ls', 'brand')
    pg.text((136, 197.5), SRC_NOTE, 2.2, FONT_CJK, MUTED, 'rs', 'source_note')
    return pg


def page_year(face_no):
    pg = Page('V_year_2027', 'V', '直式年曆（面 31）', face_no)
    pg.text((72, 14), '2027', 12, FONT_LAT_B, INK, 'ma', 'title')
    pg.text((72, 29.5), '全年年曆', 3.4, FONT_CJK, MUTED, 'ma', 'title')
    x0, y0, cwid, rhei, gap = 8, 38, 40.0, 36.5, 4.0
    for i in range(12):
        c, r = i % 3, i // 3
        bx, by = x0 + c * (cwid + gap), y0 + r * (rhei + gap * 0.4)
        pg.text((bx, by), f'{i + 1} 月', 2.9, FONT_CJK, INK, 'la', 'mini_title')
        pg.month_grid((bx, by + 4.6, bx + cwid, by + rhei), i + 1, 2.5, 1.9, 'mini')
    pg.text((8, 191.5), DRAFT, 2.2, FONT_CJK, MUTED, 'ls', 'draft')
    pg.text((8, 197.5), BRAND, 2.4, FONT_CJK, MUTED, 'ls', 'brand')
    pg.text((136, 197.5), SRC_NOTE, 2.2, FONT_CJK, MUTED, 'rs', 'source_note')
    return pg


def head_tile(src):
    """封面用頭像：以臉高為基準取 2.0 × 2.6 臉高的範圍（只裁切）。"""
    P = src.g['P']
    fh = float(P[152][1] - P[10][1])
    cx, cy = float(P[:, 0].mean()), float((P[10][1] + P[152][1]) / 2)
    w, h = fh * 2.0, fh * 2.6
    sc = min(1.0, src.W / w, src.H / h)  # 特寫圖的頭像範圍不超出原圖
    w, h = w * sc, h * sc
    return int(cx - w / 2), int(cy - h * 0.42), int(w), int(h)


def page_cover(kind, months, srcs, face_no):
    pg = Page(f'{kind}_cover', kind, f'{"橫" if kind == "H" else "直"}式封面草稿', face_no)
    Wm = FORMATS[kind]['W']
    pg.text((Wm / 2, 14), '2027', 16 if kind == 'H' else 15, FONT_LAT_B, INK, 'ma', 'title')
    pg.text((Wm / 2, 33.5), '12 位虛擬 KOL・12 種長相', 4.4, FONT_CJK, INK, 'ma', 'tagline_placeholder')
    pg.text((Wm / 2, 40.5), BRAND, 3.0, FONT_CJK, MUTED, 'ma', 'brand')
    cols, area = (6, (8, 46, 196, 144)) if kind == 'H' else (4, (8, 50, 136, 190))
    rows = 12 // cols
    gap, lab = 2.2, 4.4
    tw = (area[2] - area[0] - gap * (cols - 1)) / cols
    th = (area[3] - area[1] - gap * (rows - 1) - rows * lab) / rows
    for i, M in enumerate(months):
        s = srcs[M['V']]
        x, y = area[0] + (i % cols) * (tw + gap), area[1] + (i // cols) * (th + gap + lab)
        hx, hy, hw, hh = head_tile(s)
        a = tw / th
        if hw / hh > a:
            nw = int(hh * a)
            hx, hw = hx + (hw - nw) // 2, nw
        else:
            hh = int(hw / a)
        hx, hy = max(0, min(hx, s.W - hw)), max(0, min(hy, s.H - hh))
        pg.photo(s, box=(x, y, x + tw, y + th), crop=(hx, hy, hw, hh), note='封面頭像')
        pg.text((x + tw / 2, y + th + 0.8), M['en'].split()[0], 2.8, FONT_LAT, INK, 'ma', 'cover_name')
    pg.text((Wm - 8, FORMATS[kind]['H'] - 6.5), DRAFT, 2.2, FONT_CJK, MUTED, 'rs', 'draft')
    return pg


# ---------- 日期輸出驗證（讀回實際輸出的 300 dpi 檔） ----------
_GLYPH = {}


def glyph(text, path, size_px):
    k = (text, path, size_px)
    if k not in _GLYPH:
        f = ImageFont.truetype(path, size_px)
        im = Image.new('L', (size_px * 4, size_px * 2), 255)
        ImageDraw.Draw(im).text((size_px // 2, size_px // 3), text, fill=0, font=f)
        a = np.asarray(im) < 140
        ys, xs = np.where(a)
        _GLYPH[k] = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    return _GLYPH[k]


def read_cell(arr, box_px, cands, path, size_px):
    x0, y0, x1, y1 = box_px
    c = arr[y0:y1, x0:x1].astype(int)
    ink = c.min(-1) < 140
    if ink.sum() < 8:
        return None, 0.0, None
    ys, xs = np.where(ink)
    g = ink[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    core = c[ink]
    color = 'red' if float(core[:, 0].mean() - core[:, 1].mean()) > 60 else 'ink'
    best, score = None, 0.0
    for t in cands:
        r = glyph(t, path, size_px)
        if abs(r.shape[0] - g.shape[0]) > 3 or abs(r.shape[1] - g.shape[1]) > 3:
            continue
        h, w = min(r.shape[0], g.shape[0]), min(r.shape[1], g.shape[1])
        inter = (r[:h, :w] & g[:h, :w]).sum()
        uni = r.sum() + g.sum() - inter
        s = inter / uni if uni else 0
        if s > score:
            best, score = t, s
    return best, round(float(score), 3), color


def verify_dates(rep, hires_path):
    arr = np.asarray(Image.open(hires_path).convert('RGB'))
    res = {'page': rep['id'], 'cells_checked': 0, 'dates_matched': 0, 'min_date_score': 1.0, 'failures': []}
    days = [str(i) for i in range(1, 32)]
    for L in rep['lattices']:
        if L['type'] == 'month':
            x0, y0, x1, y1 = L['box']
            cw, rh, hh = (x1 - x0) / 7, (y1 - y0 - L['head_h']) / 6, L['head_h']
            dsz, hsz = int(round(L['digit_mm'] * MM)), int(round(L['head_mm'] * MM))
            weeks = calendar.Calendar(firstweekday=6).monthdayscalendar(2027, L['m'])  # 與渲染器不同的推算方式
            weeks += [[0] * 7] * (6 - len(weeks))
            for k in range(7):
                t, s, col = read_cell(arr, (px(x0 + k * cw), px(y0), px(x0 + (k + 1) * cw), px(y0 + hh)), list(WEEK), FONT_CJK, hsz)
                res['cells_checked'] += 1
                if t != WEEK[k] or (col == 'red') != (k in (0, 6)):
                    res['failures'].append({'m': L['m'], 'cell': f'header col {k}', 'expected': WEEK[k], 'read': t, 'score': s, 'color': col})
            for r in range(6):
                for k in range(7):
                    exp = weeks[r][k]
                    box = (px(x0 + k * cw), px(y0 + hh + r * rh), px(x0 + (k + 1) * cw), px(y0 + hh + (r + 1) * rh))
                    t, s, col = read_cell(arr, box, days, FONT_LAT, dsz)
                    res['cells_checked'] += 1
                    want_red = bool(exp) and OFF[f'2027-{L["m"]:02d}-{exp:02d}']
                    ok = (t is None and not exp) or (exp and t == str(exp) and s >= 0.6 and (col == 'red') == want_red)
                    if ok and exp:
                        res['dates_matched'] += 1
                        res['min_date_score'] = min(res['min_date_score'], s)
                    if not ok:
                        res['failures'].append({'m': L['m'], 'cell': f'r{r}c{k}', 'expected': exp or '空白', 'read': t, 'score': s,
                                                'color': col, 'want_red': want_red})
        elif L['type'] == 'strip':
            x0, y0, x1, y1 = L['box']
            n = L['n']
            cw, hrow = (x1 - x0) / n, (y1 - y0) / 2
            dsz, wsz = int(round(L['digit_mm'] * MM)), int(round(L['digit_mm'] * 0.8 * MM))
            for i in range(n):
                day = i + 1
                dow = WEEK[calendar.weekday(2027, L['m'], day) - 6]
                want_red = OFF[f'2027-{L["m"]:02d}-{day:02d}']
                t1, s1, c1 = read_cell(arr, (px(x0 + i * cw), px(y0), px(x0 + (i + 1) * cw), px(y0 + hrow)), list(WEEK), FONT_CJK, wsz)
                t2, s2, c2 = read_cell(arr, (px(x0 + i * cw), px(y0 + hrow), px(x0 + (i + 1) * cw), px(y1)), days, FONT_LAT, dsz)
                res['cells_checked'] += 2
                if t2 == str(day):
                    res['dates_matched'] += 1
                    res['min_date_score'] = min(res['min_date_score'], s2)
                if t1 != dow or t2 != str(day) or (c2 == 'red') != want_red or (c1 == 'red') != want_red:
                    res['failures'].append({'m': L['m'], 'cell': f'day {day}', 'expected': [dow, day, want_red], 'read': [t1, t2, c1, c2], 'score': [s1, s2]})
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hf-dir', required=True)
    ap.add_argument('--cache', required=True)
    a = ap.parse_args()
    picks = json.load(open(os.path.join(CAL, 'data', 'cal_r3_picks.json')))
    J = {c['cid']: c for c in json.load(open(os.path.join(CAL, 'data', 'cal_r2_judgments.json')))['candidates']}
    R = json.load(open(os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')))['items']
    clean = {c['cid']: c for c in json.load(open(os.path.join(CAL, 'data', 'cal_r3_cleanup_report.json')))['items']}
    months = picks['months']
    assert [M['m'] for M in months] == list(range(1, 13)), '月份不漏不重複'
    assert len({M['pid'] for M in months}) == 12, '12 位不同人設'
    need = {M['H'] for M in months} | {M['V'] for M in months} | {picks['grid_faces']['H']['small_photo']} | set(picks['kanon_v_check'])
    srcs = {cid: Source(cid, J, R, clean, a.hf_dir, a.cache) for cid in sorted(need)}
    pages = []
    for M in months:
        pages.append((page_H_A(M, srcs[M['H']], 2 * M['m']), 'main'))
        pages.append((page_V(M, srcs[M['V']], 'V_U', 2 * M['m'], fy=0.36), 'main'))
    gH, gV = picks['grid_faces']['H'], picks['grid_faces']['V']
    MH = next(M for M in months if M['m'] == gH['m'])
    MV = next(M for M in months if M['m'] == gV['m'])
    pages.append((page_grid_H(MH, srcs[gH['small_photo']], gH, 2 * gH['m'] + 1), 'main'))
    pages.append((page_grid_V(MV, 2 * gV['m'] + 1), 'main'))
    pages.append((page_year(31), 'main'))
    pages.append((page_cover('H', months, srcs, 1), 'main'))
    pages.append((page_cover('V', months, srcs, 1), 'main'))
    for pid in picks['compare_VA']:
        M = next(x for x in months if x['pid'] == pid)
        pages.append((page_V(M, srcs[M['V']], 'V_A', None, fy=0.36), 'compare'))
    for M in months:
        pages.append((page_H_B(M, srcs[M['H']]), 'compare'))
    MK = next(x for x in months if x['pid'] == 'kanon-komori')
    for cid in picks['kanon_v_check']:
        for fr in (('V_A', 'V_B_R2', 'V_U') if cid == 'kanon_V' else ('V_U',)):
            pages.append((page_V(MK, srcs[cid], fr, None, page_id=f'CHK_kanon_{cid}_{fr}', fy=0.36), 'check'))

    reports, checks = [], []
    for pg, group in pages:
        sub = {'main': 'pages', 'compare': 'compare', 'check': 'checks'}[group]
        hi = pg.save(sub)
        rep = pg.report()
        rep['group'] = group
        for ph_ in rep['photos']:
            mc = picks.get('manual_checks', {})
            ph_['hair']['manual_check'] = mc.get(pg.id, '未目視') if ph_['note'] is None else mc.get(f'{pg.id}#{ph_["cid"]}', '—（封面頭像）')
        rep['hires'] = os.path.relpath(hi, CAL)
        rep['preview'] = os.path.relpath(os.path.join(OUT, sub, f'{pg.id}.jpg'), CAL)
        reports.append(rep)
        if rep['lattices']:
            c = verify_dates(rep, hi)
            c['group'] = group
            checks.append(c)
        print(pg.id, 'issues', len(rep['issues']), 'date failures', len(checks[-1]['failures']) if rep['lattices'] else '-')

    json.dump({'generated_by': 'docs/calendar/tools/build_cal_r3_pages.py', 'dpi': DPI, 'coil_mm': COIL, 'trim_mm': TRIM,
               'frames': {k: {'format': v[0], 'mm': v[1], 'label': v[2]} for k, v in FRAMES.items()},
               'ppi_note': 'ppi_w／ppi_h＝裁切後原圖原生像素 ÷ 照片框英吋；upscaled_in_render＝排版時把像素放大到 300 dpi 輸出（不代表原圖細節足夠）',
               'pages': reports}, open(os.path.join(CAL, 'data', 'cal_r3_layout_report.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump({'generated_by': 'docs/calendar/tools/build_cal_r3_pages.py',
               'method': '讀回實際輸出的 300 dpi JPEG；依格線幾何切出每一格（不使用渲染時的文字位置）；以同字型字形比對讀出數字／星期，以墨色判定紅黑；'
                         '期望值用 calendar.monthdayscalendar 另行推算，紅字依人事總處放假日。',
               'pages': checks}, open(os.path.join(CAL, 'data', 'cal_r3_date_check.json'), 'w'), ensure_ascii=False, indent=1)
    tables(reports, checks)


def tables(reports, checks):
    L = ['# CAL_14b — R3 版面量測表（程式產生，請勿手改）', '',
         '> 由 `docs/calendar/tools/build_cal_r3_pages.py` 從實際渲染的頁面產生；原始資料 `data/cal_r3_layout_report.json`。',
         '> 座標都是含 2 mm 出血的畫布 mm；裁切線＝畫布內縮 2 mm；假設線圈區＝畫布上緣 0–12 mm。',
         '> 有效 ppi＝裁切後**原圖原生像素** ÷ 照片框英吋（ppi_w 以寬計、ppi_h 以高計）；「渲染時放大」只表示輸出 300 dpi 時像素被拉大，不代表原圖細節足夠。',
         '> 髮頂：程式判定（selfie_multiclass 頭髮類別最上緣）＋人工目視欄；「原圖已缺髮頂」＝頭髮碰到原圖上緣。', '']
    groups = (('main', '## 1. 主推薦暫定工作稿（橫 A＋直式統一框，各 12 面；封面與大格月曆面另列）'),
              ('compare', '## 2. 比較樣張（原直 A、橫 B 192×104）'), ('check', '## 3. Kanon 直式重查'))
    for g, title in groups:
        L += [title, '', '| 頁 | 面 | 照片框（mm） | 圖片 ID｜使用檔 | 原圖 px | 裁切 x,y,w,h（原圖 px） | 原生 px | ppi w／h | 渲染時放大 | 臉最上緣／下巴 mm | 臉完整｜避開線圈 | 髮頂（程式） | 髮頂 mm | 目視 |',
              '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
        for r in reports:
            if r['group'] != g:
                continue
            for p in r['photos']:
                if p['note'] == '封面頭像':
                    continue
                f = p.get('face') or {}
                L.append(f"| {r['id']} | {r['face_no'] or '—'} | {p['frame']} {p['frame_mm']} | {p['cid']}｜{'清理版' if p['used_file'] == 'clean' else '原圖'} | "
                         f"{p['source_px'][0]}×{p['source_px'][1]} | {','.join(map(str, p['crop_px']))} | {p['native_px'][0]}×{p['native_px'][1]} | "
                         f"{p['ppi_w']}／{p['ppi_h']} | {'是' if p['upscaled_in_render'] else '否'} | {f.get('top_mm', '—')}／{f.get('chin_mm', '—')} | "
                         f"{'是' if f.get('complete_in_frame') else '否'}｜{'是' if f.get('clear_of_coil') else '否'} | {p['hair']['status_auto']} | "
                         f"{p['hair']['top_mm_est'] if p['hair']['top_mm_est'] is not None else '—'} | {p['hair']['manual_check']} |")
        L.append('')
    covers = [r for r in reports if r['id'].endswith('_cover')]
    L += ['## 4. 封面頭像格', '', '| 封面 | 格數 | 每格 mm | 最低有效 ppi | 最低臉最上緣 mm | 全部臉完整 |', '|---|---|---|---|---|---|']
    for r in covers:
        ps = r['photos']
        L.append(f"| {r['id']} | {len(ps)} | {ps[0]['frame_size_mm'][0]:.1f}×{ps[0]['frame_size_mm'][1]:.1f} | {min(p['ppi_w'] for p in ps)} | "
                 f"{min(p['face']['top_mm'] for p in ps)} | {'是' if all(p['face']['complete_in_frame'] for p in ps) else '否'} |")
    L += ['', '## 5. 文字與邊界檢查', '', '| 頁 | 文字數 | 最小文字 em（pt） | 最小日期字 em（pt／mm） | 安全區（mm） | 問題 |', '|---|---|---|---|---|---|']
    for r in reports:
        L.append(f"| {r['id']} | {len(r['texts'])} | {r['min_text_em_pt']} | {r['min_date_em_pt'] or '—'}／{r['min_date_em_mm'] or '—'} | {r['safe_mm']} | {'；'.join(r['issues']) or '無'} |")
    L.append('')
    open(os.path.join(CAL, 'CAL_14b_LAYOUT_TABLE.generated.md'), 'w').write('\n'.join(L))
    D = ['# CAL_15b — 自繪日期「實際輸出頁」核對結果（程式產生，請勿手改）', '',
         '> 由 `docs/calendar/tools/build_cal_r3_pages.py` 產生；原始資料 `data/cal_r3_date_check.json`。',
         '> 方法：讀回實際輸出的 300 dpi JPEG，依格線幾何切出每一格（不用渲染時記下的文字位置），以同字型字形比對讀出數字或星期、以墨色判定紅黑；'
         '期望值以 `calendar.monthdayscalendar` 另行推算（渲染器用的是 `datetime`），紅字依人事總處放假日。每月固定 6 列，不併格。',
         '> 負向測試：`tools/test_cal_r3_datecheck.py` 把 1 月橫 A 的輸出檔改成「1/4 改紅、1/15 擦掉、1/10 改寫成 9」，核對程式三處都抓到、沒有誤報（說明見 `CAL_08_DATES_2027.md` §6）。', '',
         '| 頁 | 群組 | 檢查格數 | 讀到的日期 | 最低比對分數 | 失敗 |', '|---|---|---|---|---|---|']
    for c in checks:
        D.append(f"| {c['page']} | {c['group']} | {c['cells_checked']} | {c['dates_matched']} | {c['min_date_score']} | {len(c['failures'])} |")
    D += ['', f"合計：{len(checks)} 頁、{sum(c['cells_checked'] for c in checks)} 格、讀到 {sum(c['dates_matched'] for c in checks)} 個日期、失敗 {sum(len(c['failures']) for c in checks)}。", '']
    open(os.path.join(CAL, 'CAL_15b_DATE_OUTPUT_CHECK.generated.md'), 'w').write('\n'.join(D))


if __name__ == '__main__':
    main()
