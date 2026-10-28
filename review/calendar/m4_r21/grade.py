# M-4 R21：3 張本機調色（只調明暗與色彩；不改臉、身體、服裝、姿態或場景；不覆蓋原圖）。
# 每張各自的參數寫在 GRADES；輸出 <套別>_m4r20_<A|B>_grade_r21.png 存在原圖旁，並印出調色前後的量測。
# 用法：python3 review/calendar/m4_r21/grade.py [--preview 輸出資料夾]
import json, os, sys
import numpy as np
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
DIR = 'kols/{pid}/images/calendar_2027_batch1/{sid}_m4r20_{v}.png'
GRADES = [
    {'set': 'H-coco-wu', 'pid': 'coco-wu', 'v': 'A', 'why': 'Penny：提高明亮度與飽和度，改善暗淡感',
     'gamma': 0.84, 'vibrance': 0.16, 'skin_vibrance': 0.05, 'warmth': 0.0},
    {'set': 'V-miu-shiraishi', 'pid': 'miu-shiraishi', 'v': 'B', 'why': 'Penny：保留 B 的人物與構圖，以 A 的整體明暗、色彩作視覺參考，改善 B 的暗淡感',
     'match': 'A', 'match_strength': 0.85, 'vibrance': 0.10, 'skin_vibrance': 0.04, 'warmth': 0.0},
    {'set': 'V-luna-tanaka', 'pid': 'luna-tanaka', 'v': 'B', 'why': 'Penny：適度提高明亮度與飽和度',
     'gamma': 0.88, 'vibrance': 0.08, 'skin_vibrance': 0.03, 'warmth': 0.0},
]
W = np.array([0.2126, 0.7152, 0.0722])


def load(p):
    return np.asarray(Image.open(os.path.join(ROOT, p)).convert('RGB')).astype(np.float64) / 255.0


def luma(a):
    return a @ W


def stats(a):
    Y = luma(a)
    mx, mn = a.max(-1), a.min(-1)
    sat = np.where(mx > 1e-6, (mx - mn) / np.maximum(mx, 1e-6), 0)
    return {'Y_p5': round(float(np.percentile(Y, 5)), 3), 'Y_p50': round(float(np.percentile(Y, 50)), 3), 'Y_p95': round(float(np.percentile(Y, 95)), 3),
            'Y_mean': round(float(Y.mean()), 3), 'sat_mean': round(float(sat.mean()), 3),
            'clipped_pct': round(float((mx > 0.985).mean() * 100), 2), 'crushed_pct': round(float((mx < 0.015).mean() * 100), 2)}


def curve_from_points(xs, ys):
    """單調三次（Fritsch–Carlson）通過控制點的明暗曲線，回傳 1024 格查表。"""
    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    d = np.diff(ys) / np.diff(xs)
    m = np.concatenate([[d[0]], (d[:-1] + d[1:]) / 2, [d[-1]]])
    for i in range(len(d)):
        if d[i] == 0:
            m[i] = m[i + 1] = 0
        else:
            a, b = m[i] / d[i], m[i + 1] / d[i]
            s = a * a + b * b
            if s > 9:
                t = 3 / np.sqrt(s); m[i] = t * a * d[i]; m[i + 1] = t * b * d[i]
    x = np.linspace(0, 1, 1024)
    k = np.clip(np.searchsorted(xs, x) - 1, 0, len(xs) - 2)
    h = xs[k + 1] - xs[k]; t = (x - xs[k]) / h
    h00, h10, h01, h11 = 2*t**3 - 3*t**2 + 1, t**3 - 2*t**2 + t, -2*t**3 + 3*t**2, t**3 - t**2
    return np.clip(h00 * ys[k] + h10 * h * m[k] + h01 * ys[k + 1] + h11 * h * m[k + 1], 0, 1)


def skin_mask(a):
    """膚色區（色相約 0–50°、中低飽和、亮度中等）的柔性遮罩，用來降低膚色的飽和度提升。"""
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1)
    sat = np.where(mx > 1e-6, (mx - mn) / np.maximum(mx, 1e-6), 0)
    warm = (r >= g) & (g >= b * 0.9)
    m = warm & (sat > 0.08) & (sat < 0.6) & (mx > 0.25)
    return m.astype(np.float64)


def grade(a, g, ref=None):
    Y = luma(a)
    if 'match' in g:
        q = [1, 5, 25, 50, 75, 95, 99.5]
        src = np.percentile(Y, q)
        tgt = np.percentile(luma(ref), q)
        tgt = src + g['match_strength'] * (tgt - src)
        tgt[-1] = min(tgt[-1], src[-1] + 0.25 * (1 - src[-1]))  # 最亮處只小幅提升，保留高光細節
        xs = np.concatenate([[0], src, [1]]); ys = np.concatenate([[0], tgt, [1]])
        xs, idx = np.unique(xs, return_index=True); ys = np.maximum.accumulate(ys[idx])
        lut = curve_from_points(xs, ys)
    else:
        lut = np.linspace(0, 1, 1024) ** g['gamma']
    Y2 = lut[np.clip((Y * 1023).round().astype(int), 0, 1023)]
    ratio = np.where(Y > 1e-4, Y2 / np.maximum(Y, 1e-4), 1.0)[..., None]
    out = a * ratio
    # 高光保護：超出 1 的像素往其亮度收，保留色相、不硬剪
    over = out.max(-1, keepdims=True)
    k = np.where(over > 1, (1 - Y2[..., None]) / np.maximum(over - Y2[..., None], 1e-6), 1.0)
    out = Y2[..., None] + (out - Y2[..., None]) * np.clip(k, 0, 1)
    # 自然飽和度：原本越不飽和的提升越多；膚色區只小幅提升
    Yo = luma(out)[..., None]
    mx, mn = out.max(-1, keepdims=True), out.min(-1, keepdims=True)
    sat = np.where(mx > 1e-6, (mx - mn) / np.maximum(mx, 1e-6), 0)
    if ref is not None:
        rs, os_ = stats(ref)['sat_mean'], stats(out)['sat_mean']
        extra = g['vibrance'] + max(0.0, min(0.25, rs / max(os_, 1e-6) - 1))
    else:
        extra = g['vibrance']
    skin = skin_mask(a)[..., None]
    amt = (extra * (1 - sat)) * (1 - skin) + g['skin_vibrance'] * skin
    # 飽和度提升不把任一色版推過 1（避免新增剪白）、也不推到 0 以下
    hi = np.where(mx - Yo > 1e-6, (1 - Yo) / np.maximum(mx - Yo, 1e-6), np.inf)
    lo = np.where(Yo - mn > 1e-6, Yo / np.maximum(Yo - mn, 1e-6), np.inf)
    amt = np.minimum(amt, np.maximum(np.minimum(hi, lo) - 1, 0))
    out = Yo + (out - Yo) * (1 + amt)
    # 高光柔肩：0.9 以上逐漸收斂，原本未剪白的亮部不被推成死白
    K = 0.9
    knee = lambda x: np.where(x > K, K + (1 - K) * np.tanh((x - K) / (1 - K)), x)
    out = np.where(a.max(-1, keepdims=True) > 0.985, out, knee(out))
    return np.clip(out, 0, 1), {'curve': 'percentile match to A' if 'match' in g else f"gamma {g['gamma']}", 'vibrance_used': round(float(extra), 3)}


def main():
    prev = sys.argv[sys.argv.index('--preview') + 1] if '--preview' in sys.argv else None
    rep = []
    for g in GRADES:
        src = DIR.format(pid=g['pid'], sid=g['set'], v=g['v'])
        a = load(src)
        ref = load(DIR.format(pid=g['pid'], sid=g['set'], v=g['match'])) if 'match' in g else None
        out, how = grade(a, g, ref)
        dst = src.replace('.png', '_grade_r21.png')
        im = Image.fromarray((out * 255 + 0.5).astype(np.uint8))
        im.save(os.path.join(ROOT, dst), optimize=True)
        r = {'set': g['set'], 'v': g['v'], 'source': src, 'output': dst, 'why': g['why'], 'params': {k: v for k, v in g.items() if k not in ('set', 'pid', 'v', 'why')},
             'how': how, 'before': stats(a), 'after': stats(out)}
        if ref is not None:
            r['reference_A'] = stats(ref)
        rep.append(r)
        if prev:
            w = 900 if a.shape[1] > a.shape[0] else 600
            A = Image.open(os.path.join(ROOT, src)).convert('RGB'); h = round(A.height * w / A.width)
            c = Image.new('RGB', (2 * w + 10, h), (20, 20, 20)); c.paste(A.resize((w, h)), (0, 0)); c.paste(im.resize((w, h)), (w + 10, 0))
            c.save(os.path.join(prev, f"{g['set']}_grade_compare.jpg"), quality=88)
    print(json.dumps(rep, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
