# R5 — ChatGPT 覆核回覆（2026-08-28）

> 原文封存。處置見 [`../LEDGER.md`](../LEDGER.md)。
> 8 條同意結案；C-07 / C-08 / C-17 / K-01 / K-04 不同意結案；新開 C-19–C-22。

## ChatGPT R5 覆核回覆（2026-08-28）

### 一、§7 所有 🔵 項目的結案判定

| ID | 判定 | 理由 |
|---|---|---|
| C-07 | **不同意結案** | §5-7「已知風險」仍寫舊值 `8/19、42%、7 anchors`，但 §5-6 現值是 `6/20、30%、8 anchors`；Retroactive Benchmark 又寫成本 `2×13=26`，但 replicate 政策使每個 soul 最多實際生成 27 張、兩個 baseline 最多 54 張。衍生統計漂移仍存在。 |
| C-08 | **不同意結案** | ground truth、persona adaptation、最低分聚合與 replicate 原則已補到位；但實際 Phase D 仍未完全做到單一變量，且成本／實際 render 數不一致。須連同 C-21 修正後再結案。 |
| C-09 | **同意結案** | 依本檔所附規則與對抗測試，A/B/D 的結構 gate 已覆蓋先前缺口；語意層另由 K-01／C-19 處理。 |
| C-13 | **同意結案** | 已移除 `2mm`，改為相對可視描述，並補兩個不依賴左右方向的 marker。 |
| C-14 | **同意結案** | 已有機制性 blocked status、validator hard fail 與 known-issues report，不再只是文件宣告。 |
| C-15 | **同意結案** | 已補完整頂層 schema、`$ref`、required／enum／minItems／additionalProperties／ID 唯一性，且附 4/4 schema 對抗測試。 |
| C-16 | **同意結案** | a01/a02 已改為 `seated`，原問題修正到位；其他新語意矛盾另列 C-20。 |
| C-17 | **不同意結案** | 資料結構已進步，但表內多列仍同時改 framing、pose、location、light 或 camera，與「唯一變量」宣稱不符；見 C-21。 |
| C-18 | **同意結案** | signature／career 已拆成各自 override，quota 改算 effective value，原繞過路徑已封。 |
| K-01 | **不同意結案** | 目前語意覆核是 **0/20**，validator 卻仍輸出 `✓ 全數通過`。若這真是生成前 gate，未完成時必須 non-zero exit／HARD FAIL，不能只是 warning；且本輪仍抓到多個真實矛盾。 |
| K-02 | **同意結案** | 主導穿搭已降到 25%，工作室三張的 location＋outfit＋hair 四重綁定已拆開。 |
| K-03 | **同意結案** | 全體 30%、lifestyle 50%、anchor 0/8 落在 home/work，作為 pilot 可接受；後續以 Phase D 實測 scene burn-in。舊風險文字仍須依 C-07 同步。 |
| K-04 | **不同意結案** | profile_right 與第 20 張已補，但 a08 使用的 outfit_02 含「赤腳」及「外套脫下搭在椅背」，放在公園步道場景不成立。先修 a08 的 outfit／場景後才能結案。 |

### 二、新議題

#### C-19｜P0｜語意覆核尚未完成，gate 卻仍放行

目前輸出明寫：

- 語意覆核 0/20；
- 生成前必須完成；
- 最後仍是 `✓ 全數通過`。

這三件事互相矛盾。若執行端只看 exit code，就可能在 0/20 覆核時直接開始花 credit。

**修正要求**：未達 20/20、hash 過期或任一列未核可時，validator 必須 HARD FAIL 並回傳非零 exit code。完成 20/20 後再重跑，輸出才可 PASS。

#### C-20｜P0｜Phase C 仍有四個現實／結構矛盾

1. **c01**：場景是「鐵門拉下後」，光線卻是落地窗午後日光。若鐵門是店面捲門，通常會遮住主要採光；除非明寫另有未被遮擋的側窗，否則物理條件不完整。
2. **c04**：scene／pitch 寫「低頭看手機」，但 `eye_gaze=camera`。看螢幕與看鏡頭是兩個不同視線目標，identity_core 不應含衝突指令。
3. **c08**：`selfie_mirror` 需要一手拿手機，但場景同時要求一手修眉、另一手撐洗手台，三個動作只有兩隻手，無法成立。
4. **a08**：outfit_02 定義為赤腳，外套脫下搭在椅背；場景卻是在公園步道站立且沒有椅子。這張又是新增的 clean anchor，不能讓模型臨場自行忽略服裝層。

**修正要求**：生成前逐一改到 scene、view、gaze、pose、outfit 五者物理一致，更新 semantic checklist hash 後重新核可。

#### C-21｜P1｜Phase D 並非真正單一變量，render 數與成本也算錯

目前最明顯的複合變量：

- st05：相對 st00 同時改 `body_pose` 與 framing（chest_up→waist_up）。
- st06：同時改 location、自然光條件與 framing（chest_up→knee_up）。
- st07／st08：改 light 的同時也改 framing（chest_up→waist_up）。
- st08b：實際上同時改 camera／view、下打光方向與 framing。
- st10：改 outfit 的同時改 framing（chest_up→full_body）。

有些 framing 變化是為了讓被測維度可見，這可以接受，但不能再宣稱「除了 test_variable 外全部固定」。請把欄位拆成：

- `primary_test_variable`
- `required_measurement_changes`（例如為讀身材而改 full_body）
- `held_constant_fields`

另外，13 是 **test case 數**，不是 render 數。依現行 replicate：

- st00–st05：6×3＝18
- st06–st09b：6×1＝6
- st10：1×3＝3
- 每 soul 最多 **27 renders**；兩個 baseline 最多 **54 renders**，不是 26。

st09b 若條件式不執行，則應另列最低／最高成本。這項可與 Phase A/C 前置修正並行，但必須在 Soul 訓練完成前封口。

#### C-22｜P1｜五個 C 級地點足夠，但其中兩個仍被拍得偏美

地點數量與類型已足夠：早餐店、超商、洗衣店、藥妝店、月台確實有日常性；問題在視覺處理：

- **c03** 的門口晨光＋冷白混光＋不鏽鋼反射，可能被模型理解成帶電影感的早餐店人像。
- **c12** 的列車車頭燈掃過＋CCD，可能變成戲劇性月台街拍。
- c09、c10 的醜頂光／重背景，以及 c11 的貨架冷白光，較符合「不美但真實」。

不必把所有 C 級拍得難看，但至少避免五張裡有兩張被同一套「動態光＋復古濾鏡」美化。建議 c03 或 c12 至少一張改成平、雜、普通的現場光；C 級 quota 除了 location tier，也應人工檢查是否被 cinematic treatment 抵銷。

### 三、§8 三題總結

1. **🔵 結案狀態**：同意結案 8 項；不同意結案 5 項（C-07、C-08、C-17、K-01、K-04）。
2. **規格品質**：
   - 20 張的身分覆蓋在紙面上已足夠：8 clean anchors、雙側 30/60 度、左右 profile、2 張 clean face closeup、3 張 clean body-readable full-body，且造型與場景分布不再被單一組合綁死。
   - 仍有 C-20 的四個物理／結構矛盾。
   - C 級地點夠，但 c03、c12 有被美化的風險。
   - Phase D 已結構化，但仍不是嚴格單一變量，且 render 成本計算錯誤。
3. **放行判定：目前不放行生成。** 先完成 C-19、C-20 兩個 P0；兩項修完、semantic review 達 20/20 且 validator 以有效 hash PASS 後，可以開始生成。C-21、C-22 可並行處理，但必須在對應 Phase D／Phase C 圖片執行前完成。
