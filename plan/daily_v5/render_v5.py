# -*- coding: utf-8 -*-
"""把 v5 的 80 格規劃輸出成一頁可以直接在瀏覽器看的拍攝表。"""
import json, html, collections
from specs_data import SPECS

PROBE=set(json.load(open('probe16.json'))['ids'])
WHY=json.load(open('probe16.json'))['why']
NAME={"angel-chiu":"Angel Chiu 邱安晴","angeline-kwee":"Angeline Kwee 郭慧恩",
 "cheryl-soh":"Cheryl Soh 蘇思穎","emma-kao":"Emma Kao 高映真","jia-seo":"Jia Seo 徐지아",
 "miu-shiraishi":"Miu Shiraishi 白石美羽","peggy-lee":"Peggy Lee 李珮甄",
 "ruoruo-tang":"Ruoruo Tang 唐苡若","somi-oh":"Somi Oh 吳소미","sydney-leong":"Sydney Leong 梁欣妮",
 "tammy-chou":"Tammy Chou 周語彤","wanyin-jiang":"Wanyin Jiang 江晚吟",
 "wendy-yeo":"Wendy Yeo 楊薇伊","yerin-han":"Yerin Han 韓예린",
 "zhiyi-shen":"Zhiyi Shen 沈知意","zoey-yeh":"Zoey Yeh 葉芷妍"}
CITY={"angel-chiu":"台北","angeline-kwee":"雅加達","cheryl-soh":"新加坡","emma-kao":"台南",
 "jia-seo":"首爾江南","miu-shiraishi":"東京中目黑","peggy-lee":"吉隆坡","ruoruo-tang":"成都",
 "somi-oh":"釜山","sydney-leong":"檳城喬治市","tammy-chou":"台北五分埔","wanyin-jiang":"蘇州",
 "wendy-yeo":"新加坡丹戎巴葛","yerin-han":"首爾","zhiyi-shen":"上海陸家嘴","zoey-yeh":"宜蘭"}
def cat(s):
    f=s.get("flag")
    if f=="唯一的工作場域": return ("工作","work")
    if f=="房間以外": return ("外出","out")
    if f=="標誌性配額": return ("配額","quota")
    return ("私下","priv")

A=[(p,s) for p,d in SPECS.items() for s in d['slots']]
tot=len(A); day=sum(1 for _,s in A if s['time']=='day')
bath=sum(1 for _,s in A if s['fam']=='浴室'); ppl=sum(1 for _,s in A if s.get('ppl'))
E=html.escape

rows=[]
for pid,d in SPECS.items():
    body=[]
    for s in d['slots']:
        c,k=cat(s)
        pp=s.get('ppl')
        pt=(f"{pp['level']}·{pp['dist']}" if pp else "—")
        pr=' probe' if s['id'] in PROBE else ''
        why=f'<div class="why">探針理由：{E(WHY[s["id"]])}</div>' if s['id'] in PROBE else ''
        body.append(f'''<tr class="slot{pr}">
<td class="code">{E(s['id'])}</td>
<td><span class="chip {'day' if s['time']=='day' else 'night'}">{'日' if s['time']=='day' else '夜'}</span></td>
<td><span class="chip {k}">{c}</span></td>
<td class="fam">{E(s['fam'])}</td>
<td class="ev"><b>{E(s['ev'])}</b><div class="pl">{E(s['pl'])}</div>{why}</td>
<td class="meta">{E(s['pose'])}·{E(s['hand'])}<br><span class="dim">{E(s['view'])}·{E(s['topo'])}</span></td>
<td class="ppl">{E(pt)}</td></tr>''')
    rows.append(f'''<section class="p">
<h2><span class="nm">{E(NAME[pid])}</span><span class="city">{E(CITY[pid])}</span><span class="comp">{E(d['comp'])} · {E(d['rhythm'])}</span></h2>
<div class="tw"><table><thead><tr><th>格</th><th>時</th><th>類</th><th>場景族</th><th>事件與場域</th><th>姿勢 · 鏡位</th><th>路人</th></tr></thead>
<tbody>{''.join(body)}</tbody></table></div></section>''')

fam=collections.Counter(s['fam'] for _,s in A)
famrows=''.join(f'<li><span>{E(k)}</span><b>{v}</b></li>' for k,v in fam.most_common())

HTML=f'''<title>v5 拍攝表</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=IBM+Plex+Mono:wght@500;600&display=swap">
<style>
:root{{
 --bg:#F7F7F5; --card:#FFFFFF; --ink:#16171A; --mid:#5C5F66; --dim:#8A8E96;
 --rule:#E2E2DE; --accent:#C2410C; --day:#B45309; --dayb:#FEF3C7;
 --night:#334E86; --nightb:#DEE7F7; --work:#6D28D9; --workb:#EDE4FC;
 --out:#047857; --outb:#D6F0E6; --quota:#B91C1C; --quotab:#FBE0DE;
 --priv:#4B5563; --privb:#E9EAEC; --probe:#FFF8E6; --probel:#E8A317;
 --disp:"Saira Condensed",-apple-system,"Noto Sans TC",sans-serif;
 --body:"Newsreader",Georgia,"Noto Serif TC",serif;
 --mono:"IBM Plex Mono",ui-monospace,monospace;
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
 --bg:#101114; --card:#181A1E; --ink:#EDEDEA; --mid:#A2A6AE; --dim:#767A83;
 --rule:#2A2D33; --accent:#F97316; --day:#FBBF24; --dayb:#3A2E10;
 --night:#93B4F0; --nightb:#17233C; --work:#C4A6FB; --workb:#2A2140;
 --out:#5EC9A0; --outb:#0F2E25; --quota:#F8A5A0; --quotab:#3A1917;
 --priv:#B6BAC2; --privb:#26282D; --probe:#231D0E; --probel:#8A6A14;
}}}}
:root[data-theme="dark"]{{
 --bg:#101114; --card:#181A1E; --ink:#EDEDEA; --mid:#A2A6AE; --dim:#767A83;
 --rule:#2A2D33; --accent:#F97316; --day:#FBBF24; --dayb:#3A2E10;
 --night:#93B4F0; --nightb:#17233C; --work:#C4A6FB; --workb:#2A2140;
 --out:#5EC9A0; --outb:#0F2E25; --quota:#F8A5A0; --quotab:#3A1917;
 --priv:#B6BAC2; --privb:#26282D; --probe:#231D0E; --probel:#8A6A14;
}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--ink);font-family:var(--body);
 font-size:15px;line-height:1.55;padding:0 16px;padding-block:0 64px;
 max-width:1180px;margin:0 auto;-webkit-text-size-adjust:100%}}
h1,h2,h3,th,.chip,.code,.kpi b{{font-family:var(--disp)}}
header{{padding-block:40px 24px;border-bottom:2px solid var(--ink)}}
h1{{font-size:clamp(30px,5vw,46px);line-height:1.05;margin:0 0 10px;
 letter-spacing:.01em;text-wrap:balance;font-weight:700}}
.sub{{color:var(--mid);margin:0;max-width:62ch}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(128px,1fr));
 gap:1px;background:var(--rule);border:1px solid var(--rule);margin:26px 0 0}}
.kpi{{background:var(--card);padding:14px 14px 12px}}
.kpi b{{display:block;font-size:27px;line-height:1;font-weight:600}}
.kpi span{{display:block;font-size:12.5px;color:var(--dim);margin-top:5px}}
.kpi i{{font-style:normal;color:var(--accent);font-size:12.5px}}
.band{{margin:34px 0 0;padding:18px 20px;background:var(--card);
 border-left:3px solid var(--accent)}}
.band h3{{margin:0 0 10px;font-size:16px;letter-spacing:.04em;text-transform:uppercase}}
.deltas{{list-style:none;margin:0;padding:0;display:grid;
 grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:10px 26px}}
.deltas li{{display:flex;gap:10px;align-items:baseline;font-size:14px;
 border-bottom:1px dotted var(--rule);padding-bottom:7px}}
.deltas em{{font-style:normal;color:var(--mid);flex:1}}
.deltas .was{{font-family:var(--mono);color:var(--dim);text-decoration:line-through}}
.deltas .now{{font-family:var(--mono);color:var(--accent);font-weight:600}}
.famlist{{list-style:none;padding:0;margin:16px 0 0;display:flex;flex-wrap:wrap;gap:6px}}
.famlist li{{display:flex;gap:6px;align-items:baseline;background:var(--card);
 border:1px solid var(--rule);padding:3px 9px;font-size:13px}}
.famlist b{{font-family:var(--mono)}}
.p{{margin:38px 0 0;background:var(--card);border:1px solid var(--rule)}}
.p h2{{margin:0;padding:13px 16px;border-bottom:1px solid var(--rule);
 display:flex;flex-wrap:wrap;gap:10px;align-items:baseline;font-size:20px;font-weight:600}}
.nm{{letter-spacing:.01em}}
.city{{color:var(--dim);font-size:13.5px;font-family:var(--body)}}
.comp{{margin-left:auto;font-family:var(--mono);font-size:11.5px;color:var(--mid)}}
.tw{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:14px}}
th{{text-align:left;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;
 color:var(--dim);font-weight:600;padding:8px 10px;border-bottom:1px solid var(--rule);
 white-space:nowrap}}
td{{padding:10px;border-bottom:1px solid var(--rule);vertical-align:top}}
tr:last-child td{{border-bottom:0}}
.slot.probe{{background:var(--probe);box-shadow:inset 3px 0 0 var(--probel)}}
.code{{font-family:var(--mono);font-weight:600;font-size:13px;white-space:nowrap}}
.chip{{display:inline-block;padding:1px 8px;font-size:11.5px;font-weight:600;
 letter-spacing:.06em;white-space:nowrap}}
.day{{background:var(--dayb);color:var(--day)}} .night{{background:var(--nightb);color:var(--night)}}
.work{{background:var(--workb);color:var(--work)}} .out{{background:var(--outb);color:var(--out)}}
.quota{{background:var(--quotab);color:var(--quota)}} .priv{{background:var(--privb);color:var(--priv)}}
.fam{{white-space:nowrap;color:var(--mid);font-size:13px}}
.ev{{min-width:260px}} .ev b{{font-weight:600}}
.pl{{color:var(--mid);font-size:13px;margin-top:3px}}
.why{{margin-top:6px;font-size:12.5px;color:var(--probel);font-family:var(--mono)}}
.meta{{font-size:12.5px;color:var(--mid);white-space:nowrap}}
.dim{{color:var(--dim)}}
.ppl{{font-size:12.5px;color:var(--mid);white-space:nowrap}}
footer{{margin-top:44px;padding-top:18px;border-top:1px solid var(--rule);
 color:var(--dim);font-size:13px}}
@media(max-width:640px){{.ev{{min-width:180px}} .comp{{margin-left:0;width:100%}}}}
</style>
<header>
<h1>虛擬 KOL 日常拍攝表 v5</h1>
<p class="sub">十六位人設，八十格。每一格先有「只有她會發生的那個時刻」，場域、動作、服裝與光才從那個時刻長出來。
底色標黃的十六格是探針批次，通過之後才續拍其餘六十四格。</p>
<div class="kpis">
<div class="kpi"><b>{tot}</b><span>總格數 · 16 位各 5 格</span></div>
<div class="kpi"><b>{day} / {tot-day}</b><span>日 / 夜</span></div>
<div class="kpi"><b>{bath}</b><span>浴室格 <i>v4 是 16</i></span></div>
<div class="kpi"><b>{ppl}</b><span>有路人 <i>v4 是 0</i></span></div>
<div class="kpi"><b>16</b><span>探針 · 1.92 credits</span></div>
<div class="kpi"><b>9.6</b><span>全部拍完的總成本</span></div>
</div>
<div class="band">
<h3>v4 → v5 改了什麼</h3>
<ul class="deltas">
<li><em>每位都有一格浴室，13 位還在同一順位</em><span class="was">16/16</span><span class="now">6/80</span></li>
<li><em>完全沒有路人的格數</em><span class="was">80/80</span><span class="now">68/80</span></li>
<li><em>日夜比</em><span class="was">約 6:2</span><span class="now">40:40</span></li>
<li><em>膚質句違反已拍板的 D3</em><span class="was">7/16</span><span class="now">0/16</span></li>
<li><em>帶反射面卻沒有鏡面守則的格</em><span class="was">15</span><span class="now">0</span></li>
<li><em>守則與場景直接打架的格</em><span class="was">2</span><span class="now">0</span></li>
<li><em>每格守則字數</em><span class="was">約 60</span><span class="now">約 37</span></li>
<li><em>五格組成只有一種</em><span class="was">1 種</span><span class="now">6 種</span></li>
</ul>
<ul class="famlist">{famrows}</ul>
</div>
</header>
{''.join(rows)}
<footer>依 PERSONA_CANON.md 原則二，工作場域每位至多一格。<br>
每一格的動作、服裝、光、表情都可回溯到該位人設 character.md 的哪一句，出處寫在 <code>plan/daily_v5/specs/</code> 的中文規劃稿裡。</footer>
'''
open('v5_plan.html','w').write(HTML)
print("寫出 v5_plan.html", len(HTML), "bytes")
