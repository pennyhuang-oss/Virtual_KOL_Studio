# 議題帳本 — Nico Pilot

> **這是覆核狀態的唯一真理來源。** 操作方式見 [`review/README.md`](README.md)。
> 最後更新：2026-08-28　|　覆核基準：`8b6e0a5`　|　R4 已合併，待 Claude 修正
>
> **全部議題結案前，不得進入生成階段。**

## 目前進度

| 輪次 | 由誰 | 內容 | 檔案 |
|------|------|------|------|
| R1 | ChatGPT | 對 Batch 3 建模照計畫的對抗性複核 | （原始 MD，已消化）|
| R2 | Claude | schema v2 + validator v2 + Nico pilot | `review/rounds/` |
| R2' | ChatGPT | 對 R2 的複核 | （原始 MD，已消化）|
| R3 | Claude | 訓練集重構 7 anchor + 12 lifestyle | [`rounds/R3_nico_pilot_claude.md`](rounds/R3_nico_pilot_claude.md) |
| **R4** | **ChatGPT** | **已覆核，待 Claude 修正** | 本輪結論直接記於本帳本 |

---

## 議題總表

ID 規則：`C-nn` = ChatGPT 提出，`K-nn` = Claude 提出，`U-nn` = 需使用者裁決

| ID | 議題 | 提出者 | 狀態 | 備註 |
|----|------|--------|------|------|
| C-01 | scene 與 outfit_id / hair_id 雙重真理來源 | ChatGPT | ✅ 結案 | v2 schema + validator 正則攔截 |
| C-02 | row fingerprint（欄位綁列號）| ChatGPT | ✅ 結案 | 禁止任何欄位與列號綁定 |
| C-03 | A/B/C 層級被 quota 硬湊 | ChatGPT | ✅ 結案 | 改由 location_registry 決定 |
| C-04 | Phase A 假設 4 次呼叫是同一人 | ChatGPT | ✅ 結案 | 改為 4 個候選 identity |
| C-05 | 訓練集 harsh light 比例過高（L1 5/13）| ChatGPT | ✅ 結案 | 實算確認 3/19（15.8%）；極端下打光已移到 Phase D |
| C-06 | 只有 1 張乾淨全身 / 1 張乾淨臉部特寫 / 0 張乾淨右側 | ChatGPT | ✅ 結案 | 依 validator 的 clean 定義實算確認為 3 / 2 / 2 |
| C-07 | 覆核包統計與 JSON 漂移 | ChatGPT | ⚪ ChatGPT已回應 | 仍有兩處漂移；見下方詳述 |
| C-08 | QA 門檻 14/18 憑空訂且偏鬆 | ChatGPT | ⚪ ChatGPT已回應 | 方向正確，但 benchmark 尚不能重現執行；見下方詳述 |
| C-09 | validator 沒驗 Phase A / B / D | ChatGPT | ⚪ ChatGPT已回應 | 目前只驗少數存在性條件，不足以稱為完整 gate |
| C-10 | signature_family / career_related 是人工 label | ChatGPT | ✅ 結案 | Nico 現有 19 列推導值均一致；override 的縮放缺口另列 C-18 |
| C-11 | 覆核包沒附 registry，validator 無法重現 | ChatGPT | ✅ 結案 | 改用 GitHub 直讀，此問題消失 |
| C-12 | 官方 Soul ID 已改 minimum 20 張 | ChatGPT | ✅ 結案 | 接受專案實際 endpoint schema 為 5–20；不需花 credit 做空 preflight |
| C-13 | identity marker 的 `2mm` 不是模型能穩定執行的單位 | ChatGPT | ⚪ ChatGPT已回應 | 必須在 Phase A prompt 定稿／生成前改，不能延到 pilot 後 |
| C-14 | 19 位只是文件上凍結，沒有機制阻擋 | ChatGPT | ⚪ ChatGPT已回應 | 必須在任何 Nico credit 支出前完成，避免平行流程誤生成 |
| C-15 | `schema_v2.json` 未被實際執行，validator 可放過非法 enum / 空 props | ChatGPT | 🔵 Claude已修正 | **已用對抗測試複現並修好**：validator 現在逐列比對 schema 的 required/enum/minItems，注入 4 個違規全數抓到 |
| C-16 | clean anchors `nico_a01` / `nico_a02` 的 scene 與 body_pose 衝突 | ChatGPT | 🔵 Claude已修正 | **已確認並修好**：body_pose 改 seated；validator 新增姿態衝突檢查（scene 說坐/站/蹲/躺與欄位不符即報錯）|
| C-17 | Phase D stress spec 仍是不可重現的自然語言選單 | ChatGPT | ⚪ ChatGPT已回應 | st09a/b 各塞多個髮型選項，且 rubric 適用範圍未結構化 |
| C-18 | label override 可繞過 registry 推導並壓低 quota 計數 | ChatGPT | ⚪ ChatGPT已回應 | 任意一個 reason 即同時放行兩欄；persona #2 前修 |
| K-01 | validator 的 scene 衝突是 keyword guard 不是語意理解 | Claude | ⚪ ChatGPT已回應 | 同意定位為 heuristic lint，但須加入強制語意覆核 gate；本輪已抓到 a01/a02 衝突 |
| K-02 | `nico_outfit_01` 佔 7/19（37%），比 R2 被指出的 30.8% 更高 | Claude | ⚪ ChatGPT已回應 | 保留 4 張 anchor 的控制組價值；改掉至少 2/3 張工作室重複穿搭 |
| K-03 | 家＋工作室仍佔 42%，但 anchor 全在外面 | Claude | ⚪ ChatGPT已回應 | 不夠：在 lifestyle 子集是 8/12=66.7%，模型不會依 pillar 自動降權 |
| K-04 | 19 張是否應補滿 20 | Claude | ⚪ ChatGPT已回應 | 建議補第 20 張：clean profile_right＋新 body-readable outfit＋中性外部 B 場景 |
| K-05 | 跨 persona row fingerprint 檢查未實作 | Claude | ✅ 結案 | 同意延後；但必須在 persona #2 進 Phase C 前完成，不阻擋 Nico pilot |
| U-02 | ChatGPT 讀 GitHub 一次燒光 5 小時用量 | Claude | ✅ 結案 | 協定改為自帶內容的覆核請求（`tools/gen_review_request.py`），ChatGPT 不 fetch，只讀訊息本身 |
| U-01 | Retroactive Benchmark 的 baseline 選誰 | Claude | ✅ 結案 | 使用者裁決：GOOD=Iris Chen `5fe3b6ba`，KNOWN_BAD=Rainie v1 `994e33d2`（已棄用）|

**狀態圖例**：⚪ 待對方回應／ChatGPT已回應　🔵 Claude已修正（待對方確認）　🟡 待處理　🔴 有爭議　🟣 需使用者裁決　✅ 結案

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


---

## R4｜ChatGPT 實測覆核（2026-08-28）

### 已確認結案：C-05、C-06、C-10、C-12、K-05

- 實跑 `python3 tools/validate_shoot_plan_v2.py pilot/nico_pilot.json`：目前原檔輸出 `✓ 全數通過`。
- 獨立重算：L1 = 3/19；clean full-body / face-closeup / right-side = 3 / 2 / 2。
- Nico 現有列的 `signature_family` / `career_related` 與 registry 推導一致。
- C-12：接受本專案實際 MCP endpoint schema 的 5–20 契約，加上既有 13 張成功紀錄，證據足夠；不用為了規格爭議先送一次會花 credit 的訓練請求。執行當下仍應記錄 endpoint 回應。
- K-05：跨 persona fingerprint 需要至少兩位資料才有檢測價值，同意延後，但要列為 persona #2 的前置 gate。

### C-07｜統計仍與 JSON 漂移

1. `phase_d_stress_test.dominant_training_outfit` 寫 `nico_outfit_08 = 4/19`，但 JSON 實算主導穿搭是 `nico_outfit_01 = 7/19`。
2. K-03 詳述寫 anchor 分布「咖啡廳 2、人行道 3、公園 3」，合計 8；實際 7 張是 2 / 2 / 3。

**要求**：不要只讓 R3 報告由 generator 產生；所有嵌在 JSON 與 LEDGER 的衍生統計也要由同一計算函式產生或由 validator 反算比對。修正前 C-07 不結案。

### C-08｜Retroactive Benchmark 方向正確，但方法尚未封口

保留 GOOD=Iris、KNOWN_BAD=Rainie v1 的決策，但需補四件事：

1. **ground truth 定義**：Rainie v1 若拿自己的錯誤 anchor 當真理，body consistency 可能很高；`body_identity` 必須明寫是對「persona 目標身材／核准 reference」評分，而不是只看同一個錯誤 soul 是否自洽。
2. **persona-adapted 等價測項**：現有 Phase D 含 Nico outfit、Nico 右鼻翼痣與 Nico 身材敘述，不能原字套用 Iris/Rainie。應固定測試難度與變量類型，各 persona 換成自己的 approved outfit / marker / body target。
3. **評分聚合**：需明寫每個 rubric item 是整套只評一次，還是逐 shot 評分後如何聚合；目前 18 分母與 per-shot hard gate 混在一起。
4. **隨機性控制**：至少對 st00–st05、st10 做固定 seed（若支援）或重複樣本；單張輸出不足以區分 soul 品質與抽樣波動。

### C-09｜Phase A / B / D gate 仍過薄

目前 validator 只檢查：

- A：count、framing、DOF、outfit 是否 body-readable / 有 neckline；
- B：B1/B2 是否存在、B2 是否 full-body；
- D：count、st00 是否存在、是否有 hard_gates。

它沒有驗 A 四候選是否除 identity 外完全同規格、B2 是否真的更換場景／穿搭／髮型／光線，也沒有驗 D 的 ID 唯一性、必測項、條件依賴與結構欄位。應把 README/R3 宣稱的 gate 逐條轉成機器條件，否則「已補 gate」不能結案。

### C-13 / C-14｜生成前必做

- C-13：把 `2mm` 改為相對、可視語句，並補 1–2 個不依賴左右方向的骨相 marker。此改動會影響 Phase A prompt，所以正好應在 prompt 定稿前完成。
- C-14：為其餘 19 位加入機制性 blocked status，並讓執行入口拒絕非 Nico 的 v1 流程。這不是 pilot 後的優化，而是避免覆核期間誤花 credit 的保護。

### C-15｜schema v2 目前不是可執行的真理來源

我做了對抗測試：把第一列的 `purpose` 改成非法值、`head_pitch` 改成 `IMPOSSIBLE`、`props` 改成空陣列，再直接呼叫 validator；結果仍是 **0 errors / PASS**。

原因有兩層：

- validator 沒有載入 `schema_v2.json`；
- `schema_v2.json` 只有 `definitions.shot`，頂層沒有把 `phase_c_shots.items` 連到 `#/definitions/shot`，即使另跑一般 JSON Schema validator，也不會自動驗整份 pilot。

**要求**：讓完整 pilot schema 以 `$ref` 約束 shots，並由主 validator 實際執行；至少補 required、enum、props minItems、additionalProperties 策略與 shot_id 唯一性。這是 20 人規模化前的 P0，也應在 Nico 生成前修掉。

### C-16 / K-01｜語意 lint 已在真資料漏抓矛盾

- `nico_a01.scene` 明寫「靠窗的位子**坐著**」，但 `body_pose = standing`。
- `nico_a02.scene` 承接「同一個位子」，仍為 `standing`；至少語意含糊，且 R3 表格也沒有揭露這個衝突。

同意 regex 只能定位成 heuristic lint，不要求無限補詞。正式 gate 應是：機器 lint PASS 後，再跑一次逐列的結構—自然語言語意覆核；結果需留下可追溯 checklist。先修 a01/a02。

### K-02｜同穿搭控制組有價值，但 7/19 不是都由 anchor 造成

實際分解：

- 7 張 anchor 中，`outfit_01` 只有 4 張，另 3 張是 `outfit_03`；
- 另外 3 次 `outfit_01` 來自工作室 c01/c02/c07，而且同時都綁 `workplace_own_studio + hair_03`。

因此可保留 4 張 anchor 的控制組；但工作室三張至少換掉兩張穿搭，避免「人＋職業空間＋工作髮型＋職人服」四重綁定。第 20 張也不要再用 outfit_01。

### K-03｜42% 緩解仍不足

整體是 8/19，但排除 7 張外部 anchor 後，home + workplace 在 lifestyle 子集其實是 **8/12 = 66.7%**。訓練 endpoint 不知道 `pillar=anchor`，也沒有證據顯示它會自動把 clean anchor 權重拉高到足以抵銷 8 張世界重複。

建議至少把 2 張 home/work lifestyle 換成一般外部 B/C 場景，並在 validator 同時限制：

- 全體 home+work ratio；
- lifestyle 子集 home+work ratio；
- `location + outfit + hair` 固定組合重複數。

### K-04｜補滿 20，但補的是缺口，不是湊數

建議第 20 張規格：乾淨自然光的 `profile_right`（目前完全沒有）、chest-up 或 waist-up、使用尚未進訓練集的 body-readable outfit（優先 `nico_outfit_02`，不要 outfit_01）、中性外部 B 場景。這同時：

- 消除 19/20 的 endpoint 歧義；
- 補右側完整輪廓；
- 降低主導穿搭與 home/work 比例；
- 增加第 7 種穿搭。

### C-17｜Phase D 仍不可重現

`st09a` 一列同時寫「短髮全後／濕髮／bob 外翹／half-up」，`st09b` 又寫「長髮接髮或高馬尾」。一個 shot 不能同時測多個髮型，執行者若臨場選一個，benchmark 就不再可重現。

把每個 stress shot 改為結構化單一變量，至少包含：`id`、固定 prompt 欄位、唯一 test_variable、expected invariant、applicable rubric items、seed/replicate 規則。若拆成多 shot，需同步更新 count、成本與 benchmark procedure。

### C-18｜override 仍能逃過 quota

目前只要任意填一個 `label_override_reason`，就能同時放行 `signature_family` 與 `career_related` 的不一致；後面的比例又直接數使用者填的值。因此有理由字串的錯誤 override 仍可把 signature/career 比例壓低。

Nico 現況沒有 override，所以 C-10 可結案；但 persona #2 前應改成兩欄各自的 override + reason，quota 一律計算「registry 推導或已核准 override」的 effective value。
