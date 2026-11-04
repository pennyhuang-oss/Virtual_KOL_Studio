"""M-5 R37：企劃狀態同步（雙款封面定案：橫式 H-L1-R36L、直式 V-D2-R34B；定案預覽與印前檢查，交印未核准）。只改下列欄位，並把差異記在 m5r37.changes。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r37' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'r36_v_accepted_h_lit_pending' and pr['cover_person_track'] == 'stopped'
chg('status.production.cover', pr['cover'], 'r37_both_accepted_final_preview')
pr['cover'] = 'r37_both_accepted_final_preview'
D = pr['definitions']
v = ('封面狀態；M-5 R28–R30 人物封面 Owner 未接受；M-5 R31～R36 非人物封面迭代；M-5 R37 起 r37_both_accepted_final_preview＝雙款封面 Owner 已接受（定案）：'
     '橫式 H-L1-R36L（年份光感加強版）、直式 V-D2-R34B（金色年份、藍色圖示）；定案預覽 PDF 與印前檢查完成（CAL_29）；'
     '廠商規格、打樣與交印核准仍待確認；封面接受不等於交印核准')
chg('status.production.definitions.cover', D['cover'], v)
D['cover'] = v
P['m5r37'] = {
    'from_commit': '6e8940c80ea36ea0609a8dd30c6c90100b7a1efd',
    'owner': 'docs/calendar/data/cal_m5_owner_r37.json',
    'final': 'docs/calendar/data/cal_m5_final_r37.json',
    'preflight': 'docs/calendar/CAL_29_M5_R37_FINAL_PREFLIGHT.generated.md',
    'page': 'docs/calendar/data/cal_cover_r37_page.json',
    'status_line': 'M-5 R37：Owner 接受橫式加強版 H-L1-R36L，直式 V-D2-R34B 已接受——雙款封面定案。以已驗證預覽 PDF 逐頁原樣產生「定案預覽」（橫式 28 面、直式 32 面），'
                   '完成可做的印前檢查（尺寸、出血、頁序、內頁一致、字型嵌入、照片解析度與色彩）；線圈／打孔、正背面、解析度門檻、CMYK／ICC、交件規格與打樣待廠商確認。'
                   '不是交印檔，交印待 Penny 另行核准。生成 0、付費 0。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
