// 2027 KOL 桌曆｜選片頁（shoot.html）。M-4 R22 為第三輪：上方集中本輪待確認項目（新候選 A／B、改善候選、修正版比較），
// 每項附前幾輪的照片（只看不選）；下方「已選」區只看不選。資料來自 pick-data.js（產生自 data/cal_pick_r22.json）。
// 每項的回饋存在這台裝置的瀏覽器，識別鍵 cal2027-pick-r22-v1:<套別>，內容記下當時看的圖片識別（img_id）；圖片識別對不上就不套用。
// 只讀寫這個前綴；前幾輪 cal2027-pick-r20-v1:…、cal2027-pick-r21-v1:… 與其他舊鍵（cal2027-batch1-v1:…、cal2027-review-v1:…、企劃與素材頁的鍵）不讀、不寫、不刪。
// 未回覆不算接受。沒有追蹤或分析，回饋不會自動送出。
'use strict';
(() => {
  const K = window.CAL_PICK;
  const app = document.getElementById('app');
  if (!K || !K.items || !K.items.length) { app.textContent = '資料載入失敗。'; return; }

  const $ = (s, r = document) => r.querySelector(s);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const ITEMS = K.items, SEL = K.selected || [], PEND = K.pending || [];
  const BOOKS = [['H', '橫式'], ['V', '直式']];
  const label = s => `${s.book_zh} ${s.month} 月｜${s.name}`;
  const KIND_TAG = { ab: '新候選', improve: '改善候選', grade: '修正版比較' };

  // 每一項顯示的照片與選項
  const photos = it => it.kind === 'ab' ? it.candidates : it.kind === 'improve' ? [it.original, ...it.candidates] : [it.original, it.graded];
  const shown = it => photos(it).filter(p => !p.missing);
  function options(it) {
    if (it.kind === 'improve') return [['keep', `保留 ${it.original.v}`], ['1', '改用新候選 1'], ['2', '改用新候選 2'], ['edit', '仍想修改']];
    if (it.kind === 'grade') return [['graded', `用${it.graded.v}`], ['orig', '維持原版'], ['edit', '還想修改']];
    const ok = it.candidates.filter(c => !c.missing);
    return [...ok.map(c => [c.v, `接受 ${c.v}`]), ['edit', ok.length > 1 ? '兩張都想修改' : '想修改']];
  }
  const optText = (it, v) => (options(it).find(o => o[0] === v) || [, ''])[1];
  function picked(it, v) {   // 選擇對應的圖片識別（複製回饋用）
    if (it.kind === 'ab') { const c = it.candidates.find(x => x.v === v); return c ? [c.img_id] : shown(it).map(p => p.img_id); }
    if (it.kind === 'improve') return v === 'keep' ? [it.original.img_id] : v === '1' || v === '2' ? [it.candidates[+v - 1].img_id] : shown(it).map(p => p.img_id);
    return v === 'graded' ? [it.graded.img_id] : v === 'orig' ? [it.original.img_id] : shown(it).map(p => p.img_id);
  }

  // ---------- 回饋：一項一個鍵；記下圖片識別，對不上就視為未回覆 ----------
  let storeOk = true;
  const keyOf = it => K.key_prefix + it.set;
  const ids = it => shown(it).map(p => p.img_id);
  function load(it) {
    try {
      const raw = localStorage.getItem(keyOf(it));
      if (!raw) return null;
      const o = JSON.parse(raw);
      if (!o || typeof o !== 'object') return null;
      if (!Array.isArray(o.imgs) || o.imgs.join('|') !== ids(it).join('|')) return { stale: true, v: '', note: '', at: '' };
      return { v: optText(it, o.v) ? o.v : '', note: typeof o.note === 'string' ? o.note : '', at: o.at || '' };
    } catch (e) { return null; }
  }
  function save(it, v, note) {
    try {
      if (!v && !note.trim()) localStorage.removeItem(keyOf(it));  // 只清本頁這一項自己的鍵（沒選也沒備註）
      else localStorage.setItem(keyOf(it), JSON.stringify({ v, note, imgs: ids(it), at: new Date().toISOString(), round: K.round, page: PAGE_COMMIT }));
      storeOk = true;
    } catch (e) { storeOk = false; }
  }
  const fb = it => load(it) || { v: '', note: '', at: '' };
  const stCls = v => `st ${!v ? 'none' : v === 'edit' ? 'edit' : 'accept'}`;
  const stText = (it, v) => v ? optText(it, v) : '未回覆';

  // ---------- 目前這一項 ----------
  const idx = sid => ITEMS.findIndex(s => s.set === sid);
  let cur = Math.max(0, idx(decodeURIComponent(location.hash.slice(1))));

  function navHtml() {
    const book = ITEMS[cur].book;
    const tabs = BOOKS.map(([b, zh]) => {
      const n = ITEMS.filter(s => s.book === b);
      return `<button type="button" class="tab${b === book ? ' on' : ''}" data-book="${b}"${b === book ? ' aria-current="true"' : ''}>${zh}<span>${n.filter(s => fb(s).v).length}／${n.length} 已回覆</span></button>`;
    }).join('');
    const months = [];
    for (let m = 1; m <= 12; m++) {
      const it = ITEMS.find(x => x.book === book && x.month === m);
      if (it) {
        const i = ITEMS.indexOf(it), v = fb(it).v;
        months.push(`<li><button type="button" class="pn-b${i === cur ? ' on' : ''}" data-go="${i}"${i === cur ? ' aria-current="true"' : ''}><b>${m} 月</b><span>${esc(it.name)}</span><i class="${stCls(v)}">${esc(stText(it, v))}</i></button></li>`);
        continue;
      }
      const s = SEL.find(x => x.book === book && x.month === m), p = PEND.find(x => x.book === book && x.month === m);
      if (s) months.push(`<li><a class="pn-b other" href="#sel"><b>${m} 月</b><span>${esc(s.name)}</span><i class="st done">已選</i></a></li>`);
      else if (p) months.push(`<li><a class="pn-b other" href="#pend"><b>${m} 月</b><span>${esc(p.name)}</span><i class="st wait">待處理</i></a></li>`);
    }
    return `<nav class="pn" aria-label="本輪待確認：依橫式／直式、月份與角色選一項"><div class="tabs">${tabs}</div><ol>${months.join('')}</ol></nav>`;
  }

  const fig = (it, p, k) => p.missing
    ? `<figure class="cand miss"><div class="missbox"><span class="ab">${esc(p.v)}</span><p>${esc(p.missing_label)}</p></div><figcaption><b class="ab-t">${esc(p.v)}</b>　沒有這張</figcaption></figure>`
    : `<figure class="cand"><button type="button" class="zoom" data-img="${k}" aria-label="放大 ${esc(p.v)}：${esc(label(it))}">` +
      `<img src="${esc(p.img.view.src)}" width="${p.img.view.w}" height="${p.img.view.h}" alt="${esc(label(it))} ${esc(p.v)}"><span class="ab">${esc(p.v)}</span></button>` +
      `<figcaption><b class="ab-t">${esc(p.v)}</b>　圖片 ${esc(p.img_id)}　<button type="button" class="lnk" data-img="${k}">看大圖</button></figcaption></figure>`;

  function render() {
    const it = ITEMS[cur], f = fb(it);
    document.title = `${label(it)}｜選片｜2027 KOL 桌曆`;
    const ph = photos(it);
    const hint = it.hint ? `<p class="note">${esc(it.hint)}</p>` : '';
    const past = it.history || [];
    app.innerHTML = `${navHtml()}
<section class="sec set" id="set" aria-label="${esc(label(it))}">
<h2>${esc(label(it))}<span class="kind">${KIND_TAG[it.kind]}</span><i class="${stCls(f.v)}" id="set-st">${esc(stText(it, f.v))}</i></h2>
${hint}
<div class="abpair abpair-${it.book} n${ph.length}">${ph.map((p, k) => fig(it, p, k)).join('')}</div>
<div class="ch" role="radiogroup" aria-label="這一項的選擇">
${options(it).map(([v, t]) => `<label class="opt"><input type="radio" name="fb-v" value="${v}"${f.v === v ? ' checked' : ''}> ${esc(t)}</label>`).join('\n')}
<button type="button" class="btn ghost sm" id="fb-clear"${f.v ? '' : ' disabled'}>清除選擇（改回未回覆）</button>
</div>
${past.length ? `<details class="past"><summary>前幾輪的照片（${past.length} 張，只看不選）</summary><div class="pgrid pgrid-${it.book}">${past.map((p, k) => `<figure class="pc"><button type="button" class="zoom" data-img="h${k}" aria-label="放大 ${esc(p.v)}：${esc(label(it))}"><img src="${esc(p.img.view.src)}" width="${p.img.view.w}" height="${p.img.view.h}" alt="${esc(label(it))} ${esc(p.v)}" loading="lazy"></button><figcaption>${esc(p.v)}</figcaption></figure>`).join('')}</div></details>` : ''}
<label class="nl" for="fb-note">備註（具體想改哪裡、或任何意見；可留空）</label>
<textarea id="fb-note" rows="3" maxlength="2000">${esc(f.note)}</textarea>
<p class="note" id="fb-saved" aria-live="polite">${savedText(f)}</p>
<p class="acts"><button type="button" class="btn ghost" data-go="${cur - 1}"${cur ? '' : ' disabled'}>← 上一項</button><button type="button" class="btn ghost" data-go="${cur + 1}"${cur < ITEMS.length - 1 ? '' : ' disabled'}>下一項 →</button></p>
</section>
<section class="sec" id="copy"><h2>全部回饋（本輪 ${ITEMS.length} 項）</h2>
<p class="td-h" id="cp-sum"></p>
<p class="acts"><button type="button" class="btn" id="cp-btn">複製全部回饋</button></p>
<p class="note" id="cp-msg" aria-live="polite">${esc(K.store_note)}</p>
<textarea id="cp-text" rows="8" readonly aria-label="全部回饋文字"></textarea>
</section>
<section class="sec" id="sel"><h2>已選（${SEL.length} 套，不用重選）</h2>
${K.sel_note ? `<p class="td-h">${esc(K.sel_note)}</p>` : ''}
<div class="accs">${SEL.map((s, i) => { const p = s.img || (refOf(s.img_ref) || {}).img; return `<figure class="acc"><button type="button" class="zoom" data-img="sel${i}" aria-label="放大：${esc(label(s))}"><img src="${esc(p.view.src)}" width="${p.view.w}" height="${p.view.h}" alt="${esc(label(s))}" loading="lazy"></button>
<figcaption><b>${esc(label(s))}</b><br><span class="${s.edit_pending ? 'pendtag' : 'ok'}">${esc(s.label)}</span></figcaption></figure>`; }).join('')}</div>
</section>
${PEND.length ? `<section class="sec" id="pend"><h2>待處理</h2>
${PEND.map(p => `<p class="td-h"><b>${esc(label(p))}</b>｜${esc(p.v)}</p>`).join('')}
</section>` : ''}
<section class="sec hist"><h2><a href="${esc(K.history.href)}">${esc(K.history.label)} →</a></h2></section>`;
    updateCopy();
  }
  function refOf(imgId) {
    for (const it of ITEMS) for (const p of photos(it)) if (p.img_id === imgId && p.img) return p;
    return null;
  }

  function savedText(f) {
    if (!storeOk) return '這個瀏覽器不允許儲存；請在看完後直接按「複製全部回饋」。';
    if (f && f.stale) return '先前的回覆對應的是別的圖片，已不套用；這一項目前未回覆。';
    if (!f || (!f.v && !f.note)) return '還沒回覆（未回覆不算接受）。';
    const t = f.at ? new Date(f.at) : null;
    return `已存在這台裝置的瀏覽器${t && !isNaN(t) ? `（${t.toLocaleString('zh-TW', { hour12: false })}）` : ''}。${f.v ? '' : '尚未選擇，目前不算接受。'}`;
  }

  // ---------- 全部複製：未回覆不算接受 ----------
  function allText() {
    let done = 0;
    const lines = [];
    for (const [b, zh] of BOOKS) {
      lines.push(`【${zh}】`);
      ITEMS.filter(s => s.book === b).forEach(it => {
        const f = fb(it);
        if (f.v) done++;
        const pick = f.v ? `${optText(it, f.v)}（圖片 ${picked(it, f.v).join('、')}）` : `未回覆（不算接受；圖片 ${ids(it).join('、')}）`;
        const head = `${it.month} 月｜${it.name}｜${it.set}｜${KIND_TAG[it.kind]}：${pick}`;
        lines.push(f.note.trim() ? `${head}\n   備註：${f.note.trim().replace(/\s*\n\s*/g, '／')}` : head);
      });
    }
    const head = `${K.task}｜${K.round} 選片回饋（頁面版本 ${PAGE_COMMIT ? PAGE_COMMIT.slice(0, 7) : '本機預覽'}）`;
    const sum = `合計本輪 ${ITEMS.length} 項：已回覆 ${done}、未回覆 ${ITEMS.length - done}（未回覆不算接受）。已選 ${SEL.length} 套不在本次回饋內。`;
    return { done, text: [head, ...lines, sum].join('\n') };
  }
  function updateCopy() {
    const { done, text } = allText();
    $('#cp-sum').textContent = `已回覆 ${done}／${ITEMS.length}，未回覆 ${ITEMS.length - done}`;
    $('#cp-text').value = text;
    $('#prog').textContent = `本輪待確認：已回覆 ${done}／${ITEMS.length} 項（未回覆不算接受）`;
  }
  function copyAll() {
    const { text } = allText();
    const msg = $('#cp-msg'), ta = $('#cp-text');
    ta.value = text;
    const fallback = () => {
      ta.focus(); ta.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      msg.textContent = ok ? '已複製。' : '無法自動複製：文字已選取，請長按或按 Ctrl+C 複製。';
    };
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(() => { msg.textContent = '已複製。'; }, fallback);
    else fallback();
  }

  function onChoice(clear) {
    const it = ITEMS[cur];
    if (clear) app.querySelectorAll('input[name="fb-v"]').forEach(r => { r.checked = false; });
    const v = (app.querySelector('input[name="fb-v"]:checked') || {}).value || '';
    save(it, v, $('#fb-note').value);
    const f = fb(it);
    $('#fb-saved').textContent = savedText(f);
    $('#fb-clear').disabled = !f.v;
    const h = $('#set-st'); h.className = stCls(f.v); h.textContent = stText(it, f.v);
    const b = app.querySelector(`.pn-b[data-go="${cur}"] .st`); if (b) { b.className = stCls(f.v); b.textContent = stText(it, f.v); }
    const tab = app.querySelector(`.tab[data-book="${it.book}"] span`);
    if (tab) { const all = ITEMS.filter(x => x.book === it.book); tab.textContent = `${all.filter(x => fb(x).v).length}／${all.length} 已回覆`; }
    updateCopy();
  }

  function go(i, focusNav) {
    if (i < 0 || i >= ITEMS.length || i === cur) return;
    cur = i;
    try { history.replaceState(history.state, '', '#' + encodeURIComponent(ITEMS[cur].set)); } catch (e) { /* 只是記住目前這一項 */ }
    render();
    const nav = app.querySelector('.pn');
    if (nav && nav.getBoundingClientRect().top < 0) nav.scrollIntoView({ block: 'start' });
    if (focusNav) { const b = app.querySelector('.pn-b.on'); if (b) b.focus({ preventScroll: true }); }
  }

  // ---------- 放大檢視：先看顯示版，「原尺寸」改看完整版；同一項的照片可依序切換 ----------
  const viewer = $('#viewer'), vimg = $('#viewer-img'), vcap = $('#viewer-cap'), vmode = $('#viewer-mode'), vother = $('#viewer-other');
  let vk = null, lastBtn = null, pushed = false;
  function views(key) {
    const it = ITEMS[cur];
    const m = /^sel(\d+)$/.exec(key || '');
    if (m) { const s = SEL[+m[1]]; const p = s && (s.img ? s : refOf(s.img_ref)); return p ? [p.img.view, p.img.full, `${label(s)}｜${s.label}`] : null; }
    const h = /^h(\d+)$/.exec(key || '');
    if (h) { const p = (it.history || [])[+h[1]]; return p ? [p.img.view, p.img.full, `${label(it)}｜前幾輪：${p.v}`] : null; }
    const p = photos(it)[+key];
    return p && !p.missing ? [p.img.view, p.img.full, `${label(it)}｜${p.v}（圖片 ${p.img_id}）`] : null;
  }
  function setImg(m) { vimg.src = m.src; vimg.width = m.w; vimg.height = m.h; }
  function nextKey(key) {
    const ph = photos(ITEMS[cur]);
    for (let d = 1; d < ph.length; d++) { const k = (+key + d) % ph.length; if (!ph[k].missing) return String(k); }
    return null;
  }
  function show(key, nat) {
    const v = views(key);
    if (!v) return false;
    vk = key;
    setImg(nat ? v[1] : v[0]);
    vimg.alt = v[2];
    const m = nat ? v[1] : v[0];
    vcap.textContent = `${v[2]}｜${nat ? '原尺寸' : '顯示'} ${m.w}×${m.h} px` + (nat ? '' : '；按「原尺寸」看完整解析度');
    viewer.classList.toggle('natural', nat);
    vmode.textContent = nat ? '符合畫面' : '原尺寸';
    const nk = /^\d+$/.test(key) ? nextKey(key) : null;
    vother.hidden = nk === null;
    if (nk !== null) vother.textContent = `看${photos(ITEMS[cur])[+nk].v} →`;
    return true;
  }
  function openViewer(key, btn) {
    if (!show(key, false)) return;
    lastBtn = btn;
    viewer.hidden = false;
    document.documentElement.classList.add('noscroll');
    try { history.pushState({ viewer: 1 }, ''); pushed = true; } catch (e) { pushed = false; }
    $('#viewer-close').focus({ preventScroll: true });
  }
  function closeViewer(fromPop) {
    if (viewer.hidden) return;
    viewer.hidden = true;
    vimg.removeAttribute('src');
    document.documentElement.classList.remove('noscroll');
    if (pushed && !fromPop) { pushed = false; history.back(); }
    pushed = false;
    if (lastBtn && document.body.contains(lastBtn)) lastBtn.focus({ preventScroll: true });
  }
  function toggleMode(ev) {
    const nat = !viewer.classList.contains('natural');
    const body = $('#viewer-body');
    let fx = 0.5, fy = 0.5;
    if (ev && ev.target === vimg) { const r = vimg.getBoundingClientRect(); fx = (ev.clientX - r.left) / r.width; fy = (ev.clientY - r.top) / r.height; }
    show(vk, nat);
    if (nat) { body.scrollLeft = Math.max(0, fx * vimg.width - body.clientWidth / 2); body.scrollTop = Math.max(0, fy * vimg.height - body.clientHeight / 2); }
  }

  app.addEventListener('click', e => {
    const t = e.target.closest('[data-book]');
    if (t) { if (ITEMS[cur].book !== t.dataset.book) go(ITEMS.findIndex(s => s.book === t.dataset.book), true); return; }
    const g = e.target.closest('[data-go]');
    if (g && !g.disabled) { go(+g.dataset.go, g.classList.contains('pn-b')); return; }
    if (e.target.closest('#cp-btn')) { copyAll(); return; }
    if (e.target.closest('#fb-clear')) { onChoice(true); return; }
    const z = e.target.closest('[data-img]');
    if (z) openViewer(z.dataset.img, z);
  });
  app.addEventListener('change', e => { if (e.target.name === 'fb-v') onChoice(false); });
  let tmr = 0;
  app.addEventListener('input', e => { if (e.target.id === 'fb-note') { clearTimeout(tmr); tmr = setTimeout(() => onChoice(false), 400); } });
  app.addEventListener('focusout', e => { if (e.target.id === 'fb-note') { clearTimeout(tmr); onChoice(false); } });
  $('#viewer-close').addEventListener('click', () => closeViewer(false));
  vmode.addEventListener('click', () => toggleMode(null));
  vother.addEventListener('click', () => { const nk = /^\d+$/.test(vk || '') ? nextKey(vk) : null; if (nk !== null) show(nk, viewer.classList.contains('natural')); });
  vimg.addEventListener('click', toggleMode);
  window.addEventListener('popstate', () => closeViewer(true));
  window.addEventListener('hashchange', () => { const i = idx(decodeURIComponent(location.hash.slice(1))); if (i >= 0 && i !== cur) { cur = -1; go(i, false); } });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeViewer(false); });
  window.addEventListener('storage', e => { if (e.key && e.key.startsWith(K.key_prefix)) render(); });

  $('#tline').textContent = `${K.task}｜${K.round}`;
  $('#title').textContent = K.title;
  $('#intro').textContent = K.intro;
  $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
  render();
})();
