"""TASK-CAL-001 M-5 R36：加強橫式「2027」光感（加強版 H-L1-R36L，待 Owner 確認）。不生成、不付費、不買素材。

- 以 R32 H-L1（已接受）的向量來源為基底，只改「2027」（取代 R35 的淡光暈）：
  · 字形內部：上下線性漸層——上緣較亮的藍（受光面）→ 中段 → 下半部保留原本深藍 #1E2A78。參考直式 V-D2-R34B 金色年份「上亮下深」的受光方式，顏色仍是藍。
  · 外光：同一字形複本模糊後疊在背景上——一層極淡亮光、一層「上強下弱」的淡藍外光（漸層透明度，光集中在受光的上緣，下緣不起霧）、一層貼字緣微光。
  · 年份字型、大小、位置，背景、Logo、公司名稱、品牌區與其他元素不變；字本體不模糊，無描邊、浮雕、星芒、投影。
- 核對：與 R35、與 R32 原版用同一流程各算一次 300 dpi 圖逐像素比較，變動只能在年份附近；量測年份上緣／下緣的亮度差（完整封面尺寸看得出受光面）。
- 輸出：可編輯來源 docs/calendar/cover_r36/H-L1-R36L.svg（＋fonts）；public/cover36/：加強版全圖、年份局部（600 dpi，與 R35 的局部同一取法）、
  橫式 28 面完整預覽 PDF（年份為向量裁切＋漸層，外光在背景點陣裡）。R35 與更早檔案不覆蓋。直式 V-D2-R34B 已定案，不動。
用法：python3 docs/calendar/tools/build_cal_m5_cover_r36.py [--check]
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
import build_cal_m5_cover_r35 as R35  # noqa: E402

ROUND = 'M-5 R36'
BASE = 'H-L1'
CID = 'H-L1-R36L'
SRC_REL = 'docs/calendar/cover_r36'
PUB_REL = 'docs/calendar/decision_site/public/cover36'
DATA_REL = 'docs/calendar/data/cal_m5_cover_r36.json'
R35_PUB, R35_DATA = 'docs/calendar/decision_site/public/cover35', 'docs/calendar/data/cal_m5_cover_r35.json'
R32_DATA = 'docs/calendar/data/cal_m5_cover_r32.json'
F, PT = R32.FMT['H'], R32.PT
# 字形內部（上→下）：上緣受光的亮藍 → 深藍；下半部維持原本 #1E2A78
FILL = [(0.0, '#7A92F2'), (0.22, '#5770E0'), (0.5, '#30419F'), (0.75, '#1E2A78'), (1.0, '#1E2A78')]
# 外光的「上強下弱」：淡藍，透明度隨高度遞減
GLOW_FILL = [(0.0, '#8CA3F0', 1.0), (0.55, '#8CA3F0', 0.6), (1.0, '#8CA3F0', 0.25)]
# 外光三層（由下往上）：（模糊半徑 mm, 顏色或漸層, 不透明度）
GLOWS = [(3.4, '#F5F8FF', 0.6),         # 極淡亮光：讓整圈讀成光
         (2.0, 'url(#yglowg)', 0.55),   # 淡藍外光：上強下弱
         (0.7, '#6F88E4', 0.18)]        # 貼字緣微光
GLOW_REACH_MM = 11.0                    # 驗證用：外光可能影響的範圍（約 3×最大模糊半徑）
YEAR_CROP_MM, CROP_SCALE = R35.YEAR_CROP_MM, R35.CROP_SCALE


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def _grad(gid, stops, yb):
    return (f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{R32.fmt(yb[1])}" x2="0" y2="{R32.fmt(yb[3])}">' +
            ''.join(f'<stop offset="{st[0]}" stop-color="{st[1]}"' + (f' stop-opacity="{st[2]}"' if len(st) > 2 else '') + '/>' for st in stops) + '</linearGradient>')


def svg_lit():
    s = R32.svg_cover(BASE)
    m = re.search(r'<g class="txt">\n(<text [^>]*>2027</text>)', s)
    assert m, '找不到年份文字'
    yt = m.group(1)
    yb = R32.year_geom(BASE)['ink']
    W, H = F['W'], F['H']
    defs = ('<defs>' + _grad('ylit', FILL, yb) + _grad('yglowg', GLOW_FILL, yb) +
            ''.join(f'<filter id="hg{i}" x="-30" y="-30" width="{W + 60}" height="{H + 60}" filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="{sd}"/></filter>'
                    for i, (sd, _, _) in enumerate(GLOWS)) + '</defs>')
    g = '<g class="glow"><desc>年份外光（畫面點陣的一部分）：同一字形複本模糊，上強下弱</desc>' + \
        ''.join(re.sub(r'fill="[^"]+"', f'fill="{c}" opacity="{op}" filter="url(#hg{i})"', yt) for i, (_, c, op) in enumerate(GLOWS)) + '</g>'
    assert s.count('<g class="txt">') == 1 and s.count(yt) == 1
    s = s.replace('<g class="txt">', defs + '\n' + g + '\n<g class="txt">', 1)
    s = s.replace(yt, re.sub(r'fill="[^"]+"', 'fill="url(#ylit)"', yt), 1)
    t_old = '<title>2027 桌曆封面候選 H-L1｜橫式淺色 版本 1（四季光影＋兌心科技，含 2 mm 出血）</title>'
    assert s.count(t_old) == 1
    s = s.replace(t_old, f'<title>2027 桌曆封面 橫式 {CID}｜H-L1 年份光感加強版（字內受光漸層＋淡藍外光；其餘同 R32 H-L1，含 2 mm 出血）</title>')
    return s.replace('.txt text{', '.txt text,.glow text{')


def zone_diff(a_png, b_png):
    A, B = np.asarray(Image.open(a_png).convert('RGB')).astype(int), np.asarray(Image.open(b_png).convert('RGB')).astype(int)
    px = F['px'][0] / F['W']
    d = np.abs(A - B).max(axis=2)
    ys, xs = np.nonzero(d > 0)
    yb = R32.year_geom(BASE)['ink']
    r = GLOW_REACH_MM
    zone = [int((yb[0] - r) * px), int((yb[1] - r) * px), int(np.ceil((yb[2] + r) * px)), int(np.ceil((yb[3] + r) * px))]
    outside = int(((xs < zone[0]) | (xs >= zone[2]) | (ys < zone[1]) | (ys >= zone[3])).sum())
    return {'changed_px': int((d > 0).sum()), 'changed_bbox_mm': [round(xs.min() / px, 2), round(ys.min() / px, 2), round((xs.max() + 1) / px, 2), round((ys.max() + 1) / px, 2)],
            'allowed_zone_mm': [round(v / px, 2) for v in zone], 'changed_outside_zone_px': outside, 'max_channel_change': int(d.max())}


def lit_measure(view_img, orig_view):
    """完整封面尺寸（顯示版 1205 px 寬）量年份的受光面：以原版深藍像素當字形遮罩，比較上緣 1/4 與下緣 1/4 的亮度。"""
    A = np.asarray(orig_view.convert('RGB')).astype(int)
    B = np.asarray(view_img.convert('RGB')).astype(int)
    ink = np.abs(A - np.array([0x1E, 0x2A, 0x78])).max(axis=2) <= 6
    ys, xs = np.nonzero(ink)
    y0, y1 = ys.min(), ys.max()
    h = y1 - y0
    top = ink.copy()
    top[y0 + h // 4:] = False
    bot = ink.copy()
    bot[:y1 - h // 4] = False
    lum = lambda m: float((0.2126 * B[..., 0] + 0.7152 * B[..., 1] + 0.0722 * B[..., 2])[m].mean())  # noqa: E731
    lum_a = lambda m: float((0.2126 * A[..., 0] + 0.7152 * A[..., 1] + 0.0722 * A[..., 2])[m].mean())  # noqa: E731
    return {'view_px': list(view_img.size), 'year_ink_px': int(ink.sum()), 'top_quarter_luma': round(lum(top), 1), 'bottom_quarter_luma': round(lum(bot), 1),
            'orig_top_quarter_luma': round(lum_a(top), 1), 'orig_bottom_quarter_luma': round(lum_a(bot), 1),
            'top_mean_color': '#%02X%02X%02X' % tuple(int(round(v)) for v in B[top].mean(axis=0)),
            'bottom_mean_color': '#%02X%02X%02X' % tuple(int(round(v)) for v in B[bot].mean(axis=0))}


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
    G35 = {x['path']: x['sha256'] for x in json.load(open(os.path.join(ROOT, R35_DATA), encoding='utf-8'))['files']}
    G32 = {x['path']: x['sha256'] for x in json.load(open(os.path.join(ROOT, R32_DATA), encoding='utf-8'))['files']}
    LD = {x['path']: x['sha256'] for x in json.load(open(os.path.join(ROOT, R31.LAYOUT_DATA), encoding='utf-8'))['files']}
    files = {}

    def save(name, data):
        open(os.path.join(pub, name), 'wb').write(data)
        files[name] = sha256(data)
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copytree(os.path.join(ROOT, SRC_REL, 'fonts'), os.path.join(tmp, 'fonts'))
        s0, s35, s36 = R32.svg_cover(BASE), R35.svg_glow(), svg_lit()
        assert s35 == open(os.path.join(ROOT, R35.SRC_REL, f'{R35.CID}.svg'), encoding='utf-8').read(), 'R35 來源與 repo 不同'
        open(os.path.join(src_dir, f'{CID}.svg'), 'w', encoding='utf-8').write(s36)
        pngs = {}
        for tag, sv in (('r32', s0), ('r35', s35), ('r36', s36)):
            p = os.path.join(tmp, f'{tag}.svg')
            open(p, 'w', encoding='utf-8').write(sv)
            pngs[tag] = (p, R31.render(p, os.path.join(tmp, f'{tag}.png'), F['px']))
        assert sha256(R31.jpeg(pngs['r32'][1], 90)) == G32[f'cover_{BASE}_f.jpg'], 'R32 原版重算與交付預覽不同'
        assert sha256(R31.jpeg(pngs['r35'][1], 90)) == G35[f'cover_{R35.CID}_f.jpg'], 'R35 重算與交付預覽不同'
        vs35 = zone_diff(os.path.join(tmp, 'r35.png'), os.path.join(tmp, 'r36.png'))
        vs32 = zone_diff(os.path.join(tmp, 'r32.png'), os.path.join(tmp, 'r36.png'))
        assert vs35['changed_outside_zone_px'] == 0 and vs32['changed_outside_zone_px'] == 0, f'年份附近以外有變動：{vs35} {vs32}'
        fb = pngs['r36'][1]
        save(f'cover_{CID}_f.jpg', R31.jpeg(fb, 90))
        view = fb.resize(F['vpx'], Image.LANCZOS)
        save(f'cover_{CID}_v.jpg', R31.jpeg(view, 88))
        lit = lit_measure(view, pngs['r32'][1].resize(F['vpx'], Image.LANCZOS))
        lit_r35 = lit_measure(pngs['r35'][1].resize(F['vpx'], Image.LANCZOS), pngs['r32'][1].resize(F['vpx'], Image.LANCZOS))
        fn = f'year_{CID}_600dpi.jpg'
        crop_px = R35.crop_render(s36, tmp, 'r36', os.path.join(pub, fn), YEAR_CROP_MM)
        files[fn] = sha256(open(os.path.join(pub, fn), 'rb').read())
        # PDF：背景點陣（含外光）＋向量（年份＝裁切＋漸層；中文、細線、Logo 同 R32）
        art = R31.render(pngs['r36'][0], os.path.join(tmp, 'r36_art.png'), F['px'], 'txt,vec')
        aj = os.path.join(tmp, 'art.jpg')
        open(aj, 'wb').write(R31.jpeg(art, 95, 0))
        cp = os.path.join(tmp, 'cover.pdf')
        R32.cover_pdf(BASE, aj, cp, year_grad=FILL)
        src = os.path.join(ROOT, R31.LAYOUT_PDF['H'])
        assert sha256(open(src, 'rb').read()) == LD[os.path.basename(src)], 'R26 橫式 PDF 與紀錄不同'
        w = PdfWriter()
        w.add_page(PdfReader(cp).pages[0])
        for p in PdfReader(src).pages[1:]:
            w.add_page(p)
        w.add_metadata({'/Title': f'2027 桌曆 橫式 完整預覽（封面 {CID}＝H-L1 年份光感加強版，待 Owner 確認；R36）', '/Producer': 'cal2027 R36'})
        w._ID = ArrayObject([ByteStringObject(hashlib.md5(b'cal2027-R36-H').digest())] * 2)
        b = io.BytesIO()
        w.write(b)
        pname = 'cal2027_H_preview_R36.pdf'
        save(pname, b.getvalue())
        pp = os.path.join(pub, pname)
        R = PdfReader(pp)
        base = PdfReader(src)
        same = all(R.pages[i].get_contents().get_data() == base.pages[i].get_contents().get_data() for i in range(1, len(base.pages)))
        stream = R.pages[0].get_contents().get_data()
        pim = np.asarray(R31.pdf_page_png(pp, 1, F['vpx'], tmp)).astype(int)
        pdf = {'path': pname, 'cover': CID, 'pages': len(R.pages), 'trim_mm': [round(float(v) / PT, 2) for v in R.pages[0].trimbox],
               'cover_fonts': R31.pdf_fonts(pp, (1, 1)), 'cover_vs_preview_mean_abs_diff': round(float(np.abs(pim - np.asarray(view).astype(int)).mean()), 2),
               'year_vector_gradient': b' sh' in stream or b'\nsh' in stream, 'interior_pages_same_as_r26': same, 'bytes': os.path.getsize(pp)}
    out = []
    for name, h in sorted(files.items()):
        e = {'path': name, 'sha256': h, 'bytes': os.path.getsize(os.path.join(pub, name))}
        if name.endswith('.jpg'):
            im = Image.open(os.path.join(pub, name))
            e['px'] = [im.width, im.height]
        out.append(e)
    D = {'round': ROUND,
         'note': '橫式 H-L1 年份光感加強版 H-L1-R36L（字內受光漸層＋上強下弱淡藍外光），待 Owner 確認；R35 保留供比較；直式 V-D2-R34B 已定案不動。生成 0、付費 0。',
         'horizontal': {'base': BASE, 'compare_with': R35.CID, 'id': CID, 'status': 'pending_owner', 'source': f'{CID}.svg', 'source_sha256': sha256(s36.encode('utf-8')), 'px': list(F['px']),
                        'fill_gradient': [{'offset': a, 'color': c} for a, c in FILL],
                        'glow_fill': [{'offset': a, 'color': c, 'opacity': o} for a, c, o in GLOW_FILL],
                        'glow_layers': [{'blur_mm': a, 'paint': b, 'opacity': c} for a, b, c in GLOWS],
                        'unchanged': '年份字型、大小、位置；背景、Logo、公司名稱、品牌區與其他元素',
                        'diff_vs_r35': vs35, 'diff_vs_r32': vs32, 'lit_at_cover_size': lit, 'lit_at_cover_size_r35': lit_r35,
                        'year_zoom': {'r35': f'cover35/year_{R35.CID}_600dpi.jpg', 'r36': fn}, 'year_zoom_mm': list(YEAR_CROP_MM), 'year_zoom_px': crop_px},
         'vertical': {'id': 'V-D2-R34B', 'status': 'accepted', 'note': '已定案，不動；完整預覽 PDF 沿用 cover35/cal2027_V_preview_R35.pdf'},
         'pdf': {'H': pdf}, 'files': out}
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
    h = D['horizontal']
    print(json.dumps({'diff_vs_r35': h['diff_vs_r35'], 'diff_vs_r32': h['diff_vs_r32'], 'lit': h['lit_at_cover_size'], 'lit_r35': h['lit_at_cover_size_r35'],
                      'pdf': {k: v for k, v in D['pdf']['H'].items() if k != 'trim_mm'}}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
