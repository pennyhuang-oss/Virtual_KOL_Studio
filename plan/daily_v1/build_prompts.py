#!/usr/bin/env python3
"""日常素材 v1：從 matrix.json 決定性地產生 100 段 prompt。

規則全部在這裡強制執行，不依賴撰寫者記得：
  §3-0  光線只寫一句（一個光源＋一個自然後果）。五段式已於 2026-09-03 實測否決。
  §3-D① 有反射面的場景，必須寫明拍攝者位置，且第二人物排除句要寫完整。
  §3-D② 不加 film grain / 35mm / warm tones 尾巴（實測會更像精修大片）。
  §3-E  全身照必須寫「相機在她前方」與「背不對鏡頭」。
  §3-F  不掛裸否定句；戶外人多的場景不清場，改正面描述失焦路人。
  C-1   每張都必須寫她自己的髮色髮型。
  決策B  身材用描述性句子補，不寫三圍數字。
  不重述五官 —— 臉由 Soul 提供，prompt 寫了反而是 prompt 在補臉。
"""
import json, glob, re

# 會照出人像的反射面（水面／濕柏油反射天空不算，那不會照出第二張臉）
REFLECTIVE = re.compile(r"\bmirror\b|\bmirrored\b|her reflection|reflective surface", re.I)
def has_reflective(slot):
    return bool(REFLECTIVE.search(slot["scene"]) or REFLECTIVE.search(slot["action"]))

LIGHT = {
 "L1":"Plain overhead fluorescent light, flat and a little green, the corners of the room dimmer.",
 "L2":"Soft daylight from a window off to one side, the far side of the room noticeably darker.",
 "L3":"One warm lamp doing all the work, most of the room falling away into shadow.",
 "L4":"Flat grey overcast daylight, even and almost shadowless.",
 "L5":"Warm light spilling out of the shopfronts, the street behind her going dark.",
 "L6":"A single strip light overhead, hard on the top of her head and dim below it.",
 "L7":"Late afternoon sun coming in low from one side, long shadows across the floor.",
 "L8":"Open shade under the roof, the bright street beyond blown out behind her.",
 "L9":"Cool light from a lit panel beside her, the rest of the frame much darker.",
 "L10":"Warm ceiling light close overhead, steam catching it.",
 "L11":"Low golden light near sunset, warm on her with the sky behind brighter than she is.",
 "L12":"Neon signage doing all the lighting, colour falling unevenly across her.",
 "L13":"Bright even morning light, the sky behind brighter than her face.",
 "L14":"Flat white light from directly above, even and unflattering.",
}

FRAMING = {
 "chest_up":"chest-up",
 "waist_up":"from the waist up",
 "full_length":"full length, head to feet inside the frame",
 "mid_environment":"a wide shot with her small in the frame and the room around her",
}

DEVICE = {
 "front_selfie":"Shot on a phone front camera held at arm's length, slight wide-lens distortion, natural color, no beauty filter, no skin smoothing.",
 "found_mirror":"Shot on a phone rear camera held about a metre from the reflective surface, the phone visible in her own hand, natural color, no beauty filter, no skin smoothing.",
 "friend_rear":"Shot on a phone rear camera by someone standing about two metres away, natural color, no beauty retouching.",
 "propped_timer":"Shot on a phone rear camera propped on a surface nearby with the self-timer running, natural color, no beauty retouching.",
}

PEOPLE = {
 "solo_interior":"She is the only person in the photograph; no other people are visible anywhere in the frame.",
 "outdoor_background_ok":"A few anonymous strangers are in the mid-ground behind her going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing, none of their faces readable.",
}

FULL_LENGTH = "The camera is in front of her, not behind her.\nHer back is not to the camera."
# §3-D① 鏡面場景專用：原句是為了擋「第二個人拿手機」的矛盾自拍，鏡面場景要保留她自己的倒影，故改寫
MIRROR = ("The only reflection is her own; there is no second person and no second phone anywhere in the "
          "reflection, and no portrait or photograph of a person on any wall or screen.")

# 次要鏡面：畫面裡有鏡子但相機不是它。仍必須擋掉第二個人與第二支手機
MIRROR_SECONDARY = ("The only reflection in that mirror is her own; there is no second person and no second "
                    "phone in it, and no portrait or photograph of a person on any wall or screen.")

# 皮膚質地：真實感 ≠ 畫質差（2026-07-25 修正）。寫紋理，不寫 grainy／degraded。
SKIN = ("Her skin has real texture — visible pores, slight unevenness across the cheeks and a little "
        "shine where the light lands, printed as it is with no retouching and no smoothing.")

# 器材的自然痕跡：補回長度，同時強化「這是誰在什麼位置拍的」（§3-D① 縮短時就是丟了這一段）
DEVICE_TELL = {
 "front_selfie":"Her forearm runs out of the bottom corner of the frame toward the phone, and the angle is a little too close and tipped slightly down at her, the way a real front-camera shot is.",
 "found_mirror":"The reflective surface is not clean — it carries smears, dust and small scratches, and the image in it is slightly dimmer and less sharp than the room itself.",
 "friend_rear":"The framing is a fraction loose and slightly off-centre, taken quickly by someone who was already walking with her.",
 "propped_timer":"The horizon sits a little crooked and she is placed off-centre, the way a phone balanced on whatever was to hand ends up framing a room.",
}

MOMENT = "It reads as an ordinary moment that happened to be caught rather than a picture she sat down to make."

# §3-D①：縮短版失敗的主因是丟了「拍攝者在哪、距離多遠」這一句。逐張寫明，不可省。
CAMERA_POS = {
 "front_selfie":"The phone is in her own hand about half an arm's length from her face, held just above her eye line so the lens looks slightly down at her.",
 "found_mirror":"She is standing about a metre from the reflective surface with the phone at chest height, and the camera is the phone in her own hand — there is no separate photographer anywhere in the scene.",
 "friend_rear":"The person holding the phone is standing roughly two metres away at her own eye level, close enough to be someone she is with rather than someone watching her.",
 "propped_timer":"The phone is resting on a surface roughly three metres from her between chest and eye height, level with her or tipped a fraction downward, and nobody is holding it.",
}

def build(p, slot, light_code):
    L=[]
    L.append(f"A photograph of an adult {p['ethnic']} woman in her twenties, {FRAMING[slot['framing']]}.")
    # C-1（強制）：每張都要寫她自己的髮色。髮色與該格造型分開組句，避免只寫髮型漏掉髮色。
    L.append(f"Her hair is {p['hair_colour']}, {slot['hair_style']}.")
    L.append(p["body"])
    L.append("She wears "+slot["outfit"]+".")
    # §12 同穿搭一日敘事：完整重述服裝 + 至少一個狀態演進，不靠人工複製文字
    if slot.get("continuity_from"):
        L.append("This is the exact same outfit as earlier that same day, the same garments in the same "
                 "colours, worn a few hours on: "+slot.get("continuity_evolution","")+".")
    L.append("She is in "+slot["scene"]+".")
    L.append(LIGHT[light_code])
    if slot["framing"]=="full_length": L.append(FULL_LENGTH)
    if slot["device"]=="found_mirror":
        L.append(MIRROR)
    elif has_reflective(slot):
        L.append(MIRROR_SECONDARY)
    L.append(CAMERA_POS[slot["device"]])
    L.append(slot["action"])
    L.append("Visible with her: "+slot["micro"]+".")
    L.append(SKIN)
    L.append(DEVICE_TELL[slot["device"]])
    L.append(MOMENT)
    L.append(PEOPLE[slot["people"]])
    L.append(DEVICE[slot["device"]])
    return "\n".join(L)

IN_FRAME_CAMERA = re.compile(r"\bphone\b|\btripod\b|\bcamera\b", re.I)

def audit(pid,n,slot,txt,p):
    """規則檢查——違反就中止，不靠人記得。
    2026-09-09 依 GPT daily_v1 R1 第 5 題改寫：原本用 txt.count(".")<12 數句點，
    那只證明句子夠多，不證明語意區塊完整。改成逐條件檢查必備區塊。"""
    e=[]
    # C-1：檢查資料本身帶不帶顏色詞（檢查成品是套套邏輯——模板本來就會把它寫進去）
    COLOUR_WORDS=("black","brown","blonde","grey","gray","silver","red","pink","lilac","gold",
                  "ash","chestnut","greige","honey","mint","blue","green","wine","platinum")
    if not any(c in p['hair_colour'].lower() for c in COLOUR_WORDS):
        e.append(f"C-1 hair_colour 不含任何顏色詞: {p['hair_colour']!r}")
    if not slot.get("hair_style"): e.append("hair_style 空白")

    # 共同必備區塊：缺一段就是模板被改壞了
    for frag,label in [
        ("in her twenties","成人年齡句缺失"),
        ("Her hair is","C-1 髮色句缺失"),
        ("She wears","服裝句缺失"),
        ("She is in","場景句缺失"),
        ("real texture","§皮膚質地句缺失"),
        ("ordinary moment","MOMENT 句缺失"),
        ("no beauty","器材句缺失"),
    ]:
        if frag not in txt: e.append(label)

    # 條件區塊
    if slot["framing"]=="full_length" and "not behind her" not in txt:
        e.append("§3-E 全身框架句缺失")
    if slot["device"]=="found_mirror" and "no second phone" not in txt:
        e.append("§3-D① 鏡面排除句缺失")
    # 必修 4：任何實際反射面都要受稽核，不只 device==found_mirror
    if slot["device"]!="found_mirror" and has_reflective(slot) and "no second phone in it" not in txt:
        e.append("反射面出現在場景/動作裡卻沒有反射完整性句")
    if slot["people"]=="outdoor_background_ok":
        for frag in ("never looking at the camera","slight motion blur","build, age and clothing"):
            if frag not in txt: e.append(f"§9 背景路人四條件不完整，缺: {frag}")
    # 必修：架拍時相機不能出現在自己的非鏡面成像裡
    if slot["device"]=="propped_timer" and not has_reflective(slot):
        for fld in ("scene","micro"):
            if IN_FRAME_CAMERA.search(slot[fld]):
                e.append(f"架拍場景的 {fld} 寫了畫面內的手機/腳架/相機——相機不能拍到自己")
    # §12 同穿搭敘事的資料完整性
    if slot.get("continuity_from"):
        if not slot.get("continuity_evolution"): e.append("continuity_from 有值但缺 continuity_evolution")
        if "exact same outfit" not in txt: e.append("§12 同穿搭句缺失")

    if "grain" in txt or "35mm" in txt or "Instagram" in txt: e.append("§3-D② 出現已刪除的尾巴")
    for m in ["no phone","no screen","no television","no mirror"]:
        if m in txt.lower(): e.append(f"§3-F 裸否定句風險: {m}")
    if e: raise SystemExit(f"[FAIL] {pid} D{n}: "+"; ".join(e))

def main():
    m={}
    for f in sorted(glob.glob('matrix_part*.json')): m.update(json.load(open(f)))
    lights=json.load(open('lights.json'))
    want={f'{pid}:{n}' for pid,p in m.items() for n in range(1,len(p['slots'])+1)}
    if set(lights)!=want:
        raise SystemExit(f'[FAIL] lights.json 與 slot 未一一對應: 多={sorted(set(lights)-want)} 少={sorted(want-set(lights))}')
    out=[]; rows=[]
    for pid in sorted(m):
        p=m[pid]
        for n,slot in enumerate(p["slots"],1):
            code=lights[f"{pid}:{n}"]
            if slot.get('continuity_from'):
                src=p['slots'][slot['continuity_from']-1]
                if src['outfit']!=slot['outfit']:
                    raise SystemExit(f'[FAIL] {pid} D{n}: continuity_from=D{slot["continuity_from"]} 但服裝字串不同')
            txt=build(p,slot,code)
            audit(pid,n,slot,txt,p)
            wc=len(txt.split())
            out.append((pid,n,slot,code,txt,wc))
            rows.append({"persona":pid,"n":n,"tier":slot["tier"],"device":slot["device"],
                         "framing":slot["framing"],"zone":slot["zone"],"light":code,"words":wc})
    json.dump(rows,open('index.json','w'),indent=1,ensure_ascii=False)
    with open('PROMPTS.md','w') as f:
        f.write("# 日常素材 v1 — 100 段 prompt（產生檔，勿手改）\n\n")
        f.write("> 由 `build_prompts.py` 從 `matrix_part*.json` + `lights.json` 決定性產生。\n"
                "> 要改內容請改資料檔後重跑，不要直接編輯本檔。\n"
                "> 送生成時：`model='soul_2'` + 該位 `soul_id`，**不掛 Reference Element**，`aspect_ratio='3:4'`。\n\n")
        cur=None
        for pid,n,slot,code,txt,wc in out:
            if pid!=cur:
                cur=pid
                f.write(f"\n---\n\n## {pid}\n\n`soul_id` 見 `review/soul_training/SOUL_IDS.json`\n\n")
            f.write(f"### {pid} — D{n}　[{slot['tier']} 級]　{slot['zone']}　{slot['device']}　{slot['framing']}　光:{code}　{wc} 字\n\n")
            f.write("```\n"+txt+"\n```\n\n")
    print(f"寫出 {len(out)} 段")
    ws=[o[5] for o in out]
    print(f"字數 min={min(ws)} max={max(ws)} avg={sum(ws)//len(ws)}")

if __name__=="__main__": main()
