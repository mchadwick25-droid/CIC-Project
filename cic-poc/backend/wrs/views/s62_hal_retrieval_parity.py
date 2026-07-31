"""S6.2/HAL S2.8-equivalent retrieval-parity (G): the ALX instrument with
the world switched - staged HAL chunks -> FAISS via the runtime
indexers -> the hieronymian golden cases vs the committed B-RETR-POST-P3
baseline (the ALX-established correct baseline; the stale pre-R6 file
is NOT used). Standard: NO REGRESSION.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

STAGING = HERE / "staging" / "hieronymian_world"
BASELINE = BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "baselines" / "B-RETR-POST-P3.json"
WID = "hieronymian-ascetic-literary"


def main() -> int:
    import yaml
    from app.rag.indexer import LexiconIndexer
    from app.rag.story_indexer import StoryIndexer
    from app.rag.retriever import LexiconRetriever
    from app.rag.story_retriever import StoryRetriever
    from retrieval_eval.run_eval import (CATEGORIES, GOLDEN_DIR, eval_case,
                                          load_yaml, world_stems)

    lex_store = LexiconIndexer().index_lexicon(STAGING / "lexicon_chunks")
    story_store = StoryIndexer().index_stories(STAGING / "story_chunks")
    retrievers = {
        "lexicon": LexiconRetriever(vector_store=lex_store, world_id=WID),
        "story": StoryRetriever(vector_store=story_store, world_id=WID),
    }

    spec = None
    for gf in sorted(GOLDEN_DIR.glob("*.yaml")):
        s = load_yaml(gf)
        if s["world_id"] == WID:
            spec = s
            break
    assert spec, "no hieronymian golden file"

    from app.world_manifest import get_manifest_entry
    own_stems = world_stems(get_manifest_entry(WID).data_dir_name)
    # HAL: every staged file keeps a deployed filename (no new-at-swap
    # chunks) - the deployed own-stems set is exact, no extension needed
    own_stems = set(own_stems)
    cases = [eval_case(c, retrievers, own_stems) for c in spec["cases"]]

    agg = {"by_category": {}}
    for cat in CATEGORIES:
        rows = [c for c in cases if c["category"] == cat]
        if not rows:
            continue
        mrrs = [r["mrr"] for r in rows if r["mrr"] is not None]
        entry = {"n": len(rows),
                 "mean_mrr": round(sum(mrrs) / len(mrrs), 4) if mrrs else None}
        for policy in ("retrieve", "skip"):
            pr = [r["policies"][policy] for r in rows]
            scored = [x for x in pr if x["pass_at_k"] is not None]
            entry[f"pass_at_k[{policy}]"] = round(
                sum(x["pass_at_k"] for x in scored) / len(scored), 4) if scored else None
            entry[f"recall_at_k[{policy}]"] = round(
                sum(x["recall_at_k"] for x in scored) / len(scored), 4) if scored else None
            entry[f"violations[{policy}]"] = sum(len(x["violations"]) for x in pr)
        agg["by_category"][cat] = entry
    agg["isolation_violations_total"] = sum(
        len(c["isolation_violations"]) for c in cases)
    agg["metadata_check_failures"] = sum(
        1 for c in cases for m in c.get("metadata_checks", []) if not m["pass"])

    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    base_agg = base["worlds"][WID]["aggregate"]

    regressions = []
    print(f"{'metric':58s} {'baseline':>10s} {'staged':>10s}")
    for cat, entry in agg["by_category"].items():
        b = base_agg["by_category"].get(cat, {})
        for key, sv in entry.items():
            if key == "n":
                continue
            bv = b.get(key)
            marker = ""
            if key.startswith("violations"):
                if bv is not None and sv > bv:
                    marker = "  << REGRESSION"
                    regressions.append((cat, key, bv, sv))
            elif bv is not None and sv is not None and sv < bv - 1e-9:
                marker = "  << REGRESSION"
                regressions.append((cat, key, bv, sv))
            print(f"{cat + '.' + key:58s} {str(bv):>10s} {str(sv):>10s}{marker}")
    for key in ("isolation_violations_total", "metadata_check_failures"):
        bv, sv = base_agg.get(key), agg[key]
        marker = ""
        if bv is not None and sv > bv:
            marker = "  << REGRESSION"
            regressions.append(("total", key, bv, sv))
        print(f"{key:58s} {str(bv):>10s} {str(sv):>10s}{marker}")

    print(f"\n{len(regressions)} regression(s)")
    out = HERE / "staging" / "s62_hal_retrieval_parity_result.json"
    out.write_text(json.dumps({"aggregate": agg, "regressions": regressions},
                              indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"written: {out}")
    return 1 if regressions else 0


if __name__ == "__main__":
    sys.exit(main())
