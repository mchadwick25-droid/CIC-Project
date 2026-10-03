#!/usr/bin/env python3
"""Write the move ledger: one row per old → new path, from the manifest and the git log.

Usage: make_ledger.py MANIFEST OUT.md --phase "Phase 1" --commit SHA [--rewrites N --files M]
The ledger is a supplemental record (P11): the moved files themselves carry no notes.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path


def main(argv):
    manifest, out = Path(argv[0]), Path(argv[1])
    phase = argv[argv.index("--phase") + 1] if "--phase" in argv else "Phase 1"
    commit = argv[argv.index("--commit") + 1] if "--commit" in argv else "(uncommitted)"
    rewrites = argv[argv.index("--rewrites") + 1] if "--rewrites" in argv else "—"
    files = argv[argv.index("--files") + 1] if "--files" in argv else "—"
    rows = []
    for line in manifest.read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip():
            src, dst, kind = line.split("\t")
            rows.append((src, dst, kind))
    header = out.exists()
    with out.open("a", encoding="utf-8") as f:
        if not header:
            f.write("# Repo Structure — Move Ledger\n\n"
                    "Supplemental record of every path moved, renamed, or deleted by the Repo Structure\n"
                    "Cleanup thread. The moved files carry no notes (P11); this ledger and\n"
                    "`Build/Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md` are the record.\n"
                    "Anyone reading a dated document that cites an old path finds the new one here.\n")
        f.write(f"\n## {phase} — {date.today().isoformat()} — commit `{commit}`\n\n")
        f.write(f"Citations rewritten by `Build/tools/rewrite_paths.py`: {rewrites} replacements in {files} files "
                f"(current documents only; `records/`, `Archive/` and dated Ministry history untouched).\n\n")
        f.write("| from | to | kind |\n|---|---|---|\n")
        for src, dst, kind in rows:
            f.write(f"| `{src}` | {'deleted' if dst == 'DELETE' else '`' + dst + '`'} | {kind} |\n")
    print(f"ledger: {len(rows)} rows appended to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
