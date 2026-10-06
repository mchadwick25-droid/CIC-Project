import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import worker, { parseRange, BASELINE_HEADERS } from './worker.mjs';

const FILE = Buffer.from(Array.from({ length: 100 }, (_, i) => i));

function envWith(files) {
  return {
    ASSETS: {
      calls: [],
      async fetch(req) {
        this.calls.push({ url: req.url, range: req.headers.get('Range'), method: req.method });
        const p = new URL(req.url).pathname;
        if (!(p in files)) return new Response('not found', { status: 404 });
        return new Response(req.method === 'HEAD' ? null : files[p], {
          status: 200,
          headers: { 'Content-Type': 'audio/mpeg', 'Content-Length': String(files[p].length), ETag: '"abc"', 'Cache-Control': 'public, max-age=0, must-revalidate' },
        });
      },
    },
  };
}
const get = (path, headers = {}, method = 'GET') => new Request('https://example.test' + path, { method, headers });

test('parseRange: open end, closed, suffix, clamped end', () => {
  assert.deepEqual(parseRange('bytes=0-1', 100), { start: 0, end: 1 });
  assert.deepEqual(parseRange('bytes=10-', 100), { start: 10, end: 99 });
  assert.deepEqual(parseRange('bytes=-5', 100), { start: 95, end: 99 });
  assert.deepEqual(parseRange('bytes=90-500', 100), { start: 90, end: 99 });
});

test('parseRange: unsatisfiable is null; not a single bytes range is ignored', () => {
  assert.equal(parseRange('bytes=100-', 100), null);
  assert.equal(parseRange('bytes=50-10', 100), null);
  assert.equal(parseRange('bytes=-0', 100), null);
  assert.equal(parseRange('bytes=0-1,5-6', 100), 'ignore');
  assert.equal(parseRange('items=0-1', 100), 'ignore');
  assert.equal(parseRange('bytes=-', 100), 'ignore');
});

test('Safari probe: bytes=0-1 on audio answers 206 with the right bytes and headers', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 206);
  assert.equal(res.headers.get('Content-Range'), 'bytes 0-1/100');
  assert.equal(res.headers.get('Content-Length'), '2');
  assert.equal(res.headers.get('Accept-Ranges'), 'bytes');
  assert.equal(res.headers.get('Content-Type'), 'audio/mpeg');
  assert.deepEqual([...Buffer.from(await res.arrayBuffer())], [0, 1]);
  assert.equal(env.ASSETS.calls[0].range, null, 'the asset fetch carries no Range header');
});

test('a later range returns exactly that slice', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=40-' }), env);
  assert.equal(res.status, 206);
  assert.equal(res.headers.get('Content-Range'), 'bytes 40-99/100');
  assert.deepEqual([...Buffer.from(await res.arrayBuffer())], [...FILE.subarray(40)]);
});

test('no Range: 200 with the whole file and Accept-Ranges advertised', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3'), env);
  assert.equal(res.status, 200);
  assert.equal(res.headers.get('Accept-Ranges'), 'bytes');
  assert.equal(res.headers.get('ETag'), '"abc"');
  assert.equal((await res.arrayBuffer()).byteLength, 100);
});

test('unsatisfiable range: 416 with Content-Range */size', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=500-' }), env);
  assert.equal(res.status, 416);
  assert.equal(res.headers.get('Content-Range'), 'bytes */100');
});

test('multi-range is ignored: 200 with the whole file', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=0-1,5-6' }), env);
  assert.equal(res.status, 200);
  assert.equal((await res.arrayBuffer()).byteLength, 100);
});

test('HEAD advertises Accept-Ranges and sends no body', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', {}, 'HEAD'), env);
  assert.equal(res.status, 200);
  assert.equal(res.headers.get('Accept-Ranges'), 'bytes');
});

test('a missing audio file is passed through as 404', async () => {
  const env = envWith({});
  const res = await worker.fetch(get('/audio/none.mp3', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 404);
});

test('anything outside /audio/ goes straight to the assets, Range untouched', async () => {
  const env = envWith({ '/data/x.json': FILE });
  const res = await worker.fetch(get('/data/x.json', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 200);
  assert.equal(env.ASSETS.calls[0].range, 'bytes=0-1');
});

test('non-read methods on /audio/ go straight to the assets', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  await worker.fetch(get('/audio/a.mp3', {}, 'POST'), env);
  assert.equal(env.ASSETS.calls[0].method, 'POST');
});

// ---- the R2 bucket bound as AUDIO ----

function bucketWith(objects, { throws = false } = {}) {
  const calls = [];
  return {
    calls,
    async head(key) {
      calls.push(['head', key]);
      if (throws) throw new Error('bucket unreachable');
      if (!(key in objects)) return null;
      return { size: objects[key].length, httpEtag: '"r2etag"', httpMetadata: { contentType: 'audio/mpeg' } };
    },
    async get(key, opts) {
      calls.push(['get', key, opts && opts.range]);
      if (!(key in objects)) return null;
      const r = opts && opts.range;
      const body = r ? objects[key].subarray(r.offset, r.offset + r.length) : objects[key];
      return { body: new Blob([body]).stream() };
    },
  };
}
const withBucket = (files, objects, opts) => ({ ...envWith(files), AUDIO: bucketWith(objects, opts) });

test('bucket: a range is read from the bucket, with a 206 and the right bytes', async () => {
  const env = withBucket({}, { 'audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=10-19' }), env);
  assert.equal(res.status, 206);
  assert.equal(res.headers.get('Content-Range'), 'bytes 10-19/100');
  assert.equal(res.headers.get('Content-Length'), '10');
  assert.equal(res.headers.get('ETag'), '"r2etag"');
  assert.deepEqual([...Buffer.from(await res.arrayBuffer())], [...FILE.subarray(10, 20)]);
  assert.deepEqual(env.AUDIO.calls[1], ['get', 'audio/a.mp3', { offset: 10, length: 10 }]);
  assert.equal(env.ASSETS.calls.length, 0, 'the assets are not touched');
});

test('bucket: whole file, HEAD, 416 and the conditional 304', async () => {
  const env = withBucket({}, { 'audio/a.mp3': FILE });
  const whole = await worker.fetch(get('/audio/a.mp3'), env);
  assert.equal(whole.status, 200);
  assert.equal(whole.headers.get('Accept-Ranges'), 'bytes');
  assert.equal((await whole.arrayBuffer()).byteLength, 100);
  const head = await worker.fetch(get('/audio/a.mp3', {}, 'HEAD'), env);
  assert.equal(head.status, 200);
  assert.equal(head.headers.get('Content-Length'), '100');
  const bad = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=500-' }), env);
  assert.equal(bad.status, 416);
  assert.equal(bad.headers.get('Content-Range'), 'bytes */100');
  const same = await worker.fetch(get('/audio/a.mp3', { 'If-None-Match': '"r2etag"' }), env);
  assert.equal(same.status, 304);
});

test('bucket: a file the bucket lacks falls back to the assets', async () => {
  const env = withBucket({ '/audio/old.mp3': FILE }, {});
  const res = await worker.fetch(get('/audio/old.mp3', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 206);
  assert.equal(env.ASSETS.calls.length, 1);
});

test('bucket: an unreachable bucket falls back to the assets instead of failing', async () => {
  const env = withBucket({ '/audio/a.mp3': FILE }, { 'audio/a.mp3': FILE }, { throws: true });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 206);
  assert.deepEqual([...Buffer.from(await res.arrayBuffer())], [0, 1]);
});

test('bucket: manifest and other non-recording files under /audio/ always come from the assets', async () => {
  const env = withBucket({ '/audio/worlds/manifest.json': FILE }, { 'audio/worlds/manifest.json': FILE });
  const res = await worker.fetch(get('/audio/worlds/manifest.json'), env);
  assert.equal(res.status, 200);
  assert.equal(env.AUDIO.calls.length, 0);
  assert.equal(env.ASSETS.calls.length, 1);
});

test('bucket: a path with encoded characters is looked up by its decoded key', async () => {
  const env = withBucket({}, { 'audio/a b.mp3': FILE });
  const res = await worker.fetch(get('/audio/a%20b.mp3'), env);
  assert.equal(res.status, 200);
});

test('the headers added to bucket answers match the baseline of cic-website/_headers', () => {
  const text = fs.readFileSync(new URL('../cic-website/_headers', import.meta.url), 'utf8');
  const block = text.split('\n').reduce((acc, line) => {
    if (/^\/\*\s*$/.test(line)) acc.on = true;
    else if (/^\S/.test(line) && acc.on) acc.on = false;
    else if (acc.on && /^\s+[A-Za-z-]+:/.test(line)) {
      const [k, ...v] = line.trim().split(':');
      acc.map[k.trim()] = v.join(':').trim();
    }
    return acc;
  }, { on: false, map: {} }).map;
  assert.deepEqual(BASELINE_HEADERS, block);
});
