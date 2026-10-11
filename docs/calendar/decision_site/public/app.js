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
  const HI = D.hires_of || {};
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
  const LOWRES_NOTE = '低解析選圖參考；細節與印刷採用待原圖／排版覆核';
  const RES_BADGE = { page300: '300 dpi 樣張', preview100: '100% 預覽', sheet: '比較圖', lowres: '低解析', hires: '高解析預覽' };

  // ---------- 狀態 ----------
  // S.v：目前的值；S.conf[id] = { v: 確認當下的值, at }。任何變更都會刪掉該項的確認（改回舊值也一樣），要再按確認。
  const blank = () => ({ v: {}, conf: {}, confAt: null });
  let storageOK = true;
  function load() {
    try {
      const s = JSON.parse(localStorage.getItem(KEY));
      if (s && typeof s === 'object' && s.v && s.conf) {
        for (const k of Object.keys(s.conf)) if (typeof s.conf[k] === 'string') s.conf[k] = { v: s.conf[k] };
        return s;
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
  function setVal(id, val) {
    S.v[id] = val;
    delete S.conf[id];
  }

  // ---------- 題目 ----------
  const ppiRange = key => { const a = MONTHS.map(x => x[key].ppi); return `${Math.min(...a)}–${Math.max(...a)}`; };
  const HA = m => byM[m].HA, VU = m => byM[m].VU;
  const OTHER = { key: 'other', code: '另找', title: '都不採用，需另找（請在補充意見說明）', lines: ['本頁新增選項，不是 CAL_10 代碼'] };
  const OPT_SIDE = { '5b': 'H', '5c': 'HV', '7b': 'V', '10b': 'H', '10c': 'HV', '11b': 'V', '12b': 'HV' };
  const SIDE_ZH = { H: '橫式', V: '直式' };
  const LAYOUT_ZH = { H_A: '橫 A', H_B: '橫 B', V_U: '直式統一框', V_A: '原直 A' };
  const photoOf = cid => HI[cid] || (IMG['tile_' + cid] ? 'tile_' + cid : null);

  // 現有樣張：版面｜月份｜圖片 ID → 樣張頁（沒有就是「尚未排版」）
  const MOCK = {};
  for (const x of MONTHS) {
    MOCK[`H_A|${x.m}|${x.HA.cid}`] = x.HA.page;
    MOCK[`H_B|${x.m}|${x.HB.cid}`] = x.HB.page;
    MOCK[`V_U|${x.m}|${x.VU.cid}`] = x.VU.page;
    if (x.VA) MOCK[`V_A|${x.m}|${x.VA.cid}`] = x.VA.page;
  }
  MOCK['V_U|2|kanon_H'] = 'CHK_kanon_kanon_H_V_U';

  const ROSTER = { id: 'roster', label: '名單', choices: [
    { key: 'A0', code: 'A0', rec: true, title: '沿用 12 人（5 月 Somi）', imgs: [['roster_A0', 'A0 整組 12 人（封面同一張頭像）']],
      lines: ['1 Iris、2 Kanon、3 Luna、4 Angel、5 Somi、6 Vicky、7 Coco、8 Mia、9 Yuna、10 Tammy、11 Rin、12 Rainie', '名單暫留的理由是目視與展示取捨，不是「已通過辨識度」'] },
    { key: 'A1', code: 'A1', title: '只把 5 月 Somi 換成 Ananya（其餘不變）', imgs: [['roster_A1', 'A1 整組 12 人（5 月換成 Ananya）']],
      lines: ['Ananya 沒有臉部量測，不承諾不會與其他人撞臉', 'Ananya 尚未排版（沒有樣張）'] },
  ] };
  const SCALE = { id: 'scale', label: '尺度（整本的方向）', note: '同一個人（Iris）的實際既有照片。尺度是整本的方向：選 B-S1 或 B-S3 時，哪些月份要換圖要下一輪逐張評估，本頁不預先判定。', choices: [
    { key: 'B-S1', code: 'B-S1', title: '日常甜美', imgs: [['tile_iris_V', 'B-S1 例：iris_V 街拍細肩帶＋牛仔短裙']], lines: ['例圖是 1 月直式推薦圖 iris_V'] },
    { key: 'B-S2', code: 'B-S2', rec: true, title: '微性感', imgs: [['tile_iris_H', 'B-S2 例：iris_H 粉色抹胸露肩']], lines: ['目前 12 位的推薦圖多在這一級', '例圖是 1 月橫式推薦圖 iris_H'] },
    { key: 'B-S3', code: 'B-S3', title: '內衣參考', warn: true, imgs: [['tile_scale_S3_ref', 'B-S3 參考：Iris 既有內衣圖（未選作任何月份）']],
      lines: ['未採用，若選擇需再確認廠商接受範圍', '這張只作尺度參考，沒有選作任何月份，沒有圖片 ID'] },
  ] };
  const KANON = { id: 'kanon', label: 'Kanon 造型（2 月；橫直同圖）', choices: [
    { key: 'B-K1', code: 'B-K1', rec: true, cid: 'kanon_alt028', title: '非女僕：#028 碎花洋裝甜點店',
      imgs: [['H_A_02_kanon-komori', `固定推薦樣張｜橫 A｜${HA(2).ppi} ppi`], ['V_U_02_kanon-komori', `固定推薦樣張｜直式統一框｜${VU(2).ppi} ppi`]],
      lines: ['甜美高：碎花洋裝、甜點店、粉紫髮', '性感中低：偏甜不偏性感'] },
    { key: 'B-K2', code: 'B-K2', cid: 'kanon_H', title: '女僕：train_02 女僕咖啡廳',
      imgs: [[HI.kanon_H, 'kanon_H 原照片高解析預覽（未排版）'], ['CHK_kanon_kanon_H_V_U', `直式統一框樣張｜${D.checks.CHK_kanon_kanon_H_V_U.ppi} ppi`]],
      lines: ['人設本業造型', '橫式：此選擇尚未排版（沒有做女僕的橫 A／橫 B 樣張）', '直式統一框：有樣張', '黑板假字未處理'] },
  ] };
  const ANGEL = { id: 'angel', label: 'Angel 造型（4 月橫式）', note: '4 月直式不在這題：直式在第二部分 4 月卡片確認（推薦 angel_V 緞面細肩帶，兩案都用）。', choices: [
    { key: 'B-N1', code: 'B-N1', rec: true, cid: 'angel_H', title: '橫式用護理師 train_02',
      imgs: [['H_A_04_angel-chiu', `固定推薦樣張｜橫 A｜${HA(4).ppi} ppi`]], lines: ['人設本業造型；性感度低'] },
    { key: 'B-N2', code: 'B-N2', cid: 'angel_alt004', title: '橫式改河岸針織長洋裝 #004',
      imgs: [[HI.angel_alt004, 'angel_alt004 原照片高解析預覽（未排版）']], lines: ['身形最完整、優雅', '右側兩位男性路人很近，本輪沒有清理', '橫式：此選擇尚未排版'] },
  ] };
  const vaOf = pid => MONTHS.find(x => x.pid === pid);
  const LAYOUT_H = { id: 'layoutH', label: '橫式版面', choices: [
    { key: 'H_A', code: '橫 A', rec: true, title: '橫 A 半版：左側直幅照片 104×155 mm',
      imgs: [['H_A_01_iris-chen', `範例：Iris 1 月｜橫 A｜${HA(1).ppi} ppi`]], lines: [`12 面 ${ppiRange('HA')} ppi，全部 ≥ 300`, '臉與身形都保得住；右半是月曆'] },
    { key: 'H_B', code: '橫 B', title: '橫 B 大照片 192×104 mm（下方日期條）',
      imgs: [['H_B_01_iris-chen', `範例：Iris 1 月｜橫 B｜${byM[1].HB.ppi} ppi`]], lines: ['橫幅氣勢較強，但多數變成胸上特寫', `12 位推薦照片都有橫 B 樣張：${ppiRange('HB')} ppi（逐張見下方）`, '替代照片在橫 B 沒有樣張'] },
  ] };
  const LAYOUT_V = { id: 'layoutV', label: '直式版面', choices: [
    { key: 'V_U', code: '直式統一框', rec: true, title: '直式統一框 120×128 mm（四周留白）',
      imgs: [['V_U_06_vicky-lin', `範例：Vicky 6 月｜統一框｜${VU(6).ppi} ppi`]], lines: [`12 面 ${ppiRange('VU')} ppi，全部 ≥ 300`] },
    { key: 'V_A', code: '原直 A', title: '原直 A 144×150 mm（上方出血滿版）',
      imgs: [['V_A_06_vicky-lin', `範例：Vicky 6 月｜原直 A｜${vaOf('vicky-lin').VA.ppi} ppi`]], lines: ['直式滿版較有張力，但 ppi 比統一框低', '只有 Iris、Kanon、Vicky、Rin 4 位有樣張；其他月份會顯示「尚未排版」'] },
  ] };
  const GRID9 = { id: 'grid9', label: '9 月大格月曆面的小框照片', note: '主管覆核後補推薦 9b。', choices: [
    { key: '9b', code: '9b', rec: true, cid: 'yuna_altsoft', title: '放 Yuna 柔和近照小框',
      imgs: [['H_grid_09_yuna-kim', '固定推薦樣張｜9 月大格月曆面（小框 48×60 mm）'], ['CAL_R3_100pct_H_grid_09_small_photo', `小框 100% 實際像素｜${D.grid9.ppi} ppi`]],
      lines: ['主管推薦理由：在清冷主照片之外補充甜美表情，並利用既有合格小框樣張', '1152 px 寬，只適合小框；裁到肩上，避開毛衣假字；沒有修圖'] },
    { key: 'none', code: '不放', title: '大格月曆面不放小框照片', lines: ['本頁新增選項，不是 CAL_10 代碼', '此選擇尚未排版（目前樣張含小框）'] },
  ] };
  const FORM_ITEMS = [
    { id: 'recipient', label: '預計給誰看' }, { id: 'brand', label: '品牌名稱' }, { id: 'logo', label: 'Logo' }, { id: 'qr', label: 'QR code' },
  ];
  const isA1 = () => S.v.roster === 'A1';

  function monthChoices(x, side) {
    if (x.m === 5 && isA1()) {
      return [{ key: 'ananya_2', code: 'A1 圖', cid: 'ananya_2', title: 'ananya_2（A1 決策圖所用的圖）',
        imgs: [[HI.ananya_2, 'ananya_2 原照片高解析預覽（未排版）']], lines: ['此選擇尚未排版；沒有臉部量測'] }, OTHER];
    }
    const p = side === 'H' ? x.HA : x.VU;
    const rec = { key: 'rec', code: '推薦', rec: true, cid: x[side], title: x[side],
      imgs: [[p.page, `固定推薦樣張｜${LAYOUT_ZH[side === 'H' ? 'H_A' : 'V_U']}｜${p.ppi} ppi`]],
      lines: [p.cleaned ? '已做局部清理（背景、道具或假字）' : '原圖（未清理）', hairNote(p)] };
    const out = [rec];
    for (const o of x.options) {
      const sd = OPT_SIDE[o.code];
      if (!sd || !sd.includes(side)) continue;
      const cid = o.cids[0];
      const ph = photoOf(cid);
      const imgs = ph ? [[ph, `${cid} 原照片${HI[cid] ? '高解析預覽' : ''}（未排版）`]] : [];
      if (cid === 'coco_alt01') imgs.push(['coco_alt01_compare', '手機殼移除：修前／修後（部分完成）']);
      out.push({ key: o.code, code: o.code, cid, title: o.label, imgs,
        lines: [o.note, sd === 'HV' ? 'CAL_10 沒有指定橫或直；在這裡選就表示用在' + SIDE_ZH[side] : '適用：' + SIDE_ZH[side], '此選擇尚未排版'] });
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
    const c = S.conf[id];
    return c && c.v === JSON.stringify(S.v[id]) ? 'conf' : 'draft';
  }
  const ST_TEXT = { none: '未回答', draft: '草稿・待 Penny 確認', conf: 'Penny 已確認' };
  const ST_TAG = { none: '〔未回答〕', draft: '〔草稿・未確認〕', conf: '〔Penny 已確認〕' };
  const choiceOf = id => { const it = itemById(id); return it && it.choices ? it.choices.find(c => c.key === S.v[id]) : null; };

  // ---------- 目前選擇（每月每款） ----------
  function effLayout(side) {
    const id = side === 'H' ? 'layoutH' : 'layoutV';
    return answered(id) ? { key: S.v[id], def: false } : { key: side === 'H' ? 'H_A' : 'V_U', def: true };
  }
  // 回傳 { st, cid, text, isRec, other }
  function curChoice(x, side) {
    let id;
    if (x.m === 2) id = 'kanon';
    else if (x.m === 4 && side === 'H') id = 'angel';
    else id = `m${pad(x.m)}${side}${x.m === 5 && isA1() ? '_A1' : ''}`;
    const st = status(id);
    if (st === 'none') return { st, id };
    const c = choiceOf(id);
    if (c.key === 'other') return { st, id, other: true, text: '另找' };
    const isRec = !!c.rec;
    const text = (id === 'kanon' || id === 'angel') ? `${c.code}（${c.cid}）` : (c.key === 'rec' ? `${c.cid}（推薦）` : `${c.code} ${c.cid}`);
    return { st, id, cid: c.cid, isRec, text };
  }
  function laidOut(x, side, cid) {
    const lay = effLayout(side);
    return { lay, page: MOCK[`${lay.key}|${x.m}|${cid}`] || null };
  }
  function curSideHtml(x, side) {
    const c = curChoice(x, side);
    let body;
    if (c.st === 'none') body = '<p class="cur-none">尚未選擇（可按「套用推薦為草稿」，或展開下方「修改這個月」）</p>';
    else if (c.other) body = '<p class="cur-none">另找：目前沒有對應照片</p>';
    else {
      const { lay, page } = laidOut(x, side, c.cid);
      const recPage = side === 'H' ? x.HA.page : x.VU.page;
      const layNote = `<p class="note">版面：${esc(LAYOUT_ZH[lay.key])}${lay.def ? '（版面還沒選，先以推薦版面判斷）' : ''}</p>`;
      if (page && page === recPage) body = `<p class="cur-same">＝ 上面的推薦樣張</p>${layNote}`;
      else if (page) body = fig(page, `目前選擇的樣張｜${LAYOUT_ZH[lay.key]}｜${c.cid}`) + layNote;
      else {
        const ph = photoOf(c.cid);
        body = `<p class="notlaid">此選擇尚未排版</p>${layNote}` + (ph ? fig(ph, `${c.cid} 原照片${HI[c.cid] ? '高解析預覽' : ''}（未排版）`) : '');
      }
    }
    const val = c.st === 'none' ? '—' : esc(c.text);
    return `<div class="cur-side"><div class="cur-h"><b>${SIDE_ZH[side]}</b> <span class="st ${c.st}">${ST_TEXT[c.st]}</span> <span class="cur-v">${val}</span></div>${body}</div>`;
  }
  function curGrid9Html() {
    const st = status('grid9');
    const v = S.v.grid9;
    const body = st === 'none' ? '<p class="cur-none">尚未選擇</p>' : (v === '9b' ? '<p class="cur-same">＝ 推薦樣張（9 月大格面含小框）</p>' : '<p class="notlaid">不放小框：此選擇尚未排版（目前樣張含小框）</p>');
    return `<div class="cur-side"><div class="cur-h"><b>9 月大格面小框</b> <span class="st ${st}">${ST_TEXT[st]}</span> <span class="cur-v">${st === 'none' ? '—' : esc(v === '9b' ? '9b yuna_altsoft' : '不放')}</span></div>${body}</div>`;
  }
  function curHtml(x) {
    const sides = ['H', 'V'].map(s => curSideHtml(x, s)).join('');
    return `<h4>目前選擇</h4><div class="cur-grid">${sides}${x.m === 9 ? curGrid9Html() : ''}</div>`;
  }

  // ---------- 畫面元件 ----------
  function fig(iid, cap, cls) {
    const m = IMG[iid];
    if (!m) return `<div class="missing">缺圖 ${esc(iid)}</div>`;
    return `<figure class="fig${cls ? ' ' + cls : ''}"><button type="button" class="zoom" data-img="${esc(iid)}" data-cap="${esc(cap)}" aria-label="放大：${esc(cap)}">` +
      `<img src="${esc(m.t)}" width="${m.tw}" height="${m.th}" loading="lazy" decoding="async" alt="${esc(cap)}">` +
      `<span class="resb ${esc(m.res)}">${esc(RES_BADGE[m.res] || '')}</span><span class="zi" aria-hidden="true">放大</span></button>` +
      `<figcaption>${esc(cap)}${m.res === 'lowres' ? `<span class="resnote">${LOWRES_NOTE}</span>` : ''}</figcaption></figure>`;
  }
  const stPill = id => `<span class="st" data-st="${esc(id)}"></span>`;
  function choiceHtml(item, c) {
    const id = `${item.id}--${c.key}`;
    const sel = S.v[item.id] === c.key;
    const imgs = (c.imgs || []).filter(i => i[0]);
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

  // ---------- 摘要與步驟 ----------
  function sQuick() {
    return `<section class="sec quick" id="quick"><h2>決策摘要與步驟</h2>
<ol class="steps">
<li><a href="#s1">先看整組推薦</a>：第一部分全部是主管推薦組合的固定樣張。</li>
<li>按「<b>套用推薦為草稿</b>」：有推薦的項目一次填好，仍是草稿，不算核准。</li>
<li>只改例外：各月卡片的「修改這個月」，或第三、四部分的尺度、造型、版面。</li>
<li>在下面檢查摘要與修改清單。</li>
<li>按「<b>確認目前已選的項目</b>」：品牌等還沒填的維持未回答，不影響複製。</li>
<li>按「<b>複製決策結果</b>」，貼回 ChatGPT（本頁不會通知主管）。</li></ol>
<div class="actions">
<button type="button" class="btn" id="act-rec">套用推薦為草稿</button>
<button type="button" class="btn" id="act-confirm">確認目前已選的項目</button>
<button type="button" class="btn" id="act-copy">複製決策結果</button></div>
<p class="note" id="conf-at"></p>
<h3>目前選擇摘要</h3><div class="tbl"><table class="sum"><thead><tr><th>項目</th><th>目前選擇</th><th>狀態</th></tr></thead><tbody id="summary"></tbody></table></div>
<h3>與推薦不同的地方</h3><ul id="changes" class="changes"></ul>
<h3>未回答 <span id="un-n"></span></h3><ul id="unans" class="unans"></ul>
</section>`;
  }

  // ---------- 一、總覽 ----------
  function s1() {
    const hGrid = MONTHS.map(x => fig(x.HA.page, `${x.m} 月 ${first(x.en)}｜${x.H}｜${x.HA.ppi} ppi`)).join('');
    const vGrid = MONTHS.map(x => fig(x.VU.page, `${x.m} 月 ${first(x.en)}｜${x.V}｜${x.VU.ppi} ppi`)).join('');
    return `<section class="sec" id="s1"><h2>一、總覽</h2>
<p class="lead">2027 年桌曆，<b>橫式（200×151 mm）與直式（140×200 mm）兩款都做</b>；12 位不同人設各佔一個月。</p>
<div class="callout warn">以下全部是<b>主管推薦組合的固定樣張</b>，<b>不會隨你的選擇改變</b>；你改選後的結果請看各月卡片的「目前選擇」。這些是工作樣張，不是完成稿：每頁角落有「草稿 R3｜未經 Penny 核准」小字，品牌是佔位文字，沒有 Logo、QR。樣張頁可放大看 300 dpi 原檔。</div>
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
<div class="pair"><div class="grid three-col">${fig('head_somi_V', 'Somi｜somi_V 頭像', 'head')}${fig(HI.somi_V, 'somi_V 原照片高解析預覽')}${fig(byM[5].VU.page, `somi_V 直式統一框樣張｜${byM[5].VU.ppi} ppi`)}</div>
<div class="grid three-col">${fig('head_ananya_2', 'Ananya｜ananya_2 頭像', 'head')}${fig(HI.ananya_2, 'ananya_2 原照片高解析預覽')}<div class="noimg">Ananya 尚未排版，也沒有臉部量測</div></div></div>`;
    return `<section class="sec" id="s2"><h2>二、人選與每月照片</h2>
${groupHtml(ROSTER, rosterExtra)}
<h3>撞臉比較（只用既有資料，本輪沒有新量測）</h3>
<p class="note">並排看照片：上面幾列遮住頭髮只看臉，下面幾列是完整頭像。</p>
<div class="grid wide">${fig('CAL_R2_focus_kanon_somi_tammy', 'Kanon／Somi／Tammy：上三列遮髮、下三列完整頭像', 'tall')}${fig('CAL_R2_focus_iris_rainie', 'Iris／Rainie：上遮髮、下完整頭像', 'tall')}</div>
<ul class="facts">
<li><b>Kanon／Somi／Tammy</b>：遮髮後臉型與五官很接近，主要靠髮色（粉紫／銅橘／蜜金）、髮型與妝感區分。三人分在 2、5、10 月，不相鄰。</li>
<li><b>Iris／Rainie</b>：都是黑長直，差異多來自妝感（裸妝對粗眼線與雀斑妝）與表情。分在 1 月與 12 月。</li>
<li>沒有量測過的人（包括 Ananya、Sophia），<b>不能</b>說不會撞臉。</li></ul>
<details class="tech"><summary>技術說明：既有量測數字與限制（點開）</summary>
<ul class="facts">
<li>來源是先前的遮髮量測（只涵蓋 Batch 3 的 19 位）；既有規則 C-2 門檻 ≤ 0.0220。本輪沒有新量測、沒有新門檻。</li>
<li>Kanon／Somi／Tammy 既有值（照錄）：kanon↔somi 0.02794、kanon↔tammy 0.03646、somi↔tammy 0.04018，都沒有落入同框限制。這<b>不等於</b>看起來夠不同。</li>
<li>Iris／Rainie：<b>沒有任何量測</b>（兩位都屬原 11 位）。Rainie 的比較圖角度大（roll 13–15°）、有閃光，這組目視比較的可信度較低。</li>
<li>Wanyin 既有值：與 Rin 0.02234、Kanon 0.02299、Somi 0.02776（未落入 ≤ 0.0220，但很接近）。Wendy 與 Batch 3 五位的既有值都 > 0.0220，與其他人沒有量測。Sophia、Ananya 沒有任何量測。</li>
<li>限制：姿態、妝容、光線、表情、遮罩邊界、生成批次都會影響比較；數字只說明沒有落入既有規則的禁止範圍。</li></ul></details>
<details class="backup"><summary>備選人選：Wanyin、Sophia、Wendy（不占月份，點開看）</summary>
<p class="note">備選只供參考，本頁不提供直接換人的按鈕；若想換人，請寫在補充意見（例：「Wanyin 替 Rainie」）。</p>
<div class="grid wide">${fig('CAL_R2_decide_people_backup', 'Wanyin、Sophia（R2 備選圖）')}${fig('CAL_R2_decide_people_compare', 'Ananya、Wendy（R2 比較圖）')}</div>
<ul class="facts"><li>Wanyin：黑長直、旗袍古典路線。</li><li>Sophia：短捲髮、成熟路線。</li><li>Wendy：銀灰鮑伯、冷感反差，甜美度較低。</li><li>既有量測數字在上面的「技術說明」。</li></ul></details>
<h3>每月照片（H＝橫式、V＝直式；圖片 ID 與 CAL_10 相同）</h3>
<p class="note">每張卡片左邊是<b>主管推薦的固定樣張</b>（不會變），右邊是<b>目前選擇</b>。目前選擇如果沒有現成樣張，會寫「此選擇尚未排版」，並附原照片。要換圖請展開「修改這個月」。</p>
<div id="months">${MONTHS.map(monthCard).join('')}</div>
</section>`;
  }
  function monthCard(x) {
    const a1 = x.m === 5 && isA1();
    const items = monthItems().filter(i => i.m === x.m);
    const same = x.H === x.V && !a1;
    const opts = x.options.filter(o => OPT_SIDE[o.code]).map(o => `${o.code} ${o.cids[0]}（${OPT_SIDE[o.code] === 'HV' ? '未指定橫直' : SIDE_ZH[OPT_SIDE[o.code]]}）`);
    let edit = '';
    if (x.m === 2) edit += '<p class="note">2 月橫直照片由第三部分「<a href="#item-kanon">Kanon 造型</a>」決定（B-K1 非女僕／B-K2 女僕）。</p>';
    if (x.m === 4) edit += '<p class="note">4 月橫式照片由第三部分「<a href="#item-angel">Angel 造型</a>」決定（B-N1 護理師／B-N2 河岸）。</p>';
    for (const it of items) edit += groupHtml(it);
    if (x.m === 9) edit += groupHtml(GRID9);
    const sumTxt = a1 ? '修改這個月（A1：ananya_2 或另找）' : x.m === 2 ? '修改這個月（到 Kanon 造型）' : (opts.length ? `修改這個月（替代：${opts.join('、')}）` : '修改這個月（沒有替代照片，可選推薦或另找）');
    const who = a1 ? 'Ananya Kapoor <small>（名單選 A1）</small>' : `${esc(x.en)} ${esc(x.zh)} <small>${esc(x.tag)}</small>`;
    const why = a1 ? '<p class="note">Ananya（目視觀察）：南亞五官、深膚色、長捲髮，是 16 位裡最容易一眼分辨的；沒有臉部量測。</p>'
      : `<dl class="why"><dt>甜美／氣質</dt><dd>${esc(plain(x.sweet))}</dd><dt>性感與造型</dt><dd>${esc(plain(x.sexy))}</dd></dl>`;
    const recNote = same ? `<p class="note same">橫直同圖：同一張照片 <code>${esc(x.H)}</code>，兩款裁切不同。</p>` : '';
    const recFigs = fig(x.HA.page, `橫 A｜${x.H}｜${x.HA.ppi} ppi`) + fig(x.VU.page, `直式統一框｜${x.V}｜${x.VU.ppi} ppi`);
    return `<article class="month" id="month-${x.m}"><h3 class="mh"><span class="mn">${x.m} 月</span> ${who}</h3>` +
      (a1 ? '<p class="note">名單選了 A1：5 月改 Ananya。左邊仍是原推薦（Somi）的固定樣張，只供對照。</p>' : '') + why +
      `<div class="mrow"><div class="mcol"><h4>主管推薦｜固定樣張（不隨選擇改變）</h4>${recNote}<div class="grid two-col">${recFigs}</div>` +
      (x.m === 9 ? `<div class="grid two-col sub">${fig('H_grid_09_yuna-kim', '9 月大格面（含 9b 小框）')}</div>` : '') +
      `</div><div class="mcol cur" id="cur-${x.m}">${curHtml(x)}</div></div>` +
      `<details class="edit"><summary>${esc(sumTxt)}</summary>${edit}</details></article>`;
  }

  // ---------- 三、尺度與造型 ----------
  function s3() {
    const kref = `<details class="ref"><summary>參考（不可選）：Kanon 另一張女僕圖 kanon_V</summary><div class="grid two-col">${fig('tile_kanon_V', 'kanon_V 原照片（女僕胸口開口 train_01）')}${fig('CHK_kanon_kanon_V_V_U', 'kanon_V 在直式統一框：原圖已缺髮頂')}</div>` +
      `<p class="note">原圖上緣直接切過頭髮，任何框都補不回，只列參考。</p></details>`;
    const afix = `<div class="derived"><p>4 月直式（兩案都用，在第二部分 4 月卡片確認）：</p><div class="grid two-col">${fig('V_U_04_angel-chiu', `固定推薦樣張｜angel_V 直式統一框｜${VU(4).ppi} ppi`)}</div></div>`;
    return `<section class="sec" id="s3"><h2>三、尺度與造型</h2>
<p class="note">Kanon 與 Angel 分開選，不用一個「制服總開關」。</p>
${groupHtml(SCALE)}${groupHtml(KANON, kref)}${groupHtml(ANGEL, afix)}</section>`;
  }

  // ---------- 四、版面 ----------
  function s4() {
    const hb = MONTHS.map(x => fig(x.HB.page, `${x.m} 月 ${first(x.en)}｜${x.HB.ppi} ppi${/裁掉/.test(x.HB.hair) ? '｜髮頂被裁' : ''}`)).join('');
    const groups = {};
    [...MONTHS].sort((a, b) => b.HB.ppi - a.HB.ppi).forEach(x => { (groups[x.HB.ppi] = groups[x.HB.ppi] || []).push(first(x.en)); });
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
<p class="note">橫式與直式分開選。組合對應 CAL_10 代碼：橫 A＋統一框＝<b>C1</b>（推薦）；橫 B＋統一框＝<b>C2</b>（只改橫式）；橫 A＋原直 A＝<b>C3</b>（只改直式）。目前組合：<b id="ccode">—</b></p>
<p class="note">下面兩題的圖是 Iris、Vicky 的版面範例。各月在你選的版面下有沒有樣張，請看各月卡片的「目前選擇」。</p>
${groupHtml(LAYOUT_H)}
<details class="sub"><summary>橫 B 逐張：12 位推薦照片的實際樣張</summary><div class="grid">${hb}</div></details>
<div class="callout"><b>橫 B 的限制（依逐張實際結果）</b><ul>
<li>ppi：${esc(hbText)}。300 ppi 是本專案工作目標，不是廠商已確認的門檻。</li>
<li>髮頂被照片框裁掉：${esc(cut)}（程式判定，未目視）。多數變成胸上特寫，身形變少。</li>
<li>這是逐張結果，不代表整套都要新圖；若選橫 B，哪些月份要改裁切或補圖，下一輪逐月評估（本輪不生成、不外擴）。</li></ul></div>
${groupHtml(LAYOUT_V)}
<details class="sub"><summary>直式：同一人的統一框 vs 原直 A（只有 4 位有原直 A 樣張）</summary><div class="grid wide">${va}</div></details>
<div class="callout"><b>髮頂接近或進入線圈區的頁（待廠商確認，不是印刷安全保證）</b>
<p class="note">線圈區是本專案假設的上緣 12 mm；廠商的實際線圈位置還沒確認。臉都在框內、避開線圈。</p><ul>${hair.map(h => `<li>${esc(h)}</li>`).join('')}</ul></div>
</section>`;
  }

  // ---------- 五、收件對象與品牌 ----------
  function s5() {
    const r = S.v.recipient || {}, b = S.v.brand || {}, q = S.v.qr || {};
    const rad = (name, val, label, cur) => `<label class="opt"><input type="radio" name="${name}" value="${esc(val)}"${cur === val ? ' checked' : ''}> ${esc(label)}</label>`;
    return `<section class="sec" id="s5"><h2>五、收件對象與品牌</h2>
<p class="note">沒有推薦，「套用推薦」不會填這裡。沒有提供前一律用佔位，不自行填品牌或網址。可以先確認選角與版面，這裡之後再補，不影響複製。本頁<b>不收檔案</b>，Logo 檔請另外提供。</p>
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
<fieldset class="item form" id="item-comments"><legend>補充意見（自由文字，不屬於確認項目）</legend>
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
      ...MONTHS.flatMap(x => x.options.map(o => [o.code, `${x.m} 月選項${o.code === '9b' ? '（主管覆核後補推薦）' : ''}`, o.cids.join('、')])),
      ['推薦', '每月推薦圖（主管推薦）', MONTHS.map(x => `${x.m}月 H ${x.H}／V ${x.V}`).join('；')],
      ['另找', '本頁新增：該月該款不採用目前任何圖', '—'], ['不放', '本頁新增：9 月大格面不放小框照片', '—'],
      ['橫／直指定', '本頁新增：5c、10c、12b 在 CAL_10 沒有指定橫直，本頁由 Penny 指定用在哪一款（仍須後續排版覆核）', 'somi_alt065、tammy_alt075、rainie_alt02'],
      ['C2＋C3', '本頁新增說明：橫 B＋原直 A（CAL_10 沒有這個單一代碼）', '—'],
    ];
    return `<section class="sec" id="out"><h2>複製決策結果</h2>
<div class="callout">選擇只存在這個瀏覽器（localStorage），<b>不會送到伺服器</b>。複製後請<b>貼回 ChatGPT</b>；本頁不會通知主管。<br>「草稿」＝選了但還沒按確認；「Penny 已確認」＝按了確認之後沒有再改過。確認後只要再改（即使改回原來的值），那一項就回到草稿。未回答的項目不會被輸出成核准。</div>
<div class="actions"><button type="button" class="btn" id="act-copy2">複製決策結果</button><button type="button" class="btn danger" id="act-reset">重設</button></div>
<label class="lbl" for="out-text">將複製的文字（預覽，會隨選擇更新）</label>
<textarea id="out-text" rows="16" readonly></textarea>
<details class="sub"><summary>代碼與圖片 ID 對照表</summary><div class="tbl"><table><thead><tr><th>代碼</th><th>內容</th><th>圖片 ID／本頁對應</th></tr></thead><tbody>
${rows.map(r => `<tr><td>${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join('')}</tbody></table></div></details>
</section>`;
  }

  // ---------- 摘要資料與輸出文字 ----------
  function cCode() {
    const h = answered('layoutH') ? S.v.layoutH : null, v = answered('layoutV') ? S.v.layoutV : null;
    if (!h || !v) return null;
    if (h === 'H_A' && v === 'V_U') return 'C1';
    if (h === 'H_B' && v === 'V_U') return 'C2';
    if (h === 'H_A' && v === 'V_A') return 'C3';
    return 'C2＋C3 組合（CAL_10 沒有這個單一代碼）';
  }
  function valText(id) {
    if (!answered(id)) return '未回答';
    const c = choiceOf(id);
    const r = S.v.recipient || {}, b = S.v.brand || {}, q = S.v.qr || {};
    switch (id) {
      case 'roster': return S.v.roster === 'A0' ? 'A0 沿用 12 人（5 月 Somi）' : 'A1 5 月改 Ananya（ananya_2；無臉部量測、尚未排版）';
      case 'scale': return `${c.code} ${c.title}${c.rec ? '（主管推薦）' : ''}${S.v.scale === 'B-S3' ? '（未採用的參考級；需再確認廠商接受範圍）' : ''}`;
      case 'kanon': case 'angel': return `${c.code} ${c.cid} ${c.title}${c.rec ? '（主管推薦）' : ''}`;
      case 'layoutH': case 'layoutV': return `${c.code}｜${c.title}${c.rec ? '（主管推薦）' : ''}`;
      case 'grid9': return S.v.grid9 === '9b' ? '9b yuna_altsoft（主管推薦）' : '不放（本頁新增選項；尚未排版）';
      case 'recipient': return r.k === 'other' ? `其他：${r.text.trim()}` : r.k;
      case 'brand': return b.k === 'ph' ? '先用佔位「［品牌名稱 佔位］」' : b.text.trim();
      case 'logo': return S.v.logo;
      case 'qr': return q.k === 'none' ? '不放' : `提供連結：${q.url.trim()}`;
      default: return c ? c.code : '';
    }
  }
  const tagged = id => `${valText(id)}${ST_TAG[status(id)]}`;
  function monthText(it) {
    const c = choiceOf(it.id);
    if (!c) return '';
    if (c.key === 'rec') return `${c.cid}（推薦）`;
    if (c.key === 'other') return '另找（不採用目前任何圖，見補充意見）';
    return `${c.code} ${c.cid}`;
  }
  function notLaid(x, side, cid) { return !laidOut(x, side, cid).page; }
  function changeList() {
    const out = [];
    const diff = (id, rec, label) => { if (answered(id) && S.v[id] !== rec) out.push(`${label}：${tagged(id)}`); };
    diff('roster', 'A0', '名單');
    diff('scale', 'B-S2', '尺度');
    if (answered('kanon') && S.v.kanon !== 'B-K1') out.push(`Kanon 造型（2 月橫直）：${tagged('kanon')}；橫式尚未排版`);
    if (answered('angel') && S.v.angel !== 'B-N1') out.push(`Angel 造型（4 月橫式）：${tagged('angel')}；尚未排版`);
    diff('layoutH', 'H_A', '橫式版面');
    diff('layoutV', 'V_U', '直式版面');
    for (const it of monthItems()) {
      if (!answered(it.id) || S.v[it.id] === 'rec') continue;
      const c = choiceOf(it.id);
      const x = byM[it.m];
      const nl = c.cid && notLaid(x, it.side, c.cid) ? '（尚未排版）' : '';
      out.push(`${it.m} 月 ${it.side}＝${monthText(it)}${ST_TAG[status(it.id)]}${nl}`);
    }
    if (answered('grid9') && S.v.grid9 !== '9b') out.push(`9 月大格面小框：${tagged('grid9')}`);
    return out;
  }
  function counts() {
    const cnt = { none: 0, draft: 0, conf: 0 };
    allItems().forEach(i => { cnt[status(i.id)] += 1; });
    return cnt;
  }
  function buildText() {
    const items = allItems();
    const cnt = counts();
    const t = [];
    t.push('【2027 KOL 桌曆決策結果】（由決策頁產生；請貼回 ChatGPT）');
    t.push(`基準成果 SHA：${SHA}`);
    t.push(`決策頁版本：${PAGE_COMMIT || '未知（本機預覽）'}`);
    t.push(`產生時間：${new Date().toLocaleString('zh-TW', { hour12: false })}（瀏覽器時間）`);
    t.push(`狀態：Penny 已確認 ${cnt.conf} 項｜草稿・未確認 ${cnt.draft} 項｜未回答 ${cnt.none} 項`);
    if (S.confAt) t.push(`最近一次按下確認：${new Date(S.confAt).toLocaleString('zh-TW', { hour12: false })}（之後改過的項目已回到草稿）`);
    t.push('※ 草稿＝頁面上選了但尚未確認，或確認後又改過。未回答不代表核准，也不代表沿用推薦。此結果不是主管核准，也不是印刷或廠商核准。');
    t.push('');
    t.push('一、名單：' + tagged('roster'));
    t.push('二、尺度：' + tagged('scale'));
    t.push('三、Kanon 造型：' + tagged('kanon'));
    t.push('四、Angel 造型：' + tagged('angel'));
    t.push('五、橫式版面：' + tagged('layoutH'));
    t.push('六、直式版面：' + tagged('layoutV'));
    t.push('　→ 對應 CAL_10 版面代碼：' + (cCode() || '未定（橫式或直式版面未回答）'));
    t.push('七、逐月照片（H＝橫式、V＝直式；圖片 ID 同 CAL_10）');
    t.push('　※ 樣張只代表主管推薦組合；標「尚未排版」的選擇在所選版面沒有現成樣張。版面未回答時以推薦版面判斷。');
    const mi = monthItems();
    for (const x of MONTHS) {
      const a1 = x.m === 5 && isA1();
      const name = a1 ? 'Ananya（A1）' : first(x.en);
      const parts = [];
      for (const side of ['H', 'V']) {
        if (x.m === 2 || (x.m === 4 && side === 'H')) {
          const id = x.m === 2 ? 'kanon' : 'angel';
          if (!answered(id)) { parts.push(`${side} 依${x.m === 2 ? ' Kanon' : ' Angel'} 造型（未回答）${ST_TAG.none}`); continue; }
          const cid = choiceOf(id).cid;
          parts.push(`${side} 依${x.m === 2 ? ' Kanon' : ' Angel'} 造型 ${S.v[id]} → ${cid}${ST_TAG[status(id)]}${notLaid(x, side, cid) ? '（尚未排版）' : ''}`);
          continue;
        }
        const it = mi.find(i => i.m === x.m && i.side === side);
        if (!answered(it.id)) { parts.push(`${side} 未回答${ST_TAG.none}`); continue; }
        const c = choiceOf(it.id);
        parts.push(`${side} ${monthText(it)}${ST_TAG[status(it.id)]}${c.cid && notLaid(x, side, c.cid) ? '（尚未排版）' : ''}`);
      }
      t.push(`　${x.m} 月 ${name}：${parts.join('｜')}`);
    }
    t.push('　9 月大格月曆面小框：' + tagged('grid9'));
    const changes = changeList();
    t.push('　與推薦不同的地方：' + (changes.length ? changes.join('；') : '無（只計已回答項目）'));
    t.push('八、收件對象與品牌');
    t.push('　預計給誰看：' + tagged('recipient'));
    t.push('　品牌名稱：' + tagged('brand'));
    t.push('　Logo：' + tagged('logo'));
    t.push('　QR：' + tagged('qr'));
    t.push('九、補充意見（自由文字，不屬於確認項目）：' + ((S.v.comments || '').trim() || '（無）'));
    const un = items.filter(i => status(i.id) === 'none').map(i => i.label);
    t.push('十、未回答清單：' + (un.length ? un.join('、') : '無'));
    const codes = [];
    for (const id of ['roster', 'scale', 'kanon', 'angel']) if (answered(id)) codes.push(S.v[id]);
    if (cCode()) codes.push(cCode());
    if (answered('grid9')) codes.push(S.v.grid9 === '9b' ? '9b' : '9 月小框不放');
    t.push('');
    t.push('代碼摘要（只列已回答）：' + (codes.length ? codes.join('＋') : '無') + '；逐月修改：' + (changes.length ? changes.join('；') : '無'));
    return t.join('\n');
  }
  function summaryRows() {
    const mi = monthItems();
    const mc = { rec: 0, alt: 0, other: 0, none: 0 }, ms = { none: 0, draft: 0, conf: 0 };
    for (const it of mi) {
      ms[status(it.id)] += 1;
      if (!answered(it.id)) mc.none += 1; else if (S.v[it.id] === 'rec') mc.rec += 1; else if (S.v[it.id] === 'other') mc.other += 1; else mc.alt += 1;
    }
    const row = (label, href, val, st, stText) => `<tr><td><a href="${href}">${esc(label)}</a></td><td>${esc(val)}</td><td>${st ? `<span class="st ${st}">${esc(stText || ST_TEXT[st])}</span>` : ''}</td></tr>`;
    const one = (id, label) => row(label, `#item-${id}`, valText(id), status(id));
    const mst = ms.none ? 'none' : (ms.draft ? 'draft' : 'conf');
    const mstText = ms.none && ms.none < mi.length ? '部分未回答' : (ms.draft && ms.conf ? '部分草稿' : null);
    return [
      one('roster', '名單'), one('scale', '尺度'), one('kanon', 'Kanon 造型'), one('angel', 'Angel 造型'),
      one('layoutH', '橫式版面'), one('layoutV', '直式版面'),
      row('版面代碼', '#s4', cCode() || '未定', null),
      row(`逐月照片（${mi.length} 面）`, '#months', `推薦 ${mc.rec}、替代 ${mc.alt}、另找 ${mc.other}、未回答 ${mc.none}｜已確認 ${ms.conf}、草稿 ${ms.draft}`, mst, mstText),
      one('grid9', '9 月小框'), one('recipient', '收件對象'), one('brand', '品牌名稱'), one('logo', 'Logo'), one('qr', 'QR'),
      row('補充意見', '#item-comments', (S.v.comments || '').trim() ? '有（自由文字，不屬於確認項目）' : '無', null),
    ].join('');
  }

  // ---------- 更新 ----------
  function refresh() {
    const items = allItems();
    $$('[data-st]').forEach(el => { const s = status(el.dataset.st); el.className = 'st ' + s; el.textContent = ST_TEXT[s]; });
    $$('.choice').forEach(el => { const r = el.querySelector('input[type=radio]'); el.classList.toggle('sel', !!r && r.checked); });
    for (const x of MONTHS) { const el = $(`#cur-${x.m}`); if (el) el.innerHTML = curHtml(x); }
    const cnt = counts();
    $('#bar-count').textContent = `未回答 ${cnt.none}｜草稿 ${cnt.draft}｜已確認 ${cnt.conf}`;
    const un = items.filter(i => status(i.id) === 'none');
    $('#un-n').textContent = `（${un.length} 項）`;
    $('#unans').innerHTML = un.length ? un.map(i => `<li><a href="#item-${esc(i.id)}">${esc(i.label)}</a></li>`).join('') : '<li>沒有未回答的項目。</li>';
    const ch = changeList();
    $('#changes').innerHTML = ch.length ? ch.map(c => `<li>${esc(c)}</li>`).join('') : '<li>沒有（已回答的項目都與推薦相同）。</li>';
    $('#summary').innerHTML = summaryRows();
    $('#ccode').textContent = cCode() || '未定';
    $('#conf-at').textContent = S.confAt ? `最近一次確認：${new Date(S.confAt).toLocaleString('zh-TW', { hour12: false })}。確認後再改的項目（即使改回原值）會回到草稿。` : '尚未按過確認：目前所有選擇都是草稿。';
    $('#out-text').value = buildText();
  }
  function rerenderMonth(m) { const el = $(`#month-${m}`); if (el) el.outerHTML = monthCard(byM[m]); }

  function render() {
    $('#sha').textContent = SHA;
    $('#pagever').textContent = PAGE_COMMIT || '本機預覽（未部署）';
    app.innerHTML = sQuick() + s1() + s2() + s3() + s4() + s5() + sOut();
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
    setVal(name, FORM_RADIO[name] ? FORM_RADIO[name](el.value) : el.value);
    save();
    if (name === 'roster') rerenderMonth(5);
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
    setVal(id, { ...cur, k, [field]: el.value });
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
    if (b.id === 'act-copy' || b.id === 'act-copy2') copyOut();
    if (b.id === 'act-reset') resetAll();
  });
  $('#bar-copy').addEventListener('click', copyOut);

  function applyRec() {
    const recItems = () => allItems().filter(i => i.choices && i.choices.some(c => c.rec));
    const todo = recItems().filter(i => !answered(i.id));
    if (!todo.length) { toast('有推薦的項目都已回答，沒有要填的。'); return; }
    if (!window.confirm(`會把 ${todo.length} 個「未回答」且有主管推薦的項目填成推薦（草稿）。已選的項目不會被改。\n收件對象、品牌、Logo、QR 沒有推薦，不會被填。\n填好後仍要按「確認」才算 Penny 確認。要繼續嗎？`)) return;
    for (const i of todo) setVal(i.id, i.choices.find(c => c.rec).key);
    // 名單變成 A0 後，5 月改用 Somi 的題目；再補一次推薦
    for (const i of recItems()) if (!answered(i.id)) setVal(i.id, i.choices.find(c => c.rec).key);
    save();
    render();
    toast('已填入推薦（草稿）。只改想換的地方，檢查摘要後按「確認」。');
  }
  function confirmAll() {
    const items = allItems().filter(i => answered(i.id));
    const un = allItems().filter(i => !answered(i.id)).length;
    if (!items.length) { toast('還沒有任何已回答的項目。'); return; }
    if (!window.confirm(`確認後，目前已回答的 ${items.length} 項會標為「Penny 已確認」。\n未回答的 ${un} 項仍是未回答，不會被當成核准；之後再改的項目會回到草稿。\n要確認嗎？`)) return;
    const at = new Date().toISOString();
    for (const i of items) S.conf[i.id] = { v: JSON.stringify(S.v[i.id]), at };
    S.confAt = at;
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
  function viewerNote(m) {
    const px = `${m.w}×${m.h} px`;
    switch (m.res) {
      case 'page300': return `300 dpi 樣張原檔（${px}；${m.src.replace('docs/calendar/', '')}）`;
      case 'preview100': return `100% 實際像素預覽（${px}；不是印刷證明）`;
      case 'lowres': return `${LOWRES_NOTE}（裁自決策拼圖，${px}）`;
      case 'hires': return `高解析預覽：原圖 ${m.orig_px[0]}×${m.orig_px[1]} 等比縮小至 ${px}；未排版，印刷採用待排版覆核`;
      default: return `既有比較圖原檔（${px}）`;
    }
  }
  function openViewer(btn) {
    const m = IMG[btn.dataset.img];
    if (!m) return;
    lastBtn = btn;
    vimg.src = m.z;
    vimg.width = m.w;
    vimg.height = m.h;
    vimg.alt = btn.dataset.cap;
    vcap.textContent = `${btn.dataset.cap}｜${viewerNote(m)}`;
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
