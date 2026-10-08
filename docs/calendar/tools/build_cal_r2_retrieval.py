#!/usr/bin/env python3
"""TASK-CAL-001 / R2 — Higgsfield 既有生成紀錄的取回清單（程式產生 CAL_07b）。

只讀 data/cal_r2_hf_retrieved.json（取回時寫下的紀錄）與 data/cal_r2_judgments.json（哪張被選作候選）。
不連網、不需要原圖。
用法：python3 docs/calendar/tools/build_cal_r2_retrieval.py
"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CAL = os.path.join(ROOT, 'docs', 'calendar')
OUT = os.path.join(CAL, 'CAL_07b_HF_RETRIEVAL.generated.md')


def main():
    R = json.load(open(os.path.join(CAL, 'data', 'cal_r2_hf_retrieved.json')))
    J = json.load(open(os.path.join(CAL, 'data', 'cal_r2_judgments.json')))['candidates']
    P = json.load(open(os.path.join(CAL, 'data', 'cal_r2_face_pairs.json')))['people']
    used = {}
    for c in J:
        if c['src'].startswith('hf:'):
            used.setdefault(c['src'][3:], []).append(c['cid'])
    for p in P:
        for im in p['images']:
            if im['src'].startswith('hf:'):
                used.setdefault(im['src'][3:], []).append('臉部比較' if p['group'] != 'observation' else '稽核觀察頁（不作依據）')
    items = R['items']
    L = ['# CAL_07b — Higgsfield 既有生成紀錄取回清單（程式產生，請勿手改）', '',
         '> 由 `docs/calendar/tools/build_cal_r2_retrieval.py` 從 `data/cal_r2_hf_retrieved.json` 產生。',
         f"> 取回日期：{R['retrieved_on']}。方式：{R['how']}", '',
         f"> 留用 64 張：**{R['kept_64_status']}**", '',
         f"> 本機快取核對（{R['cache_check']['checked_on']}）：{R['cache_check']['ok']}/{R['cache_check']['items']} 張存在、可解碼、尺寸與 sha256 相符；"
         f"無法定位的 hf: 參照 {len(R['cache_check']['unresolved_hf_refs'])} 個。未重新下載。", '']
    daily = sorted([i for i in items if i['kind'] == 'daily_v2'], key=lambda i: i['daily140_file'])
    L += [f'## 1. daily_v2（{len(daily)} 張）', '', R['kinds']['daily_v2'], '',
          '| daily140 編號（index.json） | 人設 | slot／take | 構圖規格 | job_id | 生成時間 (UTC) | 原始尺寸 | 取回狀態 | sha256 | 本輪用途 |',
          '|---|---|---|---|---|---|---|---|---|---|']
    for i in daily:
        L.append(f"| `{i['daily140_file']}` | {i['pid']} | {i['slot']}／{i['take']} | {i['view']} | `{i['job_id']}` | "
                 f"{i['created_utc'][:16].replace('T', ' ')} | {i['px'][0]}×{i['px'][1]} | 已取回 | `{i['sha256']}` | "
                 f"{'、'.join(used.get(i['job_id'], [])) or '—（未選）'} |")
    other = sorted([i for i in items if i['kind'] != 'daily_v2'], key=lambda i: (i['kind'], i['created_utc']))
    L += ['', f'## 2. 其他工作線當天的 headshot（{len(other)} 張；只留稽核紀錄，不作本案任何依據）', '',
          f"- casting_headshot：{R['kinds']['casting_headshot']}", f"- identity_check：{R['kinds']['identity_check']}", '',
          '| 類別 | 人設 | 視角 | job_id | 生成時間 (UTC) | 使用的 Soul 名稱（紀錄原文） | 原始尺寸 | 取回狀態 | sha256 | 本輪用途 |',
          '|---|---|---|---|---|---|---|---|---|---|']
    for i in other:
        L.append(f"| {i['kind']} | {i['pid']} | {i['view']} | `{i['job_id']}` | {i['created_utc'][:16].replace('T', ' ')} | "
                 f"{i.get('soul_ref_name') or '—'} | {i['px'][0]}×{i['px'][1]} | 已取回 | `{i['sha256']}` | {'、'.join(used.get(i['job_id'], [])) or '—'} |")
    L.append('')
    open(OUT, 'w').write('\n'.join(L))
    print('ok', len(daily), len(other))


if __name__ == '__main__':
    main()
