TASK-CAL-001／M-5／R34｜直式封面 Logo 藍白比較｜執行紀錄

# M-5 R34 執行紀錄

- 起點 HEAD：`71a7296`
- 成果 commit（部署用）：`77a8632b4d59fe53e9631bee417dac56c6b40cb5`
- 本輪：生成 0、付費 0、上傳 0、購買素材 0；部署 1 次
- Owner 授權原話與 R34 指令逐字：`docs/calendar/data/cal_m5_owner_r34.json`；比較紀錄與辨識度量測：`docs/calendar/data/cal_m5_r34_design.json`
- 工具：`docs/calendar/tools/build_cal_m5_cover_r34.py`（`--check` 可完整重建比對，並確認 A／B 只有圖示範圍不同）
- 比較版與 PDF 紀錄：`docs/calendar/data/cal_m5_cover_r34.json`；部署：`review/calendar/m5_r34/deploy.json`

## 主管報告

```
TASK-CAL-001／M-5／R34｜直式封面 Logo 藍白比較｜Claude 執行回報

版本
- 起點 71a7296；成果 commit（部署用）77a8632；紀錄 commit＝本檔所在 commit
- 線上版本 77a8632（頁面 meta 與 Railway 一致）
- 本輪：生成 0、付費 0、上傳 0、購買素材 0；部署 1 次 SUCCESS（08:49→08:59 UTC），只更新 cal2027-decision
- 未合併 main、未聯絡廠商、未打樣、未下單、未送印
網址：https://cal2027-decision-production.up.railway.app/layout.html#cover

一、Owner 授權
- 原話「那試做看看，我再進行比較」
- 只試做比較，不代表接受直式封面

二、唯一修改（B）
- 以 R33 直式的向量來源為基底，只把 Insight Software 左側圖示由白色填回官網 logo01.svg 原色 #2B33F2
  - 色值已從原檔 .st0 樣式核對；原檔 sha256 與 R32 紀錄相同
- 英文字標、「兌心科技」、細線維持白色；金色 2027、背景、排版、尺寸、間距不變
- 無圓底、光暈、描邊、陰影；沒有重新生成圖片

三、確認只改了圖示
- A／B 用同一流程各算一次 300 dpi 圖逐像素比較：不同的像素 2,487 個，全部在圖示外框內（49.44–57.65 × 186.22–191.12 mm，外加 2 px 反鋸齒）；圖示外 0 個
- A 這次重算的預覽與 R33 已交付檔案位元組相同（比較基準就是 R33）
- B 的 PDF 封面頁：背景點陣與 R33 PDF 是同一張；頁面內容只差 1 行（圖示填色）

四、藍色圖示辨識度（照實記錄，未補救）
- 圖示成品約 8.2×4.9 mm；渲染色 #2B33F2；周圍底色約 #0D111E
- 亮度對比：藍色圖示約 2.6:1；白色圖示（A）與白色字標約 18.8:1
- 600 dpi 放大：藍色圖示形狀完整清楚，看得出是品牌藍
- 接近成品尺寸：藍色圖示比白色字標暗很多，在深藍底上偏隱沒，一眼先看到白色 Insight Software；圖示仍可辨認但不搶眼
- 螢幕比較不等於印刷效果

五、交付位置
- 藍色版可編輯來源：docs/calendar/cover_r34/V-D2-R34B.svg（＋fonts）
- 預覽：docs/calendar/decision_site/public/cover34/
  - cover_V-D2-R34B_{v,f}.jpg（f＝300 dpi）
  - 品牌區放大 brand_A_600dpi.jpg、brand_B_600dpi.jpg
- 藍色版直式完整預覽 PDF：cover34/cal2027_V_preview_V-D2-R34B.pdf（32 面，內頁與 R26 逐頁相同，字型子集嵌入）
- 白色版（A）保留可查看：cover33/cover_V-D2-R33_*.jpg、cal2027_V_preview_R33.pdf（未動）
- 橫式 H-L1 已接受，不修改（PDF 沿用 cover33/cal2027_H_preview_R33.pdf）

六、網站（只動 layout.html#cover）
- 橫式 H-L1「已接受」
- 直式 A 白色圖示／B 藍色圖示並排：全圖可放大＋品牌區放大＋各自 PDF
- 「選白色圖示／選藍色圖示／都想修改」＋備註＋複製封面回饋
- 新鍵 cal2027-cover-r34-a49c84，預設未選，不繼承舊選擇，不刪歷史回饋
- R33、R32、R31 與人物封面收進「先前的封面紀錄」

七、檢查
- build_cal_m5_cover_r34.py --check PASS；R33 工具 --check 仍 PASS（只加了預設不變的圖示色參數）
- builder --check PASS（含 R34 比較 5 檔，問題 0；公開檔無私有 ID）
- CAL_18–22、CAL_23 --check PASS
- 本機與線上 Playwright（桌機 1280、手機 390）：線上封面＋排版頁 77 項、定案相簿 18 項全過
  - 比較圖、全圖與品牌區放大
  - 三份 PDF 下載
  - 選擇與備註重新整理後保留
  - 複製內容含頁面版本、圖片版本、候選識別
  - 舊回饋鍵不動
- 線上逐檔 sha256 相同、圖片無中繼資料：cover34 5、cover33 4、cover32 12、cover31 10、cover30 14、cover29 10、cover28 9、cover 16、layout 158

八、待確認
- 待 Penny：選白色圖示／選藍色圖示／都想修改
- 品牌藍在深色底上的印刷表現需打樣確認（本輪未打樣）
- 阻塞：無
```
