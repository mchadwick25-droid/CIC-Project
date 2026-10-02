#!/usr/bin/env node
/**
 * Narrate The Unfolding Story: the heading and body paragraphs of
 * cic-website/story.html, spoken once and served as a static file.
 *
 * Output: cic-website/audio/site/unfolding-story.mp3 and manifest.json, which
 * records a fingerprint of the text, the voice, the model and the settings the
 * file was made with, so a later text edit shows the audio is stale.
 *
 * Usage:
 *   ELEVENLABS_API_KEY=... node Build/tools/generate_site_narration.mjs \
 *     --voice-id <id> --model <model_id> --output-format <fmt> \
 *     --settings-json '{"stability":0.55,...}' [--dry-run] [--force]
 *
 * Every paid setting is named on the command and printed before the request.
 */
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';
import { requirePaidSettings, synthesizeWithCost } from './generate_tree_narration.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
const storyPath = path.join(rootDir, 'cic-website/story.html');
export const siteAudioDir = path.join(rootDir, 'cic-website/audio/site');
export const manifestPath = path.join(siteAudioDir, 'manifest.json');
export const KEY = 'unfolding-story';

const decode = (s) => s.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;|&rsquo;/g, '’');
const plain = (s) => decode(s.replace(/<[^>]+>/g, '')).replace(/\s+/g, ' ').trim();

export function fingerprint(text) {
  return crypto.createHash('sha256').update(text).digest('hex').slice(0, 16);
}

/** The heading, then each paragraph of the story body, in page order. */
export function storyText(html) {
  const h1 = /<h1[^>]*id="story-title"[^>]*>([\s\S]*?)<\/h1>/.exec(html);
  const body = /<div class="story-body">([\s\S]*?)<\/div>/.exec(html);
  if (!h1 || !body) throw new Error('story.html: heading or story body not found');
  const paras = [...body[1].matchAll(/<p[^>]*>([\s\S]*?)<\/p>/g)].map((m) => plain(m[1])).filter(Boolean);
  return [plain(h1[1]), ...paras].join('\n\n');
}

export function parseArgs(argv) {
  const opts = { dryRun: false, force: false, voiceId: null, model: null, outputFormat: null, settingsJson: null };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--dry-run') opts.dryRun = true;
    else if (arg === '--force') opts.force = true;
    else if (arg === '--voice-id') opts.voiceId = argv[++i];
    else if (arg === '--model') opts.model = argv[++i];
    else if (arg === '--output-format') opts.outputFormat = argv[++i];
    else if (arg === '--settings-json') opts.settingsJson = argv[++i];
    else throw new Error(`unrecognized argument: ${arg}`);
  }
  return opts;
}

async function run() {
  const opts = parseArgs(process.argv.slice(2));
  const text = storyText(fs.readFileSync(storyPath, 'utf8'));
  const hash = fingerprint(text);
  const manifest = fs.existsSync(manifestPath) ? JSON.parse(fs.readFileSync(manifestPath, 'utf8')) : {};
  const file = path.join(siteAudioDir, `${KEY}.mp3`);
  const upToDate = fs.existsSync(file) && manifest[KEY]?.hash === hash;
  console.log(`=== Unfolding Story narration ${opts.dryRun ? '(dry run)' : ''} ===`);
  console.log(`${text.length} characters; ${upToDate ? 'up to date' : 'to generate'}`);
  if (opts.dryRun) return;
  if (upToDate && !opts.force) { console.log('Nothing to do.'); return; }
  requirePaidSettings(opts);
  for (const [flag, value] of [['--output-format', opts.outputFormat], ['--settings-json', opts.settingsJson]]) {
    if (!value || value.startsWith('--')) throw new Error(`${flag} is required and is never read from the environment.`);
  }
  const voiceSettings = JSON.parse(opts.settingsJson);
  const apiKey = process.env.ELEVENLABS_API_KEY;
  if (!apiKey) throw new Error('ELEVENLABS_API_KEY is not set.');
  console.log('=== PAID RUN, settings as actually used ===');
  console.log(`voice id      : ${opts.voiceId}`);
  console.log(`model         : ${opts.model}`);
  console.log(`output format : ${opts.outputFormat}`);
  console.log(`settings      : ${JSON.stringify(voiceSettings)}`);
  console.log(`characters    : ${text.length}`);
  const { audio, cost } = await synthesizeWithCost(text, { apiKey, voiceId: opts.voiceId, modelId: opts.model, outputFormat: opts.outputFormat, voiceSettings });
  fs.mkdirSync(siteAudioDir, { recursive: true });
  fs.writeFileSync(file, audio);
  manifest[KEY] = { hash, voiceId: opts.voiceId, model: opts.model, outputFormat: opts.outputFormat, settings: voiceSettings, chars: text.length };
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
  console.log(`wrote ${path.relative(rootDir, file)} (${audio.length} bytes, ${cost} credits)`);
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  run().catch((err) => { console.error(err.message); process.exit(1); });
}
