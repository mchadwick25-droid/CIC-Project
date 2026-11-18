
export function escapeHtml(s) {
  if (s === null || s === undefined) return "";
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function paragraphs(text, marks) {
  if (!text) return "";
  return String(text)
    .split(/\n\n+/)
    .map((p) => `<p>${marks ? marks.mark(p.trim()) : escapeHtml(p.trim())}</p>`)
    .join("\n");
}

function sourceHost(url) {
  try {
    return url ? new URL(url).hostname.replace(/^www\./, "") : "";
  } catch (e) {
    return "";
  }
}

const HIGHLIGHT_KIND_LABEL = { person: "Person", term: "Term", council: "Council", place: "Place" };

function highlighter(compiled) {
  const entries = ((compiled.orientation && compiled.orientation.highlights) || [])
    .filter((h) => h && h.phrase && h.note)
    .sort((a, b) => b.phrase.length - a.phrase.length);
  if (!entries.length) return null;
  const used = new Set();
  return {
    mark(text) {
      const spans = [];
      for (const h of entries) {
        if (used.has(h.phrase)) continue;
        const re = new RegExp(`(?<![\\p{L}\\p{N}])${h.phrase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}(?![\\p{L}\\p{N}])`, "gu");
        let m;
        while ((m = re.exec(text))) {
          const start = m.index, end = start + m[0].length;
          if (spans.some((s) => start < s.end && end > s.start)) continue;
          spans.push({ start, end, h });
          used.add(h.phrase);
          break;
        }
      }
      spans.sort((a, b) => a.start - b.start);
      let out = "", at = 0;
      for (const { start, end, h } of spans) {
        const kind = HIGHLIGHT_KIND_LABEL[h.kind] || "";
        out += escapeHtml(text.slice(at, start))
          + `<span class="hl" tabindex="0">${escapeHtml(text.slice(start, end))}`
          + `<span class="hl-note" role="tooltip"><b>${escapeHtml(h.label || h.phrase)}</b>${escapeHtml(h.note)}`
          + `<small>${[kind, sourceHost(h.url)].filter(Boolean).join(" \u00b7 ")}</small>`
          + "</span></span>";
        at = end;
      }
      return out + escapeHtml(text.slice(at));
    },
  };
}

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


function narrationPlayer(url) {
  if (!url) return "";
  return [
    '<div class="narration">',
    `<audio controls preload="none" src="${escapeHtml(url)}"></audio>`,
    '<p class="narration-disclosure">Synthesized voice \u2014 not a recording.</p></div>',
  ].join("");
}

export function renderStory(compiled, opts) {
  const story = (compiled.orientation && compiled.orientation.story) || [];
  const player = narrationPlayer(opts && opts.narration && opts.narration.story);
  const marks = highlighter(compiled);
  return player + story.map((unit) => paragraphs(unit.text, marks)).join("\n");
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

export function renderDocumentedStories(compiled, opts) {
  const idPrefix = (opts && opts.idPrefix) || "ds";
  const stories = (compiled.orientation && compiled.orientation.documented_stories) || [];
  if (!stories.length) return "";
  const entries = stories.map((s, i) => {
    const detailsId = `${idPrefix}-${i}`;
    const head = [`<h4>${escapeHtml(s.title || "")}</h4>`];
    if (s.when) head.push(`<p class="meta">${escapeHtml(s.when)}</p>`);
    if (s.teaser) head.push(`<p class="teaser">${escapeHtml(s.teaser)}</p>`);
    const account = s.telling || s.tellable_as;
    const documented = (opts && opts.narration && opts.narration.documented) || {};
    const body = account ? narrationPlayer(documented[s.story_id]) + paragraphs(account, highlighter(compiled)) : "";
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

export function renderLegacy(compiled, opts) {
  const legacy = (compiled.orientation && compiled.orientation.legacy) || [];
  const player = narrationPlayer(opts && opts.narration && opts.narration.legacy);
  return player + legacy.map((unit) => paragraphs(unit.text)).join("\n");
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
      const work = source.citation || [source.author, source.work].filter(Boolean).join(", ");
      const note = entry.note ? ` <span class="orient-read-first-note">${escapeHtml(entry.note)}</span>` : "";
      return `<li><span class="orient-read-first-work">${escapeHtml(work)}</span>${note}</li>`;
    });
    parts.push(['<ul class="orient-read-first">', ...items, "</ul>"].join("\n"));
  }
  return parts.join("\n");
}


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
      const href = `../talk.html?worlds=${encodeURIComponent(slug)}&mode=interview&from=traditions%2F${encodeURIComponent(slug)}.html#q=${encodeURIComponent(questionText)}`;
      let li = `<li><a href="${escapeHtml(href)}" data-question>${escapeHtml(questionText)}<span class="vh"> — ask ${escapeHtml(repName)}</span></a>`;
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

export function narrationUrls(entry, base) {
  if (!entry) return null;
  const url = (k) => (entry[k] ? base + entry[k].file : null);
  const documented = {};
  for (const k of Object.keys(entry)) {
    const m = /^docstory-(.+)$/.exec(k);
    if (m) documented[m[1]] = url(k);
  }
  return { story: url("story"), legacy: url("legacy"), documented };
}

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
