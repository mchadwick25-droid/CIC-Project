// P2-V: draft the Open-Gaps entries 157 to 163 from the final decisions.
// Usage: node open_gaps_text.mjs <audit dir> <out.txt>
import { readFileSync, writeFileSync } from "node:fs";
const [dir, out] = process.argv.slice(2);
const d = JSON.parse(readFileSync(`${dir}/decisions_final.json`, "utf8"));
const census = JSON.parse(readFileSync("cic-website/data/world-census.json", "utf8"));
const names = new Map(census.movements.map(m => [m.id, m.name]));
function wrap(text, indent) {
  const lines = []; let line = indent;
  for (const w of text.split(" ")) {
    if ((line + " " + w).length > 100 && line.trim()) { lines.push(line); line = indent + w; }
    else line = line === indent ? indent + w : `${line} ${w}`;
  }
  lines.push(line);
  return lines.join("\n");
}
const gaps = [...new Set(d.filter(x => x.verdict === "living" && x.namedGap)
  .map(x => x.namedGap.replace(/^The /, "the ").replace(/;.*$/, "")))];
const questions = d.filter(x => x.openQuestion && x.atlasId !== "I.27")
  .map(x => wrap(`- ${names.get(x.id)}: ${x.openQuestion}`, "    "));
const text = `157. **What P2-V settles (2026-11-10).** Data release 30 carries the written definition of "living"
    and the check of every living flag (Decision-Log, "What 'living' means: P2-V applied as data
    release 30", same date; audit \`Build/Ministry/Operations/Audits/2026-11-10_living/\`). Ruling 15's
    condition before the leaf appears is met; the drawn marks are P2-K1. Flags: 192 true before, 263
    after (of the 127 true in eras 1 to 9: 116 kept, 9 graded, 2 dropped; 73 added; era 10 as
    ruled at its gate).
158. **Living traditions with no entry after a date: the named gaps (2026-11-10).** Under principle 3
    of the gap sweep ruling, each is told only to the year shown, and the gap is named on its living
    flag (\`decisions_final.json\`, field \`namedGap\`). Filling any of them adds a row to a frozen
    era, so each is a change order with its sources found first. Some overlap "Breaks in the
    timeline" (2026-11-10). ${gaps.length} gaps:
${wrap(gaps.join("; ") + ".", "    ")}
159. **Present-day families the tree does not reach (2026-11-10).** The backward check
    (\`research/backward_check.json\`) traced 58 present-day families. 24 reach about 2010 through a
    living entry; 29 stop earlier (the gaps above); 5 have no entry at all: the Greek Orthodox
    Patriarchate of Alexandria, the Church of Cyprus, the Polish Orthodox Church, the Orthodox
    Church of the Czech Lands and Slovakia, and the Macedonian Orthodox Church. Eastern Catholic
    churches the tree never names: the Syriac, Coptic, Ethiopian and Eritrean, Hungarian, Slovak,
    Italo-Albanian, Bulgarian, Greek and Croatian Greek Catholic churches. For a later completeness
    pass; adding any is a change order.
160. **The Lérins entry says the abbey has stood since about 410 (2026-11-10).** The abbey's own
    history page speaks of a "reopening", which suggests a break in the community. No dated source
    in hand settles when or for how long. The living flag stands with no descent grade. For the
    entry's owner: the "stood since about 410" line, once a source is found.
161. **Link grades that reflect sources, not a break in the church (2026-11-10).** On some lines (the
    Coptic and the Latin American among them), a "continued as" link is graded low because the tree
    lacks entries or sources for a period, not because the church broke. P2-V's descent grades no
    longer copy those link grades. For P2-L11: re-check them.
162. **Living marks that wait for a dated source (2026-11-10).** Four living flags have no dated item
    after 2010: Kongo Christianity to 1650, the Anti-Trinitarian currents (the Transylvanian church),
    the Schwenkfelders and the New France mission. They stay living, graded none, as the era 10 gate
    ruled for the same case. Wanted: a dated own-voice item for each. Also weak: about 30 own-voice
    items are rotating home pages, and every CR mark could reach CD with a verified independent
    source. For the source-research thread.
163. **Open questions the check left, and one line for another owner (2026-11-10).** Each verdict
    below was applied under the rule; the question is recorded here, not decided:
${questions.join("\n")}
    For the method page's owner: "What is still to come" still says the tenth era is not yet
    linked, though P2-L10 has linked it.
`;
writeFileSync(out, text);
console.log(`gaps ${gaps.length}, questions ${questions.length}`);
