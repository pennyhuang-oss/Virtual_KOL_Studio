# M-4 R23：H-Somi R22-2 本機調色 1 張（只調明暗與色彩；不改人物、動作、服裝、背景；不覆蓋原圖；不加銳化、清晰度或局部對比）。
# 提亮中間調與暗部、適度自然飽和度；膚色只小幅提升；0.9 以上高光柔肩，保留逆光天空與草穗高光細節。
# 用法：python3 review/calendar/m4_r23/process.py [--preview 輸出資料夾]
import importlib.util, json, os, sys
import numpy as np
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
_spec = importlib.util.spec_from_file_location('p22', os.path.join(ROOT, 'review', 'calendar', 'm4_r22', 'process.py'))
p22 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(p22)
luma, stats, lapvar = p22.luma, p22.stats, p22.lapvar

IT = {'set': 'H-somi-oh', 'src': 'kols/somi-oh/images/calendar_2027_batch1/H-somi-oh_m4r22_B.png',
      'why': 'Penny：色調調整一下，明亮度跟飽和度提升一點，現在畫面有點太暗淡了',
      'gamma': 0.86, 'vibrance': 0.14, 'skin_vibrance': 0.04}


def main():
    prev = sys.argv[sys.argv.index('--preview') + 1] if '--preview' in sys.argv else None
    it = IT
    a, out, _ = p22.process(it)
    dst = it['src'].replace('.png', '_grade_r23.png')
    im = Image.fromarray((out * 255 + 0.5).astype(np.uint8))
    im.save(os.path.join(ROOT, dst), optimize=True)
    ya, yo = luma(a), luma(out)
    sa = Image.open(os.path.join(ROOT, it['src'])).convert('RGB')
    w, h = 1600, round(sa.height * 1600 / sa.width)
    va = np.asarray(sa.resize((w, h), Image.LANCZOS)).astype(float) / 255
    vo = np.asarray(im.resize((w, h), Image.LANCZOS)).astype(float) / 255
    hi = ya > 0.85
    r = {'set': it['set'], 'source': it['src'], 'output': dst, 'why': it['why'],
         'params': {k: v for k, v in it.items() if k not in ('set', 'src', 'why')},
         'before': stats(a), 'after': stats(out),
         'detail_ratio_full': round(lapvar(yo) / lapvar(ya), 3), 'detail_ratio_site_view': round(lapvar(luma(vo)) / lapvar(luma(va)), 3),
         'contrast_ratio': round(float(yo.std() / ya.std()), 3),
         'highlight_detail_ratio': round(float(yo[hi].std() / ya[hi].std()), 3) if hi.any() else None}
    if prev:
        A, B = sa.resize((w // 2, h // 2), Image.LANCZOS), im.resize((w // 2, h // 2), Image.LANCZOS)
        c = Image.new('RGB', (A.width * 2 + 10, A.height), (20, 20, 20)); c.paste(A, (0, 0)); c.paste(B, (A.width + 10, 0))
        c.save(os.path.join(prev, 'H-somi-oh_r23_site_compare.jpg'), quality=90)
        box = (700, 0, 1300, 520)
        A, B = sa.crop(box), im.crop(box)
        c = Image.new('RGB', (A.width * 2 + 10, A.height), (20, 20, 20)); c.paste(A, (0, 0)); c.paste(B, (A.width + 10, 0))
        c.save(os.path.join(prev, 'H-somi-oh_r23_full_crop_compare.jpg'), quality=92)
    print(json.dumps(r, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
