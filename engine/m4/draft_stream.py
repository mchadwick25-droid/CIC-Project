"""The participant-facing draft of a reply while it is still being written.

The voice writes tagged text ("... [[world.type.slug]]." with the tag before
the sentence's full stop). The finished reply a participant keeps is exactly
`grounding_net.strip_tags` of that raw text (`engine.m4.turn.apply_net`), so
a draft that is the tag-stripped text of the sentences completed so far is a
true prefix of the finished reply, never a different text.

A draft shows sentences only once they are complete. The last, still-open
sentence is held back: more text may extend it, and a tag may be half
written at the end of the buffer. Nothing here checks, marks, or withholds
anything. The checks run on the finished reply, which replaces the draft and
alone decides the marks, so a streamed sentence is never different from the
sentence that is kept.
"""
from engine.m4.grounding_net import strip_tags
from engine.prose import quote_aware_sentences


class DraftStream:
    def __init__(self) -> None:
        self._buffer = ""
        self._shown = ""

    def feed(self, chunk: str) -> str:
        """Add one chunk of raw model text. Returns the new display text
        that became safe to show, or "" when no new sentence has completed."""
        self._buffer += chunk
        # Whitespace does not survive the sentence split, so the open
        # sentence is located by its text rather than by summed lengths.
        parts = quote_aware_sentences(self._buffer)
        if len(parts) < 2:
            return ""
        open_start = self._buffer.rfind(parts[-1])
        if open_start == -1:
            return ""
        complete = strip_tags(self._buffer[:open_start])
        if not complete.startswith(self._shown):
            return ""
        new = complete[len(self._shown):]
        self._shown = complete
        return new
