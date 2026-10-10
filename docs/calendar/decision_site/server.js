// 2027 KOL 桌曆決策頁：只提供 public/ 底下的靜態檔，加上簡單存取保護（HTTP Basic）。
// 帳號密碼只從環境變數讀取（DECISION_USER／DECISION_PASS，在 Railway Variables 設定），不寫進前端或 repo；
// 沒設定就一律回 503，不提供任何內容。不記錄、不接收、不轉送任何使用者資料；沒有第三方服務。
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const ROOT = path.join(path.dirname(fileURLToPath(import.meta.url)), 'public');
const PORT = Number(process.env.PORT) || 8080;
const USER = process.env.DECISION_USER || '';
const PASS = process.env.DECISION_PASS || '';
const COMMIT = /^[0-9a-f]{7,40}$/.test(process.env.RAILWAY_GIT_COMMIT_SHA || '') ? process.env.RAILWAY_GIT_COMMIT_SHA : '';

const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.jpg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml', '.txt': 'text/plain; charset=utf-8' };

const BASE_HEADERS = {
  'X-Robots-Tag': 'noindex, nofollow, noarchive, nosnippet, noimageindex',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'no-referrer',
  'X-Frame-Options': 'DENY',
  'Cross-Origin-Resource-Policy': 'same-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), interest-cohort=()',
  'Content-Security-Policy': "default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; " +
    "connect-src 'none'; form-action 'none'; base-uri 'none'; frame-ancestors 'none'",
};

function digest(s) { return crypto.createHash('sha256').update(s, 'utf8').digest(); }
function same(a, b) { return crypto.timingSafeEqual(digest(a), digest(b)); }

// 失敗次數限制（記憶體內，每個 IP 10 分鐘 20 次）
const fails = new Map();
function clientIp(req) { return (req.headers['x-forwarded-for'] || '').split(',')[0].trim() || req.socket.remoteAddress || ''; }
function tooMany(ip) {
  const f = fails.get(ip);
  return f && f.n >= 20 && Date.now() - f.t < 10 * 60 * 1000;
}
function noteFail(ip) {
  const f = fails.get(ip);
  if (!f || Date.now() - f.t > 10 * 60 * 1000) fails.set(ip, { n: 1, t: Date.now() });
  else f.n += 1;
  if (fails.size > 5000) fails.clear();
}

function authorized(req) {
  const h = req.headers.authorization || '';
  if (!h.startsWith('Basic ')) return false;
  const dec = Buffer.from(h.slice(6), 'base64').toString('utf8');
  const i = dec.indexOf(':');
  if (i < 0) return false;
  const okU = same(dec.slice(0, i), USER);
  const okP = same(dec.slice(i + 1), PASS);
  return okU && okP;
}

function send(res, code, body, headers = {}) {
  res.writeHead(code, { ...BASE_HEADERS, 'Cache-Control': 'no-store', 'Content-Type': 'text/plain; charset=utf-8', ...headers });
  res.end(body);
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, 'http://x');
  if (url.pathname === '/healthz') return send(res, 200, 'ok');
  if (url.pathname === '/robots.txt') return send(res, 200, 'User-agent: *\nDisallow: /\n');
  // 通用月曆小圖示（不含任何素材）；瀏覽器抓 favicon 時常不帶憑證，所以不需要登入
  if (url.pathname === '/favicon.svg' || url.pathname === '/favicon.ico') {
    return send(res, 200, fs.readFileSync(path.join(ROOT, 'favicon.svg')), { 'Content-Type': 'image/svg+xml', 'Cache-Control': 'public, max-age=86400' });
  }
  if (req.method !== 'GET' && req.method !== 'HEAD') return send(res, 405, 'Method Not Allowed', { Allow: 'GET, HEAD' });
  if (!USER || !PASS) return send(res, 503, '存取保護尚未設定，暫不提供內容。');
  const ip = clientIp(req);
  if (tooMany(ip)) return send(res, 429, '嘗試次數過多，請稍後再試。');
  if (!authorized(req)) {
    if (req.headers.authorization) noteFail(ip);
    return send(res, 401, '需要帳號密碼。', { 'WWW-Authenticate': 'Basic realm="2027 KOL calendar decision", charset="UTF-8"' });
  }

  let rel;
  try { rel = decodeURIComponent(url.pathname); } catch { return send(res, 400, 'Bad Request'); }
  if (rel.endsWith('/')) rel += 'index.html';
  const file = path.normalize(path.join(ROOT, rel));
  if (!file.startsWith(ROOT + path.sep)) return send(res, 404, 'Not Found');
  const type = TYPES[path.extname(file).toLowerCase()];
  let st;
  try { st = fs.statSync(file); } catch { st = null; }
  if (!type || !st || !st.isFile()) return send(res, 404, 'Not Found');

  const isImg = type.startsWith('image/');
  const headers = { ...BASE_HEADERS, 'Content-Type': type,
    'Cache-Control': isImg ? 'private, max-age=3600' : 'private, no-cache' };
  if (file.endsWith('index.html')) {
    const html = fs.readFileSync(file, 'utf8').replace('__PAGE_COMMIT__', COMMIT || 'unknown');
    res.writeHead(200, headers);
    return res.end(req.method === 'HEAD' ? undefined : html);
  }
  res.writeHead(200, { ...headers, 'Content-Length': st.size });
  if (req.method === 'HEAD') return res.end();
  fs.createReadStream(file).pipe(res);
});

server.listen(PORT, () => {
  console.log(`decision page on :${PORT}; access protection ${USER && PASS ? 'configured' : 'NOT configured (serving 503)'}`);
});
