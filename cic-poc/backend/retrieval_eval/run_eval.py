"""S1.2 retrieval evaluation harness (Pass 1 SS5.4 R0; blueprint S1.2).

Deterministic, zero-API-cost, ID-based evaluation of the CURRENT retrieval
system against per-world golden cases (golden/<world>.yaml).

What "the current system, deterministically" means here, stated precisely:

The live pipeline is: FAISS similarity search (k*2 candidates) ->
partition_tier1_short_circuit (deterministic) -> evaluate_batch, whose first
loop resolves condition-less candidates locally (deterministic - and
faithfully reproduced here including the real behavior that a literal em-dash
sentinel counts as a condition) and sends the rest to a Haiku vote
(non-deterministic). This harness replays every deterministic stage by
calling the REAL code (the real vector stores, the real
partition_tier1_short_circuit, the same condition-less test evaluate_batch
uses at app/rag/batch_evaluate.py:117-121), and BRACKETS the one
non-deterministic stage with two fixed policies:

  vote=retrieve : every LLM-vote candidate is treated as RETRIEVE
  vote=skip     : every LLM-vote candidate is treated as SKIP

The real system always lies between the brackets, and every retrieval
change from Phase 3 onward moves these deterministic numbers falsifiably.
The bracket width itself is a measurement: it is exactly how much of
today's retrieval outcome hangs on the LLM vote R6 replaces.

Metrics per case: pass@k / recall@k over the final retrieved set, MRR over
the ranked candidate list (vote-independent), do_not_retrieve_when
violations (a must_not ID in the final set). Cross-world isolation is
asserted structurally on every case (every returned doc must come from the
world's own index). Optional per-case metadata assertions cover
deterministic regressions (e.g. the madrasha force_llm_vote flag).

Usage (from cic-poc/backend):
  python retrieval_eval/run_eval.py                 # all worlds with golden files
  python retrieval_eval/run_eval.py --world syriac-edessa-nisibis
  python retrieval_eval/run_eval.py --out baseline.json
"""
import argparse
import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

GOLDEN_DIR = Path(__file__).with_name("golden")

CATEGORIES = (
    "verbatim-term", "thematic", "de-dup", "negative-condition",
    "reactive-turn", "cross-world-isolation",
)


def load_yaml(path):
    import yaml
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def doc_id(doc):
    sf = doc.metadata.get("source_file", "")
    return Path(sf).stem if sf else doc.metadata.get("term") or doc.metadata.get("story_title") or "?"


def replay(retriever, label_key, query, context, k, context_surfaced=None):
    """Replay the current pipeline's deterministic stages on real data.

    Returns (ranked_ids, final_sets_by_policy, decisions) where decisions maps
    id -> 'auto' | 'no-conditions' | 'llm-vote' | 'over-limit-<policy>'.
    """
    # S3.2: the candidate path is the retriever's own candidate_search
    # (hybrid BM25+dense+expansion) - the harness measures the real
    # pipeline, same (doc, score) contract as the old direct call
    docs_with_scores = retriever.candidate_search(query, k)
    candidate_docs = [d for d, _s in docs_with_scores]
    ranked_ids = [doc_id(d) for d in candidate_docs]

    # S3.3: the session exclusion set, modeled the way the runtime holds it
    # (ConversationState.surfaced_chunk_ids -> retrieve(exclude_ids=...)).
    # A case's `surfaced:` list stands for the chunks a real session would
    # have recorded when the context transcript happened - the de-dup
    # category's test is now "is the deterministic exclusion honored
    # through the pipeline", replacing the old "can the substring proxy
    # catch it" (which measurably could not, on composite labels).
    surfaced = set(context_surfaced or [])
    if surfaced:
        candidate_docs = [d for d in candidate_docs if doc_id(d) not in surfaced]

    # S3.4 (Pass 1 R6): relevance is now the DETERMINISTIC local
    # cross-encoder - the real scoring path, real threshold. The only
    # remaining non-deterministic stage is the retained guard vote, so
    # the retrieve/skip bracket now spans ONLY candidates that are
    # relevance-kept AND carry a genuinely evaluable Do-Not-Retrieve-When
    # (retrieve = guard never fires; skip = guard always fires). The
    # bracket-width collapse relative to S3.3 is R6's designed narrowing,
    # measured.
    from app.rag.batch_evaluate import _evaluable_negative_condition
    from app.rag.cross_encoder import score_candidates, threshold_for

    scores = score_candidates(query, candidate_docs)
    rel_threshold = threshold_for(query)
    # selection order = cross-encoder ranking (same as the retrievers);
    # ranked_ids (MRR) stays the fused candidate order
    sel_docs = [d for _s, d in sorted(zip(scores, candidate_docs),
                                       key=lambda x: -x[0])]
    sel_scores = sorted(scores, reverse=True)
    kept, ce_dropped = [], set()
    for rank, (d, s) in enumerate(zip(sel_docs, sel_scores)):
        # same rank-guard as the retrievers: CE-top-k never hard-dropped
        if s >= rel_threshold or rank < k:
            kept.append(d)
        else:
            ce_dropped.add(id(d))
    guarded = {id(d) for d in kept if _evaluable_negative_condition(
        d.metadata.get("do_not_retrieve_when", ""))}

    finals = {}
    decisions = {}
    for policy in ("retrieve", "skip"):
        final = []
        for d in sel_docs:
            i = id(d)
            if i in ce_dropped:
                dec, keep = "ce-drop", False
            elif i in guarded:
                dec, keep = "guard-vote", (policy == "retrieve")
            else:
                dec, keep = "ce-keep", True
            if keep and len(final) < k:
                final.append(doc_id(d))
            decisions.setdefault(doc_id(d), dec)
        finals[policy] = final
    return ranked_ids, finals, decisions


def world_stems(world_dir_name):
    """All chunk-file stems belonging to a world's own data directory -
    the ground truth for the structural cross-world-isolation assertion
    (source_file metadata carries bare filenames, not paths)."""
    base = BACKEND / "data" / world_dir_name
    stems = set()
    for sub in ("lexicon_chunks", "story_chunks"):
        d = base / sub
        if d.is_dir():
            stems |= {p.stem for p in d.glob("*.md")}
    return stems


def eval_case(case, retrievers, own_stems):
    retr_kind = case.get("retriever", "lexicon")
    retriever = retrievers[retr_kind]
    label_key = "term" if retr_kind == "lexicon" else "story_title"
    default_k = 3 if retr_kind == "lexicon" else 2
    k = case.get("k", default_k)
    must = case.get("must", []) or []
    must_not = case.get("must_not", []) or []

    ranked, finals, decisions = replay(
        retriever, label_key, case["query"], case.get("context", ""), k,
        context_surfaced=case.get("surfaced"))

    # structural cross-world isolation: every candidate must be one of this
    # world's own chunk files (per-world index invariant)
    foreign = [r for r in ranked if r not in own_stems]

    result = {
        "id": case["id"], "category": case["category"], "retriever": retr_kind,
        "k": k, "ranked_candidates": ranked, "decisions": decisions,
        "isolation_violations": foreign, "policies": {},
    }
    if must:
        ranks = [ranked.index(m) + 1 for m in must if m in ranked]
        result["mrr"] = round(1.0 / min(ranks), 4) if ranks else 0.0
    else:
        result["mrr"] = None
    for policy, final in finals.items():
        got = [m for m in must if m in final]
        viol = [m for m in must_not if m in final]
        result["policies"][policy] = {
            "final": final,
            "pass_at_k": (1 if got else 0) if must else None,
            "recall_at_k": round(len(got) / len(must), 4) if must else None,
            "violations": viol,
        }

    checks = []
    for a in case.get("assert_metadata", []) or []:
        hits = [d for d, _s in retriever.vector_store.similarity_search_with_score(a["id"], k=50)
                if doc_id(d) == a["id"]]
        actual = hits[0].metadata.get(a["field"]) if hits else "<doc-not-found>"
        checks.append({"id": a["id"], "field": a["field"],
                       "expected": a["equals"], "actual": actual,
                       "pass": bool(hits) and actual == a["equals"]})
    if checks:
        result["metadata_checks"] = checks
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--world", default=None)
    p.add_argument("--out", default=None)
    args = p.parse_args()

    from app.rag.retriever import LexiconRetriever
    from app.rag.story_retriever import StoryRetriever

    golden_files = sorted(GOLDEN_DIR.glob("*.yaml"))
    if args.world:
        golden_files = [f for f in golden_files if load_yaml(f)["world_id"] == args.world]

    out = {"worlds": {}}
    for gf in golden_files:
        spec = load_yaml(gf)
        wid = spec["world_id"]
        from app.world_manifest import get_manifest_entry
        own_stems = world_stems(get_manifest_entry(wid).data_dir_name)

        retrievers = {
            "lexicon": LexiconRetriever(world_id=wid),
            "story": StoryRetriever(world_id=wid),
        }
        cases = [eval_case(c, retrievers, own_stems) for c in spec["cases"]]

        agg = {"n_cases": len(cases), "by_category": {}}
        for cat in CATEGORIES:
            rows = [c for c in cases if c["category"] == cat]
            if not rows:
                continue
            mrrs = [r["mrr"] for r in rows if r["mrr"] is not None]
            entry = {"n": len(rows), "mean_mrr": round(
                sum(mrrs) / len(mrrs), 4) if mrrs else None}
            for policy in ("retrieve", "skip"):
                pr = [r["policies"][policy] for r in rows]
                scored = [x for x in pr if x["pass_at_k"] is not None]
                entry[f"pass_at_k[{policy}]"] = round(
                    sum(x["pass_at_k"] for x in scored) / len(scored), 4) if scored else None
                entry[f"recall_at_k[{policy}]"] = round(
                    sum(x["recall_at_k"] for x in scored) / len(scored), 4) if scored else None
                entry[f"violations[{policy}]"] = sum(len(x["violations"]) for x in pr)
            agg["by_category"][cat] = entry
        agg["isolation_violations_total"] = sum(len(c["isolation_violations"]) for c in cases)
        agg["metadata_check_failures"] = sum(
            1 for c in cases for m in c.get("metadata_checks", []) if not m["pass"])

        out["worlds"][wid] = {"aggregate": agg, "cases": cases}

    text = json.dumps(out, indent=2, sort_keys=True)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"written: {args.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
