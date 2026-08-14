# Virtual KOL Studio — Expression System（表情系統）

> 2026-08-12 建立。起因：外部觀看者對 Iris Chen 四個批次（共 20 張）的反饋——
> 「她的表情都是一樣的，都是一號表情。雖然動作和衣服可能都有變化，但是她的髮型和表情都差不多。」
>
> 這份文件之於「臉」，等同 `WARDROBE_SYSTEM.md` 之於「衣服」：把表情與髮型從**人設的附屬品**
> 拉出來，變成**獨立輪替的變數**。

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
| `faint smirk` / `faint smile`（淡淡微笑） | ~9 |
| 嘴巴閉著或僅微張 | 19 |
| **露出牙齒** | **0** |
| **閉眼／瞇成弧線** | **0** |
| **指定眉毛動作** | **0** |
| **指定表情不對稱** | **0** |
| **在做鏡頭以外的事（沒在對鏡頭表演）** | **0** |

**最關鍵的單一發現**：20 張裡有 16 張是「意識到鏡頭 ＋ 直視鏡頭」。
**「她有沒有意識到鏡頭」這個變數，從頭到尾沒有被轉過。** 服裝轉了 20 次，臉只轉了 1 次。

這與 `WARDROBE_SYSTEM.md` 第 13 點的根因結構完全相同——當時是「支柱決定了服裝」，
這次是「一句表情模板決定了全部的臉」。

---

## 二、三個獨立軸（表情規劃的座標系）

不要用「開心／性感／慵懶」這種形容詞規劃表情，那會回到同一張臉。用三個軸定位：

| 軸 | 兩端 | 我們現況 |
|---|---|---|
| **A. 鏡頭意識** | 意識到並直視 ←→ 完全沒意識到鏡頭 | 16/20 壓在「意識到」那一端 |
| **B. 情緒能量** | 低（慵懶、放空） ←→ 高（大笑、驚訝） | 20/20 壓在「低」 |
| **C. 嘴巴狀態** | 閉合 ←→ 微張 ←→ 開口露牙 | 19/20 壓在「閉合／微張」 |

**規劃一批素材時，先在這三個軸上分配座標，再去挑下面的表情編號。**

---

## 三、每個表情都必須寫滿的三件事

這是本系統的核心規則。只寫「她在微笑」不合格，一律退回重寫。

### 1. 動機（為什麼會有這個表情）
表情要是**對某件事的反應**，不是擺出來的姿勢。prompt 要寫出她在反應什麼：
`reacting to something her friend just said off-frame`、`because the tea is too hot`。
沒有動機的表情，模型會生成「模特兒擺表情」，那正是假的來源。

### 2. 三層臉部規格（眉／眼／嘴，分開寫）
模型不會自己動眉毛。三層都要各自指定：

```
BROW: [哪一邊、往上還是往下、幅度]
EYES: [睜大/半瞇/瞇成弧線/閉起] + [看哪裡——必須有具體落點]
MOUTH: [閉合/微張/開口/露牙/咬唇/嘴角哪一邊高]
```

### 3. 不對稱（明確指定哪一邊）
`emotion-director` agent 的核心指令：**「臉永遠不會靜止，也永遠不對稱」**——
對稱的臉是 AI 感最強的訊號之一。每個表情都要指定一個不對稱點：
`the left corner of her mouth lifts higher than the right`、`only her right brow raises`。

### 4. 眼睛要有焦點
`eyes with no focal point read as dead`。就算不看鏡頭，也要寫出她在看什麼：
`looking at the condensation running down the window, not the lens`。

---

## 四、Iris Chen 的 10 個表情

> ★ = 招牌表情，**配額 ≤30%**（比照 `WARDROBE_SYSTEM.md` 的招牌服裝配額邏輯）。
> 選表情時先看象限，不要每次都挑順手的。

### 象限 1：意識到鏡頭 × 低能量

**E-1 ★半瞇微笑（現行的「一號表情」，保留但限額）**
- 動機：她知道自己好看，不解釋
- `BROW: relaxed, the right one a fraction higher than the left`
- `EYES: half-lidded, looking straight into the lens`
- `MOUTH: closed, the left corner lifted higher than the right in a faint knowing smirk`
- 適合：招牌單圖、貼文首圖

**E-2 挑眉歪頭（「幹嘛」）**
- 動機：對正在拍她的人有意見／覺得對方很煩
- `BROW: only her right brow raised high, the left held flat`
- `EYES: wide open, looking directly into the lens with a slightly sceptical tilt`
- `MOUTH: closed and pushed slightly to one side, the right corner pulled down`
- 加上：`head tilted to one side`
- 適合：他拍、朋友視角

**E-3 嘟嘴抗議**
- 動機：撒嬌、討東西、抱怨
- `BROW: both drawn slightly together in the middle`
- `EYES: looking up into the lens from under her lashes`
- `MOUTH: lower lip pushed forward in a small pout, closed`
- 適合：自拍近景

### 象限 2：意識到鏡頭 × 高能量

**E-4 開口大笑**
- 動機：鏡頭外的朋友剛講了一句很好笑的話
- `BROW: both lifted, the left slightly higher`
- `EYES: crinkled into curved crescents with visible smile lines at the outer corners, almost closed`
- `MOUTH: wide open laughing with her upper teeth visible, the left side of her mouth pulled higher`
- 加上：`head tipped back a little, chin lifted, shoulders raised in mid-laugh`
- ⚠️ 這是本系統**最重要的一個表情**——20 張裡一張都沒有

**E-5 抿嘴憋笑**
- 動機：在忍住不要笑出來（別人在鏡頭外做蠢事）
- `BROW: both raised, forehead slightly creased`
- `EYES: narrowed with genuine laughter in them, looking into the lens`
- `MOUTH: pressed firmly shut and pushed to the left, cheeks puffed slightly, nose wrinkled`
- 適合：他拍、有互動感的情境

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
- ⚠️ **這一類 20 張裡也是零**，卻最貼她 character.md 的「她不表演給鏡頭看」

**E-9 打呵欠／剛睡醒**
- 動機：真的想睡（她的帳號簡介就是「剛睡醒。」）
- `BROW: inner ends lifted, sleepy`
- `EYES: squeezed shut / barely open and watering slightly`
- `MOUTH: open in a yawn, nose wrinkled`
- 加上：`one hand rubbing her eye, hair flattened on one side from the pillow`
- 適合：晨起系列，也是她 tagline 的具象化

### 象限 4：沒意識到鏡頭 × 高能量

**E-10 講話講到一半**
- 動機：她正在跟鏡頭外的人講話，被抓拍
- `BROW: mid-movement, the left one lifting`
- `EYES: looking at someone off-frame to the left, not the lens`
- `MOUTH: caught mid-word, lips forming a vowel shape, teeth partly visible`
- 加上：`one hand raised mid-gesture, mid-sentence, unposed`
- 這是「抓拍感」最強的一個——照片看起來像剛好按到快門

---

## 五、髮型：問題不是「幾種髮型」，是「幾種狀態」

前四批其實有換髮型（放下／濕髮／鯊魚夾／低馬尾／高馬尾／半盤＋緞帶／丸子頭／辮子），
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

**規則**：每批 5 張至少涵蓋 3 種 H 狀態，且**至少 1 張要動到瀏海或分線**。

---

## 六、一批 5 張的分配規則（硬性）

- [ ] 招牌 E-1 **最多 1 張**
- [ ] **至少 1 張沒有在看鏡頭**（E-7／E-8／E-10）
- [ ] **至少 1 張嘴巴是打開的、看得到牙齒**（E-4／E-6／E-9／E-10）
- [ ] 連續兩張不可落在同一象限
- [ ] 每張都寫滿眉／眼／嘴三層 ＋ 一個不對稱點 ＋ 一個動機 ＋ 眼睛的落點
- [ ] 髮型至少 3 種狀態，至少 1 張動到瀏海或分線

### 禁用字串

以下這一整串是前四批的模板，**不可再整組沿用**：

```
chin slightly down, direct eye contact with the camera, faint smirk,
half-lidded relaxed expression
```

單獨使用其中某一項沒問題（E-1 就是它），但不可四項一起、也不可連續兩張都用。

---

## 七、與既有規則的關係

- **`SEXY_SCENE_LIBRARY.md` 第 14 點（Carousel ＝ 1 個 setup × 5–6 種表情）**：
  這份文件正是第 14 點缺的那一半。第 14 點說 carousel 要「只變表情」，但沒有定義
  「表情有哪些」——所以實務上一直做不出來。有了這 10 個編號，第 14 點才可執行。
- **`.claude/agents/emotion-director.md`**：該 agent 原本只用於影片的逐秒表情時間軸。
  本文件把它的兩條核心原則（R2 微表情流動、R3 不對稱）下放到**靜態圖**。
- **`WARDROBE_SYSTEM.md`**：同一套「獨立變數 ＋ 招牌配額」的結構，套用在臉上。

---

## 八、驗證方式（建議的第一次測試）

**用「1 個 setup × 6 種表情」測**——固定服裝、場景、光線、髮型，**只變表情**，
這樣表情是唯一變因，一次就能看出這套系統有沒有效。

而且這個測試本身就是一則可直接發佈的 carousel（`SEXY_SCENE_LIBRARY.md` 第 14 點指定的
最高優先格式，但工作室至今沒有實際做過一則）。

建議測試組合：E-1（招牌）／E-4（大笑）／E-8（專注做事）／E-2（挑眉）／E-9（打呵欠）／E-10（講話中）
——橫跨四個象限，且包含三個「零出現率」的類型。

---

*2026-08-12 建立。根因分析基礎：Iris Chen `daily_sexy_night_v1`～`v4_bolder` 共 20 張逐張回溯。*
