#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在「ChatGPT 自己認定相容」的範圍內，重排來源指派，把排程衝突與真缺口分開。

**這支程式不發明相容性。** 相容集合只有兩個來源：
  (a) ChatGPT 曾經指派過的 (persona, slot, ref)；
  (b) 它在 R6 K-02 的 BLOCK 理由裡明講「相符／同幾何」但因為被佔用或 cap 滿而不能用的。

它手工貪婪排出 26 配 13 BLOCK，只找到 1 個可搬移解。這裡用回溯搜尋在同一個相容集合裡
最大化可配槽位——如果解得更多，那些 BLOCK 就是排程問題而不是缺幾何。
"""
import json, sys
from collections import Counter, defaultdict

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))['personas']
M = json.load(open('pilot/face_crops_manifest.json', encoding='utf-8'))['artifacts']
V = 'v1'
SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
CAP = {'FACE_SHAPE_AND_JAW': 2, 'EYES_AND_BROWS': 3, 'NOSE': 3, 'MOUTH': 3}

# ── ChatGPT R5 J-08 的既定指派（不在 R6 的 39 項之列，視為已定但可搬移）──
FIXED = {
 'EYES_AND_BROWS': {'tammy-chou': 'ref_26', 'zoey-yeh': 'ref_21', 'kanon-komori': 'ref_21',
   'jia-seo': 'ref_17', 'zhiyi-shen': 'ref_16', 'wanyin-jiang': 'ref_24',
   'wendy-yeo': 'ref_29', 'peggy-lee': 'ref_27', 'angeline-kwee': 'ref_25'},
 'NOSE': {'tammy-chou': 'ref_18', 'zoey-yeh': 'ref_18', 'rin-ayase': 'ref_19',
   'yerin-han': 'ref_19', 'ruoruo-tang': 'ref_16', 'cheryl-soh': 'ref_24',
   'sydney-leong': 'ref_18', 'zhiyi-shen': 'ref_17', 'wanyin-jiang': 'ref_17',
   'wendy-yeo': 'ref_17', 'angeline-kwee': 'ref_24'},
 'MOUTH': {'angel-chiu': 'ref_18', 'nanami-fujiwara': 'ref_18', 'kanon-komori': 'ref_22',
   'jia-seo': 'ref_28', 'zhiyi-shen': 'ref_25', 'wanyin-jiang': 'ref_25',
   'peggy-lee': 'ref_26', 'somi-oh': 'ref_26', 'wendy-yeo': 'ref_19',
   'angeline-kwee': 'ref_16'}}
# ── R6 K-01 的 26 項 ──
K01 = {
 'FACE_SHAPE_AND_JAW': {'angel-chiu': 'ref_20', 'zoey-yeh': 'ref_26', 'rin-ayase': 'ref_24',
   'yerin-han': 'ref_27', 'cheryl-soh': 'ref_25', 'wendy-yeo': 'ref_16'},
 'EYES_AND_BROWS': {'miu-shiraishi': 'ref_18', 'rin-ayase': 'ref_28',
   'nanami-fujiwara': 'ref_16', 'yerin-han': 'ref_26', 'cheryl-soh': 'ref_26',
   'sydney-leong': 'ref_23'},
 'NOSE': {'angel-chiu': 'ref_16', 'emma-kao': 'ref_27', 'miu-shiraishi': 'ref_26',
   'nanami-fujiwara': 'ref_21', 'jia-seo': 'ref_19', 'somi-oh': 'ref_21',
   'peggy-lee': 'ref_20'},
 'MOUTH': {'tammy-chou': 'ref_21', 'emma-kao': 'ref_18', 'zoey-yeh': 'ref_22',
   'miu-shiraishi': 'ref_21', 'rin-ayase': 'ref_21', 'yerin-han': 'ref_16',
   'cheryl-soh': 'ref_23'}}
# ── K-02 的 BLOCK 理由裡，它自己明講「相符／同幾何」的 ──
FROM_BLOCK = [
 ('jia-seo', 'FACE_SHAPE_AND_JAW', 'ref_28', '唯一瘦長六角方向'),
 ('wanyin-jiang', 'FACE_SHAPE_AND_JAW', 'ref_25', '長窄卵形相符'),
 ('angeline-kwee', 'FACE_SHAPE_AND_JAW', 'ref_25', '極長窄卵形相符'),
 ('angel-chiu', 'EYES_AND_BROWS', 'ref_20', '圓開平視／中等眼距'),
 ('angel-chiu', 'EYES_AND_BROWS', 'ref_18', '同幾何'),
 ('kanon-komori', 'NOSE', 'ref_18', '低至中鼻樑＋圓鼻頭相符'),
 ('kanon-komori', 'NOSE', 'ref_21', '相符'),
 ('ruoruo-tang', 'MOUTH', 'ref_21', '相符的寬中等唇'),
 ('sydney-leong', 'MOUTH', 'ref_21', '雖相符'),
 ('sydney-leong', 'NOSE', 'ref_26', 'ChatGPT 提議的搬移目標'),
]
# 它自己明說不相容的，不得使用
INCOMPATIBLE = {
 ('tammy-chou', 'FACE_SHAPE_AND_JAW', 'ref_23'), ('tammy-chou', 'FACE_SHAPE_AND_JAW', 'ref_26'),
 ('zhiyi-shen', 'FACE_SHAPE_AND_JAW', 'ref_29'),
 ('ruoruo-tang', 'FACE_SHAPE_AND_JAW', 'ref_22'), ('ruoruo-tang', 'FACE_SHAPE_AND_JAW', 'ref_19'),
 ('ruoruo-tang', 'FACE_SHAPE_AND_JAW', 'ref_27'),
 ('emma-kao', 'EYES_AND_BROWS', 'ref_25'), ('emma-kao', 'EYES_AND_BROWS', 'ref_29'),
 ('emma-kao', 'EYES_AND_BROWS', 'ref_17'),
 ('ruoruo-tang', 'EYES_AND_BROWS', 'ref_19'), ('ruoruo-tang', 'EYES_AND_BROWS', 'ref_27'),
 ('ruoruo-tang', 'EYES_AND_BROWS', 'ref_23'),
 ('ruoruo-tang', 'MOUTH', 'ref_26'), ('ruoruo-tang', 'MOUTH', 'ref_28'),
 ('sydney-leong', 'MOUTH', 'ref_26'), ('sydney-leong', 'MOUTH', 'ref_28'),
 ('zhiyi-shen', 'FACE_SHAPE_AND_JAW', 'ref_17'),   # 「下巴長」，它判定不理想
}

COMPAT = defaultdict(set)
for src in (FIXED, K01):
    for slot, mp in src.items():
        for pid, ref in mp.items():
            COMPAT[(pid, slot)].add(ref)
for pid, slot, ref, _ in FROM_BLOCK:
    COMPAT[(pid, slot)].add(ref)
for k in list(COMPAT):
    COMPAT[k] -= {r for r in COMPAT[k] if (k[0], k[1], r) in INCOMPATIBLE}

# 需要指派的所有槽位＝19×4，扣掉「臉型槽本來就已經是合成來源」的那些
CUR = {}
for pid, d in D.items():
    r = dict(d.get('refs_v2') or d['refs'])
    for slot, mp in FIXED.items():
        if pid in mp: r[slot] = mp[pid]
    CUR[pid] = r
SLOTS = []
for pid in D:
    for slot in SL:
        if CUR[pid][slot] >= 'ref_16':
            COMPAT[(pid, slot)].add(CUR[pid][slot])   # 已經是合成來源，本身相容
        SLOTS.append((pid, slot))

def qa_ok(ref, slot):
    return M.get(f'{ref}__{slot}__{V}', {}).get('qa_status') == 'pass'

for k in list(COMPAT):
    COMPAT[k] = {r for r in COMPAT[k] if r >= 'ref_16' and qa_ok(r, k[1])}

best = {'n': -1, 'sol': None}
def search(i, assign, capuse, used_by):
    if best['n'] == len(SLOTS):
        return
    filled = sum(1 for v in assign.values() if v)
    if filled + (len(SLOTS) - i) <= best['n']:
        return
    if i == len(SLOTS):
        if filled > best['n']:
            best['n'] = filled; best['sol'] = dict(assign)
        return
    pid, slot = SLOTS[i]
    opts = sorted(COMPAT.get((pid, slot), set()),
                  key=lambda r: (capuse[slot][r], r))
    for ref in opts:
        if ref in used_by[pid]:            # 同一 persona 四槽必須互異
            continue
        if capuse[slot][ref] >= CAP[slot]:  # slot cap
            continue
        assign[(pid, slot)] = ref
        capuse[slot][ref] += 1; used_by[pid].add(ref)
        search(i + 1, assign, capuse, used_by)
        capuse[slot][ref] -= 1; used_by[pid].discard(ref)
    assign[(pid, slot)] = None              # 配不到
    search(i + 1, assign, capuse, used_by)
    del assign[(pid, slot)]

# 先排「選項最少」的槽位，剪枝更有效
SLOTS.sort(key=lambda ps: len(COMPAT.get(ps, set())))
search(0, {}, {s: Counter() for s in SL}, defaultdict(set))

sol = best['sol']
unfilled = [k for k, v in sol.items() if not v]
print(f'相容集合內可配 {best["n"]}/{len(SLOTS)} 個槽位；配不到 {len(unfilled)} 個')
print(f'（ChatGPT 手工排的結果是 13 個 BLOCK）\n')
print('配不到的：')
for pid, slot in sorted(unfilled):
    print(f'  {pid:16s} {slot}')
CG_BLOCK = {('tammy-chou','FACE_SHAPE_AND_JAW'),('jia-seo','FACE_SHAPE_AND_JAW'),
 ('zhiyi-shen','FACE_SHAPE_AND_JAW'),('wanyin-jiang','FACE_SHAPE_AND_JAW'),
 ('ruoruo-tang','FACE_SHAPE_AND_JAW'),('angeline-kwee','FACE_SHAPE_AND_JAW'),
 ('angel-chiu','EYES_AND_BROWS'),('emma-kao','EYES_AND_BROWS'),('somi-oh','EYES_AND_BROWS'),
 ('ruoruo-tang','EYES_AND_BROWS'),('kanon-komori','NOSE'),('ruoruo-tang','MOUTH'),
 ('sydney-leong','MOUTH')}
solved = CG_BLOCK - set(unfilled)
print(f'\n它的 13 個 BLOCK 裡，靠搬移就能解掉的：{len(solved)}')
for pid, slot in sorted(solved):
    print(f'  ✓ {pid:16s} {slot} → {sol[(pid,slot)]}')
still = CG_BLOCK & set(unfilled)
print(f'\n真的缺幾何、搬移解不掉的：{len(still)}')
for pid, slot in sorted(still):
    print(f'  ✗ {pid:16s} {slot}')
json.dump({f'{k[0]}|{k[1]}': v for k, v in sol.items()},
          open('/tmp/solved_assignment.json', 'w'), ensure_ascii=False, indent=1)
