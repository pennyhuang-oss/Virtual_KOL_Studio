# Virtual KOL Studio — 人格訓練 SOP

> 每次換裝置或開新 session 時，請讓 Claude 讀取這份文件，它會知道完整的執行方式與注意事項。

---

## 目前進度總覽

### 原始 6 位

| KOL | Soul ID | Soul 訓練 | 測試圖 | 自介素材 | 狀態 |
|-----|---------|----------|--------|---------|------|
| Iris Chen | `5fe3b6ba-1277-4822-9141-fb06eb3b93a0` | ✅ | ✅ 14 張 | ✅ 影片 v3 通過；舞蹈影片 v1-v3 通過 | ✅ 完成 |
| Luna Tanaka | `1bfab2ce-cfa5-4026-93fa-e5c91b469c7a` | ✅ | ✅ 6 張 | ❌ 待生成 | 🔄 進行中 |
| Ananya Kapoor | `fac82296-8c69-4c34-b352-1b398c8b8e1c` | ✅ | ✅ 6 張（場景 1+3 已重生成） | ❌ 待生成 | 🔄 進行中 |
| Yuna Kim | `235794a5-2eff-45fb-91b4-3232910afefa` | ✅ | ✅ 6 張 | ❌ 待生成 | 🔄 進行中 |
| Aaliya Rivera | `97f5c6cd-1c0c-4432-83d0-dd42210ecada` | ✅ | ✅ 8 張 | ❌ 待生成 | 🔄 進行中 |
| Camille Dupont | `f19dafcc-5bc8-4d8f-af1d-ee48084ac398` | ✅ | ✅ 12 張 | ✅ 4 張通過 | ✅ 完成（影片素材待生成）|

訓練順序：Ananya Kapoor → Yuna Kim → Aaliya Rivera → Camille Dupont

### 新增 6 位（2026-07-24，台灣籍）

| KOL | Soul ID | Soul 訓練 | 測試圖 | 狀態 |
|-----|---------|----------|--------|------|
| Vicky Lin | `bdb1d879-da36-4c1a-bc63-9f5b49a3e94e`（`status: training/queued`，2026-07-31 第三次重試成功受理，尚未回傳 ready） | 🔄 進行中 | ✅ 12 張（第四輪 `v4_anchored_01`–`12`，Element 錨定身分一致，使用者已核准；第一～三輪僅供對照） | 🔄 前兩次 session 累計 12 次呼叫失敗後，2026-07-31 使用者要求重試，改用先前已確認的 media_id，第一次呼叫即成功受理，判斷後端 `train` 端點異常已恢復；待確認訓練完成狀態，詳見 `kols/vicky-lin/generation_notes.md` |
| Coco Wu | `cf7045dc-4e69-4c56-9621-aa8c40bf39b4`（`status: ready`，訓練完成） | ✅ 完成 | ✅ 12 張（Reference Element `4b6c659c-786b-43de-87af-87cea3cc99dd` 錨定，`training_v1/`） | ✅ 2026-07-31 確認訓練完成，`show_characters(action='train')` 回傳的 `items` 列表確認 `raw_status: completed`；可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/coco-wu/generation_notes.md` |
| Rainie Hsu | `994e33d2-7df1-47da-8478-7a6fd849fa33`（`status: ready`，訓練完成） | ✅ 完成 | ✅ 13 張（Reference Element `ae0d8287-af47-4f9d-b357-19a477abd00d` 錨定，`training_v1/`） | ✅ 2026-07-30 訓練完成，`show_characters(action='status')` 確認 `raw_status: completed`；可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/rainie-hsu/generation_notes.md` |
| Sophia Tseng | `192562bb-ca64-4615-9515-13d34807857c`（`status: ready`，訓練完成） | ✅ 完成 | ✅ 13 張（Reference Element `980f8414-7709-47ff-9c88-fdc30b54d03d` 錨定，第三輪五官重新設計後的身分，`training_v1/`） | ✅ 2026-07-31 確認訓練完成，`show_characters(action='status')` 確認 `raw_status: completed`；可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/sophia-tseng/generation_notes.md` |
| Mia Huang | `e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4`（`status: ready`，訓練完成） | ✅ 完成 | ✅ 13 張（Reference Element `92ffbd80-32c7-495f-91ed-f109b419bb41` 錨定，`training_v1/`） | ✅ 2026-07-30 訓練完成，可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/mia-huang/generation_notes.md` |
| Zoe Lai | `27f750e6-0d32-43ce-8249-cce94ef835cd`（`status: ready`，訓練完成） | ✅ 完成 | ✅ 13 張（Reference Element `9b1c0c4b-7301-4144-9427-56e754178144` 錨定，`training_v1/`） | ✅ 2026-07-30 訓練完成，`show_characters(action='status')` 確認 `raw_status: completed`；可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/zoe-lai/generation_notes.md` |

> ✅ 截至 2026-07-31，這 6 位中已有 5 位（Coco Wu、Rainie Hsu、Sophia Tseng、Mia Huang、Zoe Lai）完成 Reference Element 錨定訓練圖批次並成功完成 Soul 訓練（`status: ready`），可用 `model: soul_2` + 各自 soul_id 生成正式內容。Vicky Lin 先前累計兩次 session、12 次呼叫皆為工具層級失敗，2026-07-31 重試後第一次呼叫即成功受理（`soul_id: bdb1d879-da36-4c1a-bc63-9f5b49a3e94e`），目前 `status: training/queued`，待確認完成。

---

## ⚡ 新 Session 啟動時，立刻做這件事

> 讀完這份文件後，直接照以下清單執行，不用等使用者再說明。

### 現在的待辦（依優先順序）

> 最後更新：2026-07-24

0. **⚠️ 強制規則（2026-07-24 新增，優先於以下所有事項）**：任何 KOL 生成臉部參考圖後，**必須停下來等使用者實際看過並明確確認滿意，才可以送進 Soul 訓練**——不可以在同一輪自動接著做完。這是因為 Vicky Lin 第一輪試跑沒有這個關卡，結果生成方向錯了才發現，浪費了生成額度。詳見 README.md「新增 KOL 流程」步驟 6，以及 `.claude/workflows/kol_content_qa_pipeline.js` 的審核流程。

1. **Vicky Lin — 重新生成臉部參考圖**
   - 外型描述已修正（見 `character.md`/`profile.json`/`generation_notes.md` 的 2026-07-24 修正記錄）：核心是「漂亮性感健身網紅」，明確禁止健美選手/男性化方向
   - 生成後停下來，等使用者確認滿意才能繼續（見上方第 0 點）

2. **Coco Wu / Rainie Hsu / Sophia Tseng / Mia Huang / Zoe Lai — 臉部參考圖生成**
   - 都還沒開始，人設文件都已完整，可以直接照 `generation_notes.md` 裡的規劃批次執行
   - 同樣適用第 0 點的強制確認關卡

3. **Luna Tanaka — 自我介紹素材圖生成**
   - Soul 訓練 ✅，測試圖 ✅，尚未生成自介素材（參考 Camille 的 `self_intro_v1` 流程）
   - 生成前先確認場景與穿搭，每個場景兩張，構圖必須不同

4. **Yuna Kim — 自我介紹素材圖生成**
   - Soul 訓練 ✅，測試圖 ✅（selfie、江南咖啡廳、弘大街頭各 2 張）
   - 同上流程

5. **Aaliya Rivera — 自我介紹素材圖生成**
   - Soul 訓練 ✅，測試圖 ✅（poolside、restaurant、selfie 共 8 張）
   - 同上流程

6. **Camille Dupont — 自我介紹影片素材生成**
   - 自介圖 4 張已通過，剪輯時間軸已完成，影片素材（10 個 shot）尚未生成

### 注意事項（每次生成前必讀）
- **Iris Chen 是所有 KOL 的標準範本**：她是第一個完成的人格，後續每一個 KOL 的訓練規格、文件規模、步驟流程，全部以她為基準。不確定某個步驟怎麼做、某份文件要寫到什麼程度，就去看 `kols/iris-chen/` 的結構和內容對齊。
- **生成測試圖前，必須先列出預計場景讓使用者確認**，同意後才執行
- 圖片無法從雲端 session 下載 Higgsfield CDN，需使用者先上傳到 GitHub，再由 Claude 用 `raw.githubusercontent.com` 搬到正確資料夾
- 所有 push 都在 branch：`claude/kol-personality-training-9otdaw`
- **⚠️ 素材生成必須參考 Benchmark 帳號（所有人格適用）**：
  - **圖片素材**：生成前先查閱該 KOL `character.md` 的 Benchmark 帳號，以對應帳號的圖文風格、構圖方式、身材展示角度作為 prompt 方向依據
  - **影音素材**：生成前先查閱該 KOL Benchmark 帳號發布的影片，以其拍攝方式、剪輯節奏、出場方式作為腳本/生成方向
  - 當不知道該給什麼 prompt 或腳本方向時，**優先查閱 Benchmark 帳號最近發布的內容找靈感**，讓素材風格對標這些帳號
  - 各 KOL 的 Benchmark 帳號詳見各自 `character.md` → 「社群平台 & Benchmark 帳號」章節
- **⚠️ 肢體動作多元化（所有人格適用）**：每次生成任何 KOL 的圖片，必須主動設計多元的姿勢、構圖與表情，禁止單一擺拍正面看鏡頭。規劃每張圖前先決定「這張照片的姿勢故事是什麼」，讓她在做某件事、有某種情緒，再寫 prompt。
  - 姿勢方向：看向遠方、中途動作被捕捉（撩髮/調整衣服/拿杯子）、側身或背影回眸、行走中側拍、坐姿變化（翹腳/前傾/下巴靠手）、與場景互動（靠牆/扶窗框/靠欄杆）
  - 表情方向：自然微笑、若有所思、被逗笑的瞬間感、放鬆閉眼享受
  - 構圖配合姿勢：廣角遠景時人物要有動態感；3/4 身時側身或斜角；近景時搭配表情或手部動作細節
- **⚠️ 同一場景兩張圖構圖必須不同（所有人格適用）**：同場景、同衣服、同環境，但兩張圖的景別和角度必須明顯不同（例如 3/4 身 vs 臉部近景；廣角遠景 vs 特寫；正面 vs 側面）
- **⚠️ 降低「AI 感」檢查清單（2026-07-24 新增，所有人格適用）**：送出生成前對照 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉逐項檢查（皮膚質感、裝置/鏡頭規格、混合不均勻光源、背景雜物細節、服裝完整度）；運動類角色（Vicky Lin、Zoe Lai）額外檢查是否偏向健美選手/男性化方向。有 `.claude/workflows/kol_content_qa_pipeline.js` 可以自動跑這套審核流程，不用每次手動對照。

---

## 工具與連接

- **AI 生圖平台**：Higgsfield（透過 MCP 連接）
- **MCP 連接方式**：Claude Connectors → higgs
- **GitHub repo**：`pennyhuang-oss/Virtual_KOL_Studio`
- **工作 branch**：`claude/kol-personality-training-9otdaw`
- **資料位置**：每個 KOL 的資料夾在 `kols/<kol-id>/`

---

## 完整訓練流程（每個 KOL 的標準步驟）

### 第一步：確認外型設定

1. 讀取該 KOL 的 `character.md` 和 `profile.json`
2. 確認以下欄位都清楚定義：
   - 臉型、髮型、眼睛、膚色
   - 身材（例如 Luna 是「童顏巨乳」）
   - 穿搭風格
3. 查看 `images/face_reference/` 裡的參考圖（每個 KOL 應有 4 張）

### 第二步：確認臉部參考圖

- 參考圖已放在 GitHub 各 KOL 的 `images/face_reference/` 資料夾
- GitHub raw URL 格式：
  ```
  https://raw.githubusercontent.com/pennyhuang-oss/Virtual_KOL_Studio/<commit-sha>/kols/<kol-id>/images/face_reference/ref_01.webp
  ```
- 這些 URL 可以直接被 Higgsfield MCP 讀取，不需要先下載

### 第三步：送進 Soul 訓練

呼叫 Higgsfield MCP 的 `show_characters` 工具：

```
show_characters(
  action='train',
  name='<KOL 英文名>',
  type='soul_2',
  images=[
    <ref_01 URL>,
    <ref_02 URL>,
    <ref_03 URL>,
    <ref_04 URL>,
    ... 其他補充圖（如有）
  ]
)
```

**最低需要 5 張圖**（Soul 要求 5–20 張）。如果只有 4 張臉部參考圖，需要額外補充至少 1 張。

訓練時間：約 10 分鐘。

### 第四步：確認訓練完成

```
show_characters(action='status', soul_id='<soul_id>')
```

回傳 `"status": "ready"` 即為完成。

### 第五步：生成測試圖確認成果

> ⚠️ **重要規則：訓練完成後，必須先向使用者確認場景，待使用者同意後才能開始生成。**
> 
> 確認項目：
> - 場景名稱（例如：街頭、咖啡廳、公園、海邊、室內等）
> - 穿搭描述（每個場景分別確認）
> - 角度與構圖（全身、3/4、特寫等）
>
> 確認過後再執行以下生成步驟。

訓練完成後，用 Soul ID 生成至少 6 張不同場景的測試圖，確認身份一致性：

```
generate_image(
  model='soul_2',
  soul_id='<soul_id>',
  prompt='...',
  aspect_ratio='9:16',
  count=2
)
```

建議場景：依使用者確認的場景為準（每個場景 2 張，至少 3 個場景共 6 張）。

Prompt 結構：
```
<年齡> <國籍> girl, <臉部特徵>, <身材描述>, <場景>, wearing <服裝>, <角度>, <光線>, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

用 `job_display(id='<job_id>')` 顯示結果。

### 第六步：更新文件並 push 到 GitHub

1. 更新 `character.md`：在外型欄位加上 Soul ID
2. 更新 `profile.json`：加上 `ai_generation` 欄位（soul_id、model、trained_at）
3. 新增 `generation_notes.md`：記錄 Soul ID、訓練圖來源、測試圖連結、prompt 結構
4. 將測試圖存入 `images/soul_test_v1/`
5. Commit 並 push 到 `claude/kol-personality-training-9otdaw`

---

## 已知問題與解法

### 問題 1：soul_2 模型無法鎖定臉部

**症狀**：傳入參考圖後，生成出來的臉完全不同。  
**原因**：`soul_2` 模型的參考圖只影響「風格」，不影響人臉身份。唯一能固定臉的方式是做 Soul 訓練（把臉訓練進 Soul ID 裡）。  
**正確做法**：不要在 `generate_image` 裡傳入臉部參考圖作為 medias，應該使用 `soul_id` 參數搭配已訓練好的 Soul。

---

### 問題 2：`show_characters` 只顯示列表，沒有啟動訓練 UI

**症狀**：呼叫 `show_characters(action='train', ...)` 後，只回傳現有角色列表，沒有啟動訓練。  
**原因（已解決）**：之前曾中途打斷過 `show_characters` 的呼叫，導致系統鎖住，之後的重試都被擋掉。  
**解法**：
- 重新整理 Claude 頁面，或開新 session 再試
- 確認 Connectors 裡的 higgs 工具都有啟用（display result 也要勾選）

---

### 問題 3：生成圖無法在 Claude 顯示

**症狀**：生成圖只有文字連結，沒有圖片預覽。  
**解法**：
1. 打開 Claude 設定 → Connectors → higgs
2. 把所有可以勾的選項全部勾起來，包括「Display Result」
3. 重新呼叫 `job_display(id='<job_id>')`

---

### 問題 4：CDN 圖片（Higgsfield CloudFront）無法從雲端 session 下載

**症狀**：在雲端 Claude Code session 裡用 `curl` 下載 `d8j0ntlcm91z4.cloudfront.net` 的圖片，收到 403 Forbidden。  
**原因**：Higgsfield CDN 會擋伺服器端的未授權請求。  
**解法**：改用 `raw.githubusercontent.com` 來存取已經 push 到 GitHub 的圖片。這個 URL 在雲端 session 裡可以正常存取：
```
https://raw.githubusercontent.com/pennyhuang-oss/Virtual_KOL_Studio/<commit-sha>/kols/<kol-id>/images/...
```

---

### 問題 5：圖片上傳到 GitHub 的錯誤位置

**症狀**：圖片上傳後跑到 `images/` 根目錄，而不是 `images/soul_test_v1/` 子資料夾。  
**正確資料夾結構**：
```
kols/<kol-id>/images/
├── face_reference/     ← 臉部參考圖（4 張）
└── soul_test_v1/       ← Soul 訓練後測試圖（6 張以上）
```
**解法**：從雲端 session 下載 raw.githubusercontent.com 的圖片，然後用 git 搬移並重新 push：
```bash
# 下載圖片
curl -s -o "/tmp/img.png" "https://raw.githubusercontent.com/..."

# 搬到正確位置
mkdir -p kols/<kol-id>/images/soul_test_v1/
cp /tmp/img.png kols/<kol-id>/images/soul_test_v1/

# 刪掉錯誤位置
git rm kols/<kol-id>/images/img.png

# commit & push
git add kols/<kol-id>/images/soul_test_v1/
git commit -m "..."
git push origin claude/kol-personality-training-9otdaw
```

---

### 問題 6：換裝置後 git 指令無法執行（Windows PowerShell）

**症狀**：在 PowerShell 執行 git 指令，出現「無法辨識 'git'」錯誤。  
**原因**：Windows PowerShell 預設不一定能找到 git；或目前所在目錄不是 git repo 的根目錄。  
**解法**：
- 不需要在本機執行 git，全部透過 Claude（雲端 session）操作
- Claude 在雲端 session 已有完整的 repo clone，可以直接 commit 和 push
- 如果需要在本機操作，使用「Git Bash」（Windows 安裝 Git for Windows 後會有）而不是 PowerShell

---

### 問題 7：雲端 session vs 本機 session 的差異

| 功能 | 雲端 session | 本機 session |
|------|-------------|-------------|
| 呼叫 Higgsfield MCP | ✅ | ✅ |
| 顯示生成圖片 | ✅（需開啟 Display Result） | ✅ |
| 啟動 Soul 訓練 UI | ✅（直接 API 呼叫） | ✅ |
| 下載 Higgsfield CDN 圖片 | ❌（403 Forbidden） | ✅ |
| 下載 raw.githubusercontent.com | ✅ | ✅ |
| git commit & push | ✅（透過 repo clone） | ✅ |

**結論**：訓練流程可以全部在雲端 session 完成。唯一限制是無法直接下載 Higgsfield CDN 圖片，但可以繞過（先 push 到 GitHub 再用 raw URL 讀取）。

---

## 每個 KOL 的資料夾結構

```
kols/<kol-id>/
├── character.md              ← 人格設定（含 Soul ID）
├── profile.json              ← 結構化資料（含 ai_generation）
├── content_style.md          ← 內容風格指南
├── script_self_intro.md      ← 自我介紹腳本
├── edit_timeline_self_intro.md ← 剪輯時間軸
├── generation_notes.md       ← AI 生成記錄（Soul ID、prompt、圖片連結）
└── images/
    ├── face_reference/       ← 臉部確認圖（4 張）
    └── soul_test_v1/         ← Soul 訓練後測試圖（6 張以上）
```

---

## 新裝置上手步驟

1. 打開 Claude（網頁版 claude.ai 或 Claude Code）
2. 確認 Connectors 裡 higgs 已連接且所有選項已勾選
3. 讓 Claude 讀取這份文件：
   ```
   請讀取 https://github.com/pennyhuang-oss/Virtual_KOL_Studio/blob/claude/kol-personality-training-9otdaw/KOL_TRAINING_SOP.md 並繼續訓練下一個 KOL
   ```
4. Claude 會自動知道進度、下一個要做誰、以及所有注意事項

---

## Higgsfield Soul V2 使用規則

- 模型名稱：`soul_2`（generate_image 裡用 `model: 'soul_2'`）
- 參數：`soul_id: '<soul_id>'`
- **不要**另外傳入 medias 作為臉部參考——Soul ID 本身就是身份
- 支援 aspect_ratio：`9:16`（直式）、`1:1`、`16:9`（橫式）
- 每次最多生成 4 張（count: 1–4）
- **⚠️ soul_id 只能用於靜態圖片生成**，影片生成中的臉部鎖定靠 `start_image` 參數（見下方舞蹈影片 SOP）

---

## 舞蹈影片生成流程（TikTok 熱梗舞）

> 完整 SOP 見 `DANCE_VIDEO_SOP.md`

**使用模型**：`seedance_2_0`（音樂同步，臉部鎖定）

**快速流程**：

```
1. media_upload + media_confirm → audio_media_id
2. soul_2 生成 start frame（THREE QUARTER SHOT）→ rawUrl
3. media_import_url → image_media_id
4. seedance_2_0（start_image + audio_references + generate_audio=False）→ 舞蹈影片
5. CapCut 後製：拖入 mp3，對齊開頭，導出
```

**適用所有 KOL**，每個 KOL 只需替換 soul_id 和服裝描述。
