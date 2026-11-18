"""Check new Church Family Tree briefs against the stories already on the tree.

Brief-Kit/Kit.md, Part 4, step 4. Run it over a batch's briefs before review:

    python tools/check_tree_overlap.py <brief.txt> [<brief.txt> ...]

A brief is `<slug>.brief.txt`; the census entry with that id is its own story
and is not compared. Two things are listed:

  SHARED QUOTE   a quoted span of five words or more that another story on the
                 tree, or another brief in the batch, already quotes
  SPELLING       a capitalized name that is not used anywhere on the tree but is
                 close to one that is, such as "Lothar" beside "Chlothar"

It exits 1 when any quote is shared. A spelling line is for a person to check:
a close name can be a different person.
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

CENSUS = Path("cic-website/data/world-census.json")
QUOTE = re.compile(r'["“]([^"“”]+)["”]')
NAME = re.compile(r"\b[A-Z][a-zà-ÿ]+(?:-[A-Z][a-zà-ÿ]+)?\b")
MIN_QUOTE_WORDS = 5
MIN_NAME_LEN = 5
CLOSE = 0.8


def fold(s: str) -> str:
    """The census validator's fold: accents, case and punctuation aside."""
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()
    s = s.replace("æ", "ae").replace("œ", "oe")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def quotes_in(text: str) -> list[str]:
    return [q for q in (m.group(1) for m in QUOTE.finditer(text)) if len(fold(q).split()) >= MIN_QUOTE_WORDS]


def names_in(text: str) -> set[str]:
    return {re.sub(r"'s$", "", n) for n in NAME.findall(text.replace("’", "'"))}


def stories(census: dict) -> dict[str, str]:
    """Each census entry's story and card quotations, keyed by id."""
    out = {}
    for m in census.get("movements", []):
        parts = [m.get("longDescription") or ""]
        card = m.get("card") or {}
        parts += [q.get("modern", "") for q in card.get("quotationOriginals", [])]
        out[m["id"]] = "\n".join(p for p in parts if p)
    return out


def tree_names(census: dict) -> set[str]:
    names = set()
    for m in census.get("movements", []):
        for k in ("name", "shortName", "informalName", "longDescription"):
            names |= names_in(m.get(k) or "")
    return names


def check(briefs: dict[str, str], census: dict) -> dict:
    """briefs: slug -> text. Returns shared quotes and spelling lines per slug."""
    others = stories(census)
    for slug, text in briefs.items():
        others[slug] = text
    known = tree_names(census)
    candidates = {fold(k): k for k in known if len(k) >= MIN_NAME_LEN}
    result = {}
    for slug, text in briefs.items():
        shared = []
        for q in quotes_in(text):
            fq = fold(q)
            hits = sorted(sid for sid, body in others.items() if sid != slug and fq in fold(body))
            if hits:
                shared.append({"quote": q, "in": hits})
        spelling = []
        for n in sorted(names_in(text)):
            if len(n) < MIN_NAME_LEN or n in known:
                continue
            close = difflib.get_close_matches(fold(n), list(candidates), n=3, cutoff=CLOSE)
            if close:
                spelling.append({"name": n, "tree": sorted(candidates[c] for c in close)})
        result[slug] = {"shared": shared, "spelling": spelling}
    return result


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("briefs", nargs="+", type=Path)
    ap.add_argument("--census", type=Path, default=CENSUS)
    args = ap.parse_args(argv)
    census = json.loads(args.census.read_text(encoding="utf-8"))
    briefs = {p.name.removesuffix(".brief.txt"): p.read_text(encoding="utf-8") for p in args.briefs}
    result = check(briefs, census)
    failed = False
    for slug, r in result.items():
        for s in r["shared"]:
            failed = True
            print(f"{slug}: SHARED QUOTE \"{s['quote']}\" also in {', '.join(s['in'])}")
        for s in r["spelling"]:
            print(f"{slug}: SPELLING {s['name']} (the tree has {', '.join(s['tree'])})")
        if not r["shared"] and not r["spelling"]:
            print(f"{slug}: clear")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
