
export const BASELINE_HEADERS = {
  'Strict-Transport-Security': 'max-age=31536000',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), payment=()',
};

export function parseRange(header, size) {
  const m = /^bytes=(\d*)-(\d*)$/.exec((header || '').trim());
  if (!m) return 'ignore';
  const [, a, b] = m;
  if (a === '' && b === '') return 'ignore';
  let start, end;
  if (a === '') {
    const suffix = Number(b);
    if (suffix === 0) return null;
    start = Math.max(0, size - suffix);
    end = size - 1;
  } else {
    start = Number(a);
    end = b === '' ? size - 1 : Math.min(Number(b), size - 1);
  }
  if (start >= size || start > end) return null;
  return { start, end };
}

function bucketHeaders(object) {
  const out = new Headers(BASELINE_HEADERS);
  out.set('Content-Type', (object.httpMetadata && object.httpMetadata.contentType) || 'audio/mpeg');
  out.set('Accept-Ranges', 'bytes');
  out.set('Cache-Control', 'public, max-age=0, must-revalidate');
  if (object.httpEtag) out.set('ETag', object.httpEtag);
  return out;
}

async function fromBucket(request, bucket, key) {
  const head = await bucket.head(key);
  if (!head) return null;
  const size = head.size;
  const out = bucketHeaders(head);
  if (head.httpEtag && request.headers.get('If-None-Match') === head.httpEtag) {
    return new Response(null, { status: 304, headers: out });
  }
  if (request.method === 'HEAD') {
    out.set('Content-Length', String(size));
    return new Response(null, { status: 200, headers: out });
  }
  const range = parseRange(request.headers.get('Range'), size);
  if (range === null) {
    out.set('Content-Range', `bytes */${size}`);
    return new Response(null, { status: 416, headers: out });
  }
  if (range === 'ignore') {
    const whole = await bucket.get(key);
    if (!whole) return null;
    out.set('Content-Length', String(size));
    return new Response(whole.body, { status: 200, headers: out });
  }
  const part = await bucket.get(key, { range: { offset: range.start, length: range.end - range.start + 1 } });
  if (!part) return null;
  out.set('Content-Range', `bytes ${range.start}-${range.end}/${size}`);
  out.set('Content-Length', String(range.end - range.start + 1));
  return new Response(part.body, { status: 206, headers: out });
}

const MAP_PATHS = new Set(['/atlas', '/atlas.html', '/atlas-v3', '/atlas-v3.html', '/world-atlas', '/world-atlas.html', '/tree', '/tree/']);
const MOVED_AUDIO = /^\/audio\/(tree|docstories|stories)\//;
const TREE_PAGE = /^\/tree\/([^/]+?)(?:\.html)?$/;

let renamesPromise = null;
function retiredRedirects(env, origin) {
  if (!renamesPromise) {
    renamesPromise = env.ASSETS.fetch(new Request(origin + '/data/world-census.json'))
      .then(r => (r.ok ? r.json() : {}))
      .then(d => new Map((d.retiredMovements || []).filter(m => m.redirectTo).map(m => [m.id, m.redirectTo])))
      .catch(() => { renamesPromise = null; return new Map(); });
  }
  return renamesPromise;
}

export async function treeRedirect(url, env) {
  const home = env.TREE_ORIGIN;
  if (!home) return null;
  const path = url.pathname;
  let target = null;
  if (MAP_PATHS.has(path)) target = home + '/';
  else if (MOVED_AUDIO.test(path)) target = home + path;
  else {
    const m = TREE_PAGE.exec(path);
    if (m) {
      const id = decodeURIComponent(m[1]);
      const renamed = (await retiredRedirects(env, url.origin)).get(id);
      target = home + '/tree/' + encodeURIComponent(renamed || id);
    }
  }
  if (!target) return null;
  const headers = new Headers(BASELINE_HEADERS);
  headers.set('Location', target + url.search);
  headers.set('Cache-Control', 'public, max-age=3600');
  return new Response(null, { status: 301, headers });
}

export function resetRenamesForTests() { renamesPromise = null; }

// Anonymous use counts from the Church Family Tree map, written to Workers Analytics Engine
// (binding EVENTS, set only in wrangler.cft.jsonc). The map sends only these event types and
// short fields: no identity, no typed text, no address. Bots and link previews are dropped.
export const EVENT_TYPES = new Set(['visit', 'open', 'listen', 'tour', 'layer', 'active', 'grow', 'next', 'owner']);
const BOT_AGENT = /bot|crawl|spider|slurp|preview|facebookexternalhit|headless|lighthouse|python|curl|wget|httpclient/i;
const MAX_BODY = 8192;
const MAX_EVENTS = 25;
const field = (v, n) => (typeof v === 'string' ? v.replace(/[^\w .:/-]/g, '').slice(0, n) : '');
const visitorId = (v) => (typeof v === 'string' && /^[a-f0-9]{32}$/.test(v) ? v : '');
const browserFamily = (ua) => (/edg\//i.test(ua) ? 'edge' : /opr\/|opera/i.test(ua) ? 'opera' : /firefox|fxios/i.test(ua) ? 'firefox' : /chrome|crios/i.test(ua) ? 'chrome' : /safari/i.test(ua) ? 'safari' : 'other');
const number = (v) => (Number.isFinite(v) && v >= 0 && v <= 86400 ? v : 0);

export function eventPoints(text, where = {}) {
  let list;
  try { list = JSON.parse(text); } catch { return []; }
  if (!Array.isArray(list)) return [];
  return list.slice(0, MAX_EVENTS)
    .filter((e) => e && typeof e === 'object' && EVENT_TYPES.has(e.t))
    .map((e) => ({
      indexes: [e.t],
      blobs: [e.t, field(e.a, 40), field(e.b, 120), field(e.c, 40), visitorId(e.v), field(where.country, 2), field(where.region, 40), field(where.browser, 10), field(where.city, 40), field(e.d, 100)],
      doubles: (Array.isArray(e.n) ? e.n : [e.n]).slice(0, 3).map(number),
    }));
}

const CONSENT_COUNTRIES = new Set(['AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'IS', 'LI', 'NO', 'GB', 'CH']);

// Tells the page whether to ask for consent: Europe (EU, EEA, UK, Switzerland) only. Nothing about the visitor is kept.
export function regionNote(request) {
  const country = String((request.cf || {}).country || '');
  const body = country ? JSON.stringify({ eu: CONSENT_COUNTRIES.has(country) }) : '{}';
  return new Response(body, { status: 200, headers: { ...BASELINE_HEADERS, 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });
}

export async function countEvents(request, env) {
  const done = new Response(null, { status: 204, headers: BASELINE_HEADERS });
  if (request.method !== 'POST') return new Response(null, { status: 405, headers: { ...BASELINE_HEADERS, Allow: 'POST' } });
  if (!env.EVENTS || BOT_AGENT.test(request.headers.get('User-Agent') || '')) return done;
  const owner = String(env.OWNER_IPS || '').split(',').map((v) => v.trim()).filter(Boolean);
  if (owner.includes(request.headers.get('CF-Connecting-IP') || '')) return done;
  if (Number(request.headers.get('Content-Length') || 0) > MAX_BODY) return new Response(null, { status: 413, headers: BASELINE_HEADERS });
  const text = await request.text();
  if (text.length > MAX_BODY) return new Response(null, { status: 413, headers: BASELINE_HEADERS });
  const cf = request.cf || {};
  const where = { country: cf.country, region: cf.region, city: cf.city, browser: browserFamily(request.headers.get('User-Agent') || '') };
  for (const point of eventPoints(text, where)) env.EVENTS.writeDataPoint(point);
  return done;
}


// Link-preview crawlers read a page's head for its title, description and picture. LinkedIn refuses a
// page over 3,145,728 bytes, and the map's home page is about 9.5 MB, so these crawlers get a small
// page made from the same head tags. Only the tree's Worker runs for "/" (run_worker_first in
// wrangler.cft.jsonc); everyone else gets the page itself.
export const UNFURLER = /LinkedInBot|Twitterbot|Slackbot|Discordbot|WhatsApp|TelegramBot|facebookexternalhit|Facebot|SkypeUriPreview|Pinterestbot/i;
const HEAD_LIMIT = 65536;
const PREVIEW_TAG = /<(?:title\b[^>]*>[^<]*<\/title>|meta\s+(?:name="(?:description|twitter:[^"]*)"|property="og:[^"]*")[^>]*>|link\s+rel="canonical"[^>]*>)/gi;

export async function previewPage(request, env) {
  const upstream = await env.ASSETS.fetch(new Request(request.url, { method: 'GET', headers: { Accept: 'text/html' } }));
  if (!upstream.ok || !upstream.body) return upstream;
  const reader = upstream.body.getReader();
  const decoder = new TextDecoder();
  let head = '';
  while (head.length < HEAD_LIMIT && !/<\/head>/i.test(head)) {
    const { done, value } = await reader.read();
    if (done) break;
    head += decoder.decode(value, { stream: true });
  }
  await reader.cancel();
  const tags = (head.match(PREVIEW_TAG) || []).join('\n');
  if (!tags) return env.ASSETS.fetch(request);
  const html = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n' + tags + '\n</head><body><p><a href="/">Open the Church Family Tree</a></p></body></html>\n';
  const headers = new Headers(BASELINE_HEADERS);
  headers.set('Content-Type', 'text/html; charset=utf-8');
  headers.set('Cache-Control', 'no-store');
  headers.set('Vary', 'User-Agent');
  return new Response(request.method === 'HEAD' ? null : html, { status: 200, headers });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/e') return countEvents(request, env);
    if (url.pathname === '/region') return regionNote(request);
    const isRead = request.method === 'GET' || request.method === 'HEAD';
    if ((url.pathname === '/' || url.pathname === '/index.html') && isRead && UNFURLER.test(request.headers.get('User-Agent') || '')) return previewPage(request, env);
    const moved = await treeRedirect(url, env);
    if (moved) return moved;
    const isRecording = url.pathname.startsWith('/audio/') && url.pathname.endsWith('.mp3');
    if (!isRecording || !isRead) return env.ASSETS.fetch(request);

    if (env.AUDIO) {
      try {
        const answer = await fromBucket(request, env.AUDIO, decodeURIComponent(url.pathname.slice(1)));
        if (answer) return answer;
      } catch (err) {
      }
    }

    const rangeHeader = request.headers.get('Range');
    const headers = new Headers(request.headers);
    headers.delete('Range');
    headers.delete('If-Range');
    const upstream = await env.ASSETS.fetch(new Request(request.url, { method: request.method, headers }));
    if (!upstream.ok) return upstream;

    const out = new Headers(upstream.headers);
    out.set('Accept-Ranges', 'bytes');
    if (!rangeHeader || request.method === 'HEAD' || upstream.status !== 200) {
      return new Response(upstream.body, { status: upstream.status, statusText: upstream.statusText, headers: out });
    }

    const buf = await upstream.arrayBuffer();
    const size = buf.byteLength;
    const range = parseRange(rangeHeader, size);
    if (range === 'ignore') {
      return new Response(buf, { status: 200, headers: out });
    }
    if (range === null) {
      out.delete('Content-Length');
      out.set('Content-Range', `bytes */${size}`);
      return new Response(null, { status: 416, headers: out });
    }
    out.set('Content-Range', `bytes ${range.start}-${range.end}/${size}`);
    out.set('Content-Length', String(range.end - range.start + 1));
    return new Response(buf.slice(range.start, range.end + 1), { status: 206, headers: out });
  },
};
