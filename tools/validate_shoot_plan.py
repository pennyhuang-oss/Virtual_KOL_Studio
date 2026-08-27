#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""驗證 MODELING_SHOOT_PLAN.md 的 13 張訓練集是否符合 WARDROBE_SYSTEM.md 與
PERSONA_CANON.md 的硬性配額。用法：python3 tools/validate_shoot_plan.py shoot.json

規則來源：
  WARDROBE_SYSTEM.md 轉盤 1–4、地點層級配額
  SEXY_SCENE_LIBRARY.md 第 2b 點（濾鏡變化）、第 7 點（自拍/他拍比例）
"""
import json, sys

def validate(S):
    bad=[]
    for k,v in S.items():
        tr=v['train']; n=len(tr)
        tier=[x[2] for x in tr]; outfit=[x[3] for x in tr]
        pov=[x[7] for x in tr]; filt=[x[8] for x in tr]
        if n!=13:                      bad.append((k,'訓練集應為 13 張',n))
        if len(v['spectrum'])!=8:      bad.append((k,'風格光譜應為 8 種',len(v['spectrum'])))
        if len(v['hair'])!=5:          bad.append((k,'髮型應為 5 種',len(v['hair'])))
        if tier.count('C')<2:          bad.append((k,'C 級「完全不美的日常」硬性下限 2',tier.count('C')))
        if tier.count('A')<2:          bad.append((k,'A 級「嚮往感」應 ≥2',tier.count('A')))
        if len(set(outfit))<8:         bad.append((k,'應涵蓋 8 種穿搭區間',len(set(outfit))))
        cap=int(n*0.30)
        top=max(outfit.count(x) for x in set(outfit))
        if top>cap:                    bad.append((k,f'單一造型不得超過 30%（上限 {cap}）',top))
        sc=sum(1 for p in pov if '自拍' in p)
        if not 4<=sc<=5:               bad.append((k,'自拍應 4–5 張',sc))
        if filt.count('ccd')!=2:       bad.append((k,'CCD 質感應 2 張',filt.count('ccd')))
        if filt.count('meitu')!=1:     bad.append((k,'美圖濾鏡應 1 張',filt.count('meitu')))
        for i in range(1,n):
            if outfit[i]==outfit[i-1]: bad.append((k,'連續兩張不得同一穿搭區間',f'#{i+1}'))
            if tr[i][4]==tr[i-1][4]:   bad.append((k,'連續兩張不得同一髮型',f'#{i+1}'))
    return bad

if __name__=='__main__':
    path = sys.argv[1] if len(sys.argv)>1 else 'shoot.json'
    S=json.load(open(path,encoding='utf-8'))
    bad=validate(S)
    print(f"檢查 {len(S)} 位 × 13 張：")
    if not bad:
        print("  ✓ 全數通過"); sys.exit(0)
    for b in bad: print("  ✗",b)
    sys.exit(1)
