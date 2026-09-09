#!/usr/bin/env python3
"""日常素材 v2：從 matrix.json 決定性地產生 100 段 prompt。

v1 失敗的六個根因（見 DIAGNOSIS.md）在這裡逐條被結構擋掉：

  R1 手機入鏡 → 相機一律只寫「輸出視角」，不寫「有人拿著手機站在哪」。
                 唯一例外是 mirror，鏡面自拍本來就該看到手機（v1 實測 2/2 正確）。
                 依 iris-chen/generation_notes.md 批次 4 的 ⚠️ 規則。
  R2 沒寫好看 → 每段強制帶 GLOW（妝、髮、膚）。Soul 提供身分，不提供好看。
  R3 光線醜   → 詞庫每一句都必須讓主光落在她臉上（§18），醜光句全部刪除。
  R4 C 級誤讀 → C 級只作用在「地點」，服裝一律時髦。稽核擋掉不時髦的服裝關鍵詞。
  R5 表情死   → 每格必須有具名表情（§20）＋ 具體姿勢，且過半要看鏡頭。
  R6 構圖散   → 刪掉 mid_environment；一律淺景深、人填滿畫面。

維持不動（都有實測支撐）：
  §9  公共場景背景路人四條件措辭（2026-08-05 的 14/14 ＋ v1 的 zoey D5）
  §11 地點寫環境元素、不點名地標
  §12 同穿搭一日敘事（2026-08-05 的 7/7）
  §3-D② 那串尾巴不跨角色固定套用 —— 改為按場景決定
"""
import json, glob, re

# ── R1 視角：只描述照片本身的輸出視角，不給模型一個可畫的相機或拍攝者 ──────────
VIEW = {
 "selfie_close":
   "A close-up front-facing selfie shot, the angle slightly above her looking down at her, "
   "framed the way her own phone front camera would frame it.",
 "mirror_half":
   "A mirror selfie: she is photographing her own reflection, the phone in her own hand at chest "
   "height, and the frame is what that phone sees.",
 "friend_near":
   "Shot from about a metre and a half away at her own eye level, a short portrait lens with the "
   "background falling into soft blur behind her.",
 "friend_full":
   "A full-length shot from about three metres away at her own eye level, head to feet inside the "
   "frame, the background softly out of focus.",
}
# 鏡面是唯一該看到手機的格式，但仍要擋掉第二個人與第二支手機
MIRROR_GUARD = ("The only reflection is her own; there is no second person and no second phone in the "
                "reflection, and no portrait or photograph of a person on any wall or screen.")
# R1 的正面封閉集合句（§9(b) 已驗證措辭），同時擋多餘手臂與入鏡相機
CLOSURE = ("Everything in this picture is accounted for: the only person in it is her, and every "
           "visible hand connects to one of her own arms.")

FRAMING = {
 "chest_up":"chest-up",
 "waist_up":"from the waist up",
 "three_quarter":"a three-quarter shot from the knees up",
 "full_length":"full length",
}

# ── R2 好看：Soul 給身分，這一段給「好看」。每段強制帶。 ──────────────────────
GLOW = ("Camera-ready natural makeup — an even lightweight base, softly groomed brows, curled "
        "separated lashes and a subtle lip colour. Her hair is styled and finished, not messy. Her "
        "skin is even and healthy with fine natural texture and a soft sheen where the light lands.")

# ── R3 光線：每一句都讓主光落在她臉上。§18 檢查「她的臉是畫面最亮的區域之一嗎？」 ──
# 逆光只能當輪廓光，且必須指名一個夠強的反射面把光丟回臉上。
LIGHT = {
 "K1":"Low golden-hour sun coming in from the front at about forty-five degrees, warm on her face, "
      "with a bright rim along her hair and shoulder and the background falling darker behind her.",
 "K2":"Soft daylight from a large window in front of her and slightly to one side, her face the "
      "brightest thing in the frame, the depth of the room falling away warm and dark.",
 "K3":"Open shade with a bright pale wall directly opposite her throwing a broad soft light back "
      "into her face, the sunlit street beyond blown out behind her.",
 "K4":"Bright overcast daylight coming from in front of her, even and flattering on the face, the "
      "sky behind her a touch brighter than she is.",
 "K5":"Warm light spilling out of the shopfronts in front of her, catching her face and the front "
      "of her clothes, the street behind her going dark.",
 "K6":"Late afternoon sun low and in front of her, warm across her face, her own long shadow "
      "running back behind her.",
 "K7":"Window light from the front-side in a cafe, clean on her face, the interior behind her "
      "falling into warm shadow with small bright highlights on glass.",
 "K8":"Blue evening light overall with one warm sign glowing in front of her, so her face carries "
      "the warm light and the street behind her stays cool.",
 "K9":"Bright daylight bouncing up off pale ground in front of her, filling under the chin and "
      "keeping her face open and clear, the sky behind her brighter than she is.",
 "K10":"Soft warm light from a vanity lamp directly in front of her face, the rest of the room "
       "falling quickly into shadow.",
 "K11":"Overhead daylight softened through cloud with a bright reflective surface in front of her — "
       "wet pavement, pale tiling — bouncing light back up into her face.",
 "K13":"The shop's own lighting, bright and even from in front of her, falling on her face and the "
       "front of her clothes, the night outside the glass going black behind her.",
 "K14":"Bright even indoor lighting from panels in front of and above her catching her face, with the "
       "polished floor and the mirrored surfaces bouncing light back up into it.",
 "K12":"Warm interior light from a lamp in front of her at face height, her face the brightest "
       "point, the depth of the room dropping into soft dark.",
}
# §3-D② 尾巴：按場景決定，不跨角色固定套用
TAIL_OK = {"K1","K4","K5","K6","K7","K9"}   # 戶外自然光與咖啡廳；室內人工光不加（§3-D② 原文：按場景決定）
TAIL = "Film grain, candid lifestyle photo, warm tones, shot on 35mm."

PEOPLE = {
 "solo":"She is the only person in the photograph; no other people are visible anywhere in the frame.",
 "background_ok":"A few anonymous strangers are in the mid-ground behind her going about their own "
   "business, backs turned or heads angled away, never looking at the camera, softly out of focus "
   "with slight motion blur, clearly different from her in build, age and clothing.",
}

# R4：不時髦的服裝關鍵詞——出現就中止
UNCHIC = ("apron","scrub","hospital","sweatshirt","knitted vest","pleated skirt and flat shoes",
          "work trousers","tabard","uniform polo","fleece")

def build(p, s):
    L=[]
    L.append(f"A photograph of a beautiful adult {p['ethnic']} woman in her twenties, {FRAMING[s['framing']]}.")
    L.append(f"Her hair is {p['hair_colour']}, {s['hair_style']}.")
    L.append(p["body"])
    L.append("She wears "+s["outfit"]+".")
    if s.get("continuity_from"):
        L.append("This is the exact same outfit as earlier that same day, the same garments in the "
                 "same colours, worn a few hours on: "+s.get("continuity_evolution","")+".")
    L.append("She is in "+s["scene"]+".")
    L.append(s["pose"])                                  # R5 具體姿勢
    L.append(s["expression"])                             # R5 具名表情
    L.append(LIGHT[s["light"]])                           # R3 主光在臉上
    L.append(GLOW)                                        # R2 好看
    L.append(VIEW[s["view"]])                             # R1 只寫視角
    if s["view"]=="mirror_half": L.append(MIRROR_GUARD)
    L.append("Visible with her: "+s["micro"]+".")
    L.append(PEOPLE[s["people"]])
    L.append(CLOSURE)                                     # R1 封閉集合
    if s["light"] in TAIL_OK: L.append(TAIL)
    return "\n".join(L)

# 允許 "in her free hand" / "in the other hand" 這類中間插形容詞的寫法——
# 舊版寫死 "in her hand"，"in her free hand" 就漏掉了（2026-09-09 反向測試抓到）
# 光線只能用在對得上的場景類別。v1→v2 過渡時 K10「梳妝檯燈」被套到超商門口，
# 這條規則就是為了讓那種錯誤中止而不是靠人眼發現。
SCENE_LIGHT = [
 (re.compile(r'vanity|washroom|studio wall with a barre', re.I), {"K10"}),
 (re.compile(r'convenience store|corner shop|laundromat|coin laundry|game-arcade|noodle shop|'
             r'dumpling counter|fast-food|post office counter|wholesale garment', re.I), {"K13","K3","K10"}),
 (re.compile(r'lift|lobby|station (?:exit|passage)|metro station|mall entrance|supermarket entrance|'
             r'gym|stairwell landing|stockroom', re.I), {"K14","K10"}),
 (re.compile(r'\bcafe\b|coffee (?:shop|bar|stand)|kopitiam|teahouse with|bakery', re.I), {"K7","K3"}),
 (re.compile(r'rooftop|bar at night|wine bar|hotel (?:bar|veranda)|music bar|lounge at night|'
             r'lantern-lit|at dusk|bath terrace', re.I), {"K8","K12"}),
 (re.compile(r'beach|paddy-field|boardwalk', re.I), {"K9"}),
]

HANDHELD = re.compile(r'\bin (?:her|one|the|his)\s+(?:\w+\s+){0,2}hands?\b|\bholding\b|'
                      r'\bunder (?:one |her )?arm\b|\bagainst her chest\b|\bcarrying\b|'
                      r'\bhooked in\b', re.I)

def audit(pid,n,s,txt,p):
    e=[]
    COLOUR=("black","brown","blonde","grey","gray","silver","red","pink","lilac","gold","ash",
            "chestnut","greige","honey","mint","blue","green","wine","platinum","orange")
    if not any(c in p['hair_colour'].lower() for c in COLOUR):
        e.append(f"C-1 hair_colour 不含顏色詞: {p['hair_colour']!r}")
    if not s.get("hair_style"): e.append("hair_style 空白")

    # R1：非鏡面格不得出現任何相機／拍攝者實體
    if s["view"]!="mirror_half":
        for w in ("phone","tripod","camera app","selfie stick","person holding"):
            if w in (s["scene"]+" "+s["micro"]+" "+s["pose"]).lower():
                e.append(f"R1 非鏡面格的場景/隨身物/姿勢寫了相機實體: {w}")
    if "Everything in this picture is accounted for" not in txt: e.append("R1 封閉集合句缺失")
    if s["view"]=="mirror_half" and "no second phone" not in txt: e.append("R1 鏡面排除句缺失")

    # R2：好看段落
    # 用獨立字面檢查 GLOW 真正要交付的三件事，不用整段常數比對——
    # 常數被清空時 "" in txt 恆真，會靜默放過（2026-09-09 反向測試抓到）
    for frag,label in (("natural makeup","妝"),("hair is styled","髮型"),("fine natural texture","膚質")):
        if frag not in txt: e.append(f"R2 GLOW 缺{label}")
    if "beautiful adult" not in txt: e.append("R2 開頭美貌詞缺失")
    for w in ("no retouching","no smoothing","unflattering","no beauty filter"):
        if w in txt.lower(): e.append(f"R2 反美貌措辭殘留: {w}")

    # R3：光線必須在白名單詞庫內（詞庫每句都已通過 §18 檢查）
    if s["light"] not in LIGHT: e.append(f"R3 未知光線代碼 {s['light']}")
    for rx,allowed in SCENE_LIGHT:
        if rx.search(s["scene"]) and s["light"] not in allowed:
            e.append(f"R3 光線 {s['light']} 與場景類別不符（此類場景可用 {sorted(allowed)}）")
            break

    # R4：服裝不得不時髦
    for w in UNCHIC:
        if w in s["outfit"].lower(): e.append(f"R4 服裝不時髦: {w}")

    # R5：表情必須具名（§20）
    if not s.get("expression") or "expression" not in s["expression"].lower().replace("expressive",""):
        if not re.search(r'\b(smile|smiling|laugh|grin|amused|pleased|calm|cool|soft|warm|playful|'
                         r'confident|serene|mischievous|composed)\b', s.get("expression",""), re.I):
            e.append("R5 表情沒有具名情緒")
    if not s.get("pose"): e.append("R5 姿勢空白")

    # R6：不得有廣角人小的構圖
    if s["framing"] not in FRAMING: e.append(f"R6 未知框架 {s['framing']}")

    # 手部預算：持握物件 ≤2，鏡面/自拍格 ≤1（一隻手已被手機或機身佔用）
    occ=len(HANDHELD.findall(s["pose"]))+len(HANDHELD.findall(s["micro"]))
    cap=1 if s["view"] in ("mirror_half","selfie_close") else 2
    if occ>cap: e.append(f"手部超額: 持握物件≈{occ} > 上限{cap}")

    # §12 同穿搭資料完整性
    if s.get("continuity_from"):
        if not s.get("continuity_evolution"): e.append("continuity_from 有值但缺 continuity_evolution")
        if "exact same outfit" not in txt: e.append("§12 同穿搭句缺失")

    # §3-F 裸否定句
    for m in ["no phone","no screen","no television","no mirror"]:
        if m in txt.lower(): e.append(f"§3-F 裸否定句風險: {m}")
    if e: raise SystemExit(f"[FAIL] {pid} D{n}: "+"; ".join(e))

def main():
    m={}
    for f in sorted(glob.glob('matrix_part*.json')): m.update(json.load(open(f)))
    out=[];rows=[]
    for pid in sorted(m):
        p=m[pid]
        for n,s in enumerate(p["slots"],1):
            if s.get("continuity_from"):
                src=p["slots"][s["continuity_from"]-1]
                if src["outfit"]!=s["outfit"]:
                    raise SystemExit(f"[FAIL] {pid} D{n}: continuity_from 服裝字串不同")
            txt=build(p,s); audit(pid,n,s,txt,p)
            wc=len(txt.split()); out.append((pid,n,s,txt,wc))
            rows.append({"persona":pid,"n":n,"tier":s["tier"],"view":s["view"],
                         "framing":s["framing"],"zone":s["zone"],"light":s["light"],"words":wc})
    # 全批不變量
    eyes=sum(1 for _,_,s,_,_ in out if s.get("eye_contact"))
    if eyes < 60: raise SystemExit(f"[FAIL] R5 看鏡頭只有 {eyes}/100，未過半數門檻 60")
    json.dump(rows,open('index.json','w'),indent=1,ensure_ascii=False)
    with open('PROMPTS.md','w') as f:
        f.write("# 日常素材 v2 — 100 段 prompt（產生檔，勿手改）\n\n"
                "> 由 `build_prompts.py` 從 `matrix_part*.json` 決定性產生。改內容請改資料檔後重跑。\n"
                "> 送生成時：`model='soul_2'` + 該位 `soul_id`，不掛 Reference Element，`aspect_ratio='3:4'`。\n\n")
        cur=None
        for pid,n,s,txt,wc in out:
            if pid!=cur: cur=pid; f.write(f"\n---\n\n## {pid}\n\n")
            f.write(f"### {pid} — D{n}　[{s['tier']} 級]　{s['zone']}　{s['view']}　"
                    f"{s['framing']}　光:{s['light']}　{wc} 字\n\n```\n{txt}\n```\n\n")
    ws=[w for *_,w in out]
    print(f"寫出 {len(out)} 段 | 字數 min={min(ws)} max={max(ws)} avg={sum(ws)//len(ws)} | 看鏡頭 {eyes}/100")

if __name__=="__main__": main()
