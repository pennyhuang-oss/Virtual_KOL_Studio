// 2027 KOL 桌曆｜排版預覽頁（layout.html，M-5 R26 起）。資料來自 layout-data.js 與 cover-data.js（程式產生）。
// 依橫式／直式、月份看實際頁面（PDF 點陣化後的圖），可放大、開關參考線；橫式可切換「完整 16:9（推薦）」與「192×104 套框」比較。
// M-5 R27 起最上面是封面區（#cover）。M-5 R28：R27 四張 Owner 已全部退回（只展示、不再提供選擇；R27 的鍵 cal2027-cover-r27-v1 不讀、不寫、不刪）；
// 新增「單人身分測試，非完成封面」：前後切換、放大、備註（鍵 cal2027-cover-r28-v1，只存備註；沒有任何接受封面的選項）。
// M-5 R29：最上方改為「Coco 單人修正效果確認」：R28／R29 全圖前後、Coco 局部放大比較、兩個選項（單人修正效果可以／還要修改）與備註
// （鍵 cal2027-cover-r29-v1）；這只是單人效果確認，不是接受封面或授權其他角色。R28 測試與 R27 退回紀錄收合保留。
// R26 的排版回饋（鍵 cal2027-layout-r26-v1）原樣保留在頁面下方；其他鍵（選片、企劃、素材頁）不讀、不寫、不刪。
// 沒有追蹤或分析，回饋不會自動送出；未選不算接受。
'use strict';
(() => {
  const L = window.CAL_LAYOUT;
  const C = window.CAL_COVER && window.CAL_COVER.cards ? window.CAL_COVER : null;
  const app = document.getElementById('app');
  const $ = (s, r = document) => r.querySelector(s);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  if (!L || !L.pages || !L.pages.H || !L.pages.V) { app.textContent = '資料載入失敗。'; return; }
  const KEY = L.feedback_key;
  const BOOK_ZH = { H: '橫式', V: '直式' };
  const SVGNS = 'http://www.w3.org/2000/svg';

  // ---------- 回饋狀態 ----------
  const blank = () => ({ dec: {}, notes: {} });
  const load = () => {
    try {
      const v = JSON.parse(localStorage.getItem(KEY) || 'null');
      return v && typeof v === 'object' ? { dec: v.dec && typeof v.dec === 'object' ? v.dec : {}, notes: v.notes && typeof v.notes === 'object' ? v.notes : {} } : blank();
    } catch (e) { return blank(); }
  };
  let st = load();
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) { /* 無痕或停用儲存時只在本頁有效 */ } };
  // 單人身分測試的備註（另一個鍵，只有 notes）
  const TKEY = C && C.test ? C.test.feedback_key : '';
  const tload = () => {
    if (!TKEY) return { notes: {} };
    try {
      const v = JSON.parse(localStorage.getItem(TKEY) || 'null');
      return v && typeof v === 'object' && v.notes && typeof v.notes === 'object' ? { notes: v.notes } : { notes: {} };
    } catch (e) { return { notes: {} }; }
  };
  const tst = tload();
  const tsave = () => { try { localStorage.setItem(TKEY, JSON.stringify(tst)); } catch (e) { /* 同上 */ } };
  let ba = 'after';   // 前後切換：after＝R28 結果、before＝R27 原本
  // 單人修正效果確認（每輪一個新鍵，M-5 R30 起 cal2027-cover-r30-v1）：dec＝'ok'|'edit'、notes＝{coco}
  const FKEY = C && C.fix ? C.fix.feedback_key : '';
  const fload = () => {
    if (!FKEY) return { dec: '', notes: {} };
    try {
      const v = JSON.parse(localStorage.getItem(FKEY) || 'null');
      return v && typeof v === 'object' ? { dec: typeof v.dec === 'string' ? v.dec : '', notes: v.notes && typeof v.notes === 'object' ? v.notes : {} } : { dec: '', notes: {} };
    } catch (e) { return { dec: '', notes: {} }; }
  };
  const fst = fload();
  const fsave = () => { try { localStorage.setItem(FKEY, JSON.stringify(fst)); } catch (e) { /* 同上 */ } };
  let fba = 'after';   // 前後切換：after＝本輪目前結果、before＝R27 原圖
  // R29 當時的回饋（舊鍵，只讀不寫；本輪不繼承它的選擇）
  const F9KEY = C && C.fix29 ? C.fix29.feedback_key : '';
  const f9 = (() => {
    if (!F9KEY) return { dec: '', notes: {} };
    try {
      const v = JSON.parse(localStorage.getItem(F9KEY) || 'null');
      return v && typeof v === 'object' ? { dec: typeof v.dec === 'string' ? v.dec : '', notes: v.notes && typeof v.notes === 'object' ? v.notes : {} } : { dec: '', notes: {} };
    } catch (e) { return { dec: '', notes: {} }; }
  })();
  // R30 當時的回饋（只讀；M-5 R31 起人物封面停止，R30 收進歷史）
  const f30 = C && C.r31 && C.fix ? (() => {
    try {
      const v = JSON.parse(localStorage.getItem(C.fix.feedback_key) || 'null');
      return v && typeof v === 'object' ? { dec: typeof v.dec === 'string' ? v.dec : '', notes: v.notes && typeof v.notes === 'object' ? v.notes : {} } : { dec: '', notes: {} };
    } catch (e) { return { dec: '', notes: {} }; }
  })() : null;
  // M-5 R31 非人物封面選擇（新鍵 cal2027-cover-r31-v1）：dec＝{H,V}（'A'|'B'|'edit'）、notes＝{H,V,general}
  const QKEY = C && C.r31 ? C.r31.feedback_key : '';
  const qst = (() => {
    if (!QKEY) return { dec: {}, notes: {} };
    try {
      const v = JSON.parse(localStorage.getItem(QKEY) || 'null');
      const obj = x => (x && typeof x === 'object' && !Array.isArray(x) ? x : {});
      return v && typeof v === 'object' ? { dec: obj(v.dec), notes: obj(v.notes) } : { dec: {}, notes: {} };
    } catch (e) { return { dec: {}, notes: {} }; }
  })();
  const qsave = () => { try { localStorage.setItem(QKEY, JSON.stringify(qst)); } catch (e) { /* 同上 */ } };
  // M-5 R32 四季光影品牌版選擇（新鍵＝cal2027-cover-r32-＋圖片版本）：dec＝{H,V}（'1'|'2'|'edit'）、notes＝{H,V,general}
  const Q2KEY = C && C.r32 ? C.r32.feedback_key : '';
  const q2 = (() => {
    if (!Q2KEY) return { dec: {}, notes: {} };
    try {
      const v = JSON.parse(localStorage.getItem(Q2KEY) || 'null');
      const obj = x => (x && typeof x === 'object' && !Array.isArray(x) ? x : {});
      return v && typeof v === 'object' ? { dec: obj(v.dec), notes: obj(v.notes) } : { dec: {}, notes: {} };
    } catch (e) { return { dec: {}, notes: {} }; }
  })();
  const q2save = () => { try { localStorage.setItem(Q2KEY, JSON.stringify(q2)); } catch (e) { /* 同上 */ } };
  // M-5 R33 直式修正版確認（新鍵＝cal2027-cover-r33-＋修正版圖片版本）：dec＝'ok'|'edit'、notes＝{V}
  const Q3KEY = C && C.r33 ? C.r33.feedback_key : '';
  const q3 = (() => {
    if (!Q3KEY) return { dec: '', notes: {} };
    try {
      const v = JSON.parse(localStorage.getItem(Q3KEY) || 'null');
      return v && typeof v === 'object' ? { dec: typeof v.dec === 'string' ? v.dec : '', notes: v.notes && typeof v.notes === 'object' && !Array.isArray(v.notes) ? v.notes : {} } : { dec: '', notes: {} };
    } catch (e) { return { dec: '', notes: {} }; }
  })();
  const q3save = () => { try { localStorage.setItem(Q3KEY, JSON.stringify(q3)); } catch (e) { /* 同上 */ } };
  // M-5 R34 直式 Logo 圖示白／藍比較（新鍵＝cal2027-cover-r34-＋比較圖版本）：dec＝'A'|'B'|'edit'、notes＝{V}
  const Q4KEY = C && C.r34 ? C.r34.feedback_key : '';
  const q4 = (() => {
    if (!Q4KEY) return { dec: '', notes: {} };
    try {
      const v = JSON.parse(localStorage.getItem(Q4KEY) || 'null');
      return v && typeof v === 'object' ? { dec: typeof v.dec === 'string' ? v.dec : '', notes: v.notes && typeof v.notes === 'object' && !Array.isArray(v.notes) ? v.notes : {} } : { dec: '', notes: {} };
    } catch (e) { return { dec: '', notes: {} }; }
  })();
  const q4save = () => { try { localStorage.setItem(Q4KEY, JSON.stringify(q4)); } catch (e) { /* 同上 */ } };
  // M-5 R35 橫式年份光暈確認（新鍵＝cal2027-cover-r35-＋修正版圖片版本）：dec＝'glow'|'orig'|'edit'、notes＝{H}
  const Q5KEY = C && C.r35 ? C.r35.feedback_key : '';
  const q5 = (() => {
    if (!Q5KEY) return { dec: '', notes: {} };
    try {
      const v = JSON.parse(localStorage.getItem(Q5KEY) || 'null');
      return v && typeof v === 'object' ? { dec: typeof v.dec === 'string' ? v.dec : '', notes: v.notes && typeof v.notes === 'object' && !Array.isArray(v.notes) ? v.notes : {} } : { dec: '', notes: {} };
    } catch (e) { return { dec: '', notes: {} }; }
  })();
  const q5save = () => { try { localStorage.setItem(Q5KEY, JSON.stringify(q5)); } catch (e) { /* 同上 */ } };

  let book = /^#V/.test(location.hash) ? 'V' : 'H';
  let frame = 'B';     // 橫式照片面顯示哪個版本：B＝完整 16:9（推薦）、A＝192×104 套框
  let guides = false;
  const views = [];     // 放大檢視：[顯示版, 完整版, 說明]
  const addView = (p, cap) => { views.push([p.view, p.full, cap]); return views.length - 1; };
  const cmpOf = m => L.compare.months.find(x => x.month === m);
  const zoomOf = m => L.compare.zooms.find(x => x.month === m);

  // ---------- 頁面圖（含參考線） ----------
  function faceFig(p, k, cap, extraCls) {
    const n = addView(p, cap);
    return `<figure class="face face-${k}${extraCls ? ' ' + extraCls : ''}" data-k="${k}" data-face="${p.face}"${p.photo_box ? ` data-box="${p.photo_box.join(',')}"` : ''}>` +
      `<button type="button" class="zoom" data-f="${n}" aria-label="放大：${esc(cap)}"><img src="${esc(p.view.src)}" width="${p.view.w}" height="${p.view.h}" alt="${esc(cap)}" loading="lazy"></button>` +
      `<figcaption>${esc(cap)}</figcaption></figure>`;
  }
  function addGuides(root) {
    root.querySelectorAll('figure.face').forEach(fig => {
      const old = fig.querySelector('svg.guides'); if (old) old.remove();
      if (!guides) return;
      const f = L.formats[fig.dataset.k];
      const svg = document.createElementNS(SVGNS, 'svg');
      svg.setAttribute('class', 'guides'); svg.setAttribute('viewBox', `0 0 ${f.W} ${f.H}`); svg.setAttribute('preserveAspectRatio', 'none'); svg.setAttribute('aria-hidden', 'true');
      const rect = (x0, y0, x1, y1, cls) => { const r = document.createElementNS(SVGNS, 'rect'); r.setAttribute('x', x0); r.setAttribute('y', y0); r.setAttribute('width', x1 - x0); r.setAttribute('height', y1 - y0); r.setAttribute('class', cls); svg.appendChild(r); };
      const line = (y, cls) => { const l = document.createElementNS(SVGNS, 'line'); l.setAttribute('x1', 0); l.setAttribute('x2', f.W); l.setAttribute('y1', y); l.setAttribute('y2', y); l.setAttribute('class', cls); svg.appendChild(l); };
      rect(0, 0, f.W, f.coil_assumed, 'g-coil');
      line(f.coil_measured, 'g-coilm');
      rect(f.trim, f.trim, f.W - f.trim, f.H - f.trim, 'g-trim');
      rect(f.safe[0], f.safe[1], f.safe[2], f.safe[3], 'g-safe');
      if (fig.dataset.box) { const b = fig.dataset.box.split(',').map(Number); rect(b[0], b[1], b[2], b[3], 'g-photo'); }
      fig.querySelector('.zoom').appendChild(svg);
    });
  }
  const coverLegend = () => `<p class="legend"${guides ? '' : ' hidden'}><span class="lg lg-coil"></span>線圈假設區（上緣 12 mm）` +
    `<span class="lg lg-trim"></span>裁切線<span class="lg lg-safe"></span>安全區（橫式＝${esc(L.formats.H.safe_label)}；直式＝${esc(L.formats.V.safe_label)}）</p>`;

  // ---------- 封面區：R28 單人身分測試＋R27 已退回 ----------
  const MARK = { '通過': '✓', '部分': '△', '未通過': '✗' };
  function r27Card(k, c) {
    const cap = `R27 ${BOOK_ZH[k]}封面 ${c.dir}｜${c.dir_zh}（Owner 已退回）`;
    const nI = addView({ view: c.ids, full: c.ids }, `${cap}｜臉部對照（左＝身分參考、右＝封面）`);
    return `<article class="ccard rej" id="cover-${c.id}"><h4>${c.dir}｜${esc(c.dir_zh)} <em class="badge">${esc(C.r27.label)}</em></h4>` +
      faceFig({ ...c.page, face: 'cover' }, k, cap) +
      `<div class="cbtns"><button type="button" class="btn ghost" data-f="${nI}">臉部對照（12 人）</button></div></article>`;
  }
  function testSection() {
    const T = C.test, I = T.imgs;
    const nB = addView(I.before, 'R27 H-A 原本（全圖）'), nA = addView(I.after, 'R28 結果（全圖，只改了 Coco）');
    const cur = ba === 'after' ? [I.after, nA, 'R28 結果（只改了 Coco）'] : [I.before, nB, 'R27 H-A 原本'];
    const one = (im, cap) => { const n = addView({ view: im, full: im }, cap); return `<figure class="tf"><button type="button" class="zoom" data-f="${n}" aria-label="放大：${esc(cap)}"><img src="${esc(im.src)}" width="${im.w}" height="${im.h}" alt="${esc(cap)}" loading="lazy"></button><figcaption>${esc(cap)}</figcaption></figure>`; };
    return `<div class="tsec" id="cover-test"><h3>${esc(T.title)} <em class="badge test">${esc(T.label)}</em></h3>` +
      `<p class="note">${esc(T.scope)}</p>` +
      `<p class="cverdict"><b>Claude 自查：${esc(T.verdict)}</b>　${esc(T.verdict_text)}</p>` +
      `<div class="fsw" role="group" aria-label="前後切換"><span class="fsw-l">全圖：</span>` +
      `<button type="button" class="seg${ba === 'before' ? ' on' : ''}" data-ba="before" aria-pressed="${ba === 'before'}">R27 原本</button>` +
      `<button type="button" class="seg${ba === 'after' ? ' on' : ''}" data-ba="after" aria-pressed="${ba === 'after'}">R28 結果</button></div>` +
      `<figure class="tf big"><button type="button" class="zoom" id="ba-zoom" data-f="${cur[1]}" aria-label="放大：${esc(cur[2])}"><img id="ba-img" src="${esc(cur[0].view.src)}" width="${cur[0].view.w}" height="${cur[0].view.h}" alt="${esc(cur[2])}"></button>` +
      `<figcaption id="ba-cap">${esc(cur[2])}｜點圖放大；放大後按「原尺寸」看完整解析度</figcaption></figure>` +
      `<h4>Coco 臉部：身分基準｜R27 原本｜R28 結果</h4>${one(I.face, 'Coco 臉部對照')}` +
      `<h4>Coco 周圍：原本｜結果</h4><div class="tpair">${one(I.crop_before, 'Coco 周圍｜R27 原本')}${one(I.crop_after, 'Coco 周圍｜R28 結果')}</div>` +
      `<details class="more"><summary>4 項檢查與改動範圍</summary><ul class="chk">${T.checks.map(x => `<li><span class="mk">${MARK[x.result] || ''} ${esc(x.result)}</span>｜${esc(x.item)}<small>${esc(x.note)}</small></li>`).join('')}</ul>` +
      `<p class="note">${esc(T.diff)}</p><div class="tpair">${one(I.region, '改動範圍：藍框＝送去編輯的裁切、紅線＝回填範圍')}${one(I.diffmap, '全圖差異：白＝有改動的像素')}</div></details>` +
      `<p class="note">${esc(T.not_finished)}</p>` +
      `<label class="nl">${esc(T.note_label)}<textarea rows="3" data-tnote="coco" placeholder="例如：像不像 Coco、哪裡不自然（可留白）">${esc(tst.notes.coco || '')}</textarea></label>` +
      `<div class="acts"><button type="button" class="btn" id="test-copy">複製備註</button></div>` +
      `<textarea id="test-text" rows="5" readonly aria-label="備註文字"></textarea></div>`;
  }
  const fig = (im, cap, cls) => { const n = addView({ view: im, full: im }, cap); return `<figure class="tf${cls ? ' ' + cls : ''}"><button type="button" class="zoom" data-f="${n}" aria-label="放大：${esc(cap)}"><img src="${esc(im.src)}" width="${im.w}" height="${im.h}" alt="${esc(cap)}" loading="lazy"></button><figcaption>${esc(cap)}</figcaption></figure>`; };
  function fixSection() {
    const F = C.fix, I = F.imgs, B = F.ba;
    const cur = fba === 'after' ? [I.after, B.after_cap] : [I.before, B.before_cap];
    const nCur = addView(cur[0], cur[1] + '（全圖）');
    return `<div class="tsec fix" id="cover-fix"><h3>${esc(F.fix_title)} <em class="badge test">${esc(F.fix_label)}</em></h3>` +
      `<p class="warn">${esc(F.fix_scope)}</p>` +
      `<div class="fsw" role="group" aria-label="${esc(F.compare_label)}"><span class="fsw-l">全圖：</span>` +
      `<button type="button" class="seg${fba === 'after' ? ' on' : ''}" data-fba="after" aria-pressed="${fba === 'after'}">${esc(B.after)}</button>` +
      `<button type="button" class="seg${fba === 'before' ? ' on' : ''}" data-fba="before" aria-pressed="${fba === 'before'}">${esc(B.before)}</button></div>` +
      `<figure class="tf big"><button type="button" class="zoom" id="fba-zoom" data-f="${nCur}" aria-label="放大：${esc(cur[1])}"><img id="fba-img" src="${esc(cur[0].view.src)}" width="${cur[0].view.w}" height="${cur[0].view.h}" alt="${esc(cur[1])}"></button>` +
      `<figcaption id="fba-cap">${esc(cur[1])}｜點圖放大；放大後按「原尺寸」看完整解析度</figcaption></figure>` +
      `<h4>臉部與身分基準</h4>${fig(I.face, `身分基準（Coco）｜${B.after}`, 'mid')}` +
      `<h4>${esc(F.compare_label)}｜封面尺寸</h4>${fig(I.coverscale, `Coco 周圍｜封面尺寸｜${B.before} → ${B.after}`, 'wide')}` +
      `<h4>${esc(F.parts_label)}</h4><div class="tparts">${I.parts.map(p => fig(p, `${p.zh}｜${B.before} → ${B.after}`)).join('')}</div>` +
      `<p class="note">${esc(F.fix_changed)}</p><p class="note"><b>${esc(F.fix_remaining)}</b></p>` +
      `<fieldset class="dq"><legend>Coco 這個人修得如何？（只確認 Coco）</legend>` + F.options.map(o =>
        `<label class="opt"><input type="radio" name="fix" value="${esc(o.v)}"${fst.dec === o.v ? ' checked' : ''}> <span>${esc(o.label)}</span></label>`).join('') +
      `<button type="button" class="lnk" data-fclear="1">清除</button></fieldset>` +
      `<label class="nl">${esc(F.note_label)}<textarea rows="3" data-fnote="coco" placeholder="可留白">${esc(fst.notes.coco || '')}</textarea></label>` +
      `<div class="acts"><button type="button" class="btn" id="fix-copy">複製回饋</button></div>` +
      `<textarea id="fix-text" rows="5" readonly aria-label="回饋文字"></textarea>` +
      `<details class="more" id="fix-tech"><summary>${esc(F.tech_label)}</summary><p class="note">${esc(F.verdict_text)}</p>` +
      `<ul class="chk">${F.checks.map(x => `<li><span class="mk">${esc(x.area)}｜${esc(x.result)}</span><small>${esc(x.note)}</small></li>`).join('')}</ul>` +
      `<div class="tscroll"><table class="bp"><thead><tr><th>誰</th><th>R28 誤改</th><th>直接還原成 R27</th><th>緊貼 Coco 的過渡帶</th><th>舊捲髮換掉後露出</th></tr></thead><tbody>` +
      F.by_person.map(r => `<tr><td>${esc(r.who)}</td><td>${r.over}</td><td>${r.restored}</td><td>${r.band}</td><td>${r.revealed}</td></tr>`).join('') + `</tbody></table></div>` +
      `<p class="note">單位：像素。${esc(F.diff)}</p><p class="note">${esc(F.principle)}</p>` +
      `<p class="note">紀錄更正：</p><ul class="chk">${F.corrections.map(x => `<li><small>${esc(x)}</small></li>`).join('')}</ul>` +
      `<p class="note">還剩、本輪未處理：</p><ul class="chk">${F.remaining.map(x => `<li><small>${esc(x)}</small></li>`).join('')}</ul>` +
      `<div class="tparts">${I.fixes.map(p => fig(p, `${p.zh}｜R27 原圖｜R29｜R30`)).join('')}</div>` +
      `<div class="tpair">${fig(I.range, 'Coco 實際編輯範圍（藍）：範圍外全部是 R27 原圖')}${fig(I.diffmap, '和 R27 原圖不同的像素（白）')}</div></details></div>`;
  }
  function fix29Section() {
    const F = C.fix29, I = F.imgs, o = F.options.find(x => x.v === f9.dec);
    return `<div class="tsec" id="cover-fix29"><p class="note">${esc(F.fix_title)}｜${esc(F.fix_label)}。這是上一版；你在那一版留下的回饋原樣保留，本輪的選擇另外記，不會自動沿用。</p>` +
      `<p class="cverdict" id="fix29-saved"><b>你在 R29 的回饋：</b>${esc(o ? o.label : '（未選）')}｜備註：${esc((f9.notes.coco || '').trim() || '（無）')}</p>` +
      `${fig(I.coverscale, 'R29｜Coco 周圍｜封面尺寸｜R28 → R29', 'wide')}` +
      `<div class="tparts">${I.parts.map(p => fig(p, `R29｜${p.zh}｜R28 → R29`)).join('')}</div>` +
      `<p class="note">${esc(F.verdict_text)}</p></div>`;
  }
  function r31Card(k, c) {
    const cap = `${BOOK_ZH[k]}封面 ${c.dir}｜${c.dir_zh}（候選）`;
    return `<article class="ccard" id="r31-${c.id}"><h4>${c.dir}｜${esc(c.dir_zh)}</h4>` + faceFig({ ...c.page, face: 'cover' }, k, cap) + '</article>';
  }
  function r31Section() {
    const Q = C.r31;
    const grp = k => `<div class="cgroup" id="r31-${k}"><h4>${BOOK_ZH[k]}</h4><div class="cgrid cgrid-${k}">${Q.cards[k].map(c => r31Card(k, c)).join('')}</div>` +
      `<fieldset class="dq"><legend>${BOOK_ZH[k]}封面選哪一張？</legend>` + Q.options.map(o =>
        `<label class="opt"><input type="radio" name="r31-${k}" value="${esc(o.v)}"${qst.dec[k] === o.v ? ' checked' : ''}> <span>${esc(o.label)}</span></label>`).join('') +
      `<button type="button" class="lnk" data-r31clear="${k}">清除</button></fieldset>` +
      `<label class="nl">${esc(Q.note_labels[k])}<textarea rows="2" data-r31note="${k}" placeholder="可留白">${esc(qst.notes[k] || '')}</textarea></label>` +
      `<p class="pdfl"><a class="btn dl" id="r31-pdf-${k}" href="${esc(Q.pdf[k].href)}" download>${BOOK_ZH[k]}${esc(Q.pdf_label)}｜${Q.pdf[k].pages} 頁、${Q.pdf[k].size_mb} MB</a></p></div>`;
    return `<div class="tsec r31" id="cover-r31"><h3>${esc(Q.cover_title)} <em class="badge test">${esc(Q.label)}</em></h3>` +
      `<p class="note">${esc(Q.scope)}</p>` +
      `<div class="tools"><label class="gsw"><input type="checkbox" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>${coverLegend()}` +
      grp('H') + grp('V') +
      `<label class="nl">${esc(Q.note_labels.general)}<textarea rows="2" data-r31note="general" placeholder="可留白">${esc(qst.notes.general || '')}</textarea></label>` +
      `<div class="acts"><button type="button" class="btn" id="r31-copy">複製回饋</button></div>` +
      `<textarea id="r31-text" rows="7" readonly aria-label="回饋文字"></textarea></div>`;
  }
  function r32Card(k, c) {
    const G = C.r32, cap = `${G.groups[k]}｜${c.title}（候選）`;
    return `<article class="ccard" id="r32-${c.id}"><h4>${esc(c.title)}</h4>` + faceFig({ ...c.page, face: 'cover' }, k, cap) +
      `<p class="pdfl"><a class="btn dl" id="r32-pdf-${c.id}" href="${esc(c.pdf.href)}" download>${esc(G.pdf_label)}｜${c.pdf.pages} 面、${c.pdf.size_mb} MB</a></p></article>`;
  }
  function r32Section() {
    const G = C.r32;
    const grp = k => `<div class="cgroup" id="r32-${k}"><h4>${esc(G.groups[k])}</h4><div class="cgrid cgrid-${k}">${G.cards[k].map(c => r32Card(k, c)).join('')}</div>` +
      `<fieldset class="dq"><legend>${esc(G.groups[k])}選哪一個版本？</legend>` + G.options.map(o =>
        `<label class="opt"><input type="radio" name="r32-${k}" value="${esc(o.v)}"${q2.dec[k] === o.v ? ' checked' : ''}> <span>${esc(o.label)}</span></label>`).join('') +
      `<button type="button" class="lnk" data-r32clear="${k}">清除</button></fieldset>` +
      `<label class="nl">${esc(G.note_labels[k])}<textarea rows="2" data-r32note="${k}" placeholder="可留白">${esc(q2.notes[k] || '')}</textarea></label></div>`;
    return `<div class="tsec r31 r32" id="cover-r32"><h3>${esc(G.cover_title)} <em class="badge test">${esc(G.label)}</em></h3>` +
      `<p class="note">${esc(G.scope)}</p>` +
      `<div class="tools"><label class="gsw"><input type="checkbox" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>${coverLegend()}` +
      grp('H') + grp('V') + `<p class="note">${esc(G.logo_note)}</p>` +
      `<label class="nl">${esc(G.note_labels.general)}<textarea rows="2" data-r32note="general" placeholder="可留白">${esc(q2.notes.general || '')}</textarea></label>` +
      `<div class="acts"><button type="button" class="btn" id="r32-copy">複製全部封面回饋</button></div>` +
      `<textarea id="r32-text" rows="8" readonly aria-label="回饋文字"></textarea></div>`;
  }
  function r32Text() {
    const G = C.r32, n = k => (q2.notes[k] || '').trim() || '（無）';
    const lab = k => { const v = q2.dec[k]; if (v === 'edit') return '都想修改'; const c = G.cards[k].find(x => x.ver === v); return c ? `選版本 ${v}（${c.id}｜${c.title}）` : '（未選）'; };
    return [`${C.task}／${C.round}｜封面選擇（頁面版本 ${PAGE_COMMIT || '本機預覽'}；圖片版本 ${G.img_ver}）`, '選擇只代表封面版本，不等於交印核准。',
      `${G.groups.H}：${lab('H')}`, `${G.groups.V}：${lab('V')}`, `${G.groups.H}備註：${n('H')}`, `${G.groups.V}備註：${n('V')}`, `整體備註：${n('general')}`].join('\n');
  }
  function r35Section() {
    const G = C.r35;
    const pdfl = (k, P) => `<p class="pdfl"><a class="btn dl" id="r35-pdf-${k}" href="${esc(P.href)}" download>${esc(G.pdf_label[k])}｜${P.pages} 面、${P.size_mb} MB</a></p>`;
    const hcard = (k, X, title) => `<article class="ccard" id="r35-H-${k}"><h4>${esc(title)}</h4>` + faceFig({ ...X.page, face: 'cover' }, 'H', `${G.h_title}｜${title}`) +
      `<p class="zl">${esc(G.zoom_label)}</p>` + fig(X.zoom, `${title}｜${G.zoom_label}`, 'zoomcrop') + pdfl(k, X.pdf) + '</article>';
    return `<div class="tsec r31 r32 r33 r34 r35" id="cover-r35"><h3>${esc(G.cover_title)}</h3><p class="note">${esc(G.scope)}</p>` +
      `<div class="tools"><label class="gsw"><input type="checkbox" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>${coverLegend()}` +
      `<div class="cgroup" id="r35-V"><h4>${esc(G.v_title)} <em class="badge ok">${esc(G.v_badge)}</em></h4>` +
      `<div class="cgrid cgrid-V one"><article class="ccard acc" id="r35-V-acc">` + faceFig({ ...G.v.page, face: 'cover' }, 'V', `${G.v_title}（${G.v_badge}）`) +
      `<p class="note">${esc(G.v_note)}</p>` + pdfl('V', G.v.pdf) + '</article></div></div>' +
      `<div class="cgroup" id="r35-H"><h4>${esc(G.h_title)} <em class="badge test">${esc(G.h_badge)}</em></h4><p class="note">${esc(G.h_note)}</p>` +
      `<div class="cgrid cgrid-H">${hcard('orig', G.orig, G.orig_title)}${hcard('glow', G.glow, G.glow_title)}</div>` +
      `<fieldset class="dq"><legend>橫式年份要用哪一個？</legend>` + G.options.map(o =>
        `<label class="opt"><input type="radio" name="r35-H" value="${esc(o.v)}"${q5.dec === o.v ? ' checked' : ''}> <span>${esc(o.label)}</span></label>`).join('') +
      `<button type="button" class="lnk" data-r35clear="H">清除</button></fieldset>` +
      `<label class="nl">${esc(G.note_label)}<textarea rows="3" data-r35note="H" placeholder="可留白">${esc(q5.notes.H || '')}</textarea></label></div>` +
      `<div class="acts"><button type="button" class="btn" id="r35-copy">複製封面回饋</button></div>` +
      `<textarea id="r35-text" rows="6" readonly aria-label="回饋文字"></textarea></div>`;
  }
  function r35Text() {
    const G = C.r35, o = G.options.find(x => x.v === q5.dec), id = { glow: G.glow.id, orig: G.orig.id }[q5.dec];
    return [`${C.task}／${C.round}｜封面確認（頁面版本 ${PAGE_COMMIT || '本機預覽'}；圖片版本 ${G.img_ver}）`, '只代表封面確認，不等於交印核准。',
      `直式：${G.v.id}（${G.v_title}）已接受，不需選擇`, `橫式：${o ? o.label : '（未選）'}${id ? `（${id}）` : ''}`,
      `橫式備註：${(q5.notes.H || '').trim() || '（無）'}`].join('\n');
  }
  function r34RO() {
    const G = C.r34, o = G.options.find(x => x.v === q4.dec), id = { A: G.a.id, B: G.b.id }[q4.dec];
    return `<div class="tsec" id="cover-r34ro"><p class="cverdict" id="r34-saved"><b>你在 R34 的選擇：</b>${esc(o ? o.label : '（未選）')}${id ? `（${esc(q4.dec)}｜${esc(id)}）` : ''}｜備註：${esc((q4.notes.V || '').trim() || '（無）')}</p>` +
      `<div class="tparts">${fig(G.a.zoom, `R34 ${G.a_title}｜${G.zoom_label}`)}${fig(G.b.zoom, `R34 ${G.b_title}｜${G.zoom_label}`)}</div></div>`;
  }
  function r34Section() {
    const G = C.r34;
    const pdfl = (k, P) => `<p class="pdfl"><a class="btn dl" id="r34-pdf-${k}" href="${esc(P.href)}" download>${esc(G.pdf_label[k])}｜${P.pages} 面、${P.size_mb} MB</a></p>`;
    const vcard = (k, X, title) => `<article class="ccard" id="r34-V-${k}"><h4>${esc(title)}</h4>` + faceFig({ ...X.page, face: 'cover' }, 'V', `${G.v_title}｜${title}`) +
      `<p class="zl">${esc(G.zoom_label)}</p>` + fig(X.zoom, `${title}｜${G.zoom_label}`, 'zoomcrop') + pdfl(k, X.pdf) + '</article>';
    return `<div class="tsec r31 r32 r33 r34" id="cover-r34"><h3>${esc(G.cover_title)}</h3><p class="note">${esc(G.scope)}</p>` +
      `<div class="tools"><label class="gsw"><input type="checkbox" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>${coverLegend()}` +
      `<div class="cgroup" id="r34-H"><h4>${esc(G.h_title)} <em class="badge ok">${esc(G.h_badge)}</em></h4>` +
      `<div class="cgrid cgrid-H one"><article class="ccard acc" id="r34-H-L1">` + faceFig({ ...G.h.page, face: 'cover' }, 'H', `${G.h_title}（${G.h_badge}）`) +
      `<p class="note">${esc(G.h_note)}</p>` + pdfl('H', G.h.pdf) + '</article></div></div>' +
      `<div class="cgroup" id="r34-V"><h4>${esc(G.v_title)} <em class="badge test">${esc(G.v_badge)}</em></h4><p class="note">${esc(G.v_note)}</p>` +
      `<div class="cgrid cgrid-V">${vcard('A', G.a, G.a_title)}${vcard('B', G.b, G.b_title)}</div>` +
      `<fieldset class="dq"><legend>直式 Logo 圖示要用哪一個？</legend>` + G.options.map(o =>
        `<label class="opt"><input type="radio" name="r34-V" value="${esc(o.v)}"${q4.dec === o.v ? ' checked' : ''}> <span>${esc(o.label)}</span></label>`).join('') +
      `<button type="button" class="lnk" data-r34clear="V">清除</button></fieldset>` +
      `<label class="nl">${esc(G.note_label)}<textarea rows="3" data-r34note="V" placeholder="可留白">${esc(q4.notes.V || '')}</textarea></label></div>` +
      `<div class="acts"><button type="button" class="btn" id="r34-copy">複製封面回饋</button></div>` +
      `<textarea id="r34-text" rows="6" readonly aria-label="回饋文字"></textarea></div>`;
  }
  function r34Text() {
    const G = C.r34, lab = { A: `${G.a.id}`, B: `${G.b.id}` }, o = G.options.find(x => x.v === q4.dec);
    return [`${C.task}／${C.round}｜直式 Logo 圖示比較（頁面版本 ${PAGE_COMMIT || '本機預覽'}；圖片版本 ${G.img_ver}）`, '只是比較，不代表接受直式封面，也不等於交印核准。',
      `橫式：${G.h.id}（${G.h_title}）已接受，不需選擇`, `直式：${o ? o.label : '（未選）'}${lab[q4.dec] ? `（${q4.dec}｜${lab[q4.dec]}）` : ''}`,
      `直式備註：${(q4.notes.V || '').trim() || '（無）'}`].join('\n');
  }
  function r33RO() {
    const G = C.r33, o = G.options.find(x => x.v === q3.dec);
    return `<div class="tsec" id="cover-r33ro"><p class="cverdict" id="r33-saved"><b>你在 R33 的回饋：</b>${esc(o ? o.label : '（未選）')}｜備註：${esc((q3.notes.V || '').trim() || '（無）')}</p>` +
      `<div class="tparts">${fig(G.v.page.view, `R33 ${G.v_title}`)}${fig(G.v.prev.page.view, `R32 ${G.v_prev_title}`)}</div></div>`;
  }
  function r33Section() {
    const G = C.r33;
    const pdfl = k => { const P = G[k.toLowerCase()].pdf; return `<p class="pdfl"><a class="btn dl" id="r33-pdf-${k}" href="${esc(P.href)}" download>${esc(G.pdf_label[k])}｜${P.pages} 面、${P.size_mb} MB</a></p>`; };
    return `<div class="tsec r31 r32 r33" id="cover-r33"><h3>${esc(G.cover_title)}</h3><p class="note">${esc(G.scope)}</p>` +
      `<div class="tools"><label class="gsw"><input type="checkbox" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>${coverLegend()}` +
      `<div class="cgroup" id="r33-H"><h4>${esc(G.h_title)} <em class="badge ok">${esc(G.h_badge)}</em></h4>` +
      `<div class="cgrid cgrid-H one"><article class="ccard acc" id="r33-H-L1">` + faceFig({ ...G.h.page, face: 'cover' }, 'H', `${G.h_title}（${G.h_badge}）`) +
      `<p class="note">${esc(G.h_note)}</p>` + pdfl('H') + '</article></div></div>' +
      `<div class="cgroup" id="r33-V"><h4>${esc(G.v_title)} <em class="badge test">${esc(G.v_badge)}</em></h4>` +
      `<ul class="chk chg">${G.v_changes.map(x => `<li>${esc(x)}</li>`).join('')}</ul>` +
      (G.logo_note ? `<p class="lnote" id="r33-logo-note">${esc(G.logo_note)}</p>` : '') +
      `<div class="cgrid cgrid-V"><article class="ccard" id="r33-V-new"><h4>本輪修正版</h4>` + faceFig({ ...G.v.page, face: 'cover' }, 'V', `${G.v_title}（${G.v_badge}）`) + pdfl('V') + '</article>' +
      `<article class="ccard prev" id="r33-V-prev"><h4>${esc(G.v_prev_title)}</h4>` + faceFig({ ...G.v.prev.page, face: 'cover' }, 'V', `${G.v_prev_title}｜直式深色 版本 2`) + '</article></div>' +
      `<fieldset class="dq"><legend>直式修正版可以嗎？</legend>` + G.options.map(o =>
        `<label class="opt"><input type="radio" name="r33-V" value="${esc(o.v)}"${q3.dec === o.v ? ' checked' : ''}> <span>${esc(o.label)}</span></label>`).join('') +
      `<button type="button" class="lnk" data-r33clear="V">清除</button></fieldset>` +
      `<label class="nl">${esc(G.note_label)}<textarea rows="3" data-r33note="V" placeholder="可留白">${esc(q3.notes.V || '')}</textarea></label></div>` +
      `<div class="acts"><button type="button" class="btn" id="r33-copy">複製封面回饋</button></div>` +
      `<textarea id="r33-text" rows="6" readonly aria-label="回饋文字"></textarea></div>`;
  }
  function r33Text() {
    const G = C.r33, o = G.options.find(x => x.v === q3.dec);
    return [`${C.task}／${C.round}｜封面確認（頁面版本 ${PAGE_COMMIT || '本機預覽'}；圖片版本 ${G.img_ver}）`, '只代表封面確認，不等於交印核准。',
      `橫式：${G.h.id}（${G.h_title}）已接受，不需選擇`, `直式：${o ? o.label : '（未選）'}（${G.v.id}｜${G.v_title}）`,
      `直式備註：${(q3.notes.V || '').trim() || '（無）'}`].join('\n');
  }
  function r32RO() {
    const G = C.r32, n = ['H', 'V', 'general'].map(k => (q2.notes[k] || '').trim()).filter(Boolean).join('／') || '（無）';
    const lab = k => { const v = q2.dec[k]; if (v === 'edit') return '都想修改'; const c = G.cards[k].find(x => x.ver === v); return c ? `選版本 ${v}（${c.id}）` : '（未選）'; };
    const imgs = k => G.cards[k].map(c => fig(c.page.view, `R32 ${G.groups[k]}｜${c.title}`)).join('');
    return `<div class="tsec" id="cover-r32ro"><p class="cverdict" id="r32-saved"><b>你在 R32 的選擇：</b>${esc(G.groups.H)} ${esc(lab('H'))}｜${esc(G.groups.V)} ${esc(lab('V'))}｜備註：${esc(n)}</p>` +
      `<div class="tparts">${imgs('H')}${imgs('V')}</div></div>`;
  }
  function r31RO() {
    const Q = C.r31, lab = v => (v === 'edit' ? '都想修改' : v ? `${v}｜${Q.dirs[v]}` : '（未選）');
    const imgs = k => Q.cards[k].map(c => fig(c.page.view, `R31 ${BOOK_ZH[k]} ${c.dir}｜${c.dir_zh}`)).join('');
    return `<div class="tsec" id="cover-r31ro"><p class="cverdict" id="r31-saved"><b>你在 R31 的選擇：</b>橫式 ${esc(lab(qst.dec.H))}｜直式 ${esc(lab(qst.dec.V))}` +
      `｜備註：${esc(['H', 'V', 'general'].map(k => (qst.notes[k] || '').trim()).filter(Boolean).join('／') || '（無）')}</p>` +
      `<div class="tparts">${imgs('H')}${imgs('V')}</div></div>`;
  }
  function r31Text() {
    const Q = C.r31, lab = v => (v === 'edit' ? '都想修改' : v ? `${v}｜${Q.dirs[v]}` : '（未選）'), n = k => (qst.notes[k] || '').trim() || '（無）';
    return [`${C.task}／${C.round}｜非人物封面選擇（頁面版本 ${PAGE_COMMIT || '本機預覽'}）`, '選擇只代表封面方向，不等於交印核准。',
      `橫式：${lab(qst.dec.H)}`, `直式：${lab(qst.dec.V)}`, `橫式備註：${n('H')}`, `直式備註：${n('V')}`, `整體備註：${n('general')}`].join('\n');
  }
  function fix30Section() {
    const F = C.fix, I = F.imgs, o = F.options.find(x => x.v === f30.dec);
    return `<div class="tsec" id="cover-fix30"><p class="note">${esc(F.fix_title)}｜Owner 未接受。這是 R30 的紀錄；你當時的回饋原樣保留，不會帶到這一輪。</p>` +
      `<p class="cverdict" id="fix30-saved"><b>你在 R30 的回饋：</b>${esc(o ? o.label : '（未選）')}｜備註：${esc((f30.notes.coco || '').trim() || '（無）')}</p>` +
      fig(I.coverscale, 'R30｜Coco 周圍｜封面尺寸｜R27 原圖 → R30', 'wide') + fig(I.face, 'R30｜身分基準（Coco）｜R30', 'mid') + '</div>';
  }
  function fixText() {
    const o = C.fix.options.find(x => x.v === fst.dec);
    return [`${C.task}／${C.round}｜Coco 單人修正效果確認（頁面版本 ${PAGE_COMMIT || '本機預覽'}）`,
      '只確認 Coco 這一個人，不代表接受整張封面，也不授權修正其他角色或另一款封面。',
      `單人修正效果：${o ? o.label : '（未選）'}`, `備註：${(fst.notes.coco || '').trim() || '（無）'}`].join('\n');
  }
  function r27Block() {
    const grp = k => `<div class="cgroup" id="cover-${k}"><h4>${BOOK_ZH[k]}</h4><div class="cgrid cgrid-${k}">${C.cards[k].map(c => r27Card(k, c)).join('')}</div></div>`;
    return `<details class="more r27" id="cover-r27"><summary>${esc(C.r27.title)}</summary>` +
      `<p class="note">${esc(C.r27.note)}</p><ul class="fbq">${C.r27.feedback.map(x => `<li>${esc(x)}</li>`).join('')}</ul>` +
      `<div class="tools"><label class="gsw"><input type="checkbox" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>${coverLegend()}` +
      grp('H') + grp('V') + '</details>';
  }
  function personHist() {
    const PH = C.person_history;
    return `<details class="more hist" id="cover-hist"><summary>${esc(PH.label)}</summary><p class="note">${esc(PH.note)}</p><p class="note">Owner 原話：「${esc(PH.owner_words)}」</p>` +
      `<details class="more r30" id="cover-r30h"><summary>R30 Coco 單人效果確認（未接受）</summary>` + fix30Section() + '</details>' +
      (C.fix29 ? `<details class="more r29" id="cover-r29h"><summary>${esc(C.fix.r29_label)}（未接受）</summary>` + fix29Section() + '</details>' : '') +
      `<details class="more r28" id="cover-r28h"><summary>${esc(C.fix.r28_label)}（未接受）</summary>` + testSection() + '</details>' +
      r27Block() + '</details>';
  }
  function coverSection() {
    if (!C || !C.test) return '';
    if (C.r35) {
      return `<section class="sec" id="cover"><h2>封面</h2>` + r35Section() +
        `<details class="more hist" id="cover-old"><summary>${esc(C.person_history.outer_label)}</summary>` +
        `<details class="more r34h" id="cover-r34h"><summary>${esc(C.r34_history_label)}</summary>` + r34RO() + '</details>' +
        `<details class="more r33h" id="cover-r33h"><summary>${esc(C.r33_history_label)}</summary>` + r33RO() + '</details>' +
        `<details class="more r32h" id="cover-r32h"><summary>${esc(C.r32_history_label)}</summary>` + r32RO() + '</details>' +
        `<details class="more r31h" id="cover-r31h"><summary>${esc(C.r31_history_label)}</summary>` + r31RO() + '</details>' +
        personHist() + '</details></section>';
    }
    if (C.r34) {
      return `<section class="sec" id="cover"><h2>封面</h2>` + r34Section() +
        `<details class="more hist" id="cover-old"><summary>${esc(C.person_history.outer_label)}</summary>` +
        `<details class="more r33h" id="cover-r33h"><summary>${esc(C.r33_history_label)}</summary>` + r33RO() + '</details>' +
        `<details class="more r32h" id="cover-r32h"><summary>${esc(C.r32_history_label)}</summary>` + r32RO() + '</details>' +
        `<details class="more r31h" id="cover-r31h"><summary>${esc(C.r31_history_label)}</summary>` + r31RO() + '</details>' +
        personHist() + '</details></section>';
    }
    if (C.r33) {
      return `<section class="sec" id="cover"><h2>封面</h2>` + r33Section() +
        `<details class="more hist" id="cover-old"><summary>${esc(C.person_history.outer_label)}</summary>` +
        `<details class="more r32h" id="cover-r32h"><summary>${esc(C.r32_history_label)}</summary>` + r32RO() + '</details>' +
        `<details class="more r31h" id="cover-r31h"><summary>${esc(C.r31_history_label)}</summary>` + r31RO() + '</details>' +
        personHist() + '</details></section>';
    }
    if (C.r32) {
      return `<section class="sec" id="cover"><h2>封面</h2>` + r32Section() +
        `<details class="more hist" id="cover-old"><summary>${esc(C.person_history.outer_label)}</summary>` +
        `<details class="more r31h" id="cover-r31h"><summary>${esc(C.r31_history_label)}</summary>` + r31RO() + '</details>' +
        personHist() + '</details></section>';
    }
    if (C.r31) {
      const PH = C.person_history;
      return `<section class="sec" id="cover"><h2>封面</h2>` + r31Section() +
        `<details class="more hist" id="cover-hist"><summary>${esc(PH.label)}</summary><p class="note">${esc(PH.note)}</p><p class="note">Owner 原話：「${esc(PH.owner_words)}」</p>` +
        `<details class="more r30" id="cover-r30h"><summary>R30 Coco 單人效果確認（未接受）</summary>` + fix30Section() + '</details>' +
        (C.fix29 ? `<details class="more r29" id="cover-r29h"><summary>${esc(C.fix.r29_label)}（未接受）</summary>` + fix29Section() + '</details>' : '') +
        `<details class="more r28" id="cover-r28h"><summary>${esc(C.fix.r28_label)}（未接受）</summary>` + testSection() + '</details>' +
        r27Block() + '</details></section>';
    }
    const grp = k => `<div class="cgroup" id="cover-${k}"><h4>${BOOK_ZH[k]}</h4><div class="cgrid cgrid-${k}">${C.cards[k].map(c => r27Card(k, c)).join('')}</div></div>`;
    return `<section class="sec" id="cover"><h2>封面</h2>` + (C.fix ? fixSection() +
      (C.fix29 ? `<details class="more r29" id="cover-r29h"><summary>${esc(C.fix.r29_label)}</summary>` + fix29Section() + '</details>' : '') +
      `<details class="more r28" id="cover-r28h"><summary>${esc(C.fix.r28_label)}</summary>` + testSection() + '</details>' : testSection()) +
      `<details class="more r27" id="cover-r27"><summary>${esc(C.r27.title)}</summary>` +
      `<p class="note">${esc(C.r27.note)}</p><ul class="fbq">${C.r27.feedback.map(x => `<li>${esc(x)}</li>`).join('')}</ul>` +
      `<div class="tools"><label class="gsw"><input type="checkbox" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>${coverLegend()}` +
      grp('H') + grp('V') + '</details></section>';
  }
  function testText() {
    return [`${C.task}／${C.round}｜Coco 單人身分測試備註（頁面版本 ${PAGE_COMMIT || '本機預覽'}）`,
      `這是${C.test.label}；只記錄意見，不是接受封面。`, `備註：${(tst.notes.coco || '').trim() || '（無）'}`].join('\n');
  }
  const refreshCover = () => {
    const t = $('#test-text'); if (t && C && C.test) t.value = testText();
    const f = $('#fix-text'); if (f && C && C.fix) f.value = fixText();
    const q = $('#r31-text'); if (q && C && C.r31) q.value = r31Text();
    const q2t = $('#r32-text'); if (q2t && C && C.r32) q2t.value = r32Text();
    const q3t = $('#r33-text'); if (q3t && C && C.r33) q3t.value = r33Text();
    const q4t = $('#r34-text'); if (q4t && C && C.r34) q4t.value = r34Text();
    const q5t = $('#r35-text'); if (q5t && C && C.r35) q5t.value = r35Text();
  };

  // ---------- 各區 ----------
  function topSection() {
    const P = L.pdf;
    const dl = k => `<a class="btn dl" href="${esc(P[k].href)}" download>${BOOK_ZH[k]} PDF（${P[k].pages} 頁，成品 ${esc(P[k].trim)}，含出血 ${esc(P[k].canvas)}，${P[k].size_mb} MB）</a>`;
    const acc = C ? `<div class="acc"><h3>${esc(C.accepted.title)}</h3><ul>${C.accepted.items.map(x => `<li>${esc(x)}</li>`).join('')}</ul><p class="note">${esc(C.accepted.scope)}</p></div>`
      : `<h3>待 Penny 決定</h3><ol class="pend">${L.pending.map(x => `<li>${esc(x)}</li>`).join('')}</ol>`;
    return `<section class="sec" id="dl"><h2>內頁排版預覽 PDF</h2><div class="dls">${dl('H')}${dl('V')}</div>` +
      `<p class="warn">${esc(L.status_note)}</p>` + acc +
      `<details class="more"><summary>推薦排法（目前預覽與 PDF 用的）</summary><ul>${L.recommended.map(x => `<li>${esc(x)}</li>`).join('')}</ul><p class="note">${esc(L.date_note)}</p></details>` +
      `<details class="more"><summary>仍需廠商確認或打樣的事（本輪不聯絡廠商、不打樣）</summary><ul>${L.vendor.map(x => `<li>${esc(x)}</li>`).join('')}</ul></details></section>`;
  }

  function navSection() {
    const tabs = ['H', 'V'].map(k => `<button type="button" class="tab${k === book ? ' on' : ''}" data-book="${k}" aria-pressed="${k === book}">${BOOK_ZH[k]}<span>${L.pdf[k].pages} 面｜${esc(L.pdf[k].trim)}</span></button>`).join('');
    const months = ['cover', ...Array.from({ length: 12 }, (_, i) => i + 1), 'other'].map(m =>
      `<li><a class="mchip" href="#${book}-${m === 'cover' ? 'cover' : m === 'other' ? 'other' : 'm' + m}">${m === 'cover' ? '封面' : m === 'other' ? '其他頁' : m + ' 月'}</a></li>`).join('');
    const fsw = book === 'H' ? `<div class="fsw" role="group" aria-label="橫式照片框"><span class="fsw-l">照片框：</span>` +
      `<button type="button" class="seg${frame === 'B' ? ' on' : ''}" data-frame="B" aria-pressed="${frame === 'B'}">完整 16:9（推薦）</button>` +
      `<button type="button" class="seg${frame === 'A' ? ' on' : ''}" data-frame="A" aria-pressed="${frame === 'A'}">192×104 套框</button></div>` : '';
    return `<section class="sec navsec" id="nav"><div class="tabs">${tabs}</div><ol class="mnav">${months}</ol>` +
      `<div class="tools">${fsw}<label class="gsw"><input type="checkbox" id="gsw" data-guides${guides ? ' checked' : ''}> 顯示參考線</label></div>` +
      `<p class="legend"${guides ? '' : ' hidden'}><span class="lg lg-coil"></span>線圈假設區（上緣 12 mm；虛線＝編輯器示意約 ${L.formats[book].coil_measured} mm）` +
      `<span class="lg lg-trim"></span>裁切線<span class="lg lg-safe"></span>${esc(L.formats[book].safe_label)}<span class="lg lg-photo"></span>照片框</p></section>`;
  }

  function note(key, label) {
    const v = st.notes[key] || '';
    return `<label class="nl">${esc(label)}<textarea rows="2" data-note="${esc(key)}" placeholder="想改什麼就寫在這裡（可留白）">${esc(v)}</textarea></label>`;
  }

  function monthCard(m) {
    const ps = L.pages[book].filter(p => p.month === m);
    const ph = ps.find(p => p.role === 'photo'), gr = ps.find(p => p.role === 'grid');
    const who = ph.person;
    let photoFig, extra = '';
    if (book === 'H') {
      const c = cmpOf(m);
      if (frame === 'A') {
        photoFig = faceFig(c.A, 'H', `橫式 ${m} 月｜${who}｜照片面（192×104 套框，比較用）`, 'is-a');
        extra += `<p class="cnote">${esc(c.note)}</p>`;
      } else {
        photoFig = faceFig(ph, 'H', `橫式 ${m} 月｜${who}｜面 ${ph.face} 照片面（完整 16:9）`);
      }
      const z = zoomOf(m);
      if (z) {
        if (frame !== 'A') extra += `<p class="cnote">192×104 套框時：${esc(c.note)}</p>`;
        extra += `<details class="zd"><summary>上下緣放大比較（照片框兩種排法）</summary>` +
          ['top', 'bottom'].map(e => `<p class="zh">${e === 'top' ? '上緣（髮頂）' : '下緣（腳／鞋）'}</p><div class="zrow">` +
            z.rows[e].map(it => { const n = addView({ view: it, full: it }, `${who} ${e === 'top' ? '上緣' : '下緣'}｜${it.label}`); return `<figure class="zf"><button type="button" class="zoom px" data-f="${n}"><img src="${esc(it.src)}" width="${it.w}" height="${it.h}" alt="${esc(it.label)}" loading="lazy"></button><figcaption>${esc(it.label)}</figcaption></figure>`; }).join('') + '</div>').join('') +
          `<p class="note">直接從 300 dpi 輸出切下來、未縮放；白色是照片框外的頁面。</p></details>`;
      }
    } else {
      photoFig = faceFig(ph, 'V', `直式 ${m} 月｜${who}｜面 ${ph.face} 照片面`);
    }
    const grFig = faceFig(gr, book, `${BOOK_ZH[book]} ${m} 月｜${who}｜面 ${gr.face} 大格面`);
    return `<article class="mcard" id="${book}-m${m}"><h3>${m} 月｜${esc(who)}</h3><div class="spread spread-${book}">${photoFig}${grFig}</div>${extra}${note(`${book}-${m}`, `${BOOK_ZH[book]} ${m} 月備註`)}</article>`;
  }

  function bookSection() {
    const P = L.pages[book];
    const cov = P.find(p => p.role === 'cover');
    const others = P.filter(p => ['memo', 'year', 'barcode'].includes(p.role));
    return `<section class="sec" id="pages"><h2>${BOOK_ZH[book]}：實際頁面（${P.length} 面，依範本頁序）</h2>` +
      `<p class="note">每月兩面：照片面在前、大格面在後。紙張正反面怎麼拼、背面會不會轉向還沒跟廠商確認，所以這裡和 PDF 都是一面一面正向排列。</p>` +
      `<article class="mcard" id="${book}-cover"><h3>封面（面 1）</h3><div class="spread spread-${book} one">${faceFig(cov, book, C ? `${BOOK_ZH[book]}｜面 1 ${C.r26_cover_label}` : `${BOOK_ZH[book]}｜面 1 封面（品牌名稱是佔位）`)}</div>${note(`${book}-cover`, `${BOOK_ZH[book]}封面備註`)}</article>` +
      Array.from({ length: 12 }, (_, i) => monthCard(i + 1)).join('') +
      `<article class="mcard" id="${book}-other"><h3>其他頁</h3><div class="spread spread-${book} many">${others.map(p => faceFig(p, book, `${BOOK_ZH[book]}｜面 ${p.face} ${p.role_zh}`)).join('')}</div>${note(`${book}-other`, `${BOOK_ZH[book]}其他頁備註`)}</article></section>`;
  }

  function fbSection() {
    const dec = L.decisions.map(d => `<fieldset class="dq"><legend>${esc(d.q)}</legend>` + d.options.map(o =>
      `<label class="opt"><input type="radio" name="dec-${esc(d.id)}" value="${esc(o.v)}"${st.dec[d.id] === o.v ? ' checked' : ''}> <span>${esc(o.label)}${o.rec ? '<em class="rec">推薦</em>' : ''}${o.note ? `<small>${esc(o.note)}</small>` : ''}</span></label>`).join('') +
      `<button type="button" class="lnk" data-clear="${esc(d.id)}">清除這題</button></fieldset>`).join('');
    const body = `<p class="note">只針對排版；照片沿用 24 張定案，不用重新接受。沒選的題目不算接受。</p>${dec}` +
      note('H-general', '橫式整體備註') + note('V-general', '直式整體備註') +
      `<div class="acts"><button type="button" class="btn" id="copy">複製全部回饋</button></div>` +
      `<textarea id="cp-text" rows="9" readonly aria-label="回饋文字"></textarea>`;
    return C ? `<section class="sec" id="fb"><details class="more hist"><summary>${esc(C.history_label)}</summary>${body}</details></section>`
      : `<section class="sec" id="fb"><h2>排版回饋</h2>${body}</section>`;
  }

  // ---------- 回饋文字 ----------
  function feedbackText() {
    const lines = [`${L.task}／${L.round}｜排版預覽回饋（頁面版本 ${PAGE_COMMIT || '本機預覽'}）`, '只針對排版；照片沿用 24 張定案（照片接受另記）。'];
    L.decisions.forEach(d => { const o = d.options.find(x => x.v === st.dec[d.id]); lines.push(`${d.q}：${o ? o.label : '（未選）'}`); });
    const order = ['H-general', 'H-cover', ...Array.from({ length: 12 }, (_, i) => `H-${i + 1}`), 'H-other', 'V-general', 'V-cover', ...Array.from({ length: 12 }, (_, i) => `V-${i + 1}`), 'V-other'];
    const name = k => { const [b, r] = k.split('-'); return `${BOOK_ZH[b]}${r === 'general' ? '整體' : r === 'cover' ? '封面' : r === 'other' ? '其他頁' : ` ${r} 月`}`; };
    const ns = order.filter(k => (st.notes[k] || '').trim()).map(k => `・${name(k)}：${st.notes[k].trim()}`);
    lines.push(ns.length ? '備註：' : '備註：（無）', ...ns);
    return lines.join('\n');
  }
  const refreshCopy = () => { const t = $('#cp-text'); if (t) t.value = feedbackText(); };
  let toastT = 0;
  const toast = msg => { const t = $('#toast'); t.textContent = msg; t.hidden = false; clearTimeout(toastT); toastT = setTimeout(() => { t.hidden = true; }, 2200); };

  // ---------- 繪製 ----------
  function render(keepScroll) {
    const y = window.scrollY;
    views.length = 0;
    app.innerHTML = coverSection() + topSection() + navSection() + bookSection() + fbSection();
    addGuides(app);
    refreshCopy();
    refreshCover();
    if (keepScroll) window.scrollTo(0, y);
  }

  app.addEventListener('click', e => {
    const b = e.target.closest('[data-book]');
    if (b) { if (b.dataset.book !== book) { book = b.dataset.book; render(true); } return; }
    const fr = e.target.closest('[data-frame]');
    if (fr) { if (fr.dataset.frame !== frame) { frame = fr.dataset.frame; render(true); } return; }
    const cl = e.target.closest('[data-clear]');
    if (cl) { delete st.dec[cl.dataset.clear]; save(); app.querySelectorAll(`input[name="dec-${cl.dataset.clear}"]`).forEach(i => { i.checked = false; }); refreshCopy(); return; }
    const fbb = e.target.closest('[data-fba]');
    if (fbb) {
      if (fbb.dataset.fba !== fba) {
        fba = fbb.dataset.fba;
        const I = C.fix.imgs, im = I[fba].view, cap = fba === 'after' ? C.fix.ba.after_cap : C.fix.ba.before_cap;
        const img = $('#fba-img'); img.src = im.src; img.alt = cap;
        $('#fba-zoom').dataset.f = String(addView(I[fba], cap + '（全圖）'));
        $('#fba-cap').textContent = `${cap}｜點圖放大；放大後按「原尺寸」看完整解析度`;
        app.querySelectorAll('[data-fba]').forEach(b => { const on = b.dataset.fba === fba; b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); });
      }
      return;
    }
    if (e.target.closest('[data-r35clear]')) { q5.dec = ''; q5save(); app.querySelectorAll('input[name="r35-H"]').forEach(i => { i.checked = false; }); refreshCover(); return; }
    if (e.target.closest('[data-r34clear]')) { q4.dec = ''; q4save(); app.querySelectorAll('input[name="r34-V"]').forEach(i => { i.checked = false; }); refreshCover(); return; }
    if (e.target.closest('[data-r33clear]')) { q3.dec = ''; q3save(); app.querySelectorAll('input[name="r33-V"]').forEach(i => { i.checked = false; }); refreshCover(); return; }
    const q2c = e.target.closest('[data-r32clear]');
    if (q2c) { const k = q2c.dataset.r32clear; delete q2.dec[k]; q2save(); app.querySelectorAll(`input[name="r32-${k}"]`).forEach(i => { i.checked = false; }); refreshCover(); return; }
    const qc = e.target.closest('[data-r31clear]');
    if (qc) { const k = qc.dataset.r31clear; delete qst.dec[k]; qsave(); app.querySelectorAll(`input[name="r31-${k}"]`).forEach(i => { i.checked = false; }); refreshCover(); return; }
    if (e.target.closest('[data-fclear]')) { fst.dec = ''; fsave(); app.querySelectorAll('input[name="fix"]').forEach(i => { i.checked = false; }); refreshCover(); return; }
    const bab = e.target.closest('[data-ba]');
    if (bab) {
      if (bab.dataset.ba !== ba) {
        ba = bab.dataset.ba;
        const I = C.test.imgs, im = I[ba].view, cap = ba === 'after' ? 'R28 結果（只改了 Coco）' : 'R27 H-A 原本';
        const img = $('#ba-img'); img.src = im.src; img.alt = cap;
        $('#ba-zoom').dataset.f = String(addView(I[ba], ba === 'after' ? 'R28 結果（全圖，只改了 Coco）' : 'R27 H-A 原本（全圖）'));
        $('#ba-cap').textContent = `${cap}｜點圖放大；放大後按「原尺寸」看完整解析度`;
        app.querySelectorAll('[data-ba]').forEach(b => { const on = b.dataset.ba === ba; b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); });
      }
      return;
    }
    const cp = e.target.closest('#copy, #test-copy, #fix-copy, #r31-copy, #r32-copy, #r33-copy, #r34-copy, #r35-copy');
    if (cp) {
      const kind = cp.id === 'r35-copy' ? 'r35' : cp.id === 'r34-copy' ? 'r34' : cp.id === 'r33-copy' ? 'r33' : cp.id === 'r32-copy' ? 'r32' : cp.id === 'r31-copy' ? 'r31' : cp.id === 'fix-copy' ? 'fix' : cp.id === 'test-copy' ? 'test' : 'layout';
      const box = $({ r35: '#r35-text', r34: '#r34-text', r33: '#r33-text', r32: '#r32-text', r31: '#r31-text', fix: '#fix-text', test: '#test-text', layout: '#cp-text' }[kind]);
      const t = kind === 'r35' ? r35Text() : kind === 'r34' ? r34Text() : kind === 'r33' ? r33Text() : kind === 'r32' ? r32Text() : kind === 'r31' ? r31Text() : kind === 'fix' ? fixText() : kind === 'test' ? testText() : feedbackText();
      box.value = t;
      const done = ok => toast(ok ? (kind === 'r35' || kind === 'r34' || kind === 'r33' ? '已複製封面回饋' : kind === 'r32' ? '已複製全部封面回饋' : kind === 'r31' || kind === 'fix' ? '已複製回饋' : kind === 'test' ? '已複製備註' : '已複製全部回饋') : '無法自動複製，請在下方文字框手動選取複製');
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(() => done(true), () => { box.select(); done(false); });
      else { box.select(); done(false); }
      return;
    }
    const z = e.target.closest('[data-f]');
    if (z) openViewer(+z.dataset.f, z);
  });
  app.addEventListener('change', e => {
    if (e.target.matches('[data-guides]')) {
      guides = e.target.checked;
      app.querySelectorAll('[data-guides]').forEach(i => { i.checked = guides; });
      app.querySelectorAll('.legend').forEach(lg => { lg.hidden = !guides; });
      addGuides(app); return;
    }
    if (e.target.type === 'radio' && e.target.name.startsWith('dec-')) { st.dec[e.target.name.slice(4)] = e.target.value; save(); refreshCopy(); }
    if (e.target.type === 'radio' && e.target.name === 'fix') { fst.dec = e.target.value; fsave(); refreshCover(); }
    if (e.target.type === 'radio' && e.target.name === 'r35-H') { q5.dec = e.target.value; q5save(); refreshCover(); }
    if (e.target.type === 'radio' && e.target.name === 'r34-V') { q4.dec = e.target.value; q4save(); refreshCover(); }
    if (e.target.type === 'radio' && e.target.name === 'r33-V') { q3.dec = e.target.value; q3save(); refreshCover(); }
    if (e.target.type === 'radio' && e.target.name.startsWith('r32-')) { q2.dec[e.target.name.slice(4)] = e.target.value; q2save(); refreshCover(); }
    if (e.target.type === 'radio' && e.target.name.startsWith('r31-')) { qst.dec[e.target.name.slice(4)] = e.target.value; qsave(); refreshCover(); }
  });
  app.addEventListener('input', e => {
    const q5k = e.target.dataset && e.target.dataset.r35note;
    if (q5k != null) {
      const v = e.target.value;
      if (v.trim()) q5.notes[q5k] = v; else delete q5.notes[q5k];
      q5save(); refreshCover(); return;
    }
    const q4k = e.target.dataset && e.target.dataset.r34note;
    if (q4k != null) {
      const v = e.target.value;
      if (v.trim()) q4.notes[q4k] = v; else delete q4.notes[q4k];
      q4save(); refreshCover(); return;
    }
    const q3k = e.target.dataset && e.target.dataset.r33note;
    if (q3k != null) {
      const v = e.target.value;
      if (v.trim()) q3.notes[q3k] = v; else delete q3.notes[q3k];
      q3save(); refreshCover(); return;
    }
    const q2k = e.target.dataset && e.target.dataset.r32note;
    if (q2k != null) {
      const v = e.target.value;
      if (v.trim()) q2.notes[q2k] = v; else delete q2.notes[q2k];
      q2save(); refreshCover(); return;
    }
    const qk = e.target.dataset && e.target.dataset.r31note;
    if (qk != null) {
      const v = e.target.value;
      if (v.trim()) qst.notes[qk] = v; else delete qst.notes[qk];
      qsave(); refreshCover(); return;
    }
    const fk = e.target.dataset && e.target.dataset.fnote;
    if (fk != null) {
      const v = e.target.value;
      if (v.trim()) fst.notes[fk] = v; else delete fst.notes[fk];
      fsave(); refreshCover(); return;
    }
    const tk = e.target.dataset && e.target.dataset.tnote;
    if (tk != null) {
      const v = e.target.value;
      if (v.trim()) tst.notes[tk] = v; else delete tst.notes[tk];
      tsave(); refreshCover(); return;
    }
    const k = e.target.dataset && e.target.dataset.note;
    if (k == null) return;
    const v = e.target.value;
    if (v.trim()) st.notes[k] = v; else delete st.notes[k];
    save(); refreshCopy();
  });

  // ---------- 放大檢視：先看顯示版，「原尺寸」改看 300 dpi 完整版 ----------
  const viewer = $('#viewer'), vimg = $('#viewer-img'), vcap = $('#viewer-cap'), vmode = $('#viewer-mode'), vbody = $('#viewer-body');
  let vk = -1, lastBtn = null, pushed = false;
  const show = (k, nat) => {
    const v = views[k]; if (!v) return;
    vk = k; const m = nat ? v[1] : v[0];
    vimg.src = m.src; vimg.width = m.w; vimg.height = m.h; vimg.alt = v[2];
    vcap.textContent = `${v[2]}｜${nat ? '原尺寸' : '顯示'} ${m.w}×${m.h} px` + (nat ? '' : v[0] === v[1] ? '；按「原尺寸」看完整解析度' : '；按「原尺寸」看 300 dpi 完整解析度');
    viewer.classList.toggle('natural', nat); vmode.textContent = nat ? '符合畫面' : '原尺寸';
  };
  function openViewer(k, btn) {
    show(k, false); lastBtn = btn; viewer.hidden = false; document.documentElement.classList.add('noscroll');
    try { history.pushState({ viewer: 1 }, ''); pushed = true; } catch (err) { pushed = false; }
    $('#viewer-close').focus({ preventScroll: true });
  }
  const close = fromPop => {
    if (viewer.hidden) return;
    viewer.hidden = true; vimg.removeAttribute('src'); document.documentElement.classList.remove('noscroll');
    if (pushed && !fromPop) { pushed = false; history.back(); }
    pushed = false;
    if (lastBtn && document.body.contains(lastBtn)) lastBtn.focus({ preventScroll: true });
  };
  const toggle = ev => {
    const nat = !viewer.classList.contains('natural');
    let fx = 0.5, fy = 0.5;
    if (ev && ev.target === vimg) { const r = vimg.getBoundingClientRect(); fx = (ev.clientX - r.left) / r.width; fy = (ev.clientY - r.top) / r.height; }
    show(vk, nat);
    if (nat) { vbody.scrollLeft = Math.max(0, fx * vimg.width - vbody.clientWidth / 2); vbody.scrollTop = Math.max(0, fy * vimg.height - vbody.clientHeight / 2); }
  };
  $('#viewer-close').addEventListener('click', () => close(false));
  vmode.addEventListener('click', () => toggle(null));
  vimg.addEventListener('click', toggle);
  window.addEventListener('popstate', () => close(true));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(false); });

  document.title = `${C ? C.title : L.title}｜2027 KOL 桌曆`;
  $('#tline').textContent = `${L.task}｜${C ? C.round : L.round}`;
  $('#title').textContent = C ? C.title : L.title;
  $('#intro').textContent = C ? C.intro : L.intro;
  $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
  render(false);
  if (location.hash) { const t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
})();
