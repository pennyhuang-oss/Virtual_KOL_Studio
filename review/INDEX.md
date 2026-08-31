# review/ 資料夾索引

**這個 repo 目前有三條各自獨立的覆核工作線。前兩條都在用 `review/`，第三條刻意不用。**
2026-08-28 合併時發現雙方都佔用了 `LEDGER.md` 與 `README.md` 這兩個檔名，
內容完全不同、不能合併，所以分開放。**動檔案前先確認自己在哪一條線。**

| 工作線 | 內容 | 主檔 | 協定 |
|---|---|---|---|
| **Nico Pilot** | 建模照計畫、Phase A–C、20 段 prompt | `review/LEDGER.md` | `review/README.md` |
| **餐廳批次一** | 壽司太陽／如膠 · Yuna＋Luna · 21 件 IG 素材 | `review/restaurant-b1/LEDGER.md` | `review/restaurant-b1/README.md` |
| **KOLCAT 型錄站** | 三個 repo 的 42 位 KOL 做成 Railway 公開型錄 | 🛑 **不在 `review/`**：帳本內嵌於 `catalog/KOLCAT_REVIEW_PACKET.md` §4 | `catalog/README.md` |

## 共用但未分家的檔名

| 檔案 | 目前歸屬 | 注意 |
|---|---|---|
| `review/REVIEW_REQUEST.md` | **餐廳批次一** | Penny 轉傳給 ChatGPT 的固定路徑，維持不動 |
| `review/requests/` `review/rounds/` `review/REVIEW_PHASE_C.md` | Nico Pilot | — |

**若 Nico 線之後也需要一個「Penny 轉傳用」的固定檔案，
不要直接用 `review/REVIEW_REQUEST.md`**——會蓋掉餐廳線正在等回覆的請求。

## 議題 ID 前綴：已佔用的不要重用

| 前綴 | 屬於 |
|---|---|
| `C-` `K-` `U-` | Nico Pilot |
| `D-` `LG-` `YG-` | 餐廳批次一 |
| `KC-` `CC-` `PP-` | KOLCAT 型錄站 |

**新工作線開張時先來這張表挑沒被用過的前綴**，不然兩條線的帳本會出現同一個 ID
指兩件事，而覆核者只讀單一檔案、看不出撞號。

## KOLCAT（第三條線）為什麼不放在 `review/`

2026-08-31 開張時，使用者明確要求「檔名一定要跟另外兩條區分開來，避免 ChatGPT 讀錯檔案」。
`review/` 底下已經有 `LEDGER.md`（兩份）、`REVIEW_REQUEST.md`、`REVIEW_PHASE_C.md`、
`REVIEW_BATCH3_FACES_R2..R10.md`，**再加一份就是在製造下一次撞名**。

→ KOLCAT 整條線收在 **`catalog/`**，給覆核者的檔案一律 `KOLCAT_` 開頭，
**而且刻意不另開 `LEDGER.md`**——帳本直接內嵌在覆核包的 §4，全線只有一個檔案要轉傳。

## 兩條線共用的結論

`SEXY_SCENE_LIBRARY.md`、`WARDROBE_SYSTEM.md`、`COMPETITOR_sherry_digitalp510.md`
以及 `tools/` 底下的檢查器是**兩條線共用**的。改動這些檔案前要想到另一條線也會讀。
