// A retired movement with no redirect keeps its address, which serves a retired notice.
// Run: node --test tools/tests/validate_census_retired.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));

function retiredErrors(pageHtml, record = {}) {
  const dir = mkdtempSync(join(tmpdir(), "census-retired-"));
  const tree = join(dir, "tree");
  mkdirSync(tree);
  for (const m of census.movements) writeFileSync(join(tree, `${m.id}.html`), census.edges
    .filter(e => e.from === m.id || e.to === m.id).map(e => `<li id="${e.id}">`).join(""));
  const retired = { id: "a-retired-movement", name: "A Retired Movement", date: "2026-11-08", reason: "A plain reason.", ...record };
  if (pageHtml !== null) writeFileSync(join(tree, `${retired.id}.html`), pageHtml);
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify({ ...census, retiredMovements: [retired] }));
  const run = spawnSync("node", ["tools/validate-census.mjs", "--skip-quotes", "--tree", tree, path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR") && l.includes("a-retired-movement"));
}

test("a retired movement with no redirect needs its retired page", () => {
  assert.equal(retiredErrors(null).length, 1);
});

test("a retired movement's address must not still serve the old entry", () => {
  assert.equal(retiredErrors("<main><h1>The old entry</h1></main>").length, 1);
});

test("a retired page passes", () => {
  assert.deepEqual(retiredErrors('<main data-retired="true"><h1>Retired</h1></main>'), []);
});

test("a retired movement that keeps its page needs its name", () => {
  assert.equal(retiredErrors('<main data-retired="true"></main>', { name: undefined }).length, 1);
});
