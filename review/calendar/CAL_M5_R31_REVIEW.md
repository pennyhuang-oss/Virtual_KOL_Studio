TASK-CAL-001／M-5／R31｜停止人物封面，改做非人物封面｜執行紀錄

# M-5 R31 執行紀錄

- 起點 HEAD：`f82eee4`
- 成果 commit（部署用）：`9df3d6259e616439d52a37a99b67527ccb4253cd`
- 本輪：生成 0、付費 0、上傳身分素材 0、未購買素材
- Owner 原話與 R31 指令逐字：`docs/calendar/data/cal_m5_owner_r31.json`
- 封面工具：`docs/calendar/tools/build_cal_m5_cover_r31.py`（`--check` 可完整重建比對）；Chromium 轉圖：`docs/calendar/tools/render_cal_svg.cjs`
- 可編輯來源：`docs/calendar/cover_r31/`（4 個 SVG＋SIL OFL 字型與授權書＋README）
- 候選紀錄：`docs/calendar/data/cal_m5_cover_r31.json`；Claude 自查：`docs/calendar/data/cal_m5_r31_trial.json`

## 主管報告

```
TASK-CAL-001／M-5／R31｜停止人物封面，改做非人物封面｜Claude 執行回報

成果 commit（部署用）：9df3d62　紀錄 commit：本檔所在 commit（起點 f82eee4）
本輪：生成 0、付費 0、上傳身分素材 0、未購買素材；未合併 main、未聯絡廠商、未打樣、未下單、未送印
Railway：只更新既有 cal2027-decision，部署 1 次 SUCCESS（09:04→09:12 UTC），線上版本 9df3d62
選封面：https://cal2027-decision-production.up.railway.app/layout.html#cover

一、Owner 決定（cal_m5_owner_r31.json）
- 原話「全部都不像本人啊……如果不放人物照片，用什麼方式做封面比較好？」
- 人物團體封面與 Coco 單人校正均未接受；人物封面停止；R27–R30 紀錄保留，不寫成接受
- 24 張月面照片與兩款內頁排版維持定案（未改）

二、完成數：4 張候選＋2 份完整預覽 PDF＋可編輯來源
- A｜四季光影：一道連續光帶，春柔光→夏水紋→秋暖光斑→冬霧光；「2027」與畫面共同構圖（四個數字的深色呼應四季）
- B｜極簡典藏：深墨底、暖白 Bodoni 數字、細線與留白、低對比光影；無金色、無仿燙金
- 橫直各自構圖（不是裁切）；不放人物、臉、剪影或舊照片；不自創品牌、Logo、標語；只有 2027＋小字 DESK CALENDAR
- 字型：Cormorant Garamond、Bodoni Moda、Inter（皆 SIL OFL，從 Google Fonts 開源庫取得，固定字重、只留拉丁字元；授權書隨來源）
- PDF：橫式 29 頁（11.4 MB）、直式 33 頁（13.5 MB）＝第 1 頁 A、第 2 頁 B，其後為 R26 已接受內頁；R26 正式預覽不覆蓋

三、檢查
- 文字位置：4 張的字形外框都在文字安全區內再留 3 mm、避開上緣 12 mm 線圈區（程式依字型實際外框計算）
- PDF：封面頁文字與細線為向量、字型全部子集嵌入（pdffonts）；封面頁讀回與預覽圖平均差 ≤1.2／255；R26 內頁 PDF 與紀錄 sha256 相同
- build_cal_m5_cover_r31.py --check PASS（SVG、預覽圖、PDF 逐檔相同）；builder --check PASS（含非人物封面 10 檔，問題 0、無私有 ID）；CAL_18–23 --check PASS
- 本機與線上 Playwright：封面＋排版頁 62 項、定案相簿 18 項全過（放大、參考線、PDF 下載、回饋保存、複製、手機 390）
- 線上逐檔：cover31 10、cover30 14、cover29 10、cover28 9、cover 16、layout 158 檔 sha256 相同

四、網站
- 主要區：橫式、直式各 A／B 並排、可放大與顯示參考線；每款「選 A／選 B／都想修改」＋備註＋整體備註＋複製回饋；兩份 PDF 下載
- 新鍵 cal2027-cover-r31-v1，舊回合選擇不沿用；人物封面收進「Owner 未接受，已停止」歷史區（R30／R29 回饋只讀）
- 內頁預覽的面 1 標為「R26 暫用封面（人物縮圖，未採用）」

五、待確認／風險（本輪不處理）
- 待 Penny：橫式、直式各選 A／B 或寫修改
- B 深底反白的細線、Bodoni 細筆畫與小字、A 淺色細膩漸層，正式印刷前都需打樣確認（本輪不打樣）
- 字型正式交印前可再決定是否沿用
- 阻塞：無
```
