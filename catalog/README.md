# `catalog/` — AI KOL 型錄站（KOLCAT）

**這一條工作線的代號是 `KOLCAT`。** 目標：把三個 repo 的 AI KOL 人設做成一個
放在 Railway 上的公開型錄網站，連結可以直接丟給客戶。

---

## 🛑 檔名隔離：這個 repo 有三條覆核線，不要互相污染

使用者特別交代過這一點。三條線各自有帳本與請求檔，**內容不能互相參照**：

| 工作線 | 主檔（給 ChatGPT 讀的那一份） | 議題 ID 前綴 |
|---|---|---|
| Nico Pilot | `review/LEDGER.md`＋`review/requests/REQ_<sha>.md` | `C-` `K-` `U-` |
| 餐廳批次一 | `review/restaurant-b1/LEDGER.md`＋`review/REVIEW_REQUEST.md` | `D-` `LG-` `YG-` |
| **KOLCAT（本線）** | **`catalog/KOLCAT_REVIEW_PACKET.md`** | **`KC-` `CC-` `PP-`** |

**本線的規則：**

1. ✅ **所有檔案都在 `catalog/` 底下**，不要在 `review/` 放任何 KOLCAT 的東西。
2. ✅ **要給 ChatGPT 的檔名一律 `KOLCAT_` 開頭。**
3. 🛑 **不要用 `LEDGER.md`、`REVIEW_REQUEST.md`、`REVIEW_PHASE_*`、`BATCH3_*` 這些檔名**——已被別線佔用。
   KOLCAT 的帳本**內嵌在覆核包的 §4**，刻意不另開一個 `LEDGER.md`，就是為了不撞名。
4. 🛑 **不要用 `C-` `D-` `K-` `LG-` `U-` `YG-` 當議題前綴**（已佔用，實際查過）。

---

## 覆核循環怎麼跑

```
Claude 更新 catalog/KOLCAT_REVIEW_PACKET.md（改 §2 規劃、§3 自開議題、§5 本輪問題）
  → commit & push
  → 使用者叫 ChatGPT「讀 catalog/KOLCAT_REVIEW_PACKET.md」
  → ChatGPT 照 §6 的格式在對話裡回覆
  → 使用者把回覆貼回給 Claude
  → Claude 逐條實測驗證，修正 §2，更新 §4 帳本，把輪次推進到 R2
  → 重複，直到 §4 全部結案
  → 使用者確認版面
  → 才連上 Railway 執行
```

### 🛑 覆核請求一定要用程式碼區塊交給使用者（2026-08-31 使用者要求）

**原話：「以後要丟給 ChatGPT 複核的請求訊息，你都要弄成我可以直接一鍵複製的形式。」**

轉傳訊息**寫在 markdown 的 fenced code block 裡**（三個反引號包起來），
這樣使用者的介面會在右上角出現複製鈕，按一下就整段帶走。

| 做 | 不要做 |
|---|---|
| 整段包在 ``` 裡，一個區塊一則訊息 | 把訊息寫成散文，讓他自己框選 |
| 區塊內用純文字，**不要有反引號** | 在區塊裡用 `code` 標記檔名（會破壞外層圍籬，也讓貼出去多出符號） |
| 區塊內自帶完整路徑：repo ／ 分支 ／ 檔名 | 只寫檔名，讓他還要回去找在哪一個 repo |
| 一則訊息就是完整可貼，不要分兩段 | 「先貼這段，再貼那段」 |

**兩件不可以跳過的：**

- 🛑 **ChatGPT 只讀那一份檔案，不要讓它爬 repo。**
  2026-08-27 實際發生過：讓它透過 GitHub 連接器讀這個 repo，**一次就燒光使用者 5 小時的方案用量**。
  所以覆核包必須**自帶全部內容**——統計數字、清單、diff 都內嵌，它不需要 fetch 任何東西。
- 🛑 **不要照收對方的主張，每一項可驗證的都要實測。**
  前兩條線的經驗是：對方在可驗證的事上準確率極高，但也發生過它引用的官方規格
  與本專案實際 endpoint 不符。**實測完才寫進帳本。**

---

## 檔案

| 檔案 | 做什麼 | 誰改 |
|---|---|---|
| `KOLCAT_REVIEW_PACKET.md` | **給 ChatGPT 的唯一入口**。規劃＋帳本＋本輪問題＋回覆格式 | Claude |
| `tools/scan_inventory.mjs` | 掃三個 repo，把「有什麼素材可用」算成 JSON。**去重恆等式不成立就 exit 2** | Claude |
| `tools/sample_derive_measure.mjs` | 分層抽樣，用最終轉檔參數**實際轉檔**後量衍生檔大小（p50／p95／max） | Claude |
| `tools/render_packet_numbers.mjs` | 把覆核包 §2.1 整段從 JSON 現算後寫回。`--check` 檢查有沒有被手改 | Claude |
| `data/inventory.json` | 盤點輸出。**覆核包裡的每個數字都出自這裡** | 程式產生，不要手改 |
| `data/derive_measurements.json` | 轉檔實測輸出 | 程式產生，不要手改 |

### 🛑 §2.1 不准手寫（`KC-02` 的根因）

R1 的覆核包 §2.1 標題寫著「這些數字全部由程式現算」，但那張表的 repo 人設數
（VKS 30／SGK 11／BUP 24）**是我目測 `ls` 輸出手寫的**，實際是 31／10／17。
覆核者從 `30+11+24=65` 對不上「42 位聯集、16 位重複」抓到這件事。

**光改對數字沒有用**——這條（先驗再說）在本專案已經是第 12 次再犯，
而唯一真的停止再犯的規則都是被寫成程式的。所以：

```bash
node catalog/tools/scan_inventory.mjs            # 重新盤點（恆等式不成立會 exit 2）
node catalog/tools/render_packet_numbers.mjs     # 重新產生覆核包 §2.1
node catalog/tools/render_packet_numbers.mjs --check   # 過期或被手改 → exit 1
```

**每次改覆核包之後、push 之前，跑一次 `--check`。**
兩支檢查都做過對抗測試（故意弄壞 → 確認真的失敗 → 還原 → 確認通過）。

**還沒做的**（等覆核通過才動手，見覆核包 §2.7）：
`data/selection.json`（挑哪些圖）、`data/status_override.json`（誰真的可上線）、
`tools/build_assets.mjs`（縮圖轉檔）、`tools/build_catalog.mjs`（產生頁面）、
`public/`（站本體）、`server.js`＋`package.json`（Railway 進入點）。

---

## 數字一律由程式算，不要手寫

```bash
node catalog/tools/scan_inventory.mjs           # 寫入 data/inventory.json
node catalog/tools/scan_inventory.mjs --print   # 只看摘要
```

三個 repo 必須是姊妹目錄（預設 `/home/user`），可用 `REPO_ROOT` 覆寫。
掃不到某個 repo 不會失敗，會記進 `missing_repos`——**Railway 的 build 環境只有
`Virtual_KOL_Studio` 一個，所以站本體不可以在 build 時呼叫這支。**

2026-08-31 首次執行的結果：

```
人設 42 位（重複收錄 16、欄位互斥 4、標為已上線 5）
分區：可撐一頁 20 / 素材不足 4 / 只有文字 18
素材：圖 727 張 2,434.8 MB｜影片 187 支 2,606.2 MB｜合計 5,041 MB
```

★ **5,041 MB 是這個專案最硬的限制**，不能原樣上 Railway。處理方式見覆核包 §2.5。

---

## Railway（覆核通過才設定）

沿用 `showgame-kol/railway/` 已驗證成功的模式。設定值與三個實際踩過的坑
（`PORT=8080` 對不上會一路 502、換 Root Directory 要清 Watch Paths、
`curl` 拿到舊快取會看起來像站掛了）寫在覆核包 §2.6，**動手前照那一節念。**

⚠ **本站與另兩個 Railway 站有一個關鍵差異**：那兩個站整站有帳號密碼（裡面是去留判斷），
**本站要給客戶所以必須公開**。公開的代價與三個選項見覆核包的 `PP-01`，**那是使用者要裁決的。**
