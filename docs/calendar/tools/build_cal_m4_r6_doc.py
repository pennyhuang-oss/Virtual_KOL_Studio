#!/usr/bin/env python3
"""TASK-CAL-001／M-4（R6）— 由 data/cal_m4_r6_replan.json（執行者分析與提案，replan-r6-v3）、data/cal_m4_owner_r6.json（Owner 決定逐字）、
data/cal_m4_supervisor_r6.json（主管 R6 覆核 REVISE 與 v2 覆核逐字）與 data/cal_m3_shoot_plan.json（現行 24 套企劃）產生：
  CAL_23_M4_R6_REPLAN.md   第一批全數退回後的全套寫真企劃重審：來源分層、修改對照（v2→v3、v1→v2）、實際看圖比較（Iris 與 5 張退回照片）、
                           共用規則（舊規則重新定性＋修訂規則）、24 套逐套審查與節奏表、23 套設計卡與構圖核算（第一批 5 張附 prompt 草稿）、
                           生成前後審美把關、決策重整、下一步單張試拍計畫（只提計畫，不執行）
產生器核對：
- 只有 V-Iris 是「已接受（不改）」；第一批 5 張整案重寫；其餘 23 套都有設計卡，結論分類一致；每套都有具體的「最吸引人的地方」。
- 構圖核算（全片幅等效的設計參考）：每套自身的預期配置加總 100%、人物占比在自己的範圍內、不低於最低安全邊界（不設其他固定門檻）；
  由焦段與占比算出距離、成品人物高度、畫面涵蓋範圍與相機俯仰（不超過 6°）；海平線／平地地平線與水平地面的消失點在相機視線高度，
  可推算位置並核對不穿過頭頸、不落在橫式裁切帶；對岸水線、樹線、坡道只列設計意圖與估計，不稱幾何驗證；景別分類與數字相符。
- 第一批 prompt 的身分句與 CAL_21 逐字相同（canon 不改）；焦段與距離和核算一致；沒有器材名詞、百分比、身材展示目的句、
  「fashion editorial」與「unretouched／unposed／available light」。
- Penny 的每個重點都有對應的證據與 A／B／C 歸因；重複動作的 v2 套數由節奏資料重新計算；決策項目都標明是否碰到 Owner 已定事項。
只排版既有文字並計算構圖數字，不新增內容；沒有呼叫任何生成服務。
用法：python3 docs/calendar/tools/build_cal_m4_r6_doc.py           # 產生
      python3 docs/calendar/tools/build_cal_m4_r6_doc.py --check   # 核對文件與資料一致
"""
import json
import math
import os
import re
import subprocess
import sys
from collections import Counter

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
CAL = os.path.join(ROOT, 'docs', 'calendar')
DATA = os.path.join(CAL, 'data')
OUT = os.path.join(CAL, 'CAL_23_M4_R6_REPLAN.md')
FIRST_LINE = 'TASK-CAL-001／M-4／R6｜v2 主管覆核與有限收尾｜送審報告'
BATCH1 = ['V-tammy-chou', 'V-rin-ayase', 'V-somi-oh', 'H-yerin-han', 'H-jia-seo']
LEVELS = ('已接受（不改）', '保留設計', '局部修改', '整案重寫')
# 器材名詞（避免器材入鏡）；補光本身可以寫成效果
EQUIP = re.compile(r'reflector|softbox|soft box|ring light|strobe|flash|light stand|umbrella|scrim|diffuser|studio light|out of frame|off-camera', re.I)
BANNED = ('fills about', '%', 'Emphasis', 'fashion editorial', 'unretouched', 'unposed', 'available light')
TRIVIAL = ('自然', '安靜', '電影感', '風景漂亮', '很美', '好看')
# 景別類型：可見範圍占身高比例（設計參考）
EXT = {'stand': (1.00, '全身站姿：髮頂到腳底'), 'knee': (0.72, '膝上：髮頂到膝下'), 'thigh': (0.60, '大腿中段以上'), 'waist': (0.42, '腰上：髮頂到臀上'),
       'chest': (0.30, '胸上'), 'seat_chair': (0.75, '坐在椅子上：髮頂到腳底'), 'seat_step': (0.65, '坐在台階上：髮頂到腳底'),
       'seat_ground': (0.55, '坐在地面／平台、腿側收：髮頂到坐面'), 'seat_half': (0.50, '坐姿半身：髮頂到坐面'),
       'seat_water': (0.55, '坐在池邊：髮頂到水面'), 'recline': (0.95, '斜躺：頭到腳（占畫寬）')}
CROP = ('knee', 'thigh', 'waist', 'chest', 'seat_half')      # 裁切景別：人物占比＝100%－頭頂留白
STANDING_CROP = ('knee', 'thigh', 'waist', 'chest')           # 站姿裁切：頭頂高度＝身高
NEAR, MID = ('waist', 'chest', 'seat_half'), ('knee', 'thigh', 'seat_water')
SAFE = {'V': (3, 3), 'H': (6, 5)}                               # 最低安全邊界：頭頂、腳下（% 畫高）
SENSOR = {'V': (24, 32), 'H': (36, 20.25)}                      # 全片幅等效畫面寬、高（mm）
PRINT = {'V': (120, 160), 'H': (192, 108)}                      # 進桌曆框後的原圖寬、高（mm）；橫式框內 104 mm
HEAD = 0.13                                                     # 頭高約身高 13%（核對地平線不穿過頭頸用）
LINE_GEO = {'horizon': '在相機視線高度，前提是海面或平地延伸到遠處', 'vp': '在相機視線高度，前提是地面水平、線條與地面平行'}


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
    """舊規則的元素出現在哪些套（從企劃資料計算；無法計算的用資料檔列出的清單）。出現不等於有問題。"""
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


def framing(sid, s, fr):
    """構圖核算（全片幅等效的設計參考，不是生成保證）。回傳計算值並核對互相一致。"""
    book = sid[0]
    h = int(s['meas'].split(' ')[0]) / 100
    ratio, label = EXT[fr['ext']]
    E = ratio * h
    sw, sh = SENSOR[book]
    f = fr['f']
    lo, hi = fr['occ']
    lay = fr['layout']
    recline = fr['ext'] == 'recline'
    p = lay[1] / 100
    assert lo <= p <= hi, (sid, 'layout 人物不在占比範圍')
    if fr['ext'] in CROP:
        assert lay[2] is None and lay[0] + lay[1] == 100, (sid, '裁切景別：頭頂留白＋人物＝100%')
    else:
        assert lay[2] is not None and sum(lay) == 100, (sid, '頭頂＋人物＋腳下＝100%')
    span = sw if recline else sh
    D, Dlo, Dhi = (E * f / (span * x) for x in (p, hi, lo))
    Hf, Wf = sh * D / f, sw * D / f
    pw, ph = PRINT[book]
    size = (lo * (pw if recline else ph), hi * (pw if recline else ph))
    head = None if recline else HEAD * h / Hf * ph            # 成品頭部約略高度（mm）
    out = dict(h=h, E=E, label=label, D=D, Dlo=Dlo, Dhi=Dhi, Hf=Hf, Wf=Wf, size=size, head=head, tilt=None, line=None)
    if not recline:
        top_safe, bot_safe = SAFE[book]
        assert lay[0] >= top_safe, (sid, '頭頂低於最低安全邊界')
        if lay[2] is not None:
            assert lay[2] >= bot_safe, (sid, '腳下低於最低安全邊界')
        top_h = h if fr['ext'] in STANDING_CROP else E          # 頭頂高度（相對她站／坐的面）
        frame_top = top_h + lay[0] / 100 * Hf
        hc = frame_top - 0.5 * Hf                                # 平視時相機應在的高度
        tilt = math.degrees(math.atan((fr['cam_h'] - hc) / D))
        assert abs(tilt) <= 6, (sid, f'相機高度與留白不一致：需俯仰 {tilt:.1f}°')
        out.update(hc=hc, tilt=tilt)
        if fr.get('line'):
            kind, name, note = fr['line']
            y = (frame_top - fr['cam_h']) / Hf * 100            # 相機視線高度在畫面中的位置，% 由上往下
            if kind in LINE_GEO:                                 # 地平線、水平地面的消失點：幾何推算
                head_end = lay[0] + HEAD * h / Hf * 100
                assert not (lay[0] - 2 <= y <= head_end + 4), (sid, f'{name} {y:.0f}% 穿過頭頸')
                if book == 'H':
                    assert 2 < y < 98, (sid, f'{name}落在橫式裁切帶')
            else:                                                # 對岸線、樹線、坡道：只寫設計意圖與估計
                assert kind == 'est' and '{y}' in note and '設計意圖' in note, (sid, '估計類線條要寫設計意圖')
            out['line'] = (kind, name, note, y)
    cls = fr['cls']
    if fr['ext'] in NEAR:
        assert cls == '近', sid
    elif fr['ext'] in MID:
        assert cls == '中', sid
    else:
        assert (cls == '中' and p >= 0.60) or (cls == '遠' and p <= 0.65), (sid, '景別分類與占比不符')
    return out


def line_txt(c, short=False):
    if c['line'] is None:
        return '—' if short else '—（畫面中沒有明顯地平線，或為近景）'
    kind, name, note, y = c['line']
    if kind == 'est':
        return f'{name}：估計約 {y:.0f}%（不是幾何驗證）' if short else f'{name}：估計，不是幾何驗證。' + note.format(y=f'{y:.0f}')
    if short:
        return f'{name}：由上 {y:.0f}%（推算）'
    return f"{name}：約在畫面由上往下 {y:.0f}%（幾何推算：{LINE_GEO[kind]}），不穿過頭頸" + (f'；{note}' if note else '')


def tilt_txt(t):
    if t is None:
        return ''
    return '平視' if abs(t) < 1 else (f'向下約 {t:.0f}°' if t > 0 else f'向上約 {-t:.0f}°')


def layout_txt(fr):
    a, b, c = fr['layout']
    if fr['ext'] == 'recline':
        return f'左 {a}%＋人物 {b}%＋右 {c}%（占畫寬）'
    return f'頭頂 {a}%＋人物 {b}%' + (f'＋腳下 {c}%' if c is not None else '（下緣裁在景別線）')


def render(P, O, SUP, X):
    S = {s['id']: s for s in P['sets']}
    order = [s['id'] for s in P['sets']]
    V = {r['id']: r for r in X['review']}
    RH = {r['id']: r for r in X['rhythm']}
    W = {w['id']: w for w in X['rewrites']}
    prep = {x['id']: x for x in load('cal_m4_batch1_prep.json')['sets']}
    PR = P['status']['production']
    # ---- 核對：來源與狀態 ----
    assert X['round'] == 'M-4 R6' and X['version'] == 'replan-r6-v3' and O['decision']['batch1'] == {s: 'Penny 退回／待重規劃' for s in BATCH1}
    assert O['page_copy']['status'].startswith('交接缺件') and O['page_copy']['text'] is None and 'owner_points' in O['source_layers']
    assert SUP['verbatim'].startswith('TASK-CAL-001／M-4／R6｜主管覆核 REVISE') and SUP['reviewed']['result_commit'] == X['history'][0]['commit']
    SV2 = SUP['v2_review']
    assert SV2['verbatim'].startswith('TASK-CAL-001／M-4／R6｜v2 主管覆核與有限收尾') and SV2['reviewed']['result_commit'] == X['supersedes']['commit'] == X['history'][1]['commit']
    T = X['trial']
    assert T['set'] in BATCH1 and T['request']['count'] == 1 and T['request']['requests'] == 1 and T['cost']['proposed_cap'] == T['cost']['r5_quote'] and len(T['flow']) == 4, '單張試拍：一張、一次請求、不自動重試'
    assert PR['accepted'] + PR['pending_owner_review'] + PR['rejected_replan'] + PR['not_generated'] == PR['sets_total'] == 24 and PR['to_complete'] == PR['pending_owner_review'] + PR['rejected_replan'] + PR['not_generated']
    assert PR['generated_cumulative'] == sum(PR['generated_log'].values()) >= PR['accepted'] + PR['rejected_replan'] and PR['rejected_sets'] == [x for x in BATCH1 if x not in PR['accepted_sets'] + PR.get('pick_sets', [])]  # M-4 R20：Yerin、Jia 有新候選，移到待選片
    # ---- 核對：結論、設計卡、節奏 ----
    assert [r['id'] for r in X['review']] == order == [r['id'] for r in X['rhythm']] and len(order) == 24
    assert all(V[i]['verdict'] in LEVELS for i in order) and [i for i in order if V[i]['verdict'] == LEVELS[0]] == ['V-iris-chen']
    assert all(V[i]['verdict'] == '整案重寫' for i in BATCH1), '第一批 5 張整案重寫'
    assert set(W) == set(order) - {'V-iris-chen'} and all(W[i]['level'] == V[i]['verdict'] for i in W)
    FR = {}
    for w in X['rewrites']:
        for k in ('picture', 'hierarchy', 'outfit', 'action', 'light', 'background', 'keep', 'owner'):
            assert w[k].strip(), (w['id'], k)
        assert w['risks'] and '主光' in w['light'], (w['id'], '光線要寫明主光來源')
        assert not re.search(r'\d\s*cm 高|約 \d+%', json.dumps(w, ensure_ascii=False)), (w['id'], '尺寸與占比改由構圖核算呈現')
        FR[w['id']] = c = framing(w['id'], S[w['id']], w['framing'])
        for m in re.finditer(r'(\d+)–(\d+) mm', json.dumps(w, ensure_ascii=False)):  # 文字中的成品尺寸必須等於核算
            assert (int(m.group(1)), int(m.group(2))) == tuple(round(x) for x in c['size']), (w['id'], m.group(0))
    for i in order:
        r = RH[i]
        assert all(r[k].strip() for k in ('dom', 'tone', 'color', 'mood', 'act', 'gaze', 'attract')), i
        assert len(r['attract']) >= 30 and r['attract'].strip('。') not in TRIVIAL, (i, '吸引點要具體')
    cls = {i: (W[i]['framing']['cls'] if i in W else RH[i]['scale']) for i in order}
    for rp in X['repeats']:
        got = sorted(i for i in order if re.search(rp['kw'], RH[i][rp['field']]))
        assert got == sorted(rp['v2']), (rp['motif'], got)
    # ---- 核對：第一批 prompt ----
    for i in BATCH1:
        p = W[i]['prompt']
        ident = prep[i]['prompt'][:prep[i]['prompt'].index(' She wears')]
        assert p.startswith(ident + ' She wears') and p.endswith(X['end_line']), f'{i}：身分句必須與 CAL_21 逐字相同'
        assert not EQUIP.search(p) and not any(b in p for b in BANNED), i
        assert all(k in p for k in ('Shot:', 'Camera:', 'Light:', 'Moment:', 'Composition:')), i
        fr, c = W[i]['framing'], FR[i]
        assert f"{fr['f']}mm lens" in p, (i, '焦段與設計卡不一致')
        m = re.search(r'from about (\d+(?:\.\d+)?) metres', p)
        assert m and c['Dlo'] - 0.5 <= float(m.group(1)) <= c['Dhi'] + 0.5, (i, '距離與構圖核算不一致', m and m.group(1), c['Dlo'], c['Dhi'])
    assert not any(b in X['end_line'] for b in BANNED)
    assert not any('prompt' in W[i] for i in W if i not in BATCH1), '本輪只有第一批附 prompt 草稿'
    for ph in X['photos']:
        own = O['owner_points'][ph['set']]
        items = [t for t in re.split('、|，但', re.sub(r'\s+', '', own.split('：', 1)[1]).rstrip('。'))]
        pts = [p['point'] for p in ph['points']]
        assert pts == items, (ph['set'], pts, items)
        assert all(p['cause'] in ('A', 'B', 'C', '—') and p['evidence'] and p['plan'] for p in ph['points']), ph['set']
        assert set(ph['dims']) == set(X['dims']), ph['set']
        assert '三成' not in json.dumps(ph, ensure_ascii=False), '不推算照片上的精確尺度'
    assert set(X['iris']['dims']) == set(X['dims'])
    aff = {}
    for r in X['old_rules']:
        a = affected(P, r['k'], r.get('sets', []))
        assert a and r['kind'] in ('廢止', '條件') and r['v2'], r['k']
        aff[r['k']] = a
    for ch in X['changes']:
        for m in re.finditer(r'(V|H)-(\w+) [^；。]*?(\d+)–(\d+) mm', ch['v2']):
            sid = next(i for i in W if i.startswith(f'{m.group(1)}-{m.group(2).lower()}'))
            assert (int(m.group(3)), int(m.group(4))) == tuple(round(x) for x in FR[sid]['size']), (ch['area'], m.group(0))
    assert all(d['owner'][:1] in ('是', '否') and d['v2'] and d['needs_owner'] in (True, False) for d in X['decisions'])
    assert X['pending_owner'] == [d['id'] for d in X['decisions'] if d['needs_owner']]
    assert X['counts'] == {'generated': 0, 'retouched': 0, 'trainings': 0, 'paid': 0, 'deploys': 0}
    cnt = {lv: [i for i in order if V[i]['verdict'] == lv] for lv in LEVELS}
    books = {b: sorted((i for i in order if i[0] == b), key=lambda i: S[i]['month']) for b in 'HV'}

    # ---- 排版 ----
    L = [FIRST_LINE, '', '# CAL_23 — M-4 R6 第一批全數退回與全套寫真企劃重審（v3：依主管 v2 覆核有限補正）', '',
         f"> 資料檔：`data/cal_m4_r6_replan.json`（{X['version']}，{X['written_on']}；執行者分析與提案，取代 {X['supersedes']['version']}＠`{X['supersedes']['commit'][:7]}`）、"
         f"`data/cal_m4_supervisor_r6.json`（主管覆核 REVISE 與 v2 覆核逐字）、`data/cal_m4_owner_r6.json`（Owner 決定與 R6 指令逐字）、`data/cal_m3_shoot_plan.json`（{P['version']}；現行 24 套）。本文件由 `tools/build_cal_m4_r6_doc.py` 產生。",
         f"> **狀態：提案，待主管覆核。** 採用前，`cal_m3_shoot_plan.json` 的 24 套原文不改。本輪生成 {X['counts']['generated']}、修圖 {X['counts']['retouched']}、訓練 {X['counts']['trainings']}、付費操作 {X['counts']['paid']}、部署 {X['counts']['deploys']}。"
         '以下是 Claude（執行者）自查，不是主管驗收，也不是 Penny 接受。', '',
         '## 0. 來源與狀態', '',
         '| 層級 | 內容 | 位置 |', '|---|---|---|',
         f"| 主管 v2 覆核（本輪） | {SV2['conclusion']} 這是文字企劃覆核，不是照片品質接受或生成授權。 | `data/cal_m4_supervisor_r6.json` v2_review.verbatim |",
         f"| 主管覆核（REVISE，上一輪） | {SUP['conclusion']} | `data/cal_m4_supervisor_r6.json` verbatim（{SUP['source']}） |"]
    L += [f"| {lab} | {txt} | `data/cal_m4_owner_r6.json` {k} |" for k, lab, txt in (
        ('verbatim', 'R6 指令原文', O['source_layers']['verbatim']), ('decision', 'Owner 決定', O['source_layers']['decision']),
        ('owner_points', '主管摘要', O['source_layers']['owner_points']), ('page_copy', 'Penny 頁面原文', O['source_layers']['page_copy']))]
    L += ['', f"- 第一批：{O['decision']['batch1_summary']}"]
    L += [f"- {s}：{v}" for s, v in O['decision']['batch1'].items()]
    L += [f"- Iris：{O['decision']['iris']}", f"- 範圍：{O['decision']['scope']}", f"- M-4 R5：{O['decision']['r5_status']}",
          f"- 進度：{PR['sets_total']} 套＝已接受 {PR['accepted']}＋待 Penny 選片 {PR['pending_owner_review']}＋退回待重規劃 {PR['rejected_replan']}＋尚未生成 {PR['not_generated']}；待完成合計 {PR['to_complete']}（累計已生成 {PR['generated_cumulative']} 張，另計" + (f"；構圖底稿另計 {PR['drafts']['generated']} 張，不是月面照片" if 'drafts' in PR else '') + "）。",
          f"- 主管 v2 覆核範圍：{SV2['scope']}", f"- 本輪限制：{SV2['limits']}",
          f"- Penny 頁面原文：{O['page_copy']['note']}", '',
          '**Penny 逐張重點（主管摘要，轉交自 R6 指令；不是 Penny 頁面原文）：**', '']
    L += [f"- {v.replace(chr(10), '').replace('  ', '')}" for v in O['owner_points'].values()]
    L += ['', '## 0.1 有限修改對照（v2 → v3，本輪）', '']
    L += table(['項目', 'v2（1af8170）', 'v3（本版）', '依據'], [[c['area'], c['v2'], c['v3'], c['why']] for c in X['changes_v3']])
    L += ['', '## 0.2 修改對照（v1 → v2，上一輪；其中補光判準與裁切景別的說法已在 v3 更正）', '']
    L += table(['項目', 'v1（5bed3a3）', 'v2（1af8170）', '依據'], [[c['area'], c['v1'], c['v2'], c['why']] for c in X['changes']])
    L += ['', '## 1. 實際看圖的檔案', '']
    L += table(['套別', '實際打開的檔案'], [[v['set'], '；'.join(v['files'])] for v in X['viewed']])
    I = X['iris']
    L += ['', '## 2. Iris（已接受）：為什麼成立', '', I['why_works'], '']
    L += table(['維度', 'V-Iris'], [[d, I['dims'][d]] for d in X['dims']])
    L += ['', '**可延續的品質原則（不是內容模板）：**', ''] + [f'{n}. {t}' for n, t in enumerate(I['keep'], 1)]
    L += ['', f"**不複製：** {I['not_copy']}", '', f"**Iris 的弱點（不改）：** {I['weak']}", '',
          '## 3. 5 張退回照片：實際看圖比較與歸因', '',
          '歸因：A＝原企劃已經造成問題；B＝生成結果偏離原企劃；C＝兩者共同造成。只引用照片上看得到的證據與企劃原文，不推測模型內部原因，也不推算照片上的精確尺度。', '']
    for n, ph in enumerate(X['photos'], 1):
        L += [f"### 3.{n} {ph['name']}｜{ph['set']}", '', f"**第一眼：** {ph['first_look']}", '']
        L += table(['維度', '這張', 'Iris 的做法'], [[d, ph['dims'][d], I['dims'][d]] for d in X['dims']])
        L += ['', '**Penny 指出的重點（主管摘要）：**', '']
        L += table(['重點', '照片上的證據', '對應的企劃內容', '歸因'], [[p['point'], p['evidence'], p['plan'], p['cause']] for p in ph['points']])
        L += ['', f"**整體歸因：** {ph['attribution']}", '']
    L += ['## 4. 共用規則', '', '### 4.1 舊規則重新定性（「出現的套」由企劃資料計算；出現不等於有問題，逐套判斷見 §5）', '',
          '「廢止」＝固定寫法本身造成問題；「條件」＝元素本身不是問題（補光、插腰、看鏡頭、近景、身材表現、高飽和都不直接判為失敗），要看在那一張是否漂亮、自然、協調。', '']
    L += table(['舊規則', '定性', '位置', '問題在哪裡', 'v2 做法', '出現', '套別'],
               [[r['rule'], r['kind'], r['where'], r['problem'], r['v2'], len(aff[r['k']]), '、'.join(aff[r['k']])] for r in X['old_rules']])
    L += ['', '### 4.2 修訂後的共用規則（所有設計卡都依此）', '']
    L += table(['編號', '規則', '內容'], [[r['id'], r['title'], r['text']] for r in X['new_rules']])
    L += ['', f"收尾句（v2）：`{X['end_line']}`", '', '## 5. 24 套逐套審查與節奏', '',
          f"結論：已接受（不改）{len(cnt[LEVELS[0]])}（{'、'.join(cnt[LEVELS[0]])}）；保留設計 {len(cnt['保留設計'])}（{'、'.join(cnt['保留設計'])}）；"
          f"局部修改 {len(cnt['局部修改'])}；整案重寫 {len(cnt['整案重寫'])}（{'、'.join(cnt['整案重寫'])}）。", '',
          '「保留設計」＝場景、服裝、姿勢、光線與構圖都不改，prompt 只套共用格式（收尾句、鞋、身材目的句改為畫面重點、補光寫成與主光同源）；'
          '「局部修改」＝保留場景與服裝方向，改占比、景別、姿勢、相機或光源；「整案重寫」＝場景、主要道具、服裝或構圖要重做。', '',
          '### 5.1 結論總表', '']
    L += table(['月份', '套別', '景別與相機（現行）', '結論', '理由'],
               [[f"{S[i]['month']} 月", i, S[i]['cam']['line'], V[i]['verdict'], V[i]['why']] for i in sorted(order, key=lambda i: (i[0], S[i]['month']))])
    L += ['', '### 5.2 節奏表（依 v2 設計；V-Iris 依已接受照片）', '',
          '景別：近＝胸上、腰上、坐姿半身；中＝大腿、膝上、坐到水面，或全身類人物占畫高 60% 以上；遠＝全身類人物占畫高 65% 以下、景占三分之一以上。', '']
    for b, name in (('H', '橫式款（16:9）'), ('V', '直式款（3:4）')):
        L += [f"**{name}**", '']
        L += table(['月', '套別', '景別', '主次', '明暗', '色彩與飽和', '情緒', '主要動作', '視線', '這張最吸引人的地方'],
                   [[S[i]['month'], i, cls[i], RH[i]['dom'], RH[i]['tone'], RH[i]['color'], RH[i]['mood'], RH[i]['act'], RH[i]['gaze'], RH[i]['attract']] for i in books[b]])
        L += ['']
    tone = lambda t: t[:3] if t.startswith(('中間調', '高反差')) else t[:2]
    rows = []
    for lab, fn in (('景別（近／中／遠）', lambda i: cls[i]), ('主次', lambda i: RH[i]['dom'].split('（')[0]), ('明暗', lambda i: tone(RH[i]['tone'])),
                    ('視線', lambda i: '看鏡頭' if RH[i]['gaze'].startswith('看鏡頭') else '不看鏡頭'), ('飽和', lambda i: RH[i]['sat'])):
        rows.append([lab] + ['、'.join(f'{k} {v}' for k, v in sorted(Counter(fn(i) for i in books[b]).items())) for b in 'HV'])
    L += ['**分布（自動統計）：**', ''] + table(['項目', '橫式 12', '直式 12'], rows)
    L += ['', '**重複動作與視線（v2 套數由節奏表重新計算）：**', '']
    L += table(['重複項目', 'v1 重建稿', 'v2', '處理'],
               [[r['motif'], f"{len(r['v1'])}：{'、'.join(r['v1'])}", f"{len(r['v2'])}：{'、'.join(r['v2']) or '—'}", r['note']] for r in X['repeats']])
    L += ['', '**發現的過度重複與修正：**', ''] + table(['位置', '問題', '修正'], [[n['where'], n['issue'], n['fix']] for n in X['rhythm_notes']])
    L += ['', '**保留的相似處（看過、決定不改）：**', ''] + [f'- {t}' for t in X['residual']]
    L += ['', '### 5.3 逐套審查（依修訂規則重看現行企劃）']
    for i in sorted(order, key=lambda i: (i[0], S[i]['month'])):
        s, v = S[i], V[i]
        L += ['', f"#### {i}｜{s['name']}｜{s['month']} 月｜{s['ratio']}｜{v['verdict']}", '']
        L += table(['項目', '內容'], [
            ['1. 現行構想', current(s)],
            ['　來源位置', f"`data/cal_m3_shoot_plan.json` sets「{i}」（CAL_18 該套段落）；prompt 同檔 `prompt` 欄"],
            ['2. 人景比例與主次', v['scale']], ['3. 服裝、鞋、動作與場景', v['outfit']], ['4. 透視、接觸點與物件尺度', v['persp']],
            ['5. 光線、配色與完成度', v['light']], ['6. 套框可行性', v['frame']], ['7. 結論', f"{v['verdict']}：{v['why']}"],
            ['8. 這張最吸引人的地方（v2）', RH[i]['attract']]])
    L += ['', '## 6. 設計卡與構圖核算', '',
          '**怎麼讀這些數字：** 焦段與距離都是全片幅等效的設計參考，用來確認占比、留白、相機高度與套框互相合理；prompt 只拿來當透視提示，不保證模型精準遵守。'
          '成品尺寸＝人物占比×進框後的原圖高度（直式 160 mm；橫式 192×108 mm 原圖、框內 104 mm；斜躺以畫寬 192 mm 計）。'
          '距離＝可見範圍×焦段÷（畫面高×占比）；可見範圍依身高乘景別比例估計（全身 1.00、膝上 0.72、腰上 0.42、胸上 0.30、坐椅 0.75、坐台階 0.65、坐地 0.55、坐姿半身 0.50、斜躺 0.95）。'
          '相機俯仰＝相機高度與「平視時應在的高度」的差。線條分三類：海平線與平地地平線、水平地面上的消失點，都在相機視線高度，可推算位置（由上往下）；'
          '對岸水線、樹線、坡道受距離與地形影響，只寫設計意圖與估計，不稱幾何驗證。', '',
          f"**最低安全邊界（下限）：** 直式 3:4 不裁切，頭頂與腳下各至少 {SAFE['V'][0]}%；橫式 16:9 上下共裁 4 mm，頭頂至少 {SAFE['H'][0]}%、腳下至少 {SAFE['H'][1]}%，地平線避開上下 2 mm 帶。下表「預期配置」是各套實際設計的位置，和下限分開。", '']
    rows = []
    for i in BATCH1 + [x for x in order if x in W and x not in BATCH1]:
        fr, c = W[i]['framing'], FR[i]
        rows.append([i, cls[i], fr['shot'].split('（')[0], f"{fr['f']}mm", f"{fr['occ'][0] * 100:.0f}–{fr['occ'][1] * 100:.0f}%", layout_txt(fr),
                     f"約 {c['D']:.1f} m（{c['Dlo']:.1f}–{c['Dhi']:.1f}）", f"{c['size'][0]:.0f}–{c['size'][1]:.0f} mm" + (f"（頭約 {c['head']:.0f}）" if c['head'] else ''),
                     f"{c['Wf']:.1f}×{c['Hf']:.1f} m", f"{fr['cam_h']:.2f} m（{fr['cam_ref']}）{tilt_txt(c['tilt'])}".rstrip(),
                     line_txt(c, short=True)])
    L += table(['套別', '景別', '景別類型', '焦段', '人物占比', '預期配置', '距離（核算）', '成品人物高度（mm）', '她的位置畫面涵蓋（寬×高）', '相機高度與俯仰', '地平線／消失點'], rows)
    L += ['']
    for i in BATCH1 + [x for x in order if x in W and x not in BATCH1]:
        w, fr, c = W[i], W[i]['framing'], FR[i]
        L += [f"### {i}｜{S[i]['name']}｜{S[i]['month']} 月｜{w['level']}" + ('｜第一批' if i in BATCH1 else ''), '']
        safe = '—（斜躺以畫寬計，左右各留一成多）' if fr['ext'] == 'recline' else (
            f"頭頂 ≥{SAFE[i[0]][0]}%" + (f"、腳下 ≥{SAFE[i[0]][1]}%" if fr['layout'][2] is not None else '（裁切景別，下緣不切在關節）'))
        L += table(['項目', '內容'], [
            ['一句話畫面', w['picture']], ['這張最吸引人的地方', RH[i]['attract']], ['視覺主次與構圖理由', w['hierarchy']],
            ['景別', f"{fr['shot']}（{cls[i]}景；{c['label']}）"], ['人物位置', fr['xpos']],
            ['人物占比（設計參考）', f"{fr['occ'][0] * 100:.0f}–{fr['occ'][1] * 100:.0f}%" + ('（占畫寬）' if fr['ext'] == 'recline' else '（占畫高）')],
            ['預期配置', layout_txt(fr)], ['最低安全邊界', safe],
            ['焦段與距離（全片幅等效，設計參考）', f"{fr['f']}mm，約 {c['D']:.1f} m（占比範圍對應 {c['Dlo']:.1f}–{c['Dhi']:.1f} m）；她的位置畫面涵蓋約 {c['Wf']:.1f} m 寬 × {c['Hf']:.1f} m 高"],
            ['相機高度', f"約 {fr['cam_h']:.2f} m（{fr['cam_ref']}）；" + ('斜躺依畫面描述' if c['tilt'] is None else f"依預期配置，平視時相機應在約 {c['hc']:.2f} m；" + ('差距在 1° 內，即平視' if abs(c['tilt']) < 1 else f"所以相機需{tilt_txt(c['tilt'])}"))],
            ['地平線／消失點', line_txt(c)],
            ['成品人物高度', f"{c['size'][0]:.0f}–{c['size'][1]:.0f} mm" + ('（斜躺身長，畫寬 192 mm）' if fr['ext'] == 'recline' else
                                                                        f"（{'直式框高 160 mm' if i[0] == 'V' else '橫式原圖高 108 mm、框內 104 mm'}{'；裁切景別為髮頂到下緣的可見部分' if fr['ext'] in CROP else ''}）；頭部約 {c['head']:.0f} mm")],
            ['服裝與鞋', w['outfit']], ['主要動作', w['action']], ['光源、明暗與色彩', w['light']], ['背景整理', w['background']],
            ['保留的部分', w['keep']], ['涉及 Owner 已定項目', w['owner']]])
        L += ['', '**最可能失敗的地方與降低風險：**', ''] + [f"- {r['r']} → {r['m']}" for r in w['risks']]
        if 'prompt' in w:
            L += ['', f"**prompt 草稿**（{w['prompt_note']}）：", '', '```text', w['prompt'], '```']
        L += ['']
    G = X['gates']
    L += ['## 7. 生成前與生成後的審美把關', '', '### 7.1 生成前（每套 prompt 送審前逐項回答）', '']
    L += table(['項目', '要回答的問題', '不通過時'], [[g['k'], g['q'], g['fail']] for g in G['pre']])
    L += ['', '### 7.2 生成後（照順序看；先看整張，再看細節）', '']
    L += table(['順序', '要看的事', '不通過時'], [[g['k'], g['q'], g['fail']] for g in G['post']])
    L += ['', f"**退回規則：** {G['rule']}", '', '## 8. 決策項目重整（D1–D5）', '',
          'v1 的 D1–D5 是提案，主管沒有代 Penny 採用。本版逐項確認是否碰到 Owner 已定事項：碰到的保留 Owner 已定內容；沒碰到的屬本輪授權內的設計，給完整推薦，送主管覆核。', '']
    L += table(['項目', 'v1 提案', '是否碰到 Owner 已定事項', 'v2 處理', '理由', '需要 Penny 決定'],
               [[f"{d['id']} {d['k']}", d['v1'], d['owner'], d['v2'], d['why'], '是' if d['needs_owner'] else '否'] for d in X['decisions']])
    L += ['', f"**尚待 Penny 決定：{'、'.join(X['pending_owner']) or '無'}。** 照片生成後仍由 Penny 看圖決定接受或修改；下一次生成的範圍與費用另行確認。", '',
          f"## 9. 下一步單張試拍計畫（提案，不執行）：{T['set']}", '', f"**狀態：** {T['status']}", '', '**為什麼最適合驗證新的寫真方向：**', '']
    L += [f'{n}. {t}' for n, t in enumerate(T['why'], 1)]
    L += ['', '**能驗證：**', ''] + [f'- {t}' for t in T['validates']] + ['', '**不能代表：**', ''] + [f'- {t}' for t in T['not_cover']]
    Q = T['request']
    L += ['', '**模型、設定與張數：**', ''] + table(['項目', '內容'], [['模型', Q['model']], ['Soul', Q['soul']], ['品質／比例', f"{Q['quality']}／{Q['aspect_ratio']}"],
          ['張數／請求', f"count {Q['count']}、{Q['requests']} 次請求（不自動重試）"], ['unlim／參考圖／style', f"{'是' if Q['use_unlim'] else '否'}／{Q['medias']}／{Q['style_id']}"], ['存放', Q['folder']], ['prompt', Q['prompt']],
          ['預期輸出', T['output']]])
    C2 = T['cost']
    L += ['', f"**費用資訊：** {C2['source']} 建議授權上限 {C2['proposed_cap']:.2f} credits。{C2['caveat']}", '', '**生成後流程：**', ''] + [f'{n}. {t}' for n, t in enumerate(T['flow'], 1)]
    L += ['', '**其他候選為什麼不先試：**', ''] + [f"- {a['set']}：{a['why_not_first']}" for a in T['alternatives']] + ['', f"**之後：** {T['next']}", '',
          '## 10. 本輪範圍', '', '- 單張試拍只提計畫，沒有呼叫任何生成或報價工具；不一次安排 5 張。', '- 只做分析、企劃重建與送審：生成 0、修圖 0、訓練 0、付費操作 0、部署 0；不啟動下一批、不改已接受的 V-Iris、不合併 main。',
          '- 人物 canon、身分、已定案月份都不改；第一批 prompt 的身分句逐字沿用 CAL_21。',
          '- 舊照片、舊企劃、v1 提案、測試與扣款證據保留，不覆蓋、不刪除。M-4 R5 記為「生成與部署完成；第一批照片 Owner 全數退回」，不是品質驗收通過。',
          '- 以上是 Claude 自查，不是主管驗收或 Penny 接受。', '']
    return '\n'.join(L)


def main():
    P, O, SUP, X = load('cal_m3_shoot_plan.json'), load('cal_m4_owner_r6.json'), load('cal_m4_supervisor_r6.json'), load('cal_m4_r6_replan.json')
    text = render(P, O, SUP, X)
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
