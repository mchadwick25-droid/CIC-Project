#!/usr/bin/env python3
"""One notice stripper, shared.

Every closure audit in this build has produced the same false positive: a
corrected phrase survives inside its own [CORRECTED …] notice, quoting the
error in order to record it, and an ad-hoc sweep reports the fix as not
landed. That is MENTION, not USE. It has misfired in four consecutive rounds
across two documents, and each time the sweep was re-derived from scratch.

The hard case is the HEADING FORM, where the bracket closes early and the
correcting prose follows outside it:

    **Heading. [CORRECTED, 2026-09-15 — Round 3.]** An earlier version said …

A pattern that only matches `**[TAG …]**` leaves that trailing prose live.

`live()` removes both forms. Import it rather than writing another regex.
"""
import re

TAGS = r"CORRECTED|ADDED|MOVED HERE|MOVED|REVISED|RE-FILED|WITHDRAWN|AMENDED|EXTENDED|SUPERSEDED|CORRECTION"

# (1) an ordinary inline notice: **[TAG …]**
_INLINE = re.compile(r"\*{0,2}\[(?:" + TAGS + r")\b[^\]]*?\]\*\*", re.S)
# (2) heading form: **… [TAG …]** <prose> … up to the paragraph's end
_HEADING = re.compile(
    r"\*\*[^*\n]{0,120}\[(?:" + TAGS + r")\b[^\]]*?\]\*\*.*?(?=\n\n|\Z)", re.S)


def live(text: str) -> str:
    """Return only text that ASSERTS something, with every notice removed."""
    return _INLINE.sub(" ", _HEADING.sub(" ", text))


def mentions_only(text: str, phrase: str) -> bool:
    """True when `phrase` appears in `text` but nowhere in its live prose."""
    return phrase in text and phrase not in live(text)
