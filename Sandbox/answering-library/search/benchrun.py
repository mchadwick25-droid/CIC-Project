"""Score retrieval of the passages a record cites, from the visitor's wording, four ways inside the lens, and test each method against the others.

  python -m search.benchrun --world lpc --db DB.sqlite --models DIR --vectors DIR --out RESULT.json

Methods: keyword, meaning, fused (keyword + meaning, reranked), fused with the world's reviewed seeds as a further ranking.
The measure is whether a passage the record cites is in the top 5, 10 and 20. Code decides; no model call, no reader.
"""
import argparse
import json
import math
import sqlite3
import sys
import time
from pathlib import Path

import yaml

from index import bench as old
from index.catalog import REPO_ROOT

from .engine import Search
from .meaning import VectorStore
from .onnx_models import BgeSmallEmbedder, MiniLMReranker

KS = (5, 10, 20)
METHODS = ("keyword_unlensed", "keyword", "meaning", "fused", "fused_seeds")
PAIRS = (("meaning", "keyword"), ("fused", "keyword"), ("fused", "meaning"), ("fused_seeds", "fused"))
ALPHA = 0.01


def sign_test_p(wins: int, losses: int) -> float:
    """Two-sided exact binomial p for wins against losses under an even split; ties are left out."""
    n = wins + losses
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, i) for i in range(min(wins, losses) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def seed_ids(db_path: Path, world: str) -> dict[str, list[int]]:
    path = REPO_ROOT / "Build" / "worlds" / world / "build" / f"{world}_Passage_Seeds.yaml"
    if not path.is_file():
        return {}
    seeds = yaml.safe_load(path.read_text(encoding="utf-8")).get("subquestions") or {}
    connection = sqlite3.connect(db_path)
    try:
        out = {}
        for sid, entry in seeds.items():
            ids = []
            for hit in entry.get("seeds") or []:
                row = connection.execute("SELECT id FROM passages WHERE passage_id = ?", (hit["passage_id"],)).fetchone()
                if row:
                    ids.append(row[0])
            out[sid] = ids
        return out
    finally:
        connection.close()


def best_rank(ranking: list[int], gold: set[int]) -> int | None:
    for position, item in enumerate(ranking, 1):
        if item in gold:
            return position
    return None


def run(world: str, db: Path, models: Path, vectors_root: Path, progress=print) -> dict:
    embedder = BgeSmallEmbedder(models / "bge-small-en-v1.5.onnx", models / "bge-small-en-v1.5.tokenizer.json")
    reranker = MiniLMReranker(models / "minilm-l6-msmarco.onnx", models / "minilm-l6-msmarco.tokenizer.json")
    search = Search(db, world, embedder=embedder, reranker=reranker)
    folder = VectorStore.folder_for(vectors_root, db, world, embedder.model_id, search.lens)
    store = VectorStore.load(folder)
    if store is None:
        started = time.monotonic()
        store = VectorStore.build(folder, db, search.lens, embedder, lambda done, total: progress(f"  embedded {done}/{total} windows"))
        progress(f"vectors built in {time.monotonic() - started:.0f} s")
    search.store = store
    seeds = seed_ids(db, world)

    evidence = old.load_record_evidence(REPO_ROOT / "records" / world)
    cells, subs, questions = old.load_cells(world), old.load_subquestions(), old.load_questions()
    connection = sqlite3.connect(db)
    to_internal = dict(connection.execute("SELECT passage_id, id FROM passages"))
    connection.close()
    gold_all = {rid: {to_internal[p] for p in old.gold_passages(db, ev) if p in to_internal} for rid, ev in evidence.items()}
    lens_set = set(search.lens)

    cases, rank_cache = [], {}
    for cell, record_ids in cells.items():
        sub = subs.get(cell)
        if not sub:
            continue
        usable = [r for r in record_ids if gold_all.get(r)]
        for wording_id in sub["ids"]:
            wording = questions.get(wording_id)
            if not wording or not usable:
                continue
            key = (cell, wording_id)
            if key not in rank_cache:
                kw = search.keyword(wording)
                ranks = {
                    "keyword_unlensed": _unlensed(db, wording, world),
                    "keyword": kw, "meaning": search.meaning(wording),
                    "fused": search.fused(wording), "fused_seeds": search.fused(wording, seeds.get(cell, ())),
                }
                rank_cache[key] = ranks
                progress(f"  {len(rank_cache)} queries ranked")
            for rid in usable:
                gold = gold_all[rid]
                cases.append({"cell": cell, "wording_id": wording_id, "record_id": rid, "gold_in_lens": bool(gold & lens_set),
                              "rank": {m: best_rank(rank_cache[key][m], gold) for m in METHODS}})
    return {"world": world, "cases": cases, "lens_passages": len(search.lens), "windows": int(store.vectors.shape[0]),
            "summary": summarise(cases)}


def _unlensed(db: Path, wording: str, world: str) -> list[int]:
    """The file-level-shelf keyword ranking (index.bench.ranked) as internal ids, kept as a reference line and not scored as a method."""
    ids = old.ranked(db, wording, world)
    if not ids:
        return []
    connection = sqlite3.connect(db)
    try:
        internal = dict(connection.execute(f"SELECT passage_id, id FROM passages WHERE passage_id IN ({','.join('?' * len(ids))})", ids))
    finally:
        connection.close()
    return [internal[p] for p in ids]


def summarise(cases: list[dict]) -> dict:
    """Case counts, and the paired tests at the level of the query. Every record cited for a sub-question shares one ranking
    for one wording, so the cases of one query are not independent; a query counts as a hit when any of its cases is a hit."""
    queries: dict[tuple, dict] = {}
    for case in cases:
        unit = queries.setdefault((case["cell"], case["wording_id"]), {m: None for m in METHODS})
        for method in METHODS:
            rank = case["rank"][method]
            if rank is not None and (unit[method] is None or rank < unit[method]):
                unit[method] = rank
    units = [{"rank": ranks} for ranks in queries.values()]
    hits = {m: {k: sum(1 for c in cases if _hit(c, m, k)) for k in KS} for m in METHODS}
    query_hits = {m: {k: sum(1 for u in units if _hit(u, m, k)) for k in KS} for m in METHODS}
    paired = {}
    for a, b in PAIRS:
        for k in KS:
            wins = sum(1 for u in units if _hit(u, a, k) and not _hit(u, b, k))
            losses = sum(1 for u in units if _hit(u, b, k) and not _hit(u, a, k))
            p = sign_test_p(wins, losses)
            paired[f"{a} vs {b} @{k}"] = {"wins": wins, "losses": losses, "p": p, "better_at_99": wins > losses and p < ALPHA}
    return {"total_cases": len(cases), "gold_in_lens": sum(1 for c in cases if c["gold_in_lens"]), "hits": hits,
            "total_queries": len(units), "query_hits": query_hits, "paired_at_query_level": paired}


def _hit(case: dict, method: str, k: int) -> bool:
    r = case["rank"][method]
    return r is not None and r <= k


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--world", required=True)
    ap.add_argument("--db", type=Path, required=True)
    ap.add_argument("--models", type=Path, required=True)
    ap.add_argument("--vectors", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)
    result = run(args.world, args.db, args.models, args.vectors)
    args.out.write_text(json.dumps(result, indent=1), encoding="utf-8")
    print(json.dumps(result["summary"], indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
