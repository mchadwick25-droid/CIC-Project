#!/usr/bin/env node
/**
 * Upload the site's recordings (cic-website/audio/**.mp3) to the R2 bucket the
 * audio Worker reads, and check that every one arrived intact.
 *
 * The object key is the file's path from cic-website/, so
 * cic-website/audio/worlds/donatism/story.mp3 is stored as
 * audio/worlds/donatism/story.mp3 and served at /audio/worlds/donatism/story.mp3.
 * The manifest files stay in git and are not uploaded.
 *
 * Usage (credentials come from the environment, never from the command line):
 *   R2_ACCOUNT_ID=... R2_ACCESS_KEY_ID=... R2_SECRET_ACCESS_KEY=... \
 *     node Build/tools/sync_audio_r2.mjs [--dry-run] [--verify] [--force] [--only audio/worlds/]
 *
 * R2_BUCKET names the bucket (default cic-audio).
 *
 * Default run: upload every file that is missing from the bucket or whose size
 * or MD5 differs. --force uploads every file. --verify uploads nothing and
 * exits 1 unless every local file is in the bucket with the same size and MD5.
 * --dry-run prints the plan without touching the network. A single-part upload's
 * ETag is the file's MD5, which is what the check compares.
 *
 * Talks to R2's S3-compatible API, signed with AWS Signature Version 4, using
 * nothing but Node.
 */
import crypto from 'crypto';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const siteDir = path.resolve(__dirname, '..', '..', 'cic-website');
const audioDir = path.join(siteDir, 'audio');

const sha256 = (data) => crypto.createHash('sha256').update(data).digest('hex');
const hmac = (key, data) => crypto.createHmac('sha256', key).update(data).digest();

/** RFC 3986 encoding of one path segment, as S3 signing requires. */
function encodeSegment(s) {
  return encodeURIComponent(s).replace(/[!'()*]/g, (c) => '%' + c.charCodeAt(0).toString(16).toUpperCase());
}

export function canonicalPath(p) {
  return p.split('/').map(encodeSegment).join('/') || '/';
}

/**
 * The headers of a signed request (AWS Signature Version 4). `headers` must
 * already hold `host`; x-amz-date is added here. Returns the full header set.
 */
export function signRequest({ method, pathName, query = '', headers, payloadHash, accessKeyId, secretAccessKey, region, service, now = new Date() }) {
  const amzDate = now.toISOString().replace(/[:-]|\.\d{3}/g, '');
  const day = amzDate.slice(0, 8);
  const all = { ...headers, 'x-amz-date': amzDate };
  if (payloadHash !== null && payloadHash !== undefined) all['x-amz-content-sha256'] = payloadHash;
  const names = Object.keys(all).map((n) => n.toLowerCase()).sort();
  const lower = Object.fromEntries(Object.entries(all).map(([k, v]) => [k.toLowerCase(), String(v).trim().replace(/\s+/g, ' ')]));
  const canonicalHeaders = names.map((n) => `${n}:${lower[n]}\n`).join('');
  const signedHeaders = names.join(';');
  const canonical = [method, canonicalPath(pathName), query, canonicalHeaders, signedHeaders, payloadHash ?? sha256('')].join('\n');
  const scope = `${day}/${region}/${service}/aws4_request`;
  const toSign = ['AWS4-HMAC-SHA256', amzDate, scope, sha256(canonical)].join('\n');
  const kDate = hmac('AWS4' + secretAccessKey, day);
  const key = hmac(hmac(hmac(kDate, region), service), 'aws4_request');
  const signature = crypto.createHmac('sha256', key).update(toSign).digest('hex');
  all.Authorization = `AWS4-HMAC-SHA256 Credential=${accessKeyId}/${scope}, SignedHeaders=${signedHeaders}, Signature=${signature}`;
  return all;
}

export function bucketClient({ accountId, accessKeyId, secretAccessKey, bucket, fetchImpl = fetch }) {
  const host = `${accountId}.r2.cloudflarestorage.com`;
  const call = async (method, key, body, extra = {}) => {
    const pathName = `/${bucket}/${key}`;
    const payloadHash = body ? sha256(body) : sha256('');
    const headers = signRequest({
      method, pathName, headers: { host, ...extra }, payloadHash, accessKeyId, secretAccessKey, region: 'auto', service: 's3',
    });
    delete headers.host;
    return fetchImpl(`https://${host}${canonicalPath(pathName)}`, { method, headers, body });
  };
  return {
    /** {size, md5} of the stored object, or null when it is not there. */
    async head(key) {
      const res = await call('HEAD', key);
      if (res.status === 404) return null;
      if (!res.ok) throw new Error(`HEAD ${key}: ${res.status}`);
      return { size: Number(res.headers.get('content-length')), md5: (res.headers.get('etag') || '').replace(/"/g, '') };
    },
    async put(key, body) {
      const res = await call('PUT', key, body, { 'content-type': 'audio/mpeg' });
      if (!res.ok) throw new Error(`PUT ${key}: ${res.status} ${(await res.text()).slice(0, 200)}`);
    },
  };
}

/** Every recording under cic-website/audio, as {key, file, size}. */
export function localRecordings(root = audioDir, base = siteDir) {
  const out = [];
  const walk = (dir) => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(full);
      else if (entry.name.endsWith('.mp3')) out.push({ key: path.relative(base, full).split(path.sep).join('/'), file: full, size: fs.statSync(full).size });
    }
  };
  if (fs.existsSync(root)) walk(root);
  return out.sort((a, b) => a.key.localeCompare(b.key));
}

const md5File = (file) => crypto.createHash('md5').update(fs.readFileSync(file)).digest('hex');

/**
 * Decide, for every local file, whether the bucket already holds it.
 * `head` is the bucket's own head(key). Returns {same, upload: [{..., why}]}.
 */
export async function planSync(files, head, { force = false, md5 = md5File, concurrency = 6 } = {}) {
  const same = [];
  const upload = [];
  let next = 0;
  const worker = async () => {
    while (next < files.length) {
      const f = files[next++];
      if (force) { upload.push({ ...f, why: 'forced' }); continue; }
      const remote = await head(f.key);
      if (!remote) upload.push({ ...f, why: 'missing' });
      else if (remote.size !== f.size) upload.push({ ...f, why: `size ${remote.size} != ${f.size}` });
      else if (remote.md5 !== md5(f.file)) upload.push({ ...f, why: 'MD5 differs' });
      else same.push(f);
    }
  };
  await Promise.all(Array.from({ length: concurrency }, worker));
  upload.sort((a, b) => a.key.localeCompare(b.key));
  return { same, upload };
}

export function parseArgs(argv) {
  const opts = { dryRun: false, verify: false, force: false, only: null };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--dry-run') opts.dryRun = true;
    else if (arg === '--verify') opts.verify = true;
    else if (arg === '--force') opts.force = true;
    else if (arg === '--only') opts.only = argv[++i];
    else throw new Error(`unrecognized argument: ${arg}`);
  }
  if (opts.verify && opts.force) throw new Error('--verify uploads nothing; it cannot be combined with --force');
  return opts;
}

const mb = (n) => (n / 1048576).toFixed(1);

async function run() {
  const opts = parseArgs(process.argv.slice(2));
  let files = localRecordings();
  if (opts.only) files = files.filter((f) => f.key.startsWith(opts.only));
  const total = files.reduce((n, f) => n + f.size, 0);
  console.log(`${files.length} recordings, ${mb(total)} MB${opts.only ? ` under ${opts.only}` : ''}`);
  if (opts.dryRun) { console.log('Dry run: nothing is contacted.'); return; }

  const need = ['R2_ACCOUNT_ID', 'R2_ACCESS_KEY_ID', 'R2_SECRET_ACCESS_KEY'].filter((n) => !process.env[n]);
  if (need.length) throw new Error(`Set ${need.join(', ')} in the environment.`);
  const bucket = process.env.R2_BUCKET || 'cic-audio';
  const client = bucketClient({ accountId: process.env.R2_ACCOUNT_ID, accessKeyId: process.env.R2_ACCESS_KEY_ID, secretAccessKey: process.env.R2_SECRET_ACCESS_KEY, bucket });
  console.log(`bucket: ${bucket}`);

  const { same, upload } = await planSync(files, (k) => client.head(k), { force: opts.force });
  console.log(`already in the bucket and identical: ${same.length}; to upload: ${upload.length}`);
  if (opts.verify) {
    upload.slice(0, 20).forEach((f) => console.log(`  NOT OK ${f.key}: ${f.why}`));
    if (upload.length) { process.exitCode = 1; console.log(`verify FAILED: ${upload.length} of ${files.length} not matching`); }
    else console.log(`verify OK: all ${files.length} recordings are in the bucket with the same size and MD5`);
    return;
  }
  let done = 0;
  for (const f of upload) {
    await client.put(f.key, fs.readFileSync(f.file));
    done++;
    if (done % 25 === 0 || done === upload.length) console.log(`  uploaded ${done}/${upload.length}`);
  }
  const after = await planSync(files, (k) => client.head(k));
  if (after.upload.length) { process.exitCode = 1; console.log(`FAILED: ${after.upload.length} files still do not match after upload`); }
  else console.log(`done: all ${files.length} recordings are in the bucket with the same size and MD5`);
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  run().catch((err) => { console.error(err.message); process.exit(1); });
}
