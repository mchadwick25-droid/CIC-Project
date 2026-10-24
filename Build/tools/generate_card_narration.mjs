#!/usr/bin/env node
/**
 * Narrate the back of each conversation-chooser card: the card's own summary
 * text, read from the census the chooser reads, in one fixed narrator voice.
 * Each piece is spoken once and served as a static file.
 *
 * Output: cic-website/audio/cards/<census-id>.mp3 and manifest.json, which
 * records a fingerprint of each summary with the voice, model and settings it
 * was made with, so a later text edit shows which audio is stale.
 *
 * Usage:
 *   ELEVENLABS_API_KEY=... node Build/tools/generate_card_narration.mjs \
 *     --voice-id <id> --model <model_id> --output-format <fmt> \
 *     --settings-json '{"stability":0.55,...}' --approved-run "<name>" --char-cap <n> \
 *     [--only <census-id>,...] [--dry-run] [--force]
 *
 * --approved-run (the run Mark approved) and --char-cap (its character limit)
 * are required except with --dry-run; a run that plans more characters than
 * its cap refuses to start. Every paid setting is named on the command and
 * printed before the requests.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { requireApprovedRun, requirePaidSettings, synthesizeWithCost } from './generate_tree_narration.mjs';
import { fingerprint, parseArgs, planPieces } from './generate_site_narration.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const siteDir = path.resolve(__dirname, '..', '..', 'cic-website');
export const cardAudioDir = path.join(siteDir, 'audio/cards');
export const manifestPath = path.join(cardAudioDir, 'manifest.json');
export { fingerprint, parseArgs, planPieces };

/** One piece per built, live world with a card summary, in census order. */
export function cardPieces(census) {
  return census.movements
    .filter((m) => m.status === 'Built & Live' && m.entry && m.entry.representativeName && m.entry.summary)
    .map((m) => ({ key: m.id, text: m.entry.summary.replace(/\s+/g, ' ').trim() }));
}

async function run() {
  const opts = parseArgs(process.argv.slice(2));
  const pieces = cardPieces(JSON.parse(fs.readFileSync(path.join(siteDir, 'data/world-census.json'), 'utf8')));
  const manifest = fs.existsSync(manifestPath) ? JSON.parse(fs.readFileSync(manifestPath, 'utf8')) : {};
  const { upToDate, toGenerate } = planPieces(pieces, { manifest, only: opts.only, force: opts.force });
  const total = toGenerate.reduce((n, p) => n + p.text.length, 0);
  console.log(`=== Card-back narration ${opts.dryRun ? '(dry run)' : ''} ===`);
  console.log(`${pieces.length} pieces; ${upToDate.length} up to date; ${toGenerate.length} to generate, ${total} characters`);
  if (opts.dryRun) { toGenerate.forEach((p) => console.log(`  would generate: ${p.key} (${p.text.length} chars)`)); return; }
  if (!toGenerate.length) { console.log('Nothing to do.'); return; }
  requirePaidSettings(opts);
  requireApprovedRun(opts, total);
  for (const [flag, value] of [['--output-format', opts.outputFormat], ['--settings-json', opts.settingsJson]]) {
    if (!value || value.startsWith('--')) throw new Error(`${flag} is required and is never read from the environment.`);
  }
  const voiceSettings = JSON.parse(opts.settingsJson);
  const apiKey = process.env.ELEVENLABS_API_KEY;
  if (!apiKey) throw new Error('ELEVENLABS_API_KEY is not set.');
  console.log('=== PAID RUN, settings as actually used ===');
  console.log(`approved run  : ${opts.approvedRun}   char cap: ${opts.charCap}`);
  console.log(`voice id      : ${opts.voiceId}`);
  console.log(`model         : ${opts.model}`);
  console.log(`output format : ${opts.outputFormat}`);
  console.log(`settings      : ${JSON.stringify(voiceSettings)}`);
  console.log(`pieces        : ${toGenerate.length}, ${total} characters`);
  fs.mkdirSync(cardAudioDir, { recursive: true });
  for (const p of toGenerate) {
    const { audio, cost } = await synthesizeWithCost(p.text, { apiKey, voiceId: opts.voiceId, modelId: opts.model, outputFormat: opts.outputFormat, voiceSettings });
    fs.writeFileSync(path.join(cardAudioDir, `${p.key}.mp3`), audio);
    manifest[p.key] = { hash: fingerprint(p.text), voiceId: opts.voiceId, model: opts.model, outputFormat: opts.outputFormat, settings: voiceSettings, chars: p.text.length };
    fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
    console.log(`  ${p.key}: ${p.text.length} chars, ${cost} credits`);
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  run().catch((err) => { console.error(err.message); process.exit(1); });
}
