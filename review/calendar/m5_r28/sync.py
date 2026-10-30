"""M-5 R28：企劃狀態同步（R27 四張封面 Owner 全退回；H-A 裡 Coco 單人身分測試 1 次）。只改下列欄位，並把差異記在 m5r28.changes。
封面編輯次數與 credits 另記（cover_edit_log），不併入月面照片累計或 R27 封面生成張數。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r28' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'candidates_ready_for_owner_choice' and pr['layout_acceptance'] == 'accepted' and pr['generated_cumulative'] == 85
chg('status.production.cover', pr['cover'], 'r27_all_rejected_single_identity_test')
pr['cover'] = 'r27_all_rejected_single_identity_test'
pr['cover_credits_log']['M-5 R28'] = 2
chg('status.production.cover_credits_log', {'M-5 R27': 16}, pr['cover_credits_log'])
assert 'cover_edit_log' not in pr
pr['cover_edit_log'] = {'M-5 R28': 1}
chg('status.production.cover_edit_log', '（無）', pr['cover_edit_log'])
D = pr['definitions']
for k, v in (
        ('cover', '封面狀態；M-5 R27 候選 4 張；M-5 R28 起 r27_all_rejected_single_identity_test＝Penny 退回 R27 全部 4 張（無已選封面、無已接受方向），只做了 H-A 裡 Coco 的單人身分測試（不是完成的封面）'),
        ('cover_credits_log', '封面實扣 credits（每輪；上傳 0）：R27 生成 16、R28 單人身分編輯 2'),
        ('cover_edit_log', '封面局部身分編輯次數（每輪）；與封面生成張數 cover_generated_log、月面照片 generated_cumulative 分開計算，不相加')):
    old = D.get(k, '（無）')
    D[k] = v
    chg(f'status.production.definitions.{k}', old, v)
P['m5r28'] = {
    'from_commit': '9aa94f94f50cf5367987deb39b138648fbc63301',
    'owner': 'docs/calendar/data/cal_m5_owner_r28.json',
    'input_audit': 'docs/calendar/data/cal_m5_r28_input_audit.json',
    'trial': 'docs/calendar/data/cal_m5_r28_trial.json',
    'test': 'docs/calendar/data/cal_m5_r28_coco_test.json',
    'page': 'docs/calendar/data/cal_cover_r28_page.json',
    'status_line': 'M-5 R28：Penny 退回 R27 全部 4 張封面（全部人臉不符），無已選封面或方向；24 張月面照片與兩款內頁排版維持已接受。R27 輸入查核：清單與平台接收都正確（12 張參考、順序、檔案內容一致），失敗在生成結果。H-A 裡 Coco 單人身分測試 1 次（實扣 2 credits、上傳 0）：臉部身分成功、其他 11 人與背景零改動，但臉比胸口／手／小腿白，膚色一致性只算部分通過 → 依規則整體記失敗；未修其他人，12 人流程只估算、待主管與 Penny 決定。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
