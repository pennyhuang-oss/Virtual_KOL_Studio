#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 R7 §5（ChatGPT L-02 已批准）的 76 格分配寫進 batch3_faces_v2.json 的 refs_v2。

三道硬檢查，任何一道不過就 exit 1 且不寫檔：
  1. 每位 persona 的四個槽必須是四個相異來源
  2. FACE_SHAPE_AND_JAW ≤2 人、EYES/NOSE/MOUTH ≤3 人
  3. 每個 (ref, slot) 都必須有 qa_status == "pass" 的 crop
"""
import json, sys
from collections import defaultdict

SLOTS = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
CAP = {'FACE_SHAPE_AND_JAW': 2, 'EYES_AND_BROWS': 3, 'NOSE': 3, 'MOUTH': 3}
SPEC = json.load(open('pilot/crop_spec.json', encoding='utf-8'))
V = SPEC['crop_spec_version']

board = json.load(open('pilot/proposed_assignment_r7.json', encoding='utf-8'))
D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
man = json.load(open('pilot/face_crops_manifest.json', encoding='utf-8'))['artifacts']

fail = []
per = defaultdict(dict)
for key, ref in board.items():
    pid, slot = key.split('|')
    per[pid][slot] = ref

# 1. 涵蓋率與相異性
for pid in D['personas']:
    got = per.get(pid, {})
    miss = [s for s in SLOTS if s not in got]
    if miss:
        fail.append(f'{pid}：缺 {", ".join(miss)}')
        continue
    if len(set(got.values())) != 4:
        fail.append(f'{pid}：四槽來源不相異 {got}')
extra = set(per) - set(D['personas'])
if extra:
    fail.append(f'分配表出現未知 persona：{sorted(extra)}')

# 2. 來源上限
use = defaultdict(lambda: defaultdict(list))
for pid, got in per.items():
    for slot, ref in got.items():
        use[slot][ref].append(pid)
for slot, refs in use.items():
    for ref, pids in refs.items():
        if len(pids) > CAP[slot]:
            fail.append(f'{slot} / {ref} 被 {len(pids)} 人使用，超過上限 {CAP[slot]}：{pids}')

# 3. crop 必須存在且 QA 通過
for pid, got in per.items():
    for slot, ref in got.items():
        k = f'{ref}__{slot}__{V}'
        a = man.get(k)
        if a is None:
            fail.append(f'{pid} / {slot}：{k} 沒有 crop')
        elif a['qa_status'] != 'pass':
            fail.append(f'{pid} / {slot}：{k} QA 未通過（{"；".join(a["qa_reasons"])}）')

if fail:
    print(f'✗ {len(fail)} 項不通過，未寫檔：')
    for f in fail:
        print('  ' + f)
    sys.exit(1)

for pid, got in per.items():
    D['personas'][pid]['refs_v2'] = {s: got[s] for s in SLOTS}
D['_r7'] = {
    'source': 'review/REVIEW_BATCH3_FACES_R7.md L-02（ChatGPT 已批准，無幾何異議）',
    'assigned_slots': len(board),
    'new_sources': ['ref_30', 'ref_31', 'ref_32', 'ref_33'],
    'applied_by': 'tools/apply_r7_assignment.py',
}
json.dump(D, open('pilot/batch3_faces_v2.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print(f'✓ 已寫入 {len(board)} 格 → refs_v2')
for slot in SLOTS:
    print(f'  {slot:20s} 用到 {len(use[slot]):2d} 個來源，單一來源最多 {max(len(v) for v in use[slot].values())}／{CAP[slot]} 人')
