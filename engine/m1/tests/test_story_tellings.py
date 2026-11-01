"""The optional story fields for reviewed tellings: heart, events,
telling_short, telling_medium, telling_long. Real lpc story as the base record."""
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


def _long(rec):
    rec["telling_long"] = "Celerinus asked Lucian to win peace for his sister. Lucian gave it, if each case went to the bishop."
    return rec


def test_a_long_telling_validates_and_has_no_floor():
    rec = _long(_with_fields(_story()))
    assert not [f for f in _schema_findings(rec) if "unexpected" in f.lower() or "additional" in f.lower()]
    assert _narratability(rec) == []
    assert len(rec["telling_long"].split()) < 340


def test_a_long_telling_over_its_ceiling_is_a_finding_and_at_the_ceiling_is_not():
    rec = _long(_with_fields(_story()))
    rec["telling_long"] = " ".join(["Celerinus asked Lucian."] * 205)
    assert len(rec["telling_long"].split()) == 615 and _narratability(rec) == []
    rec["telling_long"] += " Lucian gave it."
    assert any("telling_long runs 618 words, over its ceiling of 615" in f for f in _narratability(rec))


def test_a_long_telling_may_use_a_name_from_the_cited_passage_and_a_shorter_one_may_not():
    rec = _long(_with_fields(_story()))
    record_words = gates._story_vocabulary(rec)
    passage_only = sorted(w for w in gates._story_vocabulary(rec, with_passage=True) - record_words if w.isalpha() and len(w) > 4)
    assert passage_only, "the cited passage must hold words the record does not"
    word = passage_only[0].capitalize()
    rec["telling_long"] = f"Celerinus asked Lucian to win peace for his sister. Then {word} spoke."
    assert not any("telling_long uses" in f for f in _narratability(rec))
    rec["telling_medium"] = f"Celerinus asked Lucian to win peace for his sister. Then {word} spoke."
    assert any(f"telling_medium uses '{word.lower()}'" in f for f in _narratability(rec))


def test_a_name_outside_the_record_and_its_passage_is_a_finding_in_a_long_telling():
    rec = _long(_with_fields(_story()))
    rec["telling_long"] += " Then Tertullian wrote back."
    assert any("telling_long uses 'tertullian'" in f for f in _narratability(rec))
