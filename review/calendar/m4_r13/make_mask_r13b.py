# M-4 R13（第二次）：對照 R10 原圖重做遮罩（白＝擬編輯、黑＝保留；平台定義未確認）
# 蛋形（下方加長，留下顎與上頸空間）∩ 頭部輪廓內縮 10 px（不碰背景與外圍髮型輪廓）
import hashlib, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi

R = '/home/user/Virtual_KOL_Studio'
BASE = f'{R}/kols/somi-oh/images/calendar_2027_drafts/V-somi-oh_m4r10_composition_draft.png'
OLD = f'{R}/review/calendar/m4_r12/V-somi-oh_m4r12_edit_mask_1792x2400.png'
OUT = f'{R}/review/calendar/m4_r13'
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
EX, EY, ERX, ERY_TOP, ERY_BOT = 1212, 958, 86, 104, 116   # 蛋形：上半徑 104、下半徑 116
INSET = 10

base_img = Image.open(BASE).convert('RGB')
b = np.asarray(base_img).astype(int)
H, W = b.shape[:2]
assert (W, H) == (1792, 2400)
r, g, bl = b[..., 0], b[..., 1], b[..., 2]

# 頭部輪廓：暖色（頭髮＋皮膚），限定頭部 ROI，閉運算、補洞、取含臉中心的連通區
roi = np.zeros((H, W), bool); roi[820:1110, 1060:1380] = True
warm = (r > bl + 20) & (r > 70) & roi
warm = ndi.binary_closing(warm, structure=np.ones((7, 7)), iterations=1)
warm = ndi.binary_fill_holes(warm)
lab, _ = ndi.label(warm)
head = lab == lab[960, 1205]
head = ndi.binary_fill_holes(head)
head = ndi.gaussian_filter(head.astype(float), 4) > 0.5      # 輪廓平滑，避免順著髮絲出現鋸齒
inner = ndi.binary_erosion(head, structure=np.ones((3, 3)), iterations=INSET)

yy, xx = np.mgrid[0:H, 0:W]
ry = np.where(yy <= EY, ERY_TOP, ERY_BOT)
egg = ((xx - EX) / ERX) ** 2 + ((yy - EY) / ry) ** 2 <= 1
m = egg & inner
m = ndi.binary_opening(m, structure=np.ones((5, 5)))
lab2, n2 = ndi.label(m)
if n2 > 1:
    sizes = ndi.sum(m, lab2, range(1, n2 + 1)); m = lab2 == (1 + int(np.argmax(sizes)))
m = ndi.binary_fill_holes(m)
m = (ndi.gaussian_filter(m.astype(float), 2.5) > 0.5) & inner   # 邊界再平滑一次，仍限制在內縮輪廓內

mask = Image.fromarray((m * 255).astype(np.uint8), 'L')
mp = f'{OUT}/V-somi-oh_m4r13_edit_mask_1792x2400.png'
mask.save(mp, optimize=True)
sha = hashlib.sha256(open(mp, 'rb').read()).hexdigest()

old = np.asarray(Image.open(OLD).convert('L')) > 127
dist_out = ndi.distance_transform_edt(head)          # 到頭部輪廓外（背景）的距離
ys, xs = np.where(m)
rows = {}
for y in range(850, 1081, 10):
    a = np.where(m[y])[0]; o = np.where(old[y])[0]; h = np.where(head[y])[0]
    rows[y] = {'new': [int(a.min()), int(a.max())] if len(a) else None,
               'old': [int(o.min()), int(o.max())] if len(o) else None,
               'head': [int(h.min()), int(h.max())] if len(h) else None}
stats = {
    'mask_sha256': sha, 'size': [W, H], 'mode': 'L', 'white': 255, 'black': 0,
    'white_px': int(m.sum()), 'white_pct': round(m.sum() / (W * H) * 100, 3),
    'bbox': [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())],
    'old_white_px': int(old.sum()), 'old_bbox': [1126, 856, 1294, 1056],
    'min_dist_to_outside_head_px': float(dist_out[m].min()),
    'egg': {'cx': EX, 'cy': EY, 'rx': ERX, 'ry_top': ERY_TOP, 'ry_bottom': ERY_BOT}, 'inset_px': INSET,
    'rows': rows,
}
print(json.dumps(stats, ensure_ascii=False))

# 示意圖：全圖＋頭部放大；洋紅＝新遮罩白色部分，黃線＝R12 舊橢圓
def overlay(img):
    tint = Image.new('RGB', img.size, (255, 0, 160))
    ov = Image.composite(Image.blend(img, tint, 0.45), img, mask)
    d = ImageDraw.Draw(ov)
    d.ellipse((1126, 856, 1294, 1056), outline=(255, 230, 0), width=2)
    edge = ndi.binary_dilation(m, iterations=2) & ~m
    ea = np.asarray(ov).copy(); ea[edge] = (0, 255, 255)
    return Image.fromarray(ea)
ov = overlay(base_img)
full = ov.resize((900, 1205), Image.LANCZOS)
zx0, zy0, zx1, zy1 = 1060, 800, 1360, 1150
zoom = ov.crop((zx0, zy0, zx1, zy1)).resize((900, 1050), Image.LANCZOS)
f = ImageFont.truetype(FONT, 26); fs = ImageFont.truetype(FONT, 21)
c = Image.new('RGB', (1860, 1205 + 190), (24, 24, 27))
c.paste(full, (20, 60)); c.paste(zoom, (940, 60))
dd = ImageDraw.Draw(c)
dd.text((24, 16), 'R10 底稿（替身，非 Somi）：洋紅＝R13 擬編輯區域（遮罩白色）', font=f, fill=(250, 204, 21))
dd.text((944, 16), '頭部放大：青線＝R13 遮罩邊界、黃線＝R12 舊橢圓', font=f, fill=(250, 204, 21))
dd.text((944, 1125), '調整：下方加長到上頸（留下顎銜接空間）；左側離開背景；', font=fs, fill=(220, 220, 220))
dd.text((944, 1155), '全區在頭部輪廓內縮 10 px 以內；大衣領、毛衣領口、背景不在範圍內', font=fs, fill=(220, 220, 220))
dd.text((24, 1280), f'遮罩：{W}×{H}、8 位元灰階 PNG，白（255）＝擬編輯、黑（0）＝保留；平台的黑白定義未經官方確認。', font=fs, fill=(220, 220, 220))
dd.text((24, 1312), f'白色 {m.sum()} px（{m.sum() / (W * H) * 100:.2f}%），範圍 x{xs.min()}–{xs.max()}、y{ys.min()}–{ys.max()}；sha256 {sha[:16]}…', font=fs, fill=(220, 220, 220))
dd.text((24, 1344), '未上傳、未送出。', font=fs, fill=(220, 220, 220))
c.save(f'{OUT}/V-somi-oh_m4r13_edit_area.jpg', 'JPEG', quality=88)
print('preview', c.size)
