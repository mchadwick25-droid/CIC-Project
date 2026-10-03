"""engine.m3.admission_conform: an admitted world needs a passing (or ruled)
live admission report on its pinned package hash."""
from engine.m3.admission_conform import check

REG = {"w": {"state": "admitted", "package": {"manifest_hash": "sha256:new"}},
       "b": {"state": "building", "package": {"manifest_hash": "sha256:x"}}}


def _report(h, failed=()):
    return {"path": "r.json", "world": "w", "manifest_hash": h, "pass_count": 28 - len(failed), "battery_size": 28, "failed": sorted(failed)}


def test_a_full_pass_on_the_pinned_hash_conforms():
    assert check(REG, [_report("sha256:new")], []) == []


def test_a_report_on_an_older_package_does_not_count():
    failures = check(REG, [_report("sha256:old")], [])
    assert len(failures) == 1 and "no live admission report" in failures[0]


def test_a_shortfall_needs_a_ruling_on_the_same_hash_and_probes():
    run = _report("sha256:new", failed=["c-t-probe-01"])
    assert "no ruling" in check(REG, [run], [])[0]
    assert check(REG, [run], [{"world": "w", "manifest_hash": "sha256:new", "failing_probes": ["c-t-probe-01"]}]) == []
    assert check(REG, [run], [{"world": "w", "manifest_hash": "sha256:old", "failing_probes": ["c-t-probe-01"]}]) != []
    assert check(REG, [run], [{"world": "w", "manifest_hash": "sha256:new", "failing_probes": ["f1-e-probe-01"]}]) != []


def test_worlds_not_admitted_are_not_checked():
    assert check({"b": REG["b"]}, [], []) == []
