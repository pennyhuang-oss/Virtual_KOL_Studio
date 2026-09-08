# 897 女團選秀 — 客戶簡報網站

企劃提案站，給客戶直接看的版本。內容全部由 `public/data/` 的三個 JSON 驅動，
新增規劃不需要改程式碼。

## 內容從哪裡來

| 檔案 | 內容 | 怎麼產生 |
|---|---|---|
| `public/data/roster.json` | 15 位參賽者的規格、才藝、設定依據 | `python3 site/build_roster.py`，硬規格直接讀 `kols/<id>/profile.json` |
| `public/data/media.json` | 每位的圖片與影片清單 | `python3 site/build_media.py` 產出時一併寫入 |
| `public/data/plan.json` | 企劃敘述：總覽、流程、體檢、待裁決、替補、下一步 | 手動編輯 |

**要改名單或規格** → 改 `site/build_roster.py` 的 `EDITORIAL` 表，重跑 `build_roster.py`。
身高三圍等硬規格改不了，因為那是從人設庫讀的——要改就去改 `profile.json`，這是刻意的。

**要新增一整個章節**（例如選秀賽制、打投規則、時程表）→ 在 `plan.json` 加一個區塊，
在 `public/index.html` 加對應的 `<section>`，在 `public/app.js` 的 `NAV` 加一列。

## 素材

`build_media.py` 從 `kols/<id>/` 挑圖，縮到 1000×1400 以內轉 WebP 寫進 `public/media/<id>/`。
影片直接複製到 `public/video/`。整包約 38 MB。

`shots[0]` 會成為列表頁封面，所以生活素材排在前面，`identity_master.jpg`（證件照式的
臉部基準圖）排在最後。

`BLOCK` 常數擋掉人設庫的「私下」那一層（lingerie／onsen／bed／bathroom 等）——
這是客戶簡報，預設只放公開形象素材。要加回去就改那個常數。

## 本機執行

```
node site/server.js              # http://localhost:3000
SITE_PASSWORD=xxxx node site/server.js   # 加上通行碼
```

## 部署

Railway，root directory 設為 `site`，start command `npm start`。
`SITE_PASSWORD` 環境變數決定是否需要通行碼；不設就是公開。

伺服器刻意零依賴（只用 Node 內建模組）：建置快，而且一個要給客戶看的網站
不需要背一整包 npm 供應鏈。已實作 mp4 的 Range request——沒有它 Safari 不會播。

## 素材挑選頁 `/pick.html`

給使用者自己挑素材用的頁面，跟企劃站同一個服務，沒有額外後端。

```
python3 site/build_picker.py                 # 產生素材池（thumb 190px / full 800px）
# → 使用者在 /pick.html 挑選，按「複製選擇結果」得到 JSON
python3 site/apply_selection.py sel.json     # 套用，重寫 media/ video/ media.json
```

**素材池的兩個來源**

| 來源 | 內容 | 備註 |
|---|---|---|
| `庫` | `kols/<id>/**` 原始檔 | 含建模圖；已排除 `_rejected` / `_fail` / `_superseded` |
| `型錄` | `catalog/assets/_pick/<id>/` | 從 catalog 分支 `git archive` 取出，已是 web 尺寸；只有 5 位已建模的有 |

**設計取捨**

- 選擇存成 **asset id**（來源路徑的 sha1 前 10 碼）而不是路徑或流水號，
  所以重建素材池不會讓既有選擇指到別張圖。
- 挑選結果走 localStorage ＋剪貼簿匯出，**刻意不做後端**——這樣挑選頁只是企劃站上
  的一個靜態路由，不需要再開一個 Railway 服務（免費額度已經很緊）。
- 人設庫的 reel 單支 1.4–59MB，塞進挑選頁會讓 build context 爆掉，
  所以影片候選只顯示 `start_frame.png` 首幀，實際檔案在套用時才拉進來；
  型錄的小 clip（<1MB）則直接內嵌可預覽。
- `apply_selection.py` 有 `VIDEO_BUDGET_MB` 上限（預設 90MB），超過會跳過並警告，
  避免一次選太多大 reel 讓部署失敗。
- 「私下」那一層（lingerie／onsen／bed／bathroom）在挑選頁是**半透明並標紅字**，
  不是隱藏——客戶簡報預設不建議放，但選擇權在使用者。

## 覆蓋層與瀏覽器歷史

參賽者詳細面板與燈箱都是 **history entry**，不是純 JS 狀態。原因是使用者實測回報：
大家看完一位人設後會習慣按瀏覽器「上一頁」，而在改之前那會直接離開整個網站。

現在的行為：

| 動作 | 結果 |
|---|---|
| 點卡片開啟詳細頁 | `pushState` → 網址變成 `?c=<id>` |
| 瀏覽器上一頁 | 關掉最上層的覆蓋層（燈箱 → 詳細頁 → 名單），不會離站 |
| 「← 返回名單」／✕／Esc／點空白 | 全部走 `history.back()`，所以歷史堆疊不會跟畫面脫節 |

返回列上**不放操作說明文字**。使用者裁決：一個有文字的返回按鈕本身就夠清楚，
再附一句「按上一頁或 Esc 也可以」反而奇怪。
| 直接開 `?c=iris-chen` | 直接展開那一位——可以把單一人設的網址丟給客戶 |

`popstate` 依落地的 state 決定要關到哪一層，所以前進／後退都對得上。

**燈箱圖片尺寸**：`max-height:100%` 在 auto 尺寸的 grid track 裡是循環定義會被丟掉，
直式照片會溢出視窗（實際踩到）。改成 `calc(100dvh - Npx)` 明確對視窗計算，
並留出上下 chrome 的空間。挑選頁的燈箱同一個修法。
