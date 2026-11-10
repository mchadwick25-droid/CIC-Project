// Sources read online, for era 10 links (Decision-Log 2026-11-10, "Change order: evidence for era 10 links").
// Run: node --test tools/tests/validate_census_online.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const [a, b] = census.movements.map(m => m.id).sort();
const online = {
  kind: "primary", work: "A church's basis of union (1925)", url: "https://example.org/basis",
  accessed: "2026-11-10", locus: "art. 1", quote: "The churches unite.", license: "all rights reserved; short quotation",
};
const secondary = { kind: "secondary", work: "A modern study (2005)" };

function errors(edge) {
  const full = {
    id: `${a}--${b}`, from: a, to: b, type: "influenced", note: "A short plain note.",
    citation_specificity: "A", verification_state: "verified-online", ...edge,
  };
  const dir = mkdtempSync(join(tmpdir(), "census-online-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify({ ...census, edges: [full], retiredLinks: [] }));
  const run = spawnSync("node", ["tools/validate-census.mjs", path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR") && l.includes(`${a}--${b}`));
}

test("a Widely Accepted link on a primary read online and a study passes", () => {
  assert.deepEqual(errors({ confidence: "Widely Accepted", sources: [online, secondary] }), []);
});

test("a link resting only on a source read online cannot be Documented", () => {
  const e = errors({ confidence: "Documented", verification_state: "verified-direct", sources: [online, secondary] });
  assert.ok(e.some(l => l.includes("held in the Library")));
});

test("a source read online needs an https address and the date it was read", () => {
  assert.ok(errors({ confidence: "Widely Accepted", sources: [{ ...online, url: "example.org" }, secondary] }).some(l => l.includes("https")));
  assert.ok(errors({ confidence: "Widely Accepted", sources: [{ ...online, accessed: "Nov 2026" }, secondary] }).some(l => l.includes("accessed")));
});

test("a primary read online needs its locus, quote and license", () => {
  assert.ok(errors({ confidence: "Widely Accepted", sources: [{ ...online, quote: "" }, secondary] }).some(l => l.includes("missing quote")));
});

test("a source cannot carry both a Library file and a web address", () => {
  assert.ok(errors({ confidence: "Widely Accepted", sources: [{ ...online, file: "cic/texts/x.txt", lines: "1" }, secondary] }).some(l => l.includes("not file and lines")));
});

test("a secondary study confirmed online passes with its address and date", () => {
  assert.deepEqual(errors({ confidence: "Dominant Modern Reconstruction", verification_state: "named-not-rechecked",
    sources: [{ ...secondary, url: "https://example.org/book", accessed: "2026-11-10" }] }), []);
});
