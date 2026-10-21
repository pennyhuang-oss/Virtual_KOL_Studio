// 2027 KOL 桌曆｜目前檢視頁（shoot.html）：只放「當前照片＋待決事項」。資料來自 review-data.js（產生自 data/cal_review_current.json）。
// 已定稿企劃、月份、照片框與歷次紀錄在 history.html（只讀）；每輪更新這一頁時，完成的項目移到歷史頁，不在這裡追加全文。
// M-4 R4：Penny 接受 V-Iris，主頁拿掉回饋題；本頁不讀、不寫、不刪任何 localStorage（M-4 R3 的回饋 cal2027-review-v1:…、
// 企劃回饋 cal2027-shoot-v1:<SHA>、素材選擇 cal2027-materials-v1:<SHA> 都照舊留在瀏覽器）。沒有追蹤或分析。
'use strict';
(() => {
  const R = window.CAL_REVIEW;
  const app = document.getElementById('app');
  if (!R || !R.img || !R.next) { app.textContent = '資料載入失敗。'; return; }

  const $ = (s, r = document) => r.querySelector(s);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const I = R.img, P = R.photo, F = R.frame, N = R.next;
  const mb = n => `${(n / 1e6).toFixed(1)} MB`;

  // ---------- 畫面 ----------
  const zoomImg = (key, alt) => {
    const m = I[key];
    return `<button type="button" class="zoom" data-img="${key}" aria-label="放大：${esc(alt)}"><img src="${esc(m.src)}" width="${m.w}" height="${m.h}" alt="${esc(alt)}"${key === 'view' ? '' : ' loading="lazy"'}>` +
      (key === 'view' ? `<span class="rv-badge${P.status === 'accepted' ? ' ok' : ''}">${esc(P.label)}</span>` : '') + '</button>';
  };
  function render() {
    $('#tline').textContent = R.task;
    $('#prog').textContent = R.progress;
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    app.innerHTML = `<section class="rv-photo" id="photo" aria-label="已接受的照片">
<figure class="ph">${zoomImg('view', `${P.title}（${P.label}）`)}
<figcaption><b>${esc(P.title)}</b>｜<b class="rv-lbl${P.status === 'accepted' ? ' ok' : ''}">${esc(P.label)}</b><br>${esc(P.made)}</figcaption></figure>
<p class="acts"><button type="button" class="btn" data-open="view">看大圖</button><a class="btn ghost" id="dl" href="${esc(I.png.src)}" download="${esc(P.download_name)}">下載原圖（PNG ${P.px[0]}×${P.px[1]}，${mb(I.png.bytes)}）</a></p>
<p class="note">${esc(P.download_note)}</p>
</section>
<section class="sec" id="next"><h2>目前進度</h2>
<p class="td-h"><b>${esc(N.k)}</b>：<span class="state">${esc(N.state)}</span></p>
<ul class="nx">${N.sets.map(([n, m, b]) => `<li>${esc(n)}<span>${esc(m)}・${esc(b)}</span></li>`).join('')}</ul>
<p class="note">${esc(N.v)}</p>
<p class="callout">${esc(R.owner_action)}</p>
</section>
<section class="sec" id="frame"><h2>${esc(F.title)}</h2>
<figure class="fr">${zoomImg('frame', F.title)}<figcaption><span class="flag">${esc(F.label)}</span>${esc(F.note)}</figcaption></figure>
</section>
<section class="sec hist" id="hist"><h2><a href="${esc(R.history.href)}">${esc(R.history.label)} →</a></h2><p class="note">${esc(R.history.v)}</p></section>`;
  }

  // ---------- 放大檢視：照片在「原尺寸」時改看原圖 PNG ----------
  const VIEW = {
    view: [I.view, I.png, `${P.title}｜${P.label}`],
    frame: [I.frame, null, `${F.title}｜${F.label}`],
  };
  const viewer = $('#viewer'), vimg = $('#viewer-img'), vcap = $('#viewer-cap'), vmode = $('#viewer-mode');
  let cur = null, lastBtn = null, pushed = false;
  function setImg(m) { vimg.src = m.src; vimg.width = m.w; vimg.height = m.h; }
  function capText(nat) {
    const [fit, full, cap] = VIEW[cur];
    const m = nat && full ? full : fit;
    return `${cap}｜${m === I.png ? '原圖' : '顯示'} ${m.w}×${m.h} px` + (full && !nat ? '；按「原尺寸」看原圖' : '');
  }
  function openViewer(key, btn) {
    if (!VIEW[key]) return;
    cur = key;
    setImg(VIEW[key][0]);
    vimg.alt = VIEW[key][2];
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
    const [fit, full] = VIEW[cur];
    setImg(nat && full ? full : fit);
    viewer.classList.toggle('natural', nat);
    vmode.textContent = nat ? '符合畫面' : '原尺寸';
    vcap.textContent = capText(nat);
    if (nat) { body.scrollLeft = Math.max(0, fx * vimg.width - body.clientWidth / 2); body.scrollTop = Math.max(0, fy * vimg.height - body.clientHeight / 2); }
  }
  app.addEventListener('click', e => {
    const z = e.target.closest('[data-img], [data-open]');
    if (z) openViewer(z.dataset.img || z.dataset.open, z);
  });
  $('#viewer-close').addEventListener('click', () => closeViewer(false));
  vmode.addEventListener('click', () => toggleMode(null));
  vimg.addEventListener('click', toggleMode);
  window.addEventListener('popstate', () => closeViewer(true));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeViewer(false); });

  render();
})();
