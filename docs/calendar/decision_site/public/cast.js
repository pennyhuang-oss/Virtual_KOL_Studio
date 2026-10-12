// 2027 KOL 桌曆｜第一階段自由選角。選擇只存在本機瀏覽器 localStorage，不送到伺服器；沒有追蹤或分析。
// 名單狀態與舊版決策頁（plan.html）的資料分開存放；本頁只讀取舊版資料來顯示提示，從不寫入或轉換。
'use strict';
(() => {
  const D = window.CAL_DATA;
  const app = document.getElementById('app');
  if (!D || !D.cast) { app.textContent = '資料載入失敗。'; return; }

  const SHA = D.fixed_sha;
  const KEY = 'cal2027-casting-v1:' + SHA;
  const OLD_KEY = 'cal2027-decision-v1:' + SHA;
  const IMG = D.images;
  const C = D.cast;
  const LIST = C.candidates;
  const BY = {};
  LIST.forEach(c => { BY[c.id] = c; });
  const ORDER = LIST.map(c => c.id);
  const REC = C.rec12;
  const MAX_CMP = 4;
  const GROUP_ZH = { rec: '主管原推薦', backup: 'R1 備選', out: 'R1 未入選', r2: 'R2 追加比較' };
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();
  const fullName = c => c.native ? `${c.name} ${c.native}` : c.name;
  const sorted = a => [...a].sort((x, y) => ORDER.indexOf(x) - ORDER.indexOf(y));

  // ---------- 狀態 ----------
  // sel：已選 ID（不重複、依候選順序）；conf：{ list, at }，名單有任何更動就刪掉，要重新確認。
  const blank = () => ({ sel: [], conf: null, cmp: [], other: '', note: '' });
  let storageOK = true;
  function load() {
    try {
      const s = JSON.parse(localStorage.getItem(KEY));
      if (s && Array.isArray(s.sel)) {
        const b = blank();
        return { ...b, ...s, sel: sorted([...new Set(s.sel.filter(id => BY[id]))]), cmp: (s.cmp || []).filter(id => BY[id]).slice(0, MAX_CMP) };
      }
    } catch (e) { storageOK = false; }
    return blank();
  }
  let S = load();
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(S)); storageOK = true; } catch (e) {
      if (storageOK) toast('這個瀏覽器不允許儲存（例如無痕模式）：重新整理後選擇會消失。');
      storageOK = false;
    }
  }
  function setSel(next) {
    S.sel = sorted([...new Set(next.filter(id => BY[id]))]);
    S.conf = null;
    save();
    refresh();
  }
  function status() {
    if (S.conf && S.sel.length === 12 && S.conf.list === JSON.stringify(S.sel)) return 'conf';
    return S.sel.length ? 'draft' : 'empty';
  }
  const ST = { empty: '尚未選人', draft: '草稿・待 Penny 確認', conf: 'Penny 已確認' };
  const ST_CLASS = { empty: 'none', draft: 'draft', conf: 'conf' };
  function oldRecord() {
    try {
      const o = JSON.parse(localStorage.getItem(OLD_KEY));
      if (!o || !o.v || !Object.keys(o.v).length) return null;
      const c = o.conf && o.conf.roster;
      const rv = o.v.roster;
      const confirmed = c && (typeof c === 'string' ? c : c.v) === JSON.stringify(rv);
      return { roster: rv || null, confirmed: !!confirmed, n: Object.keys(o.v).length };
    } catch (e) { return null; }
  }

  // ---------- 比對 ----------
  function pairsAmong(ids) {
    const set = new Set(ids);
    return C.pairs.filter(p => set.has(p.a) && set.has(p.b));
  }
  const pairName = id => BY[id].name.split(' ')[0];
  function pairLine(p) {
    const v = p.v != null ? ` ${p.v}` : '';
    const lead = p.kind === 'hit' ? '既有碰撞紀錄' : (p.kind === 'near' ? '接近門檻' : '相似度提示');
    return `${lead}：${pairName(p.a)} ↔ ${pairName(p.b)}${v}｜${p.text}`;
  }
  function diffRec() {
    const sel = new Set(S.sel), rec = new Set(REC);
    return { kept: REC.filter(id => sel.has(id)), removed: REC.filter(id => !sel.has(id)), added: S.sel.filter(id => !rec.has(id)) };
  }

  // ---------- 畫面元件 ----------
  function srcKind(m) {
    if (m.res === 'hires') return `高解析預覽（原圖等比縮小，${m.w}×${m.h} px）`;
    if ((m.src || '').includes('/img/cand/')) return `R1 選角板縮圖（${m.w}×${m.h} px）`;
    if ((m.src || '').includes('/r2/faces/heads/')) return `R2 臉部比較頭像（${m.w}×${m.h} px）`;
    return `R2 比較圖裁切（${m.w}×${m.h} px）`;
  }
  function fig(iid, cap, cls) {
    const m = IMG[iid];
    if (!m) return '';
    const badge = m.res === 'hires' ? '高解析預覽' : '低解析';
    return `<figure class="fig${cls ? ' ' + cls : ''}"><button type="button" class="zoom" data-img="${esc(iid)}" data-cap="${esc(cap)}" aria-label="放大：${esc(cap)}">` +
      `<img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" loading="lazy" decoding="async" alt="${esc(cap)}">` +
      `<span class="resb ${m.res === 'hires' ? 'hires' : 'lowres'}">${badge}</span><span class="zi" aria-hidden="true">放大</span></button></figure>`;
  }
  function measNote(c) {
    if (c.measured) return '有既有遮髮量測（只涵蓋 Batch 3 的 19 位）';
    return '沒有臉部量測（未量測不等於不像）';
  }
  function card(c) {
    const pairs = C.pairs.filter(p => p.a === c.id || p.b === c.id);
    const meta = [c.origin, c.age ? `${c.age} 歲` : ''].filter(Boolean).join('，');
    return `<article class="cc" id="c-${esc(c.id)}" data-id="${esc(c.id)}">
<div class="cc-face">${fig(c.face, `${fullName(c)}｜正臉`, 'face')}</div>
<div class="cc-extra">${c.extras.map(e => fig(e, `${fullName(c)}｜其他照片`)).join('')}</div>
<h3 class="cc-h">${esc(c.name)}${c.native ? ` <span class="nat">${esc(c.native)}</span>` : ''}</h3>
<p class="cc-meta"><code>${esc(c.id)}</code> <span class="tag g-${esc(c.group)}">${esc(GROUP_ZH[c.group])}</span>${meta ? `<br>${esc(meta)}` : ''}</p>
<p class="cc-desc">${esc(c.desc)}</p>
<p class="cc-meas">${esc(measNote(c))}</p>
${pairs.length ? `<details class="cc-pairs"><summary>既有相似度紀錄（${pairs.length}）</summary><ul>${pairs.map(p => `<li class="k-${esc(p.kind)}">${esc(pairLine(p))}</li>`).join('')}</ul></details>` : ''}
<div class="cc-act"><button type="button" class="btn sel-btn" data-act="toggle" data-id="${esc(c.id)}">加入名單</button>
<label class="cmp"><input type="checkbox" data-act="cmp" data-id="${esc(c.id)}"> 並排比較</label></div>
</article>`;
  }

  // ---------- 版面 ----------
  function render() {
    $('#sha').textContent = SHA;
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    const main = LIST.filter(c => c.group !== 'r2');
    const extra = LIST.filter(c => c.group === 'r2');
    app.innerHTML = `
<section class="sec" id="legacy-box" hidden></section>
<section class="sec quick" id="picked"><h2>已選名單 <span id="pk-count"></span> <span id="pk-st" class="st"></span></h2>
<div class="actions">
<button type="button" class="btn ghost" id="act-empty">從空白開始選</button>
<button type="button" class="btn ghost" id="act-rec">載入主管原推薦 12 人作為草稿</button>
<button type="button" class="btn" id="act-confirm">確認這 12 位人設</button></div>
<p class="note" id="pk-help"></p>
<div id="pk-warn"></div>
<div id="pk-list" class="pk-grid"></div>
<div id="pk-diff" class="note"></div>
</section>
<section class="sec" id="compare"><h2>並排比較（2–4 位）</h2><div id="cmp-body"></div></section>
<section class="sec" id="cands"><h2>候選 18 位（R1 入圍比較名單）</h2>
<p class="note">名單來源：CAL_02 §3 與 data/cal_r1_candidates.json（固定 SHA）。每位可單獨加入或移出，不綁月份、照片或其他人。照片都是既有圖：正臉是 R2 臉部比較頭像或 R1 選角板圖，另兩張是 R1 選角板圖；<b>都是低解析辨識用圖</b>，只用來認人，不代表桌曆素材。相似度紀錄只照錄既有資料，沒有新量測。</p>
<div class="cc-grid">${main.map(card).join('')}</div></section>
<section class="sec" id="r2c"><h2>R2 追加比較人選（不在 R1 的 18 位內）</h2>
<p class="note">R2 為了讓 Penny 比較而補圖的兩位（CAL_02 §5.3、§6）。可以選，但兩位都沒有版面樣張；Ananya 沒有任何臉部量測。</p>
<div class="cc-grid">${extra.map(card).join('')}</div></section>
<section class="sec" id="notes"><h2>其他人設與補充意見</h2>
<label class="lbl" for="other">想看其他人設（填姓名即可；本輪不擴大掃描整個型錄）</label>
<input type="text" id="other" maxlength="300" placeholder="例：Nico Tsai、Zoey Yeh" value="${esc(S.other)}">
<label class="lbl" for="note">補充意見（自由文字，不屬於確認項目）</label>
<textarea id="note" rows="3" maxlength="3000" placeholder="例：想要多一位冷感路線；某兩位看起來太像…">${esc(S.note)}</textarea>
</section>
<section class="sec" id="out"><h2>複製選角結果</h2>
<div class="callout">選擇只存在這個瀏覽器（localStorage），<b>不會送到伺服器</b>。複製後請<b>貼回 ChatGPT</b>；本頁不會通知主管。不必先選照片、品牌或版面。</div>
<div class="actions"><button type="button" class="btn" id="act-copy">複製選角結果</button><button type="button" class="btn danger" id="act-reset">重設選角</button></div>
<label class="lbl" for="out-text">將複製的文字（預覽）</label><textarea id="out-text" rows="14" readonly></textarea>
</section>
<section class="sec" id="next"><h2>接下來</h2>
<ol class="steps"><li><b>選人</b>（本頁）：挑出 12 位不同人設。</li><li><b>確認名單</b>：恰好 12 位時按「確認這 12 位人設」，再複製結果貼回 ChatGPT。</li>
<li><b>選素材</b>：主管指派下一輪後，只整理入選 12 位的照片，讓 Penny 選橫式與直式要用的照片。</li><li><b>排月份與版面</b>：最後才決定月份、版面、尺度與品牌。</li></ol>
<p class="note">原本的照片、尺度、版面與品牌選項保留在「<a href="plan.html">原推薦方案參考</a>」，第一階段不必填。</p></section>`;
    renderLegacy();
    refresh();
  }
  function renderLegacy() {
    const o = oldRecord();
    const box = $('#legacy-box');
    if (!o) { box.hidden = true; return; }
    box.hidden = false;
    box.innerHTML = `<h2>舊版決策紀錄</h2><p class="note">這個瀏覽器有上一版決策頁的選擇紀錄（${o.n} 項；名單題 ${esc(o.roster || '未回答')}${o.confirmed ? '，當時按過確認' : ''}）。` +
      `它保留在「<a href="plan.html">原推薦方案參考</a>」頁，與這裡的新選角狀態<b>分開</b>，不會被刪除，也不會轉成新名單或核准。</p>`;
  }
  function refresh() {
    const n = S.sel.length;
    const st = status();
    $('#pk-count').textContent = `已選 ${n}／12 位`;
    const stEl = $('#pk-st');
    stEl.className = 'st ' + ST_CLASS[st];
    stEl.textContent = ST[st];
    $('#bar-count').textContent = `已選 ${n}／12｜${ST[st]}`;
    $('#act-confirm').disabled = n !== 12 || st === 'conf';
    $('#pk-help').textContent = st === 'conf'
      ? `已確認：${new Date(S.conf.at).toLocaleString('zh-TW', { hour12: false })}。之後只要換人（即使換回原名單），就會回到草稿，需要重新確認。`
      : (n === 12 ? '已選滿 12 位，可以按「確認這 12 位人設」。' : '恰好 12 位不同人設才能確認名單。');
    const warn = [];
    if (n > 12) warn.push(`<p class="pk-over">已選 ${n} 位，超過 12 位。請自己移除 ${n - 12} 位；本頁不會自動替你刪人。</p>`);
    else if (n > 0 && n < 12) warn.push(`<p class="pk-under">還差 ${12 - n} 位。</p>`);
    const pairs = pairsAmong(S.sel);
    if (pairs.length) {
      warn.push(`<div class="callout"><b>已選名單裡的既有相似度紀錄</b>（照錄既有資料；請看圖取捨，本頁不會自動換人。沒有列出的組合不代表不像）<ul>${pairs.map(p => `<li class="k-${esc(p.kind)}">${esc(pairLine(p))}</li>`).join('')}</ul></div>`);
    }
    $('#pk-warn').innerHTML = warn.join('');
    $('#pk-list').innerHTML = n ? S.sel.map(id => {
      const c = BY[id];
      return `<div class="pk"><div class="pk-img">${fig(c.face, `${fullName(c)}｜正臉`)}</div><div class="pk-t"><b>${esc(c.name)}</b>${c.native ? `<br><span class="nat">${esc(c.native)}</span>` : ''}<br><span class="tag g-${esc(c.group)}">${esc(GROUP_ZH[c.group])}</span></div>` +
        `<button type="button" class="btn ghost small" data-act="toggle" data-id="${esc(id)}">移出</button></div>`;
    }).join('') : '<p class="note">還沒有選人。可以「從空白開始選」，在下方候選卡片按「加入名單」；或「載入主管原推薦 12 人作為草稿」再只換想換的人。</p>';
    const d = diffRec();
    $('#pk-diff').innerHTML = n ? `相對主管原推薦 12 人：保留 ${d.kept.length}、移除 ${d.removed.length}${d.removed.length ? `（${esc(d.removed.map(pairName).join('、'))}）` : ''}、加入 ${d.added.length}${d.added.length ? `（${esc(d.added.map(pairName).join('、'))}）` : ''}` : '';
    // 卡片狀態
    $$('.cc').forEach(el => {
      const id = el.dataset.id;
      const inSel = S.sel.includes(id);
      el.classList.toggle('in', inSel);
      const b = el.querySelector('.sel-btn');
      b.textContent = inSel ? '移出名單' : '加入名單';
      b.classList.toggle('ghost', inSel);
      b.setAttribute('aria-pressed', inSel ? 'true' : 'false');
      el.querySelector('input[data-act="cmp"]').checked = S.cmp.includes(id);
    });
    renderCompare();
    $('#out-text').value = buildText();
  }
  function renderCompare() {
    const body = $('#cmp-body');
    if (S.cmp.length < 2) {
      body.innerHTML = `<p class="note">在候選卡片勾「並排比較」，選 2–4 位（目前 ${S.cmp.length} 位）。只用既有照片，沒有新量測。</p>` +
        (S.cmp.length ? `<button type="button" class="btn ghost small" id="cmp-clear">清除比較</button>` : '');
      return;
    }
    const cols = S.cmp.map(id => {
      const c = BY[id];
      const inSel = S.sel.includes(id);
      return `<div class="cmp-col">${fig(c.face, `${fullName(c)}｜正臉`, 'face')}<div class="cc-extra">${c.extras.map(e => fig(e, `${fullName(c)}｜其他照片`)).join('')}</div>` +
        `<h3 class="cc-h">${esc(c.name)}${c.native ? ` <span class="nat">${esc(c.native)}</span>` : ''}</h3><p class="cc-desc">${esc(c.desc)}</p><p class="cc-meas">${esc(measNote(c))}</p>` +
        `<button type="button" class="btn${inSel ? ' ghost' : ''} small" data-act="toggle" data-id="${esc(id)}">${inSel ? '移出名單' : '加入名單'}</button></div>`;
    }).join('');
    const pairs = pairsAmong(S.cmp);
    body.innerHTML = `<div class="cmp-grid n${S.cmp.length}">${cols}</div>` +
      `<div class="callout">${pairs.length ? `<b>這幾位之間的既有紀錄</b>（照錄）<ul>${pairs.map(p => `<li class="k-${esc(p.kind)}">${esc(pairLine(p))}</li>`).join('')}</ul>` : '這幾位之間<b>沒有</b>本頁資料中的量測或相似度紀錄。'}` +
      `<p class="note">沒有觸發門檻或沒有量測，都不等於看起來一定不像；請以照片判斷。</p></div>` +
      `<button type="button" class="btn ghost small" id="cmp-clear">清除比較</button>`;
  }

  // ---------- 輸出文字 ----------
  function buildText() {
    const st = status();
    const t = [];
    const d = diffRec();
    t.push('【2027 KOL 桌曆｜第一階段選角結果】（由決策頁產生；請貼回 ChatGPT）');
    t.push(`素材基準 SHA：${SHA}`);
    t.push(`頁面版本：${PAGE_COMMIT || '未知（本機預覽）'}`);
    t.push(`產生時間：${new Date().toLocaleString('zh-TW', { hour12: false })}（瀏覽器時間）`);
    t.push(`名單狀態：${st === 'conf' ? `Penny 已確認（${new Date(S.conf.at).toLocaleString('zh-TW', { hour12: false })}）` : (st === 'draft' ? '草稿（尚未確認）' : '尚未選人')}｜已選 ${S.sel.length}／12 位${S.sel.length > 12 ? '（超過 12 位）' : (S.sel.length < 12 && S.sel.length ? '（未滿 12 位）' : '')}`);
    t.push('');
    t.push(`已選人設（${S.sel.length} 位）：`);
    S.sel.forEach((id, i) => { const c = BY[id]; t.push(`　${i + 1}. ${fullName(c)}（${id}）〔${GROUP_ZH[c.group]}〕`); });
    if (!S.sel.length) t.push('　（無）');
    t.push('');
    t.push('相對主管原推薦 12 人：');
    t.push(`　保留 ${d.kept.length} 位：${d.kept.map(id => `${BY[id].name}（${id}）`).join('、') || '無'}`);
    t.push(`　移除 ${d.removed.length} 位：${d.removed.map(id => `${BY[id].name}（${id}）`).join('、') || '無'}`);
    t.push(`　加入 ${d.added.length} 位：${d.added.map(id => `${BY[id].name}（${id}）`).join('、') || '無'}`);
    const pairs = pairsAmong(S.sel);
    t.push('');
    t.push('已選名單裡的既有相似度紀錄（照錄；沒有列出不代表不像）：');
    if (pairs.length) pairs.forEach(p => t.push('　- ' + pairLine(p)));
    else t.push('　（本頁資料中沒有紀錄）');
    t.push('');
    t.push('想看的其他人設：' + ((S.other || '').trim() || '（無）'));
    t.push('補充意見（自由文字，不屬於確認項目）：' + ((S.note || '').trim() || '（無）'));
    t.push('');
    t.push('※ 尚未選定素材、月份與版面；選角照片只用來辨認人設。此結果不是主管核准，也不是印刷或廠商核准。');
    return t.join('\n');
  }

  // ---------- 事件 ----------
  function toggle(id) {
    if (!BY[id]) return;
    if (S.sel.includes(id)) setSel(S.sel.filter(x => x !== id));
    else setSel([...S.sel, id]);
  }
  app.addEventListener('click', e => {
    const z = e.target.closest('.zoom');
    if (z) { openViewer(z); return; }
    const b = e.target.closest('button');
    if (!b) return;
    if (b.dataset.act === 'toggle') { toggle(b.dataset.id); return; }
    if (b.id === 'act-empty') {
      if (S.sel.length && !window.confirm(`清空目前已選的 ${S.sel.length} 位？（舊版紀錄不受影響）`)) return;
      setSel([]);
      toast('已清空，可以從空白開始選。');
    }
    if (b.id === 'act-rec') {
      const same = JSON.stringify(S.sel) === JSON.stringify(sorted(REC));
      if (S.sel.length && !same && !window.confirm(`會把目前已選的 ${S.sel.length} 位換成主管原推薦的 12 位（草稿，不是核准）。要繼續嗎？`)) return;
      setSel(REC);
      toast('已載入主管原推薦 12 人（草稿）。只換想換的人，再按確認。');
    }
    if (b.id === 'act-confirm') openReview();
    if (b.id === 'act-copy') copyOut();
    if (b.id === 'act-reset') {
      if (!window.confirm('清除這個瀏覽器裡的選角名單、確認紀錄與補充文字？（舊版決策紀錄不受影響）')) return;
      try { localStorage.removeItem(KEY); } catch (e2) { /* 只清記憶體 */ }
      S = blank();
      render();
      toast('已重設選角。');
    }
    if (b.id === 'cmp-clear') { S.cmp = []; save(); refresh(); }
  });
  app.addEventListener('change', e => {
    const el = e.target;
    if (el.dataset && el.dataset.act === 'cmp') {
      const id = el.dataset.id;
      if (el.checked) {
        if (S.cmp.length >= MAX_CMP) { el.checked = false; toast(`最多同時比較 ${MAX_CMP} 位；先取消一位再加。`); return; }
        if (!S.cmp.includes(id)) S.cmp.push(id);
      } else S.cmp = S.cmp.filter(x => x !== id);
      save();
      refresh();
      if (S.cmp.length >= 2) toast('已更新「並排比較」區（在已選名單下方）。');
    }
  });
  let saveTimer = null;
  app.addEventListener('input', e => {
    if (e.target.id === 'other' || e.target.id === 'note') {
      S[e.target.id] = e.target.value;
      clearTimeout(saveTimer);
      saveTimer = setTimeout(save, 300);
      $('#out-text').value = buildText();
    }
  });
  $('#bar-copy').addEventListener('click', copyOut);

  // ---------- 確認視窗 ----------
  const review = $('#review');
  function openReview() {
    if (S.sel.length !== 12) { toast('恰好 12 位不同人設才能確認名單。'); return; }
    $('#review-list').innerHTML = S.sel.map(id => { const c = BY[id]; return `<div class="rv">${fig(c.face, `${fullName(c)}｜正臉`)}<p><b>${esc(c.name)}</b>${c.native ? `<br>${esc(c.native)}` : ''}</p></div>`; }).join('');
    const pairs = pairsAmong(S.sel);
    $('#review-warn').innerHTML = pairs.length ? `<div class="callout"><b>名單裡的既有相似度紀錄</b>（照錄，請自行取捨）<ul>${pairs.map(p => `<li class="k-${esc(p.kind)}">${esc(pairLine(p))}</li>`).join('')}</ul></div>` : '';
    review.hidden = false;
    document.documentElement.classList.add('noscroll');
    $('#review-ok').focus({ preventScroll: true });
  }
  function closeReview() { review.hidden = true; document.documentElement.classList.remove('noscroll'); }
  $('#review-ok').addEventListener('click', () => {
    if (S.sel.length !== 12) { closeReview(); return; }
    S.conf = { list: JSON.stringify(S.sel), at: new Date().toISOString() };
    save();
    closeReview();
    refresh();
    toast('已確認 12 位人設。請按「複製選角結果」貼回 ChatGPT。');
  });
  $('#review-cancel').addEventListener('click', closeReview);
  review.addEventListener('click', e => { const z = e.target.closest('.zoom'); if (z) openViewer(z); });

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
  function openViewer(btn) {
    const m = IMG[btn.dataset.img];
    if (!m) return;
    lastBtn = btn;
    vimg.src = m.z; vimg.width = m.w; vimg.height = m.h; vimg.alt = btn.dataset.cap;
    vcap.textContent = `${btn.dataset.cap}｜${srcKind(m)}｜${m.res === 'hires' ? '未排版，只用來認人' : '低解析辨識用圖：只用來認人，不代表桌曆素材'}`;
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
