from engine.m3.selftest import run


def test_stage4_selftest_passes():
    report = run()
    assert report["baseline_clean_fixture"]["pass"], report["baseline_clean_fixture"]
    missed = [d for d in report["defects"] if d["status"] == "MISSED"]
    assert not missed, missed
    assert report["overall_pass"]
    assert len(report["defects"]) == 2, "expected exactly the 2 M3-layer seeded defects"
