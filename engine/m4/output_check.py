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

THREE FAMILIES, chosen because each is EXACTLY decidable on the finished
text. Register in general is not (engine/m3/grading.py says so about
itself, and it is right); these three are.

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

WHAT IT DELIBERATELY DOES NOT DO: stop the model writing any of this. That
is the prompt's job, and the prompt will sometimes fail. The value here is
that a failure becomes visible instead of silent.
"""
import re

from engine.prose import QUOTE_CLOSE, QUOTE_OPEN, SELF_NAMING_MARKER, content_words, sentences

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

# A claim about the shared past. Deliberately narrow: each of these asserts
# that something HAS BEEN SAID, which is checkable, rather than merely
# referring to a topic, which is not.
_CONVERSATIONAL = re.compile(
    r"\b(?:"
    r"already (?:gave|told|said|mentioned|spoke|offered|named)"
    r"|we (?:gave|told|showed|named) you"
    r"|as we (?:said|told|mentioned|put it)"
    r"|(?:as|like) we (?:said|mentioned) (?:earlier|before|above)"
    r"|earlier we|we mentioned|we have (?:already )?(?:said|told|named)"
    r"|we told you|you(?:'ll| will) remember"
    r"|as (?:mentioned|noted) (?:earlier|above)"
    r"|(?:the|that) (?:one|woman|man|story|saying|elder) (?:we|i) (?:named|gave|told|mentioned)"
    r"|(?:i|we) have named"
    r"|so far in this conversation"
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
        if not _CONVERSATIONAL.search(sentence):
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


def check_output(text: str, *, history: list[dict] | None = None) -> list[dict]:
    """Every defect found on the finished text. Empty list is the clean case.

    `history` is the Messages-API turn list the generation call was given
    (engine.api.wiring.history_from_transcript) - passed rather than
    re-derived, so the check and the call can never disagree about what the
    voice had actually said.
    """
    if not (text or "").strip():
        return []
    return _display_findings(text) + _conversational_findings(text, history) + _pronoun_findings(text)
