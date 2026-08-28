#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 nico_pilot.json 自動產生覆核包。

存在理由：R2 覆核包的統計是我人工抄的，結果與 JSON 漂移——
寫「4 張工作室 4 張房間」實際是 3+3、寫「5 種 lighting、L1×3」實際是 6 種 L1×5。
上一輪才剛修掉 scene/ID 的雙重真理來源，統計又在文件層漂一次。
所有 count / ratio / distribution 一律由本程式計算，覆核包只手寫 rationale 與 known risk。
"""
import json, collections, subprocess, sys

def sh(c):
    try: return subprocess.run(c,shell=True,capture_output=True,text=True).stdout.strip()
    except Exception: return "(unavailable)"

def stats(d, reg):
    S=d['phase_c_shots']; n=len(S)
    HOME={'own_bedroom','own_kitchen','own_entryway','own_bathroom','own_living_room','own_balcony'}
    anchors=[s for s in S if s.get('pillar')=='anchor']
    def clean(s): return (s['filter']=='none' and s['face_visibility']=='unobstructed'
        and s['light']['family'] in ('L2_single_window_daylight','L6_soft_overcast')
        and s['camera']['type']=='phone_rear')
    ob=d['outfits']
    loc=collections.Counter(s['location'] for s in S)
    return {
     'n':n,
     'anchors':len(anchors),
     'lifestyle':n-len(anchors),
     'lighting':collections.Counter(s['light']['family'] for s in S),
     'framing':collections.Counter(s['framing'] for s in S),
     'yaw':collections.Counter(s['head_yaw'] for s in S),
     'pose':collections.Counter(s['body_pose'] for s in S),
     'view':collections.Counter(s['view'] for s in S),
     'filter':collections.Counter(s['filter'] for s in S),
     'tier':collections.Counter(reg['tiers'].get(s['location']) for s in S),
     'loc':loc,
     'outfit':collections.Counter(s['outfit_id'] for s in S),
     'hair':collections.Counter(s['hair_id'] for s in S),
     'home_studio':sum(v for k,v in loc.items() if k in HOME)+loc.get('workplace_own_studio',0),
     'anchor_in_home_or_work':sum(1 for s in anchors if s['location'] in HOME or reg.get('defaults',{}).get(s['location'])),
     'clean_face':sum(1 for s in S if s['framing']=='face_closeup' and clean(s)),
     'clean_fullbody':sum(1 for s in S if s['framing']=='full_body' and ob[s['outfit_id']]['body_readable'] and clean(s)),
     'clean_right':sum(1 for s in S if s['head_yaw'].startswith('right') and clean(s) and s['framing'] in ('face_closeup','chest_up')),
     'career':sum(1 for s in S if s['career_related']),
     'signature':sum(1 for s in S if s['signature_family']),
     'expressions':len(set(s['expression'] for s in S)),
    }

def fmt(c,total=None):
    return "、".join(f"`{k}` {v}" + (f"（{v/total:.0%}）" if total else "") for k,v in c.most_common())

if __name__=='__main__':
    d=json.load(open('pilot/nico_pilot.json',encoding='utf-8'))
    reg=json.load(open('pilot/location_registry.json',encoding='utf-8'))
    st=stats(d,reg)
    print(json.dumps({k:(dict(v) if isinstance(v,collections.Counter) else v) for k,v in st.items()},
                     ensure_ascii=False,indent=1))
