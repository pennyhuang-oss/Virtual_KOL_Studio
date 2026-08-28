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
import json, sys

ANCHOR = "68ff990e-1862-4003-bfe3-fe288275cdd4"

# ── 景別：描述畫面下緣切在哪裡（正面描述，不用 "nothing below X is visible"）──
FRAMING = {
 'face_closeup': "The bottom edge of the picture sits just below her collarbones. Her face fills most "
                 "of the frame, from the top of her hair down to the base of her neck. Her shoulders are "
                 "only barely in the picture and none of her torso, arms or hands is in it.",
 'chest_up':     "The bottom edge of the picture cuts across her chest, a little below her armpits. Her "
                 "head, shoulders and upper chest fill the frame. Her waist, hips, legs and feet are "
                 "outside the picture.",
 'waist_up':     "The bottom edge of the picture cuts across her waist at about the level of her navel. "
                 "Her head, shoulders, chest and waist fill the frame. Her hips, legs and feet are "
                 "outside the picture.",
 'knee_up':      "The bottom edge of the picture cuts across her legs just below the knees. Her head, "
                 "torso, hips and thighs are all inside the frame. Her lower legs and feet are outside "
                 "the picture.",
 'full_body':    "The whole of her is inside the picture, from the top of her head down to her shoes, "
                 "with a margin of empty ground below her feet and a little space above her head. Her "
                 "legs and shoes are clearly visible.",
}

# ── 身體朝向：寫「鏡頭看得到哪些正面特徵」，不寫角度 ──
# 身體朝向不由 head_yaw 推導——scene 才是動作的真理來源，而且「轉向」正是連續三次
# 被畫成背影的那個詞。改為逐列明寫在 pilot/phase_c_actions_en.json 的 body 欄，
# 與該列的中文 scene 一起送覆核。

HEAD_YAW = {
 'front':        "Her head is straight on to the camera.",
 'left_30':      "Her head is turned a little toward her own left, so the camera sees slightly more of "
                 "the right side of her face; her far cheek and both eyes are still fully visible.",
 'right_30':     "Her head is turned a little toward her own right, so the camera sees slightly more of "
                 "the left side of her face; her far cheek and both eyes are still fully visible.",
 'left_60':      "Her head is turned well toward her own left, so the camera mostly sees the right side "
                 "of her face; the far eye is still visible but the far cheek is mostly hidden.",
 'right_60':     "Her head is turned well toward her own right, so the camera mostly sees the left side "
                 "of her face; the far eye is still visible but the far cheek is mostly hidden.",
 'profile_left': "Her head is turned all the way to her own left, so the camera sees her profile: the "
                 "outline of her forehead, nose, lips and chin reads clearly against the background, and "
                 "only the near eye is visible.",
 'profile_right':"Her head is turned all the way to her own right, so the camera sees her profile: the "
                 "outline of her forehead, nose, lips and chin reads clearly against the background, and "
                 "only the near eye is visible.",
}
HEAD_PITCH = {
 'neutral': "Her chin is level.",
 'up_10':   "Her chin is raised a little, so her face tilts slightly upward.",
 'down_15': "Her chin is dipped, so her face tilts downward and her eyelids read lower.",
}
EYE_GAZE = {
 'camera': "She looks directly into the lens.",
 'away':   "Her eyes are directed off past the camera at something in the distance, not at the lens.",
 'down':   "Her eyes are lowered toward what is in front of her.",
 'mirror': "She looks at her own reflection in the mirror.",
}
VIEW = {
 'third_person': "Someone standing near her is holding the phone and taking this photo of her.",
 'selfie_front': "She is holding the phone herself, arm extended, shooting with the front camera. The "
                 "phone is the camera and is not itself in the picture.",
 'selfie_mirror':"She is photographing her own reflection in the mirror. The phone she is holding is "
                 "visible in the reflection.",
}
FACE_VIS = {
 'unobstructed': "Her whole face is unobstructed.",
 'partial_hair': "A few strands of hair fall across one side of her face.",
 'partial_hand': "The hand she is working with crosses in front of part of her face.",
}
EXPRESSION = {
 'neutral_relaxed':"Her expression is relaxed and neutral, mouth closed and soft.",
 'neutral_composed':"Her expression is composed and neutral, mouth closed.",
 'soft_smile':"A small closed-mouth smile, the corners barely lifted.",
 'focused':"She is concentrating on what her hands are doing; her mouth is closed and her brow is still.",
 'reading_focused':"She is reading something and concentrating on it.",
 'concentrating_slight_frown':"She is concentrating hard enough that her brows draw very slightly together.",
 'listening_attentive':"She is listening to someone, attentive, mouth closed.",
 'mid_conversation':"Her mouth is slightly open mid-sentence, caught talking.",
 'mildly_surprised':"Her eyebrows are lifted a little, mildly caught off guard.",
 'mildly_annoyed':"A faint flicker of irritation, mouth set.",
 'tired_soft':"She looks tired: eyelids a little heavy, face soft and unguarded.",
 'blank_waiting':"Her face is blank, the way a face goes when someone is simply waiting.",
 'calm_distant':"Calm and a little distant, thinking about something else.",
 'neutral_walking':"A neutral everyday face, caught mid-walk.",
 'post_shower_calm':"Calm and freshly washed, her face relaxed and a little damp.",
}

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

BOUNCE = {'diffuse':'', 'specular':''}
CAMERA_TYPE = {
 'phone_rear':"Shot on the rear camera of a phone.",
 'phone_front':"Shot on the front camera of a phone, held at arm's length.",
 'mirror_phone':"Shot on the rear camera of a phone aimed at a mirror.",
}
DISTORTION = {'none':"No lens distortion.",
              'mild':"The slight wide-angle stretch a phone lens gives at close range."}
DOF = {'adequate':"Adequate depth of field — her face, her body and the background are all in "
                  "reasonable focus. This is not a shallow blurred-background portrait; her body "
                  "outline stays sharp and readable.",
       'shallow':"Shallow depth of field: she is sharp and the background falls out of focus."}
FILTER = {'none':"Straight out of the phone, no filter and no beauty retouching.",
          'ccd':"It has the look of an old CCD compact camera: slightly soft, a little grain, "
                "colours very slightly off from true."}
COMPOSITION = {'centered':"She sits centred in the frame.",
               'off_center':"She sits off to one side of the frame rather than centred.",
               'slightly_tilted':"The horizon is very slightly tilted, the way a hand-held snapshot is."}
MOTION = {'none':"", 'minor_hand_blur':"Her moving hand is very slightly blurred, though her face stays sharp.",
          'subject_motion':"There is a trace of motion blur where she is moving, though her face stays sharp."}
WB = {'neutral':"", 'slightly_cool_auto':"The phone's auto white balance has gone a touch cool.",
      'slightly_warm_auto':"The phone's auto white balance has gone a touch warm.",
      'color_cast_from_environment':"The surroundings throw a visible colour cast across her."}
BGC = {'clean':"The background behind her is uncluttered.",
       'moderate':"There is ordinary everyday clutter in the background.",
       'heavy':"The background is busy with the ordinary mess of the place."}
HL = {'none':"", 'allowed':"A few highlights are allowed to blow out to white.",
      'heavy':"The brightest parts of the frame are blown right out to white."}

HAND_STATE = {
 'free':"is free", 'holding':"is holding", 'supporting':"is braced", 'camera':"is holding the phone",
}

def hand_line(side, slot, props, en):
    note = en['hands'][side]
    if slot['state'] == 'camera':
        return f"Her {side} hand holds the phone that is taking this picture ({note})."
    if slot['state'] == 'holding':
        return f"Her {side} hand holds {en['props'][slot['object_ref']]} ({note})."
    if slot['state'] == 'supporting':
        return f"Her {side} hand is braced {note}."
    return f"Her {side} hand is {note}."

def prop_line(p, en):
    rel = p['relation']; name = en['props'][p['id']]
    if rel.startswith('held'):
        return None   # 已由 hand_line 交代
    if rel == 'worn':
        return f"the {name}"
    if rel == 'background':
        return f"{name}, visible behind her"
    return f"{name}"

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
    if (hl['state'] == hr['state'] == 'holding' and hl['object_ref'] == hr['object_ref']):
        # held_both：一個物件由雙手共同持有，不要輸出兩行重複的句子
        P.append(f"Both of her hands together are holding {en['props'][hl['object_ref']]} — "
                 f"{en['hands']['left']}.")
    else:
        P.append(hand_line('left', hl, props, en))
        P.append(hand_line('right', hr, props, en))
    vis = [prop_line(p, en) for p in shot['props']]
    vis = [v for v in vis if v]
    if vis:
        P.append("Also in the picture: " + "; ".join(vis) + ".")
    P.append("")
    P.append("Her face is bare: her lips are the same soft pinkish-beige as the skin around them, matte, "
             "with a soft undefined edge; her eyebrows are soft and natural; her lashes are her own and "
             "unmade. Light neutral-to-cool skin with natural tonal variation and visible pores.")
    P.append(pilot['hair_color_en'] + " " + pilot['hair_en'][shot['hair_id']])
    P.append("She is wearing: " + o['en'])
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
    phone = ("The only phone in the picture is the one she is holding up at the mirror. "
             if shot['view'] == 'selfie_mirror' else "No phone is in the picture. ")
    P.append("Real skin texture with visible pores and fine flyaway hairs. She is the only person in the "
             "picture — no other people and no one else's hands. " + phone +
             "No photography equipment of any kind: no softbox, no reflector, no foam board, no light "
             "stand, no tripod, no backdrop.")
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
