"""M-5 R33：企劃狀態同步（Owner 接受橫式 H-L1；直式選 V-D2 編排，本輪修正版待確認）。只改下列欄位，並把差異記在 m5r33.changes。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r33' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'r32_seasons_brand_candidates' and pr['cover_person_track'] == 'stopped'
chg('status.production.cover', pr['cover'], 'r33_h_accepted_v_revision_pending')
pr['cover'] = 'r33_h_accepted_v_revision_pending'
D = pr['definitions']
v = ('封面狀態；M-5 R28–R30 人物封面 Owner 未接受；M-5 R31 非人物候選中 Owner 選 A 四季光影；M-5 R32 品牌版中 Owner 接受橫式 H-L1、直式選 V-D2 編排；'
     'M-5 R33 起 r33_h_accepted_v_revision_pending＝橫式 H-L1 已接受（定案），直式 V-D2 修正版（只把年份改成金色）已放上網站，等 Penny 確認；'
     '封面接受不等於交印核准')
chg('status.production.definitions.cover', D['cover'], v)
D['cover'] = v
P['m5r33'] = {
    'from_commit': 'bfbe215d2e84e7ae45e75c59b8f4faea7ddc7975',
    'owner': 'docs/calendar/data/cal_m5_owner_r33.json',
    'design': 'docs/calendar/data/cal_m5_r33_design.json',
    'covers': 'docs/calendar/data/cal_m5_cover_r33.json',
    'page': 'docs/calendar/data/cal_cover_r33_page.json',
    'source': 'docs/calendar/cover_r33/',
    'status_line': 'M-5 R33：Owner 接受橫式 H-L1（定案）；直式選 V-D2 編排並要求修改。本輪直式修正版：2027 改為柔和香檳金到暖金黃的漸層，加輕微光暈。'
                   'Penny 本輪提供藍色圓底白字 Logo，試放後 Owner 認為不協調，決定維持 R32 原本的白色 Logo 與白色中文，只改 2027。'
                   '兩份完整預覽 PDF（橫式 28 面用 H-L1、直式 32 面用修正版）。生成 0、付費 0；直式待 Penny 確認；24 張照片與內頁排版不改。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
