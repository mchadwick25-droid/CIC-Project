import json

from engine.m10.cli import main
from engine.m10.common import emit
from engine.m10.handoff import run_handoff
from engine.m10.rebaseline import declaration_path, draft_declaration, load_declaration

from .fixture_world import CODE, build_world, quiet_deps, review_text, write

HEADER = "World: fx\nDeclared by: project lead\nDate: 2026-09-29\nProcess version: pre-V2.0 document-first\nScope: Step 0 and Doc_02\n\n"
TABLE_HEAD = "| Document | Check accepted | Recorded state at declaration | Reason |\n|---|---|---|---|\n"
TAIL = "\n## Findings carried open and how each will be checked\n\n- the northern collection question, checked by Doc_03 review\n"
BASE = f"Build/worlds/{CODE}"


def _cleared(n):
    return review_text(n).replace("Approved to proceed.", "## VERDICT: NO SUBSTANTIAL REVISION REQUIRED — CLEARED REVIEW")


def _declare(root, rows, header=HEADER):
    write(root, f"Build/worlds/{CODE}/build/{CODE}_Rebaseline_Declaration.md", header + TABLE_HEAD + "".join(rows) + TAIL)


def _world(tmp_path):
    """Doc_02 has four review rounds; Step 0's only round says CLEARED."""
    root = build_world(tmp_path)
    for n in (2, 3, 4):
        write(root, f"{BASE}/Doc_02_Review_Round{n}.md", review_text(n))
    write(root, f"{BASE}/Step0_Review_Round1.md", _cleared(1))
    return root


CAP = "| Doc_02 | review-round-cap | review files: 4 | four rounds under earlier rules |\n"
WORD = "| Step0 | verdict-wording | review files: 1; latest verdict: CLEARED | older wording |\n"


def _run(root):
    return {r.name: r for r in run_handoff(CODE, quiet_deps(root))}


def _failing(reports):
    return {n for n, r in reports.items() if r.findings}


def test_valid_declaration_accepts_round_cap_and_wording_only(tmp_path):
    root = _world(tmp_path)
    assert {"handoff-02-step0", "handoff-04-step2"} <= _failing(_run(root))
    _declare(root, [CAP, WORD])
    reports = _run(root)
    assert _failing(reports) == set()
    assert len(reports["handoff-04-step2"].accepted) == 1 and len(reports["handoff-02-step0"].accepted) == 1
    assert all(a.startswith("ACCEPTED (project lead declaration 2026-09-29)") for r in reports.values() for a in r.accepted)
    assert emit(list(reports.values()), as_json=False) == 0


def test_other_failures_still_fail_beside_a_valid_declaration(tmp_path):
    root = _world(tmp_path)
    _declare(root, [CAP, WORD])
    (root / "cic/corpus-map/fx-tradition.yaml").unlink()
    assert _failing(_run(root)) == {"handoff-06-corpus-map"}


def test_accepted_lines_appear_in_default_and_json_output(tmp_path, capsys):
    root = _world(tmp_path)
    _declare(root, [CAP, WORD])
    reports = list(run_handoff(CODE, quiet_deps(root)))
    assert emit(reports, as_json=False) == 0
    out = capsys.readouterr().out
    assert "ACCEPTED (project lead declaration 2026-09-29)" in out and "accepted by project lead declaration: 2" in out
    assert emit(reports, as_json=True) == 0
    doc = json.loads(capsys.readouterr().out)
    assert doc["accepted"] == 2
    assert any(r.get("accepted") for r in doc["reports"])


def test_forbidden_check_rejects_the_declaration(tmp_path):
    root = _world(tmp_path)
    _declare(root, [CAP, WORD, "| Doc_01 | quote re-verification | review files: 1 | no |\n"])
    reports = _run(root)
    assert "handoff-declaration" in _failing(reports)
    assert not any(r.accepted for r in reports.values())
    assert {"handoff-02-step0", "handoff-04-step2"} <= _failing(reports)


def test_stale_review_count_rejects_that_document(tmp_path):
    root = _world(tmp_path)
    _declare(root, [CAP, WORD])
    write(root, f"{BASE}/Doc_02_Review_Round5.md", review_text(5))
    reports = _run(root)
    assert "handoff-declaration" in _failing(reports)
    assert "handoff-04-step2" in _failing(reports) and not reports["handoff-04-step2"].accepted
    assert reports["handoff-02-step0"].accepted


def test_wrong_declared_by_rejects(tmp_path):
    root = _world(tmp_path)
    _declare(root, [CAP, WORD], header=HEADER.replace("project lead", "build thread"))
    reports = _run(root)
    assert "handoff-declaration" in _failing(reports) and not any(r.accepted for r in reports.values())
    assert any("project lead" in f.reason for f in reports["handoff-declaration"].findings)


def test_a_world_built_under_v2_cannot_use_a_declaration(tmp_path):
    root = _world(tmp_path)
    _declare(root, [CAP, WORD], header=HEADER.replace("pre-V2.0 document-first", "V2.0"))
    reports = _run(root)
    assert "handoff-declaration" in _failing(reports) and not any(r.accepted for r in reports.values())
    assert any("V2.0 or later" in f.reason for f in reports["handoff-declaration"].findings)


def test_earlier_process_versions_are_accepted_in_either_wording(tmp_path):
    for wording in ("V1.2 and V1.3", "before V2.0", "pre-V2.0 document-first"):
        root = _world(tmp_path / wording.replace(" ", "_"))
        _declare(root, [CAP, WORD], header=HEADER.replace("pre-V2.0 document-first", wording))
        assert "handoff-declaration" not in _failing(_run(root)), wording


def test_wording_row_needs_the_recorded_verdict_to_match_the_disk(tmp_path):
    root = _world(tmp_path)
    _declare(root, [CAP, "| Step0 | verdict-wording | review files: 1; latest verdict: Approved to proceed | wrong |\n"])
    assert "handoff-declaration" in _failing(_run(root))


def test_a_negative_verdict_cannot_be_accepted(tmp_path):
    root = _world(tmp_path)
    write(root, f"{BASE}/Step0_Review_Round1.md", review_text(1, cleared=False).replace("Substantial revision required.", "Verdict: Not approved to proceed."))
    _declare(root, [CAP, "| Step0 | verdict-wording | review files: 1; latest verdict: NOT APPROVED | no |\n"])
    reports = _run(root)
    assert "handoff-declaration" in _failing(reports) and "handoff-02-step0" in _failing(reports)


def test_cap_row_on_a_document_within_the_cap_is_rejected(tmp_path):
    root = _world(tmp_path)
    _declare(root, ["| Doc_01 | review-round-cap | review files: 1 | none needed |\n"])
    assert "handoff-declaration" in _failing(_run(root))


def test_no_declaration_leaves_the_run_unchanged(tmp_path, capsys):
    root = _world(tmp_path)
    reports = list(run_handoff(CODE, quiet_deps(root)))
    assert len(reports) == 12 and not any(r.accepted for r in reports)
    assert all("accepted" not in r.to_dict() for r in reports)
    emit(reports, as_json=False)
    text = capsys.readouterr().out
    assert "ACCEPTED" not in text and "accepted" not in text
    emit(reports, as_json=True)
    assert "accepted" not in capsys.readouterr().out


def test_a_declaration_row_for_a_later_document_is_accepted_and_shown(tmp_path):
    root = _world(tmp_path)
    write(root, f"{BASE}/Doc_03_Lexicon.md", "# Doc 3\n")
    for n in (1, 2, 3, 4):
        write(root, f"{BASE}/Doc_03_Review_Round{n}.md", review_text(n))
    _declare(root, [CAP, WORD, "| Doc_03 | review-round-cap | review files: 4 | earlier rules |\n"])
    reports = _run(root)
    assert any("Doc_03 has 4 review files" in a for a in reports["handoff-declaration"].accepted)
    assert not reports["handoff-declaration"].findings


def test_draft_is_built_from_disk_state_and_needs_filling_before_it_validates(tmp_path):
    root = _world(tmp_path)
    draft = draft_declaration(CODE, root)
    assert "| Doc_02 | review-round-cap | review files: 4 |" in draft
    assert "| Step0 | verdict-wording | review files: 1; latest verdict: CLEARED |" in draft
    assert "Doc_01" not in draft
    write(root, f"Build/worlds/{CODE}/build/{CODE}_Rebaseline_Declaration.md", draft)
    _, problems = load_declaration(CODE, root)
    assert problems
    filled = draft.replace("<the process version the world was built under>", "pre-V2.0").replace("<what this declaration covers>", "Step 0 and Doc_02").replace("<reason>", "earlier rules").replace("<finding, and how it will be checked>", "open item, checked in Doc_03 review")
    declaration_path(CODE, root).write_text(filled, encoding="utf-8")
    declaration, problems = load_declaration(CODE, root)
    assert not problems and len(declaration.rows) == 2


def test_cli_prints_the_draft_without_writing(tmp_path, capsys):
    root = _world(tmp_path)
    assert main(["handoff", CODE, "--draft-declaration", "--root", str(root)]) == 0
    assert "review-round-cap" in capsys.readouterr().out
    assert not declaration_path(CODE, root).exists()


def test_review_files_sharing_a_round_number_all_count_in_the_declaration(tmp_path):
    root = build_world(tmp_path)
    for name in ("Doc_02_Recheck_Round1.md", "Doc_02_SpotCheck_Round1.md", "Doc_02_Independent_Check.md"):
        write(root, f"{BASE}/{name}", review_text(1))
    assert "| Doc_02 | review-round-cap | review files: 4 |" in draft_declaration(CODE, root)
    _declare(root, ["| Doc_02 | review-round-cap | review files: 4 | earlier rules |\n"])
    assert not _run(root)["handoff-declaration"].findings
    _declare(root, ["| Doc_02 | review-round-cap | review files: 2 | earlier rules |\n"])
    assert "the disk has 4" in " ".join(f.reason for f in _run(root)["handoff-declaration"].findings)
