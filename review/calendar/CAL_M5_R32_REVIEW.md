TASK-CAL-001／M-5／R32｜四季光影淺深雙款、兌心科技品牌整合與 Railway 更新｜執行紀錄

# M-5 R32 執行紀錄

- 起點 HEAD：`895ba18`
- 成果 commit（部署用）：`386f9af42ee9a876d066b09b8688c88e22a9f2b7`
- 本輪：生成 0、付費 0、上傳 0、購買素材 0、訓練 0
- Owner 決定與 R32 指令逐字：`docs/calendar/data/cal_m5_owner_r32.json`；執行者設計分析（分開保存）：`docs/calendar/data/cal_m5_r32_design.json`
- 封面工具：`docs/calendar/tools/build_cal_m5_cover_r32.py`（`--check` 可完整重建比對）；Chromium 轉圖沿用 `docs/calendar/tools/render_cal_svg.cjs`
- 可編輯來源：`docs/calendar/cover_r32/`（4 個 SVG、`brand/` 官網 Logo 原檔＋來源說明、`fonts/` 字型＋SIL OFL 授權書、README）
- 候選紀錄：`docs/calendar/data/cal_m5_cover_r32.json`；頁面文字：`docs/calendar/data/cal_cover_r32_page.json`；部署：`review/calendar/m5_r32/deploy.json`

## 主管報告

```
TASK-CAL-001／M-5／R32｜四季光影淺深雙款、兌心科技品牌整合與 Railway 更新｜Claude 執行回報

起點 895ba18　成果 commit（部署用）：386f9af　紀錄 commit：本檔所在 commit
線上版本：386f9af（頁面 meta 與 Railway 部署一致）
本輪：生成 0、付費 0、上傳 0、購買素材 0、訓練 0；部署 1 次 SUCCESS（10:43→10:51 UTC），只更新既有 cal2027-decision
未合併 main、未聯絡廠商、未打樣、未下單、未送印；候選未標為接受
選封面：https://cal2027-decision-production.up.railway.app/layout.html#cover

一、Owner 決定（cal_m5_owner_r32.json；設計分析另存 cal_m5_r32_design.json）
- 橫式、直式都用 R31 A 四季光影；橫式淺色、直式深色
- 兩款都放兌心科技 Logo 與「兌心科技 Insight Software」；品牌小而清楚、不搶年份；主色藍
- 24 張照片與兩款內頁不改；人物封面維持停止

二、Logo 來源
- 官網向量原檔 https://www.insight-software.com/template/img/tw/logo/logo01.svg
  （Last-Modified 2025-05-12；sha256 f7c3ff90…cc05a；原檔放在 docs/calendar/cover_r32/brand/）
- 內容：藍色圖示 #2B33F2＋兩行英文字標「Insight Software」#231815；向量原樣、等比縮放，未重畫、未拉伸、未用相似字型重打
- 橫式淺色：官方原色
- 直式深色：同一組向量改填白色的設計衍生版
  官網找不到官方反白檔，所以這是待 Owner 確認的衍生版，不是官方版本（頁面上已註明）
- 官網同目錄的 logo02.svg 是另一家公司的標誌，未使用
- Penny 提供的參考圖不在本工作環境中，以官網向量為準
- 「兌心科技」用 Noto Sans TC Medium 排字：官網 Logo 沒有中文字標，不冒稱官方字標
- 英文只出現一次（Logo 字標）；DESK CALENDAR 拿掉；無標語、無網址

三、四張候選（同一格式的兩版共用同一張背景，只差年份與品牌區的位置、比例與排法）
- 橫式淺色（背景沿用 R31 A；2027 與「兌心科技」為深品牌藍 #1E2A78，四個數字同色；Logo 官方原色）
  - 版本 1（H-L1）：年份右下；品牌區在左下，底線與年份對齊（Logo 寬 30 mm）
  - 版本 2（H-L2）：品牌區疊在年份正上方、右緣對齊，兩者成一組，左側全部留白（Logo 寬 26 mm）
- 直式深色（新畫的近黑深藍底 #070B18–#0B1226，局部光影、大面積暗部；不是淺色反轉、不是 R31 B）
  - 光影：藍紫柔光（春）、藍色水紋（夏，焦點）、少量琥珀暖光（秋）、藍紫霧（冬）
  - 文字：2027 柔白偏淺藍 #E6ECFF；Logo 與「兌心科技」白色
  - 版本 1（V-D1）：靠左；年份左下，品牌區在年份下方、左緣對齊
  - 版本 2（V-D2）：置中；年份與品牌區置中，落在光帶下方
- 尺寸（成品）：Logo 寬 26–30 mm；字標大寫高 2.5–2.9 mm；「兌心科技」字高 2.9–3.3 mm；年份數字高 27–31 mm
- 綠色未用作主色

四、交付路徑（repo 內）
- 預覽圖：docs/calendar/decision_site/public/cover32/cover_{H-L1,H-L2,V-D1,V-D2}_{v,f}.jpg
  （f＝300 dpi：橫式 2410×1831、直式 1701×2410）
- 完整預覽 PDF：docs/calendar/decision_site/public/cover32/cal2027_{H-L1,H-L2,V-D1,V-D2}_preview_R32.pdf
  - 每份只放一張封面：橫式 28 面（約 10.8 MB）、直式 32 面（約 13.0 MB）
  - 內頁直接沿用 R26 已接受 PDF 的頁面，未重排、未調色；橫式照片框維持完整 16:9（192×108 mm）
  - R26 正式預覽、R31 PDF 不覆蓋
- 可編輯來源：docs/calendar/cover_r32/{H-L1,H-L2,V-D1,V-D2}.svg＋brand/＋fonts/（授權書隨附）

五、檢查
- 4 張的年份與品牌區：字形外框都在文字安全區內再留 3 mm，避開上緣 12 mm 線圈區
  （出血 2 mm、線圈區、安全區沿用既有工作假設，未經廠商確認）
- PDF 封面頁：年份、中文、細線、Logo 都是向量
  - 兩個字型都子集嵌入（pdffonts：CormorantGaramond-Light、NotoSansTC-Medium），「兌心科技」無缺字
  - 讀回與預覽圖平均差 1.10／1.15／1.41／1.47（0–255）
  - 600 dpi 讀回的品牌區：Logo 圖示鏤空與比例正確，字標與中文清楚
- 實際看圖（Claude 自查，非主管覆核、非 Owner 接受）
  - 深色版沒有條紋與霓虹感
  - 淺色版的品牌區不擋光帶
  - 四張的年份都是主角，品牌從屬但清楚
- 工具與建置
  - build_cal_m5_cover_r32.py --check PASS（12 檔與來源 SVG 逐檔相同）；R31 工具 --check 不受影響
  - builder --check PASS（含品牌版封面 12 檔，問題 0；公開檔無私有 ID）
  - CAL_18–22 --check PASS、CAL_23 --check PASS
- 本機與線上 Playwright 全過（桌機 1280、手機 390）
  - 線上：封面＋排版頁 83 項、定案相簿回歸 18 項
  - 放大到原尺寸、參考線、4 份 PDF 下載
  - 選擇與備註重新整理後保留、複製回饋、舊回饋鍵不動、手機點選／放大／複製
- 線上逐檔 sha256 相同：cover32 12、cover31 10、cover30 14、cover29 10、cover28 9、cover 16、layout 158
  - 圖片無中繼資料
  - cover-data.js、layout.js、layout.css 與 repo 相同
  - healthz ok

六、網站（只動 cal2027-decision 的 layout.html#cover）
- 主要區：橫式淺色版本 1／2、直式深色版本 1／2，可放大、可顯示參考線，每張卡片下有完整 PDF
- 每款「選版本 1／選版本 2／都想修改」＋各自備註＋整體備註
- 「複製全部封面回饋」含頁面版本、圖片版本、候選 ID、選擇與備註
- 新鍵 cal2027-cover-r32-09fbe3（綁這一版圖片），不沿用 R31 的選擇；舊回饋不刪
- R31 候選（當時的選擇只讀）與人物封面收進「先前的封面紀錄」，預設收合
- 主要區沒有 prompt 或技術長文

七、待確認／風險（本輪不處理）
- 待 Penny：橫式、直式各選版本 1／2 或寫修改
- 待 Owner：直式深色的白色 Logo（衍生版）可否使用
- 待 Owner：橫式淺色依官方原色使用，字標是官方的深色 #231815（不是藍色）；如要全藍或其他配色也屬衍生版，需另行確認
- 深色大面積暗部與淺色細膩漸層：正式印刷前需 CMYK 轉換與打樣確認（本輪未做 CMYK、未打樣，不是印刷核准）
- 線圈區、安全區、出血沿用工作假設；字型（SIL OFL）交印前可再決定
- 阻塞：無
```
