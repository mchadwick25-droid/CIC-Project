// The `kind` field on census movements: absent for a church body, or "cross-church movement".
// Run: node --test tools/tests/validate_census_kind.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));

function validate(data) {
  const dir = mkdtempSync(join(tmpdir(), "census-kind-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify(data));
  const run = spawnSync("node", ["tools/validate-census.mjs", path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR"));
}

function withKind(kind) {
  const movements = census.movements.map((m, i) => {
    const { kind: _, ...rest } = m;
    return i === 0 && kind !== undefined ? { ...rest, kind } : rest;
  });
  return validate({ ...census, movements }).filter(l => l.includes("kind"));
}

test("a movement with no kind is a church body and passes", () => {
  assert.deepEqual(withKind(undefined), []);
});

test("a cross-church movement passes", () => {
  assert.deepEqual(withKind("cross-church movement"), []);
});

test("an unknown kind fails", () => {
  assert.equal(withKind("current").length, 1);
});

test("an empty kind fails", () => {
  assert.equal(withKind("").length, 1);
});

test("the census's own kinds all pass", () => {
  assert.deepEqual(validate(census).filter(l => l.includes("kind")), []);
});
