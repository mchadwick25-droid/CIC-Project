import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const { normalize, words, TEXT_PATHS, visibleText } = createRequire(import.meta.url)(path.join(ROOT, 'cft-website', 'search-core.js'));

export const NAMES_FILE = path.join(ROOT, 'cic-website', 'data', 'search-names.json');

// Measured on census release 52: about 22 KB and 175 to 205 KB compressed. The build fails over these.
export const BUDGET = { namesGzipBytes: 32 * 1024, wordsGzipBytes: 245 * 1024 };

export { TEXT_PATHS, visibleText };

export const NAME_KIND = { name: 'n', short: 's', everyday: 'e', other: 'o' };
export const SOURCED_KIND = {
  'other name': 'o', 'older name': 'l', spelling: 'p', 'name given by opponents': 'x',
};

export function extractFamilies(html) {
  const m = /const FAM=(\[[\s\S]*?\n\]);/.exec(html);
  if (!m) throw new Error('the page has no "const FAM=[...]" list of rivers');
  const list = new Function(`return ${m[1]};`)();
  return list.map((f) => ({ k: f.k, name: f.name, common: f.common || '' }));
}

export function readNamesFile(file = NAMES_FILE) {
  if (!fs.existsSync(file)) return { rows: [], present: false };
  const json = JSON.parse(fs.readFileSync(file, 'utf8'));
  const rows = Array.isArray(json) ? json : json.rows;
  if (!Array.isArray(rows)) throw new Error('the names file holds no list of rows');
  return { rows, present: true };
}

const dedupe = (list) => [...new Set(list.filter(Boolean))];

// What the visitor can type to reach an entry: its own names, with the kind of each.
export function namesOf(m) {
  const out = [];
  const add = (text, kind) => { const n = normalize(text); if (n) out.push([n, kind]); };
  add(m.name, 'n'); add(m.shortName, 's'); add(m.informalName, 'e');
  for (const o of (m.card && m.card.otherNames) || []) add(o, 'o');
  const seen = new Set();
  return out.filter(([n]) => (seen.has(n) ? false : seen.add(n)));
}

export function buildNamesIndex(data, families, namesFile = { rows: [] }) {
  const movements = data.movements;
  const index = new Map(movements.map((m, i) => [m.id, i]));
  const entries = movements.map((m) => m.id);
  const names = [];
  movements.forEach((m, i) => { for (const [n, k] of namesOf(m)) names.push([n, i, k]); });
  const places = [];
  const problems = [];
  for (const row of namesFile.rows) {
    const n = normalize(row.name);
    const kind = SOURCED_KIND[row.kind];
    if (!n || !kind) { problems.push(`bad row: ${JSON.stringify(row).slice(0, 80)}`); continue; }
    if (row.entry != null) {
      if (!index.has(row.entry)) { problems.push(`no such entry: ${row.entry}`); continue; }
      names.push([n, index.get(row.entry), kind]);
    } else if (row.country != null || row.region != null) {
      places.push([n, row.country != null ? 'c' : 'r', row.country != null ? row.country : row.region, kind]);
    } else problems.push(`row has no entry, country or region: ${row.name}`);
  }
  if (problems.length) throw new Error(`the names file has rows the index cannot place:\n${problems.join('\n')}`);
  names.sort((a, b) => (a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : a[1] - b[1]));
  return {
    v: 1,
    eras: data.eras.map((e) => [e.num, e.title, e.academicName || '', e.dates]),
    rivers: families.map((f) => [f.k, f.name, f.common]),
    entries, living: movements.flatMap((m, i) => (m.living ? [i] : [])), names, places,
  };
}

const STOP = new Set(('the and for that with was were this from they their have had not but are his her its who which ' +
  'also been into than then them these those there when what will would more most other some such only over after ' +
  'before about both between because while where under upon very can could may must should shall one two three ' +
  'said says say made make out all any each own same still just yet per').split(' '));

const b36 = (n) => n.toString(36);

// word -> the entries that use it. Each line is "word id id id" with ids as gaps in base 36 so the
// file compresses well. Words in nearly every entry say nothing and are dropped.
export function buildWordIndex(data) {
  const postings = new Map();
  data.movements.forEach((m, i) => {
    const seen = new Set();
    for (const text of visibleText(m)) {
      for (const w of words(text)) {
        if (w.length < 3 || /\d/.test(w) || STOP.has(w) || seen.has(w)) continue;
        seen.add(w);
        let list = postings.get(w);
        if (!list) postings.set(w, (list = []));
        list.push(i);
      }
    }
  });
  const limit = Math.floor(data.movements.length * 0.4);
  const lines = [];
  for (const w of [...postings.keys()].sort()) {
    const ids = postings.get(w);
    if (ids.length > limit) continue;
    let prev = 0;
    lines.push(`${w} ${ids.map((id) => { const g = id - prev; prev = id; return b36(g); }).join(',')}`);
  }
  return { v: 1, n: data.movements.length, words: lines };
}

const gz = (text) => zlib.gzipSync(Buffer.from(text), { level: 9 }).length;

export function buildSearchIndex({ data, html, namesFile = readNamesFile(), budget = BUDGET }) {
  const names = buildNamesIndex(data, extractFamilies(html), namesFile);
  const words = buildWordIndex(data);
  const namesJson = JSON.stringify(names), wordsJson = JSON.stringify(words);
  const sizes = {
    namesBytes: Buffer.byteLength(namesJson), namesGzipBytes: gz(namesJson),
    wordsBytes: Buffer.byteLength(wordsJson), wordsGzipBytes: gz(wordsJson),
    wordCount: words.words.length, namesFilePresent: namesFile.present !== false && namesFile.rows.length > 0,
  };
  const over = [];
  if (sizes.namesGzipBytes > budget.namesGzipBytes) over.push(`names file ${sizes.namesGzipBytes} bytes compressed, budget ${budget.namesGzipBytes}`);
  if (sizes.wordsGzipBytes > budget.wordsGzipBytes) over.push(`word list ${sizes.wordsGzipBytes} bytes compressed, budget ${budget.wordsGzipBytes}`);
  if (over.length) throw new Error(`search index over budget: ${over.join('; ')}`);
  return { namesJson, wordsJson, sizes };
}

export function writeSearchIndex(result, outDir) {
  const dir = path.join(outDir, 'data', 'search');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'names.json'), result.namesJson);
  fs.writeFileSync(path.join(dir, 'words.json'), result.wordsJson);
}
