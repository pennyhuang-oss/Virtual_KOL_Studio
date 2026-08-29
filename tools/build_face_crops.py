#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""依 pilot/crop_spec.json 從參考圖 deterministic 產生部件裁切，並寫 manifest。

ChatGPT R5 J-02.5：由程式依 landmark ＋ 規則產生，人只做 QA，不手工裁 76 次。
唯一鍵是 (source_ref_id, slot, crop_spec_version)——同一來源同一槽只裁一次，跨 persona 重用。

用法：
    python3 tools/build_face_crops.py                # 只裁「目前分配真的用到」的組合
    python3 tools/build_face_crops.py --all          # 全部 ref × 全部 slot
    python3 tools/build_face_crops.py --only ref_11  # 指定來源
"""
import json, os, sys, hashlib, glob, subprocess
import numpy as np
from PIL import Image

TOOL_VERSION = 'build_face_crops/1.0'
SPEC = json.load(open('pilot/crop_spec.json', encoding='utf-8'))
V = SPEC['crop_spec_version']
REFDIR = 'review/batch3_face_refs'
OUTDIR = f'review/batch3_face_crops/{V}'
MANIFEST = 'pilot/face_crops_manifest.json'
SLOTS = list(SPEC['slots'])
_MODEL = os.path.expanduser('~/.cache/mediapipe/face_landmarker.task')


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def landmarks(path):
    """回傳 (N,2) 的像素座標，以及影像尺寸。"""
    import mediapipe as mp
    from mediapipe.tasks import python as mpp
    from mediapipe.tasks.python import vision
    if not hasattr(landmarks, '_lm'):
        landmarks._lm = vision.FaceLandmarker.create_from_options(
            vision.FaceLandmarkerOptions(
                base_options=mpp.BaseOptions(model_asset_path=_MODEL), num_faces=1))
    img = mp.Image.create_from_file(path)
    r = landmarks._lm.detect(img)
    if not r.face_landmarks:
        return None, (img.width, img.height)
    W, H = img.width, img.height
    pts = np.array([[l.x * W, l.y * H] for l in r.face_landmarks[0]], dtype=float)
    return pts, (W, H)


def fit_aspect(box, aspect):
    """把 box 擴張（絕不收縮、絕不拉伸）到指定長寬比，維持中心。只用於 expand 模式。"""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    aw, ah = aspect
    target = aw / ah
    if w / h < target:
        nw = h * target
        cx = (x0 + x1) / 2
        x0, x1 = cx - nw / 2, cx + nw / 2
    else:
        nh = w / target
        cy = (y0 + y1) / 2
        y0, y1 = cy - nh / 2, cy + nh / 2
    return [x0, y0, x1, y1]


def compute_box(slot, P, size):
    s = SPEC['slots'][slot]
    a = s['anchors']
    W, H = size
    if slot == 'FACE_SHAPE_AND_JAW':
        faceh = P[a['bottom']][1] - P[a['top']][1]
        facew = P[a['right']][0] - P[a['left']][0]
        y0 = P[a['top']][1] - s['margin_top_x_faceh'] * faceh
        y1 = P[a['bottom']][1] + s['margin_bottom_x_faceh'] * faceh
        cx = (P[a['left']][0] + P[a['right']][0]) / 2
        need = s['min_width_x_facew'] * facew
        box = [cx - need / 2, y0, cx + need / 2, y1]
    elif slot == 'EYES_AND_BROWS':
        bt = min(P[i][1] for i in a['brow_top'])
        lb = max(P[i][1] for i in a['lid_bottom'])
        eyeh = lb - bt
        xs = [P[i][0] for i in a['outer']]
        span = max(xs) - min(xs)
        box = [min(xs) - s['margin_h_x_eyespan'] * span,
               bt - s['margin_v_x_eyeh'] * eyeh,
               max(xs) + s['margin_h_x_eyespan'] * span,
               lb + s['margin_v_x_eyeh'] * eyeh]
    elif slot == 'NOSE':
        top, bot = P[a['top']][1], P[a['bottom']][1]
        noseh = bot - top
        ax = [P[i][0] for i in a['alar']]
        aw = max(ax) - min(ax)
        box = [min(ax) - s['margin_h_x_alarw'] * aw,
               top - s['margin_v_x_noseh'] * noseh,
               max(ax) + s['margin_h_x_alarw'] * aw,
               bot + s.get('margin_v_bottom_x_noseh', 0.0) * noseh]
    elif slot == 'MOUTH':
        top, bot = P[a['top']][1], P[a['bottom']][1]
        mh = bot - top
        cx = [P[i][0] for i in a['corners']]
        mw = max(cx) - min(cx)
        box = [min(cx) - s['margin_h_x_mouthw'] * mw,
               top - s.get('margin_v_top_x_mouthh', 0.0) * mh,
               max(cx) + s['margin_h_x_mouthw'] * mw,
               bot + s['margin_v_x_mouthh'] * mh]
    else:
        raise ValueError(slot)
    # expand＝擴張取景（臉型槽需要臉周圍的脈絡）；pad＝只裁部件、之後補灰邊到長寬比。
    if s.get('aspect_mode', 'expand') == 'expand':
        box = fit_aspect(box, s['aspect_w_h'])
    return box


def qa(slot, box, P, size):
    """回傳 (status, [reasons], metrics)。"""
    q = SPEC['qa']; W, H = size
    x0, y0, x1, y1 = box
    bw, bh = x1 - x0, y1 - y0
    inter = max(0, min(x1, W) - max(x0, 0)) * max(0, min(y1, H) - max(y0, 0))
    pad = 1 - inter / (bw * bh)
    # yaw proxy：鼻尖到左右臉緣的水平距離差 ÷ 臉寬
    fl, fr, tip = P[234][0], P[454][0], P[1][0]
    facew = fr - fl
    yaw = abs(abs(tip - fl) - abs(fr - tip)) / facew if facew else 9
    reasons = []
    if pad > q['max_padding_ratio']:
        reasons.append(f'padding 佔 {pad:.0%}，超過上限 {q["max_padding_ratio"]:.0%}（部位被原圖邊界截斷）')
    lim = q['max_yaw_proxy_eyes'] if slot == 'EYES_AND_BROWS' else q['max_yaw_proxy']
    if yaw > lim:
        reasons.append(f'yaw proxy {yaw:.3f} 超過 {lim}（{"雙眼裁切對正面性要求更嚴" if slot=="EYES_AND_BROWS" else "側身過多"}）')
    if min(bw, bh) < q['min_short_side_px']:
        reasons.append(f'原圖上該部位短邊只有 {min(bw,bh):.0f}px，低於 {q["min_short_side_px"]}px（放大只會得到糊圖）')
    inb = lambda i: x0 <= P[i][0] <= x1 and y0 <= P[i][1] <= y1
    if slot == 'EYES_AND_BROWS' and inb(1):
        reasons.append('框內夾帶鼻尖')
    if slot == 'MOUTH' and inb(1):
        reasons.append('框內夾帶鼻尖')
    if slot == 'NOSE' and (inb(33) or inb(263)):
        reasons.append('框內夾帶完整的眼睛')
    if slot == 'NOSE' and inb(0):
        reasons.append('框內夾帶上唇')
    return ('pass' if not reasons else 'fail'), reasons, {
        'padding_ratio': round(pad, 4), 'yaw_proxy': round(yaw, 4),
        'source_px_short_side': round(min(bw, bh), 1)}


def crop_and_pad(src, box, out_size, rgb, mode):
    """裁出 box（越界處補灰），再依 mode 產出目標尺寸。

    expand：box 已經是目標長寬比，直接縮放。
    pad：box 是真正的部件框，等比縮到能放進目標尺寸，再置中貼到灰畫布上。
         **絕不拉伸**，灰邊是為了長寬比，不是為了裁切。
    """
    im = Image.open(src).convert('RGB')
    x0, y0, x1, y1 = [int(round(v)) for v in box]
    part = Image.new('RGB', (max(1, x1 - x0), max(1, y1 - y0)), tuple(rgb))
    sx0, sy0 = max(0, x0), max(0, y0)
    sx1, sy1 = min(im.width, x1), min(im.height, y1)
    if sx1 > sx0 and sy1 > sy0:
        part.paste(im.crop((sx0, sy0, sx1, sy1)), (sx0 - x0, sy0 - y0))
    OW, OH = out_size
    if mode == 'expand':
        return part.resize((OW, OH), Image.LANCZOS)
    sc = min(OW / part.width, OH / part.height)
    nw, nh = max(1, int(round(part.width * sc))), max(1, int(round(part.height * sc)))
    canvas = Image.new('RGB', (OW, OH), tuple(rgb))
    canvas.paste(part.resize((nw, nh), Image.LANCZOS), ((OW - nw) // 2, (OH - nh) // 2))
    return canvas


def used_pairs():
    """目前分配真的用到的 (ref, slot)。"""
    D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
    out = set()
    for pid, d in D['personas'].items():
        r = d.get('refs_v2') or d['refs']
        for slot, ref in r.items():
            out.add((ref, slot))
    return sorted(out)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
    if '--all' in sys.argv:
        refs = sorted({os.path.basename(f).split('.')[0] for f in glob.glob(REFDIR + '/ref_*')})
        pairs = [(r, s) for r in refs for s in SLOTS]
    else:
        pairs = used_pairs()
    if only:
        pairs = [p for p in pairs if p[0] == only]

    man = {'crop_spec_version': V, 'tool_version': TOOL_VERSION,
           '_gate': 'prompt manifest 只能引用 qa_status == "pass" 的 crop。',
           'artifacts': {}}
    if os.path.exists(MANIFEST):
        old = json.load(open(MANIFEST, encoding='utf-8'))
        if old.get('crop_spec_version') == V:
            man['artifacts'] = old.get('artifacts', {})

    npass = nfail = 0
    cache = {}
    for ref, slot in pairs:
        hits = [f for f in os.listdir(REFDIR) if f.startswith(ref + '.')]
        if not hits:
            print(f'  ✗ {ref} 檔案不存在'); continue
        src = os.path.join(REFDIR, hits[0])
        if ref not in cache:
            cache[ref] = landmarks(src)
        P, size = cache[ref]
        if P is None:
            print(f'  ✗ {ref} 偵測不到臉'); continue
        box = compute_box(slot, P, size)
        status, reasons, metrics = qa(slot, box, P, size)
        key = f'{ref}__{slot}__{V}'
        outp = f'{OUTDIR}/{key}.jpg'
        mode = SPEC['slots'][slot].get('aspect_mode', 'expand')
        crop_and_pad(src, box, SPEC['slots'][slot]['out'], SPEC['padding_rgb'], mode).save(
            outp, quality=95, subsampling=0)
        man['artifacts'][key] = {
            'source_ref_id': ref, 'slot': slot, 'crop_spec_version': V,
            'source_path': src, 'source_sha256': sha256(src),
            'source_size': list(size),
            'normalized_crop_box': [round(box[0] / size[0], 6), round(box[1] / size[1], 6),
                                    round(box[2] / size[0], 6), round(box[3] / size[1], 6)],
            'pixel_crop_box': [round(v, 1) for v in box],
            'padding_rgb': SPEC['padding_rgb'],
            'aspect_mode': SPEC['slots'][slot].get('aspect_mode', 'expand'),
            'out_path': outp, 'out_size': SPEC['slots'][slot]['out'],
            'out_sha256': sha256(outp),
            'tool_version': TOOL_VERSION,
            'qa_status': status, 'qa_reasons': reasons, 'qa_metrics': metrics,
            'qa_by': 'auto',
        }
        npass += status == 'pass'; nfail += status == 'fail'
        if status == 'fail':
            print(f'  ✗ {key}: {"；".join(reasons)}')

    json.dump(man, open(MANIFEST, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'\n{len(pairs)} 個 unique (source, slot) 組合 → {OUTDIR}')
    print(f'  QA pass {npass}／fail {nfail}')
    print(f'  manifest → {MANIFEST}')


if __name__ == '__main__':
    main()
