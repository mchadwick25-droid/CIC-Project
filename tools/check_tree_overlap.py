"""Check new Church Family Tree briefs against the stories already on the tree.

Brief-Kit/Kit.md, Part 3, step 4. Run it over a batch's briefs before review:

    python tools/check_tree_overlap.py <brief.txt> [<brief.txt> ...]

A brief is `<slug>.brief.txt`; the census entry with that id is its own story
and is not compared. Two things are listed:

  SHARED QUOTE   a quoted span of five words or more that another story on the
                 tree, or another brief in the batch, already quotes
  SPELLING       a capitalized name that is not used anywhere on the tree but is
                 close to one that is, such as "Lothar" beside "Chlothar"

A quote the slate allows to be used again (Mark's ruling, Decision-Log
2026-11-21: where its author or subject influenced more than one tradition or
person, and it does a new job here) is listed in a file given with --allow, one
per line as `<slug>: <quote>`, and is reported as ALLOWED REUSE.

It exits 1 when any quote is shared and not allowed. A spelling line is for a person to check:
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


def read_allow(path) -> dict[str, set[str]]:
    """slug -> folded quotes the slate allows that brief to reuse."""
    allow: dict[str, set[str]] = {}
    if path is None:
        return allow
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        slug, quote = line.split(":", 1)
        allow.setdefault(slug.strip(), set()).add(fold(quote.strip().strip('"“”')))
    return allow


def allowed(fq: str, permitted: set[str]) -> bool:
    return any(fq == a or fq in a or a in fq for a in permitted if a)


def check(briefs: dict[str, str], census: dict, allow: dict[str, set[str]] | None = None) -> dict:
    """briefs: slug -> text. Returns shared quotes and spelling lines per slug."""
    others = stories(census)
    for slug, text in briefs.items():
        others[slug] = text
    known = tree_names(census)
    candidates = {fold(k): k for k in known if len(k) >= MIN_NAME_LEN}
    result = {}
    for slug, text in briefs.items():
        shared, reused = [], []
        for q in quotes_in(text):
            fq = fold(q)
            hits = sorted(sid for sid, body in others.items() if sid != slug and fq in fold(body))
            if hits:
                (reused if allowed(fq, (allow or {}).get(slug, set())) else shared).append({"quote": q, "in": hits})
        spelling = []
        for n in sorted(names_in(text)):
            if len(n) < MIN_NAME_LEN or n in known:
                continue
            close = difflib.get_close_matches(fold(n), list(candidates), n=3, cutoff=CLOSE)
            if close:
                spelling.append({"name": n, "tree": sorted(candidates[c] for c in close)})
        result[slug] = {"shared": shared, "reused": reused, "spelling": spelling}
    return result


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("briefs", nargs="+", type=Path)
    ap.add_argument("--census", type=Path, default=CENSUS)
    ap.add_argument("--allow", type=Path, help="the slate's allowed reuses, one `<slug>: <quote>` per line")
    args = ap.parse_args(argv)
    census = json.loads(args.census.read_text(encoding="utf-8"))
    briefs = {p.name.removesuffix(".brief.txt"): p.read_text(encoding="utf-8") for p in args.briefs}
    result = check(briefs, census, read_allow(args.allow))
    failed = False
    for slug, r in result.items():
        for s in r["shared"]:
            failed = True
            print(f"{slug}: SHARED QUOTE \"{s['quote']}\" also in {', '.join(s['in'])}")
        for s in r["reused"]:
            print(f"{slug}: ALLOWED REUSE \"{s['quote']}\" also in {', '.join(s['in'])}")
        for s in r["spelling"]:
            print(f"{slug}: SPELLING {s['name']} (the tree has {', '.join(s['tree'])})")
        if not r["shared"] and not r["reused"] and not r["spelling"]:
            print(f"{slug}: clear")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
