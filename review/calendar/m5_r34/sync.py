"""M-5 R34：企劃狀態同步（橫式 H-L1 已接受；直式 Logo 圖示白／藍比較，待 Penny 選）。只改下列欄位，並把差異記在 m5r34.changes。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r34' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'r33_h_accepted_v_revision_pending' and pr['cover_person_track'] == 'stopped'
chg('status.production.cover', pr['cover'], 'r34_v_logo_icon_compare')
pr['cover'] = 'r34_v_logo_icon_compare'
D = pr['definitions']
v = ('封面狀態；M-5 R28–R30 人物封面 Owner 未接受；M-5 R31 非人物候選中 Owner 選 A 四季光影；M-5 R32 品牌版中 Owner 接受橫式 H-L1、直式選 V-D2 編排；'
     'M-5 R33 直式修正版（金色年份、白色 Logo）；M-5 R34 起 r34_v_logo_icon_compare＝橫式 H-L1 已接受（定案），直式 Logo 圖示白色（A）／官方藍（B）比較已放上網站，等 Penny 選；'
     '比較不等於接受直式封面；封面接受不等於交印核准')
chg('status.production.definitions.cover', D['cover'], v)
D['cover'] = v
P['m5r34'] = {
    'from_commit': '71a729677d6848a595627e63799fd42fb775d1ed',
    'owner': 'docs/calendar/data/cal_m5_owner_r34.json',
    'design': 'docs/calendar/data/cal_m5_r34_design.json',
    'covers': 'docs/calendar/data/cal_m5_cover_r34.json',
    'page': 'docs/calendar/data/cal_cover_r34_page.json',
    'source': 'docs/calendar/cover_r34/',
    'status_line': 'M-5 R34：Owner「那試做看看，我再進行比較」。直式以 R33 為基底，只把 Logo 左側圖示由白色填回官網原色 #2B33F2（英文字標與「兌心科技」維持白色、其餘不變），'
                   '與 R33 白色圖示版並排比較；藍色版另出直式完整預覽 PDF（32 面）。生成 0、付費 0；只是比較，不代表接受直式封面；橫式 H-L1 已接受不變。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
