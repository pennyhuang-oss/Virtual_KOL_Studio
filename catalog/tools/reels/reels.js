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
const box = $('reels'), feed = $('rfeed');
const tapHint = $('rtap'), sound = $('rmute'), bar = $('rbar');
let cur = 0, muted = true, open_ = false, touched = false;

function open(i) {
  open_ = true; cur = i;
  box.hidden = false;
  document.body.style.overflow = 'hidden';
  feed.innerHTML = list.map((v, n) => `<section data-n="${n}">
    <div class="bg" style="background-image:url('${v.poster}')"></div>
    <div class="stage" data-stage="${n}" style="background-image:url('${v.poster}')"></div>
    <div class="meta">
      ${v.img ? `<img src="${v.img}" alt="">` : ''}
      <span class="t"><b>${esc(v.zh || v.name)}</b><i>${esc(v.tag || '')}</i></span>
      <a href="/p/${v.id}.html">看人設 →</a>
    </div></section>`).join('');
  feed.scrollTop = feed.clientHeight * i;
  mount();
  feed.focus({ preventScroll: true });
  tapHint.hidden = touched || !muted;      // 開過聲音就不用再提示一次
  // 「滾一下換下一支」只在剛進來時提一次,幾秒後淡掉——長期掛著會擋畫面
  const tip = $('rtip');
  tip.textContent = matchMedia('(pointer:coarse)').matches ? '往上滑看下一支' : '滾一下換下一支';
  tip.hidden = false; tip.style.opacity = '';
  clearTimeout(tip._t);
  tip._t = setTimeout(() => { tip.style.opacity = 0;
    setTimeout(() => { tip.hidden = true; }, 700); }, 4200);
  history.replaceState(null, '', '#v' + (list[i] ? list[i].key : i));
}

function close() {
  open_ = false;
  feed.querySelectorAll('video').forEach(v => { try { v.pause(); } catch (e) {} });
  feed.innerHTML = '';
  box.hidden = true;
  document.body.style.overflow = '';
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
    if (n === cur) {
      // 旁邊那兩支是用 preload="metadata" 建的,輪到它時升級成 auto。
      // 🛑 不要在這裡叫 load()。mount() 每次換片都會跑,只要資料還沒到就再 load 一次,
      //    而 load() 會中斷正在下載的那一次——實測會一路 ERR_ABORTED 到 networkState=3
      //    （NO_SOURCE），那一支就永遠停在首幀。play() 本身就會去載。
      el.preload = 'auto';
      el.play().catch(() => {});                // 被自動播放政策擋住就算了,使用者自己按
    } else el.pause();
  });
  $('rcount').textContent = (cur + 1) + ' / ' + list.length;
  $('rprev').hidden = cur === 0;
  $('rnext').hidden = cur >= list.length - 1;
  if (cur > 0) { const t = $('rtip'); t.hidden = true; }   // 已經會換片了就不用再提示
}

// 開／關聲音。這是這一頁最容易被錯過的動作,所以三個地方都能觸發:
// 上面那顆金色的鈕、畫面中央的大提示、以及直接點影片本身。
function setMuted(m) {
  muted = m; touched = true;
  sound.classList.toggle('on', muted);
  sound.setAttribute('aria-pressed', String(muted));
  sound.querySelector('b').textContent = muted ? '開啟聲音' : '';
  sound.setAttribute('aria-label', muted ? '開啟聲音' : '關閉聲音');
  tapHint.hidden = true;
  feed.querySelectorAll('video').forEach(v => { v.muted = muted; });
  const v = feed.querySelector(`[data-stage="${cur}"] video`);
  if (v) v.play().catch(() => {});
}

// 進度條。跟著目前這一支的播放時間走。
setInterval(() => {
  if (!open_) return;
  const v = feed.querySelector(`[data-stage="${cur}"] video`);
  bar.style.width = v && v.duration ? (v.currentTime / v.duration * 100).toFixed(1) + '%' : '0%';
}, 160);

feed.addEventListener('scroll', () => {
  if (!open_) return;
  const n = Math.round(feed.scrollTop / feed.clientHeight);
  if (n !== cur && n >= 0 && n < list.length) {
    cur = n; mount();
    history.replaceState(null, '', '#v' + (list[n] ? list[n].key : n));
  }
}, { passive: true });

const go = d => {
  const n = Math.min(list.length - 1, Math.max(0, cur + d));
  feed.scrollTo({ top: n * feed.clientHeight, behavior: 'smooth' });
};
$('rclose').addEventListener('click', close);
sound.addEventListener('click', () => setMuted(!muted));
tapHint.addEventListener('click', () => setMuted(false));
$('rnext').addEventListener('click', () => go(1));
$('rprev').addEventListener('click', () => go(-1));

// 點影片本身：還在靜音就開聲音（最容易猜到的動作）,已經有聲音就暫停／繼續。
feed.addEventListener('click', e => {
  if (e.target.closest('a') || e.target.closest('button')) return;
  if (muted) { setMuted(false); return; }
  const v = feed.querySelector(`[data-stage="${cur}"] video`);
  if (v) { v.paused ? v.play().catch(() => {}) : v.pause(); }
});

// 滾輪一格＝換一支。原本靠 scroll-snap,一格滾輪只走一小段,感覺不像在滑短影音。
let lock = 0;
feed.addEventListener('wheel', e => {
  if (!open_ || Math.abs(e.deltaY) < 4) return;
  e.preventDefault();
  const now = Date.now();
  if (now < lock) return;
  lock = now + 520;
  go(e.deltaY > 0 ? 1 : -1);
}, { passive: false });
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
