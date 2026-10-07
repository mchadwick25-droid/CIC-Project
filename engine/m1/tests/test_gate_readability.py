"""Hermetic tests for engine.m1.gates.gate_readability / gate_readability_fleet:
the facilitator-spoken role (modern_term.modern_sense/distinguishing_claim,
spoken by the Facilitator, never the world's own voice) and the fleet/world
split (fleet_voice and modern_term are fleet records, never
inside any world's own records dict - gate_readability stays world-scoped,
gate_readability_fleet is its dedicated fleet-scoped twin, so fleet content
is graded exactly once rather than once per world)."""
from engine.m1.gates import gate_readability, gate_readability_fleet, gate_readability_floor, gate_readability_floor_fleet


def _dense_text(word_count: int) -> str:
    # Long, multi-syllable words with no punctuation - a low word count
    # made artificially dense enough to clear FK_CEILING regardless of
    # length, the same shape gate_readability's own module comment
    # documents testing against.
    return " ".join(["extraordinarily"] * word_count)


def _simple_text(word_count: int) -> str:
    # Short, one-syllable words with no punctuation - the mirror image of
    # _dense_text above, used to exercise gate_readability_floor's own
    # FK < 8 band rather than the ceiling.
    return " ".join(["cat"] * word_count)


_PLAIN = "This is a short, plain sentence anyone can read without any trouble at all."


def test_gate_readability_never_reads_the_fleet_argument():
    # A dense fleet-only record must NOT be flagged by gate_readability
    # itself - only by gate_readability_fleet. If gate_readability walked
    # `fleet` too, engine/m9/enforce.py's own per-world loop (same fleet
    # dict handed to every world) would score this once per world.
    fleet = {"_fleet.voice.x": {"id": "_fleet.voice.x", "record_type": "fleet_voice", "pronoun_rule": _dense_text(12)}}
    assert gate_readability({}, fleet, {}) == []


def test_gate_readability_fleet_grades_fleet_voice():
    fleet = {"_fleet.voice.x": {"id": "_fleet.voice.x", "record_type": "fleet_voice", "pronoun_rule": _dense_text(12)}}
    findings = gate_readability_fleet(fleet)
    assert any("_fleet.voice.x" in f and "pronoun_rule" in f for f in findings)


def test_gate_readability_fleet_clean_fleet_voice_not_flagged():
    fleet = {"_fleet.voice.x": {"id": "_fleet.voice.x", "record_type": "fleet_voice", "pronoun_rule": _PLAIN}}
    assert gate_readability_fleet(fleet) == []


def test_modern_sense_and_distinguishing_claim_graded_facilitator_spoken():
    fleet = {
        "_fleet.modern.x": {
            "id": "_fleet.modern.x",
            "record_type": "modern_term",
            "modern_sense": _dense_text(12),
            "distinguishing_claim": _dense_text(12),
        }
    }
    findings = gate_readability_fleet(fleet)
    assert any("modern_sense" in f for f in findings)
    assert any("distinguishing_claim" in f for f in findings)


def test_underlying_subject_graded_voice_diet():
    fleet = {"_fleet.modern.x": {"id": "_fleet.modern.x", "record_type": "modern_term", "underlying_subject": _dense_text(12)}}
    findings = gate_readability_fleet(fleet)
    assert any("underlying_subject" in f for f in findings)


def test_display_terms_never_graded_participant_label():
    # display_terms is a short citation-card label (list[str] of terms),
    # not composed prose - never reaches the readability check regardless
    # of content.
    fleet = {
        "_fleet.modern.x": {
            "id": "_fleet.modern.x",
            "record_type": "modern_term",
            "display_terms": [_dense_text(12)],
        }
    }
    assert gate_readability_fleet(fleet) == []


def test_a_clean_modern_term_is_not_flagged():
    fleet = {
        "_fleet.modern.x": {
            "id": "_fleet.modern.x",
            "record_type": "modern_term",
            "modern_sense": _PLAIN,
            "underlying_subject": _PLAIN,
            "distinguishing_claim": _PLAIN,
        }
    }
    assert gate_readability_fleet(fleet) == []


def test_the_real_fleet_modern_trinity_record_is_reachable():
    """The one real modern_term record in the fleet is reachable through
    gate_readability_fleet's own fleet.items() walk, not gate_readability's
    per-world records argument."""
    from engine.m1.loader import load_fleet_records

    fleet = load_fleet_records()
    assert "_fleet.modern.trinity" in fleet
    assert fleet["_fleet.modern.trinity"]["record_type"] == "modern_term"
    # Whatever the current finding count is, it must come from
    # gate_readability_fleet, never from gate_readability itself.
    assert gate_readability({}, fleet, {}) == []


def test_gate_readability_floor_reports_a_sub_8_field_while_the_blocking_gate_stays_clean():
    # A very simple field (short, one-syllable words) scores well below
    # the FK 8 band floor. gate_readability - the CI-blocking gate - must
    # stay clean on it (FK < 8 is not > FK_CEILING, and FRE for text this
    # simple is comfortably >= FRE_FLOOR); gate_readability_floor is the
    # report-only check that actually surfaces it.
    records = {"w.term.x": {"id": "w.term.x", "record_type": "term", "plain_meaning": _simple_text(12)}}
    assert gate_readability(records, {}, {}) == []
    findings = gate_readability_floor(records, {}, {})
    assert any("plain_meaning" in f and "below the band floor" in f for f in findings)


def test_gate_readability_floor_fleet_reports_sub_8_fleet_content():
    fleet = {"_fleet.voice.x": {"id": "_fleet.voice.x", "record_type": "fleet_voice", "pronoun_rule": _simple_text(12)}}
    assert gate_readability_fleet(fleet) == []
    findings = gate_readability_floor_fleet(fleet)
    assert any("pronoun_rule" in f for f in findings)


def test_gate_readability_floor_does_not_flag_text_at_or_above_the_band():
    # _dense_text scores far above FK_CEILING (see gate_readability's own
    # tests above) - nowhere near gate_readability_floor's FK < 8 edge.
    records = {"w.term.x": {"id": "w.term.x", "record_type": "term", "plain_meaning": _dense_text(12)}}
    assert gate_readability_floor(records, {}, {}) == []


def _demonstration(participant_text: str, representative_text: str) -> dict:
    return {
        "x.demo.1": {
            "id": "x.demo.1",
            "record_type": "demonstration",
            "exchange": [
                {"speaker": "participant", "text": participant_text},
                {"speaker": "representative", "text": representative_text},
            ],
        }
    }


def test_participant_turn_is_never_readability_graded():
    # A participant's line is a record of what was said, like quote.text:
    # a dense one fails nothing, and a simple one is not even reported.
    assert gate_readability(_demonstration(_dense_text(12), _PLAIN), {}, {}) == []
    floor = gate_readability_floor(_demonstration(_simple_text(12), _PLAIN), {}, {})
    assert not any("participant" in f for f in floor)


def test_representative_turn_is_still_readability_graded():
    # The world's own turn in the same exchange is graded exactly as before:
    # past the ceiling it fails, under the floor it is reported.
    findings = gate_readability(_demonstration(_PLAIN, _dense_text(12)), {}, {})
    assert findings and all("exchange[representative].text" in f for f in findings)
    floor = gate_readability_floor(_demonstration(_PLAIN, _simple_text(12)), {}, {})
    assert floor and all("exchange[representative].text" in f for f in floor)
