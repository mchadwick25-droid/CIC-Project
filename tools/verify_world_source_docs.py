#!/usr/bin/env python3
"""Mechanical consistency checks for a world's Doc_02 (Source Ecology) and
Source_Registry.

Usage:
    python tools/verify_world_source_docs.py <world-code> [--texts DIR]
        [--window START-END] [--tolerance N] [--report FILE]

Reads Build/worlds/<code>/Doc_02_Source_Ecology.md and
Build/worlds/<code>/Source_Registry.md, and the vendored texts directory
(default: cic/texts of this repository). Reads only; writes nothing except
the optional --report file. Output is deterministic: the same inputs give the
same report. The exit status is 1 when any check fails, 0 otherwise.

Checks
  1. texts-exist      Every vendored file named in either document exists.
  2. registry-vocab   Each Registry row is well formed: unique ids, ten cells,
                      Type in P/S/M/L, Confidence A-E, Boundary Status
                      Native/Excluded, Exclusion Reason and Licensed For
                      filled exactly when the schema requires them.
  3. cross-refs       Every "row N" reference in either document names an
                      existing row, and every vendored file a Registry row
                      names is also named in Doc_02.
  4. same-volume      Rows for the same work (same italic title or same file)
                      share a Boundary Status unless a row says why they differ.
  5. absence-claims   A sentence or row that says a source is "not vendored"
                      is checked against the vendored directory: named files
                      must not exist; a named person or work that occurs in a
                      vendored file dated inside the window must be classified
                      in the Registry; an unscoped absence claim must not name
                      a party that a vendored filename carries.
  6. universal-claims "Every Native primary source is <author>'s own writing"
                      must name each Native primary row by a different author.
  7. doc-vs-registry  A Doc_02 sentence that calls a Registry work Native or
                      Excluded agrees with at least one row for that work.
  8. quotes           Each quotation of four or more words that has a cited
                      file and locus occurs there, whitespace-normalised,
                      within the cited lines (plus the tolerance) or in the
                      cited element id.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_WINDOW = (560, 604)
DEFAULT_TOLERANCE = 10

TYPES = set("PSML")
CONFIDENCE = set("ABCDE")
BOUNDARY = {"Native", "Excluded"}
EXCLUSION = {"Out-of-Boundary", "Named Comparandum"}
EMPTY = {"", "—", "-", "–"}
COLUMNS = [
    "#", "Source", "Type", "Confidence", "Boundary Status", "Exclusion Reason",
    "Licensed For", "Verification Note", "Comparandum Note", "Added",
]
DIFFERENCE_MARKERS = (
    "separate matter", "unlike", "whereas", "by contrast", "differs from row",
    "distinct from row",
)
ABSENCE_PATTERNS = [
    re.compile(r"\b(?:not|never)\s+(?:currently\s+)?vendored\b", re.I),
    re.compile(r"\bunvendored\b", re.I),
    re.compile(r"\bnone of which (?:is|are)\s+(?:currently\s+)?vendored\b", re.I),
    re.compile(r"\bno\b[^.;|]{0,160}?\b(?:is|are)\s+(?:currently\s+)?vendored\b", re.I),
]
SCOPE_QUALIFIER = re.compile(r"\bwindow\b|\b560\b|\bin-window\b", re.I)
ENTITY = re.compile(
    r"\b[A-Z][a-z]+(?:\s+(?:the|of|de|von|van)\s+[A-Z][a-z]+|\s+[A-Z][a-z]+)+\b"
)
ENTITY_STOP_FIRST = {
    "The", "This", "That", "These", "Those", "No", "None", "Not", "Doc",
    "Registry", "Article", "Step", "World", "Book", "Named", "Row", "Rows",
    "Source", "Status", "Section", "Part", "Parts", "Library", "Constitution",
    "Construction", "Template", "Open", "Native", "Excluded", "Out", "Added",
}
PARTY_WORD = re.compile(r"\b[A-Z][a-z]{3,}(?:ist|ian|ite)s?\b")
TEXT_FILE = re.compile(r"(?<![/\w.-])[A-Za-z0-9][A-Za-z0-9._-]*\.(?:txt|xml)\b")
HEADER_RANGE = re.compile(r"\(\s*(?:c\.\s*)?(\d{3,4})\s*[-–]\s*(\d{3,4})\b")
LOCUS_ID = re.compile(
    r"\b([a-z0-9]+(?:\.[a-z0-9]+)+)-p(\d+)(?:\s*[–-]\s*p(\d+))?"
)
LINES_LIST = re.compile(
    r"lines?\s+((?:~?\d+(?:\s*[–-]\s*\d+)?(?:\s*(?:,|and)\s*)?)+)", re.I
)
TILDE_RANGE = re.compile(r"~(\d{2,6})(?:\s*[–-]\s*(\d{2,6}))?")
NUMBER_RANGE = re.compile(r"(\d{2,6})(?:\s*[–-]\s*(\d{2,6}))?")


@dataclass
class Finding:
    where: str
    message: str


@dataclass
class CheckResult:
    name: str
    description: str
    checked: str = ""
    failures: list[Finding] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.failures


@dataclass
class Row:
    line: int
    cells: list[str]

    def cell(self, name: str) -> str:
        return self.cells[COLUMNS.index(name)]

    @property
    def rid(self) -> str:
        return self.cell("#").strip()

    @property
    def status(self) -> str:
        return self.cell("Boundary Status").strip()

    @property
    def kind(self) -> str:
        return self.cell("Type").strip()


@dataclass
class World:
    code: str
    doc_path: Path
    reg_path: Path
    doc_lines: list[str]
    reg_lines: list[str]
    rows: list[Row]


TYPOGRAPHIC = str.maketrans({
    "\u00ad": None, "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
})


def collapse(text: str) -> str:
    return " ".join(text.split())


def normalise(text: str) -> str:
    """Whitespace collapsed; soft hyphens dropped; curly quotes made straight."""
    return collapse(text.translate(TYPOGRAPHIC))


def strip_marks(text: str) -> str:
    return text.replace("*", "").replace("`", "")


def split_cells(line: str) -> list[str]:
    body = line.strip().strip("|")
    return [c.strip() for c in body.split("|")]


def parse_registry(lines: list[str]) -> list[Row]:
    rows: list[Row] = []
    for number, line in enumerate(lines, 1):
        if not line.startswith("|"):
            continue
        cells = split_cells(line)
        if cells[0] in ("#", "---") or set(cells[0]) <= set("-: "):
            continue
        rows.append(Row(number, cells))
    return rows


def load_world(repo: Path, code: str) -> World:
    base = repo / "Build" / "worlds" / code
    doc_path = base / "Doc_02_Source_Ecology.md"
    reg_path = base / "Source_Registry.md"
    for path in (doc_path, reg_path):
        if not path.is_file():
            raise SystemExit(f"missing {path}")
    doc_lines = doc_path.read_text(encoding="utf-8").splitlines()
    reg_lines = reg_path.read_text(encoding="utf-8").splitlines()
    return World(code, doc_path, reg_path, doc_lines, reg_lines,
                 parse_registry(reg_lines))


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z*\"(`])", text)
    return [p for p in parts if p.strip()]


def stem_keys(filename: str) -> set[str]:
    stem = re.sub(r"\.(?:txt|xml)$", "", filename)
    keys = {stem.lower()}
    for part in stem.split("_"):
        if re.search(r"\d", part):
            keys.add(part.lower())
    return keys


class Texts:
    """The vendored directory: names, short keys, header date ranges, bodies."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.names = sorted(p.name for p in root.iterdir()
                            if p.suffix in (".txt", ".xml"))
        self.name_set = set(self.names)
        self._key_index: dict[str, list[str]] = {}
        for name in self.names:
            for key in stem_keys(name):
                self._key_index.setdefault(key, []).append(name)
        self._lines: dict[str, list[str]] = {}
        self._raw: dict[str, str] = {}

    def resolve(self, token: str) -> str | None:
        token = token.strip("`").lower()
        if token in {n.lower() for n in self.name_set}:
            return next(n for n in self.names if n.lower() == token)
        hits = self._key_index.get(re.sub(r"\.(?:txt|xml)$", "", token), [])
        return hits[0] if len(hits) == 1 else None

    def raw(self, name: str) -> str:
        if name not in self._raw:
            self._raw[name] = (self.root / name).read_text(
                encoding="utf-8", errors="replace")
        return self._raw[name]

    def lines(self, name: str) -> list[str]:
        if name not in self._lines:
            self._lines[name] = self.raw(name).splitlines()
        return self._lines[name]

    def header_range(self, name: str) -> tuple[int, int] | None:
        if name.endswith(".xml"):
            return None
        head = "\n".join(self.lines(name)[:80])
        match = HEADER_RANGE.search(head)
        if not match:
            return None
        return int(match.group(1)), int(match.group(2))

    def window_files(self, window: tuple[int, int]) -> list[str]:
        out = []
        for name in self.names:
            span = self.header_range(name)
            if span and span[0] <= window[1] and span[1] >= window[0]:
                out.append(name)
        return out


def key_in_text(name: str, haystack: str) -> bool:
    lowered = haystack.lower()
    return any(key in lowered for key in stem_keys(name))


def check_texts_exist(world: World, texts: Texts) -> CheckResult:
    result = CheckResult(
        "texts-exist", "Every vendored file named in Doc_02 or the Registry exists.")
    named: dict[str, list[str]] = {}
    for label, lines in (("Doc_02", world.doc_lines), ("Registry", world.reg_lines)):
        for number, line in enumerate(lines, 1):
            for match in TEXT_FILE.finditer(line):
                named.setdefault(match.group(0), []).append(f"{label}:{number}")
    for filename in sorted(named):
        if filename not in texts.name_set:
            result.failures.append(Finding(
                ", ".join(named[filename][:3]), f"`{filename}` is not in the texts directory"))
    result.checked = f"{len(named)} distinct file names"
    return result


def check_registry_vocab(world: World) -> CheckResult:
    result = CheckResult(
        "registry-vocab",
        "Each Registry row is well formed and uses the template's vocabulary.")
    seen: set[str] = set()
    for row in world.rows:
        where = f"Registry:{row.line}"
        if len(row.cells) != len(COLUMNS):
            result.failures.append(Finding(
                where, f"row has {len(row.cells)} cells, expected {len(COLUMNS)}"))
            continue
        rid = row.rid
        if rid in seen:
            result.failures.append(Finding(where, f"row id {rid} repeated"))
        seen.add(rid)
        letters = re.findall(r"[A-Za-z]", row.kind)
        if not letters or not set(letters) <= TYPES:
            result.failures.append(Finding(where, f"row {rid}: Type '{row.kind}' not in P/S/M/L"))
        conf = row.cell("Confidence")
        tiers = re.findall(r"(?:^|;\s*)([A-Z])\b", conf)
        if not tiers or not set(tiers) <= CONFIDENCE:
            result.failures.append(Finding(where, f"row {rid}: Confidence '{conf}' not A-E"))
        if row.status not in BOUNDARY:
            result.failures.append(Finding(
                where, f"row {rid}: Boundary Status '{row.status}' not Native/Excluded"))
            continue
        reason = row.cell("Exclusion Reason").strip()
        licensed = row.cell("Licensed For").strip()
        comparandum = row.cell("Comparandum Note").strip()
        if row.status == "Excluded":
            if reason not in EXCLUSION:
                result.failures.append(Finding(
                    where, f"row {rid}: Excluded needs Exclusion Reason Out-of-Boundary or Named Comparandum, found '{reason}'"))
            if licensed not in EMPTY:
                result.failures.append(Finding(
                    where, f"row {rid}: Excluded row carries Licensed For text"))
            if reason == "Named Comparandum" and comparandum in EMPTY:
                result.failures.append(Finding(
                    where, f"row {rid}: Named Comparandum needs a Comparandum Note"))
        else:
            if reason not in EMPTY:
                result.failures.append(Finding(
                    where, f"row {rid}: Native row carries Exclusion Reason '{reason}'"))
            if licensed in EMPTY:
                result.failures.append(Finding(
                    where, f"row {rid}: Native row has no Licensed For"))
        if row.cell("Added").strip() in EMPTY:
            result.failures.append(Finding(where, f"row {rid}: Added is empty"))
    result.checked = f"{len(world.rows)} rows"
    return result


def row_references(text: str) -> list[str]:
    """Row ids named after 'row'/'rows' in text, expanding integer ranges."""
    ids: list[str] = []
    for match in re.finditer(r"\brows?\s+(?=\d)", text):
        tail = text[match.end():match.end() + 120]
        position = 0
        while True:
            token = re.match(
                r"(\d+[a-z]?)(?:\s*(?:[–-]|to)\s*(\d+))?", tail[position:])
            if not token:
                break
            first, last = token.group(1), token.group(2)
            if last and first.isdigit():
                ids.extend(str(n) for n in range(int(first), int(last) + 1))
            else:
                ids.append(first)
            position += token.end()
            glue = re.match(
                r"(?:\s*\([a-z ]+\))?\s*(?:,\s*and|,|and)?\s*(?=\d)", tail[position:])
            if not glue or not glue.end():
                break
            position += glue.end()
    return ids


def check_cross_refs(world: World, texts: Texts) -> CheckResult:
    result = CheckResult(
        "cross-refs",
        "Row references resolve, and each file a row names is also named in Doc_02.")
    row_ids = {row.rid for row in world.rows}
    total = 0
    for label, lines in (("Doc_02", world.doc_lines), ("Registry", world.reg_lines)):
        for number, line in enumerate(lines, 1):
            for rid in row_references(strip_marks(line)):
                total += 1
                if rid not in row_ids:
                    result.failures.append(Finding(
                        f"{label}:{number}", f"reference to row {rid}, which does not exist"))
    doc_text = "\n".join(world.doc_lines)
    file_count = 0
    for row in world.rows:
        for match in TEXT_FILE.finditer(strip_marks(" ".join(row.cells))):
            file_count += 1
            filename = match.group(0)
            if not key_in_text(filename, doc_text):
                result.failures.append(Finding(
                    f"Registry:{row.line}",
                    f"row {row.rid} names `{filename}`, which Doc_02 does not mention"))
    result.checked = f"{total} row references, {file_count} Registry file names"
    return result


def work_title(row: Row) -> str | None:
    match = re.search(r"\*([^*]{4,}?)\*", row.cell("Source"))
    return collapse(match.group(1)).lower() if match else None


def check_same_volume(world: World) -> CheckResult:
    result = CheckResult(
        "same-volume",
        "Rows for one work or one file share a Boundary Status unless a note says why.")
    groups: dict[str, list[Row]] = {}
    for row in world.rows:
        if len(row.cells) != len(COLUMNS):
            continue
        title = work_title(row)
        if title:
            groups.setdefault(f"work: {title}", []).append(row)
        for match in TEXT_FILE.finditer(row.cell("Source")):
            groups.setdefault(f"file: {match.group(0)}", []).append(row)
    compared = 0
    for key in sorted(groups):
        rows = groups[key]
        if len(rows) < 2:
            continue
        compared += 1
        statuses = {row.status for row in rows}
        if len(statuses) == 1:
            continue
        explained = any(
            marker in " ".join(r.cell("Verification Note") + " " + r.cell("Exclusion Reason")).lower()
            for r in rows for marker in DIFFERENCE_MARKERS)
        if not explained:
            detail = ", ".join(f"row {r.rid} {r.status}" for r in rows)
            result.failures.append(Finding(
                f"Registry:{rows[0].line}",
                f"{key} is classified differently without a stated reason ({detail})"))
    result.checked = f"{compared} multi-row groups"
    return result


def absence_units(world: World) -> list[tuple[str, str]]:
    units: list[tuple[str, str]] = []
    for number, line in enumerate(world.doc_lines, 1):
        if line.startswith("|") or not line.strip():
            continue
        for sentence in sentences(line):
            if any(p.search(sentence) for p in ABSENCE_PATTERNS):
                units.append((f"Doc_02:{number}", sentence))
    for row in world.rows:
        if len(row.cells) != len(COLUMNS):
            continue
        joined = " ".join((row.cell("Source"), row.cell("Verification Note")))
        if any(p.search(joined) for p in ABSENCE_PATTERNS):
            units.append((f"Registry:{row.line}", joined))
    tail_start = next(
        (i for i, l in enumerate(world.reg_lines) if l.startswith("## ")), None)
    if tail_start is not None:
        for number in range(tail_start, len(world.reg_lines)):
            for sentence in sentences(world.reg_lines[number]):
                if any(p.search(sentence) for p in ABSENCE_PATTERNS):
                    units.append((f"Registry:{number + 1}", sentence))
    return units


def entity_phrases(text: str) -> list[str]:
    found: list[str] = []
    for match in ENTITY.finditer(re.sub(r"\*[^*]+\*", " ", text)):
        phrase = match.group(0)
        if phrase.split()[0] in ENTITY_STOP_FIRST:
            continue
        if phrase not in found:
            found.append(phrase)
    return found


def scan_entities(texts: Texts, names: list[str],
                  phrases: set[str]) -> dict[str, list[str]]:
    hits: dict[str, list[str]] = {p: [] for p in phrases}
    for name in names:
        data = (texts.root / name).read_text(encoding="utf-8", errors="replace")
        pending = [p for p in phrases if p.split()[-1] in data]
        if not pending:
            continue
        flat = collapse(data)
        for phrase in pending:
            if phrase in flat:
                hits[phrase].append(name)
    return hits


def check_absence_claims(world: World, texts: Texts,
                         window: tuple[int, int]) -> CheckResult:
    result = CheckResult(
        "absence-claims",
        "Statements that a source is not vendored hold against the vendored directory.")
    units = absence_units(world)
    registry_text = "\n".join(world.reg_lines)
    window_names = texts.window_files(window)
    unit_phrases = {where: entity_phrases(text) for where, text in units}
    all_phrases = {p for phrases in unit_phrases.values() for p in phrases}
    hits = scan_entities(texts, window_names, all_phrases)
    tokens = {n: set(re.split(r"[-_.]", n.lower())) for n in texts.names}
    for where, raw_text in units:
        text = strip_marks(raw_text)
        for match in TEXT_FILE.finditer(text):
            if match.group(0) in texts.name_set:
                result.failures.append(Finding(
                    where, f"says `{match.group(0)}` is not vendored, but it exists"))
        for phrase in unit_phrases[where]:
            for name in hits.get(phrase, []):
                if not key_in_text(name, registry_text):
                    result.failures.append(Finding(
                        where,
                        f"absence claim names '{phrase}', which occurs in `{name}` "
                        f"(dated {texts.header_range(name)[0]}-{texts.header_range(name)[1]}, "
                        "inside the window); the Registry does not classify that file"))
        if not SCOPE_QUALIFIER.search(text):
            for word in sorted(set(PARTY_WORD.findall(text))):
                lowered = word.lower()
                matches = sorted(n for n, toks in tokens.items()
                                 if any(t.startswith(lowered) for t in toks))
                if matches and word not in ENTITY_STOP_FIRST:
                    result.failures.append(Finding(
                        where,
                        f"unscoped absence claim names '{word}', but vendored files "
                        f"carry it: {', '.join('`' + m + '`' for m in matches[:3])}; "
                        "scope the claim to the window"))
    result.checked = (f"{len(units)} absence statements; "
                      f"{len(all_phrases)} named entities searched in "
                      f"{len(window_names)} in-window files")
    return result


def author_key(row: Row) -> str:
    source = strip_marks(row.cell("Source"))
    return collapse(source.split(",")[0])


def check_universal_claims(world: World) -> CheckResult:
    result = CheckResult(
        "universal-claims",
        "'Every Native primary source is <author>'s own writing' names each exception.")
    native = [r for r in world.rows
              if len(r.cells) == len(COLUMNS) and r.status == "Native" and "P" in r.kind]
    keys = [author_key(r) for r in native]
    if not keys:
        result.checked = "no Native primary rows"
        return result
    dominant = max(sorted(set(keys)), key=keys.count)
    outliers = sorted({k for k in keys if k != dominant})
    pattern = re.compile(r"\b(?:every|all)\s+Native\s+primary\s+sources?\b", re.I)
    claims = 0
    for number, line in enumerate(world.doc_lines, 1):
        for sentence in sentences(line):
            text = strip_marks(sentence)
            if not pattern.search(text) or "in §" in text:
                continue
            if not re.search(r"own writing|his own|her own", text, re.I):
                continue
            claims += 1
            for outlier in outliers:
                if outlier.lower() not in text.lower():
                    result.failures.append(Finding(
                        f"Doc_02:{number}",
                        f"universal claim about Native primary sources does not name the "
                        f"Native primary row by '{outlier}' (dominant author '{dominant}')"))
    result.checked = (f"{claims} universal claims; dominant author '{dominant}', "
                      f"{len(outliers)} other Native primary authors")
    return result


def check_doc_vs_registry(world: World) -> CheckResult:
    result = CheckResult(
        "doc-vs-registry",
        "Doc_02 sentences that call a Registry work Native or Excluded agree with its rows.")
    by_title: dict[str, set[str]] = {}
    for row in world.rows:
        if len(row.cells) == len(COLUMNS):
            title = work_title(row)
            if title:
                by_title.setdefault(title, set()).add(row.status)
    judged = 0
    for number, line in enumerate(world.doc_lines, 1):
        if line.startswith("|"):
            continue
        for sentence in sentences(line):
            plain = strip_marks(sentence).lower()
            claims = set()
            if re.search(r"\bexcluded\b", plain):
                claims.add("Excluded")
            if re.search(r"\bnot native\b|\bdoes not treat as native\b", plain):
                claims.add("Excluded")
            elif re.search(r"\bnative\b", plain) and "excluded" not in plain:
                claims.add("Native")
            if len(claims) != 1:
                continue
            claim = next(iter(claims))
            for title, statuses in sorted(by_title.items()):
                if re.search(r"\b" + re.escape(title) + r"\b", plain):
                    judged += 1
                    if claim not in statuses:
                        result.failures.append(Finding(
                            f"Doc_02:{number}",
                            f"sentence calls '{title}' {claim}; Registry rows say "
                            f"{', '.join(sorted(statuses))}"))
    result.checked = f"{judged} sentence/work pairs"
    return result


def line_ranges(text: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for match in LINES_LIST.finditer(text):
        for token in NUMBER_RANGE.finditer(match.group(1)):
            low = int(token.group(1))
            high = int(token.group(2) or token.group(1))
            ranges.append((low, high))
    for token in TILDE_RANGE.finditer(text):
        low = int(token.group(1))
        high = int(token.group(2) or token.group(1))
        if (low, high) not in ranges:
            ranges.append((low, high))
    return ranges


def line_files(text: str, texts: Texts) -> list[str]:
    names: list[str] = []
    for token in re.findall(r"[A-Za-z0-9][A-Za-z0-9._-]*", text):
        if token.endswith((".txt", ".xml")) or re.search(r"\d", token):
            name = texts.resolve(token)
            if name and name not in names:
                names.append(name)
    return names


def extract_quotes(line: str) -> list[str] | None:
    positions = [i for i, ch in enumerate(line) if ch == '"']
    if len(positions) % 2:
        return None
    return [line[positions[i] + 1:positions[i + 1]]
            for i in range(0, len(positions), 2)]


def quote_pieces(quote: str) -> list[str]:
    pieces = re.split(r"\.\.\.|…|\[[^\]]*\]", quote)
    return [collapse(p).strip(" ,;:") for p in pieces if len(p.split()) >= 3]


TAG = re.compile(r"<[^>]+>")
NOTE = re.compile(r"<note\b.*?</note>", re.S)
PARAGRAPH_TAG = re.compile(r"<p\b[^>]*>|</p>")


def tag_free(raw: str) -> list[str]:
    """Plain-text variants of an XML fragment: tags joined, and tags spaced."""
    return [normalise(TAG.sub("", raw)), normalise(TAG.sub(" ", raw))]


def xml_element_texts(texts: Texts, name: str, element_id: str) -> list[str]:
    """Text of the <p> or <div> carrying element_id, with and without notes.

    A paragraph's text runs to its matching </p>, so endnote paragraphs nested
    inside it do not end it early. For a div the opening tag's title and the
    text that follows it are returned, which covers letter headings."""
    raw = texts.raw(name)
    marker = f'id="{element_id}"'
    start = raw.find(marker)
    if start < 0:
        return []
    open_at = raw.rfind("<", 0, start)
    opening = raw[open_at:raw.find(">", start) + 1]
    if opening.startswith("<p"):
        depth = 0
        end = len(raw)
        for tag in PARAGRAPH_TAG.finditer(raw, open_at):
            depth += 1 if tag.group(0).startswith("<p") else -1
            if depth == 0:
                end = tag.end()
                break
        fragment = raw[open_at:end]
        return tag_free(fragment) + tag_free(NOTE.sub("", fragment))
    title = re.search(r'title="([^"]*)"', opening)
    head = (title.group(1) if title else "") + " " + raw[open_at + len(opening):open_at + len(opening) + 600]
    return tag_free(head)


def window_texts(texts: Texts, name: str, low: int, high: int,
                 tolerance: int) -> list[str]:
    lines = texts.lines(name)
    start = max(0, low - 1 - tolerance)
    stop = min(len(lines), high + tolerance)
    chunk = " ".join(lines[start:stop])
    return tag_free(chunk) if name.endswith(".xml") else [normalise(chunk)]


def check_quotes(world: World, texts: Texts, tolerance: int,
                 reference: list[Path]) -> CheckResult:
    result = CheckResult(
        "quotes",
        "Quotations with a cited file and locus occur there (whitespace collapsed, "
        "soft hyphens dropped, curly quotes made straight).")
    xml_names = sorted({
        n for lines in (world.doc_lines, world.reg_lines)
        for ln in lines for n in line_files(ln, texts) if n.endswith(".xml")})
    named_files = sorted({
        n for lines in (world.doc_lines, world.reg_lines)
        for ln in lines for n in line_files(ln, texts)})
    haystacks = {n: (normalise(texts.raw(n)) if n.endswith(".txt")
                     else tag_free(texts.raw(n))[0]) for n in named_files}
    for path in reference:
        haystacks[path.name] = normalise(path.read_text(encoding="utf-8"))
    elsewhere: list[str] = []
    pieces_checked = 0
    quotes_checked = 0
    file_only = 0
    file_only_missed: list[str] = []
    unlocated: list[str] = []
    unbalanced = 0
    for label, lines in (("Doc_02", world.doc_lines), ("Registry", world.reg_lines)):
        for number, raw in enumerate(lines, 1):
            if '"' not in raw:
                continue
            line = raw.replace("*", "").replace("`", "")
            quotes = extract_quotes(line)
            if quotes is None:
                unbalanced += 1
                continue
            files = line_files(line, texts)
            ranges = line_ranges(line)
            loci = [(m.group(1), int(m.group(2)), int(m.group(3) or m.group(2)))
                    for m in LOCUS_ID.finditer(line)]
            for quote in quotes:
                pieces = [normalise(p) for p in quote_pieces(quote)]
                if sum(len(p.split()) for p in pieces) < 4:
                    continue
                if not (files or loci):
                    unlocated.append(f"{label}:{number}")
                    continue
                if not (ranges or loci):
                    file_only += 1
                    body = [normalise(texts.raw(n)) if n.endswith(".txt")
                            else tag_free(texts.raw(n))[0] for n in files]
                    if not all(any(p in b for b in body) for p in pieces):
                        file_only_missed.append(f"{label}:{number}")
                    continue
                quotes_checked += 1
                for piece in pieces:
                    pieces_checked += 1
                    if piece_found(piece, texts, files, ranges, loci,
                                   xml_names, tolerance):
                        continue
                    if any(piece in h for h in haystacks.values()):
                        elsewhere.append(f"{label}:{number}")
                        continue
                    shown = piece if len(piece) <= 90 else piece[:87] + "..."
                    result.failures.append(Finding(
                        f"{label}:{number}",
                        f"quotation not found in its cited locus or any named file: \"{shown}\""))
    result.checked = (f"{quotes_checked} quotations ({pieces_checked} pieces) with a "
                      f"cited line range or element id; tolerance {tolerance} lines")
    if elsewhere:
        result.notes.append(
            f"{len(elsewhere)} quotation pieces were found in a named file or reference "
            f"document but not at the locus on their line ({', '.join(elsewhere)}); "
            "informational.")
    if file_only:
        result.notes.append(
            f"{file_only} quotations name a file but no line range or element id; "
            f"searched in the whole file, {file_only - len(file_only_missed)} found"
            + (f", not found at {', '.join(file_only_missed)} (informational)"
               if file_only_missed else "") + ".")
    if unlocated:
        result.notes.append(
            f"{len(unlocated)} quotations of four or more words name no file or element id "
            f"on their line and were not checked ({', '.join(unlocated)}).")
    if unbalanced:
        result.notes.append(
            f"{unbalanced} lines have an odd number of quotation marks and were not checked.")
    return result


def piece_found(piece: str, texts: Texts, files: list[str],
                ranges: list[tuple[int, int]], loci: list[tuple[str, int, int]],
                xml_names: list[str], tolerance: int) -> bool:
    for prefix, first, last in loci:
        for number in range(first, last + 1):
            for name in xml_names:
                for variant in xml_element_texts(texts, name, f"{prefix}-p{number}"):
                    if piece in variant:
                        return True
        for name in xml_names:
            for variant in xml_element_texts(texts, name, prefix):
                if piece in variant:
                    return True
    for name in files:
        for low, high in ranges:
            if low <= len(texts.lines(name)) and any(
                    piece in v for v in window_texts(texts, name, low, high, tolerance)):
                return True
    return False


def reference_documents(repo: Path) -> list[Path]:
    template = (repo / "Build" / "reference" / "L3B-World-Build-Methodology"
                / "Source_Registry_Template.md")
    return [template] if template.is_file() else []


def parse_window(world: World, override: str | None) -> tuple[int, int]:
    if override:
        low, high = re.split(r"[-–]", override)
        return int(low), int(high)
    match = re.search(r"(\d{3})\s*[–-]\s*(\d{3})\s+window", "\n".join(world.doc_lines))
    if match:
        return int(match.group(1)), int(match.group(2))
    return DEFAULT_WINDOW


def render(world: World, texts_label: str, window: tuple[int, int],
           results: list[CheckResult]) -> str:
    out = [
        f"# Doc_02 and Source Registry checks: {world.code}",
        "",
        f"- Documents: `Build/worlds/{world.code}/Doc_02_Source_Ecology.md` "
        f"({len(world.doc_lines)} lines) and `Build/worlds/{world.code}/Source_Registry.md` "
        f"({len(world.rows)} rows)",
        f"- Vendored texts: `{texts_label}`",
        f"- Window used for dating checks: {window[0]}-{window[1]}",
        f"- Checks run: {len(results)}; passed: {sum(r.passed for r in results)}; "
        f"failed: {sum(not r.passed for r in results)}",
        "",
        "| Check | Result | Scope |",
        "|---|---|---|",
    ]
    for r in results:
        out.append(f"| `{r.name}` | {'PASS' if r.passed else 'FAIL'} | {r.checked} |")
    out.append("")
    for r in results:
        out.append(f"## {r.name}: {'PASS' if r.passed else 'FAIL'}")
        out.append("")
        out.append(r.description)
        out.append("")
        out.append(f"Checked: {r.checked}.")
        for note in r.notes:
            out.append(f"- Note: {note}")
        for f in r.failures:
            out.append(f"- FAIL {f.where}: {f.message}")
        out.append("")
    overall = "PASS" if all(r.passed for r in results) else "FAIL"
    out.append(f"Overall: {overall}")
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("world", help="world registry code, e.g. rcg")
    parser.add_argument("--texts", type=Path, default=REPO_ROOT / "cic" / "texts")
    parser.add_argument("--repo", type=Path, default=REPO_ROOT)
    parser.add_argument("--window", help="START-END years; default read from Doc_02")
    parser.add_argument("--tolerance", type=int, default=DEFAULT_TOLERANCE)
    parser.add_argument("--report", type=Path, help="also write the report here")
    args = parser.parse_args(argv)

    world = load_world(args.repo, args.world)
    texts = Texts(args.texts)
    window = parse_window(world, args.window)
    results = [
        check_texts_exist(world, texts),
        check_registry_vocab(world),
        check_cross_refs(world, texts),
        check_same_volume(world),
        check_absence_claims(world, texts, window),
        check_universal_claims(world),
        check_doc_vs_registry(world),
        check_quotes(world, texts, args.tolerance, reference_documents(args.repo)),
    ]
    label = "cic/texts" if args.texts.parts[-2:] == ("cic", "texts") else args.texts.name
    report = render(world, label, window, results)
    sys.stdout.write(report)
    if args.report:
        args.report.write_text(report, encoding="utf-8")
    return 0 if all(r.passed for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
