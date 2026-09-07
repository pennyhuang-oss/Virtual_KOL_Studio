#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""建立 15 × 4 donor-slot 可用性表（ChatGPT R10 的 P-01）。

跟舊 QA 的差別，每一條都是 R10 明確推翻我的地方：

1. **不再用一組門檻刷所有槽位。** 正面度按槽位分級：
   臉型 ≤0.10、眼 ≤0.10、鼻 ≤0.20、口 ≤0.25。
2. **解析度改成 A／B／C 分級，看原始資訊量**，不是一刀切的 96px 及格線：
   A ≥96px 可直接用；B 48–95px 要先做 probe；C <48px 不直接用。
3. **不合格的格子照樣把圖裁出來**——要看得見部件才能排表，
   看不到部件就先排 ID 正是前幾輪失敗的做法。

輸出 pilot/donor_slot_table.json 與 review/donor_cards/。全部本機作業，不花 credits。
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image
from build_face_crops import (SPEC, V, REFDIR, landmarks, compute_box,
                              crop_and_pad, sha256)

OUT_DIR = 'review/donor_cards'
SLOTS = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
SLZH = {'FACE_SHAPE_AND_JAW': '臉型顎線', 'EYES_AND_BROWS': '眼與眉',
        'NOSE': '鼻', 'MOUTH': '口'}
YAW_MAX = {'FACE_SHAPE_AND_JAW': 0.10, 'EYES_AND_BROWS': 0.10,
           'NOSE': 0.20, 'MOUTH': 0.25}
# 該槽位必須完整入鏡的 landmark（不能被原圖邊界切掉）
NEED = {
    'FACE_SHAPE_AND_JAW': {'左顴弓': 234, '右顴弓': 454, '左顎角': 172,
                           '右顎角': 397, '頦下': 152},
    'EYES_AND_BROWS': {'左外眥': 33, '左內眥': 133, '右內眥': 362,
                       '右外眥': 263, '左眉': 105, '右眉': 334},
    'NOSE': {'鼻根': 168, '鼻尖': 1, '左鼻翼': 98, '右鼻翼': 327},
    'MOUTH': {'左口角': 61, '右口角': 291, '上唇': 0, '下唇': 17},
}


def grade(px):
    if px >= 96:
        return 'A'
    if px >= 48:
        return 'B'
    return 'C'


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    refs = [f'ref_{n:02d}' for n in range(1, 16)]
    table, cards = {}, {}
    for rid in refs:
        hits = [f for f in os.listdir(REFDIR) if f.startswith(rid + '.')]
        if not hits:
            print(f'  {rid} 檔案不存在'); continue
        src = os.path.join(REFDIR, hits[0])
        P, size = landmarks(src)
        if P is None:
            table[rid] = {s: {'verdict': 'no_face'} for s in SLOTS}
            print(f'  {rid} 偵測不到臉'); continue
        W, H = size
        fl, fr, tip = P[234][0], P[454][0], P[1][0]
        facew = fr - fl
        yaw = abs(abs(tip - fl) - abs(fr - tip)) / facew if facew else 9.0
        for slot in SLOTS:
            s = SPEC['slots'][slot]
            box = compute_box(slot, P, size)
            x0, y0, x1, y1 = box
            bw, bh = x1 - x0, y1 - y0
            px = min(bw, bh)
            inter = max(0, min(x1, W) - max(x0, 0)) * max(0, min(y1, H) - max(y0, 0))
            pad = 1 - inter / (bw * bh) if bw * bh else 1.0
            cut = [n for n, i in NEED[slot].items()
                   if not (0 <= P[i][0] < W and 0 <= P[i][1] < H)]
            g = grade(px)
            fails = []
            if yaw > YAW_MAX[slot]:
                fails.append(f'正面度 {yaw:.3f} 超過本槽上限 {YAW_MAX[slot]}')
            if cut:
                fails.append('原圖切掉了 ' + '、'.join(cut))
            if g == 'C':
                fails.append(f'部件只有 {px:.0f}px，C 級（<48px）不可直接用')
            if pad > 0.30:
                fails.append(f'裁切框有 {pad:.0%} 落在畫面外')
            if not fails:
                verdict = 'ready' if g == 'A' else 'probe'
            else:
                verdict = 'reject'
            # 不論過不過都把圖裁出來，要看得見才排得了表
            out = f'{OUT_DIR}/{rid}__{slot}.jpg'
            try:
                img = crop_and_pad(src, box,
                                   tuple(s['out']), tuple(SPEC.get('padding_rgb', SPEC['qa'].get('padding_rgb', [128,128,128]))),
                                   s.get('aspect_mode', 'expand'))
                img.save(out, quality=92)
            except Exception as e:
                out = None
                fails.append(f'裁切失敗：{e}')
                verdict = 'reject'
            table.setdefault(rid, {})[slot] = {
                'verdict': verdict, 'grade': g, 'part_px': round(px, 1),
                'yaw': round(yaw, 4), 'yaw_max': YAW_MAX[slot],
                'padding_ratio': round(pad, 4), 'cut_off': cut,
                'reasons': fails, 'card': out}
            cards[(rid, slot)] = out

    json.dump({'_spec': 'donor_slot_table/v1（依 R10 P-01 的分級門檻）',
               '_yaw_max': YAW_MAX,
               '_grade': {'A': '≥96px 可直接用', 'B': '48–95px 需 probe',
                          'C': '<48px 不可直接用'},
               '_verdict': {'ready': '可直接入池', 'probe': '需先做 1 張 probe',
                            'reject': '本槽不可用'},
               'refs': table},
              open('pilot/donor_slot_table.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    # 統計
    cnt = {'ready': 0, 'probe': 0, 'reject': 0}
    print(f"\n{'ref':8s}" + ''.join(f'{SLZH[s]:>18s}' for s in SLOTS))
    for rid in refs:
        if rid not in table: continue
        line = f'{rid:8s}'
        for s in SLOTS:
            c = table[rid][s]
            v = c.get('verdict', '?')
            cnt[v] = cnt.get(v, 0) + 1
            mark = {'ready': '✓', 'probe': '△', 'reject': '✗'}.get(v, '?')
            cell = f"{mark} {c.get('grade', '-')} {c.get('part_px', 0):.0f}px"
            line += f'{cell:>18s}'
        print(line)
    print(f"\n✓ 可直接入池 {cnt['ready']}　△ 需 probe {cnt['probe']}　✗ 不可用 {cnt['reject']}　（共 60 格）")
    for s in SLOTS:
        r = [rid for rid in table if table[rid][s]['verdict'] == 'ready']
        p = [rid for rid in table if table[rid][s]['verdict'] == 'probe']
        print(f'  {SLZH[s]:6s} 可直接用 {len(r)} 張：{", ".join(r) if r else "—"}')
        print(f'  {"":6s} 需 probe {len(p)} 張：{", ".join(p) if p else "—"}')
    print('\n→ pilot/donor_slot_table.json、review/donor_cards/')


if __name__ == '__main__':
    main()
