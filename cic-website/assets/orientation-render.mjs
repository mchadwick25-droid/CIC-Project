/**
 * Shared renderer: world_front-compiled JSON (engine.m2.site_compiler's
 * output, cic-website/data/worlds/<census_id>.json) -> participant-facing
 * HTML fragments.
 *
 * Website V2 world_front design, approved to proceed, site cutover
 * stage. This is the ONE place the Orientation-tier content
 * (story/documented_stories/voices/floor_note/legacy/relations_summary/
 * sourcing/read_first) and the Narrative-tier content (who_speaks/quiet/
 * questions/glossary/pull_quotes) turn into HTML, so the Atlas panel
 * (cic-website/atlas-v3.html, fetched at runtime for the 8 built worlds)
 * and each static tradition page (cic-website/traditions/<slug>.html,
 * generated once by tools/generate_tradition_pages.py, which runs this
 * same file through Node) can never quietly drift apart into two
 * independently-maintained templates - the exact anti-pattern this
 * design exists to retire.
 *
 * Plain ES module, no build step: runs unmodified in a browser via
 * `<script type="module">` and in Node via `import`/`node --input-type=module`.
 * No DOM access anywhere in this file - every function returns an HTML
 * string, so it works the same in both environments.
 */

export function escapeHtml(s) {
  if (s === null || s === undefined) return "";
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function paragraphs(text) {
  if (!text) return "";
  return String(text)
    .split(/\n\n+/)
    .map((p) => `<p>${escapeHtml(p.trim())}</p>`)
    .join("\n");
}

// A figure's own in-world name (falls back to the first name entry, then
// the record id) - never the parenthetical scholarly form, which belongs
// in a hover/detail context, not as a figure's headline name here.
function figureName(figure) {
  if (!figure) return "";
  const names = figure.names || [];
  const inWorld = names.find((n) => n.tag === "in-world");
  if (inWorld) return inWorld.name;
  if (names.length) return names[0].name;
  return figure.id || "";
}

function figureDateSpan(figure) {
  if (!figure || !figure.dates) return "";
  const d = figure.dates;
  if (d.born && d.died) return `${d.born.split(" (")[0]}–${d.died.split(" (")[0]}`;
  if (d.died) return d.died.split(" (")[0];
  if (d.born) return d.born.split(" (")[0];
  return "";
}

// ---- Orientation tier (shared between the Atlas panel and a tradition page) ----

export function renderStory(compiled) {
  const story = (compiled.orientation && compiled.orientation.story) || [];
  return story.map((unit) => paragraphs(unit.text)).join("\n");
}

export function renderVoices(compiled, opts) {
  const showHedge = !opts || opts.showHedge !== false;
  const voices = (compiled.orientation && compiled.orientation.voices) || [];
  if (!voices.length) return "";
  const blocks = voices.map((v) => {
    const name = figureName(v.figure);
    const dates = figureDateSpan(v.figure);
    const heading = dates ? `${escapeHtml(name)} <span class="orient-voice-dates">(${escapeHtml(dates)})</span>` : escapeHtml(name);
    const lines = [
      '<div class="orient-voice">',
      `<p class="orient-voice-name">${heading}</p>`,
      paragraphs(v.text).replace(/^<p>/, '<p class="orient-voice-text">'),
    ];
    if (showHedge && v.hedge) {
      lines.push(`<p class="orient-voice-hedge"><span class="orient-hedge-label">This world's own hedge:</span> ${escapeHtml(v.hedge)}</p>`);
    }
    lines.push("</div>");
    return lines.join("\n");
  });
  return ['<div class="orient-voices">', ...blocks, "</div>"].join("\n");
}

// title/when/teaser are always visible - only the full text (the actual
// documented account) sits behind the disclosure. Reuses atlas-v3.html's
// own docstory-item/docstory naming convention for visual consistency,
// but not its exact hide/show split: the Atlas panel's own pre-existing
// pattern puts the teaser behind a hover tooltip on the collapsed
// summary, while this shared renderer (used by both surfaces, so they
// can't drift apart) keeps the teaser always in view per this content
// design's own explicit rule - a deeper click is for the full account,
// not for the one-line hook that gets a reader there.
export function renderDocumentedStories(compiled, opts) {
  const idPrefix = (opts && opts.idPrefix) || "ds";
  const stories = (compiled.orientation && compiled.orientation.documented_stories) || [];
  if (!stories.length) return "";
  const entries = stories.map((s, i) => {
    const detailsId = `${idPrefix}-${i}`;
    const head = [`<h4>${escapeHtml(s.title || "")}</h4>`];
    if (s.when) head.push(`<p class="meta">${escapeHtml(s.when)}</p>`);
    if (s.teaser) head.push(`<p class="teaser">${escapeHtml(s.teaser)}</p>`);
    const body = s.text ? paragraphs(s.text) : "";
    return [
      '<div class="docstory-entry">',
      ...head,
      `<details class="docstory-item" id="${detailsId}">`,
      '<summary><span class="docstory-title">Read the full account</span></summary>',
      `<div class="docstory">${body}</div>`,
      "</details>",
      "</div>",
    ].join("\n");
  });
  return ['<div class="docstories-row">', ...entries, "</div>"].join("\n");
}

export function renderFloorNote(compiled) {
  const fn = compiled.orientation && compiled.orientation.floor_note;
  if (!fn || !fn.text) return "";
  return paragraphs(fn.text);
}

export function renderLegacy(compiled) {
  const legacy = (compiled.orientation && compiled.orientation.legacy) || [];
  return legacy.map((unit) => paragraphs(unit.text)).join("\n");
}

export function renderRelationsSummary(compiled) {
  const rs = compiled.orientation && compiled.orientation.relations_summary;
  if (!rs || !rs.text) return "";
  return `<p class="orient-relations"><i>${escapeHtml(rs.text)}</i></p>`;
}

export function renderSourcing(compiled) {
  const orientation = compiled.orientation || {};
  const sourcing = orientation.sourcing;
  const readFirst = orientation.read_first || [];
  const parts = [];
  if (sourcing && sourcing.text) parts.push(`<p>${escapeHtml(sourcing.text)}</p>`);
  if (readFirst.length) {
    const items = readFirst.map((entry) => {
      const source = entry.source || {};
      const work = [source.author, source.work].filter(Boolean).join(", ");
      const note = entry.note ? ` <span class="orient-read-first-note">${escapeHtml(entry.note)}</span>` : "";
      return `<li><span class="orient-read-first-work">${escapeHtml(work)}</span>${note}</li>`;
    });
    parts.push(['<ul class="orient-read-first">', ...items, "</ul>"].join("\n"));
  }
  return parts.join("\n");
}

// ---- Narrative tier (tradition-page-only sections) ----

export function renderWhoSpeaks(compiled) {
  const ws = (compiled.narrative && compiled.narrative.who_speaks) || {};
  if (!ws.text) return "";
  return paragraphs(ws.text);
}

export function renderQuiet(compiled) {
  const quiet = compiled.narrative && compiled.narrative.quiet;
  if (!quiet || !quiet.statement) return "";
  return paragraphs(quiet.statement);
}

// A `cite` entry resolves to a full record's own content field (a
// doctrinal_witness's `text`, an honest_limit's `statement`, etc - see
// engine/m2/site_compiler.py's own _CITE_TEXT_FIELD_BY_TYPE), not a short
// bibliographic locus, so there is no citation string in the compiled data
// to reproduce verbatim here. Rendered instead as a short, honestly-
// labeled excerpt of the record that actually grounds the question -
// never invented, never a fabricated citation form. The cut favors a
// sentence boundary within `maxLen` over an arbitrary word-boundary
// chop, so the excerpt reads as a complete thought rather than trailing
// off mid-clause; only when no sentence end falls in range does it fall
// back to the nearest word boundary. See this generator's own report for
// this judgment call.
// Most record_type values already read fine to a participant once
// underscores become spaces ("contested_claim" -> "contested claim").
// "gravity" is this project's own internal term (Doc_04 Gravity
// Discovery - a world's core theological conviction) and reads as
// jargon on its own, so it gets an explicit participant-facing label
// here rather than a hand-edited copy of the citation text, which
// would only need doing again on every recompile.
const RECORD_TYPE_LABELS = { gravity: "core conviction" };
function citeExcerpt(cite, maxLen) {
  if (!cite || !cite.text) return "";
  const rawType = cite.record_type || "";
  const label = RECORD_TYPE_LABELS[rawType] || rawType.replace(/_/g, " ");
  const full = cite.text.trim();
  let text = full;
  if (full.length > maxLen) {
    const window = full.slice(0, maxLen);
    const sentenceEnd = window.match(/^[\s\S]*[.!?](?=\s|$)/);
    if (sentenceEnd && sentenceEnd[0].length >= maxLen * 0.4) {
      text = sentenceEnd[0].trim();
    } else {
      text = window.replace(/\s+\S*$/, "").trim() + "…";
    }
  }
  return `${label ? escapeHtml(label) + ": " : ""}“${escapeHtml(text)}”`;
}

export function renderQuestions(compiled, ctx) {
  const questions = (compiled.narrative && compiled.narrative.questions) || [];
  if (!questions.length) return "";
  const slug = ctx.slug;
  const repName = ctx.representativeName;
  const items = questions
    .map((q) => {
      const exchange = (q.demonstration && q.demonstration.exchange) || [];
      const participantTurn = exchange.find((t) => t.speaker === "participant");
      if (!participantTurn) return "";
      const questionText = participantTurn.text;
      const from = (q.cite || []).map((c) => citeExcerpt(c, 160)).filter(Boolean).join(" &middot; ");
      const href = `../talk.html?worlds=${encodeURIComponent(slug)}&mode=interview&from=traditions%2F${encodeURIComponent(slug)}.html`;
      let li = `<li><a href="${href}" data-ask>${escapeHtml(questionText)}<span class="vh"> — ask ${escapeHtml(repName)}</span></a>`;
      if (from) li += `<span class="from">${from}</span>`;
      li += "</li>";
      return li;
    })
    .filter(Boolean)
    .join("\n");
  return `<ul class="questions">\n${items}\n</ul>`;
}

export function renderGlossary(compiled) {
  const glossary = (compiled.narrative && compiled.narrative.glossary) || [];
  if (!glossary.length) return "";
  const items = glossary.map(
    (t) => `<div class="orient-glossary-item"><dt>${escapeHtml(t.world_word)}</dt><dd>${escapeHtml(t.meaning)}</dd></div>`
  );
  return ['<dl class="orient-glossary">', ...items, "</dl>"].join("\n");
}

// A quote's own `speaker_or_author` arrives already resolved to a
// readable name - engine/m2/site_compiler.py's _resolve_quote() runs it
// through citation_cards.py's own figure-label lookup at compile time, so
// there is nothing left for this renderer to unwrap.
export function renderPullQuotes(compiled) {
  const quotes = (compiled.narrative && compiled.narrative.pull_quotes) || [];
  if (!quotes.length) return "";
  const blocks = quotes.map((q) => {
    const speaker = q.speaker_or_author;
    return `<blockquote class="orient-pull-quote"><p>${escapeHtml(q.text)}</p>${
      speaker ? `<cite>${escapeHtml(speaker)}</cite>` : ""
    }</blockquote>`;
  });
  return ['<div class="orient-pull-quotes">', ...blocks, "</div>"].join("\n");
}

// Every render function this module exports, keyed by name - the single
// list a Node CLI wrapper (tools/render_orientation_cli.mjs) and the Atlas
// panel's own runtime import both iterate/select from, so a new section
// added here needs no separate registration anywhere else.
export const RENDERERS = {
  story: renderStory,
  voices: renderVoices,
  documented_stories: renderDocumentedStories,
  floor_note: renderFloorNote,
  legacy: renderLegacy,
  relations_summary: renderRelationsSummary,
  sourcing: renderSourcing,
  who_speaks: renderWhoSpeaks,
  quiet: renderQuiet,
  glossary: renderGlossary,
  pull_quotes: renderPullQuotes,
};
