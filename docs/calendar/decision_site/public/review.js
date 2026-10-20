// 2027 KOL 桌曆｜目前檢視頁（shoot.html）：只放「當前照片＋待決事項」與回饋。資料來自 review-data.js（產生自 data/cal_review_current.json）。
// 已定稿企劃、月份、照片框與歷次紀錄移到 history.html（只讀）；每輪更新這一頁時，完成的項目移到歷史頁，不在這裡追加全文。
// 回饋只存在本機瀏覽器 localStorage 的新鍵（CAL_REVIEW.feedback.key），不送到伺服器、不會通知主管；沒有追蹤或分析。
// 舊資料（企劃回饋 cal2027-shoot-v1:<SHA>、素材選擇 cal2027-materials-v1:<SHA>）本頁不讀、不寫、不刪。
'use strict';
(() => {
  const R = window.CAL_REVIEW;
  const app = document.getElementById('app');
  if (!R || !R.img || !R.feedback) { app.textContent = '資料載入失敗。'; return; }

  const $ = (s, r = document) => r.querySelector(s);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const KEY = R.feedback.key;
  const CH = Object.fromEntries(R.feedback.choices);
  const I = R.img, P = R.photo, F = R.frame;
  const mb = n => `${(n / 1e6).toFixed(1)} MB`;
  const pad = n => String(n).padStart(2, '0');
  const stamp = d => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;

  // ---------- 回饋：只用新鍵 ----------
  let st = { choice: '', note: '', saved: '' };
  let canStore = true;
  try {
    const s = JSON.parse(localStorage.getItem(KEY));
    if (s && typeof s === 'object') st = { choice: CH[s.choice] ? s.choice : '', note: typeof s.note === 'string' ? s.note : '', saved: typeof s.saved === 'string' ? s.saved : '' };
  } catch (e) { canStore = false; }

  function save() {
    st.saved = stamp(new Date());
    try {
      localStorage.setItem(KEY, JSON.stringify({ v: 1, photo: `${P.set}:${R.round}`, choice: st.choice, note: st.note, saved: st.saved }));
      canStore = true;
    } catch (e) { canStore = false; }
    status();
    return canStore;
  }
  function status() {
    const el = $('#fb-status');
    if (!el) return;
    el.textContent = !canStore ? '這個瀏覽器無法儲存（可能是私密模式）；請直接按「複製回饋」。'
      : (st.saved ? `已儲存在這個瀏覽器：${st.saved}（不會自動通知主管）` : '還沒有儲存的回饋。');
    $('#fb-text').value = buildText();
  }
  function buildText() {
    const L = [R.feedback.copy_title,
      `照片：${P.title}（${P.label}）`,
      `${R.feedback.q}：${st.choice ? CH[st.choice] : '未選'}`,
      `備註：${st.note.trim() ? st.note.trim().replace(/\s*\n\s*/g, '／') : '（無）'}`];
    R.pending.filter(x => x.id !== 'figure').forEach(x => L.push(`${x.k}：${x.state}（${x.owner_action}）`));
    L.push(`儲存：${st.saved || '未儲存'}（只存在這個瀏覽器，沒有自動通知主管）`, `頁面版本：${PAGE_COMMIT || '本機預覽（未部署）'}`);
    return L.join('\n');
  }

  // ---------- 畫面 ----------
  const zoomImg = (key, alt, cls) => {
    const m = I[key];
    return `<button type="button" class="zoom ${cls || ''}" data-img="${key}" aria-label="放大：${esc(alt)}"><img src="${esc(m.src)}" width="${m.w}" height="${m.h}" alt="${esc(alt)}"${key === 'view' ? '' : ' loading="lazy"'}>` +
      (key === 'view' ? `<span class="rv-badge">${esc(P.label)}</span>` : '') + '</button>';
  };
  function render() {
    $('#tline').textContent = R.task;
    $('#prog').textContent = R.progress;
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    app.innerHTML = `<section class="rv-photo" id="photo" aria-label="首試照片">
<figure class="ph">${zoomImg('view', `${P.title}（${P.label}）`)}
<figcaption><b>${esc(P.title)}</b>｜<b class="rv-lbl">${esc(P.label)}</b><br>${esc(P.made)}</figcaption></figure>
<p class="acts"><button type="button" class="btn" data-open="view">看大圖</button><a class="btn ghost" id="dl" href="${esc(I.png.src)}" download="${esc(P.download_name)}">下載原圖（PNG ${P.px[0]}×${P.px[1]}，${mb(I.png.bytes)}）</a></p>
<p class="note">${esc(P.download_note)}</p>
</section>
<section class="sec" id="frame"><h2>${esc(F.title)}</h2>
<figure class="fr">${zoomImg('frame', F.title)}<figcaption><span class="flag">${esc(F.label)}</span>${esc(F.note)}</figcaption></figure>
</section>
<section class="sec" id="todo"><h2>本次待處理</h2>
<ol class="todo">${R.pending.map(x => `<li class="td td-${esc(x.id)}"><p class="td-h"><b>${esc(x.k)}</b>：<span class="state">${esc(x.state)}</span><span class="act">（${esc(x.owner_action)}）</span></p><p class="note">${esc(x.v)}</p>` +
      (x.crop ? `<figure class="crop">${zoomImg('reflector', x.crop.cap)}<figcaption>${esc(x.crop.cap)}</figcaption></figure>` : '') + '</li>').join('')}</ol>
</section>
<section class="sec" id="fb"><h2>你的回饋：${esc(R.feedback.q)}</h2>
<div class="ch" role="radiogroup" aria-label="${esc(R.feedback.q)}">${R.feedback.choices.map(([k, v]) => `<label><input type="radio" name="fb-choice" value="${esc(k)}"${st.choice === k ? ' checked' : ''}>${esc(v)}</label>`).join('')}</div>
<label class="lab" for="fb-note">備註（自由填寫）</label>
<textarea id="fb-note" rows="4" placeholder="${esc(R.feedback.placeholder)}"></textarea>
<p class="acts"><button type="button" class="btn" id="fb-save">儲存</button><button type="button" class="btn ghost" id="fb-copy">複製回饋</button></p>
<p class="note" id="fb-status" role="status"></p>
<p class="callout warn">${esc(R.feedback.storage_note)}</p>
<details class="out"><summary>要複製的文字</summary><textarea id="fb-text" rows="8" readonly></textarea></details>
</section>
<section class="sec hist" id="hist"><h2><a href="${esc(R.history.href)}">${esc(R.history.label)} →</a></h2><p class="note">${esc(R.history.v)}</p></section>`;
    $('#fb-note').value = st.note;
    status();
  }

  // ---------- 事件 ----------
  let noteTimer = null;
  app.addEventListener('change', e => {
    if (e.target.name === 'fb-choice') { st.choice = CH[e.target.value] ? e.target.value : ''; save(); }
  });
  app.addEventListener('input', e => {
    if (e.target.id !== 'fb-note') return;
    st.note = e.target.value;
    clearTimeout(noteTimer);
    noteTimer = setTimeout(save, 400);
  });
  app.addEventListener('click', e => {
    const z = e.target.closest('[data-img], [data-open]');
    if (z) { openViewer(z.dataset.img || z.dataset.open, z); return; }
    if (e.target.id === 'fb-save') {
      clearTimeout(noteTimer);
      st.note = $('#fb-note').value;
      toast(save() ? '已儲存在這個瀏覽器。不會自動通知主管，請複製回饋貼回對話。' : '這個瀏覽器無法儲存；請直接複製回饋。');
    }
    if (e.target.id === 'fb-copy') copyOut();
  });

  async function copyOut() {
    clearTimeout(noteTimer);
    st.note = $('#fb-note').value;
    save();
    const text = buildText();
    const ta = $('#fb-text');
    ta.value = text;
    const done = '已複製回饋，可以貼回對話。本頁不會通知主管。';
    try { await navigator.clipboard.writeText(text); toast(done); } catch (e) {
      ta.closest('details').open = true;
      ta.focus(); ta.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch (_) { ok = false; }
      toast(ok ? done : '瀏覽器不允許自動複製：文字已選取，請手動複製。');
    }
  }

  // ---------- 放大檢視：照片在「原尺寸」時改看原圖 PNG ----------
  const VIEW = {
    view: [I.view, I.png, `${P.title}｜${P.label}`],
    frame: [I.frame, null, `${F.title}｜${F.label}`],
    reflector: [I.reflector, null, '反光板位置｜原圖裁切，未修圖'],
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
  $('#viewer-close').addEventListener('click', () => closeViewer(false));
  vmode.addEventListener('click', () => toggleMode(null));
  vimg.addEventListener('click', toggleMode);
  window.addEventListener('popstate', () => closeViewer(true));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeViewer(false); });

  let toastTimer = null;
  function toast(msg) {
    const el = $('#toast');
    el.textContent = msg;
    el.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => { el.hidden = true; }, 4000);
  }

  render();
})();
