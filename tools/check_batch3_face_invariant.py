#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 3 臉部素材的硬規則檢查。規則見 BATCH3_FACE_INVARIANT.md。

存在的理由：這條規則原本只在對話裡，對話被壓縮之後我把它弄丟了，
於是整條線建立在錯的素材上。寫成可執行的斷言，才不會再靠記憶維持。

允許的臉部來源只有 ref_01–ref_15。ref_16 以上一律是走歪期間的產物，
保留檔案作失敗紀錄，但不得進入任何 active 分配。
"""
import json, os, re, sys

ALLOWED = {f'ref_{n:02d}' for n in range(1, 16)}
SLOTS = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
ERR = []


def refs_in(obj):
    """遞迴撈出所有 ref_NN 字串。"""
    if isinstance(obj, str):
        return set(re.findall(r'\bref_\d{2}\b', obj))
    out = set()
    if isinstance(obj, dict):
        for v in obj.values():
            out |= refs_in(v)
    elif isinstance(obj, list):
        for v in obj:
            out |= refs_in(v)
    return out


def check_assignment(path, get):
    if not os.path.exists(path):
        return
    D = json.load(open(path, encoding='utf-8'))
    for pid, slots in get(D):
        for slot, ref in slots.items():
            if slot in SLOTS and ref not in ALLOWED:
                ERR.append(f'{path}：{pid} 的 {slot} 指向 {ref}，'
                           f'不在允許的 ref_01–ref_15 內')


# 1. persona 的 active 分配
check_assignment('pilot/batch3_faces_v2.json',
                 lambda D: [(p, d['refs_v2']) for p, d in D['personas'].items()
                            if isinstance(d.get('refs_v2'), dict)])
check_assignment('pilot/r8_source_plan.json',
                 lambda D: list(D.get('assignment', {}).items()))

# 2. donor-slot 表不得把 ref_16+ 列為可用
p = 'pilot/donor_slot_table.json'
if os.path.exists(p):
    D = json.load(open(p, encoding='utf-8'))
    for rid, slots in D.get('refs', {}).items():
        if rid in ALLOWED:
            continue
        for slot, c in slots.items():
            if c.get('verdict') in ('ready', 'probe'):
                ERR.append(f'{p}：{rid} 不在允許範圍，卻被標成 {c["verdict"]}')

# 3. 規則文件本身要在
if not os.path.exists('BATCH3_FACE_INVARIANT.md'):
    ERR.append('BATCH3_FACE_INVARIANT.md 不見了——這條規則的正本不能刪')

print('Batch 3 臉部素材硬規則檢查')
print(f'  允許的來源：ref_01–ref_15（15 張美女參考圖）')
if ERR:
    for e in ERR:
        print('  ✗ ', e)
    print(f'\nHARD FAIL：{len(ERR)} 項違反 BATCH3_FACE_INVARIANT.md')
    sys.exit(1)
print('  ✓ 沒有任何 active 分配用到 ref_01–ref_15 以外的來源')
