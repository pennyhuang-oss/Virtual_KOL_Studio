# -*- coding: utf-8 -*-
"""把 v5 的 80 格組成英文 prompt。

跟 v4 的三個差別，都是 R1 複核抓出來的：
 1. 守則不再和場景打架。v4 的 WALL 句要求「每一面牆與螢幕只能有純表面與印刷文字」，
    卻同時讓 P1 的牆上掛著汽車海報、J2 的手機螢幕停著練習影片，直接矛盾。
    v5 改成：場景自己宣告 wall_ok / screen_ok 時，守則把那一項列為例外。
 2. 鏡面守則掃全部欄位，不是只掃 place+action。v4 只掃兩欄，
    結果 80 格裡有 15 格帶反射面卻沒插守則，其中 6 格是鏡子就在正前方的浴室自拍。
 3. 守則從約 60 字壓到約 37 字。但維持正面描述的寫法——
    VERDICT_rulefix_v1 實測「把否定句改成正面描述」2/2 通過，
    這是手上唯一的實測資料，不因為沒有實測的建議而改回否定式。
"""
import json, re, sys, collections
from specs_data import SPECS

HERE='.'
IDENT=json.load(open(f'{HERE}/identity.json'))
SKIN =json.load(open(f'{HERE}/skin.json'))
RAIL =SKIN['_rail']
PRIV={"臥室","浴室","廚房","客廳","玄關","衣櫃 / 更衣","陽台 / 頂樓","車內","車庫"}

def skin(pid,s):
    v=SKIN[pid]
    if isinstance(v,str): return v
    # 六位人設的後製本來就分兩側：她自己的空間用 home，其餘用 work
    return v["home"] if (s.get("flag") is None and s["fam"] in PRIV) else v["work"]

VIEW={
 "selfie":("Shot at arm's length on the front camera, her head and shoulders filling the frame.",1),
 "near":("Shot from about a metre and a half away at her own eye level on a short portrait lens, the background falling into soft blur behind her.",2),
 "knee":("Shot from about two metres away at her own eye level, framed from the knees up, the background softly out of focus.",2),
 "full":("Shot from about four metres away with her whole body in the frame from head to feet, so the place around her reads clearly.",2),
 "floor":("Shot from slightly above her at about two metres, looking down to where she is, so the floor and her legs read clearly in the lower half of the frame.",2),
 "low":("Shot from floor level looking slightly up at her, the line of her body running the height of the frame.",2),
}
# 鏡位對應的取景敘述，開頭那一句身分句要跟著換
FRAME={"selfie":"in a close head-and-shoulders frame","near":"from the waist up",
       "knee":"in a three-quarter shot from the knees up","full":"in a full-length shot",
       "floor":"seen from above where she is","low":"seen from low down"}

# 只認真正的反射面。v4 這條掃到 polished / reflect 這種泛用詞，
# 而 skin 句裡本來就有「reflections are kept」「anything glass stays sharp」「not polished」，
# 會讓稽核對著自己的影調句誤報。
REFLECTIVE=re.compile(r'\bmirrors?\b|\bglass\b|\bwindow pane\b|\bfogged\b|\breflection',re.I)
MIRROR_GUARD="Any mirror or glass in the scene shows no person and no face."
CLOSURE="She has exactly two arms and two hands, and every visible hand is her own."
SOLO="She is the only person in the frame."

def wall(s):
    ok=s.get("wall_ok"); sk=s.get("screen_ok")
    if ok or sk:
        what=[]
        if ok: what.append("the one thing the scene already names on the wall")
        if sk: what.append("what her own phone screen is showing")
        return ("Apart from "+" and ".join(what)+
                ", the walls and any screen behind her carry only plain finishes and printed lettering.")
    return "The walls and any screen behind her carry only plain finishes and printed lettering."

def people(s):
    p=s.get("ppl")
    if not p: return SOLO
    return (f"She is the only person near the camera. {p['en_dist'].capitalize()} behind her {p['en_level']} are "
            f"{p['en_act']}, {p['en_wear']}. They are {p['en_facing']}, small in the frame and softly out of focus.")

PPL_EN={
 "數人":"several other people","1-2人":"one or two other people",
 "遠":"well","中":"a little way",
 "背對鏡頭":"turned away from the camera","側對鏡頭":"turned side-on to the camera",
 "背對或側對鏡頭":"turned away from or side-on to the camera",
}
PPL_ACT={
 "A5":"picking things over at the stalls and talking to the stallholders",
 "G1":"lifting something off the teak shelving to look at it",
 "C1":"wheeling luggage towards the gates and waiting in the seating",
 "M1":"waiting on the other side of the counter for their own cup",
 "P2":"standing around the other cars talking and crouching to look at the wheels",
 "S1":"choosing seafood at the stalls and haggling with the stallholders",
 "S2":"eating at the next table and ordering from the owner",
 "S5":"queueing at the stalls and standing up to eat what they have bought",
 "T1":"pushing shutters up, wheeling trolleys stacked with clothes and counting stock at the doors",
 "D4":"walking along in front of the shophouses, photographing the murals and stopping to buy things",
 "Y1":"swinging in their own bays and bending down to set a ball",
 "O4":"sheltering under the same eaves and talking to someone inside the shop",
}
PPL_WEAR={
 "A5":"in the light everyday clothes and slippers people wear to a morning market, carrying shopping bags",
 "G1":"dressed the way people dress to browse a South Jakarta select shop",
 "C1":"in travellers' clothes, jackets and hoodies, wheeling cases",
 "M1":"in ordinary Nakameguro weekday clothes, a coat or a knit",
 "P2":"in the T-shirts, shorts and trainers people wear to a car meet, some in caps",
 "S1":"in the waterproof aprons of the trade or carrying shopping bags, the way a Busan market looks by day",
 "S2":"in the jackets and tracksuits of people out for a late supper",
 "S5":"locals out for the morning market in short sleeves and aprons, carrying bags",
 "T1":"in the T-shirts, shorts, bum bags and slippers of people buying wholesale",
 "D4":"tourists and locals in short sleeves and straw hats, some with cameras",
 "Y1":"in range clothes, gloves and caps",
 "O4":"small-town residents in everyday clothes, rain boots and thin jackets",
}

def scene_blob(s):
    """鏡面守則與稽核都只看場景欄位。不能看組好的 prompt——
    那裡面有 skin 句，而 skin 句本來就會出現 glass / reflections 這些字。"""
    return " ".join(str(s.get(k) or '') for k in
                    ('pl_en','ac_en','li_en','fa_en','of_en','hair_en','pl','ac','li','fa','of'))

def build(pid,s):
    I=IDENT[pid]; L=[]
    L.append(f"A photograph of a beautiful adult {I['ethnic']} woman in her twenties, {FRAME[s['view']]}.")
    L.append(f"Her hair is {I['hair_colour']}, {s['hair_en']}.")
    L.append(I['body'])
    L.append(f"She wears {s['of_en']}.")
    L.append(f"She is {s['pl_en']}.")
    L.append(s['ac_en'])
    L.append(s['fa_en'])
    L.append(s['li_en'])
    L.append(RAIL)
    L.append(skin(pid,s))
    L.append(VIEW[s['view']][0])
    # 浴室就算句子裡沒出現「鏡」字，洗手台前本來就會生出一面鏡子，一律插守則
    if s['fam']=='浴室' or REFLECTIVE.search(scene_blob(s)): L.append(MIRROR_GUARD)
    L.append(wall(s))
    L.append(people(s))
    L.append(CLOSURE)
    return "\n".join(L)

def audit(rows):
    e=[]
    for r in rows:
        t=r['id']; p=r['prompt']
        if (r['_fam']=='浴室' or REFLECTIVE.search(r['_blob'])) and MIRROR_GUARD not in p:
            e.append(f"{t}: 場景有反射面卻沒插鏡面守則")
        if re.search(r'mirror selfie|photograph of her reflection|shooting her reflection',p,re.I):
            e.append(f"{t}: 出現對鏡自拍語彙（已停用）")
        if re.search(r'\bmirror\b',r['pl_en']+r['ac_en'],re.I) and re.search(r'\bphone\b',r['pl_en']+r['ac_en'],re.I):
            e.append(f"{t}: place/action 同時有鏡子與手機——實質上是對鏡自拍")
        # 守則不得和場景宣告的東西打架
        if re.search(r'\bposter\b|\bpainting\b|framed',r['pl_en']+r['ac_en'],re.I) and not r['_wall_ok']:
            e.append(f"{t}: 場景有海報／畫作卻沒宣告 wall_ok，守則會跟它打架")
        if re.search(r'phone screen|screen (shows|is lit|paused)|on the screen',r['pl_en']+r['ac_en'],re.I) and not r['_screen_ok']:
            e.append(f"{t}: 場景有螢幕內容卻沒宣告 screen_ok，守則會跟它打架")
        # 手部預算
        need={"空手":0,"單手持物":1,"單手扶物":1,"整理頭髮":2,"整理衣物":2,
              "雙手持物":2,"操作器具":2}[r['_hand']]
        if need>VIEW[r['_view']][1]:
            e.append(f"{t}: 鏡位 {r['_view']} 只有 {VIEW[r['_view']][1]} 隻手可用，動作卻要 {need} 隻")
        if not r['li_en'].strip().endswith('.'): e.append(f"{t}: light 句沒有句號")
        if r['_view']=="floor" and not re.search(
           r'on the (wooden |exercise )?(floor|mat)\b|on the bed\b|cross-legged|'
           r'crouch|kneel|sitting on the ground|lying',r['pl_en']+' '+r['ac_en'],re.I):
            e.append(f"{t}: floor 鏡位但場景不是在地面／床上")
    for k in ('of_en','ac_en','pl_en'):
        c=collections.Counter(r[k] for r in rows)
        for v,n in c.items():
            if n>1: e.append(f"跨全批重複 {k}：{v[:40]}… × {n}")
    return e

rows=[]
for pid,d in SPECS.items():
    for s in d['slots']:
        p=dict(s)
        if s.get('ppl'):
            q=s['ppl']
            p_ppl=dict(q, en_level=PPL_EN[q['level']], en_dist=PPL_EN[q['dist']],
                       en_facing=PPL_EN[q['facing']], en_act=PPL_ACT[s['id']], en_wear=PPL_WEAR[s['id']])
            p['ppl']=p_ppl
        rows.append(dict(id=s['id'], pid=pid, soul=IDENT[pid]['soul'],
                         pl_en=s['pl_en'], ac_en=s['ac_en'], li_en=s['li_en'],
                         _view=s['view'], _hand=s['hand'],
                         _wall_ok=bool(s.get('wall_ok')), _screen_ok=bool(s.get('screen_ok')),
                         _blob=scene_blob(s), _fam=s['fam'],
                         of_en=s['of_en'], prompt=build(pid,p)))

w=[len(r['prompt'].split()) for r in rows]
print(f"產出 {len(rows)} 格 | 字數 min={min(w)} max={max(w)} avg={sum(w)//len(w)}")
print("鏡位：", dict(collections.Counter(r['_view'] for r in rows)))
print("鏡面守則：", sum(1 for r in rows if MIRROR_GUARD in r['prompt']), "格")
print("有路人：", sum(1 for r in rows if SOLO not in r['prompt']), "格")
errs=audit(rows)
json.dump(rows, open(f'{HERE}/prompts_v5.json','w'), ensure_ascii=False, indent=1)
if errs:
    print(f"\n❌ audit {len(errs)} 項："); [print("  ",x) for x in errs]; sys.exit(1)
print("\n✅ audit 全數通過")
