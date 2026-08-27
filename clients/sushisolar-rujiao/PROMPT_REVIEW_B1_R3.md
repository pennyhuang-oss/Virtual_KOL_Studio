# 批次一 Prompt — 第三輪覆核（R3）

> R2 的 3 個 blocker 已修完，請確認修法正確、且沒有換出新問題。
> 專案：Virtual KOL Studio｜`soul_2` ＋ `soul_id`｜2026-08-27
> 上一輪判定：🟡 修完 5 點可進 4 張 preflight

## 這一輪只需要你確認三件事

1. **5 個必修點修法對不對**（第一節）
2. **鮑伯的全域改寫有沒有副作用**（第二節）——這一改動到 11 件，是這輪風險最大的
3. **可不可以放行 4 張 preflight**（第五節）

---

# 一、5 個必修點的處理

| # | 你要求的 | 我的處理 |
|---|---|---|
| 1 | YG-03 / 04 / 06 補回 `collarbone-length` | ✅ 三段都補了 |
| 2 | YG-03 首句不要把 phone 當可見物件 | ✅ 改成 `In a phone selfie, a young woman covers her mouth with her free hand...`，直接用你的版本 |
| 3 | LG-07 拿掉 `one eye winking` | ✅ 改成你建議的爆米花桶抵下巴、越過桶緣看鏡頭 |
| 4 | LG-10B `pin in her bun` → half-up bob | ✅ 改成 `steadies the Japanese hairpin in her half-up bob` |
| 5 | Luna 鮑伯改「剪裁長度」而非「視覺對稱」 | ✅ 全 11 件改寫，見第二節 |
| 加 | LG-06 加 `looking down at it` | ✅ 照做 |
| 加 | LG-09 機位改 eye level or slightly above | ✅ 照做——上目遣い是這件的核心驗收點 |

## 1-1 關於 LG-07：結論照做，但你的理由要修正一個事實

你寫「保留了**已實測失敗**的單眼 wink」。

**實測失敗的不是 wink，是浴室那張的「單眼瞇起＋嘴巴微張 ooh」。**
wink 從來沒有被當成指令測過——咖啡廳那張出現的 wink 是模型自己加的，不是我要求的。

不過**兩者同屬純臉部、風險同一類**，而且你給的替代寫法把表情錨到爆米花桶上，
更符合已驗證的規律。**所以結論照做，只是這條不能記成「已實測失敗」，要記成「與已知失敗同型、未測」。**

副作用：**這批 21 件現在沒有任何一件有吐舌。**我接受這個取捨（吐舌同樣未測），
但如果你認為表情多樣性的損失比風險更重要，請說。

## 1-2 你抓到的數量錯誤：確認是 17 件

已用腳本重數：

- 保留驗證字串 `background exposed the same brightness as her skin`：**17 件**
- 特殊改寫：**4 件**（YG-06 汗蒸幕、LG-05 雨後、LG-10A／10B 祭典燈籠）

R2 寫的 18 是錯的。**我把「總件數／分類件數一致性」也加進檢查清單。**

## 1-3 「validated baseline wording」的用詞我接受

你說不要把那句升格成 magic string——目前只證明「它與成功曝光一起出現」，
沒有證明「正是它、而且只有它造成成功」。**這個區分我完全同意**，已照你的用詞
寫進 SOP：標為 **validated baseline wording**，不是 universally proven formula。

---

# 二、🔴 鮑伯的全域改寫 —— 這輪最大的改動，請重點看

你指出 `symmetrical` 描述的是**視覺結果**，會跟刻意不對稱的造型打架
（LG-02 一側壓扁、LG-03 一側塞耳後、LG-08 濕髮貼臉）。**這個我同意，而且是我沒想到的。**

全 11 件改成你建議的寫法：

| | 舊（R2） | 新（R3） |
|---|---|---|
| 底層 | `a symmetrical blunt chin-length black bob ending evenly at the jawline` | `a blunt chin-length black bob cut evenly at the jawline` |
| 自然垂放時再加 | — | `balanced evenly on both sides` |

**哪幾件加了 `balanced evenly on both sides`（頭髮自然垂放）**：LG-01、LG-04、LG-05、LG-06、LG-09
**哪幾件只用底層**（造型本身不對稱）：LG-02（一側壓扁）、LG-03（塞耳後）、LG-07（貓耳髮箍）、LG-08（濕髮貼臉）、LG-10A／10B（半盤起）

**請確認兩件事：**
1. 這個「底層剪裁 ＋ 選擇性加對稱」的分配對嗎？特別是 LG-07（戴髮箍但頭髮是垂放的）我沒加，這樣對嗎？
2. `cut evenly at the jawline` 這句**完全未驗證**。它會不會反而比 `symmetrical` 更弱——
   因為它描述的是「剪法」這種抽象概念，而不是畫面上看得到的形狀？

---

# 三、Reference image：我自己去查了官方頁面，你是對的

我不想只靠轉述，所以直接抓了你給的那頁。**逐字確認**：

> "With a reference image, the prompt field becomes unavailable.
> Soul 2.0 uses the reference as the primary direction. You can still apply a Soul ID character."

## 這推翻了我原本的假設

我一直把參考圖理解成「在 prompt 之上再加一層鎖場景的手段」。
**實際上它是取代 prompt。**

所以我先前規劃的「用台北巷弄參考圖壓過韓國場景模板、同時保留文字控制服裝與姿勢」
**在官方產品邏輯裡根本不成立**。這條路要嘛全部交給參考圖，要嘛不用。

## 剩下的問題

API 是否與 Web UI 行為一致仍未知（schema 同時列出 `prompt` 與 `medias`）。
照你的建議，**這不擋本批 21 張**，等有純場景參考圖再單獨測。

---

# 四、檢查器已重寫，而且是照你說的分兩類

你指出上一輪的 `hair length 21/21` 與 `bob geometry 11/11` 都是 false pass。**兩個都成立。**

**根因比正規表達式的 bug 更嚴重：我的腳本把 `low ponytail`／`claw clip`／`low bun` 當成「有髮長」，
但我自己寫的規則明明說「造型不算長度」。腳本執行的規則跟文件寫的規則不一樣。**

已改：

- 檢查器移到 `tools/prompt_lint.py`，**只做字串型檢查**，檔頭第一段就寫明語意型問題它抓不到
- 髮長 token 收緊成真正的長度詞（`collarbone-length` / `chin-length` / `shoulder-length`…），**造型詞一律不算**
- 鮑伯改查 `cut evenly at the jawline`，**取消上一輪那個沒揭露的 half-pinned 豁免**（那是我 11/11 灌水的原因）
- 內建 `--selftest`：7 組 known-good / known-bad 樣本，**先證明檢查器會過也會擋，才拿去檢查正式內容**

自檢輸出：

```
✓ known-good 近景    無問題
✓ 造型冒充長度        ['缺明確髮長（造型不算長度）']
✓ 否定句             ['含否定句']
✓ 兩個時間點          ['兩個時間點']
✓ 全身卻寫 pores      ['非近景卻寫 pores']
✓ Luna 缺剪裁幾何      ['鮑伯缺剪裁幾何']
✓ 抽象飄動            ['抽象飄動描述']
自檢：通過——檢查器會過也會擋
```

正式內容：**21 件全過，字數 86–118**。

> 但照你的分類，這只是 **Mechanical lint**。
> Semantic review（手數、機位與視線衝突、spec 與 prompt 是否同一張圖）**還是靠你跟我人工看**。

---

# 五、Preflight 四張：照你的新建議

1. **YG-03** — selfie 邏輯／手部／補完髮長後穩不穩／超商場景
2. **LG-05** — 鮑伯剪裁幾何 ＋ Luna 戶外是否有場景模板
3. **LG-04** — 單一 frozen expression ＋ 花瓣實體 anchor
4. **LG-10A** — 全身複雜回身 ＋ 浴衣 ＋ 祭典特殊曝光句

成本 4 × 0.12 = **0.48 credits**。
四張照五項（Identity／Pose／Expression／Scene／Outfit）評分，**另外先跑瑕疵掃描**
（髮長對稱／手指／四肢／道具連貫／臉部對稱／文字／背景人物／衣物邏輯），
瑕疵中一項直接淘汰、不進評分。

**這一輪如果你沒有新的擋點，我就跑這四張。**

---

# 六、這一輪的問題清單

1. 5 個必修點修法有沒有問題？
2. **鮑伯的 `cut evenly at the jawline` 分配對嗎？**（第二節那兩個問題）
3. LG-07 拿掉吐舌後，這批完全沒有吐舌類表情，可以接受嗎？
4. 21 段裡還有沒有你會擋下來的？
5. 有沒有這一輪才出現的新問題？

---

# 七、修改後的 21 段全文

`model: soul_2`、`quality: 2k`、`aspect_ratio: 9:16`、一段 prompt 生一張。
🔬 = 這輪的 preflight 四張。


## Yuna Kim｜10 件

### YG-01｜咖啡廳靠窗・臉部近景

- 景別：臉部＋肩膀近景 ｜ 字數：102

```
A young woman tucks a strand of hair behind her ear and turns to look at the camera, one corner of her mouth lifted, head tilted toward that hand. Close-up of face and shoulders, camera at her eye level, lens horizontal. Collarbone-length soft wavy mocha brown hair with see-through wispy bangs. Cream fitted fine-knit tee, thin gold necklace, small gold hoops. Bright cafe window seat, white wall, pale wood table, a latte and her phone. Soft cool daylight from her front-left landing on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

### YG-02｜台北公寓窗邊晨光

- 景別：3/4 身（膝上） ｜ 字數：100

```
A young woman stands at the window holding a mug with both hands and lifts it to her mouth, eyes still narrowed from sleep, a loose easy smile. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. Collarbone-length mocha brown hair, sleep-mussed, see-through bangs flattened with one tuft sticking up. White fitted camisole, high-waisted grey cotton shorts, beige cardigan slipping off one shoulder, bare feet. Small bright apartment, white walls, pale wood floor, unmade white bed. Soft morning light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-03｜超商・「今天學到一個字」 🔬

- 景別：半身自拍 ｜ 字數：94

```
In a phone selfie, a young woman covers her mouth with her free hand, laughing with her eyes squeezed shut, the oden label board visible beside her. Half body, camera just above her eye level. Collarbone-length mocha brown hair in a low ponytail with see-through bangs and loose strands at her temples. Cropped grey tee, high-waisted black shorts, black-rimmed glasses. Taiwanese convenience store, fluorescent ceiling tubes, drinks fridge, steaming oden counter, snack shelves. Flat even fluorescent light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-04｜梳妝台護膚・素顏

- 景別：臉部＋上半身近景，拍鏡中反射 ｜ 字數：99

```
A young woman presses serum into her cheek with her fingertips, eyes closed, chin lifted, mouth relaxed into a small smile. Close-up of her face and shoulders reflected in the mirror, camera at her eye level, lens horizontal. Collarbone-length mocha brown hair clipped back with a claw clip, a few strands loose at her forehead. White fitted camisole. White marble bathroom counter, square mirror, white tiled wall, skincare bottles and brushes left unarranged. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

### YG-05｜捷運月台・隨手自拍

- 景別：半身自拍 ｜ 字數：86

```
A young woman looks into her phone camera while pushing her fringe aside with her free hand, lips softly pursed, a bored flat gaze. Half-body phone selfie, camera just above her eye level. Collarbone-length sleek straight mocha brown hair, side-parted. Fitted black short-sleeve knit, khaki high-waisted mini skirt, beige mini box bag. Metro platform, yellow safety line, platform screen doors, route map lightbox, ceiling tubes. Flat even station light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-06｜汗蒸幕・甜米露

- 景別：全身（坐姿） ｜ 字數：112

```
A young woman sits cross-legged on a heated wooden floor holding a paper cup of sweet rice punch with both hands in front of her chin, her eyes peeking over the rim toward the camera, crinkled into crescents. Full body, camera at her seated eye level, lens horizontal, shot from well back. Collarbone-length mocha brown hair gathered into a low bun with two damp strands at her temples. Grey jjimjilbang tee and shorts, a towel folded into sheep horns on her head, bare feet. Korean sauna rest hall, wooden floor, low tables. Warm ceiling light on her face, the warm room behind her keeping visible detail. Natural skin texture, subtle film grain.
```

### YG-07｜客廳地板・什麼都沒發生

- 景別：半身坐姿 ｜ 字數：103

```
A young woman sits on the living room floor scrolling her phone and reaching into a snack bag, caught mid-chew with one cheek full, eyebrows raised at the camera. Half body, camera level with her face as she sits on the floor, lens horizontal. Collarbone-length mocha brown hair, the top half clipped up and the lower half loose. Beige camisole, matching short cotton shorts, bare feet. Small apartment living room, low sofa, magazines open on the floor, an electric fan in the corner. Soft window light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-08｜台式早餐店・第一則吃

- 景別：半身，人＋食物同框 ｜ 字數：109

```
A young woman bites into an egg crepe and throws a thumbs up with her free hand, eyes crinkling into crescents, nose slightly scrunched. Half body with the food in frame, camera level with her chest, lens horizontal. Collarbone-length soft wavy mocha brown hair, side-parted, a small pearl clip on one side. Light blue shirt with the top two buttons open and the hem knotted at her waist, white high-waisted shorts. Taiwanese breakfast shop, stainless steel counter, red plastic chairs, handwritten wall menu, iced tea in a glass. Daylight from the doorway on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-09｜飯店窗邊・皮膚特寫

- 景別：臉部大特寫 ｜ 字數：94

```
A young woman leans against the window frame gazing out at the city, her eyes following something far outside the glass, lashes lowered, lips relaxed. Tight close-up of her face, camera at her eye level, lens horizontal. Wet mocha brown hair pushed straight back, collarbone-length, water still beading at the ends. White bathrobe with the collar loosened. Hotel room, white bedding, floor-to-ceiling window, city towers and a river blurred outside. Soft even daylight full on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

### YG-10｜百貨美妝櫃・精緻的一面

- 景別：半身 ｜ 字數：101

```
A young woman swatches lipstick on the back of her hand and holds the swatched hand beside her face, raising one eyebrow with one corner of her mouth lifted. Half body, camera level with her chest, lens horizontal. Sleek glossy mocha brown hair, side-parted, collarbone-length with the ends curving slightly inward. Cream cropped fitted knit top, matching off-white high-waisted straight trousers, a trench coat over her arm, gold hoop earrings. Department store beauty floor, glass counters, rows of lipsticks, mirrored columns. Even ceiling light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```


## Luna Tanaka｜11 件

### LG-01｜甜點店靠窗・臉部近景

- 景別：臉部＋肩膀近景 ｜ 字數：118

```
A young woman rests both elbows on the table and cups both cheeks in her palms, squishing her cheeks round, head tilted to one side, smiling toward the camera with her eyes. Close-up of face and shoulders, camera at her eye level, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, balanced evenly on both sides, centre-parted, ends curving slightly inward. Cream square-neck puff-sleeve top, small pearl earrings. Bright dessert shop window seat, white tiled wall, pale wood table, a strawberry cake and a latte on the table in front of her. Soft side daylight on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

### LG-02｜房間晨光・第一則「她在台北」

- 景別：3/4 身（膝上） ｜ 字數：106

```
A young woman crouches down with her fingertips resting on a sunlit patch of the floor, her other hand rubbing one eye, mouth caught mid-yawn. Three-quarter body, camera level with her face as she crouches, lens horizontal, shot from well back. A blunt chin-length black bob cut evenly at the jawline, sleep-mussed with one side flattened. White lace-trimmed camisole pyjama top, matching short pyjama shorts, bare feet. Bright clean studio room, white walls, pale wood floor, a small plant and a plush toy by the window. Soft morning light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-03｜Mochi 在台北的窗台

- 景別：半身＋貓同框 ｜ 字數：105

```
A young woman leans in close to an orange cat on the windowsill and scratches its head, her eyes crinkled shut in a smile, her attention entirely on the cat. Half body with the cat in frame, camera level with her face as she sits, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, one side tucked behind her ear. Off-white fitted fine-knit top, light shorts. Bedroom windowsill, small potted plants, an iron window grille and the apartment across the street outside. Soft window light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-04｜花季公園・櫻花 🔬

- 景別：半身 ｜ 字數：109

```
A young woman holds one open palm in front of her with a blossom petal resting in it, eyes widened and mouth softly open in surprise, eyebrows raised. Half body, camera level with her chest, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, balanced evenly on both sides, a cream ribbon headband. White square-neck fitted lace top, pale pink checked mini skirt, a cream cardigan over her shoulders, pearl earrings. Park path under blossoming branches hanging into the top of the frame, petals on her shoulder. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-05｜公車站・雨停前 🔬

- 景別：3/4 身（膝上） ｜ 字數：118

```
A young woman stands at the edge of a bus shelter holding a folded clear umbrella still dripping, tilting her head and making a V sign beside her cheek, eyes crinkled. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. A blunt chin-length black bob cut evenly at the jawline, balanced evenly on both sides. Pale blue checked skirt, a pale blue cardigan over her shoulders, an off-white fitted shirt with the top buttons open. Bus shelter with a colourful route map lightbox, raindrops on the glass, wet asphalt reflecting the glow of shop signs across the street. Her face clearly lit, the glowing signs keeping their colour. Natural skin texture, subtle film grain.
```

### LG-06｜可愛系街區・扭蛋機前

- 景別：半身 ｜ 字數：108

```
A young woman holds an opened gachapon capsule in both hands at chest level, looking down at it and laughing with her eyes squeezed shut. Half body, camera level with her chest, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, balanced evenly on both sides, two small clips holding her fringe back. Pale pink cropped knit top showing a sliver of waist, white high-waisted shorts, a denim jacket tied at her waist. A row of colourful gachapon machines behind her, bright shop signage, clean pavement. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-07｜遊樂園・旋轉木馬

- 景別：全身 ｜ 字數：114

```
A young woman hugs a popcorn bucket up under her chin, her hips and torso facing away from the camera while her head and shoulders turn back over one shoulder, her eyes peeking over the rim toward the camera with a playful smile. Full body, camera at her navel level, lens horizontal, shot from well back. A blunt chin-length black bob cut evenly at the jawline, a cat-ear headband. White square-neck puff-sleeve top, pale blue pinafore skirt, white mary janes with lace socks. Amusement park beside the carousel, coloured balloons, a decorated parade street behind. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-08｜浴室鏡前・濕髮

- 景別：半身，拍鏡中反射 ｜ 字數：106

```
A young woman stops drying her hair and bites one corner of the towel between her teeth while looking at herself in the mirror, cheeks puffed out. Half body reflected in the mirror, camera at her eye level, lens horizontal. A wet blunt chin-length black bob cut evenly at the jawline, clinging to her cheeks. A white bath towel wrapped around her. Clean bright bathroom, white square tiles, a wooden-framed mirror with a little steam at one corner, skincare bottles on the counter. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-09｜台式早餐店・豆漿

- 景別：半身，人＋食物同框 ｜ 字數：113

```
A young woman holds a glass of soy milk with both hands in front of her chin, head slightly lowered, eyes looking up over the rim toward the camera, smiling with her eyes. Half body with the food in frame, camera at her eye level or slightly above, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, balanced evenly on both sides, centre-parted and worn loose. Cream fitted thin-knit short sleeve, a light mini skirt. Taiwanese breakfast shop, stainless steel counter, a metal tray, handwritten wall menu, plastic chairs. Daylight from the doorway on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-10A｜浴衣・祭典參道（全身） 🔬

- 景別：全身 ｜ 字數：115

```
A young woman stands on the festival approach with her hips and torso facing down the path, her head and shoulders turned back toward the camera, holding a candy apple beside her cheek, laughing with her eyes crinkled. Full body, camera at her navel level, lens horizontal, shot from well back. A blunt chin-length black bob cut evenly at the jawline, half-pinned up with a Japanese hairpin. Pale blue yukata with a white morning-glory print, a navy half-width obi tied tight at the waist, wooden geta. A clean bright wooden torii, paper lanterns strung overhead, food stalls. Her face clearly lit, the lantern-lit stalls behind her keeping visible detail. Natural skin texture, subtle film grain.
```

### LG-10B｜浴衣・蘋果糖（半身）

- 景別：半身 ｜ 字數：105

```
A young woman holds a candy apple up beside her cheek with one hand and steadies the Japanese hairpin in her half-up bob with the other, laughing with her eyes crinkled. Half body, camera level with her chest, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, half-pinned up with a Japanese hairpin, two strands left at her temples. Pale blue yukata with a white morning-glory print, a navy half-width obi tied tight at the waist. Paper lanterns strung overhead behind her, a blurred food stall. Her face clearly lit, the lantern-lit background keeping visible detail. Natural skin texture, subtle film grain.
```

---

# 八、附錄：已花錢驗證過的基準線（不必再討論）

不寫族裔與身材數字 ✅ 6/6｜相對機位描述 ✅ 6/6｜否定句無效（實測）｜
`background exposed the same brightness as her skin` 在 3 張室內圖解掉逆光（**validated baseline wording，非萬用公式**）｜
表情必須綁實體動作（比 V ✅／捧杯遮嘴 ✅／回眸一笑 ❌／單眼瞇起 ❌）｜
身體姿勢做得出來、純臉部表情做不出來｜`soul_id` 會鎖住整套場景模板｜
抽象的「正在飄」3/3 失敗｜沒寫髮長會生出長短不一的頭髮
