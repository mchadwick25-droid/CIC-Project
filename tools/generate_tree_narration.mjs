#!/usr/bin/env node
/**
 * Generate one-time ElevenLabs narration audio for each movement's own
 * longDescription (the "About This Movement" story on its tree/<id>.html
 * page) - Church Family Tree's narration step. One consistent narrator
 * voice across every clip, third-person historical narration matching how
 * longDescription is actually written (never a Representative speaking in
 * character - that's a separate, already-built feature).
 *
 * Output: cic-website/audio/tree/<id>.mp3, one per movement that has a
 * longDescription. Idempotent - a movement already carrying an audio file
 * is skipped unless --force, so a partial run (rate limit, a crashed
 * process, a paced multi-day batch) can always resume from where it left
 * off without re-spending on movements already narrated.
 *
 * Usage:
 *   ELEVENLABS_API_KEY=... ELEVENLABS_VOICE_ID=... node tools/generate_tree_narration.mjs [options]
 *
 * Options:
 *   --dry-run       Report what would be generated; no API calls, no files written.
 *   --only <id>     Generate (or dry-run) a single movement by its census id.
 *   --limit <n>     Cap the number of NEW clips generated this run (already-narrated
 *                   movements don't count against it). Omit to run the whole batch.
 *   --force         Regenerate even for a movement that already has an audio file.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..');
const censusPath = path.join(rootDir, 'cic-website/data/world-census.json');
export const audioDir = path.join(rootDir, 'cic-website/audio/tree');

const ELEVENLABS_TTS_URL = (voiceId) => `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;

export function parseArgs(argv) {
  const opts = { dryRun: false, only: null, limit: null, force: false };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--dry-run') opts.dryRun = true;
    else if (arg === '--force') opts.force = true;
    else if (arg === '--only') opts.only = argv[++i];
    else if (arg === '--limit') opts.limit = Number(argv[++i]);
    else throw new Error(`unrecognized argument: ${arg}`);
  }
  if (opts.limit !== null && (!Number.isInteger(opts.limit) || opts.limit < 0)) {
    throw new Error(`--limit must be a non-negative integer, got ${opts.limit}`);
  }
  return opts;
}

export function audioPathFor(movementId) {
  return path.join(audioDir, `${movementId}.mp3`);
}

/**
 * Movements that need a narration clip generated this run, in stable
 * (declared) order - never a claim about which ones already have one,
 * only which ones this run should act on given the options passed.
 */
export function planNarration(movements, { only, force, limit, existsFn = fs.existsSync }) {
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

  return { toGenerate, alreadyNarrated, skippedNoText };
}

/**
 * One ElevenLabs TTS call. `fetchImpl` is injected so tests never make a
 * real network call - production always passes the real global fetch.
 */
export async function synthesize(text, { apiKey, voiceId, fetchImpl = fetch }) {
  const response = await fetchImpl(ELEVENLABS_TTS_URL(voiceId), {
    method: 'POST',
    headers: {
      'xi-api-key': apiKey,
      'Content-Type': 'application/json',
      Accept: 'audio/mpeg',
    },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
    }),
  });
  if (!response.ok) {
    const detail = await response.text().catch(() => '');
    throw new Error(`ElevenLabs TTS failed (${response.status}): ${detail.slice(0, 300)}`);
  }
  const arrayBuffer = await response.arrayBuffer();
  return Buffer.from(arrayBuffer);
}

async function run() {
  const opts = parseArgs(process.argv.slice(2));
  const census = JSON.parse(fs.readFileSync(censusPath, 'utf-8'));
  const { toGenerate, alreadyNarrated, skippedNoText } = planNarration(census.movements, opts);

  console.log(`=== Tree narration ${opts.dryRun ? '(dry run)' : ''} ===`);
  console.log(`${census.movements.length} movements total`);
  console.log(`${skippedNoText} skipped - no longDescription to narrate`);
  console.log(`${alreadyNarrated.length} already narrated (use --force to regenerate)`);
  console.log(`${toGenerate.length} to generate this run${opts.limit !== null ? ` (--limit ${opts.limit})` : ''}`);

  if (toGenerate.length === 0) {
    console.log('\nNothing to do.');
    return;
  }

  if (opts.dryRun) {
    toGenerate.forEach((m) => console.log(`  would generate: ${m.id} (${m.longDescription.length} chars)`));
    return;
  }

  const apiKey = process.env.ELEVENLABS_API_KEY;
  const voiceId = process.env.ELEVENLABS_VOICE_ID;
  if (!apiKey) throw new Error('ELEVENLABS_API_KEY is not set - see tools/generate_tree_narration.mjs\'s own usage note.');
  if (!voiceId) throw new Error('ELEVENLABS_VOICE_ID is not set - pick a narrator voice in ElevenLabs\' dashboard first.');

  fs.mkdirSync(audioDir, { recursive: true });

  let succeeded = 0;
  const failed = [];
  for (const movement of toGenerate) {
    try {
      const audio = await synthesize(movement.longDescription, { apiKey, voiceId });
      fs.writeFileSync(audioPathFor(movement.id), audio);
      succeeded++;
      console.log(`  ok: ${movement.id}`);
    } catch (err) {
      failed.push({ id: movement.id, error: err.message });
      console.log(`  FAILED: ${movement.id} - ${err.message}`);
    }
  }

  console.log(`\n${succeeded}/${toGenerate.length} generated.`);
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
