// P2-V worksheet: every movement's living flag, its "continued as" line, and possible carriers.
// Usage: node worksheet.mjs <census> <out.json>
import { readFileSync, writeFileSync } from "node:fs";
const [censusPath, outPath] = process.argv.slice(2);
const d = JSON.parse(readFileSync(censusPath, "utf8"));
const mv = d.movements.filter(m => m.kind !== "person");
const by = new Map(mv.map(m => [m.id, m]));
const nxt = {}, prv = {};
for (const e of d.edges) if (e.type === "continued as" && by.has(e.from) && by.has(e.to)) {
  (nxt[e.from] ??= []).push(e); (prv[e.to] ??= []).push(e);
}
const RANK = { "Documented": 5, "Widely Accepted": 4, "Dominant Modern Reconstruction": 3, "Contested": 2, "Inferential-Thin": 1 };
// every path forward along "continued as" to a terminal, with the weakest link grade on it
function paths(id, seen = new Set([id])) {
  const out = nxt[id];
  if (!out) return [{ terminal: id, weakest: null, via: [] }];
  return out.flatMap(e => seen.has(e.to) ? [] : paths(e.to, new Set([...seen, e.to])).map(p => ({
    terminal: p.terminal, via: [e.id, ...p.via],
    weakest: [e.confidence, p.weakest].filter(Boolean).sort((a, b) => RANK[a] - RANK[b])[0],
  })));
}
const rows = mv.map(m => {
  const ps = paths(m.id);
  const reach = ps.filter(p => { const t = by.get(p.terminal); return t.era === 10 && t.living; });
  const linked = d.edges.filter(e => (e.from === m.id || e.to === m.id) && e.type !== "continued as")
    .map(e => ({ type: e.type, other: e.from === m.id ? e.to : e.from, dir: e.from === m.id ? "out" : "in", confidence: e.confidence }))
    .filter(x => by.get(x.other)?.living).map(x => ({ ...x, otherAtlasId: by.get(x.other).atlasId, otherName: by.get(x.other).name, otherDates: by.get(x.other).dates }));
  return {
    id: m.id, atlasId: m.atlasId, era: m.era, name: m.name, dates: m.dates, start: m.start, end: m.end,
    lane: m.laneLabel, living: m.living, livingEvidence: m.livingEvidence ?? null,
    predecessors: (prv[m.id] ?? []).map(e => ({ id: e.from, atlasId: by.get(e.from).atlasId, confidence: e.confidence })),
    successors: (nxt[m.id] ?? []).map(e => ({ id: e.to, atlasId: by.get(e.to).atlasId, living: by.get(e.to).living, confidence: e.confidence })),
    lineTerminals: ps.map(p => ({ id: p.terminal, atlasId: by.get(p.terminal).atlasId, era: by.get(p.terminal).era, living: by.get(p.terminal).living, end: by.get(p.terminal).end, weakestLink: p.weakest, via: p.via })),
    reachesLivingEra10: reach.length > 0,
    otherLinksToLivingEntries: linked,
    statusDescription: m.statusDescription, relationsSummary: m.relationsSummary, why: m.why, legacy: m.legacy ?? null,
  };
});
writeFileSync(outPath, JSON.stringify(rows, null, 1));
const t = rows.filter(r => r.living).length;
console.log(`movements ${rows.length}; living ${t}; not living ${rows.length - t}; eras 1-9 reaching living era 10 by line ${rows.filter(r => r.era < 10 && r.reachesLivingEra10).length}`);
