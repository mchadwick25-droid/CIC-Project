"""The pre-review bundle (check c): the document exists, then compile and gate
battery, bar screen, cross-world check, holdings report, in that order,
stopping at the first hard failure. The output is saved as the review brief."""
from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .common import REPO_ROOT, Finding, Report, registry_entry, rel, world_dir
from .rebaseline import DOCUMENTS, doc_label, document_path

FK_CEILING = 10.0
PACKAGE_ID = "prereview"


@dataclass
class StepResult:
    hard: list[str]
    summary: list[str]


def git_head(root: Path = REPO_ROOT) -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def _is_repo(root: Path) -> bool:
    return root.resolve() == REPO_ROOT.resolve()


def _repo_only(root: Path, tool: str) -> StepResult | None:
    """The M1 and M2 tools read this repository's registry and records only. A
    run pointed at another root must not report on the wrong tree."""
    if _is_repo(root):
        return None
    return StepResult([f"{tool} reads only this repository's registry and records; it cannot run against --root {root}"], [])


def step_build(code: str, root: Path = REPO_ROOT) -> StepResult:
    """Compile the world exactly as `engine.m2.cli build` does, without writing
    a package, and read the M1 gate battery from the compiled gates report."""
    refused = _repo_only(root, "engine.m2 compile")
    if refused:
        return refused
    from engine.m2.compiler import compile_world

    head = git_head(root)
    package = compile_world(world_key=code, package_id=PACKAGE_ID, records_commit=head, compiler_version=head)
    gates = json.loads(package["validation/gates-report.json"])["gates"]
    failing = {name: g["findings"] for name, g in gates.items() if not g["pass"]}
    hard = [f"gate {name}: {len(fs)} finding(s), first: {fs[0]}" for name, fs in failing.items()]
    return StepResult(hard, [f"m2 build: {len(gates)} gate(s), {len(failing)} failing"])


def step_bar_screen(code: str, root: Path = REPO_ROOT) -> StepResult:
    refused = _repo_only(root, "engine.m1.bar_screen")
    if refused:
        return refused
    from engine.m1.bar_screen import screen_world

    report = screen_world(code)
    fields = report["fields"]
    over = [f"{k}: fk max {v['fk_grade_max']} in {v['worst_record']}" for k, v in fields.items() if (v["fk_grade_max"] or 0) > FK_CEILING]
    lines = [f"bar screen: {len(fields)} voice-diet field(s), {len(over)} over FK {FK_CEILING:g}"] + [f"  over ceiling, {o}" for o in over]
    return StepResult([], lines)


def step_cross_world(code: str, root: Path = REPO_ROOT) -> StepResult:
    refused = _repo_only(root, "engine.m1.cross_world")
    if refused:
        return refused
    from engine.m1.cross_world import new_defects, run_all

    findings = run_all()
    new = new_defects(findings)
    mine = [f for f in new if f.scope == code]
    others = len(new) - len(mine)
    hard = [f"{f.key}: {f.message}" for f in mine]
    return StepResult(hard, [f"cross-world: {len(mine)} new defect(s) for {code}, {others} for other scopes (not blocking)"])


def step_holdings(code: str, root: Path = REPO_ROOT) -> StepResult:
    from engine.m9.holdings import DISPOSITIONS, HoldingsError, holdings_for

    try:
        rows = holdings_for(code, root)
    except HoldingsError as exc:
        return StepResult([str(exc)], [])
    counts = {d: sum(1 for r in rows if r["disposition"] == d) for d in DISPOSITIONS}
    parts = ", ".join(f"{d} {n}" for d, n in counts.items() if n)
    return StepResult([], [f"holdings: {len(rows)} vendored file(s): {parts}"])


# (name, step, needs records/<code>/): the holdings report runs for a new world
# before any records exist; the compile and the gates cannot.
STEPS: tuple[tuple[str, Callable[[str, Path], StepResult], bool], ...] = (
    ("prereview-build", step_build, True),
    ("prereview-bar-screen", step_bar_screen, True),
    ("prereview-cross-world", step_cross_world, True),
    ("prereview-holdings", step_holdings, False),
)


def brief_path(code: str, doc: int | None, root: Path = REPO_ROOT) -> Path:
    """Where the output is saved for the review brief."""
    suffix = "" if doc is None else "_Step0" if doc == 0 else f"_Doc{doc}"
    return world_dir(code, root) / "build" / f"{code}_Prereview{suffix}.txt"


def run_prereview(code: str, doc: int | None = None, root: Path = REPO_ROOT, steps=None) -> list[Report]:
    steps = STEPS if steps is None else steps
    where = f"records/worlds/{code}.yaml"
    if registry_entry(code, root) is None:
        return [Report("prereview", [Finding(where, "prereview-registry", "registry entry does not exist")])]
    reports: list[Report] = []
    if doc is not None:
        label = "Step 0" if doc == 0 else f"Doc_{doc:02d}"
        if doc not in DOCUMENTS:
            reports.append(Report("prereview-document", [Finding(rel(world_dir(code, root), root), "prereview-document", f"--doc {doc} names no document; use 0 for Step 0 or 1 to 10")]))
        elif document_path(code, doc, root) is None:
            reports.append(Report("prereview-document", [Finding(rel(world_dir(code, root), root), "prereview-document", f"no {label} file found under Build/worlds/{code}/")]))
        else:
            reports.append(Report("prereview-document", notes=[f"{label} file: {rel(document_path(code, doc, root), root)}"]))
        if reports[-1].findings:
            reports.append(Report("prereview-later-steps", notes=["stopped at prereview-document: later steps not run"], skipped=True))
            return reports
    has_records = (root / "records" / code).is_dir()
    for name, step, needs_records in steps:
        if needs_records and not has_records:
            reports.append(Report(name, notes=[f"skipped: records/{code}/ does not exist yet"], skipped=True))
            continue
        try:
            result = step(code, root)
        except Exception as exc:  # noqa: BLE001 - a crash in a step is a hard failure of that step
            result = StepResult([f"{type(exc).__name__}: {exc}"], [])
        reports.append(Report(name, [Finding(where, name, reason) for reason in result.hard], result.summary))
        if result.hard:
            reports.append(Report("prereview-later-steps", notes=[f"stopped at {name}: later steps not run"], skipped=True))
            break
    return reports
