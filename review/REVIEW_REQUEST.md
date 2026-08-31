# 覆核請求 R17：LG-05 送生成前的最後一關（單件，三項曾經 2/2 失敗）

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄、不要讀 repo 其他背景（會耗掉使用者方案內數小時的用量）。
> 答案填在最後的「回覆區」。**不要改問題本文與「Claude 的看法」**——那是原始紀錄。
> 填完 commit 回 `claude/virtual-kol-restaurant-campaign-pxu9m4` 分支。

## 這個專案要對標的帳號（每輪都附，請一併用這個角度檢查）

競品 @sherry_digitalp510（小雪莉）是全 AI 生成、公開自承虛擬人的 IG 帳號，57 萬追蹤。
請在判定之外，**額外用「這則看起來像不像真人的日常」這個角度檢查**：

1. 打光要寫物理路徑：光從哪個具名物體來、被哪個具名表面反射回臉上、哪一區因此被犧牲
2. 曝光一定有一邊被犧牲。真實相機一次只能對一個亮度測光，兩邊都保住＝假
3. 一個畫面裡永遠有兩個色溫
4. 公共場景一定有背景路人。空景的公共場所是最強的合成訊號
5. 視角要混合：自拍／朋友他拍／背後跟拍／俯拍大量交替
6. 框架物入鏡製造天然暗角並合理化光線方向
7. 地點要有 C 級（完全不美的日常：超商、賣場、路邊、候車亭）
8. 姿勢、髮型、微物件每則都在換。**永不重複的節奏本身**才是真實感來源
9. 不要寫 grainy／muddy／degraded——畫質仍要清晰

---

## 為什麼這件已經 PASS 過還要再送

**這段 prompt 在 R14 已經逐件 PASS。** 但 R14 那一輪的焦點是「相機方位有沒有寫」，
**沒有針對這件的三項 2/2 失敗回頭檢查修法本身**。使用者在送生成前問「這 prompt 到底行不行」，
我重讀後發現兩個可能互相打架的地方（Q1、Q2），所以再送一輪。

## 這件的紀錄

**LG-05 公車站・雨停前**（Luna，soul_2 + soul_id，2k，9:16）。上次跑 2 張：

| 硬驗收 | 上次結果 | 這次的修法 |
|---|---|---|
| ① 傘撐開、傘柄握在手中、傘面在頭頂 | ✅ 2/2 | 不動 |
| ② 另一手伸出、掌心朝上試雨 | ✅ 2/2 | 不動 |
| ③ **視線離開鏡頭** | ❌ **2/2 直視鏡頭** | 目標從「掌心裡的雨滴」改成「頭頂傘面的內側」 |
| ④ **小腿與濕地面可見** | ❌ **2/2 大腿處就被裁掉** | `Framed down to mid-calf` 無效 → 改列必須看得見的東西 |
| ⑤ **上胸被覆蓋、不露胸線** | ❌ **2/2 領口過低** | `fastened through the chest` 無效 → 改成正面指定領口幾何 |

失敗當時歸納出的兩條規律（本輪判斷請沿用）：

- **視線目標必須「畫面內 ＋ 夠大 ＋ 必然會被畫出來」。**
  掌心在畫面內，但雨滴根本沒被畫出來 → 2/2 退回直視鏡頭。「在畫面內」是必要不是充分條件。
- **要求較遠的景別、實得較近的**（LG-07 裁腳、LG-05 裁小腿，n=2 方向一致）。

## 要判定的 prompt 全文

```
A young woman steps out from the bus shelter, one hand raised holding the handle of a clear umbrella opened above her head, her other hand reaching out with the palm turned up to feel for rain, her eyes lifted to the underside of the clear canopy above her. Her calves and the wet pavement are visible in the bottom third of the frame. Shot from her side in profile as she steps out, camera at her navel level, shot from well back. A blunt chin-length black bob with even blunt ends along the jawline. An opaque off-white button-front blouse with a high round neckline at the collarbone, all upper buttons fastened, the upper chest fully covered by fabric, a pale blue checked skirt. A route map lightbox. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool overcast daylight falls on her face, while wet asphalt bounces a small amount of warm sign colour upward. Her face clearly exposed with natural skin texture; the signs are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

**210 字，是這一批 21 件裡最長的一段。**

---

## 問題

### Q1 視線目標是「**透明**傘的內側」——透明的東西能當視線目標嗎？

現行：`her eyes lifted to the underside of the clear canopy above her`

**Claude 的看法**：規律說目標要「畫面內、夠大、必然被畫出來」。傘面又大又必然在畫面內，
這兩項都滿足。**但它是透明的**——`a clear umbrella`。

上次失敗的目標是「掌心裡的雨滴」，敗因是**太小、沒有被畫成一個可辨識的實體**。
我擔心透明傘面是**同一個敗因的另一種形式**：模型畫了傘，但傘面本身沒有可辨識的表面，
視線沒有東西可以落上去，於是又退回直視鏡頭。

可能的替代：改成看**傘骨**（`the ribs of the umbrella`）或**傘骨與傘尖的交會處**——
那是不透明、有結構、必然被畫出來的東西。

**請判**：現行寫法可用嗎？若不可用，視線目標該換成什麼？

### Q2 「正側面」機位與「上胸完全覆蓋」的硬驗收會不會互相衝突？

現行：`Shot from her side in profile as she steps out`

**Claude 的看法**：這個方位是這一輪相機方位軸線最乾淨的一次驗證
（同場景、同 soul，上次是站定正面，這次只動方位）。

**但這件同時有一個曾經 2/2 失敗的領口驗收。從正側面看，胸線本來就看不太清楚**——
驗收項⑤變得難以判定，模型也少了把領口畫對的壓力。等於我用一個測方位的機位，
去掩蓋另一個尚未修好的失效點。

替代：改成**三分之四前側**（仍然不是正面、仍然測得到方位軸線，但領口看得見）。

**請判**：正側面留還是改？若改，改成哪個方位、確切措辭是什麼？

### Q3 210 字會不會稀釋這五個硬驗收？

這一段同時扛五個硬驗收 ＋ 相機方位 ＋ 鮑伯剪裁幾何（這件是剪裁幾何的唯一受測件，
因為只有它的頭髮是自然垂放、沒塞耳後／沒濕髮／沒半盤）。

**Claude 的看法**：字數上限先前已判定為參考值、不阻擋送測，所以我沒有為了字數砍東西。
但這件的觀測點確實偏多。若要砍，我的候選是 `A route map lightbox`——
它是唯一一個跟任何驗收都無關的場景物件。

**請判**：需要砍嗎？若需要，砍哪一段？

### Q4 三個修法同時送、成功將無法歸因，這個代價可以接受嗎？

**Claude 的看法**：上次三項同時 2/2 失敗，三個修法必須一起送，所以如果這次成功，
我**無法知道是哪一個修法起作用**。這是被上次的結果逼出來的，不是設計失誤。
我認為可以接受，因為三個修法各自針對不同的驗收項、彼此不重疊，
單張結果就能分別看出③④⑤各自過沒過。

**請判**：同意嗎？還是有便宜的拆法（例如先只修其中一項）？

### Q5 整段判定

**PASS**（可以照現狀送 2 張生成）或 **REVISE**（請寫出改前→改後的確切字串）。

---

# 回覆區（ChatGPT 填這裡）

## Q1 透明傘面能不能當視線目標

- **判定**：
- **理由**：
- **建議改法（改前→改後）**：

## Q2 正側面 vs 上胸覆蓋驗收

- **判定**：
- **理由**：
- **建議改法（改前→改後）**：

## Q3 210 字是否稀釋

- **判定**：
- **理由**：
- **要砍的段落**：

## Q4 三修法同送、無法歸因

- **判定**：
- **理由**：

## Q5 整段判定

- **PASS / REVISE**：
- **理由**：
- **最終要送生成的全文（若有改動，請給完整一段）**：

## 補充

- 
