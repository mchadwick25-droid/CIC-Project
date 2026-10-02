"""Shared plumbing for the build gates: findings, path lookup, output."""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]

PLACEHOLDER = re.compile(r"^\s*(?:|[-—–]+|tbd|todo|n/a|none|<[^>]*>|\[[^\]]*\])\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class Finding:
    path: str
    check: str
    reason: str

    def line(self) -> str:
        return f"{self.path}: {self.check}: {self.reason}"


@dataclass
class Report:
    name: str
    findings: list[Finding] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    skipped: bool = False
    incomplete: bool = False
    accepted: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def passed(self) -> bool:
        """Clean and, when the check is required, actually run."""
        return self.ok and not self.incomplete

    def to_dict(self) -> dict:
        out = {
            "check": self.name,
            "pass": self.ok,
            "skipped": self.skipped,
            "incomplete": self.incomplete,
            "findings": [asdict(f) for f in self.findings],
            "notes": self.notes,
        }
        if self.accepted:
            out["accepted"] = self.accepted
        return out


def emit(reports: list[Report], *, as_json: bool) -> int:
    ok = all(r.passed for r in reports)
    accepted = sum(len(r.accepted) for r in reports)
    if as_json:
        doc = {"pass": ok, "reports": [r.to_dict() for r in reports]}
        if accepted:
            doc["accepted"] = accepted
        print(json.dumps(doc, indent=2))
        return 0 if ok else 1
    for r in reports:
        for f in r.findings:
            print(f.line())
        for a in r.accepted:
            print(a)
    for r in reports:
        for n in r.notes:
            print(f"note: {r.name}: {n}")
    for r in reports:
        status = "INCOMPLETE (a required check did not run)" if r.incomplete else "SKIPPED" if r.skipped else "PASS" if r.ok else f"FAIL ({len(r.findings)} finding(s))"
        print(f"{r.name}: {status}" + (f" ({len(r.accepted)} accepted)" if r.accepted else ""))
    if accepted:
        print(f"accepted by project lead declaration: {accepted}")
    return 0 if ok else 1


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def registry_entry(code: str, root: Path = REPO_ROOT) -> dict | None:
    path = root / "records" / "worlds" / f"{code}.yaml"
    if not path.is_file():
        return None
    return yaml.safe_load(read_text(path)) or {}


def safety_adjacent_status(code: str, entry: dict | None) -> tuple[bool | None, str]:
    """(value, reason). The value is True or False when the registry entry sets
    safety_adjacent; None, with the reason, when the trigger cannot be
    evaluated. A grandfathered world without the field is reported as
    undetermined; a world outside that set must carry it."""
    from engine.m1.registry import SAFETY_ADJACENT_KEY, safety_adjacent
    from engine.m9.enforce import GRANDFATHERED_WORLDS

    if entry is None:
        return None, f"no registry entry records/worlds/{code}.yaml"
    value = safety_adjacent(entry)
    if value is not None:
        return value, ""
    if SAFETY_ADJACENT_KEY in entry:
        return None, f"{SAFETY_ADJACENT_KEY} in records/worlds/{code}.yaml must be true or false, found {entry[SAFETY_ADJACENT_KEY]!r}"
    if code in GRANDFATHERED_WORLDS:
        return None, f"records/worlds/{code}.yaml has no {SAFETY_ADJACENT_KEY} field (grandfathered world: reported until the project lead sets it)"
    return None, f"records/worlds/{code}.yaml has no {SAFETY_ADJACENT_KEY} field; the project lead sets it to true or false at handoff"


def world_dir(code: str, root: Path = REPO_ROOT) -> Path:
    return root / "Build" / "worlds" / code


def review_dirs(code: str, root: Path = REPO_ROOT) -> list[Path]:
    base = world_dir(code, root)
    return [d for d in (base, base / "Review-Artifacts") if d.is_dir()]


def markdown_tables(text: str) -> list[list[list[str]]]:
    """Each table as a list of rows, each row a list of stripped cells; the
    header and separator rows are dropped."""
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue
            current.append(cells)
        elif current:
            tables.append(current[1:])
            current = []
    if current:
        tables.append(current[1:])
    return tables
