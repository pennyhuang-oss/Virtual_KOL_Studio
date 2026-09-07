# zhiyi-shen Soul V2 驗證 prompt（6 張，送生成前鎖定）

soul_id: 待訓練後填入
model: `soul_2`，**不掛任何 Reference Element**
每個 spec 只生一張，**不 reroll**（依 ACCEPTANCE_LOCKED.md §二）

## 為什麼與 cheryl-soh 用完全相同的場景

場景、服裝、光線、機位、動作**逐字與 cheryl 相同**，只換各自正典髮型。

理由：碰撞門檻（§四第 5 條）要判斷的是「遮掉髮型後，cheryl 的圖會不會被判成
zhiyi」。若兩人的驗證圖穿不同衣服、在不同地點，就算判得出來，也可能只是衣服和
背景在分辨，不是臉。控制住所有非臉部變因之後，這個測驗才真的在測臉——這是**比較嚴**
的測法，而且是在看到任何訓練結果之前就選定的。

## 洩題自檢（每一則都逐項核對過）

- [x] 不含臉型、眼距、鼻樑、眼型、下顎、年齡感等任何五官描述
      （她 profile 的 `face_type` 寫了「長臉、眉骨清晰、細長眼」——**一個字都沒有寫進去**）
- [x] 不含任何三圍或身高數字（88/61/91、172cm、D cup 全部不寫）
- [x] 只寫髮色髮型（黑色長直髮中分），不寫臉
- [x] 服裝與場景全部避開她的訓練集：
      白襯衫黑窄裙／飯店夜景、白襯衫／辦公室外灘天際線、白浴袍／浴室、
      深灰套裝／玄關衣架、黑針織洋裝／飯店書桌
- [x] 同時也確認這 6 個場景不在 cheryl 的訓練集裡
- [x] §3-F：句尾不掛裸否定句；單人排除句為已知例外，保留

---

## V1 — 正面胸上（基準幾何）

```
A photograph of a young East Asian woman, chest-up, facing the camera straight on.
She has long, straight, centre-parted black hair worn loose, falling flat in front of both shoulders.
She wears a plain oatmeal-colored ribbed cotton top with a simple round neckline.
She is sitting at a small round table in a quiet neighbourhood café in the late morning;
behind her is a pale plastered wall and the soft blur of a shelf of ceramic cups.
Soft diffused window light comes from her left and wraps around her, no hard shadows.
Her lips are relaxed and closed, her shoulders are down, and she is looking directly into
the lens the way you look at someone you already know.
She is the only person in the photograph; no other people are visible anywhere in the frame.
Shot on a 50mm lens at f/2.0, natural color, fine skin texture, no beauty retouching.
```

## V2 — 左前四分之三特寫（側轉後幾何穩定）

```
A photograph of a young East Asian woman, a close portrait from the collarbone up.
The camera is positioned to her front-left, so her head is turned about thirty degrees
away from the lens and both of her eyes remain visible.
Her straight black hair is pulled back into a low twisted knot, leaving her jawline and neck clear.
She wears a thin charcoal-grey merino crewneck.
She is standing on an outdoor stairwell landing of a concrete apartment building on an
overcast afternoon; behind her is grey sky and the soft edge of a railing, thrown out of focus.
Flat even overcast daylight from above and slightly to her left.
She has just turned her head toward the camera, her mouth relaxed, breathing normally.
She is the only person in the photograph; no other people are visible anywhere in the frame.
Shot on an 85mm lens at f/2.0, natural color, visible pores, no beauty retouching.
```

## V3 — 右前四分之三胸上（非中性表情下穩定）

```
A photograph of a young East Asian woman, chest-up.
The camera is positioned to her front-right, so her body is angled and her face is turned
back toward the lens at about twenty-five degrees.
Her long straight black hair is centre-parted and loose, one side tucked behind her ear.
She wears a soft sage-green linen shirt with the top two buttons open and the collar relaxed.
She is on a wooden bench under a row of trees in a city park in the afternoon; behind her
are green leaves and dappled light, well out of focus.
Warm late-afternoon daylight filtered through leaves falls across her face from her right.
She is in the middle of saying something and has broken into a real, unposed laugh,
her eyes narrowed slightly with it and her head tipped a little.
She is the only person in the photograph; no other people are visible anywhere in the frame.
Shot on a 50mm lens at f/2.0, natural color, fine skin texture, no beauty retouching.
```

## V4 — 近正面全身（測身材：不寫任何數字）

```
A photograph of a young East Asian woman, full length, head to feet inside the frame.
She has long, straight, centre-parted black hair worn loose over her shoulders.
She wears a fitted short-sleeved navy knit top tucked into straight-leg cream cotton
trousers, with flat white leather sneakers.
She is standing in a bright empty rehearsal room with a plain off-white painted wall
behind her and a pale wooden floor.
Even soft daylight from a large window out of frame fills the room without hard shadows.
The camera is in front of her, not behind her.
Her back is not to the camera.
Her weight is on her right leg with the left knee loose, and she is pulling her hair out
from under the collar of her top with one hand, looking off to the side at nothing
in particular.
She is the only person in the photograph; no other people are visible anywhere in the frame.
Shot on a 35mm lens at f/4, natural color, no beauty retouching.
```

## V5 — 前斜側全身動態（姿勢與場景切換）

```
A photograph of a young East Asian woman, full length, walking.
Her long straight centre-parted black hair is loose and swinging with her stride.
She wears a mid-length camel wool coat open over a white crewneck and dark straight jeans,
with brown leather ankle boots, and carries a small woven basket bag in her left hand.
She is crossing a wet stone pavement on a shopping street on an overcast morning;
behind her are shopfronts and bare street trees, softened out of focus.
Flat grey overcast daylight, cool and even, with faint reflections on the wet stone.
The camera is in front of her, not behind her, positioned at about thirty degrees to her
left as she walks toward it.
Her back is not to the camera.
She is mid-stride with her weight rolling onto her front foot, her free hand lifting the
collar of the coat against the wind, and she is looking ahead down the street rather than
at the lens.
She is the only person in the photograph; no other people are visible anywhere in the frame.
Shot on a 35mm lens at f/2.8, natural color, no beauty retouching.
```

## V6 — 困難條件自拍（光線＋妝髮同時變動）

```
A photograph of a young East Asian woman, a selfie held slightly above her eye line so the
camera looks a little down at her, head and shoulders filling most of the frame.
Her straight black hair is gathered up into a loose claw-clip twist with a few strands down at the temples.
She wears a washed-out grey cotton sweatshirt with a wide neckline.
She is on a low sofa in a small living room late in the evening; behind her is a dim wall
and the warm pool of a single amber floor lamp, most of the room falling into shadow.
Warm low-level tungsten light from that one lamp on her right side, the left side of her
face falling into soft shadow, mixed shadow and warm highlight.
She is wearing almost no makeup — bare skin, uneven undertone, natural brows, no lipstick.
She has just pulled a face at the camera, one eyebrow up and her mouth pushed sideways,
caught halfway between an expression and a laugh.
She is the only person in the photograph; no other people are visible anywhere in the frame.
Shot on a phone front camera at night, slight sensor noise in the shadows, natural color,
no beauty filter, no skin smoothing.
```
