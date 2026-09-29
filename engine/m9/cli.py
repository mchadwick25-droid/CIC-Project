"""Thin CLI over the pure confinement battery, same shape as
engine/m2/cli.py and engine/m1/selftest.py's own entry points. `check`
(the CI-blocking command, Q3, increment 4) runs both gate batteries
against the real fleet and fails on anything engine/m9/enforce.py's
ACCEPTED_OPEN doesn't already know about.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from engine.m1.loader import load_world_records
from engine.m1.registry import load_registry
from engine.m4.grounding_net import _normalize, _quoted_spans

from .confinement import run_all
from .holdings import report as holdings_report
from .loader import load_shelf, read_complement_units
from .shelf import Shelf

REPO_ROOT = Path(__file__).resolve().parents[2]
_EDITION_PATH = re.compile(r"cic/texts/([\w\-]+\.(?:txt|xml))")

# Duplicated from engine/m1/gates.py::_PERSPECTIVE_FIELDS rather than
# imported - engine/m9/ imports nothing from gates.py's internals and
# gates.py imports nothing from engine/m9/ (confinement.py's own
# _EDITION_PATH comment explains why this boundary stays duplicated
# rather than crossed for one small constant).
_PERSPECTIVE_FIELDS = {
    "term": ["plain_meaning", "quick_meaning"],
    "story": ["tellable_as", "text"],
    "ambient": ["detail"],
    "doctrinal_witness": ["text"],
    "honest_limit": ["statement"],
}


def _shelf_for(world_key: str) -> tuple[Shelf, dict]:
    registry = load_registry()
    entry = registry.get(world_key)
    if entry is None:
        raise SystemExit(f"{world_key!r} is not in the registry")
    census_id = entry.get("census_id")
    if not census_id:
        raise SystemExit(f"{world_key!r} has no census_id - nothing to build a shelf from")
    records = load_world_records(world_key)
    shelf = load_shelf(world_key=world_key, census_id=census_id, records=records)
    return shelf, records


def _off_shelf_reads(records: dict, shelf: Shelf) -> list[dict]:
    """Report-only: every kind: absence record whose named file this world's
    own bucket doesn't claim - the off-shelf reads Q5 licenses at build
    time, named here so they're logged, not hidden (D3 SS1.4's own
    absence-probe row)."""
    reads = []
    for rid, rec in records.items():
        if rec.get("record_type") != "source" or rec.get("kind") != "absence":
            continue
        m = _EDITION_PATH.search(str(rec.get("edition") or ""))
        if not m:
            continue
        filename = m.group(1)
        reads.append({"record": rid, "file": filename, "on_shelf": filename in shelf.files})
    return reads


def _perspective_spans(records: dict) -> list[tuple[str, str, str]]:
    """(record_id, field, quoted span) for every quoted span in every
    voice-prose field _PERSPECTIVE_FIELDS names, plus a demonstration
    record's own exchange[].text where speaker: representative - the exact
    population Q7-I5 scored (`gate_voice_perspective`'s own scoping,
    duplicated above)."""
    out = []
    for rid, rec in records.items():
        rt = rec.get("record_type")
        texts = [(f, rec.get(f)) for f in _PERSPECTIVE_FIELDS.get(rt, [])]
        if rt == "demonstration":
            for i, turn in enumerate(rec.get("exchange") or []):
                if turn.get("speaker") == "representative":
                    texts.append((f"exchange[{i}].text", turn.get("text")))
        for field, text in texts:
            if not isinstance(text, str) or not text.strip():
                continue
            for span in _quoted_spans(text):
                out.append((rid, field, span))
    return out


def _window_match(span: str, haystacks: list[str], *, window_words: int = 6) -> bool:
    words = _normalize(span).split()
    if not words:
        return False
    windows = (
        [" ".join(words)]
        if len(words) <= window_words
        else [" ".join(words[i : i + window_words]) for i in range(len(words) - window_words + 1)]
    )
    return any(w in h for h in haystacks for w in windows)


def _complement_verbatim(records: dict, shelf: Shelf, complement_units: dict[str, str]) -> list[dict]:
    """Report-only (increment 10, Q7-I5): every quoted span in the world's
    own voice-prose that verbatim window-matches somewhere in the
    complement (every vendored file off this world's own shelf) and does
    NOT also window-match anywhere on the world's own shelf. A hit here is
    not a failure to act on - Q7-I5 read all 13 real fleet-wide hits by
    hand and found only generic-phrase coincidence or an
    already-honestly-sourced paraphrase, never actual cross-tradition
    borrowing - it is a pointer for a human to read the same way, kept
    running as the sharp half of that measurement's own instrument (the
    ratio half measured near-inert and is deliberately not reimplemented
    here)."""
    if not complement_units:
        return []
    # One combined haystack per side (Q7-I5's own measured-fast shape,
    # ~30ms per window search even at ~114MB) rather than a per-file list -
    # checking hundreds of quoted spans against ~90 separate haystacks one
    # file at a time is the combinatorial blowup Q7-I5's own methodology
    # section warns a naive sweep hits (tens of minutes per world).
    shelf_haystack = [_normalize("\x00".join(shelf.units.values()))]
    complement_haystack = [_normalize("\x00".join(complement_units.values()))]
    hits = []
    for rid, field, span in _perspective_spans(records):
        if not _window_match(span, complement_haystack):
            continue
        if _window_match(span, shelf_haystack):
            continue  # explainable from the world's own shelf - not a complement leak
        hits.append({"record": rid, "field": field, "span": span[:150]})
    return hits


def cmd_report(args: argparse.Namespace) -> int:
    shelf, records = _shelf_for(args.world_key)
    findings = run_all(records, shelf)
    total = sum(len(v) for v in findings.values())
    complement_units = read_complement_units(shelf)
    print(json.dumps({
        "world": args.world_key,
        "census_id": shelf.census_id,
        "clean": total == 0,
        "findings": findings,
        "off_shelf_reads": _off_shelf_reads(records, shelf),
        "complement_verbatim": _complement_verbatim(records, shelf, complement_units),
    }, indent=2))
    return 0


def _render_shelf_table(world_key: str, shelf: Shelf) -> str:
    """Same shape tools/gen_shelf.py's own render() produces - increment 9
    points that tool's own SHELF.md output at this instead and retires its
    line-regex bucket reader."""
    by_role: dict[str, int] = {}
    for row in shelf.rows.values():
        by_role[row.get("role") or "?"] = by_role.get(row.get("role") or "?", 0) + 1
    lines = [
        f"# Shelf — `{world_key}`",
        "",
        f"Tradition: `{shelf.census_id}` · {len(shelf.rows)} works · "
        + " · ".join(f"{r}: {n}" for r, n in sorted(by_role.items())),
        "",
        "Generated by `python -m engine.m9.cli shelf`. Do not edit; regenerate. Roles: "
        "`tradition` is this world's own voice and may be voiced; `context`, `antecedent` "
        "and `transmission` may be cited as evidence, and are voiceable only when a "
        "documented-exchange row says so (CM-8).",
        "",
        "| work | author | file | locus | role | confidence | voice_of | documented_exchange |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in sorted(shelf.rows.values(), key=lambda r: (r.get("role") or "", r.get("author") or "", r.get("work") or "")):
        lines.append(
            f"| {row.get('work', '')} | `{row.get('author', '')}` | `{row.get('source_file', '')}` | "
            f"{row.get('locus', '')} | {row.get('role', '')} | {row.get('confidence', '')} | "
            f"{row.get('voice_of') or ''} | {row.get('documented_exchange') or ''} |"
        )
    return "\n".join(lines) + "\n"


def cmd_shelf(args: argparse.Namespace) -> int:
    shelf, _records = _shelf_for(args.world_key)
    text = _render_shelf_table(args.world_key, shelf)
    if args.stdout:
        print(text)
        return 0
    target_dir = REPO_ROOT / "Build" / "worlds" / args.world_key
    if not target_dir.is_dir():
        print(f"{args.world_key}: no {target_dir.relative_to(REPO_ROOT)}/ yet - printing instead", file=sys.stderr)
        print(text)
        return 0
    (target_dir / "SHELF.md").write_text(text, encoding="utf-8")
    print(f"{args.world_key}: {target_dir.relative_to(REPO_ROOT)}/SHELF.md — {len(shelf.rows)} works")
    return 0


def cmd_holdings(args: argparse.Namespace) -> int:
    print(holdings_report(args.world_key))
    return 0


def cmd_selftest(args: argparse.Namespace) -> int:
    from . import selftest

    return selftest.main()


def cmd_check(args: argparse.Namespace) -> int:
    from . import enforce

    return enforce.main()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m engine.m9.cli")
    sub = parser.add_subparsers(dest="command", required=True)

    report = sub.add_parser("report", help="build one world's shelf, run the confinement battery, print findings")
    report.add_argument("world_key")
    report.set_defaults(func=cmd_report)

    shelf = sub.add_parser("shelf", help="render one world's SHELF.md table from its real, computed shelf")
    shelf.add_argument("world_key")
    shelf.add_argument("--stdout", action="store_true", help="print instead of writing Build/worlds/<code>/SHELF.md")
    shelf.set_defaults(func=cmd_shelf)

    holdings_p = sub.add_parser("holdings", help="one row per vendored file for a world: in_scope, named_in_records, drawn_on, disposition (Stage 2d, Build-Plan.md; report-only)")
    holdings_p.add_argument("world_key")
    holdings_p.set_defaults(func=cmd_holdings)

    selftest_p = sub.add_parser("selftest", help="M1-selftest-shaped proof: the clean fixture is clean, every seeded M9 defect fires its named check")
    selftest_p.set_defaults(func=cmd_selftest)

    check_p = sub.add_parser("check", help="the CI-blocking gate: both batteries against the real fleet, fails on anything ACCEPTED_OPEN doesn't waive")
    check_p.set_defaults(func=cmd_check)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
