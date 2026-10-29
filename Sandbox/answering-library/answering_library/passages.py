"""Cutting a division into passages of roughly 150 to 400 words at sentence
boundaries. A passage is a run of whole-space-delimited tokens, so its text is
the source text with whitespace normalised and nothing else changed."""
from __future__ import annotations

import re
from dataclasses import dataclass

MIN_WORDS = 150
MAX_WORDS = 400

_TOKEN = re.compile(r"\S+")
_CLOSERS = "\"'”’»)]›"
_END_CHARS = ".?!…"
_ABBREVIATIONS = frozenset("""
st mr mrs dr vs viz cf ibid id op cit loc no nos vol vols p pp ch chap cap caps lib lat gr ep hom serm ps ev
joh matt mt mk lk jn rom cor gal eph phil col thess tim tit heb jas pet rev gen ex exod lev num deut josh judg
sam kgs chr neh prov eccl isa jer ezek hos art can sess fol ff ed eds tr transl etc ca circ ult
Ep Sr Fr Br Ven Rt Hon
""".lower().split())
_ROMAN = re.compile(r"^[ivxlcdm]+$", re.I)


@dataclass
class Cut:
    first: int
    last: int


def token_spans(text: str, start: int, end: int) -> list[tuple[int, int]]:
    return [(start + m.start(), start + m.end()) for m in _TOKEN.finditer(text[start:end])]


def _core(token: str) -> str:
    return token.rstrip(_CLOSERS).rstrip(_END_CHARS).rstrip(_CLOSERS)


def strengths(words: list[str], script: str) -> list[int]:
    """2 after a sentence end, 1 after a clause mark, 0 elsewhere."""
    n = len(words)
    out = [0] * n
    for i, w in enumerate(words):
        stripped = w.rstrip(_CLOSERS)
        if not stripped:
            continue
        last = stripped[-1]
        if last in "?!…":
            out[i] = 2
            continue
        if script == "Grek" and last in ";;":
            out[i] = 2
            continue
        if last == ".":
            core = stripped.rstrip(".")
            low = core.lower().strip("([\"'“‘«")
            if not core or low in _ABBREVIATIONS or (len(core) <= 2 and core[:1].isalpha() and core[:1].isupper()):
                continue
            if core.isdigit() or (_ROMAN.match(core) and core.isupper() and len(core) <= 4):
                nxt = words[i + 1] if i + 1 < n else ""
                if nxt[:1].islower():
                    continue
            if core.isupper() and len(core) <= 3:
                continue
            nxt = words[i + 1] if i + 1 < n else "A"
            first = nxt.lstrip("([\"'“‘«¿¡")[:1]
            if first.islower():
                if script in ("Latn", "Grek") and len(core) >= 4:
                    out[i] = 2
                continue
            out[i] = 2
            continue
        if last in ",;:··":
            out[i] = 1
    return out


def cut_points(n: int, flags: list[int], low: int = MIN_WORDS, high: int = MAX_WORDS) -> list[int]:
    """End indices (exclusive) of each passage over n tokens."""
    if n <= high:
        return [n]
    k = -(-n // high)
    cuts: list[int] = []
    prev = 0
    for i in range(1, k):
        ideal = round(n * i / k)
        remaining_cuts = k - i
        lo = max(prev + low, n - remaining_cuts * high)
        hi = min(prev + high, n - remaining_cuts * low)
        if lo > hi:
            lo, hi = max(prev + 1, min(lo, hi)), max(prev + 1, max(lo, hi))
            hi = min(hi, n - 1)
        pick = None
        for level in (2, 1, 0):
            best = None
            for b in range(lo, hi + 1):
                if b - 1 < n and flags[b - 1] >= level:
                    d = abs(b - ideal)
                    if best is None or d < best[0]:
                        best = (d, b)
            if best:
                pick = best[1]
                break
        if pick is None:
            pick = min(max(ideal, prev + 1), n - 1)
        cuts.append(pick)
        prev = pick
    cuts.append(n)
    return cuts
