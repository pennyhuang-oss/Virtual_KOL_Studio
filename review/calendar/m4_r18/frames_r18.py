# M-4 R18：Yerin、Jia 試拍的顯示版、橫式 192×104 套框預覽，以及與各自 R5 退回照片的對照；原圖不動，衍生檔不含中繼資料
import base64, io, re, subprocess
from PIL import Image, ImageDraw, ImageFont
R = '/home/user/Virtual_KOL_Studio'
S = '<scratchpad>'   # render_svg.cjs 與暫存 SVG 所在目錄
OUT = f'{R}/review/calendar/m4_r18'
LAY = f'{R}/docs/calendar/decision_site/public/print'
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
# mode＝放進 192×104 框時從原圖上緣裁掉的 px（16:9 原圖 1152 px 高對應 108 mm，框高 104 mm，共需裁約 43 px）
SETS = [
    {'id': 'H-yerin-han', 'kol': 'yerin-han', 'name': 'Yerin', 'mode': 21,
     'ref_box': (380, 280, 1240, 1420), 'r5_box': (1120, 40, 1360, 260), 'new_box': (840, 60, 1060, 260)},
    {'id': 'H-jia-seo', 'kol': 'jia-seo', 'name': 'Jia', 'mode': 40,
     'ref_box': (380, 280, 1240, 1420), 'r5_box': (1100, 50, 1360, 300), 'new_box': (1100, 130, 1330, 370)},
]
f = ImageFont.truetype(FONT, 26); fs = ImageFont.truetype(FONT, 22)


def fit_w(im, w): return im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
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
    src = Image.open(f"{R}/kols/{s['kol']}/images/calendar_2027_batch1/{sid}_m4r18.png").convert('RGB')
    prev = Image.open(f"{R}/kols/{s['kol']}/images/calendar_2027_batch1/{sid}_m4r5.png").convert('RGB')
    ref = Image.open(f"{R}/kols/{s['kol']}/identity/identity_master.jpg").convert('RGB')
    W, H = src.size
    assert (W, H) == (2048, 1152)
    fit_w(src, 1600).save(f'{OUT}/{sid}_m4r18_view.jpg', 'JPEG', quality=90)

    # 對照：上 R5 退回、下 R18；右側臉部 身分基準｜R5｜R18
    TW = 1100
    a, b = fit_w(prev, TW), fit_w(src, TW)
    FH = 300
    faces = [(ref.crop(s['ref_box']), f"{s['name']} identity_master（身分基準）"), (prev.crop(s['r5_box']), 'R5（Penny 退回）'), (src.crop(s['new_box']), 'R18 試拍（待主管看圖）')]
    fims = [(fit_h(im, FH), lab) for im, lab in faces]
    tl = lambda l: round(ImageDraw.Draw(Image.new('RGB', (1, 1))).textlength(l, font=fs)) + 8
    fw = max(max(i.width, tl(l)) for i, l in fims)
    Wc = 20 + TW + 40 + fw + 20
    Hc = max(50 + a.height + 50 + b.height + 60, 50 + 3 * (FH + 50) + 40)
    c = Image.new('RGB', (Wc, Hc), (24, 24, 27)); d = ImageDraw.Draw(c)
    d.text((24, 12), f"{s['name']} R5 第一批（Penny 退回）", font=f, fill=(250, 204, 21)); c.paste(a, (20, 50))
    y2 = 50 + a.height + 50
    d.text((24, y2 - 38), f"{s['name']} R18 重製試拍（待主管看圖，非成品接受）", font=f, fill=(134, 239, 172)); c.paste(b, (20, y2))
    x = 20 + TW + 40; y = 50
    for im, lab in fims:
        d.text((x + 4, y), lab, font=fs, fill=(250, 204, 21)); c.paste(im, (x, y + 32)); y += FH + 50
    d.text((20, Hc - 34), f'臉部裁切只供身分比對；R5、R18 原圖皆 {W}×{H}', font=fs, fill=(200, 200, 200))
    c.save(f'{OUT}/{sid}_m4r5_vs_m4r18_compare.jpg', 'JPEG', quality=88)

    mode = s['mode']
    L = open(f'{LAY}/layout_H.svg', encoding='utf-8').read().split('\n')
    y0 = round(152 - mode * 432 / 1152, 1)
    L[text_line(L, '<title>')] = f'<title>橫式款（YFP-CA01）版型與 M-4 R18 {sid} 試拍套框預覽</title>'
    i = text_line(L, '版型與裁切示意（不含生成照片')
    L[i] = set_text(L[i], f'橫式款（YFP-CA01）：{sid} M-4 R18 重製試拍套框預覽（不是成品接受、印刷安全證明或印刷核准）')
    for needle in ('x="88.0" y="144.0" width="768.0" height="8.0"', 'x="88.0" y="568.0" width="768.0" height="8.0"',
                   'x="88.0" y="144.0" width="768.0" height="432.0"', '↑ 上緣裁約 2 mm', '↓ 下緣裁約 2 mm',
                   '工作照片框 192×104 mm（已接受）', '16:9 放入：上下各裁約 2 mm'):
        L[text_line(L, needle)] = ''
    data = b64(src, 1536)
    i = text_line(L, 'x="88.0" y="152.0" width="768.0" height="416.0" fill="#dbeafe"')
    L[i] = ('<defs><clipPath id="wf"><rect x="88" y="152" width="768" height="416"/></clipPath></defs>'
            f'<image href="data:image/jpeg;base64,{data}" x="88" y="{y0}" width="768" height="432" preserveAspectRatio="none" opacity="0.35"/>'
            f'<image href="data:image/jpeg;base64,{data}" x="88" y="{y0}" width="768" height="432" preserveAspectRatio="none" clip-path="url(#wf)"/>'
            f'<rect x="88.0" y="{y0}" width="768.0" height="432.0" fill="none" stroke="#7e3fb8" stroke-width="1.5" stroke-dasharray="2 3"/>'
            '<rect x="88.0" y="152.0" width="768.0" height="416.0" fill="none" stroke="#1d4ed8" stroke-width="2.5" stroke-dasharray="10 5"/>'
            + guide(88, 856, 152 + 0.03 * 416, '頭頂 3%', 152 + 0.03 * 416 + 15)
            + guide(88, 856, 568 - 0.03 * 416, '腳底 3%', 568 - 0.03 * 416 - 5))
    i = text_line(L, '上下各裁約 2 mm（1.9%）')
    L[i] = set_text(L[i], f'・16:9 照片寬 192 mm 時高 108 mm，比框高 4 mm；本張上裁約 {mode * 108 / 1152:.1f} mm、下裁約 {4 - mode * 108 / 1152:.1f} mm（框外半透明部分）。')
    i = text_line(L, '原生 16:9 尺寸未知')
    L[i] = set_text(L[i], f'・實際輸出 {W}×{H}；放在 192 mm 寬約 {W / (192 / 25.4):.0f} ppi，低於 300 ppi 工作目標（照實列出；不重生、不放大）。')
    i = text_line(L, '生成後仍要用實圖逐張確認')
    L[i] = set_text(L[i], '紅色虛線＝頭頂、腳底各 3% 工作參考線（本案工作參考，不是廠商裁切線）。')
    sp = f'{S}/m4r18/frame_{sid}.svg'
    open(sp, 'w', encoding='utf-8').write('\n'.join(L))
    jp = f'{OUT}/{sid}_m4r18_frame_H_192x104.jpg'
    subprocess.run(['node', f'{S}/pw/render_svg.cjs', sp, jp], check=True, cwd=f'{S}/pw')
    for p in (f'{OUT}/{sid}_m4r18_view.jpg', jp, f'{OUT}/{sid}_m4r5_vs_m4r18_compare.jpg'):
        im = Image.open(p); print(p.split('/')[-1], im.size, [k for k in im.info if k not in ('jfif', 'jfif_version', 'jfif_unit', 'jfif_density', 'icc_profile', 'progressive', 'progression', 'dpi')])
    print(sid, 'mode', mode, 'ppi', round(W / (192 / 25.4), 1))
