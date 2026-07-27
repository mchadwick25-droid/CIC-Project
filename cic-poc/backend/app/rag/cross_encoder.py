"""S3.4 - local CPU cross-encoder relevance scoring (Pass 1 R6).

Replaces the batched LLM relevance vote: relevance keep/drop is now a
deterministic local model scoring (query, retrieval-surface) pairs -
the Tier-2/3 batch-dilution failure the vote was patched around three
times becomes structurally impossible (there is no shared batch prompt
for one candidate's phrasing to dilute), and the ~2 Haiku relevance
calls per world per turn leave the latency path. The ONE remaining
Haiku call (see batch_evaluate.evaluate_negative_conditions) is invoked
only for candidates carrying a genuinely evaluable Do-Not-Retrieve-When
condition - judging the guard, never relevance.

Model: cross-encoder/ms-marco-MiniLM-L-6-v2 - the standard compact
passage-reranking cross-encoder; CPU, deterministic, ~90MB, loaded once
per process (same pattern as app/rag/embeddings.py and for the same
OOM reason).

Threshold: raw logit. Calibrated against the retrieval harness's golden
cases (see the S3.4 gate artifact for the sweep) - kept as a module
constant until S4.4 makes parameters.yaml the runtime parameter home.
"""
from __future__ import annotations

from langchain_core.documents import Document

# Calibrated on the 105-case golden set (distributions in the S3.4 gate
# artifact): on CLEAN queries, must-docs score >= 1.2 (verbatim min 2.7)
# and noise sits at median -10.7 - the -4.0 threshold separates with
# margin. On REACTIVE-SHAPE queries (another world's full turn embedded
# via the runtime's own '<name> just said:' concatenation - the exact R9
# defect S3.5 replaces), must-docs score in the noise band (median -8.3
# vs noise p90 -1.0): NO threshold separates them, measured. Until S3.5
# ships the rewrite, a query carrying the structural reactive marker gets
# the lenient floor - the cross-encoder still re-ranks (its ordering is
# informative even when its absolute score is not), but only extreme
# noise is dropped. The marker is our own construction, not a heuristic
# on participant text, and dies naturally when S3.5 replaces the
# concatenation.
RELEVANCE_THRESHOLD = -4.0
RELEVANCE_THRESHOLD_REACTIVE = -11.0
REACTIVE_MARKER = " just said: "


def threshold_for(query: str) -> float:
    return (RELEVANCE_THRESHOLD_REACTIVE if REACTIVE_MARKER in query
            else RELEVANCE_THRESHOLD)

_model = None


def _get_model():
    global _model
    if _model is None:
        from sentence_transformers import CrossEncoder
        _model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2",
                              max_length=512)
    return _model


def _pair_text(d: Document) -> str:
    """The doc side of the scoring pair: the retrieval surface PLUS a
    body snippet. The surface alone underserves the cross-encoder - its
    retrieve-when lines are meta-descriptions ('participant asks
    about...'), which a passage-relevance model scores poorly (measured:
    Sarah's story scored below the allusion records on a women-in-the-
    desert question until its own text - 'elders came to test her as a
    woman' - entered the pair). The snippet is capped so the pair stays
    inside the model's 512-token window."""
    body = d.metadata.get("content", "") or ""
    return d.page_content + ("\n" + body[:400] if body else "")


def score_candidates(query: str, docs: list[Document]) -> list[float]:
    """Raw cross-encoder logits for (query, surface+snippet) pairs."""
    if not docs:
        return []
    pairs = [(query, _pair_text(d)) for d in docs]
    return [float(s) for s in _get_model().predict(pairs)]


def relevance_partition(query: str, docs: list[Document]
                        ) -> tuple[list[Document], list[tuple[Document, float]]]:
    """(kept, dropped_with_scores) - deterministic relevance decision."""
    scores = score_candidates(query, docs)
    kept, dropped = [], []
    for d, s in zip(docs, scores):
        if s >= RELEVANCE_THRESHOLD:
            kept.append(d)
        else:
            dropped.append((d, s))
    return kept, dropped
