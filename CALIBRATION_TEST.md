# 控制變因測試（Calibration Test）— Soul 2.0

> 2026-08-27 建立。可預覽版本：<https://claude.ai/code/artifact/327f9193-9c04-40b4-8d3f-d944143111d9>
>
> **這份文件的目的不是寫出「完美 prompt」，是先建立「怎麼知道一個寫法有沒有用」。**
>
> 外部覆核（ChatGPT，2026-08-27）指出本專案方法論最大的盲點：
> 「你改太多變因，就無法知道哪個因素真的有用。」以及
> 「現在還不應該寫『完美公式』，應該先寫『測試方法』。」
>
> 這份文件就是那個測試方法。**在這份測試跑完之前，不要再改 20 件正式 spec，
> 也不要把任何新公式寫死進 `PHOTO_DIRECTION_STANDARD.md`。**

---

## 0. 為什麼需要這個

前兩輪 pilot 的失敗診斷過程長這樣：看圖 → 覺得不對 → 一次改五六件事 → 再看圖。
就算第三輪成功了，也不知道是因為 prompt 變短、pose 放前面、韓國字眼拿掉、
85mm 生效、還是參考圖生效。**這種循環會一直燒 credit，但知識不會累積。**

同時，我自己過去的內部檢查器出現過三次假陰性（把「雙手捧著」算成單手、
把解釋句裡的「35mm」當成實際焦段、動作關鍵字表漏掉「被帶起」）。
**所以評分規則必須寫成「打開圖看得到什麼」，不能寫成「prompt 裡有沒有寫」。**

---

## 1. 這次測試的固定變因（控制組）

以下每一項在**整份測試中都不准動**：

| 項目 | 固定值 |
|---|---|
| 角色 | Yuna Kim，`soul_id: 235794a5-2eff-45fb-91b4-3232910afefa` |
| 模型 | `soul_2` |
| 畫質 | `2k` |
| 比例 | `9:16` |
| 每次生成張數 | **1**（見 `SEXY_SCENE_LIBRARY.md` 第 21 點） |
| 題材 | 台北巷弄，白天，走路被叫住回頭 |
| 景別目標 | 全身 |
| 服裝 | 白色短版 T ＋ 罩衫式長版薄襯衫（未扣）＋ 低腰丹寧迷你裙 ＋ 黑瑪莉珍鞋 |
| 表情目標 | 回眸一笑 |

選 Yuna 而不是 Luna，是因為**「回眸」失敗與「場景生成到韓國」這兩個未解症狀都出在她身上**，
訊號最強。跨角色是否成立另外用第三輪的 N 組驗。

### ⚠️ 這個測試設計本身的已知弱點

`soul_2` **沒有 seed 欄位**（實測參數表：只有 `quality`／`soul_id`／`aspect_ratio`／`prompt`／1 張參考圖）。
也就是說**同一個 prompt 送兩次，結果本來就會不一樣**。n=1 的差異可能純粹是雜訊。

因此本測試的判定門檻刻意訂得保守：

- **單一維度差 ≥ 2 分**（例如 0 分 vs 2 分），或**總分差 ≥ 3 分** → 算訊號
- 差 1 分 → 記為**未分出勝負**，不寫進任何文件
- 任何要寫進 SOP 的結論，該組 arm **必須再跑一次確認**（n=2）
- 同一輪的所有 arm **要連續送出**，不要跨天比（模型端可能更新）

---

## 2. 評分表（每張圖只評這五件事，各 0–2 分）

| 維度 | 2 分 | 1 分 | 0 分 |
|---|---|---|---|
| **Identity 身分一致** | 一眼就是 Yuna | 像但五官有偏移／年齡感跑掉 | 換了一個人 |
| **Pose 姿勢達成** | 走路中回頭、重心在後腳、上半身扭轉——都做出來 | 只做出一半（有轉頭但站定，或有走路但沒回頭） | 正面站著，完全沒做 |
| **Expression 表情達成** | 明確認得出是「回眸一笑」（眼睛彎、嘴微開） | 有在笑但不是指定的那種 | 面無表情 |
| **Location 場景達成** | 一看就是台灣（繁體直式招牌／騎樓／鐵捲門／白底機車牌） | 亞洲街景但沒有可辨識的在地物件 | 明顯是韓國或日本（韓文／日文招牌） |
| **Outfit 服裝達成** | 五層單品全中 | 主要單品中，但 1–2 件跑掉（如裙變褲） | 整套換掉 |

**滿分 10 分。**

另外記一欄**不進分數**的：**「可發布？」**——這是 Penny 的美感判定。
**要分清楚：adherence 高不等於好看。**一張五項全中但很醜的圖，
仍然是有效的測試結果（代表控制桿有效），但不能發。這兩件事分開記。

**評分方式**：一定要真的把圖打開看。不准用 prompt 內容反推分數。

---

## 3. 第一輪：長度與順序（4 張）

**問的問題**：330 字失敗是因為「太長」還是因為「順序不對」？

四組**只有 prompt 本身不同**，其他全部照第 1 節固定。

> **與外部建議的一個刻意偏離**：覆核建議的 C 組短版原稿裡含
> 「Canon EOS R5, 85mm f/2.0 from 4 metres」。我把機身型號與焦段從第一輪**全部拿掉**——
> 那是兩個獨立變因，混在長度測試裡就白測了，改到第二輪單獨測。
> 同理，體型數字與族裔描述也留到第二輪。

### A 組｜330 字原版（已知失敗的對照組）

用第二輪 pilot **實際送出的那份原文，一字不改**（全文見 `AI_PROMPT_METHOD_REVIEW.md` 第 8-1 節）。
它同時包含了「長」「族裔與體型數字」「NOT Korea 否定句」「35mm」四個問題，
**所以它不是乾淨的單變因組，它是基準線**——用來確認今天的模型行為跟上次一致。

### B 組｜約 100 字

```
Full-body candid street photograph in a Taipei alley. A young woman walking away is called by name
and glances back over her shoulder mid-stride, smiling with her eyes crinkling, one hand on her bag
strap, the open panels of her sheer shirt trailing in the turn. She wears a white cropped tee, an
unbuttoned long sheer shirt, a low-rise denim mini skirt, black mary janes with white socks. Pale
green vintage tile walls, potted plants, warm awnings, traditional Chinese vertical shop signs,
parked scooters. Late afternoon sun in front of her, lighting her face. Camera at her navel level,
lens horizontal, shot from well back. Visible skin pores, natural texture, film grain.
```

### C 組｜約 80 字，相機在前

```
Full-body candid street photo, camera at her navel level, lens horizontal, shot from well back. A
young woman glances back over her shoulder mid-stride and smiles, eyes crinkling, one hand on her
bag strap, sheer open shirt trailing in the turn. White cropped tee, denim mini skirt, mary janes.
Bright Taipei alley: pale green tile walls, potted plants, traditional Chinese vertical shop signs.
Low sun in front of her lighting her face. Visible skin pores, natural skin texture, film grain.
```

### D 組｜約 80 字，**瞬間／動作在前**

**與 C 組用字完全相同，只有句子順序不同**——這是本輪唯一乾淨的單變因對照。

```
A young woman walking away in a Taipei alley glances back over her shoulder mid-stride and smiles,
eyes crinkling, one hand on her bag strap, sheer open shirt trailing in the turn. Full-body candid
street photo, camera at her navel level, lens horizontal, shot from well back. White cropped tee,
denim mini skirt, mary janes. Pale green tile walls, potted plants, traditional Chinese vertical
shop signs. Low sun in front of her lighting her face. Visible skin pores, natural skin texture,
film grain.
```

**第一輪的勝出版本稱為 `W`，第二、三輪都以 `W` 為底。**

---

## 4. 第二輪：一次一根控制桿（5 張）

每一組都是 **`W` ＋ 改一件事**。另外把 `W` 本身**再跑一次**（記為 `W'`），
它同時是這一輪的對照組，也是**雜訊估計值**——`W` 與 `W'` 的分差就是這個模型的隨機波動下限。
如果 `W` 跟 `W'` 自己就差 3 分，那這一輪所有結論都要打折看。

| 組 | 相對 `W` 唯一改變的事 | 要回答的問題 |
|---|---|---|
| **W'** | 什麼都不改，重跑 | 雜訊有多大？ |
| **E** | 加 `85mm` | 焦段寫了有用嗎？ |
| **F** | 加 `50mm` | 還是說寫什麼焦段都一樣（＝安慰劑）？ |
| **G** | 加回族裔＋三圍＋身高＋腿長比例 | `soul_id` 到底有沒有鎖體型？ |
| **I** | 掛一張**無人的台北巷弄實景**參考圖 | 參考圖是不是最強的那根桿？ |

> **E/F 是一組對子，不是兩個獨立測試。**如果 E 和 F 生出來的透視幾乎一樣，
> 結論就是「焦段數字對這個模型無效」，那 `PHOTO_DIRECTION_STANDARD.md` 裡
> 所有寫死焦段的句子都該刪掉，而不是改成另一個數字。
>
> **G 組是反向測試。**如果 G 比 `W` 差（身材反而跑掉、或臉被拉走），
> 就證實「有了 `soul_id` 就不該再寫體型」；如果 G 明顯比 `W` 好，
> 代表 `soul_id` 只鎖臉，體型描述必須保留。這一題目前是純猜測。
>
> **I 組有前置條件**：需要一張**沒有人物的台北巷弄實景照**。
> 部落客的餐廳內裝參考圖庫裡沒有街景。這張要先取得（來源與授權請 Penny 決定），
> **拿不到就先不跑，記為「未測」，不要用別的圖硬湊**——湊了就等於又多改一個變因。

---

## 5. 第三輪：專打兩個未解症狀（4 張）

| 組 | 內容 | 針對的症狀 |
|---|---|---|
| **K** | `W` ＋ 台北在地識別物加倍（具名店招內容、白底機車牌、鐵捲門、騎樓、路邊回收桶） | 場景生成到韓國／日本 |
| **L** | `W` ＋ 回眸的**身體連動完整寫法**（重心壓後腳、前腳跟離地、骨盆朝行進方向、上半身扭 30 度、髮尾在甩動軌跡上） | 回眸做不出來 |
| **M** | `W` ＋ **只寫表情名**（`glances back over her shoulder, smiling`），把身體連動全部拿掉 | 同上（L 的對照） |
| **N** | 用 **Luna 的 `soul_id`** 跑 `W`（服裝與場景照 Luna 的 spec 換掉，其餘結構不動） | 結論跨角色成立嗎？ |

**K 組是關鍵。**外部覆核的判定是：**「重點不是『排除韓國』，而是『強化台北』。」**
`soul_2` 沒有 negative prompt 欄位，`NOT Korea` 這種寫法在正向 prompt 裡不但無效，
還可能反而強化韓國。K 組要驗證的是「正向強化在地物件」能不能取代否定句。

**L vs M 是一組對子**，回答「為什麼同一輪裡『比 V』成功而『回眸』失敗」：
是因為回眸需要整段身體描述（那 L 贏），還是因為身體描述太長反而稀釋了動作關鍵字（那 M 贏）。

---

## 6. 記錄表（跑完就填，不要事後回憶）

| 組 | generation id | Identity | Pose | Expr | Location | Outfit | 總分 | 可發布？ | 目視備註 |
|---|---|---|---|---|---|---|---|---|---|
| A | | | | | | | | | |
| B | | | | | | | | | |
| C | | | | | | | | | |
| D | | | | | | | | | |
| W' | | | | | | | | | |
| E | | | | | | | | | |
| F | | | | | | | | | |
| G | | | | | | | | | |
| I | | | | | | | | | |
| K | | | | | | | | | |
| L | | | | | | | | | |
| M | | | | | | | | | |
| N | | | | | | | | | |

---

## 7. 反證表：什麼結果會讓我**放棄**現在的主張

這一節是這份測試最重要的地方。**先寫好「什麼結果算我錯」，才不會事後幫自己的結論找理由。**

| 我目前的主張 | 什麼結果會推翻它 | 推翻後要動的文件 |
|---|---|---|
| prompt 太長是主因 | B/C/D 都沒有明顯優於 A | `AI_PROMPT_METHOD_REVIEW.md` 第二節 |
| 動作／瞬間要放最前面 | D 沒有優於 C | `PHOTO_DIRECTION_STANDARD.md` 優先序 |
| 焦段要寫 | E 與 F 沒有可見差異 | `PHOTO_DIRECTION_STANDARD.md` 焦段表（整段刪） |
| `soul_id` 已鎖體型，不必寫身材 | G 明顯優於 `W` | 兩位的 spec 都要加回體型段 |
| 正向強化在地物件可以取代否定句 | K 仍然生出韓文招牌 | 要改用參考圖鎖場景，或放棄純文字控場景 |
| 回眸需要完整身體連動描述 | M 贏過 L | 表情庫（`SEXY_SCENE_LIBRARY.md` 第 20 點）要改寫成極簡寫法 |
| 結論可跨角色沿用 | N 明顯低分 | 兩位要各自建立一套 prompt 結構 |

---

## 8. 成本

2K 一張約 **0.12 credits**（已用 `transactions` 逐筆對帳確認，不是用餘額差推算）。

| 輪 | 張數 | 估計 |
|---|---|---|
| 第一輪 | 4 | 0.48 |
| 第二輪 | 5（I 組可能不跑） | 0.48–0.60 |
| 第三輪 | 4 | 0.48 |
| **合計** | **12–13** | **約 1.5 credits** |

**對帳規則**：每一輪跑完用 `transactions` 拉出逐筆記錄核對，
**絕對不要用餘額前後差來算成本**——2026-08-26 那次就是這樣把 0.48 誤報成 66 credits
（真正的落差來自同帳號其他活動的 Voice Element 與 Seed Audio）。結果記進 `clients/sushisolar-rujiao/cost-log.md`。

---

## 9. 跑完之後做什麼

**產出不是一份 prompt，是第 6 節那張填滿的表 ＋ 第 7 節被推翻的項目清單。**

依序：
1. 把被推翻的主張從 `PHOTO_DIRECTION_STANDARD.md`、`SEXY_SCENE_LIBRARY.md`、
   `AI_PROMPT_METHOD_REVIEW.md` 裡**刪掉**（不是改成另一個數字——那又是在用一套硬公式換另一套）
2. 把驗證有效的控制桿寫成 Layer C 的 prompt 骨架
3. **才**回頭改 `GENERATION_PLAN_B1.md` 那 20 件 spec
4. 才開始跑正式素材

> **提醒自己**：這份測試會得到「哪些控制桿有效」，不會得到「一條萬用公式」。
> 如果跑完之後我又寫出一套「每張都要 XXmm、每張都要 OO 站姿」的表，
> 那就是外部覆核指出的同一個錯誤犯第三次。
> 有效的控制桿是**可以選用的工具**，不是**每張都要套的模板**——
> 套死了，版面就會回到「規則太死、看起來很假」的老問題。
