"""Hermetic checks on the R41 battery's scoring rules - no live calls."""
from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import formation_world_keys, load_registry
from engine.m4.reports import r41_modern_word_battery as battery
from engine.m5.anachronism import anachronistic_term_ids

REPLY = "The word “Protestant” you are using is not ours. We gathered at the table on the Lord's day."


def _ok(**fields):
    return {"status": "ok", "reasoning": "", **fields}


def test_verbatim_ignores_case_whitespace_and_curly_quotes():
    assert battery.quote_is_verbatim('the word "Protestant"  you are using', REPLY)
    assert not battery.quote_is_verbatim("Protestants broke with Rome", REPLY)
    assert not battery.quote_is_verbatim("  ", REPLY)


def test_yes_needs_both_runs_and_a_verbatim_quote_for_that_field():
    ev = [{"item": "names_as_participants_word", "quote": "you are using"}]
    grades = [_ok(names_as_participants_word=True, evidence=ev), _ok(names_as_participants_word=True, evidence=[])]
    assert battery.settle(grades, ("names_as_participants_word",), REPLY) == {"names_as_participants_word": "yes"}


def test_evidence_for_another_field_does_not_anchor_a_flag():
    ev = [{"item": "names_as_participants_word", "quote": "you are using"}]
    grades = [_ok(false_mapping=True, evidence=ev)] * 2
    assert battery.settle(grades, ("false_mapping",), REPLY) == {"false_mapping": "unsettled"}


def test_invented_evidence_is_unsettled_not_yes():
    ev = [{"item": "defines_modern_word", "quote": "Protestants broke with Rome"}]
    grades = [_ok(defines_modern_word=True, evidence=ev)] * 2
    assert battery.settle(grades, ("defines_modern_word",), REPLY) == {"defines_modern_word": "unsettled"}


def test_split_vote_or_failed_run_is_unsettled():
    split = [_ok(etic_seam=True, evidence=[]), _ok(etic_seam=False, evidence=[])]
    assert battery.settle(split, ("etic_seam",), REPLY) == {"etic_seam": "unsettled"}
    failed = [_ok(etic_seam=False, evidence=[]), {"status": "timeout"}]
    assert battery.settle(failed, ("etic_seam",), REPLY) == {"etic_seam": "unsettled"}
    assert battery.settle([], ("etic_seam",), REPLY) == {"etic_seam": "unsettled"}


def test_agreed_no_is_no():
    grades = [_ok(dating_claim_outside_record=False, evidence=[])] * 2
    assert battery.settle(grades, ("dating_claim_outside_record",), REPLY) == {"dating_claim_outside_record": "no"}


def test_probe_set_covers_every_real_world_and_only_real_worlds():
    registry = load_registry()
    real = set(formation_world_keys(registry))
    assert set(battery.TEST_PROBES) == real
    assert set(battery.CONTROL_PROBES) == real
    assert all(len(words) == 2 for words in battery.TEST_PROBES.values())
    assert all(w in battery.MODERN_WORDS for words in battery.TEST_PROBES.values() for w in words)


def test_control_words_come_from_each_worlds_own_term_record():
    for world_key, (record_id, word) in battery.CONTROL_PROBES.items():
        record = load_world_records(world_key)[record_id]
        assert record["record_type"] == "term"
        assert word.lower() in str(record["world_word"]).lower()


def test_only_pahc_trinity_needs_the_bridge_bypass():
    registry, fleet = load_registry(), load_fleet_records()
    registered = {w: anachronistic_term_ids(fleet, registry[w]["time_window"]) for w in battery.TEST_PROBES}
    assert {w for w, ids in registered.items() if ids} == {"pahc"}
    assert "Trinity" in battery.TEST_PROBES["pahc"]
