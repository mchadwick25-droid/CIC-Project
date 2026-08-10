"""Structured logging for the pre-emission fabrication gate in
stream_representative_turn (app/graph/nodes.py).

Why this exists
---------------
The gate runs the existing screen + adjudicator on a buffered draft
BEFORE it is spoken, and regenerates once when a flag survives
adjudication. It exists because of one ruled failure class (Mark,
2026-08-10, on the T2 blind-read watchlist): the invented vignette -
particular people, relationships or events narrated as communal memory
with nothing in the world's record behind them.

Two facts about it were unrecoverable from the cell-6 verification run
without hand-forensics, and both are the kind that decide whether the
gate is worth its cost:

  1. **How often does it fire, and does the regeneration clear?** The
     gate's own screen calls `check_drift_for_message`, which logs the
     same `[drift_signal]` line the post-round watch logs. In cell 6
     the two were indistinguishable in the log: six fabrication lines,
     five gate regenerations, and telling which sixth line belonged to
     which mechanism needed line-position reconstruction against the
     round markers. A gate that cannot report its own fire rate cannot
     be tuned or retired on evidence.

  2. **What was actually flagged?** The drift record carries
     signal_type and severity but neither the offending text nor a turn
     reference - the instrument gap first recorded at Albina's
     checkpoint (2026-08-09) and hit twice more since, most recently
     when ruling this very watchlist (the side-by-side pack had to
     reconstruct each flag's round from log ordering). Blueprint B6
     fixes that gap at its source in the drift record; this module
     closes it for the gate's own path now, by carrying a head of the
     flagged draft on the line itself.

Mirrors app/length_ceiling_logging.py and app/usage_logging.py exactly:
a dedicated named logger with its own handler (the app has no
logging.basicConfig anywhere, so the root logger's default WARNING
level would otherwise swallow every INFO line), emitting one
structured, regex-parseable line per gate decision.

Observation only: never raises past its own log call, and does not
change the gate's behaviour, the prompts, the model choice, or which
draft reaches the participant.
"""
import logging

logger = logging.getLogger("cic.fabrication_gate")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    logger.addHandler(_handler)

# The four mutually exclusive outcomes of one gated representative turn.
# Named here rather than passed as free strings so a reporter and this
# module cannot drift apart silently.
OUTCOME_CLEAN = "clean"                  # screen/adjudicator raised nothing - draft spoken as drafted
OUTCOME_REGENERATED = "regenerated"      # flag survived adjudication, regeneration replaced the draft
OUTCOME_REGEN_EMPTY = "regen_empty"      # flag survived, regeneration came back empty - first draft stands
OUTCOME_CHECK_FAILED = "check_failed"    # the check itself errored - fail-open, draft stands

# How much of a flagged draft rides on the log line. Long enough to
# identify the turn and see the invented particulars that earned the
# flag; short enough that a log line stays a log line. The full text is
# always in the run artifact and the transcript.
FLAGGED_HEAD_CHARS = 240


def log_fabrication_gate_outcome(
    world_id: str | None,
    outcome: str,
    *,
    severity: str | None = None,
    first_draft_words: int | None = None,
    regenerated_words: int | None = None,
    flagged_head: str | None = None,
    request_id: str | None = None,
    session_id: str | None = None,
) -> None:
    """
    Log one gated representative turn's fabrication outcome.

    world_id: the world whose record the draft was judged against.
    outcome: one of the four OUTCOME_* constants above. The clean case is
        logged too, deliberately - a fire rate needs a denominator, and
        cell 6's did not have one.
    severity: the surviving signal's severity ("medium" = adjudicated
        extrinsic, "high" = intrinsic), or None when nothing was raised.
        The two are different findings: extrinsic is provisional by the
        adjudicator's own design (fresh retrieval may have missed the
        clearing chunk), intrinsic is settled contradiction.
    first_draft_words / regenerated_words: word counts either side of the
        regeneration. "The gate fired" and "the regeneration was
        shorter/longer" are different facts, and the second one bears on
        cost as well as on whether the corrective is understood.
    flagged_head: the first FLAGGED_HEAD_CHARS of the draft that drew the
        flag, so the finding can be ruled from the log rather than
        reconstructed by position - see this module's docstring.
    request_id / session_id: whatever identifiers already flow through the
        call site, passed through unchanged so a gate decision can be
        joined to its own [llm_usage] and [drift_signal] lines.
    """
    try:
        head = (flagged_head or "").replace("\n", " ").strip()[:FLAGGED_HEAD_CHARS]
        logger.info(
            "[fabrication_gate] world_id=%s outcome=%s severity=%s "
            "first_draft_words=%s regenerated_words=%s request_id=%s "
            "session_id=%s flagged_head=%r",
            world_id, outcome, severity if severity is not None else "None",
            first_draft_words if first_draft_words is not None else "None",
            regenerated_words if regenerated_words is not None else "None",
            request_id, session_id, head,
        )
    except Exception:
        pass
