# R11 — ChatGPT 覆核回覆（Phase C prompt 修正，2026-08-28）

> 原文封存。處置見 `REVIEW_PHASE_C.md` §6-1 與 [`../LEDGER.md`](../LEDGER.md)。
> §6-2 的爭議它撤回自己的判定，同意保留「某部位在畫面外」；
> C-35/36/38/39/40/41/43 結案；新開 C-44–C-47（3 條 P0）；三列語意重審均無異議。

## ChatGPT R11 覆核回覆

### §6-2 裁決

**同意保留景別句尾的 `... are outside the picture`。**

我撤回 R10 對這一小段的判定。它前面已有明確的裁切線位置，後句是在陳述各部位相對於該邊界的空間位置；它不等同於單獨用 `nothing below...` 要模型自行推導裁切位置。更重要的是，probe_v2、probe_v3、B2 第二次已有三次同配方成功的實測。現階段保留已驗證配方，比為了形式上的「零排除句」改動它更合理。

因此 C-35 在其餘否定式均已移除的前提下可結案；lint 也不應把 `outside the picture` 這種有明確邊界前件的 locative statement 當成失效否定。

### C-44｜P0｜身材、朝向與相機模板仍未真正依 framing 分層

C-34 的身材內容已補回，但目前三版實際仍跨用了不可見區域：

- `[[BODY-1]]` 同時用於 full_body 與 knee_up；`nico_c02／c05／c09／c11` 在 lower legs／feet 位於畫面外時，仍要求 `long straight legs`。
- `[[BODY-2]]` 同時用於 chest_up 與 waist_up；`nico_a02／a03／a04／a05／c07／a08` 在腰位於畫面外時，仍要求 `a narrow waist`。
- `[[CAMERA-1]]` 對 face_closeup 也寫 `her face, her body and the background all stay in focus`，會重新要求模型容納不存在於畫面的 body。
- `nico_a01／c01` 的 face_closeup 後接 `[[FACING-3]]`，其中 `The camera sees ... her chest`，但畫面下緣只到鎖骨附近。
- outfit 分層也還有少數殘留：`nico_c01` 的 face_closeup 仍寫 `the hem long and tucked in`；`nico_a04／a05` 的 chest_up 仍寫上衣下擺位於 natural waist。

請至少拆成 face_closeup／chest_up／waist_up／knee_up／full_body 五種可見性模板。相機句可統一改成 `all visible parts of her and the background stay in focus together`，避免逐景別另列 body。這項未修前，C-34 與 C-37 都不能結案。

### C-45｜P0｜第三人稱封閉集合在戶外產生光源與場景矛盾

`[[CLOSED-SET-1]]` 固定寫：

> The only light in the room comes from the fixtures and windows named above.

它也套在公園、街道等戶外列；戶外沒有 room、fixture 或 window，真正光源是 sky。這會直接與前面的 overcast skylight 衝突。

建議改成跨場景成立的：

> Illumination comes exclusively from the natural or architectural light sources named above.

另外，mirror 版的 `the mirror holds her and the single phone ... that is the whole of what it holds` 容易被理解成鏡中沒有浴室背景。應把封閉範圍限縮為人物與裝置，例如「鏡中浴室場景內只有 Nico 與她手上的一支手機」。

C-42 目前不能結案。

### C-46｜P0｜`WHO-SHOOTS-1` 又把第二個人顯式帶回 prompt

18 段都先寫 `Someone standing near her...`，最後才要求唯一人物是 Nico。這兩句在語意上可以靠「攝影者在畫外」解釋，但對曾經生成別人的手與手機的模型而言，前一句仍是強烈的人物 cue，正好抵消 C-42 的目的。

改成不引入 person token 的相機位置敘述，例如：

> The camera viewpoint is nearby at eye level, with the imaging device and its operator beyond the frame edge.

如此仍能表達 third-person view，又不先要求模型想像 `Someone`。

### C-47｜P1｜ring 的可見性不能只由 framing 決定

C-37 的服裝分層整體方向正確，鞋子在 waist_up／knee_up 被砍掉也正確；但戒指應由「配戴在哪隻手＋該手是否入鏡」決定，而不是只看 framing。

outfit_01 有一枚銀戒；目前 `nico_a02／a03／c07` 都有手在胸前入鏡，prompt 卻把 ring 砍掉，反而 full_body 的 `nico_a07` 有輸出。請補 ring laterality，或明定該列不配戴；不要以 chest_up 一律刪除。這不必單獨阻擋 Nico，但應與本輪 P0 一起修。

### C-34～C-43 結案判定

| ID | 判定 |
|---|---|
| C-34 | **不同意結案**：身材已補回，但 framing 分版仍不完整，見 C-44 |
| C-35 | **同意結案**：並同意保留有明確裁切線前件的 `outside the picture` |
| C-36 | **同意結案** |
| C-37 | **不同意結案**：主要修正成立，但仍有不可見身材／衣服細節與 ring 過濾問題，見 C-44、C-47 |
| C-38 | **同意結案** |
| C-39 | **同意結案** |
| C-40 | **同意結案** |
| C-41 | **同意結案**：新 outfit 與錨點在顏色、織法、領型上已明顯區隔 |
| C-42 | **不同意結案**：見 C-45、C-46 |
| C-43 | **同意結案** |

### 三列重審

- **`nico_c03`**：結構欄位彼此成立；早餐店 pillar、scene、坐姿、視線、雙手、桌面道具、混合光與 waist_up 相容。**列本身無異議**。其 prompt 仍受 C-44／C-46 共用模板影響，模板修正後再簽 prompt hash。
- **`nico_c04`**：結構欄位彼此成立；洗澡後濕髮、平靜表情、床邊坐姿、front selfie、雙手、道具與晨光相容。**列本身無異議**。其 prompt 仍受 C-44 的 camera 可見性措辭影響。
- **`nico_c09`**：C-38／C-39 的兩處修正正確；蹲姿仍呈現胸前正面、轉頭看鏡頭、購物籃靠彎曲膝並從下緣入鏡，物理上成立。**列本身無異議**。其 prompt 仍受 C-44 的 knee_up 身材模板及 C-45／C-46 共用模板影響。

### 放行判定

**目前仍不放行生成。** 先修 C-44、C-45、C-46；C-47 可同輪處理。修正後不必重掃未受影響的內容，但需要重審所有被修改共用模板展開到的列，並重新簽 prompt hash。
