TASK-CAL-001／M-3／R5｜企劃資料一致性與生成前技術收尾｜送審報告

# M-3／R5 送審紀錄

- **成果 SHA**：`9434b839f589c19832a88e36975fbb31527b7284`（基準：R4 固定成果 `4f1591790d0e04cd58b93d95be470c2ff602e63b`、送審 `42fb5df6534f0c7a75ae59a462e527ea0c891a8e`）
- **部署**：Railway 只更新 `cal2027-decision`，固定到 `9434b839f589c19832a88e36975fbb31527b7284`，deployment `d2d5674f-b4ed-4c24-aee2-8dd5c7234724`（SUCCESS）；其他 service 未動；未合併 main、未開 PR
- **企劃頁**：https://cal2027-decision-production.up.railway.app/shoot.html（免登入）
- **性質**：只修資料一致性與措辭。企劃版本仍是 shoot-plan-v5（round 改為 R5），16 套回饋延續、不重設、不需重填。生成 0、credits 0、訓練 0、Higgsfield 呼叫 0、外部聯絡 0。
- 以下驗證都是 Claude 自測，不是主管覆核；部署不等於核准。

## 1. 四項修改

1. **過時文案**：7 個月份理由改成目前企劃；已接受 V-iris、V-luna 的「與另一款的差異」改成目前的橫式款；刪除已失效的「Rin 及地長禮服」景別規則；CAL_18 的 R2 落實表欄名標成「當時（R2）怎麼落實（歷史）」。R4 owner 原文、R2 回饋、R4「改了什麼」都不改。
2. **撤回橫直參考圖策略**：execution.model.multi_stage 改為 H／V 是獨立服裝與場景，只共同維持人設身分與設定身材，不得為了讓服裝或環境相同而跨款套用參考圖；未來若要用參考圖須另行提出。頁面費用區與 CAL_18 §10 都顯示更正後文字。
3. **已接受 3 套補英文妝感**（主管核可）：只在 prompt 身分句後加一句；接受狀態沿用，r5 欄位註明主管核可的中英同步；這 3 套不再宣稱與 v4 逐字相同，另 5 套仍與 v4 相同。
4. **印刷措辭**：分成已知尺寸、比例計算、prompt 規劃目標、生成後待驗證四類；24 套的留白百分比標成「規劃／套框後理論」；判斷改成條件句「依暫定框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi」；新增每套「生成後待驗證」；120×128 寫成「裁去高度 20% 是比例事實，是否切到部位要看實圖」；保留線圈 12 mm 假設、16:9 輸出未知、300 ppi 是工作目標的限制。沒有重畫示意圖、沒有換框、沒有新增廠商查證。
   - 順帶更正兩個數字：半版直幅框 104×155 的寬度裁切是約 62%（原寫「約七成」）；V-Iris 髮頂規劃留白是約 8%（R4 結論誤寫 7%，與逐張表不一致）。

## 2. 差異（印刷逐張 24 套的舊／新文字在資料檔 `r5.changes`）

| 類別 | 位置 | 舊 | 新 |
|---|---|---|---|
| 月份理由 | months[1月].why_h | 冬日的明亮咖啡館，用清透的奶油黃開場 | 雪後清晨的白樺林，用雪白與霧玫瑰的冬日寫真開場 |
| 月份理由 | months[4月].why_h | 春天逛精品店的熱粉洋裝 | 春日花園露台的熱粉洋裝 |
| 月份理由 | months[4月].why_v | 暮春運河新綠 | 春日別墅木平台與開滿白花的果樹 |
| 月份理由 | months[8月].why_h | 夏末午後的紅磚騎樓 | 盛夏上午的岩岸海灣與向日葵黃 |
| 月份理由 | months[9月].why_h | 初秋美術館的冷調 | 初秋傍晚的湖畔木平台 |
| 月份理由 | months[10月].why_h | 秋日清晨的和室柔光 | 秋日傍晚前的當代日式旅宿與窗外紅葉 |
| 月份理由 | months[10月].why_v | 秋夜的金色酒吧 | 秋日午後的安靜港灣 |
| 交叉引用（已接受套數的比較文字，不是服裝場景表情） | sets[V-iris-chen].vs_other | 橫式款在紅磚騎樓、米杏針織套裝、側光；這款在河濱草地、白上衣＋牛仔迷你裙、逆光。 | 橫式款在夏日上午的岩岸海灣、向日葵黃馬甲短上衣＋低腰迷你裙、正面全身；這款在河濱草地、白上衣＋牛仔迷你裙、逆光。 |
| 交叉引用（已接受套數的比較文字，不是服裝場景表情） | sets[V-luna-tanaka].vs_other | 橫式款是室內和室、象牙白緞面、席地坐；這款是戶外庭院、綠色馬甲洋裝、站姿全身。 | 橫式款是室內當代日式旅宿、香檳色緞面、榻榻米上慵懶斜坐；這款是戶外庭院、綠色馬甲洋裝、站姿全身。 |
| 過時規則 | photo.rules[0] | Rin 的及地長禮服蓋住雙腳，她的坐姿全身下緣寫在禮服下襬下方。 | （刪除：R4 起 V-Rin 改為港灣膝上，不再有及地長禮服） |
| 撤回策略 | execution.model.multi_stage | 不規劃多階段（先生成再換臉、外擴、放大）。若首批發現橫直兩張服裝差太多，才考慮把第一張當唯一的參考圖餵第二張——這可能把構圖或身分一起帶過去，要另外測、另外批准。 | 不規劃多階段（先生成再換臉、外擴、放大）。H／V 本來就是兩套獨立的服裝與場景，兩張只需要共同維持人設身分（同一個 Soul 與身分句）與設定身材；不得為了讓服裝或環境相同而把一款的成品當參考圖餵給另一款。任何未來使用參考圖的方案都要另外提出、另外批准，本輪不執行。（R5 撤回先前「橫直服裝差太多就把第一張當參考圖餵第二張」的寫法。） |
| 已接受妝感中英同步（主管核可） | sets[V-iris-chen].prompt | （身分句後、She wears 前無妝感句） | Fresh, light everyday makeup with a natural lip colour. |
| 已接受妝感中英同步（主管核可） | sets[H-coco-wu].prompt | （身分句後、She wears 前無妝感句） | Sweet, light makeup with a pink lip. |
| 已接受妝感中英同步（主管核可） | sets[V-coco-wu].prompt | （身分句後、She wears 前無妝感句） | Sweet, light makeup. |
| 印刷措辭 | sets[*].frame.fit（H 12 套、V 12 套共用的兩段文字） | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。；直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 | 橫式款建議用「大照片」框（約 1.85:1）：比例上 16:9 只需上下共裁約 4%（高度 4 mm）；人物是否完整要用實圖套框確認。若橫式款最後改用半版直幅框，16:9 要裁掉約 62% 寬度，不建議硬裁，要另外規劃直幅照片。；直式款建議照片區至少 3:4：3:4 照片放進 3:4 框在比例上可完整使用。若最後選近方形框（約 0.94:1），3:4 原圖高度要裁掉約 20%（比例事實）；裁在哪裡、會不會切到髮頂、腳或其他部位，要看實圖與裁切位置，不是必然。 |
| 印刷措辭 | printing.fit.H.crop | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 比例計算：高度共裁 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm（各約 1.9%），實際分配依實圖 |
| 印刷措辭 | printing.fit.V.crop | 不裁切 | 比例計算：不裁切 |
| 印刷措辭 | printing.note | 以下分成「已知」「假設」「未知」。已知值來自廠商編輯器設定與商品頁（R1 查證，本輪只重讀既有證據、沒有重查網站）；假設值是本案為了規劃先定的數字，不是廠商規格；未知要等廠商回覆或實際打樣。只有構圖方框不代表印刷安全。 | 以下分成「已知」「假設」「未知」。已知值來自廠商編輯器設定與商品頁（R1 查證，本輪只重讀既有證據、沒有重查網站）；假設值是本案為了規劃先定的數字，不是廠商規格；未知要等廠商回覆或實際打樣。只有構圖方框不代表印刷安全。印刷數字再分成四類：已知尺寸、比例計算、prompt 規劃目標、生成後待驗證；表中的髮頂留白、腳下留白與「套框後約 x%」都是依規劃構圖推算的理論／規劃預估，不是實圖量測。 |
| 印刷措辭 | printing.categories | （無） | 新增四類說明 |
| 印刷措辭 | printing.rules | （無） | 限制：線圈／裝訂區 12 mm 是假設；16:9 實際輸出尺寸未知；300 ppi 是本案工作目標，不是已確認的廠商最低標準。 |
| 印刷措辭（並更正比例數字） | printing.compare[橫 A 半版] | 16:9 橫幅照片不適用（要裁掉約七成寬度），必須另拍直幅——不從 16:9 硬裁。 | 比例計算：16:9 照片要裁掉約 62% 寬度才放得進這個直幅框（原文誤寫「約七成」），所以不建議從 16:9 硬裁，要另外規劃直幅照片。 |
| 印刷措辭 | printing.compare[直式統一框] | 3:4 照片上下共要裁掉 32 mm（20%）：大腿中段以上會切到髮頂或腿、全身會切到腳——12 套直式款都要重排構圖。 | 比例計算：3:4 原圖放進 120×128 要裁掉高度 20%（160→128 mm）。裁在哪裡、會不會切到髮頂、腳或其他部位，要看實圖與裁切位置，不是必然；直式款可能要重新規劃上下留白。 |
| 印刷措辭（並更正數字） | printing.iris_first.answer | 不需要構圖微調：直式 3:4 照片放進暫定的 3:4 框不裁切，髮頂留白約 7%、下緣在大腿中段，人物置中、雙手都在框內；prompt 不改。 | 依暫定 3:4 框與規劃構圖，暫無須為印刷調整 V-Iris 的拍攝方向：3:4 照片放進 3:4 框在比例上不裁切；髮頂留白約 8%、下緣在大腿中段、雙手在框內是 prompt 規劃目標，不是實圖量測（R4 文字誤寫髮頂約 7%，依逐張表更正為約 8%）。 |
| 印刷措辭 | printing.iris_first.condition | 前提是直式採 3:4 照片框。若 Penny 最後選 R3 的直式統一框（120×128，約 0.94:1），3:4 照片上下要共裁 20%，這張的髮頂與下緣都會被切到，需要重排構圖；所以建議在 M-4 首試前先確認直式照片框。 | 前提是直式採 3:4 照片框。若改用 R3 直式統一框（120×128），3:4 原圖高度要裁掉 20%（比例事實）；會不會切到髮頂、手或下緣，要看實圖與裁切位置，可能需要重新規劃留白——所以建議 M-4 首試前先確認直式照片框。 |
| 印刷措辭 | printing.iris_first.verify | 首試出圖後要用實圖確認：實際像素（預期 1536×2048）、髮頂與雙手是否在框內、有效 ppi（120 mm 寬約 325 ppi）。 | 首試出圖後用實圖確認：實際輸出像素（預期 1536×2048，以實際輸出為準）、套框後髮頂與雙手是否在框內、有效 ppi（若 1536 px／120 mm 約 325 ppi；300 是本案工作目標，不是廠商已確認的最低標準）。 |
| 印刷措辭 | printing.accepted_impact.summary | 8 套已接受的企劃內容都不需要為印刷改動；H-coco-wu、H-rainie-hsu 是橫式膝上，放入框後下緣會再往上移約 2–3 cm，生成後若接近膝蓋，4 mm 的裁切改由頭頂留白多取——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。 | 依暫定框與規劃構圖，8 套已接受暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。H-coco-wu、H-rainie-hsu 是橫式膝上：套框後下緣理論上會往上移（依規劃構圖估算約 2–3 cm），若實圖接近膝蓋，4 mm 改由頭頂留白多裁——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。 |
| 印刷措辭 | composition.recommend[H] | 暫定照片框：橫式大照片框 192×104 mm（畫布 6,14–198,118）。生成用 16:9（原生尺寸未知）：放入後上下各裁約 2 mm。版面待 Penny 定案，見「印刷構圖」。 | 暫定照片框：橫式大照片框 192×104 mm（畫布 6,14–198,118）。生成用 16:9（原生尺寸未知）：比例上要裁掉高度 4 mm，規劃上下各約 2 mm。版面待 Penny 定案，見「印刷構圖」。 |
| 印刷措辭 | composition.recommend[V] | 暫定照片框：直式 3:4 框 120×160 mm（畫布 12,16–132,176）。生成用 3:4（原生 1536×2048，已知）：放入不裁切、約 325 ppi。版面待 Penny 定案。 | 暫定照片框：直式 3:4 框 120×160 mm（畫布 12,16–132,176）。生成用 3:4：比例上不裁切；若輸出 1536×2048，約 325 ppi（比例計算，以實際輸出為準）。版面待 Penny 定案。 |
| 印刷措辭 | composition.eval[近方形框] | 直式款若最後用近方形框（約 0.94:1），3:4 要上下共裁約 20%：膝上變大腿以上、全身會切到腳。所以建議直式款的照片區至少 3:4。 | 直式款若最後用近方形框（120×128，約 0.94:1），3:4 原圖高度要裁掉約 20%（比例事實）；會不會切到髮頂或腳要看實圖與裁切位置。所以建議直式款的照片區至少 3:4。 |
| 印刷措辭 | composition.eval[人物大小] | 避免人物縮小到背景裡：全身與坐姿的人物佔畫面高度約 85%（斜躺的 Rin 佔畫面寬度約 87%）；裁切景別保留完整髮頂、上緣約 4–10% 留白。 | 避免人物縮小到背景裡（以下是 prompt 規劃目標，不是實圖量測）：全身與坐姿的人物佔畫面高度約 85%（斜躺的 Rin 佔畫面寬度約 87%）；裁切景別保留完整髮頂、上緣約 4–10% 留白。 |

## 3. 未改動的證明（程式比對）

- 24 套 ID、順序、8 套已接受／16 套待決與 R4 相同；兩本月份人選與排序與 R4 相同。
- 每套欄位與 R4 逐一比對：只有印刷文字（print、frame.fit）、已接受 3 套的 prompt＋r5、V-iris／V-luna 的比較文字有變；16 套待決的 prompt 與攝影七欄位與 R4 逐字相同。
- 已接受 3 套：新 prompt＝R4 prompt 在身分句後插入核可的那一句，其他字元相同；服裝、場景、表情、姿態、攝影、身分句不變。
- 既有瀏覽器回饋：部署前在線上 R4 頁（4f15917）用測試瀏覽器實填 v5 回饋（4 套選擇、2 則備註、印刷題＋備註、整體備註）與素材頁確認；部署後同一個瀏覽器打開線上 R5 頁：兩筆 localStorage 位元組相同、選擇與備註原樣、仍是「修訂已回覆 4／16」、素材頁仍顯示已確認、開頁不改寫（8/8）。這是測試瀏覽器，不是 Penny 的瀏覽器；頁面程式不清除、不覆寫、不把舊回饋轉成核准。

## 4. 驗證

| 項目 | 結果 | 檔案 |
|---|---|---|
| R5 驗收（資料一致性、措辭、prompt 差異、比例計算、桌機＋390px 顯示、既有回饋保留與繼續填寫、無水平溢出、無 JS 錯誤） | 線上 70/70（本機 70/70） | /home/user/Virtual_KOL_Studio/review/calendar/m3_r5/live_r5_tests.tsv |
| 部署前後回饋保留（真實瀏覽器設定檔） | 8/8 | /home/user/Virtual_KOL_Studio/review/calendar/m3_r5/live_upgrade_r4_to_r5.tsv、/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/seed_v5_before_deploy.json |
| 線上檔案 sha256 與本機比對 | 666 檔不符 0；四個 HTML 頁與本機相同（9434b83） | /home/user/Virtual_KOL_Studio/review/calendar/m3_r5/live_bytes_check.txt |
| 網站建置器 --check | PASS 654 檔；ASSET_MANIFEST 不變 | — |
| CAL_18 產生器 --check | PASS；第一行為 R5；CAL_19 位元組不變 | — |
| kol-catalog 首頁 | 與存檔相同（44801 bytes） | /home/user/Virtual_KOL_Studio/review/calendar/m3_r5/live_bytes_check.txt |

測試中修正（照實記錄）：建置器新增的檢查一開始寫太寬（更正後的說明本身引用了被撤回的句子），改成只擋舊句開頭；那次建置中途失敗，暫時刪掉的 Aaliya 縮圖在下一次成功建置時重新產生，ASSET_MANIFEST 不變。R5 測試抓到 24 套 frame.fit 仍寫「全身會切到腳」「人物完整」，一併改成比例事實與條件句。

## 5. 仍未確認（不在本輪處理）

- 版面與照片框（橫式大照片框、直式 3:4 框都是暫定）待 Penny 定案；實際線圈與裝訂區、廠商 ppi 門檻、16:9 實際輸出尺寸、色彩都未知。
- 16 套修訂待 Penny 回饋；V-Iris 首試費用與生成未授權，不執行 M-4。

## 6. 檔案（完整路徑）

- `/home/user/Virtual_KOL_Studio/docs/calendar/data/cal_m3_shoot_plan.json`（r5.changes 有全部舊／新文字）
- `/home/user/Virtual_KOL_Studio/docs/calendar/CAL_18_M3_SHOOT_PLAN.md`（§0b 差異）
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/after_r5_H-iris_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/after_r5_feedback_section.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/copy_example_existing_v5_feedback.txt`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/desktop_card_H-iris_with_v5_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/desktop_card_V-iris_sync.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/desktop_cost_multi_stage.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/desktop_feedback_preserved.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/desktop_months_why.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/desktop_print_section.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/desktop_r5_decisions.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/desktop_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/live_bytes_check.txt`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/live_r5_tests.tsv`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/live_upgrade_r4_to_r5.tsv`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/local_r5_tests.tsv`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/mobile390_card_H-iris_with_v5_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/mobile390_card_V-iris_sync.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/mobile390_cost_multi_stage.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/mobile390_feedback_preserved.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/mobile390_months_why.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/mobile390_print_section.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/mobile390_r5_decisions.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/mobile390_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r5/seed_v5_before_deploy.json`

## 7. 操作紀錄

| # | 動作 | 性質 |
|---|---|---|
| 1 | 定向讀企劃資料的月份、交叉引用、執行、構圖、印刷段落，與企劃頁、建置器、CAL_18 產生器；沒有掃描整個 repo | 唯讀 |
| 2 | 在線上 R4 頁（4f15917）用測試瀏覽器設定檔實填 v5 回饋並在素材頁按確認，存下部署前狀態 | 只在測試瀏覽器 |
| 3 | 以腳本從 4f15917 套用 R5 修改（逐處比對舊值）；更新頁面、建置器、CAL_18 產生器；建置與 --check；本機測試 | 本機 |
| 4 | commit 9434b83、push；Railway 只把 cal2027-decision 固定到 9434b83（d2d5674f-b4ed-4c24-aee2-8dd5c7234724） | 其他 service 未動 |
| 5 | 部署後回饋保留驗證、R5 驗收、檔案比對、截圖、讀 kol-catalog 首頁 | 唯讀 |
| 6 | 寫本送審紀錄並 commit、push | — |

**本輪數字：** 生成 0、credits 0、訓練 0、上傳 0、Higgsfield 呼叫 0、報價預檢 0、聯絡廠商 0。
