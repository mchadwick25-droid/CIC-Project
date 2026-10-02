import { test } from 'node:test';
import assert from 'node:assert/strict';
import worker, { parseRange } from './worker.mjs';

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
