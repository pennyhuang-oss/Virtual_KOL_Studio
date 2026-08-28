# R10 — ChatGPT 覆核回覆（Phase C 20 段 prompt，2026-08-28）

> 原文封存。處置見 [`../LEDGER.md`](../LEDGER.md) 與 `REVIEW_PHASE_C.md` §6-1。
> 開出 C-34–C-43 共 10 條（8 條 P0）。逐條實測後 10 條全部屬實，全部已修；
> 唯一分歧是景別句尾的「某部位在畫面外」是否算失效否定（見 §6-2）。

## ChatGPT 覆核回覆（Phase C prompts）

### C-34｜P0｜20 段都漏掉身材 identity 描述

§3-3 說明 B2 是在修正身材設定後才通過，但 §5 的 20 段 prompt 沒有任何一段寫入 Nico 的胸型、肩腰臀比例、長軀幹或窄長輪廓；只有服裝與 framing。Reference Element 能固定臉，不等於會固定全身，第一次 B2 失敗已經是反證。請把 **B2 第二次實測成功的正面身材字串**設成共用模板，至少寫入所有會讀到胸、腰、臀或全身比例的列；不要再使用 `NOT heavy-chested` 之類否定式。這項未修前不可生成。

### C-35｜P0｜仍大量使用 §2 已證實無效的否定式

第 1 題答案是「有」，而且不是只有 §6-5 指出的那一句：

- face close-up、`[[S9]]`、`[[S10]]`、`[[S11]]` 在正確的下緣句之後，又用 `none ... is in it`／`... are outside the picture` 排除身體區域；這正是 §2-1 已證實無效的構圖否定。
- `[[S5]]` 的 `Her back is not toward the camera` 無效，應刪除。§6-5 把它誤寫成 `[[S8]]`；實際是 `[[S5]]`，出現 11 次。
- `[[S6]]` 的 `No lens distortion`、`This is not a shallow blurred-background portrait` 是相機／構圖否定。
- 多段光線仍寫 `with no hard shadow anywhere`；結尾的 `no filter and no beauty retouching` 也依賴否定。
- `nico_a01` 的 `not doing anything in particular`、`nico_c04` 的 `The phone ... is not itself in the picture` 同樣依賴模型忽略已知不可靠的否定。

修法是保留「畫面下緣切在哪裡」與可見區域的正面描述，刪掉後續排除句；相機改寫成「straight geometry／background remains recognisable and reasonably sharp」；柔光改寫成「only broad, soft-edged tonal transitions」；自拍寫成「the viewpoint is the phone’s front-camera feed, with the device immediately beyond the image boundary」。若 API 有獨立 negative prompt，排除詞應放到該欄，不要混在主 prompt 當作硬控制。

### C-36｜P0｜composition 英文會把站姿／走姿／蹲姿改成 seated

`She sits centred in the frame`／`She sits off to one side...` 的 `sits` 對模型是明確動作，不只是英文慣用語。它與下列結構欄位直接衝突：

- `nico_a03`、`nico_a04`、`nico_a06`、`nico_a07`
- `nico_c06`、`nico_c09`、`nico_c10`、`nico_c11`、`nico_c12`
- `nico_a08`

統一改成 `She is positioned centrally in the frame`／`Her figure is positioned off-centre`。不要讓 composition 模板使用任何姿態動詞。

### C-37｜P0｜builder 沒有依 framing 過濾裁切外資訊

景別雖然放在最前面，但後文又要求模型畫出裁切外的手、鞋和包，會與景別競爭：

- 應省略裁切外 hand action：`nico_a01` 雙手、`nico_a02` 左手、`nico_a03` 左手、`nico_a04` 左手、`nico_a05` 左手、`nico_c01` 雙手、`nico_c03` 右手、`nico_c12` 左手、`nico_a08` 雙手。
- face/chest/waist/knee-up 仍逐件描述裁切外的褲、鞋或拖鞋。請讓 outfit renderer 只輸出該 framing 可能看見的層；例如 chest-up 不應再提示鞋，knee-up 不應提示鞋。
- wardrobe 裡的包也沒有落點。最明顯是 `nico_c07`：兩手都拿美甲工具，prompt 卻另要求 beige canvas tote；`nico_a07`、`nico_c12` 也指定雙手狀態卻沒有說包是肩背、放下或在裁切外。這已把 C-32 從未來 schema 問題變成當前 prompt 歧義。Nico 不必等完整新 schema，但本批每列至少要把包的 `worn／set_down／outside_frame` 寫清楚。

原則應是：**只輸出預期可見的內容；不是以「outside the crop」否定其可見性。**

### C-38｜P0｜兩段仍含會誘發背影的高風險朝向語句

- `nico_a07`：`her torso turned three-quarters toward her own right` 仍是角度概念，與 §2-2 的失敗模式相同；而後面的 `[[S5]]` 又只允許輕微斜身，兩句彼此程度不一致。刪除 `three-quarters`，只保留相機看得到的正面肩線、鎖骨、褲頭正面等地標。
- `nico_c09`：`looked back over her shoulder` 是非常強的背向鏡頭提示，卻又接 `[[S5]]` 要求胸前可見。改成「她蹲著面向貨架斜側，頭轉向鏡頭」，並以可見正面地標鎖定身體，不要使用 `over her shoulder`。

`nico_a08` 是刻意的純側身 profile，現有「近肩遮住遠肩」的正面描述足夠，無異議。

### C-39｜P0｜`nico_c09` 的 basket 翻譯破壞結構欄位

結構把 `basket_c09` 定位為 crouching 姿態下的 `zone=knee`，目的是讓 knee-up 看得到；英文卻寫 `set down by her feet`，而同段 framing 又明說 feet 在畫面外。請改成購物籃位於她彎曲膝蓋旁、從畫面下緣進入構圖，避免模型為了畫腳邊籃子自行拉成全身。

`nico_c02` 的紙箱也建議同樣具體化為「紙箱上緣與打開的箱瓣從畫面下緣升到膝線」，不要只寫 `on the floor`。

### C-40｜P1｜`nico_c10` 的動作時點不一致

前句是 `lifting ... out of the drum`，後句卻是雙手已把衣物抱在胸前。兩個都是合理畫面，但不是同一瞬間。改成 `She has just removed the dried laundry and now stands in front of the open drum, holding the bundle against her chest with both hands.`，可避免模型同時生成伸進滾筒與抱胸兩組手臂。

### C-41｜P0｜outfit_01 應改成「明顯不同的衣服」，不建議把露肩開口正式化

§3-2 的處置能讓文字與必然出圖一致，但沒有處理訓練目的：這件帶兩道辨識度很高的開口會出現在 5/20，且集中於 4/8 clean anchors，容易與 identity 綁定。B2 已實測證明「明顯不同的衣服」可以保臉並服從換裝，因此應利用這個已驗證行為，將 outfit_01 改成與錨點明顯不同的顏色與上身結構，而不是只做很細微的改色。修改後重建這 5 段並重查 framing、包與手部。這比接受 Reference Element 的衣服複製更符合 Soul 訓練的去服裝綁定目的。

### C-42｜P0｜現行排除清單不足以防止已發生的污染

第 6 題答案是「不夠」。`[[S3]]` 幾乎全靠 `no other people／No phone／No photography equipment`，但 §2 已說模型不可靠地執行否定，而且這三類正是先前真的生成過的錯誤。建議改為正面封閉集合：

- third-person：畫面主體只有 Nico；每一隻可見的手都連接到 Nico 的手臂；攝影者與拍攝裝置位於畫面邊界之外；場內照明只來自該列列出的建築燈具／窗光。
- front selfie：畫面就是手機前鏡頭的輸出，拍攝裝置在影像邊界外；可見手臂數與 hands 欄一致。
- mirror selfie：鏡中只有 Nico 與她左手持有的一支手機；右手持修眉刀；每隻可見手都能連回她的手臂。

棚燈、泡棉板、第二人的手若 API 支援獨立 negative prompt，可再放入該欄作輔助，但不能把它當唯一 gate。

### C-43｜P2｜覆核檔的標題與模板編號有殘留漂移

不影響 prompt 本文，但會妨礙後續人工稽核：

- `nico_c03` 標題仍寫「廚房」，實際是早餐店。
- `nico_c04` 標題仍寫「剛醒」，實際是洗澡後。
- `nico_c09` 標題仍寫「房間」，實際是便利商店。
- §6-5 指稱 `[[S8]]` 出現 11 次，實際含 `Her back is not...` 的是 `[[S5]]`。

### 對 §6 七題的直接裁決

1. **有。** C-35、C-38 所列文字命中已證實失效／高風險寫法。
2. **不是全部忠實。** 多數 yaw／pitch／gaze／expression／light 對得上；但 C-36 改壞 body pose，C-39 改壞 prop zone，C-40 混合兩個動作時點，且所有列漏掉全域身材 identity（C-34）。
3. **選替代方案：把 outfit_01 換成明顯不同的衣服。** 理由見 C-41。
4. **有。** 主要是裁切外資訊、包的 carry state、`c09` 背影 cue 與腳邊 basket、`c10` 動作時點。
5. **刪掉。** 而且實際是 `[[S5]]`，不是 `[[S8]]`；正面地標才是有效控制。
6. **不夠。** 改為 C-42 的正面封閉集合；獨立 negative prompt 只能當輔助。
7. **目前不放行。** C-34／C-35／C-36／C-37／C-38／C-39／C-41／C-42 修正並重新展開 20 段後，需再做一次 prompt 層覆核；C-40 可同輪修。修完前不要開始生成。
