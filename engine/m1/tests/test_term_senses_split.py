"""The optional term fields that split senses.translational into how a word is heard today and what is meant here."""
import copy

from engine.m1 import gates
from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import load_registry

TERM_ID = "lpc.term.libelli"


def _term():
    return copy.deepcopy(load_world_records("lpc")[TERM_ID])


def _schema_findings(rec):
    return gates.gate_schema_validation({rec["id"]: rec}, load_fleet_records(), load_registry())


def _retrofit(rec):
    return gates.gate_glossary_retrofit_complete({rec["id"]: rec}, {}, {})


def test_a_term_with_both_split_fields_validates_and_a_term_without_them_is_unchanged():
    split = _term()
    split["senses"]["heard_today"] = "A modern listener may picture a formal identity document or licence."
    split["senses"]["meant_here"] = "We mean a compliance certificate that the authorities issued."
    assert not [f for f in _schema_findings(split) if "unexpected" in f.lower() or "additional" in f.lower()]
    assert _retrofit(split) == []
    assert _retrofit(_term()) == []


def test_one_split_field_without_the_other_is_a_finding():
    rec = _term()
    rec["senses"]["heard_today"] = "A modern listener may picture a licence."
    assert any("come as a pair" in f for f in _retrofit(rec))


def test_a_blank_split_field_is_a_finding():
    rec = _term()
    rec["senses"]["heard_today"] = "  "
    rec["senses"]["meant_here"] = "We mean a certificate."
    assert any("senses.heard_today is present and blank" in f for f in _retrofit(rec))


def test_an_unknown_senses_field_is_still_rejected():
    rec = _term()
    rec["senses"]["something_else"] = "x"
    assert any("senses" in f for f in _schema_findings(rec))
