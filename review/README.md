# 覆核協定（Claude ⇄ ChatGPT）

> 2026-08-27 建立。**這個資料夾是兩個模型互相檢核的工作區。**
> Penny 的規則：**任何規劃都不是 Claude 說可以就執行，一定要經過 ChatGPT 覆核通過才繼續。**

## 工作分支

**`claude/virtual-kol-restaurant-campaign-pxu9m4`**

⚠️ **ChatGPT 請直接 commit 到這個分支**，不要開新分支、不要推 main。
Claude 每次動工前都會先 `git pull` 這個分支。

## 主檔案：`LEDGER.md`

**一個檔案就好，不要再每輪開新檔。**
`LEDGER.md` 是一張活的議題表，每一項有固定編號與狀態。

### 狀態流

```
🔵 OPEN        Claude 提出，等 ChatGPT 判定
🟡 ANSWERED    ChatGPT 已判定，等 Claude 執行
🟢 DONE        Claude 已執行完畢
⚪ PARKED      雙方同意暫緩（要寫暫緩到什麼時候／等什麼條件）
🔴 DISPUTED    兩邊看法不同，需要用實測解決（要寫怎麼測）
```

### 給 ChatGPT 的編輯規則

1. **只改你那一欄／那一段**（`### ChatGPT 判定`），不要改 `### Claude 的看法`
   —— 那是提出當下的原始紀錄，改掉就失去了對照價值
2. **改完把狀態從 🔵 改成 🟡**（或 ⚪ / 🔴）
3. **不要刪除已 🟢 DONE 的項目**，往下沉到「已結案」區就好——那是驗證紀錄
4. **要新增議題請往表尾加**，編號續號，不要插號
5. **每一項判定請寫「理由」而不只是結論**，因為 Claude 要據此改，理由錯了結論也會被誤用
6. **如果你認為某項的 Claude 看法是對的，也請明寫「同意」**——沉默會被當成還沒看

### 給 Claude 的規則

1. **動工前一定先 `git pull`**，ChatGPT 可能已經改過
2. 執行完把狀態改成 🟢，並在「處置」欄寫**實際做了什麼、在哪個 commit**
3. **不要自己把 🔵 改成 🟢**——沒有經過判定就執行違反 Penny 的規則
4. 拿捏不準、覺得可能有盲點的地方，**當下就往 LEDGER 加一項 🔵**，不要留在腦袋裡

## 其他檔案

| 檔案 | 用途 |
|---|---|
| `LEDGER.md` | **主檔**，活的議題表 |
| `history/` | R1–R4 的歷史覆核往返，唯讀，只作追溯用 |

## 相關的專案文件（覆核時可能需要讀）

| 檔案 | 內容 |
|---|---|
| `CALIBRATION_TEST.md` | **所有付費實測的結果與結論**，是判斷「已驗證 vs 未驗證」的唯一依據 |
| `clients/sushisolar-rujiao/GENERATION_PLAN_B1.md` | 批次一 21 件完整規格，每件含實際送出的英文 prompt |
| `SEXY_SCENE_LIBRARY.md` | 累積的生成規則，第 20–26 點是這個專案期間新增的 |
| `tools/prompt_lint.py` | 送生成前的機械檢查（含 `--selftest`） |
| `clients/sushisolar-rujiao/cost-log.md` | 逐筆對帳紀錄 |
| `kols/*/images/preflight/` | preflight 成品 |
