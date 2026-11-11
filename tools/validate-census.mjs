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

const EDGE_TYPES = new Set(["gave rise to", "continued as", "influenced", "argued against", "broke with", "in contact with", "member of"]);
const SYMMETRIC_TYPES = new Set(["broke with", "in contact with"]);
const MAJOR_BY_TYPE = new Set(["gave rise to", "continued as", "broke with"]);
const CONFIDENCE = new Set(["Documented", "Widely Accepted", "Dominant Modern Reconstruction", "Contested", "Inferential-Thin"]);
const SPECIFICITY = new Set(["A", "B", "C", "D", "E"]);
const VERIFICATION = new Set(["verified-direct", "verified-online", "verified-via-authority", "named-not-rechecked", "unverified"]);
const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/;
const SOURCE_KINDS = new Set(["primary", "secondary"]);
const INTERNAL_NOTE = [/\.\.(?!\.)/, /\b(edges?|continuesAs|grade[ds]?)\b/i, /\b(the|this|our) census\b(?!\s+(recorded|listing|of\s+\d))/i, /\b[IVX]+\.\d+[a-z]?\b/];
const squash = s => s.replace(/\s+/g, " ").trim();
const textCache = new Map();
function textLines(file) {
  if (!textCache.has(file)) textCache.set(file, existsSync(file) ? readFileSync(file, "utf8").split("\n") : null);
  return textCache.get(file);
}
// A quote from a Library file must stand verbatim (whitespace aside) in the cited lines.
function checkHeldQuote(st, s) {
  if (!s.file.startsWith("cic/texts/")) { errs.push(`${st}: file must be under cic/texts/`); return; }
  const lines = textLines(s.file);
  if (!lines) { errs.push(`${st}: file not found ${s.file}`); return; }
  const m = /^(\d+)(?:-(\d+))?$/.exec(String(s.lines));
  if (!m) { errs.push(`${st}: lines must be "n" or "a-b"`); return; }
  const a = +m[1], b = +(m[2] ?? m[1]);
  if (a < 1 || b < a || b > lines.length) { errs.push(`${st}: lines ${s.lines} outside ${s.file}`); return; }
  const span = squash(lines.slice(a - 1, b).join(" "));
  if (!span.includes(squash(s.quote))) errs.push(`${st}: quote not found verbatim in ${s.file} lines ${s.lines}`);
}
const HEX = /^#[0-9A-Fa-f]{6}$/;
// A movement's kind: absent means a church body; "cross-church movement" is a defined
// movement that runs across church bodies rather than being one; "person" is a person
// entry (Decision-Log 2026-11-06, ruling 14).
const MOVEMENT_KINDS = new Set(["cross-church movement", "person"]);

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
    // A church joining a council is membership, not a rule changed (Decision-Log 2026-11-10, "a seventh link type").
    if (e.type === "member of") errs.push(`${tag}: outcome is only for "influenced", "argued against" or "in contact with" links; "member of" is never major`);
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
    // A source read online (Decision-Log 2026-11-10, "Change order: evidence for era 10 links"):
    // a web address and the date it was read stand in for a Library file. It cannot be re-checked
    // in the Library, so a link resting on it can never be Documented (checked below).
    if (s.url !== undefined || s.accessed !== undefined) {
      if (s.file || s.lines) errs.push(`${st}: a source read online carries url and accessed, not file and lines`);
      if (typeof s.url !== "string" || !/^https:\/\/\S+$/.test(s.url)) errs.push(`${st}: url must be an https address`);
      if (typeof s.accessed !== "string" || !ISO_DATE.test(s.accessed)) errs.push(`${st}: accessed must be the date read, YYYY-MM-DD`);
      if (s.kind === "primary") for (const k of ["locus", "quote", "license"]) if (!s[k]) errs.push(`${st}: primary source read online missing ${k}`);
      return;
    }
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
    checkHeldQuote(st, s);
  });
  if (e.confidence === "Documented") {
    if (!sources.some(s => s.kind === "primary")) errs.push(`${tag}: Documented needs a primary source`);
    if (e.verification_state !== "verified-direct") errs.push(`${tag}: Documented needs verification_state verified-direct`);
    if (!sources.some(s => s.kind === "primary" && s.file && !s.url)) errs.push(`${tag}: Documented needs a primary source held in the Library, not only read online`);
  }
  // A "member of" link may be Widely Accepted on the council's or member's own dated membership
  // record alone (Decision-Log 2026-11-10, "The grade of a 'member of' link"): a primary suffices.
  const memberOnRecord = e.type === "member of" && e.confidence === "Widely Accepted" && sources.some(s => s.kind === "primary");
  if ((e.confidence === "Widely Accepted" || e.confidence === "Dominant Modern Reconstruction") && !sources.some(s => s.kind === "secondary") && !memberOnRecord)
    errs.push(`${tag}: ${e.confidence} needs a secondary source`);
});

// --- entry kinds, people and review status (Decision-Log 2026-11-06 rulings 14 and 18; 2026-11-09, "The gap sweep ruled") ---
const REVIEW = new Set(["AI-checked", "partner-contributed", "scholar-reviewed"]);
const isPerson = m => m?.kind === "person";
const yearOf = item => item.person ? byId.get(item.person)?.start : item.year;
// A held voice names a row on the movement's own Library shelf (cic/corpus-map/<id>.yaml) and that row's author.
const shelfCache = new Map();
function shelfAuthor(movementId, rowId) {
  if (!shelfCache.has(movementId)) {
    const f = `cic/corpus-map/${movementId}.yaml`;
    const rows = new Map();
    if (existsSync(f)) {
      let row = null;
      for (const line of readFileSync(f, "utf8").split("\n")) {
        const r = /^- row_id: (.+)$/.exec(line);
        if (r) { row = r[1].trim(); rows.set(row, null); continue; }
        const a = /^  author: (.+)$/.exec(line);
        if (a && row && rows.get(row) === null) rows.set(row, a[1].trim());
      }
    }
    shelfCache.set(movementId, rows);
  }
  return shelfCache.get(movementId).get(rowId);
}
// A person card: one-line summary, role, up to three key works, legacy, open questions and the sources behind it.
const CARD_KEYS = ["knownFor", "role", "keyWorks", "legacy", "uncertain", "sources"];
const plain = x => typeof x === "string" && x.trim() !== "";
const isObj = x => x !== null && typeof x === "object" && !Array.isArray(x);
function checkCard(m) {
  const at = p => `${m.id}: card.${p}`;
  const card = m.card;
  if (!isPerson(m)) { errs.push(`${m.id}: card is only for a person entry`); return; }
  if (!isObj(card)) { errs.push(`${m.id}: card must be an object`); return; }
  Object.keys(card).filter(k => !CARD_KEYS.includes(k)).forEach(k => errs.push(`${at(k)} is not allowed (allowed: ${CARD_KEYS.join(", ")})`));
  const text = (obj, key, path) => { if (obj[key] !== undefined && !plain(obj[key])) errs.push(`${at(path)} must be a non-empty string`); };
  const strings = (list, path) => {
    if (!Array.isArray(list)) errs.push(`${at(path)} must be a list of non-empty strings`);
    else list.forEach((x, i) => { if (!plain(x)) errs.push(`${at(`${path}[${i}]`)} must be a non-empty string`); });
  };
  const only = (obj, allowed, path) => Object.keys(obj).filter(k => !allowed.includes(k)).forEach(k => errs.push(`${at(`${path}.${k}`)} is not allowed (allowed: ${allowed.join(", ")})`));
  text(card, "knownFor", "knownFor");
  text(card, "role", "role");
  if (card.keyWorks !== undefined) {
    if (!Array.isArray(card.keyWorks)) errs.push(`${at("keyWorks")} must be a list`);
    else {
      if (card.keyWorks.length > 3) errs.push(`${at("keyWorks")} holds at most 3 works, has ${card.keyWorks.length}`);
      card.keyWorks.forEach((w, i) => {
        if (!isObj(w)) { errs.push(`${at(`keyWorks[${i}]`)} must be an object with title and about`); return; }
        only(w, ["title", "about"], `keyWorks[${i}]`);
        ["title", "about"].forEach(k => { if (!plain(w[k])) errs.push(`${at(`keyWorks[${i}].${k}`)} must be a non-empty string`); });
      });
    }
  }
  if (card.legacy !== undefined) {
    if (!isObj(card.legacy)) errs.push(`${at("legacy")} must be an object with traces and remembered`);
    else {
      only(card.legacy, ["traces", "remembered"], "legacy");
      ["traces", "remembered"].forEach(k => { if (card.legacy[k] !== undefined) strings(card.legacy[k], `legacy.${k}`); });
    }
  }
  if (card.uncertain !== undefined) strings(card.uncertain, "uncertain");
  if (card.sources !== undefined) {
    if (!isObj(card.sources)) { errs.push(`${at("sources")} must be an object with ownWords and about`); return; }
    only(card.sources, ["ownWords", "about"], "sources");
    const listing = (key, required, extra) => {
      const items = card.sources[key];
      if (items === undefined) return;
      if (!Array.isArray(items)) { errs.push(`${at(`sources.${key}`)} must be a list`); return; }
      items.forEach((s, i) => {
        const path = `sources.${key}[${i}]`;
        if (!isObj(s)) { errs.push(`${at(path)} must be an object`); return; }
        only(s, [...required, ...extra], path);
        required.filter(k => k !== "author").forEach(k => { if (!plain(s[k])) errs.push(`${at(`${path}.${k}`)} must be a non-empty string`); });
        if (key === "about" && s.author !== null && !plain(s.author)) errs.push(`${at(`${path}.author`)} must be a non-empty string, or null for a work with no named author`);
        if (plain(s.file) && !(s.file.startsWith("cic/texts/") && existsSync(s.file))) errs.push(`${at(`${path}.file`)} ${s.file} must be an existing file under cic/texts/`);
        if (s.disputed !== undefined && !plain(s.disputed)) errs.push(`${at(`${path}.disputed`)} must be a non-empty string`);
        if (key === "about" && s.date !== null && !plain(s.date)) errs.push(`${at(`${path}.date`)} must be a string or null`);
      });
    };
    listing("ownWords", ["title", "file", "language"], ["disputed"]);
    listing("about", ["title", "author", "language", "file"], ["date"]);
  }
}
(d.movements ?? []).forEach(m => {
  if (isPerson(m)) {
    if (!("toldWithin" in m)) errs.push(`${m.id}: a person entry needs toldWithin (a movement ID, or null)`);
    else if (m.toldWithin !== null) {
      const home = byId.get(m.toldWithin);
      if (!home) errs.push(`${m.id}: toldWithin ${m.toldWithin} is not a movement`);
      else if (isPerson(home)) errs.push(`${m.id}: toldWithin ${m.toldWithin} is a person, not a movement`);
      else if (!(home.people ?? []).some(p => p.person === m.id)) errs.push(`${m.id}: missing from the people list of ${m.toldWithin}`);
    }
    if (m.people !== undefined) errs.push(`${m.id}: a person entry has no people list`);
  } else {
    if ("toldWithin" in m) errs.push(`${m.id}: toldWithin is only for a person entry`);
    if (!Array.isArray(m.people)) errs.push(`${m.id}: people must be a list (empty when it names no one)`);
    else if (!m.people.length && (typeof m.peopleNote !== "string" || !m.peopleNote.trim())) errs.push(`${m.id}: names no one, so it needs peopleNote, one plain sentence saying why`);
    else if (m.people.length && m.peopleNote !== undefined) errs.push(`${m.id}: peopleNote is only for a movement that names no one`);
  }
  if (isPerson(m) && m.peopleNote !== undefined) errs.push(`${m.id}: a person entry has no peopleNote`);
  if (m.card !== undefined) checkCard(m);
  if (!REVIEW.has(m.reviewStatus)) errs.push(`${m.id}: reviewStatus must be "AI-checked", "partner-contributed" or "scholar-reviewed"`);
  if (m.livingEvidence?.descentConfidence !== undefined) {
    if (!CONFIDENCE.has(m.livingEvidence.descentConfidence)) errs.push(`${m.id}: livingEvidence.descentConfidence must be one of the five formation_confidence levels`);
    if (m.living !== true) errs.push(`${m.id}: livingEvidence.descentConfidence grades a living tradition, but living is not true`);
    if (typeof m.livingEvidence.basis !== "string" || !m.livingEvidence.basis.trim()) errs.push(`${m.id}: livingEvidence.descentConfidence needs livingEvidence.basis, what the grade rests on`);
  }
  // The living mark (Decision-Log 2026-11-10, "What 'living' means"): every living tradition says what
  // the mark rests on, and either names the entries that carry it today or holds its own graded evidence.
  if (m.living === true && !isPerson(m)) {
    const ev = m.livingEvidence;
    if (typeof ev?.basis !== "string" || !ev.basis.trim()) errs.push(`${m.id}: living, so it needs livingEvidence.basis, what the mark rests on`);
    else if (ev.carrier === undefined && !/^(CD|CR|none)\b/.test(ev.grade ?? "")) errs.push(`${m.id}: living, so livingEvidence needs a carrier or its own grade (CD, CR or none)`);
  }
  if (m.livingEvidence?.carrier !== undefined) {
    const carrier = m.livingEvidence.carrier;
    if (!Array.isArray(carrier) || !carrier.length) errs.push(`${m.id}: livingEvidence.carrier must be a list of movement IDs`);
    else carrier.forEach(id => {
      const c = byId.get(id);
      if (!c || isPerson(c)) errs.push(`${m.id}: livingEvidence.carrier ${id} is not a movement`);
      else if (id === m.id) errs.push(`${m.id}: livingEvidence.carrier names the entry itself`);
      else if (c.living !== true) errs.push(`${m.id}: livingEvidence.carrier ${id} is not living`);
      else if (c.livingEvidence?.carrier !== undefined) errs.push(`${m.id}: livingEvidence.carrier ${id} is carried by another entry; name the entry that holds the evidence`);
    });
    if (m.living !== true) errs.push(`${m.id}: livingEvidence.carrier is only for a living tradition`);
  }
  const seen = new Set();
  let last = -Infinity;
  (Array.isArray(m.people) ? m.people : []).forEach((p, j) => {
    const pt = `${m.id} people[${j}]`;
    if (p.person !== undefined) {
      const who = byId.get(p.person);
      if (!isPerson(who)) errs.push(`${pt}: ${p.person} is not a person entry`);
      else if (who.toldWithin !== m.id) errs.push(`${pt}: ${p.person} is told within ${who.toldWithin}, not here`);
      if (Object.keys(p).length !== 1) errs.push(`${pt}: a person entry is named by its ID alone`);
    } else {
      if (typeof p.name !== "string" || !p.name.trim()) errs.push(`${pt}: a named voice needs a name`);
      if (!Number.isInteger(p.year)) errs.push(`${pt}: a named voice needs a whole-number year`);
      const line = (m.voices ?? [])[p.voice];
      if (typeof line !== "string") errs.push(`${pt}: voice must be the index of a line in voices`);
      else if (p.name && !line.includes(p.name)) errs.push(`${pt}: "${p.name}" is not named in voices[${p.voice}]`);
      if ((p.held === undefined) === (p.source === undefined)) errs.push(`${pt}: a named voice needs held (a Library row of their words) or source (a quote of their words), one of the two`);
      if (p.held !== undefined) {
        const author = shelfAuthor(m.id, p.held);
        if (author === undefined) errs.push(`${pt}: held ${p.held} is not a row on the ${m.id} Library shelf`);
        else if (!p.author || author !== p.author) errs.push(`${pt}: held row ${p.held} is by ${author}, not by the voice's author ${p.author}`);
      }
      const twin = (m.people ?? []).map(q => q.person && byId.get(q.person)).filter(Boolean)
        .find(w => p.name && [w.shortName, w.name].some(n => n && new RegExp(`(^|\\W)${n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}(\\W|$)`).test(p.name)));
      if (twin) errs.push(`${pt}: ${p.name} is already in this row as the person entry ${twin.id}`);
      if (p.source !== undefined) {
        const s = p.source;
        if (!s.work || !s.file || !s.lines || !s.quote) errs.push(`${pt}: source needs work, file, lines and quote`);
        else {
          const lines = s.file.startsWith("cic/texts/") ? textLines(s.file) : null;
          const r = /^(\d+)(?:-(\d+))?$/.exec(String(s.lines));
          if (!lines || !r) errs.push(`${pt}: source ${s.file} lines ${s.lines} not found under cic/texts/`);
          else if (!squash(lines.slice(+r[1] - 1, +(r[2] ?? r[1])).join(" ")).includes(squash(s.quote))) errs.push(`${pt}: quote not found verbatim in ${s.file} lines ${s.lines}`);
        }
      }
    }
    const key = p.person ?? p.name;
    if (seen.has(key)) errs.push(`${pt}: ${key} is listed twice`);
    seen.add(key);
    const y = yearOf(p);
    if (typeof y === "number") { if (y < last) errs.push(`${pt}: the people list is not in date order`); last = y; }
  });
});
(d.edges ?? []).forEach((e, i) => {
  if (e.concerns === undefined) return;
  const tag = `edge[${i}] ${e.id}`;
  const who = byId.get(e.concerns);
  if (typeof e.concerns !== "string" || !isPerson(who)) { errs.push(`${tag}: concerns ${e.concerns} is not a person entry`); return; }
  const names = [who.shortName, who.name].filter(Boolean);
  const texts = [e.note ?? "", ...(e.sources ?? []).map(s => s.quote ?? "")];
  if (!names.some(n => texts.some(t => t.includes(n)))) errs.push(`${tag}: concerns ${e.concerns}, but neither its note nor a source quote names ${names.join(" or ")}`);
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
  if (!r.redirectTo && !r.name) errs.push(`retiredMovements[${i}]: ${r.id} keeps its own retired page, which needs the movement's name`);
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
  checkRiverOrigins(html);
}

// --- river origins: where each river leaves its parent ---
// A river's first movements are all its church bodies tied at its earliest start. Its parent is
// the river of the strongest descent link into them: "gave rise to" or "continued as" (lineage)
// before "broke with" (a break, counted only from a movement that started earlier); then a major
// link before a minor one; then higher confidence; then the parent's earlier start, its id, and
// the link's id. "influenced" and other links never decide it. With no such link the page's
// record declares the parent, with its reason and source. The record must match this rule.
function riverOriginLink(lane, bodies) {
  const members = bodies.filter(m => m.laneOrder === lane);
  const first = Math.min(...members.map(m => m.start));
  const genesis = new Set(members.filter(m => m.start === first).map(m => m.id));
  const body = new Map(bodies.map(m => [m.id, m]));
  const conf = [...CONFIDENCE];
  const found = [];
  for (const e of d.edges ?? []) {
    let other = null, rank = null;
    if ((e.type === "gave rise to" || e.type === "continued as") && genesis.has(e.to)) { other = e.from; rank = 0; }
    else if (e.type === "broke with" && (genesis.has(e.to) || genesis.has(e.from))) { other = genesis.has(e.to) ? e.from : e.to; rank = 1; }
    const o = body.get(other);
    if (!o || o.laneOrder === lane || (rank === 1 && o.start >= first)) continue;
    const major = MAJOR_BY_TYPE.has(e.type) || !!e.outcome ? 0 : 1;
    found.push({ e, o, key: [rank, major, conf.indexOf(e.confidence), o.start] });
  }
  found.sort((x, y) => {
    for (let i = 0; i < x.key.length; i++) if (x.key[i] !== y.key[i]) return x.key[i] - y.key[i];
    return x.o.id < y.o.id ? -1 : x.o.id > y.o.id ? 1 : x.e.id < y.e.id ? -1 : x.e.id > y.e.id ? 1 : 0;
  });
  return found[0] ?? null;
}
function checkRiverOrigins(html) {
  const at = html.indexOf("const RIVER_ORIGINS = ");
  if (at < 0) { errs.push("river origins: the page has no RIVER_ORIGINS record"); return; }
  const start = at + "const RIVER_ORIGINS = ".length;
  let record;
  try { record = JSON.parse(html.slice(start, html.indexOf("\n;\n", start))); }
  catch (e) { errs.push(`river origins: RIVER_ORIGINS does not parse: ${e.message}`); return; }
  const bodies = (d.movements ?? []).filter(m => !m.kind);
  const lanes = [...new Set(bodies.map(m => m.laneOrder))].sort((a, b) => a - b);
  const byLane = new Map();
  for (const o of record) {
    const rt = `river origin ${o.lane}`;
    if (byLane.has(o.lane)) errs.push(`${rt}: listed twice`);
    byLane.set(o.lane, o);
    if (!lanes.includes(o.lane)) errs.push(`${rt}: no river has this lane`);
  }
  for (const lane of lanes) {
    const o = byLane.get(lane), rt = `river origin ${lane}`;
    if (!o) { errs.push(`${rt}: the record has no entry for this river`); continue; }
    if (lane === 0) {
      if (o.basis !== "origin" || o.parent !== null) errs.push(`${rt}: the origin trunk has basis "origin" and parent null`);
      continue;
    }
    const pick = riverOriginLink(lane, bodies);
    if (pick) {
      if (o.basis !== "lineage" || o.link !== pick.e.id || o.parent !== pick.o.laneOrder)
        errs.push(`${rt}: the strongest descent link is ${pick.e.id} (${pick.e.type}, from river ${pick.o.laneOrder}); the record must say basis "lineage", link ${pick.e.id}, parent ${pick.o.laneOrder}`);
      continue;
    }
    if (o.basis !== "declared") { errs.push(`${rt}: no descent link reaches this river's first movements, so its parent must be declared`); continue; }
    if (!lanes.includes(o.parent)) errs.push(`${rt}: parent ${o.parent} is not a river`);
    if (typeof o.reason !== "string" || !o.reason.trim()) errs.push(`${rt}: a declared parent needs its reason`);
    if (!CONFIDENCE.has(o.confidence)) errs.push(`${rt}: a declared parent needs a confidence on the five-level scale`);
    if (!Array.isArray(o.sources) || !o.sources.length) errs.push(`${rt}: a declared parent needs a source`);
    (o.sources ?? []).forEach((s, j) => {
      const st = `${rt} source[${j}]`;
      if (!SOURCE_KINDS.has(s.kind)) errs.push(`${st}: kind must be primary or secondary`);
      if (!s.work) errs.push(`${st}: no work`);
      if (s.kind === "primary") for (const k of ["file", "lines", "locus", "quote"]) if (!s[k]) errs.push(`${st}: primary source missing ${k}`);
      if (s.file || s.lines || s.quote) {
        if (!s.file || !s.lines || !s.quote) errs.push(`${st}: file, lines and quote go together`);
        else checkHeldQuote(st, s);
      }
    });
  }
  for (const lane of lanes) {
    const seen = new Set();
    let k = lane;
    while (k !== 0 && byLane.get(k) && !seen.has(k)) { seen.add(k); k = byLane.get(k).parent; }
    if (k !== 0 && byLane.has(k)) errs.push(`river origin ${lane}: following its parents never reaches the origin trunk`);
    const parent = byLane.get(lane)?.parent;
    const firstOf = l => Math.min(...bodies.filter(m => m.laneOrder === l).map(m => m.start));
    if (lane !== 0 && lanes.includes(parent) && firstOf(parent) > firstOf(lane)) errs.push(`river origin ${lane}: its parent river ${parent} starts later than it does`);
  }
}

// --- tree pages: every promised address resolves, every link has its anchor ---
if (treeDir) {
  const page = id => { const f = `${treeDir}/${id}.html`; return existsSync(f) ? readFileSync(f, "utf8") : null; };
  for (const m of d.movements ?? []) if (page(m.id) === null) errs.push(`${m.id}: no tree page at ${treeDir}/${m.id}.html`);
  const redirectsFile = `${treeDir}/../_redirects`;
  const redirects = existsSync(redirectsFile) ? readFileSync(redirectsFile, "utf8").split("\n").map(l => l.trim().split(/\s+/)) : [];
  for (const r of d.retiredMovements ?? []) {
    if (r.redirectTo) {
      if (page(r.redirectTo) === null) errs.push(`retired ${r.id}: its redirect target ${r.redirectTo} has no tree page`);
      if (page(r.id) !== null) errs.push(`retired ${r.id}: its old page still stands in ${treeDir}, so the redirect would never be reached`);
      for (const from of [`/tree/${r.id}`, `/tree/${r.id}.html`])
        if (!redirects.some(([a, b, code]) => a === from && b === `/tree/${r.redirectTo}` && code === "301")) errs.push(`retired ${r.id}: _redirects has no "${from} /tree/${r.redirectTo} 301" line`);
      continue;
    }
    const html = page(r.id);
    if (html === null) errs.push(`retired ${r.id}: no retired page at ${treeDir}/${r.id}.html`);
    else if (!html.includes('data-retired="true"')) errs.push(`retired ${r.id}: its tree page still serves the old entry, not the retired notice`);
  }
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
