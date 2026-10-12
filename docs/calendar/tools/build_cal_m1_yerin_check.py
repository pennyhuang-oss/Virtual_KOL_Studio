#!/usr/bin/env python3
"""TASK-CAL-001 第二階段｜Yerin casting_v1 a01–a04 與定案臉的並排比較板（供主管覆核，不發布到素材頁）。

來源一律從固定 commit（FIXED）讀取並核對 git blob。只做裁切、等比縮放與遮罩（臉部輪廓外塗灰，用來排除髮型、
髮色與服裝的影響）；不旋轉、不變形、不修臉。臉部關鍵點用 mediapipe FaceLandmarker（docs/calendar/tools/cal_face_lib.py）。
全身照臉太小時，先在頭部區域裁切並放大 3 倍偵測，座標再換算回原圖（只影響找臉，不改輸出像素的處理方式）。

輸出：review/calendar/yerin_face_check/CAL_M1_yerin_casting_v1_vs_canon.jpg、sources.json
用法：python3 docs/calendar/tools/build_cal_m1_yerin_check.py
"""
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cal_face_lib as F  # noqa: E402

FIXED = '4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45'
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
OUT = os.path.join(ROOT, 'review', 'calendar', 'yerin_face_check')
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
K = 'kols/yerin-han/'

# (列名, casting 檔, 對照的定案訓練圖, casting 找臉用的頭部區域[比例]或 None, 對照圖的頭部區域或 None)
# 人寫觀察放在 review/calendar/yerin_face_check/observations.json
ROWS = [
    ('a01', 'images/casting_v1/a01.png', 'images/training_v1/train_03.jpg', None, None),
    ('a02', 'images/casting_v1/a02.png', 'images/training_v1/train_02.jpg', None, None),
    ('a03', 'images/casting_v1/a03.png', 'images/training_v1/train_01.jpg', None, None),
    ('a04', 'images/casting_v1/a04.png', 'images/training_v1/train_03.jpg', (0.3, 0.0, 0.75, 0.35), None),
]
MASTER = 'identity/identity_master.jpg'


def show(rel):
    b = subprocess.check_output(['git', '-C', ROOT, 'show', f'{FIXED}:{rel}'])
    blob = subprocess.check_output(['git', '-C', ROOT, 'rev-parse', f'{FIXED}:{rel}'], text=True).strip()
    assert hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest() == blob, rel
    return b, blob


def geometry(path, head_box):
    if head_box is None:
        return F.geometry(path)
    im = Image.open(path).convert('RGB')
    W, H = im.size
    b = (int(head_box[0] * W), int(head_box[1] * H), int(head_box[2] * W), int(head_box[3] * H))
    k = 3
    sub = im.crop(b).resize(((b[2] - b[0]) * k, (b[3] - b[1]) * k), Image.LANCZOS)
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as t:
        sub.save(t.name)
    g = F.geometry(t.name)
    os.unlink(t.name)
    if g is None:
        return None
    off = np.array([b[0], b[1]], dtype=float)
    g['P'] = g['P'] / k + off
    g['mid'] = g['mid'] / k + off
    g['iod'] /= k
    g['faceh'] /= k
    return g


def panel(rel, head_box, tmpdir, tag):
    data, blob = show(K + rel)
    src = os.path.join(tmpdir, tag + os.path.splitext(rel)[1])
    open(src, 'wb').write(data)
    g = geometry(src, head_box)
    assert g is not None, rel
    full = Image.open(src).convert('RGB')
    full.thumbnail((300, 400), Image.LANCZOS)
    head = Image.open(F.head_crop(src, g, os.path.join(tmpdir, tag + '_h.jpg'), size=300))
    mask = Image.open(F.masked_face(src, g, os.path.join(tmpdir, tag + '_m.jpg'), w=250, h=300, iod_px=90))
    w0, h0 = Image.open(src).size
    meta = {'path': K + rel, 'git_blob': blob, 'sha256': hashlib.sha256(data).hexdigest(), 'px': [w0, h0],
            'yaw': round(g['yaw'], 2), 'roll_deg': round(g['roll'], 1), 'eye_dist_px': round(g['iod'], 1)}
    return [full, head, mask], meta


def main():
    notes = json.load(open(os.path.join(OUT, 'observations.json'), encoding='utf-8'))
    os.makedirs(OUT, exist_ok=True)
    f_t = ImageFont.truetype(FONT, 22)
    f_s = ImageFont.truetype(FONT, 16)
    rows, metas = [], {}
    with tempfile.TemporaryDirectory() as td:
        m_imgs, metas['identity_master'] = panel(MASTER, None, td, 'master')
        for name, cast, ref, hb_c, hb_r in ROWS:
            ci, cm = panel(cast, hb_c, td, name)
            ri, rm = panel(ref, hb_r, td, name + '_ref')
            metas[name] = {'casting': cm, 'reference': rm}
            rows.append((name, ci, ri, cm, rm))
    cellw, gap = 300, 8
    # 版面：標題 → 定案臉列 → 4 列（casting 3 格｜定案訓練圖 3 格）→ 觀察文字
    W = 6 * cellw + 7 * gap + 40
    blocks = []
    hdr = Image.new('RGB', (W, 150), 'white')
    d = ImageDraw.Draw(hdr)
    d.text((20, 14), 'Yerin Han｜casting_v1 a01–a04 與定案臉並排（主管覆核用；只裁切、縮放與臉部輪廓外塗灰，不改臉）', fill='black', font=f_t)
    d.text((20, 50), f'來源：固定 commit {FIXED}。每列左 3 格＝casting_v1（全圖｜頭部裁切｜只留臉部輪廓、兩眼距離統一 90 px）；', fill='#333', font=f_s)
    d.text((20, 74), '右 3 格＝定案 Soul 訓練集 training_v1 中姿勢最接近的一張（同樣三種裁切）。最上列是 2026-09-01 核准的 identity master。', fill='#333', font=f_s)
    d.text((20, 98), '只留臉部輪廓的那一格把頭髮、髮色、服裝都遮掉——Soul V2 不繼承髮型，所以髮色不同不算錯臉證據。', fill='#333', font=f_s)
    d.text((20, 122), '本板是目視證據，不是量測；結論由主管覆核。四張在覆核前維持「暫不採用」。', fill='#8a3b00', font=f_s)
    blocks.append(hdr)

    def row_img(label, left, right, meta_l, meta_r, obs):
        h = 400 + 34 + 26 * (len(obs) + 1) + 10
        im = Image.new('RGB', (W, h), 'white')
        d = ImageDraw.Draw(im)
        x = 20
        for i, p in enumerate(left + (right or [])):
            if i == 3:
                x += 20
            im.paste(p, (x + (cellw - p.width) // 2, 34 + (400 - p.height) // 2 if i % 3 == 0 else 34))
            x += cellw + gap
        d.text((20, 6), label, fill='black', font=f_t)
        y = 34 + 400 + 6
        def desc(m):
            return f"{m['path'].split('/images/')[-1].split('/identity/')[-1]}（{m['px'][0]}×{m['px'][1]}；臉部偏轉 yaw {m['yaw']}，傾斜 {m['roll_deg']}°）"
        line = f'左：{desc(meta_l)}' + (f'　右：{desc(meta_r)}' if meta_r else '')
        d.text((20, y), line, fill='#555', font=f_s)
        for j, o in enumerate(obs):
            d.text((20, y + 26 * (j + 1)), '・' + o, fill='black', font=f_s)
        return im

    blocks.append(row_img('定案臉：identity master（2026-09-01 核准）', m_imgs, None, metas['identity_master'], None,
                          notes['identity_master']))
    for name, ci, ri, cm, rm in rows:
        blocks.append(row_img(f'{name}（casting_v1）｜對照 {rm["path"].split("/")[-1]}', ci, ri, cm, rm, notes[name]))
    foot = Image.new('RGB', (W, 26 * (len(notes['summary']) + 1) + 20), 'white')
    d = ImageDraw.Draw(foot)
    d.text((20, 6), '小結（待主管覆核）', fill='black', font=f_t)
    for j, o in enumerate(notes['summary']):
        d.text((20, 36 + 26 * j), '・' + o, fill='black', font=f_s)
    blocks.append(foot)
    H = sum(b.height for b in blocks) + 4 * len(blocks)
    board = Image.new('RGB', (W, H), '#dddddd')
    y = 0
    for b in blocks:
        board.paste(b, (0, y))
        y += b.height + 4
    out = os.path.join(OUT, 'CAL_M1_yerin_casting_v1_vs_canon.jpg')
    board.save(out, quality=90, optimize=True)
    json.dump({'generated_by': 'docs/calendar/tools/build_cal_m1_yerin_check.py', 'fixed_sha': FIXED,
               'ops': '裁切、等比縮放、臉部輪廓外塗灰（cal_face_lib.head_crop／masked_face）；不旋轉、不變形、不修臉',
               'board': os.path.relpath(out, ROOT), 'board_sha256': hashlib.sha256(open(out, 'rb').read()).hexdigest(),
               'sources': metas}, open(os.path.join(OUT, 'sources.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(out, board.size)


if __name__ == '__main__':
    main()
