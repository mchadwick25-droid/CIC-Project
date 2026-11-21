#!/usr/bin/env python3
"""Fail if an entry number repeats in an append-only numbered log.

.gitattributes merges the Church Family Tree logs with merge=union, so two
branches that each append an entry merge without a conflict. Both branches may
have taken the same next number; the merge keeps both lines. This check catches
that. Gaps in the numbering are allowed; repeats are not.
"""
import collections
import re
import sys

LOGS = ["Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md"]


def repeated(text):
    numbers = [int(m.group(1)) for m in re.finditer(r"^(\d+)\. ", text, re.M)]
    return sorted(n for n, c in collections.Counter(numbers).items() if c > 1)


def main(paths):
    failed = False
    for path in paths:
        with open(path, encoding="utf-8") as f:
            dupes = repeated(f.read())
        if dupes:
            failed = True
            print(f"{path}: entry numbers used twice: {dupes}. Renumber the newer entry.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or LOGS))
