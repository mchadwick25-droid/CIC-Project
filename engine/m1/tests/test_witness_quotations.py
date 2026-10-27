"""The witness-quotation gate: every quotation inside a doctrinal witness's
text appears word for word in the vendored source it cites. Offline; no
model call."""
import copy

import pytest

from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import formation_world_keys
from engine.m1.witness_quotations import (
    WITNESS_QUOTATION_MIN_WORDS,
    failing_quotations,
    gate_witness_quotation_verbatim,
    known_findings,
    witness_quotations,
)

WITNESS = "lpc.witness.no-one-may-take-his-own-life"


@pytest.fixture(scope="module")
def fleet():
    return load_fleet_records()


@pytest.fixture(scope="module")
def lpc():
    return load_world_records("lpc")


def _only_witness(records, **fields):
    """The witness, changed, and the source records it names."""
    keep = {WITNESS} | {s["source_id"] for s in records[WITNESS].get("sources") or []}
    changed = copy.deepcopy({rid: r for rid, r in records.items() if rid in keep})
    changed[WITNESS].update(fields)
    return changed


def test_the_real_witness_passes(lpc, fleet):
    assert gate_witness_quotation_verbatim(_only_witness(lpc), fleet, {}) == []
    assert witness_quotations(lpc[WITNESS])


def test_a_seeded_changed_word_in_a_quotation_fails(lpc, fleet):
    text = lpc[WITNESS]["text"].replace("guiltier of his own death", "guiltier of his own demise")
    assert text != lpc[WITNESS]["text"]
    findings = gate_witness_quotation_verbatim(_only_witness(lpc, text=text), fleet, {})
    assert findings == [f"{WITNESS}\tguiltier of his own demise"]


def test_a_seeded_invented_quotation_fails(lpc, fleet):
    text = lpc[WITNESS]["text"] + ' He also wrote, "no one who has pity may ever take a life at all."'
    findings = gate_witness_quotation_verbatim(_only_witness(lpc, text=text), fleet, {})
    assert findings == [f"{WITNESS}\tno one who has pity may ever take a life at all"]


def test_punctuation_a_sentence_puts_inside_the_marks_is_not_part_of_the_quotation(lpc):
    assert "to avoid such disgrace" in witness_quotations(lpc[WITNESS])
    assert "He who kills himself is a homicide" in witness_quotations(lpc[WITNESS])


def test_a_span_shorter_than_the_minimum_is_a_term_and_is_not_checked(lpc, fleet):
    short = '"' + " ".join(["wordx"] * (WITNESS_QUOTATION_MIN_WORDS - 1)) + '"'
    records = _only_witness(lpc, text=lpc[WITNESS]["text"] + f" He used the word {short} once.")
    assert gate_witness_quotation_verbatim(records, fleet, {}) == []


def test_a_record_below_verified_direct_is_skipped_by_the_gate_but_still_fails_the_check(lpc, fleet):
    text = lpc[WITNESS]["text"].replace("guiltier of his own death", "guiltier of his own demise")
    confidence = {**lpc[WITNESS]["confidence"], "verification_state": "verified-via-authority"}
    records = _only_witness(lpc, text=text, confidence=confidence)
    assert gate_witness_quotation_verbatim(records, fleet, {}) == []
    assert failing_quotations(records[WITNESS], records, fleet) == ["guiltier of his own demise"]


def test_a_witness_with_no_resolvable_source_fails_every_quotation(lpc, fleet):
    records = _only_witness(lpc, sources=[], _body="")
    assert gate_witness_quotation_verbatim(records, fleet, {})


def test_the_corpus_has_only_the_known_findings():
    fleet = load_fleet_records()
    found = set()
    for world in formation_world_keys():
        found |= set(gate_witness_quotation_verbatim(load_world_records(world), fleet, {}))
    known = known_findings()
    assert found - known == set(), "a witness quotation that does not verify and is not a known finding"
    assert known - found == set(), "a known finding that now verifies or is gone: remove its line"
