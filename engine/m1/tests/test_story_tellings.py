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
    rec.pop("telling_long", None)
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


def test_the_cited_passage_leaves_out_the_editors_notes_and_markup():
    rec = _long(_with_fields(_story()))
    passage = gates._cited_passage(rec)
    assert "<" not in passage and "</note>" not in passage
    assert "250" not in gates._story_vocabulary(rec, with_passage=True) - gates._story_vocabulary(rec)


def test_a_cited_span_that_does_not_resolve_is_reported_for_a_long_telling():
    rec = _long(_with_fields(_story()))
    rec["sources"] = [{"source_id": "lpc.source.cyprian-epistles", "locus": "cic/texts/no_such_file.xml, lines 1-5; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 9999999-99999999; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 20-10"}]
    texts, unresolved = gates._cited_spans(rec)
    assert texts == [] and len(unresolved) == 3
    assert sum("does not resolve" in f for f in _narratability(rec)) == 3


def test_a_story_with_no_long_telling_is_not_checked_for_unresolved_spans():
    rec = _with_fields(_story())
    rec["sources"] = [{"source_id": "lpc.source.cyprian-epistles", "locus": "cic/texts/no_such_file.xml, lines 1-5"}]
    assert not any("does not resolve" in f for f in _narratability(rec))


def test_a_long_telling_may_use_a_name_from_any_cited_source_not_the_first_only():
    rec = copy.deepcopy(load_world_records("lpc")["lpc.story.the-death-of-cyprian"])
    first, second = rec["sources"][0], rec["sources"][1]
    texts = {}
    for label, source in (("first", first), ("second", second)):
        solo = {**rec, "sources": [source]}
        texts[label] = set(gates._story_vocabulary(solo, with_passage=True)) - gates._story_vocabulary(rec)
    only_second = sorted(w for w in texts["second"] - texts["first"] if w.isalpha() and len(w) > 4)
    assert only_second, "the second cited source must hold words the first and the record do not"
    word = only_second[0].capitalize()
    rec["telling_long"] = f"Cyprian was executed. Then {word} spoke."
    rec["events"] = [{"line": "Cyprian is executed", "rests_on": "Acta", "essential": True}]
    assert not any("telling_long uses" in f for f in _narratability(rec))
    rec["sources"] = [first]
    assert any(f"telling_long uses '{word.lower()}'" in f for f in _narratability(rec))


def _readability(rec):
    return gates.gate_readability({rec["id"]: rec}, {}, {})


def _floor(rec):
    return gates.gate_readability_floor({rec["id"]: rec}, {}, {})


def test_a_telling_at_grade_seven_is_not_reported_and_one_below_seven_is_reported_and_never_failed():
    rec = _long(_with_fields(_story()))
    seven = "Celerinus wrote to Lucian from his prison cell and asked for peace for his sister, who had fallen away from the church. Lucian agreed, but only if each case went before the bishop first."
    very_plain = "He ran to the town. The man was kind. He gave her a loaf. She said thanks to him. They sat down to eat. It was a good day for all of them."
    assert gates.STORY_TELLING_FK_FLOOR <= gates.grade_text(seven)["fk"] < gates.FK_FLOOR
    assert gates.grade_text(very_plain)["fk"] < gates.STORY_TELLING_FK_FLOOR
    rec["telling_long"] = seven
    assert not any("telling_long" in f for f in _floor(rec)) and not any("telling_long" in f for f in _readability(rec))
    rec["telling_long"] = very_plain
    assert gates.grade_text(very_plain)["fre"] >= gates.FRE_FLOOR
    assert any("telling_long" in f and "story-telling floor of 7 (reported, not failed)" in f for f in _floor(rec))
    assert not any("telling_long" in f for f in _readability(rec))


def test_other_fields_keep_the_band_floor_of_eight():
    term = {"id": "w.term.x", "record_type": "term", "plain_meaning": "He ran to the town. The man was kind. He gave her a loaf. She said thanks to him. They sat down to eat."}
    assert any("below the band floor of 8" in f for f in gates._floor_observations([("w.term.x", term)]))


def test_a_telling_below_the_ease_floor_still_fails():
    rec = _long(_with_fields(_story()))
    rec["telling_long"] = ("The consideration of administrative responsibilities necessitated considerable "
                           "deliberation regarding ecclesiastical jurisdiction and institutional accountability.")
    assert gates.grade_text(rec["telling_long"])["fre"] < gates.FRE_FLOOR
    assert any("telling_long scores FRE" in f for f in _readability(rec))
