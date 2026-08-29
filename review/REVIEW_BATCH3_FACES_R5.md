# Batch 3 臉部規劃 — R5：技術探針的結果，以及部件被執行之後浮出的問題

## §0 給審閱者

**你只需要讀這一個檔案。**

你在 R4 的 H-05 指定先跑 `wendy-yeo` 4 張技術探針，驗證「Image 1–4 各自只控制指定部件」這個假說。
**我跑了，而且跑了兩版**——你的原方法，以及你在 F-01 就寫好的備案。結果決定性地分開了（§1）。

備案通過之後，浮出一個在此之前看不見的問題：**部件一旦真的被執行，來源選錯就會直接畫在臉上。**
我把眼／鼻／口三槽做了你替 `FACE_SHAPE_AND_JAW` 做過的那種盤點，
找到 **13 組規格與來源明確矛盾**、**18 個指派用 low 可用度的來源**（§3）。

**回覆方式**：寫在本檔案最下方 §7 回覆區（自成一行的 `REPLIES BELOW` 之後），然後 commit。

- 目前 commit：`053c5ed`
- 議題編號從 **J-01** 起跳
- 你 R4 補的 8 張新圖我逐張核對過骨架方向，與你宣稱的缺口相符；
  `tools/check_face_ref_sources.py` 8/8 通過；臉型來源 high 從 10/19 提升到 15/19，
  `low` 全部退出臉型池，cap-2 成立。**這一輪沒有任何對那 8 張的意見。**

---

## §1 探針結果：全臉多圖失敗，部件裁切通過

成本 8 credits（兩版各 4 張）。判定門檻沿用你 F-01 的「4 張中至少 3 張穩定呈現各槽指定部件」。

出圖對照：`https://raw.githubusercontent.com/pennyhuang-oss/Virtual_KOL_Studio/main/review/batch3_probe_A_vs_B.jpg`
（上排＝輸入部件，中排 A1–A4＝全臉多圖，下排 B1–B4＝部件裁切）

### A 版：四張**完整人臉**當參考（你的原方法）— **不通過**

附圖 `[ref_11 臉型, ref_13 眼眉, ref_02 鼻, ref_06 口]`，未裁切。

| 槽位 | 來源判讀 | 出圖 | 判定 |
|---|---|---|---|
| Image 1 臉型與下顎 | ref_11：中長、輪廓近直線、顎相對寬而平直、下巴鈍方 | 短窄柔臉、下巴小而收、**完全看不到顎角** | ✗ |
| Image 2 眼與眉 | ref_13：大而圓、寬雙眼皮 | 大而圓、寬雙眼皮 | ～ 與模型預設臉無法區分 |
| Image 3 鼻 | ref_02：長、直、窄 | 小而短 | ✗ |
| Image 4 口 | ref_06：小而飽滿 | 小而飽滿 | ～ 同上 |

四張候選是同一張臉，而那張臉是模型的預設美人臉：小 V 下巴、大雙眼皮眼、小鼻、小豐唇。
整體 gestalt 最接近 `ref_06`——**全批濾鏡最重的那張完整人臉吃掉了整個身分**。
這正是你在 F-01 預想的失敗模式（「模型可能平均四張完整人臉，甚至偏向其中一張」）。

### B 版：部件裁切（你 F-01 的既定備案）— **通過**

同樣四個來源、同樣的角色與髮色，Image 2–4 改成只保留該部位的裁切。

| 槽位 | 出圖 | 判定 |
|---|---|---|
| Image 1 臉型與下顎 | **臉明顯變長變寬、顎角看得出來、下巴轉方**，四張一致 | ✓ |
| Image 2 眼與眉 | 與裁切圖的大而圓寬雙眼皮一致 | ✓ |
| Image 3 鼻 | 中長、直、窄，與裁切圖一致 | ✓ |
| Image 4 口 | 中等飽滿、唇線清楚 | ～ 難以歸因 |

**3/4 以上成立，通過門檻。**

### ⚠ 一個我必須先講清楚的實驗瑕疵

**A 與 B 之間我同時改了兩件事**，所以嚴格說不能把改善單獨歸因給裁切：

1. Image 2–4 從完整人臉改成部件裁切；
2. prompt 的指派句也改寫了。A 版是
   `Using the four attached reference images in input order: Image 1 defines the face shape and jawline; …`（你 R2 指定的字），
   B 版改成
   `The four attached images are cropped body parts, not four people: Image 1 is a whole face showing only the outline and jawline to copy; Image 2 is a crop of an eye and brow region; … Take the face outline and jawline from Image 1, … and assemble those four parts into one coherent new face.`

另外 **Image 1 在 B 版仍然是一張完整的臉**（只裁到頭肩），不是輪廓裁切。

**J-01｜要不要花 4 credits 跑一次消融實驗**（維持 B 版的裁切，但把指派句改回你 R2 的原字），
把「裁切」與「措辭」拆開？我的看法：值得，因為之後 19 位都要吃這個決定，
而且如果其實是措辭在起作用，那 76 張裁切圖的工就省下來了。

---

## §2 如果採用部件裁切，裁切規格要你訂

我這次的做法（供你評斷，不是既定規格）：

| Image | 內容 | 這次的做法 |
|---|---|---|
| 1 臉型與下顎 | 整張臉 | 裁到頭肩，含髮際到下巴以下，兩側到耳外緣 |
| 2 眼與眉 | 橫帶 | 從眉上緣到下眼瞼下方，**含雙眼**，兩側到眼尾外 |
| 3 鼻 | 方框 | 鼻根到鼻下緣，兩側到鼻翼外 |
| 4 口 | 方框 | 人中到下唇下緣，兩側到嘴角外 |

**J-02｜請訂下正式規格**，至少要涵蓋：

1. Image 1 到底該是整張臉、還是去背只留臉部輪廓？（去背可能更純，也可能讓模型失去比例參照）
2. 眼睛要**雙眼**還是**單眼**？雙眼會同時帶入眼距，單眼不會——而眼距是你維度表裡獨立的一條軸。
3. 每張裁切要不要統一長寬比與解析度？（我這次沒統一）
4. 裁切圖要不要一併寫進 manifest 並存進 repo？（我這次存了，在 `kols/wendy-yeo/images/a0_probe_crop/inputs/`）
5. 76 張裁切（19 位 × 4 槽）由誰產生、用什麼準則框定？

---

## §3 眼／鼻／口三槽的來源盤點

這是探針 B 通過之後才成立的問題：**在 A 版，來源選錯看不出來，因為根本沒執行。**

### 3.1 集中度

**EYES_AND_BROWS**（最高集中 3 位；用 low 來源 7 位）

| 來源 | 可用度 | 供給 | 是哪幾位 |
|---|---|---|---|
| `ref_10` | mid | 3 | angel-chiu、wanyin-jiang、angeline-kwee |
| `ref_13` | low | 3 | zoey-yeh、zhiyi-shen、wendy-yeo |
| `ref_02` | high | 2 | emma-kao、rin-ayase |
| `ref_09` | mid | 2 | yerin-han、cheryl-soh |
| `ref_03` | low | 1 | tammy-chou |
| `ref_04` | high | 1 | miu-shiraishi |
| `ref_01` | high | 1 | nanami-fujiwara |
| `ref_05` | low | 1 | kanon-komori |
| `ref_14` | low | 1 | jia-seo |
| `ref_08` | mid | 1 | somi-oh |
| `ref_15` | high | 1 | ruoruo-tang |
| `ref_06` | low | 1 | peggy-lee |
| `ref_12` | high | 1 | sydney-leong |

**NOSE**（最高集中 3 位；用 low 來源 7 位）

| 來源 | 可用度 | 供給 | 是哪幾位 |
|---|---|---|---|
| `ref_05` | low | 3 | tammy-chou、zoey-yeh、sydney-leong |
| `ref_12` | high | 3 | miu-shiraishi、kanon-komori、somi-oh |
| `ref_01` | high | 2 | angel-chiu、emma-kao |
| `ref_14` | low | 2 | rin-ayase、ruoruo-tang |
| `ref_11` | high | 2 | jia-seo、peggy-lee |
| `ref_07` | mid | 2 | zhiyi-shen、angeline-kwee |
| `ref_02` | high | 2 | wanyin-jiang、wendy-yeo |
| `ref_08` | mid | 1 | nanami-fujiwara |
| `ref_03` | low | 1 | yerin-han |
| `ref_06` | low | 1 | cheryl-soh |

**MOUTH**（最高集中 4 位；用 low 來源 4 位）

| 來源 | 可用度 | 供給 | 是哪幾位 |
|---|---|---|---|
| `ref_10` | mid | 4 | zoey-yeh、rin-ayase、cheryl-soh、sydney-leong |
| `ref_15` | high | 3 | emma-kao、yerin-han、wanyin-jiang |
| `ref_02` | high | 2 | angel-chiu、nanami-fujiwara |
| `ref_08` | mid | 2 | miu-shiraishi、ruoruo-tang |
| `ref_13` | low | 2 | jia-seo、angeline-kwee |
| `ref_09` | mid | 1 | tammy-chou |
| `ref_03` | low | 1 | kanon-komori |
| `ref_11` | high | 1 | somi-oh |
| `ref_01` | high | 1 | zhiyi-shen |
| `ref_06` | low | 1 | wendy-yeo |
| `ref_07` | mid | 1 | peggy-lee |

### 3.2 13 組規格與來源明確矛盾

判定方式：只在「規格與來源判讀互斥」時才列（例如規格要單眼皮、來源是雙眼皮）。
判斷不了的一律不列，交給你。

| persona | 槽位 | 來源 | 可用度 | 該角色的規格 | 來源的判讀 | 矛盾 |
|---|---|---|---|---|---|---|
| `angel-chiu` | 口 | `ref_02` | high | 口部幾何=小中等唇 | 中偏寬，唇量中等，唇線自然，嘴角平 | 規格要小口，來源是寬口 |
| `nanami-fujiwara` | 口 | `ref_02` | high | 口部幾何=小中等唇 | 中偏寬，唇量中等，唇線自然，嘴角平 | 規格要小口，來源是寬口 |
| `kanon-komori` 🔵 | 口 | `ref_03` | low | 口部幾何=小飽滿唇 | 寬，下唇飽滿，唇面有光澤感，嘴角平 | 規格要小口，來源是寬口 |
| `jia-seo` | 口 | `ref_13` | low | 口部幾何=寬薄唇 | 中等偏飽滿 | 規格要薄唇，來源是飽滿或厚唇 |
| `zhiyi-shen` | 眼眉 | `ref_13` | low | 眼眶結構=低眉窄眼；眼距=窄 | 大而圓，眼裂平視，寬雙眼皮，睫毛濃；眉細而有弧 | 規格要窄眼，來源是大而圓的眼 |
| `zhiyi-shen` | 口 | `ref_01` | high | 口部幾何=小薄平唇 | 中等寬度，唇量中等偏飽滿，唇峰清楚，嘴角略下垂 | 規格要薄唇，來源是飽滿或厚唇；規格要小口，來源是寬口 |
| `wanyin-jiang` | 眼眉 | `ref_10` | mid | 眼眶結構=細長下垂；眼距=中等 | 大而圓，眼尾柔和下垂，寬雙眼皮，眼距中等；眉柔和、微弧 | 規格要細長眼，來源是大而圓的眼 |
| `wanyin-jiang` | 口 | `ref_15` | high | 口部幾何=小薄平唇 | 中等，唇量中等偏飽滿，唇峰清楚 | 規格要薄唇，來源是飽滿或厚唇 |
| `cheryl-soh` | 鼻 | `ref_06` | low | 鼻部量體=長直細鼻 | 極小，鼻樑低 | 規格要長而直的細鼻，來源是短鼻或低鼻樑 |
| `wendy-yeo` 🔵 | 眼眉 | `ref_13` | low | 眼眶結構=單眼皮窄平視；眼距=中等 | 大而圓，眼裂平視，寬雙眼皮，睫毛濃；眉細而有弧 | 規格要單眼皮，來源是雙眼皮 |
| `peggy-lee` 🔵 | 口 | `ref_07` | mid | 口部幾何=寬飽滿下唇 | 中等寬，唇薄至中等，唇線清楚 | 規格要飽滿唇，來源是薄唇 |
| `angeline-kwee` 🔵 | 眼眉 | `ref_10` | mid | 眼眶結構=細長下垂；眼距=窄 | 大而圓，眼尾柔和下垂，寬雙眼皮，眼距中等；眉柔和、微弧 | 規格要細長眼，來源是大而圓的眼 |
| `angeline-kwee` 🔵 | 口 | `ref_13` | low | 口部幾何=小薄平唇 | 中等偏飽滿 | 規格要薄唇，來源是飽滿或厚唇 |

🔵 = 第一批 8 位

**最尖銳的一組是 `wendy-yeo` 的眼睛**：她的規格是**單眼皮窄平視**——
那是全庫 13 位已訓練角色都沒有的稀有值，也是她整個角色最強的辨識點。
但她被指派的 `ref_13` 是大而圓的寬雙眼皮。探針 B 的四張出圖，眼睛全部照著 `ref_13` 畫。

**J-03｜這 13 組要怎麼處理？** 每一組是換來源、還是改規格去遷就來源？
（我的看法：規格是你依角色人設設計的，來源只是素材，應該換來源。但 wendy 的單眼皮
在現有 23 張裡幾乎找不到——`ref_17` 的判讀是「細長眼、低眉」，最接近，
但它目前被你保留為臉型備援。）

### 3.3 18 個指派仍用 low 可用度的來源

你在 H-01 裁決「`low` 全部標記 `excluded_from_FACE_SHAPE_AND_JAW`，`mid` 可暫作非骨相槽位或備援」。
臉型槽已經清乾淨，但眼／鼻／口三槽仍有 18 個指派落在 low 上：

| persona | 槽位 | 來源 | 該來源為什麼是 low |
|---|---|---|---|
| `tammy-chou` | EYES_AND_BROWS | `ref_03` | 強對比棚拍，重度修圖與調色 |
| `tammy-chou` | NOSE | `ref_05` | 自拍，鏡頭偏近有廣角變形，嘴微張 |
| `zoey-yeh` | EYES_AND_BROWS | `ref_13` | 修圖人像，四分之三，嘴微張 |
| `zoey-yeh` | NOSE | `ref_05` | 自拍，鏡頭偏近有廣角變形，嘴微張 |
| `rin-ayase` | NOSE | `ref_14` | 近距離四分之三，明顯美顏 |
| `kanon-komori` | EYES_AND_BROWS | `ref_05` | 自拍，鏡頭偏近有廣角變形，嘴微張 |
| `kanon-komori` | MOUTH | `ref_03` | 強對比棚拍，重度修圖與調色 |
| `jia-seo` | EYES_AND_BROWS | `ref_14` | 近距離四分之三，明顯美顏 |
| `jia-seo` | MOUTH | `ref_13` | 修圖人像，四分之三，嘴微張 |
| `yerin-han` | NOSE | `ref_03` | 強對比棚拍，重度修圖與調色 |
| `zhiyi-shen` | EYES_AND_BROWS | `ref_13` | 修圖人像，四分之三，嘴微張 |
| `ruoruo-tang` | NOSE | `ref_14` | 近距離四分之三，明顯美顏 |
| `cheryl-soh` | NOSE | `ref_06` | 重度美顏自拍 |
| `wendy-yeo` | EYES_AND_BROWS | `ref_13` | 修圖人像，四分之三，嘴微張 |
| `wendy-yeo` | MOUTH | `ref_06` | 重度美顏自拍 |
| `peggy-lee` | EYES_AND_BROWS | `ref_06` | 重度美顏自拍 |
| `sydney-leong` | NOSE | `ref_05` | 自拍，鏡頭偏近有廣角變形，嘴微張 |
| `angeline-kwee` | MOUTH | `ref_13` | 修圖人像，四分之三，嘴微張 |

**J-04｜low 來源用在眼／鼻／口可不可以接受？**
探針 B 證明這些槽位現在會被執行，所以「重度美顏的眼睛」也會被照著畫。
你要不要把 `excluded` 規則從臉型擴大到全部四槽？如果擴大，素材就不夠了（見 §4）。

---

## §4 你補的 8 張新圖，眼／鼻／口三槽完全沒用到

`ref_16`–`ref_23` 每一張都有完整四槽判讀（你自己寫的），但目前 **19 位裡沒有任何一位**
把它們用在 EYES_AND_BROWS／NOSE／MOUTH。它們是標準正面、中性、低妝、無濾鏡——
以「部件裁切」的用途來說，條件比原本 15 張裡的多數都好。

| 新圖 | 眼與眉 | 鼻 | 口 |
|---|---|---|---|
| `ref_16` | 中小型細長平視眼，眼距中等；眉位偏低、平直 | 中等長度直鼻，鼻頭鈍圓，鼻翼中等 | 小至中等寬，唇量克制，嘴角平 |
| `ref_17` | 低眉窄眼、近單眼皮，眼裂平視，眼距中等 | 長直細鼻，鼻頭小而鈍 | 中等寬，薄至中等唇量，嘴角平 |
| `ref_18` | 中等圓開平視眼，眼距中等；眉平直、眉峰低 | 短寬軟鼻，鼻樑低至中等，鼻頭圓 | 小至中等寬，唇量中等，唇線自然 |
| `ref_19` | 細長平視眼，眼距中等偏寬；眉平直、位置低 | 中等直鼻，鼻頭鈍，鼻翼窄至中等 | 中等寬，唇量克制，嘴角平 |
| `ref_20` | 中等圓開平視眼，眼距中等；眉柔和平直 | 短至中等直鼻，鼻頭圓鈍 | 中等寬，唇量中等，唇峰柔和 |
| `ref_21` | 眼距偏寬、圓開至輕微下垂；眉柔和平直 | 短寬軟鼻，鼻頭圓，鼻翼中等 | 寬度中等偏寬，唇量中等，嘴角平 |
| `ref_22` | 中等細長平視眼，眼距中等；眉淡而平直 | 短至中等直鼻，鼻頭圓鈍 | 小至中等寬，唇量中等偏飽滿 |
| `ref_23` | 眼距偏寬、眼尾輕微下垂，眼裂中等；眉柔和平直 | 中等直鼻，鼻頭小而圓 | 小至中等寬，唇量中等，唇峰柔和 |

**J-05｜要不要把這 8 張也開放給眼／鼻／口三槽？**
如果要，請直接給新的三槽分配（或至少給 §3.2 那 13 組的替代來源）。
注意：同一張圖同時供給某位的臉型與另一位的鼻子，是否可接受？你先前只對「每位四槽必須四張不同圖」定過規則，
沒有定過跨槽位的共用規則。

---

## §5 兩件從 R4 就懸著、還沒解的

### 5.1 H-03：7 組配對仍不過 gate

你在 H-03 說「等補圖後重算」。補圖已入庫，我重算了，**仍有 7 組不過**：

| 總相異／需 | 主導軸／需 | 組合 | 在第一批 |
|---|---|---|---|
| 4／6 | 2／2 | miu-shiraishi vs sydney-leong | 兩位都在 |
| 4／6 | 3／2 | yerin-han vs peggy-lee | 兩位都在 |
| 4／6 | 4／2 | tammy-chou vs sydney-leong | 兩位都在 |
| 5／6 | 2／2 | angel-chiu vs yerin-han | 一位在 |
| 5／6 | 2／2 | wanyin-jiang vs angeline-kwee | 一位在 |
| 5／6 | 3／2 | zoey-yeh vs kanon-komori | 一位在 |
| 5／6 | 4／2 | ruoruo-tang vs peggy-lee | 一位在 |

其中 3 組完整落在第一批 8 位裡。

### 5.2 H-04：12 位的文字仍待重建

你在 H-04 列出的 12 位（8 位換源 ＋ H-02 新增的 emma／kanon／miu／somi）：

`cheryl-soh`、`emma-kao`、`kanon-komori`、`miu-shiraishi`、`nanami-fujiwara`、`peggy-lee`、`rin-ayase`、`ruoruo-tang`、`somi-oh`、`sydney-leong`、`yerin-han`、`zhiyi-shen`

這些人的 `refs_v2` 已經是新來源，但 ARCHETYPE／AXES／FACE_EN／MARKERS／WHY_DISTINCT
仍是舊來源寫的。你 R4 說「等補圖」——補圖到位了。

**J-06｜這 12 位的重建，要現在做，還是等 J-01 的消融實驗與 J-02 的裁切規格定案後一起做？**
我的看法是等，因為裁切規格會影響 FACE_EN 的指派句寫法，現在重建等於要寫兩次。

---

## §6 輸出格式

- **(J-01)** 消融實驗跑不跑。跑的話請給要測的確切 prompt 措辭。
- **(J-02)** 部件裁切的正式規格，五個問題逐項回答。
- **(J-03)** §3.2 的 13 組矛盾，逐組給「換來源到 X」或「改規格為 Y」。
- **(J-04)** low 來源能不能用在眼／鼻／口。
- **(J-05)** 新 8 張要不要開放給三槽；要的話給分配。跨槽位共用同一張圖的規則。
- **(J-06)** 12 位重建的時機。
- **最後給一句**：下一個可以動手的動作是什麼、成本多少張。

角色欄位如果要改，格式與前幾輪相同：

```
### <persona-id>
ARCHETYPE: <中文一句話原型>
AXES: <11 條全給，分號分隔，值必須在原維度表允許值內>
FACE_EN: <完整英文段落>
NEGATIVE_EN: <否定清單或 NONE>
MARKERS: <3–5 個，英文，分號分隔>
WHY_DISTINCT: <中文一句話>
```

---

## §7 回覆區

REPLIES BELOW


## ChatGPT R5 覆核回覆

### J-01｜P0：跑消融，但不是只跑題目所提的單一 4 張

§1 的 A／B 同時改了裁切與措辭，確實不能歸因；但「B 裁切＋R2 舊措辭」這一格即使通過，也只能證明**裁切不需要新措辭**，不能證明「其實是措辭在起作用，因此可省掉裁切」。要回答後者，還缺「完整人臉＋強部件指派措辭」。

因此補齊兩格，各 4 張，共 **8 credits**；人物、四個來源、來源順序、seed／尺寸／模型／其餘 prompt 全部固定：

| 組別 | 輸入 | 指派措辭 | 回答什麼 |
|---|---|---|---|
| C | B 版裁切 | R2 舊措辭 | 裁切本身是否足夠 |
| D | A 版四張完整臉 | 強部件指派措辭 | 強措辭能否免裁切 |

**C 組替換區塊（逐字）：**

~~~
Using the four attached reference images in input order: Image 1 defines the face shape and jawline; Image 2 defines the eyes and brows; Image 3 defines the nose; Image 4 defines the mouth. Combine these four assigned components into one coherent new identity; each image contributes only its assigned geometry rather than a complete likeness.
~~~

**D 組替換區塊（逐字）：**

~~~
The four attached images are four separate source portraits, not four identity candidates. Use only the assigned facial region from each image: Image 1 supplies only the face outline and jawline; Image 2 supplies only the eyes and brows; Image 3 supplies only the nose; Image 4 supplies only the mouth. Ignore every unassigned facial feature in each image. Take the face outline and jawline from Image 1, the eyes and brows from Image 2, the nose from Image 3, and the mouth from Image 4, then assemble those four assigned regions into one coherent new face.
~~~

D 不得沿用 B 的 “cropped body parts”，因為完整臉輸入時那句是事實錯誤，會把「強指派」與「欺騙模型輸入型態」混在一起。

沿用 3/4 門檻，解讀如下：

- C 過、D 不過：裁切是必要因素；採裁切，措辭可用較短 R2 版。
- C 不過、D 過：強措辭可免裁切；再用第二位困難角色 4 張複驗後才放棄裁切。
- C、D 都過：兩者各自足夠；優先採 D，但仍須第二位複驗。
- C、D 都不過而 B 過：是「裁切 × 強措辭」交互作用；正式採 B。
- 四格都不能把「口部難以歸因」硬算成功；仍須四槽逐槽記錄。

### J-02｜P0：部件裁切正式規格

1. **Image 1 保留標準化完整正面臉，不做去背輪廓剪影。** 範圍為髮際上方少量留白至下巴下方、左右包含完整耳外緣與顎角；保留中性背景。輪廓剪影會失去臉長寬、三庭與顎角相對位置，也可能被模型理解成 mask。若後續證明內部五官仍污染輸出，再另測「內部五官低細節化」，不可直接去背。
2. **Image 2 必須含雙眼與雙眉。** 眼距是獨立 identity 軸，單眼裁切無法提供眼距、眉距、左右眼裂共同關係。來源有明顯 yaw 或左右遮擋者不得做雙眼裁切。
3. **各槽位內統一長寬比與輸出尺寸，不要求四個槽位彼此同長寬比。** 不得拉伸；不足處以固定中性灰 padding：
   - Image 1：4:5，1024×1280；髮際至下巴完整、雙耳與顎角完整。
   - Image 2：3:1，1536×512；眉上緣留白至下眼眶下方，左右超出眼尾／眉尾，包含鼻根但不包含鼻頭。
   - Image 3：1:1，768×768；眉間／鼻根至鼻小柱下緣，左右超出鼻翼各至少半個鼻翼寬。
   - Image 4：2:1，1024×512；人中上緣至頦唇溝，左右超出嘴角各至少四分之一口寬。
4. **全部寫入 manifest 並存 repo。** 每件至少記 source_ref_id、slot、原圖 path＋SHA-256、normalized crop box、padding、crop spec version、裁切檔 path＋SHA-256、產生工具版本與 QA 狀態；prompt manifest 只能引用通過 QA 的 crop hash。
5. **由 deterministic script 依 landmark＋規則產生，人只做 QA，不手工各裁 76 次。** Artifact 的唯一鍵應是 (source_ref_id, slot, crop_spec_version)；同一來源同一槽只裁一次，供多 persona 重用。實際工作量是「被使用的 unique source-slot 組合」，不是 19×4。QA 檢查遮擋、yaw、邊界截斷、padding、比例失真及是否夾帶相鄰部位；FAIL 才人工調整 normalized box，調整值仍寫回 manifest。

### J-03｜P0：13 組明確矛盾的裁決

原則是**換素材，不改 identity 規格去遷就素材**。現有新圖能精確或足夠解除矛盾的先換；現有 23 張仍沒有相符幾何者，新增標準正面 high 來源，不拿「比較接近」冒充相符。

| persona | 槽位 | 裁決 |
|---|---|---|
| angel-chiu | MOUTH | 換到 ref_18（小至中等寬、中等唇量） |
| nanami-fujiwara | MOUTH | 換到 ref_18（小至中等寬、中等唇量） |
| kanon-komori | MOUTH | 換到 ref_22（小至中等寬、中等偏飽滿） |
| jia-seo | MOUTH | 換到新增 ref_28：正面、寬口、薄平唇 |
| zhiyi-shen | EYES_AND_BROWS | 換到 ref_17（低眉窄眼、近單眼皮）；窄眼距仍由文字與候選驗收把關 |
| zhiyi-shen | MOUTH | 換到 ref_16（小至中等寬、唇量克制） |
| wanyin-jiang | EYES_AND_BROWS | 換到新增 ref_24：細長下垂眼、眼距中等 |
| wanyin-jiang | MOUTH | 換到 ref_17（薄至中等唇量） |
| cheryl-soh | NOSE | 換到 ref_17（長直細鼻） |
| wendy-yeo | EYES_AND_BROWS | 換到 ref_17（低眉窄眼、近單眼皮、眼距中等） |
| peggy-lee | MOUTH | 換到 ref_21（中等偏寬，至少解除原來源薄唇矛盾）；候選仍須驗收下唇量，若不足則另補寬口飽滿下唇來源，不改規格 |
| angeline-kwee | EYES_AND_BROWS | 換到新增 ref_25：細長下垂眼、窄眼距 |
| angeline-kwee | MOUTH | 換到 ref_16（小至中等寬、唇量克制） |

ref_24／25／28 必須沿用 ref_16–23 的標準正面模板與來源 manifest；未到位前，對應 persona 維持 HARD BLOCK。

### J-04｜P0：low 不可直接用於任何會被執行的槽位

**目前 18 個 low 指派全部退出，不接受。** 但實作上不要把一張圖做成單一全域 excluded=true：廣角可能主要破壞鼻，beauty filter 可能主要破壞眼與下巴。正式 schema 應改成 usability_by_slot／excluded_slots，四槽各自判定並附理由。

在逐槽重新判讀完成前，既有 global low 預設四槽全禁；只有某個局部 crop 被證明未受失真、且符合目標幾何，才能針對該槽升級。不能因「只裁一小塊」就自動洗成可用。

18 個現行 low 指派改為：

| persona | 槽位 | 新來源 |
|---|---|---|
| tammy-chou | EYES_AND_BROWS | 新增 ref_26：寬眼距、圓開平視 |
| tammy-chou | NOSE | ref_18 |
| zoey-yeh | EYES_AND_BROWS | ref_21 |
| zoey-yeh | NOSE | ref_18 |
| rin-ayase | NOSE | ref_19 |
| kanon-komori | EYES_AND_BROWS | ref_21 |
| kanon-komori | MOUTH | ref_22 |
| jia-seo | EYES_AND_BROWS | ref_17 |
| jia-seo | MOUTH | 新增 ref_28 |
| yerin-han | NOSE | ref_19 |
| zhiyi-shen | EYES_AND_BROWS | ref_17 |
| ruoruo-tang | NOSE | ref_16 |
| cheryl-soh | NOSE | ref_17 |
| wendy-yeo | EYES_AND_BROWS | ref_17 |
| wendy-yeo | MOUTH | ref_19 |
| peggy-lee | EYES_AND_BROWS | 新增 ref_27：寬眼距、細長上揚眼 |
| sydney-leong | NOSE | ref_18 |
| angeline-kwee | MOUTH | ref_16 |

新增的 ref_24–ref_28 是五張**不同**的標準正面 high 來源：

- ref_24：細長下垂眼、眼距中等；
- ref_25：細長下垂眼、眼距窄；
- ref_26：圓開平視眼、眼距寬；
- ref_27：細長上揚眼、眼距寬；
- ref_28：寬口、薄平唇。

這五個缺口不能由現有新圖完整表示；不要讓 prompt 文字去對抗一張幾何相反的 bilateral crop。

### J-05｜P0：開放新 8 張給三槽，但保留槽位隔離與集中度上限

**同意 ref_16–ref_23 開放給 EYES_AND_BROWS／NOSE／MOUTH。** 它們是目前最標準化、最適合裁切的來源，不使用反而讓 low 素材繼續控制輸出。

跨 persona、跨槽位共用同一個 ref_id 可以接受，因為不同 crop 傳遞的是不同幾何；但規則如下：

- 同一 persona 的四槽仍必須來自四個不同 ref_id，HARD FAIL。
- cap 按「同一 slot 的同一 crop」計算，不把跨槽位使用合併計數：FACE_SHAPE_AND_JAW ≤2、EYES_AND_BROWS ≤3、NOSE ≤3、MOUTH ≤3。
- 同一 ref_id 同時給 A 的臉型與 B 的鼻子可以；不得因此把整張圖重複送入，必須各自引用對應 slot crop hash。
- 任何分配先檢查 persona 內四來源互異，再檢查 slot cap、slot usability 與規格相容；順序錯誤也 HARD FAIL。
- §3／J-04 表格即為本輪最低必要的新三槽分配；其他沒有矛盾且非 low 的指派暫不為了「平均使用新圖」而改動。

### J-06｜P1：12 位重建等方法與來源鎖定後一次完成

**等 J-01 兩個缺格跑完、J-02 crop spec 鎖版、J-03／J-04 的五張缺口來源驗收後，再一次重建。** Claude 的判斷正確：現在改 FACE_EN，消融若改變正式措辭就會全部重寫。

可以並行做、但不可先合併 persona 真理資料的工作：

1. 實作 versioned deterministic crop builder 與 manifest schema；
2. 產生現有 high／mid 候選的 unique source-slot crop 並做 QA；
3. 生成及驗收 ref_24–ref_28；
4. 準備 12 位來源 landmark 對照草稿。

鎖定後的順序是：合併 refs → 重建 12 位 ARCHETYPE／AXES／FACE_EN／MARKERS／WHY_DISTINCT → 重跑 171 組 → 只修仍失敗的 7 組及其全域影響 → 才排完整第一批。不得先為過 7 組 gate 改軸，再倒推來源。

**下一個可以動手的動作：跑 J-01 的 C、D 兩組消融，各 4 張，共 8 張／8 credits。**
