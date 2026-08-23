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

from engine.prose import (
    QUOTE_CLOSE,
    QUOTE_OPEN,
    SCAFFOLD_MARKERS,
    SELF_NAMING_MARKER,
    WITHHOLD_FLOOR,
    all_text,
    claim_markers,
    content_words,
    grounding_ratio,
    quote_aware_sentences,
)

# [[world.type.slug]] - record ids are dotted lowercase tokens; the tag
# grammar deliberately has no spaces so sentence splitting never breaks
# inside a tag.
_TAG = re.compile(r"\[\[([a-z0-9_.-]+)\]\]")


def strip_tags(text: str) -> str:
    """The display transform: what the participant-facing stream emits."""
    return re.sub(r"\s*\[\[[a-z0-9_.-]+\]\]", "", text)


# The last thing before a participant reads it. Every other check in this
# pipeline runs on a record, a sentence, or a tag - nothing looked at the
# finished paragraph, which is the only thing a person actually sees. Found
# across 49 live turns: markdown emphasis reaching a reader as literal
# asterisks ("they called this deeper reading *allegoria*") in 5 of them,
# and one answer that opened with a horizontal rule because the model echoed
# the question, the net withheld the echo, and the `---` under it survived
# glued to the next sentence.
#
# Residual [[...]] has never been observed, but it is here because the
# citation contract makes an explicit promise - "the tags themselves are
# never shown to the participant" - that strip_tags only keeps for tags the
# model spells correctly: its pattern is [a-z0-9_.-] with no spaces, so a
# malformed one like [[THIN GROUND: ...]] passes straight through untouched.
# One such sentence was withheld for an unrelated reason in testing; nothing
# would have caught it if it had not been.
#
# Reports, never edits. Rewriting a turn's text after the fact is the one
# thing this whole design refuses to do (the fallback ladder appends, it
# never revises), and a display defect is a signal that something upstream
# is wrong, not something to paper over on the way out.
def _quoted_spans(text: str) -> list[str]:
    spans = []
    pos = 0
    while True:
        open_m = QUOTE_OPEN.search(text, pos)
        if not open_m:
            return spans
        close_m = QUOTE_CLOSE.search(text, open_m.end())
        if not close_m:
            return spans
        spans.append(text[open_m.end() : close_m.start()])
        pos = close_m.end()


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", " ", text.lower())).strip()


def _span_in_records(span: str, records: list[dict], *, window_words: int = 6) -> bool:
    """Verbatim window-match (same shape as engine.m4.grounding's excerpt
    check): a quoted span is grounded when a window of it appears verbatim
    in a tagged record's own text."""
    words = _normalize(span).split()
    if not words:
        return False
    haystacks = [_normalize(all_text(r)) for r in records]
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
    for raw in quote_aware_sentences(text):
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
    grounding_floor: float = WITHHOLD_FLOOR,
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

        # REFERENTIAL INTEGRITY FIRST, before any exemption. Whether an id
        # resolves is not a question about the claim - it is a question
        # about the id, and no sentence is exempt from it.
        #
        # This check used to sit BELOW the scaffolding exemption, and a live
        # turn on desert walked straight through the gap: "But we do not
        # have a woman's own extended, first-person account..." matched
        # SCAFFOLD_MARKERS ("we do not have"), was exempted before its tag
        # was looked at, and shipped a citation to
        # desert.thinness.womens-first-person - a record that does not
        # exist, in a record type that does not exist. The very next
        # sentence carried the identical id, was not scaffolding, and was
        # correctly withheld. That is what a fabricated id looks like when
        # it finds the one door with no lock on it.
        #
        # It matters more since engine.api.wiring replays verified
        # citations into the model's own history: an invented id that
        # reaches `citations` comes back as a worked example of how to
        # cite, which teaches the fabrication instead of catching it.
        unknown = [t for t in tags if t not in repository_records]
        if unknown:
            entry["verdict"], entry["why"] = "withhold", f"unresolvable record id(s): {unknown}"
            continue

        if any(m in lower for m in SCAFFOLD_MARKERS) or SELF_NAMING_MARKER in lower:
            entry["why"] = "exempt: honesty scaffolding / sanctioned self-naming"
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

        markers = claim_markers(text)
        if not markers and figure_names & content_words(text):
            markers = [f"figure-name:{sorted(figure_names & content_words(text))}"]
        if not markers:
            entry["why"] = "no checkable claim - interpretive/connective framing"
            continue

        if not tags:
            entry["verdict"] = "withhold"
            entry["why"] = f"specific claim ({', '.join(markers)}) with no citation tag"
            continue

        cited_words: set[str] = set()
        for rec in tagged_records:
            cited_words |= content_words(all_text(rec))
        # the shared implementation, not a second copy of the same formula
        ratio = grounding_ratio(text, cited_words)
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
