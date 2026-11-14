// The `outcome` field on census links (Decision-Log 2026-11-08, major links).
// Run: node --test tools/tests/validate_census_outcome.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const [a, b] = census.movements.map(m => m.id).sort();

function outcomeErrors(type, outcome) {
  const edge = {
    id: `${a}--${b}`, from: a, to: b, type, confidence: "Inferential-Thin",
    note: "A short plain note.",
    sources: [{ kind: "secondary", work: "A secondary work" }],
    citation_specificity: "E", verification_state: "unverified",
  };
  if (outcome !== undefined) edge.outcome = outcome;
  const dir = mkdtempSync(join(tmpdir(), "census-outcome-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify({ ...census, edges: [edge], retiredLinks: [] }));
  const run = spawnSync("node", ["tools/validate-census.mjs", "--skip-quotes", path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR") && l.includes("outcome"));
}

test("a judged link with a plain outcome sentence passes", () => {
  assert.deepEqual(outcomeErrors("argued against", "The council condemned the group by name."), []);
});

test("a link without outcome passes", () => {
  assert.deepEqual(outcomeErrors("influenced", undefined), []);
});

test("outcome on a link that is major by type fails", () => {
  assert.equal(outcomeErrors("gave rise to", "A new church formed.").length, 1);
});

test("an empty outcome fails", () => {
  assert.equal(outcomeErrors("influenced", "  ").length, 1);
});

test("outcome with internal language fails", () => {
  assert.ok(outcomeErrors("influenced", "The census edge is graded high.").length >= 1);
});

test("outcome past 30 words fails", () => {
  assert.equal(outcomeErrors("influenced", Array(31).fill("word").join(" ") + ".").length, 1);
});

test("outcome that does not end as a sentence fails", () => {
  assert.equal(outcomeErrors("in contact with", "The two sides met").length, 1);
});
