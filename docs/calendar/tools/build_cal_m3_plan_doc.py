#!/usr/bin/env python3
"""TASK-CAL-001／M-3（R4）— 由 data/cal_m3_shoot_plan.json（shoot-plan-v5，人寫企劃）產生兩份文件：
  CAL_18_M3_SHOOT_PLAN.md          R4 owner 紀錄、8 套已接受＋16 套修訂、攝影設計、兩本攝影總覽與月份、印刷構圖核對、費用與 Iris 首張
  CAL_19_M3_R2_OWNER_DECISION.md   R2 Owner 決策紀錄（逐字回饋＋執行摘要；來源 data/cal_m3_owner_feedback_r2.json；R3 起內容不變）
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
FIRST_LINE = 'TASK-CAL-001／M-3／R4｜16 套寫真修訂與印刷構圖核對｜送審報告'
FIRST_19 = 'TASK-CAL-001／M-3／R2｜24套雙款獨立寫真企劃｜送審報告'   # R2 的決策紀錄，標題不改
ORIGIN_ZH = {'new': '新企劃', 'accepted-v2-main': 'Penny 已接受的 v2 主方向', 'accepted-v2-alt': 'Penny 採用的 v2 替代方向'}
BOOK_ZH = {'H': '橫式款', 'V': '直式款'}


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
    return [[f"{s['month']} 月", f"{s['name']}（{s['id']}）", '已接受' if s['status'] == 'accepted' else '修訂', s['cam']['shot']['zh'], s['cam']['body']['short'], s['cam']['face']['zh'],
             s['cam']['gaze']['zh'], s['cam']['angle']['short'], s['cam']['pos'], s['cam']['focus']] for s in rows]


def render18(d):
    m = d['meta']
    S = {s['id']: s for s in d['sets']}
    Ph = d['photo']
    O3 = d['owner_r3']
    O4 = d['owner_r4']
    PR = d['printing']
    L = [FIRST_LINE, '', '# CAL_18 — M-3 24 套雙款寫真企劃、攝影設計與印刷構圖（shoot-plan-v5）', '',
         f"> 資料檔：`data/cal_m3_shoot_plan.json`（{d['version']}，{d['round']}，{d['written_on']}）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。",
         f"> **{m['status']}。** 本輪生成數 {d['counts']['generated']}、credits {d['counts']['credits']}、訓練數 {d['counts']['trainings']}。",
         '> R4 狀態：8 套已接受、16 套修訂待 Penny 定案；兩本月份人選排序已確認；版面（照片框）尚未定案；生成與費用都未授權。R2 的 Owner 決策逐字紀錄見 `CAL_19_M3_R2_OWNER_DECISION.md`。', '',
         '## 0. 版本', '']
    L += table(['項目', '內容'], [['名單', f"{m['roster']}；不換人"], ['上一版企劃', f"{d['revision']['from_version']}（commit `{d['revision']['from_commit']}`）"],
                                  ['這一版', d['revision']['summary']], ['素材頁版本', f"`{m['material_page_commit']}`"], ['桌曆基準', f"`{m['calendar_baseline']}`"]])
    L += ['', f"**參考照片：** {d['ref_note']}", '']

    Sm = O4['summary']
    L += ['## 1. R4：owner 決策（逐字，主管轉述）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r4.json`（{O4['recorded_on']}）。{O4['note']}", '',
          '```text', O4['verbatim']['decisions'], '```', '', '```text', O4['verbatim']['status'], '```', '',
          '**可執行摘要（整理，不是 Penny 原話）：**', '',
          f"- 已接受 8 套：{'、'.join(Sm['accepted'])}——服裝、場景、表情與攝影照 v4，不因整體偏好重設。",
          f"- 修訂 16 套：{'、'.join(Sm['revise'])}。{Sm['jia_note']}",
          f"- 月份：{Sm['months']}", f"- 整體：{'；'.join(Sm['overall'])}。", f"- 首試：{Sm['iris_first']}",
          f"- 尚未核准：{'、'.join(Sm['not_approved'])}。", '']
    L += ['## 1b. R3：Penny 的攝影設計要求（逐字，仍適用）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r3.json`（{O3['recorded_on']}）。{O3['note']}", '',
          '```text', O3['verbatim']['requirement'], '```', '', '```text', O3['verbatim']['keep_existing'], '```', '',
          '```text', O3['verbatim']['not_approved'], '```', '', f"**落實方式：** {Ph['summary']}", '']
    L += ['**共同規則：**', ''] + [f'- {x}' for x in Ph['rules']] + ['']

    L += ['## 2. 兩本攝影總覽（月份已確認；16 套修訂待 Penny 定案）', '']
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

    L += ['## 3. R4 16 套修訂：owner 原文、新主推薦與改了什麼', '', '主推薦都是主管推薦的修訂起點加上執行者的細化，尚未經 Penny 批准。', '']
    for s in d['sets']:
        if s['status'] != 'revised':
            continue
        L += [f"### {s['id']}｜{s['month']} 月｜{s['name']}", '', '```text', s['r4']['owner'], '```', '',
              f"- **新主推薦：** {s['theme']}", f"- **攝影：** {s['cam']['line']}", f"- **改了什麼：** {s['r4']['change']}", f"- **選擇理由：** {s['cam']['why']}", '']
    L += ['### 8 套已接受（不重設）', '']
    L += table(['ID', '月份', '主題', '攝影', '印刷判斷'], [[s['id'], f"{s['month']} 月", s['theme'], s['cam']['line'], s['print']['verdict']] for s in d['sets'] if s['status'] == 'accepted'])
    L += ['', PR['accepted_impact']['summary'], '']

    L += ['## 3b. 印刷規格與安全構圖（已知／假設／未知）', '', PR['note'], '', '**已知：**', '']
    L += table(['項目', '橫式', '直式', '來源'], [[x['k'], x['H'], x['V'], x['src']] for x in PR['known']])
    L += ['', '**假設（本案規劃用，不是廠商規格）：**', '']
    L += table(['項目', '橫式', '直式', '為什麼'], [[x['k'], x['H'], x['V'], x['why']] for x in PR['assumed']])
    L += ['', '**未知：**', ''] + [f'- {x}' for x in PR['unknown']]
    L += ['', '**暫定照片框與照片比例：**', '']
    L += table(['款', '暫定照片框', '畫布座標（mm）', '來源', '照片比例', '放入後', '日期區（暫定）'],
               [[BOOK_ZH[b], f"{PR['frames'][b]['name']} {PR['frames'][b]['mm'][0]}×{PR['frames'][b]['mm'][1]} mm（{PR['frames'][b]['ratio']}）",
                 '({},{})–({},{})'.format(*PR['frames'][b]['canvas']), PR['frames'][b]['from'], PR['fit'][b]['img'] + f"（{PR['fit'][b]['scaled']}）",
                 PR['fit'][b]['crop'], '({},{})–({},{})'.format(*PR['frames'][b]['date'])] for b in 'HV'])
    L += ['', '**如果改用其他框：**', ''] + [f"- {x['k']}：{x['v']}" for x in PR['compare']]
    L += ['', f"**示意圖：** 橫式 `decision_site/public/{PR['diagrams']['H']}`、直式 `decision_site/public/{PR['diagrams']['V']}`（只有方框與尺寸，不含照片；不是印刷安全證明）。", '',
          '**原則：**', ''] + [f'- {x}' for x in PR['rules']]
    L += ['', '### 3c. 24 套逐張印刷構圖判斷（依暫定照片框）', '']
    L += table(['ID', '狀態', '照片框', '比例裁切', '邊緣的重要部位', '不能切／需要的餘量', '判斷', '原生尺寸', '有效 ppi'],
               [[s['id'], '已接受' if s['status'] == 'accepted' else '修訂', s['print']['frame'], s['print']['crop'], '；'.join(s['print']['edges']),
                 f"{s['print']['keep']}／{s['print']['need']}", s['print']['verdict'], s['print']['native'], s['print']['ppi']] for s in d['sets']])
    I = PR['iris_first']
    L += ['', '### 3d. V-Iris 首試是否需要構圖微調', '', f"- {I['answer']}", f"- {I['condition']}", f"- {I['verify']}", '']

    L += ['## 4. R2 Penny 回饋落實表（歷史紀錄；R4 的最新決定見第 1、3 節）', '']
    L += table(['人設', 'Penny 回饋（逐字）', '怎麼落實', '橫式款', '直式款'],
               [[p['name'], p['feedback'] + (f"（{p['shared']}）" if p['shared'] else ''), '；'.join(p['applied']), S[p['sets'][0]]['theme'], S[p['sets'][1]]['theme']] for p in d['people']])
    L.append('')

    for b in 'HV':
        L += [f"## {5 if b == 'H' else 6}. {BOOK_ZH[b]} 12 套總覽", '']
        rows = [s for s in d['sets'] if s['book'] == b]
        rows.sort(key=lambda s: s['month'])
        L += table(['月份（已確認）', 'ID', '狀態', '主題', '環境', '服裝', '色彩', '姿態', '表情', '性感程度', '攝影方法', '景別｜身體方向｜臉與視線｜拍攝角度'],
                   [[f"{s['month']} 月", s['id'], '已接受' if s['status'] == 'accepted' else '修訂', s['theme'], s['env'], outfit_str(s['outfit']), s['palette'], s['pose'] + s['hands'], s['expr'],
                     s['sexy'], s['method'], s['cam']['line']] for s in rows])
        L.append('')

    L += ['## 7. 兩本月份（R4 已確認）', '']
    L += table(['月份', '橫式款', '理由', '直式款', '理由'],
               [[f"{x['m']} 月", f"{x['H']}（{S[x['H']]['name']}）", x['why_h'], f"{x['V']}（{S[x['V']]['name']}）", x['why_v']] for x in d['months']])
    L += [''] + [f'- {x}' for x in d['month_rules']] + ['']

    L += ['## 8. 24 套企劃', '']
    for n, s in enumerate(d['sets'], 1):
        fr, c = s['frame'], s['cam']
        st = '已接受（R4 owner 紀錄）' if s['status'] == 'accepted' else 'R4 修訂（待 Penny 定案）'
        L += [f"### 8.{n} {s['id']}｜{s['name']}｜{BOOK_ZH[s['book']]}（{ORIGIN_ZH[s['origin']]}｜{st}）", '', f"**一句話：** {s['theme']}", '',
              f"**攝影：** {c['line']}", '']
        L += table(['攝影欄位', '中文', 'prompt 對應句'], [
            ['1. 景別', c['shot']['zh'], c['shot']['en']], ['2. 畫面上下界', c['bounds']['zh'], c['bounds']['en']],
            ['3. 身體朝向', f"{c['body']['short']}：{c['body']['zh']}", c['body']['en']],
            ['4. 臉部朝向與視線', f"{c['face']['zh']}，{c['gaze']['zh']}", f"{c['face']['en']}, {c['gaze']['en']}"],
            ['5. 相機高度與俯仰', f"{c['angle']['zh']}（{c['angle']['ref']}）", c['angle']['en']],
            ['6. 畫面配置', c['comp']['zh'], c['comp']['en']], ['7. 攝影目的', c['purpose']['zh'], c['purpose']['en']]])
        L += ['', f"**選擇理由：** {c['why']}", '',
              (f"**R4：** {s['r4']['note']}" if s['status'] == 'accepted' else f"**R4 改了什麼：** {s['r4']['change']}"), '']
        crop = fr['shot'] in ('chest', 'waist', 'thigh', 'knee')
        size = f"頭頂上方留白約 {fr['headroom']}%" if crop else f"人物約佔{fr['fill_of']} {fr['fill']}%"
        L += table(['項目', '內容'], [
            ['場景', s['scene']], ['服裝', outfit_str(s['outfit'])], ['髮型', s['hair']], ['妝感', s['makeup']],
            ['身材設定（數字）', s['meas']], ['畫面上怎麼呈現胸型、腰線、臀腿', s['body_show']],
            ['主光', s['light']['主光']], ['補光', s['light']['補光']], ['姿態', s['pose']], ['手的位置', s['hands']],
            ['表情', s['expr']], ['視線', s['gaze']],
            ['焦段／距離／視野（參考）', f"{fr['ratio']}，{fr['f']}mm，約 {fr['d']} 公尺，視野 {fr['view_w']}×{fr['view_h']} 公尺；{size}；相機約 {fr['cam_m']} 公尺高、畫面中心約 {fr['centre_m']} 公尺高，俯仰約 {fr['tilt_deg']:+.1f} 度"],
            ['原生尺寸', fr['native']],
            ['印刷（暫定照片框）', f"{s['print']['frame']}；{s['print']['crop']}；{'；'.join(s['print']['edges'])}；不能切：{s['print']['keep']}；{s['print']['need']}；判斷：{s['print']['verdict']}；{s['print']['ppi']}"],
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
    L += ['### 10.5 Iris 首張試拍提案（只是提案）', '', f"**推薦：{I['set']}**", ''] + [f'- {x}' for x in I['why']] + ['']
    L += table(['項目', '內容'], [[x['k'], x['v']] for x in I['plan']])
    L += ['', f"**授權：** {K['gate']}", '', '## 11. 要請 Penny 決定的事', ''] + [f'{i}. {q}' for i, q in enumerate(d['questions'], 1)]
    L += ['', '## 12. 共同的皮膚與質感句（每段 prompt 結尾都加）', '', '```text', d['skin_line'], '```', '']
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
    docs = {OUT18: render18(d), OUT19: render19(d)}
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
