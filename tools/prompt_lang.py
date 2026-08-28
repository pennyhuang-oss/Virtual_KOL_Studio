#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""所有角色共用的 prompt 措辭字典。

**為什麼要獨立成一個模組**：這些措辭是 Nico 那條 vertical slice 用 35 張實測換來的，
不是文案偏好。每一條都對應一個具體的失敗：
1. 這個模型**不執行否定句**——景別、服裝結構、朝向一律寫「畫面裡有什麼、邊界切在哪裡」。
2. 身體朝向**不能寫角度**（"turned 30 degrees" 連續三次被畫成背影），
   要寫「相機看得到哪些身體正面特徵」。
3. `COMPOSITION` 不得出現姿態動詞（原本的 `She sits centred` 把 10 段站姿改成坐姿）。
4. 具名攝影器材會被當成場景道具畫進畫面——光線一律描述房間裡真實存在的表面。
5. 收尾用**正面封閉集合**（"the only person in it is her"），不是 `no other people`。

抄一份到新角色的 script 裡就等於把這些教訓丟掉，所以一律 import 這裡。
`LOCATION` 是每個角色自己的場景，不放這裡。
"""

# ── 景別：描述畫面下緣切在哪裡（正面描述，不用 "nothing below X is visible"）──
FRAMING = {
 'face_closeup': "The bottom edge of the picture sits just below her collarbones. Her face fills most "
                 "of the frame, from the top of her hair down to the base of her neck. Her shoulders are "
                 "only barely in the picture; everything below them is outside it.",
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

# ── C-37：各景別看得見哪些服裝層 ──
VISIBLE_LAYERS = {
 'face_closeup': ['top', 'jewelry'],
 'chest_up':     ['top', 'jewelry'],
 'waist_up':     ['top', 'top_hem', 'bottom', 'jewelry'],
 'knee_up':      ['top', 'top_hem', 'bottom', 'jewelry'],
 'full_body':    ['top', 'top_hem', 'bottom', 'shoes', 'jewelry'],
}
# C-47：戒指／手鍊戴在手上，可見與否由「那隻手有沒有入鏡」決定，不是由景別決定。
BAG_TEXT = {
 'worn_shoulder':"{bag} hangs from her shoulder",
 'worn_crossbody':"{bag} is worn across her body",
 'set_down':"{bag} is set down beside her",
 'outside_frame':None, 'none':None,
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
 'away':   "Her eyes rest on something in the distance, off past the camera.",
 'down':   "Her eyes are lowered toward what is in front of her.",
 'mirror': "She looks at her own reflection in the mirror.",
}
VIEW = {
 'third_person': "The photograph is taken from a short distance away, at about eye level.",
 # 實測：講「器材就在畫面邊緣外」會把器材畫進畫面。只說這張圖是什麼，不說器材在哪裡。
 'selfie_front': "The picture is what her phone's own front camera sees, taken at arm's length.",
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


BOUNCE = {'diffuse':'', 'specular':''}
CAMERA_TYPE = {
 'phone_rear':"Shot on the rear camera of a phone.",
 'phone_front':"Shot on the front camera of a phone, held at arm's length.",
 'mirror_phone':"Shot on the rear camera of a phone aimed at a mirror.",
}
DISTORTION = {'none':"Straight rectilinear lens geometry: architectural lines render as straight segments with "
              "natural perspective.",
              'mild':"The slight wide-angle stretch a phone lens gives at close range."}
DOF = {'adequate':"Deep depth of field: every visible part of her and the background stay in focus "
                  "together, and her outline reads sharp against what is behind her.",
       'shallow':"Shallow depth of field: she is sharp and the background falls out of focus."}
FILTER = {'none':"The picture is straight out of the phone's camera roll, exactly as the sensor recorded it.",
          'ccd':"It has the look of an old CCD compact camera: slightly soft, a little grain, "
                "colours very slightly off from true."}
# C-36：原本寫 `She sits centred in the frame`——`sits` 對模型是明確動作，
# 會把 10 段站姿／走姿／蹲姿改成坐姿。composition 模板一律不得出現姿態動詞。
COMPOSITION = {'centered':"She is positioned centrally in the frame.",
               'off_center':"Her figure is positioned off-centre in the frame.",
               'slightly_tilted':"The horizon runs very slightly off level, the way a hand-held snapshot does."}
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
        return name
    return f"{name}"
