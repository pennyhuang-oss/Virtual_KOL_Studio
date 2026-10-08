# CAL_03b — 主視覺候選圖逐張判定（程式產生，請勿手改）

> 由 `docs/calendar/tools/build_cal_r1.py` 產生。判定與瑕疵文字來自 `data/cal_r1_casting.json`（人寫）；
> 像素、長寬比、有效 ppi、裁切保留比例由程式從原檔現算。框尺寸與 ppi 分級是本輪假設，不是廠商要求。

| 月 | 人設 | 版面 | 原圖（repo 路徑） | 原圖 px | 長寬比 | 原圖/縮圖 | 框 mm | 有效 ppi | 裁切保留 | 判定 | 瑕疵與裁切備註 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Iris Chen | 橫式半版 | `kols/iris-chen/images/training_v1/06_cafe_window_02.webp` | 1920×2560 | 0.75 | 原圖 | 102×155 | 420（充裕） | 88% | 可直接用 | 無明顯瑕疵；窗邊高光略過曝 |
| 1 | Iris Chen | 直式滿版 | `kols/iris-chen/images/training_v1/02_taipei_street_02.webp` | 1920×2560 | 0.75 | 原圖 | 144×204 | 319（充裕） | 94% | 可直接用 | 背景招牌是 AI 假字（小、可選修） |
| 2 | Kanon Komori | 橫式半版 | `kols/kanon-komori/images/training_v1/train_02.jpg` | 1728×2304 | 0.75 | 原圖 | 102×155 | 378（充裕） | 88% | 可直接用 | 背景黑板是 AI 假字（可接受） |
| 2 | Kanon Komori | 直式滿版 | `kols/kanon-komori/images/training_v1/train_01.jpg` | 1728×2304 | 0.75 | 原圖 | 144×204 | 287（可） | 94% | 可直接用 | 無明顯瑕疵；線圈區壓到瀏海上緣（不傷臉） |
| 3 | Luna Tanaka | 橫式半版 | `kols/luna-tanaka/images/soul_test_v1/03_cafe_window_01.png` | 1152×2048 | 0.5625 | 原圖 | 102×155 | 287（可） | 85% | 需修圖 | 左上有假 IG 介面字樣「Plaremgilent 1.g」、右上「×」，半版裁切後仍在框內 |
| 3 | Luna Tanaka | 直式滿版 | `kols/luna-tanaka/images/soul_test_v1/01_tokyo_street_01.png` | 1152×2048 | 0.5625 | 原圖 | 144×204 | 203（邊緣） | 80% | 需修圖 | 畫面乾淨，但原圖只有 1152 px 寬，直式滿版約 203 ppi（解析度邊緣） |
| 4 | Angel Chiu | 橫式半版 | `kols/angel-chiu/images/training_v1/train_02.jpg` | 1728×2304 | 0.75 | 原圖 | 102×155 | 378（充裕） | 88% | 可直接用 | 胸前識別證是空白卡（可接受） |
| 4 | Angel Chiu | 直式滿版 | `kols/angel-chiu/images/training_v1/train_01.jpg` | 1728×2304 | 0.75 | 原圖 | 144×204 | 287（可） | 94% | 可直接用 | 床上有識別證掛繩（可留、可修） |
| 5 | Somi Oh | 橫式半版 | `kols/somi-oh/images/training_v1/train_01.jpg` | 1728×2304 | 0.75 | 原圖 | 102×155 | 378（充裕） | 88% | 可直接用 | 炸雞紙盒配色像品牌包裝（無可讀 logo） |
| 5 | Somi Oh | 直式滿版 | `kols/somi-oh/images/training_v1/train_02.jpg` | 1728×2304 | 0.75 | 原圖 | 144×204 | 287（可） | 94% | 可直接用 | 吃串燒張嘴，親和但不性感；若要更甜，取回 daily_v2 原圖 #065/#126（海邊白洋裝） |
| 6 | Vicky Lin | 橫式半版 | `kols/vicky-lin/images/face_reference/v3_01_front_headshot.png` | 1152×2048 | 0.5625 | 原圖 | 102×155 | 287（可） | 85% | 需修圖 | 短褲上有 Nike 勾勾商標；背景路人 |
| 6 | Vicky Lin | 直式滿版 | `kols/vicky-lin/images/face_reference/v4_anchored_05_3q_halfbody.png` | 1440×2560 | 0.5625 | 原圖 | 144×204 | 254（可） | 80% | 可直接用 | 無明顯瑕疵（運動內衣上的標誌是虛構的） |
| 7 | Coco Wu | 橫式半版 | `kols/coco-wu/images/face_reference/candidate_01.png` | 1440×2560 | 0.5625 | 原圖 | 102×155 | 359（充裕） | 85% | 可直接用 | 無明顯瑕疵 |
| 7 | Coco Wu | 直式滿版 | `kols/coco-wu/images/face_reference/candidate_03.png` | 1440×2560 | 0.5625 | 原圖 | 144×204 | 254（可） | 80% | 可直接用 | 背景手機螢幕顯示她自己的照片（可接受） |
| 8 | Mia Huang | 橫式半版 | `kols/mia-huang/images/training_v1/02_gaming_chair_selfie.png` | 1440×2560 | 0.5625 | 原圖 | 102×155 | 359（充裕） | 85% | 可直接用 | 霓虹紫光色偏重，印刷色差需打樣確認 |
| 8 | Mia Huang | 直式滿版 | `kols/mia-huang/images/training_v1/13_stretch_break_candid.png` | 1440×2560 | 0.5625 | 原圖 | 144×204 | 254（可） | 80% | 可直接用 | 無明顯瑕疵；同樣是紫光 |
| 9 | Yuna Kim | 橫式半版 | `kols/yuna-kim/images/face_reference/ref_01.webp` | 1728×2304 | 0.75 | 原圖 | 102×155 | 378（充裕） | 88% | 可直接用 | 無明顯瑕疵；韓文招牌為背景 |
| 9 | Yuna Kim | 直式滿版 | `kols/yuna-kim/images/soul_test_v1/street_02.png` | 1152×2048 | 0.5625 | 原圖 | 144×204 | 203（邊緣） | 80% | 需修圖 | 肩背包疑似 GG 類老花、裙子近似名牌格紋；原圖 1152 px 寬，直式滿版約 203 ppi |
| 10 | Tammy Chou | 橫式半版 | `kols/tammy-chou/images/training_v1/train_03.jpg` | 1728×2304 | 0.75 | 原圖 | 102×155 | 378（充裕） | 88% | 需補生成 | 自拍手臂入鏡、頭髮綁起看不出蜜金大波浪、灰襯衫素色，辨識度弱 → 不採用；先取回 daily_v2 原圖（#075/#130 頂樓黑洋裝），不行再補生成 |
| 10 | Tammy Chou | 直式滿版 | `kols/tammy-chou/images/training_v1/train_01.jpg` | 1728×2304 | 0.75 | 原圖 | 144×204 | 287（可） | 94% | 可直接用 | 紙箱上有假條碼標籤（小） |
| 11 | Rin Ayase | 橫式半版 | `kols/rin-ayase/images/training_v1/train_02.jpg` | 1728×2304 | 0.75 | 原圖 | 102×155 | 378（充裕） | 88% | 可直接用 | 無明顯瑕疵 |
| 11 | Rin Ayase | 直式滿版 | `kols/rin-ayase/images/training_v1/train_01.jpg` | 1728×2304 | 0.75 | 原圖 | 144×204 | 287（可） | 94% | 可直接用 | 側身回頭、臉在右上偏小，辨識度中等 |
| 12 | Rainie Hsu | 橫式半版 | `kols/rainie-hsu/images/training_v2/04_leaving_apartment_ccd.png` | 1440×2560 | 0.5625 | 原圖 | 102×155 | 359（充裕） | 85% | 需修圖 | 右下有假日期戳記（2023/18/0?）；鏡面閃光與鏡中反射人影 |
| 12 | Rainie Hsu | 直式滿版 | `kols/rainie-hsu/images/training_v2/03_doorway_reveal_candid.png` | 1440×2560 | 0.5625 | 原圖 | 144×204 | 254（可） | 80% | 可直接用 | 人物在門框裡偏小，月份主視覺辨識度中等 |
| 備 | Wanyin Jiang | 橫式半版 | `kols/wanyin-jiang/images/training_v1/train_05.jpg` | 1728×2304 | 0.75 | 原圖 | 102×155 | 378（充裕） | 88% | 可直接用 | 無明顯瑕疵 |
| 備 | Wanyin Jiang | 直式滿版 | `kols/wanyin-jiang/images/training_v1/train_04.jpg` | 1728×2304 | 0.75 | 原圖 | 144×204 | 287（可） | 94% | 可直接用 | 全身照人物比例中等 |
| 備 | Sophia Tseng | 橫式半版 | `kols/sophia-tseng/images/training_v1/08_home_candid_sofa_wine.png` | 1440×2560 | 0.5625 | 原圖 | 102×155 | 359（充裕） | 85% | 可直接用 | 無明顯瑕疵 |
| 備 | Sophia Tseng | 直式滿版 | `kols/sophia-tseng/images/training_v1/01_morning_window_candid.png` | 1440×2560 | 0.5625 | 原圖 | 144×204 | 254（可） | 80% | 需補生成 | 側臉背影、臀部入鏡，辨識度弱 → 不採用；training_v1 其他 12 張可再挑 |

## 橫式滿版（204×155）若直接用上表的直幅原圖

| 月 | 人設 | 有效 ppi | 裁切保留 | 結論 |
|---|---|---|---|---|
| 1 | Iris Chen | 239（邊緣） | 57% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 2 | Kanon Komori | 215（邊緣） | 57% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 3 | Luna Tanaka | 143（不足） | 43% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 4 | Angel Chiu | 215（邊緣） | 57% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 5 | Somi Oh | 215（邊緣） | 57% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 6 | Vicky Lin | 143（不足） | 43% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 7 | Coco Wu | 179（不足） | 43% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 8 | Mia Huang | 179（不足） | 43% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 9 | Yuna Kim | 215（邊緣） | 57% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 10 | Tammy Chou | 215（邊緣） | 57% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 11 | Rin Ayase | 215（邊緣） | 57% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |
| 12 | Rainie Hsu | 179（不足） | 43% | 不採用：只剩頭到胸的一條，日期條會壓到下巴或胸口 |

## 計數（只算 12 位主角）

- 橫式（半版）判定：{"可直接用": 8, "需修圖": 3, "需補生成": 1}
- 直式（滿版）判定：{"可直接用": 10, "需修圖": 2}
- 不同原圖數：橫式 12、直式 12、兩款共用 0、合計 24
- 版面使用次數：橫式 12、直式 12（每月一個主視覺；封面與其他頁另計）
- 需新生成（主視覺）：橫式 1、直式 0（若改用橫式滿版，另需 12 張原生橫幅或外擴圖）
