#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""眼／鼻／口三槽的來源盤點：可用度、集中度，以及來源判讀 vs 該角色 spec 的矛盾。

探針 B 證明部件裁切之後，被指派的來源**會真的被畫出來**。
在那之前來源選錯看不出來（因為根本沒執行）；現在會直接顯示在出圖上。
所以這三槽需要做 ChatGPT 剛替 FACE_SHAPE_AND_JAW 做過的那種盤點。
"""
import json, re, sys
from collections import Counter

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
R = json.load(open('pilot/face_refs_readout.json', encoding='utf-8'))['refs']
P = D['personas']
refs = lambda p: P[p].get('refs_v2') or P[p]['refs']
SLOT_AXES = {'EYES_AND_BROWS': ['眼眶結構', '眼距'],
             'NOSE': ['鼻部量體'], 'MOUTH': ['口部幾何']}
SLOT_KEY = {'EYES_AND_BROWS': 'eyes_and_brows', 'NOSE': 'nose', 'MOUTH': 'mouth'}

# 只在「規格與來源明確互斥」時才標矛盾。判斷不了的一律留白交給審閱者。
RULES = [
 ('EYES_AND_BROWS', '單眼皮', ['雙眼皮'], '規格要單眼皮，來源是雙眼皮'),
 ('EYES_AND_BROWS', '細長',   ['大而圓', '極大'], '規格要細長眼，來源是大而圓的眼'),
 ('EYES_AND_BROWS', '窄眼',   ['大而圓', '極大'], '規格要窄眼，來源是大而圓的眼'),
 ('EYES_AND_BROWS', '圓開',   ['細長'], '規格要圓而開的眼，來源是細長眼'),
 ('EYES_AND_BROWS', '下垂',   ['上揚'], '規格要眼尾下垂，來源是上揚'),
 ('EYES_AND_BROWS', '上揚',   ['下垂'], '規格要眼尾上揚，來源是下垂'),
 ('NOSE', '長直細鼻', ['短', '低鼻樑', '鼻樑低'], '規格要長而直的細鼻，來源是短鼻或低鼻樑'),
 ('NOSE', '低鼻樑',   ['長', '高'], '規格要低鼻樑，來源是長鼻或高鼻樑'),
 ('NOSE', '短寬軟鼻', ['長'], '規格要短而寬的軟鼻，來源是長鼻'),
 ('MOUTH', '薄',     ['飽滿', '厚'], '規格要薄唇，來源是飽滿或厚唇'),
 ('MOUTH', '飽滿',   ['薄'], '規格要飽滿唇，來源是薄唇'),
 ('MOUTH', '小',     ['寬'], '規格要小口，來源是寬口'),
 ('MOUTH', '寬',     ['小'], '規格要寬口，來源是小口'),
]

rows = []
for pid in P:
    for slot in SLOT_AXES:
        ref = refs(pid)[slot]
        read = R[ref].get(SLOT_KEY[slot], '')
        spec = '；'.join(f'{a}={P[pid]["axes"][a]}' for a in SLOT_AXES[slot])
        flags = []
        for s, want, bad, why in RULES:
            if s != slot: continue
            if want in spec and any(b in read for b in bad):
                flags.append(why)
        rows.append({'persona': pid, 'slot': slot, 'ref': ref,
                     'usability': R[ref]['usability'], 'spec': spec,
                     'readout': read, 'contradictions': flags})

if __name__ == '__main__':
    if '--json' in sys.argv:
        json.dump(rows, sys.stdout, ensure_ascii=False, indent=1); sys.exit()
    bad = [r for r in rows if r['contradictions']]
    low = [r for r in rows if r['usability'] == 'low']
    print(f"三槽共 {len(rows)} 個指派")
    print(f"  用 low 來源：{len(low)} 個")
    print(f"  規格與來源明確矛盾：{len(bad)} 個\n")
    for r in bad:
        print(f"  ✗ {r['persona']:16s} {r['slot']:16s} {r['ref']} ({r['usability']})")
        print(f"      規格：{r['spec']}")
        print(f"      來源：{r['readout'][:70]}")
        for f in r['contradictions']:
            print(f"      → {f}")
