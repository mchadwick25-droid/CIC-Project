#!/usr/bin/env node
/**
 * Narrate a built world's own long-form text in that world's Representative
 * voice: the world story (orientation.story), each documented story's
 * telling, and the legacy piece. Never a teaser, caveat, hedge or bio, and
 * never a story's source wording (`text`), which the site JSON does not carry.
 *
 * --tree records the Church Family Tree's own copies instead: each piece's text
 * comes from Build/Ministry/Features/Church-Family-Tree/World-Narration/<census-id>/<key>.txt
 * (the reviewed narrator rewrite), a piece whose <key>.orig.txt no longer matches
 * the compiled world text is refused as stale, and the clips and manifest go to
 * cft-website/audio/worlds-tree/, each entry carrying the text it was recorded from,
 * and the world's entry listing all its pieces (_pieces), so the map switches a
 * world to these copies only when every piece is recorded.
 *
 * Output: cic-website/audio/worlds/<census-id>/{story,docstory-<story id>,legacy}.mp3
 * and cic-website/audio/worlds/manifest.json, which the Atlas panel and the
 * static tradition pages read to decide which players to show. A story longer
 * than the model's per-request limit is sent in parts and joined into one file.
 * Every clip is then sped up by --tempo (ffmpeg atempo, pitch-preserving).
 *
 * Usage:
 *   ELEVENLABS_API_KEY=... node Build/tools/generate_world_narration.mjs \
 *     --world <census-id> --voice-id <id> --model <model_id> \
 *     --api-speed <n> --tempo <n> --settings-json '<voice_settings>' \
 *     --approved-run "<name>" --char-cap <n> [--prefix '[audio tag] '] [--only <key,...>] [--dry-run] [--force]
 *
 * --approved-run (the run Mark approved after hearing its sample) and
 * --char-cap (its character limit, counting the prefix on every request) are
 * required except with --dry-run; a run that plans more refuses to start.
 *
 * --prefix puts an instruction (e.g. an accent tag) in front of every request's
 * text; it is printed and recorded in the manifest.
 *
 * A piece already in the manifest is skipped. --only names the pieces to
 * record (story, legacy, docstory-<story id>), whether or not they are in
 * the manifest, so a changed text is re-recorded without paying for the
 * rest; --force records every piece.
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
import { NARRATION_BITRATE, NARRATION_OUTPUT_FORMAT, requireApprovedRun, requireVoiceAndModel, synthesizeWithCost, worldsDataDir } from './generate_tree_narration.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
export const worldAudioDir = path.join(rootDir, 'cic-website/audio/worlds');
export const worldManifestPath = path.join(worldAudioDir, 'manifest.json');
export const treeTextDir = path.join(rootDir, 'Build/Ministry/Features/Church-Family-Tree/World-Narration');
export const treeAudioDir = path.join(rootDir, 'cft-website/audio/worlds-tree');
export const treeManifestPath = path.join(treeAudioDir, 'manifest.json');
export const MAX_CHARS_PER_REQUEST = 4500;

export function parseArgs(argv) {
  const o = { world: null, voiceId: null, model: null, apiSpeed: null, tempo: null, settingsJson: null, prefix: '', only: null, dryRun: false, force: false, approvedRun: null, charCap: null, tree: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--dry-run') o.dryRun = true;
    else if (a === '--tree') o.tree = true;
    else if (a === '--force') o.force = true;
    else if (a === '--world') o.world = argv[++i];
    else if (a === '--voice-id') o.voiceId = argv[++i];
    else if (a === '--model') o.model = argv[++i];
    else if (a === '--api-speed') o.apiSpeed = Number(argv[++i]);
    else if (a === '--tempo') o.tempo = Number(argv[++i]);
    else if (a === '--settings-json') o.settingsJson = argv[++i];
    else if (a === '--prefix') o.prefix = argv[++i];
    else if (a === '--only') o.only = argv[++i].split(',').map((k) => k.trim()).filter(Boolean);
    else if (a === '--approved-run') o.approvedRun = argv[++i];
    else if (a === '--char-cap') o.charCap = Number(argv[++i]);
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
  for (const s of o.documented_stories || []) {
    if (s.telling && s.telling.trim()) pieces.push({ key: `docstory-${s.story_id}`, parts: splitParagraphs(s.telling.split(/\n\n+/)) });
  }
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

const squash = (t) => t.replace(/\s+/g, ' ').trim();

/**
 * The tree's pieces: each world piece's text replaced by its reviewed narrator
 * rewrite. Throws when a rewrite is missing, or when the world text it was
 * rewritten from (<key>.orig.txt) no longer matches the compiled text.
 */
export function treePieces(world, pieces, textDir = treeTextDir) {
  return pieces.map((p) => {
    const dir = path.join(textDir, world);
    const textFile = path.join(dir, `${p.key}.txt`), origFile = path.join(dir, `${p.key}.orig.txt`);
    if (!fs.existsSync(textFile) || !fs.existsSync(origFile)) throw new Error(`${world}/${p.key}: no reviewed rewrite in ${path.relative(rootDir, dir)}`);
    if (squash(fs.readFileSync(origFile, 'utf-8')) !== squash(p.parts.flat().join('\n\n'))) throw new Error(`${world}/${p.key}: stale, the world text changed after the rewrite`);
    const text = fs.readFileSync(textFile, 'utf-8').trim();
    return { key: p.key, text, parts: splitParagraphs(text.split(/\n\n+/).map((t) => t.trim()).filter(Boolean)) };
  });
}

/** Characters the run will send: the pieces it does not skip, each request with its prefix. */
export function billableChars(pieces, entry, { prefix = '', force = false, only = null } = {}) {
  return pieces
    .filter((p) => !(entry[p.key] && !force && !only))
    .reduce((n, p) => n + p.parts.reduce((m, t) => m + prefix.length + t.length, 0), 0);
}

async function run() {
  const opts = parseArgs(process.argv.slice(2));
  if (!opts.world) throw new Error('--world is required');
  const compiled = JSON.parse(fs.readFileSync(path.join(worldsDataDir, `${opts.world}.json`), 'utf-8'));
  const all = worldPieces(compiled);
  if (opts.only) {
    const unknown = opts.only.filter((k) => !all.some((p) => p.key === k));
    if (unknown.length) throw new Error(`--only names no such piece: ${unknown.join(', ')}`);
  }
  const chosen = opts.only ? all.filter((p) => opts.only.includes(p.key)) : all;
  const pieces = opts.tree ? treePieces(opts.world, chosen) : chosen;
  const audioDir = opts.tree ? treeAudioDir : worldAudioDir, manifestPath = opts.tree ? treeManifestPath : worldManifestPath;
  const manifest = fs.existsSync(manifestPath) ? JSON.parse(fs.readFileSync(manifestPath, 'utf-8')) : {};
  const chars = pieces.reduce((n, p) => n + p.parts.reduce((m, t) => m + t.length, 0), 0);
  console.log(`=== World narration ${opts.tree ? '(tree copies) ' : ''}${opts.dryRun ? '(dry run)' : ''}: ${opts.world} ===`);
  pieces.forEach((p) => console.log(`  ${p.key}: ${p.parts.length} request(s), ${p.parts.map((t) => t.length).join('+')} chars`));
  console.log(`  total ${chars} characters`);
  if (opts.dryRun) return;

  requireVoiceAndModel(opts);
  requireApprovedRun(opts, billableChars(pieces, manifest[opts.world] || {}, opts));
  for (const [flag, v] of [['--api-speed', opts.apiSpeed], ['--tempo', opts.tempo], ['--settings-json', opts.settingsJson]]) {
    if (!v) throw new Error(`${flag} is required and is never read from the environment.`);
  }
  const apiKey = process.env.ELEVENLABS_API_KEY;
  if (!apiKey) throw new Error('ELEVENLABS_API_KEY is not set.');
  const settings = { ...JSON.parse(opts.settingsJson), speed: opts.apiSpeed };
  const outDir = path.join(audioDir, opts.world);
  fs.mkdirSync(outDir, { recursive: true });

  console.log('=== PAID RUN, settings as actually used ===');
  console.log(`approved run : ${opts.approvedRun}   char cap: ${opts.charCap}`);
  console.log(`voice id : ${opts.voiceId}\nmodel    : ${opts.model}\nsettings : ${JSON.stringify(settings)}\nprefix   : ${opts.prefix ? JSON.stringify(opts.prefix) : '(none)'}\nformat   : ${NARRATION_OUTPUT_FORMAT}, re-encoded at ${NARRATION_BITRATE} mono\ntempo    : ${opts.tempo}x after synthesis\nchars    : ${chars}`);
  console.log('===========================================');

  const entry = manifest[opts.world] || {};
  let credits = 0;
  for (const p of pieces) {
    const finalPath = path.join(outDir, `${p.key}.mp3`);
    if (entry[p.key] && !opts.force && !opts.only) { console.log(`  skip (in manifest): ${p.key}`); continue; }
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
    if (opts.tree) { entry[p.key].text = p.text; entry._pieces = all.map((x) => x.key); }
    manifest[opts.world] = entry;
    fs.mkdirSync(path.dirname(manifestPath), { recursive: true });
    fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 1) + '\n');
  }
  console.log(`\ncredits charged (character-cost headers): ${credits}`);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  run().catch((e) => { console.error(e.message); process.exitCode = 1; });
}
