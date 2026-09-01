#!/usr/bin/env node
/**
 * 素材挑選後台 → catalog/public/pick.html ＋ catalog/assets/_pick/
 *
 * 使用者 2026-09-01：「有好幾個人設明明我生產過素材卻沒放上去。
 * 你直接做一個可以勾選的網頁給我，裡面要有所有人設曾經產出的所有素材，
 * 讓我自己挑選要放什麼、不要放什麼。」
 *
 * 所以這一頁的規矩是：
 *   1. 顯示**全部**素材，包含程式預設不挑的那些（標出理由，可以自己勾回來）
 *   2. 唯一不顯示的是長邊 < 1024px 的——那是真人參考素材的防線，不是品味判斷
 *   3. 程式的挑選只當「預設值」，人勾什麼就是什麼
 *
 * 選擇結果存在瀏覽器裡（localStorage），按「複製選擇結果」拿到 JSON，
 * 貼回給 Claude 存成 catalog/data/selection.json，型錄就照那份重出。
 *
 * 用法：node catalog/tools/build_picker.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const REPO_ROOT = process.env.REPO_ROOT || '/home/user';
const DIR = path.join(import.meta.dirname, '..');
const PICK_DIR = path.join(DIR, 'assets', '_pick');
const OUT = path.join(DIR, 'public', 'pick.html');

const THUMB = { width: 320, q: 70 };

const FF = execFileSync('python3', ['-c', 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())'], { encoding: 'utf8' }).trim();
const ff = a => execFileSync(FF, ['-hide_banner', '-nostdin', '-loglevel', 'error', '-y', ...a], { stdio: ['ignore', 'pipe', 'pipe'] });

const cat = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'catalog.json'), 'utf8'));
let sel = {};
try { sel = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'selection.json'), 'utf8')).personas || {}; } catch {}

const esc = s => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const id8 = s => { let h = 5381; for (const c of s) h = ((h * 33) ^ c.charCodeAt(0)) >>> 0; return h.toString(36).padStart(7, '0'); };

fs.mkdirSync(PICK_DIR, { recursive: true });

let made = 0, cached = 0, failed = 0;
const groups = [];

for (const p of cat.personas) {
  const dir = path.join(PICK_DIR, p.id);
  fs.mkdirSync(dir, { recursive: true });

  // 目前型錄實際在用的（build_assets 的預設：候選前 9）
  const currentDefault = (sel[p.id]?.gallery) || p.media.candidates.slice(0, 9).map(c => c.rel);
  const currentHero = sel[p.id]?.hero || currentDefault[0];

  const items = [
    ...p.media.candidates.map(c => ({ ...c, blocked: null })),
    ...p.media.excluded.filter(e => e.recoverable).map(e => ({
      rel: e.file, mb: null, w: e.w, h: e.h, score: null, reasons: [], blocked: e.why,
    })),
  ];

  const rows = [];
  for (const it of items) {
    const key = id8(it.rel);
    const src = path.join(REPO_ROOT, it.rel);
    const out = path.join(dir, `${key}.jpg`);
    if (!fs.existsSync(out)) {
      if (!fs.existsSync(src)) { failed++; continue; }
      try { ff(['-i', src, '-vf', `scale=${THUMB.width}:-2`, '-q:v', String(Math.round((100 - THUMB.q) / 100 * 30) + 2), out]); made++; }
      catch { failed++; continue; }
    } else cached++;

    rows.push({
      key, rel: it.rel,
      name: it.rel.split('/').slice(3).join('/'),      // 去掉 repo/kols/<persona>/
      thumb: `/assets/_pick/${p.id}/${key}.jpg`,
      w: it.w, h: it.h, blocked: it.blocked,
      on: currentDefault.includes(it.rel),
      hero: it.rel === currentHero,
    });
  }
  groups.push({ id: p.id, name: p.name, name_zh: p.name_zh, rows });
  process.stdout.write(`  ${p.name} ${rows.length} 張\n`);
}

const CSS = `
*{box-sizing:border-box}
body{margin:0;background:#0e0e11;color:#eee;font:14px/1.6 -apple-system,"Segoe UI","PingFang TC","Microsoft JhengHei",sans-serif}
a{color:#e8c85a}
.bar{position:sticky;top:0;z-index:20;background:rgba(14,14,17,.96);backdrop-filter:blur(10px);
  border-bottom:1px solid #2a2a32;padding:14px 22px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.bar h1{font-size:16px;margin:0;font-weight:600}
.bar .sp{margin-left:auto}
button{background:#e8c85a;color:#17130a;border:0;padding:9px 18px;border-radius:4px;
  font:inherit;font-weight:600;cursor:pointer}
button.ghost{background:transparent;color:#bbb;border:1px solid #3a3a44;font-weight:400}
button:hover{filter:brightness(1.08)}
.wrap{padding:0 22px 90px}
section{padding:26px 0;border-bottom:1px solid #23232a}
h2{font-size:17px;margin:0 0 4px}
h2 small{color:#888;font-weight:400;font-size:13px;margin-left:8px}
.cnt{color:#e8c85a;font-size:13px;margin:0 0 14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.it{position:relative;border:2px solid transparent;border-radius:4px;overflow:hidden;
  background:#1a1a20;cursor:pointer;display:block}
.it img{width:100%;aspect-ratio:3/4;object-fit:cover;object-position:50% 12%;display:block;opacity:.55;transition:.15s}
.it.on{border-color:#e8c85a}
.it.on img{opacity:1}
.it .n{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(transparent,rgba(0,0,0,.92));
  padding:16px 7px 5px;font-size:10px;line-height:1.35;color:#ddd;word-break:break-all}
.it .tick{position:absolute;top:6px;left:6px;width:21px;height:21px;border-radius:3px;
  background:rgba(0,0,0,.6);border:1.5px solid #777;display:grid;place-items:center;font-size:13px;color:transparent}
.it.on .tick{background:#e8c85a;border-color:#e8c85a;color:#17130a}
.it .hero{position:absolute;top:6px;right:6px;font-size:10px;padding:2px 7px;border-radius:3px;
  background:rgba(0,0,0,.65);border:1px solid #555;color:#aaa}
.it.isHero .hero{background:#e8c85a;color:#17130a;border-color:#e8c85a;font-weight:600}
.it .warn{position:absolute;top:32px;left:6px;right:6px;font-size:9.5px;background:rgba(150,60,40,.9);
  padding:3px 5px;border-radius:3px;line-height:1.3}
.dlg{position:fixed;inset:0;background:rgba(0,0,0,.9);z-index:50;display:none;place-items:center;padding:30px}
.dlg.on{display:grid}
.dlg .box{background:#16161b;border:1px solid #33333c;border-radius:6px;padding:22px;max-width:760px;width:100%}
.dlg textarea{width:100%;height:300px;background:#0b0b0e;color:#ddd;border:1px solid #33333c;
  border-radius:4px;padding:12px;font:12px/1.5 ui-monospace,Menlo,monospace;resize:vertical}
.hint{color:#999;font-size:12.5px}
`;

const html = `<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>素材挑選後台 — KOL 型錄</title><style>${CSS}</style></head><body>

<div class="bar">
  <h1>素材挑選後台</h1>
  <span class="hint" id="tot"></span>
  <span class="sp"></span>
  <button class="ghost" onclick="location.href='/'">看型錄</button>
  <button class="ghost" id="reset">全部回到預設</button>
  <button id="copy">複製選擇結果</button>
</div>

<div class="wrap">
  <p class="hint" style="padding:16px 0 0">
    點縮圖＝要／不要。<b>右上角「封面」</b>點一下把那張設成這位人設的封面（每人一張）。<br>
    紅字的是程式預設沒挑的，理由寫在上面——<b>你要的話直接勾回來就好</b>。<br>
    選好之後按右上角「複製選擇結果」，把內容貼回給 Claude，型錄就會照你挑的重出。
  </p>
${groups.map(g => `
  <section data-p="${esc(g.id)}">
    <h2>${esc(g.name)}<small>${esc(g.name_zh || '')} · 共 ${g.rows.length} 張</small></h2>
    <p class="cnt" id="c-${esc(g.id)}"></p>
    <div class="grid">
${g.rows.map(r => `      <div class="it${r.on ? ' on' : ''}${r.hero ? ' isHero' : ''}" data-p="${esc(g.id)}" data-rel="${esc(r.rel)}">
        <img src="${r.thumb}" alt="${esc(r.name)}" loading="lazy" width="320" height="427">
        <span class="tick">✓</span><span class="hero" data-hero="1">封面</span>
        ${r.blocked ? `<span class="warn">${esc(r.blocked)}</span>` : ''}
        <span class="n">${esc(r.name)}${r.w ? ` · ${r.w}×${r.h}` : ''}</span>
      </div>`).join('\n')}
    </div>
  </section>`).join('')}
</div>

<div class="dlg" id="dlg"><div class="box">
  <p style="margin:0 0 10px"><b>把下面整段複製，貼回給 Claude。</b></p>
  <textarea id="out" readonly></textarea>
  <p style="margin:12px 0 0;display:flex;gap:10px">
    <button id="cp2">複製到剪貼簿</button>
    <button class="ghost" onclick="document.getElementById('dlg').classList.remove('on')">關閉</button>
  </p>
</div></div>

<script>
(function(){
  var KEY='kolcat-pick-v1';
  var saved={}; try{saved=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){}

  // 還原上次的選擇（如果有）
  if(Object.keys(saved).length){
    document.querySelectorAll('.it').forEach(function(el){
      var p=el.dataset.p, rel=el.dataset.rel, s=saved[p];
      if(!s) return;
      el.classList.toggle('on', (s.gallery||[]).indexOf(rel)>=0);
      el.classList.toggle('isHero', s.hero===rel);
    });
  }

  function collect(){
    var out={};
    document.querySelectorAll('section[data-p]').forEach(function(sec){
      var p=sec.dataset.p, gallery=[], hero=null;
      sec.querySelectorAll('.it').forEach(function(el){
        if(el.classList.contains('on')) gallery.push(el.dataset.rel);
        if(el.classList.contains('isHero')) hero=el.dataset.rel;
      });
      out[p]={hero:hero, gallery:gallery};
    });
    return out;
  }
  function save(){ try{localStorage.setItem(KEY, JSON.stringify(collect()))}catch(e){} }
  function counts(){
    var t=0;
    document.querySelectorAll('section[data-p]').forEach(function(sec){
      var n=sec.querySelectorAll('.it.on').length; t+=n;
      var h=sec.querySelector('.it.isHero');
      document.getElementById('c-'+sec.dataset.p).textContent =
        '已選 '+n+' 張'+(h?'':'　⚠ 還沒選封面');
    });
    document.getElementById('tot').textContent='合計已選 '+t+' 張';
  }

  document.addEventListener('click', function(e){
    var it=e.target.closest('.it'); if(!it) return;
    if(e.target.dataset.hero){
      it.closest('section').querySelectorAll('.it').forEach(function(o){o.classList.remove('isHero')});
      it.classList.add('isHero'); it.classList.add('on');
    } else {
      it.classList.toggle('on');
      if(!it.classList.contains('on')) it.classList.remove('isHero');
    }
    save(); counts();
  });

  document.getElementById('reset').addEventListener('click', function(){
    if(!confirm('把所有人設的選擇清掉，回到程式的預設？')) return;
    localStorage.removeItem(KEY); location.reload();
  });

  document.getElementById('copy').addEventListener('click', function(){
    var payload={note:'KOLCAT 素材挑選結果。貼回給 Claude，它會存成 catalog/data/selection.json 並重出型錄。',
      picked_at:new Date().toISOString().slice(0,16).replace('T',' '), personas:collect()};
    document.getElementById('out').value=JSON.stringify(payload,null,1);
    document.getElementById('dlg').classList.add('on');
  });
  document.getElementById('cp2').addEventListener('click', function(){
    var ta=document.getElementById('out'); ta.select();
    navigator.clipboard.writeText(ta.value).then(
      function(){ this.textContent='已複製 ✓'; }.bind(this),
      function(){ document.execCommand('copy'); }
    );
  });

  counts();
})();
</script>
</body></html>`;

fs.writeFileSync(OUT, html);
const sz = fs.readdirSync(PICK_DIR).reduce((a, d) => a + fs.readdirSync(path.join(PICK_DIR, d)).reduce((b, f) => b + fs.statSync(path.join(PICK_DIR, d, f)).size, 0), 0);
console.log(`\n縮圖 產生 ${made} / 沿用 ${cached} / 失敗 ${failed}，共 ${(sz / 1048576).toFixed(1)} MB`);
console.log(`寫入 ${OUT}（${(fs.statSync(OUT).size / 1024).toFixed(0)} KB）`);
