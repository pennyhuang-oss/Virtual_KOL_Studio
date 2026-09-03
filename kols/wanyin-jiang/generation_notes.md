# Wanyin Jiang 江晚吟 — Generation Notes

> ⚠️ **本檔案受 [`PERSONA_CANON.md`](../../PERSONA_CANON.md)（人設憲章）約束。**
> 憲章定義了反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源五條原則，並優先於本檔案中任何相衝突的敘述。
> 內容支柱的名稱與比重以 `profile.json` 為單一真理來源。

---

## 狀態：**建模圖已準備好，待訓練**（2026-09-03）

建立日期：2026-08-27（Batch 3）｜狀態更新：2026-09-03

| 階段 | 狀態 |
|------|------|
| 選角（identity master） | ✅ 完成，鎖在 `identity/identity_master.jpg` |
| Reference Element 錨定 | ✅ 完成，`a0e68491-43ac-40c8-99d5-fec60596ac50`（wanyin-face-only-v2，純臉緊裁切） |
| 訓練集（**5 張**） | ✅ 完成，`images/training_v1/train_01..05.jpg` |
| **Soul 訓練** | ⏸ **待執行——使用者裁決：等 19 位的建模圖全部備齊後一次送訓** |
| 首批內容生成 | ⬜ 未執行 |

### 訓練集清單（5/5，全部同時是可發布素材）

| # | 支柱 | 景別 / 角度 | 服裝 | 光線 | job |
|---|---|---|---|---|---|
| 1 | 浴室 / 晨間梳妝 | 胸上 正面 0–10° 他拍 | 米白絲質晨袍＋薄吊帶 | 晨間窗光 | `265e8425` |
| 2 | 旗袍店工作 / 量身 | 胸上 左 40° 他拍 | 墨藍素面旗袍 | 店門日光＋暖吊燈 | `facacff8` |
| 3 | 私下 / 老宅暗光 | 腰上 右 35° **自拍** | 酒紅絲質吊帶＋炭灰開襟 | 暖檯燈 vs 窗外藍調 | `a0bf8f16` |
| 4 | 外出 / 園林 | **全身** 正面 他拍 | 淡青素面旗袍 | 晨間逆光 | `9cd8d2df` |
| 5 | 換裝 / 盤扣 | **全身** 正面 他拍 | 黑色暗紋旗袍＋米白滾邊 | 午後門光 | `70578aaa` |

驗收：5 套服裝／5 個場景／5 種光線全不重複、2 張全身、1 張腰上、自拍僅 1 張、
5 張都露出完整眉眼與下顎、每張都只有她一人、臉部與 master 逐張比對通過。

完整判讀、失敗紀錄與 prompt 全文見 `review/soul_pilot/wanyin-jiang/`。

### 這一位過程中確立、適用於其餘 18 位的規則

1. **臉部 element 必須用純臉緊裁切**（切在下巴下方約 15% 臉高，不含頸根、肩線、衣領）。
   含頭肩的裁切會壓過 prompt 的身材文字。實證：`review/soul_pilot/wanyin-jiang/diagnostic/`
2. **生活照與訓練圖不使用五段式佈光**，改一句話。見 `SEXY_SCENE_LIBRARY.md` §3-0。
3. **不要把拍攝者擬人化**（`held by someone`／`whoever is holding the phone`）——會把別人的手請進畫面。
   寫 `shot on a rear phone camera from about N metres away` 即可。見 §3-D①。
4. **不用角度數字控制身體朝向**，改寫正面可見幾何。及膝景別在本模型上三度失敗，全身正面與胸／腰上可靠。
5. **不掛固定風格尾巴**（`film grain / 35mm / warm tones / Instagram style`）。見 §3-D②。

**Soul ID**：尚未取得

---

## 生成前必檢清單

1. **PERSONA_CANON.md 五條原則** — 反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源。
2. **身分一致性硬規格**（每一次 prompt 都要寫）：
   - 膚色：Fair, luminous, porcelain-toned skin — NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-colored. East Asian features (Taiwanese / Chinese / Korean / Japanese leaning), NOT Southeast Asian-leaning features.
   - 身材：165cm / 86-57-88 / D 罩杯
   - 選角階段**必須同時核對臉部與身材**——Rainie Hsu 就是只看臉沒核身材，整批訓練圖作廢重做。
3. **髮色髮型每次都要寫**（Soul V2 不繼承）：現階段為 天然黑（現階段）。
4. **SEXY_SCENE_LIBRARY.md**〈降低「AI 感」的技術要點〉五項全部套用。
5. **標誌性配額**：旗袍 / 漢服半褪 — 每月 2 期；古典舞身段影片每月 1 期。

---

## 生成紀錄

（尚無紀錄。每次生成後在此追加：日期、模型、prompt、結果連結、判斷。）
