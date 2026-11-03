TASK-CAL-001／M-5／R33｜橫式封面定案、直式品牌與金色年份修正｜執行紀錄

# M-5 R33 執行紀錄

- 起點 HEAD：`bfbe215`
- 成果 commit（部署用）：`32302806a0f847bb27cbb7c19f73089da88fd9cf`（之前的 `ac55e5c` 是藍色圓底 Logo 版，Owner 看過後改方向，已被取代）
- 本輪：生成 0、付費 0、上傳 0、購買素材 0、訓練 0
- Owner 頁面回饋、R33 指令與本輪 Owner 訊息逐字：`docs/calendar/data/cal_m5_owner_r33.json`；執行者設計分析（分開保存）：`docs/calendar/data/cal_m5_r33_design.json`
- 封面工具：`docs/calendar/tools/build_cal_m5_cover_r33.py`（`--check` 可完整重建比對）
- 可編輯來源：`docs/calendar/cover_r33/`（`V-D2-R33.svg`、字型與授權、`brand/` Penny 提供的圓形 Logo 原檔與紀錄）
- 修正版與 PDF 紀錄：`docs/calendar/data/cal_m5_cover_r33.json`；部署：`review/calendar/m5_r33/deploy.json`

## 主管報告

```
TASK-CAL-001／M-5／R33｜橫式封面定案、直式品牌與金色年份修正｜Claude 執行回報

版本
- 起點 bfbe215；成果 commit（部署用）3230280；紀錄 commit＝本檔所在 commit
- 線上版本 3230280（頁面 meta 與 Railway 一致）
- 本輪：生成 0、付費 0、上傳 0、購買素材 0；部署 2 次，皆 SUCCESS，只更新 cal2027-decision
  （第 1 次 ac55e5c 是藍色圓底 Logo 版；Owner 看過後改方向，第 2 次 3230280 取代）
- 未合併 main、未聯絡廠商、未打樣、未下單、未送印
網址：https://cal2027-decision-production.up.railway.app/layout.html#cover

一、狀態
- 橫式 H-L1：Owner 已接受、定案，頁面標「已接受」，不再要求選擇
- 直式 V-D2 修正版：待 Owner 確認，不標為最終接受
- 封面接受不等於交印核准；目前沒有交印核准

二、本輪過程（Owner 訊息逐字存於 cal_m5_owner_r33.json）
- 指定的藍色圓底白字 Logo 原本在本案、官網、官方 YouTube／Facebook 頭像都找不到
- 製作中 Penny 直接提供原檔（800×800 PNG、圓外透明、藍 #2B33F2）
  - 和官方 YouTube／Facebook 頭像同一排法，圖示與字樣重疊率約 98%
  - 和官網長條 logo01.svg 比例不同，所以沒有用長條 Logo 加藍圓
- 試放直徑 22 mm（第 1 次部署）、再縮到 15 mm，Owner 意見依序是：
  - 「不要這麼大，看起來很突兀」
  - 「藍底滿醒目的，過大會很難看」
  - 「這個藍底的logo有點不搭」
- 另做三種品牌區改法示意給 Owner 選：A 金色單色 Logo、B 淺色名牌＋官方原色、C 封面只放中文
- Owner 決定：「乾脆就維持原本白色的logo字樣，2027的字體改變而已」
- 藍色圓底 Logo 原檔保留在 cover_r33/brand/ 作紀錄，未用在封面

三、直式修正版（只改年份）
- 2027：同一字型（Cormorant Garamond Light）、同位置與大小；柔和香檳金 #F7EBCB → 暖金黃 #CDA764 的上下漸層，不偏橘、不螢光、無金屬反光、描邊、浮雕或星芒
- 光暈：同色系兩層，模糊 2.0 mm／不透明度 0.42＋模糊 0.6 mm／不透明度 0.24，以濾色疊在背景光影上；字本體不模糊
- 這是印刷圖稿上的金色效果，不是燙金或金墨，不增加製程
- 以下與 R32 V-D2 完全相同：背景、置中編排、留白、白色 Logo（官網 logo01.svg 向量改填白色的衍生版，本輪由 Owner 決定使用）、細線、白色「兌心科技」

四、Logo 實際來源
- 橫式 H-L1：官網 logo01.svg 官方原色（同 R32）
- 直式：官網 logo01.svg 向量改填白色（同 R32 V-D2；衍生版，非官方反白檔；Owner 本輪決定維持）
- Penny 提供的藍色圓底 Logo：保存於 docs/calendar/cover_r33/brand/insight-software-logo-circle.png（sha256 859e51e7…）；試放後未採用

五、交付位置
- 直式預覽：docs/calendar/decision_site/public/cover33/cover_V-D2-R33_{v,f}.jpg（f＝300 dpi，1701×2410）
- 橫式預覽：沿用 cover32/cover_H-L1_{v,f}.jpg（不改）
- 完整預覽 PDF：docs/calendar/decision_site/public/cover33/
  - cal2027_H_preview_R33.pdf：28 面，封面＝已接受 H-L1，直接取自 R32 H-L1 PDF 第 1 頁
  - cal2027_V_preview_R33.pdf：32 面，封面＝修正版，PDF 標題註明待 Owner 確認
- 內頁沿用 R26 已接受頁面（逐頁內容相同）；橫式照片框維持完整 16:9、192×108 mm
- 可編輯來源：docs/calendar/cover_r33/V-D2-R33.svg＋fonts/＋brand/
- R32 圖片、PDF 與歷史回饋不覆蓋

六、必要檢查
- 看圖（Claude 自查，非 Owner 接受）
  - 原尺寸：金色字邊緣俐落，光暈輕、不糊
  - 手機卡片大小：金色年份清楚、無髒邊
  - 品牌區與年份的比例同 R32，保留深藍光影留白
- 安全區：年份與品牌區字形外框都在文字安全區內再留 3 mm、避開上緣 12 mm 線圈區（工作假設）
- PDF
  - 年份是向量字形裁切＋線性漸層，600 dpi 讀回正確
  - 中文、細線、白色 Logo 為向量；光暈在 300 dpi 背景點陣裡
  - 兩個字型子集嵌入；封面讀回與預覽平均差 1.13（直式）／1.2（橫式）
  - 頁數 28／32，內頁與 R26 逐頁相同
- 工具
  - build_cal_m5_cover_r33.py --check PASS（R32 工具 --check 不受影響）
  - builder --check PASS（含 R33 封面 4 檔，問題 0；公開檔無私有 ID）
  - CAL_18–22、CAL_23 --check PASS
- 線上 Playwright（桌機 1280、手機 390）：封面＋排版頁 72 項、定案相簿 18 項全過
  - 圖片、放大到原尺寸、參考線
  - 兩份 PDF 下載
  - 選擇與備註重新整理後保留
  - 複製內容含頁面版本、圖片版本 5faa09、候選識別 H-L1／V-D2-R33、選擇與備註
  - 舊回饋鍵不動
- 線上逐檔 sha256 相同、圖片無中繼資料：cover33 4、cover32 12、cover31 10、cover30 14、cover29 10、cover28 9、cover 16、layout 158

七、網站
- 橫式 H-L1「已接受」
- 直式修正版（可放大）＋R32 V-D2 前一版比較
- 「接受本輪修正版／還要修改」＋備註＋複製封面回饋
- 新鍵 cal2027-cover-r33-5faa09，不繼承舊選擇，不刪歷史回饋
- R32、R31、人物封面收進「先前的封面紀錄」

八、待確認／風險
- 待 Penny：直式修正版「接受／還要修改」
- 解讀：Owner 說「2027的字體改變而已」，本輪做法是改 2027 的顏色與光暈、保留同一字型（R33 指令要求保留年份字型）。如果 Owner 是想換另一種字型，下輪再調
- 金色在 CMYK 印刷的實際色相與光暈需打樣確認（本輪未做 CMYK、未打樣）
- 線圈區、安全區沿用工作假設
- 阻塞：無
```
