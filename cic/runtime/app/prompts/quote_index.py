"""The quotation ground truth: which sayings has this world actually
licensed a Representative to quote, and did a generated turn quote
anything else?

Same shape, same contract as figure_bridge.py's own registry loader: run
AFTER generation, read a deploy view built by the generic engine
(cic/engine/build_quotes_index.py), never influence what gets said. Two
pure, no-LLM pieces live here - loading the candidate list, and finding
the quotation-marked spans a turn actually contains. The judgment of
whether a found span matches a candidate needs an LLM call and belongs
next to get_monitoring_llm in app/graph/nodes.py, the same split
filter_grounded_citations already keeps from this module's own
find_figures_used.

Detection of WHICH text counts as "quoted" is deterministic (quotation
marks), unlike a citation's connection to the text, which is a judgment.
What matching a found span against a candidate saying MEANS is not
deterministic - a real quotation is routinely paraphrased a word or two
from its licensed text_translation - which is why that half is an LLM
call, not a string comparison, exactly as filter_grounded_citations
already argued for citations over find_glosses_used's plain substring
match.
"""
from __future__ import annotations

import functools
import json
import re

# Straight and curly double quotes. A minimum content length excludes
# scare-quoted single words ("we", "I") that are emphasis, not citation -
# every genuine quotation seen in this build's own live-model testing was
# a full clause or longer.
_QUOTE_SPAN_PATTERN = re.compile(r'["“]([^"”]{8,}?)["”]')

# The character minimum above is necessary and was never sufficient. Over
# the 54 turns of the 2026-08-17 second generation pass it yields 28
# spans, of which roughly five are quotations; the rest are three
# recognisable classes, each excluded below by a rule aimed at it alone.
#
# GLOSS - "discernment (Diakrisis)", "the thoughts that trouble the mind
#   (Logismoi)", "similar to the Father (homoios)". This is the build's
#   own three-tier convention - plain phrase, then the lexicon term in
#   parentheses - and it is never a quotation.
#
# EMPHASIS - "important", "three weeks", "the Gospel,", "a holy man.".
#   Scare quotes on a phrase. Nobody's words are being put in anybody's
#   mouth, which is the only thing this gate exists to ask about. The
#   floor is four WORDS, extending the character rule's own argument with
#   what the corpus shows: the shortest genuine quotations found across
#   both passes - "Let this cup pass", "the blood of God," - sit exactly
#   at four, and everything below is emphasis.
#
# RUNAWAY - spans of 29, 66, 138 and 199 words that cross sentence
#   boundaries and paragraph breaks, produced when an unmatched opening
#   quote pairs with a later unrelated one. They begin mid-sentence in
#   lowercase, which a genuine multi-sentence quotation does not.
#
# MEASURED, not asserted. Tuned on that pass: 28 spans down to 10.
# Then run unchanged over the FIRST pass's 54 turns - different
# retrieval, different answers, never used for tuning, and far heavier on
# real scripture and patristic quotation: 27 spans down to 19, and every
# one of the seven dropped is a one-to-three word emphasis fragment
# ("properly.", "just receive", "was this natural"). No genuine quotation
# was lost on either pass, which is the property that matters - this gate
# may only ever go quiet about things that were never citations.
_MIN_QUOTED_WORDS = 4
# A trailing parenthetical is the gloss convention's own signature.
_GLOSS_TAIL = re.compile(r"\([^()]{2,40}\)\s*[.,;:]?\s*$")
# A paragraph break inside a quotation is always the unmatched-quote bug.
_QUOTE_HAS_BREAK = re.compile(r"[\n\r]")
# A sentence boundary with more text after it.
_QUOTE_INTERNAL_SENTENCE = re.compile(r"[.!?][\"”)]?\s+\S")


@functools.lru_cache(maxsize=16)
def _registry(world_id: str) -> tuple:
    """Licensed quotes for a world, from data/<world>/quotes.json (built by
    cic/engine/build_quotes_index.py). Returns a tuple of frozen dicts-as-
    tuples-of-items is unnecessary here since callers never mutate entries -
    a tuple of the raw dicts is enough to make the cache itself immutable.

    Fails toward the EMPTY registry - a world whose file is missing,
    unreadable, or not yet built (no quote/ records authored) simply has no
    candidates, exactly as figure_bridge._registry fails toward no bridged
    figures. A missing file is never distinguished from a world with zero
    quotes: both mean "nothing to check against," which the caller in
    nodes.py must treat as automatic UNLICENSED for anything quoted,
    not as "check skipped."
    """
    try:
        from app.config import settings
        path = settings.get_world_config(world_id).data_path / "quotes.json"
        entries = json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return ()
    return tuple(entries)


def licensed_quotes(world_id: str) -> tuple:
    """Public accessor - the candidate list nodes.py judges spans against."""
    return _registry(world_id)


def extract_quoted_spans(response_text: str) -> list[str]:
    """Every quotation-marked span in a generated turn that is plausibly a
    CITATION, in order of appearance, deduplicated (a voice repeating the
    same line twice in one turn is one grounding question, not two).

    Quotation marks are necessary and not sufficient: this build quotes to
    gloss a term and to lend a phrase emphasis, neither of which puts
    words in anyone's mouth. See the derivation note above the exclusion
    constants for what each rule removes and what it was measured at.
    """
    if not response_text:
        return []
    seen: list[str] = []
    for match in _QUOTE_SPAN_PATTERN.finditer(response_text):
        span = match.group(1).strip()
        if not span or span in seen:
            continue
        if len(span.split()) < _MIN_QUOTED_WORDS:
            continue
        if _GLOSS_TAIL.search(span):
            continue
        if _QUOTE_HAS_BREAK.search(span):
            continue
        # A real multi-sentence quotation opens with a capital. One that
        # opens mid-sentence and then runs past a full stop is the
        # extractor having started at the wrong quote mark.
        if _QUOTE_INTERNAL_SENTENCE.search(span) and not span[:1].isupper():
            continue
        seen.append(span)
    return seen


# --------------------------------------------------------------------------
# Attributed indirect speech - the half quotation marks do not catch.
#
# WHY THIS EXISTS. The 2026-08-17 generation audit found two fabrications
# this module's quotation-mark extractor is structurally blind to, because
# neither is quotation-marked:
#
#   Antony taught: better a man who prays badly but knows himself weak,
#   than one who works wonders and thinks he stands alone.
#       - a saying minted whole and hung on a named person. Absent from
#         records/desert/ and deploy/desert/ alike. Papnoute's permanent
#         prompt forbids exactly this in four separate places, ending "we
#         do not mint sayings. A word in the saying-shape that no one of
#         us actually said would travel as though someone had."
#
#   ...wrote back, almost disappointed, that it was ordinary food.
#       - Pliny's testimony, real and carried in pahcstory004, with the
#         name that makes it evidence stripped off.
#
# On those two turns extract_quoted_spans returns one span and zero spans
# respectively - and the one span is a lexicon gloss, not a quotation. A
# representative that attributes a saying WITHOUT quotation marks is
# invisible to the grounding gate. That is the gap these patterns close.
#
# HOW THEY WERE DERIVED, and what that is worth. Tuned on the 54 turns of
# the second generation pass, where they find 9 spans (0.2 per turn), all
# 9 genuine attributed speech. Tuned on - so that figure is a fit, not a
# measurement. Then run unchanged over the 54 turns of the FIRST pass,
# different retrieval and different answers, never used for tuning: 4
# spans, all 4 genuine. That held-out run is the number worth anything.
#
# Recall is established by neither. These catch the colon form and the
# close that-clause; an attribution phrased another way still passes
# unseen. This narrows the blind spot, it does not close it.

# Verbs that report SPEECH. "shows", "suggests", "indicates" are
# deliberately absent - a record showing something is the turn reasoning
# from its material, not the turn putting words in a named mouth.
_SPEECH_VERB = (r"(?:taught|teaches|wrote|writes|said|says|told|tells|"
                r"put it|puts it|answered|answers|replied|replies|"
                r"reports|records|describes|calls it)")

# Form A: <Name> <speech verb>: <clause>
_ATTRIBUTED_COLON = re.compile(
    rf"\b([A-Z][\w'’\-]*(?:\s+(?:of|the|[a-z]{{1,4}}|[A-Z][\w'’\-]*)){{0,3}})\s+"
    rf"{_SPEECH_VERB}\s*:\s*([^.!?\n]{{12,}}[.!?])")

# Form B: <speech verb> ... that <clause>. The 30-character bridge is the
# working limit found by sweep: below it Pliny's ", almost disappointed,"
# is lost; well above it the relative-pronoun uses start coming in.
_ATTRIBUTED_THAT = re.compile(
    rf"\b(?<!\bthat )({_SPEECH_VERB})\b([^.!?\n]{{0,30}}?)\bthat\s+"
    rf"([^.!?\n]{{12,}}[.!?])")

# The turn declaring an ABSENCE - "does not tell us", "never says",
# "nowhere records" - is the opposite of the failure being hunted.
_ATTRIBUTED_NEGATED = re.compile(
    r"(?:not|never|n't|no|cannot|can't|nowhere)\s+(?:\w+\s+){0,2}$")

# "that" as a RELATIVE PRONOUN attaches to the noun in front of it - "a
# synod that had deposed", "a community that already has", "every question
# that could be put". A determiner plus a noun immediately before "that"
# is the signature, and no true attribution carries it.
_ATTRIBUTED_RELATIVE = re.compile(
    r"\b(?:a|an|the|every|each|any|one|another|some|no)\s+[\w'’\-]+\s*,?\s*$",
    re.IGNORECASE)
_ATTRIBUTED_SUBORDINATOR = re.compile(
    r"\b(?:as though|as if|so|now|such|given|in)\s*$", re.IGNORECASE)

# A complementizer "that" opens a CLAUSE, so a pronoun, determiner or
# subordinator follows it. A demonstrative determiner is followed by its
# own noun - "that day in church", "that night", "that silence is heard" -
# which is what every remaining false fire turned out to be.
_ATTRIBUTED_CLAUSE_OPENER = re.compile(
    r"^(?:it|he|she|they|we|you|i|this|these|those|the|a|an|if|when|while|"
    r"what|there|his|her|their|our|its|my|no|nothing|someone|somewhere|"
    r"anyone|anything|everything|both|each|one|since|because|by|for)\b",
    re.IGNORECASE)


def extract_attributed_spans(response_text: str) -> list[str]:
    """Every span where the turn attributes speech to someone WITHOUT
    quotation marks, in order of appearance, deduplicated.

    Deterministic and LLM-free, exactly like extract_quoted_spans, and
    judged downstream by the same batched call. See the block comment
    above for what these rules were measured at, and what they miss.
    """
    if not response_text:
        return []
    seen: list[str] = []

    for match in _ATTRIBUTED_COLON.finditer(response_text):
        span = f"{match.group(1)} ...: {match.group(2).strip()}"
        if span not in seen:
            seen.append(span)

    for match in _ATTRIBUTED_THAT.finditer(response_text):
        preceding = response_text[max(0, match.start() - 40):match.start()]
        if _ATTRIBUTED_NEGATED.search(preceding):
            continue
        bridge = match.group(2)
        if (_ATTRIBUTED_RELATIVE.search(bridge)
                or _ATTRIBUTED_SUBORDINATOR.search(bridge)):
            continue
        clause = match.group(3).strip()
        if not _ATTRIBUTED_CLAUSE_OPENER.match(clause):
            continue
        span = f"...{match.group(1)}{bridge} that {clause}"
        if span not in seen:
            seen.append(span)

    return seen
