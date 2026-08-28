# R6 — ChatGPT 覆核回覆（2026-08-28）

> 原文封存。處置見 [`../LEDGER.md`](../LEDGER.md)。
> 8 條同意結案；C-20/c04 不同意（Claude 已接受裁決）；新開 C-23–C-26。

## ChatGPT R6 覆核回覆（2026-08-28）

### 一、§8-1 兩個爭議點裁決

1. **C-20／c04：不同意 Claude，維持不結案。**

   前鏡頭與螢幕雖在近似同一平面，卻不是同一個視線目標：鏡頭通常在螢幕上緣，使用者「看螢幕」時視線落在預覽畫面，「看鏡頭」則是直視鏡頭／觀眾。對真人只是幾公分差距，對生圖語意卻是 `looking at phone screen` 與 `looking directly into the camera` 的差別。

   目前 `scene=低頭看手機`、`eye_gaze=camera` 仍給模型兩個不同指令。兩個可接受修法擇一：

   - 保留「低頭看手機」：改 `eye_gaze=down`，prompt 明寫看螢幕預覽；
   - 保留 `eye_gaze=camera`：scene 改成「剛醒坐在床邊，用前鏡頭自拍，低著頭直視鏡頭」。

   移除 props 裡的手機是正確修正，但沒有消除 gaze 衝突。

2. **C-22／c03：同意 Claude，不必改。**

   `filter=none`，門口晨光、冷白天花燈與不鏽鋼桌面局部 specular reflection，確實是台灣早餐店常見的物理混光，不等於風格化。現在文字也沒有把 specular 寫成柔和填光。c12 的動態車頭燈＋CCD 已移除後，C-22 可結案。

### 二、§7 所有 🔵 項目

| ID | 判定 | 理由 |
|---|---|---|
| C-07 | **同意結案** | 舊的 8/19、42%、7 anchors 與手寫成本已移除；現行 6/20、30%、8 anchors、52–54 renders 前後一致。 |
| C-08 | **同意結案** | benchmark 的 ground truth、persona adaptation、最低分聚合、replicate 與動態成本均已封口。新的場景測試充分性另列 C-25。 |
| C-17 | **同意結案** | 已不再假裝所有欄位只變一項，而是把 primary、必要連動與真正固定欄位拆開，方法論成立。 |
| K-01 | **同意結案（機制層）** | 未完成語意覆核現在會 HARD FAIL exit 1，hash 過期亦會失效。實際 20/20 內容核可仍受 C-23、C-24 阻擋。 |
| K-04 | **同意結案** | outfit_02 已改成可在公園成立的帆布鞋＋薄開襟外套；a08 的 profile_right 缺口也確實補上。 |
| C-19 | **同意結案** | 0/20 不再 warning 後仍 PASS，而是明確 non-zero HARD FAIL。 |
| C-20 | **不同意結案** | c01、c08、a08 已修正；c04 仍有上述 scene／eye_gaze 衝突。 |
| C-21 | **同意結案** | fixed baseline 已補 framing／yaw／pose／camera；st05、st08b 的主變量也已真正編碼。三欄模型能區分「被測變量」與「為量測而必須連動的變更」，render 預算亦已改為 26–27／52–54。 |
| C-22 | **同意結案** | 接受 c03 現況；c12 已移除造成 cinematic treatment 的動態車頭燈與 CCD。 |

**C-21 稽核邏輯判斷**：目前沒有看見概念漏洞。完整實作需維持三個不變量：

1. 每個相對 baseline 的實際差異，必須恰好落在 `primary_test_variable ∪ required_measurement_changes`；
2. 宣告為 required change 的欄位必須真的不同，不能用理由字串認領一個未變欄位；
3. `held_constant_fields` 必須由完整可比較欄位全集反算，不能讓作者靠漏列欄位規避檢查。

本檔描述的「validator 反算」若同時滿足以上三條，C-21 可維持結案。

### 三、20 張語意逐列覆核

#### 有問題的 shot

- **`nico_c04` — P0**：`scene=低頭看手機` 與 `eye_gaze=camera` 仍是兩個視線目標。其餘已披露欄位（outfit_08、hair_06、waist_up、selfie_front、seated、晨間窗光）可同時成立。
- **`nico_c12` — P0**：第三光源已改為「月台廣告燈箱的暖白光」，filter 也改為 none，但曝光取捨仍寫「**車頭燈那側過曝**」。車頭燈已不存在，light 內部仍是舊新版本衝突；應改成廣告燈箱側／肩線高光略過曝，或刪除該過曝描述。

#### 就本檔已披露的八欄無異議

`nico_a01`、`nico_a02`、`nico_a03`、`nico_a04`、`nico_a05`、`nico_a06`、`nico_a07`、`nico_a08`、`nico_c01`、`nico_c02`、`nico_c03`、`nico_c05`、`nico_c06`、`nico_c07`、`nico_c08`、`nico_c09`、`nico_c10`、`nico_c11`。

> 這裡不能寫成完整「九欄無異議」，因為本檔沒有披露任何一列的 props；見 C-23。上述判定只涵蓋 scene／outfit／hair／framing／view／eye_gaze／body_pose／light。

### 四、新議題

#### C-23｜P0｜自給自足覆核檔缺少 20 列 props，九欄語意 gate 無法完成

§8 明確要求逐列判斷 props，但 §5-5 表格沒有 props 欄，後面的五段光線也沒有列 props。整份檔案只提到 schema 的空 props 對抗測試，沒有提供 20 張各自的實際微物件。

因此在不違反「只讀這一檔」的前提下，審閱者不可能判斷：

- 道具是否與 scene／framing 同時可見；
- 自拍裝置是否又被當作入鏡道具；
- 雙手是否被 scene、props 與拍攝裝置重複占用；
- outfit 自帶的包／飾品是否又在 props 重複生成；
- 是否符合每張至少兩個具體微物件的 §3 規則。

**修正要求**：gen_review_file 必須在每列加入實際 props（至少兩項），或新增同源生成的 shot_id→props 表。補齊後重新送一次 20 列語意覆核；未完成前維持 HARD FAIL。

#### C-24｜P0｜c12 刪除車頭燈後仍殘留舊曝光敘述

詳見逐列覆核。這是 Claude 一貫的「改一欄、另一欄未同步」問題，且正發生在準備送進訓練集的 prompt。修正 light.exposure_choice 並使 semantic checklist hash 失效後重審。

#### C-25｜P1｜Phase D 的 no_scene_burn_in 只測訓練集已出現四次的 park

`st06` 是唯一適用 `no_scene_burn_in` 的測項，但它的 location 是 park；Phase C 已有 park×4，而且全部是 clean anchors。這能測戶外泛化，卻不是「訓練集沒教過的場景」，對固定背景烙印的檢出力偏弱。

建議把 st06 改成訓練集未出現、但普通且不帶角色招牌世界的場景，例如 supermarket、bus_stop、parking_garage 或 car_interior_parked；或保留 park 測戶外泛化，再新增一個 unseen-location shot 專門評 `no_scene_burn_in`。這項可與 Phase A/C 生成並行，但須在 Soul QA 前完成。

#### C-26｜P2｜outfit_04 仍未真正符合「服裝五層」

outfit_04 的「包／外套」欄填的是灰色及膝襪。襪子是下身配件，不是包或外套；c05 雖然在物理上成立，卻未符合 §3-4 的五層規格。建議把及膝襪併入下身，另補一個能在玄關穿鞋場景成立的包或外套（例如肩背書包或短版針織外套）。

### 五、放行判定

**目前仍不放行生成。**

必須先完成：

1. C-20／`nico_c04` 的 scene—eye_gaze 裁決修正；
2. C-23：把 20 列 props 放進本覆核檔並完成真正的九欄 20/20 語意覆核；
3. C-24：修正 `nico_c12` 殘留的車頭燈曝光描述；
4. 更新資料後讓舊 semantic review hash 自動失效，再以新 hash 跑到 20/20 PASS。

C-25 可與前期生成準備並行，但需在 Phase D 前完成；C-26 為非阻擋建議。
