"""TASK-CAL-001 M-5 R35：直式 V-D2-R34B 定案；橫式 H-L1 只替「2027」加細緻輕微的光暈（修正版待確認）。不生成、不付費、不買素材。

- 橫式修正版 H-L1-R35G：以 R32 H-L1 已接受版本的向量來源為基底（build_cal_m5_cover_r32.svg_cover('H-L1')），
  只在年份文字下方加一組光暈：同一個「2027」字形複本，經高斯模糊、低不透明度疊在背景上——
  一層極淡的亮光（讓光暈讀成「光」而不是陰影）、一層淡藍柔光、一層貼近字緣的微光。
  年份本體（字型、大小、位置、深藍 #1E2A78）、背景、Logo、公司名稱、品牌區與其他元素全部不變；不模糊字本體、不描邊、不投影。
- 直式：沿用已接受的 V-D2-R34B（封面頁直接取自 R34 藍色圖示版 PDF 第 1 頁，不重畫）。
- 核對：原版與修正版用同一流程各算一次 300 dpi 圖逐像素比較，變動只能落在年份附近；PDF 封面頁的向量內容與 R32 H-L1 相同（光暈在背景點陣裡）。
- 輸出：可編輯來源 docs/calendar/cover_r35/H-L1-R35G.svg（＋fonts）；public/cover35/：修正版預覽、原版／修正版年份局部（600 dpi）、
  兩份完整預覽 PDF（橫式 28 面＝修正版、直式 32 面＝已接受 V-D2-R34B）。R32～R34 檔案不覆蓋。
用法：python3 docs/calendar/tools/build_cal_m5_cover_r35.py [--check]
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

ROUND = 'M-5 R35'
BASE = 'H-L1'
CID = 'H-L1-R35G'
V_ID = 'V-D2-R34B'
SRC_REL = 'docs/calendar/cover_r35'
PUB_REL = 'docs/calendar/decision_site/public/cover35'
DATA_REL = 'docs/calendar/data/cal_m5_cover_r35.json'
R32_PUB, R32_DATA = 'docs/calendar/decision_site/public/cover32', 'docs/calendar/data/cal_m5_cover_r32.json'
R34_PUB, R34_DATA = 'docs/calendar/decision_site/public/cover34', 'docs/calendar/data/cal_m5_cover_r34.json'
F, PT = R32.FMT['H'], R32.PT
# 光暈（由下往上疊）：（模糊半徑 mm, 顏色, 不透明度）
GLOWS = [(2.8, '#F3F6FF', 0.45),    # 極淡亮光：讓整圈讀成光，不像陰影
         (1.6, '#8FA4E7', 0.36),    # 淡藍柔光：主要的光暈
         (0.45, '#6E85D6', 0.14)]   # 貼近字緣的微光：讓實心深藍的邊緣不那麼生硬
GLOW_REACH_MM = 9.0                 # 驗證用：光暈可能影響的範圍（年份字形外框外擴，約 3×最大模糊半徑）
YEAR_CROP_MM = (96.0, 104.0, 196.0, 146.0)
CROP_SCALE = 2                      # 600 dpi


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def svg_base():
    return R32.svg_cover(BASE)


def svg_glow():
    s = svg_base()
    m = re.search(r'<g class="txt">\n(<text [^>]*>2027</text>)', s)
    assert m, '找不到年份文字'
    yt = m.group(1)
    W, H = F['W'], F['H']
    defs = '<defs>' + ''.join(f'<filter id="hg{i}" x="-30" y="-30" width="{W + 60}" height="{H + 60}" filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="{sd}"/></filter>'
                              for i, (sd, _, _) in enumerate(GLOWS)) + '</defs>'
    g = '<g class="glow"><desc>年份光暈（畫面點陣的一部分）：同一字形複本模糊、低不透明度，不改字本體</desc>' + \
        ''.join(re.sub(r'fill="[^"]+"', f'fill="{c}" opacity="{op}" filter="url(#hg{i})"', yt) for i, (_, c, op) in enumerate(GLOWS)) + '</g>'
    assert s.count('<g class="txt">') == 1
    s = s.replace('<g class="txt">', defs + '\n' + g + '\n<g class="txt">', 1)
    t_old = '<title>2027 桌曆封面候選 H-L1｜橫式淺色 版本 1（四季光影＋兌心科技，含 2 mm 出血）</title>'
    assert s.count(t_old) == 1
    s = s.replace(t_old, f'<title>2027 桌曆封面 橫式 {CID}｜H-L1 年份輕光暈修正版（其餘同 R32 H-L1，含 2 mm 出血）</title>')
    s = s.replace('.txt text{', '.txt text,.glow text{')
    return s


def compare(a_png, b_png):
    A, B = np.asarray(Image.open(a_png).convert('RGB')).astype(int), np.asarray(Image.open(b_png).convert('RGB')).astype(int)
    px = F['px'][0] / F['W']
    d = np.abs(A - B).max(axis=2)
    ys, xs = np.nonzero(d > 0)
    yb = R32.year_geom(BASE)['ink']
    r = GLOW_REACH_MM
    zone = [int((yb[0] - r) * px), int((yb[1] - r) * px), int(np.ceil((yb[2] + r) * px)), int(np.ceil((yb[3] + r) * px))]
    outside = int(((xs < zone[0]) | (xs >= zone[2]) | (ys < zone[1]) | (ys >= zone[3])).sum())
    # 字本體內部（字形外框內、遠離邊緣）應不變：用原版深藍像素當遮罩
    ink = (np.abs(A - np.array([0x1E, 0x2A, 0x78])).max(axis=2) <= 3)
    return {'changed_px': int((d > 0).sum()), 'changed_bbox_mm': [round(xs.min() / px, 2), round(ys.min() / px, 2), round((xs.max() + 1) / px, 2), round((ys.max() + 1) / px, 2)],
            'year_ink_mm': [round(v, 2) for v in yb], 'allowed_zone_mm': [round(v / px, 2) for v in zone], 'changed_outside_zone_px': outside,
            'max_channel_change': int(d.max()), 'mean_change_in_zone': round(float(d[zone[1]:zone[3], zone[0]:zone[2]].mean()), 2),
            'year_body_px': int(ink.sum()), 'year_body_changed_px': int((ink & (d > 2)).sum())}


def crop_render(svg, tmp, tag, out_jpg, box_mm):
    """只算年份這一塊（600 dpi）：把 SVG 的可視範圍改成局部框，原版與修正版用同一方法。"""
    W, H = F['W'], F['H']
    x0, y0, x1, y1 = box_mm
    head = f'viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm"'
    assert svg.count(head) == 1
    sv = svg.replace(head, f'viewBox="{x0} {y0} {x1 - x0} {y1 - y0}" width="{x1 - x0}mm" height="{y1 - y0}mm"')
    p = os.path.join(tmp, f'{tag}_crop.svg')
    open(p, 'w', encoding='utf-8').write(sv)
    px = F['px'][0] / W * CROP_SCALE
    size = (round((x1 - x0) * px), round((y1 - y0) * px))
    im = R31.render(p, os.path.join(tmp, f'{tag}_crop.png'), size)
    open(out_jpg, 'wb').write(R31.jpeg(im, 92, 0))
    return list(im.size)


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
    G32 = {x['path']: x['sha256'] for x in json.load(open(os.path.join(ROOT, R32_DATA), encoding='utf-8'))['files']}
    G34 = {x['path']: x['sha256'] for x in json.load(open(os.path.join(ROOT, R34_DATA), encoding='utf-8'))['files']}
    LD = {x['path']: x['sha256'] for x in json.load(open(os.path.join(ROOT, R31.LAYOUT_DATA), encoding='utf-8'))['files']}
    files, pdfs = {}, {}

    def save(name, data):
        open(os.path.join(pub, name), 'wb').write(data)
        files[name] = sha256(data)

    def merge(k, cover_page, title, tag):
        src = os.path.join(ROOT, R31.LAYOUT_PDF[k])
        assert sha256(open(src, 'rb').read()) == LD[os.path.basename(src)], f'R26 {k} PDF 與紀錄不同'
        w = PdfWriter()
        w.add_page(cover_page)
        for p in PdfReader(src).pages[1:]:
            w.add_page(p)
        w.add_metadata({'/Title': title, '/Producer': 'cal2027 R35'})
        w._ID = ArrayObject([ByteStringObject(hashlib.md5(f'cal2027-R35-{tag}'.encode()).digest())] * 2)
        b = io.BytesIO()
        w.write(b)
        name = f'cal2027_{k}_preview_R35.pdf'
        save(name, b.getvalue())
        return name, src
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copytree(os.path.join(ROOT, SRC_REL, 'fonts'), os.path.join(tmp, 'fonts'))
        sa, sb = svg_base(), svg_glow()
        assert sa == open(os.path.join(ROOT, R32.SRC_REL, f'{BASE}.svg'), encoding='utf-8').read(), 'R32 H-L1 來源與 repo 不同'
        open(os.path.join(src_dir, f'{CID}.svg'), 'w', encoding='utf-8').write(sb)
        pa, pb = os.path.join(tmp, 'A.svg'), os.path.join(tmp, 'B.svg')
        open(pa, 'w', encoding='utf-8').write(sa)
        open(pb, 'w', encoding='utf-8').write(sb)
        fa = R31.render(pa, os.path.join(tmp, 'A.png'), F['px'])
        fb = R31.render(pb, os.path.join(tmp, 'B.png'), F['px'])
        assert sha256(R31.jpeg(fa, 90)) == G32[f'cover_{BASE}_f.jpg'], '原版重算與 R32 交付預覽不同'
        cmp_ = compare(os.path.join(tmp, 'A.png'), os.path.join(tmp, 'B.png'))
        assert cmp_['changed_px'] > 0 and cmp_['changed_outside_zone_px'] == 0, f'年份附近以外有變動：{cmp_}'
        save(f'cover_{CID}_f.jpg', R31.jpeg(fb, 90))
        view = fb.resize(F['vpx'], Image.LANCZOS)
        save(f'cover_{CID}_v.jpg', R31.jpeg(view, 88))
        crops = {}
        for tag, sv, fn in (('orig', sa, f'year_{BASE}_600dpi.jpg'), ('glow', sb, f'year_{CID}_600dpi.jpg')):
            crops[tag] = crop_render(sv, tmp, tag, os.path.join(pub, fn), YEAR_CROP_MM)
            files[fn] = sha256(open(os.path.join(pub, fn), 'rb').read())
        # 橫式 PDF：背景點陣（含光暈）＋與 R32 相同的向量（年份、中文、細線、Logo）
        art = R31.render(pb, os.path.join(tmp, 'B_art.png'), F['px'], 'txt,vec')
        aj = os.path.join(tmp, 'art.jpg')
        open(aj, 'wb').write(R31.jpeg(art, 95, 0))
        cp = os.path.join(tmp, 'cover.pdf')
        R32.cover_pdf(BASE, aj, cp)
        hname, hsrc = merge('H', PdfReader(cp).pages[0], f'2027 桌曆 橫式 完整預覽（封面 {CID}＝H-L1 年份輕光暈修正版，待 Owner 確認；R35）', 'H')
        # 直式 PDF：封面頁直接取自 R34 藍色圖示版 PDF 第 1 頁（已接受）
        v34 = os.path.join(ROOT, R34_PUB, f'cal2027_V_preview_{V_ID}.pdf')
        assert sha256(open(v34, 'rb').read()) == G34[f'cal2027_V_preview_{V_ID}.pdf'], 'R34 藍色圖示版 PDF 與紀錄不同'
        vname, vsrc = merge('V', PdfReader(v34).pages[0], f'2027 桌曆 直式 完整預覽（封面 {V_ID}＝Owner 已接受；R35）', 'V')
        h32 = PdfReader(os.path.join(ROOT, R32_PUB, f'cal2027_{BASE}_preview_R32.pdf')).pages[0]
        xo = lambda pg: re.sub(rb'/FormXob\.[0-9a-f]+', b'/FormXob', pg.get_contents().get_data())  # noqa: E731
        for k, name, src, cover, ref_view, ref_page in (('H', hname, hsrc, CID, view, h32), ('V', vname, vsrc, V_ID, None, PdfReader(v34).pages[0])):
            pp = os.path.join(pub, name)
            R = PdfReader(pp)
            base = PdfReader(src)
            same = all(R.pages[i].get_contents().get_data() == base.pages[i].get_contents().get_data() for i in range(1, len(base.pages)))
            Fk = R32.FMT[k]
            if ref_view is None:
                ref_view = Image.open(os.path.join(ROOT, R34_PUB, f'cover_{V_ID}_v.jpg')).convert('RGB')
            pim = np.asarray(R31.pdf_page_png(pp, 1, Fk['vpx'], tmp)).astype(int)
            pdfs[k] = {'path': name, 'cover': cover, 'pages': len(R.pages), 'trim_mm': [round(float(v) / PT, 2) for v in R.pages[0].trimbox],
                       'cover_fonts': R31.pdf_fonts(pp, (1, 1)), 'cover_vs_preview_mean_abs_diff': round(float(np.abs(pim - np.asarray(ref_view).astype(int)).mean()), 2),
                       # 封面頁向量內容與基準相同（背景圖的物件名稱依圖片內容命名，比較前先統一）
                       'cover_vector_stream_same_as': ('R32 H-L1' if k == 'H' else 'R34 V-D2-R34B') if xo(R.pages[0]) == xo(ref_page) else None,
                       'interior_pages_same_as_r26': same, 'bytes': os.path.getsize(pp)}
    out = []
    for name, h in sorted(files.items()):
        e = {'path': name, 'sha256': h, 'bytes': os.path.getsize(os.path.join(pub, name))}
        if name.endswith('.jpg'):
            im = Image.open(os.path.join(pub, name))
            e['px'] = [im.width, im.height]
        out.append(e)
    D = {'round': ROUND,
         'note': '直式 V-D2-R34B 已接受（定案）；橫式 H-L1 只替 2027 加細緻輕微的光暈（修正版 H-L1-R35G 待 Owner 確認）。生成 0、付費 0；R32～R34 檔案不覆蓋。',
         'horizontal': {'base': BASE, 'base_preview': {'view': f'cover32/cover_{BASE}_v.jpg', 'full': f'cover32/cover_{BASE}_f.jpg'},
                        'id': CID, 'status': 'pending_owner', 'source': f'{CID}.svg', 'source_sha256': sha256(sb.encode('utf-8')), 'px': list(F['px']),
                        'glow_layers': [{'blur_mm': a, 'color': b, 'opacity': c} for a, b, c in GLOWS],
                        'unchanged': '年份字型、大小、位置、深藍 #1E2A78；背景、Logo、公司名稱、品牌區與其他元素',
                        'compare': cmp_, 'year_zoom_mm': list(YEAR_CROP_MM), 'year_zoom_px': crops['glow'],
                        'year_zoom': {'orig': f'year_{BASE}_600dpi.jpg', 'glow': f'year_{CID}_600dpi.jpg'}},
         'vertical': {'id': V_ID, 'status': 'accepted', 'preview': {'view': f'cover34/cover_{V_ID}_v.jpg', 'full': f'cover34/cover_{V_ID}_f.jpg'},
                      'note': 'PDF 封面頁直接取自 R34 藍色圖示版 PDF 第 1 頁，不重畫'},
         'pdf': pdfs, 'files': out}
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
    print(json.dumps({'compare': D['horizontal']['compare'], 'pdf': {k: {kk: v[kk] for kk in ('cover', 'pages', 'cover_fonts', 'cover_vs_preview_mean_abs_diff', 'cover_vector_stream_same_as', 'interior_pages_same_as_r26', 'bytes')}
                                                                     for k, v in D['pdf'].items()}}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
