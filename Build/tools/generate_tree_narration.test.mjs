import { test } from 'node:test';
import assert from 'node:assert/strict';
import path from 'path';
import { parseArgs, requirePaidSettings, planNarration, synthesize, synthesizeWithCost, audioPathFor, audioDir, resolveVoiceId, narrationTextFor, defaultVoiceSettings } from './generate_tree_narration.mjs';

function movement(id, overrides = {}) {
  return { id, name: id, longDescription: `The story of ${id}.`, ...overrides };
}

test('parseArgs: defaults with no flags', () => {
  assert.deepEqual(parseArgs([]), { dryRun: false, only: null, limit: null, charBudget: null, force: false, voiceId: null, model: null });
});

test('parseArgs: recognizes every flag', () => {
  assert.deepEqual(parseArgs(['--dry-run', '--only', 'alx', '--limit', '5', '--char-budget', '20000', '--force', '--voice-id', 'v1', '--model', 'm1']), {
    dryRun: true,
    only: 'alx',
    limit: 5,
    charBudget: 20000,
    force: true,
    voiceId: 'v1',
    model: 'm1',
  });
});

test('parseArgs: rejects an unrecognized argument', () => {
  assert.throws(() => parseArgs(['--bogus']), /unrecognized argument/);
});

test('parseArgs: rejects a negative or non-numeric --limit', () => {
  assert.throws(() => parseArgs(['--limit', '-1']), /--limit must be a non-negative integer/);
  assert.throws(() => parseArgs(['--limit', 'nope']), /--limit must be a non-negative integer/);
});

test('parseArgs: rejects a negative or non-numeric --char-budget', () => {
  assert.throws(() => parseArgs(['--char-budget', '-1']), /--char-budget must be a non-negative integer/);
  assert.throws(() => parseArgs(['--char-budget', 'nope']), /--char-budget must be a non-negative integer/);
});

test('audioPathFor: one file per movement id under cic-website/audio/tree', () => {
  assert.equal(audioPathFor('alx'), path.join(audioDir, 'alx.mp3'));
});

test('planNarration: skips a movement with no longDescription at all', () => {
  const movements = [movement('has-text'), movement('blank', { longDescription: '   ' }), movement('missing', { longDescription: undefined })];
  const { toGenerate, skippedNoText } = planNarration(movements, { only: null, force: false, limit: null });
  assert.deepEqual(toGenerate.map((m) => m.id), ['has-text']);
  assert.equal(skippedNoText, 2);
});

test('planNarration: skips a movement that is already in the manifest, unless --force', () => {
  const movements = [movement('narrated'), movement('not-yet')];
  const manifest = { narrated: {} };

  const withoutForce = planNarration(movements, { only: null, force: false, limit: null, manifest });
  assert.deepEqual(withoutForce.toGenerate.map((m) => m.id), ['not-yet']);
  assert.deepEqual(withoutForce.alreadyNarrated, ['narrated']);

  const withForce = planNarration(movements, { only: null, force: true, limit: null, manifest });
  assert.deepEqual(withForce.toGenerate.map((m) => m.id), ['narrated', 'not-yet']);
});

test('planNarration: --only narrows to a single movement by id', () => {
  const movements = [movement('a'), movement('b'), movement('c')];
  const { toGenerate } = planNarration(movements, { only: 'b', force: false, limit: null });
  assert.deepEqual(toGenerate.map((m) => m.id), ['b']);
});

test('planNarration: --char-budget stops before the running total would exceed it, in order', () => {
  const movements = [
    movement('a', { longDescription: 'x'.repeat(1000) }),
    movement('b', { longDescription: 'x'.repeat(1000) }),
    movement('c', { longDescription: 'x'.repeat(1000) }),
  ];
  const { toGenerate, skippedBudget } = planNarration(movements, {
    only: null,
    force: false,
    limit: null,
    charBudget: 2500,
  });
  assert.deepEqual(toGenerate.map((m) => m.id), ['a', 'b']);
  assert.equal(skippedBudget, 1);
});

test('planNarration: --char-budget does not skip ahead to a smaller movement that would fit', () => {
  const movements = [
    movement('big', { longDescription: 'x'.repeat(2000) }),
    movement('small', { longDescription: 'x'.repeat(100) }),
  ];
  const { toGenerate, skippedBudget } = planNarration(movements, {
    only: null,
    force: false,
    limit: null,
    charBudget: 1000,
  });
  assert.deepEqual(toGenerate, []);
  assert.equal(skippedBudget, 2);
});

test('planNarration: --char-budget combines with already-narrated and --limit filtering', () => {
  const movements = [
    movement('narrated', { longDescription: 'x'.repeat(1000) }),
    movement('a', { longDescription: 'x'.repeat(1000) }),
    movement('b', { longDescription: 'x'.repeat(1000) }),
  ];
  const manifest = { narrated: {} };
  const { toGenerate, alreadyNarrated, skippedBudget } = planNarration(movements, {
    only: null,
    force: false,
    limit: null,
    charBudget: 1000,
    manifest,
  });
  assert.deepEqual(alreadyNarrated, ['narrated']);
  assert.deepEqual(toGenerate.map((m) => m.id), ['a']);
  assert.equal(skippedBudget, 1);
});

test('planNarration: --limit caps only the NEW work, not what is already narrated', () => {
  const movements = [movement('a'), movement('b'), movement('c'), movement('d')];
  const manifest = { a: {} };
  const { toGenerate, alreadyNarrated } = planNarration(movements, { only: null, force: false, limit: 2, manifest });
  assert.deepEqual(alreadyNarrated, ['a']);
  assert.deepEqual(toGenerate.map((m) => m.id), ['b', 'c']);
});

test('narrationTextFor: falls back to longDescription when no worlds-data file exists', () => {
  const m = movement('unbuilt-movement');
  const text = narrationTextFor(m, { existsFn: () => false });
  assert.equal(text, m.longDescription);
});

test('narrationTextFor: uses a built world\'s orientation.story, joined, when the data file exists', () => {
  const m = movement('built-movement', { longDescription: 'The stale census summary.' });
  const fakeData = { orientation: { story: [{ text: 'Paragraph one.' }, { text: 'Paragraph two.' }] } };
  const text = narrationTextFor(m, {
    existsFn: () => true,
    readFn: () => JSON.stringify(fakeData),
  });
  assert.equal(text, 'Paragraph one.\n\nParagraph two.');
});

test('narrationTextFor: falls back to longDescription when the data file has no orientation.story', () => {
  const m = movement('data-without-story');
  const text = narrationTextFor(m, {
    existsFn: () => true,
    readFn: () => JSON.stringify({ orientation: { glossary: [] } }),
  });
  assert.equal(text, m.longDescription);
});

test('narrationTextFor: falls back to longDescription when orientation.story is an empty array', () => {
  const m = movement('data-with-empty-story');
  const text = narrationTextFor(m, {
    existsFn: () => true,
    readFn: () => JSON.stringify({ orientation: { story: [] } }),
  });
  assert.equal(text, m.longDescription);
});

test('planNarration: --char-budget uses the resolved narration text length, not always longDescription', () => {
  const movements = [movement('built-a', { longDescription: 'short' })];
  const textForFn = () => 'x'.repeat(500);
  const { toGenerate, skippedBudget } = planNarration(movements, {
    only: null,
    force: false,
    limit: null,
    charBudget: 400,
    textForFn,
  });
  assert.deepEqual(toGenerate, []);
  assert.equal(skippedBudget, 1);
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

  const result = await synthesize('Once, in Antioch...', { apiKey: 'test-key', voiceId: 'voice-123', modelId: 'model-x', fetchImpl: fakeFetch });

  assert.equal(capturedUrl, 'https://api.elevenlabs.io/v1/text-to-speech/voice-123');
  assert.equal(capturedInit.headers['xi-api-key'], 'test-key');
  assert.equal(JSON.parse(capturedInit.body).text, 'Once, in Antioch...');
  assert.deepEqual(JSON.parse(capturedInit.body).voice_settings, defaultVoiceSettings);
  assert.equal(JSON.parse(capturedInit.body).model_id, 'model-x');
  assert.ok(Buffer.isBuffer(result));
  assert.equal(result.toString(), 'fake-mp3-bytes');
});

test('synthesize: an explicit voiceSettings overrides the default', async () => {
  let capturedInit;
  const fakeFetch = async (url, init) => {
    capturedInit = init;
    return { ok: true, arrayBuffer: async () => new ArrayBuffer(0) };
  };
  const custom = { stability: 0.1, similarity_boost: 0.5, style: 0.5, use_speaker_boost: false };

  await synthesize('text', { apiKey: 'k', voiceId: 'v', modelId: 'm', voiceSettings: custom, fetchImpl: fakeFetch });

  assert.deepEqual(JSON.parse(capturedInit.body).voice_settings, custom);
});

test('resolveVoiceId: falls back to the default narrator when a movement has no override', () => {
  const voiceMap = { 'has-override': 'voice-abc', 'blank-override': '' };
  assert.equal(resolveVoiceId('no-such-id', { voiceMap, defaultVoiceId: 'default-voice' }), 'default-voice');
  assert.equal(resolveVoiceId('blank-override', { voiceMap, defaultVoiceId: 'default-voice' }), 'default-voice');
});

test('resolveVoiceId: uses a movement\'s own override voice when one is set', () => {
  const voiceMap = { 'has-override': 'voice-abc' };
  assert.equal(resolveVoiceId('has-override', { voiceMap, defaultVoiceId: 'default-voice' }), 'voice-abc');
});

test('resolveVoiceId: trims whitespace-only overrides down to the fallback', () => {
  const voiceMap = { spacey: '   ' };
  assert.equal(resolveVoiceId('spacey', { voiceMap, defaultVoiceId: 'default-voice' }), 'default-voice');
});

test('synthesize: throws with the response detail when ElevenLabs rejects the request', async () => {
  const fakeFetch = async () => ({
    ok: false,
    status: 401,
    text: async () => 'invalid_api_key',
  });

  await assert.rejects(
    () => synthesize('text', { apiKey: 'bad-key', voiceId: 'v', modelId: 'm', fetchImpl: fakeFetch }),
    /ElevenLabs TTS failed \(401\): invalid_api_key/
  );
});

test('synthesize: refuses to run without a modelId', async () => {
  await assert.rejects(() => synthesize('t', { apiKey: 'k', voiceId: 'v', fetchImpl: async () => ({ ok: true }) }), /modelId is required/);
});

test('synthesizeWithCost: sends output_format and returns the character-cost header', async () => {
  let capturedUrl;
  const fakeFetch = async (url) => {
    capturedUrl = url;
    return { ok: true, headers: { get: (h) => (h === 'character-cost' ? '134' : null) }, arrayBuffer: async () => new ArrayBuffer(2) };
  };
  const { audio, cost } = await synthesizeWithCost('t', { apiKey: 'k', voiceId: 'v', modelId: 'm', outputFormat: 'mp3_44100_64', fetchImpl: fakeFetch });
  assert.equal(capturedUrl, 'https://api.elevenlabs.io/v1/text-to-speech/v?output_format=mp3_44100_64');
  assert.equal(cost, 134);
  assert.equal(audio.length, 2);
});

test('requirePaidSettings: refuses a missing voice or model, never reads the environment', () => {
  const saved = process.env.ELEVENLABS_VOICE_ID;
  process.env.ELEVENLABS_VOICE_ID = 'from-env';
  try {
    assert.throws(() => requirePaidSettings({ voiceId: null, model: 'm' }), /--voice-id is required/);
    assert.throws(() => requirePaidSettings({ voiceId: 'v', model: null }), /--model is required/);
    assert.throws(() => requirePaidSettings({ voiceId: '--model', model: 'm' }), /--voice-id is required/);
    requirePaidSettings({ voiceId: 'v', model: 'm' });
  } finally {
    if (saved === undefined) delete process.env.ELEVENLABS_VOICE_ID; else process.env.ELEVENLABS_VOICE_ID = saved;
  }
});
