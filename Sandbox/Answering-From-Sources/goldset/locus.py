"""Resolves a section reference in a record's locus ("Book II, ch. 3",
"VII.24", "sec. 30", "Letter XXII") to lines of a ThML edition, through the
edition's own division numbering.

It walks down from the work's division, one number per level, matching a
child division by its `n` attribute or by the number leading its title, and
then, for a last number with no division of its own, by a paragraph that
opens with that number. Every step must match exactly one candidate; any
ambiguity, or any number the edition does not carry, returns nothing. A
section is never guessed.
"""
import functools
import html
import re

from goldset.evidence import text_lines

_ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
_DIV = re.compile(r"<div(\d)\b([^>]*)>|</div(\d)>")
_ATTR = re.compile(r'\b(title|n|id)="([^"]*)"')
_NUMBER = r"(?:[0-9]+|[IVXLCivxlc]+)"
_LABELLED = re.compile(
    r"\b(?:book|bk|letter|ep|epistle|demonstration|dem|homily|hom|sermon|oration|or|chapter|ch|cap|canon|section|sec|secs|ss|§|treatise|question|q)\.?\s*"
    rf"({_NUMBER})\b", re.IGNORECASE)
_DOTTED = re.compile(rf"(?<![\w.])({_NUMBER}(?:\.{_NUMBER}){{1,3}})(?![\w.])")
_LEAD = re.compile(rf"^\W*(?:[A-Za-z]+\.?\s+)?({_NUMBER})\b")


def number(token: str) -> int | None:
    token = token.strip().rstrip(".")
    if token.isdigit():
        return int(token)
    letters = token.lower()
    if not letters or any(c not in _ROMAN for c in letters):
        return None
    total = 0
    for a, b in zip(letters, letters[1:] + " "):
        value = _ROMAN[a]
        total += -value if b != " " and _ROMAN.get(b, 0) > value else value
    return total


def path_of(locus: str) -> list[int]:
    """The section numbers a locus names, outermost first, read from its
    opening reference (before any dash or colon that starts a gloss, and
    leaving out anything in parentheses)."""
    head = re.split(r"\s[-–—]+\s|:\s", re.sub(r"\([^)]*\)", " ", locus), maxsplit=1)[0]
    dotted = _DOTTED.search(head)
    if dotted:
        parts = [number(p) for p in dotted.group(1).split(".")]
        return [p for p in parts if p is not None] if all(p is not None for p in parts) else []
    found = [number(m.group(1)) for m in _LABELLED.finditer(head)]
    return [n for n in found if n is not None]


@functools.lru_cache(maxsize=32)
def tree(commit: str, name: str) -> tuple[dict, ...]:
    lines = text_lines(commit, name) or ()
    stack, out = [], []
    for at, line in enumerate(lines, start=1):
        for m in _DIV.finditer(line):
            if m.group(1):
                attrs = dict(_ATTR.findall(m.group(2) or ""))
                stack.append({"level": int(m.group(1)), "start": at, "title": html.unescape(attrs.get("title", "")),
                              "n": attrs.get("n", ""), "id": attrs.get("id", "")})
            elif stack:
                level = int(m.group(3))
                while stack:
                    node = stack.pop()
                    node["end"] = at
                    out.append(node)
                    if node["level"] == level:
                        break
    return tuple(sorted(out, key=lambda d: (d["start"], d["level"])))


def _children(nodes: tuple[dict, ...], parent: dict | None) -> list[dict]:
    inside = [d for d in nodes if parent is None or (d["start"] > parent["start"] and d["end"] <= parent["end"] and d["level"] > parent["level"])]
    if not inside:
        return []
    top = min(d["level"] for d in inside)
    return [d for d in inside if d["level"] == top]


def _numbered(node: dict) -> int | None:
    if node["n"]:
        value = number(node["n"])
        if value is not None:
            return value
    lead = _LEAD.match(node["title"])
    return number(lead.group(1)) if lead else None


def _names(work: str) -> list[set[str]]:
    """The work's names as word sets: the title before any dash or comma
    gloss, and each name given in parentheses ("Vita Antonii (Life of
    Antony)" gives both)."""
    head = re.split(r"\s[-\u2013\u2014]+\s|,", work, maxsplit=1)[0]
    names = [re.sub(r"\([^)]*\)", " ", head)] + re.findall(r"\(([^)]*)\)", head)
    out = []
    for name in names:
        words = {w for w in re.findall(r"[a-z]{4,}", name.lower())}
        if words:
            out.append(words)
    return out


def _work(nodes: tuple[dict, ...], work: str) -> dict | None:
    """The one outermost division whose title holds every word of one of the
    work's names."""
    names = _names(work)
    hits = [d for d in nodes if any(name <= set(re.findall(r"[a-z]{4,}", d["title"].lower())) for name in names)]
    outer = [d for d in hits if not any(o is not d and o["start"] <= d["start"] and o["end"] >= d["end"] for o in hits)]
    return outer[0] if len(outer) == 1 else None


def _paragraph(lines: tuple[str, ...], node: dict, value: int) -> int | None:
    pattern = re.compile(rf"(?:^|>)\s*{value}\.\s")
    hits = [at for at in range(node["start"], node["end"] + 1) if pattern.search(lines[at - 1])]
    return hits[0] if len(hits) == 1 else None


def resolve(commit: str, name: str, locus: str, work: str) -> tuple[int, int] | None:
    """(first line, last line) of the section the locus names, or None."""
    if not name.endswith(".xml"):
        return None
    path = path_of(locus)
    nodes = tree(commit, name)
    lines = text_lines(commit, name) or ()
    if not path or not nodes:
        return None
    scope = _work(nodes, work) if work else None
    if scope is None:
        return None
    for depth, value in enumerate(path):
        matches = [c for c in _children(nodes, scope) if _numbered(c) == value]
        if len(matches) == 1:
            scope = matches[0]
            continue
        if matches or depth != len(path) - 1:
            return None
        at = _paragraph(lines, scope, value)
        if at is None:
            return None
        nxt = _paragraph(lines, scope, value + 1)
        return at, (nxt - 1 if nxt and nxt > at else min(scope["end"], at + 40))
    return scope["start"], scope["end"]
