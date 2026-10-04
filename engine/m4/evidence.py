"""Evidence assembly - Live-Generation Design §3 (LIVE-GENERATION-DESIGN.md
§9.5): Stages A, B, D, E. Stage C is
grounding_net.scope_completion, imported here rather than reimplemented -
one tension-walk, owned once, same discipline as the m1/m4 grounding split.

Retrieval as focus, not transport (§3.1): the world's whole compiled prompt
is already cached, whole, in the system prefix. Nothing here ships new
content into context - it selects and scopes which of the ALREADY-compiled
records ground this turn, deterministically, with no model call.

Two things this module deliberately does NOT wait on before being correct
and testable, both named as still-open in the design's own §7 build map:

  - Stage A scores each cell's keyword corpus by deriving it live from the
    fleet's own canon_question records, rather than reading a precomputed
    compiled/indexes/canon-map.json. The design names that file as a
    compiler-side CACHE of exactly this derivation (§3.2) - caching it
    later changes nothing about what Stage A computes, only where the
    per-cell word sets come from.
  - Stage B scores gravity/force/contested_claim candidates directly off
    their own compiled record JSON (description/claim text), per the
    design's own recommendation (§3.2: "score them directly off their
    compiled record JSON rather than adding a chunk directory... not yet
    implemented"). This IS that implementation for those three types;
    term/story/doctrinal_witness stay scored the same way, off their own
    record JSON too - no chunk directory is read here at all, direct
    record scoring throughout.

A real, named simplification against §3.2's prose (not a silent gap):
Stage B's candidate pool is the cell's own compiled/coverage.json entry -
never the whole world. The design's text ("every other chunk-served
record... scored... and the top scorers join") reads as also searching
outside the cell-seeded set; that whole-world expansion is not built here.
What Stage C (scope_completion) already does is the one form of
beyond-the-seed expansion this module performs, and it is exactly the
gravity/contested_claim anti-conflation case the design cares most about
- the door-line bug's own systemic fix.
"""
import re

from engine.m1.canon import entity_cells, cell_keywords, retrieval_hint_keywords
from engine.prose import FALLBACK_EXCLUDED_KEYS as _FALLBACK_EXCLUDED_KEYS
from engine.prose import all_text, content_words, overlap_coefficient, retrieval_words
from engine.m4.grounding_net import scope_completion

__all__ = [
    "repository_records_by_id",
    "thin_topics_for",
    "match_asks_to_cells",
    "select_cell_candidates",
    "scope_completion",
    "thin_topic_riders",
    "apply_session_exclusion",
    "assemble_evidence",
    "render_evidence_block",
    "FLEET_FLOOR_LINE",
    "degradation_statement",
]

# Fork 2 (LIVE-GENERATION-DESIGN.md §9.5: in-voice honest-limit
# statement, code-appended) - same "appended by CODE, never recalled by a
# model" precedent as engine.m4.crisis_resources.ACUTE_DISTRESS_RESOURCES,
# for the one case that precedent doesn't cover: no cell matched this turn
# at all, or the matched cell carries no honest_limit record to speak
# instead. Same caveat crisis_resources.py states about its own
# text: real, honest, correct, NOT yet approved participant-facing
# line - flag again before any world that opens ships this literal text.
# Owned here (not engine.m4.turn, where it originated) because both a live
# participant turn and engine.m3's LiveModelAnswerer degrade the same way,
# off the same turn_evidence shape - one fallback, owned once.
FLEET_FLOOR_LINE = (
    "We don't have grounded material of our own for that. Ask us something else "
    "about what our own record actually holds, and we'll answer from it."
)


def repository_records_by_id(world_repository: dict) -> dict[str, dict]:
    """A LoadedWorld's compiled/repository.json, keyed by id - the shape
    every stage here and grounding_net.check_turn actually want."""
    return {r["id"]: r for r in world_repository["records"]}


def thin_topics_for(repository_records: dict[str, dict]) -> list[dict] | None:
    core = next((r for r in repository_records.values() if r.get("record_type") == "world_core"), None)
    return (core or {}).get("thin_topics")


def degradation_statement(turn_evidence: dict) -> str:
    """The matched cell's own honest_limit record - real, reviewed,
    already-compiled content, Stage B's own unconditional include (see
    _TYPE_FLOORS below) - when this turn matched one, else the fleet
    floor line above."""
    for candidate in turn_evidence.get("candidates", []):
        if candidate["record_type"] == "honest_limit":
            return candidate["head"]
    return FLEET_FLOOR_LINE

# A cell match needs at least this many shared content words with the
# query before it's named at all - one shared word ("church", "world") is
# noise, not a match; genuinely off-canon turns (small talk, a question
# the canon has no cell for) must be free to resolve to no cell rather
# than being forced onto the closest available one.
_MIN_ASK_MATCH_WORDS = 2

# ...but a query cannot be asked to share more words than it has.
# Measured on the 60-question reach benchmark: of nine
# questions returning an entirely empty ground, four shared exactly one
# word with exactly the right cell and were discarded before scoring.
# desert's "What did you do all day?" has ONE content word, `day`, and
# F5-I is "Walk me through an ordinary day among your people, from waking
# to sleeping"; hal's "What did you think of marriage?" has two, and F5-T
# is "What did marriage mean to your people - did you have weddings?".
# Requiring two shared words there requires the impossible.
#
# TWO GUARDS, both put in after the first draft of this relaxation broke
# exactly what the constant above was defending. With the floor simply
# lowered for short queries, "Do you like pizza?" reached C-P and F4-P on
# `like`, "Can you write me some code?" reached two cells on `write`, and
# "Tell me a joke." reached one on `tell` - the off-canon turns the
# original comment says must stay free to resolve to no cell.
#
#   CANON VOCABULARY FOR A TWO-WORD QUERY. There, a lone word may decide
#   a cell only if the fleet's own canon questions use it. That corpus is
#   86 hand-written questions - small, deliberate, fleet-owned. Hint
#   vocabulary is not: it is world-specific and, measured the same day,
#   carries ordinary verbs from the phrasing of the hints themselves
#   ("write", out of "what a bishop wrote to settle a dispute"). The
#   danger in a two-word query is precisely that the matched word is the
#   framing verb while the real subject - `code`, `pizza` - is unknown to
#   every cell. Stems are approximations and stay out too (`tell` reached
#   a cell by stem alone).
#
#   HINTS TOO FOR A ONE-WORD QUERY, because there the risk above cannot
#   arise: the single content word IS the subject, there is no other word
#   for it to be the framing of, and no vocabulary at all can give such a
#   query a second shared word. alx's "Who could be baptised?" is one
#   content word; no amount of hint writing could ever lift it over a
#   two-word floor. It still has to clear the same distinctiveness test.
#
#   AND THE WORD MUST DISCRIMINATE. `like` is in 7 of the 28 canon cells
#   and picks a cell by coin-toss; `day` is in 2, `marriage` 2, `dying`
#   1, `true` 1. A word in more than _SHORT_QUERY_MAX_CELLS cells tells
#   us nothing about which one is meant.
#
# This is NOT the single-distinctive-word tier this module measured out
# (see the note further down: 24% correct against the literal matcher's
# 31%). That tier let one word decide a cell for a query of ANY length,
# where a lone shared word among eight is genuinely noise. This moves
# only for one- and two-word queries, where a shared word is half or all
# of everything the participant said, and the overlap coefficient already
# scores it 0.5 or 1.0.
_SHORT_QUERY_WORDS = 3
_SHORT_QUERY_MAX_CELLS = 3

# Per-type floors (design §3.2): "at minimum, when the cell has them" - a
# guaranteed reachability budget, not a relevance cutoff, which is what
# makes offerability (spec §4.2: stories/quotes must stay reachable in
# conversation) a per-turn property instead of a compile-time hope.
# honest_limit is handled separately below (unconditional, no floor cap -
# see select_cell_candidates) because the §6.3 fallback ladder depends on
# it being present whenever the ground runs thin, not just when it scores
# well against this turn's message.
_TYPE_FLOORS = {
    "doctrinal_witness": 1,
    "term": 3,
    "story": 2,
    "quote": 2,
    "gravity": 2,
    "force": 1,
    "contested_claim": 1,
}
_COVERAGE_KEY_BY_TYPE = {
    "doctrinal_witness": "doctrinal_witness",
    "term": "terms",
    "story": "stories",
    "quote": "quotes",
    "gravity": "gravities",
    "force": "forces",
    "contested_claim": "contested_claims",
}

# Stage 4d (Build-Plan.md): tier prior. `retrieval.tier` (Artifact-1-
# Record-Schema.md: "1 core / 2 supporting / 3 ambient") is an authored
# importance signal - authored on roughly half the fleet's own records -
# that no ranking here has ever read; a record's centrality to its own
# world has had zero effect on which of two candidates wins a slot. A
# PRIOR, not an override: bounded well under overlap_coefficient's own
# smallest meaningful gap, so it can only ever reorder candidates whose
# relevance scores were already close, never promote a weak, merely-core
# match over a genuinely stronger one that happens to carry no tier or a
# lower one. Tier 3 and an unset tier both get zero - "ambient" makes no
# claim to priority, and neither does a record nobody has tiered yet.
_TIER_PRIOR = {1: 0.05, 2: 0.02}


def _tier_prior(record: dict) -> float:
    tier = (record.get("retrieval") or {}).get("tier")
    return _TIER_PRIOR.get(tier, 0.0)


# The prefer_instead redirect rule: "prefer_instead demotes, never
# excludes" (Build-Plan.md Stage 4a). Each
# note is free text - a condition ("participant asks X") plus its own
# " - retrieve <id>" redirect - authored for a human reader, not a
# machine-parseable rule, so this asks the identical word-overlap question
# every other scoring pass here already asks rather than attempting real
# NLU: does the participant's own query share content words with the
# note's condition half? A hit means a better-matching record almost
# certainly exists for what was actually asked (the note's own author
# already named it), so THIS record's relevance is halved - proportional,
# not a flat penalty, so a strongly-relevant record can still surface if
# its redirect target isn't in the same candidate pool, and a marginal
# one correctly falls away. Applied to overlap_coefficient's own share of
# the score only, never to _tier_prior - a record's tier is a property of
# the record, not of whether this one query happened to match a redirect
# note.
_PREFER_INSTEAD_DEMOTION_FACTOR = 0.5

# The note-authoring convention itself, not a real participant's own
# words - measured directly (fleet-wide, 702 real prefer_instead notes):
# over a third open with "participant"/"the participant"/"a participant",
# and "question"/"asking"/"wants"/"needs"/"asks" are close behind as the
# condition's own scaffolding verbs, none of them in engine.prose's
# global _STOPWORDS (that set is tuned against ordinary prose, not this
# note format's own meta-language). Left in, "What do you all believe
# about baptism?" would match ANY note opening "the participant asks..."
# on "asks" alone, demoting a record for a reason that has nothing to do
# with what was actually asked - scoped to this one function, not added
# to the global stopword list, since nothing else in this file scores
# against text written in this authoring convention.
_PREFER_INSTEAD_CONDITION_STOPWORDS = {"participant", "question", "asking", "asks", "wants", "needs"}


def _prefer_instead_demotes(query_words: set[str], record: dict) -> bool:
    for note in (record.get("retrieval") or {}).get("prefer_instead") or []:
        condition = note.split(" - retrieve", 1)[0]
        condition_words = content_words(condition) - _PREFER_INSTEAD_CONDITION_STOPWORDS
        if query_words & condition_words:
            return True
    return False

# Stage A2: a
# genuinely last-resort net under Stage A, not a replacement for it. Fires
# from assemble_evidence ONLY when match_asks_to_cells found no cell at
# all - never when a cell matched but session-exclusion emptied it
# afterward, and never displacing a cell match the curated system already
# found. Measured against pahc's own 128 records, "kingdom" (0), "heaven"
# (1), and "important" (1) all land comfortably under this pool cap, while
# common-everywhere words that can't meaningfully discriminate one record
# from another - "jesus" (20), "god" (28), "church" (47) - blow past it and
# correctly get nothing here, same as today. A query too generic for its
# own world's corpus is better left to the model's own judgement over the
# full cached prompt than handed an arbitrary handful of same-scoring
# records.
_FULLTEXT_FALLBACK_MAX_POOL = 6
_FULLTEXT_FALLBACK_MAX_RESULTS = 3


def _head_text(record: dict) -> str:
    """The compiled-facing text a record's evidence entry heads with -
    field-per-type, same fields build_prompt/build_chunks already treat as
    the model-facing content (engine/m2/builders.py), never the trailing
    provenance body."""
    record_type = record.get("record_type")
    if record_type == "term":
        return record.get("plain_meaning") or ""
    if record_type == "story":
        tellable = record.get("tellable_as")
        if not tellable:
            raise ValueError(f"{record.get('id')}: story has no tellable_as - "
                             f"refusing to fall back to text, which is never voiced")
        return tellable
    if record_type in ("quote",):
        # The speakable form is ALWAYS modern_rendering, never `text` - a
        # non-English or archaic original is primary evidence (the library
        # ruling that original-language sources can be primary evidence),
        # with modern_rendering as its own translation; `text` itself is
        # never voiced. gate_quote_recording (engine/m1/gates.py) requires
        # every quote record to carry modern_rendering, so this should be
        # unreachable in practice - fail loudly rather than silently speak
        # the original if that invariant is ever broken. The original stays
        # reachable to the net via all_text either way.
        rendering = record.get("modern_rendering")
        if not rendering:
            raise ValueError(f"{record.get('id')}: quote has no modern_rendering - "
                             f"refusing to fall back to text, which is never voiced")
        return rendering
    if record_type == "doctrinal_witness":
        return record.get("text") or "; ".join(record.get("positions") or [])
    if record_type == "honest_limit":
        return record.get("statement") or ""
    if record_type in ("gravity", "force"):
        return record.get("description") or ""
    if record_type == "contested_claim":
        return record.get("claim") or ""
    return all_text(record)


# Relocated to engine.prose.FALLBACK_EXCLUDED_KEYS (Build-Plan.md Stage 4c)
# so engine.m2.builders's compile-time retrieval index can share the
# identical exclusion set without engine/m2/ importing engine/m4/ (the
# dependency runs the other way everywhere else in this codebase) - see
# that module's own comment for the full rationale and the measurements
# behind each excluded key (pahc.term.ministrae's `senses.informational`,
# the 124-quote-hint regression on `retrieve_when`).


def _fallback_search_text(record: dict) -> str:
    parts = []

    def walk(value, key=None):
        if key in _FALLBACK_EXCLUDED_KEYS:
            return
        if isinstance(value, str):
            parts.append(value)
        elif isinstance(value, dict):
            for k, v in value.items():
                walk(v, k)
        elif isinstance(value, list):
            for item in value:
                walk(item, key)

    walk(record)
    return " ".join(parts)


def _fulltext_fallback_candidates(*, query_words: set[str], repository_records: dict[str, dict]) -> list[dict]:
    """Stage A2 - see the module-level comment on _FULLTEXT_FALLBACK_MAX_POOL
    for why this is safe. Deliberately literal (not stemmed) and
    deliberately not gated on _MIN_ASK_MATCH_WORDS - a single shared word is
    enough, since the whole gap this closes is that short natural questions
    ("what is heaven") reduce to one content word and can never reach that
    threshold. Searches _fallback_search_text(), not _head_text(): _head_text
    prefers a story's own `tellable_as` paraphrase, and
    pahc.story.didache-eucharist's own tellable_as never says "kingdom" even
    though its actual `text` - the Didache's own closing prayer - does. The
    narrower, curated _head_text is right for what gets shown to the model;
    this stage needs the wider net to find the record at all (see
    _FALLBACK_EXCLUDED_KEYS for the one respect in which that net is
    deliberately narrower than all_text's own, and why).

    The pool cap is applied PER QUERY WORD, not to the query as a whole -
    "what was the kingdom of God" is {"kingdom", "god"}, and "god" alone
    matches a quarter of pahc's own corpus. Capping the whole query would
    let that one common word veto "kingdom" (2 records) right along with
    itself. Instead an overly-common word is just dropped from
    consideration; the words still selective enough for this world's own
    corpus are what drive the match."""
    word_hit_counts = {
        word: sum(1 for record in repository_records.values() if word in content_words(_fallback_search_text(record))) for word in query_words
    }
    usable_words = {word for word, count in word_hit_counts.items() if 0 < count <= _FULLTEXT_FALLBACK_MAX_POOL}
    if not usable_words:
        return []

    scored = []
    for rid, record in repository_records.items():
        shared = usable_words & content_words(_fallback_search_text(record))
        if shared:
            scored.append((len(shared), rid, record))
    if not scored:
        return []

    scored.sort(key=lambda entry: (-entry[0], entry[1]))
    return [
        {
            "id": rid,
            "record_type": record.get("record_type"),
            "score": None,
            "head": _head_text(record),
            "confidence": (record.get("confidence") or {}).get("formation_confidence"),
            "classification": record.get("classification"),
            "cell": None,
            "fulltext_fallback": True,
        }
        for _count, rid, record in scored[:_FULLTEXT_FALLBACK_MAX_RESULTS]
    ]


def _query_words(message: str, asks: list[dict] | None) -> set[str]:
    text = " ".join([message or ""] + [a.get("text", "") for a in (asks or [])])
    return content_words(text)


# Crude suffix stripping, applied to BOTH sides of the comparison so it can
# only ever add a match, never move one. Deliberately not a real stemmer:
# no dictionary, no exceptions list, and a hard 4-character floor so it
# cannot turn "mass" into "mas" or collapse short words into each other.
# It exists because the measured failures were morphological, not
# semantic - "persecuted" against a corpus holding "persecution" 28 times,
# "belong" against a hint reading "belonging".
_SUFFIXES = ("ations", "ation", "ings", "ing", "ions", "ion", "edly", "ed")
# "es" is only a plural after a sibilant - watches, boxes, churches. Strip it
# blindly and "disputes" becomes "disput" while "dispute" stays whole, so the
# pair never converges and the stemmer defeats its own purpose.
_SIBILANTS = ("s", "x", "z", "ch", "sh")


def _stem(word: str) -> str:
    for suf in _SUFFIXES:
        if word.endswith(suf) and len(word) - len(suf) >= 4:
            return word[: -len(suf)]
    if word.endswith("es") and len(word) >= 6 and word[:-2].endswith(_SIBILANTS):
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss") and len(word) >= 5:
        return word[:-1]
    return word


def _stems(words: set[str]) -> set[str]:
    return {_stem(w) for w in words}


# THE CELL SCORER'S WEIGHTING. Stage A used to score a cell as
# len(shared) / min(len(query), len(cell_vocabulary)) - an overlap
# coefficient in which every shared word counts the same. Measured: that is
# what let a broad cell beat the right one:
# "Does God ever feel like anything, or is it only believed?" went to F6-P
# (the hard places) on `ever`, `god`, `like`, and nothing living in F1-P
# could be reached afterwards, because only the top-scoring cells survive
# to Stage B at all. A hint cannot fix that and neither can a canon
# question: the cell is chosen before any record is scored.
#
# THE DEFECT IS A SHORT TAIL, NOT THE VOCABULARY. Of 298 distinct canon
# words, 227 (76%) occur in exactly ONE cell and 284 (95%) in three or
# fewer - those are near-perfect evidence and are left alone. Twelve words
# occur in five cells or more: `people` in 17, `believe` in 9,
# `someone`/`happened`/`among` in 8, `know`/`like` in 7, `community` in 6,
# `jesus`/`church`/`anything`/`god` in 5. Counting those equally with a
# word that names one cell outright is the whole of the bug.
#
# So the weighting is deliberately surgical rather than a textbook idf:
# every word keeps weight 1.0 up to _COMMON_CELL_DF cells, and only past
# that does it taper, as _COMMON_CELL_DF / df, floored at _COMMON_WORD_FLOOR
# so a common word is discounted and never silenced. `people` lands at the
# floor, `believe` at 0.44, `like` at 0.57, `god` at 0.8.
#
# CHOSEN BY MEASUREMENT, against a textbook alternative. Six weightings
# were run over three instruments - leave-one-out across all 93 canon
# questions, the locked sixty-question benchmark, and the probe that
# motivated the change. Full idf (log(N/df) on every word) fixed the probe
# but cost one ground record, one quote and one family-level match. This
# taper fixes the same probe with NO measured cost on either instrument:
# 466 ground / 67 cells / 0 empty / 79 quotes and leave-one-out family
# accuracy 17/93, both identical to the flat scorer it replaces.
#
# A query word in NO cell vocabulary keeps weight 1.0. It can never be
# shared, so it only enlarges the denominator - the behaviour that keeps
# "Do you like pizza?" at no cell, and that a zero weight would quietly
# delete.
_COMMON_CELL_DF = 4       # a word in this many cells or fewer is still evidence
_COMMON_WORD_FLOOR = 0.25  # a word in every cell still counts for something


def _word_weights(query_words: set[str], cell_count: dict[str, int]) -> dict[str, float]:
    """Per-word evidence weight for cell scoring - see the block above for
    why the taper starts where it does and why it has a floor."""
    weights = {}
    for word in query_words:
        spread = cell_count.get(word, 0)
        weights[word] = (
            1.0 if spread <= _COMMON_CELL_DF
            else max(_COMMON_WORD_FLOOR, _COMMON_CELL_DF / spread)
        )
    return weights


def match_asks_to_cells(
    *, message: str, asks: list[dict] | None, canon_questions: dict[str, dict], repository_records: dict[str, dict] | None = None, top_n: int = 2
) -> list[dict]:
    """Stage A (design §3.2): asks -> canon cells. canon_questions is the
    fleet's own canon_question records (engine/canon/records/canon_question/),
    id -> record - the per-cell keyword corpus is derived live from their
    `text` fields (see module docstring on the canon-map.json cache this
    stands in for). Returns up to top_n {"cell", "score", "shared_words"}
    entries, score = overlap coefficient, sorted desc; empty list means
    "no cell" (design §3.2: general conversation, evidence block still
    built from Stage B alone against whatever the caller passes).

    repository_records is this world's own records, and contributes the
    second half of the corpus: engine.m1.canon.retrieval_hint_keywords
    credits each record's `retrieval.retrieve_when` text to the cells that
    record serves. Without it, a cell is only reachable through the 28
    fleet canon questions' vocabulary, so a question could miss ground
    whose own record named the very word the question used - measured on a
    live run, "What was it like when the plague came?" reached no cell at
    all while alx.story.plague-nursing sat in F6-P declaring
    retrieve_when: "sickness, death, plague, care for the dying". Passing
    None keeps the fleet-only behaviour, which is what a caller with no
    world in hand (the compile-time cache, the fleet's own tests) wants.

    Hints only ever FILL REMAINING SLOTS: the canon-vocabulary ranking is
    computed first and taken whole, and hint-found cells are appended
    after it, never interleaved. Scoring the two corpora together was the
    obvious shape and it is the wrong one - a widened cell outscores a
    cell the fleet vocabulary matched honestly, and on the 28 canon
    questions used as their own probe that displaced a top-2 cell on 11 of
    86 asks in one world. This way a turn that already had a canon match
    is bit-for-bit unchanged, and the only turns that move are the ones
    that were reaching nothing."""
    query_words = _query_words(message, asks)
    if not query_words:
        return []

    def _rank(cell_words: dict[str, set[str]], *, allow_single: bool = False) -> list[dict]:
        single_ok = allow_single and len(query_words) < _SHORT_QUERY_WORDS
        cell_count = {w: sum(1 for ws in cell_words.values() if w in ws) for w in query_words}
        discriminating = (
            {w for w in query_words if 0 < cell_count[w] <= _SHORT_QUERY_MAX_CELLS}
            if single_ok else set()
        )
        weight = _word_weights(query_words, cell_count)
        query_mass = sum(weight[w] for w in query_words)
        scored = []
        for cell, words in cell_words.items():
            shared = query_words & words
            if len(shared) < _MIN_ASK_MATCH_WORDS and not (single_ok and shared and shared <= discriminating):
                continue
            shared_mass = sum(weight[w] for w in shared)
            cell_mass = sum(weight.get(w, 1.0) for w in words)
            score = shared_mass / min(query_mass, cell_mass) if min(query_mass, cell_mass) else 0.0
            scored.append({"cell": cell, "score": round(score, 3), "shared_words": sorted(shared)})
        scored.sort(key=lambda e: (-e["score"], e["cell"]))
        return scored

    def _fill(matches, vocab, *, allow_single=False, **mark):
        """Append cells this vocabulary finds, never displacing what is
        already matched - the same discipline the retrieval hints follow."""
        already = {m["cell"] for m in matches}
        for match in _rank(vocab, allow_single=allow_single):
            if len(matches) >= top_n:
                break
            if match["cell"] not in already:
                matches.append({**match, **mark})
        return matches

    canon_words = cell_keywords(canon_questions)
    matches = _rank(canon_words)
    if len(matches) >= top_n:
        return _add_entity_cell(matches[:top_n], query_words, repository_records, canon_words)

    # Hints widen cells the fleet already defines; they never invent a
    # cell, so a stale canon_cells value on a record can't create one.
    hinted = {
        cell: canon_words.get(cell, set()) | words
        for cell, words in retrieval_hint_keywords(repository_records or {}).items()
        if cell in canon_words
    }
    if hinted:
        matches = _fill(matches, hinted, from_retrieval_hint=True)
        if len(matches) >= top_n:
            return _add_entity_cell(matches[:top_n], query_words, repository_records, canon_words)

    # Everything above compares words literally. This tier runs only when
    # that left slots unfilled, so an honest literal match is never
    # displaced by a stemmed one.
    #
    # A single-distinctive-word tier was built here and measured out. On
    # leave-one-question-out over the canon it picked the right cell 24% of
    # the time against the literal matcher's own 31% - it made questions
    # reach ground, usually the wrong ground, so it is not here.
    full = {cell: canon_words.get(cell, set()) | hinted.get(cell, set()) for cell in canon_words}
    stemmed = {cell: _stems(words) for cell, words in full.items()}
    stem_query = _stems(query_words)
    saved_query, query_words = query_words, stem_query
    matches = _fill(matches, stemmed, matched_by="stem")
    query_words = saved_query

    # LAST, and only into slots nothing else filled. Ordering is the whole
    # safety of this tier: run earlier, a 0.5 single-word canon match takes
    # a slot ahead of a 1.0 two-word hint match, and measured on ijc that
    # displaced F1-E ("I've heard a council basically voted Jesus into
    # being God") from "What happened at the councils?" in favour of a
    # weaker cell. Here a turn that already reached cells is bit-for-bit
    # unchanged and only turns reaching nothing can move - the same
    # discipline the retrieval-hint tier above follows.
    if len(matches) < top_n:
        matches = _fill(matches, canon_words, allow_single=True, matched_by="single-word")
    # A one-word query gets the hinted vocabulary too - see the note above
    # on why the framing-verb risk cannot arise when the word is the whole
    # question. Still last, still filling only what nothing else filled.
    if len(matches) < top_n and len(query_words) == 1 and hinted:
        matches = _fill(matches, hinted, allow_single=True, matched_by="single-word-hint")

    return _add_entity_cell(matches[:top_n], query_words, repository_records, canon_words)


# Entity routing (added on a measured failure - see
# engine.m1.canon.entity_cells for the failing turn). Every tier above
# compares content words and weighs a proper noun no more heavily than any
# other word, so naming a figure did nothing.
#
# IT ADDS A SLOT RATHER THAN COMPETING FOR ONE, and that is the whole
# safety argument. The alternative - letting an entity hit displace the
# weakest canon match - needed a tuned threshold on how weak is weak
# enough, and a wrong threshold silently drops an honest literal match.
# This cannot: every cell the tiers above found survives untouched, and
# the only effect of naming a figure is that one further cell's ground
# rides along. That costs tokens in an uncached per-turn block. It cannot
# cost correctness, because the ground has never been a whitelist - the
# grounding net checks each sentence against the whole repository, so a
# wider ground widens what is OFFERED and changes nothing about what may
# be said.
_ENTITY_EXTRA_CELLS = 1


def _add_entity_cell(matches, query_words, repository_records, canon_words):
    if not repository_records:
        return matches
    routes = entity_cells(repository_records, canon_vocabulary=set().union(*canon_words.values()) if canon_words else None)
    if not routes:
        return matches
    already = {m["cell"] for m in matches}
    added = 0
    for name in sorted(query_words & set(routes)):
        for cell in routes[name]:
            if added >= _ENTITY_EXTRA_CELLS:
                return matches
            if cell in already or cell not in canon_words:
                continue
            already.add(cell)
            added += 1
            matches.append({"cell": cell, "score": None, "shared_words": [name], "from_entity": name})
    return matches


def _source_key(record: dict) -> str:
    """The source family a record's material comes from - the first
    registered source_id, else the quote's own speaker/author, else the
    record's own id (so a sourceless record is its own family and can
    never crowd anything out)."""
    for entry in record.get("sources") or []:
        if entry.get("source_id"):
            return entry["source_id"]
    raw = (record.get("speaker_or_author") or "").strip()
    return raw or record.get("id", "")


def _diverse_take(
    scored: list[tuple[str, float]],
    repository_records: dict[str, dict],
    floor: int,
    session_used_keys: set[str] | None = None,
) -> list[tuple[str, float]]:
    """Breadth-first by source family, best-first within: drawing from
    other sources is meant to be a system function, not something forced
    for one question. The measured failure
    this replaces: a divinity question's quote slots both filled from
    Ignatius because his material out-scores everything, while Pliny's
    and Justin's witness sat in the same cell unseen - the voice can only
    draw breadth it is shown. Same slot count, same floors, same
    guaranteed-reachability semantics as scored[:floor]; only the
    COMPOSITION changes, and only when the cell actually holds more than
    one source family.

    `session_used_keys` follows the same principle: the priority of a
    reference source is downgraded once it has already been used - not
    banned, but the system looks to others first. Source families this
    voice has already drawn on THIS
    SESSION are considered last, never excluded. Deterministic passes, in
    order: (1) best of each family that is new both this turn and this
    session; (2) best of each family new this turn (session-used families
    return here); (3) fill remaining slots by pure score order."""
    used = session_used_keys or set()
    take: list[tuple[str, float]] = []
    covered: set[str] = set()

    def _key(rid: str) -> str:
        return _source_key(repository_records.get(rid) or {"id": rid})

    for pass_ok in (
        lambda k: k not in covered and k not in used,
        lambda k: k not in covered,
        lambda k: True,
    ):
        for rid, score in scored:
            if len(take) >= floor:
                return take
            if any(rid == r for r, _ in take):
                continue
            key = _key(rid)
            if pass_ok(key):
                covered.add(key)
                take.append((rid, score))
    return take


# Stage B2 (Build-Plan.md Stage 4c, part 2). Stage B's own candidate pool
# is deliberately the matched cell's own compiled/coverage.json entry, per
# the module docstring's named simplification - and most of the time that
# is exactly right: a cell match is curated evidence about what belongs to
# THIS cell, and letting a query wander the whole world would reintroduce
# the door-line style conflation Stage C already exists to police. But a
# coverage entry can have LITERALLY ZERO records of some type - not a low
# score, a structural absence - and Stage B then has nothing to rank at
# all for that slot, silently, even on a world whose repository holds
# records of that type elsewhere that the query's own words would
# recognize. This fires ONLY there: never for a type the coverage entry
# already has something for (that is a relevance question Stage B's own
# ranking already answers), and never for honest_limit (unconditional,
# fed to the §6.3 fallback ladder by its own separate, cell-scoped
# mechanism above - see _TYPE_FLOORS comment on why that type is never
# ranked away or filled generically).
#
# Scored against engine.prose.retrieval_words, not all_text() - the same
# narrower, participant-facing, id/apparatus-safe word set
# compiled/retrieval.json caches at build time, and for the identical
# reason Stage A2's own fulltext fallback (see _fallback_search_text)
# needs a narrower net than Stage B's own cell-curated ranking does: an
# uncurated, whole-world scan is exactly the case a stray build-commentary
# word or a dotted id fragment could surface the wrong record for, with no
# curated coverage entry standing between the query and every record in
# the world.
def _retrieval_fill_scores(*, record_type: str, query_words: set[str], repository_records: dict[str, dict]) -> list[tuple[str, float]]:
    if not query_words:
        return []
    scored = []
    for rid, record in repository_records.items():
        if record.get("record_type") != record_type:
            continue
        words = set(retrieval_words(record))
        if not words:
            continue
        shared = query_words & words
        if not shared:
            continue
        base = len(shared) / min(len(query_words), len(words))
        if _prefer_instead_demotes(query_words, record):
            base *= _PREFER_INSTEAD_DEMOTION_FACTOR
        scored.append((rid, base + _tier_prior(record)))
    scored.sort(key=lambda t: (-t[1], t[0]))
    return scored


def select_cell_candidates(*, cell: str, coverage_entry: dict, repository_records: dict[str, dict], message: str, asks: list[dict] | None, budget_chars: int = 9000, already_told_ids: set[str] | list[str] | None = None) -> list[dict]:
    """Stage B (design §3.2): cell -> candidates -> rank. coverage_entry is
    compiled/coverage.json's own entry for this cell - the seed pool every
    candidate here is drawn from (see module docstring's named
    simplification against the design's whole-world expansion prose).
    Returns an ordered list of {"id", "record_type", "score", "head",
    "confidence", "classification"} dicts; score is None for honest_limit
    (unconditional, never ranked away - see _TYPE_FLOORS comment), else the
    relevance score plus this record's own tier prior (see _tier_prior;
    Stage 4d). An entry also carries "retrieval_fill": True when the
    coverage entry had no candidates of that type at all and Stage B2
    filled the slot instead (see the comment on _retrieval_fill_scores) -
    absent, not False, on every ordinary coverage-seeded entry. An entry
    also carries "claim_guards": [...] when the record has any - the
    prefer_instead redirect rule's guard half, rendered as a rider on this
    exact candidate's own line by render_evidence_block, not a separate section
    - absent, not an empty list, on every record with none."""
    query_words = _query_words(message, asks)
    selected: list[dict] = []
    used_chars = 0

    def _entry(rid: str, record_type: str, score: float | None) -> dict | None:
        record = repository_records.get(rid)
        if record is None:
            return None
        head = _head_text(record)
        entry = {
            "id": rid,
            "record_type": record_type,
            "score": round(score, 3) if score is not None else None,
            "head": head,
            "confidence": (record.get("confidence") or {}).get("formation_confidence"),
            "classification": record.get("classification"),
        }
        guards = record.get("claim_guards")
        if guards:
            entry["claim_guards"] = guards
        return entry

    def _entry_chars(entry: dict) -> int:
        # The rider rides inside the same budget it's counted against -
        # Build-Plan.md Stage 4a's own "riders in render_evidence_block
        # inside existing budget_chars" - never a separate allowance.
        return len(entry["head"]) + sum(len(g) for g in entry.get("claim_guards") or [])

    for rid in coverage_entry.get("honest_limit") or []:
        entry = _entry(rid, "honest_limit", None)
        if entry is None:
            continue
        selected.append(entry)
        used_chars += _entry_chars(entry)

    for record_type, floor in _TYPE_FLOORS.items():
        cov_key = _COVERAGE_KEY_BY_TYPE[record_type]
        cov_ids = coverage_entry.get(cov_key) or []
        retrieval_fill = not cov_ids
        if retrieval_fill:
            scored = _retrieval_fill_scores(record_type=record_type, query_words=query_words, repository_records=repository_records)
        else:
            scored = []
            for rid in cov_ids:
                record = repository_records.get(rid)
                if record is None:
                    continue
                base = overlap_coefficient(query_words, record)
                if _prefer_instead_demotes(query_words, record):
                    base *= _PREFER_INSTEAD_DEMOTION_FACTOR
                scored.append((rid, base + _tier_prior(record)))
            scored.sort(key=lambda t: (-t[1], t[0]))
        used_keys = {
            _source_key(repository_records[rid])
            for rid in (already_told_ids or ())
            if rid in repository_records
        }
        for rid, score in _diverse_take(scored, repository_records, floor, used_keys):
            if used_chars >= budget_chars:
                break
            entry = _entry(rid, record_type, score)
            if entry is None:
                continue
            if retrieval_fill:
                entry["retrieval_fill"] = True
            selected.append(entry)
            used_chars += _entry_chars(entry)

    return selected


def thin_topic_riders(*, message: str, asks: list[dict] | None, selected: list[dict], thin_topics: list[dict] | None) -> list[dict]:
    """Stage D (design §3.2): a thin-topic rides along as a 'what we
    cannot claim' line whenever the ask/message, or a selected candidate's
    own head text, hits one of world_core.thin_topics's keywords. Returns
    the matching topic dicts themselves (deduplicated by note), not a
    per-sentence formatted string - this runs once per turn over the
    whole evidence set, unlike grounding_net's own per-sentence severity
    escalator, which is a different call site for the same field."""
    if not thin_topics:
        return []
    haystacks = [message or ""] + [a.get("text", "") for a in (asks or [])] + [c["head"] for c in selected]
    lower_haystacks = [h.lower() for h in haystacks if h]

    riders = []
    seen_notes = set()
    for topic in thin_topics:
        keywords = topic.get("keywords") or []
        if any(kw.lower() in haystack for kw in keywords for haystack in lower_haystacks):
            note = topic.get("note")
            if note not in seen_notes:
                seen_notes.add(note)
                riders.append(topic)
    return riders


def apply_session_exclusion(*, selected: list[dict], already_told_ids: set[str] | list[str] | None) -> list[dict]:
    """Stage E (design §3.2): story/quote ids already told this session are
    annotated, never dropped - the continuity rule (spec §5.5) is about
    repetition, and a follow-up about an already-told story needs the
    model to still see it, just marked as already offered."""
    if not already_told_ids:
        return selected
    told = set(already_told_ids)
    out = []
    for candidate in selected:
        if candidate["record_type"] in ("story", "quote") and candidate["id"] in told:
            candidate = {**candidate, "already_told_this_session": True}
        out.append(candidate)
    return out


# RETRIEVAL HAS NO MEMORY OF ITS OWN, AND THE MODEL DOES. Found by a live
# turn, not by inspection. Asked "You've given me two
# different pictures there. Did your own people disagree about this?", the
# voice answered at length, and well, about whether women could be elders -
# a question nobody had asked. The conversation was in the prompt and
# plainly understood; only the GROUND was blind to it, assembled from the
# follow-up's own words, and the voice answered from what it was handed.
#
# Strip the pronouns from that question and what is left is `different`,
# `disagree`, `pictures`, `two`. The subject is `this`. Measured across a
# set of ordinary follow-ups, every one routed on noise: "Why did that
# matter?" scored 1.0 on `matter`, "Who said it?" scored 1.0 on `said`,
# "Was that common?" and "What happened to him after that?" reached nothing
# at all. No hint and no canon question can help - the query has no subject
# in it.
#
# DETECTING ONE. The presence of a back-reference is not enough on its own:
# 33 of the 93 canon questions contain `that`, `this` or `it`, and in every
# one of them the question still NAMES ITS SUBJECT ("How did your people
# fast, and what was it for?"). What separates a follow-up is that it
# carries a back-reference AND almost no evidence of its own. The second
# half is measurable with the weighting the cell scorer already computes:
# the best cell's shared mass. Across the 93 canon questions that mass has
# a median of 4.17 and a minimum of 1.00; across ordinary follow-ups it is
# 0.00 to 1.25.
#
# So: a back-reference marker, AND best-cell shared mass below
# _FOLLOW_UP_MASS. Measured on three sets - it catches 9 of 11 ordinary
# follow-ups (the two it misses, "Tell me more." and "Did they all think
# so?", carry no marker), and misfires on 1 of 93 canon questions and 2 of
# the 60 benchmark questions. Both benchmark misfires currently reach NO
# cell at all, so inheriting is a gain there rather than a cost.
#
# WHAT HAPPENS THEN. The prior turn's cells lead and the message's own fill
# the remaining slots - a follow-up is ABOUT the previous subject, so the
# previous subject's ground should not be competing for second place with a
# cell matched on `said`. Two properties keep this safe: a first turn has
# no prior cells and is unchanged, and a message that is not a follow-up
# never consults history at all, so every non-referential turn is
# bit-for-bit what it was.
#
# Chains resolve to the last SELF-STANDING question, not the last message,
# so "Say more about that." followed by "And then?" both inherit from the
# real question that opened the thread rather than from each other.
_BACK_REFERENCE = {"that", "this", "those", "these", "it", "there", "then"}
_FOLLOW_UP_MASS = 1.30


def _looks_like_follow_up(message: str, asks, canon_questions, repository_records) -> bool:
    """A back-reference with no subject of its own - see the block above for
    the measurement behind both halves of the test."""
    words = _query_words(message, asks)
    if not words or not (_BACK_REFERENCE & set(re.findall(r"[a-z']+", (message or "").lower()))):
        return False
    matches = match_asks_to_cells(
        message=message, asks=asks, canon_questions=canon_questions,
        repository_records=repository_records, top_n=1,
    )
    if not matches:
        return True
    cell_words = cell_keywords(canon_questions)
    counts = {w: sum(1 for ws in cell_words.values() if w in ws) for w in words}
    weights = _word_weights(words, counts)
    return sum(weights.get(w, 1.0) for w in matches[0]["shared_words"]) < _FOLLOW_UP_MASS


def inherited_cells(history, *, canon_questions, repository_records, top_n) -> list[dict]:
    """The cells of the most recent participant message that stood on its
    own. history is the Messages-API shape engine.api.wiring builds."""
    for entry in reversed(history or []):
        if entry.get("role") != "user":
            continue
        text = entry.get("content") or ""
        if _looks_like_follow_up(text, None, canon_questions, repository_records):
            continue
        return [
            {**m, "inherited_from_prior_turn": True}
            for m in match_asks_to_cells(
                message=text, asks=None, canon_questions=canon_questions,
                repository_records=repository_records, top_n=top_n,
            )
        ]
    return []


def assemble_evidence(
    *,
    message: str,
    asks: list[dict] | None,
    canon_questions: dict[str, dict],
    coverage: dict[str, dict],
    repository_records: dict[str, dict],
    thin_topics: list[dict] | None = None,
    already_told_ids: set[str] | list[str] | None = None,
    top_n_cells: int = 2,
    history: list[dict] | None = None,
    figures_already_named: list[str] | None = None,
    secondary_context: str | None = None,
) -> dict:
    """The full pipeline, Stages A -> E, deterministic, no model call.
    Returns {"cells": [...Stage A...], "candidates": [...B+C+E...],
    "thin_ground": [...D...], "figures_already_named": [...]} - the
    structured form; render_evidence_block turns this into the §3.3 prose
    block. Kept separate so callers that need the structure (tests, future
    SSE per-sentence citation anchors) never have to re-parse rendered
    text.

    figures_already_named: display names (not record ids) of figures this
    session's own prior turns already introduced - resolved by the caller
    from the same already_bridged_figure_ids set the UI's first-occurrence
    mark grammar already threads (engine.m4.turn.run_turn's docstring on
    that param). A pilot read found both Chloe turns opened
    "One of us, Ignatius" - the session knew he was introduced, but that
    knowledge only ever suppressed the second underline; the voice itself
    was never told, and its own record text carries the introduction
    formula, so it reintroduced him. Same design as Stage E's
    already-told annotation: session state made visible, the voice finds
    its own words - never a forced saying.

    secondary_context (Stage 4f, Build-Plan.md): plain text conversational
    context this turn stands inside, distinct from the participant's own
    message - at the Table, what other seated voices just said (the same
    text table_wiring._context_prefix shows the model, unwrapped). None on
    every interview call, and every other caller. Fills only the top_n_cells
    slots the participant's own message (and, on a follow-up, the inherited
    prior subject) left EMPTY - never displaces either, the identical "fills
    only remaining slots" discipline retrieval_hint_keywords already uses
    one level down for a record's own hints. Scoped to THIS call's own
    repository_records like everything else here; nothing about isolation
    changes - a caller only ever passes its own world's context."""
    cell_matches = match_asks_to_cells(
        message=message, asks=asks, canon_questions=canon_questions, repository_records=repository_records, top_n=top_n_cells
    )
    # A follow-up is ABOUT the previous subject. See _looks_like_follow_up.
    if history and _looks_like_follow_up(message, asks, canon_questions, repository_records):
        carried = inherited_cells(
            history, canon_questions=canon_questions,
            repository_records=repository_records, top_n=top_n_cells,
        )
        if carried:
            own = [m for m in cell_matches if m["cell"] not in {c["cell"] for c in carried}]
            cell_matches = (carried + own)[:top_n_cells]

    if secondary_context and len(cell_matches) < top_n_cells:
        seen_cells = {m["cell"] for m in cell_matches}
        for m in match_asks_to_cells(
            message=secondary_context, asks=None, canon_questions=canon_questions,
            repository_records=repository_records, top_n=top_n_cells,
        ):
            if len(cell_matches) >= top_n_cells:
                break
            if m["cell"] in seen_cells:
                continue
            cell_matches.append({**m, "from_secondary_context": True})
            seen_cells.add(m["cell"])

    selected: list[dict] = []
    seen_ids: set[str] = set()
    for match in cell_matches:
        coverage_entry = coverage.get(match["cell"]) or {}
        for candidate in select_cell_candidates(
            cell=match["cell"], coverage_entry=coverage_entry, repository_records=repository_records, message=message, asks=asks,
            already_told_ids=already_told_ids,
        ):
            if candidate["id"] in seen_ids:
                continue
            seen_ids.add(candidate["id"])
            selected.append({**candidate, "cell": match["cell"]})

    # Stage A2: only when Stage A found no cell on its own EVIDENCE - never
    # when a cell matched but session-exclusion is what emptied `selected`
    # (that is an intentional "already told this" outcome, not a retrieval
    # failure).
    #
    # An entity-only match does not count as Stage A finding a cell, and
    # that clause is a regression fix rather than a refinement: measured on
    # pahc, "Who was Papias?" reached no cell before entity routing and got
    # three records from this fallback, then reached C-E through the entity
    # tier and got one, because a cell match suppressed the fallback that
    # had been carrying it. Entity routing is a weaker signal than a canon
    # or hint match by construction - it knows the question is ABOUT
    # someone, not what is being asked - so it widens the ground without
    # claiming the fallback is no longer needed.
    if not [m for m in cell_matches if not m.get("from_entity")]:
        for candidate in _fulltext_fallback_candidates(query_words=_query_words(message, asks), repository_records=repository_records):
            if candidate["id"] in seen_ids:
                continue
            seen_ids.add(candidate["id"])
            selected.append(candidate)

    # Stage C: never serve one pole of a recorded tension without the
    # record that names the tension (the door-line bug's systemic fix).
    for rid in scope_completion([c["id"] for c in selected], repository_records):
        if rid in seen_ids:
            continue
        record = repository_records.get(rid)
        if record is None:
            continue
        seen_ids.add(rid)
        selected.append(
            {
                "id": rid,
                "record_type": record.get("record_type"),
                "score": None,
                "head": _head_text(record),
                "confidence": (record.get("confidence") or {}).get("formation_confidence"),
                "classification": record.get("classification"),
                "cell": None,
                "scope_completion": True,
            }
        )

    selected = apply_session_exclusion(selected=selected, already_told_ids=already_told_ids)
    thin_ground = thin_topic_riders(message=message, asks=asks, selected=selected, thin_topics=thin_topics)

    return {
        "cells": cell_matches,
        "candidates": selected,
        "thin_ground": thin_ground,
        "figures_already_named": list(figures_already_named or []),
    }


def render_evidence_block(evidence: dict) -> str:
    """The §3.3 text block itself, ready to ride in the per-turn user
    message (never the cached system prefix). Ids are the exact strings
    the citation-tag grammar (§4.1, [[<record.id>]]) uses - this block and
    the model's own tags share one id vocabulary by construction.

    AVAILABLE IS NOT THE SAME AS ALREADY SAID, and previously only
    one of the two channels said which it was. A six-turn live run on
    desert answered a question about women by opening "Sarah, whose words
    we already gave you" - and the two turns before it were about Jesus.
    Sarah's saying was in THIS block, read for the first time, and the next
    turn compounded it: "whose one saying we already gave you".

    The two channels look alike by construction. engine.api.wiring's
    _replay_text deliberately re-attaches surviving [[id]] tags to every
    past turn it replays (without them, session memory taught the voice to
    stop citing - that docstring has the measurement), so a claim already
    spoken and a record merely offered arrive in the same grammar. This
    block was the only one of the two carrying a header, and its header
    said what may be cited, never what has been said. So the model had a
    frame for one channel and none for the other, and blurred them.

    The clause below is the frame the other channel implies but cannot
    state, put here rather than in the replayed turns on purpose:
    _replay_text keeps a past turn exactly as the participant read it,
    withheld sentences included, so that the voice's memory cannot
    disagree with the person's. Scaffolding injected into an assistant
    turn breaks that, and risks the voice emitting the scaffolding.

    Per-record marking already exists and does not cover this: Stage E
    annotates `already told this session`, but only for story/quote
    (deliberately - the continuity rule is about not re-telling a story,
    while re-using a witness is ordinary). Sarah's quote was NOT told
    before, so it correctly carried no marker, and the voice still claimed
    it had been. What was missing was never the marker; it was that an
    ABSENT marker meant nothing until this said so."""
    lines = [
        "## Ground for this turn (cite only these; anything beyond them is spoken",
        "## as our honest limit, never asserted)",
        "## Available, not already said: what we have said is only what stands in",
        "## the conversation above. Never tell a participant we already gave them",
        "## something first read here.",
    ]
    named = evidence.get("figures_already_named") or []
    if named:
        lines += [
            f"## Already introduced: {', '.join(named)}. The participant met these names in",
            "## an earlier answer. Ground text that presents them afresh is written",
            "## for a first mention; this turn is not one - carry them as someone",
            "## already known (the shape of 'Ignatius also said...'), never",
            "## re-introduced as if new.",
        ]
    for candidate in evidence["candidates"]:
        head = (candidate["head"] or "").strip().split(". ")[0].rstrip(".")
        descriptors = [candidate["record_type"]]
        if candidate.get("classification"):
            descriptors.append(str(candidate["classification"]).upper())
        if candidate.get("confidence"):
            descriptors.append(candidate["confidence"])
        if candidate.get("scope_completion"):
            descriptors.append("scope completion")
        if candidate.get("already_told_this_session"):
            descriptors.append("already told this session")
        line = f"- [[{candidate['id']}]] {', '.join(descriptors)} — {head}"
        guards = candidate.get("claim_guards")
        if guards:
            # The prefer_instead redirect rule's guard half, rendered as a
            # rider on this exact
            # candidate's own line (Adjusted-Design.md: "Guards render as
            # a rider on the candidate line inside the existing evidence
            # budget - upstream prevention, the mechanism that actually
            # works") - directly beside the one record it barred a claim
            # about, never a separate section a skim could miss.
            line += " | MUST NOT ASSERT: " + "; ".join(guards)
        lines.append(line)
    for topic in evidence["thin_ground"]:
        keywords = ", ".join(topic.get("keywords") or [])
        lines.append(f"- THIN GROUND (do not claim past it): {keywords} — {topic.get('note')}")
    return "\n".join(lines) + "\n"
