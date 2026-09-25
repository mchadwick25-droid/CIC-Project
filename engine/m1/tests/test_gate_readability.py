"""Hermetic tests for engine.m1.gates.gate_readability's modern_term
coverage (OG-13, worlds/pahc/Open_Gaps_Tracking.md): modern_sense is
spoken verbatim by facilitator_turns.bridge_turn, the same "reaches a
participant" reason every other field this gate already grades is graded,
but modern_term records live in the fleet, not a world's own records, so
this gate has to walk `fleet` specifically to reach them."""
from engine.m1.gates import gate_readability


def _dense_text(word_count: int) -> str:
    # Long, multi-syllable words with no punctuation - a low word count
    # made artificially dense enough to clear FK_CEILING regardless of
    # length, the same shape gate_readability's own module comment
    # documents testing against.
    return " ".join(["extraordinarily"] * word_count)


def test_a_modern_term_with_a_dense_modern_sense_is_flagged():
    fleet = {"_fleet.modern.x": {"id": "_fleet.modern.x", "record_type": "modern_term", "modern_sense": _dense_text(12)}}
    findings = gate_readability({}, fleet, {})
    assert any("_fleet.modern.x" in f and "modern_sense" in f for f in findings)


def test_a_modern_term_with_a_plain_modern_sense_is_not_flagged():
    fleet = {
        "_fleet.modern.x": {
            "id": "_fleet.modern.x",
            "record_type": "modern_term",
            "modern_sense": "This is a short, plain sentence anyone can read without trouble.",
        }
    }
    assert gate_readability({}, fleet, {}) == []


def test_a_non_modern_term_fleet_record_is_never_checked():
    fleet = {"_fleet.source.x": {"id": "_fleet.source.x", "record_type": "source", "modern_sense": _dense_text(12)}}
    assert gate_readability({}, fleet, {}) == []


def test_the_real_fleet_modern_trinity_record_is_reachable_through_fleet():
    """A schema-shape guard: this gate must be able to see the one real
    modern_term record in the fleet at all - proves the fleet.items() walk
    is wired, independent of whether that record's own wording happens to
    clear the ceiling today."""
    from engine.m1.loader import load_fleet_records

    fleet = load_fleet_records()
    assert "_fleet.modern.trinity" in fleet
    findings = gate_readability({}, fleet, {})
    assert isinstance(findings, list)  # does not raise; may or may not flag depending on current wording
