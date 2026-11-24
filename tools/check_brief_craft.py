"""List the sentences in a Church Family Tree brief that a reviewer must look at.

The kit's Part 1 names the faults; this lists where each may sit, so none is
missed by hand (Brief-Kit/Kit.md, Part 4, step 4). It judges nothing: the
writer and reviewer clear each line. It runs locally and calls no model.

    python tools/check_brief_craft.py <brief.txt> [<brief.txt> ...]
    python tools/check_brief_craft.py --json <brief.txt> ...
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MAX_WORDS = 30

CHECKS: dict[str, re.Pattern[str]] = {
    "dash": re.compile(r"—|–|\s-\s"),
    "not X but Y": re.compile(r"\bnot\b[^.;:!?]{1,60}?,?\s+but\b", re.I),
    "stock word": re.compile(
        r"\b(?:legacy|profound(?:ly)?|testament|tapestry|enduring|remarkabl[ey]|"
        r"pivotal|indelible|timeless|resonat\w*)\b",
        re.I,
    ),
    "silence sentence": re.compile(
        r"\b(?:do(?:es)? not (?:say|tell|record|name)|did not (?:say|record)|"
        r"(?:we|no one) (?:do(?:es)? not|cannot|can't) know|is not known|unknown|"
        r"(?:are|is|were|was) silent|no (?:record|source) (?:says|tells|survives))\b",
        re.I,
    ),
    "modern-scholar word": re.compile(
        r"\b(?:modern|scholars?|scholarship|editors?|translators?|historians?)\b", re.I
    ),
    "names a source": re.compile(
        r"\b(?:says|said|writes|wrote that|records|recorded that|reports|according to|"
        r"tells us|claims|credits)\b",
        re.I,
    ),
    "possible bare statement": re.compile(
        r"\b(?:wrote (?:a|his|her|their|several|many)|preached|was arrested|"
        r"(?:was|were) (?:accused|condemned|exiled|banished|deposed|excommunicated)|"
        r"accused (?:him|her|them)|heres(?:y|ies)|heretics?|"
        r"(?:his|her|their) (?:ideas|teachings?|views|reforms|works)|controversy|dispute)\b",
        re.I,
    ),
}

SENTENCE = re.compile(r"(?<=[.!?])[\"”’']?\s+(?=[\"“‘']?[A-Z0-9])")


def sentences(text: str) -> list[str]:
    return [s.strip() for s in SENTENCE.split(" ".join(text.split())) if s.strip()]


def check_text(text: str) -> list[dict[str, object]]:
    found: list[dict[str, object]] = []
    sents = sentences(text)
    for i, s in enumerate(sents, 1):
        for name, pat in CHECKS.items():
            if pat.search(s):
                found.append({"sentence": i, "check": name, "text": s})
        words = len(s.split())
        if words > MAX_WORDS:
            found.append({"sentence": i, "check": f"over {MAX_WORDS} words ({words})", "text": s})
        if s.endswith("?") and i < len(sents):
            found.append({"sentence": i, "check": "question", "text": s})
    return found


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    report = {p: check_text(Path(p).read_text(encoding="utf-8")) for p in args.paths}
    if args.json:
        json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0
    for path, items in report.items():
        print(f"{path}: {len(items)} to look at")
        for it in items:
            print(f"  s{it['sentence']:>3}  {it['check']:<24} {it['text']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
