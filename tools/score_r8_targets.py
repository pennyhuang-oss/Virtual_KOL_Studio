#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""量 ref_40–58 的實測幾何，跟 R8 §4 的目標比，逐格判定進窗與否。

ChatGPT 端跑不了 mediapipe，所以它明講不宣稱命中、全部標 pending。
命中與否由這支決定，不由描述決定。
"""
import json, sys
import numpy as np

SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
SLOT_AX = {'FACE_SHAPE_AND_JAW': ['face_hw', 'jaw_ratio', 'third_mid', 'third_low'],
           'EYES_AND_BROWS': ['eye_space', 'eye_open'],
           'NOSE': ['alar_r'], 'MOUTH': ['mouth_r', 'lip_r']}
AX = [a for s in SL for a in SLOT_AX[s]]
G = json.load(open('pilot/ref_geometry.json', encoding='utf-8'))
P = json.load(open('pilot/r8_source_plan.json', encoding='utf-8'))
T = json.load(open('pilot/geometry_targets.json', encoding='utf-8'))

# 尺規沿用舊池，才跟先前所有數字可比
old = [v for k, v in G.items() if 16 <= int(k.split('_')[1]) <= 33]
sd = {a: float(np.std([v[a] for v in old], ddof=1)) for a in AX}
TOL = 0.5     # 容許偏差，單位是舊池每軸 sd

rows, miss = [], []
for rid in sorted(P['images'], key=lambda r: int(r.split('_')[1])):
    if rid not in G:
        miss.append((rid, 'NO_LANDMARKS')); continue
    for slot in SL:
        e = P['images'][rid][slot]
        for a, tv in e['targets'].items():
            mv = G[rid][a]
            d = (mv - tv) / sd[a]
            rows.append((rid, slot, e['for_persona'], a, tv, mv, d))
            if abs(d) > TOL:
                miss.append((rid, f'{slot}/{a} 目標 {tv:.3f} 實測 {mv:.3f} 偏 {d:+.2f}sd'))

n = len(rows)
ok = sum(1 for r in rows if abs(r[6]) <= TOL)
print(f'76 格目標，進窗 {ok}／{n}（容許 ±{TOL}sd，sd 取舊池 ref_16–33）\n')

bad_by_ref = {}
for rid, why in miss:
    bad_by_ref.setdefault(rid, []).append(why)
print(f'需要重生的圖：{len(bad_by_ref)} 張')
for rid in sorted(bad_by_ref, key=lambda r: int(r.split('_')[1])):
    print(f'\n{rid}（{len(bad_by_ref[rid])} 格未進窗）')
    for why in bad_by_ref[rid]:
        print(f'   {why}')

json.dump({'tolerance_sd': TOL, 'sd': sd,
           'rows': [{'ref': r[0], 'slot': r[1], 'for_persona': r[2], 'axis': r[3],
                     'target': r[4], 'measured': round(r[5], 4), 'dev_sd': round(r[6], 2)}
                    for r in rows],
           'in_window': ok, 'total': n,
           'refs_needing_regen': sorted(bad_by_ref)},
          open('pilot/r8_measurement.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('\n→ pilot/r8_measurement.json')
