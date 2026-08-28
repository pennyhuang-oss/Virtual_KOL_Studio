#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生「自帶內容」的覆核請求，讓 ChatGPT 不需要連 GitHub。

背景：讓 ChatGPT 透過 GitHub 連接器讀 repo，一次就把使用者 5 小時的方案用量燒光——
它只做檢核、不做規劃與執行，用量卻比 Claude 還快，不合理。原因是連接器會爬整個
專案背景（本 repo 光 .md 就約 500KB），而它真正需要的只有「這次改了什麼」。

改法：每次改動後由本程式產生一段**自帶全部內容**的訊息，使用者直接貼給 ChatGPT。
ChatGPT 不 fetch 任何東西，只讀訊息本身。

用法：
    python3 tools/gen_review_request.py                 # 從 review/CHECKPOINT 到 HEAD
    python3 tools/gen_review_request.py <base> [<head>] # 指定範圍
輸出：review/requests/REQ_<head>.md（同時印到 stdout）
"""
import json, subprocess, sys, os, collections, re

MAXLINES = 220          # 單一檔案 diff 的行數上限
MAXTOTAL = 1400         # 全部 diff 的行數上限

def sh(c): return subprocess.run(c, shell=True, capture_output=True, text=True).stdout

def checkpoint():
    p='review/CHECKPOINT'
    return open(p).read().strip().split()[0] if os.path.exists(p) else None

def pilot_stats():
    """統計一律由 JSON 計算，不讓 ChatGPT 自己去 parse。"""
    try:
        d=json.load(open('pilot/nico_pilot.json',encoding='utf-8'))
        reg=json.load(open('pilot/location_registry.json',encoding='utf-8'))
    except Exception:
        return None
    S=d['phase_c_shots']; n=len(S)
    HOME={'own_bedroom','own_kitchen','own_entryway','own_bathroom','own_living_room','own_balcony'}
    ob=d['outfits']
    def clean(s): return (s['filter']=='none' and s['face_visibility']=='unobstructed'
        and s['light']['family'] in ('L2_single_window_daylight','L6_soft_overcast')
        and s['camera']['type']=='phone_rear')
    loc=collections.Counter(s['location'] for s in S)
    anchors=[s for s in S if s.get('pillar')=='anchor']
    return {
      "訓練張數":n, "clean anchor":len(anchors), "lifestyle":n-len(anchors),
      "光線家族":dict(collections.Counter(s['light']['family'] for s in S)),
      "景別":dict(collections.Counter(s['framing'] for s in S)),
      "頭部角度":dict(collections.Counter(s['head_yaw'] for s in S)),
      "視角":dict(collections.Counter(s['view'] for s in S)),
      "濾鏡":dict(collections.Counter(s['filter'] for s in S)),
      "地點層級":dict(collections.Counter(reg['tiers'].get(s['location']) for s in S)),
      "穿搭":dict(collections.Counter(s['outfit_id'] for s in S)),
      "髮型":dict(collections.Counter(s['hair_id'] for s in S)),
      "家+工作室":f"{sum(v for k,v in loc.items() if k in HOME)+loc.get('workplace_own_studio',0)}/{n}",
      "anchor 落在住處或職業空間":f"{sum(1 for s in anchors if s['location'] in HOME or reg.get('defaults',{}).get(s['location']))}/{len(anchors)}",
      "乾淨臉部特寫":sum(1 for s in S if s['framing']=='face_closeup' and clean(s)),
      "乾淨body_readable全身":sum(1 for s in S if s['framing']=='full_body' and ob[s['outfit_id']]['body_readable'] and clean(s)),
      "乾淨右側高資訊角度":sum(1 for s in S if s['head_yaw'].startswith('right') and clean(s) and s['framing'] in ('face_closeup','chest_up')),
      "career_related":f"{sum(1 for s in S if s['career_related'])}/{n}",
      "signature_family":f"{sum(1 for s in S if s['signature_family'])}/{n}",
    }

def open_issues():
    p='review/LEDGER.md'
    if not os.path.exists(p): return []
    out=[]
    for ln in open(p,encoding='utf-8'):
        if not ln.startswith('| '): continue
        c=[x.strip() for x in ln.strip().strip('|').split('|')]
        if len(c)>=5 and re.match(r'^[CKU]-\d+$', c[0]) and '結案' not in c[3]:
            out.append(c)
    return out

def build(base, head):
    files=[f for f in sh(f"git diff --name-only {base}..{head}").split('\n') if f.strip()]
    diff_lines=[]; total=0; skipped=[]
    for f in files:
        d=sh(f"git diff --unified=2 {base}..{head} -- '{f}'").split('\n')
        if total+len(d) > MAXTOTAL or len(d) > MAXLINES:
            skipped.append((f, len(d))); continue
        diff_lines += d; total += len(d)

    L=[];w=L.append
    w("# 覆核請求 — Virtual KOL Studio / Nico Pilot")
    w("")
    w("> **請直接讀這封訊息就好，不要用 GitHub 連接器去抓 repo。**")
    w("> 這封訊息自帶所有需要的內容。抓整個 repo 會爬到約 500KB 的專案背景，")
    w("> 但你真正需要判斷的只有下面這些改動。")
    w("")
    w(f"- 範圍：`{base[:7]}` → `{head[:7]}`")
    w(f"- 變更檔案：{len(files)} 個")
    w("")
    w("---")
    w("")
    w("## 1. 目前的規格數字（由 JSON 自動計算，不用你自己算）")
    w("")
    st=pilot_stats()
    if st:
        w("```json")
        w(json.dumps(st,ensure_ascii=False,indent=1))
        w("```")
    w("")
    w("## 2. 這次改了什麼")
    w("")
    w("```")
    w(sh(f"git log --format='%h %s' {base}..{head}").strip() or "(無 commit)")
    w("```")
    w("")
    w("```diff")
    w("\n".join(diff_lines).strip())
    w("```")
    if skipped:
        w("")
        w("**以下檔案的 diff 過長已略過**（若你需要完整內容請告訴我，我下次貼給你）：")
        for f,n in skipped: w(f"- `{f}`（{n} 行）")
    w("")
    w("---")
    w("")
    w("## 3. 待你判斷的議題")
    w("")
    iss=open_issues()
    if iss:
        w("| ID | 議題 | 提出者 | 狀態 | 備註 |")
        w("|----|------|--------|------|------|")
        for c in iss: w("| "+" | ".join(c[:5])+" |")
    else:
        w("（目前沒有未結案議題）")
    w("")
    w("---")
    w("")
    w("## 4. 請用這個格式回覆")
    w("")
    w("直接把回覆貼回給 Claude 就好，**不要寫回 GitHub**（上一輪試過，沒有成功寫入）。")
    w("")
    w("```")
    w("## 議題裁決")
    w("| ID | 你的判定 | 理由（一兩句）|")
    w("|----|---------|-------------|")
    w("| C-05 | 同意結案 / 不同意，因為… | |")
    w("")
    w("## 新發現（如果有）")
    w("| 新ID | 問題 | 嚴重度 P0/P1/P2 | 建議改法 |")
    w("|------|------|----------------|---------|")
    w("")
    w("## 放行判定")
    w("可以進入生成 / 還不行，因為…")
    w("```")
    w("")
    w("**判斷原則**：可驗證的數字請以第 1 節為準（那是程式算的）。")
    w("如果你認為某個數字不對，請直接指出，Claude 會實測驗證後回覆——")
    w("前兩輪你的數值主張全部正確，但也發生過你引用的官方規格與本專案實際 API endpoint 不同。")
    return "\n".join(L)

if __name__=='__main__':
    base = sys.argv[1] if len(sys.argv)>1 else checkpoint()
    head = sys.argv[2] if len(sys.argv)>2 else 'HEAD'
    if not base:
        print("找不到 base。請建立 review/CHECKPOINT 或以參數指定。", file=sys.stderr); sys.exit(1)
    head_sha = sh(f"git rev-parse --short {head}").strip()
    out = build(base, head)
    os.makedirs('review/requests', exist_ok=True)
    p=f"review/requests/REQ_{head_sha}.md"
    open(p,'w',encoding='utf-8').write(out)
    print(out)
    print(f"\n[已存檔 {p}｜{len(out.encode())/1024:.1f} KB]", file=sys.stderr)
