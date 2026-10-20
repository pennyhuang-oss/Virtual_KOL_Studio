// 2027 KOL 桌曆｜第二階段：為 Penny 已確認的 12 位挑照片。選擇只存在本機瀏覽器 localStorage，不送到伺服器；沒有追蹤或分析。
// 名單來自 owner 決定紀錄（data.js 的 mat.roster，產生自 data/cal_m1_owner_roster.json），不看瀏覽器裡的選角草稿。
// 第一階段選角（cast.html）與舊版決策頁（plan.html）的瀏覽器資料只讀來顯示提示，從不寫入、轉換或刪除。
'use strict';
(() => {
  const D = window.CAL_DATA;
  const app = document.getElementById('app');
  if (!D || !D.mat) { app.textContent = '資料載入失敗。'; return; }

  const SHA = D.fixed_sha;
  const KEY = 'cal2027-materials-v1:' + SHA;
  const CAST_KEY = 'cal2027-casting-v1:' + SHA;
  const OLD_KEY = 'cal2027-decision-v1:' + SHA;
  const IMG = D.images;
  const M = D.mat;
  const R = M.roster;
  const PEOPLE = M.people;
  const BYP = {};
  const ITEM = {};
  PEOPLE.forEach(p => { BYP[p.pid] = p; p.items.forEach((it, i) => { ITEM[it.id] = { ...it, pid: p.pid, n: i }; }); });
  const CAND = {};
  D.cast.candidates.forEach(c => { CAND[c.id] = c; });
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const fullName = p => p.native ? `${p.name} ${p.native}` : p.name;
  const first = pid => (CAND[pid] ? CAND[pid].name : pid).split(' ')[0];
  const when = iso => new Date(iso).toLocaleString('zh-TW', { hour12: false });

  // ---------- 狀態 ----------
  // p[pid]：H＝橫式主照片 ID、V＝直式主照片 ID（可同一張）、B＝備選 ID（不含 H、V）、note＝備註（不屬於確認項目）。
  // conf[pid]：{ v, at }。這位的 H／V／B 有任何更動就刪掉（即使改回原樣），要重新確認。
  const blankP = () => ({ H: '', V: '', B: [], note: '' });
  const blank = () => ({ p: Object.fromEntries(PEOPLE.map(p => [p.pid, blankP()])), conf: {}, gnote: '' });
  const own = (pid, id) => !!(id && ITEM[id] && ITEM[id].pid === pid);
  const byOrder = ids => [...new Set(ids)].sort((a, b) => ITEM[a].n - ITEM[b].n);
  let storageOK = true;
  function load() {
    const S0 = blank();
    try {
      const s = JSON.parse(localStorage.getItem(KEY));
      if (!s || typeof s !== 'object') return S0;
      PEOPLE.forEach(({ pid }) => {
        const q = (s.p || {})[pid] || {};
        const H = own(pid, q.H) ? q.H : '';
        const V = own(pid, q.V) ? q.V : '';
        const B = byOrder((Array.isArray(q.B) ? q.B : []).filter(id => own(pid, id) && id !== H && id !== V));
        S0.p[pid] = { H, V, B, note: typeof q.note === 'string' ? q.note : '' };
        const c = (s.conf || {})[pid];
        if (c && typeof c.v === 'string' && typeof c.at === 'string') S0.conf[pid] = { v: c.v, at: c.at };
      });
      S0.gnote = typeof s.gnote === 'string' ? s.gnote : '';
    } catch (e) { storageOK = false; }
    return S0;
  }
  let S = load();
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(S)); storageOK = true; } catch (e) {
      if (storageOK) toast('這個瀏覽器不允許儲存（例如無痕模式）：重新整理後選擇會消失。');
      storageOK = false;
    }
  }
  const cur = pid => { const q = S.p[pid]; return JSON.stringify({ H: q.H, V: q.V, B: q.B }); };
  const answered = pid => { const q = S.p[pid]; return !!(q.H || q.V || q.B.length); };
  function status(pid) {
    if (!answered(pid)) return 'none';
    const c = S.conf[pid];
    return c && c.v === cur(pid) ? 'conf' : 'draft';
  }
  const ST = { none: '未選', draft: '草稿・待 Penny 確認', conf: 'Penny 已確認目前選擇' };
  const ST_SHORT = { none: '未選', draft: '草稿', conf: '已確認' };
  const LEVEL_ZH = { fix: '待修', clean_opt: '構圖注意（可選清理）', note: '注意' };
  const SCALE_NOTE = '照片選擇意向；若採用此尺度，交印前需確認廠商接受範圍。選這張不代表整本尺度已決定。';
  function change(pid, fn) {
    fn(S.p[pid]);
    const q = S.p[pid];
    q.B = byOrder(q.B.filter(id => id !== q.H && id !== q.V));
    delete S.conf[pid];
    save();
    refreshPerson(pid);
    refreshSummary();
  }

  // ---------- 舊資料（只讀） ----------
  function legacyNote() {
    const out = [];
    try {
      const c = JSON.parse(localStorage.getItem(CAST_KEY));
      if (c && Array.isArray(c.sel) && c.sel.length) {
        const same = JSON.stringify([...c.sel].sort()) === JSON.stringify([...R.list].sort());
        const conf = c.conf && c.conf.list === JSON.stringify(c.sel);
        out.push(`這個瀏覽器有第一階段選角資料（${c.sel.length} 位，${conf ? '當時按過確認' : '草稿'}），與 Penny 已確認的名單<b>${same ? '相同' : '不同'}</b>。名單一律以紀錄為準；那份資料保留在<a href="cast.html">選角頁</a>，不會被刪除或改寫，也<b>不算</b>照片核准。`);
      }
    } catch (e) { /* 忽略 */ }
    try {
      const o = JSON.parse(localStorage.getItem(OLD_KEY));
      if (o && o.v && Object.keys(o.v).length) out.push(`另有舊版決策頁的紀錄（${Object.keys(o.v).length} 項），保留在<a href="plan.html">原推薦方案參考</a>頁；舊的照片選擇<b>不會</b>帶進這裡。`);
    } catch (e) { /* 忽略 */ }
    return out.length ? `<div class="callout">${out.map(t => `<p class="note">${t}</p>`).join('')}</div>` : '';
  }

  // ---------- 畫面元件 ----------
  function capOf(it) {
    const p = BYP[it.pid];
    return `${p.name}｜${it.id}｜${it.label}`;
  }
  function fig(iid, cap, cls) {
    const m = IMG[iid];
    if (!m) return '';
    const hi = m.res === 'hires';
    return `<figure class="fig${cls ? ' ' + cls : ''}"><button type="button" class="zoom" data-img="${esc(iid)}" data-cap="${esc(cap)}" aria-label="放大：${esc(cap)}">` +
      `<img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" loading="lazy" decoding="async" alt="${esc(cap)}">` +
      `<span class="resb ${hi ? 'hires' : 'lowres'}">${hi ? '高解析預覽' : '低解析'}</span><span class="zi" aria-hidden="true">放大</span></button></figure>`;
  }
  function tags(it) {
    const t = [];
    if (it.clean_of) t.push('<span class="tag t-clean">R3 局部清理版</span>');
    else t.push('<span class="tag t-orig">原圖・未修圖</span>');
    if (it.kind === 'thumb') t.push('<span class="tag t-low">低解析縮圖</span>');
    if (it.scale) t.push(`<span class="tag t-scale">${it.scale === 'swim' ? '泳裝' : '內衣'}</span>`);
    if (it.r3) t.push(`<span class="tag t-r3" title="${esc(it.r3)}">R3 舊推薦（參考）</span>`);
    return t.join(' ');
  }
  function card(it) {
    const [w, h] = it.orig_px;
    return `<article class="mc" id="m-${esc(it.id)}" data-mid="${esc(it.id)}">
${fig(it.img, capOf({ ...it, pid: ITEM[it.id].pid }))}
<p class="mc-id"><code>${esc(it.id)}</code> ${tags(it)}</p>
<p class="mc-l">${esc(it.label)}</p>
<p class="mc-s">${esc(it.src_zh)}｜原圖 ${w}×${h} px</p>
${it.fix ? `<p class="mc-fix lv-${esc(it.clean_of ? 'clean' : (it.level || 'note'))}"><b>${it.clean_of ? '清理狀態' : LEVEL_ZH[it.level || 'note']}：</b>${esc(it.fix)}</p>` : '<p class="mc-ok">未見明顯瑕疵（檢查方式見下行）</p>'}
${it.scale ? `<p class="mc-scale">${SCALE_NOTE}</p>` : ''}
<p class="mc-c">${esc(it.check)}${it.r3 ? `｜${esc(it.r3)}` : ''}</p>
<div class="mc-act">
<button type="button" class="btn small" data-act="H" data-mid="${esc(it.id)}">選作橫式照片</button>
<button type="button" class="btn small" data-act="V" data-mid="${esc(it.id)}">選作直式照片</button>
<button type="button" class="btn small ghost" data-act="B" data-mid="${esc(it.id)}">列為備選</button>
</div></article>`;
  }
  const EXCL_ZH = { dup: '近似重複或重複檔', exposure: '疑似裸露、走光或無法確定遮蔽範圍', face: '臉與定案人設不符或非定案臉', pending: '暫不採用（待主管覆核判斷）', defect: '瑕疵或檔名標示失敗' };
  function pairLine(q) {
    const v = q.v != null ? ` ${q.v}` : '';
    const lead = q.kind === 'hit' ? '既有碰撞紀錄' : (q.kind === 'near' ? '接近門檻' : '相似度提示');
    return `${lead}：${first(q.a)} ↔ ${first(q.b)}${v}｜${q.text}`;
  }
  function person(p, i) {
    const main = p.items.filter(it => it.tier === 'main');
    const more = p.items.filter(it => it.tier === 'more');
    const swim = p.items.filter(it => it.tier === 'swim');
    const pairs = M.pairs.filter(q => q.a === p.pid || q.b === p.pid);
    const ex = Object.entries(p.excluded);
    const nEx = ex.reduce((a, [, n]) => a + n, 0);
    const unmeasured = M.unmeasured.includes(p.pid);
    return `<section class="sec person" id="p-${esc(p.pid)}" data-pid="${esc(p.pid)}">
<div class="ph"><div class="ph-face">${fig(p.face, `${fullName(p)}｜辨識用正臉（不是素材）`, 'face')}</div>
<div class="ph-t"><h2>${i + 1}. ${esc(p.name)}${p.native ? ` <span class="nat">${esc(p.native)}</span>` : ''}</h2>
<p class="cc-meta"><code>${esc(p.pid)}</code>｜${esc(p.desc)}</p>
<div class="pline" data-line="${esc(p.pid)}"></div>
<button type="button" class="btn ghost small" data-act="clear" data-pid="${esc(p.pid)}">清除這位的選擇</button></div></div>
<h3>主要候選（${main.length} 張）</h3>
${main.length < 6 ? `<p class="note">這位可用的既有照片不足 6 張，如實列出。</p>` : ''}
<div class="mgrid">${main.map(card).join('')}</div>
${swim.length ? `<details class="more swim"><summary>泳裝／內衣素材參考（${swim.length} 張）</summary><p class="note">有差異的代表圖，可以選作橫式、直式或備選。${SCALE_NOTE}同類的其他照片放在「更多素材」。</p><div class="mgrid">${swim.map(card).join('')}</div></details>` : ''}
${more.length ? `<details class="more"><summary>更多素材（${more.length} 張）</summary><p class="note">其他合格的既有照片：多半是同一套造型的其他角度、人物較小或有較多待修處。</p><div class="mgrid">${more.map(card).join('')}</div></details>` : ''}
<details class="info"><summary>素材說明：缺口、未列出的照片、相似度</summary>
<ul class="facts">
${p.gaps.length ? p.gaps.map(g => `<li class="gap">缺口：${esc(g)}；本輪不取回、不生成。</li>`).join('') : '<li>列出的照片都有可核對的原圖（或 R3 清理輸出）；預覽是原圖等比縮小。</li>'}
<li>未列出 ${nEx} 張${nEx ? `：${ex.map(([k, n]) => `${EXCL_ZH[k]} ${n}`).join('、')}` : ''}。逐張理由記錄在 repo 的素材清單，不放上公開頁。</li>
${pairs.length ? pairs.map(q => `<li class="k-${esc(q.kind)}">${esc(pairLine(q))}（記錄，不否決名單）</li>`).join('') : ''}
${unmeasured ? '<li>這位沒有既有遮髮量測；沒有紀錄不等於不像。</li>' : ''}
</ul></details>
<label class="lbl" for="note-${esc(p.pid)}">這位的備註（自由文字，會一起複製；不屬於確認項目）</label>
<textarea id="note-${esc(p.pid)}" data-note="${esc(p.pid)}" rows="2" maxlength="2000" placeholder="例：橫式想要再亮一點；這張的路人要修">${esc(S.p[p.pid].note)}</textarea>
</section>`;
  }
  function rosterCard(p) {
    const m = IMG[p.face];
    return `<a class="rs" href="#p-${esc(p.pid)}" data-rs="${esc(p.pid)}"><img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" alt="" loading="lazy" decoding="async">` +
      `<span class="rs-t"><b>${esc(p.name)}</b><span class="rs-p" data-prog="${esc(p.pid)}"></span></span></a>`;
  }

  // ---------- 版面 ----------
  function render() {
    $('#sha').textContent = SHA;
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    $('#rosterver').textContent = `${R.version}（${R.decided_on}，Penny 在對話中確認）`;
    const v = R.vs_original_recommendation;
    app.innerHTML = `
<section class="sec quick" id="roster"><h2>Penny 已確認的 12 位 <span class="st conf">名單已確認（${esc(R.version)}）</span></h2>
<p class="note">名單依 owner 決定紀錄（<code>${esc(M.roster_file)}</code>、<code>docs/calendar/CAL_17_OWNER_ROSTER_DECISION.md</code>），<b>不是</b>依這個瀏覽器的資料。${esc(R.order_note)}。名單確認只代表人選，<b>不是</b>照片、月份、版面或印刷核准。相對主管原推薦：移除 ${esc(v.removed.map(first).join('、'))}；加入 ${esc(v.added.map(first).join('、'))}。</p>
${legacyNote()}
<div class="rs-grid">${PEOPLE.map(rosterCard).join('')}</div>
<details class="info"><summary>既有相似度疑慮（記錄，不否決名單）</summary><ul class="facts">${M.pairs.map(q => `<li class="k-${esc(q.kind)}">${esc(pairLine(q))}</li>`).join('')}
<li>沒有既有遮髮量測：${esc(M.unmeasured.map(first).join('、'))}。沒有紀錄不等於不像。</li>
<li>不換人、不改人設、不重新訓練。</li></ul></details>
<p class="note" id="sum-line"></p>
<div class="actions"><button type="button" class="btn" id="act-confirm">確認目前已選素材</button><a class="btn ghost" href="#out">看複製內容</a></div>
</section>
<section class="sec" id="people"><h2>逐位挑照片</h2>
<ul class="facts">
<li>每位最多一張「橫式照片」、一張「直式照片」，<b>可以是同一張</b>；喜歡的其他照片可以「列為備選」（不限張數）。再按一次同一個按鈕就取消。</li>
<li>每張照片有固定的素材 ID（例 <code>iris-01</code>），複製結果時用這個 ID。</li>
<li>綠色「高解析預覽」是可核對原圖的等比縮小；橘色「低解析」是 360×480 縮圖，原圖沒有取回（列為缺口）。點照片可放大，再點一下看原尺寸。</li>
<li>「R3 局部清理版」與原圖分開列，各有自己的 ID；目前<b>沒有</b>任何正式修圖版。「R3 舊推薦」只是舊方案的參考，<b>不是</b> Penny 的選擇。</li>
<li>照片能否滿版、裁切後解析度夠不夠，要排版時才判斷；這裡不下結論。選中的主照片取得原圖後，才做實際裁切與細節覆核。</li>
<li>標示分三種：「待修」是假字、可辨識角色等需要處理的地方；「構圖注意（可選清理）」是背景路人、牆上本人照片、雜物等，可以保留也可以清理；「注意」是其他提醒。</li>
<li>部分人有「泳裝／內衣素材參考」：可以照常選。這是照片選擇意向，若採用此尺度，交印前需確認廠商接受範圍；選單張照片不代表整本尺度已決定。</li>
</ul></section>
${PEOPLE.map(person).join('')}
<section class="sec" id="out"><h2>確認與複製</h2>
<div class="callout">選擇只存在這個瀏覽器（localStorage），<b>不會送到伺服器</b>。可以只選一部分就複製；未選的人會寫「未選」，<b>不算核准</b>。複製後請貼回 ChatGPT；本頁不會通知主管。</div>
<label class="lbl" for="gnote">整體補充意見（自由文字，不屬於確認項目）</label>
<textarea id="gnote" rows="3" maxlength="3000" placeholder="例：整體想要更多戶外照；某位的照片都不夠好">${esc(S.gnote)}</textarea>
<div class="actions"><button type="button" class="btn" id="act-confirm2">確認目前已選素材</button><button type="button" class="btn" id="act-copy">複製素材選擇</button><button type="button" class="btn danger" id="act-reset">重設全部素材選擇</button></div>
<label class="lbl" for="out-text">將複製的文字（預覽）</label><textarea id="out-text" rows="16" readonly></textarea>
</section>
<section class="sec" id="refs"><h2>參考頁</h2>
<ul class="facts"><li><a href="shoot.html">V-Iris 首試檢視</a>：目前要看的首試照片與回饋；<a href="history.html">已定稿企劃／歷史紀錄</a>：12 位 24 套拍攝企劃（已定稿）。兩頁都不影響這頁的素材選擇。</li>
<li><a href="cast.html">第一階段選角</a>：保留作參考；那裡的草稿狀態不影響已確認的名單。</li>
<li><a href="plan.html">原推薦方案參考</a>：R3 的月份樣張與裁切（舊推薦、舊月份）只供參考，<b>不限制</b>這裡的選擇。</li></ul></section>`;
    PEOPLE.forEach(p => refreshPerson(p.pid, true));
    refreshSummary();
  }
  function idLabel(id) {
    const it = ITEM[id];
    return `${id}（${it.label}${it.kind === 'thumb' ? '；360×480 縮圖，原圖未取回' : ''}${it.scale ? '；泳裝／內衣' : ''}）`;
  }
  function refreshPerson(pid, quiet) {
    const q = S.p[pid];
    const st = status(pid);
    const line = $(`[data-line="${pid}"]`);
    const c = S.conf[pid];
    line.innerHTML = `<p class="pl"><b>橫式：</b>${q.H ? `<a href="#m-${esc(q.H)}">${esc(q.H)}</a>` : '<span class="un">未選</span>'}　<b>直式：</b>${q.V ? `<a href="#m-${esc(q.V)}">${esc(q.V)}</a>` : '<span class="un">未選</span>'}${q.H && q.H === q.V ? '（同一張）' : ''}　<b>備選：</b>${q.B.length ? q.B.map(id => `<a href="#m-${esc(id)}">${esc(id)}</a>`).join('、') : '無'}</p>` +
      `<p class="pl"><span class="st ${st}">${ST[st]}</span>${st === 'conf' ? ` <span class="note">${esc(when(c.at))}；之後再改任何一張都會回到草稿</span>` : ''}</p>`;
    $$(`#p-${CSS.escape(pid)} .mc`).forEach(el => {
      const id = el.dataset.mid;
      const isH = q.H === id, isV = q.V === id, isB = q.B.includes(id);
      el.classList.toggle('on-h', isH);
      el.classList.toggle('on-v', isV);
      el.classList.toggle('on-b', isB);
      const bh = el.querySelector('[data-act="H"]'), bv = el.querySelector('[data-act="V"]'), bb = el.querySelector('[data-act="B"]');
      bh.textContent = isH ? '✓ 橫式照片（再按取消）' : '選作橫式照片';
      bv.textContent = isV ? '✓ 直式照片（再按取消）' : '選作直式照片';
      bh.classList.toggle('ghost', !isH); bh.setAttribute('aria-pressed', isH);
      bv.classList.toggle('ghost', !isV); bv.setAttribute('aria-pressed', isV);
      bb.disabled = isH || isV;
      bb.textContent = isH || isV ? '已選作主照片' : (isB ? '✓ 備選（再按取消）' : '列為備選');
      bb.classList.toggle('ghost', !isB); bb.setAttribute('aria-pressed', isB);
    });
    const prog = $(`[data-prog="${pid}"]`);
    if (prog) prog.innerHTML = `橫${q.H ? '✓' : '—'} 直${q.V ? '✓' : '—'} 備${q.B.length}<br><span class="st ${st}">${ST_SHORT[st]}</span>`;
    if (!quiet) $('#out-text').value = buildText();
  }
  function counts() {
    let h = 0, v = 0, conf = 0, draft = 0;
    PEOPLE.forEach(({ pid }) => { const q = S.p[pid]; if (q.H) h++; if (q.V) v++; const st = status(pid); if (st === 'conf') conf++; if (st === 'draft') draft++; });
    return { h, v, conf, draft };
  }
  function refreshSummary() {
    const k = counts();
    $('#sum-line').textContent = `進度：橫式已選 ${k.h}／12、直式已選 ${k.v}／12；已確認 ${k.conf} 位、草稿 ${k.draft} 位、未選 ${12 - k.conf - k.draft} 位。`;
    $('#bar-count').textContent = `橫 ${k.h}・直 ${k.v}／12｜已確認 ${k.conf} 位`;
    const can = k.draft > 0;
    ['#act-confirm', '#act-confirm2'].forEach(s => { $(s).disabled = !can; });
    $('#out-text').value = buildText();
  }

  // ---------- 輸出文字 ----------
  function buildText() {
    const k = counts();
    const t = [];
    t.push('【2027 KOL 桌曆｜第二階段素材選擇】（由決策頁產生；請貼回 ChatGPT）');
    t.push(`Owner 名單版本：${R.version}（${R.decided_on}，Penny 在對話中確認；紀錄 ${M.roster_file}）`);
    t.push(`素材基準 SHA：${SHA}`);
    t.push(`素材清單：${M.materials_file}（git blob ${M.materials_blob}）`);
    t.push(`頁面版本：${PAGE_COMMIT || '未知（本機預覽）'}`);
    t.push(`產生時間：${when(new Date().toISOString())}（瀏覽器時間）`);
    t.push(`進度：橫式已選 ${k.h}／12、直式已選 ${k.v}／12；已確認 ${k.conf} 位、草稿 ${k.draft} 位、未選 ${12 - k.conf - k.draft} 位`);
    t.push('');
    PEOPLE.forEach((p, i) => {
      const q = S.p[p.pid];
      const st = status(p.pid);
      t.push(`${i + 1}. ${fullName(p)}（${p.pid}）`);
      t.push(`　橫式：${q.H ? idLabel(q.H) : '未選'}`);
      t.push(`　直式：${q.V ? idLabel(q.V) : '未選'}${q.H && q.H === q.V ? '（與橫式同一張）' : ''}`);
      t.push(`　備選：${q.B.length ? q.B.join('、') : '無'}`);
      t.push(`　狀態：${st === 'conf' ? `Penny 已確認目前選擇（${when(S.conf[p.pid].at)}）` : (st === 'draft' ? '草稿・待 Penny 確認' : '未選（不算核准）')}`);
      t.push(`　備註：${(q.note || '').trim() || '（無）'}`);
    });
    t.push('');
    t.push('整體補充意見（自由文字，不屬於確認項目）：' + ((S.gnote || '').trim() || '（無）'));
    t.push('');
    const scaled = PEOPLE.some(({ pid }) => { const q = S.p[pid]; return [q.H, q.V, ...q.B].some(id => id && ITEM[id].scale); });
    if (scaled) t.push('※ 已選照片中有泳裝／內衣：這是照片選擇意向，不代表整本尺度已決定；若採用此尺度，交印前需確認廠商接受範圍。');
    t.push('※ 月份、版面、修圖與印刷可用性都還沒決定；照片能否滿版要排版後才知道。品牌、Logo、QR 本輪不需要。');
    t.push('※ 這是 Penny 的素材選擇草稿／確認紀錄，不是主管核准，也不是印刷或廠商核准。名單確認不等於照片核准。');
    return t.join('\n');
  }

  // ---------- 事件 ----------
  app.addEventListener('click', e => {
    const z = e.target.closest('.zoom');
    if (z) { openViewer(z); return; }
    const b = e.target.closest('button');
    if (!b) return;
    const act = b.dataset.act;
    if (act === 'H' || act === 'V' || act === 'B') {
      const id = b.dataset.mid;
      const pid = ITEM[id].pid;
      change(pid, q => {
        if (act === 'B') q.B = q.B.includes(id) ? q.B.filter(x => x !== id) : [...q.B, id];
        else q[act] = q[act] === id ? '' : id;
      });
      return;
    }
    if (act === 'clear') {
      const pid = b.dataset.pid;
      if (!answered(pid)) { toast('這位還沒有選照片。'); return; }
      if (!window.confirm(`清除 ${BYP[pid].name} 的橫式、直式與備選？（備註保留）`)) return;
      change(pid, q => { q.H = ''; q.V = ''; q.B = []; });
      return;
    }
    if (b.id === 'act-confirm' || b.id === 'act-confirm2') openReview();
    if (b.id === 'act-copy') copyOut();
    if (b.id === 'act-reset') {
      if (!window.confirm('清除這個瀏覽器裡的全部素材選擇、確認紀錄與備註？（名單紀錄、第一階段選角與舊版決策資料都不受影響）')) return;
      try { localStorage.removeItem(KEY); } catch (e2) { /* 只清記憶體 */ }
      S = blank();
      render();
      toast('已重設全部素材選擇。');
    }
  });
  let saveTimer = null;
  app.addEventListener('input', e => {
    const el = e.target;
    if (el.dataset && el.dataset.note) S.p[el.dataset.note].note = el.value;
    else if (el.id === 'gnote') S.gnote = el.value;
    else return;
    clearTimeout(saveTimer);
    saveTimer = setTimeout(save, 300);
    $('#out-text').value = buildText();
  });
  $('#bar-copy').addEventListener('click', copyOut);

  // ---------- 確認視窗 ----------
  const review = $('#review');
  function mini(id, side) {
    const m = IMG[ITEM[id].img];
    return `<span class="rv-m"><img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" alt="" loading="lazy" decoding="async"><span>${side} ${esc(id)}</span></span>`;
  }
  function openReview() {
    const rows = PEOPLE.map((p, i) => {
      const q = S.p[p.pid];
      if (!answered(p.pid)) return `<div class="rv-row none"><b>${i + 1}. ${esc(p.name)}</b>：未選（不會被確認）</div>`;
      const imgs = [q.H ? mini(q.H, '橫') : '<span class="un">橫：未選</span>', q.V ? mini(q.V, '直') : '<span class="un">直：未選</span>'].join('');
      return `<div class="rv-row"><b>${i + 1}. ${esc(p.name)}</b> <span class="st ${status(p.pid)}">${ST[status(p.pid)]}</span><div class="rv-imgs">${imgs}</div><span class="note">備選：${q.B.length ? esc(q.B.join('、')) : '無'}</span></div>`;
    }).join('');
    $('#review-list').innerHTML = rows;
    review.hidden = false;
    document.documentElement.classList.add('noscroll');
    $('#review-ok').focus({ preventScroll: true });
  }
  function closeReview() { review.hidden = true; document.documentElement.classList.remove('noscroll'); }
  $('#review-ok').addEventListener('click', () => {
    const at = new Date().toISOString();
    let n = 0;
    PEOPLE.forEach(({ pid }) => { if (answered(pid) && status(pid) !== 'conf') { S.conf[pid] = { v: cur(pid), at }; n++; } });
    save();
    closeReview();
    PEOPLE.forEach(({ pid }) => refreshPerson(pid, true));
    refreshSummary();
    toast(n ? `已確認 ${n} 位的目前選擇。請按「複製」貼回 ChatGPT。` : '沒有需要確認的選擇。');
  });
  $('#review-cancel').addEventListener('click', closeReview);

  async function copyOut() {
    const text = buildText();
    const ta = $('#out-text');
    ta.value = text;
    const done = '已複製。請貼回 ChatGPT；本頁不會通知主管。';
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
    const mid = iid.startsWith('m_') ? iid.slice(2) : '';
    if (!mid) return '辨識用正臉（低解析），只用來認人，不是素材';
    const it = ITEM[mid];
    const [w, h] = it.orig_px;
    return `${it.src_zh}｜原圖 ${w}×${h} px｜${m.res === 'hires' ? `預覽 ${m.w}×${m.h} px（等比縮小）` : '低解析縮圖'}｜未排版，能否滿版或印刷尚未判斷`;
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
    if (review.hidden) document.documentElement.classList.remove('noscroll');
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
  document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    if (!viewer.hidden) closeViewer(false); else if (!review.hidden) closeReview();
  });

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
