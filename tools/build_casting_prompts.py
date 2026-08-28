#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""從 pilot/batch3_casting.json 產生 Phase A 選角 prompt（每人 4 段）。

措辭字典一律 import tools/prompt_lang.py——那裡的每一條都對應 Nico 那條
vertical slice 的一個實測失敗，抄一份到這裡就等於把教訓丟掉。

本檔自己只負責三件 Nico 沒有的事：
1. **臉部骨架寫死**。face_base 由 pilot/face_fingerprints.json 的 10 條軸展開，
   送生成前必須先過 tools/face_registry.py 的碰撞檢查。
2. **身體朝向寫「鏡頭看得到哪些正面特徵」**，不寫角度（"turned 30 degrees"
   連續三次被畫成背影）。
3. **全身圖一律第三人稱正面**——全身是身材比例的最終把關點，背影與鏡子自拍都判不了。
"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prompt_lang import *   # 共用措辭字典

# 選角 4 張：景別、視角、頭部朝向、視線、表情
SHOTS = [
    {"id": "a01", "framing": "face_closeup", "view": "selfie_front",  "head": "front",
     "gaze": "camera", "expr": "neutral_relaxed", "cam": "phone_front", "dist": "mild"},
    {"id": "a02", "framing": "waist_up",     "view": "third_person",  "head": "front",
     "gaze": "camera", "expr": "soft_smile",      "cam": "phone_rear",  "dist": "none"},
    {"id": "a03", "framing": "knee_up",      "view": "third_person",  "head": "right_30",
     "gaze": "away",   "expr": "calm_distant",    "cam": "phone_rear",  "dist": "none"},
    {"id": "a04", "framing": "full_body",    "view": "third_person",  "head": "front",
     "gaze": "camera", "expr": "neutral_composed", "cam": "phone_rear", "dist": "none"},
]

# 朝向：只描述鏡頭看得到哪些身體正面特徵。a03 是唯一的四分之三側身，
# 仍然明寫肚臍與胸前朝向鏡頭，因為「轉向」正是被畫成背影的那個詞。
ORIENTATION = {
    "a01": "Her chest and both shoulders face the camera squarely.",
    "a02": "Her navel, the front of her chest and the front of both shoulders all point toward the "
           "camera. Both of her collarbones are visible.",
    "a03": "Her hips stay square to the camera while her shoulders come round only a little, so the "
           "camera still sees the front of her chest, her navel and both collarbones, with one shoulder "
           "slightly nearer the lens than the other.",
    "a04": "Her navel, the front of her chest and the front of both shoulders all point toward the "
           "camera. Both of her collarbones are visible, and the camera sees the front of her lower "
           "half — the waistband at her hips and the front of both legs.",
}

ACTION = {
    "a01": "She has just picked up her phone and is taking a photograph of herself.",
    "a02": "She is standing in the middle of the room, letting someone take a picture of her.",
    "a03": "She has stopped halfway through crossing the room and is looking at something off to one side.",
    "a04": "She is standing still, arms relaxed at her sides, letting someone photograph her whole figure.",
}


def build(pid, p, shared, shot):
    f = shot["framing"]
    P = []
    P.append("A vertical photograph of " + p["face_base"])
    P.append(p["face_negative"])
    P.append("Her face carries these recognisable features: " + "; ".join(p["identity_markers"]) + ".")
    P.append("")
    if f == 'full_body' and p.get('barefoot'):
        P.append(shared['framing_full_body_barefoot'])
    else:
        P.append(FRAMING[f])
    P.append("")
    P.append(ACTION[shot["id"]])
    P.append("")
    P.append(ORIENTATION[shot["id"]])
    P.append(HEAD_YAW[shot["head"]])
    P.append(EYE_GAZE[shot["gaze"]])
    P.append(EXPRESSION[shot["expr"]])
    P.append(FACE_VIS["unobstructed"])
    P.append(VIEW[shot["view"]])
    P.append("")
    P.append(shared["makeup_en"])
    P.append(shared["skin_en"])
    P.append(p["body_en"][f])
    hair = p["hair_color_en"] + " " + p["hair_en"]
    hl = p.get("hair_length_en", {}).get(f)
    if hl:
        hair += " " + hl
    P.append(hair)
    lay = p["outfit_en"]
    worn = [lay[k] for k in VISIBLE_LAYERS[f] if lay.get(k)]
    P.append("She is wearing " + "; ".join(worn) + ".")
    # 赤腳只在看得到腳的景別交代，而且是獨立句子——塞進 "She is wearing" 清單會變成
    # 「穿著她赤腳」，而在看不到腳的景別提它等於要求模型畫裁切外的部位。
    if p.get('barefoot') and f == 'full_body':
        P.append("Her feet are bare against the floor.")
    P.append("")
    P.append("Setting: " + p["location_en"] + ".")
    el = p["light"]
    parts = ["Light: " + el["key"] + "; " + el["bounce"] + "."]
    if el.get("secondary_source"):
        parts.append("At the same time, " + el["secondary_source"] + ".")
    parts.append("Exposure: " + el["exposure_choice"] + ".")
    if el.get("occlusion"):
        parts.append(el["occlusion"].capitalize() + ".")
    P.append(" ".join(parts))
    P.append("")
    P.append(" ".join([CAMERA_TYPE[shot["cam"]], DISTORTION[shot["dist"]], DOF["adequate"]]))
    P.append(" ".join([FILTER["none"], COMPOSITION["centered"], BGC["moderate"], HL["allowed"]]))
    CLOSED = {
        # 實測：提到器材就會把器材畫進畫面——即使是在說它在畫面外（yerin/a04 出現三腳架單眼、
        # angeline/a02+a03 出現第二隻手拿手機）。收尾句一律不再提器材位置。
        "third_person":
            "Everything in this picture is accounted for: she is the only person present, and every "
            "visible hand connects to one of her own arms. The room holds only the furnishings named "
            "above. Illumination comes exclusively from the natural or architectural light sources "
            "named above.",
        "selfie_front":
            "Everything in this picture is accounted for: she is the only person present, and every "
            "visible hand connects to one of her own arms. The room holds only the furnishings named "
            "above. Illumination comes exclusively from the natural or architectural light sources "
            "named above.",
    }
    P.append("Real skin texture with visible pores and fine flyaway hairs. " + CLOSED[shot["view"]])
    return "\n".join(P)


if __name__ == '__main__':
    spec = json.load(open('pilot/batch3_casting.json', encoding='utf-8'))
    out = {}
    for pid, p in spec['personas'].items():
        for shot in SHOTS:
            out[f"{pid}/{shot['id']}"] = build(pid, p, spec['shared'], shot)
    json.dump(out, open('pilot/batch3_casting_prompts.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f"已產生 {len(out)} 段選角 prompt → pilot/batch3_casting_prompts.json")
