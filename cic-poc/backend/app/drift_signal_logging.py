"""Lightweight, purely-additive logging for _detect_drift_signal's own
outcome (app/graph/nodes.py) - the per-signal breakdown Design §3/Blueprint
0.4 names as drift_detection's real gap.

One call per turn already covers eleven signal types (ten in
FACILITATOR_MONITORING_PROMPT's "Primary Drift Signals" list plus the
separately-screened OVER_SETTLING), which is the cheap shape and stays
unchanged. What no committed artifact has ever recorded is *which* signal
actually fired, on ordinary traffic, with what severity, per world - so a
Voice Rebuild checkpoint asking "did FLATTENING become more common on the
rebuilt worlds" or "what's declining_initiative's real firing rate" has
had no denominator to work from. This module makes both countable without
changing what fires or how any existing caller behaves.

Mirrors app/over_settling_logging.py and app/length_ceiling_logging.py
exactly: a dedicated named logger with its own handler (the app has no
logging.basicConfig anywhere, so the root logger's default WARNING level
would otherwise swallow every INFO line), emitting a structured line that
scripts/cost_baseline_runner.py-style parsing can pick up with a regex the
same way it already parses [llm_usage] lines. Deliberately NOT threaded
through the session event-sourcing model (app/graph/events.py): the
question this answers is a fleet-wide aggregate over ordinary traffic, not
a per-session fact a participant or reviewer needs in one conversation's
audit trail - state.drift_signals already carries the per-session record.

Observation only: never raises past its own log call, and does not change
which signal is detected, its severity, or any existing code path's
output.
"""
import logging

logger = logging.getLogger("cic.drift_signal")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    logger.addHandler(_handler)


def log_drift_signal_outcome(
    world_id: str | None,
    signal_type: str | None,
    severity: str | None,
) -> None:
    """
    Log one _detect_drift_signal() call's outcome.

    world_id: the world the turn belongs to, or None (untagged callers -
        see _detect_drift_signal's own docstring for who calls with which).
    signal_type: the fired signal's name (one of the eleven - ten from
        FACILITATOR_MONITORING_PROMPT plus "over_settling"), or None if
        the turn was clean. Logging the clean case too, not just fires,
        is what gives a firing rate a real denominator - the same reason
        length_ceiling_logging logs OUTCOME_UNDER alongside the two firing
        outcomes rather than only the interesting cases.
    severity: "low" | "medium" | "high" when signal_type is set; None when
        clean.
    """
    try:
        logger.info(
            "[drift_signal] world_id=%s signal_type=%s severity=%s",
            world_id, signal_type or "none", severity or "none",
        )
    except Exception:
        pass
