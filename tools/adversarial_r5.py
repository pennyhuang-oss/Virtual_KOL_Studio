#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R5 對抗測試：把 ChatGPT 這輪指出的每個缺陷重新注入，確認 validator 真的會擋。

規則是不是真的在執行，唯一的證明是「把病打回去，validator 會不會叫」。
C-15 就是這樣被抓到 schema 只是裝飾品的。
"""
import json, copy, sys
sys.path.insert(0,'tools')
from validate_shoot_plan_v2 import validate

BASE=json.load(open('pilot/nico_pilot.json',encoding='utf-8'))
REG=json.load(open('pilot/location_registry.json',encoding='utf-8'))
SCH=json.load(open('pilot/schema_v2.json',encoding='utf-8'))
SR='pilot/semantic_review.json'

def sd(p, complete=True):
    """把語意覆核標成完成，好讓其他規則的訊號不被 C-19 蓋掉。"""
    import hashlib, json as j
    h=hashlib.sha256(j.dumps(p['phase_c_shots'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:16]
    ids=[x['shot_id'] for x in p['phase_c_shots']] if complete else []
    j.dump({'data_hash':h,'reviewed_shot_ids':ids}, open(SR,'w',encoding='utf-8'), ensure_ascii=False)

def run(p):
    return validate(copy.deepcopy(p), REG, SCH)[0]

def shot(p,sid):
    return [s for s in p['phase_c_shots'] if s['shot_id']==sid][0]
def dshot(p,i):
    return [s for s in p['phase_d_stress_test']['shots'] if s['id']==i][0]

CASES=[]
def case(name, mutate, expect, complete_review=True):
    CASES.append((name,mutate,expect,complete_review))

# ---- C-19 ----
case("C-19 語意覆核 0/20 必須 HARD FAIL", lambda p: None, "語意覆核未完成", complete_review=False)

# ---- C-21 ----
def m_unclaimed(p):
    dshot(p,'st02')['fixed']['framing']='full_body'   # 改了但沒申報
case("C-21 未申報的連動變動", m_unclaimed, "未申報的變動欄位")

def m_ghost(p):
    x=dshot(p,'st09a'); x['primary_test_variable']={'field':'outfit_id','value':'nico_outfit_01'}
case("C-21 宣稱測某欄位但資料裡沒變（st08b 病）", m_ghost, "沒有真的編碼進資料")

def m_two_base(p):
    dshot(p,'st01')['primary_test_variable']=None
case("C-21 出現第二條基準線", m_two_base, "只能有一個 primary_test_variable=null")

def m_no_reason(p):
    dshot(p,'st05')['required_measurement_changes']={'framing':'  '}
case("C-21 連動變動沒寫理由", m_no_reason, "沒寫理由")

def m_hc_lie(p):
    x=dshot(p,'st04'); x['held_constant_fields']=x['held_constant_fields']+['framing']
case("C-21 held_constant 謊報（把變動欄位說成固定）", m_hc_lie, "含有正在變動的欄位")

# ---- C-22 ----
def m_drama(p):
    s=shot(p,'nico_c11')   # pharmacy, C 級, ccd
    s['light']['secondary_source']='冷氣出風口的光束從她右側掃過臉頰'
case("C-22 C 級同時有濾鏡＋戲劇性動態光", m_drama, "戲劇性動態光源")

def m_filt(p):
    for sid in ('nico_c09','nico_c10','nico_c12'):
        shot(p,sid)['filter']='ccd'
case("C-22 C 級帶濾鏡超過 1/3", m_filt, "帶濾鏡 > 1/3")

# ---- 回歸：先前四個 schema 對抗案例 ----
def m_enum(p): shot(p,'nico_c05')['framing']='SUPER_ZOOM'
case("回歸 C-15 非法 enum", m_enum, "不是合法值")
def m_req(p): del shot(p,'nico_c05')['eye_gaze']
case("回歸 C-15 缺必填欄位", m_req, "缺必填欄位")
def m_typo(p): shot(p,'nico_c05')['framming']='chest_up'
case("回歸 C-15 未定義欄位（打字錯誤）", m_typo, "未定義欄位")
def m_pose(p): shot(p,'nico_c05')['scene']='蹲在地上找東西'
case("回歸 C-16 scene 與 body_pose 矛盾", m_pose, "body_pose")

# ---- C-21 不變量 3 / C-25（R6 新增）----
def m_dropfield(p):
    del dshot(p,'st04')['fixed']['body_pose']       # 靠漏列欄位規避稽核
case("C-21 不變量3：靠漏列 fixed 欄位規避稽核", m_dropfield, "欄位集與 fixed_baseline 不一致")

def m_burn_seen(p):
    x=dshot(p,'st06'); x['fixed']['location']='park'   # 訓練集出現 4 次
    x['primary_test_variable']={'field':'location','value':'park'}
case("C-25 拿訓練集教過的場景測 no_scene_burn_in", m_burn_seen, "拿教過的場景測烙印")

def m_no_burn(p):
    for x in p['phase_d_stress_test']['shots']:
        x['applicable_rubric_items']=[i for i in x['applicable_rubric_items'] if i!='no_scene_burn_in']
case("C-25 完全沒有 shot 測 no_scene_burn_in", m_no_burn, "沒有任何 stress shot 測 no_scene_burn_in")

# ---- C-23（R6 新增）：props 重複與手部佔用 ----





# ---- C-27 / C-29（R7 新增）：結構化 props 與 hands ----
def m_dupbag(p):
    s2=shot(p,'nico_c12'); s2['props'][1]={"id":"bag","name":"結構皮革包","relation":"surface",
        "zone":"waist","expected_visible":True}
case("C-23 props 重述 outfit 已提供的包", m_dupbag, "重述了 outfit 已提供的")

def m_crossbag(p):
    s2=shot(p,'nico_a06'); s2['props'][1]={"id":"tote","name":"米色帆布托特","relation":"surface",
        "zone":"floor","expected_visible":True}
case("C-23 props 借用別套 outfit 的招牌包", m_crossbag, "另一套 outfit 的招牌包")

def m_offframe(p):
    shot(p,'nico_a01')['props'][0].update(relation="surface",zone="waist")   # face_closeup 看不到腰線
case("C-29 宣告可見的 prop 落在 framing 裁切外", m_offframe, "宣告可見卻在裁切外")

def m_synonym(p):
    shot(p,'nico_a02')['hands']['right']['object_ref']='咖啡杯'   # 用同義詞而非 prop id
case("C-27 object_ref 用同義詞繞過 prop id", m_synonym, "不是本列的 prop id")

def m_thirdhand(p):
    s2=shot(p,'nico_c10')
    s2['props'].append({"id":"coins","name":"手上的零錢","relation":"held_right",
                        "zone":"waist","expected_visible":True})   # 雙手已抱衣物
case("C-27 第三隻手（held prop 沒有手引用）", m_thirdhand, "沒有任何一隻手引用它")

def m_selfie_nocam(p):
    shot(p,'nico_c08')['hands']['left']={"state":"supporting","object_ref":None,"note":"扶著洗手台"}
case("C-27 自拍卻沒有一隻手是 camera", m_selfie_nocam, "自拍必須且只能占掉一隻手")

def m_cam_notselfie(p):
    shot(p,'nico_a01')['hands']['left']={"state":"camera","object_ref":None,"note":"舉著手機"}
case("C-27 非自拍卻標了 camera hand", m_cam_notselfie, "不是自拍，手上卻標了 camera")

def m_phone_prop(p):
    shot(p,'nico_c04')['props'][0]['name']='床上另一支手機'
case("C-27 拍攝裝置同時被列為入鏡 prop", m_phone_prop, "不得同時列為入鏡 prop")

def m_relmismatch(p):
    shot(p,'nico_c12')['props'][0]['relation']='held_left'   # 右手在拿
case("C-27 hand 與 prop 的 relation 左右不符", m_relmismatch, "應為")

def m_twohands_one(p):
    s2=shot(p,'nico_c09')
    s2['hands']['left']={"state":"holding","object_ref":"onigiri","note":"也拿著飯糰"}
case("C-27 同一個 prop 被兩隻手引用但不是 held_both", m_twohands_one, "被兩隻手同時引用")

ok=0
for name,mut,expect,cr in CASES:
    p=copy.deepcopy(BASE); sd(p, cr); mut(p)
    errs=run(p)
    hit=any(expect in e for e in errs)
    print(("  ✓ 擋下" if hit else "  ✗ 漏掉")+f"  {name}")
    if not hit:
        print("      實際錯誤：", errs[:3] or "（無）")
    ok+=hit

# ---- 反向：乾淨資料 + 完成覆核 應該全過 ----
p=copy.deepcopy(BASE); sd(p, True)
errs=run(p)
clean_ok = not errs
print(("  ✓ 通過" if clean_ok else "  ✗ 誤報")+"  反向：乾淨資料＋覆核完成應無錯誤")
if not clean_ok: print("      ",errs)

sd(BASE, False)   # 還原：真實狀態仍是 0/20
print(f"\n對抗測試 {ok}/{len(CASES)} 擋下，反向測試 {'通過' if clean_ok else '失敗'}")
sys.exit(0 if ok==len(CASES) and clean_ok else 1)
