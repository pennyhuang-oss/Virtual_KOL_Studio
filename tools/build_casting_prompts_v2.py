#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""從 pilot/batch3_casting_v2.json 產生選角 prompt（每人 4 段）＋每段要掛的四張裁切。

措辭字典一律 import tools/prompt_lang.py，鏡頭／朝向／動作沿用 v1 的 SHOTS
與 ORIENTATION／ACTION——那些每一條都對應一次實測失敗，重寫等於把教訓丟掉。

與 v1 的唯一結構差別：臉不再是一段文字描述，而是
「四張部件裁切 ＋ 位置式指派句（Image 1..4）」。文字描述臉正是上一批
被退回（「五官全都太像」）的直接原因。
"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prompt_lang import *
from build_casting_prompts import SHOTS, ORIENTATION, ACTION

SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
V = json.load(open('pilot/crop_spec.json', encoding='utf-8'))['crop_spec_version']
MAN = json.load(open('pilot/face_crops_manifest.json', encoding='utf-8'))['artifacts']

# 器材一提就會被畫進畫面（實測：yerin/a04 出現三腳架單眼、angeline 出現第二隻手拿手機），
# 所以收尾句不提器材位置，只封閉人／物／光三件事。
CLOSED = ("Everything in this picture is accounted for: she is the only person present, and every "
          "visible hand connects to one of her own arms. The room holds only the furnishings named "
          "above. Illumination comes exclusively from the natural or architectural light sources "
          "named above.")


def crops(p):
    out = []
    for s in SL:
        a = MAN[f"{p['refs_v2'][s]}__{s}__{V}"]
        assert a['qa_status'] == 'pass', f"{a['out_path']} 未過 QA"
        out.append(a['out_path'])
    return out


def build(pid, p, shared, shot):
    f = shot['framing']
    P = []
    P.append('A vertical photograph of a ' + str(p['age']) + '-year-old adult woman.')
    P.append(p['face_en'])
    P.append('Her face carries these recognisable features: ' + '; '.join(p['identity_markers']) + '.')
    P.append('')
    P.append(FRAMING[f])
    P.append('')
    P.append(ACTION[shot['id']])
    P.append('')
    P.append(ORIENTATION[shot['id']])
    P.append(HEAD_YAW[shot['head']])
    P.append(EYE_GAZE[shot['gaze']])
    P.append(EXPRESSION[shot['expr']])
    P.append(FACE_VIS['unobstructed'])
    P.append(VIEW[shot['view']])
    P.append('')
    P.append(shared['makeup_en'])
    P.append(shared['skin_en'])
    P.append(p['body_en'][f])
    hair = p['hair_color_en'] + ' ' + p['hair_en']
    hl = p.get('hair_length_en', {}).get(f)
    if hl:
        hair += ' ' + hl
    P.append(hair)
    lay = p['outfit_en']
    worn = [lay[k] for k in VISIBLE_LAYERS[f] if lay.get(k)]
    P.append('She is wearing ' + '; '.join(worn) + '.')
    P.append('')
    P.append('Setting: ' + p['location_en'] + '.')
    el = p['light']
    parts = ['Light: ' + el['key'] + '; ' + el['bounce'] + '.']
    if el.get('secondary_source'):
        parts.append('At the same time, ' + el['secondary_source'] + '.')
    parts.append('Exposure: ' + el['exposure_choice'] + '.')
    if el.get('occlusion'):
        parts.append(el['occlusion'].capitalize() + '.')
    P.append(' '.join(parts))
    P.append('')
    P.append(' '.join([CAMERA_TYPE[shot['cam']], DISTORTION[shot['dist']], DOF['adequate']]))
    P.append(' '.join([FILTER['none'], COMPOSITION['centered'], BGC['moderate'], HL['allowed']]))
    P.append('Real skin texture with visible pores and fine flyaway hairs. ' + CLOSED)
    return '\n'.join(x for x in P if x is not None)


if __name__ == '__main__':
    spec = json.load(open('pilot/batch3_casting_v2.json', encoding='utf-8'))
    out = {}
    for pid, p in spec['personas'].items():
        c = crops(p)
        for shot in SHOTS:
            out[f"{pid}/{shot['id']}"] = {'prompt': build(pid, p, spec['shared'], shot),
                                          'crops': c}
    json.dump(out, open('pilot/batch3_casting_prompts_v2.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'已產生 {len(out)} 段選角 prompt → pilot/batch3_casting_prompts_v2.json')
