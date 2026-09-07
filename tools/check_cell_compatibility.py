#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""逐格比對「人設軸」與「來源判讀」，標出方向相反的格（ChatGPT R13 T-03）。

為什麼需要：cheryl-soh 原本被排到 ref_08 當臉型，人設是「長卵形／長窄／窄顎」，
ref_08 的判讀卻是「中短，柔和圓潤，雙頰寬，顎線圓轉」——方向完全相反。
那是因為我把人設相容性整個移出解算目標，變成完全不看。這支把它補回來，
但只當「標出相反」用，不當最佳化目標——用數字驅動配對正是先前做歪的原因。
"""
import json, sys

SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
SLZH = {'FACE_SHAPE_AND_JAW': '臉型顎線', 'EYES_AND_BROWS': '眼與眉',
        'NOSE': '鼻', 'MOUTH': '口'}
READ_KEY = {'FACE_SHAPE_AND_JAW': 'face_shape_and_jaw', 'EYES_AND_BROWS': 'eyes_and_brows',
            'NOSE': 'nose', 'MOUTH': 'mouth'}
# 人設軸 → 該槽位要看的軸
AXES_OF = {'FACE_SHAPE_AND_JAW': ['輪廓原型', '臉長寬比', '三庭配置', '骨肉量', '顎頦', '頰部'],
           'EYES_AND_BROWS': ['眼眶結構', '眼距'], 'NOSE': ['鼻部量體'], 'MOUTH': ['口部幾何']}

# 相反詞對：(人設軸值裡的關鍵詞, 來源判讀裡代表相反方向的關鍵詞)
OPPOSITE = {
 'FACE_SHAPE_AND_JAW': [
   (('長窄', '極長窄', '長卵', '長方', '窄矩形', '窄長'), ('短', '中短', '圓', '短圓')),
   (('短寬', '短寬U', '短寬圓角'), ('長而窄', '長卵', '中長', '極長')),
   (('窄顎',), ('顎線寬', '寬而', '雙頰寬', '中臉最寬')),
   (('寬顎', '寬方顎'), ('顎線窄', '窄而')),
   (('清瘦平面',), ('柔軟飽滿', '肉感', '雙頰飽滿')),
   (('柔軟飽滿',), ('清瘦', '平面')),
 ],
 'EYES_AND_BROWS': [
   (('圓開',), ('細長', '窄眼', '單眼皮窄')),
   (('細長', '窄長', '單眼皮'), ('大而偏圓', '極大而圓', '大而圓')),
   (('眼距": "窄',), ('眼距寬',)),
 ],
 'NOSE': [
   (('長直細鼻',), ('短', '低鼻樑', '鼻頭小而圓', '極小')),
   (('短寬軟鼻',), ('長', '細', '鼻樑直')),
 ],
 'MOUTH': [
   (('寬中等唇', '寬薄唇', '寬飽滿'), ('小而', '小口', '口小')),
   (('小中等唇', '小薄平唇', '小飽滿唇'), ('寬', '中偏寬')),
 ],
}


def main():
    A = json.load(open('pilot/assignment_draft_v3.json', encoding='utf-8'))['assignment']
    D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))['personas']
    RO = json.load(open('pilot/face_refs_readout.json', encoding='utf-8'))
    RO = RO['refs'] if 'refs' in RO else RO
    rows, flags = [], []
    for p in sorted(A):
        ax = D[p]['axes']
        for s in SL:
            r = A[p][s]
            spec = ' / '.join(ax[a] for a in AXES_OF[s])
            read = str(RO.get(r, {}).get(READ_KEY[s], '')).strip()
            bad = []
            for keys, opps in OPPOSITE[s]:
                if any(k in spec for k in keys) and any(o in read for o in opps):
                    bad.append(f'人設「{[k for k in keys if k in spec][0]}」'
                               f'對上來源「{[o for o in opps if o in read][0]}」')
            rows.append({'persona': p, 'slot': s, 'ref': r, 'spec': spec,
                         'readout': read, 'conflicts': bad})
            if bad:
                flags.append((p, s, r, spec, read, bad))
    print(f'逐格相容檢查：76 格，標出方向相反的 {len(flags)} 格\n')
    for p, s, r, spec, read, bad in flags:
        print(f'✗ {p} / {SLZH[s]}　←　{r}')
        print(f'    人設：{spec}')
        print(f'    來源：{read[:78]}')
        for b in bad:
            print(f'    衝突：{b}')
        print()
    json.dump({'_purpose': 'ChatGPT R13 T-03 的逐格相容理由與衝突標記',
               '_method': '人設軸值對上 pilot/face_refs_readout.json 的逐張判讀；'
                          '只標出方向相反，不作為配對的最佳化目標',
               'flagged': len(flags), 'cells': rows},
              open('pilot/cell_compatibility.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'→ pilot/cell_compatibility.json（76 格全部的人設軸與來源判讀對照）')
    return 1 if flags else 0


if __name__ == '__main__':
    sys.exit(main())
