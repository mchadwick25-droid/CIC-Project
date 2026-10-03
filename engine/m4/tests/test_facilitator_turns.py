"""Regression coverage for the DOOR/TABLE_DOOR world-name slot (Built-World
Voice Alignment): the words of the facilitator must align with the text
the world has. Callers must feed card_name,
not display_name - see door_turn's own docstring - and every admitted
formation world must actually carry a card_name to feed it, or the
fallback silently reintroduces the exact scholarly-name mismatch this
thread found (e.g. ijc's display_name "Imperial and Juridical
Christianity" vs. its card_name "Church and Empire")."""
from engine.api.wiring import ADMITTED_STATES
from engine.m1.registry import formation_world_keys, load_registry
import pytest
from engine.m4 import facilitator_turns
from engine.m4.facilitator_turns import SYSTEM_NATURE


def test_door_turn_interpolates_world_name_not_display_name():
    event = facilitator_turns.door_turn(
        representative_name="Marius", role_label="Deacon of the Letters", world_name="Church and Empire"
    )
    assert event["kind"] == "door"
    assert "Church and Empire" in event["text"]
    assert "Imperial and Juridical Christianity" not in event["text"]


def test_table_door_turn_interpolates_each_seat_world_name():
    seated = [
        {"representative_name": "Theon", "role_label": "Catechetical Teacher", "world_name": "Alexandrian Christianity"},
        {"representative_name": "Chloe", "role_label": "Household Leader", "world_name": "The Scattered Households"},
    ]
    event = facilitator_turns.table_door_turn(seated)
    assert "Alexandrian Christianity" in event["text"]
    assert "The Scattered Households" in event["text"]


def test_every_admitted_formation_world_has_a_card_name():
    """The card_name-missing fallback in wiring.create_session and
    table_wiring's own seat-building exists only for the fix fixture, which
    has no card_name by design (kind == fixture, never admitted, never
    reachable by a participant). A real, admitted formation world silently
    hitting that fallback would mean the Facilitator quietly reverts to the
    scholarly display_name for that one world - the exact defect this
    thread found and fixed for the other seven."""
    registry = load_registry()
    admitted = [k for k in formation_world_keys(registry) if registry[k].get("state") in ADMITTED_STATES]
    assert admitted  # sanity: the assertion below actually exercises something
    missing = [k for k in admitted if not registry[k].get("card_name")]
    assert missing == []


"""SYSTEM_NATURE's own words are participant-facing honesty text - not
free for a future edit to drift back toward
overclaiming ("checked against the record it came from") without
noticing. Pins the exact middle sentences; an earlier reword shipped
with no such pin, which is how the wording needed a
second correction the same week."""


def test_system_nature_states_the_ruled_verification_sentences():
    assert (
        "Before you see an answer, each claim in it is checked to make sure "
        "its words come from the record it names."
    ) in SYSTEM_NATURE.text
    assert "The record itself was checked against the sources when the world was built." in SYSTEM_NATURE.text
    assert (
        "Where the record is silent, the voice is built to say so, not to fill the gap."
    ) in SYSTEM_NATURE.text


def test_system_nature_does_not_overclaim_truth_verification():
    """The defect this guards against: wording that reads as verifying
    the underlying history, not just the record's own wording."""
    assert "checked against the record it came from" not in SYSTEM_NATURE.text
    assert "every specific claim in it is checked against the record" not in SYSTEM_NATURE.text


def test_table_seat_correction_turn_names_the_seat_and_carries_its_own_kind():
    """The seat-identity guard's fallback line -
    pinned so a future edit can't silently drop the seat's own name or
    drift its kind back onto an existing one ("safety" is a different,
    unrelated situation - TABLE_DEPENDENCY_CHECK's own)."""
    event = facilitator_turns.table_seat_correction_turn("Papnoute")
    assert event["kind"] == "seat_correction"
    assert "Papnoute" in event["text"]
    assert "Facilitator" in event["text"]


def test_voice_rejected_turn_names_the_representative_and_carries_its_own_kind():
    """The uncited-claims enforcement's own interview-mode fallback -
    Option A, chosen for a single-voice interview. Pinned so a future
    edit can't silently drop the
    representative's own name, reuse "seat_correction" (a different,
    identity-impersonation-specific situation), or reintroduce Table-only
    language ("the Table is still open") that makes no sense with one
    voice."""
    event = facilitator_turns.voice_rejected_turn("Vera")
    assert event["kind"] == "grounding_correction"
    assert "Vera" in event["text"]
    assert "Facilitator" in event["text"]
    assert "Table" not in event["text"]


# --- close variants (a sitting whose limit can be lifted) ---

from engine.m4.facilitator_turns import CLOSE_VARIANTS, close_variant_text
from engine.m7.turn_readability import score_turn


def test_every_close_variant_reads_at_the_target_level_and_stays_a_close():
    for name in CLOSE_VARIANTS:
        for text in (close_variant_text(name, "Clement"), close_variant_text(name, None, daily=True)):
            assert score_turn(text).passed, (name, text)
    assert score_turn(facilitator_turns.DAILY_OPEN).passed


def test_variants_fill_the_voice_names_and_leave_no_slot_open():
    assert "Clement" in facilitator_turns.session_cap_turn("Clement", "open")["text"]
    assert "Clement or Papnoute" in facilitator_turns.table_session_cap_turn(["Clement", "Papnoute"], "open")["text"]
    for name in CLOSE_VARIANTS:
        for turn in (
            facilitator_turns.session_cap_turn("Clement", name),
            facilitator_turns.daily_cap_turn(name),
            facilitator_turns.table_session_cap_turn(["Clement", "Papnoute"], name),
        ):
            assert turn["kind"] == "close" and "{" not in turn["text"]


def test_no_variant_leaves_the_default_text_unchanged():
    assert facilitator_turns.session_cap_turn("Clement") == facilitator_turns.session_cap_turn("Clement", None)
    assert facilitator_turns.daily_cap_turn()["text"] == facilitator_turns.DAILY_CAP.text


def test_unknown_variant_is_refused_not_guessed():
    with pytest.raises(KeyError):
        close_variant_text("nonsense", "Clement")
