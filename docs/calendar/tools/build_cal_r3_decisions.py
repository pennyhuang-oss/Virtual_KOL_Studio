#!/usr/bin/env python3
"""TASK-CAL-001 / R3 — Penny 決策包圖片（四題＋各月選項附表）。每張有可放大的 _hires 版與 < 1 MB 預覽；
每張小圖都標選項代碼與圖片 ID，讓回覆可以寫代碼，不必描述「左邊第二張」。
用法：python3 docs/calendar/tools/build_cal_r3_decisions.py --hf-dir <原圖快取> --cache <清理輸出資料夾>
"""
import argparse
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
import build_cal_r3_pages as P  # noqa: E402

CAL = P.CAL
OUT = os.path.join(CAL, 'r3', 'decisions')
FONT = P.FONT_CJK


def f(n):
    return ImageFont.truetype(FONT, n)


def tile(im, code, lines, h, rec=False):
    im = im.copy()
    im.thumbnail((h * 2, h))
    head = 34 + 28 * len(lines)
    c = Image.new('RGB', (max(im.width, 300), im.height + head + 6), '#fff6d6' if rec else 'white')
    d = ImageDraw.Draw(c)
    d.text((6, 4), code + ('　★推薦' if rec else ''), fill='#b00000' if rec else 'black', font=f(26))
    for i, s in enumerate(lines):
        d.text((6, 36 + i * 28), s, fill='#333', font=f(20))
    c.paste(im, (0, head))
    return c


def row(cells, title, gap=14):
    h = max(c.height for c in cells)
    r = Image.new('RGB', (sum(c.width + gap for c in cells) + 260, h + 10), '#e9e9e9')
    ImageDraw.Draw(r).multiline_text((12, 12), title, fill='black', font=f(28), spacing=8)
    x = 260
    for c in cells:
        r.paste(c, (x, 5))
        x += c.width + gap
    return r


def sheet(rows, title, note, name):
    W = max(r.width for r in rows)
    per = max(20, (W - 40) // 23)
    lines = [note[i:i + per] for i in range(0, len(note), per)]
    top = 64 + 32 * len(lines)
    H = sum(r.height + 12 for r in rows) + top + 10
    S = Image.new('RGB', (W, H), '#d0d0d0')
    d = ImageDraw.Draw(S)
    d.text((14, 12), title, fill='black', font=f(34))
    for i, ln in enumerate(lines):
        d.text((14, 60 + 32 * i), ln, fill='#333', font=f(22))
    y = top
    for r in rows:
        S.paste(r, (0, y))
        y += r.height + 12
    S.save(os.path.join(OUT, f'{name}_hires.jpg'), quality=90)
    pv = S.copy()
    pv.thumbnail((2000, 6000))
    q = 86
    while True:
        pv.save(os.path.join(OUT, f'{name}.jpg'), quality=q)
        if os.path.getsize(os.path.join(OUT, f'{name}.jpg')) < 1_000_000 or q <= 55:
            break
        q -= 5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hf-dir', required=True)
    ap.add_argument('--cache', required=True)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    picks = json.load(open(os.path.join(CAL, 'data', 'cal_r3_picks.json')))
    J = {c['cid']: c for c in json.load(open(os.path.join(CAL, 'data', 'cal_r2_judgments.json')))['candidates']}
    R = json.load(open(os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')))['items']
    clean = {c['cid']: c for c in json.load(open(os.path.join(CAL, 'data', 'cal_r3_cleanup_report.json')))['items']}
    L = {p['id']: p for p in json.load(open(os.path.join(CAL, 'data', 'cal_r3_layout_report.json')))['pages']}
    cache = {}

    def src(cid):
        if cid not in cache:
            cache[cid] = P.Source(cid, J, R, clean, a.hf_dir, a.cache)
        return cache[cid]

    def head(cid):
        s = src(cid)
        x, y, w, h = P.head_tile(s)
        x, y = max(0, min(x, s.W - w)), max(0, min(y, s.H - h))
        return s.img.crop((x, y, x + w, y + h))

    def full(cid):
        return src(cid).img

    months = picks['months']
    # A 名單
    alt = picks['roster_compare']

    def roster(swap):
        cells = []
        for M in months:
            cid, name = M['V'], M['en'].split()[0]
            if swap and M['m'] == 5:
                cid, name = alt['may_alt_cid'], 'Ananya'
            cells.append(tile(head(cid), f'{M["m"]} 月 {name}', [cid], 230, rec=False))
        g = Image.new('RGB', (4 * (cells[0].width + 8), 3 * (max(c.height for c in cells) + 8)), 'white')
        for i, c in enumerate(cells):
            g.paste(c, ((i % 4) * (cells[0].width + 8), (i // 4) * (max(x.height for x in cells) + 8)))
        return g
    A0 = tile(roster(False), 'A0', ['沿用 R2 的 12 人（5 月 Somi）'], 1100, rec=True)
    A1 = tile(roster(True), 'A1', ['只把 5 月換成 Ananya（其餘不變）'], 1100)
    sheet([row([A0, A1], '決策 A\n名單')], '決策 A｜名單：整組放在一起看差異（封面用的同一張頭像）',
          '推薦 A0。A1 只是選項：Ananya 沒有臉部量測，不承諾不碰撞；名單暫留理由是目視與展示取捨，不是「已通過辨識度」。', 'CAL_R3_decide_A_roster')

    # B 尺度與造型
    r1 = [tile(full('iris_V'), 'B-S1 日常甜美', ['iris_V 街拍細肩帶＋牛仔短裙'], 520),
          tile(full('iris_H'), 'B-S2 微性感', ['iris_H 粉色抹胸露肩'], 520, rec=True),
          tile(Image.open(os.path.join(P.ROOT, 'kols/iris-chen/images/daily_sexy_night_v2_lingerie/02_mirror_burgundy_teddy_selfie.png')).convert('RGB'),
               'B-S3 內衣', ['只作尺度參考；沒有選作任何月份'], 520)]
    r2 = [tile(full('kanon_alt028'), 'B-K1 非女僕', ['kanon_alt028（#028）橫直同圖'], 520, rec=True),
          tile(full('kanon_H'), 'B-K2 女僕', ['kanon_H（train_02）橫直同圖'], 520),
          tile(full('kanon_V'), '參考：女僕胸口開口', ['kanon_V（train_01）原圖已缺髮頂'], 520)]
    r3 = [tile(full('angel_H'), 'B-N1 護理師（橫式）', ['angel_H（train_02）'], 520, rec=True),
          tile(full('angel_alt004'), 'B-N2 河岸（橫式）', ['angel_alt004（#004）右側路人未清理'], 520),
          tile(full('angel_V'), '直式固定', ['angel_V 緞面細肩帶（兩案都用）'], 520)]
    sheet([row(r1, '尺度\n（同一人 Iris）'), row(r2, 'Kanon\n女僕要不要用'), row(r3, 'Angel\n護理師要不要用')],
          '決策 B｜尺度與造型：同一個人的實際既有照片', '推薦 B-S2＋B-K1＋B-N1。Kanon 與 Angel 分開選，不用一個「制服總開關」。', 'CAL_R3_decide_B_scale_style')

    # C 版面
    def pg(pid, code, lines, h=560, rec=False):
        return tile(Image.open(os.path.join(CAL, L[pid]['preview'])), code, lines, h, rec)

    def ppi(pid):
        return L[pid]['photos'][0]['ppi_w']
    c1 = [pg('H_A_01_iris-chen', 'C1 橫 A 半版', [f'Iris 1 月｜{ppi("H_A_01_iris-chen")} ppi'], 520, True),
          pg('H_B_01_iris-chen', 'C2 橫 B 192×104', [f'Iris 1 月｜{ppi("H_B_01_iris-chen")} ppi（12 位中最高）'], 520)]
    c2 = []
    for pid, nm in (('vicky-lin', 'Vicky 6 月'), ('rin-ayase', 'Rin 11 月')):
        M = next(x for x in months if x['pid'] == pid)
        u, v = f'V_U_{M["m"]:02d}_{pid}', f'V_A_{M["m"]:02d}_{pid}'
        c2 += [pg(u, 'C1 直式統一框', [f'{nm}｜{ppi(u)} ppi'], 640, True), pg(v, 'C3 原直 A', [f'{nm}｜{ppi(v)} ppi'], 640)]
    hb = sorted(((L[f'H_B_{M["m"]:02d}_{M["pid"]}']['photos'][0]['ppi_w'], M['en'].split()[0]) for M in months), reverse=True)
    sheet([row(c1, '橫式'), row(c2, '直式')], '決策 C｜版面（實際樣張，ppi＝實際裁切原生像素）',
          '推薦 C1。橫 B 逐張：' + '、'.join(f'{n} {p}' for p, n in hb) + '（ppi）。300 ppi 是專案工作目標，不是廠商已確認的門檻。',
          'CAL_R3_decide_C_layout')

    # D 品牌與收件對象
    d1 = [pg('H_cover', 'D 橫式封面（佔位）', ['品牌、標語都是佔位文字'], 520), pg('V_cover', 'D 直式封面（佔位）', ['未放 Logo、QR'], 700)]
    sheet([row(d1, '決策 D\n收件對象\n與品牌')], '決策 D｜收件對象、品牌名稱、Logo、QR（未提供前一律佔位，不自行填最終品牌）',
          '要知道：給誰看（潛在客戶／合作品牌、粉絲周邊、內部留存）、品牌名稱、要不要 Logo、要不要 QR（連到哪裡）。', 'CAL_R3_decide_D_brand')

    # 附表：各月選項
    rows = []
    for M in months:
        if not M['options']:
            continue
        same = M['H'] == M['V']
        cells = [tile(full(M['H']), f'{M["m"]} 月推薦（{"橫直同圖" if same else "橫"}）', [M['H']], 380, True)]
        if M['V'] != M['H']:
            cells.append(tile(full(M['V']), f'{M["m"]} 月推薦（直）', [M['V']], 380, True))
        sp = picks['grid_faces']['H']
        for o in M['options']:
            for cid in o['cids']:
                im = full(cid)
                if cid == sp['small_photo']:  # 9b 是小框用圖：顯示實際小框裁切
                    c = sp['small_crop_frac']
                    fx0, fy0, fx1, fy1 = sp['small_frame_mm']
                    x0, y0 = int(c[0] * im.width), int(c[1] * im.height)
                    cw = int((c[2] - c[0]) * im.width)
                    im = im.crop((x0, y0, x0 + cw, y0 + int(round(cw * (fy1 - fy0) / (fx1 - fx0)))))
                n = o['note']
                cells.append(tile(im, o['code'], [cid, n[:19], n[19:38]], 380))
        rows.append(row(cells, f'{M["m"]} 月\n{M["en"].split()[0]}'))
    sheet(rows, '附表｜各月推薦與選項（代碼可直接寫在回覆裡）', '沒列的月份只有一組推薦。選項的清理狀態寫在小字；未清理的選項若被選中，下一輪再清理。', 'CAL_R3_decide_options')
    print('ok')


if __name__ == '__main__':
    main()
