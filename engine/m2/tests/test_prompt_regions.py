"""The compiled prompt's two regions (engine/m2/builders.py::build_prompt).

Above _GROUND_LINE: standing instruction - the fleet's own register/
pronoun/citation/limit segment and this world's voice_craft. No ids, and
none invented for it. Below: the world's own record, every section
addressed by an id in the [[id]] form the citation contract asks for.

The thing actually under test is that voice_craft is never given the
"(cite as [[id]])" treatment. Every voice_craft record in the fleet
carries `sources: []` on purpose (spec principle 14), so instructing a
live model to cite one produces a citation that cannot resolve to a
source by any path - which a live M3 admission probe did produce,
[[desert.voice.craft]] on f3-t-probe-01. Synthetic fixture records, same
discipline as test_demo_tagging.py's own.
"""
from engine.m2.builders import _GROUND_LINE, build_prompt

FLEET = {
    "_fleet.voice.fleet": {
        "id": "_fleet.voice.fleet",
        "record_type": "fleet_voice",
        "register_statements": [{"number": 1, "statement": "One idea per sentence."}],
        "pronoun_rule": "Strict we-voice, always, for {world}.",
        "citation_contract": "Every claim carries the id of the record it draws on.",
        "limit_discipline": "What the ground does not support is spoken as our own limit.",
    }
}

CRAFT = {
    "id": "fix.voice.craft",
    "record_type": "voice_craft",
    "sources": [],
    "identity": "Vera, Witness - a composite voice for the fixture world's two short sources.",
    "guard": "Honest thinness beats invented depth, absolutely.",
    "characteristic_concerns": ["what a short record can and cannot carry"],
    "flavor_notes": [{"segment": "self-reference", "note": "Strict we-voice."}],
}

CORE = {
    "id": "fix.core.fix",
    "record_type": "world_core",
    "horizon": "A two-source fixture world.",
    "formation_logic": "Formation by reading the two sources it has.",
    "thinness": "Thin on everything except its two sources.",
    "cautions": "Never stand in for a real world.",
}

WITNESS = {
    "id": "fix.witness.who-is-jesus",
    "record_type": "doctrinal_witness",
    "canon_cells": ["C-I"],
    "text": "We did not claim to have seen him ourselves.",
}

REPOSITORY = {r["id"]: r for r in (CRAFT, CORE, WITNESS)}
REGISTRY_ENTRY = {"display_name": "Fixture World"}


def _prompt() -> str:
    return build_prompt(REPOSITORY, FLEET, REGISTRY_ENTRY).decode("utf-8")


def test_no_voice_craft_section_is_ever_addressed_by_an_id():
    """The whole point. `sources: []` is by design on this record type, so
    a citation of it is honest and still unresolvable - the compiler must
    not ask for one."""
    prompt = _prompt()
    assert "fix.voice.craft" not in prompt
    assert "(cite as [[fix.voice.craft]])" not in prompt


def test_the_voice_craft_sections_are_headed_as_instruction_not_as_nouns():
    """A plain-noun heading reads as an id namespace - measured: the
    section headed "Identity" produced two invented ids, "Cautions"
    produced one, on a package where neither header carried an id. A
    heading phrased as a clause in the voice's own we-form cannot be read
    as an id segment, since id segments are single lowercase tokens."""
    prompt = _prompt()
    for heading in ("## Who we are", "## What we hold ourselves to",
                    "## What we keep returning to", "## How we word things"):
        assert heading in prompt
    for heading in ("## Identity", "## Guard", "## Characteristic concerns", "## Flavor notes"):
        assert heading not in prompt


def test_every_voice_craft_field_still_reaches_the_prompt():
    """Untagged, not dropped - the voice still gets all four fields."""
    prompt = _prompt()
    assert CRAFT["identity"] in prompt
    assert CRAFT["guard"] in prompt
    assert CRAFT["characteristic_concerns"][0] in prompt
    assert CRAFT["flavor_notes"][0]["note"] in prompt


def test_the_ground_line_separates_the_untagged_half_from_the_addressed_half():
    prompt = _prompt()
    boundary = prompt.index(_GROUND_LINE)
    above, below = prompt[:boundary], prompt[boundary + len(_GROUND_LINE):]

    assert "(cite as [[" not in above
    for field in ("identity", "guard"):
        assert CRAFT[field] in above

    assert "(cite as [[fix.core.fix]])" in below
    assert "(cite as [[fix.witness.who-is-jesus]])" in below


def test_the_fleet_preamble_stays_first_and_stays_untagged():
    """It always was untagged, and it has never had an id invented for it -
    that is the evidence the voice_craft move rests on."""
    prompt = _prompt()
    assert prompt.startswith("## Register")
    assert prompt.index("## Register") < prompt.index("## Who we are") < prompt.index(_GROUND_LINE)


def test_a_prompt_with_no_standing_instruction_writes_no_boundary():
    """A boundary needs two sides. Never a real compile - every world
    loads the fleet record - but a bare-records unit fixture would
    otherwise open with a paragraph about material above it that is not
    there."""
    prompt = build_prompt({WITNESS["id"]: WITNESS}, {}, REGISTRY_ENTRY).decode("utf-8")
    assert _GROUND_LINE not in prompt
    assert prompt.startswith("## Witness (C-I) (cite as [[fix.witness.who-is-jesus]])")
