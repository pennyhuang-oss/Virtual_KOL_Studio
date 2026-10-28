TASK-CAL-001／M-4／R20｜批次製作並部署 Railway 選片頁｜執行紀錄

# M-4 R20 執行紀錄

- 起點 HEAD：`fdfa4cd7636e54af8ed822ea6fc0e75c1654e8b0`
- 原圖與生成紀錄 commit：`cf615afc7bf50e981cbb3c5fb933d7fb37690ddd`
- 選片頁成果 commit（部署用）：`ff4063100e3ef5f06a2dc4c994b8847eb3315707`；cal2027-decision 部署 1 次、狀態 SUCCESS，線上頁面版本 ff40631，線上 Playwright 驗收全數通過（`review/calendar/m4_r20/deploy.json`）
- 本輪：生成 40（20 套 × A、B，各 1 次請求）、實扣 4.80（40 × 0.12，依時窗推定）；重試 0、補生 0、修圖 0、上傳 0、訓練 0

## 主管報告

```
TASK-CAL-001／M-4／R20｜批次製作並部署 Railway 選片頁｜Claude 執行回報

起點 HEAD：fdfa4cd　原圖 commit：cf615af　選片頁成果 commit（部署用）：ff40631　紀錄 commit：70b9055、ccf23f5
本輪：生成 40（20 套 × A／B，各 1 次請求）、實扣 4.80（40 × 0.12，依時窗推定）；重試 0、補生 0、修圖 0、上傳 0、訓練 0
Railway：只更新既有 cal2027-decision，部署 1 次 SUCCESS；其他服務未動

一、範圍
- 20 套＝尚未生成 18 套（含 H-somi-oh）＋H-yerin-han、H-jia-seo
- V-somi-oh 依指令暫不處理；已接受 V-Iris、V-Tammy R14、V-Rin R14 不重生
- 解讀說明：H-somi-oh 屬「尚未生成的 18 套」，照授權生成；「Somi 暫不處理」解讀為 V-somi-oh。若 Penny 本意是兩套 Somi 都不做，H-Somi 兩張可不採用（已扣 0.24）

二、輸入與設定
- prompt：R6 v3 各套設計＋後續 Owner 決定直接組裝，未重開企劃審查
  公開清單 docs/calendar/data/cal_m4_r20_prompts.json（40 份、含 sha256、無 ID）；規格 review/calendar/m4_r20/specs.py
- B 版只改一項主要安排：取景 12 套、姿態 7 套、站位 1 套（H-Yerin）
- Yerin：雙腳平踩、球桿頭輕放草地不承重、手指放鬆；50mm 約 12 m，人小景大（A sha256 ce54b1d7158e…、B 378b431f3813…）
- Jia：臀部、雙腿、雙腳與涼鞋全在木板上、離水邊；35mm 約 7 m 廣角，讀出完整平台與湖景（A ebb0a6025739…、B 15ecaf8a7fe4…）
- 送出前自查修正 2 句（修正後才建立任務）：H-Rin B 鏡頭句 as she reclines→seated head height；H-Somi B 鏡頭與配置句跟著坐姿改
- 設定：本人既有 Soul（12 個皆 ready）、soul_2、2k、橫 16:9／直 3:4；無參考圖、不傳 style、不用 unlim、不訓練；不用 photobook page 收尾句
- 報價：唯讀報價橫、直各 0.12；預估 40 × 0.12 = 4.80，未超上限

三、送出與扣款
- 平台同時進行上限 8 件：第 1 批送 12 件、4 件被拒（未建立任務、未扣款）；之後每批 8 件依序送出原 prompt，共 5 批
- 清冊先存送出意圖、再存任務 ID；40 個任務 ID 皆唯一，無重複送出
- 下載 40/40，尺寸與任務識別相符；原圖只存私有 kols/
- 扣款：本批時段 40 列 Soul V2、各 −0.12，合計 −4.80；餘額 1309.87→1305.07；他人其他模型列不檢視、不歸入
- 任務紀錄抽查 4 筆（Rin B、Yerin A、Jia A、Somi B）：prompt 與送出一致、enhance_prompt false、後端預設 style General、quality 欄 1080p

四、Claude 自查（不是主管覆核，也不是 Penny 決定；40 張全保留供選片，不重生）
- Yerin：姿勢與手指改善、球桿不承重，人景比例比 R18 好；但 A 仍約占畫高七成多、遠處有一支旗桿；B 約五成
- Jia：腳與涼鞋全在木板上，平台與湖景讀得出；人物仍偏大、坐位靠近平台邊緣，太陽未完全落下
- 明顯瑕疵：
  H-Luna B 和服下襬過短、露出腿部
  H-Somi A／B、V-Yuna A／B 背景出現韓文字（設計是無字）
  V-Miu A／B 背景出現吊床（設計寫不要）
  V-Mia A 取景比計畫寬；V-Yerin B 海平線露出太陽
  H-Somi A 單腳抬起偏刻意；H-Miu B 雙手接近扠腰
- 其餘各套場景、服裝、光色大致到位；逐套全文見 docs/calendar/data/cal_m4_r20_trial.json

五、選片頁 https://cal2027-decision-production.up.railway.app/shoot.html
- 橫式／直式分頁＋月份與角色導覽；一次一套，A、B 並排完整顯示不裁切，可放大、切原尺寸、A／B 互切
- 每套「接受 A」「接受 B」「兩張都想修改」＋備註；預設未回覆、不算接受；可清除選擇
- 「複製全部回饋」含角色、月份、圖片版本、選擇與備註
- 回饋存同一瀏覽器：新鍵 cal2027-pick-r20-v1:<套別>，綁定圖片識別，對不上不套用；舊鍵不讀、不寫、不刪
- 已接受 3 套放獨立區；Somi 標待處理，舊圖不列候選
- 頁面不放 prompt、自查、參數、費用或紀錄；公開圖去除中繼資料（顯示版長邊 1600＋原尺寸 JPEG）
- 線上驗收（Playwright，桌機 1280、手機 390）全數通過：圖片載入、A／B 對應、放大、選擇、備註、重新整理保留、複製、手機操作
- 線上 80 個候選圖檔無中繼資料、無 Soul／任務 ID

六、計數與檢查
- 月面照片累計 54 張／6.48 credits；構圖底稿 2 張／4 credits；合計 10.48
- 24 套＝已接受 3＋待 Penny 選片 20＋退回待重規劃 1（V-somi-oh）＋尚未生成 0；接受數不變
- 進度分類由三類改為四類（加入「待 Penny 選片」），CAL_18／21／23 與 builder 斷言同步
- 檢查：CAL_18–22 --check PASS、CAL_23 --check PASS（CAL_19 不變）、builder --check PASS（757 檔、選片頁 86、問題 0、公開檔無私有 ID）
- 未合併 main、未聯絡廠商

七、請主管確認
- H-Somi 範圍解讀是否正確（見一）
- 依指令未等主管覆核即部署；是否需在 Penny 選片前先看圖
```

## 範圍

- 剩餘 20 套：尚未生成的 18 套（含 H-somi-oh）＋H-yerin-han、H-jia-seo。V-somi-oh 暫不處理；已接受 V-iris-chen、V-tammy-chou R14、V-rin-ayase R14 不重生。
- 設定：各人既有 Soul、soul_2、2k；橫式 16:9、直式 3:4；無參考圖、不傳 style、不用 unlim、不訓練；不用已移除的 photobook page 收尾句。
- prompt：R6 v3 各套設計＋後續 Owner 決定直接組裝（`docs/calendar/data/cal_m4_r20_prompts.json`，含 sha256；產生規格 `review/calendar/m4_r20/specs.py`）。B 版只改一項主要安排（取景、站位或姿態）。
- Yerin：雙腳平踩草地、球桿頭輕放草地不承重、手指放鬆；人小景大（50mm、約 12 m）。Jia：臀部、雙腿、雙腳與涼鞋全在木板上、離水邊一段距離；35mm、約 7 m 廣角讀出完整平台與湖景。
- 送出前自查修正 2 句（H-rin-ayase B、H-somi-oh B 的鏡頭／配置句跟著坐姿改），修正後才建立任務。

## 生成與扣款

- 送出前：12 個 Soul 皆 ready；唯讀報價橫、直各 0.12（批次工具不支援報價，40 × 0.12 = 4.80，不超過上限）。
- 第 1 批送 12 件時平台同時進行上限 8 件，4 件被拒、未建立任務、未扣款；之後每批 8 件依序送出（共 5 批）。清冊保存送出意圖與任務 ID（私有 `review/calendar/m4_r20/execution_log.json`），40 個任務 ID 皆唯一、無重複送出。
- 下載：40/40 原圖尺寸與任務識別相符（`kols/<人設>/images/calendar_2027_batch1/<套別>_m4r20_<A|B>.png`）。
- 扣款：本批時段 40 列 Soul V2、每列 −0.12，合計 −4.80；餘額 1309.87 → 1305.07。他人其他模型的列不檢視、不歸入。
- 任務紀錄抽查 4 筆（index 3、8、16、21）：prompt 與送出版本一致、enhance_prompt false、平台預設 style General、quality 欄 1080p。

## Claude 自查（不是主管覆核，也不是 Penny 決定；40 張全部保留供選片，不重生）

全文見 `docs/calendar/data/cal_m4_r20_trial.json`。重點：
- Yerin：姿勢與手指改善、球桿不承重；人景比例比 R18 好，但 A 仍約占畫高七成多，A 遠處有一支旗桿。
- Jia：腳與涼鞋全在木板上，平台與湖景讀得出；人物仍偏大、坐位靠近平台邊緣，太陽未完全落下。
- H-Luna B 和服下襬過短；H-Somi、V-Yuna 背景出現文字；V-Miu 背景出現吊床；V-Mia A 取景比計畫寬；V-Yerin B 露出太陽。
- 其餘各套場景、服裝與光色大致到位。

## 選片頁（https://cal2027-decision-production.up.railway.app/shoot.html）

- 依橫式／直式分頁、月份與角色導覽；一次一套，A、B 並排（手機上橫式上下排），完整顯示不裁切，可點開放大、切原尺寸、A／B 互切。
- 每套選項「接受 A」「接受 B」「兩張都想修改」＋備註；預設「未回覆」，不算接受；可清除選擇。
- 「複製全部回饋」含角色、月份、選中的圖片版本（img_id）、選擇與備註。
- 回饋存同一瀏覽器（鍵 `cal2027-pick-r20-v1:<套別>`，記下 img_id；對不上就不套用）；舊鍵不讀、不寫、不刪。
- 已接受 Iris、Tammy R14、Rin R14 放獨立「已接受」區；Somi 標待處理、舊圖不列候選。
- 頁面不放 prompt、設計理由、自查、技術參數、費用或執行紀錄；公開圖去除中繼資料（顯示版長邊 1600、原尺寸 JPEG），公開檔掃描無 Soul ID、任務 ID、交易原始資料。
- 舊 M-4 R5 檢視頁程式與資料保留在 public（不再由 shoot.html 載入）。

## 計數與檢查

- 月面照片累計 54 張／6.48 credits；構圖底稿 2 張／4 credits；合計 10.48。
- 24 套＝已接受 3＋待 Penny 選片 20＋退回待重規劃 1（V-somi-oh）＋尚未生成 0；接受數不變。
- 檢查：CAL_18–22 --check PASS、CAL_23 --check PASS（CAL_19 不變）、建置 --check PASS（757 檔、選片頁 86、問題 0）；本機 Playwright 驗收（桌機 1280、手機 390）全數通過。
- 未合併 main、未聯絡廠商、未動其他 Railway 服務。
