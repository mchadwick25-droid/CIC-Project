// The optional person card: shape, size limits and the files it points at.
// Run: node --test tools/tests/validate_census_card.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const PERSON = "tertullian-s-voice";
const HOME = "latin-apologists";
const FILE = "cic/texts/AUTHORS.md";
const card = () => ({
  knownFor: "A writer in Latin.",
  role: "Writer",
  keyWorks: [{ title: "Apology", about: "a defence of Christians" }],
  legacy: { traces: ["Cyprian called him the master."], remembered: ["Later writers cited him."] },
  uncertain: ["The date of his death is not known."],
  sources: {
    ownWords: [{ title: "Apology", file: FILE, language: "Latin", disputed: "authorship disputed" }],
    about: [{ title: "On Illustrious Men", author: "Jerome", date: null, language: "English translation", file: FILE }],
  },
});

function errorsFor(change) {
  const c = structuredClone(census);
  change(c, id => c.movements.find(m => m.id === id));
  const dir = mkdtempSync(join(tmpdir(), "census-card-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify(c));
  const run = spawnSync("node", ["tools/validate-census.mjs", "--skip-quotes", path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR"));
}

test("a valid card passes", () => {
  assert.deepEqual(errorsFor((c, m) => { m(PERSON).card = card(); }), []);
});

test("a card with only some fields passes", () => {
  assert.deepEqual(errorsFor((c, m) => { m(PERSON).card = { knownFor: "A writer in Latin." }; }), []);
  assert.deepEqual(errorsFor((c, m) => { m(PERSON).card = { sources: { about: card().sources.about } }; }), []);
});

test("a card on a movement fails", () => {
  assert.equal(errorsFor((c, m) => { m(HOME).card = card(); }).length, 1);
});

test("an unknown key fails", () => {
  assert.equal(errorsFor((c, m) => { m(PERSON).card = { ...card(), mood: "calm" }; }).length, 1);
  assert.equal(errorsFor((c, m) => { const k = card(); k.legacy.extra = []; m(PERSON).card = k; }).length, 1);
});

test("four key works fail", () => {
  assert.equal(errorsFor((c, m) => { const k = card(); k.keyWorks = Array(4).fill(k.keyWorks[0]); m(PERSON).card = k; }).length, 1);
});

test("a missing file fails, and so does a file outside cic/texts/", () => {
  assert.equal(errorsFor((c, m) => { const k = card(); k.sources.ownWords[0].file = "cic/texts/no-such-file.txt"; m(PERSON).card = k; }).length, 1);
  assert.equal(errorsFor((c, m) => { const k = card(); k.sources.about[0].file = "README.md"; m(PERSON).card = k; }).length, 1);
});

test("an empty string fails", () => {
  assert.equal(errorsFor((c, m) => { const k = card(); k.knownFor = "  "; m(PERSON).card = k; }).length, 1);
  assert.equal(errorsFor((c, m) => { const k = card(); k.legacy.traces = [""]; m(PERSON).card = k; }).length, 1);
  assert.equal(errorsFor((c, m) => { const k = card(); k.sources.ownWords[0].disputed = ""; m(PERSON).card = k; }).length, 1);
});

test("a source needs its title, language and author, and a date that is a string or null", () => {
  assert.equal(errorsFor((c, m) => { const k = card(); delete k.sources.ownWords[0].language; m(PERSON).card = k; }).length, 1);
  assert.equal(errorsFor((c, m) => { const k = card(); delete k.sources.about[0].author; m(PERSON).card = k; }).length, 1);
  assert.deepEqual(errorsFor((c, m) => { const k = card(); k.sources.about[0].author = null; m(PERSON).card = k; }), []);
  assert.equal(errorsFor((c, m) => { const k = card(); k.sources.about[0].date = 553; m(PERSON).card = k; }).length, 1);
  assert.equal(errorsFor((c, m) => { const k = card(); delete k.keyWorks[0].about; m(PERSON).card = k; }).length, 1);
});
