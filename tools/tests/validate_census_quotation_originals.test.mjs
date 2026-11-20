// A person card's or council's quotationOriginals and briefReferences, and a council story's: the printed wording behind
// each quotation the brief or story gives in our modern English, and the references it draws on (Decision-Log
// 2026-11-16, release 48; 2026-11-17, release 50).
// Run: node --test tools/tests/validate_census_quotation_originals.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const ID = "athanasius-of-alexandria";

function errorsFor(change, id = ID) {
  const c = structuredClone(census);
  const m = c.movements.find(x => x.id === id);
  change(m.card ?? m.council, m);
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
  assert.ok(errs.some(e => /is not among the files the entry cites/.test(e)));
});

test("a modern wording the brief does not quote fails", () => {
  const errs = errorsFor(card => { card.quotationOriginals[0].modern = "Words the brief never quotes."; });
  assert.ok(errs.some(e => /is not a quotation in the brief/.test(e)));
  assert.ok(errs.some(e => /card\.quotationOriginals: the quotation .* has no entry/.test(e)));
});

test("a brief quotation with no entry fails", () => {
  const errs = errorsFor(card => { card.quotationOriginals.pop(); });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /card\.quotationOriginals: the quotation .* has no entry/);
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

test("a quotation with no named work fails", () => {
  const errs = errorsFor(card => { delete card.quotationOriginals[0].work; });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /\.work must be a non-empty string/);
});

const NICAEA = "council-of-nicaea-325";

test("a council's quotations and its story's are checked like a card's", () => {
  assert.deepEqual(errorsFor(() => {}, NICAEA), []);
  const council = errorsFor(co => { co.quotationOriginals[0].printed = "words the file does not hold"; }, NICAEA);
  assert.equal(council.length, 1);
  assert.match(council[0], /council\.quotationOriginals\[0\]\.printed .*does not stand in/);
  const story = errorsFor((co, m) => { m.documentedStories[0].quotationOriginals.pop(); }, NICAEA);
  assert.ok(story.length >= 1);
  story.forEach(e => assert.match(e, /documentedStories\[0\]\.quotationOriginals: the quotation .* has no entry/));
});

test("a council's how-it-worked lines must be non-empty strings", () => {
  const errs = errorsFor(co => { co.howItWorked.push(""); }, NICAEA);
  assert.equal(errs.length, 1);
  assert.match(errs[0], /council\.howItWorked\[\d+\] must be a non-empty string/);
});

test("an original beside a translation must stand in its own lines, with all three fields", () => {
  const withOriginal = (co, f) => { const q = co.quotationOriginals.find(e => e.originalFile ?? e.englishFile); f(q); };
  const wrong = errorsFor(card => withOriginal(card, q => { if (q.original) q.original = "verba quae non sunt"; else q.englishPrinted = "words the file does not hold"; }), "martin-of-tours");
  assert.equal(wrong.length, 1);
  assert.match(wrong[0], /does not stand in/);
  const partial = errorsFor(card => withOriginal(card, q => { delete q.originalLines; }), "martin-of-tours");
  assert.equal(partial.length, 1);
  assert.match(partial[0], /go together/);
});

test("one entry covers a quotation the brief breaks around \"he says\"", () => {
  const errs = errorsFor((card, m) => {
    m.longDescription += ' He wrote, "Words the brief never quoted," he said, "until now."';
    card.quotationOriginals.push({ ...card.quotationOriginals[0], modern: "Words the brief never quoted, until now." });
  });
  assert.ok(!errs.some(e => /has no entry|is not a quotation in the brief/.test(e)), errs.join("\n"));
});

test("a Greek original is compared letter by letter, accents and letter forms aside", () => {
  const original = (card, words) => { card.quotationOriginals.find(e => e.originalLines === "680").original = words; };
  assert.deepEqual(errorsFor(card => original(card, "Το θελημα του θεου γενεσθω."), "polycarp-of-smyrna"), []);
  const wrong = errorsFor(card => original(card, "Τὸ ϑέλημα τοῦ ἀνθρώπου γενέσθω."), "polycarp-of-smyrna");
  assert.equal(wrong.length, 1);
  assert.match(wrong[0], /card\.quotationOriginals\[\d+\]\.original .*does not stand in/);
});
