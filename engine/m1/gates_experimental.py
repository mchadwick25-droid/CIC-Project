"""Mechanisms for a class of bug the accepted M1 battery cannot see: a
record whose citations are real, well-formed, and rights-clean, but whose
prose says more than those citations actually support. Found live in
alx.demo.f6-p-someone-like-me (2026-08-21) - it cited two real records,
neither of which documents the specific claim it made, while the world's own
world_core named the exact gap in its `cautions` field the whole time.

NOT yet in gates.GATES / the accepted battery. These are under test - Mark,
2026-08-21: "yes lets test 2 and 3", then, after both v1 attempts came back
weak: "lets analyse why they didn't work and redesign". Findings here are
candidates for human review, not a pass/fail verdict, until proven against
real content and formally admitted the way every other gate was (its own
defect-catalog entry + selftest proof) - the bar gate_tension_coverage and
gate_grounded_claim are still under, and gate_no_build_attribution (built
here, then admitted the same day - see gates.py) already cleared.

== v1 (kept below, superseded, not in EXPERIMENTAL_GATES) ==

gate_caution_crosscheck_v1 and gate_unsupported_claim_v1 were built and run
against alx's real 137 records. Root-cause read on why each fell short:

v1 caution-crosscheck matched bare keywords against a record's WHOLE text,
which measures TOPIC, not TRUTH-VALUE - a record can mention "women" while
being the correct honest handling of that gap (an honest_limit) or while
fabricating past it (the actual bug), and keyword presence alone can't tell
those apart. Worse: "Coptic" fires identically whether a sentence is
describing the non-literate Egyptian population the world's sources are
silent on, or the 451 Chalcedonian schism - two unrelated referents that
happen to share a word. The "require >=2 keyword hits" tuning that got v1
down to a clean result was fitted to the one known bug, not the general
class - a future single-clause, single-topic fabrication would sail through
a >=2 threshold.

v1 unsupported-claim required only that a sentence share >=1 stopword-
filtered content word with its cited sources - a bar weak enough that the
real bug passed it (the fabricated sentence shares "word", "church", "men",
"same", "learned" with its citations - enough generic overlap to clear a
nonzero bar) while it fired on legitimate connective/values framing instead
("Then you have already done a hard and honest thing by saying it out
loud." shares zero words with any citation and never needed to - it isn't a
factual claim). It tried to fix this by exempting sentences that match a
hand-maintained honesty-phrase list - exemption lists don't scale and
immediately proved leaky.

== v2 (gate_grounded_claim, redesigned) ==

The shared root cause: both v1 gates ran at the wrong grain and answered the
wrong question. Topic-presence isn't truth-value; any-word-overlap isn't
grounding. v2 composes both signals as one pipeline, at the sentence level:

  1. POSITIVE specificity detection first - does this sentence even make a
     checkable claim (a proper noun, a number, or an enumerated/parallel-
     list construction - "the same water, the same bread... Greeks and
     Egyptians... men and women" is exactly that shape)? If not, it's
     interpretive/values framing and is skipped outright - no exemption
     list needed, because nothing fires on it in the first place.
  2. Only a specific claim gets grounding-checked, and grounding is now a
     RATIO (how much of the sentence's own content is attested in its cited
     internal sources), not a bare nonzero check.
  3. Only THEN, on a sentence already flagged as specific-and-ungrounded, is
     it cross-checked against world_core.thin_topics - as a severity
     escalator on a real finding, not a standalone trigger. This also
     narrows scope to record types that carry spoken/narrative claims
     (demonstration, doctrinal_witness, story); a `force` or `gravity`
     analytical record citing only a raw `source` stub is never in scope,
     which resolves the alx.force.chalcedonian-fracture false positive by
     construction, not by a special-cased exemption.
"""
import re

_NON_PROSE_KEYS = {
    "id", "world_id", "record_type", "schema_version", "status", "register",
    "_path", "_body", "world_word", "license", "narrative_tier",
    "formation_claim_barred", "citation_specificity", "verification_state",
    "evidentiary_weight", "formation_confidence",
}

_STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "at", "by",
    "for", "with", "as", "is", "was", "were", "are", "be", "been", "being",
    "it", "its", "this", "that", "these", "those", "we", "us", "our", "ours",
    "you", "your", "yours", "they", "them", "their", "he", "him", "his",
    "she", "her", "hers", "i", "me", "my", "mine", "not", "no", "so", "if",
    "than", "then", "too", "also", "one", "did", "do", "does", "had", "has",
    "have", "what", "who", "when", "where", "why", "how", "all", "any",
    "some", "into", "out", "up", "down", "over", "under", "here", "there",
    "can", "could", "would", "should", "will", "shall", "must", "let", "yet",
    "even", "still", "just", "only", "own", "back", "before", "after",
    "because", "about", "against", "between", "from", "each", "other",
}

# Updated 2026-08-21 for the fleet-wide pronoun rule (strict we-voice,
# always - see the exemplar transcript and alx.voice.craft's superseding
# ruling): vocational-honesty scaffolding now reads "we", not "I". The one
# sanctioned "I" left in the corpus - "I am a representative of [world]" -
# gets its own exemption below, not folded in here, since it isn't honesty-
# scaffolding, it's a one-time self-naming that never needs grounding.
_SCAFFOLD_MARKERS = (
    "we must be honest", "we will not invent", "we will not pretend",
    "we will not put words", "we cannot", "we will not", "we are not your judge",
    "it is not our place", "it is not our role", "we do not have",
    "we must be careful", "we will not draw one", "we will not sell you",
    "we find none of these", "we owe you honesty", "we must leave",
)

# The one sanctioned "I" left in the register: a one-time, honest self-
# naming of what the voice literally is (a representative), never an
# empirical claim about the world's history - it doesn't need a citation
# any more than a form's "I am a bot" disclosure would.
_SELF_NAMING_MARKER = "i am a representative of"

_WORD = re.compile(r"[a-zA-Z']+")
_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def _all_text(rec: dict) -> str:
    """Every string value in a record, recursively, minus purely structural
    fields - a deliberately generic extractor so this works across all
    record types without a per-type text-field map."""
    parts = []

    def walk(value, key=None):
        if isinstance(value, str):
            if key not in _NON_PROSE_KEYS:
                parts.append(value)
        elif isinstance(value, dict):
            for k, v in value.items():
                walk(v, k)
        elif isinstance(value, list):
            for item in value:
                walk(item, key)

    walk(rec)
    return " ".join(parts)


def _content_words(text: str) -> set[str]:
    words = (w.lower() for w in _WORD.findall(text))
    return {w for w in words if w not in _STOPWORDS and len(w) > 2}


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENTENCE_SPLIT.split(text or "") if s.strip()]


# An opening quote is at start-of-text or after space/colon/comma/dash and
# is followed by a non-space; a closing one follows a non-space and is
# followed by space, punctuation, or end. Apostrophes inside words ("God's")
# match neither. A lone false closer (teachers') can't force a merge because
# merging only triggers while openers outnumber closers. Shared here (not
# left as an engine.m4-only concern) because M2's compile-time demonstration
# tagging needs the identical quote-aware split M4's live net uses - one
# splitter, owned once, so a demo tagged at compile time and a live turn
# checked at generation time can never silently disagree about where a
# sentence ends.
#
# DOUBLE QUOTES (2026-08-23): for a long time only the straight SINGLE quote
# was recognised, because that is the convention the records corpus was
# written in. Two things were wrong with that. The corpus itself already
# holds 249 paired double-quoted spans (pahc and ijc most of all - real
# quoted source material), and a live model quotes with " far more readily
# than with ', whatever the prompt around it does. A double-quoted span was
# invisible to BOTH things this splitter feeds:
#
#   * the merge below never fired, so a sentence split inside the quotation
#     and orphaned half of it - seen live as `It has made men out of stones,
#     men out of beasts".` reaching a participant with its own opening
#     clause ("Clement... called him the New Song:") silently withheld;
#   * grounding_net's quoted-span check found no spans, so the verbatim
#     branch - the LENIENT path, the one that exists so framing words around
#     a real quote can never sink a real quote - was skipped entirely and
#     the sentence fell through to the ratio floor instead.
#
# Handled as families rather than one merged character class so a stray
# closer of one kind can never cancel a genuine opener of another. Curly
# DOUBLE quotes are included (they are unambiguous by character alone, so
# they need no context guard); curly SINGLE quotes are deliberately NOT -
# U+2019 is overwhelmingly an apostrophe in this corpus, and this module's
# own v1 postmortem records what apostrophe ambiguity costs.
_SYMMETRIC_QUOTES = ("'", '"')
_ASYMMETRIC_QUOTES = (("\u201c", "\u201d"),)


def _guarded_quote_pair(char: str) -> tuple[re.Pattern, re.Pattern]:
    """Open and close patterns for a delimiter that is the SAME character on
    both sides - position is the only thing that can tell them apart."""
    q = re.escape(char)
    return (
        re.compile(rf"(?:^|[\s:,\-(]){q}(?=\S)"),
        re.compile(rf"(?<=\S){q}(?=[\s.,;:!?)]|$)"),
    )


_QUOTE_FAMILIES: tuple[tuple[re.Pattern, re.Pattern], ...] = tuple(
    _guarded_quote_pair(c) for c in _SYMMETRIC_QUOTES
) + tuple((re.compile(re.escape(o)), re.compile(re.escape(c))) for o, c in _ASYMMETRIC_QUOTES)

# Kept as names because engine.m4.grounding_net has always imported them;
# they are the straight-single family, which is what every existing caller
# meant by them.
_QUOTE_OPEN, _QUOTE_CLOSE = _QUOTE_FAMILIES[0]


def _quote_balance(text: str) -> int:
    """Unclosed openers across all families. Per-family and floored at zero
    per family, so a stray closer of one kind contributes 0 rather than
    cancelling a real unclosed opener of another - which preserves, exactly,
    the "a lone false closer can't force a merge" property the single-family
    version had."""
    return sum(
        max(0, len(open_re.findall(text)) - len(close_re.findall(text)))
        for open_re, close_re in _QUOTE_FAMILIES
    )


def _quoted_spans(text: str) -> list[str]:
    """Every quoted span in `text`, walked per family so a single-quoted and
    a double-quoted span can never be mispaired with each other. A span
    nested inside another is returned as well as its container; every caller
    requires ALL spans to be verbatim in a cited record, and a nested span is
    a substring of its container, so reporting both is stricter, never
    looser. Owned here rather than in engine.m4.grounding_net (where it used
    to live) for the same reason the splitter is: M1's gates, M2's demo
    tagging and M4's live net must agree on where a quotation is, by
    construction."""
    spans: list[str] = []
    for open_re, close_re in _QUOTE_FAMILIES:
        pos = 0
        while True:
            open_m = open_re.search(text, pos)
            if not open_m:
                break
            close_m = close_re.search(text, open_m.end())
            if not close_m:
                break
            spans.append(text[open_m.end() : close_m.start()])
            pos = close_m.end()
    return spans


def _quote_aware_sentences(text: str) -> list[str]:
    """The naive splitter above, then re-merge any split that landed inside
    an open quotation - 'Behold the might of the new song! It has made
    men...' is one quoted span, not two sentences, and splitting it
    orphans a tag (or a scoring pass) from half the claim it grounds."""
    merged: list[str] = []
    for piece in _sentences(text):
        if merged and _quote_balance(merged[-1]) > 0:
            merged[-1] = merged[-1] + " " + piece
        else:
            merged.append(piece)
    return merged


def _overlap_coefficient(query_words: set[str], record: dict) -> float:
    """Overlap-coefficient lexical score: shared content words over the
    SMALLER of the query and the record's own word set - a short query
    scored against a long record isn't penalized for being short, and a
    long query against a short record isn't penalized either. Named
    distinctly from _grounding_ratio below (same file, different metric
    and purpose - that one scores a sentence against the union of its OWN
    cited records' words, denominator = the sentence's own length; this
    one ranks a candidate record's relevance to a query, denominator =
    the smaller set) so the two can never be confused or accidentally
    shadow one another. The one implementation both engine.m2.builders
    (compile-time demonstration tagging) and engine.m4.evidence (Stage B
    candidate ranking) score against, so the same query scored against
    the same record can never silently diverge between compile time and
    runtime."""
    words = _content_words(_all_text(record))
    if not words or not query_words:
        return 0.0
    shared = query_words & words
    return len(shared) / min(len(query_words), len(words))


# Language that shows a record is already NAMING a gap honestly in its own
# prose, rather than narrating past it - a hit here means the record IS the
# correct handling of a thin_topic, not a violation of it. Distinct from
# gate 3's _SCAFFOLD_MARKERS (that list catches vocational-honesty framing;
# this one catches the actual admission-of-absence phrasing).
_HEDGE_MARKERS = (
    "i must be honest", "i will not invent", "i will not put words",
    "i do not have", "i cannot show you", "not preserved", "not recoverable",
    "no female-authored", "our record does not", "does not give me",
    "does not give us", "not kept", "almost nothing", "i will not pretend",
    "and i will not invent one",
)


def gate_caution_crosscheck_v1(records, fleet, registry) -> list[str]:
    findings = []
    world_cores = {r["world_id"]: r for r in records.values() if r.get("record_type") == "world_core"}
    high_confidence = {"Documented", "Widely Accepted"}
    for rid, rec in records.items():
        if rec.get("record_type") == "world_core":
            continue
        if rec.get("register") != "emic":
            continue
        confidence = rec.get("confidence") or {}
        if confidence.get("formation_confidence") not in high_confidence:
            continue
        if confidence.get("divergence_note"):
            continue
        core = world_cores.get(rec.get("world_id"))
        if not core:
            continue
        full_text = _all_text(rec)
        text_lower = full_text.lower()
        if any(marker in text_lower for marker in _HEDGE_MARKERS):
            continue  # already names the gap honestly in its own prose - not a violation
        if rec.get("record_type") == "honest_limit" or "honest-limit" in (rec.get("tags") or []):
            continue  # this record's entire job is to state a limit - trust its own field discipline
        all_hits = []
        hit_notes = []
        for topic in core.get("thin_topics") or []:
            hits = [kw for kw in (topic.get("keywords") or []) if kw.lower() in text_lower]
            if hits:
                all_hits.extend(hits)
                hit_notes.append(topic.get("note"))
        # a single bare keyword mention (a name in passing, one incidental
        # word) is too weak a signal on its own - "widow" inside a martyrdom
        # story about someone's WIFE, or "Didymus" naming him as a teacher,
        # both hit on a single keyword with no real claim about the thin
        # topic itself. Requiring >= 2 hits is a density proxy for "this
        # record is actually asserting something in the gap area," not just
        # touching it in passing. Tuned against one known case so far -
        # needs testing against more before trusting the threshold generally.
        if len(all_hits) >= 2:
            findings.append(
                f"{rid}: formation_confidence={confidence.get('formation_confidence')!r} with no "
                f"divergence_note or in-text hedge, but text hits {len(all_hits)} thin_topic keywords "
                f"{all_hits} across {core['id']}'s named gaps ({'; '.join(hit_notes)})"
            )
    return findings


def gate_unsupported_claim_v1(records, fleet, registry) -> list[str]:
    findings = []
    checked_types = {"demonstration", "doctrinal_witness", "story"}
    for rid, rec in records.items():
        if rec.get("record_type") not in checked_types or rec.get("register") != "emic":
            continue

        cited_words: set[str] = set()
        has_checkable_source = False
        for src in rec.get("sources") or []:
            cited = records.get(src.get("source_id")) or fleet.get(src.get("source_id"))
            if not cited or cited.get("record_type") == "source":
                continue  # raw source metadata carries no body text to check against
            has_checkable_source = True
            cited_words |= _content_words(_all_text(cited))
        if not has_checkable_source:
            continue  # nothing to check against - not this gate's job

        if rec.get("record_type") == "demonstration":
            own_text = " ".join(
                t.get("text", "") for t in rec.get("exchange") or [] if t.get("speaker") == "representative"
            )
        else:
            own_text = rec.get("text") or rec.get("statement") or ""

        for sentence in _sentences(own_text):
            words = _content_words(sentence)
            if len(words) < 6:
                continue
            if any(marker in sentence.lower() for marker in _SCAFFOLD_MARKERS):
                continue
            if not (words & cited_words):
                findings.append(
                    f"{rid}: zero lexical overlap with any cited internal source's own text - "
                    f"candidate unsupported claim: {sentence!r}"
                )
    return findings


# v1 gates end here (kept for the record of what was tried and why it fell
# short - not registered below). v2 starts here.

# "one" deliberately excluded - overwhelmingly used as a pronoun/article
# ("the one asking", "one thing") rather than a quantity, which made it the
# single largest false-positive source in testing.
_SPELLED_NUMBERS = {
    "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand",
}
_DIGIT = re.compile(r"\b\d+\b")

# grounding ratio below which a specific claim counts as ungrounded. Chosen
# empirically (see the test run this was calibrated against): high enough
# that a real quoted/cited sentence (which shares most of its own words with
# the source it's quoting) clears it easily, low enough that a sentence
# built mostly from words with no citation behind them does not.
_GROUNDING_FLOOR = 0.4


# Capitalized by religious convention, not because they name a specific,
# checkable entity - "God" appears in nearly every sentence a Christian-
# formation voice speaks, and treating that as evidence of a documentary
# claim would flag almost everything. Proper-noun detection is meant to
# catch a real person/place/text (Clement, Basilides, Nicaea), not the
# doctrinal vocabulary that IS the subject matter.
_DOCTRINAL_VOCAB = {
    "god", "god's", "word", "logos", "christ", "spirit", "father", "son",
    "trinity", "scripture", "gospel", "church", "lord",
}


def _proper_nouns(sentence: str) -> set[str]:
    """Capitalized words not at the start of a clause - a cheap, no-
    dictionary proxy for named people/places/texts. A colon or semicolon
    starts a new independent clause grammatically, same as a sentence
    boundary, so the word right after one is skipped too - otherwise "...
    argue: I have to be honest" flags "I" as a proper noun for no reason
    beyond where a colon happened to land."""
    words = _WORD.findall(sentence)
    clause_starts = {0}
    for m in re.finditer(r"[:;]\s*", sentence):
        tail = sentence[m.end():]
        tail_words = _WORD.findall(sentence[: m.end()])
        if tail_words:
            clause_starts.add(len(tail_words))
    # "I'd", "I'll", "I've", "I'm" are the word "I" plus a contraction, not
    # a name - excluding bare "I" alone (the earlier version of this check)
    # missed every contracted form, since the regex keeps the apostrophe as
    # part of the token.
    return {
        w.lower() for i, w in enumerate(words)
        if i not in clause_starts
        and w[0].isupper()
        and w.lower() not in _STOPWORDS
        and w.lower() not in _DOCTRINAL_VOCAB
        and not re.match(r"i'", w, re.IGNORECASE)
        and w != "I"
    }


def _has_number(sentence: str) -> bool:
    if _DIGIT.search(sentence):
        return True
    words = {w.lower() for w in _WORD.findall(sentence)}
    return bool(words & _SPELLED_NUMBERS)


def _has_enumeration(sentence: str) -> bool:
    """The "same water, the same bread... Greeks and Egyptians... men and
    women" shape specifically: a repeated short phrase, or several SHORT
    (<=4-word) comma/and-separated items in a row - a known pattern for
    dressing invented texture up as vivid, documentary-sounding detail.
    An ordinary multi-clause sentence has commas too, but its segments are
    full clauses, not short parallel items - so raw comma-count alone
    (v2's first draft) is not the signal; segment shortness is."""
    lowered = sentence.lower()
    if lowered.count("the same ") >= 2:
        return True
    if ";" in sentence:
        return False  # a semicolon joins independent clauses, not list items
    segments = re.split(r",| and ", sentence)
    short_segments = [s for s in segments if 0 < len(_WORD.findall(s)) <= 4]
    return len(short_segments) >= 3


def _claim_markers(sentence: str) -> list[str]:
    """Positive detection: does this sentence even make a checkable claim?
    Empty result means it's interpretive/values framing - skip it outright,
    rather than firing on everything and trying to exempt framing after the
    fact (v1's mistake)."""
    markers = []
    proper_nouns = _proper_nouns(sentence)
    if proper_nouns:
        markers.append(f"proper-noun:{sorted(proper_nouns)}")
    if _has_number(sentence):
        markers.append("number")
    if _has_enumeration(sentence):
        markers.append("enumeration")
    return markers


def _grounding_ratio(sentence: str, cited_words: set[str]) -> float:
    words = _content_words(sentence)
    if not words:
        return 1.0
    return len(words & cited_words) / len(words)


def gate_grounded_claim(records, fleet, registry) -> list[str]:
    findings = []
    world_cores = {r["world_id"]: r for r in records.values() if r.get("record_type") == "world_core"}
    checked_types = {"demonstration", "doctrinal_witness", "story"}

    for rid, rec in records.items():
        if rec.get("record_type") not in checked_types or rec.get("register") != "emic":
            continue
        if rec.get("record_type") == "honest_limit" or "honest-limit" in (rec.get("tags") or []):
            continue

        cited_words: set[str] = set()
        has_checkable_source = False
        for src in rec.get("sources") or []:
            cited = records.get(src.get("source_id")) or fleet.get(src.get("source_id"))
            if not cited or cited.get("record_type") == "source":
                continue  # raw source metadata carries no body text to check against
            has_checkable_source = True
            cited_words |= _content_words(_all_text(cited))
        if not has_checkable_source:
            continue  # nothing to check against - not this gate's job

        if rec.get("record_type") == "demonstration":
            own_text = " ".join(
                t.get("text", "") for t in rec.get("exchange") or [] if t.get("speaker") == "representative"
            )
        else:
            own_text = rec.get("text") or rec.get("statement") or ""

        core = world_cores.get(rec.get("world_id"))

        for sentence in _sentences(own_text):
            sentence_lower = sentence.lower()
            if any(marker in sentence_lower for marker in _SCAFFOLD_MARKERS):
                continue
            if _SELF_NAMING_MARKER in sentence_lower:
                continue  # self-naming, not a claim about the world - nothing to ground
            markers = _claim_markers(sentence)
            if not markers:
                continue  # no checkable claim in this sentence - interpretive framing, not this gate's job

            ratio = _grounding_ratio(sentence, cited_words)
            if ratio >= _GROUNDING_FLOOR:
                continue  # grounded enough in its own cited sources

            thin_hits = []
            if core:
                text_lower = sentence.lower()
                for topic in core.get("thin_topics") or []:
                    hits = [kw for kw in (topic.get("keywords") or []) if kw.lower() in text_lower]
                    if hits:
                        thin_hits.append(f"{hits} ({topic.get('note')})")

            severity = "HIGH" if thin_hits else "MEDIUM"
            escalator = f"; falls inside a named thin topic: {'; '.join(thin_hits)}" if thin_hits else ""
            findings.append(
                f"[{severity}] {rid}: specific claim ({', '.join(markers)}), only {ratio:.0%} of its own "
                f"content grounded in cited sources{escalator} - {sentence!r}"
            )
    return findings


_TENSIONAL_MARKER = re.compile(r"\[\s*tensional\b", re.IGNORECASE)


def gate_tension_coverage(records, fleet, registry) -> list[str]:
    """Informational, not a hard fail - see the module docstring's newest
    entry below for why. Flags a `gravity` record whose `name` field
    declares it [TENSIONAL] but whose `relations` carry no `tension-with`
    entry to any other record.

    Checked directly against Doc_04_Gravity_Discovery.md (alx, 2026-08-21):
    of Alexandria's four Tensional gravities, three (learning-community,
    speculative-doctrinal, martyrdom-contemplative) have a `tension-with`
    relation that traces to a genuine competing/reshaping ("C"/"X") entry
    in Doc_04's own §6 Interaction Matrix. The fourth,
    teacher-bishop-tension, has no such entry - its only matrix listing is
    "T1 <-> C5 (R)", reinforcing, already correctly recorded as
    `associated-with`, not `tension-with`. Its two named poles
    (teacher-authority, bishop-office) were never mapped onto an opposing
    gravity/force record by Doc_04's own reviewed methodology - not a
    recording error, a real asymmetry in how that document treated its
    four Tensionals.

    So a hard-fail version of this check would have forced a fabricated
    `tension-with` target onto teacher-bishop-tension the first time it
    ran - exactly the kind of invented relation this project's no-
    fabrication discipline forbids. This gate reports the same shape of
    gap instead of blocking on it, so a human (the Doc_04 reviewer, not
    the gate) decides whether a given zero-tension-with Tensional is a
    genuine asymmetry like T1 or an actual omission worth fixing.
    """
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "gravity":
            continue
        name = rec.get("name") or ""
        if not _TENSIONAL_MARKER.search(name):
            continue
        relations = rec.get("relations") or []
        if any(r.get("type") == "tension-with" for r in relations):
            continue
        findings.append(
            f"[INFO] {rid}: named {name!r} but carries no tension-with relation - "
            f"confirm against this world's Doc_04 Interaction Matrix whether this "
            f"Tensional's poles were ever mapped onto an opposing record (a real "
            f"asymmetry, as with alx's own teacher-bishop-tension) or whether one "
            f"was missed"
        )
    return findings


# Exactly the fields engine/m2/builders.py's build_prompt() reads - the
# real, current field contract for what reaches a live model, not a
# separate guess at it. Deliberately narrower than "every string field on
# these record types": doctrinal_witness.positions/tensions,
# honest_limit.why_sources_cannot_answer, and every field on gravity/
# force/contested_claim/search_record/source are NOT compiled and are
# legitimate places for build-process language to live - scanning them
# gate_no_build_attribution ADMITTED 2026-08-21 to engine/m1/gates.py's
# GATES battery (own defect-catalog entry in fixtures/seeded_defects.yaml,
# selftest-proven per this file's own admission bar, stated below). No
# longer here - see gates.py for the implementation and its full history
# comment.

EXPERIMENTAL_GATES = {
    "grounded-claim": gate_grounded_claim,
    "tension-coverage": gate_tension_coverage,
}


def run_experimental(records: dict, fleet: dict, registry: dict) -> dict[str, list[str]]:
    return {name: fn(records, fleet, registry) for name, fn in EXPERIMENTAL_GATES.items()}
