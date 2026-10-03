#!/usr/bin/env node
/**
 * Generate one-time ElevenLabs narration audio for each movement's own
 * story - Church Family Tree's narration step. Third-person historical
 * narration (never a Representative speaking in character - that's a
 * separate, already-built feature). One consistent narrator voice for most
 * movements, with distinct per-movement overrides for the ones that already
 * have a live built Representative - see tree-narration-voices.mjs. Atlas
 * narration only; live-conversation voice is untouched by this script.
 *
 * Text source, per movement (see `narrationTextFor`): a built world with a
 * compiled cic-website/data/worlds/<id>.json carrying `orientation.story`
 * (paragraph array, each grounded in a real record) uses that - the same
 * text the real Church Family Tree (atlas-v3.html) shows for built worlds,
 * and the more rigorous, more current text once a world's full build
 * lands. Every other movement uses world-census.json's own
 * `longDescription` - the only prose that exists for it, and what
 * atlas-v3.html itself shows for every non-built movement.
 *
 * Output: cic-website/audio/tree/<id>.mp3, one per movement that has a
 * longDescription. Idempotent - a movement already carrying an audio file
 * is skipped unless --force, so a partial run (rate limit, a crashed
 * process, a paced multi-day batch) can always resume from where it left
 * off without re-spending on movements already narrated.
 *
 * Voice delivery: every call sends `defaultVoiceSettings` (see below) unless
 * a caller overrides it. Mark's own A/B listen-through (2026-09-29) found
 * the untuned voice default read as over-dramatic/preachy; these settings
 * are the converged fix - a --force re-run is how any already-narrated
 * movement picks them up.
 *
 * Usage:
 *   ELEVENLABS_API_KEY=... node Build/tools/generate_tree_narration.mjs --voice-id <id> --model <model_id> [options]
 *
 * --voice-id is the default narrator used for every movement that has no
 * override in tree-narration-voices.mjs. --voice-id and --model are required
 * and are never read from the environment; a run prints the voice, model and
 * settings it actually sends, and one line per request with the credits
 * ElevenLabs charged.
 *
 * Options:
 *   --voice-id <id>    Required (except --dry-run). Default narrator voice.
 *   --model <id>       Required (except --dry-run). ElevenLabs model id.
 *   --dry-run          Report what would be generated; no API calls, no files written.
 *   --only <id>        Generate (or dry-run) a single movement by its census id.
 *   --limit <n>        Cap the number of NEW clips generated this run (already-narrated
 *                      movements don't count against it). Omit to run the whole batch.
 *   --char-budget <n>  Stop adding movements to this run once their combined
 *                      longDescription length would exceed n characters - for
 *                      splitting a batch across a metered quota (e.g. an
 *                      ElevenLabs plan with n characters left before renewal)
 *                      without guessing a movement count. Never starts a
 *                      movement that would push the running total over budget;
 *                      applied after --limit, so the tighter of the two binds.
 *   --force            Regenerate even for a movement that already has an audio file.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { voiceOverrides } from './tree-narration-voices.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
const censusPath = path.join(rootDir, 'cic-website/data/world-census.json');
export const audioDir = path.join(rootDir, 'cic-website/audio/tree');
export const worldsDataDir = path.join(rootDir, 'cic-website/data/worlds');

const ELEVENLABS_TTS_URL = (voiceId) => `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;

/**
 * The narration delivery Mark converged on after an A/B round against the
 * untuned voice default (2026-09-29): higher stability and similarity_boost
 * pulled down slightly to soften the character, aiming for a reflective,
 * considered read rather than the performed, over-dramatic default.
 */
/**
 * Narration is requested and stored as 64 kbps mono: speech needs no more, and
 * the audio folder is the bulk of the site's size.
 */
export const NARRATION_OUTPUT_FORMAT = 'mp3_44100_64';
export const NARRATION_BITRATE = '64k';

export const defaultVoiceSettings = { stability: 0.95, similarity_boost: 0.68, style: 0.0, use_speaker_boost: true };

export function parseArgs(argv) {
  const opts = { dryRun: false, only: null, limit: null, charBudget: null, force: false, voiceId: null, model: null };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--dry-run') opts.dryRun = true;
    else if (arg === '--force') opts.force = true;
    else if (arg === '--only') opts.only = argv[++i];
    else if (arg === '--voice-id') opts.voiceId = argv[++i];
    else if (arg === '--model') opts.model = argv[++i];
    else if (arg === '--limit') opts.limit = Number(argv[++i]);
    else if (arg === '--char-budget') opts.charBudget = Number(argv[++i]);
    else throw new Error(`unrecognized argument: ${arg}`);
  }
  if (opts.limit !== null && (!Number.isInteger(opts.limit) || opts.limit < 0)) {
    throw new Error(`--limit must be a non-negative integer, got ${opts.limit}`);
  }
  if (opts.charBudget !== null && (!Number.isInteger(opts.charBudget) || opts.charBudget < 0)) {
    throw new Error(`--char-budget must be a non-negative integer, got ${opts.charBudget}`);
  }
  return opts;
}

/**
 * Paid settings are never inherited from the environment: a run that does
 * not name its voice and model on the command refuses to start.
 */
export function requirePaidSettings({ voiceId, model }) {
  for (const [flag, value] of [['--voice-id', voiceId], ['--model', model]]) {
    if (!value || value.startsWith('--')) {
      throw new Error(`${flag} is required and is never read from the environment.`);
    }
  }
}

export function audioPathFor(movementId) {
  return path.join(audioDir, `${movementId}.mp3`);
}

/**
 * The text to narrate for a movement: a built world's own compiled
 * `orientation.story` (paragraph array, each grounded in a real record)
 * when one exists, else the census `longDescription`. `existsFn`/`readFn`
 * are injected so tests never touch the real, still-growing worlds-data
 * directory.
 */
export function narrationTextFor(movement, { dataDir = worldsDataDir, existsFn = fs.existsSync, readFn = fs.readFileSync } = {}) {
  const dataPath = path.join(dataDir, `${movement.id}.json`);
  if (existsFn(dataPath)) {
    const data = JSON.parse(readFn(dataPath, 'utf-8'));
    const story = data?.orientation?.story;
    if (Array.isArray(story) && story.length > 0) {
      return story.map((p) => p.text).join('\n\n');
    }
  }
  return movement.longDescription;
}

/**
 * Movements that need a narration clip generated this run, in stable
 * (declared) order - never a claim about which ones already have one,
 * only which ones this run should act on given the options passed.
 */
export function planNarration(movements, { only, force, limit, charBudget = null, existsFn = fs.existsSync, textForFn = narrationTextFor }) {
  let candidates = movements.filter((m) => m.longDescription && m.longDescription.trim());
  const skippedNoText = movements.length - candidates.length;

  if (only) {
    candidates = candidates.filter((m) => m.id === only);
  }

  const alreadyNarrated = [];
  let toGenerate = candidates.filter((m) => {
    const has = existsFn(audioPathFor(m.id));
    if (has && !force) {
      alreadyNarrated.push(m.id);
      return false;
    }
    return true;
  });

  if (limit !== null) toGenerate = toGenerate.slice(0, limit);

  let skippedBudget = 0;
  if (charBudget !== null) {
    const withinBudget = [];
    let total = 0;
    for (const m of toGenerate) {
      const len = textForFn(m).length;
      if (total + len > charBudget) break;
      total += len;
      withinBudget.push(m);
    }
    skippedBudget = toGenerate.length - withinBudget.length;
    toGenerate = withinBudget;
  }

  return { toGenerate, alreadyNarrated, skippedNoText, skippedBudget };
}

/**
 * The voice id to narrate a given movement with: its own override from
 * tree-narration-voices.mjs when one has been chosen, else the default
 * narrator. `voiceMap` is injected so tests never depend on the real,
 * mostly-still-blank override file.
 */
export function resolveVoiceId(movementId, { voiceMap = voiceOverrides, defaultVoiceId }) {
  const override = voiceMap[movementId];
  return override && override.trim() ? override.trim() : defaultVoiceId;
}

/**
 * One ElevenLabs TTS call. `fetchImpl` is injected so tests never make a
 * real network call - production always passes the real global fetch.
 * `modelId` is required (never defaulted). `outputFormat`, when given, is
 * sent as ElevenLabs' `output_format` query parameter (e.g. mp3_44100_64).
 * Returns the audio and the credits ElevenLabs reports charging.
 */
export async function synthesizeWithCost(text, { apiKey, voiceId, modelId, outputFormat = null, voiceSettings = defaultVoiceSettings, fetchImpl = fetch }) {
  if (!modelId) throw new Error('synthesize: modelId is required');
  const url = ELEVENLABS_TTS_URL(voiceId) + (outputFormat ? `?output_format=${encodeURIComponent(outputFormat)}` : '');
  const response = await fetchImpl(url, {
    method: 'POST',
    headers: {
      'xi-api-key': apiKey,
      'Content-Type': 'application/json',
      Accept: 'audio/mpeg',
    },
    body: JSON.stringify({
      text,
      model_id: modelId,
      voice_settings: voiceSettings,
    }),
    signal: AbortSignal.timeout(180000),
  });
  if (!response.ok) {
    const detail = await response.text().catch(() => '');
    throw new Error(`ElevenLabs TTS failed (${response.status}): ${detail.slice(0, 300)}`);
  }
  const arrayBuffer = await response.arrayBuffer();
  const cost = Number(response.headers?.get?.('character-cost') || 0);
  return { audio: Buffer.from(arrayBuffer), cost };
}

export async function synthesize(text, options) {
  return (await synthesizeWithCost(text, options)).audio;
}

async function run() {
  const opts = parseArgs(process.argv.slice(2));
  const census = JSON.parse(fs.readFileSync(censusPath, 'utf-8'));
  const { toGenerate, alreadyNarrated, skippedNoText, skippedBudget } = planNarration(census.movements, opts);
  const totalChars = toGenerate.reduce((sum, m) => sum + narrationTextFor(m).length, 0);

  console.log(`=== Tree narration ${opts.dryRun ? '(dry run)' : ''} ===`);
  console.log(`${census.movements.length} movements total`);
  console.log(`${skippedNoText} skipped - no longDescription to narrate`);
  console.log(`${alreadyNarrated.length} already narrated (use --force to regenerate)`);
  console.log(`${toGenerate.length} to generate this run${opts.limit !== null ? ` (--limit ${opts.limit})` : ''}, ${totalChars} characters total`);
  if (opts.charBudget !== null) {
    console.log(`${skippedBudget} left for a later run - would exceed the ${opts.charBudget}-character budget`);
  }

  if (toGenerate.length === 0) {
    console.log('\nNothing to do.');
    return;
  }

  const defaultVoiceId = opts.voiceId;
  if (!opts.dryRun) requirePaidSettings(opts);

  if (opts.dryRun) {
    toGenerate.forEach((m) => {
      const voiceId = resolveVoiceId(m.id, { defaultVoiceId });
      const distinct = voiceId !== defaultVoiceId ? ' [distinct voice]' : '';
      const text = narrationTextFor(m);
      const source = text === m.longDescription ? '' : ' [orientation.story]';
      console.log(`  would generate: ${m.id} (${text.length} chars)${distinct}${source}`);
    });
    return;
  }

  const apiKey = process.env.ELEVENLABS_API_KEY;
  if (!apiKey) throw new Error('ELEVENLABS_API_KEY is not set - see tools/generate_tree_narration.mjs\'s own usage note.');

  fs.mkdirSync(audioDir, { recursive: true });

  console.log('=== PAID RUN, settings as actually used ===');
  console.log(`default voice id : ${defaultVoiceId}`);
  console.log(`model            : ${opts.model}`);
  console.log(`settings         : ${JSON.stringify(defaultVoiceSettings)}`);
  console.log(`items            : ${toGenerate.length}   characters: ${totalChars}`);
  console.log('===========================================');

  let succeeded = 0;
  let credits = 0;
  const failed = [];
  for (const movement of toGenerate) {
    try {
      const voiceId = resolveVoiceId(movement.id, { defaultVoiceId });
      const text = narrationTextFor(movement);
      const { audio, cost } = await synthesizeWithCost(text, { apiKey, voiceId, modelId: opts.model, outputFormat: NARRATION_OUTPUT_FORMAT });
      fs.writeFileSync(audioPathFor(movement.id), audio);
      succeeded++;
      credits += cost;
      console.log(`  ok: ${movement.id} voice=${voiceId} model=${opts.model} chars=${text.length} cost=${cost}`);
    } catch (err) {
      failed.push({ id: movement.id, error: err.message });
      console.log(`  FAILED: ${movement.id} - ${err.message}`);
    }
  }

  console.log(`\n${succeeded}/${toGenerate.length} generated. credits charged (character-cost headers): ${credits}`);
  if (failed.length > 0) {
    console.log(`${failed.length} failed - re-run (this script skips what already succeeded) to retry just these:`);
    failed.forEach(({ id, error }) => console.log(`  - ${id}: ${error}`));
    process.exitCode = 1;
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  run().catch((err) => {
    console.error(err.message);
    process.exitCode = 1;
  });
}
