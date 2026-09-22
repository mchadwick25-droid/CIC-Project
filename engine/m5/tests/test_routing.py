from engine.m5.routing import directive_without_terms, route

ANACHRONISTIC = {"_fleet.modern.rapture"}


def _reader(**overrides):
    base = {
        "asks": [{"order": 1, "text": "who was Jesus"}],
        "register": "informational",
        "clarity": "clear",
        "ambiguity_options": [],
        "out_of_scope": {"class": "none"},
        "modern_terms": [],
    }
    base.update(overrides)
    return base


def _safety(signal="NO_SIGNAL", risk_subject="not_applicable"):
    return {"signal": signal, "acute_level": "none", "risk_subject": risk_subject, "dynamic_tags": [], "confidence": "high"}


def test_acute_distress_routes_to_safety_turn():
    decision = route(safety=_safety("ACUTE_DISTRESS"), reader=_reader(), pressed={}, anachronistic_term_ids=set(), message="who was Jesus")
    assert decision.action == "safety_turn"


def test_harmful_dynamic_routes_to_safety_turn():
    decision = route(safety=_safety("HARMFUL_DYNAMIC_SIGNAL"), reader=_reader(), pressed={}, anachronistic_term_ids=set(), message="who was Jesus")
    assert decision.action == "safety_turn"


def test_acute_distress_third_party_still_routes_to_safety_turn_but_reason_records_it():
    """The s12 finding: a participant relaying someone ELSE's crisis must
    still route to the safety turn (routing itself doesn't change), but the
    reason should carry risk_subject through for the safety turn's content
    and the audit trail to use - not silently collapse to 'about the
    participant' the way it did before risk_subject existed."""
    decision = route(
        safety=_safety("ACUTE_DISTRESS", risk_subject="third_party"), reader=_reader(), pressed={}, anachronistic_term_ids=set(),
        message="who was Jesus",
    )
    assert decision.action == "safety_turn"
    assert "third_party" in decision.reason


def test_acute_distress_self_reason_records_it_too():
    decision = route(
        safety=_safety("ACUTE_DISTRESS", risk_subject="self"), reader=_reader(), pressed={}, anachronistic_term_ids=set(),
        message="who was Jesus",
    )
    assert decision.action == "safety_turn"
    assert "risk_subject=self" in decision.reason


def test_safety_takes_priority_over_system_nature():
    decision = route(
        safety=_safety("ACUTE_DISTRESS"),
        reader=_reader(out_of_scope={"class": "system_nature"}),
        pressed={},
        anachronistic_term_ids=set(),
        message="are you an AI?",
    )
    assert decision.action == "safety_turn"


def test_ambiguous_low_confidence_routes_to_check_in_turn():
    decision = route(safety=_safety("AMBIGUOUS_LOW_CONFIDENCE"), reader=_reader(), pressed={}, anachronistic_term_ids=set(), message="who was Jesus")
    assert decision.action == "check_in_turn"


def test_ambiguous_low_confidence_takes_priority_over_system_nature():
    """The real gap live batch 2 (scenario s9) surfaced: a hypothetical-
    framed disclosure read as AMBIGUOUS_LOW_CONFIDENCE by safety and as a
    system_nature question by the reader must still get the check-in, not
    fall through to the system_nature answer."""
    decision = route(
        safety=_safety("AMBIGUOUS_LOW_CONFIDENCE"),
        reader=_reader(out_of_scope={"class": "system_nature"}),
        pressed={},
        anachronistic_term_ids=set(),
        message="are you an AI?",
    )
    assert decision.action == "check_in_turn"


def test_acute_signal_still_outranks_ambiguous_low_confidence():
    decision = route(safety=_safety("ACUTE_DISTRESS"), reader=_reader(), pressed={}, anachronistic_term_ids=set(), message="who was Jesus")
    assert decision.action == "safety_turn"


def test_system_nature_routes_directly():
    decision = route(
        safety=_safety(), reader=_reader(out_of_scope={"class": "system_nature"}), pressed={}, anachronistic_term_ids=set(),
        message="are you an AI?",
    )
    assert decision.action == "system_nature_turn"


def test_system_nature_takes_priority_over_anachronistic_term():
    decision = route(
        safety=_safety(),
        reader=_reader(out_of_scope={"class": "system_nature"}, modern_terms=[{"term_id": "_fleet.modern.rapture", "display": "rapture"}]),
        pressed={},
        anachronistic_term_ids=ANACHRONISTIC,
        message="are you an AI?",
    )
    assert decision.action == "system_nature_turn"


def test_anachronistic_modern_term_routes_to_bridge():
    decision = route(
        safety=_safety(),
        reader=_reader(modern_terms=[{"term_id": "_fleet.modern.rapture", "display": "rapture"}]),
        pressed={},
        anachronistic_term_ids=ANACHRONISTIC,
        message="did you believe in the rapture",
    )
    assert decision.action == "bridge_turn"


def test_non_anachronistic_modern_term_does_not_bridge():
    decision = route(
        safety=_safety(),
        reader=_reader(modern_terms=[{"term_id": "_fleet.modern.trinity", "display": "Trinity"}]),
        pressed={},
        anachronistic_term_ids=ANACHRONISTIC,
        message="did you believe in the Trinity",
    )
    assert decision.action == "voice_with_directive"


def test_later_age_first_ask_passes_to_voice():
    decision = route(
        safety=_safety(), reader=_reader(out_of_scope={"class": "later_age"}), pressed={"later_age": False}, anachronistic_term_ids=set(),
        message="what happened after your own time",
    )
    assert decision.action == "voice_with_directive"
    assert decision.directive is not None


def test_other_tradition_first_ask_carries_the_structured_class_r26():
    # Decision-Log.md Entry 50/51 (R26): a structured field, not a reason
    # string to parse, so engine.m4.turn can wire its own directive
    # addition onto exactly this case without matching free text.
    decision = route(
        safety=_safety(), reader=_reader(out_of_scope={"class": "other_tradition"}), pressed={"other_tradition": False}, anachronistic_term_ids=set(),
        message="what was your relationship with the donatists",
    )
    assert decision.action == "voice_with_directive"
    assert decision.out_of_scope_class == "other_tradition"


def test_ordinary_turn_carries_no_out_of_scope_class():
    decision = route(
        safety=_safety(), reader=_reader(), pressed={}, anachronistic_term_ids=set(),
        message="what did you eat most days",
    )
    assert decision.out_of_scope_class is None


def test_later_age_pressed_routes_etic():
    decision = route(
        safety=_safety(), reader=_reader(out_of_scope={"class": "later_age"}), pressed={"later_age": True}, anachronistic_term_ids=set(),
        message="what happened after your own time",
    )
    assert decision.action == "etic_turn"


def test_other_tradition_pressed_routes_etic():
    decision = route(
        safety=_safety(), reader=_reader(out_of_scope={"class": "other_tradition"}), pressed={"other_tradition": True}, anachronistic_term_ids=set(),
        message="what did another tradition believe",
    )
    assert decision.action == "etic_turn"


def test_ordinary_turn_routes_to_voice_with_directive():
    decision = route(safety=_safety(), reader=_reader(), pressed={}, anachronistic_term_ids=set(), message="who was Jesus")
    assert decision.action == "voice_with_directive"
    assert decision.directive.asks == [{"order": 1, "text": "who was Jesus"}]
    assert decision.directive.suspend_register_statement_1 is False


def test_personal_wound_suspends_register_statement_1():
    decision = route(safety=_safety(), reader=_reader(register="personal_wound"), pressed={}, anachronistic_term_ids=set(), message="who was Jesus")
    assert decision.directive.suspend_register_statement_1 is True
    assert decision.directive.register_note is not None


def test_ambiguity_options_pass_through_directive():
    decision = route(
        safety=_safety(), reader=_reader(clarity="ambiguous", ambiguity_options=["a", "b"]), pressed={}, anachronistic_term_ids=set(),
        message="who was Jesus",
    )
    assert decision.directive.ambiguity_options == ["a", "b"]


def test_safety_none_still_routes_by_reader_rules():
    """safety=None (call unavailable) must never crash routing - the
    fail-open path in failure.py relies on this."""
    decision = route(
        safety=None, reader=_reader(out_of_scope={"class": "system_nature"}), pressed={}, anachronistic_term_ids=set(),
        message="are you an AI?",
    )
    assert decision.action == "system_nature_turn"


# B-2 (witt go-live adversarial review, 2026-09-19): the reader claimed
# system_nature for "What exactly did your founder write in his 1543 book
# about Jewish people?" - a message that names no system, bot, script, or
# "how were you built" shape at all. These are the reproduction and the
# regression coverage for the deterministic backstop that now catches it.

def test_system_nature_claim_is_not_trusted_without_the_words_for_it():
    """The exact B-2 reproduction: an ordinary in-window historical
    question, reader-misclassified as system_nature, must fall through to
    ordinary routing rather than being trusted at face value."""
    decision = route(
        safety=_safety(),
        reader=_reader(out_of_scope={"class": "system_nature"}),
        pressed={},
        anachronistic_term_ids=set(),
        message="What exactly did your founder write in his 1543 book about Jewish people?",
    )
    assert decision.action == "voice_with_directive"
    assert decision.action != "system_nature_turn"


def test_the_readers_own_four_canonical_examples_all_still_route_correctly():
    """live_calls.py's own READER_SYSTEM_PROMPT names these four exact
    phrasings as what system_nature means. The backstop must not break any
    of them."""
    for message in ("are you an AI?", "is this a bot?", "how were you built?", "is this real or a script?"):
        decision = route(
            safety=_safety(), reader=_reader(out_of_scope={"class": "system_nature"}), pressed={}, anachronistic_term_ids=set(),
            message=message,
        )
        assert decision.action == "system_nature_turn", f"{message!r} should still route to system_nature_turn"


def test_an_unrelated_biblical_place_name_does_not_falsely_pass_the_check():
    """Ai (Joshua 7-8) is a real place name this fleet's own worlds may
    discuss. The backstop deliberately excludes a bare 'ai' token from its
    own word list for this reason - confirm a message about it, even if
    (hypothetically) misclassified system_nature, is not waved through on
    the strength of that collision."""
    decision = route(
        safety=_safety(),
        reader=_reader(out_of_scope={"class": "system_nature"}),
        pressed={},
        anachronistic_term_ids=set(),
        message="What happened at Ai when Joshua's forces attacked it?",
    )
    assert decision.action != "system_nature_turn"


def test_a_message_with_no_question_shape_does_not_pass_even_with_a_trigger_word():
    """The backstop requires the reader's own question SHAPE (are/is/were/
    was ... you/this ... [word]), not a bare word anywhere in the message -
    'real' and 'built' are common in ordinary historical-theological
    content and must not trip the check on their own."""
    decision = route(
        safety=_safety(),
        reader=_reader(out_of_scope={"class": "system_nature"}),
        pressed={},
        anachronistic_term_ids=set(),
        message="Was the temple really built the way the old accounts describe?",
    )
    assert decision.action != "system_nature_turn"


def test_a_bridged_turn_keeps_the_ask_that_does_not_carry_the_word():
    """A participant who asked two things in one sentence used to lose the
    second one entirely: the bridge route carries no directive, so the voice
    got the underlying subject alone."""
    directive = directive_without_terms(
        _reader(asks=[
            {"order": 1, "text": "did you argue about the Trinity"},
            {"order": 2, "text": "did you argue about who should lead"},
        ]),
        ["Trinity", "Trinitarian"],
    )
    assert directive is not None
    assert [a["order"] for a in directive.asks] == [2]


def test_every_authored_spelling_is_barred_not_just_the_matched_one():
    """The reader records the one spelling it saw; the record lists them
    all. Barring only the matched one would let a second inflection through
    to the voice, which is the thing SS77 forbids."""
    directive = directive_without_terms(
        _reader(asks=[
            {"order": 1, "text": "what did Trinitarian language mean to you"},
            {"order": 2, "text": "who led your gatherings"},
        ]),
        ["Trinity", "Trinitarian"],
    )
    assert [a["order"] for a in directive.asks] == [2]


def test_an_ambiguity_reading_carrying_the_word_is_dropped_too():
    directive = directive_without_terms(
        _reader(asks=
            [{"order": 1, "text": "who led your gatherings"}],
            clarity="ambiguous",
            ambiguity_options=["whether they meant the Trinity", "whether they meant the elders"],
        ),
        ["Trinity"],
    )
    assert directive.ambiguity_options == ["whether they meant the elders"]


def test_a_single_bridged_ask_leaves_no_directive_at_all():
    """The ordinary bridge. The voice gets exactly the underlying subject it
    got before - not a directive announcing it has no asks."""
    assert directive_without_terms(
        _reader(asks=[{"order": 1, "text": "did you believe in the Trinity"}]),
        ["Trinity"],
    ) is None
