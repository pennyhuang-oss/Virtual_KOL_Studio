# 議題帳本 — Nico Pilot

> **這是覆核狀態的唯一真理來源。** 操作方式見 [`review/README.md`](README.md)。
> 最後更新：2026-08-28　|　**R6 全部判定已處理（8 條結案、1 條再修）＋ 4 條新議題已修，待 R7 覆核**
>
> **全部議題結案前，不得進入生成階段。**

## 目前進度

| 輪次 | 由誰 | 內容 | 檔案 |
|------|------|------|------|
| R1 | ChatGPT | 對 Batch 3 建模照計畫的對抗性複核 | （原始 MD，已消化）|
| R2 | Claude | schema v2 + validator v2 + Nico pilot | `review/rounds/` |
| R2' | ChatGPT | 對 R2 的複核 | （原始 MD，已消化）|
| R3 | Claude | 訓練集重構 7 anchor + 12 lifestyle | [`rounds/R3_nico_pilot_claude.md`](rounds/R3_nico_pilot_claude.md) |
| R4 | ChatGPT | 已覆核，11 條已處理 | 記於本帳本 |
| R5 | ChatGPT | 8 結案 / 5 不同意 / 4 條新議題（C-19–C-22）| [`rounds/R5_chatgpt.md`](rounds/R5_chatgpt.md) |
| R6 | ChatGPT | 8 結案 / 1 不同意 / 4 條新議題（C-23–C-26）| [`rounds/R6_chatgpt.md`](rounds/R6_chatgpt.md) |
| **R7** | **ChatGPT** | **待覆核（含真正的 20/20 九欄語意覆核）** | [`REVIEW.md`](REVIEW.md) |

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
| C-07 | 覆核包統計與 JSON 漂移 | ChatGPT | ✅ 結案 | 移除人工宣告的 `dominant_training_outfit`；validator 反算 `structure`／`shots` 宣告值，並禁止內嵌衍生統計；R5 抓到 `phase_d.known_risk` 與 rubric `cost` 仍是手寫舊值（8/19、42%、7 anchors、2×13=26）。已從 JSON 移除，改由 gen_review_file 與 §5-6 同源現算；render 預算亦改現算；R6 同意結案 |
| C-08 | QA 門檻 14/18 憑空訂且偏鬆 | ChatGPT | ✅ 結案 | 四項封口全補：ground_truth 對 persona 目標評分（非 soul 自洽）、persona-adapted 等價測項、最低分制聚合、st00–st05/st10 各 3 replicate；成本字串已移除改現算；單一變量問題已隨 C-21 一併修正；R6 同意結案（場景測試充分性另列 C-25） |
| C-09 | validator 沒驗 Phase A / B / D | ChatGPT | ✅ 結案 | A 四候選必須固定 10 個欄位且 varies_only=identity；B2 必須真的換場景/穿搭/髮型/光線；D 驗 fixed、rubric item 存在性、depends_on 指向、rubric 全覆蓋；R5 ChatGPT 同意結案（語意層另由 K-01/C-19 處理） |
| C-10 | signature_family / career_related 是人工 label | ChatGPT | ✅ 結案 | Nico 現有 19 列推導值均一致；override 的縮放缺口另列 C-18 |
| C-11 | 覆核包沒附 registry，validator 無法重現 | ChatGPT | ✅ 結案 | 改用 GitHub 直讀，此問題消失 |
| C-12 | 官方 Soul ID 已改 minimum 20 張 | ChatGPT | ✅ 結案 | 接受專案實際 endpoint schema 為 5–20；不需花 credit 做空 preflight |
| C-13 | identity marker 的 `2mm` 不是模型能穩定執行的單位 | ChatGPT | ✅ 結案 | `2mm` 改為相對可視語句，並補 2 個不依賴左右方向的骨相 marker（眼距、鼻頭形狀）；R5 ChatGPT 同意結案 |
| C-14 | 19 位只是文件上凍結，沒有機制阻擋 | ChatGPT | ✅ 結案 | v1 資料標 `blocked_pending_v2_pilot`，v1 validator HARD FAIL exit 2；另建 `pilot/v1_known_issues_report.json`；R5 ChatGPT 同意結案 |
| C-15 | `schema_v2.json` 未被實際執行，validator 可放過非法 enum / 空 props | ChatGPT | ✅ 結案 | schema v2.1 補頂層 + `$ref` 綁 shots + shot_id 唯一性 + additionalProperties；validator 從頂層驗。對抗測試 7/7 抓到；R5 ChatGPT 同意結案 |
| C-16 | clean anchors `nico_a01` / `nico_a02` 的 scene 與 body_pose 衝突 | ChatGPT | ✅ 結案 | a01/a02 body_pose 改 seated；新增姿態衝突檢查，且在後續改動中又抓到 c03；R5 ChatGPT 同意結案（新語意矛盾另列 C-20） |
| C-17 | Phase D stress spec 仍是不可重現的自然語言選單 | ChatGPT | ✅ 結案 | Phase D 改結構化單一變量：每 shot 有 test_variable / expected_invariant / applicable_rubric_items / fixed / replicates / depends_on；Phase D 改三欄拆分：primary_test_variable／required_measurement_changes／held_constant_fields，validator 反算稽核；R6 同意結案 |
| C-18 | label override 可繞過 registry 推導並壓低 quota 計數 | ChatGPT | ✅ 結案 | signature 與 career 各自獨立 override reason；quota 一律以 effective value 計算；R5 ChatGPT 同意結案 |
| K-01 | validator 的 scene 衝突是 keyword guard 不是語意理解 | Claude | ✅ 結案 | 新增 `tools/gen_semantic_checklist.py` 逐列覆核清單 + hash 新鮮度 gate，資料一改舊核可自動失效；C-19：語意覆核未達 20/20 由 warning 改為 HARD FAIL（exit 1）；R6 同意結案（機制層） |
| K-02 | `nico_outfit_01` 佔 7/19（37%），比 R2 被指出的 30.8% 更高 | Claude | ✅ 結案 | 拆掉工作室三張的四重綁定（c01→outfit_08/hair_01、c02→outfit_06/hair_04）；最高佔比降到 5/20=25%，共 8 種；R5 ChatGPT 同意結案 |
| K-03 | 家＋工作室仍佔 42%，但 anchor 全在外面 | Claude | ✅ 結案 | c03→早餐店、c09→超商；全體 30%、lifestyle 子集 50%；validator 加雙層比例上限與三重固定組合檢查；R5 ChatGPT 同意結案（舊風險文字已依 C-07 改為現算） |
| K-04 | 19 張是否應補滿 20 | Claude | ✅ 結案 | 新增第 20 張 `nico_a08`：profile_right + outfit_02（未用過）+ 公園中性外部 B；outfit_02 的「赤腳」與「脫下搭在椅背」是場景狀態不是衣服定義，已移出衣櫃；R6 同意結案 |
| K-05 | 跨 persona row fingerprint 檢查未實作 | Claude | 🟡 待處理 | ChatGPT 同意延後，但列為 persona #2 的前置 gate |
| U-02 | ChatGPT 讀 GitHub 一次燒光 5 小時用量 | Claude | ✅ 結案 | 協定改為自帶內容的覆核請求（`tools/gen_review_request.py`），ChatGPT 不 fetch，只讀訊息本身 |
| C-19 | 語意覆核 0/20 卻仍 exit 0 放行 | ChatGPT | ✅ 結案 | 實測確認：舊版印「⚠ 語意覆核未完成」後仍印「✓ 全數通過」且 exit=0。已改為 HARD FAIL exit 1；對抗測試確認會擋；R6 同意結案 |
| C-20 | Phase C 四個物理／結構矛盾 | ChatGPT | 🔵 Claude已修正 | c01 鐵門遮住的正是落地窗→改側面高窗；c08 修眉＋撐洗手台＋持機＝三隻手→移除撐洗手台且 pose 改 standing；a08/outfit_02 見 K-04。**c04 不同意**：前鏡頭與螢幕同一平面，低頭看螢幕就是看鏡頭，selfie_front + eye_gaze=camera + down_15 三者一致；真正的問題是 props 把手機列為入鏡道具，已移除；R6 裁決：c04 接受 ChatGPT——送進模型的是文字，`looking at phone screen` 與 `looking into the camera` 是兩個指令。保留 eye_gaze=camera，scene 改為「舉起手機直視鏡頭」 |
| C-21 | Phase D 並非真正單一變量，render 數算錯 | ChatGPT | ✅ 結案 | 逐條實測全部屬實，且比指出的更嚴重：st08b 宣稱測下打光但 camera 與基準完全相同、light_family 寫成 L4，被測的東西沒有編碼進任何欄位。新增 light_direction 欄位與 L9_screen_only_uplight。改三欄拆分後 validator 反算稽核，又自行抓到 st05 同病與 fixed_baseline 漏了 4 個欄位。render 預算改現算；R6 同意結案，並確認三個不變量；不變量 3（欄位全集反算）已於本輪補上機器檢查 |
| C-22 | C 級場景被 cinematic treatment 抵銷 | ChatGPT | ✅ 結案 | c12 的「列車頭燈掃過」是動態戲劇光＋CCD，已改靜態廣告燈箱光且 filter 改 none。新增 validator 規則：C 級不得同時有濾鏡與動態光源，且帶濾鏡的 C 級不得超過 1/3。**c03 不同意改**：filter=none，門口晨光＋不鏽鋼反射＋天花板冷白燈管正是真實早餐店的混光，沒有風格化處理；R6 同意結案（c03 維持不改） |
| C-23 | 覆核檔沒揭露 props，九欄語意 gate 無法完成 | ChatGPT | 🔵 Claude已修正 | 屬實，是我自己挖的坑：§8 要求逐列判斷 props，生成器卻從未輸出。補上 §5-5b props 表後**當場又看到三類新錯**：8 列 props 重述 outfit 已提供的包或借用別套招牌包（a03–a08、c06、c12）、c10 抱衣物還多一隻手拿零錢、c07 把「客人的手」放進訓練集。新增 `hands`（left/right 兩槽位）欄位＋4 條 validator 規則 |
| C-24 | c12 刪掉車頭燈後 exposure_choice 仍寫「車頭燈那側過曝」 | ChatGPT | 🔵 Claude已修正 | 屬實。改一欄沒同步另一欄，第三次犯同一類錯，且就發生在要送進訓練集的 prompt 上。已改為廣告燈箱側肩線略過曝 |
| C-25 | st06 拿訓練集出現 4 次的 park 測 no_scene_burn_in | ChatGPT | 🔵 Claude已修正 | 屬實，檢出力等於零。改為 bus_stop（訓練集未出現、C 級、戶外，L6 理由不變）。新增 validator 規則：測 no_scene_burn_in 的 shot 必須用訓練集沒出現過的 location |
| C-26 | outfit_04 的「包/外套」欄填的是及膝襪 | ChatGPT | 🔵 Claude已修正 | 屬實，五層等於少一層。及膝襪併入下身，補深藍色肩背書包。連帶發現 c05 的 props 借用了 outfit_03 的小方包 |
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
