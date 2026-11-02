"""TASK-CAL-001 M-5 R31：非人物封面 4 張候選（橫式、直式各 A／B）——原創向量、漸層、光影與字體排版；不生成、不付費、不買素材。

- A｜四季光影：一道連續的光帶橫越畫面，沿途色溫與質地漸變（春柔光→夏水紋→秋暖光斑→冬霧光），「2027」與畫面共同構圖。
- B｜極簡典藏：深墨底、暖白字；以 Bodoni 字形、比例、細線與留白構成，低對比光影增加層次；不用金色、不仿燙金。
- 橫式、直式各自構圖（不是把橫稿裁直）。畫布含 2 mm 出血；文字只放在文字安全區內、避開上緣 12 mm 線圈假設區
  （與 R26 排版預覽同一套幾何）。文字位置用字型實際字寬與字形外框計算並自動檢查。
- 可編輯來源：docs/calendar/cover_r31/{H-A,H-B,V-A,V-B}.svg（文字保留為可編輯文字、字型以相對路徑載入）＋fonts/（OFL 授權字型與授權書）。
- 預覽：Chromium 把 SVG 轉成 300 dpi 圖，輸出顯示版與完整版 JPEG（docs/calendar/decision_site/public/cover31/）。
- 預覽 PDF：每款一份＝第 1 頁封面 A、第 2 頁封面 B（候選，二選一）、其後是 R26 已接受內頁（直接沿用 R26 PDF 的頁面，不改照片、日期或排版）。
  封面頁以 reportlab 產生：畫面為 300 dpi JPEG，文字與細線為向量、字型以子集嵌入；產生後用 pdffonts 確認嵌入、pdftoppm 讀回與預覽圖比對。
  R26 正式預覽 PDF 不覆蓋。
用法：python3 docs/calendar/tools/build_cal_m5_cover_r31.py [--prepare-fonts 下載資料夾] [--check]
"""
import argparse
import hashlib
import io
import json
import math
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
ROUND = 'M-5 R31'
SRC_REL = 'docs/calendar/cover_r31'
FONT_REL = SRC_REL + '/fonts'
PUB_REL = 'docs/calendar/decision_site/public/cover31'
DATA_REL = 'docs/calendar/data/cal_m5_cover_r31.json'
LAYOUT_DATA = 'docs/calendar/data/cal_m5_layout_r26.json'
LAYOUT_PDF = {'H': 'docs/calendar/decision_site/public/layout/cal2027_H_layout_preview_R26.pdf',
              'V': 'docs/calendar/decision_site/public/layout/cal2027_V_layout_preview_R26.pdf'}
RENDER = 'docs/calendar/tools/render_cal_svg.cjs'
DPI, VIEW_DPI = 300, 150
PT = 72 / 25.4
COVERS = ('H-A', 'H-B', 'V-A', 'V-B')
DIR_ZH = {'A': '四季光影', 'B': '極簡典藏'}
# 畫布（含 2 mm 出血，mm，左上為原點）；文字安全區與線圈假設區沿用 R26（cal_m5_layout_r26.json）
FMT = {'H': {'zh': '橫式', 'W': 204, 'H': 155, 'trim': 2, 'coil': 12, 'safe': (4, 12, 200, 151), 'px': (2410, 1831), 'vpx': (1205, 916)},
       'V': {'zh': '直式', 'W': 144, 'H': 204, 'trim': 2, 'coil': 12, 'safe': (5, 12, 139, 199), 'px': (1701, 2410), 'vpx': (850, 1205)}}
TEXT_MARGIN = 3.0   # 文字字形外框離文字安全區邊界至少 mm（另加的保險距離）

# ---------- 字型（SIL OFL 1.1；從 Google Fonts 開源庫取得的可變字型做出固定字重，並只保留拉丁字元） ----------
FONTS = {
    'cormorant': {'file': 'CormorantGaramond-Light-LF.ttf', 'family': 'Cormorant Garamond Light', 'license': 'OFL-CormorantGaramond.txt',
                  'upstream': 'https://raw.githubusercontent.com/google/fonts/main/ofl/cormorantgaramond/CormorantGaramond%5Bwght%5D.ttf',
                  'src': 'cormorantgaramond_CormorantGaramond[wght].ttf', 'src_license': 'cormorantgaramond_OFL.txt',
                  'loc': {'wght': 300}, 'digits': '.lf', 'use': 'A 的「2027」',
                  'mod': '可變字型固定為 wght 300；數字預設改為齊線數字（.lf），不必靠 OpenType 功能；只保留拉丁字元'},
    'bodoni': {'file': 'BodoniModa-96-Regular.ttf', 'family': 'Bodoni Moda 96pt', 'license': 'OFL-BodoniModa.txt',
               'upstream': 'https://raw.githubusercontent.com/google/fonts/main/ofl/bodonimoda/BodoniModa%5Bopsz,wght%5D.ttf',
               'src': 'bodonimoda_BodoniModa[opsz,wght].ttf', 'src_license': 'bodonimoda_OFL.txt',
               'loc': {'opsz': 96, 'wght': 400}, 'digits': None, 'use': 'B 的「2027」',
               'mod': '可變字型固定為 opsz 96（展示用光學尺寸）、wght 400；只保留拉丁字元'},
    'inter': {'file': 'Inter-Medium.ttf', 'family': 'Inter Medium', 'license': 'OFL-Inter.txt',
              'upstream': 'https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf',
              'src': 'inter_Inter[opsz,wght].ttf', 'src_license': 'inter_OFL.txt',
              'loc': {'opsz': 14, 'wght': 500}, 'digits': None, 'use': '小字「DESK CALENDAR」',
              'mod': '可變字型固定為 opsz 14、wght 500；只保留拉丁字元'},
}
KEEP_UNI = list(range(0x20, 0x7F)) + list(range(0xA0, 0x100)) + [0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2026]


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def prepare_fonts(dl):
    """從下載的上游可變字型做出本案用的固定字重字型（只需做一次；之後建置只讀 repo 裡的字型）。"""
    from fontTools import subset
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
    out = os.path.join(ROOT, FONT_REL)
    os.makedirs(out, exist_ok=True)
    rec = {}
    for k, F in FONTS.items():
        src = os.path.join(dl, F['src'])
        up = sha256(open(src, 'rb').read())
        f = instancer.instantiateVariableFont(TTFont(src), F['loc'], updateFontNames=True)
        if F['digits']:   # 齊線數字設成預設字形
            cm = f['cmap']
            for t in cm.tables:
                if t.isUnicode():
                    for c in '0123456789':
                        g = t.cmap.get(ord(c))
                        if g and g + F['digits'] in f.getGlyphOrder():
                            t.cmap[ord(c)] = g + F['digits']
        opt = subset.Options()
        opt.layout_features = ['*']
        opt.name_IDs = ['*']
        opt.name_languages = ['*']
        opt.notdef_outline = True
        opt.glyph_names = True
        sub = subset.Subsetter(opt)
        sub.populate(unicodes=KEEP_UNI)
        sub.subset(f)
        p = os.path.join(out, F['file'])
        f.save(p)
        shutil.copyfile(os.path.join(dl, F['src_license']), os.path.join(out, F['license']))
        rec[k] = {'upstream_sha256': up, 'file_sha256': sha256(open(p, 'rb').read())}
    return rec


# ---------- 字寬與字形外框（SVG 與 PDF 共用同一套座標） ----------
_TT = {}


def tt(k):
    if k not in _TT:
        from fontTools.pens.boundsPen import BoundsPen
        from fontTools.ttLib import TTFont
        f = TTFont(os.path.join(ROOT, FONT_REL, FONTS[k]['file']))
        gs = f.getGlyphSet()
        cmap = f.getBestCmap()
        bounds = {}
        for c in set('2027DESK CALENDAR'):
            g = cmap[ord(c)]
            bp = BoundsPen(gs)
            gs[g].draw(bp)
            bounds[c] = bp.bounds
        _TT[k] = {'upm': f['head'].unitsPerEm, 'adv': {c: f['hmtx'][cmap[ord(c)]][0] for c in bounds}, 'bounds': bounds}
    return _TT[k]


def layout_text(k, s, size, ls, x, y, anchor='start'):
    """回傳起點 x、字串寬度與字形外框（mm）。字距＝每個字元後面加 ls（與 Chromium 的 letter-spacing、PDF 的 Tc 相同）；不套用字距調整。"""
    T = tt(k)
    sc = size / T['upm']
    adv = [T['adv'][c] * sc for c in s]
    width = sum(adv) + ls * (len(s) - 1)
    x0 = x - width if anchor == 'end' else x
    xmin = ymin = 1e9
    xmax = ymax = -1e9
    cx = x0
    for c, a in zip(s, adv):
        b = T['bounds'][c]
        if b:
            xmin, xmax = min(xmin, cx + b[0] * sc), max(xmax, cx + b[2] * sc)
            ymin, ymax = min(ymin, y - b[3] * sc), max(ymax, y - b[1] * sc)
        cx += a + ls
    return {'x': round(x0, 3), 'y': y, 'width': round(width, 3), 'ink': [round(v, 2) for v in (xmin, ymin, xmax, ymax)]}


def f2(v):
    return f'{v:.3f}'.rstrip('0').rstrip('.')


def font_css(keys):
    return '<style>' + ''.join(f"@font-face{{font-family:'{FONTS[k]['family']}';src:url('fonts/{FONTS[k]['file']}')}}" for k in keys) + \
        ".txt text{font-kerning:none;font-feature-settings:'kern' 0,'liga' 0}</style>"


# ---------- A｜四季光影 ----------
SEASON = [(0, '#F6E0DA'), (0.2, '#F7EBE2'), (0.36, '#DDEEEC'), (0.5, '#D2E8E7'), (0.64, '#F4E0C8'), (0.76, '#EED6BA'), (0.88, '#E4E9EE'), (1, '#F0F2F5')]
INK_A = [(0, '#78605A'), (0.35, '#4A6667'), (0.68, '#83604A'), (1, '#58636D')]
A_SPEC = {
    'H': dict(axis='x', base=[(0, '#E3D8CE'), (0.3, '#DDDCD4'), (0.55, '#DED4C8'), (0.8, '#D8D9DB'), (1, '#E1E3E6')], base_dir=(0, 0, 1, 1), vig=(0.4, 0.35),
              glows=[(30, 30, 40, 30, '#F3E4DC', .6), (95, 70, 40, 34, '#D4E6E4', .45), (150, 60, 36, 30, '#EBD4B8', .45), (190, 40, 30, 40, '#E6E9EC', .6)],
              ribbons=[(-10, 214, 66, 14, 230, 0.9, 64, 44, 9, 1.3), (-10, 214, 64, 13, 230, 1.0, 30, 20, 6, 2.1), (-10, 214, 63, 12, 230, 1.1, 10, 6, 3, 0.4)],
              slope=-0.16, mid=102,
              seg=dict(spring=[(0, 1), (0.22, 0.8), (0.36, 0)], summer=[(0.2, 0), (0.42, 1), (0.56, 0.6), (0.66, 0)],
                       autumn=[(0.5, 0), (0.66, 1), (0.8, 0.8), (0.9, 0)], winter=[(0.74, 0), (0.92, 1), (1, 1)]),
              caus_f='0.045 0.15', mist_f='0.014 0.026', dap_f='0.1 0.13', bloom=[(18, 50, 16, .6), (40, 70, 12, .5)],
              year=dict(x=189, y=140, size=48, ls=0.8, anchor='end'), sub=dict(x=188.5, y=103, size=2.5, ls=0.95, anchor='end')),
    'V': dict(axis='y', base=[(0, '#E3D8CE'), (0.3, '#DDDCD4'), (0.55, '#DED4C8'), (0.8, '#D8D9DB'), (1, '#E1E3E6')], base_dir=(0, 0, 0.4, 1), vig=(0.45, 0.4),
              glows=[(90, 34, 34, 26, '#F3E4DC', .6), (50, 82, 34, 30, '#D4E6E4', .45), (96, 124, 32, 26, '#EBD4B8', .45), (70, 175, 50, 30, '#E6E9EC', .6)],
              ribbons=[(4, 214, 74, 26, 230, 2.2, 62, 46, 8, 1.3), (4, 214, 73, 25, 230, 2.3, 30, 20, 5, 2.1), (4, 214, 72, 24, 230, 2.4, 10, 6, 3, 0.4)],
              slope=-0.05, mid=110,
              seg=dict(spring=[(0, 1), (0.22, 0.8), (0.34, 0)], summer=[(0.2, 0), (0.37, 1), (0.48, 0.6), (0.56, 0)],
                       autumn=[(0.44, 0), (0.56, 1), (0.64, 0.8), (0.72, 0)], winter=[(0.62, 0), (0.78, 1), (1, 1)]),
              caus_f='0.05 0.15', mist_f='0.026 0.014', dap_f='0.13 0.1', bloom=[(96, 30, 14, .6), (76, 44, 10, .5)],
              year=dict(x=13.5, y=181, size=46, ls=0.7, anchor='start'), sub=dict(x=15, y=191.5, size=2.4, ls=0.9, anchor='start')),
}
A_COMMON = dict(blur=(1.2, 3.2, 9), rib_op=(0.55, 0.85, 0.55, 0.45), caus_op=0.9, aut_op=0.3, aut_col='#D3AE8C', grain=0.06)


def ribbon(x0, x1, yc, amp, lam, ph, t0, t1, tamp, tph, axis, slope, mid, n=120):
    """沿主軸的波浪光帶外形（path d）：中心線 yc＋slope·(s−mid)＋amp·sin，厚度 t0→t1 加 tamp·sin。"""
    top, bot = [], []
    for i in range(n + 1):
        u = i / n
        s = x0 + (x1 - x0) * u
        c = yc + slope * (s - mid) + amp * math.sin(2 * math.pi * s / lam + ph)
        t = t0 + (t1 - t0) * u + tamp * math.sin(2 * math.pi * s / (lam * 0.7) + tph)
        a, b = (s, c - t / 2), (s, c + t / 2)
        if axis == 'y':
            a, b = (a[1], a[0]), (b[1], b[0])
        top.append(a)
        bot.append(b)
    return 'M' + ' L'.join(f'{f2(x)} {f2(y)}' for x, y in top + bot[::-1]) + ' Z'


def text_items(cid):
    k, d = cid.split('-')
    if d == 'A':
        S = A_SPEC[k]
        return [dict(role='year', font='cormorant', s='2027', fill='grad', **S['year']),
                dict(role='sub', font='inter', s='DESK CALENDAR', fill='#5E5650', op=1, **S['sub'])]
    S = B_SPEC[k]
    items = [dict(role='year', font='bodoni', s=s, fill='grad', **v) for s, v in S['years']]
    items.append(dict(role='sub', font='inter', s='DESK CALENDAR', fill='#EDE5D7', op=0.78, **S['sub']))
    return items


def placed(cid):
    out = []
    for it in text_items(cid):
        L = layout_text(it['font'], it['s'], it['size'], it['ls'], it['x'], it['y'], it.get('anchor', 'start'))
        out.append({**it, **L})
    return out


def svg_a(cid):
    k = cid[0]
    S, C, F = A_SPEC[k], A_COMMON, FMT[k]
    W, H, ax = F['W'], F['H'], S['axis']
    full = f'x1="0" y1="0" x2="{W}" y2="0"' if ax == 'x' else f'x1="0" y1="0" x2="0" y2="{H}"'
    o = [f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">',
         f'<title>2027 桌曆封面候選 {cid}｜A 四季光影（{F["zh"]}，含 2 mm 出血）</title>', font_css(('cormorant', 'inter')), '<defs>']
    bx1, by1, bx2, by2 = S['base_dir']
    o.append(f'<linearGradient id="base" x1="{bx1}" y1="{by1}" x2="{bx2}" y2="{by2}">' + ''.join(f'<stop offset="{a}" stop-color="{b}"/>' for a, b in S['base']) + '</linearGradient>')
    o.append(f'<linearGradient id="season" gradientUnits="userSpaceOnUse" {full}>' + ''.join(f'<stop offset="{a}" stop-color="{b}"/>' for a, b in SEASON) + '</linearGradient>')
    for name, pts in S['seg'].items():
        o.append(f'<linearGradient id="g_{name}" gradientUnits="userSpaceOnUse" {full}>' + ''.join(f'<stop offset="{a}" stop-color="#fff" stop-opacity="{b}"/>' for a, b in pts) + '</linearGradient>')
        o.append(f'<mask id="m_{name}"><rect width="{W}" height="{H}" fill="url(#g_{name})"/></mask>')
    b1, b2, b3 = C['blur']
    o.append(f'''<radialGradient id="vig" cx="{S['vig'][0]}" cy="{S['vig'][1]}" r="0.9"><stop offset="0.5" stop-color="#4d4036" stop-opacity="0"/><stop offset="1" stop-color="#4d4036" stop-opacity="0.2"/></radialGradient>
<filter id="b1" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="{b1}"/></filter>
<filter id="b2" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="{b2}"/></filter>
<filter id="b3" x="-30%" y="-80%" width="160%" height="260%"><feGaussianBlur stdDeviation="{b3}"/></filter>
<filter id="caustic" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="{S['caus_f']}" numOctaves="2" seed="11" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0 0 0 0 0.1 0.9 0.1 0 0 0 0 0"/></feComponentTransfer>
 <feGaussianBlur stdDeviation="0.1"/></filter>
<filter id="dapple" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="{S['dap_f']}" numOctaves="3" seed="23" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 1 0 0 0 0 0.93 0 0 0 0 0.80 1 0 0 0 0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0 0 0 0 0 0.05 0.35 0.8 0.95 1"/></feComponentTransfer>
 <feGaussianBlur stdDeviation="0.7"/></filter>
<filter id="mist" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="{S['mist_f']}" numOctaves="3" seed="5" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 1.6 0 -0.55"/>
 <feGaussianBlur stdDeviation="1.0"/></filter>
<filter id="mist2" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="0.05 0.012" numOctaves="2" seed="9" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.97 0 0 0 0 0.98 0 0 0 0 1 0 0 1.8 0 -0.75"/>
 <feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="grain" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="3.4" numOctaves="1" seed="3"/><feColorMatrix type="saturate" values="0"/></filter>''')
    rib = [ribbon(*r, axis=ax, slope=S['slope'], mid=S['mid']) for r in S['ribbons']]
    o.append(f'<mask id="ribMask"><path d="{rib[0]}" fill="#fff" filter="url(#b2)"/></mask>')
    o.append('</defs>')
    o.append('<g id="art">')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#base)"/>')
    o.append('<g filter="url(#b3)">' + ''.join(f'<ellipse cx="{a}" cy="{b}" rx="{c}" ry="{d}" fill="{e}" opacity="{g}"/>' for a, b, c, d, e, g in S['glows']) + '</g>')
    r0, r1, r2, r3 = C['rib_op']
    o.append(f'<path d="{rib[0]}" fill="url(#season)" opacity="{r0}" filter="url(#b3)"/>')
    o.append(f'<path d="{rib[0]}" fill="url(#season)" opacity="{r1}" filter="url(#b2)"/>')
    o.append(f'<path d="{rib[1]}" fill="#FFFCF6" opacity="{r2}" filter="url(#b2)"/>')
    o.append(f'<path d="{rib[2]}" fill="#FFFFFF" opacity="{r3}" filter="url(#b1)"/>')
    o.append(f'<g mask="url(#m_summer)"><g mask="url(#ribMask)"><rect width="{W}" height="{H}" fill="#CFE8E7" opacity="0.45"/>'
             f'<rect width="{W}" height="{H}" filter="url(#caustic)" opacity="{C["caus_op"]}"/></g></g>')
    o.append(f'<g mask="url(#m_autumn)"><g mask="url(#ribMask)"><rect width="{W}" height="{H}" fill="{C["aut_col"]}" opacity="{C["aut_op"]}"/>'
             f'<rect width="{W}" height="{H}" filter="url(#dapple)"/></g></g>')
    o.append(f'<g mask="url(#m_winter)"><rect width="{W}" height="{H}" fill="#E9EEF3" opacity="0.6"/><rect width="{W}" height="{H}" filter="url(#mist)"/>'
             f'<rect width="{W}" height="{H}" filter="url(#mist2)" opacity="0.7"/></g>')
    o.append('<g mask="url(#m_spring)"><g filter="url(#b3)">' + ''.join(f'<circle cx="{a}" cy="{b}" r="{c}" fill="#FFF3EC" opacity="{d}"/>' for a, b, c, d in S['bloom']) + '</g></g>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')
    o.append(f'<rect width="{W}" height="{H}" filter="url(#grain)" opacity="{C["grain"]}" style="mix-blend-mode:multiply"/>')
    o.append('</g>')
    o.extend(svg_text(cid))
    o.append('</svg>')
    return '\n'.join(o) + '\n'


# ---------- B｜極簡典藏 ----------
B_INK = {'ground': ('#2B2F37', '#22252C', '#16181D'), 'type': ('#F4EEE3', '#E4DACA'), 'line': '#EDE5D7'}
B_SPEC = {
    'H': dict(light=(0.3, 0.3, 0.75), type_grad=(55, 100), rules=[(16, 106, 188, 106, 0.18, 0.6)],
              years=[('2027', dict(x=14.5, y=101, size=58, ls=-0.6, anchor='start'))],
              sub=dict(x=188, y=113.5, size=2.4, ls=1.15, anchor='end')),
    'V': dict(light=(0.3, 0.25, 0.8), type_grad=(60, 175), rules=[(14, 182, 130, 182, 0.18, 0.6)],
              years=[('20', dict(x=12.5, y=113, size=74, ls=-0.8, anchor='start')), ('27', dict(x=12.5, y=174, size=74, ls=-0.8, anchor='start'))],
              sub=dict(x=130, y=189.5, size=2.3, ls=1.1, anchor='end')),
}


def svg_b(cid):
    k = cid[0]
    S, F = B_SPEC[k], FMT[k]
    W, H = F['W'], F['H']
    lx, ly, lr = S['light']
    g0, g1, g2 = B_INK['ground']
    o = [f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">',
         f'<title>2027 桌曆封面候選 {cid}｜B 極簡典藏（{F["zh"]}，含 2 mm 出血）</title>', font_css(('bodoni', 'inter')), '<defs>']
    sy = W / H if W > H else 1
    o.append(f'''<radialGradient id="ground" cx="{lx}" cy="{ly}" r="{lr}" gradientTransform="translate({lx} {ly}) scale(1 {f2(sy)}) translate({-lx} {-ly})">
<stop offset="0" stop-color="{g0}"/><stop offset="0.45" stop-color="{g1}"/><stop offset="1" stop-color="{g2}"/></radialGradient>
<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="1"><stop offset="0.25" stop-color="#F3EBDD" stop-opacity="0"/><stop offset="0.42" stop-color="#F3EBDD" stop-opacity="0.045"/><stop offset="0.55" stop-color="#F3EBDD" stop-opacity="0"/></linearGradient>
<filter id="grain" x="0" y="0" width="{W}" height="{H}" filterUnits="userSpaceOnUse">
 <feTurbulence type="fractalNoise" baseFrequency="3.0" numOctaves="1" seed="7"/><feColorMatrix type="saturate" values="0"/></filter>
</defs>''')
    o.append('<g id="art">')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#ground)"/>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#sheen)"/>')
    o.append(f'<rect width="{W}" height="{H}" filter="url(#grain)" opacity="0.05" style="mix-blend-mode:screen"/>')
    o.append('</g>')
    o.append('<g class="vec">' + ''.join(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{B_INK["line"]}" stroke-width="{w}" stroke-opacity="{op}"/>' for x1, y1, x2, y2, w, op in S['rules']) + '</g>')
    o.extend(svg_text(cid))
    o.append('</svg>')
    return '\n'.join(o) + '\n'


def grad_stops(cid):
    if cid[2] == 'A':
        return INK_A
    t0, t1 = B_INK['type']
    return [(0, t0), (1, t1)]


def grad_line(cid, items):
    """「2027」的漸層方向：A 沿字串橫向（四個數字對應四季的深色），B 由上到下（暖白微漸層）。"""
    ys = [i for i in items if i['role'] == 'year']
    if cid[2] == 'A':
        return (ys[0]['ink'][0], 0, ys[0]['ink'][2], 0)
    S = B_SPEC[cid[0]]
    return (0, S['type_grad'][0], 0, S['type_grad'][1])


def svg_text(cid):
    items = placed(cid)
    x1, y1, x2, y2 = grad_line(cid, items)
    o = [f'<defs><linearGradient id="ink" gradientUnits="userSpaceOnUse" x1="{f2(x1)}" y1="{f2(y1)}" x2="{f2(x2)}" y2="{f2(y2)}">' +
         ''.join(f'<stop offset="{a}" stop-color="{b}"/>' for a, b in grad_stops(cid)) + '</linearGradient></defs>', '<g class="txt">']
    for it in items:
        fill = 'url(#ink)' if it['fill'] == 'grad' else it['fill']
        op = f' fill-opacity="{it["op"]}"' if it.get('op', 1) != 1 else ''
        o.append(f'<text x="{f2(it["x"])}" y="{f2(it["y"])}" font-family="&apos;{FONTS[it["font"]]["family"]}&apos;" font-size="{it["size"]}" '
                 f'letter-spacing="{it["ls"]}" fill="{fill}"{op}>{it["s"]}</text>')
    o.append('</g>')
    return o


def text_check(cid):
    """字形外框（不是行框）必須在文字安全區內再縮 TEXT_MARGIN、且在線圈假設區以下。"""
    F = FMT[cid[0]]
    sx0, sy0, sx1, sy1 = F['safe']
    out = []
    for it in placed(cid):
        x0, y0, x1, y1 = it['ink']
        ok = x0 >= sx0 + TEXT_MARGIN and x1 <= sx1 - TEXT_MARGIN and y0 >= max(sy0, F['coil']) + TEXT_MARGIN and y1 <= sy1 - TEXT_MARGIN
        out.append({'text': it['s'], 'ink_mm': it['ink'], 'size_mm': it['size'], 'ok': ok})
    return out


def jpeg(im, q, sub=2):
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=q, subsampling=sub, optimize=False)
    return b.getvalue()


def render(svg_path, png_path, px, hide=''):
    subprocess.run(['node', os.path.join(ROOT, RENDER), svg_path, png_path, str(px[0]), str(px[1]), hide], check=True, cwd=ROOT)
    return Image.open(png_path).convert('RGB')


def cover_pdf(cid, art_jpg, path):
    """封面一頁：畫面＝300 dpi JPEG（直接放進 PDF），文字與細線為向量；字型以 TrueType 子集嵌入。"""
    from reportlab import rl_config
    from reportlab.lib.colors import Color, HexColor
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas as rl_canvas
    rl_config.useA85 = 0   # JPEG 不再包一層 ASCII85（與 R26 相同）
    F = FMT[cid[0]]
    W, H = F['W'], F['H']
    for k, Fo in FONTS.items():
        name = 'R31-' + k
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, os.path.join(ROOT, FONT_REL, Fo['file'])))
    c = rl_canvas.Canvas(path, pagesize=(W * PT, H * PT), invariant=1, pageCompression=1, initialFontName='R31-inter', initialFontSize=8)   # 不留未嵌入的預設字型
    t = F['trim']
    c.setTrimBox((t * PT, t * PT, (W - t) * PT, (H - t) * PT))
    c.setBleedBox((0, 0, W * PT, H * PT))
    from reportlab.lib.utils import ImageReader
    c.drawImage(ImageReader(io.BytesIO(open(art_jpg, 'rb').read())), 0, 0, W * PT, H * PT)   # 以內容命名圖片物件（不受暫存路徑影響），JPEG 原樣放入
    if cid[2] == 'B':
        for x1, y1, x2, y2, w, op in B_SPEC[cid[0]]['rules']:
            c.saveState()
            c.setStrokeColor(HexColor(B_INK['line']))
            c.setStrokeAlpha(op)
            c.setLineWidth(w * PT)
            c.line(x1 * PT, (H - y1) * PT, x2 * PT, (H - y2) * PT)
            c.restoreState()
    items = placed(cid)
    gx1, gy1, gx2, gy2 = grad_line(cid, items)
    stops = grad_stops(cid)
    for it in items:
        c.saveState()
        to = c.beginText(it['x'] * PT, (H - it['y']) * PT)
        to.setFont('R31-' + it['font'], it['size'] * PT)
        to.setCharSpace(it['ls'] * PT)
        if it['fill'] == 'grad':
            to.setTextRenderMode(7)   # 只當裁切路徑，再填漸層
            to.textOut(it['s'])
            c.drawText(to)
            c.linearGradient(gx1 * PT, (H - gy1) * PT, gx2 * PT, (H - gy2) * PT, [HexColor(s) for _, s in stops], [p for p, _ in stops], extend=True)
        else:
            col = HexColor(it['fill'])
            c.setFillColor(Color(col.red, col.green, col.blue, alpha=it.get('op', 1)))
            to.textOut(it['s'])
            c.drawText(to)
        c.restoreState()
    c.showPage()
    c.save()


def pdf_fonts(path, pages):
    r = subprocess.run(['pdffonts', '-f', str(pages[0]), '-l', str(pages[1]), path], capture_output=True, text=True, check=True).stdout.splitlines()[2:]
    return [{'name': ln.split()[0].split('+')[-1], 'subset_tag': '+' in ln.split()[0], 'emb': ln.split()[-5], 'sub': ln.split()[-4]} for ln in r if ln.strip()]


def pdf_page_png(path, page, size, tmp):
    base = os.path.join(tmp, f'pp_{page}')
    subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-scale-to-x', str(size[0]), '-scale-to-y', str(size[1]), '-png', path, base], check=True)
    fn = [x for x in os.listdir(tmp) if x.startswith(f'pp_{page}') and x.endswith('.png')][0]
    im = Image.open(os.path.join(tmp, fn)).convert('RGB')
    os.unlink(os.path.join(tmp, fn))
    return im


def build(src_dir, pub, data_path):
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import ArrayObject, ByteStringObject
    for d in (src_dir, pub):
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith(('.svg', '.jpg', '.pdf')):
                    os.unlink(os.path.join(d, fn))
        os.makedirs(d, exist_ok=True)
    fsrc = os.path.join(src_dir, 'fonts')
    if os.path.realpath(fsrc) != os.path.realpath(os.path.join(ROOT, FONT_REL)):
        shutil.copytree(os.path.join(ROOT, FONT_REL), fsrc, dirs_exist_ok=True)
    LD = json.load(open(os.path.join(ROOT, LAYOUT_DATA), encoding='utf-8'))
    lay_sha = {x['path']: x['sha256'] for x in LD['files']}
    files, covers = {}, []

    def save(name, data):
        open(os.path.join(pub, name), 'wb').write(data)
        files[name] = sha256(data)
    with tempfile.TemporaryDirectory() as tmp:
        cover_pdfs = {}
        for cid in COVERS:
            k = cid[0]
            F = FMT[k]
            svg = svg_a(cid) if cid[2] == 'A' else svg_b(cid)
            sp = os.path.join(src_dir, f'{cid}.svg')
            open(sp, 'w', encoding='utf-8').write(svg)
            full = render(sp, os.path.join(tmp, f'{cid}_full.png'), F['px'])
            art = render(sp, os.path.join(tmp, f'{cid}_art.png'), F['px'], 'txt,vec')
            save(f'cover_{cid}_f.jpg', jpeg(full, 90))
            view = full.resize(F['vpx'], Image.LANCZOS)
            save(f'cover_{cid}_v.jpg', jpeg(view, 88))
            aj = os.path.join(tmp, f'{cid}_art.jpg')
            open(aj, 'wb').write(jpeg(art, 95, 0))
            cp = os.path.join(tmp, f'{cid}.pdf')
            cover_pdf(cid, aj, cp)
            cover_pdfs[cid] = cp
            covers.append({'id': cid, 'kind': k, 'dir': cid[2], 'dir_zh': DIR_ZH[cid[2]], 'source': f'{cid}.svg',
                           'source_sha256': sha256(svg.encode('utf-8')), 'px': list(F['px']), 'view_px': list(F['vpx']),
                           'text': text_check(cid), '_view': view})
        pdfs = {}
        for k in 'HV':
            src = os.path.join(ROOT, LAYOUT_PDF[k])
            rel = os.path.relpath(src, os.path.join(ROOT, 'docs/calendar/decision_site/public/layout'))
            assert sha256(open(src, 'rb').read()) == lay_sha[rel], f'R26 {k} PDF 與紀錄不同'
            w = PdfWriter()
            for d in 'AB':
                w.add_page(PdfReader(cover_pdfs[f'{k}-{d}']).pages[0])
            base = PdfReader(src)
            for p in base.pages[1:]:
                w.add_page(p)
            w.add_metadata({'/Title': f'2027 桌曆 {FMT[k]["zh"]} 封面候選預覽 R31（第 1 頁 A、第 2 頁 B，其後為已接受內頁；未定案）', '/Producer': 'cal2027 R31'})
            w._ID = ArrayObject([ByteStringObject(hashlib.md5(f'cal2027-R31-{k}'.encode()).digest())] * 2)
            name = f'cal2027_{k}_cover_preview_R31.pdf'
            b = io.BytesIO()
            w.write(b)
            save(name, b.getvalue())
            pp = os.path.join(pub, name)
            R = PdfReader(pp)
            fonts = pdf_fonts(pp, (1, 2))
            match = {}
            for i, d in enumerate('AB', 1):
                cv = next(c for c in covers if c['id'] == f'{k}-{d}')
                pim = np.asarray(pdf_page_png(pp, i, FMT[k]['vpx'], tmp)).astype(int)
                vim = np.asarray(cv['_view']).astype(int)
                match[d] = round(float(np.abs(pim - vim).mean()), 2)
            pg = R.pages[0]
            pdfs[k] = {'path': name, 'pages': len(R.pages), 'order': ['封面 A（候選）', '封面 B（候選）'] + [f'R26 面 {i}' for i in range(2, len(base.pages) + 1)],
                       'media_mm': [round(float(v) / PT, 2) for v in pg.mediabox[2:]], 'trim_mm': [round(float(v) / PT, 2) for v in pg.trimbox],
                       'cover_fonts': fonts, 'cover_vs_preview_mean_abs_diff': match,
                       'interior_from': os.path.basename(src), 'interior_pages': len(base.pages) - 1, 'bytes': os.path.getsize(pp)}
    for c in covers:
        c.pop('_view')
    out = []
    for name, h in sorted(files.items()):
        e = {'path': name, 'sha256': h, 'bytes': os.path.getsize(os.path.join(pub, name))}
        if name.endswith('.jpg'):
            im = Image.open(os.path.join(pub, name))
            e['px'] = [im.width, im.height]
        out.append(e)
    fr = json.load(open(os.path.join(ROOT, FONT_REL, 'fonts.json'), encoding='utf-8'))
    D = {'round': ROUND,
         'note': '非人物封面 4 張候選（橫式、直式各 A／B），原創向量、漸層、光影與字體排版；生成 0、付費 0、未購買素材；候選未接受，R26 正式預覽 PDF 不覆蓋。',
         'directions': {'A': 'A｜四季光影：一道連續的光帶橫越畫面，春柔光→夏水紋→秋暖光斑→冬霧光，「2027」與畫面共同構圖（數字填色對應四季的深色）',
                        'B': 'B｜極簡典藏：深墨底、暖白字，Bodoni 字形、比例、細線與留白，低對比光影；不用金色、不仿燙金'},
         'formats': {k: {kk: v for kk, v in F.items() if kk not in ('px', 'vpx')} | {'text_margin_mm': TEXT_MARGIN} for k, F in FMT.items()},
         'fonts': [{'key': k, 'family': Fo['family'], 'file': Fo['file'], 'license': 'SIL Open Font License 1.1', 'license_file': Fo['license'],
                    'upstream': Fo['upstream'], 'modification': Fo['mod'], 'use': Fo['use'], **fr[k]} for k, Fo in FONTS.items()],
         'covers': covers, 'pdf': pdfs, 'files': out}
    with open(data_path, 'w', encoding='utf-8') as fh:
        json.dump(D, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    return D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prepare-fonts', metavar='DIR')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.prepare_fonts:
        rec = prepare_fonts(a.prepare_fonts)
        with open(os.path.join(ROOT, FONT_REL, 'fonts.json'), 'w', encoding='utf-8') as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print(json.dumps(rec, ensure_ascii=False))
        return
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
    print(json.dumps({'text': {c['id']: [(t['text'], t['ok'], t['ink_mm']) for t in c['text']] for c in D['covers']},
                      'pdf': {k: {kk: v[kk] for kk in ('pages', 'media_mm', 'trim_mm', 'cover_fonts', 'cover_vs_preview_mean_abs_diff', 'bytes')} for k, v in D['pdf'].items()}},
                     ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
