# Cheryl Soh 蘇思穎 — Generation Notes

> ⚠️ **本檔案受 [`PERSONA_CANON.md`](../../PERSONA_CANON.md)（人設憲章）約束。**
> 憲章定義了反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源五條原則，並優先於本檔案中任何相衝突的敘述。
> 內容支柱的名稱與比重以 `profile.json` 為單一真理來源。

---

## 狀態：**建模圖已準備好，待訓練**（2026-09-03）

| 階段 | 狀態 |
|------|------|
| 選角（identity master） | ✅ 完成 |
| Reference Element 錨定 | ✅ `5a6c5300-ec07-41aa-9d44-8c7359c6a399`（cheryl-face-only-v1，純臉緊裁切） |
| 訓練集（**5 張**） | ✅ `images/training_v1/train_01..05.jpg` |
| **Soul 訓練** | ⏸ 待執行——等 19 位備齊後一次送訓 |
| 首批內容生成 | ⬜ 未執行 |

| # | 支柱 | 景別 / 角度 | 服裝 | 光線 | job |
|---|---|---|---|---|---|
| 1 | 私下 / 一個人的房間 | 胸上 正面 | 炭灰絲質睡衣 | 飯店床頭燈 | `0a901f28` |
| 2 | 制服 / 出勤 | 胸上 左轉 | 深藍無標識制服＋絲巾＋法式包頭 | 清晨走廊嵌燈 | `b554b7bf` |
| 3 | 新加坡的家 | 腰上 右轉 **自拍** | 白色羅紋背心＋淺灰家居褲 | 午後窗光 | `81d5a227` |
| 4 | 換裝 / 穿搭 | **全身** 正面 | 焦糖針織背心＋白襯衫＋黑直筒褲 | 午後窗光 | `73045374` |
| 5 | 飯店 / 各國城市 | **全身** 正面 | 黑色細肩帶洋裝 | 夜間桌燈＋城市光 | `f5706972` |

驗收：5/5 臉與 master 一致、5/5 朝向正確、無背對鏡頭／鬼影手／鏡子構圖。單人全數成立。
制服明寫無 logo、無識別章、無航空公司標識。

**已知偏差（使用者已審閱並接受）**：#1、#3、#5 的服裝露出度或長度大於指定，
方向與 `kanon` 相同——見 `review/soul_pilot/cheryl-soh/prompts.json` 的 `_cross_persona_finding`。

**已知限制**：#4、#5 姿勢僵硬如公式照，可作訓練用但不適合直接當日常素材。
成因與修法見 `SEXY_SCENE_LIBRARY.md` §3-E。待使用者決定是否回頭重生。
**Soul ID**：尚未取得

---

## 生成前必檢清單

1. **PERSONA_CANON.md 五條原則** — 反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源。
2. **身分一致性硬規格**（每一次 prompt 都要寫）：
   - 膚色：Fair, luminous, porcelain-toned skin — NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-colored. East Asian features (Taiwanese / Chinese / Korean / Japanese leaning), NOT Southeast Asian-leaning features.
   - 身材：169cm / 89-60-90 / D 罩杯
   - 選角階段**必須同時核對臉部與身材**——Rainie Hsu 就是只看臉沒核身材，整批訓練圖作廢重做。
3. **髮色髮型每次都要寫**（Soul V2 不繼承）：現階段為 天然黑（現階段）。
4. **SEXY_SCENE_LIBRARY.md**〈降低「AI 感」的技術要點〉五項全部套用。
5. **標誌性配額**：空服制服的私下版 — 每月 1 期；泳池只在休假期出現。

---

## 生成紀錄

（尚無紀錄。每次生成後在此追加：日期、模型、prompt、結果連結、判斷。）
