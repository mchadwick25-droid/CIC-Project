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


# Keys whose string values are structure, not prose. all_text() is
# deliberately generic - it walks every string in a record so it works across
# every record type without a per-type field map - and the cost of that is
# this list: anything NOT named here is treated as something the world said.
#
# The four identifier keys at the end were missing, and they were not inert.
# A dotted id tokenizes into ordinary words: alx.source.origen-philocalia
# becomes {alx, source, origen, philocalia}. So
# alx.gravity.scripture-formative "contained" the words origen, clement and
# athanasius purely because it CITES sources with those names - and a
# sentence naming Origen scored as grounded in a record that says nothing
# about him. Measured across the six worlds: 4,203 of 83,511 content words
# (5.0%) came from identifiers alone, and 518 of those 548 distinct tokens
# also occur in real prose, so they collide rather than sitting harmlessly
# unmatched.
#
# This reaches every lexical score in the system - grounding_ratio's cited
# side, overlap_coefficient, the M1 cell keyword corpus, M2's demonstration
# tagging and M4's Stage B ranking all read all_text().
#
# retrieval hints (retrieve_when) are deliberately NOT here: that field was
# authored to be matched on.
#
# do_not_retrieve_when IS excluded (fixed 2026-09-19, Opus adversarial review
# finding D1). It was previously reasoned about together with retrieve_when
# above and left in all_text()'s pool, but reading the real records shows it
# holds a genuine anti-fabrication guard species alongside its redirect
# species - e.g. "our vendored evidence does not say [X], and the
# Representative must not supply it." Leaving that text in all_text() means
# grounding_ratio's own word-overlap check can score a FABRICATED version of
# exactly the barred claim as well-grounded, because the guard sentence that
# forbids the claim necessarily shares the claim's own vocabulary - measured
# directly: a fabricated "Brictio succeeded Martin as bishop" scored a
# perfect 1.0 grounding ratio against gallic.story.brictio-in-the-courtyard,
# whose own do_not_retrieve_when says exactly that this is not attested and
# must not be invented. This is the same category formation_claim_barred
# below is already in - a forbidden claim's own text is not "prose that
# might ground a real answer," it is the opposite.
NON_PROSE_KEYS = {
    "id", "world_id", "record_type", "schema_version", "status", "register",
    "_path", "_body", "world_word", "license", "narrative_tier",
    "formation_claim_barred", "citation_specificity", "verification_state",
    "evidentiary_weight", "formation_confidence",
    "canon_cells", "source_id", "target", "canon_question_id",
    "do_not_retrieve_when",
}


# Build-team editorial/interpretive commentary, not citable content - a
# record's own honest self-critique of its evidentiary limits, written for
# whoever reviews the record, never for a participant. all_text() (and
# NON_PROSE_KEYS above) keeps these on purpose for grounding_net's own job
# (checking whether the MODEL's generated text is grounded - a much broader
# "is this substring anywhere in the record" check with a different failure
# mode if it's too narrow). A RETRIEVAL ranking's job is the opposite risk:
# finding the WRONG record because a query word happened to appear in a
# caveat about the record rather than in the record's own substance.
# Measured directly (engine.m4.evidence's Stage A2 fallback, 2026-08-27):
# pahc.term.ministrae's own `senses.informational` field reads "...women
# held service in that church important enough that its interrogator chose
# them as the ones who would know" - a real sentence, but about Pliny's
# interrogation, not about why anything was important in the sense a
# participant asking "why was Jesus important" means. That single word, in
# that one commentary field, was enough to surface a completely unrelated
# record before this exclusion existed. `do_not_retrieve_when` is excluded
# for a sharper reason: matching on it would retrieve a record's own list of
# reasons NOT to retrieve it. `retrieve_when` is excluded for that same
# sharper reason, on a regression it caused the day 124 quote records were
# hinted at once: a hint is retrieval vocabulary written in the
# PARTICIPANT'S words, which is precisely the vocabulary a retrieval ranking
# matches on, so every hinted record started matching every hint word and
# document frequency climbed until an honestly-discriminating word stopped
# discriminating at all (measured: "believe" went from matching 4 records to
# 7 on pahc, and a real question lost its answer). Hints belong in cell
# vocabulary, scored against a curated per-cell corpus - not in a general
# retrieval ranking, where raw frequency is the whole safeguard.
#
# Shared by every retrieval-ranking consumer so they can't drift apart:
# engine.m4.evidence's Stage A2 fulltext fallback (the original use case
# this was measured against) and engine.m2.builders's compile-time
# retrieval index (Build-Plan.md Stage 4c) both exclude the identical set.
FALLBACK_EXCLUDED_KEYS = {"senses", "divergence_note", "modern_lens_note", "distortion_risk", "false_friend", "do_not_retrieve_when", "retrieve_when"}


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
    # The closed class was incomplete, and the gap was found the way the
    # others were - by a check believing it. engine.m4.output_check asks
    # whether a participant's claim of prior discourse shares any word with
    # what was actually said; "Earlier you mentioned a woman among you by
    # name" shared exactly one word with two turns about bread and baskets,
    # and it was "among". A preposition vouched for a memory that never
    # happened. These are siblings of the prepositions already listed
    # above (between, against, about, from, into, over, under) - completing
    # a closed class, not tuning one check's outcome.
    "among", "amongst", "through", "throughout", "during", "within",
    "without", "upon", "across", "toward", "towards", "beyond", "beside",
    "near", "off", "per", "onto", "unto", "along", "around", "behind",
    # Contractions tokenize as single words - the apostrophe is a word
    # character in _WORD - so every one of these was a CONTENT word until
    # 2026-08-27, scored as evidence about a cell like any noun. Found by a
    # live turn: "You've given me two different pictures there. Did your own
    # people disagree about this?" routed to F6-P on `people` and `you've`,
    # and to F2-E on `given` and `you've` - not one word that carries the
    # actual ask matched anything, and the voice answered a question about
    # women elders that nobody had asked.
    #
    # Fourteen apostrophe tokens sat in the canon's own cell vocabularies
    # (`isn't` in four cells, `can't`/`couldn't`/`what's`/`you've` in two
    # each). Twelve are pure function words and are listed here. TWO ARE
    # NOT and are deliberately absent: `women's` and `world's` are
    # possessives of content nouns and remain evidence.
    "can't", "couldn't", "didn't", "doesn't", "don't", "hasn't", "haven't",
    "i'm", "i've", "isn't", "it's", "that's", "there's", "they're",
    "wasn't", "we're", "we've", "weren't", "what's", "wouldn't",
    "you'd", "you're", "you've",
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
            if key not in NON_PROSE_KEYS:
                parts.append(value)
        elif isinstance(value, dict):
            for k, v in value.items():
                walk(v, k)
        elif isinstance(value, list):
            for item in value:
                walk(item, key)

    walk(rec)
    return " ".join(parts)


def short_head(text: str) -> str:
    """The title of a work/locus string before its scholarly apparatus. The
    corpus writes both fields title-first, apparatus after: work as "The
    Didache (The Teaching of the Twelve Apostles); final form c. 80-120 CE
    per Niederwimmer..." and locus as "Trallians 9 (the 'truly born...truly
    raised' chain)" - or, in a source's own locus entries, a trailing
    vendored-filename parenthetical never meant as prose at all. Shared by
    engine.m4.citation_cards (the participant-facing headline; the full
    string stays in the card's sources[] untouched) and engine.m2.builders's
    compile-time retrieval index (Build-Plan.md Stage 4c) - a retrieval
    ranking scoring the untruncated string would search on exactly the
    apparatus text `_quote_label` already knows not to show a participant."""
    return (text or "").split(";")[0].split(" (")[0].strip()


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
# the split - nothing moved.
#
# DEMONSTRATION_TAG_FLOOR now has a baseline. Swept offline over all 444
# representative sentences in the 50 demonstration records, scored against
# the records each demonstration's own provenance body names:
#
#     floor   tagged   on-provenance
#      0.20    57%          79%
#      0.40    48%          85%      <- shipping
#      0.60    39%          89%
#      1.00    25%          94%
#
# It sits in a broad flat region: 0.40 -> 0.60 buys four points of
# precision and costs 39 of 214 tags, and below 0.15 the floor does
# nothing at all (_MIN_SHARED_WORDS binds first). There is no better value
# visible in the data, so it stays at 0.40 - now by measurement rather
# than by eye.
#
# The lever that IS mispriced sits next to it in the same condition, in
# engine.m2.builders: _MIN_SHARED_WORDS = 2. Tags resting on exactly two
# shared words score 67% on-provenance where every other bucket scores
# 90-94%, and reading all 24 of them shows the proxy is generous -
# scaffolding ("We are not going to pretend to you now that we did." ->
# a martyrdom story, on {going, now}), a question, and list fragments all
# get citations off two generic words. See that constant's own comment.
#
# WITHHOLD_FLOOR has NO baseline. It gates live generation, so measuring
# it costs real model calls, and it was chosen by eye.
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
