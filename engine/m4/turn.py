"""The real turn loop (CiC-Program-Spec.md M4): Facilitator gate ->
routing -> generation -> grounding -> turn result. Wires together pieces
already built and proven independently (M5's live gate calls/routing/
failure semantics, this module's own generation/grounding/crisis_resources)
- it does not reimplement any of them. Does not append to the M4 event log
itself (engine.m4.store/events) - that's the caller's job, so this stays
testable against a plain TurnResult rather than a database.

Scope note: only two of the routing actions get full generation content
here - voice_with_directive/voice_pass_through (the ordinary answer path)
and safety_turn for signal=ACUTE_DISTRESS (the crisis-relevant path, since
"crisis append asserted including the empty-stream case" is the literal
stage-5 gate item this module exists to prove). Track B's own safety_turn
content (HARMFUL_DYNAMIC_SIGNAL), check_in_turn, system_nature_turn,
bridge_turn, and etic_turn are real, tested routing outcomes (engine.m5.
routing) whose Facilitator-authored turn CONTENT is not yet built - same
NotImplementedError seam as engine.m3.generation.LiveModelAnswerer, not a
gap hidden by this module.

Stage 6 addition (M8): every real model call this module makes is
attributed to the caller's session_id via engine.m8.usage.record_usage and
collected on TurnResult.usage_records - never persisted here (this module
still makes no store writes of its own), just returned so the caller can
append them to an engine.m8.log_store.UsageLogStore alongside whatever it
does with the M4 event log. A call whose CallOutcome carries no raw_usage
(a failed call, or the empty-answer citations shortcut that never calls
out at all) produces no record - there is nothing to attribute, not a gap.

M4 implementation, step 5 (LIVE-GENERATION-DESIGN.md, forks signed off
§9.5, 2026-08-22): the two-call shape (a free-text stream, then a forced-
tool-use follow-up guessing which records it drew on) is retired. One
call now carries both the answer and its own grounding, via inline
[[record.id]] tags the compiled prompt's fleet preamble (§5.2) teaches
every world's voice to emit - engine.m4.generation.call_citations is
deleted, not merely unused. engine.m4.grounding (the excerpt-match badge
check against a claimed `drawn_on` list) is untouched and no longer this
module's net - that list doesn't exist anymore now that citations are
never guessed after the fact. engine.m4.grounding_net.check_turn is the
new net: per-sentence, string-only, no model call, run over the raw
tagged text before any of it is treated as this turn's answer.

Fork 1 (sentence-gated streaming) is honored in its strictest reading
here, not a looser one: no live token-by-token SSE transport exists yet
in this codebase (engine.m2.manifest's own compat note says so plainly -
"no runtime exists yet"), so stream_voice_turn already returns full text
only once the SDK call completes, never incrementally. Given that, "check
before it reaches a participant" reduces exactly to what _apply_net does
below: every sentence is verified before ANY of this turn's text is
placed on TurnResult.voice_event. When a real per-token transport is
built, sentence-gating moves into that layer; the check itself does not
change.
"""
from dataclasses import dataclass, field

from engine.m1.loader import load_fleet_records
from engine.m4 import crisis_resources, evidence, grounding_net
from engine.m4.generation import stream_voice_turn
from engine.m4.grounding import find_do_not_voice_violation
from engine.m4.world_loader import LoadedWorld
from engine.m5 import live_calls
from engine.m5.failure import CallOutcome, resolve_gate
from engine.m5.routing import Directive
from engine.m8.usage import UsageRecord, record_usage


class UnhandledRoutingAction(NotImplementedError):
    """A real, tested routing outcome with no turn content wired up yet -
    raised loudly and named, never silently passed through as if handled."""


@dataclass(frozen=True)
class TurnResult:
    routing_action: str
    routing_reason: str
    facilitator_events: list[dict] = field(default_factory=list)
    voice_event: dict | None = None
    degraded: bool = False
    usage_records: list[UsageRecord] = field(default_factory=list)


def _maybe_record_usage(outcome: CallOutcome, *, session_id: str, call_kind: str, model_id: str) -> UsageRecord | None:
    """Every real call's raw usage is parity-checked (engine.m8.parity)
    BEFORE it becomes a UsageRecord - "usage logging with correct cache
    accounting tested against raw API shapes" happens inline, on every real
    turn, not as a separate exercise run occasionally. A divergence raises
    loudly here rather than silently producing a wrong attributed number."""
    if outcome.raw_usage is None:
        return None
    from engine.m8.parity import assert_parity
    from engine.provider.bedrock import normalize_usage

    normalized = normalize_usage(outcome.raw_usage)
    assert_parity(outcome.raw_usage, normalized)
    return record_usage(usage=normalized, session_id=session_id, call_kind=call_kind, model_id=model_id)


def _build_voice_system_prompt(world: LoadedWorld, directive: Directive | None) -> str:
    parts = [world.prompt_text]
    if directive is not None:
        asks_text = "; ".join(a["text"] for a in directive.asks) if directive.asks else "(none extracted)"
        parts.append(f"\n## This turn's private directive (never shown to the participant)\nAsks, in order: {asks_text}")
        if directive.register_note:
            parts.append(f"Register note: {directive.register_note}")
        if directive.suspend_register_statement_1:
            parts.append("Register statement 1 is suspended this turn (witness-before-answer licensed).")
        if directive.ambiguity_options:
            parts.append(f"Ambiguity options to offer: {', '.join(directive.ambiguity_options)}")
    return "\n".join(parts)


def _apply_net(raw_text: str, *, repository_records: dict[str, dict], thin_topics: list[dict] | None) -> tuple[str, list[dict], dict]:
    """The deterministic net (engine.m4.grounding_net.check_turn) over one
    turn's raw tagged output: withheld sentences never reach the returned
    text at all (Fork 1 - see module docstring on what "sentence-gated"
    means against this codebase's current non-streaming transport); the
    survivors are re-joined with their tags stripped, and their own tags
    become this turn's per-sentence citations (Artifact-5's citations
    event, gaining per-sentence anchors instead of one turn-level list -
    the SSE-shaped part of step 5; no separate SSE transport exists to
    wire this into yet, so it rides on TurnResult.voice_event['citations']
    until one does). Returns (text, citations, net_result) - net_result is
    kept whole (not just substantive_survives) so a caller can audit every
    sentence's own verdict, tags, and why, same as the M7 audit input the
    design names in §6.3."""
    net_result = grounding_net.check_turn(raw_text, repository_records, thin_topics=thin_topics)
    surviving = [s for s in net_result["sentences"] if s["verdict"] == "ok"]
    text = " ".join(s["sentence"] for s in surviving)
    citations = [{"sentence": s["sentence"], "record_ids": s["tags"]} for s in surviving if s["tags"]]
    return text, citations, net_result


def _run_ordinary_voice_turn(
    *,
    voice_client,
    voice_model_id: str,
    world: LoadedWorld,
    participant_message: str,
    directive: Directive | None,
    session_id: str,
    already_told_ids: set[str] | None = None,
) -> tuple[dict, list[UsageRecord]]:
    usage_records = []
    repository_records = evidence.repository_records_by_id(world.repository)
    thin_topics = evidence.thin_topics_for(repository_records)

    # EVIDENCE ASSEMBLY (design §3, engine.m4.evidence) - deterministic,
    # no model call, rides in the per-turn user message (never the cached
    # system prefix - §3.1/§5's own cache-conscious framing). canon_question
    # records are fleet-shared, not part of any one world's hash-verified
    # package, so loaded directly the same way engine.m1.gates already
    # loads them - not yet cached the way LazyWorldLoader caches a world's
    # own package (compiled/indexes/canon-map.json exists for exactly this
    # optimization, engine.m2.builders.build_canon_map_json, but nothing
    # reads it yet - a follow-up, not a correctness gap: this derives the
    # identical corpus live, just without the compiled cache).
    canon_questions = load_fleet_records()
    turn_evidence = evidence.assemble_evidence(
        message=participant_message,
        asks=directive.asks if directive else None,
        canon_questions=canon_questions,
        coverage=world.coverage,
        repository_records=repository_records,
        thin_topics=thin_topics,
        already_told_ids=already_told_ids,
    )
    evidence_block = evidence.render_evidence_block(turn_evidence)
    user_message = f"{evidence_block}\n{participant_message}" if turn_evidence["candidates"] else participant_message

    system_prompt = _build_voice_system_prompt(world, directive)
    stream_outcome = stream_voice_turn(voice_client, voice_model_id, system_prompt=system_prompt, message=user_message)
    if stream_outcome.status != "ok":
        raise RuntimeError(f"voice generation call failed: {stream_outcome.status} {stream_outcome.value}")
    if rec := _maybe_record_usage(stream_outcome, session_id=session_id, call_kind="voice_generation", model_id=voice_model_id):
        usage_records.append(rec)

    answer_text, citations, net_result = _apply_net(stream_outcome.value.text, repository_records=repository_records, thin_topics=thin_topics)

    degraded_by_net = not net_result["substantive_survives"]
    if degraded_by_net:
        # §6.3's fallback ladder, step 2: drop-and-continue already
        # happened inside _apply_net (withheld sentences never joined the
        # text); this is step 2's own escalation - nothing substantive
        # survived at all, so the turn degrades to the honest-limit floor,
        # appended by code, never regenerated, never a human edit.
        fallback = evidence.degradation_statement(turn_evidence)
        answer_text = f"{answer_text} {fallback}".strip() if answer_text else fallback

    do_not_voice_hit = find_do_not_voice_violation(answer_text=answer_text, quotes=world.quotes["quotes"])

    voice_event = {
        "speaker": world.world_key,
        "text": answer_text,
        "citations": citations,
        "glosses": [],
        "quote_offers": [],
        "attempts_meta": {"empty_stream_retries": 0},
        "grounding": net_result,
        "do_not_voice_violation": do_not_voice_hit,
        "degraded_by_net": degraded_by_net,
    }
    return voice_event, usage_records


def run_turn(
    *,
    session_id: str,
    voice_client,
    voice_model_id: str,
    safety_client,
    safety_model_id: str,
    world: LoadedWorld,
    participant_message: str,
    pressed: dict,
    anachronistic_term_ids: set,
    force_empty_stream: bool = False,
    already_told_ids: set[str] | None = None,
) -> TurnResult:
    """force_empty_stream is a TEST/EVIDENCE HOOK ONLY - it lets the empty-
    stream crisis-append case be exercised deterministically (a real model
    returning genuinely zero tokens is a real but unforceable event) without
    touching the append logic under test at all - see
    crisis_resources.append_crisis_resources_turn, which is what actually
    decides the append and takes no client. Must never be set true outside
    a test or evidence run.

    session_id attributes every real call this turn makes (M8: "zero
    unattributed calls") - use engine.m8.usage.SYSTEM_SESSION_ID for a
    non-session evidence run, never a blank string.

    already_told_ids feeds evidence assembly's Stage E (session exclusion,
    design §3.2) - story/quote ids the M4 event log already shows this
    session as told. Optional and caller-supplied rather than derived here:
    this module makes no store reads of its own (mirrors "makes no store
    writes of its own" above) - a caller with the real event log queries it
    and passes the set in; omitting it just means Stage E is a no-op."""
    usage_records: list[UsageRecord] = []

    safety_outcome = live_calls.call_safety(safety_client, safety_model_id, message=participant_message, recent_window=[], accumulator={})
    if rec := _maybe_record_usage(safety_outcome, session_id=session_id, call_kind="safety_call", model_id=safety_model_id):
        usage_records.append(rec)
    reader_outcome = live_calls.call_reader(safety_client, safety_model_id, message=participant_message)
    if rec := _maybe_record_usage(reader_outcome, session_id=session_id, call_kind="reader_call", model_id=safety_model_id):
        usage_records.append(rec)

    gate_result = resolve_gate(safety_outcome=safety_outcome, reader_outcome=reader_outcome, pressed=pressed, anachronistic_term_ids=anachronistic_term_ids)
    action = gate_result.routing.action

    if action == "safety_turn":
        signal = safety_outcome.value["signal"]  # safety_turn only reachable when safety succeeded and fired ACUTE/HARMFUL - engine.m5.routing rule 1
        if signal != "ACUTE_DISTRESS":
            raise UnhandledRoutingAction(
                f"safety_turn for signal={signal!r} (Track B / dependency dynamics) has no turn content wired "
                "up yet - this module only proves Track A's crisis-append mechanism, the literal stage-5 gate item"
            )

        voice_event = None
        stream_text, stream_failed = None, True
        if not force_empty_stream:
            # The voice may still offer its world's empathy (Program-Spec SS8)
            # while safety governs the turn - but the crisis-resources append
            # below never depends on whether this call even produced text.
            system_prompt = _build_voice_system_prompt(world, None)
            stream_outcome = stream_voice_turn(voice_client, voice_model_id, system_prompt=system_prompt, message=participant_message)
            if rec := _maybe_record_usage(stream_outcome, session_id=session_id, call_kind="voice_generation_crisis", model_id=voice_model_id):
                usage_records.append(rec)
            if stream_outcome.status == "ok":
                # The fleet preamble's citation contract is now always in
                # the system prompt (every world, every call), so even this
                # empathy-only call may emit [[id]] tags - the net still
                # runs here, stripping tags a participant must never see
                # and withholding anything that fails to ground, exactly
                # as the ordinary path does. A turn the net empties out
                # entirely is, correctly, functionally empty for the
                # append-decision below (stream_failed stays False - the
                # call itself succeeded - but empty_stream is judged on
                # stream_text, same as always).
                repository_records = evidence.repository_records_by_id(world.repository)
                stream_text, _citations, _net_result = _apply_net(
                    stream_outcome.value.text, repository_records=repository_records, thin_topics=evidence.thin_topics_for(repository_records)
                )
                stream_failed = False
                if stream_text.strip():
                    voice_event = {"speaker": world.world_key, "text": stream_text, "citations": [], "glosses": [], "quote_offers": [], "attempts_meta": {"empty_stream_retries": 0}}

        facilitator_event = crisis_resources.append_crisis_resources_turn(signal=signal, stream_text=stream_text, stream_failed=stream_failed)
        return TurnResult(
            routing_action=action,
            routing_reason=gate_result.routing.reason,
            facilitator_events=[facilitator_event],
            voice_event=voice_event,
            degraded=gate_result.degraded,
            usage_records=usage_records,
        )

    if action in ("voice_with_directive", "voice_pass_through"):
        voice_event, voice_usage_records = _run_ordinary_voice_turn(
            voice_client=voice_client,
            voice_model_id=voice_model_id,
            world=world,
            participant_message=participant_message,
            directive=gate_result.routing.directive,
            session_id=session_id,
            already_told_ids=already_told_ids,
        )
        return TurnResult(
            routing_action=action,
            routing_reason=gate_result.routing.reason,
            voice_event=voice_event,
            degraded=gate_result.degraded,
            usage_records=usage_records + voice_usage_records,
        )

    raise UnhandledRoutingAction(f"routing action {action!r} has no generation content wired up yet - see module docstring")
