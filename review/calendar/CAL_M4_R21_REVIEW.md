TASK-CAL-001／M-4／R21｜Owner 回饋修正批次與 Railway 更新｜執行紀錄

# M-4 R21 執行紀錄

- 起點 HEAD：`0286b9a8e1600c821507103716f08bbd5a6da7c2`
- 原圖、調色衍生檔與生成紀錄 commit：`03eb250c4baedbae4dc85b85594bf17ca229872e`
- 選片頁成果 commit（部署用）：`537fa19764a8ec247bff4e3d338972fd793ec3a9`
- 本輪：送出 20 次請求、產出 19 張（H-Miu B 被平台內容審查擋下、已退款）、實扣淨額 2.28（20 × 0.12 − 0.12，依時窗推定）；重試 0、補生 0、付費修圖 0；本機調色 3 張（不計費）

## 主管報告

```
TASK-CAL-001／M-4／R21｜Owner 回饋修正批次與 Railway 更新｜Claude 執行回報

起點 HEAD：0286b9a　原圖／調色 commit：03eb250　選片頁成果 commit（部署用）：537fa19　紀錄 commit：本檔所在 commit
本輪：送出 20、產出 19、實扣淨額 2.28（20 × 0.12 − 退款 0.12，依時窗推定）；重試 0、補生 0、付費修圖 0；本機調色 3
Railway：只更新既有 cal2027-decision，部署進行中（線上驗收後補記）；其他服務未動

一、Owner 回饋與選定
- Penny 頁面「複製全部回饋」原文（ff40631）沒有隨 R21 指令交來：Owner 紀錄 page_copy 標「交接缺件」、text 留空，不用摘要代替；R21 指令全文逐字存 instruction_verbatim
- 依 R21 指令整理：本輪選定 11 套＋先前 3 套＝14 套已選定
  無修改 7：H-Yuna B、H-Iris A、H-Jia B、H-Rainie B、V-Mia A、V-Coco B、V-Yerin A（＋V-Iris、V-Tammy R14、V-Rin R14）
  選定來源＋修改待確認 4：H-Rin R20 A（改善候選 2 張）、H-Coco R20 A、V-Miu R20 B、V-Luna R20 B（各 1 張調色）
  退回 9：H-Miu、H-Tammy、H-Yerin、H-Mia、H-Luna、H-Somi、V-Jia、V-Rainie、V-Yuna；V-Somi 不動
- 進度：24 套＝已接受 10＋已選定待確認修改 4＋待 Penny 選片 9＋退回待重規劃 1（V-Somi）＋尚未生成 0；修改版不宣稱已接受

二、本機調色 3 張（review/calendar/m4_r21/grade.py；紀錄 docs/calendar/data/cal_m4_r21_grading.json）
- 逐張參數：H-Coco A 明暗曲線 gamma 0.84＋自然飽和度 0.16（中位亮度 0.322→0.387）；V-Miu B 以同套 A 的亮度分位數 85% 匹配、最亮處只小幅提升（中位 0.481→0.490、p95 0.805→0.867，接近 A 的 0.878）；V-Luna B gamma 0.88＋自然飽和度 0.08（中位 0.275→0.322）
- 共通保護：膚色區只小幅提升飽和、提升不把色版推過 1、0.9 以上高光柔肩；三張剪白比例與原圖相同（3.8%／0.06%／0.03%，前者是夕陽本身）
- 衍生檔另存 *_m4r20_<v>_grade_r21.png，原圖不動；只調色，不改臉、身體、服裝、姿態或場景；網站提供原版／調色版比較，並註明螢幕亮度不代表印刷效果

三、生成 10 套（prompt：docs/calendar/data/cal_m4_r21_prompts.json，含 sha256；規格 review/calendar/m4_r21/specs.py＋assemble.py）
- 設定：本人既有 Soul（10 個皆 ready）、soul_2、2k、橫 16:9／直 3:4；無參考圖、不傳 style、不用 unlim；唯讀報價橫直各 0.12；預估 2.40 未超上限
- 平台同時進行上限 8 件：分 3 批（8、8、4）；清冊先存意圖再存任務 ID，20 個 ID 唯一、無重複送出
- 設計重點：H-Rin 頭靠抱枕／半躺、肩肘腕有承托；H-Miu 趴床抬腿、跪坐撩髮；H-Tammy 紫藤＋奶油色（取代桃紅）、拉近景別放大臉部、補 canon 臉型句；H-Yerin 坐草地曬太陽、無球桿；H-Mia 夕陽／晚霞為主光、扶欄杆或走棧道；H-Luna 回頭一瞬、香袋垂在手邊、和服長及腳踝；H-Somi 改 11 月芒草原黃金時刻；V-Jia 改極簡美術館冬光；V-Rainie 低機位微仰、雙眼看鏡頭；V-Yuna 保留銀杏大道、改走路／低頭街拍
- 扣款：本批時段 Soul V2 支出 20 列各 −0.12、退款 1 列 +0.12（緊接 nsfw 之後），淨額 −2.28；餘額 1263.67→1261.39；他人其他模型列不檢視、不歸入

四、Claude 自查（不是主管覆核，也不是 Penny 決定；19 張全保留，不重生）
- 改善明顯：H-Rin 兩張放鬆有承托；H-Miu A 撩人自然（對照身分基準與 5 張訓練圖，臉與嬌小上圍比例一致；趴姿腰臀只能部分核對）；H-Yerin 兩張坐草地自然、無球桿；H-Mia 人景光線一致、不再像假布景；H-Luna 兩張自然、香袋不像商品、和服長度對；H-Somi 芒草原秋意；V-Jia 美術館構圖乾淨；V-Rainie 低機位腿長自然、雙眼看鏡頭
- 問題：H-Tammy B 整張轉了 90 度、不能直接作橫式（轉正後身分相符度高）；H-Tammy A 臉是仰起側面閉眼、身分不易判斷；H-Miu B 被平台擋下缺件；H-Yerin 兩張遠處仍有旗桿；V-Yuna 背景仍有招牌字、B 沒有低頭偏站定；H-Rin 新候選 2 沒照設計把手臂搭椅背
- 逐張全文：docs/calendar/data/cal_m4_r21_trial.json

五、選片頁 https://cal2027-decision-production.up.railway.app/shoot.html
- 上方集中本輪待確認 13 項：9 套新候選（A／B／兩張都想修改；H-Miu 只有 A，B 標缺件）、H-Rin（保留原 A／新候選 1／新候選 2／仍想修改）、3 張調色（用調色版／維持原版／調色還想修改，原版與調色版並排）
- 下方「已選」14 套只看不選（4 套標修改待確認）；V-Somi 標待處理
- 新回饋鍵 cal2027-pick-r21-v1:<套別>，綁定圖片識別、對不上不套用；R20 與更舊的鍵不讀、不寫、不刪；備註、重新整理保存與複製全部回饋保留
- 頁面不放 prompt、設計理由或技術報告；公開圖去除中繼資料
- 線上驗收：部署進行中（線上驗收後補記）；本機 Playwright 驗收（桌機 1280、手機 390）全數通過

六、計數與檢查
- 月面照片累計 73 張／8.76 credits；構圖底稿 2 張／4 credits；合計 12.76
- 檢查：CAL_18–22 --check PASS、CAL_23 --check PASS（CAL_19 不變）、builder --check PASS（743 檔、選片頁 72、問題 0、公開檔無私有 ID）
- 未合併 main、未聯絡廠商、V-Somi 未動

七、需要 Penny／主管
- 請 Penny 補貼 R20 頁面「複製全部回饋」原文，以便逐字存入 Owner 紀錄
- H-Tammy B 方向錯誤的處理方式（本輪依指令不補生）
```
