"""The one retained LLM call in retrieval: Do-Not-Retrieve-When guard evaluation.

Both the lexicon and story retrievers reach this module through
app/rag/pipeline.py. Relevance is NOT decided here - S3.4 (Pass 1 R6) moved
that to the local cross-encoder (app/rag/cross_encoder.py), which is
deterministic and free. What remains is one batched Haiku call per retriever
per turn, and only when a relevance-kept candidate actually carries a
genuinely evaluable guard: see evaluate_negative_conditions.

History worth knowing, because the cost baseline still shows it: until S3.4
this module also ran a batched RELEVANCE vote (evaluate_batch / _run_batch,
logged as retrieval_filter_lexicon / retrieval_filter_story) plus a
deterministic Tier-1 short-circuit that existed only to protect Tier-1 terms
from that vote's batch dilution. All three were left in the file, uncalled,
after S3.4 rewired the pipeline; they were deleted 2026-08-09. The committed
cost baseline (Pass2/baselines/cost_baseline_2026-07_raw.jsonl) predates the
rewiring, so retrieval_filter_* still appears there - 15.6% of that measured
run. Those calls have not been made by this code since S3.4. Do not read
their presence in that log as a saving still available to take.
"""

import re
from dataclasses import dataclass

from app.usage_logging import log_llm_usage

# The model both LexiconRetriever and StoryRetriever currently hardcode for
# filter_llm (see app/rag/retriever.py and app/rag/story_retriever.py) -
# kept here as its own constant purely so evaluate_negative_conditions'
# log_llm_usage() call can log the real model string without importing
# either retriever module (which would risk a circular import back into
# this one) or app.graph.nodes
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


