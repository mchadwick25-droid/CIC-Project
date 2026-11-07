
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

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const isRead = request.method === 'GET' || request.method === 'HEAD';
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
