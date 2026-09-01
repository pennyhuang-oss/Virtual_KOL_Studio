# 覆核請求 R1：Soul 訓練規劃（19 位）

給 ChatGPT。**尚未送出任何生成。** 請針對下列決策與未知數給意見。

---

## 使用者已親自裁定的事項（請勿推翻，只需在此前提下給建議）

1. **19 位的 identity master 已定案**，逐張經使用者核可。臉部階段結束。
2. **臉型槽不附參考圖**——19 位裡有 10 位的臉型完全由文字描述產生，沒有臉部參考圖。
   原因：附整張人像時，輸出會直接複製照片裡的真人（兩次被使用者認出是特定藝人）。
3. **好看是第一驗收條件**，排在骨相正確與可量測性之前。
4. 髮色髮型是「現階段」設定，不是永久鎖定（Soul V2 不繼承）。

---

## 現況

- `pilot/nico_pilot.json` 有一套成熟的 Phase C 規格（20 張、九欄語意 gate、配額、QA rubric、
  training endpoint preflight）。狀態是 `planned_not_generated`，從未執行。
- 本規劃沿用它的配額與 rubric，但 **Phase A/B 已被新的 identity master 取代**。
- repo 已記錄兩起相關事故：
  - **Vicky Lin（2026-07-25）**：同一文字 prompt 獨立呼叫 8 次 → 8 個不同的人。
    修正流程是用 Reference Element 錨定，prompt 嵌 `<<<element_id>>>`。
  - **rainie-hsu v1**：錨點只核對臉與妝、沒核對身材 → 身型與設定不符，13 張訓練圖作廢。

---

## 已對照工具 schema 確認的事實（非記憶）

- `show_reference_elements(action='create')`：吃 `medias[]`（**複數**），同步回 `element_id`；
  prompt 嵌 `<<<element_id>>>`；**支援 `seedream_v4_5`**；**不支援 Soul V2**。
- `show_characters(action='train')`：`name` + **5–20 張**，約 10 分鐘，非阻塞；
  訓練後只能配 `soul_2` / `soul_cinematic`。

---

## 規劃的五個步驟（每位）

| 步驟 | 內容 | Credits |
|---|---|---|
| C-0 | 生 2 張全身／及膝、身材可讀的候選，使用者選 1 | 2 |
| C-1 | master（臉）+ C-0 選定圖（身材）**兩張**建成一個 Element | 未知 |
| C-2 | 20 張訓練圖，每張嵌 `<<<element_id>>>`，只變景別／角度／表情／姿勢／場景／穿搭／髮型 | 20 |
| C-3 | 訓練前 QA（配額 + 7 條硬退件），不過不送訓練 | 0 |
| C-4 | Soul 訓練，20 張 | 約 25（估計） |
| C-5 | Phase D 壓力測試 + rubric 評分 | 6–8 |

單人 ~53–55；19 位 ~1,010–1,045；**餘額 1,348**。

**建議先做 1 位 Vertical Slice**（55 credits ≒ 全案的 5%），把下列未知數買掉再放大。

---

## 需要你回答的問題

### Q-1（最重要）Element 放兩張圖，臉 + 全身，會怎麼合成？

identity master 只有頭肩，**沒有身體**。而 rainie v1 正是死在身材沒錨定。
schema 允許 `medias[]` 多張，但沒說多張如何被合成。三個選項：

- **A**：Element 放 2 張（臉部 master + 核可的全身圖）。
- **B**：Element 只放臉部 master，身材靠每張 prompt 的文字（三圍、罩杯、骨架）撐。
- **C**：建 2 個 Element（`<<<face>>>` 與 `<<<body>>>`），同一個 prompt 嵌兩個。
  schema 明說 "Multiple placeholders per prompt OK"。

哪一個最穩？C 看起來最乾淨，但兩個 element 同時注入會不會打架？

### Q-2 20 張都嵌同一個 element，會不會把 element 圖的背景／服裝一起烙進去？

identity master 的背景是柔和中性灰、穿的是米色細針織上衣。
如果 20 張訓練圖都被注入這張圖，最後訓練出來的 soul 會不會**固定帶出米色針織與灰背景**？
（`soul_qa_rubric` 的硬退件表裡就有「換裝後仍固定帶出 training garment → 直接 fail」。）

若這個風險成立，要不要在 C-1 之前先把 master **去背或換背景**？

### Q-3 Phase C 的 20 張要不要保留「困難光線」？

現規格把困難光線移到 Phase D，訓練集只留 clear/well-lit（≤3 張單一頂光）。
但 Soul 之後要用在夜拍、逆光、居酒屋暖光的日常素材。
訓練集全是好光，soul 在壞光下會不會崩？還是說訓練集就該乾淨、壞光是生成端的事？

### Q-4 pilot 該挑順利路徑還是最壞情況？

- `wanyin-jiang`：黑色長直髮、無染色、身材非極端、master 最正面乾淨 → 驗流程
- `kanon-komori`：粉紫漸層 + 20 歲 + 及腰長髮 → 驗上限

repo 的前例（Nico）選的是「全批最容易失敗的組合」。但那時候是要驗**臉能不能成立**；
現在臉已經定案，要驗的是**訓練流程本身**。這個差別會不會改變選法？

### Q-5 訓練前 QA 的第 7 條夠不夠？

我加了一條「每張訓練圖都要跟 identity master 並排比對」，因為這一輪最大的失誤
就是我從來沒有把輸出跟來源照比對過。
但 20 張逐張人工比對很重。有沒有更省力又不失效的做法？

---

## 我自己看到的風險，列出來讓你評估我有沒有漏

1. **U-1 / U-2**：Element 建立與 Soul 訓練的實際 credit 都沒有確認過的數字，
   只有 repo 一句「約 25，未逐筆核對」。第一位跑完要用 `transactions` 對帳。
2. 臉型改文字之後，19 位的整體離散度變窄（最近的三位是 cheryl-soh / nanami-fujiwara /
   ruoruo-tang，都是深色長髮長卵形）。**訓練 19 個 soul 之後，這個相似會不會被放大？**
   要不要在訓練前先處理，還是訓練後再看？
3. 訓練集「不寫背景路人」是刻意的例外，訓練完必須切回。這條靠文件記著，
   沒有任何程式在擋——要不要做成檢查？

---

## REPLIES BELOW

<!-- ChatGPT 的回覆貼在這一行下面。上面的內容不要動。 -->
