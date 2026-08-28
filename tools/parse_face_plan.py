#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 review/REVIEW_BATCH3_FACES.md §10 回覆區的 (C)(D) 解析成 pilot/batch3_faces_v2.json。

**臉**來自 ChatGPT 的規劃（使用者裁決全面採用，舊 face_type 一律作廢）。
**身材、髮色、年齡、族裔、身分**沿用 kols/*/profile.json（使用者裁決不動）。

解析失敗一律 HARD FAIL——這份 JSON 會直接餵給生成器，不能用「大概對」的資料。
"""
import json, re, sys

SRC = 'review/REVIEW_BATCH3_FACES.md'
OUT = 'pilot/batch3_faces_v2.json'
FIELDS = ['ARCHETYPE', 'AXES', 'FACE_EN', 'NEGATIVE_EN', 'MARKERS', 'WHY_DISTINCT']
SLOTS = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']

err = []
raw = open(SRC, encoding='utf-8').read()
lines = raw.split('\n')
hits = [i for i, ln in enumerate(lines) if ln.strip() == 'REPLIES BELOW']
if not hits:
    sys.exit('找不到 REPLIES BELOW')
reply = '\n'.join(lines[hits[-1] + 1:])

# ── (C) 維度表 ──
ctext = reply.split('# (C) 維度表', 1)[1].split('# (D)', 1)[0]
axes = {}
for ln in ctext.strip().split('\n'):
    if ln.count('|') < 2 or ln.startswith('維度名稱'):
        continue
    name, vals, why = [x.strip() for x in ln.split('|', 2)]
    axes[name] = {'values': [v.strip() for v in vals.split('/')], 'why': why}

# ── (D) 19 位 ──
dtext = reply.split('# (D) 19 張臉', 1)[1].split('# (E)', 1)[0]
personas = {}
for block in re.split(r'\n### ', dtext)[1:]:
    pid = block.split('\n', 1)[0].strip()
    d = {}
    for f in FIELDS:
        m = re.search(rf'^{f}: (.+)$', block, re.M)
        if not m:
            err.append(f'{pid} 缺 {f}')
            continue
        d[f.lower()] = m.group(1).strip()
    if 'axes' in d:
        ax = {}
        for pair in d['axes'].split(';'):
            if '=' not in pair:
                err.append(f'{pid} AXES 格式錯：{pair!r}'); continue
            k, v = pair.split('=', 1); ax[k.strip()] = v.strip()
        d['axes'] = ax
    if 'markers' in d:
        d['markers'] = [x.strip() for x in d['markers'].split(';') if x.strip()]
    if 'face_en' in d:
        m = re.search(r'FACE_SHAPE_AND_JAW from (ref_\d+); EYES_AND_BROWS from (ref_\d+); '
                      r'NOSE from (ref_\d+); MOUTH from (ref_\d+)', d['face_en'])
        if not m:
            err.append(f'{pid} FACE_EN 找不到四張參考圖的分工')
        else:
            d['refs'] = dict(zip(SLOTS, m.groups()))
    personas[pid] = d

# ── 驗證 ──
idx = json.load(open('kols/index.json', encoding='utf-8'))
ks = idx['kols'] if isinstance(idx, dict) else idx
draft = [k['id'] for k in ks if k.get('status') == 'draft']
missing = [p for p in draft if p not in personas]
extra = [p for p in personas if p not in draft]
if missing: err.append(f'規劃缺少這幾位：{missing}')
if extra:   err.append(f'規劃出現不在待建模名單裡的 id：{extra}')

for pid, d in personas.items():
    for k, v in d.get('axes', {}).items():
        if k not in axes:
            err.append(f'{pid} 用了 (C) 沒定義的維度 {k!r}')
        elif v not in axes[k]['values']:
            err.append(f'{pid}.{k} = {v!r} 不在允許值 {axes[k]["values"]}')
    for a in axes:
        if a not in d.get('axes', {}):
            err.append(f'{pid} 缺維度 {a}')
    n = len(d.get('markers', []))
    if not 3 <= n <= 5:
        err.append(f'{pid} MARKERS {n} 個，規格是 3–5 個')

import os
for pid, d in personas.items():
    for slot, r in d.get('refs', {}).items():
        hit = [f for f in os.listdir('review/batch3_face_refs') if f.startswith(r + '.')]
        if not hit:
            err.append(f'{pid}.{slot} 指向不存在的檔案 {r}')
        else:
            d.setdefault('ref_files', {})[slot] = 'review/batch3_face_refs/' + hit[0]

# ── 合併使用者不可變的人設 ──
for pid, d in personas.items():
    if pid not in draft: continue
    pf = json.load(open(f'kols/{pid}/profile.json', encoding='utf-8'))
    i = pf['identity']; ap = i['appearance']; m = ap['measurements']
    d['fixed'] = {
        'display': pf.get('name') or pf.get('display_name') or pid,
        'age': i['age'], 'ethnicity': i['ethnicity'],
        'public_face': pf['persona']['public_face'],
        'height_cm': m['height_cm'], 'weight_kg': m.get('weight_kg'),
        'bust_cm': m['bust_cm'], 'waist_cm': m['waist_cm'], 'hip_cm': m['hip_cm'],
        'cup': m['cup_size'], 'leg_cm': m.get('leg_length_cm'),
        'hair': ap['hair'].replace('**', ''),
        'hair_color_current': ap.get('hair_color_current', ''),
        'superseded_face_type': ap.get('face_type', ''),
    }

if err:
    print(f'HARD FAIL：{len(err)} 項')
    for e in err: print('  ✗', e)
    sys.exit(1)

out = {
    '_source': 'ChatGPT 於 review/REVIEW_BATCH3_FACES.md §10 的規劃（commit 5c02a78），使用者裁決全面採用。',
    '_scope': '臉＝ChatGPT 規劃；身材／髮色／年齡／族裔／身分＝使用者原設定，不動。',
    '_superseded': 'kols/*/profile.json 的 identity.appearance.face_type 全部作廢，'
                   '不得再拿來限制新臉、不得複製進 prompt、不得在候選驗收時要求相符。',
    'axes': axes, 'personas': personas,
}
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'✓ 解析成功：{len(personas)} 位、{len(axes)} 條維度 → {OUT}')
