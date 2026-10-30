// 2027 KOL 桌曆｜排版預覽頁（layout.html，M-5 R26 起）。資料來自 layout-data.js 與 cover-data.js（程式產生）。
// 依橫式／直式、月份看實際頁面（PDF 點陣化後的圖），可放大、開關參考線；橫式可切換「完整 16:9（推薦）」與「192×104 套框」比較。
// M-5 R27 起最上面加「封面候選」：橫式、直式各 A／B，可選 A／B／都想修改並寫備註；回饋鍵 cal2027-cover-r27-v1（只放封面選擇，不自動算 Owner 接受）。
// R26 的排版回饋（鍵 cal2027-layout-r26-v1）原樣保留在頁面下方；其他鍵（選片、企劃、素材頁）不讀、不寫、不刪。
// 沒有追蹤或分析，回饋不會自動送出；未選不算接受。
'use strict';
(() => {
  const L = window.CAL_LAYOUT;
  const C = window.CAL_COVER && window.CAL_COVER.cards ? window.CAL_COVER : null;
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
  // 封面選擇（另一個鍵）：dec＝{H, V}、notes＝{H, V, general}
  const CKEY = C ? C.feedback_key : '';
  const cload = () => {
    if (!C) return blank();
    try {
      const v = JSON.parse(localStorage.getItem(CKEY) || 'null');
      return v && typeof v === 'object' ? { dec: v.dec && typeof v.dec === 'object' ? v.dec : {}, notes: v.notes && typeof v.notes === 'object' ? v.notes : {} } : blank();
    } catch (e) { return blank(); }
  };
  const cst = cload();
  const csave = () => { try { localStorage.setItem(CKEY, JSON.stringify(cst)); } catch (e) { /* 同上 */ } };

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
  const coverLegend = () => `<p class="legend"${guides ? '' : ' hidden'}><span class="lg lg-coil"></span>線圈假設區（上緣 12 mm）` +
    `<span class="lg lg-trim"></span>裁切線<span class="lg lg-safe"></span>安全區（橫式＝${esc(L.formats.H.safe_label)}；直式＝${esc(L.formats.V.safe_label)}）</p>`;

  // ---------- 封面候選（M-5 R27） ----------
  const optLabel = (k, v) => {
    const o = C.options.find(x => x.v === v); if (!o) return '（未選）';
    const c = C.cards[k].find(x => x.dir === v);
    return c ? `${o.label}（${c.dir_zh}）` : o.label;
  };
  function coverCard(k, c) {
    const cap = `${BOOK_ZH[k]}封面 ${c.dir}｜${c.dir_zh}`;
    const nP = addView({ view: c.photo, full: c.photo }, `${cap}｜照片原圖（無文字）`);
    const nI = addView({ view: c.ids, full: c.ids }, `${cap}｜臉部對照（左＝身分參考、右＝封面）`);
    const cnt = C.grades.map(g => `${g} ${c.counts[g]}`).join('｜');
    const fl = c.flagged.length ? `<br>需注意：${c.flagged.map(x => `${esc(x.name)}（${esc(x.grade)}）`).join('、')}` : '';
    const mark = { '通過': '✓', '部分': '△', '未通過': '✗' };
    return `<article class="ccard" id="cover-${c.id}"><h4>${c.dir}｜${esc(c.dir_zh)}</h4>` +
      faceFig({ ...c.page, face: 'cover' }, k, `${cap}（含 2 mm 出血）`) +
      `<p class="cverdict"><b>${esc(c.verdict)}</b><br>身分判讀：${esc(cnt)}${fl}</p>` +
      `<div class="cbtns"><button type="button" class="btn ghost" data-f="${nP}">看照片原圖（無文字）</button><button type="button" class="btn ghost" data-f="${nI}">臉部對照（12 人）</button></div>` +
      `<details class="more"><summary>7 項檢查</summary><ul class="chk">${c.checks.map(x => `<li><span class="mk">${mark[x.result] || ''} ${esc(x.result)}</span>｜${esc(x.item)}<small>${esc(x.note)}</small></li>`).join('')}</ul></details>` +
      `<details class="more"><summary>12 人逐一判讀</summary><ul class="ppl">${c.people.map(x => `<li><b>${esc(x.name)}</b>｜${esc(x.grade)}<small>${esc(x.note)}</small></li>`).join('')}</ul></details></article>`;
  }
  function coverSection() {
    if (!C) return '';
    const grp = k => {
      const f = C.formats[k];
      return `<div class="cgroup" id="cover-${k}"><h3>${BOOK_ZH[k]}封面（成品 ${f.W - 2 * f.trim}×${f.H - 2 * f.trim} mm）</h3>` +
        `<div class="cgrid cgrid-${k}">${C.cards[k].map(c => coverCard(k, c)).join('')}</div>` +
        `<fieldset class="dq"><legend>${BOOK_ZH[k]}封面選哪一張？</legend>` + C.options.map(o =>
          `<label class="opt"><input type="radio" name="cov-${k}" value="${esc(o.v)}"${cst.dec[k] === o.v ? ' checked' : ''}> <span>${esc(optLabel(k, o.v))}</span></label>`).join('') +
        `<button type="button" class="lnk" data-cclear="${k}">清除這題</button></fieldset>` + cnote(k, `${BOOK_ZH[k]}封面備註`) + '</div>';
    };
    return `<section class="sec" id="cover"><h2>封面候選：請選擇</h2><p class="warn">${esc(C.cover_status)}</p>` +
      `<p class="note">${esc(C.made)}${esc(C.cover_note)}</p>` +
      `<div class="tools"><label class="gsw"><input type="checkbox" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>${coverLegend()}` +
      grp('H') + grp('V') + cnote('general', '封面整體備註') +
      `<div class="acts"><button type="button" class="btn" id="cover-copy">複製封面回饋</button></div>` +
      `<textarea id="cover-text" rows="7" readonly aria-label="封面回饋文字"></textarea></section>`;
  }
  function cnote(key, label) {
    const v = cst.notes[key] || '';
    return `<label class="nl">${esc(label)}<textarea rows="2" data-cnote="${esc(key)}" placeholder="想改什麼就寫在這裡（可留白）">${esc(v)}</textarea></label>`;
  }
  function coverText() {
    const lines = [`${C.task}／${C.round}｜封面回饋（頁面版本 ${PAGE_COMMIT || '本機預覽'}）`, '新候選不是 Owner 接受；這裡只記錄 Penny 的選擇與備註。'];
    ['H', 'V'].forEach(k => {
      lines.push(`${BOOK_ZH[k]}封面：${optLabel(k, cst.dec[k])}`);
      if ((cst.notes[k] || '').trim()) lines.push(`${BOOK_ZH[k]}備註：${cst.notes[k].trim()}`);
    });
    lines.push(`整體備註：${(cst.notes.general || '').trim() || '（無）'}`);
    return lines.join('\n');
  }
  const refreshCover = () => { const t = $('#cover-text'); if (t && C) t.value = coverText(); };

  // ---------- 各區 ----------
  function topSection() {
    const P = L.pdf;
    const dl = k => `<a class="btn dl" href="${esc(P[k].href)}" download>${BOOK_ZH[k]} PDF（${P[k].pages} 頁，成品 ${esc(P[k].trim)}，含出血 ${esc(P[k].canvas)}，${P[k].size_mb} MB）</a>`;
    const acc = C ? `<div class="acc"><h3>${esc(C.accepted.title)}</h3><ul>${C.accepted.items.map(x => `<li>${esc(x)}</li>`).join('')}</ul><p class="note">${esc(C.accepted.scope)}</p></div>`
      : `<h3>待 Penny 決定</h3><ol class="pend">${L.pending.map(x => `<li>${esc(x)}</li>`).join('')}</ol>`;
    return `<section class="sec" id="dl"><h2>內頁排版預覽 PDF</h2><div class="dls">${dl('H')}${dl('V')}</div>` +
      `<p class="warn">${esc(L.status_note)}</p>` + acc +
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
      `<div class="tools">${fsw}<label class="gsw"><input type="checkbox" id="gsw" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>` +
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
      `<article class="mcard" id="${book}-cover"><h3>封面（面 1）</h3><div class="spread spread-${book} one">${faceFig(cov, book, C ? `${BOOK_ZH[book]}｜面 1 ${C.r26_cover_label}` : `${BOOK_ZH[book]}｜面 1 封面（品牌名稱是佔位）`)}</div>${note(`${book}-cover`, `${BOOK_ZH[book]}封面備註`)}</article>` +
      Array.from({ length: 12 }, (_, i) => monthCard(i + 1)).join('') +
      `<article class="mcard" id="${book}-other"><h3>其他頁</h3><div class="spread spread-${book} many">${others.map(p => faceFig(p, book, `${BOOK_ZH[book]}｜面 ${p.face} ${p.role_zh}`)).join('')}</div>${note(`${book}-other`, `${BOOK_ZH[book]}其他頁備註`)}</article></section>`;
  }

  function fbSection() {
    const dec = L.decisions.map(d => `<fieldset class="dq"><legend>${esc(d.q)}</legend>` + d.options.map(o =>
      `<label class="opt"><input type="radio" name="dec-${esc(d.id)}" value="${esc(o.v)}"${st.dec[d.id] === o.v ? ' checked' : ''}> <span>${esc(o.label)}${o.rec ? '<em class="rec">推薦</em>' : ''}${o.note ? `<small>${esc(o.note)}</small>` : ''}</span></label>`).join('') +
      `<button type="button" class="lnk" data-clear="${esc(d.id)}">清除這題</button></fieldset>`).join('');
    const body = `<p class="note">只針對排版；照片沿用 24 張定案，不用重新接受。沒選的題目不算接受。</p>${dec}` +
      note('H-general', '橫式整體備註') + note('V-general', '直式整體備註') +
      `<div class="acts"><button type="button" class="btn" id="copy">複製全部回饋</button></div>` +
      `<textarea id="cp-text" rows="9" readonly aria-label="回饋文字"></textarea>`;
    return C ? `<section class="sec" id="fb"><details class="more hist"><summary>${esc(C.history_label)}</summary>${body}</details></section>`
      : `<section class="sec" id="fb"><h2>排版回饋</h2>${body}</section>`;
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
    app.innerHTML = coverSection() + topSection() + navSection() + bookSection() + fbSection();
    addGuides(app);
    refreshCopy();
    refreshCover();
    if (keepScroll) window.scrollTo(0, y);
  }

  app.addEventListener('click', e => {
    const b = e.target.closest('[data-book]');
    if (b) { if (b.dataset.book !== book) { book = b.dataset.book; render(true); } return; }
    const fr = e.target.closest('[data-frame]');
    if (fr) { if (fr.dataset.frame !== frame) { frame = fr.dataset.frame; render(true); } return; }
    const cl = e.target.closest('[data-clear]');
    if (cl) { delete st.dec[cl.dataset.clear]; save(); app.querySelectorAll(`input[name="dec-${cl.dataset.clear}"]`).forEach(i => { i.checked = false; }); refreshCopy(); return; }
    const ccl = e.target.closest('[data-cclear]');
    if (ccl) { delete cst.dec[ccl.dataset.cclear]; csave(); app.querySelectorAll(`input[name="cov-${ccl.dataset.cclear}"]`).forEach(i => { i.checked = false; }); refreshCover(); return; }
    const cp = e.target.closest('#copy, #cover-copy');
    if (cp) {
      const isC = cp.id === 'cover-copy';
      const box = $(isC ? '#cover-text' : '#cp-text');
      const t = isC ? coverText() : feedbackText();
      box.value = t;
      const done = ok => toast(ok ? (isC ? '已複製封面回饋' : '已複製全部回饋') : '無法自動複製，請在下方文字框手動選取複製');
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(() => done(true), () => { box.select(); done(false); });
      else { box.select(); done(false); }
      return;
    }
    const z = e.target.closest('[data-f]');
    if (z) openViewer(+z.dataset.f, z);
  });
  app.addEventListener('change', e => {
    if (e.target.matches('[data-guides]')) {
      guides = e.target.checked;
      app.querySelectorAll('[data-guides]').forEach(i => { i.checked = guides; });
      app.querySelectorAll('.legend').forEach(lg => { lg.hidden = !guides; });
      addGuides(app); return;
    }
    if (e.target.type === 'radio' && e.target.name.startsWith('dec-')) { st.dec[e.target.name.slice(4)] = e.target.value; save(); refreshCopy(); }
    if (e.target.type === 'radio' && e.target.name.startsWith('cov-')) { cst.dec[e.target.name.slice(4)] = e.target.value; csave(); refreshCover(); }
  });
  app.addEventListener('input', e => {
    const ck = e.target.dataset && e.target.dataset.cnote;
    if (ck != null) {
      const v = e.target.value;
      if (v.trim()) cst.notes[ck] = v; else delete cst.notes[ck];
      csave(); refreshCover(); return;
    }
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
    vcap.textContent = `${v[2]}｜${nat ? '原尺寸' : '顯示'} ${m.w}×${m.h} px` + (nat ? '' : v[0] === v[1] ? '；按「原尺寸」看完整解析度' : '；按「原尺寸」看 300 dpi 完整解析度');
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

  document.title = `${C ? C.title : L.title}｜2027 KOL 桌曆`;
  $('#tline').textContent = `${L.task}｜${C ? C.round : L.round}`;
  $('#title').textContent = C ? C.title : L.title;
  $('#intro').textContent = C ? C.intro : L.intro;
  $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
  render(false);
  if (location.hash) { const t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
})();
