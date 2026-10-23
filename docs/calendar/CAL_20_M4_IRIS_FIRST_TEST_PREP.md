TASK-CAL-001／M-4／R4｜V-Iris 首試準備、首試前核查、單張首試與定案（Penny 接受）

# CAL_20 — V-Iris 首試準備、首試前核查與單張首試（M-4）

> 資料檔：`data/cal_m3_shoot_plan.json`（shoot-plan-v12，M-4 R6）的 `m4_prep` 與 `V-iris-chen`。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。
> **M-4 R2：依 Penny 授權生成 V-Iris 首試 1 張（只送一次），結果待主管覆核；照片不放公開頁。準備文件、首張驗收條件與 M-4 R1 的核查仍適用；這不是印刷驗收。**
> R7：生成 0、credits 0、Higgsfield 呼叫 0、報價預檢 0。
> M-4 R2：生成請求 1、圖片 1、重送 0、實扣 0.12 credits（依時窗及唯一任務推定）、訓練 0、上傳 0。
> M-4 R1：生成 0、credits 0、生成任務 0、訓練 0、上傳 0；唯讀查詢 7 次：模型參數 1、Soul 狀態 1、交易明細 3、帳號餘額 1、不扣款的報價預檢 1；前後交易明細相同，沒有新增扣款。

## R4. M-4 R4 Penny 接受 V-Iris 首試（2026-10-21）

**狀態：** Penny 接受，照片直接採用。取代主管 M-4 R3「反光板及支架必修」的判定；反光板保留。不修圖、不重生、不再詢問是否接受。

**Penny 的回饋（主管（ChatGPT）轉述 Penny 的回饋；不是 Penny 在網頁回饋欄位填寫的內容（網頁回饋只存在她的瀏覽器，執行者看不到）。）：**

```text
Penny已接受V-Iris首試：
臉、身材、表情、服裝與光線均接受；反光板也接受保留，照片直接採用。
```

**接受項目：** 臉、身材、表情、服裝、光線、反光板（保留）。逐字紀錄：`docs/calendar/data/cal_m4_owner_r4.json`。

## A. M-4 R2 V-Iris 單張首試（2026-10-20）

**R2 當時狀態：** 已生成 1 張，待主管覆核；照片只在私有 repo 送審，不放公開頁。

**判定：** 部分通過：身分、服裝、姿態與手指、表情、構圖、套框與有效 ppi 都符合；一項不符合——左側草地上出現白色反光板（prompt 寫在畫面外）；兩項待判斷——胸型目視比人設保守、臉部皮膚偏光滑；遠處有失焦人形的小落差。依指示不重送、不再生成，交主管覆核；反光板與身材屬設定落差，由 Penny 判斷。

**授權：** 依 Penny 同意的條件執行：1 張、預算最多 1 credit、精確報價 ≤0.12、只送一次。沒有重送、沒有其他生成。

### A.1 送出前核對

| 項目 | 結果 |
|---|---|
| Soul | Iris Chen｜soul_2｜ready；與專案紀錄對應（ID 不公開） |
| 參數 | 與 M-4 R1 相同（quality 1.5k／2k、比例含 3:4、沒有 seed 與 negative prompt；免費額度不可用） |
| 送出前精確報價 | credits 1／credits_exact 0.12（≤0.12，可送出） |
| 重複提交 | 送出前沒有本輪的提交紀錄 |
| 存放 | 帳號偏好 auto_create_project false：不指定資料夾、不建立專案 |
| 交易邊界 | 送出前最新一列 2026-10-20 09:31:49（UTC，非 Soul V2）；前 30 列沒有 Soul V2 |
| 時窗任務基準 | 送出前帳號最近 20 個圖片任務沒有 soul_2 |

### A.2 實際設定與任務

**送出：** generate_image｜soul_2｜Iris 既有 Soul｜quality 2k｜aspect_ratio 3:4｜count 1｜use_unlim false｜不用參考圖與 style_id｜V-iris-chen 已接受 prompt 原文（一字不改）｜只送一次

**任務：** completed（輪詢 2 次）；輸出 1536×2048。任務中繼資料：寬高 1536×2048；quality 欄位記為 1080p（後台標籤；請求是 2k）；套用後台預設風格 General（沒有傳 style_id）。

**原圖：** `kols/iris-chen/images/calendar_2027_m4_r2/V-iris-chen_m4r2_first_test.png`（私有 repo；不放公開頁）。套框預覽、裁切檢視與執行紀錄：`review/calendar/m4_r2/`。

### A.3 逐項驗收

| 類別 | 條件 | 結果 | 說明 |
|---|---|---|---|
| 身分與身材 | 臉與 Iris 人設一致 | 符合 | 圓臉甜美、雙眼皮大眼、飽滿嘴唇、小下巴；與訓練圖和既有成圖是同一人的觀感（目視）。 |
| 身分與身材 | 膚色白皙自然、沒有被夕陽拍偏 | 符合 | 白皙略暖，沒有過飽和。 |
| 身分與身材 | 黑色柔順直髮過肩；成人樣貌 | 符合 | 中分黑色長直髮過肩。 |
| 身分與身材 | 身材比例符合人設 | 部分符合（待 Penny 判斷） | 腰細、整體比例自然；貼身上衣下的胸型目視比人設的「飽滿 D」保守。只以人設與既有合格參考判斷外觀比例，不從照片量測三圍或罩杯。 |
| 服裝 | 白色貼身羅紋方領短袖短上衣，露腰，不走光 | 符合 | 方領、短袖、細羅紋可見、露腰。 |
| 服裝 | 淺藍高腰牛仔迷你裙，整條入鏡 | 符合 | 高腰、整條入鏡；水洗色偏中淺藍。 |
| 服裝 | 小金色圈耳環；鞋不入鏡 | 符合 | 看得到的一側有小金圈；鞋不在畫面內。 |
| 服裝 | 衣服沒有亂碼文字、品牌或多餘配件 | 符合 | 牛仔褲扣有壓紋，沒有可讀文字。 |
| 姿態與手指 | 正面站立、重心在一腳、臀部微偏；沒有回頭或轉身 | 符合 | 身體正對鏡頭；重心偏移幅度小。 |
| 姿態與手指 | 一手插腰、一手輕碰太陽穴旁的頭髮；手指沒有融合或多指 | 符合 | 碰髮的手：拇指與食指捏住髮束，其他手指自然，沒有融合；插腰的手：手指大多被身體與裙子遮住，看得到的部分沒有異常（原生解析度與 2 倍零插值檢視）。 |
| 姿態與手指 | 沒有多餘肢體；四角與背景掃過 | 符合 | 四角只有天空與草地。 |
| 表情與視線 | 明亮溫暖的笑，只有一個表情 | 符合 |  |
| 表情與視線 | 看鏡頭；眼睛對焦清楚 | 符合 |  |
| 場景 | 台北河濱公園草地、傍晚低太陽、遠處樹林與低矮公寓 | 符合 | 另有河道與步道。 |
| 場景 | 沒有可辨識臉的路人 | 符合（有小落差） | 遠處右側河岸有 1–2 個失焦、無法辨識的人形或物件；近處草地與步道沒有人。與企劃「空無一人」有小落差，記錄。 |
| 場景 | 沒有招牌或亂碼文字；背景不像拼貼 | 符合 |  |
| 場景 | 沒有不該出現的物件 | 不符合 | 畫面左側草地上出現一個白色圓形反光板（含支架）。prompt 寫的是「just out of frame」，這是 SEXY_SCENE_LIBRARY.md §3-F「點名物件就會出現」的已知機制；位置在 120×160 mm 工作照片框內（3:4 不裁切），屬設定落差，依 §10-a 交 Penny 判斷，不自行重生。 |
| 場景 | 光向一致、臉不暗 | 符合 | 夕陽在她身後右上方，形成髮絲與肩線輪廓光；臉部由前方補光照亮、不暗。 |
| 構圖 | 直式 3:4；大腿中段以上，下緣明顯高於膝蓋 | 符合 |  |
| 構圖 | 人物置中、頭頂上方少量留白 | 符合 | 髮頂約在第 212 列（共 2048），頭頂留白約 10.4%（規劃約 8%）。 |
| 構圖 | 雙手在畫面內；自然透視、水平 | 符合 | 建築垂直線不歪，沒有廣角變形。 |
| 質感 | 自然皮膚紋理、看得到毛孔 | 部分符合 | 手臂與腹部有紋理；臉部偏光滑，毛孔不明顯。 |
| 質感 | 專業寫真質感，不是手機自拍感 | 符合 |  |
| 生成後套框與有效 ppi | 實際輸出像素 | 符合 | 1536×2048（與預期相同） |
| 生成後套框與有效 ppi | 套進 120×160 mm 工作照片框 | 符合 | 3:4 放入 3:4，不裁切（套框預覽見送審紀錄） |
| 生成後套框與有效 ppi | 髮頂上方 ≥4%，臉與雙手在框內 | 符合 | 頭頂留白約 10.4%；臉與雙手都在框內 |
| 生成後套框與有效 ppi | 有效 ppi | 符合工作目標 | 寬 1536 px ÷（120 mm ÷ 25.4）≈ 325 ppi；高 2048 px ÷（160 mm ÷ 25.4）≈ 325 ppi。300 ppi 是本案工作目標，不是廠商門檻；沒有放大補像素；不是印刷驗收。 |

### A.4 交易與歸屬

| 項目 | 內容 |
|---|---|
| 扣款 | 2026-10-20T09:44:29.926120Z -0.12 |
| 退款 | 無 |
| 淨額 | -0.12（精確報價 0.12；核准預算 1 credit；查到 2026-10-20T09:59:50Z） |
| 異常 | 沒有異常（扣款等於精確報價，沒有退款或其他 Soul V2 列） |
| 歸屬層級 | **依時窗及唯一任務推定**；不是直接對帳確認：交易明細沒有工作 ID。 |

**依據：**

- 送出前邊界之後到終態後 15 分鐘，交易明細只新增一列 Soul V2（−0.12 扣款，時間與任務完成時間同一秒），沒有退款或其他 Soul V2 列。
- 同一時窗帳號的圖片任務裡，soul_2 只有本次這一個；其他模型的任務（3 個 nano_banana_2）與其扣款（3 列 Nano Banana Pro）不是 Soul V2，不影響歸屬。
- 金額與送出前精確報價 0.12 相同。
- 沒有用帳號餘額差額推算。

### A.5 停止

依指示在這一次請求後停止：沒有重送、沒有其他生成；交主管覆核（M-4 R4 由 Penny 接受，見上方 R4）。

## 0. M-4 R1 首試前核查（2026-10-20，不生成）

**結論：** Soul 身分對應已確認；當前模型參數、Soul 狀態與報價已用唯讀查詢取得；單次首試的設定、計價、失敗扣款規則、建議上限與交易核對方法已整理。剩餘阻礙：生成與費用授權、交易關聯判準的接受、Soul 沒有正式 6 張驗證的接受。

**主管覆核：** PASS（主管 M-4 R2 覆核）：接受以既有生產紀錄＋單張首試驗收；交易歸屬只標「依時窗及唯一任務推定」；精確報價與實扣分列；1 credit 是本次核准預算，不是平台保證。

### 0.1 Soul 證據

| 項目 | 內容 | 來源檔 |
|---|---|---|
| 身分對應 | 專案內 12 處紀錄指向同一個 Soul（程式比對，ID 不公開）；2026-10-20 唯讀查詢回傳名稱 Iris Chen、類型 soul_2、狀態 ready（completed）。 | `kols/iris-chen/profile.json（ai_assets.training_images_v1.soul_training）`、`kols/iris-chen/generation_notes.md 第 244–1188 行（11 處）`、`review/LEDGER.md 第 94、128–134 行（U-01）` |
| 訓練來源 | 2026-06-25 用 14 張 Seedream 4.5 訓練圖（1920×2560）訓練。不在 2026-09 的 19 位 Soul 總表內，那批另有 6 張驗證協定。 | `kols/iris-chen/profile.json（ai_assets.training_images_v1）`、`review/soul_training/SOUL_IDS.json`、`review/soul_training/FINAL_REPORT.md` |
| 驗證證據 | 沒有 6 張驗證紀錄。以 Iris 為 GOOD 基準的 Retroactive Benchmark 有設計，但沒有執行紀錄。依指示不重訓、不補生 6 張。 | `review/LEDGER.md（U-01、C-08）`、`review/REVIEW.md 第 398 行` |
| 既有成圖 | 本機 Iris 的 soul_2 輸出 73 張：3:4 1536×2048 59 張、9:16 1152×2048 14 張（其中 3:4 的 drive_v1 15 張沒有生成紀錄）。生成筆記明寫 soul_2＋此 Soul、2k、3:4 輸出 1536×2048；6 批有逐張生成後檢查紀錄（手部、規格落差、瑕疵重生）。 | `kols/iris-chen/generation_notes.md 第 969–1014、1042–1101、1176–1248、1261–1453 行` |
| 生產中已知的行為 | 身材還原不穩：部分成圖胸型小於 87 cm／D（第 1007–1010 行）；嘴型多鎖在微笑／笑（第 1436–1446 行），V-Iris 要的是明亮的笑，相容；上身前傾＋靠近鏡頭的姿勢曾觸發拼貼（第 617–628 行），V-Iris 是正面站定，不屬此類。使用者曾裁決 Iris 為 GOOD 基準：「訓練後在生產環境跨場景跨造型使用最久」。 | `kols/iris-chen/generation_notes.md`、`review/LEDGER.md 第 132 行` |
| 目視（縮小檢視，不是量測） | 3 張訓練圖與 6 張不同日期的 Soul 輸出並排：臉型、雙眼皮大眼、唇形與黑色長直髮一致；身材在部分輸出偏纖細。接觸表只存在本機暫存，沒有放進 repo。 |  |
| 結論 | 身分對應確認；沒有正式驗證，但既有生產紀錄支持用「單張首試＋首張驗收」判定。不重訓、不補生 6 張；身材與逆光臉部列入首張驗收。 |  |

### 0.2 當前模型參數與 Soul 狀態（2026-10-20 唯讀查詢）

| 項目 | 內容 |
|---|---|
| 模型 | soul_2（Higgsfield Soul 2.0；說明：Realistic UGC, fashion editorial and character generation） |
| 參數 | quality（1.5k／2k，預設 2k）、Soul ID（選填）、style_id（選填，Soul 風格預設；首試不用）、參考圖最多 1 張（首試不用） |
| 比例 | 1:1、16:9、9:16、4:3、3:4、3:2、2:3 |
| 沒有的參數 | 沒有 seed、沒有 negative prompt、沒有費用上限參數 |
| 免費無限額度 | soul_2 支援，但這個帳號目前不可用（available false、剩餘 null） |
| Soul 狀態 | Iris Chen｜soul_2｜ready（completed） |
| 帳號 | Plus 方案；餘額只作參考（多人共用，不用來對帳） |

### 0.3 首試單次請求的確切設定

| 項目 | 設定 |
|---|---|
| 工具 | generate_image（一次一個請求；不用 generate_image_batch） |
| 模型 | soul_2 |
| Soul | Iris 既有 Soul（Iris Chen、ready；ID 依專案紀錄，不公開） |
| quality | 2k |
| aspect_ratio | 3:4 |
| count | 1 |
| use_unlim | false（用 credits 付費） |
| 參考圖／style_id | 不用 |
| prompt | V-iris-chen 已接受 prompt 原文，一字不改（2095 字元） |
| 存放位置 | 依工具規則：送出前先唯讀查 get_preferences 決定是否需要專案資料夾；不自行建立專案（需要時由主管指示） |
| 重試 | 不重試；傳輸逾時也不重送，先確認原請求結果 |

### 0.4 報價（當前）與歷史紀錄（另列）

| 報價 | 回傳 | 依據 |
|---|---|---|
| 當前報價（2026-10-20） | credits 1／credits_exact 0.12 | 不扣款的報價預檢，設定與 prompt 和首試完全相同；工具說明：「return the cost in credits for this generation without submitting any job」；預檢前後交易明細相同，沒有新增。 |
| 上一輪報價（2026-10-13） | credits 1／credits_exact 0.12 | 同設定的報價預檢（R4 紀錄） |

**歷史紀錄（不拿來估算本次）：**

| 紀錄 | 數值 | 說明 |
|---|---|---|
| Soul V2 交易明細（2026-09） | 每筆 −0.12 | Soul 訓練報告：驗證圖 114 張約 13.7 credits，交易明細為重複的 Soul V2 −0.12。 |
| 帳號交易明細（2026-10-19） | Soul V2 −0.12 後 32 秒 +0.12 退款 | 非本案、歸屬不明；說明 Soul V2 目前在交易明細仍以 0.12 記帳，且失敗可能退款。 |
| Iris 生成筆記（2026-08-05） | 「全批 14 張約 8 credits」 | 7 位角色各 2 張的約數，沒有寫怎麼算；與 0.12 不一致，只列為歷史，不拿來估算。 |

### 0.5 計價單位

- 報價以「每次請求」回傳；本案每次只送 count 1，所以一個請求就是一張。
- credits 1 是整數顯示值、credits_exact 0.12 是精確值；交易明細的 Soul V2 列以 0.12 記帳（歷史紀錄）。這些都不等於本次實扣，實扣以送出後的交易明細為準。
- 不把 0.12 推測為實扣；也不以餘額前後差額推算。

### 0.6 失敗扣款規則

- 失敗可能退款：2026-10-19 帳號交易明細有 Soul V2 −0.12 後同額退款（非本案）；其他模型也常見扣款後退款。
- 失敗也可能扣款不退：Soul 訓練協定記錄過「呼叫失敗但仍計費」的 Soul V2 −0.12（Vicky Lin 模式）。
- 傳輸逾時時結果未知：工具說明要求不要自動重送，先確認原請求結果。
- 規則：任何扣款（含失敗未退）都算進上限；失敗就停下回報，不重試。

### 0.7 建議費用上限

**單次核准上限 1 credit（1 個請求、count 1、不重試）**

1 credit 是 Penny 同意的本次核准預算（V-Iris 1 張）。工具沒有強制費用上限，不能宣稱平台保證不超扣；精確報價（0.12）與實扣分列，實扣以交易明細為準。

**停止條件：**

- 交易明細出現高於 0.12 的 Soul V2 扣款
- 同一視窗出現兩筆以上 Soul V2 扣款、無法分辨哪一筆是本次
- 出現任何無法解釋的扣款
- 請求失敗、逾時或結果不明（無論是否扣款）

任一停止條件成立：不再送出，照實回報交易明細原始列與判斷。

### 0.8 交易核對：如何把本次請求與扣款對上

1. 送出前：查交易明細，記下最新一列的時間，以及這一頁內所有 Soul V2 列。
2. 送出：只呼叫一次；記下回傳的工作 ID（只寫進送審紀錄，不放公開頁）與回傳時間；若回應含費用欄位一併記錄。
3. 等待：輪詢到終態（完成、失敗或審核拒絕）；不重送。
4. 送出後：查交易明細，直到涵蓋送出前的最新一列；終態後 15 分鐘再查一次，看有沒有遲到的扣款或退款。
5. 歸屬判準（全部符合才標「依時窗及唯一任務推定」；交易明細沒有工作 ID，所以不標成直接對帳確認）：(1) 視窗內（送出前最新一列之後，到終態後 15 分鐘）新增的 Soul V2 列恰好一筆扣款，另可有一筆同額退款；(2) 帳號生成紀錄（唯讀，含進行中）在同一視窗只有本次這一個 soul_2 任務；(3) 金額與報價一致，或差異已說明。
6. 任一不符（0 筆、2 筆以上、或視窗內有其他 soul_2 任務）：記為「無法唯一關聯」，只回報視窗內 Soul V2 列的原始資料；不以時間相近或餘額差額歸屬，停止並回報。

**限制：**

- 交易明細每列只有模型名稱、金額、動作（扣款／退款）與時間，沒有工作 ID，所以無法直接用 ID 對上；只能用「模型名稱＋時間視窗＋生成紀錄一對一」排除。
- 第 (2) 項要讀取帳號的生成紀錄（唯讀，但會看到帳號上其他人的作品），需要主管同意生成時使用。
- 2026-10-18 02:15 到 10-20 08:57（UTC）共 120 筆交易裡，Soul V2 只有 2 筆（10-19 一扣一退）；視窗內撞到他人 Soul V2 的機會低，但不能排除。

### 0.9 剩餘阻礙

| 阻礙 | 說明 | 誰決定 | M-4 R2 狀態 |
|---|---|---|---|
| 生成與費用授權 | 需要費用核准（建議上限 1 credit）與主管另發的 M-4 生成指令。 | 主管／Penny（費用） | 已解除（M-4 R2：Penny 同意 1 張、預算最多 1 credit、精確報價 ≤0.12、只送一次） |
| 交易關聯判準 | 交易明細沒有工作 ID；請主管接受「交易核對」一節的排除法判準，並同意生成時唯讀查看帳號生成紀錄。不接受時，實扣只能記為「視窗內的 Soul V2 列」，不能歸屬。 | 主管 | 已解除（主管接受；歸屬只標「依時窗及唯一任務推定」） |
| Soul 沒有正式 6 張驗證 | 依指示不重訓、不補生；請主管接受以既有生產紀錄＋首張驗收判定。 | 主管 | 已解除（主管接受以既有生產紀錄＋單張首試驗收；不補生、不重訓） |

**已不是阻礙：** V-Iris 造型（已接受）、已接受 prompt（不變）、三項檢查表差異（主管已接受）、模型參數與 Soul 狀態（已核對；生成當下再核一次）、報價（已取得 0.12）。

**首張驗收要特別看的風險：** 身材還原不穩（胸型可能小於 D）、逆光臉暗、碰頭髮的手指、戶外公園背景可能出現路人。

## 1. 已接受的 V-Iris 企劃

| 項目 | 內容 |
|---|---|
| 接受狀態 | 已接受（R4 owner 紀錄；R5 主管核可補上英文妝感句；R6、R7 維持）。Penny 不需要再選企劃。 |
| 月份與款式 | 直式款 9 月，生成比例 3:4（直式） |
| 主題 | 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。 |
| 場景 | 台北河濱公園的開闊草地，傍晚太陽低，遠處柔綠樹林與低矮公寓，草地與小徑空無一人。 |
| 服裝 | 上身：白色貼身羅紋方領短袖短上衣（露腰）；下身：淺藍高腰牛仔迷你裙；鞋：白色低筒帆布鞋（不入鏡）；配件：小金色圈耳環 |
| 姿態與手 | 站在草地上。一手插腰，一手輕碰太陽穴旁的頭髮。 |
| 表情與視線 | 明亮溫暖的笑；看鏡頭 |
| 攝影 | 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視；85mm、約 2.9 公尺；人物置中；頭頂上方少量留白，兩側是柔焦的草地與樹林，夕陽輪廓光落在頭髮與肩線 |
| 光線 | 主光：她身後側方的低角度夕陽，頭髮與肩線一圈暖色輪廓光；補光：畫面外前方的大反光板加柔光，臉與身體均勻 |
| 妝髮 | 黑色柔順直髮自然垂放過肩。乾淨的日常妝、自然唇色。 |
| 身材設定 | 162 cm／87-58-90／D；貼身方領短上衣清楚呈現 D 罩杯胸型、露出細腰；高腰牛仔迷你裙強調腰臀比與腿長。 |
| 已知風險 | 逆光臉暗（寫明反光板與柔光補臉）；膚色被夕陽拍偏（只寫一次她原本的白皙膚色）；碰頭髮的手指融合（生成後放大檢查；不行改成兩手插腰） |

## 2. 身分參考

| 項目 | 內容 | 來源檔 |
|---|---|---|
| 身分來源 | Iris 既有的 Soul（狀態見「真正生成前仍需確認」）。Soul ID 不寫進企劃、頁面或本文件；生成時從專案既有紀錄取用，並由主管指令核對。 |  |
| 人設外貌（設定，不改） | 22 歲台灣女生；圓臉甜美型、大雙眼皮深棕色眼睛、精緻鼻梁、飽滿嘴唇、小下巴；黑色柔順直髮自然放下；162 cm、87-58-90、D 罩杯，嬌小沙漏比例。 | `kols/iris-chen/profile.json（identity.appearance）` |
| prompt 開頭的身分句 | A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. |  |
| Soul V2 不繼承的部分 | 髮型、髮色與身材不從 Soul 繼承，已在身分句寫明黑色直髮過肩與身材數字（Soul V2 不繼承髮型與髮色：每張 prompt 都要寫她自己的髮色髮型（原則七 C-1）。Soul V2 不繼承身材：身材要用 prompt 句子補（數字直接寫）。） |  |
| 企劃參考照片（只用於企劃，不送進生成） | iris-04（場景）：草地、夕陽光線氛圍（Penny 喜歡的照片）；不採用回頭姿勢；iris-06（服裝材質）：白短上衣＋牛仔短裙的穿搭方向。首試不掛參考圖、不掛 Reference Element。 |  |

## 3. 最終 prompt 與生成比例

**生成比例：** 3:4 直式；R6 已接受的直式工作照片框 120×160 mm（3:4 放入 3:4 框不裁切）。

prompt（已接受版本，3:4，尚未執行；與企劃頁「prompt 草稿」逐字相同）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. Fresh, light everyday makeup with a natural lip colour. She wears a fitted white ribbed square-neck short-sleeve crop top that shows the shape of her chest and her bare waist, a high-waisted light-blue denim mini skirt and small gold hoop earrings. Setting: an open riverside lawn in a Taipei park in the late afternoon, soft green trees and low distant apartment blocks far behind her, the lawn and the path empty. One hand rests on her hip and the other lightly touches her hair at her temple; she smiles brightly and warmly. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the square-neck crop top, her bare waist, the whole denim mini skirt and her upper thighs, one hand on her hip and the other at her hair. Body: standing with her weight on one leg, her body square to the camera, shoulders level and relaxed, her hips shifted slightly to one side. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 2.9 metres, camera at her chest height, level, natural perspective without distortion. Composition: she is centred with a little space above her head and the soft lawn and trees on both sides. Emphasis: Penny's chosen outfit up close, the crop top on her chest, her bare waist and the denim mini skirt, with her bright smile. Lighting: the low sun behind her and to one side draws a warm rim along her hair and shoulders; a large white reflector and a soft fill light just out of frame in front of her light her face and body evenly; warm golden tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

## 4. 工作流（依既有專案資料；前提未滿足前不執行）

| 步驟 | 內容 | 來源檔 |
|---|---|---|
| 0. 前提 | V-Iris 造型已接受（R4 owner 紀錄；M-3 已完成），不再等待造型核准。生成與費用尚未授權：需要費用核准與主管另發的 M-4 生成指令；在那之前什麼都不送出。 | `docs/calendar/data/cal_m3_shoot_plan.json（execution.cost.iris_first.plan「前提」）` |
| 1. 核對工具當下的參數 | 生成前以工具當下的說明為準，再核一次 soul_2 的參數、比例與報價（M-4 R1 已在 2026-10-20 核對，結果見「首試前核查」）。 | `docs/calendar/data/cal_m3_shoot_plan.json（meta.aaliya_sources.model_check）` |
| 2. prompt 送出前檢查 | 用下方「送生成前檢查」逐項核對（SEXY_SCENE_LIBRARY.md §25 的 10 項＋PHOTO_DIRECTION_STANDARD.md §七）；R7 已預先核對一次，結果見表。prompt 用企劃頁的 V-iris-chen 原文，一字不改。 |  |
| 3. 送出前查交易明細 | 送出前查交易明細，記下最新一列與其中所有 Soul V2 列；不用餘額對帳（帳號同時有其他人在用）。關聯方法見「首試前核查」的交易核對。 |  |
| 4. 送出 1 個請求 | 設定照企劃：soul_2＋Iris 既有 Soul、quality 2k、aspect 3:4、count 1、不掛參考圖、use_unlim false；一次只送一個請求。 | `docs/calendar/data/cal_m3_shoot_plan.json（execution.cost.iris_first.plan「設定」）` |
| 5. 取得結果並實際看圖 | status=completed 不等於成功：每一張都要實際打開看（SEXY_SCENE_LIBRARY.md QA-2）；小區域（手指、眼睛）判讀不用插值放大（QA-1）。 |  |
| 6. 送出後查交易明細 | 查交易明細到涵蓋送出前的最新一列為止；依「首試前核查」的關聯判準記錄這一張的扣款，無法唯一關聯就照實記為無法關聯。 |  |
| 7. 不自動重試 | 無論結果好壞、成功或失敗，都先停下回報（企劃「重試」規則；優先於 SEXY_SCENE_LIBRARY.md §10-a「瑕疵可直接重生」的一般做法）。 |  |
| 8. 依驗收條件逐項判定 | 下方首張驗收條件；記錄實際像素、套框結果與有效 ppi。 |  |
| 9. 回報 | 把圖、設定、實扣與逐項驗收結果交主管覆核，再給 Penny 看；設定落差（環境、服裝、道具）不自行重生，交 Penny 判斷（SEXY_SCENE_LIBRARY.md §10-a）。 |  |

## 5. 送生成前檢查（R7 預先核對；M-4 R1 主管接受三項差異；送出當下要再核一次）

依 `SEXY_SCENE_LIBRARY.md` §25（Prompt Preflight Lint 10 項）與 `PHOTO_DIRECTION_STANDARD.md` §七（送生成前的稽核）。能機械判斷的項目由產生企劃資料的程式核對。

| 檢查 | 結果 | 說明 |
|---|---|---|
| §25-1 需要幾隻手（≤2） | 符合 | 兩隻：一手插腰、一手輕碰太陽穴旁的頭髮；沒有自拍手機。 |
| §25-2 自拍手機是否入鏡 | 不適用 | 不是自拍；prompt 沒有 phone／selfie。 |
| §25-3 中文規格的姿勢與表情是否真的在英文 prompt 裡 | 符合 | 「一手插腰，一手輕碰太陽穴旁的頭髮」「明亮溫暖的笑」都在英文句裡（程式比對）。 |
| §25-4 只描述一個靜止表情 | 符合 | 沒有 then／breaking into／just starting to。 |
| §25-5 動態衣物或髮絲 | 不適用 | 沒有寫飄動；頭髮自然垂放。 |
| §25-6 髮長有明確幾何描述 | 符合 | black silky straight hair worn down past her shoulders。 |
| §25-7 主要服裝 ≤3–4 件，最不能錯的在前 | 符合 | 入鏡 3 件：白色方領短上衣（第一）、淺藍高腰牛仔迷你裙、小金色圈耳環；白色帆布鞋不入鏡、不寫進 prompt。 |
| §25-8 visible pores 只用在看得到臉部細節的景別 | 符合 | 大腿中段以上、85mm，臉部細節可見；不是全身遠景。 |
| §25-9 機位高度、視線、頭部朝向一致 | 符合 | 相機在胸口高度平視；臉正面、看鏡頭。 |
| §25-10 一段 prompt 只對應一張 | 符合 | 只有一個景別（大腿中段以上），count 1。 |
| §七 機位寫離地公分數 | 與稽核表不同（主管 M-4 R1 接受） | prompt 寫「camera at her chest height」，沒有寫公分；企劃參考值約 1.19 公尺（胸口高度）。R7 不改已接受的 prompt。主管 M-4 R1 接受「胸口高度不補寫公分」；prompt 不變，出圖後依驗收條件判定。 |
| §七 鏡頭水平 | 符合 | level，俯仰換算約 −0.1 度。 |
| §七 焦段與距離 | 符合 | 85mm、約 2.9 公尺（不是全身照；全身 3–5 公尺的條目不適用）。 |
| §七 腳在下 1/3、上方留白 | 不適用（腳不入鏡） | 大腿中段以上；規劃髮頂留白約 8%。 |
| §七 兩隻手分別在哪 | 符合 | 插腰、碰頭髮；沒有僵直垂在身側。 |
| §七 道具互動或側身回望，不正面直視鏡頭 | 與稽核表不同（主管 M-4 R1 接受） | Penny 指定 Iris 身體面向鏡頭、有笑容、不要背部回眸或轉頭；所以正面看鏡頭。主管 M-4 R1 接受「正面看鏡頭」；prompt 不變，出圖後依驗收條件判定。 |
| §七 表情與姿勢是同一個連續動作 | 符合 | 站定、插腰碰髮、明亮的笑。 |
| §七 主光打在臉上、背景光與臉部光一致 | 與稽核表不同（主管 M-4 R1 接受） | 主光是她身後側方的低角度夕陽（輪廓光），臉靠前方大反光板與柔光；風險「逆光臉暗」已列，出圖後檢查臉部亮度與光向一致。主管 M-4 R1 接受「夕陽輪廓光配前方補光」；prompt 不變，出圖後依驗收條件判定。 |
| §七 皮膚寫毛孔與質感，沒有 smooth／flawless／porcelain | 符合 | Natural skin texture with visible pores, unretouched。 |

## 6. 現在能準備的

- V-iris-chen 的企劃內容與最終 prompt（已接受版本，R7 不改）。
- 生成比例 3:4 與直式工作照片框 120×160 mm（R6 已接受）。
- 身分句與身材數字（寫在 prompt 開頭）；Soul 使用方式（ID 不公開）。
- 送生成前檢查的預先核對結果（第 5 節）。
- 首張驗收條件與套框、有效 ppi 的計算方式。
- 送出前後查交易明細的對帳步驟與回報格式。

## 7. 生成前的確認事項（M-4 R1 逐項狀態；不猜測）

| 項目 | 狀態 | 說明 | 來源檔 |
|---|---|---|---|
| 生成與費用授權 | 已授權（M-4 R2，限 1 張） | Penny 同意：V-Iris 試拍 1 張、預算最多 1 credit、送出前精確報價須 ≤0.12、只送一次，失敗或逾時都不重送。不擴大為 24 套生成、訓練或重試授權。 |  |
| 模型與參數 | 已核對（M-4 R1） | 2026-10-20 唯讀查詢 soul_2：quality 1.5k／2k（預設 2k）、Soul ID、style_id（選填）、最多 1 張參考圖；比例含 3:4；沒有 seed 與 negative prompt。生成當下再核一次。 |  |
| Iris 的 Soul 狀態 | 已核對（M-4 R1）；正式驗證沒有 | 唯讀查詢：名稱 Iris Chen、soul_2、ready。專案內 12 處紀錄指向同一個 Soul。沒有 6 張驗證紀錄；依指示不重訓、不補生，以既有生產紀錄＋首張驗收代替（需主管接受）。 |  |
| 輸出尺寸 | 歷史紀錄已核對；本張待出圖 | 本機 Iris 的 3:4 輸出 59 張都是 1536×2048；生成筆記明寫 soul_2＋此 Soul、2k、3:4 輸出 1536×2048。這一張的實際像素要出圖後確認。 | `kols/iris-chen/generation_notes.md 第 971–973 行` |
| 費用 | 報價已取得（M-4 R1）；實扣待生成 | 2026-10-20 不扣款的報價預檢（與首試設定和 prompt 完全相同）：credits 1／credits_exact 0.12；前後交易明細沒有新增。0.12 是報價，不是實扣；歷史約數另列。 | `kols/iris-chen/generation_notes.md 第 448–453 行`、`docs/calendar/data/cal_m3_shoot_plan.json（execution.cost）` |
| 免費額度 | 已核對（M-4 R1） | soul_2 支援免費無限額度，但這個帳號目前不可用（available false）；首試設定 use_unlim false，用 credits 付費。 |  |
| 失敗與上限 | 建議已提出（M-4 R1） | 失敗可能退款也可能不退（兩種都有紀錄）；建議單次上限 1 credit、1 個請求、不重試。見「首試前核查」。 |  |
| 已接受 prompt 與稽核表的差異 | 主管已接受（M-4 R1） | 胸口高度不補寫公分、正面看鏡頭、夕陽輪廓光配前方補光；prompt 不變，出圖後依驗收條件判定。 |  |

## 8. 首張驗收條件

### 身分與身材

- [ ] 臉與 Iris 人設一致：圓臉甜美、大雙眼皮深棕眼、飽滿嘴唇、小下巴；不像另一個人。
- [ ] 膚色是她原本的白皙自然，沒有被夕陽拍偏或過飽和（風險：膚色被夕陽拍偏）。
- [ ] 黑色柔順直髮自然垂放過肩；成人樣貌。
- [ ] 身材比例符合 162 cm、87-58-90、D：胸部飽滿、腰細、臀部有形；不是童顏或身材縮水。

### 服裝

- [ ] 白色貼身羅紋方領短袖短上衣，露出腰；呈現胸型但不走光。
- [ ] 淺藍高腰牛仔迷你裙，整條入鏡。
- [ ] 小金色圈耳環；鞋不入鏡。
- [ ] 衣服上沒有亂碼文字、品牌或多餘配件。

### 姿態與手指

- [ ] 身體正對鏡頭站立，重心在一腳、臀部微偏；沒有回頭或轉身。
- [ ] 一手插腰、一手輕碰太陽穴旁的頭髮；兩隻手各五指，沒有融合、黏連或多指（風險：碰頭髮的手指融合）。
- [ ] 沒有多餘肢體；掃過畫面四角與背景（SEXY_SCENE_LIBRARY.md §10）。
- [ ] 手指判讀用原生解析度或零插值放大（QA-1）。若手指壞掉，只記錄、停下回報；改成兩手插腰要另外的指令。

### 表情與視線

- [ ] 明亮溫暖的笑，只有一個表情。
- [ ] 看鏡頭；眼睛對焦清楚。

### 場景

- [ ] 台北河濱公園開闊草地、傍晚低太陽、遠處柔綠樹林與低矮公寓。
- [ ] 草地與小徑沒有可辨識臉的路人；若遠處有失焦、認不出臉的人形，依 SEXY_SCENE_LIBRARY.md §3-F 第三次補正不算瑕疵，但與企劃「空無一人」有落差，要記錄回報。
- [ ] 沒有招牌或亂碼文字；背景不像拼貼、沒有糊掉的區塊。
- [ ] 光向一致：夕陽在她身後側方形成頭髮與肩線輪廓光，臉由前方補光照亮、不暗（風險：逆光臉暗）。

### 構圖

- [ ] 直式 3:4；大腿中段以上，下緣在大腿中段、明顯高於膝蓋。
- [ ] 人物置中、頭頂上方少量留白（規劃約 8%）；兩側是柔焦的草地與樹林。
- [ ] 雙手都在畫面內；85mm 自然透視、沒有廣角變形；水平不歪。

### 質感

- [ ] 自然皮膚紋理、看得到毛孔，不過度光滑或蠟感。
- [ ] 專業寫真質感，不是手機自拍感。

### 生成後套框與有效 ppi

- [ ] 記錄實際輸出像素（預期 1536×2048，以實際為準）。
- [ ] 套進直式工作照片框 120×160 mm：3:4 放入 3:4 不裁切；若實際不是 3:4，記錄裁切量與位置。
- [ ] 套框後髮頂上方 ≥4%，臉與雙手都在框內。
- [ ] 有效 ppi＝實際寬度像素 ÷（120 mm ÷ 25.4）；1536 px 約 325 ppi。300 ppi 是本案工作目標，不是廠商已確認的門檻。
- [ ] 不靠放大補像素；這是工作版型核對，不是印刷驗收（廠商規格與實際套版仍未知）。

### 判定與回報

- [ ] 逐項寫「符合／不符合／待 Penny 判斷」，附實圖與實際扣款。
- [ ] 通過也好、不通過也好，都先停下交主管覆核；不自動重試。

## 9. 這份文件不代表

- 不代表已生成：生成 0 張、生成任務 0。
- 不代表費用核准：credits 0；M-4 R1 只做唯讀查詢與不扣款的報價預檢。
- 不代表印刷驗收：照片框是本案工作版型，不是廠商規格或印刷安全。
- 不重新請 Penny 選企劃：V-iris-chen 已接受。
