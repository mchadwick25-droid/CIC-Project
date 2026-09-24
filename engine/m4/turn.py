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
every world's voice to emit - engine.m4.generation.call_citations is
deleted, not merely unused. engine.m4.grounding (the excerpt-match badge
check against a claimed `drawn_on` list) is untouched and no longer this
module's net - that list doesn't exist anymore now that citations are
never guessed after the fact. engine.m4.grounding_net.check_turn is the
new net: per-sentence, string-only, no model call, run over the raw
tagged text before any of it is treated as this turn's answer.

Fork 1 (sentence-gated streaming) is honored in its strictest reading
here, not a looser one: no live token-by-token SSE transport exists yet
in this codebase, so stream_voice_turn already returns full text
only once the SDK call completes, never incrementally. Given that, "check
before it reaches a participant" reduces exactly to what apply_net does
below: every sentence is verified before ANY of this turn's text is
placed on TurnResult.voice_event. When a real per-token transport is
built, sentence-gating moves into that layer; the check itself does not
change.
"""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field

from engine.m1.loader import load_fleet_records
from engine.m4 import crisis_resources, evidence, facilitator_turns, grounding_net
from engine.m4.generation import stream_voice_turn
from engine.m4.grounding import find_do_not_voice_violation
from engine.m4.citation_cards import resolve_citation_sources
from engine.m4.output_check import check_output
from engine.m4.seat_identity_guard import find_seat_identity_violation
from engine.m4.self_revision import self_revise
from engine.m4.uncited_claims import classify_neighbour_named, find_uncited_claims, find_uncited_paragraphs
from engine.m4.name_bridge import attach_cited_sources, find_figures_used, spoken_name
from engine.m4.term_glosses import find_glosses_used
from engine.m4.transparency_plan import build_transparency_plan
from engine.m4.world_loader import LoadedWorld
from engine.m5 import live_calls
from engine.m5.anachronism import resolve_term_ids, terms_in_message
from engine.m5.failure import CallOutcome, resolve_gate
from engine.m5.safety_accumulation import safety_state_events
from engine.m5.routing import Directive, directive_without_terms
from engine.m8.usage import UsageRecord, record_usage


SESSION_TURN_CAP = 10  # reference/Redesign-Spec/Artifact-6-Operations.md "per-session turn cap" (was DECIDABLE, default 40) - resolved to 10 after the live memory-growth measurement (engine/m8/live_memory_growth_run.py) showed real per-turn cost climbing, not flat, as session history accumulates. Counted in completed VOICE turns (len(history)//2), the same unit that actually drives the cost growth - a session's history is built by engine.api.wiring.history_from_transcript, which only pairs a participant message with a turn that got a real Representative reply, so facilitator-only turns (safety check-ins, system-nature, etc.) do not themselves consume the cap.


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

    if rec := _maybe_record_usage(safety_outcome, session_id=session_id, call_kind="safety_call", model_id=safety_model_id):
        usage_records.append(rec)
    if rec := _maybe_record_usage(reader_outcome, session_id=session_id, call_kind="reader_call", model_id=safety_model_id):
        usage_records.append(rec)

    # WHICH MODERN TERMS ARE IN PLAY, settled here once, before anything
    # downstream reads them - so routing's intersection and the bridge's
    # re-derivation below see the same list instead of each deriving one.
    # Two passes, and the second is not a belt-and-braces duplicate of the
    # first; they fix different failures, both measured live:
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


R26_HONEST_LIMIT_SENTENCE = "Our record doesn't mention that Christian tradition."


def _revealed_excerpts_block(revealed_excerpts: list[tuple[str, str]] | None) -> str | None:
    """R37(b) and R37-B's quoted-lines block: exactly what this
    conversation has said about the named tradition, speaker by speaker,
    word for word (engine.m4.uncited_claims.conversation_revealed_
    excerpts). A separate, labelled block in the private directive - never
    folded into history, which keeps engine.api.wiring.history_from_
    transcript's own Facilitator exclusion intact. None when nothing has
    been said."""
    if not revealed_excerpts:
        return None
    lines = "\n".join(f'- {who}: "{sentence}"' for who, sentence in revealed_excerpts)
    return (
        "What this conversation has actually said about that tradition, word for word:\n"
        f"{lines}\n"
        "That is everything you have been told about it here. Use nothing beyond these words."
    )


def _pivot_scope_clause(known_in_window: bool | None, *, has_excerpts: bool, seated: bool = False) -> str:
    """R37's own rule for the pivot - which part of this world's own
    record the answer comes from - on a question naming a tradition the
    record does not cover. known_in_window is engine.m4.uncited_claims.
    tradition_known_in_window's result (R37 condition (a), R37-A's
    asymmetric reading); None means the question named no registry
    tradition at all (e.g. "the Arians"), so nothing establishes the
    knowledge either way and the text says only that. has_excerpts is
    condition (b): the quoted-lines block rides alongside. seated: the
    named tradition's own chair is at this table, and everything it says
    is itself something this conversation told the voice (R37-B), named
    or not - so its speech is a source alongside the quoted lines, as the
    seated branch's own text already allows. Neither condition: the
    question's own words alone. Every branch keeps the
    ruling's standing limit - content about the other tradition never
    enters the answer from outside the record."""
    sources = ["the question's own words"]
    if seated:
        sources.append("what that chair has said")
    if has_excerpts:
        sources.append("the lines quoted below")
    sources_text = sources[0] if len(sources) == 1 else f"{', '.join(sources[:-1])} and {sources[-1]}"
    if known_in_window:
        return (
            "Your own world could have known of that tradition in its own time, so you may let that knowledge "
            "guide which part of your own record you answer from. It never lets you say anything about that "
            "tradition itself beyond what your own records hold and what this conversation has told you."
        )
    if known_in_window is False:
        opening = "That tradition arose after your own world's time, so you cannot have known of it."
    else:
        opening = "Nothing establishes that your own world knew of that tradition in its own time."
    return (
        f"{opening} Choose which part of your own record to answer from using only {sources_text} - "
        "never outside knowledge of that tradition."
    )


def _other_tradition_directive(
    evidence_record_ids: list[str] | None = None,
    *,
    tradition_seated: bool = False,
    tradition_seated_name: str | None = None,
    repeat_turn: bool = False,
    known_in_window: bool | None = None,
    revealed_excerpts: list[tuple[str, str]] | None = None,
) -> str | None:
    """R26, the project lead's own words: "The representative should only
    know its own sources unless they would have known the sources from
    another in reality." This is the directive text an other_tradition
    first ask now carries - see _build_turn_directive's own
    is_other_tradition_first_ask parameter. The fixed sentence here is
    engine.m4.uncited_claims.R26_HONEST_LIMIT_SENTENCE, matched exactly
    (case-insensitive) by that module's own allowed-uncited detection -
    the two must stay identical by construction, not by convention.
    Always returns real text when called (never None - see
    tradition_seated's own note below for why that changed).

    evidence_record_ids (the R39 fix that lets a world's own records stand
    in for the honest limit when they already speak to the question):
    engine.m4.uncited_claims.world_records_mention_tradition's own
    result - record ids in THIS world's own package that already,
    genuinely name the tradition asked about. R26's own ruling already
    named this exception ("unless they would have known the sources from
    another in reality"); only the mechanism was missing until now. Empty
    or None (the true "never heard of this tradition" case, e.g. alx on
    Donatism) keeps the fixed honest-limit sentence exactly as it always
    was - nothing here changes that branch. A nonempty list (e.g. ijc on
    Donatism, whose own ijc.quote.compelled-to-come-in and
    ijc.story.emperor-builds-another-basilica already name it) skips the
    honest-limit sentence entirely, since saying it would be false, and
    hands the voice those record ids as its own ground instead - cited
    under the ordinary citation contract, the same as any other turn.

    tradition_seated (the Table-parity fix): the named tradition's own
    world is SEATED at this table - the fixed honest-limit sentence
    would be false (this seat's neighbour speaks for that tradition
    directly, right there), so it is never said regardless of evidence.
    The evidence branch above still applies if this seat's own records
    happen to name it (unchanged).

    The first version of this fix returned None here with no evidence,
    reasoning that the Table's own seat-to-seat clause (table_engagement)
    already governed. That was wrong, and catching it exposed a real
    failure it produces, not just a missing belt-and-suspenders:
    table_engagement is built only when other_voice_has_spoken
    (_table_engagement_directive's own docstring) - NEVER on a round's
    true opening turn. The opening turn is exactly the turn that names
    the seated tradition in the first place, so returning None there
    left the model completely ungoverned on it. The live battery's own
    OT3 probe caught the real result: asked about the seated tradition by
    its card name, the voice answered "we were it" - claiming that
    tradition's own name and witness as its own, the exact thing R37
    forbids. tradition_seated_name (the seated tradition's own registry
    card_name, passed through from table_wiring.py so this function
    never has to know about the registry itself) now carries a real
    directive instead: this seat may respond only to the bare fact that
    a tradition under that name is seated here with its own
    Representative, and to what that chair has actually said in this
    conversation so far (R37(b), the project lead's own words: "only if
    it would have known in its own time, or if something was revealed in
    the facilitator's introduction or user, but limited only to what was
    told to them in the conversation") - never claiming that tradition's
    own name, history, or witness as this seat's own.

    repeat_turn (the same Table-parity fix): this seat's own SECOND OR
    LATER turn within the same round (turn_selector may draw a seat back
    in - the fixed sentence said once already stays true, but repeating
    it verbatim every return turn is not what interview's own single-ask
    shape ever produces). No evidence, not seated: keep R37's own
    knowledge-scope framing ("this is another tradition, answer only
    from your own records") but drop the "if nothing, say exactly..."
    clause - it was already said on this seat's first turn this round.

    known_in_window and revealed_excerpts (the R37 build): the pivot
    itself. The project lead's own words: "only if it would have known
    in its own time, or if something what revealed in the facilitators
    introduction or user, but limited only to what was told to them in
    the conversation" - and R37-B, "add or what another representitive
    revials in the conversation". known_in_window is condition (a);
    revealed_excerpts is condition (b) with R37-B's third source - see
    _pivot_scope_clause and _revealed_excerpts_block. The no-evidence
    branches each carry both. The evidence branch carries only the
    quoted lines: there the world's own records already name the
    tradition, so the record itself is the ground for the pivot. None of
    this changes R26_HONEST_LIMIT_SENTENCE or when it is said - under
    (a) the record still does not mention the tradition, so the sentence
    stays true."""
    excerpts_block = _revealed_excerpts_block(revealed_excerpts)
    if evidence_record_ids:
        ids_text = ", ".join(f"[[{rid}]]" for rid in evidence_record_ids)
        text = (
            "This question asks about another Christian tradition, not your own world - but your own "
            f"records already speak to it: {ids_text}. Answer from what those records actually say, cited "
            "as always, under the ordinary citation contract. Never speak as if you know more about that "
            "other tradition than what your own records give you and what has actually been said in this "
            "conversation."
        )
        return f"{text}\n{excerpts_block}" if excerpts_block else text
    scope = _pivot_scope_clause(known_in_window, has_excerpts=excerpts_block is not None, seated=tradition_seated)
    if tradition_seated:
        name_text = f' under the name "{tradition_seated_name}"' if tradition_seated_name else ""
        text = (
            f"This question asks about a Christian tradition seated at this table{name_text}, with its own "
            "Representative present - not your own world. Never speak for that tradition, and never claim "
            "its name, history, or witness as your own. You may respond only to the bare fact that it is "
            "seated here under that name, to what that chair has actually said in this conversation so "
            "far, and to what anyone else here has said about it - if nobody has, you know nothing more "
            "about it than its name. Where your own world's records genuinely bear on the question, answer "
            "from them as always, cited as always, but never let that stand in for the other tradition's "
            f"own voice. {scope}"
        )
    elif repeat_turn:
        text = (
            "This question asks about another Christian tradition, not your own world. Answer only from "
            "what your own world's records actually hold about it, cited as always. Never speak as if you "
            "know that other tradition's own history or doctrine - only your own, and only what you can "
            f"cite. {scope}"
        )
    else:
        text = (
            "This question asks about another Christian tradition, not your own world. Answer only from what "
            "your own world's records actually hold about it. If your own records say nothing about the "
            f'tradition named, say exactly: "{R26_HONEST_LIMIT_SENTENCE}" Then answer the rest of the question '
            "from your own records, cited as always. Never speak as if you know that other tradition's own "
            f"history or doctrine - only your own, and only what you can cite. {scope}"
        )
    return f"{text}\n{excerpts_block}" if excerpts_block else text


def _build_turn_directive(
    directive: Directive | None,
    figures_already_named: list[str] | None = None,
    table_engagement: str | None = None,
    is_other_tradition_first_ask: bool = False,
    other_tradition_evidence_ids: list[str] | None = None,
    other_tradition_seated: bool = False,
    other_tradition_seated_name: str | None = None,
    other_tradition_repeat_turn: bool = False,
    other_tradition_known_in_window: bool | None = None,
    other_tradition_revealed: list[tuple[str, str]] | None = None,
) -> str | None:
    """The per-turn half of the voice's system prompt, on its own - the
    world's compiled prompt is passed separately and unmodified, so that it
    stays byte-identical across a session and the cache prefix actually
    holds (see stream_voice_turn's docstring). This text changes every
    turn, so it must never be concatenated onto the cached half.

    table_engagement (bug fix for Table mode giving
    independent monologues instead of cross-voice engagement on broad
    questions): the Table's per-turn behavioral rule - engage what another
    voice just said, stay in your own witness, keep it compact - belongs
    HERE, not in the user-message context_prefix it used to live in
    entirely. That was the actual bug: the ambiguity_options note below
    already proved this channel wins over a competing pressure sitting in
    the user turn ("it sits after register statement 1 in the prompt, so it
    won"); the Table's engagement instruction was sitting in the weaker
    channel the whole time, ahead of a per-question evidence block that
    scales with how broad the question is and right before the bare
    participant message itself - exactly the position the ambiguity_options
    finding already showed losing. None on every interview call and on a
    table call's true opening turn (nothing said yet to engage), so both
    paths are unchanged there. table_wiring.py still builds the pending
    speech itself into context_prefix (real conversational content, not an
    instruction) - only the behavioral rule about it moved.

    Returns None only when there is no directive, no table_engagement, and
    is_other_tradition_first_ask is False (the crisis path), which leaves
    the call with the world prompt alone - exactly what it sent before.
    other_tradition_seated (the Table-parity fix): _other_
    tradition_directive ALWAYS returns real text now, never None - a
    round's opening turn never gets table_engagement (built only when
    other_voice_has_spoken, see _table_engagement_directive's own
    docstring), so an other-tradition-only opening turn with the named
    tradition seated and no evidence used to reach the model completely
    ungoverned: nothing told it the tradition it was just asked about is
    the seat beside it, and the live battery caught the real failure this
    produces - the voice claimed the seated tradition's own name and
    witness as its own, exactly what R37 forbids. There is no genuinely
    redundant case left to return None for: table_engagement (when it
    does fire, on a later turn) is a different job entirely (engage what
    was just said) and composes with this branch rather than
    duplicating it."""
    if directive is None and not table_engagement and not is_other_tradition_first_ask:
        return None
    # The leading newline is kept from when this text was concatenated onto
    # the world prompt: system blocks are joined with no separator of their
    # own, so dropping it would run the heading onto the prompt's last line.
    # The model must see exactly the bytes it saw before this split.
    parts = ["\n## This turn's private directive (never shown to the participant)"]
    if directive is not None:
        asks_text = "; ".join(a["text"] for a in directive.asks) if directive.asks else "(none extracted)"
        parts.append(f"Asks, in order: {asks_text}")
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
        if figures_already_named:
            # The directive channel is the one measured to win over other
            # pressures (see the ambiguity_options note above). Three live
            # probes showed the evidence block's own already-introduced
            # header losing to a ground record's first-mention opening
            # ("One of us, Ignatius" reproduced verbatim on turn two) - the
            # signal belongs here, where the voice actually shapes the turn.
            parts.append(
                f"Already introduced in this conversation: {', '.join(figures_already_named)}. "
                "The participant has met these names. A ground record that presents one of them afresh is "
                "written for a first mention; this turn is not one - carry the name as someone already "
                "known ('Ignatius also said...' is the shape), never re-introduced as if new."
            )
    if table_engagement:
        parts.append(table_engagement)
    if is_other_tradition_first_ask:
        other_tradition_text = _other_tradition_directive(
            other_tradition_evidence_ids,
            tradition_seated=other_tradition_seated,
            tradition_seated_name=other_tradition_seated_name,
            repeat_turn=other_tradition_repeat_turn,
            known_in_window=other_tradition_known_in_window,
            revealed_excerpts=other_tradition_revealed,
        )
        if other_tradition_text:
            parts.append(other_tradition_text)
    if len(parts) == 1:
        # Nothing was actually added. _other_tradition_directive always
        # returns real text now when called (round-2 review fix - see
        # this function's own docstring), so this path is only reachable
        # when is_other_tradition_first_ask is False and directive/
        # table_engagement were both falsy too - the header line alone is
        # not a real directive, return None exactly as the no-directive
        # path above does.
        return None
    return "\n".join(parts)


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
    """R27's own one regeneration: same append-not-replace channel and
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


def apply_net(raw_text: str, *, repository_records: dict[str, dict], thin_topics: list[dict] | None) -> tuple[str, list[dict], dict]:
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
    # R27: calls check_turn_with_paragraph_coverage instead of check_turn
    # - proven equivalent on "sentences"/"substantive_survives"/
    # "truncated" (test_grounding_net.py's own equivalence test), so
    # text/citations below are unchanged; net_result now additionally
    # carries "paragraph_coverage", unused by any reader that doesn't ask
    # for it. This is the single-pass fold: _run_ordinary_voice_turn
    # below reads paragraph coverage off THIS SAME net_result rather than
    # making a second, independent check_turn_with_paragraph_coverage
    # call - a live turn now pays the net once, not twice, in both
    # report-only and enforced modes.
    net_result = grounding_net.check_turn_with_paragraph_coverage(raw_text, repository_records, thin_topics=thin_topics)
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
    already_bridged_figure_ids: set[str] | None = None,
    already_bridged_gloss_ids: set[str] | None = None,
    history: list[dict] | None = None,
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

    correction (R27 fix F3): free text appended onto whatever
    _build_turn_directive already produced, same channel and same
    append-not-replace shape as _append_seat_identity_correction. None
    on every real caller
    (engine.api.wiring, engine.api.table_wiring never pass it - "battery-
    only, no participant path" is the fix list's own words) - it exists
    so engine.m4.live_uncited_claims_battery can simulate one regeneration
    naming a turn's own uncited sentences without duplicating this
    function's evidence-assembly/generation logic in the battery script
    itself. Purely additive: unset, this parameter changes nothing.

    debug_capture (R27 fix F6): an optional caller-supplied dict this
    function mutates in place, setting "raw_tagged_text" to the exact
    text apply_net is about to check -
    same battery-only, unset-on-every-real-caller shape as correction
    above. Never part of voice_event (no schema key for it, so it can
    never reach the real event log through this channel) - exists so the
    battery can compute paragraph-level citation coverage from the same
    raw text apply_net already has, without a second model call or a
    second copy of this function's own generation logic.

    r27_enforce/known_tradition_names (R27's flag-gated enforcement):
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
    already sets raw_text="" above) and r27_enforcement_exhausted is
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
    r27_enforce is True (fails loudly rather than silently skipping the
    neighbour_named check if omitted) - the same pre-derived list
    engine.m4.uncited_claims.known_tradition_names already produces for
    the report-only build_uncited_claims_event path, computed by the
    caller (which has registry access this function does not) and
    passed straight through.

    other_tradition_evidence_ids (the R39 fix that corrects a false
    honest-limit statement, unconditional - never gated behind
    r27_enforce, since this corrects an existing false statement rather
    than adding new enforcement): engine.m4.uncited_claims.world_records_
    mention_tradition's own result for the tradition THIS turn's message
    names, if any - same caller-computed, registry-access-needed shape
    as known_tradition_names. Read only inside _build_turn_directive,
    only when is_other_tradition_first_ask is also true; harmless (and
    correctly ignored) to pass on any other turn.

    other_tradition_known_in_window and other_tradition_revealed (the
    R37 build): engine.m4.uncited_claims.tradition_known_in_window and
    conversation_revealed_excerpts, for the same named tradition - the
    same caller-computed shape as other_tradition_evidence_ids, read at
    the same single place (_other_tradition_directive)."""
    if r27_enforce and known_tradition_names is None:
        raise ValueError(
            "r27_enforce=True requires known_tradition_names (see engine.m4.uncited_claims.known_tradition_names) "
            "- never guess the neighbour_named check's own name list"
        )
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
    # The same set that keeps the UI's figure mark first-occurrence-only,
    # resolved to spoken names and put where the VOICE can see it too
    # (a pilot read found the session tracked a figure's introduction to
    # the conversation, but only the screen knew - the voice itself was
    # never told).
    figures_already_named = [
        name
        for figure in (world.figures.get("figures") or [])
        if figure.get("id") in (already_bridged_figure_ids or set())
        and (name := spoken_name(figure))
    ]
    turn_evidence = evidence.assemble_evidence(
        message=participant_message,
        asks=directive.asks if directive else None,
        canon_questions=canon_questions,
        coverage=world.coverage,
        repository_records=repository_records,
        thin_topics=thin_topics,
        already_told_ids=already_told_ids,
        history=history,
        figures_already_named=figures_already_named,
        secondary_context=secondary_context,
    )
    evidence_block = evidence.render_evidence_block(turn_evidence)
    user_message = f"{evidence_block}\n{participant_message}" if turn_evidence["candidates"] else participant_message
    if context_prefix:
        user_message = f"{context_prefix}\n\n{user_message}"

    turn_directive = _build_turn_directive(
        directive, figures_already_named, table_engagement,
        is_other_tradition_first_ask=is_other_tradition_first_ask,
        other_tradition_evidence_ids=other_tradition_evidence_ids,
        other_tradition_seated=other_tradition_seated,
        other_tradition_seated_name=other_tradition_seated_name,
        other_tradition_repeat_turn=other_tradition_repeat_turn,
        other_tradition_known_in_window=other_tradition_known_in_window,
        other_tradition_revealed=other_tradition_revealed,
    )
    if correction:
        turn_directive = (turn_directive or "") + correction
    stream_outcome = stream_voice_turn(
        voice_client, voice_model_id, system_prompt=world.prompt_text,
        turn_directive=turn_directive, message=user_message, history=history,
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
    offending = find_seat_identity_violation(raw_text, guard_labels) if guard_labels else None
    if offending:
        seat_identity_violations.append({"world_key": world.world_key, "offending_prefix": offending, "attempt": "first"})
        retry_outcome = stream_voice_turn(
            voice_client, voice_model_id, system_prompt=world.prompt_text,
            turn_directive=_append_seat_identity_correction(turn_directive, offending),
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

    # SELF-REVISION (R38, measured 0/20 real leaks) - the generation-side
    # fix for a fabricated detail riding a real citation tag,
    # engine.m4.self_revision's own module docstring carries the full
    # mechanism and the 7b/R30 compatibility note. Runs only on
    # other_tradition-routed turns (is_other_tradition_first_ask), where
    # the leak class lives, and only when the draft survived the seat-
    # identity guard above (raw_text is never truthy after that guard's
    # own exhaustion path, so this never spends a call revising a blank
    # turn). self_revision_enabled is the caller-computed CIC_SELF_
    # REVISION kill-switch (engine.api.config, same pattern as
    # r27_enforce/CIC_R27_ENFORCE) - default True, cost/incident use
    # only; unlike r27_enforce this is generation, not enforcement, so
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
        # R27 F6: the raw, still-tagged, still-paragraphed answer - never
        # part of voice_event (no schema key for it, never persisted to
        # the real event log), a side channel purely for
        # engine.m4.live_uncited_claims_battery to compute
        # paragraph-coverage from, the same "mutate a caller-supplied
        # dict, opt-in, unset on every real caller" shape `correction`
        # already uses. This is the exact text apply_net is about to
        # strip and check below - nothing recomputed, nothing
        # re-derived.
        debug_capture["raw_tagged_text"] = raw_text

    answer_text, citations, net_result = apply_net(raw_text, repository_records=repository_records, thin_topics=thin_topics)

    # R27: report-only, no participant-visible effect unless r27_enforce
    # (below), every declarative claim sentence carrying no citation,
    # base class "uncited_claim" (the caller, which has registry/routing
    # context this function does not, refines into "neighbour_named"/
    # "own_doctrine_in_other_tradition_turn" via engine.m4.uncited_claims.
    # classify_* before persisting the uncited_claims event). Runs on
    # net_result's own sentence list, not a second pass over the text.
    uncited_claims = find_uncited_claims(net_result["sentences"])

    # paragraph_coverage now rides on THIS SAME net_result (apply_net
    # calls check_turn_with_paragraph_coverage - see that function's own
    # docstring) rather than a second, independent
    # check_turn_with_paragraph_coverage call - the net runs once per
    # attempt, not twice, folded into the R27 enforcement pass below.
    # Only the FINISHED paragraph_offenses list rides on voice_event, not
    # the whole net_result: that result's own per-sentence verdict dump
    # is real analysis weight with no reason to sit in the permanent
    # event log forever; find_uncited_paragraphs reduces it to the same
    # small {sentence, class} shape uncited_claims already uses.
    paragraph_offenses = find_uncited_paragraphs(net_result)

    # R27's flag-gated enforcement, OFF by default (see this function's
    # own docstring for the full shape). r27_enforcement_exhausted
    # and attempts_meta["r27_regenerated"] are always set (False/absent
    # when r27_enforce is False or nothing tripped it), so every reader of
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
            retry_answer_text, retry_citations, retry_net_result = apply_net(
                retry_raw_text, repository_records=repository_records, thin_topics=thin_topics
            )
            retry_uncited_claims = find_uncited_claims(retry_net_result["sentences"])
            retry_paragraph_offenses = find_uncited_paragraphs(retry_net_result)
            retry_refined = [classify_neighbour_named(o, known_tradition_names) for o in retry_uncited_claims]
            retry_hard_offenses = [o for o in retry_paragraph_offenses if o["class"] == "wholly_uncited_paragraph"] + [
                o for o in retry_refined if o["class"] == "neighbour_named"
            ]
            if retry_hard_offenses:
                r27_enforcement_exhausted = True
                raw_text = ""  # the voice's text is not shown - the caller substitutes a Facilitator turn
                answer_text, citations, net_result = apply_net("", repository_records=repository_records, thin_topics=thin_topics)
                uncited_claims = []
                paragraph_offenses = []
            else:
                raw_text = retry_raw_text
                answer_text, citations, net_result = retry_answer_text, retry_citations, retry_net_result
                uncited_claims = retry_uncited_claims
                paragraph_offenses = retry_paragraph_offenses
        else:
            attempts_meta_r27_regenerated = False
    else:
        attempts_meta_r27_regenerated = False

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

    do_not_voice_hit = find_do_not_voice_violation(answer_text=answer_text, quotes=world.quotes["quotes"])

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
        # r27_regenerated: whether R27's own enforcement attempted the one
        # allowed regeneration this turn - False when r27_enforce is off
        # (every real caller until the flag is flipped on) or when
        # nothing hard-failed on the raw attempt. attempts_meta carries
        # no schema-validated shape (engine.m4.events' REQUIRED_KEYS only
        # requires the key's presence), so this rides here rather than
        # needing a catalog change.
        "attempts_meta": {
            "empty_stream_retries": 0, "r27_regenerated": attempts_meta_r27_regenerated,
            "self_revision": self_revision_meta,
        },
        "grounding": net_result,
        "transparency": transparency,
        "do_not_voice_violation": do_not_voice_hit,
        "degraded_by_net": degraded_by_net,
        # The finished string, checked last, after the net has cut and the
        # fallback has appended - because that is the only text a person
        # actually reads, and until now nothing looked at it. Reports,
        # never edits (Program-Spec M4: never by editing a live response);
        # a finding here means something UPSTREAM is wrong.
        "output_defects": check_output(
            answer_text, history=history, participant_message=participant_message,
            citations=citations, repository_records=repository_records,
        ),
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
        # R27, additive: [] on every clean turn. Base class
        # "uncited_claim" only - see this function's own note above.
        "uncited_claims": uncited_claims,
        # Additive: [] on every clean turn, same shape/scale discipline
        # as uncited_claims above - base classes
        # "wholly_uncited_paragraph"/"inherited_ungrounded" only; the
        # caller (registry/routing context this function doesn't have)
        # cross-references this against "uncited_claims" to narrow
        # "own_doctrine_in_other_tradition_turn".
        "paragraph_offenses": paragraph_offenses,
        # R27's flag-gated enforcement, additive: False unless
        # r27_enforce was on AND the one allowed regeneration still left
        # a hard offense (wholly_uncited_paragraph or neighbour_named)
        # standing. True means answer_text is deliberately "" (the
        # voice's text is not shown), uncited_claims/paragraph_offenses
        # are both [] (there is nothing left to report on an unshown
        # turn) - the caller substitutes a facilitator_turn, the exact
        # same shape seat_identity_guard_exhausted already uses above.
        "r27_enforcement_exhausted": r27_enforcement_exhausted,
    }
    return voice_event, usage_records


# Artifact-7 SS3: the Table's per-voice runner IS the interview's ordinary
# path, scoped to one world - same compiled prompt as cached prefix, same
# evidence assembly from that world's own coverage/repository, same
# grounding net against that world's own records. The isolation property
# falls out of this line: a table voice turn simply has no other world in
# scope. Exposed as a public name rather than duplicated, so the two modes
# can never drift apart.
run_voice_turn_for_world = _run_ordinary_voice_turn


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
    r27_enforce: bool = False,
    known_tradition_names: list[str] | None = None,
    other_tradition_evidence_ids: list[str] | None = None,
    other_tradition_known_in_window: bool | None = None,
    other_tradition_revealed: list[tuple[str, str]] | None = None,
    self_revision_enabled: bool = True,
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

    r27_enforce/known_tradition_names (R27's flag-gated enforcement):
    threaded straight through to every _run_ordinary_voice_turn call this
    function makes (the ordinary path and the bridge route both generate
    a real voice answer that can carry the same offenses) - see that
    function's own docstring for the full enforcement shape. Both default
    off/None, byte-identical to before either existed."""
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
    is_acute_crisis = action == "safety_turn" and not safety_outcome.failed and safety_outcome.value.get("signal") == "ACUTE_DISTRESS"
    if not is_acute_crisis and len(history or []) // 2 >= SESSION_TURN_CAP:
        return TurnResult(
            routing_action="session_cap_turn", routing_reason=f"session turn cap reached ({SESSION_TURN_CAP} turns)",
            gate=gate, safety_state_events=safety_states,
            facilitator_events=[facilitator_turns.session_cap_turn(world.frame["representative"]["name"])],
            degraded=gate_result.degraded, usage_records=usage_records,
        )

    if action == "safety_turn":
        signal = safety_outcome.value["signal"]  # safety_turn only reachable when safety succeeded and fired ACUTE/HARMFUL - engine.m5.routing rule 1
        if signal != "ACUTE_DISTRESS":
            # Track B: a dependency dynamic, not a crisis. No resources
            # (crisis_resources.resources_for_signal already refuses them for
            # this signal) and no session freeze. Governed (Program-Spec SS8,
            # amendment: never respond, let the facilitator handle it) - the voice is
            # silenced here exactly as it already is on Track A below, and
            # the message is withheld from it the same way. Before this
            # amendment the voice spoke "alongside" the Facilitator's own
            # dependency_check_turn, which meant a per-world voice_craft
            # guard line was needed to stop it freelancing outside-help
            # language - a rule only 2 of 11 worlds ever carried. With the
            # voice never called here, that per-world prohibition is
            # unnecessary by construction, not merely unneeded to restate.
            return TurnResult(
                routing_action=action, routing_reason=gate_result.routing.reason,
                gate=gate, safety_state_events=safety_states,
                facilitator_events=[facilitator_turns.dependency_check_turn(world.frame["representative"]["name"])],
                voice_event=None, degraded=gate_result.degraded,
                usage_records=usage_records,
            )

        # Governed (CiC_System_Hub_Decision_Log.md, a portfolio decision):
        # no voice speaks once ACUTE_DISTRESS fires, in the interview any
        # more than at a table (engine.m4.round's own
        # is_acute_crisis branch, Artifact-7 SS2) - the Representative
        # never steps out of its world, full stop, and the crisis-resources
        # append below never depended on a voice call's output anyway
        # (crisis_resources' own stage-5 proof point).
        voice_event = None
        stream_text, stream_failed = None, True

        facilitator_event = crisis_resources.append_crisis_resources_turn(
            signal=signal, stream_text=stream_text, stream_failed=stream_failed,
            representative_name=world.frame["representative"]["name"],
            acute_level=safety_outcome.value["acute_level"],  # schema-required (Artifact-4 SS1), same direct-index discipline as signal above
            already_fired=track_a_last is not None,
        )
        return TurnResult(
            routing_action=action,
            gate=gate, safety_state_events=safety_states,
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
            gate=gate, safety_state_events=safety_states,
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
            session_id=session_id, already_told_ids=already_told_ids,
            already_bridged_figure_ids=already_bridged_figure_ids,
            already_bridged_gloss_ids=already_bridged_gloss_ids, history=history,
            r27_enforce=r27_enforce, known_tradition_names=known_tradition_names,
            self_revision_enabled=self_revision_enabled,
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
            is_other_tradition_first_ask=(gate_result.routing.out_of_scope_class == "other_tradition"),
            other_tradition_evidence_ids=other_tradition_evidence_ids,
            other_tradition_known_in_window=other_tradition_known_in_window,
            other_tradition_revealed=other_tradition_revealed,
            r27_enforce=r27_enforce, known_tradition_names=known_tradition_names,
            self_revision_enabled=self_revision_enabled,
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
