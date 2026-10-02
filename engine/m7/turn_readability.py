"""Per-turn readability hard-fail (Build/reference/method/Pass2-decisions/
VR_1A_NorthStar_Readability_Target_2026-08-09.md): any single emitted turn
above FK grade 10 or below Flesch Reading Ease 60 fails. FK below the band
floor of 8 is reported and never fails.

The numbers come from the record gate's own scorer (engine.m1.gates.
grade_text over engine.m1.fk), not from engine/m7/readability.py's
report-only instrument, so a turn and a record field are measured by the
same syllable counter against the same ceilings. A turn too short to grade
reliably is reported as unscored, by the same word floor the record gate
uses, never as passing.

`assert_turn_readable(text)` is the check for one turn.
`report_turns(turns)` grades a batch and returns every failure and every
below-floor turn without raising, for probe and live battery result checks.
"""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from engine.m1.gates import FK_CEILING, FK_FLOOR, FRE_FLOOR, grade_text


class TurnUnreadable(ValueError):
    """One emitted turn scored past FK_CEILING or under FRE_FLOOR."""


@dataclass(frozen=True)
class TurnScore:
    scored: bool
    words: int
    fk: float | None = None
    fre: float | None = None
    failures: tuple[str, ...] = field(default_factory=tuple)
    below_floor: bool = False

    @property
    def passed(self) -> bool:
        return not self.failures


def score_turn(text: str) -> TurnScore:
    text = text or ""
    graded = grade_text(text)
    words = len(text.split())
    if graded is None:
        return TurnScore(scored=False, words=words)
    fk, fre = graded["fk"], graded["fre"]
    failures = []
    if fk > FK_CEILING:
        failures.append(f"FK grade {fk:.1f}, above the ceiling of {FK_CEILING}")
    if fre < FRE_FLOOR:
        failures.append(f"FRE {fre:.1f}, below the floor of {FRE_FLOOR}")
    return TurnScore(scored=True, words=words, fk=fk, fre=fre, failures=tuple(failures), below_floor=fk < FK_FLOOR)


def assert_turn_readable(text: str) -> None:
    score = score_turn(text)
    if not score.passed:
        raise TurnUnreadable("; ".join(score.failures))


def report_turns(turns: Iterable[str]) -> dict:
    """{"turns", "scored", "unscored", "failed": [{"index", "fk", "fre",
    "reasons"}], "below_floor": [{"index", "fk"}]} - the two lists never
    overlap in meaning: `failed` is a hard fail, `below_floor` is reported
    only."""
    report = {"turns": 0, "scored": 0, "unscored": 0, "failed": [], "below_floor": []}
    for index, text in enumerate(turns):
        report["turns"] += 1
        score = score_turn(text)
        if not score.scored:
            report["unscored"] += 1
            continue
        report["scored"] += 1
        if not score.passed:
            report["failed"].append({"index": index, "fk": round(score.fk, 1), "fre": round(score.fre, 1), "reasons": list(score.failures)})
        elif score.below_floor:
            report["below_floor"].append({"index": index, "fk": round(score.fk, 1)})
    return report
