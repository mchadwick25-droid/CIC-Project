from engine.m10.handoff import Deps, run_handoff, step_documents

from .fixture_world import CODE, SLUG, TEXT_FILE, build_world, quiet_deps, review_text, write


def _run(root, deps=None, **kw):
    return {r.name: r for r in run_handoff(CODE, deps or quiet_deps(root), **kw)}


def _failing(reports):
    return {name for name, r in reports.items() if r.findings}


def test_complete_world_passes_all_twelve(tmp_path):
    root = build_world(tmp_path)
    reports = _run(root)
    assert len(reports) == 12
    assert _failing(reports) == set(), [f.line() for r in reports.values() for f in r.findings]


def test_step_documents_found_by_real_naming(tmp_path):
    root = build_world(tmp_path)
    docs = step_documents(CODE, root)
    assert {k: v.name for k, v in docs.items()} == {
        0: "Step0_Movement_Scope_Confirmation.md",
        1: "Doc_01_World_Identification.md",
        2: "Doc_02_Source_Ecology.md",
    }


def test_01_missing_registry_entry_or_world_id(tmp_path):
    root = build_world(tmp_path)
    (root / f"records/worlds/{CODE}.yaml").unlink()
    assert "handoff-01-identity" in _failing(_run(root))
    write(root, f"records/worlds/{CODE}.yaml", "kind: formation\ncensus_id: x\n")
    assert "handoff-01-identity" in _failing(_run(root))


def test_01_record_with_a_different_world_id(tmp_path):
    root = build_world(tmp_path)
    write(root, f"records/{CODE}/quote/{CODE}.quote.a.md", "---\nid: fx.quote.a\nworld_id: other-world\n---\n")
    assert "handoff-01-identity" in _failing(_run(root))


def test_02_step0_missing_uncleared_or_census_unchecked(tmp_path):
    root = build_world(tmp_path)
    write(root, f"Build/worlds/{CODE}/Step0_Review_Round1.md", review_text(cleared=False))
    assert "handoff-02-step0" in _failing(_run(root))
    root = build_world(tmp_path / "b")
    write(root, f"Build/worlds/{CODE}/Step0_Movement_Scope_Confirmation.md", "# Step 0\n")
    assert "handoff-02-step0" in _failing(_run(root))
    root = build_world(tmp_path / "c")
    (root / f"Build/worlds/{CODE}/Step0_Movement_Scope_Confirmation.md").unlink()
    assert "handoff-02-step0" in _failing(_run(root))


def test_03_step1_needs_a_review_that_cleared(tmp_path):
    root = build_world(tmp_path)
    (root / f"Build/worlds/{CODE}/Doc_01_Review_Round1.md").unlink()
    assert "handoff-03-step1" in _failing(_run(root))


def test_step_taking_more_than_three_rounds_fails(tmp_path):
    root = build_world(tmp_path)
    for n in (2, 3, 4):
        write(root, f"Build/worlds/{CODE}/Doc_02_Review_Round{n}.md", review_text(n))
    assert "handoff-04-step2" in _failing(_run(root))


def test_04_registry_must_give_every_corpus_map_work_and_holdings_file_a_line(tmp_path):
    root = build_world(tmp_path)
    write(root, f"Build/worlds/{CODE}/Source_Registry.md", "# Source Registry\n\nNothing here.\n")
    assert "handoff-04-step2" in _failing(_run(root))
    root = build_world(tmp_path / "h")
    deps = quiet_deps(root)
    deps.holdings = lambda code: [{"file": "zzz99_unlisted.txt", "disposition": "in scope, unread"}]
    reports = _run(root, deps)
    assert any("zzz99_unlisted.txt" in f.reason for f in reports["handoff-04-step2"].findings)
    deps.holdings = lambda code: [{"file": "zzz99_unlisted.txt", "disposition": "out of window"}]
    assert "handoff-04-step2" not in _failing(_run(root, deps))


def test_04_dossier_cross_link_needs_a_registry_line(tmp_path):
    root = build_world(tmp_path)
    path = root / f"Build/worlds/_cross-world/dossiers/{SLUG}_Source_Readiness_Dossier.md"
    path.write_text(path.read_text().replace("## 2. Cross-link opportunities\n\n- —", "## 2. Cross-link opportunities\n\n- Hermetic treatise vendored under another bucket"), encoding="utf-8")
    assert "handoff-04-step2" in _failing(_run(root))


def test_05_dossier_missing_section_or_header_field(tmp_path):
    root = build_world(tmp_path)
    path = root / f"Build/worlds/_cross-world/dossiers/{SLUG}_Source_Readiness_Dossier.md"
    text = path.read_text()
    path.write_text(text.replace("## 4. Checked and closed", "## Closed"), encoding="utf-8")
    assert "handoff-05-dossier" in _failing(_run(root))
    path.write_text(text.replace("**Time window:** 300-400", "**Time window:** —"), encoding="utf-8")
    assert "handoff-05-dossier" in _failing(_run(root))
    path.unlink()
    assert "handoff-05-dossier" in _failing(_run(root))


def test_06_bucket_missing_and_merge_check_failure(tmp_path):
    root = build_world(tmp_path)
    deps = quiet_deps(root)
    deps.corpus_merge_check = lambda r: (False, "1 finding")
    assert "handoff-06-corpus-map" in _failing(_run(root, deps))
    (root / f"cic/corpus-map/{SLUG}.yaml").unlink()
    assert "handoff-06-corpus-map" in _failing(_run(root))


def test_07_text_not_vendored_unregistered_or_without_rights(tmp_path):
    root = build_world(tmp_path)
    (root / "cic/texts/REGISTRY.yaml").write_text("[]\n", encoding="utf-8")
    assert "handoff-07-texts" in _failing(_run(root))
    root = build_world(tmp_path / "r")
    write(root, f"cic/texts/{TEXT_FILE}", "Title: T\nRights: All rights reserved\n\ntext\n")
    assert "handoff-07-texts" in _failing(_run(root))
    root = build_world(tmp_path / "v")
    (root / f"cic/texts/{TEXT_FILE}").unlink()
    assert "handoff-07-texts" in _failing(_run(root))
    root = build_world(tmp_path / "i")
    deps = quiet_deps(root)
    deps.corpus_index_build = lambda r: (False, "boom")
    assert "handoff-07-texts" in _failing(_run(root, deps))


def test_08_quote_check_runs_and_can_be_skipped_visibly(tmp_path):
    root = build_world(tmp_path)
    path = root / f"Build/worlds/{CODE}/Doc_01_World_Identification.md"
    path.write_text(path.read_text().replace("gathered", "summoned"), encoding="utf-8")
    assert "handoff-08-quotes" in _failing(_run(root))
    skipped = _run(root, quotes=False)["handoff-08-quotes"]
    assert skipped.skipped and not skipped.findings


def test_09_dossier_question_needs_a_home(tmp_path):
    root = build_world(tmp_path)
    (root / "Build/worlds/_cross-world/NEEDS-RULING.md").write_text("# Needs ruling\n", encoding="utf-8")
    assert "handoff-09-open-questions" in _failing(_run(root))
    write(root, f"Build/worlds/{CODE}/Open_Gaps_Tracking.md", "# Open Gaps\n\n- 2026-09-01: whether the northern collection belongs to a sibling world stays open.\n")
    assert "handoff-09-open-questions" not in _failing(_run(root))


def test_10_ledger_must_exist_and_carry_a_dated_entry(tmp_path):
    root = build_world(tmp_path)
    write(root, f"Build/worlds/{CODE}/Open_Gaps_Tracking.md", "# Open Gaps\n")
    assert "handoff-10-ledger" in _failing(_run(root))
    (root / f"Build/worlds/{CODE}/Open_Gaps_Tracking.md").unlink()
    assert "handoff-10-ledger" in _failing(_run(root))


def test_11_narration_hits_from_the_commentary_scan_fail(tmp_path):
    root = build_world(tmp_path)
    deps = quiet_deps(root)
    deps.commentary = lambda r, paths: [("Build/worlds/fx/Doc_01_World_Identification.md", 4, "REWRITE", "review-round")]
    reports = _run(root, deps)
    assert "handoff-11-narration" in _failing(reports)
    assert reports["handoff-11-narration"].findings[0].path.endswith("Doc_01_World_Identification.md:4")


def test_11_default_scan_runs_the_real_commentary_classifier(tmp_path):
    root = build_world(tmp_path)
    write(root, f"Build/worlds/{CODE}/Doc_01_World_Identification.md", "# Doc\n\nRevised after Round 2 review by the reviewer, 2026-09-02.\n")
    deps = quiet_deps(root)
    deps.commentary = Deps().commentary
    assert "handoff-11-narration" in _failing(_run(root, deps))


def test_12_manifest_missing_wrong_path_or_missing_round(tmp_path):
    root = build_world(tmp_path)
    manifest = root / f"Build/worlds/{CODE}/build/{CODE}_Handoff_Manifest.md"
    text = manifest.read_text()
    manifest.write_text(text.replace("Doc_02_Source_Ecology.md`", "Doc_99.md`", 1), encoding="utf-8")
    assert "handoff-12-manifest" in _failing(_run(root))
    manifest.write_text(text.replace("| Step 1 | 1 | Doc_01_Review_Round1.md | 2026-09-21 |", "| Step 1 | | | |"), encoding="utf-8")
    assert "handoff-12-manifest" in _failing(_run(root))
    manifest.write_text(text.replace("2026-09-29", ""), encoding="utf-8")
    assert "handoff-12-manifest" in _failing(_run(root))
    manifest.unlink()
    assert "handoff-12-manifest" in _failing(_run(root))
    write(root, f"Build/worlds/{CODE}/{CODE}_Handoff_Manifest.md", text)
    assert "handoff-12-manifest" in _failing(_run(root)), "the manifest lives in build/"


def test_a_not_approved_verdict_is_not_clearance(tmp_path):
    for verdict in ("Verdict: Not Approved to proceed.", "**Not Approved to Proceed.** Nine substantial findings.", "> **Disposition:** Not approved to proceed - bounded."):
        root = build_world(tmp_path / str(abs(hash(verdict))))
        write(root, f"Build/worlds/{CODE}/Doc_01_Review_Round1.md", review_text(cleared=False).replace("Substantial revision required.", verdict))
        assert "handoff-03-step1" in _failing(_run(root)), verdict


def test_a_positive_verdict_line_clears_in_the_labelled_forms_the_fleet_uses(tmp_path):
    for verdict in ("Verdict: Approved to proceed.", "**Disposition: Approved to proceed.**", "> **Status:** **Approved to proceed** (self-disposed)", "Document status: Cleared review \u2014 Approved to proceed, self-disposed"):
        root = build_world(tmp_path / str(abs(hash(verdict))))
        write(root, f"Build/worlds/{CODE}/Doc_01_Review_Round1.md", review_text(cleared=False).replace("Substantial revision required.", verdict))
        assert "handoff-03-step1" not in _failing(_run(root)), verdict


def test_the_phrase_inside_running_prose_is_not_clearance(tmp_path):
    root = build_world(tmp_path)
    prose = 'Substantial revision required. The earlier "Approved to proceed" claim in section 3 is withdrawn.'
    write(root, f"Build/worlds/{CODE}/Doc_01_Review_Round1.md", review_text(cleared=False).replace("Substantial revision required.", prose))
    assert "handoff-03-step1" in _failing(_run(root))


def test_skipping_the_quote_check_is_an_incomplete_run_not_a_pass(tmp_path):
    from engine.m10.common import emit

    root = build_world(tmp_path)
    write(root, f"Build/worlds/{CODE}/Doc_01_World_Identification.md", '# Doc 1\n\nThey say "the presbyters of the northern hills burned every copy of the letter in the square".\n')
    assert emit(run_handoff(CODE, quiet_deps(root), quotes=True), as_json=True) == 1
    assert emit(run_handoff(CODE, quiet_deps(root), quotes=False), as_json=True) == 1
    clean = build_world(tmp_path / "clean")
    assert emit(run_handoff(CODE, quiet_deps(clean), quotes=True), as_json=True) == 0
    assert emit(run_handoff(CODE, quiet_deps(clean), quotes=False), as_json=True) == 1


def test_01_a_new_world_must_set_safety_adjacent_to_true_or_false(tmp_path):
    for entry in ("kind: formation\nworld_id: fx-world\ncensus_id: fx-tradition\n", "kind: formation\nworld_id: fx-world\ncensus_id: fx-tradition\nsafety_adjacent: maybe\n"):
        root = build_world(tmp_path / str(len(entry)))
        write(root, f"records/worlds/{CODE}.yaml", entry)
        reports = _run(root)
        assert any("safety_adjacent" in f.reason for f in reports["handoff-01-identity"].findings)
    for value in ("true", "false"):
        root = build_world(tmp_path / value)
        write(root, f"records/worlds/{CODE}.yaml", f"kind: formation\nworld_id: fx-world\ncensus_id: fx-tradition\nsafety_adjacent: {value}\n")
        assert "handoff-01-identity" not in _failing(_run(root))


def test_01_a_grandfathered_world_without_the_field_is_not_a_handoff_failure(tmp_path):
    from engine.m10.common import safety_adjacent_status

    value, reason = safety_adjacent_status("syr", {"world_id": "x"})
    assert value is None and "grandfathered" in reason
