#!/usr/bin/env node
/**
 * Narrate the site's own pages, each piece spoken once and served as a static
 * file: The Unfolding Story (heading and body of story.html) and each section
 * of the About page (about.html), read from the pages themselves so the audio
 * and the words cannot drift apart unnoticed.
 *
 * Output: cic-website/audio/site/<key>.mp3 and manifest.json, which records a
 * fingerprint of each piece's text with the voice, model and settings it was
 * made with, so a later text edit shows which audio is stale. Idempotent: a
 * piece whose file exists and whose fingerprint matches is skipped unless
 * --force.
 *
 * Usage:
 *   ELEVENLABS_API_KEY=... node Build/tools/generate_site_narration.mjs \
 *     --voice-id <id> --model <model_id> --output-format <fmt> \
 *     --settings-json '{"stability":0.55,...}' [--only a,b] [--dry-run] [--force]
 *
 * Every paid setting is named on the command and printed before the requests.
 */
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';
import { requirePaidSettings, synthesizeWithCost } from './generate_tree_narration.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
const siteDir = path.join(rootDir, 'cic-website');
export const siteAudioDir = path.join(siteDir, 'audio/site');
export const manifestPath = path.join(siteAudioDir, 'manifest.json');
export const ABOUT_SECTIONS = ['mission', 'convictions', 'how-it-works', 'safety', 'about-us'];

const decode = (s) => s.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;|&rsquo;/g, '\u2019');
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

/**
 * One About section as it would be read aloud: its headings and paragraphs in
 * page order. The small-caps eyebrow label is navigation, not text, so it is
 * left out.
 */
export function sectionText(html, id) {
  const section = new RegExp(`<section[^>]*id="${id}"[^>]*>([\\s\\S]*?)</section>`).exec(html);
  if (!section) throw new Error(`about.html: section "${id}" not found`);
  const parts = [...section[1].matchAll(/<(h[23]|p)([^>]*)>([\s\S]*?)<\/\1>/g)]
    .filter((m) => !/class="eyebrow"/.test(m[2]))
    .map((m) => plain(m[3]))
    .filter(Boolean);
  if (!parts.length) throw new Error(`about.html: section "${id}" has no text`);
  return parts.join('\n\n');
}

/** Every narrated piece: key, and the text read from its page. */
export function sitePieces({ read = (f) => fs.readFileSync(path.join(siteDir, f), 'utf8') } = {}) {
  const about = read('about.html');
  return [
    { key: 'unfolding-story', text: storyText(read('story.html')) },
    ...ABOUT_SECTIONS.map((id) => ({ key: `about-${id}`, text: sectionText(about, id) })),
  ];
}

export function parseArgs(argv) {
  const opts = { dryRun: false, force: false, only: null, voiceId: null, model: null, outputFormat: null, settingsJson: null };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--dry-run') opts.dryRun = true;
    else if (arg === '--force') opts.force = true;
    else if (arg === '--only') opts.only = argv[++i].split(',').filter(Boolean);
    else if (arg === '--voice-id') opts.voiceId = argv[++i];
    else if (arg === '--model') opts.model = argv[++i];
    else if (arg === '--output-format') opts.outputFormat = argv[++i];
    else if (arg === '--settings-json') opts.settingsJson = argv[++i];
    else throw new Error(`unrecognized argument: ${arg}`);
  }
  return opts;
}

export function planPieces(pieces, { manifest, only = null, force = false }) {
  const chosen = only ? pieces.filter((p) => only.includes(p.key)) : pieces;
  const upToDate = [];
  const toGenerate = [];
  for (const p of chosen) {
    const fresh = manifest[p.key]?.hash === fingerprint(p.text);
    (fresh && !force ? upToDate : toGenerate).push(p);
  }
  return { upToDate, toGenerate };
}

async function run() {
  const opts = parseArgs(process.argv.slice(2));
  const pieces = sitePieces();
  const manifest = fs.existsSync(manifestPath) ? JSON.parse(fs.readFileSync(manifestPath, 'utf8')) : {};
  const { upToDate, toGenerate } = planPieces(pieces, { manifest, only: opts.only, force: opts.force });
  const total = toGenerate.reduce((n, p) => n + p.text.length, 0);
  console.log(`=== Site narration ${opts.dryRun ? '(dry run)' : ''} ===`);
  console.log(`${pieces.length} pieces; ${upToDate.length} up to date; ${toGenerate.length} to generate, ${total} characters`);
  if (opts.dryRun) { toGenerate.forEach((p) => console.log(`  would generate: ${p.key} (${p.text.length} chars)`)); return; }
  if (!toGenerate.length) { console.log('Nothing to do.'); return; }
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
  console.log(`pieces        : ${toGenerate.length}, ${total} characters`);
  fs.mkdirSync(siteAudioDir, { recursive: true });
  for (const p of toGenerate) {
    const { audio, cost } = await synthesizeWithCost(p.text, { apiKey, voiceId: opts.voiceId, modelId: opts.model, outputFormat: opts.outputFormat, voiceSettings });
    fs.writeFileSync(path.join(siteAudioDir, `${p.key}.mp3`), audio);
    manifest[p.key] = { hash: fingerprint(p.text), voiceId: opts.voiceId, model: opts.model, outputFormat: opts.outputFormat, settings: voiceSettings, chars: p.text.length };
    fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
    console.log(`  ${p.key}: ${p.text.length} chars, ${cost} credits`);
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  run().catch((err) => { console.error(err.message); process.exit(1); });
}
