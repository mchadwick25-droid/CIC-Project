import copy
import json
import shutil
from pathlib import Path

import pytest

from engine.m1.loader import load_world_records
from engine.m7 import standing_measure as sm

BAND = Path("engine/m7/band/baseline-2026-10-02.json")
REPORTS = Path("engine/m3/reports") / BAND.stem
WORLD = "alx"


def _probe(raw, answer, citations, stop="end_turn"):
    return {
        "probe_id": "p",
        "cell": "c",
        "passed": True,
        "usage": {"input_tokens": 100, "output_tokens": 50,
                  "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0},
        "transcript": {"answer_text": answer, "raw_text": raw, "citations": citations,
                       "stop_reason": stop, "seconds_to_first_text": 1.0, "seconds_total": 5.0},
    }


def _report(probes, manifest="h1"):
    return {
        "run_settings": {"voice_model_id": "m", "seal_hash": "s",
                         "package_manifest_hash": {WORLD: manifest}},
        "worlds": {WORLD: {"per_probe": probes}},
    }


def _real_id():
    return sorted(load_world_records(WORLD))[0]


@pytest.fixture(scope="module")
def fresh_band():
    return sm.compute_band(REPORTS)


def test_stored_band_reproduces(fresh_band):
    assert BAND.exists()
    assert json.loads(BAND.read_text()) == json.loads(sm._dump(fresh_band))


def test_unresolvable_tag_is_invented():
    real = _real_id()
    probe = _probe(f"One. [[{real}]] Two. [[{WORLD}.nope.missing]]", "One. Two.", [real])
    scores = sm.score_run(_report([probe]))
    assert scores["invented_ids_per_100_sentences"] == 50.0


def test_max_tokens_is_cutoff():
    probes = [_probe("A.", "A.", [], stop="max_tokens"), _probe("B.", "B.", [])]
    assert sm.score_run(_report(probes))["cutoff_rate"] == 0.5


def test_tag_absent_from_citations_is_withheld():
    real = sorted(load_world_records(WORLD))[:2]
    probe = _probe(f"A. [[{real[0]}]] B. [[{real[1]}]]", "A. B.", [real[0]])
    assert sm.score_run(_report([probe]))["withheld_mark_rate"] == 0.5


def test_manifest_mismatch_raises(tmp_path):
    probe = _probe("A.", "A.", [])
    for run in (1, 2, 3):
        report = _report([copy.deepcopy(probe)], manifest="h1" if run < 3 else "h2")
        (tmp_path / f"live-admission-report-baseline-r{run}-{WORLD}-2026-10-02.json").write_text(json.dumps(report))
    with pytest.raises(ValueError, match="package_manifest_hash"):
        sm.compute_band(tmp_path)


def test_not_computed_disjoint_from_computed():
    computed = set(sm.DIMENSIONS) | {"distinctness_overlap"}
    assert not computed & set(sm.NOT_COMPUTED)


def test_check_flags_missing_and_stale_band(tmp_path, monkeypatch, fresh_band):
    monkeypatch.setattr(sm, "compute_band", lambda _reports: fresh_band)
    assert sm.main(["check", "--reports", str(REPORTS), "--band", str(BAND)]) == 0
    assert sm.main(["check", "--reports", str(REPORTS), "--band", str(tmp_path / "none.json")]) == 1
    stale = tmp_path / "band.json"
    shutil.copy(BAND, stale)
    stale.write_text(stale.read_text().replace('"pass_rate"', '"pass_rate "', 1))
    assert sm.main(["check", "--reports", str(REPORTS), "--band", str(stale)]) == 1


def test_status_lets_a_lower_is_better_dimension_improve_past_the_band():
    assert sm._status(0.1, 0.2, 0.5, "invented_ids_per_100_sentences") == "better"
    assert sm._status(0.6, 0.2, 0.5, "invented_ids_per_100_sentences") == "out"
    assert sm._status(250, 260, 300, "words_median") == "out"
    assert sm._status(280, 260, 300, "words_median") == "in"


def test_compare_blocks_only_on_a_fleet_mean_outside_the_band(monkeypatch):
    band = json.loads(BAND.read_text())
    reports = [json.loads(p.read_text()) for p in sorted(REPORTS.glob("live-admission-report-baseline-r1-*.json"))]
    result = sm.compare(reports, band)
    assert result["blocking"] == []
    assert set(result["per_world"]) == set(band["worlds"])

    real = sm.score_run
    monkeypatch.setattr(sm, "score_run", lambda r: {**real(r), "words_median": 900.0})
    assert sm.compare(reports, band)["blocking"] == ["words_median"]


def test_a_sentence_withheld_for_a_quotation_counts_in_withheld_mark_rate():
    from engine.m4.turn import apply_net

    first, second = sorted(load_world_records(WORLD))[:2]
    records = {
        first: {"id": first, "record_type": "doctrinal_witness", "text": "We kept the bread together each week."},
        second: {"id": second, "record_type": "doctrinal_witness", "text": "We shared the cup."},
    }
    raw = f'We kept the bread together each week [[{first}]]. He said "a line no record carries" [[{second}]].'
    answer, citations, net = apply_net(raw, repository_records=records, thin_topics=None)
    assert [s["verdict"] for s in net["sentences"]] == ["ok"]
    assert [r["why"] for r in net["reply_shape"]["removed"]] == ["quotation typed by the voice"]
    kept = [rid for c in citations for rid in c["record_ids"]]
    assert kept == [first]
    probe = _probe(raw, answer, kept)
    assert sm.score_run(_report([probe]))["withheld_mark_rate"] == 0.5
