#!/usr/bin/env node
// Census contract validator — Blueprint increment A2.b (§L Loop Protocol).
// Run on EVERY census edit: node tools/validate-census.mjs [path]
// Exits non-zero on any violation; prints each violation on its own line.
import { readFileSync, existsSync } from "node:fs";

const args = process.argv.slice(2);
const baseIdx = args.indexOf("--base");
const basePath = baseIdx >= 0 ? args[baseIdx + 1] : null;
if (baseIdx >= 0) args.splice(baseIdx, 2);
const treeIdx = args.indexOf("--tree");
const treeDir = treeIdx >= 0 ? args[treeIdx + 1] : null;
if (treeIdx >= 0) args.splice(treeIdx, 2);
const atlasIdx = args.indexOf("--atlas");
const atlasPath = atlasIdx >= 0 ? args[atlasIdx + 1] : null;
if (atlasIdx >= 0) args.splice(atlasIdx, 2);
const path = args[0] ?? "cic-website/data/world-census.json";
const errs = [];
const warn = [];
let d;
try { d = JSON.parse(readFileSync(path, "utf8")); }
catch (e) { console.error(`PARSE FAIL: ${e.message}`); process.exit(2); }

const EDGE_TYPES = new Set(["gave rise to", "continued as", "influenced", "argued against", "broke with", "in contact with"]);
const SYMMETRIC_TYPES = new Set(["broke with", "in contact with"]);
const MAJOR_BY_TYPE = new Set(["gave rise to", "continued as", "broke with"]);
const CONFIDENCE = new Set(["Documented", "Widely Accepted", "Dominant Modern Reconstruction", "Contested", "Inferential-Thin"]);
const SPECIFICITY = new Set(["A", "B", "C", "D", "E"]);
const VERIFICATION = new Set(["verified-direct", "verified-via-authority", "named-not-rechecked", "unverified"]);
const SOURCE_KINDS = new Set(["primary", "secondary"]);
const INTERNAL_NOTE = [/\.\.(?!\.)/, /\b(edges?|continuesAs|grade[ds]?)\b/i, /\b(the|this|our) census\b(?!\s+(recorded|listing|of\s+\d))/i, /\b[IVX]+\.\d+[a-z]?\b/];
const squash = s => s.replace(/\s+/g, " ").trim();
const textCache = new Map();
function textLines(file) {
  if (!textCache.has(file)) textCache.set(file, existsSync(file) ? readFileSync(file, "utf8").split("\n") : null);
  return textCache.get(file);
}
const HEX = /^#[0-9A-Fa-f]{6}$/;
// A movement's kind: absent means a church body; "cross-church movement" is a defined
// movement that runs across church bodies rather than being one.
const MOVEMENT_KINDS = new Set(["cross-church movement"]);

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
  if (m.kind !== undefined && !MOVEMENT_KINDS.has(m.kind))
    errs.push(`${m.id}: unknown kind "${m.kind}" (leave it off for a church body; allowed: ${[...MOVEMENT_KINDS].join(", ")})`);
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
const edgeIds = new Set();
(d.edges ?? []).forEach((e, i) => {
  const tag = `edge[${i}] ${e.id ?? `${e.from}->${e.to}`}`;
  if (!byId.has(e.from)) errs.push(`${tag}: unknown from ${e.from}`);
  if (!byId.has(e.to)) errs.push(`${tag}: unknown to ${e.to}`);
  if (!EDGE_TYPES.has(e.type)) errs.push(`${tag}: unknown type "${e.type}"`);
  if (!CONFIDENCE.has(e.confidence)) errs.push(`${tag}: unknown confidence "${e.confidence}"`);
  if (SYMMETRIC_TYPES.has(e.type) && !(e.from < e.to)) errs.push(`${tag}: "${e.type}" is symmetric; from and to must be in alphabetical order`);
  const pair = `${e.from}--${e.to}`;
  if (!e.id || !(e.id === pair || new RegExp(`^${pair.replace(/[-]/g, "\\-")}--[2-9]$`).test(e.id))) errs.push(`${tag}: id must be "${pair}" or "${pair}--N"`);
  if (edgeIds.has(e.id)) errs.push(`${tag}: duplicate id`);
  edgeIds.add(e.id);
  if (!e.note) errs.push(`${tag}: no note`);
  else INTERNAL_NOTE.forEach(rx => { if (rx.test(e.note)) errs.push(`${tag}: note carries internal text (${rx})`); });
  // Major links (Decision-Log 2026-11-08): lineage and breaks are major by type; any other
  // link is major only when it carries `outcome`, one plain sentence from its own sources.
  if (e.outcome !== undefined) {
    if (MAJOR_BY_TYPE.has(e.type)) errs.push(`${tag}: outcome is only for "influenced", "argued against" or "in contact with" links; "${e.type}" is major by type`);
    if (typeof e.outcome !== "string" || !e.outcome.trim()) errs.push(`${tag}: outcome must be a non-empty sentence, or left off`);
    else {
      INTERNAL_NOTE.forEach(rx => { if (rx.test(e.outcome)) errs.push(`${tag}: outcome carries internal text (${rx})`); });
      if (e.outcome.trim().split(/\s+/).length > 30) errs.push(`${tag}: outcome runs past 30 words`);
      if (!/[.!?]['’"”)]?$/.test(e.outcome.trim())) errs.push(`${tag}: outcome must end as a sentence`);
    }
  }
  if (!SPECIFICITY.has(e.citation_specificity)) errs.push(`${tag}: citation_specificity must be A-E`);
  if (!VERIFICATION.has(e.verification_state)) errs.push(`${tag}: unknown verification_state "${e.verification_state}"`);
  const sources = Array.isArray(e.sources) ? e.sources : [];
  if (!sources.length) errs.push(`${tag}: no sources`);
  sources.forEach((s, j) => {
    const st = `${tag} source[${j}]`;
    if (!SOURCE_KINDS.has(s.kind)) errs.push(`${st}: kind must be primary or secondary`);
    if (!s.work) errs.push(`${st}: no work`);
    // A secondary work held in cic/texts/ may carry file, lines and quote (Decision-Log
    // 2026-11-08, whole-set rulings): all three together, and the quote checked like a primary's.
    if (s.kind !== "primary") {
      const held = ["file", "lines", "quote"].filter(k => s[k]);
      if (!held.length) return;
      if (held.length < 3) { errs.push(`${st}: a secondary source with a file needs file, lines and quote together`); return; }
    } else {
      for (const k of ["file", "lines", "locus", "quote", "license"]) if (!s[k]) errs.push(`${st}: primary source missing ${k}`);
    }
    if (!s.file || !s.lines || !s.quote) return;
    if (!s.file.startsWith("cic/texts/")) { errs.push(`${st}: file must be under cic/texts/`); return; }
    const lines = textLines(s.file);
    if (!lines) { errs.push(`${st}: file not found ${s.file}`); return; }
    const m = /^(\d+)(?:-(\d+))?$/.exec(String(s.lines));
    if (!m) { errs.push(`${st}: lines must be "n" or "a-b"`); return; }
    const a = +m[1], b = +(m[2] ?? m[1]);
    if (a < 1 || b < a || b > lines.length) { errs.push(`${st}: lines ${s.lines} outside ${s.file}`); return; }
    const span = squash(lines.slice(a - 1, b).join(" "));
    if (!span.includes(squash(s.quote))) errs.push(`${st}: quote not found verbatim in ${s.file} lines ${s.lines}`);
  });
  if (e.confidence === "Documented") {
    if (!sources.some(s => s.kind === "primary")) errs.push(`${tag}: Documented needs a primary source`);
    if (e.verification_state !== "verified-direct") errs.push(`${tag}: Documented needs verification_state verified-direct`);
  }
  if ((e.confidence === "Widely Accepted" || e.confidence === "Dominant Modern Reconstruction") && !sources.some(s => s.kind === "secondary"))
    errs.push(`${tag}: ${e.confidence} needs a secondary source`);
});

// --- retired links and movements: never reused, replacements resolve ---
const retiredLinkIds = new Set();
(d.retiredLinks ?? []).forEach((r, i) => {
  if (!r.id || !r.date || !r.reason) errs.push(`retiredLinks[${i}]: needs id, date and reason`);
  if (edgeIds.has(r.id)) errs.push(`retiredLinks[${i}]: ${r.id} is retired but still in use`);
  if (retiredLinkIds.has(r.id)) errs.push(`retiredLinks[${i}]: duplicate ${r.id}`);
  retiredLinkIds.add(r.id);
  if (r.replacedBy && !edgeIds.has(r.replacedBy)) errs.push(`retiredLinks[${i}]: replacedBy ${r.replacedBy} is not a current link`);
});
const retiredMovementIds = new Set();
(d.retiredMovements ?? []).forEach((r, i) => {
  if (!r.id || !r.date || !r.reason) errs.push(`retiredMovements[${i}]: needs id, date and reason`);
  if (byId.has(r.id)) errs.push(`retiredMovements[${i}]: ${r.id} is retired but still in use`);
  retiredMovementIds.add(r.id);
  if (r.redirectTo && !byId.has(r.redirectTo)) errs.push(`retiredMovements[${i}]: redirectTo ${r.redirectTo} is not a current movement`);
});

// --- release and identifier promise ---
if (!d.meta?.release?.number || !/^\d{4}-\d{2}-\d{2}$/.test(d.meta?.release?.date ?? "")) errs.push("meta.release: needs number and date (YYYY-MM-DD)");
if (!d.meta?.identifiers) errs.push("meta.identifiers: the permanence statement is missing");

// --- permanence against a base version: nothing published disappears unretired ---
if (basePath) {
  let base = null;
  try { base = JSON.parse(readFileSync(basePath, "utf8")); } catch (e) { errs.push(`--base: cannot read ${basePath}: ${e.message}`); }
  if (base) {
    for (const e of base.edges ?? []) if (e.id && !edgeIds.has(e.id) && !retiredLinkIds.has(e.id)) errs.push(`link ${e.id} was published and is gone without a retiredLinks entry`);
    for (const m of base.movements ?? []) if (!byId.has(m.id) && !retiredMovementIds.has(m.id)) errs.push(`movement ${m.id} was published and is gone without a retiredMovements entry`);
    for (const r of base.retiredLinks ?? []) if (!retiredLinkIds.has(r.id)) errs.push(`retired link ${r.id} dropped from retiredLinks`);
    if (base.meta?.release?.number && base.meta.release.number === d.meta?.release?.number && JSON.stringify(base.edges) !== JSON.stringify(d.edges))
      errs.push("links changed but meta.release.number did not");
  }
}

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

// --- place labels: drawn only from the entry's own region text ---
function checkPlaceLabel(label, entry) {
  if (typeof entry.region !== "string" || !entry.region.trim()) { errs.push(`${label}: missing region`); return; }
  const p = entry.placeLabel;
  if (typeof p !== "string" || !p.trim()) { errs.push(`${label}: missing placeLabel`); return; }
  const parts = p.replace(/ and beyond$/, "").split(" · ");
  if (parts.length > 2) errs.push(`${label}: placeLabel names more than two places`);
  let from = 0;
  for (const part of parts) {
    const at = entry.region.indexOf(part, from);
    if (!part.trim() || at < 0) errs.push(`${label}: placeLabel "${part}" is not in its region text`);
    else from = at + part.length;
  }
  for (const [place, words] of Object.entries(entry.placeQualifiers ?? {})) {
    if (!parts.includes(place)) errs.push(`${label}: place qualifier for "${place}", which is not on the place label`);
    if (typeof words !== "string" || !words.trim()) errs.push(`${label}: empty place qualifier for "${place}"`);
  }
  if (!Array.isArray(entry.modernCountries)) { errs.push(`${label}: modernCountries missing (an empty list when no country applies)`); return; }
  for (const c of entry.modernCountries) {
    if (!c || typeof c.country !== "string" || !c.country.trim()) errs.push(`${label}: a modern country has no name`);
    if (!/^Q\d+$/.test(c?.countryId ?? "")) errs.push(`${label}: modern country "${c?.country}" has no Wikidata ID`);
    if (!/^Q\d+$/.test(c?.placeId ?? "")) errs.push(`${label}: modern country "${c?.country}" has no source place ID`);
    if (!parts.includes(c?.place)) errs.push(`${label}: modern country "${c?.country}" comes from "${c?.place}", which is not on the place label`);
  }
}
(d.movements ?? []).forEach(m => checkPlaceLabel(m.id, m));
if (atlasPath) {
  const html = readFileSync(atlasPath, "utf8");
  const at = html.indexOf('"stories":', html.indexOf("const DATA"));
  const open = html.indexOf("[", at);
  let depth = 0, end = open;
  for (; end < html.length; end++) { if (html[end] === "[") depth++; else if (html[end] === "]" && --depth === 0) break; }
  JSON.parse(html.slice(open, end + 1)).forEach(s => checkPlaceLabel(`story ${s.id}`, s));
}

// --- tree pages: every promised address resolves, every link has its anchor ---
if (treeDir) {
  const page = id => { const f = `${treeDir}/${id}.html`; return existsSync(f) ? readFileSync(f, "utf8") : null; };
  for (const m of d.movements ?? []) if (page(m.id) === null) errs.push(`${m.id}: no tree page at ${treeDir}/${m.id}.html`);
  for (const r of d.retiredMovements ?? []) if (r.redirectTo && page(r.redirectTo) === null) errs.push(`retired ${r.id}: its redirect target ${r.redirectTo} has no tree page`);
  for (const e of d.edges ?? []) {
    for (const end of [e.from, e.to]) {
      const html = page(end);
      if (html !== null && !html.includes(`id="${e.id}"`)) errs.push(`${e.id}: no anchor on the ${end} tree page`);
    }
  }
}

// --- report ---
warn.forEach(w => console.log("WARN  " + w));
errs.forEach(e => console.log("ERROR " + e));
console.log(`${path}: ${byId.size} movements, ${(d.edges ?? []).length} edges, ${(d.eras ?? []).length} eras — ${errs.length} errors, ${warn.length} warnings`);
process.exit(errs.length ? 1 : 0);
