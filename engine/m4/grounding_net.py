"""Live-turn grounding for CITATION-TAGGED output (Live-Generation Design
§6 - see engine/m4/LIVE-GENERATION-DESIGN.md §9.5, all four forks signed
off). Promoted from the design's own companion prototype
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

from engine.m1.quote_verbatim import normalize_archaic_letterforms
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

# An opener with no closing "]]" anywhere after it - not a malformed tag
# (engine.m4.output_check's _ANY_TAG already reports those; a different,
# already-handled defect, since that one still has both brackets). This is
# what a generation call cut off mid-tag leaves behind: Bedrock's own
# stream ending inside "[[world.type.slug" with no "]]" ever sent. _TAG's
# grammar requires the close - deliberately, so a tag it resolves and a
# tag strip_tags removes can never disagree about what counts as one - so
# an opener that never closed is never matched by either, and unlike
# _ANY_TAG (which needs no closing bracket to be well-formed, just to be
# present) there is no complete pattern here to widen to catch it. A real
# generation call cut off exactly this way once, while rebuilding a Table
# transcript for transparency markup: one turn's raw text ended inside an
# unclosed "[[don.dw.room-for-diss", which strip_tags' own re.sub below
# left untouched, verbatim, brackets and all.
_DANGLING_TAG = re.compile(r"\[\[[a-z0-9_.-]*\Z")


def _drop_truncated_tail(text: str) -> tuple[str, bool]:
    """Back a generation cut off mid-tag off to the last sentence this turn
    actually finished, so the one shape _TAG's own grammar can never catch
    (an opener with no matching close) never reaches a participant as raw
    "[[..." syntax.

    This module's design always places a tag BEFORE its sentence's
    terminal punctuation (this file's own top docstring), so an opener
    with no close means that sentence's own close was cut too - the same
    truncation event, not two separate defects. An unclosed tag can only
    ever occur at the very end of a raw stream (that is where generation
    stopped), so the one thing known for certain is the last `.`/`!`/`?`
    before it: the last sentence the voice actually finished. Everything
    after that boundary was never confirmed complete and does not stream.

    Returns (text, truncated) rather than truncating quietly - REPORTS,
    NEVER EDITS is this module's own rule, and a report that never fires
    when an edit happens is not honouring it. Ordinary text with no
    dangling opener returns unchanged, truncated=False."""
    match = _DANGLING_TAG.search(text)
    if not match:
        return text, False
    kept = text[: match.start()]
    last_stop = max(kept.rfind("."), kept.rfind("!"), kept.rfind("?"))
    return (kept[: last_stop + 1] if last_stop != -1 else ""), True


def strip_tags(text: str) -> str:
    """The display transform: what the participant-facing stream emits."""
    text, _ = _drop_truncated_tail(text)
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
# Residual [[...]] was observed exactly once, an unclosed
# [[don.dw.room-for-diss left by a generation call cut off mid-tag - see
# _DANGLING_TAG and _drop_truncated_tail above, which now back strip_tags
# off past it. What is still true, and still here because the citation
# contract makes an
# explicit promise - "the tags themselves are never shown to the
# participant" - that strip_tags only keeps for tags the model spells
# correctly: a COMPLETE but malformed tag, spelled outside strip_tags'
# [a-z0-9_.-] pattern (like [[THIN GROUND: ...]], both brackets present),
# still passes straight through this module untouched. That shape is
# caught downstream instead, reported (not edited) by
# engine.m4.output_check's own _ANY_TAG - a deliberate division of labour,
# not a gap: _drop_truncated_tail only ever had one unambiguous signal to
# act on (an opener with no close, which can only mean a cut stream), and
# widening it to cover other malformed spellings would mean guessing at
# text the model actually finished, which this module does not do.
#
# Reports, never edits. Rewriting a turn's text after the fact is the one
# thing this whole design refuses to do (the fallback ladder appends, it
# never revises), and a display defect is a signal that something upstream
# is wrong, not something to paper over on the way out.
def quoted_span_positions(text: str) -> list[tuple[int, int, str]]:
    """Every paired quotation in `text`, left to right: (start, end,
    inner) - `start` is the opening quotation mark's own offset, `end` is
    just past the closing quotation mark, `inner` is the quoted words
    between them. engine.m4.transparency_plan places a quote's mark at
    `end`: a quote's mark follows the quoted words."""
    spans = []
    pos = 0
    while True:
        open_m = QUOTE_OPEN.search(text, pos)
        if not open_m:
            return spans
        close_m = QUOTE_CLOSE.search(text, open_m.end())
        if not close_m:
            return spans
        spans.append((open_m.end() - 1, close_m.end(), text[open_m.end() : close_m.start()]))
        pos = close_m.end()


def _quoted_spans(text: str) -> list[str]:
    return [inner for _start, _end, inner in quoted_span_positions(text)]


def _normalize(text: str) -> str:
    # Archaic letterforms first (the same mapping engine.m1.quote_verbatim's
    # own verbatim check applies): otherwise the [^a-z0-9\s] strip below silently
    # deletes ſ/þ/ð rather than folding them to their modern spelling,
    # which is a real content loss, not a normalization ("þe" becoming
    # " e" instead of "the"). Applied to both the quoted span and the
    # shelf's own record text below, since both call sites route through
    # this one function - inherently symmetric.
    text, _classes = normalize_archaic_letterforms(text)
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", " ", text.lower())).strip()


def _groundable_text(rec: dict) -> str:
    """The text a generated turn can actually be checked against for
    grounding. A quote record's own `modern_rendering` only - never
    `text` (an archaic or non-English original) - since gate_quote_
    recording (engine/m1/gates.py) and the speakable-form selection in
    evidence.py/builders.py already make modern_rendering the only form
    ever voiced; a generated span matching `text` but not the record's
    own spoken form was never legitimately produced from it. Every other
    record type keeps the wider all_text() - not scoped here, since
    readability, commentary scanning, and the retrieval word-pool all
    still need to see a quote's own `text` for their own, different
    reasons."""
    if rec.get("record_type") == "quote":
        return rec.get("modern_rendering") or ""
    return all_text(rec)


def _span_in_records(span: str, records: list[dict], *, window_words: int = 6) -> bool:
    """Verbatim window-match (same shape as engine.m4.grounding's excerpt
    check): a quoted span is grounded when a window of it appears verbatim
    in a tagged record's own text."""
    words = _normalize(span).split()
    if not words:
        return False
    haystacks = [_normalize(_groundable_text(r)) for r in records]
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


# The scaffold exemption
# below used to exempt an entire sentence the moment ANY SCAFFOLD_MARKERS
# phrase appeared anywhere in it - so "...our founder wrote against the
# peasants' rising, and that writing is part of our own history EVEN WHEN
# WE CANNOT speak its own words" rode a chronological conflation past the
# net on the strength of four words at its own tail. The fix narrows the
# exemption to the clause that actually carries the honesty-scaffolding
# phrase, not an arbitrary-length sentence attached to it: split on the
# same clause-level punctuation English prose already uses to separate
# independent claims, drop only the clause(s) containing a marker, and
# check what's LEFT the same way any other sentence would be checked. A
# genuinely pure scaffold sentence ("We must be careful here, and honest
# about the shape of what we actually hold.") still exempts cleanly - its
# residual carries no proper noun, number, or enumeration either. A tag
# counts too, on the same basis check_turn's own tag-overlap branch
# already uses ("THE TAG IS THE CLAIM"): a scaffold phrase grammatically
# FUSED with its claim ("We must be honest THAT x [[tag]]") defeats the
# punctuation split, but the tag still forces the check regardless of
# which clause it sits in. This does not change entry["sentence"] or the
# withhold/ok granularity anywhere else in this module: a sentence still
# streams or doesn't as a whole, exactly as the design already works:
# this only changes whether the decision to skip checking it gets made
# honestly.
_CLAUSE_SPLIT = re.compile(r"[,;:]|--|—")


def _scaffold_residual(text: str) -> str:
    clauses = _CLAUSE_SPLIT.split(text)
    kept = [
        c for c in clauses
        if not any(m in c.lower() for m in SCAFFOLD_MARKERS) and SELF_NAMING_MARKER not in c.lower()
    ]
    return " ".join(kept)


def verdict_for_sentence(
    text: str,
    tags: list[str],
    *,
    repository_records: dict[str, dict],
    figure_names: set[str],
    thin_topics: list[dict] | None,
    grounding_floor: float,
) -> dict:
    """One sentence's verdict - check_turn()'s own per-sentence logic,
    factored out (Build-Plan.md Stage 1, D1 grounding measurement) so a
    single constructed (sentence, tags) pair can be run directly, without
    round-tripping through tagged-text reconstruction and re-parsing. Pure
    extraction: no behavior change, verified against test_grounding_net.py
    unchanged. check_turn() below is now this function called once per
    parse_tagged() sentence; see its own docstring for the verdict
    vocabulary and the fallback ladder this implements."""
    lower = text.lower()
    entry = {"sentence": text, "tags": tags, "verdict": "ok", "why": None}

    if any(m in lower for m in SCAFFOLD_MARKERS) or SELF_NAMING_MARKER in lower:
        residual = _scaffold_residual(text)
        # A tag is itself a claim ("this sentence came from that
        # record" - the tag-overlap branch below exists for exactly
        # this), so a tagged sentence needs the same check whether or
        # not a scaffold phrase also sits in it somewhere.
        residual_markers = bool(tags) or bool(claim_markers(residual)) or bool(figure_names & content_words(residual))
        if not residual_markers:
            entry["why"] = "exempt: honesty scaffolding / sanctioned self-naming"
            return entry
        # Something besides the scaffold phrase itself still makes a
        # checkable claim - fall through to the same pipeline every
        # other sentence goes through, over the FULL sentence text
        # (the scaffold clause's own words carry no proper noun,
        # number, or enumeration, so they cannot themselves trip a
        # withhold; whatever fires below is the real content).

    unknown = [t for t in tags if t not in repository_records]
    if unknown:
        entry["verdict"], entry["why"] = "withhold", f"unresolvable record id(s): {unknown}"
        return entry
    tagged_records = [repository_records[t] for t in tags]

    spans = _quoted_spans(text)
    if spans:
        # Register statement 6, mechanical: quoted words either live
        # verbatim in a tagged record or they don't stream.
        if tags and all(_span_in_records(s, tagged_records) for s in spans):
            entry["why"] = "quoted span(s) verbatim in tagged record(s)"
            return entry
        entry["verdict"] = "withhold"
        entry["why"] = "quoted span not found verbatim in any tagged record" if tags else "quoted span with no citation tag"
        return entry

    markers = claim_markers(text)
    if not markers and figure_names & content_words(text):
        markers = [f"figure-name:{sorted(figure_names & content_words(text))}"]
    cited_words: set[str] = set()
    for rec in tagged_records:
        cited_words |= content_words(_groundable_text(rec))

    if not markers:
        if not tags:
            entry["why"] = "no checkable claim - interpretive/connective framing"
            return entry
        # THE TAG IS THE CLAIM. claim_markers only sees a proper noun, a
        # number, or a repeated phrase, and over 36 live turns that left
        # 242 of 388 sentences unexamined - the citation contract reads
        # as a guarantee over the turn and was a guarantee over the third
        # of it that happened to name someone or count something.
        #
        # 192 of those unexamined sentences carried a tag. A tag is the
        # voice asserting THIS SENTENCE CAME FROM THAT RECORD, which is
        # checkable by definition, and the net was throwing that
        # assertion away. Honouring it takes the examined share from 32%
        # to 78% without inventing a marker.
        #
        # Gated on overlap, NOT on grounding_floor. That floor was
        # calibrated on name-and-number sentences, which sit lexically
        # close to their source; applied to this population it strips
        # roughly 29 legitimate citations to catch 10 over-tags -
        # "Origen's interpretations mattered because he could show his
        # work" scores 29% and is a real claim, penalised for being long.
        # Zero shared words is the one line here that is not a chosen
        # number: a citation to a record with which the sentence shares
        # not one content word asserts nothing. Seven of the 192 were
        # that, every one framing - "That is what mattered most." tagged
        # to hal.gravity.hebraica-veritas.
        if content_words(text) & cited_words:
            entry["why"] = "tagged claim, shares ground with its own records"
            return entry
        entry["verdict"] = "withhold"
        entry["why"] = "tagged claim sharing no content word with its own tagged records"
        return entry

    if not tags:
        entry["verdict"] = "withhold"
        entry["why"] = f"specific claim ({', '.join(markers)}) with no citation tag"
        return entry

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
    return entry


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

    tagged_text is backed off past any generation cut off mid-tag
    (_drop_truncated_tail) before it is split into sentences at all, the
    same normalization strip_tags applies to the text turn.apply_net
    actually displays - so this function's own sentence list can never
    describe a fragment the participant was never shown. result["truncated"]
    is that normalization's own report, not a silent edit.
    """
    tagged_text, truncated = _drop_truncated_tail(tagged_text)
    figure_names = build_figure_lexicon(repository_records)
    results = [
        verdict_for_sentence(
            sent["text"], sent["tags"],
            repository_records=repository_records,
            figure_names=figure_names,
            thin_topics=thin_topics,
            grounding_floor=grounding_floor,
        )
        for sent in parse_tagged(tagged_text)
    ]
    substantive_survives = any(r["verdict"] == "ok" and r["tags"] for r in results)
    return {"sentences": results, "substantive_survives": substantive_survives, "truncated": truncated}


# Blank-line blocks - the exact regex
# engine.m4.live_uncited_claims_battery's own _PARAGRAPH_SPLIT already
# proved live across two battery runs (#419, #420). A paragraph is a
# sequence of the same sentences parse_tagged already produces, grouped by
# which blank-line block they fell in - nothing about how a sentence
# itself is found or tagged changes.
_PARAGRAPH_SPLIT = re.compile(r"\n\s*\n")


def split_into_paragraphs(tagged_text: str) -> list[str]:
    paragraphs = [p for p in _PARAGRAPH_SPLIT.split(tagged_text) if p.strip()]
    return paragraphs or [tagged_text]


def drop_flagged_sentences(tagged_text: str, flagged_sentences: set[str]) -> str:
    """Removes each named sentence's own raw span - tag included - from
    tagged_text, whole, and rejoins what is left. The one enforcement
    action a caller may take on a flagged sentence that is not "regenerate
    the whole turn again": reuses this module's own split_into_paragraphs/
    parse_tagged, the same sentence/paragraph boundaries every verdict in
    "sentences" was already computed against, so a sentence named by its
    own exact `verdict_for_sentence`-produced text (parse_tagged's own
    "text" field, tags already stripped) is matched and removed
    unambiguously - no re-splitting, no re-tokenizing, no risk of
    disagreeing with the net about where one sentence ends and the next
    begins.

    Two structural guarantees, not left to chance:
      - a paragraph that loses every one of its own sentences is dropped
        whole, never left behind as an empty blank-line block;
      - a paragraph that keeps at least one sentence keeps its own
        surviving sentences joined by a single space, so removing a
        sentence from the middle never leaves doubled whitespace or an
        orphaned closing quote/tag.

    What this does NOT guarantee: a sentence that grammatically promised
    the one just removed (a paragraph ending "...three things stand out:"
    whose own next sentence was the one dropped) can still read as an
    unfinished promise - a semantic dangling fragment this string-level
    operation has no way to see, as opposed to the structural one
    (broken punctuation, an empty paragraph) it does prevent."""
    kept_paragraphs = []
    for paragraph in split_into_paragraphs(tagged_text):
        kept_sentences = [sent["raw"] for sent in parse_tagged(paragraph) if sent["text"] not in flagged_sentences]
        if kept_sentences:
            kept_paragraphs.append(" ".join(kept_sentences))
    return "\n\n".join(kept_paragraphs)


def check_turn_with_paragraph_coverage(
    tagged_text: str,
    repository_records: dict[str, dict],
    *,
    thin_topics: list[dict] | None = None,
    grounding_floor: float = WITHHOLD_FLOOR,
) -> dict:
    """check_turn's own base per-sentence pass, reproduced exactly (same
    truncation backoff, same verdict_for_sentence calls, same sentence
    list, same substantive_survives/truncated meaning - a caller reading
    only this result's own "sentences"/"substantive_survives"/"truncated"
    keys cannot tell it apart from check_turn's), PLUS an additive,
    report-only "paragraph_coverage" layer. Nothing here changes what
    apply_net does with a turn - apply_net calls check_turn directly,
    never this function; this exists for engine.m4.uncited_claims's own
    paragraph-level detection to read.

    paragraph_coverage is a list, one entry per blank-line paragraph
    (split_into_paragraphs), each:
      sentence_count        - how many of this result's own "sentences"
                               belong to this paragraph (they sit
                               contiguously, in order - a caller partitions
                               the flat sentence list by walking these
                               counts, the same way this function itself
                               does below)
      cited_record_ids       - EFFECTIVE record ids this paragraph's own
                               coverage check uses: the union of every tag
                               in this paragraph's own sentences, UNLESS
                               this is a one-sentence paragraph carrying no
                               tag of its own, in which case it is the
                               immediately PRECEDING paragraph's own
                               cited_record_ids instead (coverage only;
                               see inherited_from_preceding below)
      wholly_uncited         - true when cited_record_ids is empty - this
                               paragraph carries no citation anywhere, not
                               even by inheritance
      inherited_from_preceding - true only for a one-sentence paragraph
                               that borrowed its own cited_record_ids from
                               the paragraph before it
      inherited_verdicts     - {sentence index WITHIN this paragraph:
                               verdict_for_sentence's own result}, one
                               entry per sentence that carries no tag of
                               its own but whose paragraph's own
                               cited_record_ids is non-empty - the exact
                               same function real per-sentence checking
                               already runs, fed this paragraph's own
                               inherited ids instead of that sentence's
                               own (empty) tags. No new checking logic, no
                               new model call: this is the identical
                               verdict_for_sentence a tagged sentence
                               already gets, called a second time for an
                               untagged one, against a different id set.
    """
    tagged_text, truncated = _drop_truncated_tail(tagged_text)
    figure_names = build_figure_lexicon(repository_records)
    paragraphs_raw = split_into_paragraphs(tagged_text)

    all_sentences: list[dict] = []
    paragraph_coverage: list[dict] = []
    for paragraph_text in paragraphs_raw:
        parsed = parse_tagged(paragraph_text)
        verdicts = [
            verdict_for_sentence(
                sent["text"], sent["tags"],
                repository_records=repository_records,
                figure_names=figure_names,
                thin_topics=thin_topics,
                grounding_floor=grounding_floor,
            )
            for sent in parsed
        ]
        all_sentences.extend(verdicts)

        own_record_ids = sorted({t for sent in parsed for t in sent["tags"]})
        inherited_from_preceding = False
        if len(parsed) == 1 and not own_record_ids and paragraph_coverage and paragraph_coverage[-1]["cited_record_ids"]:
            cited_record_ids = paragraph_coverage[-1]["cited_record_ids"]
            inherited_from_preceding = True
        else:
            cited_record_ids = own_record_ids

        inherited_verdicts: dict[int, dict] = {}
        if cited_record_ids:
            for i, sent in enumerate(parsed):
                if sent["tags"]:
                    continue  # already carries its own real tag - no inheritance needed
                inherited_verdicts[i] = verdict_for_sentence(
                    sent["text"], cited_record_ids,
                    repository_records=repository_records,
                    figure_names=figure_names,
                    thin_topics=thin_topics,
                    grounding_floor=grounding_floor,
                )

        paragraph_coverage.append({
            "sentence_count": len(parsed),
            "cited_record_ids": cited_record_ids,
            "wholly_uncited": not cited_record_ids,
            "inherited_from_preceding": inherited_from_preceding,
            "inherited_verdicts": inherited_verdicts,
        })

    substantive_survives = any(r["verdict"] == "ok" and r["tags"] for r in all_sentences)
    return {
        "sentences": all_sentences,
        "substantive_survives": substantive_survives,
        "truncated": truncated,
        "paragraph_coverage": paragraph_coverage,
    }


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
