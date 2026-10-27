TASK-CAL-001／M-4／R14｜Tammy、Rin 各一張重製試拍｜送審報告

# M-4 R14 送審紀錄

- 固定成果 commit：`cb1db65090dc2ddc767cc45ad8fa23617fdf9377`（起點 `aa08221`）
- 本輪：生成 2（各 1 次請求）、實扣 0.24（各 0.12，依時窗推定）；重試 0、補生 0、上傳 0、訓練 0、部署 0。

## 主管報告

```
TASK-CAL-001／M-4／R14｜Tammy、Rin 各一張重製試拍｜Claude 執行回報

起點 HEAD：aa082219b02ccb8fd7bc43185d55e75eae3b2797　成果 commit：cb1db65　紀錄 commit：本檔所在 commit
本輪：生成 2、每張 1 次請求、實扣 0.12＋0.12＝0.24（依時窗推定）；重試 0、補生 0、Somi 0、Yerin 0、Jia 0

一、輸入
- prompt：docs/calendar/data/cal_m4_r13_cards.json，固定 commit bd84cf97a7310afa672d506895e09c8d73220408，逐字未改
  V-tammy-chou sha256 9c17fe21db59b9e26d0c0793e4bfa48dc19a55d723a61f838250d8f7e7cccb2b
  V-rin-ayase  sha256 fa6975f39db1eb51006004d278910b57e800243acebdfe4945e47a33723e3eeb
- 設定：本人既有 Soul（兩個皆 ready）、soul_2、2k、3:4、count 1；無參考圖、不傳 style、不用 unlim
- 送出前：唯讀報價各 0.12；本案沒有進行中或重複任務
- 任務紀錄：prompt 與送出相同、enhance_prompt=false（沒有被改寫）；後端另記 style「General」（預設，我們沒傳）、quality 欄位 1080p（實際輸出 1536×2048）

二、交付（review/calendar/m4_r14/）
- 每張：完整顯示版 _view.jpg、120×160 套框 _frame_V_120x160.jpg、與 R5 對照 _m4r5_vs_m4r14_compare.jpg（含身分基準臉部）
- 原圖：kols/tammy-chou/…/V-tammy-chou_m4r14.png（sha256 f4b1b1d4…）、kols/rin-ayase/…/V-rin-ayase_m4r14.png（sha256 6be6d9d8…），1536×2048、約 325 ppi

三、Claude 自查（不是主管覆核，也不是 Penny 接受）
Tammy：部分通過
- 值得收嗎：接近，氣氛、光色、身分都對；姿勢與腳貼邊要主管判斷
- 好：夜晚酒廊、右側落地燈暖主光、窗外深藍，冷暖對比到位；人與椅子、燈尺度合理；手與扶手接觸自然；比 R5 的商業站姿放鬆很多
- 問題：身體正對相機端坐，散場後的親密感不夠，仍有擺拍感；腳尖低於下緣 3% 安全線、貼邊；布料偏霧面，不像真絲緞面；燈罩略高於頭部
Rin：不通過
- 值得收嗎：目前不建議
- 好：身分一致、服裝與髮型都對、迴廊乾淨、透視自然、靠柱自然
- 問題：主題光影沒出現，臉是平光，陽光只在左側地面；她看鏡頭，沒有迎光、也沒有半垂眼，結果是人站在迴廊前的時裝或旅遊照；景別是全身，比計畫的膝上寬；靴尖低於下緣 3% 安全線、貼邊

四、計數與歷程
- 月面照片 11 張／1.32 credits（加 R14 2 張）；構圖底稿 2 張／4 credits；合計 5.32
- 24 套分類不變（只有 V-Iris 已接受；Tammy、Rin 仍列退回待重規劃，等主管看圖與 Penny 決定）
- 檢查：CAL_18–22 --check PASS、CAL_23 --check PASS（CAL_19 不變）、建置 --check PASS（671 檔、問題 0、公開檔無私有 ID）

五、狀態
- 待主管看圖；Penny 未表態
- 未部署、未改 V-Iris、未合併 main、未聯絡廠商；兩張完成後停止
```
