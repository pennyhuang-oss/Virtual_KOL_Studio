#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""K-05：跨角色臉部指紋碰撞檢查。

**這支工具解決的問題**：face_type 只寫一行形容詞時，seedream 會把所有人收斂到它的
預設美女臉。本 repo 已經為此付出三次代價（zoe-lai 刪除、sophia-tseng 收斂、
nico-tsai 選角跑三輪）。把臉拆成 10 條骨相軸之後，「會不會撞臉」在**送生成之前**
就能判定，不必等出圖用肉眼發現。

規則：同一 ethnicity_group 內，任兩人至少 4 條軸不同，
且其中至少 2 條落在 dominant_axes（face_outline / eye_axis / eyelid / jaw_angle）。

用法：
    python3 tools/face_registry.py            # 檢查全表
    python3 tools/face_registry.py --new ID   # 只檢查某角色對全表
exit 0 = 全數通過；exit 1 = 有碰撞，不准送生成。
"""
import json, sys, itertools

REG = 'pilot/face_fingerprints.json'
MIN_TOTAL = 4
MIN_DOMINANT = 2


def load():
    return json.load(open(REG, encoding='utf-8'))


def axes_of(d):
    return list(d['axes'].keys())


def validate_values(d):
    """每個 persona 的每條軸都必須是 axes 定義過的值——防止拼字錯誤靜默通過。"""
    errs = []
    ax = d['axes']
    for pid, p in d['personas'].items():
        for a, allowed in ax.items():
            if a not in p:
                errs.append(f"{pid} 缺少軸 {a}")
            elif p[a] not in allowed:
                errs.append(f"{pid}.{a} = {p[a]!r} 不在允許值內 {allowed}")
        if 'ethnicity_group' not in p:
            errs.append(f"{pid} 缺少 ethnicity_group")
    return errs


def compare(d, a_id, b_id):
    ax = axes_of(d)
    dom = set(d['dominant_axes'])
    A, B = d['personas'][a_id], d['personas'][b_id]
    diff = [k for k in ax if A[k] != B[k]]
    return diff, [k for k in diff if k in dom]


def grandfathered(d):
    return {tuple(g['pair']) for g in d.get('_grandfathered', {}).get('pairs', [])}


def check(d, only=None):
    errs = validate_values(d)
    if errs:
        return errs, []
    gf = grandfathered(d)
    warn = []
    noted = []
    ids = list(d['personas'])
    pairs = itertools.combinations(ids, 2)
    if only:
        if only not in d['personas']:
            return [f"{only} 不在登記表內"], [], []
        pairs = ((only, b) for b in ids if b != only)
    for a, b in pairs:
        if d['personas'][a]['ethnicity_group'] != d['personas'][b]['ethnicity_group']:
            continue
        diff, dom = compare(d, a, b)
        below = len(diff) < MIN_TOTAL or len(dom) < MIN_DOMINANT
        if below and tuple(sorted([a, b])) in gf:
            # 已訓練角色之間的既成碰撞：登記，不阻擋（臉無法回溯修改）
            noted.append(f"既成（已訓練，無法回溯修改）：{a} vs {b} — 差 {len(diff)} 條，dominant {len(dom)}")
            continue
        if below:
            errs.append(
                f"撞臉：{a} vs {b} — 只差 {len(diff)} 條軸（門檻 {MIN_TOTAL}），"
                f"其中 dominant {len(dom)} 條（門檻 {MIN_DOMINANT}）。相異：{diff or '無'}")
        elif len(diff) == MIN_TOTAL:
            warn.append(f"僅達下限：{a} vs {b} — 差 {len(diff)} 條（{diff}），dominant {dom}")
    return errs, warn, noted


def main():
    only = None
    if '--new' in sys.argv:
        only = sys.argv[sys.argv.index('--new') + 1]
    d = load()
    errs, warn, noted = check(d, only)
    print(f"臉部指紋碰撞檢查（{len(d['personas'])} 位登記{'，只檢查 ' + only if only else ''}）")
    for n in noted:
        print('  ·  ', n)
    for w in warn:
        print('  ⚠ ', w)
    for e in errs:
        print('  ✗ ', e)
    if errs:
        print(f"\nHARD FAIL：{len(errs)} 組碰撞。修正骨相軸後才可送生成。")
        sys.exit(1)
    print('  ✓ 無碰撞')


if __name__ == '__main__':
    main()
