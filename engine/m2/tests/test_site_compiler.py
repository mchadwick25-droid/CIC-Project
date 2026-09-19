"""engine.m2.site_compiler.compile_world_front - the Website V2
world_front compiler stage (approved to proceed 2026-09-19). No real
world_front record exists yet (content migration is a separate, later
stage), so this is tested against a hand-constructed minimal record, as
the design's own validation instructions call for.
"""
import json

from engine.m2.site_compiler import compile_world_front

STORY = {
    "id": "fix.story.the-long-road",
    "record_type": "story",
    "text": "The long road story's own full text.",
    "tellable_as": "a short teller's version",
    "confidence": {"formation_confidence": "Widely Accepted"},
}

QUOTE = {
    "id": "fix.quote.identity-collision-saying",
    "record_type": "quote",
    "text": "The archaic original, Apparatus/Level-3-only.",
    "modern_rendering": "The plain modern spoken form.",
    "speaker_or_author": "fix.figure.the-elder",
    "license": "verbatim",
    "confidence": {"formation_confidence": "Documented"},
}

TERM = {
    "id": "fix.term.the-way",
    "record_type": "term",
    "world_word": "the Way",
    "plain_meaning": "A plain-language meaning of the term.",
    "quick_meaning": "A short gloss.",
    "confidence": {"formation_confidence": "Widely Accepted"},
}

FIGURE = {
    "id": "fix.figure.the-elder",
    "record_type": "figure",
    "names": [{"name": "The Elder", "tag": "in-world"}],
    "dates": {"born": 100, "died": 180},
}

HONEST_LIMIT = {
    "id": "fix.limit.x",
    "record_type": "honest_limit",
    "statement": "We cannot say for certain how this practice began.",
}

DOCTRINAL_WITNESS = {
    "id": "fix.witness.who-is-jesus",
    "record_type": "doctrinal_witness",
    "text": "We did not claim to have seen him ourselves.",
    "confidence": {"formation_confidence": "Contested"},
}

DEMONSTRATION = {
    "id": "fix.demo.identity-collision",
    "record_type": "demonstration",
    "exchange": [{"speaker": "participant", "text": "Q"}, {"speaker": "representative", "text": "A"}],
}

SOURCE = {
    "id": "fix.source.witness-scroll",
    "record_type": "source",
    "author": "Unknown",
    "work": "The Witness Scroll",
}

# A record with a markdown body ("_body") the compiler must never surface.
STORY_WITH_BODY = {**STORY, "_body": "PROVENANCE_NOTE_MUST_NEVER_APPEAR_IN_COMPILED_OUTPUT", "_path": "records/fix/story/x.md"}

RECORDS = {
    r["id"]: r
    for r in (STORY_WITH_BODY, QUOTE, TERM, FIGURE, HONEST_LIMIT, DOCTRINAL_WITNESS, DEMONSTRATION, SOURCE)
}

WORLD_FRONT = {
    "id": "fix.front.fixture-synthetic",
    "world_id": "fixture-synthetic",
    "record_type": "world_front",
    "census_id": "fixture-synthetic",
    "skim": {"tile": {"text": "A tile.", "grounded_in": [QUOTE["id"]]}},
    "orientation": {
        "story": [{"text": "p1", "grounded_in": [STORY["id"]]}],
        "documented_stories": [
            {
                "story_id": STORY["id"],
                "title": "The long road",
                "when": "early on",
                "teaser": "a teaser",
                "grounded_in": [STORY["id"]],
            }
        ],
        "voices": [
            {"figure": FIGURE["id"], "text": "v", "grounded_in": [QUOTE["id"]], "hedge": "we think"}
        ],
        "floor_note": {"from": HONEST_LIMIT["id"], "text": "adapted floor note", "no_new_claims": True},
        "legacy": [{"text": "l", "grounded_in": [TERM["id"]]}],
        "experience_today": [
            {
                "text": "still practiced",
                "url": "https://example.org",
                "grounded_in": [TERM["id"]],
                "verified_on": "2026-09-19",
            }
        ],
        "relations_summary": {"text": "r", "grounded_in": [DOCTRINAL_WITNESS["id"]]},
        "sourcing": {"text": "s", "grounded_in": [SOURCE["id"]]},
        "read_first": [{"source": SOURCE["id"], "note": "start here"}],
    },
    "narrative": {
        "who_speaks": {"text": "w", "figures": [FIGURE["id"]]},
        "quiet": HONEST_LIMIT["id"],
        "questions": [{"cell": "C-P", "demonstration": DEMONSTRATION["id"], "cite": [DOCTRINAL_WITNESS["id"]]}],
        "pull_quotes": [QUOTE["id"]],
        "glossary": [TERM["id"]],
    },
    "export": {"include_types": ["story", "quote"]},
}


def _compile() -> dict:
    payload = compile_world_front(
        WORLD_FRONT, RECORDS, {}, compiler_version="test-version", records_commit="test-commit"
    )
    return json.loads(payload)


def test_generated_by_is_present_and_carries_all_three_provenance_parts():
    out = _compile()
    assert "_generated_by" in out
    assert "test-version" in out["_generated_by"]
    assert "test-commit" in out["_generated_by"]
    assert "sha256:" in out["_generated_by"]


def test_generated_by_is_the_first_key_in_the_serialized_bytes():
    """canonical_json's own sort_keys=True puts an underscore-prefixed key
    ahead of every lowercase one - the same property compiler.py's own
    _stamp() already relies on."""
    payload = compile_world_front(
        WORLD_FRONT, RECORDS, {}, compiler_version="v", records_commit="c"
    ).decode("utf-8")
    assert payload.startswith('{"_generated_by"')


def test_skim_tile_resolves_mode1_unit():
    out = _compile()
    assert out["skim"]["tile"] == {"text": "A tile.", "grounded_in": [QUOTE["id"]]}


def test_documented_story_pulls_its_own_curated_fields_and_the_story_records_text():
    out = _compile()
    entry = out["orientation"]["documented_stories"][0]
    assert entry["title"] == "The long road"
    assert entry["teaser"] == "a teaser"
    assert entry["text"] == STORY["text"]
    assert entry["confidence"] == "Widely Accepted"


def test_floor_note_mode3_unit_resolves_from_into_grounded_in():
    out = _compile()
    assert out["orientation"]["floor_note"] == {"text": "adapted floor note", "grounded_in": [HONEST_LIMIT["id"]]}


def test_pull_quotes_resolve_from_modern_rendering_never_text():
    out = _compile()
    quote = out["narrative"]["pull_quotes"][0]
    assert quote["text"] == QUOTE["modern_rendering"]
    assert quote["text"] != QUOTE["text"]


def test_quiet_is_the_honest_limits_own_statement_verbatim():
    out = _compile()
    assert out["narrative"]["quiet"]["statement"] == HONEST_LIMIT["statement"]


def test_glossary_resolves_term_meaning_and_word():
    out = _compile()
    term = out["narrative"]["glossary"][0]
    assert term["world_word"] == "the Way"
    assert term["meaning"] == TERM["plain_meaning"]


def test_who_speaks_resolves_figure_names_and_dates():
    out = _compile()
    figure = out["narrative"]["who_speaks"]["figures"][0]
    assert figure["names"] == FIGURE["names"]
    assert figure["dates"] == FIGURE["dates"]


def test_questions_resolve_demonstration_and_cited_witnesses():
    out = _compile()
    q = out["narrative"]["questions"][0]
    assert q["demonstration"]["id"] == DEMONSTRATION["id"]
    assert q["cite"][0]["text"] == DOCTRINAL_WITNESS["text"]


def test_no_record_markdown_body_ever_appears_in_the_compiled_output():
    payload = compile_world_front(
        WORLD_FRONT, RECORDS, {}, compiler_version="v", records_commit="c"
    ).decode("utf-8")
    assert "PROVENANCE_NOTE_MUST_NEVER_APPEAR_IN_COMPILED_OUTPUT" not in payload
    assert "_body" not in payload
    assert "_path" not in payload


def test_compile_is_deterministic():
    a = compile_world_front(WORLD_FRONT, RECORDS, {}, compiler_version="v", records_commit="c")
    b = compile_world_front(WORLD_FRONT, RECORDS, {}, compiler_version="v", records_commit="c")
    assert a == b
