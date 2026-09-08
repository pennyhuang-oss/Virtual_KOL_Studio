'use strict';
/**
 * Static server for the 897 audition plan site.
 *
 * Dependency-free on purpose: Railway builds it in seconds and there is no
 * npm supply chain to worry about for a site that goes in front of a client.
 *
 * Range requests are implemented because the page plays mp4 — without them
 * Safari refuses to start playback.
 *
 * Set SITE_PASSWORD to put the whole site behind a shared passphrase.
 */
const http = require('http');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const PORT = process.env.PORT || 3000;
const ROOT = path.join(__dirname, 'public');
const PASSWORD = process.env.SITE_PASSWORD || '';
// Cookie value is derived from the password, so rotating the password
// invalidates every session that was issued under the old one.
const TOKEN = PASSWORD
  ? crypto.createHash('sha256').update(`897:${PASSWORD}`).digest('hex').slice(0, 32)
  : '';

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webp': 'image/webp',
  '.jpg': 'image/jpeg',
  '.png': 'image/png',
  '.mp4': 'video/mp4',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
};

const LOGIN_PAGE = `<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>897 女團選秀企劃</title><style>
:root{color-scheme:dark}
body{margin:0;min-height:100vh;display:grid;place-items:center;background:#0b0b0f;
color:#f4f4f6;font:15px/1.6 "Noto Sans TC",-apple-system,BlinkMacSystemFont,"PingFang TC","Microsoft JhengHei",sans-serif}
form{width:min(88vw,340px);text-align:center}
h1{font-size:15px;letter-spacing:.32em;font-weight:500;color:#8a8a99;margin:0 0 6px}
p{font-size:13px;color:#6a6a78;margin:0 0 28px}
input{width:100%;box-sizing:border-box;padding:13px 15px;border-radius:9px;
border:1px solid #2a2a34;background:#14141b;color:#f4f4f6;font-size:15px;text-align:center;letter-spacing:.1em}
input:focus{outline:none;border-color:#c9a86a}
button{width:100%;margin-top:11px;padding:13px;border:0;border-radius:9px;
background:#c9a86a;color:#14141b;font-size:14px;font-weight:600;letter-spacing:.16em;cursor:pointer}
button:hover{background:#d8bb82}
.err{color:#e0777f;font-size:13px;margin-top:14px;min-height:19px}
</style></head><body><form method="POST" action="/__login">
<h1>897 女團選秀</h1><p>本頁為企劃討論用，請輸入通行碼</p>
<input name="password" type="password" autocomplete="current-password" autofocus placeholder="通行碼">
<button type="submit">進入</button><div class="err">__ERR__</div>
</form></body></html>`;

function authed(req) {
  if (!PASSWORD) return true;
  const cookie = req.headers.cookie || '';
  return cookie.split(';').some((c) => c.trim() === `s897=${TOKEN}`);
}

function sendLogin(res, err) {
  const body = LOGIN_PAGE.replace('__ERR__', err ? '通行碼不正確' : '');
  res.writeHead(err ? 401 : 200, {
    'Content-Type': 'text/html; charset=utf-8',
    'Cache-Control': 'no-store',
  });
  res.end(body);
}

function serve(req, res, filePath) {
  fs.stat(filePath, (err, stat) => {
    if (err || !stat.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      return res.end('404');
    }
    const type = TYPES[path.extname(filePath).toLowerCase()] || 'application/octet-stream';
    // Media is content-addressed by build; markup and data must stay fresh.
    const cache = /\.(webp|mp4|jpg|png|svg)$/i.test(filePath)
      ? 'public, max-age=86400'
      : 'no-cache';
    const range = req.headers.range;

    if (range && type === 'video/mp4') {
      const m = /^bytes=(\d*)-(\d*)$/.exec(range);
      if (m) {
        let start = m[1] ? parseInt(m[1], 10) : 0;
        let end = m[2] ? parseInt(m[2], 10) : stat.size - 1;
        if (Number.isNaN(start) || Number.isNaN(end) || start > end || end >= stat.size) {
          end = Math.min(end, stat.size - 1);
          start = Math.min(start, end);
        }
        res.writeHead(206, {
          'Content-Type': type,
          'Content-Length': end - start + 1,
          'Content-Range': `bytes ${start}-${end}/${stat.size}`,
          'Accept-Ranges': 'bytes',
          'Cache-Control': cache,
        });
        return fs.createReadStream(filePath, { start, end }).pipe(res);
      }
    }

    res.writeHead(200, {
      'Content-Type': type,
      'Content-Length': stat.size,
      'Accept-Ranges': type === 'video/mp4' ? 'bytes' : 'none',
      'Cache-Control': cache,
      'X-Content-Type-Options': 'nosniff',
      'Referrer-Policy': 'no-referrer',
      // The plan is not for search engines or embedding elsewhere.
      'X-Robots-Tag': 'noindex, nofollow, noarchive',
    });
    fs.createReadStream(filePath).pipe(res);
  });
}

http.createServer((req, res) => {
  const url = new URL(req.url, 'http://x');

  if (url.pathname === '/__login' && req.method === 'POST') {
    let body = '';
    req.on('data', (c) => {
      body += c;
      if (body.length > 2048) req.destroy();
    });
    return req.on('end', () => {
      const got = new URLSearchParams(body).get('password') || '';
      const a = Buffer.from(got);
      const b = Buffer.from(PASSWORD);
      const ok = a.length === b.length && crypto.timingSafeEqual(a, b);
      if (!ok) return sendLogin(res, true);
      res.writeHead(302, {
        'Set-Cookie': `s897=${TOKEN}; Path=/; HttpOnly; SameSite=Lax; Max-Age=2592000`,
        Location: '/',
      });
      res.end();
    });
  }

  if (url.pathname === '/healthz') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    return res.end('ok');
  }

  if (!authed(req)) return sendLogin(res, false);

  // Resolve inside ROOT only — no path traversal out of public/.
  const rel = decodeURIComponent(url.pathname).replace(/^\/+/, '') || 'index.html';
  const target = path.resolve(ROOT, rel);
  if (target !== ROOT && !target.startsWith(ROOT + path.sep)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    return res.end('403');
  }
  serve(req, res, fs.existsSync(target) && fs.statSync(target).isDirectory()
    ? path.join(target, 'index.html')
    : target);
}).listen(PORT, () => {
  console.log(`897 audition site on :${PORT}${PASSWORD ? ' (password protected)' : ''}`);
});
