// The card layout's fields (Stage Two Kit, sections 1 and 2): short description, the brief's old sources,
// open questions, quotation originals and the timeline, on a tradition, a person's card, a council and an era.
// Each fault sits on its own entry, so two validator runs cover every case.
// Run: node --test tools/tests/validate_census_card_layout.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const FILE = "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml";

function errorsFor(c) {
  const dir = mkdtempSync(join(tmpdir(), "census-layout-"));
  const path = join(dir, "census.json");
  writeFileSync(path, JSON.stringify(c));
  const run = spawnSync("node", ["tools/validate-census.mjs", "--skip-quotes", path], { encoding: "utf8" });
  return run.stdout.split("\n").filter(l => l.startsWith("ERROR"));
}

const timeline = () => [{
  when: "Around 200 to 217",
  headline: "Zephyrinus, and the quarrel over Father and Son",
  witness: "Most of this comes from Hippolytus, who opposed Zephyrinus and Callistus.",
  lines: [
    { when: "Around 200", text: "Zephyrinus followed Victor as bishop of Rome.", reference: "Eusebius, Church History 5.28" },
    { when: "In Zephyrinus's time", text: "Natalius was barely taken back into communion.", reference: "Eusebius, Church History 5.28", note: "A wonder, in its witness's voice" }
  ]
}];
const layout = () => ({
  shortDescription: "The church of Rome in the 200s.",
  briefSources: [{ title: "Hippolytus, Refutation of All Heresies, Book IX", author: "Hippolytus", file: FILE }, { title: "The list of Rome's bishops of 354" }],
  timeline: timeline(),
  uncertain: ["What Callistus meant."]
});
const traditions = census.movements.filter(m => !m.kind);

test("the census as it stands passes, and every kind takes the layout fields in its own place", () => {
  const c = structuredClone(census);
  const by = id => c.movements.find(m => m.id === id);
  Object.assign(by("roman-church-third-century"), layout());
  Object.assign(by("polycarp-of-smyrna").card, layout());
  Object.assign(by("council-of-nicaea-325").council, layout());
  Object.assign(c.eras[0], layout(), { longDescription: "An era brief.", modernWorks: [{ title: "A history", author: "A. Writer" }] });
  assert.deepEqual(errorsFor(c), []);
});

test("each fault in a layout field fails on its own entry, with its own message", () => {
  const c = structuredClone(census);
  const by = id => c.movements.find(m => m.id === id);
  const faults = [
    [m => { m.shortDescription = " "; }, "shortDescription must be a non-empty string"],
    [m => { m.briefSources = []; }, "briefSources must be a non-empty list"],
    [m => { m.briefSources = [{ author: "Hippolytus" }]; }, "briefSources[0].title must be a non-empty string"],
    [m => { m.briefSources = [{ title: "X", pages: "3" }]; }, "briefSources[0].pages is not allowed"],
    [m => { m.briefSources = [{ title: "X", file: "cic/texts/no-such-file.xml" }]; }, "briefSources[0].file cic/texts/no-such-file.xml must be an existing file under cic/texts/"],
    [m => { m.uncertain = ["", "fine"]; }, "uncertain must be a list of non-empty strings"],
    [m => { m.uncertain = "one question"; }, "uncertain must be a list of non-empty strings"],
    [m => { m.timeline = []; }, "timeline must be a non-empty list of periods"],
    [m => { const t = timeline(); delete t[0].headline; m.timeline = t; }, "timeline[0].headline must be a non-empty string"],
    [m => { const t = timeline(); t[0].lines = []; m.timeline = t; }, "timeline[0].lines must be a non-empty list"],
    [m => { const t = timeline(); delete t[0].lines[0].reference; m.timeline = t; }, "timeline[0].lines[0].reference must be a non-empty string"],
    [m => { const t = timeline(); t[0].lines[0].when = ""; m.timeline = t; }, "timeline[0].lines[0].when must be a non-empty string"],
    [m => { const t = timeline(); t[0].lines[0].year = 200; m.timeline = t; }, "timeline[0].lines[0].year is not allowed"],
    [m => { const t = timeline(); t[0].mood = "dark"; m.timeline = t; }, "timeline[0].mood is not allowed"],
    [m => { const t = timeline(); t[0].witness = ""; m.timeline = t; }, "timeline[0].witness must be a non-empty string"],
    [m => { m.quotationOriginals = []; }, "quotationOriginals must be a non-empty list"]
  ];
  const expected = faults.map(([apply, message], i) => { const m = by(traditions[i].id); apply(m); return `${m.id}: ${message}`; });
  const quoted = by(traditions[faults.length].id);
  quoted.quotationOriginals = [{ modern: "Words not in the brief", printed: "x", work: "w", file: FILE, lines: "1", secondReading: "same" }];
  by("polycarp-of-smyrna").timeline = timeline();
  by("council-of-nicaea-325").shortDescription = "A council.";
  c.eras[0].mood = "grim";
  c.eras[1].longDescription = "";
  c.eras[2].modernWorks = [{ title: "No author" }];
  expected.push(
    "polycarp-of-smyrna: timeline is kept in card for a person",
    "council-of-nicaea-325: shortDescription is kept in council for a major council",
    "era 1: mood is not allowed",
    "era 2: longDescription must be a non-empty string",
    "era 3: modernWorks[0].author must be a non-empty string"
  );
  const errors = errorsFor(c);
  for (const e of expected) assert.ok(errors.some(l => l.includes(e)), `missing: ${e}`);
  assert.ok(errors.some(l => l.includes(`${quoted.id}: quotationOriginals[0].modern`)), "a quotation not in the brief fails");
  const touched = [...faults.map((_, i) => traditions[i].id), quoted.id, "polycarp-of-smyrna", "council-of-nicaea-325", "era 1", "era 2", "era 3"];
  assert.deepEqual(errors.filter(l => !touched.some(id => l.includes(`${id}:`))), [], "no other entry fails");
  assert.equal(errors.filter(l => !l.includes(quoted.id)).length, expected.length, "each fault gives one error");
});
