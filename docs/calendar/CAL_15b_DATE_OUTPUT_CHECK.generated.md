# CAL_15b — 自繪日期「實際輸出頁」核對結果（程式產生，請勿手改）

> 由 `docs/calendar/tools/build_cal_r3_pages.py` 產生；原始資料 `data/cal_r3_date_check.json`。
> 方法：讀回實際輸出的 300 dpi JPEG，依格線幾何切出每一格（不用渲染時記下的文字位置），以同字型字形比對讀出數字或星期、以墨色判定紅黑；期望值以 `calendar.monthdayscalendar` 另行推算（渲染器用的是 `datetime`），紅字依人事總處放假日。每月固定 6 列，不併格。
> 負向測試：`tools/test_cal_r3_datecheck.py` 把 1 月橫 A 的輸出檔改成「1/4 改紅、1/15 擦掉、1/10 改寫成 9」，核對程式三處都抓到、沒有誤報（說明見 `CAL_08_DATES_2027.md` §6）。

| 頁 | 群組 | 檢查格數 | 讀到的日期 | 最低比對分數 | 失敗 |
|---|---|---|---|---|---|
| H_A_01_iris-chen | main | 49 | 31 | 0.965 | 0 |
| V_U_01_iris-chen | main | 49 | 31 | 0.939 | 0 |
| H_A_02_kanon-komori | main | 49 | 28 | 0.967 | 0 |
| V_U_02_kanon-komori | main | 49 | 28 | 0.954 | 0 |
| H_A_03_luna-tanaka | main | 49 | 31 | 0.967 | 0 |
| V_U_03_luna-tanaka | main | 49 | 31 | 0.699 | 0 |
| H_A_04_angel-chiu | main | 49 | 30 | 0.967 | 0 |
| V_U_04_angel-chiu | main | 49 | 30 | 0.697 | 0 |
| H_A_05_somi-oh | main | 49 | 31 | 0.969 | 0 |
| V_U_05_somi-oh | main | 49 | 31 | 0.946 | 0 |
| H_A_06_vicky-lin | main | 49 | 30 | 0.967 | 0 |
| V_U_06_vicky-lin | main | 49 | 30 | 0.948 | 0 |
| H_A_07_coco-wu | main | 49 | 31 | 0.967 | 0 |
| V_U_07_coco-wu | main | 49 | 31 | 0.697 | 0 |
| H_A_08_mia-huang | main | 49 | 31 | 0.967 | 0 |
| V_U_08_mia-huang | main | 49 | 31 | 0.696 | 0 |
| H_A_09_yuna-kim | main | 49 | 30 | 0.967 | 0 |
| V_U_09_yuna-kim | main | 49 | 30 | 0.699 | 0 |
| H_A_10_tammy-chou | main | 49 | 31 | 0.965 | 0 |
| V_U_10_tammy-chou | main | 49 | 31 | 0.939 | 0 |
| H_A_11_rin-ayase | main | 49 | 30 | 0.967 | 0 |
| V_U_11_rin-ayase | main | 49 | 30 | 0.699 | 0 |
| H_A_12_rainie-hsu | main | 49 | 31 | 0.967 | 0 |
| V_U_12_rainie-hsu | main | 49 | 31 | 0.699 | 0 |
| H_grid_09_yuna-kim | main | 49 | 30 | 0.969 | 0 |
| V_grid_12_rainie-hsu | main | 49 | 31 | 0.799 | 0 |
| V_year_2027 | main | 588 | 365 | 0.624 | 0 |
| V_A_01_iris-chen | compare | 49 | 31 | 0.95 | 0 |
| V_A_06_vicky-lin | compare | 49 | 30 | 0.946 | 0 |
| V_A_11_rin-ayase | compare | 49 | 30 | 0.942 | 0 |
| V_A_02_kanon-komori | compare | 49 | 28 | 0.704 | 0 |
| H_B_01_iris-chen | compare | 62 | 31 | 0.945 | 0 |
| H_B_02_kanon-komori | compare | 56 | 28 | 0.953 | 0 |
| H_B_03_luna-tanaka | compare | 62 | 31 | 0.951 | 0 |
| H_B_04_angel-chiu | compare | 60 | 30 | 0.703 | 0 |
| H_B_05_somi-oh | compare | 62 | 31 | 0.945 | 0 |
| H_B_06_vicky-lin | compare | 60 | 30 | 0.703 | 0 |
| H_B_07_coco-wu | compare | 62 | 31 | 0.945 | 0 |
| H_B_08_mia-huang | compare | 62 | 31 | 0.945 | 0 |
| H_B_09_yuna-kim | compare | 60 | 30 | 0.704 | 0 |
| H_B_10_tammy-chou | compare | 62 | 31 | 0.945 | 0 |
| H_B_11_rin-ayase | compare | 60 | 30 | 0.703 | 0 |
| H_B_12_rainie-hsu | compare | 62 | 31 | 0.945 | 0 |
| CHK_kanon_kanon_V_V_A | check | 49 | 28 | 0.704 | 0 |
| CHK_kanon_kanon_V_V_B_R2 | check | 49 | 28 | 0.708 | 0 |
| CHK_kanon_kanon_V_V_U | check | 49 | 28 | 0.954 | 0 |
| CHK_kanon_kanon_H_V_U | check | 49 | 28 | 0.954 | 0 |
| CHK_kanon_kanon_alt028_V_U | check | 49 | 28 | 0.954 | 0 |

合計：48 頁、3033 格、讀到 1780 個日期、失敗 0。
