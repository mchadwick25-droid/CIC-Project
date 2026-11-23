import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import {
  BUDGET, TEXT_PATHS, visibleText, namesOf, extractFamilies, buildNamesIndex, buildWordIndex,
  buildSearchIndex, readNamesFile,
} from '../build_search_index.mjs';
import { findDataLiteral } from '../slim_map_data.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const { normalize, stem, words, withinOneTypo } = createRequire(import.meta.url)(path.join(ROOT, 'cft-website', 'search-core.js'));

const page = fs.readFileSync(path.join(ROOT, 'cft-website', 'index.html'), 'utf8');
const lit = findDataLiteral(page);
const DATA = JSON.parse(page.slice(lit.start, lit.end));
const FAMILIES = extractFamilies(page);

const small = {
  eras: [{ num: 1, title: 'The Early Church Era', academicName: null, dates: '70-312 CE' }],
  movements: [
    { id: 'a', name: 'Church of the East', shortName: 'Assyrian Church', informalName: 'The Eastern Church', start: 100, end: 900, era: 1, living: true, teaser: 'Missionaries crossed Persia along the Silk Road.' },
    { id: 'b', name: 'Saint Ephrem', kind: 'person', start: 306, end: 373, era: 2, card: { otherNames: ['Ephrem the Syrian', 'Mar Aphrem'], knownFor: 'A deacon who wrote hymns in Syriac.' } },
    { id: 'c', name: 'Council of Nicaea', kind: 'major-council', start: 325, end: 325, era: 2, council: { issue: ['The date of Easter'], decided: ['The Son and the Father share one substance.'] } },
  ],
};

test('normalize drops accents, case and punctuation, and treats St and Saint as one word', () => {
  assert.equal(normalize('Cyril of Alexandria’s'), 'cyril of alexandria');
  assert.equal(normalize('St. Ephrem'), 'saint ephrem');
  assert.equal(normalize('Saint  Ephrem'), 'saint ephrem');
  assert.equal(normalize('Théodore'), 'theodore');
  assert.equal(normalize('Nicene–Constantinopolitan'), 'nicene constantinopolitan');
  assert.equal(normalize('Wesleyan-Holiness'), 'wesleyan holiness');
  assert.equal(normalize(null), '');
});

test('a word in the middle of a longer word is not read as St', () => {
  assert.equal(normalize('first last'), 'first last');
  assert.equal(normalize('the East'), 'the east');
});

test('plurals and singulars share one stem; short words and numbers are left alone', () => {
  for (const [a, b] of [['churches', 'church'], ['bodies', 'body'], ['quakers', 'quaker'], ['councils', 'council'], ['traditions', 'tradition']]) {
    assert.equal(stem(a), stem(b), `${a} and ${b}`);
  }
  assert.equal(stem('gnosis'), 'gnosis');
  assert.equal(stem('christus'), 'christus');
  assert.equal(stem('1054'), '1054');
  assert.equal(stem('his'), 'his');
  assert.deepEqual(words('The Quakers’ meetings'), ['the', 'quaker', 'meeting']);
});

test('one-letter typos match and two do not', () => {
  assert.ok(withinOneTypo('nestorian', 'nestorain'));
  assert.ok(withinOneTypo('nestorian', 'nestorin'));
  assert.ok(withinOneTypo('nestorian', 'nestoriann'));
  assert.ok(withinOneTypo('nestorian', 'nestorlan'));
  assert.ok(!withinOneTypo('nestorian', 'nestrin'));
  assert.ok(!withinOneTypo('nestorian', 'nestorlin'));
  assert.ok(withinOneTypo('same', 'same'));
});

test('names of an entry: its own name, short name, everyday name and the other names on its card', () => {
  assert.deepEqual(namesOf(small.movements[0]), [
    ['church of the east', 'n'], ['assyrian church', 's'], ['the eastern church', 'e'],
  ]);
  assert.deepEqual(namesOf(small.movements[1]).map(([n, k]) => `${k}:${n}`), [
    'n:saint ephrem', 'o:ephrem the syrian', 'o:mar aphrem',
  ]);
});

test('visible text reads only the listed paths', () => {
  const m = { id: 'x', teaser: 'one', secretNote: 'hidden', card: { knownFor: 'two', quotationOriginals: [{ modern: 'three', printed: 'not shown' }] }, voices: ['four'] };
  assert.deepEqual(visibleText(m).sort(), ['four', 'one', 'three', 'two']);
});

test('every listed text path is found in the real data, so none has gone dead', () => {
  const dead = TEXT_PATHS.filter((p) => !DATA.movements.some((m) => visibleTextAt(m, p)));
  assert.deepEqual(dead, []);
});

function visibleTextAt(m, p) {
  const parts = p.split('.');
  let level = [m];
  for (const part of parts) {
    const list = part.endsWith('[]'), key = list ? part.slice(0, -2) : part;
    level = level.flatMap((v) => (v && v[key] != null ? (list ? (Array.isArray(v[key]) ? v[key] : []) : [v[key]]) : []));
  }
  return level.length > 0;
}

test('the names index lists every entry once by id and points each name at its entry', () => {
  const idx = buildNamesIndex(small, FAMILIES);
  assert.deepEqual(idx.entries, ['a', 'b', 'c']);
  assert.deepEqual(idx.living, [0]);
  const ephrem = idx.names.filter(([, i]) => i === 1).map(([n, , k]) => `${k}:${n}`).sort();
  assert.deepEqual(ephrem, ['n:saint ephrem', 'o:ephrem the syrian', 'o:mar aphrem']);
  assert.deepEqual(idx.names.map(([n]) => n), [...idx.names.map(([n]) => n)].sort());
  assert.deepEqual(idx.eras, [[1, 'The Early Church Era', '', '70-312 CE']]);
  assert.ok(idx.rivers.some(([, name]) => name === 'Latin West'));
});

test('sourced names join the index with their kind, for an entry or for a place', () => {
  const rows = [
    { name: 'Nestorians', entry: 'a', kind: 'name given by opponents', basis: {} },
    { name: 'Mar Ephrem', entry: 'b', kind: 'spelling', basis: {} },
    { name: 'Persia', country: 'Iran', kind: 'older name', basis: {} },
    { name: 'Asia Minor', region: 'Asia Minor', kind: 'older name', basis: {} },
  ];
  const idx = buildNamesIndex(small, FAMILIES, { rows });
  assert.ok(idx.names.some(([n, i, k]) => n === 'nestorians' && i === 0 && k === 'x'));
  assert.ok(idx.names.some(([n, i, k]) => n === 'mar ephrem' && i === 1 && k === 'p'));
  assert.deepEqual(idx.places, [['persia', 'c', 'Iran', 'l'], ['asia minor', 'r', 'Asia Minor', 'l']]);
});

test('a sourced row that points nowhere or has no known kind stops the build', () => {
  const bad = (row) => assert.throws(() => buildNamesIndex(small, FAMILIES, { rows: [row] }), /cannot place/);
  bad({ name: 'X', entry: 'nope', kind: 'spelling' });
  bad({ name: 'X', entry: 'a', kind: 'whim' });
  bad({ name: 'X', kind: 'spelling' });
  bad({ name: '', entry: 'a', kind: 'spelling' });
});

test('the build works with no names file, and reads either a list or an object with rows', () => {
  const missing = readNamesFile(path.join(ROOT, 'no', 'such', 'file.json'));
  assert.deepEqual(missing, { rows: [], present: false });
  const r = buildSearchIndex({ data: small, html: page, namesFile: missing });
  assert.equal(r.sizes.namesFilePresent, false);
  const tmp = path.join(ROOT, '.build', `names-${process.pid}.json`);
  fs.mkdirSync(path.dirname(tmp), { recursive: true });
  try {
    fs.writeFileSync(tmp, JSON.stringify([{ name: 'X', entry: 'a', kind: 'spelling' }]));
    assert.equal(readNamesFile(tmp).rows.length, 1);
    fs.writeFileSync(tmp, JSON.stringify({ rows: [{ name: 'X', entry: 'a', kind: 'spelling' }] }));
    assert.equal(readNamesFile(tmp).rows.length, 1);
    fs.writeFileSync(tmp, JSON.stringify({ nothing: 1 }));
    assert.throws(() => readNamesFile(tmp), /no list of rows/);
  } finally { fs.rmSync(tmp, { force: true }); }
});

function decode(index) {
  const out = new Map();
  for (const line of index.words) {
    const [w, gaps] = line.split(' ');
    let prev = 0;
    out.set(w, gaps.split(',').map((g) => (prev += parseInt(g, 36))));
  }
  return out;
}

test('the word list points each word at the entries that use it, and only the visible text counts', () => {
  const idx = decode(buildWordIndex({ movements: [...small.movements, { id: 'd', name: 'Hidden', teaser: 'Silk', notes: 'Persia secret' }, { id: 'e', name: 'Other', teaser: 'silk and hymns' }, { id: 'f', name: 'F', teaser: 'a' }, { id: 'g', name: 'G', teaser: 'b' }, { id: 'h', name: 'H', teaser: 'c' }, { id: 'i', name: 'I', teaser: 'd' }, { id: 'j', name: 'J', teaser: 'e' }] }));
  assert.deepEqual(idx.get('silk'), [0, 3, 4]);
  assert.deepEqual(idx.get('hymn'), [1, 4]);
  assert.ok(!idx.has('persia') || !idx.get('persia').includes(3));
  assert.ok(!idx.has('the'), 'a common word is left out');
  assert.ok(!idx.has('secret'), 'text outside the listed paths is not indexed');
});

test('a word in most entries is left out', () => {
  const movements = Array.from({ length: 10 }, (_, i) => ({ id: `m${i}`, name: `M${i}`, teaser: `bishop ${i < 2 ? 'rare' : ''}` }));
  const idx = decode(buildWordIndex({ movements }));
  assert.ok(!idx.has('bishop'));
  assert.deepEqual(idx.get('rare'), [0, 1]);
});

test('an index over its size budget fails the build and names the file', () => {
  const ok = buildSearchIndex({ data: small, html: page, namesFile: { rows: [] } });
  assert.ok(ok.sizes.namesGzipBytes > 0);
  assert.throws(() => buildSearchIndex({ data: small, html: page, namesFile: { rows: [] }, budget: { namesGzipBytes: 10, wordsGzipBytes: 1e6 } }), /over budget: names file/);
  assert.throws(() => buildSearchIndex({ data: small, html: page, namesFile: { rows: [] }, budget: { namesGzipBytes: 1e6, wordsGzipBytes: 10 } }), /over budget: word list/);
  assert.ok(BUDGET.namesGzipBytes < BUDGET.wordsGzipBytes);
});

test('the real tree builds inside the budget, every entry is in the names index and every name finds its entry', () => {
  const r = buildSearchIndex({ data: DATA, html: page });
  const names = JSON.parse(r.namesJson);
  assert.equal(names.entries.length, DATA.movements.length);
  assert.deepEqual(names.entries, DATA.movements.map((m) => m.id));
  const found = new Set(names.names.map(([, i]) => i));
  assert.equal(found.size, DATA.movements.length, 'an entry with no name in the index');
  assert.ok(names.names.some(([n]) => n === 'saint augustine' || n.includes('augustine')));
  assert.equal(names.rivers.length, FAMILIES.length);
  assert.deepEqual(names.living.map((i) => DATA.movements[i].id), DATA.movements.filter((m) => m.living).map((m) => m.id));
  assert.ok(names.living.length > 5, 'the census marks some entries as living');
  assert.equal(names.eras.length, DATA.eras.length);
  assert.ok(r.sizes.namesGzipBytes <= BUDGET.namesGzipBytes);
  assert.ok(r.sizes.wordsGzipBytes <= BUDGET.wordsGzipBytes);
  const word = decode(JSON.parse(r.wordsJson));
  assert.ok(word.size > 10000);
  const heaven = word.get('heaven');
  assert.ok(heaven && heaven.length > 3 && heaven.every((i) => i >= 0 && i < DATA.movements.length));
});
