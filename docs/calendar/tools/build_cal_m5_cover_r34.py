"""TASK-CAL-001 M-5 R34：直式封面 Logo 藍白比較（只試做比較，不代表接受）。不生成、不付費、不買素材。

- A＝R33 直式修正版（白色圖示），檔案不動，沿用 public/cover33/。
- B＝以 R33 直式為基底，只把 Insight Software 左側圖示（官網 logo01.svg 的 st0 路徑）由白色填回官方原色 #2B33F2；
  英文字標、「兌心科技」、細線維持白色；金色 2027、背景、排版、尺寸、間距全部不變；不加圓底、光暈、描邊、陰影。
  做法是在 R33 的向量來源上改一個填色，另存新版本（V-D2-R34B），不重新生成圖片。
- 核對：A、B 用同一流程各算一次 300 dpi 圖，逐像素比較，變動只能落在圖示外框內；記錄藍色圖示與周圍底色的亮度對比（照實記錄，不補救）。
- 輸出：可編輯來源 docs/calendar/cover_r34/V-D2-R34B.svg（＋fonts）；public/cover34/：B 預覽、B 直式完整預覽 PDF（32 面）、A／B 品牌區放大圖（600 dpi）。
用法：python3 docs/calendar/tools/build_cal_m5_cover_r34.py [--check]
"""
import argparse
import hashlib
import io
import json
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
import build_cal_m5_cover_r32 as R32  # noqa: E402
import build_cal_m5_cover_r33 as R33  # noqa: E402

ROUND = 'M-5 R34'
CID = 'V-D2-R34B'
SRC_REL = 'docs/calendar/cover_r34'
PUB_REL = 'docs/calendar/decision_site/public/cover34'
DATA_REL = 'docs/calendar/data/cal_m5_cover_r34.json'
R33_PUB = 'docs/calendar/decision_site/public/cover33'
R33_DATA = 'docs/calendar/data/cal_m5_cover_r33.json'
F, PT = R33.F, R32.PT
WHITE = R32.DARK['logo']
ICON_BLUE = '#2B33F2'
CROP_MM = (44.0, 181.0, 100.0, 196.0)    # 品牌區放大範圍（含出血畫布座標，mm）
CROP_SCALE = 2                          # 600 dpi


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def official_icon_color():
    """從官網 logo01.svg 原檔讀圖示（st0）的填色，核對與 #2B33F2 相同。"""
    t = open(os.path.join(ROOT, R32.LOGO_REL), encoding='utf-8').read()
    assert sha256(t.encode('utf-8')) == R32.LOGO_SHA, '官網 Logo 檔與紀錄不同'
    m = re.search(r'\.st0\{[^}]*fill:(#[0-9A-Fa-f]{6})', t)
    assert m and m.group(1).upper() == ICON_BLUE, f'官網圖示色與 {ICON_BLUE} 不同：{m and m.group(1)}'
    return m.group(1).upper()


def svg_a():
    return R33.svg_cover()


def svg_b():
    s = svg_a()
    old = f'fill="{WHITE}" fill-rule="evenodd"'
    assert s.count(old) == 1, '圖示路徑應只有一條（st0，evenodd）'
    s = s.replace(old, f'fill="{ICON_BLUE}" fill-rule="evenodd"')
    t_old = 'V-D2 修正版（金色年份；品牌區同 R32）'
    assert s.count(t_old) == 1
    s = s.replace(t_old, 'V-D2 藍色圖示比較版 B（R33 只把圖示填回官方藍 #2B33F2）')
    d_old = 'Logo 設計衍生版（官網向量改填白色，待 Owner 確認，非官方版本）'
    assert s.count(d_old) == 1
    s = s.replace(d_old, 'Logo：圖示為官網原色 #2B33F2；Insight Software 字標改填白色（官網向量，等比）')
    s = s.replace(f'<title>2027 桌曆封面 直式 {R33.CID}｜', f'<title>2027 桌曆封面 直式 {CID}｜')
    return s


def icon_box_mm():
    """圖示（st0）在畫布上的外框（mm）。"""
    from fontTools.pens.boundsPen import BoundsPen
    from fontTools.svgLib.path import parse_path
    x0, y0, s = R32.brand_geom(R33.BASE)['logo']
    b = [1e9, 1e9, -1e9, -1e9]
    for c, d in R32.logo_paths():
        if c == 'st0':
            bp = BoundsPen(None)
            parse_path(d, bp)
            bx0, by0, bx1, by1 = bp.bounds
            b = [min(b[0], bx0), min(b[1], by0), max(b[2], bx1), max(b[3], by1)]
    return [x0 + b[0] * s, y0 + b[1] * s, x0 + b[2] * s, y0 + b[3] * s]


def _lum(rgb):
    c = np.asarray(rgb, dtype=float) / 255
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return float(0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2])


def _contrast(a, b):
    la, lb = sorted([_lum(a), _lum(b)], reverse=True)
    return round((la + 0.05) / (lb + 0.05), 2)


def compare(a_png, b_png):
    """A／B 逐像素比較＋圖示辨識度量測（300 dpi 圖）。"""
    A, B = np.asarray(Image.open(a_png).convert('RGB')).astype(int), np.asarray(Image.open(b_png).convert('RGB')).astype(int)
    px = F['px'][0] / F['W']
    diff = np.abs(A - B).max(axis=2) > 0
    ys, xs = np.nonzero(diff)
    ib = icon_box_mm()
    m = 2   # 反鋸齒邊緣容許 2 px
    box = [int(ib[0] * px) - m, int(ib[1] * px) - m, int(np.ceil(ib[2] * px)) + m, int(np.ceil(ib[3] * px)) + m]
    outside = int(((xs < box[0]) | (xs >= box[2]) | (ys < box[1]) | (ys >= box[3])).sum())
    # 辨識度：圖示實心像素（B 中接近官方藍）平均色 vs 圖示外框外一圈的底色
    sub = B[box[1]:box[3], box[0]:box[2]]
    blue = np.array([0x2B, 0x33, 0xF2])
    core = np.abs(sub - blue).max(axis=2) <= 6
    ring = np.zeros(B.shape[:2], bool)
    ring[box[1] - 12:box[3] + 12, box[0] - 12:box[2] + 12] = True
    ring[box[1] - 2:box[3] + 2, box[0] - 2:box[2] + 2] = False
    bg = B[ring].mean(axis=0)
    a_core = A[box[1]:box[3], box[0]:box[2]][core].mean(axis=0)
    b_core = sub[core].mean(axis=0)
    return {'changed_px': int(diff.sum()), 'changed_bbox_px': [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1] if diff.any() else None,
            'icon_box_px': box, 'changed_outside_icon_box_px': outside, 'icon_box_mm': [round(v, 2) for v in ib],
            'icon_size_mm': [round(ib[2] - ib[0], 2), round(ib[3] - ib[1], 2)],
            'icon_core_px': int(core.sum()), 'icon_color_rendered_B': '#%02X%02X%02X' % tuple(int(round(v)) for v in b_core),
            'background_around_icon': '#%02X%02X%02X' % tuple(int(round(v)) for v in bg),
            'contrast_ratio_A_white_icon': _contrast(a_core, bg), 'contrast_ratio_B_blue_icon': _contrast(b_core, bg),
            'contrast_ratio_B_wordmark_white': _contrast([255, 255, 255], bg)}


def crop(png, out_jpg):
    im = Image.open(png).convert('RGB')
    px = im.width / F['W']
    x0, y0, x1, y1 = CROP_MM
    c = im.crop((round(x0 * px), round(y0 * px), round(x1 * px), round(y1 * px)))
    data = R31.jpeg(c, 92, 0)
    open(out_jpg, 'wb').write(data)
    return c.size


def build(src_dir, pub, data_path):
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import ArrayObject, ByteStringObject
    for d in (src_dir, pub):
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith(('.svg', '.jpg', '.pdf')):
                    os.unlink(os.path.join(d, fn))
        os.makedirs(d, exist_ok=True)
    if os.path.realpath(os.path.join(src_dir, 'fonts')) != os.path.realpath(os.path.join(ROOT, SRC_REL, 'fonts')):
        shutil.copytree(os.path.join(ROOT, SRC_REL, 'fonts'), os.path.join(src_dir, 'fonts'), dirs_exist_ok=True)
    color = official_icon_color()
    G33 = json.load(open(os.path.join(ROOT, R33_DATA), encoding='utf-8'))
    g33 = {x['path']: x['sha256'] for x in G33['files']}
    LD = json.load(open(os.path.join(ROOT, R31.LAYOUT_DATA), encoding='utf-8'))
    lay_sha = {x['path']: x['sha256'] for x in LD['files']}
    files = {}

    def save(name, data):
        open(os.path.join(pub, name), 'wb').write(data)
        files[name] = sha256(data)
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copytree(os.path.join(ROOT, SRC_REL, 'fonts'), os.path.join(tmp, 'fonts'))
        sa, sb = svg_a(), svg_b()
        # A 的來源必須與 repo 的 R33 來源相同（A 不重做，只拿來比較）
        assert sa == open(os.path.join(ROOT, R33.SRC_REL, f'{R33.CID}.svg'), encoding='utf-8').read(), 'R33 來源與 repo 不同'
        open(os.path.join(src_dir, f'{CID}.svg'), 'w', encoding='utf-8').write(sb)
        pa, pb = os.path.join(tmp, 'A.svg'), os.path.join(tmp, 'B.svg')
        open(pa, 'w', encoding='utf-8').write(sa)
        open(pb, 'w', encoding='utf-8').write(sb)
        fa = R31.render(pa, os.path.join(tmp, 'A_full.png'), F['px'])
        fb = R31.render(pb, os.path.join(tmp, 'B_full.png'), F['px'])
        cmp_ = compare(os.path.join(tmp, 'A_full.png'), os.path.join(tmp, 'B_full.png'))
        assert cmp_['changed_px'] > 0 and cmp_['changed_outside_icon_box_px'] == 0, f'圖示以外有變動：{cmp_}'
        # A 的這次重算必須與 R33 已交付的預覽相同（同一流程）
        assert sha256(R31.jpeg(fa, 90)) == g33[f'cover_{R33.CID}_f.jpg'], 'A 重算與 R33 交付預覽不同'
        save(f'cover_{CID}_f.jpg', R31.jpeg(fb, 90))
        view = fb.resize(F['vpx'], Image.LANCZOS)
        save(f'cover_{CID}_v.jpg', R31.jpeg(view, 88))
        # 品牌區放大（600 dpi）：A、B 同流程
        big = (F['px'][0] * CROP_SCALE, F['px'][1] * CROP_SCALE)
        crops = {}
        for k, p in (('A', pa), ('B', pb)):
            R31.render(p, os.path.join(tmp, f'{k}_big.png'), big)
            fn = f'brand_{k}_600dpi.jpg'
            crops[k] = crop(os.path.join(tmp, f'{k}_big.png'), os.path.join(pub, fn))
            files[fn] = sha256(open(os.path.join(pub, fn), 'rb').read())
        # B 的完整預覽 PDF：封面＝R33 同一背景點陣＋向量（只有圖示填色不同）＋R26 直式內頁
        art = R31.render(pb, os.path.join(tmp, 'B_art.png'), F['px'], 'txt,vec')
        aj = os.path.join(tmp, 'art.jpg')
        open(aj, 'wb').write(R31.jpeg(art, 95, 0))
        cp = os.path.join(tmp, 'cover.pdf')
        R33.cover_pdf(aj, cp, icon=color)
        src = os.path.join(ROOT, R31.LAYOUT_PDF['V'])
        assert sha256(open(src, 'rb').read()) == lay_sha[os.path.basename(src)], 'R26 直式 PDF 與紀錄不同'
        w = PdfWriter()
        w.add_page(PdfReader(cp).pages[0])
        for p in PdfReader(src).pages[1:]:
            w.add_page(p)
        w.add_metadata({'/Title': f'2027 桌曆 直式 完整預覽（封面 {CID}＝藍色圖示比較版 B，未接受；R34）', '/Producer': 'cal2027 R34'})
        w._ID = ArrayObject([ByteStringObject(hashlib.md5(b'cal2027-R34-V-B').digest())] * 2)
        b = io.BytesIO()
        w.write(b)
        pname = f'cal2027_V_preview_{CID}.pdf'
        save(pname, b.getvalue())
        pp = os.path.join(pub, pname)
        R = PdfReader(pp)
        base = PdfReader(src)
        same = all(R.pages[i].get_contents().get_data() == base.pages[i].get_contents().get_data() for i in range(1, len(base.pages)))
        pim = np.asarray(R31.pdf_page_png(pp, 1, F['vpx'], tmp)).astype(int)
        pdiff = round(float(np.abs(pim - np.asarray(view).astype(int)).mean()), 2)
        # A 的 R33 PDF 與 B 的 PDF：封面頁內容串流只差圖示填色
        a_pdf = PdfReader(os.path.join(ROOT, R33_PUB, 'cal2027_V_preview_R33.pdf'))
        ca, cb = a_pdf.pages[0].get_contents().get_data(), R.pages[0].get_contents().get_data()
        pdf_stream_diff_lines = sum(1 for x, y in zip(ca.split(b'\n'), cb.split(b'\n')) if x != y) + abs(len(ca.split(b'\n')) - len(cb.split(b'\n')))
        pdf = {'path': pname, 'pages': len(R.pages), 'trim_mm': [round(float(v) / PT, 2) for v in R.pages[0].trimbox],
               'cover_fonts': R31.pdf_fonts(pp, (1, 1)), 'cover_vs_preview_mean_abs_diff': pdiff, 'interior_pages_same_as_r26': same,
               'cover_stream_lines_differ_from_r33': pdf_stream_diff_lines, 'bytes': os.path.getsize(pp)}
    out = []
    for name, h in sorted(files.items()):
        e = {'path': name, 'sha256': h, 'bytes': os.path.getsize(os.path.join(pub, name))}
        if name.endswith('.jpg'):
            im = Image.open(os.path.join(pub, name))
            e['px'] = [im.width, im.height]
        out.append(e)
    D = {'round': ROUND,
         'note': '直式 Logo 藍白比較：A＝R33 白色圖示（public/cover33，不動）；B＝只把圖示填回官方藍 #2B33F2，其餘與 R33 相同。只試做比較，不代表接受直式封面。生成 0、付費 0。',
         'a': {'id': R33.CID, 'label': '白色圖示', 'preview': {'view': f'cover33/cover_{R33.CID}_v.jpg', 'full': f'cover33/cover_{R33.CID}_f.jpg'},
               'pdf': 'cover33/cal2027_V_preview_R33.pdf', 'brand_zoom': 'brand_A_600dpi.jpg'},
         'b': {'id': CID, 'label': '藍色圖示', 'source': f'{CID}.svg', 'source_sha256': sha256(sb.encode('utf-8')), 'brand_zoom': 'brand_B_600dpi.jpg'},
         'icon_color': {'official_file': os.path.relpath(os.path.join(ROOT, R32.LOGO_REL), ROOT), 'official_sha256': R32.LOGO_SHA, 'st0_fill_in_file': color, 'used': ICON_BLUE},
         'only_change': '圖示（logo01.svg 的 st0 路徑）填色 #FFFFFF → #2B33F2；英文字標、「兌心科技」、細線、金色 2027、背景、排版、尺寸、間距不變；無圓底、光暈、描邊、陰影',
         'compare': cmp_, 'brand_zoom_mm': list(CROP_MM), 'brand_zoom_px': list(crops['B']),
         'pdf': pdf, 'files': out}
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
            sdiff = open(os.path.join(tmp, 'src', f'{CID}.svg'), 'rb').read() != open(os.path.join(ROOT, SRC_REL, f'{CID}.svg'), 'rb').read()
        ok = same and not diff and not extra and not sdiff
        print(json.dumps({'check': 'PASS' if ok else 'FAIL', 'data_same': same, 'files': len(D['files']), 'diff': diff, 'extra': extra, 'source_diff': sdiff}, ensure_ascii=False))
        sys.exit(0 if ok else 1)
    D = build(os.path.join(ROOT, SRC_REL), os.path.join(ROOT, PUB_REL), os.path.join(ROOT, DATA_REL))
    print(json.dumps({'compare': D['compare'], 'pdf': D['pdf'], 'icon_color': D['icon_color']}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
