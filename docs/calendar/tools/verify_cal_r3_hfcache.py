#!/usr/bin/env python3
"""TASK-CAL-001 / R3 — 核對已取回的 Higgsfield 原圖（本機快取）：檔案在、可解碼、尺寸對、sha256 對；並寫入完整 sha256。

不連網、不重新下載。R2 只記了 sha256 前 16 碼；本程式先確認前 16 碼相符，才把完整 64 碼寫回
data/cal_r2_hf_retrieved.json。也確認 judgments／face_pairs 裡每個 hf:<job_id> 都能在紀錄中定位。
用法：python3 docs/calendar/tools/verify_cal_r3_hfcache.py --hf-dir <取回原圖的資料夾>
"""
import argparse
import datetime as dt
import hashlib
import json
import os

from PIL import Image

CAL = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REC = os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hf-dir', required=True)
    a = ap.parse_args()
    raw = open(REC).read()
    R = json.loads(raw)
    bad = []
    for it in R['items']:
        p = os.path.join(a.hf_dir, it['local'])
        if not os.path.exists(p):
            bad.append((it['job_id'], 'missing'))
            continue
        h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        if not h.startswith(it['sha256'][:16]):
            bad.append((it['job_id'], 'sha256 mismatch'))
            continue
        with Image.open(p) as im:
            im.load()
            if list(im.size) != list(it['px']):
                bad.append((it['job_id'], f'size {im.size} != {it["px"]}'))
                continue
        it['sha256'] = h
        it['bytes'] = os.path.getsize(p)
    ids = {it['job_id'] for it in R['items']}
    refs = []
    for name in ('cal_r2_judgments.json', 'cal_r2_face_pairs.json', 'cal_r3_picks.json'):
        fp = os.path.join(CAL, 'data', name)
        if os.path.exists(fp):
            refs += [s[3:] for s in json.dumps(json.load(open(fp))).replace('"', ' ').split() if s.startswith('hf:')]
    unresolved = sorted({r.rstrip(',') for r in refs} - ids)
    R['cache_check'] = {'checked_on': dt.date.today().isoformat(), 'items': len(R['items']),
                        'ok': len(R['items']) - len(bad), 'problems': bad, 'unresolved_hf_refs': unresolved,
                        'note': '本機快取逐檔核對：存在、可解碼、尺寸與紀錄相同、sha256 與 R2 紀錄的前 16 碼相同後寫入完整 64 碼；未重新下載。'}
    open(REC, 'w').write(json.dumps(R, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else ''))
    print('ok', len(R['items']) - len(bad), 'problems', bad, 'unresolved', unresolved)


if __name__ == '__main__':
    main()
