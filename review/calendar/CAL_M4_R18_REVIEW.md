TASK-CAL-001／M-4／R18｜Yerin、Jia 各一張重製試拍｜送審報告

# M-4 R18 送審紀錄

- 固定成果 commit：`998a565f7735bb3159e9a3d3b92fe1845f548eda`（起點 `e82ed45`）
- 本輪：生成 2（各 1 次請求）、實扣 0.24（各 0.12，依時窗推定）；重試 0、補生 0、修圖 0、上傳 0、部署 0。

## 主管報告

```
TASK-CAL-001／M-4／R18｜Yerin、Jia 各一張重製試拍｜Claude 執行回報

起點 HEAD：e82ed45e136a2d12502bde01a72bf63cbdf0b26b　成果 commit：998a565　紀錄 commit：本檔所在 commit
本輪：生成 2、每張 1 次請求、實扣 0.12＋0.12＝0.24（依時窗推定）；重試 0、補生 0、修圖 0；Somi 未動

一、輸入
- prompt：docs/calendar/data/cal_m4_r13_cards.json，固定 commit bd84cf97a7310afa672d506895e09c8d73220408，逐字未改
  H-yerin-han sha256 5bb8c2c7aa6ffc84a8761b44be9581e2c0a49e5253a6374ac43ccce5e7ba3ca9
  H-jia-seo   sha256 1669f5e427317092d40689aa51d7e2a33dcfecdba66f3adc1d70896093d0c2f8
- 設定：本人既有 Soul（兩個皆 ready）、soul_2、2k、16:9、count 1；無參考圖、不傳 style、不用 unlim
- 送出前：唯讀報價各 0.12；本案沒有進行中或重複任務
- 任務紀錄：prompt 與送出相同、enhance_prompt=false（沒有被改寫）；後端預設 style General、quality 欄位 1080p（輸出 2048×1152）

二、交付（review/calendar/m4_r18/）
- 每張：完整顯示版 _m4r18_view.jpg、橫式套框 _m4r18_frame_H_192x104.jpg、與 R5 對照 _m4r5_vs_m4r18_compare.jpg（含身分基準臉部）
- 原圖 2048×1152，192 mm 寬約 271 ppi（與 R5 相同限制）

三、Claude 自查（不是主管覆核，也不是 Penny 接受）
Yerin：部分通過
- 整體：清晨球道清爽明亮（新綠、白、淺天藍），比 R5 球車照好很多
- 尺度：人與草地、樹林合理；遠處樹線前又出現一台球車與旗桿（prompt 寫 no carts/flags），球車比例看起來大致合理，但仍是多出來的物件
- 扶桿與接觸：雙手疊在握把上自然、桿長合理；但一腳屈膝抬起懸空、身體倚向斜放的球桿，姿勢不自然、重心不穩
- 其他：頭轉向左後方對鏡頭笑，不是望向球道；人物在中央偏左、約占高度九成；套框帽頂與鞋都在框內
Jia：部分通過
- 整體：粉紫晚霞、夕陽倒影、平台斜線與人物色彩協調，安靜有氛圍，寫真美感高
- 共同構圖：湖面在左、平台從右下斜入、人物坐在平台邊；人物約占高度八成，比計畫大、份量偏重，但風景仍清楚
- 服裝與坐姿：酒紅細肩帶長洋裝、米白開襟滑肩、棕色涼鞋合情境；坐在平台邊雙腳垂向水面、一手撐木板，自然
- 其他：回頭看鏡頭，不是望向湖面；太陽還在地平線上；臉部柔和正面光略亮於黃昏環境；套框頭與腳都在框內

四、計數與狀態
- 月面照片 14 張／1.68 credits；構圖底稿 2 張／4 credits；合計 5.68
- 已接受仍是 3（V-Iris、V-Tammy R14、V-Rin R14）；Yerin、Jia 待主管看圖、Penny 未決定
- 檢查：CAL_18–22 --check PASS、CAL_23 --check PASS（CAL_19 不變）、建置 --check PASS（671 檔、問題 0、公開檔無私有 ID）
- 未部署、未合併 main、未聯絡廠商；兩張完成後停止
```
