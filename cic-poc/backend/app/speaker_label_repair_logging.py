"""Structured logging for speaker-label repair (app/speaker_label_repair.py).

The repair is deliberately silent to the participant, which is exactly why
it must not be silent to us. Two questions have to stay answerable from a
log rather than from re-reading transcripts:

  1. **Is the underlying defect getting better or worse?** The repair
     hides a Haiku failure mode (writing the public transcript's own
     format into a turn) that Sonnet does not have at all. If the rate is
     ever used to argue the models are equivalent, the argument needs the
     real number, and a repaired turn looks clean in every artifact.

  2. **How often does one voice ventriloquise another?** The truncation
     outcome is the constitutionally serious one - a Representative
     writing another world's dialogue - and its rate is a quality signal
     for the pilot watch, not a formatting statistic.

Mirrors app/length_ceiling_logging.py, app/fabrication_gate_logging.py and
app/drift_signal_logging.py: a dedicated named logger with its own handler
(the app has no logging.basicConfig, so the root logger's WARNING default
would swallow every INFO line), one structured line per repair.

PARSING NOTE, same convention as drift_signal_logging: scalars first as
strict key=value so a whitespace-splitting capture reads them unchanged.
No free text rides on this line at all - the repaired turn is already in
the transcript and the artifact.

Observation only: never raises past its own log call.
"""
import logging

logger = logging.getLogger("cic.speaker_label_repair")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    logger.addHandler(_handler)

# Only firing outcomes are logged. A clean turn is the overwhelming
# majority and needs no line: unlike the ceiling and the gate, whose fire
# RATES needed a denominator, the denominator here is simply the
# representative-turn count the run artifact already carries.
OUTCOME_LEADING_STRIPPED = "leading_label_stripped"   # cosmetic self-announcement
OUTCOME_TRUNCATED = "truncated_at_other_speaker"      # ventriloquism - the serious one


def log_speaker_label_repair(
    world_id: str | None,
    outcome: str,
    *,
    stripped_label: str | None = None,
    truncated_at: str | None = None,
    original_words: int | None = None,
    repaired_words: int | None = None,
    request_id: str | None = None,
    session_id: str | None = None,
) -> None:
    """Log one repaired turn.

    stripped_label: the display name removed from the front, if any.
    truncated_at: the OTHER representative's display name at which the
        turn was cut - present only on OUTCOME_TRUNCATED, and the field
        to watch, since it names who was being spoken for.
    original_words / repaired_words: how much of the turn was another
        voice's. A large gap means the model spent most of its turn
        writing someone else's lines.
    """
    try:
        logger.info(
            "[speaker_label_repair] world_id=%s outcome=%s stripped_label=%s "
            "truncated_at=%s original_words=%s repaired_words=%s "
            "request_id=%s session_id=%s",
            world_id, outcome, stripped_label or "None", truncated_at or "None",
            original_words if original_words is not None else "None",
            repaired_words if repaired_words is not None else "None",
            request_id, session_id,
        )
    except Exception:
        pass
