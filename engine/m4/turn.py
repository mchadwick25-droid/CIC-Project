"""The real turn loop (CiC-Program-Spec.md M4): Facilitator gate ->
routing -> generation -> grounding -> turn result. Wires together pieces
already built and proven independently (M5's live gate calls/routing/
failure semantics, this module's own generation/grounding/crisis_resources)
- it does not reimplement any of them. Does not append to the M4 event log
itself (engine.m4.store/events) - that's the caller's job, so this stays
testable against a plain TurnResult rather than a database.

Scope note: all seven routing actions now have turn content. Four of them
did not until recently - check_in_turn, system_nature_turn, bridge_turn,
etic_turn and Track B's own safety_turn were real, tested routing
outcomes that raised UnhandledRoutingAction rather than answering. Two
of those four could not be reached by a live session at all; both were
proven unreachable live, then wired. What the
voice generates here is still only the ordinary answer path and the acute
safety turn; the other five are the Facilitator's own words, owned by code
in engine.m4.facilitator_turns and carrying that module's craft note.

Stage 6 addition (M8): every real model call this module makes is
attributed to the caller's session_id via engine.m8.usage.record_usage and
collected on TurnResult.usage_records - never persisted here (this module
still makes no store writes of its own), just returned so the caller can
append them to an engine.m8.log_store.UsageLogStore alongside whatever it
does with the M4 event log. A call whose CallOutcome carries no raw_usage
(a failed call, or the empty-answer citations shortcut that never calls
out at all) produces no record - there is nothing to attribute, not a gap.

M4 implementation, step 5 (LIVE-GENERATION-DESIGN.md, forks signed off
§9.5): the two-call shape (a free-text stream, then a forced-
tool-use follow-up guessing which records it drew on) is retired. One
call now carries both the answer and its own grounding, via inline
[[record.id]] tags the compiled prompt's fleet preamble (§5.2) teaches
every world's voice to emit. There is no claimed `drawn_on` list,
because citations are never guessed after the fact.
engine.m4.grounding_net.check_turn is the net: per-sentence, string-only, no model call, run over the raw
tagged text before any of it is treated as this turn's answer.

The reply a participant keeps is placed on TurnResult.voice_event only
after apply_net has checked every sentence. A caller may also ask for a
stream of the reply's sentences while it is written (on_sentence,
engine.m4.sentence_stream): each sentence carries the marks the finished
plan gives it, and the finished reply's plan is authoritative.
"""
import functools
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import Callable

from engine.m1.loader import load_fleet_records
from engine.m4 import crisis_resources, facilitator_turns, grounding_net
from engine.m4.generation import stream_voice_turn
from engine.m4 import citation_attach
from engine.m4.citation_attach import attach_citations
from engine.m4.citation_cards import resolve_citation_sources
from engine.m4.output_check import check_horizon
from engine.m4.recitation import DIRECTIVE_LINE, DemonstrationIndex
from engine.m4.seat_identity_guard import find_seat_identity_violation
from engine.m4.sentence_stream import SentenceStream
from engine.m4.self_revision import self_revise
from engine.m4.named_claim_grounding import find_named_claim_flags
from engine.m4.sentence_fact_check import find_unsupported_named_claims
from engine.m4.uncited_claims import classify_neighbour_named, find_uncited_claims, find_uncited_paragraphs
from engine.m4.name_bridge import attach_cited_sources, find_figures_used
from engine.m4.rhythm import RhythmTally
from engine.m4.term_glosses import find_glosses_used
from engine.m4.transparency_plan import build_transparency_plan
from engine.m4.turn_prep import (
    R26_HONEST_LIMIT_SENTENCE,
    _build_turn_directive,
    _other_tradition_directive,
    prepare_voice_turn_inputs,
)
from engine.m4.world_loader import LoadedWorld
from engine.m5 import live_calls
from engine.m5.anachronism import terms_in_message
from engine.m5.failure import CallOutcome, resolve_gate
from engine.m5.safety_accumulation import safety_state_events
from engine.m5.routing import Directive, directive_without_terms
from engine.m8.usage import UsageRecord, record_usage


SESSION_TURN_CAP = 10  # Build/reference/Redesign-Spec/Artifact-6-Operations.md "per-session turn cap" (was DECIDABLE, default 40) - resolved to 10 after the live memory-growth measurement (engine/m8/live_memory_growth_run.py) showed real per-turn cost climbing, not flat, as session history accumulates. Counted in completed VOICE turns (len(history)//2), the same unit that actually drives the cost growth - a session's history is built by engine.api.wiring.history_from_transcript, which only pairs a participant message with a turn that got a real Representative reply, so facilitator-only turns (safety check-ins, system-nature, etc.) do not themselves consume the cap.


class UnhandledRoutingAction(NotImplementedError):
    """An eighth routing action, added to engine.m5.routing without a branch
    here.

    Unreachable as things stand - all seven actions the router can return
    are handled below - and kept anyway, because the cost is one line and
    the failure it guards is a silent fall-through: a new route quietly
    returning a turn with no content rather than saying so. engine.api.
    wiring re-raises it past its provider-failure catch so it surfaces as
    what it is, a programming error, not a Bedrock outage."""


@dataclass(frozen=True)
class GateRun:
    """One participant message's gate pass, whole - the two sealed-tier
    calls, the resolved routing, the event payloads they produce, and the
    usage they cost. Extracted from run_turn (Artifact-7) so a table round
    can gate ONCE per participant message and then run several
    voice turns against the same decision - the gate is message-level and
    world-agnostic, so running it per voice would be paying twice for the
    same answer. run_turn's own behavior is unchanged: it calls run_gate and
    reads these fields exactly where it used to compute them inline."""
    gate: dict
    gate_result: object  # engine.m5.failure.resolve_gate's result, kept whole
    safety_outcome: CallOutcome
    reader_outcome: CallOutcome
    safety_state_events: list[dict]
    usage_records: list[UsageRecord]


def run_gate(
    *,
    session_id: str,
    safety_client,
    safety_model_id: str,
    participant_message: str,
    pressed: dict,
    anachronistic_term_ids: set,
    track_b_accumulator: dict | None = None,
) -> GateRun:
    """The gate half of run_turn, verbatim - see run_turn's docstring for
    the semantics of each input. The sealed safety call still gets an empty
    window and an empty accumulator (the RECORDED, NOT CONSULTED discipline;
    engine.m5.safety_accumulation's own module docstring)."""
    usage_records: list[UsageRecord] = []

    # Concurrent, not sequential (Build-Plan.md Stage 0a): the two calls
    # share no state and the httpx-based Bedrock SDK client is thread-safe,
    # so there is nothing to serialize here. Submitted together, then
    # resolved in the same fixed order (safety, reader) the rest of this
    # function - and usage_records - has always assumed, regardless of
    # which future actually completes first.
    with ThreadPoolExecutor(max_workers=2) as pool:
        safety_future = pool.submit(live_calls.call_safety, safety_client, safety_model_id, message=participant_message, recent_window=[], accumulator={})
        reader_future = pool.submit(live_calls.call_reader, safety_client, safety_model_id, message=participant_message)
        safety_outcome = safety_future.result()
        reader_outcome = reader_future.result()

    # Citation attachment shares the safety model's quota; a throttled gate
    # call pauses it so the next turns' safety calls get the headroom.
    if safety_outcome.rate_limited or reader_outcome.rate_limited:
        citation_attach.start_cooldown()

    if rec := _maybe_record_usage(safety_outcome, session_id=session_id, call_kind="safety_call", model_id=safety_model_id):
        usage_records.append(rec)
    if rec := _maybe_record_usage(reader_outcome, session_id=session_id, call_kind="reader_call", model_id=safety_model_id):
        usage_records.append(rec)

    # The modern terms in play, settled once so routing and the bridge read
    # the same list. Whether the participant used a fleet modern term is a
    # dictionary lookup of the message, not the reader's judgement.
    if reader_outcome.value is not None:
        reader_outcome.value["modern_terms"] = terms_in_message(participant_message, load_fleet_records())

    gate_result = resolve_gate(
        safety_outcome=safety_outcome, reader_outcome=reader_outcome, pressed=pressed,
        anachronistic_term_ids=anachronistic_term_ids, message=participant_message,
    )
    gate = _gate_decision_payload(
        safety_outcome=safety_outcome, reader_outcome=reader_outcome, gate_result=gate_result
    )
    # RECORDED, NOT CONSULTED. The prior accumulator comes in from the
    # caller (same seam as `pressed`) and goes only into the next
    # safety_state payload - it is deliberately NOT passed to
    # live_calls.call_safety above, which still gets an empty window and an
    # empty accumulator. Feeding it back would change the sealed call's own
    # input and oblige the full live safety rerun (Program-Spec SS210)
    # against a 33-scenario corpus that was authored entirely as single
    # messages with no window. That is a separate decision on separate
    # evidence; see engine.m5.safety_accumulation's module docstring.
    safety_states = safety_state_events(
        track_b_accumulator, None if safety_outcome.failed else safety_outcome.value
    )
    return GateRun(
        gate=gate,
        gate_result=gate_result,
        safety_outcome=safety_outcome,
        reader_outcome=reader_outcome,
        safety_state_events=safety_states,
        usage_records=usage_records,
    )


@dataclass(frozen=True)
class TurnResult:
    routing_action: str
    routing_reason: str
    # This turn's gate_decision payload, whole (engine.m4.events' required
    # key set), written to the event log verbatim by the caller. Its
    # modern_terms are the dictionary scan's, each with its source.
    gate: dict = field(default_factory=dict)
    # The safety_state events this turn should append, already validated in
    # shape by engine.m5.safety_accumulation. Assembled here for the same
    # reason the gate payload is - this is where the safety outcome lives -
    # and appended by the caller, because this module still makes no store
    # writes of its own. Empty on most turns by design: an event is written
    # only when something actually changed.
    safety_state_events: list[dict] = field(default_factory=list)
    facilitator_events: list[dict] = field(default_factory=list)
    voice_event: dict | None = None
    degraded: bool = False
    usage_records: list[UsageRecord] = field(default_factory=list)


def _maybe_record_usage(outcome: CallOutcome, *, session_id: str, call_kind: str, model_id: str, world_key: str | None = None) -> UsageRecord | None:
    """Every real call's raw usage is parity-checked (engine.m8.parity)
    BEFORE it becomes a UsageRecord - "usage logging with correct cache
    accounting tested against raw API shapes" happens inline, on every real
    turn, not as a separate exercise run occasionally. A divergence raises
    loudly here rather than silently producing a wrong attributed number.

    world_key (Artifact-7 SS7): set for table-mode voice/selector calls so
    per-world cost at a shared table is answerable; None everywhere else -
    an interview session's calls are attributable from session_id alone."""
    if outcome.raw_usage is None:
        return None
    from engine.m8.parity import assert_parity
    from engine.provider.bedrock import normalize_usage

    normalized = normalize_usage(outcome.raw_usage)
    assert_parity(outcome.raw_usage, normalized)
    return record_usage(usage=normalized, session_id=session_id, call_kind=call_kind, model_id=model_id, world_key=world_key)


def _directive_payload(directive: Directive | None) -> dict | None:
    return None if directive is None else {
        "asks": list(directive.asks),
        "register_note": directive.register_note,
        "suspend_register_statement_1": directive.suspend_register_statement_1,
        "ambiguity_options": list(directive.ambiguity_options),
        "kind": directive.kind,
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


def _append_seat_identity_correction(turn_directive: str | None, offending_prefix: str) -> str:
    """The seat-identity guard's one regeneration: named to the voice, in
    the same private-directive channel
    _build_turn_directive already owns (measured to win over a competing
    pressure sitting in the user turn - see that function's own docstring)
    - never a second, separately-timed call or a rewrite of the world
    prompt itself. Appended onto whatever _build_turn_directive already
    produced (which may be None) rather than replacing it: the retry is
    still the same turn, same asks, same evidence, minus the one thing
    that went wrong."""
    correction = (
        "\n## Correction (your last attempt failed this)\n"
        f'Your previous answer opened a new line or sentence with "{offending_prefix}" - writing as if you '
        "were the Facilitator or another seat at this Table. You are only ever yourself: answer strictly in "
        "your own voice, with no speaker labels, no \"Name:\" prefixes, and no attributed dialogue for anyone "
        "else at the Table."
    )
    return (turn_directive or "") + correction


def _append_r27_correction(turn_directive: str | None, hard_offenses: list[dict]) -> str:
    """The uncited-claims rule's own one regeneration: same append-not-replace channel and
    shape as _append_seat_identity_correction above - the exact wording
    engine.m4.live_uncited_claims_battery's own `_build_correction`
    already proved live in the battery's own simulation, now the
    canonical, single-owned copy; the battery imports this function
    rather than keeping its own duplicate."""
    named = "; ".join(f'"{o["sentence"]}"' for o in hard_offenses)
    correction = (
        "\n## Correction (your last answer had uncited claims)\n"
        f"These sentences from your last answer carried no citation: {named} "
        "Answer again: cite every specific claim to one of your own records with an inline [[record.id]] tag, "
        "or, where your own records are silent, say so plainly instead of stating it without one."
    )
    return (turn_directive or "") + correction


def _append_sentence_fact_check_correction(turn_directive: str | None, flags: list[dict]) -> str:
    """sentence_enforce's own one regeneration: the same append-not-
    replace channel and shape as _append_r27_correction above, naming
    only the sentence(s) engine.m4.sentence_fact_check.
    find_unsupported_named_claims flagged this attempt - never the whole
    turn, and never any other offense class this correction did not name.
    Asks for exactly the two outcomes sentence_enforce is prepared to
    accept: support the claim from the world's own sources, or drop it
    voluntarily, since a second failure drops it involuntarily anyway
    (see _run_ordinary_voice_turn's own docstring, sentence_enforce)."""
    named = "; ".join(f'"{f["sentence"]}"' for f in flags)
    correction = (
        "\n## Correction (your last answer named something your own sources do not support)\n"
        f"These sentences from your last answer named a person, place, date, or number your own records do not "
        f"give: {named} Answer again: support each named claim from your own sources with an inline "
        "[[record.id]] tag, or drop the unsupported name or number entirely rather than stating it."
    )
    return (turn_directive or "") + correction


def _draft_is_final_text(
    *, is_other_tradition_first_ask: bool, self_revision_enabled: bool, r27_enforce: bool, sentence_enforce: bool,
) -> bool:
    """Whether every sentence released is certain to be in the reply a
    participant keeps. A regeneration (the two enforcement flags) or a
    rewrite (self-revision, which runs on a first other-tradition ask) would
    replace text already shown, so on those turns nothing streams. The
    seat-identity guard does not stop a Table turn streaming: it reads each
    sentence before release (engine.m4.sentence_stream), regenerates when it
    catches the first one, and cuts the turn at a later one (decision 38)."""
    return not ((is_other_tradition_first_ask and self_revision_enabled) or r27_enforce or sentence_enforce)


def apply_net(
    raw_text: str, *, repository_records: dict[str, dict], thin_topics: list[dict] | None,
    quotable_texts: list[str] | None = None,
) -> tuple[str, list[dict], dict]:
    """THE one owner of the voice text shape - everything a Representative
    says, in any mode AND in admission, is shaped by this function and only
    this function. The deterministic net (engine.m4.grounding_net.
    check_turn) runs over one turn's raw tagged output; the text keeps
    every sentence with the tags stripped (see the in-function comment -
    the checks gate decoration, never the text), and only ok-verdict
    sentences' tags become this turn's per-sentence citations (Artifact-5's
    citations event, gaining per-sentence anchors instead of one turn-level
    list; no separate SSE transport exists to wire this into yet, so it
    rides on TurnResult.voice_event['citations'] until one does). Returns
    (text, citations, net_result) - net_result is kept whole (not just
    substantive_survives) so a caller can audit every sentence's own
    verdict, tags, and why, same as the M7 audit input the design names in
    §6.3.

    Public on purpose (a foundation audit found): M3's LiveModelAnswerer
    used to re-implement this shape and drifted - it deleted withheld
    sentences and appended a floor line, both behaviors this function's own
    history had measured and rejected - so admission was grading a text no
    participant would ever read. Admission now calls this function, making
    parity structural rather than asserted. A change here changes what the
    admission battery measures, by design: they are the same thing."""
    # Calls check_turn_with_paragraph_coverage instead of check_turn
    # - proven equivalent on "sentences"/"substantive_survives"/
    # "truncated" (test_grounding_net.py's own equivalence test), so
    # text/citations below are unchanged; net_result now additionally
    # carries "paragraph_coverage", unused by any reader that doesn't ask
    # for it. This is the single-pass fold: _run_ordinary_voice_turn
    # below reads paragraph coverage off THIS SAME net_result rather than
    # making a second, independent check_turn_with_paragraph_coverage
    # call - a live turn now pays the net once, not twice, in both
    # report-only and enforced modes.
    net_result = grounding_net.check_turn_with_paragraph_coverage(
        raw_text, repository_records, thin_topics=thin_topics, quotable_texts=quotable_texts,
    )
    # THE CHECKS GATE DECORATION, NEVER THE TEXT. Program-Spec M4, and
    # again in Artifact-5 SS2 ("they gate decoration, not text"), and again
    # in SS5 ("never by editing a live response"). What the voice wrote is
    # what the participant reads; only the tags come off, and the marks round
    # words found in no record (decision 59).
    #
    # Deleting the failures was measured over 17 live turns: 25% of every
    # sentence generated, 39% of them on prose that invented nothing, and
    # the deletion orphaned whatever came next - a question about who
    # someone was, answered without naming anyone, because the naming
    # sentence went. A sentence that fails verification loses its citation
    # and is carried on the event for the SS5 audit; it is not destroyed on
    # the way to the screen.
    text = grounding_net.shown_text(raw_text, net_result["sentences"])
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
    already_bridged_figure_ids: set[str] | None = None,
    already_bridged_gloss_ids: set[str] | None = None,
    history: list[dict] | None = None,
    previous_kind: str | None = None,
    rhythm: RhythmTally | None = None,
    context_prefix: str | None = None,
    secondary_context: str | None = None,
    table_engagement: str | None = None,
    usage_world_key: str | None = None,
    guard_labels: list[str] | None = None,
    is_other_tradition_first_ask: bool = False,
    other_tradition_evidence_ids: list[str] | None = None,
    other_tradition_seated: bool = False,
    other_tradition_seated_name: str | None = None,
    other_tradition_repeat_turn: bool = False,
    other_tradition_known_in_window: bool | None = None,
    other_tradition_revealed: list[tuple[str, str]] | None = None,
    correction: str | None = None,
    debug_capture: dict | None = None,
    r27_enforce: bool = False,
    known_tradition_names: list[str] | None = None,
    self_revision_enabled: bool = True,
    sentence_enforce: bool = False,
    on_sentence: Callable[[dict], None] | None = None,
    citation_attach_model_id: str | None = None,
) -> tuple[dict, list[UsageRecord]]:
    """context_prefix, secondary_context, table_engagement, and
    usage_world_key are the table's additions (Artifact-7 SS3-4, SS7; Stage
    4f, Build-Plan.md), all None on every interview call so that path is
    byte-identical to before they existed. context_prefix carries the
    attributed at-the-Table speech since this voice's last turn - it rides
    in the per-turn user message only (never the cached system prefix, same
    cache discipline as the evidence block) and is deliberately NOT part of
    the message evidence assembly matches against: retrieval stays focused
    on the participant's own ask, not on what another voice said - EXCEPT at
    the secondary weight secondary_context supplies below, when the ask
    alone leaves a real gap. table_engagement carries the behavioral rule
    about that speech (engage it, stay compact, no foreknowledge) into
    _build_turn_directive's channel instead - see that function's own note
    on why the instruction and the content it's about now ride separately.
    usage_world_key tags this call's UsageRecord with the speaking world.

    secondary_context is the same at-the-Table speech context_prefix
    carries, unwrapped (no model-facing framing sentences), passed straight
    through to evidence.assemble_evidence's own parameter of the same name -
    fills only the cell slots the participant's own message left empty,
    never displaces a real match. Same repository_records this call already
    has; no new read, no model call, no per-turn cost growth.

    guard_labels: the seat-identity guard's own opt-in - None on every
    interview call (interview has no other seats to impersonate and
    never builds the attributed-transcript convention this defect
    echoes), so that path stays byte-identical too.
    engine.api.table_wiring passes the Facilitator's label plus every
    OTHER seated voice's label (full "Name (World)" and bare "Name" forms)
    - never the speaking voice's own label; see
    engine.m4.seat_identity_guard's own module docstring for why. A caught
    turn regenerates once, with the violation named in the retry's own
    directive (_append_seat_identity_correction); a second catch is
    reported back to the caller via this turn's additive
    seat_identity_violations/seat_identity_guard_exhausted fields rather
    than raised, so a caller that never passes guard_labels (every
    interview call) can go on reading this function's return shape exactly
    as it always has.

    correction: free text appended onto whatever
    _build_turn_directive already produced, same channel and same
    append-not-replace shape as _append_seat_identity_correction. None
    on every real caller
    (engine.api.wiring, engine.api.table_wiring never pass it - it is
    battery-only, with no participant path) - it exists
    so engine.m4.live_uncited_claims_battery can simulate one regeneration
    naming a turn's own uncited sentences without duplicating this
    function's evidence-assembly/generation logic in the battery script
    itself. Purely additive: unset, this parameter changes nothing.

    debug_capture: an optional caller-supplied dict this
    function mutates in place, setting "raw_tagged_text" to the exact
    text apply_net is about to check -
    same battery-only, unset-on-every-real-caller shape as correction
    above. Never part of voice_event (no schema key for it, so it can
    never reach the real event log through this channel) - exists so the
    battery can compute paragraph-level citation coverage from the same
    raw text apply_net already has, without a second model call or a
    second copy of this function's own generation logic.

    The enforce flag and known_tradition_names (the uncited-claims rule's
    flag-gated enforcement):
    OFF by default so every existing caller and every existing test is
    byte-identical until a caller opts in. When True: after the net's
    own check (below), a wholly_uncited_paragraph offense or a
    neighbour_named offense (the two classes this enforces -
    inherited_ungrounded stays report-only) triggers exactly one
    regeneration, in the same turn, with the violations named in the
    retry's own directive (the same append-not-replace correction
    channel and the same "regenerate once, then hand off" shape the
    seat-identity guard above and
    engine.m4.live_uncited_claims_battery's own `correction` parameter
    already use - not a third mechanism). The regenerated answer is
    re-checked the identical way; if a hard offense still survives, this
    turn's own text is set aside (answer_text/citations/net_result
    recomputed against "", exactly as seat_identity_guard_exhausted
    already sets raw_text="" above) and the enforcement-exhausted flag is
    True on the returned voice_event, for the caller to substitute a
    Facilitator turn (engine.m4.facilitator_turns.
    table_seat_correction_turn on a Table call, the same existing
    fallback; voice_turn_rejected_turn on an interview call) exactly as
    it already does for seat_identity_guard_exhausted.
    own_doctrine_in_other_tradition_turn is deliberately not computed
    here: this enforcement is narrowed to fire only on a real
    paragraph-level failure, so every sentence it would catch is already
    a wholly_uncited_paragraph offense this function catches directly -
    own_doctrine_in_other_tradition_turn itself still needs
    registry/routing context this function doesn't have and stays the
    caller's own refinement (build_uncited_claims_event), unchanged, for
    the persisted audit event. known_tradition_names is required when
    the enforce flag is True (fails loudly rather than silently skipping the
    neighbour_named check if omitted) - the same pre-derived list
    engine.m4.uncited_claims.known_tradition_names already produces for
    the report-only build_uncited_claims_event path, computed by the
    caller (which has registry access this function does not) and
    passed straight through.

    sentence_enforce (engine.m4.sentence_fact_check's own flag-gated
    enforcement, a second and independent mechanism from the
    uncited-claims enforcement's own flag above - distinct
    flag, distinct correction text, distinct failure shape): OFF by
    default, same byte-identical-until-opted-in guarantee as that
    enforcement. When True, runs after the uncited-claims enforcement
    above has already settled this turn's own text (whichever net_result
    that left in place - the first attempt's if that enforcement is off
    or never tripped, the regenerated one otherwise): if
    find_unsupported_named_claims flags anything against that text,
    exactly one regeneration follows, with the flagged sentence(s) named
    in the retry's own directive (_append_sentence_fact_check_correction,
    the same append-not-replace channel _append_r27_correction already
    uses - a third mechanism was not written for this). When the
    uncited-claims enforcement is also on and its own correction fired
    this turn, that correction rides forward into this retry's own
    directive too (composed, not replaced) - a fresh regeneration has no
    memory of the earlier call's own correction, so without carrying it
    forward this retry could just as easily regress a citation fix that
    enforcement's own retry had already won.

    The regenerated answer is re-checked TWICE, in a fixed order. First,
    when the uncited-claims enforcement is on: a wholly_uncited_paragraph
    or neighbour_named offense surviving THIS retry is that
    enforcement's own exhaustion, the identical fallback (whole turn
    blanked, that enforcement's own exhaustion flag set, caller
    substitutes a Facilitator turn) its own second failure above already
    uses - its own one-regeneration budget was already spent in the
    block above, so
    a hard offense reappearing here does not get a second regeneration
    of its own. The uncited-claims enforcement's own safety guarantee
    sits above sentence_enforce's own preferences: it is checked first,
    and it can still blank the turn even though sentence_enforce's own
    failure mode (below) never does.

    Second, only when no r27 hard offense survived: find_unsupported_
    named_claims runs again. A sentence still flagged is removed from
    the answer on its own (engine.m4.grounding_net.drop_flagged_
    sentences) - UNLESS dropping every still-flagged sentence would
    leave nothing behind, in which case the regenerated answer is kept
    as it stands, still-flagged sentence(s) and all: sentence_enforce's
    own failure mode never blanks the turn and never substitutes the
    Facilitator, even when nothing is left to drop safely. Either way,
    net_result/answer_text/citations/uncited_claims/paragraph_offenses/
    named_claim_flags/fact_check_flags are all recomputed against
    whichever text this turn ultimately answers with - the same
    recompute-on-retry discipline that enforcement's own retry already
    follows, so every report-only field on the returned voice_event
    describes the text a participant actually receives, including a
    flag deliberately left standing rather than dropped or hidden.
    Every sentence dropped
    this way, whether the correction alone already fixed everything, and
    which sentences (if any) are still flagged and left standing, is
    recorded on voice_event["sentence_enforcement"] (always present,
    empty/false on a clean turn or when this flag is off - same shape
    discipline as seat_identity_violations above). A drop can still
    leave a sentence that grammatically introduced the one just removed
    reading as an unfinished promise (drop_flagged_sentences' own
    docstring names this residual, structural-not-semantic limit); it
    never leaves a broken sentence or an empty paragraph.

    other_tradition_evidence_ids (corrects a false
    honest-limit statement, unconditional - never gated behind
    the enforce flag, since this corrects an existing false statement rather
    than adding new enforcement): engine.m4.uncited_claims.world_records_
    mention_tradition's own result for the tradition THIS turn's message
    names, if any - same caller-computed, registry-access-needed shape
    as known_tradition_names. Read only inside _build_turn_directive,
    only when is_other_tradition_first_ask is also true; harmless (and
    correctly ignored) to pass on any other turn.

    other_tradition_known_in_window and other_tradition_revealed (the
    tradition-pivot rule): engine.m4.uncited_claims.tradition_known_in_window and
    conversation_revealed_excerpts, for the same named tradition - the
    same caller-computed shape as other_tradition_evidence_ids, read at
    the same single place (_other_tradition_directive).

    on_sentence receives each sentence, with its marks, as the voice
    finishes writing it (engine.m4.sentence_stream), so a caller can show the
    reply while it is still being written. It is called only when the
    finished reply is guaranteed to be exactly that text (_draft_is_final_text);
    on any other turn it is never called and the caller waits for the whole
    reply. It observes only - nothing here changes because it is set."""
    if r27_enforce and known_tradition_names is None:
        raise ValueError(
            "r27_enforce=True requires known_tradition_names (see engine.m4.uncited_claims.known_tradition_names) "
            "- never guess the neighbour_named check's own name list"
        )
    usage_records = []
    # EVIDENCE ASSEMBLY + PRIVATE DIRECTIVE (design §3, engine.m4.evidence;
    # this function's own docstring for context_prefix/secondary_context/
    # table_engagement/the other_tradition_* family/correction) -
    # engine.m4.turn_prep.prepare_voice_turn_inputs.
    prepared = prepare_voice_turn_inputs(
        world=world,
        participant_message=participant_message,
        directive=directive,
        already_told_ids=already_told_ids,
        already_bridged_figure_ids=already_bridged_figure_ids,
        history=history,
        previous_kind=previous_kind,
        rhythm=rhythm,
        context_prefix=context_prefix,
        secondary_context=secondary_context,
        table_engagement=table_engagement,
        is_other_tradition_first_ask=is_other_tradition_first_ask,
        other_tradition_evidence_ids=other_tradition_evidence_ids,
        other_tradition_seated=other_tradition_seated,
        other_tradition_seated_name=other_tradition_seated_name,
        other_tradition_repeat_turn=other_tradition_repeat_turn,
        other_tradition_known_in_window=other_tradition_known_in_window,
        other_tradition_revealed=other_tradition_revealed,
        correction=correction,
    )
    repository_records = prepared.repository_records
    thin_topics = prepared.thin_topics
    figures_already_named = prepared.figures_already_named
    user_message = prepared.user_message
    turn_directive = prepared.turn_directive
    # Words said in this conversation may be quoted back: the participant's
    # message, the replayed transcript, and the table's context.
    echo_sources = [
        text for text in (
            participant_message, context_prefix, secondary_context,
            *((turn.get("content") for turn in history or [])),
        ) if isinstance(text, str) and text
    ]
    _net = functools.partial(apply_net, quotable_texts=echo_sources)
    demonstrations = DemonstrationIndex(repository_records)
    on_text = None
    sentences = None
    if on_sentence is not None and _draft_is_final_text(
        is_other_tradition_first_ask=is_other_tradition_first_ask,
        self_revision_enabled=self_revision_enabled, r27_enforce=r27_enforce, sentence_enforce=sentence_enforce,
    ):
        sentences = SentenceStream(
            repository_records=repository_records, world_key=world.world_key, thin_topics=thin_topics,
            guard=(lambda raw: find_seat_identity_violation(raw, guard_labels)) if guard_labels else None,
            demonstrations=demonstrations, quotable_texts=echo_sources,
        )

        def on_text(chunk: str) -> None:
            for event in sentences.feed(chunk):
                on_sentence(event)

    stream_outcome = stream_voice_turn(
        voice_client, voice_model_id, system_prompt=world.prompt_text,
        turn_directive=turn_directive, message=user_message, history=history, on_text=on_text,
    )
    if stream_outcome.status != "ok":
        raise RuntimeError(f"voice generation call failed: {stream_outcome.status} {stream_outcome.value}")
    if rec := _maybe_record_usage(stream_outcome, session_id=session_id, call_kind="voice_generation", model_id=voice_model_id, world_key=usage_world_key):
        usage_records.append(rec)

    # SEAT-IDENTITY GUARD - reject, regenerate once with the violation
    # named, and if that also catches, report it back rather than raise:
    # guard_labels is only ever non-empty
    # on a Table call (see this function's own docstring), so this whole
    # block is a no-op, zero-cost on every interview call.
    raw_text = stream_outcome.value.text
    seat_identity_violations: list[dict] = []
    seat_identity_guard_exhausted = False
    # A streamed Table turn the guard caught after sentences were already
    # shown cannot be regenerated: it ends at its last released sentence,
    # and the caller adds the Facilitator's seat-cut line.
    seat_identity_cut = False
    if sentences is not None and (kept := sentences.cut(raw_text)) is not None:
        seat_identity_violations.append({
            "world_key": world.world_key, "attempt": "streamed",
            "offending_prefix": find_seat_identity_violation(raw_text[len(kept):], guard_labels),
        })
        raw_text = kept
        seat_identity_cut = True
    offending = find_seat_identity_violation(raw_text, guard_labels) if guard_labels else None
    seat_retry_directive: str | None = None
    if offending and sentences is not None and sentences.released:
        # Inside a sentence the splitter kept whole (a quotation spanning a
        # full stop), so the per-sentence check passed it and it is already
        # shown: recorded, never regenerated over text a participant has read.
        seat_identity_violations.append({"world_key": world.world_key, "offending_prefix": offending, "attempt": "shown"})
        offending = None
    if offending:
        seat_identity_violations.append({"world_key": world.world_key, "offending_prefix": offending, "attempt": "first"})
        retry_outcome = stream_voice_turn(
            voice_client, voice_model_id, system_prompt=world.prompt_text,
            turn_directive=(seat_retry_directive := _append_seat_identity_correction(turn_directive, offending)),
            message=user_message, history=history,
        )
        if retry_outcome.status != "ok":
            raise RuntimeError(f"voice generation retry call failed: {retry_outcome.status} {retry_outcome.value}")
        if rec := _maybe_record_usage(
            retry_outcome, session_id=session_id, call_kind="voice_generation_retry", model_id=voice_model_id, world_key=usage_world_key
        ):
            usage_records.append(rec)
        retry_text = retry_outcome.value.text
        retry_offending = find_seat_identity_violation(retry_text, guard_labels)
        if retry_offending:
            seat_identity_violations.append({"world_key": world.world_key, "offending_prefix": retry_offending, "attempt": "regenerated"})
            seat_identity_guard_exhausted = True
            raw_text = ""  # the voice's text is not shown - the caller substitutes a Facilitator turn
        else:
            raw_text = retry_text

    # RECITATION (decision 59, check 3) - a reply that reads a demonstration
    # out gets one regeneration, with the directive line appended, when
    # nothing of it has been streamed yet. A second match is passed through
    # and reported on voice_event["recited_demonstration"]; never a second
    # regeneration.
    recitation_regenerated = False
    recitation_retry_failed = False
    if raw_text and demonstrations.is_recited(raw_text) and (sentences is None or not sentences.released):
        retry_base = seat_retry_directive if seat_retry_directive is not None else (turn_directive or "")
        retry_outcome = stream_voice_turn(
            voice_client, voice_model_id, system_prompt=world.prompt_text,
            turn_directive=retry_base + "\n" + DIRECTIVE_LINE,
            message=user_message, history=history,
        )
        if rec := _maybe_record_usage(
            retry_outcome, session_id=session_id, call_kind="voice_generation_retry", model_id=voice_model_id, world_key=usage_world_key
        ):
            usage_records.append(rec)
        if retry_outcome.status == "ok" and not (guard_labels and find_seat_identity_violation(retry_outcome.value.text, guard_labels)):
            raw_text = retry_outcome.value.text
            recitation_regenerated = True
            # later retries this turn carry the line too
            turn_directive = retry_base + "\n" + DIRECTIVE_LINE
        else:
            recitation_retry_failed = True

    # SELF-REVISION - the generation-side
    # fix for a fabricated detail riding a real citation tag,
    # engine.m4.self_revision's own module docstring carries the full
    # mechanism and its pre-stream compatibility note. Runs only on
    # other_tradition-routed turns (is_other_tradition_first_ask), where
    # the leak class lives, and only when the draft survived the seat-
    # identity guard above (raw_text is never truthy after that guard's
    # own exhaustion path, so this never spends a call revising a blank
    # turn). self_revision_enabled is the caller-computed CIC_SELF_
    # REVISION kill-switch (engine.api.config, same pattern as
    # the enforce flag or its environment switch) - default True, cost/incident use
    # only; unlike the enforce flag this is generation, not enforcement, so
    # it needs no known_tradition_names/registry access of its own.
    self_revision_meta: dict = {
        "ran": False, "changed": False, "draft_length": None, "revised_length": None,
        "fallback_reason": None, "latency_seconds": 0.0,
    }
    if raw_text and is_other_tradition_first_ask and self_revision_enabled:
        self_revision_result = self_revise(
            client=voice_client, model_id=voice_model_id, system_prompt=world.prompt_text,
            participant_message=participant_message, draft_raw_text=raw_text,
            repository_records=repository_records,
        )
        if self_revision_result["call_outcome"] is not None:
            if rec := _maybe_record_usage(
                self_revision_result["call_outcome"], session_id=session_id, call_kind="self_revision",
                model_id=voice_model_id, world_key=usage_world_key,
            ):
                usage_records.append(rec)
        raw_text = self_revision_result["revised_text"]
        self_revision_meta = {
            "ran": self_revision_result["ran"],
            "changed": self_revision_result["changed"],
            "draft_length": self_revision_result["draft_length"],
            "revised_length": self_revision_result["revised_length"],
            "fallback_reason": self_revision_result["fallback_reason"],
            "latency_seconds": round(self_revision_result["latency_seconds"], 3),
        }

    if debug_capture is not None:
        # The raw, still-tagged, still-paragraphed answer - never
        # part of voice_event (no schema key for it, never persisted to
        # the real event log), a side channel purely for
        # engine.m4.live_uncited_claims_battery to compute
        # paragraph-coverage from, the same "mutate a caller-supplied
        # dict, opt-in, unset on every real caller" shape `correction`
        # already uses. This is the exact text apply_net is about to
        # strip and check below - nothing recomputed, nothing
        # re-derived.
        debug_capture["raw_tagged_text"] = raw_text

    answer_text, citations, net_result = _net(raw_text, repository_records=repository_records, thin_topics=thin_topics)

    # The report-only turn checks (uncited claims, wholly uncited
    # paragraphs, named-claim grounding, the sentence fact check) run after
    # the conversation, in M7 (engine.m7.offline_checks), from the net
    # result this turn logs. They run here only when an enforcement flag
    # needs them to decide the turn.
    enforcing = r27_enforce or sentence_enforce
    if enforcing:
        uncited_claims = find_uncited_claims(net_result["sentences"])
        paragraph_offenses = find_uncited_paragraphs(net_result)
        named_claim_flags = find_named_claim_flags(net_result["sentences"], repository_records=repository_records)
        fact_check_flags = find_unsupported_named_claims(net_result["sentences"], repository_records=repository_records)

    # The uncited-claims rule's flag-gated enforcement, OFF by default
    # (see this function's own docstring for the full shape). The enforcement-exhausted flag
    # and the regenerated flag in attempts_meta are always set (False/absent
    # when the enforce flag is False or nothing tripped it), so every reader of
    # voice_event can check them unconditionally, the same
    # always-present-but-usually-empty shape seat_identity_violations
    # already uses.
    r27_enforcement_exhausted = False
    if r27_enforce:
        refined_for_enforcement = [classify_neighbour_named(o, known_tradition_names) for o in uncited_claims]
        hard_offenses = [o for o in paragraph_offenses if o["class"] == "wholly_uncited_paragraph"] + [
            o for o in refined_for_enforcement if o["class"] == "neighbour_named"
        ]
        if hard_offenses:
            attempts_meta_r27_regenerated = True
            retry_outcome = stream_voice_turn(
                voice_client, voice_model_id, system_prompt=world.prompt_text,
                turn_directive=_append_r27_correction(turn_directive, hard_offenses),
                message=user_message, history=history,
            )
            if retry_outcome.status != "ok":
                raise RuntimeError(f"voice generation retry call failed: {retry_outcome.status} {retry_outcome.value}")
            if rec := _maybe_record_usage(
                retry_outcome, session_id=session_id, call_kind="voice_generation_retry", model_id=voice_model_id, world_key=usage_world_key
            ):
                usage_records.append(rec)
            retry_raw_text = retry_outcome.value.text
            retry_answer_text, retry_citations, retry_net_result = _net(
                retry_raw_text, repository_records=repository_records, thin_topics=thin_topics
            )
            retry_uncited_claims = find_uncited_claims(retry_net_result["sentences"])
            retry_paragraph_offenses = find_uncited_paragraphs(retry_net_result)
            # Recomputed against retry_net_result for the same reason
            # retry_uncited_claims/retry_paragraph_offenses are: whichever
            # net_result this turn ultimately answers with is the one
            # named_claim_flags must describe, report-only field or not -
            # a stale, pre-retry flag list would misreport a sentence this
            # turn never actually sent.
            retry_named_claim_flags = find_named_claim_flags(retry_net_result["sentences"], repository_records=repository_records)
            # Same recompute-on-retry discipline as retry_named_claim_flags
            # above, same reason: whichever net_result this turn ultimately
            # answers with is the one this report-only field must describe.
            retry_fact_check_flags = find_unsupported_named_claims(retry_net_result["sentences"], repository_records=repository_records)
            retry_refined = [classify_neighbour_named(o, known_tradition_names) for o in retry_uncited_claims]
            retry_hard_offenses = [o for o in retry_paragraph_offenses if o["class"] == "wholly_uncited_paragraph"] + [
                o for o in retry_refined if o["class"] == "neighbour_named"
            ]
            if retry_hard_offenses:
                r27_enforcement_exhausted = True
                raw_text = ""  # the voice's text is not shown - the caller substitutes a Facilitator turn
                answer_text, citations, net_result = _net("", repository_records=repository_records, thin_topics=thin_topics)
                uncited_claims = []
                paragraph_offenses = []
                named_claim_flags = []
                fact_check_flags = []
            else:
                raw_text = retry_raw_text
                answer_text, citations, net_result = retry_answer_text, retry_citations, retry_net_result
                uncited_claims = retry_uncited_claims
                paragraph_offenses = retry_paragraph_offenses
                named_claim_flags = retry_named_claim_flags
                fact_check_flags = retry_fact_check_flags
        else:
            attempts_meta_r27_regenerated = False
    else:
        attempts_meta_r27_regenerated = False

    # sentence_enforce's own flag-gated enforcement, OFF by default (see
    # this function's own docstring for the full shape). Runs on
    # whichever net_result the uncited-claims enforcement above already
    # settled on - the first attempt's if that enforcement is off or
    # never tripped, the regenerated one otherwise. sentence_dropped/regenerated
    # are always set (empty/false when sentence_enforce is False or
    # nothing tripped it), the same always-present-but-usually-empty
    # shape attempts_meta already uses.
    sentence_enforcement = {"flagged": [], "regenerated": False, "still_flagged": [], "sentences_dropped": []}
    if sentence_enforce and fact_check_flags:
        sentence_enforcement["flagged"] = [f["sentence"] for f in fact_check_flags]
        sentence_enforcement["regenerated"] = True
        # Composed, not replaced: when the uncited-claims enforcement
        # already regenerated once this turn (hard_offenses is only ever
        # defined - possibly empty - when the uncited-claims enforcement is on), that
        # same correction rides forward into this retry's own directive
        # too. A fresh regeneration has no memory of the earlier call's
        # own correction; without carrying it forward, asking the voice
        # to fix a named claim could just as easily regress the citation
        # fix that enforcement's own retry had already won.
        sentence_retry_directive = turn_directive
        if r27_enforce and hard_offenses:
            sentence_retry_directive = _append_r27_correction(sentence_retry_directive, hard_offenses)
        sentence_retry_directive = _append_sentence_fact_check_correction(sentence_retry_directive, fact_check_flags)
        retry_outcome = stream_voice_turn(
            voice_client, voice_model_id, system_prompt=world.prompt_text,
            turn_directive=sentence_retry_directive,
            message=user_message, history=history,
        )
        if retry_outcome.status != "ok":
            raise RuntimeError(f"voice generation retry call failed: {retry_outcome.status} {retry_outcome.value}")
        if rec := _maybe_record_usage(
            retry_outcome, session_id=session_id, call_kind="voice_generation_retry", model_id=voice_model_id, world_key=usage_world_key
        ):
            usage_records.append(rec)
        retry_raw_text = retry_outcome.value.text
        retry_answer_text, retry_citations, retry_net_result = _net(
            retry_raw_text, repository_records=repository_records, thin_topics=thin_topics
        )

        # RE-CHECKED BY the uncited-claims enforcement, when that
        # enforcement is on: this retry is a fresh generation that
        # enforcement's own pass never saw, so it could just as easily
        # reintroduce a
        # wholly_uncited_paragraph or neighbour_named offense as fix the
        # named claim. That enforcement's own safety guarantee (never
        # ship one of those two offenses) sits above sentence_enforce's
        # own "never blank" preference - sentence_enforce's own
        # drop-not-blank shape (below) governs an unsupported NAME,
        # never a citation offense the uncited-claims enforcement exists
        # to catch. Its own one-regeneration budget was already spent in
        # the block above; a hard offense surviving THIS retry too is
        # exhaustion, the identical fallback its own second failure
        # already uses above.
        retry_r27_hard_offenses = []
        if r27_enforce:
            retry_refined_for_r27 = [
                classify_neighbour_named(o, known_tradition_names) for o in find_uncited_claims(retry_net_result["sentences"])
            ]
            retry_r27_hard_offenses = [
                o for o in find_uncited_paragraphs(retry_net_result) if o["class"] == "wholly_uncited_paragraph"
            ] + [o for o in retry_refined_for_r27 if o["class"] == "neighbour_named"]

        if retry_r27_hard_offenses:
            r27_enforcement_exhausted = True
            raw_text = ""  # the voice's text is not shown - the caller substitutes a Facilitator turn
            answer_text, citations, net_result = _net("", repository_records=repository_records, thin_topics=thin_topics)
            uncited_claims = []
            paragraph_offenses = []
            named_claim_flags = []
            fact_check_flags = []
        else:
            retry_fact_check_flags = find_unsupported_named_claims(retry_net_result["sentences"], repository_records=repository_records)
            if retry_fact_check_flags:
                still_flagged = {f["sentence"] for f in retry_fact_check_flags}
                sentence_enforcement["still_flagged"] = sorted(still_flagged)
                still_flagged_as_written = still_flagged | {
                    entry["source_sentence"] for entry in retry_net_result["sentences"]
                    if entry.get("source_sentence") and entry["sentence"] in still_flagged
                }
                dropped_raw_text = grounding_net.drop_flagged_sentences(retry_raw_text, still_flagged_as_written)
                if dropped_raw_text.strip():
                    # Second failure: never blank the whole turn and
                    # never substitute the Facilitator (unlike the
                    # uncited-claims enforcement's own exhaustion above)
                    # - drop only the sentence(s) still flagged, from the
                    # regenerated attempt's own raw text, then recompute
                    # every report-only field against the shortened text
                    # the same way that enforcement's own retry already
                    # does.
                    sentence_enforcement["sentences_dropped"] = sorted(still_flagged)
                    raw_text = dropped_raw_text
                else:
                    # Dropping every still-flagged sentence would leave
                    # nothing - never blank the turn for that either.
                    # Keep the regenerated answer as it stands;
                    # fact_check_flags below still reports the flag(s)
                    # standing on it rather than silently losing them.
                    raw_text = retry_raw_text
            else:
                raw_text = retry_raw_text
            answer_text, citations, net_result = _net(raw_text, repository_records=repository_records, thin_topics=thin_topics)
            uncited_claims = find_uncited_claims(net_result["sentences"])
            paragraph_offenses = find_uncited_paragraphs(net_result)
            named_claim_flags = find_named_claim_flags(net_result["sentences"], repository_records=repository_records)
            fact_check_flags = find_unsupported_named_claims(net_result["sentences"], repository_records=repository_records)

    # Verified citation attachment (engine.m4.citation_attach), off unless
    # citation_attach_model_id is set: runs on the settled text, adds a
    # citation to an uncited claim sentence only when a check call confirms
    # the record carries it, and never changes the text.
    citation_attach_meta = {"enabled": citation_attach_model_id is not None, "added": [], "trail": []}
    if citation_attach_model_id is not None and answer_text:
        added_citations, attach_usage, attach_trail = attach_citations(
            client=voice_client, model_id=citation_attach_model_id, prompt_text=world.prompt_text,
            repository_records=repository_records, net_result=net_result, session_id=session_id,
            world_key=usage_world_key,
        )
        usage_records.extend(attach_usage)
        citations = citations + added_citations
        citation_attach_meta.update(added=[c["sentence"] for c in added_citations], trail=attach_trail)

    # Real, checkable source references (see
    # citation_cards' module docstring) - resolved once here and reused
    # for both the citations a sentence already carries and whichever
    # figure mention that same sentence names.
    citations = resolve_citation_sources(citations, repository_records)

    # THE NAME/FIGURE BRIDGE (VR_1A_Transparency_Gap_2026-08-09.md) - a
    # detection pass over the finished text, same discipline as the net
    # above: string-only, no model call, runs on what the participant is
    # about to read. world.figures is compiled/figures.json, already built
    # and already loaded per turn; this is the first code that reads it.
    figures_used = find_figures_used(answer_text, world.figures.get("figures") or [], already_bridged_ids=already_bridged_figure_ids)
    figures_used = attach_cited_sources(figures_used, citations)

    # TERM/CONCEPT GLOSSES (VR_1A's other track; the original live-site
    # complaint this whole audit started from). A text scan against the
    # world's own lexicon - the same design as the name bridge above,
    # since the lexicon is the heart of the depth;
    # the module docstring carries the history of the firing rule.
    glosses = find_glosses_used(answer_text, citations, repository_records, already_bridged_ids=already_bridged_gloss_ids)

    # No code-appended floor line. Program-Spec M5: "In-world thinness is
    # never intercepted - the honest limit is the voice's own testimony,
    # not a system apology." It fired on 7 of the turns measured today and
    # on every one of the seven it landed after real surviving content,
    # telling the participant there was nothing to say directly underneath
    # the thing that had just been said. The honest limit is the voice's
    # job, and the limit records are in its ground to say it from.
    degraded_by_net = not net_result["substantive_survives"]

    # THE TRANSPARENCY PLAN - a deterministic transform over what is
    # already computed above (citations, net_result, the word marks), no
    # new evidence, no new model call. Additive: not in
    # engine.m4.events.REQUIRED_KEYS["voice_turn"], so nothing an existing
    # caller (including M3 admission) relies on changes.
    transparency = build_transparency_plan(
        citations=citations, net_result=net_result, repository_records=repository_records, world_key=world.world_key,
        text=answer_text, glosses=glosses, figures_used=figures_used,
    )

    voice_event = {
        "speaker": world.world_key,
        "text": answer_text,
        "citations": citations,
        "glosses": glosses,
        "figures_used": figures_used,
        "quote_offers": [],
        "kind": prepared.kind,
        "offered_ids": prepared.offered_ids,
        # The regenerated flag: whether this enforcement attempted the one
        # allowed regeneration this turn - False when the enforce flag is off
        # (every real caller until the flag is flipped on) or when
        # nothing hard-failed on the raw attempt. attempts_meta carries
        # no schema-validated shape (engine.m4.events' REQUIRED_KEYS only
        # requires the key's presence), so this rides here rather than
        # needing a catalog change.
        "attempts_meta": {
            "empty_stream_retries": 0, "r27_regenerated": attempts_meta_r27_regenerated,
            "self_revision": self_revision_meta,
            "citation_attach": citation_attach_meta,
            "recitation_regenerated": recitation_regenerated,
            "recitation_retry_failed": recitation_retry_failed,
        },
        # True when the reply a participant reads still runs 20 or more
        # consecutive words of a demonstration record (engine.m4.recitation).
        "recited_demonstration": bool(raw_text) and demonstrations.is_recited(raw_text),
        "grounding": net_result,
        "transparency": transparency,
        "degraded_by_net": degraded_by_net,
        # The live backstop on the finished string: the horizon scan. The
        # other output families run after the conversation, in M7. Reports,
        # never edits.
        "output_defects": check_horizon(answer_text, (world.frame.get("time_window") or {}).get("end")),
        # Additive, same discipline as transparency above: absent/empty on
        # every call that never passes guard_labels (every interview call,
        # and any Table call that generated clean on its first attempt),
        # so no existing reader of this dict needs to change.
        # seat_identity_violations is 0-2 partial payloads (world_key,
        # offending_prefix, attempt) - the caller fills in round_no/
        # position and persists one seat_identity_violation event per
        # entry. seat_identity_guard_exhausted true means answer_text is
        # deliberately "" (the voice's text is not shown) - the caller
        # substitutes a facilitator_turn (engine.m4.facilitator_turns.
        # table_seat_correction_turn) rather than surfacing this voice_turn
        # as this seat's real answer.
        "seat_identity_violations": seat_identity_violations,
        "seat_identity_guard_exhausted": seat_identity_guard_exhausted,
        "seat_identity_cut": seat_identity_cut,
        # This enforcement, additive: False unless
        # The enforce flag was on AND the one allowed regeneration still left
        # a hard offense (wholly_uncited_paragraph or neighbour_named)
        # standing. True means answer_text is deliberately "" (the
        # voice's text is not shown), uncited_claims/paragraph_offenses
        # are both [] (there is nothing left to report on an unshown
        # turn) - the caller substitutes a facilitator_turn, the exact
        # same shape seat_identity_guard_exhausted already uses above.
        "r27_enforcement_exhausted": r27_enforcement_exhausted,
        # sentence_enforce's own independent enforcement (see this
        # function's own docstring, sentence_enforce): "flagged" is
        # fact_check_flags' own sentence list from the attempt that
        # triggered the one regeneration; "still_flagged" is what
        # remained after that regeneration - empty on a clean turn or a
        # correction that fully fixed every flagged sentence.
        # "sentences_dropped" is usually the same list as "still_flagged",
        # EXCEPT when dropping every one of them would have left nothing
        # behind: there, nothing is dropped, "sentences_dropped" stays
        # empty, and "still_flagged" alone shows the flagged sentence(s)
        # this turn's own answer_text still carries as-is. This enforcement's
        # own failure mode never blanks answer_text and never substitutes
        # the Facilitator; the one way this composed turn CAN still end
        # up blank is the uncited-claims enforcement's own exhaustion
        # path above, checked first and outside this dict's own control.
        "sentence_enforcement": sentence_enforcement,
    }
    if enforcing:
        # What the enforcement decided on, for its own audit trail.
        voice_event.update({
            "uncited_claims": uncited_claims, "paragraph_offenses": paragraph_offenses,
            "named_claim_flags": named_claim_flags, "fact_check_flags": fact_check_flags,
        })
    return voice_event, usage_records


# Artifact-7 SS3: the Table's per-voice runner IS the interview's ordinary
# path, scoped to one world - same compiled prompt as cached prefix, same
# evidence assembly from that world's own coverage/repository, same
# grounding net against that world's own records. The isolation property
# falls out of this line: a table voice turn simply has no other world in
# scope. Exposed as a public name rather than duplicated, so the two modes
# can never drift apart.
run_voice_turn_for_world = _run_ordinary_voice_turn


SAFETY_ROUTES = ("safety_turn", "check_in_turn")


def safety_route_facilitator_events(gate_run, *, representative_name: str, track_a_last: dict | None) -> list[dict]:
    """The Facilitator's turn for a message routed to safety - the voice is
    never called on these routes. ACUTE_DISTRESS gets the crisis turn with
    resources appended by code; any other safety_turn signal (a dependency
    dynamic, Track B) gets the dependency check with no resources and no
    freeze; check_in_turn (an uncertain or failed safety call) gets the
    check-in, which is deliberately not an answer. One owner for these
    turns, so a message the service would otherwise refuse unread (a
    closed session, an open table round, an over-long message - decision
    35) gets exactly what an ordinary turn would."""
    action = gate_run.gate_result.routing.action
    if action == "check_in_turn":
        return [facilitator_turns.check_in_turn()]
    safety = gate_run.safety_outcome.value
    if safety["signal"] != "ACUTE_DISTRESS":
        return [facilitator_turns.dependency_check_turn(representative_name)]
    return [crisis_resources.append_crisis_resources_turn(
        signal=safety["signal"], stream_text=None, stream_failed=True,
        representative_name=representative_name,
        acute_level=safety["acute_level"],
        already_fired=track_a_last is not None,
    )]


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
    track_b_accumulator: dict | None = None,
    track_a_last: dict | None = None,
    already_told_ids: set[str] | None = None,
    already_bridged_figure_ids: set[str] | None = None,
    already_bridged_gloss_ids: set[str] | None = None,
    history: list[dict] | None = None,
    previous_kind: str | None = None,
    rhythm: RhythmTally | None = None,
    r27_enforce: bool = False,
    known_tradition_names: list[str] | None = None,
    other_tradition_evidence_ids: list[str] | None = None,
    other_tradition_known_in_window: bool | None = None,
    other_tradition_revealed: list[tuple[str, str]] | None = None,
    self_revision_enabled: bool = True,
    sentence_enforce: bool = False,
    daily_cap_reached: bool = False,
    turn_cap: int | None = None,
    facilitator_only: bool = False,
    limit_text: str | None = None,
    on_sentence: Callable[[dict], None] | None = None,
    citation_attach_enabled: bool = False,
) -> TurnResult:
    """session_id attributes every real call this turn makes (M8: "zero
    unattributed calls") - use engine.m8.usage.SYSTEM_SESSION_ID for a
    non-session evidence run, never a blank string.

    already_told_ids feeds evidence assembly's Stage E (session exclusion,
    design §3.2) - story/quote ids the M4 event log already shows this
    session as told. Optional and caller-supplied rather than derived here:
    this module makes no store reads of its own (mirrors "makes no store
    writes of its own" above) - a caller with the real event log queries it
    and passes the set in; omitting it just means Stage E is a no-op.

    already_bridged_figure_ids is the same shape and the same reason, for
    engine.m4.name_bridge.find_figures_used: figure ids this session's
    transcript already shows in a prior turn's figures_used, so a name
    bridged once does not fire again (Full UX Design §2.4/§5.7's
    "first-occurrence term" grammar, applied to names the same as lexicon
    terms). The same set also reaches the VOICE: it is
    resolved to spoken names and rendered into the evidence block as an
    already-introduced line (a pilot read found both Chloe turns opened
    "One of us, Ignatius"; the screen knew he was introduced, the voice
    did not). Caller-supplied for the identical reason as
    already_told_ids; omitting it means every matching figure fires every
    time it's named AND the voice is never told a name is already known -
    safe, but both channels get noisier than intended.

    already_bridged_gloss_ids is the same shape again, for
    engine.m4.term_glosses.find_glosses_used: term record ids this
    session's transcript already shows glossed. Same first-occurrence
    grammar, same caller-supplied/optional contract, same consequence of
    omitting it.

    track_a_last mirrors track_b_accumulator's own shape - the caller's
    SessionState.safety.track_a_last (None until Track A has fired once
    this session, per engine.m4.projection). Read only to decide which of
    Track A's three scripts to speak (crisis_resources.resources_for_signal);
    never fed to the sealed safety call, same discipline track_b_accumulator
    already holds and for the same SS210 reason (see
    engine.m5.safety_accumulation's own module docstring).

    The enforce flag and known_tradition_names (the uncited-claims rule's
    flag-gated enforcement) and sentence_enforce (sentence_fact_check's
    own, independent flag-gated enforcement): threaded straight through to
    every _run_ordinary_voice_turn call this
    function makes (the ordinary path and the bridge route both generate
    a real voice answer that can carry the same offenses) - see that
    function's own docstring for the full enforcement shape of each. All
    default off/None, byte-identical to before any of them existed.

    daily_cap_reached is engine.api.anon_cap's verdict that this visitor
    has used today's message allowance. It closes the session the same way
    the session turn cap does, at the same point, and a real crisis is
    exempt from it the same way.

    turn_cap is how many completed voice turns this sitting may hold, and
    facilitator_only makes the sitting answer through the Facilitator with no
    voice call; both come from engine.m4.grants and default to the free
    allowance. A sitting held to either limit still gives a safety route its
    Facilitator turn.

    on_sentence is passed to the two plain voice routes only. The bridge
    route is left out on purpose: its Facilitator turn is read before the
    voice, so a voice sentence shown first would arrive out of order."""
    # The gate pass, extracted whole to run_gate (Artifact-7 - a table
    # round gates once per message, then runs several voice turns
    # against the same decision). The locals below keep their old names so
    # every branch under them is untouched.
    gate_run = run_gate(
        session_id=session_id,
        safety_client=safety_client,
        safety_model_id=safety_model_id,
        participant_message=participant_message,
        pressed=pressed,
        anachronistic_term_ids=anachronistic_term_ids,
        track_b_accumulator=track_b_accumulator,
    )
    usage_records = list(gate_run.usage_records)
    safety_outcome = gate_run.safety_outcome
    reader_outcome = gate_run.reader_outcome
    gate_result = gate_run.gate_result
    action = gate_result.routing.action
    gate = gate_run.gate
    safety_states = gate_run.safety_state_events

    # THE CAP OVERRIDES EVERYTHING EXCEPT A REAL CRISIS. Checked once, here,
    # after routing but before any branch spends a voice call - so a capped
    # turn costs only the two Haiku gate calls already made above, never the
    # Sonnet generation call. ACUTE_DISTRESS is the one action that must
    # never be capped away: a participant in real crisis at turn 11 still
    # gets the safety turn, not a redirect. Every other action - the ordinary
    # voice path, Track B's non-acute safety_turn, bridge/etic/check-in/
    # system-nature - is something a capped session stops doing uniformly,
    # not selectively, so the ending reads as one clear boundary rather than
    # a handful of routes quietly behaving differently.
    # Every safety route is exempt from both caps, not acute distress
    # alone: a check-in (an uncertain or failed safety call) and a
    # dependency check are safety turns too, and a limit must never turn
    # them away (System Hub decision 35).
    is_safety_route = action in SAFETY_ROUTES
    if not is_safety_route and (daily_cap_reached or facilitator_only):
        return TurnResult(
            routing_action="session_cap_turn", routing_reason="visitor daily message cap reached",
            gate=gate, safety_state_events=safety_states,
            facilitator_events=[facilitator_turns.daily_cap_turn(limit_text)],
            degraded=gate_result.degraded, usage_records=usage_records,
        )
    turn_cap = SESSION_TURN_CAP if turn_cap is None else turn_cap
    if not is_safety_route and len(history or []) // 2 >= turn_cap:
        return TurnResult(
            routing_action="session_cap_turn", routing_reason=f"session turn cap reached ({turn_cap} turns)",
            gate=gate, safety_state_events=safety_states,
            facilitator_events=[facilitator_turns.session_cap_turn(world.frame["representative"]["name"], limit_text)],
            degraded=gate_result.degraded, usage_records=usage_records,
        )

    if action in SAFETY_ROUTES:
        return TurnResult(
            routing_action=action, routing_reason=gate_result.routing.reason,
            gate=gate, safety_state_events=safety_states,
            facilitator_events=safety_route_facilitator_events(
                gate_run, representative_name=world.frame["representative"]["name"], track_a_last=track_a_last,
            ),
            voice_event=None, degraded=gate_result.degraded, usage_records=usage_records,
        )

    if action == "system_nature_turn":
        # "immediately" (Artifact-4 SS3 rule 3) means the voice is not asked
        # anything - a question about what the system IS is not a question
        # any world can answer, and letting a world try is the failure this
        # route exists to prevent.
        return TurnResult(
            routing_action=action, routing_reason=gate_result.routing.reason,
            gate=gate, safety_state_events=safety_states,
            facilitator_events=[facilitator_turns.system_nature_turn()],
            degraded=gate_result.degraded, usage_records=usage_records,
        )

    if action == "etic_turn":
        return TurnResult(
            routing_action=action, routing_reason=gate_result.routing.reason,
            gate=gate, safety_state_events=safety_states,
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
        facilitator_event, underlying_subject = facilitator_turns.bridge_turn(fired, fleet)
        # WHAT ELSE THE PARTICIPANT ASKED. The bridge route carries no
        # directive of its own (engine.m5.routing), so a message that asks
        # two things - one carrying the modern word, one not - must still
        # carry the second ask to the voice alongside the underlying
        # subject, not the underlying subject alone. Barring the word is
        # the rule; barring the rest of the sentence is not. The fired
        # records' own display_terms
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
            session_id=session_id, already_told_ids=already_told_ids,
            already_bridged_figure_ids=already_bridged_figure_ids,
            already_bridged_gloss_ids=already_bridged_gloss_ids, history=history,
            previous_kind=previous_kind,
            rhythm=rhythm,
            r27_enforce=r27_enforce, known_tradition_names=known_tradition_names,
            self_revision_enabled=self_revision_enabled, sentence_enforce=sentence_enforce,
            citation_attach_model_id=safety_model_id if citation_attach_enabled else None,
        )
        return TurnResult(
            routing_action=action, routing_reason=gate_result.routing.reason,
            gate=gate, safety_state_events=safety_states,
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
            already_bridged_figure_ids=already_bridged_figure_ids,
            already_bridged_gloss_ids=already_bridged_gloss_ids,
            history=history,
            previous_kind=previous_kind,
            rhythm=rhythm,
            is_other_tradition_first_ask=(gate_result.routing.out_of_scope_class == "other_tradition"),
            other_tradition_evidence_ids=other_tradition_evidence_ids,
            other_tradition_known_in_window=other_tradition_known_in_window,
            other_tradition_revealed=other_tradition_revealed,
            r27_enforce=r27_enforce, known_tradition_names=known_tradition_names,
            self_revision_enabled=self_revision_enabled, sentence_enforce=sentence_enforce,
            on_sentence=on_sentence,
            citation_attach_model_id=safety_model_id if citation_attach_enabled else None,
        )
        return TurnResult(
            routing_action=action,
            gate=gate, safety_state_events=safety_states,
            routing_reason=gate_result.routing.reason,
            voice_event=voice_event,
            degraded=gate_result.degraded,
            usage_records=usage_records + voice_usage_records,
        )

    raise UnhandledRoutingAction(f"routing action {action!r} has no generation content wired up yet - see module docstring")
