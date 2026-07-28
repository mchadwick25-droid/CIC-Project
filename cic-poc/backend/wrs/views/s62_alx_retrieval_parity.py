"""S6.2 S2.8-equivalent retrieval-parity (G), Alexandria: port of the Desert
instrument (retrieval_parity.py) with the world switched - staged Alexandria
chunks -> FAISS via the runtime indexers -> the alexandria golden cases vs the
committed baseline aggregate. Standard: NO REGRESSION.

BASELINE CHOICE, discovered not assumed: the Desert instrument points at
the ORIGINAL retrieval_baseline.json, which predates S3.4/R6's
vote-bracket narrowing - for Desert the two agree (its sentinel-heavy
DNRW set keeps the bracket narrow either way), but for Alexandria the
stale file carries pre-R6 pass@k[skip]=1.0 while every current committed
baseline (retrieval_post_S3.4.json onward through B-RETR-POST-P3.json)
carries 0.0 - the R6-designed narrowing measured on a world whose 45
lexicon DNRW clauses are ALL genuinely evaluable (under an always-skip
vote everything guarded drops). A control run of the DEPLOYED chunks
through this harness reproduces the 6 stale-baseline 'regressions'
identically, proving the staged views are not the cause. This instrument
therefore compares against B-RETR-POST-P3.json, the current committed
baseline (the same one S5.3's rule-2 re-verify runs against).

Builds FAISS lexicon+story indexes from the staged view output (the same
LexiconIndexer/StoryIndexer the runtime uses, same deterministic local
embeddings), injects them into the real retrievers, and re-runs the B-RETR
golden cases for desert-monasticism. Standard: NO REGRESSION against the
committed B-RETR baseline (Ministry/Technology/Pass2/baselines/
retrieval_baseline.json) on the desert aggregate - mean MRR per category,
pass/recall@k under both LLM-vote bracket policies, isolation violations,
metadata checks.

Prints a side-by-side table and exits nonzero on any regression
(a metric strictly worse than baseline). Improvements are reported, not
hidden - e.g. the retired cross-world guard class changes some decision
paths by design (B-RETR's own dead-guard finding).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

STAGING = HERE / "staging" / "alexandria_world"
BASELINE = BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "baselines" / "B-RETR-POST-P3.json"
WID = "alexandria-catechetical"


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
    assert spec, "no alexandria golden file"

    from app.world_manifest import get_manifest_entry
    own_stems = world_stems(get_manifest_entry(WID).data_dir_name)
    # staged chunks keep deployed filenames, so own_stems is unchanged
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
    out = HERE / "staging" / "s62_alx_retrieval_parity_result.json"
    out.write_text(json.dumps({"aggregate": agg, "regressions": regressions},
                              indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"written: {out}")
    return 1 if regressions else 0


if __name__ == "__main__":
    sys.exit(main())
