#!/usr/bin/env python3
"""cic-website/data/corpus-coverage.json — the Atlas-facing join between
the census and the corpus map: for every one of its Atlas entries, which
vendored primary-source works corpus-map has actually assigned to it.

WHY, AND WHY NOW (2026-09-02, Mark's sign-off). The blueprint's own framing:
"a generated cic-website/data/corpus-coverage.json is a pure join... That is
the 'known sources for not-yet-built movements' surface, and it is honest by
construction: an entry with zero vendored works shows zero." The mechanism
was always safe (corpus-map's bucket filename IS the census id - the join
key already exists); what needed a ruling was SCOPE, since this is a public,
live feed (cic-website/, not an internal doc) and the two obvious ways to
build it differ in how honest the result reads:

Mark's ruling: VENDORED COVERAGE ONLY, across all census entries, including
the doctrinally-excluded ones that already carry vendored primary texts
(showing them is not an endorsement - the entry's own excluded status and
floor note already carry that context in the same Atlas modal). Explicitly
NOT included: the acquirable-PD/purchasable/no-edition-exists "wanted"
categorization world-build-docs/_cross-world/WANTS-REGISTER.md carries -
that data is reactive, generated only from records/ that already exist,
which today means it only has real content for the 7 already-built formation
worlds. Showing real bibliographic depth on 7 entries and nothing on the
other 285 "wanted" slots would read as an arbitrary gap to a site visitor,
not as a real signal - worse than the flat, honest "zero" this feed gives
instead. If census-wide want-tracking is ever built, joining it in here is a
one-line addition, not a redesign.

WHAT THIS DOES NOT DO. It does not touch atlas-v3.html's rendering - the
Atlas already has an obvious slot for this ("Sources to research", the
existing per-entry bibliography panel), but which panel, what copy, and how
it reads alongside the existing sources[] field is a front-end/UX decision,
not a data-mechanism one. This script only produces the join; wiring it into
the page is separate work.

Usage:
  python cic/engine/corpus_coverage.py            # write corpus-coverage.json
  python cic/engine/corpus_coverage.py --print     # to stdout instead
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
CENSUS = REPO_ROOT / "cic-website" / "data" / "world-census.json"
TARGET = REPO_ROOT / "cic-website" / "data" / "corpus-coverage.json"

sys.path.insert(0, str(HERE))
import corpus_map  # noqa: E402  (reuses load() - buckets, and its atlas_id-is-filename join)
import texts_registry as tr  # noqa: E402  (reuses read_header/rights_declared - never re-read a claim, re-read the file)

_header_cache: dict[str, str] = {}


def rights_for(source_file: str) -> str | None:
    """The vendored file's OWN header, read fresh - same discipline
    texts_registry.py's own report() uses, not a copy of a claim."""
    if source_file not in _header_cache:
        path = tr.TEXTS_DIR / source_file
        _header_cache[source_file] = tr.read_header(path) if path.exists() else ""
    return tr.rights_declared(_header_cache[source_file])


def build() -> dict:
    census = json.loads(CENSUS.read_text(encoding="utf-8"))
    movements = census.get("movements", [])
    buckets = corpus_map.load()  # atlas_id -> {"works": [...]}

    entries = {}
    with_coverage = 0
    for m in movements:
        mid = m["id"]
        bucket = buckets.get(mid) or {}
        works = []
        for w in bucket.get("works") or []:
            source_file = w.get("source_file", "")
            works.append({
                "work": w.get("work", ""),
                "author": w.get("author", ""),
                "role": w.get("role", ""),
                "confidence": w.get("confidence", ""),
                "source_file": source_file,
                "rights": rights_for(source_file) if source_file else None,
            })
        if works:
            with_coverage += 1
        entries[mid] = {
            "name": m.get("name", ""),
            "status": m.get("status", ""),
            "works": works,
        }

    return {
        "generated_by": "cic/engine/corpus_coverage.py",
        "generated_from": [
            "cic/corpus-map/*.yaml (vendored-work assignments)",
            "cic-website/data/world-census.json (entry list)",
            "cic/texts/ (each work's rights line, read fresh from the file)",
        ],
        "scope": "vendored coverage only - see this script's own docstring for why "
                 "the acquirable/purchasable/no-edition-exists breakdown is not included here",
        "counts": {
            "total_entries": len(movements),
            "entries_with_coverage": with_coverage,
            "entries_zero_coverage": len(movements) - with_coverage,
        },
        "entries": entries,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python cic/engine/corpus_coverage.py")
    parser.add_argument("--print", dest="to_stdout", action="store_true")
    args = parser.parse_args(argv)

    data = build()
    text = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n"
    if args.to_stdout:
        print(text)
        return 0
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")
    c = data["counts"]
    print(f"wrote {TARGET.relative_to(REPO_ROOT)}: {c['total_entries']} entries, "
          f"{c['entries_with_coverage']} with vendored coverage, "
          f"{c['entries_zero_coverage']} at zero")
    return 0


if __name__ == "__main__":
    sys.exit(main())
