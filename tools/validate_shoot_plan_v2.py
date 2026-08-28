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

# ---- C-15：schema_v2.json 必須被實際執行，不能只是文件 ----
POSE_WORDS={'seated':['坐','坐著','坐下'],'standing':['站','站著'],'crouching':['蹲'],
            'lying':['躺','趴'],'leaning':['靠','撐著'],'walking_frozen':['走','越過']}

def _resolve(spec, schema):
    """最小 $ref 解析（只支援 #/definitions/x）。"""
    while '$ref' in spec:
        ref=spec['$ref']
        assert ref.startswith('#/'), ref
        node=schema
        for part in ref[2:].split('/'): node=node[part]
        spec=node
    return spec

def _walk(obj, spec, path, sid, schema, e):
    spec=_resolve(spec, schema)
    for k in spec.get('required',[]):
        if k not in obj: e.append(f"{sid} 缺必填欄位 {path}{k}")
    known=set(spec.get('properties',{}))
    if not known:
        return   # schema 未宣告 properties 的 object 視為自由格式，不做未定義欄位檢查
    for k,v in obj.items():
        if k not in known:
            if not k.startswith('_'): e.append(f"{sid} 有未定義欄位 {path}{k}（打字錯誤會被靜默忽略，故視為錯誤）")
            continue
        ps=_resolve(spec['properties'][k], schema)
        enum=ps.get('enum')
        if enum and v not in enum:
            e.append(f"{sid} {path}{k}='{v}' 不是合法值，允許：{enum}")
        t=ps.get('type')
        if t=='array' and isinstance(v,list):
            mi=ps.get('minItems')
            if mi and len(v)<mi: e.append(f"{sid} {path}{k} 只有 {len(v)} 項，至少需 {mi}")
            if 'items' in ps:
                for i,it in enumerate(v):
                    if isinstance(it,dict): _walk(it, ps['items'], f"{path}{k}[{i}].", sid, schema, e)
        elif t=='object' and isinstance(v,dict):
            _walk(v, ps, f"{path}{k}.", sid, schema, e)
        elif t=='integer' and isinstance(v,int) and ps.get('minimum') is not None and v<ps['minimum']:
            e.append(f"{sid} {path}{k}={v} 小於下限 {ps['minimum']}")

def schema_check_full(pilot, schema):
    """C-15：從頂層開始驗，phase_c_shots 透過 $ref 綁到 definitions.shot。
    先前只有 definitions.shot、頂層沒連過去，非法 enum 與空 props 會整個放過。"""
    e=[]
    for k in schema.get('required',[]):
        if k not in pilot: e.append(f"pilot 缺頂層必填欄位 {k}")
    arr=schema['properties']['phase_c_shots']
    n=len(pilot.get('phase_c_shots',[]))
    if arr.get('minItems') and n<arr['minItems']: e.append(f"phase_c_shots {n} 張 < 下限 {arr['minItems']}")
    if arr.get('maxItems') and n>arr['maxItems']: e.append(f"phase_c_shots {n} 張 > 上限 {arr['maxItems']}")
    for sh_ in pilot.get('phase_c_shots',[]):
        _walk(sh_, arr['items'], "", sh_.get('shot_id','(no id)'), schema, e)
    st=pilot.get('phase_d_stress_test')
    if st: _walk(st, schema['properties']['phase_d_stress_test'], "phase_d.", "phase_d", schema, e)
    # 唯一性
    for path,key in schema.get('x-uniqueKeys',{}).items():
        node=pilot
        for part in path.split('.'): node=(node or {}).get(part) if isinstance(node,dict) else None
        if isinstance(node,list):
            ids=[x.get(key) for x in node if isinstance(x,dict)]
            dup=[i for i in set(ids) if ids.count(i)>1]
            if dup: e.append(f"{path} 的 {key} 重複：{dup}")
    return e

def schema_check(pilot, schema):
    """對 phase_c_shots 逐列比對 schema 的 required / enum / minItems。
    先前只驗業務規則，非法 enum（framing='SUPER_ZOOM'）與空 props 會整個放過——
    對抗測試證實 validator 仍 PASS，只抓到下游的計數變化。"""
    e=[]
    sh=schema['definitions']['shot']; props=sh['properties']; req=sh['required']
    def walk(obj, spec, path, shot_id):
        for k in spec.get('required',[]):
            if k not in obj: e.append(f"{shot_id} 缺必填欄位 {path}{k}")
        for k,v in obj.items():
            ps=spec.get('properties',{}).get(k)
            if not ps: continue
            enum=ps.get('enum')
            if enum and v not in enum:
                e.append(f"{shot_id} {path}{k}='{v}' 不是合法值，允許：{enum}")
            if ps.get('type')=='array' and isinstance(v,list):
                mi=ps.get('minItems')
                if mi and len(v)<mi: e.append(f"{shot_id} {path}{k} 只有 {len(v)} 項，至少需 {mi}")
            if ps.get('type')=='object' and isinstance(v,dict):
                walk(v, ps, f"{path}{k}.", shot_id)
    for sh_ in pilot['phase_c_shots']:
        sid=sh_.get('shot_id','(no id)')
        for k in req:
            if k not in sh_: e.append(f"{sid} 缺必填欄位 {k}")
        walk(sh_, sh, "", sid)
    return e

def pose_conflicts(shots):
    """C-16：scene 描述的姿態與 body_pose 欄位不符。
    a01/a02 的 scene 寫「坐著」，欄位卻是 standing——搬場景時只改了文字沒改欄位，
    與 v1 rebalancer 同一類錯誤。"""
    e=[]
    for s in shots:
        sc=s['scene']; bp=s['body_pose']
        for pose,words in POSE_WORDS.items():
            if pose==bp: continue
            if any(w in sc for w in words) and not any(w in sc for w in POSE_WORDS.get(bp,[])):
                e.append(f"{s['shot_id']} scene 讀起來是『{words[0]}』，但 body_pose='{bp}'")
                break
    return e

def validate(pilot, registry, schema=None):
    err=[]; warn=[]
    if schema:
        err += schema_check_full(pilot, schema)
    err += pose_conflicts(pilot['phase_c_shots'])
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

    # --- C-23/C-27/C-29：結構化 props 與 hands ---
    # framing 能看到哪些 zone。background 一律可見；zone 由作者依該 shot 的實際姿態指定，
    # 不是套「站姿公式」——蹲著時地上的紙箱就在膝線，不在腳下。
    FRAME_ZONES={'face_closeup':{'head'},
                 'chest_up':{'head','chest'},
                 'waist_up':{'head','chest','waist'},
                 'knee_up':{'head','chest','waist','hip','knee'},
                 'full_body':{'head','chest','waist','hip','knee','floor'}}
    REL={'held_left','held_right','held_both','surface','worn','background'}
    ST={'free','holding','supporting','camera'}
    ALLBAGS={o.get('outer_or_bag') for o in outfits.values()} - {'無','（連身）',None,''}
    for s in shots:
        sid=s['shot_id']; o=outfits[s['outfit_id']]
        if s['framing'] not in FRAME_ZONES: continue   # 非法 framing 由 schema 檢查負責
        props=s.get('props') or []
        if not all(isinstance(x,dict) for x in props):
            err.append(f"{sid} props 必須是結構化物件（id/name/relation/zone/expected_visible，C-27）"); continue
        pid={x['id']:x for x in props}
        if len(pid)!=len(props): err.append(f"{sid} props 有重複 id")
        own={x for x in (o.get('outer_or_bag'),o.get('jewelry')) if x and x!='無'}
        for x in props:
            if x['relation'] not in REL: err.append(f"{sid} props[{x['id']}].relation='{x['relation']}' 非法")
            if x['zone']!='background' and x['zone'] not in FRAME_ZONES['full_body']:
                err.append(f"{sid} props[{x['id']}].zone='{x['zone']}' 非法")
            for b in own:
                if b in x['name'] or x['name'] in b:
                    err.append(f"{sid} props『{x['name']}』重述了 outfit 已提供的『{b}』（C-23）")
            for b in ALLBAGS-own:
                if b in x['name'] or x['name'] in b:
                    err.append(f"{sid} props『{x['name']}』是另一套 outfit 的招牌包/外套『{b}』（C-23）")
            # C-29：宣告可見就必須真的落在 framing 內
            if x.get('expected_visible') and x['zone']!='background' \
               and x['zone'] not in FRAME_ZONES[s['framing']]:
                err.append(f"{sid} props『{x['name']}』zone={x['zone']}，"
                           f"但 framing={s['framing']} 只看得到 {sorted(FRAME_ZONES[s['framing']])}"
                           f"——宣告可見卻在裁切外，這個微物件對出圖毫無作用（C-29）")
        h=s.get('hands')
        if not isinstance(h,dict) or set(h)!={'left','right'}:
            err.append(f"{sid} hands 必須是 left/right 兩個槽位（C-27）"); continue
        refs=[]
        for side in ('left','right'):
            sl=h[side]
            if not isinstance(sl,dict) or sl.get('state') not in ST:
                err.append(f"{sid} hands.{side}.state 必須是 {sorted(ST)}（C-27）"); continue
            ref=sl.get('object_ref')
            if sl['state']=='holding':
                if ref not in pid:
                    err.append(f"{sid} hands.{side} state=holding，object_ref『{ref}』不是本列的 prop id"
                               f"——不得用同義詞另寫（C-27）"); continue
                want={'held_'+side,'held_both'}
                if pid[ref]['relation'] not in want:
                    err.append(f"{sid} hands.{side} 拿著『{pid[ref]['name']}』，"
                               f"但該 prop 的 relation={pid[ref]['relation']}，應為 {sorted(want)}（C-27）")
                refs.append(ref)
            else:
                if ref is not None:
                    err.append(f"{sid} hands.{side}.state={sl['state']} 不應有 object_ref（C-27）")
                if sl['state']=='camera' and s['view'] not in ('selfie_front','selfie_mirror'):
                    err.append(f"{sid} 不是自拍，手上卻標了 camera")
        # 一手一物：同一 prop 被兩手引用，只有 held_both 允許
        for r in set(refs):
            if refs.count(r)>1 and pid[r]['relation']!='held_both':
                err.append(f"{sid} prop『{pid[r]['name']}』被兩隻手同時引用，但 relation 不是 held_both（C-27）")
        cam=sum(1 for side in ('left','right') if h[side].get('state')=='camera')
        if s['view'] in ('selfie_front','selfie_mirror') and cam!=1:
            err.append(f"{sid} 是 {s['view']}，camera hand 有 {cam} 隻——自拍必須且只能占掉一隻手（C-27）")
        # 反向：宣告拿在手上的 prop，必須真的被某一手引用
        for x in props:
            if x['relation'].startswith('held_') and x['id'] not in refs:
                err.append(f"{sid} props『{x['name']}』relation={x['relation']}，"
                           f"但沒有任何一隻手引用它——不是漏掉，就是第三隻手（C-27）")
        # 拍攝裝置不得同時是入鏡 prop
        if cam and any('手機' in x['name'] for x in props):
            err.append(f"{sid} 手機是拍攝裝置，不得同時列為入鏡 prop（畫面會出現第二支手機）")

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

    # --- C-18：signature_family / career_related 各自獨立 override，且 quota 用 effective value ---
    key=pilot.get('signature_family_key')
    eff_sf=[]; eff_cr=[]
    for s2 in shots:
        dflt=registry.get('defaults',{}).get(s2['location'])
        exp_sf = (dflt['signature_family'].replace('{persona_workplace}',key) if dflt else None)
        exp_cr = bool(dflt['career_related_default']) if dflt else False
        if s2.get('signature_family')!=exp_sf:
            if not s2.get('label_override_signature_reason'):
                err.append(f"{s2['shot_id']} signature_family={s2.get('signature_family')}，registry 推導應為 {exp_sf}"
                           f"（要偏離需填 label_override_signature_reason，不能靠另一欄的理由順帶放行）")
            eff_sf.append(s2.get('signature_family'))
        else:
            eff_sf.append(exp_sf)
        if bool(s2.get('career_related'))!=exp_cr:
            if not s2.get('label_override_career_reason'):
                err.append(f"{s2['shot_id']} career_related={s2.get('career_related')}，registry 推導應為 {exp_cr}"
                           f"（要偏離需填 label_override_career_reason）")
            eff_cr.append(bool(s2.get('career_related')))
        else:
            eff_cr.append(exp_cr)
    # quota 一律以 effective value 計算，不用使用者填的值——否則錯誤 override 可壓低比例
    sf_e=sum(1 for x in eff_sf if x); cr_e=sum(1 for x in eff_cr if x)
    if sf_e/n > q['signature_family_max_ratio']:
        err.append(f"signature_family(effective) {sf_e}/{n}={sf_e/n:.0%} > {q['signature_family_max_ratio']:.0%}")
    if cr_e/n > q['career_related_max_ratio']:
        err.append(f"career_related(effective) {cr_e}/{n}={cr_e/n:.0%} > {q['career_related_max_ratio']:.0%}")

    # --- K-03：世界集中度（全體 + lifestyle 子集 + 三重固定組合）---
    hw_all=[s2 for s2 in shots if s2['location'] in HOME or registry.get('defaults',{}).get(s2['location'])]
    life=[s2 for s2 in shots if s2.get('pillar')!='anchor']
    hw_life=[s2 for s2 in life if s2['location'] in HOME or registry.get('defaults',{}).get(s2['location'])]
    wq=q.get('world_concentration_max',{})
    if wq:
        if len(hw_all)/n > wq['overall']:
            err.append(f"home+work 全體 {len(hw_all)}/{n}={len(hw_all)/n:.0%} > {wq['overall']:.0%}")
        if life and len(hw_life)/len(life) > wq['lifestyle_subset']:
            err.append(f"home+work 在 lifestyle 子集 {len(hw_life)}/{len(life)}={len(hw_life)/len(life):.0%}"
                       f" > {wq['lifestyle_subset']:.0%}（訓練 endpoint 不知道 pillar=anchor，不會自動降權）")
    combo=collections.defaultdict(list)
    for s2 in shots: combo[(s2['location'],s2['outfit_id'],s2['hair_id'])].append(s2)
    for k2,v2 in combo.items():
        if len(v2)<2: continue
        if all(x.get('pillar')=='anchor' for x in v2): continue   # anchor 之間刻意同規格，是控制組
        err.append(f"location+outfit+hair 固定組合重複：{k2} → {[x['shot_id'] for x in v2]}"
                   f"（anchor 之間可以重複，anchor 與 lifestyle 或 lifestyle 之間不行）")

    # --- C-07：任何內嵌的衍生統計都要與實況一致（人工宣告是漂移的來源）---
    import re as _re
    struct=q.get('structure','')
    m=_re.search(r'(\d+)\s*clean identity anchors?\s*\+\s*(\d+)\s*lifestyle', struct)
    if m:
        a_dec,l_dec=int(m.group(1)),int(m.group(2))
        a_act=sum(1 for x in shots if x.get('pillar')=='anchor')
        if a_dec!=a_act or l_dec!=n-a_act:
            err.append(f"phase_c_quota.structure 宣告 {a_dec}+{l_dec}，實況是 {a_act}+{n-a_act}（C-07 漂移）")
    if q.get('shots')!=n:
        err.append(f"phase_c_quota.shots={q.get('shots')} 與實際 {n} 張不符")
    blob=json.dumps(pilot,ensure_ascii=False)
    for bad_key in ('dominant_training_outfit',):
        if f'"{bad_key}"' in blob:
            err.append(f"不得內嵌人工宣告的衍生統計 `{bad_key}`——一律由 tools/gen_pilot_review.py 計算（C-07）")

    # --- Phase A / B / D gate ---
    pa=pilot.get('phase_a',{}); ic2=pa.get('identical_across_all_four',{})
    if pa.get('count')!=4: err.append("Phase A 必須是 4 個候選 identity")
    if ic2.get('framing')!='knee_up': err.append("Phase A framing 必須 knee_up（臉＋腰臀輪廓同時可判）")
    if ic2.get('camera',{}).get('depth_of_field')!='adequate': err.append("Phase A DOF 必須 adequate")
    ao=ic2.get('outfit_id')
    if ao and not pilot['outfits'][ao].get('body_readable'): err.append(f"Phase A 選角服 {ao} 必須 body_readable=true")
    if ao and not pilot['outfits'][ao].get('neckline'): err.append(f"Phase A 選角服 {ao} 必須明寫 neckline")
    # C-09：A 四候選必須除 identity 外完全同規格
    need_same={'framing','head_yaw','body_pose','view','outfit_id','hair_id','location','camera','light','filter'}
    miss=need_same-set(ic2)
    if miss: err.append(f"Phase A 的 identical_across_all_four 缺少必須固定的欄位：{sorted(miss)}")
    if 'identity' not in str(pa.get('varies_only','')):
        err.append("Phase A 的 varies_only 必須明寫唯一變數是 identity")

    # C-09：B2 必須真的更換場景／穿搭／髮型／光線，否則只驗到「能不能重現」
    pb=pilot.get('phase_b',{})
    if not (pb.get('B1') and pb.get('B2')):
        err.append("Phase B 必須有 B1 與 B2 兩張")
    else:
        if pb['B2'].get('framing')!='full_body':
            err.append("Phase B 的 B2 必須是 full_body（身材比例最終把關）")
        same=[k for k in ('location','outfit_id','hair_id','light') if str(pb['B1'].get(k))==str(pb['B2'].get(k))]
        if same:
            err.append(f"Phase B 的 B2 與 B1 在 {same} 相同——B2 的目的是驗『輕度 generalize』，"
                       f"若同場景同服裝同光線只驗到『能不能重現』")

    # C-09：Phase D 結構完整性
    pd=pilot.get('phase_d_stress_test',{})
    dshots=pd.get('shots',[])
    if len(dshots)!=pd.get('count'): err.append("Phase D count 與實際 shots 數不符")
    ids={x['id'] for x in dshots}
    if 'st00' not in ids: err.append("Phase D 缺 st00 乾淨基準線（其他 stress shot 沒有比較基準）")
    rub=pilot.get('soul_qa_rubric',{})
    rub_items=set(rub.get('items',[]))
    for x in dshots:
        if not x.get('fixed'): err.append(f"Phase D {x['id']} 缺 fixed（沒有固定欄位就不可重現）")
        bad=[i for i in x.get('applicable_rubric_items',[]) if i not in rub_items]
        if bad: err.append(f"Phase D {x['id']} 的 applicable_rubric_items 有不存在的項目：{bad}")
        dep=x.get('depends_on')
        if dep and not any(i in dep for i in ids):
            err.append(f"Phase D {x['id']} 的 depends_on 沒有指到任何存在的 shot id")
    covered=set()
    for x in dshots: covered |= set(x.get('applicable_rubric_items',[]))
    uncov=rub_items-covered
    if uncov: err.append(f"rubric 有項目沒有任何 stress shot 測到：{sorted(uncov)}")
    if not rub.get('hard_gates'): err.append("QA rubric 缺 hard_gates（總分會掩蓋關鍵失敗）")
    tm=rub.get('threshold_method',{})
    for k in ('ground_truth','persona_adaptation','scoring_aggregation','replicates'):
        if not tm.get(k): err.append(f"QA threshold_method 缺 {k}（C-08 要求的四項封口）")

    # --- K-01：語意覆核 gate（機器 lint 只是第一關）---
    import hashlib, os as _os
    h=hashlib.sha256(json.dumps(shots,ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:16]
    sr_p='pilot/semantic_review.json'
    if not _os.path.exists(sr_p):
        err.append("缺 pilot/semantic_review.json——機器 lint 通過不等於語意正確，"
                   "需先跑 tools/gen_semantic_checklist.py 並完成逐列覆核（K-01）")
    else:
        sr=json.load(open(sr_p,encoding='utf-8'))
        if sr.get('data_hash')!=h:
            err.append(f"語意覆核紀錄已過期（紀錄 hash {sr.get('data_hash')} ≠ 現行 {h}）——資料改過就要重審")
        else:
            done=set(sr.get('reviewed_shot_ids',[])); allids={x['shot_id'] for x in shots}
            missing=allids-done
            if missing:
                err.append(f"語意覆核未完成：{len(done)}/{len(allids)} 列，"
                           f"尚未覆核 {sorted(missing)[:5]}{'…' if len(missing)>5 else ''}"
                           "（C-19：這是生成前的 gate，未達 20/20 一律 HARD FAIL。"
                           "機器 lint 抓不到物理與語意矛盾——R5 就是在機器全過的狀態下被抓到 4 個。"
                           "見 pilot/semantic_review.md）")

    # --- C-21：Phase D 的每個變動都必須被認領 ---
    base={k:v for k,v in pd.get('fixed_baseline',{}).items() if not k.startswith('_')}
    if not base: err.append("Phase D 缺 fixed_baseline，無法稽核單一變量宣稱（C-21）")
    for x in dshots:
        fx={k:v for k,v in x.get('fixed',{}).items() if not k.startswith('_')}
        prim=x.get('primary_test_variable')
        rmc=x.get('required_measurement_changes',{})
        if 'primary_test_variable' not in x:
            err.append(f"Phase D {x['id']} 缺 primary_test_variable（C-21）"); continue
        if not isinstance(rmc,dict):
            err.append(f"Phase D {x['id']} 的 required_measurement_changes 必須是 欄位→理由 的物件"); continue
        if set(fx)!=set(base):
            err.append(f"Phase D {x['id']} 的 fixed 欄位集與 fixed_baseline 不一致"
                       f"（多 {sorted(set(fx)-set(base))}／少 {sorted(set(base)-set(fx))}）"
                       f"——漏列欄位就能規避稽核，故欄位全集必須相同（C-21 不變量 3）")
        diff={k for k in set(base)|set(fx) if base.get(k)!=fx.get(k)}
        claimed=set(rmc)|({prim['field']} if prim else set())
        unclaimed=diff-claimed
        if unclaimed:
            err.append(f"Phase D {x['id']} 有未申報的變動欄位 {sorted(unclaimed)}"
                       f"——宣稱單一變量但實際同時改了它們（C-21）")
        ghost=claimed-diff
        if ghost:
            err.append(f"Phase D {x['id']} 宣告要變動 {sorted(ghost)}，但 fixed 裡與基準相同"
                       f"——被測的東西沒有真的編碼進資料（C-21，st08b 就是這個病）")
        if prim and prim.get('field') in rmc:
            err.append(f"Phase D {x['id']} 的 primary 與 required_measurement 重複宣告 {prim['field']}")
        for k in rmc:
            if not str(rmc[k]).strip():
                err.append(f"Phase D {x['id']} 的 required_measurement_changes[{k}] 沒寫理由")
        hc=set(x.get('held_constant_fields',[]))
        if hc & claimed:
            err.append(f"Phase D {x['id']} 的 held_constant_fields 含有正在變動的欄位 {sorted(hc&claimed)}")
        if set(fx)-hc-claimed:
            err.append(f"Phase D {x['id']} 的 held_constant_fields 沒有涵蓋 {sorted(set(fx)-hc-claimed)}")
    trained_locs={s2['location'] for s2 in shots}
    burn=[x for x in dshots if 'no_scene_burn_in' in x.get('applicable_rubric_items',[])]
    if not burn:
        err.append("沒有任何 stress shot 測 no_scene_burn_in（C-25）")
    for x in burn:
        loc=x.get('fixed',{}).get('location')
        if loc in trained_locs:
            err.append(f"Phase D {x['id']} 測 no_scene_burn_in，但 location『{loc}』"
                       f"在訓練集出現過 {sum(1 for s2 in shots if s2['location']==loc)} 次"
                       f"——拿教過的場景測烙印，檢出力等於零（C-25）")
    prims=[x['primary_test_variable']['field'] for x in dshots if x.get('primary_test_variable')]
    if len(dshots)-len(prims)!=1:
        err.append("Phase D 必須且只能有一個 primary_test_variable=null 的基準線 shot（C-21）")

    # --- C-22：C 級場景不得被 cinematic treatment 抵銷 ---
    DRAMA=re.compile(r'掃過|掠過|打光|光束|穿透|灑落|逆光|流動|閃爍|拉出|渲染')
    tier_map=dict(zip([s2['shot_id'] for s2 in shots], tiers))
    ctier=[s2 for s2 in shots if tier_map.get(s2['shot_id'])=='C']
    filt=[s2 for s2 in ctier if s2['filter']!='none']
    for s2 in ctier:
        sec=s2['light'].get('secondary_source') or ''
        if s2['filter']!='none' and DRAMA.search(sec):
            err.append(f"{s2['shot_id']} 是 C 級場景，卻同時有懷舊/風格濾鏡（{s2['filter']}）"
                       f"與戲劇性動態光源（{sec[:20]}…）——C 級的用意是『完全不美』，"
                       f"這兩者疊加會把它變成電影感街拍（C-22）")
    if ctier and len(filt)/len(ctier) > 1/3:
        err.append(f"C 級場景 {len(filt)}/{len(ctier)} 帶濾鏡 > 1/3"
                   f"（{[s2['shot_id'] for s2 in filt]}）——C 級配額會被風格化抵銷（C-22）")

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
    sch=json.load(open('pilot/schema_v2.json',encoding='utf-8'))
    err,warn=validate(pilot,reg,sch)
    print(f"驗證 {pilot['persona_id']}（schema v{pilot['schema_version']}）")
    for w in warn: print("  ⚠ ",w)
    if err:
        for e in err: print("  ✗ ",e)
        sys.exit(1)
    print("  ✓ 全數通過")
