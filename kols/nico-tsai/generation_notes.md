# Nico Tsai 蔡妮可 — Generation Notes

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
   **修法**：景別搬到 prompt **最前面**（不是最後），並改用排他性措辭：
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
