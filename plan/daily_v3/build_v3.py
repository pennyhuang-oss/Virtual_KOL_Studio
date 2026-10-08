# -*- coding: utf-8 -*-
"""v3 產生器 —— 補齊 39 格。

與 v2 的差別（全部來自使用者的判讀）：
  規則甲  people 由場景的 publicness 推導，不再逐格手掛
  規則乙  路人穿什麼、她穿什麼，都由場景決定（scene.crowd / scene.dress）
  規則丙  牆面用 rulefix_v1 已驗證的正面描述（否定句無效）
  打光    只用留存率高的一族（光在臉上、背景壓暗）；K9/K14/K7/K3/K1/K11 全禁
  鏡位    砍掉對鏡自拍（20%，且手機物理錯）與膝上（26%）
  姿勢    詞庫擴充，且整批不得重複；同一鏡位的姿勢池分開
"""
import json, glob, random, sys, re
from collections import Counter, defaultdict

random.seed(20260910)
HERE = __file__.rsplit('/',1)[0]
V  = json.load(open(f'{HERE}/vocab.json'))
S  = json.load(open(f'{HERE}/scenes.json'))
OF = json.load(open(f'{HERE}/outfits.json'))

# 每位人設還缺幾張（目標每人 5 張），來自使用者的選片
SHORT = {"wendy-yeo":5,"zhiyi-shen":5,"angel-chiu":3,"angeline-kwee":3,"somi-oh":3,
         "yerin-han":3,"zoey-yeh":3,"emma-kao":2,"peggy-lee":2,"sydney-leong":2,
         "tammy-chou":2,"wanyin-jiang":2,"cheryl-soh":1,"jia-seo":1,"miu-shiraishi":1,
         "ruoruo-tang":1}

# 人設城市 → 場景城市
CITY = {"angel-chiu":"Taipei","tammy-chou":"Taipei","angeline-kwee":"Jakarta",
        "cheryl-soh":"Singapore","wendy-yeo":"Singapore","emma-kao":"Tainan",
        "jia-seo":"Seoul","yerin-han":"Seoul","miu-shiraishi":"Tokyo",
        "peggy-lee":"Kuala Lumpur","ruoruo-tang":"Chengdu","somi-oh":"Busan",
        "sydney-leong":"George Town","wanyin-jiang":"Suzhou","zhiyi-shen":"Shanghai",
        "zoey-yeh":"Yilan"}

def personas():
    out={}
    for f in sorted(glob.glob(f'{HERE}/../daily_v2/matrix_part*.json')):
        for pid,v in json.load(open(f)).items():
            out[pid]={"ethnic":v["ethnic"],"hair_colour":v["hair_colour"],"body":v["body"]}
    return out
P = personas()

HAIR = ["loose and straight with a centre part","in a high ponytail","brushed out into soft waves",
        "in a low twist with strands loose at the nape","half-up with the rest falling loose",
        "pushed back off her face and tucked behind both ears","in two low braids",
        "blown out straight with the ends turned under","in a loose topknot with a few pieces down",
        "swept over one shoulder in glossy waves","pinned up with a claw clip",
        "in a sleek low bun"]

GLOW = ("Camera-ready natural makeup — an even lightweight base, softly groomed brows, curled "
        "separated lashes and a subtle lip colour. Her hair is styled and finished, not messy. Her "
        "skin is even and healthy-looking with subtle professional retouching, clear and consistent "
        "in tone, with a soft sheen where the light lands and a small natural catchlight in both eyes.")
WALL = ("Every wall, panel and screen behind her carries only plain surfaces and printed text — "
        "notices, price cards and signage lettering — and no framed pictures, posters or displays "
        "of any kind hang on them.")
CLOSURE = ("Everything in this picture is accounted for: the only person in it is her, and every "
           "visible hand connects to one of her own arms.")

# micro 的 cost = 需要佔用幾隻手（0 = 放在旁邊或掛在身上，1 = 手上／臂上）
MICRO = [("a canvas tote hooked over her forearm",1),("a small chain-strap bag at her hip",0),
         ("a paper cup on the ledge beside her",0),("a woven bag set down by her feet",0),
         ("a small crossbody pouch worn across her body",0),("sunglasses hooked into her neckline",0),
         ("a slim shoulder bag on one shoulder",0),("a folded paper carrier standing beside her",0),
         ("a beaded clutch tucked under one arm",1),("a set of keys looped over one finger",1),
         ("a small paper bag on the counter beside her",0),("a phone in her free hand",1),
         ("a takeaway cup set on the ledge",0),("a straw bag propped against her ankle",0)]

LIMB_TWO=re.compile(r'\bboth hands\b|\bboth elbows\b|\bboth arms\b|\bboth thumbs\b|\bstraight arms\b|\bboth palms\b|\bboth forearms\b|\barms wrapped\b|\bhands clasped\b',re.I)
LIMB_ONE=re.compile(r'\bfree hand\b|\bone hand\b|\bone arm\b|\bone forearm\b|\bone palm\b|\bone finger\b|'
                    r'\bher free \w+\b|\bfingertips\b|\btwo fingers\b|\bthumbs? hooked\b|\bone knee\b|'
                    r'\breaching one arm\b|\btrailing along\b|\bshading her eyes\b',re.I)

def pose_cost(t):
    return 2 if LIMB_TWO.search(t) else (1 if LIMB_ONE.search(t) else 0)

def assign():
    scenes = {s["id"]: s for s in S["scenes"]}
    by_city = defaultdict(list)
    for s in S["scenes"]: by_city[s["city"]].append(s["id"])
    for c in by_city: by_city[c].sort()

    used_scene=set(); used_pose=set(); used_outfit=set()
    expr_count=Counter(); view_count=Counter(); hair_count=Counter(); micro_count=Counter()
    # 鏡位目標配額：已驗證的優先，新鏡位各給 4 格
    quota = {"V_SELFIE":11,"V_FULL":16,"V_LOW":4,"V_BACK":4,"V_SIT":4}
    # 日／夜各半 —— 使用者要求。判準不是白天晚上，是「她比背景亮」，
    # 所以白天那一組每一句都明寫背景比她暗（見 vocab._light_principle）。
    total = sum(SHORT.values())
    time_quota = {"day": (total+1)//2, "night": total//2}
    time_count = Counter()
    rows=[]
    # 輪替配發：先每人一張，再第二張…… 避免需求大的人設把該城市的場景吃光，
    # 讓只缺 1 張的人設也拿得到（先前 persona-major 的順序會餓死他們）
    order = sorted(SHORT, key=lambda p:(-SHORT[p], p))
    jobs = [(pid,k) for k in range(max(SHORT.values())) for pid in order if SHORT[pid] > k]
    for pid,k in jobs:
        cands = [i for i in by_city[CITY[pid]] if i not in used_scene]
        random.shuffle(cands)
        # 日／夜配額要驅動「選哪個場景」，不能只在場景選定後才挑光 ——
        # 否則抽到只有夜景光的場景時配額根本補不回來
        want = max(time_quota, key=lambda t: time_quota[t]-time_count[t])
        cands.sort(key=lambda i: 0 if any(V["light"][L]["time"]==want for L in scenes[i]["light"]) else 1)
        if True:
            placed=False
            for sid in list(cands):
                sc = scenes[sid]
                # 配額是偏好不是硬限制：未達配額的先試，其餘接在後面，
                # 免得「配額還有但姿勢用完」的鏡位把整格卡死
                under = [v for v in sc["views"] if view_count[v] < quota[v]]
                over  = [v for v in sc["views"] if view_count[v] >= quota[v]]
                random.shuffle(under); random.shuffle(over)
                views = under + over
                for view in views:
                    poses = [p for p in V["pose"][view] if p not in used_pose]
                    if not poses: continue
                    regs = [r for r in sc["dress"] if r in OF]
                    pool = [o for r in regs for o in OF[r] if o["text"] not in used_outfit]
                    if not pool: continue
                    # 先挑還沒滿額的時段，滿了才放寬
                    lights = sc["light"][:]
                    random.shuffle(lights)
                    under_t = [L for L in lights if time_count[V["light"][L]["time"]] < time_quota[V["light"][L]["time"]]]
                    light = (under_t or lights)[0]
                    budget = V["view"][view]["hands_free"]
                    fit = [q for q in poses if pose_cost(q) <= budget]
                    if not fit: continue
                    pose = random.choice(fit)
                    left = budget - pose_cost(pose)
                    mics = [m for m in MICRO if m[1] <= left]
                    if not mics: continue
                    outfit = random.choice(pool)
                    expr = min(V["expression"], key=lambda e:(expr_count[e], random.random()))
                    hair = min(HAIR, key=lambda h:(hair_count[h], random.random()))
                    micro = min(mics, key=lambda m:(micro_count[m[0]], random.random()))[0]
                    ppl = S["people_rule"][sc["publicness"]]
                    rows.append({"pid":pid,"n":k+1,"scene":sid,"view":view,"light":light,
                                 "pose":pose,"expr":expr,"outfit":outfit["text"],
                                 "tier":outfit["tier"],"hair":hair,"micro":micro,"people":ppl,
                                 "register":[r for r in regs if any(o["text"]==outfit["text"] for o in OF[r])][0]})
                    used_scene.add(sid); used_pose.add(pose); used_outfit.add(outfit["text"])
                    expr_count[expr]+=1; view_count[view]+=1; hair_count[hair]+=1; micro_count[micro]+=1
                    time_count[V["light"][light]["time"]]+=1
                    cands.remove(sid); placed=True; break
                if placed: break
            if not placed:
                rows.append({"pid":pid,"n":k+1,"scene":None,"_error":"該城市沒有可用的新場景"})
    return rows, scenes

def build(r, sc):
    p=P[r["pid"]]; view=V["view"][r["view"]]
    L=[]
    L.append(f"A photograph of a beautiful adult {p['ethnic']} woman in her twenties, "
             f"{ {'chest_up':'chest-up','full_length':'full length','three_quarter':'a three-quarter shot from the knees up'}[view['framing']] }.")
    L.append(f"Her hair is {p['hair_colour']}, {r['hair']}.")
    L.append(p["body"])
    L.append("She wears "+r["outfit"]+".")
    L.append(f"She is in {sc['name']}, with {sc['detail']}.")
    L.append(r["pose"]); L.append(r["expr"])
    L.append(V["light"][r["light"]]["text"])
    L.append(GLOW)
    L.append(view["text"])
    L.append(WALL)
    L.append("Visible with her: "+r["micro"]+".")
    t=S["people_text"][r["people"]]
    L.append(t.replace("{crowd}", sc.get("crowd","")) if "{crowd}" in t else t)
    L.append(CLOSURE)
    return "\n".join(L)

# ── audit ────────────────────────────────────────────────────────────────
BANNED_LIGHT={"K9","K14","K7","K3","K1","K11"}
MICRO_COST={t:c for t,c in MICRO}

def audit(rows, scenes):
    errs=[]
    for r in rows:
        if r.get("_error"): errs.append(f"{r['pid']} #{r['n']}: {r['_error']}"); continue
        sc=scenes[r["scene"]]; tag=f"{r['pid']} #{r['n']} [{r['scene']}]"
        # 規則甲
        if S["people_rule"][sc["publicness"]] != r["people"]:
            errs.append(f"{tag}: people 未由 publicness 推導")
        if sc["publicness"]=="quiet" and r["people"]!="solo":
            errs.append(f"{tag}: 僻靜場景卻掛了路人")
        # 規則乙
        if r["register"] not in sc["dress"]:
            errs.append(f"{tag}: 服裝 register「{r['register']}」不在該場景允許範圍 {sc['dress']}")
        if sc["publicness"]!="quiet" and not sc.get("crowd"):
            errs.append(f"{tag}: 有路人的場景沒有寫路人穿什麼")
        # 打光
        if r["light"] not in sc["light"]:
            errs.append(f"{tag}: 打光 {r['light']} 不在該場景允許範圍")
        if V["light"][r["light"]].get("open_sky_only") and "indoor" in sc["name"]:
            errs.append(f"{tag}: {r['light']} 只能用在開放天空的場景")
        # 鏡位
        if r["view"] not in sc["views"]:
            errs.append(f"{tag}: 鏡位 {r['view']} 不在該場景允許範圍")
        if r["view"] in ("mirror_half","friend_near"):
            errs.append(f"{tag}: 使用了已停用的鏡位")
        # 肢體預算
        budget = V["view"][r["view"]]["hands_free"]
        cost = pose_cost(r["pose"]) + MICRO_COST.get(r["micro"], 1)
        if cost > budget:
            errs.append(f"{tag}: 肢體超支 {cost}>{budget}（pose＋micro）")
    # 全批不重複
    for field,label in (("scene","場景"),("pose","姿勢"),("outfit","服裝")):
        c=Counter(r[field] for r in rows if r.get(field))
        for k,v in c.items():
            if v>1: errs.append(f"{label}重複 {v} 次：{str(k)[:60]}")
    return errs

if __name__=="__main__":
    rows, scenes = assign()
    errs = audit(rows, scenes)
    out=[]
    for r in rows:
        if r.get("_error"): continue
        r["prompt"]=build(r, scenes[r["scene"]])
        out.append(r)
    json.dump(out, open(f'{HERE}/plan_v3.json','w'), ensure_ascii=False, indent=1)
    lens=[len(x["prompt"].split()) for x in out]
    print(f"產出 {len(out)} 格 | 字數 min={min(lens)} max={max(lens)} avg={sum(lens)//len(lens)}")
    print("鏡位：",dict(Counter(x['view'] for x in out)))
    print("打光：",dict(Counter(x['light'] for x in out)))
    print("日／夜：",dict(Counter(V["light"][x['light']]["time"] for x in out)))
    print("路人：",dict(Counter(x['people'] for x in out)))
    print("露出：",dict(Counter(x['tier'] for x in out)))
    print("表情最多重複：",Counter(x['expr'] for x in out).most_common(1)[0][1],"次")
    if errs:
        print(f"\n❌ audit {len(errs)} 項不通過：")
        for e in errs: print("  ",e)
        sys.exit(1)
    print("\n✅ audit 全數通過")
