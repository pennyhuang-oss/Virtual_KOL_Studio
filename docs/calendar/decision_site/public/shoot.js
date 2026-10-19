// 2027 KOL 桌曆｜M-3 寫真拍攝企劃（R3：24 套雙款＋景別、角度與構圖）。企劃內容來自 data.js 的 m3（產生自 data/cal_m3_shoot_plan.json）；本頁沒有任何生成圖。
// Penny 的回饋只存在本機瀏覽器 localStorage（cal2027-shoot-v1:<SHA>），不送到伺服器；沒有追蹤或分析。
// v4 的回饋另存在同一筆資料的 v4 欄位；v1／v2／v3 留下的欄位原樣保留，只顯示成「舊版」、不算 v4。載入時不改寫，只有 Penny 動手後才存。
// 構圖示意只是方框與位置（依企劃數字畫），不是照片，也不是生成圖。
// 第二階段素材選擇（cal2027-materials-v1:<SHA>）本頁不讀、不寫、不刪。
'use strict';
(() => {
  const D = window.CAL_DATA;
  const app = document.getElementById('app');
  if (!D || !D.m3 || !D.mat || !D.m3.sets) { app.textContent = '資料載入失敗。'; return; }

  const SHA = D.fixed_sha;
  const KEY = 'cal2027-shoot-v1:' + SHA;
  const IMG = D.images;
  const P = D.m3;
  const CUR = P.version;
  const MP = {};
  const ITEM = {};
  D.mat.people.forEach(p => { MP[p.pid] = p; p.items.forEach(it => { ITEM[it.id] = { ...it, pid: p.pid }; }); });
  const SETS = P.sets;
  const SET = {};
  SETS.forEach(s => { SET[s.id] = s; });
  const PEOPLE = P.people;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const oneLine = s => String(s).trim().replace(/\s*\n\s*/g, '／');
  const str = x => (typeof x === 'string' ? x : '');
  const BOOK = { H: '橫式款', V: '直式款' };
  const ORIGIN = { new: '新企劃', 'accepted-v2-main': 'Penny 已接受的方向', 'accepted-v2-alt': 'Penny 採用的 v2 替代方向' };

  // ---------- 舊版（v1／v2）回饋：只讀 ----------
  const OLD_CH = { main: '接受主方向', alt: '改用替代方向', edit: '想修改' };
  const OLD_Q = {
    hv: { label: '橫直構圖', 'shoot-plan-v1': { both: '同意：同一造型橫、直各拍一張', one: '先只拍一種', unsure: '還不確定' },
      'shoot-plan-v2': { both: '先採用：同一造型橫、直各拍一張', one: '先只拍 3:4 直幅，等版面決定', unsure: '還不確定' } },
    first: { label: '首批試拍（已撤回）', 'shoot-plan-v1': { ok: '同意首批 4 位與上限', swap: '想換首批人選或上限', hold: '先不要試拍' } },
    phase1: { label: '第一階段試拍', 'shoot-plan-v2': { ok: '同意方向：第一階段先試 Iris 一位', swap: '想換第一階段的人', hold: '先不要試拍' } },
  };
  const VER = v => (v === 'shoot-plan-v1' ? 'v1' : (v === 'shoot-plan-v2' ? 'v2' : v));
  let RAW = {};
  let storageOK = true;
  try { const s = JSON.parse(localStorage.getItem(KEY)); if (s && typeof s === 'object') RAW = s; } catch (e) { storageOK = false; }
  function oldFor(pid) {
    const q = (RAW.p || {})[pid];
    if (!q || typeof q !== 'object') return { choices: [], notes: [] };
    const prev = Array.isArray(q.prev) ? q.prev : [];
    const choices = prev.filter(x => x && OLD_CH[x.c]).map(x => ({ c: x.c, v: str(x.v) || 'shoot-plan-v1' }));
    if (OLD_CH[q.c]) choices.push({ c: q.c, v: str(q.v) || 'shoot-plan-v1' });
    const notes = prev.filter(x => x && str(x.note).trim()).map(x => ({ note: x.note, v: str(x.v) || 'shoot-plan-v1' }));
    if (str(q.note).trim()) notes.push({ note: q.note, v: str(q.nv) || 'shoot-plan-v1' });
    return { choices, notes };
  }
  function oldQs() {
    const out = [];
    (Array.isArray(RAW.qprev) ? RAW.qprev : []).forEach(x => { if (x && x.k) out.push({ k: x.k, a: x.a, v: str(x.v) || 'shoot-plan-v1' }); });
    Object.entries(RAW.q || {}).forEach(([k, a]) => { if (typeof a === 'string' && a) out.push({ k, a, v: str((RAW.qv || {})[k]) || 'shoot-plan-v1' }); });
    return out.map(x => { const T = OLD_Q[x.k] || {}; return `${T.label || x.k}：${VER(x.v)}「${(T[x.v] || {})[x.a] || x.a}」`; });
  }
  function oldGnotes() {
    const out = (Array.isArray(RAW.gprev) ? RAW.gprev : []).filter(x => x && str(x.note).trim()).map(x => ({ note: x.note, v: str(x.v) || 'shoot-plan-v1' }));
    if (str(RAW.gnote).trim()) out.push({ note: RAW.gnote, v: str(RAW.gnv) || 'shoot-plan-v1' });
    return out;
  }
  const oldLine = pid => {
    const o = oldFor(pid);
    const a = o.choices.map(x => `${VER(x.v)}「${OLD_CH[x.c]}」`);
    const b = o.notes.map(x => `備註（${VER(x.v)}）：${oneLine(x.note)}`);
    return [...a, ...b].join('；');
  };
  // v3（R2）回饋：每套一筆，題目與整體備註各一筆；只讀
  const V3RAW = RAW.v3 && typeof RAW.v3 === 'object' ? RAW.v3 : {};
  const CH3 = { ok: '接受', edit: '想修改' };
  function oldV3(id) {
    const x = (V3RAW.sets || {})[id];
    if (!x || typeof x !== 'object') return '';
    const a = [];
    if (CH3[x.c]) a.push(`v3「${CH3[x.c]}」`);
    if (str(x.note).trim()) a.push(`備註（v3）：${oneLine(x.note)}`);
    return a.join('；');
  }
  function oldV3Qs() {
    return Object.entries(V3RAW.q || {}).filter(([k, x]) => x && typeof x === 'object' && (QS[k] || {}).opts && ((QS[k].opts[x.c]) || str(x.note).trim()))
      .map(([k, x]) => `${QS[k].label}：v3「${QS[k].opts[x.c] || '未回覆'}」${str(x.note).trim() ? `，備註：${oneLine(x.note)}` : ''}`);
  }
  const oldV3G = () => (str(V3RAW.gnote).trim() ? oneLine(V3RAW.gnote) : '');

  // ---------- v4 回饋（題目與選項沿用 v3，不新增問卷） ----------
  const CH = { ok: '接受', edit: '想修改' };
  const QS = {
    months_h: { label: '橫式款月份推薦', opts: { ok: '接受', edit: '想調整（寫在備註）' } },
    months_v: { label: '直式款月份推薦', opts: { ok: '接受', edit: '想調整（寫在備註）' } },
    layout: { label: '版面與構圖建議', opts: { ok: '接受', edit: '想修改（寫在備註）' } },
    iris_first: { label: 'Iris 首張試拍候選', opts: { v: '同意先試 V-iris-chen（不是費用核准）', h: '想先試 H-iris-chen', edit: '想修改（寫在備註）' } },
    assign: { label: '已接受方向的 H／V 分配', opts: { ok: '接受', edit: '想對調（寫在備註）' } },
  };
  function loadV4() {
    const v = RAW.v4 && typeof RAW.v4 === 'object' ? RAW.v4 : {};
    const out = { ver: CUR, sets: {}, q: {}, gnote: str(v.gnote) };
    SETS.forEach(s => { const x = (v.sets || {})[s.id] || {}; out.sets[s.id] = { c: CH[x.c] ? x.c : '', note: str(x.note) }; });
    Object.keys(QS).forEach(k => { const x = (v.q || {})[k] || {}; out.q[k] = { c: QS[k].opts[x.c] ? x.c : '', note: str(x.note) }; });
    return out;
  }
  let V4 = loadV4();
  function save() {
    RAW.v4 = V4;
    try { localStorage.setItem(KEY, JSON.stringify(RAW)); storageOK = true; } catch (e) {
      if (storageOK) toast('這個瀏覽器不允許儲存（例如無痕模式）：重新整理後回饋會消失，請先複製。');
      storageOK = false;
    }
  }

  // ---------- 畫面元件 ----------
  function fig(iid, cap, label) {
    const m = IMG[iid];
    if (!m) return '';
    const hi = m.res === 'hires';
    return `<figure class="fig"><button type="button" class="zoom" data-img="${esc(iid)}" data-cap="${esc(cap)}" aria-label="放大：${esc(cap)}">` +
      `<img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" loading="lazy" decoding="async" alt="${esc(cap)}">` +
      `<span class="resb ${hi ? 'hires' : 'lowres'}">${hi ? '高解析預覽' : '低解析'}</span><span class="zi" aria-hidden="true">放大</span></button>` +
      (label ? `<figcaption>${label}</figcaption>` : '') + '</figure>';
  }
  const USE_CLS = { 表情: 'u-expr', 場景: 'u-scene', 服裝材質: 'u-cloth', 身分: 'u-id' };
  function refFig(r, pid) {
    const it = ITEM[r.id];
    const nobody = /不作身材參考/.test(r.note);
    const note = r.note.replace(/；?不作身材參考：既有照片的身材不符合設定（Penny）/, '');
    return fig(it.img, `${MP[pid].name}｜${r.id}｜只參考${r.use}｜既有照片，不是新成品`,
      `<span class="tag use ${USE_CLS[r.use] || ''}">參考：${esc(r.use)}</span>${nobody ? ' <span class="tag nobody">不作身材參考</span>' : ''} <code>${esc(r.id)}</code> ${esc(note)}`);
  }
  const ul = a => `<ul class="facts">${a.map(x => `<li>${esc(x)}</li>`).join('')}</ul>`;
  const tbl = (head, rows, cls) => `<div class="tbl"><table${cls ? ` class="${cls}"` : ''}><thead><tr>${head.map(h => `<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>` +
    rows.map(r => `<tr>${r.map(c => `<td>${c && c.html ? c.html : esc(c)}</td>`).join('')}</tr>`).join('') + '</tbody></table></div>';
  const link = id => ({ html: `<a href="#c-${esc(id)}">${esc(id)}</a>` });
  const outfitList = o => `<ul class="facts">${Object.entries(o).map(([k, v]) => `<li><b>${esc(k)}</b>：${esc(v)}</li>`).join('')}</ul>`;

  function decSec() {
    const O = P.owner_r2, Sm = O.summary, O3 = P.owner_r3;
    const hasOld = PEOPLE.some(p => oldLine(p.pid)) || oldQs().length || oldGnotes().length || SETS.some(s => oldV3(s.id)) || oldV3Qs().length || oldV3G();
    return `<section class="sec" id="dec"><h2>Penny 最新要求（R3）與已生效的決定</h2>
<pre class="verb">${esc(O3.verbatim.requirement)}</pre>
<p class="callout warn"><b>${esc(O3.verbatim.not_approved.split('\n')[0])}</b>本頁每套的景別與角度都是<b>執行者的推薦</b>，不是 owner 已核准；Iris 兩款「身體正面、有笑容」是 Penny 已提出的要求。</p>
<details class="info"><summary>R3 指令：尊重既有要求（逐字）</summary><pre class="verb">${esc(O3.verbatim.keep_existing)}</pre></details>
<h3>R2 已生效的決定（不變）</h3>
<pre class="verb">${esc(O.verbatim.decisions)}</pre>
<p class="note">以上逐字保存（主管轉述）。執行整理：</p>
${ul(Sm.decided)}
<p class="note"><b>已接受的方向</b>（各保留為其中一款，另一款另設完全不同的服裝與場景；放 H 或 V 是執行者的推薦，不是 Penny 的決定）：</p>
${ul(Sm.accepted_directions.map(x => `${MP[x.pid].name}：${x.what}`))}
<p class="callout warn"><b>${esc(Sm.iris_first)}</b> 尚未授權：${esc(Sm.not_authorized.join('、'))}。尚未核准：${esc(Sm.not_approved.join('、'))}。</p>
<div class="callout${hasOld ? ' warn' : ''}">${hasOld ? '這個瀏覽器裡有舊版（v1／v2／v3）的回饋：都還在，各套與各位的區塊會列出來，<b>不算</b>這一版（v4）的回覆。' : '這個瀏覽器沒有舊版回饋紀錄。'}</div>
</section>`;
  }

  function bookTable(b) {
    const rows = SETS.filter(s => s.book === b).sort((x, y) => x.month - y.month);
    return tbl(['月', 'ID', '人設', '主題', '環境', '服裝', '色彩', '姿態', '表情', '性感', '攝影方法', '景別｜身體方向｜臉與視線｜拍攝角度'],
      rows.map(s => [`${s.month} 月`, link(s.id), s.name, s.theme, s.env, Object.values(s.outfit).join('、'), s.palette, s.pose, s.expr, s.sexy, s.method, s.cam.line]), 'book');
  }
  function booksSec() {
    return `<section class="sec" id="books"><h2>兩本總覽與月份推薦</h2>
<p class="note">月份只是推薦，待 Penny 拍板。每本 12 位各一個月；同月兩本是不同的人。</p>
<h3>月份對照</h3>
<div class="mgrid2">${P.months.map(m => `<div class="mrow2"><span class="mn2">${m.m} 月</span>` +
      `<a class="mchip h" href="#c-${esc(m.H)}"><b>橫</b> ${esc(SET[m.H].name)}<small>${esc(m.why_h)}</small></a>` +
      `<a class="mchip v" href="#c-${esc(m.V)}"><b>直</b> ${esc(SET[m.V].name)}<small>${esc(m.why_v)}</small></a></div>`).join('')}</div>
${ul(P.month_rules)}
<details class="info" open><summary>橫式款 12 套總覽（依推薦月份）</summary>${bookTable('H')}</details>
<details class="info"><summary>直式款 12 套總覽（依推薦月份）</summary>${bookTable('V')}</details>
</section>`;
  }

  // ---------- 攝影總覽（兩本各 12 張；手機上每列變成一張小卡） ----------
  const PH_HEAD = ['月', '人物', '景別', '身體方向', '臉部方向', '視線', '相機角度', '人物位置', '主要展示重點'];
  function photoTable(b) {
    const rows = SETS.filter(s => s.book === b).sort((x, y) => x.month - y.month);
    const cells = s => [`${s.month} 月`, { html: `<a href="#c-${esc(s.id)}">${esc(s.name)}</a> <code>${esc(s.id)}</code>` }, s.cam.shot.zh, s.cam.body.short, s.cam.face.zh,
      s.cam.gaze.zh, s.cam.angle.short, s.cam.pos, s.cam.focus];
    return `<div class="tbl"><table class="photo"><thead><tr>${PH_HEAD.map(h => `<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>` +
      rows.map(s => `<tr data-set="${esc(s.id)}">${cells(s).map((c, i) => `<td data-label="${esc(PH_HEAD[i])}">${c && c.html ? c.html : esc(c)}</td>`).join('')}</tr>`).join('') +
      '</tbody></table></div>';
  }
  const ORD = ['胸上', '腰上', '大腿中段以上', '膝上', '全身', '坐姿全身', '席地坐姿全身', '斜躺全身', '坐姿到水面', '正面', '約30度斜側', '約45度斜側', '側面', '側面斜躺'];
  const cnt = o => Object.entries(o).sort((a, b) => ORD.indexOf(a[0]) - ORD.indexOf(b[0])).map(([k, v]) => `${k} ${v}`).join('、');
  function photoSec() {
    const F = P.photo;
    const major = P.adjust.filter(a => a.major.length), minor = P.adjust.filter(a => !a.major.length);
    return `<section class="sec" id="photo"><h2>攝影總覽：景別、角度與構圖（推薦，待 Penny 定案）</h2>
<p class="note">${esc(F.summary)}</p>
${['H', 'V'].map(b => `<h3>${BOOK[b]}（${b === 'H' ? '16:9' : '3:4'}）攝影總覽</h3>${photoTable(b)}
<p class="note"><b>景別：</b>${esc(cnt(F.counts[b].shot))}；<b>身體方向：</b>${esc(cnt(F.counts[b].body))}。</p>
<p class="note"><b>節奏：</b>${esc(F.rhythm[b])}</p><p class="note"><b>依推薦月份：</b>${esc(F.sequence[b])}</p>`).join('')}
${ul([`近景：${F.rhythm.near}`, `角度：${F.rhythm.angles}`, `同一位的兩款：${F.rhythm.pair}`])}
<h3>調整較大的 ${major.length} 套</h3><p class="note">${esc(F.major_rule)}</p>
${tbl(['ID', '原景別', '新設計', '原因', '調整與理由'], major.map(a => [link(a.id), a.from, a.line, a.major.join('、'), `${a.change}${a.why}`]), 'adj')}
<details class="info"><summary>其他 ${minor.length} 套的調整（含已接受方向）</summary>
${tbl(['ID', '來源', '原景別', '新設計', '調整內容'], minor.map(a => [link(a.id), ORIGIN[a.origin], a.from, a.line, a.change]), 'adj')}</details>
<details class="info"><summary>共同規則與 prompt 一致性檢查</summary><h4>共同規則</h4>${ul(F.rules)}<h4>逐套檢查（產生資料時執行，不通過就無法建置）</h4>${ul(F.checks)}</details>
</section>`;
  }

  function frameTable(fr) {
    const crop = ['chest', 'waist', 'thigh', 'knee'].includes(fr.shot);
    return tbl(['項目', '內容'], [['景別', fr.shot_zh], [crop ? '頭頂上方留白' : '人物佔比', crop ? `約 ${fr.headroom}%` : `約佔${fr.fill_of} ${fr.fill}%`],
      ['焦段／距離（參考）', `${fr.f}mm／約 ${fr.d} 公尺`], ['視野（寬×高）', `${fr.view_w}×${fr.view_h} 公尺`],
      ['相機與畫面中心', `相機約 ${fr.cam_m} 公尺高、畫面中心約 ${fr.centre_m} 公尺高，換算俯仰約 ${fr.tilt_deg > 0 ? '+' : ''}${fr.tilt_deg} 度`],
      ['原生尺寸', fr.native], ['版面適配', fr.fit]]);
  }
  // 構圖示意：只畫畫框、頭與身體範圍（依企劃數字），不是照片
  function schem(s) {
    const k = s.frame.sch;
    return `<figure class="schw"><div class="nb2 sch r${s.book}" role="img" aria-label="${esc(`${s.id} 構圖示意：${s.cam.line}`)}">` +
      `<span class="sch-fig" data-x="${k.x}" data-w="${k.w}" data-top="${k.top}" data-bot="${k.bot}" data-head="${k.head}"${k.lie ? ' data-lie="1"' : ''}><i class="sch-h"></i><i class="sch-b"></i></span></div>` +
      `<figcaption class="sch-t"><b>${BOOK[s.book]}新照片 ${esc(s.ratio)}：尚未生成</b>框內只是構圖示意（人物範圍與頭的位置），不是照片</figcaption></figure>`;
  }
  function camRow(s) {
    const c = s.cam;
    return `<dl class="camrow" aria-label="攝影設計">` +
      `<div><dt>景別</dt><dd>${esc(c.shot.zh)}</dd></div><div><dt>身體方向</dt><dd>${esc(c.body.short)}</dd></div>` +
      `<div><dt>臉與視線</dt><dd>${esc(c.face.zh)}・${esc(c.gaze.short)}</dd></div><div><dt>拍攝角度</dt><dd>${esc(c.angle.short)}</dd></div></dl>`;
  }
  function camDetail(s) {
    const c = s.cam;
    return `<details class="info camd"><summary>攝影設計細節：七個欄位、理由與調整</summary>
<dl class="pdl small">
<dt>1. 景別</dt><dd>${esc(c.shot.zh)}</dd>
<dt>2. 畫面上下界</dt><dd>${esc(c.bounds.zh)}</dd>
<dt>3. 身體朝向</dt><dd>${esc(c.body.short)}：${esc(c.body.zh)}</dd>
<dt>4. 臉部朝向與視線</dt><dd>${esc(c.face.zh)}，${esc(c.gaze.zh)}</dd>
<dt>5. 相機高度與俯仰</dt><dd>${esc(c.angle.zh)}<br><small>${esc(c.angle.ref)}（焦段與距離只是參考，不是生成保證）</small></dd>
<dt>6. 畫面配置</dt><dd>${esc(c.comp.zh)}</dd>
<dt>7. 攝影目的</dt><dd>${esc(c.purpose.zh)}</dd>
<dt>選擇理由</dt><dd>${esc(c.why)}</dd>
<dt>本輪調整</dt><dd>${c.major.length ? `<span class="tag o-acc">調整較大</span> ` : ''}${esc(c.change)}</dd>
</dl></details>`;
  }
  function card(s) {
    const x = V4.sets[s.id];
    const o3 = oldV3(s.id);
    return `<article class="scard ${s.book === 'H' ? 'bh' : 'bv'}" id="c-${esc(s.id)}" data-set="${esc(s.id)}">
<p class="sc-head"><code class="sid">${esc(s.id)}</code> <span class="tag book">${BOOK[s.book]}（${esc(s.ratio)}）</span> <span class="tag ${s.origin === 'new' ? 'o-new' : 'o-acc'}">${esc(ORIGIN[s.origin])}</span> <span class="tag mon">推薦 ${s.month} 月</span> <span class="st none" data-st="${esc(s.id)}"></span></p>
<p class="sc-theme">${esc(s.theme)}</p>
${camRow(s)}
${schem(s)}
<dl class="pdl">
<dt>攝影</dt><dd class="camline">${esc(s.cam.line)}</dd>
<dt>場景</dt><dd>${esc(s.scene)}</dd>
<dt>服裝</dt><dd>${outfitList(s.outfit)}</dd>
<dt>姿態</dt><dd>${esc(s.pose)}${esc(s.hands)}</dd>
<dt>表情</dt><dd>${esc(s.expr)}；${esc(s.gaze)}</dd>
<dt>光影</dt><dd>主光：${esc(s.light['主光'])}<br>補光：${esc(s.light['補光'])}</dd>
</dl>
${camDetail(s)}
<p class="pn-n">既有參考照片（只按標示用途參考，不是新構圖的成品）：</p>
<div class="rgrid">${s.refs.map(r => refFig(r, s.pid)).join('')}</div>
<details class="info"><summary>身材、妝髮、焦段數字與差異</summary>
<dl class="pdl small">
<dt>身材設定</dt><dd>${esc(s.meas)}</dd>
<dt>畫面上怎麼呈現</dt><dd>${esc(s.body_show)}</dd>
<dt>髮型／妝感</dt><dd>${esc(s.hair)}<br>${esc(s.makeup)}</dd>
<dt>為何符合她</dt><dd>${esc(s.why)}</dd>
<dt>與另一款的差異</dt><dd>${esc(s.vs_other)}</dd>
</dl>
${frameTable(s.frame)}
${tbl(['風險', '處理'], s.risks)}
</details>
<details class="info"><summary>prompt 草稿（尚未執行）</summary><pre class="prompt">${esc(s.prompt)}</pre></details>
${o3 ? `<p class="oldfb">舊版 v3 回饋（保留，不算 v4）：${esc(o3)}</p>` : ''}
<fieldset class="fb"><legend>回饋：${esc(s.id)}</legend>
<div class="fb-opts">${Object.entries(CH).map(([k, v]) => `<label class="fb-o"><input type="radio" name="s-${esc(s.id)}" value="${k}" data-s="${esc(s.id)}"${x.c === k ? ' checked' : ''}> ${esc(v)}</label>`).join('')}</div>
<label class="lbl" for="n-${esc(s.id)}">備註</label>
<textarea id="n-${esc(s.id)}" data-n="${esc(s.id)}" rows="2" maxlength="2000" placeholder="例：想改成全身；想看側面；衣服想換顏色">${esc(x.note)}</textarea>
<button type="button" class="btn ghost small" data-clear="${esc(s.id)}">清除這套的回饋</button>
</fieldset></article>`;
  }
  function person(p, i) {
    const old = oldLine(p.pid);
    return `<section class="sec person3" id="p-${esc(p.pid)}">
<div class="ph"><div class="ph-face">${fig(MP[p.pid].face, `${MP[p.pid].name}｜辨識用正臉（既有照片）`)}</div>
<div class="ph-t"><h2>${i + 1}. ${esc(MP[p.pid].name)}${MP[p.pid].native ? ` <span class="nat">${esc(MP[p.pid].native)}</span>` : ''}</h2>
<p class="cc-meta">身材設定：${esc(p.meas)}</p></div></div>
<div class="fbq"><p class="pn-h">Penny 回饋（逐字）</p><pre class="verb">${esc(p.feedback)}${p.shared ? '\n' + esc(p.shared) : ''}</pre>
<p class="pn-h">怎麼落實</p>${ul(p.applied)}</div>
${old ? `<p class="oldfb">舊版 v1／v2 回饋（保留，不算 v4）：${esc(old)}</p>` : ''}
<div class="pair">${card(SET['H-' + p.pid])}${card(SET['V-' + p.pid])}</div>
</section>`;
  }

  function compSec() {
    const C = P.composition;
    return `<section class="sec" id="comp"><h2>構圖與生成提案（建議，未批准）</h2>
${tbl(['款式', '建議'], C.recommend.map(x => [x.k, x.v]))}
<h3>評估</h3>${ul(C.eval)}<h3>限制</h3>${ul(C.limits)}<p class="note">${esc(C.method)}</p></section>`;
  }
  function costSec() {
    const K = P.execution.cost, M = P.execution.model, I = K.iris_first;
    return `<section class="sec" id="cost"><h2>費用與 Iris 首張試拍（提案）</h2>
<p class="callout warn"><b>${esc(K.status)}</b> ${esc(K.gate)}</p>
<h3>Iris 首張：建議 <a href="#c-${esc(I.set)}">${esc(I.set)}</a></h3>${ul(I.why)}
${tbl(['項目', '內容'], I.plan.map(x => [x.k, x.v]))}
<h3>24 套的情境試算（不是預算）</h3>
${tbl(['情境', '請求數', '依 credits_exact 報價', '若實扣是顯示值（每次 1）'], K.scenarios.map(x => [x.k, String(x.n), x.exact, x.display]))}
<p class="note">${esc(K.scenario_note)}</p>
<details class="info"><summary>精確報價、歷史實扣與未知</summary>
<h4>精確報價（預檢，不送出工作）</h4>${tbl(['設定', '回傳'], K.quote.map(x => [x.cfg, x.r]))}
<p class="note">${esc(K.quote_note)}</p>
<h4>歷史實扣與紀錄</h4>${tbl(['項目', '數值', '依據', '等級'], K.history.map(x => [x.k, x.v, x.basis, x.level]))}
<h4>計價方式、張數、上限、異常</h4>${tbl(['項目', '說明'], K.facts.map(x => [x.k, x.v]))}
<p class="note"><b>未知：</b>${esc(M.unknown.join('、'))}</p>
<p class="note"><b>怎麼拍：</b>${esc(M.recommend)}（Soul ID 不列在公開頁）</p></details></section>`;
  }
  function outSec() {
    const oq = oldQs(), og = oldGnotes(), oq3 = oldV3Qs(), og3 = oldV3G();
    return `<section class="sec" id="out"><h2>回饋與複製</h2>
<div class="callout">回饋只存在這個瀏覽器，<b>不會送到伺服器</b>，也不會通知主管。<b>未回覆不算接受。</b>複製後請貼回 ChatGPT。這是對企劃方向的回饋，不是生成授權或費用核准。</div>
<h3>想請 Penny 決定的事</h3><ol class="facts">${P.questions.map(x => `<li>${esc(x)}</li>`).join('')}</ol>
<p class="note">第 1 題在各套卡片上選；其他在下面選：</p>
${Object.entries(QS).map(([k, Q]) => `<fieldset class="fb"><legend>${esc(Q.label)}</legend><div class="fb-opts col">${Object.entries(Q.opts).map(([v, t]) =>
      `<label class="fb-o"><input type="radio" name="q-${k}" value="${v}" data-q="${k}"${V4.q[k].c === v ? ' checked' : ''}> ${esc(t)}</label>`).join('')}</div>
<label class="lbl" for="qn-${k}">備註</label><textarea id="qn-${k}" data-qn="${k}" rows="1" maxlength="1500">${esc(V4.q[k].note)}</textarea></fieldset>`).join('')}
${oq3.length ? `<p class="oldfb">v3 題目的回答（保留，不算 v4）：${esc(oq3.join('；'))}</p>` : ''}
${oq.length ? `<p class="oldfb">v1／v2 題目的回答（保留，不算 v4）：${esc(oq.join('；'))}</p>` : ''}
<label class="lbl" for="gnote">整體備註</label>
<textarea id="gnote" rows="3" maxlength="3000" placeholder="例：整體想要更多戶外；性感程度想再高一點">${esc(V4.gnote)}</textarea>
${og3 ? `<p class="oldfb">v3 整體備註（保留）：${esc(og3)}</p>` : ''}
${og.length ? `<p class="oldfb">v1／v2 整體備註（保留）：${esc(og.map(x => `${VER(x.v)}「${oneLine(x.note)}」`).join('；'))}</p>` : ''}
<div class="actions"><button type="button" class="btn" id="act-copy">複製回饋</button><button type="button" class="btn danger" id="act-reset">清除 v4 回饋</button></div>
<label class="lbl" for="out-text">將複製的文字（預覽）</label><textarea id="out-text" rows="16" readonly></textarea>
</section>`;
  }
  function refsSec() {
    const A = P.aaliya, O = P.owner_refs;
    return `<section class="sec" id="refs"><h2>參考</h2>
<details class="info"><summary>Penny 喜歡的 4 張（第二階段備選，不變）</summary><p class="note">${esc(O.note)}</p>
<div class="ogrid">${O.items.map(x => { const it = ITEM[x.id]; return `<article class="oc">${fig(it.img, `${MP[it.pid].name}｜${x.id}｜既有照片`)}<p class="oc-w">${esc(x.what)}</p></article>`; }).join('')}</div></details>
<details class="info"><summary>Aaliya 的拍攝方法（主管已 PASS；只借方法，不用她的臉）</summary>
<p class="callout warn"><b>⚠ ${esc(A.warning)}</b></p>
<div class="agrid">${A.items.map(x => `<article class="ac">${fig(P.aaliya_img[x.key], `Aaliya｜${x.form}｜既有照片，只參考拍法`, `<span class="tag t-ref">Aaliya 既有照片</span> ${esc(x.form)}`)}</article>`).join('')}</div>
<dl class="mdl">${A.method.map(m => `<dt>${esc(m.item)}</dt><dd>${esc(m.how)}</dd>`).join('')}</dl></details>
<ul class="facts"><li><a href="index.html">第二階段：為入選人設挑照片</a>：素材選擇照舊保留在那一頁，本頁不讀也不改。</li>
<li>完整企劃與攝影設計：repo 的 <code>docs/calendar/CAL_18_M3_SHOOT_PLAN.md</code>（R3）；R2 Owner 決策逐字紀錄：<code>docs/calendar/CAL_19_M3_R2_OWNER_DECISION.md</code>。</li></ul></section>`;
  }

  function render() {
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    $('#planver').textContent = `${P.version}（${P.round}，${P.written_on}）`;
    app.innerHTML = decSec() + photoSec() + booksSec() +
      `<section class="sec" id="people"><h2>12 位 × 橫式款／直式款</h2>
<ul class="facts"><li>每位兩套獨立企劃：服裝與場景都不同。左邊是橫式款（16:9），右邊是直式款（3:4）；手機上上下排列。</li>
<li>每張卡片最上面直接寫<b>景別｜身體方向｜臉與視線｜拍攝角度</b>；七個攝影欄位的細節、理由與本輪調整在「攝影設計細節」展開。</li>
<li>虛線框是「尚未生成」的新照片位置，裡面的方框與圓點只是<b>構圖示意</b>（人物範圍與頭的位置，依企劃數字畫），不是照片。卡片下方的照片都是<b>既有照片</b>，只按標示的用途參考（表情／場景／服裝材質／身分），不是新構圖的成品；身材一律以設定數字為準。</li></ul>
<div class="ov">${PEOPLE.map((p, i) => { const m = IMG[MP[p.pid].face]; return `<a class="rs" href="#p-${esc(p.pid)}"><img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" alt="" loading="lazy" decoding="async"><span class="rs-t"><b>${i + 1}. ${esc(MP[p.pid].name)}</b><span class="rs-p" data-ov="${esc(p.pid)}"></span></span></a>`; }).join('')}</div>
</section>` + PEOPLE.map(person).join('') + compSec() + costSec() + outSec() + refsSec();
    placeSchem();
    SETS.forEach(s => refresh(s.id));
    refreshOut();
  }
  // CSP 不允許 HTML 內嵌 style，所以構圖示意的位置在插入後用 CSSOM 設定
  function placeSchem() {
    $$('.sch-fig').forEach(f => {
      const n = k => Number(f.dataset[k]);
      const w = n('w'), x = n('x'), top = n('top'), bot = n('bot'), head = n('head');
      f.style.left = `${Math.max(0, Math.min(1 - w, x - w / 2)) * 100}%`;
      f.style.width = `${w * 100}%`;
      f.style.top = `${top * 100}%`;
      f.style.height = `${(bot - top) * 100}%`;
      const h = f.querySelector('.sch-h'), b = f.querySelector('.sch-b');
      const box = f.parentElement.getBoundingClientRect();
      const headPx = head * box.height;
      if (f.dataset.lie) { h.style.left = '0'; h.style.top = '0'; }
      h.style.width = h.style.height = `${headPx}px`;
      b.style.top = f.dataset.lie ? '30%' : `${headPx}px`;
      if (f.dataset.lie) b.style.left = `${headPx}px`;
    });
  }
  window.addEventListener('resize', () => { clearTimeout(placeSchem.t); placeSchem.t = setTimeout(placeSchem, 150); });
  function refresh(id) {
    const c = V4.sets[id].c;
    const el = $(`[data-st="${id}"]`);
    if (el) { el.textContent = c ? CH[c] : '未回覆'; el.className = `st ${c === 'ok' ? 'conf' : (c ? 'draft' : 'none')}`; }
    const pid = SET[id].pid;
    const ov = $(`[data-ov="${pid}"]`);
    if (ov) ov.textContent = ['H', 'V'].map(b => `${b}：${V4.sets[b + '-' + pid].c ? CH[V4.sets[b + '-' + pid].c] : '未回覆'}`).join('｜');
  }
  function buildText() {
    const L = ['TASK-CAL-001／M-3／R3｜24 套寫真景別、角度與構圖細化｜Penny 企劃回饋',
      `企劃版本：${P.version}（${P.round}）｜頁面版本：${PAGE_COMMIT || '本機預覽（未部署）'}`,
      '說明：這是對 24 套企劃（含景別與角度推薦）的回饋，不是生成授權，也不是費用核准；未回覆不算接受。'];
    let ok = 0, ed = 0;
    ['H', 'V'].forEach(b => {
      L.push('', `【${BOOK[b]}（${b === 'H' ? '16:9' : '3:4'}）】`);
      SETS.filter(s => s.book === b).forEach(s => {
        const x = V4.sets[s.id];
        if (x.c === 'ok') ok++; else if (x.c === 'edit') ed++;
        L.push(`${s.id}｜${s.name}｜${s.theme}｜${s.cam.line}：${x.c ? CH[x.c] : '未回覆'}`);
        if (x.note.trim()) L.push(`   備註：${oneLine(x.note)}`);
      });
    });
    L.push('', `（已回覆 ${ok + ed}／24 套：接受 ${ok}、想修改 ${ed}、未回覆 ${24 - ok - ed}）`, '');
    Object.entries(QS).forEach(([k, Q]) => {
      const x = V4.q[k];
      L.push(`【${Q.label}】${x.c ? Q.opts[x.c] : '未回覆'}${x.note.trim() ? `；備註：${oneLine(x.note)}` : ''}`);
    });
    L.push(`【整體備註】${V4.gnote.trim() ? oneLine(V4.gnote) : '（無）'}`);
    const o3 = SETS.map(s => [s, oldV3(s.id)]).filter(([, t]) => t);
    const oq3 = oldV3Qs(), og3 = oldV3G();
    if (o3.length || oq3.length || og3) {
      L.push('', '【舊版回饋（v3，僅供參考，不算 v4）】');
      o3.forEach(([s, t]) => L.push(`${s.id}：${t}`));
      oq3.forEach(t => L.push(`v3 題目　${t}`));
      if (og3) L.push(`整體備註（v3）：${og3}`);
    }
    const olds = PEOPLE.map(p => [p, oldLine(p.pid)]).filter(([, t]) => t);
    const oq = oldQs(), og = oldGnotes();
    if (olds.length || oq.length || og.length) {
      L.push('', '【舊版回饋（v1／v2，僅供參考，不算 v4）】');
      olds.forEach(([p, t]) => L.push(`${MP[p.pid].name}：${t}`));
      oq.forEach(t => L.push(`舊版題目　${t}`));
      og.forEach(x => L.push(`整體備註（${VER(x.v)}）：${oneLine(x.note)}`));
    }
    return L.join('\n');
  }
  function refreshOut() {
    const n = SETS.filter(s => V4.sets[s.id].c).length;
    $('#bar-count').textContent = `已回覆 ${n}／24 套｜尚未生成任何照片`;
    const ta = $('#out-text');
    if (ta) ta.value = buildText();
  }

  // ---------- 事件 ----------
  app.addEventListener('change', e => {
    const t = e.target;
    if (t.dataset.s) { V4.sets[t.dataset.s].c = t.value; save(); refresh(t.dataset.s); refreshOut(); }
    else if (t.dataset.q) { V4.q[t.dataset.q].c = t.value; save(); refreshOut(); }
  });
  app.addEventListener('input', e => {
    const t = e.target;
    if (t.dataset.n) { V4.sets[t.dataset.n].note = t.value; save(); refreshOut(); }
    else if (t.dataset.qn) { V4.q[t.dataset.qn].note = t.value; save(); refreshOut(); }
    else if (t.id === 'gnote') { V4.gnote = t.value; save(); refreshOut(); }
  });
  app.addEventListener('click', e => {
    const z = e.target.closest('.zoom');
    if (z) { openViewer(z); return; }
    const cl = e.target.closest('[data-clear]');
    if (cl) {
      const id = cl.dataset.clear;
      V4.sets[id] = { c: '', note: '' };
      save();
      $$(`input[name="s-${id}"]`).forEach(r => { r.checked = false; });
      $(`#n-${id}`).value = '';
      refresh(id); refreshOut();
      toast(`已清除 ${id} 的回饋。`);
      return;
    }
    if (e.target.id === 'act-copy') copyOut();
    if (e.target.id === 'act-reset') {
      if (!window.confirm('清除本頁 v4 的全部回饋？（v1／v2／v3 舊回饋與第二階段素材選擇都不受影響）')) return;
      delete RAW.v4;
      V4 = loadV4();
      try { localStorage.setItem(KEY, JSON.stringify(RAW)); } catch (e2) { /* 只清記憶體 */ }
      render();
      toast('已清除 v4 回饋；舊版回饋保留。');
    }
  });
  $('#bar-copy').addEventListener('click', copyOut);

  async function copyOut() {
    const text = buildText();
    const ta = $('#out-text');
    ta.value = text;
    const done = '已複製回饋。請貼回 ChatGPT；本頁不會通知主管。';
    try { await navigator.clipboard.writeText(text); toast(done); } catch (e) {
      ta.focus(); ta.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch (_) { ok = false; }
      toast(ok ? done : '瀏覽器不允許自動複製：文字已選取，請手動複製。');
    }
  }

  // ---------- 放大檢視 ----------
  const viewer = $('#viewer'), vimg = $('#viewer-img'), vcap = $('#viewer-cap'), vmode = $('#viewer-mode');
  let lastBtn = null, pushed = false;
  function viewerNote(iid, m) {
    const px = m.orig_px ? `原圖 ${m.orig_px[0]}×${m.orig_px[1]} px｜` : '';
    const pv = m.res === 'hires' ? `預覽 ${m.w}×${m.h} px（等比縮小）` : '低解析';
    if (iid.startsWith('aal_')) return `${px}${pv}｜Aaliya 的既有照片，只參考拍法；她的臉不能當其他人設的參考`;
    if (iid.startsWith('m_')) return `${px}${pv}｜既有照片，不是新成品`;
    return '辨識用正臉（既有照片），只用來認人';
  }
  function openViewer(btn) {
    const iid = btn.dataset.img;
    const m = IMG[iid];
    if (!m) return;
    lastBtn = btn;
    vimg.src = m.z; vimg.width = m.w; vimg.height = m.h; vimg.alt = btn.dataset.cap;
    vcap.textContent = `${btn.dataset.cap}｜${viewerNote(iid, m)}`;
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
    viewer.classList.toggle('natural', nat);
    vmode.textContent = nat ? '符合畫面' : '原尺寸';
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
