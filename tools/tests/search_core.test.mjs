import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { buildNamesIndex, buildWordIndex, extractFamilies } from '../build_search_index.mjs';
import { findDataLiteral } from '../slim_map_data.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const S = createRequire(import.meta.url)(path.join(ROOT, 'cft-website', 'search-core.js'));
const page = fs.readFileSync(path.join(ROOT, 'cft-website', 'index.html'), 'utf8');
const lit = findDataLiteral(page);
const DATA = JSON.parse(page.slice(lit.start, lit.end));
const FAMILIES = extractFamilies(page);

const data = {
  eras: [
    { num: 1, title: 'The Early Church Era', academicName: 'The Ante-Nicene Period', dates: '70-312 CE' },
    { num: 2, title: 'The Imperial Church Era', academicName: null, dates: '312-451 CE' },
    { num: 5, title: 'The High Medieval Era', academicName: null, dates: '1054-1300' },
  ],
  movements: [
    { id: 'east', name: 'Church of the East', shortName: 'Assyrian Church', start: 424, end: 651, living: true, modernCountries: [{ country: 'Iran' }, { country: 'Iraq' }], placeLabel: 'Persia · Mesopotamia' },
    { id: 'ephrem', name: 'Saint Ephrem', kind: 'person', start: 306, end: 373, modernCountries: [{ country: 'Turkey' }], placeLabel: 'Nisibis', card: { otherNames: ['Ephrem the Syrian'] } },
    { id: 'baptist', name: 'Baptists', start: 1609, end: 2010, living: true, modernCountries: [{ country: 'United States' }] },
    { id: 'quaker', name: 'Quakers', informalName: 'Friends', start: 1650, end: 2010, living: true, modernCountries: [{ country: 'United Kingdom' }] },
    { id: 'nicaea', name: 'Council of Nicaea', kind: 'major-council', start: 325, end: 325, modernCountries: [{ country: 'Turkey' }] },
    { id: 'schism', name: 'The Great Schism', start: 1054, end: 1054 },
  ],
};
const rows = [
  { name: 'Nestorians', entry: 'east', kind: 'name given by opponents' },
  { name: 'Persia', country: 'Iran', kind: 'older name' },
  { name: 'Mesopotamia', region: 'Mesopotamia', kind: 'older name' },
];
function make(d = data, r = rows, withWords = false) {
  const index = buildNamesIndex(d, FAMILIES, { rows: r });
  const info = index.entries.map((id) => {
    const m = d.movements.find((x) => x.id === id);
    return {
      id, name: m.name, short: m.shortName || '', kind: m.kind === 'person' ? 'p' : m.kind === 'major-council' ? 'c' : 't',
      start: m.start, end: m.end, living: !!m.living, countries: [...new Set((m.modernCountries || []).map((c) => c.country))], place: m.placeLabel || '',
    };
  });
  return S.createSearcher(index, info, withWords ? S.decodeWordList(buildWordIndex(d)) : null);
}
const found = (r, d = data) => r.entries.map((h) => d.movements[h.i].id);

test('a name matches exactly first, then by its start, then by a word in it', () => {
  const s = make();
  const r = s.search('baptists');
  assert.equal(found(r)[0], 'baptist');
  assert.equal(r.entries[0].rank, 0);
  assert.deepEqual(found(s.search('church of')), ['east']);
  assert.deepEqual(found(s.search('schism')), ['schism']);
});

test('plurals, accents, "St" and "Saint", and hyphens find the same entry', () => {
  const s = make();
  assert.deepEqual(found(s.search('baptist')), ['baptist']);
  assert.deepEqual(found(s.search('Quaker')), ['quaker']);
  assert.deepEqual(found(s.search('St Ephrem')), ['ephrem']);
  assert.deepEqual(found(s.search('saint ephrem')), ['ephrem']);
  assert.deepEqual(found(s.search('Ephrem the Syrian')), ['ephrem']);
  assert.deepEqual(found(s.search('Ephrém')), ['ephrem']);
});

test('one-letter typos find the entry, two do not', () => {
  const s = make();
  assert.deepEqual(found(s.search('baptits')), ['baptist']);
  assert.deepEqual(found(s.search('quakers')), ['quaker']);
  assert.deepEqual(found(s.search('nestorain')), ['east']);
  assert.deepEqual(found(s.search('nestrian')), ['east'], 'one letter dropped');
  assert.deepEqual(found(s.search('nstrian')), [], 'two letters dropped');
});

test('a sourced name keeps its kind, so the screen can say who gave it', () => {
  const s = make();
  const hit = s.search('Nestorians').entries[0];
  assert.equal(hit.via, 'x');
  assert.equal(S.NAME_NOTE[hit.via], 'a name its opponents gave it');
  assert.equal(S.NAME_NOTE.l, 'an older name');
});

test('a country finds the entries that list it, and an older name finds the country', () => {
  const s = make();
  const iran = s.search('Iran').places[0];
  assert.equal(iran.label, 'Iran');
  assert.deepEqual(iran.ids.map((i) => data.movements[i].id), ['east']);
  const old = s.search('Persia').places[0];
  assert.equal(old.label, 'Iran');
  assert.equal(old.note, 'an older name');
  const region = s.search('Mesopotamia').places.find((p) => p.type === 'region');
  assert.deepEqual(region.ids.map((i) => data.movements[i].id), ['east']);
  assert.deepEqual(s.search('Turkey').places[0].ids.map((i) => data.movements[i].id), ['ephrem', 'nicaea']);
});

test('dates: a year, a range, a century, AD and CE, c.', () => {
  assert.deepEqual(S.parseDate('1054'), { type: 'year', a: 1054, b: 1054 });
  assert.deepEqual(S.parseDate('1054 AD'), { type: 'year', a: 1054, b: 1054 });
  assert.deepEqual(S.parseDate('AD 1054'), { type: 'year', a: 1054, b: 1054 });
  assert.deepEqual(S.parseDate('c. 325 CE'), { type: 'year', a: 325, b: 325 });
  assert.deepEqual(S.parseDate('300-400'), { type: 'range', a: 300, b: 400 });
  assert.deepEqual(S.parseDate('300 to 400'), { type: 'range', a: 300, b: 400 });
  assert.deepEqual(S.parseDate('11th century'), { type: 'century', a: 1001, b: 1100, n: 11 });
  assert.deepEqual(S.parseDate('4th century AD'), { type: 'century', a: 301, b: 400, n: 4 });
  assert.equal(S.parseDate('baptist'), null);
  assert.equal(S.parseDate('400-300'), null);
  const s = make();
  const r = s.search('1054');
  assert.deepEqual(r.date.ids.map((i) => data.movements[i].id), ['schism']);
  assert.equal(r.parts[0].label, 'The High Medieval Era');
  const cent = s.search('4th century');
  assert.deepEqual(cent.date.ids.map((i) => data.movements[i].id).sort(), ['ephrem', 'nicaea']);
  assert.equal(s.search('1700 to 1800').date.ids.length, 2);
});

test('an era and a river are found by name, and by the common name a river carries', () => {
  const s = make();
  assert.deepEqual(s.search('Early Church').parts.map((p) => p.label), ['The Early Church Era']);
  assert.ok(s.search('Orthodox').parts.some((p) => p.type === 'river' && p.label === 'Greek East'));
  assert.ok(s.search('era 2').parts.some((p) => p.label === 'The Imperial Church Era'));
});

test('a question also finds the person named in it, and says it is a question', () => {
  const s = make();
  const r = s.search('what does Ephrem say about heaven');
  assert.equal(r.question, true);
  assert.deepEqual(found(r), ['ephrem']);
  assert.equal(s.search('Ephrem').question, false);
});

test('a miss names the nearest name that starts the same way', () => {
  const s = make();
  const r = s.search('baptiser');
  assert.equal(r.entries.length, 0);
  assert.equal(r.nearest, 'Baptists');
  assert.equal(s.search('qqq').nearest, null);
});

const wordData = {
  movements: [
    { id: 'a', name: 'A', teaser: 'Origen taught that heaven was a school for souls. He wrote widely.' },
    { id: 'b', name: 'B', teaser: 'Heaven is the hope of the faithful.' },
    { id: 'c', name: 'C', teaser: 'Origen lived at Alexandria.' },
    { id: 'd', name: 'D', teaser: 'x' }, { id: 'e', name: 'E', teaser: 'y' }, { id: 'f', name: 'F', teaser: 'z' },
  ],
};

test('the text search keeps entries that use every word of the question; question words do not count', () => {
  const map = S.decodeWordList(buildWordIndex(wordData));
  const r = S.searchWords(map, 'what does Origen say about heaven');
  assert.deepEqual(r.shown, ['origen', 'heaven']);
  assert.deepEqual(r.ids, [0]);
  assert.deepEqual(S.searchWords(map, 'heavens').ids, [0, 1]);
  assert.deepEqual(S.searchWords(map, 'orange heaven').ids, [], 'a word no entry uses leaves nothing');
  assert.deepEqual(S.searchWords(map, 'origin heaven').ids, [0], 'a one-letter typo still finds it');
  assert.deepEqual(S.searchWords(map, 'origen heaven purgatory').missing, ['purgatory']);
  assert.deepEqual(S.searchWords(map, 'what does it say').ids, []);
});

test('the sentence shown is one sentence of the source, copied whole', () => {
  const texts = wordData.movements[0].teaser;
  const s = S.bestSentence([texts], ['origen', 'heaven']);
  assert.equal(s, 'Origen taught that heaven was a school for souls.');
  assert.equal(S.bestSentence(['Nothing here.'], ['origen']), null);
});

test('on the real tree, every sentence shown equals a sentence in the entry’s own text', () => {
  let checked = 0;
  for (const m of DATA.movements) {
    const texts = S.visibleText(m);
    if (!texts.length) continue;
    const tokens = S.words(texts[0]).filter((w) => w.length >= 5).slice(1, 3);
    if (!tokens.length) continue;
    const sentence = S.bestSentence(texts, tokens);
    if (sentence == null) continue;
    checked++;
    const source = texts.flatMap((t) => t.split(/(?<=[.!?])\s+/).map((x) => x.trim()));
    assert.ok(source.includes(sentence), `${m.id}: "${sentence.slice(0, 60)}"`);
    assert.ok(texts.some((t) => t.includes(sentence)), `${m.id}: not a verbatim part of the text`);
  }
  assert.ok(checked > 300, `only ${checked} entries checked`);
});

test('on the real tree the headline searches find what they should', () => {
  const index = buildNamesIndex(DATA, FAMILIES, { rows: [] });
  const info = index.entries.map((id) => {
    const m = DATA.movements.find((x) => x.id === id);
    return { id, name: m.name, short: m.shortName || '', kind: m.kind === 'person' ? 'p' : m.kind === 'major-council' ? 'c' : 't', start: m.start, end: m.end, living: !!m.living, countries: [...new Set((m.modernCountries || []).map((c) => c.country))], place: m.placeLabel || '' };
  });
  const map = S.decodeWordList(buildWordIndex(DATA));
  const s = S.createSearcher(index, info, map);
  const eth = s.search('Ethiopia');
  assert.ok(eth.places.some((p) => p.label === 'Ethiopia' && p.ids.length > 3));
  assert.ok(s.search('1054').date.ids.length > 5);
  assert.ok(s.search('origen').entries.some((h) => info[h.i].id === 'origen'));
  assert.ok(s.search('Origin').entries.some((h) => info[h.i].id === 'origen'), 'a one-letter typo reaches Origen');
  assert.equal(s.search('nestorian').entries.length, 0, 'until the names batch, the tree holds no such name');
  const text = s.searchWords('what does origen say about heaven');
  assert.deepEqual(text.shown, ['origen', 'heaven']);
});
