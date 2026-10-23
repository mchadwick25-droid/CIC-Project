"""Speaking only from inside the years: find mentions, in text a world's
voice reads, of anything after the world's window closes.

Three kinds of mention count:
- a gazetteer event (engine/m1/data/gazetteer.yaml) or a fleet modern_term
  display term whose year falls after the window's end;
- an explicit year after the window's end, written with an era marker or a
  preposition ("in 641", "AD 641", "641 CE");
- a century that begins after the window's end ("the fifth century" in a
  world that closes in 400).

Used by the M1 horizon gate on records and by the report-only runtime
backstop on replies (engine.m4.output_check).
"""
import re
from functools import lru_cache
from pathlib import Path

import yaml

GAZETTEER_PATH = Path(__file__).resolve().parent / "data" / "gazetteer.yaml"
_LATEST_YEAR = 2100
_ORDINALS = {
    "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eighth": 8,
    "ninth": 9, "tenth": 10, "eleventh": 11, "twelfth": 12, "thirteenth": 13, "fourteenth": 14,
    "fifteenth": 15, "sixteenth": 16, "seventeenth": 17, "eighteenth": 18, "nineteenth": 19, "twentieth": 20,
}
# A number counting something ("about 500 monks") is not a year.
_COUNTED = (
    r"(?!\s*(?:BC|B\.C\.|BCE|B\.C\.E\.|years|copies|people|men|women|miles|monks|nuns|bishops|brothers|sisters"
    r"|letters|pages|lines|verses|times|days|soldiers|martyrs|households|families|villages|churches)\b)"
)
# A range in parentheses names a span of years ("(411-435)"), unless a
# reference stands before it ("Psalms (119-120)", "lines (1954-1958)").
_REFERENCE_BEFORE = re.compile(r"(?:psalms?|lines?|pp?\.|pages?|chapters?|ch\.|sections?|sec\.|verses?|nos?\.)\s*$", re.IGNORECASE)
_ERA_YEAR = re.compile(
    r"\b(?:AD|A\.D\.)\s*(\d{3,4})\b|\b(\d{3,4})\s*(?:AD|A\.D\.|CE|C\.E\.)\b"
    rf"|\b(?:in|by|after|until|from|around|about|circa|c\.)\s+(\d{{3,4}})\b{_COUNTED}"
    r"|\bin\s+the\s+(\d{2,3}0)s\b"
    r"|\((?P<range>\s*(\d{3,4})\s*[-\u2013]\s*\d{2,4}\s*)\)"
    rf"|\b(?:about|around|c\.|circa)\s+(\d{{3,4}})\s*[-\u2013]\s*\d{{2,4}}\b{_COUNTED}",
    re.IGNORECASE,
)
_GROUP_NAMES = [next((n for n, i in _ERA_YEAR.groupindex.items() if i == k), None) for k in range(1, _ERA_YEAR.groups + 1)]
_CENTURY = re.compile(r"\b(" + "|".join(_ORDINALS) + r"|\d{1,2}(?:st|nd|rd|th))[- ]century\b(?!\s*(?:BC|B\.C\.|BCE))", re.IGNORECASE)


@lru_cache(maxsize=1)
def gazetteer() -> tuple[tuple[str, int, re.Pattern], ...]:
    entries = yaml.safe_load(GAZETTEER_PATH.read_text()) or []
    return tuple(
        (e["label"], int(e["year"]), re.compile(r"\b(?:" + "|".join(re.escape(p) for p in e["patterns"]) + r")\b"))
        for e in entries
    )


def dated_terms(fleet: dict) -> list[tuple[str, int, re.Pattern]]:
    """The fleet modern_term records as (label, origin year, pattern)."""
    out = []
    for record in sorted(fleet.values(), key=lambda r: r["id"]):
        if record.get("record_type") == "modern_term" and record.get("origin_year") and record.get("display_terms"):
            pattern = re.compile(r"\b(?:" + "|".join(re.escape(t) for t in record["display_terms"]) + r")\b")
            out.append((f"the modern term '{record['display_terms'][0]}'", int(record["origin_year"]), pattern))
    return out


def _century_number(token: str) -> int:
    return _ORDINALS.get(token.lower()) or int(re.match(r"\d+", token).group())


def post_window_mentions(text: str, window_end: int, terms: list[tuple[str, int, re.Pattern]] = ()) -> list[str]:
    """Each mention in `text` of something after `window_end`, as a short
    description; empty when the text stays inside the window."""
    found = []
    for label, year, pattern in (*gazetteer(), *terms):
        if year > window_end and pattern.search(text):
            found.append(f"{label} ({year})")
    for match in _ERA_YEAR.finditer(text):
        if match.group("range") and _REFERENCE_BEFORE.search(text[: match.start()]):
            continue
        year = int(next(g for name, g in zip(_GROUP_NAMES, match.groups()) if g and name != "range"))
        if window_end < year <= _LATEST_YEAR:
            found.append(f"the year {year}")
    for match in _CENTURY.finditer(text):
        century = _century_number(match.group(1))
        if (century - 1) * 100 + 1 > window_end:
            found.append(f"the {match.group(0).lower()}")
    return list(dict.fromkeys(found))
