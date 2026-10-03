import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseArgs, docStoryEntries, planDocStories, staleKeys, fingerprint } from './generate_docstory_narration.mjs';

const movements = [
  { id: 'a', documentedStories: [{ title: 'A0', text: 'one' }, { title: 'A1', text: '  ' }, { title: 'A2', text: 'three' }] },
  { id: 'built', documentedStories: [{ title: 'B0', text: 'skip me' }] },
  { id: 'c' },
];

test('docStoryEntries: unbuilt movements only, blank text skipped, index is the original position', () => {
  const e = docStoryEntries(movements, new Set(['built']));
  assert.deepEqual(e.map((x) => x.key), ['a-0', 'a-2']);
  assert.equal(e[1].hash, fingerprint('three'));
});

test('planDocStories: skips a story whose fingerprint matches; regenerates a changed one; --force redoes all', () => {
  const e = docStoryEntries(movements, new Set(['built']));
  const manifest = { 'a-0': { hash: fingerprint('one') }, 'a-2': { hash: 'old' } };
  let p = planDocStories(e, { manifest });
  assert.deepEqual(p.upToDate, ['a-0']);
  assert.deepEqual(p.toGenerate.map((x) => x.key), ['a-2']);
  assert.deepEqual(planDocStories(e, { manifest, force: true }).toGenerate.map((x) => x.key), ['a-0', 'a-2']);
  assert.deepEqual(staleKeys(e, manifest), ['a-2']);
});

test('planDocStories: --only and --limit narrow the plan; an entry missing from the manifest is generated', () => {
  const e = docStoryEntries(movements, new Set(['built']));
  const manifest = { 'a-0': { hash: fingerprint('one') } };
  assert.deepEqual(planDocStories(e, { only: ['a-2'], manifest }).toGenerate.map((x) => x.key), ['a-2']);
  assert.deepEqual(planDocStories(e, { limit: 1, manifest: {} }).toGenerate.map((x) => x.key), ['a-0']);
});

test('parseArgs: reads the paid settings from flags only; rejects unknown flags', () => {
  const o = parseArgs(['--voice-id', 'v', '--model', 'm', '--output-format', 'mp3_44100_64', '--only', 'x-0,y-1', '--limit', '3']);
  assert.deepEqual([o.voiceId, o.model, o.outputFormat, o.only, o.limit], ['v', 'm', 'mp3_44100_64', ['x-0', 'y-1'], 3]);
  assert.throws(() => parseArgs(['--bogus']), /unrecognized/);
  assert.throws(() => parseArgs(['--limit', '-2']), /non-negative/);
});
