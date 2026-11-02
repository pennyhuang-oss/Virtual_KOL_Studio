"""TASK-CAL-001 M-5 R32：四季光影淺深雙款＋兌心科技品牌（橫式淺色 1／2、直式深色 1／2）；不生成、不付費、不買素材。

- 橫式淺色：背景沿用 R31 A（build_cal_m5_cover_r31.svg_a 的 H-A 畫面，不改）；「2027」改為統一的深藍。
- 直式深色：近黑深藍底，局部光帶（藍色水紋、藍紫霧光、少量暖光），保留大片暗部；「2027」柔白偏淺藍。
- 品牌：官網正式 Logo（docs/calendar/cover_r32/brand/insight-software-logo-official.svg：藍色圖示＋深色「Insight Software」字標，向量原樣、等比縮放）。
  淺色版用官方配色；深色版沒有查到官方反白檔，改用同一組向量路徑改填白色的「設計衍生版」（待 Owner 確認，不是官方版本）。
  中文「兌心科技」以 Noto Sans TC Medium 排在 Logo 旁，與 Logo 裡的英文合成完整名稱，不重複英文。不放標語、網址；DESK CALENDAR 拿掉。
- 每款兩個版本共用同一張背景，只差年份與品牌區的位置、比例與編排。
- 輸出：可編輯來源 docs/calendar/cover_r32/{H-L1,H-L2,V-D1,V-D2}.svg（＋fonts、brand）；預覽 docs/calendar/decision_site/public/cover32/；
  每張候選一份完整預覽 PDF（封面＋R26 已接受內頁：橫式 28 面、直式 32 面），R26 正式預覽不覆蓋。
用法：python3 docs/calendar/tools/build_cal_m5_cover_r32.py [--check]
"""
import argparse
import hashlib
import io
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_cal_m5_cover_r31 as R31  # noqa: E402

ROUND = 'M-5 R32'
SRC_REL = 'docs/calendar/cover_r32'
FONT_REL = SRC_REL + '/fonts'
LOGO_REL = SRC_REL + '/brand/insight-software-logo-official.svg'
LOGO_SHA = 'f7c3ff90ff069faaf60d1f961b5e08e4c697b3a06f5a14d46c947b92a5fcc05a'
LOGO_URL = 'https://www.insight-software.com/template/img/tw/logo/logo01.svg'
PUB_REL = 'docs/calendar/decision_site/public/cover32'
DATA_REL = 'docs/calendar/data/cal_m5_cover_r32.json'
FMT, PT, TEXT_MARGIN = R31.FMT, R31.PT, R31.TEXT_MARGIN
COVERS = ('H-L1', 'H-L2', 'V-D1', 'V-D2')
FACES = {'H': 28, 'V': 32}
FONTS = {
    'year': {'file': 'CormorantGaramond-Light-LF.ttf', 'family': 'Cormorant Garamond Light', 'license': 'OFL-CormorantGaramond.txt',
             'note': '與 R31 相同（Google Fonts 開源庫 Cormorant Garamond；固定 wght 300、齊線數字預設、只留拉丁字元）'},
    'cjk': {'file': 'NotoSansTC-Medium-subset.ttf', 'family': 'Noto Sans TC Medium', 'license': 'OFL-NotoSansTC.txt',
            'upstream': 'https://raw.githubusercontent.com/google/fonts/main/ofl/notosanstc/NotoSansTC%5Bwght%5D.ttf',
            'upstream_sha256': '864727d210d54f2537bbe23b3a839436c3992af72de9322af5270897246bd44f',
            'note': '可變字型固定為 wght 500，只保留「兌心科技」與基本拉丁字元'},
}
# ---------- 配色（品牌藍為主軸） ----------
BRAND_BLUE = '#2B33F2'     # 官網 Logo 圖示色
WORDMARK = '#231815'       # 官網 Logo 字標色
LIGHT = {'year': '#1E2A78', 'cjk': '#1E2A78', 'rule': '#1E2A78'}           # 淺色版：深品牌藍（同色相、壓低明度）
DARK = {'year': '#E6ECFF', 'cjk': '#FFFFFF', 'rule': '#C9D4FF', 'logo': '#FFFFFF'}   # 深色版：柔白偏淺藍；Logo 衍生版為白
# ---------- 版面（mm，含出血畫布座標） ----------
LOGO_VIS = (0.0, 0.0, 176.21, 40.98)   # 官網 Logo 可見外框（viewBox 200×41 右側 24 單位是空白）
LAYOUT = {
    'H-L1': dict(year=dict(x=188.5, y=140, size=46, anchor='end'),
                 brand=dict(x=15.5, bottom=140, logo_w=30.0, cjk_size=3.5, gap=3.2, rule=True, anchor='start'),
                 label='年份右下；品牌區在左下，底線與年份對齊'),
    'H-L2': dict(year=dict(x=188.5, y=140, size=42, anchor='end'),
                 brand=dict(x=188.5, bottom=100.5, logo_w=26.0, cjk_size=3.1, gap=2.8, rule=True, anchor='end'),
                 label='年份與品牌疊成一組：品牌在年份正上方、右緣對齊'),
    'V-D1': dict(year=dict(x=13.5, y=176, size=44, anchor='start'),
                 brand=dict(x=15.0, bottom=191.5, logo_w=27.0, cjk_size=3.2, gap=2.9, rule=True, anchor='start'),
                 label='年份左下；品牌區在年份下方、左緣對齊'),
    'V-D2': dict(year=dict(x=72.0, y=172, size=40, anchor='middle'),
                 brand=dict(x=72.0, bottom=191.5, logo_w=26.0, cjk_size=3.1, gap=2.8, rule=True, anchor='middle'),
                 label='置中排列：年份在下方三分之一、品牌區在底部置中'),
}
YEAR_LS = 0.8


def sha256(b):
    return hashlib.sha256(b).hexdigest()


# ---------- 字寬與字形外框 ----------
_TT = {}


def tt(k):
    if k not in _TT:
        from fontTools.pens.boundsPen import BoundsPen
        from fontTools.ttLib import TTFont
        f = TTFont(os.path.join(ROOT, FONT_REL, FONTS[k]['file']))
        gs, cmap = f.getGlyphSet(), f.getBestCmap()
        chars = '2027' if k == 'year' else '兌心科技'
        bounds = {}
        for c in set(chars):
            bp = BoundsPen(gs)
            gs[cmap[ord(c)]].draw(bp)
            bounds[c] = bp.bounds
        _TT[k] = {'upm': f['head'].unitsPerEm, 'adv': {c: f['hmtx'][cmap[ord(c)]][0] for c in bounds}, 'bounds': bounds}
    return _TT[k]


def text_box(k, s, size, ls, x, y, anchor='start'):
    T = tt(k)
    sc = size / T['upm']
    adv = [T['adv'][c] * sc for c in s]
    width = sum(adv) + ls * (len(s) - 1)
    x0 = x - width if anchor == 'end' else x - width / 2 if anchor == 'middle' else x
    xmin = ymin = 1e9
    xmax = ymax = -1e9
    cx = x0
    for c, a in zip(s, adv):
        b = T['bounds'][c]
        xmin, xmax = min(xmin, cx + b[0] * sc), max(xmax, cx + b[2] * sc)
        ymin, ymax = min(ymin, y - b[3] * sc), max(ymax, y - b[1] * sc)
        cx += a + ls
    return {'x': x0, 'y': y, 'width': width, 'ink': [xmin, ymin, xmax, ymax]}


# ---------- Logo ----------
def logo_paths():
    t = open(os.path.join(ROOT, LOGO_REL), encoding='utf-8').read()
    assert sha256(t.encode('utf-8')) == LOGO_SHA, '官網 Logo 檔與紀錄不同'
    return [(c, re.sub(r'\s+', ' ', d).strip()) for c, d in re.findall(r'<path class="(st\d)" d="([^"]+)"', t, re.S)]


def _wordmark_cap():
    """字標第一行「I」的高度（Logo 原座標）＝字標大寫高度，用來換算成品可讀性。"""
    from fontTools.pens.boundsPen import BoundsPen
    from fontTools.svgLib.path import parse_path
    hs = []
    for c, d in logo_paths():
        if c == 'st1':
            bp = BoundsPen(None)
            parse_path(d, bp)
            x0, y0, x1, y1 = bp.bounds
            if y1 < 21 and (x1 - x0) < 6:
                hs.append(y1 - y0)
    return max(hs)


WORDMARK_CAP = None


def brand_geom(cid):
    """品牌區：[Logo（圖示＋Insight Software 字標）] │ 兌心科技。回傳各元素在畫布上的位置（mm）。"""
    B = LAYOUT[cid]['brand']
    s = B['logo_w'] / LOGO_VIS[2]
    lh = LOGO_VIS[3] * s
    top = B['bottom'] - lh
    cjk = text_box('cjk', '兌心科技', B['cjk_size'], 0.12 * B['cjk_size'], 0, 0)
    total = B['logo_w'] + 2 * B['gap'] + cjk['width']
    x0 = B['x'] - total if B['anchor'] == 'end' else B['x'] - total / 2 if B['anchor'] == 'middle' else B['x']
    rule_x = x0 + B['logo_w'] + B['gap']
    cy = top + lh / 2
    base = cy - (cjk['ink'][1] + cjk['ink'][3]) / 2   # 讓中文字形外框垂直置中於 Logo
    cx = rule_x + B['gap']
    cj = text_box('cjk', '兌心科技', B['cjk_size'], 0.12 * B['cjk_size'], cx, base)
    return {'logo': (x0, top, s), 'logo_box': [x0, top, x0 + B['logo_w'], top + lh], 'rule': (rule_x, top + lh * 0.12, rule_x, top + lh * 0.88),
            'cjk': cj, 'cjk_size': B['cjk_size'], 'cjk_ls': 0.12 * B['cjk_size'], 'box': [x0, min(top, cj['ink'][1]), x0 + total, max(top + lh, cj['ink'][3])]}


def year_geom(cid):
    Y = LAYOUT[cid]['year']
    return text_box('year', '2027', Y['size'], YEAR_LS, Y['x'], Y['y'], Y['anchor'])


def fmt(v):
    return f'{v:.3f}'.rstrip('0').rstrip('.')


def font_css():
    return '<style>' + ''.join(f"@font-face{{font-family:'{F['family']}';src:url('fonts/{F['file']}')}}" for F in FONTS.values()) + \
        ".txt text{font-kerning:none;font-feature-settings:'kern' 0,'liga' 0}</style>"


def svg_brand_text(cid, dark):
    C = DARK if dark else LIGHT
    yg, bg = year_geom(cid), brand_geom(cid)
    x, top, s = bg['logo']
    o = ['<g class="txt">',
         f'<text x="{fmt(yg["x"])}" y="{fmt(yg["y"])}" font-family="&apos;{FONTS["year"]["family"]}&apos;" font-size="{LAYOUT[cid]["year"]["size"]}" letter-spacing="{YEAR_LS}" fill="{C["year"]}">2027</text>',
         f'<text x="{fmt(bg["cjk"]["x"])}" y="{fmt(bg["cjk"]["y"])}" font-family="&apos;{FONTS["cjk"]["family"]}&apos;" font-size="{fmt(bg["cjk_size"])}" letter-spacing="{fmt(bg["cjk_ls"])}" fill="{C["cjk"]}">兌心科技</text>',
         '</g>', '<g class="vec">']
    rx1, ry1, rx2, ry2 = bg['rule']
    o.append(f'<line x1="{fmt(rx1)}" y1="{fmt(ry1)}" x2="{fmt(rx2)}" y2="{fmt(ry2)}" stroke="{C["rule"]}" stroke-width="0.15" stroke-opacity="0.55"/>')
    tag = 'Logo 設計衍生版（官網向量改填白色，待 Owner 確認，非官方版本）' if dark else 'Logo 官方原色（官網 logo01.svg 向量，等比縮放）'
    o.append(f'<g id="logo" transform="translate({fmt(x)} {fmt(top)}) scale({fmt(s)})"><desc>{tag}</desc>')
    for c, d in logo_paths():
        if dark:
            fill = DARK['logo']
        else:
            fill = BRAND_BLUE if c == 'st0' else WORDMARK
        rule = ' fill-rule="evenodd" clip-rule="evenodd"' if c == 'st0' else ''
        o.append(f'<path d="{d}" fill="{fill}"{rule}/>')
    o.append('</g></g>')
    return o


# ---------- 背景 ----------
def light_art():
    """橫式淺色背景＝R31 A 橫式的畫面原樣（defs 與 art 群組）。"""
    s = R31.svg_a('H-A')
    defs = s[s.index('<defs>'):s.index('</defs>') + len('</defs>')]
    art = s[s.index('<g id="art">'):s.index('<defs><linearGradient id="ink"')]
    return defs, art.rstrip()


DARK_SEASON = [(0, '#7A6BC8'), (0.2, '#7F80D6'), (0.36, '#5682DC'), (0.5, '#4A8CE8'), (0.62, '#D9A274'), (0.7, '#9F86D0'), (0.86, '#6370D6'), (1, '#33429F')]
DARK_SPEC = dict(axis='y', ribbons=[(4, 214, 82, 22, 230, 2.0, 50, 36, 7, 1.3), (4, 214, 81, 21, 230, 2.1, 24, 16, 5, 2.1), (4, 214, 80, 20, 230, 2.2, 8, 4, 3, 0.4)],
                 slope=-0.08, mid=110,
                 seg=dict(spring=[(0, 0.8), (0.18, 0.6), (0.32, 0)], summer=[(0.16, 0), (0.33, 1), (0.46, 0.7), (0.54, 0)],
                          autumn=[(0.46, 0), (0.56, 1), (0.63, 0.6), (0.7, 0)], winter=[(0.6, 0), (0.76, 1), (0.92, 0.5), (1, 0)]),
                 fade=[(0, 0.0), (0.06, 0.85), (0.6, 1), (0.82, 0.55), (1, 0.05)],
                 caus_f='0.05 0.15', mist_f='0.026 0.014', dap_f='0.13 0.1')


def dark_art():
    """直式深色背景：近黑深藍；一道光帶從右上斜落，只在光帶附近有光（藍色水紋、藍紫霧光、少量暖光），其餘保留暗部層次。"""
    W, H = FMT['V']['W'], FMT['V']['H']
    S = DARK_SPEC
    full = f'x1="0" y1="0" x2="0" y2="{H}"'
    d = ['<defs>',
         f'<linearGradient id="dbase" x1="0" y1="0" x2="0.35" y2="1"><stop offset="0" stop-color="#0B1226"/><stop offset="0.45" stop-color="#0A1022"/><stop offset="1" stop-color="#070B18"/></linearGradient>',
         f'<radialGradient id="dlift" cx="0.62" cy="0.38" r="0.62"><stop offset="0" stop-color="#1A2A5C" stop-opacity="0.55"/><stop offset="0.6" stop-color="#121D44" stop-opacity="0.25"/><stop offset="1" stop-color="#0A1022" stop-opacity="0"/></radialGradient>',
         f'<radialGradient id="dvig" cx="0.5" cy="0.45" r="0.85"><stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.45"/></radialGradient>',
         f'<linearGradient id="dseason" gradientUnits="userSpaceOnUse" {full}>' + ''.join(f'<stop offset="{a}" stop-color="{b}"/>' for a, b in DARK_SEASON) + '</linearGradient>',
         f'<linearGradient id="dfade" gradientUnits="userSpaceOnUse" {full}>' + ''.join(f'<stop offset="{a}" stop-color="#fff" stop-opacity="{b}"/>' for a, b in S['fade']) + '</linearGradient>',
         f'<mask id="m_fade"><rect width="{W}" height="{H}" fill="url(#dfade)"/></mask>']
    for name, pts in S['seg'].items():
        d.append(f'<linearGradient id="dg_{name}" gradientUnits="userSpaceOnUse" {full}>' + ''.join(f'<stop offset="{a}" stop-color="#fff" stop-opacity="{b}"/>' for a, b in pts) + '</linearGradient>')
        d.append(f'<mask id="dm_{name}"><rect width="{W}" height="{H}" fill="url(#dg_{name})"/></mask>')
    d.append(f'''<filter id="db1" x="-30" y="-30" width="{W + 60}" height="{H + 60}" filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="1.2"/></filter>
<filter id="db2" x="-30" y="-30" width="{W + 60}" height="{H + 60}" filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="3.8"/></filter>
<filter id="db3" x="-30" y="-30" width="{W + 60}" height="{H + 60}" filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="11"/></filter>
<filter id="dcaustic" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="{S['caus_f']}" numOctaves="2" seed="11" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.78 0 0 0 0 0.88 0 0 0 0 1 1 0 0 0 0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0 0 0 0 0.1 0.95 0.1 0 0 0 0 0"/></feComponentTransfer>
 <feGaussianBlur stdDeviation="0.1"/></filter>
<filter id="ddapple" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="{S['dap_f']}" numOctaves="3" seed="23" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 1 0 0 0 0 0.8 0 0 0 0 0.56 1 0 0 0 0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0 0 0 0 0 0.05 0.3 0.75 0.9 1"/></feComponentTransfer>
 <feGaussianBlur stdDeviation="0.7"/></filter>
<filter id="dmist" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="{S['mist_f']}" numOctaves="3" seed="5" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.62 0 0 0 0 0.6 0 0 0 0 1 0 0 1.6 0 -0.6"/>
 <feGaussianBlur stdDeviation="1.4"/></filter>
<filter id="dgrain" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="3.2" numOctaves="1" seed="3"/><feColorMatrix type="saturate" values="0"/></filter>''')
    rib = [R31.ribbon(*r, axis=S['axis'], slope=S['slope'], mid=S['mid']) for r in S['ribbons']]
    d.append(f'<mask id="dribMask"><path d="{rib[0]}" fill="#fff" filter="url(#db2)"/></mask>')
    d.append('</defs>')
    a = ['<g id="art">',
         f'<rect width="{W}" height="{H}" fill="url(#dbase)"/>',
         f'<rect width="{W}" height="{H}" fill="url(#dlift)"/>',
         '<g style="mix-blend-mode:screen" mask="url(#m_fade)">',
         f'<path d="{rib[0]}" fill="url(#dseason)" opacity="0.26" filter="url(#db3)"/>',
         f'<path d="{rib[0]}" fill="url(#dseason)" opacity="0.26" filter="url(#db2)"/>',
         f'<path d="{rib[1]}" fill="#AFC4FF" opacity="0.20" filter="url(#db2)"/>',
         f'<path d="{rib[2]}" fill="#DCE6FF" opacity="0.16" filter="url(#db1)"/>',
         f'<g mask="url(#dm_summer)"><g mask="url(#dribMask)"><rect width="{W}" height="{H}" fill="#3566C9" opacity="0.20"/>'
         f'<rect width="{W}" height="{H}" filter="url(#dcaustic)" opacity="0.62"/></g></g>',
         f'<g mask="url(#dm_autumn)"><g mask="url(#dribMask)"><rect width="{W}" height="{H}" fill="#C98A52" opacity="0.16"/>'
         f'<rect width="{W}" height="{H}" filter="url(#ddapple)" opacity="0.45"/></g></g>',
         f'<g mask="url(#dm_winter)"><rect width="{W}" height="{H}" filter="url(#dmist)" opacity="0.65"/></g>',
         f'<g mask="url(#dm_spring)"><g filter="url(#db3)"><circle cx="98" cy="32" r="13" fill="#B9A6F2" opacity="0.35"/><circle cx="80" cy="46" r="9" fill="#F2C8E6" opacity="0.18"/></g></g>',
         '</g>',
         f'<rect width="{W}" height="{H}" fill="url(#dvig)"/>',
         f'<rect width="{W}" height="{H}" filter="url(#dgrain)" opacity="0.05" style="mix-blend-mode:screen"/>',
         '</g>']
    return '\n'.join(d), '\n'.join(a)


def svg_cover(cid):
    k, dark = cid[0], cid[2] == 'D'
    F = FMT[k]
    W, H = F['W'], F['H']
    defs, art = dark_art() if dark else light_art()
    name = {'H-L1': '橫式淺色 版本 1', 'H-L2': '橫式淺色 版本 2', 'V-D1': '直式深色 版本 1', 'V-D2': '直式深色 版本 2'}[cid]
    o = [f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">',
         f'<title>2027 桌曆封面候選 {cid}｜{name}（四季光影＋兌心科技，含 2 mm 出血）</title>', font_css(), defs, art]
    o.extend(svg_brand_text(cid, dark))
    o.append('</svg>')
    return '\n'.join(o) + '\n'


# ---------- PDF ----------
class _RLPen:
    """把 SVG 路徑（Logo 原座標）畫進 reportlab 路徑：x' = x0 + s·x，y' = H − (y0 + s·y)（mm → pt）。"""
    def __init__(self, path, x0, y0, s, H):
        self.p, self.x0, self.y0, self.s, self.H = path, x0, y0, s, H
        self.cur = None

    def _t(self, pt):
        return ((self.x0 + self.s * pt[0]) * PT, (self.H - (self.y0 + self.s * pt[1])) * PT)

    def moveTo(self, pt):
        self.p.moveTo(*self._t(pt))
        self.cur = pt

    def lineTo(self, pt):
        self.p.lineTo(*self._t(pt))
        self.cur = pt

    def curveTo(self, *pts):
        a, b, c = pts[-3:]
        self.p.curveTo(*self._t(a), *self._t(b), *self._t(c))
        self.cur = c

    def qCurveTo(self, *pts):
        q, e = pts[0], pts[-1]
        p0 = self.cur
        c1 = (p0[0] + 2 / 3 * (q[0] - p0[0]), p0[1] + 2 / 3 * (q[1] - p0[1]))
        c2 = (e[0] + 2 / 3 * (q[0] - e[0]), e[1] + 2 / 3 * (q[1] - e[1]))
        self.curveTo(c1, c2, e)

    def closePath(self):
        self.p.close()

    def endPath(self):
        pass


def cover_pdf(cid, art_jpg, path):
    """封面一頁：畫面＝300 dpi JPEG；年份、中文名稱、細線與 Logo 都是向量；字型以 TrueType 子集嵌入。"""
    from fontTools.svgLib.path import parse_path
    from reportlab import rl_config
    from reportlab.lib.colors import HexColor
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.pdfgen.canvas import FILL_EVEN_ODD, FILL_NON_ZERO
    rl_config.useA85 = 0
    k, dark = cid[0], cid[2] == 'D'
    F = FMT[k]
    W, H = F['W'], F['H']
    for kk, Fo in FONTS.items():
        if 'R32-' + kk not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont('R32-' + kk, os.path.join(ROOT, FONT_REL, Fo['file'])))
    c = rl_canvas.Canvas(path, pagesize=(W * PT, H * PT), invariant=1, pageCompression=1, initialFontName='R32-cjk', initialFontSize=8)
    t = F['trim']
    c.setTrimBox((t * PT, t * PT, (W - t) * PT, (H - t) * PT))
    c.setBleedBox((0, 0, W * PT, H * PT))
    c.drawImage(ImageReader(io.BytesIO(open(art_jpg, 'rb').read())), 0, 0, W * PT, H * PT)
    C = DARK if dark else LIGHT
    yg, bg = year_geom(cid), brand_geom(cid)
    for key, s, size, ls, g, col in (('year', '2027', LAYOUT[cid]['year']['size'], YEAR_LS, yg, C['year']), ('cjk', '兌心科技', bg['cjk_size'], bg['cjk_ls'], bg['cjk'], C['cjk'])):
        to = c.beginText(g['x'] * PT, (H - g['y']) * PT)
        to.setFont('R32-' + key, size * PT)
        to.setCharSpace(ls * PT)
        to.setFillColor(HexColor(col))
        to.textOut(s)
        c.drawText(to)
    rx1, ry1, rx2, ry2 = bg['rule']
    c.saveState()
    c.setStrokeColor(HexColor(C['rule']))
    c.setStrokeAlpha(0.55)
    c.setLineWidth(0.15 * PT)
    c.line(rx1 * PT, (H - ry1) * PT, rx2 * PT, (H - ry2) * PT)
    c.restoreState()
    x0, y0, s = bg['logo']
    for cls, d in logo_paths():
        p = c.beginPath()
        parse_path(d, _RLPen(p, x0, y0, s, H))
        c.setFillColor(HexColor(DARK['logo'] if dark else (BRAND_BLUE if cls == 'st0' else WORDMARK)))
        c.drawPath(p, stroke=0, fill=1, fillMode=FILL_EVEN_ODD if cls == 'st0' else FILL_NON_ZERO)
    c.showPage()
    c.save()


def checks(cid):
    global WORDMARK_CAP
    if WORDMARK_CAP is None:
        WORDMARK_CAP = _wordmark_cap()
    """文字與品牌區的字形外框在文字安全區內再縮 TEXT_MARGIN、在線圈假設區以下；Logo 與中文的成品尺寸。"""
    F = FMT[cid[0]]
    sx0, sy0, sx1, sy1 = F['safe']
    lo = (sx0 + TEXT_MARGIN, max(sy0, F['coil']) + TEXT_MARGIN, sx1 - TEXT_MARGIN, sy1 - TEXT_MARGIN)
    inside = lambda b: b[0] >= lo[0] and b[1] >= lo[1] and b[2] <= lo[2] and b[3] <= lo[3]  # noqa: E731
    yg, bg = year_geom(cid), brand_geom(cid)
    s = bg['logo'][2]
    cj = bg['cjk']['ink']
    yb, lb = yg['ink'], bg['box']
    gap = max(lb[1] - yb[3], yb[1] - lb[3], lb[0] - yb[2], yb[0] - lb[2])
    return {'year_ink_mm': [round(v, 2) for v in yb], 'brand_box_mm': [round(v, 2) for v in lb],
            'year_in_safe': inside(yb), 'brand_in_safe': inside(lb), 'clear_gap_mm': round(gap, 2),
            'logo_width_mm': round(LOGO_VIS[2] * s, 2), 'logo_height_mm': round(LOGO_VIS[3] * s, 2),
            'wordmark_cap_height_mm': round(WORDMARK_CAP * s, 2), 'cjk_glyph_height_mm': round(cj[3] - cj[1], 2),
            'year_digit_height_mm': round(yb[3] - yb[1], 2)}


def build(src_dir, pub, data_path):
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import ArrayObject, ByteStringObject
    for d in (src_dir, pub):
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith(('.svg', '.jpg', '.pdf')):
                    os.unlink(os.path.join(d, fn))
        os.makedirs(d, exist_ok=True)
    for sub in ('fonts', 'brand'):
        if os.path.realpath(os.path.join(src_dir, sub)) != os.path.realpath(os.path.join(ROOT, SRC_REL, sub)):
            shutil.copytree(os.path.join(ROOT, SRC_REL, sub), os.path.join(src_dir, sub), dirs_exist_ok=True)
    LD = json.load(open(os.path.join(ROOT, R31.LAYOUT_DATA), encoding='utf-8'))
    lay_sha = {x['path']: x['sha256'] for x in LD['files']}
    files, covers, pdfs = {}, [], {}

    def save(name, data):
        open(os.path.join(pub, name), 'wb').write(data)
        files[name] = sha256(data)
    with tempfile.TemporaryDirectory() as tmp:
        for cid in COVERS:
            k = cid[0]
            F = FMT[k]
            svg = svg_cover(cid)
            sp = os.path.join(src_dir, f'{cid}.svg')
            open(sp, 'w', encoding='utf-8').write(svg)
            full = R31.render(sp, os.path.join(tmp, f'{cid}_full.png'), F['px'])
            art = R31.render(sp, os.path.join(tmp, f'{cid}_art.png'), F['px'], 'txt,vec')
            save(f'cover_{cid}_f.jpg', R31.jpeg(full, 90))
            view = full.resize(F['vpx'], Image.LANCZOS)
            save(f'cover_{cid}_v.jpg', R31.jpeg(view, 88))
            aj = os.path.join(tmp, f'{cid}_art.jpg')
            open(aj, 'wb').write(R31.jpeg(art, 95, 0))
            cp = os.path.join(tmp, f'{cid}.pdf')
            cover_pdf(cid, aj, cp)
            src = os.path.join(ROOT, R31.LAYOUT_PDF[k])
            assert sha256(open(src, 'rb').read()) == lay_sha[os.path.basename(src)], f'R26 {k} PDF 與紀錄不同'
            w = PdfWriter()
            w.add_page(PdfReader(cp).pages[0])
            base = PdfReader(src)
            for p in base.pages[1:]:
                w.add_page(p)
            w.add_metadata({'/Title': f'2027 桌曆 {F["zh"]} 封面候選 {cid} 完整預覽（R32，未定案）', '/Producer': 'cal2027 R32'})
            w._ID = ArrayObject([ByteStringObject(hashlib.md5(f'cal2027-R32-{cid}'.encode()).digest())] * 2)
            name = f'cal2027_{cid}_preview_R32.pdf'
            b = io.BytesIO()
            w.write(b)
            save(name, b.getvalue())
            pp = os.path.join(pub, name)
            R = PdfReader(pp)
            fonts = R31.pdf_fonts(pp, (1, 1))
            pim = np.asarray(R31.pdf_page_png(pp, 1, F['vpx'], tmp)).astype(int)
            diff = round(float(np.abs(pim - np.asarray(view).astype(int)).mean()), 2)
            pg = R.pages[0]
            pdfs[cid] = {'path': name, 'pages': len(R.pages), 'media_mm': [round(float(v) / PT, 2) for v in pg.mediabox[2:]],
                         'trim_mm': [round(float(v) / PT, 2) for v in pg.trimbox], 'cover_fonts': fonts, 'cover_vs_preview_mean_abs_diff': diff,
                         'interior_from': os.path.basename(src), 'bytes': os.path.getsize(pp)}
            covers.append({'id': cid, 'kind': k, 'tone': 'dark' if cid[2] == 'D' else 'light', 'version': int(cid[-1]), 'layout': LAYOUT[cid]['label'],
                           'source': f'{cid}.svg', 'source_sha256': sha256(svg.encode('utf-8')), 'px': list(F['px']),
                           'logo': 'derivative_white' if cid[2] == 'D' else 'official_colors', 'checks': checks(cid)})
    out = []
    for name, h in sorted(files.items()):
        e = {'path': name, 'sha256': h, 'bytes': os.path.getsize(os.path.join(pub, name))}
        if name.endswith('.jpg'):
            im = Image.open(os.path.join(pub, name))
            e['px'] = [im.width, im.height]
        out.append(e)
    D = {'round': ROUND,
         'note': '四季光影淺深雙款＋兌心科技品牌：橫式淺色版本 1／2、直式深色版本 1／2；每款兩個版本共用同一張背景。生成 0、付費 0、未購買素材；候選未接受，R26 正式預覽不覆蓋。',
         'logo': {'source_url': LOGO_URL, 'file': os.path.relpath(os.path.join(ROOT, LOGO_REL), os.path.join(ROOT, SRC_REL)), 'sha256': LOGO_SHA,
                  'official': '官網 logo01.svg：藍色圖示（#2B33F2）＋深色兩行字標「Insight Software」（#231815）；向量原樣、等比縮放',
                  'light_use': '橫式淺色兩版用官方原色',
                  'dark_use': '直式深色兩版用同一組向量路徑改填白色的設計衍生版——官網沒有找到官方反白檔；待 Owner 確認，不是官方版本',
                  'not_used': '官網同目錄的 logo02.svg 是另一家公司的標誌（非兌心科技），未使用'},
         'palette': {'brand_blue': BRAND_BLUE, 'wordmark': WORDMARK, 'light': LIGHT, 'dark': DARK},
         'fonts': [{'key': k, **{kk: v for kk, v in F.items()}} for k, F in FONTS.items()],
         'formats': {k: {kk: v for kk, v in F.items() if kk not in ('px', 'vpx')} | {'text_margin_mm': TEXT_MARGIN} for k, F in FMT.items()},
         'covers': covers, 'pdf': pdfs, 'files': out}
    with open(data_path, 'w', encoding='utf-8') as fh:
        json.dump(D, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    return D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.check:
        old = json.load(open(os.path.join(ROOT, DATA_REL), encoding='utf-8'))
        with tempfile.TemporaryDirectory() as tmp:
            D = build(os.path.join(tmp, 'src'), os.path.join(tmp, 'pub'), os.path.join(tmp, 'd.json'))
            same = json.loads(json.dumps(D, ensure_ascii=False)) == old
            pub = os.path.join(ROOT, PUB_REL)
            diff = [x['path'] for x in D['files'] if not os.path.exists(os.path.join(pub, x['path'])) or sha256(open(os.path.join(pub, x['path']), 'rb').read()) != x['sha256']]
            extra = sorted(set(os.listdir(pub)) - {x['path'] for x in D['files']})
            sdiff = [c['source'] for c in D['covers'] if open(os.path.join(tmp, 'src', c['source']), 'rb').read() != open(os.path.join(ROOT, SRC_REL, c['source']), 'rb').read()]
        ok = same and not diff and not extra and not sdiff
        print(json.dumps({'check': 'PASS' if ok else 'FAIL', 'data_same': same, 'files': len(D['files']), 'diff': diff, 'extra': extra, 'source_diff': sdiff}, ensure_ascii=False))
        sys.exit(0 if ok else 1)
    D = build(os.path.join(ROOT, SRC_REL), os.path.join(ROOT, PUB_REL), os.path.join(ROOT, DATA_REL))
    print(json.dumps({'checks': {c['id']: c['checks'] for c in D['covers']},
                      'pdf': {k: {kk: v[kk] for kk in ('pages', 'media_mm', 'trim_mm', 'cover_fonts', 'cover_vs_preview_mean_abs_diff', 'bytes')} for k, v in D['pdf'].items()}},
                     ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
