// Byte-range support for the audio under /audio/.
//
// Cloudflare's static-asset serving ignores a Range header: it answers 200 with
// the whole file and no Accept-Ranges. iPhone Safari first asks for bytes=0-1
// and only accepts a 206 answer, so it needs this to play and seek narration
// reliably. Every other request goes straight to the assets, unchanged.

/**
 * Parse a single-range header against a file size.
 * Returns {start, end} (inclusive), null when the range cannot be satisfied
 * (416), or 'ignore' when the header is not a single bytes range (serve 200).
 */
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

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const isAudio = url.pathname.startsWith('/audio/');
    const isRead = request.method === 'GET' || request.method === 'HEAD';
    if (!isAudio || !isRead) return env.ASSETS.fetch(request);

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
