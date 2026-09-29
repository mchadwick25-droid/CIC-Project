"""Hermetic tests for engine.m10.validation: fixtures live under tmp_path."""
from types import SimpleNamespace

from engine.m10.validation import check_results, check_wiring, detect_triggers, run_validation
from engine.m4.world_loader import LoadedWorld

HEADER = "| Probe ID | Category | Result | Basis | Transcript | Handler | Rigor | Accessibility | Craft | Focus |\n|---|---|---|---|---|---|---|---|---|---|\n"
GOOD = "| {id} | Cat | {result} | {basis} | {transcript} | {handler} | 4 | 4 | 4 | 4 |\n"


def _file(tmp_path, *rows, name="results.md"):
    (tmp_path / "t.md").write_text("transcript")
    path = tmp_path / name
    path.write_text(HEADER + "".join(rows))
    return path


def _row(id="SA-1", result="PASS", basis="observed", transcript="t.md", handler="n/a"):
    return GOOD.format(id=id, result=result, basis=basis, transcript=transcript, handler=handler)


def _checks(report):
    return sorted({f.check for f in report.findings})


def _rs_rows():
    return _row("RS-1", "PASS", handler="facilitator") + _row("RS-2", "PASS", handler="facilitator")


def test_a_fully_labeled_and_graded_file_passes(tmp_path):
    (tmp_path / "t.md").write_text("transcript")
    report, rows = check_results([_file(tmp_path, _row(), _rs_rows())], tmp_path)
    assert report.findings == [] and len(rows) == 3


def test_observed_result_needs_a_transcript_that_resolves(tmp_path):
    report, _ = check_results([_file(tmp_path, _row(transcript="missing.md"), _rs_rows())], tmp_path)
    assert _checks(report) == ["m:transcript"]


def test_transcript_anchor_is_ignored_when_resolving(tmp_path):
    (tmp_path / "t.md").write_text("transcript")
    report, _ = check_results([_file(tmp_path, _row(transcript="t.md#turn-3"), _rs_rows())], tmp_path)
    assert report.findings == []


def test_authored_result_cannot_score_pass_or_fail(tmp_path):
    report, _ = check_results([_file(tmp_path, _row(result="PASS", basis="authored", transcript="-"), _rs_rows())], tmp_path)
    assert _checks(report) == ["m:authored-scored"]


def test_authored_result_without_a_score_is_allowed(tmp_path):
    report, _ = check_results([_file(tmp_path, _row(result="NOT SCORED", basis="authored", transcript="-"), _rs_rows())], tmp_path)
    assert report.findings == []


def test_unlabeled_result_fails(tmp_path):
    report, _ = check_results([_file(tmp_path, _row(basis="assumed"), _rs_rows())], tmp_path)
    assert _checks(report) == ["m:basis"]


def test_a_graded_answer_needs_all_four_criteria(tmp_path):
    (tmp_path / "t.md").write_text("transcript")
    row = "| SA-1 | Cat | PASS | observed | t.md | n/a | 4 | 4 |  | 4 |\n"
    report, _ = check_results([_file(tmp_path, row, _rs_rows())], tmp_path)
    assert [f.reason for f in report.findings] == ["SA-1: no Craft grade"]


def test_a_table_without_criterion_columns_fails_once(tmp_path):
    path = tmp_path / "legacy.md"
    path.write_text("| Probe ID | Category | Result |\n|---|---|---|\n| SA-1 | c | PASS |\n| RS-1 | c | NOT TESTED |\n| RS-2 | c | ACCEPTABLE FALLBACK |\n")
    report, _ = check_results([path], tmp_path)
    assert _checks(report) == ["n:columns"] and len(report.findings) == 1


def test_rs2_pass_by_the_representative_is_refused(tmp_path):
    rows = _row("RS-1", "PASS", handler="facilitator") + _row("RS-2", "PASS", handler="representative")
    report, _ = check_results([_file(tmp_path, _row(transcript="t.md"), rows)], tmp_path)
    assert "n:rs2-pass" in _checks(report)


def test_rs2_acceptable_fallback_is_accepted(tmp_path):
    (tmp_path / "t.md").write_text("transcript")
    rows = _row("RS-1", "PASS", handler="facilitator") + _row("RS-2", "ACCEPTABLE FALLBACK", handler="representative")
    report, _ = check_results([_file(tmp_path, _row(), rows)], tmp_path)
    assert report.findings == []


def test_rs1_and_rs2_must_be_separate_rows(tmp_path):
    (tmp_path / "t.md").write_text("transcript")
    report, _ = check_results([_file(tmp_path, _row(), _row("RS-1/RS-2", "PASS", handler="facilitator"))], tmp_path)
    assert {"n:rs-combined", "n:rs-row"} <= set(_checks(report))


def test_a_missing_rs_row_is_reported(tmp_path):
    (tmp_path / "t.md").write_text("transcript")
    report, _ = check_results([_file(tmp_path, _row(), _row("RS-1", "PASS", handler="facilitator"))], tmp_path)
    assert [f.reason for f in report.findings] == ["no separate RS-2 row in any results file"]


def _gravity(slug, classification, confidence="Documented"):
    return {"id": f"w.gravity.{slug}", "record_type": "gravity", "classification": classification, "confidence": {"formation_confidence": confidence}}


def _contested(slug, target, confidence="Contested"):
    return {"id": f"w.contested.{slug}", "record_type": "contested_claim", "confidence": {"formation_confidence": confidence}, "relations": [{"type": "associated-with", "target": target}]}


def _index(*records):
    return {r["id"]: r for r in records}


def test_no_trigger_is_lean_and_names_the_safety_gap():
    reasons, undetermined = detect_triggers(_index(_gravity("a", "primary")), [])
    assert reasons == [] and "safety-adjacent" in undetermined[0]


def test_thin_evidence_gravity_fires():
    reasons, _ = detect_triggers(_index(_gravity("a", "supporting", "Inferential-Thin")), [])
    assert reasons == ["thin-evidence gravity: w.gravity.a (supporting) is Inferential-Thin"]


def test_contested_claim_tied_to_a_primary_gravity_fires_but_not_to_a_supporting_one():
    records = _index(_gravity("p", "primary"), _gravity("s", "supporting"), _contested("c1", "w.gravity.p"), _contested("c2", "w.gravity.s"))
    reasons, _ = detect_triggers(records, [])
    assert len(reasons) == 1 and "w.contested.c1" in reasons[0]


def test_a_primary_gravity_that_is_itself_contested_fires():
    reasons, _ = detect_triggers(_index(_gravity("p", "primary", "Contested")), [])
    assert reasons == ["Contested Primary claim: primary gravity w.gravity.p is Contested"]


def test_fabrication_recorded_in_a_failed_result_fires():
    rows = [{"file": "r.md", "id": "CT-1", "result": "FAIL", "notes": "invented a bishop: fabrication"}, {"file": "r.md", "id": "CT-2", "result": "PASS", "notes": "no fabrication"}]
    reasons, _ = detect_triggers({}, rows)
    assert reasons == ["fabrication finding: CT-1 in r.md"]


def test_run_validation_reports_lean_or_full(tmp_path):
    (tmp_path / "t.md").write_text("transcript")
    path = _file(tmp_path, _row(), _rs_rows())
    (tmp_path / "records" / "w" / "gravity").mkdir(parents=True)
    (tmp_path / "records" / "w" / "gravity" / "w.gravity.a.md").write_text(
        "---\nid: w.gravity.a\nrecord_type: gravity\nclassification: primary\nconfidence:\n  formation_confidence: Inferential-Thin\n---\n"
    )
    reports, trigger = run_validation("w", [path], tmp_path)
    assert all(r.ok for r in reports) and trigger["verdict"] == "full"
    (tmp_path / "records" / "w" / "gravity" / "w.gravity.a.md").unlink()
    assert run_validation("w", [path], tmp_path)[1]["verdict"] == "lean"


def test_no_results_files_is_a_finding(tmp_path):
    reports, _ = run_validation("w", [], tmp_path)
    assert _checks(reports[0]) == ["n:no-results"]


def _world():
    return LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={"records": [{"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."}]},
        quotes={"quotes": []},
        figures={},
        coverage={},
        frame={"representative": {"name": "Vera", "role_label": "Witness"}},
    )


def test_the_handoff_routes_fire_and_the_voice_is_never_called():
    report = check_wiring(_world(), "fixture")
    assert report.findings == [], [f.line() for f in report.findings]


def test_the_wiring_check_fails_when_a_governed_route_calls_the_voice(monkeypatch):
    stub = SimpleNamespace(routing_action="voice_with_directive", facilitator_events=[], voice_event={"text": "x"}, usage_records=[SimpleNamespace(call_kind="voice_call")])
    monkeypatch.setattr("engine.m4.turn.run_turn", lambda **kwargs: stub)
    checks = {f.check for f in check_wiring(_world(), "fixture").findings}
    assert {"o:route", "o:facilitator-turn", "o:voice-called", "o:voice-usage"} <= checks
