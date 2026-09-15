"""The deterministic governance half (C5): dominance's two prongs with the
poc's own thresholds and minimums, the round_closed governance summary
shape, and direct-address detection's conservative cases - each one a case
the poc's S4.4a battery graded live."""
from engine.m4.table_governance import (
    detect_direct_address,
    dominance_signals,
    governance_summary,
)


def _turn(speaker, words):
    return {"speaker": speaker, "text": " ".join(["word"] * words)}


def test_word_share_dominance_fires_at_70():
    transcript = [_turn("alx", 160), _turn("desert", 40)]
    signals = dominance_signals(transcript, ["alx", "desert"])
    assert [s["world_key"] for s in signals] == ["alx"]
    assert signals[0]["basis"] == "word_share" and signals[0]["share"] == 0.8
    assert signals[0]["severity"] == "high"  # >= 0.8


def test_word_share_needs_minimum_and_two_spoken():
    # Below 150 total words: no signal even at 100% share.
    assert dominance_signals([_turn("alx", 100)], ["alx", "desert"]) == []
    # Only one voice has spoken: a share comparison is meaningless.
    assert dominance_signals([_turn("alx", 400)], ["alx", "desert"]) == []


def test_legitimate_asymmetry_below_threshold_is_silent():
    # 65/35 is expected cross-world length asymmetry, not dominance - the
    # poc set the line at 0.70 for exactly this reason.
    transcript = [_turn("alx", 130), _turn("desert", 70)]
    assert dominance_signals(transcript, ["alx", "desert"]) == []


def test_turn_share_prong_fires_only_at_three_seats():
    # One voice selected 4 of 6 turns at a three-seat table: the
    # floor-allocation prong fires even though word share stays moderate.
    transcript = [_turn("alx", 30)] * 4 + [_turn("desert", 30), _turn("pahc", 30)]
    signals = dominance_signals(transcript, ["alx", "desert", "pahc"])
    assert any(s["basis"] == "turn_share" and s["world_key"] == "alx" for s in signals)
    # The identical pattern at a two-seat table stays silent on that prong.
    two_seat = [_turn("alx", 30)] * 4 + [_turn("desert", 30)] * 2
    assert all(s["basis"] != "turn_share" for s in dominance_signals(two_seat, ["alx", "desert"]))


def test_governance_summary_shape():
    transcript = [_turn("alx", 60), _turn("desert", 40)]
    summary = governance_summary(transcript, ["alx", "desert"])
    assert summary["word_share"] == {"alx": 0.6, "desert": 0.4}
    assert summary["turns"] == {"alx": 1, "desert": 1}
    assert summary["dominance_signals"] == []


NAMES = {"Theon": "alx", "Papnoute": "desert", "Chloe": "pahc"}


def test_one_name_routes():
    assert detect_direct_address("Papnoute, what do you do with a restless mind?", NAMES) == "desert"
    assert detect_direct_address("I want to ask theon about the school.", NAMES) == "alx"  # case-insensitive


def test_each_of_you_blocks_the_short_circuit():
    assert detect_direct_address("Theon, and each of you really - what is prayer?", NAMES) is None
    assert detect_direct_address("What do all of you make of fasting?", NAMES) is None


def test_two_names_is_ambiguous():
    # The poc's L3 case: naming both falls through to the selector.
    assert detect_direct_address("Papnoute, ask Theon about his school.", NAMES) is None


def test_no_name_no_partial_match():
    assert detect_direct_address("What is prayer?", NAMES) is None
    # Word boundary: a name embedded in another word never matches.
    assert detect_direct_address("The theonomy question interests me.", NAMES) is None
