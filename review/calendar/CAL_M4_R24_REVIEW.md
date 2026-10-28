TASK-CAL-001／M-4／R24｜Rainie 回歸人設與早期成功身分流程｜執行紀錄

# M-4 R24 執行紀錄

- 起點 HEAD：`2b8b37a`
- 原圖與生成紀錄 commit：`106edbfc9eb55f288a3aa3aff0cd309b4cee6461`
- 選片頁成果 commit（部署用）：`0097adaf0927d920a29070ad2b45454c00150f01`
- 本輪：V-Rainie 送出 2 次請求、產出 2 張，實扣 2 credits（每張 1，依時窗推定），未超過總上限 2；重試 0、補生 0、新建身分素材 0

## 主管報告

```
TASK-CAL-001／M-4／R24｜Rainie 回歸人設與早期成功身分流程｜Claude 執行回報

起點 HEAD：2b8b37a　原圖／生成紀錄 commit：106edbf　選片頁成果 commit（部署用）：0097ada　紀錄 commit：本檔所在 commit
本輪：V-Rainie 送出 2、產出 2；實扣 2 credits（完整報價每張 1、共 2，未超過上限）；重試 0、補生 0、訓練 0、新建身分素材 0
Railway：只更新既有 cal2027-decision，部署 1 次 SUCCESS，線上頁面版本 0097ada

一、Owner 決定與紀錄
- H-Somi R22-2-G23 正式接受（定案的是調色版本身）→ 23 套定案；只剩 V-Rainie；R23 A／B 退回
- Owner 原話逐字存 cal_m4_owner_r24.json，與執行者分析分開
- R22 頁面原文（fbf5674）逐字補存在 cal_m4_owner_r23.json 的 page_copy
- a606112 頁面原文沒有隨指令交來，標交接缺件

二、實際使用流程（已核對，不只看名稱）
- 早期成功紀錄（R23 查到的訓練集 v2 自拍任務）：
  · Seedream 4.5、quality basic
  · 以 prompt 佔位符嵌入既有 Reference Element「rainie-hsu-anchor-v2」；輸入圖為空
- 現況核對：
  · Element 仍在、狀態 completed
  · Element 內的錨點圖下載後與 face_reference/candidate_02.png 位元組相同
  · Seedream 4.5 可用、支援 3:4
  · 工具說明的輸入方式與早期紀錄一致（佔位符嵌入，不放 medias／input_images）
- 本輪：Seedream 4.5、basic、3:4（1728×2304），身分只由該 Element 提供
  · 送出後讀回兩個任務紀錄：同一 Element 與錨點媒體、輸入圖為空、prompt 與送出全文相同
- 沒有使用 Soul、v1 Element（另一張臉）或 R20–R23 任何圖片
  · 錨點只提供臉；場景、服裝、動作、構圖與人體比例依 canon 重新設計，未搬用早期照片的身體或自拍透視
- canon 重讀（profile.json、character.md）：
  · 24 歲成年、白皙膚色、沙漏身材與長腿、黑長直髮深側分、淺棕眼線不上揚、透亮唇彩、貼身洋裝＋高衩＋誇張飾品＋高跟鞋
  · 未改人設；prompt 不寫身高三圍數字、不寫占滿畫高或腳靠下緣
- 設計：5 月傍晚台北頂樓露台，香檳色緞面高衩貼身中長洋裝
  · A：欄杆邊自然站姿；B：自然行走
  · 朋友在約 5–6 公尺、胸口高度、50mm 平視拍全身

三、人體比例自查（先看整個人，再看身分與細節）
- A：頭、肩、軀幹、骨盆、腿關係自然，成年女性比例；約 7.0 頭身
  · 交叉腳站姿略有擺姿感；身形比 canon 纖細、胸型不夠飽滿；頭髮中分（設計是側分）；腳離下緣很近
- B：行走步伐、骨盆與雙腿銜接自然，雙手放鬆；約 7.7 頭身（含高跟鞋，偏長但在時尚全身照範圍）
  · 同樣偏纖細、中分；鞋尖離下緣很近
- 對照量測（同一方法，髮頂到下巴為一頭）：R20 A 約 5.1、R22 A 約 6.1、R23 B 約 5.8 頭身
  · 與 Penny「頭大身體小」的觀察一致；R24 兩張落在正常成年比例
- 身分：臉型、眉眼、鼻唇與錨點一致
- 雙眼看鏡頭、方向一致；眼線只剩極淡的外眼角上揚
- 人景：夕陽逆光與地面影子一致；A 背景可見台北 101
- 2 張全保留，不重生

四、選片頁 https://cal2027-decision-production.up.railway.app/shoot.html
- 只留 V-Rainie 待選：接受 A／接受 B／兩張都想修改＋備註；附前幾輪 8 張（只看不選）
- 已選 23 套全部定案，不要求重選
- 新回饋鍵 cal2027-pick-r24-v1，舊鍵不動，新圖不繼承舊接受狀態
- 頁面不放 prompt、模型或技術分析
- builder：Seedream 原圖多一個只含像素密度的 pHYs 區塊，放寬檢查為只允許 dpi；公開檔仍是不帶中繼資料的 JPEG
- 線上驗收：Playwright 桌機／手機 25 項全過（載圖、保存、複製、手機操作）；線上 66 圖檔無中繼資料與 ID

五、計數與檢查
- 進度：24＝23 定案＋1 待選（V-Rainie）
- 月面照片累計 85 張／11.96 credits；構圖底稿 2 張／4 credits；合計 15.96
- CAL_18–22 --check PASS、CAL_23 --check PASS（CAL_19 不變）
- builder --check PASS（737 檔、選片頁 66、問題 0）
- 本機與線上 Playwright 全過
- 扣款：送出時段 Seedream 4.5 支出 2 列各 −1；送出前已存在的同模型列不歸入；餘額 1095.19→1093.19
- 未合併 main、未聯絡廠商、未動定案照片

六、阻塞：無
- 待 Penny：V-Rainie A／B
- 若要保存 a606112 頁面原文，請 Penny 補貼
```
