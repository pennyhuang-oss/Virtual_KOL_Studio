#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 pilot/batch3_faces_v2.json 產生成一份可審閱的 HTML 規劃書。"""
import json, html, sys

DATA = json.load(open(sys.argv[1], encoding='utf-8'))
OUT  = sys.argv[2]
P    = DATA['personas']
AX   = DATA['axes']
B1   = set(DATA['batch1'])
ORDER = ([p for p in P if p in B1] + [p for p in P if p not in B1])
e = lambda s: html.escape(str(s if s is not None else ''))

# 這一輪要使用者裁決的事項
DECISIONS = [
 ("D1", "參考圖是真人照片", "flag",
  "ChatGPT 附的 15 張參考圖是真實女性的照片，其中幾張看起來是公眾人物。這些人設之後會以「真人」的身分出現在 Instagram 上，"
  "所以有一個實際風險：合成出來的臉可能與某個真實存在的人相似到被認出來。"
  "ChatGPT 的四來源拆件混合（臉型／眼眉／鼻／口各取一張）確實大幅降低這個風險，"
  "但 <b>ref_11 一張供給 5 位的臉型與下顎</b>，而臉型下顎正是身分的主要載體。"
  "我的建議：出圖後把候選臉與該張來源照並排比對，像到會被認出就換掉。這件事最後是你決定。"),
 ("D2", "FACE_EN 裡的檔名對模型是看不見的", "fix",
  "規劃寫成 <code>FACE_SHAPE_AND_JAW from ref_15</code>，但模型收到的只有四張圖，看不到檔名。"
  "查證過 <code>seedream_v4_5</code> 的介面：參考圖只有一個角色 <code>image_references</code>，沒有四個具名欄位。"
  "所以送出前必須把檔名改寫成位置指涉（第一張／第二張／第三張／第四張），並讓附圖順序與文字一致。"
  "這是我要做的修正，不需要你決定，但你要知道規劃原文不能照抄。"),
 ("D3", "同源參考圖過度集中", "flag",
  "ref_11 供給 5 位的臉型與下顎（emma／yerin／ruoruo／wendy／peggy），ref_01 供給 5 位的鼻子。"
  "這與「要長得不一樣」這個目的直接衝突。建議至少把臉型這一欄拆開，同一張最多供 2 位。"),
 ("D4", "分離規則實際上沒有約束到任何一組", "note",
  "ChatGPT 訂的規則是「同粗分群者細分軸至少差 3 條」。實際跑下來 19 位落在 19 個不同的粗分群，"
  "沒有任何兩人同群，所以那條規則一次都沒有生效。真正有意義的數字是兩兩之間 11 條軸的相異數："
  "最少 4 條、中位 9 條。最接近的三組是 miu↔sydney、tammy↔sydney、yerin↔peggy，各只差 4 條。"),
]
METHOD = [
 ("A0", "純臉選角", "每人 4 個候選。臉部與參考圖配置佔 prompt 約 80%，其餘只寫成年身分、既定髮色、素色圓領上衣、"
  "正面眼平視角、中性表情、均勻柔光、淺灰背景。<b>不寫職業、服裝、場景、道具、身材、濾鏡、相機。</b>只看骨相選人，不因妝髮選人。"),
 ("A1", "三角度複核", "選中的臉生成正面與左右各約 30 度的中性頭肩照，通過驗收才建立 Reference Element 錨點。"),
 ("A2", "帶進情境", "以錨點測一張職業場景照與一張全身照。臉漂掉就退回 A0 重選，<b>不用更多文字補丁硬救</b>。"),
]
ACCEPT = [
 "候選裁成 512×512、瞳孔水平、等比例、灰階、遮掉頭髮與服裝，只看臉。",
 "逐項核對 AXES 與 MARKERS：每張至少 4 個 MARKERS 成立，且同一角色 4 張中至少 3 張成立。",
 "把 19 位與既有 13 位混排成盲測表，隱藏 id、髮色、妝容、服裝。兩次獨立隨機排序中都要能把同一角色的三個角度歸在同組。",
 "同群內兩兩檢查：眼眶結構、眼距、鼻部量體、口部幾何、顎頦五項中至少 3 項有肉眼可量測的差異。只靠髮妝分辨即 FAIL。",
 "ArcFace 只當輔助：先用既有角色校準「同人最低相似度」與「異人最高相似度」，落在重疊區一律回人工盲測。",
 "任何角色回到「大上揚雙眼皮＋窄尖顎＋高顴＋厚唇」的預設臉組合，即使相似度工具通過也退回 A0。",
]

def card(pid):
    d = P[pid]; f = d['fixed']; c = d['closest']
    b1 = pid in B1
    axrows = "".join(
        f'<div class="ax"><dt>{e(k)}</dt><dd>{e(v)}</dd></div>'
        for k, v in d['axes'].items())
    refs = "".join(
        f'<li><span class="slot">{e(s.replace("_"," ").title())}</span>'
        f'<span class="refid">{e(r)}</span></li>'
        for s, r in d['refs'].items())
    marks = "".join(f'<li>{e(m)}</li>' for m in d['markers'])
    return f"""
<article class="persona" id="p-{e(pid)}" data-batch="{'1' if b1 else '2'}"
         data-search="{e(pid)} {e(f['display'])} {e(f['ethnicity'])} {e(d['archetype'])}">
  <header class="phead">
    <div class="pname">
      <h3>{e(f['display'])}</h3>
      <code class="pid">{e(pid)}</code>
    </div>
    <div class="pmeta">
      {'<span class="badge b1">第一批</span>' if b1 else '<span class="badge b2">第二批</span>'}
      <span class="who">{e(f['age'])} 歲 · {e(f['ethnicity'])}</span>
    </div>
  </header>
  <p class="arch"><span class="eyebrow">原型</span>{e(d['archetype'])}</p>
  <div class="split">
    <section class="fixed">
      <h4>不動的部分<span class="tag">你原本的設定</span></h4>
      <dl class="kv">
        <div><dt>身分</dt><dd>{e(f['public_face'].split(' — ')[0])}</dd></div>
        <div><dt>身材</dt><dd class="num">{e(f['height_cm'])}cm · {e(f['bust_cm'])}-{e(f['waist_cm'])}-{e(f['hip_cm'])} · {e(f['cup'])} 罩杯</dd></div>
        <div><dt>髮</dt><dd>{e(f['hair'])}</dd></div>
      </dl>
      <p class="dead"><span class="strike">舊 face_type（作廢）</span>{e(f['superseded_face_type'])}</p>
    </section>
    <section class="face">
      <h4>新的臉<span class="tag new">ChatGPT 規劃</span></h4>
      <dl class="axes">{axrows}</dl>
      <div class="two">
        <div>
          <h5>四張參考圖的分工</h5>
          <ul class="refs">{refs}</ul>
        </div>
        <div>
          <h5>辨識特徵</h5>
          <ul class="marks">{marks}</ul>
        </div>
      </div>
      <details>
        <summary>送進模型的英文原文</summary>
        <p class="en">{e(d['face_en'])}</p>
      </details>
      <p class="why"><span class="eyebrow">與誰最像</span>
        最接近 <b>{e(c['id'])}</b>，11 條軸差 <b class="num">{c['diff']}</b> 條，
        相同的是 {e('、'.join(c['same']))}。<br>{e(d['why_distinct'])}</p>
    </section>
  </div>
</article>"""

dec = "".join(
  f'<div class="dec {k}"><div class="dnum">{e(n)}</div>'
  f'<div><h4>{e(t)}</h4><p>{b}</p></div></div>'
  for n, t, k, b in DECISIONS)
meth = "".join(
  f'<li><code class="step">{e(s)}</code><b>{e(t)}</b><p>{b}</p></li>'
  for s, t, b in METHOD)
axtable = "".join(
  f'<tr><th>{e(k)}</th><td class="vals">{e(" / ".join(v["values"]))}</td>'
  f'<td class="why2">{e(v["why"])}</td></tr>' for k, v in AX.items())
acc = "".join(f'<li>{e(x)}</li>' for x in ACCEPT)

HTML = f"""<title>19 張臉的重做規劃</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700&family=Public+Sans:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;600&display=swap">
<style>
:root{{
  --paper:#e9e8e2; --card:#f4f3ef; --sunk:#dedcd4;
  --ink:#1b1b19; --muted:#6b6a62; --rule:#cbcac2;
  --accent:#1f4e79; --flag:#9c3226; --ok:#3d6b4a;
  --shadow:0 1px 0 rgba(27,27,25,.06);
}}
@media (prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    --paper:#141513; --card:#1d1f1c; --sunk:#262824;
    --ink:#e9e8e1; --muted:#9b9a90; --rule:#35372f;
    --accent:#8fb4d8; --flag:#dd8477; --ok:#84b391;
    --shadow:0 1px 0 rgba(0,0,0,.35);
  }}
}}
:root[data-theme="dark"]{{
  --paper:#141513; --card:#1d1f1c; --sunk:#262824;
  --ink:#e9e8e1; --muted:#9b9a90; --rule:#35372f;
  --accent:#8fb4d8; --flag:#dd8477; --ok:#84b391;
  --shadow:0 1px 0 rgba(0,0,0,.35);
}}
*{{box-sizing:border-box}}
body{{background:var(--paper);color:var(--ink);
  font:400 16px/1.6 "Public Sans","Helvetica Neue",Arial,"Noto Sans TC",sans-serif;
  -webkit-font-smoothing:antialiased;margin:0}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 24px 96px}}
h1,h2,h3,h4,h5{{font-family:Archivo,"Helvetica Neue",Arial,"Noto Sans TC",sans-serif;
  text-wrap:balance;margin:0}}
code,.num,.pid{{font-family:"IBM Plex Mono",ui-monospace,monospace;font-variant-numeric:tabular-nums}}

header.top{{border-bottom:2px solid var(--ink);padding:56px 0 20px;margin-bottom:36px}}
.eyebrow{{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:11px;
  letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-right:10px}}
h1{{font-size:clamp(30px,5vw,46px);font-weight:700;letter-spacing:-.02em;line-height:1.08;margin:10px 0 14px}}
.lede{{max-width:62ch;color:var(--muted);font-size:17px;margin:0}}
.stats{{display:flex;flex-wrap:wrap;gap:28px;margin-top:26px;padding-top:18px;border-top:1px solid var(--rule)}}
.stat b{{display:block;font-family:"IBM Plex Mono",monospace;font-size:24px;font-weight:600;
  font-variant-numeric:tabular-nums;line-height:1}}
.stat span{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}

section.blk{{margin:0 0 52px}}
h2{{font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:700;
  padding-bottom:8px;border-bottom:1px solid var(--rule);margin-bottom:22px}}

.dec{{display:grid;grid-template-columns:52px 1fr;gap:16px;padding:16px 18px;margin-bottom:12px;
  background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--muted);box-shadow:var(--shadow)}}
.dec.flag{{border-left-color:var(--flag)}}
.dec.fix{{border-left-color:var(--accent)}}
.dec.note{{border-left-color:var(--muted)}}
.dnum{{font-family:"IBM Plex Mono",monospace;font-weight:600;font-size:13px;color:var(--muted);padding-top:3px}}
.dec.flag .dnum{{color:var(--flag)}}
.dec.fix .dnum{{color:var(--accent)}}
.dec h4{{font-size:16px;margin-bottom:6px}}
.dec p{{margin:0;font-size:14.5px;color:var(--muted);max-width:70ch}}
.dec b{{color:var(--ink)}}
.dec code{{font-size:12.5px;background:var(--sunk);padding:1px 5px;border-radius:2px}}

ol.method{{list-style:none;padding:0;margin:0;display:grid;gap:2px}}
ol.method li{{background:var(--card);border:1px solid var(--rule);padding:14px 18px;
  display:grid;grid-template-columns:44px 1fr;gap:14px;align-items:baseline}}
.step{{font-weight:600;color:var(--accent);font-size:13px}}
ol.method b{{font-size:15px}}
ol.method p{{grid-column:2;margin:5px 0 0;font-size:14.5px;color:var(--muted);max-width:72ch}}

.scroller{{overflow-x:auto;border:1px solid var(--rule);background:var(--card)}}
table{{border-collapse:collapse;width:100%;font-size:13.5px;min-width:720px}}
th,td{{text-align:left;padding:9px 14px;border-bottom:1px solid var(--rule);vertical-align:top}}
tr:last-child th,tr:last-child td{{border-bottom:0}}
table th{{font-family:Archivo,sans-serif;font-weight:700;white-space:nowrap;width:104px}}
.vals{{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--accent);width:44%}}
.why2{{color:var(--muted)}}

.bar{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:20px;
  position:sticky;top:0;z-index:5;background:var(--paper);padding:12px 0;border-bottom:1px solid var(--rule)}}
.bar button{{font:600 12px/1 "IBM Plex Mono",monospace;letter-spacing:.06em;
  padding:8px 13px;border:1px solid var(--rule);background:var(--card);color:var(--muted);
  cursor:pointer;border-radius:2px}}
.bar button[aria-pressed="true"]{{background:var(--ink);color:var(--paper);border-color:var(--ink)}}
.bar button:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
.bar input{{flex:1;min-width:180px;font:400 14px/1 "Public Sans",sans-serif;padding:9px 12px;
  border:1px solid var(--rule);background:var(--card);color:var(--ink);border-radius:2px}}
.bar input:focus-visible{{outline:2px solid var(--accent);outline-offset:-1px}}
.count{{font:400 12px/1 "IBM Plex Mono",monospace;color:var(--muted)}}

.persona{{background:var(--card);border:1px solid var(--rule);margin-bottom:14px;
  padding:20px 22px;box-shadow:var(--shadow)}}
.phead{{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:baseline;justify-content:space-between;
  padding-bottom:12px;border-bottom:1px solid var(--rule)}}
.pname{{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}}
.pname h3{{font-size:21px;letter-spacing:-.01em}}
.pid{{font-size:12px;color:var(--muted)}}
.pmeta{{display:flex;gap:12px;align-items:center}}
.who{{font-size:13px;color:var(--muted)}}
.badge{{font:600 10.5px/1 "IBM Plex Mono",monospace;letter-spacing:.1em;padding:4px 8px;border-radius:2px}}
.badge.b1{{background:var(--accent);color:var(--card)}}
.badge.b2{{background:var(--sunk);color:var(--muted)}}
.arch{{margin:14px 0 18px;font-size:16.5px}}
.split{{display:grid;grid-template-columns:minmax(0,240px) minmax(0,1fr);gap:26px}}
@media (max-width:760px){{.split{{grid-template-columns:1fr}}}}
h4{{font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);
  margin-bottom:11px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}}
.tag{{font-family:"IBM Plex Mono",monospace;font-size:9.5px;letter-spacing:.06em;
  text-transform:none;padding:2px 6px;background:var(--sunk);border-radius:2px;color:var(--muted)}}
.tag.new{{background:var(--accent);color:var(--card)}}
h5{{font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:7px}}
dl.kv{{margin:0}}
dl.kv > div{{display:grid;grid-template-columns:40px 1fr;gap:10px;padding:5px 0;
  border-bottom:1px dotted var(--rule);font-size:13.5px}}
dl.kv dt{{color:var(--muted);font-size:11.5px;padding-top:2px}}
dl.kv dd{{margin:0}}
.dead{{margin:14px 0 0;font-size:12.5px;color:var(--muted);line-height:1.5}}
.strike{{display:block;font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.08em;
  text-transform:uppercase;text-decoration:line-through;margin-bottom:3px;color:var(--flag)}}
dl.axes{{display:grid;grid-template-columns:repeat(auto-fill,minmax(178px,1fr));gap:1px;
  margin:0 0 18px;background:var(--rule);border:1px solid var(--rule)}}
.ax{{background:var(--card);padding:7px 10px}}
.ax dt{{font-family:"IBM Plex Mono",monospace;font-size:9.5px;letter-spacing:.05em;color:var(--muted)}}
.ax dd{{margin:2px 0 0;font-size:13px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
@media (max-width:620px){{.two{{grid-template-columns:1fr}}}}
ul.refs,ul.marks{{list-style:none;padding:0;margin:0;font-size:13px}}
ul.refs li{{display:flex;justify-content:space-between;gap:10px;padding:4px 0;
  border-bottom:1px dotted var(--rule)}}
.slot{{color:var(--muted);font-size:11.5px}}
.refid{{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--accent);font-weight:600}}
ul.marks li{{padding:4px 0 4px 13px;position:relative;border-bottom:1px dotted var(--rule);color:var(--ink)}}
ul.marks li::before{{content:"";position:absolute;left:0;top:12px;width:5px;height:1px;background:var(--muted)}}
details{{margin:16px 0 0;border-top:1px solid var(--rule);padding-top:10px}}
summary{{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--muted);cursor:pointer}}
summary:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
.en{{font-size:13px;color:var(--muted);margin:9px 0 0;max-width:76ch;line-height:1.65}}
.why{{margin:16px 0 0;padding-top:12px;border-top:1px solid var(--rule);font-size:13.5px;color:var(--muted)}}
.why b{{color:var(--ink)}}
ol.acc{{padding-left:20px;margin:0;font-size:14.5px;color:var(--muted);max-width:74ch}}
ol.acc li{{margin-bottom:8px}}
ol.acc li::marker{{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--accent)}}
footer{{margin-top:56px;padding-top:20px;border-top:2px solid var(--ink);font-size:13.5px;color:var(--muted)}}
</style>

<div class="wrap">
<header class="top">
  <span class="eyebrow">Virtual KOL Studio · Batch 3</span>
  <h1>19 張臉的重做規劃</h1>
  <p class="lede">第一次選角的四張臉被判定「五官全部太像，只有髮型妝容服裝不一樣」。
  這一版的臉全部由 ChatGPT 重新規劃，舊的 <code>face_type</code> 一行形容詞全數作廢；
  身材、髮色、年齡、族裔、身分維持你原本的設定不動。</p>
  <div class="stats">
    <div class="stat"><b>19</b><span>待建模角色</span></div>
    <div class="stat"><b>11</b><span>骨相維度</span></div>
    <div class="stat"><b>15</b><span>參考圖</span></div>
    <div class="stat"><b>4</b><span>要你裁決</span></div>
    <div class="stat"><b>4–11</b><span>兩兩相異軸數</span></div>
  </div>
</header>

<section class="blk">
  <h2>先看這四件事</h2>
  {dec}
</section>

<section class="blk">
  <h2>方法：先鑄臉，後入戲</h2>
  <ol class="method">{meth}</ol>
</section>

<section class="blk">
  <h2>11 條骨相維度</h2>
  <div class="scroller"><table>{axtable}</table></div>
</section>

<section class="blk">
  <h2>19 位</h2>
  <div class="bar">
    <button type="button" data-f="all" aria-pressed="true">全部</button>
    <button type="button" data-f="1" aria-pressed="false">第一批 6 位</button>
    <button type="button" data-f="2" aria-pressed="false">其餘 13 位</button>
    <input type="search" id="q" placeholder="搜尋 id、族裔、原型…" aria-label="搜尋角色">
    <span class="count" id="count"></span>
  </div>
  {''.join(card(p) for p in ORDER)}
</section>

<section class="blk">
  <h2>出圖後怎麼驗收</h2>
  <ol class="acc">{acc}</ol>
</section>

<footer>
  臉的規劃來自 ChatGPT（<code>review/REVIEW_BATCH3_FACES.md</code> §10）。
  身材與人設沿用 <code>kols/*/profile.json</code>。
  本頁由 <code>tools/gen_faceplan_page.py</code> 從 <code>pilot/batch3_faces_v2.json</code> 產生。
</footer>
</div>

<script>
(function(){{
  var cards=[].slice.call(document.querySelectorAll('.persona'));
  var btns=[].slice.call(document.querySelectorAll('.bar button'));
  var q=document.getElementById('q'), count=document.getElementById('count'), f='all';
  function apply(){{
    var t=(q.value||'').trim().toLowerCase(), n=0;
    cards.forEach(function(c){{
      var okF = (f==='all') || c.dataset.batch===f;
      var okQ = !t || (c.dataset.search||'').toLowerCase().indexOf(t)>-1;
      var show = okF && okQ;
      c.hidden = !show;
      if(show) n++;
    }});
    count.textContent = n + ' / ' + cards.length;
  }}
  btns.forEach(function(b){{
    b.addEventListener('click',function(){{
      f=b.dataset.f;
      btns.forEach(function(x){{x.setAttribute('aria-pressed', String(x===b));}});
      apply();
    }});
  }});
  q.addEventListener('input',apply);
  apply();
}})();
</script>
"""
open(OUT, 'w', encoding='utf-8').write(HTML)
print(f'{OUT}  {len(HTML):,} 字元')
