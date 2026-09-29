import json
import types

import pytest

from engine.m10 import cli
from engine.m10.prereview import STEPS, StepResult, run_prereview

from .fixture_world import CODE, build_world, review_text, write


def _steps(log, fail_at=None):
    def make(name):
        def step(code):
            log.append(name)
            return StepResult([f"{name} broke"] if name == fail_at else [], [f"{name} ran"])

        return step

    return tuple((name, make(name)) for name, _ in STEPS)


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

    def boom(code):
        raise RuntimeError("no gates report")

    reports = run_prereview(CODE, root=root, steps=(("prereview-build", boom), ("prereview-holdings", lambda c: StepResult([], []))))
    assert reports[0].findings and "RuntimeError" in reports[0].findings[0].reason
    assert not any(r.name == "prereview-holdings" for r in reports)


def test_world_without_records_yet_skips_visibly(tmp_path):
    root = build_world(tmp_path)
    reports = run_prereview(CODE, doc=2, root=root, steps=_steps([]))
    assert all(r.skipped for r in reports if r.name.startswith("prereview-") and r.name != "prereview-document")


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
