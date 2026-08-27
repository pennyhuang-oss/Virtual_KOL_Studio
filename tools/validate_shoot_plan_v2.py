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

    # --- 訓練張數必須落在實際 endpoint 範圍 ---
    pf=pilot.get('training_endpoint_preflight')
    if not pf:
        err.append("缺 training_endpoint_preflight——不可用歷史成功紀錄推定目前 endpoint 的張數限制")
    else:
        lo,hi=pf['min_training_images'],pf['max_training_images']
        if not lo<=n<=hi: err.append(f"訓練張數 {n} 不在 endpoint 允許範圍 {lo}-{hi}（{pf['verified_at']} 實查）")

    # --- 訓練圖必須 identity_safe：臉不能糊 ---
    for s2 in shots:
        ip=s2.get('imperfection_profile',{})
        if ip.get('identity_safe') is not True: err.append(f"{s2['shot_id']} imperfection_profile.identity_safe 必須為 true")
        if ip.get('face_motion_blur') is True: err.append(f"{s2['shot_id']} 訓練圖不可有 face_motion_blur")
        if ip.get('face_detail_preserved') is not True: err.append(f"{s2['shot_id']} 訓練圖必須 face_detail_preserved")

    # --- 乾淨身分錨點下限 ---
    ca=q.get('clean_anchor_min',{})
    def clean(s2): return (s2['filter']=='none' and s2['face_visibility']=='unobstructed'
                           and s2['light']['family'] in ('L2_single_window_daylight','L6_soft_overcast')
                           and s2['camera']['type']=='phone_rear')
    cf=sum(1 for s2 in shots if s2['framing']=='face_closeup' and clean(s2))
    if cf < ca.get('face_closeup_clean',0): err.append(f"乾淨 face_closeup 只有 {cf}，需 >= {ca['face_closeup_clean']}")
    ob=pilot['outfits']
    fb=sum(1 for s2 in shots if s2['framing']=='full_body' and ob[s2['outfit_id']]['body_readable'] and clean(s2))
    if fb < ca.get('full_body_body_readable',0): err.append(f"乾淨且 body_readable 的全身只有 {fb}，需 >= {ca['full_body_body_readable']}")
    rs=sum(1 for s2 in shots if s2['head_yaw'].startswith('right') and clean(s2)
           and s2['framing'] in ('face_closeup','chest_up'))
    if rs < ca.get('right_side_clean',0): err.append(f"乾淨的右側高資訊角度只有 {rs}，需 >= {ca['right_side_clean']}")

    # --- 困難光線上限 ---
    hl=q.get('harsh_light_max',{})
    for fam,mx in hl.items():
        if fam.startswith('_'): continue
        v=sum(1 for s2 in shots if s2['light']['family']==fam)
        if v>mx: err.append(f"{fam} 有 {v} 張 > 上限 {mx}（官方 training guidance 偏向 clear/well-lit）")

    # --- anchor 不可落在角色的招牌世界或住處 ---
    HOME={'own_bedroom','own_kitchen','own_entryway','own_bathroom','own_living_room','own_balcony'}
    for s2 in shots:
        if s2.get('pillar')=='anchor' and (s2['location'] in HOME or registry.get('defaults',{}).get(s2['location'])):
            err.append(f"{s2['shot_id']} 是 identity anchor，不可放在住處或職業空間（會把最強身分訊號綁在該場景）")

    # --- signature_family / career_related 由 registry 推導 ---
    key=pilot.get('signature_family_key')
    for s2 in shots:
        dflt=registry.get('defaults',{}).get(s2['location'])
        exp_sf = (dflt['signature_family'].replace('{persona_workplace}',key) if dflt else None)
        exp_cr = bool(dflt['career_related_default']) if dflt else False
        if s2.get('signature_family')!=exp_sf and not s2.get('label_override_reason'):
            err.append(f"{s2['shot_id']} signature_family={s2.get('signature_family')}，registry 推導應為 {exp_sf}（要改需填 label_override_reason）")
        if bool(s2.get('career_related'))!=exp_cr and not s2.get('label_override_reason'):
            err.append(f"{s2['shot_id']} career_related={s2.get('career_related')}，registry 推導應為 {exp_cr}（要改需填 label_override_reason）")

    # --- Phase A / B / D gate ---
    pa=pilot.get('phase_a',{}); ic2=pa.get('identical_across_all_four',{})
    if pa.get('count')!=4: err.append("Phase A 必須是 4 個候選 identity")
    if ic2.get('framing')!='knee_up': err.append("Phase A framing 必須 knee_up（臉＋腰臀輪廓同時可判）")
    if ic2.get('camera',{}).get('depth_of_field')!='adequate': err.append("Phase A DOF 必須 adequate")
    ao=ic2.get('outfit_id')
    if ao and not pilot['outfits'][ao].get('body_readable'): err.append(f"Phase A 選角服 {ao} 必須 body_readable=true")
    if ao and not pilot['outfits'][ao].get('neckline'): err.append(f"Phase A 選角服 {ao} 必須明寫 neckline")
    pb=pilot.get('phase_b',{})
    if not (pb.get('B1') and pb.get('B2')): err.append("Phase B 必須有 B1 與 B2 兩張")
    elif pb['B2'].get('framing')!='full_body': err.append("Phase B 的 B2 必須是 full_body（身材比例最終把關）")
    pd=pilot.get('phase_d_stress_test',{})
    if len(pd.get('shots',[]))!=pd.get('count'): err.append("Phase D count 與實際 shots 數不符")
    ids={x['id'] for x in pd.get('shots',[])}
    if 'st00' not in ids: err.append("Phase D 缺 st00 乾淨基準線（其他 stress shot 沒有比較基準）")
    rub=pilot.get('soul_qa_rubric',{})
    if not rub.get('hard_gates'): err.append("QA rubric 缺 hard_gates（總分會掩蓋關鍵失敗）")

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
