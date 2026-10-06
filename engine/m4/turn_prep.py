"""The per-turn preparation shared by both voice-generation paths:
engine.m4.turn._run_ordinary_voice_turn (the whole-turn path) and
engine.m4.streaming.stream_voice_turn_sentences (the sentence-gated
streaming path, Stage 7b). Both need the identical evidence-assembled
user message and the identical private directive built for the same
turn; before this module existed, only the whole-turn path built them,
and any caller of the streaming path would otherwise have had to
duplicate that assembly sequence itself rather than share it.

Deliberately its own module rather than living in either caller: turn.py
already carries the whole-turn path's own generation/net/guard logic
(nothing here calls a model or touches TurnResult), and streaming.py's
own module docstring commits to never importing from engine.m4.turn - a
third module both depend on keeps that commitment intact while letting
the two paths share this logic instead of one reimplementing the other's
copy. Every function here is a pure transform over already-loaded world
data and already-computed routing state - no model call, no store write,
byte-identical inputs always produce byte-identical outputs.
"""
from __future__ import annotations

from dataclasses import dataclass

from engine.m1.loader import load_fleet_records
from engine.m4 import evidence
from engine.m4.name_bridge import spoken_name
from engine.m4.world_loader import LoadedWorld
from engine.m5.routing import Directive

# engine.m4.uncited_claims.R26_HONEST_LIMIT_SENTENCE, matched exactly
# (case-insensitive) by that module's own allowed-uncited detection - see
# _other_tradition_directive's own docstring for why the two must stay
# identical by construction. Kept as this module's own copy (moved here
# unchanged from engine.m4.turn, where it lived before this extraction)
# rather than imported from uncited_claims, matching how it already read
# before this module existed.
R26_HONEST_LIMIT_SENTENCE = "Our record doesn't mention that Christian tradition."


def _revealed_excerpts_block(revealed_excerpts: list[tuple[str, str]] | None) -> str | None:
    """The tradition-pivot rule's condition (b) and third-source
    quoted-lines block: exactly what this
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
    """The tradition-pivot rule for the pivot - which part of this world's
    own record the answer comes from - on a question naming a tradition
    the record does not cover. known_in_window is engine.m4.uncited_claims.
    tradition_known_in_window's result (condition (a), under its
    asymmetric reading); None means the question named no registry
    tradition at all (e.g. "the Arians"), so nothing establishes the
    knowledge either way and the text says only that. has_excerpts is
    condition (b): the quoted-lines block rides alongside. seated: the
    named tradition's own chair is at this table, and everything it says
    is itself something this conversation told the voice (the third-source
    rule), named
    or not - so its speech is a source alongside the quoted lines, as the
    seated branch's own text already allows. Neither condition: the
    question's own words alone. Every branch keeps the
    rule's standing limit - content about the other tradition never
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
    """The honest-limit rule: a Representative should only
    know its own sources unless they would have known the sources from
    another in reality. This is the directive text an other_tradition
    first ask now carries - see _build_turn_directive's own
    is_other_tradition_first_ask parameter. The fixed sentence here is
    engine.m4.uncited_claims.R26_HONEST_LIMIT_SENTENCE, matched exactly
    (case-insensitive) by that module's own allowed-uncited detection -
    the two must stay identical by construction, not by convention.
    Always returns real text when called (never None - see
    tradition_seated's own note below for why that changed).

    evidence_record_ids (lets a world's own records stand
    in for the honest limit when they already speak to the question):
    engine.m4.uncited_claims.world_records_mention_tradition's own
    result - record ids in THIS world's own package that already,
    genuinely name the tradition asked about. The honest-limit rule
    already named this exception ("unless they would have known the sources from
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
    tradition's own name and witness as its own, the exact thing the
    tradition-pivot rule forbids. tradition_seated_name (the seated tradition's own registry
    card_name, passed through from table_wiring.py so this function
    never has to know about the registry itself) now carries a real
    directive instead: this seat may respond only to the bare fact that
    a tradition under that name is seated here with its own
    Representative, and to what that chair has actually said in this
    conversation so far (the tradition-pivot rule's condition (b): "only if
    it would have known in its own time, or if something was revealed in
    the facilitator's introduction or user, but limited only to what was
    told to them in the conversation") - never claiming that tradition's
    own name, history, or witness as this seat's own.

    repeat_turn (the same Table-parity fix): this seat's own SECOND OR
    LATER turn within the same round (turn_selector may draw a seat back
    in - the fixed sentence said once already stays true, but repeating
    it verbatim every return turn is not what interview's own single-ask
    shape ever produces). No evidence, not seated: keep the
    tradition-pivot rule's own knowledge-scope framing ("this is another tradition, answer only
    from your own records") but drop the "if nothing, say exactly..."
    clause - it was already said on this seat's first turn this round.

    known_in_window and revealed_excerpts (the tradition-pivot rule): the
    pivot itself: "only if it would have known
    in its own time, or if something what revealed in the facilitators
    introduction or user, but limited only to what was told to them in
    the conversation" - and the third source, "add or what another representitive
    revials in the conversation". known_in_window is condition (a);
    revealed_excerpts is condition (b) with its third source - see
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
    witness as its own, exactly what the tradition-pivot rule forbids. There is no genuinely
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
        # returns real text now when called (see
        # this function's own docstring), so this path is only reachable
        # when is_other_tradition_first_ask is False and directive/
        # table_engagement were both falsy too - the header line alone is
        # not a real directive, return None exactly as the no-directive
        # path above does.
        return None
    return "\n".join(parts)


@dataclass(frozen=True)
class VoiceTurnInputs:
    """Everything a generation call needs besides the model client itself
    and the world's own cached system prompt: the evidence-assembled user
    message, the per-turn private directive, and the repository/thin-topic
    state the grounding checks downstream (whole-turn or per-sentence) run
    against. repository_records and thin_topics are returned alongside the
    message/directive rather than recomputed by each caller separately -
    both are deterministic functions of world.repository alone, but
    recomputing them a second time per turn is pure waste when the caller
    already has this dataclass in hand."""

    repository_records: dict[str, dict]
    thin_topics: list[dict] | None
    figures_already_named: list[str]
    user_message: str
    turn_directive: str | None


def prepare_voice_turn_inputs(
    *,
    world: LoadedWorld,
    participant_message: str,
    directive: Directive | None,
    already_told_ids: set[str] | None = None,
    already_bridged_figure_ids: set[str] | None = None,
    history: list[dict] | None = None,
    context_prefix: str | None = None,
    secondary_context: str | None = None,
    table_engagement: str | None = None,
    is_other_tradition_first_ask: bool = False,
    other_tradition_evidence_ids: list[str] | None = None,
    other_tradition_seated: bool = False,
    other_tradition_seated_name: str | None = None,
    other_tradition_repeat_turn: bool = False,
    other_tradition_known_in_window: bool | None = None,
    other_tradition_revealed: list[tuple[str, str]] | None = None,
    correction: str | None = None,
) -> VoiceTurnInputs:
    """The setup every voice-generation call needs before the first model
    call: assemble this turn's evidence (design §3, engine.m4.evidence -
    deterministic, no model call, rides in the per-turn user message,
    never the cached system prefix - §3.1/§5's own cache-conscious
    framing) and build this turn's own private directive
    (_build_turn_directive). Extracted unchanged from
    engine.m4.turn._run_ordinary_voice_turn, which called this exact
    sequence inline before engine.m4.streaming (Stage 7b) needed the
    identical sequence and had no way to reach it without either
    duplicating it or importing turn.py directly (which streaming.py's own
    module docstring commits not to do).

    Every parameter here means exactly what the same-named parameter on
    _run_ordinary_voice_turn already documents - see that function's own
    docstring for context_prefix/secondary_context/table_engagement (the
    Table's additions), the other_tradition_* family (the tradition-pivot
    rule), and correction (free text appended onto whatever
    _build_turn_directive produced - the same append-not-replace channel
    _append_seat_identity_correction and _append_r27_correction already
    use for a regeneration's own retry directive)."""
    repository_records = evidence.repository_records_by_id(world.repository)
    thin_topics = evidence.thin_topics_for(repository_records)

    # canon_question records are fleet-shared, not part of any one world's
    # hash-verified package, so loaded directly the same way
    # engine.m1.gates already loads them - not yet cached the way
    # LazyWorldLoader caches a world's own package (compiled/indexes/
    # canon-map.json exists for exactly this optimization,
    # engine.m2.builders.build_canon_map_json, but nothing reads it yet -
    # a follow-up, not a correctness gap: this derives the identical
    # corpus live, just without the compiled cache).
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

    return VoiceTurnInputs(
        repository_records=repository_records,
        thin_topics=thin_topics,
        figures_already_named=figures_already_named,
        user_message=user_message,
        turn_directive=turn_directive,
    )
