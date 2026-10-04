"""The use-note gates: every voiced citable record carries a note, and a note
is one descriptive sentence of meaning, at most four not-for claims, and
years that end inside the world's window."""
from engine.m1 import gates

REG = {"w": {"world_id": "w-world", "time_window": {"start": 100, "end": 300}}}


def _rec(record_type="term", note=None, voice=None):
    r = {"record_type": record_type, "world_id": "w-world"}
    if note is not None:
        r["use_note"] = note
    if voice:
        r["voice"] = voice
    return r


def _note(**over):
    return {"means": "The word names the community's shared way of life.", "not_for": ["a formal creed"],
            "years": {"from": 150, "to": 250}, "status": "provisional", **over}


def test_a_voiced_citable_record_without_a_note_fails_and_others_are_exempt():
    records = {"w.term.a": _rec(), "w.figure.b": _rec("figure"), "w.term.c": _rec(voice="analytic"), "w.term.d": _rec(note=_note())}
    assert [f.split(":")[0] for f in gates.gate_use_note_present(records, {}, REG)] == ["w.term.a"]


def test_a_well_formed_note_passes():
    assert gates.gate_use_note_shape({"w.term.a": _rec(note=_note())}, {}, REG) == []


def test_two_sentences_of_meaning_fail():
    [f] = gates.gate_use_note_shape({"w.term.a": _rec(note=_note(means="It names a way. It is old."))}, {}, REG)
    assert "2 sentences" in f


def test_an_instruction_in_the_meaning_or_a_not_for_line_fails():
    found = gates.gate_use_note_shape({"w.term.a": _rec(note=_note(means="Use this for questions about practice.", not_for=["Never cite it for doctrine"]))}, {}, REG)
    assert len(found) == 2 and all("instruction" in f for f in found)


def test_years_ending_after_the_window_or_running_backward_fail():
    late = gates.gate_use_note_shape({"w.term.a": _rec(note=_note(years={"from": 200, "to": 450}))}, {}, REG)
    backward = gates.gate_use_note_shape({"w.term.a": _rec(note=_note(years={"from": 250, "to": 150}))}, {}, REG)
    assert "after the world's window" in late[0]
    assert "backward" in backward[0]
