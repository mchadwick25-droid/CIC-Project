"""Context windows for quote and story records whose locus names no
`cic/texts/<file>, lines N` span, so engine.m4.fit_step.context_blocks finds
nothing for them.

The file is the vendored edition the record's source names
(engine.m1.quote_verbatim.resolve_vendored_paths). Where a locus names
several, a shorthand in the locus that begins the file's name ("npnf204")
chooses among them.

The anchor, the lines the passage sits at, is found in this order:
- for a quote, the first line where its verbatim text is found, matched as
  runs of WORD_RUN words with markup, punctuation and case set aside;
- the line numbers the locus names ("lines 68808-68812", "from line 32928",
  "line ~41112");
- the division the locus names by id ("div iii.xi.v");
- the divisions the locus names by number (see below).

An anchor from the first three is a point: its window holds the anchored
lines whole, then lines either side of them, alternating, up to
fit_step.CONTEXT_MAX_WORDS words, inside the innermost division (<div1> to
<div6>) that holds it, or, in a file with none, inside
fit_step.CONTEXT_RADIUS_LINES lines either side.

A reference by number ("VI.1-2", "65-67", "Magnesians 6", "Vision 2.4.3",
"Book I, ch. lviij") is read from the locus outside its parentheses and
before any " - " gloss; its first piece that resolves is used. A number
after ":" is a verse, finer than any edition marks, and is not used.
- In a file with divisions, the search runs inside the work: the most
  specific division id the source's `edition` names in the parentheses
  after that file's path ("div1 v", "div2 viii.ii"), or else the division
  whose title shares the most words with the source's author and work,
  then the fewest words besides, then the shallowest.
- Each number is the shallowest division beneath the last that carries it:
  as its `n` (with a `type`), as the number after one label word in its
  title or short title ("Chapter IV.", "Vision Second."), or, for a typed
  division with no `n`, at the head of its own text ("Chapter XXVI.—").
  For the last number a chapter is preferred to any other label. A leading
  name ("Magnesians") is first matched as a word of a division's title.
- Below the last division, a number is read from the "Chap. N" headings
  inside it. A number with no division and no heading beneath a division
  that has neither is finer than the edition marks and is dropped; any
  other number that does not resolve fails the piece.
- "-N" extends the last division to its sibling N.
- In a plain-text file, each number is the first heading line, a line of
  20 words or fewer led by a label word in _TEXT_LABELS ("Chapter lviij:
  ..."), whose section, up to the next such heading, holds at least
  MIN_SECTION_WORDS words, so a table of contents is passed over. A plain
  text of 2 x fit_step.CONTEXT_MAX_WORDS words or fewer is its own division,
  and "whole text" names the file from the end of its header.
Its window is the opening of the named range, up to
fit_step.CONTEXT_MAX_WORDS words; a block cut short there carries
"trimmed": True.

Each window is a context block in fit_step's own form and id, so it is
rendered and treated as context, never evidence."""
import bisect
import functools
import re
from pathlib import Path

from engine.m1.quote_verbatim import resolve_vendored_paths
from engine.m4 import fit_step

WORD_RUN = 8
MIN_SECTION_WORDS = 50
_MARKUP = re.compile(r"<[^>]+>")
_WORD = re.compile(r"\w+")
_DIV = re.compile(r"<(/?)div([1-6])\b([^>]*)>")
_ATTR = re.compile(r'\b(id|n|title|shorttitle|type)="([^"]*)"')
_LINES = re.compile(r"\blines?\s*~?\s*(\d+)(?:\s*[-–]\s*~?\s*(\d+))?", re.IGNORECASE)
_DIV_NAMED = re.compile(r"\bdiv\s+([\w.]+[\w])")
_EDITION_DIV = re.compile(r"\bdiv\d?\s+([ivxlc]+(?:\.[ivxlc]+)*)\b")
_TEXT_LABELS = frozenset({"chapter", "book", "section", "demonstration", "homily", "hymn", "letter", "memra", "part"})
_SHORTHAND = re.compile(r"\b([a-z]+\d+)\b")
_PAREN = re.compile(r"\([^()]*\)")
_PIECE = re.compile(
    r"^(?:(?:ch|chap|chapter|sec|section)\.?\s+)?(?:([A-Z][a-z]+)\s+)?([IVXLCivxlcj]+|\d+)((?:[.:]\d+)*)(?:\s*[-–]\s*(\d+))?$"
)
_HEADING = re.compile(r"^\s*(?:([A-Za-z]+)\.?\s+)?([IVXLCDMivxlcdmj]+|\d+)\b\s*[.:,—–-]?")
_RULE = re.compile(r"^\s*_{10,}\s*$")
_STOP = frozenset({"the", "and", "with", "from", "that", "this", "their", "which", "into", "letters", "letter", "works"})
_ORDINALS = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh",
             "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth",
             "twentieth")
_ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}


def number(token: str) -> int | None:
    """An Arabic numeral, a Roman one (a final "j" read as "i"), or an ordinal word, as an int."""
    token = token.lower().strip()
    if token.isdigit():
        return int(token)
    if token in _ORDINALS:
        return _ORDINALS.index(token) + 1
    token = token.replace("j", "i")
    if not token or any(ch not in _ROMAN for ch in token):
        return None
    total = 0
    for here, after in zip(token, token[1:] + " "):
        value = _ROMAN[here]
        total += -value if after != " " and _ROMAN[after] > value else value
    return total


@functools.lru_cache(maxsize=32)
def _lines(path: str) -> tuple[str, ...]:
    return tuple(Path(path).read_text(encoding="utf-8", errors="replace").splitlines())


@functools.lru_cache(maxsize=32)
def _words(path: str) -> tuple[str, tuple[int, ...], tuple[int, ...]]:
    """The file's words, lower-cased and space-joined, with each word's
    offset in that string and the line it stands on."""
    words, offsets, line_of = [], [], []
    position = 0
    for number_, line in enumerate(_lines(path), start=1):
        for word in _WORD.findall(_MARKUP.sub(" ", line).lower()):
            words.append(word)
            offsets.append(position)
            line_of.append(number_)
            position += len(word) + 1
    return " ".join(words), tuple(offsets), tuple(line_of)


@functools.lru_cache(maxsize=32)
def _divisions(path: str) -> tuple[dict, ...]:
    """Every division in the file, in file order: level, first and last line, and its id, n, title and short title."""
    found, open_at = [], {}
    for line_no, line in enumerate(_lines(path), start=1):
        for closing, level, attrs in _DIV.findall(line):
            level = int(level)
            if closing:
                if level in open_at:
                    division = open_at.pop(level)
                    division["last"] = line_no
                    found.append(division)
            else:
                open_at[level] = {"level": level, "first": line_no, "last": None, **dict(_ATTR.findall(attrs))}
    total = len(_lines(path))
    found += [{**division, "last": total} for division in open_at.values()]
    return tuple(sorted(found, key=lambda d: (d["first"], d["level"])))


def _find_text(path: str, text: str) -> tuple[int, int] | None:
    joined, offsets, line_of = _words(path)
    wanted = _WORD.findall(_MARKUP.sub(" ", text).lower())
    if len(wanted) < WORD_RUN:
        return None
    for start in range(0, len(wanted) - WORD_RUN + 1, WORD_RUN // 2):
        at = joined.find(" ".join(wanted[start:start + WORD_RUN]))
        if at < 0 or (at and joined[at - 1] != " "):
            continue
        first = max(bisect.bisect_left(offsets, at) - start, 0)
        last = min(first + len(wanted) - 1, len(line_of) - 1)
        return line_of[first], line_of[last]
    return None


def _point(record: dict, path: str, locus: str) -> tuple[int, int] | None:
    if record.get("record_type") == "quote" and (found := _find_text(path, record.get("text") or "")):
        return found
    total = len(_lines(path))
    for first, last in _LINES.findall(locus):
        first, last = int(first), int(last or first)
        if 1 <= first <= total:
            return first, min(max(last, first), total)
    named = _DIV_NAMED.search(locus)
    if named:
        for division in _divisions(path):
            if division.get("id") == named.group(1):
                return division["first"], division["first"]
    return None


def pieces(locus: str) -> list[tuple[str | None, list[int], int | None]]:
    """The references by number in a locus: (leading name, numbers, range end)."""
    text = _PAREN.sub(" ", locus).split(" - ")[0]
    parts = [p.strip() for p in re.split(r"[;,]", text) if p.strip()]
    found = []
    for index, part in enumerate(parts):
        match = _PIECE.match(part)
        if not match:
            continue
        name, head, rest, end = match.groups()
        numbers = [number(head)] + [int(n) for n in re.findall(r"\.(\d+)", (rest or "").split(":")[0])]
        if ":" in (rest or ""):
            end = None
        if None in numbers:
            continue
        if name == "Book" and len(numbers) == 1 and index + 1 < len(parts) and (inner := _PIECE.match(parts[index + 1])):
            inner_numbers = [number(inner.group(2))] + [int(n) for n in re.findall(r"\.(\d+)", (inner.group(3) or "").split(":")[0])]
            if None not in inner_numbers:
                found.append((name, numbers + inner_numbers, int(inner.group(4)) if inner.group(4) else None))
        found.append((name, numbers, int(end) if end else None))
    return found


def _label_number(label: str) -> tuple[str, int | None]:
    match = _HEADING.match(_MARKUP.sub(" ", label or ""))
    if not match:
        return "", None
    word, numeral = match.group(1) or "", match.group(2)
    value = number(numeral)
    if value is None and word:
        value = number(word)
        word = ""
    return word.lower(), value


def _ordinal_title(title: str) -> tuple[str, int | None]:
    words = (title or "").split()
    if len(words) >= 2 and (value := number(words[1].strip(".,:"))) is not None:
        return words[0].lower().strip(".,:"), value
    return _label_number(title)


@functools.lru_cache(maxsize=4096)
def _lead(path: str, first: int) -> tuple[str, int | None]:
    """The label and number the division's own opening text carries ("Chapter XXVI.—", "Demonstration VI.")."""
    opening = " ".join(_MARKUP.sub(" ", " ".join(_lines(path)[first - 1:first + 3])).split())
    return _label_number(opening)


def _matches(path: str, division: dict, value: int, name: str | None) -> bool:
    if name is None and division.get("type") and division.get("n") and number(division["n"]) == value:
        return True
    for label in (division.get("shorttitle"), division.get("title")):
        word, found = _ordinal_title(label or "")
        if found == value and (name is None or word == name.lower()):
            return True
    if division.get("type") and not division.get("n"):
        word, found = _lead(path, division["first"])
        return found == value and word in {division["type"].lower(), "chapter", (name or "").lower()}
    return False


def _inside(outer: dict | None, division: dict) -> bool:
    return outer is None or (
        outer["first"] <= division["first"] and division["last"] <= outer["last"] and division["level"] > outer["level"]
    )


def _best(candidates: list[dict], prefer_chapter: bool) -> dict | None:
    """The shallowest, then earliest; for the last number of a reference, a chapter or an
    unlabelled number first."""
    def rank(d: dict) -> tuple:
        word = _ordinal_title(d.get("title") or "")[0]
        chapter = word in ("", "chapter", "chap") or (d.get("type") or "").lower() == "chapter"
        return (prefer_chapter and not chapter, d["level"], d["first"])
    return min(candidates, key=rank) if candidates else None


def _children(divisions: tuple[dict, ...], outer: dict | None) -> list[dict]:
    level = outer["level"] + 1 if outer else 1
    return [d for d in divisions if d["level"] == level and _inside(outer, d)]


def _find(path: str, current: dict | None, value: int, name: str | None, last: bool) -> tuple[dict | None, dict | None]:
    """(the division numbered `value` beneath `current`, the division it was found in)."""
    within = [d for d in _divisions(path) if _inside(current, d)]
    found = _best([d for d in within if _matches(path, d, value, name)], last)
    if found is not None:
        return found, current
    if name:
        holder = _best([d for d in within if name.lower() in _WORD.findall((d.get("title") or "").lower())], False)
        if holder is not None:
            return _find(path, holder, value, None, last)
    return None, current


_INNER_HEADING = re.compile(r"<h[1-6][^>]*>\s*(?:chap(?:ter)?\.?)\s+([IVXLCivxlc]+|\d+)\b", re.IGNORECASE)


def _inner_headings(path: str, division: dict) -> list[tuple[int, int]]:
    """(line, number) of each "Chap. N" heading inside the division's own text."""
    lines = _lines(path)
    found = []
    for line_no in range(division["first"], division["last"] + 1):
        match = _INNER_HEADING.search(lines[line_no - 1])
        if match and (value := number(match.group(1))) is not None:
            found.append((line_no, value))
    return found


def _xml_range(path: str, scope: dict | None, name: str | None, numbers: list[int], end: int | None) -> tuple[int, int] | None:
    """The lines of the divisions `numbers` name beneath `scope`. A number below the last
    division is read from the "Chap. N" headings inside it; one finer still than the
    edition marks is dropped."""
    divisions = _divisions(path)
    current, parent = scope, scope
    for position, value in enumerate(numbers):
        found, holder = _find(path, current, value, name if position == 0 else None, position == len(numbers) - 1)
        if found is not None:
            parent, current = holder, found
            continue
        heads = _inner_headings(path, current) if current is not None else []
        starts = [line_no for line_no, n in heads if n == value]
        if starts:
            later = [line_no for line_no, _ in heads if line_no > starts[0]]
            stop = later[0] - 1 if later else current["last"]
            if end is not None and position == len(numbers) - 1:
                ends = [line_no for line_no, n in heads if n == end and line_no > starts[0]]
                if ends:
                    after = [line_no for line_no, _ in heads if line_no > ends[0]]
                    stop = after[0] - 1 if after else current["last"]
            return starts[0], stop
        if position > 0 and not heads and not _children(divisions, current):
            break
        return None
    if current is None:
        return None
    first, last = current["first"], current["last"]
    if end is not None and len(numbers) > 0:
        sibling, _ = _find(path, parent, end, None, True)
        if sibling is not None and sibling["level"] == current["level"] and sibling["last"] > last:
            last = sibling["last"]
    return first, last


def _scope(path: str, source: dict) -> dict | None:
    divisions = _divisions(path)
    by_id = {d.get("id"): d for d in divisions if d.get("id")}
    note = re.search(re.escape(Path(path).name) + r"\s*\(([^)]*)\)", source.get("edition") or "")
    named = [by_id[i] for i in _EDITION_DIV.findall(note.group(1) if note else "") if i in by_id]
    if named:
        return max(named, key=lambda d: d["level"])
    author = (source.get("author") or "").split("(")[0]
    work = re.split(r" - |;|,", source.get("work") or "")[0]
    wanted = {w for w in _WORD.findall(f"{author} {work}".lower()) if len(w) > 3 and w not in _STOP}
    def score(d: dict) -> tuple[int, float]:
        title = {w for w in _WORD.findall((d.get("title") or "").lower()) if len(w) > 3 and w not in _STOP}
        shared = len(wanted & title)
        return shared, shared / len(title) if title else 0.0

    scored = [(score(d), d) for d in divisions]
    best = max((sc for sc, _ in scored), default=(0, 0.0))
    if best[0] == 0:
        return None
    return min((d for sc, d in scored if sc == best), key=lambda d: (d["level"], d["first"]))


def _text_heading(line: str) -> tuple[str, int | None]:
    word, value = _label_number(line)
    return (word, value) if word in _TEXT_LABELS and len(line.split()) <= 20 else ("", None)


def _text_headings(path: str, value: int, after: int) -> int | None:
    lines = _lines(path)
    headings = [n for n, line in enumerate(lines, start=1) if n > after and _text_heading(line)[1] is not None]
    for index, line_no in enumerate(headings):
        if _text_heading(lines[line_no - 1])[1] != value:
            continue
        stop = headings[index + 1] if index + 1 < len(headings) else len(lines) + 1
        if sum(len(lines[n - 1].split()) for n in range(line_no, stop)) >= MIN_SECTION_WORDS:
            return line_no
    return None


def _text_range(path: str, numbers: list[int]) -> tuple[int, int] | None:
    after = 0
    for value in numbers:
        found = _text_headings(path, value, after)
        if found is None:
            return None
        after = found
    lines = _lines(path)
    word, _ = _text_heading(lines[after - 1])
    later = [n for n in range(after + 1, len(lines) + 1) if _text_heading(lines[n - 1])[0] == word]
    return after, (later[0] - 1 if later else len(lines))


def _body_start(path: str) -> int:
    rules = [n for n, line in enumerate(_lines(path)[:60], start=1) if _RULE.match(line)]
    return rules[-1] + 1 if rules else 1


def _range(path: str, source: dict, locus: str) -> tuple[int, int] | None:
    plain = not _divisions(path)
    if plain and locus.strip().lower() == "whole text":
        return _body_start(path), len(_lines(path))
    for name, numbers, end in pieces(locus):
        found = _text_range(path, numbers) if plain else _xml_range(path, _scope(path, source), name, numbers, end)
        if found:
            return found
    if plain and len(_words(path)[1]) <= 2 * fit_step.CONTEXT_MAX_WORDS:
        return _body_start(path), len(_lines(path))
    return None


def _bounds(path: str, first: int, last: int) -> tuple[int, int]:
    holding = [d for d in _divisions(path) if d["first"] <= first and last <= d["last"]]
    if holding:
        innermost = max(holding, key=lambda d: d["level"])
        return innermost["first"], innermost["last"]
    return max(first - fit_step.CONTEXT_RADIUS_LINES, 1), min(last + fit_step.CONTEXT_RADIUS_LINES, len(_lines(path)))


def division_path(path: str, first: int, last: int) -> list[str]:
    """The titles of the divisions that hold lines first..last, outermost first."""
    holding = sorted((d for d in _divisions(path) if d["first"] <= first and last <= d["last"]), key=lambda d: d["level"])
    return [d["title"] for d in holding if d.get("title")]


def _line_words(path: str, line_no: int) -> list[str]:
    return _MARKUP.sub(" ", _lines(path)[line_no - 1]).split()


def _window(path: str, first: int, last: int) -> str:
    floor, ceiling = _bounds(path, first, last)
    cited = [w for n in range(first, last + 1) for w in _line_words(path, n)]
    before: list[str] = []
    after: list[str] = []
    budget = max(fit_step.CONTEXT_MAX_WORDS - len(cited), 0)
    lower, upper = first - 1, last + 1
    while budget > 0 and (lower >= floor or upper <= ceiling):
        if lower >= floor:
            take = _line_words(path, lower)[-budget:]
            before, budget, lower = take + before, budget - len(take), lower - 1
        if budget > 0 and upper <= ceiling:
            take = _line_words(path, upper)[:budget]
            after, budget, upper = after + take, budget - len(take), upper + 1
    return " ".join(before + cited + after)


def _opening(path: str, first: int, last: int) -> tuple[str, bool]:
    """The first fit_step.CONTEXT_MAX_WORDS words of lines first..last, and whether that cut the range short."""
    words = [w for n in range(first, last + 1) for w in _line_words(path, n)]
    return " ".join(words[:fit_step.CONTEXT_MAX_WORDS]), len(words) > fit_step.CONTEXT_MAX_WORDS


def _pick(paths: list[Path], locus: str) -> list[Path]:
    present = [p for p in paths if p.is_file()]
    tokens = _SHORTHAND.findall(locus.lower())
    chosen = [p for p in present if any(p.name.lower().startswith(t + "_") for t in tokens)]
    return chosen or present[:1]


def _block(record: dict, source: dict, path: Path, lines: tuple[int, int], text: str, trimmed: bool, n: int) -> dict:
    return {
        "id": f"{fit_step.CONTEXT_PREFIX}{record['id']}.{n}", "record_id": record["id"], "source_id": source.get("source_id"),
        "file": f"cic/texts/{path.name}", "lines": f"{lines[0]}-{lines[1]}", "text": text, "trimmed": trimmed,
        "division_path": division_path(str(path), *lines),
    }


def context_blocks(record: dict, records: dict[str, dict], texts_root: Path = fit_step.REPO_ROOT) -> list[dict]:
    """At most one block per source of the record: the first of its edition files where an anchor resolves."""
    blocks = []
    for source in record.get("sources") or []:
        locus = source.get("locus") or ""
        source_record = records.get(source.get("source_id") or "") or {}
        named = resolve_vendored_paths({"sources": [source]}, records, {})
        paths = [texts_root / "cic" / "texts" / p.name for p in named]
        for path in _pick(paths, locus):
            if (point := _point(record, str(path), locus)) is not None:
                text, trimmed = _window(str(path), *point), False
                lines = point
            elif (span := _range(str(path), source_record, locus)) is not None:
                (text, trimmed), lines = _opening(str(path), *span), span
            else:
                continue
            if text:
                blocks.append(_block(record, source, path, lines, text, trimmed, len(blocks) + 1))
                break
    return blocks
