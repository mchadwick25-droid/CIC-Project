"""Lightweight, purely-additive logging for the OVER_SETTLING screen -> adjudication
yield (task: instrument over_settling_adjudication's confirm rate on ordinary traffic).

The two-stage design (_screen_over_settling, _adjudicate_over_settling in
app/graph/nodes.py) is deliberately tuned to over-flag at the screen - the
prompt tells it to flag when unsure, because every flag is handed to a
source-fed second pass that can clear it, and only a miss is unrecoverable.
That design choice is proven sound on seeded/blind-graded test batteries
(old-tree Ministry Technology/Pass2/batteries/S4.3_adjudicator_battery.md), but
nobody has ever measured what fraction of the screen's real-traffic flags
the adjudicator actually confirms - the yield on ordinary conversation, not
seeded defects. That's the one number needed before the screen's
sensitivity could be tuned at all (tightening it trades directly against
Article 5 rigor, since the design's whole logic is "only a miss is
unrecoverable" - not a decision to make on a guess).

Mirrors app/usage_logging.py's pattern exactly: a dedicated named logger
with its own handler (the app has no logging.basicConfig anywhere, so the
root logger's default WARNING level would otherwise silently swallow every
INFO line), parseable later the same way scripts/cost_baseline_runner.py
already parses [llm_usage] lines - a regex over a structured log line, not
a new database or event-store integration. Deliberately NOT threaded
through the session event-sourcing model (app/graph/events.py): the
research question this answers ("what's the confirm rate across ordinary
traffic") is a fleet-wide aggregate, not a per-session fact a participant
or reviewer needs attached to one conversation's audit trail.

Observation only: never raises past its own log call, and does not touch
prompts, model choice, or any existing code path's output.
"""
import logging

logger = logging.getLogger("cic.over_settling_decision")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    logger.addHandler(_handler)


def log_over_settling_decision(
    world_id: str | None,
    screened: bool,
    confirmed: bool | None,
) -> None:
    """
    Log one _over_settling_signal() call's outcome.

    world_id: the world the turn belongs to, or None (no sources to judge
        against - _over_settling_signal already returns None immediately
        in that case, before ever reaching the screen).
    screened: True if the first-pass screen (_screen_over_settling) flagged
        the turn at all. False means the adjudicator was never reached -
        the common case, since the screen is the cheap gate.
    confirmed: only meaningful when screened is True. True = the
        source-fed adjudicator confirmed a real missing limit (a genuine
        OVER_SETTLING signal reaches the representative). False = the
        adjudicator cleared it (screen flagged, adjudicator disagreed -
        the screen's designed-in false-positive rate doing its job).
        None = the adjudicator couldn't be reached or couldn't judge
        (infrastructure error, fails open toward NOT confirming per
        _adjudicate_over_settling's own asymmetric design) - distinguish
        this from a real "cleared" verdict rather than conflating the two,
        since an inconclusive rate that looks like a good clear rate would
        be misleading.
    """
    try:
        logger.info(
            "[over_settling_decision] world_id=%s screened=%s confirmed=%s",
            world_id, screened, confirmed,
        )
    except Exception:
        pass
