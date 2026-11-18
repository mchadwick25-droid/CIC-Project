"""Markup-aware reading of ThML, TEI/EpiDoc and USFX text: the visible text as
a main stream, editorial notes as a second stream, and the file's own
division markers as boundaries into both."""
from __future__ import annotations

import html
import re
from bisect import bisect_right
from dataclasses import dataclass, field

TOKEN = re.compile(
    r"<!--.*?-->|<\?.*?\?>|<![^>]*>|<(?P<close>/?)(?P<name>[A-Za-z][\w.:-]*)(?P<attrs>[^>]*)>|&#?\w+;|[^<&]+|[<&]",
    re.S,
)
ATTR = re.compile(r'([\w:.-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\')')
THML_DIV = re.compile(r"^div([1-9])$")
BLOCK = frozenset({
    "p", "div", "head", "li", "ul", "ol", "tr", "td", "th", "table", "br", "lb", "pb", "l", "lg",
    "h", "h1", "h2", "h3", "h4", "h5", "h6", "tei", "body", "text", "front", "back", "b", "book",
    "c", "d", "s", "sp", "speaker", "closer", "opener", "list", "item", "row", "cell", "bibl",
})
EMBEDDED = frozenset({"scripref", "quote", "q", "cit", "foreign"})
NOTE_TAGS = frozenset({"note", "f"})
SKIP_TEXT = frozenset({"style", "script"})
MARKUP_SIGNATURE = re.compile(r"<(?:lb|pb|div[1-9]?|p|head|note|milestone|book)(?:[ >/])")
MARKUP_MIN_HITS = 30

APPARATUS_TITLE = re.compile(
    r"^(title page|second title page|editorial preface|preface|prolegomena|"
    r"introductory (note|notice)|translator'?s? (preface|note)|contents|"
    r"table of contents|index|indexes|indices|general index|bibliograph|"
    r"chronological table|genealogical tables?|errata|advertisement|"
    r"elucidations?|addenda|memoir|biographical synopsis|series title)\b",
    re.I,
)
BARE_APPENDIX = re.compile(r"^appendix\b[\s.:;,–—-]*(?:[ivxl]+|\d+)?[\s.:;,]*$", re.I)


def is_apparatus_title(title: str) -> bool:
    t = title.strip()
    return bool(APPARATUS_TITLE.match(t) or BARE_APPENDIX.match(t))


def looks_like_markup(text: str, sample: int = 400_000) -> bool:
    head = text[:sample]
    return len(MARKUP_SIGNATURE.findall(head)) >= MARKUP_MIN_HITS


@dataclass
class Stream:
    text: str = ""
    out_starts: list[int] = field(default_factory=list)
    raw_starts: list[int] = field(default_factory=list)
    raw_ends: list[int] = field(default_factory=list)

    def raw_pos_start(self, i: int) -> int:
        k = bisect_right(self.out_starts, i) - 1
        if k < 0:
            return self.raw_starts[0] if self.raw_starts else 0
        return min(self.raw_starts[k] + (i - self.out_starts[k]), self.raw_ends[k] - 1)

    def raw_pos_end(self, j: int) -> int:
        """Raw index just past the character at stream index j-1."""
        k = bisect_right(self.out_starts, j - 1) - 1
        if k < 0:
            return self.raw_starts[0] if self.raw_starts else 0
        return min(self.raw_starts[k] + (j - 1 - self.out_starts[k]) + 1, self.raw_ends[k])


@dataclass
class Boundary:
    main_pos: int
    note_pos: int
    locus: str
    title: str
    apparatus: bool
    level: int
    raw_pos: int


@dataclass
class MarkupDoc:
    main: Stream
    notes: Stream
    boundaries: list[Boundary]
    embedded: list[int]


class _Builder:
    def __init__(self):
        self.parts = {"main": [], "notes": []}
        self.lens = {"main": 0, "notes": 0}
        self.maps = {"main": ([], [], []), "notes": ([], [], [])}

    def emit(self, which: str, text: str, raw_start: int, raw_end: int):
        if not text:
            return
        out_starts, raw_starts, raw_ends = self.maps[which]
        out_starts.append(self.lens[which])
        raw_starts.append(raw_start)
        raw_ends.append(raw_end)
        self.parts[which].append(text)
        self.lens[which] += len(text)

    def stream(self, which: str) -> Stream:
        o, s, e = self.maps[which]
        return Stream("".join(self.parts[which]), o, s, e)


def _attrs(raw: str) -> dict[str, str]:
    return {m.group(1): html.unescape(m.group(2) if m.group(2) is not None else m.group(3))
            for m in ATTR.finditer(raw)}


def parse(raw: str, start: int = 0) -> MarkupDoc:
    b = _Builder()
    boundaries: list[Boundary] = []
    embedded: list[int] = []
    note_depth = 0
    tei_stack: list[tuple[str, bool]] = []
    thml_stack: list[tuple[int, bool]] = []
    path: list[str] = []
    skip = 0
    pending_head: Boundary | None = None
    pending_idx = 0
    head_open = False
    head_buf: list[str] = []
    usfx_book = ""

    def apparatus_inherited() -> bool:
        return any(a for _, a in thml_stack) or any(a for _, a in tei_stack)

    def add_boundary(locus: str, title: str, apparatus: bool, level: int, raw_pos: int) -> Boundary:
        bd = Boundary(b.lens["main"], b.lens["notes"], locus, title, apparatus, level, raw_pos)
        boundaries.append(bd)
        return bd

    for m in TOKEN.finditer(raw, start):
        tok = m.group(0)
        name = m.group("name")
        if name is None:
            if tok.startswith("<!") or tok.startswith("<?"):
                continue
            if skip:
                continue
            piece = html.unescape(tok) if tok[0] == "&" and len(tok) > 1 else tok
            which = "notes" if note_depth else "main"
            b.emit(which, piece, m.start(), m.end())
            if head_open and not note_depth:
                head_buf.append(piece)
            continue

        lname = name.lower()
        closing = bool(m.group("close"))
        attr_raw = m.group("attrs")
        selfclose = attr_raw.rstrip().endswith("/")
        which = "notes" if note_depth else "main"

        if lname in SKIP_TEXT:
            skip += -1 if closing else (0 if selfclose else 1)
            skip = max(skip, 0)
            continue

        if lname in NOTE_TAGS:
            if closing:
                note_depth = max(note_depth - 1, 0)
            elif not selfclose:
                note_depth += 1
            continue

        thml = THML_DIV.match(lname)
        if thml:
            level = int(thml.group(1))
            if closing:
                if thml_stack:
                    thml_stack.pop()
                continue
            a = _attrs(attr_raw)
            title = a.get("title", "")
            locus = a.get("id") or f"div{level}@{m.start()}"
            app = is_apparatus_title(title) or apparatus_inherited()
            thml_stack.append((level, app))
            add_boundary(locus, title, app, level, m.start())
            continue

        if lname == "div":
            if closing:
                if tei_stack:
                    _, _ = tei_stack.pop()
                    if path:
                        path.pop()
                continue
            a = _attrs(attr_raw)
            typ = a.get("type", "")
            sub = a.get("subtype", "")
            n = a.get("n", "")
            is_edition = typ in ("edition", "translation", "commentary")
            label = (sub or typ or "div")
            app = apparatus_inherited() or typ in ("front", "back", "frontmatter", "backmatter")
            seg = "" if is_edition else (f"{sub}{n}" if sub and n else (n or label))
            if not selfclose:
                tei_stack.append((seg, app))
                path.append(seg)
            if not is_edition:
                locus = ".".join(p for p in path if p) or f"div@{m.start()}"
                title = f"{label} {n}".strip()
                pending_head = add_boundary(locus, title, app, len(path), m.start())
                pending_idx = len(b.parts["main"])
                b.emit(which, "\n", m.start(), m.end())
            else:
                b.emit(which, "\n", m.start(), m.end())
            continue

        if lname == "book" and not closing and "id" in _attrs(attr_raw):
            a = _attrs(attr_raw)
            usfx_book = a["id"]
            add_boundary(usfx_book, usfx_book, False, 1, m.start())
            b.emit(which, "\n", m.start(), m.end())
            continue
        if lname == "c" and not closing and usfx_book:
            a = _attrs(attr_raw)
            if "id" in a:
                add_boundary(f"{usfx_book}.{a['id']}", f"{usfx_book} {a['id']}", False, 2, m.start())
            b.emit(which, "\n", m.start(), m.end())
            continue

        if lname == "head":
            if closing:
                if head_open and pending_head is not None:
                    text = re.sub(r"\s+", " ", "".join(head_buf)).strip()
                    if text:
                        pending_head.title = text
                head_open = False
                pending_head = None
                head_buf = []
            elif not selfclose:
                fresh = pending_head is not None and not "".join(b.parts["main"][pending_idx:]).strip()
                head_open = fresh
                if not fresh:
                    pending_head = None
                head_buf = []
            b.emit(which, "\n", m.start(), m.end())
            continue

        if not closing and lname in EMBEDDED and not note_depth:
            embedded.append(b.lens["main"])

        if lname == "lb" and re.search(r'break\s*=\s*["\']no["\']', attr_raw):
            continue
        if lname in BLOCK:
            b.emit(which, "\n", m.start(), m.end())

    return MarkupDoc(b.stream("main"), b.stream("notes"), boundaries, embedded)
