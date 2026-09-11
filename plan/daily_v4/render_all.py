# -*- coding: utf-8 -*-
"""把 16 份 spec 渲染成一頁。每位人設的區塊用她自己的色盤上色 ——
這本身就是 v4 的論點：往下滑，每個人看起來都不一樣。"""
import json, glob, html, re

# 誰是亮底、誰是暗底 —— 依她檔案的「氛圍／後製」決定，不是我隨便配
THEME={"wendy-yeo":"dark","zhiyi-shen":"dark","peggy-lee":"dark","emma-kao":"dark",
       "wanyin-jiang":"dark","jia-seo":"dark","somi-oh":"dark","cheryl-soh":"dark",
       "angel-chiu":"dark",
       "zoey-yeh":"light","tammy-chou":"light","sydney-leong":"light",
       "miu-shiraishi":"light","ruoruo-tang":"light","angeline-kwee":"light",
       "yerin-han":"light"}
WHY={"dark":"她的檔案是低光／單一光源／夜間","light":"她的檔案是自然光／明亮／低對比"}

def lum(h):
    r,g,b=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    f=lambda c: c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4
    return .2126*f(r)+.7152*f(g)+.0722*f(b)
def mix(h,t,k):
    a=[int(h[i:i+2],16) for i in (1,3,5)]; b=[int(t[i:i+2],16) for i in (1,3,5)]
    return "#"+"".join(f"{round(x+(y-x)*k):02x}" for x,y in zip(a,b))

def theme_vars(pid, pal):
    cols=[c for _,c in pal]
    dark=min(cols,key=lum); light=max(cols,key=lum)
    accent=max(cols,key=lambda c: abs(lum(c)-.45))
    # accent 要在底色上看得見：挑飽和度高、亮度中段的那個
    def sat(h):
        r,g,b=[int(h[i:i+2],16) for i in (1,3,5)]
        return (max(r,g,b)-min(r,g,b))/255
    accent=max(cols,key=lambda c: sat(c)*(1-abs(lum(c)-.45)))
    if THEME[pid]=="dark":
        ground=mix(dark,"#000000",.55); sheet=mix(dark,"#000000",.35)
        ink=mix(light,"#ffffff",.25); dim=mix(ink,ground,.45)
        edge=mix(ground,ink,.18)
        if lum(accent)<.28: accent=mix(accent,"#ffffff",.4)
    else:
        ground=mix(light,"#ffffff",.5); sheet=mix(light,"#ffffff",.2)
        ink=mix(dark,"#000000",.45); dim=mix(ink,ground,.42)
        edge=mix(ground,ink,.16)
        if lum(accent)>.62: accent=mix(accent,"#000000",.35)
    return dict(ground=ground,sheet=sheet,ink=ink,dim=dim,edge=edge,accent=accent)

specs=[]
for f in sorted(glob.glob('specs/*.json')):
    specs.append(json.load(open(f)))
order=["wendy-yeo","zhiyi-shen","angel-chiu","emma-kao","cheryl-soh","peggy-lee","wanyin-jiang",
       "jia-seo","somi-oh","yerin-han","angeline-kwee","miu-shiraishi","ruoruo-tang",
       "sydney-leong","tammy-chou","zoey-yeh"]
specs.sort(key=lambda d: order.index(d["pid"]) if d["pid"] in order else 99)
SHORT={"wendy-yeo":5,"zhiyi-shen":5,"angel-chiu":3,"angeline-kwee":3,"somi-oh":3,"yerin-han":3,
       "zoey-yeh":3,"emma-kao":2,"peggy-lee":2,"sydney-leong":2,"tammy-chou":2,"wanyin-jiang":2,
       "cheryl-soh":1,"jia-seo":1,"miu-shiraishi":1,"ruoruo-tang":1}

H='''<title>16 位人設的量身定做規劃</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,600;1,6..96,400&family=Instrument+Sans:wght@400;500;600&family=Barlow+Semi+Condensed:wght@500;600&display=swap">
<style>
:root{
 --page:#121212; --pink:#EFECE6; --pdim:#8E8A83; --pedge:#2A2A2A;
 --disp:"Bodoni Moda",Georgia,"Songti TC",serif;
 --sans:"Instrument Sans",system-ui,"PingFang TC","Noto Sans TC",sans-serif;
 --cond:"Barlow Semi Condensed",var(--sans);
}
*{box-sizing:border-box}
body{background:var(--page);color:var(--pink);font-family:var(--sans);line-height:1.6;
 padding:0;margin:0}
.pad{padding-left:20px;padding-right:20px}
.wrap{max-width:960px;margin:0 auto}
.top{padding-block:46px 34px;border-bottom:1px solid var(--pedge)}
.eyebrow{font-family:var(--cond);font-size:13px;letter-spacing:.16em;text-transform:uppercase;
 color:var(--pdim);margin:0 0 10px}
h1{font-family:var(--disp);font-weight:600;font-size:clamp(30px,5.5vw,50px);line-height:1.06;
 margin:0 0 12px;text-wrap:balance}
.lead{font-size:15px;color:#C9C5BE;max-width:60ch;margin:0 0 22px}
.lead b{color:var(--pink)}
.rules{border-top:1px solid var(--pedge);padding-top:18px;margin-top:6px}
.rules h3{font-family:var(--cond);font-size:12px;letter-spacing:.14em;text-transform:uppercase;
 color:var(--pdim);margin:0 0 10px;font-weight:600}
.rules table{width:100%;border-collapse:collapse;font-size:13.5px}
.rules td{padding:6px 12px 6px 0;border-top:1px solid var(--pedge);vertical-align:top}
.rules td.k{font-family:var(--cond);white-space:nowrap;color:var(--pink)}
.rules td.v{color:#C9C5BE;font-family:var(--cond)}
.rules td.s{color:var(--pdim);font-size:12.5px}
.idx{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:1px;
 background:var(--pedge);border:1px solid var(--pedge);margin-top:26px}
.idx a{display:flex;align-items:center;gap:8px;background:var(--page);padding:9px 11px;
 text-decoration:none;font-family:var(--cond);font-size:13.5px;color:#C9C5BE}
.idx a:hover{color:var(--pink)}
.idx a .dots{display:flex;gap:2px;flex:0 0 auto}
.idx a i{width:7px;height:14px;border-radius:1px}
.idx a b{font-weight:500;color:inherit}
.idx a em{font-style:normal;color:var(--pdim);margin-left:auto;font-size:12.5px}

section.p{background:var(--ground);color:var(--ink);padding-block:44px 48px;
 border-top:1px solid var(--edge)}
section.p .num{font-family:var(--cond);font-size:12px;letter-spacing:.16em;text-transform:uppercase;
 color:var(--accent);margin:0 0 8px}
section.p h2{font-family:var(--disp);font-weight:600;font-size:clamp(26px,4.4vw,40px);
 line-height:1.07;margin:0 0 4px;text-wrap:balance}
section.p .meta{font-family:var(--cond);font-size:14px;color:var(--dim);margin:0 0 12px}
section.p .meta b{color:var(--accent);font-weight:600}
section.p .one{font-family:var(--disp);font-style:italic;font-size:17px;margin:0 0 22px;
 max-width:46ch;color:var(--ink)}
.canon{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));gap:0;
 border-top:1px solid var(--edge)}
.canon>div{padding:14px 18px 14px 0;border-right:1px solid var(--edge)}
.canon>div:last-child{border-right:0}
.canon h3{font-family:var(--cond);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;
 color:var(--dim);margin:0 0 6px;font-weight:600}
.canon p,.canon li{margin:0;font-size:13px;color:var(--ink);opacity:.88}
.sw{display:flex;gap:4px;margin:0 0 6px}
.sw i{width:24px;height:24px;border-radius:2px;border:1px solid rgba(128,128,128,.3)}
.sw-l{font-family:var(--cond);font-size:12px;color:var(--dim)}
ul.hab{list-style:none;margin:0;padding:0}
ul.hab li{padding-left:13px;position:relative;margin:2px 0;font-size:12.5px}
ul.hab li::before{content:"";position:absolute;left:0;top:.6em;width:5px;height:5px;
 background:var(--accent);border-radius:1px}
.pills{display:flex;flex-wrap:wrap;gap:6px;margin:18px 0 0}
.pills span{font-family:var(--cond);font-size:12.5px;border:1px solid var(--edge);
 border-radius:2px;padding:2px 8px;color:var(--ink);opacity:.85}
.pills span b{color:var(--accent);font-weight:600;opacity:1}
.alloc{margin-top:24px;border-top:1px solid var(--edge);padding-top:14px}
.alloc h3{font-family:var(--cond);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;
 color:var(--dim);margin:0 0 8px;font-weight:600}
.alloc .row{display:flex;gap:10px;font-family:var(--cond);font-size:13px;padding:2px 0}
.alloc .row b{color:var(--accent);font-weight:600;white-space:nowrap}
.alloc .row span{color:var(--ink);opacity:.8}
.shot{border-top:1px solid var(--edge);padding-block:22px}
.shot-head{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 13px;margin-bottom:13px}
.sid{font-family:var(--disp);font-size:26px;font-weight:600;color:var(--accent);line-height:1}
.spil{font-family:var(--cond);font-size:13.5px;color:var(--ink)}
.sw2{font-family:var(--cond);font-size:12.5px;color:var(--dim)}
.sflag{font-family:var(--cond);font-size:11.5px;border:1px solid var(--accent);color:var(--accent);
 border-radius:2px;padding:1px 7px}
dl{margin:0;display:grid;grid-template-columns:74px minmax(0,1fr);gap:0 14px}
dt{font-family:var(--cond);font-size:12.5px;color:var(--dim);padding-block:6px;
 border-top:1px solid var(--edge);opacity:.8}
dd{margin:0;padding-block:6px;border-top:1px solid var(--edge);font-size:14px}
dl>dt:first-of-type,dl>dt:first-of-type+dd{border-top:0}
.src{display:block;font-family:var(--cond);font-size:12px;color:var(--accent);margin-top:2px;opacity:.9}
.src::before{content:"← ";opacity:.6}
.cmp{margin-top:26px;border-top:1px solid var(--edge);padding-top:16px}
.cmp h3{font-family:var(--cond);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;
 color:var(--dim);margin:0 0 10px;font-weight:600}
.cmp table{width:100%;border-collapse:collapse;font-size:13px}
.cmp td{padding:7px 12px 7px 0;border-top:1px solid var(--edge);vertical-align:top}
.cmp td.k{font-family:var(--cond);white-space:nowrap;color:var(--ink)}
.cmp td.a{color:var(--dim)}
.cmp td.b{color:var(--ink)}
.tw{overflow-x:auto}
.foot{padding-block:34px 70px;border-top:1px solid var(--pedge);color:var(--pdim);font-size:13.5px}
@media(max-width:620px){
 dl{grid-template-columns:1fr;gap:0}
 dt{padding-bottom:0} dd{border-top:0;padding-top:1px}
 .canon>div{border-right:0;border-bottom:1px solid var(--edge);padding-right:0}
}
</style>
'''
def esc(s): return html.escape(s) if s else ""
B=[]
B.append('<div class="pad"><div class="wrap"><div class="top">'
 '<p class="eyebrow">daily_v4 · 每位人設量身定做</p>'
 '<h1>16 位人設，16 份不一樣的規劃</h1>'
 '<p class="lead">v2 與 v3 都是從共用池抽零件再加「不准重複」的限制，所以 20 位併排看還是像同一組攝影師的作品。'
 'v4 改成每位人設從她<b>自己的 Character Bible</b> 長出來 —— 色盤、氛圍、後製、支柱比重、標誌性配額、小習慣、語氣，'
 '全部是她檔案裡本來就寫好的，而 v2／v3 一筆都沒讀。每一格設定後面都標了出處。'
 '<b>連每位人設的區塊配色都用她自己的色盤</b>，往下滑就看得出差別。</p>'
 '<div class="rules"><h3>場域配額（硬規則，全 16 位共用）</h3><table><tbody>'
 '<tr><td class="k">工作場域</td><td class="v">最多 1 格（20%）</td><td class="s">憲章原則二：高辨識度場景不得成為主支柱、不得超過 25%</td></tr>'
 '<tr><td class="k">她自己的空間</td><td class="v">3 格以上（60%）</td><td class="s">canon 私下類合計 45–50%，是最大支柱</td></tr>'
 '<tr><td class="k">房間以外、非工作</td><td class="v">最多 1 格（20%）</td><td class="s">content_style：讓她有房間以外的地方可以去</td></tr>'
 '<tr><td class="k">標誌性配額</td><td class="v">最多 1 格</td><td class="s">憲章原則二的期數配額，不得寫成人設基調</td></tr>'
 '<tr><td class="k">跨人設</td><td class="v">80 格、80 個場域</td><td class="s">零重複，也與 v2 的 100 格零重疊</td></tr>'
 '</tbody></table></div>')
B.append('<div class="idx">')
for i,d in enumerate(specs,1):
    tv=theme_vars(d["pid"],d["palette"])
    dots=''.join(f'<i style="background:{c}"></i>' for _,c in d["palette"])
    B.append(f'<a href="#{d["pid"]}"><span class="dots">{dots}</span>'
             f'<b>{esc(d["name"].split()[0])}</b><em>缺 {SHORT[d["pid"]]}</em></a>')
B.append('</div></div></div>')

for i,d in enumerate(specs,1):
    v=theme_vars(d["pid"],d["palette"])
    style=";".join(f"--{k}:{x}" for k,x in v.items())
    B.append(f'<section class="p" id="{d["pid"]}" style="{style}"><div class="pad"><div class="wrap">')
    B.append(f'<p class="num">{i:02d} / 16 · {esc(d["city"])} · 本輪要補 {SHORT[d["pid"]]} 格 · 區塊配色 {WHY[THEME[d["pid"]]]}</p>')
    B.append(f'<h2>{esc(d["name"])}</h2>')
    B.append(f'<p class="meta"><b>{esc(d["handle"])}</b> · {esc(d["bio"])} · {esc(d["job"])}</p>')
    B.append(f'<p class="one">{esc(d["oneline"])}</p>')
    B.append('<div class="canon"><div><h3>色盤</h3><div class="sw">'
        +''.join(f'<i style="background:{c}"></i>' for _,c in d["palette"])
        +'</div><p class="sw-l">'+' · '.join(n for n,_ in d["palette"])+'</p></div>'
        +f'<div><h3>氛圍</h3><p>{esc(d["mood"])}</p></div>'
        +f'<div><h3>後製</h3><p>{esc(d["post"])}</p></div>'
        +f'<div><h3>語氣</h3><p>{esc(d["tone"])}</p></div></div>')
    B.append('<div class="canon" style="border-top:0"><div style="grid-column:span 2">'
        '<h3>小習慣 — 招牌鏡頭的來源</h3><ul class="hab">'
        +''.join(f'<li>{esc(h)}</li>' for h in d["habits"])
        +f'</ul></div><div><h3>標誌性配額</h3><p>{esc(d["quota"])}</p></div></div>')
    B.append('<div class="pills">'+''.join(f'<span>{esc(n)} <b>{w}</b></span>' for n,w in d["pillars"])+'</div>')
    work=sum(1 for s in d["slots"] if s.get("flag") and "唯一的工作場域" in s["flag"])
    out =sum(1 for s in d["slots"] if s.get("flag") and "房間以外" in s["flag"])
    B.append('<div class="alloc"><h3>她這 5 格的場域分布</h3>'
      f'<div class="row"><b>{5-work-out} 格</b><span>她自己的空間</span></div>'
      f'<div class="row"><b>{work} 格</b><span>工作場域{"（她的職業支柱只有 20%，這輪不碰）" if work==0 else ""}</span></div>'
      f'<div class="row"><b>{out} 格</b><span>房間以外、非工作場所</span></div></div>')
    for s in d["slots"]:
        B.append('<div class="shot"><div class="shot-head">'
          f'<span class="sid">{s["id"]}</span><span class="spil">{esc(s["pillar"])}</span>'
          f'<span class="sw2">支柱 {s["weight"]}</span>'
          +(f'<span class="sflag">{esc(s["flag"])}</span>' if s.get("flag") else '')
          +'</div><dl>'
          f'<dt>場域</dt><dd>{esc(s["place"])}</dd>'
          f'<dt>動作</dt><dd>{esc(s["action"])}<span class="src">{esc(s["action_src"])}</span></dd>'
          f'<dt>服裝</dt><dd>{esc(s["outfit"])}<span class="src">{esc(s["outfit_src"])}</span></dd>'
          f'<dt>光</dt><dd>{esc(s["light"])}<span class="src">{esc(s["light_src"])}</span></dd>'
          f'<dt>表情</dt><dd>{esc(s["face"])}<span class="src">{esc(s["face_src"])}</span></dd>'
          f'<dt>路人</dt><dd>{esc(s["people"])}</dd></dl></div>')
    B.append('<div class="cmp"><h3>跟 v3 差在哪</h3><div class="tw"><table><tbody>'
      +''.join(f'<tr><td class="k">{esc(k)}</td><td class="a">{esc(a)}</td><td class="b">{esc(b)}</td></tr>'
               for k,a,b in d["v3_vs_v4"])
      +'</tbody></table></div></div>')
    B.append('</div></div></section>')

B.append('<div class="pad"><div class="wrap"><div class="foot">'
 '16 位 × 5 格 = 80 格，80 個場域零重複，且與 v2 的 100 格零重疊。'
 '每一格的動作都來自該人設自己的小習慣，光與後製來自她自己的「視覺美學」段，'
 '服裝收在她自己的色盤內，表情走她自己的語氣。'
 '本輪要補的是其中 39 格（每位人設補到 5 張）。稽核見 <code>plan/daily_v4/validate_v4.py</code>。'
 '</div></div></div>')
open('/tmp/claude-0/-home-user-Virtual-KOL-Studio/126351a3-5eb7-5c02-aa1a-1fadb58568b1/scratchpad/v4_all.html','w').write(H+"".join(B))
print("ok")
