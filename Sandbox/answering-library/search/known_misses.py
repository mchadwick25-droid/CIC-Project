"""Existence checks for passages a question should reach, from the visitor's own words (lpc). Each check reports found or not found in the top 10 by each method; it is not a rate.

  python -m search.known_misses --db DB.sqlite --models DIR --vectors DIR --out RESULT.json
"""
import argparse
import json
import sqlite3
import sys
from pathlib import Path

from index import bench as old
from index.catalog import REPO_ROOT

from .benchrun import best_rank, seed_ids
from .engine import Search
from .meaning import VectorStore
from .onnx_models import BgeSmallEmbedder, MiniLMReranker

WORDING = {
    "q029": "Did Origen really teach that everyone would be saved, and was he condemned for it?",
    "q099": "Did you see miracles yourself, or only hear of them?",
    "q100": "Be honest: were the miracle stories true, or were they how you talked?",
    "q101": "In your time, was it thought right for a father to beat his son if he did it out of love?",
    "q102": "Did Augustine say a Christian should never defend himself?",
}
ARTICLE = "npnf102_augustine-city-of-god-christian-doctrine.xml"
LETTERS = "npnf101_augustine-confessions-letters.xml"
TOP = 10


def checks(connection: sqlite3.Connection) -> list[dict]:
    def ids(sql, *params):
        return {r[0] for r in connection.execute(sql, params)}

    quote = old.load_record_evidence(REPO_ROOT / "records" / "lpc")["lpc.quote.love-and-do-what-thou-wilt"]
    by_passage = {r[0]: r[1] for r in connection.execute("SELECT passage_id, id FROM passages")}
    return [
        {"name": "Letter 47.5 (Augustine to Publicola)", "question": "q102", "cell": "C9.S4",
         "gold": ids("SELECT id FROM passages WHERE file = ? AND division_locus = 'vii.1.XLVII' AND text LIKE '%As to killing others in order to defend%'", LETTERS)},
        {"name": "City of God XXII.8 (miracles)", "question": "q099", "cell": "C13.S3",
         "gold": ids("SELECT id FROM passages WHERE file = ? AND division_locus LIKE 'iv.XXII.8/%' AND division_locus NOT LIKE '%/notes'", ARTICLE)},
        {"name": "City of God XXII.8 (miracles)", "question": "q100", "cell": "C13.S3",
         "gold": ids("SELECT id FROM passages WHERE file = ? AND division_locus LIKE 'iv.XXII.8/%' AND division_locus NOT LIKE '%/notes'", ARTICLE)},
        {"name": "City of God XXI.17 (Origen)", "question": "q029", "cell": "C3.S3",
         "gold": ids("SELECT id FROM passages WHERE file = ? AND division_locus = 'iv.XXI.17'", ARTICLE)},
        {"name": "q101 quote: love-and-do-what-thou-wilt", "question": "q101", "cell": "C8.S7",
         "gold": {by_passage[p] for p in old.gold_passages(Path(connection.execute("PRAGMA database_list").fetchone()[2]), quote) if p in by_passage}},
    ]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, required=True)
    ap.add_argument("--models", type=Path, required=True)
    ap.add_argument("--vectors", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)
    embedder = BgeSmallEmbedder(args.models / "bge-small-en-v1.5.onnx", args.models / "bge-small-en-v1.5.tokenizer.json")
    reranker = MiniLMReranker(args.models / "minilm-l6-msmarco.onnx", args.models / "minilm-l6-msmarco.tokenizer.json")
    search = Search(args.db, "lpc", embedder=embedder, reranker=reranker)
    search.store = VectorStore.load(VectorStore.folder_for(args.vectors, args.db, "lpc", embedder.model_id, search.lens))
    if search.store is None:
        raise SystemExit("no vectors for this index; run search.benchrun first")
    seeds = seed_ids(args.db, "lpc")
    connection = sqlite3.connect(args.db)
    results = []
    lens = set(search.lens)
    for check in checks(connection):
        text = WORDING[check["question"]]
        rankings = {"keyword": search.keyword(text), "meaning": search.meaning(text), "fused": search.fused(text),
                    "fused_seeds": search.fused(text, seeds.get(check["cell"], ()))}
        ranks = {m: best_rank(r, check["gold"]) for m, r in rankings.items()}
        results.append({"name": check["name"], "question": check["question"], "words": text, "gold_passages": len(check["gold"]),
                        "gold_in_lens": len(check["gold"] & lens), "rank": ranks,
                        "in_top_10": {m: (r is not None and r <= TOP) for m, r in ranks.items()}})
    args.out.write_text(json.dumps(results, indent=1), encoding="utf-8")
    print(json.dumps(results, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
