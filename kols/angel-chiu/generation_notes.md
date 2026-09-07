# Angel Chiu 邱安晴 — Generation Notes

> ⚠️ **本檔案受 [`PERSONA_CANON.md`](../../PERSONA_CANON.md)（人設憲章）約束。**
> 憲章定義了反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源五條原則，並優先於本檔案中任何相衝突的敘述。
> 內容支柱的名稱與比重以 `profile.json` 為單一真理來源。

---

## 狀態：**建模圖已準備好，待訓練**（2026-09-04）

| 階段 | 狀態 |
|------|------|
| 選角（identity master） | ✅ 完成 |
| Reference Element 錨定 | ✅ `0ec9988e-def7-4bf8-9337-35b5e4757bf1`（angel-face-only-v1，純臉緊裁切） |
| 訓練集（**5 張**） | ✅ `images/training_v1/train_01..05.jpg` |
| **Soul 訓練** | ⏸ 待執行——等 19 位備齊後一次送訓 |
| 首批內容生成 | ⬜ 未執行 |

| # | 支柱 | 景別 | 服裝 | 光線 | job |
|---|---|---|---|---|---|
| 1 | 私下 / 房間裡的她 | 胸上 正面 | 深灰絲質睡裙（髮尾蜜茶金放下） | 床頭燈＋窗簾漏光 | `e0ffe99c` |
| 2 | 職業 / 醫院檯面 | 胸上 左轉 | 藍綠刷手服（髮色完全紮起藏住） | 深夜半熄日光燈 | `d8cdd7a2` |
| 3 | 浴室 / 晨間 | 腰上 **自拍** | 白棉背心＋灰短褲 | 走廊盡頭冷色窗光 | `86385aca` |
| 4 | 穿搭 / 換裝 | **全身**（§3-E） | 米白粗針織外套＋白 T＋丹寧中長裙 | 房間午後窗光 | `a507210e`（v2） |
| 5 | 外出 / 休假 | **全身**（§3-E） | 橄欖綠工裝外套＋黑 T＋工裝褲 | 騎樓陰天光 | `a3d7ae60` |

5/5 臉與 master 一致。髮尾蜜茶金的藏／露反差在 #1 與 #2 成立。刷手服無任何醫院標識。

**#4 有兩版**：v1（`81d96fb6`）姿勢較好但整張被手機外框包住且腳被裁掉，已作廢不進訓練集；
v2 為重生版，外框與裁腳都修好，但捲袖口動作未執行、姿勢較平。兩張都保留在 `review/` 供比對。
修法與驗證見 `review/soul_pilot/angel-chiu/prompts.json` 的 `_new_finding_phone_bezel`。
**Soul ID**：尚未取得

---

## 生成前必檢清單

1. **PERSONA_CANON.md 五條原則** — 反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源。
2. **身分一致性硬規格**（每一次 prompt 都要寫）：
   - 膚色：Fair, luminous, porcelain-toned skin — NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-colored. East Asian features (Taiwanese / Chinese / Korean / Japanese leaning), NOT Southeast Asian-leaning features.
   - 身材：163cm / 88-58-89 / D 罩杯
   - 選角階段**必須同時核對臉部與身材**——Rainie Hsu 就是只看臉沒核身材，整批訓練圖作廢重做。
3. **髮色髮型每次都要寫**（Soul V2 不繼承）：現階段為 黑棕 + 蜜茶金髮尾（隱藏式）。
4. **SEXY_SCENE_LIBRARY.md**〈降低「AI 感」的技術要點〉五項全部套用。
5. **標誌性配額**：改造版護理服（合身短版）、蕾絲內衣 — 每月 1–2 期，不是日常基調。

---

## 生成紀錄

（尚無紀錄。每次生成後在此追加：日期、模型、prompt、結果連結、判斷。）
