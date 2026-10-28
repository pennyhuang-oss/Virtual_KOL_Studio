# M-4 R21：Owner 回饋修正批次的 prompt 規格（10 套 × 2 張）。身分段落沿用 R20（canon，" She wears" 之前），其餘依 Penny 最新回饋重寫。
# H-Rin 的兩張是「改善候選」，Owner 選定的 R20 A 保留不替換。每套 A、B 是同一設計的兩個不同自然姿態或取景。
END = 'Natural skin texture with visible pores, believable light that belongs to the scene, refined colour grading.'
ORDER = ['wear', 'setting', 'moment', 'shot', 'camera', 'comp', 'light']
S = {}

S['H-rin-ayase'] = dict(
    note='保留 R20 A 的貴妃椅橫躺、服裝與夕陽氛圍；改善放鬆度與肩肘腕、手指的承托關係（兩張為改善候選，不取代已選 A）',
    wear='She wears a deep wine-red silk satin cowl-neck slip midi dress with thin straps, a thin gold chain necklace and small gold stud earrings; she is barefoot indoors.',
    setting='Setting: a tidy luxury hotel suite at sunset in winter, a deep green velvet chaise longue with a gently raised, cushioned end beside a floor-to-ceiling window, a soft velvet bolster pillow at the raised end, the city skyline far below in warm evening haze, straight window frames, no text.',
    shot='Shot: her whole reclining figure from head to feet across the frame, with space beyond her head and her feet.',
    camera='Camera: horizontal 16:9, from slightly above her head height as she reclines, tilted slightly down, a 50mm lens from about 3.4 metres, natural perspective.',
    comp='Composition: she lies across the middle of the frame along the chaise, her head on the left at the raised end and her feet on the right, with clear space at both ends, the window and the skyline behind her.',
    light='Light: the low sunset through the window on camera-right lays a warm band of light across her; a gentle fill keeps her face clear; wine red, warm gold and deep green velvet.',
    A=dict(change='姿態：頭靠在抱枕上，手肘落在抱枕、手背輕托臉側；另一手順著身體放在大腿上',
           moment='Moment: she lies on her side along the chaise, completely at ease, her head resting on the soft bolster at the raised end; her lower arm is bent with the elbow sunk into the bolster and the back of her hand resting loosely near her cheek, fingers soft and curled; her upper arm lies along her body with the hand resting on her thigh; her knees are softly bent and her feet relaxed, her whole body sinking into the velvet; she gazes toward the window with a calm, drowsy half-smile, as if resting comfortably after a long day.'),
    B=dict(change='姿態：半躺靠在墊高的一端，一手臂鬆鬆搭在椅背上，另一手放在腰間，頭微側向窗',
           moment='Moment: she reclines on her back against the raised, cushioned end of the chaise, her shoulders and head supported by the bolster, one arm draped loosely along the top of the backrest with the wrist and fingers hanging relaxed, the other hand resting lightly on her waist; her legs are stretched out along the velvet with one knee softly bent; her head tilts toward the window and she looks at the camera from the corner of her eyes with a calm, languid half-smile, fully relaxed.'),
)

S['H-miu-shiraishi'] = dict(
    note='保留成年角色與床上題材；姿態更性感撩人、自然有寫真吸引力；體態依身分與訓練圖核對',
    wear='She wears an ivory satin camisole with thin straps and fine lace trim, matching ivory satin shorts, small gold stud earrings and a thin gold bracelet; she is barefoot indoors.',
    setting='Setting: a small sunlit apartment bedroom on a March morning, a softly rumpled bed with cream linen and plump pillows, sheer white curtains at the window, a wooden bedside shelf with a small potted plant, no text or brands, the room tidy.',
    light='Light: morning light filtered through the sheer white curtains on the left is the key, soft and bright, catching the sheen of the satin and her skin; the white sheets and walls bounce light back into her face; cream white, ivory, light wood and a touch of green.',
    A=dict(change='姿態：趴在床上、前臂撐起上身，小腿往上抬、腳踝交叉，對鏡頭慵懶微笑',
           moment='Moment: she lies on her stomach across the bed, propped on her forearms on a pillow, her calves raised behind her with the ankles loosely crossed in the air; her shoulders are relaxed, one camisole strap has slipped a little down her shoulder, and her chin rests near her hands; she looks into the camera with a sleepy, teasing half-smile and soft, inviting eyes.',
           shot='Shot: her whole figure on the bed from a little above her head to just past her raised feet, the curtains and the window light beside her.',
           camera='Camera: horizontal 16:9, low at the height of the mattress, level, a 50mm lens from about 2.8 metres, natural perspective.',
           comp='Composition: she lies along the bed with her face on the right third, her raised feet toward the left, the window with its glowing sheer curtains behind on the left, the small plant on the shelf at the right edge.'),
    B=dict(change='姿態：跪坐在床上、坐在腳跟上，一手撩頭髮，肩帶微滑，身體微側',
           moment='Moment: she kneels on the rumpled bed sitting back on her heels, her knees slightly apart and her body turned a little to one side; one hand runs slowly through her hair at the back of her head, lifting her arm and lengthening her waist, the other hand rests on her thigh; one camisole strap has slipped off her shoulder; she looks at the camera with a soft, inviting half-smile and slightly parted lips.',
           shot='Shot: her kneeling figure from a little above her head to just below her knees on the bed, the window light beside her.',
           camera='Camera: horizontal 16:9, at her chest height, level, a 70mm lens from about 2.8 metres, natural perspective.',
           comp='Composition: she kneels just right of centre on the bed, the window with its glowing sheer curtains on the left, the soft white bedding around her, the small plant on the shelf at the right edge.'),
)

S['H-tammy-chou'] = dict(
    note='優先修正臉部身分（臉在畫面中放大、表情不誇張、補 canon 臉型句）；衣服與場景重配色（不再用突兀的桃紅）；姿態有情緒與吸引力',
    identity_add=' Her face is a soft heart shape with a broad upper face, rounded cheek transitions, a narrow lower face and a small rounded chin.',
    wear='She wears a fitted soft cream off-the-shoulder knit mini dress with a gently ruched bodice, small gold hoop earrings, a thin gold bracelet and nude pointed heels.',
    setting='Setting: a private garden on a clear April afternoon, a wooden pergola walkway hung with long cascading clusters of lavender wisteria, a smooth pale stone path, fresh green hedges, nobody else in the garden.',
    light='Light: soft afternoon sun filtering through the wisteria from behind and to the left, lighting her hair and shoulders with a warm rim, with dappled light around her; a gentle fill from the front keeps her face clear and evenly lit; lavender, cream, fresh green and warm gold — soft, harmonious colours with nothing loud.',
    A=dict(change='情緒：在紫藤下抬手捧起一串花靠近臉，閉眼聞花香、嘴角上揚（膝上）',
           moment='Moment: she stands under the hanging wisteria and gently lifts one long cluster of blossoms toward her face with one hand, her eyes softly closed and her head tilted slightly as she breathes in the scent, a dreamy, contented smile with her lips gently closed; her other hand rests lightly at her waist.',
           shot='Shot: knee-up, from a little above her head to just below her knees, the wisteria hanging around her.',
           camera='Camera: horizontal 16:9, at her chest height, level, an 85mm lens from about 3.5 metres, natural perspective.',
           comp='Composition: she stands slightly right of centre under the pergola, cascades of wisteria framing the top of the frame and the left side, the stone path receding softly behind her on the left.'),
    B=dict(change='情緒：靠著藤架木柱，回頭越過肩膀看鏡頭，俏皮溫柔的笑（腰上）',
           moment='Moment: she leans one shoulder lightly against a wooden post of the pergola, her body turned away and her face turning back over her shoulder toward the camera with a soft, playful smile and bright eyes, one hand resting on the post at the height of her shoulder, wisteria blossoms brushing near her hair.',
           shot='Shot: waist-up, from a little above her head to just below her waist, the wisteria around her.',
           camera='Camera: horizontal 16:9, at her shoulder height, level, an 85mm lens from about 2.6 metres, natural perspective.',
           comp='Composition: she is on the right third against the post, her face turned toward the left where the wisteria walkway recedes softly into the distance.'),
)

S['H-yerin-han'] = dict(
    note='新方向：坐在草地上享受陽光與球場；移除球桿與打球動作；身體、雙腿與手有自然承托，人景比例協調',
    wear='She wears a white sleeveless fitted knit golf polo, a pale sky-blue pleated golf skirt, white golf shoes and small gold studs.',
    setting='Setting: a gentle grassy slope at the edge of a golf course on a clear late-spring morning, soft green grass, the open fairway rolling away behind her, tall mature trees along the far side, open sky, no flags, carts or signs, nobody else around.',
    light='Light: warm, low morning sun from the left of the frame lights her face and body from the side, crisp and directional, with long soft shadows across the grass; a soft fill keeps her eyes clear under the cap brim; fresh green, white and pale sky blue.',
    A=dict(change='姿態：坐在草地上、雙腿向前伸、腳踝交叉，雙手撐在身後，仰臉閉眼曬太陽',
           moment='Moment: she sits on the grass with her legs stretched out in front of her and her ankles loosely crossed, leaning back with both hands planted flat on the grass behind her, her arms relaxed and taking her weight naturally; she tilts her face up toward the morning sun with her eyes softly closed and a happy, peaceful smile, simply enjoying the sunshine.',
           shot='Shot: her whole seated figure from a little above her cap to just past her shoes, with the fairway and the trees around her.',
           camera='Camera: horizontal 16:9, at her seated shoulder height, level, a 50mm lens from about 5 metres, natural perspective.',
           comp='Composition: she sits on the left third facing the right, the fairway rolling away behind her and to the right, the line of tall trees across the upper part of the frame, plenty of open sky above her cap.'),
    B=dict(change='姿態：側坐草地、雙膝收向一側，一手撐草地、一手輕扶帽簷，望向球道後轉頭對鏡頭笑',
           moment='Moment: she sits on the grass with her knees bent and drawn together to one side, her weight resting on one hand planted on the grass beside her hip, the other hand lightly touching the brim of her cap; she has been gazing out over the sunlit fairway and now turns her head to the camera with a wide, relaxed smile.',
           shot='Shot: her whole seated figure from a little above her cap to just past her shoes, with the fairway behind her.',
           camera='Camera: horizontal 16:9, at her seated chest height, level, a 70mm lens from about 5 metres, natural perspective.',
           comp='Composition: she sits on the right third, the fairway opening out behind her and to the left, the tall trees across the upper middle, the morning sky above.'),
)

S['H-mia-huang'] = dict(
    note='重做可信的場景與人景光線：同一空間、可理解的主光（低角度夕陽／晚霞）、扶欄杆或走在木棧道上的接觸關係；拿掉頭頂燈串與堆疊裝飾',
    wear='She wears a pastel-pink satin corset top with a sweetheart neckline, a white high-waisted A-line mini skirt, white platform sandals, small pearl earrings and a thin silver bracelet.',
    setting='Setting: a real seaside amusement pier at dusk in summer, a long weathered wooden boardwalk with a simple wooden railing, the calm sea beside it, a pink and lavender sunset sky over the water, one Ferris wheel standing far down the pier with its lights just coming on, a few plain lamp posts along the railing, nothing else on the boardwalk, nobody else around.',
    A=dict(change='接觸：雙前臂靠在木欄杆上、身體轉向鏡頭，手拿棉花糖，夕陽從側面照臉',
           moment='Moment: she leans with both forearms resting on the wooden railing, her body turned toward the camera and her weight on one leg, a fist-sized cloud of pink cotton candy held loosely in one hand above the rail; the sea breeze lifts her hair and she gives the camera a playful wink with a teasing half-smile.',
           shot='Shot: knee-up, from a little above her head to just below her knees, the railing and the sea beside her.',
           camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 4.5 metres, natural perspective.',
           comp='Composition: she stands left of centre against the railing, the sea and the sunset sky across the background on the right, the distant Ferris wheel small on the right third, the boardwalk running away behind her.',
           light='Light: the low setting sun just above the sea on the right of the frame is the key, warming the side of her face, her hair and the satin with golden light that matches the sky; the soft glow of the sky fills the shadow side; candy pink, lavender, sea blue and warm gold.'),
    B=dict(change='接觸：走在木棧道上朝鏡頭走來、拿著棉花糖大笑，晚霞為主光',
           moment='Moment: she strolls along the boardwalk toward the camera mid-step, her sandals on the weathered planks, swinging the pink cotton candy loosely in one hand, her other hand brushing the wind-blown hair from her face, laughing as she looks at the camera.',
           shot='Shot: full-length, from a little above her head to just below her sandals on the boardwalk, the railing and the sea beside her.',
           camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 7 metres, natural perspective.',
           comp='Composition: she walks slightly left of centre, the boardwalk and its railing leading from her toward the distant Ferris wheel on the right, the sea and the afterglow filling the right side.',
           light='Light: the bright afterglow of the sky just after sunset lights her softly and evenly from the sea side, with a faint warm rim on her hair; the Ferris wheel lights glow small in the distance; candy pink, lavender, sea blue and warm gold.'),
)

S['H-luna-tanaka'] = dict(
    note='保留 R20 A 的庭院、和服與方向；改善僵硬動作、營造自然有情緒的瞬間；香袋保留但不像展示商品；和服下襬長及腳踝',
    wear='She wears a properly dressed silk kimono in a soft, muted dusty lotus-pink with a fine, small autumn-grass pattern, the left side wrapped over the right with a neat white under-collar, the kimono hem falling to her ankles, a deep plum Nagoya obi tied in a neat drum knot with a pale-gold obijime cord and a cream obiage, white tabi socks and low zori sandals, and a small pearl hair pin above one ear.',
    setting='Setting: the stone-paved garden path of a contemporary Japanese residence on an autumn afternoon, a wide wooden engawa veranda and open sliding shoji doors revealing a clean tatami room, raked white gravel, neatly pruned pines and one maple with red leaves, everything new and well kept, nobody else in the garden.',
    light='Light: slanting autumn afternoon sun through the pine branches from the left, with a gentle fill keeping her face clear; muted lotus pink, deep plum, white gravel and maple red.',
    A=dict(change='瞬間：剛從緣側走下、邊走邊回頭，一手隨意垂著勾住香袋細繩，一手輕扶髮簪',
           moment='Moment: she has just stepped down from the veranda onto the stone path and turns back toward the camera mid-step, as if someone has called her name; one hand hangs relaxed at her side with a small palm-sized cream fabric sachet dangling from her fingers by its short drawstring cord, plain and without logos, the other hand lightly touching the pearl pin in her hair; she smiles shyly and warmly, her sleeves swinging softly with the movement.',
           shot='Shot: full-length, from a little above her head to just below her zori, with the veranda, the open room and the garden around her.',
           camera='Camera: horizontal 16:9, at her hip height, level, a 50mm lens from about 5 metres, natural perspective.',
           comp='Composition: she stands about three-fifths from the left edge, the veranda and the open tatami room behind her on the left, a branch of red maple leaves at the upper right, clear space above her head and below her feet.'),
    B=dict(change='瞬間：站在楓樹下抬頭看飄落的紅葉，一手伸出輕接，香袋細繩勾在另一手指上',
           moment='Moment: she stands beneath the maple, looking up at a red leaf drifting down and reaching out one open hand to catch it, her face in three-quarter view with a soft, wistful smile; the small plain cream fabric sachet hangs from the fingers of her other hand by its short drawstring cord at her side.',
           shot='Shot: full-length, from a little above her head to just below her zori, under the maple with the garden around her.',
           camera='Camera: horizontal 16:9, at her waist height, level, a 70mm lens from about 6 metres, natural perspective.',
           comp='Composition: she stands on the right third under the arching maple branches, the red leaves across the top right, the veranda soft in the background on the left, clear space above her head and below her feet.'),
)

S['H-somi-oh'] = dict(
    note='依 Owner 指示捨棄炸雞店，重新設計：11 月首爾近郊的芒草（銀草）原、黃金時刻逆光；服裝延續暖橘奶油色系',
    wear='She wears a cream cable-knit cropped cardigan buttoned over a fitted rust-orange ribbed knit mini dress, brown suede ankle boots and small red enamel heart earrings.',
    setting='Setting: a wide hillside field of tall silver grass in late November at golden hour, the feathery grass heads glowing silver-gold, a narrow dirt path winding through the field, low hills and a soft hazy sky in the distance, no signs, nobody else around.',
    light='Light: the low golden-hour sun behind her and to the left backlights the silver grass and draws a warm rim around her hair and shoulders; a soft, warm fill from the front keeps her face clear and glowing; silver gold, rust orange, cream and soft sky blue.',
    A=dict(change='設計：走在芒草小徑上，回頭對鏡頭開懷大笑，頭髮被風吹起（全身）',
           moment='Moment: she walks along the narrow path through the tall silver grass and turns back toward the camera mid-step, laughing openly with her eyes curved into crescents and dimples showing, the breeze lifting her honey-orange hair, one hand trailing lightly across the tops of the grass.',
           shot='Shot: full-length, from a little above her head to just below her boots, the silver grass around her.',
           camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 7 metres, natural perspective.',
           comp='Composition: she is on the left third on the path, the glowing silver grass filling the field around her and stretching to the hills on the right, the sun low behind her on the left.'),
    B=dict(change='設計：站在芒草中，雙手縮進開襟衫袖子捧在下巴邊，笑眼看鏡頭（膝上）',
           moment='Moment: she stands among the tall silver grass with her hands tucked into the long sleeves of her cardigan and drawn up near her chin against the evening chill, her shoulders slightly raised, smiling at the camera with her eyes curved into crescents and dimples showing.',
           shot='Shot: knee-up, from a little above her head to just below her knees, the silver grass around her waist and in the foreground.',
           camera='Camera: horizontal 16:9, at her chest height, level, an 85mm lens from about 4 metres, natural perspective.',
           comp='Composition: she stands slightly right of centre, the glowing grass around her waist and soft in the foreground, the field and the hazy hills behind her.'),
)

S['V-jia-seo'] = dict(
    note='依 Owner 指示捨棄溫室，重新設計：2 月的極簡美術館，落地窗冬日柔光、一幅淡藍與薄荷色的大型抽象畫；先建立漂亮可信的人景構圖，再安排自然姿態',
    wear='She wears a white sleeveless mock-neck fitted crop top, a high-waisted mint-sage satin pencil skirt that narrows to just below the knee with a front slit, white strappy sandals and small silver stud earrings.',
    setting='Setting: a bright, minimalist contemporary art gallery on a February afternoon, white walls, a polished pale concrete floor, a tall floor-to-ceiling window letting in soft winter daylight, one large abstract painting in pale blue, mint and white hanging on the wall, a low white bench, nobody else in the room.',
    light='Light: soft, cool winter daylight from the tall window is the key, wrapping gently around her face and body, with a soft reflection on the polished floor; the white walls fill the shadows; white, pale blue, mint and soft grey.',
    A=dict(change='構圖：站在落地窗旁、一側肩膀輕靠窗框，看鏡頭，畫作在另一側（全身）',
           moment='Moment: she stands beside the tall window with one shoulder resting lightly against the window frame, her weight on one leg and the other knee softly bent through the skirt slit, one hand resting at her waistband, looking at the camera with a calm, soft expression.',
           shot='Shot: full-length, from a little above her head to just below her sandals, the window and the painting in the frame with her.',
           camera='Camera: vertical 3:4, at her waist height, level, a 50mm lens from about 4.5 metres, natural perspective with straight vertical lines.',
           comp='Composition: she stands on the left third beside the window, the large pale painting on the white wall to the right of her, the polished floor across the bottom of the frame, clear space above her head and below her feet.'),
    B=dict(change='構圖：側坐在白色矮長椅上、雙腿交疊，面向畫作，回頭看鏡頭（膝上）',
           moment='Moment: she sits sideways on the low white bench facing the painting, her legs crossed with the slit falling open at the knee, one hand resting on the bench beside her, and she looks back over her shoulder at the camera with a quiet, gentle smile.',
           shot='Shot: seated, from a little above her head to just below her knees, the painting behind her.',
           camera='Camera: vertical 3:4, at her seated chest height, level, a 70mm lens from about 3 metres, natural perspective with straight vertical lines.',
           comp='Composition: she sits slightly left of centre on the bench, the large pale painting filling the wall behind her on the right, the window light coming from the left.'),
)

S['V-rainie-hsu'] = dict(
    note='修正眼神：雙眼穩定聚焦看鏡頭；避免讓腿顯短的俯角——相機放低到膝蓋高度、微仰，以自然比例呈現長腿，不拉伸、不變形',
    wear='She wears a black satin halter mini dress, a long black leather trench coat worn open, black pointed stiletto ankle boots and large silver statement drop earrings.',
    setting='Setting: a city street at night just after rain, closed shopfronts with plain frosted glass and no signs or text, one shop window glowing warm amber beside her, the wet pavement reflecting warm and cool light, cool street lights far down the street, nobody else around.',
    light='Light: the warm amber light from the shop window on her right is the key, lighting her face evenly enough to show both eyes clearly; a soft fill keeps the shadow side readable; cool blue street lights and their reflections behind; black, warm amber and cool blue.',
    A=dict(change='姿態：朝鏡頭跨一步、前腳腳尖點地，外套隨步伐敞開，雙眼直視鏡頭（全身，低機位）',
           moment='Moment: she steps forward toward the camera beside the glowing window, her front foot placed in line ahead of the back one with the toe pointed, one hand holding the edge of her open coat at her hip, her chin level, looking straight into the camera with steady, focused eyes — both eyes looking at the lens — and a confident, slight smile.',
           shot='Shot: full-length, from a little above her head to just below her boots, her reflection on the wet pavement at her feet.',
           camera='Camera: vertical 3:4, low at about her knee height, tilted very slightly up, a 50mm lens from about 4.5 metres, natural perspective with natural body proportions.',
           comp='Composition: she stands slightly right of centre, her feet near the bottom of the frame, the wet street and its reflections receding to the left, the warm shop window beside her on the right.'),
    B=dict(change='姿態：背靠發光櫥窗邊框，一膝微彎、腳尖點地，雙眼直視鏡頭（膝上偏全身，低機位）',
           moment='Moment: she leans her back and one shoulder lightly against the frame of the glowing shop window, one knee softly bent with that foot resting on its toe, her other leg straight, both hands loosely holding the open coat at her sides; she turns her face to the camera and looks straight into the lens with calm, steady eyes and slightly parted lips.',
           shot='Shot: from a little above her head to just below her ankles, the glowing window beside her.',
           camera='Camera: vertical 3:4, low at about her knee height, tilted very slightly up, a 70mm lens from about 4 metres, natural perspective with natural body proportions.',
           comp='Composition: she stands on the right third against the window frame, the warm window light filling the right edge, the wet street receding softly on the left.'),
)

S['V-yuna-kim'] = dict(
    note='保留 Owner 認可的銀杏大道場景；改成自然好看的街拍瞬間（走路中、低頭看落葉），不只站定看鏡頭，也不加一串動作；背景字跡模糊不可讀',
    wear='She wears a cream tweed cropped jacket, collarless and buttoned, a matching high-waisted tweed mini skirt, black knee-high leather boots, small pearl earrings and a small plain black shoulder bag without any logos.',
    setting='Setting: a quiet avenue in late autumn lined on both sides with golden ginkgo trees, fallen yellow leaves covering the sidewalk, low modern buildings far behind and softly out of focus with no readable signs, the street empty.',
    light='Light: low afternoon sun behind the ginkgo trees lights the leaves and draws a warm rim on her hair; a gentle fill keeps her face clear; golden yellow, cream and black.',
    A=dict(change='街拍：朝鏡頭走來的步伐中，順手撥開被風吹到臉上的頭髮，眼睛帶笑看鏡頭（全身）',
           moment='Moment: she walks toward the camera along the leaf-covered sidewalk mid-stride, one boot lifting off the leaves, and brushes a strand of wind-blown hair from her face with one hand, her other hand holding the bag strap at her shoulder; she glances at the camera with a natural, smiling look, as if a friend has just called out to her.',
           shot='Shot: full-length, from a little above her head to just below her boots, the golden avenue around her.',
           camera='Camera: vertical 3:4, at her waist height, level, an 85mm lens from about 7 metres, shallow depth of field, natural perspective with straight vertical lines.',
           comp='Composition: she walks slightly left of centre, the ginkgo avenue receding behind her to a soft golden vanishing point at about the height of her hips, clear space above her head and below her boots.'),
    B=dict(change='街拍：停下腳步低頭看腳邊落葉，把頭髮塞到耳後，抓拍到的淺淺笑意（膝上）',
           moment='Moment: she has paused on the sidewalk and looks down at the golden leaves around her boots, tucking her hair behind her ear with one hand, her face in three-quarter view with a small, unguarded smile, caught naturally in the moment.',
           shot='Shot: knee-up, from a little above her head to just below her knees, the golden avenue behind her.',
           camera='Camera: vertical 3:4, at her chest height, level, an 85mm lens from about 3.3 metres, shallow depth of field, natural perspective with straight vertical lines.',
           comp='Composition: she stands slightly right of centre, golden ginkgo leaves softly filling the background, the avenue receding on the left.'),
)
