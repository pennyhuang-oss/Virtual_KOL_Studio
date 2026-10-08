#!/usr/bin/env python3
"""TASK-CAL-001 / R3 — 完整頁序與紙張模型（排到最後一張，核算張數）。

a. 編輯面順序：依廠商 2027 範本（橫式 8385／8364、直式 8404），列出全部 28／32 面。
b. 實體紙張正反面：
   H1（假設）：第 k 張紙（k＝1…N/2）＝面 2k−1（正）＋面 2k（背）。
   H2（示意）：封面單獨一張、背面空白；之後第 j 張紙（j＝2、3…）＝面 2j−2（正）＋面 2j−1（背），
       排到最後一面為止。需要的張數＝1＋ceil((N−1)/2)。
c. 翻頁後立架兩側可見面（上緣線圈、往後翻）：翻過 n 張時，前坡＝第 n+1 張的正面，背坡＝第 n 張的背面。
   兩者來自不同張紙；背面若與正面同向印刷，翻到背坡會上下顛倒（是否自動旋轉 180° 待廠商確認；本輪工作稿一律單面正向）。
輸出：data/cal_r3_pagemodel.json、CAL_13b_PAGE_MODEL.generated.md、r3/pagemodel/CAL_R3_pagemodel_{H,V}.jpg（含 _hires）
用法：python3 docs/calendar/tools/build_cal_r3_pagemodel.py
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

CAL = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(CAL, 'r3', 'pagemodel')
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
SPEC = {'H': {'sheets': 14, 'faces': 28, 'name': '橫式 200×151 mm'}, 'V': {'sheets': 16, 'faces': 32, 'name': '直式 140×200 mm'}}


def faces(kind):
    """回傳 [(面, 範本內容, R3 草稿內容)]。R3 草稿每月「照片面在前、大格面在後」（與 8364／8404 同序）。"""
    L = [(1, {'8385': '封面', '8364': '封面'} if kind == 'H' else {'8404': '封面'}, '封面草稿（品牌佔位）')]
    for m in range(1, 13):
        a, b = 2 * m, 2 * m + 1
        if kind == 'H':
            L.append((a, {'8385': f'{m} 月大格月曆面', '8364': f'{m} 月照片面（含小月曆）'}, f'{m} 月照片面（橫 A）'))
            L.append((b, {'8385': f'{m} 月照片面（照片＋單行日期條）', '8364': f'{m} 月大格月曆面'},
                      '1 月大格月曆面（代表）' if m == 1 else f'{m} 月大格月曆面（本輪未製作）'))
        else:
            L.append((a, {'8404': f'{m} 月照片面（照片＋日期條）'}, f'{m} 月照片面（直式統一框）'))
            L.append((b, {'8404': f'{m} 月大格月曆面'}, '12 月大格月曆面（代表）' if m == 12 else f'{m} 月大格月曆面（本輪未製作）'))
    if kind == 'H':
        L += [(26, {'8385': 'MEMO', '8364': 'MEMO'}, 'MEMO（本輪不製作）'),
              (27, {'8385': 'MEMO／裝飾底頁', '8364': 'MEMO／裝飾底頁'}, 'MEMO（本輪不製作；可放年曆）'),
              (28, {'8385': '條碼頁（不可編輯）', '8364': '條碼頁（不可編輯）'}, '條碼頁（廠商固定）')]
    else:
        L += [(n, {'8404': f'MEMO {n - 25}'}, 'MEMO（本輪不製作）') for n in range(26, 31)]
        L += [(31, {'8404': '2027 全年年曆'}, '2027 年曆（草稿）'), (32, {'8404': '條碼頁（不可編輯）'}, '條碼頁（廠商固定）')]
    return L


def h1(n):
    return [{'sheet': k, 'front': 2 * k - 1, 'back': 2 * k} for k in range(1, n // 2 + 1)]


def h2(n):
    S = [{'sheet': 1, 'front': 1, 'back': None}]
    f, j = 2, 2
    while f <= n:
        S.append({'sheet': j, 'front': f, 'back': f + 1 if f + 1 <= n else None})
        f += 2
        j += 1
    return S


def check(sheets, n, spec_sheets):
    seen = [x for s in sheets for x in (s['front'], s['back']) if x is not None]
    return {'sheets': len(sheets), 'spec_sheets': spec_sheets, 'faces_placed': len(seen),
            'all_faces_once': sorted(seen) == list(range(1, n + 1)), 'blank_sides': sum(s['back'] is None for s in sheets),
            'fits_spec': len(sheets) == spec_sheets and sorted(seen) == list(range(1, n + 1))}


def states(sheets):
    """翻過 n 張（n＝0…張數）時兩側可見面。"""
    out = []
    for n in range(0, len(sheets) + 1):
        front = sheets[n]['front'] if n < len(sheets) else None
        back = sheets[n - 1]['back'] if n >= 1 else None
        out.append({'flipped': n, 'front_slope': front, 'back_slope': back})
    return out


def font(s):
    return ImageFont.truetype(FONT, s)


def draw(kind, F, m1, m2):
    content = {n: draft for n, _, draft in F}
    rows = len(m1['sheets'])
    W, cw, ch = 1900, 420, 64
    H = 150 + rows * (ch + 10) + 120 + (len(m2['sheets']) // 2 + 1) * 40 + 120
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)
    d.text((20, 15), f'{SPEC[kind]["name"]}｜{SPEC[kind]["faces"]} 面／規格 {SPEC[kind]["sheets"]} 張｜紙張模型（全部是假設，拼版與背面方向待廠商確認）', fill='black', font=font(30))
    d.text((20, 60), 'H1：第 k 張＝面 2k-1（正）＋面 2k（背）　｜　右欄：翻過 n 張時立架兩側可見（前坡＝第 n+1 張正面；背坡＝第 n 張背面，背面同向印刷會上下顛倒）', fill='#333', font=font(20))
    y = 100
    d.text((20, y), '張', fill='black', font=font(22))
    d.text((90, y), '正面（面號｜R3 草稿）', fill='black', font=font(22))
    d.text((90 + cw + 20, y), '背面（面號｜R3 草稿）', fill='black', font=font(22))
    d.text((90 + 2 * cw + 60, y), '翻過 n 張後：前坡｜背坡', fill='black', font=font(22))
    y += 34
    d.text((90 + 2 * cw + 60, y), 'n=0：前坡 面1（封面）｜背坡 —（立架背板）', fill='#333', font=font(18))
    y += 30
    st = {s['flipped']: s for s in m1['states']}
    for s in m1['sheets']:
        k = s['sheet']
        d.text((30, y + 18), f'{k}', fill='black', font=font(24))
        for i, face in enumerate((s['front'], s['back'])):
            x = 90 + i * (cw + 20)
            fill = '#e8f1ff' if i == 0 else '#fff1e0'
            if 'MEMO' in content[face] or '條碼' in content[face]:
                fill = '#eeeeee'
            d.rectangle((x, y, x + cw, y + ch), fill=fill, outline='#888')
            d.text((x + 8, y + 6), f'面 {face}', fill='black', font=font(20))
            d.text((x + 8, y + 34), content[face], fill='#222', font=font(18))
        sv = st[k]
        fr = '—' if sv['front_slope'] is None else f"面{sv['front_slope']}"
        bk = '—' if sv['back_slope'] is None else f"面{sv['back_slope']}"
        d.text((90 + 2 * cw + 60, y + 18), f'n={k}：前坡 {fr}｜背坡 {bk}（上下顛倒？待確認）', fill='#333', font=font(18))
        y += ch + 10
    c = m1['check']
    d.text((20, y + 10), f"H1 核算：{c['sheets']} 張＝規格 {c['spec_sheets']} 張；{c['faces_placed']} 面全部各出現一次＝{'是' if c['all_faces_once'] else '否'} → 符合張數（仍是假設）", fill='#0a6', font=font(22))
    y += 60
    c2 = m2['check']
    d.text((20, y), f"H2（封面單張、背面空白）：需要 {c2['sheets']} 張 ≠ 規格 {c2['spec_sheets']} 張（最後一張＝面 {m2['sheets'][-1]['front']}／背面空白）→ 不符合目前規格的示意", fill='#c00', font=font(22))
    y += 40
    toks = [f"{s['sheet']}:{s['front']}/{s['back'] or '空白'}" for s in m2['sheets']]
    for i in range(0, len(toks), 12):
        d.text((20, y), '　'.join(toks[i:i + 12]), fill='#a00', font=font(18))
        y += 30
    img = img.crop((0, 0, W, y + 20))
    os.makedirs(OUT, exist_ok=True)
    hi = os.path.join(OUT, f'CAL_R3_pagemodel_{kind}_hires.jpg')
    img.save(hi, quality=92)
    pv = img.copy()
    pv.thumbnail((1600, 3000))
    pv.save(os.path.join(OUT, f'CAL_R3_pagemodel_{kind}.jpg'), quality=85)


def main():
    model = {}
    md = ['# CAL_13b — 完整頁序與紙張模型（程式產生，請勿手改）', '',
          '> 由 `docs/calendar/tools/build_cal_r3_pagemodel.py` 產生。**H1、H2 都是假設**；實際拼版、條碼面印在哪、背面是否旋轉 180° 都待廠商確認。',
          '> 本輪工作稿一律**單面正向**，沒有自行旋轉任何交稿面。', '']
    for kind in ('H', 'V'):
        n, ns = SPEC[kind]['faces'], SPEC[kind]['sheets']
        F = faces(kind)
        m1 = {'sheets': h1(n)}
        m1['check'] = check(m1['sheets'], n, ns)
        m1['states'] = states(m1['sheets'])
        m2 = {'sheets': h2(n)}
        m2['check'] = check(m2['sheets'], n, ns)
        model[kind] = {'spec': SPEC[kind], 'faces': [{'face': a, 'template': b, 'r3_draft': c} for a, b, c in F], 'H1': m1, 'H2': m2}
        tpl = list(F[0][1].keys())
        md += [f"## {SPEC[kind]['name']}：{n} 面、規格 {ns} 張", '', '### a. 編輯面順序', '',
               '| 面 | ' + ' | '.join(f'範本 {t}' for t in tpl) + ' | R3 草稿 |', '|---|' + '---|' * len(tpl) + '---|']
        for a, b, c in F:
            md.append(f'| {a} | ' + ' | '.join(b[t] for t in tpl) + f' | {c} |')
        c = m1['check']
        md += ['', '### b. 實體紙張正反面（H1 假設：第 k 張＝面 2k−1／2k）', '',
               f"核算：{c['sheets']} 張（規格 {c['spec_sheets']}）；放入 {c['faces_placed']} 面，1…{n} 各一次＝{'是' if c['all_faces_once'] else '否'}；空白面 {c['blank_sides']} → **{'符合張數' if c['fits_spec'] else '不符合'}（仍是假設）**", '',
               '| 張 | 正面 | 背面 |', '|---|---|---|']
        draft = {a: cc for a, _, cc in F}
        for s in m1['sheets']:
            md.append(f"| {s['sheet']} | 面 {s['front']}｜{draft[s['front']]} | 面 {s['back']}｜{draft[s['back']]} |")
        md += ['', '### c. 翻頁後立架兩側可見面（H1）', '',
               '前坡＝翻過 n 張後最上面那張的正面；背坡＝剛翻過去那張的背面。兩者**不在同一張紙**。背坡內容若與正面同向印刷會上下顛倒（待廠商確認是否自動旋轉）。', '',
               '| 翻過 n 張 | 前坡可見 | 背坡可見 |', '|---|---|---|']
        for s in m1['states']:
            fr = '—（只剩立架）' if s['front_slope'] is None else f"面 {s['front_slope']}｜{draft[s['front_slope']]}"
            bk = '—（立架背板）' if s['back_slope'] is None else f"面 {s['back_slope']}｜{draft[s['back_slope']]}"
            md.append(f"| {s['flipped']} | {fr} | {bk} |")
        c2 = m2['check']
        md += ['', '### H2（封面單張、背面空白）——**不符合目前規格的示意**', '',
               f"定義：第 1 張＝面 1（封面）＋空白；第 j 張（j≥2）＝面 2j−2（正）＋面 2j−1（背）。排到最後一面需要 1＋ceil(({n}−1)/2)＝**{c2['sheets']} 張**，規格是 {ns} 張；"
               f"最後一張只有面 {m2['sheets'][-1]['front']}（條碼面），背面空白。→ 多一張紙，**不列為可行方案**，只用來說明「拼版不同，同時可見的面就不同」。", '',
               '| 張 | 正面 | 背面 |', '|---|---|---|']
        for s in m2['sheets']:
            md.append(f"| {s['sheet']} | 面 {s['front']} | {'空白' if s['back'] is None else '面 ' + str(s['back'])} |")
        md.append('')
        draw(kind, F, m1, m2)
    json.dump({'generated_by': 'docs/calendar/tools/build_cal_r3_pagemodel.py', 'models': model},
              open(os.path.join(CAL, 'data', 'cal_r3_pagemodel.json'), 'w'), ensure_ascii=False, indent=1)
    open(os.path.join(CAL, 'CAL_13b_PAGE_MODEL.generated.md'), 'w').write('\n'.join(md))
    for k in ('H', 'V'):
        print(k, model[k]['H1']['check'], model[k]['H2']['check'])


if __name__ == '__main__':
    main()
