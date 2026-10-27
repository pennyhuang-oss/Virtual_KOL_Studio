// 2027 KOL 桌曆｜選片頁（shoot.html，M-4 R20 起）：每套 A、B 兩張候選，一次看一套。資料來自 pick-data.js（產生自 data/cal_pick_r20.json）。
// 每套的回饋存在這台裝置的瀏覽器，識別鍵 cal2027-pick-r20-v1:<套別>，內容記下當時看的圖片識別（img_id）；圖片識別對不上就不套用（不把舊圖的選擇套到新圖）。
// 只讀寫這個前綴；其他鍵（M-4 R5 的 cal2027-batch1-v1:…、M-4 R3 的 cal2027-review-v1:…、企劃與素材頁的鍵）不讀、不寫、不刪。
// 未回覆不算接受。沒有追蹤或分析，回饋不會自動送出。
'use strict';
(() => {
  const K = window.CAL_PICK;
  const app = document.getElementById('app');
  if (!K || !K.sets || !K.sets.length) { app.textContent = '資料載入失敗。'; return; }

  const $ = (s, r = document) => r.querySelector(s);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const SETS = K.sets, ACC = K.accepted || [], PEND = K.pending || [];
  const BOOKS = [['H', '橫式'], ['V', '直式']];
  const CHOICE = { A: '接受 A', B: '接受 B', edit: '兩張都想修改' };
  const label = s => `${s.book_zh} ${s.month} 月｜${s.name}`;

  // ---------- 回饋：一套一個鍵；記下圖片識別，對不上就視為未回覆 ----------
  let storeOk = true;
  const keyOf = s => K.key_prefix + s.set;
  const ids = s => s.candidates.map(c => c.img_id);
  function load(s) {
    try {
      const raw = localStorage.getItem(keyOf(s));
      if (!raw) return null;
      const o = JSON.parse(raw);
      if (!o || typeof o !== 'object') return null;
      const [a, b] = ids(s);
      if (o.imgA !== a || o.imgB !== b) return { stale: true, v: '', note: '', at: '' };
      return { v: CHOICE[o.v] ? o.v : '', note: typeof o.note === 'string' ? o.note : '', at: o.at || '' };
    } catch (e) { return null; }
  }
  function save(s, v, note) {
    const [a, b] = ids(s);
    try {
      if (!v && !note.trim()) localStorage.removeItem(keyOf(s));  // 只清本頁這一套自己的鍵（沒選也沒備註）
      else localStorage.setItem(keyOf(s), JSON.stringify({ v, note, imgA: a, imgB: b, at: new Date().toISOString(), round: K.round, page: PAGE_COMMIT }));
      storeOk = true;
    } catch (e) { storeOk = false; }
  }
  const fb = s => load(s) || { v: '', note: '', at: '' };
  const stateOf = s => fb(s).v;

  // ---------- 目前這一套 ----------
  const idx = sid => SETS.findIndex(s => s.set === sid);
  const byHash = () => Math.max(0, idx(decodeURIComponent(location.hash.slice(1))));
  let cur = byHash();

  function navHtml() {
    const book = SETS[cur].book;
    const tabs = BOOKS.map(([b, zh]) => {
      const n = SETS.filter(s => s.book === b);
      const done = n.filter(s => stateOf(s)).length;
      return `<button type="button" class="tab${b === book ? ' on' : ''}" data-book="${b}"${b === book ? ' aria-current="true"' : ''}>${zh}<span>${done}／${n.length} 已回覆</span></button>`;
    }).join('');
    const months = [];
    for (let m = 1; m <= 12; m++) {
      const s = SETS.find(x => x.book === book && x.month === m);
      if (s) {
        const i = SETS.indexOf(s), st = stateOf(s);
        months.push(`<li><button type="button" class="pn-b${i === cur ? ' on' : ''}" data-go="${i}"${i === cur ? ' aria-current="true"' : ''}><b>${m} 月</b><span>${esc(s.name)}</span><i class="st ${st ? (st === 'edit' ? 'edit' : 'accept') : 'none'}">${st ? CHOICE[st] : '未回覆'}</i></button></li>`);
        continue;
      }
      const a = ACC.find(x => x.book === book && x.month === m), p = PEND.find(x => x.book === book && x.month === m);
      if (a) months.push(`<li><a class="pn-b other" href="#acc"><b>${m} 月</b><span>${esc(a.name)}</span><i class="st done">已接受</i></a></li>`);
      else if (p) months.push(`<li><a class="pn-b other" href="#pend"><b>${m} 月</b><span>${esc(p.name)}</span><i class="st wait">待處理</i></a></li>`);
    }
    return `<nav class="pn" aria-label="依橫式／直式、月份與角色選一套"><div class="tabs">${tabs}</div><ol>${months.join('')}</ol></nav>`;
  }

  const fig = (s, c) =>
    `<figure class="cand cand-${c.v}"><button type="button" class="zoom" data-img="${c.v}" aria-label="放大 ${c.v}：${esc(label(s))}">` +
    `<img src="${esc(c.img.view.src)}" width="${c.img.view.w}" height="${c.img.view.h}" alt="${esc(label(s))} 候選 ${c.v}"><span class="ab">${c.v}</span></button>` +
    `<figcaption><b class="ab-t">${c.v}</b>　圖片 ${esc(c.img_id)}　<button type="button" class="lnk" data-img="${c.v}">看大圖</button></figcaption></figure>`;

  function render() {
    const s = SETS[cur], f = fb(s);
    document.title = `${label(s)}｜選片｜2027 KOL 桌曆`;
    app.innerHTML = `${navHtml()}
<section class="sec set" id="set" aria-label="${esc(label(s))}">
<h2>${esc(label(s))}<i class="st ${f.v ? (f.v === 'edit' ? 'edit' : 'accept') : 'none'}" id="set-st">${f.v ? CHOICE[f.v] : '未回覆'}</i></h2>
<div class="abpair abpair-${s.book}">${s.candidates.map(c => fig(s, c)).join('')}</div>
<div class="ch" role="radiogroup" aria-label="這一套的選擇">
${['A', 'B', 'edit'].map(v => `<label class="opt"><input type="radio" name="fb-v" value="${v}"${f.v === v ? ' checked' : ''}> ${CHOICE[v]}</label>`).join('\n')}
<button type="button" class="btn ghost sm" id="fb-clear"${f.v ? '' : ' disabled'}>清除選擇（改回未回覆）</button>
</div>
<label class="nl" for="fb-note">備註（具體想改哪裡、或任何意見；可留空）</label>
<textarea id="fb-note" rows="3" maxlength="2000">${esc(f.note)}</textarea>
<p class="note" id="fb-saved" aria-live="polite">${savedText(f)}</p>
<p class="acts"><button type="button" class="btn ghost" data-go="${cur - 1}"${cur ? '' : ' disabled'}>← 上一套</button><button type="button" class="btn ghost" data-go="${cur + 1}"${cur < SETS.length - 1 ? '' : ' disabled'}>下一套 →</button></p>
</section>
<section class="sec" id="copy"><h2>全部回饋（${SETS.length} 套）</h2>
<p class="td-h" id="cp-sum"></p>
<p class="acts"><button type="button" class="btn" id="cp-btn">複製全部回饋</button></p>
<p class="note" id="cp-msg" aria-live="polite">${esc(K.store_note)}</p>
<textarea id="cp-text" rows="8" readonly aria-label="全部回饋文字"></textarea>
</section>
<section class="sec" id="acc"><h2>已接受（${ACC.length} 套，不需回覆）</h2>
<div class="accs">${ACC.map((a, i) => `<figure class="acc"><button type="button" class="zoom" data-img="acc${i}" aria-label="放大：${esc(label(a))}"><img src="${esc(a.img.view.src)}" width="${a.img.view.w}" height="${a.img.view.h}" alt="${esc(label(a))}" loading="lazy"></button>
<figcaption><b>${esc(label(a))}</b><br><span class="ok">${esc(a.label)}</span></figcaption></figure>`).join('')}</div>
</section>
<section class="sec" id="pend"><h2>待處理</h2>
${PEND.map(p => `<p class="td-h"><b>${esc(label(p))}</b>｜${esc(p.v)}</p>`).join('')}
</section>
<section class="sec hist"><h2><a href="${esc(K.history.href)}">${esc(K.history.label)} →</a></h2></section>`;
    updateCopy();
  }

  function savedText(f) {
    if (!storeOk) return '這個瀏覽器不允許儲存；請在看完後直接按「複製全部回饋」。';
    if (f && f.stale) return '先前的回覆對應的是別的圖片，已不套用；這一套目前未回覆。';
    if (!f || (!f.v && !f.note)) return '還沒回覆（未回覆不算接受）。';
    const t = f.at ? new Date(f.at) : null;
    return `已存在這台裝置的瀏覽器${t && !isNaN(t) ? `（${t.toLocaleString('zh-TW', { hour12: false })}）` : ''}。${f.v ? '' : '尚未選擇，目前不算接受。'}`;
  }

  // ---------- 全部複製：未回覆不算接受 ----------
  function allText() {
    const n = { A: 0, B: 0, edit: 0, none: 0 };
    const lines = [];
    for (const [b, zh] of BOOKS) {
      lines.push(`【${zh}】`);
      SETS.filter(s => s.book === b).forEach(s => {
        const f = fb(s), [a, bb] = ids(s);
        n[f.v || 'none']++;
        const pick = f.v === 'A' ? `接受 A（圖片 ${a}）` : f.v === 'B' ? `接受 B（圖片 ${bb}）` : f.v === 'edit' ? `兩張都想修改（圖片 ${a}、${bb}）` : `未回覆（不算接受；圖片 ${a}、${bb}）`;
        const head = `${s.month} 月｜${s.name}｜${s.set}：${pick}`;
        lines.push(f.note.trim() ? `${head}\n   備註：${f.note.trim().replace(/\s*\n\s*/g, '／')}` : head);
      });
    }
    const head = `${K.task}｜${K.round} 選片回饋（頁面版本 ${PAGE_COMMIT ? PAGE_COMMIT.slice(0, 7) : '本機預覽'}）`;
    const sum = `合計 ${SETS.length} 套：已回覆 ${SETS.length - n.none}（接受 A ${n.A}、接受 B ${n.B}、兩張都想修改 ${n.edit}）、未回覆 ${n.none}（未回覆不算接受）。`;
    return { n, text: [head, ...lines, sum].join('\n') };
  }
  function updateCopy() {
    const { n } = allText();
    const done = SETS.length - n.none;
    $('#cp-sum').textContent = `已回覆 ${done}／${SETS.length}：接受 A ${n.A}、接受 B ${n.B}、兩張都想修改 ${n.edit}、未回覆 ${n.none}`;
    $('#cp-text').value = allText().text;
    $('#prog').textContent = `已回覆 ${done}／${SETS.length} 套（未回覆不算接受）`;
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
    const s = SETS[cur];
    if (clear) app.querySelectorAll('input[name="fb-v"]').forEach(r => { r.checked = false; });
    const v = (app.querySelector('input[name="fb-v"]:checked') || {}).value || '';
    save(s, v, $('#fb-note').value);
    const f = fb(s), st = f.v;
    $('#fb-saved').textContent = savedText(f);
    $('#fb-clear').disabled = !st;
    const cls = `st ${st ? (st === 'edit' ? 'edit' : 'accept') : 'none'}`;
    const h = $('#set-st'); h.className = cls; h.textContent = st ? CHOICE[st] : '未回覆';
    const b = app.querySelector(`.pn-b[data-go="${cur}"] .st`); if (b) { b.className = cls; b.textContent = st ? CHOICE[st] : '未回覆'; }
    const tab = app.querySelector(`.tab[data-book="${s.book}"] span`);
    if (tab) { const all = SETS.filter(x => x.book === s.book); tab.textContent = `${all.filter(x => stateOf(x)).length}／${all.length} 已回覆`; }
    updateCopy();
  }

  function go(i, focusNav) {
    if (i < 0 || i >= SETS.length || i === cur) return;
    cur = i;
    try { history.replaceState(history.state, '', '#' + encodeURIComponent(SETS[cur].set)); } catch (e) { /* 只是記住目前這一套 */ }
    render();
    const nav = app.querySelector('.pn');
    if (nav && nav.getBoundingClientRect().top < 0) nav.scrollIntoView({ block: 'start' });
    if (focusNav) { const b = app.querySelector('.pn-b.on'); if (b) b.focus({ preventScroll: true }); }
  }

  // ---------- 放大檢視：先看顯示版，「原尺寸」改看原尺寸完整版；候選可切換 A／B ----------
  const viewer = $('#viewer'), vimg = $('#viewer-img'), vcap = $('#viewer-cap'), vmode = $('#viewer-mode'), vother = $('#viewer-other');
  let vk = null, lastBtn = null, pushed = false;
  function views(key) {
    const s = SETS[cur];
    const c = s.candidates.find(x => x.v === key);
    if (c) return [c.img.view, c.img.full, `${label(s)}｜候選 ${c.v}（圖片 ${c.img_id}）`];
    const m = /^acc(\d+)$/.exec(key || '');
    const a = m && ACC[+m[1]];
    return a ? [a.img.view, a.img.full, `${label(a)}｜${a.label}`] : null;
  }
  function setImg(m) { vimg.src = m.src; vimg.width = m.w; vimg.height = m.h; }
  function capText(nat) {
    const [fit, full, cap] = views(vk);
    const m = nat ? full : fit;
    return `${cap}｜${m === full ? '原尺寸' : '顯示'} ${m.w}×${m.h} px` + (nat ? '' : '；按「原尺寸」看完整解析度');
  }
  function show(key, nat) {
    const v = views(key);
    if (!v) return false;
    vk = key;
    setImg(nat ? v[1] : v[0]);
    vimg.alt = v[2];
    vcap.textContent = capText(nat);
    viewer.classList.toggle('natural', nat);
    vmode.textContent = nat ? '符合畫面' : '原尺寸';
    vother.hidden = !/^[AB]$/.test(key);
    vother.textContent = key === 'A' ? '看 B →' : '← 看 A';
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
    if (t) { const i = SETS.findIndex(s => s.book === t.dataset.book); if (SETS[cur].book !== t.dataset.book) go(i, true); return; }
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
  vother.addEventListener('click', () => show(vk === 'A' ? 'B' : 'A', viewer.classList.contains('natural')));
  vimg.addEventListener('click', toggleMode);
  window.addEventListener('popstate', () => closeViewer(true));
  window.addEventListener('hashchange', () => { const h = decodeURIComponent(location.hash.slice(1)); const i = idx(h); if (i >= 0 && i !== cur) { cur = -1; go(i, false); } });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeViewer(false); });
  window.addEventListener('storage', e => { if (e.key && e.key.startsWith(K.key_prefix)) render(); });

  $('#tline').textContent = `${K.task}｜${K.round}`;
  $('#title').textContent = K.title;
  $('#intro').textContent = K.intro;
  $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
  render();
})();
