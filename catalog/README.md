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
Claude 更新 catalog/KOLCAT_REVIEW_PACKET.md
       （改 §2 規劃、§3 自開議題、§4 帳本、§5 本輪問題）
  → 跑 render_packet_numbers.mjs --check → commit & push
  → 使用者把「請 ChatGPT 覆核」那段訊息貼給它（見下面「轉傳訊息」）
  → 🛑 ChatGPT 自己把回覆 commit 回同一個檔案的最末尾（附加新的一節）
  → Claude git fetch 拉下來 → 逐項實測驗證 → 修正 §2、更新 §4 帳本 → 推進輪次
  → 重複，直到 §4 的 P0 全部結案
  → 使用者確認版面
  → 才連上 Railway 執行
```

### 🛑 本線的 ChatGPT 要寫回 GitHub（跟另外兩條線相反）

`review/README.md` 寫著「ChatGPT 不再讀 GitHub、也不寫回 GitHub」，**那是 Nico 線與餐廳線的協定，
不適用於本線**。本線改成寫回，理由是 R1 那一輪**使用者手動轉傳漏掉了**——
他先說「GPT 檢核好了」，但遠端與本地都沒有任何回覆，後來才補 commit 進來。

**寫回不等於讓它爬 repo。** 兩件事分開：

| | 本線的規則 |
|---|---|
| **讀** | 🛑 **只讀 `catalog/KOLCAT_REVIEW_PACKET.md` 一個檔案。** 不要爬 repo——2026-08-27 實測過，連接器爬整個專案**一次就燒光使用者 5 小時的方案用量** |
| **寫** | ✅ **只附加到那個檔案的最末尾**，只動那一個檔案，只推工作分支 |

規則全文寫在覆核包的 §0.5（給 ChatGPT 讀的那一份），這裡只記為什麼。

### 🛑 Claude 這邊要配合的三件事

1. **每次開工先 `git fetch`。** 它可能已經 commit 了回覆——
   R1 那次我先查了分支才發現沒有，第二次查才有。**不要憑使用者說「好了」就當它到了。**
2. **改檔案前先確認遠端沒有新的回覆節**，否則會蓋掉它的 commit。
   拉下來之後再改，並且**只改 §2／§4／§5，不要動它的回覆節**（那是歷史紀錄）。
3. **拉下它的 commit 之後跑 `render_packet_numbers.mjs --check`。**
   §2.1 是程式產生的，如果它手改了那一段，`--check` 會 exit 1——**這就是防它改錯地方的那道閘門**。

**兩件不可以跳過的：**

- 🛑 **不要讓 ChatGPT 爬 repo。** 覆核包必須**自帶全部內容**——統計數字、清單、diff 都內嵌。
- 🛑 **不要照收對方的主張，每一項可驗證的都要實測。**
  R1 的實例：它的 `KC-02` 抓對了我手寫錯的數字（成立），
  但它解釋成因那段算式**自己算錯**（主張要有 7 位人設同時存在三個 repo，實際解不出整數）。
  **兩件事都要寫進帳本**，這才是「誰主張什麼」的紀錄有用的地方。

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

---

## 轉傳訊息（給使用者一鍵複製用）

**照「三條線共用：轉傳訊息一律用程式碼區塊」那條規則**（`review/INDEX.md`），
每輪交給使用者的訊息要放在 fenced code block 裡。訊息骨架：

- 指名 repo ／ 分支 ／ 檔名（**只有這一個檔案**）
- 明講不要讀 `review/` 底下的東西（另外兩條線的）
- 明講**要把回覆 commit 回檔案最末尾**，不要只留在對話裡
- 明講不准動 §2.1（程式產生）與既有小節
- 指定本輪要答的問題編號與新議題的 ID 前綴
- 明講不要給版面美感意見（§0.4）
