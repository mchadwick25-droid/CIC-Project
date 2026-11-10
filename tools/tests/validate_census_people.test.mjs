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
// Other persons told within HOME are told within no tradition here, so a case that empties
// HOME's people list tests PERSON alone.
const alone = c => c.movements
  .filter(x => x.kind === "person" && x.toldWithin === HOME && x.id !== PERSON)
  .forEach(x => { x.toldWithin = null; });

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
  assert.deepEqual(errorsFor((c, m) => { alone(c); m(PERSON).toldWithin = null; m(HOME).people = []; m(HOME).peopleNote = "No one is shown."; }), []);
});

test("toldWithin must name a movement that lists the person", () => {
  assert.equal(errorsFor((c, m) => { m(PERSON).toldWithin = "no-such-movement"; }).length, 2);
  assert.equal(errorsFor((c, m) => { alone(c); m(HOME).people = []; m(HOME).peopleNote = "No one is shown."; }).length, 1);
});

test("a movement that names no one says why in peopleNote, and only then", () => {
  assert.equal(errorsFor((c, m) => { alone(c); m(PERSON).toldWithin = null; m(HOME).people = []; delete m(HOME).peopleNote; }).length, 1);
  assert.equal(errorsFor((c, m) => { alone(c); m(PERSON).toldWithin = null; m(HOME).people = []; m(HOME).peopleNote = " "; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(HOME).peopleNote = "No one is shown."; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(PERSON).peopleNote = "No one is shown."; }).length, 1);
});

test("toldWithin is only for a person entry", () => {
  assert.equal(errorsFor((c, m) => { m(HOME).toldWithin = null; }).length, 1);
});

test("every movement has a people list and every entry a review status", () => {
  assert.equal(errorsFor((c, m) => { alone(c); delete m(HOME).people; }).length, 2);
  assert.equal(errorsFor((c, m) => { m(HOME).reviewStatus = "checked"; }).length, 1);
});

const ARNOBIUS_ROW = readFileSync("cic/corpus-map/latin-apologists.yaml", "utf8").match(/^- row_id: (.+)\n(?:  .*\n)*?  author: arnobius$/m)[1];
const arnobius = (h, extra = {}) => ({ name: "Arnobius", year: 300, voice: h.voices.findIndex(v => v.includes("Arnobius")), author: "arnobius", held: ARNOBIUS_ROW, ...extra });

test("a named voice must be named in its voices line and held on its own shelf by its author", () => {
  assert.deepEqual(errorsFor((c, m) => { const h = m(HOME); h.people = [{ person: PERSON }, arnobius(h)]; }), []);
  assert.equal(errorsFor((c, m) => { const h = m(HOME); h.people = [{ person: PERSON }, arnobius(h, { held: undefined })]; }).length, 1);
  assert.equal(errorsFor((c, m) => { const h = m(HOME); h.people = [{ person: PERSON }, arnobius(h, { author: "lactantius" })]; }).length, 1);
  assert.equal(errorsFor((c, m) => { const h = m(HOME); h.people = [{ person: PERSON }, arnobius(h, { held: "no-such-row" })]; }).length, 1);
  assert.equal(errorsFor((c, m) => { const h = m(HOME); h.people = [{ person: PERSON }, arnobius(h, { name: "Nobody Named Here" })]; }).length, 1);
});

test("the people list runs in date order", () => {
  assert.equal(errorsFor((c, m) => { const h = m(HOME); h.people = [{ person: PERSON }, arnobius(h, { year: 100 })]; }).length, 1);
});

test("a person entry is not listed again as a named voice", () => {
  assert.equal(errorsFor((c, m) => {
    const h = m(HOME);
    h.people = [{ person: PERSON }, arnobius(h, { name: "Tertullian", voice: 0 })];
  }).filter(l => l.includes("already in this row")).length, 1);
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
  // No basis: the descent grade and the living mark each need one.
  assert.equal(errorsFor((c, m) => { m(living).livingEvidence = { descentConfidence: "Contested" }; }).length, 2);
  assert.equal(errorsFor((c, m) => { m(living).livingEvidence.descentConfidence = "Likely"; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(HOME).livingEvidence = { basis: "A stated basis.", descentConfidence: "Contested" }; }).length, 1);
});

test("a living tradition says what its mark rests on (Decision-Log 2026-11-10, \"What 'living' means\")", () => {
  const carried = census.movements.find(m => m.living && m.livingEvidence?.carrier).id;
  const named = new Set(census.movements.flatMap(m => m.livingEvidence?.carrier ?? []));
  const own = census.movements.find(m => m.living && !m.livingEvidence?.carrier && m.livingEvidence?.grade && !named.has(m.id)).id;
  const ended = census.movements.find(m => m.kind !== "person" && m.living === false).id;
  assert.equal(errorsFor((c, m) => { delete m(own).livingEvidence; }).length, 1);
  assert.equal(errorsFor((c, m) => { delete m(own).livingEvidence.grade; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(carried).livingEvidence.carrier = ["no-such-movement"]; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(carried).livingEvidence.carrier = [ended]; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(carried).livingEvidence.carrier = [carried]; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(carried).livingEvidence.carrier = []; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(own).livingEvidence.carrier = [carried]; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(ended).livingEvidence = { basis: "A stated basis.", carrier: [own] }; }).length, 1);
});
