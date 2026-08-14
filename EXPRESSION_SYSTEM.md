# Virtual KOL Studio — Expression System（表情系統）

> 2026-08-12 建立，同日擴大為全角色適用。
>
> **起因**：外部觀看者對 Iris Chen 四個批次（共 20 張）的反饋——「她的表情都是一樣的，都是一號表情。
> 雖然動作和衣服可能都有變化，但是她的髮型和表情都差不多。」
>
> **使用者判斷（2026-08-12）**：「這個問題好像不只有 Iris 這個人設是這樣，其他的 KOL 應該也有同樣的
> 問題。所以如果要改這個設定的話，就全部的 KOL 一起改。只是因為我現在先用 Iris 當作 sample 進行比較多
> 的產出，所以我比較容易發現這個問題。」
>
> 這份文件之於「臉」，等同 `WARDROBE_SYSTEM.md` 之於「衣服」：把表情與髮型從**人設的附屬品**
> 拉出來，變成**獨立輪替的變數**。**適用全部 11 位角色，不是 Iris 個案。**

---

## 一、根因分析（2026-08-12，Iris Chen 20 張逐張回溯）

**問題不在生成模型，在 prompt 模板。** 四個批次（`daily_sexy_night_v1`～`v4_bolder`）的
`[POSE / EXPRESSION]` 欄位，20 張裡有 19 張是同一個公式的變體：

```
chin slightly down, direct eye contact with the camera, faint smirk,
half-lidded relaxed expression / calm unbothered expression
```

逐項統計：

| 項目 | 20 張中的出現率 |
|---|---|
| `chin down`（下巴微低） | ~15 |
| `direct eye contact`（直視鏡頭） | ~16 |
| `half-lidded`（半瞇眼） | ~10 |
| `faint smirk` / `faint smile` | ~9 |
| 嘴巴閉著或僅微張 | 19 |
| **露出牙齒** | **0** |
| **閉眼／瞇成弧線** | **0** |
| **指定眉毛動作** | **0** |
| **指定表情不對稱** | **0** |
| **在做鏡頭以外的事（沒在對鏡頭表演）** | **0** |

**最關鍵的單一發現**：20 張裡有 16 張是「意識到鏡頭 ＋ 直視鏡頭」。
**「她有沒有意識到鏡頭」這個變數，從頭到尾沒有被轉過。** 服裝轉了 20 次，臉只轉了 1 次。

這與 `WARDROBE_SYSTEM.md` 第 13 點的根因結構完全相同——當時是「內容支柱決定了服裝」，
這次是「一句表情模板決定了全部的臉」。

### 1-b. 全角色層級的第二個問題：角色之間也會撞臉

同一組表情模板套在 11 位角色身上，後果不只是「每個角色自己單調」，而是
**11 位角色的臉會收斂成同一個人**——因為決定「這是誰」的除了五官，更大一部分是
**她怎麼笑、眼睛habitually 看哪裡、預設情緒強度**。五官由 `soul_id` 鎖定，但表情人格從來沒被定義過。

所以本系統分兩層：

- **共用層**（第二～四、六節）：三個軸、四項必寫、10 個表情庫、分配規則——**全角色一致**
- **人格層**（第五節）：每位角色的**招牌表情、第二常用、禁用表情、笑的方式、眼神預設**——**每位角色都不同**

> **笑的方式是最強的區隔器。** 如果 11 位角色笑起來一模一樣，她們就是同一個人穿不同衣服。

---

## 二、三個獨立軸（表情規劃的座標系）

不要用「開心／性感／慵懶」這種形容詞規劃表情，那會回到同一張臉。用三個軸定位：

| 軸 | 兩端 | 我們現況（Iris 20 張） |
|---|---|---|
| **A. 鏡頭意識** | 意識到並直視 ←→ 完全沒意識到鏡頭 | 16/20 壓在「意識到」那一端 |
| **B. 情緒能量** | 低（慵懶、放空） ←→ 高（大笑、驚訝） | 20/20 壓在「低」 |
| **C. 嘴巴狀態** | 閉合 ←→ 微張 ←→ 開口露牙 | 19/20 壓在「閉合／微張」 |

**規劃一批素材時，先在這三個軸上分配座標，再去挑第四節的表情編號。**

---

## 三、每個表情都必須寫滿的四件事

這是本系統的核心規則。只寫「她在微笑」不合格，一律退回重寫。

### 1. 動機（為什麼會有這個表情）
表情要是**對某件事的反應**，不是擺出來的姿勢。prompt 要寫出她在反應什麼：
`reacting to something her friend just said off-frame`、`because the tea is too hot`。
沒有動機的表情，模型會生成「模特兒擺表情」，那正是假的來源。

### 2. 三層臉部規格（眉／眼／嘴，分開寫）
模型不會自己動眉毛。三層都要各自指定：

```
BROW:  [哪一邊、往上還是往下、幅度]
EYES:  [睜大/半瞇/瞇成弧線/閉起] + [看哪裡——必須有具體落點]
MOUTH: [閉合/微張/開口/露牙/咬唇/嘴角哪一邊高]
```

### 3. 不對稱（明確指定哪一邊）
`.claude/agents/emotion-director.md` 的核心指令：**「臉永遠不會靜止，也永遠不對稱」**——
對稱的臉是 AI 感最強的訊號之一。每個表情都要指定一個不對稱點：
`the left corner of her mouth lifts higher than the right`、`only her right brow raises`。

### 4. 眼睛要有焦點
`eyes with no focal point read as dead`。就算不看鏡頭，也要寫出她在看什麼：
`looking at the condensation running down the window, not the lens`。

---

## 三之二、⚠️ 表情層與展示層是兩個獨立的層，不可互相犧牲

> **背景（2026-08-12，使用者退回 Iris `daily_expression_v5` 第一版規劃）**：
> 「你規劃的這 6 個場景，都沒有讓我看文字的時候，會覺得生成出來有什麼展示性感的想像。」

**這是導入本系統時最容易踩的坑，第一次規劃就踩到了。** 為了讓表情有可信的動機（第三節第 1 點），
規劃很容易整批推向「她在做一件日常瑣事、沒意識到鏡頭」——開冰箱、看筆電、曬衣服、脫鞋。
**表情層解決了，展示層卻整個崩掉。**

對照很明顯：`daily_sexy_night_v4_bolder` 在**文字階段**就讀得出性感（「V 領深至胸骨」「浴巾上緣壓在
胸口最上方」「背面全裸」）；v5 第一版卻是超大 T 恤、針織背心、睡袍、格紋襯衫——全是**舒適感**，
不是**展示感**。

**規則：規劃每一張時，兩個問題都要答得出來——**

1. **這張的表情動機是什麼？**（她在反應什麼事）
2. **這張的展示機制是什麼？**（畫面上是什麼讓身體被呈現出來）

### 展示機制的三種類型（每張至少一種，最好兩種）

| 類型 | 內容 | 例 |
|---|---|---|
| **A. 動作把身體拉長／彎折／打開** | 伸懶腰、後仰、手舉高、跨坐、趴姿翹腿、坐上檯面 | 跪坐後仰＝胸口打開＋腰線拉長 |
| **B. 衣服「正在發生什麼事」** | 濕透貼身、肩帶滑落中、下襬掀起、只扣一顆、綁帶鬆開 | 白背心被水淋濕貼在身上 |
| **C. 接觸點（觸覺聯想）** | 皮膚壓著玻璃／絲綢／檯面／水／地板 | 背貼落地窗、手撐淋浴間玻璃 |

**展示機制必須寫成畫面上看得到的物理事實，不是形容詞。**
❌ `sexy pose` ／ ✅ `both arms raised and pressed flat against the glass, which lifts her ribcage and lengthens her torso`

**額外好處**：A 型與 C 型的動作天然會把手放在對比色的實體表面上（玻璃、檯面、地板），
正好滿足第 10-c 點的手部防呆。

---

## 四、10 個表情庫（全角色共用編號）

> 編號全角色通用，但**強度與風味依第五節的角色人格調整**。
> 例：E-4 大笑，Coco 是少女式尖叫大笑，Ananya 是溫暖大姊式大笑，Sophia 則根本不做 E-4。

### 象限 1：意識到鏡頭 × 低能量

**E-1 半瞇微笑**
- 動機：她知道自己好看，不解釋
- `BROW: relaxed, the right one a fraction higher than the left`
- `EYES: half-lidded, looking straight into the lens`
- `MOUTH: closed, the left corner lifted higher than the right in a faint knowing smirk`

**E-2 挑眉歪頭（「幹嘛」）**
- 動機：對正在拍她的人有意見／覺得對方很煩
- `BROW: only her right brow raised high, the left held flat`
- `EYES: wide open, looking directly into the lens with a slightly sceptical tilt`
- `MOUTH: closed and pushed slightly to one side, the right corner pulled down`
- 加上：`head tilted to one side`

**E-3 嘟嘴抗議**
- 動機：撒嬌、討東西、抱怨
- `BROW: both drawn slightly together in the middle`
- `EYES: looking up into the lens from under her lashes`
- `MOUTH: lower lip pushed forward in a small pout, closed`

### 象限 2：意識到鏡頭 × 高能量

**E-4 開口大笑**
- 動機：鏡頭外的朋友剛講了一句很好笑的話
- `BROW: both lifted, the left slightly higher`
- `EYES: crinkled into curved crescents with visible smile lines at the outer corners, almost closed`
- `MOUTH: wide open laughing with her upper teeth visible, the left side pulled higher`
- 加上：`head tipped back a little, chin lifted, shoulders raised in mid-laugh`
- ⚠️ Iris 20 張裡**一張都沒有**——全角色最該補的一個

**E-5 抿嘴憋笑**
- 動機：在忍住不要笑出來（別人在鏡頭外做蠢事）
- `BROW: both raised, forehead slightly creased`
- `EYES: narrowed with genuine laughter in them, looking into the lens`
- `MOUTH: pressed firmly shut and pushed to the left, cheeks puffed slightly, nose wrinkled`

**E-6 驚訝／被抓到**
- 動機：沒想到現在正在被拍
- `BROW: both shot up high, forehead creased`
- `EYES: wide open, whites visible above the iris, caught looking at the lens`
- `MOUTH: open in a small round O`
- 加上：`shoulders pulled up, body leaning back slightly, one hand half-raised`

### 象限 3：沒意識到鏡頭 × 低能量

**E-7 放空**
- 動機：發呆，什麼都沒在想
- `BROW: completely relaxed, no tension anywhere`
- `EYES: unfocused but with a stated resting point — looking at the condensation on the window, not the lens`
- `MOUTH: slightly open and slack, lower lip loose`
- 加上：`facial muscles entirely released, no performance for the camera at all`

**E-8 專注做事**
- 動機：在做一件小事——擦乳液、剪指甲、看手機、挑指甲油
- `BROW: slightly drawn together in concentration`
- `EYES: cast down, focused on [她手上的東西], completely unaware of the camera`
- `MOUTH: lips slightly pursed / lower lip caught between her teeth in concentration`
- ⚠️ Iris 20 張裡也是**零**，卻最貼她 `character.md` 的「她不表演給鏡頭看」

**E-9 打呵欠／剛睡醒**
- 動機：真的想睡
- `BROW: inner ends lifted, sleepy`
- `EYES: squeezed shut / barely open and watering slightly`
- `MOUTH: open in a yawn, nose wrinkled`
- 加上：`one hand rubbing her eye, hair flattened on one side from the pillow`

### 象限 4：沒意識到鏡頭 × 高能量（先列，勾引組在後）

**E-10 講話講到一半**
- 動機：她正在跟鏡頭外的人講話，被抓拍
- `BROW: mid-movement, the left one lifting`
- `EYES: looking at someone off-frame to the left, not the lens`
- `MOUTH: caught mid-word, lips forming a vowel shape, teeth partly visible`
- 加上：`one hand raised mid-gesture, mid-sentence, unposed`
- 「抓拍感」最強的一個——照片看起來像剛好按到快門

### 勾引組（E-11～E-13，2026-08-12 補）

> **背景**：使用者看過 Iris v5 規劃後指出「動作可能都要帶有一些勾引、賣弄性感的那種感覺」。
> 檢視 E-1～E-10 才發現**只有 E-1 是明確勾引的**，其餘九個都是「生活感的臉」——
> 表情庫本身缺了一整個類別。以下三個補上這個缺口。
>
> **共同前提**：`.claude/agents/emotion-director.md` 的品味線——**挑逗可以，低俗不行**；
> 這三個表情的關鍵字是「她知道你在看，而且她樂在其中」，不是取悅或討好。
> **象限上全部屬於「意識到鏡頭」**，與 E-7／E-8／E-9／E-10 的「沒意識到」形成對照。

**E-11 咬下唇（回眸）**
- 動機：她知道你在看，而且故意讓你看
- `BROW: the right one raised a fraction, the left held level`
- `EYES: locked on the lens from under lowered lids, unhurried`
- `MOUTH: lower lip caught between her teeth on the left side, the right corner curling up`
- 加上：`looking back over one shoulder`（回眸版效果最強）

**E-12 微張嘴、緩緩呼氣（慵懶版）**
- 動機：剛伸展完／剛醒／熱——身體的自然反應，不是擺出來的
- `BROW: both relaxed, inner ends slightly lifted`
- `EYES: nearly closed, lashes low, only just still looking at the lens`
- `MOUTH: parted, jaw loose, mid-exhale, lower lip fuller than the upper`
- 加上：`chin lifted, throat and collarbone exposed`（這個表情要配合仰頭才成立）

**E-13 手指抵著下唇、眼睛往上看鏡頭**
- 動機：在想一件事，想到一半發現你在看
- `BROW: both lifted slightly, an unspoken question`
- `EYES: looking up into the lens from beneath, head angled down`
- `MOUTH: closed, her index finger resting against the centre of her lower lip`
- ⚠️ **注意**：頭低、眼睛往上看是**表情**，不是相機角度——相機仍維持平視或微俯角，
  絕不可改成由下往上仰拍（`SEXY_SCENE_LIBRARY.md` 第 16 點）

---

## 四之二、⚠️ 模型能力邊界：細微的嘴部表情生不出來（2026-08-14 實測，9 次生成）

> **這是導入本系統後最重要的一次實測發現，直接決定哪些表情可以用。**

Iris `daily_expression_v5` 首批 6 張 ＋ 重生 3 張，結果如下：

| 表情 | 類型 | 結果 |
|---|---|---|
| **E-4 開口大笑** | 大動作 | ✅ 成功 |
| **E-13 手指抵下唇** | 有實體錨點 | ✅ 成功（本批最好的一張） |
| **E-1 半瞇微笑** | 模型預設臉 | ✅ 成功 |
| **E-11 咬下唇** | 純肌肉細節 | ❌ **兩次都失敗**：第一次變成閉嘴微笑，第二次變成開口大笑 |
| **E-5 抿嘴憋笑** | 純肌肉細節 | ❌ 第一次變成閉嘴微笑；第二次加了「手抬到嘴邊」才勉強有一點，仍不到位 |
| **E-12 微張嘴呼氣** | 純肌肉細節 | ❌ 第一次變成閉嘴微笑；第二次仰頭做到了，但嘴變成大笑 |

**失敗模式高度一致：只要表情是純肌肉的細微變化，模型一律忽略，並倒退回它的預設臉——「閉嘴微笑」或「開口大笑」。** 而那個閉嘴微笑，正是這整套系統要解決的「一號表情」本人。

**第二次重生已證明這不是 prompt 寫法問題**：即使把表情段落搬到 prompt 最前面、寫成「這張照片唯一必須呈現的就是 X」、加上「如果只是閉嘴微笑就算失敗」的否定句、並拉近景別到半身，三個細微表情仍然全部失敗。**這是模型能力邊界，不是描述精度問題，不要再燒 credit 重試。**

### 修正後的表情選用規則

**每個表情都必須落在下面兩類之一，否則不要排進批次：**

| 類 | 定義 | 可用表情 |
|---|---|---|
| **① 大動作表情** | 臉部有大幅度的形變，遠看就看得出來 | E-4 大笑、E-6 驚訝（眉眼大開＋嘴成 O）、E-9 打呵欠、E-2 挑眉（眉毛位移夠大）、E-3 嘟嘴（唇部外推夠大） |
| **② 有實體錨點的表情** | 畫面上有一個**看得見的物件或手部動作**參與這個表情 | E-13 手指抵下唇、手背半摀嘴、手撥開頭髮、咬著吸管／髮尾、手背抵額頭、手托腮擠壓臉頰 |

**禁止單獨使用的（純肌肉細節，實測生不出來）**：咬下唇、抿嘴憋笑、微張嘴呼氣、似笑非笑、嘴角極小幅度上揚。

**這條對第五節的角色人格有直接影響**——Sophia 的「只有眼睛在笑，嘴幾乎不動」與 Luna 的「嘴角極小幅度上揚」都屬於純肌肉細節，**目前的模型做不到**。這兩位角色的表情要改用②類的實體錨點來達成同樣的克制感（例如手指抵著杯緣、手背撐著下顎），而不是靠嘴部的微小變化。

### 補充：景別要求

`.claude/agents/emotion-director.md` 早有一句「微表情在全身遠景裡是看不見的，若鏡頭太遠讀不到臉，要求更近的景別」——**這條之前只用在影片上，靜態圖從沒套用。** 本批失敗的三張初版全部是中景到全身。**排表情批次時，臉必須在畫面裡夠大**：胸上到腰上的景別為佳，全身遠景不要指望表情讀得到。

---

## 五、各角色的表情人格（每位都不同）

> **這一節是防止 11 位角色撞臉的關鍵。** 招牌表情配額一律 **≤30%**。
> 「禁用」欄不是絕對禁止，而是**該表情不屬於這個角色，用了會讓她不像她**。

| 角色 | 招牌（≤30%） | 第二常用 | 禁用 | **笑的方式（最強區隔器）** | 眼神預設 |
|---|---|---|---|---|---|
| **Iris Chen** 22 台北 IT girl | E-1 半瞇微笑 | E-8 專注做事 | 對鏡頭比 pose 的甜笑、誇張驚訝 | 閉嘴的鼻息笑，真的笑出來會低頭用手背擋一下 | 直視鏡頭，但沒有在討好 |
| **Coco Wu** 20 台中校園甜心 | **E-4 大笑** | E-6 驚訝 | E-1 半瞇冷笑（太有距離感）、deadpan | 少女式尖叫大笑，笑到瞇成一條線、肩膀抖、會遮嘴 | 亮、直接、什麼都寫在臉上 |
| **Rainie Hsu** 24 派對女王 | E-2 挑眉 | E-5 抿嘴壞笑 | E-3 嘟嘴撒嬌（不符她的權力關係） | **只有半邊嘴角，不出聲**，笑完把視線移開 | 由上往下斜看鏡頭，帶挑釁 |
| **Sophia Tseng** 28 貴婦名媛 | E-7 放空（疏離版） | E-5 抿嘴（極小幅度） | E-4 大笑露牙、E-6 誇張驚訝、E-3 嘟嘴 | **只有眼睛在笑，嘴幾乎不動**，最多嘴角 2mm | 不太看鏡頭，看鏡頭時也沒有要交流 |
| **Mia Huang** 22 直播主 | E-2 挑眉（表演式） | E-10 講話中（她一直在跟 chat 講話） | 長時間安靜放空 | 誇張、往後仰、笑完馬上做鬼臉接下一句 | 對著鏡頭像對著觀眾，不斷 break 第四面牆 |
| **Vicky Lin** 25 健身 | E-2 挑眉（得意版） | E-8 專注（訓練中） | E-3 嘟嘴撒嬌 | 開口笑＋挑眉，帶挑釁的「你看吧」 | 直視，帶競爭感 |
| **Luna Tanaka** 20 京都 | E-7 放空（在看一個很小的東西） | E-8 專注 | E-4 大笑、E-6 誇張驚訝 | **眼睛先笑，嘴角極小幅度上揚**，沒有聲音 | 常常不在鏡頭上，看光、看窗、看手上的東西 |
| **Ananya Kapoor** 23 孟買 | **E-4 大笑（溫暖大姊版）** | E-8 專注（瑜伽） | E-2 冷挑眉 | 頭往後仰、整張臉都在笑、會拍大腿 | 溫暖直視，像在看一個她喜歡的人 |
| **Camille Dupont** 22 里昂 | E-7 放空（夢遊感） | E-1 半瞇（更鬆、更不對焦） | E-6 誇張驚訝、E-4 爆笑 | **幾乎不笑**，只有一邊嘴角，而且笑完立刻收 | 沒有對焦點的柔軟視線 |
| **Aaliya Okonkwo** 25 東洛杉磯 | E-10 講話講到一半 | E-4 大笑 | 長時間放空 | **先 deadpan、再突然爆笑**——反差就是她的笑點 | 邊講邊看鏡頭外的人，偶爾轉回鏡頭 |
| **Yuna Kim** 21 首爾 | E-1 半瞇（冷版） | E-8 專注（護膚） | E-6 誇張驚訝 | 低調、短促，笑一下就收回去 | 平視鏡頭，淡，不需要你看 |

**三組容易撞的招牌，區隔寫法**（規劃時務必照這個寫，不然三個人會長一樣）：

- **E-2 挑眉三人組**：Rainie＝**嘲諷**的冷挑眉（嘴角往下）／ Mia＝**表演給觀眾看**的誇張挑眉（配合手勢）／ Vicky＝**得意挑釁**的挑眉（配合開口笑）
- **E-7 放空三人組**：Sophia＝**有錢人的無聊**（眼神空但姿態端正）／ Luna＝**在專心看一個很小的東西**（眼睛有落點）／ Camille＝**剛醒還沒回神**（臉部完全鬆掉）
- **E-4 大笑二人組**：Coco＝**少女尖叫**（高頻、遮嘴、肩膀抖）／ Ananya＝**溫暖大姊**（低頻、往後仰、整張臉）

---

## 六、髮型：問題不是「幾種髮型」，是「幾種狀態」

Iris 前四批其實有換髮型（放下／濕髮／鯊魚夾／低馬尾／高馬尾／半盤＋緞帶／丸子頭／辮子），
**但讀起來還是一樣**，因為全部都是「同樣長度、同樣中分、同樣黑直、同樣乾淨」的變體。

真正會改變臉部讀感的是下面兩個變數，**前四批一次都沒動過**：

| 變數 | 選項 | 影響 |
|---|---|---|
| **瀏海** | 無瀏海／空氣瀏海／旁分長瀏海／中分長瀏海垂在兩頰 | **改變臉型輪廓，效果最大** |
| **分線** | 中分／深旁分／全部往後撥 | 改變臉的寬窄讀感 |

再加上「頭髮的狀態」（不是造型）：

- **H-1 剛洗完的濕髮**：貼頭皮、顏色更深、一束一束、髮尾滴水
- **H-2 隔夜亂髮／睡壓痕**：蓬、有靜電、一邊被壓翹
- **H-3 隨手抓起來的盤髮**：鯊魚夾，碎髮掉一堆
- **H-4 吹整過的滑順放下**：有光澤、明確指定分線
- **H-5 綁起來的**：高馬尾／低雙辮／半盤＋緞帶

**規則**：每批 5–6 張至少涵蓋 3 種 H 狀態，且**至少 1 張要動到瀏海或分線**。

---

## 七、一批 5–6 張的分配規則（硬性，全角色適用）

- [ ] 該角色的招牌表情**最多 1 張**
- [ ] **至少 1 張沒有在看鏡頭**（E-7／E-8／E-10）
- [ ] **至少 1 張嘴巴是打開的、看得到牙齒**（E-4／E-6／E-9／E-10；Sophia、Camille、Luna 這類禁用大笑的角色改用 E-10 講話中）
- [ ] 連續兩張不可落在同一象限
- [ ] 每張都寫滿眉／眼／嘴三層 ＋ 一個不對稱點 ＋ 一個動機 ＋ 眼睛的落點
- [ ] 髮型至少 3 種狀態，至少 1 張動到瀏海或分線
- [ ] 表情選擇有對照第五節該角色的「禁用」欄

### 禁用字串

以下這一整串是 Iris 前四批的模板，**全角色都不可再整組沿用**：

```
chin slightly down, direct eye contact with the camera, faint smirk,
half-lidded relaxed expression
```

單獨使用其中某一項沒問題（E-1 就是它），但不可四項一起、也不可連續兩張都用。

---

## 八、與既有規則的關係

- **`SEXY_SCENE_LIBRARY.md` 第 14 點（Carousel ＝ 1 個 setup × 5–6 種表情）**：
  這份文件正是第 14 點缺的那一半。第 14 點說 carousel 要「只變表情」，但沒有定義
  「表情有哪些」——所以實務上一直做不出來。有了這 10 個編號，第 14 點才可執行。
- **`.claude/agents/emotion-director.md`**：該 agent 原本只用於影片的逐秒表情時間軸。
  本文件把它的兩條核心原則（R2 微表情流動、R3 不對稱）下放到**靜態圖**。
- **`WARDROBE_SYSTEM.md`**：同一套「獨立變數 ＋ 招牌配額」的結構，套用在臉上。
  規劃素材時，服裝轉盤（WARDROBE）與表情轉盤（本文件）**各自獨立轉**。

---

## 九、導入狀態

| 角色 | 表情人格已定義 | 已用新系統生成 |
|---|---|---|
| Iris Chen | ✅ | ⬜ 待生成（`daily_expression_v5` 規劃見其 `generation_notes.md`）|
| 其餘 10 位 | ✅ | ⬜ 尚未 |

**既有素材不需重做。** 使用者 2026-08-12 明確表示：舊素材雖被指出表情重複，「那些素材沒有不好，
還是可以使用」——本系統只適用於**新生成的批次**，不追溯。

---

*2026-08-12 建立，同日擴大為全角色適用。根因分析基礎：Iris Chen `daily_sexy_night_v1`～`v4_bolder` 共 20 張逐張回溯。*
