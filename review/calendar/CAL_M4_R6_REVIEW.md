TASK-CAL-001／M-4／R6｜全套寫真企劃重審｜送審報告

# M-4 R6 送審紀錄

- **固定成果 commit**：`5bed3a3163bbc9a84a5991034634e7bff9b2c6e5`（基準：上次部署收尾紀錄 `4bc31d35ca2981c3d48583ddc9ebbd770f6176af`；原照片 `a95e52feb0858f28de7ffbd6a105215d8f961f87`；原選片頁 `f04bc3d06c28ece44983f2f7ddd740021c33aa33`）
- **集中文件**：`docs/calendar/CAL_23_M4_R6_REPLAN.md`（由 `docs/calendar/tools/build_cal_m4_r6_doc.py` 從 `docs/calendar/data/cal_m4_r6_replan.json` 產生，`--check` PASS）
- **Owner 原始回饋**：`docs/calendar/data/cal_m4_owner_r6.json`（主管轉交的 R6 指令逐字，含 Penny 決定與逐張重點；與執行者分析分開）。Penny 在選片頁按「複製本批回饋」產生的原文沒有隨指令附上，執行者未取得；若之後提供，逐字補在同檔 `page_copy`。
- **狀態**：提案，待主管覆核。採用前 `cal_m3_shoot_plan.json` 的 24 套原文不改。以下是執行者自查，不是主管獨立覆核，也不是 Penny 接受。
- **本輪**：生成 0、修圖 0、訓練 0、付費操作 0、部署 0；不啟動下一批、不合併 main、不聯絡廠商。

## 1. Owner 決定的落實

- 第一批 5 張（V-tammy-chou、V-rin-ayase、V-somi-oh、H-yerin-han、H-jia-seo）逐張記為「Penny 退回／待重規劃」；沒有任何一張列為已接受或可交印。
- V-iris-chen 已接受，保留不改。
- M-4 R5 記為「生成與部署完成；第一批照片 Owner 全數退回」（`review/calendar/CAL_M4_R5_REVIEW.md` §8；CAL_22 開頭狀態行），不是品質驗收通過。
- 企劃升為 `shoot-plan-v12`：已生成 6、已接受 1、退回 5、其餘 23 套待製作；`batch1.status` = owner-rejected-r6。CAL_18、CAL_21、CAL_22 狀態行同步；CAL_19 位元組不變；CAL_20 只有版本號變動。
- 舊照片、舊企劃、測試與扣款證據都保留，沒有覆蓋或刪除。

## 2. 實際看圖（CAL_23 §1–§3）

- 實際打開：V-Iris 顯示版原圖與套框；5 張原圖（顯示版全圖，並以原圖 100% 看臉、手、腳、靴底、帽頂）與套框。檔案清單在 CAL_23 §1。
- Iris 成立的原因：光從哪裡來看得出來而且同時落在人與景上、衣服屬於這個地點與時間、動作是正在發生的瞬間、靠景深分離、背景沒有大型道具、色調一致、平視。這是七條品質原則，不是要複製河濱、姿勢或服裝。
- 5 張逐維度與 Iris 對照（構圖、人物占比、姿態、服裝與場景、透視與尺度、光線、配色、景深、精修氛圍、套框），Penny 的 20 個重點逐一列出照片證據、對應企劃原文與歸因。整體歸因：Tammy C（以 A 為主）、Rin C（以 A 為主）、Somi C（以 A 為主）、Yerin C、Jia C（以 A 為主）。共同的企劃根因是：85% 人物占比、身材展示優先、畫面外補光造成的獨立臉部光、輕仰、插腰類展示姿勢、大型接觸道具、服裝不合情境。

## 3. 共用規則（CAL_23 §4）

- 9 條造成問題的舊規則，受影響套數由企劃資料計算：85% 占比 13 套、身材展示目的句 21 套、畫面外補光 24 套、輕仰 5 套、展示型手部 6 套、大型接觸道具 8 套、服裝不合情境 6 套、鞋不寫入 prompt 11 套、fashion editorial 收尾 24 套。
- 12 條修訂規則（R6-1～R6-12）：先設計畫面、占比依景別（設計參考）、單一有來源的主光、平視、服裝先合情境、動作瞬間、大型道具只在必要時保留、身材只留在身分句、鞋一律定義、寫真集收尾句、素面環境、套框預留。

## 4. 24 套逐套審查（CAL_23 §5）

- 保留 1：V-iris-chen（已接受基準）。
- 整案重寫 7：V-tammy-chou、V-rin-ayase、V-somi-oh、H-yerin-han、H-jia-seo（第一批）、H-miu-shiraishi（床上睡衣構圖＋童顏顯小風險）、V-miu-shiraishi（吊床大型道具）。
- 局部重寫 16：H-yuna-kim、H-rin-ayase、H-tammy-chou、H-coco-wu、H-mia-huang、H-iris-chen（企劃，非已接受照片）、H-luna-tanaka、H-somi-oh、H-rainie-hsu、V-jia-seo、V-mia-huang、V-rainie-hsu、V-luna-tanaka、V-coco-wu、V-yerin-han、V-yuna-kim。
- 每套都列出現行構想與來源位置、人景比例、服裝鞋動作與場景、透視接觸與尺度、光線配色精修、套框可行性與結論理由。人物 canon、身分與已定案月份都沒有改；Penny 指定項目（H-Tammy 粉色針織洋裝、H-Luna 香袋與手部、已接受 v2 主方向的店／泳池／露台與服裝）都保留。

## 5. 重建稿（CAL_23 §6）

- 23 份重建稿都先寫畫面設計：一句話畫面與情緒、視覺主次、景別／相機／人物位置／大致占比（設計參考）、服裝與鞋、自然動作、光源明暗與色彩、背景整理、套框預留、最可能失敗的地方與降低風險。
- 第一批 5 張重建方案（附 prompt 草稿；身分句逐字沿用 CAL_21）：
  - V-Tammy（1 月）：新年夜老飯店酒廊的高拱窗邊，看窗外城市燈光；香檳色真絲中長洋裝、不拿包；吊燈暖光＋窗外夜光；約 50% 畫高。
  - V-Rin（10 月）：秋日傍晚石造迴廊，走進拱洞間的一道陽光；駝色長大衣＋象牙白針織中長洋裝＋踝靴；約 50%。
  - V-Somi（12 月）：保留溫泉街雪景；藍調時刻手插口袋走上坡、抬頭看雪；燕麥色長大衣＋磚紅圍巾＋褲襪短靴；燈籠為主光；約 40–45%。
  - H-Yerin（5 月）：移除球車；晨光中拎一支球桿走在球道邊；逆光、枝葉茂密的春天樹林；約 50%。
  - H-Jia（9 月）：保留湖畔；坐在木平台盡頭看夕陽湖面；燕麥色開襟＋深酒紅長洋裝＋平底涼鞋；移除長椅；約 35–40%。
- 其餘 18 套在排入生成批次時，依同一份設計組 prompt 並送審。

## 6. 生成前後把關（CAL_23 §7）

- 生成前 8 項：畫面邏輯、人景主次、服裝情境、姿態、尺度與接觸、光線、配色、prompt 用語。
- 生成後 7 項依序：第一眼、人景融合、比例與透視、姿態與神情、構圖與套框、技術細節、解析度。1–4 任一項失敗就退回，即使手腳正常、解析度足夠。

## 7. 需要 Penny 決定（CAL_23 §8）

- D1 H-Miu 3 月：改窗邊晨光（建議）或保留床上題材。
- D2 雪景服裝（H-Yuna 1 月、V-Somi 12 月）：及膝／中長裙＋褲襪（建議）、迷你裙＋褲襪、或保留光腿（不建議）。
- D3 V-Rin 10 月新場景：石造迴廊（建議）或紅葉庭園小徑。
- D4 H-Rainie 12 月：已接受的紅色緞面洋裝外是否加披肩長大衣（建議加）。
- D5 H-Yerin 5 月：移除球車（建議）或保留但改遠景。

## 8. 未處理與提醒

- 線上選片頁（f04bc3d）仍顯示第一批 5 張與回饋按鈕；本輪不部署，等下次部署時更新。
- 下一次生成的範圍與費用另行確認；本輪沒有報價或送出。

## 9. 主管覆核用檔案

- `docs/calendar/CAL_23_M4_R6_REPLAN.md`（主要文件）
- `docs/calendar/data/cal_m4_r6_replan.json`（分析與提案資料）
- `docs/calendar/data/cal_m4_owner_r6.json`（Owner 決定與指令逐字）
- `docs/calendar/tools/build_cal_m4_r6_doc.py`（產生器與核對，`--check`）
- `docs/calendar/data/cal_m3_shoot_plan.json`（v12 狀態）與 `docs/calendar/CAL_18_M3_SHOOT_PLAN.md`、`CAL_22_M4_BATCH1_RESULTS.md`（狀態行）
- 看圖用原檔：`kols/{tammy-chou,rin-ayase,somi-oh,yerin-han,jia-seo}/images/calendar_2027_batch1/*_m4r5.png`、`review/calendar/m4_r5/*_frame_*.jpg`、`docs/calendar/decision_site/public/img/review/V-iris-chen_m4r2_view.jpg`、`review/calendar/m4_r2/frame_preview_V_120x160.jpg`
