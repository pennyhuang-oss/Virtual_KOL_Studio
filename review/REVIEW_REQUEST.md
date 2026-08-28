# 覆核請求 R12：11 件未跑 prompt 的**完整全文**逐件覆核

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄或讀 repo 背景。回覆填在最後的「回覆區」。

## 這個專案要對標的帳號（每輪都附）

競品 @sherry_digitalp510（小雪莉）是全 AI 生成、公開自承虛擬人的 IG 帳號，57 萬追蹤。
請在逐件判定之外，**額外用「這則看起來像不像真人的日常」這個角度檢查**：
① 打光寫物理路徑（具名光源／具名反射面／哪一區被犧牲）② 曝光一定犧牲一邊
③ 一個畫面兩個色溫（有兩個光源時）④ 公共場景一定有背景路人
⑤ 視角混合（自拍／他拍／背後跟拍／俯拍）⑥ 框架物入鏡製造天然暗角
⑦ 地點要有 C 級不美的日常 ⑧ 姿勢與微物件每則都換，永不重複的節奏本身才是真實感
⑨ 不要寫 grainy／muddy／degraded，畫質仍要清晰

---

## 為什麼要重新覆核整段

使用者問「要送出去跑的 prompt 都讓 ChatGPT 複核過了嗎」。查證後答案是**沒有**：

- LG-01 是 R10 判 REVISE、R11 只裁決了**片語層級**的還原
- **組裝後的完整 prompt，從來沒有人看過整段**，我就送生成了
- 我把「片語被核可」當成「整段被核可」——那是我自己的判斷，不是你給的授權

已建立 `tools/approval_check.py` 指紋閘門（**這是你在 R7 Q5 就建議過的，我遲了四輪才做**）：
規格表登記 prompt 的 sha1，只有指紋相符的件才可送生成，覆核後改一個字就變「改過字」擋下。

**本檔的 11 件目前全部是「未覆核」狀態，一件都不能送生成。**
請對**完整 prompt 全文**逐件判定，通過的我才登記指紋。

## 這一輪已知的新事實（供判斷參考）

**LG-01 preflight 的結果**（框架物那一類的第一次實測）：
- ✅ **隔窗框架物成立**：臉與雙手隔玻璃清楚可見，**沒有重影、沒有多手**。
  你把「玻璃反光」改成「單側窗框」是對的。
- ❌ **視線 2/2 直視鏡頭**，而 `to one side of the camera` 這句**確實在 prompt 裡**。

  對照已成功的案例：LG-03 看貓（同框）✅、LG-06 看手上扭蛋（同框）✅、
  LG-01 看「鏡頭一側的車流」（**畫面外**）❌。

  **我的推論**：視線要離開鏡頭，必須給**畫面內看得見的目標**；
  「看向畫面外的某物」沒有可對焦的對象，就退回預設的看鏡頭。n=2，與 D-06 一致。

  **本批有 8 件宣告「不看鏡頭」，請用這條檢查它們的視線目標在不在畫面內。**

**LG-07 preflight**：背後跟拍、回頭、環握桶靠髖側 3 項皆 2/2 成立（已核准）。

---
## YG-03｜陽台・收乾淨的衣服

姿勢：**A 動作中**（正在把毛巾從晾衣桿上取下）｜相機：**1 自拍**｜視線：看鏡頭｜手在臉旁：否

- **凍結瞬間**：伸手把一條白毛巾從晾衣桿上拉下來的那一瞬間，手臂還舉著，轉頭對鏡頭笑。
- **手部任務**：拍攝手／鏡外手：持手機自拍，**off-frame**（仍佔一隻解剖學的手） ／ 可見手 A：舉起、正把白毛巾從晾衣桿上拉下 ／ 可見手 B：**N/A**——兩隻手已用完
- **硬驗收**：① 自拍構圖成立且**手機不入鏡** ② **只有一隻可見手**，且**手臂是舉起的、正在取毛巾**（不是抱在胸前）③ 畫面無任何印刷文字 ④ 半身比例
- **不可刪除措辭**：`The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame.`（R8a 封住自拍手與手機入鏡）

```text
In a phone selfie, a young woman pulls a plain white towel down off the drying pole, arm still raised, smiling at the camera. The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame. Close half-body framing, camera just above her eye level. Collarbone-length mocha brown hair in a low ponytail, see-through bangs. A grey fitted cropped cotton tee, high-waisted black shorts, black-rimmed glasses. A narrow covered balcony, a white painted wall, an iron window grille, plain towels on the pole. Flat overcast daylight on her face, her face evenly exposed, the white wall bouncing cool fill onto her jaw, staying slightly darker than her skin. Natural skin texture, subtle film grain.
```

## YG-06｜汗蒸幕・甜米露

姿勢：**D 非站坐體位**（盤腿坐地、上身後仰）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：盤腿坐在木地板上，蒸完澡整個人鬆掉，上半身往後仰、單手撐在身後地板上，臉朝上笑出來，紙杯放在身旁地上。
- **手部任務**：可見手 A：撐在身後的木地板上，支撐後仰的上半身 ／ 可見手 B：自然放在膝上 ／ 紙杯**放在地上**，不佔手
- **硬驗收**：① 盤腿坐姿、全身入鏡 ② 上半身後仰、一手撐地 ③ **視線不在鏡頭上**（臉朝上）④ 頭上毛巾羊角可見
- **不可刪除措辭**：`with one hand planted on the floor behind her and her other hand relaxed on one knee`（R10/R11 具名接觸面＋補上原本漏寫的第二隻手）

```text
A young woman sits cross-legged on a heated floor, leaning back with one hand planted on the floor behind her and her other hand relaxed on one knee, shoulders dropped, face tilted upward in a loose open-mouthed laugh, a paper cup beside her. Full body, camera at her seated eye level, shot from well back. Collarbone-length mocha brown hair in a low bun, damp strands at her temples. A grey sauna tee and shorts, a towel folded into sheep horns on her head, bare feet. A bright sauna rest hall. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm ceiling light on her face, the wooden floor bouncing warm fill up onto her chin, the hall behind her staying readable and slightly darker. Natural skin texture, subtle film grain.
```

## YG-07｜客廳地板・什麼都沒發生

姿勢：**D 非站坐體位**（坐地板）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：坐在地板上專心滑手機，一手伸進零食袋裡摸，嘴裡還在嚼、一邊臉頰鼓著，完全沒注意到有人在拍。
- **手部任務**：可見手 A：拿著手機在滑（手機入鏡，這件不是自拍） ／ 可見手 B：伸進零食袋 ／ 無第三個手部任務
- **硬驗收**：① 坐在地上 ② 一手滑手機、一手伸進零食袋（**可見手剛好兩隻**）③ **視線在手機上、不看鏡頭** ④ 一邊臉頰鼓著
- **不可刪除措辭**：`Exactly two hands are visible.`（R8a 鎖定可見手數）

```text
A young woman sits on the floor absorbed in her phone held in one hand, her other hand reaching into a snack bag, one cheek full mid-chew, her eyes down on the screen. Exactly two hands are visible. Half body, camera level with her face as she sits. Collarbone-length mocha brown hair, the top half clipped up. A beige camisole and short cotton shorts. A living room floor, a low sofa, magazines. Cool window light on her face, a warm lamp glowing behind her, the pale floor bouncing fill onto her chin. Her face is clearly exposed with natural skin texture; the window is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## YG-08｜台式早餐店・第一則吃

姿勢：**A 動作中**（端著盤子走到座位、正拉開椅子）｜相機：**6 框架物取景**（從騎樓柱旁拍進店裡）｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：一手端著裝了蛋餅的鐵盤，另一手正把紅色塑膠椅往外拉開，低頭看著要坐的位置。
- **手部任務**：可見手 A：端著裝了蛋餅的鐵盤 ／ 可見手 B：抓著紅色塑膠凳的**凳面側緣**往外拉 ／ 無第三個手部任務
- **硬驗收**：① 一手端鐵盤、另一手抓凳面側緣往外拉（**身體正在移動中**）② **視線朝下、不看鏡頭** ③ 人與食物同框（蛋餅在盤上）④ **騎樓柱只佔單側最外緣，不與人、盤、凳重疊**
- **不可刪除措辭**：`confined to the far outer edge`（R11 限制框架物寬度） ／ `clearly visible in the central area`（R11 劃定中央安全區）

```text
A young woman carries a metal tray with an egg crepe, her other hand gripping the side edge of a red plastic stool and pulling it out, eyes down on the seat. Half body, camera level with her chest, a narrow concrete pillar confined to the far outer edge, with her hands, tray, food, and stool clearly visible in the central area. Collarbone-length soft wavy mocha brown hair, side-parted. A light blue shirt knotted at the waist, white high-waisted shorts. A breakfast shop, a steel counter. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## YG-09｜飯店窗邊・皮膚特寫

姿勢：**B 支撐姿勢**（靠窗框）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否（無手）

- **凍結瞬間**：臉部大特寫，側身靠著窗框，眼睛看著窗外遠處，睫毛半垂、嘴唇放鬆——這件刻意不做表情。
- **手部任務**：可見手 A：**N/A**（臉部大特寫，裁切外） ／ 可見手 B：**N/A**（裁切外） ／ **本件沒有任何手部任務**
- **硬驗收**：① 臉部大特寫比例，臉佔滿畫面 ② 視線在畫面外、**不看鏡頭** ③ **畫面內沒有任何手** ④ 光線正面均勻、無逆光
- **不可刪除措辭**：`with both arms and hands below the frame`（R8b 正面寫法鎖定裁切，取代否定句）

```text
A young woman leans against the window frame gazing far out through the glass, lashes lowered, lips relaxed. Tight close-up of her face, camera at her eye level. The crop contains only her face, hair, neck, and bathrobe collar, with both arms and hands below the frame. Collarbone-length mocha brown hair pushed back off her face. A white bathrobe with the collar loosened. A hotel room, white bedding, a floor-to-ceiling window, city towers outside. Soft window light full on her face, the white bedding bouncing fill up under her jaw. Her face is clearly exposed with natural skin texture; the city outside is the brightest area, only its smallest highlights reaching white. Visible skin pores, subtle film grain.
```

## YG-10｜百貨美妝櫃・精緻的一面

姿勢：**B 支撐姿勢**（前傾靠櫃檯）｜相機：**4 過肩**｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：從她身後越過肩膀拍：她低頭把口紅在手背上劃一道，注意力全在手背的顏色上。
- **手部任務**：可見手 A：手背朝上攤平，承接試色 ／ 可見手 B：拿著口紅，正在手背上劃 ／ 無第三個手部任務（**這件的兩隻手在腰腹高度、遠離臉部，不會與臉部區域競爭**）
- **硬驗收**：① **過肩視角**：她的肩膀或後腦在前景，櫃檯與手背在畫面中段 ② 一手攤平、一手拿口紅劃在其上 ③ **視線在手背上、不看鏡頭** ④ 半身比例
- **不可刪除措辭**：

```text
Seen from behind over her shoulder, a young woman leans toward the counter and draws a lipstick stripe across the back of her other hand, her eyes down on the swatch. Half body, camera behind her shoulder at chest level. Sleek glossy collarbone-length mocha brown hair, side-parted, ends curving slightly inward. A cream cropped fitted knit top, off-white high-waisted straight trousers, gold hoop earrings. A department store beauty floor, glass counters, rows of lipsticks, glossy pale columns. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool recessed ceiling light on her, warm accent light inside the glass cases, the white counter bouncing fill onto her jaw, the floor behind her slightly darker. Natural skin texture, subtle film grain.
```

## LG-02｜房間晨光・第一則「她在台北」

姿勢：**A 動作中 ＋ D 非站坐體位**（正在蹲下）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：**是**（2026-08-29 更正——揉眼在物理上就是手在臉旁，先前誤記為否，使整批統計失真。**不因此改姿勢**，只把指標如實記錄）

- **凍結瞬間**：蹲下來，一手的指尖停在地板的光斑上，另一手揉著一隻眼睛，嘴巴打呵欠打到一半。
- **手部任務**：可見手 A：指尖停在地板光斑上 ／ 可見手 B：揉一隻眼睛 ／ 無第三個手部任務
- **硬驗收**：① 蹲姿 ② 一手指尖在地板光斑上 ③ 另一手揉眼 ④ **沒被揉的那隻眼睛朝下看向光斑**（不可看向鏡頭）
- **不可刪除措辭**：`her open eye lowered`（R10 沒被揉的那隻眼不可看鏡頭）

```text
A young woman crouches, knees together, the fingertips of one hand on a sunlit patch of floor while her other hand rubs one eye, her open eye lowered toward the patch, mouth mid-yawn. Three-quarter body to just above the knees, camera level with her face, shot from well back. A blunt chin-length black bob cut evenly at the jawline, sleep-mussed, one side flattened. A white lace-trimmed camisole pyjama top and shorts. A bright clean room, white walls, a pale wood floor, a half-unpacked box. Soft morning light on her face, the white walls bouncing fill back. Her face is clearly exposed with natural skin texture; the window is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## LG-05｜公車站・雨停前

姿勢：**A 動作中**（正要走出亭子、撐開傘）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：雨還沒完全停，她正要走出候車亭，一手把透明傘撐開舉到頭頂上，另一手伸到亭外、掌心朝上試雨還下不下，視線落在掌心那幾滴雨上。
- **手部任務**：可見手 A：舉在頭頂、握著撐開的透明傘的傘柄 ／ 可見手 B：伸到亭外、掌心朝上試雨 ／ 無第三個手部任務
- **硬驗收**：① **傘是撐開的**，傘柄握在手中、傘面在她頭頂上方（接觸點明確，不可浮空）② 另一手伸到亭外、掌心朝上 ③ **視線落在掌心、不看鏡頭** ④ 景別到小腿中段
- **不可刪除措辭**：`palm turned up to feel for rain`（R10 取代沒有功能的拎裙襬）

```text
A young woman steps out from the bus shelter, one hand raised holding the handle of a clear umbrella opened above her head, her other hand reaching out with the palm turned up to feel for rain, eyes on the drops in her palm. Framed down to mid-calf, camera at her navel level, shot from well back. A blunt chin-length black bob with even blunt ends along the jawline. An off-white cotton button-front blouse fastened through the chest, a pale blue checked skirt. A route map lightbox, wet asphalt throwing warm sign colour back up. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Her face clearly exposed with natural skin texture; the signs are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

## LG-06｜可愛系街區・扭蛋機前

姿勢：**C 靜止站定**｜相機：**1 自拍**｜視線：看鏡頭（手機）｜手在臉旁：否

- **凍結瞬間**：轉到扭蛋之後在扭蛋機前自拍一張，一手把打開的扭蛋殼舉到胸前給鏡頭看，笑到眼睛瞇起來。
- **手部任務**：拍攝手／鏡外手：持手機自拍，**off-frame**（仍佔一隻解剖學的手） ／ 可見手 A：舉著打開的扭蛋殼在胸前 ／ 可見手 B：**N/A**——兩隻手已用完
- **硬驗收**：① 自拍構圖成立且**手機不入鏡** ② **只有一隻可見手**，舉著扭蛋殼在胸前 ③ 整排扭蛋機在她身後 ④ 半身比例
- **不可刪除措辭**：`The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame.`（R8a 封住自拍手與手機入鏡）

```text
In a phone selfie, a young woman holds an opened gachapon capsule up at chest level, laughing with her eyes crinkled. The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame. Half body, camera just above her eye level. A blunt chin-length black bob cut evenly at the jawline, two small clips holding her fringe back. A pale pink cropped knit top, white high-waisted shorts, a denim jacket at her waist. A row of colourful gachapon machines behind her, signage well out of focus. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Soft daylight on her face, evenly exposed, the coloured panels throwing colour onto her arms, the machines behind her staying slightly darker. Natural skin texture, subtle film grain.
```

## LG-09｜台式早餐店・豆漿

姿勢：**B 支撐姿勢**（手肘靠桌前傾）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：低頭把吸管插進豆漿杯的封膜，一手扶杯、一手捏吸管往下插，注意力全在那個動作上。
- **手部任務**：可見手 A：扶住玻璃杯 ／ 可見手 B：捏著吸管往下插 ／ 無第三個手部任務
- **硬驗收**：① 一手扶**塑膠豆漿杯**、一手捏吸管往下插 ② **視線在杯子上、不看鏡頭** ③ 人與豆漿杯同框 ④ 半身比例
- **不可刪除措辭**：`clear disposable plastic cup`（R10 玻璃杯配熱封膜物理不成立） ／ `sealed film lid`（R10 封膜是插吸管動作的接觸對象）

```text
A young woman holds a clear disposable plastic cup of soy milk steady with one hand while her other hand pushes a straw down through its sealed film lid, her eyes down on the cup. Half body with the cup in frame, camera at her eye level. A blunt chin-length black bob cut evenly at the jawline, centre-parted. A cream fitted thin-knit top with a clear waistline. A breakfast shop, a steel counter, the wall menu out of focus. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## LG-10B｜浴衣・蘋果糖（半身）

姿勢：**C 靜止站定**｜相機：**6 框架物取景**（透過攤位布簾之間）｜視線：看鏡頭｜手在臉旁：**是**（配額內 2/3）

- **凍結瞬間**：透過祭典攤位垂下的布簾之間拍過去：她站在攤子前，一手把蘋果糖舉在臉頰旁，笑到眼睛彎起來。
- **手部任務**：可見手 A：把蘋果糖舉在臉頰旁 ／ 可見手 B：自然垂在身側 ／ 無第三個手部任務
- **硬驗收**：① 一手舉蘋果糖在臉頰旁、**眼睛看鏡頭** ② **素面布簾只在左右最外緣形成窄條**，臉、蘋果糖、雙手與腰帶都在清楚的中央區③ 浴衣**左襟在上**、半幅帶綁緊收腰 ④ 半身比例
- **不可刪除措辭**：`with her face, candy apple, hands, and obi clearly visible in the centre`（R11 刪掉 hands 後布簾可遮住握糖接觸點） ／ `eyes toward the camera`（R10 metadata 說看鏡頭，prompt 必須明寫）

```text
A young woman holds a candy apple beside her cheek, her other arm relaxed at her side, laughing, eyes toward the camera. Half body, camera level with her chest, plain hanging cloth curtains forming narrow blurred strips at the far left and right edges, with her face, candy apple, hands, and obi clearly visible in the centre. A blunt chin-length black bob cut evenly at the jawline, half-pinned with a hairpin. A pale-blue floral yukata, the wearer's left panel over the right, a flat navy obi. Paper lanterns overhead. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm lantern light on her face, the approach underfoot bouncing warm fill up. Her face is clearly exposed with natural skin texture; the lanterns are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

---

## 回覆區（請只填這一段）

### 整批：8 件宣告「不看鏡頭」的視線目標，有幾件在畫面外？
- **判定**：**2 件在畫面外／沒有畫面內目標：YG-06、YG-09。其餘 6 件的目標都在畫面內。**
- **逐件點名**：
  1. **YG-06：畫面外／無可見目標。** 只有 `face tilted upward`，未指定她在看什麼；全身、平視機位也不保證天花板或頂燈入鏡，因此本質上仍是「朝畫面外方向看」。
  2. **YG-07：畫面內。** 目標是她手上的手機螢幕。
  3. **YG-08：畫面內。** 目標是正在拉出的紅色塑膠凳／座位，且凳子已被指定在中央安全區。
  4. **YG-09：畫面外。** `gazing far out through the glass` 沒有鎖定畫面內物件，硬驗收更直接寫「視線在畫面外」；這與 LG-01 已經 2/2 失敗的機制相同。雖然 prompt 列有 city towers，並未寫眼睛對焦於其中一棟可見高樓。
  5. **YG-10：畫面內。** 目標是畫面中段、她正在試色的手背。
  6. **LG-02：畫面內。** 目標是地板上可見的日照光斑。
  7. **LG-05：畫面內。** 目標是她攤開掌心中的雨滴。
  8. **LG-09：畫面內。** 目標是手中正在插吸管的豆漿杯。
- **建議改法**：YG-06 不必硬塞一個物件目標，可直接用「笑到雙眼閉起」封住直視鏡頭，並把硬驗收③改成眼睛閉起、臉朝上；這比虛構畫外目標自然。YG-09 若必須保留睜眼遠望，將一棟可見高樓放進臉旁窄幅窗景，寫明眼睛對焦於該高樓，並把硬驗收由「視線在畫面外」改成「視線落在畫面內可見高樓」。不要再用純方向詞要求不看鏡頭。

### YG-03
- **判定**：PASS ／ REVISE ／ BLOCK → **PASS**
- **理由**：自拍手在畫外、另一手與毛巾／晾衣桿有明確接觸，單一可見手與半身構圖閉合；手機不入鏡與無印刷文字也有直接約束。陽台家務是 C 級日常，少量家務自拍放在已有多種他拍視角的批次中，仍符合真人社群帳號會出現的自我記錄。
- **建議改法**：可登記目前全文指紋並送測。驗收需確認毛巾正在被可見手拉離晾衣桿，不接受毛巾或手臂浮空。

### YG-06
- **判定**：PASS ／ REVISE ／ BLOCK → **REVISE**
- **理由**：兩手位置、後仰重心、盤腿全身與公共汗蒸幕都已完整寫入，動作比舉杯到臉旁更像真人放鬆的抓拍；但「臉朝上」沒有畫面內視線目標，可能像 LG-01 一樣退回直視鏡頭。另紙杯目前只寫 `beside her`，刪掉了「在地板上」的接觸面，杯子仍有浮空或被模型交回手中的空間。
- **建議改法**：首句末段改為 `shoulders dropped, face tilted upward in a loose open-mouthed laugh with her eyes squeezed shut, a paper cup resting on the floor beside her`；硬驗收③同步改為「雙眼閉起、臉朝上，不看鏡頭」。修改後重新登記指紋。

### YG-07
- **判定**：PASS ／ REVISE ／ BLOCK → **PASS**
- **理由**：手機是畫面內明確視線目標；一手持手機、一手伸進零食袋、鼓著一邊臉頰與兩手總數也互相閉合。客廳地板、吃零食、沒注意鏡頭是本批最強的 C 級真人日常之一；窗光、暖燈與地板回彈亦有物理來源及曝光取捨。
- **建議改法**：可登記目前全文指紋並送測。視線必須實際落在手機螢幕，不能只低頭卻看向鏡頭或零食袋。

### YG-08
- **判定**：PASS ／ REVISE ／ BLOCK → **REVISE**
- **理由**：凳子是畫面內目標，柱子安全區、食物、雙手接觸點與背景路人也已完整恢復；但首句 `carries a metal tray with an egg crepe, her other hand...` 只用 `other` 暗示托盤由第一隻手拿，沒有直接寫 `in one hand`。更大的問題是半身構圖要同時看見低處的凳面側緣、抓凳的手與上方托盤，容易裁掉凳手或自行拉成更遠景，與硬驗收①④的安全需求競爭。
- **建議改法**：首句改成 `carries a metal tray with an egg crepe in one hand while her other hand grips the side edge of a red plastic stool and pulls it out`。景別放寬為至少大腿中段／three-quarter body，讓凳面接觸點、托盤與人物同框；若必須保留半身，就改用有椅背的紅色塑膠椅，讓抓握點提高到腰側可見範圍。不可維持無背矮凳又要求穩定半身。

### YG-09
- **判定**：PASS ／ REVISE ／ BLOCK → **REVISE**
- **理由**：大特寫、零手、窗光與床單回彈本身成立，也提供精緻畫面與 C 級日常之間的節奏落差；但本件直接使用已知失敗型的畫外視線。列出 `city towers outside` 不等於讓其中一棟成為可見對焦目標，現有 `gazing far out` 仍可能退回正視鏡頭。
- **建議改法**：在臉旁保留一條窄幅窗景，加入一棟清楚可見但不搶主體的遠方高樓，首句改為眼睛對焦該高樓；例如 `a distant tower visible through a narrow strip of window beside her face, her lowered eyes focused on it`。同步修改凍結瞬間與硬驗收②，不能一邊要求畫面內目標、一邊保留「視線在畫面外」。

### YG-10
- **判定**：PASS ／ REVISE ／ BLOCK → **PASS**
- **理由**：手背試色是畫面內視線錨點；過肩前景、櫃檯中段與雙手試色構成清楚的景深和單一任務。從對標角度看，這是有別於自拍／正面展示的真實購物行為；嵌燈、櫃內暖光與白檯回彈也具備物理路徑。
- **建議改法**：可登記目前全文指紋並送測。若只生成普通側面半身、沒有前景肩膀或後腦，不算過肩視角成立。

### LG-02
- **判定**：PASS ／ REVISE ／ BLOCK → **REVISE**
- **理由**：未被揉的眼睛已有畫面內光斑作目標，晨起蹲下、揉眼與打呵欠也很像 C 級日常；但 `Three-quarter body to just above the knees` 與「指尖接觸地板光斑」在垂直構圖上衝突。裁切停在膝上時，地板與觸地指尖通常位於裁切線下方，模型只能犧牲接觸點或自行違反景別拉遠。
- **建議改法**：硬驗收已不要求膝上景，直接將景別放寬為完整蹲姿／至少到小腿與地面接觸區，例如 `Full crouching body with the fingertips and sunlit floor patch visible, camera level with her face, shot from well back.` 保留 `her open eye lowered toward the patch`，修改後重新登記指紋。

### LG-05
- **判定**：PASS ／ REVISE ／ BLOCK → **PASS**
- **理由**：掌心雨滴是畫面內視線目標；開傘、握柄、另一手試雨與走出候車亭有真實因果，已消除上一版為姿勢而拎裙襬的擺拍感。中景路人、濕地暖色反射與高光犧牲也符合公共場景及物理光線規則。
- **建議改法**：可登記目前全文指紋並送測。驗收需看見傘柄與手接觸、傘面確實在頭頂，以及掌心位於亭外而未被背景人物遮住。

### LG-06
- **判定**：PASS ／ REVISE ／ BLOCK → **PASS**
- **理由**：自拍手 off-frame、另一手實際握住胸前扭蛋，單手可見性與半身構圖一致；在多數抓拍與不看鏡頭項目之間保留少量正面自拍，符合真人帳號的視角混合。扭蛋店與背景路人也有合理的公共生活感。
- **建議改法**：可登記目前全文指紋並送測。背景人物的肢體不得與主角輪廓黏連；主角仍只能有一隻可見手。

### LG-09
- **判定**：PASS ／ REVISE ／ BLOCK → **REVISE**
- **理由**：豆漿杯是畫面內目標，塑膠杯、封膜與吸管的物理關係已正確；插吸管也是可信的 C 級早餐日常。但姿勢宣告為「手肘靠桌前傾」，完整 prompt 完全沒有前傾、手肘或前臂接觸檯面的描述，因此目前只是一般半身站／坐姿，削弱本輪宣稱的姿勢多樣性。手部任務仍殘留「扶住玻璃杯」，也與 prompt／硬驗收的塑膠杯不一致。
- **建議改法**：把手部任務的「玻璃杯」改成「透明塑膠豆漿杯」；首句加入 `leaning forward over the counter with both forearms supported near its edge`，再接一手穩杯、一手插吸管。確認新增支撐不把手肘誤寫成額外手部任務，修改後重新登記指紋。

### LG-10B
- **判定**：PASS ／ REVISE ／ BLOCK → **REVISE**
- **理由**：視線看鏡頭已明寫，布簾也被限制在左右窄邊，框架物方向正確；但硬驗收②與不可刪除句要求 `hands` 複數都在清楚中央區，prompt 同時把第二隻手安排為 `other arm relaxed at her side`。半身裁切下，垂在身側的手通常落在腰線以下而被裁掉，模型可能拉遠、抬高手臂或違反「雙手清楚」才能同時滿足。這是完整組裝後才看得出的內部衝突。
- **建議改法**：把第二隻手改為自然輕放在 obi 正面／腰側，讓它在半身中央區確實可見；同步更新手部任務與首句，例如 `her other hand resting lightly on the front of her obi`。保留布簾安全區與 `eyes toward the camera`，修改後重新登記指紋。

### 其他（只寫會導致生成失敗的項目）
- 本輪 8 件「不看鏡頭」中，YG-06 可用閉眼直接消除畫外對焦問題；YG-09 則必須改成畫面內可見目標。其餘 6 件已有畫面內目標，不應因 LG-01 的 2/2 結果再做批次性改寫。
