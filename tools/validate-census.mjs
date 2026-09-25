#!/usr/bin/env node
// Census contract validator — Blueprint increment A2.b (§L Loop Protocol).
// Run on EVERY census edit: node tools/validate-census.mjs [path]
// Exits non-zero on any violation; prints each violation on its own line.
import { readFileSync } from "node:fs";

const path = process.argv[2] ?? "cic-website/data/world-census.json";
const errs = [];
const warn = [];
let d;
try { d = JSON.parse(readFileSync(path, "utf8")); }
catch (e) { console.error(`PARSE FAIL: ${e.message}`); process.exit(2); }

const EDGE_TYPES = new Set(["formed", "transmitted to", "argued against", "contemporary with", "in tension with"]);
const CONFIDENCE = new Set(["Documented", "Widely Accepted", "Contested"]);
const HEX = /^#[0-9A-Fa-f]{6}$/;

// --- eras ---
if (!Array.isArray(d.eras) || d.eras.length === 0) errs.push("eras: missing/empty");
const eraNums = new Set();
(d.eras ?? []).forEach(e => {
  eraNums.add(e.num);
  for (const k of ["no", "num", "title", "dates", "ground", "groundDark"])
    if (e[k] == null) errs.push(`era ${e.num ?? "?"}: missing ${k}`);
  if (e.ground && !HEX.test(e.ground)) errs.push(`era ${e.num}: bad ground hex`);
  if (e.groundDark && !HEX.test(e.groundDark)) errs.push(`era ${e.num}: bad groundDark hex`);
});

// --- movements ---
const byId = new Map();
(d.movements ?? []).forEach(m => {
  if (byId.has(m.id)) errs.push(`duplicate movement id: ${m.id}`);
  byId.set(m.id, m);
  for (const k of ["id", "atlasId", "era", "name", "dates", "start", "end", "laneOrder", "status", "statusWord"])
    if (m[k] == null) errs.push(`${m.id ?? m.atlasId ?? "?"}: missing ${k}`);
  if (typeof m.start === "number" && typeof m.end === "number" && m.start > m.end)
    errs.push(`${m.id}: start ${m.start} > end ${m.end}`);
  if (m.era != null && !eraNums.has(m.era)) errs.push(`${m.id}: unknown era ${m.era}`);
  if (m.status === "Built & Live" && !m.entry) errs.push(`${m.id}: Built & Live but no entry block`);
  if (m.shortName && m.shortName.length > 20) warn.push(`${m.id}: shortName >20 chars ("${m.shortName}")`);
  // Decision 7 (2026-09-25, Mark's ruling "a"): statusWord is plain words at
  // the source, never a build-stage tag - the "(Era N Step 0)" suffix this
  // check guards against was dropped fleet-wide from all 220 movements that
  // carried it, and must not come back.
  if (m.statusWord && (m.statusWord.includes("Step 0") || m.statusWord.includes("(Era ")))
    errs.push(`${m.id}: statusWord carries a build-stage tag ("${m.statusWord}") - plain words only`);
});

// --- edges ---
(d.edges ?? []).forEach((e, i) => {
  if (!byId.has(e.from)) errs.push(`edge[${i}]: unknown from ${e.from}`);
  if (!byId.has(e.to)) errs.push(`edge[${i}]: unknown to ${e.to}`);
  if (!EDGE_TYPES.has(e.type)) errs.push(`edge[${i}]: unknown type "${e.type}"`);
  if (!CONFIDENCE.has(e.confidence)) errs.push(`edge[${i}]: unknown confidence "${e.confidence}"`);
  if (!e.note) warn.push(`edge[${i}] ${e.from}->${e.to}: no note`);
});

// --- continuesAs: pairs exist, adjacent-era, successor starts no earlier than predecessor ---
(d.movements ?? []).forEach(m => {
  if (!m.continuesAs) return;
  const s = byId.get(m.continuesAs);
  if (!s) { errs.push(`${m.id}: continuesAs unknown id ${m.continuesAs}`); return; }
  const gap = s.era - m.era;
  if (gap < 0 || gap > 1) errs.push(`${m.id} -> ${s.id}: continuesAs spans era ${m.era}->${s.era} (must be same or adjacent)`);
  if (typeof s.start === "number" && typeof m.start === "number" && s.start < m.start)
    warn.push(`${m.id} -> ${s.id}: successor starts before predecessor`);
});

// --- meta consistency: counts must match the movements array (caught stale at the Era 5 survey, 2026-08-02) ---
if (d.meta) {
  const n = (d.movements ?? []).length;
  if (d.meta.totalEntries !== n) errs.push(`meta.totalEntries ${d.meta.totalEntries} != ${n} movements`);
  const live = (d.movements ?? []).filter(m => m.status === "Built & Live").length;
  if (d.meta.liveCount !== undefined && d.meta.liveCount !== live) errs.push(`meta.liveCount ${d.meta.liveCount} != ${live} Built & Live`);
  if (d.meta.statusCounts) {
    const sc = {};
    for (const m of d.movements ?? []) sc[m.status] = (sc[m.status] || 0) + 1;
    for (const [k, v] of Object.entries(d.meta.statusCounts))
      if (sc[k] !== v) errs.push(`meta.statusCounts["${k}"] ${v} != actual ${sc[k] ?? 0}`);
    for (const k of Object.keys(sc))
      if (!(k in d.meta.statusCounts)) errs.push(`meta.statusCounts missing status "${k}" (actual ${sc[k]})`);
  }
}

// --- report ---
warn.forEach(w => console.log("WARN  " + w));
errs.forEach(e => console.log("ERROR " + e));
console.log(`${path}: ${byId.size} movements, ${(d.edges ?? []).length} edges, ${(d.eras ?? []).length} eras — ${errs.length} errors, ${warn.length} warnings`);
process.exit(errs.length ? 1 : 0);
