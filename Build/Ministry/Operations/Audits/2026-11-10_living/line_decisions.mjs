// P2-V: decisions for every era 1-9 entry whose "continued as" line reaches a living era 10 entry.
// Usage: node line_decisions.mjs <worksheet.json> <census> <out.json>
import { readFileSync, writeFileSync } from "node:fs";
const [wsPath, censusPath, outPath] = process.argv.slice(2);
const ws = JSON.parse(readFileSync(wsPath, "utf8"));
const d = JSON.parse(readFileSync(censusPath, "utf8"));
const by = new Map(d.movements.map(m => [m.id, m]));
const edge = new Map(d.edges.map(e => [e.id, e]));
const RANK = { "Documented": 5, "Widely Accepted": 4, "Dominant Modern Reconstruction": 3, "Contested": 2, "Inferential-Thin": 1 };
const LEVEL = { "Dominant Modern Reconstruction": "a dominant modern reconstruction", "Contested": "contested", "Inferential-Thin": "an inference on thin evidence" };
const nm = id => by.get(id).name.replace(/^The /, "the ");
const list = names => names.length === 1 ? names[0] : `${names.slice(0, -1).join(", ")} and ${names.at(-1)}`;
const out = ws.filter(r => r.era < 10 && r.reachesLivingEra10).map(r => {
  const live = r.lineTerminals.filter(t => t.era === 10 && t.living);
  const carrier = [...new Set(live.map(t => t.id))];
  const names = carrier.map(nm);
  let basis = `The same tradition, by its line of later entries, as ${list(names)}, which ${carrier.length > 1 ? "carry" : "carries"} it today.`;
  let descentConfidence = null;
  const weak = live.map(t => t.weakestLink).filter(g => g && RANK[g] < 4).sort((a, b) => RANK[a] - RANK[b])[0];
  if (weak) {
    descentConfidence = weak;
    const e = live.flatMap(t => t.via).map(id => edge.get(id)).find(e => e.confidence === weak);
    basis += ` The line runs through one link the tree rates ${LEVEL[weak]}: ${nm(e.from).replace(/^the /, "The ")} continued as ${nm(e.to)}.`;
  }
  return {
    id: r.id, atlasId: r.atlasId, verdict: "living", group: "line", carrier, basis, descentConfidence,
    outcome: r.living ? (descentConfidence ? "graded" : "kept") : "added",
  };
});
writeFileSync(outPath, JSON.stringify(out, null, 1) + "\n");
const c = o => out.filter(x => x.outcome === o).length;
console.log(`line entries ${out.length}: kept ${c("kept")}, graded ${c("graded")}, added ${c("added")}`);
