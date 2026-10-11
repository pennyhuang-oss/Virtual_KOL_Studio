#!/usr/bin/env python3
"""TASK-CAL-001 — 2027 KOL 桌曆決策頁的素材與資料。

所有圖片與資料一律從固定成果 commit（FIXED）讀取（git show），不讀工作目錄、不讀分支頭。
- 整張複製：位元組不變，manifest 記錄來源路徑與 git blob。
- 裁切：從固定 commit 的決策拼圖裁出單張照片（只裁切、四邊內縮 2 px 避開拼貼邊界，重新存成 JPEG q95），manifest 記錄裁切框。
- 縮圖：上面兩者的等比縮小（Lanczos，JPEG q82），只給卡片顯示；點開放大一律看原檔或裁切檔。
- 高解析預覽（替代照片）：來源只限可核對的既有檔——固定 commit 的 repo 檔（git blob）、R2 已取回的 Higgsfield 快取
  （data/cal_r2_hf_retrieved.json 的 sha256）、R3 清理輸出（data/cal_r3_cleanup_report.json 的 clean_sha256）。
  只做等比縮小（長邊 1600 px，JPEG q88，不帶原檔中繼資料）。頁面資料只放圖片 ID，不放 job_id、來源路徑或帳號資料。
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
    if rel.startswith(('r3/pages/hires/', 'r3/compare/hires/', 'r3/checks/hires/')):
        return 'page300'
    if rel.startswith('r3/previews/'):
        return 'preview100'
    return 'sheet'


def put(iid, data, thumb_box, meta, res, extra=None):
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
    if meta['kind'] != 'hires_preview':
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


# ---------- 資料 ----------

def load_json(rel):
    return json.loads(git_bytes(rel))


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
    not_recomputed = []
    for e in man['files']:
        p = os.path.join(SITE, e['published'])
        listed.add(os.path.relpath(p, PUB))
        data = open(p, 'rb').read()
        if sha256(data) != e['sha256']:
            print('sha256 不符', e['published']); bad += 1
        if e['kind'] == 'copy':
            if blob_of(data) != e['source_blob'] or git_blob(e['source'][len(CAL):]) != e['source_blob']:
                print('與固定 commit 不同', e['published']); bad += 1
        if e['kind'] == 'crop':
            src = Image.open(io.BytesIO(git_bytes(e['source'][len(CAL):]))).convert('RGB')
            if jpeg(src.crop(tuple(e['box_px'])), 95) != data:
                print('裁切無法重現', e['published']); bad += 1
        if e['kind'] == 'hires_preview':
            needs_cache = not e['source'].startswith('repo@')
            if needs_cache and not (hf_dir and clean_dir):
                not_recomputed.append(e['cid'])
            elif hires_bytes(hires_source(e['cid'], J, R, C, hf_dir, clean_dir)[0])[0] != data:
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
