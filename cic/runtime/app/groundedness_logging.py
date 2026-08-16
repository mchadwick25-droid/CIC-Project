"""Lightweight, purely-additive logging for check_quotation_grounding's own
outcome (app/graph/nodes.py) - Tier 2, Check B of the grounding gate scoped
2026-08-15 (the "What Improved" review round, which found a live-generated
turn give Papnoute an unattributed Evagrius line with no record home
anywhere in the build).

PHASE 0 (this commit): shadow mode only. This module's log lines are the
entire effect of the check - what ships to the participant is unchanged.
The question this answers, before anyone trusts the check to alter a
single turn: on real traffic, across real worlds, what is this check's
own false-positive rate? A turn tagged UNLICENSED that a human spot-review
confirms is actually a real miss is what earns Phase 1 (active
correction, scoped separately) for a given world or fleet-wide - a bar
Mark sets from this module's own numbers, not one this module assumes.

Mirrors app/drift_signal_logging.py and app/length_ceiling_logging.py
exactly: a dedicated named logger with its own handler (the app has no
logging.basicConfig anywhere, so the root logger's default WARNING level
would otherwise swallow every INFO line), a structured line
scripts/cost_baseline_runner.py-style parsing can pick up the same way it
already parses [llm_usage] lines, and named outcome constants so the
caller and this module cannot drift apart silently.

Two log calls per checked turn, not one, because a single summary line
would answer "how often does this fire" but not "on what, specifically" -
and a reviewer spot-checking false positives needs the actual span text,
not just a count:

  log_quotation_grounding_outcome  - one line per turn, always (including
      the NO_QUOTES case - the same "log the clean case too" principle
      drift_signal_logging.py already states, because a firing rate needs
      a real denominator, not just its numerator).
  log_unlicensed_quotation         - one line per UNLICENSED span, only
      when the outcome is UNLICENSED, carrying the span text itself
      (truncated) so a human reviewing the log can judge the finding
      without re-running anything.

Observation only: never raises past its own log call, and does not change
which spans are flagged, what a Representative says, or any existing code
path's output.
"""
import logging

logger = logging.getLogger("cic.groundedness")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    logger.addHandler(_handler)

# Mutually exclusive per-turn outcomes.
OUTCOME_NO_QUOTES = "no_quotes"            # nothing quotation-marked in the turn - nothing to check
OUTCOME_ALL_MATCHED = "all_matched"        # every quoted span traced to a licensed quote
OUTCOME_UNLICENSED = "unlicensed"          # at least one quoted span did not trace to any licensed quote
OUTCOME_CHECK_FAILED = "check_failed"      # the judge call itself errored or returned unparseable output - fail-open, not a finding

# Why a span went UNLICENSED - distinguished because they call for different
# next steps: NO_CANDIDATES means "author some quote records for this
# world," JUDGE_NO_MATCH means "this specific span is the actual finding."
REASON_NO_CANDIDATES = "no_licensed_quotes_for_world"
REASON_JUDGE_NO_MATCH = "judge_found_no_match"


def log_quotation_grounding_outcome(
    world_id: str | None,
    outcome: str,
    *,
    spans_checked: int = 0,
    spans_matched: int = 0,
    spans_unlicensed: int = 0,
    request_id: str | None = None,
    session_id: str | None = None,
) -> None:
    """Log one check_quotation_grounding() call's outcome, one line, every
    turn the check runs on - see module docstring for why the clean case
    (OUTCOME_NO_QUOTES) is logged too, not just findings.
    """
    try:
        logger.info(
            "[groundedness_quote] world_id=%s outcome=%s spans_checked=%d "
            "spans_matched=%d spans_unlicensed=%d request_id=%s session_id=%s",
            world_id, outcome, spans_checked, spans_matched, spans_unlicensed,
            request_id, session_id,
        )
    except Exception:
        pass


def log_unlicensed_quotation(
    world_id: str | None,
    span_text: str,
    reason: str,
    *,
    request_id: str | None = None,
    session_id: str | None = None,
) -> None:
    """Log one specific UNLICENSED span - the finding a human spot-review
    actually reads. span_text is truncated, not hashed: the whole point is
    a reviewer can judge the finding from the log line alone.
    """
    try:
        preview = span_text[:200].replace("\n", " ")
        logger.info(
            "[groundedness_quote_span] world_id=%s reason=%s request_id=%s "
            "session_id=%s span=%r",
            world_id, reason, request_id, session_id, preview,
        )
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Tier 2, Check A - figure chronology (app.graph.nodes.check_figure_chronology).
# Same two-line-per-turn discipline as Check B just above: one summary line
# every turn the check runs on (including the clean case, for a real
# denominator), one detail line per actual finding, carrying enough text
# for a human to judge it without re-running anything.
# ---------------------------------------------------------------------------

# Mutually exclusive per-turn outcomes.
OUTCOME_NO_FIGURES = "no_figures"                # nothing bridged in the turn - nothing to check
OUTCOME_NO_DATED_FIGURES = "no_dated_figures"    # figures named, but none carry an attested date in the registry
OUTCOME_ALL_CONSISTENT = "all_consistent"        # every dated figure's mentions matched its attested date
OUTCOME_CONTRADICTION = "contradiction"          # at least one dated figure's mentions contradicted its attested date


def log_named_undated_figures(
    world_id: str | None,
    figure_ids: list,
    *,
    request_id: str | None = None,
    session_id: str | None = None,
) -> None:
    """Figures a turn NAMED that carry no attested date - the backfill
    demand signal (T3-E).

    Added 2026-08-15 after finding that Phase 0 could not answer the
    question T3-E was designed around. check_figure_chronology logged
    figures_checked, which counts only the figures it COULD check; a figure
    named with no date left no trace at all, so "which undated figures do
    participants actually meet" - the whole basis for backfilling by demand
    rather than exhaustively - was unanswerable from the logs the check was
    already writing.

    One line per turn, not per figure: the ids are what a worklist needs,
    and a turn naming five undated figures is one observation of each, not
    five log lines' worth of event.
    """
    try:
        if not figure_ids:
            return
        logger.info(
            "[groundedness_figure_undated] world_id=%s count=%d request_id=%s "
            "session_id=%s figures=%s",
            world_id, len(figure_ids), request_id, session_id,
            ",".join(figure_ids),
        )
    except Exception:
        pass


def log_figure_chronology_outcome(
    world_id: str | None,
    outcome: str,
    *,
    figures_checked: int = 0,
    figures_consistent: int = 0,
    figures_contradicted: int = 0,
    figures_undated: int = 0,
    request_id: str | None = None,
    session_id: str | None = None,
) -> None:
    """Log one check_figure_chronology() call's outcome, one line, every
    turn the check runs on - see this module's docstring for why the clean
    case (OUTCOME_NO_FIGURES / OUTCOME_NO_DATED_FIGURES / OUTCOME_ALL_CONSISTENT)
    is logged too, not just findings.
    """
    try:
        logger.info(
            "[groundedness_figure] world_id=%s outcome=%s figures_checked=%d "
            "figures_consistent=%d figures_contradicted=%d figures_undated=%d "
            "request_id=%s session_id=%s",
            world_id, outcome, figures_checked, figures_consistent,
            figures_contradicted, figures_undated, request_id, session_id,
        )
    except Exception:
        pass


def log_figure_chronology_contradiction(
    world_id: str | None,
    figure_id: str,
    display_name: str,
    attested: str,
    reason: str,
    *,
    request_id: str | None = None,
    session_id: str | None = None,
) -> None:
    """Log one specific CONTRADICTION finding - the figure's attested dated
    name string (the ground truth) plus the judge's stated reason, so a
    reviewer can judge the finding from the log line alone.
    """
    try:
        preview = reason[:200].replace("\n", " ")
        logger.info(
            "[groundedness_figure_contradiction] world_id=%s figure_id=%s "
            "display_name=%s attested=%r request_id=%s session_id=%s "
            "reason=%r",
            world_id, figure_id, display_name, attested, request_id,
            session_id, preview,
        )
    except Exception:
        pass
