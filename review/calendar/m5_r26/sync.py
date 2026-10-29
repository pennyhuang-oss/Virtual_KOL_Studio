"""M-5 R26：企劃狀態同步（印前檢查進行中、排版預覽待 Penny 看、排版接受另記）。只改下列欄位，並把差異記在 m5r26.changes。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
P_REL = 'docs/calendar/data/cal_m3_shoot_plan.json'
p = os.path.join(ROOT, P_REL)
P = json.load(open(p, encoding='utf-8'))
assert 'm5r26' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['prepress_check'] == 'not_started'
chg('status.production.prepress_check', pr['prepress_check'], 'in_progress')
pr['prepress_check'] = 'in_progress'
for k, v in (('layout_preview', 'ready_for_owner_review'), ('layout_acceptance', 'not_given'), ('layout_file', 'docs/calendar/data/cal_m5_layout_r26.json')):
    assert k not in pr
    chg(f'status.production.{k}', '（無）', v)
    pr[k] = v
D = pr['definitions']
old = D['prepress_check']
D['prepress_check'] = '印前檢查（套框、有效 ppi、色彩、版型、日期等）狀態；M-4 R25 只列尺寸與缺口；M-5 R26 起進行中（已做排版預覽、裁切、ppi、日期與 PDF 核對；廠商項目、打樣未確認）'
chg('status.production.definitions.prepress_check', old, D['prepress_check'])
D['layout_preview'] = '排版預覽狀態；M-5 R26 兩款完整頁面預覽與 PDF 完成，待 Penny 看（工作版、非交印核准）'
D['layout_acceptance'] = '排版接受狀態，與照片接受（owner_selection）分開記錄；not_given＝Penny 尚未接受排版'
chg('status.production.definitions.layout_preview／layout_acceptance', '（無）', '新增兩個定義')
P['m5r26'] = {
    'from_commit': '0ac62ca410f61852383ecb78cf5b00691ac24897',
    'owner': 'docs/calendar/data/cal_m5_owner_r26.json',
    'layout': 'docs/calendar/data/cal_m5_layout_r26.json',
    'page': 'docs/calendar/data/cal_layout_r26_page.json',
    'status_line': 'M-5 R26：兩款排版預覽完成（橫式 28 面、直式 32 面，實際 mm 尺寸 PDF，標為預覽、非交印核准），待 Penny 看；橫式推薦改用完整 16:9（192×108 mm）照片框、與 R6 的 192×104 套框並列比較，未定案。照片沿用 24 張定案，不需重新接受；排版接受另記。本輪生成 0、付費 0。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
