

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

    subject = _table_engagement_directive(own_world_is_subject=True, is_second_pass=False, is_final_turn=False, num_seats=2)
    other = _table_engagement_directive(own_world_is_subject=False, is_second_pass=False, is_final_turn=False, num_seats=2)
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
    full answer, scoped to the ONE prior speaker the turn selector named
    (points 9-10, made structural the same day - see the next test), never
    a survey of the whole Table."""
    from engine.api.table_wiring import _table_engagement_directive

    first = _table_engagement_directive(own_world_is_subject=False, is_second_pass=False, is_final_turn=False, num_seats=3)
    second = _table_engagement_directive(
        own_world_is_subject=False, is_second_pass=True, is_final_turn=False, num_seats=3, engage_name="Theon"
    )
    assert "Answer the participant first" in first and "real agreement as readily as" in first
    assert "Keep this turn compact" in first
    assert "not another full answer" in second and "go deeper" in second
    assert "not a survey of everyone at the Table" in second
    assert "not concluding here" in second
    assert "Theon" in second
    assert "shorter than your first answer" in second
    # point 10 names BOTH an alignment and a disagreement as legal focuses -
    # independent review, 2026-09-05: the pre-review wording only offered
    # contrast, a real bias toward manufactured disagreement.
    assert "genuine alignment or a genuine contrast" in second
    # the shared frame (no-foreknowledge, never-retell) is identical either way
    for text in (first, second):
        assert "no knowledge of their worlds" in text and "never retell their stories" in text


def test_table_engagement_directive_second_pass_names_its_one_engagement_target():
    """STRUCTURAL FIX, 2026-09-05 (Mark: "i dont want fix on fix, this
    should be a base program than generates this, not after fixes" - after
    a live round closed on a full-table synthesis and a floor-only fix
    would just have moved where the same collision happened). engage_name
    is threaded in from the turn selector's own resolved
    Selection.engages (engine.m4.turn_selector._resolve_engages, which
    always names something on a real second-pass turn) - a return turn
    names ONE voice, never every voice at once, structurally rather than
    by asking nicely."""
    from engine.api.table_wiring import _table_engagement_directive

    named = _table_engagement_directive(
        own_world_is_subject=False, is_second_pass=True, is_final_turn=False, num_seats=3, engage_name="Chloe"
    )
    assert "responds specifically to what Chloe said" in named
    assert "what the other voices said" not in named  # the aggregate framing is gone once a name is known

    # Defensive only - a real second-pass turn always carries a resolved
    # engage_name (turn_selector's own no-immediate-self-repeat invariant
    # guarantees _resolve_engages never returns None there); the directive
    # itself still degrades to the old aggregate framing rather than
    # producing a broken sentence if it somehow arrives without one.
    unnamed = _table_engagement_directive(own_world_is_subject=False, is_second_pass=True, is_final_turn=False, num_seats=3)
    assert "what the other voices said" in unnamed
    assert "not a survey of everyone at the Table" in unnamed


def test_scoped_pending_keeps_participant_facilitator_and_the_engaged_voice_only():
    """Independent review, 2026-09-05, the finding that actually mattered:
    naming one voice in the directive is not structural scoping if the
    turn can still SEE every other voice's full answer regardless -
    _scoped_pending is what makes the other voice's content genuinely
    absent from this turn's context, not merely unmentioned in an
    instruction. table_history_for's own session-memory reconstruction
    (the alternating history pairs) is untouched by this - see the call
    site in _advance_open_round."""
    from engine.api.table_wiring import FACILITATOR_LABEL, PARTICIPANT_LABEL, _scoped_pending

    pending = [
        f"{PARTICIPANT_LABEL}: what is prayer?",
        "Theon (Alexandrian Christianity): the Logos...",
        "Chloe (The House-Churches): a real man...",
        f"{FACILITATOR_LABEL}: a note on register.",
    ]
    scoped = _scoped_pending(pending, keep_labels={PARTICIPANT_LABEL, FACILITATOR_LABEL, "Theon (Alexandrian Christianity)"})
    assert scoped == [
        f"{PARTICIPANT_LABEL}: what is prayer?",
        "Theon (Alexandrian Christianity): the Logos...",
        f"{FACILITATOR_LABEL}: a note on register.",
    ]
    assert not any("Chloe" in line for line in scoped)  # not the engaged voice - genuinely gone


def test_table_engagement_directive_scales_with_seat_count():
    """Point 3: "a little increase of pressure to shorten... as we are now
    sharing with one or two other voices" - singular/plural phrasing only,
    never a different rule; a 2-seat and a 3-seat table get the identical
    instruction shape, just "the other voice" vs "the other voices"."""
    from engine.api.table_wiring import _table_engagement_directive

    two = _table_engagement_directive(own_world_is_subject=False, is_second_pass=False, is_final_turn=False, num_seats=2)
    three = _table_engagement_directive(own_world_is_subject=False, is_second_pass=False, is_final_turn=False, num_seats=3)
    assert "the other voices" not in two  # singular only at a 2-seat table
    assert "the other voice" in two
    assert "the other voices" in three  # plural at a 3-seat table


def test_table_engagement_directive_final_turn_is_not_the_same_set_as_second_pass():
    """Independent review, 2026-09-05 - the sharpest finding: is_final_turn
    and is_second_pass are different sets (a first-time speaker can land on
    the cap-forced last turn; a mid-round second-pass turn is provably not
    final), and conflating them was backwards on both sides - a non-final
    turn falsely claimed the round was ending, and the true final turn (when
    it happened to be some voice's FIRST turn) told it to "leave room" for a
    voice it could never be drawn back to. Only is_final_turn licenses the
    settle-and-hand-off-to-the-participant framing; every other turn - first
    pass or second pass alike - keeps the ordinary "leave room" ending."""
    from engine.api.table_wiring import _table_engagement_directive

    # A first-time speaker landing on the actual final turn: gets the
    # settle/hand-off framing despite is_second_pass=False.
    first_pass_final = _table_engagement_directive(
        own_world_is_subject=False, is_second_pass=False, is_final_turn=True, num_seats=3
    )
    assert "last turn before the participant speaks again" in first_pass_final
    assert "leave the floor open for the participant" in first_pass_final
    # A pre-existing vacuous assertion here (independent review, 2026-09-05)
    # checked for a substring with a semicolon the code never produces -
    # always true regardless of correctness. The real, distinguishing
    # phrase is the non-final ending's own "drawn back in every time" -
    # this genuinely never appears on a final turn.
    assert "drawn back in every time" not in first_pass_final
    assert "Answer the participant first" in first_pass_final  # still a real, full first answer

    # A second-pass turn that is provably NOT the final one: never claims
    # the round is ending.
    second_pass_not_final = _table_engagement_directive(
        own_world_is_subject=False, is_second_pass=True, is_final_turn=False, num_seats=3
    )
    assert "last turn before the participant speaks again" not in second_pass_not_final
    assert "Leave room for the other voices" in second_pass_not_final

    # A second-pass turn that IS the final one: both apply together.
    second_pass_final = _table_engagement_directive(
        own_world_is_subject=False, is_second_pass=True, is_final_turn=True, num_seats=3
    )
    assert "not another full answer" in second_pass_final
    assert "last turn before the participant speaks again" in second_pass_final


def test_table_engagement_directive_subject_second_pass_add_clause_is_scoped():
    """Independent review, 2026-09-05: own_world_is_subject's stance used to
    say "add what you would add" unconditionally - an open invitation that
    directly collided with is_second_pass's own "this turn is not another
    full answer" on the one combination no test exercised. The subject
    stance's own closing clause now respects is_second_pass instead of
    contradicting it."""
    from engine.api.table_wiring import _table_engagement_directive

    first_pass = _table_engagement_directive(own_world_is_subject=True, is_second_pass=False, is_final_turn=False, num_seats=2)
    second_pass = _table_engagement_directive(own_world_is_subject=True, is_second_pass=True, is_final_turn=False, num_seats=2)
    assert "and add what you would add" in first_pass
    assert "and add what you would add" not in second_pass
    assert "not everything, this is still not another full answer" in second_pass


def test_table_engagement_directive_subject_second_pass_names_its_target_without_contradiction():
    """Independent review, 2026-09-05: the one untested combination, and
    the one with a real bug. is_second_pass's own focus text said "never
    a correction of theirs"; the SAME call's subject stance (above) was
    telling the voice to "confirm or correct what has been said of your
    world" - both cannot be true of the same turn. own_world_is_subject
    now gets its own focus branch: no "correction" language to contradict
    stance's own, just which prior statement (engage_name) is in view -
    the confirm-or-correct instruction itself stays in stance, said once."""
    from engine.api.table_wiring import _table_engagement_directive

    text = _table_engagement_directive(
        own_world_is_subject=True, is_second_pass=True, is_final_turn=False, num_seats=3, engage_name="Theon"
    )
    assert "never a correction of theirs" not in text
    assert "Theon" in text
    assert "the one thing most worth confirming or correcting" in text  # stance's own add_clause, untouched
    assert "not a survey of everyone at the Table" in text
    assert "not concluding" in text


def test_table_engagement_directive_forbids_a_fabricated_facilitator_line():
    """BUG FIX, 2026-09-05, found by the first live proof of this design
    (not the deterministic tests): a voice's own generated text opened with
    a fabricated "The Facilitator: ..." line and a "---" separator before
    its real answer - the Facilitator is a separate, code-owned voice
    (engine.m4.facilitator_turns), never something a Representative
    invents. The directive now opens with an explicit prohibition, on
    every pass and every seat count, before the risky "being brought in"
    phrasing that likely triggered it even gets a chance to land."""
    from engine.api.table_wiring import _table_engagement_directive

    for is_second_pass in (False, True):
        for is_final_turn in (False, True):
            text = _table_engagement_directive(
                own_world_is_subject=False, is_second_pass=is_second_pass, is_final_turn=is_final_turn, num_seats=3
            )
            assert "never write a line for the Facilitator" in text
            assert "never narrate your own entrance" in text
            assert "stage direction" in text
            # the prohibition is the first real instruction, ahead of the
            # phrase that likely triggered the fabrication in the live sample
            assert text.index("never write a line for the Facilitator") < text.index("You know the other voices")
