#!/usr/bin/env python3
"""TASK-CAL-001 / R2 — 紙張模型：編輯器面號 → 實體紙張正反面 → 三角立架翻頁時兩側看到哪一面。

兩個拼版假設（廠商未確認，全部標「假設」）：
  H1：第 k 張紙＝面 2k−1（正）＋面 2k（背）
  H2：面 1 為封面單獨一張（背面空白或底板），之後第 k 張＝面 2k（正）＋面 2k+1（背）——用來示範「拼版不同，同時可見的面就不同」
面的內容沿用廠商 2027「祥羊迎春」範本：橫式（8385）＝面2 一月大格、面3 一月照片…；直式（8404）＝面2 一月照片、面3 一月大格…
另外標出：上緣線圈翻到背坡後，背面若與正面同向印刷會上下顛倒（是否自動旋轉 180°：待廠商確認）。
用法：python3 docs/calendar/tools/build_cal_r2_papermodel.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
OUT = os.path.join(ROOT, 'docs', 'calendar', 'r2', 'papermodel')
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'


def font(n):
    return ImageFont.truetype(FONT, n)


def content(kind, face, total):
    if face == 1:
        return '封面'
    if face == total:
        return '條碼頁'
    if 2 <= face <= 25:
        m = face // 2
        first, second = ('大格', '照片') if kind == 'H' else ('照片', '大格')
        return f'{m}月{first if face % 2 == 0 else second}'
    if kind == 'V' and face == 31:
        return '年曆'
    return 'MEMO'


def sheets(hyp, total):
    if hyp == 'H1':
        return [(2 * k - 1, 2 * k) for k in range(1, total // 2 + 1)]
    s = [(1, None)]
    f = 2
    while f <= total:
        s.append((f, f + 1 if f + 1 <= total else None))
        f += 2
    return s


def visible(sh, flipped):
    """翻過 flipped 張後：前坡＝下一張的正面；背坡最上層＝最後翻過那張的背面。"""
    front = sh[flipped][0] if flipped < len(sh) else None
    back = sh[flipped - 1][1] if flipped > 0 else None
    return front, back


def draw_model(kind, total):
    W, H = 1900, 1320
    S = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(S)
    d.text((20, 14), f'紙張模型（{ "橫式 28 面／14 張" if kind == "H" else "直式 32 面／16 張"}）｜面的內容依廠商 2027 祥羊迎春範本｜全部為「假設」，待廠商確認拼版與背面方向',
           fill='black', font=font(26))
    y = 70
    for hyp, desc in (('H1', 'H1：第 k 張＝面 2k-1（正）＋面 2k（背）'), ('H2', 'H2：封面單獨一張，之後第 k 張＝面 2k（正）＋面 2k+1（背）')):
        sh = sheets(hyp, total)
        d.text((20, y), desc, fill='#b00' if hyp == 'H1' else '#06c', font=font(24))
        y += 40
        # 前 5 張紙
        x = 20
        for i, (fr, bk) in enumerate(sh[:5], 1):
            d.rectangle((x, y, x + 330, y + 120), outline='black', width=2)
            d.text((x + 8, y + 6), f'第 {i} 張紙', fill='#555', font=font(18))
            d.text((x + 8, y + 36), f'正：面{fr}  {content(kind, fr, total)}', fill='black', font=font(21))
            d.text((x + 8, y + 74), f'背：面{bk}  {content(kind, bk, total)}' if bk else '背：空白／底板', fill='black', font=font(21))
            x += 360
        y += 140
        # 翻頁狀態
        x = 20
        for flipped in range(0, 4):
            fr, bk = visible(sh, flipped)
            d.rectangle((x, y, x + 440, y + 230), outline='#999', width=2)
            d.text((x + 10, y + 8), f'翻過 {flipped} 張後', fill='#555', font=font(19))
            # 三角立架側視圖
            cx, base, top = x + 220, y + 130, y + 45
            d.line((cx - 80, base, cx, top), fill='black', width=4)
            d.line((cx, top, cx + 80, base), fill='black', width=4)
            d.ellipse((cx - 8, top - 8, cx + 8, top + 8), outline='black', width=3)
            d.text((x + 12, y + 150), f'前坡：面{fr}｜{content(kind, fr, total) if fr else "—"}', fill='#b00', font=font(20))
            d.text((x + 12, y + 186), f'背坡：{("面" + str(bk) + "｜" + content(kind, bk, total)) if bk else "底板"}', fill='#06c', font=font(20))
            x += 470
        y += 260
    h2 = '本月大格＋上個月照片' if kind == 'H' else '本月照片＋上個月大格'
    h1same = '本月照片＋下個月大格' if kind == 'H' else '本月大格＋下個月照片'
    for i, line in enumerate(['背面方向：紙張以上緣線圈為軸翻到背坡後，若背面與正面「同向」印刷，背坡看到的內容會上下顛倒，',
                              '需要「天地相反（頭對腳）」印刷才正。廠商編輯器每一面都正向顯示，是否自動旋轉：待廠商確認。',
                              f'H1：「同月照片＋同月大格」分在立架兩側同時可見，但兩者不在同一張紙（同一張紙的正反面是「{h1same}」）。',
                              f'H2：同時可見的是「{h2}」。哪一個成立取決於廠商實際拼版，本輪不下結論。']):
        d.text((20, y + 4 + i * 34), line, fill='black', font=font(21))
    S = S.crop((0, 0, W, y + 4 + 4 * 34 + 16))
    p = os.path.join(OUT, f'CAL_R2_papermodel_{kind}.jpg')
    S.save(p, quality=88)
    return p


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    print(draw_model('H', 28), draw_model('V', 32))
