#!/usr/bin/env node
/**
 * Narrate the documented stories inside the unbuilt movements of the Church
 * Family Tree (world-census.json `documentedStories[].text`). Story text
 * only - never the teaser or the caveat. Built worlds are excluded: their
 * stories live in compiled world data, a separate step.
 *
 * Output: cic-website/audio/docstories/<movement-id>-<n>.mp3 (n = 0-based
 * position in the movement's documentedStories) and manifest.json, which
 * records a fingerprint of the text each file was made from, so a later text
 * edit shows which audio is stale. Idempotent: a story whose file exists and
 * whose fingerprint matches is skipped unless --force.
 *
 * Usage:
 *   ELEVENLABS_API_KEY=... node Build/tools/generate_docstory_narration.mjs \
 *     --voice-id <id> --model <model_id> --output-format <fmt> [options]
 *
 * --voice-id, --model and --output-format are required (except --dry-run) and
 * never read from the environment. The run prints the settings it sends and
 * one line per request with the credits charged.
 *
 * Options:
 *   --dry-run        Report the plan; no API calls, no files written.
 *   --only a,b       Only these keys (e.g. antiochene-church-third-century-0).
 *   --limit <n>      Cap the NEW clips generated this run.
 *   --force          Regenerate even when the file and fingerprint match.
 */
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';
import { defaultVoiceSettings, requirePaidSettings, synthesizeWithCost, worldsDataDir } from './generate_tree_narration.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
const censusPath = path.join(rootDir, 'cic-website/data/world-census.json');
export const docStoryAudioDir = path.join(rootDir, 'cic-website/audio/docstories');
export const manifestPath = path.join(docStoryAudioDir, 'manifest.json');

export function parseArgs(argv) {
  const opts = { dryRun: false, only: null, limit: null, force: false, voiceId: null, model: null, outputFormat: null };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--dry-run') opts.dryRun = true;
    else if (arg === '--force') opts.force = true;
    else if (arg === '--only') opts.only = argv[++i].split(',').filter(Boolean);
    else if (arg === '--limit') opts.limit = Number(argv[++i]);
    else if (arg === '--voice-id') opts.voiceId = argv[++i];
    else if (arg === '--model') opts.model = argv[++i];
    else if (arg === '--output-format') opts.outputFormat = argv[++i];
    else throw new Error(`unrecognized argument: ${arg}`);
  }
  if (opts.limit !== null && (!Number.isInteger(opts.limit) || opts.limit < 0)) {
    throw new Error(`--limit must be a non-negative integer, got ${opts.limit}`);
  }
  return opts;
}

export const audioPathFor = (key) => path.join(docStoryAudioDir, `${key}.mp3`);
export const fingerprint = (text) => crypto.createHash('sha256').update(text).digest('hex').slice(0, 16);

/** Every documented story of every unbuilt movement that has story text. */
export function docStoryEntries(movements, builtIds) {
  const entries = [];
  for (const m of movements) {
    if (builtIds.has(m.id)) continue;
    (m.documentedStories || []).forEach((s, index) => {
      if (s.text && s.text.trim()) {
        entries.push({ key: `${m.id}-${index}`, movementId: m.id, index, title: s.title, text: s.text, hash: fingerprint(s.text) });
      }
    });
  }
  return entries;
}

export function planDocStories(entries, { only = null, limit = null, force = false, manifest = {}, existsFn = fs.existsSync }) {
  let candidates = only ? entries.filter((e) => only.includes(e.key)) : entries;
  const upToDate = [];
  let toGenerate = candidates.filter((e) => {
    const done = existsFn(audioPathFor(e.key)) && manifest[e.key]?.hash === e.hash;
    if (done && !force) { upToDate.push(e.key); return false; }
    return true;
  });
  if (limit !== null) toGenerate = toGenerate.slice(0, limit);
  return { toGenerate, upToDate };
}

/** Manifest keys whose audio was made from text that has since changed. */
export function staleKeys(entries, manifest) {
  return entries.filter((e) => manifest[e.key] && manifest[e.key].hash !== e.hash).map((e) => e.key);
}

async function run() {
  const opts = parseArgs(process.argv.slice(2));
  const census = JSON.parse(fs.readFileSync(censusPath, 'utf-8'));
  const built = new Set(fs.readdirSync(worldsDataDir).map((f) => f.replace('.json', '')));
  const entries = docStoryEntries(census.movements, built);
  const manifest = fs.existsSync(manifestPath) ? JSON.parse(fs.readFileSync(manifestPath, 'utf-8')) : {};
  const { toGenerate, upToDate } = planDocStories(entries, { ...opts, manifest });
  const totalChars = toGenerate.reduce((n, e) => n + e.text.length, 0);

  console.log(`=== Documented-story narration ${opts.dryRun ? '(dry run)' : ''} ===`);
  console.log(`${entries.length} stories in unbuilt movements; ${upToDate.length} up to date; ${toGenerate.length} to generate, ${totalChars} characters`);
  const stale = staleKeys(entries, manifest);
  if (stale.length) console.log(`STALE (text changed since narrated): ${stale.join(', ')}`);
  if (opts.dryRun) { toGenerate.forEach((e) => console.log(`  would generate: ${e.key} (${e.text.length} chars)`)); return; }
  if (toGenerate.length === 0) { console.log('Nothing to do.'); return; }

  requirePaidSettings(opts);
  if (!opts.outputFormat || opts.outputFormat.startsWith('--')) throw new Error('--output-format is required and is never read from the environment.');
  const apiKey = process.env.ELEVENLABS_API_KEY;
  if (!apiKey) throw new Error('ELEVENLABS_API_KEY is not set.');

  fs.mkdirSync(docStoryAudioDir, { recursive: true });
  console.log('=== PAID RUN, settings as actually used ===');
  console.log(`voice id      : ${opts.voiceId}`);
  console.log(`model         : ${opts.model}`);
  console.log(`output format : ${opts.outputFormat}`);
  console.log(`settings      : ${JSON.stringify(defaultVoiceSettings)}`);
  console.log(`items         : ${toGenerate.length}   characters: ${totalChars}`);
  console.log('===========================================');

  let ok = 0, credits = 0;
  const failed = [];
  for (const e of toGenerate) {
    try {
      const { audio, cost } = await synthesizeWithCost(e.text, { apiKey, voiceId: opts.voiceId, modelId: opts.model, outputFormat: opts.outputFormat });
      fs.writeFileSync(audioPathFor(e.key), audio);
      manifest[e.key] = { hash: e.hash, voiceId: opts.voiceId, model: opts.model, outputFormat: opts.outputFormat, chars: e.text.length };
      fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 1) + '\n');
      ok++; credits += cost;
      console.log(`  ok: ${e.key} voice=${opts.voiceId} model=${opts.model} format=${opts.outputFormat} chars=${e.text.length} cost=${cost} bytes=${audio.length}`);
    } catch (err) {
      failed.push(e.key);
      console.log(`  FAILED: ${e.key} - ${err.message}`);
    }
  }
  console.log(`\n${ok}/${toGenerate.length} generated. credits charged (character-cost headers): ${credits}`);
  if (failed.length) { console.log(`failed (re-run to retry only these): ${failed.join(', ')}`); process.exitCode = 1; }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  run().catch((err) => { console.error(err.message); process.exitCode = 1; });
}
