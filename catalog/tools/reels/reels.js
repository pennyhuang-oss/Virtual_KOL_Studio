const VIDS = __VIDS__;

const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
  .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const $ = id => document.getElementById(id);

/* ── 上面的縮圖牆 ── */
const grid = $('grid'), who = $('who');
let filter = null, list = VIDS;

function renderGrid() {
  list = filter ? VIDS.filter(v => v.id === filter) : VIDS;
  grid.innerHTML = list.map((v, i) => `<button type="button" class="vc" data-i="${i}"
    aria-label="播放 ${esc(v.zh || v.name)} 的第 ${i + 1} 支影片">
    <img src="${v.poster}" alt="" loading="lazy" width="720" height="1280">
    <span class="pl"><span>▶</span></span>
    <span class="cap">${v.img ? `<img src="${v.img}" alt="" width="400" height="533">` : ''}
      <b>${esc(v.zh || v.name)}</b></span></button>`).join('');
  grid.querySelectorAll('.vc').forEach(el =>
    el.addEventListener('click', () => open(Number(el.dataset.i))));
  $('empty').hidden = list.length > 0;
  $('empty').textContent = list.length ? '' : '這位人設目前只有圖像素材。';
}

// 人設篩選。只列真的有影片的人設,不然客戶會點到空的。
const byId = new Map();
VIDS.forEach(v => byId.set(v.id, (byId.get(v.id) || 0) + 1));
const chip = (label, val) => {
  const b = document.createElement('button');
  b.type = 'button'; b.textContent = label;
  b.setAttribute('aria-pressed', String(filter === val));
  b.addEventListener('click', () => {
    filter = val;
    who.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', 'false'));
    b.setAttribute('aria-pressed', 'true');
    renderGrid();
  });
  who.appendChild(b);
};
chip(`全部 ${VIDS.length}`, null);
[...byId.keys()].forEach(id => {
  const v = VIDS.find(x => x.id === id);
  chip(`${v.zh || v.name} ${byId.get(id)}`, id);
});
renderGrid();

/* ── 全螢幕播放器 ──
   🛑 一次只建立目前這支與前後各一支的 <video>。48 支加起來 139 MB,
      全部建出來瀏覽器會同時去要 metadata,手機直接卡住。 */
const box = $('reels'), feed = $('rfeed'), hint = $('rhint');
let cur = 0, muted = true, open_ = false;

function open(i) {
  open_ = true; cur = i;
  box.hidden = false;
  document.body.style.overflow = 'hidden';
  feed.innerHTML = list.map((v, n) => `<section data-n="${n}">
    <div class="bg" style="background-image:url('${v.poster}')"></div>
    <div class="stage" data-stage="${n}">
      <div class="ph" style="background-image:url('${v.poster}')"></div>
    </div>
    <div class="meta">
      ${v.img ? `<img src="${v.img}" alt="">` : ''}
      <span class="t"><b>${esc(v.zh || v.name)}</b><i>${esc(v.tag || '')}</i></span>
      <a href="/p/${v.id}.html">看人設 →</a>
    </div></section>`).join('');
  feed.scrollTop = feed.clientHeight * i;
  mount();
  feed.focus({ preventScroll: true });
  hint.hidden = false;
  setTimeout(() => { hint.style.opacity = 0; }, 4000);
  history.replaceState(null, '', '#v' + (list[i] ? list[i].key : i));
}

function close() {
  open_ = false;
  feed.querySelectorAll('video').forEach(v => { try { v.pause(); } catch (e) {} });
  feed.innerHTML = '';
  box.hidden = true;
  document.body.style.overflow = '';
  hint.style.opacity = '';
  history.replaceState(null, '', location.pathname);
}

// 目前這支與前後各一支要有 <video>,其餘只留首幀
function mount() {
  list.forEach((v, n) => {
    const stage = feed.querySelector(`[data-stage="${n}"]`);
    if (!stage) return;
    const near = Math.abs(n - cur) <= 1;
    const has = stage.querySelector('video');
    if (near && !has) {
      const el = document.createElement('video');
      el.playsInline = true; el.loop = true; el.muted = muted;
      el.preload = n === cur ? 'auto' : 'metadata';
      el.poster = v.poster;
      // 🛑 MP4 放前面,沒有 H.264 的瀏覽器才退到 WebM（跟人設頁同一條規則）
      const s1 = document.createElement('source'); s1.src = v.mp4; s1.type = 'video/mp4'; el.appendChild(s1);
      if (v.webm) { const s2 = document.createElement('source'); s2.src = v.webm; s2.type = 'video/webm'; el.appendChild(s2); }
      stage.appendChild(el);
    } else if (!near && has) { try { has.pause(); } catch (e) {} has.remove(); }
  });
  feed.querySelectorAll('video').forEach(el => {
    const n = Number(el.closest('section').dataset.n);
    el.muted = muted;
    if (n === cur) el.play().catch(() => {});   // 被自動播放政策擋住就算了,使用者自己按
    else el.pause();
  });
  $('rcount').textContent = (cur + 1) + ' / ' + list.length;
}

feed.addEventListener('scroll', () => {
  if (!open_) return;
  const n = Math.round(feed.scrollTop / feed.clientHeight);
  if (n !== cur && n >= 0 && n < list.length) {
    cur = n; mount();
    history.replaceState(null, '', '#v' + (list[n] ? list[n].key : n));
  }
}, { passive: true });

const go = d => { feed.scrollTo({ top: (cur + d) * feed.clientHeight, behavior: 'smooth' }); };
$('rclose').addEventListener('click', close);
$('rmute').addEventListener('click', () => {
  muted = !muted;
  $('rmute').textContent = muted ? '🔇' : '🔊';
  $('rmute').setAttribute('aria-label', muted ? '開啟聲音' : '關閉聲音');
  feed.querySelectorAll('video').forEach(v => { v.muted = muted; });
  const v = feed.querySelector(`[data-stage="${cur}"] video`);
  if (v) v.play().catch(() => {});
});
document.addEventListener('keydown', e => {
  if (!open_) return;
  if (e.key === 'Escape') { close(); return; }
  if (e.key === 'ArrowDown' || e.key === 'PageDown') { e.preventDefault(); go(1); }
  if (e.key === 'ArrowUp' || e.key === 'PageUp') { e.preventDefault(); go(-1); }
});

// 網址帶 #v<key> 就直接開那一支——客戶要把某一支轉給同事時用得到
(function fromHash() {
  const m = /^#v(.+)$/.exec(location.hash || '');
  if (!m) return;
  const i = VIDS.findIndex(v => v.key === m[1]);
  if (i >= 0) { filter = null; renderGrid(); open(i); }
})();
