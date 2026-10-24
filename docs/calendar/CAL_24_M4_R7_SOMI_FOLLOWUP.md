TASK-CAL-001／M-4／R7｜主管實際看圖覆核與有限收尾｜送審報告

# CAL_24 — M-4 R7 Somi 後續單張測試方案（提案，未執行）

> 資料：`data/cal_m4_r7_followup.json`；主管結論：`data/cal_m4_supervisor_r7.json`（逐字）；R7 試拍與 Claude 自查：`data/cal_m4_r7_trial.json`。
> **狀態：提案，待主管覆核；不是生成授權。** 本輪生成 0、修圖 0、訓練 0、付費操作 0、部署 0。以下是 Claude 的提案，不是主管驗收或 Penny 接受。

## 1. 主管看圖結論（摘要；原文見資料檔）

- 結論：REVISE，不建議採用；Penny 尚未接受。配色、人景融合改善，但構圖與寫真完成度仍未通過。
- 空間配置：上方天空、屋簷與大燈籠占用大量空間，人物卻擠到底邊、靴底被切；重點是整張空間配置失衡，不能只用人物占比解釋。
- 干擾物：招牌、電線、水管與牆腳雜物干擾畫面；大燈籠及文字搶走注意力。文字不是所有照片的通用退回理由，但本張確實搶戲。
- 姿態：姿態仍偏看鏡頭站拍，沒有形成走進光中看雪的瞬間。
- 光線驗證：配色改善，但燈籠主光的落實只能標「部分有效」，不稱已可靠驗證。
- V-Somi 狀態：R5 退回；R7 主管建議退回，Penny 未接受。唯一原圖保留，不修圖、不補生、不改成已接受。

## 2. 保留的部分

- 藍調時刻與落雪
- 深蔓越莓紅大衣＋象牙白針織迷你洋裝＋白色及膝長靴（Owner 已接受的造型）
- 溫泉街雪景方向（Penny 指定保留）
- 燈籠的暖光與藍調天光的冷暖關係（R7 只算部分有效，這次改由一排小燈籠提供，不靠一盞近景大燈籠）

## 3. 畫面設計

從整張出發：上方只留一窄條屋頂與深藍天空，中段是點著小燈籠的街道與她的全身，下方留一段雪地讓雙靴完整；她站在燈光裡抬頭看雪。畫面焦點是人與落雪，不是燈籠或招牌。

| 位置 | 安排 |
|---|---|
| 上方 | 窄條屋頂與深藍天空（不讓天空、屋簷與大燈籠占去上半） |
| 中段 | 她的全身與點著小燈籠、往遠處退的街道 |
| 下方 | 她前方一段雪地，雙靴完整、靴下有雪 |
| 左右 | 左右位置不限，以平衡為準 |

**主要動作（只有一個）：** 站在燈光裡抬頭看落雪、帶淺笑、不看鏡頭。拿掉朝鏡頭走、手插口袋等互相競爭的描述。

**減少搶戲：**

- 不安排近景大燈籠：燈籠改為沿屋簷的一排小燈籠，往遠處退
- 屋面改為關著的木拉門，減少可能長出招牌字樣的平面
- 一句話排除招牌、海報、電線、水管與雜物（不再逐項寫「無字」）

## 4. 不可妥協的成品要求 vs. 可容許的變化

**不可妥協（任一項不符就退回）：**

1. 雙靴完整、靴下有雪地；120×160 mm 不裁切時腳不碰下緣
2. 整張空間配置平衡：天空、屋簷與燈籠不壓過人物，人物不擠在底邊
3. 沒有搶戲的近景大型物件、招牌文字或雜物（遠處小而不可辨讀的字不一律退回，但不得搶戲）
4. 讀得出「在燈光與落雪中抬頭看雪」的瞬間，不是正對鏡頭的站拍
5. 可辨識為 Somi、明確成年；人與街的冷暖光可信、不浮貼
6. 藍調時刻與深蔓越莓紅／象牙白／白靴的配色

**可容許變化（偏離 prompt 不等於美感失敗）：**

- 人物在畫面左右的位置與確切大小（只要符合前兩項）
- 燈籠數量、位置與大小（不在近景搶戲即可）
- 大衣開或合、雙手位置
- 臉的角度（側臉或三分之二側臉）與笑容大小
- 街道有沒有坡度、有沒有蒸氣、雪量多寡
- 相機略高或略低
- 遠處小而模糊、不可辨讀的字樣

## 5. 精簡 prompt（身分句逐字沿用；R7 的 378 字縮為 268 字）

```text
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. Light makeup with a glossy lip, her cheeks flushed pink from the cold. She wears a long deep-cranberry wool coat over an ivory ribbed knit mini dress, white knee-high boots and small pearl earrings. A quiet, wide photograph of a snowy hot-spring town street at blue hour, with snow falling softly. Low wooden inns with closed sliding doors line the street, and small warm paper lanterns glow along the eaves, receding into the distance. She stands in the middle of the street a short way from the camera, in the soft glow of the lanterns, and tilts her face up to watch the falling snow with a small smile, not looking at the camera. Framing from top to bottom: a narrow band of rooftops and deep-blue sky, then the lantern-lit street with her whole figure, then open snowy road in front of her; both boots are fully in frame with snow below them. The warm lantern glow touches her face, her coat and the snow around her, and the rest of the scene stays cool blue. Vertical 3:4, eye level, natural perspective. A clean street with no shop signs, posters, wires, pipes or clutter. Natural skin texture with visible pores, believable light that belongs to the scene, refined colour grading, finished like a page from a high-end photobook.
```

## 6. 相對 R7 刪改了什麼、為什麼

| 刪掉 | 改成 | 原因 |
|---|---|---|
| 「the nearest lantern hanging just above and in front of her toward the upper right」與「the nearest lantern is her key light」 | 沿屋簷往遠處退的一排小燈籠；暖光來自燈籠群 | R7 長出一盞近景大燈籠，占去上方空間、文字搶戲；主光也只做到部分有效。 |
| 「warm plain paper lanterns that have no lettering」「no signs, no traffic signs and no wires」逐項排除 | 關著木拉門的屋面＋一句「no shop signs, posters, wires, pipes or clutter」 | 逐項寫「無字」在 R5、R7 都沒擋住文字；改為減少會出現招牌的平面。只是假設，不保證有效。 |
| 「her figure filling a little under half the frame height」與「a 50mm lens from about 6 metres」 | 由上到下描述畫面：窄條天空與屋頂／街道與她的全身／她前方的雪地，雙靴完整、靴下有雪 | 數字描述在 R7 沒被遵守；改寫成畫面上下各放什麼，直接對應「靴子被切、上方太滿」的問題。不再加百分比門檻。 |
| 「walks slowly down the gently sloping street toward the camera with her hands in her coat pockets」 | 站在燈光裡抬頭看落雪、帶淺笑、不看鏡頭 | 朝鏡頭走＋手插口袋＋抬頭看雪三件事互相競爭，結果變成看鏡頭的走秀站拍；只留一個動作。 |
| 石溝蒸氣、道路往遠處升高、街道往左上退、上方開闊天空等構圖細節 | （不另加） | 描述太多互相競爭；R7 上方天空過多。 |
| Light 段的長句（主光、背光側、共用冷暖光） | 一句：燈籠暖光落在臉、大衣與周圍雪地，其餘保持冷藍 | 保留人景冷暖關係，句子縮短。 |
| 「worn open」「her eyes open」 | （不寫） | 屬可容許變化，不必指定。 |

不宣稱精簡 prompt 一定有效，也不再追加百分比門檻。

## 7. 構圖參考圖流程：這次不建議

- 已知（唯讀）：R7 送出前的唯讀查詢（models_explore get soul_2）：soul_2 可帶 1 張參考圖（role image）；style_id 可和 soul_id 並用，但不能和參考圖並用。
- 未確認：soul_id 與構圖參考圖能否同時使用、身分保持是否受影響、費用是否不同，都沒有確認；要確認得先上傳或製作參考圖，本輪不允許（不建任務、不生成參考圖）。
- 決定：這次仍用既有 Soul 純文字流程，不換模型、不加參考圖。

## 8. 下一次單張測試提案

- 套別：V-somi-oh；1 張、1 次請求、不自動重試。
- 設定：soul_2、somi-oh 既有 Soul、2k、3:4、count 1；不用 unlim、參考圖無、style 不傳。
- 費用：R5、R7 同設定報價與實扣都是 0.12 credits，只供參考，不代表下次價格，也不是生成授權；送出前要重新做不扣款、不建任務的報價預檢。
- 流程：1. 只送 1 次，失敗不自動重試；2. 執行者先依「不可妥協」逐項看圖自查，再看可容許變化；3. 主管實際看圖；4. 最後由 Penny 決定。
- 不宣稱精簡 prompt 一定有效；若再失敗，照實交付並回報，不自行連續重試。

## 9. 本輪範圍

- 不生成、不修圖、不訓練、不付費、不部署；不原樣重送 R7 prompt；不啟動 H-Jia 或其他照片；不改已接受的 V-Iris；不合併 main。
- 事實同步：累計生成改為 7（R2 1＋R5 5＋R7 1），和 24 套完成分類分開計算；V-Somi 仍是「退回待重規劃」，照片歷程記為「R5 退回；R7 主管建議退回，Penny 未接受」。
