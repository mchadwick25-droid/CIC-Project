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
from engine.m4 import crisis_resources, evidence, facilitator_turns, grounding_net
from engine.m4.generation import stream_voice_turn
from engine.m4.grounding import find_do_not_voice_violation
from engine.m4.world_loader import LoadedWorld
from engine.m5 import live_calls
from engine.m5.anachronism import resolve_term_ids, terms_in_message
from engine.m5.failure import CallOutcome, resolve_gate
from engine.m5.routing import Directive, directive_without_terms
from engine.m8.usage import UsageRecord, record_usage


class UnhandledRoutingAction(NotImplementedError):
    """A real, tested routing outcome with no turn content wired up yet -
    raised loudly and named, never silently passed through as if handled."""


@dataclass(frozen=True)
class TurnResult:
    routing_action: str
    routing_reason: str
    # This turn's gate_decision payload, whole (engine.m4.events' own
    # required key set). The caller writes it to the event log verbatim -
    # it does not rebuild one, and until this field existed it could not:
    # every gate_decision this build ever wrote had asks, register,
    # out_of_scope, modern_terms, safety and directive all blank, because
    # the only thing that ever reached the caller was the route. The whole
    # audit surface Artifact-5 SS5 and the M7 audit read from was empty.
    #
    # Assembled here rather than in the caller because this is where the
    # two gate outcomes actually are, and it is deliberately the RESOLVED
    # modern_terms that go in: reader_term_id and source: message_scan on
    # each entry are how an auditor sees which path found a term and what
    # the model called it first.
    gate: dict = field(default_factory=dict)
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


def _directive_payload(directive: Directive | None) -> dict | None:
    return None if directive is None else {
        "asks": list(directive.asks),
        "register_note": directive.register_note,
        "suspend_register_statement_1": directive.suspend_register_statement_1,
        "ambiguity_options": list(directive.ambiguity_options),
    }


def _gate_decision_payload(*, safety_outcome: CallOutcome, reader_outcome: CallOutcome, gate_result) -> dict:
    """One turn's gate_decision event payload, built from the two gate
    outcomes rather than from the route alone.

    Every key engine.m4.events requires is filled from what the gate
    actually produced. A failed call contributes None (or an empty list
    where the key is a list) - which is a real, readable statement that the
    call did not return, not the same thing as the blank payload this
    replaces, where a successful gate and a failed one logged identically.
    """
    reader = None if reader_outcome.failed else reader_outcome.value
    directive = gate_result.routing.directive
    return {
        "asks": list(reader.get("asks") or []) if reader else [],
        "register": reader.get("register") if reader else None,
        "out_of_scope": reader.get("out_of_scope") if reader else None,
        "modern_terms": list(reader.get("modern_terms") or []) if reader else [],
        "safety": None if safety_outcome.failed else safety_outcome.value,
        "route": gate_result.routing.action,
        "directive": _directive_payload(directive),
        "degraded": gate_result.degraded,
    }


def _build_turn_directive(directive: Directive | None) -> str | None:
    """The per-turn half of the voice's system prompt, on its own - the
    world's compiled prompt is passed separately and unmodified, so that it
    stays byte-identical across a session and the cache prefix actually
    holds (see stream_voice_turn's docstring). This text changes every
    turn, so it must never be concatenated onto the cached half.

    Returns None when there is no directive (the crisis path), which leaves
    the call with the world prompt alone - exactly what it sent before."""
    if directive is None:
        return None
    asks_text = "; ".join(a["text"] for a in directive.asks) if directive.asks else "(none extracted)"
    # The leading newline is kept from when this text was concatenated onto
    # the world prompt: system blocks are joined with no separator of their
    # own, so dropping it would run the heading onto the prompt's last line.
    # The model must see exactly the bytes it saw before this split.
    parts = [f"\n## This turn's private directive (never shown to the participant)\nAsks, in order: {asks_text}"]
    if directive.register_note:
        parts.append(f"Register note: {directive.register_note}")
    if directive.suspend_register_statement_1:
        parts.append("Register statement 1 is suspended this turn (witness-before-answer licensed).")
    if directive.ambiguity_options:
        # NOT "options to offer". That wording instructed the voice to
        # present a menu, and it sits after register statement 1 in the
        # prompt, so it won: measured over five questions the first
        # sentence answered the ask on 2 of 5 turns, and the participant
        # was handed "I hear two ways to take your question" instead of an
        # answer. Removing the instruction entirely took that to 5 of 5.
        # This keeps the reading available to the voice as information and
        # restates statement 1 rather than overriding it.
        parts.append(
            f"The ask could be read these ways: {'; '.join(directive.ambiguity_options)}. "
            "Answer the most likely reading first, in your opening sentence; then, only if the others "
            "would change the answer, say briefly what they would change. Never open by listing the readings."
        )
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
    # THE CHECKS GATE DECORATION, NEVER THE TEXT. Program-Spec M4, and
    # again in Artifact-5 SS2 ("they gate decoration, not text"), and again
    # in SS5 ("never by editing a live response"). What the voice wrote is
    # what the participant reads; only the tags come off.
    #
    # Deleting the failures was measured over 17 live turns: 25% of every
    # sentence generated, 39% of them on prose that invented nothing, and
    # the deletion orphaned whatever came next - a question about who
    # someone was, answered without naming anyone, because the naming
    # sentence went. A sentence that fails verification loses its citation
    # and is carried on the event for the SS5 audit; it is not destroyed on
    # the way to the screen.
    text = grounding_net.strip_tags(raw_text)
    citations = [
        {"sentence": s["sentence"], "record_ids": s["tags"]}
        for s in net_result["sentences"]
        if s["verdict"] == "ok" and s["tags"]
    ]
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
    history: list[dict] | None = None,
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

    stream_outcome = stream_voice_turn(
        voice_client, voice_model_id, system_prompt=world.prompt_text,
        turn_directive=_build_turn_directive(directive), message=user_message, history=history,
    )
    if stream_outcome.status != "ok":
        raise RuntimeError(f"voice generation call failed: {stream_outcome.status} {stream_outcome.value}")
    if rec := _maybe_record_usage(stream_outcome, session_id=session_id, call_kind="voice_generation", model_id=voice_model_id):
        usage_records.append(rec)

    answer_text, citations, net_result = _apply_net(stream_outcome.value.text, repository_records=repository_records, thin_topics=thin_topics)

    # No code-appended floor line. Program-Spec M5: "In-world thinness is
    # never intercepted - the honest limit is the voice's own testimony,
    # not a system apology." It fired on 7 of the turns measured today and
    # on every one of the seven it landed after real surviving content,
    # telling the participant there was nothing to say directly underneath
    # the thing that had just been said. The honest limit is the voice's
    # job, and the limit records are in its ground to say it from.
    degraded_by_net = not net_result["substantive_survives"]

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
        # The finished string, checked last, after the net has cut and the
        # fallback has appended - because that is the only text a person
        # actually reads, and until now nothing looked at it.
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
    history: list[dict] | None = None,
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

    # WHICH MODERN TERMS ARE IN PLAY, settled here once, before anything
    # downstream reads them - so routing's intersection and the bridge's
    # re-derivation below see the same list instead of each deriving one.
    # Two passes, and the second is not a belt-and-braces duplicate of the
    # first; they fix different failures, both measured live on 2026-08-24:
    #
    #   resolve_term_ids  - the reader is INSTRUCTED to invent its term_id
    #     (engine.m5.live_calls' own prompt), and routing matches those
    #     against fleet record ids. The intersection was empty every time.
    #   terms_in_message  - the reader flagged "Trinity" on two attempts at
    #     the same question and returned modern_terms: [] on a third. An id
    #     fix cannot help a flag that never came. Whether the participant
    #     used the word is not a judgement call, so it is not left to one.
    #
    # The reader's own reading is kept, not replaced: it can flag terms the
    # fleet carries no record for (those keep its id and never intersect),
    # and it reads framings a word list cannot see.
    if reader_outcome.value is not None:
        fleet_records = load_fleet_records()
        resolved = resolve_term_ids(reader_outcome.value.get("modern_terms"), fleet_records)
        resolved += terms_in_message(
            participant_message, fleet_records, already_found={t["term_id"] for t in resolved}
        )
        reader_outcome.value["modern_terms"] = resolved

    gate_result = resolve_gate(safety_outcome=safety_outcome, reader_outcome=reader_outcome, pressed=pressed, anachronistic_term_ids=anachronistic_term_ids)
    action = gate_result.routing.action
    gate = _gate_decision_payload(
        safety_outcome=safety_outcome, reader_outcome=reader_outcome, gate_result=gate_result
    )

    if action == "safety_turn":
        signal = safety_outcome.value["signal"]  # safety_turn only reachable when safety succeeded and fired ACUTE/HARMFUL - engine.m5.routing rule 1
        if signal != "ACUTE_DISTRESS":
            # Track B: a dependency dynamic, not a crisis. No resources
            # (crisis_resources.resources_for_signal already refuses them for
            # this signal) and no session freeze - Program-Spec SS8 asks for
            # "an explicit continue path back to the voice after non-acute
            # signals", so the voice is not silenced and the message is not
            # withheld from it.
            voice_event, voice_usage_records = _run_ordinary_voice_turn(
                voice_client=voice_client, voice_model_id=voice_model_id, world=world,
                participant_message=participant_message, directive=gate_result.routing.directive,
                session_id=session_id, already_told_ids=already_told_ids, history=history,
            )
            return TurnResult(
                routing_action=action, routing_reason=gate_result.routing.reason,
                gate=gate,
                facilitator_events=[facilitator_turns.dependency_check_turn()],
                voice_event=voice_event, degraded=gate_result.degraded,
                usage_records=usage_records + voice_usage_records,
            )

        voice_event = None
        stream_text, stream_failed = None, True
        if not force_empty_stream:
            # The voice may still offer its world's empathy (Program-Spec SS8)
            # while safety governs the turn - but the crisis-resources append
            # below never depends on whether this call even produced text.
            stream_outcome = stream_voice_turn(voice_client, voice_model_id, system_prompt=world.prompt_text, message=participant_message)
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
            gate=gate,
            routing_reason=gate_result.routing.reason,
            facilitator_events=[facilitator_event],
            voice_event=voice_event,
            degraded=gate_result.degraded,
            usage_records=usage_records,
        )

    if action == "check_in_turn":
        # Softer than the safety turn and deliberately not an answer: the
        # safety call was uncertain, so the message is not passed to the
        # voice this turn (Artifact-4 SS3 rule 2 ranks this above ordinary
        # routing precisely so a possible disclosure is never answered as if
        # it were an ordinary question).
        return TurnResult(
            routing_action=action, routing_reason=gate_result.routing.reason,
            gate=gate,
            facilitator_events=[facilitator_turns.check_in_turn()],
            degraded=gate_result.degraded, usage_records=usage_records,
        )

    if action == "system_nature_turn":
        # "immediately" (Artifact-4 SS3 rule 3) means the voice is not asked
        # anything - a question about what the system IS is not a question
        # any world can answer, and letting a world try is the failure this
        # route exists to prevent.
        return TurnResult(
            routing_action=action, routing_reason=gate_result.routing.reason,
            gate=gate,
            facilitator_events=[facilitator_turns.system_nature_turn()],
            degraded=gate_result.degraded, usage_records=usage_records,
        )

    if action == "etic_turn":
        return TurnResult(
            routing_action=action, routing_reason=gate_result.routing.reason,
            gate=gate,
            facilitator_events=[facilitator_turns.etic_turn(reader_outcome.value["out_of_scope"]["class"])],
            degraded=gate_result.degraded, usage_records=usage_records,
        )

    if action == "bridge_turn":
        # The Facilitator speaks the modern sense; the voice answers the
        # term-free underlying subject and never sees the participant's
        # modern word (Program-Spec SS77). The fired terms are recomputed
        # here from what the reader and the registry already produced -
        # routing carries the decision, not the payload.
        fleet = load_fleet_records()
        fired = [
            fleet[t["term_id"]]
            for t in (reader_outcome.value.get("modern_terms") or [])
            if t["term_id"] in anachronistic_term_ids and t["term_id"] in fleet
        ]
        facilitator_event, underlying_subject = facilitator_turns.bridge_turn(fired)
        # WHAT ELSE THE PARTICIPANT ASKED. The bridge route carries no
        # directive of its own (engine.m5.routing), so a message that asked
        # two things - one carrying the modern word, one not - used to reach
        # the voice as the underlying subject alone, and the second ask was
        # simply gone. Barring the word is the rule; barring the rest of the
        # sentence was never part of it. The fired records' own display_terms
        # are what gets barred, all of them, not just the spelling that
        # happened to match - so an ask carrying a different inflection of
        # the same term is still kept away from the voice.
        barred = [term for record in fired for term in (record.get("display_terms") or [])]
        bridge_directive = directive_without_terms(reader_outcome.value, barred)
        # The event log said directive: None for this route because that was
        # true when the payload was assembled. It is not true any more, and
        # a record that disagrees with what the voice was handed is the exact
        # failure the gate_decision fix existed to end.
        gate["directive"] = _directive_payload(bridge_directive)
        voice_event, voice_usage_records = _run_ordinary_voice_turn(
            voice_client=voice_client, voice_model_id=voice_model_id, world=world,
            participant_message=underlying_subject, directive=bridge_directive,
            session_id=session_id, already_told_ids=already_told_ids, history=history,
        )
        return TurnResult(
            routing_action=action, routing_reason=gate_result.routing.reason,
            gate=gate,
            facilitator_events=[facilitator_event], voice_event=voice_event,
            degraded=gate_result.degraded, usage_records=usage_records + voice_usage_records,
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
            history=history,
        )
        return TurnResult(
            routing_action=action,
            gate=gate,
            routing_reason=gate_result.routing.reason,
            voice_event=voice_event,
            degraded=gate_result.degraded,
            usage_records=usage_records + voice_usage_records,
        )

    raise UnhandledRoutingAction(f"routing action {action!r} has no generation content wired up yet - see module docstring")
