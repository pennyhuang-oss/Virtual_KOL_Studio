// 2027 KOL 桌曆｜排版預覽頁（layout.html，M-5 R26 起）。資料來自 layout-data.js（程式產生）。
// 依橫式／直式、月份看實際頁面（PDF 點陣化後的圖），可放大、開關參考線；橫式可切換「完整 16:9（推薦）」與「192×104 套框」比較。
// 回饋只存在這台裝置的瀏覽器，鍵是資料裡的 feedback_key（cal2027-layout-r26-v1），只放排版回饋，與選片回饋分開；
// 其他鍵（選片、企劃、素材頁）不讀、不寫、不刪。沒有追蹤或分析，回饋不會自動送出；未選不算接受。
'use strict';
(() => {
  const L = window.CAL_LAYOUT;
  const app = document.getElementById('app');
  const $ = (s, r = document) => r.querySelector(s);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  if (!L || !L.pages || !L.pages.H || !L.pages.V) { app.textContent = '資料載入失敗。'; return; }
  const KEY = L.feedback_key;
  const BOOK_ZH = { H: '橫式', V: '直式' };
  const SVGNS = 'http://www.w3.org/2000/svg';

  // ---------- 回饋狀態 ----------
  const blank = () => ({ dec: {}, notes: {} });
  const load = () => {
    try {
      const v = JSON.parse(localStorage.getItem(KEY) || 'null');
      return v && typeof v === 'object' ? { dec: v.dec && typeof v.dec === 'object' ? v.dec : {}, notes: v.notes && typeof v.notes === 'object' ? v.notes : {} } : blank();
    } catch (e) { return blank(); }
  };
  let st = load();
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) { /* 無痕或停用儲存時只在本頁有效 */ } };

  let book = /^#V/.test(location.hash) ? 'V' : 'H';
  let frame = 'B';     // 橫式照片面顯示哪個版本：B＝完整 16:9（推薦）、A＝192×104 套框
  let guides = false;
  const views = [];     // 放大檢視：[顯示版, 完整版, 說明]
  const addView = (p, cap) => { views.push([p.view, p.full, cap]); return views.length - 1; };
  const cmpOf = m => L.compare.months.find(x => x.month === m);
  const zoomOf = m => L.compare.zooms.find(x => x.month === m);

  // ---------- 頁面圖（含參考線） ----------
  function faceFig(p, k, cap, extraCls) {
    const n = addView(p, cap);
    return `<figure class="face face-${k}${extraCls ? ' ' + extraCls : ''}" data-k="${k}" data-face="${p.face}"${p.photo_box ? ` data-box="${p.photo_box.join(',')}"` : ''}>` +
      `<button type="button" class="zoom" data-f="${n}" aria-label="放大：${esc(cap)}"><img src="${esc(p.view.src)}" width="${p.view.w}" height="${p.view.h}" alt="${esc(cap)}" loading="lazy"></button>` +
      `<figcaption>${esc(cap)}</figcaption></figure>`;
  }
  function addGuides(root) {
    root.querySelectorAll('figure.face').forEach(fig => {
      const old = fig.querySelector('svg.guides'); if (old) old.remove();
      if (!guides) return;
      const f = L.formats[fig.dataset.k];
      const svg = document.createElementNS(SVGNS, 'svg');
      svg.setAttribute('class', 'guides'); svg.setAttribute('viewBox', `0 0 ${f.W} ${f.H}`); svg.setAttribute('preserveAspectRatio', 'none'); svg.setAttribute('aria-hidden', 'true');
      const rect = (x0, y0, x1, y1, cls) => { const r = document.createElementNS(SVGNS, 'rect'); r.setAttribute('x', x0); r.setAttribute('y', y0); r.setAttribute('width', x1 - x0); r.setAttribute('height', y1 - y0); r.setAttribute('class', cls); svg.appendChild(r); };
      const line = (y, cls) => { const l = document.createElementNS(SVGNS, 'line'); l.setAttribute('x1', 0); l.setAttribute('x2', f.W); l.setAttribute('y1', y); l.setAttribute('y2', y); l.setAttribute('class', cls); svg.appendChild(l); };
      rect(0, 0, f.W, f.coil_assumed, 'g-coil');
      line(f.coil_measured, 'g-coilm');
      rect(f.trim, f.trim, f.W - f.trim, f.H - f.trim, 'g-trim');
      rect(f.safe[0], f.safe[1], f.safe[2], f.safe[3], 'g-safe');
      if (fig.dataset.box) { const b = fig.dataset.box.split(',').map(Number); rect(b[0], b[1], b[2], b[3], 'g-photo'); }
      fig.querySelector('.zoom').appendChild(svg);
    });
  }

  // ---------- 各區 ----------
  function topSection() {
    const P = L.pdf;
    const dl = k => `<a class="btn dl" href="${esc(P[k].href)}" download>${BOOK_ZH[k]} PDF（${P[k].pages} 頁，成品 ${esc(P[k].trim)}，含出血 ${esc(P[k].canvas)}，${P[k].size_mb} MB）</a>`;
    return `<section class="sec" id="dl"><h2>下載排版預覽 PDF</h2><div class="dls">${dl('H')}${dl('V')}</div>` +
      `<p class="warn">${esc(L.status_note)}</p>` +
      `<h3>待 Penny 決定</h3><ol class="pend">${L.pending.map(x => `<li>${esc(x)}</li>`).join('')}</ol>` +
      `<details class="more"><summary>推薦排法（目前預覽與 PDF 用的）</summary><ul>${L.recommended.map(x => `<li>${esc(x)}</li>`).join('')}</ul><p class="note">${esc(L.date_note)}</p></details>` +
      `<details class="more"><summary>仍需廠商確認或打樣的事（本輪不聯絡廠商、不打樣）</summary><ul>${L.vendor.map(x => `<li>${esc(x)}</li>`).join('')}</ul></details></section>`;
  }

  function navSection() {
    const tabs = ['H', 'V'].map(k => `<button type="button" class="tab${k === book ? ' on' : ''}" data-book="${k}" aria-pressed="${k === book}">${BOOK_ZH[k]}<span>${L.pdf[k].pages} 面｜${esc(L.pdf[k].trim)}</span></button>`).join('');
    const months = ['cover', ...Array.from({ length: 12 }, (_, i) => i + 1), 'other'].map(m =>
      `<li><a class="mchip" href="#${book}-${m === 'cover' ? 'cover' : m === 'other' ? 'other' : 'm' + m}">${m === 'cover' ? '封面' : m === 'other' ? '其他頁' : m + ' 月'}</a></li>`).join('');
    const fsw = book === 'H' ? `<div class="fsw" role="group" aria-label="橫式照片框"><span class="fsw-l">照片框：</span>` +
      `<button type="button" class="seg${frame === 'B' ? ' on' : ''}" data-frame="B" aria-pressed="${frame === 'B'}">完整 16:9（推薦）</button>` +
      `<button type="button" class="seg${frame === 'A' ? ' on' : ''}" data-frame="A" aria-pressed="${frame === 'A'}">192×104 套框</button></div>` : '';
    return `<section class="sec navsec" id="nav"><div class="tabs">${tabs}</div><ol class="mnav">${months}</ol>` +
      `<div class="tools">${fsw}<label class="gsw"><input type="checkbox" id="gsw"${guides ? ' checked' : ''}> 顯示參考線</label></div>` +
      `<p class="legend"${guides ? '' : ' hidden'}><span class="lg lg-coil"></span>線圈假設區（上緣 12 mm；虛線＝編輯器示意約 ${L.formats[book].coil_measured} mm）` +
      `<span class="lg lg-trim"></span>裁切線<span class="lg lg-safe"></span>${esc(L.formats[book].safe_label)}<span class="lg lg-photo"></span>照片框</p></section>`;
  }

  function note(key, label) {
    const v = st.notes[key] || '';
    return `<label class="nl">${esc(label)}<textarea rows="2" data-note="${esc(key)}" placeholder="想改什麼就寫在這裡（可留白）">${esc(v)}</textarea></label>`;
  }

  function monthCard(m) {
    const ps = L.pages[book].filter(p => p.month === m);
    const ph = ps.find(p => p.role === 'photo'), gr = ps.find(p => p.role === 'grid');
    const who = ph.person;
    let photoFig, extra = '';
    if (book === 'H') {
      const c = cmpOf(m);
      if (frame === 'A') {
        photoFig = faceFig(c.A, 'H', `橫式 ${m} 月｜${who}｜照片面（192×104 套框，比較用）`, 'is-a');
        extra += `<p class="cnote">${esc(c.note)}</p>`;
      } else {
        photoFig = faceFig(ph, 'H', `橫式 ${m} 月｜${who}｜面 ${ph.face} 照片面（完整 16:9）`);
      }
      const z = zoomOf(m);
      if (z) {
        if (frame !== 'A') extra += `<p class="cnote">192×104 套框時：${esc(c.note)}</p>`;
        extra += `<details class="zd"><summary>上下緣放大比較（照片框兩種排法）</summary>` +
          ['top', 'bottom'].map(e => `<p class="zh">${e === 'top' ? '上緣（髮頂）' : '下緣（腳／鞋）'}</p><div class="zrow">` +
            z.rows[e].map(it => { const n = addView({ view: it, full: it }, `${who} ${e === 'top' ? '上緣' : '下緣'}｜${it.label}`); return `<figure class="zf"><button type="button" class="zoom px" data-f="${n}"><img src="${esc(it.src)}" width="${it.w}" height="${it.h}" alt="${esc(it.label)}" loading="lazy"></button><figcaption>${esc(it.label)}</figcaption></figure>`; }).join('') + '</div>').join('') +
          `<p class="note">直接從 300 dpi 輸出切下來、未縮放；白色是照片框外的頁面。</p></details>`;
      }
    } else {
      photoFig = faceFig(ph, 'V', `直式 ${m} 月｜${who}｜面 ${ph.face} 照片面`);
    }
    const grFig = faceFig(gr, book, `${BOOK_ZH[book]} ${m} 月｜${who}｜面 ${gr.face} 大格面`);
    return `<article class="mcard" id="${book}-m${m}"><h3>${m} 月｜${esc(who)}</h3><div class="spread spread-${book}">${photoFig}${grFig}</div>${extra}${note(`${book}-${m}`, `${BOOK_ZH[book]} ${m} 月備註`)}</article>`;
  }

  function bookSection() {
    const P = L.pages[book];
    const cov = P.find(p => p.role === 'cover');
    const others = P.filter(p => ['memo', 'year', 'barcode'].includes(p.role));
    return `<section class="sec" id="pages"><h2>${BOOK_ZH[book]}：實際頁面（${P.length} 面，依範本頁序）</h2>` +
      `<p class="note">每月兩面：照片面在前、大格面在後。紙張正反面怎麼拼、背面會不會轉向還沒跟廠商確認，所以這裡和 PDF 都是一面一面正向排列。</p>` +
      `<article class="mcard" id="${book}-cover"><h3>封面（面 1）</h3><div class="spread spread-${book} one">${faceFig(cov, book, `${BOOK_ZH[book]}｜面 1 封面（品牌名稱是佔位）`)}</div>${note(`${book}-cover`, `${BOOK_ZH[book]}封面備註`)}</article>` +
      Array.from({ length: 12 }, (_, i) => monthCard(i + 1)).join('') +
      `<article class="mcard" id="${book}-other"><h3>其他頁</h3><div class="spread spread-${book} many">${others.map(p => faceFig(p, book, `${BOOK_ZH[book]}｜面 ${p.face} ${p.role_zh}`)).join('')}</div>${note(`${book}-other`, `${BOOK_ZH[book]}其他頁備註`)}</article></section>`;
  }

  function fbSection() {
    const dec = L.decisions.map(d => `<fieldset class="dq"><legend>${esc(d.q)}</legend>` + d.options.map(o =>
      `<label class="opt"><input type="radio" name="dec-${esc(d.id)}" value="${esc(o.v)}"${st.dec[d.id] === o.v ? ' checked' : ''}> <span>${esc(o.label)}${o.rec ? '<em class="rec">推薦</em>' : ''}${o.note ? `<small>${esc(o.note)}</small>` : ''}</span></label>`).join('') +
      `<button type="button" class="lnk" data-clear="${esc(d.id)}">清除這題</button></fieldset>`).join('');
    return `<section class="sec" id="fb"><h2>排版回饋</h2><p class="note">只針對排版；照片沿用 24 張定案，不用重新接受。沒選的題目不算接受。</p>${dec}` +
      note('H-general', '橫式整體備註') + note('V-general', '直式整體備註') +
      `<div class="acts"><button type="button" class="btn" id="copy">複製全部回饋</button></div>` +
      `<textarea id="cp-text" rows="9" readonly aria-label="回饋文字"></textarea></section>`;
  }

  // ---------- 回饋文字 ----------
  function feedbackText() {
    const lines = [`${L.task}／${L.round}｜排版預覽回饋（頁面版本 ${PAGE_COMMIT || '本機預覽'}）`, '只針對排版；照片沿用 24 張定案（照片接受另記）。'];
    L.decisions.forEach(d => { const o = d.options.find(x => x.v === st.dec[d.id]); lines.push(`${d.q}：${o ? o.label : '（未選）'}`); });
    const order = ['H-general', 'H-cover', ...Array.from({ length: 12 }, (_, i) => `H-${i + 1}`), 'H-other', 'V-general', 'V-cover', ...Array.from({ length: 12 }, (_, i) => `V-${i + 1}`), 'V-other'];
    const name = k => { const [b, r] = k.split('-'); return `${BOOK_ZH[b]}${r === 'general' ? '整體' : r === 'cover' ? '封面' : r === 'other' ? '其他頁' : ` ${r} 月`}`; };
    const ns = order.filter(k => (st.notes[k] || '').trim()).map(k => `・${name(k)}：${st.notes[k].trim()}`);
    lines.push(ns.length ? '備註：' : '備註：（無）', ...ns);
    return lines.join('\n');
  }
  const refreshCopy = () => { const t = $('#cp-text'); if (t) t.value = feedbackText(); };
  let toastT = 0;
  const toast = msg => { const t = $('#toast'); t.textContent = msg; t.hidden = false; clearTimeout(toastT); toastT = setTimeout(() => { t.hidden = true; }, 2200); };

  // ---------- 繪製 ----------
  function render(keepScroll) {
    const y = window.scrollY;
    views.length = 0;
    app.innerHTML = topSection() + navSection() + bookSection() + fbSection();
    addGuides(app);
    refreshCopy();
    if (keepScroll) window.scrollTo(0, y);
  }

  app.addEventListener('click', e => {
    const b = e.target.closest('[data-book]');
    if (b) { if (b.dataset.book !== book) { book = b.dataset.book; render(true); } return; }
    const fr = e.target.closest('[data-frame]');
    if (fr) { if (fr.dataset.frame !== frame) { frame = fr.dataset.frame; render(true); } return; }
    const cl = e.target.closest('[data-clear]');
    if (cl) { delete st.dec[cl.dataset.clear]; save(); app.querySelectorAll(`input[name="dec-${cl.dataset.clear}"]`).forEach(i => { i.checked = false; }); refreshCopy(); return; }
    if (e.target.closest('#copy')) {
      const t = feedbackText();
      $('#cp-text').value = t;
      const done = ok => toast(ok ? '已複製全部回饋' : '無法自動複製，請在下方文字框手動選取複製');
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(() => done(true), () => { $('#cp-text').select(); done(false); });
      else { $('#cp-text').select(); done(false); }
      return;
    }
    const z = e.target.closest('[data-f]');
    if (z) openViewer(+z.dataset.f, z);
  });
  app.addEventListener('change', e => {
    if (e.target.id === 'gsw') { guides = e.target.checked; const lg = $('.legend'); if (lg) lg.hidden = !guides; addGuides(app); return; }
    if (e.target.type === 'radio' && e.target.name.startsWith('dec-')) { st.dec[e.target.name.slice(4)] = e.target.value; save(); refreshCopy(); }
  });
  app.addEventListener('input', e => {
    const k = e.target.dataset && e.target.dataset.note;
    if (k == null) return;
    const v = e.target.value;
    if (v.trim()) st.notes[k] = v; else delete st.notes[k];
    save(); refreshCopy();
  });

  // ---------- 放大檢視：先看顯示版，「原尺寸」改看 300 dpi 完整版 ----------
  const viewer = $('#viewer'), vimg = $('#viewer-img'), vcap = $('#viewer-cap'), vmode = $('#viewer-mode'), vbody = $('#viewer-body');
  let vk = -1, lastBtn = null, pushed = false;
  const show = (k, nat) => {
    const v = views[k]; if (!v) return;
    vk = k; const m = nat ? v[1] : v[0];
    vimg.src = m.src; vimg.width = m.w; vimg.height = m.h; vimg.alt = v[2];
    vcap.textContent = `${v[2]}｜${nat ? '原尺寸' : '顯示'} ${m.w}×${m.h} px` + (nat ? '' : '；按「原尺寸」看 300 dpi 完整解析度');
    viewer.classList.toggle('natural', nat); vmode.textContent = nat ? '符合畫面' : '原尺寸';
  };
  function openViewer(k, btn) {
    show(k, false); lastBtn = btn; viewer.hidden = false; document.documentElement.classList.add('noscroll');
    try { history.pushState({ viewer: 1 }, ''); pushed = true; } catch (err) { pushed = false; }
    $('#viewer-close').focus({ preventScroll: true });
  }
  const close = fromPop => {
    if (viewer.hidden) return;
    viewer.hidden = true; vimg.removeAttribute('src'); document.documentElement.classList.remove('noscroll');
    if (pushed && !fromPop) { pushed = false; history.back(); }
    pushed = false;
    if (lastBtn && document.body.contains(lastBtn)) lastBtn.focus({ preventScroll: true });
  };
  const toggle = ev => {
    const nat = !viewer.classList.contains('natural');
    let fx = 0.5, fy = 0.5;
    if (ev && ev.target === vimg) { const r = vimg.getBoundingClientRect(); fx = (ev.clientX - r.left) / r.width; fy = (ev.clientY - r.top) / r.height; }
    show(vk, nat);
    if (nat) { vbody.scrollLeft = Math.max(0, fx * vimg.width - vbody.clientWidth / 2); vbody.scrollTop = Math.max(0, fy * vimg.height - vbody.clientHeight / 2); }
  };
  $('#viewer-close').addEventListener('click', () => close(false));
  vmode.addEventListener('click', () => toggle(null));
  vimg.addEventListener('click', toggle);
  window.addEventListener('popstate', () => close(true));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(false); });

  document.title = `${L.title}｜2027 KOL 桌曆`;
  $('#tline').textContent = `${L.task}｜${L.round}`;
  $('#title').textContent = L.title;
  $('#intro').textContent = L.intro;
  $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
  render(false);
  if (location.hash) { const t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
})();
