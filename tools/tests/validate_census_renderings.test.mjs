// Listed renderings map to their originals and record their second reading
// (Decision-Log 2026-11-16, "Renderings made at the point of use and checked twice").
// Run: node --test tools/tests/validate_census_renderings.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const listing = JSON.parse(readFileSync("tools/quote_renderings.json", "utf8"));

function errorsFor(change) {
  const l = structuredClone(listing);
  change(l.renderings[0], l);
  const dir = mkdtempSync(join(tmpdir(), "census-renderings-"));
  const path = join(dir, "renderings.json");
  writeFileSync(path, JSON.stringify(l));
  const run = spawnSync("node", ["tools/validate-census.mjs", "--skip-quotes", "--renderings", path, "cic-website/data/world-census.json"], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR"));
}

test("the published listing passes", () => {
  assert.deepEqual(errorsFor(() => {}), []);
});

test("a listing with no lines fails", () => {
  assert.equal(errorsFor(r => { delete r.original.lines; }).length, 1);
});

test("lines past the end of the file fail", () => {
  assert.equal(errorsFor(r => { r.original.lines = "9999998-9999999"; }).length, 1);
});

test("a reversed range fails", () => {
  assert.equal(errorsFor(r => { r.original.lines = "200-100"; }).length, 1);
});

test("an original the entry does not cite fails", () => {
  const errs = errorsFor(r => { r.original.file = "cic/texts/benedict_rule-of-saint-benedict_gasquet1925.txt"; r.original.lines = "1"; });
  assert.equal(errs.length, 1);
  assert.match(errs[0], /is not among the files/);
});

test("an original outside cic/texts fails", () => {
  assert.equal(errorsFor(r => { r.original.file = "README.md"; }).length, 1);
});

test("a listing for no census entry fails", () => {
  assert.equal(errorsFor(r => { r.id = "no-such-person"; }).length, 1);
});

test("a listing with no language fails", () => {
  assert.equal(errorsFor(r => { delete r.original.language; }).length, 1);
});

test("a listing with no second reading fails", () => {
  assert.equal(errorsFor(r => { delete r.second_reading; }).length, 1);
});

test("a second reading whose record is missing fails", () => {
  assert.equal(errorsFor(r => { r.second_reading.record = "Build/Ministry/no-such-record.md"; }).length, 1);
});

test("a second reading with no verdict fails", () => {
  assert.equal(errorsFor(r => { delete r.second_reading.verdict; }).length, 1);
});

test("a second reading with another verdict fails", () => {
  assert.equal(errorsFor(r => { r.second_reading.verdict = "fine"; }).length, 1);
});
