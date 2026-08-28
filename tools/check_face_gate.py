#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ChatGPT R2 F-03 裁決的分離 gate。取代原本的粗分群規則（那條是空 gate）。

三條規則：
  1. 任兩人 11 條軸至少相異 6 條
  2. 六條主導軸至少相異 2 條
  3. 若兩人共用同一張 FACE_SHAPE_AND_JAW：總相異至少 7 條、主導軸至少 3 條

用 refs_v2（R2 的新分配）判定「共用臉型來源」。
一律提醒：**這只驗證規格**。上一版規格全過，出圖仍撞臉；真正的驗收是去髮妝盲測。
"""
import json, sys, itertools
from collections import Counter

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
P, ALL = D['personas'], list(D['axes'])
DOM = ['輪廓原型', '臉長寬比', '三庭配置', '骨肉量', '顎頦', '眼眶結構']
assert all(a in ALL for a in DOM), '主導軸名稱與維度表對不上'

refs = lambda p: P[p].get('refs_v2') or P[p]['refs']
err = []

# 來源分配規則（F-02）
cs = Counter(refs(p)['FACE_SHAPE_AND_JAW'] for p in P)
cn = Counter(refs(p)['NOSE'] for p in P)
for k, v in cs.items():
    if v > 2: err.append(f'臉型來源 {k} 供給 {v} 位（上限 2）')
for k, v in cn.items():
    if v > 3: err.append(f'鼻子來源 {k} 供給 {v} 位（上限 3）')
for p in P:
    if len(set(refs(p).values())) < 4:
        err.append(f'{p} 的四個槽位沒有用到四張不同的圖：{refs(p)}')

# 分離 gate（F-03）
rows = []
for a, b in itertools.combinations(P, 2):
    n = sum(1 for x in ALL if P[a]['axes'][x] != P[b]['axes'][x])
    dm = sum(1 for x in DOM if P[a]['axes'][x] != P[b]['axes'][x])
    share = refs(a)['FACE_SHAPE_AND_JAW'] == refs(b)['FACE_SHAPE_AND_JAW']
    need_n, need_d = (7, 3) if share else (6, 2)
    if n < need_n or dm < need_d:
        rows.append((n, need_n, dm, need_d, a, b, share))
rows.sort()

print(f'臉部分離 gate（{len(P)} 位、{len(P)*(len(P)-1)//2} 組配對）')
print(f'  來源分配：臉型上限 {max(cs.values())}/2、鼻子上限 {max(cn.values())}/3')
for n, nn, dm, nd, a, b, share in rows:
    tag = '  ← 共用臉型來源，適用較嚴的 7/3' if share else ''
    err.append(f'{a} vs {b}：總相異 {n}（需 {nn}）、主導軸 {dm}（需 {nd}）{tag}')

for e in err:
    print('  ✗ ', e)
if err:
    print(f'\nHARD FAIL：{len(err)} 項。未通過前不得生成。')
    sys.exit(1)
print('  ✓ 全數通過')
print('  ※ 這只驗證規格。真正的驗收是出圖後的去髮妝盲測。')
