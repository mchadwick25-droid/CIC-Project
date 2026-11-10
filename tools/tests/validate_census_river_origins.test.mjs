// Where each river leaves its parent: the page's RIVER_ORIGINS record against the census links.
// Run: node --test tools/tests/validate_census_river_origins.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const page = readFileSync("cft-website/index.html", "utf8");
const MARK = "const RIVER_ORIGINS = ";
const recStart = page.indexOf(MARK) + MARK.length;
const recEnd = page.indexOf("\n;\n", recStart);
const record = JSON.parse(page.slice(recStart, recEnd));

function validate(data, rec = record) {
  const dir = mkdtempSync(join(tmpdir(), "census-rivers-"));
  const path = join(dir, "census.json"), atlas = join(dir, "index.html");
  writeFileSync(path, JSON.stringify(data));
  writeFileSync(atlas, page.slice(0, recStart) + JSON.stringify(rec, null, 1) + page.slice(recEnd));
  const run = spawnSync("node", ["tools/validate-census.mjs", path, "--atlas", atlas], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR") && l.includes("river origin"));
}
const link = (from, to, type) => ({ id: `${from}--${to}`, from, to, type, confidence: "Documented" });

test("the census and the page's record agree", () => {
  assert.deepEqual(validate(census), []);
});

test("data order never decides a river's parent", () => {
  assert.deepEqual(validate({ ...census, edges: [...census.edges].reverse() }), []);
});

test("an influence into a river's first movement does not make it the parent", () => {
  const e = link("antiochene-exegetical-christianity-chrysostom-ce", "the-1904-07-revival-family-wales-mukti-india-pyo", "influenced");
  assert.deepEqual(validate({ ...census, edges: [e, ...census.edges] }), []);
});

test("a new descent link into a declared river fails until the record names it", () => {
  const e = link("the-mainline-century-liberal-and-neo-orthodox", "the-1904-07-revival-family-wales-mukti-india-pyo", "gave rise to");
  const errs = validate({ ...census, edges: [e, ...census.edges] });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /river origin 7: the strongest descent link is/);
});

test("a break counts only from a movement that started earlier", () => {
  const later = link("the-1904-07-revival-family-wales-mukti-india-pyo", "the-mainline-century-liberal-and-neo-orthodox", "broke with");
  assert.deepEqual(validate({ ...census, edges: [later, ...census.edges] }), []);
  const earlier = link("the-1904-07-revival-family-wales-mukti-india-pyo", "lutheran-wittenberg-and-its-congregations", "broke with");
  assert.equal(validate({ ...census, edges: [earlier, ...census.edges] }).length, 1);
});

test("lineage outranks a break, whatever their order", () => {
  const brk = link("the-reformed-cities-zurich-and-geneva", "the-1904-07-revival-family-wales-mukti-india-pyo", "broke with");
  const rise = link("the-mainline-century-liberal-and-neo-orthodox", "the-1904-07-revival-family-wales-mukti-india-pyo", "gave rise to");
  const rec = record.map(o => o.lane === 7 ? { lane: 7, parent: 6, basis: "lineage", link: rise.id } : o);
  assert.deepEqual(validate({ ...census, edges: [brk, rise, ...census.edges] }, rec), []);
  assert.deepEqual(validate({ ...census, edges: [rise, brk, ...census.edges] }, rec), []);
});

test("every river needs an entry", () => {
  const errs = validate(census, record.filter(o => o.lane !== 7));
  assert.deepEqual(errs, ["ERROR river origin 7: the record has no entry for this river"]);
});

test("a declared quote must stand verbatim in its Library file", () => {
  const rec = record.map(o => o.lane === 80 ? { ...o, sources: [{ ...o.sources[0], quote: "Valentinus wished to be pope." }] } : o);
  assert.equal(validate(census, rec).length, 1);
});

test("a parent that never reaches the origin trunk fails", () => {
  const rec = record.map(o => o.lane === 7 ? { ...o, parent: 7 } : o);
  assert.ok(validate(census, rec).some(l => l.includes("never reaches the origin trunk")));
});
