"""M-5 R30：企劃狀態同步（還原 R28 誤改的其他人與背景，Coco 單人效果待 Penny 確認）。只改下列欄位，並把差異記在 m5r30.changes。
本機修正是免費、非生成的編修，記在 cover_local_fix_log，不併入生成或編輯次數。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r30' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'r29_single_fix_owner_check' and pr['cover_local_fix_log'] == {'M-5 R29': 1} and pr['cover_edit_log'] == {'M-5 R28': 1} and pr['generated_cumulative'] == 85
chg('status.production.cover', pr['cover'], 'r30_single_fix_owner_check')
pr['cover'] = 'r30_single_fix_owner_check'
old = dict(pr['cover_local_fix_log'])
pr['cover_local_fix_log']['M-5 R30'] = 1
chg('status.production.cover_local_fix_log', old, pr['cover_local_fix_log'])
D = pr['definitions']
v = ('封面狀態；M-5 R28 起 R27 四張 Owner 全退回、無已接受底圖；M-5 R29 起 Coco 單人本機膚色修正版放上網站；'
     'M-5 R30 起 r30_single_fix_owner_check＝已還原 R28 誤改的其他人與背景、等 Penny 確認 Coco「單人修正效果」；不等於接受整張封面或授權其他角色修正')
chg('status.production.definitions.cover', D['cover'], v)
D['cover'] = v
P['m5r30'] = {
    'from_commit': '0c2a3364f4a774a6a50302916b5d2037444ed4a1',
    'owner': 'docs/calendar/data/cal_m5_owner_r30.json',
    'trial': 'docs/calendar/data/cal_m5_r30_trial.json',
    'restore': 'docs/calendar/data/cal_m5_r30_restore.json',
    'page': 'docs/calendar/data/cal_cover_r30_page.json',
    'status_line': 'M-5 R30：主管看圖覆核 R29（膚色改善，可交 Owner 確認單人效果；腿保留現有明暗）。本輪只做本機免費還原（生成 0、付費 0、上傳 0）：'
                   '按人物歸屬重查 R28 回填範圍，除 Rainie 手臂、Mia 腳背外還有 Somi 左袖與牆、椅子、地板被改到，全部從 R27 原圖還原；'
                   '舊捲髮換掉後露出的地方只能用編輯結果並對齊色調；補平 R29 腳踝接縫。無損主檔相對 R27：Coco 實際編輯範圍外 0 改動。'
                   'R28「其餘 11 人保持」改記未通過。待 Penny 確認 Coco 單人效果；不批准其他角色或另一款封面。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
