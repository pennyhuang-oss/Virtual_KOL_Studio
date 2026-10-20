#!/usr/bin/env python3
"""TASK-CAL-001／M-4（R1）— 由 data/cal_m3_shoot_plan.json（shoot-plan-v8，人寫企劃）產生三份文件：
  CAL_18_M3_SHOOT_PLAN.md          主管結論（M-3 完成）、23 套已接受＋H-Luna 主管覆核通過、攝影設計、兩本攝影總覽與月份、印刷構圖核對、費用與 Iris 首張
  CAL_19_M3_R2_OWNER_DECISION.md   R2 Owner 決策紀錄（逐字回饋＋執行摘要；來源 data/cal_m3_owner_feedback_r2.json；R3 起內容不變）
  CAL_20_M4_IRIS_FIRST_TEST_PREP.md  V-Iris 首試準備（R7 起）與首試前核查（M-4 R1 起）；企劃資料的 m4_prep，只整理、不生成
只排版既有文字，不新增內容；沒有呼叫任何生成服務。
用法：python3 docs/calendar/tools/build_cal_m3_plan_doc.py           # 產生
      python3 docs/calendar/tools/build_cal_m3_plan_doc.py --check   # 核對文件與資料一致
"""
import json
import os
import subprocess
import sys

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
CAL = os.path.join(ROOT, 'docs', 'calendar')
PLAN = os.path.join(CAL, 'data', 'cal_m3_shoot_plan.json')
OUT18 = os.path.join(CAL, 'CAL_18_M3_SHOOT_PLAN.md')
OUT19 = os.path.join(CAL, 'CAL_19_M3_R2_OWNER_DECISION.md')
OUT20 = os.path.join(CAL, 'CAL_20_M4_IRIS_FIRST_TEST_PREP.md')
FIRST_LINE = 'TASK-CAL-001／M-4／R1｜V-Iris首試前核查｜送審報告'
FIRST_20 = 'TASK-CAL-001／M-4／R1｜V-Iris 首試準備與首試前核查（不生成、未授權）'
FIRST_19 = 'TASK-CAL-001／M-3／R2｜24套雙款獨立寫真企劃｜送審報告'   # R2 的決策紀錄，標題不改
ORIGIN_ZH = {'new': '新企劃', 'accepted-v2-main': 'Penny 已接受的 v2 主方向', 'accepted-v2-alt': 'Penny 採用的 v2 替代方向'}
BOOK_ZH = {'H': '橫式款', 'V': '直式款'}
ST_ZH = {'accepted': '已接受', 'owner_revised': '依owner指定修訂，待主管核對落實', 'supervisor_verified': '依owner指示修訂，主管覆核通過'}


def cell(s):
    return str(s).replace('|', '／').replace('\n', ' ')


def table(head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    return out + ['| ' + ' | '.join(cell(c) for c in r) + ' |' for r in rows]


def outfit_str(o):
    return '；'.join(f'{k}：{v}' for k, v in o.items())


def photo_rows(d, b):
    rows = [s for s in d['sets'] if s['book'] == b]
    rows.sort(key=lambda s: s['month'])
    return [[f"{s['month']} 月", f"{s['name']}（{s['id']}）", ST_ZH[s['status']], s['cam']['shot']['zh'], s['cam']['body']['short'], s['cam']['face']['zh'],
             s['cam']['gaze']['zh'], s['cam']['angle']['short'], s['cam']['pos'], s['cam']['focus']] for s in rows]


def render18(d):
    m = d['meta']
    S = {s['id']: s for s in d['sets']}
    Ph = d['photo']
    O3 = d['owner_r3']
    O4 = d['owner_r4']
    PR = d['printing']
    L = [FIRST_LINE, '', f"# CAL_18 — M-3 24 套雙款寫真企劃、攝影設計與印刷構圖（{d['version']}）", '',
         f"> 資料檔：`data/cal_m3_shoot_plan.json`（{d['version']}，{d['round']}，{d['written_on']}）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。",
         f"> **{m['status']}。** 本輪生成數 {d['counts']['generated']}、credits {d['counts']['credits']}、訓練數 {d['counts']['trainings']}。",
         '> R4 狀態（歷史）：8 套已接受、16 套修訂待 Penny 定案；兩本月份人選排序已確認；版面（照片框）尚未定案；生成與費用都未授權。R2 的 Owner 決策逐字紀錄見 `CAL_19_M3_R2_OWNER_DECISION.md`。',
         '> R5：只修資料一致性與措辭（見 0b），沒有攝影方向變更。',
         '> R6 狀態（歷史）：22 套已接受；H-jia-seo、H-luna-tanaka 兩套新推薦待 Penny 定案；兩本月份與工作照片框已接受（工作版型，不是廠商規格、印刷安全或成品核准）。',
         '> R7 狀態（歷史）：23 套已接受（加上 H-jia-seo）；H-luna-tanaka 依 Penny 指定只把手部改為雙手輕捧日式小香袋，當時記為「依owner指定修訂，待主管核對落實」。',
         '> **M-4 R1 狀態：主管結論 M-3／R7 PASS，M-3 完成——23 套 owner 接受＋H-Luna 依 owner 指示修訂、主管覆核通過（Penny 沒有看過修訂後的版本）；不再要求 owner 填企劃問卷。V-Iris 首試準備與首試前核查見 `CAL_20_M4_IRIS_FIRST_TEST_PREP.md`；生成與費用都未授權。**', '',
         '## 0. 版本', '']
    L += table(['項目', '內容'], [['名單', f"{m['roster']}；不換人"], ['上一版企劃', f"{d['revision']['from_version']}（commit `{d['revision']['from_commit']}`）"],
                                  ['這一版', d['revision']['summary']], ['R7（歷史）', f"{d['r7']['summary']}（基準 commit `{d['r7']['from_commit']}`）"], ['R6（歷史）', f"{d['r6']['summary']}（基準 commit `{d['r6']['from_commit']}`）"],
                                  ['R5 資料修訂', f"{d['r5']['summary']}（基準 commit `{d['r5']['from_commit']}`）"],
                                  ['素材頁版本', f"`{m['material_page_commit']}`"], ['桌曆基準', f"`{m['calendar_baseline']}`"]])
    L += ['', f"**參考照片：** {d['ref_note']}", '']
    L += ['## 0a. M-4 R1 修改（差異）', '', f"{d['m4r1']['summary']}", '']
    L += table(['類別', '位置', '舊', '新'], [[x['kind'], x['where'], x['old'], x['new']] for x in d['m4r1']['changes']])
    L += ['', '## 0b. R7 修改（差異，歷史）', '', f"{d['r7']['summary']}", '']
    L += table(['類別', '位置', '舊', '新'], [[x['kind'], x['where'], x['old'], x['new']] for x in d['r7']['changes'] if x['kind'] != '狀態（owner 決策）'])
    L += ['', f"狀態：{sum(1 for x in d['r7']['changes'] if x['kind'] == '狀態（owner 決策）')} 套由「R6 待決」改為「已接受」（R7 owner 紀錄：H-jia-seo）；H-luna-tanaka 記為「依owner指定修訂，待主管核對落實」。", '']
    L += ['## 0c. R6 修改（差異，歷史）', '', f"{d['r6']['summary']}", '']
    L += table(['類別', '位置', '舊', '新'], [[x['kind'], x['where'], x['old'], x['new']] for x in d['r6']['changes'] if x['kind'] != '狀態（owner 決策）'])
    L += ['', f"狀態：{sum(1 for x in d['r6']['changes'] if x['kind'] == '狀態（owner 決策）')} 套由「修訂」改為「已接受」（R6 owner 紀錄）。", '']
    L += ['## 0d. R5 資料修訂（差異，歷史）', '', '**不變：** ' + '；'.join(d['r5']['unchanged']) + '。', '']
    L += table(['類別', '位置', '舊', '新'], [[x['kind'], x['where'], x['old'], x['new']] for x in d['r5']['changes'] if not x['where'].startswith('sets[') or x['kind'] != '印刷措辭'])
    L += ['', f"另有 24 套逐張印刷文字的措辭修訂（共 {sum(1 for x in d['r5']['changes'] if x['where'].startswith('sets[') and x['kind'] == '印刷措辭')} 套），新文字見 3c；舊文字保留在資料檔 `r5.changes`。", '']

    SU = d['sup_m4r1']
    L += ['## 1. 主管結論（M-4 R1，逐字）', '', f"> 資料檔：`data/cal_m4_supervisor_r1.json`（{SU['recorded_on']}）。{SU['source']}{SU['note']}", '',
          '```text', SU['verbatim']['conclusion'], '```', '', '**本輪指示（逐字）：**', '', '```text', SU['verbatim']['instructions'], '```', '']
    O7 = d['owner_r7']
    S7 = O7['summary']
    L += ['## 1a. R7：owner 決策（歷史，逐字，主管轉述）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r7.json`（{O7['recorded_on']}）。{O7['source']}{O7['note']}", '',
          '```text', O7['verbatim']['decisions'], '```', '', '**Penny 原文（R7）：**', '']
    for sid, x in O7['verbatim']['per_set'].items():
        L += [f"- {sid}（{x['month']} 月）：「{x['text']}」"]
    L += ['', '**主管的收尾指示（逐字，不是 Penny 原話）：**', '', '```text', O7['verbatim']['supervisor']['wrap_up'], '```', '',
          '**可執行摘要（整理，不是 Penny 原話）：**', '',
          f"- 已接受 23 套（R4 的 8 套＋R6 的 14 套＋R7 的 H-jia-seo）：{'、'.join(S7['accepted'])}——拍攝內容與 prompt 不變，不再要求回覆。",
          f"- {'、'.join(S7['owner_revised'])}：{S7['owner_revised_label']}（見第 3 節）。", f"- {S7['no_more_owner_questions']}",
          f"- 月份：{S7['months']}", f"- 照片框：{S7['frames']}", f"- 首試：{S7['iris_first']}", f"- 尚未核准：{'、'.join(S7['not_approved'])}。", '']
    O6 = d['owner_r6']
    S6 = O6['summary']
    L += ['## 1b. R6：owner 決策（歷史，逐字，主管轉述）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r6.json`（{O6['recorded_on']}）。{O6['source']}{O6['note']}", '',
          '```text', O6['verbatim']['decisions'], '```', '', '**Penny 對兩套的原文回饋：**', '']
    for sid, x in O6['verbatim']['per_set'].items():
        L += [f"- {sid}（{x['month']} 月）：「{x['text']}」"]
    L += ['', '**可執行摘要（整理，不是 Penny 原話）：**', '',
          f"- 已接受 22 套（R4 的 8 套＋R6 的 14 套）：{'、'.join(S6['accepted'])}——拍攝內容與 prompt 不變，不再要求回覆。",
          f"- 待決 2 套：{'、'.join(S6['pending'])}（R6 新推薦，見第 3 節）。", f"- 月份：{S6['months']}", f"- 照片框：{S6['frames']}",
          f"- 首試：{S6['iris_first']}", f"- 尚未核准：{'、'.join(S6['not_approved'])}。", '']
    Sm = O4['summary']
    L += ['## 1c. R4：owner 決策（歷史，逐字，主管轉述）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r4.json`（{O4['recorded_on']}）。{O4['note']}", '',
          '```text', O4['verbatim']['decisions'], '```', '', '```text', O4['verbatim']['status'], '```', '',
          '**可執行摘要（整理，不是 Penny 原話）：**', '',
          f"- 已接受 8 套：{'、'.join(Sm['accepted'])}——服裝、場景、表情與攝影照 v4，不因整體偏好重設。",
          f"- 修訂 16 套：{'、'.join(Sm['revise'])}。{Sm['jia_note']}",
          f"- 月份：{Sm['months']}", f"- 整體：{'；'.join(Sm['overall'])}。", f"- 首試：{Sm['iris_first']}",
          f"- 尚未核准：{'、'.join(Sm['not_approved'])}。", '']
    L += ['## 1d. R3：Penny 的攝影設計要求（逐字，仍適用）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r3.json`（{O3['recorded_on']}）。{O3['note']}", '',
          '```text', O3['verbatim']['requirement'], '```', '', '```text', O3['verbatim']['keep_existing'], '```', '',
          '```text', O3['verbatim']['not_approved'], '```', '', f"**落實方式：** {Ph['summary']}", '']
    L += ['**共同規則：**', ''] + [f'- {x}' for x in Ph['rules']] + ['']

    L += ['## 2. 兩本攝影總覽（月份已確認；M-3 完成：23 套已接受＋H-Luna 主管覆核通過）', '']
    head = ['月份（已確認）', '人物', '狀態', '景別', '身體方向', '臉部方向', '視線', '相機角度', '人物位置', '主要展示重點']
    for b, n in (('H', '2.1'), ('V', '2.2')):
        L += [f"### {n} {BOOK_ZH[b]}（{'16:9' if b == 'H' else '3:4'}）", '']
        L += table(head, photo_rows(d, b))
        c = Ph['counts'][b]
        L += ['', f"**景別：** {'、'.join(f'{k} {v}' for k, v in c['shot'].items())}；**身體方向：** {'、'.join(f'{k} {v}' for k, v in c['body'].items())}。", '',
              f"**節奏：** {Ph['rhythm'][b]}", '', f"**依推薦月份的景別順序：** {Ph['sequence'][b]}", '']
    L += [f"**近景：** {Ph['rhythm']['near']}", '', f"**角度與視線：** {Ph['rhythm']['angles']}", '', f"**同一位的兩款：** {Ph['rhythm']['pair']}", '',
          f"**戶外與重複：** {Ph['rhythm']['outdoor']}", '']
    L += ['### 2.3 prompt 一致性檢查（產生資料時逐套執行，不通過就無法建置）', ''] + [f'- {x}' for x in Ph['checks']] + ['']

    L += ['## 3. R7：H-Luna 依 owner 指定修訂（M-4 R1 主管覆核通過）', '', '只改手部與香袋；主管 M-4 R1 覆核通過，M-3 完成。Penny 指定了這個修改，但沒有看過修訂後的版本；不再請 Penny 回覆香袋顏色、手勢或整套企劃。', '']
    for s in d['sets']:
        if s['status'] != 'supervisor_verified':
            continue
        r7 = s['r7']
        L += [f"### {s['id']}｜{s['month']} 月｜{s['name']}｜{s['m4r1']['label']}", '', f"**M-4 R1：** {s['m4r1']['note']}", '', f"**Penny 原文（R7）：**「{r7['owner']}」", '',
              '**主管補充的落實細節（逐字，不是 Penny 原話）：**', '', '```text', r7['supervisor'], '```', '',
              f"- **改了什麼：** {r7['change']}", f"- **不變：** {r7['kept']}", f"- **參考圖：** {r7['no_ref']}", f"- **R7 當時的狀態：** {r7['note']}", f"- **攝影（不變）：** {s['cam']['line']}", '',
              '**修改前（R6）→ 修改後（R7）：**', '']
        L += table(['欄位', '修改前（R6）', '修改後（R7）'], [[x['k'], x['before'], x['after']] for x in r7['diff']])
        L.append('')
    L += ['### R6 的 2 套新推薦（歷史：當時的 Penny 原文與改動）', '']
    L += table(['ID', 'R6 Penny 原文', 'R6 改了什麼', '目前'], [[s['id'], s['r6']['owner'], s['r6']['change'], ST_ZH[s['status']] + (f"（{s['r7']['accepted_in']}）" if s['status'] == 'accepted' else '')]
                                                         for s in d['sets'] if s['r6'].get('change')])
    L += ['', '### 23 套已接受（拍攝內容與 prompt 不變）', '']
    L += table(['ID', '月份', '接受輪次', '主題', '攝影', '印刷判斷'], [[s['id'], f"{s['month']} 月", s['r7']['accepted_in'], s['theme'], s['cam']['line'], s['print']['verdict']] for s in d['sets'] if s['status'] == 'accepted'])
    L += ['', '### R4 的 16 套修訂（歷史：當時的 owner 原文與改動，見第 8 節各套）', '']
    L += table(['ID', 'R4 改了什麼（歷史）'], [[s['id'], s['r4']['change']] for s in d['sets'] if s['r4'].get('change')])
    L += ['', PR['accepted_impact']['summary'], '']
    AN = d['accepted_notes']
    L += [f"**已接受套數的中英同步（{AN['status']}）：** {AN['summary']}", '']
    L += table(['ID', '中文妝感（已接受）', '已補進英文 prompt 的一句'], [[x['id'], x['makeup_zh'], f"`{x['added_en']}`"] for x in AN['items']])
    L.append('')

    L += ['## 3b. 印刷規格與安全構圖（已知／假設／未知）', '', PR['note'], '', '**四類數字：**', '']
    L += table(['類別', '內容'], [[x['k'], x['v']] for x in PR['categories']])
    L += ['', '**已知：**', '']
    L += table(['項目', '橫式', '直式', '來源'], [[x['k'], x['H'], x['V'], x['src']] for x in PR['known']])
    L += ['', '**假設（本案規劃用，不是廠商規格）：**', '']
    L += table(['項目', '橫式', '直式', '為什麼'], [[x['k'], x['H'], x['V'], x['why']] for x in PR['assumed']])
    L += ['', '**未知：**', ''] + [f'- {x}' for x in PR['unknown']]
    L += ['', '**暫定照片框與照片比例：**', '']
    L += table(['款', '暫定照片框', '畫布座標（mm）', '來源', '照片比例', '放入後（比例計算）', '日期區（暫定）'],
               [[BOOK_ZH[b], f"{PR['frames'][b]['name']} {PR['frames'][b]['mm'][0]}×{PR['frames'][b]['mm'][1]} mm（{PR['frames'][b]['ratio']}）",
                 '({},{})–({},{})'.format(*PR['frames'][b]['canvas']), PR['frames'][b]['from'], PR['fit'][b]['img'] + f"（{PR['fit'][b]['scaled']}）",
                 PR['fit'][b]['crop'], '({},{})–({},{})'.format(*PR['frames'][b]['date'])] for b in 'HV'])
    L += ['', '**如果改用其他框：**', ''] + [f"- {x['k']}：{x['v']}" for x in PR['compare']]
    L += ['', f"**示意圖：** 橫式 `decision_site/public/{PR['diagrams']['H']}`、直式 `decision_site/public/{PR['diagrams']['V']}`（只有方框與尺寸，不含照片；不是印刷安全證明）。", '',
          '**原則：**', ''] + [f'- {x}' for x in PR['rules']]
    L += ['', '### 3c. 24 套逐張印刷構圖判斷（依已接受的工作照片框）', '']
    L += ['百分比與「套框後約 x%」都是依規劃構圖推算的理論／規劃預估，不是實圖量測。', '']
    L += table(['ID', '狀態', '照片框', '比例計算', '邊緣（規劃預估）', '不能切／規劃目標', '印刷判斷（條件）', '生成後待驗證', '原生尺寸', '有效 ppi'],
               [[s['id'], ST_ZH[s['status']], s['print']['frame'], s['print']['crop'], '；'.join(s['print']['edges']),
                 f"{s['print']['keep']}／{s['print']['need']}", s['print']['verdict'], s['print']['verify'], s['print']['native'], s['print']['ppi']] for s in d['sets']])
    I = PR['iris_first']
    L += ['', '### 3d. V-Iris 首試是否需要構圖微調', '', f"- {I['answer']}", f"- {I['condition']}", f"- {I['verify']}",
          f"- R7：首張驗收條件（含套框與有效 ppi）見 `{os.path.basename(d['m4_prep']['doc'])}`。", '']

    L += ['## 4. R2 Penny 回饋落實表（歷史紀錄；最新決定見第 1、3 節）', '']
    L += table(['人設', 'Penny 回饋（逐字）', '當時（R2）怎麼落實（歷史，部分場景已在 R4 撤回）', '目前橫式款', '目前直式款'],
               [[p['name'], p['feedback'] + (f"（{p['shared']}）" if p['shared'] else ''), '；'.join(p['applied']), S[p['sets'][0]]['theme'], S[p['sets'][1]]['theme']] for p in d['people']])
    L.append('')

    for b in 'HV':
        L += [f"## {5 if b == 'H' else 6}. {BOOK_ZH[b]} 12 套總覽", '']
        rows = [s for s in d['sets'] if s['book'] == b]
        rows.sort(key=lambda s: s['month'])
        L += table(['月份（已確認）', 'ID', '狀態', '主題', '環境', '服裝', '色彩', '姿態', '表情', '性感程度', '攝影方法', '景別｜身體方向｜臉與視線｜拍攝角度'],
                   [[f"{s['month']} 月", s['id'], ST_ZH[s['status']], s['theme'], s['env'], outfit_str(s['outfit']), s['palette'], s['pose'] + s['hands'], s['expr'],
                     s['sexy'], s['method'], s['cam']['line']] for s in rows])
        L.append('')

    L += ['## 7. 兩本月份（已確認）', '']
    L += table(['月份', '橫式款', '理由', '直式款', '理由'],
               [[f"{x['m']} 月", f"{x['H']}（{S[x['H']]['name']}）", x['why_h'], f"{x['V']}（{S[x['V']]['name']}）", x['why_v']] for x in d['months']])
    L += [''] + [f'- {x}' for x in d['month_rules']] + ['']

    L += ['## 8. 24 套企劃', '']
    for n, s in enumerate(d['sets'], 1):
        fr, c = s['frame'], s['cam']
        st = f"已接受（{s['r7']['accepted_in']} owner 紀錄）" if s['status'] == 'accepted' else s['m4r1']['label']
        L += [f"### 8.{n} {s['id']}｜{s['name']}｜{BOOK_ZH[s['book']]}（{ORIGIN_ZH[s['origin']]}｜{st}）", '', f"**一句話：** {s['theme']}", '',
              f"**攝影：** {c['line']}", '']
        L += table(['攝影欄位', '中文', 'prompt 對應句'], [
            ['1. 景別', c['shot']['zh'], c['shot']['en']], ['2. 畫面上下界', c['bounds']['zh'], c['bounds']['en']],
            ['3. 身體朝向', f"{c['body']['short']}：{c['body']['zh']}", c['body']['en']],
            ['4. 臉部朝向與視線', f"{c['face']['zh']}，{c['gaze']['zh']}", f"{c['face']['en']}, {c['gaze']['en']}"],
            ['5. 相機高度與俯仰', f"{c['angle']['zh']}（{c['angle']['ref']}）", c['angle']['en']],
            ['6. 畫面配置', c['comp']['zh'], c['comp']['en']], ['7. 攝影目的', c['purpose']['zh'], c['purpose']['en']]])
        L += ['', f"**選擇理由：** {c['why']}", '',
              (f"**R7：** {s['r7']['note']}" if s['status'] == 'accepted' else f"**R7 改了什麼：** {s['r7']['change']}"), '']
        if s['r6'].get('change'):
            L += [f"**R6 改了什麼（歷史）：** {s['r6']['change']}", '']
        if s['r4'].get('change'):
            L += [f"**R4 改了什麼（歷史）：** {s['r4']['change']}", '']
        if 'r5' in s:
            L += [f"**R5：** {s['r5']['note']}補上的句子：`{s['r5']['added_en']}`", '']
        crop = fr['shot'] in ('chest', 'waist', 'thigh', 'knee')
        size = f"頭頂上方留白約 {fr['headroom']}%（規劃）" if crop else f"人物約佔{fr['fill_of']} {fr['fill']}%（規劃）"
        L += table(['項目', '內容'], [
            ['場景', s['scene']], ['服裝', outfit_str(s['outfit'])], ['髮型', s['hair']], ['妝感', s['makeup']],
            ['身材設定（數字）', s['meas']], ['畫面上怎麼呈現胸型、腰線、臀腿', s['body_show']],
            ['主光', s['light']['主光']], ['補光', s['light']['補光']], ['姿態', s['pose']], ['手的位置', s['hands']],
            ['表情', s['expr']], ['視線', s['gaze']],
            ['焦段／距離／視野（參考）', f"{fr['ratio']}，{fr['f']}mm，約 {fr['d']} 公尺，視野 {fr['view_w']}×{fr['view_h']} 公尺；{size}；相機約 {fr['cam_m']} 公尺高、畫面中心約 {fr['centre_m']} 公尺高，俯仰約 {fr['tilt_deg']:+.1f} 度"],
            ['原生尺寸', fr['native']],
            ['印刷（工作照片框）', f"{s['print']['frame']}；{s['print']['crop']}；{'；'.join(s['print']['edges'])}；不能切：{s['print']['keep']}；{s['print']['need']}；判斷：{s['print']['verdict']}{s['print']['verify']}；{s['print']['ppi']}"],
            ['為何符合人設', s['why']], ['與同一人另一款的差異', s['vs_other']],
            ['參考照片（用途）', '；'.join(f"{r['id']}：{r['use']}（{r['note']}）" for r in s['refs'])],
            ['月份（已確認）', f"{s['month']} 月（{s['season']}）"]])
        L += ['', '| 風險 | 處理 |', '|---|---|'] + [f"| {cell(a)} | {cell(b)} |" for a, b in s['risks']]
        L += ['', f"prompt 草稿（{fr['ratio']}，尚未執行）：", '', '```text', s['prompt'], '```', '']

    c = d['composition']
    L += ['## 9. 構圖與生成提案', ''] + table(['款式', '建議'], [[x['k'], x['v']] for x in c['recommend']])
    L += ['', '**評估：**', ''] + [f'- {x}' for x in c['eval']] + ['', '**限制：**', ''] + [f'- {x}' for x in c['limits']] + ['', c['method'], '']

    e = d['execution']
    K, M = e['cost'], e['model']
    L += ['## 10. 費用（本輪不變；分開精確報價、歷史實扣、未知）', '', f"**狀態：** {K['status']}", '', f"**模型：** {M['recommend']}", '',
          f"**多階段與參考圖（R5 更正）：** {M['multi_stage']}", '',
          '### 10.1 精確報價（generate_image 的 get_cost 預檢，不送出工作）', '']
    L += table(['設定', '回傳'], [[x['cfg'], x['r']] for x in K['quote']])
    L += ['', K['quote_note'], '', '### 10.2 歷史實扣與紀錄', '']
    L += table(['項目', '數值', '依據', '等級', '來源檔'], [[x['k'], x['v'], x['basis'], x['level'], '、'.join(f'`{y}`' for y in x.get('src', []))] for x in K['history']])
    L += ['', '### 10.3 計價方式、張數、上限、異常', '']
    L += table(['項目', '說明', '來源檔'], [[x['k'], x['v'], '、'.join(f'`{y}`' for y in x.get('src', []))] for x in K['facts']])
    L += ['', '### 10.4 24 套獨立拍攝的情境試算（不是預算）', '']
    L += table(['情境', '請求數', '依 credits_exact 報價', '若實扣是顯示值（每次 1）'], [[x['k'], x['n'], x['exact'], x['display']] for x in K['scenarios']])
    L += ['', K['scenario_note'], '', '**未知：** ' + '、'.join(M['unknown']), '']
    I = K['iris_first']
    L += ['### 10.5 Iris 首張試拍提案（只是提案）', '', f"**推薦：{I['set']}**　{I['status_m4r1']}（歷史：{I['status_r7']}；{I['status_r6']}）", '',
          f"首試準備（工作流、待確認事項、首張驗收條件）見 `{os.path.basename(d['m4_prep']['doc'])}`。", ''] + [f'- {x}' for x in I['why']] + ['']
    L += table(['項目', '內容'], [[x['k'], x['v']] for x in I['plan']])
    L += ['', f"**授權：** {K['gate']}", '', '## 11. 要請 Penny 決定的事', '']
    L += [f'{i}. {q}' for i, q in enumerate(d['questions'], 1)] or ['沒有要請 Penny 決定的企劃事項：M-3 已完成（主管 M-4 R1 結論），不再要求 owner 填企劃問卷。首試的費用核准資訊見 `CAL_20_M4_IRIS_FIRST_TEST_PREP.md`。']
    L += ['', '## 12. 共同的皮膚與質感句（每段 prompt 結尾都加）', '', '```text', d['skin_line'], '```', '']
    return '\n'.join(L)


def render20(d):
    """V-Iris 首試準備：只排版企劃資料的 m4_prep 與 V-iris-chen 的已接受內容。"""
    M4 = d['m4_prep']
    s = [x for x in d['sets'] if x['id'] == M4['set']][0]
    src = lambda x: '、'.join(f'`{y}`' for y in x.get('src', []))
    C = M4['counts']
    L = [FIRST_20, '', f"# CAL_20 — {M4['title']}", '',
         f"> 資料檔：`data/cal_m3_shoot_plan.json`（{d['version']}，{d['round']}）的 `m4_prep` 與 `{s['id']}`。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。",
         f"> **{M4['status']}**", f"> R7：生成 {C['generated']}、credits {C['credits']}、Higgsfield 呼叫 {C['higgsfield_calls']}、報價預檢 {C['price_prechecks']}。"]
    R1 = M4['r1']
    C1 = R1['counts']
    L += [f"> M-4 R1：生成 {C1['generated']}、credits {C1['credits']}、生成任務 {C1['generation_jobs']}、訓練 {C1['trainings']}、上傳 {C1['uploads']}；{R1['counts_note']}", '',
          f"## 0. {R1['title']}", '', f"**結論：** {R1['verdict']}", '', '### 0.1 Soul 證據', '']
    L += table(['項目', '內容', '來源檔'], [[x['k'], x['v'], src(x)] for x in R1['soul']])
    L += ['', '### 0.2 當前模型參數與 Soul 狀態（2026-10-20 唯讀查詢）', '']
    L += table(['項目', '內容'], [[x['k'], x['v']] for x in R1['params']])
    L += ['', '### 0.3 首試單次請求的確切設定', '']
    L += table(['項目', '設定'], [[x['k'], x['v']] for x in R1['request']])
    L += ['', '### 0.4 報價（當前）與歷史紀錄（另列）', '']
    L += table(['報價', '回傳', '依據'], [[x['k'], x['v'], x['basis']] for x in R1['quote']])
    L += ['', '**歷史紀錄（不拿來估算本次）：**', '']
    L += table(['紀錄', '數值', '說明'], [[x['k'], x['v'], x['basis']] for x in R1['history']])
    L += ['', '### 0.5 計價單位', ''] + [f'- {x}' for x in R1['pricing']]
    L += ['', '### 0.6 失敗扣款規則', ''] + [f'- {x}' for x in R1['failure']]
    L += ['', '### 0.7 建議費用上限', '', f"**{R1['cap']['v']}**", '', R1['cap']['why'], '', '**停止條件：**', ''] + [f'- {x}' for x in R1['cap']['stop']] + ['', R1['cap']['stop_note']]
    L += ['', '### 0.8 交易核對：如何把本次請求與扣款對上', ''] + [f'{i}. {x}' for i, x in enumerate(R1['recon'], 1)]
    L += ['', '**限制：**', ''] + [f'- {x}' for x in R1['recon_limits']]
    L += ['', '### 0.9 剩餘阻礙', '']
    L += table(['阻礙', '說明', '誰決定'], [[x['k'], x['v'], x['who']] for x in R1['blockers']])
    L += ['', '**已不是阻礙：** ' + '、'.join(R1['not_blockers']) + '。', '', '**首張驗收要特別看的風險：** ' + '、'.join(R1['risks']) + '。', '',
          '## 1. 已接受的 V-Iris 企劃', '']
    L += table(['項目', '內容'], [[x['k'], x['v']] for x in M4['plan']])
    L += ['', '## 2. 身分參考', '']
    L += table(['項目', '內容', '來源檔'], [[x['k'], x['v'], src(x)] for x in M4['identity']])
    L += ['', '## 3. 最終 prompt 與生成比例', '', f"**生成比例：** {M4['ratio']}", '',
          f"prompt（已接受版本，{s['ratio']}，尚未執行；與企劃頁「prompt 草稿」逐字相同）：", '', '```text', s['prompt'], '```', '',
          '## 4. 工作流（依既有專案資料；前提未滿足前不執行）', '']
    L += table(['步驟', '內容', '來源檔'], [[x['k'], x['v'], src(x)] for x in M4['workflow']])
    L += ['', '## 5. 送生成前檢查（R7 預先核對；M-4 R1 主管接受三項差異；送出當下要再核一次）', '',
          '依 `SEXY_SCENE_LIBRARY.md` §25（Prompt Preflight Lint 10 項）與 `PHOTO_DIRECTION_STANDARD.md` §七（送生成前的稽核）。能機械判斷的項目由產生企劃資料的程式核對。', '']
    L += table(['檢查', '結果', '說明'], [[x['k'], x['r'], x['v']] for x in M4['lint']])
    L += ['', '## 6. 現在能準備的', ''] + [f'- {x}' for x in M4['ready_now']]
    L += ['', '## 7. 生成前的確認事項（M-4 R1 逐項狀態；不猜測）', '']
    L += table(['項目', '狀態', '說明', '來源檔'], [[x['k'], x['state'], x['v'], src(x)] for x in M4['tbc']])
    L += ['', '## 8. 首張驗收條件', '']
    for g in M4['accept']:
        L += [f"### {g['k']}", ''] + [f'- [ ] {x}' for x in g['items']] + ['']
    L += ['## 9. 這份文件不代表', ''] + [f'- {x}' for x in M4['not']] + ['']
    return '\n'.join(L)


def render19(d):
    o = d['owner_r2']
    s = o['summary']
    L = [FIRST_19, '', '# CAL_19 — M-3／R2 Owner 決策紀錄', '',
         f"> 資料檔：`data/cal_m3_owner_feedback_r2.json`（{o['recorded_on']}）。{o['note']}", '',
         f"**來源：** {o['source']}", '', '## 1. 逐字紀錄：Penny 最新決定（已生效，不重新詢問）', '', '```text', o['verbatim']['decisions'], '```', '',
         '## 2. 逐字紀錄：逐位 owner 回饋', '']
    for pid, text in o['verbatim']['per_person'].items():
        L += ['```text', text, '```', '']
        if pid == 'rainie-hsu':
            L += ['```text', o['verbatim']['shared_line_after_somi_coco_rainie'], '```', '', '（上一行原文接在 Somi、Coco、Rainie 三行之後。）', '']
    L += ['## 3. Rin 的 v2 替代方向（逐字讀出）', '', f"「{o['rin_v2_alt_exact']['text']}」", '', f"來源：{o['rin_v2_alt_exact']['from']}", '',
          '## 4. 執行摘要（整理，不是 Penny 原話）', '', '**已確定的雙款獨立策略：**', ''] + [f'- {x}' for x in s['decided']]
    L += ['', '**已接受的拍攝方向：**', ''] + [f"- {x['pid']}：{x['what']}" for x in s['accepted_directions']] + ['', s['accepted_note'], '',
          '**待修改的拍攝方向：**', ''] + [f'- {x}' for x in s['to_modify']]
    L += ['', f"**首試 Iris：** {s['iris_first']}", '', '**尚未授權：** ' + '、'.join(s['not_authorized']) + '。', '',
          '**尚未核准（本輪提出、待 Penny 拍板）：** ' + '、'.join(s['not_approved']) + '。', '']
    return '\n'.join(L)


def main():
    d = json.load(open(PLAN, encoding='utf-8'))
    docs = {OUT18: render18(d), OUT19: render19(d), OUT20: render20(d)}
    if '--check' in sys.argv:
        bad = [os.path.basename(p) for p, t in docs.items() if not os.path.exists(p) or open(p, encoding='utf-8').read() != t]
        print('PASS' if not bad else 'FAIL：文件與資料不一致，請重新產生：' + '、'.join(bad))
        return 1 if bad else 0
    for p, t in docs.items():
        with open(p, 'w', encoding='utf-8') as f:
            f.write(t)
        print('wrote', os.path.relpath(p, ROOT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
