"""SH-11: structured logging for the answer bank's hit/miss decisions.

The whole premise of building this (Ministry/Technology/Pass3/cost_floor_model.py
STEP 5, preserved at commit d7c1e86 - orphaned off main by the branch-chaining
cleanup, not superseded) rests on a SERVED FRACTION estimate: ~5.2% central,
not the 30-50% first assumed, because a precomputed answer can only be served
when three things are simultaneously true - the participant chose the
question-first door, tapped a starter rather than typing freely, and stayed on
the walk without deviating. Nobody has measured the real number on live
traffic; this is what would let someone. Mirrors app/over_settling_logging.py
and app/length_ceiling_logging.py exactly: a dedicated logger with its own
handler, parseable later by scripts/cost_baseline_runner.py the same way it
already parses [llm_usage] lines.

Deliberately only logs when curriculum_ref is present at all - an ordinary
free-typed message was never a candidate for a bank hit, and logging every
such message would dilute the served-fraction measurement with traffic this
feature was never going to touch.
"""

import logging

logger = logging.getLogger("cic.answer_bank")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    logger.addHandler(_handler)


def log_answer_bank_decision(
    world_id: str | None,
    role: str | None,
    set_id: str | None,
    question_order: int | None,
    hit: bool,
    reason: str | None,
) -> None:
    """
    world_id/role/set_id/question_order: the bank key the client's
    curriculum_ref asked for - logged even on a miss, so a missing world's
    bank (not yet built) is distinguishable from a real mismatch.
    hit: True if a precomputed answer was actually served.
    reason: None on a hit; on a miss, one of "no_bank_entry" (nothing
    precomputed yet for this key), "text_mismatch" (the client's message
    didn't match the bank entry's own stored question - never served, even
    though a curriculum_ref was presented; see app/answer_bank.py on why
    this fails safe rather than trusting the ref alone), or
    "table_mode_excluded" (SH-11 v1 is interview-mode/solo only).
    """
    try:
        logger.info(
            "[answer_bank_decision] world_id=%s role=%s set_id=%s "
            "question_order=%s hit=%s reason=%s",
            world_id, role, set_id, question_order, hit, reason,
        )
    except Exception:
        pass
