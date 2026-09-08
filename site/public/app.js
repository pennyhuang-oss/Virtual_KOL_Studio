'use strict';
/* 897 女團選秀 — 企劃提案站
   Everything renders from data/plan.json + data/roster.json + data/media.json,
   so adding a new section or a new contestant is a data edit, not a code edit. */

const $ = (s, r = document) => r.querySelector(s);
const el = (t, cls, txt) => {
  const n = document.createElement(t);
  if (cls) n.className = cls;
  if (txt != null) n.textContent = txt;
  return n;
};
// Editorial copy may carry **bold**, `code` and 「quotes」. Escape first, then
// re-introduce only those two tags — never inject raw source text as HTML.
const esc = (s) => String(s).replace(/[&<>"]/g, (c) =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const rich = (s) => esc(s)
  .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
  .replace(/`(.+?)`/g, '<code>$1</code>');

const NAV = [
  ['top', '總覽'], ['flow', '流程'], ['talentmodel', '才藝架構'], ['roster', '參賽者'],
  ['talents', '才藝一覽'], ['checks', '體檢'], ['decisions', '待裁決'],
  ['alternates', '替補'], ['next', '下一步'],
];

let PLAN, ROSTER, MEDIA, gallery = [], gi = 0;

/* Overlays are history entries, not just JS state. People reach for browser
   Back to leave a detail panel, and before this that navigated away from the
   whole site. Back now closes the topmost overlay, ?c=<id> makes a contestant
   linkable, and every close path routes through history so the stack cannot
   drift out of sync with what is on screen. */
const NAVSTATE = { depth: 0 };

function pushOverlay(kind, params) {
  const q = new URLSearchParams(params);
  NAVSTATE.depth += 1;
  history.pushState({ o: kind, depth: NAVSTATE.depth }, '',
    `${location.pathname}?${q}`);
}

function popOverlay() {
  if (NAVSTATE.depth > 0) history.back();
  else { closeLightbox(true); closeDetail(true); }
}

async function boot() {
  try {
    const [p, r, m] = await Promise.all(
      ['data/plan.json', 'data/roster.json', 'data/media.json']
        .map((u) => fetch(u).then((x) => {
          if (!x.ok) throw new Error(`${u}: ${x.status}`);
          return x.json();
        }))
    );
    PLAN = p; ROSTER = r; MEDIA = m;
  } catch (e) {
    $('#loading').textContent = `載入失敗：${e.message}`;
    return;
  }
  render();
  $('#loading').remove();
  $('#app').hidden = false;
  openFromUrl();
}

function render() {
  const { meta, overview } = PLAN;
  document.title = meta.title;
  const bn = $('#brand-name');
  bn.firstChild.textContent = meta.short || meta.title;
  $('#brand-sub').textContent = meta.status;
  $('#hero-status').textContent = `${meta.kicker || meta.subtitle}　·　${meta.status}`;
  $('#hero-headline').textContent = overview.headline;
  $('#hero-tagline').textContent = overview.tagline || '';
  $('#hero-body').textContent = overview.body;
  $('#hero-positions').innerHTML = `<b style="color:var(--gold)">定位不預先指派　</b>${esc(overview.positions_note)}`;
  $('#foot-note').textContent = meta.note;
  $('#foot-date').textContent = meta.updated;

  const nav = $('#nav');
  NAV.forEach(([id, label]) => {
    const a = el('a', null, label);
    a.href = `#${id}`;
    nav.append(a);
  });

  const facts = $('#hero-facts');
  overview.facts.forEach((f) => {
    const d = el('div', 'fact');
    d.append(el('b', null, f.k), el('span', null, f.l), el('i', null, f.d));
    facts.append(d);
  });

  const flow = $('#flow-list');
  PLAN.flow.forEach((s) => {
    const li = el('li', s.state === 'current' ? 'current' : null);
    li.append(el('b', null, s.n), el('strong', null, s.t), el('span', null, s.d));
    if (s.state === 'current') li.append(el('em', null, '● 目前階段'));
    flow.append(li);
  });

  const tm = PLAN.talent_model;
  if (tm) {
    $('#tm-title').textContent = tm.title;
    $('#tm-body').innerHTML = rich(tm.body);
    const host = $('#tm-stats');
    tm.stats.forEach((f) => {
      const d = el('div', 'fact');
      d.append(el('b', null, f.k), el('span', null, f.l), el('i', null, f.d));
      host.append(d);
    });
    $('#tm-note').textContent = tm.note;
  }

  renderRoster();
  renderTalents();

  const checks = $('#check-list');
  PLAN.checks.forEach((c) => {
    const d = el('div', 'check');
    d.append(el('b', null, c.k), el('span', null, c.v), el('i', null, c.note));
    checks.append(d);
  });

  const dl = $('#decision-list');
  PLAN.decisions.forEach((d) => {
    const flag = /法遵|優先度最高/.test(d.level);
    const box = el('div', flag ? 'decision flag' : 'decision');
    const head = el('div', 'decision-head');
    head.append(el('h3', null, d.t), el('span', null, d.level));
    const p = el('p', null, d.body);
    const rec = el('p', 'rec');
    rec.innerHTML = `<b>建議　</b>${esc(d.rec)}`;
    box.append(head, p, rec);
    dl.append(box);
  });

  const al = $('#alt-list');
  PLAN.alternates.forEach((a) => {
    const d = el('div', 'alt');
    const h = el('h3', null, a.name);
    h.append(el('small', null, a.native));
    const t = el('p', 'spec', a.spec);
    const tag = el('span', 'talent', a.talent);
    d.append(h, t, tag, el('p', 'why', a.why));
    al.append(d);
  });

  const nl = $('#next-list');
  PLAN.next.forEach((n) => nl.append(el('li', null, n)));
}

function specLine(c) {
  const s = c.specs;
  return `${s.height_cm}cm · ${s.cup} · ${s.bust_cm}-${s.waist_cm}-${s.hip_cm}`;
}

function renderRoster(filter) {
  const host = $('#groups');
  host.textContent = '';

  const fbar = $('#filters');
  if (!fbar.childElementCount) {
    const mk = (key, label) => {
      const b = el('button', null, label);
      b.onclick = () => {
        [...fbar.children].forEach((x) => x.classList.remove('on'));
        b.classList.add('on');
        renderRoster(key);
      };
      return b;
    };
    const all = mk(null, `全部 ${ROSTER.contestants.length}`);
    all.classList.add('on');
    fbar.append(all);
    PLAN.groups.forEach((g) => {
      const n = ROSTER.contestants.filter((c) => c.group === g.key).length;
      if (n) fbar.append(mk(g.key, `${g.label} ${n}`));
    });
  }

  PLAN.groups.forEach((g) => {
    if (filter && filter !== g.key) return;
    const list = ROSTER.contestants.filter((c) => c.group === g.key);
    if (!list.length) return;

    const sec = el('div', 'group');
    const head = el('div', 'group-head');
    const h3 = el('h3', null, '');
    h3.append(document.createTextNode(g.label + ' '), el('b', null, `${list.length} 位`));
    head.append(h3, el('p', null, g.desc));
    sec.append(head);

    const cards = el('div', 'cards');
    list.forEach((c) => cards.append(card(c)));
    sec.append(cards);
    host.append(sec);
  });
}

function card(c) {
  const m = MEDIA[c.id] || {};
  const b = el('button', 'card');
  b.type = 'button';
  b.onclick = () => openDetail(c);

  const wrap = el('div', 'card-img');
  if (m.cover) {
    const img = el('img');
    img.src = m.cover;
    img.alt = `${c.name} 形象素材`;
    img.loading = 'lazy';
    wrap.append(img);
  }
  wrap.append(el('span', 'card-tag', c.group));
  if (m.videos && m.videos.length) {
    wrap.append(el('span', 'card-vid', `影片 ${m.videos.length}`));
  }

  const body = el('div', 'card-body');
  const name = el('div', 'card-name', c.name);
  if (c.native_name) name.append(el('small', null, c.native_name));
  body.append(
    name,
    el('div', 'card-meta', `${c.ethnicity} · ${c.age} 歲`),
    el('div', 'card-talent', c.talent)
  );
  const spec = el('div', 'card-spec');
  spec.innerHTML = `<b>${c.specs.height_cm}</b>cm　<b>${c.specs.cup}</b> cup　<b>${c.specs.whr}</b> 腰臀比`;
  body.append(spec);

  b.append(wrap, body);
  return b;
}

function renderTalents() {
  const t = $('#talent-table');
  t.innerHTML = `<thead><tr>
    <th>參賽者</th><th>類型</th><th>主打才藝</th><th>共同必修</th><th>首波影片提案</th>
  </tr></thead>`;
  const tb = el('tbody');
  ROSTER.contestants.forEach((c) => {
    const tr = el('tr');
    const who = el('td', 'who', c.name);
    if (c.native_name) who.append(el('small', null, c.native_name));
    const ty = el('td', null, c.group);
    const ta = el('td', null, c.talent);
    const sec = el('td', 'ev', c.secondary || '');
    tr.append(who, ty, ta, sec, el('td', null, c.video_proposal));
    tb.append(tr);
  });
  t.append(tb);
}

/* ---------- detail ---------- */

let CURRENT = null;

function openDetail(c, silent) {
  CURRENT = c;
  if (!silent) pushOverlay('detail', { c: c.id });
  $('#detail-who').textContent = `${c.name}　${c.native_name || ''}`.trim();
  const m = MEDIA[c.id] || {};
  const host = $('#detail-inner');
  host.textContent = '';

  const head = el('div', 'dt-head');
  head.append(el('span', 'dt-tag', `${c.group}類　·　${c.ethnicity}`));
  const h2 = el('h2', null, c.name);
  if (c.native_name) h2.append(el('small', null, c.native_name));
  const badge = el('span', c.soul === '已訓練' ? 'dt-badge ready' : 'dt-badge',
    c.soul === '已訓練' ? '建模已完成' : '建模圖已備齊・待送訓');
  h2.append(badge);
  head.append(h2, el('p', 'dt-sub', `${c.age} 歲　·　${c.location}　·　${c.handle}`));
  host.append(head);

  const cols = el('div', 'dt-cols');
  const left = el('div');
  const right = el('div');

  if (m.shots && m.shots.length) {
    const g = el('div', 'dt-gallery');
    m.shots.forEach((src, i) => {
      const btn = el('button');
      btn.type = 'button';
      const img = el('img');
      img.src = src;
      img.alt = `${c.name} 素材 ${i + 1}`;
      img.loading = 'lazy';
      btn.append(img);
      btn.onclick = () => openLightbox(m.shots, i);
      g.append(btn);
    });
    const blk = el('div', 'dt-block');
    blk.append(el('h4', null, `形象素材　${m.shots.length} 張`), g);
    left.append(blk);
  }

  if (m.videos && m.videos.length) {
    const blk = el('div', 'dt-block');
    blk.append(el('h4', null, `既有影片素材　${m.videos.length} 支`));
    const vs = el('div', 'dt-videos');
    m.videos.forEach((src) => {
      const v = el('video');
      v.src = src;
      v.controls = true;
      v.preload = 'metadata';
      v.playsInline = true;
      vs.append(v);
    });
    blk.append(vs);
    left.append(blk);
  }

  const talent = el('div', 'dt-block');
  talent.append(el('h4', null, '主打才藝'), el('p', 'dt-talent', c.talent));
  const q = el('div', 'quote');
  q.innerHTML = rich(c.evidence);
  talent.append(el('h4', null, '才藝說明'), q);
  if (c.secondary) {
    talent.append(el('h4', null, '共同必修（團體表演）'), el('p', null, c.secondary));
  }
  right.append(talent);

  const vid = el('div', 'dt-block');
  vid.append(el('h4', null, '首波影片提案'), el('p', null, c.video_proposal));
  right.append(vid);

  const sp = el('div', 'dt-block');
  sp.append(el('h4', null, '身形規格'));
  const grid = el('div', 'dt-specs');
  [
    ['身高', `${c.specs.height_cm}cm`],
    ['罩杯', c.specs.cup],
    ['胸', `${c.specs.bust_cm}cm`],
    ['腰', `${c.specs.waist_cm}cm`],
    ['臀', `${c.specs.hip_cm}cm`],
    ['腰臀比', c.specs.whr],
    ['腿長比', `${c.specs.leg_ratio}%`],
  ].forEach(([k, v]) => {
    const d = el('div');
    d.append(el('b', null, k), el('span', null, v));
    grid.append(d);
  });
  sp.append(grid);
  right.append(sp);

  [['人設定位', c.archetype], ['髮色髮型', c.hair], ['臉型', c.face], ['身形敘述', c.figure]]
    .filter(([, v]) => v)
    .forEach(([k, v]) => {
      const b = el('div', 'dt-block');
      b.append(el('h4', null, k), el('p', null, v));
      right.append(b);
    });

  cols.append(left, right);
  host.append(cols);

  $('#detail').hidden = false;
  document.body.style.overflow = 'hidden';
  $('#detail').scrollTop = 0;
}

function closeDetail(silent) {
  if (!silent && !$('#detail').hidden) return popOverlay();
  $('#detail').hidden = true;
  document.body.style.overflow = '';
  CURRENT = null;
}

/* ---------- lightbox ---------- */

function openLightbox(shots, i, silent) {
  gallery = shots; gi = i;
  showShot();
  $('#lightbox').hidden = false;
  if (!silent) {
    const c = CURRENT ? { c: CURRENT.id, i } : { i };
    pushOverlay('lightbox', c);
  }
}

function closeLightbox(silent) {
  if (!silent && !$('#lightbox').hidden) return popOverlay();
  $('#lightbox').hidden = true;
}
function showShot() {
  $('#lb-img').src = gallery[gi];
  $('#lb-count').textContent = `${gi + 1} / ${gallery.length}`;
}
function step(d) {
  gi = (gi + d + gallery.length) % gallery.length;
  showShot();
}

$('#detail-close').onclick = () => closeDetail();
$('#detail-back').onclick = () => closeDetail();
$('.lb-close').onclick = () => closeLightbox();
$('.lb-prev').onclick = () => step(-1);
$('.lb-next').onclick = () => step(1);
$('#lightbox').onclick = (e) => { if (e.target.id === 'lightbox') closeLightbox(); };

document.addEventListener('keydown', (e) => {
  if (!$('#lightbox').hidden) {
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') step(-1);
    if (e.key === 'ArrowRight') step(1);
    return;
  }
  if (e.key === 'Escape' && !$('#detail').hidden) closeDetail();
});

/* Back / Forward: close down to whatever the entry we landed on describes. */
window.addEventListener('popstate', (ev) => {
  const st = ev.state || {};
  NAVSTATE.depth = st.depth || 0;
  const want = st.o || null;
  if (want !== 'lightbox' && !$('#lightbox').hidden) closeLightbox(true);
  if (want === null && !$('#detail').hidden) closeDetail(true);
  if (want === 'detail' && $('#detail').hidden) {
    const c = byId(new URLSearchParams(location.search).get('c'));
    if (c) openDetail(c, true);
  }
});

function byId(id) {
  return (ROSTER && ROSTER.contestants.find((x) => x.id === id)) || null;
}

/* A ?c=<id> link opens straight onto that contestant, so a single
   contestant can be sent to the client as its own URL. */
function openFromUrl() {
  const id = new URLSearchParams(location.search).get('c');
  const c = byId(id);
  if (!c) return;
  history.replaceState({ o: 'detail', depth: 1 }, '', location.href);
  NAVSTATE.depth = 1;
  openDetail(c, true);
}

boot();
