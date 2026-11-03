"""Source passages for a record's cited works, with the surrounding division.

A passage is found, in this order, from:
  cited lines   a locus that names lines (`anf02 lines 15211-15218`, `npnf204 line 18744`, `cic/texts/<file>, lines N-M`)
  quoted words  the record's own `text`, searched in the cited work
  work opening  the opening of the work's division, when the locus names neither

The text is the innermost division (ThML `divN`) that holds the anchor, with its path of titles;
when the division is larger than the word cap, the cited lines stay whole and the lines either side
are added alternately until the cap. A file with no divisions gives lines either side of the anchor.
The file comes from the source record's `edition` (`cic/texts/<file>`), the volume named in the
locus, or the source's `external_ids.ccel_volume`.
"""
import bisect
import re
from functools import lru_cache
from pathlib import Path

from engine.m1.quote_verbatim import _ELLIPSIS_RE, _extract_texts_filenames, _segment_pattern

DIVISION_MAX_WORDS = 450
FALLBACK_RADIUS_LINES = 30
MIN_DIVISION_WORDS = 60
OPENING_WORDS = 120
MAX_PASSAGES_PER_RECORD = 3
QUOTE_PROBE_WORDS = 8

_MARKUP = re.compile(r"<[^>]+>")
_DIV_TAG = re.compile(r"<(/?)div([1-7])\b([^>]*)>")
_ATTR_ID = re.compile(r'\bid="([^"]*)"')
_ATTR_TITLE = re.compile(r'\btitle="([^"]*)"')
_LINE_LOCUS = re.compile(r"(?:\b([a-z]+\d+[a-z]*)\s+)?\blines?\s+(\d+)(?:\s*[-–]\s*(\d+))?", re.IGNORECASE)
_LOCUS_FILE = re.compile(r"\(([\w.\-]+\.(?:xml|txt))\)")
_HEADER_RULE = re.compile(r"^\s*_{10,}\s*$")


def texts_dir(texts_root: Path) -> Path:
    return texts_root / "cic" / "texts"


@lru_cache(maxsize=8)
def _load(path: str) -> dict:
    lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    events = []
    for number, line in enumerate(lines, start=1):
        for closing, level, attrs in _DIV_TAG.findall(line):
            ident, title = _ATTR_ID.search(attrs), _ATTR_TITLE.search(attrs)
            events.append((number, bool(closing), int(level), ident.group(1) if ident else None, title.group(1) if title else None))
    stripped = [_MARKUP.sub(" ", line) for line in lines]
    starts, total = [], 0
    for text in stripped:
        starts.append(total)
        total += len(text) + 1
    return {"lines": lines, "events": events, "stripped": stripped, "starts": starts, "joined": "\n".join(stripped)}


def _words(stripped: list[str], first: int, last: int) -> list[str]:
    return " ".join(stripped[first - 1:last]).split()


def _containing(events: list, number: int) -> list[tuple[int, int, str | None, str | None]]:
    """The divisions open at a line, outermost first, as (line, level, id, title)."""
    stack = []
    for line, closing, level, ident, title in events:
        if line > number or (closing and line == number):
            break
        if closing:
            while stack and stack[-1][1] >= level:
                if stack.pop()[1] == level:
                    break
        else:
            stack.append((line, level, ident, title))
    return stack


def _division_end(events: list, start: int, level: int) -> int:
    for line, closing, lvl, _ident, _title in events:
        if closing and lvl == level and line >= start:
            return line
    return start


def _trim(data: dict, first: int, last: int, anchor: tuple[int, int], cap: int) -> tuple[str, int, int, bool]:
    """Lines first..last as text; over the cap, the anchor lines whole and lines either side of them until the cap."""
    stripped = data["stripped"]
    if len(_words(stripped, first, last)) <= cap:
        return " ".join(_words(stripped, first, last)), first, last, False
    lo, hi = max(anchor[0], first), min(anchor[1], last)
    used = len(_words(stripped, lo, hi))
    while used < cap and (lo > first or hi < last):
        if lo > first:
            lo -= 1
            used += len(_words(stripped, lo, lo))
        if used < cap and hi < last:
            hi += 1
            used += len(_words(stripped, hi, hi))
    return " ".join(_words(stripped, lo, hi)), lo, hi, True


def _passage_at(path: Path, anchor: tuple[int, int], cap: int) -> dict | None:
    data = _load(str(path))
    count = len(data["lines"])
    if anchor[0] > count:
        return None
    anchor = (anchor[0], min(anchor[1], count))
    stack = _containing(data["events"], anchor[0])
    while len(stack) > 1 and len(_words(data["stripped"], stack[-1][0], _division_end(data["events"], stack[-1][0], stack[-1][1]))) < MIN_DIVISION_WORDS:
        stack.pop()
    if stack:
        line, level, _ident, _title = stack[-1]
        first, last = line, _division_end(data["events"], line, level)
        path_titles = [t for _l, _lv, _i, t in stack if t]
    else:
        first, last = max(anchor[0] - FALLBACK_RADIUS_LINES, 1), min(anchor[1] + FALLBACK_RADIUS_LINES, count)
        path_titles = []
    text, lo, hi, trimmed = _trim(data, first, max(last, anchor[1]), anchor, cap)
    if not text:
        return None
    return {"division_path": path_titles, "lines": f"{lo}-{hi}", "trimmed": trimmed, "has_division": bool(stack), "text": text}


def _work_range(data: dict, source: dict) -> tuple[int, int] | None:
    """The source's work as a division: by its `external_ids.thml_div` id, else by its title."""
    thml_div = (source.get("external_ids") or {}).get("thml_div")
    if not thml_div:
        return _work_by_title(data, source.get("work"))
    for line, closing, level, ident, _title in data["events"]:
        if not closing and ident == thml_div:
            return line, _division_end(data["events"], line, level)
    return None


def _work_by_title(data: dict, work: str | None) -> tuple[int, int] | None:
    """The first division of level 1 to 3 whose title holds, or is held by, one of the names in the source's `work` field."""
    names = {re.sub(r"\W+", " ", n).strip().lower() for n in re.split(r"[;,()\u2013\u2014]| - ", work or "")}
    names = {n for n in names if len(n) >= 8}
    for line, closing, level, _ident, title in data["events"]:
        if closing or level > 3 or not title:
            continue
        clean = re.sub(r"\W+", " ", title).strip().lower()
        if len(clean) >= 8 and any(n in clean or clean in n for n in names):
            return line, _division_end(data["events"], line, level)
    return None


def _find_quote(path: Path, text: str, work: tuple[int, int] | None) -> tuple[int, int] | None:
    """The lines holding the quote's opening or closing words, searched inside the work first."""
    data = _load(str(path))
    segments = [s.strip() for s in _ELLIPSIS_RE.split(text or "") if s.strip()]
    if not segments:
        return None
    probes = [" ".join(segments[0].split()[:QUOTE_PROBE_WORDS]), " ".join(segments[-1].split()[-QUOTE_PROBE_WORDS:]),
              " ".join(segments[0].split()[:5])]
    ranges = ([work] if work else []) + [(1, len(data["lines"]))]
    for probe in probes:
        if len(probe.split()) < 3:
            continue
        pattern = _segment_pattern(probe)
        for first, last in ranges:
            begin = data["starts"][first - 1]
            end = data["starts"][last] if last < len(data["starts"]) else len(data["joined"])
            found = pattern.search(data["joined"], begin, end)
            if found:
                line = bisect.bisect_right(data["starts"], found.start())
                tail = bisect.bisect_right(data["starts"], max(found.end() - 1, found.start()))
                return line, tail
    return None


def _candidate_files(source: dict, locus: str, volume: str | None, texts: Path) -> list[Path]:
    names = _extract_texts_filenames(source.get("edition") or "") + _LOCUS_FILE.findall(locus or "")
    ext = source.get("external_ids") or {}
    volumes = [v for v in (volume, ext.get("ccel_volume")) if v]
    for vol in volumes:
        names += [p.name for p in sorted(texts.glob(f"{vol}_*"))]
    ordered = list(dict.fromkeys(names))
    if volume:
        ordered.sort(key=lambda n: not n.startswith(f"{volume}_"))
    return [texts / n for n in ordered if (texts / n).is_file()]


def _opening(path: Path, work: tuple[int, int] | None, cap: int) -> dict | None:
    data = _load(str(path))
    if work:
        first, last = work
        stack = [(first, 0, None, None)]
        titles = [t for _l, _lv, _i, t in _containing(data["events"], first) if t]
    elif path.suffix == ".xml":
        return None
    else:
        header = [n for n, line in enumerate(data["lines"][:120], start=1) if _HEADER_RULE.match(line)]
        first, last, titles = (header[-1] + 1 if header else 1), len(data["lines"]), []
        stack = []
    text, lo, hi, _ = _trim(data, first, last, (first, first), cap)
    if not text:
        return None
    return {"division_path": titles, "lines": f"{lo}-{hi}", "trimmed": True, "has_division": bool(stack), "text": text}


def resolve_record(record: dict, records: dict[str, dict], texts_root: Path, cap: int = DIVISION_MAX_WORDS) -> dict:
    """{"passages": [...], "unresolved": [{"record_id", "source_id", "reason"}]} for one record."""
    texts = texts_dir(texts_root)
    passages, unresolved = [], []
    sources = record.get("sources") or []
    if not sources:
        return {"passages": [], "unresolved": [{"record_id": record["id"], "source_id": None, "reason": "the record names no source"}]}
    for entry in sources:
        sid, locus = entry.get("source_id"), entry.get("locus") or ""
        source = records.get(sid or "")
        if not source:
            unresolved.append({"record_id": record["id"], "source_id": sid, "reason": "no source record"})
            continue
        base = {"record_id": record["id"], "source_id": sid, "locus": locus}
        explicit = _LINE_LOCUS.findall(locus)
        found = None
        for volume, first, last in explicit:
            for path in _candidate_files(source, locus, volume or None, texts):
                got = _passage_at(path, (int(first), int(last or first)), cap)
                if got:
                    found = {**base, "file": path.name, "how": "cited lines", **got}
                    break
            if found:
                break
        files = _candidate_files(source, locus, None, texts)
        if not found and record.get("text"):
            for path in files:
                work = _work_range(_load(str(path)), source)
                hit = _find_quote(path, record["text"], work)
                got = _passage_at(path, hit, cap) if hit else None
                if got:
                    found = {**base, "file": path.name, "how": "quoted words found", **got}
                    break
        if not found:
            for path in files:
                work = _work_range(_load(str(path)), source)
                got = _opening(path, work, min(cap, OPENING_WORDS))
                if got:
                    found = {**base, "file": path.name, "how": "work opening only", **got}
                    break
        if found:
            passages.append(found)
        elif source.get("kind") == "unvendored":
            unresolved.append({"record_id": record["id"], "source_id": sid, "reason": "the source is not vendored"})
        elif not files:
            unresolved.append({"record_id": record["id"], "source_id": sid,
                               "reason": "the cited record is a project record, not a vendored text" if source.get("kind") is None
                               else "no vendored file found for the source"})
        else:
            unresolved.append({"record_id": record["id"], "source_id": sid,
                               "reason": "the locus names no line, the words were not found, and the work's division in the file was not identified"})
    passages.sort(key=lambda p: ("work opening only" == p["how"]))
    if any(p["how"] != "work opening only" for p in passages):
        passages = [p for p in passages if p["how"] != "work opening only"]
    return {"passages": passages[:MAX_PASSAGES_PER_RECORD], "unresolved": unresolved}
