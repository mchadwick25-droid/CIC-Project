"""The one place that knows how a chunk body is divided into sections.

This codebase's chunk bodies use TWO section conventions, and which one a
world uses is an authoring convention of that world's build, not something
the runtime gets to assume:

  1. Fenced headings -   "## Quick Meaning" on its own line, content on the
                          lines below (Syriac, Alexandria, PAHC, Hieronymian,
                          Imperial).
  2. Inline bold labels - "**Quick Meaning:**" with the content following on
                          the SAME line, and no "##" anywhere in the file
                          (Desert Monasticism).

Before this module, three separate places encoded that knowledge
independently: indexer.parse_key_sources, indexer.parse_quick_meaning, and
retriever.get_context_for_response's R7 strip. The first two got it right.
The third searched only for a following "##" to find where a section ended,
which made "no ## in this file" indistinguishable from "nothing follows this
section" - and for Desert, whose Quick Meaning is the FIRST section of a file
containing zero "##", that discarded the entire lexicon body and left only the
front-matter block. Papnoute was generating with no retrieved lexicon content
at all: an Article 5 grounding failure, not a formatting nit.

The fix is not a fourth copy of the boundary rule. It is one primitive, used
by everything that needs it, with both conventions tested. Three operations
are genuinely different and all three are needed:

  find_section    - locate a section's boundaries
  extract_section - the section's own text        (what the indexer needs)
  excise_section  - the body WITHOUT that section (what the retriever needs)
  truncate_at     - the body BEFORE a section     (the Key Sources strip)

Only `excise_section` needs to know where a section ENDS, which is precisely
why it was the one that broke: the other two can stop at the section's start.
"""

from dataclasses import dataclass

# A section runs until the first of: a horizontal rule, a fenced heading, or
# a blank-line-preceded bold label. This is the same triple indexer.py has
# used correctly since S3.1; it is stated once here and imported everywhere.
SECTION_END_MARKERS: tuple[str, ...] = ("\n---", "\n## ", "\n\n**")

# Tried in order; the first one present in the body wins, so a body carrying
# both conventions resolves to the fenced form, exactly as the previous
# hand-rolled copies did.
QUICK_MEANING_MARKERS: tuple[str, ...] = (
    "## Quick Meaning", "**Quick Meaning:**", "**Quick Meaning**",
)
KEY_SOURCES_MARKERS: tuple[str, ...] = (
    "## Key Sources", "**Key Sources:**", "**Key Sources**",
)


@dataclass(frozen=True)
class Section:
    """Where a named section sits inside a chunk body.

    start         - index of the marker itself
    content_start - index just past the marker (where the section's text begins)
    end           - index of the first end-marker after content_start, or
                    len(body) when the section runs to the end of the body.
                    `end == len(body)` is the case the old retriever copy
                    could not distinguish from "marker not found".
    marker        - the marker string that actually matched
    end_marker    - the end marker that won, or None when the section runs to
                    the end of the body
    """

    start: int
    content_start: int
    end: int
    marker: str
    end_marker: str | None


def find_section(body: str, markers: tuple[str, ...]) -> Section | None:
    """Locate the first of `markers` present in `body` and its extent.

    Returns None only when NO marker is present. A present marker whose
    section runs to the end of the body returns a Section with
    end == len(body) - the distinction the R7 bug collapsed.
    """
    for marker in markers:
        start = body.find(marker)
        if start == -1:
            continue
        content_start = start + len(marker)
        end = len(body)
        end_marker = None
        for candidate in SECTION_END_MARKERS:
            pos = body.find(candidate, content_start)
            if pos != -1 and pos < end:
                end = pos
                end_marker = candidate
        return Section(start=start, content_start=content_start, end=end,
                       marker=marker, end_marker=end_marker)
    return None


def extract_section(body: str, markers: tuple[str, ...]) -> str:
    """The named section's own text, or "" when absent.

    The trailing .lstrip(":") handles the bold-label convention, where the
    marker "**Quick Meaning**" may be followed by the colon that the
    "**Quick Meaning:**" spelling includes in the marker itself.
    """
    section = find_section(body, markers)
    if section is None:
        return ""
    return body[section.content_start:section.end].strip().lstrip(":").strip()


def excise_section(body: str, markers: tuple[str, ...]) -> str:
    """`body` with the named section removed, and nothing else changed.

    Removing a section means removing its heading, its text, AND the
    separator that closed it - a horizontal rule that terminated the removed
    section belongs to the removed section, not to whatever follows. Leaving
    it behind produces a body that opens with an orphaned "---": the rule
    below a heading that is no longer there.

    That detail is what makes this byte-identical to the old hand-rolled
    strip on every fenced-heading world (verified against all 60 such
    deployed chunks) while also recovering the bold-label world's body in
    full, instead of trading one convention's correctness for the other's.
    """
    section = find_section(body, markers)
    if section is None:
        return body

    head = body[:section.start].rstrip()
    tail = body[section.end:]

    # Drop the separator line that closed the removed section, if that is
    # what ended it. A fenced heading or bold label that ends the section
    # opens the NEXT section and must be kept.
    if section.end_marker == "\n---":
        tail = tail.lstrip("\n")
        newline = tail.find("\n")
        rule, rest = (tail, "") if newline == -1 else (tail[:newline], tail[newline:])
        if rule.strip() and set(rule.strip()) <= set("-*_"):
            tail = rest

    tail = tail.lstrip()
    return f"{head}\n\n{tail}" if tail else head


def truncate_at(body: str, markers: tuple[str, ...]) -> str:
    """`body` up to (not including) the named section - everything from that
    section to the end of the body is dropped.

    Used for the Key Sources apparatus (S5.2), which must never enter
    generation context and is always the last thing in a chunk. Unlike
    excise_section this never needs the section's END, which is why the old
    hand-rolled Key Sources strip was correct for both conventions and the
    Quick Meaning strip beside it was not.
    """
    section = find_section(body, markers)
    return body if section is None else body[:section.start].rstrip()
