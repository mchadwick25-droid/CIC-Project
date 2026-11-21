"""List the quoted spans in a Church Family Tree brief and the card entry that holds each.

Brief-Kit/Kit.md, Part 4, step 7. Run it on each piece's folder once its brief and card are final:

    python tools/list_second_readings.py <piece folder> [<piece folder> ...]

A folder named for its slug holds `<slug>.brief.txt` and `<slug>.card.json`. A quotation the brief
breaks around "he says" is one card entry, so up to four spans in a row may make
one entry, as in tools/validate-census.mjs. Each span gets one line:

  READ BLIND     six words or more, and no card entry holds it, or its entry has
                 no secondReading yet
  CHECK AT CARD  under six words (the whole entry's words, where spans make one
                 entry), and its entry has no secondReading yet: the card checker
                 checks it against its original and print, and it carries
                 "checked at card"
  CARRIED        its entry holds a secondReading (an earlier blind verdict, kept
                 only when the span stands word for word in a passage already read,
                 or "checked at card")

Card entries the brief no longer quotes are listed as STALE. It exits 1 when any
span needs a blind reading or a card check, or any entry is stale.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

QUOTE = re.compile(r'["“]([^"“”]+)["”]')
BLIND_MIN_WORDS = 6  # Decision-Log 2026-11-21, "Kit change order: reused quotes, fewer blind readings"


def fold(s: str) -> str:
    """The census validator's fold: accents, case and punctuation aside."""
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()
    s = s.replace("æ", "ae").replace("œ", "oe")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def spans_in(brief: str) -> list[str]:
    return [m.group(1) for m in QUOTE.finditer(brief)]


def entries_of(card: dict) -> list[dict]:
    out = list(card.get("quotationOriginals") or [])
    for s in card.get("documentedStories") or []:
        out += list((s or {}).get("quotationOriginals") or [])
    return out


def needs(folded_words: str) -> str:
    return "READ BLIND" if len(folded_words.split()) >= BLIND_MIN_WORDS else "CHECK AT CARD"


def listing(brief: str, card: dict) -> dict:
    spans = spans_in(brief)
    folded = [fold(s) for s in spans]
    entries = entries_of(card)
    by_modern = {fold(e.get("modern", "")): e for e in entries if e.get("modern")}
    rows, used, i = [], set(), 0
    while i < len(spans):
        for k in (4, 3, 2, 1):
            run = " ".join(folded[i:i + k])
            if i + k <= len(spans) and run in by_modern:
                e = by_modern[run]
                used.add(run)
                verdict = e.get("secondReading")
                rows.append({"span": " ... ".join(spans[i:i + k]), "status": "CARRIED" if verdict else needs(run),
                             "secondReading": verdict})
                i += k
                break
        else:
            rows.append({"span": spans[i], "status": needs(folded[i]), "secondReading": None})
            i += 1
    stale = [e["modern"] for e in entries if e.get("modern") and fold(e["modern"]) not in used]
    return {"spans": rows, "stale": stale}


def piece(folder: Path) -> tuple[Path, Path]:
    brief, card = folder / f"{folder.name}.brief.txt", folder / f"{folder.name}.card.json"
    for p in (brief, card):
        if not p.exists():
            raise SystemExit(f"{folder}: no {p.name}")
    return brief, card


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folders", nargs="+", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    result, bad = {}, False
    for folder in args.folders:
        b, c = piece(folder)
        r = listing(b.read_text(encoding="utf-8"), json.loads(c.read_text(encoding="utf-8")))
        result[folder.name] = r
        bad |= bool(r["stale"]) or any(s["status"] != "CARRIED" for s in r["spans"])
    if args.json:
        print(json.dumps(result, indent=1, ensure_ascii=False))
    else:
        for name, r in result.items():
            print(f"{name}: {len(r['spans'])} spans")
            for s in r["spans"]:
                v = f" ({s['secondReading']})" if s["secondReading"] else ""
                print(f"  {s['status']:<13}{v} {s['span']}")
            for m in r["stale"]:
                print(f"  STALE         {m}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
