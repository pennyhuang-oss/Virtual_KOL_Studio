# 交叉覆核工作區（Claude ⇄ ChatGPT）

> 這個資料夾是 Claude 與 ChatGPT 互相檢核的**唯一入口**。
> 規則：**任何規劃在 `LEDGER.md` 全部結案之前，不得進入生成階段。**

---

## 給 ChatGPT 的操作說明

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

**只改兩個地方：**

1. **`review/LEDGER.md`** — 這是主要溝通管道
   - 新發現的問題：在表格最下方新增一列，ID 用 `C-nn`（ChatGPT 提出）
   - 回應既有議題：把該列的 `狀態` 改成 `ChatGPT已回應`，並在下方「議題詳述」區塊補你的論述
   - 同意結案：把 `狀態` 改成 `雙方同意`
2. **`review/rounds/R{n}_..._chatgpt.md`** — 需要長篇論述時，開一個新檔放完整內容，
   並在 LEDGER 對應議題裡連結過去

**請不要直接改 `pilot/` 底下的 JSON。** 那是 Claude 這側的實作，
你指出問題、Claude 修改，這樣才能保留「誰主張什麼」的紀錄。

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
