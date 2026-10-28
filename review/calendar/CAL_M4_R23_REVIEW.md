TASK-CAL-001／M-4／R23｜最後兩項修正、Rainie 身分查核與 Railway 更新｜執行紀錄

# M-4 R23 執行紀錄

- 起點 HEAD：`04b1a87`
- 原圖、調色衍生檔與查核／生成紀錄 commit：`dab82fe6d3586fef6e13fc621a4d52618f356c30`
- 選片頁成果 commit（部署用）：`a6061126901037db5d1a1be5ad1d499c0e9158d2`
- 本輪：V-Rainie 送出 2 次請求、產出 2 張、實扣 0.24（2 × 0.12，依時窗推定）；重試 0、補生 0、付費修圖 0；H-Somi 本機調色 1 張（不計費）

## 主管報告

```
TASK-CAL-001／M-4／R23｜最後兩項修正、Rainie 身分查核與 Railway 更新｜Claude 執行回報

起點 HEAD：04b1a87　原圖／查核 commit：dab82fe　選片頁成果 commit（部署用）：a606112　紀錄 commit：本檔所在 commit
本輪：V-Rainie 送出 2、產出 2、實扣 0.24（每張 0.12，未超過總上限 0.24）；重試 0、補生 0、訓練 0；H-Somi 本機調色 1
Railway：只更新既有 cal2027-decision，部署 1 次 SUCCESS，線上頁面版本 a606112

一、Owner 決定與紀錄
- 22 套定案＝既有 18＋本輪 4（H-Mia R22-A、H-Luna R21-A-G22、V-Miu R20-B-G22、V-Somi R22-B；H-Luna、V-Miu 定案的是修正版本身）
- H-Somi 改選 R22-2（來源選定），調色版待確認；V-Rainie R22 A／B 退回、重製
- Owner 原話逐字存 cal_m4_owner_r23.json；執行者分析另存 cal_m4_r23_rainie_check.json，不混在一起
- R21 頁面原文（537fa19）逐字補存在 cal_m4_owner_r22.json 的 page_copy，與本輪決定分開
- fbf5674 頁面原文沒有隨 R23 指令交來，標交接缺件

二、H-Somi 調色（review/calendar/m4_r23/process.py；紀錄 cal_m4_r23_grading.json）
- 從 R22-2 原圖另存：明暗曲線 gamma 0.86＋自然飽和度 0.14（膚色 0.04），高光柔肩
- 中位亮度 0.381→0.436、飽和 0.396→0.409；剪白 4.82% 不變（夕陽本身）
- 細節比 0.97、對比比 0.95：沒有變銳利；最亮區的層次保留 87%
- 人物、動作、服裝、背景不變，原圖不動

三、Rainie 查核（cal_m4_r23_rainie_check.json；任務與 Soul ID 只在私有紀錄）
- 早期正常圖（實際看原圖）：訓練集 v2 自拍（Seedream 4.5＋錨點 Element v2，不是 Soul 產出），以及 R5 舞蹈起始畫面（Soul 產出，與平台結果逐像素相同）
- 已確認：
  · R20、R21、R22 的 V-Rainie 6 張與 H-Rainie 2 張都用同一個 Soul，與 profile 目前 ready 的 v2 Soul 一致；deprecated 的 v1 Soul 沒用過
  · 抽查 R20 A、R21 A、R22 A／B 的平台任務紀錄：身分參考「Rainie Hsu v2」，網址等於該 Soul 縮圖；沒有輸入圖或 Element；prompt 改寫關閉；style 為平台預設
  · 早期 Soul 產出（R5、R10 起始畫面）的任務紀錄設定相同
  · 沒有套用錯的參考圖；訓練圖與錨點只供人工比對，從未送入本批
  · v1 與 v2 錨點是兩張不同的臉，目前 Rainie 對應 v2
  · 量測：早期正常圖眼睛寬 64–90 px、臉高佔畫面 16–21%；R20–R22 月曆六張只有 32–46 px、臉高 12–14%
  · 目視：早期正面看鏡頭的圖正常；R14 起始畫面（側臉）與月曆 R20 A 可見一眼瞳孔偏向鼻側
- 未確認：
  · 平台紀錄不顯示 Soul ID 欄位，Soul 對應是由清冊＋縮圖網址兩點確認
  · H-Rainie 兩張臉太小，量測抓不到
  · 平台是否在 8–10 月間更新過 Soul V2 模型，無從得知
- 推測（未證實）：
  · 全身直式構圖讓臉太小、眼睛細節不足，加上頭轉向一側又指定看別處時，較容易出錯
  · 場景、服裝或某個 prompt 詞都沒有被證實是成因
- 結論：身分來源可確認、沒有用錯 Soul 或參考圖，不列阻塞，未新建或重訓 Soul

四、V-Rainie 新候選 2 張（cal_m4_r23_prompts.json，含 sha256；規格 review/calendar/m4_r23/specs.py）
- 設定：正確的既有 Soul（ready）、soul_2、2k、3:4；無參考圖、無 style、無 unlim；唯讀報價 0.12
- 意圖與任務 ID 先存，各 1 次請求，無重送
- 場景：捨棄雨夜街道，換成 5 月晴天午後的林蔭巷弄＋白牆咖啡館；樹蔭下柔和天光；白色細肩帶方領短洋裝、金飾、高跟鞋
- 只寫一個凝視指令：臉與視線都朝向鏡頭
- A：腰上中近景，拿冰拿鐵；B：全身朝鏡頭走，人物占滿畫高；85mm、平視、合理距離
- 扣款：本批時段 Soul V2 支出 2 列各 −0.12，無退款；餘額 1182.43→1182.19
  · 查詢前帳號已有非本案的 Seedance 2.0 支出，不檢視、不歸入

五、Claude 自查（不是主管覆核，也不是 Penny 決定；與早期正常圖原尺寸並排）
- A：眼睛寬約 63 px（與早期正常圖同級），雙眼瞳孔都在中央、方向一致，看不出內聚
  · 實際景別到大腿（設計是腰上），相機略高；眼線仍上揚（這個 Soul 一貫如此）
- B：全身，腿長比例自然，無仰拍拉伸
  · 眼睛約 36 px，原尺寸看方向一致，但細節比 A 少
  · 鞋子成了繫踝涼跟鞋
- 只有 2 張，不能據此證實成因

六、選片頁 https://cal2027-decision-production.up.railway.app/shoot.html
- 本輪待確認只有 2 項：
  · H-Somi：原版／調色版（用調色版／維持原版／還想修改＋備註）
  · V-Rainie：A／B／兩張都想修改＋備註
- 兩項附前幾輪照片：H-Somi 5 張、V-Rainie 6 張，只看不選
- 已選 23 套：22 套定案＋H-Somi 調色待確認
- 新回饋鍵 cal2027-pick-r23-v1，舊鍵不動；新圖不繼承舊接受狀態
- 頁面不放查核長文或 prompt
- 線上驗收：Playwright 桌機／手機 31 項全過（載圖、版本、保存、複製、手機操作）；線上 74 圖檔無中繼資料與 ID

七、計數與檢查
- 進度：24＝已接受 22＋調色待確認 1＋待選 1＋退回 0＋未生成 0
- 月面照片累計 83 張／9.96 credits；構圖底稿 2 張／4 credits；合計 13.96
- CAL_18–22 --check PASS、CAL_23 --check PASS（CAL_19 不變）
- builder --check PASS（745 檔、選片頁 74、問題 0）
- 本機與線上 Playwright 全過
- 未合併 main、未聯絡廠商、未動定案照片

八、阻塞：無
- 待 Penny：H-Somi 調色版、V-Rainie A／B
- 若要保存 fbf5674 頁面原文，請 Penny 補貼
```
