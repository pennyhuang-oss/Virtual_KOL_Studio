# 2027 桌曆封面（M-5 R33）

- 橫式：H-L1（Owner 已接受，與 R32 相同；來源在 `../cover_r32/H-L1.svg`）。
- 直式：`V-D2-R33.svg`＝R32 V-D2 只改年份的修正版，待 Owner 確認。
  - 「2027」：同一字型（Cormorant Garamond Light）、同位置與大小，柔和香檳金到暖金黃的上下漸層，加一層輕微的光暈。這是印刷圖稿中的金色視覺效果，不是燙金或金墨。
  - 背景、置中編排、留白、白色 Logo、細線與白色「兌心科技」都與 R32 V-D2 相同（Owner 決定維持原本白色 Logo）。
  - `brand/`：Penny 提供的藍色圓底 Logo 原檔與紀錄（試放後未採用，見 `brand/SOURCE.md`）。
- 字型在 `fonts/`（SIL OFL，授權書隨附）。
- 重建：`python3 docs/calendar/tools/build_cal_m5_cover_r33.py`（`--check` 會重建並與 repo 逐檔比對）。
