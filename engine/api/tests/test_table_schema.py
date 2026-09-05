

def test_round_design_subject_world_framed_as_witness():
    """Mark's ruling (2026-08-29): 'make the round design fix, papnoute
    confirms from his own witness'. The ROUND LOOP chooses the frame:
    a voice whose own world the participant named gets the
    witness-confirm stance; every other voice keeps the hearsay rule."""
    from types import SimpleNamespace
    from engine.api.table_wiring import _context_prefix, _own_world_named, _table_engagement_directive

    worlds = {
        "desert": SimpleNamespace(frame={"representative": {"name": "Papnoute"}, "display_name": "Desert Monasticism"}),
        "alx": SimpleNamespace(frame={"representative": {"name": "Theon"}, "display_name": "Alexandrian Christianity"}),
    }
    msg = "Theon, tell me plainly what you know about Papnoute's world and how its people live."
    assert _own_world_named("desert", worlds, msg) is True    # named as subject
    assert _own_world_named("alx", worlds, msg) is False      # leading vocative = addressee, not subject
    assert _own_world_named("desert", worlds, "What do each of you make of fasting?") is False
    # a mid-sentence mention IS the subject even for a voice also addressed
    assert _own_world_named("alx", worlds, "Papnoute, what would Theon's people say to that?") is True
    assert _own_world_named("desert", worlds, "Papnoute, what would Theon's people say to that?") is False

    # The stance/behavioral rule lives in the directive channel since the
    # 2026-09-05 bug fix (engine.m4.turn._build_turn_directive) - _context_prefix
    # now carries only the pending speech itself, identically regardless of
    # who the subject is.
    pending = ["The Participant: " + msg]
    prefix = _context_prefix(pending)
    assert msg in prefix
    assert "you are the witness" not in prefix and "we know only what we have heard at this Table" not in prefix

    subject = _table_engagement_directive(own_world_is_subject=True)
    other = _table_engagement_directive(own_world_is_subject=False)
    assert "you are the witness" in subject and "Confirm or correct" in subject
    assert "we know only what we have heard at this Table" not in subject
    assert "we know only what we have heard at this Table" in other
    assert "you are the witness" not in other
    # shared frame stays identical on both sides
    for text in (subject, other):
        assert "never retell their stories" in text and "Keep this turn compact" in text


def test_round_is_broad_only_at_three_plus_seats_and_never_after_direct_address():
    """Mark's ruling (2026-09-05): the 5-turn minimum applies only to a
    round genuinely addressed to the whole table - never one that opened
    naming one Representative directly, and never a two-seat table, where
    "every seat has spoken" is just the ordinary alternating exchange."""
    from engine.api.table_wiring import _round_is_broad

    three = ["cappadocian", "pahc", "syr"]
    two = ["alx", "desert"]

    assert _round_is_broad(["cappadocian"], three, opened_by_direct_address=False) is False
    assert _round_is_broad(["cappadocian", "pahc"], three, opened_by_direct_address=False) is False
    assert _round_is_broad(["cappadocian", "pahc", "syr"], three, opened_by_direct_address=False) is True
    # order and repeats don't matter, only coverage
    assert _round_is_broad(["syr", "cappadocian", "syr", "pahc"], three, opened_by_direct_address=False) is True
    # a round that opened naming one Representative never qualifies, even
    # if every seat is later heard anyway
    assert _round_is_broad(["cappadocian", "pahc", "syr"], three, opened_by_direct_address=True) is False
    # two seats: "everyone has spoken" is the ordinary case, never broad
    assert _round_is_broad(["alx", "desert"], two, opened_by_direct_address=False) is False
