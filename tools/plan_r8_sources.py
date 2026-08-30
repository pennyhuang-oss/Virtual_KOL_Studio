#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 19 位的目標幾何排成一組要生的參考圖規格。

結構沿用 ref_30–33 的做法：一張圖同時供應四個不同人物的四個不同槽位，
所以沒有任何一張圖等於任何一位人物的完整長相。

用循環錯位保證：第 k 張圖帶 persona k 的臉、k+1 的眼、k+2 的鼻、k+3 的口。
於是 persona k 的四槽分別來自第 k、k-1、k-2、k-3 張圖——四張互異，
而且每張圖的每個槽位只被用一次，所有上限自動滿足。
"""
import json, itertools
import numpy as np

AX = ['face_hw', 'jaw_ratio', 'third_mid', 'third_low',
      'eye_space', 'eye_open', 'alar_r', 'mouth_r', 'lip_r']
# derive_geometry_targets.py 內部用「上庭高度＋中庭佔比」避免三庭加不起來，
# 這裡換回三庭本身，因為要圖的人看的是三庭。
SLOT_AX = {'FACE_SHAPE_AND_JAW': ['face_hw', 'jaw_ratio', 'third_mid', 'third_low'],
           'EYES_AND_BROWS': ['eye_space', 'eye_open'],
           'NOSE': ['alar_r'], 'MOUTH': ['mouth_r', 'lip_r']}
SL = list(SLOT_AX)
OFF = {'FACE_SHAPE_AND_JAW': 0, 'EYES_AND_BROWS': 1, 'NOSE': 2, 'MOUTH': 3}

T = json.load(open('pilot/geometry_targets.json', encoding='utf-8'))
D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
pids = sorted(D['personas'])
N = len(pids)
tgt = {p: dict(v, **T['thirds'][p]) for p, v in T['targets'].items()}

# 第 k 張圖：臉取 pids[k]、眼取 pids[k+1]、鼻取 pids[k+2]、口取 pids[k+3]
images, assign = {}, {}
for k in range(N):
    rid = f'ref_{40 + k}'
    images[rid] = {slot: {'for_persona': pids[(k + OFF[slot]) % N],
                          'targets': {a: round(tgt[pids[(k + OFF[slot]) % N]][a], 3)
                                      for a in SLOT_AX[slot]}}
                   for slot in SL}
for k, p in enumerate(pids):
    assign[p] = {slot: f'ref_{40 + (k - OFF[slot]) % N}' for slot in SL}

# 驗：四槽互異、每個 (來源,槽) 只被一位用、達成的分離度
bad = [p for p in pids if len(set(assign[p].values())) != 4]
use = {}
for p in pids:
    for s, r in assign[p].items():
        use.setdefault((r, s), []).append(p)
over = {k: v for k, v in use.items() if len(v) > 1}
M = np.array([[tgt[p][a] for a in AX] for p in pids])
G = json.load(open('pilot/ref_geometry.json', encoding='utf-8'))
sd = np.array([[G[D['personas'][p]['refs_v2'][next(s for s in SL if a in SLOT_AX[s])]][a]
                for a in AX] for p in pids]).std(0, ddof=1)
Z = M / sd
mind = min(np.linalg.norm(Z[i] - Z[j]) / np.sqrt(len(AX))
           for i, j in itertools.combinations(range(N), 2))
print(f'要生的圖：{N} 張（ref_40–ref_{40+N-1}）')
print(f'四槽互異違規：{len(bad)}；(來源,槽) 重用違規：{len(over)}')
print(f'若每張都命中目標，171 組的最小配對距離：{mind:.3f}（門檻 {T["threshold"]}）')
json.dump({'images': images, 'assignment': assign,
           'min_pair_if_hit': float(mind), 'threshold': T['threshold']},
          open('pilot/r8_source_plan.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('→ pilot/r8_source_plan.json')
