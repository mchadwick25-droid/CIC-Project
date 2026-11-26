"""Fail a pull request that changes the Church Family Tree writing standard
without Mark's words in a new Decision-Log entry.

Locked: everything under Brief-Kit/ (the kit and the
role prompts), everything under Stage-Two-Kit/ and everything under Who-Profiles/bar/, all in
Build/Ministry/Features/Church-Family-Tree/. A change to any of them passes
only when the same pull request adds an entry to that folder's
Decision-Log.md whose heading or "Decided" line names Mark and which has a
line with a quotation in it.

Usage: python tools/check_standard_lock.py --base origin/main
"""

import argparse
import re
import subprocess
import sys

FOLDER = "Build/Ministry/Features/Church-Family-Tree/"
LOCKED_DIRS = (FOLDER + "Brief-Kit/", FOLDER + "Stage-Two-Kit/", FOLDER + "Who-Profiles/bar/")
DECISION_LOG = FOLDER + "Decision-Log.md"

QUOTATION = re.compile(r"“[^”]*\S[^”]*”|\"[^\"]*\S[^\"]*\"")
DECIDED = re.compile(r"^\*\*Decided\b")


def locked(paths):
    return sorted(p for p in paths if p.startswith(LOCKED_DIRS))


def added_entries(diff_text):
    """Each Decision-Log entry the diff adds, as its added lines, heading first."""
    entries, current = [], None
    for line in diff_text.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue
        if line.startswith("@@"):
            current = None
            continue
        if not line.startswith("+"):
            current = None
            continue
        text = line[1:]
        if text.startswith("## "):
            current = [text]
            entries.append(current)
        elif current is not None:
            current.append(text)
    return entries


def entry_ok(entry):
    heading, body = entry[0], entry[1:]
    names_mark = "Mark" in heading or any(DECIDED.match(l) and "Mark" in l for l in body)
    quotes = any(QUOTATION.search(l) for l in entry)
    return names_mark and quotes


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def check(base):
    merge_base = git("merge-base", base, "HEAD").strip()
    changed = git("diff", "--name-only", merge_base, "HEAD").split()
    hits = locked(changed)
    if not hits:
        print("No locked standard file changed.")
        return 0
    diff = git("diff", "-U0", merge_base, "HEAD", "--", DECISION_LOG)
    if any(entry_ok(e) for e in added_entries(diff)):
        print("Locked standard files changed, with a new Decision-Log entry carrying Mark's words:")
        for p in hits:
            print("  " + p)
        return 0
    print("FAIL: this pull request changes the locked writing standard:")
    for p in hits:
        print("  " + p)
    print(
        "It needs a new entry in " + DECISION_LOG + " whose heading or **Decided** line "
        "names Mark and which quotes his words."
    )
    return 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base", required=True, help="the branch the pull request merges into, e.g. origin/main")
    return check(ap.parse_args(argv).base)


if __name__ == "__main__":
    sys.exit(main())
