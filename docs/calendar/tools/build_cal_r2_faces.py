#!/usr/bin/env python3
"""TASK-CAL-001 / R2 — 十二人辨識比較（A 完整頭像、B 遮髮遮衣遮背景的臉部比較）。

只做裁切、等比例縮放、遮罩；不旋轉、不變形、不修圖、不美顏、不生成。
輸入：docs/calendar/data/cal_r2_face_pairs.json
      repo 路徑直接讀；`hf:` 開頭的是 Higgsfield 既有生成紀錄，需先依 data/cal_r2_hf_retrieved.json
      的 job_id 取回到 --hf-dir（本機快取，不進 repo）。
輸出：docs/calendar/r2/faces/ 底下的單張衍生圖與總覽圖（每張 < 1 MB），以及 data/cal_r2_face_geometry.json

用法（repo 根目錄）：
  python3 docs/calendar/tools/build_cal_r2_faces.py --hf-dir <取回原圖的資料夾>
"""
import argparse
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from cal_face_lib import geometry, head_crop, masked_face  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
OUT = os.path.join(CAL, 'r2', 'faces')
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'


def font(n):
    return ImageFont.truetype(FONT, n)


def resolve(src, hf_dir, retrieved):
    if src.startswith('hf:'):
        jid = src[3:]
        x = next(r for r in retrieved if r['job_id'] == jid)
        return os.path.join(hf_dir, x['local'])
    return os.path.join(ROOT, src)


def tile_row(cells, label_w=0, bg='white'):
    W = label_w + sum(c.width + 8 for c in cells)
    H = max(c.height for c in cells)
    row = Image.new('RGB', (W, H), bg)
    x = label_w
    for c in cells:
        row.paste(c, (x, 0))
        x += c.width + 8
    return row


def labelled(path, top, bottom, w):
    im = Image.open(path).convert('RGB')
    im.thumbnail((w, w * 2))
    cell = Image.new('RGB', (im.width, im.height + 58), 'white')
    cell.paste(im, (0, 28))
    d = ImageDraw.Draw(cell)
    d.text((2, 2), top, fill='black', font=font(19))
    d.text((2, im.height + 31), bottom, fill='#444', font=font(15))
    return cell


def stack(rows, title, out, bg='#d0d0d0', max_w=2000):
    W = max(r.width for r in rows)
    H = sum(r.height + 10 for r in rows) + 56
    S = Image.new('RGB', (W, H), bg)
    ImageDraw.Draw(S).text((10, 12), title, fill='black', font=font(24))
    y = 56
    for r in rows:
        S.paste(r, (0, y))
        y += r.height + 10
    hi = out.replace('.jpg', '_hires.jpg')
    S.save(hi, quality=90)
    S.thumbnail((max_w, max_w * 3))
    q = 85
    while True:
        S.save(out, quality=q)
        if os.path.getsize(out) < 1_000_000 or q <= 60:
            break
        q -= 5
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hf-dir', required=True)
    a = ap.parse_args()
    spec = json.load(open(os.path.join(CAL, 'data', 'cal_r2_face_pairs.json')))
    retrieved = json.load(open(os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')))['items']
    for sub in ('heads', 'masked'):
        os.makedirs(os.path.join(OUT, sub), exist_ok=True)

    geo = {}
    for person in spec['people']:
        pid = person['id']
        geo[pid] = []
        for k, item in enumerate(person['images'], 1):
            p = resolve(item['src'], a.hf_dir, retrieved)
            g = geometry(p)
            if g is None:
                raise SystemExit(f'no face: {pid} {item["src"]}')
            h = os.path.join(OUT, 'heads', f'{pid}_{k}.jpg')
            m = os.path.join(OUT, 'masked', f'{pid}_{k}.jpg')
            head_crop(p, g, h)
            masked_face(p, g, m)
            geo[pid].append({'src': item['src'], 'tag': item['tag'], 'yaw_proxy': round(g['yaw'], 3),
                             'roll_deg': round(g['roll'], 1), 'eye_distance_px': round(g['iod'], 1),
                             'head': os.path.relpath(h, CAL), 'masked': os.path.relpath(m, CAL)})

    json.dump({'generated_by': 'docs/calendar/tools/build_cal_r2_faces.py',
               'yaw_proxy': '鼻尖相對兩眼中點的水平偏移 ÷ 眼距；0 為正臉。只用來挑角度相近的圖，不是辨識分數。',
               'people': geo}, open(os.path.join(CAL, 'data', 'cal_r2_face_geometry.json'), 'w'), ensure_ascii=False, indent=1)

    names = {p['id']: p['label'] for p in spec['people']}

    def cells(pid, kind, w):
        return [labelled(os.path.join(CAL, x[kind]), f"{names[pid]}（{x['tag']}）",
                         f"yaw {x['yaw_proxy']:+.2f}｜roll {x['roll_deg']:+.0f}°", w) for x in geo[pid]]

    leads = [p['id'] for p in spec['people'] if p['group'] == 'lead']
    extra = [p['id'] for p in spec['people'] if p['group'] == 'compare']
    for kind, title in (('head', 'A｜完整頭像（同尺寸，只裁切與等比縮放）'),
                        ('masked', 'B｜遮住頭髮、服裝、背景（臉部橢圓以外填灰；以眼距等比縮放，未旋轉）')):
        for part, ids in (('1', leads[:6]), ('2', leads[6:]), ('extra', extra)):
            rows = [tile_row(cells(ids[i], kind, 230) + (cells(ids[i + 1], kind, 230) if i + 1 < len(ids) else []))
                    for i in range(0, len(ids), 2)]
            stack(rows, f'{title}｜{part}', os.path.join(OUT, f'CAL_R2_faces_{"A" if kind == "head" else "B"}_{part}.jpg'))

    for key, ids, title in spec['focus']:
        rows = []
        for kind in ('masked', 'head'):
            for i in ids:
                cs = cells(i, kind, 300 if len(geo[i]) <= 4 else 230)
                rows += [tile_row(cs[j:j + 6]) for j in range(0, len(cs), 6)]
        stack(rows, title, os.path.join(OUT, f'CAL_R2_focus_{key}.jpg'))
    print('ok', sum(len(v) for v in geo.values()), 'faces')


if __name__ == '__main__':
    main()
