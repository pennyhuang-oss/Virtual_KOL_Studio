# 覆核請求 R8a：重寫後的 prompt（第一批，高風險 7 件）

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄或讀 repo 背景（連接器爬整個 repo 會一次耗掉使用者 5 小時用量）。
> 判斷所需內容已全部貼在下面。回覆填在最後的「回覆區」，不要改問題本文。

R7 的五題判定已全部照做：13 件已整併成「有效規格」，手部任務獨立成列
（可見性型、允許 off-frame／N/A），抽象飄動移出，硬驗收重新產生，再由規格派生 prompt。
依 R7 Q5 **逐件回 PASS／REVISE／BLOCK**；依「閱讀分批」建議先送高風險 7 件，其餘 6 件另送。

> 本檔 12KB，超過協定裡 8KB 的目標。背景已砍到最精簡，剩下的是 R7 指定必附的
> 逐件內容（有效規格／手部任務／prompt／硬驗收）。13 件拆得更碎只會讓標頭重複更多次、
> 總讀取量更大，所以選 7＋6 兩批。

## 我最不確定的一件事（請優先看）

**光線句是新寫法。** YG-04 的 A/B 測出舊寫法
`background exposed the same brightness as her skin` 會讓背景與臉只差 0.03–0.11 級、
臉部反差 0.0 級；新寫法拉到 0.37–0.43 級。但你說過不要因一組 2 張就批次改寫，
**高反差場景也還沒驗證**。

我沒有套單一全域字串，改成**每件依它自己的光學設定宣告寫**：
宣告「低反差」→ 臉均勻曝光＋背景 staying slightly darker（本批 1 件）；
宣告「取捨」→ 臉受光＋**具名的那一邊** allowed to clip（本批 6 件）。

**「取捨」寫法完全沒實測過。** 顧慮是：明寫某區過曝，可能把 D-04 好不容易解掉的
臉部逆光叫回來。我把「臉受光」與「某處犧牲」寫成兩個並列子句，讓臉永遠不是被犧牲那邊——
但這只是推論，沒有證據。**風險太高請直接要求改回。**

---

## YG-03｜陽台・收乾淨的衣服

**半身自拍。**　|　反射面：具名（白牆回冷色填光）｜曝光：低反差（有遮蔽陽台、霧面窗板）｜色溫：不適用（單一天光）

- **凍結瞬間**：把已經收下來、折好的白毛巾抱在胸前，對鏡頭笑的那一瞬間。
- **手部任務**：拍攝手／鏡外手：持手機自拍，**off-frame**（仍佔一隻解剖學的手） ／ 可見手 A：把折好的白毛巾按在胸前 ／ 可見手 B：**N/A**——兩隻手已用完
- **硬驗收**：① 自拍構圖成立且**手機不入鏡** ② **只有一隻可見手**，抓著毛巾 ③ 畫面無任何印刷文字 ④ 半身比例與光線正確

```text
In a phone selfie, a young woman presses a folded plain white towel against her chest with one visible hand, smiling at the camera. Close half-body framing, camera just above her eye level. Collarbone-length mocha brown hair in a low ponytail, see-through bangs, loose strands at her temples. A plain grey fitted cropped cotton tee, high-waisted black shorts, black-rimmed glasses. A narrow covered apartment balcony, a white painted wall, an iron window grille, a steel drying pole holding plain towels and pale bedsheets. Flat overcast daylight on her face, her face evenly exposed, the white wall bouncing cool fill onto her jaw and staying slightly darker than her skin. Natural skin texture, subtle film grain.
```

## YG-07｜客廳地板・什麼都沒發生

**半身坐姿。**　|　反射面：具名（淺色地板回彈補下巴）｜曝光：取捨（窗邊失細節）｜色溫：分裂（窗光冷白 vs 角落暖立燈）

- **凍結瞬間**：坐在地上，一手滑手機、另一手伸進零食袋，嘴裡還在嚼、一邊臉頰鼓著，眉毛抬起看鏡頭。
- **手部任務**：可見手 A：拿著手機在滑（**手機入鏡**，這件不是自拍） ／ 可見手 B：伸進零食袋 ／ 無第三個手部任務
- **硬驗收**：① 坐在地上 ② 一手滑手機、一手伸進零食袋（**可見手剛好兩隻**）③ 一邊臉頰鼓著 ④ 半身坐姿比例

```text
A young woman sits on the living room floor scrolling her phone in one hand while her other hand reaches into a snack bag, one cheek full mid-chew, eyebrows raised at the camera. Half body, camera level with her face as she sits. Collarbone-length mocha brown hair, the top half clipped up and the lower half loose. A beige camisole, matching short cotton shorts, bare feet. A small apartment living room, a low sofa, magazines on the floor, a fan in the corner. Cool window light on her face, a warm lamp glowing behind her, the pale floor bouncing fill onto her chin, the window itself allowed to clip to white. Natural skin texture, subtle film grain.
```

## YG-08｜台式早餐店・第一則吃

**半身，人＋食物同框。**　|　反射面：具名（不鏽鋼餐檯回彈補下巴）｜曝光：取捨（門口天光失細節）｜色溫：分裂（門口冷白 vs 店內日光燈）

- **凍結瞬間**：單手拿著蛋餅咬下一口，另一手對鏡頭比大拇指，鼻子微微皺起在笑。
- **手部任務**：可見手 A：拿著蛋餅送到嘴邊、正在咬 ／ 可見手 B：對鏡頭比大拇指 ／ 無第三個手部任務
- **硬驗收**：① **單手**拿蛋餅咬 ② 另一手比大拇指 ③ 人與食物同框 ④ 襯衫下擺在腰際打結、露一截腰

```text
A young woman bites into an egg crepe held in one hand and throws a thumbs up with her other hand, nose slightly scrunched, eyes crinkled. Half body with the food in frame, camera level with her chest. Collarbone-length soft wavy mocha brown hair, side-parted, a small pearl clip on one side. A light blue short-sleeve shirt knotted at the waist, white high-waisted shorts. A breakfast shop, a stainless steel counter, red plastic stools, a metal tray, iced tea in a tall glass. Cool daylight from the doorway on her face, warm fluorescent light inside, the steel counter bouncing fill onto her chin, the doorway behind her allowed to clip. Natural skin texture, subtle film grain.
```

## YG-10｜百貨美妝櫃・精緻的一面

**半身。**　|　反射面：具名（白檯面與鏡面柱回彈）｜曝光：低反差（百貨均勻嵌燈）｜色溫：分裂（嵌燈冷白 vs 玻璃櫃內暖重點光）

- **凍結瞬間**：把試完色的手背舉在臉旁，抬眼看鏡頭，一邊眉毛挑起、同側嘴角上揚。
- **手部任務**：可見手 A：手背朝上舉在臉旁展示試色 ／ 可見手 B：自然垂放，**風衣掛在該側前臂**（承重在前臂，不是手部任務） ／ 無第三個手部任務
- **硬驗收**：① 試色的手背舉在臉旁 ② **臉部區域只有一隻手** ③ 風衣掛在另一側前臂 ④ 半身比例

```text
A young woman holds her swatched hand up beside her face, her other arm relaxed at her side with a trench coat draped over that forearm, one eyebrow raised and the same corner of her mouth lifted. Half body, camera level with her chest. Sleek glossy collarbone-length mocha brown hair, side-parted, ends curving slightly inward. A cream cropped fitted knit top, matching off-white high-waisted straight trousers, gold hoop earrings. A department store beauty floor, glass counters, rows of lipsticks, mirrored columns. Cool recessed ceiling light on her face, warm accent light inside the glass cases, the white counter bouncing fill onto her chin, the floor behind her slightly darker. Natural skin texture, subtle film grain.
```

## LG-02｜房間晨光・第一則「她在台北」

**3/4 身（膝上）。**　|　反射面：具名（白牆與淺木地板整體回彈）｜曝光：取捨（窗外壓白）｜色溫：不適用

- **凍結瞬間**：蹲下來，一手的指尖停在地板的光斑上，另一手揉著一隻眼睛，嘴巴打呵欠打到一半。
- **手部任務**：可見手 A：指尖停在地板光斑上 ／ 可見手 B：揉一隻眼睛 ／ 無第三個手部任務
- **硬驗收**：① 蹲姿 ② 一手指尖在地板光斑上 ③ 另一手揉眼 ④ 3/4 身比例、赤腳

```text
A young woman crouches with her knees together, the fingertips of one hand resting on a sunlit patch of the floor while her other hand rubs one eye, her mouth caught mid-yawn. Three-quarter body, camera level with her face as she crouches, shot from well back. A blunt chin-length black bob cut evenly at the jawline, sleep-mussed with one side flattened. A white lace-trimmed camisole pyjama top, matching short pyjama shorts, bare feet. A bright clean room, white walls, a pale wood floor, a half-unpacked cardboard box in the corner. Soft morning light on her face, the white walls bouncing fill back onto her, the window allowed to clip to white. Natural skin texture, subtle film grain.
```

## LG-05｜公車站・雨停前

**3/4 身（膝上）。**　|　反射面：具名（濕柏油把對街招牌的暖色反上來）｜曝光：取捨（招牌高光失細節）｜色溫：分裂（雨後冷天光 vs 對街暖招牌）

- **凍結瞬間**：站在候車亭邊緣，一手握著收起的透明傘、傘尖朝下貼在腿側，另一手在臉頰旁比 V，頭往同側傾著笑。
- **手部任務**：可見手 A：握著收起的透明傘柄，傘身朝下垂在腿側 ／ 可見手 B：在臉頰旁比 V ／ 無第三個手部任務
- **硬驗收**：① 一手握收起的透明傘、**傘尖朝下貼腿側**（不可浮空）② 另一手在臉頰旁比 V ③ 襯衫扣到胸口、不露 ④ 3/4 身比例

```text
A young woman stands at a bus shelter, one hand gripping the curved handle of a folded clear umbrella its closed canopy hanging straight down beside her thigh, her other hand making a V sign beside her cheek, head tilted, eyes crinkled. Three-quarter body, camera at her navel level, shot from well back. A blunt chin-length black bob with even blunt ends along the jawline. An opaque off-white cotton short-sleeve button-front blouse fastened through the chest, a pale blue checked skirt with one continuous hem around her thighs. A colourful route map lightbox, wet asphalt throwing warm shop-sign colour back onto her, the brightest signs allowed to clip. Her face clearly lit. Natural skin texture, subtle film grain.
```

## LG-10B｜浴衣・蘋果糖（半身）

**半身。**　|　反射面：具名（參道地面回彈暖光）｜曝光：取捨（燈籠高光失細節）｜色溫：分裂（燈籠暖橘 vs 天空殘藍）

- **凍結瞬間**：站定，一手把蘋果糖舉在臉頰旁、另一手扶著髮簪，笑到眼睛彎起來。
- **手部任務**：可見手 A：把蘋果糖舉在臉頰旁 ／ 可見手 B：扶著半盤髮上的和風髮簪 ／ 無第三個手部任務
- **硬驗收**：① 一手舉蘋果糖在臉頰旁 ② 另一手扶髮簪 ③ 浴衣**左襟在上**、半幅帶綁緊收腰 ④ 半身比例

```text
A young woman holds a candy apple up beside her cheek with one hand and steadies the hairpin in her half-up bob with her other hand, laughing with her eyes crinkled. Half body, camera level with her chest. A blunt chin-length black bob cut evenly at the jawline, half-pinned up with a Japanese hairpin, two strands at her temples. A pale-blue floral yukata, an ankle-length wrap robe with the left front panel crossed over the right, a wide flat navy obi sash. Paper lanterns overhead, a blurred food stall, the last blue of the sky. Warm lantern light on her face, the approach underfoot bouncing warm fill up, the lanterns themselves allowed to clip. Natural skin texture, subtle film grain.
```

---

## 回覆區（請只填這一段）

### 光線句（全批適用）
- **判定**：REVISE
- **理由**：低反差寫法可以保留；它至少已有 YG-04 的方向性證據，而且本批 YG-03 的白牆補光與「背景略暗於膚色」是同一套可理解的光學關係。未實測的風險在「某區 allowed to clip」：這是生成命令，不只是攝影容許值，可能把整片窗／門口／招牌／燈籠推成大面積死白，並連帶壓暗或逆光臉部。現有 2 張低反差結果不能外推成 6 個高反差場景已驗證。
- **建議改法**：不要改回舊的同亮度句，也不要一次放行 6 件。把取捨句統一成「臉部保留自然膚色與高光細節；具名光源是畫面最亮處，只有局部最高光可到白色」，再先選一個窗／門口類與一個點光源類各做最小 preflight。例：`Her face is clearly exposed with natural skin texture; the doorway is the brightest area, with only its small brightest region reaching white.` 通過後才能擴到同類場景，不能把窗類結果直接當成燈籠／招牌類證據。

### YG-03
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：凍結瞬間與一隻可見手的解剖分配成立，低反差光線也與場景一致；但 prompt 只寫 `one visible hand` 修飾毛巾動作，沒有明確封住自拍手、手機或第二隻手入鏡，硬驗收①②仍可能失敗。
- **建議改法**：在第一句後加：`The frame contains exactly one visible hand; her phone and camera-holding hand stay outside the frame.` 其餘可保留；光線依上方低反差寫法原樣送 preflight。

### YG-07
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：兩手任務與單一瞬間清楚，沒有第三個動作；但半身坐姿同時寫 `bare feet` 會誘使模型拉遠或把腿腳塞進構圖，而赤腳並非本件硬驗收。另 `scrolling` 是時間動作，靜態畫面以拇指停在螢幕上更可驗收。
- **建議改法**：刪除 `bare feet`；首句改為 `holds her phone in one hand with her thumb resting on the screen, while her other hand is inside the open snack bag`，並補 `Exactly two hands are visible.` 光線改用上方「局部最高光」版本後送 preflight。

### YG-08
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：單手持蛋餅咬、另一手比讚是同一瞬間且兩手角色互斥；半身、人食同框、打結衣襬也都直接寫入，沒有構圖與硬驗收衝突。門口作為最高亮區在光學上合理。
- **建議改法**：內容可送；只把全批未驗證的 `doorway behind her allowed to clip` 換成上方「門口最亮、僅局部最高光到白、臉保留細節」句，並把這張列入門口／窗類 preflight。

### YG-10
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：手部任務數量正確，但 `swatched hand` 沒明說手背朝鏡頭，可能生成掌心或手指試色；`mirrored columns` 又可能複製手、臉或人物，直接威脅「臉旁只有一隻手」的驗收。
- **建議改法**：首句改成 `holds the back of one swatched hand facing the camera beside her face`。把背景改成 `mirror-faced columns reflecting only soft, out-of-focus ceiling lights`，並補 `Her reflection is outside the composition.` 若流程不接受否定式，直接把 `mirrored columns` 換成 `glossy pale columns`，不要用鏡面來賭肢體去重。

### LG-02
- **判定**：PASS ／ REVISE ／ BLOCK → BLOCK
- **理由**：規格內部不可同時驗收：畫幅定義為膝上 3/4 身，硬驗收卻要求赤腳；赤腳必須看見腳，膝上構圖必然把腳裁掉。加上手指碰地板的動作，模型為了交代手、光斑與腳，很可能自行拉成全身，不能靠 prompt 小修同時滿足兩者。
- **建議改法**：先決定唯一真相來源。若比例優先，從硬驗收④與 prompt 刪除赤腳，只驗收到膝上；若赤腳是敘事必要條件，將規格與硬驗收改成全身／至少完整到腳，並相應調整 `Three-quarter body`。在兩者統一前不要送生成。

### LG-05
- **判定**：PASS ／ REVISE ／ BLOCK → BLOCK
- **理由**：膝上 3/4 身與「完整確認傘尖朝下貼腿側」也互相衝突。手在髖部附近時，一把收起的長傘通常延伸至膝下；現有構圖可能裁掉傘尖，硬驗收①便無法從成品證明，模型也可能為保留整把傘自行改成更遠景。此外英文首句在 `umbrella its closed canopy` 之間缺少連接結構。
- **建議改法**：若傘尖可見是硬條件，將構圖改為至少到小腿中段，並寫 `one hand gripping the curved handle of a folded clear umbrella, with its entire closed canopy and downward-pointing tip visible beside her leg`；若必須維持膝上構圖，就把硬驗收改成「傘身垂直貼大腿、下端可 off-frame」，不可仍要求驗到傘尖。兩者統一後再送。

### LG-10B
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：兩手任務與半身瞬間成立；但半身 prompt 寫 `ankle-length` 會對模型發出展示全長服裝的訊號，增加拉遠風險。左右襟也應鎖定為穿著者視角，否則 `left` 可能被解讀成畫面左側。
- **建議改法**：刪除半身不可驗收的 `ankle-length`，改成 `a pale-blue floral yukata with the wearer’s left front panel layered over the wearer’s right, secured by a wide flat navy obi`。燈籠光線依上方改成只有局部最高光到白，並把本件列為點光源類 preflight。

### 其他（只寫會導致生成失敗的項目）
- YG-10 若保留鏡面，反射人物／肢體必須列入硬驗收，否則「實體手剛好兩隻」通過時仍可能留下鏡中多手。
