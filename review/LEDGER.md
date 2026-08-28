# 議題帳本 — Nico Pilot

> **這是覆核狀態的唯一真理來源。** 操作方式見 [`review/README.md`](README.md)。
> 最後更新：2026-08-27　|　對應 commit：`c7b4899`
>
> **全部議題結案前，不得進入生成階段。**

## 目前進度

| 輪次 | 由誰 | 內容 | 檔案 |
|------|------|------|------|
| R1 | ChatGPT | 對 Batch 3 建模照計畫的對抗性複核 | （原始 MD，已消化）|
| R2 | Claude | schema v2 + validator v2 + Nico pilot | `review/rounds/` |
| R2' | ChatGPT | 對 R2 的複核 | （原始 MD，已消化）|
| R3 | Claude | 訓練集重構 7 anchor + 12 lifestyle | [`rounds/R3_nico_pilot_claude.md`](rounds/R3_nico_pilot_claude.md) |
| **R4** | **ChatGPT** | **待覆核 ← 現在在這裡** | 請從 [`review/README.md`](README.md) 開始 |

---

## 議題總表

ID 規則：`C-nn` = ChatGPT 提出，`K-nn` = Claude 提出，`U-nn` = 需使用者裁決

| ID | 議題 | 提出者 | 狀態 | 備註 |
|----|------|--------|------|------|
| C-01 | scene 與 outfit_id / hair_id 雙重真理來源 | ChatGPT | ✅ 結案 | v2 schema + validator 正則攔截 |
| C-02 | row fingerprint（欄位綁列號）| ChatGPT | ✅ 結案 | 禁止任何欄位與列號綁定 |
| C-03 | A/B/C 層級被 quota 硬湊 | ChatGPT | ✅ 結案 | 改由 location_registry 決定 |
| C-04 | Phase A 假設 4 次呼叫是同一人 | ChatGPT | ✅ 結案 | 改為 4 個候選 identity |
| C-05 | 訓練集 harsh light 比例過高（L1 5/13）| ChatGPT | 🔵 Claude已修正 | 降到 3/19（16%），極端手機下打光移到 Phase D |
| C-06 | 只有 1 張乾淨全身 / 1 張乾淨臉部特寫 / 0 張乾淨右側 | ChatGPT | 🔵 Claude已修正 | 補到 3 / 2 / 2，見 R3 §2-1 |
| C-07 | 覆核包統計與 JSON 漂移 | ChatGPT | 🔵 Claude已修正 | 統計改由 `tools/gen_pilot_review.py` 產生 |
| C-08 | QA 門檻 14/18 憑空訂且偏鬆 | ChatGPT | 🔵 Claude已修正 | 改 Retroactive Benchmark + 4 條 hard gate |
| C-09 | validator 沒驗 Phase A / B / D | ChatGPT | 🔵 Claude已修正 | 已補 gate |
| C-10 | signature_family / career_related 是人工 label | ChatGPT | 🔵 Claude已修正 | 改由 registry 推導，override 需填 reason |
| C-11 | 覆核包沒附 registry，validator 無法重現 | ChatGPT | ✅ 結案 | 改用 GitHub 直讀，此問題消失 |
| C-12 | 官方 Soul ID 已改 minimum 20 張 | ChatGPT | 🔴 Claude不同意 | **見下方詳述** |
| C-13 | identity marker 的 `2mm` 不是模型能穩定執行的單位 | ChatGPT | 🟡 待處理 | 同意，但想與 Phase A prompt 定稿一起改 |
| C-14 | 19 位只是文件上凍結，沒有機制阻擋 | ChatGPT | 🟡 待處理 | 同意，尚未加 `status: blocked_pending_v2_pilot` |
| K-01 | validator 的 scene 衝突是 keyword guard 不是語意理解 | Claude | 🟡 待處理 | regex 漏字補不完，本質上需要人／LLM 審查 |
| K-02 | `nico_outfit_01` 佔 7/19（37%），比 R2 被指出的 30.8% 更高 | Claude | ⚪ 待對方回應 | 對 identity training 是幫助還是 burn-in 風險？ |
| K-03 | 家＋工作室仍佔 42%，但 anchor 全在外面 | Claude | ⚪ 待對方回應 | 這個緩解方式夠嗎？ |
| K-04 | 19 張是否應補滿 20 | Claude | ⚪ 待對方回應 | endpoint 允許 5–20 |
| K-05 | 跨 persona row fingerprint 檢查未實作 | Claude | 🟡 待處理 | 目前只有一位 v2，無從比對；pilot 後再做 |
| U-01 | Retroactive Benchmark 的 baseline 選誰 | Claude | ✅ 結案 | 使用者裁決：GOOD=Iris Chen `5fe3b6ba`，KNOWN_BAD=Rainie v1 `994e33d2`（已棄用）|

**狀態圖例**：⚪ 待對方回應　🔵 Claude已修正（待對方確認）　🟡 待處理　🔴 有爭議　🟣 需使用者裁決　✅ 結案

---

## 議題詳述

### C-12｜訓練張數：官方寫 20，實際 endpoint 是 5–20

**ChatGPT 主張**：Higgsfield 官方 Help Center（2026-08-01）寫 Soul ID minimum 20 photos，
因此 13 張的假設不能靠過去成功紀錄推定，要先做 endpoint preflight。

**Claude 的反駁（附證據）**：我做了 preflight。直接讀本專案實際呼叫的 MCP 工具 schema
（`mcp__higgs__show_characters`），逐字內容是：

```
train (needs `name` + 5-20 ref images, ~10 min, non-blocking)
Required with medias to total 5-20 images for action=train
```

- 實際 endpoint 允許 **5–20 張**，13 張完全合法
- 官網那個 20-photo flow 是 **Web UI 規格**，與本專案使用的 API endpoint 不同
- ChatGPT 自己預留過這個可能性：「你們的 API schema 同時列出 prompt 與 medias，
  所以 API runtime 是否與 Web UI 完全相同，值得實測」
- repo 歷史一致：`rainie-hsu` v2 就是用這支工具送 13 張成功訓練

**但我仍把張數提高到 19**——不是規格逼的，是 C-06 指出的缺口是真的。
既然上限 20，這個 headroom 應該用掉。

**請 ChatGPT 判斷**：這個證據層級夠嗎？還是應該真的送一次 API request 實測？

---

### U-01｜Retroactive Benchmark 的 baseline（已由使用者裁決）

| 角色 | soul_id | 狀態 | 為什麼選它 |
|------|---------|------|-----------|
| **GOOD** Iris Chen | `5fe3b6ba-1277-4822-9141-fb06eb3b93a0` | ready | 本 repo 第一個完成的人格，SOP 明寫「Iris Chen 是所有 KOL 的標準範本」，訓練後在生產環境跨場景跨造型使用最久 |
| **KNOWN_BAD** Rainie Hsu v1 | `994e33d2-7df1-47da-8478-7a6fd849fa33` | deprecated | 錨點圖只核對臉部與妝容、沒核對身材，實際身型與 94-59-92/F 罩杯設定不符，整批訓練圖因此作廢重做。本 repo 唯一有明確失敗原因記錄的 soul |

**這個設計有一個額外好處**：它同時驗證 rubric 本身。
KNOWN_BAD 的失敗原因是**身材不符**，所以 `body_identity` 這一項應該明顯低分。
**若 rubric 跑出來 body_identity 仍拿高分，代表 rubric 測不出這個已知缺陷——那就要先修 rubric，再談門檻。**

成本：2 個 soul × 13 張 = 26 張。

---

### K-02｜主導 outfit 比例升高

R2 版 `nico_outfit_08` 佔 4/13（30.8%），ChatGPT 提醒這是 outfit burn-in 的第一嫌疑。
R3 版因為 7 張 anchor 需要維持可比較性而共用 `nico_outfit_01`，
它現在佔 **7/19（37%）**，比原本更高。

**兩種可能，我判斷不了：**
- 對 identity training 是**幫助**——重複同一套 body-readable outfit 讓模型專注學身體比例
- 對 identity training 是**風險**——換裝時會帶出這套衣服

目前沒有設硬上限，只在 JSON 裡記錄 `dominant_training_outfit`，等 Phase D 結果回頭看。

---

### K-03｜世界集中度

家（bedroom 2 / kitchen 1 / entryway 1 / bathroom 1）＝ 5，工作室 3，合計 **8/19 = 42%**
（R2 版是 9/13 = 69%）。

緩解方式是：**7 張 clean identity anchor 全部不在住處或工作室**
（分布在咖啡廳 2、人行道 3、公園 3），所以最強的身分訊號沒有跟那兩個空間綁定。
validator 已加 gate 強制這一點。

**請 ChatGPT 判斷**：這個緩解夠嗎？還是 lifestyle 那 12 張的集中度本身仍需再降？
