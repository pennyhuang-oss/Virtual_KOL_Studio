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
