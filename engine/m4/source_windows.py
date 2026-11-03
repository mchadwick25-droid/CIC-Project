"""Context windows for quote and story records whose locus names no
`cic/texts/<file>, lines N` span, so engine.m4.fit_step.context_blocks finds
nothing for them.

The file is the vendored edition the record's source names
(engine.m1.quote_verbatim.resolve_vendored_paths). Where a locus names
several, a shorthand in the locus that begins the file's name ("npnf204")
chooses among them. The anchor, the line the passage sits at, is found in
this order:
- for a quote, the first line where its verbatim text is found, matched as
  runs of WORD_RUN words with markup, punctuation and case set aside;
- the line numbers the locus names ("lines 68808-68812", "from line 32928",
  "line ~41112");
- the division the locus names by id ("div iii.xi.v").

The window holds the anchored lines whole, then lines either side of them,
alternating, up to fit_step.CONTEXT_MAX_WORDS words. It stays inside the
innermost division (<div1> to <div6>) that holds the anchor, where the file
has one, and otherwise inside fit_step.CONTEXT_RADIUS_LINES lines either
side. Each window is a context block in fit_step's own form and id, so it is
rendered and treated as context, never evidence."""
import bisect
import functools
import re
from pathlib import Path

from engine.m1.quote_verbatim import resolve_vendored_paths
from engine.m4 import fit_step

WORD_RUN = 8
_MARKUP = re.compile(r"<[^>]+>")
_WORD = re.compile(r"\w+")
_DIV = re.compile(r"<(/?)div([1-6])\b([^>]*)>")
_ID = re.compile(r'\bid="([^"]+)"')
_LINES = re.compile(r"\blines?\s*~?\s*(\d+)(?:\s*[-–]\s*~?\s*(\d+))?", re.IGNORECASE)
_DIV_NAMED = re.compile(r"\bdiv\s+([\w.]+[\w])")
_SHORTHAND = re.compile(r"\b([a-z]+\d+)\b")


@functools.lru_cache(maxsize=32)
def _lines(path: str) -> tuple[str, ...]:
    return tuple(Path(path).read_text(encoding="utf-8", errors="replace").splitlines())


@functools.lru_cache(maxsize=32)
def _words(path: str) -> tuple[str, tuple[int, ...], tuple[int, ...]]:
    """The file's words, lower-cased and space-joined, with each word's
    offset in that string and the line it stands on."""
    words, offsets, line_of = [], [], []
    position = 0
    for number, line in enumerate(_lines(path), start=1):
        for word in _WORD.findall(_MARKUP.sub(" ", line).lower()):
            words.append(word)
            offsets.append(position)
            line_of.append(number)
            position += len(word) + 1
    return " ".join(words), tuple(offsets), tuple(line_of)


@functools.lru_cache(maxsize=32)
def _divisions(path: str) -> tuple[tuple[int, int, int, str], ...]:
    """(level, first line, last line, id) for every division in the file."""
    found, open_at = [], {}
    for number, line in enumerate(_lines(path), start=1):
        for closing, level, attrs in _DIV.findall(line):
            level = int(level)
            if closing:
                if level in open_at:
                    first, ident = open_at.pop(level)
                    found.append((level, first, number, ident))
            else:
                ident = _ID.search(attrs)
                open_at[level] = (number, ident.group(1) if ident else "")
    total = len(_lines(path))
    found += [(level, first, total, ident) for level, (first, ident) in open_at.items()]
    return tuple(found)


def _find_text(path: str, text: str) -> tuple[int, int] | None:
    joined, offsets, line_of = _words(path)
    wanted = _WORD.findall(_MARKUP.sub(" ", text).lower())
    if len(wanted) < WORD_RUN:
        return None
    for start in range(0, len(wanted) - WORD_RUN + 1, WORD_RUN // 2):
        at = joined.find(" ".join(wanted[start:start + WORD_RUN]))
        if at < 0 or (at and joined[at - 1] != " "):
            continue
        first = bisect.bisect_left(offsets, at) - start
        first = max(first, 0)
        last = min(first + len(wanted) - 1, len(line_of) - 1)
        return line_of[first], line_of[last]
    return None


def _anchor(record: dict, path: str, locus: str) -> tuple[int, int] | None:
    if record.get("record_type") == "quote" and (found := _find_text(path, record.get("text") or "")):
        return found
    total = len(_lines(path))
    for first, last in _LINES.findall(locus):
        first, last = int(first), int(last or first)
        if 1 <= first <= total:
            return first, min(max(last, first), total)
    named = _DIV_NAMED.search(locus)
    if named:
        for _level, first, _last, ident in _divisions(path):
            if ident == named.group(1):
                return first, first
    return None


def _bounds(path: str, first: int, last: int) -> tuple[int, int]:
    holding = [(level, low, high) for level, low, high, _ in _divisions(path) if low <= first and last <= high]
    if holding:
        _level, low, high = max(holding)
        return low, high
    return max(first - fit_step.CONTEXT_RADIUS_LINES, 1), min(last + fit_step.CONTEXT_RADIUS_LINES, len(_lines(path)))


def _window(path: str, first: int, last: int) -> str:
    lines = _lines(path)
    floor, ceiling = _bounds(path, first, last)

    def words(number: int) -> list[str]:
        return _MARKUP.sub(" ", lines[number - 1]).split()

    cited = [w for n in range(first, last + 1) for w in words(n)]
    before: list[str] = []
    after: list[str] = []
    budget = max(fit_step.CONTEXT_MAX_WORDS - len(cited), 0)
    lower, upper = first - 1, last + 1
    while budget > 0 and (lower >= floor or upper <= ceiling):
        if lower >= floor:
            take = words(lower)[-budget:]
            before, budget, lower = take + before, budget - len(take), lower - 1
        if budget > 0 and upper <= ceiling:
            take = words(upper)[:budget]
            after, budget, upper = after + take, budget - len(take), upper + 1
    return " ".join(before + cited + after)


def _pick(paths: list[Path], locus: str) -> list[Path]:
    present = [p for p in paths if p.is_file()]
    tokens = _SHORTHAND.findall(locus.lower())
    chosen = [p for p in present if any(p.name.lower().startswith(t + "_") for t in tokens)]
    return chosen or present[:1]


def context_blocks(record: dict, records: dict[str, dict], texts_root: Path = fit_step.REPO_ROOT) -> list[dict]:
    """One block per source of the record whose edition and anchor resolve."""
    blocks = []
    for source in record.get("sources") or []:
        locus = source.get("locus") or ""
        named = resolve_vendored_paths({"sources": [source]}, records, {})
        paths = [texts_root / "cic" / "texts" / p.name for p in named]
        for path in _pick(paths, locus):
            anchor = _anchor(record, str(path), locus)
            if anchor is None:
                continue
            text = _window(str(path), *anchor)
            if text:
                blocks.append({
                    "id": f"{fit_step.CONTEXT_PREFIX}{record['id']}.{len(blocks) + 1}", "record_id": record["id"],
                    "source_id": source.get("source_id"), "file": f"cic/texts/{path.name}",
                    "lines": f"{anchor[0]}-{anchor[1]}", "text": text,
                })
                break
    return blocks
