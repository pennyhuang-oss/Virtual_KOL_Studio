# CAL_07 — 替代選圖與 Higgsfield 既有原圖取回紀錄（TASK-CAL-001／R2，R3 更新）

> **R3**：主推薦已改為 `data/cal_r3_picks.json`（4 位橫直同圖：Kanon #028、Somi #063、Coco candidate_01、Tammy #130）；本檔 §3 是 R2 的逐位替代紀錄。
> 選圖都是**建議**，未經 Penny 拍板。圖片請看 `r2/decisions/CAL_R2_decide_people_1.jpg`～`_3.jpg`（每月一列：H 建議、V 建議、替代）。逐張的技術、一致性、美感、瑕疵、動作在 `CAL_11b_ASSET_TABLE.generated.md`。

## 1. 取回範圍與方式

| 項目 | 內容 |
|---|---|
| 依據 | 主管 R2：「可取回相關 daily_v2 既有原圖，不需再把下載本身列成 owner 決策；不得下載無關帳號內容或修改紀錄」 |
| 方式 | Higgsfield `show_generations`（唯讀）列出既有 job → 以 job 的結果網址下載原檔到本機快取。**沒有生成、沒有花 credits、沒有修改或刪除任何紀錄** |
| 對應方法 | repo 只有 daily_v2 的 360×480 縮圖（`review/soul_pilot/daily140/thumbs/001–140.jpg`；原檔名 `001.png` 等記在 `index.json`，但 index 只有 Soul ID、沒有 job_id）。先試「按生成時間排序對應」→ 138 張有 90 張對錯，**放棄**；改用縮圖與 Higgsfield 預覽圖的影像相關係數逐張比對，138/138 對上（最低 r＝0.9999）。對照表：`data/cal_r2_daily140_jobs.json` |
| 取回了哪些 | daily140 涵蓋 20 位人設；**只取回與本案有關的 7 位**（Batch 3 的 kanon、somi、angel、tammy、rin＋備選 wanyin＋比較用 wendy），每位 7 張（D1–D5 第 1 輪＋D4、D5 第 2 輪）＝**49 張**，全部成功 |
| 沒取回 | daily140 的其他 13 位（與本案無關）；miu-shiraishi（不在工作名單，只在替換組合裡被提到） |
| 原檔存放 | 本機快取，**不進 repo**（49＋33 張共約 221 MB）。repo 只放裁切／縮圖等衍生檔。重建衍生檔的腳本都吃 `--hf-dir <快取資料夾>` |
| 逐張紀錄 | 程式產生的 `CAL_07b_HF_RETRIEVAL.generated.md`（job_id、daily140 編號、slot／take、生成時間、原始尺寸、取回狀態、完整 sha256（R3 補齊）、本輪用途）；原始資料 `data/cal_r2_hf_retrieved.json` |

### 1.1 「留用 64 張」

**未確認。** repo 沒有逐張的留用清單；Higgsfield 紀錄的 liked 欄位 138 張全部是 false。本輪取回的圖**不推定已獲 Penny 採用**；被選作候選只代表「Claude 認為可以給 Penny 看」。

### 1.2 其他工作線的 33 張 headshot（R3：維持排除，只留稽核）

- 查詢 Batch 3 紀錄時，同帳號 **2026-10-08 由其他工作線產生**的 neutral casting headshot 18 張（08:23–09:14 UTC）與 identity check 15 張（09:39–09:42 UTC）也被唯讀取回。它們**不是本任務生成、用途未知、未經 Penny 審**。
- 主管 R2 Q5：「33 張他線圖維持排除於依據之外」。R3 處理：**不作本案主角、身份參考、碰撞或辨識度結論的依據；不再擴大取回**；觀察頁從主要比較資料夾移到 `r2/audit_otherline/`（只留稽核），不放進 Penny 決策包。
- 稽核紀錄保留（`data/cal_r2_hf_retrieved.json`、`CAL_07b` §2）；**沒有刪除或修改任何 Higgsfield 紀錄**。

### 1.3 R3 本機快取核對

- `tools/verify_cal_r3_hfcache.py` 逐檔核對 82 張本機原圖：**82/82** 檔案存在、可解碼、尺寸與紀錄相同、sha256 與 R2 記下的前 16 碼相同後，把**完整 64 碼 sha256** 寫回 `data/cal_r2_hf_retrieved.json`（`CAL_07b` 表格改列完整 sha256）。**沒有重新下載。**
- judgments、臉部比較、R3 選圖裡所有 `hf:<job_id>` 參照都能在紀錄中定位（無法定位 0 個）。
- 留用 64 張：繼續標**未確認**。

## 2. 下載成功 ≠ 合格

49 張 daily_v2 原圖中，**10 張**被選作候選或比較用（含 wendy 2 張），另 5 張只用於臉部比較（`CAL_07b` 的「本輪用途」欄）；其餘 34 張未選。原因多半是 daily_v2 已知的「背景路人過近」：即使被選上的圖，最終交稿前也多需修掉路人（`CAL_11b` 的動作欄）。

## 3. 逐位替代選圖（對應主管 R2 §3）

| 月 | 人設 | R1 | R2 建議（H＝橫式、V＝直式） | 替代／對照 | 主管要求與處理 |
|---|---|---|---|---|---|
| 1 | iris-chen | H 咖啡店 `training_v1/06`；V 街拍 `training_v1/02` | 同 R1（V 需淡化招牌假字） | — | 未點名；同一張咖啡店圖橫半 420／直大 339 ppi，可兩用 |
| 2 | kanon-komori | H 女僕 `train_02`；V 女僕胸口開口 `train_01` | 同 R1（V 只適合縮框） | **非女僕**：daily_v2 #028 碎花洋裝甜點店、#112 酒紅單肩夜街、repo `train_03` cosplay 工作室短背心（R1 漏看） | 「提供非女僕既有候選」→ 有 3 張；女僕或非女僕列入 `CAL_10` 決策 2 |
| 3 | luna-tanaka | H 假 IG 介面字樣；V 1152 px（203 ppi） | H `face_reference/ref_01`；V `ref_02`（1728×2304） | R1 兩張作對照 | 「處理低解析度候選」→ 換圖，直式 305 ppi |
| 4 | angel-chiu | H 護理師 `train_02`；V 緞面細肩帶 `train_01` | 同 R1 | daily_v2 #004 河岸針織長洋裝（背景兩位男性路人） | 未點名 |
| 5 | somi-oh | H 炸雞 `train_01`；V 咬串燒 `train_02` | H 同 R1（紙袋假字需修）；**V daily_v2 #063 白西裝外套** | #065 海邊白洋裝（初夏感最強，但背景 3 位路人） | 「替換張嘴吃串燒」→ 已換 |
| 6 | vicky-lin | H `v3_01`（與 v4 訓練集不是同一張臉）；V `v4_anchored_05` | **H `v4_anchored_04`**；V 同 R1 | R1 `v3_01` 作對照 | 主管要求看一致性 → 發現 R1 橫式不一致，已換 |
| 7 | coco-wu | H `candidate_01`；V `candidate_03` | H 同 R1（人像牆需淡化）；**V `training_v1/01`**（Hello Kitty 手機殼需修掉） | R1 `candidate_03` 作對照 | 「評估人像牆與手機是否搶主角」→ candidate_03 的手機畫面是她自己的另一張臉、又有人像牆 → 換；candidate_01 人像牆會分散但主角臉最大 → 修圖 |
| 8 | mia-huang | H 電競椅 `02`；V 伸懶腰 `13` | 同 R1 | — | 未點名；紫光需打樣 |
| 9 | yuna-kim | H `ref_01`；V `street_02`（203 ppi） | H 同 R1；**V `face_reference/ref_04`**（305 ppi） | **柔和替代** `soul_test_v1/selfie_02`：臉最清楚，但 1152 px 寬（縮框也只有 236 ppi）且毛衣有假字 → 只適合小框 | 「較柔和替代」＋「低解析度」→ 已提供，限制如實標示 |
| 10 | tammy-chou | H 灰襯衫 `train_03`（需補生成）；V 倉庫坐箱 `train_01` | **H 倉庫坐箱 `train_01`**；**V daily_v2 #130 頂樓夜景黑洋裝** | #075 同場景第二張（表情更柔） | 「替換灰襯衫；比較倉庫坐箱與更能展現長捲髮、身形、柔和氣質的圖」→ 三張並排在 `CAL_R2_decide_people_3.jpg` |
| 11 | rin-ayase | H 盤髮裸背 `train_02`；V 晨袍回頭 `train_01` | H 同 R1；**V daily_v2 #053 正臉微笑**（背景路人需修） | R1 晨袍 `train_01`（最性感、臉小） | 「較柔和、臉清楚的替代」→ 已提供 |
| 12 | rainie-hsu | H 出門 `training_v2/04`；V 門口 `03`（人物偏小） | H 同 R1（假日期戳必修）；**V `training_v2/08` 床上晨光** | `training_v2/02` 鏡前濃豔 | 「替換門口照；柔和替代」→ 已換 |
| 備 | sophia-tseng | H 紅酒 `08`；V 背影 `01` | H 同 R1；**V `training_v1/02` 床上自拍甜笑**（建議縮框） | — | 「換掉背影」→ 已換 |
| 備 | wanyin-jiang | H `train_05`；V `train_04` | 同 R1 | — | 未點名；兩張都是全身，臉小 |

## 4. Ananya、Wendy 補圖（不只靠文字排除）

| 人設 | 圖 | 來源 | 看圖重點 |
|---|---|---|---|
| ananya-kapoor | ① `face_reference/ref_01` ② `ref_02` ③ `soul_test_v1/04_cafe_window_02` | repo | 深膚色、長捲髮、自信性感；與 12 位的臉部差異最大（`CAL_06` §4.4）。ref 兩張 1728×2304 可做任何框；③ 1152 px 屬邊緣 |
| wendy-yeo | ① daily_v2 #083 窗邊（冷感成熟、臉清楚）② daily_v2 #085 紅色抹胸背影回頭 ③ repo `training_v1/train_03` 浴袍 | daily_v2 ×2＋repo ×1 | 銀灰鮑伯辨識度高、偏冷；甜美度低於 12 位中多數 |

- 圖：`r2/decisions/CAL_R2_decide_people_compare.jpg`（決策板用）、`r2/assets/CAL_R2_assets_ananya-kapoor.jpg`、`_wendy-yeo.jpg`（裁切與細節）。
- 兩人**都沒有被排除**：要不要放進 12 位是 Penny 的美感判斷（`CAL_10` 決策 1）。若放進來，替換誰、會不會與既有碰撞值衝突，見 `CAL_02` §5.3 與 `CAL_06` §2（wendy 對 5 位 Batch 3 主角的值都 > 0.0220；ananya 沒有量測）。
