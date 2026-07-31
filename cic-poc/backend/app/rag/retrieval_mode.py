"""Why a retrieval is being run - the question it is being asked to answer.

This codebase retrieves from a world's record for two genuinely different
reasons, and they want different behavior:

  TURN         The representative is about to speak. The question is
               "what should surface to THIS participant, in THIS conversation,
               right now." Conversational appropriateness is part of the
               question, so the Do-Not-Retrieve-When guards apply, and a chunk
               already surfaced this session is excluded so the representative
               does not repeat itself.

  ADJUDICATION A turn has already been spoken and is being judged against the
               record (fabrication, over-settling, and the repair-challenge
               adjudicators). The question is "what does this world's record
               actually CONTAIN." Nothing here is shown to a participant.

Before this type existed, those two callers differed only in which keyword
arguments they happened to pass, and the difference was never written down
anywhere. That produced two defects of the same shape and opposite sign:

  * Guards: the adjudication call site omitted nothing, so it inherited
    turn-time's guard behavior. A conversational-timing rule was therefore
    filtering the evidence used to judge whether a claim was fabricated - and
    it could hide the exact chunk that would have CLEARED the claim. The
    fabrication adjudicator's own FABRICATED_EXTRINSIC verdict is explicitly
    provisional for this reason ("fresh retrieval may simply have missed the
    chunk"); applying guards there made that miss more likely, in the
    fail-toward-false-accusation direction. Every one of the 178 deployed
    chunks carries a Do-Not-Retrieve-When the runtime treats as evaluable, so
    this was not a corner case - it was every candidate, every adjudication.

  * Session exclusion: the adjudication call site omitted exclude_ids, so it
    got the right behavior. If it had passed the session's exclusion set - an
    entirely natural thing for a later maintainer to do, since every other
    caller does - the adjudicator would have been denied precisely the chunks
    the representative most recently spoke from, which are the chunks most
    likely to settle the claim being judged.

Both were accidents of kwarg defaults. One happened to be right and one
happened to be wrong, and nothing in the code distinguished them. Naming the
mode makes both deliberate, states the reasoning where it can be read, and
means a third mode (or a new call site) has to answer these questions rather
than inherit an answer.

The mode carries only what is genuinely determined by WHY the retrieval runs.
Query text, conversation context, the session exclusion set and k stay
parameters, because they are determined by WHERE the call comes from.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalMode:
    """The question a retrieval is being asked. See module docstring."""

    name: str

    apply_guards: bool
    """Run the Do-Not-Retrieve-When vote on relevance-kept candidates.

    The guard answers "should this surface to the participant right now" -
    a conversational-appropriateness judgement. That is part of the question
    at turn time and a liability at adjudication time.
    """

    allow_session_exclusion: bool
    """Honour the caller's session exclusion set.

    False means the pipeline IGNORES exclude_ids even when one is passed -
    not merely that this caller happens not to pass one. An adjudicator must
    see the whole record; excluding what was already said this session would
    withhold the chunks the judged turn most likely drew on.
    """

    guardless_audit_reason: str
    """Audit-trail wording for a candidate kept without a guard vote, so the
    Level 2/3 trail says WHY no guard ran rather than implying none existed."""


TURN = RetrievalMode(
    name="turn",
    apply_guards=True,
    allow_session_exclusion=True,
    guardless_audit_reason="no evaluable guard",
)

ADJUDICATION = RetrievalMode(
    name="adjudication",
    apply_guards=False,
    allow_session_exclusion=False,
    guardless_audit_reason="guards not applied: adjudication evidence",
)
