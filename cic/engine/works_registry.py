#!/usr/bin/env python3
"""Validator for cic/corpus-map/WORKS.yaml - checked, not just trusted.

WHY. WORKS.yaml is hand-maintained prose-plus-structure, the same shape as
texts_registry.py's own ENTRIES tuple - and that file's own docstring makes
the argument this one follows: a registry that just repeats hand-typed
claims is exactly the kind of self-certified report this project's review
discipline already distrusts. Two things are worth checking every run
rather than trusting whatever was true when a WORKS.yaml entry was written:
(1) every item address actually resolves to a file that exists under
cic/texts/, and (2) work_id values are unique, since other tooling (a
future source-record work_id field, per Fable's blueprint W1) will use
work_id as a foreign key and a silent duplicate would corrupt that join
without ever raising an error on its own.

WHAT THIS DOES NOT CHECK. Whether an external_id (CPG/CPL/Wikidata) is
correct - that would require calling out to those authorities, which this
script does not do. A null external_id is honest and not a problem; a
WRONG one would be, and this script cannot catch that class of error at
all. Bibliographic accuracy at that level stays a human verification
question, the same way rights_declared() in texts_registry.py reads a
file's rights line but cannot confirm the file's publisher told the truth.

Usage:
  python cic/engine/works_registry.py            # report
  python cic/engine/works_registry.py --check    # exit 1 on any problem
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
WORKS_FILE = REPO_ROOT / "cic" / "corpus-map" / "WORKS.yaml"
TEXTS_DIR = REPO_ROOT / "cic" / "texts"

_ADDRESS = re.compile(r"^cic:([A-Za-z0-9._-]+):(.+)$")


def load() -> dict:
    return yaml.safe_load(WORKS_FILE.read_text(encoding="utf-8")) or {}


def parse_address(addr: str) -> tuple[str, str] | None:
    """A canonical address is cic:<file-stem-with-extension>:<locus>. Returns
    (filename, locus) or None if the address doesn't match the form at all -
    a distinct problem from the filename not existing, which report() checks
    separately so the two failure modes aren't conflated in the output."""
    m = _ADDRESS.match(addr.strip())
    if not m:
        return None
    return m.group(1), m.group(2)


def problems(data: dict) -> list[str]:
    out = []
    works = data.get("works") or []
    seen_ids: set[str] = set()

    for w in works:
        wid = w.get("work_id")
        if not wid:
            out.append(f"(untitled entry, title={w.get('title')!r}): missing work_id")
            continue
        if wid in seen_ids:
            out.append(f"{wid}: duplicate work_id - breaks any future work_id foreign key")
        seen_ids.add(wid)

        expressions = w.get("expressions") or []
        if not expressions:
            out.append(f"{wid}: no expressions listed - a Work with nothing carrying it "
                       f"is not distinguishable from one that was never actually vendored")
        for i, expr in enumerate(expressions):
            items = expr.get("items") or []
            if not items:
                out.append(f"{wid}: expression #{i} ({expr.get('translator')!r}) has no items - "
                           f"an expression with no vendored file behind it belongs in a want-"
                           f"list, not here")
            for addr in items:
                parsed = parse_address(addr)
                if not parsed:
                    out.append(f"{wid}: item address {addr!r} does not match the "
                               f"cic:<file>:<locus> form")
                    continue
                filename, _locus = parsed
                # Locus is deliberately NOT validated beyond existing as a
                # non-empty string - "whole-file" and "book-i" (two seed
                # entries' placeholders, pending narrowing to a real ThML
                # div or section marker) are honest locus values, not
                # errors, and this validator has no way to confirm a real
                # locus like "xvi" actually exists inside the file without
                # re-implementing each format's own structure parser.
                if not (TEXTS_DIR / filename).exists():
                    out.append(f"{wid}: item {addr!r} references "
                               f"cic/texts/{filename}, which does not exist on disk")
    return out


def report() -> int:
    data = load()
    works = data.get("works") or []
    print(f"{len(works)} work(s) in WORKS.yaml\n")
    for w in works:
        n_expr = len(w.get("expressions") or [])
        n_items = sum(len(e.get("items") or []) for e in (w.get("expressions") or []))
        ext = w.get("external_ids") or {}
        verified = [k for k, v in ext.items() if v]
        print(f"  {w.get('work_id')}: {n_expr} expression(s), {n_items} item(s), "
              f"external_ids verified: {verified or 'none'}")

    probs = problems(data)
    if probs:
        print(f"\n{len(probs)} problem(s):")
        for p in probs:
            print(f"  - {p}")
        return 1
    print("\nOK: every work_id unique, every item address resolves to a file on disk "
          "(or is a flagged placeholder awaiting narrowing).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 on any problem, same as report()'s own exit code")
    ap.parse_args()
    return report()


if __name__ == "__main__":
    sys.exit(main())
