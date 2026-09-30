"""The project lead's re-baseline declaration for a world built before the
record-native process: which pre-V2.0 approval-history failures the handoff
gate reports as accepted instead of failing on."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from .common import PLACEHOLDER, REPO_ROOT, Finding, markdown_tables, read_text, rel, world_dir
from .rounds import ROUND_CAP, cycle_rounds, review_files
from .verdicts import CLEARED, verdict_word

CHECK_ID = "handoff-declaration"
CAP_CHECK = "review-round-cap"
WORDING_CHECK = "verdict-wording"
ACCEPTABLE_CHECKS = (CAP_CHECK, WORDING_CHECK)
DECLARER = "project lead"
HEADER_KEYS = ("World", "Declared by", "Date", "Process version", "Scope")
OPEN_SECTION = "Findings carried open and how each will be checked"
DOCUMENTS = tuple(range(0, 11))
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_REVIEWISH = re.compile(r"review|spotcheck|round|verification|history|superseded", re.IGNORECASE)


def doc_label(doc: int) -> str:
    return "Step0" if doc == 0 else f"Doc_{doc:02d}"


def parse_doc_label(cell: str) -> int | None:
    text = re.sub(r"[`*]", "", cell).strip()
    if re.fullmatch(r"Step[\s_]?0", text, re.IGNORECASE):
        return 0
    m = re.fullmatch(r"Doc[\s_]?0*(\d+)", text, re.IGNORECASE)
    return int(m.group(1)) if m and 1 <= int(m.group(1)) <= 10 else None


def declaration_path(code: str, root: Path = REPO_ROOT) -> Path:
    return world_dir(code, root) / "build" / f"{code}_Rebaseline_Declaration.md"


def document_path(code: str, doc: int, root: Path = REPO_ROOT) -> Path | None:
    base = world_dir(code, root)
    if not base.is_dir():
        return None
    pattern = r"(?:[\w]+_)?Step_?0(?!\d)" if doc == 0 else rf"(?:{re.escape(code)}_)?Doc_?0*{doc}(?!\d)"
    for path in sorted(base.glob("*.md")):
        if not _REVIEWISH.search(path.name) and re.match(pattern, path.name):
            return path
    return None


@dataclass(frozen=True)
class State:
    files: int
    rounds: int
    latest_round: int
    word: str


def current_state(code: str, doc: int, root: Path = REPO_ROOT) -> State:
    found = review_files(code, doc, root)
    if not found:
        return State(0, 0, 0, "none")
    latest = max(found)
    return State(sum(len(v) for v in found.values()), len(cycle_rounds(found, root)), latest, verdict_word(found[latest]))


@dataclass(frozen=True)
class Row:
    doc: int
    check: str
    files: int | None
    verdict: str | None
    reason: str


@dataclass
class Declaration:
    date: str
    rows: list[Row] = field(default_factory=list)


def _field(text: str, key: str) -> str:
    m = re.search(rf"^[ \t]*[*_`]*{re.escape(key)}[*_`]*[ \t]*:[ \t]*(.*)$", text, re.MULTILINE)
    return re.sub(r"^[*_`\s]+|[*_`\s]+$", "", m.group(1)) if m else ""


def _row(cells: list[str]) -> Row | None:
    doc = parse_doc_label(cells[0])
    if doc is None:
        return None
    state = cells[2]
    files = re.search(r"review files\s*:\s*(\d+)", state, re.IGNORECASE)
    verdict = re.search(r"latest verdict\s*:\s*([^;|]+)", state, re.IGNORECASE)
    check = re.sub(r"[\s_`]+", "-", cells[1].strip().lower())
    return Row(doc, check, int(files.group(1)) if files else None, verdict.group(1).strip() if verdict else None, cells[3])


def _row_errors(code: str, row: Row, root: Path) -> list[str]:
    label = doc_label(row.doc)
    if document_path(code, row.doc, root) is None:
        return [f"{label}: the document does not exist"]
    state = current_state(code, row.doc, root)
    errors = []
    if row.files is None:
        errors.append(f"{label}: the recorded state gives no 'review files: N' count")
    elif row.files != state.files:
        errors.append(f"{label}: the declaration records {row.files} review files and the disk has {state.files}; a review file added after the declaration is not accepted")
    if row.check == CAP_CHECK and state.rounds <= ROUND_CAP:
        errors.append(f"{label}: the document has {state.rounds} review rounds, within the cap of {ROUND_CAP}, so there is nothing to accept")
    if row.check == WORDING_CHECK:
        if row.verdict is None:
            errors.append(f"{label}: the recorded state gives no 'latest verdict: WORD'")
        elif row.verdict != state.word:
            errors.append(f"{label}: the declaration records the latest verdict as {row.verdict!r} and the disk reads {state.word!r}")
        if state.word != CLEARED:
            errors.append(f"{label}: only the older wording {CLEARED!r} is accepted; the latest verdict reads {state.word!r}")
    if PLACEHOLDER.match(row.reason):
        errors.append(f"{label}: the reason is empty")
    return errors


def load_declaration(code: str, root: Path = REPO_ROOT) -> tuple[Declaration | None, list[Finding]]:
    """(valid declaration or None, findings). No file gives (None, []). A
    header or check-set error rejects the whole declaration; a stale or
    missing document rejects that row and still fails loudly."""
    path = declaration_path(code, root)
    if not path.is_file():
        return None, []
    where = rel(path, root)
    text = read_text(path)
    fail = lambda reason: Finding(where, CHECK_ID, reason)  # noqa: E731
    values = {k: _field(text, k) for k in HEADER_KEYS}
    fatal = [f"header field '{k}' is missing or empty" for k, v in values.items() if PLACEHOLDER.match(v)]
    if values["World"] and values["World"] != code:
        fatal.append(f"World is {values['World']!r}, not {code!r}")
    if values["Declared by"] and values["Declared by"] != DECLARER:
        fatal.append(f"Declared by must be exactly {DECLARER!r}, found {values['Declared by']!r}")
    if values["Date"] and not _DATE.match(values["Date"]):
        fatal.append(f"Date {values['Date']!r} is not an ISO date")
    if re.search(r"\bV(?:[2-9]|\d{2,})\.\d", re.sub(r"(?i)\b(?:pre-|before\s+)V\d+\.\d+", "", values["Process version"])):
        fatal.append(f"Process version {values['Process version']!r}: a world built under Process V2.0 or later cannot use a declaration")
    if not re.search(rf"^#+\s*{re.escape(OPEN_SECTION)}\s*$", text, re.IGNORECASE | re.MULTILINE):
        fatal.append(f"the section '{OPEN_SECTION}' is missing")
    rows: list[Row] = []
    for table in markdown_tables(text):
        for cells in table:
            if len(cells) != 4:
                continue
            row = _row(cells)
            if row is None:
                fatal.append(f"table row names no document Step0 or Doc_01 to Doc_10: {cells[0][:60]!r}")
            else:
                rows.append(row)
    if not rows:
        fatal.append("no accepted item in the table")
    for row in rows:
        if row.check not in ACCEPTABLE_CHECKS:
            fatal.append(f"{doc_label(row.doc)}: {row.check!r} is not a check a declaration can accept; the only checks are {', '.join(ACCEPTABLE_CHECKS)}")
    seen = set()
    for row in rows:
        if (row.doc, row.check) in seen:
            fatal.append(f"{doc_label(row.doc)}: {row.check} is listed twice")
        seen.add((row.doc, row.check))
    if fatal:
        return None, [fail(reason) for reason in fatal]
    good, errors = [], []
    for row in rows:
        row_errors = _row_errors(code, row, root)
        errors += row_errors
        if not row_errors:
            good.append(row)
    return Declaration(values["Date"], good), [fail(reason) for reason in errors]


def accepted_reason(code: str, row: Row, root: Path, label: str | None = None) -> str:
    """The failure text a valid row accepts, in the handoff gate's own words."""
    state = current_state(code, row.doc, root)
    label = label or doc_label(row.doc)
    if row.check == CAP_CHECK:
        return f"{label} took {state.rounds} review rounds; the cap is {ROUND_CAP}"
    return f"latest review round {state.latest_round} of {label} does not say 'Approved to proceed'"


def draft_declaration(code: str, root: Path = REPO_ROOT, today: date | None = None) -> str:
    """A pre-filled declaration body drawn from the current disk state."""
    lines = [
        f"World: {code}",
        f"Declared by: {DECLARER}",
        f"Date: {(today or date.today()).isoformat()}",
        "Process version: <the process version the world was built under>",
        "Scope: <what this declaration covers>",
        "",
        "| Document | Check accepted | Recorded state at declaration | Reason |",
        "|---|---|---|---|",
    ]
    for doc in DOCUMENTS:
        if document_path(code, doc, root) is None:
            continue
        state = current_state(code, doc, root)
        if state.rounds > ROUND_CAP:
            lines.append(f"| {doc_label(doc)} | {CAP_CHECK} | review files: {state.files} | <reason> |")
        if state.word == CLEARED:
            lines.append(f"| {doc_label(doc)} | {WORDING_CHECK} | review files: {state.files}; latest verdict: {state.word} | <reason> |")
    lines += ["", f"## {OPEN_SECTION}", "", "- <finding, and how it will be checked>", ""]
    return "\n".join(lines)
