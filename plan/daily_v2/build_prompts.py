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
   "framed the way her own phone front camera would frame it. Her other arm runs out of the bottom "
   "corner of the frame toward the camera, so only one of her hands is doing anything else.",
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
# 會照出人像的反射面（水面／濕柏油反射天空不算）。v1 有這條，v2 重寫時漏掉，
# 造成 jia-seo D5 有鏡面柱子卻沒有反射完整性句 —— 就是 v1 rin D4 的失效模式。
REFLECTIVE = re.compile(r"\bmirror\b|\bmirrored\b|her reflection|reflective surface", re.I)
def scene_text(slot):
    """場景的完整文字。2026-09-09 把 scene 拆成 location + scene_details 之後，
    所有原本讀 scene 的檢查都必須讀這個合體，否則會像我一開始那樣檢查到已停用的欄位。"""
    return slot.get("location","")+", "+slot.get("scene_details","")

def has_reflective(slot):
    return bool(REFLECTIVE.search(scene_text(slot)) or REFLECTIVE.search(slot["pose"]))

# 次要鏡面：畫面裡有鏡子但相機不是它。仍必須擋掉第二個人與第二支手機。
MIRROR_SECONDARY = ("The only reflection in that mirror is her own; there is no second person and no "
                    "second phone in it, and no portrait or photograph of a person on any wall or screen.")

CLOSURE = ("Everything in this picture is accounted for: the only person in it is her, and every "
           "visible hand connects to one of her own arms.")

FRAMING = {
 "chest_up":"chest-up",
 "waist_up":"from the waist up",
 "three_quarter":"a three-quarter shot from the knees up",
 "full_length":"full length",
}

# ── R2 好看：Soul 給身分，這一段給「好看」。每段強制帶。 ──────────────────────
# 2026-09-09 修正：原本寫 "fine natural texture and a soft sheen"，在 zoey（訓練圖全素顏）
# 身上讀成斑點色塊，在 rin（訓練圖有妝）身上才讀成光澤。
# 回頭查 identity_master.json —— 產生那 20 張已認可臉孔的 prompt —— 它寫的是
#   "Even, healthy-looking skin with fine natural texture AND subtle professional retouching"
# 兩半成對。我只抄了「紋理」那一半，漏掉「修飾」那一半，紋理就變成瑕疵。
# 這裡不再寫「紋理」（素顏調性的 Soul 會把它讀成不均勻），改寫均勻膚色＋修飾＋光落處的光澤，
# 並補上 identity_master 也有的眼神光——真實感交給光線與構圖負責，不交給皮膚負責。
GLOW = ("Camera-ready natural makeup — an even lightweight base, softly groomed brows, curled "
        "separated lashes and a subtle lip colour. Her hair is styled and finished, not messy. Her "
        "skin is even and healthy-looking with subtle professional retouching, clear and consistent "
        "in tone, with a soft sheen where the light lands and a small natural catchlight in both eyes.")

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
 "K7":"Window light from the front-side, clean on her face, the interior behind her "
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
 "K15":"Daylight through the front window together with the counter's own strip lighting, both "
       "coming from in front of her onto her face, the back of the room falling darker.",
 "K14":"Bright even indoor lighting from panels in front of and above her catching her face, with the "
       "polished floor and the mirrored surfaces bouncing light back up into it.",
 "K12":"Warm interior light from a lamp in front of her at face height, her face the brightest "
       "point, the depth of the room dropping into soft dark.",
}
# §3-D② 尾巴：按場景決定，不跨角色固定套用
TAIL_OK = {"K1","K4","K5","K6","K7","K9","K15"}   # 戶外自然光與咖啡廳；室內人工光不加（§3-D② 原文：按場景決定）
# 2026-09-09 移除。實測：帶這串尾巴的每一張都出現模擬底片邊框＋橘色邊緣亂碼文字
# （左右邊條平均亮度只有中央的 30-45%），不帶的都沒有。相關性 4/4 vs 3/3。
# 從 10 張那輪就存在，我連三輪漏掉，是用量測而不是目視才抓到。
#
# 我先前重新加回它的理由是「§3-D② 原文說按場景決定，不是禁用」＋「早期 Iris 好看的
# 14 張都帶這串」。但早期 Iris 是 Seedream 4.5，不是 Soul V2 —— 在 Soul V2 上它產生片框。
# 所以 §3-D② 當初「從模板刪除」的裁決在這個模型上是對的，我的重新加回是錯的。
TAIL = ""

PEOPLE = {
 "solo":"She is the only person in the photograph; no other people are visible anywhere in the frame.",
 # 2026-09-09 改寫：原措辭允許「heads angled away」，那仍會渲染出側臉 → 撞臉。
 # 改成只准後腦勺、加重失焦、人數降到一兩位。§9 的四條件仍在，但改為更強的版本。
 "background_ok":"One or two anonymous strangers are well back behind her, walking away with the "
   "backs of their heads to the camera so that no face is visible at any angle, heavily out of "
   "focus and reduced to soft shapes with motion blur, clearly different from her in build, age "
   "and clothing.",
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
    L.append(f"She is in {s['location']}, with {s['scene_details']}.")
    L.append(s["pose"])                                  # R5 具體姿勢
    L.append(s["expression"])                             # R5 具名表情
    L.append(LIGHT[s["light"]])                           # R3 主光在臉上
    L.append(GLOW)                                        # R2 好看
    L.append(VIEW[s["view"]])                             # R1 只寫視角
    if s["view"]=="mirror_half":
        L.append(MIRROR_GUARD)
    elif has_reflective(s):
        L.append(MIRROR_SECONDARY)
    L.append("Visible with her: "+s["micro"]+".")
    L.append(PEOPLE[s["people"]])
    L.append(CLOSURE)                                     # R1 封閉集合
    if TAIL and s["light"] in TAIL_OK: L.append(TAIL)
    return "\n".join(L)

# 允許 "in her free hand" / "in the other hand" 這類中間插形容詞的寫法——
# 舊版寫死 "in her hand"，"in her free hand" 就漏掉了（2026-09-09 反向測試抓到）
# 光線只能用在對得上的場景類別。v1→v2 過渡時 K10「梳妝檯燈」被套到超商門口，
# 這條規則就是為了讓那種錯誤中止而不是靠人眼發現。
SCENE_LIGHT = [
 (re.compile(r'vanity|washroom|studio wall with a barre', re.I), {"K10"}),
 (re.compile(r'convenience store|corner shop|laundromat|coin laundry|game-arcade|noodle shop|'
             r'dumpling|fast-food|post office|wholesale garment', re.I), {"K13","K15","K3","K10"}),
 (re.compile(r'lift|lobby|station (?:exit|passage)|metro station|mall entrance|supermarket entrance|'
             r'gym|stairwell landing|stockroom', re.I), {"K14","K10"}),
 (re.compile(r'\bcafe\b|coffee (?:shop|bar|stand)|kopitiam|teahouse with|bakery', re.I), {"K7","K3"}),
 (re.compile(r'rooftop|bar at night|wine bar|hotel (?:bar|veranda)|music bar|lounge at night|'
             r'lantern-lit|at dusk|bath terrace', re.I), {"K8","K12"}),
 (re.compile(r'beach|paddy-field|boardwalk', re.I), {"K9"}),
 # U3（2026-09-09）：K6「午後低斜陽＋長影」在 rin D4 柱廊連續兩次沒讀出來，
 # 出來是散射光、無方向性、無長影。判定該句在有遮蔽的建築場景無效，改用 K3（對面淺牆反射）。
 # 這是資料映射修正，不是新增黑名單。
 (re.compile(r'colonnade|shopping arcade|five-foot way|covered|courtyard|under the|shophouse|'
             r'\barch\b|lobby|passage', re.I), {"K3","K7","K14","K12","K8","K5","K10","K15","K11"}),
]

# 這三句光線斷言了夜晚／夜間燈光，場景就必須也是夜晚，否則畫面自相矛盾
# 「free hand」只有一隻。姿勢用掉了，隨身物就不能再拿走，否則物件會浮在空中
# （2026-09-09 A/B 實測：rin B 的罐子懸空，因為 pose 與 micro 都指派了 free hand）
# 表情必須交代眼睛在做什麼。zoey 那張面無表情的成因就是「眼睛沒有被指派任何事」。
EYES_DOING = re.compile(r'\beyes?\b|\bgaze\b', re.I)
# 讀起來冷／死／低頭的措辭，實測過會出面無表情或 v1 的低頭問題
DEAD_EXPR = ("without any smile","eyes lowered","expressionless","unbothered","too tired",
             "eyes half closed","chin level","flat, ")
# 手不准懸空，也不准手肘外翻——zoey 的手就是懸在鬢角旁邊沒碰到
HOVER_POSE = ("just touching","hovering","held near","close to her hair","elbow out","elbows out")

# 2026-09-09 使用者裁決：100 格全部要有露出，程度全面往上一級。
# 依據：她通過的 7 張每張至少一項露出，否決的 3 張一項都沒有。
SKIN = re.compile(r'crop tank|crop top|crop tee|crop shirt|cropped|bandeau|halter|camisole|spaghetti|'
                  r'sleeveless|tube top|slip dress|bikini|cover-up|low (?:open )?back|'
                  r'plunging|deep V|deep scoop|sweetheart|off-shoulder|one-shoulder|strapless|'
                  r'sports bra|shorts|mini skirt|micro skirt|short (?:\w+ ){0,3}skirt|'
                  r'leggings|midriff|cowl neck|low cowl|'
                  r'slit|corset|thin straps|sheer', re.I)
# 腰線斷點：不增加露出也能做出形狀。rin D4 的柱狀剪影就是缺這個。
WAIST = re.compile(r'high-waisted|tucked into|knotted at the waist|tied at the waist|belted|'
                   r'with a belt|corset|cinched|tie waist|wrap|smocked|ruched|bodycon|'
                   r'low-rise|worn short|worn cropped|cropped at the waist|at the waist|'
                   r'tied low on the hips|knotted at the hip|crop top|crop tank|crop tee|'
                   r'cropped|crop shirt|bandeau|sports bra', re.I)
# 全身框架必須有動作，不得正面直立
DYNAMIC_POSE = re.compile(r'leaning back|mid-stride|turned back over her shoulder|half-seated', re.I)

# 手／臂的佔用計數。2026-09-09：zoey D4 長出第三隻手，因為姿勢寫 both elbows resting
# （兩臂都被佔用）而隨身物又寫 basket on one arm。舊正則只認 hand 不認 elbow/arm。
LIMB_ONE  = re.compile(r'\b(?:her )?free hand\b|\bone hand\b|\bone arm\b|\bone forearm\b|'
                       r'\bher (?:near|far|other) hand\b|\bfingertips\b|\bher fingers\b|'
                       r'\bone palm\b|\bthumb hooked\b|\bon one arm\b', re.I)
LIMB_TWO  = re.compile(r'\bboth hands\b|\bboth elbows\b|\bboth arms\b', re.I)
FREE_HAND = LIMB_ONE

NIGHT_LIGHT = {"K13","K8","K12"}
NIGHT_SCENE = re.compile(r'\bat night\b|late at night|evening|dusk|\bnight\b', re.I)
# 場景字串會被套進 "She is in {scene}"，首名詞不能是檯面／桌面／梳妝台
SCENE_HEAD_BAD = re.compile(r'^(?:a|the)\s+(?:[\w\-]+\s+){0,3}(counter|table|worktop|vanity)\b'
                            r'(?!.*\b(?:with|in)\b)', re.I)

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
            if w in (scene_text(s)+" "+s["micro"]+" "+s["pose"]).lower():
                e.append(f"R1 非鏡面格的場景/隨身物/姿勢寫了相機實體: {w}")
    if "Everything in this picture is accounted for" not in txt: e.append("R1 封閉集合句缺失")
    if s["view"]=="mirror_half" and "no second phone" not in txt: e.append("R1 鏡面排除句缺失")
    # 2026-09-09：鏡面排除句說「反射裡只有她」，背景路人句說後面有人，
    # 在鏡面構圖下兩句互相矛盾（路人會出現在反射裡）。鏡面格一律單人。
    if s["view"]=="mirror_half" and s["people"]!="solo":
        e.append("鏡面格不得有背景路人——反射裡會出現他們，與鏡面排除句矛盾")
    if s["view"]!="mirror_half" and has_reflective(s) and "no second phone in it" not in txt:
        e.append("R1 場景/姿勢有會照出人像的反射面，卻沒有反射完整性句")

    # R2：好看段落
    # 用獨立字面檢查 GLOW 真正要交付的三件事，不用整段常數比對——
    # 常數被清空時 "" in txt 恆真，會靜默放過（2026-09-09 反向測試抓到）
    for frag,label in (("natural makeup","妝"),("hair is styled","髮型"),("subtle professional retouching","膚質修飾")):
        if frag not in txt: e.append(f"R2 GLOW 缺{label}")
    if "beautiful adult" not in txt: e.append("R2 開頭美貌詞缺失")
    for w in ("no retouching","no smoothing","unflattering","no beauty filter"):
        if w in txt.lower(): e.append(f"R2 反美貌措辭殘留: {w}")

    # R3：光線必須在白名單詞庫內（詞庫每句都已通過 §18 檢查）
    if s["light"] not in LIGHT: e.append(f"R3 未知光線代碼 {s['light']}")
    for rx,allowed in SCENE_LIGHT:
        if rx.search(scene_text(s)) and s["light"] not in allowed:
            e.append(f"R3 光線 {s['light']} 與場景類別不符（此類場景可用 {sorted(allowed)}）")
            break

    # 光線斷言夜晚 → 場景也必須是夜晚
    if s["light"] in NIGHT_LIGHT and not NIGHT_SCENE.search(scene_text(s)):
        e.append(f"光線 {s['light']} 斷言夜晚，但場景沒有寫夜晚")
    # 場景首名詞不能是檯面（"She is in a … counter" 不通）
    # 2026-09-09 依 GPT R2 2-2：原本的「檯面黑名單」只是在記住一次事故
    #（未來遇到 reception desk / checkout lane 還會再加 regex），
    # 真正的不變量是「location 必須是能接在 She is in ... 後面的地點片語」。
    # 拆成 location + scene_details 之後這個錯誤類別在資料層就消掉了，
    # 這條保留為 lint，抓「把檯面誤填進 location」的資料輸入錯誤。
    for fld in ("location","scene_details"):
        if not s.get(fld): e.append(f"{fld} 空白")
    if SCENE_HEAD_BAD.match(s.get("location","")):
        e.append("location 首名詞是檯面／桌面，不是地點——應移到 scene_details")

    # R4-A：每套都要有露出（使用者 2026-09-09 裁決）
    if not SKIN.search(s["outfit"]):
        e.append("R4 服裝沒有任何露出元素（使用者裁決 100 格全部要有）")
    # R4-B：每套都要有腰線斷點
    if not WAIST.search(s["outfit"]):
        e.append("R4 服裝沒有腰線斷點，剪影會變成柱子")
    # R4-C：全身框架不得配正面直立姿勢
    if s["framing"]=="full_length" and not DYNAMIC_POSE.search(s["pose"]):
        e.append("R4 全身框架配了正面直立姿勢（rin D3 坐姿通過／D4 站姿否決，同一套衣服）")

    # R4：服裝不得不時髦
    for w in UNCHIC:
        if w in s["outfit"].lower(): e.append(f"R4 服裝不時髦: {w}")

    # R5-A：表情必須交代眼睛，且不得用已知會出死臉的措辭
    if not EYES_DOING.search(s.get("expression","")):
        e.append("R5 表情沒有交代眼睛在做什麼")
    for w in DEAD_EXPR:
        if w in s.get("expression","").lower(): e.append(f"R5 死臉措辭: {w}")
    # R5-B：姿勢不得讓手懸空或手肘外翻
    for w in HOVER_POSE:
        if w in s.get("pose","").lower(): e.append(f"R5 姿勢會讓手懸空/手肘外翻: {w}")

    # R5：表情必須具名（§20）
    if not s.get("expression") or "expression" not in s["expression"].lower().replace("expressive",""):
        if not re.search(r'\b(smile|smiling|laugh|grin|amused|pleased|calm|cool|soft|warm|playful|'
                         r'confident|serene|mischievous|composed)\b', s.get("expression",""), re.I):
            e.append("R5 表情沒有具名情緒")
    if not s.get("pose"): e.append("R5 姿勢空白")

    # R6：不得有廣角人小的構圖
    if s["framing"] not in FRAMING: e.append(f"R6 未知框架 {s['framing']}")

    # §9 強化版措辭不得被改回舊版（舊版允許側臉 → 撞臉）
    if s["people"]=="background_ok":
        for frag in ("no face is visible at any angle","heavily out of focus",
                     "build, age and clothing"):
            if frag not in txt: e.append(f"§9 背景路人措辭不完整，缺: {frag}")

    # 四肢預算：姿勢與隨身物加起來不得超過她有的兩隻手臂
    def limbs(txt):
        return 2*len(LIMB_TWO.findall(txt)) + len(LIMB_ONE.findall(txt))
    cap_limb = 1 if s["view"] in ("mirror_half","selfie_close") else 2
    used = limbs(s["pose"]) + limbs(s["micro"])
    if used > cap_limb:
        e.append(f"四肢超額：姿勢＋隨身物共佔用 {used} 隻手臂，上限 {cap_limb}"
                 f"（自拍／鏡面格一隻手已被手機佔用）")

    # 手部預算：持握物件 ≤2，鏡面/自拍格 ≤1（一隻手已被手機或機身佔用）
    occ=len(HANDHELD.findall(s["pose"]))+len(HANDHELD.findall(s["micro"]))
    cap=1 if s["view"] in ("mirror_half","selfie_close") else 2
    if occ>cap: e.append(f"手部超額: 持握物件≈{occ} > 上限{cap}")

    # §12-B：延續句不得提到這套衣服沒有的部件
    #   2026-09-09：改寫服裝後 rin D4 變成無袖針織，延續句卻還寫「袖子推起來」；
    #   tammy D4 變成襯衫＋短褲，延續句還寫「長褲」與「針織」。兩件都是我漏改。
    if s.get("continuity_evolution"):
        ev=s["continuity_evolution"].lower(); of=s["outfit"].lower()
        for part,absent in (("sleeve","sleeveless"),):
            if part in ev and absent in of:
                e.append(f"§12 延續句提到 {part}，但服裝是 {absent}")
        for part in ("trousers","jeans","skirt","shorts","knit","shirt","dress","coat","blazer"):
            if part in ev and part not in of:
                e.append(f"§12 延續句提到「{part}」，但這套服裝沒有")

    # §12 同穿搭資料完整性
    if s.get("continuity_from"):
        if not s.get("continuity_evolution"): e.append("continuity_from 有值但缺 continuity_evolution")
        if "exact same outfit" not in txt: e.append("§12 同穿搭句缺失")

    # §3-F 裸否定句
    # §3-D②：這串尾巴已於 2026-09-09 因底片邊框實測移除，不得再出現。
    # 這條規則先前在一次改寫中整條消失，而 rule_regression 的清單也漏列它，
    # 所以測試回報「齊全」。兩個漏洞一起補。
    for w in ("grain","35mm","instagram","film"):
        if w in txt.lower(): e.append(f"§3-D② 出現已移除的尾巴字樣: {w}")

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
