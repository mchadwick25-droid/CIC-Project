// Story cards show reader text only: no census or story id, and no builder's note in "How it connects".
// Run: node --test tools/tests/validate_census_story_text.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const censusPath = "cic-website/data/world-census.json";
const page = readFileSync("cft-website/index.html", "utf8");
const at = page.indexOf('"stories":', page.indexOf("const DATA"));
const open = page.indexOf("[", at);
let end = open;
for (let depth = 0; end < page.length; end++) { if (page[end] === "[") depth++; else if (page[end] === "]" && --depth === 0) break; }
const stories = JSON.parse(page.slice(open, end + 1));

function validate(list) {
  const dir = mkdtempSync(join(tmpdir(), "census-stories-"));
  const atlas = join(dir, "index.html");
  writeFileSync(atlas, page.slice(0, open) + JSON.stringify(list, null, 1) + page.slice(end + 1));
  const run = spawnSync("node", ["tools/validate-census.mjs", "--skip-quotes", censusPath, "--atlas", atlas], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR") && l.includes("story "));
}
const withSummary = (i, text, field = "relationsSummary") => stories.map((s, j) => j === i ? { ...s, [field]: text } : s);

test("every story card on the page reads as plain text", () => {
  assert.deepEqual(validate(stories), []);
});

test("a census id in How it connects fails", () => {
  const errs = validate(withSummary(0, "It belongs beside the-moravian-church-at-herrnhut."));
  assert.equal(errs.length, 1);
  assert.match(errs[0], /shows the id "the-moravian-church-at-herrnhut"/);
});

test("a one-word census id fails only in its lower-case slug form", () => {
  assert.equal(validate(withSummary(0, "Its rival was donatism.")).length, 1);
  assert.deepEqual(validate(withSummary(0, "Its rival was Donatism.")), []);
});

test("an id in the caveat or teaser fails too", () => {
  assert.equal(validate(withSummary(0, "See puritanism for more.", "caveat")).length, 1);
  assert.equal(validate(withSummary(0, "Close to anatolian-church-third-century.", "teaser")).length, 1);
});

test("builder notes in How it connects fail", () => {
  for (const note of [
    "Donatism grew from it, though that record never names Abitinae.",
    "Tertullian, whose record sits with the Latin apologists, cites her vision.",
    "Placed at 3.5 because the church spoke Greek.",
    "The flagellants of 1260, drafted separately below, followed it.",
    "He appears here as a story rather than as his own entry.",
    "The Maronite church is recorded on this map only up to 1517.",
  ]) assert.ok(validate(withSummary(0, note)).length >= 1, note);
});

test("history's own records are not builder notes", () => {
  assert.deepEqual(validate(withSummary(0, "Her trial record survives in Latin, with the French minute of the court.")), []);
});
