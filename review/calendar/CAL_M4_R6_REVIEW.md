TASK-CAL-001／M-4／R6｜主管覆核 REVISE｜修正重審規則與構圖矛盾｜送審報告

# M-4 R6 送審紀錄（依主管覆核 REVISE 修訂，v2）

- **固定成果 commit**：`1af817043f700d7e6275c2f037fc3ca9e33159d0`（基準：上一版送審紀錄 `1e7d5100fdcda804d3d8425cba7d8ee15756eda4`；被覆核的 v1 成果 `5bed3a3163bbc9a84a5991034634e7bff9b2c6e5`；原照片 `a95e52feb0858f28de7ffbd6a105215d8f961f87`；線上選片頁 `f04bc3d06c28ece44983f2f7ddd740021c33aa33`）
- **主管覆核原文**：`docs/calendar/data/cal_m4_supervisor_r6.json`（主管覆核意見經 Penny 轉交，逐字保存；維持 R6，不另開新輪次）
- **集中文件**：`docs/calendar/CAL_23_M4_R6_REPLAN.md`（由 `docs/calendar/tools/build_cal_m4_r6_doc.py` 從 `docs/calendar/data/cal_m4_r6_replan.json`〔replan-r6-v2〕產生，`--check` PASS）
- **狀態**：提案，待主管覆核。採用前 `cal_m3_shoot_plan.json` 的 24 套原文不改。以下是 Claude 自查，不是主管驗收，也不是 Penny 接受。
- **本輪**：生成 0、修圖 0、訓練 0、付費操作 0、部署 0；不啟動下一批、不改已接受的 V-Iris、不合併 main。

## 1. 修改對照（摘要；完整 18 項見 CAL_23 §0.1）

| 主管意見 | 本版處理 |
|---|---|
| 一、寫真定位 | 刪除「不精修／unretouched／available light／unposed」作為全套必要條件；目標改為寫真集完成度（允許姿態指導、補光、調色、膚質與環境整理），本輪不實際修圖。收尾句改為「Natural skin texture with visible pores, believable light that belongs to the scene, refined colour grading, finished like a page from a high-end photobook.」補光、插腰、看鏡頭、近景、身材表現、高飽和都不再直接判為失敗；舊規則表分「廢止」與「條件」，表中「出現的套」不等於有問題。 |
| 二、24 套節奏 | 新增節奏表（景別、主次、明暗、色彩、情緒、主要動作、視線、這張最吸引人的地方），橫式、直式分開統計；修正直式 8–9 月（V-Yerin 與 V-Iris 同型）、直式 10–11 月（迴廊與銀杏大道同型）、直式 2／6 月、橫式 5–6 月與 9 月的重複。 |
| 三、構圖與攝影描述 | 每套寫人物占比範圍與預期配置（頭頂＋人物＋腳下＝100%），最低安全邊界另列；產生器由焦段與占比算出距離、成品人物與頭部尺寸、畫面涵蓋範圍、相機俯仰與地平線位置並核對一致（全片幅等效設計參考）。刪除「Yerin 大了三成」推估。V-Somi 成品改為 64–72 mm（原誤寫約 5 cm）；H-Jia 45–52 mm（原寫約 4 cm）；v1 膝上寫成約 60–65% 的矛盾一併修正。 |
| 四、第一批 5 份 | 見 §4。其餘套撥髮 6→3、回頭笑 5→0、看窗外 3→1、碰花葉 5→1；接花瓣、手拿銀杏葉刪除；一張一個主要動作。 |
| 五、決策重整 | D1–D5 逐項確認是否碰到 Owner 已定事項：D1、D2、D4 保留 Owner 已定內容；D3、D5 是本輪授權內設計，給完整推薦。尚待 Penny 決定：無。 |
| 六、來源與紀錄 | Owner 紀錄分層標示（R6 指令原文／Owner 決定／主管摘要／Penny 頁面原文＝交接缺件，不是執行者漏讀，取得後逐字補存）。進度改為 24 套＝已接受 1＋退回待重規劃 5＋尚未生成 18；待完成合計 23；累計已生成 6（另計）。CAL_18、CAL_21 狀態行同步。 |

## 2. 24 套結論（v2）

- 已接受（不改）1：V-iris-chen。
- 保留設計 3：H-coco-wu、V-coco-wu、V-mia-huang（設計不改，prompt 只套共用格式）。
- 局部修改 14：H-yuna-kim、H-rin-ayase、H-miu-shiraishi、H-tammy-chou、H-mia-huang、H-iris-chen、H-luna-tanaka、H-somi-oh、H-rainie-hsu、V-jia-seo、V-rainie-hsu、V-luna-tanaka、V-yerin-han、V-yuna-kim。
- 整案重寫 6：第一批 5 張＋V-miu-shiraishi（吊床移除）。H-Miu 由 v1 整案改為局部（保留 Owner 已接受的床上題材）。
- 節奏分布（CAL_23 §5.2 自動統計）：橫式 近 2／中 5／遠 5、看鏡頭 8／12；直式 近 1／中 5／遠 6、看鏡頭 7／12。

## 3. 構圖核算方法（CAL_23 §6）

- 距離＝可見範圍×焦段÷（畫面高×占比）；可見範圍＝身高×景別比例（設計參考）。成品人物高度＝占比×進框原圖高（直式 160 mm；橫式 108 mm、框內 104 mm）。
- 核對：預期配置加總 100%；裁切景別人物占比 ≥80%；最低安全邊界（直式頭腳各 ≥3%；橫式頭頂 ≥6%、腳下 ≥5%）；相機高度與平視高度差 ≤6°；地平線不穿過頭頸、不落在橫式裁切帶；prompt 的焦段與距離和核算一致；文字中的 mm 數字等於核算值。
- 自查做了反向測試：把 V-Somi 距離改回 8 m、尺寸寫成 50–55 mm、配置寫成 8＋58＋5、膝上寫成 60%、H-Jia 相機改 0.8 m（對岸線穿過頭部）、prompt 加 unretouched 或 reflector、吸引點只寫「自然」、V-Yerin 加撥頭髮，產生器都會擋下。

## 4. 第一批 5 份修訂方案（完整設計卡與 prompt 草稿見 CAL_23 §6）

| 套別 | v2 方案 | 對應主管意見 | 核算（全片幅等效，設計參考） |
|---|---|---|---|
| V-Tammy（1 月） | 新年夜老飯店酒廊：側坐深藍綠絲絨扶手椅，黃銅落地燈是主光、同色溫補光讓臉清楚；香檳色緞面斜裁中長洋裝、不拿包；看鏡頭。 | 交代合理的室內光與臉部呈現，不追求無補光 | 坐姿全身 58–66%；50mm 約 3.0 m；成品 93–106 mm |
| V-Rin（10 月） | 保留迴廊：低斜硬光從拱洞切進來成為光影主體；黑色細針織中長洋裝＋披肩駝色大衣；肩靠石柱、臉迎光、眼簾半垂；膝上。 | 檢查造型魅力與光影層次，不做普通大衣旅遊照 | 膝上 86–90%；50mm 約 2.1 m |
| V-Somi（12 月） | 保留雪街與 Owner 已接受造型（大衣改深蔓越莓紅）；藍調時刻，她走到最近的燈籠下，燈籠光同時落在她和周圍雪地、木牆，背光側是藍色天光。 | 人物位置與最近燈籠及天光整合，不再暖臉貼冷背景 | 全身 40–45%；50mm 約 5.9 m；成品 64–72 mm |
| H-Yerin（5 月） | 移除球車；一個動作：雙手疊在立在草上的球桿握把上站定、望向球道遠端；側前方晨光＋同色溫補光。 | 簡化走路、拎桿、碰帽、回頭笑的多重動作 | 全身 55–60%；85mm 約 12.3 m；成品 59–65 mm |
| H-Jia（9 月） | 保留湖畔：平台從右下斜入、她坐在盡頭右三分之一、對岸線在上三分之一且不切過頭部；日落後餘暉照亮側臉；深酒紅細針織長洋裝＋滑肩米白開襟。 | 人物縮小但保留辨識與寫真吸引力，以具體構圖取代「人很小」 | 坐姿全身 42–48%；50mm 約 5.2 m；相機約 1.1 m 微向下；成品 45–52 mm |

5 份 prompt 的身分句都和 CAL_21 逐字相同（canon 不改）；焦段與距離和核算一致；沒有器材名詞、百分比、身材展示目的句、fashion editorial、unretouched／unposed／available light。本輪不送出、不報價。

## 5. 尚待 Owner 決策

- 無。D1–D5 的逐項確認見 CAL_23 §8：D1（H-Miu 床上題材）、D2（雪景短裙＋長靴）、D4（H-Rainie 不加外套）保留 Owner 已定內容；D3（V-Rin 迴廊）、D5（H-Yerin 移除球車）是本輪授權內設計，給完整推薦。
- 提醒主管覆核：V-Somi 大衣由亮紅改深蔓越莓紅屬「已接受造型的顏色調整」，理由是 Penny 指出色彩對比不協調；若主管認為需 Penny 確認，可改列。

## 6. Claude 自查（不是主管驗收或 Penny 接受）

- `python3 docs/calendar/tools/build_cal_m4_r6_doc.py --check` → PASS（含構圖核算、prompt、節奏、來源與進度欄位核對；另做 12 項反向測試，11 項原本就會擋下，「膝上寫成 60%」原本沒擋，已補核對後擋下）。
- `python3 docs/calendar/tools/build_cal_m3_plan_doc.py --check` → PASS（CAL_18–22；CAL_19 位元組不變；CAL_18、CAL_21 狀態行改用新進度欄位）。
- `python3 docs/calendar/tools/build_cal_decision_site.py --check --hf-dir … --clean-dir …` → PASS：671 檔，問題 0；公開檔無私有識別碼、無交易原始資料（site 資料只在 repo 內更新，沒有部署）。

## 7. 未處理與提醒

- 線上選片頁（`f04bc3d`）仍顯示第一批 5 張與回饋按鈕；本輪部署 0，等下次部署時更新。
- Penny 選片頁的完整回饋原文仍是交接缺件；取得後逐字補存在 `cal_m4_owner_r6.json` 的 `page_copy.text`。
- 下一次生成的範圍與費用另行確認；本輪沒有報價或送出。

## 8. 必要閱讀清單（主管覆核用）

1. `docs/calendar/CAL_23_M4_R6_REPLAN.md`：§0.1 修改對照、§5.2 節奏表與分布、§6 構圖核算總表與第一批 5 張設計卡＋prompt、§8 決策重整（主要文件）。
2. `docs/calendar/data/cal_m4_r6_replan.json`（replan-r6-v2 資料）。
3. `docs/calendar/data/cal_m4_supervisor_r6.json`（主管 REVISE 逐字）與 `docs/calendar/data/cal_m4_owner_r6.json`（來源分層、交接缺件）。
4. `docs/calendar/tools/build_cal_m4_r6_doc.py`（核算公式與核對）。
5. `docs/calendar/data/cal_m3_shoot_plan.json` 的 `status.production` 與 `m4r6`（進度欄位定義）。
6. 看圖原檔（同 v1）：`kols/{tammy-chou,rin-ayase,somi-oh,yerin-han,jia-seo}/images/calendar_2027_batch1/*_m4r5.png`、`review/calendar/m4_r5/*_frame_*.jpg`、`docs/calendar/decision_site/public/img/review/V-iris-chen_m4r2_view.jpg`。

## 附錄：v1 送審紀錄（`1e7d510`；已由本版取代，原文保留）

> TASK-CAL-001／M-4／R6｜全套寫真企劃重審｜送審報告
>
> # M-4 R6 送審紀錄
>
> - **固定成果 commit**：`5bed3a3163bbc9a84a5991034634e7bff9b2c6e5`（基準：上次部署收尾紀錄 `4bc31d35ca2981c3d48583ddc9ebbd770f6176af`；原照片 `a95e52feb0858f28de7ffbd6a105215d8f961f87`；原選片頁 `f04bc3d06c28ece44983f2f7ddd740021c33aa33`）
> - **集中文件**：`docs/calendar/CAL_23_M4_R6_REPLAN.md`（由 `docs/calendar/tools/build_cal_m4_r6_doc.py` 從 `docs/calendar/data/cal_m4_r6_replan.json` 產生，`--check` PASS）
> - **Owner 原始回饋**：`docs/calendar/data/cal_m4_owner_r6.json`（主管轉交的 R6 指令逐字，含 Penny 決定與逐張重點；與執行者分析分開）。Penny 在選片頁按「複製本批回饋」產生的原文沒有隨指令附上，執行者未取得；若之後提供，逐字補在同檔 `page_copy`。
> - **狀態**：提案，待主管覆核。採用前 `cal_m3_shoot_plan.json` 的 24 套原文不改。以下是執行者自查，不是主管獨立覆核，也不是 Penny 接受。
> - **本輪**：生成 0、修圖 0、訓練 0、付費操作 0、部署 0；不啟動下一批、不合併 main、不聯絡廠商。
>
> ## 1. Owner 決定的落實
>
> - 第一批 5 張（V-tammy-chou、V-rin-ayase、V-somi-oh、H-yerin-han、H-jia-seo）逐張記為「Penny 退回／待重規劃」；沒有任何一張列為已接受或可交印。
> - V-iris-chen 已接受，保留不改。
> - M-4 R5 記為「生成與部署完成；第一批照片 Owner 全數退回」（`review/calendar/CAL_M4_R5_REVIEW.md` §8；CAL_22 開頭狀態行），不是品質驗收通過。
> - 企劃升為 `shoot-plan-v12`：已生成 6、已接受 1、退回 5、其餘 23 套待製作；`batch1.status` = owner-rejected-r6。CAL_18、CAL_21、CAL_22 狀態行同步；CAL_19 位元組不變；CAL_20 只有版本號變動。
> - 舊照片、舊企劃、測試與扣款證據都保留，沒有覆蓋或刪除。
>
> ## 2. 實際看圖（CAL_23 §1–§3）
>
> - 實際打開：V-Iris 顯示版原圖與套框；5 張原圖（顯示版全圖，並以原圖 100% 看臉、手、腳、靴底、帽頂）與套框。檔案清單在 CAL_23 §1。
> - Iris 成立的原因：光從哪裡來看得出來而且同時落在人與景上、衣服屬於這個地點與時間、動作是正在發生的瞬間、靠景深分離、背景沒有大型道具、色調一致、平視。這是七條品質原則，不是要複製河濱、姿勢或服裝。
> - 5 張逐維度與 Iris 對照（構圖、人物占比、姿態、服裝與場景、透視與尺度、光線、配色、景深、精修氛圍、套框），Penny 的 20 個重點逐一列出照片證據、對應企劃原文與歸因。整體歸因：Tammy C（以 A 為主）、Rin C（以 A 為主）、Somi C（以 A 為主）、Yerin C、Jia C（以 A 為主）。共同的企劃根因是：85% 人物占比、身材展示優先、畫面外補光造成的獨立臉部光、輕仰、插腰類展示姿勢、大型接觸道具、服裝不合情境。
>
> ## 3. 共用規則（CAL_23 §4）
>
> - 9 條造成問題的舊規則，受影響套數由企劃資料計算：85% 占比 13 套、身材展示目的句 21 套、畫面外補光 24 套、輕仰 5 套、展示型手部 6 套、大型接觸道具 8 套、服裝不合情境 6 套、鞋不寫入 prompt 11 套、fashion editorial 收尾 24 套。
> - 12 條修訂規則（R6-1～R6-12）：先設計畫面、占比依景別（設計參考）、單一有來源的主光、平視、服裝先合情境、動作瞬間、大型道具只在必要時保留、身材只留在身分句、鞋一律定義、寫真集收尾句、素面環境、套框預留。
>
> ## 4. 24 套逐套審查（CAL_23 §5）
>
> - 保留 1：V-iris-chen（已接受基準）。
> - 整案重寫 7：V-tammy-chou、V-rin-ayase、V-somi-oh、H-yerin-han、H-jia-seo（第一批）、H-miu-shiraishi（床上睡衣構圖＋童顏顯小風險）、V-miu-shiraishi（吊床大型道具）。
> - 局部重寫 16：H-yuna-kim、H-rin-ayase、H-tammy-chou、H-coco-wu、H-mia-huang、H-iris-chen（企劃，非已接受照片）、H-luna-tanaka、H-somi-oh、H-rainie-hsu、V-jia-seo、V-mia-huang、V-rainie-hsu、V-luna-tanaka、V-coco-wu、V-yerin-han、V-yuna-kim。
> - 每套都列出現行構想與來源位置、人景比例、服裝鞋動作與場景、透視接觸與尺度、光線配色精修、套框可行性與結論理由。人物 canon、身分與已定案月份都沒有改；Penny 指定項目（H-Tammy 粉色針織洋裝、H-Luna 香袋與手部、已接受 v2 主方向的店／泳池／露台與服裝）都保留。
>
> ## 5. 重建稿（CAL_23 §6）
>
> - 23 份重建稿都先寫畫面設計：一句話畫面與情緒、視覺主次、景別／相機／人物位置／大致占比（設計參考）、服裝與鞋、自然動作、光源明暗與色彩、背景整理、套框預留、最可能失敗的地方與降低風險。
> - 第一批 5 張重建方案（附 prompt 草稿；身分句逐字沿用 CAL_21）：
>   - V-Tammy（1 月）：新年夜老飯店酒廊的高拱窗邊，看窗外城市燈光；香檳色真絲中長洋裝、不拿包；吊燈暖光＋窗外夜光；約 50% 畫高。
>   - V-Rin（10 月）：秋日傍晚石造迴廊，走進拱洞間的一道陽光；駝色長大衣＋象牙白針織中長洋裝＋踝靴；約 50%。
>   - V-Somi（12 月）：保留溫泉街雪景；藍調時刻手插口袋走上坡、抬頭看雪；燕麥色長大衣＋磚紅圍巾＋褲襪短靴；燈籠為主光；約 40–45%。
>   - H-Yerin（5 月）：移除球車；晨光中拎一支球桿走在球道邊；逆光、枝葉茂密的春天樹林；約 50%。
>   - H-Jia（9 月）：保留湖畔；坐在木平台盡頭看夕陽湖面；燕麥色開襟＋深酒紅長洋裝＋平底涼鞋；移除長椅；約 35–40%。
> - 其餘 18 套在排入生成批次時，依同一份設計組 prompt 並送審。
>
> ## 6. 生成前後把關（CAL_23 §7）
>
> - 生成前 8 項：畫面邏輯、人景主次、服裝情境、姿態、尺度與接觸、光線、配色、prompt 用語。
> - 生成後 7 項依序：第一眼、人景融合、比例與透視、姿態與神情、構圖與套框、技術細節、解析度。1–4 任一項失敗就退回，即使手腳正常、解析度足夠。
>
> ## 7. 需要 Penny 決定（CAL_23 §8）
>
> - D1 H-Miu 3 月：改窗邊晨光（建議）或保留床上題材。
> - D2 雪景服裝（H-Yuna 1 月、V-Somi 12 月）：及膝／中長裙＋褲襪（建議）、迷你裙＋褲襪、或保留光腿（不建議）。
> - D3 V-Rin 10 月新場景：石造迴廊（建議）或紅葉庭園小徑。
> - D4 H-Rainie 12 月：已接受的紅色緞面洋裝外是否加披肩長大衣（建議加）。
> - D5 H-Yerin 5 月：移除球車（建議）或保留但改遠景。
>
> ## 8. 未處理與提醒
>
> - 線上選片頁（f04bc3d）仍顯示第一批 5 張與回饋按鈕；本輪不部署，等下次部署時更新。
> - 下一次生成的範圍與費用另行確認；本輪沒有報價或送出。
>
> ## 9. 主管覆核用檔案
>
> - `docs/calendar/CAL_23_M4_R6_REPLAN.md`（主要文件）
> - `docs/calendar/data/cal_m4_r6_replan.json`（分析與提案資料）
> - `docs/calendar/data/cal_m4_owner_r6.json`（Owner 決定與指令逐字）
> - `docs/calendar/tools/build_cal_m4_r6_doc.py`（產生器與核對，`--check`）
> - `docs/calendar/data/cal_m3_shoot_plan.json`（v12 狀態）與 `docs/calendar/CAL_18_M3_SHOOT_PLAN.md`、`CAL_22_M4_BATCH1_RESULTS.md`（狀態行）
> - 看圖用原檔：`kols/{tammy-chou,rin-ayase,somi-oh,yerin-han,jia-seo}/images/calendar_2027_batch1/*_m4r5.png`、`review/calendar/m4_r5/*_frame_*.jpg`、`docs/calendar/decision_site/public/img/review/V-iris-chen_m4r2_view.jpg`、`review/calendar/m4_r2/frame_preview_V_120x160.jpg`
