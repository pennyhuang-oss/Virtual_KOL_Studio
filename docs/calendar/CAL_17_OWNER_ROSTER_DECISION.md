# CAL_17 — Owner 名單決定紀錄（TASK-CAL-001／第二階段）

> 資料檔：`data/cal_m1_owner_roster.json`（version `roster-v1`）。決策頁的「Penny 已確認的 12 位」只依這份紀錄產生，**不依瀏覽器 localStorage**。
> 之後若要改名單，只能另建**新的草稿版本**（新的 version），不得覆寫本紀錄。

## 1. 決定內容

| 項目 | 內容 |
|---|---|
| 決定者 | Penny（owner）。在對話中明確表示「我選完了」，主管轉述為確認名單 |
| 日期 | 2026-10-12 |
| 名單（12 位） | iris-chen、luna-tanaka、somi-oh、coco-wu、mia-huang、yuna-kim、tammy-chou、rin-ayase、rainie-hsu、miu-shiraishi、jia-seo、yerin-han |
| 順序 | **不是月份順序**；月份尚未決定 |
| 相對主管原推薦 | 移除 kanon-komori、angel-chiu、vicky-lin；加入 miu-shiraishi、jia-seo、yerin-han |
| 第一階段頁面的輸出 | 選角頁複製出的文字仍標「草稿」。依主管指示，**不要求 Penny 回頁面重新確認** |
| 第一階段瀏覽器資料 | `cal2027-casting-v1:<SHA>`、`cal2027-decision-v1:<SHA>` 都保留，不刪除、不轉換；第二階段用新的 `cal2027-materials-v1:<SHA>` |

## 2. 這份確認的範圍

- **只確認 12 位人設名單。**
- 不是照片核准、不是月份核准、不是版面核准、不是印刷或廠商核准。
- 部署或頁面上的任何狀態都不等於核准。

## 3. 取消登入

- Penny 要求取消決策頁的帳號密碼，並**明確同意此展示頁公開可讀**；不另設密碼或其他存取障礙。
- 保留 `robots.txt` 全站 Disallow 與 `X-Robots-Tag: noindex`。這只是請搜尋引擎不要收錄，**不能保證**沒有人搜尋到或打開頁面。
- 公開內容只限本案展示照片與必要的選擇資料；不發布帳號資料、Soul ID、job_id、訓練集整包或內部工作紀錄。

## 4. 相似度疑慮（記錄，不否決名單）

照錄既有資料（`CAL_02` §3、§5；遮髮量測只涵蓋 Batch 3 的 19 位）：

| 配對 | 既有值 | 類型 |
|---|---|---|
| Miu ↔ Jia | 0.01219 | 落在既有同框門檻內（≤0.0220） |
| Miu ↔ Somi | 0.01894 | 同上 |
| Jia ↔ Somi | 0.01986 | 同上 |
| Yerin ↔ Rin | 0.02085 | 同上 |
| Somi ↔ Tammy | 0.04018 | R2 目視：遮髮後骨架接近，區分主要靠髮色與髮型 |
| Iris ↔ Rainie | 未量測 | 都是長直黑髮；R2 目視：差異多來自妝感與表情 |

- Iris、Luna、Coco、Mia、Yuna、Rainie 沒有既有遮髮量測；**沒有紀錄不等於不像**。
- 本輪不換人、不改人設、不重新訓練、不改 Soul ID。
- 待版面階段注意：`PERSONA_CANON.md` 原則七 C-2 規定「有碰撞關係的兩位不得同框」（同一張圖、同一支影片、同一組輪播）。上面 4 組 ≤0.0220 的配對若出現在同一面（例如 12 人格封面），就會碰到這條規則。**本紀錄只提出，不決定版面**。

## 5. 第二階段素材盤點的發現（與名單無關，但會影響選照片）

- **Yerin**：`kols/yerin-han/images/casting_v1/` 的 4 張（a01–a04）是選角前期圖，目視臉與 2026-09-01 定案的 identity master 及 Soul 訓練集（`training_v1`）不同 → 不放進素材候選。第一階段選角頁的 Yerin 卡片用的是 `training_v1` 與驗證圖，不受影響。
- **Rainie**：只有 `training_v2` 是定案臉（`CAL_02`：舊資料夾是另一張臉，不可混用）；`training_v1`、`face_reference`、舞蹈起始畫面都不放進候選。
- **Coco／Mia**：`face_reference/round1_*` 是被退回的第一輪臉部候選，不放進候選。
- 完整剔除清單與理由：`data/cal_m1_materials.json` 每位的 `excluded`。
