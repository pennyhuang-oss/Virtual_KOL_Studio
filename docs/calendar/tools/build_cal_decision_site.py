#!/usr/bin/env python3
"""TASK-CAL-001 — 2027 KOL 桌曆決策頁的素材與資料。

所有圖片一律從固定成果 commit（FIXED，git show）或可核對 sha256 的本機快取讀取，不讀工作目錄、不讀分支頭；
資料也從固定 commit 讀，只有第二階段的兩份人寫清單（cal_m1_*.json，本輪新增）從工作目錄讀，並在頁面資料記錄其 git blob。
- 整張複製：位元組不變，manifest 記錄來源路徑與 git blob。
- 裁切：從固定 commit 的決策拼圖裁出單張照片（只裁切、四邊內縮 2 px 避開拼貼邊界，重新存成 JPEG q95），manifest 記錄裁切框。
- 縮圖：上面兩者的等比縮小（Lanczos，JPEG q82），只給卡片顯示；點開放大一律看原檔或裁切檔。
- 高解析預覽（替代照片）：來源只限可核對的既有檔——固定 commit 的 repo 檔（git blob）、R2 已取回的 Higgsfield 快取
  （data/cal_r2_hf_retrieved.json 的 sha256）、R3 清理輸出（data/cal_r3_cleanup_report.json 的 clean_sha256）。
  只做等比縮小（長邊 1600 px，JPEG q88，不帶原檔中繼資料）。頁面資料只放圖片 ID，不放 job_id、來源路徑或帳號資料。
- 第二階段素材（data/cal_m1_materials.json，本輪人寫清單，從工作目錄讀）：每張照片用同一套來源核對後等比縮小；
  沒有取回原圖的 daily140 照片只複製 repo 的 360×480 縮圖（位元組不變）。名單只依 data/cal_m1_owner_roster.json。
- M-3 拍攝企劃（data/cal_m3_shoot_plan.json，R2 起為 24 套雙款，R3 起每套附攝影設計，R4 起附印刷構圖判斷，M-4 R1 起 M-3 完成（23 套已接受＋H-Luna 主管覆核通過）並附 V-Iris 首試準備與首試前核查，人寫，從工作目錄讀）：企劃文字照搬；Aaliya 參考照片從固定 commit 讀檔後等比縮小，
  其餘參考圖沿用第二階段素材的預覽。企劃資料不含 Soul ID 或 job_id；新企劃沒有任何生成圖。
不生成、不外擴、不增強、不修圖、不重新下載。

輸出：docs/calendar/decision_site/public/img/{z,t}/、public/data.js、decision_site/ASSET_MANIFEST.json
用法：python3 docs/calendar/tools/build_cal_decision_site.py --hf-dir <取回快取> --clean-dir <R3 清理輸出>   # 產生
      python3 docs/calendar/tools/build_cal_decision_site.py --check [--hf-dir ... --clean-dir ...]  # 核對
"""
import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys

import numpy as np
from PIL import Image

FIXED = '4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45'
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SITE = os.path.join(ROOT, 'docs', 'calendar', 'decision_site')
PUB = os.path.join(SITE, 'public')
CAL = 'docs/calendar/'


def git_bytes(rel):
    return subprocess.check_output(['git', '-C', ROOT, 'show', f'{FIXED}:{CAL}{rel}'])


def git_blob(rel):
    return subprocess.check_output(['git', '-C', ROOT, 'rev-parse', f'{FIXED}:{CAL}{rel}'], text=True).strip()


def blob_of(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def jpeg(im, q):
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=q, optimize=True)
    return b.getvalue()


# ---------- 拼圖裁切（版面規則見 build_cal_r3_decisions.py 的 tile/row/sheet） ----------

def runs(mask):
    out, start = [], None
    for i, v in enumerate(mask):
        if v and start is None:
            start = i
        if not v and start is not None:
            out.append((start, i))
            start = None
    if start is not None:
        out.append((start, len(mask)))
    return out


def sheet_rows(a):
    col = a[:, 255, :].astype(int)
    return [r for r in runs(np.abs(col - 233).max(axis=1) <= 6) if r[1] - r[0] > 50]


def row_tiles(a, ry0, ry1):
    blk = a[ry0 + 5:ry1 - 5].astype(int)
    isbg = (np.abs(blk - 233).max(axis=2) <= 10).mean(axis=0) > 0.97
    isbg[:258] = True
    return [r for r in runs(~isbg) if r[1] - r[0] > 100]


def photo_box(a, tx0, tx1, ty0, head, h):
    bg = a[ty0 + 2, tx0 + 3].astype(int)
    py0, py1 = ty0 + head, ty0 + head + h
    d = np.abs(a[py0:py1, tx0:tx1].astype(int) - bg).max(axis=2)
    margin = (d <= 20).mean(axis=0) > 0.97
    x1 = tx1
    while x1 > tx0 and margin[x1 - 1 - tx0]:
        x1 -= 1
    return [tx0, py0, x1, py1]


def inset(box, k=2):
    return [box[0] + k, box[1] + k, box[2] - k, box[3] - k]


def composite_tiles(rel, h, head_of):
    """回傳 [[box,...] 每列]；head_of(is_yellow) → 標題高度。"""
    a = np.asarray(Image.open(io.BytesIO(git_bytes(rel))).convert('RGB'))
    out = []
    for ry0, ry1 in sheet_rows(a):
        boxes = []
        for tx0, tx1 in row_tiles(a, ry0, ry1):
            ty0 = ry0 + 5
            yellow = a[ty0 + 2, tx0 + 3][2] < 235
            b = photo_box(a, tx0, tx1, ty0, head_of(yellow), h)
            if b[2] - b[0] > 100:
                boxes.append(inset(b))
        out.append(boxes)
    return out


# ---------- 圖片登錄 ----------

IMAGES = {}
MANIFEST = []


def res_of(rel):
    if rel.startswith(('img/cand/', 'r2/faces/heads/')):
        return 'lowres'
    if rel.startswith(('r3/pages/hires/', 'r3/compare/hires/', 'r3/checks/hires/')):
        return 'page300'
    if rel.startswith('r3/previews/'):
        return 'preview100'
    return 'sheet'


def put(iid, data, thumb_box, meta, res, extra=None, public_src=True):
    z = os.path.join(PUB, 'img', 'z', iid + '.jpg')
    t = os.path.join(PUB, 'img', 't', iid + '.jpg')
    with open(z, 'wb') as f:
        f.write(data)
    im = Image.open(io.BytesIO(data)).convert('RGB')
    th = im.copy()
    th.thumbnail(thumb_box, Image.LANCZOS)
    tdata = jpeg(th, 82)
    with open(t, 'wb') as f:
        f.write(tdata)
    IMAGES[iid] = {'z': f'img/z/{iid}.jpg', 't': f'img/t/{iid}.jpg', 'w': im.width, 'h': im.height,
                   'tw': th.width, 'th': th.height, 'kind': meta['kind'], 'res': res, **(extra or {})}
    if meta['kind'] != 'hires_preview' and public_src:
        IMAGES[iid]['src'] = meta['source']
    MANIFEST.append({'published': f'public/img/z/{iid}.jpg', 'sha256': sha256(data), **meta})
    MANIFEST.append({'published': f'public/img/t/{iid}.jpg', 'sha256': sha256(tdata), 'kind': 'thumbnail',
                     'source': f'public/img/z/{iid}.jpg', 'op': f'等比縮小至 {th.width}×{th.height}（Lanczos，JPEG q82）'})


def copy(iid, rel, thumb_box=(720, 720)):
    data = git_bytes(rel)
    assert blob_of(data) == git_blob(rel)
    put(iid, data, thumb_box, {'kind': 'copy', 'source': CAL + rel, 'source_blob': git_blob(rel), 'op': '位元組不變複製'}, res_of(rel))


def crop(iid, rel, box, thumb_box=(720, 720)):
    src = Image.open(io.BytesIO(git_bytes(rel))).convert('RGB')
    data = jpeg(src.crop(tuple(box)), 95)
    put(iid, data, thumb_box, {'kind': 'crop', 'source': CAL + rel, 'source_blob': git_blob(rel), 'box_px': box,
                               'op': f'裁切 {box}（只裁切；JPEG q95）'}, 'lowres')


HIRES_LONG = 1600


def hires_bytes(src_bytes):
    im = Image.open(io.BytesIO(src_bytes)).convert('RGB')
    w, h = im.size
    im.thumbnail((HIRES_LONG, HIRES_LONG), Image.LANCZOS)
    return jpeg(im, 88), (w, h)


def hires_source(cid, J, R, C, hf_dir, clean_dir):
    """回傳 (原檔位元組, manifest 來源描述)；核對不過就丟例外。不回傳 job_id。"""
    if cid in C:  # 有 R3 清理版的用清理版（與頁面其他地方一致）
        c = C[cid]
        b = open(os.path.join(clean_dir, os.path.basename(c['clean_file'])), 'rb').read()
        assert sha256(b) == c['clean_sha256'], cid
        return b, {'source': 'R3 清理輸出（data/cal_r3_cleanup_report.json 的 clean_sha256 核對）', 'source_sha256': c['clean_sha256']}
    src = J[cid]['src']
    if src.startswith('hf:'):
        r = next(x for x in R if x['job_id'] == src[3:])
        b = open(os.path.join(hf_dir, r['local']), 'rb').read()
        assert sha256(b) == r['sha256'], cid
        return b, {'source': 'R2 已取回的 Higgsfield 快取（data/cal_r2_hf_retrieved.json 的 sha256 核對）', 'source_sha256': r['sha256']}
    b = subprocess.check_output(['git', '-C', ROOT, 'show', f'{FIXED}:{src}'])
    blob = subprocess.check_output(['git', '-C', ROOT, 'rev-parse', f'{FIXED}:{src}'], text=True).strip()
    assert blob_of(b) == blob, cid
    return b, {'source': f'repo@{FIXED}:{src}', 'source_blob': blob, 'source_sha256': sha256(b)}


def hires(cid, J, R, C, hf_dir, clean_dir):
    b, meta = hires_source(cid, J, R, C, hf_dir, clean_dir)
    data, (w, h) = hires_bytes(b)
    im = Image.open(io.BytesIO(data))
    put('hi_' + cid, data, (720, 720), {'kind': 'hires_preview', 'cid': cid, **meta,
        'op': f'原檔 {w}×{h} 等比縮小至 {im.width}×{im.height}（Lanczos，JPEG q88，不帶中繼資料）'},
        'hires', {'cid': cid, 'orig_px': [w, h]})



# ---------- 第二階段素材（data/cal_m1_materials.json；本輪新增的人寫清單，讀工作目錄） ----------
# 圖片仍一律從固定 commit 讀（repo 檔、daily140 縮圖），或從可核對 sha256 的本機快取讀（R2 取回原圖、R3 清理輸出）。
M1_FILE = 'docs/calendar/data/cal_m1_materials.json'
ROSTER_FILE = 'docs/calendar/data/cal_m1_owner_roster.json'
M3_FILE = 'docs/calendar/data/cal_m3_shoot_plan.json'
MAT_THUMB = (480, 480)
SRC_ZH = {'repo': '既有原圖（repo）', 'hf': '既有原圖（R2 已取回）', 'clean': 'R3 局部清理版（本機清理輸出）',
          'thumb': '360×480 縮圖（原圖未取回）'}


def wt_bytes(rel):
    return open(os.path.join(ROOT, rel), 'rb').read()


def root_show(rel):
    b = subprocess.check_output(['git', '-C', ROOT, 'show', f'{FIXED}:{rel}'])
    blob = subprocess.check_output(['git', '-C', ROOT, 'rev-parse', f'{FIXED}:{rel}'], text=True).strip()
    assert blob_of(b) == blob, rel
    return b, blob


def mat_source(src, D140, R, C, hf_dir, clean_dir):
    """回傳 (原檔位元組, 種類 repo／hf／clean／thumb, manifest 來源描述)；核對不過就丟例外。不回傳 job_id。"""
    if src.startswith('clean:'):
        c = C[src[6:]]
        b = open(os.path.join(clean_dir, os.path.basename(c['clean_file'])), 'rb').read()
        assert sha256(b) == c['clean_sha256'], src
        return b, 'clean', {'source': f'R3 清理輸出 {src[6:]}（data/cal_r3_cleanup_report.json 的 clean_sha256 核對；原圖 {c["src"] if not c["src"].startswith("hf:") else "R2 取回原圖"}）',
                            'source_sha256': c['clean_sha256']}
    if src.startswith('daily140:'):
        f = src.split(':', 1)[1]
        row = D140[f]
        r = next((x for x in R if x['job_id'] == row['job_id']), None)
        if r:
            b = open(os.path.join(hf_dir, r['local']), 'rb').read()
            assert sha256(b) == r['sha256'], src
            return b, 'hf', {'source': f'R2 已取回的 Higgsfield 快取：daily140 {f}（data/cal_r2_daily140_jobs.json 對到 data/cal_r2_hf_retrieved.json，sha256 核對）',
                             'source_sha256': r['sha256']}
        rel = f'review/soul_pilot/daily140/thumbs/{f[:-4]}.jpg'
        b, blob = root_show(rel)
        return b, 'thumb', {'source': f'repo@{FIXED}:{rel}', 'source_blob': blob}
    b, blob = root_show(src)
    return b, 'repo', {'source': f'repo@{FIXED}:{src}', 'source_blob': blob, 'source_sha256': sha256(b)}


def excl_group(reason):
    if '待主管覆核' in reason:
        return 'pending'
    if any(k in reason for k in ('臉與', '臉部候選', '目視臉', '定案臉', '定案的 training_v2', '臉的版本')):
        return 'face'
    if any(k in reason for k in ('疑似裸露', '暗示裸露', '走光')):
        return 'exposure'
    if any(k in reason for k in ('近似重複', '重複檔')):
        return 'dup'
    return 'defect'


def build_materials(cast, R, C, hf_dir, clean_dir):
    M = json.loads(wt_bytes(M1_FILE))
    roster = json.loads(wt_bytes(ROSTER_FILE))
    assert [p['pid'] for p in M['people']] == roster['list'], '素材清單與名單紀錄不一致'
    D140 = {r['file']: r for r in load_json('data/cal_r2_daily140_jobs.json')['rows']}
    cands = {c['id']: c for c in cast['candidates']}
    people = []
    for p in M['people']:
        pid = p['pid']
        items, gaps = [], []
        for it in p['items']:
            b, kind, meta = mat_source(it['src'], D140, R, C, hf_dir, clean_dir)
            iid = 'm_' + it['id']
            src_im = Image.open(io.BytesIO(b))
            w, h = src_im.size
            if kind == 'thumb':
                put(iid, b, MAT_THUMB, {'kind': 'copy', 'mid': it['id'], 'mat_src': it['src'], **meta, 'op': '位元組不變複製（360×480 縮圖）'},
                    'lowres', {'orig_px': [w, h]}, public_src=False)
                gaps.append(f"{it['id']}（daily140 {it['src'].split(':', 1)[1][:3]}）只有 360×480 縮圖，原圖未取回")
            else:
                data, _ = hires_bytes(b)
                pim = Image.open(io.BytesIO(data))
                put(iid, data, MAT_THUMB, {'kind': 'hires_preview', 'mid': it['id'], 'mat_src': it['src'], **meta,
                    'op': f'原檔 {w}×{h} 等比縮小至 {pim.width}×{pim.height}（Lanczos，JPEG q88，不帶中繼資料）'},
                    'hires', {'orig_px': [w, h]})
            items.append({'id': it['id'], 'img': iid, 'tier': it['tier'], 'label': it['label'], 'fix': it['fix'],
                          'check': it['check'], 'r3': it.get('r3', ''), 'clean_of': it.get('clean_of', ''),
                          'scale': it.get('scale', ''), 'level': it.get('level', ''),
                          'kind': kind, 'src_zh': SRC_ZH[kind], 'orig_px': [w, h]})
        ex = {}
        for e in p['excluded']:
            g = excl_group(e['reason'])
            ex[g] = ex.get(g, 0) + 1
        c = cands[pid]
        people.append({'pid': pid, 'name': c['name'], 'native': c['native'], 'desc': c['desc'], 'face': c['face'],
                       'items': items, 'gaps': gaps, 'excluded': ex})
    in12 = set(roster['list'])
    pairs = [q for q in cast['pairs'] if q['a'] in in12 and q['b'] in in12]
    return {'roster': {k: roster[k] for k in ('version', 'decided_on', 'decided_by', 'list', 'order_note',
                                                'vs_original_recommendation', 'scope', 'access')},
            'roster_file': ROSTER_FILE, 'materials_file': M1_FILE,
            'materials_blob': blob_of(wt_bytes(M1_FILE)), 'roster_blob': blob_of(wt_bytes(ROSTER_FILE)),
            'checks': M['checks'], 'people': people, 'pairs': pairs,
            'unmeasured': roster['similarity_concerns']['unmeasured']}

def build_m3(mat):
    """M-3 拍攝企劃：企劃文字照搬；Aaliya 參考照片（固定 commit）等比縮小；其他圖片只引用既有素材預覽。"""
    raw = wt_bytes(M3_FILE)
    P = json.loads(raw)
    roster = json.loads(wt_bytes(ROSTER_FILE))
    assert [p['pid'] for p in P['people']] == roster['list'], '企劃與名單紀錄不一致'
    assert P['counts'] == {'generated': 0, 'credits': 0, 'trainings': 0}
    assert P['version'] == 'shoot-plan-v8' and P['revision']['from_version'] == 'shoot-plan-v7'
    acc, ver = P['status']['accepted'], P['status']['supervisor_verified']
    assert P['status']['m3'] == 'complete' and len(acc) == 23 and ver == ['H-luna-tanaka'] and not P['status']['revised'], 'M-4 R1 狀態不對'
    assert sorted(acc + ver) == sorted(x['id'] for x in P['sets'])
    assert P['status']['frames'] == 'accepted' and P['status']['months'] == 'confirmed' and P['status']['owner_decisions_open'] == 0 and P['questions'] == []
    for x in P['sets']:  # M-4 R1：23 套已接受（註明在哪一輪接受）；H-Luna 依 owner 指示修訂、主管覆核通過，R7 的原文與改動前後保留，Penny 沒有看過修訂後版本
        assert x['status'] == ('accepted' if x['id'] in acc else 'supervisor_verified') and x['print']['frame'] and x['print']['verdict'], x['id']
        if x['status'] == 'supervisor_verified':
            assert x['r7']['status'] == 'owner_revised' and x['r7']['owner'].strip() and x['r7']['diff'] and x['r7']['seen_by_owner'] is False, x['id']
            assert x['m4r1']['label'] == '依owner指示修訂，主管覆核通過' and x['m4r1']['seen_by_owner'] is False and x['r6']['change'].strip(), x['id']
        else:
            assert x['r7']['status'] == 'accepted' and x['r7']['accepted_in'] in ('R4', 'R6', 'R7'), x['id']
    M4 = P['m4_prep']  # R7：V-Iris 首試準備；M-4 R1：首試前核查（唯讀查詢與不扣款的報價預檢，不生成）
    assert M4['set'] == 'V-iris-chen' and M4['counts'] == {'generated': 0, 'credits': 0, 'higgsfield_calls': 0, 'price_prechecks': 0}
    assert M4['tbc'] and M4['accept'] and M4['lint'] and os.path.isfile(os.path.join(ROOT, M4['doc'])), 'V-Iris 首試準備不完整'
    R1 = M4['r1']
    assert R1['counts']['generated'] == 0 and R1['counts']['credits'] == 0 and R1['counts']['generation_jobs'] == 0 and R1['blockers'] and R1['cap']['v']
    assert all('state' in x for x in M4['tbc']) and not M4['workflow'][0]['v'].startswith('Penny 核定這套造型與費用'), '首試前提未更新'
    for b in 'HV':
        assert os.path.isfile(os.path.join(ROOT, 'docs/calendar/decision_site/public', P['printing']['diagrams'][b])), b
    assert all(x['id'] in acc for x in P['accepted_notes']['items']), '技術備註只列已接受的套數'
    # R5：已接受套數的英文妝感同步只多一句；橫直兩款不互相當參考圖
    for x in P['sets']:
        if 'r5' in x:
            assert x['status'] == 'accepted' and x['prompt'].count(x['r5']['added_en']) == 1, x['id']
    assert not P['execution']['model']['multi_stage'].startswith('不規劃多階段（先生成再換臉、外擴、放大）。若首批發現'), '已撤回的橫直參考圖策略'
    for x in P['sets']:  # R3：每套都要有七個攝影欄位（中文＋英文），英文句逐字在 prompt 裡
        c = x['cam']
        for k in ('shot', 'bounds', 'body', 'face', 'gaze', 'angle', 'comp', 'purpose'):
            assert c[k]['zh'].strip() and c[k]['en'].strip() and x['prompt'].count(c[k]['en']) >= 1, (x['id'], k)
        assert c['line'] and c['pos'] and c['focus'] and c['why'], x['id']
    ids = [x['id'] for x in P['sets']]
    assert len(ids) == 24 and len(set(ids)) == 24 and sorted(ids) == sorted(b + '-' + pid for pid in roster['list'] for b in 'HV'), '24 套 ID 不對'
    for b in 'HV':
        col = [m[b] for m in P['months']]
        assert [m['m'] for m in P['months']] == list(range(1, 13)) and sorted(col) == sorted(b + '-' + pid for pid in roster['list']), '月份不對'
    assert all(m['H'][2:] != m['V'][2:] for m in P['months']), '同月兩本同一人'
    have = {it['id'] for p in mat['people'] for it in p['items']}
    for x in P['owner_refs']['items']:
        assert x['id'] in have, x['id']
    for x in P['sets']:
        for r in x['refs']:
            assert r['id'] in have, r
    aal = {}
    for x in P['aaliya']['items']:
        b, blob = root_show(x['src'])
        data, (w, h) = hires_bytes(b)
        assert [w, h] == x['px'], (x['src'], w, h)
        pim = Image.open(io.BytesIO(data))
        iid = 'aal_' + x['key']
        put(iid, data, MAT_THUMB, {'kind': 'hires_preview', 'aal': x['key'], 'aal_src': x['src'],
                                   'source': f'repo@{FIXED}:{x["src"]}', 'source_blob': blob, 'source_sha256': sha256(b),
                                   'op': f'原檔 {w}×{h} 等比縮小至 {pim.width}×{pim.height}（Lanczos，JPEG q88，不帶中繼資料）'},
            'hires', {'orig_px': [w, h]})
        aal[x['key']] = iid
    pub = json.loads(raw)  # 公開資料不放 repo 路徑：Aaliya 只留「子資料夾/檔名」，其餘來源欄位（src）不發佈
    for x in pub['aaliya']['items']:
        x['file'] = '/'.join(x.pop('src').split('/')[-2:])

    def drop_src(o):
        if isinstance(o, dict):
            return {k: drop_src(v) for k, v in o.items() if k != 'src'}
        return [drop_src(v) for v in o] if isinstance(o, list) else o
    pub = drop_src(pub)
    text = json.dumps(pub, ensure_ascii=False)
    for bad in ('kols/', 'job_id', 'soul_id', 'sophia'):
        assert bad not in text.lower(), bad
    shas = {P['meta']['material_page_commit'], P['meta']['calendar_baseline'], P['meta']['aaliya_sources']['catalog_commit'],
            P['revision']['from_commit'], P['r5']['from_commit'], P['r6']['from_commit'], P['r7']['from_commit']}
    hexes = set(re.findall(r'(?<![0-9a-z])[0-9a-f]{8,}(?:-[0-9a-f]{4,})*', json.dumps(P, ensure_ascii=False)))
    assert hexes <= shas, f'企劃資料出現疑似 ID：{sorted(hexes - shas)}'  # 不放 Soul ID、job_id（連 repo 內的來源欄位也檢查）
    return {**pub, 'plan_file': M3_FILE, 'plan_blob': blob_of(raw), 'aaliya_img': aal}


# ---------- 資料 ----------

def load_json(rel):
    return json.loads(git_bytes(rel))


# R1 入圍比較 18 位（CAL_02 §3，data/cal_r1_candidates.json）＋R2 追加比較 2 位（CAL_02 §5.3／§6）。
# 描述只取自 R1／R2 文件（cal_r1_candidates.json 的 why／diff、CAL_02 §5.1、CAL_06），一句話；不新增量測。
REC12 = ['iris-chen', 'kanon-komori', 'luna-tanaka', 'angel-chiu', 'somi-oh', 'vicky-lin',
         'coco-wu', 'mia-huang', 'yuna-kim', 'tammy-chou', 'rin-ayase', 'rainie-hsu']
CAST_INFO = {  # id: (一句外型／氣質, 臉部照片來源, 其他照片)
    'iris-chen': ('長直黑髮、圓臉大眼，笑起來最甜的鄰家型', 'h1', ['c1', 'c2']),
    'kanon-komori': ('粉紫長髮＋瀏海，二次元偶像感；女僕咖啡廳人設', 'h1', ['c2', 'c3']),
    'luna-tanaka': ('黑色齊瀏海短鮑伯、嬌小，日系清純', 'h1', ['c1', 'c3']),
    'angel-chiu': ('高瘦窄臉、尖下巴，棕金漸層長髮；護理師人設', 'h1', ['c1', 'c2']),
    'somi-oh': ('銅橘短髮、表情外放，爽朗暖色的美食帳號', 'h1', ['c2', 'c3']),
    'vicky-lin': ('小麥膚色、高馬尾、健身體態，性感來自身體線條', 'h1', ['c1', 'c2']),
    'coco-wu': ('深棕長捲髮配瀏海，笑得最開的元氣甜', 'h2', ['c1', 'c2']),  # h1 背景有可辨識角色手機殼，改用 h2
    'mia-huang': ('灰金挑粉的捲短髮、霓虹電競房，甜而俏皮', 'h1', ['c1', 'c2']),
    'yuna-kim': ('及肩黑棕微捲、韓系素顏，清冷安靜', 'h1', ['c1', 'c2']),
    'tammy-chou': ('蜜金色大波浪，時髦的網拍老闆娘', 'h1', ['c1', 'c3']),
    'rin-ayase': ('酒紅長捲髮、銀座夜色，成熟性感、不靠暴露', 'h1', ['c2', 'c3']),
    'rainie-hsu': ('長直黑髮、濃妝立體，夜店派對感', 'h1', ['c1', 'c2']),
    'wanyin-jiang': ('長直黑髮、旗袍與蘇州園林，東方古典、安靜', 'h1', ['c1', 'c2']),
    'sophia-tseng': ('深棕及肩捲髮、28 歲貴婦感，都會夜景', 'h1', ['c2', 'c3']),
    'miu-shiraishi': ('白金短鮑伯＋瀏海、咖啡店員，甜', 'c3', ['c1', 'c2']),
    'jia-seo': ('藍黑髮＋薄荷內染、K-pop 舞蹈老師，偏冷', 'c3', ['c2', 'c1']),
    'peggy-lee': ('酒紅大捲髮＋灰挑染、改裝車行銷，帥氣性感', 'c3', ['c1', 'c2']),
    'yerin-han': ('亞麻棕長髮、高爾夫教練，運動甜美', 'c3', ['c1', 'c2']),
    'ananya-kapoor': ('深膚色、長捲髮、南亞五官（印度旁遮普設定）', 'h1', ['hi_ananya_2', 'x_ananya_3']),
    'wendy-yeo': ('銀灰鮑伯，冷感中性的反差路線', 'h1', ['x_wendy_1', 'x_wendy_2']),
}
EXTRA = {'ananya-kapoor': ('Ananya Kapoor', '', ''), 'wendy-yeo': ('Wendy Yeo', '', '')}
BATCH3 = {'kanon-komori', 'somi-oh', 'angel-chiu', 'tammy-chou', 'rin-ayase', 'wanyin-jiang', 'wendy-yeo',
          'miu-shiraishi', 'jia-seo', 'peggy-lee', 'yerin-han'}
# 既有遮髮量測紀錄（照錄；hit＝≤0.0220 既有同框門檻，near＝接近但未觸發，visual＝R2 目視觀察）
PAIRS = [
    ('miu-shiraishi', 'jia-seo', 0.01219, 'hit'), ('miu-shiraishi', 'kanon-komori', 0.01734, 'hit'),
    ('miu-shiraishi', 'somi-oh', 0.01894, 'hit'), ('jia-seo', 'somi-oh', 0.01986, 'hit'),
    ('peggy-lee', 'tammy-chou', 0.02008, 'hit'), ('yerin-han', 'rin-ayase', 0.02085, 'hit'),
    ('wanyin-jiang', 'rin-ayase', 0.02234, 'near'), ('wanyin-jiang', 'kanon-komori', 0.02299, 'near'),
    ('kanon-komori', 'rin-ayase', 0.02302, 'near'),
    ('kanon-komori', 'somi-oh', 0.02794, 'visual'), ('kanon-komori', 'tammy-chou', 0.03646, 'visual'),
    ('somi-oh', 'tammy-chou', 0.04018, 'visual'), ('iris-chen', 'rainie-hsu', None, 'visual'),
]
PAIR_NOTE = {
    'hit': '既有遮髮量測落在既有同框門檻內（≤0.0220）',
    'near': '既有遮髮量測接近門檻，但未觸發',
    'visual': '',
}
VISUAL = {
    frozenset(['kanon-komori', 'somi-oh']): 'R2 目視：遮髮後骨架接近，區分主要靠髮色與髮型',
    frozenset(['kanon-komori', 'tammy-chou']): 'R2 目視：遮髮後骨架接近，區分主要靠髮色與髮型',
    frozenset(['somi-oh', 'tammy-chou']): 'R2 目視：遮髮後骨架接近，區分主要靠髮色與髮型',
    frozenset(['iris-chen', 'rainie-hsu']): '兩位都是長直黑髮、沒有臉部量測；R2 目視：差異多來自妝感與表情',
}


def build_cast():
    r1 = {c['id']: c for c in load_json('data/cal_r1_candidates.json')['candidates']}
    assert len(r1) == 18 and set(REC12) <= set(r1)
    X = 'r2/decisions/CAL_R2_decide_people_compare.jpg'
    xbox = {'x_ananya_3': [880, 94, 1116, 514], 'x_wendy_1': [230, 564, 545, 984], 'x_wendy_2': [555, 564, 870, 984]}
    out = []
    for pid, (desc, face, extras) in CAST_INFO.items():
        def img(ref):
            if ref in ('h1', 'h2'):
                rel, iid = f'r2/faces/heads/{pid}_{ref[1]}.jpg', f'cast_{pid}_h{ref[1]}'
            elif ref in ('c1', 'c2', 'c3'):
                rel, iid = f'img/cand/{pid}_{ref[1]}.jpg', f'cast_{pid}_c{ref[1]}'
            elif ref.startswith('x_'):
                iid = 'cast_' + ref[2:]
                if iid not in IMAGES:
                    crop(iid, X, inset(xbox[ref]))
                return iid
            else:
                return ref  # 既有的高解析預覽
            if iid not in IMAGES:
                copy(iid, rel)
            return iid
        if pid in r1:
            c = r1[pid]
            group = 'rec' if pid in REC12 else ('backup' if c['role'] == 'backup' else 'out')
            name, native, origin, age = c['name'], c['native_name'], c['origin_src'], c['age']
        else:
            group = 'r2'
            name, native, origin = EXTRA[pid]
            age = None
        notes = []
        for a, b, v, kind in PAIRS:
            if pid in (a, b):
                other = b if pid == a else a
                notes.append({'with': other, 'v': v, 'kind': kind,
                              'text': VISUAL.get(frozenset([a, b]), PAIR_NOTE[kind])})
        out.append({'id': pid, 'name': name, 'native': native, 'origin': origin, 'age': age, 'group': group,
                    'desc': desc, 'face': img(face), 'extras': [img(e) for e in extras],
                    'measured': pid in BATCH3, 'pairs': notes})
    return {'candidates': out, 'rec12': REC12,
            'pairs': [{'a': a, 'b': b, 'v': v, 'kind': k, 'text': VISUAL.get(frozenset([a, b]), PAIR_NOTE[k])} for a, b, v, k in PAIRS],
            'sources': ['docs/calendar/CAL_02_CASTING.md §3（18 位）', 'docs/calendar/data/cal_r1_candidates.json',
                        'docs/calendar/CAL_02_CASTING.md §5.3、§6（Ananya、Wendy）', 'docs/calendar/CAL_06_FACES.md §2、§4']}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--hf-dir', help='R2 已取回的 Higgsfield 原圖快取（核對 sha256 後才使用）')
    ap.add_argument('--clean-dir', help='R3 清理輸出資料夾（含 coco_alt01.png 等；核對 clean_sha256）')
    a = ap.parse_args()
    if a.check:
        return check(a.hf_dir, a.clean_dir)
    if not (a.hf_dir and a.clean_dir):
        ap.error('產生時需要 --hf-dir 與 --clean-dir')
    for d in ('z', 't'):
        os.makedirs(os.path.join(PUB, 'img', d), exist_ok=True)
        for fn in os.listdir(os.path.join(PUB, 'img', d)):
            os.remove(os.path.join(PUB, 'img', d, fn))

    picks = load_json('data/cal_r3_picks.json')
    lay = {p['id']: p for p in load_json('data/cal_r3_layout_report.json')['pages']}
    months = picks['months']

    def pid(kind, M):
        return f'{kind}_{M["m"]:02d}_{M["pid"]}'

    # 整張複製：R3 樣張頁（300 dpi）
    for p in ['H_cover', 'V_cover', 'H_grid_09_yuna-kim', 'V_grid_12_rainie-hsu', 'V_year_2027']:
        copy(p, f'r3/pages/hires/{p}.jpg')
    for M in months:
        copy(pid('H_A', M), f'r3/pages/hires/{pid("H_A", M)}.jpg')
        copy(pid('V_U', M), f'r3/pages/hires/{pid("V_U", M)}.jpg')
        copy(pid('H_B', M), f'r3/compare/hires/{pid("H_B", M)}.jpg')
    va = [f'V_A_{M["m"]:02d}_{M["pid"]}' for M in months if M['pid'] in picks['compare_VA']]
    for p in va:
        copy(p, f'r3/compare/hires/{p}.jpg')
    for p in ['CHK_kanon_kanon_H_V_U', 'CHK_kanon_kanon_V_V_U']:
        copy(p, f'r3/checks/hires/{p}.jpg')
    copy('CAL_R2_focus_kanon_somi_tammy', 'r2/faces/CAL_R2_focus_kanon_somi_tammy_hires.jpg', (616, 2600))
    copy('CAL_R2_focus_iris_rainie', 'r2/faces/CAL_R2_focus_iris_rainie_hires.jpg', (616, 2600))
    copy('CAL_R2_decide_people_backup', 'r2/decisions/CAL_R2_decide_people_backup.jpg', (900, 1100))
    copy('CAL_R2_decide_people_compare', 'r2/decisions/CAL_R2_decide_people_compare.jpg', (1205, 1100))
    copy('coco_alt01_compare', 'r3/cleanup/coco_alt01_compare_hires.jpg', (1000, 1000))
    copy('CAL_R3_100pct_V_year_top', 'r3/previews/CAL_R3_100pct_V_year_top.jpg', (1000, 1000))
    copy('CAL_R3_100pct_H_grid_09_small_photo', 'r3/previews/CAL_R3_100pct_H_grid_09_small_photo.jpg', (1000, 1000))

    # 高解析預覽：有實際替代選項的照片＋名單比較用的 somi_V（來源核對後等比縮小）
    J = {c['cid']: c for c in load_json('data/cal_r2_judgments.json')['candidates']}
    R = load_json('data/cal_r2_hf_retrieved.json')['items']
    C = {c['cid']: c for c in load_json('data/cal_r3_cleanup_report.json')['items']}
    HI = ['kanon_H', 'angel_alt004', 'ananya_2', 'somi_V', 'somi_H', 'somi_alt065', 'coco_alt01',
          'tammy_H', 'tammy_alt075', 'rin_altR1V', 'rainie_alt02']
    for cid in HI:
        hires(cid, J, R, C, a.hf_dir, a.clean_dir)

    # 裁切：決策 B（每格 390×520）
    B = 'r3/decisions/CAL_R3_decide_B_scale_style_hires.jpg'
    rowsB = composite_tiles(B, 520, lambda y: 62)
    namesB = [['iris_V', 'iris_H', 'scale_S3_ref'], ['kanon_alt028', 'kanon_H', 'kanon_V'], ['angel_H', 'angel_alt004', 'angel_V']]
    assert [len(r) for r in rowsB] == [3, 3, 3], rowsB
    for names, boxes in zip(namesB, rowsB):
        for n, b in zip(names, boxes):
            # 有高解析預覽，或已有 300 dpi 樣張可看的推薦圖，不再發佈低解析裁切
            if n not in HI and n not in ('kanon_alt028', 'angel_H', 'angel_V'):
                crop('tile_' + n, B, b)
    # 裁切：各月選項附表（每格高 380）
    O = 'r3/decisions/CAL_R3_decide_options_hires.jpg'
    rowsO = composite_tiles(O, 380, lambda y: 62 if y else 118)
    namesO = {2: ['kanon_alt028', 'kanon_H'], 4: ['angel_H', 'angel_V', 'angel_alt004'], 5: ['somi_V', 'somi_H', 'somi_alt065'],
              7: ['coco_H', 'coco_alt01'], 9: ['yuna_H', 'yuna_V', 'yuna_altsoft'], 10: ['tammy_V', 'tammy_H', 'tammy_alt075'],
              11: ['rin_H', 'rin_V', 'rin_altR1V'], 12: ['rainie_H', 'rainie_V', 'rainie_alt02']}
    om = [M['m'] for M in months if M['options']]
    assert om == list(namesO) and [len(r) for r in rowsO] == [len(namesO[m]) for m in om], rowsO
    want = set()  # 附表裡的替代照片都已有高解析預覽（9b 用固定 commit 的 100% 預覽），不再裁切
    for m, boxes in zip(om, rowsO):
        for n, b in zip(namesO[m], boxes):
            if n in want:
                crop('tile_' + n, O, b)
    # 裁切：決策 A 的 5 月頭像（封面同一張頭像；A0 Somi、A1 Ananya）
    A = 'r3/decisions/CAL_R3_decide_A_roster_hires.jpg'
    aa = np.asarray(Image.open(io.BytesIO(git_bytes(A))).convert('RGB'))
    (ry0, _), = sheet_rows(aa)
    for gx, n in ((260, 'head_somi_V'), (1506, 'head_ananya_2')):
        cy = ry0 + 5 + 62 + 306
        crop(n, A, inset(photo_box(aa, gx, gx + 300, cy, 62, 230)), (460, 460))
    # A0、A1 各自的 12 人格（每格 300×298、間距 8；整格 1232×918）
    for gx, n in ((260, 'roster_A0'), (1506, 'roster_A1')):
        crop(n, A, [gx, ry0 + 5 + 62, gx + 1232 - 8, ry0 + 5 + 62 + 918 - 8], (900, 900))

    # ---------- 第一階段選角：候選人設與辨識用圖 ----------
    cast = build_cast()

    # ---------- 第二階段：入選 12 位的素材 ----------
    mat = build_materials(cast, R, C, a.hf_dir, a.clean_dir)

    # ---------- M-3：拍攝企劃 ----------
    m3 = build_m3(mat)

    # ---------- 頁面資料 ----------
    def ph(p):
        q = lay[p]['photos'][0]
        return {'page': p, 'cid': q['cid'], 'frame': q['frame'], 'frame_mm': q['frame_size_mm'], 'ppi': q['ppi_w'],
                'cleaned': q['used_file'] == 'clean', 'hair': q['hair']['status_auto'], 'hair_check': q['hair']['manual_check'],
                'face_clear': q['face']['clear_of_coil'] and q['face']['complete_in_frame']}

    out_months = []
    for M in months:
        out_months.append({k: M[k] for k in ('m', 'pid', 'en', 'zh', 'tag', 'H', 'V', 'sweet', 'sexy', 'options')} | {
            'HA': ph(pid('H_A', M)), 'VU': ph(pid('V_U', M)), 'HB': ph(pid('H_B', M)),
            'VA': ph(f'V_A_{M["m"]:02d}_{M["pid"]}') if M['pid'] in picks['compare_VA'] else None})
    data = {
        'fixed_sha': FIXED,
        'built_from': [CAL + 'data/cal_r3_picks.json', CAL + 'data/cal_r3_layout_report.json'],
        'decision_codes': picks['decision_codes'],
        'roster_compare': picks['roster_compare'],
        'grid_faces': picks['grid_faces'],
        'months': out_months,
        'checks': {p: ph(p) for p in ('CHK_kanon_kanon_H_V_U', 'CHK_kanon_kanon_V_V_U', 'CHK_kanon_kanon_alt028_V_U')},
        'grid9': ph('H_grid_09_yuna-kim'),
        'hires_of': {cid: 'hi_' + cid for cid in HI},
        'cast': cast,
        'mat': mat,
        'm3': m3,
        'images': IMAGES,
    }
    with open(os.path.join(PUB, 'data.js'), 'w', encoding='utf-8') as f:
        f.write('// 程式產生（docs/calendar/tools/build_cal_decision_site.py），不要手改。資料來源：固定成果 commit ' + FIXED + '\n')
        f.write('window.CAL_DATA = ' + json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + ';\n')
    man = {'generated_by': 'docs/calendar/tools/build_cal_decision_site.py', 'fixed_sha': FIXED,
           'note': '只發佈下列檔案。copy＝與固定 commit 的同一路徑位元組相同（source_blob＝git blob）；crop＝從固定 commit 的拼圖純裁切（低解析選圖參考）；hires_preview＝可核對來源的原圖等比縮小（不含 job_id）；thumbnail＝等比縮小。沒有生成、外擴、增強或修圖。本檔不對外提供。',
           'files': MANIFEST}
    with open(os.path.join(SITE, 'ASSET_MANIFEST.json'), 'w', encoding='utf-8') as f:
        json.dump(man, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'ok: {len(IMAGES)} images, {len(MANIFEST)} files')


def check(hf_dir=None, clean_dir=None):
    man = json.load(open(os.path.join(SITE, 'ASSET_MANIFEST.json'), encoding='utf-8'))
    assert man['fixed_sha'] == FIXED
    listed = set()
    bad = 0
    J = {c['cid']: c for c in load_json('data/cal_r2_judgments.json')['candidates']}
    R = load_json('data/cal_r2_hf_retrieved.json')['items']
    C = {c['cid']: c for c in load_json('data/cal_r3_cleanup_report.json')['items']}
    D140 = {r['file']: r for r in load_json('data/cal_r2_daily140_jobs.json')['rows']}
    not_recomputed = []
    for e in man['files']:
        p = os.path.join(SITE, e['published'])
        listed.add(os.path.relpath(p, PUB))
        data = open(p, 'rb').read()
        if sha256(data) != e['sha256']:
            print('sha256 不符', e['published']); bad += 1
        if e['kind'] == 'copy' and 'mid' in e:
            b, kind, _ = mat_source(e['mat_src'], D140, R, C, hf_dir, clean_dir)
            if kind != 'thumb' or b != data:
                print('素材縮圖與固定 commit 不同', e['published']); bad += 1
        elif e['kind'] == 'copy':
            if blob_of(data) != e['source_blob'] or git_blob(e['source'][len(CAL):]) != e['source_blob']:
                print('與固定 commit 不同', e['published']); bad += 1
        if e['kind'] == 'crop':
            src = Image.open(io.BytesIO(git_bytes(e['source'][len(CAL):]))).convert('RGB')
            if jpeg(src.crop(tuple(e['box_px'])), 95) != data:
                print('裁切無法重現', e['published']); bad += 1
        if e['kind'] == 'hires_preview':
            needs_cache = not e['source'].startswith('repo@')
            name = e.get('mid') or e.get('aal') or e['cid']
            if needs_cache and not (hf_dir and clean_dir):
                not_recomputed.append(name)
            else:
                if 'aal' in e:
                    src = root_show(e['aal_src'])[0]
                elif 'mid' in e:
                    src = mat_source(e['mat_src'], D140, R, C, hf_dir, clean_dir)[0]
                else:
                    src = hires_source(e['cid'], J, R, C, hf_dir, clean_dir)[0]
                if hires_bytes(src)[0] != data:
                    print('高解析預覽無法重現', e['published']); bad += 1
    on_disk = set()
    for d in ('z', 't'):
        for fn in os.listdir(os.path.join(PUB, 'img', d)):
            on_disk.add(f'img/{d}/{fn}')
    extra = on_disk - listed
    if extra:
        print('manifest 以外的圖片：', sorted(extra)); bad += 1
    n = {k: sum(e['kind'] == k for e in man['files']) for k in ('copy', 'crop', 'hires_preview', 'thumbnail')}
    print(f'{"FAIL" if bad else "PASS"}: {len(man["files"])} 檔（copy {n["copy"]}、crop {n["crop"]}、高解析預覽 {n["hires_preview"]}、thumbnail {n["thumbnail"]}），問題 {bad}'
          + (f'；未提供快取、只核對 sha256 的高解析預覽：{", ".join(not_recomputed)}' if not_recomputed else ''))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
