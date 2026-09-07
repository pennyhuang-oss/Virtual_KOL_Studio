#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""依 ChatGPT R11 的逐格視覺裁定，排 19 位 × 4 槽的分配草案（0 credits）。

R11 撤銷了固定 yaw 門檻，改成它逐格看過 donor cards 後的人工裁定表。
本檔把那張表寫死，不由程式重新推導——程式自己放寬門檻正是前面失敗的模式。

硬規則（R10 P-02）：
  1. 每位四槽來自 4 個不同 ref
  2. 同一 (ref, slot) 最多供 2 位
  3. 同一 ref 跨四槽合計最多供 6 次
  4. 任兩位 persona 最多共用 1 個相同的 (ref, slot)
  5. 先用「可用」格；只在容量不足時啟用最少的「條件式」格
"""
import json, itertools, sys
from collections import defaultdict

SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
SLZH = {'FACE_SHAPE_AND_JAW': '臉型顎線', 'EYES_AND_BROWS': '眼與眉',
        'NOSE': '鼻', 'MOUTH': '口'}
R = lambda *ns: [f'ref_{n:02d}' for n in ns]

# ── ChatGPT R11 Q-01 的逐格裁定（原文照抄，不得由程式放寬）──
USABLE = {
    'FACE_SHAPE_AND_JAW': R(1, 2, 3, 4, 5, 6, 8, 10, 11, 14, 15),
    'EYES_AND_BROWS':     R(1, 3, 4, 5, 6, 14, 15),
    'NOSE':               R(1, 3, 4, 5, 6, 14, 15),
    'MOUTH':              R(1, 2, 3, 6, 14, 15),
}
CONDITIONAL = {
    'FACE_SHAPE_AND_JAW': R(7, 9),
    'EYES_AND_BROWS':     R(2, 7, 8, 9, 10, 11),
    'NOSE':               R(2, 8, 10),
    'MOUTH':              R(5, 7, 8, 10, 13),
}
CAP_SLOT = 2      # 同一 (ref, slot) 最多供幾位
CAP_REF = 6       # 同一 ref 跨四槽合計最多供幾次
SHARE_MAX = 1     # 任兩位最多共用幾個相同的 (ref, slot)

T = json.load(open('pilot/donor_slot_table.json', encoding='utf-8'))['refs']
D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))['personas']
pids = sorted(D)

# ── C 級一律排除，即使 R11 把它列為條件式 ──
conflicts = []
for slot in SL:
    for pool, name in ((USABLE, '可用'), (CONDITIONAL, '條件式')):
        keep = []
        for r in pool[slot]:
            g = T[r][slot]['grade']
            if g == 'C':
                conflicts.append(f'{r} / {SLZH[slot]}：R11 列為「{name}」，'
                                 f'但解析度只有 {T[r][slot]["part_px"]:.0f}px（C 級），'
                                 f'依 R11 自己的「C 級仍排除」規則移除')
            else:
                keep.append(r)
        pool[slot] = keep

GRADE = {(r, s): T[r][s]['grade'] for r in T for s in SL}

# ── 容量檢查 ──
print('每槽容量（同一 (ref, slot) 上限 2 位）')
for slot in SL:
    u, c = len(USABLE[slot]), len(CONDITIONAL[slot])
    print(f'  {SLZH[slot]:6s} 可用 {u} 張／{u*2} 人　＋條件式 {c} 張／{c*2} 人'
          f'　＝ 最多 {(u+c)*2} 人' + ('' if (u+c)*2 >= 19 else '   ← 不足 19'))
if conflicts:
    print('\nR11 裁定與解析度分級的衝突（已依 R11 自己的規則排除）：')
    for c in conflicts:
        print('  ! ' + c)

# ── 排表：優先用「可用」格，並讓使用次數平均 ──
assign = {p: {} for p in pids}
use_slot = defaultdict(int)   # (ref, slot) -> 幾位
use_ref = defaultdict(int)    # ref -> 跨槽合計


def shared(p, ref, slot):
    """加入這格之後，會不會有另一位跟 p 共用超過 SHARE_MAX 格。"""
    for q in pids:
        if q == p or not assign[q]:
            continue
        n = sum(1 for s, r in assign[p].items() if assign[q].get(s) == r)
        if assign[q].get(slot) == ref:
            n += 1
        if n > SHARE_MAX:
            return True
    return False


def candidates(p, slot):
    out = []
    for tier, pool in ((0, USABLE[slot]), (1, CONDITIONAL[slot])):
        for r in pool:
            if r in assign[p].values():
                continue
            if use_slot[(r, slot)] >= CAP_SLOT or use_ref[r] >= CAP_REF:
                continue
            if shared(p, r, slot):
                continue
            out.append((tier, use_slot[(r, slot)], use_ref[r], r))
    out.sort()
    return out


# ── 供需總量：R11 的 Q-02 只逐槽檢查，漏了「同一 ref 跨四槽 ≤6」這條全域上限 ──
supply = {}
for r in [f'ref_{n:02d}' for n in range(1, 16)]:
    n_slots = sum(1 for s in SL if r in USABLE[s] + CONDITIONAL[s])
    supply[r] = min(CAP_REF, CAP_SLOT * n_slots)
total = sum(supply.values())
print(f'\n全域供需：總供給 {total}　需求 76　'
      f'{"✓" if total >= 76 else f"✗ 差 {76 - total} 格"}')
if total < 76:
    print('  逐槽都夠，但「同一 ref 跨四槽最多 6 次」這條全域上限擋住了。')
    thin = {r: supply[r] for r in supply if supply[r] < CAP_REF}
    print('  供給不足 6 的來源：' +
          '、'.join(f'{r}={n}' for r, n in sorted(thin.items())))

# ── 解算：逐格填，選擇最少的先填，可回溯 ──
CELLS = [(p, s) for p in pids for s in SL]
CELLS.sort(key=lambda ps: len(USABLE[ps[1]]) + len(CONDITIONAL[ps[1]]))
NEED = {}


def cost(slot, r):
    return 1 if (r in CONDITIONAL[slot] or GRADE[(r, slot)] == 'B') else 0


def options(p, slot):
    out = []
    for r in USABLE[slot] + CONDITIONAL[slot]:
        if r in assign[p].values():
            continue
        if use_slot[(r, slot)] >= CAP_SLOT or use_ref[r] >= CAP_REF:
            continue
        if shared(p, r, slot):
            continue
        out.append(r)
    out.sort(key=lambda r: (cost(slot, r), use_slot[(r, slot)], use_ref[r]))
    return out


def search(i):
    if i == len(CELLS):
        return True
    p, slot = CELLS[i]
    for r in options(p, slot):
        assign[p][slot] = r
        use_slot[(r, slot)] += 1
        use_ref[r] += 1
        if search(i + 1):
            return True
        del assign[p][slot]
        use_slot[(r, slot)] -= 1
        use_ref[r] -= 1
    return False


sys.setrecursionlimit(10000)
# 供給不足時直接停——回溯會永遠找不到解，只是空轉
ok = search(0) if total >= 76 else False
fail = []
if not ok:
    print('\n✗ 在現行規則下排不滿 76 格——需要先放寬一條規則，見上面的供需算式。')
    json.dump({'_infeasible': True, '_supply_total': total, '_demand': 76,
               '_supply_per_ref': supply,
               '_note': 'R11 Q-02 只逐槽檢查容量，漏了同一 ref 跨四槽 ≤6 的全域上限。'},
              open('pilot/assignment_draft.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    sys.exit(2)
print(f'\n解算完成')

# ── 驗證 ──
errs = list(fail)
for p in pids:
    if len(assign[p]) != 4:
        errs.append(f'{p} 缺槽位')
    elif len(set(assign[p].values())) != 4:
        errs.append(f'{p} 四槽來源不相異：{assign[p]}')
for (r, s), n in use_slot.items():
    if n > CAP_SLOT:
        errs.append(f'{r}/{SLZH[s]} 供 {n} 位，超過上限 {CAP_SLOT}')
for r, n in use_ref.items():
    if n > CAP_REF:
        errs.append(f'{r} 跨槽合計 {n} 次，超過上限 {CAP_REF}')
for a, b in itertools.combinations(pids, 2):
    n = sum(1 for s in SL if assign[a].get(s) and assign[a].get(s) == assign[b].get(s))
    if n > SHARE_MAX:
        errs.append(f'{a} 與 {b} 共用 {n} 格，超過上限 {SHARE_MAX}')

print('\n分配草案')
print(f"{'persona':18s}" + ''.join(f'{SLZH[s]:>16s}' for s in SL))
for p in pids:
    line = f'{p:18s}'
    for s in SL:
        r = assign[p].get(s, '—')
        g = GRADE.get((r, s), '')
        tier = 'B條件' if r in CONDITIONAL[s] else ''
        line += f"{r + ' ' + g + tier:>16s}"
    print(line)

nb = sum(1 for p in pids for s in SL
         if assign[p].get(s) and (GRADE[(assign[p][s], s)] == 'B'
                                  or assign[p][s] in CONDITIONAL[s]))
print(f'\n76 格：已排 {sum(len(v) for v in assign.values())}，'
      f'其中需驗證（B 級或條件式）{nb} 格')
if errs:
    print(f'\nHARD FAIL：{len(errs)} 項')
    for e in errs:
        print('  ✗ ' + e)
    sys.exit(1)
print('  ✓ 四槽相異、slot 上限、ref 上限、兩人共用上限全部通過')

json.dump({'_source': 'ChatGPT R11 Q-01 逐格視覺裁定',
           '_rules': {'cap_ref_slot': CAP_SLOT, 'cap_ref_total': CAP_REF,
                      'max_shared_between_two_personas': SHARE_MAX},
           '_c_grade_conflicts': conflicts,
           'usable': USABLE, 'conditional': CONDITIONAL,
           'assignment': assign,
           'needs_validation': {f'{p}|{s}': assign[p][s] for p in pids for s in SL
                                if GRADE[(assign[p][s], s)] == 'B'
                                or assign[p][s] in CONDITIONAL[s]}},
          open('pilot/assignment_draft.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('\n→ pilot/assignment_draft.json')
