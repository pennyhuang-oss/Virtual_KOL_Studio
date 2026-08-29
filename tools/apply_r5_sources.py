#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""套用 ChatGPT R5 的 J-03／J-04／J-08 來源重配到 refs_v2。

衝突時以 J-08 為準——它是最後一版，且明說「為避免同一 persona 重複來源」而做的連動。
"""
import json, sys
from collections import Counter

F = 'pilot/batch3_faces_v2.json'
D = json.load(open(F, encoding='utf-8'))
P = D['personas']
M = json.load(open('pilot/face_crops_manifest.json', encoding='utf-8'))['artifacts']
V = json.load(open('pilot/crop_spec.json', encoding='utf-8'))['crop_spec_version']

NEW = {
 'EYES_AND_BROWS': {
   'tammy-chou': 'ref_26', 'zoey-yeh': 'ref_21', 'kanon-komori': 'ref_21',
   'jia-seo': 'ref_17', 'zhiyi-shen': 'ref_16', 'wanyin-jiang': 'ref_24',
   'wendy-yeo': 'ref_29', 'peggy-lee': 'ref_27', 'angeline-kwee': 'ref_25'},
 'NOSE': {
   'tammy-chou': 'ref_18', 'zoey-yeh': 'ref_18', 'rin-ayase': 'ref_19',
   'yerin-han': 'ref_19', 'ruoruo-tang': 'ref_16', 'cheryl-soh': 'ref_24',
   'sydney-leong': 'ref_18', 'zhiyi-shen': 'ref_17', 'wanyin-jiang': 'ref_17',
   'wendy-yeo': 'ref_17', 'angeline-kwee': 'ref_24'},
 'MOUTH': {
   'angel-chiu': 'ref_18', 'nanami-fujiwara': 'ref_18', 'kanon-komori': 'ref_22',
   'jia-seo': 'ref_28', 'zhiyi-shen': 'ref_25', 'wanyin-jiang': 'ref_25',
   'peggy-lee': 'ref_26', 'somi-oh': 'ref_26', 'wendy-yeo': 'ref_19',
   'angeline-kwee': 'ref_16'},
}
CAP = {'FACE_SHAPE_AND_JAW': 2, 'EYES_AND_BROWS': 3, 'NOSE': 3, 'MOUTH': 3}

changed = 0
for slot, mp in NEW.items():
    for pid, ref in mp.items():
        r = P[pid].setdefault('refs_v2', dict(P[pid]['refs']))
        if r.get(slot) != ref:
            r[slot] = ref; changed += 1

err = []
# 1. 每位四槽必須四張不同圖（ChatGPT J-05 的 HARD FAIL）
for pid, d in P.items():
    r = d['refs_v2']
    if len(set(r.values())) < 4:
        dup = [k for k, v in Counter(r.values()).items() if v > 1]
        err.append(f'{pid} 的四槽有重複來源 {dup}：{r}')
# 2. slot cap
for slot, cap in CAP.items():
    c = Counter(P[p]['refs_v2'][slot] for p in P)
    for k, v in c.items():
        if v > cap:
            err.append(f'{slot} 的 {k} 供給 {v} 位，超過 cap {cap}：'
                       f'{[p for p in P if P[p]["refs_v2"][slot]==k]}')
# 3. 每個指派都要有通過 QA 的 crop
for pid, d in P.items():
    for slot, ref in d['refs_v2'].items():
        k = f'{ref}__{slot}__{V}'
        if k not in M:
            err.append(f'{pid}.{slot} → {ref}：還沒有裁切件 {k}')
        elif M[k]['qa_status'] == 'fail':
            err.append(f'{pid}.{slot} → {ref}：裁切 QA 未過（{M[k]["qa_reasons"][0]}）')

print(f'套用 R5 來源重配：{changed} 項變更')
for e in err:
    print('  ✗ ', e)
if err:
    print(f'\nHARD FAIL：{len(err)} 項。未寫入。')
    sys.exit(1)

for slot, cap in CAP.items():
    c = Counter(P[p]['refs_v2'][slot] for p in P)
    print(f'  {slot:20s} 用了 {len(c)} 張來源，最高集中 {max(c.values())}/{cap}')
old = sum(1 for p in P for v in P[p]['refs_v2'].values() if v < 'ref_16')
print(f'  仍指向舊 15 張真人照的指派：{old}')
D['_r5_sources'] = {
  '_source': 'ChatGPT R5 J-03／J-04／J-08。衝突以 J-08 為準。',
  '_gate': '每位四槽互異、slot cap（臉型 2／其餘 3）、每個指派都對應通過 QA 的 crop。',
}
json.dump(D, open(F, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('  ✓ 已寫入 refs_v2')
