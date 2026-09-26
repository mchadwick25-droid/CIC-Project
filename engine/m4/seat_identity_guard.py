"""Detects a generated voice turn writing itself as the Facilitator or
another seated voice - the constitutional-boundary breach Facilitator
Governance names (a Representative speaking outside its own witness, under
another name, uncited). Confirmed live (a
Table turn labelled Papnoute that opened "The Facilitator: Papnoute has
already given his witness..." and continued "Theon (Alexandrian
Christianity): In practice, it meant...", zero citation marks on the whole
block) and, in a milder shape (a seat prefixing its OWN label onto its own
turn), in a live-table-battery report
(engine/m4/reports/live-table-battery-F1-2026-08-28.json, probe
L4-no-foreknowledge: "Papnoute (Desert Monasticism): Theon has answered you
rightly..."). A pre-existing defect class, not a regression.

This module guards against the Facilitator's own label and every OTHER
seated voice's label - never the speaking voice's own label. A voice
prefixing its OWN name onto its own turn (the "leading
label" case above) is a separate, milder, cosmetic defect, out of this guard's
scope: it never breaches the isolation
property this guard exists to hold, since the voice is still only ever
speaking as itself.

A caught label must sit at a line start or right after a sentence-ending
punctuation + whitespace - the two positions a real attributed-transcript
line can open at (engine.api.table_wiring._labels builds exactly this
"Name (World): text" / "The Facilitator: text" convention, fed to a voice
via context_prefix/history; the leak is almost certainly the model echoing
a format it was shown). A bare substring occurrence - a voice writing the
WORD "Facilitator" or another seat's own name in running prose - is not
the defect and must not be caught; only the attributed dialogue-tag SHAPE
is. This is a real, accepted tradeoff of the bare "<Name>:" pattern in
particular: a sentence that happens to end
right before a seat's bare name followed by a colon mid-prose ("Ask
Theon. Theon: he's usually right") would false-positive. Accepted as
specified rather than narrowed further - the real leaks this guard exists
to catch are worth one rare, harmless extra regeneration.
"""
import re


def _label_pattern(label: str) -> str:
    return re.escape(label) + r":"


def _guard_regex(labels: list[str]) -> re.Pattern:
    alternation = "|".join(_label_pattern(label) for label in labels)
    # MULTILINE so ^ matches every line start, not just the string's own
    # start - a leak partway down a paragraph (the confirmed staging case)
    # is exactly as much the defect as one opening the whole turn.
    return re.compile(rf"(?:^|(?<=[.!?]\s))({alternation})", re.MULTILINE)


def find_seat_identity_violation(text: str, labels: list[str]) -> str | None:
    """Returns the exact offending prefix caught (the matched label plus
    its colon), or None if text is clean against every label in `labels`.
    `labels` is built by the caller per turn (Facilitator + every OTHER
    seated voice, both its full "Name (World)" label and its bare name) -
    this function holds no seating knowledge of its own, so it is equally
    usable from a two-seat or three-seat table, or (with an empty/None
    `labels`) not at all, which is how the interview path stays untouched."""
    if not labels or not text:
        return None
    match = _guard_regex(labels).search(text)
    return match.group(1) if match else None
