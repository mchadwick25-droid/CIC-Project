"""Compiles a world_front record + its referenced records into the
resolved per-world JSON the participant-facing website reads
(cic-website/data/worlds/<census_id>.json) - the compiler stage of the
Website V2 world_front design (approved to proceed 2026-09-19).

Deliberately its own module, not folded into engine/m2/compiler.py's own
compile_world(): that function's whole job is producing what reaches the
Representative's own prompt/capsule/chunks/repository, and world_front/
facilitator_brief must never enter that pipeline at all (see
engine/m2/builders.py's own CHUNK_DIR_BY_TYPE/_PACKAGE_EXCLUDED_RECORD_
TYPES comments, and engine/m2/tests/test_voice_assembly_exclusion.py's
own regression proof). Keeping this compilation a structurally separate
function, over a structurally separate output, is a second, independent
guarantee beyond the exclusion lists themselves: nothing here can ever be
wired into compile_world()'s own return value, because it is never
called from there, and compile_world() never calls this.

Like every builder in engine/m2/builders.py, this is a pure function:
same world_front record + same referenced records in, same bytes out. No
filesystem writes happen here - a caller (a CLI, same shape as
engine/m2/cli.py) decides where the compiled JSON actually lands.

Never copies a referenced record's markdown BODY (the free-text
provenance/review notes after the closing `---` fence, the loader's own
`_body` field) into the output - only structured front-matter fields,
the same discipline engine/m2/builders.py already holds for
_chunk_text() and build_repository_json()'s own _PACKAGE_STRIPPED_FIELDS.
"""
from engine.m4.citation_cards import _quote_speaker_label

from .canonical import canonical_json, sha256_prefixed


def _by_id(*record_dicts: dict) -> dict:
    """Records from every dict passed, world/local records winning over
    fleet on a rare id collision - same precedence build_prompt()'s own
    lookups already assume (a world's own record set is looked up first
    in this codebase's other builders)."""
    merged: dict = {}
    for d in record_dicts:
        merged.update(d)
    return merged


def _resolve_unit(unit: dict | None) -> dict | None:
    """A world_front rendering unit - mode 1 ({text, grounded_in}) or
    mode 3 ({from, text, no_new_claims}) - resolved to the one shape a
    site template needs: {"text": ..., "grounded_in": [...]}. Mode 3's
    `from` is folded into grounded_in (an adapted rendering is still
    grounded in the record it adapts); `no_new_claims` is a schema/gate-
    time obligation (engine.m1.gates.check_mode3_claim_fidelity), not
    something the compiled site needs to carry forward."""
    if not unit:
        return None
    if "from" in unit:
        return {"text": unit.get("text"), "grounded_in": [unit["from"]]}
    return {"text": unit.get("text"), "grounded_in": list(unit.get("grounded_in") or [])}


def _resolve_units(units: list | None) -> list:
    return [u for u in (_resolve_unit(unit) for unit in (units or [])) if u]


def _confidence_label(record: dict | None) -> str | None:
    """The record's own five-level confidence vocabulary label
    (_CONFIDENCE_SCHEMA.formation_confidence, engine/m1/schemas.py) -
    passed through rather than re-mapped, since that vocabulary (Widely
    Accepted / Dominant Modern Reconstruction / Inferential-Thin /
    Contested / Documented) already IS the plain-word rendering the
    design calls for; there is no further translation to do."""
    if not record:
        return None
    return (record.get("confidence") or {}).get("formation_confidence")


def _resolve_story(story_id: str | None, records: dict) -> dict | None:
    rec = records.get(story_id) if story_id else None
    if not rec:
        return None
    return {
        "id": story_id,
        "text": rec.get("text"),
        "tellable_as": rec.get("tellable_as"),
        "confidence": _confidence_label(rec),
    }


def _resolve_quote(quote_id: str | None, records: dict) -> dict | None:
    """`modern_rendering` only - NEVER `text` (Mark's standing quote
    ruling). See engine/m1/gates.py's gate_quote_mark_fidelity for the
    mechanical check that a world_front's own AUTHORED prose already
    follows this rule before it ever reaches this compiler; this is the
    same field choice made independently, at compile time, for the
    reference itself.

    `speaker_or_author` is resolved through citation_cards.py's own
    `_quote_speaker_label` rather than passed through raw: the corpus
    authors this field two legitimate ways (a `figure` record id, or
    already-readable prose - engine/m1/cross_world.py's
    check_quote_speaker_labels), and this compiler has the same full-
    repository access citation_cards.py's own docstring gives as the
    reason to resolve a figure id through the figure's own name rather
    than a cruder id-to-slug fallback. Found live in 6 of 8 built worlds'
    pull_quotes during the site-cutover build (worked around at the
    render layer first; fixed at the actual source here)."""
    rec = records.get(quote_id) if quote_id else None
    if not rec:
        return None
    return {
        "id": quote_id,
        "text": rec.get("modern_rendering"),
        "speaker_or_author": _quote_speaker_label(rec, records),
        "confidence": _confidence_label(rec),
    }


def _resolve_term(term_id: str | None, records: dict) -> dict | None:
    rec = records.get(term_id) if term_id else None
    if not rec:
        return None
    return {
        "id": term_id,
        "world_word": rec.get("world_word"),
        "meaning": rec.get("plain_meaning") or rec.get("quick_meaning"),
        "confidence": _confidence_label(rec),
    }


def _resolve_figure(figure_id: str | None, records: dict) -> dict | None:
    rec = records.get(figure_id) if figure_id else None
    if not rec:
        return None
    return {"id": figure_id, "names": rec.get("names") or [], "dates": rec.get("dates") or {}}


def _resolve_honest_limit(limit_id: str | None, records: dict) -> dict | None:
    rec = records.get(limit_id) if limit_id else None
    if not rec:
        return None
    # Rendered verbatim from the record's own `statement` field (mode 2) -
    # never trimmed, never paraphrased.
    return {"id": limit_id, "statement": rec.get("statement")}


def _resolve_doctrinal_witness(dw_id: str | None, records: dict) -> dict | None:
    rec = records.get(dw_id) if dw_id else None
    if not rec:
        return None
    return {"id": dw_id, "text": rec.get("text"), "confidence": _confidence_label(rec)}


# narrative.questions[].cite's schema (engine/m1/schemas.py) allows any
# record id, but every world built so far only ever cited doctrinal_witness
# records in practice - until hal's and ijc's own builds each independently
# found _resolve_doctrinal_witness() silently emitting a {"text": None}
# entry for a cite pointing at a different record type (a story, in ijc's
# case; both worked around it in their own content rather than fix the
# compiler). This is the field that actually holds each type's content;
# quote is deliberately absent - a `cite` is evidence for a demonstration's
# own answer-ground, not a quotable line, so a quote belongs in
# `pull_quotes` (resolved through _resolve_quote's own modern_rendering-only
# rule) rather than here.
_CITE_TEXT_FIELD_BY_TYPE = {
    "doctrinal_witness": "text",
    "story": "text",
    "honest_limit": "statement",
    "contested_claim": "claim",
    "gravity": "description",
    "force": "description",
}


def _resolve_citation(cite_id: str | None, records: dict) -> dict | None:
    """A `narrative.questions[].cite` entry, type-aware. Returns None -
    dropped from the compiled list, same as an unresolved id - for a
    record type this citation shape doesn't cover, rather than emit an
    entry with a null `text` a template would render as empty."""
    rec = records.get(cite_id) if cite_id else None
    if not rec:
        return None
    field = _CITE_TEXT_FIELD_BY_TYPE.get(rec.get("record_type"))
    if field is None:
        return None
    return {"id": cite_id, "record_type": rec.get("record_type"), "text": rec.get(field), "confidence": _confidence_label(rec)}


def _resolve_source(source_id: str | None, records: dict) -> dict | None:
    rec = records.get(source_id) if source_id else None
    if not rec:
        return None
    return {"id": source_id, "author": rec.get("author"), "work": rec.get("work")}


def _resolve_demonstration(demo_id: str | None, records: dict) -> dict | None:
    rec = records.get(demo_id) if demo_id else None
    if not rec:
        return None
    return {"id": demo_id, "exchange": rec.get("exchange") or []}


def _skim(world_front: dict) -> dict:
    skim = world_front.get("skim") or {}
    return {"tile": _resolve_unit(skim.get("tile"))}


def _orientation(world_front: dict, records: dict) -> dict:
    orientation = world_front.get("orientation") or {}

    documented_stories = []
    for entry in orientation.get("documented_stories") or []:
        story = _resolve_story(entry.get("story_id"), records)
        documented_stories.append(
            {
                "story_id": entry.get("story_id"),
                # title/when/teaser are the world_front's OWN curated
                # framing (the story record itself has no such fields) -
                # text/confidence are pulled from the story record.
                "title": entry.get("title"),
                "when": entry.get("when"),
                "teaser": entry.get("teaser"),
                "text": story.get("text") if story else None,
                "confidence": story.get("confidence") if story else None,
            }
        )

    voices = []
    for entry in orientation.get("voices") or []:
        resolved = _resolve_unit(entry) or {}
        voices.append(
            {
                **resolved,
                "figure": _resolve_figure(entry.get("figure"), records),
                "hedge": entry.get("hedge"),
            }
        )

    experience_today = []
    for entry in orientation.get("experience_today") or []:
        resolved = _resolve_unit(entry) or {}
        experience_today.append(
            {**resolved, "url": entry.get("url"), "verified_on": entry.get("verified_on")}
        )

    read_first = [
        {"source": _resolve_source(entry.get("source"), records), "note": entry.get("note")}
        for entry in orientation.get("read_first") or []
    ]

    return {
        "story": _resolve_units(orientation.get("story")),
        "documented_stories": documented_stories,
        "voices": voices,
        "floor_note": _resolve_unit(orientation.get("floor_note")),
        "legacy": _resolve_units(orientation.get("legacy")),
        "experience_today": experience_today,
        "relations_summary": _resolve_unit(orientation.get("relations_summary")),
        "sourcing": _resolve_unit(orientation.get("sourcing")),
        "read_first": read_first,
    }


def _narrative(world_front: dict, records: dict) -> dict:
    narrative = world_front.get("narrative") or {}
    who_speaks = narrative.get("who_speaks") or {}

    questions = [
        {
            "cell": entry.get("cell"),
            "demonstration": _resolve_demonstration(entry.get("demonstration"), records),
            "cite": [
                w
                for w in (_resolve_citation(cid, records) for cid in (entry.get("cite") or []))
                if w
            ],
        }
        for entry in narrative.get("questions") or []
    ]

    return {
        "who_speaks": {
            "text": who_speaks.get("text"),
            "figures": [
                f
                for f in (_resolve_figure(fid, records) for fid in (who_speaks.get("figures") or []))
                if f
            ],
        },
        # mode 2: the honest_limit's own `statement` field, verbatim.
        "quiet": _resolve_honest_limit(narrative.get("quiet"), records),
        "questions": questions,
        # mode 2, each: quote.modern_rendering, never quote.text.
        "pull_quotes": [
            q for q in (_resolve_quote(qid, records) for qid in (narrative.get("pull_quotes") or [])) if q
        ],
        "glossary": [
            t for t in (_resolve_term(tid, records) for tid in (narrative.get("glossary") or [])) if t
        ],
    }


def compile_world_front(
    world_front: dict,
    records: dict,
    fleet: dict,
    *,
    compiler_version: str,
    records_commit: str,
) -> bytes:
    """world_front record + its referenced records -> the resolved JSON a
    site template reads directly, with every reference already expanded
    (story text, quote modern_rendering, honest_limit statement, figure
    names/dates, term meanings, confidence labels) and no record's
    markdown body notes anywhere in it.

    `_generated_by` is written first (canonical_json's own sort_keys=True
    puts any underscore-prefixed key ahead of every lowercase one, the
    same property engine/m2/compiler.py's own _stamp() already relies on)
    and carries three things, for the site-staleness CI check: this
    compiler's own version/commit, the records commit it read, and a
    hash of the world_front record itself - so a change to any of the
    three is independently visible in the compiled output's own header,
    without having to diff the whole file to find out which one moved.
    """
    all_records = _by_id(fleet, records)
    world_front_hash = sha256_prefixed(canonical_json(world_front))
    provenance = (
        f"cic-m2-site-compiler {compiler_version} from records_commit {records_commit}, "
        f"world_front {world_front.get('id')} {world_front_hash}"
    )
    payload = {
        "_generated_by": provenance,
        "census_id": world_front.get("census_id"),
        "skim": _skim(world_front),
        "orientation": _orientation(world_front, all_records),
        "narrative": _narrative(world_front, all_records),
    }
    return canonical_json(payload)
