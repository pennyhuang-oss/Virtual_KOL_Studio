TASK-CAL-001／M-4／R13｜Somi局部身分編輯與其餘四位製作準備（第二次）｜送審報告

# M-4 R13 第二次 送審紀錄

- 固定成果 commit：`f8b894e9ac484046e9b8a80132fa11294be850cd`（起點 `0a38302`）
- 本輪：生成 0、上傳 0、送出 0、扣款 0、訓練 0、部署 0。
- 交圖：遮罩示意圖 `review/calendar/m4_r13/V-somi-oh_m4r13_edit_area.jpg`（未送出，所以沒有結果圖）。

## 主管報告

```
TASK-CAL-001／M-4／R13（第二次）｜Somi局部身分編輯與其餘四位製作準備｜Claude 執行回報

起點 HEAD：0a38302eec2282e65d411fb9e39ef1159a83f60f（未回退、未覆蓋）
成果 commit：f8b894e9ac484046e9b8a80132fa11294be850cd　紀錄 commit：本檔所在 commit（成果 commit 的下一個）
本輪：生成 0、上傳 0、送出 0、扣款 0、訓練 0、部署 0

一、Somi 局部編輯：未送出（停在送出前必要確認第 2 項）
1. 遮罩（已補正，Claude 自查）
   - 檔案：review/calendar/m4_r13/V-somi-oh_m4r13_edit_mask_1792x2400.png
   - sha256：b19057febd7f0e881a85fbbf8db343c996cfa63989bf7ebbddf11192d492a587
   - 示意圖：review/calendar/m4_r13/V-somi-oh_m4r13_edit_area.jpg；產生程式 make_mask_r13b.py（可重現同一 hash）
   - 1792×2400 灰階；範圍 x1137–1297、y856–1073，占全圖 0.63%
   - 對 R12 的調整：下緣 y1056→1073，給下顎與上頸銜接空間（下巴以下約 50 px、毛衣領口以上約 27 px）；
     左緣原本在 y≈950–990 貼到背景與外圍髮型交界，改為離背景至少 10 px；右側與頂端仍在頭髮內。
   - 範圍外：背景、外圍髮型輪廓、大衣領、毛衣領口、身體。R12 舊遮罩保留不刪。
   - 限制：左臉頰到背景只有約 20 px 頭髮，左緣離目前臉頰輪廓約 0–10 px；Somi 臉型較窄、輪廓會往內收，所以不往外擴。
2. Element 引用語法：確認。工具說明寫明 <<<element_id>>> 嵌在 prompt 內、不要放進 medias，支援 nano_banana_2。
3. 遮罩黑白定義：無法確認 → 依指示停止付費操作。
   本輪新查（都沒有黑白定義）：nano_banana_2 模型說明（只寫 is_inpaint「Whether to restrict the edit to the supplied mask.」）、
   Higgsfield 打包工作流程清單、Marketplace apps（inpaint／mask 0 筆）、官方 API 文件首頁與完整目錄、官方 OpenAPI 規格（全文無 mask／inpaint）、
   官方 SDK 頁、官方部落格 Nano Banana Pro Inpaint（2025-12-11，只寫用筆刷塗要改的區域）。
   第三方說法不一致：Hugging Face Diffusers、Astria 寫白＝編輯；Stability AI 舊版 API 相反。不能套用。
4. 上傳費用：未確認（官方沒寫；以往上傳沒有對應扣款列，屬依時窗推定）。
5. 報價：不含遮罩的唯讀報價 2 credits（R10 原任務＋Somi Element＋is_inpaint、2k、3:4、count 1、不用 unlim），已等於上限；
   含實際遮罩的完整報價未做（沒有上傳遮罩）。
6. prompt：docs/calendar/data/cal_m4_r13b_somi_precheck.json（prompt.text，佔位符版），commit f8b894e，
   sha256 3aecf30413059f311030f3f06d1fba96219594b30308db12210e7e81c1855ff0；
   與 R12 範本差異只有 young woman → adult woman；遮罩補正不需改字。填入 Element 後的版本只在私有紀錄。
7. 照片交付：沒有結果圖（未送出），所以沒有結果套框、R10／結果對照與臉部前後對照；只交遮罩示意圖。

二、其餘四位製作卡（生成 0）
- docs/calendar/CAL_27_M4_R13_NEXT_CARDS.md「R13 第二次：簡明製作卡」：吸引點、人景構圖、造型姿態、光色、prompt、流程、風險、費用。
- prompt 全文：docs/calendar/data/cal_m4_r13_cards.json，固定 commit bd84cf97a7310afa672d506895e09c8d73220408
  Tammy 9c17fe21db59b9e26d0c0793e4bfa48dc19a55d723a61f838250d8f7e7cccb2b
  Rin   fa6975f39db1eb51006004d278910b57e800243acebdfe4945e47a33723e3eeb
  Yerin 5bb8c2c7aa6ffc84a8761b44be9581e2c0a49e5253a6374ac43ccce5e7ba3ca9
  Jia   1669f5e427317092d40689aa51d7e2a33dcfecdba66f3adc1d70896093d0c2f8
- 流程：Tammy、Rin 走 Soul 2＋既有 Soul 純文字 1 次；Yerin、Jia 暫緩（遠景，等身分步驟有可用結果；Jia 沒有 Element 紀錄）。

三、下一個小批次建議（請主管覆核）
- Tammy、Rin 各 1 張，每張 0.12，合計 0.24 credits（送出前重新唯讀報價）。
- Somi 是否做遮罩編輯，等 Penny 對遮罩定義風險的決定（見四）。

四、Owner 待決
- 選項 A：接受「白＝編輯」這個未經官方確認的慣例，並決定上傳費用的處理（依以往紀錄視為 0，或上限改為 2＋實際上傳費用）
  → 上傳 1 個遮罩、含遮罩唯讀報價不超過上限才送 1 次。若定義相反，結果會是臉不變、其他地方被重畫，算失敗，不補送。
- 選項 B：Somi 先不做，先做 Tammy、Rin（0.24）。

五、計數與歷程
- 月面照片 9 張／1.08 credits；構圖底稿另計 2 張／4 credits；訓練 0。不變。24 套分類不變（只有 V-Iris 已接受）。
- V-Somi 歷程加註 R13 第二次未送出；企劃資料新增 m4r13b。

六、主管結論與 Claude 自查分開
- 主管 R12：局部編輯方向 PASS（主管結論）。
- Claude 自查：遮罩涵蓋臉型、下顎與上頸，不碰背景、衣領與外圍髮型（自查，不是主管覆核，也不是 Penny 接受）。

七、檢查：CAL_18–22 --check、CAL_23 --check（CAL_19 不變）、建置 --check。未部署、未改 V-Iris、未合併 main、未聯絡廠商。
```
