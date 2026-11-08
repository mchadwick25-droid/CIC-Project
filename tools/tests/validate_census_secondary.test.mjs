// Secondary sources held in cic/texts/ (Decision-Log 2026-11-08, whole-set rulings).
// Run: node --test tools/tests/validate_census_secondary.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const [a, b] = census.movements.map(m => m.id).sort();
const held = census.edges.flatMap(e => e.sources).find(s => s.kind === "secondary" && s.file && s.lines && s.quote);

function secondaryErrors(source) {
  const edge = {
    id: `${a}--${b}`, from: a, to: b, type: "influenced", confidence: "Dominant Modern Reconstruction",
    note: "A short plain note.", sources: [source],
    citation_specificity: "A", verification_state: "verified-direct",
  };
  const dir = mkdtempSync(join(tmpdir(), "census-secondary-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify({ ...census, edges: [edge], retiredLinks: [] }));
  const run = spawnSync("node", ["tools/validate-census.mjs", path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR") && l.includes("source[0]"));
}

test("a secondary source with the work only passes", () => {
  assert.deepEqual(secondaryErrors({ kind: "secondary", work: "A secondary work" }), []);
});

test("a held secondary source with a verbatim quote passes", () => {
  assert.deepEqual(secondaryErrors({ ...held }), []);
});

test("a held secondary source with a quote not in its lines fails", () => {
  assert.equal(secondaryErrors({ ...held, quote: "words that are not in the text at all" }).length, 1);
});

test("a held secondary source with a file but no quote fails", () => {
  assert.equal(secondaryErrors({ ...held, quote: null }).length, 1);
});
