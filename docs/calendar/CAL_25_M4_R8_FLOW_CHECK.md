TASK-CAL-001／M-4／R8｜主管看圖覆核與構圖控制流程查核｜送審報告

# CAL_25 — M-4 R8 構圖控制流程唯讀查核與下一次測試提案（提案，未執行）

> 資料：`data/cal_m4_r8_flow_check.json`（不含 ID）；主管結論：`data/cal_m4_supervisor_r8.json`（逐字）；R8 測試與 Claude 自查：`data/cal_m4_r8_trial.json`；私有查核紀錄：`review/calendar/m4_r8/flow_check_log.json`。
> **狀態：提案，待主管覆核；不是生成授權。** 本輪生成 0、修圖 0、訓練 0、上傳 0、付費操作 0、部署 0。以下是 Claude 的查核與提案，不是主管驗收或 Penny 接受。

## 1. 主管看圖結論（摘要；原文見資料檔）

- 結論：REVISE，不建議採用；Penny 尚未接受。
- 改善：大燈籠減少、配色維持協調。
- 腳下留白：前腳幾乎碰影像下緣，白框不能算腳下留白。
- 人景主次：人物仍主導畫面，街道未形成共同構圖。
- 姿態：抬手側看像安排好的街拍，沒有抬頭看雪的瞬間。
- 背景：招牌、電線、桶子與停放車輛仍讓背景雜亂。
- 白邊成因：白邊成因未確認；photobook page 收尾句是待查假設，不得寫成已證實原因。該用語來自主管建議，一併記錄。
- 唯一原圖保留，不修改、不標為已接受。本輪不再安排純文字重試，也不啟動 H-Jia。
- V-Somi 照片歷程：R5 退回；R7 主管建議退回，Penny 未接受；R8 主管建議退回，Penny 未接受。24 套完成分類不變（已接受 1、退回待重規劃 5、尚未生成 18）；累計生成 8、credits 0.96。

## 2. 既有 Soul 流程能力查核（查詢日期 2026-10-24）

方法：不上傳、不建任務、不付費。查 MCP 模型 schema（models_explore get）、工具說明、get_cost 唯讀報價（前後交易與任務清單都沒變）、Higgsfield 官方說明中心頁面。沒有列出 Elements（會看到同工作區其他元素）。

| 問題 | 結論 | 狀態 | 來源 |
|---|---|---|---|
| 1. soul_id 能否與參考圖同時使用？ | 可以送出：官方說明寫「You can still apply a Soul ID character and a Soul HEX palette alongside it」（參考圖時）；MCP schema 沒有禁止（只寫 style_id 不能與參考圖並用）；唯讀報價 soul_2＋soul_id＋1 張參考圖被接受、0.12。加參考圖後身分是否仍保持：沒有證據。 | 可並用：已確認；並用後身分保持：未確認 | [官方說明 Soul 使用頁](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-soul-to-generate-images)（頁面更新 2026-09-09）；MCP models_explore get soul_2；get_cost 唯讀報價 |
| 2. 參考圖的用途是構圖、風格、身分，還是混合？ | 官方只寫「Soul 2.0 uses the reference as the primary direction」，並寫「With a reference image, the prompt field becomes unavailable」（網頁介面，Soul／Soul 2.0／Soul Cinema 都一樣）。官方沒有拆分參考圖影響構圖、光線、服裝或臉的哪一項，所以視為混合影響；具體影響範圍未確認。MCP 可同時傳 prompt，但後台會不會採用 prompt：未確認。第三方轉述「掛 Soul ID 時參考圖的姿勢與服裝被忽略」：非官方，未確認。 | 主要方向（混合）：已確認；各項影響範圍與 MCP 的 prompt 是否生效：未確認 | [官方說明 Soul 使用頁（含 FAQ）](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-soul-to-generate-images)（頁面更新 2026-09-09）；第三方搜尋摘要（Reddit 轉述） |
| 3. 有無參考強度、姿勢或構圖控制參數？ | MCP soul_2 只有 quality、style_id、soul_id、1 張參考圖、比例；沒有參考強度、姿勢、構圖、seed、negative 參數。官方說明頁也沒有強度設定。後台任務紀錄有 style_strength 1、Soul 參考 strength 1 等欄位，但 MCP 無法設定，能否調整未確認。其他工具：nano_banana_2 有 mask＋is_inpaint（限制只改遮罩區）；outpaint_image 只有比例與寬高，沒有方向或錨點參數；Nano Banana 系列官方寫可放最多 14 張參考、在 prompt 說明每張的用途。 | Soul 沒有強度／姿勢／構圖參數：已確認；後台強度可否調整：未確認 | MCP models_explore get soul_2、nano_banana_2；outpaint_image 工具 schema；[官方說明 Soul 使用頁](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-soul-to-generate-images)（頁面更新 2026-09-09）；[官方說明 Nano Banana 頁](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-nano-banana)（頁面更新 2026-09-09）；R8 本案任務紀錄（只讀本案） |
| 4. 比例、解析度、style 的相容限制與費用？ | soul_2：比例 1:1、16:9、9:16、4:3、3:4、3:2、2:3；quality 1.5k／2k（3:4 2k 實際輸出 1536×2048）；style_id 不能與參考圖並用（所以加參考圖時只能用後台預設風格）；unlim 不可用。唯讀報價：soul_2＋Soul＋參考圖 0.12；outpaint 2；nano_banana_pro 2k 2（1k 也是 2）；nano_banana_2 2k 2；gpt_image_2_5 high 2k 2.75；seedream_v4_5 basic 1。Element 建立費用：未確認。 | 已確認（報價是 2026-10-24 唯讀報價，不是帳單；Element 費用未確認） | MCP models_explore get；get_cost 唯讀報價 8 次，前後交易與任務清單不變；[官方說明 Soul 使用頁設定表](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-soul-to-generate-images)（頁面更新 2026-09-09） |
| 5. 官方有無身分保持能力與限制的說明？ | 有。官方 Soul ID 頁：「the same face appears across every generation, regardless of style, pose, or lighting」；限制：「Expect "clearly the same person" rather than a pixel-identical face」、「extreme style shifts or unusual angles can introduce small drift」、一個 Soul ID 只放一人；並寫「A reference image anchors a single generation but drifts across many separate ones」、訓練建議 20 張以上（最多 80）、訓練好的 Soul 會自動出現在 Elements。身材是否保持官方沒寫：未確認。Somi 的 Soul 名稱標示以 5 張訓練，少於官方建議；這點對全身小臉的影響未確認。Somi Soul 是否已出現在本工作區 Elements：未確認（本輪沒列 Elements）。 | 官方說明存在：已確認；身材保持、Somi Soul 在 Elements 的可用性：未確認 | [官方說明 Soul ID 頁](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-create-and-use-a-soul-id-character)（頁面更新 2026-09-02）；MCP show_characters 工具說明、status（Somi Soul ready） |

- 使用權：官方說明：「You own your outputs」、「The Terms of Use do not restrict commercial use of outputs」；上傳或使用他人影像需取得本人同意（Section 5.3）。所以底稿用本帳號生成、不含真人照片；不用網路圖片、不用其他 KOL 已接受的照片。（[官方說明](https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially)，頁面更新 2026-09-12；已確認（官方說明頁；未逐條讀完整服務條款））
- 提醒：參考圖可以送出，不等於能精準控制構圖；schema 允許，也不等於身分保持已驗證。

## 3. 路徑比較（只列有依據的三條）

| 項目 | A. 構圖底稿＋Soul 參考（推薦） | B. 構圖底稿＋Element 換人 | C. 既有 Soul 成品外擴＋遮罩清理（只當收尾工具） |
|---|---|---|---|
| 工具與必要輸入 | 第 1 步 nano_banana_pro（2k、3:4、不加參考、無身分）生成構圖底稿；第 2 步 soul_2＋Somi 既有 Soul＋底稿當 1 張參考圖（2k、3:4、不傳 style） | 第 1 步同 A；第 2 步 nano_banana_pro（或 seedream_v4_5）以底稿為參考，prompt 內嵌 Somi 的 Element 佔位符，要求只換人、其餘保留 | outpaint_image（來源可用已完成的任務；比例、寬高）補腳下雪地與街景；nano_banana_2 mask＋is_inpaint 去除招牌、電線、車輛 |
| 身分控制 | Soul ID（官方：可與參考圖並用；Somi 在 R5／R7／R8 都可辨識） | Element（官方：訓練好的 Soul 會自動出現在 Elements；但 Somi Soul 在本工作區 Elements 的可用性與非 Soul 模型的身分保真度都未確認） | 原圖像素保留（外擴只補邊；遮罩避開人物） |
| 構圖控制 | 由底稿決定（官方：參考圖是主要方向）；構圖、雜物、白邊、姿態在第 1 步就能便宜地看到，不合格就停 | 由底稿＋編輯指令；Nano Banana 官方：每張參考在 prompt 說明用途 | 只能把畫面往外補，沒有方向或錨點參數（補在哪一側未確認）；不能改姿態 |
| 光色控制 | 底稿裡的藍調＋近處燈籠暖光；第 2 步 prompt 只補身分、服裝與動作 | 編輯時可能重打光或改色，未確認 | 外擴區的光色是否一致未確認 |
| 可能改變或失去 | 參考圖是混合影響：底稿替身的臉、服裝細節可能被帶進來；MCP 的 prompt 可能不生效；也可能 Soul ID 蓋過參考構圖（第三方說法，未確認） | 身分可能比 Soul 弱；可能改到背景；需要先確認 Element（列 Elements 會看到同工作區其他元素） | R8 白邊在像素裡，外擴前要先裁掉並上傳衍生檔；姿態（主管第 4 點）無法修；每處清理都要做遮罩並上傳 |
| 步驟數 | 2 | 2（＋Element 確認） | 2–3 |
| 可確認費用（唯讀報價） | 2＋0.12＝2.12（底稿改 seedream_v4_5 basic 則 1＋0.12＝1.12） | 2＋2＝4（Element 建立費用未確認） | 外擴 2＋每次遮罩清理 2 |
| 未知項 | 參考圖各項影響範圍、prompt 是否生效、替身臉是否被 Soul 換掉 | Somi Element 是否存在、身分保真度 | 外擴方向、遮罩清理後的接縫與光色 |
| 最小測試判讀 | 第 2 張同時保住底稿構圖且臉是 Somi → 成功；構圖保住但臉不是 Somi → 身分層壓不過參考，停，改評估 B；構圖跑掉 → 參考圖在 Soul ID 下控制不了構圖，停 | 臉是 Somi、底稿其餘不變 → 可行；臉不像或背景被改 → 不採用 | 只適合構圖已大致成立、只差腳下雪地或零星雜物的照片；不建議當主流程 |
| 用於其餘月份 | 成功後每套：依 CAL_23 構圖欄位寫底稿說明 → 底稿自查 → Soul 一步；每套約 2.12（或 1.12），23 套未含重試約 48.8（或 25.8），只是依報價的估算 | 與 A 相同的每套底稿流程，第 2 步改用 Element；每套約 4 | 每套成品視需要補一步；不能解決姿態與人景主次 |

## 4. 推薦：路徑 A

身分層沿用目前唯一有證據的 Soul（官方說明＋R5／R7／R8 實際結果）；構圖改由官方寫明是「主要方向」的參考圖控制，而且構圖、雜物、白邊、姿態都能在第 1 步用底稿先檢查，不合格就停在第 1 步，不花身分那一步。兩步分開，失敗時知道是哪一層出問題。

C 不當主流程：外擴與遮罩清理改不了姿態與人景主次（主管第 3、4 點），R8 的白邊又在像素裡，要先裁切再上傳。B 留作 A 的身分層失敗時的下一步，前提是先確認 Somi 的 Element。

## 5. 下一次測試完整計畫（未執行）

- 狀態：提案，未執行；需要 Penny 授權新增支出。對象：V-somi-oh（2027 年 12 月；月份、造型、場景方向不變，只改製作流程）。
- 請求：下一次測試 1 次（第 1 步底稿）；底稿經主管看過後，第 2 步另行授權 1 次；重試 0。
- 為什麼是一張底稿：主管要求下一次只測「一張」。手上沒有構圖正確、又沒有他人臉的參考圖，所以 A 至少要兩步；建議下一次只做第 1 步（一張底稿），先看「構圖、雜物、白邊、姿態」能不能被控制，再決定是否花第 2 步。若 Penny 想一次授權兩步，上限 2.12、仍不重試。
- 預期費用（唯讀報價）：下一次 2 credits（第 1 步）；全程 2.12（第 1 步 2＋第 2 步 0.12）；底稿改 seedream_v4_5 basic：下一次 1；全程 1＋0.12＝1.12。
- 若執行：只做第 1 步：累計生成 8→9（底稿算 1 次生成，但不是月面照片）、credits 0.96→2.96（Seedream 底稿則 1.96）；兩步都做：生成 10、credits 3.08（Seedream 底稿則 2.08）。

### 5.1 第 1 步：構圖底稿（無身分；下一次的「一張」）

- 設定：nano_banana_pro、2k、3:4、count 1；參考圖：不加；Soul：不用（無身分）；不用 unlim。
- 來源與使用權：本帳號生成，官方說明：輸出歸使用者、可商用；不含任何真人照片。
- prompt（英文全文）：

```
A photograph of a quiet hot-spring town lane at blue hour in gentle snowfall, seen at eye level from across the lane, with natural perspective. Top of the picture: snow-laden wooden eaves and a strip of deep-blue evening sky. Middle: the lane recedes to the left between old dark-timber inns with closed wooden lattice doors; a few small plain paper lanterns glow under the eaves, getting smaller into the distance. Bottom third: smooth fresh snow covering the lane, untouched in the foreground. A young Korean woman with honey-orange brown hair in a layered wolf cut, wearing a long deep-cranberry wool coat over an ivory knit mini dress and white knee-high boots, walks slowly from right to left along the lane with her hands in her coat pockets, glancing up at the falling snow, her face in three-quarter view. She is a modest figure a little right of centre, with the lane opening out ahead of her; her whole body is visible, both boots stand on the snow, and a wide stretch of snow lies between her boots and the bottom of the picture. The nearest lantern casts a warm amber pool of light on her and on the snow around her; everything else stays cool blue. It is a quiet pedestrian lane: plain timber walls, lattice doors, lanterns and snow are all there is.
```

### 5.2 第 2 步：Somi 身分（Soul＋底稿參考；底稿通過後另行授權）

- 設定：soul_2、somi-oh 既有 Soul（送出前確認 ready）、參考圖：第 1 步底稿（任務 ID 當 role image）、2k、3:4、count 1；style：不傳（與參考圖不相容）；不用 unlim。
- prompt 說明：prompt 只寫身分（canon 逐字）、服裝、動作；構圖、背景、光線交給底稿。官方說明網頁介面加參考圖時 prompt 不可用；MCP 送出的 prompt 會不會生效未確認，結果要記錄。
- prompt（英文全文；前三句是 canon 身分句，逐字不改）：

```
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. Light makeup with a glossy lip, her cheeks flushed pink from the cold. She wears a long deep-cranberry wool coat over an ivory ribbed knit mini dress, white knee-high boots and small pearl earrings. She walks slowly along a snowy hot-spring town lane at blue hour with her hands in her coat pockets, glancing up at the falling snow, in the warm glow of a small paper lantern.
```

### 5.3 主管要求的四件事怎麼處理

- 避免帶入其他人的臉：底稿由模型生成、不用任何真人或網路照片，也不用其他 KOL 已接受的照片；替身臉放小、四分之三側臉抬頭看雪，減少可帶入的臉部細節；第 2 步由 Somi 的 Soul 提供身分；驗收時與 kols/somi-oh/identity/identity_master.jpg 對照，不像 Somi 就判失敗，不補救。
- 完整雙靴、腳下雪地與人景主次：在底稿裡用相對位置描述：畫面下方三分之一是未踩過的新雪，她是偏右的中等大小人物、前方留出巷道空間，雙靴站在雪上、靴下有一大段雪地；不設固定百分比，量測數字只記錄不當門檻。
- 背景整理：改選本身就乾淨的場景：步行巷、素面木牆、格子門、少量素面紙燈籠與雪，正面寫出畫面裡有什麼；不再增加否定詞（R5–R8 都寫了否定詞仍出現文字與雜物）。雜物在第 1 步底稿就檢查。
- 避免相紙框、頁面或文字版面：兩步 prompt 都拿掉 photobook／page／print 類用語與比例文字（比例只用參數）；白邊在第 1 步底稿就檢查，出現就停。這只是避開待查假設，不證明白邊成因。

### 5.4 驗收項目

第 1 步底稿（Claude 自查後交主管及 Penny 看）：

- 1. 照片填滿整個畫面，沒有白邊、相紙框、頁面或文字版面
- 2. 雙靴完整、靴下有可見雪地，沒有貼到下緣
- 3. 人與巷道共同構圖：巷道、屋簷與燈籠的退縮線條是畫面的一部分，不只是背景（看圖判斷，人物高度只記錄）
- 4. 沒有招牌文字、電線、車輛、桶子等雜物
- 5. 姿態讀得出慢走中抬頭看雪的瞬間，不是對鏡頭擺姿勢
- 6. 藍調＋近處燈籠暖光圈，酒紅／象牙白／白靴配色

第 2 步成品（Claude 自查後交主管及 Penny 看圖）：

- 1–6 與底稿相同，且沒有比底稿變差
- 7. 臉是 Somi（對照 identity_master.jpg），成年，沒有替身臉混入
- 8. 服裝正確：深蔓越莓紅大衣、象牙白針織迷你洋裝、白色及膝長靴
- 9. 1536×2048、120×160 mm 套框約 325 ppi

### 5.5 失敗停止點

- 第 1 步完成後先停下，交主管及 Penny 看底稿（預設；不自動接第 2 步）
- 第 1 步驗收 1、2、4 任一不通過 → 記錄並停，不重試；回報構圖控制在底稿層也失敗
- 第 2 步只在另行授權後送 1 次，不論結果都不重試
- 報價高於授權上限、Soul 不是 ready、或有進行中的同類任務 → 不送

## 6. 未確認問題與取得方式

1. MCP 送 soul_2＋參考圖時，prompt 會不會生效？——官方說明只講網頁介面；可由 A 的第 2 步結果判讀（服裝、動作是否跟 prompt 而非底稿），或經 Penny 同意後向 Higgsfield 支援詢問（本輪不聯絡廠商）
2. 掛 Soul ID 時參考圖還控制構圖嗎？替身臉會不會被帶入？——官方沒有拆分；只能由 A 的第 2 步判讀，或經 Penny 同意詢問支援
3. Somi Soul 是否已出現在本工作區 Elements（B 的前提）？——經 Penny 同意後做一次唯讀 Elements 列表（會看到同工作區其他元素，只記錄 Somi 那筆），或在網頁介面查看
4. outpaint 補在哪一側、能否指定？——schema 沒有方向參數；支援詢問或實測（C 不是推薦路徑，暫不需要）
5. R8 白邊成因——仍是待查假設；A 的兩步都拿掉相關用語，只能當觀察，不能當證實

## 7. 需 Penny 決定

1. 是否授權下一次測試：只做第 1 步底稿，1 次請求、上限 2 credits（或 Seedream 底稿上限 1）、不重試；或一次授權兩步（上限 2.12／1.12）
2. 底稿模型：nano_banana_pro（報價 2）或 seedream_v4_5 basic（報價 1）
3. 是否允許一次唯讀 Elements 列表，為 B 預作確認（會看到同工作區其他元素名稱，只記錄 Somi 那筆）
4. 是否允許向 Higgsfield 支援詢問未確認項目（本輪不聯絡廠商）

## 8. 必要閱讀清單

- `docs/calendar/data/cal_m4_supervisor_r8.json`（主管結論逐字、收尾句來源）
- `docs/calendar/CAL_25_M4_R8_FLOW_CHECK.md`（本文件）
- `docs/calendar/data/cal_m4_r8_flow_check.json`（查核結論、路徑、測試計畫的資料版）
- `docs/calendar/data/cal_m4_r8_trial.json`（R8 Claude 自查，保留不改）
- `review/calendar/m4_r8/V-somi-oh_m4r8_view.jpg`、`V-somi-oh_m4r8_frame_V_120x160.jpg`（R8 照片）
- `review/calendar/CAL_M4_R8_REVIEW.md`（送審紀錄）
