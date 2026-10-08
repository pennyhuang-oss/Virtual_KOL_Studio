# CAL_06 — 十二人辨識比較：A 完整頭像、B 遮髮比較（TASK-CAL-001／R2）

> R1 的 12 位是**工作名單，不是定案**。本檔只提供可目視的比較材料與既有數字，不做「辨識度通過／不通過」的判定，也**沒有建立任何新的數字門檻**。

## 1. 方法

| 項目 | 做法 |
|---|---|
| 每人幾張 | 2 張既有圖（12 主角＋wanyin、sophia、ananya、wendy 共 16 位） |
| 怎麼挑 | mediapipe FaceLandmarker（478 點）量每張的 yaw 代理值（鼻尖相對兩眼中點的水平偏移 ÷ 眼距，0＝正臉）與 roll（兩眼連線角度）；挑最接近正臉、roll 小、臉夠大的，第二張盡量取**不同拍攝批次**。這些數字只用來挑角度相近的圖，**不是辨識分數** |
| 圖源 | 原 11 位：repo 訓練圖／face_reference；Batch 3：Soul 驗證圖 V6（統一灰上衣、室內燈）＋2026-09-10 daily_v2 原圖（R2 取回） |
| 人工覆寫（4 處） | **iris**：自動挑到的第二張是 `selfie_expression_v6/E19_bite_hair`（咬頭髮遮嘴）→ 改用同批 `training_v1/06`。**yuna**：自動挑到 `face_reference/ref_02`（roll −25°）→ 改用 `soul_test_v1/selfie_02`（roll −4°）。**vicky**：自動挑到 `face_reference/01、02`（第二輪圖；`generation_notes` 記錄第二、三輪各自獨立生成、身分不一致）→ 改用已核准訓練集 `v4_anchored_08`、`_02`。**rainie／mia**：自動挑到的第一張分別是閉眼（`06_perfume`）與化妝棉遮臉頰（`10_skincare`）→ 改用下一張睜眼、無遮擋的圖 |
| A 完整頭像 | 以眼距等比縮放到同一大小，臉置中，同尺寸格子；含頭髮與服裝 |
| B 遮髮比較 | 臉部輪廓（mediapipe FACE_OVAL）以外全部填灰，邊緣羽化；同樣以眼距等比縮放 |
| 只做 | 裁切、等比縮放、遮罩。**不旋轉、不變形、不修圖、不美顏、不生成** |
| 重建 | `python3 docs/calendar/tools/build_cal_r2_faces.py --hf-dir <取回原圖資料夾>`；選圖清單 `data/cal_r2_face_pairs.json`，量測結果 `data/cal_r2_face_geometry.json` |

### 1.1 每人用的 2 張圖與角度

| 人設 | 圖 1（yaw／roll） | 圖 2（yaw／roll） |
|---|---|---|
| iris-chen | training_v1/08（−0.06／0°） | training_v1/06（+0.01／−5°） |
| kanon-komori | verify_v1/V6（+0.05／0°） | daily_v2 #026 `8e4d02cc`（−0.05／−2°） |
| luna-tanaka | soul_test_v1/04（+0.04／−4°） | pilot_b1/LG05_a（+0.07／−2°） |
| angel-chiu | verify_v1/V6（−0.01／0°） | daily_v2 #003 `080fe64f`（−0.03／−2°） |
| somi-oh | verify_v1/V6（−0.01／−3°） | daily_v2 #063 `4e54ab6b`（−0.08／−3°） |
| vicky-lin | v4_anchored_08（−0.11／−9°） | v4_anchored_02（−0.14／−10°） |
| coco-wu | training_v1/01（−0.04／+8°） | face_reference/candidate_02（−0.06／+7°） |
| mia-huang | training_v1/08（+0.04／−11°） | training_v1/06（+0.05／−14°） |
| yuna-kim | soul_test_v1/selfie_01（−0.05／−5°） | soul_test_v1/selfie_02（−0.10／−4°） |
| tammy-chou | verify_v1/V6（+0.01／+5°） | daily_v2 #071 `5b7715e1`（+0.04／+10°） |
| rin-ayase | verify_v1/V6（−0.02／−2°） | daily_v2 #051 `adcfde8a`（+0.07／−6°） |
| rainie-hsu | training_v2/08（0.00／+13°） | training_v2/04（+0.17／+15°） |
| wanyin-jiang（備選） | verify_v1/V6（−0.05／−4°） | daily_v2 #076 `3df45038`（−0.03／−7°） |
| sophia-tseng（備選） | training_v1/10（+0.05／+8°） | training_v1/12（+0.08／+4°） |
| ananya-kapoor（比較） | face_reference/ref_02（−0.07／−5°） | soul_test_v1/04（−0.10／−3°） |
| wendy-yeo（比較） | verify_v1/V6（−0.04／−2°） | training_v1/train_03（−0.01／−8°） |

## 2. 既有碰撞值（照錄，不是本輪量測）

來源：`review/soul_pilot/_screen19_v1/screen19_pairs.json`（遮髮量測，只涵蓋 Batch 3 的 19 位）；規則 C-2 門檻 ≤0.0220（`review/soul_training/RULING_collision_accepted.md`）。

| 配對（12 位中屬 Batch 3 的 5 位，全部 10 組） | 既有值 |
|---|---|
| rin ↔ kanon | 0.02302（最接近的一組） |
| kanon ↔ somi | 0.02794 |
| rin ↔ somi | 0.0296 |
| rin ↔ tammy | 0.03214 |
| kanon ↔ tammy | 0.03646 |
| kanon ↔ angel | 0.03908 |
| somi ↔ tammy | 0.04018 |
| somi ↔ angel | 0.04087 |
| rin ↔ angel | 0.04426 |
| angel ↔ tammy | 0.06861（最遠的一組） |

| 備選／比較對 5 位 | kanon | somi | angel | tammy | rin |
|---|---|---|---|---|---|
| wanyin | 0.02299 | 0.02776 | 0.04419 | 0.03382 | 0.02234 |
| wendy | 0.028 | 0.04262 | 0.05923 | 0.0241 | 0.02715 |
| miu（參考：R1 落選原因） | **0.01734** | **0.01894** | 0.0435 | 0.03383 | 0.02572 |

- 主管點名的 Angel／Tammy 在既有量測裡反而是最遠的一組；主管關心的應是兩人髮色區間相近（棕金 vs 蜜金），這是遮髮量測看不到的部分，所以仍做了目視比較（§4.2）。
- **未觸發門檻不等於辨識度已通過。** 這些數字只說明「沒有落入既有規則禁止同框的範圍」。
- **原 11 位彼此、原 11 位與 Batch 3 之間沒有任何量測**（iris／rainie、coco、mia、vicky、luna、yuna 都在這一類）。本輪也**不新建**沒有校準的數字門檻，只提供 B 遮髮圖給人目視。

## 3. 比較限制（看圖前先讀）

| 限制 | 影響 | 本輪做了什麼 |
|---|---|---|
| **姿態** | yaw 0.1 以上或 roll 10° 以上，臉型與五官比例會被透視改變。rainie 兩張 roll 13–15°、第二張 yaw +0.17；mia 兩張 roll −11／−14°；vicky 兩張 roll −9／−10° | 只等比縮放、**不旋轉**（旋轉會引入重採樣）；角度直接標在每張圖下方 |
| **妝容** | 眼線、唇色、雀斑妝會被誤讀成五官差異。rainie 粗眼線＋雀斑點、mia 紅唇＋腮紅、sophia 橘唇、vicky 小麥膚＋亮面妝 | 文字觀察時把「妝」與「骨架」分開寫 |
| **光線** | Batch 3 的 V6 驗證圖是同一個室內燈場景（最公平）；daily_v2 與原 11 位的圖光線各不相同；rainie 圖 2 有手機閃光，遮罩臉右半過曝 | 重點比較盡量用 V6 對 V6 |
| **表情** | 開口大笑（coco candidate_03、iris 圖 1）會改變下半臉輪廓 | 一致性圖保留原表情，不挑「最像」的 |
| **遮罩邊界** | FACE_OVAL 會切掉部分額頭與下顎角；瀏海重的人（kanon、luna、coco）額頭被瀏海遮住，B 圖仍看得到瀏海下緣 | 不另外修補；看 B 圖時以眼、鼻、嘴、臉頰為主 |
| **批次** | 原 11 位的 repo 圖橫跨多個生成批次（Seedream、Soul、face_reference 各輪），同一人不同批次本來就有差異 | 一致性另做（§5） |

## 4. 重點比較（觀察，不是判定）

### 4.1 Kanon／Somi／Tammy　`r2/faces/CAL_R2_focus_kanon_somi_tammy.jpg`

- **在同一場景的 V6 驗證圖上，三人遮髮後的骨架很接近**：鵝蛋臉、相近的鼻樑與嘴型、相同的灰上衣與燈光。主要差異：kanon 臉頰較圓、眼睛較大、下半臉較短；somi 眉形較清楚、下巴略尖；tammy 臉中段較長、氣質較成熟。
- 既有數字：kanon↔somi 0.02794 是三者中最近的；tammy 與兩人較遠（0.03646、0.04018）。目視印象與數字大致同方向，但數字沒有觸發門檻不代表看起來夠不同。
- **加回頭髮後差異明顯得多**（粉紫瀏海／銅橘／蜜金挑染）。誠實的結論：**這三位的區分有相當比例靠髮色、髮型與妝感承擔**——與 R1 `CAL_02` §5.2 的自評一致，也符合 repo 既有規則 C-1「髮型是身分區分要件」。
- 對桌曆的意義：三人分在 2、5、10 月，不相鄰；主視覺都保留完整髮型，不建議用遮髮或包頭造型。

### 4.2 Angel／Tammy　`r2/faces/CAL_R2_focus_angel_tammy.jpg`

- 兩人髮色同屬棕金漸層／蜜金區間。遮髮後 angel 臉較窄、顴骨較高、笑時嘴角上提明顯；tammy 臉較柔、眼距看起來較寬。
- daily_v2 圖上 tammy roll +10°，比較時要考慮角度。
- 加回頭髮：angel 是深棕到金的漸層、多半綁起；tammy 是整頭蜜金大波浪。樣張上建議 tammy 用放下長捲髮的圖（R2 已換成倉庫坐箱與頂樓黑洋裝）。

### 4.3 Iris／Rainie　`r2/faces/CAL_R2_focus_iris_rainie.jpg`

- 兩位都是黑長直，**原 11 位，沒有量測**。
- 遮髮後：iris 臉較圓、笑容寬、裸妝；rainie 下顎較立體、粗眼線＋雀斑點妝。差異**很大一部分來自妝感與表情**。
- 限制最大的一組：rainie 兩張 roll 13–15°，圖 2 還有閃光過曝 → 這組比較的可信度低於其他組。
- 對桌曆的意義：已分在 1 月與 12 月（頭尾）；若 Penny 看圖覺得太像，可用 wanyin（同為黑長直，但旗袍古典路線）或 sophia 替換其中一位（見 `CAL_02` §5.3）。

### 4.4 其他觀察

- **16 位放在一起**（`CAL_R2_faces_A_*`、`_B_*`）：ananya 最容易一眼分辨（南亞五官、深膚色）；vicky 次之（小麥膚、下顎寬）；coco、luna 靠瀏海與圓臉；mia 靠灰金挑粉髮與紅唇妝。
- **他線 headshot（觀察用，不作依據）**：`r2/faces/CAL_R2_focus_otherline_headshots.jpg` 是同帳號 2026-10-08 由**其他工作線**產生的 neutral casting headshot（統一灰背景、灰 T、頭髮後梳）。在這種統一條件下，12 位的臉看起來比本檔的 A／B 圖更相近。但這批圖**不是本任務生成、用途未知、未經 Penny 審**，部分有假介面字樣（tammy、rainie）或閉眼（vicky、rainie），能否代表各自的 Soul 也未確認 → 只記錄觀察，不作結論。

## 5. 同一人兩張以上的一致性

### 5.1 Vicky　`r2/faces/CAL_R2_focus_consistency_vicky.jpg`

- 比較用 `v4_anchored_08`、R1 直式候選 `v4_anchored_05` 與 R1 橫式候選 `v3_01_front_headshot`。
- **v3_01 明顯是不同的臉**（臉更寬、眉更粗、眼型不同）；v4 兩張一致。`generation_notes` 記錄第二、三輪圖各自獨立生成、身分不一致，v4_anchored 才是已核准訓練集。
- **處理**：R1 橫式候選作廢，改用 `v4_anchored_04_3q_headshot`（`CAL_07` §3）。

### 5.2 Coco　`r2/faces/CAL_R2_focus_consistency_coco.jpg`

- 比較用 `training_v1/01`（也是 R2 的直式替代）、R1 橫式 `candidate_01`、R1 直式 `candidate_03`、另一張既有圖 `training_v1/12`。
- 01、candidate_01、12 三張一致（齊瀏海、圓臉、笑時臉頰隆起）。
- candidate_03 的頭大幅傾斜（yaw −0.37、roll +20°）、張嘴大笑、橘色唇妝 → 遮髮後與其他三張差異最大，但主要是角度與表情造成，**不能據此判定是不同的人**；加上手機畫面與人像牆搶主角，R2 不用這張。

### 5.3 Mia　`r2/faces/CAL_R2_focus_consistency_mia.jpg`

- 比較用 `training_v1/10`（化妝棉遮臉頰，只作一致性對照）、R1 橫式 `02_gaming_chair`、R1 直式 `13_stretch_break`。
- 三張的眼型、紅唇、腮紅與灰金挑粉髮一致；R1 兩張候選角度大（roll +20°、+36°），遮髮比較的參考價值有限，完整頭像上看是同一人。
- **處理**：兩張候選保留；最終交稿前打樣看紫光色偏。

## 6. 對選角的影響（建議，不是定案）

- 12 位工作名單**不因本輪比較而更動**：沒有新的量測，既有碰撞值沒有觸發門檻。
- 但主管與 Penny 看圖時請特別留意 §4.1、§4.3：**如果認為 Kanon／Somi／Tammy 或 Iris／Rainie 太像，替換組合在 `CAL_02` §5.3；替換需要的照片已在 `r2/decisions/CAL_R2_decide_people_backup.jpg`、`_compare.jpg`**。
- 若之後要把原 11 位也納入數字量測，需要先用既有校準方法（screen19 的遮髮量測流程）重跑，而不是在本案臨時定門檻；這不在本輪範圍。
