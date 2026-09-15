#!/usr/bin/env python3
"""One notice stripper, shared — and honest about what it cannot decide.

Every closure audit in this build has produced the same false positive: a
corrected phrase survives inside its own [CORRECTED …] notice, quoting the
error in order to record it, and an ad-hoc sweep reports the fix as not
landed. That is MENTION, not USE. It misfired in four consecutive rounds
across two documents, and each time the sweep was re-derived from scratch.

This build writes notices in two shapes.

  FORM A — the narration is INSIDE the brackets:

      **[CORRECTED, 2026-09-15 — Round 1's M1:** an earlier version said
      *"unread at source"* … .**]**

  FORM B — the brackets are a bare provenance stamp and whatever follows
  is outside them:

      **…live sentence. [CORRECTED, 2026-09-15 — Round 1's M7.]** <prose>

Form A is bounded and can be removed exactly. **Form B cannot.** Surveyed
across Doc_09, the seven chunks and the index, the prose trailing a Form B
stamp is narration in 5 cases and a LIVE ASSERTION in 6, and the tag does
not separate them: `[CORRECTED … M7.]` is followed by live text while
`[CORRECTED … H2.]` is followed by narration. No pattern decides it.

Round 5's HIGH-2 was the previous version of this file trying anyway. It
matched Form B by an optional prefix that also matched zero characters, so
it fired on every Form A notice too and then consumed to the end of the
paragraph: Doc_09 §7 lost 48% of its live prose and §2's escalation
paragraph came back as a single space. A closure audit run through it
reported live, uncorrected text as "mention only" — manufacturing exactly
the false conclusion the recurring defect depends on.

So the contract here is deliberately asymmetric:

  live()      removes Form A spans ONLY. It NEVER deletes prose outside a
              bracket, so it cannot hide a live assertion. It will leave
              some Form B narration standing, which makes a fixed thing
              look unfixed — costing a reviewer time, not a reader truth.

  classify()  is the one to call in a closure audit. It returns AMBIGUOUS
              rather than guessing when every surviving occurrence of a
              phrase sits in Form B trailing prose. AMBIGUOUS means open
              the file; it does not mean closed.

A control stated more broadly than it is implemented is worse than no
control, because the next round will trust it.
"""
import re

TAGS = (r"CORRECTED|ADDED|MOVED HERE|MOVED|REVISED|RE-FILED|WITHDRAWN"
        r"|AMENDED|EXTENDED|SUPERSEDED|CORRECTION")

# The body of a notice runs to the first `]**`. It may itself contain a
# `]` — a [sic], a Markdown link, a bracketed gloss — so stop only at a
# `]` that is actually followed by `**` (Round 5's LOW-17).
_BODY = r"(?:[^\]]|\](?!\*\*))*?"

# A complete notice span, from the opening bracket to its `]**` terminator.
_NOTICE = re.compile(r"\*{0,2}\[(?:" + TAGS + r")\b" + _BODY + r"\]\*\*", re.S)

# A Form B stamp: a notice span whose body never re-opens bold. In Form A
# the `:**` that introduces the narration always does.
_STAMP = re.compile(r"\[(?:" + TAGS + r")\b[^*\]]*?\]\*\*", re.S)


def live(text: str) -> str:
    """Text with every notice SPAN removed. Never removes prose outside one.

    Under-strips by design: Form B narration survives. See the module
    docstring for why that direction is the safe one.
    """
    return _NOTICE.sub(" ", text)


def notice_spans(text: str):
    """(start, end) of every bracket-delimited notice span in `text`."""
    return [(m.start(), m.end()) for m in _NOTICE.finditer(text)]


def trailing_spans(text: str):
    """(start, end) of the prose after each Form B stamp, to the paragraph end.

    Undecidable regions: narration in some, live assertion in others.
    Computed on the ORIGINAL text — `live()` has already deleted the stamps
    that delimit these regions, so they cannot be found in stripped output.
    """
    out = []
    for m in _STAMP.finditer(text):
        end = text.find("\n\n", m.end())
        out.append((m.end(), len(text) if end == -1 else end))
    return out


def classify(text: str, phrase: str) -> str:
    """'absent' | 'live' | 'notice-only' | 'ambiguous'.

    Every occurrence is located in the ORIGINAL text and placed in one of
    three regions: inside a notice span (mention), inside Form B trailing
    prose (undecidable), or neither (live).

    'ambiguous' is a verdict, not a failure: it means a human has to look.
    Never report a finding closed on 'ambiguous'.
    """
    if phrase not in text:
        return "absent"
    notices = notice_spans(text)
    trailing = trailing_spans(text)
    seen = set()
    for m in re.finditer(re.escape(phrase), text):
        i = m.start()
        if any(a <= i < b for a, b in notices):
            seen.add("notice")
        elif any(a <= i < b for a, b in trailing):
            seen.add("ambiguous")
        else:
            return "live"
    return "ambiguous" if "ambiguous" in seen else "notice-only"


def mentions_only(text: str, phrase: str) -> bool:
    """True when `phrase` appears in `text` but nowhere in its live prose.

    Conservative: 'ambiguous' returns False, so an audit re-checks by hand
    rather than recording a closure it has not established.
    """
    return classify(text, phrase) == "notice-only"
