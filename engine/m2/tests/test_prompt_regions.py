"""The compiled prompt's two regions (engine/m2/builders.py::build_prompt).

Above _GROUND_LINE: standing instruction - this world's voice_craft, beneath
the engine's shape segment, which is sent ahead of the prompt as its own
system block. No ids, and none invented for it. Below: the world's own record, every section
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

CRAFT = {
    "id": "fix.voice.craft",
    "record_type": "voice_craft",
    "sources": [],
    "identity": "Vera, Witness - a composite voice for the fixture world's two short sources.",
    "guard": "Honest thinness beats invented depth, absolutely.",
    "characteristic_concerns": ["what a short record can and cannot carry"],
    "flavor_notes": [{"segment": "place", "note": "The two sources stay concrete."},
                     {"segment": "self-reference", "note": "Strict we-voice, restated."}],
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
    return build_prompt(REPOSITORY, REGISTRY_ENTRY).decode("utf-8")


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


def test_the_prompt_opens_with_who_we_are_naming_the_world():
    """The shape segment's sanctioned "I am a representative of" points here
    for the world's own name."""
    prompt = _prompt()
    assert prompt.startswith("## Who we are\n\nOur world's name: Fixture World.\n\n" + CRAFT["identity"])
    assert "## Register" not in prompt and "## Citation contract" not in prompt


def test_flavor_notes_that_restate_the_shape_segment_are_not_compiled():
    prompt = _prompt()
    assert "Strict we-voice, restated." not in prompt and "[self-reference]" not in prompt
    assert "- [place] The two sources stay concrete." in prompt


def test_records_with_no_voice_craft_still_sit_below_the_boundary():
    """The shape segment always stands above the prompt, so the line is
    written whenever there are records below it."""
    prompt = build_prompt({WITNESS["id"]: WITNESS}, REGISTRY_ENTRY).decode("utf-8")
    assert prompt.startswith("## Who we are\n\nOur world's name: Fixture World.\n")
    assert prompt.index(_GROUND_LINE) < prompt.index("## Witness (C-I) (cite as [[fix.witness.who-is-jesus]])")


def test_the_gravities_list_strips_the_build_taxonomy_bracket_not_the_name():
    """A gravity's own `name` field ends in a bracketed build taxonomy tag
    (e.g. "Divine Pedagogy [SUPPORTING - explanatory framework]") - real
    and useful to a reviewer, never meant for a model prompt.
    engine.m4.citation_cards._short_name already stripped this for the
    participant-facing citation card; build_prompt's own Gravities list
    did not, so the raw tag reached the model. Shared fix, via
    engine.prose.strip_name_taxonomy_tag - see
    test_citation_cards.py::test_gravity_and_force_labels_strip_the_
    build_taxonomy_bracket_not_the_name for the citation-card half."""
    gravity = {
        "id": "fix.gravity.a-tension",
        "record_type": "gravity",
        "name": "A Tension [TENSIONAL]",
        "description": "Two poles, both real, neither surrendered.",
    }
    prompt = build_prompt({**REPOSITORY, gravity["id"]: gravity}, REGISTRY_ENTRY).decode("utf-8")
    assert "- [[fix.gravity.a-tension]] A Tension" in prompt
    assert "[TENSIONAL]" not in prompt


def test_the_gravities_list_strips_a_leading_tag_too_and_leaves_real_parens_alone():
    """Two rzg gravity records carry the tag first, not last, because the
    name reads better that way - "[TENSIONAL] Council-Led Civic Authority
    (Zurich) vs. Consistorial Independence from Civil Control (Geneva)".
    The real "(Zurich)"/"(Geneva)" parentheses are part of the name, not a
    build-taxonomy bracket, and must survive."""
    gravity = {
        "id": "rzg.gravity.council-led-authority-vs-consistorial-independence",
        "record_type": "gravity",
        "name": "[TENSIONAL] Council-Led Civic Authority (Zurich) vs. Consistorial Independence from Civil Control (Geneva)",
        "description": "Two cities, two answers.",
    }
    prompt = build_prompt({**REPOSITORY, gravity["id"]: gravity}, REGISTRY_ENTRY).decode("utf-8")
    assert "- [[rzg.gravity.council-led-authority-vs-consistorial-independence]] Council-Led Civic Authority (Zurich) vs. Consistorial Independence from Civil Control (Geneva)" in prompt
    assert "[TENSIONAL]" not in prompt


def test_the_worked_line_tags_the_world_s_own_first_term_and_gravity():
    """The citation contract in the shape segment points to this line, so the
    voice sees the [[id]] form in its own namespace. A world whose
    demonstrations carry no tags (rzg) otherwise had no tagged example."""
    term = {"id": "fix.term.bread", "record_type": "term", "quick_meaning": "Bread, daily."}
    gravity = {"id": "fix.gravity.a-tension", "record_type": "gravity", "name": "A Tension"}
    prompt = build_prompt({**REPOSITORY, term["id"]: term, gravity["id"]: gravity}, REGISTRY_ENTRY).decode("utf-8")
    line = prompt.split("## Our worked line\n\n", 1)[1].split("\n", 1)[0]
    assert line.endswith("[[fix.term.bread]] [[fix.gravity.a-tension]].'")
    assert prompt.index("## Our worked line") < prompt.index(_GROUND_LINE)


def test_a_world_with_no_term_or_gravity_tags_its_first_citable_record():
    prompt = _prompt()
    assert "## Our worked line\n\n'" in prompt and "[[fix.core.fix]].'" in prompt


def test_quote_records_are_not_listed_in_the_prompt():
    """A quote reaches the voice only through the turn's evidence block,
    the one place it can be placed from, so the prompt lists none of them:
    no id and no words."""
    quote = {
        "id": "fix.quote.witness-saying",
        "record_type": "quote",
        "speaker_or_author": "The witness",
        "text": "We did not see him ourselves.",
        "modern_rendering": "We never saw him with our own eyes.",
    }
    prompt = build_prompt({**REPOSITORY, quote["id"]: quote}, REGISTRY_ENTRY).decode("utf-8")
    assert prompt == _prompt()
    assert "fix.quote.witness-saying" not in prompt
    assert "with our own eyes" not in prompt
