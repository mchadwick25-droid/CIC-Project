#!/usr/bin/env node
// Checks the live Church Family Tree addresses after a deploy: every movement
// page answers on the tree's domain, every old address on Church in
// Conversation redirects there permanently in one hop (renamed movements to
// their new page), and the census is the same file at both addresses.
// Usage: node tools/check_tree_domains.mjs [--sample N]

import { readFileSync } from 'node:fs';
import crypto from 'node:crypto';

const TREE = 'https://www.churchfamilytree.com';
const OLD = 'https://churchinconversation.com';
const args = process.argv.slice(2);
const sampleAt = args.indexOf('--sample');
const sample = sampleAt >= 0 ? Number(args[sampleAt + 1]) : Infinity;
const census = JSON.parse(readFileSync('cic-website/data/world-census.json', 'utf8'));
const problems = [];

async function head(url) {
  const res = await fetch(url, { redirect: 'manual' });
  await res.arrayBuffer();
  return res;
}

const ids = census.movements.map(m => m.id).slice(0, sample);
for (const id of ids) {
  const page = await head(`${TREE}/tree/${id}`);
  if (page.status !== 200) problems.push(`${TREE}/tree/${id}: ${page.status}`);
  for (const old of [`${OLD}/tree/${id}`, `${OLD}/tree/${id}.html`]) {
    const res = await head(old);
    const want = `${TREE}/tree/${id}`;
    if (res.status !== 301 || res.headers.get('location') !== want) problems.push(`${old}: ${res.status} -> ${res.headers.get('location')} (want 301 -> ${want})`);
  }
}
for (const r of census.retiredMovements ?? []) {
  if (!r.redirectTo) continue;
  const res = await head(`${OLD}/tree/${r.id}`);
  const want = `${TREE}/tree/${r.redirectTo}`;
  if (res.status !== 301 || res.headers.get('location') !== want) problems.push(`${OLD}/tree/${r.id}: ${res.status} -> ${res.headers.get('location')} (want 301 -> ${want})`);
}
for (const path of ['/atlas-v3.html', '/atlas.html', '/world-atlas.html']) {
  const res = await head(OLD + path);
  if (res.status !== 301 || res.headers.get('location') !== `${TREE}/`) problems.push(`${OLD}${path}: ${res.status} -> ${res.headers.get('location')}`);
}
const digest = async url => {
  const res = await fetch(url, { redirect: 'manual' });
  const body = Buffer.from(await res.arrayBuffer());
  return { status: res.status, hash: crypto.createHash('sha256').update(body).digest('hex'), type: res.headers.get('content-type') };
};
const [a, b] = await Promise.all([digest(`${OLD}/data/world-census.json`), digest(`${TREE}/data/world-census.json`)]);
if (a.status !== 200 || b.status !== 200) problems.push(`census status: old ${a.status}, tree ${b.status}`);
if (a.hash !== b.hash) problems.push(`census differs: old ${a.hash.slice(0, 16)}, tree ${b.hash.slice(0, 16)}`);
if (a.type !== b.type) problems.push(`census content type differs: old ${a.type}, tree ${b.type}`);

console.log(`${ids.length} movements checked on both domains; census ${a.hash === b.hash ? 'identical' : 'DIFFERENT'}; ${problems.length} problems`);
problems.forEach(p => console.log(`- ${p}`));
process.exit(problems.length ? 1 : 0);
