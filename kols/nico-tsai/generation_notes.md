# Nico Tsai 蔡妮可 — Generation Notes

> **這份檔案是按時間累加的歷程紀錄，越前面越舊。**
> **不要拿前面的章節當現行規格**——早期章節裡的三圍（86-59-88／C）、髮色（冷灰奶茶漂色，無銀灰挑染）、
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

## 狀態：**訓練中 — Phase A/B/C 完成，Soul 訓練已送出**

建立日期：2026-08-27（Batch 3）

| 階段 | 狀態 |
|------|------|
| 選角（candidate 生成與挑選） | ✅ Round 3 通過，選定 candidate_03 |
| Reference Element 錨定 | ✅ `68ff990e-1862-4003-bfe3-fe288275cdd4` |
| 訓練集（20 張） | ✅ 2026-08-28 完成並驗收 |
| Soul 訓練 | 🔵 2026-08-28 送出訓練，`soul_id` `46d1e11e-92a7-4fd7-8776-dcd4e2067627` |
| 首批內容生成 | ⬜ 未執行 |

**Soul ID**：`46d1e11e-92a7-4fd7-8776-dcd4e2067627`

---

## 生成前必檢清單

1. **PERSONA_CANON.md 五條原則** — 反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源。
2. **身分一致性硬規格**（每一次 prompt 都要寫）：
   - 膚色：Fair, luminous, porcelain-toned skin — NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-colored. East Asian features (Taiwanese / Chinese / Korean / Japanese leaning), NOT Southeast Asian-leaning features.
   - 身材：167cm / **90-59-88 / D 罩杯**（U-03 使用者裁決；纖細骨架＋飽滿胸型，不要寫 small bust／NOT heavy-chested 這類把身形推平的否定詞）
   - 選角階段**必須同時核對臉部與身材**——Rainie Hsu 就是只看臉沒核身材，整批訓練圖作廢重做。
3. **髮色髮型每次都要寫**（Soul V2 不繼承）：現行為 **齊下巴短鮑伯 · 冷調中栗棕（mushroom brown，帶灰底），左側鬢角一道銀灰挑染**——單一平染到頭皮、髮根與髮尾同色。單一真理來源為 `pilot/nico_pilot.json` 的 `hair_en` / `hair_color_en`。
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

---

## Phase C 20 張完成 — 使用者驗收（2026-08-28）

**經過**：ChatGPT R14 判定 PASS（14 輪覆核、58 條議題結案 54 條），20 張一次生成完成，
`lint_prompts.py` 20/20、validator exit 0、語意覆核 20/20、跨檔案一致性 ✓。
成本 20 張，累計 35 張。

### 使用者驗收結果

| 項目 | 判定 |
|------|------|
| 臉部一致性 | ✅ **「臉的確從頭到尾都是同一個人」** |
| `a01` 景別漂移（指定 face_closeup 出成 waist_up）| ⭕ **「沒什麼差別，無所謂」**——不重拍 |
| 整體 | ⚠️ **「還是少了一點真人感」**，但**「這 20 張的確可以直接送進 Soul 訓練」** |
| `c08`（浴室鏡前）| ❌ **洗手台下方多出一雙不屬於任何人的赤腳與黑褲腿** |

### 兩個要記住的教訓

**1. `c08` 的多餘肢體是我逐張檢查時漏掉的。**
`SEXY_SCENE_LIBRARY.md` §10 早就要求「生成後逐張檢查多餘肢體」，我也確實逐張看過，
但只掃了主體與大構圖，**沒有掃畫面深處、家具下方、鏡子邊緣**——那雙腳就在洗手台下面。
已把「刻意掃四個角落與家具底下」寫進 §10。
使用者裁決這 20 張不重拍；Soul V2 學的是臉與身形，背景物件被學進去的風險低。

**2. 「少了一點真人感」的根因找到了，而且是可量化的。**
使用者問「怎麼都沒參考小雪莉那個帳號的分析」，查證後：
**20 張裡有 14 張是公共場所（超商、藥妝店、洗衣店、月台、早餐店、街道、公園、咖啡廳），
全部寫成「畫面裡只有她一個人」，0 張有背景路人。**

而 `SEXY_SCENE_LIBRARY.md` §9 早在 2026-08-05 就用 14 張實測把這條規則**反轉**過：
> 空景的台北巷弄、空景的夜市、空無一人的海灘，本身就是最強的「這是合成的」訊號。

**問題不在於這個判斷本身**——訓練集確實不該有第二個人（會被學進身分），
ChatGPT 的 C-42／C-46 也是往這個方向推的，那是對的。
**問題在於我不知道有這條規則，於是把它當成一個普遍原則做完了全部 20 張，
而不是記成一個「訓練集專屬的例外、Soul 訓練完成後要立刻切回來」的決定。**

已寫入：
- `SEXY_SCENE_LIBRARY.md` §9 新增 **(b-例外) 建模訓練集**，並記錄本次事故
- `KOL_TRAINING_SOP.md` 新增〈**訓練集 vs 日常素材：兩套不同的規則**〉七項對照表，
  以及「下一個角色開始生成日常素材前必讀 `COMPETITOR_sherry_digitalp510.md`」的五條對照清單

**使用者指示**：這 20 張不改；**下一個角色的日常素材要參考小雪莉的分析**，
尤其是她日常發布的素材照片。建模階段仍以「臉能被模型穩定辨識」為最優先。

---

## Soul 訓練送出 — 2026-08-28

**soul_id**：`46d1e11e-92a7-4fd7-8776-dcd4e2067627`（name: `nico-tsai`, type: `soul_2`）
**訓練圖**：`images/training_v1/` 全部 20 張，以 image job id 直接送入（不需重新上傳）。
**狀態**：送出時 `queued` → `training`，約 10 分鐘。

| 檔案 | image job id |
|------|--------------|
| 01_a01 | `e7b71e33-d384-4690-9efb-12dd224751e7` |
| 02_a02 | `04cf64bc-fa3c-459c-8fdd-8891b2ea08d2` |
| 03_a03 | `3f351447-21d7-46ae-9056-215cdd1d9935` |
| 04_a04 | `c7b29f08-2dc2-48ee-8921-dbc58cfcee77` |
| 05_a05 | `bee22e06-b9ec-4f69-8c9b-6ccb7a1da684` |
| 06_a06 | `0d186f7f-ff1a-4ddc-8a83-f7957434ede2` |
| 07_a07 | `0e0d7d06-3427-4c7a-a130-f06d191b70cc` |
| 08_c01 | `c026304f-531e-46a1-a0e6-21f6637c4b10` |
| 09_c02 | `a90a8119-ee38-4610-8eac-24111abfd03e` |
| 10_c03 | `23528447-4c6d-4c56-bc6b-9ce557e1a3eb` |
| 11_c04 | `05abdd6a-ef6f-4aea-af19-3ac4ded7bbaf` |
| 12_c05 | `e3136069-6362-499c-991a-eccb0e27d51d` |
| 13_c06 | `f3d53c2e-1851-490a-b0f3-9b2b623ee4ea` |
| 14_c07 | `c4863316-a474-4807-b24b-896b66081b0e` |
| 15_c08 | `668c0eee-9a02-46a6-bcb7-51b60c43e08f` |
| 16_c09 | `a4265212-28b2-484a-9d09-6879f12ecaca` |
| 17_c10 | `b55bc844-4013-4b27-a0e4-ddb9dfa6e029` |
| 18_c11 | `328c9d14-ac5c-4b0e-940d-958823a2fff4` |
| 19_c12 | `6de1a33c-aa96-4a65-8566-f4db487d6ede` |
| 20_a08 | `c38af964-7aee-4e38-9bbd-853b015d58a5` |

**要記的操作細節**：生成完成的圖，其 job id 直接寫在 PNG 的 `hf-job-id` tEXt chunk 裡，
`show_characters(action='train')` 的 `images` 直接吃 image job id，
**不必**走 `media_upload → PUT → media_confirm`。下一個角色照這條路走。

**c08 一併送訓**：使用者裁決 20 張不重拍。洗手檯下的多餘肢體是背景物件，
Soul V2 學的是臉與身形；若訓練後在 Phase D 出現不明肢體，回頭把 c08 抽掉重訓（剩 19 張仍在 5–20 範圍內）。
