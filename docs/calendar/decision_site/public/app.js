// 2027 KOL 桌曆決策頁：畫面、選擇、儲存（只存在本機瀏覽器 localStorage）與複製。
// 不傳送任何資料到伺服器；沒有追蹤或分析。圖片與 ID 都來自 data.js（固定成果 commit 產生）。
'use strict';
(() => {
  const D = window.CAL_DATA;
  const app = document.getElementById('app');
  if (!D) { app.textContent = '資料載入失敗。'; return; }

  const SHA = D.fixed_sha;
  const KEY = 'cal2027-decision-v1:' + SHA;
  const IMG = D.images;
  const MONTHS = D.months;
  const byM = {};
  MONTHS.forEach(x => { byM[x.m] = x; });
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const plain = s => String(s || '').replace(/\*\*/g, '');
  const first = s => String(s).split(' ')[0];
  const pad = n => String(n).padStart(2, '0');
  const PAGE_COMMIT = (() => { const v = ($('meta[name="page-commit"]') || {}).content || ''; return /^[0-9a-f]{7,40}$/.test(v) ? v : ''; })();

  // ---------- 狀態 ----------
  const blank = () => ({ v: {}, conf: {}, confAt: null });
  let storageOK = true;
  function load() {
    try {
      const s = JSON.parse(localStorage.getItem(KEY));
      if (s && typeof s === 'object' && s.v && s.conf) return s;
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

  // ---------- 題目 ----------
  const ppiRange = key => { const a = MONTHS.map(x => x[key].ppi); return `${Math.min(...a)}–${Math.max(...a)}`; };
  const HA = m => byM[m].HA, VU = m => byM[m].VU;
  const OTHER = { key: 'other', code: '另找', title: '都不採用，需另找（請在補充意見說明）', lines: ['本頁新增選項，不是 CAL_10 代碼'] };
  const OPT_SIDE = { '5b': 'H', '5c': 'HV', '7b': 'V', '10b': 'H', '10c': 'HV', '11b': 'V', '12b': 'HV' };
  const SIDE_ZH = { H: '橫式', V: '直式' };

  const ROSTER = { id: 'roster', label: '名單', choices: [
    { key: 'A0', code: 'A0', rec: true, title: '沿用 12 人（5 月 Somi）', imgs: [['roster_A0', 'A0 整組 12 人（封面同一張頭像）']],
      lines: ['1 Iris、2 Kanon、3 Luna、4 Angel、5 Somi、6 Vicky、7 Coco、8 Mia、9 Yuna、10 Tammy、11 Rin、12 Rainie', '名單暫留的理由是目視與展示取捨，不是「已通過辨識度」'] },
    { key: 'A1', code: 'A1', title: '只把 5 月 Somi 換成 Ananya（其餘不變）', imgs: [['roster_A1', 'A1 整組 12 人（5 月換成 Ananya）']],
      lines: ['Ananya 沒有臉部量測，不承諾不會與其他人撞臉', '本輪沒有 Ananya 的版面樣張'] },
  ] };
  const SCALE = { id: 'scale', label: '尺度（整本的方向）', note: '同一個人（Iris）的實際既有照片。尺度是整本的方向：選 B-S1 或 B-S3 時，哪些月份要換圖要下一輪逐張評估，本頁不預先判定。', choices: [
    { key: 'B-S1', code: 'B-S1', title: '日常甜美', imgs: [['tile_iris_V', 'B-S1 例：iris_V 街拍細肩帶＋牛仔短裙']], lines: ['例圖是 1 月直式推薦圖 iris_V'] },
    { key: 'B-S2', code: 'B-S2', rec: true, title: '微性感', imgs: [['tile_iris_H', 'B-S2 例：iris_H 粉色抹胸露肩']], lines: ['目前 12 位的推薦圖多在這一級', '例圖是 1 月橫式推薦圖 iris_H'] },
    { key: 'B-S3', code: 'B-S3', title: '內衣參考', warn: true, imgs: [['tile_scale_S3_ref', 'B-S3 參考：Iris 既有內衣圖（未選作任何月份）']],
      lines: ['未採用，若選擇需再確認廠商接受範圍', '這張只作尺度參考，沒有選作任何月份，沒有圖片 ID'] },
  ] };
  const KANON = { id: 'kanon', label: 'Kanon 造型（2 月；橫直同圖）', choices: [
    { key: 'B-K1', code: 'B-K1', rec: true, cid: 'kanon_alt028', title: '非女僕：#028 碎花洋裝甜點店',
      imgs: [['tile_kanon_alt028', 'kanon_alt028 原照片'], ['H_A_02_kanon-komori', `橫 A 樣張｜${HA(2).ppi} ppi`], ['V_U_02_kanon-komori', `直式統一框樣張｜${VU(2).ppi} ppi`]],
      lines: ['甜美高：碎花洋裝、甜點店、粉紫髮', '性感中低：偏甜不偏性感'] },
    { key: 'B-K2', code: 'B-K2', cid: 'kanon_H', title: '女僕：train_02 女僕咖啡廳',
      imgs: [['tile_kanon_H', 'kanon_H 原照片'], ['CHK_kanon_kanon_H_V_U', `直式統一框樣張｜${D.checks.CHK_kanon_kanon_H_V_U.ppi} ppi`]],
      lines: ['人設本業造型', '黑板假字未處理', '本輪沒有做女僕的橫 A 樣張'] },
  ] };
  const ANGEL = { id: 'angel', label: 'Angel 造型（4 月橫式）', note: '4 月直式不在這題：直式在第二部分選（推薦 angel_V 緞面細肩帶，兩案都用）。', choices: [
    { key: 'B-N1', code: 'B-N1', rec: true, cid: 'angel_H', title: '橫式用護理師 train_02',
      imgs: [['tile_angel_H', 'angel_H 原照片'], ['H_A_04_angel-chiu', `橫 A 樣張｜${HA(4).ppi} ppi`]], lines: ['人設本業造型；性感度低'] },
    { key: 'B-N2', code: 'B-N2', cid: 'angel_alt004', title: '橫式改河岸針織長洋裝 #004',
      imgs: [['tile_angel_alt004', 'angel_alt004 原照片']], lines: ['身形最完整、優雅', '右側兩位男性路人很近，本輪沒有清理', '本輪沒有這張的橫 A 樣張'] },
  ] };
  const vaOf = pid => MONTHS.find(x => x.pid === pid);
  const LAYOUT_H = { id: 'layoutH', label: '橫式版面', choices: [
    { key: 'H_A', code: '橫 A', rec: true, title: '橫 A 半版：左側直幅照片 104×155 mm',
      imgs: [['H_A_01_iris-chen', `Iris 1 月｜橫 A｜${HA(1).ppi} ppi`]], lines: [`12 面 ${ppiRange('HA')} ppi，全部 ≥ 300`, '臉與身形都保得住；右半是月曆'] },
    { key: 'H_B', code: '橫 B', title: '橫 B 大照片 192×104 mm（下方日期條）',
      imgs: [['H_B_01_iris-chen', `Iris 1 月｜橫 B｜${byM[1].HB.ppi} ppi`]], lines: ['橫幅氣勢較強，但多數變成胸上特寫', `12 面 ${ppiRange('HB')} ppi（逐張見下方）`] },
  ] };
  const LAYOUT_V = { id: 'layoutV', label: '直式版面', choices: [
    { key: 'V_U', code: '直式統一框', rec: true, title: '直式統一框 120×128 mm（四周留白）',
      imgs: [['V_U_06_vicky-lin', `Vicky 6 月｜統一框｜${VU(6).ppi} ppi`]], lines: [`12 面 ${ppiRange('VU')} ppi，全部 ≥ 300`] },
    { key: 'V_A', code: '原直 A', title: '原直 A 144×150 mm（上方出血滿版）',
      imgs: [['V_A_06_vicky-lin', `Vicky 6 月｜原直 A｜${vaOf('vicky-lin').VA.ppi} ppi`]], lines: ['直式滿版較有張力，但 ppi 比統一框低', '只有 Iris、Kanon、Vicky、Rin 4 位做了樣張'] },
  ] };
  const GRID9 = { id: 'grid9', label: '9 月大格月曆面的小框照片', note: 'R3 沒有給這題推薦，請 Penny 直接選。', choices: [
    { key: '9b', code: '9b', cid: 'yuna_altsoft', title: '放 Yuna 柔和近照（R3 樣張目前的做法）',
      imgs: [['H_grid_09_yuna-kim', '9 月大格月曆面樣張（小框 48×60 mm）'], ['tile_yuna_altsoft', `yuna_altsoft 小框裁切｜${D.grid9.ppi} ppi`]],
      lines: ['1152 px 寬，只適合小框', '裁到肩上，避開毛衣假字；沒有修圖'] },
    { key: 'none', code: '不放', title: '大格月曆面不放小框照片', lines: ['本頁新增選項，不是 CAL_10 代碼'] },
  ] };
  const FORM_ITEMS = [
    { id: 'recipient', label: '預計給誰看' }, { id: 'brand', label: '品牌名稱' }, { id: 'logo', label: 'Logo' }, { id: 'qr', label: 'QR code' },
  ];
  const isA1 = () => S.v.roster === 'A1';

  function monthChoices(x, side) {
    if (x.m === 5 && isA1()) {
      return [{ key: 'ananya_2', code: 'A1 圖', cid: 'ananya_2', title: 'ananya_2（A1 決策圖所用的圖）',
        imgs: [['tile_ananya_2', 'ananya_2 原照片（R2 比較圖）']], lines: ['本輪沒有 Ananya 的版面樣張與臉部量測；選了之後下一輪才排版'] }, OTHER];
    }
    const p = side === 'H' ? x.HA : x.VU;
    const rec = { key: 'rec', code: '推薦', rec: true, cid: x[side], title: x[side],
      imgs: [[p.page, `${SIDE_ZH[side]}樣張｜${x[side]}｜${p.ppi} ppi`]],
      lines: [p.cleaned ? '已做局部清理（背景、道具或假字）' : '原圖（未清理）', hairNote(p)] };
    const out = [rec];
    for (const o of x.options) {
      const sd = OPT_SIDE[o.code];
      if (!sd || !sd.includes(side)) continue;
      const cid = o.cids[0];
      const imgs = [['tile_' + cid, `${cid} 原照片`]];
      if (cid === 'coco_alt01') imgs.push(['coco_alt01_compare', '手機殼移除：修前／修後（部分完成）']);
      out.push({ key: o.code, code: o.code, cid, title: o.label, imgs,
        lines: [o.note, sd === 'HV' ? 'CAL_10 沒有指定橫或直；在這裡選就表示用在' + SIDE_ZH[side] : '適用：' + SIDE_ZH[side], '本輪沒有這張的版面樣張'] });
    }
    out.push(OTHER);
    return out;
  }
  function hairNote(p) {
    if (/線圈區內/.test(p.hair)) return '髮頂進入線圈區（臉不受影響），待廠商確認線圈位置';
    if (/貼近|很貼近/.test(p.hair_check)) return '髮頂貼近線圈區，待廠商確認線圈位置';
    if (/裁掉/.test(p.hair)) return '髮頂被照片框裁掉（程式判定）';
    return '';
  }
  function monthItems() {
    const out = [];
    for (const x of MONTHS) {
      if (x.m === 2) continue; // 由 Kanon 造型決定
      const sides = x.m === 4 ? ['V'] : ['H', 'V'];
      for (const side of sides) {
        const a1 = x.m === 5 && isA1();
        out.push({ id: `m${pad(x.m)}${side}${a1 ? '_A1' : ''}`, m: x.m, side,
          label: `${x.m} 月 ${a1 ? 'Ananya' : first(x.en)} ${SIDE_ZH[side]}照片`, choices: monthChoices(x, side) });
      }
    }
    return out;
  }
  function allItems() {
    return [ROSTER, SCALE, KANON, ANGEL, LAYOUT_H, LAYOUT_V, ...monthItems(), GRID9, ...FORM_ITEMS];
  }
  const itemById = id => allItems().find(i => i.id === id);

  function answered(id) {
    const v = S.v[id];
    if (v == null || v === '') return false;
    const it = itemById(id);
    if (it && it.choices) return it.choices.some(c => c.key === v);
    if (id === 'recipient') return !!v.k && (v.k !== 'other' || !!(v.text || '').trim());
    if (id === 'brand') return v.k === 'ph' || (v.k === 'name' && !!(v.text || '').trim());
    if (id === 'logo') return ['已有', '尚未提供', '不放'].includes(v);
    if (id === 'qr') return v.k === 'none' || (v.k === 'link' && !!(v.url || '').trim());
    return false;
  }
  function status(id) {
    if (!answered(id)) return 'none';
    return S.conf[id] === JSON.stringify(S.v[id]) ? 'conf' : 'draft';
  }
  const ST_TEXT = { none: '未回答', draft: '草稿・待 Penny 確認', conf: 'Penny 已確認' };
  const ST_TAG = { none: '〔未回答〕', draft: '〔草稿・未確認〕', conf: '〔Penny 已確認〕' };

  // ---------- 畫面元件 ----------
  function fig(iid, cap, cls) {
    const m = IMG[iid];
    if (!m) return `<div class="missing">缺圖 ${esc(iid)}</div>`;
    return `<figure class="fig${cls ? ' ' + cls : ''}"><button type="button" class="zoom" data-img="${esc(iid)}" data-cap="${esc(cap)}" aria-label="放大：${esc(cap)}">` +
      `<img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" loading="lazy" decoding="async" alt="${esc(cap)}"><span class="zi" aria-hidden="true">放大</span></button>` +
      `<figcaption>${esc(cap)}</figcaption></figure>`;
  }
  const stPill = id => `<span class="st" data-st="${esc(id)}"></span>`;
  function choiceHtml(item, c) {
    const id = `${item.id}--${c.key}`;
    const sel = S.v[item.id] === c.key;
    const imgs = c.imgs || [];
    return `<div class="choice${c.rec ? ' rec' : ''}${c.warn ? ' warnc' : ''}${sel ? ' sel' : ''}" data-key="${esc(c.key)}">` +
      (imgs.length ? `<div class="imgs n${Math.min(imgs.length, 3)}">${imgs.map(([i, cap]) => fig(i, cap)).join('')}</div>` : '') +
      `<label class="pick" for="${esc(id)}"><input type="radio" id="${esc(id)}" name="${esc(item.id)}" value="${esc(c.key)}"${sel ? ' checked' : ''}>` +
      `<span><span class="code">${esc(c.code)}</span> ${esc(c.title)}</span></label>` +
      `<div class="badges">${c.rec ? '<span class="badge rec">主管推薦</span>' : ''}${c.cid ? `<span class="badge id">圖片 ID ${esc(c.cid)}</span>` : ''}</div>` +
      ((c.lines || []).filter(Boolean).length ? `<ul class="lines">${c.lines.filter(Boolean).map(l => `<li>${esc(l)}</li>`).join('')}</ul>` : '') +
      `</div>`;
  }
  function groupHtml(item, extra) {
    return `<fieldset class="item" id="item-${esc(item.id)}"><legend>${esc(item.label)} ${stPill(item.id)}</legend>` +
      (item.note ? `<p class="note">${esc(item.note)}</p>` : '') +
      `<div class="choices${item.choices.length <= 2 ? ' two' : ''}">${item.choices.map(c => choiceHtml(item, c)).join('')}</div>${extra || ''}</fieldset>`;
  }

  // ---------- 一、總覽 ----------
  function s1() {
    const hGrid = MONTHS.map(x => fig(x.HA.page, `${x.m} 月 ${first(x.en)}｜${x.H}｜${x.HA.ppi} ppi`)).join('');
    const vGrid = MONTHS.map(x => fig(x.VU.page, `${x.m} 月 ${first(x.en)}｜${x.V}｜${x.VU.ppi} ppi`)).join('');
    return `<section class="sec" id="s1"><h2>一、總覽</h2>
<p class="lead">2027 年桌曆，<b>橫式（200×151 mm）與直式（140×200 mm）兩款都做</b>；12 位不同人設各佔一個月。下面是依主管推薦組合排的工作樣張，點圖可放大（300 dpi 原檔）。</p>
<div class="callout warn">這些都是<b>工作樣張</b>，不是完成稿：每頁角落有「草稿 R3｜未經 Penny 核准」小字，品牌是佔位文字，沒有 Logo、QR。</div>
<h3>兩款封面</h3><div class="grid wide">${fig('H_cover', '橫式封面（12 格頭像；品牌與標語是佔位）')}${fig('V_cover', '直式封面（12 格頭像；品牌與標語是佔位）')}</div>
<h3>12 個月照片面｜橫式（橫 A 半版）</h3><div class="grid">${hGrid}</div>
<h3>12 個月照片面｜直式（統一框 120×128）</h3><div class="grid">${vGrid}</div>
<h3>代表頁：大格月曆面與年曆（各只做了代表）</h3>
<div class="grid wide">${fig('H_grid_09_yuna-kim', '橫式 9 月大格月曆面（代表；含小框照片）')}${fig('V_grid_12_rainie-hsu', '直式 12 月大格月曆面（代表）')}${fig('V_year_2027', '直式全年年曆（最小日期字 7.2 pt）')}${fig('CAL_R3_100pct_V_year_top', '年曆 100% 實際像素（不是印刷證明）')}</div>
<div class="callout"><b>尚未製作</b>（上面的代表頁不代表整本已完成）<ul>
<li>橫式：其餘 11 個大格月曆面、面 26–27 MEMO；面 28 條碼頁由廠商固定。</li>
<li>直式：其餘 11 個大格月曆面、面 26–30 MEMO；面 32 條碼頁由廠商固定。</li></ul></div>
<div class="callout"><b>本頁看不出來的事</b><ul>
<li><b>印刷色彩</b>：螢幕顏色不等於印刷顏色，沒有打樣（Mia 紫光、Rin 暗部、Iris 窗光最需要看）。</li>
<li><b>字體可讀性</b>：螢幕放大看得清楚，不等於印出來看得清楚；年曆最小日期字 7.2 pt 最需要打樣確認。</li>
<li><b>正反面與方向</b>：哪一面印在紙張正面或背面、背面是否旋轉，要等廠商確認；樣張都是單面正向。</li></ul></div>
</section>`;
  }

  // ---------- 二、人選與每月照片 ----------
  function s2() {
    const rosterExtra = `<h4 class="sub">5 月直接比較：Somi（A0）與 Ananya（A1）</h4>
<div class="pair"><div class="grid three-col">${fig('head_somi_V', 'Somi｜somi_V 頭像', 'head')}${fig('tile_somi_V', 'somi_V 原照片')}${fig(byM[5].VU.page, `somi_V 直式統一框樣張｜${byM[5].VU.ppi} ppi`)}</div>
<div class="grid three-col">${fig('head_ananya_2', 'Ananya｜ananya_2 頭像', 'head')}${fig('tile_ananya_2', 'ananya_2 原照片')}<div class="noimg">Ananya 沒有版面樣張，也沒有臉部量測</div></div></div>`;
    return `<section class="sec" id="s2"><h2>二、人選與每月照片</h2>
${groupHtml(ROSTER, rosterExtra)}
<h3>撞臉比較（只用既有資料，本輪沒有新量測）</h3>
<div class="grid wide">${fig('CAL_R2_focus_kanon_somi_tammy', 'Kanon／Somi／Tammy：上三列遮髮、下三列完整頭像', 'tall')}${fig('CAL_R2_focus_iris_rainie', 'Iris／Rainie：上遮髮、下完整頭像', 'tall')}</div>
<ul class="facts">
<li><b>Kanon／Somi／Tammy</b>：既有遮髮量測值（照錄）kanon↔somi 0.02794、kanon↔tammy 0.03646、somi↔tammy 0.04018，都沒有落入既有規則的同框限制（≤ 0.0220）。這<b>不等於</b>看起來夠不同：三人遮髮後骨架很接近，區分有相當比例靠髮色、髮型與妝感。三人分在 2、5、10 月，不相鄰。</li>
<li><b>Iris／Rainie</b>：<b>沒有任何量測</b>。兩位都是黑長直，差異很大一部分來自妝感與表情；Rainie 的比較圖角度大、有閃光，這組目視比較的可信度較低。分在 1 月與 12 月。</li>
<li>沒有量測過的人（包括 Ananya），<b>不能</b>說不會撞臉。</li></ul>
<details class="backup"><summary>備選人選：Wanyin、Sophia、Wendy（不占月份，點開看）</summary>
<p class="note">備選只供參考，本頁不提供直接換人的按鈕；若想換人，請寫在補充意見（例：「Wanyin 替 Rainie」）。</p>
<div class="grid wide">${fig('CAL_R2_decide_people_backup', 'Wanyin、Sophia（R2 備選圖）')}${fig('CAL_R2_decide_people_compare', 'Ananya、Wendy（R2 比較圖）')}</div>
<ul class="facts"><li>Wanyin：黑長直、旗袍古典路線。既有值：與 Rin 0.02234、Kanon 0.02299、Somi 0.02776（未落入 ≤ 0.0220，但很接近）。</li>
<li>Sophia：短捲髮、成熟路線；沒有任何量測。</li>
<li>Wendy：銀灰鮑伯、冷感反差，甜美度較低。與 Batch 3 五位的既有值都 > 0.0220；與其他人沒有量測。</li></ul></details>
<h3>每月照片（H＝橫式、V＝直式；圖片 ID 與 CAL_10 相同）</h3>
<p class="note">推薦圖下方是實際版面樣張；替代圖只有原照片（本輪沒有排版）。「另找」表示這款都不要目前的圖。</p>
<div id="months">${monthsHtml()}</div>
</section>`;
  }
  function monthsHtml() { return MONTHS.map(monthCard).join(''); }
  function monthCard(x) {
    const a1 = x.m === 5 && isA1();
    const items = monthItems().filter(i => i.m === x.m);
    const same = x.H === x.V && !a1;
    const opts = x.options.filter(o => OPT_SIDE[o.code]).map(o => `${o.code} ${o.cids[0]}（${OPT_SIDE[o.code] === 'HV' ? '未指定橫直' : SIDE_ZH[OPT_SIDE[o.code]]}）`);
    let body = '';
    if (x.m === 2) body += derivedKanon();
    if (x.m === 4) body += derivedAngel();
    for (const it of items) body += groupHtml(it);
    if (x.m === 9) body += groupHtml(GRID9);
    const who = a1 ? 'Ananya Kapoor <small>（名單選 A1）</small>' : `${esc(x.en)} ${esc(x.zh)} <small>${esc(x.tag)}</small>`;
    const why = a1 ? '<p class="note">Ananya 只在名單選 A1 時出現：沒有臉部量測，本輪沒有版面樣張。</p>' :
      `<dl class="why"><dt>甜美／氣質</dt><dd>${esc(plain(x.sweet))}</dd><dt>性感與造型</dt><dd>${esc(plain(x.sexy))}</dd></dl>`;
    return `<article class="month" id="month-${x.m}"><h3 class="mh"><span class="mn">${x.m} 月</span> ${who}</h3>${why}` +
      (same ? `<p class="note same">橫直同圖：同一張照片 <code>${esc(x.H)}</code>，下面是它在橫式與直式的實際裁切。</p>` : '') +
      (!a1 && opts.length ? `<p class="note">替代選項：${esc(opts.join('、'))}</p>` : '') + body + `</article>`;
  }
  function derivedKanon() {
    const k = S.v.kanon;
    const st = k ? `目前選 <b>${esc(k)}</b>（${ST_TEXT[status('kanon')]}）` : '目前<b>未回答</b>；推薦 B-K1';
    const figs = k === 'B-K2' ? fig('tile_kanon_H', 'B-K2｜kanon_H 原照片（橫式樣張本輪沒有做）') + fig('CHK_kanon_kanon_H_V_U', 'B-K2｜kanon_H 直式統一框樣張')
      : fig('H_A_02_kanon-komori', `B-K1｜kanon_alt028 橫式樣張｜${HA(2).ppi} ppi`) + fig('V_U_02_kanon-komori', `B-K1｜kanon_alt028 直式樣張｜${VU(2).ppi} ppi`);
    return `<div class="derived"><p>2 月橫直照片由第三部分「<a href="#item-kanon">Kanon 造型</a>」決定：${st}。</p><div class="grid two-col">${figs}</div></div>`;
  }
  function derivedAngel() {
    const k = S.v.angel;
    const st = k ? `目前選 <b>${esc(k)}</b>（${ST_TEXT[status('angel')]}）` : '目前<b>未回答</b>；推薦 B-N1';
    const f = k === 'B-N2' ? fig('tile_angel_alt004', 'B-N2｜angel_alt004 原照片（橫式樣張本輪沒有做）') : fig('H_A_04_angel-chiu', `B-N1｜angel_H 橫式樣張｜${HA(4).ppi} ppi`);
    return `<div class="derived"><p>4 月橫式照片由第三部分「<a href="#item-angel">Angel 造型</a>」決定：${st}。直式照片在下面選。</p><div class="grid two-col">${f}</div></div>`;
  }

  // ---------- 三、尺度與造型 ----------
  function s3() {
    const kref = `<details class="ref"><summary>參考（不可選）：Kanon 另一張女僕圖 kanon_V</summary><div class="grid two-col">${fig('tile_kanon_V', 'kanon_V 原照片（女僕胸口開口 train_01）')}${fig('CHK_kanon_kanon_V_V_U', 'kanon_V 在直式統一框：原圖已缺髮頂')}</div>` +
      `<p class="note">原圖上緣直接切過頭髮，任何框都補不回，只列參考。</p></details>`;
    const afix = `<div class="derived"><p>4 月直式（兩案都用，在第二部分確認）：</p><div class="grid two-col">${fig('tile_angel_V', 'angel_V 原照片（緞面細肩帶）')}${fig('V_U_04_angel-chiu', `angel_V 直式統一框樣張｜${VU(4).ppi} ppi`)}</div></div>`;
    return `<section class="sec" id="s3"><h2>三、尺度與造型</h2>
<p class="note">Kanon 與 Angel 分開選，不用一個「制服總開關」。</p>
${groupHtml(SCALE)}${groupHtml(KANON, kref)}${groupHtml(ANGEL, afix)}</section>`;
  }

  // ---------- 四、版面 ----------
  function s4() {
    const hb = MONTHS.map(x => fig(x.HB.page, `${x.m} 月 ${first(x.en)}｜${x.HB.ppi} ppi${/裁掉/.test(x.HB.hair) ? '｜髮頂被裁' : ''}`)).join('');
    const hbSorted = [...MONTHS].sort((a, b) => b.HB.ppi - a.HB.ppi);
    const groups = {};
    hbSorted.forEach(x => { (groups[x.HB.ppi] = groups[x.HB.ppi] || []).push(first(x.en)); });
    const hbText = Object.keys(groups).sort((a, b) => b - a).map(p => `${groups[p].join('、')} ${p}`).join('；');
    const cut = MONTHS.filter(x => /裁掉/.test(x.HB.hair)).map(x => first(x.en)).join('、');
    const va = MONTHS.filter(x => x.VA).map(x => `<div class="pairbox"><h4>${x.m} 月 ${esc(first(x.en))}</h4><div class="grid two-col">` +
      fig(x.VU.page, `統一框｜${x.VU.ppi} ppi`) + fig(x.VA.page, `原直 A｜${x.VA.ppi} ppi`) + `</div></div>`).join('');
    const hair = [];
    for (const x of MONTHS) {
      for (const [p, lab] of [[x.HA, '橫 A'], [x.VU, '直式統一框'], [x.VA, '原直 A']]) {
        if (!p) continue;
        const n = hairNote(p);
        if (n && !/裁掉/.test(n)) hair.push(`${x.m} 月 ${first(x.en)}（${lab}，${p.cid}）：${n.replace('，待廠商確認線圈位置', '')}`);
      }
    }
    return `<section class="sec" id="s4"><h2>四、版面</h2>
<p class="note">橫式與直式分開選。兩題的組合對應 CAL_10 代碼：橫 A＋統一框＝<b>C1</b>（推薦）；橫 B＋統一框＝<b>C2</b>（只改橫式）；橫 A＋原直 A＝<b>C3</b>（只改直式）。目前組合：<b id="ccode">—</b></p>
${groupHtml(LAYOUT_H)}
<details class="sub"><summary>橫 B 逐張：12 位實際樣張</summary><div class="grid">${hb}</div></details>
<div class="callout"><b>橫 B 的限制（依逐張實際結果）</b><ul>
<li>ppi：${esc(hbText)}。300 ppi 是本專案工作目標，不是廠商已確認的門檻。</li>
<li>髮頂被照片框裁掉：${esc(cut)}（程式判定，未目視）。多數變成胸上特寫，身形變少。</li>
<li>這是逐張結果，不代表整套都要新圖；若選橫 B，哪些月份要改裁切或補圖，下一輪逐月評估（本輪不生成、不外擴）。</li></ul></div>
${groupHtml(LAYOUT_V)}
<details class="sub"><summary>直式：同一人的統一框 vs 原直 A（4 位）</summary><div class="grid wide">${va}</div></details>
<div class="callout"><b>髮頂接近或進入線圈區的頁（待廠商確認，不是印刷安全保證）</b>
<p class="note">線圈區是本專案假設的上緣 12 mm；廠商的實際線圈位置還沒確認。臉都在框內、避開線圈。</p><ul>${hair.map(h => `<li>${esc(h)}</li>`).join('')}</ul></div>
</section>`;
  }

  // ---------- 五、收件對象與品牌 ----------
  function s5() {
    const r = S.v.recipient || {}, b = S.v.brand || {}, q = S.v.qr || {};
    const rad = (name, val, label, cur) => `<label class="opt"><input type="radio" name="${name}" value="${esc(val)}"${cur === val ? ' checked' : ''}> ${esc(label)}</label>`;
    return `<section class="sec" id="s5"><h2>五、收件對象與品牌</h2>
<p class="note">沒有提供前一律用佔位，不自行填品牌或網址。本頁<b>不收檔案</b>，Logo 檔請另外提供。</p>
<fieldset class="item form" id="item-recipient"><legend>預計給誰看 ${stPill('recipient')}</legend>
${rad('recipient', '潛在客戶／合作品牌', '潛在客戶／合作品牌', r.k)}${rad('recipient', '粉絲周邊', '粉絲周邊', r.k)}${rad('recipient', '內部留存', '內部留存', r.k)}${rad('recipient', 'other', '其他：', r.k)}
<input type="text" id="recipient-text" maxlength="200" placeholder="其他對象（選「其他」時填）" value="${esc(r.text || '')}"></fieldset>
<fieldset class="item form" id="item-brand"><legend>品牌名稱 ${stPill('brand')}</legend>
${rad('brand', 'name', '品牌名稱：', b.k)}<input type="text" id="brand-text" maxlength="100" placeholder="輸入品牌名稱" value="${esc(b.text || '')}">
${rad('brand', 'ph', '先用佔位「［品牌名稱 佔位］」', b.k)}</fieldset>
<fieldset class="item form" id="item-logo"><legend>Logo ${stPill('logo')}</legend>
${rad('logo', '已有', '已有（檔案另外提供）', S.v.logo)}${rad('logo', '尚未提供', '尚未提供', S.v.logo)}${rad('logo', '不放', '不放', S.v.logo)}</fieldset>
<fieldset class="item form" id="item-qr"><legend>QR code ${stPill('qr')}</legend>
${rad('qr', 'none', '不放', q.k)}${rad('qr', 'link', '提供連結：', q.k)}<input type="text" id="qr-url" inputmode="url" maxlength="300" placeholder="QR 要連到的網址" value="${esc(q.url || '')}"></fieldset>
<fieldset class="item form" id="item-comments"><legend>補充意見（選填）</legend>
<textarea id="comments" rows="4" maxlength="4000" placeholder="例：想換人、某月想另找圖、對尺度的說明…">${esc(S.v.comments || '')}</textarea></fieldset>
</section>`;
  }

  // ---------- 輸出 ----------
  function sOut() {
    const rows = [
      ['A0', '名單沿用 12 人（主管推薦）', '—'], ['A1', '5 月 Somi 換 Ananya', 'ananya_2'],
      ['B-S1', '尺度：日常甜美', '例 iris_V'], ['B-S2', '尺度：微性感（主管推薦）', '例 iris_H'], ['B-S3', '尺度：內衣（參考，未採用）', '參考圖沒有 ID'],
      ['B-K1', 'Kanon 非女僕，橫直同圖（主管推薦）', 'kanon_alt028'], ['B-K2', 'Kanon 女僕，橫直同圖', 'kanon_H'],
      ['B-N1', 'Angel 橫式護理師（主管推薦）', 'angel_H'], ['B-N2', 'Angel 橫式河岸', 'angel_alt004'],
      ['C1', '橫 A＋直式統一框（主管推薦）', '本頁：橫式版面「橫 A」＋直式版面「直式統一框」'], ['C2', '橫 B＋直式統一框', '本頁：「橫 B」＋「直式統一框」'], ['C3', '橫 A＋原直 A', '本頁：「橫 A」＋「原直 A」'],
      ...MONTHS.flatMap(x => x.options.map(o => [o.code, `${x.m} 月選項`, o.cids.join('、')])),
      ['推薦', '每月推薦圖（主管推薦）', MONTHS.map(x => `${x.m}月 H ${x.H}／V ${x.V}`).join('；')],
      ['另找', '本頁新增：該月該款不採用目前任何圖', '—'], ['不放', '本頁新增：9 月大格面不放小框照片', '—'],
      ['橫／直指定', '本頁新增：5c、10c、12b 在 CAL_10 沒有指定橫直，本頁由 Penny 指定用在哪一款', 'somi_alt065、tammy_alt075、rainie_alt02'],
      ['C2＋C3', '本頁新增說明：橫 B＋原直 A（CAL_10 沒有這個單一代碼）', '—'],
    ];
    return `<section class="sec" id="out"><h2>輸出決策結果</h2>
<div class="callout">選擇只存在這個瀏覽器（localStorage），<b>不會送到伺服器</b>。複製後請<b>貼回 ChatGPT</b>；本頁不會通知主管。<br>「草稿」＝在頁面上選了但還沒按確認；「Penny 已確認」＝按了下面的確認鈕。未回答的項目不會被輸出成核准。</div>
<h3>未回答 <span id="un-n"></span></h3><ul id="unans" class="unans"></ul>
<div class="actions">
<button type="button" class="btn" id="act-rec">套用整組推薦（只填未回答的項目）</button>
<button type="button" class="btn" id="act-confirm">確認目前已回答的選擇（Penny 明確確認）</button>
<button type="button" class="btn" id="act-copy">複製決策結果</button>
<button type="button" class="btn danger" id="act-reset">重設</button></div>
<p class="note" id="conf-at"></p>
<label class="lbl" for="out-text">將複製的文字（預覽，會隨選擇更新）</label>
<textarea id="out-text" rows="16" readonly></textarea>
<details class="sub"><summary>代碼與圖片 ID 對照表</summary><div class="tbl"><table><thead><tr><th>代碼</th><th>內容</th><th>圖片 ID／本頁對應</th></tr></thead><tbody>
${rows.map(r => `<tr><td>${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join('')}</tbody></table></div></details>
</section>`;
  }

  // ---------- 輸出文字 ----------
  function choiceOf(id) { const it = itemById(id); return it && it.choices ? it.choices.find(c => c.key === S.v[id]) : null; }
  function line(id, fmt) { const st = status(id); return st === 'none' ? `未回答${ST_TAG.none}` : `${fmt()}${ST_TAG[st]}`; }
  function cCode() {
    const h = answered('layoutH') ? S.v.layoutH : null, v = answered('layoutV') ? S.v.layoutV : null;
    if (!h || !v) return null;
    if (h === 'H_A' && v === 'V_U') return 'C1';
    if (h === 'H_B' && v === 'V_U') return 'C2';
    if (h === 'H_A' && v === 'V_A') return 'C3';
    return 'C2＋C3 組合（CAL_10 沒有這個單一代碼）';
  }
  function monthText(it) {
    const c = choiceOf(it.id);
    if (!c) return '';
    if (c.key === 'rec') return `${c.cid}（推薦）`;
    if (c.key === 'other') return '另找（不採用目前任何圖，見補充意見）';
    return `${c.code} ${c.cid}`;
  }
  function buildText() {
    const items = allItems();
    const cnt = { none: 0, draft: 0, conf: 0 };
    items.forEach(i => { cnt[status(i.id)] += 1; });
    const t = [];
    const C = (id, f) => line(id, f);
    const ch = id => choiceOf(id);
    t.push('【2027 KOL 桌曆決策結果】（由決策頁產生；請貼回 ChatGPT）');
    t.push(`基準成果 SHA：${SHA}`);
    t.push(`決策頁版本：${PAGE_COMMIT || '未知（本機預覽）'}`);
    t.push(`產生時間：${new Date().toLocaleString('zh-TW', { hour12: false })}（瀏覽器時間）`);
    t.push(`狀態：Penny 已確認 ${cnt.conf} 項｜草稿・未確認 ${cnt.draft} 項｜未回答 ${cnt.none} 項`);
    if (S.confAt) t.push(`最近一次按下確認：${new Date(S.confAt).toLocaleString('zh-TW', { hour12: false })}`);
    t.push('※ 草稿＝頁面上選了但尚未按確認。未回答不代表核准，也不代表沿用推薦。此結果不是主管核准，也不是印刷或廠商核准。');
    t.push('');
    t.push('一、名單：' + C('roster', () => S.v.roster === 'A0' ? 'A0 沿用 12 人（5 月 Somi）' : 'A1 5 月改 Ananya（ananya_2；無臉部量測、無樣張）'));
    t.push('二、尺度：' + C('scale', () => `${ch('scale').code} ${ch('scale').title}${ch('scale').rec ? '（主管推薦）' : ''}${S.v.scale === 'B-S3' ? '（未採用的參考級；需再確認廠商接受範圍）' : ''}`));
    t.push('三、Kanon 造型：' + C('kanon', () => `${ch('kanon').code} ${ch('kanon').cid} ${ch('kanon').title}${ch('kanon').rec ? '（主管推薦）' : ''}`));
    t.push('四、Angel 造型：' + C('angel', () => `${ch('angel').code} ${ch('angel').cid} ${ch('angel').title}${ch('angel').rec ? '（主管推薦）' : ''}`));
    t.push('五、橫式版面：' + C('layoutH', () => `${ch('layoutH').code}｜${ch('layoutH').title}${ch('layoutH').rec ? '（主管推薦）' : ''}`));
    t.push('六、直式版面：' + C('layoutV', () => `${ch('layoutV').code}｜${ch('layoutV').title}${ch('layoutV').rec ? '（主管推薦）' : ''}`));
    t.push('　→ 對應 CAL_10 版面代碼：' + (cCode() || '未定（橫式或直式版面未回答）'));
    t.push('七、逐月照片（H＝橫式、V＝直式；圖片 ID 同 CAL_10）');
    const mi = monthItems();
    const changes = [];
    for (const x of MONTHS) {
      const a1 = x.m === 5 && isA1();
      const name = a1 ? 'Ananya（A1）' : first(x.en);
      let s;
      if (x.m === 2) {
        s = S.v.kanon && answered('kanon') ? `H／V 依 Kanon 造型 ${S.v.kanon} → ${ch('kanon').cid}${ST_TAG[status('kanon')]}` : `H／V 依 Kanon 造型（未回答）${ST_TAG.none}`;
      } else {
        const parts = [];
        if (x.m === 4) parts.push(answered('angel') ? `H 依 Angel 造型 ${S.v.angel} → ${ch('angel').cid}${ST_TAG[status('angel')]}` : `H 依 Angel 造型（未回答）${ST_TAG.none}`);
        for (const it of mi.filter(i => i.m === x.m)) {
          parts.push(`${it.side} ${line(it.id, () => monthText(it))}`);
          if (answered(it.id) && S.v[it.id] !== 'rec') changes.push(`${x.m} 月 ${it.side}＝${monthText(it)}${ST_TAG[status(it.id)]}`);
        }
        s = parts.join('｜');
      }
      t.push(`　${x.m} 月 ${name}：${s}`);
    }
    t.push('　9 月大格月曆面小框：' + C('grid9', () => S.v.grid9 === '9b' ? '9b yuna_altsoft' : '不放（本頁新增選項）'));
    if (answered('kanon') && S.v.kanon !== 'B-K1') changes.unshift(`2 月 H／V＝${S.v.kanon} ${ch('kanon').cid}`);
    if (answered('angel') && S.v.angel !== 'B-N1') changes.unshift(`4 月 H＝${S.v.angel} ${ch('angel').cid}`);
    t.push('　與每月推薦不同的地方：' + (changes.length ? changes.join('；') : '無（只計已回答項目）'));
    t.push('八、收件對象與品牌');
    const r = S.v.recipient || {}, b = S.v.brand || {}, q = S.v.qr || {};
    t.push('　預計給誰看：' + C('recipient', () => r.k === 'other' ? `其他：${r.text.trim()}` : r.k));
    t.push('　品牌名稱：' + C('brand', () => b.k === 'ph' ? '先用佔位「［品牌名稱 佔位］」' : b.text.trim()));
    t.push('　Logo：' + C('logo', () => S.v.logo));
    t.push('　QR：' + C('qr', () => q.k === 'none' ? '不放' : `提供連結：${q.url.trim()}`));
    t.push('九、補充意見：' + ((S.v.comments || '').trim() || '（無）'));
    const un = items.filter(i => status(i.id) === 'none').map(i => i.label);
    t.push('十、未回答清單：' + (un.length ? un.join('、') : '無'));
    const codes = [];
    if (answered('roster')) codes.push(S.v.roster);
    if (answered('scale')) codes.push(S.v.scale);
    if (answered('kanon')) codes.push(S.v.kanon);
    if (answered('angel')) codes.push(S.v.angel);
    if (cCode()) codes.push(cCode());
    t.push('');
    t.push('代碼摘要（只列已回答）：' + (codes.length ? codes.join('＋') : '無') + '；逐月修改：' + (changes.length ? changes.join('；') : '無'));
    return t.join('\n');
  }

  // ---------- 更新 ----------
  function refresh() {
    const items = allItems();
    $$('[data-st]').forEach(el => { const s = status(el.dataset.st); el.className = 'st ' + s; el.textContent = ST_TEXT[s]; });
    $$('.choice').forEach(el => {
      const name = el.querySelector('input[type=radio]');
      el.classList.toggle('sel', !!name && name.checked);
    });
    const cnt = { none: 0, draft: 0, conf: 0 };
    items.forEach(i => { cnt[status(i.id)] += 1; });
    $('#bar-count').textContent = `未回答 ${cnt.none}｜草稿 ${cnt.draft}｜已確認 ${cnt.conf}`;
    const un = items.filter(i => status(i.id) === 'none');
    $('#un-n').textContent = `（${un.length} 項）`;
    $('#unans').innerHTML = un.length ? un.map(i => `<li><a href="#item-${esc(i.id)}">${esc(i.label)}</a></li>`).join('') : '<li>沒有未回答的項目。</li>';
    const cc = cCode();
    $('#ccode').textContent = cc || '未定';
    $('#conf-at').textContent = S.confAt ? `最近一次確認：${new Date(S.confAt).toLocaleString('zh-TW', { hour12: false })}（確認後再修改的項目會變回草稿）` : '尚未按過確認：目前所有選擇都是草稿。';
    $('#out-text').value = buildText();
  }
  function rerenderMonths() { $('#months').innerHTML = monthsHtml(); }

  function render() {
    $('#sha').textContent = SHA;
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    app.innerHTML = s1() + s2() + s3() + s4() + s5() + sOut();
    refresh();
  }

  // ---------- 事件 ----------
  let saveTimer = null;
  const saveSoon = () => { clearTimeout(saveTimer); saveTimer = setTimeout(save, 300); };
  const FORM_RADIO = { recipient: v => ({ k: v, text: ($('#recipient-text').value || '') }), brand: v => ({ k: v, text: $('#brand-text').value || '' }),
    qr: v => ({ k: v, url: $('#qr-url').value || '' }), logo: v => v };
  app.addEventListener('change', e => {
    const el = e.target;
    if (!(el instanceof HTMLInputElement) || el.type !== 'radio') return;
    const name = el.name;
    S.v[name] = FORM_RADIO[name] ? FORM_RADIO[name](el.value) : el.value;
    save();
    if (name === 'roster' || name === 'kanon' || name === 'angel') rerenderMonths();
    refresh();
  });
  const TEXT_FIELDS = { 'recipient-text': ['recipient', 'other', 'text'], 'brand-text': ['brand', 'name', 'text'], 'qr-url': ['qr', 'link', 'url'] };
  app.addEventListener('input', e => {
    const el = e.target;
    if (el.id === 'comments') { S.v.comments = el.value; saveSoon(); refresh(); return; }
    const f = TEXT_FIELDS[el.id];
    if (!f) return;
    const [id, k, field] = f;
    const cur = S.v[id] && typeof S.v[id] === 'object' ? S.v[id] : {};
    S.v[id] = { ...cur, k, [field]: el.value };
    const radio = $(`input[name="${id}"][value="${k}"]`);
    if (radio) radio.checked = true;
    saveSoon();
    refresh();
  });
  app.addEventListener('click', e => {
    const z = e.target.closest('.zoom');
    if (z) { openViewer(z); return; }
    const b = e.target.closest('button');
    if (!b) return;
    if (b.id === 'act-rec') applyRec();
    if (b.id === 'act-confirm') confirmAll();
    if (b.id === 'act-copy') copyOut();
    if (b.id === 'act-reset') resetAll();
  });
  $('#bar-copy').addEventListener('click', copyOut);

  function applyRec() {
    const items = allItems().filter(i => i.choices && i.choices.some(c => c.rec));
    const todo = items.filter(i => !answered(i.id));
    if (!todo.length) { toast('所有有推薦的項目都已回答，沒有要填的。'); return; }
    if (!window.confirm(`會把 ${todo.length} 個「未回答」且有主管推薦的項目填成推薦（草稿）。已選的項目不會被改。\n收件對象、品牌、Logo、QR 與 9 月小框沒有推薦，仍需自己選。\n填好後仍要按「確認」才算 Penny 確認。要繼續嗎？`)) return;
    let rosterChanged = false;
    for (const i of todo) { S.v[i.id] = i.choices.find(c => c.rec).key; if (i.id === 'roster') rosterChanged = true; }
    // 名單變成 A0 後，5 月改用 Somi 的題目；再補一次推薦
    if (rosterChanged) for (const i of allItems().filter(x => x.choices && x.choices.some(c => c.rec))) if (!answered(i.id)) S.v[i.id] = i.choices.find(c => c.rec).key;
    save();
    rerenderMonths();
    $$('#app input[type=radio]').forEach(r => { r.checked = S.v[r.name] === r.value || (S.v[r.name] && S.v[r.name].k === r.value); });
    refresh();
    toast('已填入推薦（草稿）。請檢查後按「確認」。');
  }
  function confirmAll() {
    const items = allItems().filter(i => answered(i.id));
    const un = allItems().filter(i => !answered(i.id)).length;
    if (!items.length) { toast('還沒有任何已回答的項目。'); return; }
    if (!window.confirm(`確認後，目前已回答的 ${items.length} 項會標為「Penny 已確認」。\n未回答的 ${un} 項仍是未回答，不會被當成核准。\n要確認嗎？`)) return;
    for (const i of items) S.conf[i.id] = JSON.stringify(S.v[i.id]);
    S.confAt = new Date().toISOString();
    save();
    refresh();
    toast('已確認。記得按「複製決策結果」貼回 ChatGPT。');
  }
  function resetAll() {
    if (!window.confirm('清除這個瀏覽器裡的所有選擇與確認紀錄？此動作無法復原。')) return;
    try { localStorage.removeItem(KEY); } catch (e) { /* 無法存取時只清記憶體 */ }
    S = blank();
    render();
    toast('已重設。');
  }
  async function copyOut() {
    const text = buildText();
    const ta = $('#out-text');
    ta.value = text;
    const done = '已複製。請貼回 ChatGPT；本頁不會通知主管。';
    try {
      await navigator.clipboard.writeText(text);
      toast(done);
    } catch (e) {
      ta.focus();
      ta.select();
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
    vimg.src = m.z;
    vimg.width = m.w;
    vimg.height = m.h;
    vimg.alt = btn.dataset.cap;
    vcap.textContent = `${btn.dataset.cap}（${m.w}×${m.h} px；${m.kind === 'crop' ? '裁自' : '原檔'} ${m.src.replace('docs/calendar/', '')}）`;
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
    if (lastBtn) lastBtn.focus({ preventScroll: true });
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
