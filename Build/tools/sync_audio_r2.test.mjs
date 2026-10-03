import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'fs';
import os from 'os';
import path from 'path';
import { signRequest, canonicalPath, planSync, parseArgs, localRecordings, bucketClient } from './sync_audio_r2.mjs';

test('signature matches the published AWS get-vanilla vector', () => {
  const out = signRequest({
    method: 'GET', pathName: '/', headers: { host: 'example.amazonaws.com' }, payloadHash: null,
    accessKeyId: 'AKIDEXAMPLE', secretAccessKey: 'wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY',
    region: 'us-east-1', service: 'service', now: new Date('2015-08-30T12:36:00Z'),
  });
  assert.match(out.Authorization, /SignedHeaders=host;x-amz-date, Signature=5fa00fa31553b73ebf1942676e86291e8372ff2a2260956d9b8aae1d763fbf31$/);
});

test('canonicalPath encodes each segment and keeps the slashes', () => {
  assert.equal(canonicalPath('/cic-audio/audio/a b/é.mp3'), '/cic-audio/audio/a%20b/%C3%A9.mp3');
});

test('planSync sorts files into same and upload with the reason', async () => {
  const files = [
    { key: 'audio/a.mp3', file: 'a', size: 3 },
    { key: 'audio/b.mp3', file: 'b', size: 3 },
    { key: 'audio/c.mp3', file: 'c', size: 3 },
    { key: 'audio/d.mp3', file: 'd', size: 3 },
  ];
  const remote = { 'audio/a.mp3': { size: 3, md5: 'x' }, 'audio/b.mp3': { size: 4, md5: 'x' }, 'audio/d.mp3': { size: 3, md5: 'other' } };
  const { same, upload } = await planSync(files, async (k) => remote[k] ?? null, { md5: () => 'x' });
  assert.deepEqual(same.map((f) => f.key), ['audio/a.mp3']);
  assert.deepEqual(upload.map((f) => [f.key, f.why]), [
    ['audio/b.mp3', 'size 4 != 3'], ['audio/c.mp3', 'missing'], ['audio/d.mp3', 'MD5 differs'],
  ]);
});

test('planSync with force uploads everything without asking the bucket', async () => {
  let asked = 0;
  const { upload } = await planSync([{ key: 'k', file: 'f', size: 1 }], async () => { asked++; return null; }, { force: true });
  assert.equal(upload.length, 1);
  assert.equal(asked, 0);
});

test('parseArgs reads the flags and rejects the rest', () => {
  assert.deepEqual(parseArgs(['--dry-run', '--only', 'audio/worlds/']), { dryRun: true, verify: false, force: false, only: 'audio/worlds/' });
  assert.throws(() => parseArgs(['--bogus']), /unrecognized/);
  assert.throws(() => parseArgs(['--verify', '--force']), /cannot be combined/);
});

test('localRecordings lists mp3 files by their path from the site root and skips the rest', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'r2-'));
  fs.mkdirSync(path.join(root, 'audio', 'worlds', 'x'), { recursive: true });
  fs.writeFileSync(path.join(root, 'audio', 'worlds', 'x', 'story.mp3'), 'abc');
  fs.writeFileSync(path.join(root, 'audio', 'worlds', 'manifest.json'), '{}');
  const found = localRecordings(path.join(root, 'audio'), root);
  assert.deepEqual(found.map((f) => [f.key, f.size]), [['audio/worlds/x/story.mp3', 3]]);
});

test('bucketClient reads size and MD5 from HEAD, maps 404 to null, and signs without leaking the secret', async () => {
  const calls = [];
  const fetchImpl = async (url, init) => {
    calls.push({ url, init });
    if (url.endsWith('missing.mp3')) return { status: 404, ok: false, headers: new Headers() };
    return { status: 200, ok: true, headers: new Headers({ 'content-length': '7', etag: '"abc123"' }), text: async () => '' };
  };
  const c = bucketClient({ accountId: 'acct', accessKeyId: 'AK', secretAccessKey: 'SECRETVALUE', bucket: 'cic-audio', fetchImpl });
  assert.deepEqual(await c.head('audio/a.mp3'), { size: 7, md5: 'abc123' });
  assert.equal(await c.head('audio/missing.mp3'), null);
  await c.put('audio/a.mp3', Buffer.from('1234567'));
  assert.equal(calls[0].url, 'https://acct.r2.cloudflarestorage.com/cic-audio/audio/a.mp3');
  assert.equal(calls[2].init.method, 'PUT');
  assert.equal(calls[2].init.headers['content-type'], 'audio/mpeg');
  assert.ok(!JSON.stringify(calls).includes('SECRETVALUE'));
});
