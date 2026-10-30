"""M-5 R27：12 位封面身分參考。每位一張既有身分基準；identity_master 原樣使用（只轉 JPEG、去中繼資料），
其他來源只做頭肩裁切（不修圖、不放大），輸出到 review/calendar/m5_r27/refs/，並寫 refs.json（來源、裁切框、sha256）。"""
import hashlib
import io
import json
import os
import subprocess
import sys

from PIL import Image

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, os.path.join(ROOT, 'docs', 'calendar', 'tools'))
from cal_face_lib import landmarks  # noqa: E402

OUT = os.path.join(ROOT, 'review', 'calendar', 'm5_r27', 'refs')
# 順序＝送入模型的 Image 1–12（橫式月份順序）
REFS = [
    ('yuna-kim', 'Yuna Kim', 'kols/yuna-kim/images/face_reference/ref_01.webp', 'Soul 訓練用臉部參考（ref_01，正面）'),
    ('rin-ayase', 'Rin Ayase', 'kols/rin-ayase/identity/identity_master.jpg', 'identity_master（Penny 2026-09-01 核准）'),
    ('miu-shiraishi', 'Miu Shiraishi', 'kols/miu-shiraishi/identity/identity_master.jpg', 'identity_master（Penny 2026-09-01 核准）'),
    ('tammy-chou', 'Tammy Chou', 'kols/tammy-chou/identity/identity_master.jpg', 'identity_master（Penny 2026-09-01 核准）'),
    ('yerin-han', 'Yerin Han', 'kols/yerin-han/identity/identity_master.jpg', 'identity_master（Penny 2026-09-01 核准）'),
    ('coco-wu', 'Coco Wu', 'kols/coco-wu/images/face_reference/candidate_01.png', 'Reference Element 錨點原圖（coco-wu-anchor-c01；使用者核准送訓）'),
    ('mia-huang', 'Mia Huang', 'kols/mia-huang/images/face_reference/candidate_02.png', 'Reference Element 錨點原圖（使用者核准送訓）'),
    ('iris-chen', 'Iris Chen', 'kols/iris-chen/images/training_v1/05_cafe_window_01.webp', 'Soul 訓練集 training_v1（正面近景）'),
    ('jia-seo', 'Jia Seo', 'kols/jia-seo/identity/identity_master.jpg', 'identity_master（Penny 2026-09-01 核准）'),
    ('luna-tanaka', 'Luna Tanaka', 'kols/luna-tanaka/images/face_reference/ref_04.webp', 'Soul 訓練用臉部參考（ref_04，正面）'),
    ('somi-oh', 'Somi Oh', 'kols/somi-oh/identity/identity_master.jpg', 'identity_master（Penny 2026-09-01 核准）'),
    ('rainie-hsu', 'Rainie Hsu', 'kols/rainie-hsu/images/face_reference/candidate_02.png', 'Reference Element v2 錨點原圖（rainie-hsu-anchor-v2；R24 核對）'),
]


# 自動頭肩框仍含背景人像照片牆（Coco）或手機（Rainie）的，改用人工框（只裁切）
OVERRIDE = {'coco-wu': [380, 176, 1409, 1548], 'rainie-hsu': [340, 196, 1140, 1263]}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for i, (pid, name, src, why) in enumerate(REFS, 1):
        raw = open(os.path.join(ROOT, src), 'rb').read()
        assert subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch', src], capture_output=True).returncode == 0, src
        im = Image.open(io.BytesIO(raw)).convert('RGB')
        W, H = im.size
        if 'identity_master' in src:
            box = [0, 0, W, H]
        elif pid in OVERRIDE:
            box = OVERRIDE[pid]
        else:
            P, _ = landmarks(os.path.join(ROOT, src))
            assert P is not None, src
            x0, x1 = P[:, 0].min(), P[:, 0].max()
            y0, y1 = P[:, 1].min(), P[:, 1].max()
            fw = x1 - x0
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            w = min(W, fw * 2.2)
            h = min(H, w * 4 / 3)
            bx = int(round(min(max(cx - w / 2, 0), W - w)))
            by = int(round(min(max(cy - h * 0.40, 0), H - h)))
            box = [bx, by, bx + int(round(w)), by + int(round(h))]
        c = im.crop(box)
        b = io.BytesIO()
        c.save(b, 'JPEG', quality=95, subsampling=0)
        data = b.getvalue()
        fn = f'ref{i:02d}_{pid}.jpg'
        open(os.path.join(OUT, fn), 'wb').write(data)
        rows.append({'image_no': i, 'set': pid, 'name': name, 'source': src, 'source_sha256': sha(raw), 'source_px': [W, H],
                     'why': why, 'crop_box_px': box, 'file': f'review/calendar/m5_r27/refs/{fn}', 'px': list(c.size), 'sha256': sha(data)})
        print(i, pid, box, c.size)
    json.dump({'note': '封面身分參考（送入模型的順序即 Image 1–12）；只裁切、不修圖、不放大；JPEG q95 不帶中繼資料', 'refs': rows},
              open(os.path.join(ROOT, 'review', 'calendar', 'm5_r27', 'refs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
