// 建配對索引:38 位上線人設 × 關鍵詞。
// 兩個來源,都不是編出來的:
//   ① Buildup_KOL 的 topic_affinity.json（18 位有）——pillar_keywords、topic_hooks、redlines
//   ② catalog.json（38 位都有）——支柱名、適合方向、領域、一句話定位、視覺調性、目標受眾
import fs from 'node:fs';
const CAT = JSON.parse(fs.readFileSync('/home/user/Virtual_KOL_Studio/catalog/data/catalog.json', 'utf8'));
const SEL = JSON.parse(fs.readFileSync('/home/user/Virtual_KOL_Studio/catalog/data/selection.json', 'utf8')).personas;
const TA = id => { const f = `/home/user/Buildup_KOL/kols/${id}/topic_affinity.json`;
  try { return JSON.parse(fs.readFileSync(f, 'utf8')); } catch { return null; } };

const COPY = JSON.parse(fs.readFileSync('/home/user/Virtual_KOL_Studio/catalog/data/copy.json', 'utf8'));
const clean = s => String(s || '').replace(/\s*[（(][^）)]*[)）]/g, '').trim();
const out = [];
for (const p of CAT.personas.filter(p => SEL[p.id])) {
  const t = TA(p.id);
  const kw = new Set(), hooks = [], block = new Set();
  // ① 支柱關鍵字
  if (t?.pillar_keywords) for (const arr of Object.values(t.pillar_keywords)) arr.forEach(w => kw.add(w));
  // ① 題目連結點
  if (t?.topic_hooks) for (const h of t.topic_hooks) {
    hooks.push({ t: h.title, a: h.angle, ev: !!h.evergreen, k: h.keywords || [] });
    (h.keywords || []).forEach(w => kw.add(w));
  }
  // ① 紅線(靜靜排除,不對客戶說「她不接什麼」)
  if (t?.redlines) for (const r of t.redlines) if (r.severity === 'block') (r.keywords || []).forEach(w => block.add(w));
  // ② 型錄本來就有的欄位
  p.pillars.forEach(x => { clean(x.name).split(/[\/、,，]/).forEach(w => { w = w.trim(); if (w.length >= 2) kw.add(w); }); });
  (p.fit || []).forEach(f => clean(f).split(/[、,，（(]/).forEach(w => { w = w.trim(); if (w.length >= 2) kw.add(w); }));
  if (p.category) kw.add(p.category);
  // ③ copy.json 的 match_keywords:補給沒有 topic_affinity.json 的那 20 位。
  //    有 topic_affinity 的不覆寫（那邊的關鍵詞更細,而且是同一份資料的來源）。
  ((COPY.match_keywords || {})[p.id] || []).forEach(w => kw.add(w));
  out.push({
    id: p.id, name: p.name, zh: p.name_zh || '', age: p.age, cat: p.category,
    tag: p.tagline || '', aud: p.audience || '', mood: p.mood || p.aesthetic_mood || '',
    loc: p.location || '', langs: p.languages || [],
    imgs: SEL[p.id].gallery.length, vids: (SEL[p.id].videos || []).length,
    rich: !!t, kw: [...kw], hooks, block: [...block],
  });
}
const rich = out.filter(o => o.rich);
console.log(`人設 ${out.length} 位｜有 topic_affinity 的 ${rich.length} 位`);
console.log(`關鍵詞:平均每位 ${(out.reduce((a, o) => a + o.kw.length, 0) / out.length).toFixed(1)} 個`);
console.log(`  有 affinity 的平均 ${(rich.reduce((a, o) => a + o.kw.length, 0) / rich.length).toFixed(1)} 個`);
const thin = out.filter(o => !o.rich);
console.log(`  只有型錄欄位的 ${thin.length} 位平均 ${(thin.reduce((a, o) => a + o.kw.length, 0) / thin.length).toFixed(1)} 個｜最少 ${Math.min(...thin.map(o => o.kw.length))}`);
console.log(`題目連結點 ${out.reduce((a, o) => a + o.hooks.length, 0)} 個｜block 紅線詞 ${out.reduce((a, o) => a + o.block.length, 0)} 個`);
console.log('--- 只有型錄欄位那批的關鍵詞長什麼樣（angel-chiu）---');
console.log(out.find(o => o.id === 'angel-chiu').kw.join('、'));
// 索引是衍生檔,不進 git（跑一次就重建）。MATCH_OUT 可指到別處。
const OUT = process.env.MATCH_OUT || '/home/user/Virtual_KOL_Studio/catalog/build';
fs.mkdirSync(OUT, { recursive: true });
const f = OUT + '/match_index.json';
fs.writeFileSync(f, JSON.stringify(out));
console.log('索引', f, (fs.statSync(f).size / 1024).toFixed(0), 'KB');
