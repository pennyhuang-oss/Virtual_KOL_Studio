TASK-CAL-001／M-5／R37｜雙款封面定案與印前檢查｜執行紀錄

# M-5 R37 執行紀錄

- 起點 HEAD：`6e8940c`
- 成果 commit（部署用）：`a12b59664ec2aed2f62a9a7b309792807c646c69`
- 本輪：生成 0、付費 0、上傳 0、購買素材 0；改設計 0；部署 1 次
- Owner R36 頁面回饋全文與 R37 指令逐字：`docs/calendar/data/cal_m5_owner_r37.json`
- 工具：`docs/calendar/tools/build_cal_m5_final_r37.py`（`--check` 會完整重建，並逐頁比對來源 PDF 與印前檢查結果）
- 定案預覽與印前檢查紀錄：`docs/calendar/data/cal_m5_final_r37.json`；文件：`docs/calendar/CAL_29_M5_R37_FINAL_PREFLIGHT.generated.md`
- 部署：`review/calendar/m5_r37/deploy.json`

## 主管報告

```
TASK-CAL-001／M-5／R37｜雙款封面定案與印前檢查｜Claude 執行回報

版本
- 起點 6e8940c；成果 commit（部署用）a12b596；紀錄 commit＝本檔所在 commit
- 線上版本 a12b596（頁面 meta 與 Railway 一致）
- 本輪：生成 0、付費 0、上傳 0、購買素材 0；不改設計、不重生
- 部署 1 次 SUCCESS（08:02→08:09 UTC），只更新 cal2027-decision
- 未合併 main、未聯絡廠商、未打樣、未下單、未送印；交印未核准

連結
- 定案頁：https://cal2027-decision-production.up.railway.app/layout.html#cover
- 橫式定案預覽 PDF：https://cal2027-decision-production.up.railway.app/cover37/cal2027_H_final_preview.pdf
- 直式定案預覽 PDF：https://cal2027-decision-production.up.railway.app/cover37/cal2027_V_final_preview.pdf

一、Owner 回饋保存與定案
- R36 頁面回饋全文已逐字保存（頁面版本 f1b2947…；圖片版本 df0d5a）
- 直式：V-D2-R34B 已接受
- 橫式：接受加強版 H-L1-R36L，備註無
- 只鎖定這兩版；候選與歷史回饋都保留
- 沒有要求 Penny 重貼或重選
- 內頁與 24 張照片不變
- 回饋原文註明「只代表封面確認，不等於交印核准」

二、定案預覽 PDF（名稱是「定案預覽」，不是交印檔）
- 做法：從已驗證的預覽 PDF 逐頁原樣複製，只改文件標題與主旨
- 頁面內容、圖片、字型、尺寸框逐頁比對，與來源相同
- 橫式 cal2027_H_final_preview.pdf
  - 28 面，封面 H-L1-R36L
  - 來源 cover36/cal2027_H_preview_R36.pdf（commit f1b2947）
  - sha256 23b32c22c106119b4439a0da55d523bb8b275dbfe4e44bdad002a6115ba146d1
- 直式 cal2027_V_final_preview.pdf
  - 32 面，封面 V-D2-R34B
  - 來源 cover35/cal2027_V_preview_R35.pdf（commit 6add915；封面頁即 R34 V-D2-R34B 已接受版）
  - sha256 21f1b4faf1ed049d2820c09fb47baa399749106730ea71e2ff180e0b685271d6

三、檔案檢查（已通過）
- 頁數：橫式 28／直式 32，符合預期
- 成品尺寸：橫式 200×151 mm、直式 140×200 mm
- 出血四邊各 2 mm；每頁 MediaBox／TrimBox／BleedBox 一致；旋轉全部 0°
- 封面頁是已接受版本；內頁與 R26 已接受排版逐頁相同
- 頁序
  - 橫式：封面 → 12 個月（照片面 → 大格面）→ MEMO → 條碼
  - 直式：再加全年年曆
- 字型全部子集嵌入
- 照片框：橫式 192×108 mm（完整 16:9）、直式 120×160 mm
- 照片有效解析度（照實記錄，未放大）：橫式約 271 ppi、直式約 325–366 ppi
- 封面畫面 300 ppi；文字與 Logo 為向量
- 圖片為 RGB JPEG、無透明遮罩
- 封面年份與品牌區都在已知安全區內
- PDF 1.4、無輸出意圖
- 安全區與線圈區是本案工作假設，不是廠商書面規格

四、廠商待確認（檔案檢查無法替代）
- 線圈／打孔位置與裝訂區（目前以上緣 12 mm 假設）
- 正背面對應、背面是否旋轉（目前單面正向逐面排列）
- 解析度門檻
  - 編輯器只有好／標準／差，沒有數字
  - 300 ppi 是本案目標，不是廠商門檻
- RGB→CMYK 由誰轉、用哪個 ICC（目前 RGB、無 ICC）
- 交件格式
  - 逐面上傳或整份 PDF、是否要 PDF/X 或裁切標記、單檔上限
- 透明：品牌區細線用 55% 不透明度，是否需要先平面化

五、打樣重點（沒有實際打樣，不判定印刷效果通過）
- 橫式
  - 淺色漸層：是否斷層或偏色
  - 藍色年份光感：字內亮藍到深藍的漸層、淡藍外光是否保留
- 直式
  - 深色暗部：是否塌黑
  - 金色年份：印刷金是 CMYK 色，不是燙金
  - 約 8.2×4.9 mm 的小藍色圖示：在深底上的辨識度

六、網站（只動 layout.html#cover）
- 「封面定案」區直接顯示兩款，各標「已接受（定案）」
- 兩款都可放大到原尺寸、可開參考線、可下載完整定案預覽 PDF
- 「交印前還要確認」可展開（6 項）
- 已移除本輪選擇介面：沒有選項、備註、複製，也不寫新的回饋鍵
- R36 光感比較、R35～R31、人物封面收進「先前的封面紀錄」
  - 當時回饋只讀保留
  - R36 顯示「接受加強版（H-L1-R36L）」

七、檢查
- build_cal_m5_final_r37.py --check PASS
- build_cal_m5_cover_r32～r36 --check 全部 PASS
- builder --check PASS（含 R37 定案預覽 2 檔，問題 0；公開檔無私有 ID）
- CAL_18、CAL_23 --check PASS
- Playwright 本機與線上（桌機 1280、手機 390）全過
  - 線上封面＋排版頁 75 項、定案相簿 18 項
  - 兩款放大
  - 兩份 PDF 下載與 sha256
  - 交印前清單
  - 歷史只讀
  - 舊回饋鍵不動
  - 無「可直接交印」
  - 手機無橫向捲動
- 線上逐檔 sha256 相同、圖片無中繼資料：cover37 2、cover36 4、cover35 6、cover34 5、cover33 4、cover32 12、cover31 10、cover30 14、cover29 10、cover28 9、cover 16、layout 158

八、待確認／風險
- 交印前需要
  - 廠商規格（四、五）
  - 實際打樣
  - Penny 另行核准交印
- 阻塞：無
```
