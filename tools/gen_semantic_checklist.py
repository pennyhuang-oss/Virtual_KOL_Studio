#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""K-01：產生逐列的「結構欄位 ↔ 自然語言」語意覆核清單。

為什麼需要：validator 的 scene 衝突檢查是 regex heuristic lint，補不完
（漏 T恤/上衣/鞋/靴/長髮/dress/skirt…），而且已經在真資料漏抓過矛盾
（nico_a01 scene 寫「坐著」、body_pose 卻是 standing，是 ChatGPT 人工看出來的）。
所以機器 lint 只能當第一關，第二關必須是逐列的人／LLM 語意覆核，並留下可追溯紀錄。

產出 pilot/semantic_review.md（給人看）與 pilot/semantic_review.json（給 validator 檢查新鮮度）。
資料一改，hash 就對不上，覆核紀錄自動失效——避免「改完資料卻沿用舊的核可」。
"""
import json, hashlib, sys

def data_hash(shots):
    return hashlib.sha256(json.dumps(shots,ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:16]

def shot_hash(s):
    """C-33 後改為逐列 hash。整份 blob 一個 hash 的話，改一列就作廢全部 20 列的覆核，
    覆核與修正會互相打架、永遠收斂不了。改一列只失效那一列。"""
    body={k:v for k,v in s.items() if not k.startswith('_')}
    return hashlib.sha256(json.dumps(body,ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:12]

def build(pilot):
    S=pilot['phase_c_shots']; O=pilot['outfits']; H=pilot['hair']
    L=[];w=L.append
    h=data_hash(S)
    w("# 語意覆核清單 — Nico Pilot Phase C")
    w("")
    w(f"> 資料 hash：`{h}`　|　{len(S)} 列　|　**逐列 hash**：改一列只失效那一列，其餘核可保留")
    w("> **機器 lint 已通過不代表語意正確。** 逐列確認「scene 這句話」與右邊每個結構欄位是否真的相容。")
    w("> 覆核完成後把 `pilot/semantic_review.json` 的 `reviewed_shot_ids` 填滿並記錄 `data_hash`。")
    w("> 資料一改 hash 就變，舊的覆核紀錄自動失效。")
    w("")
    for s in S:
        w(f"### {s['shot_id']}　`{shot_hash(s)}`")
        w("")
        w(f"**scene**：{s['scene']}")
        w("")
        w("| 欄位 | 值 | 與 scene 相容？ |")
        w("|------|----|----------------|")
        w(f"| body_pose | `{s['body_pose']}` | ☐ |")
        w(f"| framing | `{s['framing']}` | ☐ |")
        w(f"| head_yaw / pitch | `{s['head_yaw']}` / `{s['head_pitch']}` | ☐ |")
        w(f"| eye_gaze | `{s['eye_gaze']}` | ☐ |")
        w(f"| view | `{s['view']}` | ☐ |")
        w(f"| expression | `{s['expression']}` | ☐ |")
        w(f"| outfit | `{s['outfit_id']}` — {O[s['outfit_id']]['label']}（{O[s['outfit_id']]['neckline']}）| ☐ |")
        w(f"| hair | `{s['hair_id']}` — {H[s['hair_id']]} | ☐ |")
        w(f"| location | `{s['location']}` | ☐ |")
        w(f"| light | `{s['light']['family']}` / bounce={s['light']['bounce_type']} | ☐ |")
        w(f"| face_visibility | `{s['face_visibility']}` | ☐ |")
        for q in s['props']:
            w(f"| prop `{q['id']}` | {q['name']}（{q['relation']}・zone={q['zone']}・"
              f"可見={q['expected_visible']}）| ☐ |")
        for side in ('left','right'):
            sl=s['hands'][side]
            w(f"| hands.{side} | `{sl['state']}`"
              f"{'→`'+sl['object_ref']+'`' if sl.get('object_ref') else ''}（{sl['note']}）| ☐ |")
        w("")
        w("**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜"
          "室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜"
          "**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜"
          "**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）")
        w("")
    return "\n".join(L), h

if __name__=='__main__':
    pilot=json.load(open('pilot/nico_pilot.json',encoding='utf-8'))
    md,h=build(pilot)
    open('pilot/semantic_review.md','w',encoding='utf-8').write(md)
    import os
    prev={}
    if os.path.exists('pilot/semantic_review.json'):
        prev=json.load(open('pilot/semantic_review.json',encoding='utf-8'))
    S=pilot['phase_c_shots']
    cur={s['shot_id']:shot_hash(s) for s in S}
    old=prev.get('reviewed',{})   # {shot_id: {hash, by, at}}
    kept={k:v for k,v in old.items() if k in cur and v.get('hash')==cur[k]}
    dropped=sorted(set(old)-set(kept))
    rec={"data_hash":h,"total_shots":len(S),"shot_hashes":cur,"reviewed":kept,
         "reviewed_shot_ids":sorted(kept),
         "_note":"逐列 hash：某一列改過，只有那一列的核可失效，其餘保留（C-33）。"}
    json.dump(rec,open('pilot/semantic_review.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(f"已產生 pilot/semantic_review.md（{len(pilot['phase_c_shots'])} 列，hash {h}）")
    print(f"覆核進度：{len(rec['reviewed'])}/{rec['total_shots']}")
    if dropped: print(f"  因資料變動而失效的核可：{dropped}")
