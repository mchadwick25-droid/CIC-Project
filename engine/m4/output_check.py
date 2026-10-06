"""The last thing before a participant reads it.

WHY THIS EXISTS, and why it is not another regex widened. Every check in
this engine looks INWARD: M1 gates a record against its sources,
grounding_net gates a sentence against its own records, M3 gates a citation
against a source id. The finished paragraph - the only artifact a person
actually sees - was verified by nobody. grounding_net's own module carries
a twelve-line comment about exactly this ("the last thing before a
participant reads it"), naming markdown emphasis reaching readers in 5 of
49 live turns, a stray horizontal rule, and predicting the malformed-tag
case verbatim. No such function was ever written. This is it.

THE DIVISION OF LABOUR, which is the point. A prompt is a REQUEST and the
model may decline it. Three separate defects were each met, over one day,
by asking the prompt more insistently: an id printed beside a heading, then
"(cite as [[id]])" when that was not enough; a clause telling the evidence
block to say its ground was not already spoken, which a bait probe broke
two hours later. Asking is upstream and probabilistic. Checking is
downstream and exact. This module only checks.

REPORTS, NEVER EDITS - the stance grounding_net's comment already states
and Program-Spec M4 requires ("never by editing a live response"; the
fallback ladder appends, it never revises). A finding is a signal that
something upstream is wrong, not something to paper over on the way out.
So nothing here mutates text, and the findings ride on the voice event.

FOUR FAMILIES, chosen because each is EXACTLY decidable on the finished
text (given, for the fourth, the citations and records the turn already
resolved). Register in general is not (engine/m3/grading.py says so about
itself, and it is right); these four are.

  display        markup that was never meant for a person. Residual
                 [[...]] in any spelling, literal asterisks, a markdown
                 heading, a horizontal rule.
  conversational a claim about what has already passed between the two of
                 us. THIS IS THE ONE CLASS THE ENGINE CAN VERIFY PERFECTLY
                 and never did: the transcript is right here. Checked the
                 same way grounding_net checks a claim against its records
                 - same shape, different ground.
  pronoun        the strict we-voice. First-person singular outside the one
                 sanctioned self-naming line, and outside quoted historical
                 speech, which keeps its own original wording by rule.
  guard_proximity a sentence that cites a record marked with a
                 claim_guards entry - a barred proposition -
                 and shares that barred proposition's own subject matter
                 (Build-Plan.md Stage 4b). grounding_net's per-sentence
                 check alone catches a
                 fabricated version of exactly such a claim only 2 times
                 in 13; this is a second, independent
                 net at the one place both the sentence and its own
                 citation are already known together. Feeds the m7 audit
                 instrument at defect severity - reports
                 only, same as every family here, never removes a
                 sentence.

WHAT IT DELIBERATELY DOES NOT DO: stop the model writing any of this. That
is the prompt's job, and the prompt will sometimes fail. The value here is
that a failure becomes visible instead of silent.
"""
import re

from engine.prose import GUARD_MARKERS, QUOTE_CLOSE, QUOTE_OPEN, SELF_NAMING_MARKER, content_words, is_guard_marker_line, sentences

# Anything in tag position, however it is spelled. grounding_net.strip_tags
# matches [a-z0-9_.-]+ ONLY, because it must also resolve what it strips -
# so a tag carrying uppercase, a colon and spaces survives it untouched.
# Eight [[THIN: ...]] tags reached a participant across three turns of one
# live probe on desert. Stripping and resolving are two jobs; this one only
# asks whether anything tag-shaped is still on the page.
_ANY_TAG = re.compile(r"\[\[[^\]]*\]\]")
_HEADING = re.compile(r"^\s{0,3}#{1,6}\s", re.MULTILINE)
_RULE = re.compile(r"^\s*-{3,}\s*$", re.MULTILINE)
_ASTERISK = re.compile(r"\*")

# A claim about the shared past. TWO PARTS, BOTH REQUIRED, because one is
# not enough: "as we put it, not by chattering words but by experience" is
# the voice attributing WORDING to its own tradition, not telling the
# participant what it said earlier - and the first version flagged it. A
# claim about this conversation nearly always addresses the participant
# ("we told YOU") or dates itself ("already", "earlier", "so far"). A claim
# about how the tradition phrased something does neither.
_SPEECH_ACT = re.compile(
    r"\b(?:we|i) (?:have )?(?:already )?(?:said|told|gave|given|showed|named|mentioned|spoke|offered)\b",
    re.IGNORECASE,
)
_SESSION_MARKER = re.compile(
    r"\b(?:you|already|earlier|before|previously|so far|just now|in this conversation)\b",
    re.IGNORECASE,
)

# The participant asserting that something was said. The false premise
# lives HERE, in their turn - acceptance is the absence of a correction in
# the reply, which is undecidable from the reply alone. This is why the
# check takes the participant message: no pattern over the output reaches
# a defect whose other half is in the input.
_PARTICIPANT_PRIOR = re.compile(
    r"\b(?:"
    r"earlier you (?:mentioned|said|named|told|spoke)"
    r"|you (?:earlier |already |just )?(?:mentioned|named|told me|told us|said)"
    r"|remind me (?:of )?what you (?:told|said)"
    r"|as you (?:said|mentioned|put it)"
    r"|going back to what you said"
    r")\b",
    re.IGNORECASE,
)

# The voice DECLINING a premise about the conversation. Deliberately about
# saying and naming, never about the record: an earlier version matched "we
# did not leave behind an account of how we sat with the dying", which is
# an honest limit about what survives, not a correction of the participant.
_PREMISE_CORRECTION = re.compile(
    r"\b(?:"
    r"we have not (?:said|named|mentioned|spoken|told)"
    r"|we did not (?:say|name|mention)"
    r"|we haven't (?:said|named|mentioned)"
    r"|(?:have )?not yet (?:said|named|mentioned)"
    r"|this is the first (?:time|thing)"
    r"|we have (?:said|named) nothing"
    r"|you may be thinking of"
    r")\b",
    re.IGNORECASE,
)

_FIRST_PERSON_SINGULAR = re.compile(r"\b(?:I|me|my|mine|myself)\b")


def _quoted_ranges(text: str) -> list[tuple[int, int]]:
    """Character ranges inside quotation marks.

    grounding_net._quoted_spans returns the span TEXT, for matching a quote
    against a record. This needs the OFFSETS, to decide whether a pronoun
    falls inside quoted historical speech - a different question, so a
    different function rather than a reshaped shared one.
    """
    ranges, pos = [], 0
    while True:
        open_m = QUOTE_OPEN.search(text, pos)
        if not open_m:
            return ranges
        close_m = QUOTE_CLOSE.search(text, open_m.end())
        if not close_m:
            return ranges
        ranges.append((open_m.end(), close_m.start()))
        pos = close_m.end()


def _finding(family: str, finding: str, sentence: str = "") -> dict:
    return {"family": family, "finding": finding, "sentence": sentence.strip()}


def _display_findings(text: str) -> list[dict]:
    out = []
    for match in _ANY_TAG.finditer(text):
        out.append(_finding("display", f"tag markup reached the participant: {match.group(0)}", match.group(0)))
    if _ASTERISK.search(text):
        out.append(_finding("display", "literal asterisk in participant-facing text"))
    if _HEADING.search(text):
        out.append(_finding("display", "markdown heading in participant-facing text"))
    if _RULE.search(text):
        out.append(_finding("display", "horizontal rule in participant-facing text"))
    return out


def _proper_nouns(sentence: str) -> set[str]:
    """Capitalised words that are not the sentence's first word.

    The subject of a claim about the past is almost always a name, and a
    name is the one part of such a claim that can be checked EXACTLY: it
    either occurs in a prior turn or it does not.
    """
    rest = sentence.split(" ", 1)
    return set(re.findall(r"\b[A-Z][a-z]{2,}\b", rest[1])) if len(rest) > 1 else set()


def _conversational_findings(text: str, history: list[dict] | None) -> list[dict]:
    """A claim that something was already said, checked against what was.

    THE FIRST VERSION OF THIS WAS WRONG, and the way it was wrong is worth
    keeping. It asked whether the claim shared any content word with the
    prior turns - and the words a back-reference is built from ("told",
    "said", "named", "asking") recur across every turn, so the frame of the
    claim vouched for the claim. Measured on the bait probe: "We told you
    it is not effort alone" shared four words with turns that had discussed
    neither effort nor salvation, and passed. The test was reading the
    verbs of alleging instead of the thing alleged.

    So this decides only what is decidable, and says so where it is not -
    the same honesty engine/m3/grading.py states about register:

      false        no prior assistant turn exists at all, or the claim
                   names a person or place that occurs in none of them.
                   Both are exact.
      unverified   a claim of prior discourse with no name in it. Whether
                   the TOPIC was discussed is a semantic judgment no
                   pattern here can make, so it is surfaced, not ruled on.
                   The count is itself the signal.

    A claim whose names all appear in prior turns produces no finding.
    """
    said = [t.get("content") or "" for t in (history or []) if t.get("role") == "assistant"]
    out = []
    for sentence in sentences(text):
        if not (_SPEECH_ACT.search(sentence) and _SESSION_MARKER.search(sentence)):
            continue
        if not said:
            out.append(_finding("conversational", "false: claims something was already said, on a turn with no prior turns", sentence))
            continue
        names = _proper_nouns(sentence)
        unsaid = sorted(n for n in names if not any(n in turn for turn in said))
        if unsaid:
            out.append(
                _finding("conversational", f"false: claims prior mention of {', '.join(unsaid)}, named in no prior turn", sentence)
            )
        elif not names:
            out.append(
                _finding("conversational", "unverified: claims prior discourse with no name in it - needs a reader", sentence)
            )
    return out


def _premise_findings(text: str, participant_message: str | None, said: list[str]) -> list[dict]:
    """The participant asserts prior discourse. Was there any?

    THIS IS THE HALF THE OUTPUT CANNOT SEE. A live probe on desert opened a
    reply "That was Sarah - Amma Sarah, by the honored address we gave to
    proven elders", two turns into a conversation about daily bread. Sarah
    had never been mentioned. Nothing in that sentence is a back-reference
    phrase; the acceptance is carried by the word "that", pointing at a
    mention the participant asserted and the transcript refutes. Widening a
    pattern over the reply never reaches it, because half the defect is in
    the input.

    So: when the participant claims we said something, ask first whether the
    claim is SUPPORTED - do the words they used, minus the framing, appear
    in anything we actually said? A supported claim is an ordinary
    follow-up and produces nothing, which is what keeps this quiet on the
    common case.

    An UNSUPPORTED claim is a false premise, and then the reply has exactly
    one correct move: decline it. Declining produces nothing. Otherwise:

      false        the reply introduces a name that appears in no prior
                   turn - it has supplied a specific memory that never
                   happened. Exact.
      unverified   the reply neither corrects nor names. Whether it went
                   along with the premise is a reading.
    """
    if not participant_message or not _PARTICIPANT_PRIOR.search(participant_message):
        return []

    prior_words: set[str] = set()
    for turn in said:
        prior_words |= content_words(turn)

    # Strip the assertion's own framing, so "you mentioned"/"you told me"
    # cannot vouch for itself out of some earlier turn's ordinary prose.
    asked = content_words(_PARTICIPANT_PRIOR.sub(" ", participant_message))
    if not said:
        pass  # no prior turn at all: every such claim is false
    elif asked & prior_words:
        return []  # supported - an ordinary follow-up

    if _PREMISE_CORRECTION.search(text):
        return []  # the voice declined it, which is the correct move

    unsaid = sorted(n for n in _proper_nouns_in(text) if not any(n in turn for turn in said))
    if unsaid:
        return [
            _finding(
                "conversational",
                f"false: answered an unsupported claim of prior discourse by naming {', '.join(unsaid)}, "
                "which appears in no prior turn",
                participant_message,
            )
        ]
    return [
        _finding(
            "conversational",
            "unverified: answered an unsupported claim of prior discourse without correcting it - needs a reader",
            participant_message,
        )
    ]


def _proper_nouns_in(text: str) -> set[str]:
    names: set[str] = set()
    for sentence in sentences(text):
        names |= _proper_nouns(sentence)
    return names


def _pronoun_findings(text: str) -> list[dict]:
    quoted = _quoted_ranges(text)
    out = []
    for sentence in sentences(text):
        if SELF_NAMING_MARKER in sentence.lower():
            continue  # the one fleet-sanctioned exception
        start = text.find(sentence)
        for match in _FIRST_PERSON_SINGULAR.finditer(sentence):
            at = start + match.start() if start >= 0 else -1
            if any(lo <= at < hi for lo, hi in quoted):
                continue  # a quoted figure keeps their own first person, by rule
            out.append(_finding("pronoun", f"first-person singular {match.group(0)!r} outside the sanctioned self-naming line", sentence))
            break
    return out


# The note-authoring convention itself (from the prefer_instead redirect
# rule's migration; Build/tools/split_retrieval_guards.py), measured the same way
# engine/m4/evidence.py's own _PREFER_INSTEAD_CONDITION_STOPWORDS was:
# "participant is asking whether...", "the Representative must not...",
# "our vendored evidence..." are the note's own scaffolding, not part of
# the barred proposition. A different set from evidence.py's own (guard
# notes and redirect notes share an origin but not identical phrasing),
# kept local rather than imported - each module's own scaffolding list
# stays honest about what it was actually measured against.
_GUARD_PROXIMITY_BOILERPLATE = {
    "participant", "question", "asking", "asks", "wants", "needs", "wanted",
    "whether", "representative", "vendored", "evidence", "record", "record's",
    "story", "native", "voice",
}
_PROPER_NOUN = re.compile(r"\b[A-Z][a-z]{2,}\b")

# Below this, a shared word or two is closer to coincidence than to
# asserting the same claim - measured directly: every one of Stage 1's own
# 13 fabricated flat assertions shares at least 2 claim words with its own
# guard's proposition (_guard_proposition below) once boilerplate and
# proper nouns are stripped; the smallest observed overlap among all 13 is
# exactly 2, so this is the real floor the data supports, not a guess.
_GUARD_PROXIMITY_MIN_SHARED_WORDS = 2


def _guard_proposition(guard_text: str) -> set[str]:
    """A claim_guards entry's own barred subject matter - what it actually
    asserts, not who or what it is about. GUARD_MARKERS' own honesty-
    framing phrases and the note-authoring boilerplate are stripped first,
    and its own proper nouns are excluded from the result entirely.

    PROPER NOUNS ARE EXCLUDED ON PURPOSE. Two names sharing a sentence is
    not itself the barred claim - "Brictio" and "Martin" appear together
    in every truthful sentence about their courtyard scene, since that is
    who the scene is about. A sentence is asserting the barred proposition
    only when it shares the claim's own non-name vocabulary (what it
    actually says about them - "succeeded", "bishop" - not just their
    names). Measured against a constructed false positive before this
    exclusion existed: "Brictio was in the courtyard when Martin
    confronted him" shared 2 words with this guard's own full text on a
    flat, unsplit count - the same threshold that correctly catches all 13
    of Stage 1's own fabricated flat assertions on the split, name-
    excluded set. Excluding proper nouns fixed the false positive without
    losing any of the 13 (a stricter design that also required an
    OVERLAPPING proper noun was tried first and tested worse: it missed a
    real case where the fabrication named none of the guard's own proper
    nouns at all).
    """
    stripped = guard_text
    for marker in GUARD_MARKERS:
        stripped = re.sub(re.escape(marker), " ", stripped, flags=re.IGNORECASE)
    all_words = content_words(stripped) - _GUARD_PROXIMITY_BOILERPLATE
    proper = {p.lower() for p in _PROPER_NOUN.findall(stripped)}
    return all_words - proper


def _guard_proximity_findings(text: str, citations: list[dict] | None, repository_records: dict[str, dict] | None) -> list[dict]:
    if not citations or not repository_records:
        return []
    out = []
    for citation in citations:
        sentence = (citation.get("sentence") or "").strip()
        if not sentence or is_guard_marker_line(sentence):
            continue  # the voice is honestly declining or framing a limit, not asserting one
        sentence_words = content_words(sentence)
        for rid in citation.get("record_ids") or []:
            record = repository_records.get(rid) or {}
            for guard in record.get("claim_guards") or []:
                shared = sentence_words & _guard_proposition(guard)
                if len(shared) < _GUARD_PROXIMITY_MIN_SHARED_WORDS:
                    continue
                out.append(
                    _finding(
                        "guard_proximity",
                        f"cites {rid}, barred from asserting {guard!r} - this sentence shares "
                        f"{len(shared)} content word(s) with the barred claim's own subject matter: {sorted(shared)}",
                        sentence,
                    )
                )
    return out


def check_output(
    text: str,
    *,
    history: list[dict] | None = None,
    participant_message: str | None = None,
    citations: list[dict] | None = None,
    repository_records: dict[str, dict] | None = None,
) -> list[dict]:
    """Every defect found on the finished text. Empty list is the clean case.

    `history` is the Messages-API turn list the generation call was given
    (engine.api.wiring.history_from_transcript) - passed rather than
    re-derived, so the check and the call can never disagree about what the
    voice had actually said. `participant_message` is the turn being
    answered: half of a false-premise defect lives there, and no pattern
    over the reply alone can reach it. `citations` is engine.m4.
    citation_cards.resolve_citation_sources's own output (per-sentence
    entries with resolved `record_ids`) and `repository_records` is the
    world's own compiled records by id - both optional, both needed
    together for the guard_proximity family; a caller with neither (e.g.
    a bare-text check) gets the first three families only, exactly as
    before this family existed.
    """
    if not (text or "").strip():
        return []
    said = [t.get("content") or "" for t in (history or []) if t.get("role") == "assistant"]
    return (
        _display_findings(text)
        + _conversational_findings(text, history)
        + _premise_findings(text, participant_message, said)
        + _pronoun_findings(text)
        + _guard_proximity_findings(text, citations, repository_records)
    )


def find_shipped_defects(report: dict) -> list[dict]:
    """Every output_defects[] entry that actually shipped in a live-test
    report - engine.m4.live_turn_run's or engine.m4.live_table_run's own
    report shape, read directly rather than re-derived, so this can never
    disagree with what the report itself recorded.

    WHY THIS EXISTS: a live-turn report can carry a false
    conversational-memory defect
    (check_output's own family, this module's ONE perfectly-decidable
    class) on a turn presented as `degraded: false`. `degraded` on these
    reports means "a gate call failed," not "the turn was good" - it says
    nothing about output_defects, and nothing else reads the field, so it
    would otherwise only be found by opening the raw JSON by hand. This
    module's own REPORTS, NEVER EDITS stance is right for a live participant turn
    (the module's header explains why); it does not follow that a REVIEW
    of an already-shipped report should have the same blind spot. A gate
    reading a finished report is downstream of generation, not upstream of
    it - checking it does not soften the module's own "asking is upstream
    and probabilistic, checking is downstream and exact" division.

    Every finding returned here already shipped to a participant (or would
    have, on a real run) - this cannot be waived away as "the model might
    have declined," because by the time it reaches this function, it did
    not decline.
    """
    found = []
    for r in report.get("results", []):  # live_turn_run.py's own shape
        voice = (r.get("result") or {}).get("voice_event") or {}
        for defect in voice.get("output_defects") or []:
            found.append({"id": r.get("id"), "message": r.get("message"), **defect})
    for round_ in report.get("rounds", []):  # live_table_run.py's own shape
        for turn in round_.get("turns", []):
            voice = turn.get("voice") or {}
            for defect in voice.get("output_defects") or []:
                found.append({
                    "round_no": turn.get("round_no"), "position": turn.get("position"),
                    "turn_selected": turn.get("turn_selected"), **defect,
                })
    return found
