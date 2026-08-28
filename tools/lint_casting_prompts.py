#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase A 選角 prompt 靜態檢查。

與 lint_prompts.py（Nico 的 Phase C 專用）分開，因為選角有兩個結構性差異：
1. **沒有 Reference Element**——臉還沒定下來，這批圖就是要生出臉。
2. **允許臉部與膚色的否定式**。Round 2 實測：顏色類否定（`not tanned`）有效，
   Round 3 實測：face_negative 是把臉推離模型預設美女臉的有效手段。
   但構圖／服裝結構／朝向的否定仍然完全無效，因此否定式只准出現在
   face_negative 與 skin 兩行，其餘任何一行出現就是錯。
"""
import json, re, sys

ERR = []
def err(m): ERR.append(m)

spec = json.load(open('pilot/batch3_casting.json', encoding='utf-8'))
pr   = json.load(open('pilot/batch3_casting_prompts.json', encoding='utf-8'))
sys.path.insert(0, 'tools')
from build_casting_prompts import SHOTS
SH = {s['id']: s for s in SHOTS}

NEG = re.compile(r'\b(not|no|none|nothing|never|neither)\b', re.I)
# 該景別之外不得出現的身體部位詞
BEYOND = {
 'face_closeup': ['waist', 'hips', 'navel', 'legs', 'thighs', 'knees', 'feet', 'shoes', 'trousers', 'joggers', 'shorts'],
 'waist_up':     ['legs', 'thighs', 'knees', 'feet', 'shoes'],
 'knee_up':      ['feet', 'shoes'],
 'full_body':    [],
}
# 該景別的身體描述必須以這句結尾（確認用對了 body_en 的那一版）
BODY_TAIL = {
 'face_closeup': 'enters the frame',
 'waist_up':     'waist is narrow',
 'knee_up':      'hips',
 'full_body':    'She is 1',
}
VISIBLE = {'face_closeup': ['top', 'jewelry'], 'waist_up': ['top', 'top_hem', 'bottom', 'jewelry'],
           'knee_up': ['top', 'top_hem', 'bottom', 'jewelry'],
           'full_body': ['top', 'top_hem', 'bottom', 'shoes', 'jewelry']}

for key, txt in pr.items():
    pid, sid = key.split('/')
    p = spec['personas'][pid]
    f = SH[sid]['framing']
    lines = txt.split('\n')
    neg_ok = {p['face_negative'], spec['shared']['skin_en']}

    # 1. 否定式只准出現在 face_negative 與 skin 兩行
    for ln in lines:
        if ln in neg_ok:
            continue
        m = NEG.search(ln)
        if m:
            err(f"{key} 非臉／膚色行出現否定式：…{ln[max(0, m.start()-40):m.end()+40].strip()}…")

    # 2. 景別之外的身體部位詞（景別句本身除外——它就是在交代邊界）
    # 景別句本身就是在交代邊界切在哪裡，必然會提到裁切外的部位——豁免它
    fi = next(i for i, ln in enumerate(lines) if 'bottom edge of the picture' in ln or 'whole of her is inside' in ln)
    for tok in BEYOND[f]:
        for i, ln in enumerate(lines):
            if i == fi:
                continue
            if re.search(r'\b' + tok + r'\b', ln, re.I):
                err(f"{key}（{f}）提到裁切外的「{tok}」：{ln[:90]}")

    # 3. body_en 用對版本
    if BODY_TAIL[f] not in txt:
        err(f"{key} 的身體描述不是 {f} 那一版（找不到 {BODY_TAIL[f]!r}）")

    # 4. 服裝層：該景別看得見的要在、看不見的不准在
    lay = p['outfit_en']
    for k, v in lay.items():
        present = v[:40] in txt
        if k in VISIBLE[f] and not present:
            err(f"{key}（{f}）缺少應可見的服裝層 {k}")
        if k not in VISIBLE[f] and present:
            err(f"{key}（{f}）寫了看不見的服裝層 {k}")

    # 5. 赤腳：只准在全身出現，且不得同時出現鞋
    if p.get('barefoot'):
        if 'bare' in txt.lower().replace('her face is bare', '') and f != 'full_body':
            if re.search(r'\bbare (feet|foot)\b', txt, re.I):
                err(f"{key}（{f}）在看不到腳的景別提到赤腳")
        if re.search(r'\b(shoes|slippers|loafers)\b', txt, re.I):
            err(f"{key} 角色設定為赤腳，卻出現鞋")
    elif f == 'full_body' and 'bare feet' in txt.lower():
        err(f"{key} 角色有穿鞋，卻出現 bare feet")

    # 6. 選角不得有 Reference Element
    if '<<<' in txt:
        err(f"{key} 出現 Reference Element——選角階段臉還沒定下來，不該有錨點")

    # 7. 身體朝向不得用角度
    if re.search(r'\b\d+\s*degrees?\b', txt, re.I):
        err(f"{key} 用角度描述朝向——實測連續三次被畫成背影，一律改寫「鏡頭看得到哪些正面特徵」")

print(f"選角 prompt 靜態檢查（{len(pr)} 段）")
for e in ERR:
    print('  ✗ ', e)
if ERR:
    print(f"\nHARD FAIL：{len(ERR)} 項。")
    sys.exit(1)
print(f"  ✓ {len(pr)}/{len(pr)} 通過")
