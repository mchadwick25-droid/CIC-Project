"""The Answerer seam. M3 needs a world to answer a probe before anything can
be graded - stage 0-4 built the harness against FixtureRecordAnswerer, a
deterministic, no-model stand-in that answers straight from a world's own
records, proving the battery/masking/grading pipeline end-to-end without
pretending a live model integration exists. LiveModelAnswerer was the
named, deliberately-unimplemented seam for when a provider decision got
made - it has been (M4/M5's own real client-based calls, M8's live-
attribution evidence run, engine/m8/reports/live-attribution-report.json),
so it's real now: this same class is the M4 build map's own M3 row
(LIVE-GENERATION-DESIGN.md §7 - "LiveModelAnswerer = this same pipeline
minus the safety gate, pointed at sealed probes - admission finally
measures the real generation path, which is the whole point of
admission"). Both classes share one interface: answer(cell, probe_text) ->
AnswerResult - probe_text was added to the seam for LiveModelAnswerer's
sake (a real answer needs the actual question); FixtureRecordAnswerer
ignores it, unchanged in every other respect.

Building LiveModelAnswerer is DECIDABLE - the same evidence-assembly +
one-tagged-generation-call + deterministic-net pipeline engine.m4.turn
already runs for a live participant, wired to a different caller and
missing only the safety/routing gate a sealed probe doesn't need. RUNNING
it against a real model is real spend and stays a stop-and-ask like any
other live-model run this project has drawn that line around (Build-
Blueprint.md SS4) - nothing in this class makes a call until a caller
who has that authorization actually invokes .answer().
"""
from dataclasses import dataclass

from engine.m1 import canon
from engine.m4 import evidence as m4_evidence
from engine.m4.generation import stream_voice_turn
from engine.m4.grounding_net import check_turn
from engine.m4.world_loader import LoadedWorld

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

    def answer(self, cell: str, probe_text: str) -> AnswerResult:
        # probe_text is unused here by design: this stand-in answers
        # straight from records, keyed only by cell - it never needed the
        # probe's actual wording, and still doesn't. Kept in the signature
        # so both Answerer implementations share one real interface (see
        # module docstring) rather than LiveModelAnswerer needing a
        # different call shape than the harness already uses.
        #
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
    """Admission's real answerer: engine.m4.turn's own evidence-assembly +
    one-tagged-generation-call + deterministic-net pipeline, pointed at a
    sealed probe instead of a live participant message, with M4's safety/
    reader/routing gate skipped outright - a sealed probe already IS the
    ask, there is no message to classify or route.

    Construction takes no client action and makes no call - only
    .answer() does, and only when a caller with real-spend authorization
    invokes it (the same discipline this project has held everywhere else
    a live model call is one function call away: crisis_resources' own
    "delivered by code" precedent, engine.m4.turn's own force_empty_stream
    test-hook warning, Build-Blueprint.md SS4's spend-authority split)."""

    def __init__(self, *, world: LoadedWorld, canon_questions: dict[str, dict], client, model_id: str):
        self.world = world
        self.canon_questions = canon_questions
        self.client = client
        self.model_id = model_id
        self.repository_records = m4_evidence.repository_records_by_id(world.repository)
        self.thin_topics = m4_evidence.thin_topics_for(self.repository_records)

    def answer(self, cell: str, probe_text: str) -> AnswerResult:
        turn_evidence = m4_evidence.assemble_evidence(
            message=probe_text,
            asks=None,
            canon_questions=self.canon_questions,
            coverage=self.world.coverage,
            repository_records=self.repository_records,
            thin_topics=self.thin_topics,
        )
        evidence_block = m4_evidence.render_evidence_block(turn_evidence)
        user_message = f"{evidence_block}\n{probe_text}" if turn_evidence["candidates"] else probe_text

        stream_outcome = stream_voice_turn(self.client, self.model_id, system_prompt=self.world.prompt_text, message=user_message)
        if stream_outcome.status != "ok":
            raise RuntimeError(f"LiveModelAnswerer: voice generation call failed: {stream_outcome.status} {stream_outcome.value}")

        net_result = check_turn(stream_outcome.value.text, self.repository_records, thin_topics=self.thin_topics)
        surviving = [s for s in net_result["sentences"] if s["verdict"] == "ok"]
        text = " ".join(s["sentence"] for s in surviving)
        citations = sorted({rid for s in surviving for rid in s["tags"]})

        if not net_result["substantive_survives"]:
            # Same Fork-2 fallback engine.m4.turn uses for a live turn - an
            # admission probe that guts is exactly the case admission
            # exists to surface, not paper over with a friendlier answer.
            fallback = m4_evidence.degradation_statement(turn_evidence)
            text = f"{text} {fallback}".strip() if text else fallback

        # source_record_id/source_record_type are metadata only - never
        # read by masking.py/grading.py (the masked transcript carries
        # `citations` alone) - so "the first cited record, if any" is a
        # defensible single "primary source" for a real answer that may
        # legitimately draw on several, not a fabricated precision the
        # deterministic FixtureRecordAnswerer's single-record answers
        # actually have.
        primary = self.repository_records.get(citations[0]) if citations else None
        return AnswerResult(
            text=text,
            citations=citations,
            source_record_id=citations[0] if citations else None,
            source_record_type=primary.get("record_type") if primary else None,
        )
