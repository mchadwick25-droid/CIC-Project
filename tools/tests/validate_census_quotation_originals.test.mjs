// A person card's quotationOriginals and briefReferences: the printed wording behind each quotation the brief gives
// in our modern English, and the references the brief draws on (Decision-Log 2026-11-16, release 48).
// Run: node --test tools/tests/validate_census_quotation_originals.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const ID = "athanasius-of-alexandria";

function errorsFor(change) {
  const c = structuredClone(census);
  change(c.movements.find(m => m.id === ID).card, c.movements.find(m => m.id === ID));
  const dir = mkdtempSync(join(tmpdir(), "census-originals-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify(c));
  const run = spawnSync("node", ["tools/validate-census.mjs", "--skip-quotes", path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR"));
}

test("the published cards pass", () => {
  assert.deepEqual(errorsFor(() => {}), []);
});

test("a printed wording that is not in its lines fails", () => {
  const errs = errorsFor(card => { card.quotationOriginals[0].printed = "words the file does not hold"; });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /does not stand in/);
});

test("lines outside the file fail", () => {
  const errs = errorsFor(card => { card.quotationOriginals[0].lines = "9999998-9999999"; });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /must be a line or range inside/);
});

test("a file the card does not cite fails", () => {
  const errs = errorsFor(card => { card.quotationOriginals[0].file = "cic/texts/benedict_rule-of-saint-benedict_gasquet1925.txt"; card.quotationOriginals[0].lines = "1"; });
  assert.ok(errs.some(e => /is not among the files the card cites/.test(e)));
});

test("a modern wording the brief does not quote fails", () => {
  const errs = errorsFor(card => { card.quotationOriginals[0].modern = "Words the brief never quotes."; });
  assert.ok(errs.some(e => /is not a quotation in the brief/.test(e)));
  assert.ok(errs.some(e => /has no entry in card.quotationOriginals/.test(e)));
});

test("a brief quotation with no entry fails", () => {
  const errs = errorsFor(card => { card.quotationOriginals.pop(); });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /has no entry in card.quotationOriginals/);
});

test("a second reading outside the three verdicts fails", () => {
  const errs = errorsFor(card => { card.quotationOriginals[0].secondReading = "close"; });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /secondReading/);
});

test("an unknown field fails", () => {
  const errs = errorsFor(card => { card.quotationOriginals[0].note = "a process note"; });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /is not allowed/);
});

test("an empty reference fails", () => {
  const errs = errorsFor(card => { card.briefReferences.push(""); });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /briefReferences/);
});
