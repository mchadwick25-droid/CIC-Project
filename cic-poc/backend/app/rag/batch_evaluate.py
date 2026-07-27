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

from app.usage_logging import log_llm_usage

# The model both LexiconRetriever and StoryRetriever currently hardcode for
# filter_llm (see app/rag/retriever.py and app/rag/story_retriever.py) -
# kept here as its own constant purely so _run_batch's log_llm_usage() call
# can log the real model string without importing either retriever module
# (which would risk a circular import back into this one) or app.graph.nodes
# (which imports app.rag, so a reverse import here would also be circular).
# Independent of those constructors - must be kept in sync by hand if the
# filter model ever changes.
_FILTER_MODEL = "claude-haiku-4-5-20251001"


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


def _evaluable_negative_condition(dnrw: str) -> bool:
    """True if the Do-Not-Retrieve-When text carries at least one clause the
    runtime can genuinely evaluate. The retired condition classes (Pass 1
    SS3.2) don't count: cross-world guards are structural (each world has
    its own index - the guard can never fire) and must not drag a doc to
    the vote on their account. Migrated worlds' chunks no longer carry
    retired clauses at all; this filter matters for the unmigrated worlds'
    hand-authored free text."""
    if not dnrw:
        return False
    retired = ("different world", "cross-apply", "another world's own")
    clauses = [c.strip() for c in dnrw.split(";") if c.strip()]
    return any(not any(r in c.lower() for r in retired) for c in clauses)


def partition_tier1_short_circuit(
    candidate_docs: list,
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

    S3.3 (Pass 1 R4): the old already_discussed substring proxy is GONE -
    it broke on composite labels ("Hesychia (Stillness)" never matched a
    context saying "hesychia", the measured composite-Term de-dup gap).
    Already-surfaced chunks are now excluded deterministically at
    candidate stage by the ID-keyed session exclusion set
    (ConversationState.surfaced_chunk_ids), before this function runs.
    """
    auto_retrieve = []
    needs_llm_vote = []

    for rank, doc in enumerate(candidate_docs):
        is_gravity_term = doc.metadata.get("tier") == 1 and rank < TIER1_SHORT_CIRCUIT_RANK
        # S3.3 (anticipating R6's own stated rule): a candidate carrying a
        # genuinely evaluable Do-Not-Retrieve-When condition NEVER
        # short-circuits past it - its own guard gets the vote. Sentinel
        # nulls are normalized to "" at index time (S3.3), so a non-empty
        # value here is real condition text, not an em-dash. Before this,
        # tier-1 docs bypassed their own guards unless the broken
        # substring proxy happened to catch them - the measured
        # negative-condition worsening when that proxy was removed.
        has_negative_condition = _evaluable_negative_condition(
            doc.metadata.get("do_not_retrieve_when", ""))
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

        if is_gravity_term and not force_llm_vote and not has_negative_condition:
            auto_retrieve.append(doc)
        else:
            needs_llm_vote.append(doc)

    return auto_retrieve, needs_llm_vote


def evaluate_negative_conditions(
    llm,
    candidates: list[Candidate],
    query: str,
    conversation_context: str,
    item_noun: str = "entry",
) -> list[tuple[bool, str]]:
    """S3.4 (Pass 1 R6): the ONE retained Haiku call - judges ONLY whether
    each candidate's own Do-Not-Retrieve-When guard applies to this turn.
    Relevance is no longer this call's question (the local cross-encoder
    decided that deterministically before we got here); every candidate in
    this batch is already relevance-kept and carries a genuinely evaluable
    guard. RETRIEVE unless the guard clearly applies - fail-open toward
    retrieval, because the guard is a narrow disambiguation instrument,
    not a relevance filter."""
    if not candidates:
        return []
    entries_block = "\n\n".join(
        f"""{position}. {item_noun.capitalize()}: {c.label}
DO-NOT-RETRIEVE-WHEN: {c.do_not_retrieve_when}"""
        for position, c in enumerate(candidates, start=1)
    )
    prompt = f"""Each {item_noun} below has already been judged relevant to the participant's message. Your ONLY question, for each one independently: does its own DO-NOT-RETRIEVE-WHEN condition clearly apply to this specific turn?

Participant's message: {query}

Recent conversation context: {conversation_context}

Candidates:

{entries_block}

For EACH numbered candidate: answer SKIP only if its stated condition clearly applies to this turn; otherwise RETRIEVE. Do not re-judge relevance - that decision is already made. When unsure whether the condition applies, RETRIEVE.

Respond with exactly {len(candidates)} lines, one per candidate:
N. RETRIEVE: <brief reason>
or
N. SKIP: <brief reason>

Use the same numbering as above. Do not add commentary outside these lines."""
    response = llm.invoke(prompt)
    label = ("negative_condition_story" if item_noun == "story"
             else "negative_condition_lexicon")
    log_llm_usage(label, response, _FILTER_MODEL)
    parsed: dict[int, tuple[bool, str]] = {}
    for line in response.content.strip().split("\n"):
        match = _LINE_PATTERN.match(line)
        if not match:
            continue
        parsed[int(match.group(1))] = (
            match.group(2).upper() == "RETRIEVE",
            match.group(3).strip() or "guard evaluated",
        )
    # fail-open toward retrieval: an unparsed line means the guard was not
    # clearly shown to apply
    return [parsed.get(pos, (True, "no clear guard verdict; retrieved"))
            for pos in range(1, len(candidates) + 1)]


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
    # item_noun distinguishes which retriever called this shared helper -
    # LexiconRetriever passes "lexicon entry" (see app/rag/retriever.py),
    # StoryRetriever passes "story" (see app/rag/story_retriever.py). Used
    # only to pick the right log label; no other behavior depends on it.
    label = "retrieval_filter_story" if item_noun == "story" else "retrieval_filter_lexicon"
    log_llm_usage(label, response, _FILTER_MODEL)
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
