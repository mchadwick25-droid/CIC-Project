

def test_round_design_subject_world_framed_as_witness():
    """Mark's ruling (2026-08-29): 'make the round design fix, papnoute
    confirms from his own witness'. The ROUND LOOP chooses the frame:
    a voice whose own world the participant named gets the
    witness-confirm stance; every other voice keeps the hearsay rule."""
    from types import SimpleNamespace
    from engine.api.table_wiring import _context_prefix, _own_world_named

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

    pending = ["The Participant: " + msg]
    subject = _context_prefix(pending, own_world_is_subject=True)
    other = _context_prefix(pending, own_world_is_subject=False)
    assert "you are the witness" in subject and "Confirm or correct" in subject
    assert "we know only what we have heard at this Table" not in subject
    assert "we know only what we have heard at this Table" in other
    assert "you are the witness" not in other
    # shared frame stays identical on both sides
    for text in (subject, other):
        assert "never retell their stories" in text and "Keep this turn compact" in text
