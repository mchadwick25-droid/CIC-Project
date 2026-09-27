import { test } from 'node:test';
import assert from 'node:assert/strict';
import path from 'path';
import { parseArgs, planNarration, synthesize, audioPathFor, audioDir } from './generate_tree_narration.mjs';

function movement(id, overrides = {}) {
  return { id, name: id, longDescription: `The story of ${id}.`, ...overrides };
}

test('parseArgs: defaults with no flags', () => {
  assert.deepEqual(parseArgs([]), { dryRun: false, only: null, limit: null, force: false });
});

test('parseArgs: recognizes every flag', () => {
  assert.deepEqual(parseArgs(['--dry-run', '--only', 'alx', '--limit', '5', '--force']), {
    dryRun: true,
    only: 'alx',
    limit: 5,
    force: true,
  });
});

test('parseArgs: rejects an unrecognized argument', () => {
  assert.throws(() => parseArgs(['--bogus']), /unrecognized argument/);
});

test('parseArgs: rejects a negative or non-numeric --limit', () => {
  assert.throws(() => parseArgs(['--limit', '-1']), /--limit must be a non-negative integer/);
  assert.throws(() => parseArgs(['--limit', 'nope']), /--limit must be a non-negative integer/);
});

test('audioPathFor: one file per movement id under cic-website/audio/tree', () => {
  assert.equal(audioPathFor('alx'), path.join(audioDir, 'alx.mp3'));
});

test('planNarration: skips a movement with no longDescription at all', () => {
  const movements = [movement('has-text'), movement('blank', { longDescription: '   ' }), movement('missing', { longDescription: undefined })];
  const { toGenerate, skippedNoText } = planNarration(movements, { only: null, force: false, limit: null, existsFn: () => false });
  assert.deepEqual(toGenerate.map((m) => m.id), ['has-text']);
  assert.equal(skippedNoText, 2);
});

test('planNarration: skips a movement that already has an audio file, unless --force', () => {
  const movements = [movement('narrated'), movement('not-yet')];
  const exists = (p) => p.endsWith('narrated.mp3');

  const withoutForce = planNarration(movements, { only: null, force: false, limit: null, existsFn: exists });
  assert.deepEqual(withoutForce.toGenerate.map((m) => m.id), ['not-yet']);
  assert.deepEqual(withoutForce.alreadyNarrated, ['narrated']);

  const withForce = planNarration(movements, { only: null, force: true, limit: null, existsFn: exists });
  assert.deepEqual(withForce.toGenerate.map((m) => m.id), ['narrated', 'not-yet']);
});

test('planNarration: --only narrows to a single movement by id', () => {
  const movements = [movement('a'), movement('b'), movement('c')];
  const { toGenerate } = planNarration(movements, { only: 'b', force: false, limit: null, existsFn: () => false });
  assert.deepEqual(toGenerate.map((m) => m.id), ['b']);
});

test('planNarration: --limit caps only the NEW work, not what is already narrated', () => {
  const movements = [movement('a'), movement('b'), movement('c'), movement('d')];
  const exists = (p) => p.endsWith('a.mp3');
  const { toGenerate, alreadyNarrated } = planNarration(movements, { only: null, force: false, limit: 2, existsFn: exists });
  assert.deepEqual(alreadyNarrated, ['a']);
  assert.deepEqual(toGenerate.map((m) => m.id), ['b', 'c']);
});

test('synthesize: posts the text to the right voice endpoint and returns audio bytes', async () => {
  let capturedUrl, capturedInit;
  const fakeFetch = async (url, init) => {
    capturedUrl = url;
    capturedInit = init;
    return {
      ok: true,
      arrayBuffer: async () => new TextEncoder().encode('fake-mp3-bytes').buffer,
    };
  };

  const result = await synthesize('Once, in Antioch...', { apiKey: 'test-key', voiceId: 'voice-123', fetchImpl: fakeFetch });

  assert.equal(capturedUrl, 'https://api.elevenlabs.io/v1/text-to-speech/voice-123');
  assert.equal(capturedInit.headers['xi-api-key'], 'test-key');
  assert.equal(JSON.parse(capturedInit.body).text, 'Once, in Antioch...');
  assert.ok(Buffer.isBuffer(result));
  assert.equal(result.toString(), 'fake-mp3-bytes');
});

test('synthesize: throws with the response detail when ElevenLabs rejects the request', async () => {
  const fakeFetch = async () => ({
    ok: false,
    status: 401,
    text: async () => 'invalid_api_key',
  });

  await assert.rejects(
    () => synthesize('text', { apiKey: 'bad-key', voiceId: 'v', fetchImpl: fakeFetch }),
    /ElevenLabs TTS failed \(401\): invalid_api_key/
  );
});
