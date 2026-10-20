// 2027 KOL 桌曆｜M-3 寫真拍攝企劃（M-4 R1：M-3 完成——23 套已接受＋H-Luna 依 owner 指示修訂、主管覆核通過；V-Iris 首試準備與首試前核查）。企劃內容來自 data.js 的 m3（產生自 data/cal_m3_shoot_plan.json）；本頁沒有任何生成圖。
// 舊版回饋（v1–v6）只存在本機瀏覽器 localStorage（cal2027-shoot-v1:<SHA>），不送到伺服器；沒有追蹤或分析。
// R7 起沒有必填決策：本頁只讀那筆資料、把 v1–v6 列為歷史，不寫入、不清除（沒有任何會呼叫 localStorage.setItem／removeItem 的程式）。
// M-4 R1：23 套已接受、H-luna-tanaka「依owner指示修訂，主管覆核通過」（Penny 沒有看過修訂後版本），M-3 完成；不請 Penny 回覆。
// M-4 R2：V-Iris 依授權生成 1 張首試，本頁只顯示結果文字（驗收、扣款、歸屬層級），照片與工作 ID 不放本頁。
// 構圖示意與印刷示意都只是方框與尺寸（依企劃數字畫），不是照片，也不是生成圖。
// 第二階段素材選擇（cal2027-materials-v1:<SHA>）本頁不讀、不寫、不刪。
// M-4 R3：本頁改為「已定稿企劃／歷史紀錄」（history.html，只讀）；目前檢視（首試照片、待決事項、回饋）在 shoot.html。
// 公開資料不含交易原始資料（建置器只留實扣摘要）；照片只放在目前檢視頁。
'use strict';
(() => {
  const D = window.CAL_DATA;
  const app = document.getElementById('app');
  if (!D || !D.m3 || !D.mat || !D.m3.sets) { app.textContent = '資料載入失敗。'; return; }

  const SHA = D.fixed_sha;
  const KEY = 'cal2027-shoot-v1:' + SHA;
  const IMG = D.images;
  const P = D.m3;
  const MP = {};
  const ITEM = {};
  D.mat.people.forEach(p => { MP[p.pid] = p; p.items.forEach(it => { ITEM[it.id] = { ...it, pid: p.pid }; }); });
  const SETS = P.sets;
  const SET = {};
  SETS.forEach(s => { SET[s.id] = s; });
  const VSETS = SETS.filter(s => s.status === 'supervisor_verified');
  const ACC = SETS.filter(s => s.status === 'accepted');
  const PEOPLE = P.people;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const oneLine = s => String(s).trim().replace(/\s*\n\s*/g, '／');
  const str = x => (typeof x === 'string' ? x : '');
  const BOOK = { H: '橫式款', V: '直式款' };
  const R3NOTE = '主管 M-4 R3：反光板及支架必修；人物與身材待 Penny 看圖回饋。';
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
  try { const s = JSON.parse(localStorage.getItem(KEY)); if (s && typeof s === 'object') RAW = s; } catch (e) { /* 讀不到就當作沒有舊回饋；本頁不寫入 */ }
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
  const Q34 = {   // v3／v4／v5 頁面上的題目（現在不再問，只用來讀出舊答案）
    months_h: { label: '橫式款月份推薦', opts: { ok: '接受', edit: '想調整（寫在備註）' } },
    months_v: { label: '直式款月份推薦', opts: { ok: '接受', edit: '想調整（寫在備註）' } },
    layout: { label: '版面與構圖建議', opts: { ok: '接受', edit: '想修改（寫在備註）' } },
    iris_first: { label: 'Iris 首張試拍候選', opts: { v: '同意先試 V-iris-chen（不是費用核准）', h: '想先試 H-iris-chen', edit: '想修改（寫在備註）' } },
    assign: { label: '已接受方向的 H／V 分配', opts: { ok: '接受', edit: '想對調（寫在備註）' } },
    frames: { label: '印刷構圖示意與暫定照片框', opts: { ok: '接受', edit: '想修改（寫在備註）' } },
  };
  const OLDV = ['v6', 'v5', 'v4', 'v3'];
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

  // ---------- R7 起沒有必填決策，也沒有新的回饋欄位；v6 的兩套回覆與 v1–v5 一樣只讀、列為歷史 ----------
  const VER_LABEL = VSETS.length ? VSETS[0].m4r1.label : '';

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
  const stTag = s => (s.status === 'accepted' ? '<span class="tag acc">已接受</span>' : '<span class="tag acc ver">依owner指示修訂・主管覆核通過</span>');
  const stText = s => (s.status === 'accepted' ? '已接受' : VER_LABEL);

  function decSec() {
    const O7 = P.owner_r7, S7 = O7.summary, O6 = P.owner_r6, O4 = P.owner_r4, O3 = P.owner_r3, O2 = P.owner_r2, SU = P.sup_m4r1, R2 = P.m4_prep.r2;
    const hasOld = PEOPLE.some(p => oldLine(p.pid)) || oldQs().length || oldGnotes().length || SETS.some(s => oldSetAll(s.id)) || OLDV.some(v => oldQ(v).length || oldG(v));
    const ids = a => a.map(s => `<a href="#c-${esc(s.id)}">${esc(s.id)}</a>`).join('、');
    return `<section class="sec" id="dec"><h2>M-3 完成（主管結論）與 V-Iris 首試前核查</h2>
<pre class="verb">${esc(SU.verbatim.conclusion)}</pre>
<p class="note">${esc(SU.source)}${esc(SU.note)}</p>
<div class="statgrid">
<div class="stat acc"><b>已接受 ${ACC.length} 套</b><span>owner 接受，拍攝內容與 prompt 不變（R4 的 8 套＋R6 的 14 套＋R7 的 H-jia-seo）</span><p>${ids(ACC)}</p></div>
<div class="stat acc"><b>${esc(VER_LABEL)} ${VSETS.length} 套</b><span>只改雙手與香袋；Penny 指定了這個修改，但沒有看過修訂後的版本</span><p>${ids(VSETS)}</p></div>
<div class="stat conf"><b>M-3 完成，沒有待決事項</b><span>不再要求 owner 填企劃問卷；月份與工作照片框維持（${esc(S7.frames)}）。</span></div>
<div class="stat warn"><b>V-iris-chen 單張首試（M-4 R2）</b><span>R2 當時：${esc(R2.status)}實扣 ${R2.charge.net}（${esc(R2.attribution.level)}）。${esc(R3NOTE)}<a href="shoot.html">看首試照片（目前檢視頁）</a>｜<a href="#prep">首試紀錄</a></span></div>
</div>
<p class="callout warn"><b>只授權了 V-Iris 首試 1 張</b>（Penny 同意：預算最多 1 credit、精確報價 ≤0.12、只送一次），已送出一次並停止；沒有 24 套生成、訓練或重試授權。首試結果不是印刷驗收。</p>
<details class="info"><summary>M-4 R2 授權與主管對 R1 的覆核（逐字）</summary><pre class="verb">${esc(P.auth_m4r2.verbatim.authorization)}</pre><pre class="verb">${esc(P.auth_m4r2.verbatim.r1_review)}</pre><p class="note">${esc(P.auth_m4r2.note)}</p></details>
<details class="info"><summary>M-4 R2 改了哪些文字（舊 → 新）</summary>${ul(P.m4r2.changes.map(x => `［${x.kind}］${x.where}：${x.old} → ${x.new}`))}</details>
<details class="info"><summary>主管本輪指示（逐字）</summary><pre class="verb">${esc(SU.verbatim.instructions)}</pre></details>
<details class="info"><summary>M-4 R1 改了哪些文字（舊 → 新）</summary>${ul(P.m4r1.changes.map(x => `［${x.kind}］${x.where}：${x.old} → ${x.new}`))}</details>
<details class="info"><summary>R7 owner 決策（歷史，逐字）</summary><pre class="verb">${esc(O7.verbatim.decisions)}</pre><p class="note">${esc(O7.source)}${esc(O7.note)}</p></details>
<details class="info"><summary>R7：Penny 原文與主管補充細節（逐字；只有引號內是 Penny 原話）</summary>${VSETS.map(s => `<p class="note"><b>${esc(s.id)}（${s.month} 月）Penny：</b>「${esc(s.r7.owner)}」</p><p class="note">主管補充的落實細節（不是 Penny 原話）：</p><pre class="verb">${esc(s.r7.supervisor)}</pre>`).join('')}<p class="note">主管的收尾指示（不是 Penny 原話）：</p><pre class="verb">${esc(O7.verbatim.supervisor.wrap_up)}</pre></details>
<details class="info"><summary>R7 改了哪些文字（舊 → 新，歷史）</summary>${ul(P.r7.changes.filter(x => x.kind !== '狀態（owner 決策）').map(x => `［${x.kind}］${x.where}：${x.old} → ${x.new}`))}</details>
<details class="info"><summary>R6 owner 決策、兩套原文與改動（歷史，逐字）</summary><pre class="verb">${esc(O6.verbatim.decisions)}</pre>${SETS.filter(s => s.r6.owner).map(s => `<p class="note"><b>${esc(s.id)}（${s.month} 月）Penny（R6）：</b>「${esc(s.r6.owner)}」</p><pre class="verb">${esc(s.r6.supervisor)}</pre>`).join('')}${ul(P.r6.changes.filter(x => x.kind !== '狀態（owner 決策）').map(x => `［${x.kind}］${x.where}：${x.old} → ${x.new}`))}</details>
<details class="info"><summary>R5 資料修訂與已接受套數的中英同步（歷史）</summary><p class="note">${esc(P.r5.summary)}</p>${ul(P.r5.changes.filter(x => !(x.kind === '印刷措辭' && x.where.startsWith('sets['))).map(x => `［${x.kind}］${x.where}：${x.old} → ${x.new}`))}<p class="note">${esc(P.accepted_notes.status)}：${esc(P.accepted_notes.summary)}</p>${ul(P.accepted_notes.items.map(x => `${x.id}：中文「${x.makeup_zh}」→ 英文補上「${x.added_en}」`))}</details>
<details class="info"><summary>R4 owner 決策與逐套要求（歷史，逐字）</summary><pre class="verb">${esc(O4.verbatim.decisions)}</pre>${SETS.filter(s => s.r4.owner).map(s => `<pre class="verb">${esc(s.r4.owner)}</pre>`).join('')}<pre class="verb">${esc(O4.verbatim.closing)}</pre></details>
<details class="info"><summary>R3 攝影設計要求（逐字，仍適用）</summary><pre class="verb">${esc(O3.verbatim.requirement)}</pre><pre class="verb">${esc(O3.verbatim.keep_existing)}</pre></details>
<details class="info"><summary>R2 已生效的決定（逐字）</summary><pre class="verb">${esc(O2.verbatim.decisions)}</pre>${ul(O2.summary.decided)}</details>
<div class="callout${hasOld ? ' warn' : ''}">${hasOld ? '這個瀏覽器裡有舊版（v1–v6）的回饋：都還在，各套與各位的區塊會列出來，只是歷史，<b>不會</b>變成新的核准；本頁不改寫也不清除它們。' : '這個瀏覽器沒有舊版回饋紀錄。'}</div>
</section>`;
  }

  function bookTable(b) {
    const rows = SETS.filter(s => s.book === b).sort((x, y) => x.month - y.month);
    return tbl(['月', 'ID', '狀態', '人設', '主題', '環境', '服裝', '色彩', '姿態', '表情', '性感', '攝影方法', '景別｜身體方向｜臉與視線｜拍攝角度'],
      rows.map(s => [`${s.month} 月`, link(s.id), stText(s), s.name, s.theme, s.env, Object.values(s.outfit).join('、'), s.palette, s.pose, s.expr, s.sexy, s.method, s.cam.line]), 'book');
  }
  function booksSec() {
    return `<section class="sec" id="books"><h2>兩本月份（已確認）與總覽</h2>
<p class="callout"><b>兩本月份人選排序已確認（R4 確認、R6／R7 維持；M-3 完成）。</b>不再請 Penny 重新核准；服裝與場景配合既定月份。</p>
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
<h3>R7 依owner指定修訂的 ${VSETS.length} 套（主管覆核通過）：改了什麼</h3>
${stbl(['ID', '攝影（不變）', '改了什麼'], VSETS.map(s => [link(s.id), s.cam.line, s.r7.change]), 'adj')}
<details class="info"><summary>R6 的 2 套新推薦（歷史）</summary>${stbl(['ID', '現在', '原設計（R5）', 'R6 改了什麼'], SETS.filter(s => s.r6.change).map(s => [link(s.id), { html: stTag(s) }, s.r6.from_line, s.r6.change]), 'adj')}</details>
<details class="info"><summary>R4 的 16 套修訂（歷史）</summary>${stbl(['ID', '現在', 'R4 改了什麼'], SETS.filter(s => s.r4.change).map(s => [link(s.id), { html: stTag(s) }, s.r4.change]), 'adj4')}</details>
<details class="info"><summary>共同規則與 prompt 一致性檢查</summary><h4>共同規則</h4>${ul(F.rules)}<h4>逐套檢查（產生資料時執行，不通過就無法建置）</h4>${ul(F.checks)}</details>
</section>`;
  }

  // ---------- 印刷構圖 ----------
  function printSec() {
    const R = P.printing, I = R.iris_first;
    const dg = b => `<figure class="pdiag"><button type="button" class="zoom svgz" data-svg="${esc(R.diagrams[b])}" data-cap="${esc(`${BOOK[b]}版型與裁切示意（不含照片）`)}" aria-label="放大：${esc(BOOK[b])}版型與裁切示意">` +
      `<img src="${esc(R.diagrams[b])}" alt="${esc(`${BOOK[b]}版型與裁切示意：成品、出血、安全框、假設線圈區、工作照片框與照片比例`)}" loading="lazy" decoding="async"><span class="zi" aria-hidden="true">放大</span></button>` +
      `<figcaption>${esc(BOOK[b])}：${esc(R.frames[b].name)} ${R.frames[b].mm[0]}×${R.frames[b].mm[1]} mm｜${esc(R.fit[b].img)} 放入：${esc(R.fit[b].crop)}｜<a href="${esc(R.diagrams[b])}" target="_blank" rel="noopener">開新分頁看原圖</a></figcaption></figure>`;
    return `<section class="sec" id="print"><h2>印刷構圖核對：裁切、出血與裝訂安全</h2>
<p class="callout"><b>工作照片框已接受（R6）</b>：${esc(P.owner_r6.summary.frames)}</p>
<p class="callout warn">${esc(R.note)}</p>
<h3>四類數字</h3>${stbl(['類別', '內容'], R.categories.map(x => [x.k, x.v]), 'cat4')}
<div class="pdiags">${dg('H')}${dg('V')}</div>
<h3>已知（廠商編輯器設定與商品頁）</h3>${stbl(['項目', '橫式', '直式', '來源'], R.known.map(x => [x.k, x.H, x.V, x.src]))}
<h3>假設（本案規劃用，不是廠商規格）</h3>${stbl(['項目', '橫式', '直式', '為什麼'], R.assumed.map(x => [x.k, x.H, x.V, x.why]))}
<h3>未知</h3>${ul(R.unknown)}
<h3>如果改用其他照片框</h3>${ul(R.compare.map(x => `${x.k}：${x.v}`))}
<h3>原則</h3>${ul(R.rules)}
<h3>V-iris-chen 首試是否需要構圖微調</h3>${ul([I.answer, I.condition, I.verify])}
<h3>${ACC.length} 套已接受是否受影響</h3><p class="note">${esc(R.accepted_impact.summary)}</p>
<details class="info" open><summary>24 套逐張印刷構圖判斷（依已接受的工作照片框）</summary>
<p class="note">百分比與「套框後約 x%」都是依規劃構圖推算的理論／規劃預估，不是實圖量測。</p>
${stbl(['ID', '狀態', '照片框', '比例計算', '邊緣（規劃預估）', '不能切', '規劃目標', '印刷判斷（條件）', '生成後待驗證', '原生尺寸', '有效 ppi'],
      SETS.map(s => [link(s.id), { html: stTag(s) }, s.print.frame, s.print.crop, s.print.edges.join('；'), s.print.keep, s.print.need, s.print.verdict, s.print.verify, s.print.native, s.print.ppi]), 'ptab')}</details>
</section>`;
  }

  function frameTable(fr) {
    const crop = ['chest', 'waist', 'thigh', 'knee'].includes(fr.shot);
    return tbl(['項目', '內容'], [['景別', fr.shot_zh], [crop ? '頭頂上方留白（規劃）' : '人物佔比（規劃）', crop ? `約 ${fr.headroom}%` : `約佔${fr.fill_of} ${fr.fill}%`],
      ['焦段／距離（參考）', `${fr.f}mm／約 ${fr.d} 公尺`], ['視野（寬×高）', `${fr.view_w}×${fr.view_h} 公尺`],
      ['相機與畫面中心', `相機約 ${fr.cam_m} 公尺高、畫面中心約 ${fr.centre_m} 公尺高，換算俯仰約 ${fr.tilt_deg > 0 ? '+' : ''}${fr.tilt_deg} 度`],
      ['原生尺寸', fr.native]]);
  }
  // 構圖示意：只畫畫框、頭與身體範圍（依企劃數字），不是照片
  function schem(s) {
    const k = s.frame.sch;
    return `<figure class="schw"><div class="nb2 sch r${s.book}" role="img" aria-label="${esc(`${s.id} 構圖示意：${s.cam.line}`)}">` +
      `<span class="sch-fig" data-x="${k.x}" data-w="${k.w}" data-top="${k.top}" data-bot="${k.bot}" data-head="${k.head}"${k.lie ? ' data-lie="1"' : ''}><i class="sch-h"></i><i class="sch-b"></i></span></div>` +
      (s.id === P.m4_prep.set ? `<figcaption class="sch-t"><b>${BOOK[s.book]}新照片 ${esc(s.ratio)}：首試已生成 1 張（M-4 R2；${esc(R3NOTE)}）</b>照片在<a href="shoot.html">目前檢視頁</a>，本頁不放；框內仍只是構圖示意</figcaption>`
        : `<figcaption class="sch-t"><b>${BOOK[s.book]}新照片 ${esc(s.ratio)}：尚未生成</b>框內只是構圖示意（人物範圍與頭的位置），不是照片</figcaption>`) +
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
<dt>印刷（工作照片框）</dt><dd>${esc(s.print.edges.join('；'))}；不能切：${esc(s.print.keep)}；${esc(s.print.need)}；${esc(s.print.ppi)}；${esc(s.print.verify)}</dd>
</dl></details>`;
  }
  const r6Hist = s => (s.r6.change ? `<details class="info"><summary>R6 的修改（歷史）</summary><p class="note">Penny（R6）：「${esc(s.r6.owner)}」</p><pre class="verb">${esc(s.r6.supervisor)}</pre><p class="note">${esc(s.r6.change)}</p><p class="note">原設計（R5）：${esc(s.r6.from_theme)}｜${esc(s.r6.from_line)}</p></details>` : '');
  function r4Box(s) {
    if (s.status === 'accepted') {
      return `<div class="r4box acc"><p><b>已接受（${esc(s.r7.accepted_in)} owner 紀錄）</b>：服裝、場景、表情與攝影照目前版本，不需再回覆。</p>` +
        (s.r5 ? `<p class="tnote"><b>R5 主管核可的中英同步</b>：英文 prompt 補上中文妝感「${esc(s.r5.makeup_zh)}」的一句（${esc(s.r5.added_en)}）；服裝、場景、表情、姿態、攝影與身分不變，接受狀態沿用。</p>` : '') + r6Hist(s) + '</div>';
    }
    const r7 = s.r7;
    return `<div class="r4box acc ver"><p><b>${esc(s.m4r1.label)}</b>：${esc(s.m4r1.note)}</p>
<p><b>R7 改了什麼：</b>${esc(r7.change)}</p>
<p><b>Penny 原文（R7）：</b>「${esc(r7.owner)}」</p>
<p class="tnote">${esc(r7.no_ref)}</p>
<details class="info" open><summary>修改前（R6）→ 修改後（R7）</summary>${stbl(['欄位', '修改前（R6）', '修改後（R7）'], r7.diff.map(x => [x.k, x.before, x.after]), 'diff7')}<p class="note">不變：${esc(r7.kept)}</p></details>
<details class="info"><summary>主管補充的落實細節（逐字，不是 Penny 原話）</summary><pre class="verb">${esc(r7.supervisor)}</pre></details>
${r6Hist(s)}
<details class="info"><summary>R4 的修改要求與改動（歷史）</summary><pre class="verb">${esc(s.r4.owner)}</pre><p class="note">${esc(s.r4.change)}</p></details></div>`;
  }
  function card(s) {
    const acc = s.status === 'accepted';
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
${old ? `<p class="oldfb">舊版回饋（歷史，不是新的核准）：${esc(old)}</p>` : ''}
${acc ? '' : `<p class="callout">這套不需要 Penny 回覆：${esc(s.m4r1.note)}</p>`}</article>`;
  }
  function person(p, i) {
    const old = oldLine(p.pid);
    return `<section class="sec person3" id="p-${esc(p.pid)}">
<div class="ph"><div class="ph-face">${fig(MP[p.pid].face, `${MP[p.pid].name}｜辨識用正臉（既有照片）`)}</div>
<div class="ph-t"><h2>${i + 1}. ${esc(MP[p.pid].name)}${MP[p.pid].native ? ` <span class="nat">${esc(MP[p.pid].native)}</span>` : ''}</h2>
<p class="cc-meta">身材設定：${esc(p.meas)}</p></div></div>
<details class="info fbq"><summary>R2 回饋與當時的落實（歷史紀錄；最新決定見各套卡片）</summary><pre class="verb">${esc(p.feedback)}${p.shared ? '\n' + esc(p.shared) : ''}</pre>${ul(p.applied)}</details>
${old ? `<p class="oldfb">舊版 v1／v2 回饋（保留，歷史）：${esc(old)}</p>` : ''}
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
<p class="callout warn"><b>${esc(I.status_m4r2)}</b> ${esc(K.status)} ${esc(K.gate)}</p>
<h3>Iris 首張：<a href="#c-${esc(I.set)}">${esc(I.set)}</a>（方向已接受）</h3>${ul(I.why)}
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
<p class="note"><b>怎麼拍：</b>${esc(M.recommend)}（Soul ID 不列在公開頁）</p>
<p class="note"><b>多階段與參考圖（R5 更正）：</b>${esc(M.multi_stage)}</p></details></section>`;
  }
  // ---------- V-Iris 首試準備（R7）：只整理，不生成 ----------
  function prepSec() {
    const M4 = P.m4_prep, C = M4.counts, IV = SET[M4.set], R1 = M4.r1, C1 = R1.counts, R2 = M4.r2, C2 = R2.counts, CH = R2.charge;
    const rows2 = [];
    R2.accept.forEach(g => g.items.forEach(x => rows2.push([g.k, x.c, x.r, x.v])));
    return `<section class="sec" id="prep"><h2>${esc(M4.title)}</h2>
<h3>${esc(R2.title)}</h3>
<p class="callout warn"><b>R2 當時：${esc(R2.status)}</b> ${esc(R2.auth)}生成請求 ${C2.generation_requests}、圖片 ${C2.images}、重送 ${C2.retries}、訓練 ${C2.trainings}、上傳 ${C2.uploads}。</p>
<p class="callout"><b>判定：</b>${esc(R2.verdict)}</p>
<p class="callout warn"><b>${esc(R3NOTE)}</b>照片、待決事項與回饋在<a href="shoot.html">目前檢視頁</a>。</p>
<h4>逐項驗收</h4>${stbl(['類別', '條件', '結果', '說明'], rows2, 'acc2')}
<h4>扣款與歸屬</h4>${stbl(['項目', '內容'], [
      ['扣款／退款', `扣款 ${CH.n_spend} 筆、退款 ${CH.n_refund} 筆（${CH.rows}）`],
      ['淨額', `${CH.net}（精確報價 ${CH.quote_exact}；核准預算 ${CH.budget} credit；任務完成後與終態後 15 分鐘各查一次）`], ['異常', CH.anomaly],
      ['歸屬層級', `${R2.attribution.level}；${R2.attribution.not}`]], 'chg2')}${ul(R2.attribution.basis)}
<details class="info"><summary>送出前核對與實際設定</summary>${stbl(['項目', '結果'], R2.pre.map(x => [x.k, x.v]), 'prep2')}<p class="note"><b>送出：</b>${esc(R2.request)}</p><p class="note"><b>任務：</b>${esc(R2.job.status)}；輸出 ${R2.job.px[0]}×${R2.job.px[1]}。${esc(R2.job.observed)}</p></details>
<p class="note">${esc(R2.files)}</p>
<h3>首試準備與首試前核查（R7、M-4 R1）</h3>
<p class="callout"><b>M-4 R1：</b>${esc(R1.review)}</p>
<p class="note">M-4 R1：生成 ${C1.generated}、credits ${C1.credits}、生成任務 ${C1.generation_jobs}、訓練 ${C1.trainings}、上傳 ${C1.uploads}；${esc(R1.counts_note)}（R7：生成 ${C.generated}、credits ${C.credits}、Higgsfield 呼叫 ${C.higgsfield_calls}、報價預檢 ${C.price_prechecks}。）</p>
<p class="note">完整文件：repo 的 <code>${esc(M4.doc)}</code>。企劃內容見 <a href="#c-${esc(M4.set)}">${esc(M4.set)} 卡片</a>；Penny 不需要再選企劃。</p>
<h3>${esc(R1.title)}</h3><p class="callout"><b>結論：</b>${esc(R1.verdict)}</p>
<h4>M-4 R1 的剩餘阻礙（M-4 R2 都已解除）</h4>${stbl(['阻礙', '說明', '誰決定', 'M-4 R2 狀態'], R1.blockers.map(x => [x.k, x.v, x.who, x.state]), 'block')}
<p class="note"><b>已不是阻礙：</b>${esc(R1.not_blockers.join('、'))}。<b>首張驗收要特別看的風險：</b>${esc(R1.risks.join('、'))}。</p>
<h4>建議費用上限</h4><p class="callout warn"><b>${esc(R1.cap.v)}</b>　${esc(R1.cap.why)}</p>${ul(R1.cap.stop.map(x => '停止條件：' + x))}<p class="note">${esc(R1.cap.stop_note)}</p>
<h4>Soul 證據</h4>${stbl(['項目', '內容'], R1.soul.map(x => [x.k, x.v]), 'prep2')}
<h4>當前模型參數與 Soul 狀態（2026-10-20 唯讀查詢）</h4>${stbl(['項目', '內容'], R1.params.map(x => [x.k, x.v]), 'prep2')}
<h4>首試單次請求的確切設定</h4>${stbl(['項目', '設定'], R1.request.map(x => [x.k, x.v]), 'prep2')}
<h4>報價（當前）</h4>${stbl(['報價', '回傳', '依據'], R1.quote.map(x => [x.k, x.v, x.basis]), 'prep3')}
<h4>歷史紀錄（另列，不拿來估算本次）</h4>${stbl(['紀錄', '數值', '說明'], R1.history.map(x => [x.k, x.v, x.basis]), 'prep3')}
<h4>計價單位</h4>${ul(R1.pricing)}<h4>失敗扣款規則</h4>${ul(R1.failure)}
<h4>交易核對：如何把本次請求與扣款對上</h4><ol class="facts">${R1.recon.map(x => `<li>${esc(x)}</li>`).join('')}</ol>${ul(R1.recon_limits.map(x => '限制：' + x))}
<h3>V-Iris 首試準備（R7 整理，M-4 R1 更新）</h3>
<h3>已接受的企劃</h3>${stbl(['項目', '內容'], M4.plan.map(x => [x.k, x.v]), 'prep2')}
<h3>身分參考</h3>${stbl(['項目', '內容'], M4.identity.map(x => [x.k, x.v]), 'prep2')}
<h3>最終 prompt 與生成比例</h3><p class="note"><b>生成比例：</b>${esc(M4.ratio)}</p>
<details class="info"><summary>最終 prompt（已接受版本，尚未執行；與卡片上的 prompt 草稿逐字相同）</summary><pre class="prompt">${esc(IV.prompt)}</pre></details>
<h3>工作流（前提未滿足前不執行）</h3>${stbl(['步驟', '內容'], M4.workflow.map(x => [x.k, x.v]), 'prep2')}
<h3>現在能準備的</h3>${ul(M4.ready_now)}
<h3>生成前的確認事項（M-4 R1 逐項狀態）</h3>${stbl(['項目', '狀態', '說明'], M4.tbc.map(x => [x.k, x.state, x.v]), 'prep3')}
<h3>首張驗收條件</h3>${M4.accept.map(g => `<h4>${esc(g.k)}</h4>${ul(g.items)}`).join('')}
<details class="info"><summary>送生成前檢查（R7 預先核對；主管 M-4 R1 接受三項差異；送出當下要再核一次）</summary>${stbl(['檢查', '結果', '說明'], M4.lint.map(x => [x.k, x.r, x.v]), 'prep3')}</details>
<h3>這份準備不代表</h3>${ul(M4.not)}
</section>`;
  }
  function outSec() {
    const oq = oldQs(), og = oldGnotes();
    return `<section class="sec" id="out"><h2>定稿進度與複製</h2>
<div class="callout"><b>M-3 已完成，沒有必填決策。</b>主管結論：23 套 owner 接受＋H-Luna 依 owner 指示修訂、主管覆核通過；不再要求 owner 填企劃問卷。這一頁不是生成授權，也不是費用核准。</div>
<p class="note">本頁只讀、不寫入也不清除這個瀏覽器的資料：v1–v6 的舊回饋與第二階段素材選擇都原樣保留，只在下面列為歷史。複製的文字是定稿進度，可以貼回 ChatGPT 備查。</p>
${OLDV.map(v => { const q = oldQ(v); return q.length ? `<p class="oldfb">${v} 題目的回答（保留，歷史）：${esc(q.join('；'))}</p>` : ''; }).join('')}
${oq.length ? `<p class="oldfb">v1／v2 題目的回答（保留，歷史）：${esc(oq.join('；'))}</p>` : ''}
${OLDV.map(v => (oldG(v) ? `<p class="oldfb">${v} 整體備註（保留，歷史）：${esc(oldG(v))}</p>` : '')).join('')}
${og.length ? `<p class="oldfb">v1／v2 整體備註（保留，歷史）：${esc(og.map(x => `${VER(x.v)}「${oneLine(x.note)}」`).join('；'))}</p>` : ''}
<div class="actions"><button type="button" class="btn" id="act-copy">複製定稿進度</button></div>
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
<li>完整企劃、攝影設計與印刷構圖：repo 的 <code>docs/calendar/CAL_18_M3_SHOOT_PLAN.md</code>（M-4 R1）；V-Iris 首試準備與首試前核查：<code>${esc(P.m4_prep.doc)}</code>；R2 Owner 決策逐字紀錄：<code>docs/calendar/CAL_19_M3_R2_OWNER_DECISION.md</code>。</li></ul></section>`;
  }

  function render() {
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    $('#planver').textContent = `${P.version}（${P.round}，${P.written_on}）`;
    app.innerHTML = decSec() + photoSec() + printSec() + booksSec() +
      `<section class="sec" id="people"><h2>12 位 × 橫式款／直式款</h2>
<ul class="facts"><li>每位兩套獨立企劃：服裝與場景都不同。左邊是橫式款（16:9），右邊是直式款（3:4）；手機上上下排列。</li>
<li>M-3 已完成：綠色「已接受」的 23 套照目前版本；H-luna-tanaka 標「依owner指示修訂・主管覆核通過」，寫明改了什麼、你的原文與修改前後。都不需要回覆。</li>
<li>每張卡片最上面直接寫<b>景別｜身體方向｜臉與視線｜拍攝角度</b>；七個攝影欄位與理由在「攝影設計細節」展開；虛線框下方一行是這張的印刷判斷。</li>
<li>虛線框是「尚未生成」的新照片位置，裡面的方框與圓點只是<b>構圖示意</b>，不是照片。卡片下方的照片都是<b>既有照片</b>，只按標示的用途參考，不是新構圖的成品；身材一律以設定數字為準。</li></ul>
<div class="ov">${PEOPLE.map((p, i) => { const m = IMG[MP[p.pid].face]; return `<a class="rs" href="#p-${esc(p.pid)}"><img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" alt="" loading="lazy" decoding="async"><span class="rs-t"><b>${i + 1}. ${esc(MP[p.pid].name)}</b><span class="rs-p" data-ov="${esc(p.pid)}"></span></span></a>`; }).join('')}</div>
</section>` + PEOPLE.map(person).join('') + compSec() + costSec() + prepSec() + outSec() + refsSec();
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
  const stOf = id => (SET[id].status === 'accepted' ? '已接受' : '主管覆核通過');
  function refresh(id) {
    const el = $(`[data-st="${id}"]`);
    if (el) {
      const acc = SET[id].status === 'accepted';
      el.textContent = acc ? '不需回覆' : '主管覆核通過（不需回覆）';
      el.className = 'st conf';
    }
    const pid = SET[id].pid;
    const ov = $(`[data-ov="${pid}"]`);
    if (ov) ov.textContent = ['H', 'V'].map(b => `${b}：${stOf(b + '-' + pid)}`).join('｜');
  }
  function buildText() {
    const M4 = P.m4_prep, R1 = M4.r1, R2 = M4.r2, C2 = R2.counts;
    const L = ['TASK-CAL-001｜已定稿企劃／歷史紀錄（M-3 企劃與 M-4 R1–R2）',
      `企劃版本：${P.version}（${P.round}）｜頁面版本：${PAGE_COMMIT || '本機預覽（未部署）'}`,
      '說明：M-3 已完成（主管結論），沒有必填決策。V-Iris 首試只授權 1 張，已送出一次並停止；這份進度不是新的生成授權或費用核准。'];
    L.push('', `【已接受 ${ACC.length} 套（R4／R6／R7 owner 紀錄）】`, ACC.map(s => s.id).join('、'));
    L.push('', `【${VER_LABEL}：${VSETS.length} 套】`);
    VSETS.forEach(s => {
      L.push(`${s.id}｜${s.month}月｜${s.name}｜${s.theme}｜${s.cam.line}`, `   改了什麼：${s.r7.change}`, `   Penny 原文（R7）：「${s.r7.owner}」`, `   ${s.m4r1.note}`);
    });
    L.push('', '【兩本月份】已確認（R4 確認、R6／R7 維持）', `【工作照片框】已接受（R6）：${P.owner_r6.summary.frames}`);
    L.push('', `【V-Iris 單張首試（M-4 R2）】R2 當時：${R2.status}`, `   判定：${R2.verdict}`,
      `   扣款 ${R2.charge.n_spend} 筆、退款 ${R2.charge.n_refund} 筆；淨額 ${R2.charge.net}（${R2.charge.rows}）`,
      `   歸屬：${R2.attribution.level}（${R2.attribution.not}）`, `   ${R3NOTE}`, `   照片：目前檢視頁 shoot.html`, `   文件：${M4.doc}`);
    L.push(`【本輪】生成請求 ${C2.generation_requests}、圖片 ${C2.images}、重送 ${C2.retries}、訓練 ${C2.trainings}、上傳 ${C2.uploads}；實扣 ${C2.credits_charged}（${R2.attribution.level}）`);
    OLDV.forEach(v => {
      const sets = SETS.map(s => [s, oldSet(v, s.id)]).filter(([, t]) => t), q = oldQ(v), g = oldG(v);
      if (!sets.length && !q.length && !g) return;
      L.push('', `【舊版回饋（${v}，僅供參考，不是新的核准）】`);
      sets.forEach(([s, t]) => L.push(`${s.id}：${t}`));
      q.forEach(t => L.push(`${v} 題目　${t}`));
      if (g) L.push(`整體備註（${v}）：${g}`);
    });
    const olds = PEOPLE.map(p => [p, oldLine(p.pid)]).filter(([, t]) => t);
    const oq = oldQs(), og = oldGnotes();
    if (olds.length || oq.length || og.length) {
      L.push('', '【舊版回饋（v1／v2，僅供參考，不是新的核准）】');
      olds.forEach(([p, t]) => L.push(`${MP[p.pid].name}：${t}`));
      oq.forEach(t => L.push(`舊版題目　${t}`));
      og.forEach(x => L.push(`整體備註（${VER(x.v)}）：${oneLine(x.note)}`));
    }
    return L.join('\n');
  }
  function refreshOut() {
    $('#bar-count').textContent = `歷史紀錄（只讀）｜M-3：已接受 ${ACC.length} 套＋主管覆核通過 ${VSETS.length} 套｜V-Iris 首試：反光板必修，人物與身材待 Penny 回饋`;
    const ta = $('#out-text');
    if (ta) ta.value = buildText();
  }

  // ---------- 事件 ----------
  app.addEventListener('click', e => {
    const z = e.target.closest('.zoom');
    if (z) { openViewer(z); return; }
    if (e.target.id === 'act-copy') copyOut();
  });
  $('#bar-copy').addEventListener('click', copyOut);

  async function copyOut() {
    const text = buildText();
    const ta = $('#out-text');
    ta.value = text;
    const done = '已複製企劃與歷史紀錄。可以貼回 ChatGPT；本頁不會通知主管。';
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
