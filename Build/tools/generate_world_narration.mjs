#!/usr/bin/env node
/**
 * Narrate a built world's own long-form text in that world's Representative
 * voice: the world story (orientation.story), each documented story, and the
 * legacy piece. Text only; never a teaser, caveat, hedge or bio.
 *
 * Output: cic-website/audio/worlds/<census-id>/{story,docstory-<n>,legacy}.mp3
 * and cic-website/audio/worlds/manifest.json, which the Atlas panel and the
 * static tradition pages read to decide which players to show. A story longer
 * than the model's per-request limit is sent in parts and joined into one file.
 * Every clip is then sped up by --tempo (ffmpeg atempo, pitch-preserving).
 *
 * Usage:
 *   ELEVENLABS_API_KEY=... node Build/tools/generate_world_narration.mjs \
 *     --world <census-id> --voice-id <id> --model <model_id> \
 *     --api-speed <n> --tempo <n> --settings-json '<voice_settings>' [--prefix '[audio tag] '] [--dry-run] [--force]
 *
 * --prefix puts an instruction (e.g. an accent tag) in front of every request's
 * text; it is printed and recorded in the manifest.
 *
 * Voice, model, settings, speed and tempo are all required (except --dry-run)
 * and never read from the environment; the run prints what it sends and the
 * credits charged per request.
 */
import fs from 'fs';
import path from 'path';
import os from 'os';
import { execFileSync } from 'child_process';
import { fileURLToPath } from 'url';
import { NARRATION_BITRATE, NARRATION_OUTPUT_FORMAT, requirePaidSettings, synthesizeWithCost, worldsDataDir } from './generate_tree_narration.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
export const worldAudioDir = path.join(rootDir, 'cic-website/audio/worlds');
export const worldManifestPath = path.join(worldAudioDir, 'manifest.json');
export const MAX_CHARS_PER_REQUEST = 4500;

export function parseArgs(argv) {
  const o = { world: null, voiceId: null, model: null, apiSpeed: null, tempo: null, settingsJson: null, prefix: '', dryRun: false, force: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--dry-run') o.dryRun = true;
    else if (a === '--force') o.force = true;
    else if (a === '--world') o.world = argv[++i];
    else if (a === '--voice-id') o.voiceId = argv[++i];
    else if (a === '--model') o.model = argv[++i];
    else if (a === '--api-speed') o.apiSpeed = Number(argv[++i]);
    else if (a === '--tempo') o.tempo = Number(argv[++i]);
    else if (a === '--settings-json') o.settingsJson = argv[++i];
    else if (a === '--prefix') o.prefix = argv[++i];
    else throw new Error(`unrecognized argument: ${a}`);
  }
  return o;
}

/** Split paragraphs into the fewest balanced parts, each at most `max` characters. */
export function splitParagraphs(paras, max = MAX_CHARS_PER_REQUEST) {
  const total = paras.reduce((n, p) => n + p.length + 2, 0);
  const parts = Math.max(1, Math.ceil(total / max));
  const target = total / parts;
  const out = [];
  let cur = [], len = 0;
  for (const p of paras) {
    if (cur.length && len + p.length > target && out.length < parts - 1) { out.push(cur); cur = []; len = 0; }
    cur.push(p); len += p.length + 2;
  }
  if (cur.length) out.push(cur);
  return out.map((ps) => ps.join('\n\n'));
}

/** The narratable pieces of a compiled world: [{ key, parts: [text, ...] }]. */
export function worldPieces(compiled) {
  const o = compiled.orientation || {};
  const pieces = [];
  const story = (o.story || []).map((u) => u.text).filter(Boolean);
  if (story.length) pieces.push({ key: 'story', parts: splitParagraphs(story) });
  (o.documented_stories || []).forEach((s, i) => {
    if (s.text && s.text.trim()) pieces.push({ key: `docstory-${i}`, parts: splitParagraphs([s.text]) });
  });
  const legacy = (o.legacy || []).map((u) => u.text).filter(Boolean);
  if (legacy.length) pieces.push({ key: 'legacy', parts: splitParagraphs(legacy) });
  return pieces;
}

function tempoFile(inFiles, outFile, tempo) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'wn-'));
  const list = path.join(dir, 'list.txt');
  fs.writeFileSync(list, inFiles.map((f) => `file '${f}'`).join('\n'));
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', list, '-filter:a', `atempo=${tempo}`, '-ac', '1', '-ar', '44100', '-b:a', NARRATION_BITRATE, outFile]);
  fs.rmSync(dir, { recursive: true, force: true });
}

async function run() {
  const opts = parseArgs(process.argv.slice(2));
  if (!opts.world) throw new Error('--world is required');
  const compiled = JSON.parse(fs.readFileSync(path.join(worldsDataDir, `${opts.world}.json`), 'utf-8'));
  const pieces = worldPieces(compiled);
  const manifest = fs.existsSync(worldManifestPath) ? JSON.parse(fs.readFileSync(worldManifestPath, 'utf-8')) : {};
  const chars = pieces.reduce((n, p) => n + p.parts.reduce((m, t) => m + t.length, 0), 0);
  console.log(`=== World narration ${opts.dryRun ? '(dry run)' : ''}: ${opts.world} ===`);
  pieces.forEach((p) => console.log(`  ${p.key}: ${p.parts.length} request(s), ${p.parts.map((t) => t.length).join('+')} chars`));
  console.log(`  total ${chars} characters`);
  if (opts.dryRun) return;

  requirePaidSettings(opts);
  for (const [flag, v] of [['--api-speed', opts.apiSpeed], ['--tempo', opts.tempo], ['--settings-json', opts.settingsJson]]) {
    if (!v) throw new Error(`${flag} is required and is never read from the environment.`);
  }
  const apiKey = process.env.ELEVENLABS_API_KEY;
  if (!apiKey) throw new Error('ELEVENLABS_API_KEY is not set.');
  const settings = { ...JSON.parse(opts.settingsJson), speed: opts.apiSpeed };
  const outDir = path.join(worldAudioDir, opts.world);
  fs.mkdirSync(outDir, { recursive: true });

  console.log('=== PAID RUN, settings as actually used ===');
  console.log(`voice id : ${opts.voiceId}\nmodel    : ${opts.model}\nsettings : ${JSON.stringify(settings)}\nprefix   : ${opts.prefix ? JSON.stringify(opts.prefix) : '(none)'}\nformat   : ${NARRATION_OUTPUT_FORMAT}, re-encoded at ${NARRATION_BITRATE} mono\ntempo    : ${opts.tempo}x after synthesis\nchars    : ${chars}`);
  console.log('===========================================');

  const entry = manifest[opts.world] || {};
  let credits = 0;
  for (const p of pieces) {
    const finalPath = path.join(outDir, `${p.key}.mp3`);
    if (entry[p.key] && !opts.force) { console.log(`  skip (in manifest): ${p.key}`); continue; }
    const partFiles = [];
    for (const [i, text] of p.parts.entries()) {
      const { audio, cost } = await synthesizeWithCost(opts.prefix + text, { apiKey, voiceId: opts.voiceId, modelId: opts.model, voiceSettings: settings, outputFormat: NARRATION_OUTPUT_FORMAT });
      const f = path.join(os.tmpdir(), `${opts.world}-${p.key}-${i}.mp3`);
      fs.writeFileSync(f, audio);
      partFiles.push(f);
      credits += cost;
      console.log(`  ok: ${p.key} part ${i + 1}/${p.parts.length} voice=${opts.voiceId} model=${opts.model} chars=${text.length} cost=${cost}`);
    }
    tempoFile(partFiles, finalPath, opts.tempo);
    partFiles.forEach((f) => fs.rmSync(f, { force: true }));
    entry[p.key] = { file: `${opts.world}/${p.key}.mp3`, chars: p.parts.reduce((n, t) => n + t.length, 0), voiceId: opts.voiceId, model: opts.model, apiSpeed: opts.apiSpeed, tempo: opts.tempo, outputFormat: NARRATION_OUTPUT_FORMAT, prefix: opts.prefix || undefined, settings: JSON.parse(opts.settingsJson) };
    manifest[opts.world] = entry;
    fs.writeFileSync(worldManifestPath, JSON.stringify(manifest, null, 1) + '\n');
  }
  console.log(`\ncredits charged (character-cost headers): ${credits}`);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  run().catch((e) => { console.error(e.message); process.exitCode = 1; });
}
