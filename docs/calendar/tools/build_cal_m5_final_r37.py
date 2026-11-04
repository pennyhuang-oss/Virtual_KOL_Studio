"""TASK-CAL-001 M-5 R37：雙款封面定案（橫式 H-L1-R36L、直式 V-D2-R34B）＋定案預覽 PDF 的印前檢查。不改設計、不重生。

- 定案來源：已驗證的完整預覽 PDF——橫式 public/cover36/cal2027_H_preview_R36.pdf（28 面）、直式 public/cover35/cal2027_V_preview_R35.pdf（32 面）。
- 定案預覽：把來源 PDF 的每一頁原樣複製成新檔，只換文件標題／主旨（標「定案預覽」、註明不是交印檔），頁面內容、圖片、字型、尺寸框一律不動；
  逐頁核對與來源相同。輸出 public/cover37/cal2027_{H,V}_final_preview.pdf。
- 印前檢查（只做檔案層面能確認的）：頁數、成品尺寸／出血框、頁序與內頁一致性、字型嵌入、圖片解析度與色彩、透明、輸出意圖；
  已知安全區與照片框引用既有紀錄。廠商規格與印刷效果另列「待確認」，不判定通過。
- 輸出：docs/calendar/data/cal_m5_final_r37.json、docs/calendar/CAL_29_M5_R37_FINAL_PREFLIGHT.generated.md。
用法：python3 docs/calendar/tools/build_cal_m5_final_r37.py [--check]
"""
import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_cal_m5_cover_r31 as R31  # noqa: E402
import build_cal_m5_cover_r32 as R32  # noqa: E402

ROUND = 'M-5 R37'
PUBD = 'docs/calendar/decision_site/public'
PUB_REL = PUBD + '/cover37'
DATA_REL = 'docs/calendar/data/cal_m5_final_r37.json'
DOC_REL = 'docs/calendar/CAL_29_M5_R37_FINAL_PREFLIGHT.generated.md'
PT = R32.PT
BOOKS = {
    'H': {'zh': '橫式', 'cover': 'H-L1-R36L', 'cover_desc': '橫式淺色 版本 1，年份光感加強版（R36）', 'faces': 28,
          'src': PUBD + '/cover36/cal2027_H_preview_R36.pdf', 'src_data': 'docs/calendar/data/cal_m5_cover_r36.json', 'src_commit': 'f1b2947bacc95f96803df80c86fcf7a43a32404b',
          'cover_ref': PUBD + '/cover36/cal2027_H_preview_R36.pdf', 'cover_ref_data': 'docs/calendar/data/cal_m5_cover_r36.json',
          'cover_safe_from': ('docs/calendar/data/cal_m5_cover_r32.json', 'H-L1'), 'preview': {'view': 'cover36/cover_H-L1-R36L_v.jpg', 'full': 'cover36/cover_H-L1-R36L_f.jpg'}},
    'V': {'zh': '直式', 'cover': 'V-D2-R34B', 'cover_desc': '直式深色 版本 2，金色年份、藍色圖示（R34 B）', 'faces': 32,
          'src': PUBD + '/cover35/cal2027_V_preview_R35.pdf', 'src_data': 'docs/calendar/data/cal_m5_cover_r35.json', 'src_commit': '6add91528468166a3cf0b75984e49b9faa53d2d6',
          'cover_ref': PUBD + '/cover34/cal2027_V_preview_V-D2-R34B.pdf', 'cover_ref_data': 'docs/calendar/data/cal_m5_cover_r34.json',
          'cover_safe_from': ('docs/calendar/data/cal_m5_cover_r32.json', 'V-D2'), 'preview': {'view': 'cover34/cover_V-D2-R34B_v.jpg', 'full': 'cover34/cover_V-D2-R34B_f.jpg'}},
}
OUT_NAME = 'cal2027_{k}_final_preview.pdf'
VENDOR_PENDING = [
    ('線圈／打孔', '線圈實際寬度、打孔位置與裝訂區沒有書面規格；本案以畫布上緣 12 mm 為線圈假設區（編輯器示意量得橫式 8.9、直式 9.7 mm），需廠商確認'),
    ('正背面與旋轉', '編輯器面號與實體紙張正反面的對應、背面是否自動旋轉 180° 未知；本 PDF 單面正向逐面排列，未旋轉任何面'),
    ('解析度要求', '編輯器只顯示「好／標準／差」三級、沒有公開數字門檻；橫式照片有效約 271 ppi、直式約 325–366 ppi，未放大；300 ppi 是本案工作目標，不是廠商門檻'),
    ('RGB／CMYK 與 ICC', '成品以 CMYK 四色印刷；本 PDF 圖片為 DeviceRGB、沒有嵌入 ICC 描述檔、沒有輸出意圖；由誰轉 CMYK、用哪個描述檔需廠商確認'),
    ('交件規格', '交件方式（編輯器逐面上傳或整份 PDF）、是否需要 PDF/X、裁切標記、單檔上限（說明頁 300MB／編輯器設定值 30）待廠商確認；本 PDF 為 PDF 1.4、無裁切標記'),
    ('透明', '兩款封面的品牌區細分隔線用 55% 不透明度（PDF 透明度設定）；其餘為不透明圖片與向量；RIP 是否需要先平面化待廠商確認'),
]
PROOF_FOCUS = [
    ('橫式', '淺色四季光影漸層（大面積淺色、細膩色階是否有斷層或偏色）'),
    ('橫式', '藍色年份光感（字內由亮藍到深藍的漸層、淡藍外光是否保留、筆畫是否清楚）'),
    ('直式', '深色暗部（近黑深藍的層次是否塌黑、有無色偏）'),
    ('直式', '金色年份（香檳金到暖金黃的漸層與輕微光暈；印刷金色是 CMYK 色，不是燙金）'),
    ('直式', '小尺寸藍色圖示（約 8.2×4.9 mm 的品牌藍圖示在深底上的辨識度）'),
]


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def _norm(stream):
    return re.sub(rb'/FormXob\.[0-9a-f]+', b'/FormXob', stream)


def _imgs(page):
    out = []
    res = page.get('/Resources') or {}
    xo = res.get('/XObject') or {}
    for name, ref in xo.items():
        o = ref.get_object()
        if o.get('/Subtype') == '/Image':
            out.append((o.get('/Width'), o.get('/Height'), sha256(o._data)))
        elif o.get('/Subtype') == '/Form':
            r2 = (o.get('/Resources') or {}).get('/XObject') or {}
            for _, rr in r2.items():
                oo = rr.get_object()
                if oo.get('/Subtype') == '/Image':
                    out.append((oo.get('/Width'), oo.get('/Height'), sha256(oo._data)))
    return sorted(out)


def _alpha(page):
    res = page.get('/Resources') or {}
    gs = res.get('/ExtGState') or {}
    vals = set()
    for _, ref in gs.items():
        o = ref.get_object()
        for k in ('/CA', '/ca'):
            if k in o and float(o[k]) < 1:
                vals.add(round(float(o[k]), 3))
        if '/SMask' in o and o['/SMask'] != '/None':
            vals.add('smask')
    return sorted(vals, key=str)


def _mm(box):
    return [round(float(v) / PT, 2) for v in box]


def pdf_images(path):
    rows = subprocess.run(['pdfimages', '-list', path], capture_output=True, text=True, check=True).stdout.splitlines()[2:]
    out = []
    for ln in rows:
        c = ln.split()
        if len(c) < 14:
            continue
        out.append({'page': int(c[0]), 'type': c[2], 'w': int(c[3]), 'h': int(c[4]), 'color': c[5], 'enc': c[8], 'x_ppi': int(c[12]), 'y_ppi': int(c[13])})
    return out


def pdf_fonts_all(path):
    rows = subprocess.run(['pdffonts', path], capture_output=True, text=True, check=True).stdout.splitlines()[2:]
    return [{'name': r.split()[0].split('+')[-1], 'subset': '+' in r.split()[0], 'emb': r.split()[-5], 'sub': r.split()[-4]} for r in rows if r.strip()]


def build(pub, data_path, doc_path):
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import ArrayObject, ByteStringObject
    os.makedirs(pub, exist_ok=True)
    for fn in os.listdir(pub):
        if fn.endswith('.pdf'):
            os.unlink(os.path.join(pub, fn))
    L = json.load(open(os.path.join(ROOT, R31.LAYOUT_DATA), encoding='utf-8'))
    LD = {x['path']: x['sha256'] for x in L['files']}
    files, books = [], {}
    for k, B in BOOKS.items():
        src = os.path.join(ROOT, B['src'])
        srec = {x['path']: x['sha256'] for x in json.load(open(os.path.join(ROOT, B['src_data']), encoding='utf-8'))['files']}
        src_bytes = open(src, 'rb').read()
        assert sha256(src_bytes) == srec[os.path.basename(src)], f'{k} 定案來源 PDF 與紀錄不同'
        S = PdfReader(src)
        w = PdfWriter()
        for p in S.pages:
            w.add_page(p)
        w.add_metadata({'/Title': f'2027 桌曆 {B["zh"]} 定案預覽（封面 {B["cover"]}，Owner 已接受）',
                        '/Subject': '定案預覽｜不是交印檔｜交印前仍需廠商確認規格與打樣，並經 Penny 另行核准（TASK-CAL-001 M-5 R37）',
                        '/Keywords': 'final preview; not a print-ready file; vendor specs and proof pending; print approval pending',
                        '/Author': 'Virtual KOL Studio', '/Producer': 'cal2027 R37'})
        w._ID = ArrayObject([ByteStringObject(hashlib.md5(f'cal2027-R37-final-{k}'.encode()).digest())] * 2)
        b = io.BytesIO()
        w.write(b)
        name = OUT_NAME.format(k=k)
        open(os.path.join(pub, name), 'wb').write(b.getvalue())
        out_path = os.path.join(pub, name)
        R = PdfReader(out_path)
        # 逐頁與來源相同（內容串流、圖片、尺寸框）
        same_src = len(R.pages) == len(S.pages) and all(
            R.pages[i].get_contents().get_data() == S.pages[i].get_contents().get_data() and _imgs(R.pages[i]) == _imgs(S.pages[i]) and
            _mm(R.pages[i].mediabox) == _mm(S.pages[i].mediabox) and _mm(R.pages[i].trimbox) == _mm(S.pages[i].trimbox) and _mm(R.pages[i].bleedbox) == _mm(S.pages[i].bleedbox)
            for i in range(len(S.pages)))
        # 封面頁＝已接受版本的封面頁；內頁＝R26 已接受排版逐頁相同
        cref = PdfReader(os.path.join(ROOT, B['cover_ref'])).pages[0]
        crec = {x['path']: x['sha256'] for x in json.load(open(os.path.join(ROOT, B['cover_ref_data']), encoding='utf-8'))['files']}
        assert sha256(open(os.path.join(ROOT, B['cover_ref']), 'rb').read()) == crec[os.path.basename(B['cover_ref'])]
        cover_same = _norm(R.pages[0].get_contents().get_data()) == _norm(cref.get_contents().get_data()) and _imgs(R.pages[0]) == _imgs(cref)
        lay = os.path.join(ROOT, R31.LAYOUT_PDF[k])
        assert sha256(open(lay, 'rb').read()) == LD[os.path.basename(lay)]
        LP = PdfReader(lay)
        interior_same = len(LP.pages) == len(R.pages) and all(R.pages[i].get_contents().get_data() == LP.pages[i].get_contents().get_data() and _imgs(R.pages[i]) == _imgs(LP.pages[i])
                                                                for i in range(1, len(LP.pages)))
        F = L['formats'][k]
        media_ok = all(_mm(p.mediabox) == [0.0, 0.0, float(F['W']), float(F['H'])] for p in R.pages)
        trim_ok = all(_mm(p.trimbox) == [float(F['trim']), float(F['trim']), float(F['W'] - F['trim']), float(F['H'] - F['trim'])] for p in R.pages)
        bleed_ok = all(_mm(p.bleedbox) == [0.0, 0.0, float(F['W']), float(F['H'])] for p in R.pages)
        rot = sorted({int(p.get('/Rotate', 0)) for p in R.pages})
        fonts = pdf_fonts_all(out_path)
        imgs = pdf_images(out_path)
        roles = [(p['face'], p['role'], p.get('month')) for p in L['pages'][k]]
        photo_faces = [f for f, r, _ in roles if r == 'photo']
        photo_imgs = [x for x in imgs if x['page'] in photo_faces]
        eff = [ph['eff_ppi'] for p in L['pages'][k] for ph in p.get('photos', []) if ph.get('eff_ppi')]
        up = any(ph.get('resampled_up') for p in L['pages'][k] for ph in p.get('photos', []) if ph.get('role') != 'cover_thumb')
        alpha = {i + 1: a for i, p in enumerate(R.pages) if (a := _alpha(p))}
        root = R.trailer['/Root']
        version = open(out_path, 'rb').read(8).decode('latin-1').strip().lstrip('%')
        cs_name, cs_role = BOOKS[k]['cover_safe_from']
        cchk = next(c for c in json.load(open(os.path.join(ROOT, cs_name), encoding='utf-8'))['covers'] if c['id'] == cs_role)['checks']
        books[k] = {
            'cover': B['cover'], 'cover_desc': B['cover_desc'], 'status': 'owner_accepted', 'preview': B['preview'],
            'source': {'file': B['src'].replace(PUBD + '/', ''), 'sha256': sha256(src_bytes), 'bytes': len(src_bytes), 'commit': B['src_commit']},
            'final_preview': {'file': f'cover37/{name}', 'sha256': sha256(open(out_path, 'rb').read()), 'bytes': os.path.getsize(out_path),
                              'pages_identical_to_source': same_src, 'metadata_title': f'2027 桌曆 {B["zh"]} 定案預覽（封面 {B["cover"]}，Owner 已接受）'},
            'checks': {
                'pages': len(R.pages), 'pages_expected': B['faces'], 'pages_ok': len(R.pages) == B['faces'],
                'canvas_mm': [F['W'], F['H']], 'trim_mm': [F['W'] - 2 * F['trim'], F['H'] - 2 * F['trim']], 'bleed_mm_each_side': F['trim'],
                'media_ok': media_ok, 'trim_ok': trim_ok, 'bleed_ok': bleed_ok, 'rotation': rot,
                'cover_page_is_accepted_version': cover_same, 'interior_same_as_r26_accepted': interior_same,
                'page_order': [{'face': f, 'role': r, 'month': m} for f, r, m in roles],
                'fonts': fonts, 'fonts_all_embedded_subset': all(f['emb'] == 'yes' and f['sub'] == 'yes' for f in fonts),
                'images': {'count': len(imgs), 'colors': sorted({x['color'] for x in imgs}), 'encodings': sorted({x['enc'] for x in imgs}),
                           'smask': sum(1 for x in imgs if x['type'] == 'smask'), 'cover_art_ppi': [x['x_ppi'] for x in imgs if x['page'] == 1],
                           'photo_pages': len(photo_imgs), 'photo_ppi_min': min(x['x_ppi'] for x in photo_imgs), 'photo_ppi_max': max(x['x_ppi'] for x in photo_imgs)},
                'photo_frame_mm': ([F['photo']['B'][2] - F['photo']['B'][0], F['photo']['B'][3] - F['photo']['B'][1]] if k == 'H' else
                                   [F['photo']['V'][2] - F['photo']['V'][0], F['photo']['V'][3] - F['photo']['V'][1]]),
                'photo_eff_ppi_from_r26': [min(eff), max(eff)], 'photo_resampled_up': up,
                'transparency': {str(p): v for p, v in alpha.items()}, 'output_intents': '/OutputIntents' in root, 'pdf_version': version,
                'cover_text_safe': {'year_in_safe': cchk['year_in_safe'], 'brand_in_safe': cchk['brand_in_safe'], 'note': '年份與品牌區位置與 R32 相同；字形外框在文字安全區內再留 3 mm、避開上緣 12 mm 線圈假設區'},
                'text_safe_mm': F['text_safe'], 'vendor_safe_mm': F['vendor_safe'], 'coil_assumed_mm': F['coil_assumed'], 'coil_measured_mm': F['coil_measured']}}
        c = books[k]['checks']
        assert c['pages_ok'] and media_ok and trim_ok and bleed_ok and same_src and cover_same and interior_same and c['fonts_all_embedded_subset'] and not up, f'{k} 檢查未通過'
        files.append({'path': name, 'sha256': books[k]['final_preview']['sha256'], 'bytes': books[k]['final_preview']['bytes']})
    D = {'round': ROUND,
         'note': '雙款封面定案：橫式 H-L1-R36L、直式 V-D2-R34B（Owner 已接受）。定案預覽 PDF 為已驗證預覽 PDF 的逐頁原樣複製（只換文件標題）。不是交印檔；交印仍待 Penny 另行核准。不改設計、不重生。',
         'books': books, 'vendor_pending': [{'item': a, 'detail': b} for a, b in VENDOR_PENDING],
         'proof_focus': [{'book': a, 'item': b} for a, b in PROOF_FOCUS],
         'not_judged': '沒有實際打樣，不判定印刷效果通過；螢幕預覽不等於印刷效果', 'files': files}
    with open(data_path, 'w', encoding='utf-8') as fh:
        json.dump(D, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    open(doc_path, 'w', encoding='utf-8').write(render_doc(D))
    return D


def render_doc(D):
    yn = lambda v: '是' if v else '否'  # noqa: E731
    o = ['<!-- 由 docs/calendar/tools/build_cal_m5_final_r37.py 產生；請勿手動修改 -->', '',
         '# CAL_29｜2027 桌曆封面定案與定案預覽印前檢查（M-5 R37）', '',
         '> **定案預覽，不是交印檔。** 封面確認不等於交印核准；交印前仍需廠商確認規格、實際打樣，並由 Penny 另行核准。本輪不改設計、不重生。', '',
         '## 1. 定案版本與檔案', '',
         '| 款式 | 定案封面 | 定案預覽 PDF | 頁數 | SHA-256 | 來源（已驗證預覽） |', '|---|---|---|---|---|---|']
    for k, B in D['books'].items():
        fp, s, c = B['final_preview'], B['source'], B['checks']
        o.append(f"| {BOOKS[k]['zh']} | {B['cover']}（{B['cover_desc']}；Owner 已接受） | `public/{fp['file']}` | {c['pages']} 面 | `{fp['sha256']}` | `public/{s['file']}`（commit `{s['commit'][:7]}`；sha256 `{s['sha256'][:16]}…`） |")
    o += ['', '定案預覽 PDF 是來源 PDF 的逐頁原樣複製，只換文件標題與主旨；頁面內容、圖片、字型、尺寸框逐頁比對與來源相同。', '',
          '## 2. 檔案檢查（已通過）', '', '| 項目 | 橫式 | 直式 |', '|---|---|---|']
    H, V = D['books']['H']['checks'], D['books']['V']['checks']
    rows = [
        ('頁數', f"{H['pages']} 面（應為 {H['pages_expected']}）", f"{V['pages']} 面（應為 {V['pages_expected']}）"),
        ('成品尺寸（裁切線）', f"{H['trim_mm'][0]}×{H['trim_mm'][1]} mm", f"{V['trim_mm'][0]}×{V['trim_mm'][1]} mm"),
        ('出血', f"四邊各 {H['bleed_mm_each_side']} mm（含出血 {H['canvas_mm'][0]}×{H['canvas_mm'][1]} mm）", f"四邊各 {V['bleed_mm_each_side']} mm（含出血 {V['canvas_mm'][0]}×{V['canvas_mm'][1]} mm）"),
        ('每頁尺寸框（MediaBox／TrimBox／BleedBox）', f"全部一致：{yn(H['media_ok'] and H['trim_ok'] and H['bleed_ok'])}", f"全部一致：{yn(V['media_ok'] and V['trim_ok'] and V['bleed_ok'])}"),
        ('頁面旋轉', '無（全部 0°）' if H['rotation'] == [0] else str(H['rotation']), '無（全部 0°）' if V['rotation'] == [0] else str(V['rotation'])),
        ('封面頁＝已接受版本', yn(H['cover_page_is_accepted_version']), yn(V['cover_page_is_accepted_version'])),
        ('內頁與 R26 已接受排版逐頁相同', yn(H['interior_same_as_r26_accepted']), yn(V['interior_same_as_r26_accepted'])),
        ('頁序', '面 1 封面；面 2–25 每月照片面→大格面；26–27 MEMO；28 條碼', '面 1 封面；面 2–25 每月照片面→大格面；26–30 MEMO；31 全年年曆；32 條碼'),
        ('字型', '全部嵌入（子集）：' + '、'.join(f['name'] for f in H['fonts']), '全部嵌入（子集）：' + '、'.join(f['name'] for f in V['fonts'])),
        ('照片框', f"{H['photo_frame_mm'][0]}×{H['photo_frame_mm'][1]} mm（完整 16:9）", f"{V['photo_frame_mm'][0]}×{V['photo_frame_mm'][1]} mm"),
        ('照片有效解析度', f"約 {H['photo_eff_ppi_from_r26'][0]:.0f} ppi（PDF 內 {H['images']['photo_ppi_min']}–{H['images']['photo_ppi_max']} ppi；未放大）",
         f"約 {V['photo_eff_ppi_from_r26'][0]:.0f}–{V['photo_eff_ppi_from_r26'][1]:.0f} ppi（PDF 內 {V['images']['photo_ppi_min']}–{V['images']['photo_ppi_max']} ppi；未放大）"),
        ('封面畫面解析度', f"{H['images']['cover_art_ppi'][0]} ppi（文字、Logo 為向量）", f"{V['images']['cover_art_ppi'][0]} ppi（文字、Logo 為向量）"),
        ('圖片色彩', '、'.join(H['images']['colors']) + f"（{'、'.join(H['images']['encodings'])}；無透明遮罩）", '、'.join(V['images']['colors']) + f"（{'、'.join(V['images']['encodings'])}；無透明遮罩）"),
        ('封面文字安全區', f"年份 {yn(H['cover_text_safe']['year_in_safe'])}、品牌區 {yn(H['cover_text_safe']['brand_in_safe'])} 在安全區內", f"年份 {yn(V['cover_text_safe']['year_in_safe'])}、品牌區 {yn(V['cover_text_safe']['brand_in_safe'])} 在安全區內"),
        ('PDF 版本／輸出意圖', f"{H['pdf_version']}；輸出意圖：{yn(H['output_intents'])}", f"{V['pdf_version']}；輸出意圖：{yn(V['output_intents'])}"),
    ]
    o += [f'| {a} | {b} | {c} |' for a, b, c in rows]
    o += ['', '說明：安全區與線圈區是本案工作假設（橫式文字安全區＝廠商編輯器安全框；直式廠商安全框為 0，本案自訂裁切線內 3 mm、上緣避開 12 mm），不是廠商書面規格。', '',
          '## 3. 廠商待確認（檔案檢查無法替代）', '']
    o += [f'- **{x["item"]}**：{x["detail"]}' for x in D['vendor_pending']]
    o += ['', '## 4. 打樣重點（沒有實際打樣，不判定印刷效果通過）', '']
    o += [f'- {x["book"]}｜{x["item"]}' for x in D['proof_focus']]
    o += ['', '## 5. 狀態', '', '- 封面：橫式 H-L1-R36L、直式 V-D2-R34B 都是 Owner 已接受（定案）；候選與歷史回饋保留在紀錄中。',
          '- 內頁與 24 張定案照片維持原樣。', '- 交印：未核准；待廠商確認規格、打樣，並由 Penny 另行核准。', '']
    return '\n'.join(o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.check:
        old = json.load(open(os.path.join(ROOT, DATA_REL), encoding='utf-8'))
        with tempfile.TemporaryDirectory() as tmp:
            D = build(os.path.join(tmp, 'pub'), os.path.join(tmp, 'd.json'), os.path.join(tmp, 'doc.md'))
            same = json.loads(json.dumps(D, ensure_ascii=False)) == old
            pub = os.path.join(ROOT, PUB_REL)
            diff = [x['path'] for x in D['files'] if not os.path.exists(os.path.join(pub, x['path'])) or sha256(open(os.path.join(pub, x['path']), 'rb').read()) != x['sha256']]
            extra = sorted(set(os.listdir(pub)) - {x['path'] for x in D['files']})
            doc_same = open(os.path.join(tmp, 'doc.md'), encoding='utf-8').read() == open(os.path.join(ROOT, DOC_REL), encoding='utf-8').read()
        ok = same and not diff and not extra and doc_same
        print(json.dumps({'check': 'PASS' if ok else 'FAIL', 'data_same': same, 'files': len(D['files']), 'diff': diff, 'extra': extra, 'doc_same': doc_same}, ensure_ascii=False))
        sys.exit(0 if ok else 1)
    D = build(os.path.join(ROOT, PUB_REL), os.path.join(ROOT, DATA_REL), os.path.join(ROOT, DOC_REL))
    print(json.dumps({k: {'final': v['final_preview'], 'checks': {kk: vv for kk, vv in v['checks'].items() if kk not in ('page_order', 'fonts')}} for k, v in D['books'].items()}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
