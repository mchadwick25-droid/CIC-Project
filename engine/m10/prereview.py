"""The pre-review bundle (check c): compile and gate battery, bar screen,
cross-world check, holdings report, in that order, stopping at the first hard
failure."""
from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .common import REPO_ROOT, Finding, Report, registry_entry, world_dir

FK_CEILING = 10.0
PACKAGE_ID = "prereview"


@dataclass
class StepResult:
    hard: list[str]
    summary: list[str]


def _git_head() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def step_build(code: str) -> StepResult:
    """Compile the world exactly as `engine.m2.cli build` does, without writing
    a package, and read the M1 gate battery from the compiled gates report."""
    from engine.m2.compiler import compile_world

    head = _git_head()
    package = compile_world(world_key=code, package_id=PACKAGE_ID, records_commit=head, compiler_version=head)
    gates = json.loads(package["validation/gates-report.json"])["gates"]
    failing = {name: g["findings"] for name, g in gates.items() if not g["pass"]}
    hard = [f"gate {name}: {len(fs)} finding(s), first: {fs[0]}" for name, fs in failing.items()]
    return StepResult(hard, [f"m2 build: {len(gates)} gate(s), {len(failing)} failing"])


def step_bar_screen(code: str) -> StepResult:
    from engine.m1.bar_screen import screen_world

    report = screen_world(code)
    fields = report["fields"]
    over = [f"{k}: fk max {v['fk_grade_max']} in {v['worst_record']}" for k, v in fields.items() if (v["fk_grade_max"] or 0) > FK_CEILING]
    lines = [f"bar screen: {len(fields)} voice-diet field(s), {len(over)} over FK {FK_CEILING:g}"] + [f"  over ceiling, {o}" for o in over]
    return StepResult([], lines)


def step_cross_world(code: str) -> StepResult:
    from engine.m1.cross_world import new_defects, run_all

    findings = run_all()
    new = new_defects(findings)
    mine = [f for f in new if f.scope == code]
    others = len(new) - len(mine)
    hard = [f"{f.key}: {f.message}" for f in mine]
    return StepResult(hard, [f"cross-world: {len(mine)} new defect(s) for {code}, {others} for other scopes (not blocking)"])


def step_holdings(code: str) -> StepResult:
    from engine.m9.holdings import DISPOSITIONS, holdings_for

    rows = holdings_for(code)
    counts = {d: sum(1 for r in rows if r["disposition"] == d) for d in DISPOSITIONS}
    parts = ", ".join(f"{d} {n}" for d, n in counts.items() if n)
    return StepResult([], [f"holdings: {len(rows)} vendored file(s): {parts}"])


STEPS: tuple[tuple[str, Callable[[str], StepResult]], ...] = (
    ("prereview-build", step_build),
    ("prereview-bar-screen", step_bar_screen),
    ("prereview-cross-world", step_cross_world),
    ("prereview-holdings", step_holdings),
)


def run_prereview(code: str, doc: int | None = None, root: Path = REPO_ROOT, steps=None) -> list[Report]:
    steps = STEPS if steps is None else steps
    where = f"records/worlds/{code}.yaml"
    if registry_entry(code, root) is None:
        return [Report("prereview", [Finding(where, "prereview-registry", "registry entry does not exist")])]
    reports: list[Report] = []
    if doc is not None and not any(re.match(rf"(?:{re.escape(code)}_)?Doc_?0*{doc}(?!\d)", p.name) for p in world_dir(code, root).glob("*.md")):
        reports.append(Report("prereview-document", notes=[f"no Doc_{doc:02d} file found under Build/worlds/{code}/"]))
    has_records = (root / "records" / code).is_dir()
    for name, step in steps:
        if not has_records:
            reports.append(Report(name, notes=[f"skipped: records/{code}/ does not exist yet"], skipped=True))
            continue
        try:
            result = step(code)
        except Exception as exc:  # noqa: BLE001 - a crash in a step is a hard failure of that step
            result = StepResult([f"{type(exc).__name__}: {exc}"], [])
        reports.append(Report(name, [Finding(where, name, reason) for reason in result.hard], result.summary))
        if result.hard:
            reports.append(Report("prereview-later-steps", notes=[f"stopped at {name}: later steps not run"], skipped=True))
            break
    return reports
