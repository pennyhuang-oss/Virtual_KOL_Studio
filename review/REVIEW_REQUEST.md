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

- **判定**：透明傘面可以作為場景物件，但不宜單獨作為這次的硬驗收視線目標；改看「整片深色傘骨」。
- **理由**：傘面夠大、在畫面內且必然生成，優於掌心雨滴；但 `underside of the clear canopy` 指向的是透明材質形成的空泛區域，缺少有邊界、有對比的落點，仍可能只被模型理解為「臉朝上」，而不是眼睛確實離開鏡頭。只寫中央傘尖／hub 又會回到「目標太小」的風險。傘骨是一組橫跨頭頂的大型、不透明、高對比結構，既保留自然的抬眼動作，也更符合「畫面內＋夠大＋必然會被畫出來」三條。
- **建議改法（改前→改後）**：`her eyes lifted to the underside of the clear canopy above her` → `her eyes lifted toward the fan of dark umbrella ribs spreading across the clear canopy above her`

## Q2 正側面 vs 上胸覆蓋驗收

- **判定**：改成前側三分之四，不保留正側面。
- **理由**：正側面雖能乾淨測到方位改變，但會讓高圓領、鎖骨位置與上胸覆蓋程度難以判讀。這不是把領口問題修好，而是讓曾經 2/2 失敗的驗收失去正面證據。前側三分之四仍明確偏離預設正面、足以驗證方位軸線，同時能讓領口輪廓與上胸布料在畫面中可見；兩個目標不再互相犧牲。
- **建議改法（改前→改後）**：`Shot from her side in profile as she steps out, camera at her navel level, shot from well back.` → `Shot from her three-quarter front-left as she steps out, camera at her navel level, from well back.`

## Q3 210 字是否稀釋

- **判定**：不因 210 字刪內容；字數本身不是已驗證的失敗門檻。
- **理由**：五項硬驗收集中在開頭三句與服裝句，位置優先度高，沒有被埋在末段。其餘內容也不是純裝飾：路人支撐公共場景真實感，光線段提供雙色溫、反射路徑與曝光犧牲，髮型是本件唯一要測的剪裁幾何。尤其 `A route map lightbox` 不能刪，它同時使後文的 `warm sign colour` 與 `the signs are the brightest area` 有具名、可見的物理來源；刪除反而會製造光線邏輯空缺。若生成失敗，應依五項逐欄結果判斷，不應先把未證實的總字數當根因。
- **要砍的段落**：無；保留 `A route map lightbox`。

## Q4 三修法同送、無法歸因

- **判定**：同意三項同送，代價可接受；不建議先只修一項。
- **理由**：這一輪的目的是讓 LG-05 成為可用素材，不是建立單一變因的通用因果律。③視線、④構圖範圍、⑤領口是三個不同輸出欄位，各自有獨立的改動與驗收結果；即使同一批生成，仍能逐張記錄三欄各自 PASS／FAIL，判斷哪一項修法是否有效。真正無法排除的是跨指令交互作用，但為此拆成三輪會讓已知失敗繼續消耗生成額度。若某一欄再次失敗，再只針對該欄做單變因追測即可。

## Q5 整段判定

- **PASS / REVISE**：**REVISE**
- **理由**：構圖、景別、手物關係、領口幾何、公共路人與物理光線路徑均可保留；送生成前只需修正兩個會直接影響硬驗收的衝突：把透明傘面改成大面積、高對比的傘骨視線目標，並把正側面改成可驗收領口的前側三分之四。完成後可直接送 2 張。
- **最終要送生成的全文（若有改動，請給完整一段）**：

```
A young woman steps out from the bus shelter, one hand raised holding the handle of a clear umbrella opened above her head, her other hand reaching out with the palm turned up to feel for rain, her eyes lifted toward the fan of dark umbrella ribs spreading across the clear canopy above her. Her calves and the wet pavement are visible in the bottom third of the frame. Shot from her three-quarter front-left as she steps out, camera at her navel level, from well back. A blunt chin-length black bob with even blunt ends along the jawline. An opaque off-white button-front blouse with a high round neckline at the collarbone, all upper buttons fastened, the upper chest fully covered by fabric, a pale blue checked skirt. A route map lightbox. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool overcast daylight falls on her face, while wet asphalt bounces a small amount of warm sign colour upward. Her face clearly exposed with natural skin texture; the signs are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

## 補充

- 本輪改成前側三分之四後，⑤不能只靠「胸線沒有露」判 PASS；應正向確認高圓領邊界位於鎖骨、左右領口連續、上胸由不透明布料覆蓋。否則仍可能把裁切或姿勢遮擋誤判為領口修復成功。
