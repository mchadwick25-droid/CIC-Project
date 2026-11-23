// The sourced search names file beside the census: every row needs a real target, a kind and a basis.
// Run: node --test tools/tests/validate_census_search_names.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const censusText = readFileSync("cic-website/data/world-census.json", "utf8");

function validate(rows) {
  const dir = mkdtempSync(join(tmpdir(), "census-names-"));
  writeFileSync(join(dir, "world-census.json"), censusText);
  writeFileSync(join(dir, "search-names.json"), JSON.stringify({ rows }));
  const run = spawnSync("node", ["tools/validate-census.mjs", "--skip-quotes", join(dir, "world-census.json")], { encoding: "utf8" });
  return run.stdout.split("\n").filter((l) => l.startsWith("ERROR") && l.includes("search-names"));
}

const good = {
  name: "Montanist",
  kind: "name given by opponents",
  entry: "montanism-the-new-prophecy",
  basis: { source: "tree", entry: "montanism-the-new-prophecy", field: "longDescription", text: "that was their opponents' label." },
};

test("a row with a real entry, a kind and a basis passes", () => {
  assert.deepEqual(validate([good]), []);
});

test("a row with no real entry fails", () => {
  assert.equal(validate([{ ...good, entry: "no-such-entry" }]).length, 1);
});

test("a row with no kind or a wrong kind fails", () => {
  assert.equal(validate([{ ...good, kind: undefined }]).length, 1);
  assert.equal(validate([{ ...good, kind: "nickname" }]).length, 1);
});

test("a row with no basis fails", () => {
  const { basis: _, ...bare } = good;
  assert.equal(validate([bare]).length, 1);
});

test("a tree basis that is not word for word in the entry fails", () => {
  assert.equal(validate([{ ...good, basis: { ...good.basis, text: "words the entry never says" } }]).length, 1);
});

test("a row needs exactly one of entry, country or region", () => {
  assert.equal(validate([{ ...good, country: "Iran" }]).length, 1);
});
