"""M-5 R27：企劃狀態同步（Owner 接受 R26 排版；12 人團體封面 4 張候選待 Penny 選擇）。只改下列欄位，並把差異記在 m5r27.changes。
封面生成張數與 credits 另記（cover_generated_log），不併入月面照片累計（generated_cumulative 85）或構圖底稿（drafts）。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
P_REL = 'docs/calendar/data/cal_m3_shoot_plan.json'
p = os.path.join(ROOT, P_REL)
P = json.load(open(p, encoding='utf-8'))
assert 'm5r27' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['layout_preview'] == 'ready_for_owner_review' and pr['layout_acceptance'] == 'not_given'
assert pr['generated_cumulative'] == 85 and pr['prepress_check'] == 'in_progress' and pr['print_approval'] == 'not_given'
for k, v in (('layout_preview', 'owner_reviewed'), ('layout_acceptance', 'accepted')):
    chg(f'status.production.{k}', pr[k], v)
    pr[k] = v
for k, v in (('layout_acceptance_record', 'docs/calendar/data/cal_m5_owner_r27.json'), ('cover', 'candidates_ready_for_owner_choice'),
             ('cover_file', 'docs/calendar/data/cal_m5_cover_r27.json'), ('cover_generated_log', {'M-5 R27': 4}), ('cover_credits_log', {'M-5 R27': 16})):
    assert k not in pr
    chg(f'status.production.{k}', '（無）', v)
    pr[k] = v
D = pr['definitions']
for k, v in (
        ('layout_preview', '排版預覽狀態；M-5 R26 兩款完整頁面預覽與 PDF 完成；M-5 R27 起 owner_reviewed＝Penny 已看過並回覆（工作版、非交印核准）'),
        ('layout_acceptance', '排版接受狀態，與照片接受（owner_selection）分開記錄；M-5 R27 起 accepted＝Penny 接受 R26 頁面（5a82bf9）的推薦排法：橫式照片框完整 16:9（192×108 mm）、橫式與直式推薦排法。排版接受不等於交印核准'),
        ('layout_acceptance_record', 'Penny 接受排版的原話紀錄'),
        ('cover', '封面狀態；M-5 R27 起 candidates_ready_for_owner_choice＝12 人團體封面候選（橫式 A／B、直式 A／B）已排版放上網站，等 Penny 選；Claude 自查身分未全數確認，沒有一張可定案。不等於 Owner 接受'),
        ('cover_file', '封面候選排版資料（版面、標題位置與檢查、檔案 hash）'),
        ('cover_generated_log', '封面生成張數（每輪）；與月面照片 generated_cumulative、構圖底稿 drafts 分開計算，不相加'),
        ('cover_credits_log', '封面生成實扣 credits（每輪；上傳身分參考圖 0）')):
    old = D.get(k, '（無）')
    D[k] = v
    chg(f'status.production.definitions.{k}', old, v)
P['m5r27'] = {
    'from_commit': '8863eaa50e18a9408274d8057cc2bec3a01b3775',
    'owner': 'docs/calendar/data/cal_m5_owner_r27.json',
    'identity': 'docs/calendar/data/cal_m5_r27_identity.json',
    'prompts': 'docs/calendar/data/cal_m5_r27_prompts.json',
    'trial': 'docs/calendar/data/cal_m5_r27_trial.json',
    'cover': 'docs/calendar/data/cal_m5_cover_r27.json',
    'page': 'docs/calendar/data/cal_cover_r27_page.json',
    'status_line': 'M-5 R27：Penny 接受 R26 排版（橫式完整 16:9 192×108 mm、兩款推薦排法；排版接受不等於交印核准）。12 人團體封面生成 4 張候選（橫式 A／B、直式 A／B，各 1 次請求、實扣 16 credits、上傳 0、未重試），本機排上「2027」後放到排版頁供 Penny 選。Claude 自查：4 張都是 12 人同場，但沒有一張能確認 12 人身分（H-A、V-A、V-B 各有 1–2 位明顯換成別人；H-B 3 位看不清），不可定案；未補生、未修臉。月面照片 24 張不動。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
