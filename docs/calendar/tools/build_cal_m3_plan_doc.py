#!/usr/bin/env python3
"""TASK-CAL-001／M-3（R1）— 由 data/cal_m3_shoot_plan.json（人寫企劃）產生 CAL_18_M3_SHOOT_PLAN.md。

只排版既有文字，不新增內容；沒有呼叫任何生成服務。姓名取自 kols/<id>/profile.json 的 identity。
用法：python3 docs/calendar/tools/build_cal_m3_plan_doc.py           # 產生
      python3 docs/calendar/tools/build_cal_m3_plan_doc.py --check   # 核對文件與資料一致
"""
import json
import os
import subprocess
import sys

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
PLAN = os.path.join(ROOT, 'docs', 'calendar', 'data', 'cal_m3_shoot_plan.json')
OUT = os.path.join(ROOT, 'docs', 'calendar', 'CAL_18_M3_SHOOT_PLAN.md')
FIRST_LINE = 'TASK-CAL-001／M-3／R1｜專業寫真企劃修訂與費用查證｜送審報告'


def name_of(pid):
    i = json.load(open(os.path.join(ROOT, 'kols', pid, 'profile.json'), encoding='utf-8'))['identity']
    return f"{i['name']}（{i['native_name']}，{i['age']}）"


def cell(s):
    return str(s).replace('|', '／').replace('\n', ' ')


def table(head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    out += ['| ' + ' | '.join(cell(c) for c in r) + ' |' for r in rows]
    return out


def render(d):
    m = d['meta']
    R = d['revision']
    L = [FIRST_LINE, '', '# CAL_18 — M-3 12 位人設專業寫真拍攝企劃（R1 修訂版）', '',
         f"> 資料檔：`data/cal_m3_shoot_plan.json`（{d['version']}，{d['round']}，{d['written_on']}）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。",
         f"> **{m['status']}。** 本輪生成數 {d['counts']['generated']}、credits {d['counts']['credits']}、訓練數 {d['counts']['trainings']}。",
         '> 這是企劃，不是核准：每一項都要 Penny 拍板；生成放行目前是 BLOCK，之後由主管另發執行指令。', '',
         '## 0. 版本、範圍與主管覆核', '']
    L += table(['項目', '內容'], [
        ['名單', f"{m['roster']}；不換人，順序不是月份"], ['素材頁版本', f"`{m['material_page_commit']}`"],
        ['桌曆基準', f"`{m['calendar_baseline']}`"], ['上一版企劃', f"{R['from_version']}（commit `{R['from_commit']}`）"],
        ['Aaliya 圖片來源', f"repo `{m['aaliya_sources']['repo_commit']}`；型錄分支 `{m['aaliya_sources']['catalog_branch']}` @ `{m['aaliya_sources']['catalog_commit']}`"],
        ['型錄頁', m['aaliya_sources']['catalog_url']], ['模型查詢', m['aaliya_sources']['model_check']]])
    L += [''] + table(['主管覆核項目', '結論'], [[x['k'], x['v']] for x in R['verdicts']])
    L += ['', '**R1 移除的全組硬性規則**（不是專業寫真的必要條件）：' + '、'.join(R['method_removed']) + '。', '']

    o = d['owner_refs']
    L += ['## 1. Penny 喜歡的 4 張（審美參考，不變）', '', o['note'], '']
    L += table(['素材 ID', '照片', '可借用的特徵'], [[x['id'], x['what'], x['cue']] for x in o['items']])
    L += ['', o['reading'], '']

    a = d['aaliya']
    L += ['## 2. Aaliya 研究（主管 PASS；方法清單 R1 修訂）', '', f"**身分對應：** {m['aaliya_sources']['identity_note']}", '',
          f"**來源一致性：** {m['aaliya_sources']['note']}", '', f"**⚠ {a['warning']}**", '',
          '### 2.1 紀錄（有寫的 vs 沒寫的）', '',
          f"- face_reference：{a['records']['face_reference']}", f"- soul_test_v1：{a['records']['soul_test_v1']}",
          f"- 後製／中繼資料：{a['records']['post']}", '', '### 2.2 入選 5 張的證據表', '']
    L += table(['#', '檔案（repo 路徑）', '尺寸', '類別', '模型', '原始 prompt', 'Soul ID', '後製／裁切／增強', '拍攝形式（目視）'],
               [[i, f"`{x['src']}`", f"{x['px'][0]}×{x['px'][1]}", x['kind'], x['model'], x['prompt'], x['soul'], x['post'], x['form']]
                for i, x in enumerate(a['items'], 1)])
    L += ['', '「尺寸」是讀檔實測；「模型／prompt／Soul ID／後製」只照錄紀錄，紀錄沒有的寫「未知」或「推定」。', '', '### 2.3 目視觀察（不是紀錄）', '']
    L += [f"{i}. **{x['form']}**：" + '；'.join(x['obs']) + '。' for i, x in enumerate(a['items'], 1)]
    L += ['', f"未採用：{a['not_used']}", '', '### 2.4 可移植的方法（R1 修訂版）', '']
    L += table(['項目', '做法'], [[x['item'], x['how']] for x in a['method']])
    L.append('')

    P = d['people']
    L += ['## 3. 12 位差異總表', '']
    L += table(['人設', '企劃名稱', '修訂', '時段', '光線', '配色', '場景', '服裝', '姿勢', '表情', '取景', '第一階段'],
               [[name_of(p['pid']), p['title'], '主方向' if p['rev'] == 'direction' else '姿態與細節', p['diff']['time'], p['diff']['light'], p['diff']['palette'],
                 p['diff']['place'], p['diff']['outfit'], p['diff']['pose'], p['diff']['face'], p['diff']['frame'], '建議' if p['first'] else ''] for p in P])
    L += ['', '**仍然接近、需要 Penny 判斷的地方（不宣稱已消除）：**', ''] + [f'- {x}' for x in d['overlap']] + ['']

    L += ['## 4. 每位企劃', '',
          '每位一個主推薦、一個替代方向。「參考照片」是第二階段素材頁既有的照片 ID，只用來認人與看氣質，**不是新成品、不會照抄**；新企劃的照片**尚未生成**。',
          'prompt 是可直接使用的草稿，**尚未執行**；橫、直兩段的取景句依各自的取景設計寫成。', '']
    for n, p in enumerate(P, 1):
        H, V = p['frames']['H'], p['frames']['V']
        L += [f"### 4.{n} {name_of(p['pid'])}｜{p['title']}" + ('（第一階段建議）' if p['first'] else ''), '',
              f"**R1 修訂（{'主方向' if p['rev'] == 'direction' else '姿態與細節'}）：**" + ('' if p['prev']['title'] == p['title'] else f"舊版標題「{p['prev']['title']}」。"), '']
        L += [f'- {x}' for x in p['rev_items']]
        L += ['', f"- **與人設核對：** {p['check']}", f"- **為什麼適合她：** {p['why']}", f"- **參考照片（既有）：** {'、'.join(p['refs'])}"]
        if p['check9']:
            L += ['- **逐項檢查：** ' + '；'.join(p['check9'])]
        L += [f"- **舊版姿勢：** {p['prev']['pose']}", '']
        L += table(['項目', '內容'], [['場景', p['scene']], ['服裝', p['outfit']], ['髮型／髮色', p['hair']], ['配件', p['acc']], ['光線', p['light']],
                                      ['表情', p['expr']], ['姿勢與雙手', p['pose']], ['甜美元素', p['sweet']], ['性感元素', p['sexy']], ['替代方向', p['alt']]])
        L += ['', '**取景設計：**', '']
        L += table(['', '橫 3:2', '直 3:4'], [
            ['景別', H['shot_zh'], V['shot_zh']], ['人物佔畫面高度', f"約 {H['pct']}%", f"約 {V['pct']}%"],
            ['頭頂／手腳範圍', H['ext_zh'], V['ext_zh']], ['留白位置', H['space_zh'], V['space_zh']],
            ['焦段／距離', f"{H['f']}mm／約 {H['d']} 公尺", f"{V['f']}mm／約 {V['d']} 公尺"],
            ['視野（寬×高，公尺）', f"{H['view_w']}×{H['view_h']}", f"{V['view_w']}×{V['view_h']}"],
            ['人物範圍高度（公尺）', H['extent'], V['extent']], ['模型原生輸出', H['native'], V['native']], ['版面適配', H['fit'], V['fit']]])
        L += ['', '| 風險 | 處理 |', '|---|---|'] + [f"| {cell(r['risk'])} | {cell(r['fix'])} |" for r in p['risks']]
        L += ['', '橫構圖 prompt 草稿（3:2，未執行）：', '', '```text', p['prompt_h'], '```', '',
              '直構圖 prompt 草稿（3:4，未執行）：', '', '```text', p['prompt_v'], '```', '']

    c = d['composition']
    L += ['## 5. 橫直構圖策略（R1 修訂）', '', f"**建議：{c['recommend']}。**", ''] + [f'- {x}' for x in c['why']]
    L += ['', f"**另一種做法：** {c['alt']}", '', '**換算與檢查：**', ''] + [f'- {x}' for x in c['checks']] + ['']
    L += table(['層次', '說明'], [[x['k'], x['v']] for x in c['layers']])
    L.append('')

    e = d['execution']
    md, K = e['model'], e['cost']
    L += ['## 6. 執行與費用（R1 唯讀查證）', '', f"**狀態：** {K['status']}", '', f"**模型：** {md['recommend']}", '']
    L += table(['人設', 'Soul 狀態（紀錄）'], [[x['who'], x['status']] for x in md['soul_status']])
    L += ['', 'Soul ID 不列在本文件與公開頁面。', '', '### 6.1 歷史實際扣款', '']
    L += table(['項目', '數值', '依據', '等級', '來源檔'], [[x['k'], x['v'], x['basis'], x['level'], '、'.join(f'`{y}`' for y in x.get('src', []))] for x in K['history']])
    L += ['', '### 6.2 今天的工具報價（get_cost 預檢，2026-10-13）', '']
    L += table(['設定', '回傳'], [[x['cfg'], x['r']] for x in K['quote']])
    L += ['', K['quote_note'], '', '### 6.3 計價方式、每次張數、費用上限、異常', '']
    L += table(['項目', '說明', '來源檔'], [[x['k'], x['v'], '、'.join(f'`{y}`' for y in x.get('src', []))] for x in K['facts']])
    L += ['', '### 6.4 撤回的數字', ''] + [f'- {x}' for x in K['withdrawn']]
    L += ['', '### 6.5 分階段測試（提案）', ''] + table(['項目', '內容'], [[x['k'], x['v']] for x in K['phases']])
    L += ['', '**為什麼第一階段是 Iris：**', ''] + [f'- {x}' for x in K['why_iris']]
    L += ['', '**已知限制：**', ''] + [f'- {x}' for x in md['known_limits']]
    L += ['', f"**多階段：** {md['multi_stage']}", '', '**未知：** ' + '、'.join(md['unknown']), '', f"**授權：** {K['gate']}", '']

    L += ['## 7. 要請 Penny 決定的事', ''] + [f'{i}. {q}' for i, q in enumerate(d['questions'], 1)]
    L += ['', '## 8. 共同的皮膚與質感句（每段 prompt 結尾都加）', '', '```text', d['skin_line'], '```', '']
    return '\n'.join(L)


def main():
    d = json.load(open(PLAN, encoding='utf-8'))
    text = render(d)
    if '--check' in sys.argv:
        ok = open(OUT, encoding='utf-8').read() == text
        print('PASS' if ok else 'FAIL：文件與資料不一致，請重新產生')
        return 0 if ok else 1
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(text)
    print('wrote', os.path.relpath(OUT, ROOT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
