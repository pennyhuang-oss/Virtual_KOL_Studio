"""M-5 R29：企劃狀態同步（Coco 單人本機膚色修正版，待 Penny 確認單人效果）。只改下列欄位，並把差異記在 m5r29.changes。
本機修正是免費、非生成的編修，另記 cover_local_fix_log，不併入生成或編輯次數。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r29' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'r27_all_rejected_single_identity_test' and pr['cover_edit_log'] == {'M-5 R28': 1} and pr['generated_cumulative'] == 85
chg('status.production.cover', pr['cover'], 'r29_single_fix_owner_check')
pr['cover'] = 'r29_single_fix_owner_check'
assert 'cover_local_fix_log' not in pr
pr['cover_local_fix_log'] = {'M-5 R29': 1}
chg('status.production.cover_local_fix_log', '（無）', pr['cover_local_fix_log'])
D = pr['definitions']
for k, v in (
        ('cover', '封面狀態；M-5 R28 起 R27 四張 Owner 全退回、無已接受底圖；M-5 R29 起 r29_single_fix_owner_check＝Coco 單人本機膚色修正版已放上網站，等 Penny 確認「單人修正效果」；不等於接受整張封面或授權其他角色修正'),
        ('cover_local_fix_log', '封面本機修正次數（每輪；免費、不生成、不上傳），與生成張數、局部身分編輯次數分開計算')):
    old = D.get(k, '（無）')
    D[k] = v
    chg(f'status.production.definitions.{k}', old, v)
P['m5r29'] = {
    'from_commit': 'f98c88bb526227a7a91748f22a92cf198ac759b5',
    'owner': 'docs/calendar/data/cal_m5_owner_r29.json',
    'trial': 'docs/calendar/data/cal_m5_r29_trial.json',
    'fix': 'docs/calendar/data/cal_m5_r29_skin.json',
    'page': 'docs/calendar/data/cal_cover_r29_page.json',
    'status_line': 'M-5 R29：主管看圖覆核 R28（Coco 臉部身分明顯恢復、方向部分通過；胸口／右手／腿比臉深）。本輪只做本機免費修正（生成 0、付費 0、上傳 0）：從 R28 另存膚色修正版，只調 Coco 的脖子＋胸口、右手、雙腿（含 R28 漏蓋的左小腿下段）的色相、飽和度與小幅明暗；臉與其他人不動。胸口與手已和臉連貫，腿仍略深。更正 R28 紀錄：回填範圍內誤含 Rainie 前臂與 Mia 腳背各一小塊；生成失敗的臉部尺寸等只是可能因素；重做率 30% 只是情境假設。待 Penny 確認單人效果；不批准其他角色或另一款封面。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
