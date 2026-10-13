// 2027 KOL 桌曆｜M-3 寫真拍攝企劃（R1 修訂版）。企劃內容來自 data.js 的 m3（產生自 data/cal_m3_shoot_plan.json）；本頁沒有任何生成圖。
// Penny 的回饋只存在本機瀏覽器 localStorage（cal2027-shoot-v1:<SHA>），不送到伺服器；沒有追蹤或分析。
// 舊版（v1）頁面存的回饋原樣保留：載入時不改寫；只在 Penny 動手修改後才存成新格式，舊的選擇與備註搬進 prev 保存。
// 舊版回饋一律標成「舊版」，不算新版的回覆。第二階段素材選擇（cal2027-materials-v1:<SHA>）本頁不讀、不寫、不刪。
'use strict';
(() => {
  const D = window.CAL_DATA;
  const app = document.getElementById('app');
  if (!D || !D.m3 || !D.mat) { app.textContent = '資料載入失敗。'; return; }

  const SHA = D.fixed_sha;
  const KEY = 'cal2027-shoot-v1:' + SHA;
  const IMG = D.images;
  const P = D.m3;
  const CUR = P.version;
  const OLD = P.revision.from_version;
  const MP = {};
  const ITEM = {};
  D.mat.people.forEach(p => { MP[p.pid] = p; p.items.forEach(it => { ITEM[it.id] = { ...it, pid: p.pid }; }); });
  const PEOPLE = P.people;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const nm = pid => MP[pid].name;
  const fullName = pid => MP[pid].native ? `${MP[pid].name} ${MP[pid].native}` : MP[pid].name;
  const VER_ZH = v => (v === CUR ? '新版 v2' : (v === OLD ? '舊版 v1' : v));
  const oneLine = s => s.trim().replace(/\s*\n\s*/g, '／');

  // ---------- 回饋狀態 ----------
  const CH = { main: '接受主方向', alt: '改用替代方向', edit: '想修改' };
  const QS = {
    hv: { label: '橫直構圖', opts: { both: '先採用：同一造型橫、直各拍一張', one: '先只拍 3:4 直幅，等版面決定', unsure: '還不確定' } },
    phase1: { label: '第一階段試拍', opts: { ok: '同意方向：第一階段先試 Iris 一位（費用另外查證、核定）', swap: '想換第一階段的人（寫在備註）', hold: '先不要試拍' } },
  };
  // 舊版頁面的題目與選項文字（只用來顯示舊回答）
  const QS_OLD = {
    hv: { label: '橫直構圖', opts: { both: '同意：同一造型橫、直各拍一張', one: '先只拍一種（寫在備註）', unsure: '還不確定' } },
    first: { label: '首批試拍（首批 4 位＋依 0.12 計價的上限；已撤回）', opts: { ok: '同意這個方向（Iris、Rin、Miu、Mia；上限依建議），由主管另發執行指令', swap: '想換首批人選或上限（寫在備註）', hold: '先不要試拍' } },
  };
  const qLabel = (k, v, ver) => { const T = ver === CUR ? QS : QS_OLD; return (T[k] && T[k].opts[v]) || v; };
  const str = x => (typeof x === 'string' ? x : '');
  function blank() {
    return { fmt: 2, p: Object.fromEntries(PEOPLE.map(p => [p.pid, { c: '', v: '', note: '', nv: '', prev: [] }])),
      q: {}, qv: {}, qprev: [], gnote: '', gnv: '', gprev: [] };
  }
  let storageOK = true;
  function load() {
    const S0 = blank();
    try {
      const s = JSON.parse(localStorage.getItem(KEY));
      if (!s || typeof s !== 'object') return S0;
      PEOPLE.forEach(({ pid }) => {
        const q = (s.p || {})[pid] || {};
        const c = CH[q.c] ? q.c : '';
        const note = str(q.note);
        S0.p[pid] = { c, v: c ? (str(q.v) || OLD) : '', note, nv: note ? (str(q.nv) || OLD) : '',
          prev: Array.isArray(q.prev) ? q.prev.filter(x => x && typeof x === 'object') : [] };
      });
      Object.entries(s.q || {}).forEach(([k, v]) => { if (typeof v === 'string' && v) { S0.q[k] = v; S0.qv[k] = str((s.qv || {})[k]) || OLD; } });
      S0.qprev = Array.isArray(s.qprev) ? s.qprev : [];
      S0.gnote = str(s.gnote);
      S0.gnv = S0.gnote ? (str(s.gnv) || OLD) : '';
      S0.gprev = Array.isArray(s.gprev) ? s.gprev : [];
    } catch (e) { storageOK = false; }
    return S0;
  }
  let S = load();
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(S)); storageOK = true; } catch (e) {
      if (storageOK) toast('這個瀏覽器不允許儲存（例如無痕模式）：重新整理後回饋會消失，請先複製。');
      storageOK = false;
    }
  }
  const curChoice = pid => { const q = S.p[pid]; return q.c && q.v === CUR ? q.c : ''; };
  function oldChoices(pid) {  // 所有舊版留下的選擇（目前欄位＋prev）
    const q = S.p[pid];
    const out = q.prev.filter(x => x.c && x.v !== CUR).map(x => ({ c: x.c, v: x.v }));
    if (q.c && q.v !== CUR) out.push({ c: q.c, v: q.v });
    return out;
  }
  function oldNotes(pid) {
    const q = S.p[pid];
    return q.prev.filter(x => typeof x.note === 'string' && x.note.trim()).map(x => ({ note: x.note, v: x.v }));
  }
  function setChoice(pid, c) {
    const q = S.p[pid];
    if (q.c && q.v !== CUR) q.prev.push({ c: q.c, v: q.v });
    q.c = c; q.v = CUR;
  }
  function setNote(pid, text) {
    const q = S.p[pid];
    if (q.note.trim() && q.nv !== CUR) q.prev.push({ note: q.note, v: q.nv });
    q.note = text; q.nv = text ? CUR : '';
  }
  function setQ(k, v) {
    if (S.q[k] && S.qv[k] !== CUR) S.qprev.push({ k, a: S.q[k], v: S.qv[k] });
    S.q[k] = v; S.qv[k] = CUR;
  }
  function setG(text) {
    if (S.gnote.trim() && S.gnv !== CUR) S.gprev.push({ note: S.gnote, v: S.gnv });
    S.gnote = text; S.gnv = text ? CUR : '';
  }
  const oldQ = () => [...S.qprev.filter(x => x.v !== CUR), ...Object.keys(S.q).filter(k => S.qv[k] !== CUR).map(k => ({ k, a: S.q[k], v: S.qv[k] }))];

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
  const REF_TAG = '<span class="tag t-ref">既有照片參考</span>';
  function refFig(id) {
    const it = ITEM[id];
    return fig(it.img, `${nm(it.pid)}｜${id}｜${it.label}｜既有照片，只當參考`, `${REF_TAG} <code>${esc(id)}</code> ${esc(it.label)}`);
  }
  const ul = a => `<ul class="facts">${a.map(x => `<li>${esc(x)}</li>`).join('')}</ul>`;
  const tbl = (head, rows) => `<div class="tbl"><table><thead><tr>${head.map(h => `<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>` +
    rows.map(r => `<tr>${r.map(c => `<td>${esc(c)}</td>`).join('')}</tr>`).join('') + '</tbody></table></div>';
  const REV_ZH = { direction: 'R1：主方向修訂', pose: 'R1：姿態與細節修訂' };

  function revSec() {
    const R = P.revision;
    const withOld = PEOPLE.filter(p => oldChoices(p.pid).length || (S.p[p.pid].note && S.p[p.pid].nv !== CUR));
    return `<section class="sec" id="rev"><h2>這一版改了什麼（R1）</h2>
${tbl(['主管覆核項目', '結論'], R.verdicts.map(x => [x.k, x.v]))}
<ul class="facts">
<li><b>Somi、Miu、Mia 的主方向改了</b>：Somi 不再拿炸雞（食物只在畫面邊緣）、Miu 從吧台改到窗邊座位（不穿圍裙、不捧杯）、Mia 改成簡潔站姿（耳機只是小配件）。原本的拍法改列為各自的替代方向。</li>
<li><b>其他九位逐位檢查</b>：拿掉像隨拍的動作、遮身形的衣服與多餘動作；每張只留一個主要姿態，表情是一個靜止的瞬間。</li>
<li><b>光線與膚色</b>：允許畫面外的柔光箱、反光板補光；逆光一定補臉；膚色只寫一次她原本的白皙膚色，不再堆疊「瓷白」。</li>
<li><b>取景重算</b>：每位的橫、直各有景別、人物佔比、頭頂與手腳範圍、留白位置；焦段與距離都換算過（舊版「85mm、5 公尺、橫幅全身」拍不下全身）。</li>
<li><b>移除四條全組硬性規則</b>：${esc(R.method_removed.join('、'))}。</li>
<li><b>費用</b>：舊版的預算數字撤回；生成仍暫停。Penny 可以先決定拍攝方向，費用另外核定。</li>
</ul>
<div class="callout${withOld.length ? ' warn' : ''}">${withOld.length
      ? `你在舊版填過 ${withOld.length} 位的回饋：${esc(withOld.map(p => nm(p.pid)).join('、'))}。這些都還在，卡片上標成「舊版」，<b>不算</b>新版的回覆；請看過新版後重新選。`
      : '這個瀏覽器沒有舊版的回饋紀錄。'}</div>
</section>`;
  }

  function aaliyaSec() {
    const A = P.aaliya;
    const src = P.meta.aaliya_sources;
    return `<section class="sec" id="aaliya"><h2>一、參考 Aaliya 的「拍攝方法」</h2>
<p class="callout warn"><b>⚠ ${esc(A.warning)}</b></p>
<p class="note">以下 5 張是 Aaliya 型錄頁（<a href="${esc(src.catalog_url)}" target="_blank" rel="noopener noreferrer">型錄頁</a>）上最像專業寫真、形式又各不相同的既有照片。只用來說明「光怎麼打、人怎麼站、背景怎麼處理」。</p>
<div class="agrid">${A.items.map(x => `<article class="ac">
${fig(P.aaliya_img[x.key], `Aaliya｜${x.form}｜既有照片，只參考拍法`, `<span class="tag t-ref">Aaliya 既有照片</span> ${esc(x.form)}`)}
<ul class="facts">${x.obs.map(o => `<li>${esc(o)}</li>`).join('')}</ul>
<p class="ac-rec">紀錄：模型 ${esc(x.model)}｜原始 prompt ${esc(x.prompt)}</p></article>`).join('')}</div>
<h3>移植到 12 位的做法（R1 修訂）</h3>
<dl class="mdl">${A.method.map(m => `<dt>${esc(m.item)}</dt><dd>${esc(m.how)}</dd>`).join('')}</dl>
<p class="note">R1 拿掉的全組硬性規則：${esc(P.revision.method_removed.join('、'))}。這些不是專業寫真的必要條件。</p>
<details class="info"><summary>紀錄細節：哪些有紀錄、哪些是推定</summary>
<ul class="facts"><li>${esc(src.identity_note)}</li><li>${esc(src.note)}</li>
<li>face_reference：${esc(A.records.face_reference)}</li><li>soul_test_v1：${esc(A.records.soul_test_v1)}</li>
<li>後製與中繼資料：${esc(A.records.post)}</li><li>未採用：${esc(A.not_used)}</li></ul>
${tbl(['形式', '檔案', '類別', '原圖尺寸（實測）', '模型（紀錄）', '原始 prompt', 'Soul', '後製／裁切／增強'],
    A.items.map(x => [x.form, x.file, x.kind, `${x.px[0]}×${x.px[1]}`, x.model, x.prompt, x.soul, x.post]))}
</details></section>`;
  }

  function ownerSec() {
    const O = P.owner_refs;
    return `<section class="sec" id="owner"><h2>二、Penny 喜歡的 4 張（審美參考，不變）</h2>
<p class="note">${esc(O.note)}</p>
<div class="ogrid">${O.items.map(x => `<article class="oc">${refFig(x.id)}<p class="oc-w">${esc(x.what)}</p><p class="oc-c">可借用：${esc(x.cue)}</p></article>`).join('')}</div>
<p class="note">${esc(O.reading)}</p></section>`;
  }

  function overview() {
    return `<div class="ov">${PEOPLE.map((p, i) => {
      const m = IMG[MP[p.pid].face];
      return `<a class="rs" href="#s-${esc(p.pid)}"><img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" alt="" loading="lazy" decoding="async">` +
        `<span class="rs-t"><b>${i + 1}. ${esc(nm(p.pid))}</b><span class="rs-p">${esc(p.title)}</span><span class="rs-p rv-${esc(p.rev)}">${esc(REV_ZH[p.rev])}</span><span class="rs-p" data-ov="${esc(p.pid)}"></span></span></a>`;
    }).join('')}</div>`;
  }
  function diffTable() {
    return tbl(['人設', '時段', '光線', '配色', '場景', '服裝', '姿勢', '表情', '取景'],
      PEOPLE.map(p => { const f = p.diff; return [nm(p.pid), f.time, f.light, f.palette, f.place, f.outfit, f.pose, f.face, f.frame]; }));
  }
  function frameTable(p) {
    const H = p.frames.H, V = p.frames.V;
    const row = (k, fn) => [k, fn(H), fn(V)];
    return tbl(['', '橫 3:2', '直 3:4'], [
      row('景別', x => x.shot_zh),
      row('人物佔畫面高度', x => `約 ${x.pct}%`),
      row('頭頂／手腳範圍', x => x.ext_zh),
      row('留白位置', x => x.space_zh),
      row('焦段／距離', x => `${x.f}mm／約 ${x.d} 公尺`),
      row('視野（寬×高，公尺）', x => `${x.view_w}×${x.view_h}`),
      row('模型原生輸出', x => x.native),
      row('版面適配（只是比例換算）', x => x.fit),
    ]);
  }
  function plan(p, i) {
    const pid = p.pid;
    const cur = curChoice(pid);
    const olds = oldChoices(pid);
    const q = S.p[pid];
    const titleChanged = p.prev.title !== p.title;
    return `<section class="sec plan" id="s-${esc(pid)}" data-pid="${esc(pid)}">
<div class="ph"><div class="ph-face">${fig(MP[pid].face, `${fullName(pid)}｜辨識用正臉（既有照片）`)}</div>
<div class="ph-t"><h2>${i + 1}. ${esc(nm(pid))}${MP[pid].native ? ` <span class="nat">${esc(MP[pid].native)}</span>` : ''}</h2>
<p class="ptitle">${esc(p.title)}</p>
<p><span class="tag rv-${esc(p.rev)}">${esc(REV_ZH[p.rev])}</span>${p.first ? ' <span class="tag t-first">第一階段建議（待批准）</span>' : ''} <span class="st none" data-st="${esc(pid)}"></span></p></div></div>
<div class="revbox"><p class="pn-h">這一版改了什麼${titleChanged ? `（舊版標題：${esc(p.prev.title)}）` : ''}</p>${ul(p.rev_items)}</div>
<div class="pgrid">
<div class="pnew"><p class="pn-h">這個企劃的新照片</p><div class="ng"><div class="nb nb-h"><b>橫 3:2</b><span>尚未生成</span></div><div class="nb nb-v"><b>直 3:4</b><span>尚未生成</span></div></div>
<p class="pn-n">目前不會試拍：生成暫停，等 Penny 批准與主管另發指令。這裡不放任何示意圖。</p></div>
<div class="pref"><p class="pn-h">既有照片參考：認人與氣質用，<b>不是新成品，不會照抄</b></p><div class="rgrid">${p.refs.map(refFig).join('')}</div></div>
</div>
<dl class="pdl">
<dt>為什麼適合她</dt><dd>${esc(p.why)}</dd>
<dt>畫面</dt><dd>${esc(p.scene)}</dd>
<dt>穿什麼</dt><dd>${esc(p.outfit)}<br>髮型：${esc(p.hair)}<br>配件：${esc(p.acc)}</dd>
<dt>光線</dt><dd>${esc(p.light)}</dd>
<dt>表情與姿勢</dt><dd>${esc(p.expr)}<br>${esc(p.pose)}</dd>
<dt>甜美在哪</dt><dd>${esc(p.sweet)}</dd>
<dt>性感在哪</dt><dd>${esc(p.sexy)}</dd>
<dt>替代方向</dt><dd>${esc(p.alt)}</dd>
</dl>
<details class="info"><summary>取景設計：橫／直分別怎麼拍</summary>${frameTable(p)}</details>
<details class="info"><summary>與人設核對、逐項檢查與風險</summary>
<dl class="pdl small"><dt>與人設核對</dt><dd>${esc(p.check)}</dd>
${p.check9.length ? `<dt>逐項檢查</dt><dd>${ul(p.check9)}</dd>` : ''}
<dt>舊版姿勢</dt><dd>${esc(p.prev.pose)}</dd></dl>
${tbl(['風險', '處理'], p.risks.map(r => [r.risk, r.fix]))}
</details>
<details class="info"><summary>prompt 草稿（尚未執行）</summary>
<p class="note">可直接使用的英文草稿，<b>沒有送出過</b>。橫、直兩段的取景句各自依上面的取景設計寫成；每段結尾都有同一句皮膚與質感描述。執行時沿用這位既有的 Soul（不列在公開頁）。</p>
<p class="lbl">橫構圖（3:2）</p><pre class="prompt">${esc(p.prompt_h)}</pre>
<p class="lbl">直構圖（3:4）</p><pre class="prompt">${esc(p.prompt_v)}</pre>
</details>
<fieldset class="fb"><legend>Penny 的回饋：${esc(nm(pid))}（新版）</legend>
${olds.length ? `<p class="oldfb">舊版回饋（保留，不算新版）：${esc(olds.map(x => `${VER_ZH(x.v)} 選了「${CH[x.c] || x.c}」`).join('；'))}</p>` : ''}
<div class="fb-opts">${Object.entries(CH).map(([k, v]) => `<label class="fb-o"><input type="radio" name="c-${esc(pid)}" value="${k}" data-c="${esc(pid)}"${cur === k ? ' checked' : ''}> ${esc(v)}</label>`).join('')}</div>
<label class="lbl" for="note-${esc(pid)}">備註（想修改哪裡、喜歡哪裡；會一起複製）<span class="oldnote" data-oldnote="${esc(pid)}"></span></label>
<textarea id="note-${esc(pid)}" data-note="${esc(pid)}" rows="2" maxlength="2000" placeholder="例：衣服想換成白色；背景想要海邊">${esc(q.note)}</textarea>
${oldNotes(pid).length ? `<p class="oldfb">舊版備註（保留）：${esc(oldNotes(pid).map(x => `${VER_ZH(x.v)}「${oneLine(x.note)}」`).join('；'))}</p>` : ''}
<button type="button" class="btn ghost small" data-clear="${esc(pid)}">清除這位的新版回饋</button>
</fieldset></section>`;
  }

  function compSec() {
    const C = P.composition;
    return `<section class="sec" id="comp"><h2>四、橫直構圖（R1 修訂）</h2>
<p class="lead"><b>建議：${esc(C.recommend)}。</b></p>${ul(C.why)}
<p class="note"><b>另一種做法：</b>${esc(C.alt)}</p>
<h3>換算與檢查</h3>${ul(C.checks)}
<p class="note">每位的景別、人物佔比、頭頂與手腳範圍、留白位置與焦段距離，寫在各位卡片的「取景設計」。</p>
<details class="info"><summary>拆開來看：構圖需求、模型輸出、版面適配、出血線圈、廠商未知</summary>
${tbl(['層次', '說明'], C.layers.map(x => [x.k, x.v]))}</details></section>`;
  }

  function costSec() {
    const E = P.execution, M = E.model, K = E.cost;
    return `<section class="sec" id="cost"><h2>五、試拍與費用（R1 查證）</h2>
<p class="callout warn"><b>生成仍暫停。</b>${esc(K.status)} ${esc(K.gate)}</p>
<p class="note"><b>Penny 可以先決定拍攝方向，費用另外核定。</b>本頁沒有任何要你核准花費的選項。</p>
<h3>撤回的數字</h3>${ul(K.withdrawn)}
<h3>改成分階段（提案）</h3>
${tbl(['項目', '內容'], K.phases.map(x => [x.k, x.v]))}
<p class="note"><b>為什麼第一階段是 Iris：</b></p>${ul(K.why_iris)}
<details class="info"><summary>費用查證明細：歷史實扣、今天的工具報價、計價方式與異常</summary>
<h4>歷史實際扣款</h4>${tbl(['項目', '數值', '依據', '等級'], K.history.map(x => [x.k, x.v, x.basis, x.level]))}
<h4>今天的工具報價（預檢，不送出工作）</h4>${tbl(['設定', '回傳'], K.quote.map(x => [x.cfg, x.r]))}
<p class="note">${esc(K.quote_note)}</p>
<h4>計價方式、張數、上限、異常</h4>${tbl(['項目', '說明'], K.facts.map(x => [x.k, x.v]))}
</details>
<details class="info"><summary>模型、Soul 狀態與已知限制</summary>
<p class="note"><b>怎麼拍：</b>${esc(M.recommend)}</p>
${ul(M.why)}
${tbl(['人設', 'Soul 狀態（紀錄）'], M.soul_status.map(x => [x.who, x.status]))}
<p class="note">Soul ID 不列在公開頁。</p>
${ul(M.known_limits)}
<p class="note"><b>多階段：</b>${esc(M.multi_stage)}</p>
<p class="note"><b>未知：</b>${esc(M.unknown.join('、'))}</p></details></section>`;
  }

  function oldQLines() {
    return oldQ().map(x => `${(x.v === CUR ? QS : QS_OLD)[x.k] ? (x.v === CUR ? QS : QS_OLD)[x.k].label : x.k}：${VER_ZH(x.v)} 選了「${qLabel(x.k, x.a, x.v)}」`);
  }
  function outSec() {
    const oq = oldQLines();
    return `<section class="sec" id="out"><h2>六、回饋與複製</h2>
<div class="callout">回饋只存在這個瀏覽器（localStorage），<b>不會送到伺服器</b>，也不會通知主管。可以只回覆一部分就複製；沒回覆新版的會寫「未回覆新版」。複製後請貼回 ChatGPT。<br>這是對拍攝方向的回饋，<b>不是</b>生成授權或費用核准，也不是照片、月份、版面或印刷核准。</div>
<h3>想請 Penny 決定的事</h3>
<ol class="facts">${P.questions.map(x => `<li>${esc(x)}</li>`).join('')}</ol>
<p class="note">第 1 題在各位卡片上選（Somi 若想回到炸雞拍法、Miu 若想回到咖啡師拍法，選「改用替代方向」）。第 2、3 題在下面選：</p>
${Object.entries(QS).map(([k, Q]) => `<fieldset class="fb"><legend>${esc(Q.label)}（新版）</legend><div class="fb-opts col">${Object.entries(Q.opts).map(([v, t]) =>
      `<label class="fb-o"><input type="radio" name="q-${k}" value="${v}" data-q="${k}"${S.q[k] === v && S.qv[k] === CUR ? ' checked' : ''}> ${esc(t)}</label>`).join('')}</div></fieldset>`).join('')}
${oq.length ? `<p class="oldfb">舊版題目的回答（保留，不算新版）：${esc(oq.join('；'))}</p>` : ''}
<label class="lbl" for="gnote">整體備註（自由文字）<span class="oldnote" id="gnote-old"></span></label>
<textarea id="gnote" rows="3" maxlength="3000" placeholder="例：整體想要更多戶外；某位的方向想整個換掉">${esc(S.gnote)}</textarea>
${S.gprev.length ? `<p class="oldfb">舊版整體備註（保留）：${esc(S.gprev.map(x => `${VER_ZH(x.v)}「${oneLine(str(x.note))}」`).join('；'))}</p>` : ''}
<div class="actions"><button type="button" class="btn" id="act-copy">複製回饋</button><button type="button" class="btn danger" id="act-reset">清除本頁全部回饋</button></div>
<label class="lbl" for="out-text">將複製的文字（預覽）</label><textarea id="out-text" rows="16" readonly></textarea>
</section>
<section class="sec" id="refs"><h2>其他頁面</h2><ul class="facts">
<li><a href="index.html">第二階段：為入選人設挑照片</a>：素材選擇照舊保留在那一頁，本頁不讀也不改。</li>
<li>完整企劃文件：repo 的 <code>docs/calendar/CAL_18_M3_SHOOT_PLAN.md</code>（企劃資料 <code>${esc(P.plan_file)}</code>）。</li></ul></section>`;
  }

  function render() {
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    $('#planver').textContent = `${P.version}（${P.round} 修訂，${P.written_on}）`;
    app.innerHTML = revSec() + aaliyaSec() + ownerSec() +
      `<section class="sec" id="people"><h2>三、12 位企劃（R1 修訂）</h2>
<ul class="facts"><li>每位一個主推薦、一個替代方向。順序是名單順序，不是月份。</li>
<li>每張只拍一位、只有一個主要姿態；全部維持成人樣貌，不做任何降齡呈現。</li>
<li>灰色框是「尚未生成」的新照片位置；旁邊的照片是她<b>既有</b>的照片，只用來認人。</li></ul>
${overview()}
<details class="info"><summary>12 位差異總表與仍然接近的地方</summary>${diffTable()}
<p class="note"><b>仍然接近、需要 Penny 判斷（不宣稱已消除）：</b></p>${ul(P.overlap)}</details>
</section>` + PEOPLE.map(plan).join('') + compSec() + costSec() + outSec();
    PEOPLE.forEach(p => refresh(p.pid));
    refreshOut();
  }

  function refresh(pid) {
    const c = curChoice(pid);
    const olds = oldChoices(pid);
    const t = c ? CH[c] : (olds.length ? '未回覆新版（有舊版回饋）' : '未回覆新版');
    const el = $(`[data-st="${pid}"]`);
    if (el) { el.textContent = t; el.className = `st ${c ? 'conf' : (olds.length ? 'draft' : 'none')}`; }
    const ov = $(`[data-ov="${pid}"]`);
    if (ov) ov.textContent = `回饋：${t}`;
    const on = $(`[data-oldnote="${pid}"]`);
    const q = S.p[pid];
    if (on) on.textContent = q.note.trim() && q.nv !== CUR ? `（這段寫於${VER_ZH(q.nv)}）` : '';
  }
  function buildText() {
    const L = ['TASK-CAL-001／M-3／R1｜專業寫真企劃修訂與費用查證｜Penny 企劃回饋',
      `企劃版本：${P.version}（${P.round} 修訂）｜頁面版本：${PAGE_COMMIT || '本機預覽（未部署）'}`,
      '說明：這是對拍攝方向的回饋，不是生成授權，也不是費用核准；不代表照片、月份、版面或印刷核准。', '', '【12 位企劃（新版 v2）】'];
    let n = 0;
    PEOPLE.forEach((p, i) => {
      const c = curChoice(p.pid);
      const olds = oldChoices(p.pid);
      const q = S.p[p.pid];
      if (c) n++;
      const oldTxt = olds.length ? `（舊版回饋：${olds.map(x => `${VER_ZH(x.v)}「${CH[x.c] || x.c}」`).join('、')}；企劃已修訂，不算新版回覆）` : '';
      L.push(`${i + 1}. ${nm(p.pid)}（${p.pid}）｜${p.title}：${c ? CH[c] : '未回覆新版'}${c ? '' : oldTxt}`);
      if (c && olds.length) L.push(`   舊版回饋（參考）：${olds.map(x => `${VER_ZH(x.v)}「${CH[x.c] || x.c}」`).join('、')}`);
      if (q.note.trim()) L.push(`   備註${q.nv !== CUR ? `（寫於${VER_ZH(q.nv)}）` : ''}：${oneLine(q.note)}`);
      oldNotes(p.pid).forEach(x => L.push(`   舊版備註（${VER_ZH(x.v)}）：${oneLine(x.note)}`));
    });
    L.push(`（新版已回覆 ${n}／${PEOPLE.length} 位）`, '');
    Object.entries(QS).forEach(([k, Q]) => L.push(`【${Q.label}】${S.q[k] && S.qv[k] === CUR ? Q.opts[S.q[k]] : '未回覆新版'}`));
    oldQLines().forEach(x => L.push(`【舊版題目，不算新版】${x}`));
    L.push(`【整體備註】${S.gnote.trim() ? `${S.gnv !== CUR ? `（寫於${VER_ZH(S.gnv)}）` : ''}${oneLine(S.gnote)}` : '（無）'}`);
    S.gprev.forEach(x => L.push(`【舊版整體備註】（${VER_ZH(x.v)}）${oneLine(str(x.note))}`));
    return L.join('\n');
  }
  function refreshOut() {
    const n = PEOPLE.filter(p => curChoice(p.pid)).length;
    $('#bar-count').textContent = `新版已回覆 ${n}／${PEOPLE.length} 位｜尚未生成任何照片`;
    const g = $('#gnote-old');
    if (g) g.textContent = S.gnote.trim() && S.gnv !== CUR ? `（這段寫於${VER_ZH(S.gnv)}）` : '';
    const ta = $('#out-text');
    if (ta) ta.value = buildText();
  }

  // ---------- 事件 ----------
  app.addEventListener('change', e => {
    const t = e.target;
    if (t.dataset.c) { setChoice(t.dataset.c, t.value); save(); refresh(t.dataset.c); refreshOut(); }
    else if (t.dataset.q) { setQ(t.dataset.q, t.value); save(); refreshOut(); }
  });
  app.addEventListener('input', e => {
    const t = e.target;
    if (t.dataset.note) { setNote(t.dataset.note, t.value); save(); refresh(t.dataset.note); refreshOut(); }
    else if (t.id === 'gnote') { setG(t.value); save(); refreshOut(); }
  });
  app.addEventListener('click', e => {
    const z = e.target.closest('.zoom');
    if (z) { openViewer(z); return; }
    const cl = e.target.closest('[data-clear]');
    if (cl) {
      const pid = cl.dataset.clear;
      const q = S.p[pid];
      if (curChoice(pid)) { q.c = ''; q.v = ''; }
      if (q.nv === CUR) { q.note = ''; q.nv = ''; }
      save();
      $$(`input[name="c-${pid}"]`).forEach(r => { r.checked = false; });
      $(`#note-${pid}`).value = q.note;
      refresh(pid); refreshOut();
      toast(`已清除 ${nm(pid)} 的新版回饋（舊版回饋保留）。`);
      return;
    }
    if (e.target.id === 'act-copy') copyOut();
    if (e.target.id === 'act-reset') {
      if (!window.confirm('清除本頁全部回饋？舊版的回饋也會一起刪除。（只清本頁；第二階段素材選擇不受影響）')) return;
      S = blank();
      try { localStorage.removeItem(KEY); } catch (e2) { /* 只清記憶體 */ }
      render();
      toast('已清除本頁回饋。');
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
