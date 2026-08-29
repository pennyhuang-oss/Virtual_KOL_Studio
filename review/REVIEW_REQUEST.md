# 覆核請求 R13：LG-05 的修法 ＋ 6 件待確認的完整 prompt

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄或讀 repo 背景。回覆填在最後的「回覆區」。

## 這個專案要對標的帳號（每輪都附）

競品 @sherry_digitalp510（小雪莉）是全 AI 生成、公開自承虛擬人的 IG 帳號，57 萬追蹤。
請在逐件判定之外，**額外用「這則看起來像不像真人的日常」這個角度檢查**：
① 打光寫物理路徑 ② 曝光一定犧牲一邊 ③ 一個畫面兩個色溫（有兩個光源時）
④ 公共場景一定有背景路人 ⑤ 視角混合 ⑥ 框架物入鏡製造天然暗角
⑦ 地點要有 C 級不美的日常 ⑧ 姿勢與微物件每則都換，永不重複的節奏本身才是真實感
⑨ 不要寫 grainy／muddy／degraded，畫質仍要清晰

---

## 這一輪的三個新實測結果（會影響其他件，請一併檢查）

### 一、視線規律要修正：「在畫面內」是必要條件，不是充分條件

我上一輪從 LG-01 推論「視線要離開鏡頭必須給畫面內看得見的目標」，你也用它逐件檢查過。
**LG-05 推翻了這個說法的寬鬆版本**：

| 目標 | 性質 | 結果 |
|---|---|---|
| 貓（LG-03）／扭蛋（LG-06）／手機螢幕（YG-07） | 大、明確、一定會被畫出來 | ✅ |
| 鏡頭一側的車流（LG-01） | 畫面外 | ❌ 2/2 |
| **掌心裡的雨滴（LG-05）** | **掌心在畫面內，但雨滴根本沒被畫出來** | ❌ 2/2 |

**修正為：目標必須是畫面內、夠大、必然會被算圖畫出來的實體。**

**請用這條重新檢查本批**，特別是 YG-09（遠方高樓，在窄幅窗景裡，會不會太小？）
與 LG-02（地板光斑，算不算「必然會被畫出來的實體」？）。

### 二、景別 2/2 被拉近，`Framed down to X` 無效

| 件 | 要求 | 實得 |
|---|---|---|
| LG-07（已核准） | 全身、完整的腳 | 腳被裁 |
| **LG-05** | `Framed down to mid-calf` | 大腿處就裁掉 |

我在 LG-05 改成**正面指名「什麼必須看得見」**：
`Her calves and the wet pavement are visible in the bottom third of the frame`
（比照你在 R8b 給 LG-07 的 `her complete feet visible within the bottom third of the frame` 寫法）。
**這樣改對嗎？本批 YG-08（大腿中段）與 LG-02（完整蹲姿）也是同類要求，需要一起改嗎？**

### 三、LG-05 的服裝失控，且涉及尺度

prompt 寫 `An off-white cotton button-front blouse fastened through the chest`，
**A 張生成無扣低領上衣、B 張有扣但胸口敞開的 V 領，兩張胸線都明顯外露。**
這件過去就出過同型問題（R8a 曾因此刪掉「前兩顆解開」）。

我改成正面指定領口高度：`A high-necked off-white cotton blouse buttoned up to the collarbone`。
**`fastened through the chest` 為什麼無效？`buttoned up to the collarbone` 會有效嗎？
本批其他件的上衣需不需要同樣處理？**

### 已驗證成功的兩項（供參考，不必改）

- **LG-05 ①：撐開的傘 2/2 成功**——手握柄、傘面在頭頂兩個接觸關係都成立，
  沒有重現這件過去的浮空雨傘。R10 把收起的傘改成撐開是對的。
- **YG-07 已核准**（本批唯一跑過的件），③ 視線落在手機螢幕成功。

---

## 逐件內容（LG-05 是改過的草案，其餘 6 件是 R12 判 REVISE 後我照指定改法改完的版本）

## LG-05｜公車站・雨停前　**（本輪新改草案，未經覆核）**

姿勢：**A 動作中**（正要走出亭子、撐開傘）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：雨還沒完全停，她正要走出候車亭，一手把透明傘撐開舉到頭頂上，另一手伸到亭外、掌心朝上試雨還下不下，**抬眼看著頭頂那面透明傘的內側**。
- **手部任務**：可見手 A：舉在頭頂、握著撐開的透明傘的傘柄 ／ 可見手 B：伸到亭外、掌心朝上試雨 ／ 無第三個手部任務
- **硬驗收**：① **傘是撐開的**，傘柄握在手中、傘面在她頭頂上方（接觸點明確，不可浮空）**✅ 2/2 已驗證** ② 另一手伸到亭外、掌心朝上 **✅ 2/2** ③ **視線抬起看向頭頂的傘面內側、不看鏡頭** ④ **小腿與濕地面在畫面下方 1/3 內可見** ⑤ **領口扣到鎖骨、不露胸線**
- **不可刪除措辭**：`palm turned up to feel for rain`（R10 取代沒有功能的拎裙襬）

```text
A young woman steps out from the bus shelter, one hand raised holding the handle of a clear umbrella opened above her head, her other hand reaching out with the palm turned up to feel for rain, her eyes lifted to the underside of the clear canopy above her. Her calves and the wet pavement are visible in the bottom third of the frame, camera at her navel level, shot from well back. A blunt chin-length black bob with even blunt ends along the jawline. A high-necked off-white cotton blouse buttoned up to the collarbone, a pale blue checked skirt. A route map lightbox, wet asphalt throwing warm sign colour back up. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Her face clearly exposed with natural skin texture; the signs are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

## YG-06｜汗蒸幕・甜米露　（R12 REVISE 後已改）

姿勢：**D 非站坐體位**（盤腿坐地、上身後仰）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：盤腿坐在木地板上，蒸完澡整個人鬆掉，上半身往後仰、單手撐在身後地板上，臉朝上笑出來，紙杯放在身旁地上。
- **手部任務**：可見手 A：撐在身後的木地板上，支撐後仰的上半身 ／ 可見手 B：自然放在膝上 ／ 紙杯**放在地上**，不佔手
- **硬驗收**：① 盤腿坐姿、全身入鏡 ② 上半身後仰、一手撐地 ③ **雙眼閉起、臉朝上，不看鏡頭**④ 頭上毛巾羊角可見
- **不可刪除措辭**：`with one hand planted on the floor behind her and her other hand relaxed on one knee`（R10/R11 具名接觸面＋補上原本漏寫的第二隻手）

```text
A young woman sits cross-legged on a heated floor, leaning back with one hand planted on the floor behind her and her other hand relaxed on one knee, shoulders dropped, face tilted upward in a loose open-mouthed laugh with her eyes squeezed shut, a paper cup resting on the floor beside her. Full body, camera at her seated eye level, shot from well back. Collarbone-length mocha brown hair in a low bun, damp strands at her temples. A grey sauna tee and shorts, a towel folded into sheep horns on her head, bare feet. A bright sauna rest hall. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm ceiling light on her face, the wooden floor bouncing warm fill up onto her chin, the hall behind her staying readable and slightly darker. Natural skin texture, subtle film grain.
```

## YG-08｜台式早餐店・第一則吃　（R12 REVISE 後已改）

姿勢：**A 動作中**（端著盤子走到座位、正拉開椅子）｜相機：**6 框架物取景**（從騎樓柱旁拍進店裡）｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：一手端著裝了蛋餅的鐵盤，另一手正把紅色塑膠椅往外拉開，低頭看著要坐的位置。
- **手部任務**：可見手 A：端著裝了蛋餅的鐵盤 ／ 可見手 B：抓著紅色塑膠凳的**凳面側緣**往外拉 ／ 無第三個手部任務
- **硬驗收**：① 一手端鐵盤、另一手抓凳面側緣往外拉（**身體正在移動中**）② **視線朝下、不看鏡頭** ③ 人與食物同框（蛋餅在盤上）④ **騎樓柱只佔單側最外緣，不與人、盤、凳重疊** ⑤ **景別到大腿中段，凳面接觸點與托盤同框**
- **不可刪除措辭**：`confined to the far outer edge`（R11 限制框架物寬度） ／ `clearly visible in the central area`（R11 劃定中央安全區）

```text
A young woman carries a metal tray with an egg crepe in one hand while her other hand grips the side edge of a red plastic stool and pulls it out, eyes down on the seat. Three-quarter body down to mid-thigh, camera level with her chest, a narrow concrete pillar confined to the far outer edge, with her hands, tray, food, and stool clearly visible in the central area. Collarbone-length soft wavy mocha brown hair, side-parted. A light blue shirt knotted at the waist, white high-waisted shorts. A breakfast shop, a steel counter. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## YG-09｜飯店窗邊・皮膚特寫　（R12 REVISE 後已改）

姿勢：**B 支撐姿勢**（靠窗框）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否（無手）

- **凍結瞬間**：臉部大特寫，側身靠著窗框，臉旁保留一條窄幅窗景、裡面有一棟清楚可見的遠方高樓，**她的眼睛對焦在那棟高樓上**，睫毛半垂、嘴唇放鬆——這件刻意不做表情。
- **手部任務**：可見手 A：**N/A**（臉部大特寫，裁切外） ／ 可見手 B：**N/A**（裁切外） ／ **本件沒有任何手部任務**
- **硬驗收**：① 臉部大特寫比例，臉佔滿畫面 ② **視線落在畫面內可見的那棟遠方高樓上**③ **畫面內沒有任何手** ④ 光線正面均勻、無逆光
- **不可刪除措辭**：`with both arms and hands below the frame`（R8b 正面寫法鎖定裁切，取代否定句）

```text
A young woman leans against the window frame, a distant tower visible through a narrow strip of window beside her face, her lowered eyes focused on it, lips relaxed. Tight close-up of her face, camera at her eye level. The crop contains only her face, hair, neck, and bathrobe collar, with both arms and hands below the frame. Collarbone-length mocha brown hair pushed back off her face. A white bathrobe with the collar loosened. A hotel room, white bedding, a floor-to-ceiling window, city towers outside. Soft window light full on her face, the white bedding bouncing fill up under her jaw. Her face is clearly exposed with natural skin texture; the city outside is the brightest area, only its smallest highlights reaching white. Visible skin pores, subtle film grain.
```

## LG-02｜房間晨光・第一則「她在台北」　（R12 REVISE 後已改）

姿勢：**A 動作中 ＋ D 非站坐體位**（正在蹲下）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：**是**（2026-08-29 更正——揉眼在物理上就是手在臉旁，先前誤記為否，使整批統計失真。**不因此改姿勢**，只把指標如實記錄）

- **凍結瞬間**：蹲下來，一手的指尖停在地板的光斑上，另一手揉著一隻眼睛，嘴巴打呵欠打到一半。
- **手部任務**：可見手 A：指尖停在地板光斑上 ／ 可見手 B：揉一隻眼睛 ／ 無第三個手部任務
- **硬驗收**：① 蹲姿 ② 一手指尖在地板光斑上 ③ 另一手揉眼 ④ **沒被揉的那隻眼睛朝下看向光斑**（不可看向鏡頭）⑤ **指尖與光斑的接觸點在畫面內**
- **不可刪除措辭**：`her open eye lowered`（R10 沒被揉的那隻眼不可看鏡頭）

```text
A young woman crouches, knees together, the fingertips of one hand on a sunlit patch of floor while her other hand rubs one eye, her open eye lowered toward the patch, mouth mid-yawn. Full crouching body with the fingertips and sunlit floor patch visible, camera level with her face, shot from well back. A blunt chin-length black bob cut evenly at the jawline, sleep-mussed, one side flattened. A white lace-trimmed camisole pyjama top and shorts. A bright clean room, white walls, a pale wood floor, a half-unpacked box. Soft morning light on her face, the white walls bouncing fill back. Her face is clearly exposed with natural skin texture; the window is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## LG-09｜台式早餐店・豆漿　（R12 REVISE 後已改）

姿勢：**B 支撐姿勢**（手肘靠桌前傾）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **凍結瞬間**：低頭把吸管插進豆漿杯的封膜，一手扶杯、一手捏吸管往下插，注意力全在那個動作上。
- **手部任務**：可見手 A：扶住**透明塑膠豆漿杯** ／ 可見手 B：捏著吸管往下插 ／ 無第三個手部任務
- **硬驗收**：① 一手扶**塑膠豆漿杯**、一手捏吸管往下插 ② **視線在杯子上、不看鏡頭** ③ 人與豆漿杯同框 ④ 半身比例
- **不可刪除措辭**：`clear disposable plastic cup`（R10 玻璃杯配熱封膜物理不成立） ／ `sealed film lid`（R10 封膜是插吸管動作的接觸對象）

```text
A young woman leans forward over the counter with both forearms supported near its edge, holding a clear disposable plastic cup of soy milk steady with one hand while her other hand pushes a straw down through its sealed film lid, her eyes down on the cup. Half body with the cup in frame, camera at her eye level. A blunt chin-length black bob cut evenly at the jawline, centre-parted. A cream fitted thin-knit top with a clear waistline. A breakfast shop, a steel counter, the wall menu out of focus. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## LG-10B｜浴衣・蘋果糖（半身）　（R12 REVISE 後已改）

姿勢：**C 靜止站定**｜相機：**6 框架物取景**（透過攤位布簾之間）｜視線：看鏡頭｜手在臉旁：**是**（配額內 2/3）

- **凍結瞬間**：透過祭典攤位垂下的布簾之間拍過去：她站在攤子前，一手把蘋果糖舉在臉頰旁，笑到眼睛彎起來。
- **手部任務**：可見手 A：把蘋果糖舉在臉頰旁 ／ 可見手 B：輕放在腰帶正面 ／ 無第三個手部任務
- **硬驗收**：① 一手舉蘋果糖在臉頰旁、**眼睛看鏡頭** ② **素面布簾只在左右最外緣形成窄條**，臉、蘋果糖、雙手與腰帶都在清楚的中央區③ 浴衣**左襟在上**、半幅帶綁緊收腰 ④ 半身比例
- **不可刪除措辭**：`with her face, candy apple, hands, and obi clearly visible in the centre`（R11 刪掉 hands 後布簾可遮住握糖接觸點） ／ `eyes toward the camera`（R10 metadata 說看鏡頭，prompt 必須明寫）

```text
A young woman holds a candy apple beside her cheek, her other hand resting lightly on the front of her obi, laughing, eyes toward the camera. Half body, camera level with her chest, plain hanging cloth curtains forming narrow blurred strips at the far left and right edges, with her face, candy apple, hands, and obi clearly visible in the centre. A blunt chin-length black bob cut evenly at the jawline, half-pinned with a hairpin. A pale-blue floral yukata, the wearer's left panel over the right, a flat navy obi. Paper lanterns overhead. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm lantern light on her face, the approach underfoot bouncing warm fill up. Her face is clearly exposed with natural skin texture; the lanterns are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

---

## 回覆區（請只填這一段）

### 新結果一：視線目標「夠大、必然被畫出來」——本批哪幾件不合格
- **判定**：REVISE；本批不合格的是 **YG-09、LG-02**。LG-05、YG-08、LG-09 合格；YG-06 是閉眼、LG-10B 是看鏡頭，不適用這條離鏡視線規則。
- **逐件點名**：
  - **LG-05：合格。** 撐開的傘面是大面積、在頭頂且已由硬驗收①保證入鏡的實體；看傘面內側比看掌心雨滴可靠。
  - **YG-06：不適用。** 雙眼閉起，不需要外部視線目標。
  - **YG-08：合格。** 紅色凳面是大、具名、與手部接觸且硬驗收要求同框的實體。
  - **YG-09：不合格。** 「窄幅窗景中的遠方高樓」同時受大特寫與窄窗限制，模型可能只畫成模糊小形狀，甚至省略；即使出現，也未必大到能辨識眼睛正在對焦它。
  - **LG-02：不合格。** 光斑可以很大，但它是照明效果，不是必然獨立成形的實體；模型可把地板整體照亮而不畫清楚邊界，視線與指尖便失去可驗收目標。
  - **LG-09：合格。** 豆漿杯是主動作中心的大型近前景實體，且硬驗收要求人杯同框。
  - **LG-10B：不適用。** 視線直接看鏡頭。
- **建議改法**：
  - **YG-09**：不要以「遠方塔樓」當小目標。改成鄰近建築的一大片立面填滿窗邊可見區，例如：`a nearby building facade filling the visible strip of window beside her face, her lowered eyes focused on that broad facade`。窗景需占足以辨識的一側區域；若仍堅持極窄窗條，就不能把精確對焦高樓列硬驗收。
  - **LG-02**：把半拆紙箱移到光斑內，讓視線落在大而必畫出的箱口；指尖仍可接觸箱旁被照亮的地板。例：`a large open cardboard box sitting in the sunlit patch, her open eye lowered toward the box opening`。硬驗收④改驗箱口，⑤保留指尖與光斑接觸。

### 新結果二：景別改用「什麼必須看得見」的寫法，對嗎？哪幾件要一起改
- **判定**：REVISE；方向正確，且比單寫 `Framed down to X` 更可驗收，但它是較強的正面錨點，不是成功保證。本批 **LG-05、YG-06、YG-08、LG-02** 都應用同一原則；LG-10B 已把臉、糖、雙手、腰帶列為中央可見，無須再改。
- **理由**：模型對抽象景別名稱可以用近似構圖交差；列出具體可見部位與接觸點，才能把裁切結果綁到硬驗收。LG-05 新句已鎖小腿與濕地面，修法正確。YG-08 仍以 `down to mid-thigh` 為主，正是已證實會失效的同類句；YG-06 的 `Full body`、LG-02 的 `Full crouching body` 也仍偏抽象，尤其前者已有完整腳被裁的同型反例。
- **建議改法**：
  - **LG-05**：保留 `Her calves and the wet pavement are visible in the bottom third of the frame`。
  - **YG-06**：改成 `Her complete head, crossed legs, and both bare feet are visible, with floor visible around her seated body`。
  - **YG-08**：把景別句改成 `Her upper body and both thighs through mid-thigh are visible, with both hand-object contact points, the tray, food, and stool seat clearly visible in the central area`；保留單側柱最外緣限制。
  - **LG-02**：改成 `Her complete crouching pose, both knees, both hands, the fingertip-floor contact, and the sunlit patch are visible`。若採上題紙箱方案，再把箱口列入可見內容。
  - 不要只增加更多景別同義詞；具體可見清單應取代抽象重複。

### 新結果三：領口用 buttoned up to the collarbone 有效嗎？其他件要不要比照
- **判定**：REVISE；`buttoned up to the collarbone` 比 `fastened through the chest` 明確，但仍不足以單獨保證。應同時正面指定「領型高度＋上胸由不透明布料完整覆蓋」。
- **理由**：`fastened through the chest` 描述的是扣合範圍，不是領口幾何；模型仍可生成低 V 領，再把 V 領下方的鈕扣扣上，因此兩張都能在字面上部分符合卻露出胸線。`buttoned up to the collarbone` 提供了垂直高度錨點，方向較好，但 `high-necked`、`buttoned` 與 `collarbone` 仍可能被各自近似處理。直接指定高圓領／標準襯衫領，以及上胸完整被不透明布料覆蓋，約束更完整。
- **建議改法**：
  - **LG-05** 改成：`an opaque off-white button-front blouse with a high round neckline at the collarbone, all upper buttons fastened, the upper chest fully covered by fabric`。
  - 不要全批機械貼同一句，應依服裝處理。**YG-08** 的打結襯衫需補標準領與上方鈕扣扣合；**YG-09** 的 `bathrobe with the collar loosened` 會直接誘發開領，應改為交疊閉合到鎖骨；**LG-02** 的 lace-trim camisole 本身是低領高風險款，若胸線不可露，必須改成較高領睡衣上衣；**LG-09** 的薄針織上衣補高圓領。**YG-06** 一般 sauna tee 風險較低，可只明確成 `crew-neck sauna tee`。**LG-10B** 已有左襟在上與腰帶固定，不必套西式扣領句。

### LG-05
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：傘面是大且已驗證必畫出的視線目標，撐傘與試雨兩手任務也已 2/2 成立；小腿與濕地面的新可見句比原景別句正確。尚未放行的關鍵是領口：新句改善了高度資訊，但未完整鎖住領型與上胸覆蓋。另外，這版只寫暖招牌反光，臉部受光的物理來源與雨天冷色環境光不夠明確，真人日常感會比先前的雙色溫版本弱。
- **建議改法**：採用上方完整領口句；光線補成 `Cool overcast daylight falls on her face, while wet asphalt bounces a small amount of warm sign colour upward`，再接現有招牌局部高光犧牲句。其餘動作、視線與小腿可見句保留後可送 preflight。

### YG-06
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：閉眼朝上不受新視線規則影響；後仰、一手撐地、一手放膝與地上紙杯也形成自然且不重複的日常瞬間。問題是 `Full body` 加 `shot from well back` 已有同型裁腳反例，未正面列出交叉腿與雙腳必須看見。
- **建議改法**：加入上方「完整頭部、盤腿與雙腳均可見，坐姿周圍保留地板」句；服裝可收斂為 `a grey crew-neck sauna tee and shorts`。修後可送。

### YG-08
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：凳面是足夠大且必然入鏡的視線目標；端盤、拉凳、低頭看座位、柱邊框架與早餐店路人共同構成很像真人被抓拍到的 C 級日常。未通過處是景別仍使用已證實不可靠的 `down to mid-thigh`，且 `light blue shirt knotted at the waist` 沒有控制上胸開口。
- **建議改法**：改用上方具體可見清單，明列雙腿至大腿中段、兩個接觸點、盤與凳面；上衣改為 `a light-blue collared button-front shirt knotted at the waist, its upper buttons fastened and upper chest covered`。其餘可保留。

### YG-09
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：窗框、白床單反光、局部窗外高光與無手裁切方向合理，也具有人在飯店發呆的日常感；但窄幅窗景中的遠塔不符合新視線充分條件，大特寫又進一步壓縮它。另 `collar loosened` 與本輪已證實的領口失控方向相同，在臉部大特寫下更容易把胸線帶進下緣。
- **建議改法**：將目標換成填滿窗側可見區的鄰近建築立面，或降低硬驗收精度、不再要求能判定對焦某一棟遠塔；浴袍改為 `an opaque white bathrobe with overlapping lapels closed securely at the collarbone`。兩項修完再送。

### LG-02
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：蹲下、揉眼、打呵欠與碰地板是自然且有微物件／接觸關係的晨間瞬間；但光斑不是必然有清楚邊界的實體，無法穩定承擔精確視線目標。完整蹲姿也仍可能被模型用裁腳近景近似完成。lace-trim camisole 同時是本批另一個領口尺度風險。
- **建議改法**：依上方方案把大紙箱放入光斑，視線改落在箱口；明列完整蹲姿、雙膝、雙手、指尖接觸點、光斑與箱口可見。若不得露胸線，將上衣改為 `an opaque high-neck sleeveless cotton pyjama top with subtle lace trim`，不要保留天然低領的 camisole 名稱。

### LG-09
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：杯子是大、近且由雙手接觸的可靠視線目標；插吸管、熱封膜、前傾支撐與早餐店路人都具體而像真人日常，半身也足以容納所有硬驗收。唯一需要跟進的新系統性風險是 `thin-knit top` 未定義領型，模型可能自行補低領；若本輪尺度要求適用全批，不應留白。
- **建議改法**：上衣改為 `an opaque cream fitted crew-neck knit top with a clear waistline`。其餘可原樣送。

### LG-10B
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：看鏡頭不受離鏡視線新規則影響；半身構圖已正面列出臉、蘋果糖、雙手與腰帶位於中央，左右布簾只占外緣，沒有使用失效的 `Framed down to X`。浴衣左襟在上、腰帶固定也比一般開領上衣具有更明確的閉合結構。祭典路人、燈籠暖光與布簾天然暗角能成立真人日常視覺。
- **建議改法**：可原樣送。驗收仍需確認布簾沒有遮住握糖接觸點或腰帶上的另一手。

### 其他（只寫會導致生成失敗的項目）
- LG-05、YG-08、YG-09、LG-02、LG-09 的領口修正屬同一個尺度風險，但應依各自服裝結構改寫，不要把西式 `buttoned up` 字串硬套到浴袍、睡衣或針織上衣。
