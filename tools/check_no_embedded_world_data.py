#!/usr/bin/env python3
"""Fail when a NEW embedded-world-data anti-pattern appears in cic-website.

Website V2 world_front design (approved to proceed 2026-09-19): every
participant-facing site surface should be generated from records/<code>/
via the compiler (engine.m2.site_compiler), fetching its data at runtime -
never a data blob embedded directly in the page's own <script> block,
which is how cic-website/atlas-v3.html works today and the exact
duplication-without-a-single-source-of-truth this whole design exists to
retire (see this repo's CLAUDE.md and the two live fabrication fixes,
commits fbb6557/763c48d, this design's own motivating cases).

atlas-v3.html's own migration is a separate, later stage (this pass is
infrastructure only) - so this check does not fail on that ALREADY-
existing instance. It fails only on a NEW file adopting the same
anti-pattern, via a baseline of already-known offenders (the same
baseline/allowlist shape as tools/check_paths.py).

Usage:
  check_no_embedded_world_data.py                     report every offending
                                                        file not in the
                                                        baseline, exit 1 if any
  check_no_embedded_world_data.py --baseline FILE      use FILE instead of the
                                                        default baseline
  check_no_embedded_world_data.py --write-baseline FILE
                                                        record the current set
                                                        as the accepted baseline
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent if HERE.name == "tools" else Path.cwd()
DEFAULT_BASELINE = HERE / "embedded-world-data-baseline.txt"

# A top-level SCREAMING_SNAKE_CASE const assigned an object or array
# literal, inside a <script> block - the exact shape atlas-v3.html's own
# `const DATA = { ... }` takes. Deliberately narrow to this one
# recognizable pattern rather than "any JS object literal": an ordinary
# lowercase config constant is not what this check exists to catch, and
# a broader pattern would drown real findings in noise the same way
# several engine/m1/gates.py patterns' own comments already warn against.
_EMBEDDED_DATA_RE = re.compile(r"^\s*const\s+[A-Z][A-Z0-9_]*\s*=\s*[\{\[]", re.MULTILINE)


def offending_files() -> set[str]:
    hits: set[str] = set()
    for path in (REPO / "cic-website").rglob("*.html"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if _EMBEDDED_DATA_RE.search(text):
            hits.add(path.relative_to(REPO).as_posix())
    return hits


def load_baseline(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--write-baseline", type=Path)
    args = parser.parse_args(argv)

    found = offending_files()

    if args.write_baseline:
        args.write_baseline.write_text(
            "\n".join(sorted(found)) + ("\n" if found else ""), encoding="utf-8"
        )
        print(f"wrote {len(found)} entries to {args.write_baseline}")
        return 0

    baseline = load_baseline(args.baseline)
    new_offenders = sorted(found - baseline)
    stale_baseline_entries = sorted(baseline - found)

    if new_offenders:
        print("New embedded-world-data anti-pattern found (not in the accepted baseline):")
        for f in new_offenders:
            print(f"  {f}")
        print(
            "\nParticipant-facing site data belongs in records/<code>/ (world_front), "
            "compiled by engine.m2.site_compiler, fetched at runtime - not embedded "
            "directly in a page's own <script> block."
        )
    if stale_baseline_entries:
        print("Baseline entries that no longer offend (safe to remove from the baseline):")
        for f in stale_baseline_entries:
            print(f"  {f}")

    return 1 if new_offenders else 0


if __name__ == "__main__":
    sys.exit(main())
