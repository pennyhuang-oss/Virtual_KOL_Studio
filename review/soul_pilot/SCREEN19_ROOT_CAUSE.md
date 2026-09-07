# 19 位全配對篩檢（選項丙）結果：**這是系統性問題，不是一對的問題**

日期 2026-09-07。成本 **0 credits**（純本地運算）。

篩檢用的量尺與碰撞判定完全相同：mediapipe 478 landmark → 置中、RMS 尺度正規化
→ SVD Procrustes 對齊 → 平均 RMS 距離。對象是 19 位的 `identity_master.jpg`。

## 一、校準點

**cheryl-soh ↔ zhiyi-shen = 0.0157，而這一對在盲測中確定失敗。**
這是唯一有實測依據的門檻，不是我挑的數字。

## 二、171 組配對的分布

| | 配對數 | 佔比 |
|---|---|---|
| ≤ 0.0157（比失敗那一對更接近或相當） | **6** | 4% |
| ≤ 0.0200 | 30 | 18% |
| ≤ 0.0220 | **41** | **24%** |
| ≤ 0.0250 | 72 | 42% |

平均 0.0287，中位數 0.0268，最小 0.0122，最大 0.0686。

**比失敗那一對還接近的 5 組：**

| 距離 | 配對 |
|---|---|
| 0.0122 | jia-seo ↔ miu-shiraishi |
| 0.0133 | cheryl-soh ↔ nanami-fujiwara |
| 0.0139 | cheryl-soh ↔ ruoruo-tang |
| 0.0147 | nanami-fujiwara ↔ sydney-leong |
| 0.0151 | sydney-leong ↔ zhiyi-shen |
| *0.0157* | *cheryl-soh ↔ zhiyi-shen（已實測失敗）* |

## 三、目視複核（因為 landmark 只是篩檢，不是判決）

量化工具在已知失敗的那一對上自己也只拿 6/8，所以低於門檻只代表「嫌疑」。
把上表 6 組的 master **遮掉髮型髮色**並排（`_screen19_v1/closest_pairs_masked.jpg`）：

**前四組基本上是同一張臉。** 同樣的雙眼皮杏眼、同樣窄而挺的鼻樑、
同樣的厚唇與唇珠、同樣的卵形下顎；差異只在臉寬與髮型。
第五組（sydney ↔ zhiyi）稍可分辨（zhiyi 臉較長），但仍然接近。

**目視結果與量化結果一致：這 6 組都該視為碰撞。**

## 四、每一位牽涉到幾組 ≤0.0220

| 組數 | 人設 |
|---|---|
| 11 | ruoruo-tang |
| 10 | sydney-leong |
| 9 | nanami-fujiwara |
| 7 | miu-shiraishi |
| 6 | jia-seo / cheryl-soh / zhiyi-shen |
| 5 | emma-kao |
| 4 | yerin-han / kanon-komori / rin-ayase |
| 3 | peggy-lee |
| 2 | tammy-chou / somi-oh |
| 1 | angeline-kwee / wendy-yeo / wanyin-jiang |
| **0** | **angel-chiu、zoey-yeh** |

**19 位裡有 17 位至少牽涉一組。只有 angel-chiu 和 zoey-yeh 是乾淨的。**

## 五、共同成因

`kols/*/profile.json` 裡，**20 位共用完全相同的一段 `appearance.skin` 硬規格**：

> Fair, luminous, porcelain-toned skin — NOT tanned, NOT bronzed, NOT olive,
> NOT deep golden or wheat-colored. East Asian features (Taiwanese / Chinese /
> Korean / Japanese leaning), NOT Southeast Asian-leaning features.

這段字不只鎖膚色，還鎖了**五官族裔走向**。19 位的 identity 都是在這段相同硬規格
＋相同 prompt 模板下生成的。

**但每位的 `face_type` 其實是有差異化的**，而且差異寫得很具體：

- wanyin-jiang：鵝蛋臉、柳葉眉、**丹鳳眼、薄唇**
- kanon-komori：**非常小的臉**、大眼、**圓鼻頭**
- miu-shiraishi：**圓臉**大眼、**下垂眼尾**、童顏
- zhiyi-shen：**長臉**、眉骨清晰、**細長眼**
- peggy-lee：**濃眉大眼、五官張揚立體**
- somi-oh：**圓潤有肉感**、酒窩、月牙眼
- zoey-yeh：圓眼、眼尾下垂、柔弱清純

**關鍵觀察：cheryl 寫的是「鵝蛋臉」，zhiyi 寫的是「長臉」——設計上是不同的臉，
但生成出來還是撞了（0.0157，實測失敗）。**

結論：**設計意圖有差異化，生成結果沒有。** 那段共用硬規格＋共用模板壓過了
每人一行的 `face_type`。

嚴格說，我只證明了「相關」而非「因果」——要證明因果必須實測（見下）。
但可以確定的事實是：**設計是分開的，輸出不是。**

## 六、這對已花的成本意味著什麼

已訓練並驗證的 cheryl-soh 與 zhiyi-shen 共花 51.44 credits。
**若最終決定重做 identity，這兩個 soul 會失效，51.44 等於學費。**

但它換到的資訊是：5 張訓練集足夠、管線正確、而 19 位的臉區分度不足——
其中最後一項若沒有試點，會在花掉 475 credits 之後才發現。

## 七、建議下一步：**先做方法實測，不要直接重做 19 位**

直接重做 19 位的 identity + 19 × 5 張訓練集 + 19 × 25 credits 重訓，
是在**還沒證明新方法有效**的情況下下重注。

建議先花**個位數 credits** 做一次方法實測：

1. 挑 4 位目前撞得最兇的（例如 jia-seo、miu-shiraishi、cheryl-soh、nanami-fujiwara）。
2. 改寫生成方式：把共用的 `appearance.skin` 硬規格**縮到只管膚色**，
   把族裔與五官交還給各自的 `face_type`，並把 `face_type` 從一行擴寫成
   明確的幾何描述（臉長寬比、眼型與眼距、鼻樑寬窄、唇厚、下顎角度）。
3. 各生 1 張新 identity 候選（4 credits 左右）。
4. 用本篩檢同一把尺算這 4 位的 6 組配對距離，並遮髮目視。
5. **只有在這 4 位彼此都拉開到明顯高於 0.0220 之後**，才把方法套用到 19 位。

若實測顯示改寫規格仍拉不開，那問題在模型本身對「白皙東亞女性」的先驗過強，
就要改用別的手段（不同 base model、或用 Reference Element 混入更強的臉部變異），
而不是繼續重生。

**此決策由使用者定，我不自行執行第 7 節的任何生成。**
