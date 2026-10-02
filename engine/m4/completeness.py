"""A reply must end on a finished sentence.

The voice call has an output ceiling. When the model reaches it, the API
stops with stop_reason == "max_tokens" and the text ends wherever the
count ran out: mid-clause, mid-quotation, mid-tag. Nothing downstream
looked at the reason, so that fragment was graded, shown and stored as a
finished reply.

This module holds the two exact facts the rest of the engine needs:

  ends_on_full_stop(text)            whether the text stops on a finished
                                     sentence
  trim_to_complete_sentence(text)    the longest prefix that does, and the
                                     fragment cut off behind it

Tags are not prose. A sentence the model closes as "soul. [[alx.x]]" or
"soul [[alx.x]]." is finished; a stream that stops inside "[[alx.gra" is
not, and the dangling opener is dropped with the fragment around it.

A quotation counts as part of its sentence. A reply that stops inside an
open quotation is cut off even when an earlier sentence inside the quote
ended on a full stop, so a prefix that leaves a quotation open is not
accepted.
"""
import re

from engine.prose import QUOTE_CLOSE, QUOTE_OPEN, quote_aware_sentences

_TRAILING_TAGS = re.compile(r"(?:\s*\[\[[^\]]*\]\])+\s*\Z")
_DANGLING_TAG = re.compile(r"\s*\[\[[^\]]*\Z")
_TERMINAL = re.compile(r"[.!?…][\"'”’)\]]*\Z")


def _open_quotes(text: str) -> int:
    return len(QUOTE_OPEN.findall(text)) - len(QUOTE_CLOSE.findall(text))


def _finished(text: str) -> bool:
    body = _DANGLING_TAG.sub("", text or "")
    body = _TRAILING_TAGS.sub("", body).rstrip()
    return bool(_TERMINAL.search(body)) and _open_quotes(body) <= 0


def ends_on_full_stop(text: str) -> bool:
    """True when `text` is non-blank and stops on a finished sentence."""
    if not (text or "").strip():
        return False
    return _finished(text)


def trim_to_complete_sentence(text: str) -> tuple[str, str]:
    """(kept, dropped): `kept` is the longest prefix of `text` that ends on
    a finished sentence, `dropped` is the remainder. Text that already ends
    on a finished sentence comes back whole with an empty remainder. Text
    with no finished sentence at all comes back as ("", text)."""
    if not (text or "").strip():
        return "", text or ""
    if _finished(text):
        return text, ""
    parts = quote_aware_sentences(text)
    ends: list[int] = []
    cursor = 0
    for part in parts:
        start = text.index(part, cursor)
        cursor = start + len(part)
        ends.append(cursor)
    for k in range(len(parts) - 1, -1, -1):
        if _finished(text[: ends[k]]):
            return text[: ends[k]], text[ends[k]:]
    return "", text
