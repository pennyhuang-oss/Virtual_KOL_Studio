#!/usr/bin/env python3
"""TASK-CAL-001／M-3（R2）— 由 data/cal_m3_shoot_plan.json（shoot-plan-v3，人寫企劃）產生兩份文件：
  CAL_18_M3_SHOOT_PLAN.md          24 套雙款企劃、兩本總覽與月份、構圖、費用與 Iris 首張提案
  CAL_19_M3_R2_OWNER_DECISION.md   Owner 決策紀錄（逐字回饋＋執行摘要；來源 data/cal_m3_owner_feedback_r2.json）
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
FIRST_LINE = 'TASK-CAL-001／M-3／R2｜24套雙款獨立寫真企劃｜送審報告'
ORIGIN_ZH = {'new': '新企劃', 'accepted-v2-main': 'Penny 已接受的 v2 主方向', 'accepted-v2-alt': 'Penny 採用的 v2 替代方向'}
BOOK_ZH = {'H': '橫式款', 'V': '直式款'}


def cell(s):
    return str(s).replace('|', '／').replace('\n', ' ')


def table(head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    return out + ['| ' + ' | '.join(cell(c) for c in r) + ' |' for r in rows]


def outfit_str(o):
    return '；'.join(f'{k}：{v}' for k, v in o.items())


def render18(d):
    m = d['meta']
    S = {s['id']: s for s in d['sets']}
    L = [FIRST_LINE, '', '# CAL_18 — M-3 24 套雙款獨立寫真企劃（shoot-plan-v3）', '',
         f"> 資料檔：`data/cal_m3_shoot_plan.json`（{d['version']}，{d['round']}，{d['written_on']}）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。",
         f"> **{m['status']}。** 本輪生成數 {d['counts']['generated']}、credits {d['counts']['credits']}、訓練數 {d['counts']['trainings']}。",
         '> 這是企劃，不是核准：24 套內容、月份、版面與 H／V 分配都待 Penny 拍板；生成與費用都未授權。Owner 決策逐字紀錄見 `CAL_19_M3_R2_OWNER_DECISION.md`。', '',
         '## 0. 版本', '']
    L += table(['項目', '內容'], [['名單', f"{m['roster']}；不換人"], ['上一版企劃', f"{d['revision']['from_version']}（commit `{d['revision']['from_commit']}`）"],
                                  ['這一版', d['revision']['summary']], ['素材頁版本', f"`{m['material_page_commit']}`"], ['桌曆基準', f"`{m['calendar_baseline']}`"]])
    L += ['', f"**參考照片：** {d['ref_note']}", '']

    L += ['## 1. Penny 回饋落實表', '']
    L += table(['人設', 'Penny 回饋（逐字）', '怎麼落實', '橫式款', '直式款'],
               [[p['name'], p['feedback'] + (f"（{p['shared']}）" if p['shared'] else ''), '；'.join(p['applied']), S[p['sets'][0]]['theme'], S[p['sets'][1]]['theme']] for p in d['people']])
    L.append('')

    for b in 'HV':
        L += [f"## {2 if b == 'H' else 3}. {BOOK_ZH[b]} 12 套總覽", '']
        rows = [s for s in d['sets'] if s['book'] == b]
        rows.sort(key=lambda s: s['month'])
        L += table(['月份（推薦）', 'ID', '主題', '環境', '服裝', '色彩', '姿態', '表情', '性感程度', '攝影方法', '景別'],
                   [[f"{s['month']} 月", s['id'], s['theme'], s['env'], outfit_str(s['outfit']), s['palette'], s['pose'] + s['hands'], s['expr'],
                     s['sexy'], s['method'], f"{s['frame']['shot_zh']}（{s['frame']['ratio']}）"] for s in rows])
        L.append('')

    L += ['## 4. 兩本月份推薦（待 Penny 拍板）', '']
    L += table(['月份', '橫式款', '理由', '直式款', '理由'],
               [[f"{x['m']} 月", f"{x['H']}（{S[x['H']]['name']}）", x['why_h'], f"{x['V']}（{S[x['V']]['name']}）", x['why_v']] for x in d['months']])
    L += [''] + [f'- {x}' for x in d['month_rules']] + ['']

    L += ['## 5. 24 套企劃', '']
    for n, s in enumerate(d['sets'], 1):
        fr = s['frame']
        L += [f"### 5.{n} {s['id']}｜{s['name']}｜{BOOK_ZH[s['book']]}（{ORIGIN_ZH[s['origin']]}）", '', f"**一句話：** {s['theme']}", '']
        L += table(['項目', '內容'], [
            ['場景', s['scene']], ['服裝', outfit_str(s['outfit'])], ['髮型', s['hair']], ['妝感', s['makeup']],
            ['身材設定（數字）', s['meas']], ['畫面上怎麼呈現胸型、腰線、臀腿', s['body_show']],
            ['主光', s['light']['主光']], ['補光', s['light']['補光']], ['姿態', s['pose']], ['手的位置', s['hands']],
            ['表情', s['expr']], ['視線', s['gaze']],
            ['景別與人物佔比', f"{fr['shot_zh']}；人物約佔{fr['pct_of']} {fr['pct']}%；{fr['ext_zh']}；{fr['space_zh']}"],
            ['焦段／距離／視野', f"{fr['ratio']}，{fr['f']}mm，約 {fr['d']} 公尺，視野 {fr['view_w']}×{fr['view_h']} 公尺"],
            ['原生尺寸', fr['native']], ['版面適配', fr['fit']],
            ['為何符合人設', s['why']], ['與同一人另一款的差異', s['vs_other']],
            ['參考照片（用途）', '；'.join(f"{r['id']}：{r['use']}（{r['note']}）" for r in s['refs'])],
            ['推薦月份', f"{s['month']} 月（{s['season']}）"]])
        L += ['', '| 風險 | 處理 |', '|---|---|'] + [f"| {cell(a)} | {cell(b)} |" for a, b in s['risks']]
        L += ['', f"prompt 草稿（{fr['ratio']}，尚未執行）：", '', '```text', s['prompt'], '```', '']

    c = d['composition']
    L += ['## 6. 構圖與生成提案', ''] + table(['款式', '建議'], [[x['k'], x['v']] for x in c['recommend']])
    L += ['', '**評估：**', ''] + [f'- {x}' for x in c['eval']] + ['', '**限制：**', ''] + [f'- {x}' for x in c['limits']] + ['', c['method'], '']

    e = d['execution']
    K, M = e['cost'], e['model']
    L += ['## 7. 費用（分開精確報價、歷史實扣、未知）', '', f"**狀態：** {K['status']}", '', f"**模型：** {M['recommend']}", '',
          '### 7.1 精確報價（generate_image 的 get_cost 預檢，不送出工作）', '']
    L += table(['設定', '回傳'], [[x['cfg'], x['r']] for x in K['quote']])
    L += ['', K['quote_note'], '', '### 7.2 歷史實扣與紀錄', '']
    L += table(['項目', '數值', '依據', '等級', '來源檔'], [[x['k'], x['v'], x['basis'], x['level'], '、'.join(f'`{y}`' for y in x.get('src', []))] for x in K['history']])
    L += ['', '### 7.3 計價方式、張數、上限、異常', '']
    L += table(['項目', '說明', '來源檔'], [[x['k'], x['v'], '、'.join(f'`{y}`' for y in x.get('src', []))] for x in K['facts']])
    L += ['', '### 7.4 24 套獨立拍攝的情境試算（不是預算）', '']
    L += table(['情境', '請求數', '依 credits_exact 報價', '若實扣是顯示值（每次 1）'], [[x['k'], x['n'], x['exact'], x['display']] for x in K['scenarios']])
    L += ['', K['scenario_note'], '', '**未知：** ' + '、'.join(M['unknown']), '']
    I = K['iris_first']
    L += ['### 7.5 Iris 首張試拍提案（只是提案）', '', f"**推薦：{I['set']}**", ''] + [f'- {x}' for x in I['why']] + ['']
    L += table(['項目', '內容'], [[x['k'], x['v']] for x in I['plan']])
    L += ['', f"**授權：** {K['gate']}", '', '## 8. 要請 Penny 決定的事', ''] + [f'{i}. {q}' for i, q in enumerate(d['questions'], 1)]
    L += ['', '## 9. 共同的皮膚與質感句（每段 prompt 結尾都加）', '', '```text', d['skin_line'], '```', '']
    return '\n'.join(L)


def render19(d):
    o = d['owner_r2']
    s = o['summary']
    L = [FIRST_LINE, '', '# CAL_19 — M-3／R2 Owner 決策紀錄', '',
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
