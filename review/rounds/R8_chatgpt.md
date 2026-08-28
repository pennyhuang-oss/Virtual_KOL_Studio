# R8 — ChatGPT 覆核回覆（2026-08-29）

> 原文封存。處置見 [`../LEDGER.md`](../LEDGER.md)。
> 20 列語意覆核：19 列無異議（已記入 `pilot/semantic_review.json`）、`nico_c04` 一列 P0。
> C-29／C-30 結案；C-27 拆為 C-31／C-32（persona #2 gate）；新開 C-33。

## ChatGPT R8 覆核回覆（2026-08-29）

### 一、§7 所有 🔵 項目

| ID | 判定 | 理由 |
|---|---|---|
| C-27 | **不同意結案** | `relation`／`object_ref`／`laterality` 已封住同義詞、第三手與鏡像左右的大部分漏洞；但 `zone` 仍是作者自填，且 `background` 幾乎成為永遠可見的通行證。機器目前只能驗宣告是否自洽，不能驗 zone 宣告是否為真；見 C-31、C-32。 |
| C-28 | **不同意結案** | c05 的雙髮夾已修；c04 的 scene 與 wet hair 也對齊，但原本的 `expression=just_woken_blank` 沒同步改，與「剛洗完澡」再次衝突。見 C-33。 |
| C-29 | **同意結案（本輪 8 列內容層）** | 原先裁切外的 props／hands 已換到可見區，c02 改 knee_up、c05 改腰線以上動作，實際內容修正到位。zone 機制的通用繞過風險另列 C-31。 |
| C-30 | **同意結案** | c07 已改成非人體形狀的甲片展示棒，右手改拿上膠筆，scene／hands／props 現在能完成同一動作。 |

### 二、結構化設計裁決

四個原漏洞的處置：

1. **同義詞繞過**：`object_ref` 引用 prop ID，已關閉。
2. **單一手槽塞多個動作**：`state` enum＋單一 `object_ref` 已大幅關閉；但複數物件聚合仍有 C-32。
3. **可見性關係**：`relation + zone + expected_visible` 提供了機器稽核所需欄位，但作者可自行宣告 zone，尚未完全關閉。
4. **鏡像左右不明**：`laterality=subject_anatomical` 已關閉。

#### C-31｜P1｜作者自填 zone 是新的繞過路徑

讓 zone 依實際姿態調整是必要的；蹲姿的地面紙箱確實可能落在 knee zone，不能硬套站姿公式。但若 validator 只做「framing 是否允許作者填的 zone」，作者可把任何裁切外物件改標成 `chest` 或 `background` 後通過。

尤其 `background` 目前沒有畫面區域資訊，face_closeup 也能無條件接受 background；這無法證明該背景物真的在構圖內。

建議：

- zone 必須加入 `basis = body_relative | frame_relative | environment`；
- held prop 的 zone 必須由 hand 的 `hand_zone` 推導，不能兩邊各自填；
- surface prop 需有 `support_surface` 與 `frame_region = foreground_lower | midground | background_left | background_right | background_center`；
- `background` 不再是單一萬用 zone，必須指定 frame_region；
- zone／frame_region／姿態任何一項改動，都必須讓 semantic-review hash 失效；
- `expected_visible=false` 的物件不得計入「每張至少兩個微物件」。

因此，自由度可以保留，但只能作為**待人審核的姿態描述**，不能單憑作者宣告就自動 PASS。這是 P1，因為現有人工 20/20 gate 仍能擋住 Nico；persona #2 前應完成。

#### C-32｜P1｜hands 尚未涵蓋 wardrobe carry state 與「一個 ID 代表多物件」

仍有兩個結構缺口：

- outfit 自帶的托特、書包、皮革包等可能占用手、手肘或肩，但目前 hands 只引用 props，不會稽核 wardrobe item 的攜帶方式。建議 outfit carry item 也有 ID 與 `carry_relation = shoulder | crossbody | hand_left | hand_right | placed`，並納入手部占用。
- c11 的 `hand_creams` 是一個 prop ID 代表兩罐實體物件，兩手共同引用；這和 c10「同一團衣物由雙手抱」在機器上長得一樣。應增加 `quantity`／`unit_refs`，或拆成 `cream_left`、`cream_right`。購物籃掛手肘也不宜標 `worn`，建議新增 `carried_arm`。

這些目前沒有造成 c11 的物理矛盾，但會讓通用 validator 混淆「雙手持同一物」與「每手各持一物」。

### 三、20/20 九欄語意覆核

#### 有問題的 shot

- **`nico_c04` — P0**：scene 已改為「剛洗完澡坐在床邊」，hair_06 的滴水濕髮因此成立；但 `expression` 仍是 `just_woken_blank`。這是從「剛醒」版本遺留的狀態，與現行場景不一致。請改為 post_shower_neutral／tired_relaxed 等與剛洗澡相容的表情，並同步更新 prompt 與 semantic hash。

#### 無異議

`nico_a01`、`nico_a02`、`nico_a03`、`nico_a04`、`nico_a05`、`nico_a06`、`nico_a07`、`nico_a08`、`nico_c01`、`nico_c02`、`nico_c03`、`nico_c05`、`nico_c06`、`nico_c07`、`nico_c08`、`nico_c09`、`nico_c10`、`nico_c11`、`nico_c12`。

以上 19 列的 scene／outfit／hair／framing／view／eye_gaze／body_pose／props／hands／light，在本檔披露的內容下可同時成立。背景 props 的「是否真的被構圖納入」仍需由 semantic checklist 人工確認，不能只靠 `zone=background` 自動核可。

### 四、新議題

#### C-33｜P0｜c04 改成洗澡後，expression 仍殘留剛醒狀態

這是直接進 prompt 的跨欄位矛盾，也是「改一欄未同步另一欄」的同類問題。生成前修正，讓舊 semantic hash 失效後重跑。

### 五、放行判定

**目前仍不放行生成，僅剩 C-33 一項 P0。**

c04 表情修正後，如果：

1. 新資料使舊 semantic-review hash 失效；
2. 重新核對 c04；
3. 20/20 全數核可；
4. validator 以新 hash PASS；

即可開始 Nico 生成。C-31、C-32 是結構化系統的 P1，可與 Nico 生成並行，但必須在 persona #2 前完成，否則 zone 誤標、wardrobe 占手與複數物件仍可能被機器漏掉。
