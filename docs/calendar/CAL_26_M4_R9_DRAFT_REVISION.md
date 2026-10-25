TASK-CAL-001／M-4／R9｜底稿退回與有限收尾｜送審報告

# CAL_26 — M-4 R9 底稿退回後的修訂 prompt（提案，未執行）

> 資料：`data/cal_m4_r9_followup.json`（不含 ID）；主管結論：`data/cal_m4_supervisor_r9.json`（逐字）；R9 底稿與 Claude 自查：`data/cal_m4_r9_draft.json`。
> **狀態：提案，待主管覆核；不是生成授權。** 本輪生成 0、修圖 0、訓練 0、付費 0、部署 0。以下是 Claude 的提案，不是主管驗收或 Penny 接受。

## 1. 主管看圖結論（摘要；原文見資料檔）

- 結論：REVISE，底稿不通過，不得送 Soul 第二步。
- 空間斷裂：三段拼接明顯，屋頂、街道與人物不是連續空間。
- 改善：背景整理、人物大小、完整雙靴與抬頭神情有改善。
- 主要失敗：主要失敗是空間斷裂，不再追加人物百分比門檻。
- 可能成因：Top／Middle／Bottom 分段描述可能造成拼接，尚未證實。
- 主管自述：主管承認前次審稿未抓出此風險，與執行端紀錄分開保存。
- 範圍：不把本次失敗概括成模型或路徑 A 無效。
- 主管自述另存：主管表示前次（R8 流程查核）審稿時沒有抓出分段描述的拼接風險；這是主管自述，另存於此，不改寫執行端（Claude）當時的紀錄。CAL_25 §5.1 的分段寫法由 Claude 撰寫。
- 狀態：主管退回底稿，Penny 未接受。唯一原圖、Claude 自查原文與扣款證據保留不改。
- 計數不變：月面照片生成 8、credits 0.96；構圖底稿生成 1、credits 2；合計 2.96。24 套完成分類不變（已接受 1、退回待重規劃 5、尚未生成 18）。

## 2. 模型名稱唯讀核對（2026-10-25）

範圍：只查本任務的送出參數與回傳、任務詳情、交易列、模型 schema 與官方說明頁；沒有讀他人作品、沒有建立測試任務、沒有聯絡支援，一次查完。

| 項目 | 結果 | 狀態 | 來源 |
|---|---|---|---|
| 請求的模型 | nano_banana_pro | 已確認 | 送出參數；送出回傳的 model 也是 nano_banana_pro |
| 交易計費名稱 | Nano Banana Pro（−2） | 已確認（歸屬本任務是依時窗推定） | 交易列 2026-10-25T13:27:20Z |
| 任務紀錄 model 欄位 | nano_banana_2 | 已確認 | 任務輪詢、任務清單、依 ID 查詢與單筆顯示四處一致；任務詳情 params 沒有另外的 model 欄位 |
| 模型 schema 與官方名稱 | nano_banana_pro＝Nano Banana Pro；nano_banana_2＝Nano Banana 2；兩者是不同 ID 與名稱；官方說明頁也列為不同模型 | 已確認；沒有找到兩者互為別名的官方對應 | models_explore get；官方說明 Nano Banana 頁（2026-09-09 更新） |
| 實際後端模型 | 未確認 | 未確認 | 唯讀資料只能確認前三項；不推測為別名，也不判定送錯。2k 3:4 報價兩者都是 2，價格無法區分；不拿他人任務比對輸出。 |

## 3. 修訂 prompt 全文（未執行）

- sha256 `3f5c858f5f8b7c1b667be5dca9cf39d8765053f04f7e4efdb654b652dee79321`；242 個英文詞（R9 為 225 個）。

```
One continuous, atmospheric winter photograph, taken from a single camera position at eye level, standing in a quiet hot-spring town lane at blue hour in gentle snowfall and looking along it with natural perspective. The lane runs away from the camera and bends gently to the left between old dark-timber inns with closed wooden lattice doors; their snow-laden eaves recede in one line under a deep-blue evening sky, and a few small plain paper lanterns glow beneath them, getting smaller into the distance. The same smooth, fresh snow covers the ground all the way from the foreground, where it is untouched, back along the lane. A 24-year-old adult Korean woman with honey-orange brown hair in a layered wolf cut, wearing a long deep-cranberry wool coat over an ivory knit mini dress and white knee-high boots, walks slowly along the lane with her hands in her coat pockets, glancing up at the falling snow with a soft smile, her face in three-quarter view. She is a modest figure a little right of centre, part of the street rather than in front of it; her whole body is visible, both boots stand on the snow, and open snow stretches between her and the camera. The nearest lantern lights her face, her coat and the snow around her with warm amber light; everything else stays cool blue. It is a quiet pedestrian lane: plain timber walls, lattice doors, lanterns and snow are all there is.
```

## 4. 相對 R9 的必要刪改與理由

| R9 原文 | 修訂 | 理由 |
|---|---|---|
| A photograph of a quiet hot-spring town lane at blue hour in gentle snowfall, seen at eye level from across the lane, with natural perspective. | One continuous, atmospheric winter photograph, taken from a single camera position at eye level, standing in a quiet hot-spring town lane at blue hour in gentle snowfall and looking along it with natural perspective. | 用一句話說明是一張連續照片，不列禁止詞。R9 同時寫「從巷道對面看」和「巷道往左退」，等於兩種視角；改成一個相機位置沿巷道看。「atmospheric winter」保留寫真氛圍。 |
| Top of the picture: snow-laden wooden eaves and a strip of deep-blue evening sky. Middle: the lane recedes to the left between old dark-timber inns with closed wooden lattice doors; a few small plain paper lanterns glow under the eaves, getting smaller into the distance. Bottom third: smooth fresh snow covering the lane, untouched in the foreground. | The lane runs away from the camera and bends gently to the left between old dark-timber inns with closed wooden lattice doors; their snow-laden eaves recede in one line under a deep-blue evening sky, and a few small plain paper lanterns glow beneath them, getting smaller into the distance. The same smooth, fresh snow covers the ground all the way from the foreground, where it is untouched, back along the lane. | 刪除 Top／Middle／Bottom 分段版面寫法（可能與三段拼接有關，未證實）；同樣的元素改成同一空間的描述：同一條巷道、屋簷連成一條往遠處退的線、同一片雪地從前景延伸到巷道深處。保留屋簷、深藍天空、木格門、小燈籠、未踩過的前景新雪。 |
| walks slowly from right to left along the lane with her hands in her coat pockets, glancing up at the falling snow, her face in three-quarter view. | walks slowly along the lane with her hands in her coat pockets, glancing up at the falling snow with a soft smile, her face in three-quarter view. | 相機沿巷道看時，「由右往左」等於橫越巷道，和沿巷道走矛盾；R9 也沒照做，行走方向不是驗收項目，所以拿掉。「with a soft smile」寫明 R9 已改善的抬頭神情，避免變得平淡。 |
| She is a modest figure a little right of centre, with the lane opening out ahead of her; her whole body is visible, both boots stand on the snow, and a wide stretch of snow lies between her boots and the bottom of the picture. | She is a modest figure a little right of centre, part of the street rather than in front of it; her whole body is visible, both boots stand on the snow, and open snow stretches between her and the camera. | 「bottom of the picture」是畫面版面用語，改成她和相機之間的空間；「part of the street rather than in front of it」表達人與街道共同構圖。「lane opening out ahead of her」依賴已拿掉的行走方向，一併刪除。沒有加百分比或距離。 |
| The nearest lantern casts a warm amber pool of light on her and on the snow around her; | The nearest lantern lights her face, her coat and the snow around her with warm amber light; | R9 臉部受光偏中性；光色設計不變，只寫明燈籠照到臉。 |
| （其餘：人物年齡與外型、服裝、「everything else stays cool blue」、最後一句背景整理） | 逐字保留 | R9 較成功的人物、服裝、配色與背景整理不動。 |

刪掉分段寫法只是避開一個可能的成因，不代表已找到確定成因。

## 5. 這次只打算驗證

- 主要：拿掉分段寫法、改成單一相機位置後，這一張是否是一個連續空間（沒有接縫，屋頂、巷道、地面與人物在同一透視）。
- 同時看 R9 已改善的部分是否保留：背景乾淨、中小人物、完整雙靴、抬頭看雪的神情、藍調與暖燈配色。
- 整張是否有寫真吸引力，不是只做到空間正確（交主管及 Penny 看圖判斷）。

不驗證：

- 身分（沒有 Soul，人物仍是替身，不是 Somi 成品）
- 第二步
- 分段寫法是否就是成因：一張沒有接縫，也只代表這一次沒有出現，不能證實成因
- 發生率（只有一張）

## 6. 尚未確認的風險

- 仍可能出現拼接、分格、白邊或頁面式版面；R8 白邊與 R9 三段拼接的成因都未確認。
- 實際後端模型未確認（任務紀錄欄位是 nano_banana_2）；結果好壞無法歸因到模型。
- 相機沿巷道看，人物可能變大、置中或背對；行走方向不指定，可能變成朝鏡頭走的擺拍感。
- 前景雪地可能仍窄（不設門檻，只看圖判斷）。
- 燈籠可能仍不是臉部主光；燈籠上可能有小字。
- 輸出 1792×2400 不是精確 3:4，套框要從上緣裁 11 px（約 379 ppi）。

## 7. 下一次單張測試的設定與費用參考

- 狀態：參考，不是授權；需 Penny 另行授權新增支出。
- 設定：nano_banana_pro、2k、3:4、count 1；無參考圖、無 Soul、不用 unlim、不訓練；請求 1 次、重試 0。
- 費用參考：R9 唯讀報價 2（2026-10-25）、實扣 2；舊報價不代表新增授權，送出前要重新唯讀報價並確認不超過新授權上限。
- 紀錄：送出後照 R9 記錄送出參數、回傳 model、任務紀錄 model 欄位與交易名稱。
- 停止點：不論結果都停，交主管及 Penny 看圖；不送第二步、不重試、不修圖、不拼接補救。

## 8. 必要閱讀清單

- `docs/calendar/data/cal_m4_supervisor_r9.json`（主管結論逐字）
- `docs/calendar/CAL_26_M4_R9_DRAFT_REVISION.md`（本文件）
- `docs/calendar/data/cal_m4_r9_followup.json`（模型核對、修訂 prompt、驗證範圍與風險的資料版）
- `docs/calendar/data/cal_m4_r9_draft.json`（R9 底稿 Claude 自查，保留不改）
- `review/calendar/m4_r9/V-somi-oh_m4r9_draft_view.jpg`、`V-somi-oh_m4r9_draft_frame_V_120x160.jpg`（R9 底稿）
