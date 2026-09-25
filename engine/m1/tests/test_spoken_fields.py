"""The spoken-field registry's own tests.

Two jobs. The first proves the three relocated consumer lists
(gates.ATTRIBUTION_FIELDS, gates.PERSPECTIVE_FIELDS,
cross_world.PARTICIPANT_FIELDS) really did move here unchanged - a pin on
their exact values, so relocating them is provably not also a quiet
behavior change. The second is the actual point of a single registry: every
field name any of those three, or the other four spoken-field-reading sites
this registry consolidates (build_prompt/_chunk_text/build_fleet_preamble in
engine/m2/builders.py, _head_text in engine/m4/evidence.py, the label
helpers in engine/m4/citation_cards.py), is known to read must be declared
here - so a future field added to one of those without being declared is a
failing test, not a silent seventh list.

The builders.py/evidence.py/citation_cards.py field sets below are
enumerated by hand, verified against the actual code on 2026-09-19 - not
walked by an AST scanner. That is a deliberate, disclosed scoping decision:
those three sites are procedural code with meaningful field-emission order
and, for citation_cards.py, real cross-record label derivation, not flat
lookup tables - mechanically parsing arbitrary field-access expressions out
of them is a larger, separate undertaking than this registry's own job
(one declared list, not a sixth or seventh). A hand-enumerated set still
catches the actual failure mode this registry exists to prevent: a field
present in the compiled prompt that gate coverage or a citation card never
learns about, because nobody wrote it down in one place. Extending real
AST enforcement to these three sites is a later, separately-scoped step.
"""
from engine.m1 import cross_world, gates
from engine.m1.spoken_fields import SPOKEN_FIELDS, fields_with_role


def test_attribution_fields_relocated_unchanged():
    assert gates._ATTRIBUTION_FIELDS == {
        "voice_craft": ["identity", "guard"],
        "world_core": ["horizon", "formation_logic", "thinness", "cautions"],
        "term": ["plain_meaning", "quick_meaning", "world_word"],
        "doctrinal_witness": ["text"],
        "honest_limit": ["statement"],
        "story": ["tellable_as", "text"],
        "fleet_voice": ["pronoun_rule", "citation_contract", "limit_discipline"],
    }


def test_perspective_fields_relocated_unchanged():
    assert gates._PERSPECTIVE_FIELDS == {
        "term": ["plain_meaning", "quick_meaning"],
        "story": ["tellable_as", "text"],
        "ambient": ["detail"],
        "doctrinal_witness": ["text"],
        "honest_limit": ["statement"],
    }


def test_participant_fields_relocated_unchanged():
    assert cross_world._PARTICIPANT_FIELDS == {
        "figure": ["bridge_line"],
        "term": ["world_word"],
        "story": ["tellable_as"],
        "gravity": ["name"],
        "force": ["name"],
        "contested_claim": ["claim"],
    }


def _assert_all_declared(consumer_name: str, field_lists: dict[str, list[str]]) -> None:
    for record_type, field_names in field_lists.items():
        declared = SPOKEN_FIELDS.get(record_type, {})
        for field_name in field_names:
            assert field_name in declared, (
                f"{consumer_name} reads {record_type}.{field_name}, "
                f"which engine/m1/spoken_fields.py does not declare"
            )


def test_gates_attribution_fields_are_all_declared():
    _assert_all_declared("gates._ATTRIBUTION_FIELDS", gates._ATTRIBUTION_FIELDS)


def test_gates_perspective_fields_are_all_declared():
    _assert_all_declared("gates._PERSPECTIVE_FIELDS", gates._PERSPECTIVE_FIELDS)


def test_cross_world_participant_fields_are_all_declared():
    _assert_all_declared("cross_world._PARTICIPANT_FIELDS", cross_world._PARTICIPANT_FIELDS)


# Hand-verified against engine/m2/builders.py build_prompt() (voice_craft's
# instruct() calls, world_core/term/doctrinal_witness/honest_limit/gravity/
# quote/story's emit() calls) and build_fleet_preamble() (fleet_voice's own
# six fields), 2026-09-19.
_BUILD_PROMPT_READS = {
    "voice_craft": ["identity", "guard", "characteristic_concerns", "flavor_notes"],
    "world_core": ["horizon", "formation_logic", "thinness", "cautions"],
    "term": ["plain_meaning", "quick_meaning", "world_word"],
    "doctrinal_witness": ["text"],
    "honest_limit": ["statement"],
    "gravity": ["name"],
    "story": ["tellable_as", "text"],
    "demonstration": ["exchange"],
    "fleet_voice": [
        "register_statements", "register_hold", "pronoun_rule",
        "citation_contract", "story_quote_reach", "limit_discipline",
    ],
}

# Hand-verified against engine/m2/builders.py _chunk_text(), 2026-09-19.
_CHUNK_TEXT_READS = {
    "term": ["plain_meaning", "world_word", "quick_meaning"],
    "story": ["tellable_as", "text"],
    "ambient": ["detail"],
    "doctrinal_witness": ["text"],
}

# Hand-verified against engine/m4/evidence.py _head_text(), 2026-09-19.
_HEAD_TEXT_READS = {
    "term": ["plain_meaning"],
    "story": ["tellable_as", "text"],
    "quote": ["modern_rendering", "text"],
    "doctrinal_witness": ["text", "positions"],
    "honest_limit": ["statement"],
    "gravity": ["description"],
    "force": ["description"],
    "contested_claim": ["claim"],
}

# Hand-verified against engine/m4/citation_cards.py's _LABEL_FIELDS and its
# helper functions (_figure_label, _quote_label, _quote_speaker_label),
# 2026-09-19 - the underlying fields those derivations read, not the
# derivation logic itself (see module docstring above).
_CITATION_LABEL_READS = {
    "term": ["world_word"],
    "story": ["tellable_as"],
    "gravity": ["name", "description"],
    "force": ["name", "description"],
    "contested_claim": ["claim"],
    "doctrinal_witness": ["text"],
    "honest_limit": ["statement"],
    "figure": ["names"],
    "quote": ["speaker_or_author", "sources"],
    "source": ["work"],
    "modern_term": ["display_terms"],
}

# Hand-verified against engine/m4/citation_cards.py's resolve_source_card
# modern_term-only enrichment (OG-13, worlds/pahc/Open_Gaps_Tracking.md) -
# carried onto the card verbatim, not derived through _LABEL_FIELDS, so
# tracked as its own read-site rather than folded into the label reads
# above.
_MODERN_TERM_CARD_READS = {
    "modern_term": ["modern_sense", "distinguishing_claim"],
}


def test_build_prompt_reads_are_all_declared():
    _assert_all_declared("builders.build_prompt/build_fleet_preamble", _BUILD_PROMPT_READS)


def test_chunk_text_reads_are_all_declared():
    _assert_all_declared("builders._chunk_text", _CHUNK_TEXT_READS)


def test_head_text_reads_are_all_declared():
    _assert_all_declared("evidence._head_text", _HEAD_TEXT_READS)


def test_citation_label_reads_are_all_declared():
    _assert_all_declared("citation_cards label helpers", _CITATION_LABEL_READS)


def test_modern_term_card_reads_are_all_declared():
    _assert_all_declared("citation_cards.resolve_source_card modern_term enrichment", _MODERN_TERM_CARD_READS)


def test_fields_with_role_filters_correctly():
    assert fields_with_role("story") == ["tellable_as", "text"]
    assert fields_with_role("story", "voice-diet") == ["tellable_as", "text"]
    assert fields_with_role("voice_craft", "instruction") == [
        "identity", "guard", "characteristic_concerns", "flavor_notes",
    ]
    assert fields_with_role("nonexistent-type") == []
    assert fields_with_role("nonexistent-type", "voice-diet") == []
