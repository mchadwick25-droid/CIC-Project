"""Lightweight, purely-additive logging for the HARD_CEILING_WORLDS
length-ceiling retry mechanism in stream_representative_turn
(app/graph/nodes.py).

Why this exists
---------------
The mechanism buffers a ceilinged world's first draft instead of streaming
it, and silently regenerates once if the draft exceeds
`ceiling * retry_trigger_multiple`. That regeneration is a second full
`main_response` call, logged by usage_logging.py under the *same* label as
the first - so a cost log records the spend but not the fact that a retry
happened, and not the word counts that decided it.

Both of the questions the project actually needs answered about this
mechanism are therefore currently unanswerable from any committed
artifact without forensics:

  1. **How often does it fire, per world?** Recovering this from the
     2026-07 B-COST raw log required reconstructing retry pairs from a
     token-arithmetic signature (the second call's input_tokens exceeds
     the first's by exactly first-call output_tokens + 51, the corrective
     message's own token cost) and attributing calls to worlds by
     matching cached-prefix sizes. That works, but it is forensics against
     a log that was never designed to answer the question, it is specific
     to the current corrective wording, and it silently measures nothing
     at all for a world that was not yet in HARD_CEILING_WORLDS when the
     log was collected.

  2. **How wide is the dead zone?** nodes.py already logs the
     over-ceiling-but-under-trigger case, deliberately, because a prior
     Opus review asked for observability into that zone *before* anyone
     touched the trigger multiple again. But it logs it with a bare
     print() to stdout, which no harness captures and no committed
     artifact records - so the zone's real frequency is still not a
     number anyone can cite.

This module makes both countable. It does not change the mechanism: the
ceilings, the trigger multiples, the corrective message, and which draft
reaches the participant are all exactly as they were.

Mirrors app/usage_logging.py and app/over_settling_logging.py: a dedicated
named logger with its own handler (the app has no logging.basicConfig
anywhere, so the root logger's default WARNING level would otherwise
swallow every INFO line), emitting a structured line that
scripts/cost_baseline_runner.py parses with a regex the same way it
already parses [llm_usage] lines. Deliberately NOT threaded through the
session event-sourcing model (app/graph/events.py): the question this
answers is a fleet-wide aggregate over ordinary traffic, not a per-session
fact a participant or reviewer needs in one conversation's audit trail.

Observation only: never raises past its own log call, and does not touch
prompts, model choice, generation, or any existing code path's output.
"""
import logging

logger = logging.getLogger("cic.length_ceiling")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    logger.addHandler(_handler)

# The three mutually exclusive outcomes of one ceilinged representative
# turn. Named here rather than passed as free strings so the reporter and
# this module cannot drift apart silently.
OUTCOME_UNDER = "under_ceiling"      # draft <= ceiling: the ceiling held on its own
OUTCOME_DEAD_ZONE = "dead_zone"      # ceiling < draft <= trigger: over, left uncorrected
OUTCOME_RETRIED = "retried"          # draft > trigger: regenerated once


def log_length_ceiling_outcome(
    world_id: str | None,
    ceiling: int,
    trigger_multiple: float,
    first_draft_words: int,
    outcome: str,
    retry_words: int | None = None,
    *,
    request_id: str | None = None,
    session_id: str | None = None,
) -> None:
    """
    Log one ceilinged representative turn's length outcome.

    world_id: the world whose Permanent Prompt states the ceiling. Only
        HARD_CEILING_WORLDS members ever reach this function - a world
        with no ceiling has no first-draft word count to report, because
        its turn streams live and is never measured.
    ceiling: the world's stated hard ceiling in words (HARD_CEILING_WORLDS).
    trigger_multiple: the world's own retry trigger multiple
        (RETRY_TRIGGER_MULTIPLES) - logged per-line rather than assumed by
        the reader, because it is per-world and has already been retuned
        once per world on measured evidence.
    first_draft_words: len(draft.split()) on the buffered first attempt.
        This is the number the whole mechanism turns on, and the one no
        committed artifact has ever recorded.
    outcome: one of OUTCOME_UNDER / OUTCOME_DEAD_ZONE / OUTCOME_RETRIED.
        All three are logged, including the ordinary under-ceiling case,
        so a fire rate has a real denominator rather than one inferred
        from a separate count of turns.
    retry_words: the regenerated answer's word count, when outcome is
        OUTCOME_RETRIED; None otherwise. Recorded because "the retry
        fired" and "the retry actually reached the ceiling" are different
        facts, and only the first is currently visible anywhere.
    request_id / session_id: whatever identifiers are already flowing
        through the call site, passed straight through unchanged, so a
        turn's ceiling outcome can be joined back to its own [llm_usage]
        lines after the fact.
    """
    try:
        logger.info(
            "[length_ceiling] world_id=%s ceiling=%s trigger_multiple=%s "
            "first_draft_words=%s outcome=%s retry_words=%s request_id=%s "
            "session_id=%s",
            world_id, ceiling, trigger_multiple, first_draft_words, outcome,
            retry_words if retry_words is not None else "None",
            request_id, session_id,
        )
    except Exception:
        pass
