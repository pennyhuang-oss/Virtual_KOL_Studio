#!/usr/bin/env node
/**
 * 從 catalog.json ＋ assets/ 產生靜態頁面 → catalog/public/
 *
 * 內容依據只有使用者說的那四件事（見覆核包 §2.2）：
 *   1 設定是什麼  2 有哪些素材  3 細節到什麼程度  4 大概的營運數據
 * 🛑 不輸出任何狀態、handle、三圍、prompt／模型／credits、營運統計期間。
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';

const DIR = path.join(import.meta.dirname, '..');
const PUB = path.join(DIR, 'public');
const cat = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'catalog.json'), 'utf8'));
// 🛑 首頁與報價頁的文字全部來自 pitch.json（對外報價 PPT 逐字匯入），不要在這支程式裡編字。
// 那份 PPT 的數字、價格、方案內容是業務承諾（覆核包 §12.6）。
// ⚠ 案例段落渲染的是 `why_public` 不是 `why`：使用者 2026-09-03 裁決 PP-06
//   「改寫得模糊一點再放」，`why` 留逐字原文存查。
const pitch = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'pitch.json'), 'utf8'));
const copy  = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'copy.json'), 'utf8'));

const esc = s => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const CAT_LABEL = {
  travel_culture: '旅遊・城市文化', digital_culture: '數位娛樂・科技', outdoor_adventure: '戶外・登山',
  knowledge_culture: '知識・規則研究', beauty: '美妝・保養', nightlife: '夜生活', lifestyle: '生活風格',
  fitness: '健身', gaming: '遊戲・實況', wellness: '身心健康', 'luxury lifestyle': '精品生活',
  mythology_immersion: '神話沉浸', history_immersion: '歷史沉浸', null: '其他',
};
const catLabel = c => CAT_LABEL[c] || c || '其他';

// 語言標準化：只留語言名，不留熟練度括號
const langShort = s => String(s).replace(/\s*[（(].*?[)）]\s*/g, '').replace(/\s*—.*$/, '').trim();

// 地區歸成市場（篩選器用，依 Q2 把語言與地區合併成「市場」）
function market(loc = '') {
  const l = String(loc);
  if (/Taiwan|台北|台中|高雄|新竹|台灣/i.test(l)) return '台灣';
  if (/Singapore|新加坡|丹戎巴葛/i.test(l)) return '新加坡';
  if (/Malaysia|Kuala Lumpur/i.test(l)) return '馬來西亞';
  if (/Japan|Kyoto|Tokyo|京都/i.test(l)) return '日本';
  if (/Korea|Seoul|首爾/i.test(l)) return '韓國';
  if (/India|Mumbai/i.test(l)) return '印度';
  if (/France|Paris/i.test(l)) return '法國';
  if (/California|Los Angeles|LA\b/i.test(l)) return '美國';
  return '跨區';
}

// 🛑 素材網址一定要帶內容雜湊。
// 2026-09-03 踩到：伺服器對 /assets/ 送 `max-age=604800`（七天），
// 而 `hero.jpg` 這種網址是固定的、內容卻會換。換完圖之後使用者的瀏覽器
// 七天內都拿自己的舊快取，看到的還是舊封面——而且**客戶也會遇到同一件事**，
// 那不是「叫他重新整理」能解決的。
// → 網址後面接 `?v=<內容雜湊>`：內容一變網址就變，快取自然失效，
//   而沒變的檔案仍然享有七天快取。
const vtag = (abs) => {
  try {
    const h = crypto.createHash('md5').update(fs.readFileSync(abs)).digest('hex').slice(0, 10);
    return '?v=' + h;
  } catch { return ''; }
};

const assetsOf = id => {
  const d = path.join(DIR, 'assets', id);
  let files = []; try { files = fs.readdirSync(d); } catch {}
  const gal = files.filter(f => /^g\d+\.jpg$/.test(f)).sort();
  const u = f => `/assets/${id}/${f}` + vtag(path.join(d, f));
  return {
    hero: files.includes('hero.jpg') ? u('hero.jpg') : (gal[0] ? u(gal[0]) : null),
    gallery: gal.map(f => ({ web: u(f), thumb: u(f.replace('.jpg', '_t.jpg')) })),
    posters: files.filter(f => /_poster\.jpg$/.test(f)).sort().map(u),
  };
};

const CSS = `
:root{
  --bg:#0b0b0d; --bg2:#131317; --line:#26262c; --line2:#34343c;
  --ink:#f2f2f4; --ink2:#a8a8b3; --ink3:#6f6f7c;
  --accent:#c9a227; --accent2:#e8c85a;
  --serif:"Noto Serif TC",Georgia,"Songti TC",serif;
  --sans:"Noto Sans TC",-apple-system,"Segoe UI","PingFang TC","Microsoft JhengHei",sans-serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
  -webkit-font-smoothing:antialiased;line-height:1.7}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
.wrap{max-width:1240px;margin:0 auto;padding:0 24px}

/* ── 頁首 ── */
.top{border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50;
  background:rgba(11,11,13,.88);backdrop-filter:blur(14px)}
.top .wrap{display:flex;align-items:center;gap:20px;height:64px}
.brand{font-family:var(--serif);font-size:19px;letter-spacing:.06em}
.brand b{color:var(--accent2);font-weight:600}
.top nav{margin-left:auto;display:flex;gap:22px;font-size:13px;color:var(--ink2)}
.top nav a:hover{color:var(--ink)}

/* ── 開場 ── */
.hero{padding:96px 0 56px;border-bottom:1px solid var(--line)}
.hero h1{font-family:var(--serif);font-size:clamp(34px,5.4vw,60px);line-height:1.18;margin:0 0 22px;
  font-weight:500;letter-spacing:.01em}
.hero h1 em{font-style:normal;color:var(--accent2)}
.hero .lede{max-width:660px;color:var(--ink2);font-size:16.5px;margin:0 0 30px}
.stats{display:flex;flex-wrap:wrap;gap:0;border:1px solid var(--line);border-radius:3px;overflow:hidden;max-width:760px}
.stat{flex:1 1 150px;padding:18px 22px;border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.stat b{display:block;font-family:var(--serif);font-size:30px;color:var(--accent2);line-height:1.1}
.stat span{font-size:12px;color:var(--ink3);letter-spacing:.08em}

/* ── AI 揭露（首屏，CC-04）── */
.disclose{margin-top:34px;border-left:2px solid var(--accent);background:var(--bg2);
  padding:16px 20px;max-width:760px;border-radius:0 3px 3px 0}
.disclose b{color:var(--accent2);font-weight:600}
.disclose p{margin:6px 0 0;color:var(--ink2);font-size:13.5px}

/* ── 篩選 ── */
.filters{padding:30px 0 8px;position:sticky;top:64px;background:var(--bg);z-index:40;
  border-bottom:1px solid var(--line)}
.frow{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin-bottom:12px}
.frow>span{font-size:11px;color:var(--ink3);letter-spacing:.12em;min-width:52px}
.chip{border:1px solid var(--line2);background:transparent;color:var(--ink2);
  padding:5px 13px;border-radius:100px;font-size:12.5px;cursor:pointer;font-family:inherit;
  transition:.16s}
.chip:hover{border-color:var(--ink3);color:var(--ink)}
.chip[aria-pressed=true]{background:var(--accent2);border-color:var(--accent2);color:#17130a;font-weight:600}
.count{font-size:12px;color:var(--ink3);padding:10px 0 14px}

/* ── 型錄牆 ── */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:22px;padding:22px 0 80px}
.card{background:var(--bg2);border:1px solid var(--line);border-radius:3px;overflow:hidden;
  transition:.2s;display:flex;flex-direction:column}
.card:hover{border-color:var(--line2);transform:translateY(-3px)}
.card .ph{aspect-ratio:3/4;background:#1a1a20;overflow:hidden;position:relative}
.card .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;transition:.4s}
.card:hover .ph img{transform:scale(1.03)}
.card .body{padding:15px 16px 17px}
.card .nm{font-family:var(--serif);font-size:18px;margin:0 0 2px;font-weight:500}
.card .zh{font-size:12px;color:var(--ink3);margin:0 0 9px}
.card .tl{font-size:13px;color:var(--ink2);margin:0 0 12px;line-height:1.6;
  display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.tags{display:flex;flex-wrap:wrap;gap:5px}
.tag{font-size:10.5px;letter-spacing:.05em;color:var(--ink3);border:1px solid var(--line2);
  padding:2px 8px;border-radius:2px}
.tag.k{color:var(--accent2);border-color:#4a3d16}

/* ── 人設頁 ── */
.pback{font-size:12.5px;color:var(--ink3);padding:26px 0 0}
.pback:hover{color:var(--ink)}
.phead{display:grid;grid-template-columns:minmax(0,420px) minmax(0,1fr);gap:44px;padding:30px 0 46px;
  border-bottom:1px solid var(--line);align-items:start}
.phead .pimg{aspect-ratio:3/4;background:#1a1a20;border-radius:3px;overflow:hidden}
.phead .pimg img{width:100%;height:100%;object-fit:cover;object-position:50% 10%}
.phead h1{font-family:var(--serif);font-size:clamp(30px,4vw,44px);margin:0 0 4px;font-weight:500}
.phead .zh{color:var(--ink3);font-size:14px;margin:0 0 18px}
.phead .tl{font-size:18px;color:var(--accent2);font-family:var(--serif);line-height:1.6;margin:0 0 26px}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:1px;
  background:var(--line);border:1px solid var(--line);border-radius:3px;overflow:hidden;margin-bottom:24px}
.fact{background:var(--bg2);padding:13px 15px}
.fact span{display:block;font-size:10.5px;color:var(--ink3);letter-spacing:.1em;margin-bottom:3px}
.fact b{font-weight:500;font-size:13.5px}

section.sec{padding:44px 0;border-bottom:1px solid var(--line)}
section.sec>h2{font-family:var(--serif);font-size:13px;letter-spacing:.2em;color:var(--ink3);
  text-transform:uppercase;margin:0 0 22px;font-weight:400}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:36px}
.lbl{font-size:11px;letter-spacing:.1em;color:var(--ink3);margin:0 0 8px}
.prose{color:var(--ink2);font-size:14.5px;margin:0}
ul.plain{list-style:none;padding:0;margin:0}
ul.plain li{padding:7px 0;border-bottom:1px solid var(--line);font-size:14px;color:var(--ink2);
  display:flex;justify-content:space-between;gap:14px}
ul.plain li:last-child{border-bottom:0}
ul.plain li b{color:var(--ink);font-weight:500}
ul.plain li i{font-style:normal;color:var(--accent2);font-size:12.5px;white-space:nowrap}


/* 圖庫 */
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px}
.gal a{aspect-ratio:3/4;overflow:hidden;background:#1a1a20;border-radius:2px;display:block}
.gal img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;transition:.3s}
.gal a:hover img{transform:scale(1.04)}
.vids{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}
.vid{position:relative;aspect-ratio:9/16;background:#1a1a20;border-radius:2px;overflow:hidden}
.vid img{width:100%;height:100%;object-fit:cover;object-position:50% 20%;opacity:.82}
.vid .play{position:absolute;inset:0;display:grid;place-items:center;font-size:34px;color:#fff;
  text-shadow:0 2px 14px rgba(0,0,0,.7)}

/* 燈箱 */
.lb{position:fixed;inset:0;background:rgba(6,6,8,.96);z-index:100;display:none;
  place-items:center;padding:36px}
.lb[open],.lb.on{display:grid}
.lb img{max-width:100%;max-height:88vh;object-fit:contain;border-radius:2px}
.lb button{position:absolute;top:22px;right:26px;background:none;border:1px solid var(--line2);
  color:var(--ink);width:38px;height:38px;border-radius:100px;cursor:pointer;font-size:17px}

/* ── 首頁（對外報價 PPT 的網頁版）────────────────────────────── */
.top nav a.on{color:var(--accent2)}
.hsec{padding:82px 0;border-bottom:1px solid var(--line)}
.hsec:nth-child(even){background:var(--bg2)}
.eyebrow{font-size:11px;letter-spacing:.22em;color:var(--accent);margin:0 0 14px;font-weight:500}
.hsec h2{font-family:var(--serif);font-size:clamp(26px,3.6vw,40px);line-height:1.28;margin:0 0 18px;
  font-weight:500;letter-spacing:.01em}
.lead{color:var(--ink2);font-size:16px;max-width:720px;margin:0 0 34px}
.kicker{margin:34px 0 0;padding-top:20px;border-top:1px solid var(--line2);color:var(--ink);
  font-family:var(--serif);font-size:16.5px;max-width:820px;line-height:1.75}
.fine{color:var(--ink3);font-size:12px;margin:18px 0 0;max-width:760px;line-height:1.65}

/* 開場 */
.hhero{padding:104px 0 88px;border-bottom:1px solid var(--line);position:relative}
.hhero h1{font-family:var(--serif);font-size:clamp(36px,6.2vw,68px);line-height:1.16;margin:0 0 26px;
  font-weight:500;letter-spacing:.005em}
.hhero h1 em{font-style:normal;color:var(--accent2)}
.hhero .sub{max-width:640px;color:var(--ink2);font-size:17px;margin:0 0 36px}
.btns{display:flex;flex-wrap:wrap;gap:12px}
.btn{display:inline-block;padding:13px 26px;border:1px solid var(--line2);border-radius:2px;
  font-size:14px;color:var(--ink2);transition:.18s}
.btn:hover{border-color:var(--ink3);color:var(--ink)}
.btn.p{background:var(--accent2);border-color:var(--accent2);color:#17130a;font-weight:600}
.btn.p:hover{background:var(--accent);border-color:var(--accent);color:#17130a}

/* 三欄／多欄卡 */
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(258px,1fr));gap:1px;
  background:var(--line);border:1px solid var(--line);border-radius:3px;overflow:hidden}
.col{background:var(--bg);padding:26px 24px 28px}
.hsec:nth-child(even) .col{background:var(--bg2)}
.col .t{font-family:var(--serif);font-size:18px;margin:0 0 9px;font-weight:500;color:var(--ink)}
.col .n{font-size:10.5px;letter-spacing:.16em;color:var(--accent);margin:0 0 10px}
.col .tag{display:inline-block;font-size:10.5px;letter-spacing:.1em;color:var(--accent2);
  border:1px solid #4a3d16;padding:2px 8px;border-radius:2px;margin:0 0 12px}
.col p{margin:0;color:var(--ink2);font-size:14px;line-height:1.72}
.col .you{margin:14px 0 0;padding-top:12px;border-top:1px solid var(--line);
  font-size:12.5px;color:var(--ink3)}
.col .you b{color:var(--accent2);font-weight:500}

/* 兩欄對照（案例／預算）*/
/* ⚠ 標籤的 class 是 vlb 不是 lb：.lb 是燈箱，帶 display:none，撞上去整段會消失。*/
.vs{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);
  border:1px solid var(--line);border-radius:3px;overflow:hidden}
.vs>div{background:var(--bg);padding:28px 26px 30px}
.hsec:nth-child(even) .vs>div{background:var(--bg2)}
.vs .b{border-top:2px solid var(--accent)}
.vs .vlb{font-size:11.5px;letter-spacing:.14em;color:var(--ink3);margin:0 0 12px}
.vs .amt{font-family:var(--serif);font-size:clamp(24px,3vw,34px);line-height:1.2;margin:0 0 6px;
  color:var(--ink)}
.vs .b .amt{color:var(--accent2)}
.vs .amtn{font-size:12px;color:var(--ink3);margin:0 0 20px;line-height:1.6}
.vs dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:9px 16px;font-size:13.5px}
.vs dt{color:var(--ink3);white-space:nowrap}
.vs dd{margin:0;color:var(--ink2)}

/* 條列型（永續／突破／適合／保證） */
.rows{border:1px solid var(--line);border-radius:3px;overflow:hidden}
.row3{display:grid;grid-template-columns:170px 1fr 1fr;gap:0;border-bottom:1px solid var(--line)}
.row2{display:grid;grid-template-columns:190px 1fr;gap:0;border-bottom:1px solid var(--line)}
.row3:last-child,.row2:last-child{border-bottom:0}
.row3>div,.row2>div{padding:20px 22px;border-right:1px solid var(--line)}
.row3>div:last-child,.row2>div:last-child{border-right:0}
.row3 .k,.row2 .k{font-family:var(--serif);font-size:15.5px;color:var(--ink)}
.row3 .was{color:var(--ink3);font-size:13.5px}
.row3 .now,.row2 .v{color:var(--ink2);font-size:14px}
.row3 .now{color:var(--ink)}
.rhead{display:grid;grid-template-columns:170px 1fr 1fr;background:var(--bg2);
  border-bottom:1px solid var(--line2);font-size:11px;letter-spacing:.14em;color:var(--ink3)}
.hsec:nth-child(even) .rhead{background:var(--bg)}
.rhead>div{padding:11px 22px;border-right:1px solid var(--line)}
.rhead>div:last-child{border-right:0}
.rhead .hl{color:var(--accent2)}

/* 精選預覽（第 8 段）*/
.feat{display:grid;grid-template-columns:repeat(auto-fit,minmax(214px,1fr));gap:18px;margin-bottom:30px}
.fcard{background:var(--bg2);border:1px solid var(--line);border-radius:3px;overflow:hidden;
  transition:.2s;display:block}
.hsec:nth-child(even) .fcard{background:var(--bg)}
.fcard:hover{border-color:var(--line2);transform:translateY(-3px)}
.fcard .ph{aspect-ratio:3/4;background:#1a1a20;overflow:hidden}
.fcard .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;transition:.4s}
.fcard:hover .ph img{transform:scale(1.03)}
.fcard .bd{padding:14px 15px 16px}
.fcard .nm{font-family:var(--serif);font-size:17px;margin:0 0 3px;font-weight:500}
.fcard .zh{font-size:11.5px;color:var(--ink3);margin:0 0 8px}
.fcard .mt{font-size:11px;color:var(--accent2);letter-spacing:.04em;margin:0}

/* AI 揭露（首頁第 2 段內，R5 要求不能掉到後段）*/
.hsec .disclose{margin-top:34px;max-width:none}

/* 報價頁 */
.plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:20px}
.plan{border:1px solid var(--line);border-radius:3px;padding:30px 26px 32px;background:var(--bg2);
  display:flex;flex-direction:column}
.plan.f{border-color:var(--accent);background:linear-gradient(180deg,rgba(201,162,39,.07),transparent 60%)}
.plan .tier{font-size:11px;letter-spacing:.16em;color:var(--accent);margin:0 0 12px}
.plan h3{font-family:var(--serif);font-size:22px;margin:0 0 16px;font-weight:500}
.plan .pr{font-family:var(--serif);font-size:32px;color:var(--accent2);line-height:1.1;margin:0 0 22px}
.plan .pr i{font-style:normal;font-size:14px;color:var(--ink3);font-family:var(--sans)}
.plan ul{list-style:none;padding:0;margin:0}
.plan li{padding:9px 0;border-bottom:1px solid var(--line);font-size:13.5px;color:var(--ink2)}
.plan li:last-child{border-bottom:0}
.qa{border-top:1px solid var(--line)}
.qa>div{border-bottom:1px solid var(--line);padding:22px 0}
.qa .q{font-family:var(--serif);font-size:17px;margin:0 0 9px;color:var(--ink)}
.qa .a{margin:0;color:var(--ink2);font-size:14.5px;max-width:840px}

/* 收尾 */
.close{padding:96px 0 104px;text-align:center}
.close h2{font-family:var(--serif);font-size:clamp(24px,3.4vw,36px);line-height:1.4;margin:0 auto 32px;
  max-width:900px;font-weight:500}
.close .btns{justify-content:center}

@media(max-width:820px){
  .vs{grid-template-columns:1fr}
  .row3,.rhead{grid-template-columns:1fr}
  .row2{grid-template-columns:1fr}
  .row3>div,.row2>div,.rhead>div{border-right:0;border-bottom:1px solid var(--line)}
  .row3>div:last-child,.row2>div:last-child,.rhead>div:last-child{border-bottom:0}
  .rhead{display:none}
  .hhero{padding:64px 0 56px}
  .hsec{padding:56px 0}
}
footer{padding:52px 0 70px;color:var(--ink3);font-size:12.5px}
footer p{margin:0 0 7px;max-width:720px}
@media(max-width:820px){.phead{grid-template-columns:1fr;gap:26px}.hero{padding:60px 0 40px}}
`;

const layout = (title, body, { desc = '', nav = '' } = {}) => `<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>${esc(title)}</title>
${desc ? `<meta name="description" content="${esc(desc)}">` : ''}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;500;600&family=Noto+Sans+TC:wght@300;400;500&display=swap" rel="stylesheet">
<style>${CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <div class="brand"><a href="/"><b>兌心</b>科技</a></div>
  <nav>
    <a href="/kols.html"${nav === 'kols' ? ' class="on"' : ''}>全部人設</a>
    <a href="/pricing.html"${nav === 'pricing' ? ' class="on"' : ''}>報價</a>
  </nav>
</div></header>
${body}
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="放大檢視">
  <button type="button" aria-label="關閉">✕</button><img alt="">
</div>
<script>
(function(){
  var lb=document.getElementById('lb'), im=lb.querySelector('img'), last=null;
  document.addEventListener('click',function(e){
    var a=e.target.closest('[data-lb]'); if(a){e.preventDefault();last=a;
      im.src=a.getAttribute('data-lb'); im.alt=a.getAttribute('data-alt')||'';
      lb.classList.add('on'); lb.querySelector('button').focus(); return;}
    if(e.target===lb||e.target.closest('#lb button')){close();}
  });
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&lb.classList.contains('on'))close();});
  function close(){lb.classList.remove('on'); im.src=''; if(last)last.focus();}
})();
</script>
</body></html>`;

// ── 型錄牆（原本的首頁,使用者 2026-09-03 裁決搬到 /kols.html,內容不重做）──
const people = cat.personas.map(p => ({ ...p, a: assetsOf(p.id), mk: market(p.location) }));
const totalImages = people.reduce((a, p) => a + p.media.image_count, 0);
const totalVideos = people.reduce((a, p) => a + p.media.video_count, 0);

const cats = [...new Set(people.map(p => catLabel(p.category)))].sort();
const mks = [...new Set(people.map(p => p.mk))].sort();

const card = p => `
<a class="card" href="/p/${esc(p.id)}.html">
  <div class="ph">${p.a.hero ? `<img src="${p.a.hero}" alt="${esc(p.name)}" loading="lazy" width="1080" height="1440">` : ''}</div>
  <div class="body">
    <h3 class="nm">${esc(p.name)}</h3>
    <p class="zh">${esc([p.name_zh, p.age ? p.age + ' 歲' : null, p.mk].filter(Boolean).join(' · '))}</p>
    <p class="tl">${esc(p.tagline || '')}</p>
    <div class="tags">
      <span class="tag k">${esc(catLabel(p.category))}</span>
      <span class="tag">${p.media.image_count} 張圖</span>
      ${p.media.video_count ? `<span class="tag">${p.media.video_count} 支影片</span>` : ''}
    </div>
  </div>
</a>`;

const kolsPage = layout('虛擬 KOL 型錄 — 兌心科技', `
<div class="hero"><div class="wrap">
  <h1>虛擬 <em>KOL</em> 型錄</h1>
  <p class="lede">${people.length} 位可合作的虛擬 KOL。每一位都有完整的人物設定、內容主題與視覺調性，
  並且已經產出可用的圖像與影片素材。</p>
  <div class="disclose">
    <b>這些是 AI 生成的虛擬人物。</b>
    <p>不是真人。所有肖像與影片皆由本團隊自行生成，角色設定、語氣與內容規範亦為原創。
    虛擬 KOL 沒有檔期衝突、不會有個人爭議，且能同時經營多個平台與多語市場。</p>
  </div>
</div></div>

<div class="filters"><div class="wrap">
  <div class="frow"><span>領域</span>
    <button class="chip" aria-pressed="true" data-f="cat" data-v="">全部</button>
    ${cats.map(c => `<button class="chip" aria-pressed="false" data-f="cat" data-v="${esc(c)}">${esc(c)}</button>`).join('')}
  </div>
  <div class="frow"><span>市場</span>
    <button class="chip" aria-pressed="true" data-f="mk" data-v="">全部</button>
    ${mks.map(m => `<button class="chip" aria-pressed="false" data-f="mk" data-v="${esc(m)}">${esc(m)}</button>`).join('')}
  </div>
  <div class="frow"><span>素材</span>
    <button class="chip" aria-pressed="true" data-f="med" data-v="">全部</button>
    <button class="chip" aria-pressed="false" data-f="med" data-v="video">有影片素材</button>
  </div>
  <div class="frow"><span>排序</span>
    <button class="chip" aria-pressed="true" data-s="feat">推薦</button>
    <button class="chip" aria-pressed="false" data-s="material">素材最多</button>
    <button class="chip" aria-pressed="false" data-s="age">年齡由小到大</button>
    <button class="chip" aria-pressed="false" data-s="name">名字</button>
  </div>
  <p class="count" id="count">顯示 ${people.length} 位</p>
</div></div>

<div class="wrap"><div class="grid" id="grid">
${people.map((p, i) => `<div class="cell" data-cat="${esc(catLabel(p.category))}" data-mk="${esc(p.mk)}" data-video="${p.media.video_count ? 'video' : ''}" data-feat="${i}" data-material="${p.media.image_count * 10 + p.media.video_count}" data-age="${p.age || 99}" data-name="${esc(p.name)}">${card(p)}</div>`).join('')}
</div></div>

<div class="wrap" id="about"><section class="sec">
  <h2>關於這份型錄</h2>
  <div class="two">
    <div><p class="lede prose">這份型錄只收錄<b>素材已經到位</b>的人設。還在建置中的角色不列入，
    所以你在這裡看到的每一位，都是現在就能討論合作的。</p></div>
    <div><p class="prose">每一位人設的頁面包含：角色設定與語氣、內容主題與比重、合作邊界、
    設定文件的深度，以及實際產出的圖像與影片素材。</p></div>
  </div>
</section></div>

<footer><div class="wrap">
  <p>本型錄所有人物均為 AI 生成的虛擬角色，非真實人物。</p>
  <p>素材與設定為本團隊原創。頁面不進入搜尋引擎索引。</p>
</div></footer>

<script>
(function(){
  var st={cat:'',mk:'',med:''}, sort='feat';
  var grid=document.getElementById('grid');
  var cells=[].slice.call(grid.querySelectorAll('.cell'));

  function apply(){
    var n=0;
    cells.forEach(function(c){
      var ok=(!st.cat||c.dataset.cat===st.cat)&&(!st.mk||c.dataset.mk===st.mk)&&(!st.med||c.dataset.video===st.med);
      c.hidden=!ok; if(ok)n++;
    });
    document.getElementById('count').textContent='顯示 '+n+' 位';

    var sorted=cells.slice().sort(function(a,b){
      if(sort==='feat')     return (+a.dataset.feat)-(+b.dataset.feat);
      if(sort==='material') return (+b.dataset.material)-(+a.dataset.material);
      if(sort==='age')      return (+a.dataset.age)-(+b.dataset.age);
      return a.dataset.name.localeCompare(b.dataset.name,'zh-Hant');
    });
    sorted.forEach(function(c){ grid.appendChild(c); });
  }

  document.querySelectorAll('.chip[data-f]').forEach(function(b){
    b.addEventListener('click',function(){
      var f=b.dataset.f; st[f]=b.dataset.v;
      document.querySelectorAll('.chip[data-f="'+f+'"]').forEach(function(o){
        o.setAttribute('aria-pressed', String(o===b)); });
      apply();
    });
  });
  document.querySelectorAll('.chip[data-s]').forEach(function(b){
    b.addEventListener('click',function(){
      sort=b.dataset.s;
      document.querySelectorAll('.chip[data-s]').forEach(function(o){
        o.setAttribute('aria-pressed', String(o===b)); });
      apply();
    });
  });
  apply();
})();
</script>
`, { desc: '可合作的虛擬 KOL 型錄，含完整角色設定與可用素材。', nav: 'kols' });

// ── 人設頁 ──────────────────────────────────────────────────────────
const personPage = p => {
  const facts = [
    ['年齡', p.age ? p.age + ' 歲' : null],
    ['市場', p.mk],
    ['族裔', p.ethnicity],
    ['語言', p.languages.length ? p.languages.map(langShort).slice(0, 3).join('・') : null],
    ['領域', catLabel(p.category)],
  ].filter(x => x[1]);

  return layout(`${p.name} — 虛擬 KOL 型錄`, `
<div class="wrap">
  <p class="pback"><a href="/kols.html">← 回到全部人設</a></p>
  <div class="phead">
    <div class="pimg">${p.a.hero ? `<img src="${p.a.hero}" alt="${esc(p.name)}" width="1080" height="1440">` : ''}</div>
    <div>
      <h1>${esc(p.name)}</h1>
      <p class="zh">${esc(p.name_zh || '')}</p>
      <p class="tl">${esc(p.tagline || '')}</p>
      <div class="facts">${facts.map(([k, v]) => `<div class="fact"><span>${esc(k)}</span><b>${esc(v)}</b></div>`).join('')}</div>
      ${p.archetype ? `<p class="prose">${esc(p.archetype)}</p>` : ''}
    </div>
  </div>

  ${p.pillars.length ? `<section class="sec"><h2>內容主題</h2>
    <ul class="plain">${p.pillars.map(x => `<li><b>${esc(x.name)}</b>${x.weight ? `<i>${esc(x.weight)}</i>` : ''}</li>`).join('')}</ul>
  </section>` : ''}

  ${(p.personality.length || p.voice_tone || p.aesthetic_mood) ? `<section class="sec"><h2>性格・語氣・視覺調性</h2>
    ${p.personality.length ? `<p class="lbl">性格</p><ul class="plain">${p.personality.slice(0, 8).map(t => `<li>${esc(t)}</li>`).join('')}</ul>` : ''}
    <div class="two" style="margin-top:26px">
      ${p.voice_tone ? `<div><p class="lbl">語氣</p><p class="prose">${esc(p.voice_tone)}</p></div>` : ''}
      ${p.aesthetic_mood ? `<div><p class="lbl">視覺調性</p><p class="prose">${esc(p.aesthetic_mood)}</p></div>` : ''}
    </div>
  </section>` : ''}

  ${p.a.gallery.length ? `<section class="sec"><h2>圖像素材</h2>
    <div class="gal">${p.a.gallery.map((g, i) => `<a href="${g.web}" data-lb="${g.web}" data-alt="${esc(p.name)} 素材 ${i + 1}">
      <img src="${g.thumb}" alt="${esc(p.name)} 素材 ${i + 1}" loading="lazy" width="400" height="533"></a>`).join('')}</div>
  </section>` : ''}

  ${p.a.posters.length ? `<section class="sec"><h2>影片素材</h2>
    <div class="vids">${p.a.posters.map((s, i) => `<div class="vid">
      <img src="${s}" alt="${esc(p.name)} 影片 ${i + 1} 首幀" loading="lazy" width="720" height="1280">
      <span class="play" aria-hidden="true">▶</span></div>`).join('')}</div>
    <p class="prose" style="margin-top:14px;font-size:13px">影片可於洽談時提供完整檔案。</p>
  </section>` : ''}

  ${p.fit.length ? `<section class="sec"><h2>適合的合作方向</h2>
    <ul class="plain">${p.fit.slice(0, 8).map(x => `<li>${esc(x)}</li>`).join('')}</ul>
    <p class="prose" style="margin-top:16px;font-size:13.5px">
      以上是依她現有人設最自然的方向。<b>虛擬 KOL 的設定可以依品牌需求調整</b>——
      選定了外形之後，內容主題與語氣都能配合合作內容重新設定。</p>
  </section>` : ''}
</div>
<footer><div class="wrap">
  <p>${esc(p.name)} 為 AI 生成的虛擬角色，非真實人物。</p>
  <p><a href="/kols.html">← 回到全部人設</a></p>
</div></footer>
`, { desc: p.tagline || '', nav: 'kols' });
};


// ── 首頁：對外報價 PPT 的網頁版 ──────────────────────────────────
// 使用者 2026-09-03：「我現在就是想把對外報價的 PPT 轉成網頁版的 dashboard。」
// 段落與 PPT 頁次的對應表在覆核包 §12.2（13 段）。
// 🛑 PPT 的 p15 方案報價與 p16 常見問題不在首頁,搬去 /pricing.html。
// 🛑 文字全部來自 pitch.json,這裡只排版,不改一個字（業務承諾）。
const P = pitch;

// 第 8 段的精選預覽。🛑 放哪幾位由使用者在 copy.json 的 `featured` 指定,
// 程式不自己挑（覆核包 §12.2 的 R5 規定）。指名的人設若不在型錄裡就跳過。
const featured = (copy.featured || [])
  .map(id => people.find(p => p.id === id))
  .filter(Boolean);

// 🛑 寫成程式擋住,不要只寫成規則（這個 repo 的教訓：文件會再犯,程式不會）。
// R5 否決了「第 8 段只放一個文字連結」,理由是客戶點擊之前就要先看到真的有人設有素材。
// 所以這一段少於 3 位就不是那個規劃,直接不要產出。
if (featured.length < 3) {
  console.error(`🛑 首頁精選預覽只湊到 ${featured.length} 位（規劃要求 3〜4 位）。`);
  console.error(`   copy.json 的 \`featured\` = ${JSON.stringify(copy.featured || [])}`);
  console.error('   → 那幾個 id 要在 catalog.json 的人設裡找得到。改好再跑。');
  process.exit(2);
}
if (featured.some(p => !p.a.hero)) {
  console.error('🛑 精選預覽有人設沒有封面圖 → ' +
    featured.filter(p => !p.a.hero).map(p => p.id).join('、'));
  process.exit(2);
}

const cols = (arr, n = '') => `<div class="cols">${arr.map(c => `<div class="col">
  ${c.n ? `<p class="n">${esc(c.n)}</p>` : ''}
  ${c.tag ? `<span class="tag">${esc(c.tag)}</span>` : ''}
  <p class="t">${esc(c.t)}</p>
  <p>${esc(c.p)}</p>
  ${c.you ? `<p class="you">您要做的：<b>${esc(c.you)}</b></p>` : ''}
</div>`).join('')}</div>${n ? `<p class="kicker">${esc(n)}</p>` : ''}`;

const rows2 = arr => `<div class="rows">${arr.map(([k, v]) => `<div class="row2">
  <div class="k">${esc(k)}</div><div class="v">${esc(v)}</div></div>`).join('')}</div>`;

const vsSide = (d, cls) => `<div class="${cls}">
  <p class="vlb">${esc(d.label)}</p>
  <p class="amt">${esc(d.amount)}</p>
  <p class="amtn">${esc(d.amount_note)}</p>
  <dl>${d.rows.map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join('')}</dl>
</div>`;

const homePage = layout('虛擬 KOL 品牌顧問服務 — 兌心科技', `
<div class="hhero"><div class="wrap">
  <p class="eyebrow">${esc(P.hero.eyebrow)}</p>
  <h1>${P.hero.title_lines.map((l, i) => i === P.hero.title_lines.length - 1
      ? `<em>${esc(l)}</em>` : esc(l)).join('<br>')}</h1>
  <p class="sub">${esc(P.hero.sub)}</p>
  <div class="btns">${P.hero.cta.map(c =>
    `<a class="btn${c.primary ? ' p' : ''}" href="${esc(c.href)}">${esc(c.label)}</a>`).join('')}</div>
</div></div>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.what.eyebrow)}</p>
  <h2>${esc(P.what.title)}</h2>
  <p class="lead">${esc(P.what.lead)}</p>
  ${cols(P.what.pillars.map(x => ({ t: x.k, p: x.v })), P.what.note)}
  <div class="disclose">
    <b>這些 KOL 是 AI 生成的虛擬人物。</b>
    <p>不是真人。所有肖像、聲音與影片皆由本團隊自行生成，人設、語氣與內容規範亦為原創；
    發布時依各平台規範標示 AI 內容。虛擬 KOL 沒有檔期衝突、不會有個人爭議，
    且能同時經營多個平台與多語市場。</p>
  </div>
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.value.eyebrow)}</p>
  <h2>${esc(P.value.title)}</h2>
  ${cols(P.value.cards.map(c => ({ tag: c.tag, t: c.h, p: c.p })))}
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.why_public.eyebrow)}</p>
  <h2>${esc(P.why_public.title)}</h2>
  <p class="lead">${esc(P.why_public.lead)}</p>
  <div class="vs">
    ${vsSide(P.why_public.compare.a, 'a')}
    ${vsSide(P.why_public.compare.b, 'b')}
  </div>
  <p class="kicker">${esc(P.why_public.kicker)}</p>
  <p class="fine">${esc(P.why_public.disclaimer)}</p>
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.budget.eyebrow)}</p>
  <h2>${esc(P.budget.title)}</h2>
  ${rows2(P.budget.rows.map(r => [r.k, r.v]))}
  <p class="kicker">${esc(P.budget.note)}</p>
  <p class="fine">${esc(P.budget.footnote)}</p>
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.legacy.eyebrow)}</p>
  <h2>${esc(P.legacy.title)}</h2>
  <p class="lead">${esc(P.legacy.lead)}</p>
  ${rows2(P.legacy.rows)}
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.breakthrough.eyebrow)}</p>
  <h2>${esc(P.breakthrough.title)}</h2>
  <div class="rows">
    <div class="rhead"><div></div><div>傳統製作的限制</div><div class="hl">數位人 KOL</div></div>
    ${P.breakthrough.rows.map(([k, was, now]) => `<div class="row3">
      <div class="k">${esc(k)}</div><div class="was">${esc(was)}</div>
      <div class="now">${esc(now)}</div></div>`).join('')}
  </div>
  <p class="fine">${esc(P.breakthrough.note)}</p>
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">CATALOGUE｜看實際的人設與素材</p>
  <h2>不必想像，直接看</h2>
  <p class="lead">每一位都有完整的人物設定、內容主題與視覺調性，並且已經產出可用的圖像與影片素材。
  點進任何一位，都能直接在網頁上看完他全部的素材。</p>
  <div class="feat">${featured.map(p => `<a class="fcard" href="/p/${esc(p.id)}.html">
    <div class="ph">${p.a.hero ? `<img src="${p.a.hero}" alt="${esc(p.name)}" loading="lazy" width="1080" height="1440">` : ''}</div>
    <div class="bd">
      <p class="nm">${esc(p.name)}</p>
      <p class="zh">${esc([p.name_zh, p.mk].filter(Boolean).join(' · '))}</p>
      <p class="mt">${esc(catLabel(p.category))}</p>
    </div></a>`).join('')}</div>
  <div class="btns"><a class="btn p" href="/kols.html">看全部人設 →</a></div>
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.engine.eyebrow)}</p>
  <h2>${esc(P.engine.title)}</h2>
  <p class="lead">${esc(P.engine.lead)}</p>
  ${cols(P.engine.steps.map(x => ({ n: x.n, t: x.t, p: x.p })))}
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.fit.eyebrow)}</p>
  <h2>${esc(P.fit.title)}</h2>
  <p class="lead">${esc(P.fit.lead)}</p>
  ${rows2(P.fit.rows)}
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.quality.eyebrow)}</p>
  <h2>${esc(P.quality.title)}</h2>
  ${cols(P.quality.cards.map(([h, p]) => ({ t: h, p })), P.quality.kicker)}
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.onboarding.eyebrow)}</p>
  <h2>${esc(P.onboarding.title)}</h2>
  ${cols(P.onboarding.steps.map(x => ({ n: x.n, t: x.t, p: x.p, you: x.you })), P.onboarding.kicker)}
</div></section>

<div class="close"><div class="wrap">
  <h2>${esc(P.closing.title)}</h2>
  <div class="btns">
    <a class="btn p" href="${esc(P.closing.cta.href)}">${esc(P.closing.cta.label)}</a>
    <a class="btn" href="/pricing.html">方案與報價</a>
  </div>
</div></div>

<footer><div class="wrap">
  <p>${esc(P.brand.name)}　${esc(P.brand.en)}　${esc(P.brand.line)}</p>
  <p>本站所有 KOL 均為 AI 生成的虛擬角色，非真實人物；素材與設定為本團隊原創。</p>
  <p>頁面不進入搜尋引擎索引。</p>
</div></footer>
`, { desc: P.hero.sub, nav: '' });

// ── 報價頁（PPT p15 方案報價 ＋ p16 常見問題）────────────────────
// 🛑 價格與方案內容一個字都不改（覆核包 §12.6）。
const pricingPage = layout('方案與報價 — 兌心科技', `
<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.plans.eyebrow)}</p>
  <h2>${esc(P.plans.title)}</h2>
  <div class="plans">${P.plans.items.map(x => `<div class="plan${x.featured ? ' f' : ''}">
    <p class="tier">${esc(x.tier)}</p>
    <h3>${esc(x.name)}</h3>
    <p class="pr">${esc(x.price)}<i>${esc(x.unit)}</i></p>
    <ul>${x.bullets.map(b => `<li>${esc(b)}</li>`).join('')}</ul>
  </div>`).join('')}</div>
  <p class="kicker">${esc(P.quality.kicker)}</p>
</div></section>

<section class="hsec"><div class="wrap">
  <p class="eyebrow">${esc(P.faq.eyebrow)}</p>
  <h2>${esc(P.faq.title)}</h2>
  <div class="qa">${P.faq.items.map(([q, a]) => `<div>
    <p class="q">${esc(q)}</p><p class="a">${esc(a)}</p></div>`).join('')}</div>
</div></section>

<div class="close"><div class="wrap">
  <h2>${esc(P.closing.title)}</h2>
  <div class="btns">
    <a class="btn p" href="${esc(P.closing.cta.href)}">${esc(P.closing.cta.label)}</a>
    <a class="btn" href="/">回首頁</a>
  </div>
</div></div>

<footer><div class="wrap">
  <p>${esc(P.brand.name)}　${esc(P.brand.en)}　${esc(P.brand.line)}</p>
  <p>本站所有 KOL 均為 AI 生成的虛擬角色，非真實人物。</p>
</div></footer>
`, { desc: '虛擬 KOL 經營的方案與報價。', nav: 'pricing' });

// ── 寫檔 ────────────────────────────────────────────────────────────
fs.rmSync(PUB, { recursive: true, force: true });
fs.mkdirSync(path.join(PUB, 'p'), { recursive: true });
fs.writeFileSync(path.join(PUB, 'index.html'), homePage);
fs.writeFileSync(path.join(PUB, 'kols.html'), kolsPage);
fs.writeFileSync(path.join(PUB, 'pricing.html'), pricingPage);
for (const p of people) fs.writeFileSync(path.join(PUB, 'p', `${p.id}.html`), personPage(p));
fs.writeFileSync(path.join(PUB, 'robots.txt'), 'User-agent: *\nDisallow: /\n');

console.log(`產生 ${people.length + 3} 頁 → ${PUB}`);
for (const f of ['index.html', 'kols.html', 'pricing.html']) {
  console.log(`  ${f.padEnd(13)} ${(fs.statSync(path.join(PUB, f)).size / 1024).toFixed(0)} KB`);
}
console.log(`  p/*.html      ${people.length} 頁`);
console.log(`  首頁精選預覽   ${featured.map(p => p.name).join('、')}`);
