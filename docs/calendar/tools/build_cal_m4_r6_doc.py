#!/usr/bin/env python3
"""TASK-CAL-001／M-4（R6）— 由 data/cal_m4_r6_replan.json（執行者分析與提案）、data/cal_m4_owner_r6.json（Owner 決定逐字）
與 data/cal_m3_shoot_plan.json（現行 24 套企劃）產生：
  CAL_23_M4_R6_REPLAN.md   第一批全數退回後的全套寫真企劃重審：實際看圖比較（Iris 與 5 張退回照片）、24 套逐套審查、
                           共用規則修訂、重建稿（第一批 5 張附 prompt 草稿）、生成前後審美把關、待 Penny 決定
產生器核對：24 套都有判斷且只有 V-Iris 保留；每個非保留都有重建稿；Penny 的每個重點都有對應的證據與 A／B／C 歸因；
第一批 prompt 的身分句與 CAL_21 逐字相同（canon 不改），且沒有器材字、占比百分比、身材展示句與「fashion editorial」；
舊規則的受影響套數由企劃資料實際計算，且受影響的套都不是「保留」（V-Iris 已接受照片除外）。
只排版既有文字，不新增內容；沒有呼叫任何生成服務。
用法：python3 docs/calendar/tools/build_cal_m4_r6_doc.py           # 產生
      python3 docs/calendar/tools/build_cal_m4_r6_doc.py --check   # 核對文件與資料一致
"""
import json
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
CAL = os.path.join(ROOT, 'docs', 'calendar')
DATA = os.path.join(CAL, 'data')
OUT = os.path.join(CAL, 'CAL_23_M4_R6_REPLAN.md')
FIRST_LINE = 'TASK-CAL-001／M-4／R6｜全套寫真企劃重審｜送審報告'
BATCH1 = ['V-tammy-chou', 'V-rin-ayase', 'V-somi-oh', 'H-yerin-han', 'H-jia-seo']
EQUIP = re.compile(r'reflector|softbox|soft box|key light|fill light|\bfill\b|ring light|strobe|flash|light stand|out of frame|umbrella|scrim|diffuser|studio light', re.I)
LEVELS = ('保留', '局部重寫', '整案重寫')


def cell(s):
    return str(s).replace('|', '／').replace('\n', ' ')


def table(head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    return out + ['| ' + ' | '.join(cell(c) for c in r) + ' |' for r in rows]


def load(name):
    return json.load(open(os.path.join(DATA, name), encoding='utf-8'))


def current(s):
    o = '、'.join(f'{k}：{v}' for k, v in s['outfit'].items())
    lt = '；'.join(f'{k}：{v}' for k, v in s['light'].items())
    return f"{s['scene']}｜服裝｜{o}｜姿勢｜{s['pose']}｜手｜{s['hands']}｜景別與相機｜{s['cam']['line']}｜光｜{lt}｜構圖｜{s['cam']['comp']['zh']}"


def affected(P, k, manual):
    """舊規則實際影響到哪些套（從企劃資料計算；無法計算的用資料檔列出的清單）。"""
    S = P['sets']
    txt = lambda s, *ks: json.dumps([s[x] for x in ks], ensure_ascii=False)
    f = {
        'occupancy': lambda s: 'fills about' in s['prompt'],
        'body_first': lambda s: bool(re.search('胸|腰|臀|腿', s['cam']['purpose']['zh'])),
        'fill_light': lambda s: bool(re.search('反光板|柔光箱|畫面外', txt(s, 'light'))),
        'low_angle': lambda s: '輕仰' in s['cam']['angle']['zh'],
        'hand_on_hip': lambda s: bool(re.search('插腰|腰頭兩側|在肩高', s['hands'])),
        'big_prop': lambda s: bool(re.search('球車|繫船柱|吊床|長椅|貴妃椅|欄杆|吧台', txt(s, 'scene', 'pose', 'hands'))),
        'shoes_rule': lambda s: '不入鏡' in json.dumps(s['outfit'], ensure_ascii=False) and '鞋' in json.dumps(s['outfit'], ensure_ascii=False),
        'editorial_line': lambda s: 'fashion editorial' in s['prompt'],
    }.get(k)
    return [s['id'] for s in S if f(s)] if f else manual


def render(P, O, X):
    S = {s['id']: s for s in P['sets']}
    order = [s['id'] for s in P['sets']]
    V = {r['id']: r for r in X['review']}
    W = {w['id']: w for w in X['rewrites']}
    prep = {x['id']: x for x in load('cal_m4_batch1_prep.json')['sets']}
    # ---- 核對 ----
    assert X['round'] == 'M-4 R6' and O['decision']['batch1'] == {s: 'Penny 退回／待重規劃' for s in BATCH1}
    assert [r['id'] for r in X['review']] == order and len(order) == 24
    assert all(V[i]['verdict'] in LEVELS for i in order) and [i for i in order if V[i]['verdict'] == '保留'] == ['V-iris-chen'], '只有 V-Iris 保留'
    assert all(V[i]['verdict'] == '整案重寫' for i in BATCH1), '第一批 5 張整案重寫'
    assert set(W) == {i for i in order if V[i]['verdict'] != '保留'} and all(W[i]['level'] == V[i]['verdict'] for i in W)
    for w in X['rewrites']:
        for k in ('picture', 'hierarchy', 'outfit', 'action', 'light', 'background', 'frame'):
            assert w[k].strip(), (w['id'], k)
        assert all(w['framing'][k].strip() for k in ('shot', 'camera', 'position', 'occupancy')) and w['risks'], w['id']
        assert re.search('設計參考|近景', w['framing']['occupancy']), w['id']
        for m in re.finditer('反光板|柔光箱|補光|畫面外', w['light']):  # 只能出現在「拿掉／不加」之後
            assert re.search('(拿掉|不加)[^。；]*$', w['light'][:m.start()]), (w['id'], w['light'])
    for i in BATCH1:
        p = W[i]['prompt']
        ident = prep[i]['prompt'][:prep[i]['prompt'].index(' She wears')]
        assert p.startswith(ident + ' She wears') and p.endswith(X['end_line']), f'{i}：身分句必須與 CAL_21 逐字相同'
        assert not EQUIP.search(p) and 'fills about' not in p and '%' not in p and 'Emphasis' not in p and 'fashion editorial' not in p, i
        assert 'Shot:' in p and 'Camera:' in p and 'Light:' in p and 'Moment:' in p, i
    assert set(W) - set(BATCH1) and not any('prompt' in W[i] for i in W if i not in BATCH1), '本輪只有第一批附 prompt 草稿'
    for ph in X['photos']:
        own = O['owner_points'][ph['set']]
        items = [t for t in re.split('、|，但', re.sub(r'\s+', '', own.split('：', 1)[1]).rstrip('。'))]
        pts = [p['point'] for p in ph['points']]
        assert pts == items, (ph['set'], pts, items)
        assert all(p['cause'] in ('A', 'B', 'C', '—') and p['evidence'] and p['plan'] for p in ph['points']), ph['set']
        assert set(ph['dims']) == set(X['dims']), ph['set']
    assert set(X['iris']['dims']) == set(X['dims'])
    aff = {}
    for r in X['old_rules']:
        a = affected(P, r['k'], r.get('sets', []))
        assert a, r['k']
        assert all(V[i]['verdict'] != '保留' for i in a if i != 'V-iris-chen'), r['k']
        aff[r['k']] = a
    assert X['counts'] == {'generated': 0, 'retouched': 0, 'trainings': 0, 'paid': 0, 'deploys': 0}
    cnt = {lv: [i for i in order if V[i]['verdict'] == lv] for lv in LEVELS}

    # ---- 排版 ----
    L = [FIRST_LINE, '', '# CAL_23 — M-4 R6 第一批全數退回與全套寫真企劃重審', '',
         f"> 資料檔：`data/cal_m4_r6_replan.json`（{X['version']}，{X['written_on']}；執行者分析與提案）、`data/cal_m4_owner_r6.json`（Owner 決定與主管指令逐字）、`data/cal_m3_shoot_plan.json`（{P['version']}；現行 24 套）。本文件由 `tools/build_cal_m4_r6_doc.py` 產生。",
         f"> **狀態：提案，待主管覆核。** 採用前，`cal_m3_shoot_plan.json` 的 24 套原文不改。本輪生成 {X['counts']['generated']}、修圖 {X['counts']['retouched']}、訓練 {X['counts']['trainings']}、付費操作 {X['counts']['paid']}、部署 {X['counts']['deploys']}。以下分析是執行者自查，不是主管獨立覆核，也不是 Penny 接受。", '',
         '## 0. Owner 決定（摘要；逐字原文見 `data/cal_m4_owner_r6.json`）', '',
         f"- 第一批：{O['decision']['batch1_summary']}"]
    L += [f"- {s}：{v}" for s, v in O['decision']['batch1'].items()]
    L += [f"- Iris：{O['decision']['iris']}", f"- 範圍：{O['decision']['scope']}", f"- M-4 R5：{O['decision']['r5_status']}", f"- 限制：{O['decision']['limits']}",
          f"- 原始回饋：{O['page_copy']['note']}", '',
          '**Penny 逐張重點（主管轉交，逐字）：**', '']
    L += [f"- {v.replace(chr(10), '').replace('  ', '')}" for v in O['owner_points'].values()]
    L += ['', '## 1. 實際看圖的檔案', '']
    L += table(['套別', '實際打開的檔案'], [[v['set'], '；'.join(v['files'])] for v in X['viewed']])
    I = X['iris']
    L += ['', '## 2. Iris（已接受）：為什麼成立', '', I['why_works'], '']
    L += table(['維度', 'V-Iris'], [[d, I['dims'][d]] for d in X['dims']])
    L += ['', '**可延續的品質原則（不是內容模板）：**', ''] + [f'{n}. {t}' for n, t in enumerate(I['keep'], 1)]
    L += ['', f"**不複製：** {I['not_copy']}", '', f"**Iris 的弱點（不改）：** {I['weak']}", '',
          '## 3. 5 張退回照片：實際看圖比較與歸因', '',
          '歸因：A＝原企劃已經造成問題；B＝生成結果偏離原企劃；C＝兩者共同造成。只引用照片上看得到的證據與企劃原文，不推測模型內部原因。', '']
    for n, ph in enumerate(X['photos'], 1):
        L += [f"### 3.{n} {ph['name']}｜{ph['set']}", '', f"**第一眼：** {ph['first_look']}", '']
        L += table(['維度', '這張', 'Iris 的做法'], [[d, ph['dims'][d], I['dims'][d]] for d in X['dims']])
        L += ['', '**Penny 指出的重點：**', '']
        L += table(['重點', '照片上的證據', '對應的企劃內容', '歸因'], [[p['point'], p['evidence'], p['plan'], p['cause']] for p in ph['points']])
        L += ['', f"**整體歸因：** {ph['attribution']}", '']
    L += ['## 4. 共用規則', '', '### 4.1 造成問題的舊規則（受影響套數由企劃資料計算）', '']
    L += table(['舊規則', '位置', '問題', '受影響', '套別'], [[r['rule'], r['where'], r['problem'], len(aff[r['k']]), '、'.join(aff[r['k']])] for r in X['old_rules']])
    L += ['', '### 4.2 修訂後的共用規則（所有重建稿都依此）', '']
    L += table(['編號', '規則', '內容'], [[r['id'], r['title'], r['text']] for r in X['new_rules']])
    L += ['', '## 5. 24 套逐套審查', '', f"結論：保留 {len(cnt['保留'])}（{'、'.join(cnt['保留'])}）；局部重寫 {len(cnt['局部重寫'])}；整案重寫 {len(cnt['整案重寫'])}（{'、'.join(cnt['整案重寫'])}）。", '',
          '「保留」＝符合本輪要求；「局部重寫」＝保留場景與服裝方向，改占比、姿勢、相機或光線；「整案重寫」＝場景、主要道具、服裝或構圖要重做。', '']
    L += table(['月份', '套別', '景別與相機（現行）', '結論', '理由'],
               [[f"{S[i]['month']} 月", i, S[i]['cam']['line'], V[i]['verdict'], V[i]['why']] for i in sorted(order, key=lambda i: (i[0], S[i]['month']))])
    for i in sorted(order, key=lambda i: (i[0], S[i]['month'])):
        s, v = S[i], V[i]
        L += ['', f"### {i}｜{s['name']}｜{s['month']} 月｜{s['ratio']}｜{v['verdict']}", '']
        L += table(['項目', '內容'], [
            ['1. 現行構想', current(s)],
            ['　來源位置', f"`data/cal_m3_shoot_plan.json` sets「{i}」（CAL_18 該套段落）；prompt 同檔 `prompt` 欄"],
            ['2. 人景比例與主次', v['scale']], ['3. 服裝、鞋、動作與場景', v['outfit']], ['4. 透視、接觸點與物件尺度', v['persp']],
            ['5. 光線、配色與精修', v['light']], ['6. 套框可行性', v['frame']], ['7. 結論', f"{v['verdict']}：{v['why']}"]])
    L += ['', '## 6. 重建稿', '', '每份先寫畫面設計，再組 prompt。占比是設計參考，不是 prompt 能精準控制的保證。第一批 5 張附 prompt 草稿（本輪不送出、不報價）；其餘套數在排入生成批次時依同一份設計組 prompt 並送審。', '']
    for i in BATCH1 + [x for x in order if x in W and x not in BATCH1]:
        w = W[i]
        fr = w['framing']
        L += [f"### {i}｜{S[i]['name']}｜{S[i]['month']} 月｜{w['level']}" + ('｜第一批' if i in BATCH1 else ''), '']
        L += table(['項目', '內容'], [
            ['一句話畫面與情緒', w['picture']], ['視覺主次與構圖理由', w['hierarchy']],
            ['景別', fr['shot']], ['相機', fr['camera']], ['人物位置', fr['position']], ['大致占比', fr['occupancy']],
            ['服裝與鞋', w['outfit']], ['自然動作', w['action']], ['光源、明暗與色彩', w['light']], ['背景整理', w['background']],
            ['套框預留', w['frame']], ['保留的部分', w['keep']], ['涉及 Owner 已定項目', w['owner']]])
        L += ['', '**最可能失敗的地方與降低風險：**', ''] + [f"- {r['r']} → {r['m']}" for r in w['risks']]
        if 'prompt' in w:
            L += ['', f"**prompt 草稿**（{w['prompt_note']}）：", '', '```text', w['prompt'], '```']
        L += ['']
    G = X['gates']
    L += ['## 7. 生成前與生成後的審美把關', '', '### 7.1 生成前（每套 prompt 送審前逐項回答）', '']
    L += table(['項目', '要回答的問題', '不通過時'], [[g['k'], g['q'], g['fail']] for g in G['pre']])
    L += ['', '### 7.2 生成後（照順序看；先看整張，再看細節）', '']
    L += table(['順序', '要看的事', '不通過時'], [[g['k'], g['q'], g['fail']] for g in G['post']])
    L += ['', f"**退回規則：** {G['rule']}", '', '## 8. 需要 Penny 決定的事項', '']
    for d in X['decisions']:
        L += [f"### {d['id']} {d['k']}", '', f"- 原因：{d['why']}"] + [f'- {o}' for o in d['options']] + [f"- 取捨：{d['tradeoff']}", '']
    L += ['## 9. 本輪範圍', '', '- 只做分析、企劃重建與送審：生成 0、修圖 0、訓練 0、付費操作 0、部署 0；不啟動下一批、不合併 main、不聯絡廠商。',
          '- 人物 canon、身分、已定案月份都不改；第一批 prompt 的身分句逐字沿用 CAL_21。',
          '- 舊照片、舊企劃、測試與扣款證據保留，不覆蓋、不刪除。M-4 R5 記為「生成與部署完成；第一批照片 Owner 全數退回」，不是品質驗收通過。',
          '- 下一次生成的範圍與費用另行確認。', '']
    return '\n'.join(L)


def main():
    P, O, X = load('cal_m3_shoot_plan.json'), load('cal_m4_owner_r6.json'), load('cal_m4_r6_replan.json')
    text = render(P, O, X)
    if '--check' in sys.argv:
        ok = os.path.exists(OUT) and open(OUT, encoding='utf-8').read() == text
        print('PASS' if ok else 'FAIL：CAL_23 與資料不一致，請重新產生')
        return 0 if ok else 1
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(text)
    print('wrote', os.path.relpath(OUT, ROOT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
