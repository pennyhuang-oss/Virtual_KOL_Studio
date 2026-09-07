# 抽驗 5 位驗證結果（2026-09-07）

使用者裁定抽驗 5 位。用與試點**完全相同的 6 個 spec**（同場景、同服裝、同光線、
同機位、同動作），只換各自正典髮型，因此結果可與 cheryl-soh／zhiyi-shen 直接比較。

規則同 `../soul_training/ACCEPTANCE_LOCKED.md` §二：只用 `soul_2` + `soul_id`，
不掛 Reference Element，不重述五官、不寫三圍，每 spec 只生一張不 reroll。

## 為什麼選這 5 位（不是隨機）

| 人設 | 選擇理由 |
|---|---|
| kanon-komori | 唯一 6 張訓練集；且是童顏設定，有**年齡紅線** |
| miu-shiraishi | 童顏設定；且屬 171 組裡**最接近的配對**（與 jia-seo，0.0122） |
| ruoruo-tang | **碰撞牽涉最多**（11 組 ≤0.0220） |
| wanyin-jiang | `face_type` **規格最獨特**（丹鳳眼、薄唇），測獨特規格有沒有活下來 |
| zoey-yeh | **零碰撞的乾淨對照組**；且訓練最慢（約 35 分鐘） |

成本：5 × 6 × 0.12 = **3.6 credits**，30 張一次成功無重生。

## 判定

**5 位全部通過門檻 1 與門檻 2。**

| 人設 | 門檻 1 同一人 | 門檻 2 V1/V2/V3/V6 無漂移 | 髮色髮型正確 |
|---|---|---|---|
| kanon-komori | 通過 | 通過 | 粉紫漸層 6/6 正確 |
| miu-shiraishi | 通過 | 通過 | 淺亞麻米金 6/6 正確 |
| ruoruo-tang | 通過 | 通過 | 淺栗棕 6/6 正確 |
| wanyin-jiang | 通過 | 通過 | 黑色長直 6/6 正確 |
| zoey-yeh | 通過 | 通過 | 黑色中分直髮 6/6 正確 |

方法：以既有公式裁臉，與各自 `identity_master.jpg` 並排比對眉形、眼型、眼距、
鼻樑、唇形、下顎收尖點（見 `_sample_v1/` 的比對圖）。

**年齡紅線**：kanon-komori 與 miu-shiraishi 都是童顏設定，
**6 張都讀為成年人（約 20–25），沒有任何一張漂移成未成年**。
兩位的 Soul 與各自 master 的年齡感一致，即 Soul 沒有把她們變得更小。

**零碰撞對照組成立**：zoey-yeh 目視明顯與其他 4 位不同，
與她在篩檢中 0 組 ≤0.0220 的結果一致——**篩檢工具的判斷方向是對的**。

## 三個非門檻發現

### 1. 獨特的 `face_type` 特徵沒有活下來，但不是 Soul 的錯

wanyin-jiang 的 `face_type` 寫「鵝蛋臉、**柳葉眉、丹鳳眼、薄唇**」。
出圖的唇偏厚、眼型是標準杏眼，**丹鳳眼與薄唇都沒有出現**。

但比對她自己的 `identity_master.jpg` 後確認：**master 本身就沒有這兩個特徵。**
Soul 忠實複製了 master。**特徵是在 identity 生成階段就丟掉的，不是訓練丟的。**

這是 `PERSONA_CANON.md` 原則六根因在第三條戰線上的印證，
也直接支持新增的六-A（`face_type` 必須具體到可測量）。

### 2. 身高／嬌小感沒有被 Soul 繼承

kanon-komori 規格 153cm「極嬌小」、miu-shiraishi 156cm，
但兩位的 V4 全身照都**讀為一般比例成年人，沒有嬌小感**。
與 cheryl-soh 的身材落差是同一個現象：**Soul V2 不可靠地繼承身材與身高。**

好消息是這一項**可以用 prompt 補**——見 `_body_test_v1/BODY_TEST_v1.md`。

### 3. V5 街景仍出現背景路人

與 `SEXY_SCENE_LIBRARY.md` §3-F 第三次補正一致：單人排除句在人多的戶外場景擋不住。
路人全部失焦、無可辨識人臉，依 §QA-1 不構成失敗。

## 結論

**17 位裡抽驗 5 位，全部通過。** 沒有發現任何個別人設訓壞。
配合兩位試點的 6/6 結果，19 位的 Soul 訓練品質可視為一致。

抽驗的 5 位狀態升為 `face_validated`（與試點的 `trained_face_validated` 同級）。
未抽驗的 12 位維持 `ready_unvalidated`。
