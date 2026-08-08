# Sophia Tseng — AI 生成規劃（Generation Notes）

> **狀態：✅ Soul 訓練已完成（`status: ready`），soul_id `192562bb-ca64-4615-9515-13d34807857c` 已可用於 `model: soul_2` 正式生成內容**
> 2026-07-30 完成第三輪五官結構重新設計（見下方「二次修正」章節），使用者核准 `candidate_01.png`–`candidate_04.png` 並指示直接送訓練（「你就直接拿去訓練吧」）。2026-07-31 已用 `candidate_01.png` 建立 Reference Element `980f8414-7709-47ff-9c88-fdc30b54d03d`，生成 13 張完整訓練集（`images/training_v1/`），並呼叫 `show_characters(action='train')` 成功受理，同日以 `action='status'` 確認 `raw_status: completed`，訓練正式完成。詳見下方「2026-07-31」章節。

---

## 人物設定

| 欄位 | 設定 | 狀態 |
|------|------|------|
| 名字 | Sophia Tseng（曾詩妃） | — |
| 年齡 | 28 歲 | — |
| 國籍 | 台灣 | — |
| 臉型參考 | **（2026-07-30 二次修正，見下方章節）** 柔和圓潤臉型，飽滿蘋果肌，無明顯顴骨線條；下顎線條柔軟、無明顯下顎角（刻意不是高顴骨，也不是雕塑感銳利下顎）；溫暖圓潤杏眼，淺內雙/近單眼皮摺痕（刻意不是又大又戲劇性的雙眼皮大眼）；鼻頭圓潤柔和（不是銳利挺翹鼻梁）；唇形自然飽滿柔和帶真笑；左眼尾下方一顆天然小痣（專屬辨識特徵）；膚色白皙透亮有光澤。**純粹描述性特徵，不參考任何真實名人臉型或身材。此為第二次修正——第一次（同日稍早）只改了髮型/身材/服裝，臉部結構仍與 Rainie Hsu 共用「高顴骨」等形容詞骨架，使用者反饋兩人五官仍太像；本次改為與 Rainie（鵝蛋臉、高顴骨、雕塑感銳利下顎、大而戲劇性雙眼皮大眼）在幾何結構上互斥、不共用形容詞的設計。** | — |
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
>
> **⚠️ 2026-07-30 二次修正（同日）：上一次替換只解決了髮型/身材/服裝，臉部本體仍是問題根源，本次再整段替換臉部描述。** 使用者看過第一次修正後的批次（已改名 `round3_candidate_01–04.png`）反饋：五官（臉型、顴骨、下顎、眼型）跟 Rainie Hsu 幾乎一樣，只是換了髮型跟衣服。根因是第一次修正的臉型描述（心形臉＋高而柔和的顴骨＋eyes rounded and warm）雖然用詞不同，但和 Rainie（oval face＋high cheekbones＋large striking double-eyelid eyes）共用「cheekbones」「大而有神的眼睛」這種形容詞骨架，本質上仍是同一種「鵝蛋/心形＋高顴骨＋大眼」的東亞美女模板，只是換了幾個形容詞，模型生成結果自然趨同。本次修正把整個臉部幾何結構方向反過來：**顴骨從「高」改成「無明顯顴骨線條的圓潤蘋果肌」，下顎從「雕塑/柔和但仍收緊」改成「柔軟無角度」，眼型從「圓潤有神的大眼」改成「杏眼＋淺內雙/近單眼皮、比大眼安靜」，並新增鼻型、唇型的具體區隔與一顆左眼尾小痣作為專屬辨識特徵**——詳見下方「2026-07-30 二次修正：五官結構重新設計」章節的逐項對照表。

> 以下為可重複使用的基礎描述，維持五官、身材比例、氣質的一致性；場景、服裝、拍攝裝置、光源、背景雜物依批次變化，依 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五點檢查清單撰寫（含 2026-07-30 新增的第 2b／7／8 點：相機濾鏡風格變化、自拍與他拍比例、discovery 圖穿搭要日常）。全部為純物理／氣質描述詞，**不引用任何真實名人姓名或臉型**。

```
28-year-old Taiwanese woman, breathtakingly warm, universally-recognized mainstream beauty — the kind of gorgeous face that turns heads instantly, unmistakably and conventionally pretty (not merely handsome, striking, or interesting), softly rounded face with full, plush cheeks and NO visible cheekbone definition (deliberately the OPPOSITE of an angular, high-cheekbone bone structure), a soft, gently-tapering jawline with no visible jaw angle or sculpted edge (deliberately NOT a sharp, defined, or sculpted jawline), gentle almond-shaped eyes with a subtle, shallow single-fold/monolid-leaning eyelid (deliberately NOT a large, dramatic double-eyelid "big eyes" shape — quieter and smaller than a striking glamour-model eye, calm and warm rather than bold or dramatic), a softly rounded nose with a gentle, unsculpted tip (NOT a sharp or high-bridge nose), naturally fuller, softly rounded lips with a relaxed, warm curve and a genuine gentle smile (NOT a flat, distant, or languid expression), a small natural beauty mark just below the outer corner of her left eye (a subtle, memorable, distinguishing detail unique to her), fair, luminous porcelain-toned glowing skin with visible pores and subtle natural texture (NOT tanned, bronzed, olive, or deep golden/wheat-colored), slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, this soft rounded facial structure is her own distinct beauty archetype — warm, gently mature, approachable — never cold, aloof, severe, or plain, and structurally distinct from an oval-faced, high-cheekbone, sculpted-jaw, large-eyed glamour archetype, 168cm tall slender elongated hourglass figure, 84cm bust (C cup, modest and natural, NOT dramatically full), 60cm narrow waist, 86cm hips, waist-to-hip ratio approximately 0.70 — a leaner, more streamlined silhouette than a dramatic curvy hourglass (deliberately distinct from a full-bust F-cup glamour figure), long lean legs, elongated graceful silhouette, elegant shoulder and neck line, calm and composed in poise and posture but warm and approachable in facial expression, always poised upright posture with natural unforced elegant movement (never a stiff standing pose), warm dark chestnut-brown hair (NOT jet-black), styled in her signature sleek low bun/chignon at the nape of the neck with a few soft face-framing strands loose, OR — when worn down — a polished chin-to-collarbone-length bob with a soft side part (always neat and salon-finished, NEVER long loose flowing hair past the shoulders), minimal fine jewelry — a single delicate gold ring, a thin bracelet, or a quality watch where scene-appropriate, never stacked or costume-looking, [SCENE], wearing [OUTFIT — a quiet-luxury tailored piece such as an oversized cashmere knit, a silk blouse with structured shoulders, wide-leg camel or charcoal wool trousers, a tailored long blazer worn open, or a loosely-belted silk robe — always a relaxed, structured, or wide-leg silhouette, NEVER a tight bodycon or clingy slip-dress silhouette, color-coordinated within her ivory / camel / deep charcoal / cream palette], [POSE/ANGLE — natural elegant gesture such as adjusting a cuff, looking out a window, mid-conversation, with a warm genuine smile or soft approachable expression, NOT a stiff, cold, or distant pose], [DEVICE/CAMERA SPEC — see selfie vs. candid rules below, mix both across a set], [LIGHTING RECIPE — indoor quiet-luxury recipe or outdoor/work-site recipe, see below], [BACKGROUND CLUTTER DETAIL], [OPTIONAL CAMERA-STYLE VARIANT — CCD digicam or beauty-app filter for a subset of images, see below], crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
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

## 2026-07-30 二次修正：五官結構重新設計 — 第三輪 Discovery 批次（已生成）

**沿用上方「核心 Prompt 結構」（2026-07-30 二次修正版）的完整臉部/身材/髮型描述，4 張皆使用日常穿搭（居家針織、絲質家居袍、寬褲），混合自拍/candid 視角＋1 張 CCD 濾鏡變化，符合 `SEXY_SCENE_LIBRARY.md` 第 2/2b/7/8 點規則。**

| 檔名 | 視角 | 穿搭 | 濾鏡/裝置 | Job ID |
|------|------|------|-----------|--------|
| candidate_01.png | 自拍（前鏡頭，俯角近景） | 米白喀什米爾針織衫 | 前鏡頭較軟畫質 | `dd23a245-5449-46bf-8656-2be370de173e` |
| candidate_02.png | 他拍/candid（3/4 半身） | 米白絲質家居袍＋米色細肩帶內搭＋炭灰寬褲 | 標準，crisp | `e33694bb-e4a7-4d3b-accf-afa59130562e` |
| candidate_03.png | 自拍（全身鏡子自拍，手機入鏡） | 駝色針織外套＋米色內搭＋炭灰寬褲 | 前鏡頭較軟畫質 | `6c76cd03-e995-4ad4-82c0-60b647f0dccb` |
| candidate_04.png | 他拍/candid（3/4 半身，床邊整理頭髮） | 米色長袖上衣＋寬鬆亞麻褲 | **CCD 數位相機質感** | `48762491-d4d3-4e1c-bf67-24849546ffa5` |

`get_cost` 預估每張 1 credit，4 張皆一次生成成功。

**誠實視覺一致性評估（親自用 Read 工具逐張檢視，並直接調出 Rainie Hsu 的實際訓練圖逐項比對五官）**：

逐項對照表（Sophia 新版 vs. Rainie Hsu 已核准版）：

| 特徵 | Sophia（本輪） | Rainie Hsu（已核准） | 是否有區隔 |
|------|---------------|----------------------|-----------|
| 臉型/顴骨 | 圓潤、豐頰、無明顯顴骨線條 | 鵝蛋臉、高顴骨、下顎線分明 | ✅ 明顯不同 |
| 眼型 | 杏眼、淺內雙，安靜溫和 | 大而有神、雙眼皮、戲劇化 | ✅ 明顯不同 |
| 妝容/眼線 | 幾乎無明顯眼線，自然妝感 | 可辨識的眼尾上揚細線＋飽和唇色 | ✅ 明顯不同 |
| 髮色/髮型 | 栗棕色，低盤髮髻或及肩鮑伯 | 黑色，長直髮放下 | ✅ 明顯不同 |
| 身材比例 | 168cm／84-60-86cm／C 罩杯，纖細修長 | 165cm／94-59-92cm／F 罩杯，誇張沙漏型 | ✅ 明顯不同 |
| 整體氣質 | 溫暖、圓潤、親和的成熟感 | 豔麗、張揚、戲劇化的性感 | ✅ 明顯不同 |

**結論：這次是真正的區隔，不是同一張臉換髮型衣服。** 4 張圖裡的臉——圓潤的臉頰、無顴骨的柔和輪廓、安靜的杏眼、栗棕色髮色——跟 Rainie Hsu 實際的訓練圖（尖下巴、高顴骨、大雙眼皮、黑髮）放在一起，即使穿同樣的衣服/髮型也不會被認成同一個人。這是本次要解決的核心問題，已經達成。

**⚠️ 誠實記錄一個瑕疵**：candidate_03 的「左眼尾小痣」這個辨識特徵，在生成結果中位置跑到了**額頭中央**，而且顏色是鮮紅色的一個圓點，視覺上更像印度傳統的「bindi/tikka」額飾，而不是原本設定的「左眼尾下方一顆不起眼的自然小痣」——這是一個未預期的生成錯誤，不是刻意加入的文化符號，且不美觀、不符合原意。**建議不要選用 candidate_03 作為身分錨點**，或如果喜歡這張的角度/穿搭，需要在下一輪重新生成時明確排除這個瑕疵（例如把「beauty mark」改成更明確的「a single small brown mole」並指定位置只在下眼尾附近，不要讓模型自由發揮位置與顏色）。candidate_01、02、04 的小痣位置與顏色都正常（左眼下方/臉頰，深棕色調），沒有這個問題。

**其他觀察**：
- CCD 濾鏡（04）風格辨識度中等，色調偏柔和但沒有非常明顯的復古顆粒感，跟 Coco Wu／Rainie Hsu 之前的 CCD 效果強度類似（風格變化存在但不算搶眼）。
- 未發現手部/肢體異常或不合理鏡頭透視問題（依 `SEXY_SCENE_LIBRARY.md` 第 10 點新規則逐張檢查）。
- 自拍（01、03）確實比他拍（02、04）柔和一些，但差異不算劇烈，跟先前其他角色的觀察一致——文字指令對「自拍畫質」的實際影響力有限。

**⚠️ 下一步（不可跳過）**：等待使用者從 4 張中選出核准的一張（**建議排除 candidate_03 因額頭瑕疵**，除非使用者不介意或想要求重新生成這張），選定後才能進入 Reference Element 錨定與完整訓練集生成。本輪**沒有**建立 Reference Element，**沒有**呼叫 `show_characters(action='train')`，`profile.json` 的 `ai_generation`／soul_id 維持原狀未變更。

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

## 2026-07-31：建立 Reference Element、生成完整訓練圖批次、送出 Soul 訓練

**觸發背景**：使用者看過第三輪五官重新設計後的候選圖（`candidate_01.png`–`candidate_04.png`，見上方「二次修正」章節），明確表示：「好吧，我覺得這邊這個 Sophia 新的，你就直接拿去，我覺得四張都可以，你就直接拿去訓練吧。」——與 Coco/Rainie/Zoe/Mia 相同的「核准即送訓練」授權模式。

### 1. 錨點選定與 Reference Element 建立

雖然使用者表示 4 張皆可接受，但延續先前已明確向使用者反映的疑慮——`candidate_03.png` 的「左眼尾下方天然小痣」實際生成結果是額頭正中央一個類似硃砂痣/bindi 的紅色印記，屬非預期瑕疵——選用 `candidate_01.png`（自拍/cashmere 毛衣款）作為身分錨點，而非隨機或使用 candidate_03。

- `media_upload` → `curl PUT` → `media_confirm`（media_id: `ddb2fa8e-f755-41fa-ba4c-6ab73b677b4a`）
- `show_reference_elements(action='create', category='character', name='sophia-tseng-face', medias=[...])` 建立成功
- **Element ID：`980f8414-7709-47ff-9c88-fdc30b54d03d`**（name: `sophia-tseng-face`）

### 2. 完整訓練圖批次生成（13 張，`seedream_v4_5`，`aspect_ratio: 9:16`）

依 `content_style.md` 六大支柱權重分配：早晨 3 張（20%）、穿搭 2 張（15%）、浴室保養 2 張（15%）、居家 3 張（20%）、飯店旅遊 2 張（15%，因總量捨入略低於 20%）、健身 1 張（10%，因總量捨入略低）。每張 prompt 皆內嵌 `<<<980f8414-7709-47ff-9c88-fdc30b54d03d>>>` 錨定身分，並依 `SEXY_SCENE_LIBRARY.md` 混合自拍/他拍視角、CCD 數位相機與美圖濾鏡風格變化、僅本人入鏡（無其他人物）、身材數據（168cm/84-60-86cm/C cup）與膚色白皙基調皆明確寫入文字。

**產出檔案**（`kols/sophia-tseng/images/training_v1/`）：
| 檔名 | 支柱 | 視角/風格 |
|------|------|-----------|
| 01_morning_window_candid.png | 早晨 | 他拍，窗邊晨光 |
| 02_morning_selfie_bed.png | 早晨 | 自拍，床上剛醒 |
| 03_morning_kitchen_ccd.png | 早晨 | 他拍，CCD 濾鏡，手沖咖啡 |
| 04_outfit_mirror_selfie_tryon.png | 穿搭 | 鏡前自拍，試穿針織衫 |
| 05_outfit_candid_blazer.png | 穿搭 | 他拍，西裝外套定裝 |
| 06_bathroom_candid_skincare.png | 浴室保養 | 他拍，大理石台面保養 |
| 07_bathroom_mirror_selfie_meitu.png | 浴室保養 | 鏡前自拍，美圖濾鏡 |
| 08_home_candid_sofa_wine.png | 居家 | 他拍，沙發夜景紅酒 |
| 09_home_candid_reading_corner.png | 居家 | 他拍，閱讀角落＋貓 |
| 10_home_selfie_couch_loungewear.png | 居家 | 自拍，沙發居家服 |
| 11_hotel_candid_bed_window.png | 飯店旅遊 | 他拍，飯店床邊晨光 |
| 12_hotel_mirror_selfie_ccd.png | 飯店旅遊 | 鏡前自拍，CCD 濾鏡 |
| 13_fitness_candid_reformer.png | 健身 | 他拍，Pilates reformer |

**生成過程的已知異常**：13 張中有 4 張（09、10、11、13）第一次呼叫遭遇 `429 rate_limit_reached`，立即重試後全數第二次即成功，無需第三次重試。

### 3. 誠實視覺評估（已用 Read 工具實際目視檢查全部 13 張，非假設）

- **身分一致性**：13 張的臉部特徵（圓潤臉型、無明顯顴骨、內雙/杏眼、柔和下顎線、左眼尾下方小痣）皆與 Reference Element 錨點一致，且與 Rainie Hsu 的尖下巴/高顴骨/大雙眼皮五官結構明確可辨識為不同人——第三輪五官重新設計的差異化目標達成。
- **手部/肢體檢查**（依 `SEXY_SCENE_LIBRARY.md` 第 10 點新規則逐張檢查）：13 張手部姿勢與手指數量皆正常，無多出的手指或肢體，無不自然關節扭曲；鏡頭角度與透視在所有張數中皆合理，無物理不可能的拍攝角度。
- **人物入鏡規則**（第 9 點新規則）：13 張皆只有 Sophia 本人入鏡，09 號圖的貓咪為場景道具動物，非人物角色，符合規則。
- **選/他拍與濾鏡變化**：5 張自拍（02、04、07、10、12）、8 張他拍/候拍，CCD 濾鏡 2 張（03、12）、美圖濾鏡 1 張（07），符合「不要整組同一種質感」的規則。
- **輕微觀察**（非缺陷，僅供未來留意）：13 號（Pilates reformer）prompt 原意是「不看鏡頭」，但實際生成結果她的視線落在鏡頭方向並帶微笑——與文字指令有落差，但不影響身分/瑕疵判斷，可接受。

**結論**：13 張訓練圖身分一致、無明顯 AI 瑕疵，符合送訓練標準。

### 4. Soul 訓練送出

依使用者指示直接送訓練，呼叫 `show_characters(action='train', name='Sophia Tseng', images=[...13張訓練圖的 job id])`，**第一次呼叫即成功受理**，取得 `soul_id: 192562bb-ca64-4615-9515-13d34807857c`，`raw_status: queued`（訓練中，尚未完成）。同批呼叫的 `items` 列表回應中，順帶確認 **Coco Wu 的訓練已從 `training/queued` 轉為 `status: ready`**（`raw_status: completed`）——已同步更新 `kols/coco-wu/` 相關檔案。

**同日追蹤確認完成**：透過 `show_characters(action='status', soul_id='192562bb-ca64-4615-9515-13d34807857c')` 確認 `status: ready`、`raw_status: completed`。Soul 訓練正式完成，可用 `model: soul_2` + 此 soul_id 生成正式發布內容。

`profile.json` 已補上 `ai_assets.training_images_v1` 完整欄位（含 Reference Element、13 張訓練圖路徑、soul_training 狀態，`status: ready`）。

---

## 下一步

1. ~~五官結構重新設計（第三輪）~~ 已完成，使用者核准並指示直接送訓練
2. ~~建立 Reference Element~~ 已完成（`element_id: 980f8414-7709-47ff-9c88-fdc30b54d03d`，錨點來源 `candidate_01.png`）
3. ~~生成完整訓練圖批次（13 張，涵蓋六大支柱）~~ 已完成，詳見上方「2026-07-31」章節
4. ~~送出 Soul 訓練~~ 已完成（`soul_id: 192562bb-ca64-4615-9515-13d34807857c`）
5. ~~確認訓練完成狀態~~ 已完成（2026-07-31，`action='status'` 確認 `status: ready`、`raw_status: completed`）
6. 現在可用 `model: soul_2` + 此 soul_id 生成正式發布內容
7. 影片生成流程（模型選擇、prompt 模板、剪輯節奏對應）待圖片流程確認後另行規劃，目前尚未展開
8. 若未來新增「詹師傅工班現場」「客戶現場勘查」「巷口麵館」「永和爸媽家」等 `content_style.md` / `character.md` 已提及但尚無批次草稿的生活主題場景，其光線配方應套用本檔案「光線配方二：戶外／工作現場」，而非批次 1–5 的室內奢華配方

---

## 2026-08-05 競品對標實測批次（Sherry 打法驗證，7 位台灣籍角色各 2 張）

> **批次目的**：驗證從競品 @sherry_digitalp510 拆解出的三項新做法能否用純生成複製——(1) 公共場景加入背景路人、(2) 同穿搭一日敘事串聯兩張、(3) 地點寫成環境元素清單。完整拆解見 `COMPETITOR_sherry_digitalp510.md`，規則已寫入 `SEXY_SCENE_LIBRARY.md` 第 9／11／12 點。
>
> **平台／模型**：Higgsfield `soul_2` + 本角色 `soul_id`，quality 2k，aspect_ratio 3:4
> **成本**：全批 14 張約 8 credits
> **使用者決定**：本批次**不重新生成**，spec 落差記錄在案，留待後續處理

### 本角色結果

| 項目 | 內容 |
|---|---|
| Soul ID | `192562bb-ca64-4615-9515-13d34807857c` |
| 場景 | 精品百貨（露臺咖啡／中庭行走） |
| 穿搭（A/B 共用） | 象牙白寬版喀什米爾針織 + 駝色寬口褲 + 米色結構托特 + 細金手鐲 + 墨鏡（A 置於桌上／B 拿在手中） |
| Job ID（A） | `06bcbbe1-d402-4f9c-b52e-eb9cda88d1e8` |
| Job ID（B） | `281dadc5-3603-401c-9d3f-a24106de5028` |
| 評定 | ✅ 通過（本批最佳） |

幾乎無破綻。低盤髮髻、暖栗棕髮色、柔和圓潤臉型與左眼尾小痣等 2026-07-30 重新設計的辨識特徵全部穩定呈現，與 Rainie 的區隔明確。B 張背景 5 位以上路人（西裝男、女性顧客、店員）全部背向或側臉、失焦，處理得非常自然。同穿搭延續 + 墨鏡位置變化成功。**唯一落差**：點名「台北 101」但生成為通用摩天樓群（同規則 11）。

### 本批次共同結論（全 7 位角色適用）

- ✅ **背景路人：14/14 全部成功，且無任何配角撞臉主角。** 四條件措辭（背向／不看鏡頭／失焦／外型與主角區隔）有效，成本為零。原「預設只有本人入鏡」規則對公共場景已反轉。
- ✅ **同穿搭一日敘事：7/7 成功。** 服裝配件完整延續且狀態自然演變。
- ⚠️ **地點：環境元素清單成功，點名地標全部失敗。** 「愛河」生出墨爾本天際線、「台北 101」生出通用摩天樓群。
- ⚠️ **中文招牌全部亂碼**（與競品同等程度），本批次接受此取捨。
- 🔴 **打光尚未套用新公式。** 本批次仍使用舊的「品質形容詞」寫法（`crisp`／`high dynamic range`／`well-exposed`）。2026-08-05 拆解競品後已改寫 `SEXY_SCENE_LIBRARY.md` 第 3 點為五段式物理光線公式，**下一批次應以驗證該公式為首要目標**。

---

## 2026-08-07 R8 舞蹈克隆完整跑完 Step 1–8（動作驅動複製法 Method B）

**背景**：舞蹈批次分配（見 `DANCE_CLONE_SOP.md` 大量選片 SOP、GitHub Issue #3）R8 分配給 Sophia Tseng。驅動片：`https://www.instagram.com/reel/DVnFmlVEcre/`（白色長袖 crop top + 黑色運動褲手勢舞，越南街頭夜景）。

### Step 1–2：下載與裁剪

- `yt-dlp` 下載，1080×1920、VP9 編碼、~14.1s，含原始配樂（aac）
- 內容目視核對：白色高領/字母印花長袖 crop top + 黑色寬鬆抽繩運動褲，越南街頭夜景（機車併排停放、店面招牌、掛燈裝飾樹、越南國旗），單鏡頭手持跟拍，一連串嘟嘴/吐舌/比YA等手勢舞動作，符合分配描述
- 依 `DANCE_CLONE_SOP.md` Step 2 已知風險（VP9 原始編碼直接餵給 Motion Control 會反覆失敗且無錯誤訊息），先確認並轉存為 H.264
- 原始畫面右側帶完整 CapCut 編輯 App 圖示工具列（電量/播放/文字/貼圖/特效/濾鏡/展開箭頭），用 `ffmpeg crop` 裁掉右側 100px 圖示欄（1080→980），並微調裁掉頂部/底部合計 50px（1920→1870），確認未裁到任何手勢動作，輸出 `driver_cropped.mp4`（980×1870、h264、30fps、~14.1s）
- 音軌另存 `driver_audio.m4a`（aac、44.1kHz、雙聲道、~14.1s）

### Step 3：Performance Sheet + Emotion Timeline

呼叫 `performance-director` 與 `emotion-director` agent。重點結論：

- **情緒設計**：驅動片本身表情強度（嘟嘴、吐舌、大笑張嘴）比 Sophia 預設的「沉靜、篤定、克制的性感」基調誇張許多，與 Luna Tanaka R1、Rainie Hsu R5 遇到的落差是同一類型
- **次級動態載體**：crop top 為貼身剪裁，主要動態載體是及肩 bob 短髮甩動
- **`scene_control` 選用 `image`**：不借用驅動片真實越南街頭場景（機車車牌、招牌可能無法清理），改用 Sophia 自己生成的場景

### Step 4：起始畫面（Start Frame）

- 模型：`soul_2` + `soul_id: 192562bb-ca64-4615-9515-13d34807857c`
- **第一次生成被打回**：`start_frame_v1_rejected_wrong_pants.png` 生成出深 U 領露胸口版本上衣 + 直筒西裝褲，跟分配描述「白色長袖 crop top + 黑色運動褲」不符，打回重生成
- **第二次生成核准**：`start_frame.png` 改為高領字母印花 crop top + 黑色寬鬆抽繩運動褲，場景為越南夜間街景（掛燈裝飾樹、店面暖光、越南國旗），符合分配描述，核准進入 Step 5

### Step 5：Motion Control

- 驅動片 `driver_cropped.mp4` 上傳確認，`media_id: 1546f4fa-12f0-4870-880d-a9b0b2176e09`
- `image_id`: `825d358e-53bf-4ccb-b37d-2b1e951fb328`（起始畫面 job，直接沿用不需重新上傳）
- `scene_control`: `image`（Sophia 自己生成的越南街景），`resolution`: `1080p`
- 輸出：`1072×1936`、30fps、~14.1s，Job ID `a9be7ac6-dbb6-400a-b0e0-5315e3185142`
- **輸出本身無聲**（`ffprobe` 確認只有一條 h264 視訊流），需要 Step 6 手動混音

### Step 6：手動混音

用 `ffmpeg -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` 把 Step 2 抽出的 `driver_audio.m4a`（驅動片原始配樂，裁剪起點對齊 0s，trim 至 14.07s 貼合生成畫面）蓋上 Kling 輸出的無聲畫面，輸出 `sophia_dance_clone_r8_ig_reel.mp4`（1072×1936、30fps、~14.07s，含視訊+音訊雙軌，已用 `ffprobe` 確認）。

### Step 7：授權與發佈限制檢查

- **驅動動作**：來自第三方 Instagram 創作者，本次生成僅供內部方法驗證；若要對外發佈，需評估重現程度是否需要致敬標註或改編到不可辨識
- **配樂**：混音使用的是驅動片原始配樂，**未取得商用授權**，正式發佈前必須替換為已授權/可商用曲庫版本，並重新對拍
- **背景**：`scene_control` 選用 `image`，未借用驅動片真實越南街頭背景，不涉及第三方場景可辨識性問題；但生成場景中出現越南國旗（通用國家象徵，非特定品牌/地標），對外發佈前建議留意是否需要調整
- **素材存放**：驅動片原始檔（`driver_raw.mp4`、`driver_cropped.mp4`、`driver_audio.m4a` 原始複本）僅存在本機工作資料夾，未存入本 repo

### Step 8：QA 檢核（已用 Read 工具目視抽幀比對，非假設）

抽樣 0.5s / 2.0s / 4.0s / 6.0s / 6.5s / 8.0s / 8.3s / 10.0s / 10.4s / 12.0s / 12.5s / 13.0s / 13.9s 共 13 個時間點：

- [x] **身分一致**：全程可清楚辨認黑棕短 bob、五官輪廓，跟起始畫面的錨定身分一致，多個抽樣幀交叉比對未觀察到臉型結構漂移
- [x] **微表情有變化**：抽樣幀之間表情、嘴型、眼神角度皆不同（嘟嘴 → 開口說話 → 大笑吐舌 → 比YA燦笑 → 收尾微笑），不是同一張臉套多個手勢的面具臉
- [x] **手部整體無明顯崩壞**（13 幀抽樣檢視未發現手指數量/形狀異常，含 10.4s 比YA手勢與運動模糊幀）
- [x] **背景穩定**：越南街景（掛燈裝飾樹、店面暖光、越南國旗、機車）全程一致，無鬼影閃爍
- [x] **規格**：1072×1936（超過 1080×1920 門檻）、30fps、音樂已對齊長度
- [ ] **表情強度與人設基調落差（已知限制，非本輪 QA 阻斷項）**：驅動片原始的嘟嘴/吐舌/大笑表情比 Sophia「沉靜克制」人設基調誇張許多。**使用者已審閱並明確決定維持原始表情強度**——理由是舞蹈類內容本身表情即是表演的一部分，誇張表情比刻意收斂更生動，不列入本輪合格/不合格判定
- [ ] **無確認的定格/freeze 點**：本次沒有針對逐幀定格做另外驗證，留待下次需要更嚴謹驗證時補做

**結論**：Step 4 起始畫面第一次生成因服裝款式不符被打回，第二次生成核准後 Step 5–8 一次到位。QA 檢核的身分一致性/手部/次級動態/背景穩定項目全數通過。表情強度與人設基調的落差經使用者審閱後**明確決定保留**，記錄為使用者核准的設計選擇，不是待修正的缺陷。

### 產出檔案

- `kols/sophia-tseng/images/dance_clone_r8/start_frame.png`（已核准起始畫面，第二次生成版本）
- `kols/sophia-tseng/images/dance_clone_r8/start_frame_v1_rejected_wrong_pants.png`（第一次生成，服裝不符分配描述，僅供對照）
- `kols/sophia-tseng/videos/dance_clone_r8/sophia_dance_clone_r8_ig_reel.mp4`（1072×1936、30fps、~14.07s，含驅動片原始配樂音軌，未經授權，僅供內部驗證）

---

## 2026-08-07～08-08 R9 舞蹈克隆完整跑完 Step 1–8（動作驅動複製法 Method B）

**背景**：舞蹈批次分配（見 `DANCE_CLONE_SOP.md`、GitHub Issue #3 2026-08-07 補充4）R9 分配給 Sophia Tseng。驅動片：`https://www.instagram.com/reel/DB2yTeEv7LG/`（奶油色皺褶蝴蝶結緞面比基尼、居家手勢/身體展示型動作、越南歌曲「2 Phút Hơn」remix，室內奶油色牆面+木地板+深灰沙發）。

### Step 1–2：下載與裁剪（2026-08-08 補做）

- 從 Google Drive（file ID `1CxjE-0H2nXyAH8E5QVX8REVBiS9H0Pqz`）用 `curl` 下載，876×1558、**VP9 編碼**、~8.13s，含原始配樂（aac）
- **原始畫面右側/頂部帶完整的編輯 App 介面圖示**（頂端音樂條「2 Phút Hơn」+ 返回箭頭、右側設定/裁切/比例/文字/貼圖/濾鏡/疊層/新增/展開等工具列圖示），全片固定位置疊在畫面上，判斷是螢幕錄製編輯畫面而非乾淨匯出檔——**這支跟 Sophia R8、Mia Huang R1 一樣，是需要額外裁切排除 UI 的案例**
- 用 `ffmpeg crop=786:1397:0:100` 裁掉右側工具列欄與頂部音樂條/返回箭頭，目視確認裁切後畫面完全無 UI 殘留、且未裁到手勢動作範圍；底部另外抽樣確認乾淨（僅為腿部+地板，無 UI）
- 依 `DANCE_CLONE_SOP.md` Step 2 已知風險（VP9 原始編碼直接餵給 Motion Control 會反覆失敗且無錯誤訊息），已用 `-c:v libx264 -pix_fmt yuv420p` 重新編碼，輸出 `driver_cropped.mp4`（786×1396、h264、~8.12s，已用 `ffprobe` 確認編碼）
- 音軌另存 `driver_audio.m4a`（aac、~8.13s）
- 內容目視核對：奶油色皺褶蝴蝶結緞面比基尼、居家手勢/身體展示型動作，符合分配描述

### Step 3：Performance Sheet + Emotion Timeline（2026-08-08，`performance-director` + `emotion-director` agent）

呼叫兩個 agent（依 1 秒取樣的文字時間軸描述）。重點結論：

- **次級動態載體**：Step 4 已核准的絲質敞開罩衫外袍（寬版垂墜袖）+ 中長 bob 髮型。**罩衫及踝長裾的下半段在 mid-thigh up 裁切框外**，次級動態的可讀性要靠肩到大腿中段這一段的開襟角度變化，不依賴裙擺甩動——這是可接受的取捨，QA 時不要誤判
- **不對稱錨點（Sophia 目前沒有既有的動態不對稱設計，這次新建）**：比照 Coco Wu 案例，訂為「右嘴角先動、左嘴角慢半拍到位」+「右眉為主要動作眉」+「頭傾方向預設偏她的右側」；4.0s 情緒峰值與 8.0s 收尾這兩處允許趨近對稱（情緒真正外露時放鬆規則）
- **識別痣呈現（左眼尾下方小痣）**：0.0–1.9s、5.0–7.5s 正面直視是最清楚的窗口；2.0–2.9s 闔眼頭傾方向須偏右（不能偏左，否則左頰壓縮遮痣）；4.0s 撥髮動作的髮絲收尾方向須落向右肩，避免掃過左頰；8.0s 頭傾角度須控制在 15–20 度內、維持接近正面
- **面具臉風險（5.0–7.0s 三個連續「抿嘴微笑+直視鏡頭」姿勢）**：已設計專屬區隔訊號避免雷同——6.0s 有 6.3s 視線短暫飄移再收回，7.0s 有 7.2s 偏慢眨眼 + 7.5s 嘴角微露齒縫，5.0s 與其餘兩秒都不重複
- **`scene_control` 選用 `image`**：延續 Step 4 決定，保留 Sophia 自己生成的信義區公寓場景，不借用驅動片場景
- **阻斷級風險 — 4.0s 表演強度需使用者裁決（詳見下方「待裁決事項」）**：驅動片原始是「雙手舉高撥髮+張嘴大笑+身體明顯晃動」，跟 Sophia「沉靜克制」人設基調落差最大的一拍，兩位 agent 都判定不應該逕行決定，需要使用者選擇比照 R8 保留原強度、或收斂為「輕笑瞇眼」版本
- **條件式阻斷（生成後 QA 留意，不阻擋 Step 5）**：4.0s 雙手快速甩動時檢查手指/寬袖是否崩壞；細肩帶低胸剪裁在晃動下檢查肩帶是否滑落跑位；5.0–7.0s 凍結段要加密抽樣（5.0/5.5/6.0/6.5/7.0）確認外袍/頭髮持續有微幅飄動，避免被判定「同步靜止」失敗

完整 Performance Sheet 與 Emotion Timeline（含逐秒時間軸、眼神腳本、可直接貼入 prompt 的文字片段）存於本次 session 記錄，未來需要時可重新呼叫兩個 agent 依同一份驅動片時間軸重建。

### 待裁決事項（Step 5 前必須有結論）：4.0s 表演強度

驅動片原始：雙手舉高撥髮、**張嘴大笑**、身體明顯晃動（全片動態模糊最重的一刻，唯一的高能拍點）。

- **方案 A（比照 R8 先例，保留原始強度）**：張嘴大笑、露齒，跟驅動片 1:1 轉印。優點是動作驅動法的真實物理感完整保留、記憶點最強；缺點是與 Sophia 人設基調落差最大
- **方案 B（agent 建議方案，收斂為 Sophia 天花板內的版本）**：改為「帶氣音的短促輕笑（breathy huff-laugh）」，嘴唇微張但不露滿口牙齒，改用眼尾瞇起/自然笑紋傳達情緒（全片唯一允許眼睛因笑意變形的時刻）。優點是全片情緒天花板一致、更貼合人設；缺點是視覺記憶點的爆發力較弱，且 Motion Control 工具沒有直接的「降低動態幅度」參數，若要收斂需在後製或重新調整 prompt 措辭上額外處理

肢體骨架（雙手舉高撥髮）兩案都不變，差別只在臉部表情強度。

**使用者裁決（2026-08-08）：採方案 A，保留原始強度**——張嘴大笑、身體晃動照原始骨架與情緒強度轉印，不收斂。跟 R8 同一類決策模式，記錄為使用者核准的設計選擇。生成後仍要照 Step 3 標記的條件式阻斷項檢查 4.0s 手指/寬袖是否崩壞。

### Step 4：起始畫面

- 模型：`soul_2` + `soul_id: 192562bb-ca64-4615-9515-13d34807857c`
- **服裝刻意調整,不是照抄驅動片**：驅動片原始服裝是貼身緞面蝴蝶結比基尼，但 Sophia 人設明確列出「不出現：貼身緊繃的 bodycon，她的性感是寬鬆剪裁與垂墜感」，直接照抄會踩到這條硬性邊界；且比基尼本身沒有任何會動的元素。改為**絲質細肩帶連身居家套裝 + 同色系寬鬆罩衫外袍**（罩衫敞開垂墜作為次級動態載體），保留原片奶油色調與居家調性
- 場景選她「居家 / 信義區公寓」pillar 的落地窗城市夜景，符合她慣用的 ivory/champagne 低對比色調
- **第一次生成**：`start_frame.png`，五官/身材與 soul_id 錨定一致，服裝符合上述調整方向，場景/光線/表情皆貼合人設。**已核准**（使用者確認左眼尾小痣辨識度清楚、服裝調整方向可接受，2026-08-08 再次向使用者確認核准狀態時複核一致）
- Job ID：`1b43fa58-1900-4b52-87aa-9e99eb14993f`

### Step 5：Motion Control（2026-08-08 完成）

- 驅動片 `driver_cropped.mp4` 上傳確認，`media_id: f91e0b92-21e1-4779-bb14-80491b7c9565`
- `image_id`: `1b43fa58-1900-4b52-87aa-9e99eb14993f`（Step 4 起始畫面 job，直接沿用不需重新上傳）
- `scene_control`: `image`（Sophia 自己生成的信義區公寓落地窗場景），`resolution`: `1080p`
- 輸出：`1072×1936`、30fps、~8.1s，Job ID `dc913bfb-ba8e-45c7-b7e7-795f63c41a0b`
- **輸出本身無聲**（`ffprobe` 確認只有一條 h264 視訊流，同 R8），需要 Step 6 手動混音

### Step 6：手動混音

用 `ffmpeg -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` 把 Step 2 抽出的 `driver_audio.m4a`（驅動片原始配樂「2 Phút Hơn」remix，未裁切偏移，起點對齊 0s）蓋上 Kling 輸出的無聲畫面，輸出 `sophia_dance_clone_r9_ig_reel.mp4`（1072×1936、30fps、~8.1s，含視訊+音訊雙軌，已用 `ffprobe` 確認）。

### Step 7：授權與發佈限制檢查

- **驅動動作**：來自第三方 Instagram 創作者（shortcode `DB2yTeEv7LG`），本次生成僅供內部方法驗證；若要對外發佈，需評估重現程度是否需要致敬標註或改編到不可辨識
- **配樂**：混音使用的是驅動片原始配樂（越南歌曲「2 Phút Hơn」remix），**未取得商用授權**，正式發佈前必須替換為已授權/可商用曲庫版本，並重新對拍
- **背景**：`scene_control` 選用 `image`，未借用驅動片真實居家背景，不涉及第三方場景可辨識性問題
- **素材存放**：驅動片原始檔（`driver_raw.mp4`、`driver_cropped.mp4`、`driver_audio.m4a`）僅存在本機工作資料夾，未存入本 repo

### Step 8：QA 檢核（已用 Read 工具目視抽幀比對，非假設）

抽樣 0.5s / 2.0s / 3.0s / 4.0s / 4.05s / 4.15s / 4.3s / 5.0s / 6.0s / 7.0s / 7.2s / 8.0s 共 12 個時間點：

- [x] **身分一致**：全程可清楚辨認短棕 bob、五官輪廓，跟起始畫面的錨定身分一致，多個抽樣幀交叉比對未觀察到臉型結構漂移
- [x] **微表情有變化，通過面具臉檢查**：5.0s（抿嘴+手扶鎖骨）、6.0s（自信抿笑+側身）、7.0s（笑容加深+露齒）三個原本風險最高的連續姿勢，實際抽幀確認頭部角度、嘴型開合度、眼神焦點皆有可辨識差異，不是同一張臉套三個手勢
- [x] **次級動態載體有效**：敞開罩衫外袍的寬版垂墜袖在 4.0s 高動態時刻有明顯的甩動/飄動殘影，頭髮也隨動作自然擺動，5–7s 相對靜止段落外袍下緣仍有隨呼吸的微幅飄動，未觀察到「同步靜止」
- [x] **手部整體無明顯崩壞**（4.0s/4.05s/4.15s 雙手同時舉高撥髮的高風險動作，2.0s 雙手交疊繫帶動作，抽樣檢視皆未發現手指數量/形狀異常）
- [x] **肩帶穩定性**：4.0s 身體晃動下細肩帶未見滑落或版型跑位，剪裁維持穩定
- [x] **背景穩定**：信義區公寓落地窗城市夜景全程一致，無鬼影閃爍，未出現驅動片場景殘留
- [x] **規格**：1072×1936、30fps、音樂已對齊長度（~8.1s）
- [x] **表演強度**：4.0s 張嘴大笑+身體晃動維持驅動片原始強度，符合使用者方案 A 裁決

**結論**：Step 1–8 一次到位，未發生像 R8 那樣需要重生成的環節。QA 檢核全數通過，包含 Performance Sheet／Emotion Timeline 事前標記的高風險項目（4.0s 手部/寬袖崩壞、5–7s 次級動態不足、面具臉風險）皆未在實際生成結果中出現。表演強度依使用者裁決採方案 A（保留原始強度），與 R8 同一類決策模式。

### 產出檔案

- `kols/sophia-tseng/images/dance_clone_r9/start_frame.png`（已核准起始畫面）
- `kols/sophia-tseng/videos/dance_clone_r9/sophia_dance_clone_r9_ig_reel.mp4`（1072×1936、30fps、~8.1s，含驅動片原始配樂音軌，未經授權，僅供內部驗證）
- 本機工作資料夾（未進 git）：`driver_raw.mp4`（VP9 原始檔）、`driver_cropped.mp4`（786×1396、H.264、~8.12s，已去除編輯 App UI）、`driver_audio.m4a`（原始配樂音軌）

---

## 2026-08-08 R11 舞蹈克隆 — Step 1–3 完成，Step 4 待生成

**背景**：舞蹈批次分配（見 `DANCE_CLONE_SOP.md`、GitHub Issue #3 2026-08-07 補充4）R11 分配給 Sophia Tseng（原
luna-tanaka，因 Luna 害羞人設跟這支的自信眼神落差大改分配）。驅動片：IG shortcode `DHI2Xhvr1b`（深藍三角
比基尼上衣+寬鬆灰色運動長褲「PEACE LOVE」腰間鬆緊帶+頭頂墨鏡，米白素色牆面/更衣室場景）。

### Step 1–2：下載與裁剪

- 從 Google Drive（file ID `1ChRPXiz-G3sJrN_xYGp4KgPqAMKOIxUo`）用 `curl` 下載，760×1352、VP9 編碼、~9.5s，
  含原始配樂（aac）
- 內容目視核對：深藍三角比基尼上衣+寬鬆運動長褲+頭頂墨鏡，胸上到大腿三分身取景，單鏡頭固定站姿，全片
  重複「雙臂胸前交叉/放下」的手勢動作，符合分配描述
- 原始畫面右側/左側邊緣殘留社群 App 圖示（faint 白色圖示輪廓+左側一個深色小方塊圖示），用
  `ffmpeg crop=660:1352:38:0` 裁掉兩側邊緣後確認無殘留、未裁到手部動作範圍
- 轉 H.264（VP9→H.264 已知風險），輸出 `driver_cropped.mp4`（660×1352、~9.5s）；音軌另存 `driver_audio.m4a`

### Step 3：Performance Sheet + Emotion Timeline（`performance-director` + `emotion-director` agent）

呼叫兩個 agent。**這支驅動片是目前處理過的案例裡風險評級最高的一支**，重點結論：

- **核心問題（阻斷級提醒，跟 R9/R10 性質不同）**：驅動片 0.5s–5.3s 將近 4.8 秒維持同一個「自信抿笑、
  直視鏡頭」狀態，全片只有 5.5s、7.5s 兩個微小變化點，是目前 Sophia 系列裡表情密度最低的一支。這**不是
  R8/R9 那種「要不要收斂驅動片本身已有的表情強度」的裁決問題**，而是「驅動片根本沒有表情素材可以轉印」
  ——兩位 agent 都不建議換驅動片（動作本身是好的記憶點，取景/裁法也對），但要求 emotion-director **主動
  設計一套完全獨立於手勢動作之外的微表情演變**（呼吸/眨眼/嘴角不對稱時序/眼神焦點轉移），寫死在 prompt
  裡，不能指望驅動片提供
- **管線層級疑慮（Step 5 生成後第一優先驗證項目）**：Motion Control 慣例上會把驅動片的臉部動態一併轉印，
  這支驅動片臉部動態趨近於零，**如果生成結果臉部完全跟著驅動片靜止、prompt 設計的表情演變沒有落地，
  這是阻斷級失敗**，不能當成「驅動片本來就這樣」接受——這點明確不同於 R9（驅動片本身表情有自然變化，
  只是三段相似）
- **次級動態載體**：比基尼上衣+運動長褲在三分身取景內幾乎沒有可視擺動元素（褲管飄動範圍在框外），
  建議加一件敞開輕薄罩衫/開襟外套披肩（不套袖），前襟隨手臂交叉/打開動作有 3-5 幀延遲的擺盪與歸位——
  動作與載體天然搭配（交叉手勢本身就會帶動敞開外套前襟），不是硬加的元素
- **場景與敘事定位**：建議定位在 Pilates/健身工作室的更衣室或訓練前後片刻（呼應她既有「健身/Pilates」
  支柱：安靜的自律，訓練後妝髮依然完整，沒有狼狽感），把交叉手臂動作的動機重新詮釋為「確認外套穿法/
  垂墜感」而非「對鏡頭展示身材」，肢體骨架完全不變，只調整表情背後的意圖設定
- **情緒基調**：「度假鬆弛,但骨子裡還是她」——不用更興奮的表情補償更隨性的穿著(這是最容易讀成刻意耍帥
  的錯誤路徑),表情強度維持克制天花板,篤定的內容從「我知道我很美」換成「我知道這樣穿很舒服」
- **不對稱識別錨點**：沿用 R9「右嘴角先動、左嘴角慢半拍」+「右眉為主要動作眉」+「頭傾偏右」，新增規則：
  **長靜止段落（0–5.3s）右嘴角要維持比左側多 1-2% 的靜態張力**，不能兩側完全放鬆對稱，避免長段落出現
  完全對稱的定格臉
- **QA 密度要求**：0.0–5.3s 高風險窗口建議每 0.5s 抽一幀（約 10-11 個樣本），比 R9 的抽樣密度更高，逐一
  比對嘴角曲度差/眼睛開闔度/頭傾角度/呼吸起伏是否真的有變化
- **框取後製建議**：三分身取景無法在單次生成內切換到臉部特寫，建議成品完成後在 6.5s（雙臂放下全身展示）
  與 9.2s（收尾）兩個天然停頓點做後製 punch-in 到腰上特寫，零額外生成成本
- **`scene_control` 選用 `image`**：保留 Sophia 自己生成的場景，不借用驅動片素色牆面

### Step 4：起始畫面（已生成，等待使用者核准）

- 模型：`soul_2` + `soul_id: 192562bb-ca64-4615-9515-13d34807857c`，Job ID `373611e0-8ec0-4d72-927e-16850e1221c7`
- 場景：Pilates 工作室更衣室（reformer 器材、木質長椅、折疊毛巾），符合 Step 3 建議的敘事定位
- 服裝：深藍三角運動內衣+寬鬆灰色抽繩運動長褲+敞開米色針織罩衫（不套袖，垂墜在肩上）+頭頂墨鏡，
  低盤髮髻+幾縷碎髮，符合 Sophia 髮型規則（不留長髮披肩）
- 依 `DANCE_CLONE_SOP.md` 人工核准關卡規則，生成後停在這裡等使用者核准——**已核准**

### Step 5：Motion Control

- 驅動片 `driver_cropped.mp4` 上傳確認，`media_id: 6cb35f79-d20a-4bf8-8832-8e1c10351761`
- `image_id`: `373611e0-8ec0-4d72-927e-16850e1221c7`，`scene_control: image`，`resolution: 1080p`
- Job ID `17112f32-bb28-413e-a31b-98ed0217b9c8`，`status: completed`（一次通過，無審核問題）
- 輸出：`1072×1936`、30fps、~9.5s
- **輸出本身無聲**（`ffprobe` 確認只有一條 h264 視訊流），需要 Step 6 手動混音

### Step 6：手動混音

用 `ffmpeg -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` 把 Step 2 抽出的 `driver_audio.m4a`
（驅動片原始配樂，起點對齊 0s）蓋上 Kling 輸出的無聲畫面，輸出 `sophia_dance_clone_r11_ig_reel.mp4`
（1072×1936、30fps、~9.5s，含視訊+音訊雙軌，已用 `ffprobe` 確認）。

### Step 7：授權與發佈限制檢查

- **驅動動作**：來自第三方上傳素材，本次生成僅供內部方法驗證；若要對外發佈，需評估重現程度是否需要
  致敬標註或改編到不可辨識
- **配樂**：混音使用的是驅動片原始配樂，**未取得商用授權**，正式發佈前必須替換為已授權/可商用曲庫版本，
  並重新對拍
- **背景**：`scene_control` 選用 `image`，未借用驅動片真實背景，不涉及第三方場景可辨識性問題
- **素材存放**：驅動片原始檔僅存在本機工作資料夾，未存入本 repo

### Step 8：QA 檢核（已用 Read 工具目視抽幀比對，非假設）

依 Emotion Timeline 建議的高密度抽樣，於 0.0–5.5s 每 0.5s 抽一幀，加上 6.5s/7.5s/9.2s，共 17 個時間點：

- [x] **身分一致**：全程可清楚辨認低盤髮髻+碎髮、五官輪廓，跟起始畫面的錨定身分一致
- [x] **面具臉風險未成真，優於預期**：儘管驅動片本身表情近乎靜止，實際生成結果在 0.0s/1.5s/3.0s/4.5s/
  5.5s/6.5s/7.5s/9.2s 之間仍可觀察到清楚的表情漸進變化（從內斂沉靜到更開朗的微笑），未出現 Performance/
  Emotion Sheet 事前擔心的「驅動片臉部通道蓋過獨立表情設計」的阻斷級失敗
- [x] **次級動態載體有效**：敞開米色針織罩衫在多個抽樣幀可見明顯的垂墜/披掛角度變化，尤其手臂交叉/放下
  的轉換時刻，未觀察到「同步靜止」
- [x] **手部整體無明顯崩壞**：雙臂交叉/放下的重複動作抽樣檢視未發現手指數量/形狀異常
- [x] **背景穩定**：Pilates 工作室場景（reformer 器材、窗景、毛巾）全程一致，無鬼影閃爍
- [x] **規格**：1072×1936、30fps、音樂已對齊長度（~9.5s）

**結論**：Step 1–8 一次到位，未發生像 R8/R10 那樣需要重生成的環節。這支驅動片事前評估的面具臉風險
（目前處理過的案例裡最高）在實際生成結果中沒有成真，QA 檢核全數通過。

### 產出檔案

- `kols/sophia-tseng/images/dance_clone_r11/start_frame.png`（已核准起始畫面）
- `kols/sophia-tseng/videos/dance_clone_r11/sophia_dance_clone_r11_ig_reel.mp4`（1072×1936、30fps、~9.5s，
  含驅動片原始配樂音軌，未經授權，僅供內部驗證）
