#!/usr/bin/env node
/**
 * 從 catalog.json ＋ assets/ 產生靜態頁面 → catalog/public/
 *
 * 內容依據只有使用者說的那四件事（見覆核包 §2.2）：
 *   1 設定是什麼  2 有哪些素材  3 細節到什麼程度  4 大概的營運數據
 * 🛑 不輸出任何狀態、handle、三圍、prompt／模型／credits、營運統計期間。
 */
import fs from 'node:fs';
import path from 'node:path';

const DIR = path.join(import.meta.dirname, '..');
const PUB = path.join(DIR, 'public');
const cat = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'catalog.json'), 'utf8'));

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

const assetsOf = id => {
  const d = path.join(DIR, 'assets', id);
  let files = []; try { files = fs.readdirSync(d); } catch {}
  const gal = files.filter(f => /^g\d+\.jpg$/.test(f)).sort();
  return {
    hero: files.includes('hero.jpg') ? `/assets/${id}/hero.jpg` : (gal[0] ? `/assets/${id}/${gal[0]}` : null),
    gallery: gal.map(f => ({ web: `/assets/${id}/${f}`, thumb: `/assets/${id}/${f.replace('.jpg', '_t.jpg')}` })),
    posters: files.filter(f => /_poster\.jpg$/.test(f)).sort().map(f => `/assets/${id}/${f}`),
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

/* 設定深度 */
.depth{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1px;
  background:var(--line);border:1px solid var(--line);border-radius:3px;overflow:hidden}
.depth div{background:var(--bg2);padding:16px 17px}
.depth b{display:block;font-family:var(--serif);font-size:26px;color:var(--accent2);line-height:1.1}
.depth span{font-size:11.5px;color:var(--ink3)}
.aspects{display:flex;flex-wrap:wrap;gap:6px;margin-top:16px}

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

footer{padding:52px 0 70px;color:var(--ink3);font-size:12.5px}
footer p{margin:0 0 7px;max-width:720px}
@media(max-width:820px){.phead{grid-template-columns:1fr;gap:26px}.hero{padding:60px 0 40px}}
`;

const layout = (title, body, { desc = '' } = {}) => `<!doctype html>
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
  <div class="brand"><a href="/"><b>KOL</b> 型錄</a></div>
  <nav><a href="/">全部人設</a><a href="/#about">關於這份型錄</a></nav>
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

// ── 首頁 ────────────────────────────────────────────────────────────
const people = cat.personas.map(p => ({ ...p, a: assetsOf(p.id), mk: market(p.location) }));
const totalImages = people.reduce((a, p) => a + p.media.image_count, 0);
const totalVideos = people.reduce((a, p) => a + p.media.video_count, 0);
const totalSpecLines = people.reduce((a, p) => a + p.depth.doc_lines_total, 0);

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

const index = layout('AI KOL 型錄', `
<div class="hero"><div class="wrap">
  <h1>${people.length} 位<em>已建置完成</em>的<br>虛擬 KOL</h1>
  <p class="lede">每一位都有完整的角色設定、內容規範與視覺規格，並且已經產出可用的圖像與影片素材。
  這份型錄讓你在幾分鐘內看完他們是誰、內容長什麼樣、素材到什麼程度。</p>
  <div class="stats">
    <div class="stat"><b>${people.length}</b><span>人設</span></div>
    <div class="stat"><b>${totalImages}</b><span>可用圖像</span></div>
    <div class="stat"><b>${totalVideos}</b><span>影片素材</span></div>
    <div class="stat"><b>${totalSpecLines.toLocaleString('en-US')}</b><span>行角色設定</span></div>
  </div>
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
  <p class="count" id="count">顯示 ${people.length} 位</p>
</div></div>

<div class="wrap"><div class="grid" id="grid">
${people.map(p => `<div class="cell" data-cat="${esc(catLabel(p.category))}" data-mk="${esc(p.mk)}" data-video="${p.media.video_count ? 'video' : ''}">${card(p)}</div>`).join('')}
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
  var st={cat:'',mk:'',med:''};
  var cells=[].slice.call(document.querySelectorAll('#grid .cell'));
  document.querySelectorAll('.chip').forEach(function(b){
    b.addEventListener('click',function(){
      var f=b.dataset.f;
      st[f]=b.dataset.v;
      document.querySelectorAll('.chip[data-f="'+f+'"]').forEach(function(o){
        o.setAttribute('aria-pressed', String(o===b));
      });
      var n=0;
      cells.forEach(function(c){
        var ok=(!st.cat||c.dataset.cat===st.cat)&&(!st.mk||c.dataset.mk===st.mk)&&(!st.med||c.dataset.video===st.med);
        c.hidden=!ok; if(ok)n++;
      });
      document.getElementById('count').textContent='顯示 '+n+' 位';
    });
  });
})();
</script>
`, { desc: `${people.length} 位已建置完成的 AI 虛擬 KOL，含完整角色設定與可用素材。` });

// ── 人設頁 ──────────────────────────────────────────────────────────
const personPage = p => {
  const d = p.depth;
  const facts = [
    ['年齡', p.age ? p.age + ' 歲' : null],
    ['市場', p.mk],
    ['族裔', p.ethnicity],
    ['語言', p.languages.length ? p.languages.map(langShort).slice(0, 3).join('・') : null],
    ['領域', catLabel(p.category)],
  ].filter(x => x[1]);

  return layout(`${p.name} — AI KOL 型錄`, `
<div class="wrap">
  <p class="pback"><a href="/">← 回到全部人設</a></p>
  <div class="phead">
    <div class="pimg">${p.a.hero ? `<img src="${p.a.hero}" alt="${esc(p.name)}" width="1080" height="1440">` : ''}</div>
    <div>
      <h1>${esc(p.name)}</h1>
      <p class="zh">${esc(p.name_zh || '')}</p>
      <p class="tl">${esc(p.tagline || '')}</p>
      <div class="facts">${facts.map(([k, v]) => `<div class="fact"><span>${esc(k)}</span><b>${esc(v)}</b></div>`).join('')}</div>
      ${p.archetype ? `<p class="prose">${esc(String(p.archetype).replace(/\s*—\s*/, '｜'))}</p>` : ''}
    </div>
  </div>

  ${(p.personality.length || p.voice_tone) ? `<section class="sec"><h2>設定</h2><div class="two">
    ${p.personality.length ? `<div><p class="lbl">性格</p><div class="tags">${p.personality.slice(0, 10).map(t => `<span class="tag">${esc(t)}</span>`).join('')}</div></div>` : ''}
    ${p.voice_tone ? `<div><p class="lbl">語氣</p><p class="prose">${esc(p.voice_tone)}</p></div>` : ''}
    ${p.aesthetic?.mood ? `<div><p class="lbl">視覺調性</p><p class="prose">${esc(p.aesthetic.mood)}</p></div>` : ''}
  </div></section>` : ''}

  ${p.pillars.length ? `<section class="sec"><h2>內容主題與比重</h2>
    <ul class="plain">${p.pillars.map(x => `<li><b>${esc(x.name)}</b>${x.weight ? `<i>${esc(x.weight)}</i>` : ''}</li>`).join('')}</ul>
  </section>` : ''}

  <section class="sec"><h2>設定的細節到什麼程度</h2>
    <div class="depth">
      <div><b>${d.doc_lines_total.toLocaleString('en-US')}</b><span>行設定文件</span></div>
      <div><b>${d.spec_fields}</b><span>項規格欄位</span></div>
      ${d.pillar_count ? `<div><b>${d.pillar_count}</b><span>條內容主題</span></div>` : ''}
      ${d.training_set_images ? `<div><b>${d.training_set_images}</b><span>張專屬視覺訓練集</span></div>` : ''}
    </div>
    ${d.docs.length ? `<p class="lbl" style="margin-top:18px">設定文件</p>
      <ul class="plain">${d.docs.map(x => `<li><b>${esc(x.label)}</b><i>${x.lines} 行</i></li>`).join('')}</ul>` : ''}
    ${d.aspects.length ? `<p class="lbl" style="margin-top:18px">涵蓋面向</p>
      <div class="aspects">${d.aspects.map(a => `<span class="tag k">${esc(a)}</span>`).join('')}</div>` : ''}
  </section>

  ${p.a.gallery.length ? `<section class="sec"><h2>圖像素材（共 ${p.media.image_count} 張，此處展示 ${p.a.gallery.length} 張）</h2>
    <div class="gal">${p.a.gallery.map((g, i) => `<a href="${g.web}" data-lb="${g.web}" data-alt="${esc(p.name)} 素材 ${i + 1}">
      <img src="${g.thumb}" alt="${esc(p.name)} 素材 ${i + 1}" loading="lazy" width="400" height="533"></a>`).join('')}</div>
  </section>` : ''}

  ${p.a.posters.length ? `<section class="sec"><h2>影片素材（共 ${p.media.video_count} 支）</h2>
    <div class="vids">${p.a.posters.map((s, i) => `<div class="vid">
      <img src="${s}" alt="${esc(p.name)} 影片 ${i + 1} 首幀" loading="lazy" width="720" height="1280">
      <span class="play" aria-hidden="true">▶</span></div>`).join('')}</div>
    <p class="prose" style="margin-top:14px;font-size:13px">影片可於實際洽談時提供完整檔案。</p>
  </section>` : ''}

  ${(p.boundaries.fit.length || p.boundaries.not.length) ? `<section class="sec"><h2>合作方向</h2><div class="two">
    ${p.boundaries.fit.length ? `<div><p class="lbl">適合</p><ul class="plain">${p.boundaries.fit.slice(0, 8).map(x => `<li>${esc(x)}</li>`).join('')}</ul></div>` : ''}
    ${p.boundaries.not.length ? `<div><p class="lbl">不接</p><ul class="plain">${p.boundaries.not.slice(0, 8).map(x => `<li>${esc(x)}</li>`).join('')}</ul></div>` : ''}
  </div></section>` : ''}
</div>
<footer><div class="wrap">
  <p>${esc(p.name)} 為 AI 生成的虛擬角色，非真實人物。</p>
  <p><a href="/">← 回到全部人設</a></p>
</div></footer>
`, { desc: p.tagline || '' });
};

// ── 寫檔 ────────────────────────────────────────────────────────────
fs.rmSync(PUB, { recursive: true, force: true });
fs.mkdirSync(path.join(PUB, 'p'), { recursive: true });
fs.writeFileSync(path.join(PUB, 'index.html'), index);
for (const p of people) fs.writeFileSync(path.join(PUB, 'p', `${p.id}.html`), personPage(p));
fs.writeFileSync(path.join(PUB, 'robots.txt'), 'User-agent: *\nDisallow: /\n');

console.log(`產生 ${people.length + 1} 頁 → ${PUB}`);
console.log(`  index.html ${(fs.statSync(path.join(PUB, 'index.html')).size / 1024).toFixed(0)} KB`);
