# 2027 桌曆封面（M-5 R33）

- 橫式：H-L1（Owner 已接受，與 R32 相同；來源在 `../cover_r32/H-L1.svg`）。
- 直式：`V-D2-R33.svg`＝R32 V-D2 的修正版，待 Owner 確認。
  - 背景、置中編排與留白沿用 R32 V-D2。
  - 「2027」：同一字型（Cormorant Garamond Light），柔和香檳金到暖金黃的上下漸層，加一層輕微的光暈。這是印刷圖稿中的金色視覺效果，不是燙金或金墨。
  - Logo：Penny 提供的藍色圓底白字原檔（`brand/insight-software-logo-circle.png`，來源與核對見 `brand/SOURCE.md`），直徑 22 mm。
  - 「兌心科技」：淡香檳白，與圓形 Logo 並排。
- 字型在 `fonts/`（SIL OFL，授權書隨附）；SVG 以相對路徑載入字型與 Logo。
- 重建：`python3 docs/calendar/tools/build_cal_m5_cover_r33.py`（`--check` 會重建並與 repo 逐檔比對）。
