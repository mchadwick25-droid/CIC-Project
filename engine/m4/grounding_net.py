"""Live-turn grounding for CITATION-TAGGED output (Live-Generation Design
§6, all four forks signed off 2026-08-22 - see engine/m4/LIVE-GENERATION-
DESIGN.md §9.5). Promoted from the design's own companion prototype
(grounding_experimental.py, claude/cic-design-assignment-ecoxh2), which
proved this exact logic against the real alx package (§6.2's run log) -
ported unchanged except this docstring; the calibration history below is
that prototype's own postmortem, kept because it is why the module is
shaped this way, not just how it got here.

What it checks is the design's output contract: the voice generates each
sentence with inline citation tags naming the record(s) that sentence draws
on - ``... the same bread, the same cup [[alx.term.eucharistia]].`` - tags
BEFORE the terminal punctuation, so a naive sentence splitter keeps a tag
inside its own sentence. The runtime strips tags before any participant
sees text; this module is what looks at them first.

Why this is sharper than the record-level experimental gate it descends
from (engine/m1/gates_experimental.gate_grounded_claim): that gate checks a
sentence against the union of EVERYTHING its record cites, so a sentence
can free-ride on words contributed by a source it never actually drew on.
Here every sentence names its own ground, so the grounding ratio is scoped
to exactly the records the sentence itself claims.

Calibrated against the real alx package (the run log is in the design doc):
the fabricated door line, tagged with the two records it originally cited,
comes back 28% grounded -> withheld; the corrected line clears the floor
against its three real sources at 40%; both licensed-quote sentences pass
by verbatim window-match rather than ratio (framing words around a real
quote should never sink a real quote). Three defects the first draft of
THIS module showed against real data, fixed here and worth keeping named
(the same discipline as the m1 module's v1 postmortem):
  1. a "marginal band" between floor/2 and floor let the one known real
     fabrication stream with only its badge withheld - removed; below the
     floor is withheld, full stop, and the quote-verbatim check carries
     the legitimate cases that used to need the band;
  2. the naive sentence splitter broke inside quotations ('...stones!'
     split mid-quote), orphaning a tag from the claim it grounded - the
     splitter now merges sentences until quotes balance;
  3. a sentence-initial figure name ("Clement wrote a whole book...")
     escaped the capitalization heuristic for proper nouns - a compiled
     figure-name lexicon (from the package's own figure records) now
     catches attributions positionally-blind.

Deterministic, no model call, string ops only - cheap enough to run inside
the streaming path per sentence. The claim-detection, scaffold/self-naming
exemptions, stopword list, and grounding floor are imported from the m1
experimental module unchanged: one implementation of "does this sentence
even make a checkable claim," owned once.
"""
import re

from engine.m1.gates_experimental import (
    _GROUNDING_FLOOR,
    _SCAFFOLD_MARKERS,
    _SELF_NAMING_MARKER,
    _all_text,
    _claim_markers,
    _content_words,
    _quote_aware_sentences,
    # Quotation-finding moved to the m1 module alongside the splitter that
    # depends on it (2026-08-23, when double-quoted spans turned out to be
    # invisible to both). Imported, never re-implemented: this module's
    # verbatim check and that splitter's merge have to agree on where a
    # quotation is or a sentence gets cut in half and the orphan withheld.
    _quoted_spans,
)

# [[world.type.slug]] - record ids are dotted lowercase tokens; the tag
# grammar deliberately has no spaces so sentence splitting never breaks
# inside a tag.
_TAG = re.compile(r"\[\[([a-z0-9_.-]+)\]\]")


def strip_tags(text: str) -> str:
    """The display transform: what the participant-facing stream emits."""
    return re.sub(r"\s*\[\[[a-z0-9_.-]+\]\]", "", text)


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", " ", text.lower())).strip()


def _span_in_records(span: str, records: list[dict], *, window_words: int = 6) -> bool:
    """Verbatim window-match (same shape as engine.m4.grounding's excerpt
    check): a quoted span is grounded when a window of it appears verbatim
    in a tagged record's own text."""
    words = _normalize(span).split()
    if not words:
        return False
    haystacks = [_normalize(_all_text(r)) for r in records]
    windows = (
        [" ".join(words)]
        if len(words) <= window_words
        else [" ".join(words[i : i + window_words]) for i in range(len(words) - window_words + 1)]
    )
    return any(w in h for h in haystacks for w in windows)


def build_figure_lexicon(repository_records: dict[str, dict]) -> set[str]:
    """Lowercased attested figure names from the package's own figure
    records - a positive lexicon, so a sentence-initial 'Clement wrote...'
    counts as a checkable attribution even though the capitalization
    heuristic is blind at position 0."""
    names: set[str] = set()
    for rec in repository_records.values():
        if rec.get("record_type") != "figure":
            continue
        for entry in rec.get("names") or []:
            # names entries are {name, tag}; only the in-world name feeds
            # the lexicon - scholarly forms ("Clement of Alexandria (Titus
            # Flavius Clemens...)") would pull common place/epithet words
            # in as false figure-signals.
            if isinstance(entry, dict) and entry.get("tag") == "in-world":
                for word in (entry.get("name") or "").split():
                    if len(word) > 2:
                        names.add(word.lower())
    return names


def parse_tagged(text: str) -> list[dict]:
    """Split tagged output into sentences, each with its own claimed ids."""
    out = []
    for raw in _quote_aware_sentences(text):
        ids = _TAG.findall(raw)
        out.append({"raw": raw, "text": strip_tags(raw).strip(), "tags": ids})
    return out


def _thin_topic_hits(sentence_lower: str, thin_topics: list[dict] | None) -> list[str]:
    hits = []
    for topic in thin_topics or []:
        kws = [kw for kw in (topic.get("keywords") or []) if kw.lower() in sentence_lower]
        if kws:
            hits.append(f"{kws} ({topic.get('note')})")
    return hits


def check_turn(
    tagged_text: str,
    repository_records: dict[str, dict],
    *,
    thin_topics: list[dict] | None = None,
    grounding_floor: float = _GROUNDING_FLOOR,
) -> dict:
    """Per-sentence verdicts over one tagged turn.

    Verdicts, mapped to the design's fallback ladder:
      ok       - no checkable claim, or the claim is grounded in its own tags
                 (ratio over the floor, or a quoted span verbatim-matched)
      withhold - the sentence never reaches the stream: unresolvable tag,
                 an untagged specific claim, a quoted span found in no
                 tagged record, or a tagged claim whose own sources don't
                 carry it

    Citation-badge display stays engine.m4.grounding's job (excerpt match
    gates decoration) - this check decides only what may stream at all.
    """
    figure_names = build_figure_lexicon(repository_records)
    results = []
    for sent in parse_tagged(tagged_text):
        text, tags = sent["text"], sent["tags"]
        lower = text.lower()
        entry = {"sentence": text, "tags": tags, "verdict": "ok", "why": None}
        results.append(entry)

        if any(m in lower for m in _SCAFFOLD_MARKERS) or _SELF_NAMING_MARKER in lower:
            entry["why"] = "exempt: honesty scaffolding / sanctioned self-naming"
            continue

        unknown = [t for t in tags if t not in repository_records]
        if unknown:
            entry["verdict"], entry["why"] = "withhold", f"unresolvable record id(s): {unknown}"
            continue
        tagged_records = [repository_records[t] for t in tags]

        spans = _quoted_spans(text)
        if spans:
            # Register statement 6, mechanical: quoted words either live
            # verbatim in a tagged record or they don't stream.
            if tags and all(_span_in_records(s, tagged_records) for s in spans):
                entry["why"] = "quoted span(s) verbatim in tagged record(s)"
                continue
            entry["verdict"] = "withhold"
            entry["why"] = "quoted span not found verbatim in any tagged record" if tags else "quoted span with no citation tag"
            continue

        markers = _claim_markers(text)
        if not markers and figure_names & _content_words(text):
            markers = [f"figure-name:{sorted(figure_names & _content_words(text))}"]
        if not markers:
            entry["why"] = "no checkable claim - interpretive/connective framing"
            continue

        if not tags:
            entry["verdict"] = "withhold"
            entry["why"] = f"specific claim ({', '.join(markers)}) with no citation tag"
            continue

        cited_words: set[str] = set()
        for rec in tagged_records:
            cited_words |= _content_words(_all_text(rec))
        words = _content_words(text)
        ratio = (len(words & cited_words) / len(words)) if words else 1.0
        entry["ratio"] = round(ratio, 2)

        if ratio >= grounding_floor:
            entry["why"] = f"grounded {ratio:.0%} in own tagged records"
        else:
            thin = _thin_topic_hits(lower, thin_topics)
            entry["verdict"] = "withhold"
            entry["why"] = (
                f"specific claim ({', '.join(markers)}) only {ratio:.0%} grounded in its own tags"
                + (f"; inside a named thin topic: {'; '.join(thin)}" if thin else "")
            )

    substantive_survives = any(r["verdict"] == "ok" and r["tags"] for r in results)
    return {"sentences": results, "substantive_survives": substantive_survives}


def scope_completion(record_ids: list[str], repository_records: dict[str, dict]) -> list[str]:
    """The anti-conflation rule from the design's retrieval section: never
    serve one pole of a recorded tension without the record that names the
    tension. Returns the extra ids the evidence block must carry: any
    gravity/contested_claim record standing in a tension-with or
    disputed-by relation with a retrieved record, walked in BOTH directions
    (relations are reciprocal by schema, but walking both ways means one
    missing back-edge can't silently drop the guard)."""
    wanted_types = {"gravity", "contested_claim"}
    tension_kinds = {"tension-with", "disputed-by"}
    seed = set(record_ids)
    extra: set[str] = set()

    for rid in record_ids:
        rec = repository_records.get(rid)
        for rel in (rec or {}).get("relations") or []:
            target = repository_records.get(rel.get("target"))
            if rel.get("type") in tension_kinds and target and target.get("record_type") in wanted_types:
                extra.add(target["id"])

    for rec in repository_records.values():
        if rec.get("record_type") not in wanted_types:
            continue
        for rel in rec.get("relations") or []:
            if rel.get("type") in tension_kinds and rel.get("target") in seed:
                extra.add(rec["id"])

    return sorted(extra - seed)
