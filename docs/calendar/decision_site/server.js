// 2027 KOL 桌曆決策頁：只提供 public/ 底下的靜態檔。公開可讀、不需登入（Penny 2026-10-12 同意，見 CAL_17）。
// noindex／robots.txt 只是請搜尋引擎不要收錄，不是存取保護。不記錄、不接收、不轉送任何使用者資料；沒有第三方服務。
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.join(path.dirname(fileURLToPath(import.meta.url)), 'public');
const PORT = Number(process.env.PORT) || 8080;
const COMMIT = /^[0-9a-f]{7,40}$/.test(process.env.RAILWAY_GIT_COMMIT_SHA || '') ? process.env.RAILWAY_GIT_COMMIT_SHA : '';

const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.jpg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml', '.txt': 'text/plain; charset=utf-8', '.pdf': 'application/pdf' };

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

function send(res, code, body, headers = {}) {
  res.writeHead(code, { ...BASE_HEADERS, 'Cache-Control': 'no-store', 'Content-Type': 'text/plain; charset=utf-8', ...headers });
  res.end(body);
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, 'http://x');
  if (url.pathname === '/healthz') return send(res, 200, 'ok');
  if (url.pathname === '/robots.txt') return send(res, 200, 'User-agent: *\nDisallow: /\n');
  // 通用月曆小圖示（不含任何素材）
  if (url.pathname === '/favicon.svg' || url.pathname === '/favicon.ico') {
    return send(res, 200, fs.readFileSync(path.join(ROOT, 'favicon.svg')), { 'Content-Type': 'image/svg+xml', 'Cache-Control': 'public, max-age=86400' });
  }
  if (req.method !== 'GET' && req.method !== 'HEAD') return send(res, 405, 'Method Not Allowed', { Allow: 'GET, HEAD' });

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
    'Cache-Control': isImg ? 'public, max-age=3600' : 'no-cache' };
  // 排版預覽 PDF（M-5 R26 起）：一律下載，不在頁面內嵌開啟；檔名只用英數
  if (type === 'application/pdf') headers['Content-Disposition'] = `attachment; filename="${path.basename(file).replace(/[^A-Za-z0-9._-]/g, '_')}"`;
  if (file.endsWith('.html')) {
    const html = fs.readFileSync(file, 'utf8').replace('__PAGE_COMMIT__', COMMIT || 'unknown');
    res.writeHead(200, headers);
    return res.end(req.method === 'HEAD' ? undefined : html);
  }
  res.writeHead(200, { ...headers, 'Content-Length': st.size });
  if (req.method === 'HEAD') return res.end();
  fs.createReadStream(file).pipe(res);
});

server.listen(PORT, () => {
  console.log(`decision page on :${PORT}; public, no login`);
});
