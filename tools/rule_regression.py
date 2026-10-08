# -*- coding: utf-8 -*-
"""規則清單 regression test。

存在的理由（2026-09-09）：把 v1 的產生器重寫成 v2 時，我靜默丟掉了三個 v1 有的防護
（REFLECTIVE 反射面偵測、MIRROR_SECONDARY 次要鏡面句、IN_FRAME_CAMERA 正則），
而且真的有一格中（jia-seo D5）。靠人工記憶不可靠，所以把「哪些不變量必須存在」寫成測試。

用法：python3 tools/rule_regression.py plan/daily_v2/build_prompts.py

依 GPT daily_v2 R2 複核建議分三層：
  A 硬擋（deterministic invariant）—— 資料自相矛盾就一定錯，缺一條就 FAIL
  B lint（heuristic）—— 缺了只警告，因為它們是風格偏好不是真理
  C 模型行為假設 —— 不在此測，因為 audit 通過不代表模型會照做
"""
import sys, re

LAYER_A = {  # 硬擋：這些不變量在任何版本的產生器裡都必須存在
 "封閉集合句":            r'Everything in this picture is accounted for',
 "鏡面排除句":            r'no second phone',
 "次要反射面偵測":         r'REFLECTIVE',
 "次要反射面句":           r'MIRROR_SECONDARY',
 "非鏡面格禁相機實體":      r'非鏡面格.*相機實體',
 "四肢預算":              r'LIMB_ONE|limb',
 "continuity 服裝一致":    r'continuity_from.*服裝字串不同|continuity_from',
 "continuity 部件一致":    r'延續句提到',
 "C-1 髮色":             r'hair_colour',
 "光線白名單":             r'未知光線代碼',
 "框架白名單":             r'未知框架',
 "背景路人措辭完整性":      r'no face is visible at any angle',
 "美貌段三件事":           r'natural makeup|GLOW',
 "服裝須有露出":           r'SKIN',
 "服裝須有腰線斷點":        r'WAIST',
 # 2026-09-09：這條規則在一次改寫中整條消失，而本清單當時漏列它，
 # 所以 regression 測試回報「齊全」。凡是加過的硬擋規則都必須列進來。
 "§3-D② 尾巴不得出現":      r'已移除的尾巴字樣',
 "鏡面格不得有背景路人":     r'鏡面格不得有背景路人',
 "location/scene_details":  r'scene_text',
}
LAYER_B = {  # lint：heuristic，缺了只警告
 "反美貌措辭黑名單":        r'反美貌措辭',
 "不時髦服裝黑名單":        r'UNCHIC',
 "死臉措辭黑名單":          r'DEAD_EXPR',
 "懸空姿勢黑名單":          r'HOVER_POSE',
 "裸否定句黑名單":          r'裸否定句',
 "光線↔場景一致性":        r'SCENE_LIGHT',
 "夜晚一致性":             r'NIGHT_LIGHT',
 "全身須動態姿勢":          r'DYNAMIC_POSE',
 "表情須交代眼睛":          r'EYES_DOING',
}

def main(path):
    s=open(path).read()
    miss_a=[k for k,pat in LAYER_A.items() if not re.search(pat,s)]
    miss_b=[k for k,pat in LAYER_B.items() if not re.search(pat,s)]
    print(f"檢查 {path}")
    print(f"  A 層硬擋不變量 {len(LAYER_A)-len(miss_a)}/{len(LAYER_A)}")
    for k in miss_a: print(f"     ✗ 缺少：{k}")
    print(f"  B 層 lint      {len(LAYER_B)-len(miss_b)}/{len(LAYER_B)}")
    for k in miss_b: print(f"     ⚠ 缺少：{k}（只是警告）")
    if miss_a:
        print(f"\n[FAIL] A 層有 {len(miss_a)} 個不變量不見了。"
              f"重寫產生器時最容易發生，不要靠記憶，把它加回來。")
        sys.exit(1)
    print("\n[OK] A 層不變量齊全。")

if __name__=="__main__":
    main(sys.argv[1] if len(sys.argv)>1 else 'plan/daily_v2/build_prompts.py')
