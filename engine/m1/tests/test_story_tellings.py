"""The optional story fields for reviewed tellings: heart, events,
telling_short, telling_medium. Real lpc story as the base record."""
import copy

from engine.m1 import gates
from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import load_registry

STORY_ID = "lpc.story.celerinus-writes-to-lucian"


def _story():
    return copy.deepcopy(load_world_records("lpc")[STORY_ID])


def _schema_findings(rec):
    return gates.gate_schema_validation({rec["id"]: rec}, load_fleet_records(), load_registry())


def _narratability(rec):
    return gates.gate_narratability({rec["id"]: rec}, {}, {})


def _with_fields(rec):
    rec["heart"] = "Celerinus pleads for his sister and Lucian grants peace on one condition."
    rec["events"] = [
        {"line": "Celerinus asks Lucian to win peace for his sister", "rests_on": "Ep. XX", "essential": True},
        {"line": "Lucian grants it if each case goes to the bishop", "rests_on": "Ep. XXI", "essential": True},
        {"line": "Numeria and Candida are named in the grant", "rests_on": "Ep. XXI"},
    ]
    rec["telling_short"] = "Celerinus asked Lucian to win peace for his sister. Lucian gave it, if each case went to the bishop."
    rec["telling_medium"] = "Celerinus asked Lucian to win peace for his sister, Numeria and Candida. Lucian gave it, if each case went to the bishop."
    return rec


def test_a_story_with_the_new_fields_validates_and_a_story_without_them_is_unchanged():
    assert not [f for f in _schema_findings(_story()) if "unexpected" in f.lower() or "additional" in f.lower()]
    assert not [f for f in _schema_findings(_with_fields(_story())) if "unexpected" in f.lower() or "additional" in f.lower()]
    assert _narratability(_story()) == []
    assert _narratability(_with_fields(_story())) == []


def test_a_malformed_events_entry_is_rejected_by_the_schema():
    rec = _with_fields(_story())
    rec["events"][0]["unknown"] = 1
    assert any("events" in f for f in _schema_findings(rec))
    rec = _with_fields(_story())
    del rec["events"][1]["rests_on"]
    assert any("events" in f for f in _schema_findings(rec))


def test_an_over_length_telling_is_a_finding():
    rec = _with_fields(_story())
    rec["telling_short"] = " ".join(["Celerinus asked Lucian."] * 40)
    assert any("telling_short runs" in f for f in _narratability(rec))


def test_a_name_the_full_record_never_uses_is_a_finding():
    rec = _with_fields(_story())
    rec["telling_short"] = "Celerinus asked Lucian to win peace for his sister. Then Tertullian wrote back."
    findings = _narratability(rec)
    assert any("'tertullian'" in f for f in findings)


def test_a_number_the_full_record_never_uses_is_a_finding():
    rec = _with_fields(_story())
    rec["telling_medium"] = rec["telling_medium"] + " It was settled in 4000 days."
    assert any("'4000'" in f for f in _narratability(rec))


def test_a_shorter_telling_needs_an_essential_event():
    rec = _with_fields(_story())
    for event in rec["events"]:
        event.pop("essential", None)
    assert any("essential" in f for f in _narratability(rec))
    rec = _with_fields(_story())
    del rec["events"]
    assert any("essential" in f for f in _narratability(rec))


def test_the_new_fields_are_readability_graded_like_telling():
    rec = _with_fields(_story())
    labels = [label for label, _ in gates._readability_checks("story", rec)]
    assert {"telling", "telling_short", "telling_medium", "heart"} <= set(labels)
