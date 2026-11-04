TASK-CAL-001／M-5／R36｜加強橫式「2027」字體光感｜執行紀錄

# M-5 R36 執行紀錄

- 起點 HEAD：`5c87d5d`
- 成果 commit（部署用）：`f1b2947bacc95f96803df80c86fcf7a43a32404b`
- 本輪：生成 0、付費 0、上傳 0、購買素材 0；部署 1 次
- Owner 回饋與 R36 指令逐字：`docs/calendar/data/cal_m5_owner_r36.json`；修改紀錄與量測（分開保存）：`docs/calendar/data/cal_m5_r36_design.json`
- 工具：`docs/calendar/tools/build_cal_m5_cover_r36.py`（`--check` 可完整重建比對，並確認只有年份附近改變）
- 加強版與 PDF 紀錄：`docs/calendar/data/cal_m5_cover_r36.json`；部署：`review/calendar/m5_r36/deploy.json`

## 主管報告

```
TASK-CAL-001／M-5／R36｜加強橫式「2027」字體光感｜Claude 執行回報

版本
- 起點 5c87d5d；成果 commit（部署用）f1b2947；紀錄 commit＝本檔所在 commit
- 線上版本 f1b2947（頁面 meta 與 Railway 一致）
- 本輪：生成 0、付費 0、上傳 0、購買素材 0；部署 1 次 SUCCESS（07:07→07:15 UTC），只更新 cal2027-decision
- 未合併 main、未聯絡廠商、未打樣、未下單、未送印
比較網址：https://cal2027-decision-production.up.railway.app/layout.html#cover

一、Owner 回饋
- 原話：「那能再叫他加強一點嗎？就是真的要有像直式的那一種，是有光線的字的那種感覺。」

二、加強版 H-L1-R36L（只改 2027，取代 R35 的淡光暈；不是只加大模糊）
- 字形內部：上下漸層，參考直式金色年份「上亮下深」的受光方式，改用藍色
  - 上緣受光的亮藍 #7A92F2 → #5770E0 → #30419F → 下半部保留原本深藍 #1E2A78
- 外光：同一字形複本模糊三層
  - 極淡亮光：3.4 mm／0.6
  - 淡藍外光：2.0 mm／0.55，透明度上強下弱，光集中在受光的上緣，下緣不起霧
  - 貼字緣微光：0.7 mm／0.18
- 比較過的強度
  - 較淡的漸層：亮部不夠明顯
  - 整圈均勻外光：下緣起霧
  - 更亮的漸層與外光：接近霓虹
  - 選了亮部明顯、不刺眼、下緣乾淨的這一組
- 不變：年份字型、大小、位置、背景、Logo、公司名稱、品牌區與其他元素；字本體不模糊；無描邊、浮雕、星芒、投影

三、效果差異（完整封面為準）
- 完整封面顯示尺寸（1205 px 寬）量年份字形
  - R36：上緣 1/4 平均亮度 129.7（#677FE8），下緣 1/4 為 45.2（原本深藍）
  - R35：上下都約 45，沒有受光面
- 看圖
  - 不放大也看得出 2027 上緣亮藍、往下漸深，像受光的字；外光可察覺但不刺眼、不成霓虹
  - 縮到約 300 px 寬，亮部仍看得出、數字清楚
  - 600 dpi：上緣細筆畫（2 的勾、7 的橫）是亮藍、邊緣俐落，沒有被光吃掉；下緣深藍乾淨、無霧邊

四、核對
- 與 R35、與 R32 原版用同一流程各算一次 300 dpi 圖逐像素比較：變動全部在年份外擴 11 mm 內，範圍外 0（背景與品牌區不變）
- R35 與 R32 重算結果與已交付預覽位元組相同
- PDF
  - 年份為向量裁切＋線性漸層；外光在 300 dpi 背景點陣裡
  - 中文、細線、Logo 同 R32；字型子集嵌入
  - 讀回與預覽平均差 0.96
  - 28 面，內頁與 R26 逐頁相同；照片框 192×108 mm
- R32 的 PDF 函式加了可選的年份漸層參數（預設不變）；R32、R35 工具 --check 仍 PASS

五、交付位置
- 可編輯來源：docs/calendar/cover_r36/H-L1-R36L.svg（＋fonts、README）
- 預覽：docs/calendar/decision_site/public/cover36/
  - 加強版全圖：cover_H-L1-R36L_{v,f}.jpg（f＝300 dpi，2410×1831）
  - 年份局部：year_H-L1-R36L_600dpi.jpg（與 R35 的 cover35/year_H-L1-R35G_600dpi.jpg 同一取法）
- 橫式 28 面完整預覽 PDF：cover36/cal2027_H_preview_R36.pdf（封面＝加強版，標待確認）
- R35 保留供比較（cover35/）；直式 V-D2-R34B 已定案未動（PDF 沿用 cover35/cal2027_V_preview_R35.pdf）

六、網站（只動 layout.html#cover）
- 直式 V-D2-R34B「已接受」，不需選擇
- 橫式 R35／R36 並排：全圖可放大，年份 600 dpi 局部可點開，各自附 PDF
- 「接受加強版／維持 R35／還要修改」＋備註＋複製封面回饋（含頁面版本、圖片版本、版本識別、選擇與備註）
- 新鍵 cal2027-cover-r36-df0d5a，預設未選，不刪歷史回饋；R35 收進歷史

七、檢查
- build_cal_m5_cover_r36.py --check PASS；R32、R35 工具 --check PASS
- builder --check PASS（含 R36 4 檔，問題 0；公開檔無私有 ID）
- CAL_18–22、CAL_23 --check PASS
- 本機與線上 Playwright（桌機 1280、手機 390）：線上封面＋排版頁 78 項、定案相簿 18 項全過
  - 比較圖、放大、三份 PDF
  - 加強版 PDF 年份為向量漸層
  - 選擇與備註保存、複製
  - 舊回饋鍵不動
- 線上逐檔 sha256 相同、圖片無中繼資料：cover36 4、cover35 6、cover34 5、cover33 4、cover32 12、cover31 10、cover30 14、cover29 10、cover28 9、cover 16、layout 158

八、待確認／風險
- 待 Penny：接受加強版／維持 R35／還要修改
- 亮藍受光面與外光在印刷上的效果需打樣確認（本輪未打樣、未改色彩模式，不是交印核准）
- 阻塞：無
```
