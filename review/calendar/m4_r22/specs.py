# M-4 R22：剩餘 4 套的 prompt 規格（各 2 張）。身分段落沿用既有 canon（H-Mia／H-Somi／V-Rainie 取 R20/R21 同一段；V-Somi 取企劃 v12）。
# 每套 A、B 是同一設計、變化一項主要安排；動作只寫一個，不堆疊。
END = 'Natural skin texture with visible pores, believable light that belongs to the scene, refined colour grading.'
ORDER = ['wear', 'setting', 'moment', 'shot', 'camera', 'comp', 'light']
S = {}

S['H-mia-huang'] = dict(
    note='Penny 兩輪都說背景太假：捨棄遊樂碼頭、摩天輪、燈串與棉花糖，改成真實的夏日海灘黃金時刻；單一自然光源（低角度夕陽在畫外左後方）、人物坐或站在沙灘上有清楚接觸、85mm 淺景深。服裝保留（粉色緞面馬甲上衣＋白色迷你裙），拿掉棉花糖道具（理由：道具讓畫面像擺設，Penny 要自然可信）；赤腳在沙灘（涼鞋在沙灘上不合理）。',
    wear='She wears a pastel-pink satin corset top with a sweetheart neckline, a white high-waisted A-line mini skirt, small pearl earrings and a thin silver bracelet; she is barefoot on the sand.',
    setting='Setting: a wide, quiet sandy beach on a clear July evening at golden hour, soft pale sand with footprints, low dunes with tufts of beach grass behind her, calm sea and gentle small waves, an open sky fading from warm gold to soft pink, nobody else on the beach, no buildings, signs or props.',
    light='Light: the low evening sun is just out of frame behind her on the left, giving her hair and shoulders a warm golden rim, while the bright glow of the open sky in front of her lights her face softly and evenly; the sand bounces a little warm light back up; warm gold, candy pink, white and soft sea blue.',
    A=dict(change='安排：坐在沙灘上，雙腿往一側收、一手撐沙（膝上）',
           moment='Moment: she sits on the sand with her knees bent and her legs tucked to one side, leaning lightly on one hand planted in the sand, and smiles at the camera with a playful, relaxed look as the sea breeze moves her hair.',
           shot='Shot: her whole seated figure from a little above her head to just past her bare feet, the sand and the sea around her.',
           camera='Camera: horizontal 16:9, at her seated chest height, level, an 85mm lens from about 4.5 metres, shallow depth of field so the sea and dunes fall softly out of focus, natural perspective.',
           comp='Composition: she sits on the left third, the soft sand in the foreground, the calm sea and the glowing sky across the background on the right.'),
    B=dict(change='安排：站在潮線附近，雙手自然垂下、迎風撥髮（全身）',
           moment='Moment: she stands barefoot on the wet sand near the waterline with her weight on one leg, and brushes the wind-blown hair from her face with one hand, smiling at the camera.',
           shot='Shot: full-length, from a little above her head to just below her bare feet, the wet sand and the sea around her.',
           camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 7 metres, shallow depth of field, natural perspective.',
           comp='Composition: she stands on the left third, the shining wet sand at her feet, the gentle waves and the glowing sky filling the right side.'),
)

S['H-somi-oh'] = dict(
    note='保留 Owner 選定的 R21 B（芒草原、服裝、色調）；改成身體放鬆、動作連貫的自然抓拍瞬間；不扭腰、不插腰、不抬腳；每張只寫一個動作。兩張是改善候選，不自動替換 R21 B。',
    wear='She wears a cream cable-knit cropped cardigan buttoned over a fitted rust-orange ribbed knit mini dress, brown suede ankle boots and small red enamel heart earrings.',
    setting='Setting: a wide hillside field of tall silver grass in late November at golden hour, the feathery grass heads glowing silver-gold, a narrow dirt path winding through the field, low hills and a soft hazy sky in the distance, no signs, nobody else around.',
    light='Light: the low golden-hour sun behind her and to the left backlights the silver grass and draws a warm rim around her hair and shoulders; a soft, warm fill from the front keeps her face clear and glowing; silver gold, rust orange, cream and soft sky blue.',
    A=dict(change='抓拍：站在芒草中，風把頭髮吹到臉上，她自然笑出來（膝上，沿用 R21 B 的取景）',
           moment='Moment: she stands relaxed among the tall silver grass with her arms hanging loosely at her sides, and a gust of wind blows her hair across her face, making her laugh naturally with her eyes curved into crescents and dimples showing, caught in the moment.',
           shot='Shot: knee-up, from a little above her head to just below her knees, the silver grass around her waist and in the foreground.',
           camera='Camera: horizontal 16:9, at her chest height, level, an 85mm lens from about 4 metres, natural perspective.',
           comp='Composition: she stands slightly right of centre, the glowing grass around her waist and soft in the foreground, the field and the hazy hills behind her.'),
    B=dict(change='抓拍：沿小徑慢慢走來、低頭看著草穗微笑（全身）',
           moment='Moment: she walks slowly along the narrow path toward the camera with her arms relaxed, looking down at the glowing grass beside the path with a soft, happy smile, as if she has not noticed the camera.',
           shot='Shot: full-length, from a little above her head to just below her boots, the silver grass around her.',
           camera='Camera: horizontal 16:9, at her waist height, level, an 85mm lens from about 7 metres, natural perspective.',
           comp='Composition: she walks slightly left of centre on the path, the glowing silver grass filling the field around her and stretching to the hills, the sun low behind her on the left.'),
)

S['V-rainie-hsu'] = dict(
    note='身分來源檢查：沒有 identity_master；Soul 訓練圖（training_v2 13 張）與錨點多為 3/4 側臉、視線看手機或往下，正面直視鏡頭的樣本很少；基準中沒有鬥雞眼。R20/R21 四張中，頭轉向一側、眼睛被要求看鏡頭時，遠側眼球偏向鼻側，看起來內聚。修正：讓視線順著臉的方向（看向畫外遠處或往下），不要求直視鏡頭；相機在腰高、85mm 遠距離，全身、腳在畫面下緣、前腳腳尖延伸，不極端仰拍、不廣角拉伸。服裝：長風衣遮住腿線，改為短版黑色皮夾克（理由：Penny 要看出長腿）；其餘保留。',
    wear='She wears a black satin halter mini dress, a cropped black leather jacket worn open, black pointed stiletto ankle boots and large silver statement drop earrings.',
    setting='Setting: a city street at night just after rain, closed shopfronts with plain frosted glass and no signs or text, one shop window glowing warm amber beside her, the wet pavement reflecting warm and cool light, cool street lights far down the street, nobody else around.',
    light='Light: the warm amber light from the shop window on her right is the key, lighting her face softly from the side; a soft fill keeps the shadow side readable; cool blue street lights and their reflections behind; black, warm amber and cool blue.',
    A=dict(change='視線：頭和眼睛一起轉向畫面左側遠處的街燈（3/4 臉）；全身、前腳延伸',
           moment='Moment: she stands beside the glowing window with her weight on her back leg and her front leg extended forward with the toe pointed, and turns her head toward the distant street lights on the left of the frame, her eyes following the same direction as her face, calm and composed.',
           shot='Shot: full-length, from a little above her head to just below her boots, her feet close to the bottom of the frame, her reflection on the wet pavement.',
           camera='Camera: vertical 3:4, at her waist height, level, an 85mm lens from about 8 metres, natural perspective with natural body proportions.',
           comp='Composition: she stands slightly right of centre, the wet street and its reflections receding to the left where she looks, the warm shop window beside her on the right.'),
    B=dict(change='視線：靠著發光櫥窗、低頭微笑（眼睛往下），雙腿交叉站立；全身',
           moment='Moment: she leans one shoulder lightly against the frame of the glowing shop window with her legs crossed at the ankles, and lowers her gaze toward the wet pavement with a soft, private smile, her face turned slightly down in the same direction as her eyes.',
           shot='Shot: full-length, from a little above her head to just below her boots, her feet close to the bottom of the frame.',
           camera='Camera: vertical 3:4, at her waist height, level, an 85mm lens from about 8 metres, natural perspective with natural body proportions.',
           comp='Composition: she stands on the right third against the window frame, the warm window light along the right edge, the wet street receding softly on the left.'),
)

S['V-somi-oh'] = dict(
    note='回看 R5／R7／R8／R11：句子長、同時要求多個動作與構圖控制（手放口袋撐開外套、另一手接雪、抬頭、身材展示），結果不自然或失敗；這輪不原樣重送、不用遮罩或底稿流程。沿用冬季雪景與酒紅／象牙白服裝，兩種簡單景別、各一個動作：A 以神情與雪景氛圍為主（胸上），B 以完整人物與雪街共同構圖為主（全身）。',
    identity='A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. Light makeup with a glossy lip, her cheeks flushed pink from the cold.',
    wear='She wears a fitted ivory ribbed knit mini dress with a high round neck, a long wine-red wool coat worn open, white knee-high boots and small pearl earrings.',
    setting='Setting: a quiet street in a small hot-spring town on a snowy winter evening, low wooden inns with warm paper lanterns, thin steam rising from a stone channel at the roadside, a light layer of snow on the ground, the street empty.',
    light='Light: the warm glow of the paper lanterns lights her face softly from the front and side, with the cool blue of the snowy evening around her; snowflakes catch the lantern light; wine red, ivory, lantern amber and snowy blue.',
    A=dict(change='景別：胸上；神情為主——抬眼看飄雪、自然笑開',
           moment='Moment: she looks up at the falling snow with a bright, delighted smile, a few snowflakes caught in her hair.',
           shot='Shot: chest-up, from a little above her head to just below her chest, the lanterns glowing softly behind her.',
           camera='Camera: vertical 3:4, at her eye level, level, an 85mm lens from about 2 metres, shallow depth of field, natural perspective.',
           comp='Composition: her face in the upper third slightly left of centre, the warm lantern bokeh and falling snow behind her on the right.'),
    B=dict(change='景別：全身；人物與雪街共同構圖——雙手插口袋慢慢走來',
           moment='Moment: she walks slowly toward the camera along the snowy street with both hands in her coat pockets, smiling softly.',
           shot='Shot: full-length, from a little above her head to just below her boots, the lantern-lit inns and the snowy street around her.',
           camera='Camera: vertical 3:4, at her waist height, level, a 50mm lens from about 6 metres, natural perspective with straight vertical lines.',
           comp='Composition: she walks slightly left of centre, the row of lantern-lit wooden inns receding behind her on the right, the snowy street at her feet, clear space above her head and below her boots.'),
)
