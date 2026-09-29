"""Claims-register control.

  claims  derives every absence or exclusivity claim from a world's
          deliverables and record files, and halts on any claim the world's
          claims register does not hold, on any register entry no live claim
          supports, and on any entry whose evidence no longer resolves

The register is Build/worlds/<code>/<code>_Claims_Register.md, made from
Build/reference/L4-Templates/Claims_Register_Template.md. Registration is the
control: it shows a claim is known, listed and answerable. It does not show
the claim is true. Verification is separate work, recorded in the register.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

from .common import REPO_ROOT, Finding, Report, emit, read_text, rel, world_dir
from .deployed import _id_pattern, load_records, world_codes

REGISTER_SUFFIX = "_Claims_Register.md"
STATUSES = ("VERIFIED", "UNVERIFIED", "JUDGEMENT")
CONFIDENCE_LEVELS = ("Documented", "Widely Accepted", "Dominant Modern Reconstruction", "Contested", "Inferential-Thin")
REGISTER_COLUMNS = ("id", "status", "confidence", "source", "check", "file", "claim")
MIN_SENTENCE_CHARS = 25

_RECORD_NOUN = (
    r"(?:sources?|texts?|witness(?:es)?|accounts?|records?|documents?|letters?|writers?|authors?|voices?"
    r"|evidence|attestations?|mentions?|corpus|works?|manuscripts?|inscriptions?|references?)"
)
_OTHER = r"(?:other |further |surviving |extant |ancient |contemporary |independent |second |earlier |later |written |first-hand |direct )*"

# Each pattern is one shape of absence or exclusivity claim about the record.
# The set is closed and short so that every derived claim can be explained by
# naming the pattern that matched it.
CLAIM_PATTERNS: tuple[tuple[str, re.Pattern], ...] = tuple(
    (name, re.compile(pattern, re.IGNORECASE))
    for name, pattern in (
        ("no-source", rf"\bno {_OTHER}{_RECORD_NOUN}\b"),
        ("none-of", rf"\bnone of (?:the|these|those|our|this world's|its) {_OTHER}{_RECORD_NOUN}\b"),
        ("not-one", rf"\bnot (?:one|a single) {_OTHER}{_RECORD_NOUN}\b"),
        ("nothing-in", rf"\bnothing (?:in|from|among) (?:the|our|any|this|these) {_OTHER}{_RECORD_NOUN}\b"),
        ("only", rf"\b(?:the|an?) only {_OTHER}(?:surviving |extant |known |named )*{_RECORD_NOUN}\b|\bonly (?:one|two|three) {_OTHER}{_RECORD_NOUN}\b"),
        ("sole", r"\b(?:the )?sole (?:surviving |extant |known )?\w+"),
        ("never", r"\bnever (?:mentions?|says?|records?|attests?|names?|uses?|describes?|quotes?|cites?|appears?|speaks?|refers?)\b"),
        ("no-other", r"\bno other\b"),
        ("nowhere", r"\bnowhere (?:in|is|does|do|else|attested|mentioned|said|recorded)\b"),
        ("not-attested", r"\b(?:is|are|was|were) not (?:attested|recorded|preserved|mentioned|extant)\b|\bunattested\b"),
        ("silent", r"\b(?:is|are|was|were|remains?|remained) silent\b|\bsays? nothing\b|\bsilent (?:on|about)\b"),
        ("exclusive", r"\bexclusively\b|\bsolely\b|\buniquely (?:attested|recorded|documented)\b"),
        ("absent-from", rf"\babsent from (?:the|our|this) {_OTHER}{_RECORD_NOUN}\b"),
        ("no-one-writes", r"\bno one (?:wrote|writes|recorded|records|says|said|left|survives)\b"),
    )
)

_DELIVERABLE_EXCLUDED = re.compile(r"review|superseded|claims_register|template|open_gaps|decision_log|spotcheck|spot_check", re.IGNORECASE)
_RECORD_FIELD_EXCLUDED = frozenset({
    "id", "world_id", "record_type", "schema_version", "status", "register", "canon_cells", "confidence", "sources",
    "relations", "retrieval", "claim_guards", "edition", "external_ids", "rights_status", "attribution_status",
    "discovery_channel", "kind", "work_id", "shelf_row", "demo_tag", "_path", "_body",
})
_FENCE = re.compile(r"```.*?```", re.DOTALL)
_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
_REPO_PATH = re.compile(r"(?<![\w/])(?:cic|Build|records|packages|engine|Archive|tools)/[\w\-./]+\.\w+")
_TRAILING = ".,;:)]}'\"`"


# ---- derivation ----------------------------------------------------------------------------------


def normalise(text: str) -> str:
    text = re.sub(r"[*_`]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def claim_id(text: str) -> str:
    """Eight hex digits from the claim's normalised, lowercased text, so a
    reworded claim is a new claim."""
    return hashlib.sha1(normalise(text).lower().encode("utf-8")).hexdigest()[:8]


def matching_patterns(sentence: str) -> list[str]:
    return [name for name, pattern in CLAIM_PATTERNS if pattern.search(sentence)]


def markdown_units(text: str) -> list[str]:
    """Sentence-like units of a markdown file: each table row is one unit, each
    prose block is split at sentence ends, fenced blocks are dropped."""
    text = _FENCE.sub("\n", text)
    units: list[str] = []
    block: list[str] = []

    def flush() -> None:
        if block:
            prose = re.sub(r"\s+", " ", " ".join(block))
            units.extend(_SENTENCE_END.split(prose))
            block.clear()

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            flush()
        elif stripped.startswith("|"):
            flush()
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                units.append(" ".join(cells))
        elif stripped.startswith("#"):
            flush()
            units.append(stripped.lstrip("#").strip())
        else:
            block.append(stripped)
    flush()
    return units


def _strings(value, key: str = "") -> list[str]:
    if key in _RECORD_FIELD_EXCLUDED:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [s for item in value for s in _strings(item)]
    if isinstance(value, dict):
        return [s for k, v in value.items() for s in _strings(v, str(k))]
    return []


def record_text(path: Path) -> str:
    """A record file's prose: its body and every string field that is not
    envelope, provenance or guard text."""
    lines = read_text(path).splitlines()
    if not lines or lines[0].strip() != "---":
        return read_text(path)
    try:
        close = lines[1:].index("---") + 1
        front = yaml.safe_load("\n".join(lines[1:close])) or {}
    except (ValueError, yaml.YAMLError):
        return "\n".join(lines)
    fields = _strings(front) if isinstance(front, dict) else []
    return "\n\n".join([*fields, "\n".join(lines[close + 1 :])])


def deliverable_files(code: str, root: Path = REPO_ROOT) -> list[Path]:
    """The world's build documents (Doc_NN files, chunk folders, the profile
    and capsule) and its record files. Review files, superseded material, the
    register itself and the gaps and decision ledgers are not deliverables."""
    base = world_dir(code, root)
    found: dict[Path, None] = {}
    if base.is_dir():
        for path in sorted(base.glob("*.md")):
            if re.match(r"(?:Doc_?\d+|.*_World_(?:Profile|Capsule_Core))", path.name, re.IGNORECASE) and not _DELIVERABLE_EXCLUDED.search(path.name):
                found[path] = None
        for directory in sorted(base.glob("*-Chunks")):
            for path in sorted(directory.glob("*.md")):
                found[path] = None
    records = root / "records" / code
    if records.is_dir():
        for path in sorted(records.glob("*/*.md")):
            found[path] = None
    return list(found)


def derive_claims(code: str, root: Path = REPO_ROOT) -> dict[str, dict]:
    """{id: {file, text, patterns}} for every claim in the deliverables. When
    one claim appears in several files the first file in path order holds it."""
    claims: dict[str, dict] = {}
    for path in deliverable_files(code, root):
        text = record_text(path) if "records" in path.relative_to(root).parts[:1] else read_text(path)
        for unit in markdown_units(text):
            sentence = normalise(unit)
            if len(sentence) < MIN_SENTENCE_CHARS:
                continue
            patterns = matching_patterns(sentence)
            if patterns:
                claims.setdefault(claim_id(sentence), {"file": path.name, "path": path, "text": sentence, "patterns": patterns})
    return claims


# ---- the register --------------------------------------------------------------------------------


def register_path(code: str, root: Path = REPO_ROOT) -> Path:
    return world_dir(code, root) / f"{code}{REGISTER_SUFFIX}"


def read_register(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    """(rows, columns missing from the register table). A row is the table's
    cells by lowercased header, and carries its own `line` number."""
    rows: list[dict[str, str]] = []
    missing: list[str] = list(REGISTER_COLUMNS)
    text = read_text(path)
    for table in _register_tables(text):
        header, body = table
        if "id" not in header or "status" not in header:
            continue
        missing = [c for c in REGISTER_COLUMNS if c not in header]
        for cells in body:
            if not any(c.strip() for c in cells):
                continue
            row = {h: (cells[i].strip("` ") if i < len(cells) else "") for i, h in enumerate(header)}
            rows.append(row)
    return rows, missing


def _register_tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    tables: list[tuple[list[str], list[list[str]]]] = []
    block: list[list[str]] = []

    def flush() -> None:
        rows = [r for r in block if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
        if rows:
            tables.append(([c.lower().strip("*` ") for c in rows[0]], rows[1:]))

    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            block.append([c.strip() for c in s.strip("|").split("|")])
        elif block:
            flush()
            block = []
    if block:
        flush()
    return tables


def _evidence_findings(code: str, where: str, row: dict[str, str], deliverables: dict[str, Path], records: dict[str, dict], root: Path) -> list[Finding]:
    """Findings for a register row whose evidence no longer resolves: its file
    is not a deliverable, or a repository path or record id in its source or
    check cell does not exist."""
    findings: list[Finding] = []
    label = f"{where} [{row.get('id', '?')}]"
    file = row.get("file", "").strip()
    if file and file not in deliverables:
        findings.append(Finding(label, "c:file-unresolved", f"file {file!r} is not one of this world's deliverables"))
    evidence = " ".join(row.get(k, "") for k in ("source", "check"))
    for match in _REPO_PATH.finditer(evidence):
        candidate = match.group(0).rstrip(_TRAILING)
        if not (root / candidate).exists():
            findings.append(Finding(label, "c:evidence-unresolved", f"{candidate} does not exist"))
    codes = sorted(set(world_codes(root)) | {code})
    for match in re.finditer(_id_pattern(codes), evidence):
        identifier = match.group(0).rstrip(_TRAILING)
        prefix = identifier.split(".", 1)[0]
        known = records if prefix == code else load_records(prefix, root)
        if identifier not in known:
            findings.append(Finding(label, "c:evidence-unresolved", f"{identifier} is not a record"))
    return findings


def check_claims(code: str, root: Path = REPO_ROOT) -> Report:
    report = Report("claims")
    files = deliverable_files(code, root)
    if not files:
        report.findings.append(Finding(rel(world_dir(code, root), root), "c:no-deliverables", "no build documents, chunks or records to derive claims from"))
        return report
    claims = derive_claims(code, root)
    register = register_path(code, root)
    where = rel(register, root)
    if not register.is_file():
        if claims:
            report.findings.append(Finding(where, "c:no-register", f"the world has {len(claims)} absence or exclusivity claim(s) and no claims register"))
        else:
            report.notes.append("no claims derived and no register: nothing to register")
        return report
    rows, missing = read_register(register)
    if missing:
        report.findings.append(Finding(where, "c:columns", f"the register table lacks column(s): {', '.join(missing)}"))
    deliverables = {p.name: p for p in files}
    records = load_records(code, root)
    registered: dict[str, dict[str, str]] = {}
    for row in rows:
        cid = row.get("id", "")
        if cid in registered:
            report.findings.append(Finding(f"{where} [{cid}]", "c:duplicate", "the id appears in more than one register row"))
        registered[cid] = row
        status = row.get("status", "").strip().upper()
        if status not in STATUSES:
            report.findings.append(Finding(f"{where} [{cid}]", "c:status", f"status must be one of {', '.join(STATUSES)}, found {row.get('status')!r}"))
            continue
        if status != "UNVERIFIED":
            if not row.get("check", "").strip("-— "):
                report.findings.append(Finding(f"{where} [{cid}]", "c:check-missing", f"a {status} entry must name the check or the reading that supports it"))
            if row.get("confidence", "") not in CONFIDENCE_LEVELS:
                report.findings.append(Finding(f"{where} [{cid}]", "c:confidence", f"a {status} entry carries one of the five formation_confidence levels, found {row.get('confidence')!r}"))
        elif row.get("confidence", "").strip("-— ") and row.get("confidence") not in CONFIDENCE_LEVELS:
            report.findings.append(Finding(f"{where} [{cid}]", "c:confidence", f"confidence must be one of the five formation_confidence levels or empty, found {row.get('confidence')!r}"))
        report.findings.extend(_evidence_findings(code, where, row, deliverables, records, root))
    for cid, claim in sorted(claims.items(), key=lambda kv: (kv[1]["file"], kv[1]["text"])):
        if cid not in registered:
            report.findings.append(Finding(f"{rel(claim['path'], root)}", "c:unregistered", f"[{cid}] ({', '.join(claim['patterns'])}) {claim['text'][:160]}"))
    for cid, row in registered.items():
        if cid and cid not in claims:
            report.findings.append(Finding(f"{where} [{cid}]", "c:stale", f"no claim in the deliverables has this id any more: {row.get('claim', '')[:120]}"))
    unverified = sum(1 for cid in claims if cid in registered and registered[cid].get("status", "").strip().upper() == "UNVERIFIED")
    report.notes.append(f"{len(claims)} claim(s) derived, {len(registered)} registered, {unverified} registered but UNVERIFIED (registration is the control; it does not show a claim is true)")
    return report


def bootstrap_rows(code: str, root: Path = REPO_ROOT) -> list[str]:
    """Register rows for every derived claim the register does not hold yet,
    as UNVERIFIED, ready to paste."""
    register = register_path(code, root)
    held = {r.get("id") for r in read_register(register)[0]} if register.is_file() else set()
    claims = derive_claims(code, root)
    return [
        f"| `{cid}` | UNVERIFIED | - | - | - | {claim['file']} | {claim['text'].replace('|', '/')} |"
        for cid, claim in sorted(claims.items(), key=lambda kv: (kv[1]["file"], kv[1]["text"]))
        if cid not in held
    ]


# ---- command line --------------------------------------------------------------------------------


def add_parser(subparsers) -> None:
    p = subparsers.add_parser("claims", help="every absence or exclusivity claim in the deliverables is in the claims register, and every register entry is live")
    p.add_argument("world_code")
    p.add_argument("--bootstrap", action="store_true", help="print UNVERIFIED register rows for the claims not yet registered, then exit 0")
    p.add_argument("--json", action="store_true", help="print one JSON document instead of lines")
    p.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root to check (default: this repository)")


def run(args) -> int:
    if args.bootstrap:
        for line in bootstrap_rows(args.world_code, args.root):
            print(line)
        return 0
    return emit([check_claims(args.world_code, args.root)], as_json=args.json)
