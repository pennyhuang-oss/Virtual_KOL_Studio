# CAL_REVIEW_REQUEST_R3 — 2027 KOL 雙款桌曆｜R3 送審請求

- **任務**：TASK-CAL-001／R3（修正 R2 證據與量測，整理一致版型、清理草稿，完成 Penny 可直接拍板的精簡決策包）
- **Repo**：`pennyhuang-oss/Virtual_KOL_Studio`｜**分支**：`claude/epic-carson-n5w0qu`（未合併 main）
- **固定成果 commit**：`4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45`（請以此為準，不以移動中的分支頭為準）
- **覆核者**：ChatGPT｜**拍板**：Penny｜**執行**：Claude
- GitHub 看檔：`https://github.com/pennyhuang-oss/Virtual_KOL_Studio/blob/4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45/<路徑>`

## 1. 必讀文件（依序；只讀這些）

| # | 路徑 | 內容 |
|---|---|---|
| 1 | `docs/calendar/CAL_12_R2_FIX_TABLE.md` | 你的 R2 結論逐項處理（完成／部分／未完成＋證據）與真正影響交印的缺口 |
| 2 | `docs/calendar/CAL_10_OWNER_DECISIONS.md` | Penny 決策包：四題、各一推薦、一行回覆、廠商詢問稿（未發送） |
| 3 | `docs/calendar/CAL_14_LAYOUT_R3.md` | 統一版型、實際裁切量測、橫 B 逐張、Kanon 重查 |
| 4 | `docs/calendar/CAL_13_PAGE_MODEL.md` | 完整頁序與紙張模型核算 |
| 5 | `docs/calendar/CAL_16_CLEANUP.md` | 清理：完成、部分、撤回 |
| 6 | `docs/calendar/CAL_08_DATES_2027.md` §3、§6 | 廠商素材已核／抽查／未核；自繪日期輸出頁核對 |
| 選讀 | `docs/calendar/CAL_14b_LAYOUT_TABLE.generated.md`、`CAL_15b_DATE_OUTPUT_CHECK.generated.md`、`CAL_13b_PAGE_MODEL.generated.md` | 程式產生的逐框、逐頁表 |
| 選讀 | `review/calendar/CAL_R3_EXEC_PROMPT_FROM_PENNY.md` | 你的 R2 結論與 R3 要求（Penny 轉交原文） |

## 2. 必看圖片（皆在 `docs/calendar/` 底下，預覽 < 1 MB）

| 路徑 | 看什麼 |
|---|---|
| `r3/decisions/CAL_R3_decide_A_roster.jpg` | 名單：A0（5 月 Somi）vs A1（5 月 Ananya）整組 |
| `r3/decisions/CAL_R3_decide_B_scale_style.jpg` | 尺度（Iris 三級）、Kanon 女僕與否、Angel 護理師與否 |
| `r3/decisions/CAL_R3_decide_C_layout.jpg` | 橫 A vs 橫 B；直式統一框 vs 原直 A（含 ppi） |
| `r3/sheets/CAL_R3_set_H_1.jpg`、`_H_2.jpg`、`_V_1.jpg`、`_V_2.jpg` | 24 面暫定工作稿（每格標圖片 ID、清理版／原圖、ppi、髮頂） |
| `r3/sheets/CAL_R3_set_cover_grid_year.jpg` | 兩款封面、9 月與 12 月大格月曆面、年曆 |
| `r3/sheets/CAL_R3_kanon_V_check.jpg` | Kanon 直式重查 |
| `r3/sheets/CAL_R3_HB_1.jpg` | 橫 B 192×104 逐張（1–6 月） |
| `r3/cleanup/kanon_alt028_compare.jpg`、`iris_V_compare.jpg`、`coco_alt01_compare.jpg` | 清理修前／修後／版面實際大小（含部分完成的手機殼） |
| `r3/pagemodel/CAL_R3_pagemodel_V.jpg` | 紙張模型（直式 32 面、16 張） |
| `r3/previews/CAL_R3_100pct_V_year_top.jpg` | 年曆 100% 實際像素（最小日期字 7.2 pt） |

可放大版本：同名 `_hires.jpg`，或單頁 `r3/pages/hires/<頁>.jpg`（300 dpi）。

## 3. 請判定（每題 PASS／REVISE／BLOCK＋一句理由）

1. **Q1 頁序與紙張模型**：H1／H2 核算與「H1 下照片面落在紙張背面」的發現是否正確？是否同意在廠商回覆前維持單面正向、不旋轉？
2. **Q2 統一版型**：直式統一框 120×128 取代原直 A 與「不足才縮框」是否合理？是否有你認為應列例外的月份？
3. **Q3 量測**：`CAL_14b` 的欄位（原圖、實際框、原生像素、ppi、臉、髮頂程式判定＋目視）是否滿足要求？24 面主推薦的目視只到總覽圖層級，是否足夠？
4. **Q4 選圖**：4 位橫直同圖（Kanon #028、Somi #063、Coco candidate_01、Tammy #130）與甜美／性感分列是否可以？
5. **Q5 清理**：完成的 5 項是否可接受（Iris 招牌近看看得出局部模糊）？手機殼「部分完成」移到選項、Somi 紙袋與 Tammy 路人撤回的處理是否恰當？
6. **Q6 日期**：輸出頁逐格核對（3,033 格、失敗 0、負向測試）與已核／抽查／未核分類是否滿足 Q7 的要求？
7. **Q7 決策包**：四題、推薦、代碼與一行回覆是否夠精簡、可直接給 Penny？廠商詢問稿是否只問影響交件的事？
8. **Q8 下一輪**：在 Penny 回答四題、廠商回覆前，下一輪應做什麼、不做什麼？請提供 R4 執行 prompt（或指示暫停等待）。

## 4. 回覆格式

```
Q1: PASS|REVISE|BLOCK — 理由
...
Q7: PASS|REVISE|BLOCK — 理由
必改項（若有）：
可選項（若有）：
R4 執行 prompt（或「暫停等待 Penny／廠商」）：
```
