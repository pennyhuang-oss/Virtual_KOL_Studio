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
  ['top', '總覽'], ['division', '分工'], ['options', '營運方案'], ['timeline', '日程'],
  ['roster', '參賽者'], ['talents', '才藝'], ['specspolicy', '規格分層'],
  ['decisions', '待裁決'], ['next', '下一步'],
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

  renderDivision();
  renderAssets();
  renderModules();
  renderChoices();
  renderSpecsPolicy();
  renderCodename();
  renderTimeline();
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
    const p = el('p');
    p.innerHTML = rich(d.body).replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>');
    const rec = el('p', 'rec');
    rec.innerHTML = `<b>建議　</b>${rich(d.rec).replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>')}`;
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


/* ---------- proposal sections ---------- */

function renderDivision() {
  const d = PLAN.division;
  if (!d) return;
  $('#div-title').textContent = d.title;
  $('#div-note').textContent = d.note;
  const t = $('#div-table');
  t.innerHTML = '<thead><tr><th></th><th>兌心科技（我方）</th><th>客戶營運團隊</th></tr></thead>';
  const tb = el('tbody');
  d.rows.forEach((r) => {
    const tr = el('tr');
    tr.append(el('th', null, r.item), el('td', 'us', r.us), el('td', null, r.them));
    tb.append(tr);
  });
  t.append(tb);
}

function renderAssets() {
  const a = PLAN.assets_now;
  if (!a) return;
  $('#as-title').textContent = a.title;
  $('#as-note').textContent = a.note;
  const host = $('#as-stats');
  a.stats.forEach((f) => {
    const x = el('div', 'fact');
    x.append(el('b', null, f.k), el('span', null, f.l), el('i', null, f.d));
    host.append(x);
  });
  const c = $('#as-cons');
  a.constraints.forEach((line) => {
    const p = el('p', 'constraint');
    p.innerHTML = rich(line);
    c.append(p);
  });
}

function renderModules() {
  const m = PLAN.modules;
  if (!m) return;
  $('#mod-title').textContent = m.title;
  $('#mod-note').textContent = m.note;
  const host = $('#mod-list');
  m.rows.forEach((r) => {
    const x = el('div', 'mod');
    x.append(el('b', null, r.m), el('span', null, r.use));
    host.append(x);
  });
}

function renderSpecsPolicy() {
  const sp = PLAN.specs_policy;
  if (!sp) return;
  $('#sp-title').textContent = sp.title;
  $('#sp-body').innerHTML = rich(sp.body).replace(/\n\n/g, '<br><br>');
  const host = $('#sp-reasons');
  sp.reasons.forEach((r) => {
    const li = el('li');
    li.innerHTML = rich(r);
    host.append(li);
  });
  $('#sp-note').innerHTML = rich(sp.note);
}

function renderCodename() {
  const c = PLAN.codename;
  if (!c) return;
  $('#cn-title').textContent = c.title;
  $('#cn-body').innerHTML = rich(c.body);
  const t = $('#cn-table');
  t.innerHTML = '<thead><tr><th>代號</th><th>對應</th><th>理由</th></tr></thead>';
  const tb = el('tbody');
  c.rows.forEach((r) => {
    const tr = el('tr');
    tr.append(el('th', null, r[0]), el('td', null, r[1]), el('td', 'cn', r[2]));
    tb.append(tr);
  });
  t.append(tb);
  $('#cn-note').innerHTML = rich(c.note).replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>');
}

function renderTimeline() {
  const tl = PLAN.timeline;
  if (!tl) return;
  $('#tl-title').textContent = tl.title;
  const t = $('#tl-table');
  t.innerHTML = '<thead><tr><th>週次</th><th>客戶營運團隊</th><th>我方交付</th></tr></thead>';
  const tb = el('tbody');
  tl.rows.forEach((r) => {
    const tr = el('tr');
    const them = el('td');
    them.innerHTML = rich(r.them);
    tr.append(el('th', null, r.w), them, el('td', 'us', r.us));
    tb.append(tr);
  });
  t.append(tb);

  const c = tl.compare;
  if (!c) return;
  $('#tl-compare').hidden = false;
  $('#tlc-title').textContent = c.title;
  $('#tlc-note').innerHTML = rich(c.note);
  const ct = $('#tlc-table');
  ct.innerHTML = '<thead><tr>' +
    c.head.map((h) => `<th>${esc(h)}</th>`).join('') + '</tr></thead>';
  const ctb = el('tbody');
  c.rows.forEach((r) => {
    const tr = el('tr');
    tr.append(el('th', null, r[0]));
    r.slice(1).forEach((v) => {
      const td = el('td');
      td.innerHTML = rich(v);
      ctb.appendChild;
      tr.append(td);
    });
    ctb.append(tr);
  });
  ct.append(ctb);
}

/* ---------- the option picker ---------- */

const PICK_KEY = 'kol897-plan-choice-v1';
let CHOICE = {};

function renderChoices() {
  const groups = PLAN.choices;
  if (!groups) return;
  try { CHOICE = JSON.parse(localStorage.getItem(PICK_KEY) || '{}'); } catch (e) { CHOICE = {}; }

  const host = $('#choice-groups');
  host.textContent = '';
  groups.forEach((g) => {
    const sec = el('div', 'cgroup');
    const head = el('div', 'cgroup-head');
    head.append(el('h3', null, g.label),
      el('span', 'cgroup-n', `${g.options.length} 個方案`));
    sec.append(head);

    const grid = el('div', g.options.length === 4 ? 'opts four' : 'opts');
    g.options.forEach((o) => grid.append(optionCard(g, o)));
    sec.append(grid);
    host.append(sec);
  });
  syncPickbar();
}

function optionCard(g, o) {
  const card = el('button', 'opt');
  card.type = 'button';
  card.dataset.group = g.group;
  card.dataset.id = o.id;
  if (o.rec) card.classList.add('rec');
  if (CHOICE[g.group] === o.id) card.classList.add('on');

  const head = el('div', 'opt-head');
  head.append(el('span', 'opt-tag', o.tag), el('h4', null, o.name));
  if (o.rec) head.append(el('em', 'recmark', '建議'));
  card.append(head);
  card.append(el('p', 'opt-lead', o.lead));

  if (o.weeks || o.videos || o.load) {
    const m = el('div', 'opt-nums');
    if (o.weeks) m.append(numTile('賽程', `${o.weeks}`, '週'));
    if (o.videos) m.append(numTile('影片需求', `${o.videos}`, '支'));
    if (o.load) m.append(numTile('營運負荷', o.load, ''));
    card.append(m);
  }

  if (o.detail) {
    const dl = el('dl', 'opt-detail');
    o.detail.forEach(([k, v]) => {
      const row = el('div');
      row.append(el('dt', null, k), el('dd', null, v));
      dl.append(row);
    });
    card.append(dl);
  }

  if (o.rules) card.append(bullets('設計要點', o.rules, 'rules'));
  if (o.mods) {
    const w = el('div', 'opt-mods');
    w.append(el('b', null, '用到的 897 模組'));
    const tags = el('div', 'modtags');
    o.mods.forEach((x) => tags.append(el('span', null, x)));
    w.append(tags);
    card.append(w);
  }
  if (o.pros) card.append(bullets('優點', o.pros, 'pros'));
  if (o.cons) card.append(bullets('缺點', o.cons, 'cons'));
  if (o.meta) {
    const m = el('div', 'opt-meta');
    o.meta.forEach(([k, v]) => {
      const row = el('div');
      row.append(el('b', null, k), el('span', null, v));
      m.append(row);
    });
    card.append(m);
  }
  if (o.flag) {
    const f = el('div', 'opt-flag');
    f.append(el('b', null, `⚠ ${o.flag.t}`));
    const body = el('p');
    body.innerHTML = rich(o.flag.b);
    f.append(body);
    card.append(f);
  }

  card.append(el('span', 'opt-pickhint', CHOICE[g.group] === o.id ? '✓ 已選擇' : '點選此方案'));
  card.onclick = () => {
    CHOICE[g.group] = CHOICE[g.group] === o.id ? null : o.id;
    if (!CHOICE[g.group]) delete CHOICE[g.group];
    try { localStorage.setItem(PICK_KEY, JSON.stringify(CHOICE)); } catch (e) { /* private mode */ }
    renderChoices();
  };
  return card;
}

function numTile(label, val, unit) {
  const d = el('div', 'numtile');
  const b = el('b', null, val);
  if (unit) b.append(el('u', null, unit));
  d.append(el('span', null, label), b);
  return d;
}

function bullets(label, items, cls) {
  const w = el('div', `opt-list ${cls}`);
  w.append(el('b', null, label));
  const ul = el('ul');
  items.forEach((x) => {
    const li = el('li');
    li.innerHTML = rich(x);
    ul.append(li);
  });
  w.append(ul);
  return w;
}

/* The bar is the point of the picker: during the pitch the client clicks
   three cards and reads the resulting schedule and material load off one
   line, instead of cross-referencing three tables. */
function syncPickbar() {
  const bar = $('#pickbar');
  const groups = PLAN.choices || [];
  const chosen = groups
    .map((g) => ({ g, o: g.options.find((x) => x.id === CHOICE[g.group]) }))
    .filter((x) => x.o);

  if (!chosen.length) {
    bar.hidden = true;
    document.body.classList.remove('has-pickbar');
    reserveForBar();
    return;
  }
  bar.hidden = false;
  document.body.classList.add('has-pickbar');

  const sel = $('#pickbar-sel');
  sel.textContent = '';
  chosen.forEach(({ g, o }) => {
    const chip = el('span', 'chip');
    chip.append(el('b', null, g.letter), el('i', null, o.tag),
      el('span', null, o.name));
    sel.append(chip);
  });

  const v = chosen.find((x) => x.g.group === 'voting');
  const out = $('#pickbar-out');
  out.textContent = '';
  if (v && v.o.weeks) {
    out.append(el('span', null, `賽程約 ${v.o.weeks} 週`),
      el('span', null, `影片需求 ${v.o.videos} 支`),
      el('span', null, `營運負荷 ${v.o.load}`));
  } else if (v) {
    out.append(el('span', null, '此方案需搭配 A 或 B 使用'));
  }
  if (chosen.length === groups.length) {
    out.append(el('span', 'done', '✓ 三項都已選定'));
  } else {
    const left = groups.filter((g) => !CHOICE[g.group]).map((g) => g.letter);
    out.append(el('span', 'todo', `尚未選：${left.join('、')}`));
  }
  reserveForBar();
}

/* The bar's height depends on how much the chips wrap, so reserve the space
   it actually occupies rather than a guessed constant. */
function reserveForBar() {
  requestAnimationFrame(() => {
    const bar = $('#pickbar');
    const h = bar.hidden ? 0 : bar.getBoundingClientRect().height;
    document.body.style.paddingBottom = h ? `${Math.ceil(h) + 12}px` : '';
  });
}

window.addEventListener('resize', reserveForBar);

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

$('#pickbar-clear').onclick = () => {
  CHOICE = {};
  try { localStorage.removeItem(PICK_KEY); } catch (e) { /* private mode */ }
  renderChoices();
};

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
