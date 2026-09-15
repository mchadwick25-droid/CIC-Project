from engine.m9.selftest import run


def test_m9_selftest_passes():
    report = run()
    assert not report["baseline_clean_fixture"]["findings_by_check"], report["baseline_clean_fixture"]
    missed = [r for r in report["defects"] if r.get("status") == "MISSED"]
    assert not missed, missed
    assert report["inertness"]["pass"], report["inertness"]
    assert report["overall_pass"]
