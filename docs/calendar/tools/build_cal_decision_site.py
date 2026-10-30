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
- M-3 拍攝企劃（data/cal_m3_shoot_plan.json，R2 起為 24 套雙款，R3 起每套附攝影設計，R4 起附印刷構圖判斷，M-4 R1 起 M-3 完成（23 套已接受＋H-Luna 主管覆核通過）並附 V-Iris 首試準備與首試前核查，M-4 R2 起附單張首試結果（照片不公開），人寫，從工作目錄讀）：企劃文字照搬；Aaliya 參考照片從固定 commit 讀檔後等比縮小，
  其餘參考圖沿用第二階段素材的預覽。企劃資料不含 Soul ID 或 job_id；新企劃沒有任何生成圖。M-4 R3 起這份企劃改在歷史頁（history.html），
  公開資料再移除交易原始資料（交易時間、他人交易列與統計），只留實扣摘要。
- M-4 R3 目前檢視頁（shoot.html；data/cal_review_current.json，人寫，從工作目錄讀）：V-Iris 首試照片（主管同意公開）——原圖 PNG 只移除
  文字中繼資料區塊（含工作識別碼）、顯示版等比縮小、套框預覽位元組不變；來源 commit 與 sha256 記在資料檔。M-4 R4：Penny 接受這張（含反光板），
  主頁標「已接受」、拿掉回饋題與反光板裁切；完成的檢視項目（data/cal_review_history.json）放進 data.js 給歷史頁只讀顯示。
  M-4 R5：第一批 5 張（一次看一位；原圖去文字區塊、顯示版、套框預覽位元組不變），V-Iris 移到「已接受紀錄」（只留原圖與顯示版）。
不生成、不外擴、不增強、不修圖、不重新下載。

輸出：docs/calendar/decision_site/public/img/{z,t,review,pick}/、public/data.js、public/review-data.js、public/pick-data.js、decision_site/ASSET_MANIFEST.json
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
    assert P['counts'] == {'generated': 85, 'credits': 11.96, 'trainings': 0}, 'M-4 R2 生成 1 張；M-4 R5 第一批 5 張（每位 1 次請求）；M-4 R7、R8、R11 V-Somi 試拍各 1 張；M-4 R14 Tammy、Rin 各 1 張；M-4 R16 Rin 1 張；M-4 R18 Yerin、Jia 各 1 張；M-4 R20 20 套各 2 張；M-4 R21 20 次請求產出 19 張（淨扣 2.28）；M-4 R22 4 套各 2 張；M-4 R23 V-Rainie 2 張；M-4 R24 V-Rainie 2 張（Seedream＋既有身分錨點，各 1）'
    assert P.get('draft_counts') == {'generated': 2, 'credits': 4} == {k: P['status']['production']['drafts'][k] for k in ('generated', 'credits')}, 'M-4 R9、R10 構圖底稿各 1 張另計，不併入月面照片'
    assert P['version'] == 'shoot-plan-v12' and P['revision']['from_version'] == 'shoot-plan-v11'
    PR = P['status']['production']  # M-4 R4：Penny 接受 V-Iris（含反光板）；M-4 R6：第一批 5 張 Penny 全數退回，24 套重審提案待主管覆核
    assert P['status']['iris_first'] == 'accepted-by-owner' and PR['accepted_sets'][:3] == ['V-iris-chen', 'V-tammy-chou', 'V-rin-ayase'] and len(PR['accepted_sets']) == 24 and (PR['sets_total'], PR['accepted'], PR['selected_pending_edit'], PR['rejected_replan'], PR['not_generated'], PR['to_complete'], PR['generated_cumulative'], PR['pending_owner_review']) == (24, 24, 0, 0, 0, 0, 85, 0)
    assert P['m4_prep']['r4']['status'].startswith('Penny 接受') and P['batch1']['status'] == 'owner-rejected-r6' and P['batch1']['sets'] == BATCH1_SETS and PR['rejected_sets'] == [s for s in BATCH1_SETS if s not in PR['accepted_sets'] + PR['pick_sets']]  # M-4 R16：Penny 接受 Tammy R14；R17 後接受 Rin R14；R20：Yerin、Jia 有新候選
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
    R2 = M4['r2']  # M-4 R2：只送一次；歸屬只標「依時窗及唯一任務推定」；照片與工作 ID 不放公開資料
    assert R2['counts']['generation_requests'] == 1 and R2['counts']['images'] == 1 and R2['counts']['retries'] == 0, '首試只能送一次'
    assert R2['attribution']['level'] == '依時窗及唯一任務推定' and R2['charge']['within_budget'] and R2['accept'] and R2['verdict']
    assert '已關聯」' not in json.dumps(R1['recon'], ensure_ascii=False) and not R1['cap']['why'].startswith('當前報價 0.12；整數顯示值是 1'), 'R1 覆核用語未同步'
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
    redact_tx(pub)
    text = json.dumps(pub, ensure_ascii=False)
    for bad in ('kols/', 'job_id', 'soul_id', 'sophia'):
        assert bad not in text.lower(), bad
    assert not TX_RAW.search(text), f'公開資料出現交易原始資料：{TX_RAW.search(text).group(0)}'
    shas = {P['meta']['material_page_commit'], P['meta']['calendar_baseline'], P['meta']['aaliya_sources']['catalog_commit'],
            P['revision']['from_commit'], P['r5']['from_commit'], P['r6']['from_commit'], P['r7']['from_commit'], P['m4r1']['from_commit'],
            P['m4r2']['from_commit'], P['m4r4']['from_commit'], P['m4r5']['from_commit'], P['m4r6']['from_commit'],
            P['m4r7']['from_commit'], P['m4r7']['photo_commit'], P['m4r7']['record_commit'],
            P['m4r8']['from_commit'], P['m4r8']['photo_commit'], P['m4r8']['record_commit'], P['m4r9']['from_commit'],
            P['m4r9']['photo_commit'], P['m4r9']['record_commit'], P['m4r10']['from_commit'], P['m4r11']['from_commit'],
            P['m4r11']['photo_commit'], P['m4r11']['record_commit'], P['m4r12']['from_commit'], P['m4r13']['from_commit'],
            P['m4r13b']['from_commit'], P['m4r14']['from_commit'],
            P['m4r15']['from_commit'], P['m4r16']['from_commit'],
            P['m4r17']['from_commit'], P['m4r17b']['from_commit'],
            P['m4r18']['from_commit'], P['m4r19']['from_commit'], P['m4r20']['from_commit'], P['m4r21']['from_commit'], P['m4r22']['from_commit'], P['m4r23']['from_commit'], P['m4r24']['from_commit'], P['m4r25']['from_commit'], P['m5r26']['from_commit'], P['m5r27']['from_commit']}   # commit SHA，不是私有 ID
    hexes = set(re.findall(r'(?<![0-9a-z])[0-9a-f]{8,}(?:-[0-9a-f]{4,})*', json.dumps(P, ensure_ascii=False)))
    assert hexes <= shas, f'企劃資料出現疑似 ID：{sorted(hexes - shas)}'  # 不放 Soul ID、job_id（連 repo 內的來源欄位也檢查）
    return {**pub, 'plan_file': M3_FILE, 'plan_blob': blob_of(raw), 'aaliya_img': aal}


# M-4 R3：交易原始資料不公開。公開資料（歷史頁）只留摘要：實扣淨額、精確報價、核准預算、歸屬層級；
# 交易時間、送出前邊界列、他人的交易與任務、帳號交易統計只留在 repo（data/cal_m3_shoot_plan.json、私有執行紀錄）。
TX_HIDDEN = '交易明細原始列不公開（保存在私有 repo）'
TX_RAW = re.compile(r'\d{2}:\d{2}:\d{2}|\d{1,2}-\d{2} \d{2}:\d{2}|列 Nano Banana|個 nano_banana|筆交易|秒 \+0')  # 交易時間、他人交易列與統計


def redact_tx(pub):
    def sub(o, k, must, new):
        assert must in o[k], (k, must)
        o[k] = new
    M4 = pub['m4_prep']
    R1, R2 = M4['r1'], M4['r2']
    ch = R2['charge']
    R2['charge'] = {k: ch[k] for k in ('net', 'budget', 'quote_exact', 'within_budget', 'above_quote', 'anomaly')} | {
        'n_spend': len(ch['spend']), 'n_refund': len(ch['refund']), 'rows': TX_HIDDEN}
    pre = next(x for x in R2['pre'] if x['k'] == '交易邊界')
    sub(pre, 'v', '送出前最新一列', '送出前已記下交易明細的最新一列；前 30 列沒有 Soul V2。' + TX_HIDDEN)
    sub(R2['attribution']['basis'], 1, 'nano_banana_2', '同一時窗帳號的圖片任務裡，soul_2 只有本次這一個；其他模型的任務與扣款不是 Soul V2，不影響歸屬（明細不公開）。')
    h = R1['history'][1]
    sub(h, 'k', '帳號交易明細（2026-10-19）', '帳號交易明細（非本案）')
    sub(h, 'v', '32 秒', '曾有 Soul V2 扣款後同額退款')
    sub(R1['failure'], 0, '2026-10-19', '失敗可能退款：帳號交易明細有 Soul V2 扣款後同額退款的紀錄（非本案）；其他模型也常見扣款後退款。')
    sub(R1['recon_limits'], 2, '120 筆交易', '送出前兩天的帳號交易裡 Soul V2 很少（明細不公開）；視窗內撞到他人 Soul V2 的機會低，但不能排除。')
    h = pub['execution']['cost']['history'][1]
    sub(h, 'k', '2026-10-13 帳號交易明細', '帳號交易明細（2026-10-13 查詢，非本案）')
    sub(h, 'v', '今天也有', 'Soul V2 仍以每筆 −0.12 記帳（明細不公開）')


# ---------- 目前檢視頁（shoot.html，M-4 R3 起）——當前照片、套框預覽、待決事項 ----------
# 主頁只放「當前照片＋待決事項」（data/cal_review_current.json，人寫，從工作目錄讀）；完成項目移到 data/cal_review_history.json 與歷史頁（history.html）。
# M-4 R4：Penny 接受 V-Iris（含反光板），主頁改為「已接受」並拿掉回饋題；反光板裁切不再發佈。
# 圖片從資料檔記錄的 commit 讀檔並核對 sha256：
# - 原圖 PNG：只移除文字中繼資料區塊（tEXt／iTXt／zTXt；原檔帶有生成平台的工作識別碼），其餘區塊位元組不變，解碼後像素相同；
# - 顯示版：原圖等比縮小（長邊 1600 px，JPEG q88，不帶中繼資料）；套框預覽：位元組不變複製。
# 不修圖、不調身材、不重新生成。輸出 public/img/review/ 與 public/review-data.js（不放 Soul ID、工作 ID、交易資料、repo 路徑）。
REVIEW_FILE = 'docs/calendar/data/cal_review_current.json'
REVIEW_HIST = 'docs/calendar/data/cal_review_history.json'
REVIEW_DIR = os.path.join(PUB, 'img', 'review')
PNG_SIG = b'\x89PNG\r\n\x1a\n'
PNG_TEXT = (b'tEXt', b'iTXt', b'zTXt')


def png_chunks(b):
    assert b[:8] == PNG_SIG
    i, out = 8, []
    while i < len(b):
        n = int.from_bytes(b[i:i + 4], 'big')
        out.append((b[i + 4:i + 8], b[i:i + 12 + n]))
        i += 12 + n
    assert i == len(b) and out[-1][0] == b'IEND'
    return out


def png_strip_text(b):
    ch = png_chunks(b)
    return PNG_SIG + b''.join(c for t, c in ch if t not in PNG_TEXT), [t.decode() for t, _ in ch if t in PNG_TEXT]


def review_src(s):
    b = subprocess.check_output(['git', '-C', ROOT, 'show', f'{s["commit"]}:{s["path"]}'])
    assert sha256(b) == s['sha256'], s['path']
    return b


def review_png(ph, name):
    """原圖 PNG 只移除文字中繼資料區塊；回傳 (公開檔名, 位元組, manifest 欄位, 顯示版)。"""
    png = review_src(ph['src'])
    clean, removed = png_strip_text(png)
    assert removed == ['tEXt'], removed
    idat = lambda b: b''.join(c for t, c in png_chunks(b) if t == b'IDAT')
    a, c = Image.open(io.BytesIO(png)), Image.open(io.BytesIO(clean))
    assert idat(clean) == idat(png) and list(a.size) == ph['px'] and a.tobytes() == c.tobytes() and not c.info, '去中繼資料後影像不同'
    view, _ = hires_bytes(png)
    vim = Image.open(io.BytesIO(view))
    src = {'source': f'{ph["src"]["commit"]}:{ph["src"]["path"]}', 'source_sha256': ph['src']['sha256']}
    return [
        (name + '.png', clean, {'kind': 'review_png', 'set': ph['set'], **src,
            'op': f'只移除文字中繼資料區塊 {"、".join(removed)}（含生成平台工作識別碼）；IHDR／IDAT／IEND 位元組不變，解碼像素相同'}),
        (name + '_view.jpg', view, {'kind': 'review_preview', 'set': ph['set'], **src,
            'op': f'原圖 {a.width}×{a.height} 等比縮小至 {vim.width}×{vim.height}（Lanczos，JPEG q88，不帶中繼資料）'}),
    ]


def review_outputs(R):
    """回傳 [(檔名, 位元組, manifest 欄位)]；產生與 --check 共用。
    M-4 R5：第一批 5 張（原圖去文字區塊、顯示版、套框預覽位元組不變）＋已接受紀錄的 V-Iris（沿用 M-4 R3 起的公開檔名）。"""
    out = []
    for ph in R['batch']['photos']:
        out += review_png(ph, ph['set'] + '_m4r5')
        fr = ph['frame_src']
        out.append((os.path.basename(fr['path']), review_src(fr), {'kind': 'review_copy', 'set': ph['set'],
                    'source': f'{fr["commit"]}:{fr["path"]}', 'source_sha256': fr['sha256'], 'op': '位元組不變複製'}))
    for a in R['accepted']:
        out += [(n.replace('_m4r2.png', '_m4r2_first_test.png'), d, m) for n, d, m in review_png(a, a['set'] + '_m4r2')]
    return out


def public_secrets():
    """不能出現在任何公開檔的字串：Iris 與第一批 5 位的 Soul ID、首試與第一批的工作 ID（私有執行紀錄與原圖文字區塊）。只在記憶體比對，不輸出。"""
    R = json.loads(wt_bytes(REVIEW_FILE))
    out = set()
    for pid in ['iris-chen'] + [ph['src']['path'].split('/')[1] for ph in R['batch']['photos']]:
        out.add(json.loads(wt_bytes(f'kols/{pid}/profile.json'))['ai_assets']['training_images_v1']['soul_training']['soul_id'])
    logs = sorted(f'review/calendar/{d}/execution_log.json' for d in os.listdir(os.path.join(ROOT, 'review', 'calendar'))
                  if d.startswith(('m4_r', 'm5_r')) and os.path.isfile(os.path.join(ROOT, 'review', 'calendar', d, 'execution_log.json')))
    assert 'review/calendar/m4_r20/execution_log.json' in logs  # M-4 R20 起：所有 M-4 私有執行紀錄的 UUID（含 12 位的 Soul ID 與全部任務 ID）
    assert 'review/calendar/m5_r27/execution_log.json' in logs  # M-5 R27 起：封面生成的任務 ID、上傳的 media ID 與結果網址裡的帳號路徑
    for log in logs:
        t = wt_bytes(log).decode()
        out |= set(re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', t))
        out |= set(re.findall(r'user_[A-Za-z0-9]{20,}', t))
    for ph in R['batch']['photos'] + R['accepted'] + list(pick_photos(json.loads(wt_bytes(PICK_FILE)))):
        for t, c in png_chunks(review_src(ph['src'])):
            if t in PNG_TEXT:
                out.add(c[8:-4].split(b'\0', 1)[1].decode('latin-1'))
    assert len(out) >= 12 and all(len(x) >= 32 for x in out)
    return out


def scan_public(secrets):
    """回傳公開資料夾裡含私有識別碼的檔案（含去掉連字號的寫法）。"""
    needles = [x.encode() for x in secrets] + [x.replace('-', '').encode() for x in secrets]
    hits = []
    for d, _, fs in os.walk(PUB):
        for fn in fs:
            b = open(os.path.join(d, fn), 'rb').read()
            if any(n in b for n in needles):
                hits.append(os.path.relpath(os.path.join(d, fn), PUB))
    return hits


BATCH1_SETS = ['V-tammy-chou', 'V-rin-ayase', 'V-somi-oh', 'H-yerin-han', 'H-jia-seo']


def build_review():
    raw = wt_bytes(REVIEW_FILE)
    R = json.loads(raw)
    B = R['batch']
    assert R['round'] == 'M-4 R5' and [p['set'] for p in B['photos']] == BATCH1_SETS and B['key_prefix'] == 'cal2027-batch1-v1:'
    assert all(p['key'] == B['key_prefix'] + p['set'] and 1 <= len(p['checks']) <= 5 for p in B['photos']), '回饋鍵一張一個；看圖提醒精簡'
    assert B['photo_version'].startswith('M-4 R5 第一批 5 張'), '複製的回饋要帶照片版本'
    assert [a['set'] for a in R['accepted']] == ['V-iris-chen'] and '不需回覆' in R['accepted'][0]['v'] and '不是印刷核准' in B['frame_label']
    assert 'feedback' not in R and 'photo' not in R and 'next' not in R
    os.makedirs(REVIEW_DIR, exist_ok=True)
    for fn in os.listdir(REVIEW_DIR):
        os.remove(os.path.join(REVIEW_DIR, fn))
    files = {}
    for name, data, meta in review_outputs(R):
        with open(os.path.join(REVIEW_DIR, name), 'wb') as f:
            f.write(data)
        MANIFEST.append({'published': f'public/img/review/{name}', 'sha256': sha256(data), **meta})
        im = Image.open(io.BytesIO(data))
        files.setdefault(meta['set'], {})[{'review_png': 'png', 'review_preview': 'view', 'review_copy': 'frame'}[meta['kind']]] = {
            'src': f'img/review/{name}', 'w': im.width, 'h': im.height, 'bytes': len(data)}
    pub = json.loads(raw)
    pub.pop('note')
    for x in pub['batch']['photos'] + pub['accepted']:
        x.pop('src')
        x.pop('frame_src', None)
        x['img'] = files[x['set']]
        assert set(x['img']) == ({'png', 'view', 'frame'} if 'key' in x else {'png', 'view'})
    text = json.dumps(pub, ensure_ascii=False)
    for bad in ('kols/', 'job', 'soul', 'review/calendar', 'credit', '交易', '扣款', 'natural skin texture', 'lighting:', 'she wears', 'prompt'):  # 主頁不放長 prompt 與費用
        assert bad not in text.lower(), bad
    assert not re.search(r'[0-9a-f]{8,}', text), '檢視頁資料出現疑似 ID'
    return pub


# ---------- 選片頁（shoot.html，M-4 R20 起；R21 第二輪；R22 第三輪；R23 第四輪；R24 第五輪；R25 起為定案相簿）——本輪待確認＋已選＋待處理，或定案＋歷史候選 ----------
# 資料 data/cal_pick_r25.json（mode=final：24 套定案照片＋各套歷史候選；不收集回饋）（人寫，從工作目錄讀）；資料裡凡是帶 img_id 與 src 的照片物件，都從記錄的 commit 讀原圖 PNG 並核對 sha256，
# 公開兩種 JPEG（不帶任何中繼資料）：顯示版等比縮小（長邊 1600 px，JPEG q88）；完整版原尺寸（JPEG q92），供放大檢視。不修圖、不裁切、不重新生成
# （調色版是 repo 內已 commit 的本機調色衍生檔，這裡同樣只轉檔）。
# 每張照片綁定固定圖片識別 img_id（<套別>-R2x-<A|B|1|2>、V-Somi 先前試拍 V-somi-oh-R5／R7／R8／R11、本機調色／修正版 <來源>-G21／-G22／-G23）；
# 頁面回饋鍵 cal2027-pick-r24-v1:<套別>，存的是當時的 img_id，換圖就不再套用舊回饋；R20–R23 的鍵（cal2027-pick-r20-v1: … -r23-v1:）不讀、不寫、不刪。
# R24 起 V-Rainie 原圖是 Seedream 4.5 輸出（3:4，1728×2304），同樣帶平台文字區塊、同樣只轉檔。
# 每項的 history 是前幾輪的照片（只看不選）。
# 公開資料不放 prompt、自查、費用、執行紀錄、Soul ID、任務 ID 或 repo 路徑。
PICK_FILE = 'docs/calendar/data/cal_pick_r25.json'
FINAL_FILE = 'docs/calendar/data/cal_m4_final_r25.json'
PICK_DIR = os.path.join(PUB, 'img', 'pick')


def pick_imgs(x):
    """一張照片的公開檔：[(檔名, 位元組, manifest 欄位)]；產生與 --check 共用。"""
    png = review_src(x['src'])
    clean, removed = png_strip_text(png)
    assert removed == (['tEXt'] if not re.search(r'-G2\d$', x['img_id']) else []), (x['img_id'], removed)  # 生成原圖帶平台文字區塊；本機調色／修正衍生檔沒有
    im = Image.open(io.BytesIO(clean))
    assert list(im.size) == x['px'] and set(im.info) <= {'dpi'}, x['img_id']   # Seedream 原圖另帶 pHYs（只有像素密度，無識別資訊）；公開檔一律重新編碼為不帶中繼資料的 JPEG
    rgb = im.convert('RGB')
    view, _ = hires_bytes(png)
    vim = Image.open(io.BytesIO(view))
    src = {'set': x['set'], 'img_id': x['img_id'], 'source': f'{x["src"]["commit"]}:{x["src"]["path"]}', 'source_sha256': x['src']['sha256']}
    return [(x['img_id'] + '_view.jpg', view, {'kind': 'pick_preview', **src, 'op': f'原圖 {im.width}×{im.height} 等比縮小至 {vim.width}×{vim.height}（Lanczos，JPEG q88，不帶中繼資料）'}),
            (x['img_id'] + '.jpg', jpeg(rgb, 92), {'kind': 'pick_full', **src, 'op': f'原圖 {im.width}×{im.height} 原尺寸轉 JPEG q92（不裁切、不縮放，不帶中繼資料）'})]


def photo_objs(node, sid=None):
    """走訪資料，回傳所有帶 img_id 與 src 的照片物件（附上所屬套別）。"""
    if isinstance(node, dict):
        sid = node.get('set', sid)
        if 'img_id' in node and 'src' in node:
            yield node, sid
        for v in node.values():
            yield from photo_objs(v, sid)
    elif isinstance(node, list):
        for v in node:
            yield from photo_objs(v, sid)


def pick_photos(K):
    seen = set()
    for x, sid in photo_objs({k: K[k] for k in ('items', 'selected', 'final', 'history') if k in K}):
        if x['img_id'] not in seen:
            seen.add(x['img_id'])
            yield {**x, 'set': sid}


def pick_outputs(K):
    return [o for x in pick_photos(K) for o in pick_imgs(x)]


def build_pick():
    raw = wt_bytes(PICK_FILE)
    K = json.loads(raw)
    P = json.loads(wt_bytes(M3_FILE))
    PR = P['status']['production']
    assert K['round'] == 'M-4 R25' and K['mode'] == 'final' and 'items' not in K and 'key_prefix' not in K   # 定案相簿不收集回饋、不讀寫瀏覽器資料
    FN = json.loads(wt_bytes(FINAL_FILE))
    assert PR['owner_selection'] == 'complete' and PR['prepress_check'] == 'in_progress' and PR['print_approval'] == 'not_given' and PR['final_list'] == FINAL_FILE
    assert PR['layout_preview'] == 'owner_reviewed' and PR['layout_acceptance'] == 'accepted' and PR['layout_file'] == LAYOUT_FILE   # M-5 R26：排版接受與照片接受分開；R27 Penny 接受
    assert PR['layout_acceptance_record'] == COVER_OWNER and PR['cover'] == 'candidates_ready_for_owner_choice' and PR['cover_file'] == COVER_FILE   # M-5 R27：封面候選不是 Owner 接受
    assert PR['generated_cumulative'] == 85 and PR['cover_generated_log'] == {'M-5 R27': 4}   # 封面張數另計，不併入月面照片
    assert PR['pick_sets'] == [] and PR['selected_edit_sets'] == [] and PR['rejected_sets'] == [] and sorted(PR['accepted_sets']) == sorted(x['id'] for x in P['sets'])
    fin = K['final']
    assert len(fin) == 24 and [(f['book'], f['month']) for f in fin] == [(b, m) for b in 'HV' for m in range(1, 13)], '橫式、直式各 1–12 月，無缺月、無重複'
    assert [(f['set'], f['img_id'], f['src']['path'], f['src']['sha256']) for f in fin] == [(e['set'], e['img_id'], e['file'], e['sha256']) for e in FN['sets']], '相簿與唯一定案清單一致'
    plan = {x['id']: x for x in P['sets']}
    acc = PR['accepted_versions']
    for f in fin:
        q = plan[f['set']]
        assert (f['book'], f['month'], f['name']) == (q['book'], q['month'], q['name']), f['set']
        assert f['set'] not in acc or f['img_id'] == acc[f['set']], f['set']   # 選中調色／修正版的套別指向衍生檔本身
    fids = {f['img_id'] for f in fin}
    for h in K['history']:
        assert h['set'] in plan and h['photos'] and not fids & {p['img_id'] for p in h['photos']}, h['set']   # 歷史候選不混入定案
    all_ids = [x['img_id'] for x in pick_photos(K)]
    assert len(all_ids) == len(set(all_ids)) == 91   # 定案 24＋歷史候選 67
    os.makedirs(PICK_DIR, exist_ok=True)
    for fn in os.listdir(PICK_DIR):
        os.remove(os.path.join(PICK_DIR, fn))
    files = {}
    for name, data, meta in pick_outputs(K):
        with open(os.path.join(PICK_DIR, name), 'wb') as f:
            f.write(data)
        MANIFEST.append({'published': f'public/img/pick/{name}', 'sha256': sha256(data), **meta})
        im = Image.open(io.BytesIO(data))
        files.setdefault(meta['img_id'], {})[{'pick_preview': 'view', 'pick_full': 'full'}[meta['kind']]] = {
            'src': f'img/pick/{name}', 'w': im.width, 'h': im.height, 'bytes': len(data)}
    pub = json.loads(raw)
    pub.pop('note')
    for x, _ in list(photo_objs({k: pub[k] for k in ('items', 'selected', 'final', 'history') if k in pub})):
        x.pop('src')
        x['img'] = files[x['img_id']]
        assert set(x['img']) == {'view', 'full'}
    for s in pub.get('selected', []):
        assert 'img_ref' not in s or s['img_ref'] in files
    text = json.dumps(pub, ensure_ascii=False)
    for bad in ('kols/', 'job', 'soul', 'review/calendar', 'credit', '交易', '扣款', '自查', 'natural skin texture', 'she wears', 'prompt', 'png', 'nsfw'):
        assert bad not in text.lower(), bad
    assert not re.search(r'[0-9a-f]{8,}', text), '選片頁資料出現疑似 ID'
    return pub


def build_review_hist():
    H = json.loads(wt_bytes(REVIEW_HIST))
    assert [x['round'] for x in H['items']] == ['M-4 R3'] and H['items'][0]['feedback_key'] == 'cal2027-review-v1:V-iris-chen-m4r2'
    text = json.dumps(H, ensure_ascii=False)
    assert not re.search(r'[0-9a-f]{8,}', text) and not any(b in text.lower() for b in ('kols/', 'job', 'soul'))
    return H['items']


# ---------- 排版預覽頁（layout.html，M-5 R26 起）----------
# 頁面圖、比較圖與兩份 PDF 由 docs/calendar/tools/build_cal_m5_layout.py 產生在 public/layout/，檔案清單與 sha256 記在 data/cal_m5_layout_r26.json；
# 這裡只核對檔案（位元組相同、清單外不得有檔）並組出頁面資料 layout-data.js。頁面文字與選項來自人寫的 data/cal_layout_r26_page.json。
# 回饋鍵 cal2027-layout-r26-v1 只存排版回饋，與選片回饋分開；其他舊鍵不讀、不寫、不刪。公開資料不放 repo 路徑、sha256 或來源 commit。
LAYOUT_FILE = 'docs/calendar/data/cal_m5_layout_r26.json'
LAYOUT_PAGE = 'docs/calendar/data/cal_layout_r26_page.json'
LAYOUT_DIR = os.path.join(PUB, 'layout')
LAYOUT_JS_HEAD = ('// 程式產生（docs/calendar/tools/build_cal_decision_site.py），不要手改。排版預覽頁（layout.html）的資料，'
                  '來源 docs/calendar/data/cal_m5_layout_r26.json 與 cal_layout_r26_page.json\nwindow.CAL_LAYOUT = ')
LAYOUT_ROLE = {'cover': '封面', 'photo': '照片面', 'grid': '大格面', 'memo': 'MEMO', 'year': '全年年曆', 'barcode': '條碼頁（廠商固定）'}


def layout_files_diff(L):
    want = {x['path']: x['sha256'] for x in L['files']}
    disk = {}
    for d, _, fs in os.walk(LAYOUT_DIR):
        for fn in fs:
            p = os.path.join(d, fn)
            disk[os.path.relpath(p, LAYOUT_DIR)] = sha256(open(p, 'rb').read())
    return sorted(set(want.items()) ^ set(disk.items()))


def build_layout():
    L = json.loads(wt_bytes(LAYOUT_FILE))
    G = json.loads(wt_bytes(LAYOUT_PAGE))
    FN = json.loads(wt_bytes(FINAL_FILE))
    assert L['round'] == G['round'] == 'M-5 R26' and G['feedback_key'] == 'cal2027-layout-r26-v1'
    assert L['photo_source']['final_list'] == FINAL_FILE and [(s['set'], s['img_id'], s['sha256']) for s in L['photo_source']['sets']] == \
        [(s['set'], s['img_id'], s['sha256']) for s in FN['sets']], '排版用的 24 張與唯一定案清單一致'
    diff = layout_files_diff(L)
    assert not diff, f'排版預覽檔案與紀錄不同：{diff[:5]}'
    dc = L['date_check']
    assert dc['failures'] == 0 and dc['negative_test']['pass'] and dc['dates_read'] == 365 * 6 + 31, '日期讀回核對全過'
    assert [p['face'] for p in L['pages']['H']] == list(range(1, 29)) and [p['face'] for p in L['pages']['V']] == list(range(1, 33))
    assert not any(p['issues'] for k in 'HV' for p in L['pages'][k]) and not any(p['issues'] for p in L['compare_A'])
    person = {s['set']: s['person'] for s in L['photo_source']['sets']}

    def img(rel):
        im = Image.open(os.path.join(LAYOUT_DIR, rel))
        return {'src': 'layout/' + rel, 'w': im.width, 'h': im.height}

    def page(p):
        ph = next((x for x in p['photos'] if x['role'] == 'photo'), None)
        return {'face': p['face'], 'role': p['role'], 'role_zh': LAYOUT_ROLE[p['role']], 'month': p['month'], 'person': person.get(p['set']),
                'view': img(p['view']), 'full': img(p['full']), 'photo_box': ph['box_mm'] if ph else None}
    A = {p['month']: p for p in L['compare_A'] if p['variant'] == 'A'}
    mm = 104 / 1109
    months = []
    for sid, c in L['crops_H'].items():
        a = c['A']
        if a['cuts_subject_px']:
            note = f"放進 192×104 框一定會切到 {a['cuts_subject_px']} px：推薦切在髮頂（深色頭髮對夜空，約 {a['cuts_subject_px'] * mm:.1f} mm）；另一排法切鞋底。"
        elif a['extra_on_truncated_px']:
            note = f"髮頂上方空間不夠，只能裁 {a['top']} px；其餘 {a['bottom']} px 從下緣裁。{c['visual_note']}，所以會再多裁約 {a['bottom'] * mm:.1f} mm。"
        else:
            note = '只裁掉頭頂上方的空白，人物不受影響。'
        months.append({'month': c['month'], 'set': sid, 'person': person[sid], 'A': page(A[c['month']]), 'note': note})
    lab = {'B': '完整 16:9（推薦）', 'A': '192×104 套框', 'A2': '192×104 套框・另一排法'}
    zooms = []
    for z in L['zooms']:
        g = next((x for x in zooms if x['set'] == z['set']), None)
        if g is None:
            g = {'set': z['set'], 'person': person[z['set']], 'month': L['crops_H'][z['set']]['month'], 'rows': {}}
            zooms.append(g)
        g['rows'].setdefault(z['edge'], []).append({'variant': z['variant'], 'label': lab[z['variant']], **img(z['file'])})
    pdf = {}
    for k in 'HV':
        f = L['formats'][k]
        name = f'cal2027_{k}_layout_preview_R26.pdf'
        pdf[k] = {'href': 'layout/' + name, 'size_mb': round(os.path.getsize(os.path.join(LAYOUT_DIR, name)) / 1048576, 1), 'pages': L['pdf'][k]['pages'],
                  'trim': f"{f['W'] - 2 * f['trim']}×{f['H'] - 2 * f['trim']} mm", 'canvas': f"{f['W']}×{f['H']} mm"}
    fmts = {k: {x: L['formats'][k][x] for x in ('zh', 'W', 'H', 'trim', 'coil_assumed', 'coil_measured')} |
            {'safe': L['formats'][k]['vendor_safe' if k == 'H' else 'text_safe'],
             'safe_label': '廠商安全框' if k == 'H' else '文字安全區（本案自訂；廠商安全框為 0）'} for k in 'HV'}
    pub = {**{k: G[k] for k in ('task', 'round', 'title', 'intro', 'status_note', 'feedback_key', 'decisions', 'pending', 'recommended', 'vendor')},
           'pdf': pdf, 'formats': fmts, 'pages': {k: [page(p) for p in L['pages'][k]] for k in 'HV'},
           'compare': {'months': months, 'zooms': zooms},
           'date_note': f"日期已從輸出的 PDF 逐格讀回核對：{dc['dates_read']} 個日期、錯誤 {dc['failures']}。"}
    text = json.dumps(pub, ensure_ascii=False)
    for bad in ('kols/', 'job', 'soul', 'review/calendar', 'credit', 'prompt', 'docs/'):
        assert bad not in text.lower(), bad
    assert not re.search(r'[0-9a-f]{8,}', text), '排版頁資料出現疑似 ID'
    return pub


# ---------- 封面候選（layout.html 上方的封面比較區，M-5 R27 起）----------
# 封面頁面圖、原圖（無文字、無中繼資料）與臉部對照圖由 docs/calendar/tools/build_cal_m5_cover.py 產生在 public/cover/，
# 檔案清單與 sha256 記在 data/cal_m5_cover_r27.json；逐張驗收在 data/cal_m5_r27_trial.json；頁面文字在人寫的 data/cal_cover_r27_page.json。
# 回饋鍵 cal2027-cover-r27-v1 只存封面選擇；新候選不自動記為 Owner 接受。公開資料不放 prompt、repo 路徑、sha256 或平台 ID。
COVER_FILE = 'docs/calendar/data/cal_m5_cover_r27.json'
COVER_PAGE = 'docs/calendar/data/cal_cover_r27_page.json'
COVER_TRIAL = 'docs/calendar/data/cal_m5_r27_trial.json'
COVER_IDENT = 'docs/calendar/data/cal_m5_r27_identity.json'
COVER_OWNER = 'docs/calendar/data/cal_m5_owner_r27.json'
COVER_DIR = os.path.join(PUB, 'cover')
COVER_JS_HEAD = ('// 程式產生（docs/calendar/tools/build_cal_decision_site.py），不要手改。排版頁（layout.html）封面比較區的資料，'
                 '來源 docs/calendar/data/cal_m5_cover_r27.json、cal_m5_r27_trial.json 與 cal_cover_r27_page.json\nwindow.CAL_COVER = ')
CHECK_MARK = {'pass': '通過', 'partial': '部分', 'fail': '未通過'}


def cover_files_diff(C):
    want = {x['path']: x['sha256'] for x in C['files']}
    disk = {fn: sha256(open(os.path.join(COVER_DIR, fn), 'rb').read()) for fn in os.listdir(COVER_DIR)} if os.path.isdir(COVER_DIR) else {}
    return sorted(set(want.items()) ^ set(disk.items()))


def build_cover():
    C = json.loads(wt_bytes(COVER_FILE))
    G = json.loads(wt_bytes(COVER_PAGE))
    T = json.loads(wt_bytes(COVER_TRIAL))
    ID = json.loads(wt_bytes(COVER_IDENT))
    O = json.loads(wt_bytes(COVER_OWNER))
    assert C['round'] == G['round'] == T['round'] == ID['round'] == O['round'] == 'M-5 R27' and G['feedback_key'] == 'cal2027-cover-r27-v1'
    assert O['layout_acceptance']['page_version'].startswith('5a82bf9') and [x['set'] for x in ID['rows']] == list(T['covers']['H-A']['identity'])
    diff = cover_files_diff(C)
    assert not diff, f'封面檔案與紀錄不同：{diff[:5]}'
    assert [c['id'] for c in C['covers']] == list(T['covers']) == ['H-A', 'H-B', 'V-A', 'V-B'] and not any(c['issues'] for c in C['covers'])
    gen = T['generation']
    assert gen['covers'] == gen['requests'] == 4 and gen['retries'] == gen['extra_generation'] == 0 and gen['credits'] <= gen['credit_cap'] == 16
    assert T['summary']['finalizable_covers'] == 0 and not any(c['finalizable'] for c in T['covers'].values()), '身分未全數確認，不能標為可定案'
    name = {x['set']: x['name'].split()[0] for x in ID['rows']}

    def img(fn):
        im = Image.open(os.path.join(COVER_DIR, fn))
        return {'src': 'cover/' + fn, 'w': im.width, 'h': im.height}
    cards = {'H': [], 'V': []}
    for cv in C['covers']:
        t = T['covers'][cv['id']]
        n = t['identity_counts']
        cards[cv['kind']].append({
            'id': cv['id'], 'dir': cv['direction'], 'dir_zh': G['directions'][cv['direction']],
            'page': {'view': img(f"cover_{cv['id']}_v.jpg"), 'full': img(f"cover_{cv['id']}_f.jpg")},
            'photo': img(f"photo_{cv['id']}.jpg"), 'ids': img(f"ids_{cv['id']}.jpg"),
            'verdict': t['verdict'], 'counts': {g: n[g] for g in T['grades']},
            'flagged': [{'name': name[p], 'grade': v['grade']} for p, v in t['identity'].items() if v['grade'] in ('不符', '無法判定')],
            'checks': [{'item': r['item'], 'result': CHECK_MARK[r['result']], 'note': r['note']} for r in t['checks']],
            'people': [{'name': name[p], 'grade': v['grade'], 'note': v['note']} for p, v in t['identity'].items()],
        })
    fm = {k: {x: C['formats'][k][x] for x in ('zh', 'W', 'H', 'trim', 'coil_assumed', 'safe', 'safe_label')} for k in 'HV'}
    pub = {**{k: G[k] for k in ('task', 'round', 'title', 'intro', 'feedback_key', 'cover_status', 'cover_note', 'options', 'accepted', 'history_label', 'r26_cover_label')},
           'formats': fm, 'cards': cards, 'grades': T['grades'],
           'summary': T['summary']['statement'],
           'made': f"{gen['covers']} 張候選（橫式、直式各 A／B），每張 1 次生成、沒有重試或補生；12 位用各自的身分參考圖一起送入。"}
    text = json.dumps(pub, ensure_ascii=False)
    for bad in ('kols/', 'job', 'soul', 'review/calendar', 'credit', 'prompt', 'docs/', 'nano', 'media', 'image 1', 'she wears'):
        assert bad not in text.lower(), bad
    assert not re.search(r'[0-9a-f]{8,}', text), '封面資料出現疑似 ID'
    return pub


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
        'review_hist': build_review_hist(),
        'images': IMAGES,
    }
    review = build_review()
    pick = build_pick()
    lay = build_layout()
    with open(os.path.join(PUB, 'layout-data.js'), 'w', encoding='utf-8') as f:
        f.write(LAYOUT_JS_HEAD + json.dumps(lay, ensure_ascii=False, indent=1, sort_keys=True) + ';\n')
    with open(os.path.join(PUB, 'cover-data.js'), 'w', encoding='utf-8') as f:
        f.write(COVER_JS_HEAD + json.dumps(build_cover(), ensure_ascii=False, indent=1, sort_keys=True) + ';\n')
    with open(os.path.join(PUB, 'pick-data.js'), 'w', encoding='utf-8') as f:
        f.write('// 程式產生（docs/calendar/tools/build_cal_decision_site.py），不要手改。選片頁（shoot.html）的資料，來源 docs/calendar/data/cal_pick_r25.json（定案相簿）\n')
        f.write('window.CAL_PICK = ' + json.dumps(pick, ensure_ascii=False, indent=1, sort_keys=True) + ';\n')
    with open(os.path.join(PUB, 'review-data.js'), 'w', encoding='utf-8') as f:
        f.write('// 程式產生（docs/calendar/tools/build_cal_decision_site.py），不要手改。目前檢視頁（shoot.html）的資料，來源 docs/calendar/data/cal_review_current.json\n')
        f.write('window.CAL_REVIEW = ' + json.dumps(review, ensure_ascii=False, indent=1, sort_keys=True) + ';\n')
    with open(os.path.join(PUB, 'data.js'), 'w', encoding='utf-8') as f:
        f.write('// 程式產生（docs/calendar/tools/build_cal_decision_site.py），不要手改。資料來源：固定成果 commit ' + FIXED + '\n')
        f.write('window.CAL_DATA = ' + json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + ';\n')
    man = {'generated_by': 'docs/calendar/tools/build_cal_decision_site.py', 'fixed_sha': FIXED,
           'note': '只發佈下列檔案。copy＝與固定 commit 的同一路徑位元組相同（source_blob＝git blob）；crop＝從固定 commit 的拼圖純裁切（低解析選圖參考）；hires_preview＝可核對來源的原圖等比縮小（不含 job_id）；thumbnail＝等比縮小；review_*＝M-4 R5 檢視頁的照片（review_png 只移除 PNG 文字中繼資料區塊、review_preview 等比縮小、review_copy 位元組不變）；pick_*＝選片頁的照片（pick_preview 等比縮小、pick_full 原尺寸 JPEG，皆不帶中繼資料）。沒有生成、外擴、增強或修圖。本檔不對外提供。',
           'files': MANIFEST}
    with open(os.path.join(SITE, 'ASSET_MANIFEST.json'), 'w', encoding='utf-8') as f:
        json.dump(man, f, ensure_ascii=False, indent=1)
        f.write('\n')
    hits = scan_public(public_secrets())
    assert not hits, f'公開檔含私有識別碼：{hits}'
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
    RV = {f'public/img/review/{n}': (d, m) for n, d, m in review_outputs(json.loads(wt_bytes(REVIEW_FILE)))}
    PK = {f'public/img/pick/{n}': (d, m) for n, d, m in pick_outputs(json.loads(wt_bytes(PICK_FILE)))}
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
        if e['kind'].startswith('review_'):
            if e['published'] not in RV or RV[e['published']][0] != data or RV[e['published']][1]['kind'] != e['kind']:
                print('目前檢視頁圖片無法重現', e['published']); bad += 1
        if e['kind'].startswith('pick_'):
            if e['published'] not in PK or PK[e['published']][0] != data or PK[e['published']][1]['kind'] != e['kind'] or Image.open(io.BytesIO(data)).info.get('exif'):
                print('選片頁圖片無法重現', e['published']); bad += 1
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
    for d in ('z', 't', 'review', 'pick'):
        for fn in os.listdir(os.path.join(PUB, 'img', d)):
            on_disk.add(f'img/{d}/{fn}')
    extra = on_disk - listed
    if extra:
        print('manifest 以外的圖片：', sorted(extra)); bad += 1
    if set(RV) - {e['published'] for e in man['files']}:
        print('目前檢視頁圖片未發佈：', sorted(set(RV) - {e['published'] for e in man['files']})); bad += 1
    if set(PK) - {e['published'] for e in man['files']}:
        print('選片頁圖片未發佈：', sorted(set(PK) - {e['published'] for e in man['files']})); bad += 1
    LY = json.loads(wt_bytes(LAYOUT_FILE))
    ld = layout_files_diff(LY)
    if ld:
        print('排版預覽檔案與紀錄不同：', ld[:5]); bad += 1
    try:
        lay_js = LAYOUT_JS_HEAD + json.dumps(build_layout(), ensure_ascii=False, indent=1, sort_keys=True) + ';\n'
        if open(os.path.join(PUB, 'layout-data.js'), encoding='utf-8').read() != lay_js:
            print('layout-data.js 無法重現'); bad += 1
    except AssertionError as e:
        print('排版預覽資料檢查失敗：', e); bad += 1
    CV = json.loads(wt_bytes(COVER_FILE))
    cd = cover_files_diff(CV)
    if cd:
        print('封面檔案與紀錄不同：', cd[:5]); bad += 1
    try:
        cov_js = COVER_JS_HEAD + json.dumps(build_cover(), ensure_ascii=False, indent=1, sort_keys=True) + ';\n'
        if open(os.path.join(PUB, 'cover-data.js'), encoding='utf-8').read() != cov_js:
            print('cover-data.js 無法重現'); bad += 1
    except AssertionError as e:
        print('封面資料檢查失敗：', e); bad += 1
    hits = scan_public(public_secrets())
    if hits:
        print('公開檔含私有識別碼：', hits); bad += 1
    pubtext = ''.join(open(os.path.join(PUB, f), encoding='utf-8').read() for f in os.listdir(PUB) if f.endswith(('.js', '.html', '.css')))
    if TX_RAW.search(pubtext):
        print('公開檔出現交易原始資料：', TX_RAW.search(pubtext).group(0)); bad += 1
    n = {k: sum(e['kind'] == k for e in man['files']) for k in ('copy', 'crop', 'hires_preview', 'thumbnail')}
    nr = sum(e['kind'].startswith('review_') for e in man['files'])
    npk = sum(e['kind'].startswith('pick_') for e in man['files'])
    print(f'{"FAIL" if bad else "PASS"}: {len(man["files"])} 檔（copy {n["copy"]}、crop {n["crop"]}、高解析預覽 {n["hires_preview"]}、thumbnail {n["thumbnail"]}、舊檢視頁 {nr}、選片頁 {npk}）＋排版預覽 {len(LY["files"])} 檔＋封面候選 {len(CV["files"])} 檔，問題 {bad}；公開檔無私有識別碼、無交易原始資料'
          + (f'；未提供快取、只核對 sha256 的高解析預覽：{", ".join(not_recomputed)}' if not_recomputed else ''))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
