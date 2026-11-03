"""TASK-CAL-001 M-5 R33：橫式 H-L1 定案；直式 V-D2 修正版（只把「2027」改成金色＋收斂光暈）。不生成、不付費、不買素材。

- 橫式：沿用 Owner 已接受的 R32 H-L1（封面頁直接取自 R32 H-L1 完整預覽 PDF 第 1 頁，不重畫、不改）。
- 直式：以 R32 V-D2 為基礎，背景（build_cal_m5_cover_r32.dark_art() 原樣）、置中編排、留白、年份位置與大小都不變。
  · 「2027」：同一字型（Cormorant Garamond Light）、同位置；柔和香檳金→暖金黃的上下漸層（受光感），字形本體清楚；
    背後一層輕微、收斂的同色光暈（只在畫面點陣裡，以「濾色」疊在背景光影上）。這是印刷圖稿裡的金色視覺效果，不是燙金或金墨。
  · 品牌區：依 Owner 本輪決定「乾脆就維持原本白色的logo字樣，2027的字體改變而已」，與 R32 V-D2 完全相同
    （官網 logo01.svg 向量改填白色的衍生版＋細線＋白色「兌心科技」，build_cal_m5_cover_r32 的同一組幾何與配色）。
  · Penny 本輪提供的藍色圓底 Logo（docs/calendar/cover_r33/brand/insight-software-logo-circle.png）試放後 Owner 判斷不協調，未採用，原檔保留作紀錄。
- 輸出：可編輯來源 docs/calendar/cover_r33/（SVG、fonts、brand）；預覽與兩份完整預覽 PDF 在 docs/calendar/decision_site/public/cover33/
  （橫式 28 面＝已接受 H-L1＋R26 內頁；直式 32 面＝本輪修正版＋R26 內頁）。R32 圖片、PDF 與歷史回饋不覆蓋。
用法：python3 docs/calendar/tools/build_cal_m5_cover_r33.py [--check] [--proto 目錄]
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_cal_m5_cover_r31 as R31  # noqa: E402
import build_cal_m5_cover_r32 as R32  # noqa: E402

ROUND = 'M-5 R33'
CID = 'V-D2-R33'
BASE = 'V-D2'              # R32 的直式版本 2：品牌區幾何與配色原樣沿用
SRC_REL = 'docs/calendar/cover_r33'
PUB_REL = 'docs/calendar/decision_site/public/cover33'
DATA_REL = 'docs/calendar/data/cal_m5_cover_r33.json'
R32_PUB = 'docs/calendar/decision_site/public/cover32'
R32_DATA = 'docs/calendar/data/cal_m5_cover_r32.json'
FMT, PT, TEXT_MARGIN, FONTS, fmt = R32.FMT, R32.PT, R32.TEXT_MARGIN, R32.FONTS, R32.fmt
F = FMT['V']
# ---------- 年份（只改這裡）：位置與大小同 R32 V-D2 ----------
YEAR = dict(R32.LAYOUT[BASE]['year'], ls=R32.YEAR_LS)
GOLD = [(0.0, '#F7EBCB'), (0.34, '#EDD49E'), (0.7, '#DFBB78'), (1.0, '#CDA764')]   # 柔和香檳金（上、受光）→ 暖金黃（下）；色相 38–45°，不偏橘
GLOW = '#E6C27F'          # 光暈同色系
GLOWS = [(2.0, 0.42), (0.6, 0.24)]   # （模糊半徑 mm, 不透明度）：一層柔光＋一層貼近字緣的微光；不模糊字本體
CIRCLE_REL = SRC_REL + '/brand/insight-software-logo-circle.png'
CIRCLE_SHA = '859e51e7ddf0e9a4c7cccc0a725d5e5ae9a134c15110b0fcdbdbdc8056665416'
LOGO_STATUS = {
    'used': 'R32 V-D2 的同一個白色 Logo：官網 logo01.svg 向量（等比、不重畫）改填白色的設計衍生版，非官方反白檔',
    'decision': 'Owner 本輪決定維持原本白色 Logo（2026-11-03 原話：「乾脆就維持原本白色的logo字樣，2027的字體改變而已」）',
    'official_source': R32.LOGO_URL,
    'official_sha256': R32.LOGO_SHA,
    'circle_logo': {'file': 'brand/insight-software-logo-circle.png', 'sha256': CIRCLE_SHA,
                    'source': 'Penny 在 R33 進行中提供（原話「這個logo也給你做參考」）；800×800 PNG、圓外透明、藍 #2B33F2',
                    'verified': '和官方 YouTube、Facebook 頭像同一排法，圖示與字樣重疊率約 98%',
                    'tried': '試放直徑 22 mm → 15 mm 後，Owner 認為藍底 Logo 在深藍畫面上不協調（「這個藍底的logo有點不搭」），未採用；原檔保留作紀錄',
                    'used': False},
}


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def year_geom():
    return R32.text_box('year', '2027', YEAR['size'], YEAR['ls'], YEAR['x'], YEAR['y'], YEAR['anchor'])


def svg_cover():
    W, H = F['W'], F['H']
    defs, art = R32.dark_art()   # 與 R32 V-D2 同一張背景
    yg = year_geom()
    y0, y1 = yg['ink'][1], yg['ink'][3]
    ytext = lambda attrs: (f'<text x="{fmt(yg["x"])}" y="{fmt(yg["y"])}" font-family="&apos;{FONTS["year"]["family"]}&apos;" font-size="{YEAR["size"]}" '  # noqa: E731
                           f'letter-spacing="{YEAR["ls"]}" {attrs}>2027</text>')
    gdefs = ['<defs>', f'<linearGradient id="ygold" gradientUnits="userSpaceOnUse" x1="0" y1="{fmt(y0)}" x2="0" y2="{fmt(y1)}">' +
             ''.join(f'<stop offset="{a}" stop-color="{c}"/>' for a, c in GOLD) + '</linearGradient>']
    for i, (sd, _) in enumerate(GLOWS):
        gdefs.append(f'<filter id="yglow{i}" x="-30" y="-30" width="{W + 60}" height="{H + 60}" filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="{sd}"/></filter>')
    gdefs.append('</defs>')
    # 品牌區與 R32 V-D2 相同：取 R32 的品牌輸出，只把白色年份換成金色年份
    brand = R32.svg_brand_text(BASE, True)
    assert brand[1].startswith('<text') and '>2027</text>' in brand[1]
    brand = [brand[0], ytext('fill="url(#ygold)"')] + brand[2:]
    o = [f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">',
         f'<title>2027 桌曆封面 直式 {CID}｜V-D2 修正版（金色年份；品牌區同 R32），含 2 mm 出血</title>',
         R32.font_css().replace('.txt text{', '.txt text,.glow text{'), defs, '\n'.join(gdefs), art,
         '<g class="glow" style="mix-blend-mode:screen"><desc>年份光暈（畫面點陣的一部分）</desc>'] + \
        [ytext(f'fill="{GLOW}" opacity="{op}" filter="url(#yglow{i})"') for i, (_, op) in enumerate(GLOWS)] + ['</g>'] + brand + ['</svg>']
    return '\n'.join(o) + '\n'


# ---------- PDF ----------
def _font(k):
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    if 'R33-' + k not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont('R33-' + k, os.path.join(ROOT, R32.FONT_REL, FONTS[k]['file'])))
    return 'R33-' + k


def cover_pdf(art_jpg, path, icon=None):
    """直式封面一頁：背景（含年份光暈）＝300 dpi JPEG；金色年份＝向量字形裁切＋線性漸層；中文、細線、白色 Logo 為向量（同 R32）；字型子集嵌入。"""
    from fontTools.svgLib.path import parse_path
    from reportlab import rl_config
    from reportlab.lib.colors import HexColor
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.pdfgen.canvas import FILL_EVEN_ODD, FILL_NON_ZERO
    rl_config.useA85 = 0
    W, H = F['W'], F['H']
    c = rl_canvas.Canvas(path, pagesize=(W * PT, H * PT), invariant=1, pageCompression=1, initialFontName=_font('cjk'), initialFontSize=8)
    t = F['trim']
    c.setTrimBox((t * PT, t * PT, (W - t) * PT, (H - t) * PT))
    c.setBleedBox((0, 0, W * PT, H * PT))
    c.drawImage(ImageReader(io.BytesIO(open(art_jpg, 'rb').read())), 0, 0, W * PT, H * PT)
    yg, bg = year_geom(), R32.brand_geom(BASE)
    # 金色年份：字形當裁切路徑，再畫上下漸層
    c.saveState()
    to = c.beginText(yg['x'] * PT, (H - yg['y']) * PT)
    to.setFont(_font('year'), YEAR['size'] * PT)
    to.setCharSpace(YEAR['ls'] * PT)
    to.setTextRenderMode(7)
    to.textOut('2027')
    c.drawText(to)
    y0, y1 = yg['ink'][1], yg['ink'][3]
    c.linearGradient(0, (H - y0) * PT, 0, (H - y1) * PT, [HexColor(col) for _, col in GOLD], [a for a, _ in GOLD], extend=True)
    c.restoreState()
    # 品牌區：與 R32 V-D2 相同（白色中文、細線、白色 Logo 衍生版）
    D = R32.DARK
    cj = bg['cjk']
    to = c.beginText(cj['x'] * PT, (H - cj['y']) * PT)
    to.setFont(_font('cjk'), bg['cjk_size'] * PT)
    to.setCharSpace(bg['cjk_ls'] * PT)
    to.setFillColor(HexColor(D['cjk']))
    to.textOut('兌心科技')
    c.drawText(to)
    rx1, ry1, rx2, ry2 = bg['rule']
    c.saveState()
    c.setStrokeColor(HexColor(D['rule']))
    c.setStrokeAlpha(0.55)
    c.setLineWidth(0.15 * PT)
    c.line(rx1 * PT, (H - ry1) * PT, rx2 * PT, (H - ry2) * PT)
    c.restoreState()
    x0, ly0, s = bg['logo']
    for cls, d in R32.logo_paths():
        p = c.beginPath()
        parse_path(d, R32._RLPen(p, x0, ly0, s, H))
        c.setFillColor(HexColor(icon if (icon and cls == 'st0') else D['logo']))   # icon：R34 比較版把圖示（st0）填回官方藍；預設全白＝R33
        c.drawPath(p, stroke=0, fill=1, fillMode=FILL_EVEN_ODD if cls == 'st0' else FILL_NON_ZERO)
    c.showPage()
    c.save()


def checks():
    """年份與品牌區的字形外框在文字安全區內再縮 TEXT_MARGIN、在線圈假設區以下；品牌區尺寸沿用 R32 V-D2。"""
    sx0, sy0, sx1, sy1 = F['safe']
    lo = (sx0 + TEXT_MARGIN, max(sy0, F['coil']) + TEXT_MARGIN, sx1 - TEXT_MARGIN, sy1 - TEXT_MARGIN)
    inside = lambda b: b[0] >= lo[0] and b[1] >= lo[1] and b[2] <= lo[2] and b[3] <= lo[3]  # noqa: E731
    yb = year_geom()['ink']
    r32 = R32.checks(BASE)
    lb = r32['brand_box_mm']
    return {'year_ink_mm': [round(v, 2) for v in yb], 'brand_box_mm': lb, 'year_in_safe': inside(yb), 'brand_in_safe': r32['brand_in_safe'],
            'clear_gap_mm': round(lb[1] - yb[3], 2), 'year_digit_height_mm': round(yb[3] - yb[1], 2),
            'logo_width_mm': r32['logo_width_mm'], 'wordmark_cap_height_mm': r32['wordmark_cap_height_mm'], 'cjk_glyph_height_mm': r32['cjk_glyph_height_mm'],
            'same_as_r32_except_year': True}



def proto(out):
    os.makedirs(out, exist_ok=True)
    shutil.copytree(os.path.join(ROOT, R32.FONT_REL), os.path.join(out, 'fonts'), dirs_exist_ok=True)
    sp = os.path.join(out, f'{CID}.svg')
    open(sp, 'w', encoding='utf-8').write(svg_cover())
    R31.render(sp, os.path.join(out, f'{CID}_full.png'), F['px'])
    print(json.dumps(checks(), ensure_ascii=False))


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
    assert sha256(open(os.path.join(ROOT, CIRCLE_REL), 'rb').read()) == CIRCLE_SHA, 'Penny 提供的圓形 Logo 原檔與紀錄不同'
    LD = json.load(open(os.path.join(ROOT, R31.LAYOUT_DATA), encoding='utf-8'))
    lay_sha = {x['path']: x['sha256'] for x in LD['files']}
    G32 = json.load(open(os.path.join(ROOT, R32_DATA), encoding='utf-8'))
    g32 = {x['path']: x['sha256'] for x in G32['files']}
    files, pdfs = {}, {}

    def save(name, data):
        open(os.path.join(pub, name), 'wb').write(data)
        files[name] = sha256(data)

    def merge(k, cover_page, title, tag):
        src = os.path.join(ROOT, R31.LAYOUT_PDF[k])
        assert sha256(open(src, 'rb').read()) == lay_sha[os.path.basename(src)], f'R26 {k} PDF 與紀錄不同'
        w = PdfWriter()
        w.add_page(cover_page)
        for p in PdfReader(src).pages[1:]:
            w.add_page(p)
        w.add_metadata({'/Title': title, '/Producer': 'cal2027 R33'})
        w._ID = ArrayObject([ByteStringObject(hashlib.md5(f'cal2027-R33-{tag}'.encode()).digest())] * 2)
        b = io.BytesIO()
        w.write(b)
        name = f'cal2027_{k}_preview_R33.pdf'
        save(name, b.getvalue())
        return name, os.path.basename(src)
    with tempfile.TemporaryDirectory() as tmp:
        # 直式修正版
        svg = svg_cover()
        sp = os.path.join(src_dir, f'{CID}.svg')
        open(sp, 'w', encoding='utf-8').write(svg)
        full = R31.render(sp, os.path.join(tmp, 'full.png'), F['px'])
        art = R31.render(sp, os.path.join(tmp, 'art.png'), F['px'], 'txt,vec')
        save(f'cover_{CID}_f.jpg', R31.jpeg(full, 90))
        view = full.resize(F['vpx'], Image.LANCZOS)
        save(f'cover_{CID}_v.jpg', R31.jpeg(view, 88))
        aj = os.path.join(tmp, 'art.jpg')
        open(aj, 'wb').write(R31.jpeg(art, 95, 0))
        cp = os.path.join(tmp, 'cover.pdf')
        cover_pdf(aj, cp)
        vname, vsrc = merge('V', PdfReader(cp).pages[0], f'2027 桌曆 直式 完整預覽（封面 {CID}＝V-D2 修正版，待 Owner 確認；R33）', 'V')
        # 橫式：已接受 H-L1，封面頁直接取 R32 H-L1 完整預覽 PDF 的第 1 頁
        h32 = os.path.join(ROOT, R32_PUB, 'cal2027_H-L1_preview_R32.pdf')
        assert sha256(open(h32, 'rb').read()) == g32['cal2027_H-L1_preview_R32.pdf'], 'R32 H-L1 PDF 與紀錄不同'
        hname, hsrc = merge('H', PdfReader(h32).pages[0], '2027 桌曆 橫式 完整預覽（封面 H-L1＝Owner 已接受；R33）', 'H')
        for k, name, src, cover in (('H', hname, hsrc, 'H-L1'), ('V', vname, vsrc, CID)):
            pp = os.path.join(pub, name)
            R = PdfReader(pp)
            fonts = R31.pdf_fonts(pp, (1, 1))
            Fk = FMT[k]
            ref = view if k == 'V' else Image.open(os.path.join(ROOT, R32_PUB, 'cover_H-L1_v.jpg')).convert('RGB')
            pim = np.asarray(R31.pdf_page_png(pp, 1, Fk['vpx'], tmp)).astype(int)
            diff = round(float(np.abs(pim - np.asarray(ref).astype(int)).mean()), 2)
            # 內頁與 R26 已接受 PDF 逐頁比對（頁面內容物件相同）
            base = PdfReader(os.path.join(ROOT, R31.LAYOUT_PDF[k]))
            same = all(R.pages[i].get_contents().get_data() == base.pages[i].get_contents().get_data() for i in range(1, len(base.pages)))
            pg = R.pages[0]
            pdfs[k] = {'path': name, 'cover': cover, 'pages': len(R.pages), 'media_mm': [round(float(v) / PT, 2) for v in pg.mediabox[2:]],
                       'trim_mm': [round(float(v) / PT, 2) for v in pg.trimbox], 'cover_fonts': fonts, 'cover_vs_preview_mean_abs_diff': diff,
                       'interior_from': src, 'interior_pages_same_as_r26': same, 'bytes': os.path.getsize(pp)}
    out = []
    for name, h in sorted(files.items()):
        e = {'path': name, 'sha256': h, 'bytes': os.path.getsize(os.path.join(pub, name))}
        if name.endswith('.jpg'):
            im = Image.open(os.path.join(pub, name))
            e['px'] = [im.width, im.height]
        out.append(e)
    D = {'round': ROUND,
         'note': '橫式 H-L1 Owner 已接受（沿用 R32，不改）；直式 V-D2 修正版一張：只把 2027 改成金色＋收斂光暈，品牌區依 Owner 決定維持 R32 白色 Logo，待 Owner 確認。生成 0、付費 0、未購買素材；R32 檔案不覆蓋。',
         'horizontal': {'id': 'H-L1', 'status': 'accepted', 'preview': {'view': f'{R32_PUB.split("/")[-1]}/cover_H-L1_v.jpg', 'full': f'{R32_PUB.split("/")[-1]}/cover_H-L1_f.jpg'},
                        'note': '封面與 R32 H-L1 相同（PDF 第 1 頁直接取自 R32 H-L1 完整預覽 PDF）'},
         'vertical': {'id': CID, 'base': 'V-D2', 'status': 'pending_owner', 'source': f'{CID}.svg', 'source_sha256': sha256(svg.encode('utf-8')),
                      'px': list(F['px']), 'checks': checks(),
                      'palette': {'year_gold_gradient': GOLD, 'year_glow': {'color': GLOW, 'layers': [{'blur_mm': a, 'opacity': b} for a, b in GLOWS]},
                                  'brand': 'R32 V-D2 原樣：' + json.dumps(R32.DARK, ensure_ascii=False)},
                      'background': '與 R32 V-D2 相同（build_cal_m5_cover_r32.dark_art）'},
         'logo': LOGO_STATUS,
         'fonts': [{'key': k, 'file': Fo['file'], 'family': Fo['family'], 'license': Fo['license']} for k, Fo in FONTS.items()],
         'format': {kk: v for kk, v in F.items() if kk not in ('px', 'vpx')} | {'text_margin_mm': TEXT_MARGIN},
         'pdf': pdfs, 'files': out}
    with open(data_path, 'w', encoding='utf-8') as fh:
        json.dump(D, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    return D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--proto')
    a = ap.parse_args()
    if a.proto:
        proto(a.proto)
        return
    if a.check:
        old = json.load(open(os.path.join(ROOT, DATA_REL), encoding='utf-8'))
        with tempfile.TemporaryDirectory() as tmp:
            D = build(os.path.join(tmp, 'src'), os.path.join(tmp, 'pub'), os.path.join(tmp, 'd.json'))
            same = json.loads(json.dumps(D, ensure_ascii=False)) == old
            pub = os.path.join(ROOT, PUB_REL)
            diff = [x['path'] for x in D['files'] if not os.path.exists(os.path.join(pub, x['path'])) or sha256(open(os.path.join(pub, x['path']), 'rb').read()) != x['sha256']]
            extra = sorted(set(os.listdir(pub)) - {x['path'] for x in D['files']})
            sdiff = open(os.path.join(tmp, 'src', f'{CID}.svg'), 'rb').read() != open(os.path.join(ROOT, SRC_REL, f'{CID}.svg'), 'rb').read()
        ok = same and not diff and not extra and not sdiff
        print(json.dumps({'check': 'PASS' if ok else 'FAIL', 'data_same': same, 'files': len(D['files']), 'diff': diff, 'extra': extra, 'source_diff': sdiff}, ensure_ascii=False))
        sys.exit(0 if ok else 1)
    D = build(os.path.join(ROOT, SRC_REL), os.path.join(ROOT, PUB_REL), os.path.join(ROOT, DATA_REL))
    print(json.dumps({'checks': D['vertical']['checks'], 'pdf': {k: {kk: v[kk] for kk in ('cover', 'pages', 'trim_mm', 'cover_fonts', 'cover_vs_preview_mean_abs_diff', 'interior_pages_same_as_r26', 'bytes')}
                                                                 for k, v in D['pdf'].items()}}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
