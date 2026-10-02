"""Pins the exact staging repro and
the exact live-table-battery repro
(engine/m4/reports/live-table-battery-F1-2026-08-28.json,
L4-no-foreknowledge) as real, real-world-shaped regression cases - not just
synthetic ones a narrower implementation could still pass."""
from engine.m4.seat_identity_guard import find_seat_identity_violation

FACILITATOR = "The Facilitator"
THEON_FULL = "Theon (Alexandrian Christianity)"
THEON_BARE = "Theon"
PAPNOUTE_FULL = "Papnoute (Desert Monasticism)"
PAPNOUTE_BARE = "Papnoute"


def test_catches_the_exact_staging_repro():
    # cic-engine-staging: a Table round (Theon, Papnoute,
    # Chloe; "who is jesus") produced a turn labelled Papnoute whose text
    # began impersonating the Facilitator, then a second seat, mid-turn.
    text = (
        "The Facilitator: Papnoute has already given his witness. Let me bring in someone who hasn't spoken "
        "yet. Theon, you named him the Logos. "
        "Theon (Alexandrian Christianity): In practice, it meant the Word through whom all things were made "
        "took on our flesh - not a lesser god, not a ray of the sun, but the very reason of the Father, now "
        "walking among us."
    )
    # Guarding Papnoute's own turn: Papnoute's own label is never in
    # `labels` (self-labeling is out of scope, see the module docstring) -
    # only the Facilitator and the OTHER two seats.
    labels = [FACILITATOR, THEON_FULL, THEON_BARE, "Chloe (The Scattered Households)", "Chloe"]
    offending = find_seat_identity_violation(text, labels)
    # The Facilitator label opens the text, so it is the first match found
    # - confirms detection fires before any of the impersonated content is
    # ever reached, not only somewhere later in the block.
    assert offending == "The Facilitator:"


def test_catches_the_mid_turn_other_seat_label_in_isolation():
    # The same staging text, but with the leading Facilitator label
    # removed - confirms the SECOND pattern (an other seat's full
    # "Name (World):" label, mid-paragraph) is independently detectable,
    # not just incidentally caught because it happened to follow the first.
    text = (
        "Theon, you named him the Logos. "
        "Theon (Alexandrian Christianity): In practice, it meant the Word through whom all things were made "
        "took on our flesh."
    )
    labels = [FACILITATOR, THEON_FULL, THEON_BARE]
    assert find_seat_identity_violation(text, labels) == "Theon (Alexandrian Christianity):"


def test_catches_the_august_battery_repro_bare_and_full_forms():
    # engine/m4/reports/live-table-battery-F1-2026-08-28.json,
    # L4-no-foreknowledge: Papnoute's own turn opened with its own full
    # label. Out of THIS guard's scope (self-labeling, see module
    # docstring) when Papnoute is the speaker - but the identical shape
    # against ANOTHER seat's label is exactly what this guard exists for,
    # so pin it as a positive case guarding Theon's own turn instead.
    text = "Papnoute (Desert Monasticism): Theon has answered you rightly - he knows only what I have said here."
    labels = [FACILITATOR, PAPNOUTE_FULL, PAPNOUTE_BARE]
    assert find_seat_identity_violation(text, labels) == "Papnoute (Desert Monasticism):"


def test_bare_name_colon_pattern_also_catches():
    text = "Theon: I have never held that view."
    assert find_seat_identity_violation(text, [FACILITATOR, THEON_FULL, THEON_BARE]) == "Theon:"


def test_clean_text_is_not_flagged():
    text = (
        "We watched them. Not counted weeks, not questions memorized - we watched their lives. "
        "Baptism was not a ceremony marking a choice already made."
    )
    assert find_seat_identity_violation(text, [FACILITATOR, THEON_FULL, THEON_BARE]) is None


def test_a_name_or_facilitator_mentioned_in_running_prose_is_not_flagged():
    # The defect is the attributed dialogue-tag SHAPE, not the bare word.
    # A voice is free to talk ABOUT the Facilitator or another seat.
    text = "Theon would say the Facilitator keeps this space honest, and I agree with him on that much."
    assert find_seat_identity_violation(text, [FACILITATOR, THEON_FULL, THEON_BARE]) is None


def test_speakers_own_label_is_never_guarded_against():
    # Self-labeling is a separate, milder,
    # cosmetic defect, out of this guard's scope - callers must never
    # include the speaking voice's own label in `labels`. This test pins
    # that the function itself is agnostic to which labels it's handed and
    # will happily NOT catch a label the caller chose to omit.
    text = "Papnoute (Desert Monasticism): I have kept this discipline for forty years."
    labels = [FACILITATOR, THEON_FULL, THEON_BARE]  # Papnoute's own label deliberately absent
    assert find_seat_identity_violation(text, labels) is None


def test_no_labels_never_flags_anything_the_interview_path_stays_untouched():
    text = "The Facilitator: I am not who I claim to be."
    assert find_seat_identity_violation(text, []) is None
    assert find_seat_identity_violation(text, None) is None


def test_empty_text_is_not_flagged():
    assert find_seat_identity_violation("", [FACILITATOR]) is None
