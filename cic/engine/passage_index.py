#!/usr/bin/env python3
"""Passage index: which vendored works treat or cite a Bible passage.

cic/texts/PASSAGES.sqlite, rebuilt from the markup of the ThML volumes.
Derived and gitignored, like cic/texts/INDEX.sqlite.

WHAT IT READS. CCEL's ThML volumes tag scripture two ways, and each tag
carries an `osisRef` (Bible:Rom.5.12, Bible:Acts.1.1-Acts.1.2):

  <scripCom ... />  opens a homily or commentary section and names the
                    passage it expounds. It is the only evidence that a
                    section TREATS a passage.
  <scripRef>...</scripRef>  a mention inside running text. It CITES.

The two kinds are stored apart and never merged. A citation is not
evidence that a work treats a passage.

TREATS COMES ONLY FROM CCEL'S TAGS, and a tag names the verses a homily opens with, which can be fewer than it covers. Some volumes carry them and some do not (Chrysostom's
Hebrews and Galatians are untagged), so a query also lists untagged volumes that cite
the book heavily, as leads to read and never as findings.

A scripCom whose own type is `Citation` is a citation by CCEL's own label
and is stored as `cites`. `Sermon`, `Commentary` and untyped scripCom tags
are stored as `treats`.

NOTHING IS INTERPRETED. A row is a location: file, raw line, the enclosing
section's title and id. The extract shown at query time is copied
verbatim from the file, tag-stripped, never paraphrased. The index does
not rank commentaries, summarise them, or say where they agree.

LANGUAGE. A hit carries the file's language from its filename code and
whether an English reading exists. Every ThML volume vendored today is
English; plain-text files are not indexed here.

TRADITION AND WINDOW. A hit carries the Atlas entries the file is mapped
to in cic/corpus-map, with each role and the entry's own date window from
ATLAS-TARGETS.md. The window is the entry's, not the author's.

Usage:
  python cic/engine/passage_index.py --build
  python cic/engine/passage_index.py "Romans 5:12"
  python cic/engine/passage_index.py "Rom 5:12-21" --treats-only
  python cic/engine/passage_index.py "Matt 5" --limit 10
  python cic/engine/passage_index.py --readings "Acts 2:14a, 22-32; Ps 16; 1 Pet 1:3-9; John 20:19-31"

READINGS. A pastor pastes the readings they are preaching on, from whatever
lectionary their church uses, and the index answers for each. No lectionary
table is stored: the Revised Common Lectionary's table of citations is
copyrighted (Consultation on Common Texts), and its owners require
written permission for use outside congregations, non-profit groups and
member denominations. The readings are the pastor's own input.
"""
from __future__ import annotations

import argparse
import html
import re
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TEXTS_DIR = REPO_ROOT / "cic" / "texts"
MAP_DIR = REPO_ROOT / "cic" / "corpus-map"
DB_PATH = TEXTS_DIR / "PASSAGES.sqlite"

# Verse positions are ordinals so a range is two numbers. A reference to a
# whole chapter has verse 0 on the left and a large verse on the right.
_CH = 1000
_LAST_VERSE = _CH - 1

# OSIS book ids as CCEL writes them (the `osisRef` attribute), with the
# names and abbreviations a user types. Matched case-insensitively with
# dots and spaces dropped.
_BOOKS = {
    "Gen": "genesis gen ge gn", "Exod": "exodus exod ex exo", "Lev": "leviticus lev le",
    "Num": "numbers num nu", "Deut": "deuteronomy deut dt de", "Josh": "joshua josh jos",
    "Judg": "judges judg jdg", "Ruth": "ruth ru", "1Sam": "1samuel 1sam 1sa", "2Sam": "2samuel 2sam 2sa",
    "1Kgs": "1kings 1kgs 1ki", "2Kgs": "2kings 2kgs 2ki", "1Chr": "1chronicles 1chr 1ch",
    "2Chr": "2chronicles 2chr 2ch", "Ezra": "ezra ezr", "Neh": "nehemiah neh ne",
    "Esth": "esther esth es", "Job": "job jb", "Ps": "psalms psalm ps psa", "Prov": "proverbs prov pr",
    "Eccl": "ecclesiastes eccl ecc", "Song": "songofsolomon song sos canticles", "Isa": "isaiah isa is",
    "Jer": "jeremiah jer", "Lam": "lamentations lam", "Ezek": "ezekiel ezek eze", "Dan": "daniel dan",
    "Hos": "hosea hos", "Joel": "joel", "Amos": "amos", "Obad": "obadiah obad", "Jonah": "jonah",
    "Mic": "micah mic", "Nah": "nahum nah", "Hab": "habakkuk hab", "Zeph": "zephaniah zeph",
    "Hag": "haggai hag", "Zech": "zechariah zech", "Mal": "malachi mal",
    "Matt": "matthew matt mt", "Mark": "mark mk", "Luke": "luke lk", "John": "john jn",
    "Acts": "acts ac", "Rom": "romans rom ro", "1Cor": "1corinthians 1cor 1co",
    "2Cor": "2corinthians 2cor 2co", "Gal": "galatians gal", "Eph": "ephesians eph",
    "Phil": "philippians phil php", "Col": "colossians col", "1Thess": "1thessalonians 1thess 1th",
    "2Thess": "2thessalonians 2thess 2th", "1Tim": "1timothy 1tim 1ti", "2Tim": "2timothy 2tim 2ti",
    "Titus": "titus tit", "Phlm": "philemon phlm phm", "Heb": "hebrews heb",
    "Jas": "james jas jm", "1Pet": "1peter 1pet 1pe", "2Pet": "2peter 2pet 2pe",
    "1John": "1john 1jn", "2John": "2john 2jn", "3John": "3john 3jn", "Jude": "jude",
    "Rev": "revelation rev re apocalypse",
}
_ALIAS = {a: osis for osis, names in _BOOKS.items() for a in names.split()}

_OSIS_POINT = re.compile(r"^(?:Bible:)?([1-3]?[A-Za-z]+)\.(\d+)(?:\.(\d+))?$")
_DIV = re.compile(r"<div(\d)\b([^>]*)>")
_ATTR_TITLE = re.compile(r'\btitle="([^"]*)"')
_ATTR_ID = re.compile(r'\bid="([^"]*)"')
_SCRIPCOM = re.compile(r"<scripCom\b([^>]*)>")
_SCRIPREF = re.compile(r"<scripRef\b([^>]*)>")
_OSIS = re.compile(r'\bosisRef="([^"]*)"')
_TYPE = re.compile(r'\btype="([^"]*)"')
_TAG = re.compile(r"<[^>]+>")
_LANG = re.compile(r"-(lat|grc|fra|deu|ita|spa|syr|heb|arm|cop|ara|nld|rus|swe|enm|gmh|hrv|por|pol|ces)_")


def parse_osis_point(text: str):
    """'Rom.5.12' -> ('Rom', 5, 12); 'Rom.5' -> ('Rom', 5, None); else None."""
    m = _OSIS_POINT.match(text)
    if not m:
        return None
    book, ch, v = m.group(1), int(m.group(2)), m.group(3)
    return book, ch, (int(v) if v is not None else None)


def parse_osis_ref(value: str):
    """An osisRef attribute -> list of (book, start, end) with ordinal positions.

    A ref is space-separated tokens, each a point or `a-b` range. A token
    that does not parse is skipped and counted by the caller, not guessed.
    """
    spans, bad = [], 0
    for token in value.split():
        ends = token.split("-")
        if len(ends) > 2:
            bad += 1
            continue
        pts = [parse_osis_point(e) for e in ends]
        if any(p is None for p in pts) or pts[0][0] != pts[-1][0]:
            bad += 1
            continue
        a, b = pts[0], pts[-1]
        start = a[1] * _CH + (a[2] if a[2] is not None else 0)
        end = b[1] * _CH + (b[2] if b[2] is not None else _LAST_VERSE)
        if len(ends) == 1 and a[2] is not None:
            end = start
        if end < start:
            bad += 1
            continue
        spans.append((a[0], start, end))
    return spans, bad


def parse_query(text: str):
    """'Romans 5:12-21' / 'Rom 5' / '1 Cor 13:4' -> (osis book, start, end), or raise ValueError."""
    m = re.match(r"^\s*([1-3]?\s*[A-Za-z][A-Za-z .]*?)\s*\.?\s*(\d+)(?:\s*[:.]\s*(\d+))?(?:\s*[-–]\s*(?:(\d+)\s*[:.]\s*)?(\d+))?\s*$", text)
    if not m:
        raise ValueError(f"cannot read a passage from {text!r}; try 'Romans 5:12' or 'Matt 5-7'")
    name = re.sub(r"[ .]", "", m.group(1)).lower()
    book = _ALIAS.get(name)
    if book is None:
        raise ValueError(f"unknown book {m.group(1).strip()!r}")
    ch, v, ech_or_v, ev = int(m.group(2)), m.group(3), m.group(4), m.group(5)
    if v is None and ev is not None:  # 'Matt 5-7' means chapters 5 to 7
        return book, ch * _CH, int(ev) * _CH + _LAST_VERSE
    if v is None:
        return book, ch * _CH, ch * _CH + _LAST_VERSE
    start = ch * _CH + int(v)
    if ev is None:
        return book, start, start
    if ech_or_v is not None:
        return book, start, int(ech_or_v) * _CH + int(ev)
    return book, start, ch * _CH + int(ev)


def _file_language(name: str) -> str:
    m = _LANG.search(name)
    return m.group(1) if m else "eng"


def scan_file(path: Path):
    """Yield one record per scripCom and scripRef, in file order.

    `section` is (title, id, work): the innermost open div and the title of the open top-level div, which names the work. Divs are tracked by
    their opening tag; the volume's own nesting is not rebuilt, since a
    closing tag is not needed to know which div an inline tag sits in
    until the next opening div tag supersedes it.
    """
    section = ("", "", "")
    bad = 0
    with path.open(encoding="utf-8", errors="replace") as fh:
        for lineno, line in enumerate(fh, 1):
            for m in _DIV.finditer(line):
                t, i = _ATTR_TITLE.search(m.group(2)), _ATTR_ID.search(m.group(2))
                title = html.unescape(t.group(1)) if t else ""
                work = title if m.group(1) == "1" else section[2]
                section = (title, i.group(1) if i else "", work)
            for m in _SCRIPCOM.finditer(line):
                o = _OSIS.search(m.group(1))
                if not o:
                    bad += 1
                    continue
                ty = _TYPE.search(m.group(1))
                kind = "cites" if ty and ty.group(1) == "Citation" else "treats"
                yield kind, lineno, section, o.group(1), (ty.group(1) if ty else "")
            for m in _SCRIPREF.finditer(line):
                o = _OSIS.search(m.group(1))
                if not o:
                    bad += 1
                    continue
                yield "cites", lineno, section, o.group(1), ""
    if bad:
        yield "unreadable", 0, ("", "", ""), "", str(bad)


_SCHEMA = """
CREATE TABLE hits(
  book TEXT, start INTEGER, end INTEGER, kind TEXT, tag_type TEXT,
  file TEXT, line INTEGER, section_title TEXT, section_id TEXT, work_title TEXT, lang TEXT);
CREATE INDEX hits_by_passage ON hits(book, start, end);
CREATE TABLE skipped(file TEXT, unreadable_tags INTEGER, unreadable_refs INTEGER);
"""


def build(db_path: Path = DB_PATH, texts_dir: Path = TEXTS_DIR) -> dict:
    if db_path.exists():
        db_path.unlink()
    con = sqlite3.connect(db_path)
    con.executescript(_SCHEMA)
    totals = {"files": 0, "treats": 0, "cites": 0, "unreadable_refs": 0}
    for path in sorted(texts_dir.glob("*.xml")):
        rows, untagged, badref = [], 0, 0
        lang = _file_language(path.name)
        for kind, lineno, (title, sid, work), osis, ty in scan_file(path):
            if kind == "unreadable":
                untagged = int(ty)
                continue
            spans, bad = parse_osis_ref(osis)
            badref += bad
            for book, start, end in spans:
                rows.append((book, start, end, kind, ty, path.name, lineno, title, sid, work, lang))
        if not rows:
            continue
        con.executemany("INSERT INTO hits VALUES (?,?,?,?,?,?,?,?,?,?,?)", rows)
        con.execute("INSERT INTO skipped VALUES (?,?,?)", (path.name, untagged, badref))
        totals["files"] += 1
        totals["treats"] += sum(r[3] == "treats" for r in rows)
        totals["cites"] += sum(r[3] == "cites" for r in rows)
        totals["unreadable_refs"] += badref
    con.commit()
    con.close()
    return totals


def _atlas_windows() -> dict:
    out = {}
    path = MAP_DIR / "ATLAS-TARGETS.md"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 5 and cells[0].startswith("`"):
                out[cells[0].strip("`")] = (cells[1], cells[2])
    return out


def _file_mappings() -> dict:
    """file -> [(atlas_id, role)], read from the generated buckets."""
    import yaml
    out = {}
    for bucket in sorted(MAP_DIR.glob("*.yaml")):
        if bucket.name in ("AUTHOR-IDS.yaml", "PAIRS.yaml", "UNATTRIBUTED.yaml", "WORKS.yaml"):
            continue
        data = yaml.safe_load(bucket.read_text(encoding="utf-8")) or {}
        for w in data.get("works", []) if isinstance(data, dict) else []:
            f = w.get("source_file")
            if f:
                out.setdefault(f, set()).add((data.get("atlas_id", bucket.stem), w.get("role", "")))
    return {f: sorted(v) for f, v in out.items()}


def _extract(path: Path, lineno: int, kind: str, width: int = 280) -> str:
    """Verbatim text at a hit, tag-stripped. For a section that treats the
    passage, the first prose after the opening tag; for a citation, the
    sentence window around it on its own line."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if kind == "treats":
        buf = []
        for ln in lines[lineno:lineno + 40]:
            t = html.unescape(_TAG.sub(" ", ln))
            t = re.sub(r"\s+", " ", t).strip(" —-")
            if t:
                buf.append(t)
            if sum(len(b) for b in buf) > width:
                break
        text = " ".join(buf)
    else:
        text = re.sub(r"\s+", " ", html.unescape(_TAG.sub(" ", lines[lineno - 1]))).strip()
    return text[:width] + ("..." if len(text) > width else "")


def _verse_tokens(rest: str, book_label: str):
    """'2:14a, 22-32' -> [(start, end), ...]; a chapter with no verse is the whole chapter."""
    spans, ch = [], None
    for tok in [x for x in re.split(r"\s*,\s*", rest.strip()) if x]:
        tok = re.sub(r"(?<=\d)[a-z]\b", "", tok)
        m = re.match(r"^(?:(\d+)\s*:\s*)?(\d+)(?:\s*-\s*(?:(\d+)\s*:\s*)?(\d+))?$", tok)
        if not m:
            raise ValueError(f"cannot read {tok!r} in {book_label} {rest!r}")
        c1, v1, c2, v2 = m.groups()
        if c1 is not None:
            ch = int(c1)
            start = ch * _CH + int(v1)
            end = start if v2 is None else (int(c2) if c2 else ch) * _CH + int(v2)
        elif ch is None:  # a bare number first: a whole chapter, or chapters 'a-b'
            start = int(v1) * _CH
            end = (int(v2) if v2 else int(v1)) * _CH + _LAST_VERSE
            spans.append((start, end))
            continue
        else:  # a verse or verse range in the chapter already open
            start = ch * _CH + int(v1)
            end = start if v2 is None else (int(c2) if c2 else ch) * _CH + int(v2)
        if end < start:
            raise ValueError(f"range runs backwards: {tok!r} in {book_label}")
        spans.append((start, end))
    return spans


def parse_readings(text: str):
    """A pastor's list of readings -> [{label, book, spans}], one per reading.

    Readings are separated by ';', newlines or ' or '. A part with no book
    name ('3:1-7' after 'Gen 2:15-17') continues the book before it. Verse
    letters (14a) are dropped, since the index works in whole verses. Raises
    ValueError naming what it could not read; nothing is guessed.
    """
    parts = [p.strip() for p in re.split(r"[;\n]|\s+or\s+", text.replace("\u2013", "-").replace("\u2014", "-")) if p.strip()]
    out, last_book = [], None
    for part in parts:
        m = re.match(r"^((?:[1-3]\s*)?[A-Za-z][A-Za-z.]*(?:\s+[A-Za-z][A-Za-z.]*)*)\s*(\d.*)$", part)
        if m:
            name = re.sub(r"[ .]", "", m.group(1)).lower()
            book = _ALIAS.get(name)
            if book is None:
                raise ValueError(f"unknown book {m.group(1).strip()!r} in {part!r}")
            rest = m.group(2)
        elif re.match(r"^\d", part) and last_book:
            book, rest = last_book, part
        else:
            raise ValueError(f"cannot read a reading from {part!r}")
        last_book = book
        out.append({"label": part, "book": book, "spans": _verse_tokens(rest, book)})
    if not out:
        raise ValueError("no readings found")
    return out


def search_spans(book: str, spans, db_path: Path = DB_PATH, treats_only: bool = False, limit: int = 20):
    """Hits for any of several spans of one book, each hit once, treats first."""
    con = sqlite3.connect(db_path)
    seen, rows = set(), []
    for start, end in spans:
        sql = ("SELECT kind, tag_type, file, line, section_title, section_id, work_title, lang FROM hits "
               "WHERE book=? AND start<=? AND end>=?")
        if treats_only:
            sql += " AND kind='treats'"
        for r in con.execute(sql, [book, end, start]):
            if (r[0], r[2], r[3]) not in seen:
                seen.add((r[0], r[2], r[3]))
                rows.append(r)
    con.close()
    rows.sort(key=lambda r: (r[0] != "treats", r[2], r[3]))
    return rows[:limit], len(rows)


def search(query: str, db_path: Path = DB_PATH, treats_only: bool = False, limit: int = 20):
    book, start, end = parse_query(query)
    con = sqlite3.connect(db_path)
    sql = ("SELECT kind, tag_type, file, line, section_title, section_id, work_title, lang FROM hits "
           "WHERE book=? AND start<=? AND end>=?")
    args = [book, end, start]
    if treats_only:
        sql += " AND kind='treats'"
    sql += " ORDER BY (kind='treats') DESC, file, line"
    rows = con.execute(sql, args).fetchall()
    con.close()
    return rows[:limit], len(rows)


def untagged_leads(book: str, db_path: Path = DB_PATH, min_cites: int = 25):
    """Volumes with no treats tags for `book` that cite it heavily.

    CCEL tags a homily to its passage in some volumes and not in others, so
    a missing TREATS line is not proof that nothing treats the passage. A
    volume that cites a book many times and carries no treats tags may well
    be a commentary on it. These are leads to open and read, never findings.
    """
    con = sqlite3.connect(db_path)
    rows = con.execute(
        "SELECT file, COUNT(*) FROM hits WHERE book=? AND file NOT IN "
        "(SELECT DISTINCT file FROM hits WHERE kind='treats' AND book=?) GROUP BY file "
        "HAVING COUNT(*) >= ? ORDER BY COUNT(*) DESC", (book, book, min_cites)).fetchall()
    con.close()
    return rows


def nearest_treats(book: str, start: int, end: int, db_path: Path = DB_PATH, limit: int = 4):
    """Tagged sections of the same chapter(s) that do not overlap the query.

    A homily is tagged to the verses it opens with, and it may range over
    more. When nothing overlaps, the nearest tagged sections in the same
    chapter are the first places to look.
    """
    lo, hi = (start // _CH) * _CH, (end // _CH) * _CH + _LAST_VERSE
    con = sqlite3.connect(db_path)
    rows = con.execute(
        "SELECT file, line, section_title, start, end FROM hits WHERE book=? AND kind='treats' "
        "AND start<=? AND end>=? AND NOT (start<=? AND end>=?)", (book, hi, lo, end, start)).fetchall()
    con.close()
    rows.sort(key=lambda r: min(abs(r[3] - end), abs(r[4] - start)))
    return rows[:limit]


def _print_rows(rows, windows, maps):
    for kind, ty, f, line, title, sid, work, lang in rows:
        label = "TREATS" if kind == "treats" else "cites "
        english = "English" if lang == "eng" else f"{lang} only (no English in this file)"
        print(f"{label}  {f}:{line}  [{english}]")
        print(f"        work: {work}\n        section: {title or sid}")
        tr = "; ".join(f"{aid} ({role}, {windows.get(aid, ('', ''))[1]})" for aid, role in maps.get(f, [])[:4])
        if tr:
            print(f"        volume mapped to: {tr}")
        print(f"        extract: {_extract(TEXTS_DIR / f, line, kind)}\n")


def _run_readings(text, a):
    try:
        readings = parse_readings(text)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2
    windows, maps = _atlas_windows(), _file_mappings()
    for r in readings:
        rows, total = search_spans(r["book"], r["spans"], a.db, a.treats_only, a.limit)
        n_treats = sum(1 for x in rows if x[0] == "treats")
        print(f"=== {r['label']}  ({total} hit(s); showing {len(rows)}, {n_treats} of them TREATS)\n")
        _print_rows(rows, windows, maps)
        if not n_treats:
            near = nearest_treats(r["book"], min(s for s, _ in r["spans"]), max(e for _, e in r["spans"]), db_path=a.db)
            if near:
                print("NEAREST TAGGED (same chapter, other verses; a homily may range beyond its lemma):")
                for f, line, title, s, e in near:
                    print(f"        {f}:{line}  {title}")
                print()
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("query", nargs="?", help="a passage, e.g. 'Romans 5:12' or 'Matt 5-7'")
    ap.add_argument("--build", action="store_true", help="(re)build cic/texts/PASSAGES.sqlite")
    ap.add_argument("--readings", help="a list of readings, e.g. 'Acts 2:14a, 22-32; Ps 16; 1 Pet 1:3-9; John 20:19-31'")
    ap.add_argument("--treats-only", action="store_true")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--db", type=Path, default=DB_PATH)
    a = ap.parse_args(argv)
    if a.build:
        t = build(a.db)
        print(f"{t['files']} file(s): {t['treats']} treats, {t['cites']} cites; "
              f"{t['unreadable_refs']} reference(s) skipped as unreadable -> {a.db.name}")
        return 0
    if not a.query and not a.readings:
        ap.print_usage()
        return 2
    if not a.db.exists():
        print("no index yet; run with --build first", file=sys.stderr)
        return 2
    if a.readings:
        a.limit = min(a.limit, 5) if a.limit == 20 else a.limit
        return _run_readings(a.readings, a)
    try:
        rows, total = search(a.query, a.db, a.treats_only, a.limit)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2
    windows, maps = _atlas_windows(), _file_mappings()
    print(f"{total} hit(s) for {a.query!r}; showing {len(rows)}. TREATS = a section tagged to the passage; CITES = a mention.\n")
    _print_rows(rows, windows, maps)
    if not any(r[0] == "treats" for r in rows):
        near = nearest_treats(*parse_query(a.query), db_path=a.db)
        if near:
            print("NEAREST TAGGED (in the same chapter; tagged to other verses, but a homily may range beyond its lemma):")
            for f, line, title, s, e in near:
                print(f"        {f}:{line}  {title}")
            print()
    leads = untagged_leads(parse_query(a.query)[0], a.db)
    if leads:
        print("NOT TAGGED: these volumes carry no section tags for this book, so they cannot show as TREATS, "
              "but cite this book heavily. A commentary among them may treat the passage; open and read:")
        for f, n in leads[:8]:
            print(f"        {f}  ({n} citations of this book)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
