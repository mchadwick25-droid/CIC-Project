"""Hermetic tests for engine.m10.integrity: fixtures live under tmp_path."""
from engine.m10 import cli
from engine.m10.integrity import check_integrity, check_stated_counts, check_superseded

from .test_deployed import _prompt, _records, _world_root

WORLD = "Build/worlds/w"
LEDGER = "# Open Gaps\n\n- 2026-09-01: the dating of the northern letter is disputed among editors.\n"
DOC = "# Doc 4\n\n## Open items\n\n- The dating of the northern letter is disputed among editors.\n"


def _write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _clean_world(tmp_path, *, prompt=None):
    root = _world_root(tmp_path, prompt or _prompt(), _records())
    _write(root, f"{WORLD}/Open_Gaps_Tracking.md", LEDGER)
    _write(root, f"{WORLD}/Doc_04_Gravity_Discovery.md", DOC)
    _write(root, f"{WORLD}/w_Representative_Construction_Notes_Vera.md", "# Notes\n\nThe record store holds 3 quote records.\n")
    return root


def _by_name(reports):
    return {r.name: r for r in reports}


def _checks(report):
    return sorted({f.check for f in report.findings})


def test_a_world_that_meets_the_principle_passes(tmp_path):
    reports = check_integrity("w", _clean_world(tmp_path), check_stale=False)
    assert all(r.ok for r in reports), [f.line() for r in reports for f in r.findings]


def test_an_open_item_with_no_ledger_entry_fails(tmp_path):
    root = _clean_world(tmp_path)
    _write(root, f"{WORLD}/Doc_05_Ecology.md", "# Doc 5\n\n## Open items\n\n- Whether the eastern hymnal predates the schism at all.\n")
    report = _by_name(check_integrity("w", root, check_stale=False))["integrity open items"]
    assert _checks(report) == ["i:gaps-unmatched"]


def test_a_file_named_as_an_earlier_version_and_left_unmarked_fails(tmp_path):
    root = _clean_world(tmp_path)
    _write(root, f"{WORLD}/Doc_02_Source_Ecology_OLD.md", "# Doc 2, earlier text\n")
    findings = check_superseded("w", root)
    assert [f.check for f in findings] == ["i:superseded-unmarked"]


def test_an_earlier_version_marked_superseded_in_its_first_lines_passes(tmp_path):
    root = _clean_world(tmp_path)
    _write(root, f"{WORLD}/Doc_02_Source_Ecology_OLD.md", "# Doc 2\n\nStatus: Superseded by Doc_02_Source_Ecology.md.\n")
    assert check_superseded("w", root) == []


def test_a_file_in_archive_is_not_a_live_version(tmp_path):
    root = _clean_world(tmp_path)
    _write(root, f"{WORLD}/Archive/Doc_02_Source_Ecology_OLD.md", "# Doc 2, earlier text\n")
    _write(root, f"{WORLD}/Archive/Doc_04_Gravity_Discovery.md", "# Doc 4, earlier text\n")
    assert check_superseded("w", root) == []


def test_two_unmarked_files_standing_as_the_same_document_fail(tmp_path):
    root = _clean_world(tmp_path)
    _write(root, f"{WORLD}/Doc_04_Gravity_Discovery_Revised.md", "# Doc 4 again\n")
    findings = check_superseded("w", root)
    assert [f.check for f in findings] == ["i:two-live-versions"] and "Doc_04" in findings[0].reason


def test_two_construction_notes_files_fail_until_one_is_marked(tmp_path):
    root = _clean_world(tmp_path)
    other = _write(root, f"{WORLD}/w_Representative_Construction_Notes_Vera_v1.md", "# Notes, first version\n")
    assert [f.check for f in check_superseded("w", root)] == ["i:two-live-versions"]
    other.write_text("# Notes, first version\n\nSuperseded by the current Construction Notes.\n")
    assert check_superseded("w", root) == []


def test_a_stated_record_count_the_records_contradict_fails(tmp_path):
    root = _clean_world(tmp_path)
    _write(root, f"{WORLD}/w_Representative_Construction_Notes_Vera.md", "# Notes\n\nThe record store holds 7 quote records.\n")
    findings = check_stated_counts("w", root)
    assert [f.check for f in findings] == ["i:count-contradiction"] and "the records hold 3" in findings[0].reason


def test_notes_marked_superseded_are_not_read_for_counts(tmp_path):
    root = _clean_world(tmp_path)
    _write(root, f"{WORLD}/w_Representative_Construction_Notes_Vera.md", "# Notes\n\nSuperseded.\n\nThe record store holds 7 quote records.\n")
    assert check_stated_counts("w", root) == []


def test_a_fix_described_as_applied_but_absent_from_the_deployed_prompt_fails(tmp_path):
    root = _clean_world(tmp_path, prompt=_prompt(gravities=0))
    report = _by_name(check_integrity("w", root, check_stale=False))["integrity deployed artifact"]
    assert _checks(report) == ["i:deployed:k:gravity-index"]


def test_a_world_folder_that_does_not_exist_fails(tmp_path):
    assert _checks(check_integrity("nowhere", tmp_path)[0]) == ["i:no-world"]


def test_the_command_exits_by_the_findings(tmp_path, capsys):
    root = _clean_world(tmp_path)
    assert cli.main(["integrity", "w", "--no-stale", "--root", str(root)]) == 0
    _write(root, f"{WORLD}/Doc_02_Source_Ecology_OLD.md", "# earlier\n")
    assert cli.main(["integrity", "w", "--no-stale", "--root", str(root)]) == 1
    assert "i:superseded-unmarked" in capsys.readouterr().out


def _stale(monkeypatch):
    monkeypatch.setattr("engine.m2.checks.staleness_sweep", lambda registry, repo_root: {"w": {"stale": True, "diff": ["compiled/prompt.txt"]}})


def test_the_stale_package_check_runs_by_default_and_names_the_repin_command(tmp_path, monkeypatch):
    root = _clean_world(tmp_path)
    _stale(monkeypatch)
    report = _by_name(check_integrity("w", root))["integrity deployed artifact"]
    assert _checks(report) == ["i:deployed:k:stale"]
    assert "python -m engine.m2.cli build w" in report.findings[0].reason


def test_no_stale_skips_the_recompile_as_it_does_for_deployed(tmp_path, monkeypatch, capsys):
    root = _clean_world(tmp_path)
    _stale(monkeypatch)
    assert _checks(_by_name(check_integrity("w", root, check_stale=False))["integrity deployed artifact"]) == []
    assert cli.main(["integrity", "w", "--root", str(root)]) == 1
    assert "i:deployed:k:stale" in capsys.readouterr().out
    assert cli.main(["integrity", "w", "--no-stale", "--root", str(root)]) == 0
