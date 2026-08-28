#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""驗證 pilot/batch3_faces_v2.json 是否真的滿足 ChatGPT 自己訂的分離規則。

規則（ChatGPT (C) 節原文）：
  先以「輪廓原型、臉長寬比、三庭配置、骨肉量」形成粗分群，
  再要求**同群角色**在「眼眶結構、眼距、鼻部量體、口部幾何、顎頦」至少 3 軸不同。

這支程式的存在理由：上一版的指紋表判定零碰撞、出圖還是撞臉。
所以這次不只要跑，還要記得——**這只驗證規格，不驗證出圖**。出圖的驗收在 (E)。
"""
import json, sys, itertools
from collections import defaultdict

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
P = D['personas']
COARSE = ['輪廓原型', '臉長寬比', '三庭配置', '骨肉量']
FINE   = ['眼眶結構', '眼距', '鼻部量體', '口部幾何', '顎頦']
MIN_FINE = 3

err, warn = [], []
groups = defaultdict(list)
for pid, d in P.items():
    groups[tuple(d['axes'][a] for a in COARSE)].append(pid)

print(f"粗分群：{len(groups)} 群 / {len(P)} 位")
for k, v in sorted(groups.items(), key=lambda x: -len(x[1])):
    if len(v) > 1:
        print(f"  {len(v)} 位同群 {list(k)}：{v}")

for g, members in groups.items():
    for a, b in itertools.combinations(members, 2):
        diff = [f for f in FINE if P[a]['axes'][f] != P[b]['axes'][f]]
        if len(diff) < MIN_FINE:
            err.append(f"同群但細分軸只差 {len(diff)} 條（門檻 {MIN_FINE}）：{a} vs {b}；相異={diff}")

# 額外：全體兩兩的總相異軸數，找出最接近的組合
ALL = list(D['axes'])
pairs = []
for a, b in itertools.combinations(P, 2):
    n = sum(1 for x in ALL if P[a]['axes'][x] != P[b]['axes'][x])
    pairs.append((n, a, b))
pairs.sort()
print(f"\n全體 {len(pairs)} 組配對，11 條軸的相異數：最少 {pairs[0][0]}、中位 {pairs[len(pairs)//2][0]}、最多 {pairs[-1][0]}")
print("最接近的 6 組：")
for n, a, b in pairs[:6]:
    diff = [x for x in ALL if P[a]['axes'][x] != P[b]['axes'][x]]
    same = [x for x in ALL if P[a]['axes'][x] == P[b]['axes'][x]]
    print(f"  {n} 條不同 | {a} vs {b}")
    print(f"      相同：{same}")

# 參考圖用量集中度：臉型／下顎是身分主要載體，同一張圖供太多人會反噬「要長得不一樣」這件事
from collections import Counter
for slot in ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']:
    c = Counter(d['refs'][slot] for d in P.values())
    top, n = c.most_common(1)[0]
    if slot == 'FACE_SHAPE_AND_JAW' and n >= 4:
        warn.append(f"{slot}：{top} 一張供給 {n} 位（{[p for p,d in P.items() if d['refs'][slot]==top]}）。"
                    f"臉型與下顎是身分的主要載體，同源太多人會直接抵銷「要長得不一樣」的目的。")
    elif n >= 5:
        warn.append(f"{slot}：{top} 一張供給 {n} 位。")

print()
for w in warn: print('  ⚠ ', w)
for e in err: print('  ✗ ', e)
if err:
    print(f"\nHARD FAIL：{len(err)} 項")
    sys.exit(1)
print(f"  ✓ 規格層分離規則通過（{len(P)} 位、{len(groups)} 群）")
print("  ※ 提醒：這只驗證規格。上一版規格也全過，出圖仍撞臉——真正的驗收是 (E) 的盲測。")
