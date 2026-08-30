#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 ChatGPT 已認可的相容集合內，重排來源以最大化「最接近那一對」的實測距離。

為什麼要這支：R7 的分配表是按「幾何相符」排的，沒有按「彼此分得夠不夠開」排。
emma-kao ↔ wendy-yeo 兩位都符合各自的規格，卻生出同一張臉——
分離度是獨立於相符度的另一個條件，得另外最佳化。

距離定義與 tools/measure_fed_geometry.py 相同：量的是實際餵進去的裁切的形狀比例，
不是規格形容詞。門檻 1.02 由兩次實測外推（見 review/SEPARATION_TEST.md）。
"""
import json, itertools, random, sys
from collections import defaultdict
import numpy as np

sys.path.insert(0, 'tools')
SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
CAP = {'FACE_SHAPE_AND_JAW': 2, 'EYES_AND_BROWS': 3, 'NOSE': 3, 'MOUTH': 3}
FROM = {'FACE_SHAPE_AND_JAW': ['face_hw', 'jaw_ratio', 'third_mid', 'third_low'],
        'EYES_AND_BROWS': ['eye_space', 'eye_open'],
        'NOSE': ['alar_r'], 'MOUTH': ['mouth_r', 'lip_r']}
AX = [a for v in FROM.values() for a in v]
THRESHOLD = 1.02

g = json.load(open('pilot/ref_geometry.json', encoding='utf-8'))
DB = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
man = json.load(open('pilot/face_crops_manifest.json', encoding='utf-8'))['artifacts']
V = json.load(open('pilot/crop_spec.json', encoding='utf-8'))['crop_spec_version']
pids = sorted(DB['personas'])
cur = {p: dict(DB['personas'][p]['refs_v2']) for p in pids}

# 相容集合：直接沿用 solve_source_assignment.py 裡 ChatGPT 自己講過的相容性，
# 再加上 R7 已批准的現行分配（那些依定義相容）。
import solve_source_assignment as S
COMPAT = {k: set(v) for k, v in S.COMPAT.items()}
for p in pids:
    for s in SL:
        COMPAT.setdefault((p, s), set()).add(cur[p][s])
for k in list(COMPAT):
    COMPAT[k] = {r for r in COMPAT[k]
                 if man.get(f'{r}__{k[1]}__{V}', {}).get('qa_status') == 'pass'}

sd0 = np.array([[g[cur[p][s]][a] for s, ax in FROM.items() for a in ax]
                for p in pids]).std(0, ddof=1)

def Z(asg):
    return np.array([[g[asg[p][s]][a] for s, ax in FROM.items() for a in ax]
                     for p in pids]) / sd0

def pair_dists(asg):
    z = Z(asg)
    return {(pids[i], pids[j]): float(np.linalg.norm(z[i] - z[j]) / np.sqrt(len(AX)))
            for i, j in itertools.combinations(range(len(pids)), 2)}

def score(asg):
    """(最小配對距離, 低於門檻的組數的負值) —— 先推高最差的一對，再減少不合格組數。"""
    d = pair_dists(asg)
    return (min(d.values()), -sum(1 for v in d.values() if v < THRESHOLD))

def legal(asg):
    for p in pids:
        if len(set(asg[p].values())) != 4:
            return False
    for s in SL:
        c = defaultdict(int)
        for p in pids:
            c[asg[p][s]] += 1
        if max(c.values()) > CAP[s]:
            return False
    return True

best = {p: dict(cur[p]) for p in pids}
bs = score(best)
print(f'現行（R7 已批准）：最小配對 {bs[0]:.3f}，低於 {THRESHOLD} 的有 {-bs[1]} 組')

random.seed(11)
for restart in range(8):
    a = {p: dict(best[p]) for p in pids}
    cs = score(a)
    for _ in range(12000):
        p = random.choice(pids); s = random.choice(SL)
        opts = COMPAT.get((p, s), set()) - {a[p][s]}
        if not opts:
            continue
        old = a[p][s]; a[p][s] = random.choice(sorted(opts))
        if not legal(a):
            a[p][s] = old; continue
        v = score(a)
        if v > cs: cs = v
        else: a[p][s] = old
    if cs > bs:
        bs = cs; best = {p: dict(a[p]) for p in pids}
    print(f'  restart {restart+1}: 最小配對 {cs[0]:.3f}，低於門檻 {-cs[1]} 組')

d = pair_dists(best)
changed = [(p, s, cur[p][s], best[p][s]) for p in pids for s in SL if cur[p][s] != best[p][s]]
print(f'\n最佳解：最小配對 {bs[0]:.3f}，低於門檻 {-bs[1]} 組，改動 {len(changed)} 格')
for p, s, o, n in changed:
    print(f'  {p:18s} {s:20s} {o} → {n}')
low = sorted((v, k) for k, v in d.items() if v < THRESHOLD)
if low:
    print(f'\n仍低於 {THRESHOLD} 的配對：')
    for v, k in low:
        print(f'  {v:.2f}  {k[0]} ↔ {k[1]}')
json.dump({p: best[p] for p in pids},
          open('pilot/proposed_assignment_sep.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('\n→ pilot/proposed_assignment_sep.json')
