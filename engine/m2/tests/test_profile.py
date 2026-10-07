"""The World Profile view (engine/m2/profile.py) and the optional record fields
it and the prompt builder read. Synthetic records, no network."""
from engine.m1.schemas import build_schema
from engine.m2 import cli
from engine.m2.builders import SOURCE_ANCHOR_HEADER, _GROUND_LINE, build_prompt
from engine.m2.profile import NOT_CARRIED, SECTION_TITLES, build_profile

from .test_prompt_regions import CORE, CRAFT, REGISTRY_ENTRY, REPOSITORY

OBSERVATION = "Worship and doctrine are one act here, and no single lens shows it."
ANCHOR = "Our images come from the two letters we hold. When a fitting image does not come from them, we fall back to the plain shape of our own life."

GRAVITY = {
    "id": "fix.gravity.the-letter", "record_type": "gravity", "classification": "primary", "name": "The Letter [PRIMARY]",
    "description": "The letter shapes everything.", "confidence": {"formation_confidence": "Documented"},
    "sources": [{"source_id": "fix.source.letter", "locus": "1"}],
}
TENSION = {"id": "fix.gravity.the-pull", "record_type": "gravity", "classification": "tensional", "name": "The Pull", "description": "Two ways at once."}
FORCE = {
    "id": "fix.force.the-move", "record_type": "force", "name": "The Move", "kind": "initiating", "matrix_cell": "1A",
    "description": "A move from outside.", "relations": [{"type": "associated-with", "target": "fix.gravity.the-letter"}],
}
TERM = {"id": "fix.term.word", "record_type": "term", "world_word": "logos", "plain_meaning": "the word", "quick_meaning": "the word said", "distortion_risk": "low", "false_friend": ["reason"]}
CLAIM = {"id": "fix.contested.date", "record_type": "contested_claim", "claim": "The letter dates to 150.", "held_against": ["a later date"], "concedes": "The date is uncertain.", "confidence": {"formation_confidence": "Contested"}}
LIMIT = {"id": "fix.limit.women", "record_type": "honest_limit", "statement": "We hold no woman's writing.", "why_sources_cannot_answer": "None survives.", "nearest_material": ["fix.quote.q1"]}
ENTRY = {"display_name": "Fixture World", "time_window": {"start": 100, "end": 200}, "place": "Testland", "living_tradition_flag": False}


def _records(*extra, core=CORE):
    records = {r["id"]: r for r in (core, *extra)}
    return records


def _full(core=None):
    return _records(GRAVITY, TENSION, FORCE, TERM, CLAIM, LIMIT, core=core or {**CORE, "integrative_observation": OBSERVATION, "living_traditions": "We name no living communion."})


def _section(text, number):
    head = f"## Section {number}: "
    start = text.index(head)
    nxt = text.find("\n## ", start + 1)
    return text[start : nxt if nxt != -1 else len(text)]


def test_a_world_with_records_for_a_section_renders_that_section_from_them():
    text = build_profile(_full(), ENTRY, "fix")
    assert "### Primary Gravities" in text and "The letter shapes everything." in text and "fix.source.letter" in text
    assert "**Cell:** 1A" in text and "**Gravity connection:** fix.gravity.the-letter" in text
    assert "### logos" in text and "**False friends:**\n- reason" in text
    assert "The date is uncertain." in text and "We hold no woman's writing." in text
    assert "**Temporal scope:** 100-200" in text and "**Geographic scope:** Testland" in text
    assert OBSERVATION in _section(text, 10)
    assert "We name no living communion." in _section(text, 9)


def test_the_integrative_observation_renders_only_when_the_record_carries_it():
    with_it = build_profile(_full(), ENTRY, "fix")
    without = build_profile(_full(core=CORE), ENTRY, "fix")
    assert OBSERVATION in with_it
    assert OBSERVATION not in without and NOT_CARRIED in _section(without, 10)


def test_a_section_no_record_carries_is_one_plain_line_and_nothing_is_invented():
    text = build_profile(_records(), {"display_name": "Bare"}, "bare")
    for number in (2, 4, 5, 6, 7, 10):
        assert _section(text, number).split("\n", 2)[2].strip() == NOT_CARRIED
    assert "**World Profile completion status:** INCOMPLETE" in text


def test_the_ecological_summary_is_never_carried_by_records():
    assert NOT_CARRIED in _section(build_profile(_full(), ENTRY, "fix"), 4)


def test_all_eleven_sections_are_present_in_order():
    text = build_profile(_full(), ENTRY, "fix")
    positions = [text.index(f"## Section {n}: ") for n in range(1, 12)]
    assert positions == sorted(positions) and len(SECTION_TITLES) == 10


def test_the_view_is_deterministic():
    assert build_profile(_full(), ENTRY, "fix") == build_profile(dict(reversed(list(_full().items()))), ENTRY, "fix")


def test_the_command_prints_the_profile_and_refuses_an_unknown_world(capsys, tmp_path):
    assert cli.main(["profile", "fix"]) == 0
    assert capsys.readouterr().out.startswith("# World Profile: Fixture World (synthetic) (fix)")
    out = tmp_path / "p.md"
    assert cli.main(["profile", "fix", "--out", str(out)]) == 0 and out.read_text().startswith("# World Profile")
    assert cli.main(["profile", "no-such-world"]) == 1


def test_the_optional_fields_validate_in_the_record_schema():
    import jsonschema

    jsonschema.Draft202012Validator.check_schema(build_schema("world_core"))
    assert "integrative_observation" in build_schema("world_core")["properties"]
    craft = build_schema("voice_craft")["properties"]
    assert "source_anchor" in craft and "source_anchor_entries" in craft


def test_the_prompt_is_byte_identical_when_the_optional_fields_are_absent_or_not_spoken():
    base = build_prompt(REPOSITORY, REGISTRY_ENTRY)
    observed = {**REPOSITORY, CORE["id"]: {**CORE, "integrative_observation": OBSERVATION}}
    assert build_prompt(observed, REGISTRY_ENTRY) == base
    listed = {**REPOSITORY, CRAFT["id"]: {**CRAFT, "source_anchor_entries": ["a", "b", "c", "d", "e"]}}
    assert build_prompt(listed, REGISTRY_ENTRY) == base
    assert SOURCE_ANCHOR_HEADER not in base.decode("utf-8")


def test_a_source_anchor_compiles_as_its_own_section_above_the_ground_line():
    anchored = {**REPOSITORY, CRAFT["id"]: {**CRAFT, "source_anchor": ANCHOR}}
    text = build_prompt(anchored, REGISTRY_ENTRY).decode("utf-8")
    section = f"## {SOURCE_ANCHOR_HEADER}\n\n{ANCHOR}\n"
    assert section in text and text.index(section) < text.index(_GROUND_LINE)
    assert "[[" not in section
    assert text.count(ANCHOR) == 1
