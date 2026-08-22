from engine.m1.loader import load_world_records
from engine.m3 import harness
from engine.m3.generation import AnswerResult
from engine.m3.selftest import run


def test_stage4_selftest_passes():
    report = run()
    assert report["baseline_clean_fixture"]["pass"], report["baseline_clean_fixture"]
    missed = [d for d in report["defects"] if d["status"] == "MISSED"]
    assert not missed, missed
    assert report["overall_pass"]
    assert len(report["defects"]) == 2, "expected exactly the 2 M3-layer seeded defects"


def test_run_battery_accepts_a_custom_answerer_and_calls_it_per_probe():
    """run_battery's own answerer= param (M4 step 6: wiring a real
    LiveModelAnswerer through the same battery/masking/grading pipeline)
    - proven here with a recording stand-in, not a live model, against the
    real sealed battery and real fixture-world records."""

    class _RecordingAnswerer:
        def __init__(self):
            self.calls = []

        def answer(self, cell, probe_text):
            self.calls.append((cell, probe_text))
            return AnswerResult(text="a fixed answer", citations=[], source_record_id=None, source_record_type=None)

    records = load_world_records("fix")
    answerer = _RecordingAnswerer()
    results = harness.run_battery("fix", records, answerer=answerer)

    assert len(answerer.calls) == len(results) > 0
    assert all(text for _cell, text in answerer.calls)  # the real probe text reached the answerer, not a placeholder
    assert all(r.checks for r in results)  # every probe was actually graded against "a fixed answer"
