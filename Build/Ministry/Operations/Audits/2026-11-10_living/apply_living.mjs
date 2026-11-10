// P2-V: apply the living-flag check to the census as one data release.
// Usage: node apply_living.mjs <census in> <decisions.json> <era10 evidence.json> <census out> <release number> <release date> <log out>
// era10 evidence.json adds dated evidence and a grade to era 10 carriers that had none (their flags stay as ruled).
// decisions.json is the reviewed outcome for every movement in eras 1 to 9 (decisions_final.json).
// Era 10 flags were set at the era 10 gate (G-5) and are not changed here.
import { readFileSync, writeFileSync } from "node:fs";

const [inPath, decPath, e10Path, outPath, relNum, relDate, logPath] = process.argv.slice(2);
const d = JSON.parse(readFileSync(inPath, "utf8"));
const decisions = JSON.parse(readFileSync(decPath, "utf8"));
const by = new Map(d.movements.map(m => [m.id, m]));
const log = [];

for (const x of decisions) {
  const m = by.get(x.id);
  if (!m) throw new Error(`no movement ${x.id}`);
  if (m.era === 10 || m.kind === "person") throw new Error(`${x.id}: era 10 and person entries are not changed here`);
  const before = { living: m.living, livingEvidence: m.livingEvidence ?? null };
  const living = x.verdict === "living";
  const ev = { basis: x.basis };
  if (living) {
    if (x.carrier?.length) ev.carrier = x.carrier;
    else {
      if (x.evidence) ev.evidence = x.evidence;
      ev.grade = x.grade;
    }
    if (x.descentConfidence) ev.descentConfidence = x.descentConfidence;
  }
  ev.group = x.group;
  m.living = living;
  m.livingEvidence = ev;
  log.push({ id: m.id, atlasId: m.atlasId, outcome: x.outcome, before, after: { living, livingEvidence: ev } });
}

for (const x of JSON.parse(readFileSync(e10Path, "utf8"))) {
  const m = by.get(x.id);
  if (!m || m.era !== 10 || m.living !== true) throw new Error(`${x.id}: not a living era 10 entry`);
  const before = structuredClone(m.livingEvidence);
  m.livingEvidence = { ...m.livingEvidence, evidence: x.evidence, grade: x.grade };
  log.push({ id: m.id, atlasId: m.atlasId, outcome: "era 10 evidence added", before: { livingEvidence: before }, after: { livingEvidence: m.livingEvidence } });
}

d.meta.release = { number: Number(relNum), date: relDate };
writeFileSync(outPath, JSON.stringify(d, null, 1) + "\n");
writeFileSync(logPath, JSON.stringify(log, null, 1) + "\n");
const count = o => log.filter(l => l.outcome === o).length;
console.log(`applied ${log.length}: kept ${count("kept")}, graded ${count("graded")}, dropped ${count("dropped")}, added ${count("added")}, stays not living ${count("stays not living")}`);
console.log(`living now ${d.movements.filter(m => m.living === true && m.kind !== "person").length}`);
