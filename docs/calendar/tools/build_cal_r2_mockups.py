#!/usr/bin/env python3
"""TASK-CAL-001 / R2 — 本機桌曆樣張（草稿，未經 Penny 選定）。

真實尺寸、300 dpi；畫布含 2 mm 出血（橫 204×155、直 144×204 mm）。
照片只做裁切與等比縮放；日期全部來自人事總處 116 年辦公日曆表（cal_dates.py）。
線圈區：上緣 12 mm（＝出血 2＋廠商橫式安全框 10；直式安全框廠商設 0，此值為本輪假設）。
用法：python3 docs/calendar/tools/build_cal_r2_mockups.py --hf-dir <取回原圖的資料夾>
"""
import argparse
import json
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(__file__))
from cal_dates import EN, FONT_CJK, FONT_LAT, FONT_LAT_B, INK, MUTED, draw_grid, draw_strip, f  # noqa: E402
from cal_face_lib import geometry  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
OUT = os.path.join(CAL, 'r2', 'mockups')
DPI = 300
MM = DPI / 25.4
COIL = 12
BRAND = '［品牌名稱 佔位］'

PEOPLE = {
    'iris-chen': ('Iris Chen', '陳芯語', '台北 It Girl', 1, 'iris_H', 'iris_V', 'iris_V'),
    'vicky-lin': ('Vicky Lin', '林薇淇', '高雄健身', 6, 'vicky_H', 'vicky_V', 'vicky_V'),
    'rin-ayase': ('Rin Ayase', '綾瀨凜', '銀座夜色', 11, 'rin_H', 'rin_V', 'rin_altR1V'),
}
COVER = [('iris-chen', 'Iris', 'iris_H'), ('kanon-komori', 'Kanon', 'kanon_alt028'), ('luna-tanaka', 'Luna', 'luna_V'),
         ('angel-chiu', 'Angel', 'angel_alt004'), ('somi-oh', 'Somi', 'somi_V'), ('vicky-lin', 'Vicky', 'vicky_V'),
         ('coco-wu', 'Coco', 'coco_H'), ('mia-huang', 'Mia', 'mia_H'), ('yuna-kim', 'Yuna', 'yuna_V'),
         ('tammy-chou', 'Tammy', 'tammy_V'), ('rin-ayase', 'Rin', 'rin_V'), ('rainie-hsu', 'Rainie', 'rainie_V')]


def px(v):
    return int(round(v * MM))


def place_photo(page, src, box_mm, fy=0.36, report=None, key=''):
    """把原圖裁成照片框的比例後等比縮放放進 box（mm，畫布座標）。臉中心優先放在框高 fy 的位置。"""
    x0, y0, x1, y1 = box_mm
    w, h = x1 - x0, y1 - y0
    im = Image.open(src).convert('RGB')
    W, H = im.size
    g = geometry(src)
    if g:
        cx = float(g['mid'][0])
        cy = float((g['P'][10][1] + g['P'][152][1]) / 2)
    else:
        cx, cy = W / 2, H * 0.3
    a = w / h
    if W / H > a:
        ch, cw = H, round(H * a)
        cx0 = min(max(round(cx - cw / 2), 0), W - cw)
        cy0 = 0
    else:
        cw, ch = W, round(W / a)
        cx0 = 0
        cy0 = min(max(round(cy - fy * ch), 0), H - ch)
    crop = im.crop((cx0, cy0, cx0 + cw, cy0 + ch)).resize((px(w), px(h)), Image.LANCZOS)
    page.paste(crop, (px(x0), px(y0)))
    if report is not None:
        r = {'src_px': [W, H], 'crop_px': [cx0, cy0, cw, ch], 'frame_mm': [round(w, 1), round(h, 1)],
             'effective_ppi': round(cw / (w / 25.4)), 'upscaled': bool(cw < px(w))}
        if g:
            k = h / ch
            r['forehead_y_mm'] = round(float(y0 + (g['P'][10][1] - cy0) * k), 1)
            r['chin_y_mm'] = round(float(y0 + (g['P'][152][1] - cy0) * k), 1)
            r['face_clear_of_coil'] = bool(r['forehead_y_mm'] >= COIL + 3)
        report[key] = r
    return page


def text(d, xy_mm, s, size_mm, font=FONT_CJK, fill=INK, anchor='la'):
    d.text((px(xy_mm[0]), px(xy_mm[1])), s, fill=fill, font=f(font, size_mm * MM), anchor=anchor)


def guides(page, W, H, safe):
    """預覽用參考線：紅＝線圈區、藍＝裁切線、綠＝安全框。不屬於印刷內容。"""
    g = page.copy().convert('RGBA')
    ov = Image.new('RGBA', g.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rectangle((0, 0, px(W), px(COIL)), fill=(255, 0, 0, 70))
    d.rectangle((px(2), px(2), px(W - 2), px(H - 2)), outline=(0, 90, 255, 255), width=4)
    t, r, b, l = safe
    d.rectangle((px(2 + l), px(2 + t), px(W - 2 - r), px(H - 2 - b)), outline=(0, 170, 60, 255), width=3)
    return Image.alpha_composite(g, ov).convert('RGB')


def save(img, name, guide_img=None):
    hi = os.path.join(OUT, 'hires', f'{name}.jpg')
    img.save(hi, quality=92, dpi=(DPI, DPI))
    pv = img.copy()
    pv.thumbnail((1400, 1400))
    pv.save(os.path.join(OUT, f'{name}.jpg'), quality=86)
    if guide_img is not None:
        gp = guide_img.copy()
        gp.thumbnail((1400, 1400))
        gp.save(os.path.join(OUT, f'{name}_guides.jpg'), quality=84)


def month_head(d, x, y, m, name_en, name_zh, tag, size=1.0):
    text(d, (x, y), f'{m:02d}', 15 * size, FONT_LAT_B)
    text(d, (x + 24 * size, y + 2.2 * size), EN[m - 1].upper(), 4.4 * size, FONT_LAT, MUTED)
    text(d, (x + 24 * size, y + 8.2 * size), f'2027 · {m} 月', 4.0 * size, FONT_CJK, MUTED)
    text(d, (x, y + 20 * size), f'{name_en}  {name_zh}', 4.6 * size, FONT_CJK)
    text(d, (x, y + 26.5 * size), tag, 3.4 * size, FONT_CJK, MUTED)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hf-dir', required=True)
    a = ap.parse_args()
    os.makedirs(os.path.join(OUT, 'hires'), exist_ok=True)
    J = {c['cid']: c for c in json.load(open(os.path.join(CAL, 'data', 'cal_r2_judgments.json')))['candidates']}
    R = json.load(open(os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')))['items']

    def src(cid):
        s = J[cid]['src']
        if s.startswith('hf:'):
            return os.path.join(a.hf_dir, next(r for r in R if r['job_id'] == s[3:])['local'])
        return os.path.join(ROOT, s)

    rep = {}
    for pid, (en, zh, tag, m, h_cid, v_cid, hb_cid) in PEOPLE.items():
        # 橫式 A：左半直幅照片＋右半日期（優先方案）
        W, H = 204, 155
        pg = Image.new('RGB', (px(W), px(H)), 'white')
        place_photo(pg, src(h_cid), (0, 0, 104, H), fy=0.34, report=rep, key=f'{pid}_H_A')
        d = ImageDraw.Draw(pg)
        month_head(d, 112, 16, m, en, zh, tag)
        draw_grid(d, (px(112), px(54), px(198), px(140)), 2027, m, MM, title=False)
        text(d, (198, 147), BRAND, 2.8, FONT_CJK, MUTED, anchor='ra')
        save(pg, f'H_A_{m:02d}_{pid}', guides(pg, W, H, (10, 2, 2, 2)))

        # 橫式 B：大照片＋下方單行日期（比較方案；照片框避開線圈，不滿版）
        pg = Image.new('RGB', (px(W), px(H)), 'white')
        place_photo(pg, src(hb_cid), (6, 14, 198, 118), fy=0.40, report=rep, key=f'{pid}_H_B')
        d = ImageDraw.Draw(pg)
        text(d, (8, 122), f'{m:02d}', 9, FONT_LAT_B)
        text(d, (8, 133), EN[m - 1].upper() + ' 2027', 2.8, FONT_LAT, MUTED)
        text(d, (8, 137.5), f'{en} {zh}', 3.0, FONT_CJK)
        draw_strip(d, (px(46), px(122), px(198), px(140)), 2027, m, MM)
        text(d, (198, 145), BRAND, 2.8, FONT_CJK, MUTED, anchor='ra')
        save(pg, f'H_B_{m:02d}_{pid}', guides(pg, W, H, (10, 2, 2, 2)))

        # 直式 A：大照片（上 150 mm）＋下方日期
        W, H = 144, 204
        pg = Image.new('RGB', (px(W), px(H)), 'white')
        place_photo(pg, src(v_cid), (0, 0, W, 150), fy=0.36, report=rep, key=f'{pid}_V_A')
        d = ImageDraw.Draw(pg)
        month_head(d, 8, 155, m, en, zh, tag, size=0.8)
        draw_grid(d, (px(58), px(154), px(138), px(199)), 2027, m, MM, title=False)
        text(d, (8, 197), BRAND, 2.6, FONT_CJK, MUTED)
        save(pg, f'V_A_{m:02d}_{pid}', guides(pg, W, H, (2, 2, 2, 2)))

        # 直式 B：縮框留白
        pg = Image.new('RGB', (px(W), px(H)), 'white')
        place_photo(pg, src(v_cid), (10, 16, 134, 148), fy=0.36, report=rep, key=f'{pid}_V_B')
        d = ImageDraw.Draw(pg)
        month_head(d, 10, 155, m, en, zh, tag, size=0.8)
        draw_grid(d, (px(58), px(154), px(134), px(199)), 2027, m, MM, title=False)
        text(d, (10, 197), BRAND, 2.6, FONT_CJK, MUTED)
        save(pg, f'V_B_{m:02d}_{pid}', guides(pg, W, H, (2, 2, 2, 2)))

    # 配對的大格月曆面（以 Iris／1 月為例，兩款各一）
    for kind, (W, H) in (('H', (204, 155)), ('V', (144, 204))):
        pg = Image.new('RGB', (px(W), px(H)), 'white')
        d = ImageDraw.Draw(pg)
        text(d, (10, 15), '01', 12, FONT_LAT_B)
        text(d, (30, 16.5), 'JANUARY 2027', 4, FONT_LAT, MUTED)
        text(d, (30, 22), 'Iris Chen 陳芯語｜台北 It Girl', 3.6, FONT_CJK)
        top = 32
        draw_grid(d, (px(10), px(top), px(W - 10), px(H - 12)), 2027, 1, MM, title=False)
        text(d, (W - 10, H - 7), '紅字依行政院人事行政總處 116 年辦公日曆表', 2.4, FONT_CJK, MUTED, anchor='ra')
        save(pg, f'{kind}_grid_01_iris-chen', guides(pg, W, H, (10, 2, 2, 2) if kind == 'H' else (2, 2, 2, 2)))

    # 封面草稿（兩款）
    heads = []
    for pid, label, cid in COVER:
        s = src(cid)
        im = Image.open(s).convert('RGB')
        g = geometry(s)
        fh = float(g['P'][152][1] - g['P'][10][1])
        cx, cy = float(g['mid'][0]), float((g['P'][10][1] + g['P'][152][1]) / 2)
        side_w, side_h = fh * 2.0, fh * 2.6
        box = (int(cx - side_w / 2), int(cy - side_h * 0.42), int(cx + side_w / 2), int(cy + side_h * 0.58))
        canvas = Image.new('RGB', (box[2] - box[0], box[3] - box[1]), (235, 235, 235))
        ix0, iy0 = max(box[0], 0), max(box[1], 0)
        canvas.paste(im.crop((ix0, iy0, min(box[2], im.width), min(box[3], im.height))), (ix0 - box[0], iy0 - box[1]))
        heads.append((label, canvas, round(canvas.width / 1)))
    for kind, (W, H), cols, area in (('H', (204, 155), 6, (8, 46, 196, 146)), ('V', (144, 204), 4, (8, 52, 136, 196))):
        pg = Image.new('RGB', (px(W), px(H)), 'white')
        d = ImageDraw.Draw(pg)
        text(d, (W / 2, 16), '2027', 16, FONT_LAT_B, anchor='ma')
        text(d, (W / 2, 33 if kind == 'H' else 34), '12 位虛擬 KOL・12 種長相', 4.6, FONT_CJK, anchor='ma')
        text(d, (W / 2, 40 if kind == 'H' else 42), BRAND, 3.2, FONT_CJK, MUTED, anchor='ma')
        x0, y0, x1, y1 = area
        rows = 12 // cols
        gap = 2.2
        tw = (x1 - x0 - gap * (cols - 1)) / cols
        th = (y1 - y0 - gap * (rows - 1) - rows * 4.5) / rows
        for i, (label, head, _) in enumerate(heads):
            cx_, cy_ = x0 + (i % cols) * (tw + gap), y0 + (i // cols) * (th + gap + 4.5)
            hh = head.copy()
            a_ = tw / th
            if hh.width / hh.height > a_:
                nw = int(hh.height * a_)
                hh = hh.crop(((hh.width - nw) // 2, 0, (hh.width + nw) // 2, hh.height))
            else:
                nh = int(hh.width / a_)
                hh = hh.crop((0, 0, hh.width, nh))
            rep[f'cover_{kind}_{label}'] = {'tile_mm': [round(tw, 1), round(th, 1)], 'effective_ppi': round(hh.width / (tw / 25.4)),
                                            'upscaled': bool(hh.width < px(tw))}
            pg.paste(hh.resize((px(tw), px(th)), Image.LANCZOS), (px(cx_), px(cy_)))
            text(d, (cx_ + tw / 2, cy_ + th + 0.8), label, 3.0, FONT_LAT, INK, anchor='ma')
        save(pg, f'{kind}_cover', guides(pg, W, H, (10, 2, 2, 2) if kind == 'H' else (2, 2, 2, 2)))

    json.dump({'generated_by': 'docs/calendar/tools/build_cal_r2_mockups.py', 'dpi': DPI, 'coil_mm': COIL,
               'note': 'effective_ppi＝原圖裁切後像素 ÷ 框寬英吋；upscaled=true 表示排版時有放大（只影響預覽品質判斷，不代表原圖細節足夠）。',
               'placements': rep}, open(os.path.join(CAL, 'data', 'cal_r2_mockup_report.json'), 'w'), ensure_ascii=False, indent=1)
    sheet()
    sheet_pairs()
    print('ok', len(rep))


def sheet():
    """總覽：每位 4 種照片面＋配對月曆面＋封面（各張 < 1 MB）。"""
    from PIL import ImageFont
    lab = ImageFont.truetype(FONT_CJK, 26)
    groups = [('iris-chen', '01'), ('vicky-lin', '06'), ('rin-ayase', '11')]
    for pid, m in groups:
        names = [f'H_A_{m}_{pid}', f'H_B_{m}_{pid}', f'V_A_{m}_{pid}', f'V_B_{m}_{pid}']
        ims = [Image.open(os.path.join(OUT, n + '.jpg')) for n in names]
        for i in ims:
            i.thumbnail((900, 900))
        W = ims[0].width + ims[1].width + 30
        H = max(ims[0].height, ims[1].height) + max(ims[2].height, ims[3].height) + 100
        S = Image.new('RGB', (max(W, ims[2].width + ims[3].width + 30), H), '#cfcfcf')
        d = ImageDraw.Draw(S)
        d.text((10, 6), f'{pid}｜左上：橫式 A 半版（推薦）　右上：橫式 B 大照片（比較）　下：直式 A 大照片／直式 B 縮框｜草稿', fill='black', font=lab)
        S.paste(ims[0], (0, 44))
        S.paste(ims[1], (ims[0].width + 30, 44))
        y = 44 + max(ims[0].height, ims[1].height) + 20
        S.paste(ims[2], (0, y))
        S.paste(ims[3], (ims[2].width + 30, y))
        S.save(os.path.join(OUT, f'CAL_R2_mockups_{m}_{pid}.jpg'), quality=82)


def sheet_pairs():
    from PIL import ImageFont
    lab = ImageFont.truetype(FONT_CJK, 26)
    rows = [('橫式：照片面（A 半版）＋配對大格月曆面', ['H_A_01_iris-chen', 'H_grid_01_iris-chen']),
            ('直式：照片面（A 大照片）＋配對大格月曆面', ['V_A_01_iris-chen', 'V_grid_01_iris-chen']),
            ('封面草稿：橫式／直式（品牌為佔位文字）', ['H_cover', 'V_cover'])]
    for i, (title, names) in enumerate(rows, 1):
        ims = [Image.open(os.path.join(OUT, n + '.jpg')) for n in names]
        for im in ims:
            im.thumbnail((900, 900))
        S = Image.new('RGB', (sum(im.width for im in ims) + 30, max(im.height for im in ims) + 50), '#cfcfcf')
        ImageDraw.Draw(S).text((10, 8), title + '｜草稿', fill='black', font=lab)
        x = 0
        for im in ims:
            S.paste(im, (x, 46))
            x += im.width + 30
        S.save(os.path.join(OUT, f'CAL_R2_pairs_{i}.jpg'), quality=84)


if __name__ == '__main__':
    main()
