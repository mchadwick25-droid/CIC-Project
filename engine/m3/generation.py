"""The Answerer seam. Two answerers share one interface,
answer(cell, probe_text) -> AnswerResult.

FixtureRecordAnswerer answers straight from a world's own records with no
model call, and proves the battery, masking and grading pipeline end to end.

LiveModelAnswerer answers a sealed probe through engine.m4.turn.run_turn,
the call the conversation path makes: the gate (safety and reader), routing,
the per-turn directive, evidence assembly, the voice call, the repeat-recital
retry, self-revision where the deployment runs it, the net, and the settled
reply. Construction makes no call; only .answer() does, so only a caller
holding an approved live test spends anything.
"""
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml

from engine.m1 import canon
from engine.m1.loader import load_fleet_records
from engine.m4 import evidence as m4_evidence
from engine.m4.facilitator_turns import voice_rejected_turn
from engine.m4.rhythm import tally_from_transcript
from engine.m4.turn import SESSION_TURN_CAP, UnhandledRoutingAction, run_turn
from engine.m4.uncited_claims import (
    conversation_revealed_excerpts,
    known_tradition_names,
    match_named_tradition,
    tradition_known_in_window,
    world_records_mention_tradition,
)
from engine.m4.world_loader import LoadedWorld
from engine.m5.anachronism import anachronistic_term_ids
from engine.m3.call_capture import CapturingClient
from engine.provider.guard import LiveTestCapReached, LiveTestGuardError

REPO_ROOT = Path(__file__).resolve().parents[2]
RENDER_YAML = REPO_ROOT / "render.yaml"
PRODUCTION_SERVICE = "cic-engine"
GATE_FAILED_ROUTE = "safety_unread_turn"

# A participant whose message fails to produce a reply sends it again; a
# probe is given the same one resend.
RESENDS = 1

_TYPE_PRIORITY = ["doctrinal_witness", "quote", "story", "term"]


@dataclass(frozen=True)
class AnswerResult:
    text: str
    citations: list[str]
    source_record_id: str | None
    source_record_type: str | None
    # Per-sentence {sentence, record_ids} entries from the net - the
    # live path carries them so grading can tell a MISCOPIED ADDRESS on a
    # verifiable sentence from a fabrication. Fixture answers leave this None.
    citation_entries: list[dict] | None = None
    live_turn: "LiveTurn | None" = None


@dataclass(frozen=True)
class LiveTurn:
    """Everything one live-path probe produced: the route and the reader's
    reading, the draft the voice wrote on each call, the voice event the
    reply was built from, what each call cost, and how many sends it took."""
    routing_action: str
    routing_reason: str
    gate: dict
    voice_event: dict | None
    facilitator_events: list[dict]
    voice_calls: list[dict]
    usage: list[dict]
    sends: int


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




class AnswerUnavailable(Exception):
    """The live path produced no reply for a probe after its resend."""


@dataclass(frozen=True)
class LivePathSettings:
    """The deployment's own settings: the exact model ids and the three
    flags that change what a turn does."""
    voice_model_id: str
    safety_model_id: str
    r27_enforce: bool
    self_revision_enabled: bool
    citation_attach_enabled: bool
    streaming_enabled: bool = False

    def printable(self) -> dict:
        return asdict(self)


def production_settings(render_yaml: Path = RENDER_YAML) -> dict:
    """The pinned model patterns and flags of the production service,
    read from the deployment file, with the engine's own defaults for any
    flag the file leaves unset."""
    services = yaml.safe_load(render_yaml.read_text(encoding="utf-8"))["services"]
    env = {e["key"]: e.get("value") for s in services if s["name"] == PRODUCTION_SERVICE for e in s.get("envVars", [])}
    on = ("1", "true", "yes")
    return {
        "voice_model_pattern": env["CIC_API_VOICE_MODEL_PATTERN"],
        "safety_model_pattern": env["CIC_API_SAFETY_MODEL_PATTERN"],
        "r27_enforce": (env.get("CIC_R27_ENFORCE") or "") in on,
        "self_revision_enabled": (env.get("CIC_SELF_REVISION") or "1") not in ("0", "false", "no"),
        "citation_attach_enabled": (env.get("CIC_CITATION_ATTACH") or "") in on,
        "streaming_enabled": (env.get("CIC_API_STREAMING") or "") in on,
    }


class LiveModelAnswerer:
    """Answers each sealed probe as the first message of a fresh interview
    session: engine.m4.turn.run_turn, with the inputs the conversation path
    derives for a first message. `client` serves both the voice and the gate
    calls and is wrapped to keep the raw drafts."""

    def __init__(self, *, world: LoadedWorld, registry: dict, client, settings: LivePathSettings):
        self.world = world
        self.registry = registry
        self.client = CapturingClient(client)
        self.settings = settings
        self.session_id = f"admission-{world.world_key}"
        self.term_ids = anachronistic_term_ids(load_fleet_records(), world.frame["time_window"])
        self.repository_records = m4_evidence.repository_records_by_id(world.repository)
        self.tradition_names = known_tradition_names(registry, exclude_world_key=world.world_key) if settings.r27_enforce else None
        self.turns: list[LiveTurn] = []

    def _turn_inputs(self, probe_text: str) -> dict:
        named = match_named_tradition(probe_text, self.registry, exclude_world_key=self.world.world_key)
        return {
            "other_tradition_evidence_ids": (
                world_records_mention_tradition(self.repository_records, self.registry[named]) if named else None
            ),
            "other_tradition_known_in_window": (
                tradition_known_in_window(self.registry[self.world.world_key], self.registry[named]) if named else None
            ),
            "other_tradition_revealed": (
                conversation_revealed_excerpts([], self.registry[named], speaking_world_key=self.world.world_key) if named else None
            ),
        }

    def _send(self, probe_text: str):
        return run_turn(
            session_id=self.session_id,
            voice_client=self.client,
            voice_model_id=self.settings.voice_model_id,
            safety_client=self.client,
            safety_model_id=self.settings.safety_model_id,
            world=self.world,
            participant_message=probe_text,
            pressed={"later_age": False, "other_tradition": False},
            anachronistic_term_ids=self.term_ids,
            track_b_accumulator=None,
            track_a_last=None,
            check_ins_shown=frozenset(),
            already_told_ids=set(),
            already_bridged_figure_ids=set(),
            already_bridged_gloss_ids=set(),
            history=[],
            previous_kind=None,
            rhythm=tally_from_transcript([]),
            r27_enforce=self.settings.r27_enforce,
            known_tradition_names=self.tradition_names,
            self_revision_enabled=self.settings.self_revision_enabled,
            turn_cap=SESSION_TURN_CAP,
            limit_text=None,
            citation_attach_enabled=self.settings.citation_attach_enabled,
            on_sentence=(lambda _event: None) if self.settings.streaming_enabled else None,
            **self._turn_inputs(probe_text),
        )

    def answer(self, cell: str, probe_text: str) -> AnswerResult:
        last_error: Exception | None = None
        for sends in range(1, RESENDS + 2):
            mark = self.client.mark()
            try:
                result = self._send(probe_text)
            except (LiveTestCapReached, LiveTestGuardError, UnhandledRoutingAction):
                raise
            except RuntimeError as error:  # the voice call failed: the participant sends again
                last_error = error
                continue
            if result.routing_action == GATE_FAILED_ROUTE:
                last_error = RuntimeError(f"gate call failed: {result.routing_reason}")
                continue
            break
        else:
            raise AnswerUnavailable(f"{type(last_error).__name__}: {last_error}") from last_error

        voice_event = result.voice_event
        if voice_event is not None and voice_event.get("r27_enforcement_exhausted"):
            text = voice_rejected_turn(self.world.frame["representative"]["name"])["text"]
            citation_entries = []
        elif voice_event is not None:
            text = voice_event["text"]
            citation_entries = [{"sentence": c["sentence"], "record_ids": list(c["record_ids"])} for c in voice_event["citations"]]
        else:
            text = "\n\n".join(event["text"] for event in result.facilitator_events)
            citation_entries = []
        citations = sorted({rid for entry in citation_entries for rid in entry["record_ids"]})
        primary = self.repository_records.get(citations[0]) if citations else None
        turn = LiveTurn(
            routing_action=result.routing_action,
            routing_reason=result.routing_reason,
            gate=result.gate,
            voice_event=voice_event,
            facilitator_events=result.facilitator_events,
            voice_calls=self.client.since(mark),
            usage=[
                {"call_kind": r.call_kind, "model_id": r.model_id, **asdict(r.usage)} for r in result.usage_records
            ],
            sends=sends,
        )
        self.turns.append(turn)
        return AnswerResult(
            text=text,
            citations=citations,
            source_record_id=citations[0] if citations else None,
            source_record_type=primary.get("record_type") if primary else None,
            citation_entries=citation_entries,
            live_turn=turn,
        )
