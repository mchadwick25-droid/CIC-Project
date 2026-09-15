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

# Round 7's HIGH-1 and MEDIUM-2 both came from trying to express a
# BALANCED-DELIMITER problem as a regex. Round 6 fixed the nested case by
# extending each span to the last `]**` in the paragraph, which then
# swallowed the live prose between two SIBLING notices -- 14,337 characters
# at 15 sites, reintroducing Round 5's HIGH-2. And the paragraph bound
# itself was wrong: it tested for a literally empty line, so a
# whitespace-only line, a list item or a table row let a body run on.
#
# Measured across the nine deliverables: of 75 notice spans, ZERO cross a
# newline. Notices in this build are LINE-SCOPED, and that is the exact
# boundary. A scanner that walks one line, tracking nesting depth, decides
# both cases correctly and cannot cross anything at all.
_OPENER = re.compile(r"\*{0,2}\[(?:" + TAGS + r")\b")
_CLOSER = "]**"


def _scan_line(line, base=0):
    """(spans, unterminated_offsets) for one line, depth-aware.

    An opener inside another notice's body increments depth, so a quoted
    notice cannot terminate its container (Round 6's LOW-8). Depth
    returning to zero ends the span there, so a sibling notice later on
    the same line is a separate span (Round 7's HIGH-1).
    """
    spans, bad, i, n = [], [], 0, len(line)
    while i < n:
        m = _OPENER.search(line, i)
        if not m:
            break
        depth, j, close = 1, m.end(), -1
        while j < n:
            o = _OPENER.search(line, j)
            c = line.find(_CLOSER, j)
            if c == -1:
                break
            if o and o.start() < c:
                depth += 1
                j = o.end()
                continue
            depth -= 1
            j = c + len(_CLOSER)
            if depth == 0:
                close = j
                break
        if close == -1:
            bad.append(base + m.start())
            i = m.end()
        else:
            spans.append((base + m.start(), base + close))
            i = close
    return spans, bad


def _walk(text):
    spans, bad, off = [], [], 0
    for line in text.split("\n"):
        s, b = _scan_line(line, off)
        spans += s
        bad += b
        off += len(line) + 1
    return spans, bad


def notice_spans(text: str):
    """(start, end) of every notice span in `text`. Never crosses a line."""
    return _walk(text)[0]


def unterminated(text: str):
    """Offsets of openers with no balancing `]**` on their own line.

    A non-empty result means malformed notice markup, not malformed prose.
    Such an opener is left standing rather than acted on -- the safe
    direction, since it cannot then delete anything.
    """
    return _walk(text)[1]


def live(text: str) -> str:
    """Text with every notice SPAN removed. Never removes prose outside one.

    Under-strips by design: a Form B stamp's trailing narration survives.
    See the module docstring for why that direction is the safe one.
    """
    out, prev = [], 0
    for a, b in notice_spans(text):
        out.append(text[prev:a])
        out.append(" ")
        prev = b
    out.append(text[prev:])
    return "".join(out)


def trailing_spans(text: str):
    """(start, end) of the prose after each Form B stamp, to the line's end.

    Undecidable regions: narration in some, live assertion in others.
    """
    out = []
    for a, b in notice_spans(text):
        body = text[a:b]
        if "**" in body[body.index("[") + 1:-3]:
            continue            # Form A: narration is inside the brackets
        end = text.find("\n", b)
        out.append((b, len(text) if end == -1 else end))
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
    # Round 7's HIGH-1: Round 6 extended every span here to the last `]**`
    # in the paragraph, to stop a quoted notice truncating its container.
    # That absorbed the live prose between two SIBLING notices instead --
    # 14,337 characters at 15 sites. The scanner above now decides nesting
    # by depth, on the line, so no extension is needed or wanted.
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
