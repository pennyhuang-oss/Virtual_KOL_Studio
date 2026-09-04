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
 * 2026-09-04 加上影片（使用者：「你先讓我在後台挑選影片」）。
 * 影片母體 170 支、2,511 MB,原檔不進 git 也不上 Railway,所以這一頁給的是：
 *   ・首幀圖（320 寬）
 *   ・**3 秒動態預覽**——從整支的 15%／45%／75% 各取 1 秒接起來,
 *     這樣看得到整支的變化,不是只看得到開頭那一秒。
 * 實測過才定規格：平均 預覽 43.8 KB ＋ 首幀 16.8 KB → 170 支約 10 MB,進 git 沒問題。
 *
 * 用法：node catalog/tools/build_picker.mjs
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const REPO_ROOT = process.env.REPO_ROOT || '/home/user';
const DIR = path.join(import.meta.dirname, '..');
const PICK_DIR = path.join(DIR, 'assets', '_pick');
const OUT = path.join(DIR, 'public', 'pick.html');

const THUMB = { width: 320, q: 70 };
// 影片預覽：3 段 × 1 秒,320 寬,15fps,無聲。取樣點刻意不是 0%——
// 開頭那一秒常常是靜止的首幀,看不出這支在做什麼。
const VPREV = { width: 320, fps: 15, crf: 32, at: [0.15, 0.45, 0.75], segSec: 1, vp9crf: 44 };
// ⚠ 每支預覽同時出 H.264/mp4 與 VP9/webm 兩種,原因是可測性不是相容性：
//   Playwright 內建的 Chromium **完全沒有 H.264**（`canPlayType('video/mp4; codecs="avc1..."')`
//   回空字串,VP8/VP9 回 probably）,所以只出 mp4 的話「滑過會不會播」在這台機器上永遠驗不了
//   ——會變成「我沒測」卻寫成「應該可以」。實測 VP9 CRF 44 = 63 KB,跟 mp4 的 58 KB 差不多。
//   瀏覽器自己挑：給 webm 的挑 webm,舊 Safari 挑 mp4。
const PROBE_CACHE = path.join(DIR, 'data', 'video_probe.json');
let probe = {};
try { probe = JSON.parse(fs.readFileSync(PROBE_CACHE, 'utf8')); } catch {}

const FF = execFileSync('python3', ['-c', 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())'], { encoding: 'utf8' }).trim();
const ff = a => execFileSync(FF, ['-hide_banner', '-nostdin', '-loglevel', 'error', '-y', ...a], { stdio: ['ignore', 'pipe', 'pipe'] });
// ⚠ 探測規格一律用真 ffmpeg 讀,不要自己解 MP4 atom
//   （CLAUDE.md 記過一次：手寫 atom 解析器 offset 算錯,讀成 Baseline/Level 3.0,
//     據此推出一整套錯的根因,真 ffmpeg 一驗是 High profile）。
// ⚠ ffmpeg 對「只有 -i 沒有輸出」會以非 0 結束,而規格印在 stderr,
//   所以一定要在 catch 外面讀 stderr（volumedetect 那次踩過反向的坑）。
const ffInfo = src => {
  let err = '';
  try { execFileSync(FF, ['-hide_banner', '-nostdin', '-i', src], { stdio: ['ignore', 'pipe', 'pipe'] }); }
  catch (e) { err = String(e.stderr || ''); }
  const d = err.match(/Duration:\s*(\d+):(\d\d):(\d\d(?:\.\d+)?)/);
  const v = err.match(/Video:.*?,\s*(\d{2,5})x(\d{2,5})/);
  return {
    sec: d ? (+d[1] * 3600 + +d[2] * 60 + parseFloat(d[3])) : null,
    w: v ? +v[1] : null, h: v ? +v[2] : null,
  };
};

const cat = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'catalog.json'), 'utf8'));
let sel = {};
try { sel = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'selection.json'), 'utf8')).personas || {}; } catch {}

const esc = s => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const id8 = s => { let h = 5381; for (const c of s) h = ((h * 33) ^ c.charCodeAt(0)) >>> 0; return h.toString(36).padStart(7, '0'); };

fs.mkdirSync(PICK_DIR, { recursive: true });

let made = 0, cached = 0, failed = 0;
let vmade = 0, vcached = 0, vfailed = 0;
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
      // 同樣帶內容雜湊，理由見 build_site.mjs 的 vtag 註解
      thumb: `/assets/_pick/${p.id}/${key}.jpg?v=` +
        crypto.createHash('md5').update(fs.readFileSync(out)).digest('hex').slice(0, 10),
      w: it.w, h: it.h, blocked: it.blocked,
      on: currentDefault.includes(it.rel),
      hero: it.rel === currentHero,
    });
  }
  // ── 影片 ──────────────────────────────────────────────────
  // 站上現在的預設是「前 3 支的首幀圖」,所以預設就勾那 3 支,
  // 讓這一頁反映的是現況,不是空白。
  const currentVideos = sel[p.id]?.videos || p.media.videos.slice(0, 3).map(v => v.rel);
  const vrows = [];
  for (const v of p.media.videos) {
    const key = id8(v.rel);
    const src = path.join(REPO_ROOT, v.rel);
    const post = path.join(dir, `${key}_vp.jpg`);
    const prev = path.join(dir, `${key}_vc.mp4`);
    const prevW = path.join(dir, `${key}_vc.webm`);
    if (!fs.existsSync(src)) { vfailed++; continue; }

    if (!probe[v.rel]) probe[v.rel] = ffInfo(src);
    const info = probe[v.rel];
    if (!info.sec) { vfailed++; continue; }

    if (!fs.existsSync(post) || !fs.existsSync(prev)) {
      try {
        ff(['-ss', String(info.sec * VPREV.at[0]), '-i', src, '-frames:v', '1',
            '-vf', `scale=${VPREV.width}:-2`, '-q:v', '6', post]);
        // 三段各自轉好再接起來。⚠ concat 清單裡的相對路徑是相對「清單檔所在目錄」,
        //   不是相對 cwd——寫成 `vtest/x.mp4` 會被找成 `vtest/vtest/x.mp4`（踩過）。
        const segs = VPREV.at.map((frac, i) => {
          const seg = path.join(dir, `${key}_s${i}.mp4`);
          ff(['-ss', String(Math.max(0, info.sec * frac)), '-i', src, '-t', String(VPREV.segSec), '-an',
              '-vf', `scale=${VPREV.width}:-2,fps=${VPREV.fps}`, '-c:v', 'libx264',
              '-crf', String(VPREV.crf), '-preset', 'veryfast', '-pix_fmt', 'yuv420p', seg]);
          return seg;
        });
        const list = path.join(dir, `${key}_list.txt`);
        fs.writeFileSync(list, segs.map(f => `file '${path.basename(f)}'`).join('\n') + '\n');
        ff(['-f', 'concat', '-safe', '0', '-i', list, '-c', 'copy', '-movflags', '+faststart', prev]);
        for (const f of [...segs, list]) fs.rmSync(f, { force: true });
        vmade++;
      } catch { vfailed++; continue; }
    } else vcached++;

    // webm 從已經轉好的 mp4 再轉一次就好,不用回去重切原片
    if (!fs.existsSync(prevW)) {
      try {
        ff(['-i', prev, '-c:v', 'libvpx-vp9', '-crf', String(VPREV.vp9crf), '-b:v', '0',
            '-deadline', 'good', '-cpu-used', '4', '-row-mt', '1', '-an', prevW]);
      } catch { /* webm 轉失敗不擋,mp4 還在 */ }
    }

    const tag = f => `?v=` + crypto.createHash('md5').update(fs.readFileSync(f)).digest('hex').slice(0, 10);
    vrows.push({
      key, rel: v.rel,
      name: v.rel.split('/').slice(3).join('/'),
      poster: `/assets/_pick/${p.id}/${key}_vp.jpg` + tag(post),
      clip: `/assets/_pick/${p.id}/${key}_vc.mp4` + tag(prev),
      clipW: fs.existsSync(prevW) ? `/assets/_pick/${p.id}/${key}_vc.webm` + tag(prevW) : null,
      sec: Math.round(info.sec), w: info.w, h: info.h, mb: v.mb,
      on: currentVideos.includes(v.rel),
    });
  }

  groups.push({ id: p.id, name: p.name, name_zh: p.name_zh, rows, vrows });
  process.stdout.write(`  ${p.name} ${rows.length} 張圖、${vrows.length} 支影片\n`);
}
fs.writeFileSync(PROBE_CACHE, JSON.stringify(probe, null, 1));

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

/* 圖片／影片切換 */
.tabs{display:flex;gap:0;border:1px solid #3a3a44;border-radius:4px;overflow:hidden}
.tabs button{background:transparent;color:#bbb;border:0;border-radius:0;padding:8px 16px;font-weight:400}
.tabs button[aria-pressed=true]{background:#e8c85a;color:#17130a;font-weight:600}
body:not(.m-vid) .gvid,body.m-vid .grid{display:none}

/* 影片卡：首幀 ＋ 滑過／點一下播 3 秒動態預覽 */
.gvid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px}
.vt{position:relative;border:2px solid transparent;border-radius:4px;overflow:hidden;
  background:#1a1a20;cursor:pointer;display:block}
.vt .ph{position:relative;aspect-ratio:9/16;background:#121216}
.vt .ph img,.vt .ph video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  object-position:50% 18%;display:block}
.vt .ph img{opacity:.55;transition:.15s}
.vt .ph video{opacity:0;transition:.15s}
.vt.on .ph img{opacity:1}
.vt.play .ph video{opacity:1}
.vt.on{border-color:#e8c85a}
.vt .tick{position:absolute;top:6px;left:6px;width:21px;height:21px;border-radius:3px;
  background:rgba(0,0,0,.6);border:1.5px solid #777;display:grid;place-items:center;
  font-size:13px;color:transparent;z-index:2}
.vt.on .tick{background:#e8c85a;border-color:#e8c85a;color:#17130a}
.vt .len{position:absolute;top:6px;right:6px;z-index:2;font-size:10px;padding:2px 6px;border-radius:3px;
  background:rgba(0,0,0,.72);color:#ddd;font-variant-numeric:tabular-nums}
.vt .pv{position:absolute;bottom:34px;left:6px;z-index:2;font-size:9.5px;padding:2px 6px;
  border-radius:3px;background:rgba(0,0,0,.72);color:#8ecf8e}
.vt .n{position:absolute;left:0;right:0;bottom:0;z-index:2;
  background:linear-gradient(transparent,rgba(0,0,0,.94));
  padding:16px 7px 5px;font-size:10px;line-height:1.35;color:#ddd;word-break:break-all}
`;

const html = `<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>素材挑選後台 — KOL 型錄</title><style>${CSS}</style></head><body>

<div class="bar">
  <h1>素材挑選後台</h1>
  <span class="tabs">
    <button data-mode="img" aria-pressed="true">圖片</button>
    <button data-mode="vid" aria-pressed="false">影片</button>
  </span>
  <span class="hint" id="tot"></span>
  <span class="sp"></span>
  <button class="ghost" onclick="location.href='/'">看型錄</button>
  <button class="ghost" id="reset">全部回到預設</button>
  <button id="copy">複製選擇結果</button>
</div>

<div class="wrap">
  <p class="hint" style="padding:16px 0 0" id="help-img">
    點縮圖＝要／不要。<b>右上角「封面」</b>點一下把那張設成這位人設的封面（每人一張）。<br>
    紅字的是程式預設沒挑的，理由寫在上面——<b>你要的話直接勾回來就好</b>。<br>
    選好之後按右上角「複製選擇結果」，把內容貼回給 Claude，型錄就會照你挑的重出。
  </p>
  <p class="hint" style="padding:16px 0 0" id="help-vid">
    <b>滑過（手機是點一下）就會播 3 秒預覽</b>——那 3 秒是從整支的 15%／45%／75% 各取 1 秒接起來的，
    所以看得到整支的變化，不是只看得到開頭。<b>點左上角的方框＝要／不要。</b><br>
    右上角是這支的長度，底下是檔名與原始尺寸。目前預設勾的是站上現在用的那幾支。<br>
    ⚠ 這裡放的是壓過的預覽，不是原片。<b>挑好之後我才會把你挑的那幾支轉成網頁播放用的檔案</b>——
    170 支全部轉多半是白轉。
  </p>
${groups.map(g => `
  <section data-p="${esc(g.id)}">
    <h2>${esc(g.name)}<small>${esc(g.name_zh || '')} · ${g.rows.length} 張圖 · ${g.vrows.length} 支影片</small></h2>
    <p class="cnt" id="c-${esc(g.id)}"></p>
    <div class="gvid">
${g.vrows.length ? g.vrows.map(v => `      <div class="vt${v.on ? ' on' : ''}" data-p="${esc(g.id)}" data-rel="${esc(v.rel)}">
        <div class="ph">
          <img src="${v.poster}" alt="${esc(v.name)}" loading="lazy" width="320" height="569">
          <video muted loop playsinline preload="none">
            ${v.clipW ? `<source src="${v.clipW}" type="video/webm">` : ''}
            <source src="${v.clip}" type="video/mp4">
          </video>
        </div>
        <span class="tick">✓</span>
        <span class="len">${Math.floor(v.sec / 60)}:${String(v.sec % 60).padStart(2, '0')}</span>
        <span class="pv">預覽 3 秒</span>
        <span class="n">${esc(v.name)}${v.w ? ` · ${v.w}×${v.h} · ${v.mb} MB` : ''}</span>
      </div>`).join('\n') : '      <p class="hint">這位人設沒有影片素材。</p>'}
    </div>
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
  var KEY='kolcat-pick-v2';
  var saved={}; try{saved=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){}
  // v1 只存圖片。沿用它的圖片選擇,影片就照頁面上的預設值。
  if(!Object.keys(saved).length){
    try{ saved=JSON.parse(localStorage.getItem('kolcat-pick-v1')||'{}') }catch(e){}
  }

  // 還原上次的選擇（如果有）。⚠ 只有 v2 才動影片——
  //   v1 沒有 videos 欄位,若拿 undefined 去比對會把預設的三支全部取消掉。
  if(Object.keys(saved).length){
    document.querySelectorAll('.it').forEach(function(el){
      var s=saved[el.dataset.p]; if(!s) return;
      el.classList.toggle('on', (s.gallery||[]).indexOf(el.dataset.rel)>=0);
      el.classList.toggle('isHero', s.hero===el.dataset.rel);
    });
    document.querySelectorAll('.vt').forEach(function(el){
      var s=saved[el.dataset.p]; if(!s || !s.videos) return;
      el.classList.toggle('on', s.videos.indexOf(el.dataset.rel)>=0);
    });
  }

  // ── 圖片／影片切換 ──
  var mode='img';
  try{ mode=localStorage.getItem('kolcat-pick-mode')||'img' }catch(e){}
  function setMode(m){
    mode=m;
    document.body.classList.toggle('m-vid', m==='vid');
    document.querySelectorAll('.tabs button').forEach(function(b){
      b.setAttribute('aria-pressed', String(b.dataset.mode===m)); });
    document.getElementById('help-img').hidden = (m!=='img');
    document.getElementById('help-vid').hidden = (m!=='vid');
    try{ localStorage.setItem('kolcat-pick-mode', m) }catch(e){}
    counts();
  }
  document.querySelectorAll('.tabs button').forEach(function(b){
    b.addEventListener('click', function(){ setMode(b.dataset.mode); });
  });

  function collect(){
    var out={};
    document.querySelectorAll('section[data-p]').forEach(function(sec){
      var p=sec.dataset.p, gallery=[], hero=null;
      sec.querySelectorAll('.it').forEach(function(el){
        if(el.classList.contains('on')) gallery.push(el.dataset.rel);
        if(el.classList.contains('isHero')) hero=el.dataset.rel;
      });
      var videos=[];
      sec.querySelectorAll('.vt.on').forEach(function(el){ videos.push(el.dataset.rel); });
      out[p]={hero:hero, gallery:gallery, videos:videos};
    });
    return out;
  }
  function save(){ try{localStorage.setItem(KEY, JSON.stringify(collect()))}catch(e){} }
  function counts(){
    var t=0;
    document.querySelectorAll('section[data-p]').forEach(function(sec){
      var el=document.getElementById('c-'+sec.dataset.p);
      if(mode==='vid'){
        var v=sec.querySelectorAll('.vt.on').length,
            all=sec.querySelectorAll('.vt').length;
        t+=v;
        el.textContent = all ? ('已選 '+v+' / '+all+' 支影片') : '沒有影片素材';
      } else {
        var n=sec.querySelectorAll('.it.on').length; t+=n;
        el.textContent='已選 '+n+' 張'+(sec.querySelector('.it.isHero')?'':'　⚠ 還沒選封面');
      }
    });
    document.getElementById('tot').textContent =
      '合計已選 '+t+(mode==='vid'?' 支影片':' 張圖');
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

  // 影片：點一下＝要／不要
  document.addEventListener('click', function(e){
    var vt=e.target.closest('.vt'); if(!vt) return;
    vt.classList.toggle('on'); save(); counts();
  });

  // 滑過就播那 3 秒。preload="none" 所以在滑到之前不會下載任何影片,
  // 而且一次只播一支——170 支同時播會把瀏覽器拖垮。
  var playing=null;
  function stopPlaying(){
    if(!playing) return;
    var v=playing.querySelector('video');
    try{ v.pause(); v.currentTime=0 }catch(e){}
    playing.classList.remove('play'); playing=null;
  }
  function startPlaying(vt){
    if(playing===vt) return;
    stopPlaying();
    var v=vt.querySelector('video'); if(!v) return;
    playing=vt; vt.classList.add('play');
    v.play().catch(function(){ /* 使用者還沒互動過就被擋,不是錯誤 */ });
  }
  document.addEventListener('pointerover', function(e){
    var vt=e.target.closest('.vt'); if(vt) startPlaying(vt);
  });
  document.addEventListener('pointerout', function(e){
    var vt=e.target.closest('.vt');
    if(vt && vt===playing && !vt.contains(e.relatedTarget)) stopPlaying();
  });
  // 手機沒有滑過,點一下就播（勾選由上面那個 click 處理,兩件事同時發生沒關係）
  document.addEventListener('touchstart', function(e){
    var vt=e.target.closest('.vt'); if(vt) startPlaying(vt);
  }, {passive:true});

  document.getElementById('reset').addEventListener('click', function(){
    if(!confirm('把所有人設的選擇清掉，回到程式的預設？')) return;
    localStorage.removeItem(KEY); location.reload();
  });

  document.getElementById('copy').addEventListener('click', function(){
    var payload={note:'KOLCAT 素材挑選結果（圖片 ＋ 影片）。貼回給 Claude，它會存成 catalog/data/selection.json 並重出型錄。',
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

  setMode(mode);
})();
</script>
</body></html>`;

fs.writeFileSync(OUT, html);
const sz = fs.readdirSync(PICK_DIR).reduce((a, d) => a + fs.readdirSync(path.join(PICK_DIR, d)).reduce((b, f) => b + fs.statSync(path.join(PICK_DIR, d, f)).size, 0), 0);
console.log(`\n圖片縮圖 產生 ${made} / 沿用 ${cached} / 失敗 ${failed}`);
console.log(`影片預覽 產生 ${vmade} / 沿用 ${vcached} / 失敗 ${vfailed}`);
console.log(`_pick 總大小 ${(sz / 1048576).toFixed(1)} MB`);
console.log(`  可挑：${groups.reduce((a, g) => a + g.rows.length, 0)} 張圖、` +
  `${groups.reduce((a, g) => a + g.vrows.length, 0)} 支影片`);
console.log(`寫入 ${OUT}（${(fs.statSync(OUT).size / 1024).toFixed(0)} KB）`);
