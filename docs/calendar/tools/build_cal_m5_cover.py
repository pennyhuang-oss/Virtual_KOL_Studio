"""TASK-CAL-001 M-5 R27：12 人團體封面 4 張候選的本機排版（照片本身不含文字，「2027」由本機排上去）。

- 輸入：4 張生成原圖（私有、含平台任務識別中繼資料，不進 git；用 --raw-dir 指定，sha256 必須與紀錄相同）、
  review/calendar/m5_r27 的身分參考圖與臉框（face_boxes.json）。
- 版面：照片等比縮放到含出血畫布的高度、左右置中裁掉多餘寬度（不放大、不調色、不修圖）；
  標題「2027」＋小字「DESK CALENDAR」置中，放在線圈假設區（上緣 12 mm）以下、人物頭頂以上。
  沒有提供品牌名稱，所以不放品牌、Logo 或佔位字。字型為開放授權的 Inter（預覽用，正式字型未定）。
- 自動檢查：標題在文字安全區內、不碰線圈假設區；標題框（外擴 2 mm）不碰任何人的頭部範圍；
  標題底下只有牆面（像素與牆面中位色差異大的比例）；每張臉離裁切線至少 3 mm、不在線圈區。
- 輸出（docs/calendar/decision_site/public/cover/，皆不帶中繼資料）：
  cover_{id}_v.jpg（150 dpi 顯示版）、cover_{id}_f.jpg（300 dpi）、photo_{id}.jpg（原生像素、無文字）、ids_{id}.jpg（逐人臉部對照）；
  資料寫到 docs/calendar/data/cal_m5_cover_r27.json。
用法：python3 -I docs/calendar/tools/build_cal_m5_cover.py --raw-dir DIR [--check]
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
ROUND = 'M-5 R27'
PUB_REL = 'docs/calendar/decision_site/public/cover'
DATA_REL = 'docs/calendar/data/cal_m5_cover_r27.json'
TRIAL_REL = 'docs/calendar/data/cal_m5_r27_trial.json'
R27 = 'review/calendar/m5_r27'
DPI = 300
VIEW_DPI = 150
COVERS = ('H-A', 'H-B', 'V-A', 'V-B')
# 4 張原圖（M-5 R27 生成、各 1 次請求）：檔名 cover_{id}.png 的 sha256
SRC_SHA = {
    'H-A': '278ce0954d3a5527c418a25de527a0cb82fe9f5e958ea27eede2c9ce38aae6f5',
    'H-B': '7f4e118566c9d5a6df5c03e712d89572bd8506af7f2f2d00b459343b2a668f16',
    'V-A': '960a23ab3acacd7c569d4f3dcb0ab1f6e965789debc63d07dd2ecc1003aecd1f',
    'V-B': 'd3da281b41bfe00be55bbe8961580da23bb4af1b5b48d155f6fde93c0bc558e3',
}
FONT_DIR = '/usr/share/fonts/opentype/inter'
FONTS = {'title': 'InterDisplay-Light.otf', 'sub': 'Inter-Medium.otf', 'label': 'Inter-Medium.otf'}
CJK_FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'   # 只用在臉部對照圖的小字標籤
FONT_NOTE ='預覽用字型：Inter Display Light（2027）／Inter Medium（DESK CALENDAR），開放授權（SIL OFL）；正式字型未定。'
INK = (52, 44, 40)
# 畫布（含 2 mm 出血，mm，左上為原點）；與 R26 排版預覽相同的幾何
FMT = {
    'H': {'zh': '橫式', 'W': 204, 'H': 155, 'trim': 2, 'coil_assumed': 12, 'safe': (4, 12, 200, 151), 'safe_label': '廠商安全框',
          'title_cap_mm': 14.0, 'title_top_mm': 15.0, 'sub_cap_mm': 2.2, 'gap_mm': 3.0},
    'V': {'zh': '直式', 'W': 144, 'H': 204, 'trim': 2, 'coil_assumed': 12, 'safe': (5, 12, 139, 199), 'safe_label': '文字安全區（本案自訂）',
          'title_cap_mm': 21.0, 'title_top_mm': 17.0, 'sub_cap_mm': 2.6, 'gap_mm': 4.0},
}
SUB = 'DESK CALENDAR'
SUB_TRACK = 0.42   # 字距（em）
HEAD_UP, HEAD_SIDE = 0.9, 0.35   # 頭部範圍：臉框往上加 0.9 倍臉高（頭髮）、左右各加 0.35 倍臉寬
CLEAR_MM = 2.0
FACE_EDGE_MM = 3.0
WALL_DIFF = 40      # 與牆面中位色的 RGB 距離超過此值算「不是牆」
WALL_MAX = 0.01     # 標題框內「不是牆」的像素比例上限


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def jpeg(im, q, sub=2):
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=q, subsampling=sub, optimize=False)
    return b.getvalue()


def font(k, px):
    return ImageFont.truetype(os.path.join(FONT_DIR, FONTS[k]), px)


def px(mm):
    return mm * DPI / 25.4


def load_raw(raw_dir, c):
    p = os.path.join(raw_dir, f'cover_{c}.png')
    b = open(p, 'rb').read()
    assert sha256(b) == SRC_SHA[c], f'{c}：原圖 sha256 與紀錄不同'
    im = Image.open(io.BytesIO(b))
    im.load()
    return im.convert('RGB')   # 只取像素，丟掉所有中繼資料


def geometry(k, size):
    """原圖等比縮放到畫布高度、左右置中裁切。回傳：畫布像素大小、縮放後寬、左側裁掉的像素、原圖→畫布 mm 的比例。"""
    f = FMT[k]
    W, H = size
    cw, ch = round(px(f['W'])), round(px(f['H']))
    sw = round(W * ch / H)
    assert sw >= cw, '只裁左右，不放大'
    off = (sw - cw) // 2
    mm_per_src = f['H'] / H
    crop_lr_mm = (W * mm_per_src - f['W']) / 2
    return {'canvas_px': [cw, ch], 'scaled_w': sw, 'off_px': off, 'mm_per_src': mm_per_src, 'crop_lr_mm': round(crop_lr_mm, 2),
            'eff_ppi': round(H / (f['H'] / 25.4))}


def to_mm(k, g, box):
    f = FMT[k]
    s = g['mm_per_src']
    dx = g['crop_lr_mm']
    return [box[0] * s - dx, box[1] * s, box[2] * s - dx, box[3] * s]


def title_layout(k):
    """標題各行的位置（mm）與墨跡框；字級由數字的實際墨跡高度決定。"""
    f = FMT[k]
    probe = font('title', 1000)
    b = probe.getbbox('2027', anchor='ls')
    em_title = f['title_cap_mm'] / ((b[3] - b[1]) / 1000)
    sp = font('sub', 1000)
    sb = sp.getbbox('H', anchor='ls')
    em_sub = f['sub_cap_mm'] / ((sb[3] - sb[1]) / 1000)
    cx = f['W'] / 2
    # 2027：墨跡上緣對齊 title_top
    tb = [v / 1000 * em_title for v in b]
    t_base = f['title_top_mm'] - tb[1]
    t_box = [cx - (tb[2] - tb[0]) / 2, f['title_top_mm'], cx + (tb[2] - tb[0]) / 2, t_base + tb[3]]
    # DESK CALENDAR：逐字排、加字距，置中
    adv = [sp.getlength(ch) / 1000 * em_sub for ch in SUB]
    total = sum(adv) + SUB_TRACK * em_sub * (len(SUB) - 1)
    s_top = t_box[3] + f['gap_mm']
    s_base = s_top + f['sub_cap_mm']
    s_box = [cx - total / 2, s_top, cx + total / 2, s_base]
    return {'em_title_mm': round(em_title, 3), 'em_sub_mm': round(em_sub, 3), 'title': {'text': '2027', 'x_ink_left': t_box[0] - tb[0], 'base': t_base, 'box': t_box},
            'sub': {'text': SUB, 'x0': s_box[0], 'base': s_base, 'box': s_box, 'adv': adv},
            'box': [min(t_box[0], s_box[0]), t_box[1], max(t_box[2], s_box[2]), s_box[3]]}


def draw_title(page, k, T):
    d = ImageDraw.Draw(page)
    ft = font('title', round(px(T['em_title_mm'])))
    d.text((px(T['title']['x_ink_left']), px(T['title']['base'])), '2027', font=ft, fill=INK, anchor='ls')
    fs = font('sub', round(px(T['em_sub_mm'])))
    x = T['sub']['x0']
    for ch, a in zip(SUB, T['sub']['adv']):
        d.text((px(x), px(T['sub']['base'])), ch, font=fs, fill=INK, anchor='ls')
        x += a + SUB_TRACK * T['em_sub_mm']


def wall_ratio(page, box_mm):
    a = np.asarray(page.crop(tuple(round(px(v)) for v in box_mm))).reshape(-1, 3).astype(np.int32)
    med = np.median(a, axis=0)
    return float((np.sqrt(((a - med) ** 2).sum(1)) > WALL_DIFF).mean())


def inter(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def build_cover(c, raw, F, refs, out_dir):
    k = c[0]
    f = FMT[k]
    g = geometry(k, raw.size)
    cw, ch = g['canvas_px']
    page = raw.resize((g['scaled_w'], ch), Image.LANCZOS).crop((g['off_px'], 0, g['off_px'] + cw, ch))
    T = title_layout(k)
    wall = wall_ratio(page, [T['box'][0] - 1, T['box'][1] - 1, T['box'][2] + 1, T['box'][3] + 1])
    people = F['covers'][c]['people']
    heads, faces, issues = {}, {}, []
    for pid, v in people.items():
        x0, y0, x1, y1 = v['face']
        w, h = x1 - x0, y1 - y0
        heads[pid] = to_mm(k, g, [x0 - HEAD_SIDE * w, y0 - HEAD_UP * h, x1 + HEAD_SIDE * w, y1])
        faces[pid] = to_mm(k, g, v['face'])
    tb = T['box']
    tbx = [tb[0] - CLEAR_MM, tb[1] - CLEAR_MM, tb[2] + CLEAR_MM, tb[3] + CLEAR_MM]
    s = f['safe']
    if not (tb[0] >= s[0] and tb[2] <= s[2] and tb[1] >= max(s[1], f['coil_assumed'] + 2)):
        issues.append('標題超出文字安全區或太靠近線圈區')
    hit = [pid for pid, hb in heads.items() if inter(tbx, hb)]
    if hit:
        issues.append(f'標題碰到頭部範圍：{hit}')
    if wall > WALL_MAX:
        issues.append(f'標題底下不只是牆面（{wall:.3f}）')
    t = f['trim']
    near = [pid for pid, fb in faces.items() if fb[0] < t + FACE_EDGE_MM or fb[2] > f['W'] - t - FACE_EDGE_MM or fb[1] < f['coil_assumed'] or fb[3] > f['H'] - t - FACE_EDGE_MM]
    if near:
        issues.append(f'臉太靠近裁切線或在線圈區：{near}')
    head_top = min(hb[1] for hb in heads.values())
    under = [hb for hb in heads.values() if hb[0] < tb[2] and hb[2] > tb[0]]
    clear_mm = round(min(hb[1] for hb in under) - tb[3], 1) if under else None
    draw_title(page, k, T)
    # 輸出
    files = {}

    def save(name, data):
        open(os.path.join(out_dir, name), 'wb').write(data)
        files[name] = sha256(data)
    save(f'cover_{c}_f.jpg', jpeg(page, 90))
    view = page.resize((round(cw * VIEW_DPI / DPI), round(ch * VIEW_DPI / DPI)), Image.LANCZOS)
    save(f'cover_{c}_v.jpg', jpeg(view, 88))
    save(f'photo_{c}.jpg', jpeg(raw, 90))
    save(f'ids_{c}.jpg', jpeg(id_sheet(c, raw, F, refs), 88))
    fh = sorted(round(fb[3] - fb[1], 1) for fb in faces.values())
    return {'id': c, 'kind': k, 'direction': c[2], 'src_px': list(raw.size), 'geometry': g, 'title_box_mm': [round(v, 2) for v in tb],
            'title_to_nearest_head_mm': clear_mm, 'highest_head_top_mm': round(head_top, 1), 'wall_ratio': round(wall, 4),
            'face_h_mm': {'min': fh[0], 'median': fh[len(fh) // 2], 'max': fh[-1]},
            'faces_mm': {pid: [round(v, 1) for v in fb] for pid, fb in faces.items()}, 'issues': issues, 'files': files}


def id_sheet(c, raw, F, refs):
    """逐人臉部對照：左＝送入的身分參考臉、右＝封面上的臉（只裁切與等比縮放），標名字。"""
    T, cols, lab, gap = 220, 4, 34, 14
    rows = (len(refs) + cols - 1) // cols
    W = cols * (2 * T + 2) + (cols - 1) * gap
    S = Image.new('RGB', (W, rows * (T + lab) + (rows - 1) * gap), (255, 255, 255))
    d = ImageDraw.Draw(S)
    ft = font('label', 19)
    for i, r in enumerate(refs):
        x, y = (i % cols) * (2 * T + 2 + gap), (i // cols) * (T + lab + gap)
        a = Image.open(os.path.join(ROOT, r['file'])).convert('RGB').crop(tuple(F['refs'][r['set']])).resize((T, T), Image.LANCZOS)
        b = raw.crop(tuple(F['covers'][c]['people'][r['set']]['crop'])).resize((T, T), Image.LANCZOS)
        S.paste(a, (x, y + lab))
        S.paste(b, (x + T + 2, y + lab))
        d.text((x + 2, y + lab - 8), f"{r['image_no']}  {r['name']}", font=ft, fill=(34, 34, 38), anchor='ls')
        d.text((x + 2 * T + 2, y + lab - 8), '左 參考｜右 封面', font=ImageFont.truetype(CJK_FONT, 15), fill=(110, 110, 114), anchor='rs')
    return S


def build(raw_dir, pub, data_path):
    if os.path.isdir(pub):
        shutil.rmtree(pub)
    os.makedirs(pub)
    F = json.load(open(os.path.join(ROOT, R27, 'face_boxes.json'), encoding='utf-8'))
    refs = json.load(open(os.path.join(ROOT, R27, 'refs.json'), encoding='utf-8'))['refs']
    for r in refs:
        assert sha256(open(os.path.join(ROOT, r['file']), 'rb').read()) == r['sha256'], r['file']
    trial = json.load(open(os.path.join(ROOT, TRIAL_REL), encoding='utf-8'))
    out = []
    for c in COVERS:
        raw = load_raw(raw_dir, c)
        out.append(build_cover(c, raw, F, refs, pub))
    files = []
    for cv in out:
        for name, h in sorted(cv['files'].items()):
            im = Image.open(os.path.join(pub, name))
            files.append({'path': name, 'sha256': h, 'px': [im.width, im.height], 'bytes': os.path.getsize(os.path.join(pub, name))})
    D = {
        'round': ROUND,
        'note': '12 人團體封面 4 張候選的本機排版（由 docs/calendar/tools/build_cal_m5_cover.py 產生）。照片不含文字；「2027」與 DESK CALENDAR 由本機排上去。未提供品牌名稱，不放品牌或 Logo。這是候選預覽，不是 Owner 接受、也不是交印核准。',
        'source_sha256': SRC_SHA,
        'fonts': FONT_NOTE,
        'formats': {k: {x: FMT[k][x] for x in ('zh', 'W', 'H', 'trim', 'coil_assumed', 'safe', 'safe_label')} | {'trim_mm': [FMT[k]['W'] - 4, FMT[k]['H'] - 4]} for k in 'HV'},
        'rules': {'head_range': f'臉框往上加 {HEAD_UP} 倍臉高、左右各加 {HEAD_SIDE} 倍臉寬', 'title_clearance_mm': CLEAR_MM, 'face_edge_mm': FACE_EDGE_MM,
                  'wall_check': f'標題框內與牆面中位色 RGB 距離 > {WALL_DIFF} 的像素比例 ≤ {WALL_MAX}', 'coil_margin_mm': 2},
        'fit': '照片等比縮放到含出血畫布高度、左右置中裁切；不放大、不調色、不修圖',
        'covers': out,
        'files': files,
        'identity_verdict': {c: trial['covers'][c]['verdict'] for c in COVERS},
    }
    assert all(not cv['issues'] for cv in out), [(cv['id'], cv['issues']) for cv in out]
    with open(data_path, 'w', encoding='utf-8') as fh:
        json.dump(D, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    return D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw-dir', required=True)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.check:
        old = json.load(open(os.path.join(ROOT, DATA_REL), encoding='utf-8'))
        with tempfile.TemporaryDirectory() as tmp:
            D = build(a.raw_dir, os.path.join(tmp, 'cover'), os.path.join(tmp, 'data.json'))
            same = json.loads(json.dumps(D, ensure_ascii=False)) == old
            pub = os.path.join(ROOT, PUB_REL)
            have = sorted(os.listdir(pub))
            diff = [x['path'] for x in D['files'] if not os.path.exists(os.path.join(pub, x['path'])) or sha256(open(os.path.join(pub, x['path']), 'rb').read()) != x['sha256']]
            extra = sorted(set(have) - {x['path'] for x in D['files']})
        ok = same and not diff and not extra
        print(json.dumps({'check': 'PASS' if ok else 'FAIL', 'data_same': same, 'files': len(D['files']), 'diff': diff, 'extra': extra}, ensure_ascii=False))
        sys.exit(0 if ok else 1)
    D = build(a.raw_dir, os.path.join(ROOT, PUB_REL), os.path.join(ROOT, DATA_REL))
    for cv in D['covers']:
        print(cv['id'], cv['geometry']['canvas_px'], 'ppi', cv['geometry']['eff_ppi'], 'crop', cv['geometry']['crop_lr_mm'], 'title', cv['title_box_mm'],
              'clear', cv['title_to_nearest_head_mm'], 'wall', cv['wall_ratio'], 'face', cv['face_h_mm'])
    print('files', len(D['files']), round(sum(x['bytes'] for x in D['files']) / 1048576, 1), 'MB')


if __name__ == '__main__':
    main()
