#!/usr/bin/env python3
"""The zero-crossover gate for the clean system.

Rule: no EXECUTABLE reference under cic/ may reach outside cic/ into the
old tree. Python and config files are checked for old-tree path strings;
a hit fails the build. Record bodies (.md front matter + prose) are
exempt for one declared reason: provenance citations to archived build
documents are historical data - the scholarly audit trail - not live
references, and scrubbing them would destroy information. Nothing
executes them.

Run: python cic/checks/isolation.py    (exit 0 = isolated)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # cic/

# Path fragments that mean the old tree. A match in any executable file
# under cic/ is a crossover.
FORBIDDEN = (
    "cic-poc",
    "World-Builds",
    "wrs/",
    "wrs.",
    "s62_",
    "Syriac-Build",
    "L0-Reference", "L1-", "L2-", "L3-Governance", "L4-Templates",
    "Ministry/",
    "Project-Reference",
    "backend/data",
)

CHECKED_SUFFIXES = {".py", ".json", ".yaml", ".yml", ".toml", ".cfg", ".ini",
                    ".ts", ".tsx", ".js", ".sh"}


def main() -> int:
    failures = []
    deploy = ROOT / "deploy"
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix not in CHECKED_SUFFIXES:
            continue
        if p == Path(__file__).resolve():
            continue  # this file names the forbidden strings on purpose
        if deploy in p.parents and p.suffix == ".json":
            # generated data views serialize record fields, and record
            # provenance prose (exempt by declared rule) flows into them;
            # nothing executes these files
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for token in FORBIDDEN:
            if token in text:
                line = next((i + 1 for i, ln in enumerate(text.splitlines())
                             if token in ln), 0)
                failures.append(f"{p.relative_to(ROOT.parent)}:{line}: "
                                f"references old tree ({token!r})")
    for f in failures:
        print(f"  CROSSOVER: {f}")
    n = sum(1 for p in ROOT.rglob('*') if p.is_file())
    print(f"isolation: {'FAIL' if failures else 'PASS'} "
          f"({n} files under cic/, {len(failures)} crossover(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
