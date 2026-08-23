"""Deterministic prose measurement, shared across modules.

Tokenizing, sentence splitting, quote-aware splitting, lexical overlap,
and the claim-marker rules. Nothing here decides policy; each caller
decides what to do with the measurement.

This code used to live in `gates_experimental.py`, whose own docstring
said it was "NOT yet in gates.GATES / the accepted battery... candidates
for human review, not a pass/fail verdict". That was true of the gates in
that file, and it is still true - they remain there, and still do not run.
It was never true of these primitives. Four production modules had reached
across the boundary for them by their private names, because this was the
only implementation of any of it in the codebase:

    engine/m1/canon.py          the cell keyword corpus - whether a
                                question reaches any ground at all
    engine/m2/builders.py       compile-time demonstration tagging
    engine/m4/evidence.py       Stage A/B retrieval scoring
    engine/m4/grounding_net.py  every per-sentence verdict

They are load-bearing, so they are public, named plainly, and live in a
file whose name does not tell a reader they are experimental. The split is
a move: not one character of behaviour changed with it.

One constant, GROUNDING_FLOOR, was doing two unrelated jobs on two
different metrics. It is now DEMONSTRATION_TAG_FLOOR and WITHHOLD_FLOOR -
same value, separately settable, each documented against the measurement
it actually gates. See their comment below.
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
SCAFFOLD_MARKERS = (
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
SELF_NAMING_MARKER = "i am a representative of"


_WORD = re.compile(r"[a-zA-Z']+")


_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def all_text(rec: dict) -> str:
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


def content_words(text: str) -> set[str]:
    words = (w.lower() for w in _WORD.findall(text))
    return {w for w in words if w not in _STOPWORDS and len(w) > 2}


def sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENTENCE_SPLIT.split(text or "") if s.strip()]


# An opening quote is a straight single quote at start-of-text or after
# space/colon/comma/dash; a closing one is followed by space, punctuation,
# or end. Apostrophes inside words ("God's") match neither. A lone false
# closer (teachers') can't force a merge because merging only triggers
# while openers outnumber closers. Shared here (not left as an engine.m4-
# only concern) because M2's compile-time demonstration tagging needs the
# identical quote-aware split M4's live net uses - one splitter, owned
# once, so a demo tagged at compile time and a live turn checked at
# generation time can never silently disagree about where a sentence ends.
# Straight single AND double quotes. Double quotes were missing, and the
# corpus already holds 249 paired double-quoted spans - so a sentence
# quoting with " split inside the quotation and the orphan reached a
# participant on its own. Seen live on alx: `It has made men out of stones,
# men out of beasts".` was shown while its own opening clause, "Clement,
# one of our first teachers, called him the New Song:", was withheld for
# having no tag. A live model quotes with " far more readily than with ',
# whatever the prompt around it does.
QUOTE_OPEN = re.compile(r"""(?:^|[\s:,\-(])['"](?=\S)""")


QUOTE_CLOSE = re.compile(r"""(?<=\S)['"](?=[\s.,;:!?)]|$)""")


def _quote_balance(text: str) -> int:
    return len(QUOTE_OPEN.findall(text)) - len(QUOTE_CLOSE.findall(text))


def quote_aware_sentences(text: str) -> list[str]:
    """The naive splitter above, then re-merge any split that landed inside
    an open quotation - 'Behold the might of the new song! It has made
    men...' is one quoted span, not two sentences, and splitting it
    orphans a tag (or a scoring pass) from half the claim it grounds."""
    merged: list[str] = []
    for piece in sentences(text):
        if merged and _quote_balance(merged[-1]) > 0:
            merged[-1] = merged[-1] + " " + piece
        else:
            merged.append(piece)
    return merged


def overlap_coefficient(query_words: set[str], record: dict) -> float:
    """Overlap-coefficient lexical score: shared content words over the
    SMALLER of the query and the record's own word set - a short query
    scored against a long record isn't penalized for being short, and a
    long query against a short record isn't penalized either. Named
    distinctly from grounding_ratio below (same file, different metric
    and purpose - that one scores a sentence against the union of its OWN
    cited records' words, denominator = the sentence's own length; this
    one ranks a candidate record's relevance to a query, denominator =
    the smaller set) so the two can never be confused or accidentally
    shadow one another. The one implementation both engine.m2.builders
    (compile-time demonstration tagging) and engine.m4.evidence (Stage B
    candidate ranking) score against, so the same query scored against
    the same record can never silently diverge between compile time and
    runtime."""
    words = content_words(all_text(record))
    if not words or not query_words:
        return 0.0
    shared = query_words & words
    return len(shared) / min(len(query_words), len(words))

# "one" deliberately excluded - overwhelmingly used as a pronoun/article
# ("the one asking", "one thing") rather than a quantity, which made it the
# single largest false-positive source in testing.
SPELLED_NUMBERS = {
    "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand",
}


_DIGIT = re.compile(r"\b\d+\b")

# Two floors, one number, and they were a single constant until now. They
# are separated because they are not even the same measurement:
#
#   DEMONSTRATION_TAG_FLOOR  engine.m2.builders, compile time. Scores an
#                            overlap coefficient - shared words over the
#                            SMALLER of the sentence and the candidate
#                            record. Decides whether a demonstration
#                            sentence earns a citation tag baked into the
#                            package.
#   WITHHOLD_FLOOR           engine.m4.grounding_net, run time. Scores a
#                            grounding ratio - shared words over the
#                            SENTENCE'S OWN length. Decides whether a
#                            sentence a Representative just produced
#                            reaches the participant at all.
#
# Different denominators mean 0.4 does not mean the same thing on both
# sides, so one number governing both was a coincidence of authorship, not
# a shared decision. Both are 0.4 today, which is where they were before
# the split - nothing moved, and moving either one needs its own
# measurement (Program-Spec principle 10: measured, not asserted). Neither
# has a baseline behind it yet; the value was chosen by eye.
DEMONSTRATION_TAG_FLOOR = 0.4
WITHHOLD_FLOOR = 0.4


# Capitalized by religious convention, not because they name a specific,
# checkable entity - "God" appears in nearly every sentence a Christian-
# formation voice speaks, and treating that as evidence of a documentary
# claim would flag almost everything. Proper-noun detection is meant to
# catch a real person/place/text (Clement, Basilides, Nicaea), not the
# doctrinal vocabulary that IS the subject matter.
# Looked up with a trailing "s" stripped, because the plural was the actual
# defect: "scripture" was already exempt and "Scriptures" was not, so the
# net struck a sentence for saying the word Scriptures, and struck
# "Christian" every time a Christian representative used it of itself.
_DOCTRINAL_VOCAB = {
    "god", "god's", "word", "logos", "christ", "spirit", "father", "son",
    "trinity", "scripture", "gospel", "church", "lord", "christian",
    "christianity", "apostle", "psalm", "testament",
}


def _is_common_vocab(word: str) -> bool:
    w = word.lower()
    return w in _DOCTRINAL_VOCAB or (w.endswith("s") and w[:-1] in _DOCTRINAL_VOCAB)


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
        and not _is_common_vocab(w)
        and not re.match(r"i'", w, re.IGNORECASE)
        and w != "I"
    }


# "two ways to take your question" - the voice counting its own readings
# aloud, not a figure about the world. Over 17 measured live turns this
# shape accounted for every spelled-number false positive, and striking it
# decapitated the answer: the opening sentence went and the participant was
# handed a list starting at item two. Gated on the sentence actually being
# about the ask - "he would read a passage three ways" counts a doctrine,
# and an earlier draft of this rule wrongly freed it.
_DISCOURSE_COUNT = re.compile(
    r"\b(?:one|two|three|four|five)\s+(?:possible\s+|different\s+|separate\s+)?"
    r"(?:ways?|readings?|questions?|meanings?)\b",
    re.IGNORECASE,
)
_ABOUT_THE_ASK = re.compile(
    r"\b(?:your question|you(?:'re| are)? ask\w*|what you(?:'ve| have)? asked|"
    r"which you mean|you meant|the one you meant|take your question)\b",
    re.IGNORECASE,
)


def _has_number(sentence: str) -> bool:
    if _DIGIT.search(sentence):
        return True  # a digit is always a figure or a date
    words = {w.lower() for w in _WORD.findall(sentence)}
    if not words & SPELLED_NUMBERS:
        return False
    if not _ABOUT_THE_ASK.search(sentence):
        return True
    stripped = _DISCOURSE_COUNT.sub(" ", sentence)
    return bool({w.lower() for w in _WORD.findall(stripped)} & SPELLED_NUMBERS)


def _has_enumeration(sentence: str) -> bool:
    """NARROWED to the repeated-phrase signal it was built for. The
    short-segment count went with it: measured over 17 live turns it fired
    9 times and every one was ordinary parallel prose ("We lived among
    them, learned from them, argued with them."). Short parallel clauses
    are what register statements 2 and 3 ask the voice to write, so the
    rule was deleting the register it exists beside."""
    return sentence.lower().count("the same ") >= 2


def claim_markers(sentence: str) -> list[str]:
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


def grounding_ratio(sentence: str, cited_words: set[str]) -> float:
    words = content_words(sentence)
    if not words:
        return 1.0
    return len(words & cited_words) / len(words)
