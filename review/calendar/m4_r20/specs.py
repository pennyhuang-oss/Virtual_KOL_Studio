# M-4 R20：20 套 × A／B 的 prompt 組裝規格。
# A＝R6 v3 已覆核設計（cal_m4_r6_replan.json rewrites）＋後續 Owner 決定；身分句（canon）取自企劃 prompt 原文、不改。
# B＝同一角色、月份、服裝與場景方向，只改一項主要安排（取景／站位／自然姿態）。
# 收尾句用 R6-10 end_line 去掉已移除的 photobook 片段。
END = 'Natural skin texture with visible pores, believable light that belongs to the scene, refined colour grading.'

S = {}

S['H-iris-chen'] = dict(
    wear='She wears a sunflower-yellow structured cotton bustier crop top with thin straps, a matching low-rise mini skirt with a small side slit, flat white strappy sandals, a thin gold chain necklace and small gold stud earrings.',
    setting='Setting: a summer bay in the late morning, a wide, flat and dry pale rock shelf well back from the water, clear turquoise water, a distant green headland and a clean blue sky, the shore empty.',
    moment='Moment: she stands on the rock shelf with both hands resting lightly on her hips at the low waistband, her weight on one leg, smiling brightly into the camera as the sea breeze lifts her hair.',
    shot='Shot: full-length, from a little above her head to just below her sandals, with the bay and the headland around her.',
    camera='Camera: horizontal 16:9, at her hip height, level, a 50mm lens from about 5.5 metres, natural perspective.',
    comp='Composition: she stands about two-fifths from the left edge, the turquoise bay and the green headland opening out on the right, the sea horizon at the height of her hips across the middle of the frame, clear space above her head and below her feet.',
    light='Light: bright late-morning sun from high front-left, with a gentle fill keeping the shadows on her face soft; sunflower yellow, turquoise and pale rock grey.',
    B=dict(change='取景：改為膝上近一點',
           shot='Shot: knee-up, from a little above her head to just below her knees, the bay and the headland behind her.',
           camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 4.5 metres, natural perspective.',
           comp='Composition: she stands left of centre, the turquoise bay and the green headland soft behind her on the right, the sea horizon behind her hips.'))

S['H-luna-tanaka'] = dict(
    wear='She wears a properly dressed silk kimono in a soft, muted dusty lotus-pink with a fine, small autumn-grass pattern, the left side wrapped over the right with a neat white under-collar, a deep plum Nagoya obi tied in a neat drum knot with a pale-gold obijime cord and a cream obiage, white tabi socks and low zori sandals, and a small pearl hair pin above one ear.',
    setting='Setting: the stone-paved garden path of a contemporary Japanese residence on an autumn afternoon, a wide wooden engawa veranda and open sliding shoji doors revealing a clean tatami room, raked white gravel, neatly pruned pines and one maple with red leaves, everything new and well kept, nobody else in the garden.',
    moment='Moment: she has paused on the path in front of the veranda, both hands resting together just below her obi, lightly holding a small palm-sized cream fabric sachet with a short drawstring cord, plain and without any logos; her body is turned about 30 degrees toward camera-left and her face turns to the camera with a sweet, gentle smile.',
    shot='Shot: full-length, from a little above her head to just below her zori, with the veranda, the open room and the garden around her.',
    camera='Camera: horizontal 16:9, at her hip height, level, a 50mm lens from about 5 metres, natural perspective.',
    comp='Composition: she stands about three-fifths from the left edge, the veranda and the open tatami room behind her on the left, a branch of red maple leaves at the upper right, clear space above her head and below her feet.',
    light='Light: slanting autumn afternoon sun through the pine branches from the left, with a gentle fill keeping her face clear; muted lotus pink, deep plum, white gravel and maple red.',
    B=dict(change='取景：改為膝上',
           shot='Shot: knee-up, from a little above her head to just below her knees, the veranda and the open room soft behind her.',
           camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 4.2 metres, natural perspective.',
           comp='Composition: she stands right of centre, the veranda and the tatami room soft behind her on the left, red maple leaves at the upper right edge.'))

S['H-somi-oh'] = dict(
    wear='She wears a fitted cream rib-knit cropped cardigan worn open over a rust-orange ribbed square-neck camisole with thin straps, a high-waisted rust-orange knit mini skirt, brown heeled loafers and small red enamel heart earrings.',
    setting='Setting: a small retro Korean snack bar on a late-autumn night before opening, a warm orange tiled counter, a row of red leather bar stools, plain tiled walls with no menus or text, a warm pendant lamp hanging above the counter and a small plate of golden fried chicken resting soft and out of focus at the right edge, nobody else inside.',
    moment='Moment: she leans one hip lightly against the tiled counter, one hand resting on the counter edge and the other tucking her hair behind her ear, laughing openly at the camera with her eyes curved into crescents and dimples showing.',
    shot='Shot: knee-up, from a little above her head to just below her knees, the counter and the stools beside her.',
    camera='Camera: horizontal 16:9, at her waist height, level, a 70mm lens from about 4 metres, natural perspective.',
    comp='Composition: she stands on the left third, the orange counter and the row of red stools running away to the right, the pendant lamp glowing just above her.',
    light='Light: the warm pendant lamp above and slightly in front of her is the key, lighting her face, her hair and the counter, with the shop\'s other warm lights around her; a soft fill keeps her face clear while the pendant stays the most distinct light; warm orange, red and cream.',
    B=dict(change='姿態：改為側坐在紅色高腳椅上',
           camera='Camera: horizontal 16:9, at her seated chest height, level, a 70mm lens from about 4 metres, natural perspective.',
           comp='Composition: she sits on the nearest stool on the left third, the orange counter and the row of red stools running away to the right, the pendant lamp glowing just above her.',
           moment='Moment: she sits sideways on one of the red bar stools, one forearm resting on the counter and her other hand on her knee, laughing openly at the camera with her eyes curved into crescents and dimples showing.',
           shot='Shot: knee-up, from a little above her head to just below her knees, the counter beside her.'))

S['H-coco-wu'] = dict(
    wear='She wears a white linen sundress with thin straps, a fitted ruched bodice with a soft V neckline, a cinched waist and a flared mini skirt, flat white sandals and a white daisy hair clip.',
    setting='Setting: a wide lavender field in early summer in the late afternoon, long purple rows running into the distance and gathering behind her, the rows natural rather than perfectly even, a few soft green trees on the horizon, the field empty.',
    moment='Moment: she stands between the rows holding a straw sun hat loosely at her side with one hand and tucking her hair behind her ear with the other, laughing at the camera with her eyes squeezed into crescents and deep dimples showing.',
    shot='Shot: knee-up, from a little above her head to just below her knees, the lavender rows around her.',
    camera='Camera: horizontal 16:9, at her chest height, level, an 85mm lens from about 4.5 metres, natural perspective.',
    comp='Composition: she is centred, the lavender rows converging behind her as leading lines, the line of trees low behind her waist and well clear of her head.',
    light='Light: the low late-afternoon sun behind her draws a warm rim along her hair and shoulders; a soft fill from the front keeps her face clear without overpowering the rim, her warm skin tone matching the sunset field; lavender, warm gold and white.',
    B=dict(change='取景：改為全身，花田更開闊',
           shot='Shot: full-length, from a little above her head to just below her sandals, with the lavender rows stretching around her.',
           camera='Camera: horizontal 16:9, at her waist height, level, a 50mm lens from about 5.5 metres, natural perspective.',
           comp='Composition: she stands in the centre of the field, the rows converging to the horizon behind her, the trees low on the horizon, clear space above her head and below her feet.'))

S['H-mia-huang'] = dict(
    wear='She wears a pastel-pink satin corset top with a sweetheart neckline, a white high-waisted A-line mini skirt, white platform sandals, small pearl earrings and a thin silver bracelet.',
    setting='Setting: a seaside amusement pier at dusk in summer, a wooden boardwalk with a railing, a pink and lavender sunset over the sea, a lit Ferris wheel and amusement lights far behind softening into bokeh, no signs or text, nobody else around.',
    moment='Moment: one hand rests on her hip and the other holds a fist-sized cloud of pink cotton candy beside her chin; she gives the camera a playful wink with a teasing half-smile.',
    shot='Shot: waist-up, from a little above her head to just above her hips, the dusk sky and the lights behind her.',
    camera='Camera: horizontal 16:9, at her chest height, level, an 85mm lens from about 3.2 metres, natural perspective.',
    comp='Composition: she is slightly left of centre, the glowing Ferris wheel bokeh behind her shoulder on camera-right, the sea horizon low behind her waist.',
    light='Light: a string of warm bulbs just above her is the key, its warm glow falling on her face, her hair and the satin; the dusk sky gives the background its blue-violet; a gentle fill keeps her face clear; candy pink, blue-violet and warm gold.',
    B=dict(change='取景：改為大腿中段以上，帶到欄杆與海面',
           shot='Shot: mid-thigh-up, from a little above her head to mid-thigh, the boardwalk railing and the sea beside her.',
           camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 4.3 metres, natural perspective.',
           comp='Composition: she stands left of centre beside the railing, the sea and the pink and lavender sky across the background, the Ferris wheel lights glowing on camera-right.'))

S['H-yuna-kim'] = dict(
    wear='She wears an open white cropped shearling jacket, a fitted dusty-rose fine-rib square-neck long-sleeve knit top, a high-waisted pale-grey wool mini skirt, pale-grey suede knee-high boots and thin silver earrings.',
    setting='Setting: a quiet birch forest on a winter morning after fresh snow, slim white trunks in even rows, a path covered with smooth new snow, a little soft mist far back, no signs, the forest empty.',
    moment='Moment: she stands at the side of the path gathering the collar of her jacket together at her chest with both hands, breathing out a soft cloud of white breath, looking down the path with a faint smile.',
    shot='Shot: knee-up, from a little above her head to just below her knees, the birch trunks around her.',
    camera='Camera: horizontal 16:9, at her chest height, level, an 85mm lens from about 4.7 metres, natural perspective.',
    comp='Composition: she stands on the left third, her body and gaze turned toward the right where the snowy path recedes between the trunks, the white trunks making an even vertical rhythm with her.',
    light='Light: soft, diffused early-morning light among the trees with bright bounce from the snow; a cool white fill keeps her face clear without being brighter than the snow light; white, ash grey and dusty rose.',
    B=dict(change='取景：改為全身，帶到長靴與雪地小徑',
           shot='Shot: full-length, from a little above her head to just below her boots, the snowy path and the trunks around her.',
           camera='Camera: horizontal 16:9, at her waist height, level, a 50mm lens from about 6 metres, natural perspective.',
           comp='Composition: she stands on the left third at the edge of the path, the path receding to the right between the trunks, clear space above her head and below her boots.'))

S['H-tammy-chou'] = dict(
    wear='She wears a fitted hot-pink square-neck rib-knit mini dress, white pointed slingback heels, gold hoop earrings and a thin gold bracelet.',
    setting='Setting: a private garden on a clear April afternoon, a smooth pale stone path, neatly trimmed hedges, white flowering trees and beds of tulips on both sides, no bench or garden furniture, the garden empty.',
    moment='Moment: she walks toward the camera along the stone path with small, easy steps, laughing out loud as she looks at the camera.',
    shot='Shot: full-length, from a little above her head to just below her heels, with the path, the hedges and the white blossoms around her.',
    camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 10 metres, natural perspective.',
    comp='Composition: she is slightly right of centre, the stone path running in from the lower left to her feet, white blossoms and green hedges framing both sides; her hot-pink dress is the only strong colour in the frame.',
    light='Light: the spring afternoon sun from the left and slightly behind her makes the blossoms glow and outlines her hair; a soft fill keeps her face clear; hot pink, white and fresh green.',
    B=dict(change='姿態：改為在步道上停步站定',
           moment='Moment: she has stopped on the stone path, standing with her weight settled and one foot slightly forward, her hands relaxed at her sides, laughing out loud as she looks at the camera.'))

S['H-rin-ayase'] = dict(
    wear='She wears a deep wine-red silk satin cowl-neck slip midi dress with thin straps, a thin gold chain necklace and small gold stud earrings; she is barefoot indoors.',
    setting='Setting: a tidy luxury hotel suite at sunset in winter, a deep green velvet chaise longue beside a floor-to-ceiling window, the city skyline far below in warm evening haze, straight window frames, no text.',
    moment='Moment: she reclines on her side along the chaise, propped on her lower forearm on the cushion, her other hand resting naturally at her waist, her legs softly bent and crossed, looking out of the window at the last sunset light with a calm, languid half-smile.',
    shot='Shot: her whole reclining figure from head to feet across the frame, with space beyond her head and her feet.',
    camera='Camera: horizontal 16:9, from slightly above her head height as she reclines, tilted slightly down, a 50mm lens from about 3.4 metres, natural perspective.',
    comp='Composition: she lies across the middle of the frame along the chaise, her head on the left and her feet on the right, with clear space at both ends, the window and the skyline behind her.',
    light='Light: the low sunset through the window on camera-right lays a warm band of light across her; a gentle fill keeps her face clear; wine red, warm gold and deep green velvet.',
    B=dict(change='姿態：改為側坐在貴妃椅一端',
           moment='Moment: she sits upright at one end of the chaise with her legs folded to one side on the velvet, one hand resting on the armrest, turning her face to the window and the sunset with a calm half-smile.',
           shot='Shot: her whole seated figure from a little above her head to just below her feet, the chaise and the window beside her.',
           camera='Camera: horizontal 16:9, from slightly above her seated head height, tilted slightly down, a 50mm lens from about 3.4 metres, natural perspective.',
           comp='Composition: she sits right of centre on the chaise, the window and the skyline on the right where she looks, clear space above her head.'))

S['H-rainie-hsu'] = dict(
    wear='She wears a blood-red satin corset mini dress with a thigh-high slit, black strappy high-heeled sandals, large silver statement drop earrings and a slim silver cuff.',
    setting='Setting: a high-rise penthouse terrace on a December night, a low clean glass balustrade, a smooth dark stone floor, a warm wall lamp on the terrace wall, the city lights spread far below into warm-gold and cool bokeh, nothing else on the terrace.',
    moment='Moment: she leans back against the glass balustrade with both hands resting on the rail behind her and one leg forward through the slit, looking straight into the camera with a confident, slightly mischievous smirk.',
    shot='Shot: knee-up, from a little above her head to just below her knees, the city lights behind her.',
    camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 4.9 metres, natural perspective.',
    comp='Composition: she stands on the right third, the glowing city bokeh filling the left side, the wall lamp glowing on the terrace wall just to camera-right of her.',
    light='Light: the warm wall lamp beside her at head height is the key, lighting her face and catching red highlights on the satin; a soft fill keeps her face clear; the city lights stay soft behind her; blood red, night blue and warm gold.',
    B=dict(change='取景：改為全身，帶到高跟鞋與石材地面',
           shot='Shot: full-length, from a little above her head to just below her heels, the stone floor and the city lights around her.',
           camera='Camera: horizontal 16:9, at her waist height, level, a 50mm lens from about 5.5 metres, natural perspective.',
           comp='Composition: she stands on the right third against the balustrade, the city bokeh across the left and behind her, the wall lamp just to camera-right of her, clear space above her head and below her heels.'))

S['H-miu-shiraishi'] = dict(
    wear='She wears an ivory satin camisole with thin straps and fine lace trim, matching ivory satin shorts, small gold stud earrings and a thin gold bracelet; she is barefoot indoors.',
    setting='Setting: a small sunlit apartment bedroom on a March morning, a neatly made bed with cream linen, sheer white curtains at the window, a wooden bedside shelf with a small potted plant, no text or brands, the room tidy.',
    moment='Moment: she sits on the bed hugging one raised knee with both arms, her chin resting near her knee, giving the camera a relaxed, just-woken smile, her head level.',
    shot='Shot: a close seated shot, from a little above her head down to the bed surface, the curtains and the window light beside her.',
    camera='Camera: horizontal 16:9, at her seated chest height, level, a 50mm lens from about 2 metres, natural perspective.',
    comp='Composition: she sits just right of centre, the window with its glowing sheer curtains on the left, the soft white bedding around her, the small plant on the shelf at the right edge.',
    light='Light: morning light filtered through the sheer white curtains on the left is the key, soft and bright; the white sheets and walls on the right bounce light back into her face; cream white, ivory, light wood and a touch of green.',
    B=dict(change='姿態：改為坐在床緣、雙腳踩地',
           moment='Moment: she sits on the edge of the bed with both feet resting on the wooden floor and her hands resting on the bed beside her hips, smiling at the camera with a relaxed, just-woken look.',
           shot='Shot: her whole seated figure from a little above her head to just below her feet, the bed and the window beside her.',
           camera='Camera: horizontal 16:9, at her seated chest height, level, a 50mm lens from about 3 metres, natural perspective.',
           comp='Composition: she sits just right of centre on the edge of the bed, the curtained window glowing on the left, the small plant on the shelf at the right edge.'))

S['V-luna-tanaka'] = dict(
    wear='She wears a pale sage-green cotton sundress with a sweetheart neckline, a fitted bodice and a softly flared mini skirt, cream low block-heel strappy sandals and a thin gold bracelet.',
    setting='Setting: a quiet garden behind an old wooden Kyoto-style townhouse just after the June rain, moss ground still glistening, a low wooden fence, waist-high white hydrangeas in bloom, maple branches overhead, nobody else around.',
    moment='Moment: she stands among the white hydrangeas with both hands clasped lightly behind her back, smiling gently at the camera.',
    shot='Shot: knee-up, from a little above her head to just below her knees, hydrangeas at her waist and in the foreground.',
    camera='Camera: vertical 3:4, at her chest height, level, an 85mm lens from about 3.1 metres, natural perspective with straight vertical lines.',
    comp='Composition: she stands slightly left of centre, the white hydrangeas around her waist and soft in the foreground, the wooden fence behind her and maple branches across the top edge.',
    light='Light: the bright, even overcast light after rain as one large soft source, the moss and petals slightly wet and glistening; a gentle fill keeps her face clear; sage green, white and moss green.',
    B=dict(change='取景：改為全身站在石板小徑上',
           shot='Shot: full-length, from a little above her head to just below her sandals, standing on the stone path beside the hydrangeas.',
           camera='Camera: vertical 3:4, at her waist height, level, a 50mm lens from about 4.2 metres, natural perspective with straight vertical lines.',
           comp='Composition: she stands slightly left of centre on the stone path, the hydrangeas along the fence beside her, maple branches across the top, clear space above her head and below her feet.'))

S['V-coco-wu'] = dict(
    wear='She wears a mint-green ribbed triangle bikini top with matching side-tie bottoms that fully cover, an open sheer lilac short-sleeve cover-up shirt resting off her shoulders and a white daisy hair clip; she is barefoot with her lower legs in the water.',
    setting='Setting: a resort hotel pool on a weekend late morning, pale cream stone tiles, clear turquoise water, white umbrellas folded in the distance, the pool deck empty.',
    moment='Moment: she sits on the pool edge with both lower legs in the water, leaning back on her hands, her head tilted back, laughing with her eyes squeezed into crescents and dimples showing.',
    shot='Shot: seated, from a little above her head down to just below the waterline, her knees and the top of her lower legs in the water.',
    camera='Camera: vertical 3:4, at her seated chest height, level, a 70mm lens from about 2.4 metres, natural perspective.',
    comp='Composition: she is centred, the turquoise water across the bottom of the frame, the stone deck and the folded white umbrellas behind her.',
    light='Light: bright late-morning sun from high front-left, with a gentle fill softening the shadows on her face; the water throws moving aqua light patterns onto her legs; turquoise, mint, lilac and pale stone.',
    B=dict(change='姿態：改為身體微微前傾、雙手放在膝上',
           moment='Moment: she sits on the pool edge with both lower legs in the water, leaning slightly forward with her hands resting on her knees, laughing at the camera with her eyes squeezed into crescents and dimples showing.'))

S['V-mia-huang'] = dict(
    wear='She wears a lilac fitted fine-knit off-shoulder mini dress, white knee-high boots, small pearl hair clips on one side and thin silver earrings.',
    setting='Setting: a riverside promenade on a spring night, cherry trees in full bloom arching overhead, plain paper lanterns without any writing hanging along the path, a deep blue night sky, nobody else around.',
    moment='Moment: one hand lightly touches a blossom branch beside her shoulder; she smiles sweetly at the camera.',
    shot='Shot: chest-up, from a little above her head to just below her bust.',
    camera='Camera: vertical 3:4, at her eye level, tilted slightly down, an 85mm lens from about 1.5 metres, natural perspective.',
    comp='Composition: she is slightly left of centre, blossom branches framing the top and the upper right, the lanterns behind her softened into warm points of light, her face in the upper third.',
    light='Light: a plain paper lantern hanging about an arm\'s length in front of her on the left is the key, warming her face and the blossoms near her; the deep blue night sky behind; cherry pink, warm orange and night blue.',
    B=dict(change='取景：改為膝上，帶到花枝與燈籠步道',
           shot='Shot: knee-up, from a little above her head to just below her knees, standing under the arching branches.',
           camera='Camera: vertical 3:4, at her chest height, level, an 85mm lens from about 3 metres, natural perspective.',
           comp='Composition: she stands slightly left of centre under the arching blossoms, the line of lanterns receding behind her on the right as warm points of light.'))

S['V-yuna-kim'] = dict(
    wear='She wears a cream tweed cropped jacket, collarless and buttoned, a matching high-waisted tweed mini skirt, black knee-high leather boots, small pearl earrings and a small plain black shoulder bag without any logos.',
    setting='Setting: a quiet avenue in late autumn lined on both sides with golden ginkgo trees, fallen yellow leaves covering the sidewalk, low modern buildings softly out of focus, no signs or text, the street empty.',
    moment='Moment: she has stopped on the sidewalk with one hand holding the strap of the bag at her shoulder, looking down the avenue into the distance with a thoughtful smile.',
    shot='Shot: full-length, from a little above her head to just below her boots, with the avenue around her.',
    camera='Camera: vertical 3:4, at her waist height, level, an 85mm lens from about 7 metres, natural perspective with straight vertical lines.',
    comp='Composition: she stands on the left third with her body and gaze toward the right, the ginkgo avenue forming a golden tunnel that recedes behind her to a vanishing point at about the height of her hips, clear space above her head and below her boots.',
    light='Light: low afternoon sun behind the ginkgo trees lights the leaves and draws a warm rim on her hair; a gentle fill keeps her face clear; golden yellow, cream and black.',
    B=dict(change='取景：改為膝上',
           shot='Shot: knee-up, from a little above her head to just below her knees, the golden avenue behind her.',
           camera='Camera: vertical 3:4, at her chest height, level, an 85mm lens from about 3.3 metres, natural perspective with straight vertical lines.',
           comp='Composition: she stands left of centre, her gaze toward the right where the avenue recedes, golden ginkgo leaves filling the background.'))

S['V-rainie-hsu'] = dict(
    wear='She wears a black satin halter mini dress, a long black leather trench coat worn open, black pointed stiletto ankle boots and large silver statement drop earrings.',
    setting='Setting: a city street at night just after rain, closed shopfronts with plain frosted glass and no signs or text, one shop window glowing warm amber beside her, the wet pavement reflecting warm and cool light, cool street lights far down the street, nobody else around.',
    moment='Moment: she has stopped beside the glowing shop window, one hand holding the edge of the open coat at her waist, looking toward the distant street lights on camera-left with a relaxed expression, her lips slightly parted.',
    shot='Shot: full-length, from a little above her head to just below her boots, her reflection on the wet pavement at her feet.',
    camera='Camera: vertical 3:4, at her waist height, level, a 50mm lens from about 4.3 metres, natural perspective with straight vertical lines.',
    comp='Composition: she stands on the right third, the wet street and its reflections receding to the left, the warm shop window beside her on the right.',
    light='Light: the warm amber light from the shop window on her right is the key, lighting half of her face; a soft fill keeps the shadow side readable; cool blue street lights and their reflections behind; black, warm amber and cool blue.',
    B=dict(change='取景：改為膝上',
           shot='Shot: knee-up, from a little above her head to just below her knees.',
           camera='Camera: vertical 3:4, at her waist height, level, an 85mm lens from about 3.6 metres, natural perspective with straight vertical lines.',
           comp='Composition: she stands right of centre beside the glowing window, the wet street and the street lights receding softly on the left.'))

S['V-miu-shiraishi'] = dict(
    wear='She wears an apricot cotton-sateen mini dress with thin straps, a fitted bodice with a sweetheart neckline and a softly flared skirt to mid-thigh, white strappy flat sandals and small pearl earrings.',
    setting='Setting: a holiday villa on an April morning, a wooden deck with three wide wooden steps, a whole fruit tree in full white blossom behind like a cloud, fresh green hedges, no hammock, no text, nobody else around.',
    moment='Moment: she sits on the second step with her knees together and angled to one side, her feet resting on the first step and her forearms resting lightly on her knees, leaning slightly forward and smiling brightly at the camera.',
    shot='Shot: her whole seated figure from a little above her head to just below her feet, with the steps and the blossoming tree around her.',
    camera='Camera: vertical 3:4, at her seated chest height, level, a 50mm lens from about 3.2 metres, natural perspective.',
    comp='Composition: the white blossoming tree fills the upper part of the frame, the wide steps cross the lower part, and she sits in the lower third slightly left of centre.',
    light='Light: soft, bright spring morning daylight under thin cloud, the blossoms glowing with light passing through them; a gentle fill keeps her face clear; apricot, blossom white, fresh green and pale wood.',
    B=dict(change='取景：改為坐姿近一點（到膝下）',
           shot='Shot: seated, from a little above her head to just below her knees, the blossoming tree behind her.',
           camera='Camera: vertical 3:4, at her seated chest height, level, an 85mm lens from about 2.8 metres, natural perspective.',
           comp='Composition: she sits slightly left of centre on the step, the white blossoms filling the background behind her.'))

S['V-jia-seo'] = dict(
    wear='She wears a white sleeveless mock-neck fitted crop top, a high-waisted mint-sage satin pencil skirt that narrows to just below the knee with a front slit, white strappy sandals and small silver stud earrings.',
    setting='Setting: a glass greenhouse conservatory in February, warm and humid inside while winter shows faintly through the glass, white steel frames overhead, lush tropical plants with large monstera leaves about an arm\'s length across, a stone path, nobody else around.',
    moment='Moment: she stands on the stone path with her weight settled on one leg, one hand resting on her hip at the high waistband and the other arm relaxed at her side, looking at the camera with a calm, soft expression.',
    shot='Shot: full-length, from a little above her head to just below her sandals, with the steel frames and the plants around her.',
    camera='Camera: vertical 3:4, at her waist height, level, a 50mm lens from about 4.1 metres, natural perspective with straight vertical lines.',
    comp='Composition: she stands slightly left of centre on the path, the white steel frames across the top and large green leaves framing both sides without covering her, clear space above her head and below her feet.',
    light='Light: bright diffused daylight through the glass roof as one large soft source; a gentle fill keeps her face clear; deep and pale greens, white and mint.',
    B=dict(change='取景：改為膝上',
           shot='Shot: knee-up, from a little above her head to just below her knees, the leaves around her.',
           camera='Camera: vertical 3:4, at her chest height, level, an 85mm lens from about 3 metres, natural perspective with straight vertical lines.',
           comp='Composition: she stands slightly left of centre, the white steel frames above her and large green leaves soft on both sides.'))

S['V-yerin-han'] = dict(
    wear='She wears a white fitted ribbed scoop-neck tank mini dress and small gold hoop earrings; she is barefoot on the beach, carrying a pair of white sandals in one hand.',
    setting='Setting: a wide white-sand beach just after sunset, calm shallow water, the sky and the sea both turned soft pink and lavender like a mirror, no hard backlight, nobody else around.',
    moment='Moment: she walks through the shallow water with small waves washing around her ankles, the pair of white sandals dangling from one hand, looking down at the water by her feet with a happy smile.',
    shot='Shot: full-length, from a little above her head to just below her feet in the water, with plenty of sky and sea around her.',
    camera='Camera: vertical 3:4, at her hip height, level, a 50mm lens from about 5 metres, natural perspective.',
    comp='Composition: she is on the right third, the pink and lavender sky and sea filling most of the frame above and to the left, the sea horizon at the height of her hips.',
    light='Light: the bright, soft afterglow from the sky after sunset lights her evenly from the sea side; the water and her dress reflect the pink and lavender sky; soft pink, lavender, pale blue and white.',
    B=dict(change='姿態：改為在淺水中停步、仰望天空',
           moment='Moment: she stands still in the shallow water with the white sandals in one hand, turning her face up toward the glowing sky with a calm, happy smile.'))

S['H-yerin-han'] = dict(
    wear='She wears a white sleeveless fitted knit golf polo, a pale sky-blue pleated golf skirt, white golf shoes and small gold studs.',
    setting='Setting: the edge of a fairway on a clear late-spring morning, bright green grass with dew still on it, tall, fully leafed mature trees along the far side, clearly much taller than her, open sky, no flags or signs with text, nobody else around.',
    moment='Moment: she stands upright with both feet flat on the grass about hip-width apart and her weight settled evenly, holding a single golf club loosely in one hand with its head resting lightly on the grass beside her foot, her other arm relaxed at her side with the fingers loose, looking down the fairway toward the next hole with an easy, confident smile.',
    shot='Shot: a wide full-length shot, from well above her cap to well below her shoes; she is a modest figure in the scene, with wide open fairway around her and plenty of sky above her cap.',
    camera='Camera: horizontal 16:9, at her waist height, level, a 50mm lens from about 12 metres, natural perspective.',
    comp='Composition: she stands on the left third of the frame with her body angled to the right, the fairway opening out ahead of her on the right, the line of tall trees across the upper middle; the fairway and the trees share the picture with her.',
    light='Light: the low morning sun from the right of the frame, ahead of her, lights her face and the front of her body from the side, crisp and directional, with long soft shadows stretching behind her across the grass and sparkles of dew; a soft fill keeps her eyes clear under the cap brim; fresh green, white and pale sky blue.',
    B=dict(change='站位：改站右三分之一、望向左側球道（光向隨之改為畫面左側）',
           comp='Composition: she stands on the right third of the frame with her body angled to the left, the fairway opening out ahead of her on the left, the line of tall trees across the upper middle; the fairway and the trees share the picture with her.',
           light='Light: the low morning sun from the left of the frame, ahead of her, lights her face and the front of her body from the side, crisp and directional, with long soft shadows stretching behind her across the grass and sparkles of dew; a soft fill keeps her eyes clear under the cap brim; fresh green, white and pale sky blue.'))

S['H-jia-seo'] = dict(
    wear='She wears a deep wine-red fine-knit long dress that falls to her ankles, a soft cream cardigan slipping off one shoulder, flat brown leather sandals and small silver hoop earrings.',
    setting='Setting: a quiet lake in early autumn just after sunset, the sun already gone below the far shore, a wide pale wooden deck running out over the still water, the far shore lined with trees just turning yellow, the sky and the lake glowing soft pink and lavender with the afterglow, no bench, nobody else around.',
    moment='Moment: she sits on the deck boards well back from the water\'s edge, her hips, legs, feet and sandals all resting on the boards, her legs folded to one side with her long skirt spreading over the wood, one hand resting on the boards beside her, gazing out across the lake with a calm, thoughtful half-smile, her face in three-quarter profile toward the camera.',
    shot='Shot: a wide seated full-length shot showing the whole deck around her; her seated figure is small in the frame, with the open lake, the far shore and the sky around her.',
    camera='Camera: horizontal 16:9, from a little above her seated head height, angled slightly down, a 35mm lens from about 7 metres, natural perspective.',
    comp='Composition: the deck runs in diagonally from the lower right corner toward the middle of the frame; she sits on the deck on the right third, about a body length back from its end, with clear boards between her and the water; the far shore lies across the upper third, above her head; the wide glowing lake fills the left half.',
    light='Light: the brightest part of the afterglow sky is low on the left of the frame beyond the far shore, and it lights her face softly as she looks toward it, with a faint pink sheen on the water and on her hair; any fill stays gentle so her face is no brighter than the sky; soft pink, lavender, lake blue-grey, cream and deep wine.',
    B=dict(change='姿態：改為雙膝立起、手臂輕環膝上',
           moment='Moment: she sits on the deck boards well back from the water\'s edge with her knees drawn up and her arms resting loosely around them, her sandals flat on the boards and her long skirt draped over her legs, gazing out across the lake with a calm, thoughtful half-smile, her face in three-quarter profile toward the camera.'))

ORDER = ['moment', 'wear', 'setting', 'shot', 'camera', 'comp', 'light']
