# Sophia Tseng — AI 生成規劃（Generation Notes）

> **status: PENDING — 這是規劃文件，不是生產紀錄。** 目前尚未執行任何實際 AI 生成（無訓練圖、無 Soul 訓練、無正式產出影像或影片）。以下 prompt 與批次規劃為「準備開始生成時」的參考草稿，實際執行後請依真實結果更新本檔，並補上真實的 job id / soul id / 生成日期。

---

## 人物設定

| 欄位 | 設定 | 狀態 |
|------|------|------|
| 名字 | Sophia Tseng（曾詩妃） | — |
| 年齡 | 28 歲 | — |
| 國籍 | 台灣 | — |
| 臉型參考 | **（2026-07-30 更新，見下方章節）** 心形臉，高而柔和的顴骨，下顎線條收得溫柔纖細、收至柔軟的尖下巴（刻意不是鵝蛋臉，也不是銳利方下顎），眼神溫暖圓潤有神，鼻梁挺直，唇形飽滿帶真笑，膚色白皙透亮有光澤。**純粹描述性特徵，不參考任何真實名人臉型或身材。刻意與 Rainie Hsu 的鵝蛋/銳利臉型做出結構性區隔。** | — |
| 身材 | **（2026-07-30 更新）** 纖細修長沙漏身形：168cm，84-60-86cm（C 罩杯），腰臀比約 0.70，腿長 83cm——比誇張豐滿的曲線更收斂、更修長，上圍精巧自然不誇張，肩頸線條優雅，站姿坐姿永遠挺直。刻意與 Rainie Hsu（94-59-92cm，F 罩杯，張揚沙漏比例）做出區隔 | — |
| 髮型 | **（2026-07-30 更新）** 暖栗棕色髮絲（不是純黑）——招牌造型是後頸低盤髮髻（chignon），兩側留幾縷髮絲自然垂落；放下時是及下巴到鎖骨長度的俐落 bob，側分，永遠不留長髮披肩。刻意與 Rainie Hsu 的長黑直髮做出區隔 | — |
| 穿衣風格 | **（2026-07-30 更新）** Quiet luxury：寬版喀什米爾針織、垂墜感絲質襯衫、挺括剪裁西裝外套、寬口褲、寬鬆繫帶絲質家居袍，輪廓寬鬆挺括而非貼身緊繃，色調偏 ivory／香檳米／深炭灰／駝色。刻意避免任何讀起來像 bodycon／緊身洋裝的剪裁 | — |
| 眼鏡 | 平時不戴；度假或機場造型偶爾配戴太陽眼鏡 | — |
| 氣質關鍵字 | 沉靜、篤定、從容、不費力、有距離的優雅、克制的性感 | — |
| **Soul 訓練** | 尚未開始 | **PENDING** |
| **訓練圖張數** | 0（尚未生成） | **PENDING** |
| **Soul ID** | 無（尚未建立） | **PENDING** |

---

## Face/Style 探索批次（Discovery Batch）— 2026-07-25（第一輪，已否決）

> **status: REJECTED — 已被使用者否決，改用 Seedream 4.5 重新生成（見下方「2026-07-25 三次修正」章節）。** 這一批是「找臉」用的第一輪探索批次，用 `soul_2`（無 `soul_id`）text-only 生成，**未建立 Reference Element、未 anchor、未進入 Soul 訓練**。使用者反饋：4 張彼此臉型不一致（`soul_2` 沒有 `soul_id` 時每次獨立生成都是不同臉），且整體「太醜，不是標準美女的長相」——兩個問題都指向同一個根因：`soul_2` 沒有可重複使用的身分錨點，加上當時的臉部描述用詞（「calm, distant, languid」語感）偏冷、偏疏離。檔案已改名為 `round1_candidate_01.png`–`round1_candidate_04.png` 保留備查，**不再作為候選**。

- **平台／模型**：Higgsfield，`soul_2`（Higgsfield Soul 2.0，text-only 一次性角色參考，**未帶 `soul_id`**——尚無 Soul 可用）；quality 2k
- **Prompt 來源**：當時沿用的核心 Prompt 結構（含 168cm／88-58-89cm／D 罩杯等三圍數字、室內奢華光線配方一），但臉部描述仍是修正前的「calm composed eyes... subtle relaxed curve」語感，**未包含**溫暖真笑、主流美女錨定、或膚色白皙的用詞
- **成本**：generate_image 帳前預檢（get_cost）估算約 0.12 credits／張；實際生成後帳戶餘額由 18.23 → 16.07 credits，本批次 4 張實際共花費 **2.16 credits**
- **產出**：4 張候選圖，已否決，改名保存於 `kols/sophia-tseng/images/face_reference/`

| 檔名（已改名） | 角度／構圖 | Job ID | 狀態 |
|------|-----------|--------|------|
| round1_candidate_01.png | 正面特寫大頭照（headshot） | `0d40d2f1-8ce3-4a1f-863d-a5a6ae7f3491` | ❌ 已否決（臉部不一致＋不夠主流美女） |
| round1_candidate_02.png | 正面半身（waist-up） | `11b6948e-aebc-40c7-aace-5fd37300d907` | ❌ 已否決 |
| round1_candidate_03.png | 3/4 側身半身，頭轉回鏡頭 | `4936f551-9e0f-4fde-b95b-41e7bb9638b3` | ❌ 已否決 |
| round1_candidate_04.png | 正面全身（head-to-toe） | `6b2b5927-5ec7-4fc6-ac6e-fdcacc828785` | ❌ 已否決 |

**下一步（已執行，見下方章節）**：
1. ~~使用者從 4 張候選圖中挑出最喜歡的臉／風格~~ → 使用者否決全部 4 張
2. 改用 `seedream_v4_5`（工作室唯一驗證過能穩定輸出一致臉孔的模型，見 `iris-chen/generation_notes.md`）＋修正後的臉部描述，重新跑第二輪探索批次
3. 待使用者從第二輪 4 張中挑出喜歡的臉／風格後，才建立 Reference Element 錨定身分，依「計畫批次 Prompt 規劃」6 個批次擴充成完整訓練圖集
4. 挑選訓練圖後才進入 Soul 訓練（`status: PENDING`，尚未開始）

---

## 2026-07-25 三次修正：改用 Seedream 4.5 並修正臉部描述 prompt 本體

> **status: REJECTED（2026-07-30）— 使用者看過這一輪 4 張候選圖後，反饋臉型、髮型、妝容、身材都跟 Rainie Hsu 太過同質化，且服裝不好看，要求全部重新生成並換一個視覺設定。檔案已改名為 `round2_candidate_01.png`–`round2_candidate_04.png` 保留備查（因為 `round1_candidate_*` 檔名已被第一輪否決批次占用），不再作為候選。詳見下方「2026-07-30 全面重新設計」章節，該章節取代本節「核心 Prompt 結構」的臉部/身材/髮型描述。** 本次修正處理兩個根本問題：(1) 模型選錯——`soul_2` 沒有 `soul_id` 時每次獨立生成都是不同臉，這正是本工作室唯一驗證有效的做法（見 `iris-chen/generation_notes.md`）明確警告過的問題，改用 `seedream_v4_5`（同一份 text prompt 能穩定輸出高度一致的臉孔）；(2) 臉部描述 prompt 本體從未真正跟上 `profile.json` 已修正的 `face_type` 用詞——上面「核心 Prompt 結構」區塊原本仍寫著 `calm composed eyes with a quiet self-assured gaze` 與 `full lips with a subtle relaxed curve`，沒有明講「真笑」、沒有「主流美女」錨定用詞、也完全沒提到膚色白皙，這次已直接改寫該區塊本體（見上方「核心 Prompt 結構」，**不是**只改 `profile.json`／`character.md`）。

### 改動內容

1. **模型**：`soul_2`（無 soul_id，text-only）→ **`seedream_v4_5`**
2. **核心 Prompt 本體修正**（`generation_notes.md` 上方「核心 Prompt 結構」區塊，已直接改寫，非規劃草稿）：
   - 舊：`calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped)` → 新：`oval face with warm, wide, expressive eyes (rounded and warm, NOT narrow, sharp, almond-shaped, or cold/blank)`
   - 舊：`full lips with a subtle relaxed curve` → 新：`full soft lips with a warm, gentle, genuine smile (NOT a flat, distant, or languid expression)`
   - 新增膚色白皙用詞：`fair, luminous porcelain-toned glowing skin ... (NOT tanned, bronzed, olive, or deep golden/wheat-colored)`（原本完全沒有提到膚色）
   - 開頭新增主流美女錨定：`breathtakingly elegant, universally-recognized mainstream beauty — the kind of gorgeous face that turns heads instantly, unmistakably and conventionally pretty (not merely handsome, striking, or interesting)`
   - POSE/ANGLE 佔位說明也加上「with a warm genuine smile or soft approachable expression, NOT a stiff, cold, or distant pose」，避免未來批次的姿態描述又讀回冷淡感
3. **本次探索批次的實際 prompt**：沿用改寫後的核心描述，場景統一為「極簡米白色調室內、大面窗自然光＋暖燈」，服裝統一為米白絲質襯衫（單一變數只變角度／構圖，與第一輪做法一致，方便比對臉孔一致性），角度沿用第一輪的四種構圖模式（正面特寫大頭照／正面半身／3/4 側身回頭／正面全身）

### 第二輪產出

- **平台／模型**：Higgsfield，`seedream_v4_5`；aspect_ratio `9:16`；quality `basic`
- **成本**：get_cost 帳前預檢單張估算 1 credit；實際生成後 4 張共扣款 **8 credits**（帳戶餘額 11.35 → 3.35，每張實際約 2 credits，高於預檢估算，已如實記錄而非沿用預檢數字）

| 檔名（已改名） | 角度／構圖 | Job ID | 狀態 |
|------|-----------|--------|------|
| round2_candidate_01.png | 正面特寫大頭照（headshot） | `e9cd4f57-ae93-4a68-aabe-7331c8e14afe` | ❌ 已否決（與 Rainie Hsu 同質化＋服裝不好看） |
| round2_candidate_02.png | 正面半身（waist-up） | `c919727f-6749-4e96-a17d-5deb1a84b748` | ❌ 已否決 |
| round2_candidate_03.png | 3/4 側身半身，頭轉回鏡頭 | `f1a59b23-a0cd-40e9-a496-7d529df06867` | ❌ 已否決 |
| round2_candidate_04.png | 正面全身（head-to-toe） | `655c6b1e-40f1-44e4-a98a-50118fa460c7` | ❌ 已否決 |

### 誠實視覺評估

- **主流美女／溫暖感**：明顯改善。4 張臉都是圓潤、有神、雙眼含笑的東亞美女臉型，笑容是真笑（露齒或嘴角上揚看得出來），不是冷淡/疏離的表情，符合 `profile.json` 修正後 `face_type` 的方向。不再有第一輪那種偏冷、偏距離感的問題。
- **臉部一致性**：4 張明顯是同一張臉——同樣的臉型輪廓、眼型、鼻型、笑容弧度、髮型（黑色直髮、中分），這正是 `seedream_v4_5` 相對 `soul_2`（無 soul_id）的優勢，符合 `iris-chen/generation_notes.md` 記錄的經驗。第一輪 `soul_2` 4 張彼此不像同一人的問題，這一輪沒有再出現。
- **待觀察的小問題**：candidate_03、candidate_04 的手臂／大腿膚色明顯比臉部更偏小麥／古銅，跟臉部「白皙有光澤」的用詞不完全一致（臉部膚色符合 fair/porcelain 的描述，但四肢偏暖偏深）。這是輕微的臉部與身體膚色不統一，如果使用者選中這批中的某一張要繼續往下建立 Reference Element，建議在後續批次的 prompt 額外強調身體膚色也要 `fair, porcelain-toned` 以求全身一致，目前尚未修正。
- **結論**：這一輪已解決使用者原本反饋的兩個問題（臉不一致、不夠主流美女），可以作為挑選候選使用；四肢膚色的小瑕疵不影響選臉，但正式擴充訓練圖集時應留意。**（2026-07-30 更新：這一輪雖然解決了「臉不一致」與「不夠主流美女」，但使用者後續反饋這一輪的臉型／髮型／身材與 Rainie Hsu 太過同質化，見下方章節，本批次已被否決並改名為 `round2_candidate_01–04.png`。）**

---

## 2026-07-30 全面重新設計：與 Rainie Hsu 視覺區隔＋穿搭修正

> **status: 新一輪 Discovery 批次已生成，等待使用者挑選。** 本次是本檔案第三次視覺調整（第一次是 2026-07-25 從 `soul_2` 換成 `seedream_v4_5`；第二次是同日修正臉部溫暖度用詞），這次處理的是完全不同的問題：**視覺同質化**，不是臉部一致性或主流美女程度的問題。

### 使用者反饋原文

> 「Sophia 這個人設我想要全部重新生成。因為她的臉跟 Rainie 的太同質化了，一點都看不出來區別，髮型、妝容、身材都蠻類似的，而且穿著也不是很好看。所以重新生成新的，幫她換一個設定吧。」

比對兩人 `profile.json` 的 `identity.appearance` 欄位後確認根因：Sophia（168cm／88-58-89cm／D 罩杯／長直髮或大波浪黑髮／鵝蛋臉溫暖大眼）與 Rainie（165cm／94-59-92cm／F 罩杯／長直黑髮／鵝蛋臉＋高顴骨銳利下顎）在數字上雖有差異，但用詞的「形容詞骨架」太像（都是鵝蛋臉、都是溫暖大眼系的東亞美女臉、都是黑髮長髮放下、都是沙漏身形），導致模型實際生成出來的臉/髮/身材趨同。Sophia 的職業設定（居家美學顧問、quiet luxury 貴婦名媛）完全保留，**沒有改動人格特質、內容支柱、或聲音語氣**，只重新設計視覺識別。

### 差異化改動與理由

| 維度 | 舊版（造成同質化） | 新版（2026-07-30） | 為何能與 Rainie 區隔 |
|------|------|------|------|
| **臉型** | 鵝蛋臉，溫暖圓眼，飽滿唇（跟 Rainie 的鵝蛋臉+高顴骨用詞骨架太像） | **心形臉**，高而柔和的顴骨，下顎線條收得溫柔纖細，收至一個**柔軟的尖下巴**（NOT 鵝蛋臉，NOT 銳利方下顎） | Rainie 是鵝蛋臉+雕塑感銳利下顎+高顴骨的 glamour 臉；Sophia 改成心形臉+柔和顴骨+尖下巴，臉型輪廓的幾何形狀本身不同，同時保留「溫暖、非冷淡」的修正成果（沒有退回 2026-07-25 之前那種偏冷的問題） |
| **髮型** | 深色髮絲，俐落直髮或大波浪，放下 | **暖栗棕色**（不是純黑）髮絲，招牌是**後頸低盤髮髻／chignon**；放下時是**及下巴到鎖骨的短 bob** | Rainie 是長黑直髮、永遠放下、及腰或及肩；Sophia 改成暖棕色調＋盤髮為主／及短 bob，長度、髮色、髮型三個變數都不同，不再是「兩個都是黑長直髮放下」的讀法 |
| **身材** | 168cm，88-58-89cm，D 罩杯，腰臀比 0.65（豐滿沙漏） | 168cm（不變），**84-60-86cm，C 罩杯，腰臀比約 0.70**——更收斂、更修長的沙漏身形，上圍刻意改小且不強調豐滿 | Rainie 是 94-59-92cm／F 罩杯的張揚豐滿沙漏；Sophia 改成上圍更小、腰臀比更平緩（0.70 vs Rainie 的 0.64）的纖細修長路線，兩人的身材「情緒」不同——一個是張揚曲線，一個是收斂修長 |
| **服裝** | 絲質洋裝、絲質睡袍、「裡面幾乎什麼都沒穿」的西裝外套——輪廓偏貼身、風險接近 Rainie 的招牌 bodycon 剪裁 | 寬版喀什米爾針織、垂墜絲質襯衫、挺括西裝外套＋寬口褲、寬鬆繫帶家居袍——**輪廓全面改成寬鬆／挺括**，色調加入駝色，`profile.json`／`character.md`／`content_style.md` 已同步改寫，明確排除 bodycon／緊身洋裝剪裁 | Rainie 的招牌是黑色 bodycon 貼身洋裝、statement 珠寶；Sophia 改成寬鬆挺括剪裁＋極簡真品珠寶，剪裁邏輯完全相反（寬鬆 vs 貼身），色調也拉開（ivory/駝色/炭灰 vs 黑色/紅色/銀色） |

同步更新的檔案：`profile.json`（`identity.appearance` 全欄位、`identity.appearance.measurements`、`content.pillars` 穿搭支柱描述）、`character.md`（外型表格列、服裝參考表、不出現的視覺元素）、`content_style.md`（各支柱視覺規格的服裝描述、頂部校對記錄新增 2026-07-30 說明）、本檔案的「人物設定」表與「核心 Prompt 結構」（整段替換，見上方章節）。

### 套用的新 SEXY_SCENE_LIBRARY.md 規則（2026-07-30 新增）

本次批次同時套用了使用者提到的四條新規則：
1. **第 2 點附加**：自拍鏡頭改用較柔和的前鏡頭畫質語言（`front camera quality, slightly softer focus than a rear camera shot...`），不再跟他拍/candid 鏡頭共用同一套 `crisp sharp focus`。
2. **第 2b 點**：4 張中安排了 1 張 CCD 數位相機質感（candidate_03）與 1 張美顏 App 濾鏡質感（candidate_01），不是整批統一 iPhone 直出質感。
3. **第 7 點**：4 張裡 2 張自拍視角（candidate_01 正面特寫、candidate_04 鏡子自拍）＋ 2 張他拍/候補抓拍視角（candidate_02 居家半身、candidate_03 街頭 3/4 側身），不是單一視角。
4. **第 8 點**：4 張的服裝全部走「居家放鬆」「日常外出」這類日常款（奶油色棉織衫、寬口褲、駝色大衣），沒有使用「正式外出」或「飯店旅遊」的招牌造型當作參考錨定圖。

### 新批次產出

- **平台／模型**：Higgsfield，`seedream_v4_5`；aspect_ratio `9:16`；quality `basic`
- **成本**：`get_cost` 帳前預檢單張估算 1 credit；實際生成 4 張後帳戶餘額由 2774.7 → 2724.7 credits，本批次實際共扣款 **50 credits**（每張約 12.5 credits，高於預檢估算，如實記錄）。生成過程中曾多次遇到 `429 rate_limit_reached`，等待約 1–2 分鐘後重試即恢復正常，非本批次特有問題

| 檔名 | 角度／構圖 | 視角 | 相機風格變化 | Job ID |
|------|-----------|------|------|--------|
| candidate_01.png | 正面特寫大頭照（headshot），暖栗棕色 bob 放下 | 自拍（前鏡頭，柔焦） | 美顏 App 濾鏡 | `e9b39440-8467-451e-95be-b056b897728d` |
| candidate_02.png | 正面半身（waist-up），低盤髮髻，奶油色喀什米爾針織＋炭灰寬口褲 | 他拍/候補抓拍（後鏡頭，銳利） | 一般 iPhone 直出 | `b0e814f6-bb0d-47a9-9489-61dd242946ac` |
| candidate_03.png | 3/4 側身，頭轉回鏡頭，信義區街頭日常，駝色大衣 | 他拍/候補抓拍（路人視角） | CCD 數位相機 | `755079df-43bb-49df-943c-60f2697a43f6` |
| candidate_04.png | 正面全身（head-to-toe），更衣間鏡子自拍，象牙白喀什米爾開衫＋駝色寬口褲 | 自拍（鏡子，手機入鏡，前鏡頭柔焦） | 一般 iPhone 直出 | `c16c08f6-45c4-4be4-b1c5-49966142d113` |

### 誠實視覺評估

- **(a) 是否與 Rainie Hsu 視覺區隔明顯**：**是，明顯改善。** 直接比對 Rainie 現有 `candidate_01.png`／`candidate_02.png`（長黑直髮放下、鵝蛋臉+高顴骨+銳利下顎、黑色/白色貼身緊身上衣＋牛仔褲/白色打底褲）後確認：新版 Sophia 4 張的髮色明顯偏暖栗棕（不是純黑）、髮型是低盤髮髻或及肩 bob（不是長髮放下）、臉型是圓潤心形臉+柔和顴骨（比 Rainie 更軟、更沒有攻擊性的下顎線）、服裝是寬鬆喀什米爾針織/寬口褲/駝色大衣（不是貼身上衣/牛仔褲）、色調是 ivory/駝色/炭灰（不是黑白）。四個維度（髮色、髮型、臉型、服裝輪廓+色調）都做出了結構性區隔，不再是「同一張臉換衣服」的觀感。
- **(b) 是否仍溫暖／大眾審美的漂亮，沒有退回冷淡感**：**是。** 4 張的表情都是真誠的溫暖微笑或放鬆的笑意（candidate_01、02、03 都有明顯眼神含笑與嘴角上揚，candidate_04 是自然的鏡前微笑），沒有出現 2026-07-25 之前那種冷淡/疏離的問題，符合 `profile.json` 修正後的 `face_type` 方向。
- **(c) 服裝是否讀成「安靜奢華／優雅日常」而不是不好看或跟 bodycon 太像**：**大致是，但有一處值得注意。** candidate_02（奶油針織+炭灰寬口褲）、candidate_03（駝色大衣+絲質襯衫+寬口褲）明確是寬鬆挺括剪裁，質感清楚，完全不是 bodycon 讀法。candidate_04（更衣間鏡子自拍）外層是寬鬆喀什米爾開衫＋寬口褲，輪廓正確，但**內搭的絲質細肩帶背心領口偏低、露出的乳溝比預期明顯**——雖然色調（香檳色）與材質（絲質）都在人設範圍內，且外層開衫仍維持寬鬆廓形，但這件內搭本身比「日常居家服」再性感一點，嚴格來說跟第 8 點「discovery 圖穿搭要日常，不要角色最極端造型」的精神有一點點拉扯，建議如果使用者選中這張要繼續往下走，可以要求後續批次把這件內搭換成領口更高的款式，或保留但只用在明確標記為「換裝/穿搭」情境的正式批次，不用在其他更衣間之外的日常參考圖。
- **(d) 自拍鏡頭是否比他拍鏡頭明顯更柔/畫質更低**：**部分達成，效果不完全一致。** candidate_01（正面特寫自拍＋美顏濾鏡）明顯比 candidate_02／candidate_03 柔焦、膚色更均勻打亮，前鏡頭質感的差異看得出來。但 candidate_04（鏡子自拍）畫面整體仍然相當銳利清晰，跟 candidate_02／03 的他拍鏡頭在銳利度上差異不大，「前鏡頭較柔」的效果在這張沒有明顯讀出來——這是本次執行上的小落差，如果之後要更嚴格套用這條規則，candidate_04 這類鏡子自拍的柔焦程度可能需要在 prompt 裡再加重（例如更明確地降低對比/銳度用詞）。
- **臉部一致性（附帶觀察）**：4 張並非用同一個 Reference Element 錨定生成（純文字 discovery 批次，本來就允許），但實際輸出的臉型（心形臉、柔和顴骨、圓潤雙眼、暖棕髮色）在 4 張之間相當接近，如果使用者選中其中一張，仍建議按標準流程建立 Reference Element 後再擴充訓練圖集，以確保後續大量生成的身分穩定一致。
- **結論**：本輪已達成使用者要求的「與 Rainie 視覺區隔」核心目標，四個對照維度中三個（臉型、髮型、服裝輪廓+色調）效果清楚，第四個（自拍畫質應更柔）效果部分達成；服裝整體方向正確，但 candidate_04 的內搭領口比日常參考圖預期的稍微性感一點，已如實記錄，建議使用者選圖時留意。

### 檔名處理說明

`round1_candidate_01–04.png` 這個檔名已被第一輪（2026-07-25，`soul_2` 無 soul_id）否決批次占用，因此本次「原本要否決的第二輪」（2026-07-25 三次修正後產出的 `candidate_01–04.png`）改名為 **`round2_candidate_01–04.png`**，而不是覆蓋成 `round1_candidate_*`。新一輪（本章節，2026-07-30）產出的 4 張圖沿用標準檔名 `candidate_01–04.png`。

---

## 訓練圖生成流程規劃（尚未執行）

> 以下沿用工作室既有的生成流程慣例（參考 `iris-chen/generation_notes.md`），實際平台與模型待正式開始生成時確認與記錄。

### 平台與模型（提案，待確認）

- **平台**：Higgsfield.ai（工作室既定平台）
- **模型**：提案沿用 Seedream 4.5（`seedream_v4_5`），因其對亞洲臉孔生成品質穩定；實際是否採用需在首批測試後確認並記錄結果
- **理由**：Sophia 的美學是「成熟、精緻、克制」，需要模型在光線與皮膚質感上表現乾淨、低對比，避免過度銳化或棚拍感——但「克制」指的是色調與構圖，**不是**畫質或光線刻意調差，這點在 2026-07-25 校準後尤其重要（見下方修正記錄）

### 批次規劃（提案）

- 提案共 6 個批次，對應六個核心場景（見下方「計畫批次 Prompt 規劃」），涵蓋人物設定中六大內容支柱（早晨／穿搭／浴室／居家／飯店旅遊／健身）
- 每批次提案生成 2 張（同場景多張差異有限，不需要 4 張）
- **總計畫張數：待實測後決定，此處不預設具體數字**
- 每個批次的 prompt 均依 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五點檢查清單撰寫（皮膚質感／拍攝裝置感／符合場景類型的光源配方／背景生活雜物／完整明確服裝），詳見下方各批次 prompt

### 待辦事項

1. 依下方核心 prompt 結構與批次規劃，於 Higgsfield 進行首批測試生成
2. 確認臉型、身材比例、氣質是否符合設定，必要時調整 prompt 用詞
3. 挑選訓練圖，送入 Soul 訓練流程
4. 訓練完成後，將真實 Soul ID、訓練圖路徑、生成日期回填本檔案

---

## 核心 Prompt 結構

> **⚠️ 2026-07-30：本節 prompt 本體已整段替換，不是修補。** 舊版核心 prompt（`oval face`＋`88cm bust D cup`＋`sleek straight or softly waved dark hair`）正是造成 Sophia 與 Rainie Hsu 視覺同質化的根本原因之一——臉型描述詞（鵝蛋臉＋溫暖大眼＋直挺鼻梁＋飽滿唇）和 Rainie 的臉型 prompt 在關鍵形容詞上高度重疊，身材數字（88-58-89cm）與髮型描述（深色直髮/大波浪，放下）也和 Rainie（94-59-92cm，長黑直髮放下）在生成模型眼中太接近，導致實際輸出的臉/髮型/身材趨同。以下是全新的核心描述，三個維度（臉型、髮型、身材比例）都做了結構性改寫，服裝語言也改寫為寬鬆挺括剪裁，取代舊版可能被讀成貼身的絲質洋裝語言。詳細差異化理由見下方「2026-07-30 全面重新設計」章節。

> 以下為可重複使用的基礎描述，維持五官、身材比例、氣質的一致性；場景、服裝、拍攝裝置、光源、背景雜物依批次變化，依 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五點檢查清單撰寫（含 2026-07-30 新增的第 2b／7／8 點：相機濾鏡風格變化、自拍與他拍比例、discovery 圖穿搭要日常）。全部為純物理／氣質描述詞，**不引用任何真實名人姓名或臉型**。

```
28-year-old Taiwanese woman, breathtakingly elegant, universally-recognized mainstream beauty — the kind of gorgeous face that turns heads instantly, unmistakably and conventionally pretty (not merely handsome, striking, or interesting), heart-shaped face with soft high cheekbones and a gently tapered jawline narrowing to a soft, delicate pointed chin (NOT a rounded oval face, NOT a sharp angular jaw), warm, wide-set expressive eyes (rounded and warm, NOT narrow, sharp, almond-shaped, or cold/blank), straight refined nose bridge, full soft lips with a warm, gentle, genuine smile (NOT a flat, distant, or languid expression), fair, luminous porcelain-toned glowing skin with visible pores and subtle natural texture (NOT tanned, bronzed, olive, or deep golden/wheat-colored), slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slender elongated hourglass figure, 84cm bust (C cup, modest and natural, NOT dramatically full), 60cm narrow waist, 86cm hips, waist-to-hip ratio approximately 0.70 — a leaner, more streamlined silhouette than a dramatic curvy hourglass (deliberately distinct from a full-bust F-cup glamour figure), long lean legs, elongated graceful silhouette, elegant shoulder and neck line, calm and composed in poise and posture but warm and approachable in facial expression, always poised upright posture with natural unforced elegant movement (never a stiff standing pose), warm dark chestnut-brown hair (NOT jet-black), styled in her signature sleek low bun/chignon at the nape of the neck with a few soft face-framing strands loose, OR — when worn down — a polished chin-to-collarbone-length bob with a soft side part (always neat and salon-finished, NEVER long loose flowing hair past the shoulders), minimal fine jewelry — a single delicate gold ring, a thin bracelet, or a quality watch where scene-appropriate, never stacked or costume-looking, [SCENE], wearing [OUTFIT — a quiet-luxury tailored piece such as an oversized cashmere knit, a silk blouse with structured shoulders, wide-leg camel or charcoal wool trousers, a tailored long blazer worn open, or a loosely-belted silk robe — always a relaxed, structured, or wide-leg silhouette, NEVER a tight bodycon or clingy slip-dress silhouette, color-coordinated within her ivory / camel / deep charcoal / cream palette], [POSE/ANGLE — natural elegant gesture such as adjusting a cuff, looking out a window, mid-conversation, with a warm genuine smile or soft approachable expression, NOT a stiff, cold, or distant pose], [DEVICE/CAMERA SPEC — see selfie vs. candid rules below, mix both across a set], [LIGHTING RECIPE — indoor quiet-luxury recipe or outdoor/work-site recipe, see below], [BACKGROUND CLUTTER DETAIL], [OPTIONAL CAMERA-STYLE VARIANT — CCD digicam or beauty-app filter for a subset of images, see below], crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

**⚠️ 2026-07-30 新增：自拍／他拍鏡頭規格（套用 `SEXY_SCENE_LIBRARY.md` 第 2、2b、7 點）**——`[DEVICE/CAMERA SPEC]` 佔位不可統一都用同一套語言，整組素材必須混合以下兩種，且自拍鏡頭要明顯比他拍/candid 鏡頭「畫質等級更低、更柔」：

- **自拍視角（前鏡頭）**：`shot on iPhone 15 Pro front camera, front camera quality, slightly softer focus than a rear camera shot, mild natural grain, slightly lower dynamic range, gentle noise in low light, NOT ultra-crisp or overly HD`
- **他拍/候補抓拍視角（後鏡頭或路人視角）**：`shot on iPhone 15 Pro back camera, slight autofocus softness on background elements, natural highlight clipping near window light, subtle motion blur on hair/hands, faint JPEG compression at high-contrast edges, crisp sharp focus, high dynamic range`
- **鏡子自拍**需明講 `phone visible in the mirror reflection`，不要只寫「自拍」

**⚠️ 2026-07-30 新增：相機/濾鏡風格變化（套用 `SEXY_SCENE_LIBRARY.md` 第 2b 點）**——整批素材不要全部都是同一種「iPhone 直出」質感，每組至少安排 1 張套用以下風格之一：
- **CCD 數位相機質感**：`shot on CCD digital camera, soft slightly muted colors, gentle film-like grain, subtle vignette, warm nostalgic tone, lower dynamic range than modern phone HDR, Y2K digicam aesthetic`
- **美顏/美圖 App 濾鏡質感**：`soft beautifying camera app filter, subtle skin-smoothing glow, brightened even skin tone, soft dreamy focus, warm glowy filter, popular Asian beauty-camera-app aesthetic`

**⚠️ 2026-07-30 新增：Discovery／參考錨定圖穿搭要「日常」（套用 `SEXY_SCENE_LIBRARY.md` 第 8 點）**——Discovery 批次與未來建立 Reference Element 用的參考圖，服裝一律走「居家放鬆」「老友聚會／低調日常」這類日常款（寬版針織、繫帶家居袍、寬口褲），不要用「正式外出」「飯店旅遊」等場景的招牌造型，招牌造型留給之後有明確場景對應的正式批次使用。

**⚠️ 2026-07-25 燈光／身材數字校準**（**光源結論仍然有效；文中引用的三圍數字 88-58-89cm／D 罩杯已於 2026-07-30 更新為 84-60-86cm／C 罩杯，見上方「人物設定」表與下方「2026-07-30 全面重新設計」章節，此處歷史記錄保留原文不改，不代表現行數字**）：參照 `vicky-lin/generation_notes.md` 的二次修正經驗與 `SEXY_SCENE_LIBRARY.md` 2026-07-25 針對〈光源〉的修正，對本檔案做了以下校準（詳細改動另見下方「用詞備註」與各批次 prompt）：

1. **身材數字直接寫入**：核心 prompt 與全部 6 個批次的身材描述，從原本「tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve」這類模糊形容詞，改成直接寫入 `profile.json` 的實際三圍數字——168cm、88cm 胸（D 罩杯）、58cm 腰、89cm 臀、腰臀比約 0.65。避免身材跟人物設定對不上的問題（Vicky Lin 就是因為這個問題被使用者明確反饋過）。
2. **臉部／眼睛用詞檢查**：逐一檢查後，本檔案原本的批次 prompt 並未使用 `almond-shaped`、`narrow`、`sharp intense` 這類會被模型解讀成瞇眼/銳利的字眼（`character.md` 在更早一輪已修正過），但為了保險起見，仍在核心 prompt 明確加上 `(rounded and warm, NOT narrow or almond-shaped)` 作為額外防呆，避免未來任何批次不小心加回類似字眼。
3. **光源拆成兩套配方**：Sophia 的內容幾乎全是室內場景（公寓／飯店／浴室大理石／Pilates 個人工作室），過去 6 個批次全部沿用同一套「mixed color temperature、uneven light falloff、natural highlight clipping、faint JPEG compression artifacts、high-ISO noise」語言——這套語言原本是為了模擬「真實但不完美」的室內光源，但套用在 Sophia 身上風險很高：她的品牌核心就是「安靜的奢華感」，畫面必須乾淨、精緻、光線好，一旦被模型解讀成偏暗/偏灰/顆粒感重，就會直接違反她「quiet luxury 是很有質感的」這個定位（`character.md` 明講「不出現的視覺元素」包含「凌亂、沒整理過的場景」與棚拍痕跡，但沒有一句話說她的照片可以看起來畫質差）。校準後拆成兩套配方（詳見下方「用詞備註」）：
   - **室內奢華場景配方**（批次 1–5：公寓早晨／鏡前換裝／飯店套房／大理石浴室／居家夜晚）：保留自然窗光＋暖燈的混合光源邏輯（這是真實室內光的樣子，不是刻意做舊），但移除會讀成「偏暗、偏糊、畫質差」的字眼（拿掉 `uneven light falloff`、`high-ISO noise`，`highlight clipping` 僅保留在窗邊逆光這種合理情境），改用「evenly diffused, elegant well-lit, polished」等字眼明講這是精緻有質感的室內光，不是刻意不完美。
   - **戶外／工作現場配方**（批次 6：Pilates 工作室，大窗自然光＋動態訓練中）：改用 `SEXY_SCENE_LIBRARY.md` 「戶外/生活風格場景」配方——黃金時段或明亮日光＋淺景深背景虛化＋crisp high dynamic range，因為這個場景本身就是大窗日光灌入＋身體在動態訓練中，適合套用討喜自然光邏輯而非室內混合光邏輯。同樣的配方也保留給未來若新增「詹師傅工班現場」「客戶現場勘查」「巷口麵館」「永和爸媽家」等 `content_style.md` / `character.md` 提到但目前尚無批次草稿的生活主題場景使用。
4. **配件明確化**：原本 6 個批次都沒有明講首飾，只在人物設定文字裡籠統帶過「首飾極簡，只一件但是真品」。校準後每個批次都直接寫出該場景該有的具體配件（一枚戒指、一條細手鍊、一支質感手錶，或明講「不戴首飾」），不留給模型自己猜。
5. **服裝配色語言強化**：把「tastefully color-coordinated」的語言更明確地寫進核心 prompt 與各批次，確保同色系（ivory／香檳米／深炭灰／霧金）成套感被模型讀到。
6. **姿態自然度強化**：保留「篤定、從容、不費力」的方向，但每個批次都加強「自然的小動作」描述（調整袖口、望向窗外、手指劃過布料等），明確排除「stiff pose」，避免讀起來像制式站定擺拍。
7. **畫質結尾強化**：結尾統一改成「editorial-magazine-level production quality... NOT degraded, grainy, dim, or moody-dark」，因為 Sophia 的定位是全部 12 位角色裡製作質感最精緻的一位，任何一批次都不該出現偏暗/顆粒感重/做舊濾鏡的結果。

**用詞備註**：
- 刻意避免 iris-chen 系列常用的 `candid casual`／重顆粒 `film grain` 語感——Sophia 的美學是「乾淨、精緻、克制」，不是隨手感，但「乾淨」指的是**色調與構圖**，也包含光線本身——2026-07-25 校準前這裡曾寫「光源仍須依檢查清單寫成混合、不均勻的真實光源」，這個說法已修正：真實光源可以混合（窗光＋燈光），但**不等於**偏暗/偏糊/顆粒感重，見下方兩套光線配方
- `poised`、`composed`、`quiet self-assured` 等詞用來維持她「不費力」的氣質，避免生成出誇張表情或用力擺拍；同時每個批次都應包含至少一個自然的小動作（調整袖口、望向窗外、手指劃過布料、隨手摸貓），避免讀成制式站定擺拍
- 五官與身材描述詞需在每個批次中保持一致（含三圍數字），場景、服裝、裝置、光源、背景雜物、配件部分才做變化
- 皮膚質感一律使用 `visible pores`、`natural texture`、`unretouched`、`natural imperfections` 等詞，**避免** `flawless`、`smooth`、`glossy skin`、`airbrushed`、`porcelain skin`（會推向塑膠感）
- 每個批次必須具體指定拍攝裝置與鏡頭（前鏡頭自拍 / 後鏡頭 / 腳架），不留給模型自己猜
- 配件（首飾／手錶）必須逐場景明講，不能只靠「首飾極簡」這種籠統形容詞帶過

**光線配方一：室內奢華場景**（公寓／飯店／浴室大理石／Pilates 個人工作室等——她大部分的內容）：
```
soft ambient warm light — natural window daylight blending gently with warm lamp glow or marble-reflected light,
evenly diffused and flattering across her face, gentle directional falloff without harsh or heavy shadow,
elegant well-lit interior photography, polished and clear — NOT intentionally dim, imperfect, or grainy;
quiet luxury photography is well-lit and polished, not moody-dark
```

**光線配方二：戶外／工作現場／生活主題場景**（Pilates 工作室大窗日光、未來的詹師傅工班現場、客戶現場勘查、巷口麵館、永和爸媽家等）：
```
golden hour sunlight or bright clear daylight, natural directional light with soft flattering falloff,
shallow depth of field with blurred bokeh background, crisp sharp focus on subject,
high dynamic range, natural color grading — NOT degraded, dim, or muddy
```

---

## 計畫批次 Prompt 規劃（規劃中，尚未生成）

> **⚠️ 2026-07-30 過時警告**：下方 6 個批次草稿撰寫於視覺重新設計之前，臉部／身材／髮型描述仍是舊版（`mature refined oval face`、`88cm bust D cup`、`sleek straight dark hair`），服裝也仍包含「絲質洋裝」「絲質睡袍」等可能貼身的舊版語言。這些草稿**均未執行過**（狀態一律規劃中），但正式生成訓練圖集之前，必須先依上方「核心 Prompt 結構」（2026-07-30 版）與「2026-07-30 全面重新設計」章節的新臉型／身材／髮型／服裝描述整段替換，不能直接沿用下方舊草稿。
>
> 以下 6 個批次涵蓋人物設定中六大內容支柱（早晨／穿搭／浴室／居家／飯店旅遊／健身）。每個批次的 prompt 為草稿，均依 `SEXY_SCENE_LIBRARY.md` 的降低「AI 感」五點檢查清單撰寫（皮膚質感關鍵字／具體裝置與鏡頭破綻／符合場景類型的光源配方／具體生活雜物背景／完整明確服裝），正式生成前可能需要微調用詞。**狀態一律為「規劃中」，尚無任何實際輸出。**

### 批次 1 — 設計師公寓早晨（規劃中）

**場景描述**：信義區高樓層公寓，落地窗晨光灑入客廳或臥室，她剛醒，穿著絲質睡袍，手捧咖啡杯，望向窗外城市天際線。強調「安靜的富裕感」，不是刻意擺拍的晨間 routine。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair with a polished salon finish, wearing a single thin gold bracelet on one wrist and no other jewelry, standing by floor-to-ceiling window in a high-floor Taipei Xinyi apartment, city skyline visible through the window in soft morning haze, wearing an ivory silk robe with a shawl collar loosely tied at the waist, tonal ivory-on-ivory color coordination, one shoulder line slightly exposed, hem falling just above the knee, holding a ceramic coffee cup with both hands, gazing calmly out the window not at camera, natural unhurried body language mid-thought, weight settled gently onto one hip rather than standing stiffly straight, shot on iPhone 15 Pro back camera, slight autofocus softness on the city skyline in the background, subtle natural motion blur on the hand holding the coffee cup, soft ambient warm light — natural window daylight blending gently with the residual warm glow of a lamp left on from the night before, evenly diffused and flattering across her face, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished and clear, a phone charging cable coiled loosely on the floor near the window ledge, yesterday's water glass half-full on the console table, a cashmere throw left slightly rumpled on the reading chair, her phone lying face-down on the kitchen island in the background, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 2 — 絲質洋裝鏡前換裝（規劃中）

**場景描述**：全身鏡前，試穿設計師絲質洋裝，調整肩帶或衣領，頭微側評估合身度與剪裁，動作是評估而非展示。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek softly waved dark hair with a polished salon finish, wearing a single delicate gold ring, no other jewelry so the outfit itself is the focus, standing in front of a full-length mirror in a minimalist bedroom, wearing a champagne-beige silk slip dress with adjustable thin straps, a soft cowl neckline, bias-cut skirt falling mid-calf, tonal champagne-on-neutral color coordination, adjusting the shoulder strap with a natural unhurried gesture while assessing her reflection, head slightly tilted, weight shifted onto one hip, calm evaluating expression not performing for camera, shot on iPhone 15 Pro back camera on a tripod framing a candid mirror moment, slight autofocus softness on the mirror frame and edges of the reflection, subtle natural motion blur on her fingers adjusting the strap, soft ambient warm light — natural window daylight blending gently with a warm vanity lamp beside the mirror, evenly diffused and flattering, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished and clear, an open walk-in closet rail visible at the edge of frame with a few empty hangers, a pair of heels kicked off near the mirror, a phone and half-finished cup of coffee left on the dresser, a garment bag draped over a chair in the background, full body 3/4 angle mirror shot, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 3 — 五星飯店套房（規劃中）

**場景描述**：剛 check-in 的飯店套房，行李尚未完全打開，坐在大床邊，落地窗外是城市天際線，情緒是從容抵達而非興奮打卡。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair with a polished salon finish, wearing a slim gold watch and a thin gold necklace tucked beneath her collar, sitting on the edge of a five-star hotel bed with slightly rumpled crisp white linens, floor-to-ceiling window with sheer curtains showing a city skyline behind her, an open suitcase with clothes half-unpacked at the foot of the bed, wearing a tailored travel dress in charcoal wool-crepe, fitted through the waist, cap sleeves, hem at the knee, monochromatic charcoal-on-charcoal tailoring, calm composed expression looking toward the window not at camera, one hand resting lightly on the bed adjusting the cuff of her sleeve, natural unhurried arrival posture rather than a stiff sitting pose, shot on iPhone 15 Pro back camera, slight autofocus softness on the sheer curtains and skyline in the background, subtle natural motion blur on a strand of hair moved by the air conditioning breeze, soft ambient warm light — warm amber hotel lamp light blending gently with cool daylight through the sheer curtains, evenly diffused and flattering across the bed linens, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished and clear, a room-service tray with a half-eaten pastry and coffee cup on the side table, a luggage tag still attached to the suitcase handle, slippers placed unevenly by the bed, a phone charging cable draped over the nightstand, medium shot from the side, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 4 — 大理石浴室保養儀式（規劃中）

**場景描述**：大理石浴室台面前，專注地進行保養步驟，動作精確不匆忙，不看鏡頭，光線乾淨冷靜。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair pulled back neatly, no jewelry during her skincare routine, standing at a marble bathroom vanity, wearing an ivory silk robe with a notched shawl collar, loosely tied at the waist, sleeves pushed up to the forearm, tonal ivory-on-marble color coordination, applying skincare product to her face with precise unhurried movements, focused on her own reflection in the mirror not on camera, shot on iPhone 15 Pro front camera propped against the vanity mirror, slight autofocus softness on the marble reflections in the background, subtle natural motion blur on her fingertips applying the product, soft ambient warm light — cool daylight from a small bathroom window blending gently with the warm vanity bulb lights around the mirror, evenly diffused and flattering, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished and clear, a row of half-used skincare bottles and jars neatly arranged with faint fingerprint smudges on the counter, a damp hand towel draped over the faucet, a stray hair tie left on the counter, the mirror edge slightly fogged from earlier shower steam, medium close-up mirror shot, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 5 — 居家信義區公寓夜晚（規劃中）

**場景描述**：沙發上，喀什米爾家居服，手裡一杯紅酒，望向落地窗外信義區城市夜景。安靜的一個人的夜晚，姿態放鬆但依然挺直，不是刻意擺拍的放鬆時刻。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek straight or softly waved dark hair with a polished salon finish, wearing a single thin gold ring, no other jewelry for her evening at home, sitting on a sofa in a Taipei Xinyi apartment living room at night, floor-to-ceiling window behind her showing the city skyline lit up in the dark, wearing an oversized cashmere cardigan in deep charcoal over a silk camisole, wide-leg cashmere lounge pants, monochromatic charcoal-on-charcoal tonal coordination, bare feet tucked beneath her, holding a wine glass loosely by the stem, gazing toward the window at the city lights not at camera, a grey British shorthair cat named Ink resting quietly against the sofa arm beside her, one hand idly resting near the cat, natural unhurried evening posture rather than a stiff pose, shot on iPhone 15 Pro back camera, slight autofocus softness on the city night lights bokeh through the window, subtle natural motion blur on the wine glass as she tilts it slightly, soft ambient warm light — a warm reading lamp beside the sofa blending gently with the cool glow of city lights through the window at night, evenly diffused and flattering, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished, glowing, and clear even at night, a cashmere throw blanket neatly folded at the end of the sofa, an open book placed face-down on the coffee table, a half-empty wine bottle with the cork resting beside it, her phone screen dimly lit on the side table, a candle burned down partway on the console, medium wide shot, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 6 — Pilates／Reformer 訓練室（規劃中）

**場景描述**：私人 Pilates 工作室，reformer 訓練中的專注瞬間，安靜的自律，不看鏡頭，線條乾淨。強調姿態與線條的維持，不是揮汗如雨的強度展示，符合她「不費力」的整體氣質。光線配方：戶外／工作現場（大窗日光灌入＋動態訓練中，改用討喜自然光邏輯而非室內混合光邏輯）。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, faint natural sweat sheen on collarbone and temples, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek dark hair pulled back in a low bun with a few loose flyaways, small gold stud earrings only, no watch or bracelet during training, on a reformer machine in a private Pilates studio, mirror wall and large studio windows in the background, wearing fitted high-waist charcoal leggings and a fitted seamless sports bra in an ivory-champagne tone, tonal charcoal-and-ivory color coordination, mid-movement in a controlled reformer exercise, focused expression not looking at camera, natural fluid motion through the exercise rather than a static held pose, shot on iPhone 15 Pro back camera positioned on a tripod across the studio, slight autofocus softness on the reformer's springs and straps in the foreground, subtle natural motion blur on her extended leg mid-movement, bright daylight flooding through the studio's large windows, natural directional light with soft flattering falloff across her form, shallow depth of field with soft blurred bokeh on the mirror wall and studio background behind her, crisp sharp focus on her form, high dynamic range, natural color grading, a rolled yoga mat leaning against the mirror wall, a water bottle with condensation beads on the floor beside the reformer, a folded towel on the bench, her phone and a spare hair tie left on the windowsill, medium wide shot, editorial-magazine-level production quality, clean low-contrast natural color grade, quiet luxury editorial photo — NOT degraded, dim, grainy, or muddy, natural true-to-life color and skin tones, Instagram style
```

---

## 下一步

> **⚠️ 目前狀態（2026-07-30）：STOP — 等待使用者從新一輪 4 張候選圖（`candidate_01.png`–`candidate_04.png`）中挑選喜歡的臉／髮型／身材／服裝方向。本輪仍是純探索性 Discovery 批次，尚未建立 Reference Element、尚未 anchor 身分、尚未呼叫 `show_characters(action='train')`、尚未進入 Soul 訓練。在使用者明確回覆選中哪一張（或要求再修改）之前，不要自行往下推進到訓練圖擴充或 Soul 訓練階段。**

1. 使用者從 4 張新候選圖中挑出最喜歡的臉／髮型／身材／服裝方向（或反饋仍需調整）
2. 選定後，先用 `media_upload` → `media_confirm` → `show_reference_elements(action='create')` 把選中的那張圖轉成 Reference Element（`element_id`），再進行下一步——不要用純文字 prompt 各自獨立生成訓練圖集，避免身分不一致
3. 依上方「核心 Prompt 結構」（2026-07-30 版）的新臉型／身材／髮型／服裝描述，重寫批次 1–6 的草稿 prompt（目前批次 1–6 仍是重新設計前的舊版語言，見「計畫批次 Prompt 規劃」章節開頭的過時警告），並內嵌 `<<<element_id>>>` 取代文字描述五官/身形
4. 正式生成前，先用批次 1（設計師公寓早晨）做小規模測試，確認模型輸出的臉型、身材數字比例與氣質是否符合「人物設定」表格，並確認室內奢華光線配方是否讀出「乾淨精緻」而非「偏暗/顆粒感重」
5. 測試通過後依序完成批次 2–6，批次 6 額外確認戶外/工作現場光線配方（淺景深＋明亮日光）是否與其餘 5 批次的室內奢華配方在同一套身分下仍保持一致的臉部與身材識別度
6. 挑選訓練圖，進入 Soul 訓練（`status: PENDING`）
7. Soul 訓練完成後，回填真實 Soul ID、訓練圖路徑（如 `kols/sophia-tseng/images/training_v1/`）與實際生成日期，並將本檔案的規劃內容更新為正式紀錄
8. 若未來新增「詹師傅工班現場」「客戶現場勘查」「巷口麵館」「永和爸媽家」等 `content_style.md` / `character.md` 已提及但尚無批次草稿的生活主題場景，其光線配方應套用本檔案「光線配方二：戶外／工作現場」，而非批次 1–5 的室內奢華配方
