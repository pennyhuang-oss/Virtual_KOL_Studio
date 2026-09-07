'use strict';
/* 素材挑選頁 — 897 女團養成計畫
   Selections live in localStorage and are exported as JSON for the user to
   paste back; there is no backend, which is what keeps this a single static
   route on the plan site rather than another service. */

const KEY = 'kol897-pick-v1';
const $ = (s, r = document) => r.querySelector(s);
const el = (t, c, x) => { const n = document.createElement(t); if (c) n.className = c; if (x != null) n.textContent = x; return n; };

let POOL = {};           // id -> {name, items[...]}
let PICK = {};           // id -> {items: Set, cover: assetId|null}
let FILTER = 'all';
let LB = { list: [], i: 0, kid: null };

/* ---------- persistence ---------- */

function load() {
  let raw = {};
  try { raw = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { raw = {}; }
  Object.keys(POOL).forEach((kid) => {
    const s = raw[kid] || {};
    const valid = new Set(POOL[kid].items.map((x) => x.id));
    PICK[kid] = {
      items: new Set((s.items || []).filter((x) => valid.has(x))),
      cover: valid.has(s.cover) ? s.cover : null,
    };
  });
}

function save() {
  const out = {};
  Object.keys(PICK).forEach((kid) => {
    out[kid] = { items: [...PICK[kid].items], cover: PICK[kid].cover };
  });
  try { localStorage.setItem(KEY, JSON.stringify(out)); } catch (e) { /* private mode */ }
}

/* ---------- rendering ---------- */

function visible(kid) {
  return POOL[kid].items.filter((it) => {
    if (FILTER === 'sel') return PICK[kid].items.has(it.id);
    if (FILTER === 'vid') return it.type === 'video';
    return true;
  });
}

function render() {
  const app = $('#app');
  app.textContent = '';
  Object.keys(POOL).forEach((kid) => {
    const p = POOL[kid];
    const items = visible(kid);

    const sec = el('section', 'person');
    sec.dataset.kid = kid;

    const head = el('div', 'phead');
    const h2 = el('h2', null, p.name);
    if (p.native) h2.append(el('span', null, p.native));
    const act = el('div', 'pact');
    const bAll = el('button', null, '全選');
    bAll.onclick = () => { POOL[kid].items.forEach((it) => PICK[kid].items.add(it.id)); after(kid); };
    const bNone = el('button', null, '全不選');
    bNone.onclick = () => { PICK[kid].items.clear(); PICK[kid].cover = null; after(kid); };
    act.append(bAll, bNone);
    head.append(h2, el('span', 'tag', p.group), act, countEl(kid));
    sec.append(head);

    const grid = el('div', 'grid');
    items.forEach((it) => grid.append(cell(kid, it)));
    if (!items.length) grid.append(el('p', null, '（此篩選下沒有素材）'));
    sec.append(grid);
    app.append(sec);
  });
  stats();
}

function countEl(kid) {
  const n = PICK[kid].items.size;
  const tot = POOL[kid].items.length;
  const s = el('span', n ? 'count' : 'count zero');
  s.innerHTML = `已選 <b>${n}</b> / ${tot}`;
  return s;
}

function cell(kid, it) {
  const b = el('button', 'cell');
  b.dataset.id = it.id;
  if (PICK[kid].items.has(it.id)) b.classList.add('sel');
  if (PICK[kid].cover === it.id) b.classList.add('cover');
  if (it.sensitive) b.classList.add('sens');

  if (it.thumb) {
    const img = el('img');
    img.src = it.thumb;
    img.alt = it.name;
    img.loading = 'lazy';
    b.append(img);
  } else {
    b.append(el('div', 'noimg', it.name));
  }

  if (it.type === 'video') {
    b.append(el('span', 'badge vid', `▶ 影片 ${it.mb}MB`));
  } else if (it.sensitive) {
    b.append(el('span', 'badge', '私下層'));
  }
  b.append(el('span', 'origin', it.origin));

  const z = el('button', 'zoom', '⤢');
  z.title = '放大檢視';
  z.onclick = (e) => { e.stopPropagation(); openLb(kid, it.id); };
  b.append(z);

  b.onclick = () => { toggle(kid, it.id); };
  return b;
}

function toggle(kid, id) {
  const s = PICK[kid].items;
  if (s.has(id)) {
    s.delete(id);
    if (PICK[kid].cover === id) PICK[kid].cover = null;
  } else {
    s.add(id);
  }
  after(kid);
}

/** Repaint one contestant's section in place — the grid is large enough that
    a full re-render on every click loses scroll position. */
function after(kid) {
  save();
  const sec = document.querySelector(`.person[data-kid="${kid}"]`);
  if (!sec) return render();
  sec.querySelectorAll('.cell').forEach((c) => {
    c.classList.toggle('sel', PICK[kid].items.has(c.dataset.id));
    c.classList.toggle('cover', PICK[kid].cover === c.dataset.id);
  });
  sec.querySelector('.count').replaceWith(countEl(kid));
  if (FILTER === 'sel') render();
  stats();
}

function stats() {
  let n = 0, v = 0;
  const empty = [];
  Object.keys(PICK).forEach((kid) => {
    const s = PICK[kid].items;
    n += s.size;
    if (!s.size) empty.push(POOL[kid].name);
    POOL[kid].items.forEach((it) => { if (it.type === 'video' && s.has(it.id)) v += 1; });
  });
  $('#s-total').textContent = n;
  $('#s-vid').textContent = v;
  $('#s-empty').textContent = empty.length ? `尚未選：${empty.join('、')}` : '每位都已選';
}

/* ---------- lightbox ---------- */

/* The lightbox is a history entry so browser Back closes it instead of
   leaving the picker (and losing the user's place in a 468-cell grid). */
function openLb(kid, id) {
  LB.kid = kid;
  LB.list = visible(kid);
  LB.i = Math.max(0, LB.list.findIndex((x) => x.id === id));
  showLb();
  $('#lb').hidden = false;
  document.body.style.overflow = 'hidden';
  history.pushState({ lb: 1 }, '', location.pathname);
}

function showLb() {
  const it = LB.list[LB.i];
  const slot = $('#lbslot');
  slot.textContent = '';
  if (it.type === 'video' && it.clip) {
    const v = el('video');
    v.src = it.clip; v.controls = true; v.autoplay = true; v.loop = true; v.playsInline = true;
    slot.append(v);
  } else if (it.full) {
    const img = el('img');
    img.src = it.full; img.alt = it.name;
    slot.append(img);
  } else {
    slot.append(el('div', 'noimg', '（此素材沒有可預覽的畫面）'));
  }
  const picked = PICK[LB.kid].items.has(it.id);
  const isCover = PICK[LB.kid].cover === it.id;
  $('#lbpick').textContent = picked ? (isCover ? '已是封面' : '設為封面') : '選取這張';
  $('#lbpick').className = picked && !isCover ? 'pri' : '';
  const note = it.type === 'video'
    ? `影片　${it.mb}MB${it.clip ? '' : '（完整 reel，此處僅顯示首幀）'}`
    : '圖片';
  $('#lbmeta').textContent =
    `${POOL[LB.kid].name}　·　${LB.i + 1} / ${LB.list.length}　·　${note}　·　${it.origin}　·　${it.name}`;
}

function stepLb(d) {
  LB.i = (LB.i + d + LB.list.length) % LB.list.length;
  showLb();
}

function closeLb(fromPop) {
  if (!fromPop && !$('#lb').hidden && (history.state || {}).lb) return history.back();
  $('#lb').hidden = true;
  const v = $('#lbslot video');
  if (v) v.pause();
  document.body.style.overflow = '';
}

window.addEventListener('popstate', () => {
  if (!$('#lb').hidden) closeLb(true);
});

/* ---------- export ---------- */

function collect() {
  const out = { picked_at: new Date().toISOString().slice(0, 16).replace('T', ' '), personas: {} };
  Object.keys(POOL).forEach((kid) => {
    const s = PICK[kid].items;
    if (!s.size) return;
    const order = POOL[kid].items.filter((it) => s.has(it.id));
    out.personas[kid] = {
      cover: PICK[kid].cover || order[0].id,
      items: order.map((it) => it.id),
    };
  });
  return out;
}

function doCopy() {
  const json = JSON.stringify(collect(), null, 1);
  $('#out').value = json;
  $('#out-dlg').hidden = false;
  navigator.clipboard && navigator.clipboard.writeText(json).catch(() => {
    $('#out').select();
  });
}

/* ---------- boot ---------- */

fetch('data/pool.json')
  .then((r) => { if (!r.ok) throw new Error('pool.json ' + r.status); return r.json(); })
  .then((p) => {
    POOL = p;
    load();
    render();
  })
  .catch((e) => { $('#app').textContent = '素材池載入失敗：' + e.message; });

$('#f-all').onclick = () => setFilter('all', '#f-all');
$('#f-sel').onclick = () => setFilter('sel', '#f-sel');
$('#f-vid').onclick = () => setFilter('vid', '#f-vid');
function setFilter(f, btn) {
  FILTER = f;
  ['#f-all', '#f-sel', '#f-vid'].forEach((s) => $(s).classList.toggle('on', s === btn));
  render();
}

$('#reset').onclick = () => {
  if (!confirm('清空所有選擇？這不能復原。')) return;
  Object.keys(PICK).forEach((kid) => { PICK[kid] = { items: new Set(), cover: null }; });
  save();
  render();
};

/* Seeds the picker with whatever the live site currently shows, so the user
   edits the existing choice instead of starting from an empty grid. */
$('#preset').onclick = () => {
  fetch('data/media.json').then((r) => r.json()).then((m) => {
    let hit = 0;
    Object.keys(POOL).forEach((kid) => {
      const cur = m[kid];
      if (!cur) return;
      const live = new Set([...(cur.shots || []), ...(cur.videos || [])]
        .map((p) => p.split('/').pop().replace(/\.(webp|mp4)$/, '')));
      POOL[kid].items.forEach((it) => {
        // media.json is keyed by sequence, not asset id, so match on source name
        const base = it.name.replace(/\.[a-z0-9]+$/i, '');
        if (live.has(base) || (cur.videos || []).some((v) => v.endsWith(it.name))) {
          PICK[kid].items.add(it.id); hit += 1;
        }
      });
    });
    save(); render();
    alert(hit ? `已帶入 ${hit} 件目前線上版使用的素材。` :
      '目前線上版的素材是縮圖流水號，對不回原始檔，請直接手動挑選。');
  });
};

$('#copy').onclick = doCopy;
$('#out-copy').onclick = () => {
  navigator.clipboard && navigator.clipboard.writeText($('#out').value);
  $('#out').select();
};
$('#out-close').onclick = () => { $('#out-dlg').hidden = true; };

$('#lb .x').onclick = () => closeLb();
$('#lb .p').onclick = () => stepLb(-1);
$('#lb .n').onclick = () => stepLb(1);
$('#lb').onclick = (e) => { if (e.target.id === 'lb') closeLb(); };
$('#lbpick').onclick = () => {
  const it = LB.list[LB.i];
  if (!PICK[LB.kid].items.has(it.id)) PICK[LB.kid].items.add(it.id);
  else PICK[LB.kid].cover = it.id;
  after(LB.kid);
  showLb();
};

document.addEventListener('keydown', (e) => {
  if ($('#lb').hidden) return;
  if (e.key === 'Escape') closeLb();
  if (e.key === 'ArrowLeft') stepLb(-1);
  if (e.key === 'ArrowRight') stepLb(1);
  if (e.key === ' ') { e.preventDefault(); $('#lbpick').click(); }
});
