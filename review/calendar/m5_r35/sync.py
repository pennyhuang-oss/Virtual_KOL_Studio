"""M-5 R35：企劃狀態同步（直式 V-D2-R34B 已接受；橫式 H-L1 年份輕光暈修正版待 Penny 確認）。只改下列欄位，並把差異記在 m5r35.changes。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r35' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'r34_v_logo_icon_compare' and pr['cover_person_track'] == 'stopped'
chg('status.production.cover', pr['cover'], 'r35_v_accepted_h_glow_pending')
pr['cover'] = 'r35_v_accepted_h_glow_pending'
D = pr['definitions']
v = ('封面狀態；M-5 R28–R30 人物封面 Owner 未接受；M-5 R31 非人物候選中 Owner 選 A 四季光影；M-5 R32 品牌版中 Owner 接受橫式 H-L1、直式選 V-D2 編排；'
     'M-5 R33 直式修正版（金色年份、白色 Logo）；M-5 R34 直式 Logo 圖示藍白比較；M-5 R35 起 r35_v_accepted_h_glow_pending＝直式 V-D2-R34B（藍色圖示）Owner 已接受、定案；'
     '橫式 H-L1 背景、品牌與排版已接受，年份輕光暈修正版 H-L1-R35G 已放上網站，等 Penny 確認；封面接受不等於交印核准')
chg('status.production.definitions.cover', D['cover'], v)
D['cover'] = v
P['m5r35'] = {
    'from_commit': '4a7ba635e10bbead7e123962ab70bb43dbf88a43',
    'owner': 'docs/calendar/data/cal_m5_owner_r35.json',
    'design': 'docs/calendar/data/cal_m5_r35_design.json',
    'covers': 'docs/calendar/data/cal_m5_cover_r35.json',
    'page': 'docs/calendar/data/cal_cover_r35_page.json',
    'source': 'docs/calendar/cover_r35/',
    'status_line': 'M-5 R35：Owner 選定直式 B｜V-D2-R34B（「現在這樣就很好了，不用再改了」），直式封面正式接受、定案。橫式 H-L1 只替 2027 加細緻輕微的淡藍柔光（H-L1-R35G），'
                   '其餘與已接受版相同，修正版待 Penny 確認。兩份完整預覽 PDF（橫式 28 面用修正版、直式 32 面用 V-D2-R34B）。生成 0、付費 0；兩款封面接受不等於交印核准。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
