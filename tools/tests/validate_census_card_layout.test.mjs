// The card layout's fields (Stage Two Kit, sections 1 and 2): short description, the brief's old sources,
// open questions, quotation originals and the timeline, on a tradition, a person's card, a council and an era.
// Run: node --test tools/tests/validate_census_card_layout.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const TRADITION = "roman-church-third-century";
const PERSON = "polycarp-of-smyrna";
const COUNCIL = "council-of-nicaea-325";
const FILE = "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml";

function errorsFor(change) {
  const c = structuredClone(census);
  change(c, id => c.movements.find(m => m.id === id));
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

test("the census as it stands passes", () => {
  assert.deepEqual(errorsFor(() => {}), []);
});

test("every kind takes the layout fields in its own place", () => {
  assert.deepEqual(errorsFor((c, m) => { Object.assign(m(TRADITION), layout()); }), []);
  assert.deepEqual(errorsFor((c, m) => { Object.assign(m(PERSON).card, layout()); }), []);
  assert.deepEqual(errorsFor((c, m) => { Object.assign(m(COUNCIL).council, layout()); }), []);
  assert.deepEqual(errorsFor(c => { Object.assign(c.eras[0], layout(), { longDescription: "An era brief.", modernWorks: [{ title: "A history", author: "A. Writer" }] }); }), []);
});

test("a person's or council's layout fields on the entry itself fail", () => {
  assert.equal(errorsFor((c, m) => { m(PERSON).timeline = timeline(); }).length, 1);
  assert.equal(errorsFor((c, m) => { m(COUNCIL).shortDescription = "A council."; }).length, 1);
});

test("an empty short description fails", () => {
  assert.equal(errorsFor((c, m) => { m(TRADITION).shortDescription = " "; }).length, 1);
});

test("a brief source needs a title, takes only title, author and file, and a file must be held", () => {
  assert.equal(errorsFor((c, m) => { m(TRADITION).briefSources = []; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(TRADITION).briefSources = [{ author: "Hippolytus" }]; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(TRADITION).briefSources = [{ title: "X", pages: "3" }]; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(TRADITION).briefSources = [{ title: "X", file: "cic/texts/no-such-file.xml" }]; }).length, 1);
});

test("open questions are plain strings", () => {
  assert.equal(errorsFor((c, m) => { m(TRADITION).uncertain = ["", "fine"]; }).length, 1);
  assert.equal(errorsFor((c, m) => { m(TRADITION).uncertain = "one question"; }).length, 1);
});

test("a timeline is periods of dated, referenced lines", () => {
  assert.equal(errorsFor((c, m) => { m(TRADITION).timeline = []; }).length, 1);
  assert.equal(errorsFor((c, m) => { const t = timeline(); delete t[0].headline; m(TRADITION).timeline = t; }).length, 1);
  assert.equal(errorsFor((c, m) => { const t = timeline(); t[0].lines = []; m(TRADITION).timeline = t; }).length, 1);
  assert.equal(errorsFor((c, m) => { const t = timeline(); delete t[0].lines[0].reference; m(TRADITION).timeline = t; }).length, 1);
  assert.equal(errorsFor((c, m) => { const t = timeline(); t[0].lines[0].when = ""; m(TRADITION).timeline = t; }).length, 1);
  assert.equal(errorsFor((c, m) => { const t = timeline(); t[0].lines[0].year = 200; m(TRADITION).timeline = t; }).length, 1);
  assert.equal(errorsFor((c, m) => { const t = timeline(); t[0].mood = "dark"; m(TRADITION).timeline = t; }).length, 1);
  assert.equal(errorsFor((c, m) => { const t = timeline(); t[0].witness = ""; m(TRADITION).timeline = t; }).length, 1);
});

test("a tradition's quotation originals are checked against its brief", () => {
  assert.equal(errorsFor((c, m) => { m(TRADITION).quotationOriginals = []; }).length, 1);
  assert.ok(errorsFor((c, m) => { m(TRADITION).quotationOriginals = [{ modern: "Words not in the brief", printed: "x", work: "w", file: FILE, lines: "1", secondReading: "same" }]; }).length >= 1);
});

test("an era takes only its known keys", () => {
  assert.equal(errorsFor(c => { c.eras[0].mood = "grim"; }).length, 1);
  assert.equal(errorsFor(c => { c.eras[0].longDescription = ""; }).length, 1);
  assert.equal(errorsFor(c => { c.eras[0].modernWorks = [{ title: "No author" }]; }).length, 1);
});
