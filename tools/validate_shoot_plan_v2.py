#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shoot Plan Validator v2 — 語意 + 反作弊版

v1 只驗數字（張數、比例、連續重複），因此出現「validator PASS 但計畫其實不成立」：
  - scene 文字寫的衣服與 outfit_id 不同（12/260 列）
  - scene 寫濕髮但 hair_id 指向盤髮（14/260 列）
  - 文件說 B 級 7–8，validator 沒驗，15/20 位是 B=9 仍判 PASS
  - 為了湊 A>=2，把「早上煮咖啡」標成 A 級
  - 濾鏡與視角被演算法綁定列號，20 位的第 1 列全是 meitu＋自拍

v2 的規則來源是機器可讀的 spec（本檔 + location_registry.json），文件由 spec 產生，
不再出現「文件一套規則、validator 另一套規則」。
"""
import json, sys, re, collections

WEAR = re.compile(r'(針織|襯衫|背心|洋裝|短裙|長裙|褲|外套|帽T|大學T|西裝|睡衣|睡袍|浴衣|'
                  r'比基尼|泳衣|吊帶|圍裙|制服|和服|旗袍|罩衫|polo|球衣|賽車服|女僕裝)')
HAIRW = re.compile(r'(濕髮|馬尾|丸子|盤起|盤髮|髮髻|辮|放下|塞耳後|公主切|鮑伯|瀏海)')
FILTW = re.compile(r'(濾鏡|CCD|美圖|直出|畫質|銳利|顆粒)')
VIDEO = re.compile(r'(一鏡到底|連換|縮時|過程|從.{1,6}到.{1,6}的變化)')
MULTI = re.compile(r'(另一天|同行程|以及|，還有)')

def ratio_ok(v, spec):
    m=re.match(r'^(>=|<=)(\d+)$', str(spec))
    return None if not m else (v>=int(m.group(2)) if m.group(1)=='>=' else v<=int(m.group(2)))

def validate(pilot, registry):
    err=[]; warn=[]
    shots=pilot['phase_c_shots']; q=pilot['phase_c_quota']
    n=len(shots)
    if n!=q['shots']: err.append(f"張數 {n} != {q['shots']}")

    outfits=pilot['outfits']; hairs=pilot['hair']

    # --- 語意衝突：scene 不得重寫 outfit / hair / filter ---
    for s in shots:
        sc=s['scene']
        if WEAR.search(sc): err.append(f"{s['shot_id']} scene 出現服裝詞『{WEAR.search(sc).group()}』——服裝只能來自 outfit_id")
        if HAIRW.search(sc): err.append(f"{s['shot_id']} scene 出現髮型詞『{HAIRW.search(sc).group()}』——髮型只能來自 hair_id")
        if FILTW.search(sc): err.append(f"{s['shot_id']} scene 出現濾鏡/畫質描述——只能來自 filter")
        if VIDEO.search(sc): err.append(f"{s['shot_id']} scene 使用影片語言『{VIDEO.search(sc).group()}』——單張圖必須是 frozen moment")
        if MULTI.search(sc): err.append(f"{s['shot_id']} scene 含多個時空『{MULTI.search(sc).group()}』——一列只能有一個時空")
        if s['outfit_id'] not in outfits: err.append(f"{s['shot_id']} 未知 outfit_id {s['outfit_id']}")
        if s['hair_id'] not in hairs: err.append(f"{s['shot_id']} 未知 hair_id {s['hair_id']}")
        # 光線五段
        lt=s['light']
        for f in ['family','key','bounce','bounce_type','exposure_choice']:
            if not lt.get(f): err.append(f"{s['shot_id']} light.{f} 缺漏")
        if lt.get('bounce_type')=='specular' and '補' in str(lt.get('bounce','')):
            warn.append(f"{s['shot_id']} 用 specular 反射面當柔和填光——鏡面/金屬會產生高光，不像白牆能整體補亮")
        # full_body 不可 shallow DOF
        if s['framing']=='full_body' and s['camera']['depth_of_field']=='shallow':
            err.append(f"{s['shot_id']} full_body 不可用 shallow DOF（身體輪廓會糊）")

    # --- 地點層級由 registry 決定 ---
    tiers=[]
    for s in shots:
        t=registry['tiers'].get(s['location'])
        if t is None: err.append(f"{s['shot_id']} location『{s['location']}』不在 registry")
        if s.get('location_tier_override'):
            if not s.get('location_tier_override_reason'):
                err.append(f"{s['shot_id']} 有 tier override 但沒寫 reason")
            t=s['location_tier_override']
        tiers.append(t)
    c=collections.Counter(tiers)
    if c['C'] < q['location_tier']['C_min']:
        err.append(f"C 級 {c['C']} < 下限 {q['location_tier']['C_min']}")

    # --- 身分覆蓋 ---
    ic=q['identity_coverage']
    yaw=collections.Counter(s['head_yaw'] for s in shots)
    for k,spec in ic['head_yaw'].items():
        v = sum(v2 for k2,v2 in yaw.items() if k2.startswith('profile')) if k=='profile_any' else yaw[k]
        if ratio_ok(v,spec) is False: err.append(f"head_yaw {k}={v}，需 {spec}")
    fr=collections.Counter(s['framing'] for s in shots)
    for k,spec in ic['framing'].items():
        if ratio_ok(fr[k],spec) is False: err.append(f"framing {k}={fr[k]}，需 {spec}")
    if len(set(s['body_pose'] for s in shots)) < int(ic['body_pose_distinct'][2:]):
        err.append(f"body_pose 只有 {len(set(s['body_pose'] for s in shots))} 種，需 {ic['body_pose_distinct']}")
    if len(set(s['expression'] for s in shots)) < int(ic['expression_distinct'][2:]):
        err.append(f"expression 只有 {len(set(s['expression'] for s in shots))} 種，需 {ic['expression_distinct']}")
    unob=sum(1 for s in shots if s['face_visibility']=='unobstructed')
    if ratio_ok(unob, ic['face_visibility_unobstructed']) is False:
        err.append(f"臉部無遮擋 {unob} 張，需 {ic['face_visibility_unobstructed']}")

    # --- 造型 ---
    od=len(set(s['outfit_id'] for s in shots))
    if od < q['outfit_distinct_min']: err.append(f"outfit 只用 {od} 種，需 >= {q['outfit_distinct_min']}")
    if q.get('hair_all_variants_used'):
        miss=set(hairs)-set(s['hair_id'] for s in shots)
        if miss: err.append(f"未用到的髮型變體：{sorted(miss)}")

    # --- 招牌世界 / 職業（換衣服逃不掉）---
    sf=sum(1 for s in shots if s.get('signature_family'))
    if sf/n > q['signature_family_max_ratio']:
        err.append(f"signature_family {sf}/{n}={sf/n:.0%} > {q['signature_family_max_ratio']:.0%}")
    cr=sum(1 for s in shots if s.get('career_related'))
    if cr/n > q['career_related_max_ratio']:
        err.append(f"career_related {cr}/{n}={cr/n:.0%} > {q['career_related_max_ratio']:.0%}")

    # --- 視角 / 濾鏡 ---
    tp=sum(1 for s in shots if s['view']=='third_person')
    if ratio_ok(tp,q['view']['third_person']) is False: err.append(f"third_person {tp}，需 {q['view']['third_person']}")
    sel=n-tp
    if ratio_ok(sel,q['view']['selfie_total']) is False: err.append(f"自拍合計 {sel}，需 {q['view']['selfie_total']}")
    fc=collections.Counter(s['filter'] for s in shots)
    for k,spec in q['filter'].items():
        if k.startswith('_'): continue
        v=fc[k]
        if isinstance(spec,int):
            if v!=spec: err.append(f"filter {k}={v}，需 {spec}")
        elif ratio_ok(v,spec) is False: err.append(f"filter {k}={v}，需 {spec}")
    for s in shots:
        if s['filter']=='ccd' and s['framing']=='full_body':
            err.append(f"{s['shot_id']} CCD 不可用在 full_body（臉部解析度不足）")

    # --- 反作弊：不完美攝影變數不可全部相同 ---
    for f in ['composition','white_balance','background_clutter']:
        vals=set(s.get('imperfection_profile',{}).get(f) for s in shots)
        if len(vals)<2: warn.append(f"imperfection_profile.{f} 13 張全部相同——真人照片不會這樣")
    fams=set(s['light']['family'] for s in shots)
    if len(fams)<4: err.append(f"lighting family 只有 {len(fams)} 種，需 >=4（避免每張都是同一種漂亮的物理光）")
    return err,warn

if __name__=='__main__':
    pilot=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'pilot/nico_pilot.json',encoding='utf-8'))
    reg=json.load(open('pilot/location_registry.json',encoding='utf-8'))
    err,warn=validate(pilot,reg)
    print(f"驗證 {pilot['persona_id']}（schema v{pilot['schema_version']}）")
    for w in warn: print("  ⚠ ",w)
    if err:
        for e in err: print("  ✗ ",e)
        sys.exit(1)
    print("  ✓ 全數通過")
