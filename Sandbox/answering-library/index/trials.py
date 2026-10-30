import hashlib
import json
import re
import sqlite3
from collections import defaultdict
from pathlib import Path
from typing import Callable, Iterable, Sequence

from . import bench, catalog
from .bench import Case, RecordEvidence

DEPTH = 100
KS = (10, 20)
WORDING_CONDITIONS = bench.CONDITIONS


def passage_digest(db_path: Path) -> str:
    """Identifies the passage set and byte spans, which is all the gold lookup depends on, whatever the context column holds."""
    connection = sqlite3.connect(db_path)
    try:
        digest = hashlib.sha256()
        for row in connection.execute("SELECT passage_id, byte_start, byte_end FROM passages ORDER BY id"):
            digest.update(repr(row).encode())
        return digest.hexdigest()[:12]
    finally:
        connection.close()


def gold_cache(db_path: Path, evidence: dict[str, RecordEvidence], directory: Path) -> dict[str, dict[str, str]]:
    path = directory / f"gold_{passage_digest(db_path)}.json"
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    gold = {rid: bench.gold_passages(db_path, ev) for rid, ev in evidence.items()}
    directory.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(gold), encoding="utf-8")
    return gold


def gold_files(db_path: Path, cells: dict[str, list[str]], gold: dict[str, dict[str, str]]) -> dict[str, int]:
    used = {p for ids in cells.values() for r in ids for p in gold.get(r, {})}
    connection = sqlite3.connect(db_path)
    try:
        counts: dict[str, int] = defaultdict(int)
        for passage_id in used:
            counts[connection.execute("SELECT file FROM passages WHERE passage_id = ?", (passage_id,)).fetchone()[0]] += 1
        return dict(counts)
    finally:
        connection.close()


def pair_counts(db_path: Path, cells: dict[str, list[str]], gold: dict[str, dict[str, str]]) -> dict[str, int]:
    """For each file, the number of (sub-question, record) pairs whose cited passages include a passage of that file."""
    connection = sqlite3.connect(db_path)
    try:
        counts: dict[str, int] = defaultdict(int)
        for cell, record_ids in cells.items():
            for record_id in record_ids:
                files = {connection.execute("SELECT file FROM passages WHERE passage_id = ?", (p,)).fetchone()[0] for p in gold.get(record_id, {})}
                for file in files:
                    counts[file] += 1
        return dict(counts)
    finally:
        connection.close()


def pilot_selection(db_path: Path, cells: dict[str, list[str]], gold: dict[str, dict[str, str]], files: int, radius: int) -> dict[str, list[str]]:
    """The `files` files holding the most bench pairs; in each, every gold passage and the `radius` passages either side of it."""
    counts = pair_counts(db_path, cells, gold)
    chosen = [f for f, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:files]]
    anchors = {p for ids in cells.values() for r in ids for p in gold.get(r, {})}
    selection = {}
    for file in sorted(chosen):
        connection = sqlite3.connect(db_path)
        try:
            ordered = [r[0] for r in connection.execute("SELECT passage_id FROM passages WHERE file = ? ORDER BY byte_start, ordinal", (file,))]
        finally:
            connection.close()
        position = {pid: i for i, pid in enumerate(ordered)}
        keep: set[int] = set()
        for anchor in anchors & set(position):
            i = position[anchor]
            keep.update(range(max(0, i - radius), min(len(ordered), i + radius + 1)))
        selection[file] = [ordered[i] for i in sorted(keep)]
    return selection


def _shuffle_key(passage_id: str) -> str:
    return hashlib.sha1(passage_id.encode()).hexdigest()


def embedding_items(db_path: Path, world: str, priority: Iterable[str]) -> tuple[list[tuple[str, str]], int]:
    """Passages of the shelf's files, the priority files first in file order, then every other passage in a fixed pseudo-random
    order. Returns the pairs and how many belong to the priority files."""
    priority = set(priority)
    connection = sqlite3.connect(db_path)
    try:
        rows = connection.execute(
            "SELECT p.passage_id, p.file, p.text FROM passages p WHERE EXISTS "
            "(SELECT 1 FROM shelf_files s WHERE s.file = p.file AND s.world = ?) ORDER BY p.file, p.byte_start, p.ordinal", (world,)).fetchall()
    finally:
        connection.close()
    first = [(pid, text) for pid, file, text in rows if file in priority]
    rest = sorted(((pid, text) for pid, file, text in rows if file not in priority), key=lambda item: _shuffle_key(item[0]))
    return first + rest, len(first)


def keyword_ranker(db_path: Path, world: str, restrict: set[str] | None = None, depth: int = DEPTH) -> Callable[[str], list[str]]:
    def rank(text: str) -> list[str]:
        if restrict is None:
            return bench.ranked(db_path, text, world, depth)
        deep = bench.ranked(db_path, text, world, 4000)
        return [p for p in deep if p in restrict][:depth]

    return rank


def cases_with(db_path: Path, world: str, rank, gold: dict[str, dict[str, str]]):
    evidence = bench.load_record_evidence(catalog.REPO_ROOT / "records" / world)
    cells = bench.load_cells(world)
    cases, _, ungrounded = bench.run_bench(db_path, world, evidence, cells, bench.load_subquestions(), bench.load_questions(),
                                           rank=rank, gold_cache=gold)
    return cases


def recall_at(cases: Sequence[Case], k: int) -> float:
    return sum(1 for c in cases if c.best_rank is not None and c.best_rank <= k) / len(cases) if cases else 0.0


def recall_row(cases: Sequence[Case]) -> dict[str, dict[int, float]]:
    return {condition: {k: recall_at([c for c in cases if c.condition == condition], k) for k in KS} for condition in WORDING_CONDITIONS}


CLUSTER = re.compile(r"^C(\d+)")


def by_cluster(cases: Sequence[Case]) -> dict[str, list[Case]]:
    groups: dict[str, list[Case]] = defaultdict(list)
    for case in cases:
        groups[case.cluster].append(case)
    return dict(sorted(groups.items(), key=lambda kv: int(CLUSTER.match(kv[0]).group(1))))


def percent(value: float) -> str:
    return f"{round(value * 100)}%"


def recall_table(rows: dict[str, Sequence[Case]]) -> str:
    lines = ["| Run | wording @10 | @20 | wording+label @10 | @20 | record routing @10 | @20 |", "|---|---:|---:|---:|---:|---:|---:|"]
    for name, cases in rows.items():
        r = recall_row(cases)
        cells = [percent(r[c][k]) for c in WORDING_CONDITIONS for k in KS]
        lines.append(f"| {name} | " + " | ".join(cells) + " |")
    return "\n".join(lines)
