# M-4 R14：Tammy、Rin 試拍的顯示版、直式 120×160 套框預覽，以及與各自 R5 退回照片的對照；原圖不動，衍生檔不含中繼資料
import base64, io, re, subprocess
from PIL import Image, ImageDraw, ImageFont
R = '/home/user/Virtual_KOL_Studio'
S = '<scratchpad>'   # render_svg.cjs 與暫存 SVG 所在目錄
OUT = f'{R}/review/calendar/m4_r14'
LAY = f'{R}/docs/calendar/decision_site/public/print'
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
SETS = [
    {'id': 'V-tammy-chou', 'kol': 'tammy-chou', 'name': 'Tammy',
     'ref': f'{R}/kols/tammy-chou/images/training_v1/train_01.jpg', 'ref_label': 'Tammy Soul 訓練圖 1（身分基準）', 'ref_box': (530, 500, 880, 900),
     'r5_box': (620, 330, 900, 640), 'r14_box': (590, 480, 850, 760)},
    {'id': 'V-rin-ayase', 'kol': 'rin-ayase', 'name': 'Rin',
     'ref': f'{R}/kols/rin-ayase/identity/identity_master.jpg', 'ref_label': 'Rin identity_master（身分基準）', 'ref_box': (380, 280, 1240, 1420),
     'r5_box': (700, 190, 960, 470), 'r14_box': (620, 400, 920, 700)},
]
f = ImageFont.truetype(FONT, 26); fs = ImageFont.truetype(FONT, 22)


def fit_h(im, h): return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def b64(im, width):
    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=90)
    return base64.b64encode(buf.getvalue()).decode()


def guide(x1, x2, y, label, ly):
    return (f'<line x1="{x1}" y1="{y:.1f}" x2="{x2}" y2="{y:.1f}" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4 3"/>'
            f'<text x="{x2 - 6}" y="{ly:.1f}" font-size="12" font-weight="700" text-anchor="end" fill="#dc2626" stroke="#ffffff" stroke-width="3" paint-order="stroke" font-family="WenQuanYi Zen Hei, sans-serif">{label}</text>')


def text_line(lines, needle):
    hits = [i for i, l in enumerate(lines) if needle in l]
    assert len(hits) == 1, (needle, hits)
    return hits[0]


def set_text(line, new):
    return re.sub(r'>[^<]*</text>', '>' + new + '</text>', line)


for s in SETS:
    sid = s['id']
    src = Image.open(f"{R}/kols/{s['kol']}/images/calendar_2027_batch1/{sid}_m4r14.png").convert('RGB')
    r5 = Image.open(f"{R}/kols/{s['kol']}/images/calendar_2027_batch1/{sid}_m4r5.png").convert('RGB')
    ref = Image.open(s['ref']).convert('RGB')
    W, H = src.size
    CH = round(W * 4 / 3); TOP = H - CH
    assert 0 <= TOP < 60, (W, H)
    crop34 = src.crop((0, TOP, W, H))
    src.resize((1200, round(H * 1200 / W)), Image.LANCZOS).save(f'{OUT}/{sid}_m4r14_view.jpg', 'JPEG', quality=90)

    # 對照：上排 R5 退回｜R14 試拍；下排臉部 身分基準｜R5｜R14
    TH = 960
    a, b = fit_h(r5, TH), fit_h(src, TH)
    faces = [(ref.crop(s['ref_box']), s['ref_label']), (r5.crop(s['r5_box']), 'R5（Penny 退回）'), (src.crop(s['r14_box']), 'R14 試拍（待主管看圖）')]
    FH = 360
    fims = [(fit_h(im, FH), lab) for im, lab in faces]
    tl = lambda l: round(ImageDraw.Draw(Image.new('RGB', (1, 1))).textlength(l, font=fs)) + 8
    Wc = max(a.width + b.width + 60, sum(max(i.width, tl(l)) + 24 for i, l in fims) + 40)
    Hc = 50 + TH + 60 + FH + 70
    c = Image.new('RGB', (Wc, Hc), (24, 24, 27)); d = ImageDraw.Draw(c)
    c.paste(a, (20, 50)); d.text((24, 12), f"{s['name']} R5 第一批（Penny 退回）", font=f, fill=(250, 204, 21))
    c.paste(b, (40 + a.width, 50)); d.text((44 + a.width, 12), f"{s['name']} R14 重製試拍（待主管看圖，非成品接受）", font=f, fill=(134, 239, 172))
    x = 20; y = 50 + TH + 50
    for im, lab in fims:
        c.paste(im, (x, y)); d.text((x + 4, y - 32), lab, font=fs, fill=(250, 204, 21)); x += max(im.width, tl(lab)) + 24
    d.text((20, Hc - 34), f'臉部裁切只供身分比對；R5、R14 原圖皆 {W}×{H}，上排依高度縮放並排', font=fs, fill=(200, 200, 200))
    c.save(f'{OUT}/{sid}_m4r5_vs_m4r14_compare.jpg', 'JPEG', quality=88)

    L = open(f'{LAY}/layout_V.svg', encoding='utf-8').read().split('\n')
    L[text_line(L, '<title>')] = f'<title>直式款（YFP-CA08）版型與 M-4 R14 {sid} 試拍套框預覽</title>'
    i = text_line(L, '版型與裁切示意（不含生成照片')
    L[i] = set_text(L[i], f'直式款（YFP-CA08）：{sid} M-4 R14 重製試拍套框預覽（不是成品接受、印刷安全證明或印刷核准）')
    i = text_line(L, 'x="112.0" y="160.0" width="480.0" height="640.0" fill="#dbeafe"')
    L[i] = (f'<image href="data:image/jpeg;base64,{b64(crop34, 960)}" x="112" y="160" width="480" height="640" preserveAspectRatio="none"/>'
            '<rect x="112.0" y="160.0" width="480.0" height="640.0" fill="none" stroke="#1d4ed8" stroke-width="2.5" stroke-dasharray="10 5"/>'
            + guide(112, 592, 160 + 0.03 * 640, '頭頂 3%', 160 + 0.03 * 640 + 15)
            + guide(112, 592, 800 - 0.03 * 640, '腳底 3%', 800 - 0.03 * 640 - 5))
    for needle in ('工作照片框 120×160 mm（已接受）', '3:4 放入：不裁切', '灰點線＝R3 統一框'):
        L[text_line(L, needle)] = ''
    i = text_line(L, '若輸出 1536×2048 約 325 ppi')
    L[i] = set_text(L[i], f'・實際輸出 {W}×{H}' + ('（3:4，不裁切）' if TOP == 0 else f'；放入框前從上緣裁 {TOP} px') + f'；寬 120 mm 約 {W / (120 / 25.4):.0f} ppi。')
    i = text_line(L, '生成後仍要用實圖逐張確認')
    L[i] = set_text(L[i], '紅色虛線＝R6-12 最低安全邊界：頭頂、腳底各 3%（本案工作下限，不是廠商規格）。')
    sp = f'{S}/m4r14/frame_{sid}.svg'
    open(sp, 'w', encoding='utf-8').write('\n'.join(L))
    jp = f'{OUT}/{sid}_m4r14_frame_V_120x160.jpg'
    subprocess.run(['node', f'{S}/pw/render_svg.cjs', sp, jp], check=True, cwd=f'{S}/pw')
    for p in (f'{OUT}/{sid}_m4r14_view.jpg', jp, f'{OUT}/{sid}_m4r5_vs_m4r14_compare.jpg'):
        im = Image.open(p); print(p.split('/')[-1], im.size, [k for k in im.info if k not in ('jfif', 'jfif_version', 'jfif_unit', 'jfif_density', 'icc_profile', 'progressive', 'progression', 'dpi')])
    print(sid, 'TOP', TOP, 'ppi', round(W / (120 / 25.4), 1))
