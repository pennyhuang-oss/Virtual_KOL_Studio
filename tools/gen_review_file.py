#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生 review/REVIEW.md — 單一、自給自足的覆核檔案。

需求：ChatGPT 只讀這一個檔案就要能完全理解「這個專案在做什麼、背景是什麼、
現在要它檢核什麼」，不需要讀 repo 裡任何其他檔案，也不需要前幾輪的對話記憶。

設計重點：
- §0–§8 由本程式產生，統計一律從 JSON 計算（人工抄寫是 C-07 漂移的來源）
- §9 之後是回覆區，**重新產生時完整保留**，ChatGPT 的意見不會被覆蓋
"""
import json, re, collections, subprocess, os, re, hashlib

MARK = "<!-- ===== REPLIES BELOW — 本行以下不會被自動產生覆蓋 ===== -->"

def sh(c): return subprocess.run(c,shell=True,capture_output=True,text=True).stdout.strip()

def load():
    return (json.load(open('pilot/nico_pilot.json',encoding='utf-8')),
            json.load(open('pilot/location_registry.json',encoding='utf-8')))

def stats(d,reg):
    S=d['phase_c_shots']; n=len(S); O=d['outfits']
    HOME={'own_bedroom','own_kitchen','own_entryway','own_bathroom','own_living_room','own_balcony'}
    def clean(s): return (s['filter']=='none' and s['face_visibility']=='unobstructed'
        and s['light']['family'] in ('L2_single_window_daylight','L6_soft_overcast')
        and s['camera']['type']=='phone_rear')
    life=[s for s in S if s.get('pillar')!='anchor']
    anc=[s for s in S if s.get('pillar')=='anchor']
    loc=collections.Counter(s['location'] for s in S)
    hw=lambda xs:[s for s in xs if s['location'] in HOME or reg.get('defaults',{}).get(s['location'])]
    return dict(n=n,anchors=len(anc),life=len(life),
      light=collections.Counter(s['light']['family'] for s in S),
      framing=collections.Counter(s['framing'] for s in S),
      yaw=collections.Counter(s['head_yaw'] for s in S),
      pose=collections.Counter(s['body_pose'] for s in S),
      view=collections.Counter(s['view'] for s in S),
      filt=collections.Counter(s['filter'] for s in S),
      tier=collections.Counter(reg['tiers'].get(s['location']) for s in S),
      loc=loc, outfit=collections.Counter(s['outfit_id'] for s in S),
      hair=collections.Counter(s['hair_id'] for s in S),
      expr=len(set(s['expression'] for s in S)),
      hw_all=len(hw(S)), hw_life=len(hw(life)),
      anchor_in_hw=len(hw(anc)),
      clean_face=sum(1 for s in S if s['framing']=='face_closeup' and clean(s)),
      clean_body=sum(1 for s in S if s['framing']=='full_body' and O[s['outfit_id']]['body_readable'] and clean(s)),
      clean_right=sum(1 for s in S if s['head_yaw'].startswith('right') and clean(s) and s['framing'] in ('face_closeup','chest_up')),
      career=sum(1 for s in S if s['career_related']),
      sig=sum(1 for s in S if s['signature_family']))

def cnt(c,total=None):
    return "、".join(f"`{k}`×{v}"+(f"（{v/total:.0%}）" if total else "") for k,v in c.most_common())

def ledger_open():
    out=[]
    if not os.path.exists('review/LEDGER.md'): return out
    for ln in open('review/LEDGER.md',encoding='utf-8'):
        if not ln.startswith('| '): continue
        c=[x.strip() for x in ln.strip().strip('|').split('|')]
        if len(c)>=5 and re.match(r'^[CKU]-\d+$',c[0]) and '結案' not in c[3]:
            out.append(c)
    return out

def build():
    d,reg=load(); s=stats(d,reg); S=d['phase_c_shots']
    commit=sh("git rev-parse --short HEAD")
    vout=sh("python3 tools/validate_shoot_plan_v2.py pilot/nico_pilot.json")
    L=[];w=L.append

    w("# Nico Pilot — 覆核檔案（自給自足，只讀這一份就夠）")
    w("")
    w("> **⚠️ 這一輪（R1–R9，規劃層覆核）已經結束並全數通過。**")
    w("> validator exit 0、語意逐列覆核 20/20、對抗測試 26/26。")
    w("> **現在進行中的是 R10：20 段實際 prompt 的覆核，檔案在 "
      "[`REVIEW_PHASE_C.md`](REVIEW_PHASE_C.md)。**")
    w("> 本檔保留作為規劃層的完整紀錄。")
    w("")
    w("## §0 給審閱者")
    w("")
    w("**你只需要讀這一個檔案。** 不要用 GitHub 連接器去抓 repo 裡的其他檔案——")
    w("這個專案光 `.md` 就約 500KB，爬完會把使用者的方案用量燒光，而你真正需要的內容全在這裡。")
    w("")
    w("**回覆方式**：把你的意見**直接寫在本檔案最下方 §9 回覆區**（在 `REPLIES BELOW` 那行以下）。")
    w("那一段不會被自動產生覆蓋。Claude 會讀你寫的內容並修正。")
    w("")
    w(f"- 目前 commit：`{commit}`")
    w(f"- 檔案角色：本檔 §0–§8 由 `tools/gen_review_file.py` 從 `pilot/nico_pilot.json` 自動產生，"
      "所有數字都是程式算的，不是人工抄的")
    w("")
    w("---")
    w("")
    w("## §1 這個專案在做什麼")
    w("")
    w("**Virtual KOL Studio** 是一個虛擬 KOL（AI 生成的網紅角色）資料庫。每個角色有完整人設，")
    w("用 AI 生圖平台 Higgsfield 產生素材，發布到 Instagram / TikTok / X。")
    w("")
    w("內容方向是模仿日本 AV 女優公開社群帳號的風格，強調**寄生親密感**——讓粉絲感覺")
    w("「偷窺到她的私下生活」。所有素材維持 SFW（不露骨、不涉及未成年）。")
    w("")
    w("### 什麼是「建模照」")
    w("")
    w("要讓同一個虛擬角色在不同素材裡長得像同一個人，必須先訓練一個專屬的身分模型")
    w("（Higgsfield **Soul V2**）。訓練完成得到一個 `soul_id`，之後所有生成都掛這個 id。")
    w("**建模照**就是拿去訓練這個模型的那組照片。")
    w("")
    w("**關鍵技術限制**：Soul V2 不繼承訓練圖的髮型與髮色，每次生成都要在 prompt 裡重寫。")
    w("")
    w("### 目前進度")
    w("")
    w("- repo 裡已有 **6 個角色的 Soul 訓練完成**並在生產環境用了數週")
    w("- 現在要新增 20 位（Batch 3），**Nico Tsai 是第一個 pilot**，走完整流程驗證方法")
    w("- **尚未生成任何一張圖**。這份規劃通過覆核才會開始花錢")
    w("")
    w("### 為什麼挑 Nico 當 pilot")
    w("")
    w("26 歲台灣籍美甲師，**短鮑伯 + 冷灰奶茶漂色 + C 罩杯纖細身材**——")
    w("是全批 20 位裡最容易失敗的組合（模型傾向把所有人畫成豐滿、把漂色畫成銀白、把短髮加長）。")
    w("而且她在第一輪已經失敗過一次，有前後對照價值。")
    w("")
    w("---")
    w("")
    w("## §2 流程：四個階段")
    w("")
    w("| 階段 | 內容 | 張數 | 目的 |")
    w("|------|------|------|------|")
    w("| **A 選角** | 4 個候選 identity | 4 | 挑出「臉＋上半身輪廓」成立的那一個 |")
    w("| **B 錨定驗證** | Reference Element + B1/B2 | 2 | B1 驗能不能重現、B2 驗能不能輕度外推。身材比例的最終把關在這裡 |")
    w("| **C 訓練集** | 正式建模照 | 20 | 送進 Soul 訓練 |")
    w("| **D 壓力測試** | 訓練後的漂移測試 | 13 | 這個 repo 從來沒做過的一步 |")
    w("")
    w("### Phase A 為什麼是「4 個候選人」不是「同一人的 4 個視角」")
    w("")
    w("這個 repo 自己的歷史證實：另一個角色 Rainie 的 4 張候選圖是**各自獨立生成的 4 個人**，")
    w("身材差異大到後來必須換錨點、整批 13 張訓練圖與一個 soul_id 全部作廢重做。")
    w("所以不可假設「4 次無錨定呼叫會得到同一個人」。")
    w("")
    w("### 訓練張數的實際限制")
    pf=d['training_endpoint_preflight']
    w("")
    w(f"直接讀本專案實際呼叫的 API 工具 schema（`{pf['tool']}`），逐字內容：")
    w("")
    w("```")
    w(pf['verbatim'])
    w("```")
    w("")
    w(f"→ **{pf['min_training_images']}–{pf['max_training_images']} 張**。"
      "（官網 Help Center 寫 minimum 20，那是 Web UI 規格，與本專案使用的 API 不同。）")
    w("")
    w("---")
    w("")
    w("## §3 這個專案的既有規則（判斷時請以這些為準）")
    w("")
    w("### 3-1 人設憲章")
    w("")
    w("1. **反差公式**：檯面上是公開面貌（日常、得體）；私底下在自己的私人平台展現性感的一面。")
    w("   **不是**「回家就鬆垮邋遢」。**檯面 ≠ 職業**——不公開職業本身就是成立的設定。")
    w("2. **標誌性場景配額**：泳池、和服、女僕裝、直播間等高辨識度場景不得成為主支柱或超過 25%。")
    w("   判斷法：「如果這個設定成立，她一年 365 天會不會有 300 天都長這樣？」")
    w("3. **造型可變**：髮色髮型是現階段設定，不是永久鎖定。")
    w("4. **不寫絕對禁令**：用「預設、多數時候」「不常見（不是不可能）」。")
    w("5. **單一真理來源**：支柱以 JSON 為準，全檔同步。")
    w("")
    w("### 3-2 造型差異化四轉盤")
    w("")
    w("來自拆解一個競品帳號（全 AI 生成的虛擬 KOL，57 萬粉，抽樣 60 則貼文 109 張圖）。")
    w("核心診斷：**把「造型」綁死在「內容主題」上，每個角色會被自己的人設關進一個房間。**")
    w("")
    w("| 轉盤 | 規則 |")
    w("|------|------|")
    w("| 穿搭 | 每位至少 8 種明顯不同的風格區間；連續兩則不得同區間；招牌風格 ≤30% |")
    w("| 髮型 | 至少 5 種變體，**每則明確指定**，不可讓模型自己決定 |")
    w("| 地點層級 | 每 10 則：A 級 2–3、B 級 4–5、**C 級至少 2（硬性下限）** |")
    w("| 微物件 | 每則至少換 2 樣，**prompt 中必須具體點名** |")
    w("")
    w("**地點三層級**：**A**＝一般人做不到的（遊艇、五星飯店套房、豪華 villa）；")
    w("**B**＝偶爾會去的（咖啡廳、餐酒館、自宅、工作場所）；")
    w("**C**＝天天在做且完全不美的（賣場、超商、加油站、洗衣店、藥妝店、車站月台、早餐店）。")
    w("")
    w("> **C 級是整套系統的靈魂。** 全部都是 A 級的帳號讀起來像型錄。")
    w("> 競品敢在 57 萬粉的帳號上發 Costco 推推車、麥當勞飲料杯——")
    w("> 正是這些一點都不美的地方，讓觀眾相信「她是個剛好很有錢的真人」。")
    w("")
    w("### 3-3 五段式物理光線公式")
    w("")
    w("拆解競品 31 張素材後的結論：**她做對的不是把光線寫得更漂亮，")
    w("而是把光線寫成「物理規格」而不是「品質形容詞」。**")
    w("寫 `golden hour`、`crisp`、`well-exposed` 只告訴模型「要好看」，")
    w("沒告訴它「光從哪來、被什麼反射回來、哪裡該暗」——**這正是 AI 感的主要來源**。")
    w("")
    w("每個 prompt 的光線要寫滿五段：")
    w("")
    w("| 段 | 內容 |")
    w("|----|------|")
    w("| ① KEY | 具名、畫面內可指認的光源＋方向＋高度 |")
    w("| ② BOUNCE | **具名的物理反射面**＋它把什麼顏色的光丟回主體（最大的缺口）|")
    w("| ③ 色溫分裂 | 畫面裡同時存在的兩個色溫（**可為 null，不強制**）|")
    w("| ④ 曝光取捨 | 相機對什麼測光，因此什麼被允許過曝或壓黑 |")
    w("| ⑤ 遮擋/框架 | 鏡頭與主體之間形塑光線的實體 |")
    w("")
    w("**bounce 要區分**：`diffuse`（白牆／床單／淺色地板，能整體補亮）")
    w("vs `specular`（鏡面／玻璃／金屬／烤漆，只產生高光，不能當柔和填光）。")
    w("")
    w("### 3-4 其他硬規則")
    w("")
    w("- **服裝五層**：上身（單品＋材質＋顏色＋**領型**）＋下身＋鞋＋包或外套＋首飾髮飾。")
    w("  只寫 `casual top and shorts` 一律退回。不寫領型模型會自補低胸，導致身材判讀失真。")
    w("- **自拍/他拍混合**：自拍要寫 `front camera quality, slightly softer focus, NOT ultra-crisp`；")
    w("  他拍才用 `crisp sharp focus`。")
    w("- **皮膚質感**：每個 prompt 加 `visible skin pores, natural skin imperfections`，")
    w("  **避免** `smooth`／`flawless`／`airbrushed`／`porcelain skin`。")
    w("- **膚色**：全批一律白皙瓷感，明確排除 `tanned`／`bronzed`／`olive`／`deep golden`。")
    w("- **模型選擇**：選角階段用 `seedream_v4_5`。**不可用 `soul_2`**——")
    w("  沒有 soul_id 錨定時它每次呼叫都會重新想像一張臉。")
    w("")
    w("---")
    w("")
    w("## §4 前八輪覆核發生過什麼（你的前任意見與 Claude 犯過的錯）")
    w("")
    w("| 輪次 | 發現的主要問題 |")
    w("|------|---------------|")
    w("| R1 | Claude 自己發明「攝影棚定裝照」，違反 6 條 repo 早就寫好的規則。實際出圖把泡棉板、棚燈、門框、相機全畫進畫面；景別指令失效（指定臉部特寫出成全身）；髮色從冷灰奶茶變銀白 |")
    w("| R2 | Claude 寫了一支「為了讓 validator PASS 而改資料」的程式，它只改 outfit/hair 數字沒動 scene 文字 → 12 列服裝衝突、14 列髮型衝突；濾鏡與視角用列位置指派 → 20 位的第 1 列全是 meitu＋自拍 |")
    w("| R3 | 覆核包統計與 JSON 漂移（寫 5 種 lighting 實際 6 種、寫 L1×3 實際 ×5、寫 4+4 場景實際 3+3）。原因是人工抄寫 |")
    w("| R4 | `schema_v2.json` 根本沒被執行（對抗測試：注入非法 enum 仍 PASS）；anchor 的 scene 寫「坐著」但欄位是 `standing`；label override 可用一個理由同時放行兩欄 |")
    w("| R5 | 兩個 P0：(a) 語意覆核 0/20，validator 卻印「✓ 全數通過」且 exit=0——這個 gate 形同虛設；(b) Phase C 三個物理矛盾（鐵門遮住的正是那面落地窗／修眉＋撐洗手台＋持機＝三隻手／衣櫃把「赤腳」寫進定義卻用在公園）。另外 Phase D 宣稱單一變量但實際同時改 3 個欄位，且 st08b 宣稱測下打光——那個變量根本沒有編碼進任何欄位 |")
    w("| R6 | 我自己挖的坑：§8 要求逐列覆核 9 個欄位（含 props），但本檔從來沒有揭露過任何一列的 props——審閱者不可能完成。補上 props 表之後，當場看到 8 列 props 重述 outfit 已有的包、`c10` 第三隻手、`c07` 把客人的手放進訓練集。另外 `c12` 刪掉車頭燈時沒同步改曝光敘述（改一欄忘另一欄，第三次）；`st06` 拿訓練集出現 4 次的 park 去測固定背景烙印 |")
    w("| R7 | 20 列語意覆核只有 11 列無異議，9 列 P0。最大的一類：**微物件寫在 framing 裁切外**——`a01` 是臉部特寫卻把道具放在桌上，`c02` 蹲著拆箱卻用 chest_up，`c12` 的「月台地上黃線」還是我 R6 自己加的。另外 `c04` 的 scene 寫「剛醒」但 hair_06 定義是「剛洗完澡滴水濕髮」；`c05` 的髮夾同時由 outfit 與 hair 定義——**C-01 那個雙重真理來源的病，換一對欄位重演** |")
    w("| R8 | 20 列覆核 19 列無異議，只剩 `c04` 一條 P0：R7 把 scene 從「剛醒」改成「剛洗完澡」對齊髮型時，`expression` 還留著 `just_woken_blank`——**修一個跨欄位矛盾的同時製造了另一個**，同一類錯第五次。連帶暴露一個流程缺陷：語意覆核用整份資料一個 hash，改一列就作廢全部 20 列的核可，覆核與修正會互相打架、永遠收斂不了；已改為逐列 hash |")
    w("")
    w("**共同模式**：Claude 反覆犯的是同一類錯——**改了一個欄位，沒有同步改另一個**，")
    w("以及**把規則形式化之後，對規則本身過度擬合**（為了湊 quota 把普通場景標成 A 級）。")
    w("")
    w("**R5 的教訓**：機器 lint 全過，不代表計畫成立。R5 的 4 個矛盾都是在 validator 印")
    w("「✓ 全數通過」的狀態下被人讀出來的。所以本輪起，語意逐列覆核未達 20/20 一律 HARD FAIL。")
    w("")
    w("目前這一版是 R5 的 13 條判定 + 4 條新議題全部處理完之後的結果。")
    w("")
    w("---")
    w("")
    w("## §5 現行規格（全部由 JSON 計算）")
    w("")
    w("### 5-1 身分規格")
    i=d['identity_spec']
    w("")
    w(f"- 年齡／族裔：{i['age']} / {i['ethnicity']}")
    w(f"- 膚色：{i['skin']}")
    w(f"- 排除：{i['skin_negative']}")
    w(f"- 臉部基底：{i['face_base']}")
    w("- **身分 marker**（讓模型學到「某一個具體的人」而不是 generic beautiful East Asian woman）：")
    for m in i['identity_markers']: w(f"  - {m}")
    w(f"- 註：{i['_markers_note']}")
    w(f"- 身材數字（metadata）：{i['body_numeric']}")
    w(f"- **身材視覺比例（prompt 實際使用）**：{i['body_visual']}")
    w(f"- 排除：{i['body_negative']}")
    w("")
    w("### 5-2 造型庫")
    w("")
    w("| ID | 區間 | 領型 | 上身 | 下身 | 鞋 | 包/外套 | 首飾 | 身材可讀 |")
    w("|----|------|------|------|------|----|---------|------|---------|")
    for k,o in d['outfits'].items():
        w(f"| `{k[-2:]}` | {o['label']} | {o['neckline']} | {o['top']} | {o['bottom']} | {o['shoes']} | {o['outer_or_bag']} | {o['jewelry']} | {'✅' if o['body_readable'] else '❌'} |")
    w("")
    w("**髮型變體**")
    w("")
    for k,v in d['hair'].items(): w(f"- `{k[-2:]}`：{v}")
    w("")
    w("### 5-3 Phase A — 4 個候選 identity")
    a=d['phase_a']; ic=a['identical_across_all_four']
    w("")
    w(f"**4 張完全相同**：framing `{ic['framing']}`／yaw `{ic['head_yaw']}`／pose `{ic['body_pose']}`／"
      f"view `{ic['view']}`／outfit `{ic['outfit_id'][-2:]}`／hair `{ic['hair_id'][-2:]}`／"
      f"location `{ic['location']}`／DOF `{ic['camera']['depth_of_field']}`")
    w("")
    w(f"**唯一變數**：{a['varies_only']}")
    w("")
    w("**選角服硬性規則**：")
    for r in a['phase_a_outfit_rules']: w(f"- {r}")
    w("")
    w(f"**範圍修正**：{a.get('_scope_correction','')}")
    w("")
    w("### 5-4 Phase B")
    pb=d['phase_b']
    w("")
    for k in ('B1','B2'):
        x=pb[k]
        w(f"- **{k}**（{x['purpose']}）：framing `{x['framing']}`／yaw `{x['head_yaw']}`／"
          f"location {x['location']}／outfit {x['outfit_id']}／hair {x['hair_id']}／light {x['light']}")
    w(f"- {pb['B2'].get('_why','')}")
    w(f"- {pb.get('final_body_gate','')}")
    w("")
    w(f"### 5-5 Phase C — {s['n']} 張訓練集（{s['anchors']} clean anchor + {s['life']} lifestyle）")
    w("")
    w("| # | id | 目的 | 場景 | 地點 | 層級 | outfit | hair | framing | yaw | pitch | 表情 | 姿態 | 視線 | 視角 | 臉部 | 光線家族 | bounce | 濾鏡 | 招牌 | 職業 |")
    w("|---|----|------|------|------|------|--------|------|---------|-----|-------|------|------|------|------|------|---------|--------|------|------|------|")
    for n_,x in enumerate(S,1):
        w(f"| {n_:02d} | `{x['shot_id'][-3:]}` | {x['purpose']} | {x['scene']} | `{x['location']}` | "
          f"{reg['tiers'].get(x['location'])} | `{x['outfit_id'][-2:]}` | `{x['hair_id'][-2:]}` | {x['framing']} | "
          f"{x['head_yaw']} | {x['head_pitch']} | {x['expression']} | {x['body_pose']} | {x['eye_gaze']} | "
          f"{x['view']} | {x['face_visibility']} | {x['light']['family']} | {x['light']['bounce_type']} | "
          f"{x['filter']} | {x['signature_family'] or '—'} | {'是' if x['career_related'] else '—'} |")
    w("")
    w("**每張的光線五段**")
    w("")
    for n_,x in enumerate(S,1):
        l=x['light']; ip=x['imperfection_profile']
        w(f"- **{n_:02d} `{x['shot_id'][-3:]}`** ① {l['key']}｜② （{l['bounce_type']}）{l['bounce']}｜"
          f"③ {l['secondary_source'] or '**無**（刻意留白）'}｜④ {l['exposure_choice']}｜⑤ {l['occlusion'] or '無'}")
        w(f"  - 不完美變數：構圖 {ip['composition']}／動態 {ip['motion']}／白平衡 {ip['white_balance']}／"
          f"背景 {ip['background_clutter']}／高光 {ip['highlight_clipping']}／identity_safe {ip['identity_safe']}")
    w("")
    w("")
    w("#### 5-5b 每列的 props（微物件）")
    w("")
    w("> C-27/C-29：props 與 hands 已改為結構化。每個 prop 有 `id`／`relation`／`zone`／`expected_visible`；")
    w("> 每隻手有 `state`（free｜holding｜supporting｜camera）與 `object_ref`（**只能引用 prop id，不得另寫同義詞**）。")
    w("> `zone` 是該物件靠近哪個身體地標，**依該 shot 的實際姿態判定，不是套站姿公式**——")
    w("> 蹲著拆箱時地上的紙箱就在膝線，不在腳下。validator 用 framing→zone 對照表反查可見性。")
    w("> 左右一律指**角色的解剖學左右、鏡像翻轉前**（`selfie_mirror` 出圖會左右翻，欄位不翻）。")
    w("> C-23（上一輪）：本檔原本沒有揭露任何一列的 props——這是本檔的生成漏洞。")
    w("> 補上之後當場看到 8 列的 props 重述了 outfit 已提供的包/外套或借用別套的招牌包、")
    w("> `c10` 抱著衣物還多一隻手拿零錢、`c07` 把「客人的手」放進訓練集。全部已修。")
    w("> 並新增 **`hands` 欄位（left / right 兩個槽位）**：人只有兩隻手，")
    w("> 把手部佔用從 scene＋props 的推論改成明寫，validator 才稽核得動。")
    w("> 判斷 props 時請一併檢查：道具是否與 framing 同時可見、拍攝裝置有沒有又被當入鏡道具、")
    w("> 雙手有沒有被 scene＋props＋持機重複占用、outfit 自帶的包／飾品有沒有在 props 重複生成。")
    w("")
    FZ={'face_closeup':'head','chest_up':'head,chest','waist_up':'head,chest,waist',
        'knee_up':'head,chest,waist,hip,knee','full_body':'全部含 floor'}
    w("| id | framing（看得到的 zone）| view | 左手 | 右手 | props（relation・zone）| outfit 自帶的包/外套・首飾 |")
    w("|----|----------------------|------|------|------|----------------------|--------------------------|")
    for x in S:
        o=d['outfits'][x['outfit_id']]; h=x['hands']
        def hh(sl):
            r=f"`{sl['state']}`"
            if sl.get('object_ref'): r+=f"→`{sl['object_ref']}`"
            return r+f"（{sl['note']}）"
        pr="；".join(f"`{q['id']}` {q['name']}（{q['relation']}・{q['zone']}）" for q in x['props'])
        w(f"| `{x['shot_id']}` | {x['framing']}（{FZ[x['framing']]}）| {x['view']} | {hh(h['left'])} | "
          f"{hh(h['right'])} | {pr} | {o['outer_or_bag']}・{o['jewelry']} |")
    w("")
    w("### 5-6 現行分布（程式計算）")
    w("")
    w(f"- **光線家族**：{cnt(s['light'],s['n'])}")
    w(f"- **景別**：{cnt(s['framing'])}")
    w(f"- **頭部角度**：{cnt(s['yaw'])}")
    w(f"- **身體姿態**：{cnt(s['pose'])}")
    w(f"- **視角**：{cnt(s['view'])}")
    w(f"- **濾鏡**：{cnt(s['filt'])}")
    w(f"- **地點層級**：{cnt(s['tier'])}")
    w(f"- **地點**：{cnt(s['loc'])}")
    w(f"- **穿搭**：{cnt(s['outfit'],s['n'])}")
    w(f"- **髮型**：{cnt(s['hair'])}")
    w(f"- **表情種類**：{s['expr']} 種")
    w(f"- **乾淨臉部特寫 / 乾淨 body-readable 全身 / 乾淨右側**：{s['clean_face']} / {s['clean_body']} / {s['clean_right']}")
    w(f"- **home+work**：全體 {s['hw_all']}/{s['n']}（{s['hw_all']/s['n']:.0%}）、"
      f"lifestyle 子集 {s['hw_life']}/{s['life']}（{s['hw_life']/s['life']:.0%}）、"
      f"**anchor 落在住處或職業空間 {s['anchor_in_hw']}/{s['anchors']}**")
    w(f"- **career_related**：{s['career']}/{s['n']}（上限 40%）｜**signature_family**：{s['sig']}/{s['n']}（上限 25%）")
    w("")
    w("### 5-7 Phase D — 壓力測試")
    pd=d['phase_d_stress_test']
    w("")
    w(f"{pd['_purpose']}")
    w("")
    fb=pd['fixed_baseline']
    w("**固定基準**："+"、".join(f"`{k}`={v}" for k,v in fb.items() if not k.startswith('_')))
    if fb.get('_note'): w("")
    if fb.get('_note'): w(f"> {fb['_note']}")
    w("")
    w(f"**seed 政策**：{pd['seed_policy']}")
    w("")
    w(pd.get('_c21_note',''))
    w("")
    w("| id | 被測維度（primary）| 為了量得到而必須連動改的 | 期望不變的是 | 適用 rubric | replicates | 依賴 |")
    w("|----|-------------------|------------------------|-------------|------------|-----------|------|")
    for x in pd['shots']:
        prim=x.get('primary_test_variable')
        pv=f"`{prim['field']}` = {prim['value']}" if prim else "—（基準線）"
        rmc=x.get('required_measurement_changes',{})
        rv="；".join(f"`{k}`（{v}）" for k,v in rmc.items()) or "無"
        w(f"| `{x['id']}` | {pv} | {rv} | {x['expected_invariant']} | {'、'.join(x['applicable_rubric_items'])} | "
          f"{x['replicates']} | {x.get('depends_on') or '—'} |")
    w("")
    # C-21：render 數與成本一律現算，不得手寫
    cond=[x for x in pd['shots'] if x.get('depends_on')]
    tot=sum(x['replicates'] for x in pd['shots'])
    cond_r=sum(x['replicates'] for x in cond)
    w(f"**render 預算（現算，非手寫）**：{len(pd['shots'])} 是 test case 數，不是 render 數。"
      f"依 replicates 加總，每個 soul {tot-cond_r}–{tot} 張"
      f"（{len(cond)} 個條件式 shot：{'、'.join(x['id'] for x in cond) or '無'}）。"
      f"Retroactive Benchmark 跑 GOOD + KNOWN_BAD 兩個 soul = {2*(tot-cond_r)}–{2*tot} 張。")
    w("")
    # C-07：集中度沿用同一份現算 stats，不得手寫
    w(f"**已知風險（現算）**：家＋工作場所共 {s['hw_all']}/{s['n']}（{s['hw_all']/s['n']:.0%}）；"
      f"{s['anchors']} 張 clean identity anchor 中有 {s['anchor_in_hw']} 張落在這兩個空間。"
      f"若 stress test 仍出現固定背景烙印，代表 lifestyle 那 {s['life']} 張的世界集中度還要再降。"
      f"（C-07：此段原本是 JSON 內嵌的手寫字串，資料一改就變舊值，已改為與 §5-6 同源現算。）")
    w("")
    w("### 5-8 Soul QA Rubric")
    r=d['soul_qa_rubric']; tm=r['threshold_method']
    w("")
    w(f"{r['_scale']}　9 個項目：{'、'.join(r['items'])}")
    w("")
    w("**Hard gates（總分無法掩蓋的關鍵失敗）**：")
    for g in r['hard_gates']: w(f"- {g}")
    w("")
    w(f"**總分門檻**：{r['aggregate_threshold']}")
    w("")
    w(f"**訂定方法：{tm['name']}**")
    for k in ('_why','ground_truth','persona_adaptation','scoring_aggregation','replicates','_cost_note'):
        if tm.get(k): w(f"- **{k}**：{tm[k]}")
    w("")
    w("**baseline**（由使用者裁決）：")
    for k,v in tm['baselines'].items():
        w(f"- **{k}** {v['persona']}（`{v['soul_id'][:8]}`，{v['status']}）：{v['_why']}")
        if v.get('_expected_signal'): w(f"  - 預期訊號：{v['_expected_signal']}")
    w("")
    w("---")
    w("")
    w("## §6 驗證器做了什麼")
    w("")
    w("`tools/validate_shoot_plan_v2.py`，只用標準函式庫。目前的檢查：")
    w("")
    w("- **schema 執行**：從頂層驗，`phase_c_shots` 透過 `$ref` 綁到 shot 定義；required／enum／minItems／"
      "未定義欄位／shot_id 唯一性")
    w("- **語意衝突**：scene 不得出現服裝／髮型／濾鏡詞（單一真理來源）、影片語言、一列多時空、"
      "**scene 描述的姿態與 `body_pose` 不符**")
    w("- **光線**：五段完整性、`specular` 誤當柔和填光、lighting family ≥4 種、L1 醜頂光上限")
    w("- **身分覆蓋**：yaw／framing／pose／expression／face_visibility 覆蓋率、髮型變體全覆蓋、"
      "乾淨錨點下限（臉部特寫／body-readable 全身／右側高資訊角度）")
    w("- **世界集中度**：home+work 全體與 lifestyle 子集雙層上限、`location+outfit+hair` 三重固定組合重複"
      "（anchor 之間豁免，那是控制組）")
    w("- **標籤**：`signature_family`／`career_related` 由 registry 推導，兩欄各自獨立 override 且需理由，"
      "quota 以 effective value 計算")
    w("- **Phase gate**：A 四候選必須固定 10 個欄位且唯一變數是 identity；B2 必須真的換場景/穿搭/髮型/光線；"
      "D 的 fixed／rubric item 存在性／depends_on 指向／rubric 全覆蓋")
    w("- **反漂移**：禁止內嵌人工宣告的衍生統計，並反算 `structure`／`shots` 的宣告值")
    w("- **訓練安全**：`identity_safe`／`face_motion_blur`／`face_detail_preserved`；"
      "`full_body` 禁 shallow DOF；CCD 禁用於 `full_body`")
    w("- **語意覆核 gate**：機器 lint 通過後仍需逐列人／LLM 覆核，紀錄用 hash 綁資料，改資料自動失效")
    w("")
    w("**對抗測試結果**：注入 7 個違規（拿掉 Phase A 必固定欄位、B2 場景設同 B1、rubric 引用不存在項目、"
      "塞回人工統計、structure 宣告 99+1、無理由的雙欄 override），**7/7 全數抓到**。")
    w("另一次注入 4 個 schema 違規（非法 framing／非法 yaw／空 props／非法 DOF），**4/4 全數抓到**。")
    w("")
    w("**目前輸出**：")
    w("")
    w("```")
    w(vout)
    w("```")
    w("")
    w("---")
    w("")
    w("## §7 議題帳本現況")
    w("")
    op=ledger_open()
    if op:
        w("| ID | 議題 | 提出者 | 狀態 | 備註 |")
        w("|----|------|--------|------|------|")
        for c in op: w("| "+" | ".join(c[:5])+" |")
    else:
        w("（目前沒有未結案議題）")
    w("")
    w("狀態圖例：🔵 Claude已修正（待你確認）　🟡 待處理　⚪ 待回應　🔴 有爭議")
    w("")
    w("---")
    w("")
    w("## §8 本輪請你判斷")
    w("")
    w("### 8-1 上一輪的結果")
    w("")
    w("你 R8 的 C-33 屬實，已修（`expression` → `post_shower_calm`）。")
    w("C-31／C-32 我同意，但按你的判定不阻擋 Nico，已列為 **persona #2 的前置 gate**（見 §7）。")
    w("")
    w("**你 R8 判無異議的 19 列已經記進 `pilot/semantic_review.json`**，")
    w("每一列連同它自己的 hash 一起簽在你名下。這些列自 R8 之後沒有再動過。")
    w("")
    w("順帶修掉一個流程缺陷：原本語意覆核是**整份資料一個 hash**，改一列就作廢全部 20 列，")
    w("覆核與修正會互相打架、永遠收斂不了。已改成**逐列 hash**——改一列只失效那一列。")
    w("所以現在 validator 顯示 **19/20**，唯一缺的就是 `nico_c04`。")
    w("")
    w("### 8-2 這一輪只需要你做一件事")
    w("")
    w("**重審 `nico_c04` 這一列**（§5-5 與 §5-5b 都找得到）。改動只有一個欄位：")
    w("`expression` 從 `just_woken_blank` 改成 `post_shower_calm`，其餘欄位與你 R8 看到的完全相同。")
    w("")
    w("請確認這一列的 `scene`／`outfit`／`hair`／`framing`／`view`／`eye_gaze`／`body_pose`／")
    w("`expression`／`props`／`hands`／`light` 現在是否同時成立。")
    w("")
    w("如果沒問題就回「`nico_c04` 無異議」，**Nico 就開始生成**（Phase A 4 張選角 → B 錨定 → C 訓練 → Soul → D 壓力測試）。")
    w("如果還有問題，請說明並給修正方向。")
    w("")
    w("（若你另外看到 §7 裡任何一條需要翻案，也一併說；但不必再重掃 19 列。）")
    w("")
    w("**判斷原則**：§5 的數字都是程式算的。如果你認為某個數字不對，直接指出——")
    w("Claude 會實測驗證。R5 與 R6 你提的每一條我都實跑驗證過，數值主張全部屬實；")
    w("唯一一次分歧是你引用的官方訓練張數規格與本專案實際 API endpoint 不同（見 §2）。")
    w("")
    w("---")
    w("")
    w("## §9 你的回覆區")
    w("")
    w("把意見寫在下面這行以下。Claude 會讀這一段。")
    w("")
    w(MARK)
    w("")
    return "\n".join(L)

if __name__=='__main__':
    body=build()
    p='review/REVIEW.md'
    replies=""
    if os.path.exists(p):
        old=open(p,encoding='utf-8').read()
        if MARK in old: replies=old.split(MARK,1)[1]
    open(p,'w',encoding='utf-8').write(body+replies)
    print(f"已產生 {p}（{os.path.getsize(p)/1024:.1f} KB）")
    if replies.strip(): print(f"  已保留回覆區 {len(replies)} 字元")
