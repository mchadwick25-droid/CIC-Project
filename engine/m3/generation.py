"""The Answerer seam. M3 needs a world to answer a probe before anything can
be graded - but M4 (the real conversational runtime: gate, retrieval, one
generation call, streaming) doesn't exist until stage 5, and a real answer
would mean a real model call, which means a provider decision (spec
principle 11: model/provider switches land last and alone) nobody has made
yet - no Bedrock preflight has run (spec SS10, an explicitly listed blocked
risk). So this stage builds the harness against FixtureRecordAnswerer, a
deterministic, no-model stand-in that answers straight from a world's own
records - proving the battery/masking/grading pipeline end-to-end without
pretending a live model integration exists. LiveModelAnswerer is the named,
deliberately-unimplemented seam for when that decision is actually made.
"""
from dataclasses import dataclass

from engine.m1 import canon

_TYPE_PRIORITY = ["doctrinal_witness", "quote", "story", "term"]


@dataclass(frozen=True)
class AnswerResult:
    text: str
    citations: list[str]
    source_record_id: str | None
    source_record_type: str | None


class NoCoverageError(Exception):
    """Raised when a world has neither a demonstration, substantive record,
    nor honest_limit for a cell - a gates-green world should never hit this
    (canon-coverage, engine.m1.gates, already rules it out), so this is a
    loud failure, never a silent empty answer."""


class FixtureRecordAnswerer:
    """Answers straight from an already-loaded records dict - the caller
    owns loading (and, for the stage-4 selftest, mutating) that dict, so
    this class never reads disk itself and works identically against a
    clean or a seeded-defect copy of a world's records."""

    def __init__(self, records: dict[str, dict]):
        self.records = records

    def answer(self, cell: str) -> AnswerResult:
        # citations cover the cell's FULL answer-eligible surface (every
        # demonstration/substantive/honest_limit record tagged for this
        # cell), not just whichever one supplies the primary text - a real
        # conversation could surface any of them, and fabrication-pressure
        # probing (spec M3) is meant to test that whole surface, not one
        # cherry-picked record.
        citations = self._citation_surface(cell)

        demo = self._demonstration_for(cell)
        if demo is not None:
            return self._answer_from_demonstration(demo, citations)

        classification = canon.classify_cell(cell, self.records)
        if classification["status"] == "substantive":
            record = self._pick_substantive(classification["substantive"])
            return self._answer_from_substantive(record, citations)
        if classification["status"] == "honest_limit":
            record = self.records[classification["honest_limit"][0]]
            return AnswerResult(
                text=record["statement"],
                citations=citations,
                source_record_id=record["id"],
                source_record_type="honest_limit",
            )
        raise NoCoverageError(f"cell {cell} has no demonstration, substantive record, or honest_limit")

    def _citation_surface(self, cell: str) -> list[str]:
        eligible_types = {"demonstration", "honest_limit", *canon.substantive_types()}
        source_ids = set()
        for record in self.records.values():
            if record.get("record_type") in eligible_types and cell in (record.get("canon_cells") or []):
                source_ids.update(s["source_id"] for s in record.get("sources") or [])
        return sorted(source_ids)

    def _demonstration_for(self, cell: str) -> dict | None:
        demos = [
            r
            for r in self.records.values()
            if r.get("record_type") == "demonstration" and cell in (r.get("canon_cells") or [])
        ]
        return sorted(demos, key=lambda r: r["id"])[0] if demos else None

    def _answer_from_demonstration(self, demo: dict, citations: list[str]) -> AnswerResult:
        exchange = demo.get("exchange") or []
        rep_turns = [turn for turn in exchange if turn.get("speaker") == "representative"]
        text = rep_turns[-1]["text"] if rep_turns else ""
        return AnswerResult(
            text=text,
            citations=citations,
            source_record_id=demo["id"],
            source_record_type="demonstration",
        )

    def _pick_substantive(self, ids: list[str]) -> dict:
        by_type = {self.records[rid]["record_type"]: rid for rid in ids}
        for record_type in _TYPE_PRIORITY:
            if record_type in by_type:
                return self.records[by_type[record_type]]
        return self.records[sorted(ids)[0]]

    def _answer_from_substantive(self, record: dict, citations: list[str]) -> AnswerResult:
        record_type = record["record_type"]
        text = {
            "doctrinal_witness": record.get("text", ""),
            "quote": record.get("text", ""),
            "story": " ".join(filter(None, [record.get("tellable_as"), record.get("text")])),
            "term": " ".join(filter(None, [record.get("plain_meaning"), record.get("quick_meaning")])),
        }.get(record_type, "")
        return AnswerResult(
            text=text,
            citations=citations,
            source_record_id=record["id"],
            source_record_type=record_type,
        )


class LiveModelAnswerer:
    """The real seam, deliberately unimplemented. Wiring this up means
    choosing and configuring a model provider (spec principle 11: lands
    last and alone) and accepting real per-call cost (spec principle 13:
    cost discipline, attributed per session) - both outside this build
    thread's DECIDABLE authority (Build-Blueprint.md SS4: spending beyond
    the budget envelope is Mark's call). Raising here, rather than quietly
    falling back to the mock, is the point: nothing should ever mistake a
    mock admission run for a real one."""

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "LiveModelAnswerer is not wired up: no model provider is configured for this build "
            "(Bedrock preflight is blocked on the live AWS account, spec SS10). Configuring one is "
            "a stop-and-ask - a provider/spend decision, not a DECIDABLE implementation choice."
        )
