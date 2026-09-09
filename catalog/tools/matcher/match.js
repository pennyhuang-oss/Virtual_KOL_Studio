const IDX = __INDEX__;
const SYN = __SYN__;
const IND = __IND__;   // 產業對照表:客戶打的字庫裡沒有時,用它找最接近的品類

/* ── 共用 ── */
const norm = s => String(s == null ? '' : s).toLowerCase().replace(/\s+/g, '');
const esc = s => String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const nameOf = o => o.zh || o.name;
const tip = document.getElementById('tip');
const showTip = (el, html) => {
  tip.innerHTML = html;
  const r = el.getBoundingClientRect();
  tip.style.opacity = 1;
  const w = tip.offsetWidth, h = tip.offsetHeight;
  tip.style.left = Math.min(window.innerWidth - w - 10, Math.max(8, r.left + r.width / 2 - w / 2)) + 'px';
  tip.style.top = Math.max(8, r.top - h - 8) + 'px';
};
const hideTip = () => { tip.style.opacity = 0; };


/* ── 配對 ── */
// 分兩層強度。
// 🛑 為什麼要分:中文用二字組比對會過度命中——「行車紀錄器」的二字組「紀錄」
//    會打中「紀錄片推薦」,結果查行車紀錄器時,拍紀錄片的人排在改裝店企劃前面。
//    三字以上的重疊才算 strong,只靠二字組命中的算 weak,只給一半分。
function toks(q){
  const s = norm(q), strong = new Set(), weak = new Set(), short = new Set();
  (s.match(/[a-z0-9]{2,}/g) || []).forEach(w => (w.length <= 3 ? short : strong).add(w));
  const cjk = s.replace(/[^一-鿿]/g, '');
  for (let i = 0; i < cjk.length - 1; i++) weak.add(cjk.slice(i, i + 2));
  for (let n = 3; n <= cjk.length; n++)
    for (let i = 0; i + n <= cjk.length; i++) strong.add(cjk.slice(i, i + n));
  const all = [...strong, ...weak, ...short];
  for (const row of SYN) if (row.some(w => all.includes(norm(w))))
    row.forEach(w => { const n = norm(w);
      if (n.length <= 3 && /^[a-z0-9]+$/.test(n)) short.add(n);
      else if (n.replace(/[^一-鿿]/g, '').length === 2 && !/[a-z0-9]/.test(n)) weak.add(n);
      else strong.add(n); });
  return { strong: [...strong], weak: [...weak], short: [...short] };
}
// 回傳 0＝沒命中、1＝只靠二字組（半分）、2＝三字以上或整詞（全分）
function thit(T, text){
  const n = norm(text);
  if (T.strong.some(t => n.includes(t))) return 2;
  if (T.short.some(t => new RegExp('(^|[^a-z0-9])' + t + '([^a-z0-9]|$)').test(n))) return 2;
  return T.weak.some(t => n.includes(t)) ? 1 : 0;
}
const wsum = (arr, T) => arr.reduce((a, x) => a + thit(T, x) / 2, 0);
// 紅線:命中就靜靜排除,不對客戶說「她不接什麼」。
// 🛑 不能只認強命中——紅線詞大多是兩個字（代餐、投注、斷食、必勝），
//    兩個字在查詢裡只會切成弱 token,只認強命中等於這些紅線永遠擋不住。
//    所以額外認「整個詞剛好等於查詢切出來的那個二字組」。
const blocked = (o, T) => o.block.some(x => {
  const v = thit(T, x);
  return v === 2 || (v === 1 && T.weak.indexOf(norm(x)) >= 0);
});
// 把一組「庫裡真的有的詞」直接當 token 用（產業對照表的替代查詢走這條）。
// 這些詞是人挑過的,不是查詢字切出來的碎片,所以一律算強命中。
function toksFrom(terms){
  const strong = [], short = [];
  terms.forEach(t => { const n = norm(t);
    (n.length <= 3 && /^[a-z0-9]+$/.test(n) ? short : strong).push(n); });
  return { strong, weak: [], short };
}
function match(q){ return matchT(toks(q)); }
// Tb＝額外要過紅線的那組 token。替代查詢一定要帶原本客戶打的字進來——
// 不然紅線變成拿「品類的詞」在驗,客戶打某位人設明確不接的題目時,她會從替代查詢那條路回到名單上。
function matchT(T, Tb){
  if (!T.strong.length && !T.weak.length && !T.short.length) return [];
  const out = [];
  for (const o of IDX) {
    if (blocked(o, T) || (Tb && blocked(o, Tb))) continue;
    const hooks = o.hooks.filter(h => thit(T, h.t) || (h.k || []).some(k => thit(T, k)));
    const kws = o.kw.filter(k => thit(T, k));
    const pil = o.pil.filter(x => thit(T, x));
    const fits = o.fit.filter(f => thit(T, f));
    const soft = [o.tag, o.aud, o.mood].filter(s => thit(T, s));
    const catH = thit(T, o.cat) === 2;
    // 每一項按命中強度加權（弱命中算半個）
    const wh = wsum(hooks.map(h => h.t), T) + 0, wk = wsum(o.kw.filter(k => thit(T, k)), T),
          wp = wsum(pil, T), wf = wsum(fits, T), ws = wsum(soft, T);
    const topic = Math.min(100, Math.round(26 * wh + 9 * wp + 7 * wk + 6 * ws));
    const cate = Math.min(100, Math.round(30 * wf + (catH ? 25 : 0) + 5 * wk));
    if (!topic && !cate) continue;
    // 訊號強弱＝庫裡有幾處資料對得上這個查詢字,跟「合不合」是兩件事。
    // 冷門的單一詞（烤箱、護士鞋）本來就只命中一兩處,分數天生低;
    // 不標出來,客戶會把「資料少」讀成「人設不合」。
    const hstr = h => Math.max(thit(T, h.t), ...(h.k || []).map(k => thit(T, k)), 0);
    let full = catH ? 1 : 0, half = 0;
    for (const v of [...hooks.map(hstr), ...[...kws, ...pil, ...fits, ...soft].map(x => thit(T, x))])
      v === 2 ? full++ : half++;
    const nHit = full + half, ev = full + half * .5;
    out.push({ o, topic, cate, hooks, kws, pil, fits, soft, catH, nHit,
               sig: ev >= 4 ? 2 : ev >= 2 ? 1 : 0,
               total: Math.round(topic * .6 + cate * .4) });
  }
  out.sort((a, b) => b.total - a.total);
  const best = out.length ? out[0].total : 0;
  out.forEach(r => { r.best = r.total === best; });   // 並列同分都算全庫最高
  return out;
}
const SIG = ['弱', '中', '強'];
const SIGB = ['<span class="bdg n">訊號弱</span>', '', ''];
const SIGN = ['這個查詢字冷門，能佐證的資料少，分數天生偏低——低分不等於配不上。',
              '有幾處對得上，但還沒到滿載。', ''];

// 找最接近的產業桶。命中數並列的桶一起用（例:「相機」同時屬於 3C 與攝影）。
function nearest(q){
  const T = toks(q);
  // 強命中（三字以上或整詞）永遠贏過弱命中（只靠二字組）。
  // 沒分強弱時「工廠自動化」會配到文具的「自動筆」——因為它們共用「自動」這兩個字。
  const scored = IND.map(b => {
    let st = 0, wk = 0;
    for (const h of b.hit) { const v = thit(T, h); if (v === 2) st++; else if (v === 1) wk++; }
    return { b, s: st * 10 + wk };
  }).filter(x => x.s > 0).sort((a, b) => b.s - a.s);
  if (!scored.length) return null;
  const top = scored.filter(x => x.s === scored[0].s).slice(0, 2);   // 並列就一起用
  return { names: top.map(x => x.b.name), terms: [...new Set(top.flatMap(x => x.b.expand))] };
}

// 直接命中與替代查詢的結果合起來。
// 🛑 不把兩邊的分數相加——那樣拆解表就對不上顯示的數字了,而「每一分都可以攤開來看」是這一頁的前提。
// 改成排序時把「字面和品類都對到」的排前面：那是比「只對到品類」更強的主張,而且講得出理由。
// 例:查「烤箱」,梁欣妮字面就有烤箱、又落在廚房家電這個品類,所以她排在只對到品類的人前面。
function mergeRes(a, b){
  const lit = new Set(a.map(r => r.o.id));
  const m = new Map();
  for (const r of [...a, ...b]) { const p = m.get(r.o.id); if (!p || r.total > p.total) m.set(r.o.id, r); }
  const out = [...m.values()];
  const top = Math.max(...out.map(r => r.total), 0);
  // 只有分數跟第一名同一個量級的字面命中才往前提。
  // 不設這個門檻,「高鐵」會把 12 分的人排在 67 分的人前面——客戶看了會覺得這個工具壞了。
  out.forEach(r => { r.lit = lit.has(r.o.id); r.up = r.lit && r.total >= top * 0.6; });
  out.sort((x, y) => (y.up - x.up) || (y.total - x.total));
  const best = out.length ? out[0].total : 0;
  out.forEach(r => { r.best = r.total === best; });
  return out;
}

const svg = document.getElementById('svg');
const PAD = { l: 44, r: 14, t: 12, b: 40 }, W = 420, H = 360;
const px = v => PAD.l + (v / 100) * (W - PAD.l - PAD.r);
const py = v => H - PAD.b - (v / 100) * (H - PAD.t - PAD.b);
let RES = [];

function drawPlot(res){
  const g = [`<title id="svgt">配對定位圖：橫軸主題契合 0 到 100，縱軸品類契合 0 到 100</title>`];
  g.push(`<rect x="${px(50)}" y="${py(100)}" width="${px(100)-px(50)}" height="${py(50)-py(100)}" fill="#e7cd74" fill-opacity=".05"></rect>`);
  for (const v of [0, 50, 100]) {
    g.push(`<line x1="${px(v)}" y1="${py(0)}" x2="${px(v)}" y2="${py(100)}" stroke="rgba(242,242,244,${v===50?'.16':'.09'})"></line>`);
    g.push(`<line x1="${px(0)}" y1="${py(v)}" x2="${px(100)}" y2="${py(v)}" stroke="rgba(242,242,244,${v===50?'.16':'.09'})"></line>`);
    g.push(`<text class="tick" x="${px(v)}" y="${py(0)+14}" text-anchor="middle">${v}</text>`);
    g.push(`<text class="tick" x="${px(0)-7}" y="${py(v)+3.5}" text-anchor="end">${v}</text>`);
  }
  g.push(`<text class="qlab" x="${px(100)-4}" y="${py(100)+12}" text-anchor="end">首選</text>`);
  g.push(`<text class="qlab" x="${px(100)-4}" y="${py(0)-7}" text-anchor="end">會講這題，品類要溝通</text>`);
  g.push(`<text class="qlab" x="${px(0)+5}" y="${py(100)+12}">接這品類，建議換題目</text>`);
  g.push(`<text class="axlab" x="${(px(0)+px(100))/2}" y="${H-7}" text-anchor="middle">主題契合</text>`);
  g.push(`<text class="axlab" transform="translate(12,${(py(0)+py(100))/2}) rotate(-90)" text-anchor="middle">品類契合</text>`);
  const top = res.slice(0, 4).map(r => r.o.id);
  const groups = new Map();
  for (const r of res) { const k = r.topic + '|' + r.cate;
    if (!groups.has(k)) groups.set(k, []); groups.get(k).push(r); }
  [...groups.values()].reverse().forEach(grp => {
    const r = grp[0], on = grp.some(x => top.includes(x.o.id));
    g.push(`<circle class="dot" data-key="${r.topic}|${r.cate}" cx="${px(r.topic)}" cy="${py(r.cate)}"
      r="${on ? 7 : (grp.length > 1 ? 6.5 : 5)}" fill="${on ? 'var(--gold2)' : 'var(--dotq)'}"
      stroke="var(--card)" stroke-width="2"></circle>`);
    if (grp.length > 1 && !on) g.push(`<text class="tick" x="${px(r.topic)}" y="${py(r.cate)+3}"
      text-anchor="middle" fill="var(--ink2)" style="font-size:9px">${grp.length}</text>`);
  });
  res.slice(0, 4).forEach((r, i) => {
    const x = px(r.topic), y = py(r.cate), flip = x > W - 100;
    g.push(`<text class="dlab" x="${flip ? x - 11 : x + 11}" y="${y + (i % 2 ? 13 : 4)}"
      text-anchor="${flip ? 'end' : 'start'}">${esc(nameOf(r.o))}</text>`);
  });
  svg.innerHTML = g.join('');
  svg.querySelectorAll('.dot').forEach(c => {
    c.addEventListener('pointerenter', () => {
      const grp = groups.get(c.dataset.key) || [], r = grp[0];
      showTip(c, `<b>${grp.slice(0, 4).map(x => esc(nameOf(x.o))).join('、')}`
        + `${grp.length > 4 ? ' 等 ' + grp.length + ' 位' : ''}</b>`
        + `<span>主題 ${r.topic}　品類 ${r.cate}　匹配度 ${r.total}</span>`);
    });
    c.addEventListener('pointerleave', hideTip);
    c.addEventListener('click', () => { const grp = groups.get(c.dataset.key); if (grp) drawAnat(grp[0]); });
  });
}

function drawAnat(r){
  document.getElementById('anatwho').textContent = nameOf(r.o);
  const L = [], row = (a, b, c, cls) => L.push(`<tr class="${cls || ''}"><td>${a}</td><td class="n">${b}</td><td class="n">${c}</td></tr>`);
  L.push('<tr><th>命中項</th><th style="text-align:right">數量</th><th style="text-align:right">小計</th></tr>');
  row('<b style="color:var(--ink)">主題契合</b>', '', r.topic, 'grp');
  row('題目連結點　× 26', r.hooks.length, 26 * r.hooks.length, 'sub');
  row('內容主題　　× 9', r.pil.length, 9 * r.pil.length, 'sub');
  row('主題關鍵詞　× 7', r.kws.length, 7 * r.kws.length, 'sub');
  row('定位／受眾　× 6', r.soft.length, 6 * r.soft.length, 'sub');
  row('<b style="color:var(--ink)">品類契合</b>', '', r.cate, 'grp');
  row('合作方向　　× 30', r.fits.length, 30 * r.fits.length, 'sub');
  row('領域相符　　＋25', r.catH ? 1 : 0, r.catH ? 25 : 0, 'sub');
  row('關鍵詞　　　× 5', r.kws.length, 5 * r.kws.length, 'sub');
  row('<b style="color:var(--ink)">匹配度</b>　主題 ' + r.topic + ' × 0.6 ＋ 品類 ' + r.cate + ' × 0.4', '', r.total, 'tot');
  L.push(`<tr class="sig"><td colspan="3"><b>訊號 ${SIG[r.sig]}</b>　庫裡有 ${r.nHit} 處資料對得上。${SIGN[r.sig]}${r.best && r.sig < 2 ? '這已經是全庫最高分。' : ''}</td></tr>`);
  const words = [...new Set([...r.fits, ...r.pil, ...r.kws])].slice(0, 6);
  if (words.length) L.push(`<tr><td colspan="3" style="color:var(--ink3);font-size:12px;border-bottom:0;padding-top:2px">
    命中的詞：${words.map(w => `<i style="font-style:normal;color:var(--gold2)">${esc(w)}</i>`).join('、')}</td></tr>`);
  if (r.hooks[0]) L.push(`<tr><td colspan="3" style="border-bottom:0;padding-top:8px">
    <div style="border-left:2px solid var(--goldd);padding-left:10px;font-size:12.5px;color:var(--ink2)">
    ${esc(r.hooks[0].t)}${r.hooks[0].ev ? '<span class="bdg">常青</span>' : '<span class="bdg w">需搭時事</span>'}
    <div style="color:var(--ink3);margin-top:2px">${esc(r.hooks[0].a)}</div></div></td></tr>`);
  document.getElementById('anat').innerHTML = L.join('');
  document.querySelectorAll('.rrow').forEach(x => x.classList.toggle('on', x.dataset.id === r.o.id));
}

// 三層,永遠給得出答案——空白畫面對客戶來說等於「你們做不了」。
//   ① 直接命中
//   ② 沒命中 → 產業對照表找最接近的品類,用那個品類的詞重查,畫面上明說換過
//   ③ 連對照表也沒有（工廠、物流這類）→ 排「可切入面最廣」的幾位,並說清楚這是通用排序
// 命中在這個分數以下就算「太薄」——「蛋糕」只對到 4 分，而它屬於烘焙與甜點，
// 那一桶排出來的結果好得多，所以薄命中也要補上相近品類一起排。
const THIN = 12;
function renderQ(q){
  const note = document.getElementById('note');
  let mode = 'hit', near = null;
  const direct = match(q);
  RES = direct;
  if (!direct.length || direct[0].total < THIN) {
    near = nearest(q);
    if (near) {
      const nr = matchT(toksFrom(near.terms), toks(q));
      if (nr.length) { RES = mergeRes(direct, nr); mode = direct.length ? 'mix' : 'near'; }
    }
  }
  if (!RES.length) {
    mode = 'wide';
    // 🛑 通用排序也要過紅線。它不走 match(),所以要自己擋一次——
    //    不然客戶打一個某位人設明確不接的題目,她照樣會出現在名單上。
    const T0 = toks(q);
    RES = IDX.filter(o => !blocked(o, T0))
      .sort((a, b) => b.bd - a.bd).slice(0, 6).map(o => ({
      o, topic: 0, cate: 0, total: 0, hooks: [], kws: [], pil: [], fits: [], soft: [],
      catH: false, nHit: 0, sig: 0, best: false, wide: true }));
  }
  note.hidden = mode === 'hit';
  if (mode === 'hit') note.innerHTML = '';
  if (mode === 'mix')
    note.innerHTML = `<b>「${esc(q)}」在我們的人設設定裡只對到很少的字，</b>所以下面把最接近的
      <b class="g">${near.names.map(esc).join('＋')}</b>一起放進來排。
      標了<b class="g">字面命中</b>的那幾位，是這個字和這個品類都對得上，所以排在前面。
      <span class="s">虛擬人設的內容方向可以照你的產品重新設定，所以這是起點，不是篩選結果。</span>`;
  else if (mode === 'near')
    note.innerHTML = `<b>「${esc(q)}」在我們的人設設定裡沒有直接對應的字。</b>
      它最接近的是<b class="g">${near.names.map(esc).join('＋')}</b>，所以下面改用那個品類來排——
      分數是「她們現在的設定裡有多少現成切入點」，不是這個字本身的命中度。
      <span class="s">虛擬人設的內容方向可以照你的產品重新設定，所以這是起點，不是篩選結果。</span>`;
  else if (mode === 'wide')
    note.innerHTML = `<b>「${esc(q)}」這個產業，我們庫裡目前沒有現成的切入點。</b>
      下面列的是<b class="g">可切入面最廣</b>的幾位——她們的設定橫跨的品類最多，改成你的產業時最好接。
      <span class="s">這不是配對結果，是通用排序。虛擬人設的內容主題與語氣本來就可以照品牌需求重寫，
      所以「查不到」不等於做不了——直接跟我們談這個產業要怎麼設定會更快。</span>`;
  // 通用排序沒有兩軸可畫（分數全是 0，畫出來會是一堆疊在原點的點），整組收起來。
  document.getElementById('two').hidden = mode === 'wide';
  document.getElementById('rankh').textContent = mode === 'wide' ? '可切入面最廣的幾位' : '匹配度排行';
  document.getElementById('rankp').textContent = mode === 'wide'
    ? '這一段沒有分數——這個產業還沒有現成的切入點，所以排的是「設定橫跨最多品類」的順序。'
    : '點任一列，上面的拆解表會換成那一位。';
  const rank = document.getElementById('rank');
  if (mode !== 'wide') { drawPlot(RES); drawAnat(RES[0]); }
  rank.innerHTML = RES.slice(0, 8).map(r => {
    const words = [...new Set([...r.fits, ...r.pil, ...r.kws])].slice(0, 4);
    return `<div class="rrow" data-id="${r.o.id}"><span class="sc">${r.wide ? '—' : r.total}</span>
      <span class="nm">${esc(nameOf(r.o))}${r.lit ? '<span class="bdg">字面命中</span>' : ''}${
        r.best && !r.lit ? '<span class="bdg">全庫最高</span>' : ''}${r.wide ? '' : SIGB[r.sig]}</span>
      ${r.wide ? `<span class="mt">可切入 ${r.o.pil.length ? r.o.pil.length + ' 個內容主題' : '多個品類'}　${esc((r.o.fit || [])[0] || '')}</span>`
        : words.length ? `<span class="mt">${words.map(w => `<i>${esc(w)}</i>`).join('、')}</span>` : ''}</div>`;
  }).join('');
  rank.querySelectorAll('.rrow').forEach(el => el.addEventListener('click', () => {
    const r = RES.find(x => x.o.id === el.dataset.id); if (r) drawAnat(r); }));
  document.getElementById('rest').textContent = mode === 'wide' ? ''
    : RES.length > 8 ? `另外 ${RES.length - 8} 位也有命中，在圖上是灰色的點。` : '';
}


/* ── 啟動 ── */
const EG = ['精品旅宿','登山裝備','AI 工具','韓系保養','遊戲周邊','旗袍訂製','烘焙器材','高爾夫球具','咖啡豆','機能服飾'];
const egs = document.getElementById('egs');
EG.forEach(e => { const b = document.createElement('button'); b.textContent = e;
  b.addEventListener('click', () => { document.getElementById('q').value = e; renderQ(e); }); egs.appendChild(b); });
document.getElementById('go').addEventListener('click', () => renderQ(document.getElementById('q').value));
document.getElementById('q').addEventListener('keydown', e => { if (e.key === 'Enter') renderQ(e.target.value); });

document.getElementById('q').value = '精品旅宿';
renderQ('精品旅宿');
