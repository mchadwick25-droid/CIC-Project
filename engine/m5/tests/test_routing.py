from engine.m5.routing import route

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


def _safety(signal="NO_SIGNAL"):
    return {"signal": signal, "acute_level": "none", "dynamic_tags": [], "confidence": "high"}


def test_acute_distress_routes_to_safety_turn():
    decision = route(safety=_safety("ACUTE_DISTRESS"), reader=_reader(), pressed={}, anachronistic_term_ids=set())
    assert decision.action == "safety_turn"


def test_harmful_dynamic_routes_to_safety_turn():
    decision = route(safety=_safety("HARMFUL_DYNAMIC_SIGNAL"), reader=_reader(), pressed={}, anachronistic_term_ids=set())
    assert decision.action == "safety_turn"


def test_safety_takes_priority_over_system_nature():
    decision = route(
        safety=_safety("ACUTE_DISTRESS"),
        reader=_reader(out_of_scope={"class": "system_nature"}),
        pressed={},
        anachronistic_term_ids=set(),
    )
    assert decision.action == "safety_turn"


def test_system_nature_routes_directly():
    decision = route(safety=_safety(), reader=_reader(out_of_scope={"class": "system_nature"}), pressed={}, anachronistic_term_ids=set())
    assert decision.action == "system_nature_turn"


def test_system_nature_takes_priority_over_anachronistic_term():
    decision = route(
        safety=_safety(),
        reader=_reader(out_of_scope={"class": "system_nature"}, modern_terms=[{"term_id": "_fleet.modern.rapture", "display": "rapture"}]),
        pressed={},
        anachronistic_term_ids=ANACHRONISTIC,
    )
    assert decision.action == "system_nature_turn"


def test_anachronistic_modern_term_routes_to_bridge():
    decision = route(
        safety=_safety(),
        reader=_reader(modern_terms=[{"term_id": "_fleet.modern.rapture", "display": "rapture"}]),
        pressed={},
        anachronistic_term_ids=ANACHRONISTIC,
    )
    assert decision.action == "bridge_turn"


def test_non_anachronistic_modern_term_does_not_bridge():
    decision = route(
        safety=_safety(),
        reader=_reader(modern_terms=[{"term_id": "_fleet.modern.trinity", "display": "Trinity"}]),
        pressed={},
        anachronistic_term_ids=ANACHRONISTIC,
    )
    assert decision.action == "voice_with_directive"


def test_later_age_first_ask_passes_to_voice():
    decision = route(safety=_safety(), reader=_reader(out_of_scope={"class": "later_age"}), pressed={"later_age": False}, anachronistic_term_ids=set())
    assert decision.action == "voice_with_directive"
    assert decision.directive is not None


def test_later_age_pressed_routes_etic():
    decision = route(safety=_safety(), reader=_reader(out_of_scope={"class": "later_age"}), pressed={"later_age": True}, anachronistic_term_ids=set())
    assert decision.action == "etic_turn"


def test_other_tradition_pressed_routes_etic():
    decision = route(safety=_safety(), reader=_reader(out_of_scope={"class": "other_tradition"}), pressed={"other_tradition": True}, anachronistic_term_ids=set())
    assert decision.action == "etic_turn"


def test_ordinary_turn_routes_to_voice_with_directive():
    decision = route(safety=_safety(), reader=_reader(), pressed={}, anachronistic_term_ids=set())
    assert decision.action == "voice_with_directive"
    assert decision.directive.asks == [{"order": 1, "text": "who was Jesus"}]
    assert decision.directive.suspend_register_statement_1 is False


def test_personal_wound_suspends_register_statement_1():
    decision = route(safety=_safety(), reader=_reader(register="personal_wound"), pressed={}, anachronistic_term_ids=set())
    assert decision.directive.suspend_register_statement_1 is True
    assert decision.directive.register_note is not None


def test_ambiguity_options_pass_through_directive():
    decision = route(safety=_safety(), reader=_reader(clarity="ambiguous", ambiguity_options=["a", "b"]), pressed={}, anachronistic_term_ids=set())
    assert decision.directive.ambiguity_options == ["a", "b"]


def test_safety_none_still_routes_by_reader_rules():
    """safety=None (call unavailable) must never crash routing - the
    fail-open path in failure.py relies on this."""
    decision = route(safety=None, reader=_reader(out_of_scope={"class": "system_nature"}), pressed={}, anachronistic_term_ids=set())
    assert decision.action == "system_nature_turn"
