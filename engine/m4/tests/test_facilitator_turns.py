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
from engine.m4 import facilitator_turns
from engine.m4.facilitator_turns import SYSTEM_NATURE


def test_door_turn_interpolates_world_name_not_display_name():
    event = facilitator_turns.door_turn(
        representative_name="Marius", world_name="Church and Empire"
    )
    assert event["kind"] == "door"
    assert "Church and Empire" in event["text"]
    assert "Imperial and Juridical Christianity" not in event["text"]


def test_table_door_turn_interpolates_each_seat_world_name():
    seated = [
        {"representative_name": "Theon", "world_name": "Alexandrian Christianity"},
        {"representative_name": "Chloe", "world_name": "The Scattered Households"},
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
    assert "The record itself was checked against the sources when the tradition was built." in SYSTEM_NATURE.text
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


def test_check_in_turn_selects_text_by_reason():
    assert facilitator_turns.check_in_turn()["text"] == facilitator_turns.CHECK_IN.text
    assert facilitator_turns.check_in_turn("general")["text"] == facilitator_turns.CHECK_IN.text
    assert facilitator_turns.check_in_turn("loss_to_suicide")["text"] == facilitator_turns.CHECK_IN_LOSS.text
    assert facilitator_turns.check_in_turn("coercion_by_person")["text"] == facilitator_turns.CHECK_IN_COERCION.text
    assert facilitator_turns.check_in_turn("not_applicable")["text"] == facilitator_turns.CHECK_IN.text
    for reason in ("general", "loss_to_suicide", "coercion_by_person"):
        turn = facilitator_turns.check_in_turn(reason)
        assert turn["kind"] == "safety"
        assert turn["resources_appended"] is False
        assert turn["check_in_reason"] == reason
    assert facilitator_turns.check_in_turn("not_applicable")["check_in_reason"] == "general"
