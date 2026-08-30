# 覆核請求 R14：相機方位這條軸線一直是空的

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄或讀 repo 背景。回覆填在最後的「回覆區」。

## 這個專案要對標的帳號（每輪都附）

競品 @sherry_digitalp510（小雪莉）是全 AI 生成的 IG 帳號，57 萬追蹤。請一併用
「這則像不像真人的日常」檢查：① 打光寫物理路徑 ② 曝光犧牲一邊 ③ 兩個色溫
④ 公共場景有背景路人 ⑤ **視角混合** ⑥ 框架物入鏡 ⑦ 地點要有 C 級不美的日常
⑧ 姿勢與微物件每則都換 ⑨ 不要寫 grainy／muddy／degraded

---

## 這一輪最重要的發現

使用者指出 **Luna 的素材「角度、姿勢、遠近基本上都沒差別」**。清點 21 段 prompt 後：

- **只有 2/21 指定了「相機在她的哪一側」**，其餘 19 件沒寫 → 模型一律給正面
- **0/21 有焦段語言**（10 件有 `out of focus`，但那只是在說背景糊掉）

**根因**：我一直把 D-02 驗證過的
`camera at her navel level, lens horizontal, shot from well back`
當成完整的相機規格在用。它有**高度、傾角、距離**，**唯獨沒有方位**——我從未發現。

### LG-07 的兩個版本是同件同 soul 的直接對照

| 版本 | 寫法 | 描述的對象 | 結果 |
|---|---|---|---|
| v1 | `hips angled away and shoulders turned toward the camera` | **她的身體** | ❌ 2/2 完全正面站立 |
| v2 | `Following her from behind` | **相機的位置** | ✅ 2/2 成立 |

**推論：寫相機的位置，不要寫身體的朝向。**
要她「轉身」是要模型解一個姿勢問題；要相機「走到她背後」是換一個視角問題。

**使用者的判斷是**：soul 只鎖臉，姿勢、景深、遠近應該從 prompt 解決，不重訓 soul。
（Luna 的 soul 已重訓過一次，成本高。）**這一輪就是照這個方向做的。**

## 本輪改了什麼

已為 9 件未跑的件加入**相機方位**與**鏡頭／景深**語言，方位覆蓋率 2/21 → 7/21：

| 件 | 新增的相機語言 |
|---|---|
| LG-02 | `Shot from her three-quarter front-left and slightly above, looking down at her` |
| LG-05 | `Shot from her side in profile as she steps out` |
| LG-09 | `shot from her three-quarter front-right`＋`on a short telephoto with the shop behind her compressed` |
| LG-10B | `shot on a short telephoto with the stalls behind her compressed` |
| YG-06 | `shot from her three-quarter back` |
| YG-08 | `shot from her side in profile at chest level` |
| YG-09 | `shallow depth of field with only her face sharp` |
| YG-03 | `the balcony behind her falling out of focus` |
| YG-10 | （原本就有 `Seen from behind over her shoulder`，未改） |

同時 YG-03、YG-10 補上 `high crew neckline`——R13 的領口橫向規則當時只套用在判 REVISE 的件，
**已放行的沒有回頭重掃**，結果 LG-06 兩張都因領口過低被使用者退掉。

## 請判斷的四題

### Q1｜「寫相機位置不要寫身體朝向」這條推論成立嗎？
證據只有 LG-07 一組同件對照。**這條要是錯的，我這 9 件就都改錯方向了。**

### Q2｜焦段與景深語言完全沒有實測（0/21 用過）
`short telephoto`、`compressed`、`shallow depth of field` 這些字對 `soul_2` 有效嗎？
還是會被忽略、甚至干擾別的東西？**要不要先單獨 preflight 一件再擴散？**

### Q3｜方位覆蓋率 7/21 夠嗎？分布合理嗎？
已核准的 12 件不能改（prompt 已凍結）。剩下 9 件裡我給了 4 種方位。
**還是應該更激進，把「正面」壓到更低？**

### Q4｜逐件看，這 9 段完整 prompt 有沒有問題？
特別是新加的相機句會不會跟既有的景別句、框架物句打架。

---
## LG-02｜房間晨光・第一則「她在台北」

姿勢：**A 動作中 ＋ D 非站坐體位**（正在蹲下）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：**是**（2026-08-29 更正——揉眼在物理上就是手在臉旁，先前誤記為否，使整批統計失真。**不因此改姿勢**，只把指標如實記錄）

- **硬驗收**：① **完整蹲姿、雙膝、雙手都可見** ② 一手指尖在地板光斑上 ③ 另一手揉眼 ④ **沒被揉的那隻眼睛朝下看向紙箱開口**（**2026-08-29 依 R13 改目標**——光斑是照明效果、不是必然獨立成形的實體，模型可能整片照亮而不畫出邊界）⑤ **指尖與光斑的接觸點在畫面內** ⑥ **高領睡衣、不露胸線**
- **不可刪除措辭**：`her open eye lowered`（R10 沒被揉的那隻眼不可看鏡頭） ／ `the box opening`（R13 視線：光斑是照明效果不是實體） ／ `high-neck sleeveless cotton pyjama top`（R13 領口尺度：camisole 是天然低領高風險款）

```text
A young woman crouches, knees together, the fingertips of one hand on a sunlit patch of floor while her other hand rubs one eye, her open eye lowered toward the opening of a large open cardboard box sitting in the sunlit patch, mouth mid-yawn. Her complete crouching pose, both knees, both hands, the fingertip-floor contact, the sunlit patch and the box opening are visible. Shot from her three-quarter front-left and slightly above, looking down at her, shot from well back. A blunt chin-length black bob cut evenly at the jawline, sleep-mussed, one side flattened. An opaque high-neck sleeveless cotton pyjama top with subtle lace trim, and shorts. A bright clean room, white walls, a pale wood floor. Soft morning light on her face, the white walls bouncing fill back. Her face is clearly exposed with natural skin texture; the window is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## LG-05｜公車站・雨停前

姿勢：**A 動作中**（正要走出亭子、撐開傘）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **硬驗收**：① **傘是撐開的**，傘柄握在手中、傘面在她頭頂上方 **✅ 2/2 已驗證** ② 另一手伸到亭外、掌心朝上 **✅ 2/2** ③ **視線抬起看向頭頂的傘面內側、不看鏡頭** ④ **小腿與濕地面在畫面下方 1/3 內可見** ⑤ **高圓領扣到鎖骨、上胸完全被不透明布料覆蓋、不露胸線**
- **不可刪除措辭**：`palm turned up to feel for rain`（R10 取代沒有功能的拎裙襬） ／ `the upper chest fully covered by fabric`（R13 領口尺度：fastened through the chest 無效，2/2 胸線外露） ／ `Her calves and the wet pavement are visible in the bottom third`（R13 景別：Framed down to X 無效，改列什麼必須看得見）

```text
A young woman steps out from the bus shelter, one hand raised holding the handle of a clear umbrella opened above her head, her other hand reaching out with the palm turned up to feel for rain, her eyes lifted to the underside of the clear canopy above her. Her calves and the wet pavement are visible in the bottom third of the frame. Shot from her side in profile as she steps out, camera at her navel level, shot from well back. A blunt chin-length black bob with even blunt ends along the jawline. An opaque off-white button-front blouse with a high round neckline at the collarbone, all upper buttons fastened, the upper chest fully covered by fabric, a pale blue checked skirt. A route map lightbox. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool overcast daylight falls on her face, while wet asphalt bounces a small amount of warm sign colour upward. Her face clearly exposed with natural skin texture; the signs are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

## LG-09｜台式早餐店・豆漿

姿勢：**B 支撐姿勢**（手肘靠桌前傾）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **硬驗收**：① 一手扶**塑膠豆漿杯**、一手捏吸管往下插 ② **視線在杯子上、不看鏡頭** ③ 人與豆漿杯同框 ④ 半身比例 ⑤ **高圓領上衣、不露胸線**
- **不可刪除措辭**：`clear disposable plastic cup`（R10 玻璃杯配熱封膜物理不成立） ／ `sealed film lid`（R10 封膜是插吸管動作的接觸對象） ／ `crew-neck`（R13 領口尺度：thin-knit top 未定義領型）

```text
A young woman leans forward over the counter with both forearms supported near its edge, holding a clear disposable plastic cup of soy milk steady with one hand while her other hand pushes a straw down through its sealed film lid, her eyes down on the cup. Half body with the cup in frame, shot from her three-quarter front-right at her eye level, on a short telephoto with the shop behind her compressed and softly out of focus. A blunt chin-length black bob cut evenly at the jawline, centre-parted. An opaque cream fitted crew-neck knit top with a clear waistline. A breakfast shop, a steel counter, the wall menu out of focus. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## LG-10B｜浴衣・蘋果糖（半身）

姿勢：**C 靜止站定**｜相機：**6 框架物取景**（透過攤位布簾之間）｜視線：看鏡頭｜手在臉旁：**是**（配額內 2/3）

- **硬驗收**：① 一手舉蘋果糖在臉頰旁、**眼睛看鏡頭** ② **素面布簾只在左右最外緣形成窄條**，臉、蘋果糖、雙手與腰帶都在清楚的中央區③ 浴衣**左襟在上**、半幅帶綁緊收腰 ④ 半身比例
- **不可刪除措辭**：`with her face, candy apple, hands, and obi clearly visible in the centre`（R11 刪掉 hands 後布簾可遮住握糖接觸點） ／ `eyes toward the camera`（R10 metadata 說看鏡頭，prompt 必須明寫）

```text
A young woman holds a candy apple beside her cheek, her other hand resting lightly on the front of her obi, laughing, eyes toward the camera. Half body, camera level with her chest, shot on a short telephoto with the stalls behind her compressed, plain hanging cloth curtains forming narrow blurred strips at the far left and right edges, with her face, candy apple, hands, and obi clearly visible in the centre. A blunt chin-length black bob cut evenly at the jawline, half-pinned with a hairpin. A pale-blue floral yukata, the wearer's left panel over the right, a flat navy obi. Paper lanterns overhead. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm lantern light on her face, the approach underfoot bouncing warm fill up. Her face is clearly exposed with natural skin texture; the lanterns are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

## YG-03｜陽台・收乾淨的衣服

姿勢：**A 動作中**（正在把毛巾從晾衣桿上取下）｜相機：**1 自拍**｜視線：看鏡頭｜手在臉旁：否

- **硬驗收**：① 自拍構圖成立且**手機不入鏡** ② **只有一隻可見手**，且**手臂是舉起的、正在取毛巾**（不是抱在胸前）③ 畫面無任何印刷文字 ④ 半身比例 ⑤ **高圓領、不露胸線**（2026-08-29 補：R13 的領口橫向規則當時只套用在判 REVISE 的件，已放行的沒有回頭重掃）
- **不可刪除措辭**：`The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame.`（R8a 封住自拍手與手機入鏡） ／ `high crew neckline`（R13 領口尺度橫向規則，2026-08-29 補掃）

```text
In a phone selfie, a young woman pulls a plain white towel down off the drying pole, arm still raised, smiling at the camera. The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame. Close half-body framing, camera just above her eye level, the balcony behind her falling out of focus. Collarbone-length mocha brown hair in a low ponytail, see-through bangs. An opaque grey fitted cropped cotton tee with a high crew neckline, high-waisted black shorts, black-rimmed glasses. A narrow covered balcony, a white painted wall, an iron window grille, plain towels on the pole. Flat overcast daylight on her face, her face evenly exposed, the white wall bouncing cool fill onto her jaw, staying slightly darker than her skin. Natural skin texture, subtle film grain.
```

## YG-06｜汗蒸幕・甜米露

姿勢：**D 非站坐體位**（盤腿坐地、上身後仰）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否

- **硬驗收**：① **完整頭部、盤腿與雙腳都可見，坐姿周圍保留地板** ② 上半身後仰、一手撐地 ③ **雙眼閉起、臉朝上，不看鏡頭**④ 頭上毛巾羊角可見
- **不可刪除措辭**：`with one hand planted on the floor behind her and her other hand relaxed on one knee`（R10/R11 具名接觸面＋補上原本漏寫的第二隻手） ／ `both bare feet are visible`（R13 景別：Full body 有裁腳反例，改列具體可見部位）

```text
A young woman sits cross-legged on a heated floor, leaning back with one hand planted on the floor behind her and her other hand relaxed on one knee, shoulders dropped, face tilted upward in a loose open-mouthed laugh with her eyes squeezed shut, a paper cup resting on the floor beside her. Her complete head, crossed legs, and both bare feet are visible, with floor visible around her seated body, shot from her three-quarter back at her seated eye level, shot from well back. Collarbone-length mocha brown hair in a low bun, damp strands at her temples. A grey crew-neck sauna tee and shorts, a towel folded into sheep horns on her head, bare feet. A bright sauna rest hall. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm ceiling light on her face, the wooden floor bouncing warm fill up onto her chin, the hall behind her staying readable and slightly darker. Natural skin texture, subtle film grain.
```

## YG-08｜台式早餐店・第一則吃

姿勢：**A 動作中**（端著盤子走到座位、正拉開椅子）｜相機：**6 框架物取景**（從騎樓柱旁拍進店裡）｜視線：不看鏡頭｜手在臉旁：否

- **硬驗收**：① 一手端鐵盤、另一手抓凳面側緣往外拉（**身體正在移動中**）② **視線朝下、不看鏡頭** ③ 人與食物同框（蛋餅在盤上）④ **騎樓柱只佔單側最外緣，不與人、盤、凳重疊** ⑤ **上半身與雙腿到大腿中段可見，兩個接觸點、托盤、食物、凳面都在中央區** ⑥ **襯衫有領、上方鈕扣扣上、上胸被覆蓋**
- **不可刪除措辭**：`confined to the far outer edge`（R11 限制框架物寬度） ／ `clearly visible in the central area`（R11 劃定中央安全區） ／ `both hand-object contact points`（R13 景別：down to mid-thigh 屬已證實失效的同類句） ／ `upper chest covered`（R13 領口尺度）

```text
A young woman carries a metal tray with an egg crepe in one hand while her other hand grips the side edge of a red plastic stool and pulls it out, eyes down on the seat. Her upper body and both thighs through mid-thigh are visible, with both hand-object contact points, the tray, food, and stool seat clearly visible in the central area, shot from her side in profile at chest level, a narrow concrete pillar confined to the far outer edge. Collarbone-length soft wavy mocha brown hair, side-parted. A light-blue collared button-front shirt knotted at the waist, its upper buttons fastened and upper chest covered, white high-waisted shorts. A breakfast shop, a steel counter. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## YG-09｜飯店窗邊・皮膚特寫

姿勢：**B 支撐姿勢**（靠窗框）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否（無手）

- **硬驗收**：① 臉部大特寫比例，臉佔滿畫面 ② **視線落在填滿臉旁窗景的鄰近建築立面上**（**2026-08-29 依 R13 修正**——「窄幅窗景中的遠塔」同時受大特寫與窄窗限制，模型可能只畫成模糊小形狀甚至省略，不符合「夠大、必然被畫出來」的條件）③ **畫面內沒有任何手** ④ 光線正面均勻、無逆光 ⑤ **浴袍衣襟交疊閉合到鎖骨、不露胸線**
- **不可刪除措辭**：`with both arms and hands below the frame`（R8b 正面寫法鎖定裁切，取代否定句） ／ `filling the visible strip of window beside her face`（R13 視線：目標要夠大、必然被畫出來） ／ `closed securely at the collarbone`（R13 領口尺度：大特寫下更容易把胸線帶進下緣）

```text
A young woman leans against the window frame, a nearby building facade filling the visible strip of window beside her face, her lowered eyes focused on that broad facade, lips relaxed. Tight close-up of her face, camera at her eye level, shallow depth of field with only her face sharp. The crop contains only her face, hair, neck, and bathrobe collar, with both arms and hands below the frame. Collarbone-length mocha brown hair pushed back off her face. An opaque white bathrobe with overlapping lapels closed securely at the collarbone. A hotel room, white bedding, a floor-to-ceiling window, city towers outside. Soft window light full on her face, the white bedding bouncing fill up under her jaw. Her face is clearly exposed with natural skin texture; the city outside is the brightest area, only its smallest highlights reaching white. Visible skin pores, subtle film grain.
```

## YG-10｜百貨美妝櫃・精緻的一面

姿勢：**B 支撐姿勢**（前傾靠櫃檯）｜相機：**4 過肩**｜視線：不看鏡頭｜手在臉旁：否

- **硬驗收**：① **過肩視角**：她的肩膀或後腦在前景，櫃檯與手背在畫面中段 ② 一手攤平、一手拿口紅劃在其上 ③ **視線在手背上、不看鏡頭** ④ 半身比例 ⑤ **高圓領、不露胸線**（2026-08-29 補：R13 的領口橫向規則當時只套用在判 REVISE 的件，已放行的沒有回頭重掃）
- **不可刪除措辭**：`high crew neckline`（R13 領口尺度橫向規則，2026-08-29 補掃）

```text
Seen from behind over her shoulder, a young woman leans toward the counter and draws a lipstick stripe across the back of her other hand, her eyes down on the swatch. Half body, camera behind her shoulder at chest level. Sleek glossy collarbone-length mocha brown hair, side-parted, ends curving slightly inward. An opaque cream cropped fitted knit top with a high crew neckline, off-white high-waisted straight trousers, gold hoop earrings. A department store beauty floor, glass counters, rows of lipsticks, glossy pale columns. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool recessed ceiling light on her, warm accent light inside the glass cases, the white counter bouncing fill onto her jaw, the floor behind her slightly darker. Natural skin texture, subtle film grain.
```

---

## 回覆區（請只填這一段）

### Q1 寫相機位置不要寫身體朝向，這條成立嗎
- **判定**：
- **理由**：
- **建議改法**：

### Q2 焦段與景深語言對 soul_2 有效嗎，要不要先單獨 preflight
- **判定**：
- **理由**：
- **建議改法**：

### Q3 方位覆蓋率與分布
- **判定**：
- **理由**：
- **建議改法**：

### LG-02
- **判定**：PASS ／ REVISE ／ BLOCK →
- **理由**：
- **建議改法**：

### LG-05
- **判定**：PASS ／ REVISE ／ BLOCK →
- **理由**：
- **建議改法**：

### LG-09
- **判定**：PASS ／ REVISE ／ BLOCK →
- **理由**：
- **建議改法**：

### LG-10B
- **判定**：PASS ／ REVISE ／ BLOCK →
- **理由**：
- **建議改法**：

### YG-03
- **判定**：PASS ／ REVISE ／ BLOCK →
- **理由**：
- **建議改法**：

### YG-06
- **判定**：PASS ／ REVISE ／ BLOCK →
- **理由**：
- **建議改法**：

### YG-08
- **判定**：PASS ／ REVISE ／ BLOCK →
- **理由**：
- **建議改法**：

### YG-09
- **判定**：PASS ／ REVISE ／ BLOCK →
- **理由**：
- **建議改法**：

### YG-10
- **判定**：PASS ／ REVISE ／ BLOCK →
- **理由**：
- **建議改法**：

### 其他（只寫會導致生成失敗的項目）
-
