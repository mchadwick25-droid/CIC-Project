
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { slimMap, writeSlimMap } from './slim_map_data.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const OUT = path.join(ROOT, '.build', 'tree');

export const TREE_FILES = [
  ['cft-website', '.'],
];

export const SHARED_FILES = [
  'data/world-census.json',
  'data/worlds',
  'assets/narration-player.js',
  'assets/feedback.js',
  'assets/feedback.css',
  'assets/favicon.svg',
  'assets/og-image.jpg',
  'assets/place-line.js',
  'assets/orientation-render.mjs',
  'assets/portraits',
  'assets/world-icons',
  'audio/worlds',
].map((p) => [`cic-website/${p}`, p]);

function filesUnder(abs) {
  const stat = fs.statSync(abs);
  if (stat.isFile()) return [''];
  const out = [];
  for (const entry of fs.readdirSync(abs, { withFileTypes: true })) {
    for (const rel of filesUnder(path.join(abs, entry.name))) {
      out.push(rel ? path.join(entry.name, rel) : entry.name);
    }
  }
  return out;
}

function digest(file) {
  return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
}

function copyAll(pairs) {
  const copied = [];
  for (const [from, to] of pairs) {
    const src = path.join(ROOT, from);
    if (!fs.existsSync(src)) throw new Error(`missing source: ${from}`);
    for (const rel of filesUnder(src)) {
      const s = rel ? path.join(src, rel) : src;
      const d = path.join(OUT, to, rel);
      fs.mkdirSync(path.dirname(d), { recursive: true });
      fs.copyFileSync(s, d);
      copied.push([s, d]);
    }
  }
  return copied;
}

function main() {
  fs.rmSync(OUT, { recursive: true, force: true });
  fs.mkdirSync(OUT, { recursive: true });
  const own = copyAll(TREE_FILES);
  const shared = copyAll(SHARED_FILES);
  // The committed page holds all the data. The site gets the slim page and the card files (see
  // tools/slim_map_data.mjs), so its copy of index.html differs from the source by design.
  const slim = slimMap(fs.readFileSync(path.join(ROOT, 'cft-website', 'index.html'), 'utf8'));
  writeSlimMap(slim, OUT, false);
  const page = path.join(OUT, 'index.html');
  const mismatched = [...own, ...shared].filter(([s, d]) => d !== page && digest(s) !== digest(d));
  for (const [s, d] of mismatched) {
    console.error(`copy differs from its source: ${path.relative(ROOT, d)} <- ${path.relative(ROOT, s)}`);
  }
  console.log(`tree site: ${own.length} own files (the map page slimmed, ${Object.keys(slim.entries).length} card files added), ${shared.length} shared files, ${mismatched.length} mismatched, in ${path.relative(ROOT, OUT)}/`);
  if (mismatched.length) process.exit(1);
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main();
