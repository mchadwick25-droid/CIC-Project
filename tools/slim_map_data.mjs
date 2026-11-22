import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const MARKER = 'const DATA = ';
const SLIM_FLAG = ['const SLIM_MAP = false;', 'const SLIM_MAP = true;'];

export function findDataLiteral(html) {
  const at = html.indexOf(MARKER);
  if (at < 0) throw new Error('the page has no "const DATA = " literal');
  const start = at + MARKER.length;
  let depth = 0, inString = false, escaped = false;
  for (let i = start; i < html.length; i++) {
    const c = html[i];
    if (inString) {
      if (escaped) escaped = false;
      else if (c === '\\') escaped = true;
      else if (c === '"') inString = false;
      continue;
    }
    if (c === '"') inString = true;
    else if (c === '{' || c === '[') depth++;
    else if (c === '}' || c === ']') {
      depth--;
      if (depth === 0) return { start, end: i + 1 };
    }
  }
  throw new Error('the data literal never closes');
}

// A list of dotted paths ("documentedStories[].title") becomes a tree: true keeps a whole value,
// an object keeps only the named parts. Arrays take the spec of their elements.
export function buildSpec(paths) {
  const spec = {};
  for (const p of paths) {
    const parts = p.split('.').map((s) => s.replace(/\[\]$/, ''));
    let node = spec;
    parts.forEach((part, i) => {
      if (i === parts.length - 1) {
        if (node[part] && node[part] !== true) throw new Error(`"${p}" is both a leaf and a parent`);
        node[part] = true;
      } else {
        if (node[part] === true) throw new Error(`"${p}" sits under a path kept whole`);
        node[part] = node[part] || {};
        node = node[part];
      }
    });
  }
  return spec;
}

const isObject = (v) => v !== null && typeof v === 'object' && !Array.isArray(v);

// Returns [slim, rest]: what the map needs to start, and everything else, with the same shape so
// that merge(slim, rest) gives the original back. undefined means "nothing on this side".
export function split(value, spec) {
  if (spec === true) return [value, undefined];
  if (!spec) return [undefined, value];
  if (Array.isArray(value)) {
    const slim = [], rest = [];
    let anyRest = false;
    for (const el of value) {
      const [s, r] = split(el, spec);
      slim.push(s === undefined ? {} : s);
      rest.push(r === undefined ? {} : r);
      if (r !== undefined && !(isObject(r) && Object.keys(r).length === 0)) anyRest = true;
    }
    return [slim, anyRest ? rest : undefined];
  }
  if (isObject(value)) {
    const slim = {}, rest = {};
    for (const [k, v] of Object.entries(value)) {
      const [s, r] = split(v, spec[k]);
      if (s !== undefined) slim[k] = s;
      if (r !== undefined) rest[k] = r;
    }
    return [slim, Object.keys(rest).length ? rest : undefined];
  }
  return [undefined, value];
}

export function merge(slim, rest) {
  if (rest === undefined) return slim;
  if (slim === undefined) return rest;
  if (Array.isArray(slim) && Array.isArray(rest)) return slim.map((s, i) => merge(s, rest[i]));
  if (isObject(slim) && isObject(rest)) {
    const out = { ...slim };
    for (const [k, v] of Object.entries(rest)) out[k] = merge(slim[k], v);
    return out;
  }
  throw new Error('cannot merge values of different shapes');
}

const sha256 = (text) => crypto.createHash('sha256').update(text, 'utf8').digest('hex');

export function loadConfig(file = path.join(ROOT, 'tools', 'slim_map_fields.json')) {
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

// Splits the page's embedded data into a small starting copy and the rest. Returns the slim page,
// one "rest" object per movement (keyed by id), and one per link (keyed by link id).
export function slimMap(html, config = loadConfig()) {
  const { start, end } = findDataLiteral(html);
  const data = JSON.parse(html.slice(start, end));
  const slimData = {};
  const entries = {};
  const edgesDetail = {};
  const moveSpec = buildSpec(config.movements.keep);
  const edgeSpec = buildSpec(config.edges.keep);
  const hashes = Object.entries(config.movements.hash || {});
  for (const [key, value] of Object.entries(data)) {
    if (config.wholeSections.includes(key)) slimData[key] = value;
    else if (key === 'movements') {
      slimData.movements = value.map((m) => {
        if (typeof m.id !== 'string') throw new Error('a movement has no id');
        const [s, r] = split(m, moveSpec);
        for (const [to, from] of hashes) if (typeof m[from] === 'string') s[to] = sha256(m[from]);
        entries[m.id] = { id: m.id, ...(r || {}) };
        return s;
      });
    } else if (key === 'edges') {
      slimData.edges = value.map((e) => {
        if (typeof e.id !== 'string') throw new Error('a link has no id');
        const [s, r] = split(e, edgeSpec);
        if (r !== undefined) edgesDetail[e.id] = r;
        return s;
      });
    } else throw new Error(`"${key}" is in the data but in none of the field lists`);
  }
  if (html.split(SLIM_FLAG[0]).length !== 2) throw new Error(`the page must hold "${SLIM_FLAG[0]}" exactly once`);
  const slimHtml = (html.slice(0, start) + JSON.stringify(slimData) + html.slice(end)).replace(SLIM_FLAG[0], SLIM_FLAG[1]);
  return { html: slimHtml, entries, edgesDetail, data, slimData };
}

// Puts the original data back together from the three parts (the check that nothing is lost).
export function rebuild(slimData, entries, edgesDetail, config = loadConfig()) {
  const hashKeys = Object.keys(config.movements.hash || {});
  const out = { ...slimData };
  out.movements = slimData.movements.map((s) => {
    const base = { ...s };
    for (const k of hashKeys) delete base[k];
    const { id, ...rest } = entries[s.id];
    return merge(base, Object.keys(rest).length ? rest : undefined);
  });
  out.edges = slimData.edges.map((e) => merge(e, edgesDetail[e.id]));
  return out;
}

function stats(result) {
  const gz = (s) => zlib.gzipSync(Buffer.from(s), { level: 9 }).length;
  const sizes = Object.values(result.entries).map((e) => Buffer.byteLength(JSON.stringify(e))).sort((a, b) => a - b);
  const detail = JSON.stringify(result.edgesDetail);
  return {
    pageBytes: Buffer.byteLength(result.html),
    pageGzipBytes: gz(result.html),
    entryCount: sizes.length,
    entryMedianBytes: sizes[Math.floor(sizes.length / 2)],
    entryMaxBytes: sizes[sizes.length - 1],
    edgesDetailBytes: Buffer.byteLength(detail),
    edgesDetailGzipBytes: gz(detail),
  };
}

// Writes the slim page and its data files into outDir. With clean, the directory is emptied first.
export function writeSlimMap(result, outDir, clean = true) {
  if (clean) fs.rmSync(outDir, { recursive: true, force: true });
  fs.mkdirSync(path.join(outDir, 'data', 'entries'), { recursive: true });
  fs.writeFileSync(path.join(outDir, 'index.html'), result.html);
  for (const [id, entry] of Object.entries(result.entries)) {
    fs.writeFileSync(path.join(outDir, 'data', 'entries', `${id}.json`), JSON.stringify(entry));
  }
  fs.writeFileSync(path.join(outDir, 'data', 'edges-detail.json'), JSON.stringify(result.edgesDetail));
}

function main() {
  const outDir = path.resolve(ROOT, process.argv[2] || '.build/tree-slim');
  const html = fs.readFileSync(path.join(ROOT, 'cft-website', 'index.html'), 'utf8');
  const result = slimMap(html);
  writeSlimMap(result, outDir);
  const s = stats(result);
  console.log(`slim map: page ${(s.pageBytes / 1e6).toFixed(2)} MB (${(s.pageGzipBytes / 1e6).toFixed(2)} MB compressed), ` +
    `${s.entryCount} entry files (median ${(s.entryMedianBytes / 1e3).toFixed(1)} KB, largest ${(s.entryMaxBytes / 1e3).toFixed(1)} KB), ` +
    `link details ${(s.edgesDetailBytes / 1e6).toFixed(2)} MB (${(s.edgesDetailGzipBytes / 1e6).toFixed(2)} MB compressed), in ${path.relative(ROOT, outDir)}/`);
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main();
