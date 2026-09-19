/**
 * Shared renderer: world_front-compiled JSON (engine.m2.site_compiler's
 * output, cic-website/data/worlds/<census_id>.json) -> participant-facing
 * HTML fragments.
 *
 * Website V2 world_front design (approved to proceed 2026-09-19), site
 * cutover stage. This is the ONE place the Orientation-tier content
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
    .join("");
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
  return story.map((unit) => paragraphs(unit.text)).join("");
}

export function renderVoices(compiled) {
  const voices = (compiled.orientation && compiled.orientation.voices) || [];
  if (!voices.length) return "";
  return (
    '<div class="orient-voices">' +
    voices
      .map((v) => {
        const name = figureName(v.figure);
        const dates = figureDateSpan(v.figure);
        const heading = dates ? `${escapeHtml(name)} <span class="orient-voice-dates">(${escapeHtml(dates)})</span>` : escapeHtml(name);
        let block = `<div class="orient-voice"><p class="orient-voice-name">${heading}</p>`;
        block += paragraphs(v.text).replace(/^<p>/, '<p class="orient-voice-text">');
        if (v.hedge) {
          block += `<p class="orient-voice-hedge"><span class="orient-hedge-label">This world's own hedge:</span> ${escapeHtml(v.hedge)}</p>`;
        }
        block += "</div>";
        return block;
      })
      .join("") +
    "</div>"
  );
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
  return (
    '<div class="docstories-row">' +
    stories
      .map((s, i) => {
        const detailsId = `${idPrefix}-${i}`;
        let head = `<h4>${escapeHtml(s.title || "")}</h4>`;
        if (s.when) head += `<p class="meta">${escapeHtml(s.when)}</p>`;
        if (s.teaser) head += `<p class="teaser">${escapeHtml(s.teaser)}</p>`;
        const body = s.text ? paragraphs(s.text) : "";
        return (
          `<div class="docstory-entry">${head}` +
          `<details class="docstory-item" id="${detailsId}">` +
          `<summary><span class="docstory-title">Read the full account</span></summary>` +
          `<div class="docstory">${body}</div>` +
          "</details></div>"
        );
      })
      .join("") +
    "</div>"
  );
}

export function renderFloorNote(compiled) {
  const fn = compiled.orientation && compiled.orientation.floor_note;
  if (!fn || !fn.text) return "";
  return paragraphs(fn.text);
}

export function renderLegacy(compiled) {
  const legacy = (compiled.orientation && compiled.orientation.legacy) || [];
  return legacy.map((unit) => paragraphs(unit.text)).join("");
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
  let html = "";
  if (sourcing && sourcing.text) html += `<p>${escapeHtml(sourcing.text)}</p>`;
  if (readFirst.length) {
    html +=
      '<ul class="orient-read-first">' +
      readFirst
        .map((entry) => {
          const source = entry.source || {};
          const work = [source.author, source.work].filter(Boolean).join(", ");
          const note = entry.note ? ` <span class="orient-read-first-note">${escapeHtml(entry.note)}</span>` : "";
          return `<li><span class="orient-read-first-work">${escapeHtml(work)}</span>${note}</li>`;
        })
        .join("") +
      "</ul>";
  }
  return html;
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
// never invented, never a fabricated citation form. See this generator's
// own report for this judgment call.
function citeExcerpt(cite, maxLen) {
  if (!cite || !cite.text) return "";
  const label = (cite.record_type || "").replace(/_/g, " ");
  let text = cite.text.trim();
  if (text.length > maxLen) {
    text = text.slice(0, maxLen).replace(/\s+\S*$/, "") + "…";
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
    .join("");
  return `<ul class="questions">${items}</ul>`;
}

export function renderGlossary(compiled) {
  const glossary = (compiled.narrative && compiled.narrative.glossary) || [];
  if (!glossary.length) return "";
  return (
    '<dl class="orient-glossary">' +
    glossary
      .map((t) => `<div class="orient-glossary-item"><dt>${escapeHtml(t.world_word)}</dt><dd>${escapeHtml(t.meaning)}</dd></div>`)
      .join("") +
    "</dl>"
  );
}

// A quote's own `speaker_or_author` field is sometimes a resolved
// scholarly attribution string ("Palladius, in the Syriac recension of
// the Paradise") and sometimes a bare record id (`desert.figure.sarah`) -
// a real, fleet-wide authoring inconsistency this session found across 6
// of the 8 built worlds' own quote records, which the compiler's own
// _resolve_quote() (engine/m2/site_compiler.py) passes through verbatim
// without resolving against the figure records. Rather than leak an
// internal id into participant-facing text, this resolves it against the
// same figures the compiled JSON already carries in narrative.who_speaks
// (the world's own anchor figures) when possible, and otherwise falls
// back to reformatting the id's own last segment as a name - never a
// fabricated addition, just the id's own words made readable. See this
// generator's own report for the full finding and the fix that actually
// belongs in the compiler.
const _BARE_RECORD_ID_RE = /^[a-z0-9]+\.(figure|quote|story)\.[a-z0-9-]+$/;

function resolveSpeaker(raw, compiled) {
  if (!raw) return "";
  if (!_BARE_RECORD_ID_RE.test(raw)) return raw;
  const figures = (compiled.narrative && compiled.narrative.who_speaks && compiled.narrative.who_speaks.figures) || [];
  const match = figures.find((f) => f.id === raw);
  if (match) return figureName(match);
  const lastSegment = raw.split(".").pop();
  return lastSegment
    .split("-")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
}

export function renderPullQuotes(compiled) {
  const quotes = (compiled.narrative && compiled.narrative.pull_quotes) || [];
  if (!quotes.length) return "";
  return (
    '<div class="orient-pull-quotes">' +
    quotes
      .map((q) => {
        const speaker = resolveSpeaker(q.speaker_or_author, compiled);
        return `<blockquote class="orient-pull-quote"><p>${escapeHtml(q.text)}</p>${
          speaker ? `<cite>${escapeHtml(speaker)}</cite>` : ""
        }</blockquote>`;
      })
      .join("") +
    "</div>"
  );
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
