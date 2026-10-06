// Byte-range support for the audio under /audio/.
//
// Cloudflare's static-asset serving ignores a Range header: it answers 200 with
// the whole file and no Accept-Ranges. iPhone Safari first asks for bytes=0-1
// and only accepts a 206 answer, so it needs this to play and seek narration
// reliably. The recordings (.mp3) are read from the R2 bucket bound as AUDIO
// when there is one, and from the static assets otherwise, or when the bucket
// does not hold the file. Everything else, including the small manifest files
// under /audio/, goes straight to the assets, unchanged.

// The baseline security headers of cic-website/_headers. A response built here
// does not pass through that file, so they are repeated; a test keeps the two
// in step.
export const BASELINE_HEADERS = {
  'Strict-Transport-Security': 'max-age=31536000',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), payment=()',
};

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

function bucketHeaders(object) {
  const out = new Headers(BASELINE_HEADERS);
  out.set('Content-Type', (object.httpMetadata && object.httpMetadata.contentType) || 'audio/mpeg');
  out.set('Accept-Ranges', 'bytes');
  out.set('Cache-Control', 'public, max-age=0, must-revalidate');
  if (object.httpEtag) out.set('ETag', object.httpEtag);
  return out;
}

/**
 * Answer from the bucket: null when the file is not there (the caller then
 * falls back to the assets), otherwise a 200, 206, 304 or 416 response.
 */
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

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const isRead = request.method === 'GET' || request.method === 'HEAD';
    const isRecording = url.pathname.startsWith('/audio/') && url.pathname.endsWith('.mp3');
    if (!isRecording || !isRead) return env.ASSETS.fetch(request);

    if (env.AUDIO) {
      try {
        const answer = await fromBucket(request, env.AUDIO, decodeURIComponent(url.pathname.slice(1)));
        if (answer) return answer;
      } catch (err) {
        // The bucket is unreachable: serve from the assets rather than fail.
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
