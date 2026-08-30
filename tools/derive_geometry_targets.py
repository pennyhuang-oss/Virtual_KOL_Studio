#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 11 條形容詞軸翻成可量測的數值窗，再求出「能讓 171 組全部過門檻」的目標幾何。

為什麼要這一步：形容詞是這次失敗的直接原因。ChatGPT 生的 18 張圖，
每一張的形容詞都對，但同一個形容詞（例如「寬顎」）它一律畫成池子中位數附近，
於是 19 位人物擠在 5% 的帶寬裡。要它畫得開，就得給它數字，不能再給形容詞。

窗的上下界取自「真人照 ref_01–15」的實測範圍——那是真人臉確實做得到的範圍，
不是我憑空定的。每條軸切三段（低／中／高），形容詞決定落在哪一段。
"""
import json, itertools, sys
import numpy as np

# 三庭不是三條獨立的軸——它們加起來必為 1。把上庭高度與「中庭佔中下庭的比例」
# 當兩條獨立軸，才不會排出上庭 0.29 這種不存在的臉。
AX = ['face_hw', 'jaw_ratio', 'third_up', 'mid_share',
      'eye_space', 'eye_open', 'alar_r', 'mouth_r', 'lip_r']
SLOT_OF = {'face_hw': 'FACE_SHAPE_AND_JAW', 'jaw_ratio': 'FACE_SHAPE_AND_JAW',
           'third_up': 'FACE_SHAPE_AND_JAW', 'mid_share': 'FACE_SHAPE_AND_JAW',
           'eye_space': 'EYES_AND_BROWS', 'eye_open': 'EYES_AND_BROWS',
           'alar_r': 'NOSE', 'mouth_r': 'MOUTH', 'lip_r': 'MOUTH'}
THRESHOLD = 1.02

g = json.load(open('pilot/ref_geometry.json', encoding='utf-8'))
D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
pids = sorted(D['personas'])

def derived(v):
    d = dict(v)
    d['third_up'] = 1 - v['third_mid'] - v['third_low']
    d['mid_share'] = v['third_mid'] / (v['third_mid'] + v['third_low'])
    return d

g = {k: derived(v) for k, v in g.items()}
real = [v for k, v in g.items() if int(k.split('_')[1]) <= 15]
LO = {a: min(v[a] for v in real) for a in AX}
HI = {a: max(v[a] for v in real) for a in AX}

def band(a, level):
    """level: 0 低 / 1 中 / 2 高。回傳 (下界, 上界)。"""
    lo, hi = LO[a], HI[a]
    step = (hi - lo) / 3
    return (lo + level * step, lo + (level + 1) * step)

def level(axes):
    """把一位 persona 的形容詞軸翻成 9 條測量軸各自的段位。"""
    L = {}
    r = axes['臉長寬比']
    L['face_hw'] = 2 if r in ('極長窄', '長窄') else (0 if r == '短寬' else 1)
    j = axes['顎頦']
    L['jaw_ratio'] = 0 if j.startswith('窄顎') else (1 if j.startswith('柔方顎') else 2)
    # 中庭佔比：長中庭／短下庭往高推，短中庭／長下庭往低推，同時出現則互相抵銷。
    t = axes['三庭配置']
    push = ('長中庭' in t) + ('短下庭' in t) - ('短中庭' in t) - ('長下庭' in t)
    L['mid_share'] = 2 if push > 0 else (0 if push < 0 else 1)
    L['third_up'] = 1          # 額高不在形容詞表裡，留在中段當自由軸
    e = axes['眼距']
    L['eye_space'] = {'窄': 0, '中等': 1, '寬': 2}[e]
    o = axes['眼眶結構']
    L['eye_open'] = 2 if o.startswith('圓開') else 0
    n = axes['鼻部量體']
    L['alar_r'] = 2 if n == '短寬軟鼻' else (0 if n == '長直細鼻' else 1)
    m = axes['口部幾何']
    L['mouth_r'] = 2 if m.startswith('寬') else 0
    L['lip_r'] = 0 if '薄' in m else (2 if '飽滿' in m else 1)
    return L

B = {p: {a: band(a, level(D['personas'][p]['axes'])[a]) for a in AX} for p in pids}
cur = np.array([[g[D['personas'][p]['refs_v2'][SLOT_OF[a]]][a] for a in AX] for p in pids])
sd = cur.std(0, ddof=1)

def mind(M):
    Z = M / sd
    return min(np.linalg.norm(Z[i] - Z[j]) / np.sqrt(len(AX))
               for i, j in itertools.combinations(range(len(pids)), 2))

# 從「各自窗內、最接近現況」的點出發，做投影式爬山：只在窗內移動。
X = np.array([[min(max(cur[i][k], B[p][a][0]), B[p][a][1])
               for k, a in enumerate(AX)] for i, p in enumerate(pids)])
print(f'現行實際幾何的最小配對距離：{mind(cur):.3f}')
print(f'把每位夾進自己的窗之後：      {mind(X):.3f}')

rng = np.random.default_rng(3)
best = X.copy(); bv = mind(best)
for it in range(60000):
    i = rng.integers(len(pids)); k = rng.integers(len(AX))
    p, a = pids[i], AX[k]
    old = best[i][k]
    best[i][k] = rng.uniform(*B[p][a])
    v = mind(best)
    if v > bv: bv = v
    else: best[i][k] = old
print(f'在窗內最佳化後：              {bv:.3f}   （門檻 {THRESHOLD}）\n')

if bv < THRESHOLD:
    print('⚠ 即使每位都放到自己形容詞允許的最極端，仍過不了門檻——必須動規格，不只是換圖。')

need = {}
for i, p in enumerate(pids):
    for k, a in enumerate(AX):
        d = (best[i][k] - cur[i][k]) / sd[k]
        if abs(d) >= 0.8:                      # 只列出真的要搬動的
            need.setdefault(p, []).append((a, cur[i][k], best[i][k], d))

print(f'需要調整的 persona：{len(need)} 位\n')
for p in sorted(need, key=lambda x: -len(need[x])):
    print(f'{p}')
    for a, c, t, d in sorted(need[p], key=lambda r: -abs(r[3])):
        arrow = '↑' if d > 0 else '↓'
        print(f'   {SLOT_OF[a]:20s} {a:10s} 現在 {c:.3f} → 目標 {t:.3f} {arrow}')
def to_thirds(t):
    up, ms = t['third_up'], t['mid_share']
    rest = 1 - up
    return {'third_mid': round(rest * ms, 3), 'third_low': round(rest * (1 - ms), 3)}

json.dump({'thirds': {p: to_thirds({a: float(best[i][k]) for k, a in enumerate(AX)})
                      for i, p in enumerate(pids)},
           'targets': {p: {a: float(best[i][k]) for k, a in enumerate(AX)}
                       for i, p in enumerate(pids)},
           'current': {p: {a: float(cur[i][k]) for k, a in enumerate(AX)}
                       for i, p in enumerate(pids)},
           'bands': {p: {a: list(map(float, B[p][a])) for a in AX} for p in pids},
           'min_pair_achievable': float(bv), 'threshold': THRESHOLD},
          open('pilot/geometry_targets.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('\n→ pilot/geometry_targets.json')
