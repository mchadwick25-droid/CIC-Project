"""Regression coverage for the DOOR/TABLE_DOOR world-name slot (Built-World
Voice Alignment, 2026-09-17, Mark's ruling: "the words of the facilitator
should align with the text the world has"). Callers must feed card_name,
not display_name - see door_turn's own docstring - and every admitted
formation world must actually carry a card_name to feed it, or the
fallback silently reintroduces the exact scholarly-name mismatch this
thread found (e.g. ijc's display_name "Imperial and Juridical
Christianity" vs. its card_name "Church and Empire")."""
from engine.api.wiring import ADMITTED_STATES
from engine.m1.registry import formation_world_keys, load_registry
from engine.m4 import facilitator_turns


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
