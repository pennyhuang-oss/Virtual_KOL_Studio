// 把配對器樣板 ＋ 配對索引組成一份可以直接開的 HTML。
// 這支目前只產原型（build/ 底下，不進 git、也不在型錄站的路由上）——
// 要不要併進型錄站是另一個決定，還沒做。
//
// 順序：node build_catalog.mjs → node build_match_index.mjs → node build_matcher.mjs
import fs from 'node:fs';

const ROOT = '/home/user/Virtual_KOL_Studio/catalog';
const OUT = process.env.MATCH_OUT || ROOT + '/build';
const CAT = JSON.parse(fs.readFileSync(ROOT + '/data/catalog.json', 'utf8'));
const byId = Object.fromEntries(CAT.personas.map(p => [p.id, p]));

const idx = JSON.parse(fs.readFileSync(OUT + '/match_index.json', 'utf8')).map(o => {
  const p = byId[o.id];
  return { id: o.id, name: o.name, zh: o.zh, cat: o.cat, rich: o.rich,
    tag: o.tag, aud: o.aud, mood: o.mood, kw: o.kw, block: o.block,
    pil: (p.pillars || []).map(x => x.name), fit: p.fit || [],
    hooks: o.hooks.map(h => ({ t: h.title ?? h.t, a: h.angle ?? h.a, ev: h.ev, k: h.k })) };
});

// 雷達的 10 個合作品類群。每一格的分數是頁面自己用同一套配對邏輯算的,不是手填,
// 所以這裡只需要給「這一群包含哪些詞」。
const COLS = [
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

// 同義詞。客戶打「爬山」我們庫裡寫「登山」,不展開就查不到。
const SYN = [
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

const html = fs.readFileSync(ROOT + '/tools/matcher.tpl.html', 'utf8')
  .replace('__INDEX__', JSON.stringify(idx))
  .replace('__COLS__', JSON.stringify(COLS))
  .replace('__SYN__', JSON.stringify(SYN));
for (const m of html.match(/__[A-Z]+__/g) || []) throw new Error('樣板還有沒填的空格 ' + m);
fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(OUT + '/kol-matcher.html', html);
console.log(`人設 ${idx.length}｜品類 ${COLS.length}｜同義詞 ${SYN.length} 組｜${(html.length / 1024).toFixed(0)} KB`);
console.log('→ ' + OUT + '/kol-matcher.html');
