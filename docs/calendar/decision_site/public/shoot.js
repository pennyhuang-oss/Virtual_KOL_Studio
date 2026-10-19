// 2027 KOL 桌曆｜M-3 寫真拍攝企劃（R4：8 套已接受＋16 套修訂＋印刷構圖核對）。企劃內容來自 data.js 的 m3（產生自 data/cal_m3_shoot_plan.json）；本頁沒有任何生成圖。
// Penny 的回饋只存在本機瀏覽器 localStorage（cal2027-shoot-v1:<SHA>），不送到伺服器；沒有追蹤或分析。
// v5 的回饋另存在同一筆資料的 v5 欄位；v1／v2／v3／v4 留下的欄位原樣保留，只顯示成「舊版」、不算 v5。載入時不改寫，只有 Penny 動手後才存。
// R4 owner 紀錄的 8 套已接受與兩本月份直接顯示為已確認，不再要求回覆；只有 16 套修訂與印刷示意需要回饋。
// 已接受套數的技術備註（中文妝感沒寫進英文 prompt）只顯示、不改內容，待主管確認。
// 構圖示意與印刷示意都只是方框與尺寸（依企劃數字畫），不是照片，也不是生成圖。
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
  const REV = SETS.filter(s => s.status === 'revised');
  const ACC = SETS.filter(s => s.status === 'accepted');
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
  // v3（R2）與 v4（R3）回饋：每套一筆，題目與整體備註各一筆；只讀
  const CH = { ok: '接受', edit: '想修改' };
  const Q34 = {   // v3／v4 頁面上的題目（R4 不再問，只用來讀出舊答案）
    months_h: { label: '橫式款月份推薦', opts: { ok: '接受', edit: '想調整（寫在備註）' } },
    months_v: { label: '直式款月份推薦', opts: { ok: '接受', edit: '想調整（寫在備註）' } },
    layout: { label: '版面與構圖建議', opts: { ok: '接受', edit: '想修改（寫在備註）' } },
    iris_first: { label: 'Iris 首張試拍候選', opts: { v: '同意先試 V-iris-chen（不是費用核准）', h: '想先試 H-iris-chen', edit: '想修改（寫在備註）' } },
    assign: { label: '已接受方向的 H／V 分配', opts: { ok: '接受', edit: '想對調（寫在備註）' } },
  };
  const OLDV = ['v4', 'v3'];
  const oldRaw = ver => (RAW[ver] && typeof RAW[ver] === 'object' ? RAW[ver] : {});
  function oldSet(ver, id) {
    const x = (oldRaw(ver).sets || {})[id];
    if (!x || typeof x !== 'object') return '';
    const a = [];
    if (CH[x.c]) a.push(`${ver}「${CH[x.c]}」`);
    if (str(x.note).trim()) a.push(`備註（${ver}）：${oneLine(x.note)}`);
    return a.join('；');
  }
  function oldQ(ver) {
    return Object.entries(oldRaw(ver).q || {}).filter(([k, x]) => x && typeof x === 'object' && Q34[k] && (Q34[k].opts[x.c] || str(x.note).trim()))
      .map(([k, x]) => `${Q34[k].label}：${ver}「${Q34[k].opts[x.c] || '未回覆'}」${str(x.note).trim() ? `，備註：${oneLine(x.note)}` : ''}`);
  }
  const oldG = ver => (str(oldRaw(ver).gnote).trim() ? oneLine(oldRaw(ver).gnote) : '');
  const oldSetAll = id => OLDV.map(v => oldSet(v, id)).filter(Boolean).join('；');

  // ---------- v5 回饋：只有 16 套修訂與印刷示意；已接受 8 套與月份已確認，不再問 ----------
  const QS = { frames: { label: '印刷構圖示意與暫定照片框', opts: { ok: '接受', edit: '想修改（寫在備註）' } } };
  function loadV5() {
    const v = RAW.v5 && typeof RAW.v5 === 'object' ? RAW.v5 : {};
    const out = { ver: CUR, sets: {}, q: {}, gnote: str(v.gnote) };
    REV.forEach(s => { const x = (v.sets || {})[s.id] || {}; out.sets[s.id] = { c: CH[x.c] ? x.c : '', note: str(x.note) }; });
    Object.keys(QS).forEach(k => { const x = (v.q || {})[k] || {}; out.q[k] = { c: QS[k].opts[x.c] ? x.c : '', note: str(x.note) }; });
    return out;
  }
  let V5 = loadV5();
  function save() {
    RAW.v5 = V5;
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
  // 手機上每列變成一張小卡（表頭隱藏、欄名在格內）
  const stbl = (head, rows, cls) => `<div class="tbl"><table class="photo ${cls || ''}"><thead><tr>${head.map(h => `<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>` +
    rows.map(r => `<tr>${r.map((c, i) => `<td data-label="${esc(head[i])}">${c && c.html ? c.html : esc(c)}</td>`).join('')}</tr>`).join('') + '</tbody></table></div>';
  const link = id => ({ html: `<a href="#c-${esc(id)}">${esc(id)}</a>` });
  const outfitList = o => `<ul class="facts">${Object.entries(o).map(([k, v]) => `<li><b>${esc(k)}</b>：${esc(v)}</li>`).join('')}</ul>`;
  const stTag = s => (s.status === 'accepted' ? '<span class="tag acc">已接受</span>' : '<span class="tag rev">R4 修訂</span>');

  function decSec() {
    const O4 = P.owner_r4, Sm = O4.summary, O3 = P.owner_r3, O2 = P.owner_r2;
    const hasOld = PEOPLE.some(p => oldLine(p.pid)) || oldQs().length || oldGnotes().length || SETS.some(s => oldSetAll(s.id)) || OLDV.some(v => oldQ(v).length || oldG(v));
    return `<section class="sec" id="dec"><h2>R4 owner 決策與目前狀態</h2>
<pre class="verb">${esc(O4.verbatim.decisions)}</pre>
<p class="note">${esc(O4.note)}</p>
<div class="statgrid">
<div class="stat acc"><b>已接受 ${ACC.length} 套</b><span>不需再回覆，不因整體偏好重設</span><p>${ACC.map(s => `<a href="#c-${esc(s.id)}">${esc(s.id)}</a>`).join('、')}</p></div>
<div class="stat rev"><b>修訂 ${REV.length} 套</b><span>新主推薦，請選「接受」或「想修改」</span><p>${REV.map(s => `<a href="#c-${esc(s.id)}">${esc(s.id)}</a>`).join('、')}</p></div>
<div class="stat conf"><b>兩本月份已確認</b><span>${esc(Sm.months)}</span></div>
<div class="stat warn"><b>V-iris-chen 首試</b><span>${esc(Sm.iris_first)}</span></div>
</div>
<p class="callout warn">${esc(Sm.jia_note)} 16 套的新主推薦與暫定照片框都<b>還沒有經 Penny 批准</b>；生成與費用都未授權。</p>
<div class="callout"><b>已接受套數的技術備註（${esc(P.accepted_notes.status)}）</b>：${esc(P.accepted_notes.summary)}${ul(P.accepted_notes.items.map(x => `${x.id}：中文「${x.makeup_zh}」→ 建議補一句「${x.proposal_en}」`))}</div>
<details class="info"><summary>R4 逐套修改要求（逐字，主管轉述）</summary>${REV.map(s => `<pre class="verb">${esc(s.r4.owner)}</pre>`).join('')}<pre class="verb">${esc(O4.verbatim.closing)}</pre></details>
<details class="info"><summary>R3 攝影設計要求（逐字，仍適用）</summary><pre class="verb">${esc(O3.verbatim.requirement)}</pre><pre class="verb">${esc(O3.verbatim.keep_existing)}</pre></details>
<details class="info"><summary>R2 已生效的決定（逐字）</summary><pre class="verb">${esc(O2.verbatim.decisions)}</pre>${ul(O2.summary.decided)}</details>
<div class="callout${hasOld ? ' warn' : ''}">${hasOld ? '這個瀏覽器裡有舊版（v1／v2／v3／v4）的回饋：都還在，各套與各位的區塊會列出來，<b>不算</b>這一版（v5）的回覆，也不會變成新的核准。' : '這個瀏覽器沒有舊版回饋紀錄。'}</div>
</section>`;
  }

  function bookTable(b) {
    const rows = SETS.filter(s => s.book === b).sort((x, y) => x.month - y.month);
    return tbl(['月', 'ID', '狀態', '人設', '主題', '環境', '服裝', '色彩', '姿態', '表情', '性感', '攝影方法', '景別｜身體方向｜臉與視線｜拍攝角度'],
      rows.map(s => [`${s.month} 月`, link(s.id), s.status === 'accepted' ? '已接受' : 'R4 修訂', s.name, s.theme, s.env, Object.values(s.outfit).join('、'), s.palette, s.pose, s.expr, s.sexy, s.method, s.cam.line]), 'book');
  }
  function booksSec() {
    return `<section class="sec" id="books"><h2>兩本月份（已確認）與總覽</h2>
<p class="callout"><b>兩本月份人選排序已確認（R4）。</b>不再請 Penny 重新核准；服裝與場景配合既定月份。</p>
<div class="mgrid2">${P.months.map(m => `<div class="mrow2"><span class="mn2">${m.m} 月</span>` +
      `<a class="mchip h" href="#c-${esc(m.H)}"><b>橫</b> ${esc(SET[m.H].name)}<small>${esc(m.why_h)}</small></a>` +
      `<a class="mchip v" href="#c-${esc(m.V)}"><b>直</b> ${esc(SET[m.V].name)}<small>${esc(m.why_v)}</small></a></div>`).join('')}</div>
${ul(P.month_rules)}
<details class="info"><summary>橫式款 12 套總覽（依月份）</summary>${bookTable('H')}</details>
<details class="info"><summary>直式款 12 套總覽（依月份）</summary>${bookTable('V')}</details>
</section>`;
  }

  // ---------- 攝影總覽（兩本各 12 張） ----------
  const PH_HEAD = ['月', '人物', '狀態', '景別', '身體方向', '臉部方向', '視線', '相機角度', '人物位置', '主要展示重點'];
  function photoTable(b) {
    const rows = SETS.filter(s => s.book === b).sort((x, y) => x.month - y.month);
    return stbl(PH_HEAD, rows.map(s => [`${s.month} 月`, { html: `<a href="#c-${esc(s.id)}">${esc(s.name)}</a> <code>${esc(s.id)}</code>` },
      { html: stTag(s) }, s.cam.shot.zh, s.cam.body.short, s.cam.face.zh, s.cam.gaze.zh, s.cam.angle.short, s.cam.pos, s.cam.focus]));
  }
  const ORD = ['胸上', '腰上', '大腿中段以上', '膝上', '全身', '坐姿全身', '席地坐姿全身', '斜躺全身', '坐姿到水面', '正面', '約30度斜側', '約45度斜側', '側面', '側面斜躺'];
  const cnt = o => Object.entries(o).sort((a, b) => ORD.indexOf(a[0]) - ORD.indexOf(b[0])).map(([k, v]) => `${k} ${v}`).join('、');
  function photoSec() {
    const F = P.photo;
    return `<section class="sec" id="photo"><h2>攝影總覽：景別、角度與構圖</h2>
<p class="note">${esc(F.summary)}</p>
${['H', 'V'].map(b => `<h3>${BOOK[b]}（${b === 'H' ? '16:9' : '3:4'}）攝影總覽</h3>${photoTable(b)}
<p class="note"><b>景別：</b>${esc(cnt(F.counts[b].shot))}；<b>身體方向：</b>${esc(cnt(F.counts[b].body))}。</p>
<p class="note"><b>節奏：</b>${esc(F.rhythm[b])}</p><p class="note"><b>依月份：</b>${esc(F.sequence[b])}</p>`).join('')}
${ul([`近景：${F.rhythm.near}`, `角度與視線：${F.rhythm.angles}`, `同一位的兩款：${F.rhythm.pair}`, `戶外與重複：${F.rhythm.outdoor}`])}
<h3>R4 修訂的 ${REV.length} 套：改了什麼</h3>
${stbl(['ID', '原設計（v4）', '新設計', '改了什麼'], REV.map(s => { const a = P.adjust.find(x => x.id === s.id); return [link(s.id), a.from, a.line, s.r4.change]; }), 'adj')}
<details class="info"><summary>共同規則與 prompt 一致性檢查</summary><h4>共同規則</h4>${ul(F.rules)}<h4>逐套檢查（產生資料時執行，不通過就無法建置）</h4>${ul(F.checks)}</details>
</section>`;
  }

  // ---------- 印刷構圖 ----------
  function printSec() {
    const R = P.printing, I = R.iris_first;
    const dg = b => `<figure class="pdiag"><button type="button" class="zoom svgz" data-svg="${esc(R.diagrams[b])}" data-cap="${esc(`${BOOK[b]}版型與裁切示意（不含照片）`)}" aria-label="放大：${esc(BOOK[b])}版型與裁切示意">` +
      `<img src="${esc(R.diagrams[b])}" alt="${esc(`${BOOK[b]}版型與裁切示意：成品、出血、安全框、假設線圈區、暫定照片框與照片比例`)}" loading="lazy" decoding="async"><span class="zi" aria-hidden="true">放大</span></button>` +
      `<figcaption>${esc(BOOK[b])}：${esc(R.frames[b].name)} ${R.frames[b].mm[0]}×${R.frames[b].mm[1]} mm｜${esc(R.fit[b].img)} 放入：${esc(R.fit[b].crop)}｜<a href="${esc(R.diagrams[b])}" target="_blank" rel="noopener">開新分頁看原圖</a></figcaption></figure>`;
    return `<section class="sec" id="print"><h2>印刷構圖核對：裁切、出血與裝訂安全</h2>
<p class="callout warn">${esc(R.note)}</p>
<div class="pdiags">${dg('H')}${dg('V')}</div>
<h3>已知（廠商編輯器設定與商品頁）</h3>${stbl(['項目', '橫式', '直式', '來源'], R.known.map(x => [x.k, x.H, x.V, x.src]))}
<h3>假設（本案規劃用，不是廠商規格）</h3>${stbl(['項目', '橫式', '直式', '為什麼'], R.assumed.map(x => [x.k, x.H, x.V, x.why]))}
<h3>未知</h3>${ul(R.unknown)}
<h3>如果改用其他照片框</h3>${ul(R.compare.map(x => `${x.k}：${x.v}`))}
<h3>原則</h3>${ul(R.rules)}
<h3>V-iris-chen 首試是否需要構圖微調</h3>${ul([I.answer, I.condition, I.verify])}
<h3>8 套已接受是否受影響</h3><p class="note">${esc(R.accepted_impact.summary)}</p>
<details class="info" open><summary>24 套逐張印刷構圖判斷（依暫定照片框）</summary>
${stbl(['ID', '狀態', '照片框', '比例裁切', '邊緣的重要部位', '不能切', '需要的餘量', '判斷', '原生尺寸', '有效 ppi'],
      SETS.map(s => [link(s.id), { html: stTag(s) }, s.print.frame, s.print.crop, s.print.edges.join('；'), s.print.keep, s.print.need, s.print.verdict, s.print.native, s.print.ppi]), 'ptab')}</details>
</section>`;
  }

  function frameTable(fr) {
    const crop = ['chest', 'waist', 'thigh', 'knee'].includes(fr.shot);
    return tbl(['項目', '內容'], [['景別', fr.shot_zh], [crop ? '頭頂上方留白' : '人物佔比', crop ? `約 ${fr.headroom}%` : `約佔${fr.fill_of} ${fr.fill}%`],
      ['焦段／距離（參考）', `${fr.f}mm／約 ${fr.d} 公尺`], ['視野（寬×高）', `${fr.view_w}×${fr.view_h} 公尺`],
      ['相機與畫面中心', `相機約 ${fr.cam_m} 公尺高、畫面中心約 ${fr.centre_m} 公尺高，換算俯仰約 ${fr.tilt_deg > 0 ? '+' : ''}${fr.tilt_deg} 度`],
      ['原生尺寸', fr.native]]);
  }
  // 構圖示意：只畫畫框、頭與身體範圍（依企劃數字），不是照片
  function schem(s) {
    const k = s.frame.sch;
    return `<figure class="schw"><div class="nb2 sch r${s.book}" role="img" aria-label="${esc(`${s.id} 構圖示意：${s.cam.line}`)}">` +
      `<span class="sch-fig" data-x="${k.x}" data-w="${k.w}" data-top="${k.top}" data-bot="${k.bot}" data-head="${k.head}"${k.lie ? ' data-lie="1"' : ''}><i class="sch-h"></i><i class="sch-b"></i></span></div>` +
      `<figcaption class="sch-t"><b>${BOOK[s.book]}新照片 ${esc(s.ratio)}：尚未生成</b>框內只是構圖示意（人物範圍與頭的位置），不是照片</figcaption>` +
      `<p class="prline"><a href="#print">印刷</a>：${esc(s.print.frame)}｜${esc(s.print.crop)}｜${esc(s.print.verdict)}</p></figure>`;
  }
  function camRow(s) {
    const c = s.cam;
    return `<dl class="camrow" aria-label="攝影設計">` +
      `<div><dt>景別</dt><dd>${esc(c.shot.zh)}</dd></div><div><dt>身體方向</dt><dd>${esc(c.body.short)}</dd></div>` +
      `<div><dt>臉與視線</dt><dd>${esc(c.face.zh)}・${esc(c.gaze.short)}</dd></div><div><dt>拍攝角度</dt><dd>${esc(c.angle.short)}</dd></div></dl>`;
  }
  function camDetail(s) {
    const c = s.cam;
    return `<details class="info camd"><summary>攝影設計細節：七個欄位與理由</summary>
<dl class="pdl small">
<dt>1. 景別</dt><dd>${esc(c.shot.zh)}</dd>
<dt>2. 畫面上下界</dt><dd>${esc(c.bounds.zh)}</dd>
<dt>3. 身體朝向</dt><dd>${esc(c.body.short)}：${esc(c.body.zh)}</dd>
<dt>4. 臉部朝向與視線</dt><dd>${esc(c.face.zh)}，${esc(c.gaze.zh)}</dd>
<dt>5. 相機高度與俯仰</dt><dd>${esc(c.angle.zh)}<br><small>${esc(c.angle.ref)}（焦段與距離只是參考，不是生成保證）</small></dd>
<dt>6. 畫面配置</dt><dd>${esc(c.comp.zh)}</dd>
<dt>7. 攝影目的</dt><dd>${esc(c.purpose.zh)}</dd>
<dt>選擇理由</dt><dd>${esc(c.why)}</dd>
<dt>印刷（暫定照片框）</dt><dd>${esc(s.print.edges.join('；'))}；不能切：${esc(s.print.keep)}；${esc(s.print.need)}；${esc(s.print.ppi)}</dd>
</dl></details>`;
  }
  function r4Box(s) {
    if (s.status === 'accepted') {
      const n = P.accepted_notes.items.find(x => x.id === s.id);
      return `<div class="r4box acc"><p><b>已接受（R4 owner 紀錄）</b>：服裝、場景、表情與攝影照上一版，不需再回覆。</p>` +
        (n ? `<p class="tnote"><b>技術備註（${esc(P.accepted_notes.status)}）</b>：中文妝感「${esc(n.makeup_zh)}」沒有寫進英文 prompt；建議生成前補一句，不改其他內容。</p>` : '') + '</div>';
    }
    return `<div class="r4box rev"><p><b>R4 改了什麼：</b>${esc(s.r4.change)}</p>
<details class="info"><summary>Penny 的修改要求（逐字，主管轉述）</summary><pre class="verb">${esc(s.r4.owner)}</pre></details></div>`;
  }
  function card(s) {
    const acc = s.status === 'accepted';
    const x = acc ? null : V5.sets[s.id];
    const old = oldSetAll(s.id);
    return `<article class="scard ${s.book === 'H' ? 'bh' : 'bv'}${acc ? ' isacc' : ''}" id="c-${esc(s.id)}" data-set="${esc(s.id)}" data-status="${esc(s.status)}">
<p class="sc-head"><code class="sid">${esc(s.id)}</code> <span class="tag book">${BOOK[s.book]}（${esc(s.ratio)}）</span> ${stTag(s)} <span class="tag mon">${s.month} 月（已確認）</span> <span class="st none" data-st="${esc(s.id)}"></span></p>
<p class="sc-theme">${esc(s.theme)}</p>
${r4Box(s)}
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
<dt>來源</dt><dd>${esc(ORIGIN[s.origin])}</dd>
</dl>
${frameTable(s.frame)}
${tbl(['風險', '處理'], s.risks)}
</details>
<details class="info"><summary>prompt 草稿（尚未執行）</summary><pre class="prompt">${esc(s.prompt)}</pre></details>
${old ? `<p class="oldfb">舊版回饋（保留，不算 v5）：${esc(old)}</p>` : ''}
${acc ? '' : `<fieldset class="fb"><legend>回饋：${esc(s.id)}（R4 修訂）</legend>
<div class="fb-opts">${Object.entries(CH).map(([k, v]) => `<label class="fb-o"><input type="radio" name="s-${esc(s.id)}" value="${k}" data-s="${esc(s.id)}"${x.c === k ? ' checked' : ''}> ${esc(v)}</label>`).join('')}</div>
<label class="lbl" for="n-${esc(s.id)}">備註</label>
<textarea id="n-${esc(s.id)}" data-n="${esc(s.id)}" rows="2" maxlength="2000" placeholder="例：想改成全身；想看側面；衣服想換顏色">${esc(x.note)}</textarea>
<button type="button" class="btn ghost small" data-clear="${esc(s.id)}">清除這套的回饋</button>
</fieldset>`}</article>`;
  }
  function person(p, i) {
    const old = oldLine(p.pid);
    return `<section class="sec person3" id="p-${esc(p.pid)}">
<div class="ph"><div class="ph-face">${fig(MP[p.pid].face, `${MP[p.pid].name}｜辨識用正臉（既有照片）`)}</div>
<div class="ph-t"><h2>${i + 1}. ${esc(MP[p.pid].name)}${MP[p.pid].native ? ` <span class="nat">${esc(MP[p.pid].native)}</span>` : ''}</h2>
<p class="cc-meta">身材設定：${esc(p.meas)}</p></div></div>
<details class="info fbq"><summary>R2 回饋與當時的落實（歷史紀錄；最新決定見各套卡片）</summary><pre class="verb">${esc(p.feedback)}${p.shared ? '\n' + esc(p.shared) : ''}</pre>${ul(p.applied)}</details>
${old ? `<p class="oldfb">舊版 v1／v2 回饋（保留，不算 v5）：${esc(old)}</p>` : ''}
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
    return `<section class="sec" id="cost"><h2>費用與 Iris 首張試拍（費用方案不變）</h2>
<p class="callout warn"><b>${esc(I.status_r4)}</b> ${esc(K.status)} ${esc(K.gate)}</p>
<h3>Iris 首張：<a href="#c-${esc(I.set)}">${esc(I.set)}</a>（方向已同意）</h3>${ul(I.why)}
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
    const oq = oldQs(), og = oldGnotes();
    return `<section class="sec" id="out"><h2>回饋與複製</h2>
<div class="callout">回饋只存在這個瀏覽器，<b>不會送到伺服器</b>，也不會通知主管。<b>未回覆不算接受。</b>複製後請貼回 ChatGPT。這是對企劃方向的回饋，不是生成授權或費用核准。已接受的 8 套與兩本月份已確認，不需要再回覆。</div>
<h3>想請 Penny 決定的事</h3><ol class="facts">${P.questions.map(x => `<li>${esc(x)}</li>`).join('')}</ol>
<p class="note">第 1 題在 16 張修訂卡片上選；第 2 題在下面選：</p>
${Object.entries(QS).map(([k, Q]) => `<fieldset class="fb"><legend>${esc(Q.label)}</legend><p class="note"><a href="#print">看印刷構圖示意</a></p><div class="fb-opts col">${Object.entries(Q.opts).map(([v, t]) =>
      `<label class="fb-o"><input type="radio" name="q-${k}" value="${v}" data-q="${k}"${V5.q[k].c === v ? ' checked' : ''}> ${esc(t)}</label>`).join('')}</div>
<label class="lbl" for="qn-${k}">備註</label><textarea id="qn-${k}" data-qn="${k}" rows="1" maxlength="1500">${esc(V5.q[k].note)}</textarea></fieldset>`).join('')}
${OLDV.map(v => { const q = oldQ(v); return q.length ? `<p class="oldfb">${v} 題目的回答（保留，不算 v5）：${esc(q.join('；'))}</p>` : ''; }).join('')}
${oq.length ? `<p class="oldfb">v1／v2 題目的回答（保留，不算 v5）：${esc(oq.join('；'))}</p>` : ''}
<label class="lbl" for="gnote">整體備註</label>
<textarea id="gnote" rows="3" maxlength="3000" placeholder="例：整體想要更多戶外；性感程度想再高一點">${esc(V5.gnote)}</textarea>
${OLDV.map(v => (oldG(v) ? `<p class="oldfb">${v} 整體備註（保留）：${esc(oldG(v))}</p>` : '')).join('')}
${og.length ? `<p class="oldfb">v1／v2 整體備註（保留）：${esc(og.map(x => `${VER(x.v)}「${oneLine(x.note)}」`).join('；'))}</p>` : ''}
<div class="actions"><button type="button" class="btn" id="act-copy">複製回饋</button><button type="button" class="btn danger" id="act-reset">清除 v5 回饋</button></div>
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
<li>完整企劃、攝影設計與印刷構圖：repo 的 <code>docs/calendar/CAL_18_M3_SHOOT_PLAN.md</code>（R4）；R2 Owner 決策逐字紀錄：<code>docs/calendar/CAL_19_M3_R2_OWNER_DECISION.md</code>。</li></ul></section>`;
  }

  function render() {
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    $('#planver').textContent = `${P.version}（${P.round}，${P.written_on}）`;
    app.innerHTML = decSec() + photoSec() + printSec() + booksSec() +
      `<section class="sec" id="people"><h2>12 位 × 橫式款／直式款</h2>
<ul class="facts"><li>每位兩套獨立企劃：服裝與場景都不同。左邊是橫式款（16:9），右邊是直式款（3:4）；手機上上下排列。</li>
<li>綠色「已接受」的 8 套照上一版、不需再回覆；橘色「R4 修訂」的 16 套先寫「改了什麼」，再請你選「接受」或「想修改」。</li>
<li>每張卡片最上面直接寫<b>景別｜身體方向｜臉與視線｜拍攝角度</b>；七個攝影欄位與理由在「攝影設計細節」展開；虛線框下方一行是這張的印刷判斷。</li>
<li>虛線框是「尚未生成」的新照片位置，裡面的方框與圓點只是<b>構圖示意</b>，不是照片。卡片下方的照片都是<b>既有照片</b>，只按標示的用途參考，不是新構圖的成品；身材一律以設定數字為準。</li></ul>
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
  const stOf = id => (SET[id].status === 'accepted' ? '已接受' : (V5.sets[id].c ? CH[V5.sets[id].c] : '未回覆'));
  function refresh(id) {
    const el = $(`[data-st="${id}"]`);
    if (el) {
      const acc = SET[id].status === 'accepted', c = acc ? '' : V5.sets[id].c;
      el.textContent = acc ? '不需回覆' : (c ? CH[c] : '未回覆');
      el.className = `st ${acc ? 'conf' : (c === 'ok' ? 'conf' : (c ? 'draft' : 'none'))}`;
    }
    const pid = SET[id].pid;
    const ov = $(`[data-ov="${pid}"]`);
    if (ov) ov.textContent = ['H', 'V'].map(b => `${b}：${stOf(b + '-' + pid)}`).join('｜');
  }
  function buildText() {
    const L = ['TASK-CAL-001／M-3／R4｜16 套寫真修訂與印刷構圖核對｜Penny 企劃回饋',
      `企劃版本：${P.version}（${P.round}）｜頁面版本：${PAGE_COMMIT || '本機預覽（未部署）'}`,
      '說明：這是對 16 套修訂與印刷示意的回饋，不是生成授權，也不是費用核准；未回覆不算接受。'];
    let ok = 0, ed = 0;
    ['H', 'V'].forEach(b => {
      L.push('', `【${BOOK[b]}（${b === 'H' ? '16:9' : '3:4'}）R4 修訂】`);
      REV.filter(s => s.book === b).sort((x, y) => x.month - y.month).forEach(s => {
        const x = V5.sets[s.id];
        if (x.c === 'ok') ok++; else if (x.c === 'edit') ed++;
        L.push(`${s.id}｜${s.month}月｜${s.name}｜${s.theme}｜${s.cam.line}：${x.c ? CH[x.c] : '未回覆'}`);
        if (x.note.trim()) L.push(`   備註：${oneLine(x.note)}`);
      });
    });
    L.push('', `（16 套修訂已回覆 ${ok + ed}／16：接受 ${ok}、想修改 ${ed}、未回覆 ${16 - ok - ed}）`);
    L.push('', '【已接受（R4 owner 紀錄，不需再回覆）】', ACC.map(s => s.id).join('、'));
    L.push('【兩本月份】已確認（R4 owner 紀錄）', '');
    Object.entries(QS).forEach(([k, Q]) => {
      const x = V5.q[k];
      L.push(`【${Q.label}】${x.c ? Q.opts[x.c] : '未回覆'}${x.note.trim() ? `；備註：${oneLine(x.note)}` : ''}`);
    });
    L.push(`【整體備註】${V5.gnote.trim() ? oneLine(V5.gnote) : '（無）'}`);
    OLDV.forEach(v => {
      const sets = SETS.map(s => [s, oldSet(v, s.id)]).filter(([, t]) => t), q = oldQ(v), g = oldG(v);
      if (!sets.length && !q.length && !g) return;
      L.push('', `【舊版回饋（${v}，僅供參考，不算 v5）】`);
      sets.forEach(([s, t]) => L.push(`${s.id}：${t}`));
      q.forEach(t => L.push(`${v} 題目　${t}`));
      if (g) L.push(`整體備註（${v}）：${g}`);
    });
    const olds = PEOPLE.map(p => [p, oldLine(p.pid)]).filter(([, t]) => t);
    const oq = oldQs(), og = oldGnotes();
    if (olds.length || oq.length || og.length) {
      L.push('', '【舊版回饋（v1／v2，僅供參考，不算 v5）】');
      olds.forEach(([p, t]) => L.push(`${MP[p.pid].name}：${t}`));
      oq.forEach(t => L.push(`舊版題目　${t}`));
      og.forEach(x => L.push(`整體備註（${VER(x.v)}）：${oneLine(x.note)}`));
    }
    return L.join('\n');
  }
  function refreshOut() {
    const n = REV.filter(s => V5.sets[s.id].c).length;
    $('#bar-count').textContent = `修訂已回覆 ${n}／16 套｜已接受 8 套｜尚未生成任何照片`;
    const ta = $('#out-text');
    if (ta) ta.value = buildText();
  }

  // ---------- 事件 ----------
  app.addEventListener('change', e => {
    const t = e.target;
    if (t.dataset.s) { V5.sets[t.dataset.s].c = t.value; save(); refresh(t.dataset.s); refreshOut(); }
    else if (t.dataset.q) { V5.q[t.dataset.q].c = t.value; save(); refreshOut(); }
  });
  app.addEventListener('input', e => {
    const t = e.target;
    if (t.dataset.n) { V5.sets[t.dataset.n].note = t.value; save(); refreshOut(); }
    else if (t.dataset.qn) { V5.q[t.dataset.qn].note = t.value; save(); refreshOut(); }
    else if (t.id === 'gnote') { V5.gnote = t.value; save(); refreshOut(); }
  });
  app.addEventListener('click', e => {
    const z = e.target.closest('.zoom');
    if (z) { openViewer(z); return; }
    const cl = e.target.closest('[data-clear]');
    if (cl) {
      const id = cl.dataset.clear;
      V5.sets[id] = { c: '', note: '' };
      save();
      $$(`input[name="s-${id}"]`).forEach(r => { r.checked = false; });
      $(`#n-${id}`).value = '';
      refresh(id); refreshOut();
      toast(`已清除 ${id} 的回饋。`);
      return;
    }
    if (e.target.id === 'act-copy') copyOut();
    if (e.target.id === 'act-reset') {
      if (!window.confirm('清除本頁 v5 的全部回饋？（v1–v4 舊回饋與第二階段素材選擇都不受影響）')) return;
      delete RAW.v5;
      V5 = loadV5();
      try { localStorage.setItem(KEY, JSON.stringify(RAW)); } catch (e2) { /* 只清記憶體 */ }
      render();
      toast('已清除 v5 回饋；舊版回饋保留。');
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

  // ---------- 放大檢視（既有照片與印刷示意） ----------
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
    if (btn.dataset.svg) {
      vimg.removeAttribute('width'); vimg.removeAttribute('height');
      vimg.src = btn.dataset.svg; vimg.alt = btn.dataset.cap;
      vcap.textContent = `${btn.dataset.cap}｜只有方框與尺寸，不是照片，也不是印刷安全證明`;
    } else {
      const iid = btn.dataset.img;
      const m = IMG[iid];
      if (!m) return;
      vimg.src = m.z; vimg.width = m.w; vimg.height = m.h; vimg.alt = btn.dataset.cap;
      vcap.textContent = `${btn.dataset.cap}｜${viewerNote(iid, m)}`;
    }
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
