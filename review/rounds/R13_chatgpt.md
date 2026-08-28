# R13 — ChatGPT 覆核回覆（Phase C 最終模板，2026-08-28）

> 原文封存。處置見 `REVIEW_PHASE_C.md` §6-1 與 [`../LEDGER.md`](../LEDGER.md)。
> C-37／C-48／C-49 結案；指定七列逐列覆核均無異議；新開 C-50（唯一 P0，且它同時修正自己 R12 的措辭）。

## ChatGPT R13 覆核回覆

### C-50｜P0｜`CAMERA-1` 的「平行畫面邊緣」與手持傾斜互斥

C-48 原本的戶外 `room` 假設已移除，但替代句：

> vertical lines in the scene stay straight and parallel to the frame edges

會與 `nico_c02／nico_c05` 的：

> The horizon runs very slightly off level

直接衝突。相機有 roll、地平線傾斜時，場景垂直線就不會平行畫面的垂直邊緣；「直線不彎曲」與「直線平行邊框」是兩件不同的事。

這裡也修正我 R12 提供的措辭：我當時建議的 `parallel to the frame edges` 不夠精確。請改為只描述 rectilinear lens、不鎖相機 roll，例如：

> Straight rectilinear lens geometry: architectural lines render as straight segments with natural perspective.

並讓 lint 加一條交叉檢查：`composition=slightly_tilted` 時不得出現 `parallel to the frame edges`／`vertical lines stay vertical`。修正後只需重看 `CAMERA-1` 與 `nico_c02／c05` 的展開。

### 指定七列覆核

- `nico_a01`：已移除 hand cue；face_closeup 的朝向、身材與服裝只描述可見部位，無異議。
- `nico_a02`：chest_up 使用肩線版 `FACING-1`，左手省略、右手與咖啡杯保留，戒指恢復，無異議。
- `nico_a03`：同上；站姿與 composition 不衝突，無異議。
- `nico_a04`：肩線版朝向、右手杯、裁切後服裝層一致，無異議。
- `nico_a05`：肩線版朝向、右手保溫瓶、胸上裁切一致，無異議。
- `nico_c12`：waist_up 不再提 hip，左手省略、右手悠遊卡與肩背包可見，無異議。
- `nico_a08`：已改成肩線與臉的右側 profile，兩隻裁切外的手均未展開，無異議。

### 結案判定

| ID | 判定 |
|---|---|
| C-48 | **同意結案**：戶外 `room` 問題已消失；新產生的 geometry／roll 衝突另列 C-50 |
| C-49 | **同意結案**：三類裁切外 cue 均已修正，反向測試也覆蓋原缺陷 |
| C-37 | **同意結案**：服裝、手部、戒指與解剖部位的可見性過濾現已收斂 |
| C-44 | **暫不同意結案**：身材、朝向與 framing 已修正，但相機共用模板尚有 C-50 |

除 C-50 外，指定七列與本輪展開結果未發現新的內容空缺。chest_up 不描述腰仍是正確做法。

### 放行判定

**目前仍不放行生成，只剩 C-50 一項 P0。** 修正相機幾何句並確認 `nico_c02／c05` 後，若沒有其他改動，即可結案 C-44 並放行 20 張生成。
