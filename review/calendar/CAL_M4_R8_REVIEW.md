TASK-CAL-001／M-4／R8｜主管看圖覆核與構圖控制流程查核｜送審報告

# M-4 R8 送審紀錄（主管看圖覆核後的構圖控制流程唯讀查核）

- **固定成果 commit**：`3159528b914af76260da8a56853323dd257e1aa9`（被覆核的照片成果 `de17da5`、紀錄 `9b14b2b`）
- **主管結論（逐字另存）**：`docs/calendar/data/cal_m4_supervisor_r8.json`。REVISE，不建議採用；Penny 尚未接受。和 Claude 自查（`cal_m4_r8_trial.json`）分開保存；自查原文沒改，只加了指向主管結論的欄位與狀態行。
- **收尾句來源**：「finished like a page from a high-end photobook」由 Claude 在 R6 REVISE 依主管「寫真集完成度」的意見寫成，之後沿用；主管表示該用語來自主管建議。兩者都記錄。白邊與這句的關係仍是待查假設，沒有證實。
- **本輪**：新增生成 0、修圖 0、訓練 0、上傳 0、付費操作 0、部署 0；唯一原圖保留，沒有修改，也沒有改成已接受；沒有純文字重試，沒有啟動 H-Jia。

## 1. 事實同步

- V-Somi 照片歷程：「R5 退回；R7 主管建議退回，Penny 未接受；R8 主管建議退回，Penny 未接受」（`status.production.set_notes`）。主管建議退回不是 Penny 決定。
- 累計生成 8、credits 0.96，不變；24 套完成分類：已接受 1、退回待重規劃 5、尚未生成 18，不變。
- 同步位置：企劃資料 `meta.status`、`counts_note`、`status.production.set_notes`、`m4r8`（加照片與紀錄 commit、主管結論、查核資料路徑與變更列）；CAL_18 的 R8 狀態行；選片頁資料 `data.js` 只在 repo 重建，沒有部署（新增的兩個 R8 commit SHA 已加進建置檢查的允許清單，它們不是私有 ID）。
- 檢查：CAL_18–22 `--check` PASS、CAL_23 `--check` PASS（CAL_19 與先前版本逐字相同）、建置 `--check` PASS（671 檔，公開檔無私有識別碼、無交易原始資料）。

## 2. 唯讀能力查核（`docs/calendar/CAL_25_M4_R8_FLOW_CHECK.md` §2）

- 方法：MCP 模型 schema、工具說明、8 次 get_cost 唯讀報價（前後交易最新一列與任務清單最新一筆都沒變）、Higgsfield 官方說明頁。沒有上傳、沒有建任務、沒有付費，也沒有列出 Elements。私有紀錄 `review/calendar/m4_r8/flow_check_log.json`。
- 結論摘要：
  - Soul ID 可與參考圖並用（官方說明＋報價被接受）；並用後身分是否保持未確認。
  - 參考圖是「primary direction」（官方），影響範圍混合、未拆分；網頁介面加參考圖時 prompt 不可用；MCP 送出的 prompt 是否生效未確認。
  - Soul 沒有參考強度、姿勢、構圖參數（schema）；後台有強度欄位但無法設定。
  - 費用（唯讀報價）：Soul＋參考 0.12、外擴 2、Nano Banana Pro 2、Nano Banana 2 2、GPT Image 2.5 high 2.75、Seedream 4.5 basic 1。
  - 官方身分保持說明：同一人但非逐像素相同、極端風格或角度會小幅漂移；身材保持官方沒寫。

## 3. 路徑與推薦（CAL_25 §3–§5）

- A. 構圖底稿＋Soul 參考（推薦）；B. 構圖底稿＋Element 換人；C. 既有成品外擴＋遮罩清理（只當收尾工具）。
- 下一次測試（提案，未執行）：只做 A 的第 1 步，一張無身分的構圖底稿（Nano Banana Pro 2k 3:4，報價 2；或 Seedream 4.5 basic，報價 1），1 次請求、不重試；底稿交主管及 Penny 看過後，第 2 步（Soul＋底稿參考，報價 0.12）另行授權。
- 雙靴與雪地、人景主次、背景整理、白邊與版面、避免他人臉、驗收與停止點：見 CAL_25 §5。

## 4. 需 Penny 決定

見 CAL_25 §7：是否授權下一次測試與上限、底稿模型、是否允許一次唯讀 Elements 列表、是否允許向 Higgsfield 支援詢問。

## 5. 必要閱讀清單

- `docs/calendar/data/cal_m4_supervisor_r8.json`
- `docs/calendar/CAL_25_M4_R8_FLOW_CHECK.md`
- `docs/calendar/data/cal_m4_r8_flow_check.json`
- `docs/calendar/data/cal_m4_r8_trial.json`
- `review/calendar/m4_r8/V-somi-oh_m4r8_view.jpg`、`review/calendar/m4_r8/V-somi-oh_m4r8_frame_V_120x160.jpg`

## 前一版紀錄（R8 單張測試，`9b14b2b`；原文保留）

TASK-CAL-001／M-4／R8｜Somi 精簡 prompt 單張測試｜送審報告

# M-4 R8 送審紀錄：V-Somi 精簡 prompt 單張測試

- **固定成果 commit**：`de17da5d91d9622632ff56dd7f9717dfed2387c4`（方案基準：CAL_24 成果 `efa00c8`、紀錄 `0784cd4`；主管對方案的 PASS 不是照片接受）
- **授權**：`docs/calendar/data/cal_m4_auth_r8.json`（逐字）。只限 V-Somi 1 張、最多 1 次請求、上限 0.12 credits；不授權自動重試、補生或其他角色。
- **結果紀錄**：`docs/calendar/data/cal_m4_r8_trial.json`（不含 ID）；私有執行紀錄 `review/calendar/m4_r8/execution_log.json`。
- **本輪**：生成 1、請求 1、重試 0、實扣 0.12、修圖 0、訓練 0、部署 0。以下是 Claude 自查，不是主管看圖覆核，也不是 Penny 接受。

## 1. 最終 prompt

- 來源：efa00c8 `CAL_24` §5，只做兩處授權修改，其餘逐字保留：
  - 「wide photograph」→「environmental full-length portrait」
  - 「a short way from the camera」→「seen from a comfortable distance, with the street clearly surrounding her」
- 最終全文與 hash：在結果紀錄 `prompt.text`；sha256 `05cc5303…74b494e`（原 CAL_24 版本 `1707a72f…`）。

## 2. 設定、請求與扣款

- 設定：soul_2、somi-oh 既有 Soul（送出前確認 ready）、2k、3:4、count 1；不用 unlim、不加參考圖、不傳 style（後台套用預設 General）、不訓練。
- 報價：`get_cost` 唯讀報價 0.12（≤ 上限 0.12）。報價前後交易與任務清單都沒變，確認報價沒建任務、沒扣款。
- 請求：1 次，2 次輪詢後完成，沒有重試。
- 扣款：只有一列 Soul V2 −0.12（2026-10-24T13:55:11Z），沒有退款。
  - 依時窗推定，不是直接對帳：扣款時間和任務建立時間一致，同時窗只有這一個 soul_2 任務；交易明細沒有任務 ID。

## 3. 圖片位置

- 原圖（不改、私有）：`kols/somi-oh/images/calendar_2027_batch1/V-somi-oh_m4r8.png`（1536×2048，sha256 `d1702991…ce024cb`，檔內含平台任務 ID）
- 顯示版：`review/calendar/m4_r8/V-somi-oh_m4r8_view.jpg`（1200×1600，無中繼資料）
- 套框預覽：`review/calendar/m4_r8/V-somi-oh_m4r8_frame_V_120x160.jpg`（無中繼資料）

## 4. 實際看圖自查（依 CAL_24 必要要求；可容許變化不算失敗）

| 必要要求 | 結果 | 看到的情況 |
|---|---|---|
| 1. 雙靴完整、靴下有雪 | 不通過 | 後腳完整；前腳靴底剛好壓在照片區下緣（白邊上），靴下沒有雪地。 |
| 2. 空間配置平衡 | 大致通過 | 天空只剩一條、沒有近景大燈籠、街道往中央退，比 R7 平衡；人物仍約占照片區高度 77%，下方雪地不足。 |
| 3. 沒有搶戲的物件、文字、雜物 | 部分通過 | 近景大燈籠消失；左緣燈籠有大字，右側有字的布招與招牌箱，天空有電線，右側有腳踏車與紅桶，但比 R7 不搶戲。 |
| 4. 讀得出抬頭看雪 | 不通過 | 不看鏡頭（改善）；但轉頭看畫面右側、一手在衣領旁，像走路回眸的造型照。 |
| 5. Somi 可辨識、成年；光色可信 | 大致通過 | 可辨識且成年；臉部受光偏均勻，周圍雪地看不出燈籠暖光圈，但沒有明顯浮貼。 |
| 6. 藍調與酒紅／象牙白配色 | 通過 | 深藍天色、小燈籠、深蔓越莓紅、象牙白、白靴協調。 |

- **新問題：白色相紙邊框。** 整張外圍有一圈白邊（原圖上 44、下 42、左 99、右 84 px），成品必須滿版。
  - 若裁掉白邊再取 3:4，約 286 ppi（低於 300），前腳仍貼邊。
  - 邊框很可能和共用收尾句「finished like a page from a high-end photobook」有關（推測，未驗證）；這句 24 套共用，請主管一併考量。
- **可容許變化（不算失敗）**：人物在中間、大衣扣起而下襬開、臉的角度、雪量、燈籠數量。
- **自查結論：不通過。** 必要要求第 1、4 項不通過，第 3 項仍有文字與電線，另有白邊。照片狀態維持「待主管及 Penny 審圖」。

## 5. 未受控制的項目（R5、R7、R8 純文字 prompt 對照）

| 項目 | 三輪結果 | 說明 |
|---|---|---|
| 人物大小與腳下留白 | R5 約 80% 右靴出界；R7 至少 67% 右靴被切；R8 約 77% 前腳貼邊 | 數字描述（R7）與由上到下的畫面描述（R8）都沒有留出靴下雪地 |
| 文字（燈籠、招牌） | 三輪都有 | R8 變小、不在中心，但仍出現 |
| 電線 | 三輪都有 | 每次都排除，仍出現 |
| 動作與視線 | R5 抬眼但攤掌；R7 看鏡頭；R8 轉頭看側邊 | 「抬頭看雪」R7、R8 都沒落實 |
| 白色相紙邊框 | R8 首次出現 | 可能與收尾句有關（推測） |

- **受控制的部分**：藍調時刻與點亮燈籠、酒紅／象牙白配色、移除近景大燈籠、不看鏡頭、Somi 身分。
- **下一步**：依指示停止純文字重試。之後先唯讀查構圖參考流程：soul_2 帶 Soul 時能否同時用 1 張參考圖、身分保持、費用。也請主管考量共用收尾句。本輪不換模型、不建任務、不啟動其他流程。

## 6. 事實同步

- 累計生成 7 → 8（R2 1＋R5 5＋R7 1＋R8 1），credits 0.84 → 0.96。
- V-Somi 照片歷程加「R8 試拍待主管及 Penny 審圖」；24 套完成分類不變。
- 同步位置：
  - 企劃資料、CAL_18／21／23
  - 選片頁資料：只在 repo 重建（建置檢查 PASS，671 檔、問題 0），沒有部署
- 建置的 ID 允許清單加了 R8 基準 commit SHA。

## 7. 未完成事項

- 主管實際看圖覆核，最後由 Penny 決定。
- 構圖參考流程的唯讀查詢，等主管指示。
- 沒有修圖、補生、部署；沒有啟動 H-Jia；沒有改已接受的 V-Iris；沒有合併 main。
