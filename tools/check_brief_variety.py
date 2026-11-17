"""Count the story moves that repeat across a batch of Church Family Tree briefs.

A move found in more than a quarter of the batch goes back to the writers of
those pieces (Brief-Kit/Process.md, step 4). Run it over the whole batch:

    python tools/check_brief_variety.py <brief.txt> [<brief.txt> ...]
    python tools/check_brief_variety.py --json <brief.txt> ...

It prints each move with the pieces that make it, and exits 1 when any move is
over its share.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SHARE = 0.25

# Opening: an unnamed scene, then the name revealed ("The soldier was Martin", "He was Benedict").
REVEAL = re.compile(
    r"(?:^|[.!?][\"\u201d']?\s+)(?:(?:(?:That|The|His|Her|Their)\s+(?:[a-z]+\s+){0,2}(?:was|were)"
    r"|(?:He|She|They)\s+(?:was|were))\s+(?:the\s+)?[A-Z][a-z]+"
    r"|This was (?:the \w+ century|[A-Z][a-z]+))"
)
# Setting: a time or place tag, the kind writers stack in one sentence.
TAG = re.compile(
    r"\b(?:(?:[Ii]n|[Aa]t|[Ff]rom)\s+(?:the\s+)?(?:\w+(?:th|st|nd|rd)[- ]century|\d{3,4}s?\b|what is now|today's|[A-Z][a-z]+)"
    r"|(?:[Aa]round|[Aa]bout) the year \d+|\w+(?:th|st|nd|rd)-century|[Tt]his was (?:the \w+ century|[A-Z][a-z]+))"
)
NOW = re.compile(r"\bin (?:what is now|today's)\b")
# Witness: the stock formula that opens the sourcing line.
WITNESS = re.compile(
    r"\b(?:Most of what we know|(?:Almost|Nearly) (?:all|everything) (?:that )?we know|Everything we know|All (?:that )?we know)\b"
)
# Ending: the last paragraph turns to a later writer or institution.
LATER = re.compile(
    r"\b(?:\w+ (?:centuries|century|generations?|years) (?:later|after|on)|later (?:writers?|historians?|councils?|scholars?)"
    r"|in the \w+(?:th|st|nd|rd) century|(?:in|by) \d{3,4}\b|\d{3,4}s\b|afterwards?)",
)

MOVES = {
    "reveal": "an unnamed opening, then the name revealed",
    "stacked-setting": "a setting slot (a time and a place stacked in one early sentence, or \"in what is now\" more than once)",
    "witness-formula": "the \"Most of what we know\" witness formula",
    "yet-pivot": "a sentence opening with \"Yet\"",
    "later-ending": "an ending on a later writer or institution (a later time marker in the last two paragraphs)",
}


def sentences(text: str) -> list[str]:
    out = []
    for para in re.split(r"\n\s*\n", text):
        out += re.split(r"(?<=[.!?])\s+|(?<=[.!?][\"\u201d'])\s+", para.strip())
    return [s for s in out if s.strip()]


TIME = re.compile(r"century|\d{3,4}|[Tt]his was the")
PLACE = re.compile(r"(?:[Ii]n|[Aa]t|[Ff]rom)\s+(?:the\s+)?[A-Z]|what is now|today's|[Tt]his was [A-Z]")


def stacked(tags: list[str]) -> bool:
    """A setting slot: a time and a place stacked in one sentence ("in the fourth century, in Roman Gaul")."""
    return len(tags) >= 2 and any(TIME.search(t) for t in tags) and any(PLACE.search(t) for t in tags)


def moves_in(text: str) -> set[str]:
    """The repeating moves one brief makes."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    found = set()
    opening = " ".join(paras[:2])
    if REVEAL.search(opening):
        found.add("reveal")
    sents = sentences(text)
    early = sents[: max(3, len(sents) * 2 // 5)]  # setting lines live in the first part of the story
    if any(stacked(TAG.findall(s)) for s in early) or len(NOW.findall(text)) > 1:
        found.add("stacked-setting")
    if WITNESS.search(text):
        found.add("witness-formula")
    if any(s.startswith("Yet ") for s in sentences(text)):
        found.add("yet-pivot")
    if paras and LATER.search(" ".join(paras[-2:])):
        found.add("later-ending")
    return found


def check(paths: list[Path]) -> dict:
    pieces = {p.name.split(".")[0]: moves_in(p.read_text(encoding="utf-8")) for p in paths}
    limit = int(len(pieces) * SHARE)
    report = {}
    for move in MOVES:
        who = sorted(k for k, v in pieces.items() if move in v)
        report[move] = {"count": len(who), "pieces": who, "over": len(who) > limit}
    return {"batch": len(pieces), "limit": limit, "moves": report}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("briefs", nargs="+", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    result = check(args.briefs)
    if args.json:
        print(json.dumps(result, indent=1))
    else:
        print(f"{result['batch']} briefs; a move in more than {result['limit']} goes back to its writers")
        for move, r in result["moves"].items():
            mark = "OVER" if r["over"] else "ok  "
            print(f"{mark} {r['count']:>2}  {MOVES[move]}: {', '.join(r['pieces']) or '-'}")
    return 1 if any(r["over"] for r in result["moves"].values()) else 0


if __name__ == "__main__":
    sys.exit(main())
