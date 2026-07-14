"""Shared batch-evaluation helper for Retrieve-When / Do-Not-Retrieve-When filtering.

Both the lexicon and story retrievers ask an LLM whether each RAG candidate
should actually be retrieved for a given turn. Evaluating one candidate per
LLM call meant a single representative turn could fire 4-6 filter calls just
for the lexicon, plus more for stories - real added latency. This batches all
of a retriever's candidates that have Retrieve-When/Do-Not-Retrieve-When
conditions into a single LLM call per retriever per turn.
"""

import re
from dataclasses import dataclass


@dataclass
class Candidate:
    """A RAG candidate awaiting a retrieve/skip decision."""

    label: str
    retrieve_when: str
    do_not_retrieve_when: str
    tier: int = 1


_LINE_PATTERN = re.compile(r"^\s*(\d+)\.\s*(RETRIEVE|SKIP)\s*:\s*(.*)$", re.IGNORECASE)

# How close to the top of the initial semantic search a Tier 1 candidate
# must rank to short-circuit straight to RETRIEVE, bypassing the LLM vote
# entirely. See partition_tier1_short_circuit for why this exists.
TIER1_SHORT_CIRCUIT_RANK = 2


def partition_tier1_short_circuit(
    candidate_docs: list,
    conversation_context: str,
    label_key: str,
) -> tuple[list, list]:
    """
    Split retrieval candidates into (auto_retrieve, needs_llm_vote).

    A Tier 1 document - a world's own human-curated center-of-gravity term
    or story, per its front-matter - that also lands among the closest
    semantic matches for the query is retrieved deterministically, without
    an LLM relevance vote. This exists because asking the LLM to judge
    Tier 1 relevance "generously" was tried three ways (a shared-batch
    instruction, an isolated single-candidate call, and an isolated call
    with an explicit "don't let prior context override this" clause) and
    still reverted to literal keyword-matching against the participant's
    exact wording once real conversation context was present - see the
    session notes around 2026-07-12. The vector embedding plus the
    human-curated Tier 1 flag are a stronger and cheaper signal than
    further prompt engineering achieved.

    A term already named in conversation_context is excluded from the
    short-circuit (falls through to the normal LLM vote instead), as a
    cheap proxy for "already surfaced this turn" - the one genuine
    Do-Not-Retrieve-When case a pure rank/tier check can't itself detect.
    """
    auto_retrieve = []
    needs_llm_vote = []
    context_lower = conversation_context.lower()

    for rank, doc in enumerate(candidate_docs):
        label = doc.metadata.get(label_key, "")
        is_gravity_term = doc.metadata.get("tier") == 1 and rank < TIER1_SHORT_CIRCUIT_RANK
        already_discussed = bool(label) and label.lower() in context_lower
        # A chunk's own Do-Not-Retrieve-When can name a specific, easily-
        # confused sibling term (e.g. "don't retrieve this hymn-genre term
        # when the participant is actually asking about a different, prose
        # genre") rather than a generic cross-world guard. The short-circuit
        # never evaluates that text at all, so a chunk authored with this
        # kind of narrow disambiguation in mind can opt out of the
        # short-circuit entirely via this flag, forcing its own
        # Do-Not-Retrieve-When condition through the LLM vote instead of
        # being silently bypassed.
        force_llm_vote = bool(doc.metadata.get("force_llm_vote"))

        if is_gravity_term and not already_discussed and not force_llm_vote:
            auto_retrieve.append(doc)
        else:
            needs_llm_vote.append(doc)

    return auto_retrieve, needs_llm_vote


def evaluate_batch(
    llm,
    candidates: list[Candidate],
    query: str,
    conversation_context: str,
    item_noun: str = "entry",
    extra_instruction: str = "",
) -> list[tuple[bool, str]]:
    """
    Decide retrieve/skip for every candidate, in as few LLM calls as possible.

    Candidates with no Retrieve-When/Do-Not-Retrieve-When conditions are
    resolved locally (always retrieved, matching the single-item behavior
    this replaces). Everything else goes into one batched prompt. Returns
    decisions in the same order as `candidates`.
    """
    results: list[tuple[bool, str] | None] = [None] * len(candidates)
    needs_llm: list[int] = []

    for i, candidate in enumerate(candidates):
        if not candidate.retrieve_when and not candidate.do_not_retrieve_when:
            results[i] = (True, "No conditions specified, using semantic match")
        else:
            needs_llm.append(i)

    if not needs_llm:
        return results  # type: ignore[return-value]

    # Tier 1 candidates (a world's own declared center-of-gravity concepts)
    # are evaluated in their own smaller call, separate from Tier 2/3
    # candidates. Mixing them into one batch was found to dilute the
    # generous-weighting instruction for Tier 1 terms: evaluated alone, a
    # Tier 1 term like raza correctly retrieves on a foundational question
    # even without literal keyword overlap; mixed into a 6-candidate batch
    # dominated by peripheral Tier 2/3 terms, the model reverted to uniform
    # literal keyword-matching across the whole batch and the exception was
    # lost. Splitting costs at most one extra LLM call per retriever per
    # turn (only when both tiers are present in the candidate pool).
    tier1 = [i for i in needs_llm if candidates[i].tier == 1]
    other = [i for i in needs_llm if candidates[i].tier != 1]

    if tier1:
        tier1_instruction = extra_instruction + (
            " Every candidate in this batch is Tier 1. Judge relevance against the participant's "
            "own question, not against whether another representative's answer already covered the "
            "ground - a different world's answer having already touched the topic is not a reason to "
            "SKIP this world's own center-of-gravity term; this representative would still reach for "
            "it as their own formation's way into the same question."
        )
        _run_batch(llm, candidates, tier1, query, conversation_context, item_noun, tier1_instruction, results)
    if other:
        _run_batch(llm, candidates, other, query, conversation_context, item_noun, extra_instruction, results)

    return results  # type: ignore[return-value]


def _run_batch(
    llm,
    candidates: list[Candidate],
    indices: list[int],
    query: str,
    conversation_context: str,
    item_noun: str,
    extra_instruction: str,
    results: list,
) -> None:
    """Run one batched evaluation call for the given candidate indices, writing decisions into `results` in place."""
    entries_block = "\n\n".join(
        f"""{position}. {item_noun.capitalize()}: {candidates[i].label}
TIER: {candidates[i].tier}{" (this world's own declared center of gravity - its most foundational, load-bearing concept)" if candidates[i].tier == 1 else ""}
RETRIEVE-WHEN: {candidates[i].retrieve_when or "None specified"}
DO-NOT-RETRIEVE-WHEN: {candidates[i].do_not_retrieve_when or "None specified"}"""
        for position, i in enumerate(indices, start=1)
    )

    prompt = f"""You are evaluating whether each of the following {item_noun} candidates should be retrieved for a conversation.

Participant's message: {query}

Recent conversation context: {conversation_context}

Candidates:

{entries_block}

For EACH numbered candidate above, decide independently whether it should be retrieved.
{extra_instruction}
Respond with exactly {len(indices)} lines, one per candidate, in this exact format:
N. RETRIEVE: <brief reason>
or
N. SKIP: <brief reason>

Use the same numbering as above. Do not add commentary outside these lines.
"""

    response = llm.invoke(prompt)
    parsed: dict[int, tuple[bool, str]] = {}

    for line in response.content.strip().split("\n"):
        match = _LINE_PATTERN.match(line)
        if not match:
            continue
        position = int(match.group(1))
        should_retrieve = match.group(2).upper() == "RETRIEVE"
        reason = match.group(3).strip() or ("Matched conditions" if should_retrieve else "Did not match conditions")
        parsed[position] = (should_retrieve, reason)

    for position, i in enumerate(indices, start=1):
        results[i] = parsed.get(position, (False, "No decision returned by batch evaluation; defaulting to skip"))
