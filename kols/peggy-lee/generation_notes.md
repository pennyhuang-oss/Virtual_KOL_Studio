# Peggy Lee 李珮甄 — Generation Notes

> ⚠️ **本檔案受 [`PERSONA_CANON.md`](../../PERSONA_CANON.md)（人設憲章）約束。**
> 憲章定義了反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源五條原則，並優先於本檔案中任何相衝突的敘述。
> 內容支柱的名稱與比重以 `profile.json` 為單一真理來源。

---

## 狀態：**建模圖已準備好，待訓練**（2026-09-04）

| 階段 | 狀態 |
|------|------|
| 選角（identity master） | ✅ 完成 |
| Reference Element 錨定 | ✅ `8a33b9d3-bcfd-43c5-b4c6-c9fba5b194b4`（peggy-face-only-v1，純臉緊裁切，0 credits） |
| 訓練集（**5 張**） | ✅ `images/training_v1/train_01..05.jpg` |
| **Soul 訓練** | ⏸ 待執行——等 19 位備齊後一次送訓 |
| 首批內容生成 | ⬜ 未執行 |

| # | 支柱 | 景別 | 服裝 | 光線 | job |
|---|---|---|---|---|---|
| 1 | 私下 / 房間與車庫 | 腰上 右轉 30° | 黑羅紋背心＋高腰深色牛仔＋沾油工作襯衫 | 引擎蓋下單顆工作燈 | `d794ae85` |
| 2 | 改裝店工作 / 車 | 胸上 右轉 40° | 黑店 T＋工作證吊繩 | 捲門進來的平光 | `0cd1350e` |
| 3 | 浴室 / 晨間 | 胸上 正面 | 白色毛巾浴袍 | 霧面小窗晨光 | `1db6c7ca` |
| 4 | 穿搭 | **全身**（§3-E） | 黑短版長袖＋高腰黑直筒＋黑長靴 | 房間窗光 | `a202f286` |
| 5 | 夜衝 / 公路 | **全身**（§3-E） | 深紅車隊外套＋黑上衣＋黑牛仔＋黑靴 | 加油站頂棚燈 | `02424460` |

5/5 臉與 identity master 一致，正酒紅＋銀灰挑染五張都看得到（#2 是高馬尾，銀灰在馬尾中段最清楚）。

**§3-E 全身照**：#4 單腳踩床架拉長靴拉鍊、低頭看自己的手；#5 單腳承重、手握油槍、看油表不看鏡頭。
兩張都有實際動作、都沒有回到公式站姿，累計 §3-E 成功數 10/10。

**本批新發現（已寫入 `review/soul_pilot/peggy-lee/prompts.json`）**：
seedream 有可能 `status=completed` 卻交出**完全未收斂的雜訊圖**（#2 第一次，job `e8eddf2c`）。
已用 native-resolution crop 複驗、重新下載 SHA-256 相同，確認不是縮圖誤判也不是下載損毀；
同批同模型另外 9 張全部正常，因此不是 prompt 問題。**規則：每一張圖歸檔前都必須實際看過，
不可因為 jobs_wait 回報 completed 就收檔。** 重跑時 prompt 一字未改即成功，成本 1 credit。

**已知偏差（收下但記錄）**：#1 工作襯衫被綁在腰上而非當外套穿、短版露腰——覆蓋度偏差累計仍全部同向；
#2 視線往上不在鏡頭、機位偏低（prompt 未指定機位高度），工作證上有約 30px 的證件照人像，
技術上違反「牆上／螢幕上不得有人像」條款，屬極小區域，不值得再花 credit 重跑。

**Soul ID**：尚未取得

---

## 生成前必檢清單

1. **PERSONA_CANON.md 五條原則** — 反差公式、標誌性場景配額、造型可變性、不寫絕對禁令、單一真理來源。
2. **身分一致性硬規格**（每一次 prompt 都要寫）：
   - 膚色：Fair, luminous, porcelain-toned skin — NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-colored. East Asian features (Taiwanese / Chinese / Korean / Japanese leaning), NOT Southeast Asian-leaning features.
   - 身材：166cm / 93-58-92 / F 罩杯
   - 選角階段**必須同時核對臉部與身材**——Rainie Hsu 就是只看臉沒核身材，整批訓練圖作廢重做。
3. **髮色髮型每次都要寫**（Soul V2 不繼承）：現階段為 正酒紅 + 銀灰挑染（特殊色）。
4. **SEXY_SCENE_LIBRARY.md**〈降低「AI 感」的技術要點〉五項全部套用。
5. **標誌性配額**：賽車服 / 車展 showgirl 造型 — **每月 2 期**（車展是活動，不是她的日常穿著）。

---

## 生成紀錄

（尚無紀錄。每次生成後在此追加：日期、模型、prompt、結果連結、判斷。）
