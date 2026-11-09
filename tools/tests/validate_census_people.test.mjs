// Entry kinds, people, links that concern a person, descent grade and review status
// (Decision-Log 2026-11-06 rulings 14, 15 and 18; 2026-11-09, "The gap sweep ruled").
// Run: node --test tools/tests/validate_census_people.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const PERSON = "tertullian-s-voice";
const HOME = "latin-apologists";

function errorsFor(change) {
  const c = structuredClone(census);
  change(c, id => c.movements.find(m => m.id === id));
  const dir = mkdtempSync(join(tmpdir(), "census-people-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify(c));
  const run = spawnSync("node", ["tools/validate-census.mjs", path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR"));
}

test("the published census passes", () => {
  assert.deepEqual(errorsFor(() => {}), []);
});

test("a kind outside the set fails", () => {
  assert.equal(errorsFor((c, m) => { m(HOME).kind = "school"; }).length, 1);
});

test("a person entry needs toldWithin", () => {
  assert.equal(errorsFor((c, m) => { delete m(PERSON).toldWithin; }).length, 2);
});

test("a person may be told within no tradition", () => {
  assert.deepEqual(errorsFor((c, m) => { m(PERSON).toldWithin = null; m(HOME).people = []; }), []);
});

test("toldWithin must name a movement that lists the person", () => {
  assert.equal(errorsFor((c, m) => { m(PERSON).toldWithin = "no-such-movement"; }).length, 2);
  assert.equal(errorsFor((c, m) => { m(HOME).people = []; }).length, 1);
});

test("toldWithin is only for a person entry", () => {
  assert.equal(errorsFor((c, m) => { m(HOME).toldWithin = null; }).length, 1);
});

test("every movement has a people list and every entry a review status", () => {
  assert.equal(errorsFor((c, m) => { delete m(HOME).people; }).length, 2);
  assert.equal(errorsFor((c, m) => { m(HOME).reviewStatus = "checked"; }).length, 1);
});

test("a named voice must be named in its voices line and backed by the Library", () => {
  const voice = (c, m, extra) => { const h = m(HOME); h.people = [{ person: PERSON }, { name: "Lactantius", year: 303, voice: h.voices.findIndex(v => v.includes("Lactantius")), ...extra }]; };
  assert.equal(errorsFor((c, m) => voice(c, m, {})).length, 1);
  assert.equal(errorsFor((c, m) => voice(c, m, { held: "cic/texts/README.md" })).length, 0);
  assert.equal(errorsFor((c, m) => voice(c, m, { held: "cic/texts/README.md", name: "Nobody Named Here" })).length, 1);
});

test("the people list runs in date order", () => {
  assert.equal(errorsFor((c, m) => {
    const h = m(HOME);
    h.people = [{ person: PERSON }, { name: "Tertullian", year: 100, voice: 0, held: "cic/texts/README.md" }];
  }).length, 1);
});

test("concerns must name a person entry its note or a quote names", () => {
  const edge = c => c.edges.find(e => e.id === "greek-apologists-second-century--latin-apologists");
  assert.equal(errorsFor(c => { edge(c).concerns = HOME; }).length, 1);
  assert.equal(errorsFor(c => { edge(c).concerns = PERSON; edge(c).note = "Tertullian read the Greek apologists."; }).length, 0);
  assert.equal(errorsFor(c => { edge(c).concerns = PERSON; edge(c).note = "A plain note."; edge(c).sources.forEach(s => { s.quote = s.quote?.replaceAll("Tertullian", "T"); }); }).length >= 1, true);
});

test("the descent grade takes the five confidence levels, on a living tradition", () => {
  const living = census.movements.find(m => m.living && m.livingEvidence).id;
  assert.deepEqual(errorsFor((c, m) => { m(living).livingEvidence.descentConfidence = "Contested"; }), []);
  assert.equal(errorsFor((c, m) => { m(living).livingEvidence.descentConfidence = "Likely"; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(HOME).livingEvidence = { descentConfidence: "Contested" }; }).length, 1);
});
