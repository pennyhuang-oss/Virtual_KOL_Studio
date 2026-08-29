#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A0 純臉選角 prompt。ChatGPT (B)「先鑄臉、後入戲」。

與 Phase A/C 的最大差別：**這一段沒有場景**。
上一輪四張臉全部收斂的成因之一，就是四段 prompt 的非臉部分逐字相同
（膚色、妝、相機、濾鏡、收尾、居家場景、素顏、白天自然光），共同語境比臉部差異更強勢。
A0 把那些全部拿掉，只留：成年身分／既定髮色／素色圓領上衣／正面眼平／中性表情／
均勻柔光／淺灰背景。臉佔全段約 80%。

不得出現：職業、服裝造型、場景、道具、身材、濾鏡、相機器材。
（器材那條是實測——提到器材就會把器材畫進畫面，即使是在說它在畫面外。）
"""
import json, sys, os

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
RO = json.load(open('pilot/face_refs_readout.json', encoding='utf-8'))['refs']
SLOTS = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']

# 標準化拍攝條件。刻意不寫相機、鏡頭、燈具——只寫畫面裡看得到的狀態。
SHOT = ("Photographed straight on at eye level, head upright and square to the lens, expression "
        "calm and neutral, mouth closed. Her hair is combed back so that her hairline, both ears, "
        "the whole line of her jaw and both cheeks read clearly. She wears a plain grey crew-neck "
        "cotton top against an even, featureless light grey backdrop. Soft frontal light lands "
        "equally on both sides of her face. The frame runs from just above her head down to the "
        "top of her shoulders. Real skin with visible pores and natural tonal variation.")


def build(pid):
    d = D['personas'][pid]
    f = d['fixed']
    P = [d['face_en']]
    if d.get('negative_en') and d['negative_en'].strip().upper() != 'NONE':
        P.append(d['negative_en'])
    P.append("Her face carries these recognisable features: " + "; ".join(d['markers']) + ".")
    P.append("")
    P.append(d['_a0_hair_en'])
    P.append(SHOT)
    return "\n".join(P)


def manifest(pid):
    r = D['personas'][pid].get('refs_v2') or D['personas'][pid]['refs']
    out = []
    for i, s in enumerate(SLOTS):
        ref = r[s]
        hit = [x for x in os.listdir('review/batch3_face_refs') if x.startswith(ref + '.')]
        if not hit:
            raise SystemExit(f'{pid}: {ref} 檔案不存在')
        out.append({'array_index': i, 'slot': s, 'ref': ref,
                    'path': 'review/batch3_face_refs/' + hit[0],
                    'usability': RO[ref]['usability']})
    return out


if __name__ == '__main__':
    pid = sys.argv[1]
    d = D['personas'][pid]
    if '_a0_hair_en' not in d:
        raise SystemExit(f'{pid} 缺 _a0_hair_en（A0 需要一句只講髮色髮型、不講造型的英文）')
    txt = build(pid)
    man = manifest(pid)
    # F-01：送出前必須有 manifest，順序不符 HARD FAIL
    assert [m['slot'] for m in man] == SLOTS, '附圖順序與槽位順序不符'
    face_chars = len(d['face_en']) + len(d.get('negative_en', '')) + len('; '.join(d['markers']))
    print(f"=== {pid} A0 ===")
    print(f"臉部佔比：{face_chars}/{len(txt)} = {face_chars/len(txt):.0%}")
    print("\n--- manifest ---")
    for m in man:
        print(f"  [{m['array_index']}] {m['slot']:20s} {m['ref']} ({m['usability']})  {m['path']}")
    print("\n--- prompt ---")
    print(txt)
