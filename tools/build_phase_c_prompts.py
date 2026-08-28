#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""從 pilot/nico_pilot.json 產生 Phase C 20 段 prompt。

**為什麼要用程式產生**：R3 的教訓是人工抄寫必然漂移。這 20 段 prompt 是真正會送進
模型、花掉 credit 的東西，不能手寫。每一段都由該列的結構欄位組出來，
欄位改了 prompt 就跟著改，不會有「JSON 一套、prompt 另一套」。

**措辭來源**：Round 2 / Round 3 / Phase B 的實測結論（見 kols/nico-tsai/generation_notes.md）
1. 這個模型**不執行否定句**。構圖與服裝結構一律用「畫面裡有什麼、邊界切在哪裡」描述。
2. 身體朝向**不能寫角度**（"turned 30 degrees" 連續三次被畫成背影）。
   一律寫「相機看得到哪些身體正面特徵」。
3. Reference Element 在**指定同一件衣服**時會把該件衣服的細節整件複製。
"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ANCHOR = "68ff990e-1862-4003-bfe3-fe288275cdd4"

from prompt_lang import *   # 共用措辭字典（見該檔頂端的五條實測規則）

LOCATION = {
 'workplace_own_studio': "her own small nail studio in Taipei — a white manicure desk, a task lamp "
   "clamped to its edge, shelves of gel colour bottles on the wall",
 'local_cafe': "a small neighbourhood cafe, wooden tables and a bar counter behind her",
 'own_bedroom': "her own bedroom, the bed unmade behind her",
 'own_bathroom': "her own small bathroom, white tiled walls and a basin",
 'own_entryway': "the entryway of her flat, a shoe cabinet against the wall and the front door beside her",
 'park': "a paved path through an ordinary neighbourhood park in Taipei, low shrubs and a row of trees",
 'city_street': "an ordinary back lane in the Da'an district of Taipei, scooters parked along the wall",
 'breakfast_shop': "a Taiwanese breakfast shop, stainless-steel tables and plastic stools, the shutter "
   "door open to the street",
 'convenience_store': "the inside of a Taiwanese convenience store, magazine racks and shelves of goods",
 'laundromat': "a self-service laundromat, a row of front-loading machines along the wall",
 'pharmacy': "the aisle of a Taiwanese drugstore, shelves of boxed products",
 'train_platform': "an MRT platform in Taipei, tiled floor and the track edge behind her",
}

def build(shot, pilot, en):
    o = pilot['outfits'][shot['outfit_id']]
    props = {p['id']: p for p in shot['props']}
    L, w = [], None
    P = []
    P.append(f"A vertical photograph of <<<{ANCHOR}>>>.")
    P.append(FRAMING[shot['framing']])
    P.append("")
    P.append(en['action'])
    P.append("")
    P.append(en['body'])
    P.append(HEAD_YAW[shot['head_yaw']])
    P.append(HEAD_PITCH[shot['head_pitch']])
    P.append(EYE_GAZE[shot['eye_gaze']])
    P.append(EXPRESSION[shot['expression']])
    P.append(FACE_VIS[shot['face_visibility']])
    P.append(VIEW[shot['view']])
    P.append("")
    hl, hr = shot['hands']['left'], shot['hands']['right']
    vis = en.get('hands_visible', {'left': True, 'right': True})
    if (hl['state'] == hr['state'] == 'holding' and hl['object_ref'] == hr['object_ref']):
        # held_both：一個物件由雙手共同持有，不要輸出兩行重複的句子
        P.append(f"Both of her hands together are holding {en['props'][hl['object_ref']]} — "
                 f"{en['hands']['left']}.")
    else:
        # C-37：裁切外的手不寫進 prompt——描述看不見的東西會跟景別指令競爭
        if vis.get('left'):  P.append(hand_line('left', hl, props, en))
        if vis.get('right'): P.append(hand_line('right', hr, props, en))
    seen = [prop_line(q, en) for q in shot['props'] if q.get('expected_visible')]
    seen = [v for v in seen if v]
    if seen:
        P.append("Also in the picture: " + "; ".join(seen) + ".")
    P.append("")
    P.append("Her face is bare: her lips are the same soft pinkish-beige as the skin around them, matte, "
             "with a soft undefined edge; her eyebrows are soft and natural; her lashes are her own and "
             "unmade. Light neutral-to-cool skin with natural tonal variation and visible pores.")
    P.append(pilot['body_en'][shot['framing']])
    P.append(pilot['hair_color_en'] + " " + pilot['hair_en'][shot['hair_id']])
    lay = o['en_layers']
    worn = [lay[k] for k in VISIBLE_LAYERS[shot['framing']] if lay.get(k)]
    if lay.get('rings') and any(vis.values()):
        worn.append(lay['rings'])
    bag_t = BAG_TEXT.get(en.get('bag_state', 'none'))
    if bag_t and lay.get('bag'):
        worn.append(bag_t.format(bag=lay['bag']))
    P.append("She is wearing " + "; ".join(worn) + ".")
    P.append("")
    P.append("Setting: " + LOCATION[shot['location']] + ".")
    el = en['light']
    parts = ["Light: " + el['key'] + "; " + el['bounce'] + "."]
    if el.get('secondary_source'): parts.append("At the same time, " + el['secondary_source'] + ".")
    parts.append("Exposure: " + el['exposure_choice'] + ".")
    if el.get('occlusion'): parts.append(el['occlusion'].capitalize() + ".")
    P.append(" ".join(parts))
    P.append("")
    cam = shot['camera']
    P.append(" ".join([CAMERA_TYPE[cam['type']], DISTORTION[cam['distortion']], DOF[cam['depth_of_field']]]))
    ip = shot['imperfection_profile']
    real = [FILTER[shot['filter']], COMPOSITION[ip['composition']], MOTION[ip['motion']],
            WB[ip['white_balance']], BGC[ip['background_clutter']], HL[ip['highlight_clipping']]]
    P.append(" ".join(x for x in real if x))
    # C-42：改為正面封閉集合。原本整段靠 no other people / No phone / No photography equipment，
    # 但這個模型不可靠地執行否定，而這三類正是先前真的生成過的錯誤。
    CLOSED = {
     'third_person':
        "Everything in this picture is accounted for: the only person in it is her, and every visible "
        "hand connects to one of her own arms. The camera viewpoint sits nearby at about eye level, "
        "with the imaging device and whoever holds it beyond the frame edge. Illumination comes "
        "exclusively from the natural or architectural light sources named above.",
     'selfie_front':
        "Everything in this picture is accounted for: the image is what her phone's front camera sees, "
        "so the device itself sits just beyond the frame edge. The only person in it is her, and every "
        "visible hand connects to one of her own arms. Illumination comes exclusively from the natural "
        "or architectural light sources named above.",
     'selfie_mirror':
        "Everything in this picture is accounted for: within the reflected bathroom scene the only "
        "person is her and the only device is the single phone in her raised hand. Every visible hand "
        "connects to one of her own arms. Illumination comes exclusively from the fixtures named above.",
    }
    P.append("Real skin texture with visible pores and fine flyaway hairs. " + CLOSED[shot['view']])
    return "\n".join(P)

if __name__ == '__main__':
    pilot = json.load(open('pilot/nico_pilot.json', encoding='utf-8'))
    actions = json.load(open('pilot/phase_c_actions_en.json', encoding='utf-8'))
    out = {}
    for s in pilot['phase_c_shots']:
        sid = s['shot_id']
        if sid not in actions:
            print(f"缺 {sid} 的英文動作句", file=sys.stderr); sys.exit(1)
        out[sid] = build(s, pilot, actions[sid])
    json.dump(out, open('pilot/phase_c_prompts.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f"已產生 {len(out)} 段 prompt → pilot/phase_c_prompts.json")
