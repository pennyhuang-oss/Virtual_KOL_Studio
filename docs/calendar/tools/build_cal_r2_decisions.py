#!/usr/bin/env python3
"""TASK-CAL-001 / R2 — Owner 決策板用的圖片（每張 < 1 MB）。

1) 人選與具體照片：每月一列＝R2 建議的橫式圖、直式圖、替代圖（只做縮圖，不修圖）
2) 尺度：同一個人（Iris、Kanon）的實際既有照片並排
用法：python3 docs/calendar/tools/build_cal_r2_decisions.py --hf-dir <取回原圖的資料夾>
"""
import argparse
import json
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
OUT = os.path.join(CAL, 'r2', 'decisions')
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'

MONTHS = [  # (月, 人設, 標籤, [(cid, 用途標籤)])
    (1, 'iris-chen', 'Iris', [('iris_H', 'H 建議'), ('iris_V', 'V 建議')]),
    (2, 'kanon-komori', 'Kanon', [('kanon_H', 'H 建議・女僕'), ('kanon_V', 'V 建議・女僕'), ('kanon_alt028', '替代・非女僕'), ('kanon_alt112', '替代・非女僕'), ('kanon_alt_t03', '替代・非女僕（repo）')]),
    (3, 'luna-tanaka', 'Luna', [('luna_H', 'H 建議（換圖）'), ('luna_V', 'V 建議（換圖）')]),
    (4, 'angel-chiu', 'Angel', [('angel_H', 'H 建議・護理師'), ('angel_V', 'V 建議'), ('angel_alt004', '替代・外景')]),
    (5, 'somi-oh', 'Somi', [('somi_H', 'H 建議'), ('somi_V', 'V 建議（換圖）'), ('somi_alt065', '替代・海邊')]),
    (6, 'vicky-lin', 'Vicky', [('vicky_H', 'H 建議（換圖）'), ('vicky_V', 'V 建議')]),
    (7, 'coco-wu', 'Coco', [('coco_H', 'H 建議（需修人像牆）'), ('coco_alt01', 'V 建議（需修手機殼）')]),
    (8, 'mia-huang', 'Mia', [('mia_H', 'H 建議'), ('mia_V', 'V 建議')]),
    (9, 'yuna-kim', 'Yuna', [('yuna_H', 'H 建議'), ('yuna_V', 'V 建議（換圖）'), ('yuna_altsoft', '柔和替代（小框）')]),
    (10, 'tammy-chou', 'Tammy', [('tammy_H', 'H 建議・倉庫坐箱'), ('tammy_V', 'V 建議・頂樓'), ('tammy_alt075', '替代・頂樓')]),
    (11, 'rin-ayase', 'Rin', [('rin_H', 'H 建議'), ('rin_V', 'V 建議・柔和'), ('rin_altR1V', '替代・晨袍')]),
    (12, 'rainie-hsu', 'Rainie', [('rainie_H', 'H 建議（需修日期戳）'), ('rainie_V', 'V 建議・柔和'), ('rainie_alt02', '替代・濃豔')]),
]
EXTRA = [('wanyin-jiang', 'Wanyin（備選）', ['wanyin_H', 'wanyin_V']), ('sophia-tseng', 'Sophia（備選）', ['sophia_H', 'sophia_V']),
         ('ananya-kapoor', 'Ananya（比較）', ['ananya_1', 'ananya_2', 'ananya_3']), ('wendy-yeo', 'Wendy（比較）', ['wendy_1', 'wendy_2', 'wendy_3'])]
SCALE = [('Iris｜A 日常甜美', 'kols/iris-chen/images/training_v1/02_taipei_street_02.webp'),
         ('Iris｜B 微性感', 'kols/iris-chen/images/training_v1/06_cafe_window_02.webp'),
         ('Iris｜C 內衣（只作尺度參考）', 'kols/iris-chen/images/daily_sexy_night_v2_lingerie/02_mirror_burgundy_teddy_selfie.png'),
         ('Kanon｜非女僕・甜', 'cid:kanon_alt028'), ('Kanon｜女僕制服', 'cid:kanon_H'), ('Kanon｜女僕・胸口開口', 'cid:kanon_V')]


def font(n):
    return ImageFont.truetype(FONT, n)


def save(img, path, max_w=2000):
    img.thumbnail((max_w, max_w * 3))
    q = 86
    while True:
        img.save(path, quality=q)
        if os.path.getsize(path) < 1_000_000 or q <= 55:
            break
        q -= 5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hf-dir', required=True)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    J = {c['cid']: c for c in json.load(open(os.path.join(CAL, 'data', 'cal_r2_judgments.json')))['candidates']}
    R = json.load(open(os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')))['items']

    def path(src):
        if src.startswith('cid:'):
            src = J[src[4:]]['src']
        if src.startswith('hf:'):
            return os.path.join(a.hf_dir, next(r for r in R if r['job_id'] == src[3:])['local'])
        return os.path.join(ROOT, src)

    def thumb(src, label, h=420):
        im = Image.open(path(src)).convert('RGB')
        im.thumbnail((h, h))
        c = Image.new('RGB', (im.width, im.height + 34), 'white')
        c.paste(im, (0, 34))
        ImageDraw.Draw(c).text((3, 4), label, fill='black', font=font(20))
        return c

    def row(title, cells):
        h = max(c.height for c in cells)
        r = Image.new('RGB', (230 + sum(c.width + 10 for c in cells), h + 8), 'white')
        ImageDraw.Draw(r).text((10, 12), title, fill='#b00', font=font(26))
        x = 230
        for c in cells:
            r.paste(c, (x, 4))
            x += c.width + 10
        return r

    def sheet(rows, title, name):
        W = max(r.width for r in rows)
        S = Image.new('RGB', (W, sum(r.height + 8 for r in rows) + 56), '#d4d4d4')
        ImageDraw.Draw(S).text((10, 12), title, fill='black', font=font(28))
        y = 56
        for r in rows:
            S.paste(r, (0, y))
            y += r.height + 8
        save(S, os.path.join(OUT, name))

    rows = [row(f'{m} 月\n{lab}', [thumb(J[cid]['src'], tag) for cid, tag in items]) for m, pid, lab, items in MONTHS]
    for i in range(0, 12, 4):
        sheet(rows[i:i + 4], f'決策 1｜人選與具體照片（{i + 1}–{i + 4} 月）｜H＝橫式、V＝直式｜草稿，未拍板', f'CAL_R2_decide_people_{i // 4 + 1}.jpg')
    rows = [row(lab, [thumb(J[c]['src'], c) for c in cids]) for pid, lab, cids in EXTRA]
    sheet(rows[:2], '決策 1｜備選（不占月份）', 'CAL_R2_decide_people_backup.jpg')
    sheet(rows[2:], '決策 1｜比較用：Ananya、Wendy（R1 未入選，R2 補圖）', 'CAL_R2_decide_people_compare.jpg')
    cells = [thumb(src, lab, 460) for lab, src in SCALE]
    sheet([row('尺度', cells[:3]), row('造型', cells[3:])], '決策 2｜尺度與造型：同一個人的實際既有照片', 'CAL_R2_decide_scale.jpg')
    print('ok')


if __name__ == '__main__':
    main()
