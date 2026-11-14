// Major councils, the new card keys and the quotation check.
// Run: node --test tools/tests/validate_census_council.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const COUNCIL = "council-of-nicaea-325";
const PERSON = "arius";

function errorsFor(change, flags = ["--skip-quotes"]) {
  const c = structuredClone(census);
  change(c, id => c.movements.find(m => m.id === id));
  const dir = mkdtempSync(join(tmpdir(), "census-council-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify(c));
  const run = spawnSync("node", ["tools/validate-census.mjs", ...flags, path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR"));
}

test("the census's own councils and people pass", () => {
  assert.deepEqual(errorsFor(() => {}), []);
});

test("a major council has its own kind", () => {
  assert.equal(census.movements.find(m => m.id === COUNCIL).kind, "major-council");
});

test("a council object on a movement or a person fails", () => {
  assert.equal(errorsFor((c, m) => { m("donatism").council = m(COUNCIL).council; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(PERSON).council = m(COUNCIL).council; }).length, 1);
});

test("a council with an unknown key, river, part or witness kind fails", () => {
  assert.equal(errorsFor((c, m) => { m(COUNCIL).council.mood = "calm"; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).council.rivers = ["Atlantis"]; }).length >= 1, true);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).council.traditions[0].part = "Visited"; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).council.record[0].kind = "rumour"; }).length, 1);
});

test("a council tradition must be an entry of the tree and carry its name", () => {
  assert.equal(errorsFor((c, m) => { m(COUNCIL).council.traditions[0].id = "no-such-entry"; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).council.traditions[0].name = "Some other name"; }).length, 1);
});

test("a council's first river must be its lane", () => {
  assert.equal(errorsFor((c, m) => { m(COUNCIL).laneOrder = 4; }).length, 1);
});

test("a council's people: entries, named lines and their verdicts", () => {
  assert.equal(errorsFor((c, m) => { m(COUNCIL).people.push({ name: "Someone Unscored", verdict: "NOT SCORED", part: "Sat in the hall" }); }).length, 0);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).people.push({ name: "Someone", verdict: "MAYBE", part: "Sat" }); }).length, 1);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).people.push({ person: "donatism", part: "Sat" }); }).length, 1);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).people.push({ person: PERSON, part: "Again" }); }).length, 1);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).people.push({ name: "Arius", verdict: "WHO", part: "Has an entry" }); }).length, 1);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).people.push({ person: PERSON }); }).length >= 1, true);
});

test("a person listed in a council may be told within another tradition", () => {
  const who = census.movements.find(m => m.id === PERSON);
  assert.notEqual(who.toldWithin, COUNCIL);
  assert.deepEqual(errorsFor(() => {}), []);
});

test("a person cannot be told within a council", () => {
  assert.equal(errorsFor((c, m) => { m(PERSON).toldWithin = COUNCIL; }).length >= 1, true);
});

test("the new card keys pass, and a bad label or list fails", () => {
  assert.deepEqual(errorsFor((c, m) => { m(PERSON).card.label = "Outside witness"; m(PERSON).card.otherNames = ["Areios"]; }), []);
  assert.equal(errorsFor((c, m) => { m(PERSON).card.label = "Famous"; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(PERSON).card.otherNames = "Areios"; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(PERSON).card.datesNote = ""; }).length, 1);
});

test("a made-up quotation fails the check against the cited files", () => {
  const errs = errorsFor((c, m) => { m(PERSON).longDescription += '\n\nHe said "this sentence is in no held book anywhere at all."'; }, []);
  assert.equal(errs.length, 1);
  assert.match(errs[0], /quotation not found verbatim/);
});
