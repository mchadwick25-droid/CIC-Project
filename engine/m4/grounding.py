"""The do-not-voice licence check.

Program-Spec §4.1 names it directly: the record set holds "licensed quotes
(including do-not-voice, so a violation is recognizable)". A quote the
world's own rights record forbids speaking must never appear verbatim in
an answer - not a citation question but a content-licensing one, checked
here because this is the one place both the record licence data and the
answer text are in hand together.

What used to live beside it - ground_citations and its excerpt-window
helpers - is gone. It had no call sites left once the voice began carrying
its own inline citation tags (there is no post-hoc claimed_drawn_on list
to badge-check any more), and dead code that looks like a safety check is
worse than no code at all.
"""
import re


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", (text or "").lower())


def find_do_not_voice_violation(*, answer_text: str, quotes: list[dict]) -> str | None:
    """Returns the offending quote id if a do-not-voice-licensed quote's
    exact text appears verbatim in the answer, else None. Fires whether or
    not the voice ever cited the quote."""
    normalized_answer = _normalize(answer_text)
    for quote in quotes:
        if quote.get("license") != "do-not-voice":
            continue
        if _normalize(quote["text"]) in normalized_answer:
            return quote["id"]
    return None
