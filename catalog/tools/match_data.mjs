// 配對邏輯的唯一來源。三支程式共用:
//   build_match_index.mjs（診斷／看數字）、build_site.mjs（型錄的 /match.html 與人設頁雷達）
// 🛑 權重改一次就三個地方一起變,不要在別處另抄一份。
import fs from 'node:fs';

const ROOT = '/home/user/Virtual_KOL_Studio/catalog';

// ── 十個合作品類群。每一格的分數是 cell() 算的,不是手填,
//    所以這裡只需要說「這一群包含哪些詞」。
export const COLS = [
  { k: '服飾穿搭', w: ['服飾','穿搭','內衣','塑身','家居服','睡衣','棉麻','正裝','球衣','舞蹈服','運動服','襯衫','禮服','鞋','配件','時尚','ootd','outfit','試穿','選貨'] },
  { k: '美妝保養', w: ['保養','美妝','彩妝','護膚','底妝','防曬','美白','身體護理','美甲','香水','洗髮','skincare','眼妝','卸妝','面膜','精華'] },
  { k: '飯店旅遊', w: ['飯店','酒店','旅宿','旅行','旅遊','航空','行李','文旅','民宿','溫泉','hotel','travel','度假','觀光','城市'] },
  { k: '餐飲食品', w: ['食品','餐飲','外送','零食','烘焙','咖啡','茶','酒','飲','食材','甜點','麵包','消化','保健','小吃'] },
  { k: '運動健身', w: ['運動','健身','瑜珈','皮拉提斯','戶外','登山','高爾夫','恢復','筋膜','訓練','球具','機能','gym','肌肉','球衣'] },
  { k: '3C科技AI', w: ['科技','ai','3c','相機','耳機','音響','生產力','電商工具','直播設備','機器人','行車紀錄','金融科技','虛擬人','網路','工具'] },
  { k: '遊戲動漫', w: ['遊戲','電競','動漫','周邊','cosplay','假髮','手作','聯名','次文化','實況','桌遊'] },
  { k: '居家生活', w: ['家居','雜貨','香氛','器皿','花藝','園藝','助眠','寢具','生活雜貨','居家','舒緩','清潔','咖啡器具'] },
  { k: '精品配件', w: ['珠寶','腕錶','皮件','禮服','訂製','精品','高級','黑膠','書寫','鋼筆','旗袍','新中式'] },
  { k: '知識文化', w: ['書','課程','知識','文化','工藝','在地','紀錄片','歷史','傳統','教育','旅文','線上課'] },
];

// ── 同義詞。客戶打「爬山」,我們庫裡寫的是「登山」,不展開就查不到。
export const SYN = [
  ['旅宿','飯店','酒店','hotel','住宿','旅館'],
  ['保養','護膚','skincare','美妝','彩妝'],
  ['登山','爬山','戶外','hiking','outdoor','健行'],
  ['健身','訓練','重訓','gym','運動','fitness'],
  ['咖啡','咖啡廳','咖啡館','cafe','coffee'],
  ['旗袍','中式','漢服','新中式'],
  ['遊戲','電競','gaming','game','手遊'],
  ['烘焙','甜點','麵包','bakery','dessert'],
  ['穿搭','服飾','時尚','fashion','outfit','ootd'],
  ['旅遊','旅行','travel','觀光'],
  ['美食','吃播','餐飲','food'],
  ['汽車','改裝','車','car','automotive'],
  ['舞蹈','跳舞','dance'],
  ['花藝','花店','植物','flower'],
  ['高爾夫','高球','golf'],
  ['ai','人工智慧','生成式'],
];

// ── 索引:上線人設 × 關鍵詞。兩個來源,都不是編出來的。
//   ① Buildup_KOL 的 topic_affinity.json（18 位有）——pillar_keywords、topic_hooks、redlines
//   ② catalog.json（38 位都有）——支柱名、適合方向、領域、一句話定位、視覺調性、目標受眾
//   ③ copy.json 的 match_keywords——補給沒有 ① 的那 20 位
export function buildIndex() {
  const CAT = JSON.parse(fs.readFileSync(ROOT + '/data/catalog.json', 'utf8'));
  const SEL = JSON.parse(fs.readFileSync(ROOT + '/data/selection.json', 'utf8')).personas;
  const COPY = JSON.parse(fs.readFileSync(ROOT + '/data/copy.json', 'utf8'));
  const TA = id => { try {
    return JSON.parse(fs.readFileSync(`/home/user/Buildup_KOL/kols/${id}/topic_affinity.json`, 'utf8'));
  } catch { return null; } };
  const clean = s => String(s || '').replace(/\s*[（(][^）)]*[)）]/g, '').trim();

  const out = [];
  for (const p of CAT.personas.filter(p => SEL[p.id])) {
    const t = TA(p.id);
    const kw = new Set(), hooks = [], block = new Set();
    if (t?.pillar_keywords) for (const arr of Object.values(t.pillar_keywords)) arr.forEach(w => kw.add(w));
    if (t?.topic_hooks) for (const h of t.topic_hooks) {
      hooks.push({ t: h.title, a: h.angle, ev: !!h.evergreen, k: h.keywords || [] });
      (h.keywords || []).forEach(w => kw.add(w));
    }
    // 紅線:靜靜排除,不對客戶說「她不接什麼」
    if (t?.redlines) for (const r of t.redlines) if (r.severity === 'block') (r.keywords || []).forEach(w => block.add(w));
    (p.pillars || []).forEach(x => clean(x.name).split(/[\/、,，]/).forEach(w => { w = w.trim(); if (w.length >= 2) kw.add(w); }));
    (p.fit || []).forEach(f => clean(f).split(/[、,，（(]/).forEach(w => { w = w.trim(); if (w.length >= 2) kw.add(w); }));
    if (p.category) kw.add(p.category);
    ((COPY.match_keywords || {})[p.id] || []).forEach(w => kw.add(w));
    out.push({
      id: p.id, name: p.name, zh: p.name_zh || '', cat: p.category,
      tag: p.tagline || '', aud: p.audience || '', mood: p.mood || p.aesthetic_mood || '',
      pil: (p.pillars || []).map(x => x.name),
      pdesc: (p.pillars || []).map(x => x.desc || ''),
      fit: p.fit || [],
      rich: !!t, kw: [...kw], hooks, block: [...block],
    });
  }
  return out;
}

// ── 一格的分數。人設頁的雷達與 /match.html 的雷達說明用的是同一支。
const norm = s => String(s == null ? '' : s).toLowerCase().replace(/\s+/g, '');
const has = (text, w) => norm(text).includes(norm(w));
export function cell(o, col) {
  const fits = o.fit.filter(f => col.w.some(w => has(f, w)));
  const pil = o.pil.filter((x, i) => col.w.some(w => has(x, w) || has(o.pdesc[i] || '', w)));
  const kws = o.kw.filter(k => col.w.some(w => has(k, w)));
  const hooks = o.hooks.filter(h => col.w.some(w => has(h.t, w) || (h.k || []).some(x => has(x, w))));
  const catH = col.w.some(w => has(o.cat, w));
  return { v: Math.min(100, 26 * fits.length + 14 * hooks.length + 9 * pil.length + 4 * kws.length + (catH ? 18 : 0)),
           fits, pil, hooks: hooks.length, kws: kws.length };
}
