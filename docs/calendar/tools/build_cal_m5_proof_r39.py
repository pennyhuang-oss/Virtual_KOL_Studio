#!/usr/bin/env python3
"""TASK-CAL-001／M-5 R39 — 試印候選 PDF（尚未核准下單）。

來源：R37 定案預覽（docs/calendar/decision_site/public/cover37/，Owner 已接受；本工具不修改它）。
預覽標記的出處：build_cal_m5_layout.py 的 Page.marker()（role='marker'），每面右下一行
「版面預覽 R26｜非交印核准｜面 n／N」。R37 定案預覽是逐頁原樣複製，所以標記仍在。
本工具不重跑整套排版（會引入與定案無關的差異），而是在定案預覽 PDF 的內容流裡刪除
同一個文字物件（文字刪除，不加白色矩形、不動圖片與線條），並拿掉最後一面條碼佔位頁：
  橫式 28 面 → 試印候選 27 頁；直式 32 面 → 31 頁。
  印廠作品仍是 28／32 面，最後一面是印廠條碼頁（不上傳、保持空白）——產品並沒有少一面。

核對（全部要過才寫檔）：
  - 只少了標記文字：其餘文字逐字、逐位置、逐色、逐字型相同；殘留預覽字樣 0
  - 每頁圖片串流位元相同（照片原始像素不變）、頁框相同、字型全部嵌入
  - 200 dpi 渲染比對：變動像素全在標記範圍內
  - 頁序、封面、月份、星期、日期、紅字（人事總處 116 年辦公日曆）、全年年曆：直接讀 PDF 文字層核對

用法：
  python3 docs/calendar/tools/build_cal_m5_proof_r39.py           # 產出並寫紀錄
  python3 docs/calendar/tools/build_cal_m5_proof_r39.py --check   # 重建到暫存資料夾，sha256 必須與 repo 內相同
"""
import argparse
import calendar
import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile

import numpy as np
import pymupdf

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
SRC_DIR = os.path.join(CAL, 'decision_site', 'public', 'cover37')
OUT_DIR = os.path.join(CAL, 'proof_r39')
DATA = os.path.join(CAL, 'data', 'cal_m5_proof_r39.json')
DGPA = os.path.join(CAL, 'data', 'cal_r2_official_2027_dgpa.json')
MM = 25.4 / 72
FIXED_DATE = "D:20261106000000+08'00'"
WEEK = '日一二三四五六'
EN = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
MARKER = re.compile(r'^版面預覽 R26｜非交印核准｜面 (\d+)／(\d+)$')
PREVIEW_WORDS = re.compile(r'版面預覽|非交印|佔位|示意|R2\d|條碼頁|廠商固定')

BOOKS = {
    'H': dict(src='cal2027_H_final_preview.pdf', faces=28, cover='H-L1-R36L',
              src_sha='23b32c22c106119b4439a0da55d523bb8b275dbfe4e44bdad002a6115ba146d1',
              out='cal2027_H_R39_試印候選_尚未核准下單.pdf',
              title='2027 桌曆 橫式 試印候選 R39（封面 H-L1-R36L）— 尚未核准下單'),
    'V': dict(src='cal2027_V_final_preview.pdf', faces=32, cover='V-D2-R34B',
              src_sha='21f1b4faf1ed049d2820c09fb47baa399749106730ea71e2ff180e0b685271d6',
              out='cal2027_V_R39_試印候選_尚未核准下單.pdf',
              title='2027 桌曆 直式 試印候選 R39（封面 V-D2-R34B）— 尚未核准下單'),
}
SUBJECT = ('試印候選、尚未核准下單（TASK-CAL-001 M-5 R39）｜由 R37 定案預覽刪除「版面預覽 R26」標記文字並排除條碼佔位頁；'
           '印廠作品最後一面為印廠條碼頁（不上傳、保持空白）｜未打樣、未下單')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def spans(page):
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines', []):
            for s in line['spans']:
                if s['text'].strip():
                    yield s


def span_key(s):
    return (s['text'], tuple(round(v, 2) for v in s['bbox']), s['font'], round(s['size'], 3), s['color'])


def red(color):
    r, g, b = (color >> 16) & 255, (color >> 8) & 255, color & 255
    return r - g > 60


def boxes(page):
    return {k: [round(v, 3) for v in getattr(page, k)] for k in ('mediabox', 'cropbox', 'bleedbox', 'trimbox', 'artbox')}


def images(doc, pno):
    out = []
    for img in doc[pno].get_images(full=True):
        out.append(dict(w=img[2], h=img[3], cs=img[5], sha256=sha(doc.xref_stream_raw(img[0]))))
    return sorted(out, key=lambda x: x['sha256'])


# ---------- build ----------
def build(kind, out_dir):
    B = BOOKS[kind]
    src = os.path.join(SRC_DIR, B['src'])
    assert sha(open(src, 'rb').read()) == B['src_sha'], f'{kind}: 來源 sha256 不符'
    doc = pymupdf.open(src)
    assert len(doc) == B['faces']
    last = doc[-1].get_text()
    assert '最後一面＝條碼頁' in last and '預覽佔位' in last, f'{kind}: 最後一面不是條碼佔位頁'
    removed = []
    for pno in range(B['faces'] - 1):
        page = doc[pno]
        marks = [s for s in spans(page) if MARKER.match(s['text'])]
        others = [s for s in spans(page) if not MARKER.match(s['text'])]
        if pno == 0:
            assert not marks, '封面不應有標記'
            continue
        assert len(marks) == 1, f'{kind} 面 {pno + 1}: 標記 {len(marks)} 個'
        m = MARKER.match(marks[0]['text'])
        assert (int(m.group(1)), int(m.group(2))) == (pno + 1, B['faces']), f'{kind} 面 {pno + 1}: 標記面碼不符'
        rect = pymupdf.Rect(marks[0]['bbox']) + (-0.3, -0.3, 0.3, 0.3)
        clash = [s['text'] for s in others if pymupdf.Rect(s['bbox']).intersects(rect)]
        assert not clash, f'{kind} 面 {pno + 1}: 標記範圍內有其他文字 {clash}'
        page.add_redact_annot(rect, fill=False)   # 只刪文字；不畫任何矩形
        page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                              graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                              text=pymupdf.PDF_REDACT_TEXT_REMOVE)
        removed.append(dict(face=pno + 1, text=marks[0]['text'], size_pt=round(marks[0]['size'], 2),
                            bbox_mm=[round(v * MM, 2) for v in marks[0]['bbox']]))
    doc.delete_page(B['faces'] - 1)
    doc.set_metadata(dict(title=B['title'], subject=SUBJECT, author='Virtual KOL Studio',
                          keywords='proof candidate; not approved for order; preview markers removed; barcode placeholder page excluded',
                          creator='docs/calendar/tools/build_cal_m5_proof_r39.py', producer='cal2027 R39',
                          creationDate=FIXED_DATE, modDate=FIXED_DATE))
    out = os.path.join(out_dir, B['out'])
    doc.save(out, garbage=3, deflate=True, no_new_id=True)
    return out, removed


# ---------- checks ----------
def check_same_except_marker(kind, src, out):
    s, o = pymupdf.open(src), pymupdf.open(out)
    res = []
    for pno in range(len(o)):
        ps, po = s[pno], o[pno]
        assert boxes(ps) == boxes(po), f'{kind} 頁 {pno + 1}: 頁框不同'
        assert images(s, pno) == images(o, pno), f'{kind} 頁 {pno + 1}: 圖片不同'
        ks = [span_key(x) for x in spans(ps) if not MARKER.match(x['text'])]
        ko = [span_key(x) for x in spans(po)]
        assert ks == ko, f'{kind} 頁 {pno + 1}: 標記以外的文字不同'
        left = [x['text'] for x in spans(po) if PREVIEW_WORDS.search(x['text'])]
        assert not left, f'{kind} 頁 {pno + 1}: 仍有預覽字樣 {left}'
        assert not list(po.annots()), '不應留下註解'
        marks = [pymupdf.Rect(x['bbox']) + (-0.3, -0.3, 0.3, 0.3) for x in spans(ps) if MARKER.match(x['text'])]
        a = ps.get_pixmap(dpi=200, alpha=False)
        b = po.get_pixmap(dpi=200, alpha=False)
        A = np.frombuffer(a.samples, np.uint8).reshape(a.height, a.width, 3)
        Bm = np.frombuffer(b.samples, np.uint8).reshape(b.height, b.width, 3)
        diff = (A != Bm).any(axis=2)
        mask = np.zeros_like(diff)
        for r in marks:
            q = r * (200 / 72)
            mask[max(int(q.y0) - 1, 0):int(q.y1) + 2, max(int(q.x0) - 1, 0):int(q.x1) + 2] = True
        outside = int((diff & ~mask).sum())
        assert outside == 0, f'{kind} 頁 {pno + 1}: 標記範圍外有 {outside} 個像素改變'
        res.append(dict(page=pno + 1, marker_removed=len(marks), spans_kept=len(ko), images=len(images(o, pno)),
                        changed_px_200dpi=int(diff.sum()), changed_px_outside_marker=outside))
    fonts = sorted({(f[3], f[1]) for p in o for f in p.get_fonts()})
    assert all(ext in ('ttf', 'otf', 'cff', 'cid') and '+' in name for name, ext in fonts), f'{kind}: 字型未全部子集嵌入 {fonts}'
    return res, [f'{n} ({e})' for n, e in fonts]


def page_roles(kind, doc):
    roles = []
    for pno, page in enumerate(doc):
        t = page.get_text()
        if pno == 0:
            roles.append('cover')
        elif 'MEMO' in t:
            roles.append('memo')
        elif '全年年曆' in t:
            roles.append('year')
        else:
            ms = [i + 1 for i, n in enumerate(EN) if re.search(r'\b' + n + r'\b', t)]
            assert len(ms) == 1, f'{kind} 頁 {pno + 1}: 找不到唯一月份 {ms}'
            roles.append(('grid' if f'2027 年 {ms[0]} 月' in t else 'strip', ms[0]))
    want = ['cover'] + [r for m in range(1, 13) for r in (('strip', m), ('grid', m))]
    want += ['memo', 'memo'] if kind == 'H' else ['memo'] * 5 + ['year']
    assert roles == want, f'{kind}: 頁序不符 {roles}'
    return roles


def bands(items, key, gap=3.0):
    """依 key（pt）由小到大分群：相鄰差距大於 gap 就換一群（同一列的字因字形高度不同會有些微差）。"""
    out = []
    for s in sorted(items, key=key):
        if out and key(s) - key(out[-1][-1]) <= gap:
            out[-1].append(s)
        else:
            out.append([s])
    return out


def check_dates(kind, doc, off):
    """直接讀文字層：每個日期格的列、行、數字、紅黑與星期（週日起始）都要對。"""
    out = []
    for pno, page in enumerate(doc):
        ss = list(spans(page))
        wk = [s for s in ss if s['text'] in WEEK]
        # 日期數字（月份大字「01」…「12」另由位置／字級排除）
        dg = [s for s in ss if s['text'].isdigit() and 1 <= int(s['text']) <= 31 and not s['text'].startswith('0')]
        cx = lambda s: (s['bbox'][0] + s['bbox'][2]) / 2
        cy = lambda s: (s['bbox'][1] + s['bbox'][3]) / 2
        t = page.get_text()
        cells = fails = 0
        if pno == 0 or 'MEMO' in t:
            continue
        ms = [i + 1 for i, n in enumerate(EN) if re.search(r'\b' + n + r'\b', t)]
        is_strip = bool(ms) and len(wk) >= 28   # 全年年曆也有很多星期字，但沒有英文月份
        if is_strip:
            m = ms[0]
            n = calendar.monthrange(2027, m)[1]
            band = np.median([cy(s) for s in wk])
            wk = sorted([s for s in wk if abs(cy(s) - band) < 3], key=cx)
            wsize = float(np.median([x['size'] for x in wk]))
            ds = sorted([s for s in dg if 0 < cy(s) - band < 15 and s['size'] < 2 * wsize], key=cx)
            assert len(wk) == n and len(ds) == n, f'{kind} 頁 {pno + 1}: 日期條 {len(wk)}/{len(ds)}≠{n}'
            for i in range(n):
                d = i + 1
                dow = WEEK[(dt.date(2027, m, d).weekday() + 1) % 7]
                want = off[f'2027-{m:02d}-{d:02d}']
                ok = (ds[i]['text'] == str(d) and wk[i]['text'] == dow and abs(cx(ds[i]) - cx(wk[i])) < 1.5 / MM
                      and red(ds[i]['color']) == want and red(wk[i]['color']) == want)
                cells += 1
                fails += not ok
            out.append(dict(page=pno + 1, type='strip', months=[m], cells=cells, failures=fails))
            continue
        # 大格／全年：每 7 個同一列、依序「日…六」的星期字＝一個月的表頭
        heads = []
        for band in bands(wk, cy):
            run_ = []
            for s in sorted(band, key=cx):
                if WEEK.index(s['text']) == len(run_):
                    run_.append(s)
                    if len(run_) == 7:
                        heads.append(run_)
                        run_ = []
                else:
                    run_ = [s] if s['text'] == WEEK[0] else []
        titles = [s for s in ss if re.fullmatch(r'(\d{1,2}) 月', s['text'])]
        months_seen = []
        for h in heads:
            cxs = [cx(x) for x in h]
            cw = (cxs[-1] - cxs[0]) / 6
            hy = cy(h[0])
            if ms:
                m = ms[0]
            else:  # 全年年曆：表頭上方最近的「N 月」
                cand = [s for s in titles if cy(s) < hy and hy - cy(s) < 20 and cxs[0] - cw <= s['bbox'][0] <= cxs[0] + cw]
                m = int(re.match(r'\d+', min(cand, key=lambda s: hy - cy(s))['text']).group())
            months_seen.append(m)
            for k, x in enumerate(h):
                cells += 1
                fails += red(x['color']) != (k in (0, 6))
            other_heads = [cy(g[0]) for g in heads if g is not h and abs(cx(g[0]) - cxs[0]) < cw and cy(g[0]) > hy]
            ylim = min(other_heads) if other_heads else 1e9
            mine = [s for s in dg if cxs[0] - cw / 2 <= cx(s) <= cxs[-1] + cw / 2 and hy < cy(s) < ylim]
            got = {}
            for r, row in enumerate(bands(mine, cy)):
                for s in row:
                    k = int(np.argmin([abs(cx(s) - c) for c in cxs]))
                    assert (r, k) not in got, f'{kind} 頁 {pno + 1}: 同一格有兩個數字'
                    got[(r, k)] = s
            want = {}
            for r, wkrow in enumerate(calendar.Calendar(firstweekday=6).monthdayscalendar(2027, m)):
                for k, d in enumerate(wkrow):
                    if d:
                        want[(r, k)] = d
            for key in set(got) | set(want):
                cells += 1
                d = want.get(key)
                s = got.get(key)
                ok = d is not None and s is not None and s['text'] == str(d) and red(s['color']) == off[f'2027-{m:02d}-{d:02d}']
                fails += not ok
        out.append(dict(page=pno + 1, type='year' if not ms else 'grid', months=months_seen, cells=cells, failures=fails))
    return out


def run(out_dir):
    off = {d['date']: d['off'] for d in json.load(open(DGPA, encoding='utf-8'))['days']}
    assert len(off) == 365 and sum(off.values()) == 121
    result = {'note': '程式產生（docs/calendar/tools/build_cal_m5_proof_r39.py），請勿手改。試印候選、尚未核准下單。',
              'round': 'M-5 R39', 'books': {}}
    for kind in ('H', 'V'):
        B = BOOKS[kind]
        out, removed = build(kind, out_dir)
        src = os.path.join(SRC_DIR, B['src'])
        same, fonts = check_same_except_marker(kind, src, out)
        o = pymupdf.open(out)
        roles = page_roles(kind, o)
        dates = check_dates(kind, o, off)
        assert sum(d['failures'] for d in dates) == 0, f'{kind}: 日期核對失敗 {[d for d in dates if d["failures"]]}'
        s1 = images(pymupdf.open(src), 0)
        result['books'][kind] = dict(
            source=os.path.relpath(src, ROOT), source_sha256=B['src_sha'],
            output=os.path.relpath(out, ROOT) if out_dir == OUT_DIR else os.path.basename(out),
            output_sha256=sha(open(out, 'rb').read()), pages=len(o),
            vendor_faces=B['faces'], vendor_last_face='印廠條碼頁（不上傳、保持空白；產品仍為 %d 面）' % B['faces'],
            cover=B['cover'], cover_image_sha256=[x['sha256'] for x in s1],
            page_size_mm=[round(o[0].mediabox.width * MM, 2), round(o[0].mediabox.height * MM, 2)],
            trimbox_mm=[round(v * MM, 2) for v in o[0].trimbox], bleed_each_side_mm=2.0,
            markers_removed=len(removed), removed=removed, fonts=fonts,
            page_roles=[r if isinstance(r, str) else f'{r[0]}-{r[1]:02d}' for r in roles],
            date_check=dict(method='讀 PDF 文字層，依表頭位置定行、依列定週；期望值用 calendar（週日起始）與人事總處 116 年辦公日曆（365 天、放假 121 天）',
                            pages=len(dates), cells=sum(d['cells'] for d in dates), failures=0, per_page=dates),
            same_as_source_except_marker=same)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.check:
        rec = json.load(open(DATA, encoding='utf-8'))
        with tempfile.TemporaryDirectory() as td:
            r = run(td)
            for k in ('H', 'V'):
                got, want = r['books'][k]['output_sha256'], rec['books'][k]['output_sha256']
                assert got == want, f'{k}: 重建 sha256 {got} ≠ 紀錄 {want}'
                assert sha(open(os.path.join(ROOT, rec['books'][k]['output']), 'rb').read()) == want, f'{k}: repo 內檔案 sha256 不符'
        print('check PASS')
        return
    os.makedirs(OUT_DIR, exist_ok=True)
    r = run(OUT_DIR)
    json.dump(r, open(DATA, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, b in r['books'].items():
        print(k, b['pages'], '頁', b['output_sha256'], '標記移除', b['markers_removed'],
              '日期格', b['date_check']['cells'], '失敗 0')


if __name__ == '__main__':
    sys.exit(main())
