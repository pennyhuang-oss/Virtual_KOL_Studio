# Ruoruo Tang 唐苡若 — Generation Notes

> ⚠️ **本檔案受 [`PERSONA_CANON.md`](../../PERSONA_CANON.md)（人設憲章）約束。**
> 憲章定義了反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源五條原則，並優先於本檔案中任何相衝突的敘述。
> 內容支柱的名稱與比重以 `profile.json` 為單一真理來源。

---

## 狀態：**建模圖已準備好，待訓練**（2026-09-04）

| 階段 | 狀態 |
|------|------|
| 選角（identity master） | ✅ 完成 |
| Reference Element 錨定 | ✅ `7d30e2b0-b7b3-40cb-9352-592b250e2b60`（ruoruo-face-only-v1，純臉緊裁切） |
| 訓練集（**5 張**） | ✅ `images/training_v1/train_01..05.jpg` |
| **Soul 訓練** | ⏸ 待執行——等 19 位備齊後一次送訓 |
| 首批內容生成 | ⬜ 未執行 |

| # | 支柱 | 景別 | 服裝 | 光線 | job |
|---|---|---|---|---|---|
| 1 | 私下 / 家裡的地墊 | 胸上 正面 | 炭灰羅紋連身衣 | 午後側窗光 | `b7d7f063` |
| 2 | 器械皮拉提斯 | 胸上 側轉（實出背 3/4） | 鼠尾草綠露背上衣＋高腰褲 | 教室高窗平光 | `6ec25031` |
| 3 | 浴室 / 晨間 | 腰上 **對鏡自拍** | 白色細肩背心＋灰短褲 | 晨間冷色窗光 | `ac35561a` |
| 4 | 穿搭 | **全身**（§3-E） | 燕麥色長大衣＋黑針織＋寬褲 | 玄關門口日光 | `e4fbe408` |
| 5 | 外出 / 成都 | **全身**（§3-E） | 黑風衣＋白 T＋灰運動長褲 | 巷弄樹蔭陰天光 | `c96c9892` |

5/5 臉與 master 一致，栗棕髮色正確。**#4 #5 為 §3-E 第二次驗證，兩張都自然可發布。**

**使用者裁決 2026-09-04**：#2（實際出成背 3/4＋露背款）與 #3（實際出成對鏡自拍、手機入鏡）
**均判定可用，不重生**。#3 的成因已寫成規則見 `prompts.json` 的 `_new_finding_selfie_mirror`。
**Soul ID**：尚未取得

---

## 生成前必檢清單

1. **PERSONA_CANON.md 五條原則** — 反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源。
2. **身分一致性硬規格**（每一次 prompt 都要寫）：
   - 膚色：Fair, luminous, porcelain-toned skin — NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-colored. East Asian features (Taiwanese / Chinese / Korean / Japanese leaning), NOT Southeast Asian-leaning features.
   - 身材：167cm / 87-59-90 / C 罩杯
   - 選角階段**必須同時核對臉部與身材**——Rainie Hsu 就是只看臉沒核身材，整批訓練圖作廢重做。
3. **髮色髮型每次都要寫**（Soul V2 不繼承）：現階段為 淺栗棕（暖調染色）。
4. **SEXY_SCENE_LIBRARY.md**〈降低「AI 感」的技術要點〉五項全部套用。
5. **標誌性配額**：連身運動衣 / 高難度體位 — 每週 1 期。

---

## 生成紀錄

（尚無紀錄。每次生成後在此追加：日期、模型、prompt、結果連結、判斷。）
