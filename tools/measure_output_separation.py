#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""量已生成的 identity master 之間的分離度。

量的是輸出圖上的臉部比例（以臉寬正規化），不是來源、不是文字。
校準值（先前量過，見 review/SEPARATION_TEST.md）：
  同一人不同抽樣 0.31–0.57（雜訊底線）；兩個不同人 1.19–1.22；門檻 1.02（外推）。
"""
import sys, os, itertools, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_face_crops import landmarks  # noqa

def ratios(path):
    P, size = landmarks(path)
    if P is None:
        raise SystemExit(f'偵測不到臉：{path}')
    L, R = P[234], P[454]
    fw = np.linalg.norm(R - L)
    d = lambda a, b: np.linalg.norm(P[a] - P[b]) / fw
    return np.array([
        d(10, 152),    # 臉高
        d(172, 397),   # 顎寬
        d(133, 362),   # 眼距
        d(33, 133),    # 眼裂長
        d(159, 145),   # 眼裂高
        d(129, 358),   # 鼻翼寬
        d(1, 168),     # 鼻長
        d(61, 291),    # 嘴寬
        d(0, 17),      # 唇厚
        d(10, 168),    # 上庭
        d(168, 2),     # 中庭
        d(2, 152),     # 下庭
    ])

if __name__ == '__main__':
    files = sys.argv[1:]
    V = {}
    for f in files:
        V[f] = ratios(f)
    keys = list(V)
    M = np.array([V[k] for k in keys])
    sd = M.std(axis=0, ddof=1)
    sd[sd == 0] = 1e-9
    Z = (M - M.mean(axis=0)) / sd
    out = []
    for i, j in itertools.combinations(range(len(keys)), 2):
        out.append((float(np.linalg.norm(Z[i] - Z[j]) / np.sqrt(len(sd))), keys[i], keys[j]))
    out.sort()
    for dist, a, b in out:
        flag = '同一張臉' if dist < 0.6 else ('偏近' if dist < 1.02 else 'OK')
        print(f'{dist:6.3f}  {flag:5s}  {a}  vs  {b}')
