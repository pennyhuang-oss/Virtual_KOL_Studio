# Nico Tsai 蔡妮可 — Generation Notes

> **這份檔案是按時間累加的歷程紀錄，越前面越舊。**
> **不要拿前面的章節當現行規格**——早期章節裡的三圍（86-59-88／C）、髮色（冷灰奶茶漂色）、
> 以及 Round 1 記下的「景別用排他性措辭」修法，**都已被後續實測推翻或由使用者改版**。
>
> | 要找什麼 | 現行真理來源 |
> |---------|------------|
> | 完整規格（臉、身材、髮色、衣櫃、20 張訓練集）| [`../../pilot/nico_pilot.json`](../../pilot/nico_pilot.json) |
> | 人設敘述 | [`profile.json`](profile.json)、[`character.md`](character.md) |
> | 會送進模型的 prompt | [`../../pilot/phase_c_prompts.json`](../../pilot/phase_c_prompts.json) |
> | 模型的實測行為 | [`../../KOL_TRAINING_SOP.md`](../../KOL_TRAINING_SOP.md)〈這個模型的實測行為〉|

> ⚠️ **本檔案受 [`PERSONA_CANON.md`](../../PERSONA_CANON.md)（人設憲章）約束。**
> 憲章定義了反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源五條原則，並優先於本檔案中任何相衝突的敘述。
> 內容支柱的名稱與比重以 `profile.json` 為單一真理來源。

---

## 狀態：**PENDING — 尚未執行任何生成**

建立日期：2026-08-27（Batch 3）

| 階段 | 狀態 |
|------|------|
| 選角（candidate 生成與挑選） | 🔶 第一輪已生成，**已否決**（見下方記錄） |
| Reference Element 錨定 | ⬜ 未執行 |
| 訓練集（13 張） | ⬜ 未執行 |
| Soul 訓練 | ⬜ 未執行 |
| 首批內容生成 | ⬜ 未執行 |

**Soul ID**：尚未取得

---

## 生成前必檢清單

1. **PERSONA_CANON.md 五條原則** — 反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源。
2. **身分一致性硬規格**（每一次 prompt 都要寫）：
   - 膚色：Fair, luminous, porcelain-toned skin — NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-colored. East Asian features (Taiwanese / Chinese / Korean / Japanese leaning), NOT Southeast Asian-leaning features.
   - 身材：167cm / 86-59-88 / C 罩杯
   - 選角階段**必須同時核對臉部與身材**——Rainie Hsu 就是只看臉沒核身材，整批訓練圖作廢重做。
3. **髮色髮型每次都要寫**（Soul V2 不繼承）：現階段為 冷灰奶茶（漂色）· 短鮑伯。
4. **SEXY_SCENE_LIBRARY.md**〈降低「AI 感」的技術要點〉五項全部套用。
5. **標誌性配額**：露背 / 絲質吊帶 + 指甲特寫的並置 — 每月 1 期。

---

## 生成紀錄

### 2026-08-27 第一輪選角（Round 1）— ⚠️ 已否決，需修正 prompt 重跑

**目的**：Batch 3 的流程驗證批次。5 位驗證名單中先跑 Nico 一位，因為她是「C 罩杯纖細對照組 + 冷灰奶茶短鮑伯」，
是最容易失敗的一位（模型傾向把所有人畫成豐滿、把漂色畫成銀白）。

**模型**：`seedream_v4_5`（**不是** `soul_2`）。
依 `kols/rainie-hsu/generation_notes.md` 的實證：soul_2 在沒有 soul_id 錨定時每次呼叫都會重新想像一張臉，
四張根本不像同一個人。本輪確認 seedream_v4_5 的臉部一致性成立。

**產出**：`images/face_reference/candidate_01–04.png`

| 檔案 | 預期景別 | job_id |
|------|---------|--------|
| candidate_01.png | 正面臉部特寫 | `4c69edc0-bcb7-420f-ad30-0ff17a592b08` |
| candidate_02.png | 正面半身 | `a7acf61a-0cc1-4478-ba2b-b18acded0a90` |
| candidate_03.png | 四分之三側半身 | `9bd0340a-e59a-4809-b819-818e1ba43a23` |
| candidate_04.png | 全身 | `291a4b4f-9a4f-4229-92dc-fcf012565841` |

**守住的**：
- ✅ 臉部一致性 — 四張是同一個人，證實 seedream_v4_5 是正確選擇
- ✅ 白皙冷調膚色 — 沒有被帶往小麥／古銅
- ✅ 短鮑伯 — 沒有自動加長
- ✅ 真實膚質 — 毛孔、雀斑、鎖骨的痣都在，非塑膠感

**否決原因（四項，全部是 prompt 設計問題，不是模型問題）**：

1. **`[LIGHTING]` 的具名器材被當成場景道具畫進畫面。**
   prompt 寫了 `white foam board just out of frame camera-right`、`tungsten practical lamp`、
   `shot just past the edge of an open doorframe` — 出圖把泡棉板、攝影棚燈、門框全部畫出來，
   candidate_01 連相機都入鏡。`just out of frame` 這個指令模型不遵守。
   **根因**：`SEXY_SCENE_LIBRARY.md` 的五段式物理光公式是為**真實生活場景**設計的
   （窗光、水面反射、霓虹燈），硬套在「攝影棚」設定上，那些具名器材就變成畫面內容。
   **修法**：選角照改用她自己的工作室作為場景，讓具名光源是那個空間本來就有的東西
   （落地窗、白牆反射、工作燈），器材就不會突兀。

2. **鏡頭景別指令完全無效。**
   candidate_01 指令是 `tight front-facing headshot, head and shoulders only`，出圖卻是接近全身。
   `rainie-hsu` 第一輪也記錄過同樣問題（candidate_04 全身變半身）——這是**重複發生**的已知缺陷。
   **修法（⚠️ 2026-08-28 實測推翻，見本檔 Round 2 章節）**：景別搬到 prompt **最前面**（不是最後），並改用排他性措辭：
   `extreme close-up portrait, her face fills the entire frame, nothing below the collarbone is visible`。

3. **髮色偏離設定。** 設定是「冷灰奶茶」，出圖是銀白色。
   **根因**：`bleached` 這個詞把顏色一路推到白金。
   **修法**：拿掉 `bleached`，改為
   `a light milk-tea brown with a cool greige cast — clearly still a brown, NOT silver, NOT white, NOT platinum`。

4. **領口漂移導致身材判讀失真。**
   prompt 只寫 `fitted ribbed knit long-sleeve top`，沒寫領型，模型自己補了大 U 領低胸，
   candidate_01 的胸型因此讀起來明顯超過 C 罩杯設定。
   **修法**：明確寫 `high crew neckline`。這也呼應 rainie-hsu v2 的教訓——
   身材規格必須在 prompt 本體寫死，而且不能讓服裝細節留白。

**下一步**：修正上述四點後**只重跑 Nico 一位**確認修法有效，再放行其餘 4 位驗證名單
（yerin-han、angeline-kwee、kanon-komori、wendy-yeo）。
本輪**沒有**建立 Reference Element、**沒有**呼叫 `show_characters(action='train')`，
`profile.json` 的 soul_id 維持 PENDING。

---

## Batch 3 · Phase A Round 2 — 2026-08-28（規劃通過 gate 後的第一次生成）

**前置狀態**：`tools/validate_shoot_plan_v2.py` exit 0、語意逐列覆核 20/20（ChatGPT R5–R9）、
對抗測試 26/26。也就是說：**計畫層的 QA 全綠，出圖仍然全錯**——
規劃 gate 管的是「這個計畫成不成立」，管不到「prompt 送進模型會被怎麼解讀」。這是兩層不同的東西。

**成本**：6 張（4 張首批 + 2 張單張探針），約 6.5 credits。

### 首批 4 張：全數不合格，五個缺陷同時出現

| 缺陷 | 說明 |
|------|------|
| **景別完全失效** | 指定 knee_up，4/4 出全身含鞋。**這是第三次**（rainie-hsu R1、nico R1、本輪）。R1 記的修法「景別搬到第一行＋排他性措辭」**無效** |
| **髮色 ombré** | 深棕髮根 → 金／白髮尾。R1 拿掉 `bleached` 解決了「整頭銀白」，但模型改成有髮根的漸層 |
| **服裝漂移成短版** | 4/4 露腰。prompt 從未寫 cropped |
| **身體轉開** | 寫 "turned about 30 degrees toward her own left"，模型解讀成**背對鏡頭**，正面軀幹讀不到——Phase A 的目的直接失效 |
| **拍攝裝置入鏡** | candidate_02 畫進一隻手拿著手機。與 R1「棚燈入鏡」同一類 |

### 根因：**這個模型不執行否定句**

`nothing below the knee is visible`／`NOT a crop top`／`no ombré`／`NOT a full-length shot`
全部無效。有效的是**正面描述目標狀態**：

| 失效寫法（否定） | 有效寫法（正面描述） | 結果 |
|-----------------|-------------------|------|
| `nothing below the knee is visible` | `the bottom edge of the picture cuts straight across her thighs, roughly a hand's width above the knee` | ✅ 景別修正 |
| `NOT a crop top, no exposed midriff` | `the hem is long and tucked into her trouser waistband` | ✅ 服裝修正 |
| `no ombré, no dark roots, no lightened tips` | `a single flat salon dye job done right down to the scalp: the hair at her parting and roots is exactly the same medium brown as the hair at the ends` | ✅ 髮色修正 |
| `her back is not toward the camera` | `her chest and hips are turned only slightly so the front of her body stays fully visible to the lens` | ✅ 朝向修正 |

**這條規則要寫進 SOP**：seedream 的 prompt 一律用「畫面裡有什麼、邊界切在哪裡」描述，
不要用「不要有什麼」。否定詞只在**顏色排除**時有一點作用（`not tanned` 有效），
在**構圖與服裝結構**上完全無效。

### 兩張探針的結果

- **probe_v2**（修景別／服裝／朝向）：景別 ✅、露腰 ✅、朝向 ✅、手機入鏡 ✅；**髮色仍 ombré** ❌、唇色仍濃 ❌
- **probe_v3**（再修髮色／妝）：髮色 ✅ 變成從髮根到髮尾一致的冷調棕，無漸層無金色

### 仍未解決（需使用者裁決）

1. **髮色明度**：設定寫「冷灰奶茶（**漂過的高明度**髮色）」。probe_v3 為了消除漸層，
   顏色被拉到**中等棕**，比設定暗。真正的目標在 v2（有髮根的金）與 v3（均勻中棕）之間。
2. **胸型偏大**：probe_v3 的胸型讀起來仍超過「small natural bust with a shallow curve / C 罩杯」。
   **這正是 rainie-hsu v1 整批作廢的原因**——錨點只核對臉沒核對身材。Phase A 不放行前必須先解決。
3. 唇色仍偏紅（次要）。

**下一步**：這兩項要使用者裁決後才續跑，不自行試錯。

---

## Batch 3 · Phase A Round 3 ＋ Phase B — 2026-08-28

**臉部骨架改版（U-03）**：使用者看到 Round 2 出圖就指出「五官跟 Rainie 太像」。
比對確認屬實——高顴骨、銳利下顎、大而上揚的雙眼皮眼、厚唇有唇珠，是同一組骨架，
也就是 seedream 的預設美女臉。使用者裁決改為**少女短臉型**（見 PERSONA_CANON 原則六）。
胸型由 C 放寬為 D（原本的 small bust / NOT heavy-chested 與使用者偏好不符）。

**選角結果**：4 張候選骨架全部脫離 Rainie。使用者選 **candidate_03**。
Reference Element `68ff990e-1862-4003-bfe3-fe288275cdd4`（nico-tsai-anchor）。

### Phase B：B1 通過，B2 第一次失敗、第二次通過

| | 結果 |
|---|---|
| **B1**（重現） | ✅ 臉完全重現，骨架、痣、下半臉比例一致 |
| **B2 第一次** | ❌ 又拍成背面。全身圖是**身材比例的最終把關點**，背影判不了，作廢 |
| **B2 第二次** | ✅ 正面全身、換場景（公園）＋換穿搭（outfit_03）＋換髮型（hair_02）＋換光線（L6）後身分守住 |

### 兩個必須記錄的發現

#### 1. 「turned about 30 degrees」會被讀成「轉過去背對鏡頭」——連續三次

Round 2 首批、Round 3 的 c01、B2 第一次，全部同一個寫法、同一個結果。
`her back is not toward the camera` 這種否定完全無效（與 Round 2 的結論一致）。

**有效寫法**：不要描述「轉多少度」，要描述**鏡頭看得到什麼**：

> `Her navel, the front of her chest and the front of both shoulders all point toward the camera.
>  Both of her collarbones are visible. The camera sees the front of her jeans — the fly, the button
>  and the front pockets — not the back pockets.`

一次就對。**朝向一律用「相機看得到哪些身體正面特徵」來寫，不要用角度。**

#### 2. Reference Element 會把「服裝以外」的影像細節一起帶走——我先前判斷錯誤

我原本告訴使用者：c03 的露肩開口與髮際灰銀段是服裝／髮型層，錨點只鎖臉與身形，不會傳下去。
**實測結果一半錯**：

- **服裝**：B1 指定同一件炭灰高領毛衣 → 露肩開口原封不動跟著出現，即使 prompt 明寫
  "unbroken and continuous over both shoulders, a complete shoulder seam on each side"。
  B2 指定完全不同的衣服（奶油短版針織）→ 開口消失。
  → **錨點的服裝在「指定同一件衣服」時會被整件複製，指定不同衣服時才會被覆蓋。**
- **髮色**：c03 → B1 → B2 三張全部保留左側那段灰銀挑染，三次 prompt 都明寫
  "a single flat salon dye job … no lighter section anywhere along the strand"。
  → **這一段已經是身分的一部分，prompt 蓋不掉。**

**待使用者裁決**：灰銀挑染要當成 Nico 的造型接受，還是重建乾淨錨點。
