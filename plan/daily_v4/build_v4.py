# -*- coding: utf-8 -*-
"""v4 產生器：把 16 份量身定做的 spec 組成英文 prompt。

與 v2／v3 最大的差別：**沒有全域的膚質／影調句**。
每位人設的 skin 句都翻自她自己 character.md 的「後製」欄（見 skin.json），
所以 zoey 是「不修膚質、允許過曝」，tammy 是「明亮飽和、允許雜物入鏡」，
wendy 是「低光高對比、臉可以半明半暗」—— 這三種在 v3 下是同一句。
"""
import json, glob, re, sys
from collections import Counter

HERE=__file__.rsplit('/',1)[0]
IDENT=json.load(open(f'{HERE}/identity.json'))
SKIN =json.load(open(f'{HERE}/skin.json'))

VIEW={
 "selfie":{"framing":"chest-up","hands":1,
  "text":"A close-up front-facing selfie shot, the angle slightly above her looking down at her, framed the way her own phone front camera would frame it. Her other arm runs out of the bottom corner of the frame toward the camera, so only one of her hands is doing anything else."},
 "near":{"framing":"from the waist up","hands":2,
  "text":"Shot from about a metre and a half away at her own eye level, a short portrait lens, the background falling into soft blur behind her."},
 "knee":{"framing":"a three-quarter shot from the knees up","hands":2,
  "text":"Shot from about two metres away at her own eye level, knees up inside the frame, the background softly out of focus."},
 "full":{"framing":"full length","hands":2,
  "text":"A full-length shot from about three metres away at her own eye level, head to feet inside the frame, the background softly out of focus."},
 "floor":{"framing":"a three-quarter shot from the knees up","hands":2,
  "text":"Shot from about two metres away at a slightly higher angle looking down at her where she sits on the floor, so the floor and her legs read clearly in the lower half of the frame."},
 "low":{"framing":"full length","hands":2,
  "text":"A full-length shot taken from low down, the camera at about her knee height looking up past her, so her legs run long into the frame."},
}
WALL=("Every wall, panel and screen behind her carries only plain surfaces and printed text — "
      "notices, labels and signage lettering — and no framed pictures, posters or displays of "
      "any kind hang on them.")
CLOSURE=("Everything in this picture is accounted for: the only person in it is her, and every "
         "visible hand connects to one of her own arms.")
SOLO="She is the only person in the photograph; no other people are visible anywhere in the frame."
# 場景裡有鏡子／玻璃／反光面時自動補這一句。
# v2 曾經有這條（MIRROR_SECONDARY），在 v1→v2 改寫時被我弄掉了，jia-seo D5 因此出事。
MIRROR_GUARD=("This is a direct front-camera photograph of her, not a picture of her reflection: "
  "any mirror or glass in the room sits beside or behind her and shows no face at all.")
REFLECTIVE=re.compile(r'\bmirror|\bglass\b|\breflect|\bwindow pane|\bpolished\b',re.I)

LIMB_TWO=re.compile(r'\bboth hands\b|\bboth arms\b|\bboth elbows\b|\bhands clasped\b|\bboth palms\b|'
                    r'\bstraight arms\b|\barms wrapped\b|\bboth thumbs\b|\bboth forearms\b',re.I)
LIMB_ONE=re.compile(r'\bone hand\b|\bher other hand\b|\bthe other hand\b|\bfree hand\b|\bone arm\b|'
                    r'\bone forearm\b|\bfingertips\b|\bone palm\b|\bthumb hooked\b|'
                    r'\bholding\b|\bcarrying\b|\breaching\b',re.I)
def limb_cost(t):
    return 2 if LIMB_TWO.search(t) else (1 if LIMB_ONE.search(t) else 0)

def build(pid, s):
    I=IDENT[pid]; v=VIEW[s["view"]]
    L=[]
    L.append(f"A photograph of a beautiful adult {I['ethnic']} woman in her twenties, {v['framing']}.")
    L.append(f"Her hair is {I['hair_colour']}, {s['hair']}.")
    L.append(I["body"])
    L.append("She wears "+s["outfit"]+".")
    L.append("She is "+s["place"]+".")
    L.append(s["action"])
    L.append(s["face"])
    L.append(s["light"])
    L.append(SKIN[pid])
    L.append(v["text"])
    if REFLECTIVE.search(s["place"]+" "+s["action"]):
        L.append(MIRROR_GUARD)
    L.append(WALL)
    L.append(s["people"] if s.get("people") else SOLO)
    L.append(CLOSURE)
    return "\n".join(L)

def audit(rows):
    e=[]
    for r in rows:
        t=f"{r['pid']} {r['id']}"
        v=VIEW[r["view"]]
        c=limb_cost(r["action"])
        if c>v["hands"]: e.append(f"{t}: 肢體超支 {c}>{v['hands']}（{r['view']}）")
        # 對鏡自拍已停用（手機物理錯）：只擋真正「拍自己的倒影」的寫法，
        # 場景裡單純有一面鏡子不算 —— 那種情況由 MIRROR_GUARD 處理
        blob=(r["action"]+" "+r["place"]).lower()
        for bad in ("mirror selfie","photographing her own reflection","her own reflection in the mirror",
                    "the frame is what that phone sees"):
            if bad in blob: e.append(f"{t}: 出現已停用的對鏡自拍寫法「{bad}」")
        # 鏡子 ＋ 手機同時出現 = 實質上的對鏡自拍，即使沒有寫「mirror selfie」這個詞
        if re.search(r'\bmirror\b',blob) and re.search(r'\bphone\b',blob):
            e.append(f"{t}: place/action 同時有鏡子與手機 — 實質上是已停用的對鏡自拍")
        if not r["light"].strip().endswith("."): e.append(f"{t}: light 句沒有句號")
        # floor 鏡位的敘述是「坐在地板上」，場景必須真的是坐在地面／床／台階上。
        # 注意要先排除 floor-to-ceiling window 與 floor lamp，否則會誤判過關
        if r["view"]=="floor":
            blob=re.sub(r'floor-to-ceiling|floor lamp','',r["place"]+" "+r["action"],flags=re.I)
            if not re.search(r'on the (wooden )?floor\b|on the mat\b|on the exercise mat|cross-legged|'
                             r'on the kerb|on the step|sitting on the ground|on (the|her) bed\b',blob,re.I):
                e.append(f"{t}: floor 鏡位但場景不是坐在地面／床／台階上")
        for k in ("place","action","outfit","light","face","hair","view"):
            if not r.get(k): e.append(f"{t}: 缺 {k}")
    # 跨全批不得撞服裝／動作
    for f in ("outfit","action"):
        c=Counter(r[f] for r in rows)
        for k,n in c.items():
            if n>1: e.append(f"{f} 重複 {n} 次：{k[:50]}")
    return e

if __name__=="__main__":
    rows=[]
    for f in sorted(glob.glob(f'{HERE}/en/*.json')):
        d=json.load(open(f))
        for s in d["slots"]:
            s["pid"]=d["pid"]; rows.append(s)
    errs=audit(rows)
    for r in rows: r["prompt"]=build(r["pid"], r)
    rows.sort(key=lambda r:(r["pid"],r["id"]))
    json.dump(rows,open(f'{HERE}/prompts_v4.json','w'),ensure_ascii=False,indent=1)
    w=[len(r["prompt"].split()) for r in rows]
    print(f"產出 {len(rows)} 格 | 字數 min={min(w)} max={max(w)} avg={sum(w)//len(w)}")
    print("鏡位：",dict(Counter(r['view'] for r in rows)))
    print("人設：",len({r['pid'] for r in rows}),"位")
    if errs:
        print(f"\n❌ audit {len(errs)} 項："); [print("  ",x) for x in errs]; sys.exit(1)
    print("\n✅ audit 全數通過")
