"""world_front / facilitator_brief schemas (Website V2 world_front design,
approved to proceed 2026-09-19). Not exercised by the fleet-wide selftest
yet - no world has a world_front record (content migration is a separate,
later stage) - so this is the schema's own direct proof: it validates a
correctly-shaped record of each type, and it rejects the specific
malformations the design's three-mode rendering system exists to prevent.
"""
from jsonschema import Draft202012Validator

from engine.m1.schemas import build_schema

WORLD_FRONT_SCHEMA = build_schema("world_front")
FACILITATOR_BRIEF_SCHEMA = build_schema("facilitator_brief")


def _errors(schema: dict, record: dict) -> list[str]:
    return [e.message for e in Draft202012Validator(schema).iter_errors(record)]


def _minimal_world_front(**overrides) -> dict:
    record = {
        "id": "fix.front.fixture-synthetic",
        "world_id": "fixture-synthetic",
        "record_type": "world_front",
        "schema_version": 2,
        "status": "draft",
        "register": "etic",
        "census_id": "fixture-synthetic",
        "skim": {"tile": {"text": "In our own words.", "grounded_in": ["fix.term.the-way"]}},
        "orientation": {
            "story": [{"text": "p1", "grounded_in": ["fix.term.the-way"]}],
            "documented_stories": [
                {
                    "story_id": "fix.story.the-long-road",
                    "title": "The long road",
                    "when": "early in the movement",
                    "teaser": "a short teaser",
                    "grounded_in": ["fix.story.the-long-road"],
                }
            ],
            "voices": [
                {"figure": "fix.figure.the-elder", "text": "v", "grounded_in": ["fix.term.the-way"], "hedge": "we think"}
            ],
            "floor_note": {"from": "fix.honest_limit.x", "text": "adapted wording", "no_new_claims": True},
            "legacy": [{"text": "l", "grounded_in": ["fix.term.the-way"]}],
            "experience_today": [
                {
                    "text": "still practiced today",
                    "url": "https://example.org",
                    "grounded_in": ["fix.term.the-way"],
                    "verified_on": "2026-09-19",
                }
            ],
            "relations_summary": {"text": "r", "grounded_in": ["fix.term.the-way"]},
            "sourcing": {"text": "s", "grounded_in": ["fix.term.the-way"]},
            "read_first": [{"source": "fix.source.witness-scroll", "note": "start here"}],
        },
        "narrative": {
            "who_speaks": {"text": "w", "figures": ["fix.figure.the-elder"]},
            "quiet": "fix.honest_limit.x",
            "questions": [{"cell": "C-P", "demonstration": "fix.demo.identity-collision", "cite": ["fix.dw.x"]}],
            "pull_quotes": ["fix.quote.witness-saying"],
            "glossary": ["fix.term.the-way"],
        },
        "export": {"include_types": ["story", "quote"]},
    }
    record.update(overrides)
    return record


def _minimal_facilitator_brief(**overrides) -> dict:
    record = {
        "id": "fix.facilitator_brief.fixture-synthetic",
        "world_id": "fixture-synthetic",
        "record_type": "facilitator_brief",
        "schema_version": 2,
        "status": "draft",
        "register": "etic",
        "audience": "facilitator",
        "world_identity": {"text": "x", "grounded_in": ["fix.term.the-way"]},
        "formation_strengths": [{"text": "y", "grounded_in": ["fix.term.the-way"]}],
        "formation_limitations": [{"text": "z", "grounded_in": ["fix.term.the-way"]}],
        "participant_type_fit": [{"text": "a", "grounded_in": ["fix.term.the-way"]}],
        "pairing_guidance": {"text": "b", "grounded_in": ["fix.term.the-way"]},
        "cautions": ["be careful about X"],
        "living_tradition_handling": {"text": "c", "grounded_in": ["fix.term.the-way"]},
        "redirect_notes": {"text": "d", "grounded_in": ["fix.term.the-way"]},
    }
    record.update(overrides)
    return record


def test_a_well_formed_world_front_record_validates_clean():
    assert _errors(WORLD_FRONT_SCHEMA, _minimal_world_front()) == []


def test_a_well_formed_facilitator_brief_record_validates_clean():
    assert _errors(FACILITATOR_BRIEF_SCHEMA, _minimal_facilitator_brief()) == []


def test_mode1_unit_without_grounded_in_is_rejected():
    """A mode 1 unit ({text, grounded_in}) with no grounded_in matches
    neither the mode 1 nor the mode 3 branch of the anyOf - it is simply
    an authored claim with nothing behind it, which this schema exists to
    catch mechanically rather than trust to review."""
    bad = _minimal_world_front()
    bad["skim"]["tile"] = {"text": "In our own words."}
    assert _errors(WORLD_FRONT_SCHEMA, bad) != []


def test_mode1_unit_with_empty_grounded_in_is_rejected():
    """grounded_in must be a NON-EMPTY list (minItems: 1) - an empty list
    is a typed null here (Artifact-1's own sentinel-rule discipline), not
    a valid 'grounded in nothing' state the way term.false_friend's empty
    list legitimately means 'none identified'."""
    bad = _minimal_world_front()
    bad["skim"]["tile"] = {"text": "In our own words.", "grounded_in": []}
    assert _errors(WORLD_FRONT_SCHEMA, bad) != []


def test_mode3_unit_requires_from_text_and_no_new_claims_true():
    good = _minimal_world_front()
    good["orientation"]["floor_note"] = {"from": "fix.honest_limit.x", "text": "adapted", "no_new_claims": True}
    assert _errors(WORLD_FRONT_SCHEMA, good) == []

    missing_from = _minimal_world_front()
    missing_from["orientation"]["floor_note"] = {"text": "adapted", "no_new_claims": True}
    assert _errors(WORLD_FRONT_SCHEMA, missing_from) != []

    false_flag = _minimal_world_front()
    false_flag["orientation"]["floor_note"] = {"from": "fix.honest_limit.x", "text": "adapted", "no_new_claims": False}
    assert _errors(WORLD_FRONT_SCHEMA, false_flag) != []


def test_register_is_not_a_settable_field_on_any_unit():
    """Deliberate design-review finding: per-unit register was tried and
    rejected as incompatible with this schema system's additionalProperties:
    false architecture. register belongs on the envelope only - a unit
    that tries to carry its own is an unknown-field error, the same as any
    other stray key."""
    bad = _minimal_world_front()
    bad["skim"]["tile"] = {"text": "In our own words.", "grounded_in": ["fix.term.the-way"], "register": "etic"}
    assert _errors(WORLD_FRONT_SCHEMA, bad) != []


def test_experience_today_requires_verified_on():
    bad = _minimal_world_front()
    bad["orientation"]["experience_today"] = [
        {"text": "still practiced today", "url": "https://example.org", "grounded_in": ["fix.term.the-way"]}
    ]
    assert _errors(WORLD_FRONT_SCHEMA, bad) != []


def test_unknown_top_level_field_is_a_hard_error():
    bad = _minimal_world_front()
    bad["extra_field"] = "not part of the schema"
    assert _errors(WORLD_FRONT_SCHEMA, bad) != []


def test_facilitator_brief_audience_is_fixed_to_facilitator():
    bad = _minimal_facilitator_brief(audience="participant")
    assert _errors(FACILITATOR_BRIEF_SCHEMA, bad) != []


def test_facilitator_brief_cautions_is_a_plain_string_list_not_units():
    good = _minimal_facilitator_brief()
    good["cautions"] = ["first caution", "second caution"]
    assert _errors(FACILITATOR_BRIEF_SCHEMA, good) == []

    bad = _minimal_facilitator_brief()
    bad["cautions"] = [{"text": "a caution", "grounded_in": ["fix.term.the-way"]}]
    assert _errors(FACILITATOR_BRIEF_SCHEMA, bad) != []
