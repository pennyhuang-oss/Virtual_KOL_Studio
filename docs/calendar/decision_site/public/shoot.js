// 2027 KOL 桌曆｜M-3 寫真拍攝企劃（R2：24 套雙款）。企劃內容來自 data.js 的 m3（產生自 data/cal_m3_shoot_plan.json）；本頁沒有任何生成圖。
// Penny 的回饋只存在本機瀏覽器 localStorage（cal2027-shoot-v1:<SHA>），不送到伺服器；沒有追蹤或分析。
// v3 的回饋另存在同一筆資料的 v3 欄位；v1／v2 留下的欄位原樣保留，只顯示成「舊版」、不算 v3。載入時不改寫，只有 Penny 動手後才存。
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

  // ---------- v3 回饋 ----------
  const CH = { ok: '接受', edit: '想修改' };
  const QS = {
    months_h: { label: '橫式款月份推薦', opts: { ok: '接受', edit: '想調整（寫在備註）' } },
    months_v: { label: '直式款月份推薦', opts: { ok: '接受', edit: '想調整（寫在備註）' } },
    layout: { label: '版面與構圖建議', opts: { ok: '接受', edit: '想修改（寫在備註）' } },
    iris_first: { label: 'Iris 首張試拍候選', opts: { v: '同意先試 V-iris-chen（不是費用核准）', h: '想先試 H-iris-chen', edit: '想修改（寫在備註）' } },
    assign: { label: '已接受方向的 H／V 分配', opts: { ok: '接受', edit: '想對調（寫在備註）' } },
  };
  function loadV3() {
    const v = RAW.v3 && typeof RAW.v3 === 'object' ? RAW.v3 : {};
    const out = { ver: CUR, sets: {}, q: {}, gnote: str(v.gnote) };
    SETS.forEach(s => { const x = (v.sets || {})[s.id] || {}; out.sets[s.id] = { c: CH[x.c] ? x.c : '', note: str(x.note) }; });
    Object.keys(QS).forEach(k => { const x = (v.q || {})[k] || {}; out.q[k] = { c: QS[k].opts[x.c] ? x.c : '', note: str(x.note) }; });
    return out;
  }
  let V3 = loadV3();
  function save() {
    RAW.v3 = V3;
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
    const O = P.owner_r2, Sm = O.summary;
    const hasOld = PEOPLE.some(p => oldLine(p.pid)) || oldQs().length || oldGnotes().length;
    return `<section class="sec" id="dec"><h2>Penny 已生效的決定（R2）</h2>
<pre class="verb">${esc(O.verbatim.decisions)}</pre>
<p class="note">以上逐字保存（主管轉述）。執行整理：</p>
${ul(Sm.decided)}
<p class="note"><b>已接受的方向</b>（各保留為其中一款，另一款另設完全不同的服裝與場景；放 H 或 V 是執行者的推薦，不是 Penny 的決定）：</p>
${ul(Sm.accepted_directions.map(x => `${MP[x.pid].name}：${x.what}`))}
<p class="callout warn"><b>${esc(Sm.iris_first)}</b> 尚未授權：${esc(Sm.not_authorized.join('、'))}。尚未核准：${esc(Sm.not_approved.join('、'))}。</p>
<div class="callout${hasOld ? ' warn' : ''}">${hasOld ? '這個瀏覽器裡有 v1／v2 的舊回饋：都還在，各位的區塊會列出來，<b>不算</b> v3 的回覆。' : '這個瀏覽器沒有舊版回饋紀錄。'}</div>
</section>`;
  }

  function bookTable(b) {
    const rows = SETS.filter(s => s.book === b).sort((x, y) => x.month - y.month);
    return tbl(['月', 'ID', '人設', '主題', '環境', '服裝', '色彩', '姿態', '表情', '性感', '攝影方法', '景別'],
      rows.map(s => [`${s.month} 月`, link(s.id), s.name, s.theme, s.env, Object.values(s.outfit).join('、'), s.palette, s.pose, s.expr, s.sexy, s.method, `${s.frame.shot_zh}（${s.frame.ratio}）`]), 'book');
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

  function frameTable(fr) {
    return tbl(['項目', '內容'], [['景別', fr.shot_zh], ['人物佔比', `約佔${fr.pct_of} ${fr.pct}%`], ['頭頂／手腳', fr.ext_zh], ['留白位置', fr.space_zh],
      ['焦段／距離', `${fr.f}mm／約 ${fr.d} 公尺`], ['視野（寬×高）', `${fr.view_w}×${fr.view_h} 公尺`], ['原生尺寸', fr.native], ['版面適配', fr.fit]]);
  }
  function card(s) {
    const x = V3.sets[s.id];
    return `<article class="scard ${s.book === 'H' ? 'bh' : 'bv'}" id="c-${esc(s.id)}" data-set="${esc(s.id)}">
<p class="sc-head"><code class="sid">${esc(s.id)}</code> <span class="tag book">${BOOK[s.book]}（${esc(s.ratio)}）</span> <span class="tag ${s.origin === 'new' ? 'o-new' : 'o-acc'}">${esc(ORIGIN[s.origin])}</span> <span class="tag mon">推薦 ${s.month} 月</span> <span class="st none" data-st="${esc(s.id)}"></span></p>
<p class="sc-theme">${esc(s.theme)}</p>
<div class="nb2 r${s.book}"><b>${BOOK[s.book]}新照片 ${esc(s.ratio)}</b><span>尚未生成</span></div>
<div class="rgrid">${s.refs.map(r => refFig(r, s.pid)).join('')}</div>
<dl class="pdl">
<dt>場景</dt><dd>${esc(s.scene)}</dd>
<dt>服裝</dt><dd>${outfitList(s.outfit)}</dd>
<dt>姿態</dt><dd>${esc(s.pose)}${esc(s.hands)}</dd>
<dt>表情</dt><dd>${esc(s.expr)}；${esc(s.gaze)}</dd>
<dt>光影</dt><dd>主光：${esc(s.light['主光'])}<br>補光：${esc(s.light['補光'])}</dd>
</dl>
<details class="info"><summary>身材、妝髮、景別與差異</summary>
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
<fieldset class="fb"><legend>回饋：${esc(s.id)}</legend>
<div class="fb-opts">${Object.entries(CH).map(([k, v]) => `<label class="fb-o"><input type="radio" name="s-${esc(s.id)}" value="${k}" data-s="${esc(s.id)}"${x.c === k ? ' checked' : ''}> ${esc(v)}</label>`).join('')}</div>
<label class="lbl" for="n-${esc(s.id)}">備註</label>
<textarea id="n-${esc(s.id)}" data-n="${esc(s.id)}" rows="2" maxlength="2000" placeholder="例：衣服想換顏色；場景想更高級">${esc(x.note)}</textarea>
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
${old ? `<p class="oldfb">舊版回饋（保留，不算 v3）：${esc(old)}</p>` : ''}
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
    const oq = oldQs(), og = oldGnotes();
    return `<section class="sec" id="out"><h2>回饋與複製</h2>
<div class="callout">回饋只存在這個瀏覽器，<b>不會送到伺服器</b>，也不會通知主管。<b>未回覆不算接受。</b>複製後請貼回 ChatGPT。這是對企劃方向的回饋，不是生成授權或費用核准。</div>
<h3>想請 Penny 決定的事</h3><ol class="facts">${P.questions.map(x => `<li>${esc(x)}</li>`).join('')}</ol>
<p class="note">第 1 題在各套卡片上選；其他在下面選：</p>
${Object.entries(QS).map(([k, Q]) => `<fieldset class="fb"><legend>${esc(Q.label)}</legend><div class="fb-opts col">${Object.entries(Q.opts).map(([v, t]) =>
      `<label class="fb-o"><input type="radio" name="q-${k}" value="${v}" data-q="${k}"${V3.q[k].c === v ? ' checked' : ''}> ${esc(t)}</label>`).join('')}</div>
<label class="lbl" for="qn-${k}">備註</label><textarea id="qn-${k}" data-qn="${k}" rows="1" maxlength="1500">${esc(V3.q[k].note)}</textarea></fieldset>`).join('')}
${oq.length ? `<p class="oldfb">舊版題目的回答（保留，不算 v3）：${esc(oq.join('；'))}</p>` : ''}
<label class="lbl" for="gnote">整體備註</label>
<textarea id="gnote" rows="3" maxlength="3000" placeholder="例：整體想要更多戶外；性感程度想再高一點">${esc(V3.gnote)}</textarea>
${og.length ? `<p class="oldfb">舊版整體備註（保留）：${esc(og.map(x => `${VER(x.v)}「${oneLine(x.note)}」`).join('；'))}</p>` : ''}
<div class="actions"><button type="button" class="btn" id="act-copy">複製回饋</button><button type="button" class="btn danger" id="act-reset">清除 v3 回饋</button></div>
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
<li>完整企劃：repo 的 <code>docs/calendar/CAL_18_M3_SHOOT_PLAN.md</code>；Owner 決策逐字紀錄：<code>docs/calendar/CAL_19_M3_R2_OWNER_DECISION.md</code>。</li></ul></section>`;
  }

  function render() {
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    $('#planver').textContent = `${P.version}（${P.round}，${P.written_on}）`;
    app.innerHTML = decSec() + booksSec() +
      `<section class="sec" id="people"><h2>12 位 × 橫式款／直式款</h2>
<ul class="facts"><li>每位兩套獨立企劃：服裝與場景都不同。左邊是橫式款（16:9），右邊是直式款（3:4）；手機上上下排列。</li>
<li>灰色框是「尚未生成」的新照片位置。旁邊的照片都是<b>既有照片</b>，只按標示的用途參考（表情／場景／服裝材質／身分），不是新企劃的成品；身材一律以設定數字為準。</li></ul>
<div class="ov">${PEOPLE.map((p, i) => { const m = IMG[MP[p.pid].face]; return `<a class="rs" href="#p-${esc(p.pid)}"><img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" alt="" loading="lazy" decoding="async"><span class="rs-t"><b>${i + 1}. ${esc(MP[p.pid].name)}</b><span class="rs-p" data-ov="${esc(p.pid)}"></span></span></a>`; }).join('')}</div>
</section>` + PEOPLE.map(person).join('') + compSec() + costSec() + outSec() + refsSec();
    SETS.forEach(s => refresh(s.id));
    refreshOut();
  }
  function refresh(id) {
    const c = V3.sets[id].c;
    const el = $(`[data-st="${id}"]`);
    if (el) { el.textContent = c ? CH[c] : '未回覆'; el.className = `st ${c === 'ok' ? 'conf' : (c ? 'draft' : 'none')}`; }
    const pid = SET[id].pid;
    const ov = $(`[data-ov="${pid}"]`);
    if (ov) ov.textContent = ['H', 'V'].map(b => `${b}：${V3.sets[b + '-' + pid].c ? CH[V3.sets[b + '-' + pid].c] : '未回覆'}`).join('｜');
  }
  function buildText() {
    const L = ['TASK-CAL-001／M-3／R2｜24套雙款獨立寫真企劃｜Penny 企劃回饋',
      `企劃版本：${P.version}（${P.round}）｜頁面版本：${PAGE_COMMIT || '本機預覽（未部署）'}`,
      '說明：這是對 24 套企劃方向的回饋，不是生成授權，也不是費用核准；未回覆不算接受。'];
    let ok = 0, ed = 0;
    ['H', 'V'].forEach(b => {
      L.push('', `【${BOOK[b]}（${b === 'H' ? '16:9' : '3:4'}）】`);
      SETS.filter(s => s.book === b).forEach(s => {
        const x = V3.sets[s.id];
        if (x.c === 'ok') ok++; else if (x.c === 'edit') ed++;
        L.push(`${s.id}｜${s.name}｜${s.theme}：${x.c ? CH[x.c] : '未回覆'}`);
        if (x.note.trim()) L.push(`   備註：${oneLine(x.note)}`);
      });
    });
    L.push('', `（已回覆 ${ok + ed}／24 套：接受 ${ok}、想修改 ${ed}、未回覆 ${24 - ok - ed}）`, '');
    Object.entries(QS).forEach(([k, Q]) => {
      const x = V3.q[k];
      L.push(`【${Q.label}】${x.c ? Q.opts[x.c] : '未回覆'}${x.note.trim() ? `；備註：${oneLine(x.note)}` : ''}`);
    });
    L.push(`【整體備註】${V3.gnote.trim() ? oneLine(V3.gnote) : '（無）'}`);
    const olds = PEOPLE.map(p => [p, oldLine(p.pid)]).filter(([, t]) => t);
    const oq = oldQs(), og = oldGnotes();
    if (olds.length || oq.length || og.length) {
      L.push('', '【舊版回饋（v1／v2，僅供參考，不算 v3）】');
      olds.forEach(([p, t]) => L.push(`${MP[p.pid].name}：${t}`));
      oq.forEach(t => L.push(`舊版題目　${t}`));
      og.forEach(x => L.push(`整體備註（${VER(x.v)}）：${oneLine(x.note)}`));
    }
    return L.join('\n');
  }
  function refreshOut() {
    const n = SETS.filter(s => V3.sets[s.id].c).length;
    $('#bar-count').textContent = `已回覆 ${n}／24 套｜尚未生成任何照片`;
    const ta = $('#out-text');
    if (ta) ta.value = buildText();
  }

  // ---------- 事件 ----------
  app.addEventListener('change', e => {
    const t = e.target;
    if (t.dataset.s) { V3.sets[t.dataset.s].c = t.value; save(); refresh(t.dataset.s); refreshOut(); }
    else if (t.dataset.q) { V3.q[t.dataset.q].c = t.value; save(); refreshOut(); }
  });
  app.addEventListener('input', e => {
    const t = e.target;
    if (t.dataset.n) { V3.sets[t.dataset.n].note = t.value; save(); refreshOut(); }
    else if (t.dataset.qn) { V3.q[t.dataset.qn].note = t.value; save(); refreshOut(); }
    else if (t.id === 'gnote') { V3.gnote = t.value; save(); refreshOut(); }
  });
  app.addEventListener('click', e => {
    const z = e.target.closest('.zoom');
    if (z) { openViewer(z); return; }
    const cl = e.target.closest('[data-clear]');
    if (cl) {
      const id = cl.dataset.clear;
      V3.sets[id] = { c: '', note: '' };
      save();
      $$(`input[name="s-${id}"]`).forEach(r => { r.checked = false; });
      $(`#n-${id}`).value = '';
      refresh(id); refreshOut();
      toast(`已清除 ${id} 的回饋。`);
      return;
    }
    if (e.target.id === 'act-copy') copyOut();
    if (e.target.id === 'act-reset') {
      if (!window.confirm('清除本頁 v3 的全部回饋？（v1／v2 舊回饋與第二階段素材選擇都不受影響）')) return;
      delete RAW.v3;
      V3 = loadV3();
      try { localStorage.setItem(KEY, JSON.stringify(RAW)); } catch (e2) { /* 只清記憶體 */ }
      render();
      toast('已清除 v3 回饋；舊版回饋保留。');
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
