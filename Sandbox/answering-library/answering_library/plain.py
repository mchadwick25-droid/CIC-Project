"""Division scheme for a plain-text file: which marker families describe its
divisions, the divisions they cut, and the evidence for the choice."""
from __future__ import annotations

import re
import statistics
from dataclasses import dataclass, field

from . import markers as mk

OVERSIZE_WORDS = 5000
SUBSPLIT_WORDS = 2500
GOOD_RANGE = (40, OVERSIZE_WORDS)
TINY_WORDS = 30
TOC_RUN = 5
MIN_GOOD_SHARE = 0.15
CAPS_SUBSTANTIVE_WORDS = 60
CAPS_MIN_SUBSTANTIVE = 0.6
FRONT_MAX_WORDS = 3000
PACK_SOFT = 150
PACK_HARD = 600
MAX_FAMILIES = 3
_SENTENCE_FINAL = re.compile(r"[.?!…:;»”’\"')\]]\s*$")


@dataclass
class Division:
    start: int
    end: int
    locus: str
    title: str
    apparatus: bool
    origin: str
    level: int = 0
    words: int = 0
    line_start: int = 0
    line_end: int = 0


@dataclass
class Scheme:
    divisions: list[Division]
    furniture_lines: set[int]
    furniture_kinds: dict[str, int]
    work: str
    families: list[dict] = field(default_factory=list)
    candidates: dict[str, dict] = field(default_factory=dict)
    header_end_char: int = 0
    marker_division_words: list[int] = field(default_factory=list)
    body_words: int = 0
    covered_words: int = 0
    total_words: int = 0
    furniture_words: int = 0


def _prefix(values: list[int]) -> list[int]:
    out = [0]
    for v in values:
        out.append(out[-1] + v)
    return out


def _segment_words(headings: list[mk.Heading], pref: list[int], end_line: int) -> list[int]:
    out = []
    for k, h in enumerate(headings):
        nxt = headings[k + 1].line if k + 1 < len(headings) else end_line
        out.append(pref[nxt] - pref[h.line])
    return out


def _score(words: list[int], total: int) -> tuple[float, float, float]:
    if not total or not words:
        return 0.0, 0.0, 0.0
    good = sum(w for w in words if GOOD_RANGE[0] <= w <= GOOD_RANGE[1])
    over = sum(w for w in words if w > OVERSIZE_WORDS)
    tiny = sum(1 for w in words if w < TINY_WORDS) / len(words)
    return (good - 0.5 * over) / total - 0.3 * tiny, good / total, over / total


def _merge(chosen: list[list[mk.Heading]]) -> list[tuple[int, mk.Heading]]:
    by_line: dict[int, tuple[int, mk.Heading]] = {}
    for rank, headings in enumerate(chosen):
        for h in headings:
            if h.line not in by_line:
                by_line[h.line] = (rank, h)
    return [by_line[k] for k in sorted(by_line)]


def _pack(lines: list[str], pref_words: list[int], start: int, end: int, furniture: set[int]) -> list[tuple[int, int]]:
    """Blocks of consecutive paragraphs, closed at a sentence-final paragraph
    end once they hold PACK_SOFT words, or at PACK_HARD regardless."""
    blocks: list[tuple[int, int]] = []
    block_start = None
    acc = 0
    last_text_line = None
    i = start
    while i < end:
        if lines[i].strip() and i not in furniture:
            if block_start is None:
                block_start = i
            para_start = i
            while i < end and lines[i].strip():
                if i not in furniture:
                    last_text_line = i
                i += 1
            acc += pref_words[i] - pref_words[para_start]
            final = last_text_line is not None and bool(_SENTENCE_FINAL.search(lines[last_text_line]))
            if (acc >= PACK_SOFT and final) or acc >= PACK_HARD:
                blocks.append((block_start, i))
                block_start, acc = None, 0
        else:
            i += 1
    if block_start is not None:
        if blocks and acc < PACK_SOFT // 2:
            blocks[-1] = (blocks[-1][0], end)
        else:
            blocks.append((block_start, end))
    return blocks


def _toc_like(lines: list[str], start: int, end: int) -> bool:
    body = [ln for ln in lines[start:end] if ln.strip()]
    if len(body) < 5:
        return False
    hits = sum(1 for ln in body if mk._TOC_LINE.search(ln) and len(ln.strip()) < 90)
    return hits / len(body) >= 0.5


def analyse(text: str) -> Scheme:
    lines = text.split("\n")
    n = len(lines)
    offsets = [0] * (n + 1)
    pos = 0
    for i, ln in enumerate(lines):
        offsets[i] = pos
        pos += len(ln) + 1
    offsets[n] = len(text)

    h_end = mk.header_end(lines)
    fur = mk.find_furniture(lines, h_end)
    work_lines = [(" " * len(ln) if i in fur.lines else ln) for i, ln in enumerate(lines)]
    work = "\n".join(work_lines)
    word_counts = [len(ln.split()) for ln in work_lines]
    pref = _prefix(word_counts)
    body_total = pref[n] - pref[h_end]

    families = mk.find_headings(lines, h_end, fur.lines)
    candidates: dict[str, dict] = {}
    usable: dict[str, list[mk.Heading]] = {}
    for fam, hs in families.items():
        seq = mk.sequentiality(hs)
        words = _segment_words(hs, pref, n)
        score, good, over = _score(words, body_total)
        numeric = fam != "caps"
        substantive = sum(1 for w in words if w >= CAPS_SUBSTANTIVE_WORDS) / len(words) if words else 0.0
        eligible = len(hs) >= 3 and (seq >= 0.6 if numeric else substantive >= CAPS_MIN_SUBSTANTIVE)
        candidates[fam] = {"n": len(hs), "sequentiality": round(seq, 3), "score": round(score, 3),
                           "good_share": round(good, 3), "oversize_share": round(over, 3), "eligible": eligible,
                           "substantive_share": round(substantive, 3)}
        if eligible:
            usable[fam] = hs

    chosen_names: list[str] = []
    chosen: list[list[mk.Heading]] = []
    best_score = 0.0
    while len(chosen_names) < MAX_FAMILIES and usable:
        best = None
        for fam, hs in usable.items():
            if fam in chosen_names:
                continue
            merged = [h for _, h in _merge(chosen + [hs])]
            sc = _score(_segment_words(merged, pref, n), body_total)[0]
            if best is None or sc > best[0] or (sc == best[0] and len(hs) > len(usable[best[1]])):
                best = (sc, fam)
        if best is None:
            break
        if chosen_names and best[0] - best_score < 0.02:
            break
        chosen_names.append(best[1])
        chosen.append(usable[best[1]])
        best_score = best[0]
    if chosen_names:
        final_words = _segment_words([h for _, h in _merge(chosen)], pref, n)
        if _score(final_words, body_total)[1] < MIN_GOOD_SHARE:
            chosen_names, chosen = [], []

    medians = {}
    for name, hs in zip(chosen_names, chosen):
        ws = _segment_words(hs, pref, n)
        medians[name] = statistics.median(ws) if ws else 0
    order = sorted(range(len(chosen_names)), key=lambda i: -medians[chosen_names[i]])
    chosen_names = [chosen_names[i] for i in order]
    chosen = [chosen[i] for i in order]

    divisions: list[Division] = []

    def make(a: int, b: int, locus: str, title: str, apparatus: bool, origin: str, level: int = 0) -> Division:
        return Division(offsets[a], offsets[b] if b < n else len(text), locus, title, apparatus, origin,
                        level, pref[b] - pref[a], a, b)

    if h_end > 0:
        divisions.append(make(0, h_end, "header", "", True, "header"))

    merged = _merge(chosen)
    if merged:
        first_line = merged[0][1].line
        if first_line > h_end and pref[first_line] - pref[h_end] > 0:
            divisions.append(make(h_end, first_line, "front", "", pref[first_line] - pref[h_end] <= FRONT_MAX_WORDS, "front"))
        stack: list[str] = []
        marker_divs: list[Division] = []
        for k, (rank, h) in enumerate(merged):
            nxt_line = merged[k + 1][1].line if k + 1 < len(merged) else n
            del stack[rank:]
            while len(stack) < rank:
                stack.append("")
            stack.append(h.label)
            locus = "/".join(p for p in stack if p)
            apparatus = bool(mk.APPARATUS_HEADING.match(h.title)) or _toc_like(lines, h.line, nxt_line)
            marker_divs.append(make(h.line, nxt_line, locus, h.title, apparatus, "marker", rank))
        run = 0
        for idx, d in enumerate(marker_divs):
            run = run + 1 if d.words < TINY_WORDS else 0
            if run == TOC_RUN:
                for back in range(idx - TOC_RUN + 1, idx + 1):
                    marker_divs[back].apparatus = True
            elif run > TOC_RUN:
                d.apparatus = True
        divisions.extend(marker_divs)
        marker_words = [d.words for d in marker_divs]
        final: list[Division] = []
        for d in divisions:
            if d.origin in ("marker", "front") and d.words > SUBSPLIT_WORDS:
                for (a, b) in _pack(lines, pref, d.line_start, d.line_end, fur.lines):
                    final.append(make(a, b, f"{d.locus}/line{a + 1}", d.title, d.apparatus, "sub", d.level))
            else:
                final.append(d)
        divisions = final
    else:
        marker_words = []
        for (a, b) in _pack(lines, pref, h_end, n, fur.lines):
            divisions.append(make(a, b, f"line{a + 1}", "", False, "pack"))

    covered = sum(marker_words)
    return Scheme(
        divisions=divisions, furniture_lines=fur.lines, furniture_kinds=fur.kinds, work=work,
        families=[{"family": name, "n": len(hs), "sequentiality": candidates[name]["sequentiality"]}
                  for name, hs in zip(chosen_names, chosen)],
        candidates=candidates, header_end_char=offsets[h_end], marker_division_words=marker_words,
        body_words=body_total, covered_words=covered, total_words=pref[n],
        furniture_words=sum(len(lines[i].split()) for i in fur.lines),
    )


def pack_chars(text: str, start: int, end: int) -> list[tuple[int, int]]:
    """Paragraph-pack blocks over text[start:end] as character ranges."""
    seg_lines = text[start:end].split("\n")
    offsets = []
    pos = start
    for ln in seg_lines:
        offsets.append(pos)
        pos += len(ln) + 1
    offsets.append(end)
    pref = _prefix([len(ln.split()) for ln in seg_lines])
    blocks = _pack(seg_lines, pref, 0, len(seg_lines), set())
    return [(offsets[a], min(offsets[b], end)) for a, b in blocks]
