#!/usr/bin/env python3
"""TASK-CAL-001 / R3 — 總覽圖（每張 < 1 MB）、100% 實際像素預覽、清理修前／修後／版面實際大小對照。

只讀 build_cal_r3_pages.py 產生的頁面與 data/cal_r3_layout_report.json、data/cal_r3_cleanup_report.json。
用法：python3 docs/calendar/tools/build_cal_r3_sheets.py --hf-dir <原圖快取> --cache <清理輸出資料夾>
"""
import argparse
import json
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
OUT = os.path.join(CAL, 'r3')
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
MM = 300 / 25.4


def f(n):
    return ImageFont.truetype(FONT, n)


def save_small(img, path, max_w=2000):
    img = img.copy()
    img.thumbnail((max_w, max_w * 3))
    q = 86
    while True:
        img.save(path, quality=q)
        if os.path.getsize(path) < 1_000_000 or q <= 55:
            return path
        q -= 5


def labelled(path, lines, w):
    im = Image.open(path).convert('RGB')
    im.thumbnail((w, w * 2))
    lh = 26
    c = Image.new('RGB', (im.width, im.height + lh * len(lines) + 8), 'white')
    c.paste(im, (0, lh * len(lines) + 8))
    d = ImageDraw.Draw(c)
    for i, s in enumerate(lines):
        d.text((4, 4 + i * lh), s, fill='black' if i == 0 else '#444', font=f(20 if i == 0 else 17))
    return c


def grid(cells, cols, title, bg='#d6d6d6', pad=16):
    rows = [cells[i:i + cols] for i in range(0, len(cells), cols)]
    cw = max(c.width for c in cells)
    rh = [max(c.height for c in r) for r in rows]
    S = Image.new('RGB', (cols * (cw + pad) + pad, sum(rh) + pad * (len(rows) + 1) + 60), bg)
    ImageDraw.Draw(S).text((pad, 14), title, fill='black', font=f(28))
    y = 60
    for r, h in zip(rows, rh):
        x = pad
        for c in r:
            S.paste(c, (x, y))
            x += cw + pad
        y += h + pad
    return S


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hf-dir', required=True)
    ap.add_argument('--cache', required=True)
    a = ap.parse_args()
    L = {p['id']: p for p in json.load(open(os.path.join(CAL, 'data', 'cal_r3_layout_report.json')))['pages']}
    picks = json.load(open(os.path.join(CAL, 'data', 'cal_r3_picks.json')))
    months = picks['months']
    sh = os.path.join(OUT, 'sheets')
    os.makedirs(sh, exist_ok=True)

    def ph(pid):
        return L[pid]['photos'][0]

    def info(pid):
        p = ph(pid)
        return [f"{pid}", f"{p['cid']}｜{'清理版' if p['used_file'] == 'clean' else '原圖'}｜{p['ppi_w']} ppi｜髮頂：{p['hair']['status_auto']}"]

    # 1–2 主推薦 24 面
    for kind, key, cols in (('H', 'H_A', 2), ('V', 'V_U', 3)):
        ids = [f'{key}_{M["m"]:02d}_{M["pid"]}' for M in months]
        for part in (0, 1):
            cells = [labelled(os.path.join(CAL, L[i]['preview']), info(i), 900 if kind == 'H' else 620) for i in ids[part * 6:part * 6 + 6]]
            S = grid(cells, cols, f'R3 暫定工作稿｜{"橫式 A 半版" if kind == "H" else "直式統一框 120×128"}｜{part * 6 + 1}–{part * 6 + 6} 月｜草稿，未經 Penny 核准、未經廠商確認')
            S.save(os.path.join(sh, f'CAL_R3_set_{kind}_{part + 1}_hires.jpg'), quality=88)
            save_small(S, os.path.join(sh, f'CAL_R3_set_{kind}_{part + 1}.jpg'))
    # 3 封面、大格月曆面、年曆
    ids = ['H_cover', 'V_cover', 'H_grid_09_yuna-kim', 'V_grid_12_rainie-hsu', 'V_year_2027']
    cells = [labelled(os.path.join(CAL, L[i]['preview']), [i, f"面 {L[i]['face_no']}｜最小日期字 {L[i]['min_date_em_pt']} pt" if L[i]['min_date_em_pt'] else f"面 {L[i]['face_no']}"], 760) for i in ids]
    S = grid(cells, 3, 'R3 暫定工作稿｜兩款封面、代表大格月曆面（橫 9 月含柔和小框、直 12 月）、直式年曆｜草稿')
    S.save(os.path.join(sh, 'CAL_R3_set_cover_grid_year_hires.jpg'), quality=88)
    save_small(S, os.path.join(sh, 'CAL_R3_set_cover_grid_year.jpg'))
    # 4 原直 A vs 直式統一框
    cells = []
    for pid in picks['compare_VA']:
        M = next(x for x in months if x['pid'] == pid)
        for fr in ('V_A', 'V_U'):
            i = f'{fr}_{M["m"]:02d}_{pid}'
            p = ph(i)
            cells.append(labelled(os.path.join(CAL, L[i]['preview']),
                                  [f"{M['en']}｜{'原直 A 144×150' if fr == 'V_A' else '統一框 120×128'}",
                                   f"{p['cid']}｜原生 {p['native_px'][0]}×{p['native_px'][1]} px｜{p['ppi_w']} ppi",
                                   f"臉最上緣 {p['face']['top_mm']} mm｜髮頂：{p['hair']['status_auto']}"], 520))
    S = grid(cells, 4, '直式比較｜原直 A（144×150）vs 直式統一框（120×128）｜同一張圖、實際裁切重算 ppi')
    S.save(os.path.join(sh, 'CAL_R3_compare_VA_VU_hires.jpg'), quality=88)
    save_small(S, os.path.join(sh, 'CAL_R3_compare_VA_VU.jpg'))
    # 5 橫 B 逐張
    ids = [f'H_B_{M["m"]:02d}_{M["pid"]}' for M in months]
    for part in (0, 1):
        cells = [labelled(os.path.join(CAL, L[i]['preview']), info(i), 760) for i in ids[part * 6:part * 6 + 6]]
        S = grid(cells, 3, f'橫 B 大照片 192×104（比較，非主推薦）｜{part * 6 + 1}–{part * 6 + 6} 月｜ppi＝實際裁切原生像素')
        S.save(os.path.join(sh, f'CAL_R3_HB_{part + 1}_hires.jpg'), quality=88)
        save_small(S, os.path.join(sh, f'CAL_R3_HB_{part + 1}.jpg'))
    # 6 Kanon 直式重查
    ids = [i for i in L if i.startswith('CHK_kanon_')]
    cells = []
    for i in ids:
        p = ph(i)
        cells.append(labelled(os.path.join(CAL, L[i]['preview']),
                              [f"{p['cid']}｜{p['frame_label']}", f"框 {p['frame_mm']} mm｜{p['ppi_w']} ppi",
                               f"臉完整：{'是' if p['face']['complete_in_frame'] else '否'}｜臉最上緣 {p['face']['top_mm']} mm",
                               f"髮頂：{p['hair']['status_auto']}"], 520))
    S = grid(cells, 5, 'Kanon 直式重查｜train_01 女僕胸口開口（原圖已缺髮頂）在三種框、train_02 女僕與 #028 在統一框')
    S.save(os.path.join(sh, 'CAL_R3_kanon_V_check_hires.jpg'), quality=88)
    save_small(S, os.path.join(sh, 'CAL_R3_kanon_V_check.jpg'))

    # 7 100% 實際像素預覽（直接從 300 dpi 輸出檔裁，不縮放）
    pv = os.path.join(OUT, 'previews')
    os.makedirs(pv, exist_ok=True)
    for pid, box_mm, name in (('H_A_01_iris-chen', (110, 12, 200, 151), 'H_A_01_grid'),
                              ('V_U_01_iris-chen', (8, 146, 140, 200), 'V_U_01_grid'),
                              ('V_year_2027', (6, 36, 100, 110), 'V_year_top'),
                              ('H_B_01_iris-chen', (4, 118, 200, 151), 'H_B_01_strip'),
                              ('H_grid_09_yuna-kim', (8, 10, 110, 100), 'H_grid_09_small_photo'),
                              ('H_cover', (4, 40, 104, 100), 'H_cover_tiles')):
        im = Image.open(os.path.join(CAL, L[pid]['hires']))
        c = im.crop(tuple(int(round(v * MM)) for v in box_mm))
        S = Image.new('RGB', (c.width, c.height + 70), 'white')
        S.paste(c, (0, 70))
        ImageDraw.Draw(S).text((8, 8), f'{pid}｜100%＝300 dpi 實際像素（螢幕 100% 顯示 ≠ 印刷尺寸；不是印刷可讀性證明）｜範圍 {box_mm} mm', fill='black', font=f(26))
        S.save(os.path.join(pv, f'CAL_R3_100pct_{name}.jpg'), quality=90)

    # 8 清理：修前 100%｜修後 100%｜版面實際大小（從 300 dpi 輸出頁裁出同一區域）
    cl = json.load(open(os.path.join(CAL, 'data', 'cal_r3_cleanup_report.json')))['items']
    R = json.load(open(os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')))['items']
    cd = os.path.join(OUT, 'cleanup')
    for it in cl:
        cid = it['cid']
        src = it['src']
        orig = os.path.join(a.hf_dir, next(r for r in R if r['job_id'] == src[3:])['local']) if src.startswith('hf:') else os.path.join(ROOT, src)
        A = Image.open(orig).convert('RGB')
        B = Image.open(os.path.join(a.cache, it['clean_file'])).convert('RGB')
        W, H = A.size
        xs = [o['box_px'][0] for o in it['ops']] + [o['box_px'][2] for o in it['ops']]
        ys = [o['box_px'][1] for o in it['ops']] + [o['box_px'][3] for o in it['ops']]
        mx, my = int(0.04 * W), int(0.04 * H)
        box = (max(min(xs) - mx, 0), max(min(ys) - my, 0), min(max(xs) + mx, W), min(max(ys) + my, H))
        a_, b_ = A.crop(box), B.crop(box)
        panels = [(a_, '修前（原圖 100%）'), (b_, '修後（清理版 100%）')]
        used = [p for p in L.values() if p['group'] == 'main' for ph_ in p['photos'] if ph_['cid'] == cid and ph_['note'] is None]
        page = next((p for p in used if p['id'].startswith('V_U')), used[0] if used else None)
        if page:
            p = next(x for x in page['photos'] if x['cid'] == cid and x['note'] is None)
            cx0, cy0, cw, ch = p['crop_px']
            fx0, fy0, fx1, fy1 = p['frame_mm']
            k = (fx1 - fx0) / cw
            bx = (max(box[0], cx0), max(box[1], cy0), min(box[2], cx0 + cw), min(box[3], cy0 + ch))
            if bx[0] < bx[2] and bx[1] < bx[3]:
                mm = (fx0 + (bx[0] - cx0) * k, fy0 + (bx[1] - cy0) * k, fx0 + (bx[2] - cx0) * k, fy0 + (bx[3] - cy0) * k)
                pg = Image.open(os.path.join(CAL, page['hires'])).crop(tuple(int(round(v * MM)) for v in mm))
                panels.append((pg, f'版面實際大小：{page["id"]}\n（300 dpi 輸出頁，{mm[2] - mm[0]:.0f}×{mm[3] - mm[1]:.0f} mm）'))
        h = max(pn.height for pn, _ in panels)
        S = Image.new('RGB', (sum(pn.width + 20 for pn, _ in panels) + 20, h + 140), 'white')
        d = ImageDraw.Draw(S)
        d.text((10, 8), f'{cid}｜{it["why"]}', fill='black', font=f(26))
        x = 10
        for pn, lab in panels:
            S.paste(pn, (x, 120))
            d.multiline_text((x, 50), lab, fill='#333', font=f(22), spacing=6)
            x += pn.width + 20
        S.save(os.path.join(cd, f'{cid}_compare_hires.jpg'), quality=90)
        save_small(S, os.path.join(cd, f'{cid}_compare.jpg'), max_w=2400)
    print('ok')


if __name__ == '__main__':
    main()
