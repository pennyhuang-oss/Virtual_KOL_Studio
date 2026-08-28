#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生 review/REVIEW_PHASE_C.md — 生成前最後一關的覆核檔。

與前九輪不同：前面覆核的是**計畫**（結構、配額、物理一致性），那一關已經通過。
這一份要覆核的是**真的會送進模型、會花掉 credit 的那 20 段 prompt 文字**。
"""
import json, os, subprocess

MARK = "<!-- ===== REPLIES BELOW — 本行以下不會被自動產生覆蓋 ===== -->"

def sh(c): return subprocess.run(c, shell=True, capture_output=True, text=True).stdout.strip()

def build():
    p = json.load(open('pilot/nico_pilot.json', encoding='utf-8'))
    pr = json.load(open('pilot/phase_c_prompts.json', encoding='utf-8'))
    en = json.load(open('pilot/phase_c_actions_en.json', encoding='utf-8'))
    reg = json.load(open('pilot/location_registry.json', encoding='utf-8'))['tiers']
    S = p['phase_c_shots']
    L = []; w = L.append

    w("# Nico Pilot — Phase C 20 段 prompt 覆核（生成前最後一關）")
    w("")
    w("## §0 給審閱者")
    w("")
    w("**你只需要讀這一個檔案。** 不要用 GitHub 連接器去抓 repo 裡的其他檔案——")
    w("背景、規則、判斷所需的一切都在這份檔案裡。")
    w("")
    w("**回覆方式**：把意見寫在本檔案最下方 §7 回覆區（`REPLIES BELOW` 那行以下），然後 commit。")
    w("那一段不會被自動產生覆蓋。")
    w("")
    w(f"- 目前 commit：`{sh('git rev-parse --short HEAD')}`")
    w("- 議題編號請從 **C-34** 起跳，每條標 **P0**（必須先修才能生成）／**P1**／**P2**")
    w("")
    w("---")
    w("")
    w("## §1 現在在哪一步")
    w("")
    w("**Virtual KOL Studio** 是虛擬 KOL 資料庫。要讓同一個角色在不同素材裡長得像同一個人，")
    w("必須先用一組**建模照**訓練身分模型（Higgsfield Soul V2）。Nico Tsai 是 Batch 3 的 pilot。")
    w("")
    w("你（ChatGPT）已經覆核過九輪，那九輪針對的是**計畫**：結構、配額、欄位矛盾、")
    w("物理一致性、gate 設計。結果：")
    w("")
    w("- `tools/validate_shoot_plan_v2.py` exit 0")
    w("- 20 列九欄語意逐列覆核 **20/20**（你在 R8/R9 簽核）")
    w("- 對抗測試 26/26")
    w("")
    w("**然後我們第一次真的去生成，結果全錯。** 這是本輪的關鍵背景——")
    w("計畫層的 QA 管的是「這個計畫成不成立」，管不到「這段文字送進模型會被怎麼解讀」。")
    w("")
    w("目前進度：")
    w("")
    w("| 階段 | 狀態 |")
    w("|------|------|")
    w("| A 選角（4 個候選 identity）| ✅ 使用者選定 candidate_03 |")
    w("| Reference Element 錨點 | ✅ `nico-tsai-anchor` 已建立 |")
    w("| B1 驗重現 | ✅ 臉完全重現 |")
    w("| B2 驗輕度外推（全身＝身材最終把關）| ✅ 第一次失敗、修正後通過 |")
    w("| **C 訓練集 20 張** | **← 本輪覆核的對象，尚未生成** |")
    w("| Soul 訓練 → D 壓力測試 | 未開始 |")
    w("")
    w("**尚未生成任何一張訓練圖。你放行才會開始花這 20 張的 credit。**")
    w("")
    w("---")
    w("")
    w("## §2 實測得到的模型行為規則（判斷 prompt 時請以這些為準）")
    w("")
    w("這些不是理論，是前三輪燒掉 13 張換來的。**每一條都有前後對照。**")
    w("")
    w("### 2-1 這個模型不執行否定句")
    w("")
    w("首批 4 張同時出現五個缺陷，全部源自否定句被忽略：")
    w("")
    w("| 失效寫法（否定）| 有效寫法（正面描述目標狀態）|")
    w("|----------------|---------------------------|")
    w("| `nothing below the knee is visible` | `the bottom edge of the picture cuts straight across her thighs` |")
    w("| `NOT a crop top, no exposed midriff` | `the hem is long and tucked into her trouser waistband` |")
    w("| `no ombré, no dark roots, no lightened tips` | `a single flat salon dye job done right down to the scalp: the hair at her roots is exactly the same brown as the ends` |")
    w("| `NOT a full-length shot` | （刪除，改由「下緣切在哪裡」承擔）|")
    w("")
    w("**顏色排除仍然有效**（`not tanned` 有效），**構圖與服裝結構的否定完全無效**。")
    w("")
    w("### 2-2 身體朝向不能寫角度")
    w("")
    w("`turned about 30 degrees toward her own left` 連續**三次**被畫成背影")
    w("（Round 2 首批、Round 3 的 c01、B2 第一次）。`her back is not toward the camera` 無效。")
    w("")
    w("有效寫法是描述**相機看得到哪些身體正面特徵**：")
    w("")
    w("> Her navel and the front of both shoulders point toward the camera. Both of her collarbones are")
    w("> visible. The camera sees the front of her jeans — the fly, the button and the front pockets —")
    w("> not the back pockets.")
    w("")
    w("一次就對。**因此本批 20 段的朝向一律用這個寫法，不出現任何角度數字。**")
    w("")
    w("### 2-3 景別指令要放最前面，而且要說「下緣切在哪裡」")
    w("")
    w("景別失效在本 repo 已經發生三次（rainie R1、nico R1、nico Round 2），")
    w("R1 記的修法「放第一行＋排他措辭」實測**無效**。有效的是把畫面下緣的位置講出來。")
    w("")
    w("### 2-4 Reference Element 會把「同一件衣服」整件複製")
    w("")
    w("B1 指定與錨點同一件炭灰高領毛衣 → 錨點那件衣服的**兩道窄露肩開口**原封不動跟著出現，")
    w("即使 prompt 明寫 `unbroken and continuous over both shoulders, a complete shoulder seam on each side`。")
    w("B2 指定完全不同的衣服 → 開口消失。")
    w("")
    w("**→ 指定同一件衣服時，錨點的版本會覆蓋 prompt；指定不同衣服時 prompt 才有效。**")
    w("")
    w("### 2-5 錨點的髮色細節蓋不掉")
    w("")
    w("candidate_03 左側髮際有一段銀灰挑染。c03 → B1 → B2 三張全部保留，")
    w("三次 prompt 都明寫「單一平染、任何一段都沒有較淺的部分」。**已經是身分的一部分。**")
    w("")
    w("---")
    w("")
    w("## §3 錨點與使用者已裁決的兩件事")
    w("")
    w("### 3-1 銀灰挑染：保留")
    w("")
    w("使用者裁決（2026-08-28）保留為 Nico 的造型。理由：美業從業者染這個完全合理，")
    w("而且三次明確指令都蓋不掉，重建錨點不保證做得掉。")
    w("")
    w("**因此 20 段 prompt 一律把它寫成刻意的挑染**，而不是每次徒勞地要求消除：")
    w("")
    w("> " + p['hair_color_en'])
    w("")
    w("### 3-2 outfit_01：採納你的意見，換成明顯不同的衣服")
    w("")
    w("`nico_outfit_01` 原本就是錨點圖身上那件炭灰高領羅紋針織。依 §2-4，20 張裡有 5 張用這件")
    w("（`a01`／`a02`／`a03`／`a07`／`c07`，其中 4 張是 clean anchor），那 5 張一定會帶出")
    w("錨點那兩道窄露肩開口。")
    w("")
    w("上一輪我的處置是把開口寫進衣櫃定義，讓文字與必然出圖一致。**你（C-41）指出那沒有處理**")
    w("**訓練目的**——高辨識度的開口出現在 4/8 clean anchor，容易與 identity 綁在一起，")
    w("正好違反 Soul 訓練「去服裝綁定」的目的；而 B2 已實測證明「明顯不同的衣服」可以保住臉")
    w("又服從換裝。**我採納你的意見**，改成顏色、織法、領型三者都與錨點不同的一件：")
    w("")
    w("> " + p['outfits']['nico_outfit_01']['en_layers']['top'])
    w("")
    w("### 3-3 身材設定變更")
    w("")
    w("使用者裁決把胸型由 C 放寬為 D（90-59-88）。原本的 `small natural bust with a shallow curve`")
    w("＋ `NOT heavy-chested` 與使用者偏好不符，而且那組否定詞正是把身形往平板推的原因。")
    w("")
    w("### 3-4 臉部骨架改版")
    w("")
    w("使用者看到第一輪出圖就指出「五官跟庫裡既有角色 rainie-hsu 太像」。")
    w("比對確認屬實——那是模型的預設美女臉。骨架改為**少女短臉型**：")
    w("下半臉短、下巴小而窄、額頭寬、雙頰圓潤、大而圓的眼睛、顴骨低、鼻短鼻頭微翹、人中短小嘴。")
    w("")
    w("**這一類判斷不在你的職責範圍**——它不是對錯問題而是「這個角色該長什麼樣」，")
    w("已列入 `review/README.md` 的「必須由使用者拍板」清單。列在這裡只是讓你知道背景。")
    w("")
    w("---")
    w("")
    w("## §4 這 20 段 prompt 是怎麼產生的")
    w("")
    w("**不是手寫的。** `tools/build_phase_c_prompts.py` 從 `pilot/nico_pilot.json` 的結構欄位組出來，")
    w("欄位改了 prompt 就跟著改。理由：R3 已經證實人工抄寫必然漂移。")
    w("")
    w("組裝順序（固定）：")
    w("")
    w("```")
    w("錨點引用 → 景別（下緣切在哪裡）→ 動作 → 身體朝向（正面特徵）→ 頭部角度 → 俯仰")
    w("→ 視線 → 表情 → 臉部遮擋 → 誰在拍 → 左手 → 右手 → 其他入鏡物件")
    w("→ 素顏/膚色 → 髮色＋髮型 → 服裝五層 → 場所 → 光線五段 → 相機 → 濾鏡與不完美 → 排除清單")
    w("```")
    w("")
    w("中文欄位（scene／手部註記／道具名／光線五段）有一層對應的英文，")
    w("存在 `pilot/phase_c_actions_en.json`。**這層中英對應正是 §6 第 2 題要請你核的。**")
    w("")
    w("服裝與髮型的英文已移進 `nico_pilot.json` 本身（原本放在 builder 裡，")
    w("那會構成第二份真理來源——也就是你 R1 開的 C-01 那個病）。")
    w("")
    w("---")
    w("")
    w("## §5 20 段 prompt 全文")
    w("")
    # 20 段裡逐字相同的樣板抽出來只印一次——這份檔案要控制體積（你上次讀 repo 燒掉 5 小時用量）
    # C-43：樣板代號原本依長度排序編號，每次重新產生都會變，導致覆核意見裡的編號對不上。
    # 改為語意固定的名稱。
    import collections as _c
    NAMED = [
        ("FACE-BARE",   lambda t: t.startswith("Her face is bare")),
        ("HAIR-COLOUR", lambda t: t.startswith(p['hair_color_en'][:40])),
        ("BODY",        lambda t: t.startswith("Her build") or t.startswith("Her frame is slight")),
        ("FRAME",       lambda t: t.startswith("The bottom edge of the picture")
                                  or t.startswith("The whole of her is inside")),
        ("FACING",      lambda t: t.startswith("The camera sees the front")
                                  or t.startswith("Her body is angled")
                                  or t.startswith("The camera is beside her")),
        ("HEAD",        lambda t: t.startswith("Her head is")),
        ("CAMERA",      lambda t: t.startswith("Shot on the")),
        ("CLOSED-SET",  lambda t: t.startswith("Real skin texture")),
        ("WHO-SHOOTS",  lambda t: t.startswith("Someone standing near her")
                                  or t.startswith("The picture is what her phone")
                                  or t.startswith("She is photographing her own reflection")),
    ]
    cnt = _c.Counter()
    for sh_ in S:
        for ln in pr[sh_['shot_id']].split("\n"):
            if len(ln) > 60: cnt[ln] += 1
    shared = {}
    seq = _c.Counter()
    for ln, n in sorted(cnt.items(), key=lambda kv: -len(kv[0])):
        if n < 3: continue
        for name, test in NAMED:
            if test(ln):
                seq[name] += 1
                shared[ln] = f"[[{name}-{seq[name]}]]"
                break
    w("**20 段裡重複出現的樣板**，抽出來只印一次；下面各段以 `[[名稱]]` 代替，")
    w("**實際送進模型時是完整文字**。這樣做只是為了控制這份檔案的體積。")
    w("（代號改為語意固定的名稱——上一輪用長度排序的流水號，每次重新產生都會變，")
    w("你 C-43 指出的 `[[S8]]`/`[[S5]]` 對不上就是這個原因。）")
    w("")
    for ln, tag in sorted(shared.items(), key=lambda kv: kv[1]):
        w(f"- `{tag}`（{cnt[ln]} 段共用）：{ln}")
    w("")
    w("下面每一段：左邊是該列的結構欄位（真理來源），右邊是產生出來的 prompt。")
    w("")
    for i, s in enumerate(S, 1):
        sid = s['shot_id']
        w(f"### {i}. `{sid}` — {s['purpose']}／{s['pillar']}")
        w("")
        w("| 欄位 | 值 |")
        w("|------|----|")
        w(f"| 中文 scene（真理來源）| **{s['scene']}** |")
        w(f"| framing / view | `{s['framing']}` / `{s['view']}` |")
        w(f"| head_yaw / pitch / gaze | `{s['head_yaw']}` / `{s['head_pitch']}` / `{s['eye_gaze']}` |")
        w(f"| body_pose / expression | `{s['body_pose']}` / `{s['expression']}` |")
        w(f"| face_visibility | `{s['face_visibility']}` |")
        w(f"| outfit / hair | `{s['outfit_id']}` / `{s['hair_id']}` |")
        w(f"| location（層級）| `{s['location']}`（{reg.get(s['location'])}）|")
        hl, hr = s['hands']['left'], s['hands']['right']
        w(f"| hands | L `{hl['state']}`{'→`'+hl['object_ref']+'`' if hl.get('object_ref') else ''}"
          f"（{hl['note']}）／ R `{hr['state']}`{'→`'+hr['object_ref']+'`' if hr.get('object_ref') else ''}"
          f"（{hr['note']}）|")
        w("| props | " + "；".join(f"`{q['id']}` {q['name']}（{q['relation']}・zone={q['zone']}）"
                                   for q in s['props']) + " |")
        lt = s['light']
        w(f"| light | `{lt['family']}`・bounce=`{lt['bounce_type']}` |")
        w(f"| filter / camera | `{s['filter']}` / `{s['camera']['type']}`・"
          f"distortion=`{s['camera']['distortion']}`・dof=`{s['camera']['depth_of_field']}` |")
        ip = s['imperfection_profile']
        w(f"| imperfection | composition=`{ip['composition']}`・motion=`{ip['motion']}`・"
          f"wb=`{ip['white_balance']}`・clutter=`{ip['background_clutter']}`・"
          f"highlight=`{ip['highlight_clipping']}` |")
        w("")
        w("```text")
        body = pr[sid]
        for c, tag in shared.items():
            body = body.replace(c, tag)
        w(body)
        w("```")
        w("")
    w("---")
    w("")
    w("## §6 本輪請你判斷")
    w("")
    w("### 6-1 上一輪（R13）你開的 C-50，已修")
    w("")
    w("**屬實。** 實測 `composition=slightly_tilted` 的三列中，`nico_c02` 與 `nico_c05`")
    w("同時含「場景垂直線平行畫面邊緣」與「地平線略歪」——相機有 roll 時這兩件事不可能同時成立。")
    w("（`nico_c08` 是鏡面自拍、鏡頭 distortion=mild，沒有那句，所以沒中招。）")
    w("")
    w("也謝謝你修正自己 R12 的措辭。已改為你這輪給的：")
    w("")
    w("> Straight rectilinear lens geometry: architectural lines render as straight segments with "
      "natural perspective.")
    w("")
    w("**lint 已加你要求的交叉檢查**：`composition=slightly_tilted` 時不得出現")
    w("`parallel to the frame edges` 或 `vertical lines stay vertical`。")
    w("反向測試：把衝突打回 `nico_c02`，lint 擋下。")
    w("")
    w("### 6-2 這一輪請你判斷")
    w("")
    w("**1. C-50 可否結案？連帶 C-44。**")
    w("")
    w("**2. 你指定要重看的 `CAMERA-1` 與 `nico_c02`／`nico_c05` 展開結果，都在 §5。**")
    w("")
    w("**3. 放行判定。** 你上一輪說「修正相機幾何句並確認 c02／c05 後，")
    w("   若沒有其他改動，即可結案 C-44 並放行 20 張生成」——本輪除了這一處，")
    w("   資料與模板都沒有其他改動。")
    w("")
    w("**現在 lint 擋的規則**（`tools/lint_prompts.py`，20/20 通過）：")
    w("否定詞為 0；姿態動詞與 body_pose 一致；身材必須是該 framing 的版本；")
    w("整段不得出現該 framing 裁切外的解剖名詞；face_closeup 不得提到軀幹；")
    w("兩手都在畫面外時不得出現「hand」；不得描述該景別看不見的服裝層；")
    w("戒指依手部可見性；裁切外的手不得描述；宣告不可見的道具不得出現；")
    w("**相機幾何句不得與 composition=slightly_tilted 互斥**；相機句不得假設室內；")
    w("戶外不得說光來自 room；不得出現第二個 person token；每段都要有正面封閉集合收尾。")
    w("")
    w("---")
    w("")
    w("## §7 你的回覆區")
    w("")
    w("把意見寫在下面這行以下。")
    w("")
    w(MARK)
    w("")
    return "\n".join(L)

if __name__ == '__main__':
    body = build()
    path = 'review/REVIEW_PHASE_C.md'
    replies = ""
    if os.path.exists(path):
        old = open(path, encoding='utf-8').read()
        if MARK in old: replies = old.split(MARK, 1)[1]
    open(path, 'w', encoding='utf-8').write(body + replies)
    print(f"已產生 {path}（{os.path.getsize(path)/1024:.1f} KB）")
    if replies.strip(): print(f"  已保留回覆區 {len(replies)} 字元")
