"""Repair transcript-format leakage in a representative's own turn.

THE DEFECT, and why it is deterministic repair rather than a prompt fix.
Measured 2026-08-10 across the six T2/T3 arms (Ministry/Technology/Table/
runs/), counting representative turns only:

    arm                            model    leading-label  mid-turn-label
    pre1A-table                    Sonnet         0              0
    sonnet-v4-table                Sonnet         0              0
    haiku-current-table            Haiku          2              2
    haiku-v4-table                 Haiku          3              1
    haiku-v4-guard-table           Haiku          3              1
    haiku-v4-guard-fabgate-table   Haiku         12              2
    ship-regression                Haiku          6              1

Zero in every Sonnet arm; present in every Haiku arm, at up to 21% of
turns. The representative is writing the PUBLIC TRANSCRIPT'S OWN FORMAT
into its answer, because that format is what it reads in context. Two
shapes, and the second is the serious one:

  leading label   the turn opens "Chloe: You are reading truly..." - the
                  speaker announcing itself, which the UI already does.
                  Cosmetic on its own.

  mid-turn label  the turn continues "\n\nPapnoute: The sickness we saw
                  was the keeping..." - one representative writing
                  ANOTHER world's dialogue inside its own turn. This is
                  not cosmetic. Facilitator Governance calls the
                  public-transcript isolation "the boundary that makes
                  the table constitutionally sound": only spoken words
                  cross between representatives, and no world ever speaks
                  for another. A turn that ventriloquises another world
                  breaches exactly that, and the participant cannot tell
                  it from a real exchange.

It also cascades. Once a leaked label reaches the transcript, the next
speaker reads it and reacts: in the ship-regression run Mar Yausep spent
a whole turn telling the participant "That is not Chloe's voice. That is
my own voice put into her mouth. I wrote a sentence labeled 'Chloe:'..."
- a Representative narrating its own generation failure to a seeker.
Removing the cause removes that whole class.

WHY REPAIR AND NOT A PROMPT INSTRUCTION. The prompts already say to
speak only as yourself, at length, in several places; the Sonnet arms
obey and the Haiku arms do not, which is the documented shape of
smaller-model instruction-following under dense negative constraint
(Pass 3's cost-floor model warned exactly this). A deterministic repair
costs nothing, cannot regress, and does not spend more of the prompt
budget on a rule that is already there.

DELIBERATELY NARROW. Only a seated representative's display name, only
at the very start of the text or at the start of a line, only when
followed by a colon. Everything else is left exactly as generated - this
never rewrites a Representative's words, it only removes a format
artifact and cuts a turn where it stopped being that voice's own.
"""
import re

from app.speaker_label_repair_logging import (
    OUTCOME_LEADING_STRIPPED, OUTCOME_TRUNCATED, log_speaker_label_repair,
)


def _label_pattern(names: list[str]) -> re.Pattern:
    alt = "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True) if n)
    return re.compile(rf"^[ \t]*({alt})[ \t]*:[ \t]*", re.MULTILINE)


def repair_speaker_labels(
    text: str,
    own_display_name: str | None,
    other_display_names: list[str],
    *,
    world_id: str | None = None,
    request_id: str | None = None,
    session_id: str | None = None,
) -> str:
    """Strip a leading speaker label and cut anything spoken in another
    voice's name. Returns the repaired text (unchanged when clean).

    own_display_name: this speaker's display name ("Chloe").
    other_display_names: the other seated representatives' display names.
        Only these are treated as impersonation boundaries - an arbitrary
        capitalised word followed by a colon is left alone.

    A truncation that would leave nothing is NOT applied: an empty turn
    corrupts every later turn that reads it out of the public transcript
    (the same reason stream_representative_turn retries a blank stream),
    so in that case the original text stands and the outcome is logged
    for the pilot watch rather than silently swallowed.
    """
    if not text:
        return text
    names = [n for n in ([own_display_name] + list(other_display_names)) if n]
    if not names:
        return text
    original = text
    pattern = _label_pattern(names)

    # 1. a label at the very start is this speaker announcing itself
    leading = pattern.match(text)
    stripped_leading = None
    if leading:
        stripped_leading = leading.group(1)
        text = text[leading.end():]

    # 2. any FURTHER label at a line start begins someone else's turn
    truncated_at = None
    nxt = pattern.search(text)
    if nxt:
        head = text[:nxt.start()].strip()
        if head:
            truncated_at = nxt.group(1)
            text = head
        # else: the whole turn is another voice's - leave it, log it,
        # and let the post-round watch and the pilot see it rather than
        # emitting an empty message.

    if stripped_leading or truncated_at:
        log_speaker_label_repair(
            world_id,
            OUTCOME_TRUNCATED if truncated_at else OUTCOME_LEADING_STRIPPED,
            stripped_label=stripped_leading, truncated_at=truncated_at,
            original_words=len(original.split()),
            repaired_words=len(text.split()),
            request_id=request_id, session_id=session_id,
        )
    return text
