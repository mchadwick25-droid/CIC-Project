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


# How much of a flagged turn rides on the line. Long enough to identify
# the turn and see what earned the flag; short enough to stay a log line.
FLAGGED_HEAD_CHARS = 240


def log_drift_signal_outcome(
    world_id: str | None,
    signal_type: str | None,
    severity: str | None,
    *,
    description: str | None = None,
    flagged_head: str | None = None,
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
    description (T3/B6): the signal's own rationale - for an adjudicated
        fabrication this is where "Adjudication: extrinsic - <reason>"
        lives, appended by _detect_drift_signal. Newlines are flattened so
        one signal stays one line.
    flagged_head (T3/B6): the first FLAGGED_HEAD_CHARS of the turn that
        drew the signal.

    Why the last two exist. A hard-bar signal that cannot be audited from
    its own artifact has cost this project real time three times now: at
    Albina's checkpoint (2026-08-09), where locating a single fabrication
    flag meant reconstructing the drift-record index against the exchange
    list by hand and the commit recorded it as "a defect in the
    instrument, not just this run"; again when ruling the T2 blind-read
    watchlist, where every flagged turn had to be recovered by log
    POSITION against round markers; and again in cell 6, where the
    fabrication gate's own screens were indistinguishable from the
    post-round watch's. The gate's line already carries its head
    (app/fabrication_gate_logging.py); this closes the same gap on the
    watch that flags everything else.

    PARSING NOTE for harnesses: the scalar fields stay strict key=value
    and come FIRST, so the existing whitespace-splitting capture
    (scripts/voice_rebuild_research_probe.py's _TaggedLogCapture) keeps
    reading them unchanged. The two free-text fields are quoted reprs and
    come LAST; read them with a regex, not a whitespace split, which will
    otherwise stop at their first space.
    """
    try:
        desc = (description or "").replace("\n", " ").strip()
        head = (flagged_head or "").replace("\n", " ").strip()[:FLAGGED_HEAD_CHARS]
        logger.info(
            "[drift_signal] world_id=%s signal_type=%s severity=%s "
            "description=%r flagged_head=%r",
            world_id, signal_type or "none", severity or "none", desc, head,
        )
    except Exception:
        pass
