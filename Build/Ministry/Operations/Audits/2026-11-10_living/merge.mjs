// P2-V: merge the six research batches and the line decisions into one draft of decisions.
// Usage: node merge.mjs <audit dir> <out.json>
import { readFileSync, writeFileSync } from "node:fs";
const [dir, outPath] = process.argv.slice(2);
const J = p => JSON.parse(readFileSync(p, "utf8"));
const census = J("cic-website/data/world-census.json");
const by = new Map(census.movements.map(m => [m.id, m]));
const qc = J(`${dir}/research/quote_check.json`);
const passed = (id, i) => qc.some(r => r.id === id && r.item === i && r.saved && r.fresh);
const byAtlas = new Map(census.movements.map(m => [m.atlasId, m.id]));
const res = [1, 2, 3, 4, 5, 6].flatMap(i => J(`${dir}/research/result_batch_${i}.json`))
  .map(r => ({ ...r, carrier: (r.carrier ?? []).map(c => by.has(c) ? c : byAtlas.get(c) ?? c) }));
const line = J(`${dir}/line_decisions.json`);
const year = s => Number(String(s ?? "").slice(0, 4)) || null;
const out = new Map();
for (const r of res) {
  const living = r.verdict === "living";
  const ev = (r.evidence ?? []).map((e, i) => ({ ...e, verified: !!(e.quote && passed(r.id, i)) }));
  let grade = "n/a";
  if (living && !(r.carrier?.length)) {
    const dated = ev.filter(e => year(e.date) >= 2011);
    const ind = dated.filter(e => e.kind === "independent" && e.verified);
    const newest = Math.max(...dated.map(e => year(e.date)), 0), newestV = Math.max(...dated.filter(e => e.verified).map(e => year(e.date)), 0);
    if (!dated.length) grade = "none (no dated item after 2010 found)";
    else if (r.grade === "CD" && ind.length) grade = `CD (Contemporary-Documented); newest dated item ${newest}, newest verified ${newestV || "none"}`;
    else grade = `CR (Contemporary-Reported); newest dated item ${newest}, newest verified ${newestV || "none"}`;
  }
  out.set(r.id, {
    id: r.id, atlasId: r.atlasId, currentFlag: by.get(r.id).living, verdict: r.verdict, group: r.class,
    tradition: r.tradition, presentBody: r.presentBody, namedGap: r.namedGap,
    carrier: r.carrier ?? [], evidenceItems: ev,
    evidence: ev.length ? ev.map(e => `${e.title}, ${e.publisher} (${e.date}): ${e.kind}; ${e.verified ? "verified" : "not verified"}. ${e.url}`).join(" | ") : null,
    grade, descentConfidence: living ? r.descentConfidence ?? null : null, descentBasis: r.descentBasis ?? null,
    basis: r.basis, endQuote: r.endQuote ?? null, wanted: r.wanted ?? null, openQuestion: r.openQuestion ?? null,
    agentGrade: r.grade,
  });
}
for (const l of line) out.set(l.id, { ...l, currentFlag: by.get(l.id).living, evidence: null, grade: "n/a" });
// flatten carriers to the entries that hold evidence themselves
const holds = id => { const x = out.get(id); const m = by.get(id); return x ? (x.verdict === "living" && !x.carrier.length) : (m.era === 10 && m.living && !m.livingEvidence?.carrier); };
const problems = [];
function resolve(id, seen = new Set()) {
  if (seen.has(id)) { problems.push(`carrier loop at ${id}`); return []; }
  seen.add(id);
  const x = out.get(id), m = by.get(id);
  if (!m) { problems.push(`unknown carrier ${id}`); return []; }
  if (holds(id)) return [id];
  if (x && x.verdict === "living" && x.carrier.length) return x.carrier.flatMap(c => resolve(c, seen));
  problems.push(`carrier ${id} is not living or holds nothing`); return [];
}
for (const x of out.values()) if (x.verdict === "living" && x.carrier.length) {
  const flat = [...new Set(x.carrier.flatMap(c => resolve(c, new Set([x.id]))))];
  if (flat.join() !== x.carrier.join()) x.carrierAsDrafted = x.carrier;
  x.carrier = flat;
  if (!flat.length) problems.push(`${x.atlasId}: no carrier left`);
}
for (const x of out.values()) {
  const L = x.verdict === "living";
  x.outcome = x.currentFlag ? (L ? (x.descentConfidence ? "graded" : "kept") : "dropped") : (L ? "added" : "stays not living");
}
const arr = [...out.values()].sort((a, b) => by.get(a.id).era - by.get(b.id).era || by.get(a.id).start - by.get(b.id).start);
writeFileSync(outPath, JSON.stringify(arr, null, 1) + "\n");
const c = o => arr.filter(x => x.outcome === o).length;
console.log(`decisions ${arr.length}: kept ${c("kept")}, graded ${c("graded")}, dropped ${c("dropped")}, added ${c("added")}, stays not living ${c("stays not living")}`);
console.log(`grades on own evidence: ${["CD","CR","none"].map(g => g + " " + arr.filter(x => x.grade.startsWith(g)).length).join(", ")}`);
problems.forEach(p => console.log("PROBLEM", p));
