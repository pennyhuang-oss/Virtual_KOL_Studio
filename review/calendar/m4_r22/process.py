# M-4 R22：2 張本機修正（只調明暗與色彩；不改臉、身體、服裝、姿態或場景；不覆蓋原圖；不加銳化、清晰度或局部對比）。
# H-Luna：從 R21 A 原圖另存；整體提亮＋適度飽和，背光的臉用大範圍柔邊遮罩局部提亮。
# V-Miu：從未修改的 R20 B 原圖重做；保留 R21 的提亮與暖色方向，但不再拉高對比（R21 依 A 的分位數拉伸，整體對比 +13%、細節能量 +40%）。
# 用法：python3 review/calendar/m4_r22/process.py [--preview 輸出資料夾]
import importlib.util, json, os, sys
import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
_spec = importlib.util.spec_from_file_location('grade21', os.path.join(ROOT, 'review', 'calendar', 'm4_r21', 'grade.py'))
g21 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(g21)
luma, stats, skin_mask, load = g21.luma, g21.stats, g21.skin_mask, g21.load

ITEMS = [
    {'set': 'H-luna-tanaka', 'src': 'kols/luna-tanaka/images/calendar_2027_batch1/H-luna-tanaka_m4r21_A.png',
     'why': 'Penny：明亮度跟飽和度都要提升，人臉背光很黑要更明亮',
     'gamma': 0.80, 'vibrance': 0.14, 'skin_vibrance': 0.04,
     'face': {'center': [1080, 285], 'radii': [125, 160], 'feather': 90, 'gamma': 0.78}},
    {'set': 'V-miu-shiraishi', 'src': 'kols/miu-shiraishi/images/calendar_2027_batch1/V-miu-shiraishi_m4r20_B.png',
     'why': 'Penny：色調還行，但變得有點太銳化，不像原版柔和',
     'gamma': 0.95, 'vibrance': 0.11, 'skin_vibrance': 0.03},
]


def lapvar(y):
    l = -4 * y[1:-1, 1:-1] + y[:-2, 1:-1] + y[2:, 1:-1] + y[1:-1, :-2] + y[1:-1, 2:]
    return float(l.var())


def soft_ellipse(h, w, c, r, feather):
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt(((xx - c[0]) / r[0]) ** 2 + ((yy - c[1]) / r[1]) ** 2)
    inner = 1.0
    m = np.clip((inner + feather / max(r) - d) / (feather / max(r)), 0, 1)   # 1 在橢圓內，往外 feather px 漸變到 0
    return m * m * (3 - 2 * m)   # smoothstep，邊緣無硬邊


def tone(a, Y2):
    Y = luma(a)
    ratio = np.where(Y > 1e-4, Y2 / np.maximum(Y, 1e-4), 1.0)[..., None]
    out = a * ratio
    over = out.max(-1, keepdims=True)
    k = np.where(over > 1, (1 - Y2[..., None]) / np.maximum(over - Y2[..., None], 1e-6), 1.0)
    return Y2[..., None] + (out - Y2[..., None]) * np.clip(k, 0, 1)


def vibrance(out, a, amt_all, amt_skin):
    Yo = luma(out)[..., None]
    mx, mn = out.max(-1, keepdims=True), out.min(-1, keepdims=True)
    sat = np.where(mx > 1e-6, (mx - mn) / np.maximum(mx, 1e-6), 0)
    skin = skin_mask(a)[..., None]
    amt = (amt_all * (1 - sat)) * (1 - skin) + amt_skin * skin
    hi = np.where(mx - Yo > 1e-6, (1 - Yo) / np.maximum(mx - Yo, 1e-6), np.inf)
    lo = np.where(Yo - mn > 1e-6, Yo / np.maximum(Yo - mn, 1e-6), np.inf)
    amt = np.minimum(amt, np.maximum(np.minimum(hi, lo) - 1, 0))
    return Yo + (out - Yo) * (1 + amt)


def knee(out, a, K=0.9):
    f = np.where(out > K, K + (1 - K) * np.tanh((out - K) / (1 - K)), out)
    return np.where(a.max(-1, keepdims=True) > 0.985, out, f)


def process(it):
    a = load(it['src'])
    Y = luma(a)
    Y2 = Y ** it['gamma']
    face = None
    if 'face' in it:
        f = it['face']
        m = soft_ellipse(*Y.shape, f['center'], f['radii'], f['feather'])
        Y2 = Y2 * (1 - m) + (Y2 ** (f['gamma'] / 1.0)) * m   # 臉部在整體提亮之上再柔和提亮
        face = m
    out = tone(a, Y2)
    out = vibrance(out, a, it['vibrance'], it['skin_vibrance'])
    out = np.clip(knee(out, a), 0, 1)
    return a, out, face


def main():
    prev = sys.argv[sys.argv.index('--preview') + 1] if '--preview' in sys.argv else None
    rep = []
    for it in ITEMS:
        a, out, face = process(it)
        dst = it['src'].replace('.png', '_grade_r22.png')
        im = Image.fromarray((out * 255 + 0.5).astype(np.uint8))
        im.save(os.path.join(ROOT, dst), optimize=True)
        ya, yo = luma(a), luma(out)
        r = {'set': it['set'], 'source': it['src'], 'output': dst, 'why': it['why'],
             'params': {k: v for k, v in it.items() if k not in ('set', 'src', 'why')},
             'before': stats(a), 'after': stats(out),
             'detail_ratio_full': round(lapvar(yo) / lapvar(ya), 3), 'contrast_ratio': round(float(yo.std() / ya.std()), 3)}
        sa = Image.open(os.path.join(ROOT, it['src'])).convert('RGB')
        w = 1600 if sa.width > sa.height else 1200
        h = round(sa.height * w / sa.width)
        va = np.asarray(sa.resize((w, h), Image.LANCZOS)).astype(float) / 255
        vo = np.asarray(im.resize((w, h), Image.LANCZOS)).astype(float) / 255
        r['detail_ratio_site_view'] = round(lapvar(luma(vo)) / lapvar(luma(va)), 3)
        if face is not None:
            m = face > 0.9
            r['face_Y_median'] = [round(float(np.median(ya[m])), 3), round(float(np.median(yo[m])), 3)]
        rep.append(r)
        if prev:
            for tag, A, B in (('site', sa.resize((w // 2, h // 2), Image.LANCZOS), im.resize((w // 2, h // 2), Image.LANCZOS)),):
                c = Image.new('RGB', (A.width * 2 + 10, A.height), (20, 20, 20)); c.paste(A, (0, 0)); c.paste(B, (A.width + 10, 0))
                c.save(os.path.join(prev, f"{it['set']}_r22_{tag}_compare.jpg"), quality=90)
            # 原尺寸局部並排（臉或畫面中央）
            cx, cy = (it['face']['center'] if 'face' in it else (a.shape[1] // 2, a.shape[0] // 3))
            box = (max(0, cx - 300), max(0, cy - 250), min(a.shape[1], cx + 300), min(a.shape[0], cy + 350))
            A, B = sa.crop(box), im.crop(box)
            c = Image.new('RGB', (A.width * 2 + 10, A.height), (20, 20, 20)); c.paste(A, (0, 0)); c.paste(B, (A.width + 10, 0))
            c.save(os.path.join(prev, f"{it['set']}_r22_full_crop_compare.jpg"), quality=92)
    print(json.dumps(rep, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
