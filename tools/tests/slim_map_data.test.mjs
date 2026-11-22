import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { buildSpec, split, merge, findDataLiteral, slimMap, rebuild, loadConfig } from '../slim_map_data.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const AUDIT = path.join(ROOT, 'Build/Ministry/Operations/Audits/2026-11-22_cft-phone-loading-audit/startup_fields.json');

test('split and merge give back the original, through arrays of objects and nested objects', () => {
  const spec = buildSpec(['id', 'tags', 'stories[].title', 'card.role']);
  const value = {
    id: 'a', tags: ['x', 'y'], big: 'text',
    stories: [{ title: 't1', text: 'long one' }, { title: 't2', text: 'long two', extra: { deep: 1 } }],
    card: { role: 'bishop', quote: 'q', list: [1, 2] },
  };
  const [slim, rest] = split(value, spec);
  assert.deepEqual(slim, { id: 'a', tags: ['x', 'y'], stories: [{ title: 't1' }, { title: 't2' }], card: { role: 'bishop' } });
  assert.ok(!('big' in slim) && 'big' in rest);
  assert.deepEqual(merge(slim, rest), value);
});

test('an array whose parts are all kept leaves nothing behind, and empty and missing values survive', () => {
  const spec = buildSpec(['id', 'places[].name', 'gone']);
  const value = { id: 'b', places: [{ name: 'Rome' }, { name: 'Tyre' }], notes: [], other: null };
  const [slim, rest] = split(value, spec);
  assert.deepEqual(slim, { id: 'b', places: [{ name: 'Rome' }, { name: 'Tyre' }] });
  assert.deepEqual(rest, { notes: [], other: null });
  assert.deepEqual(merge(slim, rest), value);
  assert.deepEqual(merge({ id: 'c' }, undefined), { id: 'c' });
});

test('a path cannot be both a leaf and a parent', () => {
  assert.throws(() => buildSpec(['card', 'card.role']), /sits under a path kept whole/);
  assert.throws(() => buildSpec(['card.role', 'card']), /both a leaf and a parent/);
});

test('findDataLiteral reads past braces and quotes inside strings', () => {
  const html = 'x<script>\nconst DATA = {"a":"}{\\"]","b":[1,{"c":2}]};\nconst Y=1;</script>';
  const { start, end } = findDataLiteral(html);
  assert.deepEqual(JSON.parse(html.slice(start, end)), { a: '}{"]', b: [1, { c: 2 }] });
});

const html = fs.readFileSync(path.join(ROOT, 'cft-website', 'index.html'), 'utf8');
const config = loadConfig();
const result = slimMap(html, config);

test('the real page: the three parts rebuild the original data exactly', () => {
  assert.deepEqual(rebuild(result.slimData, result.entries, result.edgesDetail, config), result.data);
});

test('the real page: long descriptions leave the page and a hash of each stays', () => {
  const slimById = new Map(result.slimData.movements.map((m) => [m.id, m]));
  let withText = 0;
  for (const m of result.data.movements) {
    const s = slimById.get(m.id);
    assert.ok(!('longDescription' in s), `${m.id} still carries its long description`);
    if (typeof m.longDescription === 'string') {
      withText++;
      assert.equal(s.descHash, crypto.createHash('sha256').update(m.longDescription, 'utf8').digest('hex'), m.id);
    } else assert.ok(!('descHash' in s), m.id);
  }
  assert.ok(withText > 500);
});

test('the real page: every path the audit found at start-up is kept in the slim copy', () => {
  const audit = JSON.parse(fs.readFileSync(AUDIT, 'utf8')).startup_leaves;
  const keep = new Set(config.movements.keep.concat(config.edges.keep.map((p) => `@${p}`)));
  const missing = [];
  for (const p of audit) {
    const m = /^DATA\.(movements|edges)\[\]\.(.+)$/.exec(p);
    if (!m) continue;
    const rel = m[2].replace(/\[\]/g, '[]');
    if (m[1] === 'movements' && rel === 'longDescription') continue;
    const set = m[1] === 'movements' ? config.movements.keep : config.edges.keep;
    const covered = set.some((k) => rel === k || rel.startsWith(`${k}.`) || rel.startsWith(`${k}[]`));
    if (!covered) missing.push(p);
  }
  assert.deepEqual(missing, [], 'the audit found these read at start-up, but tools/slim_map_fields.json does not keep them');
  assert.ok(keep.size > 0);
});

test('the real page: every kept field exists on at least one entry, so the field list has no typos', () => {
  const present = (list, spec) => {
    const found = new Set();
    const walk = (v, prefix) => {
      if (Array.isArray(v)) v.forEach((x) => walk(x, `${prefix}[]`));
      else if (v && typeof v === 'object') for (const [k, x] of Object.entries(v)) { const p = prefix ? `${prefix}.${k}` : k; found.add(p); walk(x, p); }
    };
    list.forEach((x) => walk(x, ''));
    return spec.filter((k) => !found.has(k.replace(/\[\]/g, '[]')) && ![...found].some((f) => f.replace(/\[\]/g, '') === k.replace(/\[\]/g, '')));
  };
  assert.deepEqual(present(result.data.movements, config.movements.keep), []);
  assert.deepEqual(present(result.data.edges, config.edges.keep), []);
});

test('the real page: size budget for the page a phone downloads', () => {
  const pageMb = Buffer.byteLength(result.html) / 1e6;
  assert.ok(pageMb < 1.6, `the slim page is ${pageMb.toFixed(2)} MB; the budget is 1.6 MB`);
  const biggest = Math.max(...Object.values(result.entries).map((e) => Buffer.byteLength(JSON.stringify(e))));
  assert.ok(biggest < 64 * 1024, `the largest card file is ${biggest} bytes; the budget is 64 KB`);
  const detailMb = Buffer.byteLength(JSON.stringify(result.edgesDetail)) / 1e6;
  assert.ok(detailMb < 1.6, `the link details are ${detailMb.toFixed(2)} MB; the budget is 1.6 MB`);
  assert.equal(Object.keys(result.entries).length, result.data.movements.length);
});

test('the real page: the slim copy turns the slim switch on and the committed page leaves it off', () => {
  assert.equal(html.split('const SLIM_MAP = false;').length, 2);
  assert.ok(!result.html.includes('const SLIM_MAP = false;'));
  assert.equal(result.html.split('const SLIM_MAP = true;').length, 2);
  assert.throws(() => slimMap(html.replace('const SLIM_MAP = false;', ''), config), /SLIM_MAP/);
});
