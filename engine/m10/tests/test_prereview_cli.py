import json
import types

import pytest

from engine.m10 import cli
from engine.m10.prereview import STEPS, StepResult, run_prereview

from .fixture_world import CODE, build_world, review_text, write


def _steps(log, fail_at=None):
    def make(name):
        def step(code, root):
            log.append(name)
            return StepResult([f"{name} broke"] if name == fail_at else [], [f"{name} ran"])

        return step

    return tuple((name, make(name), needs) for name, _, needs in STEPS)


def test_steps_run_in_the_specified_order(tmp_path):
    root = build_world(tmp_path)
    (root / "records" / CODE).mkdir(parents=True)
    log = []
    reports = run_prereview(CODE, root=root, steps=_steps(log))
    assert log == ["prereview-build", "prereview-bar-screen", "prereview-cross-world", "prereview-holdings"]
    assert all(r.ok for r in reports)


def test_stops_on_first_hard_failure(tmp_path):
    root = build_world(tmp_path)
    (root / "records" / CODE).mkdir(parents=True)
    log = []
    reports = run_prereview(CODE, root=root, steps=_steps(log, fail_at="prereview-bar-screen"))
    assert log == ["prereview-build", "prereview-bar-screen"]
    assert [r.name for r in reports if r.findings] == ["prereview-bar-screen"]


def test_a_crashing_step_is_a_hard_failure(tmp_path):
    root = build_world(tmp_path)
    (root / "records" / CODE).mkdir(parents=True)

    def boom(code, root):
        raise RuntimeError("no gates report")

    reports = run_prereview(CODE, root=root, steps=(("prereview-build", boom, True), ("prereview-holdings", lambda c, r: StepResult([], []), False)))
    assert reports[0].findings and "RuntimeError" in reports[0].findings[0].reason
    assert not any(r.name == "prereview-holdings" for r in reports)


def test_world_without_records_yet_skips_the_record_steps_visibly_and_still_runs_holdings(tmp_path):
    root = build_world(tmp_path)
    log = []
    reports = {r.name: r for r in run_prereview(CODE, doc=2, root=root, steps=_steps(log))}
    assert log == ["prereview-holdings"]
    assert all(reports[n].skipped for n in ("prereview-build", "prereview-bar-screen", "prereview-cross-world"))
    assert not reports["prereview-holdings"].skipped and reports["prereview-holdings"].ok


def test_steps_receive_the_root(tmp_path):
    root = build_world(tmp_path)
    seen = []
    step = lambda code, r: (seen.append(r), StepResult([], []))[1]  # noqa: E731
    run_prereview(CODE, root=root, steps=(("prereview-holdings", step, False),))
    assert seen == [root]


def test_the_repository_only_tools_refuse_a_foreign_root_instead_of_reading_the_wrong_tree(tmp_path):
    from engine.m10.prereview import step_bar_screen, step_build, step_cross_world

    for step in (step_build, step_bar_screen, step_cross_world):
        assert "--root" in step(CODE, tmp_path).hard[0]


def test_the_holdings_step_reads_the_root_registry(tmp_path):
    from engine.m10.prereview import step_holdings

    root = build_world(tmp_path)
    assert "no time_window" in step_holdings(CODE, root).hard[0]
    registry = root / f"records/worlds/{CODE}.yaml"
    registry.write_text(registry.read_text() + "time_window: {start: 9000, end: 9100}\n")
    assert step_holdings(CODE, root).hard == []


def test_a_missing_document_fails_and_stops_the_run(tmp_path):
    root = build_world(tmp_path)
    log = []
    reports = run_prereview(CODE, doc=3, root=root, steps=_steps(log))
    doc_report = next(r for r in reports if r.name == "prereview-document")
    assert doc_report.findings and "Doc_03" in doc_report.findings[0].reason
    assert log == []


def test_doc_zero_names_the_step_zero_file(tmp_path):
    root = build_world(tmp_path)
    report = next(r for r in run_prereview(CODE, doc=0, root=root, steps=_steps([])) if r.name == "prereview-document")
    assert report.ok and "Step0_Movement_Scope_Confirmation.md" in report.notes[0]
    (root / f"Build/worlds/{CODE}/Step0_Movement_Scope_Confirmation.md").unlink()
    report = next(r for r in run_prereview(CODE, doc=0, root=root, steps=_steps([])) if r.name == "prereview-document")
    assert report.findings and "Step 0" in report.findings[0].reason


def test_a_document_number_outside_zero_to_ten_fails(tmp_path):
    root = build_world(tmp_path)
    assert next(r for r in run_prereview(CODE, doc=11, root=root, steps=()) if r.name == "prereview-document").findings


def test_the_command_saves_the_output_as_the_review_brief_and_states_the_path(tmp_path, capsys, monkeypatch):
    root = build_world(tmp_path)
    monkeypatch.setattr("engine.m10.cli.run_prereview", lambda code, doc, r: run_prereview(code, doc, r, steps=_steps([])))
    assert cli.main(["prereview", CODE, "--doc", "2", "--root", str(root)]) == 0
    out = capsys.readouterr().out
    saved = root / f"Build/worlds/{CODE}/build/{CODE}_Prereview_Doc2.txt"
    assert f"review brief saved: Build/worlds/{CODE}/build/{CODE}_Prereview_Doc2.txt" in out
    text = saved.read_text()
    assert "prereview-holdings: PASS" in text and text.split("\n", 1)[1] in out
    assert cli.main(["prereview", CODE, "--doc", "0", "--root", str(root)]) == 0
    assert (root / f"Build/worlds/{CODE}/build/{CODE}_Prereview_Step0.txt").is_file()


def test_the_json_output_carries_the_saved_path(tmp_path, capsys, monkeypatch):
    root = build_world(tmp_path)
    monkeypatch.setattr("engine.m10.cli.run_prereview", lambda code, doc, r: run_prereview(code, doc, r, steps=_steps([])))
    assert cli.main(["prereview", CODE, "--json", "--root", str(root)]) == 0
    assert json.loads(capsys.readouterr().out)["saved"] == f"Build/worlds/{CODE}/build/{CODE}_Prereview.txt"


def test_an_unregistered_world_saves_nothing(tmp_path, capsys):
    assert cli.main(["prereview", "nope", "--root", str(tmp_path)]) == 1
    assert not (tmp_path / "Build").exists()


def test_unregistered_world_fails(tmp_path):
    assert run_prereview("nope", root=tmp_path, steps=())[0].findings


def test_cli_roundcount_exit_codes_and_route_message(tmp_path, capsys):
    for n in (1, 2, 3, 4):
        write(tmp_path, f"Build/worlds/w/Doc_05_Review_Round{n}.md", "x")
    assert cli.main(["roundcount", "w", "5", "--root", str(tmp_path)]) == 1
    assert "route to project lead" in capsys.readouterr().out
    assert cli.main(["roundcount", "w", "4", "--root", str(tmp_path)]) == 0
    assert cli.main(["roundcount", "w", "4", "--check-new", "--root", str(tmp_path)]) == 0


def test_cli_json_output_and_reviewfile(tmp_path, capsys):
    good = write(tmp_path, "Doc_01_Review_Round1.md", review_text())
    assert cli.main(["reviewfile", str(good), "--json"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["pass"] is True
    bad = write(tmp_path, "Doc_02_Review_Round1.md", "no label\n")
    assert cli.main(["reviewfile", str(bad)]) == 1
    assert "reviewfile-label" in capsys.readouterr().out


def test_cli_lists_only_optional_modules_that_exist(capsys):
    with pytest.raises(SystemExit):
        cli.main(["--help"])
    help_text = capsys.readouterr().out
    for name in ("handoff", "prereview", "roundcount", "reviewfile", "gaps"):
        assert name in help_text


def test_cli_dispatches_to_optional_module_subcommands(monkeypatch, capsys):
    def add_parser(sub):
        p = sub.add_parser("fakecheck")
        p.add_argument("world_code")

    def run(args):
        print("ran", args.command, args.world_code)
        return 7

    Fake = types.SimpleNamespace(__name__="engine.m10.fake", add_parser=add_parser, run=run)
    monkeypatch.setattr(cli, "_load_optional", lambda: [Fake])
    assert cli.main(["fakecheck", "zz"]) == 7
    assert "ran fakecheck zz" in capsys.readouterr().out


def test_load_optional_skips_only_missing_modules(monkeypatch):
    import importlib

    real = importlib.import_module

    def fake(name):
        if name == "engine.m10.deployed":
            raise ModuleNotFoundError("gone", name=name)
        if name == "engine.m10.validation":
            raise ModuleNotFoundError("inner dependency", name="something_else")
        return real(name)

    monkeypatch.setattr(cli.importlib, "import_module", fake)
    with pytest.raises(ModuleNotFoundError):
        cli._load_optional()
