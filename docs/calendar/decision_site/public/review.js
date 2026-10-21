// 2027 KOL 桌曆｜目前檢視頁（shoot.html）：只放「當前要看的照片＋回饋」。資料來自 review-data.js（產生自 data/cal_review_current.json）。
// 已定稿企劃、月份、照片框與歷次紀錄在 history.html（只讀）；每輪更新這一頁時，完成的項目移到歷史頁，不在這裡追加全文。
// M-4 R5：第一批 5 位，一次只看一位（上方名字切換；不做並排網格或接觸表，C-2）。每張的回饋存在這台裝置的瀏覽器，
// 識別鍵 cal2027-batch1-v1:<套別>，一張一個鍵；只讀寫這個前綴，其他鍵（M-4 R3 的 cal2027-review-v1:…、企劃回饋 cal2027-shoot-v1:<SHA>、
// 素材選擇 cal2027-materials-v1:<SHA>）不讀、不寫、不刪。未回覆不算接受。沒有追蹤或分析，回饋不會自動送出。
'use strict';
(() => {
  const R = window.CAL_REVIEW;
  const app = document.getElementById('app');
  if (!R || !R.batch || !R.batch.photos || !R.batch.photos.length) { app.textContent = '資料載入失敗。'; return; }

  const $ = (s, r = document) => r.querySelector(s);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const B = R.batch, PH = B.photos, ACC = R.accepted || [];
  const mb = n => `${(n / 1e6).toFixed(1)} MB`;
  const CHOICE = { accept: '接受', edit: '想修改' };

  // ---------- 回饋：一張一個鍵，只用本批前綴 ----------
  let storeOk = true;
  function load(p) {
    try {
      const raw = localStorage.getItem(p.key);
      if (!raw) return null;
      const o = JSON.parse(raw);
      return o && typeof o === 'object' ? { v: CHOICE[o.v] ? o.v : '', note: typeof o.note === 'string' ? o.note : '', at: o.at || '' } : null;
    } catch (e) { return null; }
  }
  function save(p, v, note) {
    try {
      if (!v && !note.trim()) localStorage.removeItem(p.key);  // 只清本批這一張自己的鍵（例如把備註刪光且沒選）
      else localStorage.setItem(p.key, JSON.stringify({ v, note, at: new Date().toISOString(), batch: B.id, page: PAGE_COMMIT }));
      storeOk = true;
    } catch (e) { storeOk = false; }
  }
  const stateOf = p => { const f = load(p); return f && f.v ? f.v : ''; };

  // ---------- 目前這一位 ----------
  const byHash = () => { const h = decodeURIComponent(location.hash.slice(1)); return Math.max(0, PH.findIndex(p => p.set === h)); };
  let cur = byHash();

  const zoomBtn = (key, m, alt, badge) =>
    `<button type="button" class="zoom" data-img="${key}" aria-label="放大：${esc(alt)}"><img src="${esc(m.src)}" width="${m.w}" height="${m.h}" alt="${esc(alt)}">` +
    (badge ? `<span class="rv-badge">${esc(badge)}</span>` : '') + '</button>';

  function navHtml() {
    return PH.map((p, i) => {
      const s = stateOf(p);
      return `<li><button type="button" class="pn-b${i === cur ? ' on' : ''}" data-go="${i}"${i === cur ? ' aria-current="true"' : ''}>` +
        `<b>${i + 1}. ${esc(p.name)}</b><span>${esc(p.month)}・${esc(p.book)}</span><i class="st ${s || 'none'}">${s ? CHOICE[s] : '未回覆'}</i></button></li>`;
    }).join('');
  }

  function render() {
    const p = PH[cur], I = p.img, f = load(p) || { v: '', note: '', at: '' };
    document.title = `${p.name}｜目前檢視｜2027 KOL 桌曆`;
    app.innerHTML = `<nav class="pn" aria-label="${esc(B.title)}：選一位來看"><ol>${navHtml()}</ol></nav>
<section class="rv-photo" id="photo" aria-label="${esc(p.title)}">
<figure class="ph">${zoomBtn('view', I.view, p.title, f.v ? CHOICE[f.v] : '待你檢視')}
<figcaption><b>${esc(p.title)}</b>｜${esc(B.made)}</figcaption></figure>
<p class="acts"><button type="button" class="btn" data-open="view">看大圖</button><a class="btn ghost" id="dl" href="${esc(I.png.src)}" download="${esc(p.download_name)}">下載原圖（PNG ${p.px[0]}×${p.px[1]}，${mb(I.png.bytes)}）</a></p>
<p class="note">${esc(B.download_note)}</p>
</section>
<section class="sec" id="fb" aria-label="你的回饋"><h2>你的回饋：${esc(p.name)}</h2>
<div class="ch" role="radiogroup" aria-label="這一張">
<label class="opt"><input type="radio" name="fb-v" value="accept"${f.v === 'accept' ? ' checked' : ''}> 接受</label>
<label class="opt"><input type="radio" name="fb-v" value="edit"${f.v === 'edit' ? ' checked' : ''}> 想修改</label>
</div>
<label class="nl" for="fb-note">備註（想修改哪裡、或任何意見；可留空）</label>
<textarea id="fb-note" rows="3" maxlength="2000">${esc(f.note)}</textarea>
<p class="note" id="fb-saved" aria-live="polite">${savedText(f)}</p>
<p class="acts"><button type="button" class="btn ghost" data-go="${cur - 1}"${cur ? '' : ' disabled'}>← 上一位</button><button type="button" class="btn ghost" data-go="${cur + 1}"${cur < PH.length - 1 ? '' : ' disabled'}>下一位 →</button></p>
</section>
<section class="sec" id="check"><h2>看圖提醒</h2>
<ul class="ck">${p.checks.map(c => `<li>${esc(c)}</li>`).join('')}</ul>
<p class="note">${esc(B.checks_note)}</p>
</section>
<section class="sec" id="frame"><h2>${esc(p.frame_title)}</h2>
<figure class="fr">${zoomBtn('frame', I.frame, p.frame_title)}<figcaption><span class="flag">${esc(B.frame_label)}</span>${esc(p.frame_note)}</figcaption></figure>
</section>
<section class="sec" id="copy"><h2>本批回饋（${PH.length} 張）</h2>
<p class="td-h" id="cp-sum"></p>
<p class="acts"><button type="button" class="btn" id="cp-btn">複製本批回饋</button></p>
<p class="note" id="cp-msg" aria-live="polite">${esc(B.copy_note)}</p>
<textarea id="cp-text" rows="7" readonly aria-label="本批回饋文字"></textarea>
</section>
<section class="sec" id="acc"><h2>已接受紀錄</h2>
${ACC.map((a, i) => `<p class="td-h"><b>${esc(a.title)}</b>｜<b class="rv-lbl ok">${esc(a.label)}</b>　${esc(a.v)}</p>
<p class="acts"><button type="button" class="btn ghost" data-open="acc${i}">看大圖</button><a class="btn ghost" href="${esc(a.img.png.src)}" download="${esc(a.download_name)}">下載原圖（PNG ${a.px[0]}×${a.px[1]}，${mb(a.img.png.bytes)}）</a></p>`).join('')}
</section>
<section class="sec hist" id="hist"><h2><a href="${esc(R.history.href)}">${esc(R.history.label)} →</a></h2><p class="note">${esc(R.history.v)}</p></section>`;
    updateCopy();
  }

  function savedText(f) {
    if (!storeOk) return '這個瀏覽器不允許儲存；請在看完後直接按「複製本批回饋」。';
    if (!f || (!f.v && !f.note)) return '還沒回覆（未回覆不算接受）。';
    const t = f.at ? new Date(f.at) : null;
    return `已存在這台裝置的瀏覽器${t && !isNaN(t) ? `（${t.toLocaleString('zh-TW', { hour12: false })}）` : ''}。${f.v ? '' : '尚未選「接受」或「想修改」，目前不算接受。'}`;
  }

  // ---------- 整批複製：未回覆不算接受 ----------
  function batchText() {
    const n = { accept: 0, edit: 0, none: 0 };
    const lines = PH.map((p, i) => {
      const f = load(p) || { v: '', note: '' };
      n[f.v || 'none']++;
      const head = `${i + 1}. ${p.name}｜${p.set}｜${p.month}${p.book}：${f.v ? CHOICE[f.v] : '未回覆（不算接受）'}`;
      return f.note.trim() ? `${head}\n   備註：${f.note.trim().replace(/\s*\n\s*/g, '／')}` : head;
    });
    const head = `${R.task}｜${B.title} Penny 回饋（頁面版本 ${PAGE_COMMIT ? PAGE_COMMIT.slice(0, 7) : '本機預覽'}）`;
    return { n, text: [head, ...lines, `合計：接受 ${n.accept}、想修改 ${n.edit}、未回覆 ${n.none}（未回覆不算接受）。`].join('\n') };
  }
  function updateCopy() {
    const { n, text } = batchText();
    $('#cp-sum').textContent = `已回覆 ${n.accept + n.edit}／${PH.length}：接受 ${n.accept}、想修改 ${n.edit}、未回覆 ${n.none}（未回覆不算接受）`;
    $('#cp-text').value = text;
  }
  function copyBatch() {
    const { text } = batchText();
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

  function onChoice() {
    const p = PH[cur];
    const v = (app.querySelector('input[name="fb-v"]:checked') || {}).value || '';
    save(p, v, $('#fb-note').value);
    const f = load(p);
    $('#fb-saved').textContent = savedText(f);
    const s = stateOf(p);
    const b = app.querySelector(`.pn-b[data-go="${cur}"] .st`);
    if (b) { b.className = `st ${s || 'none'}`; b.textContent = s ? CHOICE[s] : '未回覆'; }
    const badge = app.querySelector('#photo .rv-badge');
    if (badge) badge.textContent = s ? CHOICE[s] : '待你檢視';
    updateCopy();
  }

  function go(i, focusNav) {
    if (i < 0 || i >= PH.length || i === cur) return;
    cur = i;
    try { history.replaceState(history.state, '', '#' + encodeURIComponent(PH[cur].set)); } catch (e) { /* 只是記住目前這一位 */ }
    render();
    const nav = app.querySelector('.pn');
    if (nav && nav.getBoundingClientRect().top < 0) nav.scrollIntoView({ block: 'start' });
    if (focusNav) { const b = app.querySelector('.pn-b.on'); if (b) b.focus({ preventScroll: true }); }
  }

  // ---------- 放大檢視：照片在「原尺寸」時改看原圖 PNG ----------
  const viewer = $('#viewer'), vimg = $('#viewer-img'), vcap = $('#viewer-cap'), vmode = $('#viewer-mode');
  let vk = null, lastBtn = null, pushed = false;
  function views(key) {
    const p = PH[cur];
    if (key === 'view') return [p.img.view, p.img.png, p.title];
    if (key === 'frame') return [p.img.frame, null, `${p.frame_title}｜${B.frame_label}`];
    const m = /^acc(\d+)$/.exec(key || '');
    const a = m && ACC[+m[1]];
    return a ? [a.img.view, a.img.png, `${a.title}｜${a.label}`] : null;
  }
  function setImg(m) { vimg.src = m.src; vimg.width = m.w; vimg.height = m.h; }
  function capText(nat) {
    const [fit, full, cap] = views(vk);
    const m = nat && full ? full : fit;
    return `${cap}｜${full && m === full ? '原圖' : '顯示'} ${m.w}×${m.h} px` + (full && !nat ? '；按「原尺寸」看原圖' : '');
  }
  function openViewer(key, btn) {
    const v = views(key);
    if (!v) return;
    vk = key;
    setImg(v[0]);
    vimg.alt = v[2];
    vcap.textContent = capText(false);
    lastBtn = btn;
    viewer.classList.remove('natural');
    vmode.textContent = '原尺寸';
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
    const [fit, full] = views(vk);
    setImg(nat && full ? full : fit);
    viewer.classList.toggle('natural', nat);
    vmode.textContent = nat ? '符合畫面' : '原尺寸';
    vcap.textContent = capText(nat);
    if (nat) { body.scrollLeft = Math.max(0, fx * vimg.width - body.clientWidth / 2); body.scrollTop = Math.max(0, fy * vimg.height - body.clientHeight / 2); }
  }

  app.addEventListener('click', e => {
    const g = e.target.closest('[data-go]');
    if (g && !g.disabled) { go(+g.dataset.go, g.classList.contains('pn-b')); return; }
    if (e.target.closest('#cp-btn')) { copyBatch(); return; }
    const z = e.target.closest('[data-img], [data-open]');
    if (z) openViewer(z.dataset.img || z.dataset.open, z);
  });
  app.addEventListener('change', e => { if (e.target.name === 'fb-v') onChoice(); });
  let tmr = 0;
  app.addEventListener('input', e => { if (e.target.id === 'fb-note') { clearTimeout(tmr); tmr = setTimeout(onChoice, 400); } });
  app.addEventListener('focusout', e => { if (e.target.id === 'fb-note') { clearTimeout(tmr); onChoice(); } });
  $('#viewer-close').addEventListener('click', () => closeViewer(false));
  vmode.addEventListener('click', () => toggleMode(null));
  vimg.addEventListener('click', toggleMode);
  window.addEventListener('popstate', () => closeViewer(true));
  window.addEventListener('hashchange', () => { const i = byHash(); if (i !== cur) { cur = -1; go(i, false); } });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeViewer(false); });
  window.addEventListener('storage', e => { if (e.key && e.key.startsWith(B.key_prefix)) render(); });

  $('#tline').textContent = R.task;
  $('#prog').textContent = R.progress;
  $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
  render();
})();
