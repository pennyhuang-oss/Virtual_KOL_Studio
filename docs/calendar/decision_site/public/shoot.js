// 2027 KOL 桌曆｜M-3 寫真拍攝企劃。企劃內容來自 data.js 的 m3（產生自 data/cal_m3_shoot_plan.json）；本頁沒有任何生成圖。
// Penny 的回饋只存在本機瀏覽器 localStorage（cal2027-shoot-v1:<SHA>），不送到伺服器；沒有追蹤或分析。
// 第二階段素材選擇（cal2027-materials-v1:<SHA>）與更早的選角／決策資料，本頁不讀、不寫、不刪。
'use strict';
(() => {
  const D = window.CAL_DATA;
  const app = document.getElementById('app');
  if (!D || !D.m3 || !D.mat) { app.textContent = '資料載入失敗。'; return; }

  const SHA = D.fixed_sha;
  const KEY = 'cal2027-shoot-v1:' + SHA;
  const IMG = D.images;
  const P = D.m3;
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

  // ---------- 回饋狀態 ----------
  const CH = { main: '接受主方向', alt: '改用替代方向', edit: '想修改' };
  const QS = {
    hv: { label: '橫直構圖', opts: { both: '同意：同一造型橫、直各拍一張', one: '先只拍一種（寫在備註）', unsure: '還不確定' } },
    first: { label: '首批試拍', opts: { ok: '同意這個方向（Iris、Rin、Miu、Mia；上限依建議），由主管另發執行指令', swap: '想換首批人選或上限（寫在備註）', hold: '先不要試拍' } },
  };
  const blank = () => ({ p: Object.fromEntries(PEOPLE.map(p => [p.pid, { c: '', note: '' }])), q: { hv: '', first: '' }, gnote: '' });
  let storageOK = true;
  function load() {
    const S0 = blank();
    try {
      const s = JSON.parse(localStorage.getItem(KEY));
      if (!s || typeof s !== 'object') return S0;
      PEOPLE.forEach(({ pid }) => {
        const q = (s.p || {})[pid] || {};
        S0.p[pid] = { c: CH[q.c] ? q.c : '', note: typeof q.note === 'string' ? q.note : '' };
      });
      Object.keys(QS).forEach(k => { const v = (s.q || {})[k]; S0.q[k] = QS[k].opts[v] ? v : ''; });
      S0.gnote = typeof s.gnote === 'string' ? s.gnote : '';
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
    return fig(it.img, `${nm(it.pid)}｜${id}｜${it.label}｜既有照片，只當參考`,
      `${REF_TAG} <code>${esc(id)}</code> ${esc(it.label)}`);
  }
  const ul = a => `<ul class="facts">${a.map(x => `<li>${esc(x)}</li>`).join('')}</ul>`;
  const tbl = (head, rows) => `<div class="tbl"><table><thead><tr>${head.map(h => `<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>` +
    rows.map(r => `<tr>${r.map(c => `<td>${esc(c)}</td>`).join('')}</tr>`).join('') + '</tbody></table></div>';

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
<h3>移植到 12 位的做法</h3>
<dl class="mdl">${A.method.map(m => `<dt>${esc(m.item)}</dt><dd>${esc(m.how)}</dd>`).join('')}</dl>
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
    return `<section class="sec" id="owner"><h2>二、Penny 喜歡的 4 張（審美參考）</h2>
<p class="note">${esc(O.note)}</p>
<div class="ogrid">${O.items.map(x => `<article class="oc">${refFig(x.id)}<p class="oc-w">${esc(x.what)}</p><p class="oc-c">可借用：${esc(x.cue)}</p></article>`).join('')}</div>
<p class="note">${esc(O.reading)}</p></section>`;
  }

  function overview() {
    return `<div class="ov">${PEOPLE.map((p, i) => {
      const m = IMG[MP[p.pid].face];
      return `<a class="rs" href="#s-${esc(p.pid)}"><img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" alt="" loading="lazy" decoding="async">` +
        `<span class="rs-t"><b>${i + 1}. ${esc(nm(p.pid))}</b><span class="rs-p">${esc(p.title)}</span><span class="rs-p" data-ov="${esc(p.pid)}"></span></span></a>`;
    }).join('')}</div>`;
  }
  function diffTable() {
    return tbl(['人設', '時段', '光線', '配色', '場景', '服裝', '姿勢', '表情', '取景'],
      PEOPLE.map(p => { const f = p.diff; return [nm(p.pid), f.time, f.light, f.palette, f.place, f.outfit, f.pose, f.face, f.frame]; }));
  }
  function plan(p, i) {
    const pid = p.pid;
    const q = S.p[pid];
    return `<section class="sec plan" id="s-${esc(pid)}" data-pid="${esc(pid)}">
<div class="ph"><div class="ph-face">${fig(MP[pid].face, `${fullName(pid)}｜辨識用正臉（既有照片）`)}</div>
<div class="ph-t"><h2>${i + 1}. ${esc(nm(pid))}${MP[pid].native ? ` <span class="nat">${esc(MP[pid].native)}</span>` : ''}</h2>
<p class="ptitle">${esc(p.title)}</p>
<p>${p.first ? '<span class="tag t-first">首批試拍建議</span> ' : ''}<span class="st none" data-st="${esc(pid)}"></span></p></div></div>
<div class="pgrid">
<div class="pnew"><p class="pn-h">這個企劃的新照片</p><div class="ng"><div class="nb nb-h"><b>橫 3:2</b><span>尚未生成</span></div><div class="nb nb-v"><b>直 3:4</b><span>尚未生成</span></div></div>
<p class="pn-n">拍板並經主管另發指令後才會試拍；這裡不放任何示意圖。</p></div>
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
<details class="info"><summary>拍攝細節：構圖、風險、與人設核對</summary>
<dl class="pdl small">
<dt>與人設核對</dt><dd>${esc(p.check)}</dd>
<dt>背景與色彩</dt><dd>${esc(p.bg)}</dd>
<dt>橫構圖</dt><dd>${esc(p.frame_h)}</dd>
<dt>直構圖</dt><dd>${esc(p.frame_v)}</dd>
<dt>臉／髮頂／身形／日期區</dt><dd>${esc(p.keep)}</dd>
</dl>
${tbl(['風險', '處理'], p.risks.map(r => [r.risk, r.fix]))}
</details>
<details class="info"><summary>prompt 草稿（尚未執行）</summary>
<p class="note">可直接使用的英文草稿，<b>沒有送出過</b>。兩段只差取景句；每段結尾都有同一句皮膚與質感描述。執行時沿用這位既有的 Soul（不列在公開頁）。</p>
<p class="lbl">橫構圖（3:2）</p><pre class="prompt">${esc(p.prompt_h)}</pre>
<p class="lbl">直構圖（3:4）</p><pre class="prompt">${esc(p.prompt_v)}</pre>
</details>
<fieldset class="fb"><legend>Penny 的回饋：${esc(nm(pid))}</legend>
<div class="fb-opts">${Object.entries(CH).map(([k, v]) => `<label class="fb-o"><input type="radio" name="c-${esc(pid)}" value="${k}" data-c="${esc(pid)}"${q.c === k ? ' checked' : ''}> ${esc(v)}</label>`).join('')}</div>
<label class="lbl" for="note-${esc(pid)}">備註（想修改哪裡、喜歡哪裡；會一起複製）</label>
<textarea id="note-${esc(pid)}" data-note="${esc(pid)}" rows="2" maxlength="2000" placeholder="例：衣服想換成白色；背景想要海邊">${esc(q.note)}</textarea>
<button type="button" class="btn ghost small" data-clear="${esc(pid)}">清除這位的回饋</button>
</fieldset></section>`;
  }

  function compSec() {
    const C = P.composition;
    return `<section class="sec" id="comp"><h2>四、橫直構圖</h2>
<p class="lead"><b>建議：${esc(C.recommend)}。</b></p>${ul(C.why)}
<p class="note"><b>另一種做法：</b>${esc(C.alt)}</p>
<p class="note">每位的臉、髮頂、身形和日期區在橫直兩種構圖能不能保住，寫在各位卡片的「拍攝細節」裡。</p>
<details class="info"><summary>拆開來看：構圖需求、模型輸出、解析度、出血線圈、廠商未知</summary>
${tbl(['層次', '說明'], C.layers.map(x => [x.k, x.v]))}</details></section>`;
  }

  function costSec() {
    const E = P.execution, M = E.model, K = E.cost;
    return `<section class="sec" id="cost"><h2>五、試拍與成本（只是提案）</h2>
<p class="callout warn"><b>本頁不授權任何花費。</b>${esc(K.gate)}</p>
<p class="note"><b>怎麼拍：</b>${esc(M.recommend)}</p>
<h3>首批建議 4 位</h3>
${tbl(['人設', '為什麼先拍她'], K.first_batch.map(x => [x.who, x.why]))}
${tbl(['項目', '內容'], K.plan.map(x => [x.k, x.v]))}
<details class="info"><summary>單價依據（哪些是查證、哪些是歷史紀錄、哪些未知）</summary>
${tbl(['項目', '數值', '依據', '等級'], K.unit.map(x => [x.k, x.v, x.basis, x.level]))}</details>
<details class="info"><summary>重生上限與停止條件</summary>${ul(K.retry)}</details>
<details class="info"><summary>模型、Soul 狀態與已知限制</summary>
${ul(M.why)}
${tbl(['人設', 'Soul 狀態（紀錄）'], M.soul_status.map(x => [x.who, x.status]))}
<p class="note">Soul ID 不列在公開頁。</p>
${ul(M.known_limits)}
<p class="note"><b>多階段：</b>${esc(M.multi_stage)}</p>
<p class="note"><b>未知：</b>${esc(M.unknown.join('、'))}</p></details></section>`;
  }

  function outSec() {
    return `<section class="sec" id="out"><h2>六、回饋與複製</h2>
<div class="callout">回饋只存在這個瀏覽器（localStorage），<b>不會送到伺服器</b>，也不會通知主管。可以只回覆一部分就複製；沒回覆的會寫「未回覆」。複製後請貼回 ChatGPT。<br>這是對企劃方向的回饋，<b>不是</b>生成授權，也不是照片、月份、版面或印刷核准。</div>
<h3>想請 Penny 決定的事</h3>
<ol class="facts">${P.questions.map(x => `<li>${esc(x)}</li>`).join('')}</ol>
<p class="note">第 1、3、4 題在各位卡片上選（Somi、Coco 若想改回其他方向，請選「想修改」並寫在備註）。第 2、5 題在下面選：</p>
${Object.entries(QS).map(([k, Q]) => `<fieldset class="fb"><legend>${esc(Q.label)}</legend><div class="fb-opts col">${Object.entries(Q.opts).map(([v, t]) =>
      `<label class="fb-o"><input type="radio" name="q-${k}" value="${v}" data-q="${k}"${S.q[k] === v ? ' checked' : ''}> ${esc(t)}</label>`).join('')}</div></fieldset>`).join('')}
<label class="lbl" for="gnote">整體備註（自由文字）</label>
<textarea id="gnote" rows="3" maxlength="3000" placeholder="例：整體想要更多戶外；某位的方向想整個換掉">${esc(S.gnote)}</textarea>
<div class="actions"><button type="button" class="btn" id="act-copy">複製回饋</button><button type="button" class="btn danger" id="act-reset">清除本頁全部回饋</button></div>
<label class="lbl" for="out-text">將複製的文字（預覽）</label><textarea id="out-text" rows="14" readonly></textarea>
</section>
<section class="sec" id="refs"><h2>其他頁面</h2><ul class="facts">
<li><a href="index.html">第二階段：為入選人設挑照片</a>：素材選擇照舊保留在那一頁，本頁不讀也不改。</li>
<li>完整企劃文件：repo 的 <code>docs/calendar/CAL_18_M3_SHOOT_PLAN.md</code>（企劃資料 <code>${esc(P.plan_file)}</code>）。</li></ul></section>`;
  }

  function render() {
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    $('#planver').textContent = `${P.version}（${P.written_on}）`;
    app.innerHTML = aaliyaSec() + ownerSec() +
      `<section class="sec" id="people"><h2>三、12 位企劃</h2>
<ul class="facts"><li>每位一個主推薦、一個替代方向（替代方向寫在卡片的「替代方向」）。順序是名單順序，不是月份。</li>
<li>每張只拍一位；甜美與性感元素寫在卡片上，全部維持成人樣貌，不做任何降齡呈現。</li>
<li>灰色框是「尚未生成」的新照片位置；旁邊的照片是她<b>既有</b>的照片，只用來認人。</li></ul>
${overview()}
<details class="info"><summary>12 位差異總表與仍然接近的地方</summary>${diffTable()}
<p class="note"><b>仍然接近、需要 Penny 判斷（不宣稱已消除）：</b></p>${ul(P.overlap)}</details>
</section>` + PEOPLE.map(plan).join('') + compSec() + costSec() + outSec();
    PEOPLE.forEach(p => refresh(p.pid));
    refreshOut();
  }

  function refresh(pid) {
    const c = S.p[pid].c;
    const t = c ? CH[c] : '未回覆';
    const el = $(`[data-st="${pid}"]`);
    if (el) { el.textContent = t; el.className = `st ${c ? 'conf' : 'none'}`; }
    const ov = $(`[data-ov="${pid}"]`);
    if (ov) ov.textContent = `回饋：${t}`;
  }
  function buildText() {
    const L = ['TASK-CAL-001／M-3｜12 位人設專業寫真拍攝規劃｜Penny 企劃回饋',
      `企劃版本：${P.version}｜頁面版本：${PAGE_COMMIT || '本機預覽（未部署）'}`,
      '說明：這是對拍攝企劃方向的回饋，不是生成授權；也不是照片、月份、版面或印刷核准。', '', '【12 位企劃】'];
    let n = 0;
    PEOPLE.forEach((p, i) => {
      const q = S.p[p.pid];
      if (q.c) n++;
      L.push(`${i + 1}. ${nm(p.pid)}（${p.pid}）｜${p.title}：${q.c ? CH[q.c] : '未回覆'}`);
      if (q.note.trim()) L.push(`   備註：${q.note.trim().replace(/\s*\n\s*/g, '／')}`);
    });
    L.push(`（已回覆 ${n}／${PEOPLE.length} 位）`, '');
    Object.entries(QS).forEach(([k, Q]) => L.push(`【${Q.label}】${S.q[k] ? Q.opts[S.q[k]] : '未回覆'}`));
    L.push(`【整體備註】${S.gnote.trim() ? S.gnote.trim().replace(/\s*\n\s*/g, '／') : '（無）'}`);
    return L.join('\n');
  }
  function refreshOut() {
    const n = PEOPLE.filter(p => S.p[p.pid].c).length;
    $('#bar-count').textContent = `已回覆 ${n}／${PEOPLE.length} 位｜尚未生成任何照片`;
    const ta = $('#out-text');
    if (ta) ta.value = buildText();
  }

  // ---------- 事件 ----------
  app.addEventListener('change', e => {
    const t = e.target;
    if (t.dataset.c) { S.p[t.dataset.c].c = t.value; save(); refresh(t.dataset.c); refreshOut(); }
    else if (t.dataset.q) { S.q[t.dataset.q] = t.value; save(); refreshOut(); }
  });
  app.addEventListener('input', e => {
    const t = e.target;
    if (t.dataset.note) { S.p[t.dataset.note].note = t.value; save(); refreshOut(); }
    else if (t.id === 'gnote') { S.gnote = t.value; save(); refreshOut(); }
  });
  app.addEventListener('click', e => {
    const z = e.target.closest('.zoom');
    if (z) { openViewer(z); return; }
    const cl = e.target.closest('[data-clear]');
    if (cl) {
      const pid = cl.dataset.clear;
      S.p[pid] = { c: '', note: '' };
      save();
      $$(`input[name="c-${pid}"]`).forEach(r => { r.checked = false; });
      $(`#note-${pid}`).value = '';
      refresh(pid); refreshOut();
      toast(`已清除 ${nm(pid)} 的回饋。`);
      return;
    }
    if (e.target.id === 'act-copy') copyOut();
    if (e.target.id === 'act-reset') {
      if (!window.confirm('清除本頁全部回饋？（只清本頁；第二階段素材選擇不受影響）')) return;
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
