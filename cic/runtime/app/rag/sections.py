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

# A FENCED section ("## Name") may legitimately contain bold labels inside it -
# "## Distortion Risk" holds "**Modern Hearing:**" and "**World Hearing:**" as
# sub-labels, not as the next section. Ending such a section at the first
# "\n\n**" stops it dead at its own first sub-label and reports an extent of a
# few characters where the real section is several hundred. That was harmless
# while the only excised section was Quick Meaning (plain prose in every
# deployed chunk, verified), and becomes wrong the moment anything with
# sub-labels is excised. A BOLD-label section cannot contain another bold
# label - that IS the next section - so it keeps all three end markers.
FENCED_SECTION_END_MARKERS: tuple[str, ...] = ("\n---", "\n## ")

# Tried in order; the first one present in the body wins, so a body carrying
# both conventions resolves to the fenced form, exactly as the previous
# hand-rolled copies did.
QUICK_MEANING_MARKERS: tuple[str, ...] = (
    "## Quick Meaning", "**Quick Meaning:**", "**Quick Meaning**",
)
KEY_SOURCES_MARKERS: tuple[str, ...] = (
    "## Key Sources", "**Key Sources:**", "**Key Sources**",
)

# Voice Rebuild Phase 0.2 (2026-08-08): the fail-closed fallback for
# truncate_at, below. A chunk missing a Key Sources marker entirely used
# to pass its whole tail through unfiltered (the fail-open bug the
# Research-stage leak audit found live in 6 chunks). These are the two
# apparatus-only trailing sections the audit found actually occurring in
# those 6 files - Final Assembly Instruction (IJC's two) and Related-
# Terms Reciprocity Note (Syriac's two; its own text talks about "runtime
# recognizability" and "completeness," builder language, not voice). Both
# conventions listed per this module's own rule, though only the fenced
# form is attested in the corpus today.
TRAILING_APPARATUS_MARKERS: tuple[str, ...] = (
    "## Final Assembly Instruction", "**Final Assembly Instruction:**",
    "**Final Assembly Instruction**",
    "## Related-Terms Reciprocity Note", "**Related-Terms Reciprocity Note:**",
    "**Related-Terms Reciprocity Note**",
)


def _both_conventions(name: str) -> tuple[str, ...]:
    """This module's own rule, applied to one section name."""
    return (f"## {name}", f"**{name}:**", f"**{name}**")


# Build-record sections that must never reach the Representative's prompt.
# Distinct from KEY_SOURCES (citation apparatus) and QUICK_MEANING (deduped
# against the cached prefix): these are commentary written FOR A BUILDER about
# why a chunk matters to the world build, and the Representative has no use
# for any of it.
#
# "Distortion Risk" is the load-bearing one and is removed on grounds of
# coherence before cost. Its body is written as "A modern reader hears X..." -
# it hands the Representative explicit knowledge of how a modern participant
# thinks, which is precisely what the permanent prompt's Total Embeddedness
# rule forbids ("You do not know you are a reconstruction. You do not know you
# are mediated by AI."). FLAG-018 is the observed consequence: the voice read
# the apparatus as a task and opened turns with unprompted sense-clarifications
# for terms nobody had spoken. The compensating instruction written to suppress
# that shipped in the dynamic prompt on every single turn; removing the cause
# lets the instruction go with it.
#
# Deliberately NOT listed, though they read like apparatus by name:
#   Usage Guidance   - carries real anti-fabrication constraints for the voice
#   Absent Story Note - tells the voice what NOT to invent when asked
#   Plural-Voices Note - attribution honesty, which the voice must carry
#   Source Identification / Tier Justification / Final Assembly Instruction
#                    - already stripped at index time by StoryIndexer
VOICE_APPARATUS_LEXICON_SECTIONS: tuple[str, ...] = (
    "Distortion Risk", "Ecological Function",
)
VOICE_APPARATUS_STORY_SECTIONS: tuple[str, ...] = (
    "Formation Ecology Connection",
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
        ends = (FENCED_SECTION_END_MARKERS if marker.startswith("## ")
                else SECTION_END_MARKERS)
        for candidate in ends:
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


def truncate_at(body: str, markers: tuple[str, ...], *,
                fail_closed: bool = True) -> str:
    """`body` up to (not including) the named section - everything from that
    section to the end of the body is dropped.

    Used for the Key Sources apparatus (S5.2), which must never enter
    generation context and is always the last thing in a chunk. Unlike
    excise_section this never needs the section's END, which is why the old
    hand-rolled Key Sources strip was correct for both conventions and the
    Quick Meaning strip beside it was not.

    fail_closed (Voice Rebuild Phase 0.2, 2026-08-08): when none of
    `markers` matches, the body used to pass through unfiltered - fail-open,
    and the reason 6 chunks with no Key Sources marker at all were shipping
    their build-apparatus tail verbatim (the Research-stage leak audit's
    own finding). Fail-closed instead checks TRAILING_APPARATUS_MARKERS as
    a fallback and cuts at whichever candidate - primary or fallback -
    appears EARLIEST by position (not by which tuple it came from; a chunk
    could in principle carry both). Only when nothing in either tuple
    appears at all does the body pass through unchanged - the genuinely
    clean case, not a failure to detect one. Pass fail_closed=False to
    restore the old behavior for a caller that needs it (none do today).
    """
    section = find_section(body, markers)
    if section is not None:
        return body[:section.start].rstrip()
    if not fail_closed:
        return body
    earliest = None
    for marker in TRAILING_APPARATUS_MARKERS:
        pos = body.find(marker)
        if pos != -1 and (earliest is None or pos < earliest):
            earliest = pos
    return body if earliest is None else body[:earliest].rstrip()


# Below this, a body has no substance left to ground an answer on. Used by
# excise_sections to refuse an excision that would empty a chunk out.
MIN_VOICE_BODY_CHARS = 200


def excise_sections(body: str, section_names: tuple[str, ...]) -> str:
    """`body` with each named section removed, in both conventions.

    A section that is absent is simply skipped, so this is idempotent and
    safe to run over content another stage may already have stripped.

    FAIL-SAFE: if removing the apparatus would leave nothing to speak from,
    the original body is returned untouched. Eight deployed lexicon chunks
    (pahclex012, pahclex013, syrlex005, syrlex008, desertlex013,
    desertlex017, desertlex018, ijclex011) carry no World Meaning section at
    all - or an empty one - so their entire substance sits inside what this
    function is otherwise asked to strip. Removing it would hand the Representative a chunk with
    no content, which is the Article 5 grounding failure this module was
    written to stop happening a second time; paying for the apparatus on
    those few chunks is strictly the better failure. The chunks themselves
    need authoring attention - that is a records problem, not a runtime one,
    and this guard must not be read as making it go away.
    """
    original = body
    for name in section_names:
        body = excise_section(body, _both_conventions(name))
    body = _drop_trailing_rule(body)
    if len(body.strip()) < MIN_VOICE_BODY_CHARS < len(original.strip()):
        return original
    return body


def _drop_trailing_rule(body: str) -> str:
    """Remove a horizontal rule left dangling at the end of a body.

    excise_section drops the rule that CLOSED the section it removed, which
    is correct. It cannot drop the rule that OPENED it - that rule closed the
    section before, and while that section stands the rule belongs to it. But
    when the removed section was the last thing in the body, that opening rule
    is now trailing nothing, and the caller appends its own separator directly
    after it. Cheaper to tidy here than to make excise_section reason about
    what follows it.
    """
    stripped = body.rstrip()
    while True:
        nl = stripped.rfind("\n")
        last = stripped[nl + 1:].strip()
        if not last or not (set(last) <= set("-*_") and len(last) >= 3):
            return stripped
        stripped = stripped[:max(nl, 0)].rstrip()
