"""The twelve handoff checks (check a) and the quote re-verification (check b)."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import yaml

from .common import PLACEHOLDER, REPO_ROOT, Finding, Report, markdown_tables, read_text, registry_entry, rel, safety_adjacent_status, world_dir
from .gaps import LEDGER_NAME
from .matching import matched, split_chunks
from .quotes import check_quotes
from .rebaseline import CHECK_ID, Declaration, accepted_reason, declaration_path, doc_label, document_path, load_declaration
from .rounds import ROUND_CAP, cap_message, clearance_message, counted_review_files, latest_review, review_files
from .verdicts import has_clearance

_REVIEWISH = re.compile(r"review|spotcheck|round|verification|history|superseded", re.IGNORECASE)
_DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
DOSSIER_SECTIONS = (
    (1, "already assigned"),
    (2, "cross-link opportunities"),
    (3, "verified acquisition leads"),
    (4, "checked and closed"),
    (5, "open cross-world questions"),
)
DOSSIER_HEADER_FIELDS = ("Atlas ID", "Corpus-map slug", "Time window")
STEP_LABELS = {0: "Step 0 Movement-Scope Confirmation", 1: "Step 1 World Identification", 2: "Step 2 Source Ecology"}


def _run_corpus_merge_check(root: Path) -> tuple[bool, str]:
    script = root / "cic" / "engine" / "corpus_map_merge.py"
    proc = subprocess.run([sys.executable, str(script), "--check"], cwd=root, capture_output=True, text=True)
    lines = (proc.stdout + proc.stderr).strip().splitlines()
    return proc.returncode == 0, lines[-1] if lines else ""


def _run_corpus_index_build(root: Path) -> tuple[bool, str]:
    sys.path.insert(0, str(root / "cic" / "engine"))
    try:
        import corpus_index

        with tempfile.TemporaryDirectory() as tmp:
            n_files, n_units = corpus_index.build(Path(tmp) / "INDEX.sqlite")
        return n_files > 0, f"{n_files} file(s), {n_units} passage unit(s)"
    except Exception as exc:  # noqa: BLE001 - any build failure is the finding
        return False, f"{type(exc).__name__}: {exc}"
    finally:
        sys.path.pop(0)


def _commentary(root: Path, paths: list[Path]) -> list[tuple[str, int, str, str]]:
    sys.path.insert(0, str(REPO_ROOT / "tools"))
    try:
        import check_live_commentary as clc

        hits = []
        for p in paths:
            for h in clc.scan_file(root, p, "worlds"):
                if h.category in ("REWRITE", "ROUTE"):
                    hits.append((h.path, h.line, h.category, ",".join(h.patterns)))
        return hits
    finally:
        sys.path.pop(0)


@dataclass
class Deps:
    root: Path = REPO_ROOT
    holdings: Callable[[str], list[dict]] | None = None
    corpus_merge_check: Callable[[Path], tuple[bool, str]] = _run_corpus_merge_check
    corpus_index_build: Callable[[Path], tuple[bool, str]] = _run_corpus_index_build
    commentary: Callable[[Path, list[Path]], list[tuple[str, int, str, str]]] = _commentary


@dataclass
class World:
    code: str
    root: Path
    entry: dict | None
    slug: str | None
    findings: list[Finding] = field(default_factory=list)

    @property
    def dir(self) -> Path:
        return world_dir(self.code, self.root)


def step_documents(code: str, root: Path = REPO_ROOT) -> dict[int, Path | None]:
    base = world_dir(code, root)
    found: dict[int, Path | None] = {0: None, 1: None, 2: None}
    if not base.is_dir():
        return found
    for path in sorted(base.glob("*.md")):
        if _REVIEWISH.search(path.name):
            continue
        name = path.name
        if re.match(r"(?:[\w]+_)?Step_?0(?!\d)", name) and found[0] is None:
            found[0] = path
            continue
        for n in (1, 2):
            if re.match(rf"(?:{re.escape(code)}_)?Doc_?0*{n}(?!\d)", name) and found[n] is None:
                found[n] = path
    return found


def source_registry_files(code: str, root: Path = REPO_ROOT) -> list[Path]:
    base = world_dir(code, root)
    return sorted(p for p in base.glob("*Source_Registry*.md") if not _REVIEWISH.search(p.name)) if base.is_dir() else []


def manifest_path(code: str, root: Path = REPO_ROOT) -> Path:
    return world_dir(code, root) / "build" / f"{code}_Handoff_Manifest.md"


def dossier_path(slug: str, root: Path = REPO_ROOT) -> Path:
    return root / "Build" / "worlds" / "_cross-world" / "dossiers" / f"{slug}_Source_Readiness_Dossier.md"


def bucket_path(slug: str, root: Path = REPO_ROOT) -> Path:
    return root / "cic" / "corpus-map" / f"{slug}.yaml"


def bucket_works(slug: str | None, root: Path) -> list[dict]:
    if not slug or not bucket_path(slug, root).is_file():
        return []
    return list((yaml.safe_load(read_text(bucket_path(slug, root))) or {}).get("works") or [])


def _section(text: str, number: int) -> str:
    m = re.search(rf"^##\s+{number}\.[^\n]*\n(.*?)(?=^##\s+\d+\.|\Z)", text, re.MULTILINE | re.DOTALL)
    return m.group(1) if m else ""


def _bullets(section: str) -> list[str]:
    items = [re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", ln).strip() for ln in section.splitlines() if re.match(r"^\s*(?:[-*]|\d+[.)])\s+", ln)]
    return [i for i in items if not PLACEHOLDER.match(i)]


def _file_mentioned(filename: str, text: str) -> bool:
    stem = filename.rsplit(".", 1)[0]
    prefix = stem.split("_")[0]
    return filename in text or stem in text or bool(re.search(rf"\b{re.escape(prefix)}\b", text))


def _check_01(w: World) -> list[Finding]:
    path = f"records/worlds/{w.code}.yaml"
    if w.entry is None:
        return [Finding(path, "handoff-01-identity", "registry entry does not exist")]
    world_id = w.entry.get("world_id")
    if not world_id:
        return [Finding(path, "handoff-01-identity", "registry entry has no world_id")]
    out = []
    from engine.m9.enforce import GRANDFATHERED_WORLDS

    value, reason = safety_adjacent_status(w.code, w.entry)
    if value is None and w.code not in GRANDFATHERED_WORLDS:
        out.append(Finding(path, "handoff-01-identity", reason))
    records = w.root / "records" / w.code
    if records.is_dir():
        bad = []
        for p in sorted(records.rglob("*.md")):
            head = "\n".join(read_text(p).splitlines()[:30])
            m = re.search(r"^world_id:\s*(\S+)", head, re.MULTILINE)
            if m and m.group(1).strip("\"'") != world_id:
                bad.append(rel(p, w.root))
        for p in bad[:5]:
            out.append(Finding(p, "handoff-01-identity", f"world_id differs from the registry's {world_id!r}"))
        if len(bad) > 5:
            out.append(Finding(f"records/{w.code}", "handoff-01-identity", f"{len(bad) - 5} more records carry a different world_id"))
    return out


def _check_step(w: World, step: int, docs: dict[int, Path | None], check_id: str) -> list[Finding]:
    label = STEP_LABELS[step]
    doc = docs[step]
    if doc is None:
        return [Finding(rel(w.dir, w.root), check_id, f"{label} document not found")]
    out: list[Finding] = []
    reviews = review_files(w.code, step, w.root)
    if not reviews:
        out.append(Finding(rel(doc, w.root), check_id, f"{label} has no review file"))
        return out
    counted = counted_review_files(w.code, step, w.root)
    if len(counted) > ROUND_CAP:
        out.append(Finding(rel(doc, w.root), check_id, cap_message(label, len(counted))))
    description, latest = latest_review(reviews)
    if not has_clearance(latest):
        out.append(Finding(rel(latest[0], w.root), check_id, clearance_message(label, description)))
    return out


def _check_02_census(w: World, doc: Path | None) -> list[Finding]:
    census_path = w.root / "cic-website" / "data" / "world-census.json"
    out: list[Finding] = []
    if not census_path.is_file():
        return [Finding("cic-website/data/world-census.json", "handoff-02-step0", "census file is missing")]
    census = json.loads(read_text(census_path))
    ids = {m.get("id") for m in census.get("movements", [])}
    if w.slug not in ids:
        out.append(Finding("cic-website/data/world-census.json", "handoff-02-step0", f"no movement {w.slug!r} in the census"))
    if doc is not None and "world-census" not in read_text(doc):
        out.append(Finding(rel(doc, w.root), "handoff-02-step0", "Step 0 does not record the movement's status in world-census.json"))
    return out


def _dossier_items(w: World, text: str) -> tuple[list[dict], list[str], list[str], list[str]]:
    s1 = _section(text, 1)
    rows = []
    for table in markdown_tables(s1):
        for cells in table:
            if cells and not PLACEHOLDER.match(cells[0]):
                rows.append({"work": cells[0], "file": cells[-1]})
    s2 = _bullets(_section(text, 2))
    s3 = [c[0] for t in markdown_tables(_section(text, 3)) for c in t if c and not PLACEHOLDER.match(c[0])]
    s5 = _bullets(_section(text, 5))
    return rows, s2, s3, s5


def _check_04(w: World, docs: dict[int, Path | None]) -> list[Finding]:
    out = _check_step(w, 2, docs, "handoff-04-step2")
    doc = docs[2]
    registries = source_registry_files(w.code, w.root)
    body = "\n".join(read_text(p) for p in ([doc] if doc else []) + registries)
    if not body:
        return out
    chunks = split_chunks(body)
    where = rel(registries[0] if registries else doc, w.root)
    for work in bucket_works(w.slug, w.root):
        title, source = str(work.get("work", "")), str(work.get("source_file", ""))
        if not (source and _file_mentioned(source, body)) and not matched(title, chunks):
            out.append(Finding(where, "handoff-04-step2", f"corpus-map work has no registry line: {title[:80]}"))
    dossier = dossier_path(w.slug or "", w.root)
    if dossier.is_file():
        rows, s2, s3, _ = _dossier_items(w, read_text(dossier))
        for r in rows:
            if not (r["file"] and _file_mentioned(r["file"], body)) and not matched(r["work"], chunks):
                out.append(Finding(where, "handoff-04-step2", f"dossier section 1 work has no registry line: {r['work'][:80]}"))
        for item in s2:
            if not matched(item, chunks, 0.5):
                out.append(Finding(where, "handoff-04-step2", f"dossier section 2 cross-link has no registry line: {item[:80]}"))
        for item in s3:
            if not matched(item, chunks, 0.5):
                out.append(Finding(where, "handoff-04-step2", f"dossier section 3 lead has no registry line: {item[:80]}"))
    return out


def _check_04_holdings(w: World, docs: dict[int, Path | None], deps: Deps) -> list[Finding]:
    doc = docs[2]
    registries = source_registry_files(w.code, w.root)
    body = "\n".join(read_text(p) for p in ([doc] if doc else []) + registries)
    where = rel(registries[0] if registries else (doc or w.dir), w.root)
    try:
        if deps.holdings is not None:
            rows = deps.holdings(w.code)
        else:
            from engine.m9.holdings import holdings_for

            rows = holdings_for(w.code, w.root)
    except Exception as exc:  # noqa: BLE001
        return [Finding(where, "handoff-04-step2", f"holdings report could not run: {type(exc).__name__}: {exc}")]
    out = []
    for row in rows:
        if row["disposition"] in ("not yet assessed", "in scope, unread") and not _file_mentioned(row["file"], body):
            out.append(Finding(where, "handoff-04-step2", f"holdings file marked '{row['disposition']}' has no registry line: {row['file']}"))
    return out


def _check_05(w: World) -> list[Finding]:
    path = dossier_path(w.slug or "", w.root)
    where = rel(path, w.root)
    if not w.slug or not path.is_file():
        return [Finding(where, "handoff-05-dossier", "Source Readiness Dossier does not exist")]
    text = read_text(path)
    out = []
    for field_name in DOSSIER_HEADER_FIELDS:
        m = re.search(rf"\*\*{re.escape(field_name)}:\*\*\s*(.*)", text)
        if not m or PLACEHOLDER.match(m.group(1)):
            out.append(Finding(where, "handoff-05-dossier", f"header field '{field_name}' is missing or empty"))
    for number, title in DOSSIER_SECTIONS:
        m = re.search(rf"^##\s+{number}\.\s*(.*)$", text, re.MULTILINE)
        if not m or title not in m.group(1).lower():
            out.append(Finding(where, "handoff-05-dossier", f"section {number} '{title}' is missing"))
    return out


def _check_06(w: World, deps: Deps) -> list[Finding]:
    path = bucket_path(w.slug or "", w.root)
    where = rel(path, w.root)
    if not w.slug or not path.is_file():
        return [Finding(where, "handoff-06-corpus-map", "corpus-map bucket does not exist")]
    out = []
    doc = yaml.safe_load(read_text(path)) or {}
    works = doc.get("works") or []
    if not works:
        out.append(Finding(where, "handoff-06-corpus-map", "bucket lists no works"))
    unnumbered = [x for x in works if not str(x.get("row_id") or "").strip()]
    if unnumbered:
        out.append(Finding(where, "handoff-06-corpus-map", f"{len(unnumbered)} of {len(works)} rows in {where} carry no row_id; the Library owns the fix, it issues every row_id and a builder never invents one"))
    if doc.get("atlas_id") != w.slug:
        out.append(Finding(where, "handoff-06-corpus-map", f"bucket atlas_id is {doc.get('atlas_id')!r}, not {w.slug!r}"))
    ok, detail = deps.corpus_merge_check(w.root)
    if not ok:
        out.append(Finding("cic/corpus-map", "handoff-06-corpus-map", f"corpus_map_merge.py --check failed: {detail}"))
    return out


def _check_07(w: World, deps: Deps) -> list[Finding]:
    from importlib import import_module

    sys.path.insert(0, str(REPO_ROOT / "cic" / "engine"))
    try:
        texts_registry = import_module("texts_registry")
    finally:
        sys.path.pop(0)
    registry_file = w.root / "cic" / "texts" / "REGISTRY.yaml"
    registered = {e.get("filename") for e in (yaml.safe_load(read_text(registry_file)) or [])} if registry_file.is_file() else set()
    out = []
    files = sorted({str(x.get("source_file")) for x in bucket_works(w.slug, w.root) if x.get("source_file")})
    for name in files:
        path = w.root / "cic" / "texts" / name
        where = f"cic/texts/{name}"
        if not path.is_file():
            out.append(Finding(where, "handoff-07-texts", "assigned work's file is not vendored"))
            continue
        if name not in registered:
            out.append(Finding("cic/texts/REGISTRY.yaml", "handoff-07-texts", f"no entry for {name}"))
        rights = texts_registry.rights_declared(texts_registry.read_header(path))
        if not texts_registry.rights_clears(rights):
            out.append(Finding(where, "handoff-07-texts", f"no verifiable rights line in the file header ({rights!r})"))
        if path.stat().st_size == 0:
            out.append(Finding(where, "handoff-07-texts", "file is empty"))
    ok, detail = deps.corpus_index_build(w.root)
    if not ok:
        out.append(Finding("cic/texts", "handoff-07-texts", f"corpus_index.py --build is not clean: {detail}"))
    return out


def _check_09(w: World) -> list[Finding]:
    path = dossier_path(w.slug or "", w.root)
    if not path.is_file():
        return []
    _, _, _, questions = _dossier_items(w, read_text(path))
    homes = []
    for p in (w.root / "Build" / "worlds" / "_cross-world" / "NEEDS-RULING.md", w.dir / LEDGER_NAME):
        if p.is_file():
            homes += split_chunks(read_text(p))
    return [
        Finding(rel(path, w.root), "handoff-09-open-questions", f"dossier section 5 question is not in NEEDS-RULING.md or Open_Gaps_Tracking.md: {q[:80]}")
        for q in questions
        if not matched(q, homes, 0.5)
    ]


def _check_10(w: World) -> list[Finding]:
    ledger = w.dir / LEDGER_NAME
    where = rel(ledger, w.root)
    if not ledger.is_file():
        return [Finding(where, "handoff-10-ledger", "Open_Gaps_Tracking.md does not exist")]
    if not _DATE.search(read_text(ledger)):
        return [Finding(where, "handoff-10-ledger", "no dated entry: the library stage's own gaps are not listed")]
    return []


def _check_11(w: World, docs: dict[int, Path | None], deps: Deps) -> list[Finding]:
    paths = [p for p in docs.values() if p] + source_registry_files(w.code, w.root)
    dossier = dossier_path(w.slug or "", w.root)
    if dossier.is_file():
        paths.append(dossier)
    return [
        Finding(f"{path}:{line}", "handoff-11-narration", f"process narration in a file that becomes canonical ({category}: {patterns})")
        for path, line, category, patterns in deps.commentary(w.root, paths)
    ]


def _cell(cells: list[str], index: int) -> str:
    return cells[index] if index < len(cells) else ""


def _check_12(w: World, docs: dict[int, Path | None]) -> list[Finding]:
    path = manifest_path(w.code, w.root)
    where = rel(path, w.root)
    if not path.is_file():
        return [Finding(where, "handoff-12-manifest", "handoff manifest does not exist")]
    text = read_text(path)
    out = []
    m = re.search(r"Handoff date\s*\|\s*([^|]*)\|", text)
    if not m or not _DATE.search(m.group(1)):
        out.append(Finding(where, "handoff-12-manifest", "handoff date is missing or not an ISO date"))
    tables = markdown_tables(text)
    paths_rows = {r[0].lower(): r for t in tables for r in t if len(r) >= 2}
    wanted = {
        "step 0": docs[0],
        "step 1": docs[1],
        "step 2": docs[2],
    }
    for key, doc in wanted.items():
        row = next((r for name, r in paths_rows.items() if name.startswith(key) and len(r) == 2), None)
        if row is None or PLACEHOLDER.match(row[1]):
            out.append(Finding(where, "handoff-12-manifest", f"no path listed for {key.title()}"))
        elif doc is not None and rel(doc, w.root) not in row[1]:
            out.append(Finding(where, "handoff-12-manifest", f"{key.title()} path does not match {rel(doc, w.root)}"))
    for label, target in (("Source Readiness Dossier", dossier_path(w.slug or "", w.root)), ("Corpus-map assignments", bucket_path(w.slug or "", w.root)), ("Open gaps", w.dir / LEDGER_NAME)):
        row = next((r for name, r in paths_rows.items() if name.startswith(label.lower())), None)
        if row is None or PLACEHOLDER.match(row[1]) or rel(target, w.root) not in row[1]:
            out.append(Finding(where, "handoff-12-manifest", f"{label} path is missing or does not match {rel(target, w.root)}"))
    for key in ("step 0", "step 1", "step 2"):
        row = next((r for t in tables for r in t if len(r) >= 4 and r[0].lower() == key), None)
        if row is None or PLACEHOLDER.match(row[1]) or not re.search(r"\d", row[1]) or not _DATE.search(row[3]):
            out.append(Finding(where, "handoff-12-manifest", f"{key.title()} review round or date is missing"))
    return out


def run_handoff(code: str, deps: Deps | None = None, *, quotes: bool = True) -> list[Report]:
    deps = deps or Deps()
    root = deps.root
    entry = registry_entry(code, root)
    slug = (entry or {}).get("census_id")
    w = World(code, root, entry, slug)
    docs = step_documents(code, root)
    reports: list[Report] = []

    def add(name: str, findings: list[Finding], notes: list[str] | None = None) -> None:
        reports.append(Report(name, findings, notes or []))

    add("handoff-01-identity", _check_01(w))
    add("handoff-02-step0", _check_step(w, 0, docs, "handoff-02-step0") + _check_02_census(w, docs[0]))
    add("handoff-03-step1", _check_step(w, 1, docs, "handoff-03-step1"))
    add("handoff-04-step2", _check_04(w, docs) + _check_04_holdings(w, docs, deps))
    add("handoff-05-dossier", _check_05(w))
    add("handoff-06-corpus-map", _check_06(w, deps))
    add("handoff-07-texts", _check_07(w, deps))
    if quotes:
        q_findings, q_notes = check_quotes(code, [p for p in docs.values() if p] + source_registry_files(code, root), root, slug=slug)
        add("handoff-08-quotes", q_findings, q_notes)
    else:
        reports.append(Report("handoff-08-quotes", notes=["skipped by --skip-quotes; the handoff is incomplete until check 8 has run"], skipped=True, incomplete=True))
    add("handoff-09-open-questions", _check_09(w))
    add("handoff-10-ledger", _check_10(w))
    add("handoff-11-narration", _check_11(w, docs, deps))
    add("handoff-12-manifest", _check_12(w, docs))
    declaration, problems = load_declaration(code, root)
    if declaration is not None or problems:
        reports.append(_apply_declaration(w, reports, declaration, problems))
    return reports


_STEP_CHECK_IDS = {0: "handoff-02-step0", 1: "handoff-03-step1", 2: "handoff-04-step2"}


def _apply_declaration(w: World, reports: list[Report], declaration: Declaration | None, problems: list[Finding]) -> Report:
    """Move the failures a valid declaration accepts out of their reports and
    onto the report's accepted list; return the declaration's own report."""
    own = Report(CHECK_ID, list(problems))
    if declaration is None:
        return own
    by_name = {r.name: r for r in reports}
    for row in declaration.rows:
        reason = accepted_reason(w.code, row, w.root, STEP_LABELS.get(row.doc))
        doc = document_path(w.code, row.doc, w.root)
        tag = f"ACCEPTED (project lead declaration {declaration.date})"
        report = by_name.get(_STEP_CHECK_IDS.get(row.doc, ""))
        if report is None:
            own.accepted.append(f"{tag}: {rel(doc, w.root)}: {CHECK_ID}: {reason}")
            continue
        hit = next((f for f in report.findings if reason in f.reason), None)
        if hit is None:
            own.findings.append(Finding(rel(declaration_path(w.code, w.root), w.root), CHECK_ID, f"{doc_label(row.doc)}: {row.check} matches no current failure of {report.name}"))
            continue
        report.findings.remove(hit)
        report.accepted.append(f"{tag}: {hit.line()}")
    return own
