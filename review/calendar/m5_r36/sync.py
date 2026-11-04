"""M-5 R36：企劃狀態同步（直式 V-D2-R34B 已接受；橫式 H-L1 年份光感加強版待 Penny 確認）。只改下列欄位，並把差異記在 m5r36.changes。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r36' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'r35_v_accepted_h_glow_pending' and pr['cover_person_track'] == 'stopped'
chg('status.production.cover', pr['cover'], 'r36_v_accepted_h_lit_pending')
pr['cover'] = 'r36_v_accepted_h_lit_pending'
D = pr['definitions']
v = ('封面狀態；M-5 R28–R30 人物封面 Owner 未接受；M-5 R31 非人物候選中 Owner 選 A 四季光影；M-5 R32 品牌版中 Owner 接受橫式 H-L1、直式選 V-D2 編排；'
     'M-5 R33 直式修正版；M-5 R34 直式 Logo 藍白比較；M-5 R35 直式 V-D2-R34B 定案、橫式年份輕光暈；M-5 R36 起 r36_v_accepted_h_lit_pending＝直式 V-D2-R34B 已接受（定案）；'
     '橫式 H-L1 年份光感加強版 H-L1-R36L（字內受光漸層＋淡藍外光）已放上網站與 R35 比較，等 Penny 確認；封面接受不等於交印核准')
chg('status.production.definitions.cover', D['cover'], v)
D['cover'] = v
P['m5r36'] = {
    'from_commit': '5c87d5d3fb3e5ee218ee7448236987e9d28a8161',
    'owner': 'docs/calendar/data/cal_m5_owner_r36.json',
    'design': 'docs/calendar/data/cal_m5_r36_design.json',
    'covers': 'docs/calendar/data/cal_m5_cover_r36.json',
    'page': 'docs/calendar/data/cal_cover_r36_page.json',
    'source': 'docs/calendar/cover_r36/',
    'status_line': 'M-5 R36：Owner 要求橫式年份「像直式那種有光線的字」。加強版 H-L1-R36L：字形內部上緣亮藍、往下漸深到原本深藍的受光漸層，加上上強下弱的淡藍外光；'
                   '其餘與已接受 H-L1 相同；與 R35 並排比較，待 Penny 確認。橫式 28 面完整預覽 PDF。直式 V-D2-R34B 已定案不動。生成 0、付費 0；封面接受不等於交印核准。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
