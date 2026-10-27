#!/usr/bin/env python3
"""TASK-CAL-001／M-4（R5）— 由 data/cal_m3_shoot_plan.json（shoot-plan-v11，人寫企劃）產生五份文件：
  CAL_18_M3_SHOOT_PLAN.md          主管結論（M-3 完成）、23 套已接受＋H-Luna 主管覆核通過、攝影設計、兩本攝影總覽與月份、印刷構圖核對、費用與 Iris 首張
  CAL_19_M3_R2_OWNER_DECISION.md   R2 Owner 決策紀錄（逐字回饋＋執行摘要；來源 data/cal_m3_owner_feedback_r2.json；R3 起內容不變）
  CAL_20_M4_IRIS_FIRST_TEST_PREP.md  V-Iris 首試準備（R7 起）、首試前核查（M-4 R1 起）、單張首試結果（M-4 R2 起）與 Penny 定案（M-4 R4）；企劃資料的 m4_prep
  CAL_21_M4_BATCH1_PREP.md         第一批 5 位角色的生成準備（M-4 R4；來源 data/cal_m4_batch1_prep.json）：完整 prompt、差異、Soul 證據、設定與報價；
                                   prompt 必須等於已接受企劃原文套用資料檔列出的光線句改寫，產生器逐張核對
  CAL_22_M4_BATCH1_RESULTS.md      第一批 5 位的生成結果（M-4 R5；來源 data/cal_m4_batch1_run.json）：最終送出 prompt 與差異、原圖、驗收、
                                   像素與 ppi、逐筆扣款與歸屬；送出 prompt 必須等於 CAL_21 原文（V-Rin 只套用授權的景別用語修正），產生器逐張核對
只排版既有文字，不新增內容；沒有呼叫任何生成服務。
用法：python3 docs/calendar/tools/build_cal_m3_plan_doc.py           # 產生
      python3 docs/calendar/tools/build_cal_m3_plan_doc.py --check   # 核對文件與資料一致
"""
import json
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
CAL = os.path.join(ROOT, 'docs', 'calendar')
PLAN = os.path.join(CAL, 'data', 'cal_m3_shoot_plan.json')
OUT18 = os.path.join(CAL, 'CAL_18_M3_SHOOT_PLAN.md')
OUT19 = os.path.join(CAL, 'CAL_19_M3_R2_OWNER_DECISION.md')
OUT20 = os.path.join(CAL, 'CAL_20_M4_IRIS_FIRST_TEST_PREP.md')
OUT21 = os.path.join(CAL, 'CAL_21_M4_BATCH1_PREP.md')
BATCH = os.path.join(CAL, 'data', 'cal_m4_batch1_prep.json')
OUT22 = os.path.join(CAL, 'CAL_22_M4_BATCH1_RESULTS.md')
RUN = os.path.join(CAL, 'data', 'cal_m4_batch1_run.json')
AUTH = os.path.join(CAL, 'data', 'cal_m4_auth_r5.json')
FIRST_LINE = 'TASK-CAL-001／M-4／R6｜主管覆核 REVISE｜修正重審規則與構圖矛盾｜送審報告'
FIRST_20 = 'TASK-CAL-001／M-4／R4｜V-Iris 首試準備、首試前核查、單張首試與定案（Penny 接受）'
FIRST_19 = 'TASK-CAL-001／M-3／R2｜24套雙款獨立寫真企劃｜送審報告'   # R2 的決策紀錄，標題不改
ORIGIN_ZH = {'new': '新企劃', 'accepted-v2-main': 'Penny 已接受的 v2 主方向', 'accepted-v2-alt': 'Penny 採用的 v2 替代方向'}
BOOK_ZH = {'H': '橫式款', 'V': '直式款'}
ST_ZH = {'accepted': '已接受', 'owner_revised': '依owner指定修訂，待主管核對落實', 'supervisor_verified': '依owner指示修訂，主管覆核通過'}


def progress(d):
    """24 套進度：四類互斥（已接受＋待 Penny 選片＋退回待重規劃＋尚未生成；M-4 R20 起加入待選片）；待完成合計與累計已生成另計。"""
    PR = d['status']['production']
    assert PR['accepted'] + PR['pending_owner_review'] + PR['rejected_replan'] + PR['not_generated'] == PR['sets_total'] == 24
    assert PR['to_complete'] == PR['pending_owner_review'] + PR['rejected_replan'] + PR['not_generated'] and PR['generated_cumulative'] == sum(PR['generated_log'].values()) >= PR['accepted'] + PR['rejected_replan']
    return (f"{PR['sets_total']} 套＝已接受 {PR['accepted']}＋待 Penny 選片 {PR['pending_owner_review']}＋退回待重規劃 {PR['rejected_replan']}＋尚未生成 {PR['not_generated']}；"
            f"待完成合計 {PR['to_complete']}（累計已生成 {PR['generated_cumulative']} 張，另計"
            + (f"；構圖底稿另計 {PR['drafts']['generated']} 張，不是月面照片" if 'drafts' in PR else '') + '）。')


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
         f"> **{m['status']}。** 生成數 {d['counts']['generated']}、credits {d['counts']['credits']}、訓練數 {d['counts']['trainings']}"
         + (f"；構圖底稿另計：生成 {d['draft_counts']['generated']}、credits {d['draft_counts']['credits']}（不是月面照片）" if 'draft_counts' in d else '') + f"（{d['counts_note']}）",
         '> R4 狀態（歷史）：8 套已接受、16 套修訂待 Penny 定案；兩本月份人選排序已確認；版面（照片框）尚未定案；生成與費用都未授權。R2 的 Owner 決策逐字紀錄見 `CAL_19_M3_R2_OWNER_DECISION.md`。',
         '> R5：只修資料一致性與措辭（見 0b），沒有攝影方向變更。',
         '> R6 狀態（歷史）：22 套已接受；H-jia-seo、H-luna-tanaka 兩套新推薦待 Penny 定案；兩本月份與工作照片框已接受（工作版型，不是廠商規格、印刷安全或成品核准）。',
         '> R7 狀態（歷史）：23 套已接受（加上 H-jia-seo）；H-luna-tanaka 依 Penny 指定只把手部改為雙手輕捧日式小香袋，當時記為「依owner指定修訂，待主管核對落實」。',
         '> M-4 R1 狀態（歷史）：主管結論 M-3／R7 PASS，M-3 完成——23 套 owner 接受＋H-Luna 依 owner 指示修訂、主管覆核通過（Penny 沒有看過修訂後的版本）；不再要求 owner 填企劃問卷。',
         f"> M-4 R2 狀態（歷史）：{d['m4_prep']['r2']['status']}{d['m4_prep']['r2']['verdict']}",
         f"> M-4 R4 狀態（歷史）：{d['m4_prep']['r4']['status']}（{d['m4_prep']['r4']['supersedes']}）；首試紀錄見 `CAL_20_M4_IRIS_FIRST_TEST_PREP.md`。",
         "> M-4 R5 狀態（歷史）：第一批 5 位各生成 1 張並上線審圖；生成準備見 `CAL_21_M4_BATCH1_PREP.md`，結果與扣款見 `CAL_22_M4_BATCH1_RESULTS.md`。",
         f"> **M-4 R6 狀態：{d['m4r6']['batch1_line']} {progress(d)}以下 24 套是採用重審提案前的原文。**", '',
         *([f"> **{d['m4r7']['status_line']}** 試拍紀錄見 `data/cal_m4_r7_trial.json`，主管結論見 `data/cal_m4_supervisor_r7.json`，後續測試方案見 `CAL_24_M4_R7_SOMI_FOLLOWUP.md`。", ''] if 'm4r7' in d else []),
         *([f"> **{d['m4r8']['status_line']}** 測試紀錄見 `data/cal_m4_r8_trial.json`，主管結論見 `data/cal_m4_supervisor_r8.json`，構圖控制流程查核見 `CAL_25_M4_R8_FLOW_CHECK.md`。", ''] if 'm4r8' in d else []),
         *([f"> **{d['m4r9']['status_line']}** 底稿紀錄見 `data/cal_m4_r9_draft.json`，主管結論見 `data/cal_m4_supervisor_r9.json`，修訂 prompt 見 `CAL_26_M4_R9_DRAFT_REVISION.md`。", ''] if 'm4r9' in d else []),
         *([f"> **{d['m4r10']['status_line']}** 底稿紀錄與第二步提案見 `data/cal_m4_r10_draft.json`。", ''] if 'm4r10' in d else []),
         *([f"> **{d['m4r11']['status_line']}** 測試紀錄見 `data/cal_m4_r11_trial.json`，主管結論見 `data/cal_m4_supervisor_r11.json`。", ''] if 'm4r11' in d else []),
         *([f"> **{d['m4r12']['status_line']}** 測試包見 `data/cal_m4_r12_edit_prep.json`。", ''] if 'm4r12' in d else []),
         *([f"> **{d['m4r13']['status_line']}** 前置核對見 `data/cal_m4_r13_somi_precheck.json`，製作卡見 `CAL_27_M4_R13_NEXT_CARDS.md`。", ''] if 'm4r13' in d else []),
         *([f"> **{d['m4r13b']['status_line']}** 前置核對與遮罩見 `data/cal_m4_r13b_somi_precheck.json`。", ''] if 'm4r13b' in d else []),
         *([f"> **{d['m4r14']['status_line']}** 試拍紀錄見 `data/cal_m4_r14_trial.json`。", ''] if 'm4r14' in d else []),
         *([f"> **{d['m4r15']['status_line']}** 主管覆核見 `data/cal_m4_supervisor_r14.json`，收尾與 Rin 修訂 prompt 見 `data/cal_m4_r15_followup.json`。", ''] if 'm4r15' in d else []),
         *([f"> **{d['m4r16']['status_line']}** 授權與 Penny 決定見 `data/cal_m4_auth_r16.json`，試拍紀錄見 `data/cal_m4_r16_trial.json`。", ''] if 'm4r16' in d else []),
         *([f"> **{d['m4r17']['status_line']}** 主管比較與 Penny 原話見 `data/cal_m4_supervisor_r16.json`。", ''] if 'm4r17' in d else []),
         *([f"> **{d['m4r17b']['status_line']}** Penny 原話見 `data/cal_m4_owner_r17b.json`。", ''] if 'm4r17b' in d else []),
         *([f"> **{d['m4r18']['status_line']}** 試拍紀錄見 `data/cal_m4_r18_trial.json`。", ''] if 'm4r18' in d else []),
         *([f"> **{d['m4r19']['status_line']}** Penny 原話見 `data/cal_m4_owner_r19.json`，主管覆核見 `data/cal_m4_supervisor_r18.json`，Yerin 修訂見 `data/cal_m4_r19_followup.json`。", ''] if 'm4r19' in d else []),
         *([f"> **{d['m4r20']['status_line']}** 授權見 `data/cal_m4_auth_r20.json`，製作與自查紀錄見 `data/cal_m4_r20_trial.json`，選片頁資料見 `data/cal_pick_r20.json`。", ''] if 'm4r20' in d else []),
         '## 0. 版本', '']
    L += table(['項目', '內容'], [['名單', f"{m['roster']}；不換人"], ['上一版企劃', f"{d['revision']['from_version']}（commit `{d['revision']['from_commit']}`）"],
                                  ['這一版', d['revision']['summary']], ['M-4 R2（歷史）', f"{d['m4r2']['summary']}（基準 commit `{d['m4r2']['from_commit']}`）"], ['M-4 R1（歷史）', f"{d['m4r1']['summary']}（基準 commit `{d['m4r1']['from_commit']}`）"], ['R7（歷史）', f"{d['r7']['summary']}（基準 commit `{d['r7']['from_commit']}`）"], ['R6（歷史）', f"{d['r6']['summary']}（基準 commit `{d['r6']['from_commit']}`）"],
                                  ['R5 資料修訂', f"{d['r5']['summary']}（基準 commit `{d['r5']['from_commit']}`）"],
                                  ['素材頁版本', f"`{m['material_page_commit']}`"], ['桌曆基準', f"`{m['calendar_baseline']}`"]])
    L += ['', f"**參考照片：** {d['ref_note']}", '']
    L += ['## 0a. M-4 R2 修改（差異）', '', f"{d['m4r2']['summary']}", '']
    L += table(['類別', '位置', '舊', '新'], [[x['kind'], x['where'], x['old'], x['new']] for x in d['m4r2']['changes']])
    L += ['', '## 0b. M-4 R1 修改（差異，歷史）', '', f"{d['m4r1']['summary']}", '']
    L += table(['類別', '位置', '舊', '新'], [[x['kind'], x['where'], x['old'], x['new']] for x in d['m4r1']['changes']])
    L += ['', '## 0c. R7 修改（差異，歷史）', '', f"{d['r7']['summary']}", '']
    L += table(['類別', '位置', '舊', '新'], [[x['kind'], x['where'], x['old'], x['new']] for x in d['r7']['changes'] if x['kind'] != '狀態（owner 決策）'])
    L += ['', f"狀態：{sum(1 for x in d['r7']['changes'] if x['kind'] == '狀態（owner 決策）')} 套由「R6 待決」改為「已接受」（R7 owner 紀錄：H-jia-seo）；H-luna-tanaka 記為「依owner指定修訂，待主管核對落實」。", '']
    L += ['## 0d. R6 修改（差異，歷史）', '', f"{d['r6']['summary']}", '']
    L += table(['類別', '位置', '舊', '新'], [[x['kind'], x['where'], x['old'], x['new']] for x in d['r6']['changes'] if x['kind'] != '狀態（owner 決策）'])
    L += ['', f"狀態：{sum(1 for x in d['r6']['changes'] if x['kind'] == '狀態（owner 決策）')} 套由「修訂」改為「已接受」（R6 owner 紀錄）。", '']
    L += ['## 0e. R5 資料修訂（差異，歷史）', '', '**不變：** ' + '；'.join(d['r5']['unchanged']) + '。', '']
    L += table(['類別', '位置', '舊', '新'], [[x['kind'], x['where'], x['old'], x['new']] for x in d['r5']['changes'] if not x['where'].startswith('sets[') or x['kind'] != '印刷措辭'])
    L += ['', f"另有 24 套逐張印刷文字的措辭修訂（共 {sum(1 for x in d['r5']['changes'] if x['where'].startswith('sets[') and x['kind'] == '印刷措辭')} 套），新文字見 3c；舊文字保留在資料檔 `r5.changes`。", '']

    AU = d['auth_m4r2']
    L += ['## 1. 授權與主管覆核（M-4 R2，逐字）', '', f"> 資料檔：`data/cal_m4_authorization_r2.json`（{AU['recorded_on']}）。{AU['source']}{AU['note']}", '',
          '```text', AU['verbatim']['authorization'], '```', '', '**主管對 R1 的覆核（逐字）：**', '', '```text', AU['verbatim']['r1_review'], '```', '']
    SU = d['sup_m4r1']
    L += ['## 1a. 主管結論（M-4 R1，歷史，逐字）', '', f"> 資料檔：`data/cal_m4_supervisor_r1.json`（{SU['recorded_on']}）。{SU['source']}{SU['note']}", '',
          '```text', SU['verbatim']['conclusion'], '```', '', '**本輪指示（逐字）：**', '', '```text', SU['verbatim']['instructions'], '```', '']
    O7 = d['owner_r7']
    S7 = O7['summary']
    L += ['## 1b. R7：owner 決策（歷史，逐字，主管轉述）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r7.json`（{O7['recorded_on']}）。{O7['source']}{O7['note']}", '',
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
    L += ['## 1c. R6：owner 決策（歷史，逐字，主管轉述）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r6.json`（{O6['recorded_on']}）。{O6['source']}{O6['note']}", '',
          '```text', O6['verbatim']['decisions'], '```', '', '**Penny 對兩套的原文回饋：**', '']
    for sid, x in O6['verbatim']['per_set'].items():
        L += [f"- {sid}（{x['month']} 月）：「{x['text']}」"]
    L += ['', '**可執行摘要（整理，不是 Penny 原話）：**', '',
          f"- 已接受 22 套（R4 的 8 套＋R6 的 14 套）：{'、'.join(S6['accepted'])}——拍攝內容與 prompt 不變，不再要求回覆。",
          f"- 待決 2 套：{'、'.join(S6['pending'])}（R6 新推薦，見第 3 節）。", f"- 月份：{S6['months']}", f"- 照片框：{S6['frames']}",
          f"- 首試：{S6['iris_first']}", f"- 尚未核准：{'、'.join(S6['not_approved'])}。", '']
    Sm = O4['summary']
    L += ['## 1d. R4：owner 決策（歷史，逐字，主管轉述）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r4.json`（{O4['recorded_on']}）。{O4['note']}", '',
          '```text', O4['verbatim']['decisions'], '```', '', '```text', O4['verbatim']['status'], '```', '',
          '**可執行摘要（整理，不是 Penny 原話）：**', '',
          f"- 已接受 8 套：{'、'.join(Sm['accepted'])}——服裝、場景、表情與攝影照 v4，不因整體偏好重設。",
          f"- 修訂 16 套：{'、'.join(Sm['revise'])}。{Sm['jia_note']}",
          f"- 月份：{Sm['months']}", f"- 整體：{'；'.join(Sm['overall'])}。", f"- 首試：{Sm['iris_first']}",
          f"- 尚未核准：{'、'.join(Sm['not_approved'])}。", '']
    L += ['## 1e. R3：Penny 的攝影設計要求（逐字，仍適用）', '', f"> 資料檔：`data/cal_m3_owner_feedback_r3.json`（{O3['recorded_on']}）。{O3['note']}", '',
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
    L += ['### 10.5 Iris 首張試拍', '', f"**{I['set']}**　M-4 R4：{d['m4_prep']['r4']['status']}（歷史：{I['status_m4r2']}；{I['status_m4r1']}；{I['status_r7']}；{I['status_r6']}）", '',
          f"首試準備（工作流、待確認事項、首張驗收條件）見 `{os.path.basename(d['m4_prep']['doc'])}`。", ''] + [f'- {x}' for x in I['why']] + ['']
    L += table(['項目', '內容'], [[x['k'], x['v']] for x in I['plan']])
    L += ['', f"**授權：** {K['gate']}", '', '## 11. 要請 Penny 決定的事', '']
    L += [f'{i}. {q}' for i, q in enumerate(d['questions'], 1)] or ['沒有要請 Penny 決定的企劃事項：M-3 已完成（主管 M-4 R1 結論），不再要求 owner 填企劃問卷。V-Iris 首試 Penny 已接受（M-4 R4，含反光板），不再詢問；第一批 5 張 Penny 已全數退回（M-4 R6）；24 套重審與重建提案見 `CAL_23_M4_R6_REPLAN.md`，其中需要 Penny 決定的事項列在該文件第 8 節。']
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
    R2 = M4['r2']
    C2 = R2['counts']
    L += [f"> M-4 R2：生成請求 {C2['generation_requests']}、圖片 {C2['images']}、重送 {C2['retries']}、實扣 {C2['credits_charged']} credits（{R2['attribution']['level']}）、訓練 {C2['trainings']}、上傳 {C2['uploads']}。"]
    R4 = M4['r4']
    L += [f"> M-4 R1：生成 {C1['generated']}、credits {C1['credits']}、生成任務 {C1['generation_jobs']}、訓練 {C1['trainings']}、上傳 {C1['uploads']}；{R1['counts_note']}", '',
          f"## R4. {R4['title']}", '', f"**狀態：** {R4['status']}。{R4['supersedes']}。{R4['not']}", '', f"**Penny 的回饋（{R4['source']}）：**", '', '```text', '\n'.join(R4['owner']), '```', '',
          f"**接受項目：** {'、'.join(R4['accepted'])}。逐字紀錄：`{R4['file']}`。", '',
          f"## A. {R2['title']}", '', f"**R2 當時狀態：** {R2['status']}", '', f"**判定：** {R2['verdict']}", '', f"**授權：** {R2['auth']}", '', '### A.1 送出前核對', '']
    L += table(['項目', '結果'], [[x['k'], x['v']] for x in R2['pre']])
    J2 = R2['job']
    L += ['', '### A.2 實際設定與任務', '', f"**送出：** {R2['request']}", '', f"**任務：** {J2['status']}（輪詢 {J2['polls']} 次）；輸出 {J2['px'][0]}×{J2['px'][1]}。{J2['observed']}", '',
          f"**原圖：** `{R2['src'][0]}`（私有 repo；不放公開頁）。套框預覽、裁切檢視與執行紀錄：`{R2['src'][1]}`。", '', '### A.3 逐項驗收', '']
    L += table(['類別', '條件', '結果', '說明'], [[g['k'], x['c'], x['r'], x['v']] for g in R2['accept'] for x in g['items']])
    CH = R2['charge']
    L += ['', '### A.4 交易與歸屬', '', '| 項目 | 內容 |', '|---|---|',
          f"| 扣款 | {'；'.join(f'{x['at']} {x['credits']}' for x in CH['spend'])} |", f"| 退款 | {'；'.join(f'{x['at']} {x['credits']}' for x in CH['refund']) or '無'} |",
          f"| 淨額 | {CH['net']}（精確報價 {CH['quote_exact']}；核准預算 {CH['budget']} credit；查到 {CH['checked_at']}） |", f"| 異常 | {CH['anomaly']} |",
          f"| 歸屬層級 | **{R2['attribution']['level']}**；{R2['attribution']['not']} |", '', '**依據：**', ''] + [f'- {x}' for x in R2['attribution']['basis']]
    L += ['', '### A.5 停止', '', '依指示在這一次請求後停止：沒有重送、沒有其他生成；交主管覆核（M-4 R4 由 Penny 接受，見上方 R4）。', '',
          f"## 0. {R1['title']}", '', f"**結論：** {R1['verdict']}", '', f"**主管覆核：** {R1['review']}", '', '### 0.1 Soul 證據', '']
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
    L += table(['阻礙', '說明', '誰決定', 'M-4 R2 狀態'], [[x['k'], x['v'], x['who'], x['state']] for x in R1['blockers']])
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


EQUIP = re.compile(r'reflector|softbox|soft box|key light|fill light|\bfill\b|ring light|strobe|flash|light stand|out of frame|umbrella|scrim|diffuser|studio light', re.I)
MARKERS = ['She wears', 'Setting:', 'Shot:', 'Body:', 'Face and gaze:', 'Camera:', 'Composition:', 'Emphasis:', 'Lighting:', 'Natural skin texture']


def render21(d, B):
    """第一批 5 位的生成準備：prompt 由已接受企劃原文套用光線句改寫算出，逐張核對後才排版。"""
    S = {s['id']: s for s in d['sets']}
    X = B['sets']
    assert B['round'] == 'M-4 R4' and d['round'] in ('M-4 R5', 'M-4 R6') and len(X) == 5 and len({x['pid'] for x in X}) == 5 and all(x['pid'] != 'iris-chen' for x in X), '第一批要 5 位不同角色、不含 Iris'
    assert B['counts']['generated'] == 0 and B['counts']['credits'] == 0 and B['status'] == 'prepared-pending-supervisor-review' and d['batch1']['status'] in ('generated-pending-owner-review', 'owner-rejected-r6') and [x['id'] for x in X] == d['batch1']['sets']
    rows = []
    for x in X:
        s = S[x['id']]
        assert s['status'] == 'accepted' and x['ratio'] == s['ratio'] and x['month'] == s['month'] and x['frame'] == s['print']['frame'], x['id']
        p = s['prompt']
        for c in x['changes']:
            assert p.count(c['before']) == 1, x['id']
            p = p.replace(c['before'], c['after'])
        assert p == x['prompt'], f"{x['id']}：prompt 與「已接受原文＋列出的改寫」不同"
        cam = all(x['prompt'].count(s['cam'][k]['en']) >= 1 for k in ('shot', 'bounds', 'body', 'face', 'gaze', 'angle', 'comp', 'purpose'))
        pos = [x['prompt'].find(m) for m in MARKERS]
        assert cam and all(v >= 0 for v in pos) and pos == sorted(pos), x['id']
        assert not EQUIP.search(x['prompt']), (x['id'], EQUIP.search(x['prompt']).group(0))
        assert x['request']['count'] == 1 and x['request']['model'] == 'soul_2' and x['request']['quality'] == '2k' and x['request']['aspect_ratio'] == s['ratio'] and x['quote']['credits_exact'] == B['quote']['per_request_exact']
        assert not re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}', json.dumps(x)), '不寫 Soul ID'
        rows.append([x['id'], '✓ 原文＋%d 處光線改寫' % len(x['changes']), '✓ 8 個攝影欄位英文句都在', '✓ 依序', '✓ 沒有', f"✓ {x['ratio']}／count 1"])
    assert round(sum(x['quote']['credits_exact'] for x in X), 2) == B['quote']['total_exact']
    Q = B['quote']
    R = B['request']
    L = [FIRST_LINE, '', '# CAL_21 — 第一批 5 位角色生成準備（M-4 R4 準備；M-4 R5 已依本文件生成）', '',
         '> **M-4 R5：主管覆核 PASS，已依本文件每位送出 1 次（共 5 次、無重試）；V-Rin 只改授權的景別用語，其餘 4 份逐字照送。結果、最終送出文字與差異、驗收與扣款見 `CAL_22_M4_BATCH1_RESULTS.md`。以下保留 M-4 R4 準備時的內容與數字，不回改。**', '',
         f"> 資料檔：`data/cal_m4_batch1_prep.json`（{B['version']}，{B['written_on']}）與 `data/cal_m3_shoot_plan.json`（{d['version']}）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準；5 份 prompt 由產生器核對「已接受企劃原文＋下列光線句改寫」後才排版。",
         f"> **本輪生成 {B['counts']['generated']}、修圖 {B['counts']['retouched']}、訓練 {B['counts']['trainings']}、扣 credits {B['counts']['credits']}；唯讀查詢 {B['counts']['readonly_queries']} 次（含不扣款報價預檢 {B['counts']['quote_prechecks']} 次）。**", '',
         '## 0. 依據與範圍', '', f"- {B['basis']['owner']}", f"- {B['basis']['not_authorized']}",
         f"- V-Iris：{d['m4_prep']['r4']['status']}（M-4 R4；{d['m4_prep']['r4']['supersedes']}）。目前進度：{progress(d)}", '',
         '## 1. 5 位總覽（依送出順序）', '']
    L += table(['#', '角色', '套別', '月份', '比例', '景別（企劃）', '推薦理由', '選這一款的理由'],
               [[x['order'], x['name'], x['id'], f"{x['month']} 月", x['ratio'], x['cam_line'], x['why_pick'], x['why_ratio']] for x in X])
    Sel = B['selection']
    L += ['', '## 2. 怎麼選的', '', f"**範圍：** {Sel['pool']}", '', f"**規則：** {Sel['rule']}", '', '**本批差異：**', '']
    L += table(['面向', '本批'], [['比例', Sel['mix']['ratio']], ['光線', Sel['mix']['light']], ['景別', Sel['mix']['framing']], ['視線', Sel['mix']['gaze']], ['外觀', Sel['mix']['look']]])
    L += ['', '**沒有選的人與原因：**', '']
    L += table(['角色', '原因'], [[e['who'], e['why']] for e in Sel['excluded']])
    L += ['', '## 3. 描述方法（沿用 V-Iris 首試的組織方式）', '', '順序：' + ' → '.join(B['method']['order']) + '。', '', B['method']['note'], '', f"**唯一的修改：** {B['method']['only_change']}", '',
          '## 4. 共同設定、報價與費用', '']
    L += table(['項目', '設定'], [['工具', R['tool']], ['模型', R['model']], ['Soul', '各人設既有 Soul（見逐張）；ID 只在 profile.json，不寫出'], ['quality', R['quality']], ['count', f"{R['count']}（每次請求 1 張；共 {R['requests']} 次請求）"],
                                  ['use_unlim', 'false（用 credits）'], ['參考圖', R['medias']], ['style_id', R['style_id']], ['送出方式', R['sequence']], ['重試', R['retry']],
                                  ['明確失敗且未扣款', R['failed_clean']], ['存放', R['storage']]])
    L += ['', f"**報價（{Q['date']}；{Q['how']}）：**", '']
    L += table(['#', '套別', '比例', '顯示值', '精確報價（credits_exact）'], [[x['order'], x['id'], x['ratio'], x['quote']['credits'], x['quote']['credits_exact']] for x in X])
    L += ['', f"**合計（精確報價）：{Q['total_exact']:.2f} credits**（{Q['requests']} 次 × {Q['per_request_exact']}）。", '', f"**建議整批預算：** {Q['budget']}", '', Q['not_guarantee'], '',
          f"**預檢前後的交易：** {Q['tx_check']}", '', f"**參考：** {Q['history']}", '', '**停止條件（任一成立就停，不補送）：**', ''] + [f'- {x}' for x in R['stop']]
    L += ['', R['after_stop'], '', '**交易核對：**', '', f"- {B['recon']['method']}", f"- {B['recon']['criteria']}", f"- {B['recon']['late']}", '',
          '## 5. 生成前核對', ''] + [f'- {x}' for x in B['checks']]
    L += ['', '**程式核對結果（產生器）：**', '']
    L += table(['套別', 'prompt 來源', '中英攝影欄位', '描述順序', '器材字', '比例／張數'], rows)
    for i, x in enumerate(X, 6):
        s = S[x['id']]
        z = x['zh']
        L += ['', f"## {i}. {x['name']}｜{x['id']}｜{x['month']} 月｜{x['ratio']}", '',
              f"**企劃來源：** {x['plan_source']}", '', f"**為什麼選她：** {x['why_pick']}", '', f"**為什麼是這一款：** {x['why_ratio']}", '',
              f"**canon 摘要：** {x['meas']}；髮：{z['髮妝'].split('；')[0]}（Soul V2 不繼承髮型與身材，prompt 逐字寫明）。", '', '### 中文拍攝摘要', '']
        L += table(['項目', '內容'], [[k, z[k]] for k in ('場景', '服裝', '髮妝', '姿態與雙手', '表情', '視線', '光線')] + [['景別', x['cam_line']], ['畫面上下界', x['bounds']]])
        so = x['soul']
        L += ['', '### Soul 與設定', '']
        L += table(['項目', '內容'], [['Soul', f"{so['name']}（指紋 sha256 前 8 碼 `{so['fingerprint']}`；ID 不寫出）"], ['紀錄位置', so['record']], ['專案狀態', f"{so['profile_status']}；訓練圖 {so['training_images']} 張"],
                                      ['既有驗證', so['verification']], ['帳號查詢', so['account_2026_10_21']], ['限制', so['limits']],
                                      ['設定', f"model {x['request']['model']}｜quality {x['request']['quality']}｜aspect_ratio {x['request']['aspect_ratio']}｜count {x['request']['count']}｜use_unlim false｜{x['request']['medias']}｜style_id {x['request']['style_id']}"],
                                      ['存放位置', x['request']['folder_id']], ['報價', f"顯示值 {x['quote']['credits']}／精確 {x['quote']['credits_exact']}（{x['quote']['at']}）"]])
        L += ['', '### 相對已定稿 prompt 的修改', '']
        for c in x['changes']:
            L += ['前：', '', '```text', c['before'], '```', '', '後：', '', '```text', c['after'], '```', '', f"理由：{c['why']}", '']
        L += ['### 完整英文 prompt（可直接送出）', '', '```text', x['prompt'], '```', '', '### 最重要的驗收重點', ''] + [f'- {f}' for f in x['accept_focus']]
        L += ['', '### 已知風險', ''] + [f'- {r}' for r in x['risks']]
        L += ['', '### 工作照片框', '', f"- {x['frame']}", f"- {x['native']}", f"- {x['ppi']}"] + [f'- {e}' for e in x['edges']]
    L += ['', f"## {len(X) + 6}. 生成後（主管另發整批生成指令之後）", ''] + [f'- {x}' for x in B['after_generation']] + ['']
    return '\n'.join(L)


def render22(d, B, U, A):
    """第一批 5 位的生成結果：送出 prompt 逐張核對（等於 CAL_21 原文；V-Rin 只套用授權的景別用語修正）、原圖 sha256、扣款合計。"""
    import hashlib
    X = {x['id']: x for x in B['sets']}
    Z = U['sets']
    sc = A['scope']
    assert U['round'] == 'M-4 R5' and d['round'] in ('M-4 R5', 'M-4 R6') and [z['id'] for z in Z] == sc['sets'] == d['batch1']['sets'] and len(Z) <= sc['requests_max']
    fix = U['prompt_fix']
    assert fix == A['prompt_fix'] and fix['set'] == 'V-rin-ayase'
    rows, money = [], []
    for z in Z:
        x = X[z['id']]
        want = x['prompt'].replace(fix['before'], fix['after']) if z['id'] == fix['set'] else x['prompt']
        assert x['prompt'].count(fix['before']) == (1 if z['id'] == fix['set'] else 0), z['id']
        assert z['prompt_final'] == want and hashlib.sha256(want.encode()).hexdigest() == z['prompt_sha256'], f"{z['id']}：送出 prompt 不等於 CAL_21 原文＋授權修正"
        assert not EQUIP.search(z['prompt_final']), z['id']
        q = z['request']
        assert (q['model'], q['quality'], q['count'], q['use_unlim'], q['aspect_ratio']) == (sc['model'], sc['quality'], sc['count'], sc['use_unlim'], x['ratio']) and z['requests'] == sc['per_set'], z['id']
        r = z['result']
        with open(os.path.join(ROOT, r['path']), 'rb') as f:
            assert hashlib.sha256(f.read()).hexdigest() == r['sha256'], r['path']
        assert r['px'] == ([1536, 2048] if x['ratio'] == '3:4' else [2048, 1152]) and z['status'] == 'completed', z['id']
        assert z['quote']['credits_exact'] <= sc['quote_max_each'] and [c['credits'] for c in z['charge']['rows']] == [-z['quote']['credits_exact']] and not z['charge']['refunds'], z['id']
        assert z['charge']['attribution'] == '依時窗及唯一任務推定'
        money.append(z['quote']['credits_exact'])
    C = U['charges']
    assert round(sum(money), 2) == C['charged_total'] == C['quote_total_exact'] <= sc['budget_credits'] and C['refunds_total'] == 0 and C['late_recheck']
    assert not re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}', json.dumps(U)), '不寫工作 ID 或 Soul ID'
    K = U['counts']
    L = [FIRST_LINE, '', '# CAL_22 — 第一批 5 位角色生成結果（M-4 R5）', '',
         f"> 資料檔：`data/cal_m4_batch1_run.json`（{U['version']}，{U['written_on']}）、`data/cal_m4_auth_r5.json`（主管指令逐字）、`data/cal_m4_batch1_prep.json`（CAL_21）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，產生器逐張核對送出 prompt、原圖 sha256 與扣款合計後才排版。工作 ID 與 Soul ID 只在私有執行紀錄 `review/calendar/m4_r5/execution_log.json` 與各人設 profile.json。",
         f"> **本輪請求 {K['requests']} 次（每位 1 次、無重試）、完成 {K['completed']}、失敗 {K['failed']}；生成 {K['generated']} 張；修圖 {K['retouched']}、放大 {K['upscaled']}、訓練 {K['trainings']}；實扣 {C['charged_total']:.2f} credits（核准額度 {C['budget']:.2f}），退款 {C['refunds_total']}。**",
         '> 以下驗收是執行者自測，不是主管覆核；照片是否接受由 Penny 在目前檢視頁決定。',
         f"> **{d['m4r6']['batch1_line']}**" if 'm4r6' in d else '', '',
         '## 0. 授權範圍', '']
    L += table(['項目', '內容'], [['指令', A['task']], ['基準', f"成果 `{A['base']['result']}`、送審 `{A['base']['review']}`"], ['名單與順序', '、'.join(sc['sets'])],
                                  ['請求上限', f"每位 {sc['per_set']} 次、共最多 {sc['requests_max']} 次、不補送"], ['費用', f"每張精確報價 ≤ {sc['quote_max_each']}、合計 ≤ {sc['quote_max_total']:.2f}、核准額度 {sc['budget_credits']:.2f} credits"],
                                  ['設定', f"{sc['model']}、quality {sc['quality']}、count {sc['count']}、use_unlim false、不掛參考圖、不傳 style_id"]])
    L += ['', '**規則：**', ''] + [f'- {x}' for x in A['rules']]
    L += ['', '## 1. 結果總覽', '']
    L += table(['#', '角色', '套別', '月份', '結果', '原圖（私有 repo）', '像素', '套框有效 ppi', '實扣', '和企劃最大的落差'],
               [[z['order'], z['name'], z['id'], f"{z['month']} 月", '完成（1 次請求）', f"`{z['result']['path']}`", '×'.join(map(str, z['result']['px'])),
                 f"{z['ppi']['effective']}（{'低於' if z['ppi']['below_target'] else '高於'} 300 工作目標）", f"{-z['charge']['rows'][0]['credits']:.2f}", z['acceptance']['gaps'][0]] for z in Z])
    L += ['', f"**送出前核對：** Soul：{U['precheck']['souls']}；存放：{U['precheck']['preferences']}；模型：{U['precheck']['model']}。", '',
          f"**中斷處理：** {U['interruption']}", '',
          '## 2. 最終送出文字與差異', '', f"**唯一修改（{fix['set']}，主管授權、不另送審）：**", '', '前：', '', '```text', fix['before'], '```', '', '後：', '', '```text', fix['after'], '```', '',
          f"中文標示同步為「{fix['zh']}」。理由：{fix['why']}。", '', '其餘 4 份逐字等於 `CAL_21_M4_BATCH1_PREP.md` 的送審版（產生器逐字比對；sha256 也和送出前寫下的提交意圖相同）。', '']
    L += table(['套別', '與 CAL_21 的關係', '送出 prompt sha256', '平台回應'],
               [[z['id'], z['prompt_vs_prep'], f"`{z['prompt_sha256'][:16]}…`", f"{z['echo']['model']}／{z['echo']['quality']}／{z['echo']['aspect_ratio']}／Soul {z['echo']['soul_name']}"] for z in Z])
    for z in Z:
        L += ['', f"### {z['order']}. {z['name']}｜{z['id']}（最終送出文字）", '', '```text', z['prompt_final'], '```']
    L += ['', '## 3. 逐筆扣款、退款與歸屬', '']
    L += table(['#', '套別', '精確報價', 'Soul V2 扣款列（UTC）', '金額', '退款', '時窗起點（送出前最新一列）', '時窗內其他', '歸屬'],
               [[z['order'], z['id'], z['quote']['credits_exact'], z['charge']['rows'][0]['at'], z['charge']['rows'][0]['credits'], '無' if not z['charge']['refunds'] else z['charge']['refunds'],
                 z['charge']['window_after'], f"soul_2 任務 {z['charge']['soul2_jobs_in_window']} 個（本次）；其他：{z['charge']['others_in_window']}", z['charge']['attribution']] for z in Z])
    LR = C['late_recheck']
    L += ['', f"**合計：** 精確報價 {C['quote_total_exact']:.2f}、實扣 {C['charged_total']:.2f}、退款 {C['refunds_total']}；核准額度 {C['budget']:.2f}。{C['per_request']}。", '',
          f"**歸屬層級：** {C['attribution']}", '', f"**說明：** {C['not_guarantee']}", '',
          f"**15 分鐘複查（{LR['at']}）：** {LR['window']}。{LR['result']}", '', f"**本批之後的扣款列：** {LR['after_batch']}", '',
          '## 4. 逐張驗收（執行者自測）', '']
    ZH = [('identity', '身分與髮色髮型'), ('body', '身材呈現'), ('outfit', '服裝'), ('hands_feet', '手腳結構'), ('expression_gaze', '表情與視線'), ('scene', '場景'), ('light', '光線'), ('composition', '構圖'), ('texture', '質感')]
    for z in Z:
        a = z['acceptance']
        L += [f"### {z['order']}. {z['name']}｜{z['id']}｜{z['month']} 月｜{z['ratio']}", '']
        L += table(['項目', '看圖紀錄'], [[zh, a[k]] for k, zh in ZH] + [['上下留白（佔原圖高）', f"上 {a['margins']['head']}；下 {a['margins']['feet']}"]])
        L += ['', '**主管指定重點：**', ''] + [f'- {f}' for f in a['focus']]
        L += ['', '**和企劃的落差：**', ''] + [f'- {g}' for g in a['gaps']]
        L += ['', f"**像素與套框：** {z['ppi']['how']}", '', f"**套框放法：** {z['frame']['placement']}（預覽 `{z['frame']['preview']}`）", '',
              f"**原圖：** `{z['result']['path']}`（{z['result']['bytes']:,} bytes，sha256 `{z['result']['sha256']}`；{z['result']['png_text_chunks']}；平台記錄 quality 欄 {z['result']['job_meta']['quality_field']}、style {z['result']['job_meta']['style']}、seed {z['result']['job_meta']['seed']}）", '']
    L += ['## 5. 像素與有效 ppi', '']
    L += table(['套別', '實際像素', '工作照片框', '有效 ppi', '300 ppi 工作目標'],
               [[z['id'], '×'.join(map(str, z['result']['px'])), '×'.join(map(str, z['ppi']['frame_mm'])) + ' mm', z['ppi']['effective'], '低於（照實列出，不重生、不放大，不代表不能印）' if z['ppi']['below_target'] else '達到'] for z in Z])
    L += ['', '## 6. 接下來', '', '- Penny 在目前檢視頁（shoot.html）一次看一位，選「接受」或「想修改」並可加備註，看完複製整批回饋給主管；未回覆不算接受。',
          '- 本批 5 次請求已用完；不論結果都不自行補生、修圖或放大。是否重拍、改哪裡，等 Penny 回饋與主管指示。', '']
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
    B = json.load(open(BATCH, encoding='utf-8'))
    docs = {OUT18: render18(d), OUT19: render19(d), OUT20: render20(d), OUT21: render21(d, B),
            OUT22: render22(d, B, json.load(open(RUN, encoding='utf-8')), json.load(open(AUTH, encoding='utf-8')))}
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
