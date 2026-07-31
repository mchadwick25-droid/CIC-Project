"""The one candidate-to-decision pipeline both retrievers run.

LexiconRetriever.retrieve and StoryRetriever.retrieve were the same ~95 lines
twice: session exclusion, cross-encoder scoring, the rank-aware relevance
threshold, the guard partition, the batched guard vote, and the decision/audit
loop. The only real differences were which metadata key holds a candidate's
display label ("term" vs "story_title"), the noun handed to the guard-vote
prompt, and the default k.

That duplication was not a tidiness problem, it was a correctness problem with
a track record. The adjudication-guard fix had to be written twice, in two
files, in identical form; so did the audit-reason change that came with it.
A maintainer who fixed one and missed the other would have left adjudication
half-guarded - lexicon evidence unfiltered, story evidence still filtered by a
conversational-timing rule - and nothing would have failed. Everything in here
is now written once, and the retrievers differ only where they genuinely
differ: what they index, and how they serialize a chunk for the model.
"""

from dataclasses import dataclass
from pathlib import Path

from langchain_core.documents import Document

from app.rag.batch_evaluate import (Candidate, _evaluable_negative_condition,
                                     evaluate_negative_conditions)
from app.rag.retrieval_mode import RetrievalMode


@dataclass(frozen=True)
class RetrieverSpec:
    """What actually distinguishes one retriever from the other."""

    label_key: str
    """Metadata key holding a candidate's display label - "term" for lexicon
    entries, "story_title" for stories."""

    item_noun: str
    """How the guard-vote prompt should refer to one of these ("lexicon
    entry" / "story")."""

    default_k: int
    """Stories use a lower k than lexicon entries: they are longer, and a
    representative should draw on one or two, not pepper a turn with
    narrative."""


LEXICON_SPEC = RetrieverSpec(label_key="term", item_noun="lexicon entry",
                             default_k=3)
STORY_SPEC = RetrieverSpec(label_key="story_title", item_noun="story",
                           default_k=2)


@dataclass
class PipelineResult:
    """Decided documents plus the full audit trail of what was considered."""

    documents: list[Document]
    reasoning: str
    evaluations: list  # list[RetrievalEvaluation], typed by the caller


def run_retrieval(
    *,
    spec: RetrieverSpec,
    mode: RetrievalMode,
    candidate_docs: list[Document],
    query: str,
    conversation_context: str,
    k: int,
    exclude_ids: set[str] | None,
    filter_llm,
    evaluation_cls,
) -> PipelineResult:
    """Take scored candidates through exclusion, relevance, guards, decisions.

    `evaluation_cls` is RetrievalEvaluation; it is injected rather than
    imported to keep this module free of a back-import into retriever.py,
    which imports this one.
    """
    # ------------------------------------------------------------------
    # S3.3 (Pass 1 R4): deterministic session exclusion by chunk-id stem.
    # Honoured only when the mode allows it - an adjudicator must see the
    # whole record, including what was already surfaced this session, since
    # those are exactly the chunks the judged turn most likely spoke from.
    # This IGNORES a passed exclusion set rather than trusting every caller
    # to omit one; that is the difference between correct-by-construction
    # and correct-by-habit.
    # ------------------------------------------------------------------
    excluded_evals = []
    if exclude_ids and mode.allow_session_exclusion:
        kept = []
        for doc in candidate_docs:
            stem = Path(doc.metadata.get("source_file", "")).stem
            if stem in exclude_ids:
                excluded_evals.append(evaluation_cls(
                    term=doc.metadata.get(spec.label_key, "unknown"),
                    source_file=doc.metadata.get("source_file", ""),
                    retrieved=False,
                    reason="Session exclusion set: already surfaced "
                           "this session (deterministic ID match).",
                ))
            else:
                kept.append(doc)
        candidate_docs = kept

    # ------------------------------------------------------------------
    # S3.4 (Pass 1 R6): relevance is decided by the local cross-encoder,
    # deterministically - the batched LLM relevance vote (and the tier-1
    # short-circuit that existed to protect tier-1 terms from that vote's
    # batch dilution) are both gone. The ONE remaining LLM call judges only
    # Do-Not-Retrieve-When guards, and only when a relevance-kept candidate
    # actually carries an evaluable one - and only in a mode that applies
    # guards at all.
    # ------------------------------------------------------------------
    from app.rag.cross_encoder import score_candidates, threshold_for

    scores = score_candidates(query, candidate_docs)
    rel_threshold = threshold_for(query)
    # S3.4: selection order is the cross-encoder's ranking (its ordering is
    # reliable even where its absolute score is not - see cross_encoder.py);
    # the fused candidate list stays the audit-trail order.
    candidate_docs = [d for _s, d in sorted(
        zip(scores, candidate_docs), key=lambda x: -x[0])]
    scores = sorted(scores, reverse=True)

    decisions_by_id: dict[int, tuple[bool, str]] = {}
    guarded_docs: list[Document] = []
    for rank, (doc, score) in enumerate(zip(candidate_docs, scores)):
        # A candidate the cross-encoder itself ranks inside the final k is
        # never hard-dropped on absolute score: the model's ordering is
        # reliable where its absolute calibration is not (measured -
        # deep-thematic must-docs score in the noise band on clean queries
        # yet rank top). The threshold prunes only beyond-window noise,
        # which also bounds the guard-vote batch.
        if score < rel_threshold and rank >= k:
            decisions_by_id[id(doc)] = (
                False,
                f"Cross-encoder relevance {score:.2f} below threshold "
                f"{rel_threshold} - not relevant to this turn.",
            )
        elif mode.apply_guards and _evaluable_negative_condition(
                doc.metadata.get("do_not_retrieve_when", "")):
            guarded_docs.append(doc)
        else:
            decisions_by_id[id(doc)] = (
                True,
                f"Cross-encoder relevance {score:.2f} - retrieved "
                f"({mode.guardless_audit_reason}).",
            )

    if guarded_docs:
        candidates = [
            Candidate(
                label=doc.metadata.get(spec.label_key, "unknown"),
                retrieve_when=doc.metadata.get("retrieve_when", ""),
                do_not_retrieve_when=doc.metadata.get("do_not_retrieve_when", ""),
                tier=doc.metadata.get("tier", 1),
            )
            for doc in guarded_docs
        ]
        decisions = evaluate_negative_conditions(
            filter_llm,
            candidates,
            query,
            conversation_context,
            item_noun=spec.item_noun,
        )
        decisions_by_id.update(
            {id(doc): decision for doc, decision in zip(guarded_docs, decisions)}
        )

    filtered_docs: list[Document] = []
    reasoning_parts: list[str] = []
    evaluations = list(excluded_evals)

    for doc in candidate_docs:
        should_retrieve, reason = decisions_by_id[id(doc)]
        label = doc.metadata.get(spec.label_key, "unknown")
        source_file = doc.metadata.get("source_file", "")

        evaluations.append(evaluation_cls(
            term=label,
            source_file=source_file,
            retrieved=should_retrieve,
            reason=reason,
        ))

        if should_retrieve and len(filtered_docs) < k:
            filtered_docs.append(doc)
            reasoning_parts.append(f"Retrieved '{label}': {reason}")
        elif should_retrieve:
            reasoning_parts.append(f"Retrieved but over limit '{label}': {reason}")
        else:
            reasoning_parts.append(f"Skipped '{label}': {reason}")

    return PipelineResult(
        documents=filtered_docs,
        reasoning="\n".join(reasoning_parts),
        evaluations=evaluations,
    )
