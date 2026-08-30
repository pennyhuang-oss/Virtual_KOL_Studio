#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""量測「實際會被餵進去的幾何」的人物間分離度。

K-05 的舊註冊表量的是 spec 文字之間的距離，那次 4 張臉零碰撞卻長得一模一樣。
這支量的是每位 persona 四個指定來源上實測到的形狀比例，
所以它跟輸出的關聯是直接的，不經過形容詞。
"""
import json, sys, itertools
import numpy as np

GEOM = sys.argv[1] if len(sys.argv) > 1 else 'pilot/ref_geometry.json'
# 哪個槽位負責哪些量測軸
FROM = {
    'FACE_SHAPE_AND_JAW': ['face_hw', 'jaw_ratio', 'third_mid', 'third_low'],
    'EYES_AND_BROWS':     ['eye_space', 'eye_open'],
    'NOSE':               ['alar_r'],
    'MOUTH':              ['mouth_r', 'lip_r'],
}
AX = [a for v in FROM.values() for a in v]

g = json.load(open(GEOM, encoding='utf-8'))
D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))

vec = {}
for pid, d in D['personas'].items():
    r = d['refs_v2']
    vec[pid] = np.array([g[r[slot]][a] for slot, axes in FROM.items() for a in axes])

M = np.array([vec[p] for p in sorted(vec)])
sd = M.std(axis=0, ddof=1)
pids = sorted(vec)

print('每軸在 19 位人物間的標準差（以合成池 ref_16-33 的量測為單位）')
for a, s, lo, hi in zip(AX, sd, M.min(axis=0), M.max(axis=0)):
    print(f'  {a:11s} sd={s:.4f}   範圍 {lo:.3f}–{hi:.3f}')

Z = (M - M.mean(axis=0)) / sd
pairs = []
for i, j in itertools.combinations(range(len(pids)), 2):
    d = np.linalg.norm(Z[i] - Z[j]) / np.sqrt(len(AX))   # 每軸平均 z 距離
    nsame = int(np.sum(np.abs(Z[i] - Z[j]) < 0.5))       # 幾個軸幾乎同值
    pairs.append((d, nsame, pids[i], pids[j]))
pairs.sort()

print(f'\n171 組配對，每軸平均 z 距離：'
      f'最小 {pairs[0][0]:.2f}／中位 {pairs[len(pairs)//2][0]:.2f}／最大 {pairs[-1][0]:.2f}')
print('\n最接近的 12 組（這些是最可能被看成同一張臉的）')
for d, n, a, b in pairs[:12]:
    print(f'  {d:.2f}  {n}/9 軸幾乎同值   {a} ↔ {b}')
print('\n最分離的 5 組')
for d, n, a, b in pairs[-5:]:
    print(f'  {d:.2f}  {n}/9 軸幾乎同值   {a} ↔ {b}')
