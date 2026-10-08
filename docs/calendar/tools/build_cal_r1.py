#!/usr/bin/env python3
"""TASK-CAL-001 / R1 — 選角板、縮圖總覽、裁切與有效解析度評估。

唯讀：只讀 repo 既有素材，不改任何原檔，不呼叫任何生成服務。
輸入：docs/calendar/data/cal_r1_casting.json（人寫的判斷）＋ repo 原檔
輸出：docs/calendar/img/、docs/calendar/sheets/、docs/calendar/data/cal_r1_*.json、docs/calendar/casting_board.html

用法（repo 根目錄）：python3 docs/calendar/tools/build_cal_r1.py
"""
import glob
import html
import itertools
import json
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
GH = 'https://github.com/pennyhuang-oss/Virtual_KOL_Studio/blob/main/'
CATALOG = 'https://kol-catalog-production.up.railway.app/p/{}.html'
COLLISION_MAX = 0.0220  # review/soul_training/RULING_collision_accepted.md 規則 C-1/C-2 的配對門檻

# 版面框（含 2 mm 出血的畫布尺寸，單位 mm）。
# 廠商查得的事實：出血 2 mm（兩款）；橫式安全邊上 10 mm；直式安全邊 0（但編輯器線圈示意約佔上緣 7.7–9.7 mm）。
# 以下框型、日期條高度、臉的目標位置都是「本輪假設」，不是廠商要求。
FRAMES = {
    'H_full':  {'w': 204, 'h': 155, 'coil': 12, 'strip': 30, 'fy': 0.36, 'src': 'H', 'label': '橫式滿版（假設日期條 30 mm）'},
    'H_split': {'w': 102, 'h': 155, 'coil': 12, 'strip': 0,  'fy': 0.30, 'src': 'H', 'label': '橫式半版直幅照片框（另一半放日期）'},
    'V_full':  {'w': 144, 'h': 204, 'coil': 12, 'strip': 34, 'fy': 0.28, 'src': 'V', 'label': '直式滿版（假設日期條 34 mm）'},
}
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'


def font(size):
    try:
        return ImageFont.truetype(FONT, size)
    except OSError:
        return ImageFont.load_default()


def id7(text):
    """與 catalog/tools/build_assets.mjs 相同的 djb2，讓素材 ID 能對回型錄衍生檔 g_<id7>.jpg。"""
    h = 5381
    for c in text:
        h = ((h * 33) ^ ord(c)) & 0xFFFFFFFF
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    s = ''
    while h:
        s = digits[h % 36] + s
        h //= 36
    return (s or '0').rjust(7, '0')


def rel(p):
    return os.path.relpath(p, CAL).replace(os.sep, '/')


def find_souls(o):
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'soul_id' and isinstance(v, str):
                out.append({'soul_id': v, 'status': o.get('status')})
            else:
                out += find_souls(v)
    elif isinstance(o, list):
        for v in o:
            out += find_souls(v)
    return out


def ppi_band(p):
    # 本專案的工作判準（不是廠商要求）：≥300 充裕、250–299 可、200–249 邊緣、<200 不足。
    return '充裕' if p >= 300 else '可' if p >= 250 else '邊緣' if p >= 200 else '不足'


def crop_for(img_size, anchor, F):
    W, H = img_size
    cx, cy = anchor
    a = F['w'] / F['h']
    if W / H > a:
        ch, cw = H, round(H * a)
        x0 = min(max(round(cx * W - cw / 2), 0), W - cw)
        y0 = 0
    else:
        cw, ch = W, round(W / a)
        x0 = 0
        y0 = min(max(round(cy * H - F['fy'] * ch), 0), H - ch)
    return x0, y0, cw, ch


def preview(im, box, F, out, label, overlay=True, width=420):
    x0, y0, cw, ch = box
    pv = im.crop((x0, y0, x0 + cw, y0 + ch))
    pv.thumbnail((width, width))
    if overlay:
        pw, ph = pv.size
        k = ph / F['h']
        ov = Image.new('RGBA', pv.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(ov)
        d.rectangle((0, 0, pw, F['coil'] * k), fill=(255, 0, 0, 90))
        if F['strip']:
            d.rectangle((0, ph - F['strip'] * k, pw, ph), fill=(0, 90, 255, 90))
        d.rectangle((2 * k, 2 * k, pw - 2 * k, ph - 2 * k), outline=(255, 255, 255, 220), width=1)
        pv = Image.alpha_composite(pv.convert('RGBA'), ov).convert('RGB')
        dd = ImageDraw.Draw(pv)
        dd.rectangle((0, ph - 24, pw, ph), fill='black')
        dd.text((4, ph - 23), label, fill='yellow', font=font(17))
    pv.save(out, quality=84)


def main():
    data = json.load(open(os.path.join(CAL, 'data', 'cal_r1_casting.json')))
    cat = {p['id']: p for p in json.load(open(os.path.join(ROOT, 'catalog/data/catalog.json')))['personas']}
    souls_b3 = json.load(open(os.path.join(ROOT, 'review/soul_training/SOUL_IDS.json')))
    pairs = json.load(open(os.path.join(ROOT, 'review/soul_pilot/_screen19_v1/screen19_pairs.json')))
    dist = {frozenset((p['a'], p['b'])): p['d'] for p in pairs}
    screened = {p['a'] for p in pairs} | {p['b'] for p in pairs}

    for sub in ('img/cand', 'img/crop', 'sheets'):
        os.makedirs(os.path.join(CAL, sub), exist_ok=True)

    leads = [c for c in data['candidates'] if c['role'] == 'lead']
    lead_ids = [c['id'] for c in leads]
    out_cands, crop_report = [], {}

    for c in data['candidates']:
        pid = c['id']
        prof = json.load(open(os.path.join(ROOT, f'kols/{pid}/profile.json')))
        idn = prof.get('identity', {})
        souls = find_souls(prof)
        live = [s for s in souls if s['status'] != 'deprecated']
        sj = souls_b3.get(pid, {}).get('soul_id')
        soul = {
            'profile_ids': souls,
            'source': f'kols/{pid}/profile.json',
            'cross_check': ('SOUL_IDS.json 一致' if sj and any(s['soul_id'] == sj for s in live)
                            else 'SOUL_IDS.json 不一致' if sj else 'SOUL_IDS.json 未收錄（只有 Batch 3）'),
            'platform_checked': False,
        }
        coll = None
        if pid in screened:
            near = sorted((dist[frozenset((pid, o))], o) for o in screened if o != pid)
            hits = [(o, d) for d, o in near if d <= COLLISION_MAX]
            with_leads = [(o, d) for d, o in near if o in lead_ids and d <= COLLISION_MAX]
            coll = {'nearest': [near[0][1], near[0][0]], 'hits_le_0220': len(hits),
                    'hits_with_leads': with_leads}

        if c['role'] in ('lead', 'backup'):
            paths = [c['V']['path'], c['H']['path']] + c.get('extra', [])
        else:
            paths = c['imgs']
        imgs = []
        for n, p in enumerate(paths[:3], 1):
            full = os.path.join(ROOT, p)
            with Image.open(full) as im:
                W, H = im.size
                t = im.convert('RGB')
                t.thumbnail((560, 560))
                tname = f'img/cand/{pid}_{n}.jpg'
                t.save(os.path.join(CAL, tname), quality=82)
            k = id7('Virtual_KOL_Studio/' + p)
            in_catalog = os.path.exists(os.path.join(ROOT, f'catalog/assets/{pid}/g_{k}.jpg'))
            imgs.append({'asset_id': f'A-{k}', 'path': p, 'px': [W, H], 'thumb': tname,
                         'catalog_asset': f'g_{k}' if in_catalog else None, 'original_url': GH + p})

        rec = {k: v for k, v in c.items() if k not in ('imgs',)}
        rec.update({'name': idn.get('name'), 'native_name': idn.get('native_name'), 'age': idn.get('age'),
                    'ethnicity_src': idn.get('ethnicity'), 'origin_src': idn.get('origin'),
                    'asian_evidence': f"kols/{pid}/profile.json identity.ethnicity=「{idn.get('ethnicity')}」/ origin=「{idn.get('origin')}」",
                    'catalog_url': CATALOG.format(pid) if pid in cat else None,
                    'soul': soul, 'collision': coll, 'images': imgs})

        if c['role'] in ('lead', 'backup'):
            crop_report[pid] = {}
            for fname, F in FRAMES.items():
                slot = c[F['src']]
                full = os.path.join(ROOT, slot['path'])
                with Image.open(full) as im0:
                    im = im0.convert('RGB')
                W, H = im.size
                box = crop_for((W, H), slot['anchor'], F)
                x0, y0, cw, ch = box
                ppi = cw / (F['w'] / 25.4)
                face_y = (slot['anchor'][1] * H - y0) / ch * F['h']
                pv = f'img/crop/{pid}_{fname}.jpg'
                preview(im, box, F, os.path.join(CAL, pv), f'{fname} {ppi:.0f}ppi')
                clean = f'img/crop/{pid}_{fname}_clean.jpg'
                preview(im, box, F, os.path.join(CAL, clean), '', overlay=False, width=360)
                crop_report[pid][fname] = {
                    'src': slot['path'], 'src_px': [W, H], 'src_aspect': round(W / H, 4),
                    'frame_mm': [F['w'], F['h']], 'frame_aspect': round(F['w'] / F['h'], 4),
                    'crop_box_px': [x0, y0, cw, ch], 'keeps_pct_of_source': round(cw * ch / (W * H) * 100),
                    'effective_ppi': round(ppi), 'ppi_band': ppi_band(ppi),
                    'face_center_y_mm': round(face_y, 1),
                    'face_clear_of_coil_and_strip': F['coil'] + 8 < face_y < F['h'] - F['strip'] - 8,
                    'preview': pv, 'verdict_slot': slot['verdict'] if fname != 'H_full' else '不採用（現有直幅原圖）',
                }
        out_cands.append(rec)

    # 主角之間的碰撞（只有 Batch 3 有量測）
    b3_leads = [i for i in lead_ids if i in screened]
    lead_pairs = sorted((dist[frozenset(x)], x) for x in itertools.combinations(b3_leads, 2))

    json.dump({'generated_by': 'docs/calendar/tools/build_cal_r1.py', 'frames_assumed': FRAMES,
               'ppi_bands_assumed': '≥300 充裕｜250–299 可｜200–249 邊緣｜<200 不足（本專案工作判準，非廠商要求）',
               'results': crop_report},
              open(os.path.join(CAL, 'data', 'cal_r1_crop_report.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump({'generated_by': 'docs/calendar/tools/build_cal_r1.py', 'collision_threshold': COLLISION_MAX,
               'batch3_lead_pairs_min': [{'a': x[0], 'b': x[1], 'd': d} for d, x in lead_pairs[:5]],
               'candidates': out_cands, 'excluded_before_shortlist': data['excluded_before_shortlist']},
              open(os.path.join(CAL, 'data', 'cal_r1_candidates.json'), 'w'), ensure_ascii=False, indent=1)

    by_id = {c['id']: c for c in out_cands}
    month_order = sorted(leads, key=lambda c: c['month'])
    build_sheets(by_id, month_order, data)
    build_html(by_id, month_order, data, crop_report, lead_pairs)
    build_table_md(by_id, month_order, data, crop_report)
    build_candidates_md(by_id, data, lead_pairs)
    print('ok', len(out_cands), 'candidates;', len(crop_report), 'crop sets; lead pair min', lead_pairs[0])


def build_sheets(by_id, month_order, data):
    f, fs = font(24), font(18)
    # 1) 12 位主角同版面總覽（月份順序）：上排直式滿版裁切、下排橫式半版裁切，都不加遮罩
    cols, cw = 6, 372
    cells = []
    for c in month_order:
        pid = c['id']
        v = Image.open(os.path.join(CAL, f'img/crop/{pid}_V_full_clean.jpg'))
        h = Image.open(os.path.join(CAL, f'img/crop/{pid}_H_split_clean.jpg'))
        v.thumbnail((cw - 8, 500))
        h.thumbnail((cw - 8, 500))
        cell = Image.new('RGB', (cw, 46 + v.height + 6 + h.height + 8), 'white')
        d = ImageDraw.Draw(cell)
        d.text((6, 8), f"{c['month']:>2}月  {by_id[pid]['name']} {by_id[pid]['native_name'] or ''}", fill='black', font=f)
        cell.paste(v, (4, 46))
        cell.paste(h, (4, 46 + v.height + 6))
        cells.append(cell)
    rows = [cells[i:i + cols] for i in range(0, len(cells), cols)]
    H = sum(max(c.height for c in r) + 8 for r in rows) + 60
    S = Image.new('RGB', (cols * cw, H), '#d9d9d9')
    d = ImageDraw.Draw(S)
    d.text((10, 14), 'TASK-CAL-001 R1｜12 位主角暫定總覽（每格上：直式候選／下：橫式半版候選）｜建議稿，未拍板', fill='black', font=f)
    y = 60
    for r in rows:
        for i, c in enumerate(r):
            S.paste(c, (i * cw, y))
        y += max(c.height for c in r) + 8
    S.save(os.path.join(CAL, 'sheets/CAL_R1_overview_12.jpg'), quality=85)

    # 2) 18 位候選比較（每位 3 張既有圖）
    rows = []
    for c in data['candidates']:
        rec = by_id[c['id']]
        tag = {'lead': f"主角 {c.get('month', '')}月", 'backup': '備選', 'out': '落選'}[c['role']]
        ims = [Image.open(os.path.join(CAL, i['thumb'])) for i in rec['images']]
        for im in ims:
            im.thumbnail((300, 300))
        row = Image.new('RGB', (330 + 3 * 306, 306), 'white')
        d = ImageDraw.Draw(row)
        d.text((8, 10), rec['name'] or c['id'], fill='black', font=f)
        d.text((8, 42), rec['native_name'] or '', fill='black', font=fs)
        d.text((8, 70), f"{rec['age']} 歲｜{rec['ethnicity_src']}", fill='#333', font=fs)
        d.text((8, 98), tag, fill='#b00' if c['role'] == 'lead' else '#06c' if c['role'] == 'backup' else '#777', font=f)
        for n, (im, meta) in enumerate(zip(ims, rec['images'])):
            row.paste(im, (330 + n * 306, 3))
            d.rectangle((330 + n * 306, 280, 330 + n * 306 + 140, 303), fill='black')
            d.text((334 + n * 306, 281), meta['asset_id'], fill='yellow', font=fs)
        rows.append(row)
    S = Image.new('RGB', (rows[0].width, sum(r.height + 4 for r in rows)), '#999')
    y = 0
    for r in rows:
        S.paste(r, (0, y))
        y += r.height + 4
    S.save(os.path.join(CAL, 'sheets/CAL_R1_candidates_18.jpg'), quality=82)

    # 3) 裁切預覽（紅＝線圈區、藍＝假設日期條、白框＝裁切線）
    rows = []
    for c in month_order + [x for x in data['candidates'] if x['role'] == 'backup']:
        pid = c['id']
        ims = [Image.open(os.path.join(CAL, f'img/crop/{pid}_{fr}.jpg')) for fr in FRAMES]
        row = Image.new('RGB', (230 + sum(i.width + 6 for i in ims), max(i.height for i in ims) + 4), 'white')
        d = ImageDraw.Draw(row)
        d.text((6, 8), by_id[pid]['name'], fill='black', font=f)
        d.text((6, 40), f"{c.get('month', '備選')}{'月' if c.get('month') else ''}", fill='#b00', font=fs)
        x = 230
        for im in ims:
            row.paste(im, (x, 2))
            x += im.width + 6
        rows.append(row)
    W = max(r.width for r in rows)
    S = Image.new('RGB', (W, sum(r.height + 4 for r in rows)), '#888')
    y = 0
    for r in rows:
        S.paste(r, (0, y))
        y += r.height + 4
    S.save(os.path.join(CAL, 'sheets/CAL_R1_crops_12.jpg'), quality=80)


def build_table_md(by_id, month_order, data, crop_report):
    """CAL_03b：每位主角的橫直式候選圖、尺寸、有效 ppi、瑕疵、判定，以及計數。全部現算，不要手改。"""
    L = ['# CAL_03b — 主視覺候選圖逐張判定（程式產生，請勿手改）', '',
         '> 由 `docs/calendar/tools/build_cal_r1.py` 產生。判定與瑕疵文字來自 `data/cal_r1_casting.json`（人寫）；',
         '> 像素、長寬比、有效 ppi、裁切保留比例由程式從原檔現算。框尺寸與 ppi 分級是本輪假設，不是廠商要求。', '',
         '| 月 | 人設 | 版面 | 原圖（repo 路徑） | 原圖 px | 長寬比 | 原圖/縮圖 | 框 mm | 有效 ppi | 裁切保留 | 判定 | 瑕疵與裁切備註 |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|']
    counts = {'H': {}, 'V': {}}
    distinct = {'H': set(), 'V': set()}
    for c in month_order + [x for x in data['candidates'] if x['role'] == 'backup']:
        pid = c['id']
        for fname, slot in (('H_split', 'H'), ('V_full', 'V')):
            r = crop_report[pid][fname]
            v = c[slot]['verdict']
            if c['role'] == 'lead':
                counts[slot][v] = counts[slot].get(v, 0) + 1
                distinct[slot].add(r['src'])
            L.append(f"| {c.get('month', '備')} | {by_id[pid]['name']} | {'橫式半版' if slot == 'H' else '直式滿版'} | `{r['src']}` | "
                     f"{r['src_px'][0]}×{r['src_px'][1]} | {r['src_aspect']} | 原圖 | {r['frame_mm'][0]}×{r['frame_mm'][1]} | "
                     f"{r['effective_ppi']}（{r['ppi_band']}） | {r['keeps_pct_of_source']}% | {v} | {c[slot]['defects']} |")
    L += ['', '## 橫式滿版（204×155）若直接用上表的直幅原圖', '',
          '| 月 | 人設 | 有效 ppi | 裁切保留 | 結論 |', '|---|---|---|---|---|']
    for c in month_order:
        r = crop_report[c['id']]['H_full']
        L.append(f"| {c['month']} | {by_id[c['id']]['name']} | {r['effective_ppi']}（{r['ppi_band']}） | {r['keeps_pct_of_source']}% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |")
    shared = distinct['H'] & distinct['V']
    L += ['', '## 計數（只算 12 位主角）', '',
          f"- 橫式（半版）判定：{json.dumps(counts['H'], ensure_ascii=False)}",
          f"- 直式（滿版）判定：{json.dumps(counts['V'], ensure_ascii=False)}",
          f"- 不同原圖數：橫式 {len(distinct['H'])}、直式 {len(distinct['V'])}、兩款共用 {len(shared)}、合計 {len(distinct['H'] | distinct['V'])}",
          '- 版面使用次數：橫式 12、直式 12（每月一個主視覺；封面與其他頁另計）',
          f"- 需新生成（主視覺）：橫式 {counts['H'].get('需補生成', 0)}、直式 {counts['V'].get('需補生成', 0)}"
          '（若改用橫式滿版，另需 12 張原生橫幅或外擴圖）', '']
    open(os.path.join(CAL, 'CAL_03b_PRINT_TABLE.generated.md'), 'w').write('\n'.join(L))


def build_candidates_md(by_id, data, lead_pairs):
    """CAL_02b：18 位候選的客觀欄位（程式從 profile.json／SOUL_IDS.json／碰撞表現抓）。"""
    L = ['# CAL_02b — 18 位候選客觀欄位（程式產生，請勿手改）', '',
         '> 由 `docs/calendar/tools/build_cal_r1.py` 從 `kols/{id}/profile.json`、`review/soul_training/SOUL_IDS.json`、',
         '> `review/soul_pilot/_screen19_v1/screen19_pairs.json` 現抓。Soul ID 只核對 repo 紀錄，**沒有**在 Higgsfield 端查驗。', '',
         '| 角色 | 角色 ID | 姓名 | 設定年齡 | 亞洲背景依據（profile.json 原文） | 型錄頁 | Soul ID（狀態） | Soul 交叉核對 | 臉部碰撞（≤0.0220） |',
         '|---|---|---|---|---|---|---|---|---|']
    role_zh = {'lead': '主角', 'backup': '備選', 'out': '落選'}
    for c in data['candidates']:
        r = by_id[c['id']]
        souls = '<br>'.join(f"`{s['soul_id']}`（{s['status']}）" for s in r['soul']['profile_ids']) or '未確認'
        coll = r['collision']
        cs = (f"最近 {coll['nearest'][0]} {coll['nearest'][1]:.5f}；共 {coll['hits_le_0220']} 組；與主角："
              + ('、'.join(f'{o} {d:.5f}' for o, d in coll['hits_with_leads']) or '無')) if coll else '未量測（非 Batch 3 的 19 位）'
        role = role_zh[c['role']] + (f" {c['month']}月" if c.get('month') else '')
        L.append(f"| {role} | `{c['id']}` | {r['name']} {r['native_name'] or ''} | {r['age']} | ethnicity「{r['ethnicity_src']}」／origin「{r['origin_src']}」 | "
                 f"[連結]({r['catalog_url']}) | {souls} | {r['soul']['cross_check']} | {cs} |")
    L += ['', f"Batch 3 主角之間最近的三組：" + '；'.join(f'{x[0]}↔{x[1]} {d:.5f}' for d, x in lead_pairs[:3]) + '（全部 > 0.0220）。', '']
    open(os.path.join(CAL, 'CAL_02b_CANDIDATES.generated.md'), 'w').write('\n'.join(L))


def esc(s):
    return html.escape(str(s if s is not None else ''))


def build_html(by_id, month_order, data, crop_report, lead_pairs):
    css = """
:root{--bg:#f6f5f3;--fg:#1d1d1f;--mut:#666;--card:#fff;--line:#ddd;--lead:#b3261e;--bak:#0b62c4;--out:#777}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#17181a;--fg:#ececec;--mut:#aaa;--card:#222326;--line:#3a3a3a}}
:root[data-theme=dark]{--bg:#17181a;--fg:#ececec;--mut:#aaa;--card:#222326;--line:#3a3a3a}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,"PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif}
main{max-width:1280px;margin:0 auto;padding:16px}
h1{font-size:22px;margin:8px 0}h2{font-size:18px;margin:28px 0 8px;border-bottom:2px solid var(--line);padding-bottom:4px}
.note{color:var(--mut);font-size:13px}.warn{background:#fff3cd;color:#5c4700;padding:8px 12px;border-radius:6px;font-size:14px}
.grid12{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}
.m{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:6px}
.m img{width:100%;display:block;border-radius:4px}.m b{display:block;font-size:14px;margin:4px 0}
.cand{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px;margin:12px 0}
.cand h3{margin:0 0 6px;font-size:17px}.tag{display:inline-block;font-size:12px;color:#fff;border-radius:4px;padding:1px 6px;margin-left:6px}
.lead{background:var(--lead)}.backup{background:var(--bak)}.out{background:var(--out)}
.imgs{display:flex;gap:8px;flex-wrap:wrap}.imgs figure{margin:0;width:200px}.imgs img{width:200px;border-radius:4px;display:block}
figcaption{font-size:11.5px;color:var(--mut);word-break:break-all}
dl{display:grid;grid-template-columns:110px 1fr;gap:2px 10px;margin:8px 0;font-size:13.5px}dt{color:var(--mut)}dd{margin:0;min-width:0;overflow-wrap:anywhere}
table{border-collapse:collapse;width:100%;font-size:13px;background:var(--card)}th,td{border:1px solid var(--line);padding:4px 6px;text-align:left;vertical-align:top}
.crops{display:flex;gap:6px;flex-wrap:wrap}.crops img{height:220px;border-radius:3px}
a{color:inherit}.tw{overflow-x:auto;max-width:100%}img{max-width:100%}
@media (max-width:600px){.imgs figure,.imgs img{width:100%}dl{grid-template-columns:90px 1fr}.crops img{height:160px}}
"""
    h = ['<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>2027 桌曆選角板</title>', f'<style>{css}</style></head><body><main>',
         '<h1>2027 KOL 雙款桌曆｜選角板 R1</h1>',
         '<p class="warn">建議稿，未經 Penny 拍板。本輪沒有生成任何圖片、沒有花 credits、沒有下單或聯絡廠商。所有圖片都是 repo 內既有原檔的縮圖。</p>',
         '<p class="note">素材 ID = A-＋型錄同一套 djb2 雜湊（對得上型錄衍生檔 g_xxxxxxx）。「原圖」連到 GitHub 上的原檔（需 repo 權限）。'
         '碰撞距離出自 review/soul_pilot/_screen19_v1/screen19_pairs.json（只量過 Batch 3 的 19 位，門檻 ≤0.0220）。</p>']

    h.append('<h2>一、12 位主角同版面總覽（暫定月份順序）</h2><p class="note">每格上：直式滿版裁切；下：橫式半版裁切。裁切框為本輪假設，見下方第三節。</p><div class="grid12">')
    for c in month_order:
        r = by_id[c['id']]
        h.append(f'<div class="m"><b>{c["month"]} 月｜{esc(r["name"])} {esc(r["native_name"])}</b>'
                 f'<img src="img/crop/{c["id"]}_V_full_clean.jpg" alt="{esc(r["name"])} 直式"><img style="margin-top:4px" src="img/crop/{c["id"]}_H_split_clean.jpg" alt="{esc(r["name"])} 橫式"></div>')
    h.append('</div>')

    h.append('<h2>二、候選比較（18 位：12 主角＋2 備選＋4 主要落選）</h2>')
    for c in data['candidates']:
        r = by_id[c['id']]
        role = {'lead': ('主角', 'lead'), 'backup': ('備選', 'backup'), 'out': ('落選', 'out')}[c['role']]
        extra = f'｜{c["month"]} 月' if c.get('month') else (f'｜可替：{esc(c.get("replaces"))}' if c.get('replaces') else '')
        h.append(f'<section class="cand" id="{c["id"]}"><h3>{esc(r["name"])} {esc(r["native_name"])}<span class="tag {role[1]}">{role[0]}</span>{extra}</h3><div class="imgs">')
        for i in r['images']:
            cat = f'；型錄同圖 {i["catalog_asset"]}' if i['catalog_asset'] else ''
            h.append(f'<figure><img loading="lazy" src="{i["thumb"]}" alt="{esc(i["asset_id"])}"><figcaption><b>{i["asset_id"]}</b> {i["px"][0]}×{i["px"][1]}{cat}<br>{esc(i["path"])}<br><a href="{i["original_url"]}">原圖</a></figcaption></figure>')
        h.append('</div><dl>')
        souls = '、'.join(f'{s["soul_id"]}（{s["status"]}）' for s in r['soul']['profile_ids']) or '未確認'
        coll = r['collision']
        coll_s = (f'最近 {coll["nearest"][0]} {coll["nearest"][1]:.5f}；≤0.0220 共 {coll["hits_le_0220"]} 組；與主角碰撞 {coll["hits_with_leads"] or "無"}'
                  if coll else '未量測（不在 Batch 3 的 19 位篩檢內）')
        for k, v in [('角色 ID', c['id']), ('設定年齡', r['age']), ('亞洲背景依據', r['asian_evidence']),
                     ('型錄頁', f'<a href="{r["catalog_url"]}">{r["catalog_url"]}</a>' if r['catalog_url'] else '—'),
                     ('Soul ID', f'{esc(souls)}<br><span class="note">來源 {r["soul"]["source"]}；{r["soul"]["cross_check"]}；未在 Higgsfield 端查驗</span>'),
                     ('臉部碰撞', esc(coll_s)), ('推薦理由', esc(c['why'])), ('具體缺點', esc(c['cons'])), ('與他人差異', esc(c['diff']))]:
            h.append(f'<dt>{k}</dt><dd>{v if k in ("型錄頁", "Soul ID") else esc(v)}</dd>')
        if c['role'] in ('lead', 'backup'):
            for s in ('H', 'V'):
                h.append(f'<dt>{"橫式" if s == "H" else "直式"}候選判定</dt><dd>{esc(c[s]["verdict"])}：{esc(c[s]["defects"])}</dd>')
        for rj in c.get('rejected', []):
            h.append(f'<dt>已剔除圖</dt><dd>{esc(rj["path"])}：{esc(rj["why"])}</dd>')
        h.append('</dl></section>')

    h.append('<h2>三、裁切與有效印刷解析度（12 主角＋2 備選）</h2>'
             '<p class="note">紅＝線圈區（上緣 12 mm 畫布，含 2 mm 出血）；藍＝假設的日期條；白框＝裁切線（出血內縮 2 mm）。'
             'ppi = 裁切後實際像素 ÷ 框寬英吋，沒有任何放大。分級是本專案的工作判準，不是廠商要求。</p>'
             '<div class="tw"><table><tr><th>月</th><th>人設</th><th>橫式滿版 204×155</th><th>橫式半版 102×155</th><th>直式滿版 144×204</th><th>預覽</th></tr>')
    for c in month_order + [x for x in data['candidates'] if x['role'] == 'backup']:
        cr = crop_report[c['id']]
        cell = lambda k: f'{cr[k]["effective_ppi"]} ppi（{cr[k]["ppi_band"]}）<br>{cr[k]["src_px"][0]}×{cr[k]["src_px"][1]}<br>{esc(cr[k]["verdict_slot"])}'
        h.append(f'<tr><td>{c.get("month", "備")}</td><td>{esc(by_id[c["id"]]["name"])}</td><td>{cell("H_full")}</td><td>{cell("H_split")}</td><td>{cell("V_full")}</td>'
                 f'<td><div class="crops">' + ''.join(f'<img loading="lazy" src="img/crop/{c["id"]}_{k}.jpg" alt="{k}">' for k in FRAMES) + '</div></td></tr>')
    h.append('</table></div>')

    h.append('<h2>四、篩選前即排除</h2><div class="tw"><table><tr><th>人設</th><th>原因</th></tr>')
    for e in data['excluded_before_shortlist']:
        h.append(f'<tr><td>{esc("、".join(e["ids"]))}</td><td>{esc(e["why"])}</td></tr>')
    h.append('</table></div>')
    lp = '；'.join(f'{x[0]}↔{x[1]} {d:.5f}' for d, x in lead_pairs[:3])
    h.append(f'<p class="note">主角中屬 Batch 3 者的最近配對：{esc(lp)}（皆 &gt; 0.0220）。原 11 位與 Batch 3 之間沒有量測，臉部差異以目視判斷。</p>')
    h.append('</main></body></html>')
    open(os.path.join(CAL, 'casting_board.html'), 'w').write('\n'.join(h))


if __name__ == '__main__':
    main()
