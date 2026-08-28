# R12 — ChatGPT 覆核回覆（Phase C 共用模板，2026-08-28）

> 原文封存。處置見 `REVIEW_PHASE_C.md` §6-1 與 [`../LEDGER.md`](../LEDGER.md)。
> C-34／C-42／C-45／C-46／C-47 結案；C-37／C-44 不同意結案；新開 C-48／C-49（皆 P0）。
> 並裁決五版身材的切分點正確，且 chest_up 不寫腰不是空缺。

## ChatGPT R12 覆核回覆

### C-48｜P0｜相機共用模板在戶外仍寫 `room`

`[[CAMERA-1]]` 的：

> Straight lens geometry: vertical lines in the room stay vertical.

仍展開到公園、街道等戶外列。C-45 已把封閉集合的 `room` 修掉，但同一個場景假設殘留在相機模板，會重新引入室內 cue。請改為跨場景成立的：

> Straight lens geometry: vertical lines in the scene stay straight and parallel to the frame edges.

或更短的 `Straight lens geometry throughout the frame.`。修正前 C-44 尚不能結案。

### C-49｜P0｜仍有三類裁切外身體／手部 cue

五版 `BODY-*` 本身已正確切分，但其他段落仍把畫面外部位帶回 prompt：

1. `[[FACING-1]]` 寫 `one hip is nearer the lens`。它用在 chest_up 的 `nico_a02／a03／a04／a05`，也用在 waist_up 的 `nico_c12`；這些 framing 都明訂 hips 在畫面外。請把朝向模板也依 framing 分版：chest/waist-up 用肩線、鎖骨與胸前地標，knee/full-body 才能用 hip。
2. `nico_a01` 是 face_closeup，動作句仍寫 `with her hands still`。即使沒描述手的位置，仍會提示模型把手納入畫面。改成 `sitting quietly, facing the camera, with her attention on the lens`。
3. `nico_a08` 是 chest_up，卻仍寫 `with her whole body ... turned`，後面又逐句描述左右手垂在身側。改成只描述可見的肩線／上半身 profile，並刪掉兩句手部描述。

這表示 C-37 的 framing 過濾尚未完全收斂；現行 lint 也應新增「可見區域外的 anatomical token」檢查，而不只檢查服裝層與 hands 欄位的正式輸出。

### 五版身材切分裁決

**切分點正確：**

- face_closeup：只寫頸部、肩部、畫面下緣可見的鎖骨
- chest_up：肩、胸、鎖骨、上臂
- waist_up：再加入腰
- knee_up：再加入下腹與 hips
- full_body：再加入 legs、身高與完整比例

chest_up 不寫 waist **不是空缺**。腰不在該畫面裡，模型沒有可見的腰身需要補；身份的腰身一致性由 waist_up／knee_up／full_body 列提供。相反地，在 chest_up 強寫腰，才會與裁切線競爭並誘發 zoom-out。

### 結案判定

| ID | 判定 |
|---|---|
| C-34 | **同意結案**：五版身材內容與切分點正確 |
| C-37 | **不同意結案**：仍有 C-49 所列裁切外 cue |
| C-42 | **同意結案**：三種 view 的封閉集合現在可成立 |
| C-44 | **不同意結案**：BODY 與服裝分層已修正，但 CAMERA／FACING 尚有 C-48、C-49 |
| C-45 | **同意結案** |
| C-46 | **同意結案** |
| C-47 | **同意結案**：戒指已改由可見手部決定，a02／a03／c07 均已補回 |

除 C-48／C-49 外，重新展開的 prompt 沒看到因刪除腰、hips、legs、鞋或裁切外手部而形成新的可見資訊空缺。

### 放行判定

**目前仍不放行生成。** 先修 C-48、C-49，再重新展開並只重審受影響的 `nico_a01／a02／a03／a04／a05／c12／a08` 與共用 `CAMERA-1` 展開結果；不需要重掃未受相關模板改動的其他欄位。
