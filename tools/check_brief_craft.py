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

TARGET_WORDS = 30
LIST_PAST = 36  # list only sentences well past the target; a word or two over is never a finding
SHORT_WORDS = 7
SHORT_RUN = 3

PRONOUN = r"(?!(?:He|She|They|It|We|I|You|His|Her|Their|This|That)\b)"
QUOTED = re.compile(r"\"[^\"]*\"|“[^”]*”")

# Checks on the narrator's own words (quotations removed first).
NARRATOR: dict[str, re.Pattern[str]] = {
    "dash": re.compile(r"(?<!\d)[—–](?!\d)|\s-\s"),
    "not X but Y": re.compile(r"\bnot\b[^.;:!?]{1,60}?,?\s+but\b", re.I),
    "stock word": re.compile(r"\b(?:legacy|profound(?:ly)?|testament|tapestry|enduring|remarkabl[ey])\b", re.I),
    "silence sentence": re.compile(
        r"\b(?:do(?:es)? not (?:say|tell|record|name)|did not (?:say|record)|"
        r"(?:we|no one) (?:do(?:es)? not|cannot|can't) know|is not known|unknown|"
        r"(?:are|is|were|was) silent|no (?:record|source) (?:says|tells|survives))\b",
        re.I,
    ),
}
# Checks on the whole sentence.
WHOLE: dict[str, re.Pattern[str]] = {
    "modern-scholar word": re.compile(
        r"\b(?:modern|editors?|translators?|scholarship)\b"
        r"|\b(?:a|an|one|some|many|most|later|recent|other)\s+(?:\w+\s+)?(?:historians?|scholars?)\b"
        r"|\b(?:historians|scholars)\b(?!,?\s+[A-Z])",
        re.I,
    ),
    "names a source": re.compile(
        PRONOUN + r"\b[A-Z][a-z]+(?:\s+of\s+[A-Z][a-z]+)?,?\s+(?:says|said|writes|records|reports|claims|credits)\b"
        r"|\b(?:says|writes|records|reports)\s+" + PRONOUN + r"[A-Z][a-z]+"
        r"|\baccording to\b"
    ),
    "possible bare statement": re.compile(
        r"\b(?:wrote (?:a|his|her|their|several|many)|preached|was arrested|"
        r"(?:was|were) (?:accused|condemned|exiled|banished|deposed|excommunicated)|"
        r"heres(?:y|ies)|heretics?|(?:his|her|their) (?:ideas|teachings?|views|reforms)|controversy|dispute)\b",
        re.I,
    ),
}
EXPLAINED = re.compile(r"\b(?:because|about|over|against|meaning|that is|for teaching|for saying|charging)\b|:", re.I)

SENTENCE = re.compile(r"(?<=[.!?])[\"”’']?\s+(?=[\"“‘']?[A-Z0-9])")


def sentences(text: str) -> list[tuple[str, str]]:
    """Each sentence, with the narrator's own words (quoted spans blanked, even across sentences)."""
    flat = " ".join(text.split())
    own_flat = QUOTED.sub(lambda m: " " * len(m.group(0)), flat)
    out, start = [], 0
    for m in list(SENTENCE.finditer(flat)) + [None]:
        end = m.start() if m else len(flat)
        s, own = flat[start:end].strip(), own_flat[start:end].strip()
        if s:
            out.append((s, own))
        if m:
            start = m.end()
    return out


LABEL = re.compile(r"\b(?:heres(?:y|ies)|heretics?)\b", re.I)


def check_text(text: str) -> list[dict[str, object]]:
    found: list[dict[str, object]] = []
    run = 0
    label_seen = False
    for i, (s, own) in enumerate(sentences(text), 1):
        hits = [n for n, pat in NARRATOR.items() if pat.search(own)]
        hits += [n for n, pat in WHOLE.items() if pat.search(s)]
        if "possible bare statement" in hits:
            only_label = LABEL.search(s) and not WHOLE["possible bare statement"].search(LABEL.sub("", s))
            if EXPLAINED.search(s) or (only_label and label_seen):
                hits.remove("possible bare statement")
        label_seen = label_seen or bool(LABEL.search(s))
        if own.rstrip().endswith("?"):
            hits.append("question")
        words = len(s.split())
        if words > LIST_PAST:
            hits.append(f"well past {TARGET_WORDS} words ({words})")
        run = run + 1 if words <= SHORT_WORDS else 0
        if run == SHORT_RUN:
            hits.append(f"run of {SHORT_RUN} short sentences")
        found += [{"sentence": i, "check": h, "text": s} for h in hits]
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
