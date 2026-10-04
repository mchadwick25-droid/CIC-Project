"""After-edit gates: `records` and `regate`.

`records <code> [--freeze]` fails when a world lacks a record type the site
and the facilitator need (world_front, facilitator_brief, search_record) or
its compiled site JSON, at the states the M1 cross-world gate requires them
(admitted, open) or with --freeze, and whenever it cannot produce its
capsule. A world outside the grandfathered set may not carry a waiver for
those types, and may carry any other waiver only with an owning finding and
the project lead's approval. `regate` applies the same waiver rule.

`regate <code> [--base REF]` re-runs the readability gate (FK 10 and FRE 60
hard, FK 8 reported) and the voice-craft budget over the records changed
since the merge-base with REF, and reports the same fields of the whole
world. The scorer is the M1 gate's own (engine.m1.gates.grade_text); this
module holds no thresholds of its own. A field fails when its text is new
or edited and does not clear the gates. A public field left as it was at the
base is reported, not failed: it cannot have regressed.
"""
from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from engine.m1 import cross_world, gates, schemas
from engine.m1.fk import fk_grade
from engine.m1.loader import load_world_records, parse_record_text
from engine.m9.enforce import ACCEPTED_OPEN as M9_ACCEPTED_OPEN
from engine.m9.enforce import GRANDFATHERED_WORLDS, PROJECT_LEAD, new_world_waiver_problem

from .common import REPO_ROOT, Finding, Report, emit, registry_entry

DEFAULT_BASES = ("origin/main", "main", "HEAD")
FRONT_TYPES = ("world_front", "facilitator_brief")
FRONT_PROSE_KEYS = frozenset({"text", "teaser", "note", "hedge"})
FRONT_PROSE_LISTS = frozenset({"cautions"})


@dataclass(frozen=True)
class PublicField:
    rid: str
    record_type: str
    label: str
    text: str
    path: str = ""


def front_prose_checks(rec: dict) -> list[tuple[str, str]]:
    """(label, text) for each authored prose string in a world_front or
    facilitator_brief record. Bare record ids (mode 2), grounding ids, urls,
    dates and titles are not prose and are skipped; mode 2 text is graded as
    the field of the record it renders."""
    found: list[tuple[str, str]] = []

    def walk(node, path: str, key: str | None) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{path}.{k}" if path else k, k)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]", key)
        elif isinstance(node, str) and node.strip():
            if key in FRONT_PROSE_KEYS or key in FRONT_PROSE_LISTS:
                found.append((path, node))

    for field in schemas.TYPE_PROPERTIES.get(rec.get("record_type"), {}):
        if field in rec:
            walk(rec[field], field, field)
    return found


def public_fields(records: dict[str, dict]) -> list[PublicField]:
    """Every field of the world a participant, the model or a facilitator
    reads as prose: the M1 gate's spoken fields, and the front and brief."""
    out: list[PublicField] = []
    for rid, rec in sorted(records.items()):
        record_type = rec.get("record_type")
        pairs = gates._readability_checks(record_type, rec)
        if record_type in FRONT_TYPES:
            pairs = pairs + front_prose_checks(rec)
        seen: dict[str, int] = {}
        for label, text in pairs:
            seen[label] = seen.get(label, 0) + 1
            unique = label if seen[label] == 1 else f"{label}#{seen[label]}"
            out.append(PublicField(rid, record_type, unique, text, rec.get("_path", "")))
    return out


def readability_failures(item: PublicField) -> list[str]:
    graded = gates.grade_text(item.text)
    if graded is None:
        return []
    reasons = []
    if graded["fk"] > gates.FK_CEILING:
        reasons.append(f"FK grade {graded['fk']:.1f}, above the ceiling of {gates.FK_CEILING}")
    if graded["fre"] < gates.FRE_FLOOR:
        reasons.append(f"FRE {graded['fre']:.1f}, below the floor of {gates.FRE_FLOOR}")
    return reasons


def below_band_floor(item: PublicField) -> bool:
    graded = gates.grade_text(item.text)
    return graded is not None and graded["fk"] < gates.FK_FLOOR


def voice_budget(rec: dict) -> dict:
    """{"words", "ceiling", "fk"} for a voice_craft record's prompt text."""
    parts = gates.voice_craft_prompt_parts(rec)
    return {
        "words": sum(len(p.split()) for p in parts),
        "ceiling": gates.voice_craft_word_ceiling(rec),
        "fk": fk_grade(" ".join(p for p in parts if p)),
    }


def voice_budget_failures(head: dict, base: dict | None) -> list[str]:
    """Reasons a voice_craft record fails the budget. Words above the ceiling
    and FK above the ceiling each fail when the record is new, was within the
    limit at the base, or is worse than it was at the base."""
    now = voice_budget(head)
    then = voice_budget(base) if base is not None else None
    reasons = []
    if now["words"] > now["ceiling"] and (then is None or then["words"] <= then["ceiling"] or now["words"] > then["words"]):
        reasons.append(f"identity+guard+flavor_notes+characteristic_concerns total {now['words']} words, above the ceiling of {now['ceiling']}")
    if now["fk"] > gates.FK_CEILING and (then is None or then["fk"] <= gates.FK_CEILING or now["fk"] > then["fk"]):
        reasons.append(f"identity+guard+flavor_notes+characteristic_concerns read at FK grade {now['fk']:.1f}, above the ceiling of {gates.FK_CEILING}")
    return reasons


def _git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


def resolve_merge_base(root: Path, base: str | None) -> str:
    candidates = (base,) if base else DEFAULT_BASES
    last_error = ""
    for ref in candidates:
        try:
            return _git(root, "merge-base", ref, "HEAD").strip()
        except subprocess.CalledProcessError as exc:
            last_error = (exc.stderr or "").strip()
    raise ValueError(f"cannot resolve a base ref from {', '.join(candidates)}: {last_error}")


def record_prefixes(code: str) -> tuple[str, ...]:
    """Every home of the world's records, as repo-relative directory prefixes."""
    return (f"records/{code}/", f"Build/worlds/{code}/surface/", f"Build/worlds/{code}/build/records/")


def changed_record_paths(root: Path, code: str, merge_base: str) -> set[str]:
    """Record files added or edited since the merge-base. A file moved
    without a change to its content is not an edit."""
    prefixes = record_prefixes(code)
    names = []
    for line in _git(root, "diff", "--name-status", "-M", "--diff-filter=ACMR", merge_base, "--", *prefixes).splitlines():
        status, *paths = line.split("\t")
        if status != "R100":
            names.append(paths[-1])
    names += _git(root, "ls-files", "--others", "--exclude-standard", "--", *prefixes).splitlines()
    return {n for n in names if n.endswith(".md") and n.startswith(prefixes)}


def base_records(root: Path, code: str, merge_base: str) -> dict[str, dict]:
    """The world's records as they stood at the merge-base, from every home."""
    out: dict[str, dict] = {}
    for prefix in record_prefixes(code):
        for name in _git(root, "ls-tree", "-r", "--name-only", merge_base, "--", prefix).splitlines():
            if not name.endswith(".md") or name[len(prefix):].count("/") != 1:
                continue
            try:
                rec = parse_record_text(_git(root, "show", f"{merge_base}:{name}"), f"{merge_base}:{name}")
            except ValueError:
                continue
            if rec.get("id"):
                out[rec["id"]] = rec
    return out


def compare_world(head: dict[str, dict], base: dict[str, dict], changed_paths: set[str]) -> tuple[list[Finding], list[str]]:
    findings: list[Finding] = []
    base_texts: dict[str, set[str]] = {}
    for f in public_fields(base):
        base_texts.setdefault(f.rid, set()).add(f.text)
    fields = public_fields(head)
    graded = edited = below_floor = 0
    carried_over: list[str] = []
    for item in fields:
        if gates.grade_text(item.text) is not None:
            graded += 1
        is_edited = item.text not in base_texts.get(item.rid, set())
        reasons = readability_failures(item)
        if is_edited:
            edited += 1
            if below_band_floor(item):
                below_floor += 1
            for reason in reasons:
                findings.append(Finding(item.path or item.rid, "readability", f"{item.rid}: {item.label}: {reason}"))
        elif reasons:
            carried_over.append(f"{item.rid}: {item.label}: {'; '.join(reasons)}: not a regression, already failed at the base and unchanged")
    for rid, rec in sorted(head.items()):
        if rec.get("record_type") != "voice_craft":
            continue
        if rec.get("_path") in changed_paths or rid not in base:
            for reason in voice_budget_failures(rec, base.get(rid)):
                findings.append(Finding(rec.get("_path", rid), "voice-budget", f"{rid}: {reason}"))
    notes = [
        f"{len(fields)} public-facing fields checked, {graded} long enough to grade, {edited} new or edited",
    ]
    if below_floor:
        notes.append(f"{below_floor} edited field(s) below FK {gates.FK_FLOOR} (reported, not failed)")
    notes.extend(carried_over)
    return findings, notes


def run_regate(code: str, base: str | None = None, root: Path = REPO_ROOT) -> Report:
    report = Report(f"regate {code}")
    if registry_entry(code, root) is None:
        report.findings.append(Finding(f"records/worlds/{code}.yaml", "registry", "no registry entry for this world code"))
        return report
    try:
        merge_base = resolve_merge_base(root, base)
        changed = changed_record_paths(root, code, merge_base)
        before = base_records(root, code, merge_base)
    except (ValueError, subprocess.CalledProcessError) as exc:
        report.findings.append(Finding(f"records/{code}", "base", str(exc)))
        return report
    findings, notes = compare_world(load_world_records(code, records_root=root / "records"), before, changed)
    report.findings.extend(findings)
    report.findings.extend(new_world_waiver_findings(code))
    report.notes.extend([f"{len(changed)} record file(s) changed since {merge_base[:10]}", *notes])
    return report


REQUIRED_WAIVER_PREFIXES = ("required-record-type/", "required-site-json/")


def required_type_waivers(code: str) -> list[str]:
    prefixes = (f"required-record-type/{code}/", f"required-site-json/{code}")
    return sorted(k for k in cross_world.ACCEPTED_OPEN if k.startswith(prefixes))


def new_world_waiver_findings(code: str) -> list[Finding]:
    """Waivers on a world outside the grandfathered set, in both waiver
    registries. A required-record-type or site-JSON waiver is never allowed.
    Any other waiver needs an owning finding and the project lead's approval."""
    if code in GRANDFATHERED_WORLDS:
        return []
    path = f"records/{code}"
    out: list[Finding] = []
    for key in sorted(cross_world.ACCEPTED_OPEN):
        if code not in key.split("/")[1:]:
            continue
        if key.startswith(REQUIRED_WAIVER_PREFIXES):
            out.append(Finding(path, "waiver-not-allowed", f"{key}: a world outside the grandfathered set cannot waive a required record type"))
        elif not str(cross_world.ACCEPTED_OPEN[key]).strip():
            out.append(Finding(path, "waiver-not-allowed", f"{key}: a waiver on a world outside the grandfathered set names no owning finding"))
        elif cross_world.ACCEPTED_OPEN_APPROVED_BY.get(key, "").strip() != PROJECT_LEAD:
            out.append(Finding(path, "waiver-not-allowed", f"{key}: a waiver on a world outside the grandfathered set lacks approved_by: {PROJECT_LEAD!r}"))
    for key in sorted(M9_ACCEPTED_OPEN):
        if key.rsplit("/", 1)[-1] != code:
            continue
        problem = new_world_waiver_problem(M9_ACCEPTED_OPEN[key])
        if problem is not None:
            out.append(Finding(path, "waiver-not-allowed", f"{key}: a waiver on a world outside the grandfathered set is not allowed: {problem}"))
    return out


def run_records(code: str, root: Path = REPO_ROOT, *, freeze: bool = False) -> Report:
    report = Report(f"records {code}")
    entry = registry_entry(code, root)
    if entry is None:
        report.findings.append(Finding(f"records/worlds/{code}.yaml", "registry", "no registry entry for this world code"))
        return report
    records = load_world_records(code, records_root=root / "records")
    present = {r.get("record_type") for r in records.values()}
    grandfathered = code in GRANDFATHERED_WORLDS
    waivers = set(required_type_waivers(code))
    path = f"records/{code}"
    state = entry.get("state")
    required_now = freeze or state in cross_world.REQUIRED_TYPES_STATES

    def missing(key: str, reason: str) -> None:
        if key in waivers and grandfathered:
            report.notes.append(f"{key}: waived for a grandfathered world ({reason})")
        else:
            report.findings.append(Finding(path, "required-record-type" if key.startswith("required-record") else "required-site-json", reason))

    if required_now:
        for record_type in cross_world._REQUIRED_ADMITTED_RECORD_TYPES:
            if record_type not in present:
                missing(f"required-record-type/{code}/{record_type}", f"no {record_type} record")
        census_id = entry.get("census_id")
        site_json = root / "cic-website" / "data" / "worlds" / f"{census_id}.json" if census_id else None
        if site_json is None or not site_json.is_file():
            missing(f"required-site-json/{code}", f"no compiled site JSON at cic-website/data/worlds/{census_id or '<no census_id>'}.json")
    else:
        report.notes.append(f"state {state!r}: required record types and the site JSON are checked from {'/'.join(cross_world.REQUIRED_TYPES_STATES)} or with --freeze")
    report.findings.extend(new_world_waiver_findings(code))
    try:
        from engine.m2 import builders

        if not builders.build_capsule(records, entry):
            report.findings.append(Finding(path, "capsule", "the capsule builds empty"))
    except Exception as exc:  # any build failure means the capsule is not producible
        report.findings.append(Finding(path, "capsule", f"the capsule cannot be built: {type(exc).__name__}: {exc}"))
    return report


def add_parser(subparsers) -> None:
    p = subparsers.add_parser("records", help="the world carries every required record type and its site JSON (from admitted, or with --freeze), has no waiver for them, and can build its capsule")
    p.add_argument("world_code")
    p.add_argument("--freeze", action="store_true", help="require the record types and site JSON whatever the world's state")
    p.add_argument("--json", action="store_true", help="print one JSON document instead of lines")
    p.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root to check (default: this repository)")
    p = subparsers.add_parser("regate", help="readability and the voice-craft budget on every new or edited public-facing field since the base ref")
    p.add_argument("world_code")
    p.add_argument("--base", default=None, help="git ref to compare against (default: origin/main, then main, then HEAD)")
    p.add_argument("--json", action="store_true", help="print one JSON document instead of lines")
    p.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root to check (default: this repository)")


def run(args) -> int:
    if args.command == "records":
        return emit([run_records(args.world_code, args.root, freeze=args.freeze)], as_json=args.json)
    return emit([run_regate(args.world_code, args.base, args.root)], as_json=args.json)
