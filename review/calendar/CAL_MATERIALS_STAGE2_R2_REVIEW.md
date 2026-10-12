# 第二階段素材頁｜修正輪（尺度重審、Yerin 證據、措辭）送審

- **依據**：主管判定
  - Q1 REVISE：不能用廠商尺度未確認當作 owner 不能看或選照片的理由；
  - Q2 REVISE：Yerin 錯臉需並排證據；
  - Q3 PASS：縮圖先選，原圖等選中後再定向取回。
- **範圍**：只修篩選與覆核證據，沒有擴充介面功能。roster-v1、免登入、逐人選素材流程都不變。
- **成果 commit**：`b8108eb648a46a57e3bb4dc2158cf878c23d7963`（上一版 `5cd6c23`）
- **部署**：Railway `cal2027-decision`，來源固定在 `b8108eb`，deployment `24568d40-905f-4361-b3a7-5c6e447b1cf0`（SUCCESS）
- **網址**：https://cal2027-decision-production.up.railway.app（不需登入）
- 以下驗證全部是 **Claude 自測**，不是主管的獨立驗證。

## 1. 尺度重審（Q1）

- 原先只因尺度排除的 58 張（Iris 56、Coco 2）逐張重審。
  - 先用總覽目視，再把胸部與裙下區域局部放大（原圖裁切）檢查遮蔽。
  - 沒有用資料夾名稱代替判斷。
  - `drive_v1` 的 15 張先比對 sha256：與 `daily_sexy_night_v1–v4` 的同名檔位元組完全相同，是重複檔。
- **結果：恢復 19、不發布 18、品質排除 21**（重複 18、瑕疵 3）。
- **恢復的 19 張**：非裸露、臉一致、遮蔽可確認的泳裝／內衣。
  - 新 ID 接續編號：`iris-23`–`iris-39`、`coco-20`–`coco-21`。
  - 有差異的代表圖 9 張（Iris 7、Coco 2）放在可展開的「泳裝／內衣素材參考」，其餘 10 張放「更多素材」。
  - 都可以選作橫式、直式或備選。
  - 每張卡片標「泳裝」或「內衣」，並寫：「照片選擇意向；若採用此尺度，交印前需確認廠商接受範圍。選這張不代表整本尺度已決定。」
  - 複製文字若含這類照片，會加註同一句。
  - 頁面沒有寫成禁止、違法或需要 owner 再批准才能看（自動檢查）。
  - 蕾絲半透但遮蔽可確認的，卡片註明「交印前以原圖確認」。
- **不發布的 18 張**（全是 Iris）單獨記錄，不與一般泳裝／內衣混類：
  - 蕾絲或水下透視、遮蔽範圍無法確定：3（紅色蕾絲、細蕾絲、溫泉）；
  - 疑似裸露：1（襯衫敞開、內未穿內衣）；
  - 暗示裸露：9（被子、抱枕、泡泡浴、床單、浴巾遮蔽，或裸背）；
  - 走光：1（坐姿短睡裙，裙下可見內褲）；
  - 走光疑慮：4（坐姿短睡裙裙下無法確定 1；肩帶滑落、罩杯下緣翻起 3）。
  - 上一輪已排除的 Iris 浴室檯面照（裙下可見內褲）也改歸入「走光」記錄。它不在這 58 張內。
- **品質排除 21 張**：
  - 位元組相同的重複檔 15；
  - 同套、同姿勢的近似重複 3（E16、E19 與 iris-29 同套；03b 與 iris-32 同套）；
  - 檔名標示瑕疵 3（兩張手部瑕疵、一張黑邊構圖錯誤）。
- 沒有生成、修圖、呼叫 Higgsfield 或重新下載；恢復的照片都是 repo 原圖等比縮小。

### 1.1 逐張結果（58 張）

| # | 人設 | 檔案（kols/<人設>/images/ 之下） | 結果 | 新 ID | 標註／理由 |
|---|---|---|---|---|---|
| 1 | Iris | `daily_expression_v5/04_window_glass_E1_smirk.png` | 不發布（遮蔽） |  | 疑似裸露／無法確定遮蔽：紅色蕾絲內衣透視，胸部遮蔽範圍無法確定；不發布 |
| 2 | Iris | `daily_expression_v5/05_rug_prone_E13_finger_lip.png` | 恢復 | iris-30（更多素材） | 地毯趴姿・黑色長袖上衣＋丁字褲・比噓 |
| 3 | Iris | `daily_expression_v5/expression_failed/01a_E11_bitelip_FAILED_smile.png` | 恢復 | iris-31（更多素材） | 浴室・白細肩帶背心＋黑色內褲・揮手 |
| 4 | Iris | `daily_expression_v5/expression_failed/02a_E5_suppressed_FAILED_smile.png` | 恢復 | iris-24（參考區） | 廚房檯面坐姿・白襯衫敞開＋黑色內衣褲 |
| 5 | Iris | `daily_expression_v5/expression_failed/02b_E5_partial_but_outfit_out_of_scope.png` | 不發布（遮蔽） |  | 疑似裸露：襯衫敞開、內未穿內衣，胸部側面外露；不發布 |
| 6 | Iris | `daily_expression_v5/expression_failed/03a_E12_exhale_FAILED_smile.png` | 恢復 | iris-32（更多素材） | 沙發・黑色內衣＋蕾絲內褲・雙手舉高 |
| 7 | Iris | `daily_expression_v5/expression_failed/03b_E12_exhale_FAILED_became_laugh.png` | 品質：重複 |  | 與 iris-32 近似重複（同場景、同造型、姿勢幾乎相同） |
| 8 | Iris | `daily_reel_music_r1/start_frame.png` | 恢復 | iris-28（參考區） | 百葉窗日光・床上・白色蕾絲內衣＋毯子 |
| 9 | Iris | `daily_sexy_night_v1/01_bedroom_black_lace_selfie.png` | 恢復 | iris-33（更多素材） | 床邊自拍・黑色蕾絲內衣＋灰色開襟 |
| 10 | Iris | `daily_sexy_night_v1/04_fulllength_mirror_ivory_silk.png` | 恢復 | iris-34（更多素材） | 全身鏡自拍・米白內衣褲＋白襯衫 |
| 11 | Iris | `daily_sexy_night_v2_lingerie/01_bed_black_lace_babydoll_selfie.png` | 恢復 | iris-25（參考區） | 床上自拍・黑色蕾絲內衣褲・甜笑 |
| 12 | Iris | `daily_sexy_night_v2_lingerie/02_mirror_burgundy_teddy_selfie.png` | 恢復 | iris-26（參考區） | 鏡子自拍・酒紅內衣褲＋黑絲襪＋薄外袍 |
| 13 | Iris | `daily_sexy_night_v2_lingerie/03_bathroom_pink_babydoll_selfie.png` | 恢復 | iris-35（更多素材） | 浴室鏡子自拍・粉色內衣褲 |
| 14 | Iris | `daily_sexy_night_v2_lingerie/04_lyingbed_navy_lace_bodysuit_selfie.png` | 恢復 | iris-36（更多素材） | 躺床自拍・深藍蕾絲連身內衣 |
| 15 | Iris | `daily_sexy_night_v2_lingerie/05_dressingtable_ivory_garter_selfie.png` | 恢復 | iris-27（參考區） | 梳妝台坐姿・米白內衣＋吊帶襪 |
| 16 | Iris | `daily_sexy_night_v2_lingerie/alternates/02_alt_mirror_vanitybulbs_hand_defect.png` | 品質：瑕疵 |  | 檔名標示手部瑕疵；與 iris-26 是同一套酒紅內衣的鏡子自拍 |
| 17 | Iris | `daily_sexy_night_v2_lingerie/alternates/03_alt_bathroom_hand_defect.png` | 品質：瑕疵 |  | 檔名標示手部瑕疵；與 iris-35 是同一套粉色內衣的浴室鏡子自拍 |
| 18 | Iris | `daily_sexy_night_v3_implied/01_bed_duvet_selfie.png` | 不發布（遮蔽） |  | 暗示裸露：以被子遮胸，上身是否著衣無法確定；不發布（與一般泳裝／內衣分開記錄） |
| 19 | Iris | `daily_sexy_night_v3_implied/02_prone_bareback_candid.png` | 不發布（遮蔽） |  | 暗示裸露：裸背趴姿、下身蓋床單，未見衣物；不發布（與一般泳裝／內衣分開記錄） |
| 20 | Iris | `daily_sexy_night_v3_implied/03_floor_cushion_hug_candid.png` | 不發布（遮蔽） |  | 暗示裸露：以抱枕遮胸，上身是否著衣無法確定；不發布（與一般泳裝／內衣分開記錄） |
| 21 | Iris | `daily_sexy_night_v3_implied/04_bubblebath_candle_selfie.png` | 不發布（遮蔽） |  | 暗示裸露：泡泡浴，泡沫以下未見衣物；不發布（與一般泳裝／內衣分開記錄） |
| 22 | Iris | `daily_sexy_night_v3_implied/05_window_bedsheet_wrap_candid.png` | 不發布（遮蔽） |  | 暗示裸露：以床單包裹身體；畫面遮蔽完整，但屬暗示裸身；不發布（與一般泳裝／內衣分開記錄） |
| 23 | Iris | `daily_sexy_night_v3_implied/alternates/03_alt_floor_cushion_daylight_mood.png` | 不發布（遮蔽） |  | 暗示裸露：以抱枕遮胸，上身是否著衣無法確定（同系列另一張）；不發布（與一般泳裝／內衣分開記錄） |
| 24 | Iris | `daily_sexy_night_v4_bolder/01_bed_deepv_silkslip_selfie.png` | 不發布（遮蔽） |  | 走光：坐姿短睡裙，裙下可見內褲（局部放大確認）；不發布 |
| 25 | Iris | `daily_sexy_night_v4_bolder/02_mirror_micro_lace_stockings_selfie.png` | 不發布（遮蔽） |  | 疑似裸露／無法確定遮蔽：細蕾絲內衣褲透視，胸部與下身遮蔽範圍無法確定；不發布 |
| 26 | Iris | `daily_sexy_night_v4_bolder/03_bathroom_towel_wet_selfie.png` | 不發布（遮蔽） |  | 暗示裸露：以浴巾包裹上身與下身；不發布（與一般泳裝／內衣分開記錄） |
| 27 | Iris | `daily_sexy_night_v4_bolder/04_sidelying_bareback_candid.png` | 不發布（遮蔽） |  | 暗示裸露：上身裸背、手持毛巾遮前胸；不發布（與一般泳裝／內衣分開記錄） |
| 28 | Iris | `daily_sexy_night_v4_bolder/05_window_open_cardigan_candid.png` | 恢復 | iris-37（更多素材） | 夜景窗邊坐姿・黑色平口內衣＋高腰內褲＋灰開襟 |
| 29 | Iris | `daily_sexy_night_v4_bolder/alternates/01_alt_bright_room.png` | 不發布（遮蔽） |  | 走光疑慮：坐姿短睡裙，裙下區域局部放大仍無法確定；不發布 |
| 30 | Iris | `daily_sexy_night_v4_bolder/alternates/02_alt_black_bar_framing_bug.png` | 品質：瑕疵 |  | 檔名標示構圖錯誤（左側黑邊）；與 iris-38 是同一套黑色內衣的鏡子自拍 |
| 31 | Iris | `daily_sexy_night_v4_bolder/alternates/02_alt_daylight_window.png` | 恢復 | iris-38（更多素材） | 日光鏡子自拍・黑色內衣褲＋黑絲襪 |
| 32 | Iris | `daily_sexy_night_v4_bolder/alternates/04_alt_bright_room.png` | 不發布（遮蔽） |  | 暗示裸露：上身裸背、臀部大面積外露；不發布（與一般泳裝／內衣分開記錄） |
| 33 | Iris | `dance_clone_r15/start_frame.png` | 恢復 | iris-23（參考區） | 海邊・黑色連身泳衣＋眼鏡・推眼鏡微笑 |
| 34 | Iris | `drive_v1/01_bed_black_lace_babydoll_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 35 | Iris | `drive_v1/01_bed_deepv_silkslip_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 36 | Iris | `drive_v1/01_bed_duvet_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 37 | Iris | `drive_v1/01_bedroom_black_lace_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 38 | Iris | `drive_v1/02_bathroom_wethair_mirror.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 39 | Iris | `drive_v1/02_mirror_burgundy_teddy_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 40 | Iris | `drive_v1/02_mirror_micro_lace_stockings_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 41 | Iris | `drive_v1/02_prone_bareback_candid.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 42 | Iris | `drive_v1/03_bathroom_towel_wet_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 43 | Iris | `drive_v1/03_floor_cushion_hug_candid.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 44 | Iris | `drive_v1/04_bubblebath_candle_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 45 | Iris | `drive_v1/04_lyingbed_navy_lace_bodysuit_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 46 | Iris | `drive_v1/04_sidelying_bareback_candid.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 47 | Iris | `drive_v1/05_dressingtable_ivory_garter_selfie.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 48 | Iris | `drive_v1/05_window_open_cardigan_candid.png` | 品質：重複 |  | 與 daily_sexy_night 系列同名檔位元組完全相同（重複檔） |
| 49 | Iris | `lingerie_mirror_r1/start_frame.png` | 恢復 | iris-39（更多素材） | 水泥牆房間・黑色內衣褲・鏡子自拍 |
| 50 | Iris | `onsen_bucket_r1/start_frame.png` | 不發布（遮蔽） |  | 疑似裸露／無法確定遮蔽：溫泉水中，水面下遮蔽範圍無法確定；不發布 |
| 51 | Iris | `selfie_expression_v6/E14_wink.png` | 不發布（遮蔽） |  | 走光疑慮：肩帶滑落、罩杯下緣翻起，胸下緣外露範圍無法確定；不發布 |
| 52 | Iris | `selfie_expression_v6/E15_tongue_out.png` | 不發布（遮蔽） |  | 走光疑慮：肩帶滑落、罩杯下緣翻起，胸下緣外露範圍無法確定；不發布 |
| 53 | Iris | `selfie_expression_v6/E17_cheek_squeeze_cute.png` | 恢復 | iris-29（參考區） | 床上近距離自拍・黑色內衣・戳臉頰 |
| 54 | Iris | `selfie_expression_v6/E19_bite_hair.png` | 品質：重複 |  | 與 iris-29 近似重複（同場景、同造型、姿勢幾乎相同） |
| 55 | Iris | `selfie_expression_v6/expression_failed/E16_pout_FAILED_became_smile.png` | 品質：重複 |  | 與 iris-29 近似重複（同場景、同造型、姿勢幾乎相同） |
| 56 | Iris | `selfie_expression_v6/expression_failed/E18_sultry_FAILED_became_toothy_smile.png` | 不發布（遮蔽） |  | 走光疑慮：肩帶滑落、罩杯下緣翻起，胸下緣外露範圍無法確定；不發布 |
| 57 | Coco | `dance_clone_r12/start_frame.png` | 恢復 | coco-20（參考區） | 綠色三角比基尼＋腰鏈・雙馬尾・伸手 |
| 58 | Coco | `dance_clone_r13/start_frame.png` | 恢復 | coco-21（參考區） | 紅色碎花比基尼・抓雙馬尾大笑 |

## 2. Yerin 錯臉證據（Q2）

- 比較板：`review/calendar/yerin_face_check/CAL_M1_yerin_casting_v1_vs_canon.jpg`
- 來源與 hash：`review/calendar/yerin_face_check/sources.json`
- 人寫觀察：`review/calendar/yerin_face_check/observations.json`
- 產生工具：`docs/calendar/tools/build_cal_m1_yerin_check.py`
- 內容：
  - 最上列是 identity master（2026-09-01 核准）。
  - a01–a04 每張一列，各三格：完整照片、頭部裁切、只留臉部輪廓且兩眼距離統一。
    - 只留輪廓的格子把頭髮與服裝遮成灰色。Soul V2 不繼承髮型，所以髮色不算證據。
  - 每列右側是 `training_v1` 裡姿勢最接近的一張，做同樣三種裁切。
  - 每列寫出檔名、尺寸、臉部偏轉／傾斜數值與具體觀察。
- 處理：只裁切、等比縮放、臉部輪廓外塗灰；不旋轉、不變形、不修臉。全身照先在頭部區域放大找臉，座標再換算回原圖。
- 觀察（目視，不是量測）：
  - a01–a04 彼此像同一張臉。
  - 與定案臉相比，下列各項都不同：
    - 眼型：細長上揚，對比大而圓、雙眼皮；
    - 膚色與雀斑：小麥色有雀斑，對比白皙無雀斑；
    - 臉型：顴骨與下顎較明顯，對比鵝蛋圓潤；
    - 唇形與外觀年齡。
  - 遮掉頭髮後，差異仍在。
- 板上寫明的限制：
  - a03 與對照圖方向相反、傾斜大，證據力最弱；a04 臉小；
  - 膚色可能部分來自光線；
  - 不以「早於定案」作為錯臉證明。
- 狀態：四張維持「暫不採用（待主管覆核判斷）」。
  - 剔除理由已改寫；頁面的未列出分類也改成「暫不採用（待主管覆核判斷）」。
  - 比較板不發布到素材頁。

## 3. 措辭

- **R3 清理版不再寫「完成」**。5 張一律寫「已處理……；成品質感待覆核」：
  - Iris 招牌清理版（iris-02）：「已處理；近看有失焦色塊，成品質感待覆核」；
  - Coco 手機殼清理版（coco-04）仍寫「修補不完全自然」。
- **待修項分三級**：
  - 「待修」15 張：假字、可辨識角色、假日期戳等；
  - 「構圖注意（可選清理）」32 張：背景路人、牆上本人照片、他人入鏡、雜物、閃光；
  - 「注意」64 張：其他提醒，例如臉小、低頭、低解析。
  - 背景路人與牆上本人照片不再寫成必修。
- 頁面說明加上：「選中的主照片取得原圖後，才做實際裁切與細節覆核。」
- Yerin daily 086（yerin-07）是已發布的低解析縮圖。
  - 原註記「坐姿裙下區域在縮圖上無法確認」，改為「……若選用需先取回原圖確認遮蔽」。
  - ID 與圖片不變（見第 6 節）。

## 4. 保留使用者選擇

- 現有 171 個素材 ID 的來源與分區完全不變；新照片接續新 ID，不重新編號。
- 上一版發佈的 606 個檔，新版 sha256 全部相同，所以沒有任何舊 ID 換圖。
- 新增 38 個檔：19 張預覽與 19 張縮圖。
- 瀏覽器資料的 key（`cal2027-materials-v1:<SHA>`）與格式不變，不會因為增加候選而清空。

## 5. 驗收（Claude 自測）

**升版保留**是在線上實測的：
1. 先在舊版（`5cd6c23`）用一個保存下來的瀏覽器設定檔選照片：
   - Iris：橫 iris-03、直 iris-01、備 iris-12；
   - Luna：橫直同一張 luna-02；
   - Coco：橫 coco-04（清理版）、備 coco-15；
   - Yerin：直 yerin-06（低解析縮圖）；
   - Coco 加備註。
2. 按確認，再把 Iris 改了又改回，讓 Iris 成為草稿。
3. 部署 `b8108eb` 後，用同一個設定檔開新版。

本機也用同一個 port 先跑舊版、再換新版，重做一次。結果檔：`review/calendar/materials_stage2_r2/live_upgrade_test_results.txt`（線上 46／46 PASS）、`local_upgrade_test_results.txt`（本機 46／46 PASS）。

| 檢查 | 結果 |
|---|---|
| 升版後選擇保留 | localStorage 內容與升版前位元組相同。Iris 仍是草稿；Luna、Coco、Yerin 仍是「已確認」，確認時間不變。Coco 備註、各按鈕狀態都對應原選擇。已選 ID 的縮圖檔名不變。桌機與手機各測一次 |
| 舊 ID 沒有換圖 | 上一版的 606 個發佈檔，新版 sha256 全部相同。171 個舊 ID 的來源與分區不變 |
| 新增圖片 | 卡片 190 張（171＋19）。「泳裝／內衣素材參考」只在 Iris（7）與 Coco（2）；19 張都有標籤與尺度提示；其餘 10 張在「更多素材」。所有縮圖載入，展開全部後沒有橫向捲動（1366 與 390） |
| 尺度提示 | 該區與每張卡片都寫「照片選擇意向；若採用此尺度，交印前需確認廠商接受範圍」與「不代表整本尺度已決定」。頁面沒有「禁止／違法／需 owner 再批准」字樣 |
| 選擇與複製 | iris-26 列為備選只影響 Iris；coco-20 選作直式會撤銷 Coco 的確認。複製文字裡 coco-20 註明「泳裝／內衣」，並附尺度說明與頁面版本 `b8108eb…`（範例 `live_copy_example.txt`） |
| 措辭 | iris-02 寫「已處理；近看有失焦色塊，成品質感待覆核」；5 張清理版都沒有「完成」。背景路人與牆上本人照片標「構圖注意（可選清理）」；假字仍標「待修」 |
| 免登入與資料 | 頁面、新圖片、data.js 都是 200，沒有 `WWW-Authenticate`。data.js 不含 job_id／soul_id／hf:／kols 路徑 |
| 線上檔案一致 | 不帶憑證抓 652 個檔（manifest 644＋頁面 JS／CSS），與 commit 內容 sha256 全部相同；3 個 HTML 的頁面版本都是 `b8108eb…` |
| 產生物可重現 | `build_cal_decision_site.py --check --hf-dir … --clean-dir …`：PASS，644 檔，問題 0 |
| 其他服務 | 型錄首頁與部署前位元組相同；`kol-catalog`（eabb3a25）、`897-audition`（90a81d86）的 deployment 不變 |

依指示沒有重跑與本輪無關的全部檢查（上一輪 123 項）。

截圖（線上 `b8108eb`）在 `review/calendar/materials_stage2_r2/`：
- `live_verify_top.jpg`、`live_verify-mobile_top.jpg`：頁首與進度，顯示升版後保留的選擇；
- `live_verify_iris_swim.jpg`、`live_verify-mobile_iris_swim.jpg`：Iris 泳裝／內衣參考區；
- `live_verify_coco_swim.jpg`、`live_verify-mobile_coco_swim.jpg`：Coco 參考區；
- `live_verify_iris_clean_wording.jpg`、`live_verify-mobile_iris_clean_wording.jpg`：清理版措辭；
- `live_seed_top.jpg`：升版前在舊版選的狀態。

## 6. 請主管確認

1. 恢復 19 張與不發布 18 張的分界是否同意？逐張理由見 1.1。
2. Yerin 比較板是否足以支持「臉與定案不同」？主管判斷前，四張維持暫不採用。
3. Yerin daily 086（yerin-07）是已發布的低解析縮圖，縮圖上看不清坐姿裙下。目前保留並加註「若選用需先取回原圖確認遮蔽」，沒有下架，以免改變既有 ID。是否要改成先不發布？

## 7. 實際外部操作

| 時間（UTC） | 操作 | 對象 |
|---|---|---|
| 14:19 前 | 在線上舊版（`5cd6c23`）用測試瀏覽器設定檔選照片（只寫入測試瀏覽器自己的 localStorage） | 唯讀網站 |
| 14:19 | commit 並 push `b8108eb` 到 `claude/epic-carson-n5w0qu` | GitHub（未合併 main、沒有開 PR） |
| 14:19 | `connect-service-source`：`cal2027-decision` 固定到 `b8108eb` | Railway；deployment `24568d40` SUCCESS（14:27 起服務新版） |
| 14:28–14:30 | 線上驗收：升版保留（桌機、手機）、byte 比對、免登入、型錄比對 | 唯讀 |
| 之後 | push 送審文件與截圖（只有 `review/`，不影響部署） | GitHub |

- 只動 `cal2027-decision`，沒有修改其他 service，沒有新增付費服務。變數不變（仍沒有帳密變數）。
- 沒有取回 daily 原圖、沒有呼叫 Higgsfield、沒有重新下載外部素材、沒有生成或修圖。
- 沒有花 credits、沒有聯絡廠商、沒有上傳廠商編輯器、沒有下單。
- 沒有接續 R4，沒有製作交印包。
