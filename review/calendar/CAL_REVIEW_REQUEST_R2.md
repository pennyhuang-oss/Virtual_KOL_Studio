# CAL_REVIEW_REQUEST_R2 — 2027 KOL 雙款桌曆｜R2 送審請求

- **任務**：TASK-CAL-001／R2（修正 R1 證據與選圖，製作可供 owner 拍板的臉部比較及桌曆樣張）
- **Repo**：`pennyhuang-oss/Virtual_KOL_Studio`
- **分支**：`claude/epic-carson-n5w0qu`（未合併 main）
- **固定成果 commit**：`6a21602c95c1c4eef7f4816654d17b19a8af0815`
- **覆核者**：ChatGPT（規劃主管、獨立覆核）｜**拍板**：Penny｜**執行**：Claude

## 0. 讀取規則

- 只讀下面 §1、§2 列出的檔案與圖片，**不要爬整個 repo**。
- 以 commit `6a21602` 為準；同一分支之後的 commit 只會是本請求檔或你回覆後的修正。
- GitHub 網頁看檔：`https://github.com/pennyhuang-oss/Virtual_KOL_Studio/blob/6a21602c95c1c4eef7f4816654d17b19a8af0815/<路徑>`
- 請直接在對話裡回覆，由 Penny 轉回給 Claude。

## 1. 要讀的檔案（精確路徑，依序）

| 順序 | 路徑 | 內容 |
|---|---|---|
| 1 | `docs/calendar/CAL_05_R1_FIX_TABLE.md` | **R1 必改項逐項處理表**（每項：處理、檔案、狀態） |
| 2 | `review/calendar/CAL_R1_SUPERVISOR_REVIEW.md` | 你的 R1 覆核原文（逐字照錄，供核對沒被改寫） |
| 3 | `docs/calendar/CAL_10_OWNER_DECISIONS.md` | Penny 決策板（4 個決策附圖）、技術預設、廠商詢問稿（未發送） |
| 4 | `docs/calendar/CAL_06_FACES.md` | 十二人辨識比較：方法、既有碰撞值照錄、比較限制、重點配對、一致性 |
| 5 | `docs/calendar/CAL_07_PICKS_RETRIEVAL.md` | 逐位替代選圖、Higgsfield 取回範圍與方式、Ananya／Wendy |
| 6 | `docs/calendar/CAL_11_ASSET_QUALITY.md` | 素材分欄摘要、203 ppi 處理、橫式大照片逐張結果 |
| 7 | `docs/calendar/CAL_09_MOCKUPS.md` | 桌曆樣張規格、ppi 與臉部位置量測、發現 |
| 8 | `docs/calendar/CAL_08_DATES_2027.md` | 官方 2027 日期、適用範圍、廠商素材逐月比對、農曆 |
| 9 | `docs/calendar/CAL_01_SPEC_EVIDENCE.md` §3.3、§4、§5、§6 | R2 修正段落（翻頁改為假設、3/1 更正、條款拆分、試做前提） |
| 選讀 | `docs/calendar/CAL_11b_ASSET_TABLE.generated.md` | 52 張逐張分欄（程式產生，較長） |
| 選讀 | `docs/calendar/CAL_07b_HF_RETRIEVAL.generated.md` | 82 張取回逐張紀錄（程式產生） |
| 選讀 | `docs/calendar/CAL_02_CASTING.md` §4、§5.3；`CAL_03_ASSET_AUDIT_ROUTE.md` §2、§3、§6；`CAL_04_MONTHS_DECISIONS.md` | 其餘 R2 修正處（以「R2 修正」標出） |

## 2. 要看的圖（請實際打開；每張 < 1 MB）

| 路徑（皆在 `docs/calendar/` 底下） | 看什麼 |
|---|---|
| `r2/decisions/CAL_R2_decide_people_1.jpg`、`_2.jpg`、`_3.jpg` | **每月一列：H 建議、V 建議、替代** → 判斷人選與具體照片是否漂亮、性感、甜美，替代是否回應你的要求 |
| `r2/decisions/CAL_R2_decide_scale.jpg` | 尺度（同一人 Iris 的 A／B／C）與造型（Kanon 非女僕／女僕／女僕胸口開口） |
| `r2/decisions/CAL_R2_decide_people_backup.jpg`、`_compare.jpg` | 備選 Wanyin、Sophia（已換掉背影）；Ananya、Wendy 各 3 張 |
| `r2/faces/CAL_R2_focus_kanon_somi_tammy.jpg`、`CAL_R2_focus_angel_tammy.jpg`、`CAL_R2_focus_iris_rainie.jpg` | 重點配對：上＝遮髮、下＝完整頭像 |
| `r2/faces/CAL_R2_focus_consistency_vicky.jpg`、`_coco.jpg`、`_mia.jpg` | 同一人多張的一致性（Vicky 的 R1 橫式候選是不同的臉） |
| `r2/faces/CAL_R2_faces_B_1.jpg`、`_B_2.jpg`、`_B_extra.jpg` | 16 位遮髮總覽（A 完整頭像版：`_A_1`、`_A_2`、`_A_extra`） |
| `r2/faces/CAL_R2_focus_otherline_headshots.jpg` | 其他工作線當天的 neutral headshot（**只作觀察**，見 §5 第 7 點） |
| `r2/mockups/CAL_R2_mockups_01_iris-chen.jpg`、`_06_vicky-lin.jpg`、`_11_rin-ayase.jpg` | 每張 4 種：左上橫 A 半版、右上橫 B 大照片、左下直 A 大照片、右下直 B 縮框 |
| `r2/mockups/CAL_R2_pairs_1.jpg`、`_2.jpg`、`_3.jpg` | 照片面＋配對大格月曆面（橫、直）、兩款封面草稿 |
| `r2/assets/CAL_R2_assets_somi-oh.jpg`、`_tammy-chou.jpg`、`_coco-wu.jpg`、`_kanon-komori.jpg` | 裁切預覽（紅＝線圈）＋原圖 100% 細節（臉、手、假字、路人） |
| `r2/assets/CAL_R2_consistency_1.jpg` | 候選臉 vs 該角色參考臉（遮髮並排） |
| `r2/papermodel/CAL_R2_papermodel_H.jpg`、`_V.jpg` | 紙張模型：面號、正反面、兩種拼版假設、背面方向 |
| `r2/dates/CAL_R2_datecheck_01-02.jpg`、`_11-12.jpg` | 官方 vs 廠商日期素材並排（含補假最多的 2 月與 12 月） |

高解析版本：同名 `_hires.jpg`，或 `r2/mockups/hires/`（300 dpi 原尺寸）。

## 3. 已確定、不需再討論

2027 年；橫式、直式兩款都做；合作廠商免費試做；12 個月各一位不同既有人設；亞洲女性為主；漂亮、性感、甜美；展示不同長相與外型表現形式。

## 4. R1 必改項處理摘要（完整版見 `CAL_05`）

| 你的要求 | 處理 | 狀態 |
|---|---|---|
| 覆核紀錄＋逐項處理表 | 原文逐字照錄；處理表 | 完成 |
| 直式 MEMO 5 面＋年曆 1 面 | R1 文件本來正確；R1 送審請求措辭含糊，R2 一律寫「MEMO 5 面＋年曆 1 面（面 31）」 | 完成 |
| 正反面 vs 兩側同時可見；撤回同月兩面同時可見 | CAL_01 §3.3 重寫並撤回 | 完成 |
| 紙張模型、結果標假設 | H1／H2 兩種拼版假設＋背面方向 | 完成（仍為假設） |
| 兩款都做、免費＝已知前提 | 只列履行細節＋詢問稿 | 完成 |
| Miu 入 → 出 2 進 2 | 改寫並列候選 | 完成 |
| Sophia 未量測 ≠ 不碰撞 | 改寫 | 完成 |
| 撤回 Ananya 可替任意人 | 撤回並補 3 張圖 | 完成 |
| 刪除東亞限制、全面避開制服、D1 只做一款 | 刪除／撤回；制服改為 Penny 的造型選項 | 完成 |
| 泳裝／內衣 ≠ 不雅；製作上傳與評論上傳分開 | 條款拆三列；尺度改問廠商 | 完成 |
| 歷史 credits 只標歷史參考 | 已標 | 完成 |
| 十二人 A 頭像＋B 遮髮；說明限制；照錄碰撞值；不建新門檻 | 16 位 × 2 張；Batch 3 五位之間全部 10 組既有值照錄；沒有新門檻 | 完成 |
| Somi／Tammy／Rainie／Yuna／Rin／Luna／Kanon／Coco／Sophia 選圖 | 逐位處理（CAL_07 §3） | 完成（Yuna 柔和替代只有 1152 px，限小框） |
| daily_v2 原圖取回、逐張紀錄、64 張未確認 | 49 張取回並記錄；64 張標未確認 | 完成 |
| Ananya、Wendy 各 2–3 張 | 各 3 張 | 完成 |
| 素材分欄、細節圖、格紋、203 ppi、橫式滿版逐張、日期不算遮擋 | CAL_11／11b；138 張細節圖 | 完成 |
| 6 張月份照片面＋配對月曆面＋橫式大照片比較＋兩款封面 | CAL_09 | 完成 |
| 官方日期核對、範圍、廠商素材、農曆 | CAL_08 | 部分（見 §5 第 4 點） |
| 帶圖決策、技術細節自理、廠商詢問稿不發送 | CAL_10 | 完成 |
| **自查更正** | R1「廠商 3/1 未標紅」是誤判；Vicky R1 橫式是不同的臉；Kanon `train_03`（非女僕）R1 漏看 | 已更正 |

## 5. 未完成事項與原因

1. **廠商履行資訊**（數量、紙材、期限、交件方式與檔案規格、拼版與背面方向、印刷品質門檻、RGB／CMYK、單檔上限、尺度審稿、展示與案例、素材保密刪除）：依指示**不聯絡廠商**，詢問稿已寫好未發送。
2. **翻頁關係**：拼版與背面方向未確認 → 紙張模型結論仍是假設。
3. **原 11 位之間、原 11 位與 Batch 3 之間沒有數字量測**：只做 B 遮髮圖目視；依指示不建立未校準的新門檻。
4. **日期**：廠商橫式背面單行日期條字太小，只抽看 4 個月；2026/12、2028/1 小月曆不在範圍、未核。
5. **修圖未做**：假字（招牌、紙袋、毛衣、日期戳）、Hello Kitty 手機殼、背景路人都還在；本輪只做裁切、縮放、遮罩等衍生檔。
6. **橫式大照片要達 ≥250 ppi 需要新圖**（原生橫幅或外擴）：本輪不生成，只做現有圖的比較樣張（三位 190–254 ppi）。
7. **請你判斷是否越界**：為了在統一光線下補一組臉部觀察，我另外唯讀取回同帳號 2026-10-08 由**其他工作線**產生的 33 張 headshot（本案名單內的人設），只放觀察頁，不作依據、不作候選。若越界，下一輪刪除觀察頁與紀錄即可（原檔不在 repo）。
8. **留用 64 張**：repo 沒有名單、Higgsfield liked 欄全 false → 未確認。
9. **樣張沒有放進廠商編輯器試排**，也沒有色彩打樣。
10. **決策板圖沒有另存高解析版**：它是縮圖拼板；每張照片的高解析在 `r2/assets/*_hires.jpg`。

## 6. 本輪實際操作與驗證

| 做了什麼 | 結果 |
|---|---|
| Higgsfield `show_generations`、`show_characters`（唯讀） | 取回 82 張（49 daily_v2＋33 他線 headshot），全部成功，記 job_id／尺寸／sha256；12 主角＋2 備選＋Ananya、Wendy 共 16 個 Soul ID 在平台上都存在、狀態 ready |
| daily140 縮圖 ↔ job_id 對應 | 按時間排序對應 90/138 錯 → 改影像相關係數，138/138 對上（最低 r＝0.9999） |
| 人事總處 116 年辦公日曆表 xlsx 逐日解析 | 365 天星期全對、放假 121 天（與新聞稿一致）、無補班；`tools/parse_cal_r2_dgpa.py` 重建結果與存檔逐位元組相同 |
| 廠商日期素材 5 類逐月目視比對 | 紅字與官方全部一致；差異只在節日文字與併格 |
| 臉部比較（mediapipe 478 點，只裁切／縮放／遮罩） | 54 張頭像與遮罩圖；選圖角度記在 `data/cal_r2_face_geometry.json` |
| 素材量測 | 52 張 × 4 種框＝208 張裁切預覽、138 張原圖細節圖；與量測檔逐一對過，無殘留舊檔 |
| 樣張量測 | 12 張照片面的額頭全部在畫布上緣 23.9 mm 以下（線圈區 12 mm）；封面 24 格有效 ppi 全部 ≥ 364 |
| R1 重建 | 只因 R2 的文字修正改到 `casting_board.html`、`data/cal_r1_candidates.json` |
| 圖片大小 | 所有總覽圖 < 1 MB；只有 1 張高解析版略超過 1 MB |
| 範圍 | 只改 `docs/calendar/` 與 `review/calendar/`；沒有動其他工作線、人設原始素材、canon 或 Soul ID |
| **沒有做** | **沒有生成、沒有花 credits、沒有上傳、沒有下單、沒有聯絡廠商、沒有改 canon 或 Soul ID**；沒有重新訓練、沒有發布新公開網站、沒有修改任何 Higgsfield 紀錄 |

## 7. Penny 要選的具體圖片選項（`CAL_10`）

1. **人選與照片**：12 位照現在名單？Kanon／Somi／Tammy、Iris／Rainie 放一起像不像？要不要放進 Ananya、Wendy、Wanyin、Sophia？有替代的月份選哪張（2 月 Kanon 女僕 vs 非女僕 3 張；4 月 Angel 河岸；5 月 Somi 海邊；9 月 Yuna 柔和近照；10 月 Tammy 頂樓第二張；11 月 Rin 晨袍；12 月 Rainie 鏡前）。
2. **尺度與造型**：A 日常甜美／B 微性感（建議）／C 內衣（只作參考，需先問廠商）；職業制服（女僕、護理師）要不要用。
3. **版面**：橫式 A 半版（建議）或 B 大照片；直式 A 大照片（建議，不足 300 ppi 的月份自動縮框）或整本 B 縮框。
4. **品牌與收件對象**：給誰看、品牌名稱、Logo、QR（目前都是佔位）。

## 8. 請你回答（每項 PASS／REVISE／BLOCK＋一句理由）

**Q1 文件修正**：`CAL_05` 逐項處理是否到位？有沒有改寫你的結論，或仍把推論寫成事實？

**Q2 臉部比較**：`CAL_06` 的方法與限制說明是否足夠？看重點配對圖後，Kanon／Somi／Tammy、Iris／Rainie 是否需要在下一輪前換人，或交給 Penny 看圖決定即可？

**Q3 選圖**：`CAL_R2_decide_people_1–3` 每位的建議與替代，是否回應你點名的問題？有沒有仍不夠漂亮、性感或甜美的？

**Q4 素材品質**：`CAL_11`／`CAL_11b` 的分欄與「採用層級」是否合格？細節圖有沒有漏看的瑕疵？203 ppi 與橫式大照片的處理是否站得住？

**Q5 取回範圍**：49 張 daily_v2 的取回與紀錄是否合格？§5 第 7 點的 33 張他線 headshot 是否越界？

**Q6 樣張**：6 張主樣張（橫 A、直 A × Iris、Vicky、Rin）、配對月曆面、橫 B 比較、兩款封面，是否足以讓 Penny 拍板版面？日期可讀、臉不被侵入是否成立？

**Q7 日期**：`CAL_08` 的官方來源、適用範圍、廠商比對與農曆處理是否足夠？

**Q8 決策板與詢問稿**：`CAL_10` 是否夠簡短、Penny 能直接看圖回答？詢問稿是否只問影響交件的事？

**Q9 下一輪**：請根據覆核結論提供**下一輪（R3）的完整執行 prompt**，可直接貼給 Claude。

## 9. 回覆格式

```
Q1: PASS|REVISE|BLOCK — 理由
...
Q8: PASS|REVISE|BLOCK — 理由
必改項（若有）：
可選項（若有）：
R3 執行 prompt：
（完整文字）
```
