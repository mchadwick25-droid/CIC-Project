import json
import re
import sqlite3
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .catalog import REPO_ROOT, TEXTS_DIR
from .check import fold
from .retrieve import fts_query

QUESTION_COVERAGE = REPO_ROOT / "Build" / "Ministry" / "Features" / "Question-Coverage"
KS = (5, 10, 20)
DEPTH = 100
OCR_WEAK = 0.8
COARSE_WORDS = 800
MIN_OVERLAP = 2

STOPWORDS = frozenset(
    """
    a about after all also am an and any are as at be been being but by can could did do does for from had has have he her him his
    how i if in into is it its me my no not of on one or our out she so some than that the their them then there these they this
    those to up us was we were what when where which who whom why will with would you your yours
    """.split()
)
_FILE_MENTION = re.compile(r"cic/texts/([\w\-.]+\.(?:txt|xml))")
_LINES = re.compile(r"lines?\s+(\d[\d,\s\-–and]*)", re.IGNORECASE)
_NUMBER_RANGE = re.compile(r"(\d+)\s*[-–]\s*(\d+)|(\d+)")


@dataclass(frozen=True)
class Citation:
    file: str
    start: int
    end: int


@dataclass
class RecordEvidence:
    record_id: str
    record_type: str
    quote: str | None
    retrieve_when: list[str] = field(default_factory=list)
    citations: list[Citation] = field(default_factory=list)


def read_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def parse_citations(locus: str) -> list[Citation]:
    mentions = list(_FILE_MENTION.finditer(locus))
    citations = []
    for index, mention in enumerate(mentions):
        stop = mentions[index + 1].start() if index + 1 < len(mentions) else len(locus)
        tail = locus[mention.end():stop]
        for block in _LINES.finditer(tail):
            for match in _NUMBER_RANGE.finditer(block.group(1)):
                if match.group(1):
                    citations.append(Citation(mention.group(1), int(match.group(1)), int(match.group(2))))
                else:
                    number = int(match.group(3))
                    citations.append(Citation(mention.group(1), number, number))
    return citations


def load_record_evidence(records_dir: Path) -> dict[str, RecordEvidence]:
    evidence = {}
    for path in sorted(records_dir.glob("*/*.md")):
        front = read_front_matter(path)
        if not front.get("id"):
            continue
        item = RecordEvidence(front["id"], front.get("record_type", ""), front.get("text") if front.get("record_type") == "quote" else None,
                              [str(x) for x in (front.get("retrieval") or {}).get("retrieve_when") or []])
        for source in front.get("sources") or []:
            item.citations += parse_citations(str(source.get("locus") or ""))
        if item.citations or item.quote:
            evidence[item.record_id] = item
    return evidence


def load_questions(repository: Path = QUESTION_COVERAGE / "Repository") -> dict[str, str]:
    questions = {}
    for path in sorted(repository.glob("0[1-6]-*.yaml")):
        for q in (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("questions", []):
            questions[q["id"]] = q["t"]
    return questions


def load_subquestions(repository: Path = QUESTION_COVERAGE / "Repository") -> dict[str, dict]:
    data = yaml.safe_load((repository / "07-subquestions.yaml").read_text(encoding="utf-8"))
    return {s["id"]: s for s in data["subquestions"]}


def load_cells(world: str, coverage_dir: Path = QUESTION_COVERAGE / "Coverage-Maps") -> dict[str, list[str]]:
    cells: dict[str, list[str]] = {}
    for path in sorted(coverage_dir.glob("C*-coverage.json")):
        cluster = path.name.split("-")[0]
        data = json.loads(path.read_text(encoding="utf-8"))
        for key, cell in (data.get("worlds", {}).get(world) or {}).items():
            if re.fullmatch(r"S\d+", key) and isinstance(cell, dict):
                ids = [r if isinstance(r, str) else r.get("id") for r in cell.get("records", [])]
                cells[f"{cluster}.{key}"] = [i for i in ids if i and i.startswith(f"{world}.")]
    return cells


def line_offsets(data: bytes) -> list[int]:
    offsets = [0]
    for match in re.finditer(b"\n", data):
        offsets.append(match.end())
    return offsets


def _normalize(text: str) -> str:
    return " ".join(fold(text).split())


def gold_passages(db_path: Path, evidence: RecordEvidence, texts_dir: Path = TEXTS_DIR) -> dict[str, str]:
    """passage_id -> how it was found ('line' or 'quote'), for passages in the index."""
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    found: dict[str, str] = {}
    try:
        by_file = defaultdict(list)
        for c in evidence.citations:
            by_file[c.file].append(c)
        for file_name, citations in by_file.items():
            path = texts_dir / file_name
            if not path.is_file():
                continue
            offsets = line_offsets(path.read_bytes())
            for c in citations:
                lo = offsets[min(c.start, len(offsets)) - 1] if c.start >= 1 else 0
                hi = offsets[min(c.end, len(offsets) - 1)] if c.end < len(offsets) else offsets[-1]
                for row in connection.execute(
                        "SELECT passage_id FROM passages WHERE file = ? AND byte_start < ? AND byte_end > ?", (file_name, max(hi, lo + 1), lo)):
                    found[row["passage_id"]] = "line"
        if evidence.quote:
            words = _normalize(evidence.quote).split()
            probe = " ".join(words[:10])
            if probe:
                files = {c.file for c in evidence.citations}
                for row in connection.execute("SELECT passage_id, file, text FROM passages"
                                              + (" WHERE file IN (%s)" % ",".join("?" * len(files)) if files else ""), list(files)):
                    if probe in _normalize(row["text"]):
                        found[row["passage_id"]] = "quote"
    finally:
        connection.close()
    return found


def query_terms(wording: str) -> list[str]:
    return [t for t in re.findall(r"[^\W_]+", wording.casefold()) if t not in STOPWORDS and len(t) > 1]


def ranked(db_path: Path, wording: str, world: str, depth: int = DEPTH, min_ocr: float | None = None) -> list[str]:
    match = fts_query(" ".join(query_terms(wording)))
    if not match:
        return []
    connection = sqlite3.connect(db_path)
    try:
        sql = (
            "SELECT p.passage_id FROM passage_fts JOIN passages p ON p.id = passage_fts.rowid "
            "WHERE passage_fts MATCH ? AND EXISTS (SELECT 1 FROM shelf_files s WHERE s.file = p.file AND s.world = ?) "
            "{floor}ORDER BY bm25(passage_fts) LIMIT ?"
        ).format(floor="" if min_ocr is None else "AND (p.ocr_score IS NULL OR p.ocr_score >= ?) ")
        params = (match, world) + (() if min_ocr is None else (min_ocr,)) + (depth,)
        return [r[0] for r in connection.execute(sql, params)]
    finally:
        connection.close()


@dataclass
class Case:
    sub_question: str
    cluster: str
    wording_id: str
    wording: str
    record_id: str
    best_rank: int | None
    condition: str = "wording"


CONDITIONS = ("wording", "wording+label", "record routing")
_ROUTING_LEAD = re.compile(r"^participant (?:asks|is asking|says|wants)( about| whether| how| what| if| to)?\s*", re.IGNORECASE)


def routing_query(retrieve_when: list[str]) -> str:
    return " ".join(_ROUTING_LEAD.sub("", phrase) for phrase in retrieve_when)


def run_bench(db_path: Path, world: str, evidence: dict[str, RecordEvidence], cells: dict[str, list[str]],
              subquestions: dict[str, dict], questions: dict[str, str], texts_dir: Path = TEXTS_DIR,
              min_ocr: float | None = None):
    gold_cache = {rid: gold_passages(db_path, ev, texts_dir) for rid, ev in evidence.items()}
    cases: list[Case] = []
    ungrounded: dict[str, list[str]] = defaultdict(list)

    def add(cell, wording_id, text, usable, condition):
        position = {pid: i + 1 for i, pid in enumerate(ranked(db_path, text, world, min_ocr=min_ocr))}
        for rid in usable:
            ranks = [position[p] for p in gold_cache[rid] if p in position]
            cases.append(Case(cell, cell.split(".")[0], wording_id, text, rid, min(ranks) if ranks else None, condition))

    for cell, record_ids in cells.items():
        sub = subquestions.get(cell)
        if not sub:
            continue
        usable = [r for r in record_ids if gold_cache.get(r)]
        ungrounded[cell] += [r for r in record_ids if r not in usable]
        for wording_id in sub["ids"]:
            wording = questions.get(wording_id)
            if wording:
                add(cell, wording_id, wording, usable, CONDITIONS[0])
                add(cell, wording_id, f"{wording} {sub['label']}", usable, CONDITIONS[1])
        for rid in usable:
            routing = routing_query(evidence[rid].retrieve_when)
            if routing.strip():
                add(cell, "retrieve_when", routing, [rid], CONDITIONS[2])
    return cases, gold_cache, {k: v for k, v in ungrounded.items() if v}


def recall(cases: list[Case], k: int) -> float:
    return sum(1 for c in cases if c.best_rank is not None and c.best_rank <= k) / len(cases) if cases else 0.0


def passage_info(db_path: Path, passage_ids) -> list[sqlite3.Row]:
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    try:
        ids = list(passage_ids)
        rows = []
        for i in range(0, len(ids), 500):
            chunk = ids[i:i + 500]
            rows += connection.execute(
                f"SELECT passage_id, file, language, ocr_score, word_count, text FROM passages WHERE passage_id IN ({','.join('?' * len(chunk))})",
                chunk).fetchall()
        return rows
    finally:
        connection.close()


def diagnose(db_path: Path, case_group: list[Case], gold: dict[str, str]) -> tuple[str, str]:
    """Reason class and a short detail for a (sub-question, record) pair no wording reached within k."""
    rows = passage_info(db_path, gold)
    languages = {r["language"] for r in rows}
    terms = {t for c in case_group for t in query_terms(c.wording)}
    overlap = 0
    for r in rows:
        words = {fold(w) for w in re.findall(r"[^\W_]+", r["text"])}
        overlap = max(overlap, len(terms & words))
    weak = [r for r in rows if r["ocr_score"] is not None and r["ocr_score"] < OCR_WEAK]
    coarse = [r for r in rows if r["word_count"] > COARSE_WORDS]
    if rows and all(r["language"] not in ("eng", "en", "") for r in rows) and overlap < MIN_OVERLAP:
        return "foreign-language source", f"gold passages are {'/'.join(sorted(languages))}; at most {overlap} query terms occur in them"
    if weak and len(weak) == len(rows):
        return "OCR", f"gold passages have OCR scores below {OCR_WEAK} (lowest {min(r['ocr_score'] for r in weak):.2f})"
    if coarse and len(coarse) == len(rows):
        return "division too coarse", f"gold passages run {max(r['word_count'] for r in coarse)} words"
    if overlap < MIN_OVERLAP:
        return "vocabulary mismatch", f"at most {overlap} query terms occur in the gold passages"
    return "outranked", f"{overlap} query terms occur in the gold passages but other passages score higher"
