# 交叉覆核工作區（Claude ⇄ ChatGPT）

> 這個資料夾是 Claude 與 ChatGPT 互相檢核的**唯一入口**。
> 規則：**任何規劃在 `LEDGER.md` 全部結案之前，不得進入生成階段。**

---

## ⚠️ 2026-08-27 協定修正：ChatGPT 不再讀 GitHub

**發生什麼事**：讓 ChatGPT 透過 GitHub 連接器讀 repo，**一次讀取就把使用者 5 小時的方案用量燒光**。
它只做檢核、不做規劃與執行，用量卻比 Claude 還快——因為連接器會爬整個專案背景
（本 repo 光 `.md` 就約 500KB），而它真正需要判斷的只有「這次改了什麼」。

**另外**：上一輪請 ChatGPT 把意見寫回 GitHub，實際上**沒有發生**——
遠端沒有它的 commit 也沒有新分支。所以寫回路徑也不成立。

### 現在的做法

```
Claude 改動 → python3 tools/gen_review_request.py → 產生自帶內容的訊息
           → 使用者複製貼上給 ChatGPT（ChatGPT 不 fetch 任何東西）
           → ChatGPT 在對話裡回覆 → 使用者貼回給 Claude
           → Claude 實測驗證 → 修正 → 更新 LEDGER → 更新 CHECKPOINT
```

- `review/CHECKPOINT` 記錄 ChatGPT 最後覆核到的 commit，delta 從那裡算起
- 產生的請求存在 `review/requests/REQ_<sha>.md`，同時印到 stdout 方便複製
- 請求內含：程式算好的規格數字、本輪 diff、未結案議題表、固定的回覆格式
- **統計數字一律由程式計算後內嵌**，ChatGPT 不需要自己 parse JSON

以下「給 ChatGPT 的操作說明」保留作為**它主動想查證某個檔案時**的參考，
但常態流程不需要它讀 repo。

---

## 給 ChatGPT 的操作說明（僅供主動查證時使用）

### 你要讀什麼

| 檔案 | 內容 | 是不是真理來源 |
|------|------|---------------|
| `review/LEDGER.md` | **議題帳本**——所有未結案的爭點、待驗證假設、待使用者決定的事 | ✅ 覆核狀態的真理來源 |
| `pilot/nico_pilot.json` | Nico pilot 的完整規格 | ✅ **規格的真理來源** |
| `pilot/location_registry.json` | 地點層級與 signature/career 預設值 | ✅ |
| `pilot/schema_v2.json` | 資料結構定義 | ✅ |
| `tools/validate_shoot_plan_v2.py` | 驗證器 | ✅ |
| `review/rounds/*.md` | 歷次覆核的完整論述（唯讀存查）| ❌ 歷史紀錄，不要以此為準 |

**統計數字一律以 JSON 為準。** 任何 `.md` 裡的 count / ratio 都是產生出來的，
若與 JSON 不符，那就是 bug——請直接開一條 ledger 議題。

### 你要寫回什麼

**直接在對話裡回覆，不要寫回 GitHub。** 使用者會把你的回覆貼給 Claude，
由 Claude 統一更新 `LEDGER.md`。這樣既省你的用量，也保留「誰主張什麼」的紀錄。

回覆格式在每封覆核請求的第 4 節。

### 你可以自己驗證

```bash
python3 tools/validate_shoot_plan_v2.py pilot/nico_pilot.json
```

不需要額外依賴，只用標準函式庫。它會讀 `pilot/location_registry.json`。

---

## 給 Claude 的操作說明

1. 每次開工先讀 `review/LEDGER.md`，處理所有 `ChatGPT已回應` 的議題
2. **實測驗證對方的每一項可驗證主張**，不要直接照收——已經發生過對方數字全對、
   也發生過對方引用的官方規格與本專案實際 endpoint 不同的情況
3. 修改後更新 LEDGER 該列狀態為 `Claude已修正`，並寫清楚改了什麼、commit hash
4. 自己拿捏不準或可能有盲點的地方，**主動開一條 `K-nn` 議題**，不要等對方發現

---

## 狀態流轉

```
待對方回應 → ChatGPT已回應 → Claude已修正 → 雙方同意 → 結案
                  ↑                              ↓
                  └──────── 若不同意 ────────────┘

需使用者裁決 ← 任一方認為這是產品決策而非技術判斷
```

**只有全部議題進入「結案」，才可以開始花 credit 生成。**
