# Virtual KOL Studio — 人格訓練 SOP

> 每次換裝置或開新 session 時，請讓 Claude 讀取這份文件，它會知道完整的執行方式與注意事項。

---

## 目前進度總覽

| KOL | Soul ID | 狀態 |
|-----|---------|------|
| Iris Chen | `5fe3b6ba-1277-4822-9141-fb06eb3b93a0` | ✅ 完成 |
| Luna Tanaka | `1bfab2ce-cfa5-4026-93fa-e5c91b469c7a` | ✅ 完成 |
| Ananya Kapoor | `fac82296-8c69-4c34-b352-1b398c8b8e1c` | 🔄 訓練完成，測試圖已上傳，場景待使用者下次確認 |
| Yuna Kim | `235794a5-2eff-45fb-91b4-3232910afefa` | 🔄 訓練完成，測試圖場景待確認 |
| Aaliya Rivera | `97f5c6cd-1c0c-4432-83d0-dd42210ecada` | 🔄 訓練完成，測試圖場景待確認 |
| Camille Dupont | `f19dafcc-5bc8-4d8f-af1d-ee48084ac398` | ✅ 完成 |

訓練順序：Ananya Kapoor → Yuna Kim → Aaliya Rivera → Camille Dupont

---

## ⚡ 新 Session 啟動時，立刻做這件事

> 讀完這份文件後，直接照以下清單執行，不用等使用者再說明。

### 現在的待辦（依優先順序）

1. **Yuna Kim — 詢問測試圖場景**
   - 訓練已完成（Soul ID: `235794a5-2eff-45fb-91b4-3232910afefa`）
   - 尚未生成測試圖，**必須先問使用者想要哪 3 個場景（含穿搭、構圖）再生成**
   - 生成完成後：圖片 push 到 `kols/yuna-kim/images/soul_test_v1/`，更新 `character.md`、`profile.json`、`generation_notes.md`

2. **Aaliya Rivera — 詢問測試圖場景**
   - 訓練已完成（Soul ID: `97f5c6cd-1c0c-4432-83d0-dd42210ecada`）
   - 同上流程，先確認場景再生成

3. **Ananya Kapoor — 使用者確認測試圖是否滿意**
   - 測試圖已上傳（`kols/ananya-kapoor/images/soul_test_v1/`），但使用者未確認場景是否OK
   - 若使用者想重新生成，需先確認新場景

### 注意事項（每次生成前必讀）
- **Iris Chen 是所有 KOL 的標準範本**：她是第一個完成的人格，後續每一個 KOL 的訓練規格、文件規模、步驟流程，全部以她為基準。不確定某個步驟怎麼做、某份文件要寫到什麼程度，就去看 `kols/iris-chen/` 的結構和內容對齊。
- **生成測試圖前，必須先列出預計場景讓使用者確認**，同意後才執行
- 圖片無法從雲端 session 下載 Higgsfield CDN，需使用者先上傳到 GitHub，再由 Claude 用 `raw.githubusercontent.com` 搬到正確資料夾
- 所有 push 都在 branch：`claude/kol-personality-training-9otdaw`
- **⚠️ 肢體動作多元化（所有人格適用）**：每次生成任何 KOL 的圖片，必須主動設計多元的姿勢、構圖與表情，禁止單一擺拍正面看鏡頭。規劃每張圖前先決定「這張照片的姿勢故事是什麼」，讓她在做某件事、有某種情緒，再寫 prompt。
  - 姿勢方向：看向遠方、中途動作被捕捉（撩髮/調整衣服/拿杯子）、側身或背影回眸、行走中側拍、坐姿變化（翹腳/前傾/下巴靠手）、與場景互動（靠牆/扶窗框/靠欄杆）
  - 表情方向：自然微笑、若有所思、被逗笑的瞬間感、放鬆閉眼享受
  - 構圖配合姿勢：廣角遠景時人物要有動態感；3/4 身時側身或斜角；近景時搭配表情或手部動作細節
- **⚠️ 同一場景兩張圖構圖必須不同（所有人格適用）**：同場景、同衣服、同環境，但兩張圖的景別和角度必須明顯不同（例如 3/4 身 vs 臉部近景；廣角遠景 vs 特寫；正面 vs 側面）

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
