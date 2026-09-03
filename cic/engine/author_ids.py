#!/usr/bin/env python3
"""Validator for cic/corpus-map/AUTHOR-IDS.yaml.

WHY A SEPARATE SCRIPT, NOT FOLDED INTO works_registry.py. Different data
shape (a flat slug -> {wikidata, viaf} map, not a list of Works with
expressions and items) and a different validation question (does this
external id look well-formed, not does this item address resolve to a
real file) - matches this project's one-script-per-registry convention
(texts_registry.py, corpus_map.py, works_registry.py each own one file).

WHAT THIS CHECKS. Format sanity only: a Wikidata id matches Q<digits>, a
VIAF id is numeric. It does NOT check that the id actually identifies the
right person - that would mean calling out to Wikidata/VIAF, which this
script does not do, the same limitation works_registry.py's own docstring
states for CPG/CPL/Wikidata fields there. A wrong-but-well-formed id
(Q174929 attached to the wrong author) is not something format
validation can ever catch.

Usage:
  python cic/engine/author_ids.py            # report
  python cic/engine/author_ids.py --check    # exit 1 on any problem
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
AUTHOR_IDS_FILE = REPO_ROOT / "cic" / "corpus-map" / "AUTHOR-IDS.yaml"

_WIKIDATA = re.compile(r"^Q[1-9]\d*$")
_VIAF = re.compile(r"^\d+$")


def load() -> dict:
    return yaml.safe_load(AUTHOR_IDS_FILE.read_text(encoding="utf-8")) or {}


def problems(data: dict) -> list[str]:
    out = []
    authors = data.get("authors") or {}
    for slug, ids in authors.items():
        if not ids or not (ids.get("wikidata") or ids.get("viaf")):
            out.append(f"{slug}: no identifiers at all - remove the row rather than leave it empty")
            continue
        wd = ids.get("wikidata")
        if wd is not None and not _WIKIDATA.match(str(wd)):
            out.append(f"{slug}: wikidata {wd!r} does not match the Q<digits> form")
        viaf = ids.get("viaf")
        if viaf is not None and not _VIAF.match(str(viaf)):
            out.append(f"{slug}: viaf {viaf!r} is not purely numeric")
    return out


def report() -> int:
    data = load()
    authors = data.get("authors") or {}
    print(f"{len(authors)} author(s) in AUTHOR-IDS.yaml")
    for slug, ids in authors.items():
        print(f"  {slug}: wikidata={ids.get('wikidata')}, viaf={ids.get('viaf')}")

    probs = problems(data)
    if probs:
        print(f"\n{len(probs)} problem(s):")
        for p in probs:
            print(f"  - {p}")
        return 1
    print("\nOK: every entry has at least one identifier, in a well-formed shape.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.parse_args()
    return report()


if __name__ == "__main__":
    sys.exit(main())
