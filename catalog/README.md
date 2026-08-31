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
| `tools/scan_inventory.mjs` | 掃三個 repo，把「有什麼素材可用」算成 JSON | Claude |
| `data/inventory.json` | 上面那支的輸出。**覆核包裡的每個數字都出自這裡** | 程式產生，不要手改 |

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
