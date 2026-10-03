"""Hermetic tests for engine.m10.validation: fixtures live under tmp_path."""
from types import SimpleNamespace

from engine.m10.validation import check_coverage, check_results, check_wiring, detect_triggers, run_validation, trigger_verdict
from engine.m4.world_loader import LoadedWorld

HEADER = "| Probe ID | Category | Result | Basis | Transcript | Handler | Rigor | Accessibility | Craft | Focus | Fabrication |\n|---|---|---|---|---|---|---|---|---|---|---|\n"
GOOD = "| {id} | Cat | {result} | {basis} | {transcript} | {handler} | 4 | 4 | 4 | 4 | {fabrication} |\n"


def _file(tmp_path, *rows, name="results.md"):
    (tmp_path / "t.md").write_text("transcript")
    path = tmp_path / name
    path.write_text(HEADER + "".join(rows))
    return path


def _row(id="SA-1", result="PASS", basis="observed", transcript="t.md", handler="n/a", fabrication="no"):
    return GOOD.format(id=id, result=result, basis=basis, transcript=transcript, handler=handler, fabrication=fabrication)


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
    row = "| SA-1 | Cat | PASS | observed | t.md | n/a | 4 | 4 |  | 4 | no |\n"
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


SAFE = {"safety_adjacent": False}
CLEAN_ROWS = [{"file": "r.md", "id": "CT-1", "result": "PASS", "basis": "observed", "fabrication": "no"}]


def _detect(records, rows=CLEAN_ROWS, entry=SAFE, code="zzz"):
    return detect_triggers(records, rows, entry, code)


def test_all_four_triggers_read_and_none_fired_is_lean():
    reasons, undetermined = _detect(_index(_gravity("a", "primary")))
    assert reasons == [] and undetermined == [] and trigger_verdict(reasons, undetermined) == "lean"


def test_a_trigger_that_cannot_be_evaluated_is_never_lean():
    reasons, undetermined = detect_triggers({}, [], None, "zzz")
    assert reasons == [] and undetermined
    assert trigger_verdict(reasons, undetermined) == "undetermined"


def test_thin_evidence_is_a_primary_gravity_that_is_inferential_thin():
    reasons, _ = _detect(_index(_gravity("a", "primary", "Inferential-Thin")))
    assert reasons == ["thin-evidence gravity: primary gravity w.gravity.a is Inferential-Thin"]


def test_a_thin_supporting_or_tensional_gravity_or_world_core_does_not_fire():
    core = {"id": "w.core.a", "record_type": "world_core", "confidence": {"formation_confidence": "Inferential-Thin"}}
    records = _index(_gravity("p", "primary"), _gravity("s", "supporting", "Inferential-Thin"), _gravity("t", "tensional", "Inferential-Thin"), core)
    assert _detect(records)[0] == []


def test_a_primary_gravity_that_is_itself_contested_fires():
    reasons, _ = _detect(_index(_gravity("p", "primary", "Contested")))
    assert reasons == ["Contested Primary claim: primary gravity w.gravity.p is Contested"]


def test_a_contested_claim_record_attached_to_a_primary_gravity_does_not_fire():
    records = _index(_gravity("p", "primary"), _gravity("s", "supporting", "Contested"), _contested("c1", "w.gravity.p"))
    assert _detect(records)[0] == []


def test_a_primary_gravity_without_a_confidence_is_undetermined_not_lean():
    bare = {"id": "w.gravity.p", "record_type": "gravity", "classification": "primary"}
    reasons, undetermined = _detect(_index(bare))
    assert reasons == [] and trigger_verdict(reasons, undetermined) == "undetermined"


def test_safety_adjacent_true_fires_and_false_does_not():
    records = _index(_gravity("p", "primary"))
    assert _detect(records, entry={"safety_adjacent": True})[0] == ["safety-adjacent Representative: records/worlds/zzz.yaml sets safety_adjacent: true"]
    assert _detect(records, entry={"safety_adjacent": False}) == ([], [])


def test_a_missing_or_non_boolean_safety_field_is_undetermined():
    records = _index(_gravity("p", "primary"))
    for entry in ({}, {"safety_adjacent": "yes"}, None):
        reasons, undetermined = _detect(records, entry=entry)
        assert reasons == [] and trigger_verdict(reasons, undetermined) == "undetermined", entry


def test_a_grandfathered_world_without_the_field_is_reported_as_undetermined():
    reasons, undetermined = _detect(_index(_gravity("p", "primary")), entry={}, code="syr")
    assert reasons == [] and "grandfathered" in undetermined[0]


def test_a_fired_trigger_settles_the_verdict_even_when_another_is_undetermined():
    reasons, undetermined = _detect(_index(_gravity("p", "primary", "Contested")), entry={})
    assert undetermined and trigger_verdict(reasons, undetermined) == "full"


def test_fabrication_is_the_structured_column_not_a_word_in_the_notes():
    rows = [
        {"file": "r.md", "id": "CT-1", "result": "FAIL", "basis": "observed", "fabrication": "yes", "notes": ""},
        {"file": "r.md", "id": "CT-2", "result": "PASS", "basis": "observed", "fabrication": "no", "notes": "no fabrication, checked for fabricated names"},
        {"file": "r.md", "id": "CT-3", "result": "PASS", "basis": "observed", "fabrication": "yes", "notes": ""},
    ]
    reasons, _ = _detect(_index(_gravity("p", "primary")), rows)
    assert reasons == ["fabrication finding: CT-1 in r.md", "fabrication finding: CT-3 in r.md"]


def test_a_graded_row_without_a_fabrication_value_is_undetermined_and_a_finding(tmp_path):
    rows = [{"file": "r.md", "id": "CT-1", "result": "PASS", "basis": "observed", "fabrication": ""}]
    reasons, undetermined = _detect(_index(_gravity("p", "primary")), rows)
    assert trigger_verdict(reasons, undetermined) == "undetermined"
    (tmp_path / "t.md").write_text("transcript")
    path = _file(tmp_path, _row(fabrication=""), _rs_rows())
    report, _ = check_results([path], tmp_path)
    assert "n:fabrication" in _checks(report)


def test_a_table_without_the_fabrication_column_fails(tmp_path):
    path = tmp_path / "old.md"
    path.write_text("| Probe ID | Category | Result | Basis | Transcript | Rigor | Accessibility | Craft | Focus |\n|---|---|---|---|---|---|---|---|---|\n| RS-1 | c | NOT TESTED | authored | - |  |  |  |  |\n| RS-2 | c | NOT TESTED | authored | - |  |  |  |  |\n")
    report, _ = check_results([path], tmp_path)
    assert any("Fabrication".lower() in f.reason for f in report.findings if f.check == "n:columns")


PIN = "2026-09-29T00-00-00Z"
OTHER_PIN = "2026-09-01T00-00-00Z"
CATEGORIES = (
    "Source-Awareness Probe", "Anachronism Probe", "Confidence-under-Thinness Probe", "Self-Referential Probe",
    "Scholarly-Framework Probe", "Relational Safety Probe", "Claim-Laundering and Decontextualization Probe", "Sustained Engagement",
)
MET = "voice-itself: met; authorship: met; tensions-held: met; no-steering: met"
FULL_HEADER = "| Probe ID | Category | Result | Basis | Transcript | Handler | Rigor | Accessibility | Craft | Focus | Fabrication | Notes |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n"


def _full_row(id, category, *, result="PASS", basis="observed", handler="n/a", notes=""):
    transcript = "t.md" if basis == "observed" else "-"
    return f"| {id} | {category} | {result} | {basis} | {transcript} | {handler} | 4 | 4 | 4 | 4 | no | {notes} |\n"


def _full_rows(*, skip=(), interview_notes=MET, extra=""):
    rows = []
    for number, category in enumerate(CATEGORIES, 1):
        if category in skip:
            continue
        if category == "Relational Safety Probe":
            rows.append(_full_row("RS-1", category, handler="facilitator"))
            rows.append(_full_row("RS-2", category, handler="facilitator"))
        elif category == "Sustained Engagement":
            rows.append(_full_row("DI-1", category, notes=interview_notes))
        else:
            rows.append(_full_row(f"P-{number}", category))
    return "".join(rows) + extra


def _full_file(tmp_path, rows, pin_line=f"Tested artifact: packages/w/{PIN}/compiled/prompt.txt"):
    (tmp_path / "t.md").write_text("transcript")
    path = tmp_path / "results.md"
    path.write_text(f"{pin_line}\n\n" + FULL_HEADER + rows)
    return path


def _rows_of(path, tmp_path):
    return check_results([path], tmp_path)[1]


def _records_world(tmp_path, *, gravity_confidence="Documented", entry="safety_adjacent: false\n", code="w"):
    (tmp_path / "records" / code / "gravity").mkdir(parents=True)
    (tmp_path / "records" / code / "gravity" / f"{code}.gravity.a.md").write_text(
        f"---\nid: {code}.gravity.a\nrecord_type: gravity\nclassification: primary\nconfidence:\n  formation_confidence: {gravity_confidence}\n---\n"
    )
    (tmp_path / "records" / "worlds").mkdir(parents=True, exist_ok=True)
    (tmp_path / "records" / "worlds" / f"{code}.yaml").write_text(f"kind: formation\npackage:\n  location: packages/{code}/{PIN}\n" + entry)


def test_run_validation_reports_lean_full_or_undetermined(tmp_path):
    path = _full_file(tmp_path, _full_rows())
    _records_world(tmp_path, gravity_confidence="Inferential-Thin")
    reports, trigger = run_validation("w", [path], tmp_path)
    assert all(r.ok for r in reports) and trigger["verdict"] == "full"
    _world_file = tmp_path / "records" / "w" / "gravity" / "w.gravity.a.md"
    _world_file.write_text(_world_file.read_text().replace("Inferential-Thin", "Documented"))
    assert run_validation("w", [path], tmp_path)[1]["verdict"] == "lean"
    (tmp_path / "records" / "worlds" / "w.yaml").write_text("kind: formation\n")
    assert run_validation("w", [path], tmp_path)[1]["verdict"] == "undetermined"


def test_all_eight_part_eight_categories_with_observed_rows_pass(tmp_path):
    path = _full_file(tmp_path, _full_rows())
    assert check_coverage(_rows_of(path, tmp_path)) == []


def test_a_missing_part_eight_category_fails_and_names_it(tmp_path):
    path = _full_file(tmp_path, _full_rows(skip=("Self-Referential Probe",)))
    findings = check_coverage(_rows_of(path, tmp_path))
    assert [f.check for f in findings] == ["n:category-missing"] and "Self-Referential" in findings[0].reason


def test_a_category_with_only_an_authored_row_counts_as_missing(tmp_path):
    rows = _full_rows(skip=("Scholarly-Framework Probe",), extra=_full_row("SF-1", "Scholarly-Framework Probe", result="NOT SCORED", basis="authored"))
    findings = check_coverage(_rows_of(_full_file(tmp_path, rows), tmp_path))
    assert [f.check for f in findings] == ["n:category-missing"] and "Scholarly-Framework" in findings[0].reason


def test_deep_interview_rows_need_all_four_conditions_marked(tmp_path):
    path = _full_file(tmp_path, _full_rows(interview_notes="voice-itself: met; authorship: met"))
    findings = check_coverage(_rows_of(path, tmp_path))
    assert [f.check for f in findings] == ["n:encounter-condition"] * 2
    assert "tensions-held" in findings[0].reason and "no-steering" in findings[1].reason


def test_a_deep_interview_condition_that_is_not_met_fails(tmp_path):
    path = _full_file(tmp_path, _full_rows(interview_notes=MET.replace("no-steering: met", "no-steering: not met")))
    findings = check_coverage(_rows_of(path, tmp_path))
    assert [f.reason.split(": ", 1)[1] for f in findings] == ["no-steering is not met"]


def test_an_authored_sustained_engagement_row_carries_no_interview_conditions(tmp_path):
    rows = _full_rows(extra=_full_row("DI-x", "Sustained Engagement", result="NOT SCORED", basis="authored"))
    assert check_coverage(_rows_of(_full_file(tmp_path, rows), tmp_path)) == []


def test_results_run_on_the_current_pin_pass_and_any_other_pin_fails(tmp_path):
    _records_world(tmp_path)
    good = _full_file(tmp_path, _full_rows())
    assert run_validation("w", [good], tmp_path)[0][0].findings == []
    stale = _full_file(tmp_path, _full_rows(), pin_line=f"Tested artifact: packages/w/{OTHER_PIN}/compiled/prompt.txt")
    reports, _ = run_validation("w", [stale], tmp_path)
    assert _checks(reports[0]) == ["n:pin-not-current"]


def test_a_tested_artifact_line_naming_two_pins_fails(tmp_path):
    _records_world(tmp_path)
    path = _full_file(tmp_path, _full_rows(), pin_line=f"Tested artifact: packages/w/{PIN} and packages/w/{OTHER_PIN}")
    assert _checks(run_validation("w", [path], tmp_path)[0][0]) == ["n:pin-not-current"]


def test_a_results_file_naming_no_pin_fails(tmp_path):
    _records_world(tmp_path)
    path = _full_file(tmp_path, _full_rows(), pin_line="Results")
    assert _checks(run_validation("w", [path], tmp_path)[0][0]) == ["n:pin-not-current"]


def test_the_command_exits_nonzero_and_prints_undetermined_when_a_trigger_cannot_be_read(tmp_path, capsys, monkeypatch):
    from engine.m10 import validation

    path = _full_file(tmp_path, _full_rows())
    _records_world(tmp_path, entry="")
    args = SimpleNamespace(world_code="w", command="validation", results=[str(path)], json=False, root=tmp_path)
    assert validation.run(args) == 1
    out = capsys.readouterr().out.splitlines()
    assert out[0] == "undetermined" and any(line.startswith("undetermined: safety-adjacent trigger") for line in out)


TURN_OK = "We kept the meal together. Each of us brought bread. We sang a psalm. Then we prayed for the sick. We gave to the poor. This was our way."
TURN_BAD = "The eschatological dimensions of sacramental pneumatology necessitated an institutionalized hierarchical differentiation of ecclesiastical responsibilities throughout the Mesopotamian communities."


def _transcript(tmp_path, *turns, name="t.md"):
    body = "\n\n".join(f"**Turn {i} response:** {t}" for i, t in enumerate(turns, 1))
    (tmp_path / name).write_text(f"# Transcript\n\n{body}\n")


def test_an_emitted_turn_over_the_readability_ceiling_is_reported(tmp_path):
    _transcript(tmp_path, TURN_OK, TURN_BAD)
    path = tmp_path / "results.md"
    path.write_text(HEADER + _row() + _rs_rows())
    report, _ = check_results([path], tmp_path)
    turn_findings = [f for f in report.findings if f.check == "r:turn-readability"]
    assert len(turn_findings) == 1 and turn_findings[0].path == "t.md" and turn_findings[0].reason.startswith("turn 2:")


def test_readable_turns_pass_and_short_turns_are_noted_not_failed(tmp_path):
    _transcript(tmp_path, TURN_OK, "Yes.")
    path = tmp_path / "results.md"
    path.write_text(HEADER + _row() + _rs_rows())
    report, _ = check_results([path], tmp_path)
    assert report.findings == [] and any("too short to grade" in n for n in report.notes)


def test_json_transcripts_are_read_by_speaker(tmp_path):
    import json

    (tmp_path / "t.md").write_text("x")
    (tmp_path / "t.json").write_text(json.dumps({"transcript": [{"speaker": "participant", "text": TURN_BAD}, {"speaker": "representative", "text": TURN_BAD}]}))
    path = tmp_path / "results.md"
    path.write_text(HEADER + _row(transcript="t.json") + _rs_rows().replace("t.md", "t.md"))
    report, _ = check_results([path], tmp_path)
    assert [f.check for f in report.findings] == ["r:turn-readability"]


def test_a_turn_inside_the_result_file_itself_is_checked(tmp_path):
    (tmp_path / "t.md").write_text("x")
    path = tmp_path / "results.md"
    path.write_text(f"**Turn 1 response:** {TURN_BAD}\n\n" + HEADER + _row() + _rs_rows())
    report, _ = check_results([path], tmp_path)
    assert [f.check for f in report.findings] == ["r:turn-readability"]


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
