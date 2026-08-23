"""Evidence assembly - Live-Generation Design §3 (LIVE-GENERATION-DESIGN.md,
forks signed off §9.5, 2026-08-22): Stages A, B, D, E. Stage C is
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
from engine.m1.canon import cell_keywords
from engine.m1.gates_experimental import _all_text, _content_words, _overlap_coefficient
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

# Fork 2 (LIVE-GENERATION-DESIGN.md §9.5: RULED, in-voice honest-limit
# statement, code-appended) - same "appended by CODE, never recalled by a
# model" precedent as engine.m4.crisis_resources.ACUTE_DISTRESS_RESOURCES,
# for the one case that precedent doesn't cover: no cell matched this turn
# at all, or the matched cell carries no honest_limit record to speak
# instead. Same craft-pass caveat crisis_resources.py states about its own
# text: real, honest, correct, NOT yet a Mark-approved participant-facing
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


def _head_text(record: dict) -> str:
    """The compiled-facing text a record's evidence entry heads with -
    field-per-type, same fields build_prompt/build_chunks already treat as
    the model-facing content (engine/m2/builders.py), never the trailing
    provenance body."""
    record_type = record.get("record_type")
    if record_type == "term":
        return record.get("plain_meaning") or ""
    if record_type == "story":
        return record.get("tellable_as") or record.get("text") or ""
    if record_type in ("quote",):
        return record.get("text") or ""
    if record_type == "doctrinal_witness":
        return record.get("text") or "; ".join(record.get("positions") or [])
    if record_type == "honest_limit":
        return record.get("statement") or ""
    if record_type in ("gravity", "force"):
        return record.get("description") or ""
    if record_type == "contested_claim":
        return record.get("claim") or ""
    return _all_text(record)




def _query_words(message: str, asks: list[dict] | None) -> set[str]:
    text = " ".join([message or ""] + [a.get("text", "") for a in (asks or [])])
    return _content_words(text)


def match_asks_to_cells(*, message: str, asks: list[dict] | None, canon_questions: dict[str, dict], top_n: int = 2) -> list[dict]:
    """Stage A (design §3.2): asks -> canon cells. canon_questions is the
    fleet's own canon_question records (records/_fleet/canon_question/),
    id -> record - the per-cell keyword corpus is derived live from their
    `text` fields (see module docstring on the canon-map.json cache this
    stands in for). Returns up to top_n {"cell", "score", "shared_words"}
    entries, score = overlap coefficient, sorted desc; empty list means
    "no cell" (design §3.2: general conversation, evidence block still
    built from Stage B alone against whatever the caller passes)."""
    query_words = _query_words(message, asks)
    if not query_words:
        return []

    cell_words = cell_keywords(canon_questions)

    scored = []
    for cell, words in cell_words.items():
        shared = query_words & words
        if len(shared) < _MIN_ASK_MATCH_WORDS:
            continue
        score = len(shared) / min(len(query_words), len(words))
        scored.append({"cell": cell, "score": round(score, 3), "shared_words": sorted(shared)})
    scored.sort(key=lambda e: (-e["score"], e["cell"]))
    return scored[:top_n]


def select_cell_candidates(*, cell: str, coverage_entry: dict, repository_records: dict[str, dict], message: str, asks: list[dict] | None, budget_chars: int = 9000) -> list[dict]:
    """Stage B (design §3.2): cell -> candidates -> rank. coverage_entry is
    compiled/coverage.json's own entry for this cell - the seed pool every
    candidate here is drawn from (see module docstring's named
    simplification against the design's whole-world expansion prose).
    Returns an ordered list of {"id", "record_type", "score", "head",
    "confidence", "classification"} dicts; score is None for honest_limit
    (unconditional, never ranked away - see _TYPE_FLOORS comment)."""
    query_words = _query_words(message, asks)
    selected: list[dict] = []
    used_chars = 0

    def _entry(rid: str, record_type: str, score: float | None) -> dict | None:
        record = repository_records.get(rid)
        if record is None:
            return None
        head = _head_text(record)
        return {
            "id": rid,
            "record_type": record_type,
            "score": round(score, 3) if score is not None else None,
            "head": head,
            "confidence": (record.get("confidence") or {}).get("formation_confidence"),
            "classification": record.get("classification"),
        }

    for rid in coverage_entry.get("honest_limit") or []:
        entry = _entry(rid, "honest_limit", None)
        if entry is None:
            continue
        selected.append(entry)
        used_chars += len(entry["head"])

    for record_type, floor in _TYPE_FLOORS.items():
        cov_key = _COVERAGE_KEY_BY_TYPE[record_type]
        scored = []
        for rid in coverage_entry.get(cov_key) or []:
            record = repository_records.get(rid)
            if record is None:
                continue
            scored.append((rid, _overlap_coefficient(query_words, record)))
        scored.sort(key=lambda t: (-t[1], t[0]))
        for rid, score in scored[:floor]:
            if used_chars >= budget_chars:
                break
            entry = _entry(rid, record_type, score)
            if entry is None:
                continue
            selected.append(entry)
            used_chars += len(entry["head"])

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
    annotated, never dropped - the continuity rule (spec §5, quality bar 5:
    "no repeated story/quote/term within a session absent an explicit
    request; no invented callbacks") is about repetition, and a follow-up
    about an already-told story needs the model to still see it, just
    marked as already offered.

    Cited as "bar 5" rather than "§5.5": §5 is a flat list of seven quality
    bars with no subsections, so "§5.5" read as a section number that does
    not exist. The reference was always right about WHERE - only the
    notation implied a heading."""
    if not already_told_ids:
        return selected
    told = set(already_told_ids)
    out = []
    for candidate in selected:
        if candidate["record_type"] in ("story", "quote") and candidate["id"] in told:
            candidate = {**candidate, "already_told_this_session": True}
        out.append(candidate)
    return out


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
) -> dict:
    """The full pipeline, Stages A -> E, deterministic, no model call.
    Returns {"cells": [...Stage A...], "candidates": [...B+C+E...],
    "thin_ground": [...D...]} - the structured form; render_evidence_block
    turns this into the §3.3 prose block. Kept separate so callers that
    need the structure (tests, future SSE per-sentence citation anchors)
    never have to re-parse rendered text."""
    cell_matches = match_asks_to_cells(message=message, asks=asks, canon_questions=canon_questions, top_n=top_n_cells)

    selected: list[dict] = []
    seen_ids: set[str] = set()
    for match in cell_matches:
        coverage_entry = coverage.get(match["cell"]) or {}
        for candidate in select_cell_candidates(
            cell=match["cell"], coverage_entry=coverage_entry, repository_records=repository_records, message=message, asks=asks
        ):
            if candidate["id"] in seen_ids:
                continue
            seen_ids.add(candidate["id"])
            selected.append({**candidate, "cell": match["cell"]})

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

    return {"cells": cell_matches, "candidates": selected, "thin_ground": thin_ground}


def render_evidence_block(evidence: dict) -> str:
    """The §3.3 text block itself, ready to ride in the per-turn user
    message (never the cached system prefix). Ids are the exact strings
    the citation-tag grammar (§4.1, [[<record.id>]]) uses - this block and
    the model's own tags share one id vocabulary by construction."""
    lines = [
        "## Ground for this turn (cite only these; anything beyond them is spoken",
        "## as our honest limit, never asserted)",
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
        lines.append(f"- [[{candidate['id']}]] {', '.join(descriptors)} — {head}")
    for topic in evidence["thin_ground"]:
        keywords = ", ".join(topic.get("keywords") or [])
        lines.append(f"- THIN GROUND (do not claim past it): {keywords} — {topic.get('note')}")
    return "\n".join(lines) + "\n"
