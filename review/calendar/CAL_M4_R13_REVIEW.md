TASK-CAL-001／M-4／R13｜停止反覆前置，交付Somi測試結果與其餘四位製作準備｜送審報告

# M-4 R13 送審紀錄

- **固定成果 commit**：`bd84cf97a7310afa672d506895e09c8d73220408`（R12 成果 `d154bde`、紀錄 `a862ce1`）
- **本輪**：生成 0、上傳 0、付費 0、訓練 0、部署 0。

## 1. Somi 遮罩身分編輯：未送出

- 遮罩覆蓋：正確（臉、瀏海、髮際線、上頸；邊界在頭髮與皮膚內）。
- Element 佔位符：符合工具要求（`<<<element_id>>>` 寫在 prompt，不放 medias）。
- 遮罩白黑定義：**無法確認**。查過 schema、工具說明、Higgsfield 官方頁與打包工作流程，都沒有定義；只有第三方與業界慣例寫白色＝編輯。
- 上傳費用：官方未說明；repo 以往上傳沒有對應扣款紀錄。
- 依停止規則：沒有上傳、沒有含遮罩報價、沒有送出、沒有扣款；不改用整張生成。
- 紀錄：`docs/calendar/data/cal_m4_r13_somi_precheck.json`。

## 2. 其餘四位製作卡

- `docs/calendar/CAL_27_M4_R13_NEXT_CARDS.md`（資料 `docs/calendar/data/cal_m4_r13_cards.json`）：Tammy、Rin、Yerin、Jia 各一張。
- 下一批建議：Tammy、Rin 各 1 張 Soul 純文字，合計約 0.24 credits；Yerin、Jia 等身分編輯方法有結果再排。

## 3. 計數

- 月面候選 9 張／1.08 credits、底稿 2 張／4 credits，合計 5.08，不變；24 套分類不變，只有 V-Iris 已接受。
- 檢查：CAL_18–22 `--check` PASS、CAL_23 `--check` PASS（CAL_19 不變）、建置 `--check` PASS；未部署。
