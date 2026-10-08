# -*- coding: utf-8 -*-
"""把一位人設的量身定做規劃算成網頁。頁面配色直接用她自己的色盤 ——
這本身就是 v4 的論點：每位人設有自己的樣子，連她的規劃頁都不該長得一樣。"""
import json, html, sys

d = json.load(open(sys.argv[1] if len(sys.argv)>1 else 'sample_wendy.json'))
P = dict(d["palette"])
amber, green, brass, wood, black = (P["琥珀"], P["深綠"], P["黃銅"], P["暗木"], P["黑"])

H = f'''<title>Wendy Yeo 拍攝規劃</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,600;1,6..96,400&family=Instrument+Sans:wght@400;500;600&family=Barlow+Semi+Condensed:wght@500;600&display=swap">
<style>
:root{{
 --black:{black}; --wood:{wood}; --brass:{brass}; --amber:{amber}; --green:{green};
 --ground:#17110C; --sheet:#211A13; --edge:#3A2C1F; --ink:#EFE6D8; --dim:#A08D74;
 --disp:"Bodoni Moda",Georgia,"Songti TC",serif;
 --sans:"Instrument Sans",system-ui,"PingFang TC","Noto Sans TC",sans-serif;
 --cond:"Barlow Semi Condensed",var(--sans);
}}
*{{box-sizing:border-box}}
body{{background:var(--ground);color:var(--ink);font-family:var(--sans);line-height:1.6;
 padding-block:0;padding-left:20px;padding-right:20px}}
.wrap{{max-width:940px;margin:0 auto}}

header{{padding-block:46px 0;border-bottom:1px solid var(--edge)}}
.eyebrow{{font-family:var(--cond);font-size:13px;letter-spacing:.16em;text-transform:uppercase;
 color:var(--amber);margin:0 0 10px}}
h1{{font-family:var(--disp);font-weight:600;font-size:clamp(32px,6vw,56px);line-height:1.05;
 margin:0 0 4px;letter-spacing:-.01em;text-wrap:balance}}
.handle{{font-family:var(--cond);font-size:15px;color:var(--dim);margin:0 0 14px}}
.handle b{{color:var(--brass);font-weight:600}}
.oneline{{font-family:var(--disp);font-style:italic;font-size:clamp(16px,2.2vw,20px);
 color:#DCCDB4;max-width:44ch;margin:0 0 26px}}

.canon{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0;
 border-top:1px solid var(--edge);margin-top:30px}}
.canon>div{{padding:16px 18px 16px 0;border-right:1px solid var(--edge)}}
.canon>div:last-child{{border-right:0}}
.canon h3{{font-family:var(--cond);font-size:12px;letter-spacing:.14em;text-transform:uppercase;
 color:var(--dim);margin:0 0 7px;font-weight:600}}
.canon p{{margin:0;font-size:13.5px;color:#DCCDB4}}
.sw{{display:flex;gap:5px;margin:0 0 6px}}
.sw i{{width:26px;height:26px;border-radius:2px;border:1px solid rgba(255,255,255,.14)}}
.sw-label{{font-family:var(--cond);font-size:12px;color:var(--dim)}}
ul.hab{{list-style:none;margin:0;padding:0;font-size:13px;color:#DCCDB4}}
ul.hab li{{padding-left:14px;position:relative;margin:2px 0}}
ul.hab li::before{{content:"";position:absolute;left:0;top:.62em;width:5px;height:5px;
 background:var(--amber);border-radius:1px}}

.pill-row{{display:flex;flex-wrap:wrap;gap:7px;margin:24px 0 0}}
.pill-row span{{font-family:var(--cond);font-size:13px;border:1px solid var(--edge);
 border-radius:2px;padding:3px 9px;color:#DCCDB4}}
.pill-row span b{{color:var(--amber);font-weight:600}}

h2.sec{{font-family:var(--disp);font-weight:600;font-size:26px;margin:52px 0 4px}}
.sec-note{{font-size:13.5px;color:var(--dim);margin:0 0 22px;max-width:60ch}}

.shot{{border-top:1px solid var(--edge);padding-block:26px}}
.shot:last-of-type{{border-bottom:1px solid var(--edge)}}
.shot-head{{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px 14px;margin-bottom:16px}}
.shot-id{{font-family:var(--disp);font-size:30px;font-weight:600;color:var(--amber);
 line-height:1;font-variant-numeric:tabular-nums}}
.shot-pillar{{font-family:var(--cond);font-size:14px;color:var(--ink)}}
.shot-w{{font-family:var(--cond);font-size:13px;color:var(--dim)}}
.shot-flag{{font-family:var(--cond);font-size:12px;background:var(--green);color:#E6F0E8;
 border-radius:2px;padding:2px 8px}}
dl{{margin:0;display:grid;grid-template-columns:82px minmax(0,1fr);gap:0 16px}}
dt{{font-family:var(--cond);font-size:13px;color:var(--dim);padding-block:7px;
 border-top:1px solid rgba(58,44,31,.6)}}
dd{{margin:0;padding-block:7px;border-top:1px solid rgba(58,44,31,.6);font-size:14.5px}}
dl>dt:first-of-type,dl>dt:first-of-type+dd{{border-top:0}}
.src{{display:block;font-family:var(--cond);font-size:12.5px;color:var(--brass);margin-top:3px}}
.src::before{{content:"← ";opacity:.65}}

table{{width:100%;border-collapse:collapse;font-size:13.5px}}
th,td{{text-align:left;vertical-align:top;padding:9px 12px 9px 0;border-top:1px solid var(--edge)}}
th{{font-family:var(--cond);font-size:12px;letter-spacing:.1em;text-transform:uppercase;
 color:var(--dim);font-weight:600}}
td.k{{font-family:var(--cond);color:var(--ink);white-space:nowrap}}
td.old{{color:#9E8C74}}
td.new{{color:#EFE6D8}}
.tw{{overflow-x:auto}}
.close{{border-top:1px solid var(--edge);margin-top:40px;padding-block:24px 70px;
 font-family:var(--disp);font-style:italic;font-size:17px;color:#DCCDB4;max-width:52ch}}
@media(max-width:620px){{
 dl{{grid-template-columns:1fr;gap:0}}
 dt{{padding-bottom:0;border-top:1px solid rgba(58,44,31,.6)}}
 dd{{border-top:0;padding-top:2px}}
 .canon>div{{border-right:0;border-bottom:1px solid var(--edge);padding-right:0}}
}}
</style>
'''

def esc(s): return html.escape(s) if s else ""

B=[f'''<div class="wrap"><header>
<p class="eyebrow">量身定做樣本 · daily_v4</p>
<h1>{esc(d["name"])}</h1>
<p class="handle"><b>{esc(d["handle"])}</b> · {esc(d["bio"])} · {esc(d["city"])} · {esc(d["job"])}</p>
<p class="oneline">{esc(d["oneline"])}</p>
<div class="canon">
 <div><h3>色盤</h3><div class="sw">'''
+''.join(f'<i style="background:{c}"></i>' for _,c in d["palette"])
+'</div><p class="sw-label">'+' · '.join(n for n,_ in d["palette"])+'</p></div>'
+f'''<div><h3>氛圍</h3><p>{esc(d["mood"])}</p></div>
 <div><h3>後製</h3><p>{esc(d["post"])}</p></div>
 <div><h3>語氣</h3><p>{esc(d["tone"])}</p></div>
</div>
<div class="canon" style="border-top:0">
 <div style="grid-column:span 2"><h3>小習慣 — 招牌鏡頭的來源</h3><ul class="hab">'''
+''.join(f'<li>{esc(h)}</li>' for h in d["habits"])
+f'''</ul></div>
 <div><h3>標誌性配額（憲章原則二）</h3><p>{esc(d["quota"])}</p></div>
</div>
<div class="pill-row">'''
+''.join(f'<span>{esc(n)} <b>{w}</b></span>' for n,w in d["pillars"])
+'''</div>
<p class="sec-note" style="margin-top:18px">以上全部抄自 <code>kols/wendy-yeo/character.md</code>、
<code>content_style.md</code>、<code>profile.json</code>。daily_v2 與 v3 一筆都沒讀。</p>
</header>

<h2 class="sec">場域配額</h2>
<p class="sec-note">先前的版本把「支柱」當成「場域」在排，5 格裡有 3 格在吧檯或店門口＝60%，
違反憲章原則二（高辨識度場景不得成為主支柱、不得超過 25%）。改成硬規則：</p>
<div class="tw"><table><thead><tr><th>場域</th><th>格數</th><th>依據</th></tr></thead><tbody>'''
+''.join(f'<tr><td class="k">{esc(a)}</td><td class="new">{esc(b)}</td><td class="old">{esc(c)}</td></tr>'
         for a,b,c in d["alloc_rule"])
+'''</tbody></table></div>

<h2 class="sec">她的五格</h2>
<p class="sec-note">每一項設定後面標的是它的出處。</p>''']

for s in d["slots"]:
    B.append(f'''<div class="shot"><div class="shot-head">
<span class="shot-id">{s["id"]}</span>
<span class="shot-pillar">{esc(s["pillar"])}</span>
<span class="shot-w">支柱 {s["weight"]}</span>
{f'<span class="shot-flag">{esc(s["flag"])}</span>' if s["flag"] else ''}
</div>
<dl>
<dt>場域</dt><dd>{esc(s["place"])}</dd>
<dt>動作</dt><dd>{esc(s["action"])}<span class="src">{esc(s["action_src"])}</span></dd>
<dt>服裝</dt><dd>{esc(s["outfit"])}<span class="src">{esc(s["outfit_src"])}</span></dd>
<dt>光</dt><dd>{esc(s["light"])}<span class="src">{esc(s["light_src"])}</span></dd>
<dt>表情</dt><dd>{esc(s["face"])}<span class="src">{esc(s["face_src"])}</span></dd>
<dt>路人</dt><dd>{esc(s["people"])}</dd>
</dl></div>''')

B.append('''<h2 class="sec">跟 v3 差在哪</h2>
<p class="sec-note">同質性不是靠「詞庫夠大 ＋ 不准重複」解決的。20 位人設併排看會像同一組，
是因為她們本來就是從同一個池子抽的。</p>
<div class="tw"><table><thead><tr><th></th><th>v3 給 wendy 的</th><th>v4</th></tr></thead><tbody>'''
+''.join(f'<tr><td class="k">{esc(k)}</td><td class="old">{esc(a)}</td><td class="new">{esc(b)}</td></tr>'
         for k,a,b in d["v3_vs_v4"])
+'''</tbody></table></div>
<p class="close">v4 的全域限制只剩一條：跨人設不得撞場域、撞動作。
光不再有全域規則 —— 由每個人自己的「視覺美學」段決定，
所以 zoey 會是低對比、顆粒、不修膚質，somi 會是高飽和暖調，
跟 wendy 的低光高對比完全不是同一件事。</p>
</div>''')

open('/tmp/claude-0/-home-user-Virtual-KOL-Studio/126351a3-5eb7-5c02-aa1a-1fadb58568b1/scratchpad/v4_wendy.html','w').write(H+"".join(B))
print("ok")
