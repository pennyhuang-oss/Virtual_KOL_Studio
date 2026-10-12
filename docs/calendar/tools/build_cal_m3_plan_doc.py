#!/usr/bin/env python3
"""TASK-CAL-001／M-3 — 由 data/cal_m3_shoot_plan.json（人寫企劃）產生 CAL_18_M3_SHOOT_PLAN.md。

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
FIRST_LINE = 'TASK-CAL-001／M-3｜12 位人設專業寫真拍攝規劃｜送審報告'


def name_of(pid):
    i = json.load(open(os.path.join(ROOT, 'kols', pid, 'profile.json'), encoding='utf-8'))['identity']
    return f"{i['name']}（{i['native_name']}，{i['age']}）"


def cell(s):
    return str(s).replace('|', '／').replace('\n', ' ')


def render(d):
    L = [FIRST_LINE, '', '# CAL_18 — M-3 12 位人設專業寫真拍攝企劃', '']
    m = d['meta']
    L += [f"> 資料檔：`data/cal_m3_shoot_plan.json`（{d['version']}，{d['written_on']}）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。",
          f"> **{m['status']}。** 本輪生成數 {d['counts']['generated']}、credits {d['counts']['credits']}、訓練數 {d['counts']['trainings']}。",
          '> 這是企劃，不是核准：每一項都要 Penny 拍板，之後由主管另發執行指令。', '',
          '## 0. 版本與範圍', '',
          '| 項目 | 內容 |', '|---|---|',
          f"| 名單 | {m['roster']}；不換人，順序不是月份 |",
          f"| 素材頁版本 | `{m['material_page_commit']}` |",
          f"| 桌曆基準 | `{m['calendar_baseline']}` |",
          f"| Aaliya 圖片來源 | repo `{m['aaliya_sources']['repo_commit']}`；型錄分支 `{m['aaliya_sources']['catalog_branch']}` @ `{m['aaliya_sources']['catalog_commit']}` |",
          f"| 型錄頁 | {m['aaliya_sources']['catalog_url']} |",
          f"| 模型查詢 | {cell(m['aaliya_sources']['model_check'])} |", '']

    o = d['owner_refs']
    L += ['## 1. Penny 喜歡的 4 張（審美參考）', '', o['note'], '',
          '| 素材 ID | 照片 | 可借用的特徵 |', '|---|---|---|']
    L += [f"| {x['id']} | {cell(x['what'])} | {cell(x['cue'])} |" for x in o['items']]
    L += ['', o['reading'], '']

    a = d['aaliya']
    L += ['## 2. Aaliya 研究', '', f"**身分對應：** {m['aaliya_sources']['identity_note']}", '',
          f"**來源一致性：** {m['aaliya_sources']['note']}", '',
          f"**⚠ {a['warning']}**", '',
          '### 2.1 紀錄（有寫的 vs 沒寫的）', '',
          f"- face_reference：{a['records']['face_reference']}",
          f"- soul_test_v1：{a['records']['soul_test_v1']}",
          f"- 後製／中繼資料：{a['records']['post']}", '',
          '### 2.2 入選 5 張的證據表', '',
          '| # | 檔案（repo 路徑） | 尺寸 | 類別 | 模型 | 原始 prompt | Soul ID | 後製／裁切／增強 | 拍攝形式（目視） |',
          '|---|---|---|---|---|---|---|---|---|']
    for i, x in enumerate(a['items'], 1):
        L.append(f"| {i} | `{x['src']}` | {x['px'][0]}×{x['px'][1]} | {cell(x['kind'])} | {cell(x['model'])} | {cell(x['prompt'])} | {cell(x['soul'])} | {cell(x['post'])} | {cell(x['form'])} |")
    L += ['', '「尺寸」是本輪讀檔所得（實測）；「模型／prompt／Soul ID／後製」只照錄紀錄，紀錄沒有的寫「未知」或「推定」。', '',
          '### 2.3 目視觀察（不是紀錄）', '']
    for i, x in enumerate(a['items'], 1):
        L.append(f"{i}. **{x['form']}**：" + '；'.join(x['obs']) + '。')
    L += ['', f"未採用：{a['not_used']}", '', '### 2.4 可移植的方法（移植方法，不複製內容）', '',
          '| 項目 | 做法 |', '|---|---|']
    L += [f"| {x['item']} | {cell(x['how'])} |" for x in a['method']]
    L.append('')

    P = d['people']
    L += ['## 3. 12 位差異總表', '',
          '| 人設 | 企劃名稱 | 時段 | 光線 | 配色 | 場景 | 服裝類型 | 姿勢 | 表情 | 取景 | 首批 |',
          '|---|---|---|---|---|---|---|---|---|---|---|']
    for p in P:
        f = p['diff']
        L.append(f"| {name_of(p['pid'])} | {cell(p['title'])} | {f['time']} | {cell(f['light'])} | {f['palette']} | {f['place']} | {cell(f['outfit'])} | {f['pose']} | {f['face']} | {f['frame']} | {'是' if p['first'] else ''} |")
    L += ['', '**仍然接近、需要 Penny 判斷的地方（不宣稱已消除）：**', '']
    L += [f'- {x}' for x in d['overlap']]
    L.append('')

    L += ['## 4. 每位企劃', '',
          '每位一個主推薦、一個替代方向。「參考照片」是第二階段素材頁既有的照片 ID，只用來認人與看氣質，**不是新成品、不會照抄**；新企劃的照片**尚未生成**。',
          'prompt 是可直接使用的草稿，**尚未執行**；兩段（橫／直）只差取景句。', '']
    for n, p in enumerate(P, 1):
        L += [f"### 4.{n} {name_of(p['pid'])}｜{p['title']}" + ('（首批建議）' if p['first'] else ''), '',
              f"- **與人設核對：** {p['check']}",
              f"- **為什麼適合她：** {p['why']}",
              f"- **參考照片（既有）：** {'、'.join(p['refs'])}", '',
              '| 項目 | 內容 |', '|---|---|',
              f"| 場景 | {cell(p['scene'])} |", f"| 服裝 | {cell(p['outfit'])} |", f"| 髮型／髮色 | {cell(p['hair'])} |",
              f"| 配件 | {cell(p['acc'])} |", f"| 光線（主光／補光） | {cell(p['light'])} |", f"| 背景與色彩 | {cell(p['bg'])} |",
              f"| 表情與視線 | {cell(p['expr'])} |", f"| 姿勢與雙手 | {cell(p['pose'])} |",
              f"| 橫構圖 | {cell(p['frame_h'])} |", f"| 直構圖 | {cell(p['frame_v'])} |",
              f"| 甜美元素 | {cell(p['sweet'])} |", f"| 性感元素 | {cell(p['sexy'])} |",
              f"| 臉／髮頂／身形／日期區 | {cell(p['keep'])} |", f"| 替代方向 | {cell(p['alt'])} |", '',
              '| 風險 | 處理 |', '|---|---|']
        L += [f"| {cell(r['risk'])} | {cell(r['fix'])} |" for r in p['risks']]
        L += ['', '橫構圖 prompt 草稿（3:2，未執行）：', '', '```text', p['prompt_h'], '```', '',
              '直構圖 prompt 草稿（3:4，未執行）：', '', '```text', p['prompt_v'], '```', '']

    c = d['composition']
    L += ['## 5. 橫直構圖策略', '', f"**建議：{c['recommend']}。**", '']
    L += [f'- {x}' for x in c['why']]
    L += ['', f"**另一種做法：** {c['alt']}", '', '| 層次 | 說明 |', '|---|---|']
    L += [f"| {x['k']} | {cell(x['v'])} |" for x in c['layers']]
    L += ['', '每位在橫／直兩種構圖下臉、髮頂、身形、日期區能否保住，見第 4 節各位的「臉／髮頂／身形／日期區」列。', '']

    e = d['execution']
    md = e['model']
    L += ['## 6. 執行與成本建議（只是提案，不授權任何花費）', '', f"**模型：** {md['recommend']}", '']
    L += [f'- {x}' for x in md['why']]
    L += ['', '| 人設 | Soul 狀態（紀錄） |', '|---|---|']
    L += [f"| {x['who']} | {cell(x['status'])} |" for x in md['soul_status']]
    L += ['', 'Soul ID 不列在本文件與公開頁面。', '', '**已知限制：**', '']
    L += [f'- {x}' for x in md['known_limits']]
    L += ['', f"**多階段：** {md['multi_stage']}", '', '**未知：** ' + '、'.join(md['unknown']), '',
          '### 6.1 單價依據', '', '| 項目 | 數值 | 依據 | 等級 |', '|---|---|---|---|']
    co = e['cost']
    L += [f"| {x['k']} | {cell(x['v'])} | {cell(x['basis'])} | {x['level']} |" for x in co['unit']]
    L += ['', '### 6.2 數量與預算', '', '| 項目 | 內容 |', '|---|---|']
    L += [f"| {x['k']} | {cell(x['v'])} |" for x in co['plan']]
    L += ['', '### 6.3 首批建議人選', '', '| 人設 | 理由 |', '|---|---|']
    L += [f"| {x['who']} | {cell(x['why'])} |" for x in co['first_batch']]
    L += ['', '### 6.4 重生上限與停止條件', '']
    L += [f'- {x}' for x in co['retry']]
    L += ['', f"**授權：** {co['gate']}", '']

    L += ['## 7. 要請 Penny 決定的事', '']
    L += [f'{i}. {q}' for i, q in enumerate(d['questions'], 1)]
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
