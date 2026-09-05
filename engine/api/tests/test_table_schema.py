

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

    subject = _table_engagement_directive(own_world_is_subject=True, is_second_pass=False, num_seats=2)
    other = _table_engagement_directive(own_world_is_subject=False, is_second_pass=False, num_seats=2)
    assert "you are the witness" in subject and "Confirm or correct" in subject
    assert "we know only what we have heard at this Table" not in subject
    assert "we know only what we have heard at this Table" in other
    assert "you are the witness" not in other
    # shared frame stays identical on both sides
    for text in (subject, other):
        assert "never retell their stories" in text and "Keep this turn compact" in text


def test_table_engagement_directive_first_pass_vs_second_pass():
    """Mark's ruling (2026-09-05, design enhancement): a voice's first turn
    in a round answers and engages what's come before (points 6-8, naming
    agreement as readily as difference); a later turn in the SAME round
    is a different instruction entirely - depth or contrast, not another
    full answer, and no obligation to touch every other voice (points 9-10)."""
    from engine.api.table_wiring import _table_engagement_directive

    first = _table_engagement_directive(own_world_is_subject=False, is_second_pass=False, num_seats=3)
    second = _table_engagement_directive(own_world_is_subject=False, is_second_pass=True, num_seats=3)
    assert "engage what" in first and "real agreement as readily as" in first
    assert "Keep this turn compact" in first
    assert "not another full answer" in second and "Go deeper" in second
    assert "do not have to touch everything" in second
    assert "shorter than your first answer" in second
    # the shared frame (no-foreknowledge, never-retell) is identical either way
    for text in (first, second):
        assert "no knowledge of their worlds" in text and "never retell their stories" in text


def test_table_engagement_directive_scales_with_seat_count():
    """Point 3: "a little increase of pressure to shorten... as we are now
    sharing with one or two other voices" - singular/plural phrasing only,
    never a different rule; a 2-seat and a 3-seat table get the identical
    instruction shape, just "the other voice" vs "the other voices"."""
    from engine.api.table_wiring import _table_engagement_directive

    two = _table_engagement_directive(own_world_is_subject=False, is_second_pass=False, num_seats=2)
    three = _table_engagement_directive(own_world_is_subject=False, is_second_pass=False, num_seats=3)
    assert "the other voices" not in two  # singular only at a 2-seat table
    assert "the other voice" in two
    assert "the other voices" in three  # plural at a 3-seat table
