"""TASK-CAL-001 M-5 R33：橫式 H-L1 定案；直式 V-D2 修正版（金色年份＋收斂光暈、圓形 Logo 品牌區）。不生成、不付費、不買素材。

- 橫式：沿用 Owner 已接受的 R32 H-L1（封面頁直接取自 R32 H-L1 完整預覽 PDF 第 1 頁，不重畫、不改）。
- 直式：以 R32 V-D2 為基礎（背景＝build_cal_m5_cover_r32.dark_art() 原樣、置中編排、留白）。
  · 「2027」：同一字型（Cormorant Garamond Light）、置中；柔和香檳金→暖金黃的上下漸層（受光感），字形本體清楚；
    背後一層輕微、收斂的同色光暈（只在畫面點陣裡，以「濾色」疊在背景光影上）。這是印刷圖稿裡的金色視覺效果，不是燙金或金墨。
  · 「兌心科技」：淡香檳白（比年份淡、不同色），與圓形 Logo 並排、垂直置中。
  · Logo：Owner 指定「藍色圓底、白色圖示與白色 Insight Software 字樣」那款完整 Logo＝Penny 在本輪提供的原檔
    （docs/calendar/cover_r33/brand/insight-software-logo-circle.png，800×800 PNG、圓外透明），原樣等比放入，不重畫、不加圓、不改色。
- 輸出：可編輯來源 docs/calendar/cover_r33/（SVG、fonts、brand 來源紀錄）；預覽與兩份完整預覽 PDF 在 docs/calendar/decision_site/public/cover33/
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
SRC_REL = 'docs/calendar/cover_r33'
PUB_REL = 'docs/calendar/decision_site/public/cover33'
DATA_REL = 'docs/calendar/data/cal_m5_cover_r33.json'
R32_PUB = 'docs/calendar/decision_site/public/cover32'
R32_DATA = 'docs/calendar/data/cal_m5_cover_r32.json'
FMT, PT, TEXT_MARGIN, FONTS, fmt = R32.FMT, R32.PT, R32.TEXT_MARGIN, R32.FONTS, R32.fmt
F = FMT['V']
# ---------- 配色 ----------
GOLD = [(0.0, '#F7EBCB'), (0.34, '#EDD49E'), (0.7, '#DFBB78'), (1.0, '#CDA764')]   # 柔和香檳金（上、受光）→ 暖金黃（下）；色相 38–45°，不偏橘
GLOW = '#E6C27F'          # 光暈同色系
CJK = '#EDE4CF'           # 「兌心科技」淡香檳白：比年份淡，和年份同一暖色調，和 Logo 的藍白分開
# ---------- 版面（mm，含 2 mm 出血的畫布座標；置中軸 x=72） ----------
YEAR = dict(x=72.0, y=164.0, size=40, ls=R32.YEAR_LS)       # 基線由 R32 的 172 上移 8 mm，讓出圓形 Logo 的高度
BRAND = dict(cx=72.0, bottom=195.0, d=22.0, gap=3.6, cjk_size=3.5)   # 圓形 Logo 直徑 22 mm：圓內字樣大寫高 1.65 mm、約 924 ppi
GLOWS = [(2.0, 0.42), (0.6, 0.24)]   # （模糊半徑 mm, 不透明度）：一層柔光＋一層貼近字緣的微光；不模糊字本體
LOGO_REL = SRC_REL + '/brand/insight-software-logo-circle.png'
LOGO_SHA = '859e51e7ddf0e9a4c7cccc0a725d5e5ae9a134c15110b0fcdbdbdc8056665416'
LOGO_PX = 800              # 原檔邊長（px）；圓＝整張（圓心 400,400、半徑 400），圓外透明
LOGO_CAP_PX = 60           # 原檔裡「Insight」的 I 高度（px）＝圓內英文字樣的大寫高
LOGO_STATUS = {
    'wanted': 'Owner 指定：藍色圓底、白色圖示與白色 Insight Software 字樣的完整 Logo（Penny 提供的那款）',
    'found': True,
    'source': 'Penny 在 R33 進行中直接提供（2026-11-03，訊息原文「這個logo也給你做參考」）；原檔原樣保存，未重畫、未改色、未加圓',
    'file': 'brand/insight-software-logo-circle.png',
    'sha256': LOGO_SHA,
    'format': '800×800 PNG（RGBA）；圓外透明；藍色 #2B33F2（與官網 Logo 圖示同色）',
    'verified': '和官方 YouTube、Facebook 頭像（同一款排法、白底藍圖示黑字）逐像素比對：圖示與字樣重疊率約 98%（差異只在邊緣反鋸齒）；'
                '和官網長條 logo01.svg 的比例不同（圓形款的圖示與兩行字距另有排法），所以不能用長條 Logo 加藍圓代替',
}


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def year_geom():
    return R32.text_box('year', '2027', YEAR['size'], YEAR['ls'], YEAR['x'], YEAR['y'], 'middle')


def logo_bytes():
    b = open(os.path.join(ROOT, LOGO_REL), 'rb').read()
    assert sha256(b) == LOGO_SHA, 'Penny 提供的圓形 Logo 原檔與紀錄不同'
    return b


def brand_geom():
    """品牌區：[圓形 Logo] 兌心科技，整組以 x=72 置中；中文字形外框垂直置中於圓心。"""
    B = BRAND
    ls = 0.12 * B['cjk_size']
    w = R32.text_box('cjk', '兌心科技', B['cjk_size'], ls, 0, 0)
    total = B['d'] + B['gap'] + w['width']
    x0 = B['cx'] - total / 2
    r = B['d'] / 2
    cx, cy = x0 + r, B['bottom'] - r
    base = cy - (w['ink'][1] + w['ink'][3]) / 2
    cj = R32.text_box('cjk', '兌心科技', B['cjk_size'], ls, x0 + B['d'] + B['gap'], base)
    return {'circle': (cx, cy, r), 'cjk': cj, 'cjk_ls': ls,
            'box': [x0, min(cy - r, cj['ink'][1]), x0 + total, max(cy + r, cj['ink'][3])]}


def svg_cover():
    W, H = F['W'], F['H']
    defs, art = R32.dark_art()   # 與 R32 V-D2 同一張背景
    yg, bg = year_geom(), brand_geom()
    y0, y1 = yg['ink'][1], yg['ink'][3]
    fam = lambda k: f'font-family="&apos;{FONTS[k]["family"]}&apos;"'  # noqa: E731
    ytext = lambda attrs: (f'<text x="{fmt(yg["x"])}" y="{fmt(yg["y"])}" {fam("year")} font-size="{YEAR["size"]}" '  # noqa: E731
                           f'letter-spacing="{YEAR["ls"]}" {attrs}>2027</text>')
    gdefs = ['<defs>', f'<linearGradient id="ygold" gradientUnits="userSpaceOnUse" x1="0" y1="{fmt(y0)}" x2="0" y2="{fmt(y1)}">' +
             ''.join(f'<stop offset="{a}" stop-color="{c}"/>' for a, c in GOLD) + '</linearGradient>']
    for i, (sd, _) in enumerate(GLOWS):
        gdefs.append(f'<filter id="yglow{i}" x="-30" y="-30" width="{W + 60}" height="{H + 60}" filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="{sd}"/></filter>')
    gdefs.append('</defs>')
    cx, cy, r = bg['circle']
    cj = bg['cjk']
    o = [f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">',
         f'<title>2027 桌曆封面 直式 {CID}｜V-D2 修正版（金色年份、圓形 Logo），含 2 mm 出血</title>',
         R32.font_css().replace('.txt text{', '.txt text,.glow text{'), defs, '\n'.join(gdefs), art,
         '<g class="glow" style="mix-blend-mode:screen"><desc>年份光暈（畫面點陣的一部分）</desc>'] + \
        [ytext(f'fill="{GLOW}" opacity="{op}" filter="url(#yglow{i})"') for i, (_, op) in enumerate(GLOWS)] + \
        ['</g>', '<g class="txt">', ytext('fill="url(#ygold)"'),
         f'<text x="{fmt(cj["x"])}" y="{fmt(cj["y"])}" {fam("cjk")} font-size="{fmt(BRAND["cjk_size"])}" letter-spacing="{fmt(bg["cjk_ls"])}" fill="{CJK}">兌心科技</text>',
         '</g>', '<g class="vec" id="logo"><desc>Logo：Penny 提供的原檔（藍色圓底、白色圖示與 Insight Software 字樣），原樣等比放入</desc>',
         f'<image href="brand/{os.path.basename(LOGO_REL)}" x="{fmt(cx - r)}" y="{fmt(cy - r)}" width="{fmt(2 * r)}" height="{fmt(2 * r)}" preserveAspectRatio="xMidYMid meet"/>',
         '</g>', '</svg>']
    return '\n'.join(o) + '\n'


# ---------- PDF ----------
def _font(c, k):
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    if 'R33-' + k not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont('R33-' + k, os.path.join(ROOT, R32.FONT_REL, FONTS[k]['file'])))
    return 'R33-' + k


def cover_pdf(art_jpg, path):
    """直式封面一頁：背景（含年份光暈）＝300 dpi JPEG；金色年份＝向量字形裁切＋線性漸層；中文為向量；Logo＝原檔 PNG（無損、含透明）；字型子集嵌入。"""
    from reportlab import rl_config
    from reportlab.lib.colors import HexColor
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas as rl_canvas
    rl_config.useA85 = 0
    W, H = F['W'], F['H']
    c = rl_canvas.Canvas(path, pagesize=(W * PT, H * PT), invariant=1, pageCompression=1, initialFontName=_font(None, 'cjk'), initialFontSize=8)
    t = F['trim']
    c.setTrimBox((t * PT, t * PT, (W - t) * PT, (H - t) * PT))
    c.setBleedBox((0, 0, W * PT, H * PT))
    c.drawImage(ImageReader(io.BytesIO(open(art_jpg, 'rb').read())), 0, 0, W * PT, H * PT)
    yg, bg = year_geom(), brand_geom()
    # 金色年份：字形當裁切路徑，再畫上下漸層
    c.saveState()
    to = c.beginText(yg['x'] * PT, (H - yg['y']) * PT)
    to.setFont(_font(c, 'year'), YEAR['size'] * PT)
    to.setCharSpace(YEAR['ls'] * PT)
    to.setTextRenderMode(7)
    to.textOut('2027')
    c.drawText(to)
    y0, y1 = yg['ink'][1], yg['ink'][3]
    c.linearGradient(0, (H - y0) * PT, 0, (H - y1) * PT, [HexColor(col) for _, col in GOLD], [a for a, _ in GOLD], extend=True)
    c.restoreState()
    cj = bg['cjk']
    to = c.beginText(cj['x'] * PT, (H - cj['y']) * PT)
    to.setFont(_font(c, 'cjk'), BRAND['cjk_size'] * PT)
    to.setCharSpace(bg['cjk_ls'] * PT)
    to.setFillColor(HexColor(CJK))
    to.textOut('兌心科技')
    c.drawText(to)
    cx, cy, r = bg['circle']
    # 圓形 Logo：原檔 PNG 原樣嵌入（無損 Flate＋透明遮罩），等比放入直徑 2r 的方框
    c.drawImage(ImageReader(io.BytesIO(logo_bytes())), (cx - r) * PT, (H - cy - r) * PT, 2 * r * PT, 2 * r * PT, mask='auto')
    c.showPage()
    c.save()


def checks():
    sx0, sy0, sx1, sy1 = F['safe']
    lo = (sx0 + TEXT_MARGIN, max(sy0, F['coil']) + TEXT_MARGIN, sx1 - TEXT_MARGIN, sy1 - TEXT_MARGIN)
    inside = lambda b: b[0] >= lo[0] and b[1] >= lo[1] and b[2] <= lo[2] and b[3] <= lo[3]  # noqa: E731
    yg, bg = year_geom(), brand_geom()
    yb, lb, cj = yg['ink'], bg['box'], bg['cjk']['ink']
    return {'year_ink_mm': [round(v, 2) for v in yb], 'brand_box_mm': [round(v, 2) for v in lb], 'year_in_safe': inside(yb), 'brand_in_safe': inside(lb),
            'clear_gap_mm': round(lb[1] - yb[3], 2), 'year_digit_height_mm': round(yb[3] - yb[1], 2), 'logo_diameter_mm': BRAND['d'],
            'logo_wordmark_cap_height_mm': round(LOGO_CAP_PX / LOGO_PX * BRAND['d'], 2), 'logo_effective_ppi': round(LOGO_PX / (BRAND['d'] / 25.4)),
            'cjk_glyph_height_mm': round(cj[3] - cj[1], 2), 'year_center_x_mm': round((yb[0] + yb[2]) / 2, 2), 'brand_center_x_mm': round((lb[0] + lb[2]) / 2, 2)}


def proto(out):
    os.makedirs(out, exist_ok=True)
    shutil.copytree(os.path.join(ROOT, R32.FONT_REL), os.path.join(out, 'fonts'), dirs_exist_ok=True)
    shutil.copytree(os.path.join(ROOT, SRC_REL, 'brand'), os.path.join(out, 'brand'), dirs_exist_ok=True)
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
    logo_bytes()
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
         'note': '橫式 H-L1 Owner 已接受（沿用 R32，不改）；直式 V-D2 修正版一張（金色年份＋收斂光暈、Penny 提供的藍色圓底 Logo），待 Owner 確認。生成 0、付費 0、未購買素材；R32 檔案不覆蓋。',
         'horizontal': {'id': 'H-L1', 'status': 'accepted', 'preview': {'view': f'{R32_PUB.split("/")[-1]}/cover_H-L1_v.jpg', 'full': f'{R32_PUB.split("/")[-1]}/cover_H-L1_f.jpg'},
                        'note': '封面與 R32 H-L1 相同（PDF 第 1 頁直接取自 R32 H-L1 完整預覽 PDF）'},
         'vertical': {'id': CID, 'base': 'V-D2', 'status': 'pending_owner', 'source': f'{CID}.svg', 'source_sha256': sha256(svg.encode('utf-8')),
                      'px': list(F['px']), 'checks': checks(),
                      'palette': {'year_gold_gradient': GOLD, 'year_glow': {'color': GLOW, 'layers': [{'blur_mm': a, 'opacity': b} for a, b in GLOWS]}, 'cjk': CJK},
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
