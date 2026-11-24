// Modern works on an entry or a documented story: title and author required, a few optional strings, nothing else.
// Run: node --test tools/tests/validate_census_modern_works.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const ENTRY = census.movements.find(m => (m.documentedStories ?? []).length).id;
const work = () => ({ title: "The Church in the Roman Empire", author: "W. M. Ramsay", year: "1893", note: "A study of the inscriptions." });

function errorsFor(change) {
  const c = structuredClone(census);
  change(c.movements.find(m => m.id === ENTRY));
  const dir = mkdtempSync(join(tmpdir(), "census-modern-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify(c));
  const run = spawnSync("node", ["tools/validate-census.mjs", "--skip-quotes", path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR") && l.includes("modernWorks"));
}

test("modern works on an entry and on a story pass", () => {
  assert.deepEqual(errorsFor(m => { m.modernWorks = [work()]; m.documentedStories[0].modernWorks = [work()]; }), []);
});

test("a missing author, an unknown key or an empty list fails", () => {
  assert.equal(errorsFor(m => { m.modernWorks = [{ title: "A book" }]; }).length, 1);
  assert.equal(errorsFor(m => { m.modernWorks = [{ ...work(), pages: "12" }]; }).length, 1);
  assert.equal(errorsFor(m => { m.modernWorks = []; }).length, 1);
});
