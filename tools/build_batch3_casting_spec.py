#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""從 profile.json 的 appearance ＋ batch3_faces_v2.json 的 fixed 數據，
組出 13 位的選角規格 → pilot/batch3_casting_v2.json。

跟第一版（pilot/batch3_casting.json）的三個差別，每一個都對應一次實測失敗：

1. **臉不再用文字描述。** face_base／face_negative 整組拿掉，改成四張裁切
   ＋ face_en 的位置式指派。文字描述臉是上一批「五官全都太像」的直接原因。
2. **不寫任何否定句。** 已證實模型不執行否定；第一版的 face_negative 整段是空轉。
3. **選角服裝一律合身。** 第一版 16/16 把 E 罩杯畫成平胸，最大嫌疑是寬鬆家居服
   把胸線蓋掉了。選角是身材的驗收關，衣服不能擋。
"""
import json

M = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))['personas']

# 每位只需要指定「服裝／場景／光線／髮」與一句身材性格；身材數字從 fixed 讀。
P = {
 'angel-chiu': dict(
   figure='她的身材是標準的豐滿勻稱，肩線平順',
   hair_color_en='Her hair is a dark brown-black, with the last hand-span of the ends lightened to a honey-tea gold.',
   hair_en='It is long and straight, worn down and loose over her shoulders.',
   hair_length='Its length reaches the middle of her back.',
   outfit=dict(top='a fitted charcoal ribbed cotton tank top that follows the line of her torso',
               top_hem='the hem is tucked into her waistband',
               bottom='straight-leg light denim jeans sitting at her natural waist',
               shoes='white canvas sneakers',
               jewelry='a thin gold chain at her throat'),
   location='her rented flat near the hospital — a drying rack of scrubs by the balcony door, a stack of nursing textbooks on the low table, and a half-finished mug of tea',
   light=dict(key='late afternoon daylight comes through the balcony door on her left and is the main light on her face',
              bounce='the white wall on her right throws that light back into the shadow side of her face',
              secondary_source='', exposure_choice='the camera meters for her face, so the balcony door blows out to flat white',
              occlusion='the corridor behind her falls away into shadow')),
 'cheryl-soh': dict(
   figure='她的身材是空服員式的修長勻稱，肩線平、背挺',
   hair_color_en='Her hair is a deep natural black with a soft sheen.',
   hair_en='It is long and worn down, falling in a loose wave through the lower half.',
   hair_length='Its length reaches past her shoulder blades.',
   outfit=dict(top='a fitted white ribbed knit long-sleeve top that follows the line of her torso',
               top_hem='the hem sits at her hip bone',
               bottom='tailored navy wide-leg trousers sitting high at her waist',
               shoes='flat black loafers', jewelry='small gold stud earrings'),
   location='her own apartment in Singapore — a cabin bag standing open against the wall, a row of hotel keycards on the shelf, and blackout curtains pushed to one side',
   light=dict(key='morning daylight comes through the tall window behind her right shoulder and wraps onto her face',
              bounce='the pale grey wall opposite fills the shadow side',
              secondary_source='a warm floor lamp is still switched on in the corner behind her',
              exposure_choice='the camera meters for her face, so the window blows out to flat white',
              occlusion='the hallway behind her falls away into shadow')),
 'emma-kao': dict(
   figure='她的身材是高挑端莊型，肩背挺直',
   hair_color_en='Her hair is a deep brown, natural and even from root to tip.',
   hair_en='It is shoulder-length and straight, blown under at the ends so it curves in toward her jaw.',
   hair_length='Its length reaches her shoulders.',
   outfit=dict(top='a fitted cream silk-knit shell top that follows the line of her torso',
               top_hem='the hem is tucked into her skirt',
               bottom='a tailored black pencil skirt sitting at her natural waist',
               shoes='nude low heels', jewelry='a single strand of small pearls'),
   location='her flat after the evening broadcast — a garment bag hanging on the wardrobe door, a script marked in red on the table, and the television still on with the sound off',
   light=dict(key='a warm floor lamp beside her is the main light on her face',
              bounce='the cream wall behind her throws that light back into the shadow side',
              secondary_source='the muted television puts a cool flickering blue into the room behind her',
              exposure_choice='the camera meters for her face, so the lamp shade blows out to flat white',
              occlusion='the far side of the room falls away into shadow')),
 'jia-seo': dict(
   figure='她的身材是舞者型，肩背有薄薄的肌肉線條，腿長',
   hair_color_en='Her hair is a cool ash blue-black, with an under-layer dyed a clear mint green that shows when it moves.',
   hair_en='It is long and straight, worn down.',
   hair_length='Its length reaches the middle of her back.',
   outfit=dict(top='a fitted black cropped long-sleeve dance top that follows the line of her torso',
               top_hem='the hem ends just above her waistband, leaving a hand-width of her midriff visible',
               bottom='high-waisted black nylon track pants',
               shoes='white high-top sneakers', jewelry='a black elastic hair tie around her wrist'),
   location='the practice room after hours — one wall entirely mirrored, a speaker on the floor in the corner, and water bottles lined up along the skirting board',
   light=dict(key='the ceiling fluorescents overhead are the main light on her face',
              bounce='the mirrored wall throws that light back into the shadow side of her face',
              secondary_source='', exposure_choice='the camera meters for her face, so the ceiling panels blow out to flat white',
              occlusion='the far end of the room falls away into shadow')),
 'kanon-komori': dict(
   figure='她的身材在很小的骨架上顯得胸線特別重',
   hair_color_en='Her hair is a pink-lilac gradient: dark at the roots for the first hand’s width, then blending down through a dusty lilac into a clear cotton-candy pink at the ends.',
   hair_en='It is very long, worn down with a loose wave through the lower half.',
   hair_length='Its length reaches her waist.',
   outfit=dict(top='a fitted pale pink ribbed cotton T-shirt that follows the line of her torso',
               top_hem='the hem sits at her hip bone',
               bottom='short grey cotton shorts with a soft elastic waistband',
               shoes='flat pink house slippers',
               jewelry='a small tortoiseshell claw clip holding a section of hair at the back of her head'),
   location='her small studio flat in Akihabara — a sewing machine on a desk against the wall, folded fabric stacked on the floor, and a whole wall of soft toys on shelves behind her',
   light=dict(key='afternoon daylight comes through the window on her right and is the main light on her face',
              bounce='the white wall and the pale fabric stacked on the floor throw that light back into the shadow side of her face',
              secondary_source='a small pink night light still switched on behind her left shoulder puts a second, cooler pink colour into that side of the room',
              exposure_choice='the camera meters for her face, so the window blows out to flat white',
              occlusion='the depth of the shelves behind her falls away into shadow')),
 'nanami-fujiwara': dict(
   figure='她的身材柔和圓潤，肩線是斜的',
   hair_color_en='Her hair is a deep natural black, straight and glossy.',
   hair_en='It is long and worn down, falling straight without a wave.',
   hair_length='Its length reaches past her shoulder blades.',
   outfit=dict(top='a fitted oatmeal ribbed cotton long-sleeve top that follows the line of her torso',
               top_hem='the hem is tucked into her waistband',
               bottom='a long dark green cotton wrap skirt',
               shoes='flat woven house sandals', jewelry='a plain wooden hair pin held in one hand'),
   location='the private wing of the family ryokan — a paper shoji screen behind her, tatami underfoot, and a folded yukata stacked on the low chest',
   light=dict(key='overcast daylight comes through the shoji screen behind her left shoulder and is the main light on her face',
              bounce='the tatami and the pale paper screen throw that light back into the shadow side of her face',
              secondary_source='', exposure_choice='the camera meters for her face, so the shoji screen blows out to flat white',
              occlusion='the corridor beyond the doorway falls away into shadow')),
 'rin-ayase': dict(
   figure='她的身材是明顯的沙漏型，胸與臀都滿，腰窄',
   hair_color_en='Her hair is a dark wine-red brown that only shows its red under direct light.',
   hair_en='It is long and blown into a soft large wave, worn down.',
   hair_length='Its length reaches past her shoulder blades.',
   outfit=dict(top='a fitted black fine-knit long-sleeve top that follows the line of her torso',
               top_hem='the hem is tucked into her skirt',
               bottom='a tailored camel midi skirt sitting at her natural waist',
               shoes='black heeled ankle boots', jewelry='a thin gold bracelet'),
   location='her apartment before a shift — a dress bag hanging on the wardrobe door, a lacquer tray of hair pins on the table, and the city lights behind the window',
   light=dict(key='a warm table lamp beside her is the main light on her face',
              bounce='the pale wall behind her throws that light back into the shadow side',
              secondary_source='the city outside the window puts a cool blue into the room behind her',
              exposure_choice='the camera meters for her face, so the lamp shade blows out to flat white',
              occlusion='the far corner of the room falls away into shadow')),
 'sydney-leong': dict(
   figure='她的身材在嬌小的骨架上胸線特別重',
   hair_color_en='Her hair is a light honey-gold brown, evenly lightened from root to tip.',
   hair_en='It is mid-length with a soft natural wave, worn down.',
   hair_length='Its length reaches just past her collarbones.',
   outfit=dict(top='a fitted white ribbed cotton T-shirt that follows the line of her torso',
               top_hem='the hem is tucked into her shorts',
               bottom='blue denim shorts with a turned-up cuff',
               shoes='white canvas slip-ons',
               jewelry='a plain linen bib apron, dusted with flour across the front'),
   location='her one-person bakery studio in George Town — a stand mixer on the steel bench, cooling racks of madeleines behind her, and brown paper boxes stacked ready for pickup',
   light=dict(key='morning daylight comes through the shopfront window on her left and is the main light on her face',
              bounce='the steel bench throws that light back up into the shadow side of her face',
              secondary_source='', exposure_choice='the camera meters for her face, so the shopfront window blows out to flat white',
              occlusion='the back of the kitchen falls away into shadow')),
 'tammy-chou': dict(
   figure='她的身材在嬌小的骨架上胸線很滿，腰窄',
   hair_color_en='Her hair is a milk-tea golden brown, with a lighter money-piece section framing each side of her face.',
   hair_en='It is long and permed into a full airy wave, worn down.',
   hair_length='Its length reaches the middle of her back.',
   outfit=dict(top='a fitted cream ribbed knit long-sleeve top that follows the line of her torso',
               top_hem='the hem is tucked into her waistband',
               bottom='a high-waisted brown corduroy mini skirt',
               shoes='cream ankle boots', jewelry='layered thin gold necklaces'),
   location='her clothing studio — a double rail packed with stock behind her, a ring light on a stand switched off to one side, and a full-length mirror against the wall',
   light=dict(key='daylight comes through the studio window on her right and is the main light on her face',
              bounce='the white wall and the full-length mirror throw that light back into the shadow side of her face',
              secondary_source='', exposure_choice='the camera meters for her face, so the window blows out to flat white',
              occlusion='the depth of the clothing rail behind her falls away into shadow')),
 'wanyin-jiang': dict(
   figure='她的身材勻稱，肩線窄而平，腰細',
   hair_color_en='Her hair is a deep natural black, straight and heavy.',
   hair_en='It is very long and worn down, falling straight without a wave.',
   hair_length='Its length reaches her waist.',
   outfit=dict(top='a fitted dark teal silk mandarin-collar top that follows the line of her torso',
               top_hem='the hem sits at her hip bone',
               bottom='straight-leg black trousers', shoes='flat black cloth shoes',
               jewelry='a pair of small jade drop earrings'),
   location='her qipao workshop in a Suzhou courtyard house — bolts of silk stacked on the shelf behind her, a tailor’s dummy in the corner, and a lattice window onto the courtyard',
   light=dict(key='daylight comes through the lattice window on her left and is the main light on her face',
              bounce='the whitewashed wall behind her throws that light back into the shadow side of her face',
              secondary_source='', exposure_choice='the camera meters for her face, so the lattice window blows out to flat white',
              occlusion='the depth of the shelves behind her falls away into shadow')),
 'yerin-han': dict(
   figure='她的身材是高挑修長型，肩線平',
   hair_color_en='Her hair is a soft ash brown, evenly toned.',
   hair_en='It is long and straight, worn down with a middle parting.',
   hair_length='Its length reaches the middle of her back.',
   outfit=dict(top='a fitted heather-grey ribbed cotton long-sleeve top that follows the line of her torso',
               top_hem='the hem is tucked into her waistband',
               bottom='straight-leg indigo jeans sitting at her natural waist',
               shoes='white leather sneakers', jewelry='a thin silver ring on one hand'),
   location='her flat in Seoul — a bookshelf of paperbacks behind her, a record player on the low cabinet, and the window blinds half drawn',
   light=dict(key='afternoon daylight comes through the half-drawn blinds on her right and is the main light on her face',
              bounce='the pale wall on her left throws that light back into the shadow side of her face',
              secondary_source='', exposure_choice='the camera meters for her face, so the gaps in the blinds blow out to flat white',
              occlusion='the far side of the room falls away into shadow')),
 'zhiyi-shen': dict(
   figure='她的身材高挑，肩線平而清楚，腿長',
   hair_color_en='Her hair is a deep natural black with a strong sheen.',
   hair_en='It is long and straight with a middle parting, worn down.',
   hair_length='Its length reaches past her shoulder blades.',
   outfit=dict(top='a fitted black fine-knit turtleneck that follows the line of her torso',
               top_hem='the hem is tucked into her trousers',
               bottom='tailored charcoal straight-leg trousers sitting high at her waist',
               shoes='black heeled loafers', jewelry='a plain steel watch'),
   location='her apartment in Pudong late in the evening — a laptop still open on the dining table, a lanyard dropped beside it, and the tower lights across the river through the window',
   light=dict(key='the pendant light over the dining table is the main light on her face',
              bounce='the pale table top throws that light back up into the shadow side of her face',
              secondary_source='the tower lights across the river put a cool blue into the room behind her',
              exposure_choice='the camera meters for her face, so the pendant bulb blows out to flat white',
              occlusion='the far end of the room falls away into shadow')),
 'zoey-yeh': dict(
   figure='她的身材纖細，肩線窄',
   hair_color_en='Her hair is a natural black, fine and soft in texture.',
   hair_en='It is long and straight with a middle parting, worn down.',
   hair_length='Its length reaches the middle of her back.',
   outfit=dict(top='a fitted oatmeal ribbed cotton long-sleeve top that follows the line of her torso',
               top_hem='the hem is tucked into her waistband',
               bottom='a long sage-green cotton skirt',
               shoes='flat brown leather sandals',
               jewelry='a canvas bib apron with a brass clip on the front'),
   location='her flower shop in a converted old house — buckets of eucalyptus and lisianthus on the wooden floor, a roll of brown wrapping paper on the bench, and rain on the window behind her',
   light=dict(key='overcast daylight comes through the rain-covered shopfront window behind her left shoulder and wraps onto her face',
              bounce='the pale wooden floor throws that light back up into the shadow side of her face',
              secondary_source='', exposure_choice='the camera meters for her face, so the window blows out to flat white',
              occlusion='the back of the shop falls away into shadow')),
}

CUP = {'C': 'full and rounded', 'D': 'heavy and rounded',
       'E': 'strikingly heavy and rounded', 'F': 'strikingly heavy and rounded'}


def body(pid):
    """身材一律從胸開始寫，並明說四肢有肉。

    第一版 16/16 把 E 罩杯畫成平胸；把胸放句首、把「四肢有健康的肉」寫成
    肯定句之後才改善。這裡不寫「不瘦」之類的否定句，模型不執行否定。
    """
    f = M[pid]['fixed']
    w = CUP[f['cup']]
    lead = (f"Her figure reads full-chested first: her bust is {w}, and it carries the front of her "
            f"top out clearly beyond the line of her ribs.")
    waist = "Below it her waist draws in narrow."
    # 大腿只能出現在看得到大腿的景別——半身照寫大腿等於要求模型畫裁切外的部位。
    flesh_upper = ("Her upper arms and her shoulders carry a healthy layer of soft flesh over the "
                   "bone.")
    flesh_full = ("Her upper arms, her shoulders and her thighs all carry a healthy layer of soft "
                  "flesh over the bone.")
    # 身高分三段。二分法會把 165–167cm 也寫成「骨架很小、四肢短」，那是錯的描述。
    h = f['height_cm']
    if h >= 168:
        frame = "She is tall, and her legs are long in proportion to her body."
    elif h >= 162:
        frame = "She is of average height, and her legs are in even proportion to her body."
    else:
        frame = "Her whole frame is finely scaled and her limbs are short in proportion."

    return {
      'face_closeup': ("Her shoulders and the base of her neck enter the frame, with the collarbone "
                       "visible where it does."),
      'waist_up': f"{lead} {waist} {flesh_upper}",
      'knee_up': f"{lead} {waist} Her hips carry the same fullness. {flesh_full} {frame}",
      'full_body': f"{lead} {waist} Her hips carry the same fullness. {flesh_full} {frame}",
    }


out = {}
for pid, d in P.items():
    f = M[pid]['fixed']
    out[pid] = {
        'display': f['display'], 'age': f['age'], 'ethnicity_zh': f['ethnicity'],
        'face_en': M[pid]['face_en'],
        'refs_v2': json.load(open('pilot/r8_source_plan.json',
                                  encoding='utf-8'))['assignment'][pid],
        'identity_markers': M[pid]['markers'],
        'measurements': {k: f[k] for k in
                         ('height_cm', 'weight_kg', 'bust_cm', 'waist_cm', 'hip_cm', 'cup', 'leg_cm')},
        'figure_zh': d['figure'],
        'body_en': body(pid),
        'hair_color_en': d['hair_color_en'], 'hair_en': d['hair_en'],
        'hair_length_en': {k: d['hair_length'] for k in ('waist_up', 'knee_up', 'full_body')},
        'outfit_en': d['outfit'], 'location_en': d['location'],
        'light': {k: v for k, v in d['light'].items() if v},
        'barefoot': False,
    }

spec = {
  '_schema': 'batch3_casting/v2',
  '_face_note': '臉由四張裁切＋face_en 的位置式指派決定，不再用文字描述臉；'
                'face_base／face_negative 已整組移除。',
  '_outfit_note': '選角服裝一律合身：第一版寬鬆家居服把胸線蓋掉，16/16 把 E 罩杯畫成平胸。',
  '_negation_note': '全檔不寫否定句。已實測模型不執行否定。',
  'shared': json.load(open('pilot/batch3_casting.json', encoding='utf-8'))['shared'],
  'personas': out,
}
json.dump(spec, open('pilot/batch3_casting_v2.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print(f'已產生 {len(out)} 位選角規格 → pilot/batch3_casting_v2.json')
