"""The conversation's rhythm, read from the session's own transcript events
(decision 60): when a quote was last voiced, which quotes and stories the
conversation has already used, and when a figure was last introduced. The
tally is recomputed from the transcript on every turn and never stored.

A round is one participant message and every reply to it. A quote is
"voiced" and a story "told" when the reply's transparency plan marked it
inline, so a record only cited at the end of a reply does not count.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

QUOTE_INTERVAL = 3
FIGURE_INTERVAL = 3

_WORDS_ASKED = re.compile(r"\b(say|says|said|put it|their own words|word for word)\b", re.IGNORECASE)
_WORD_USE_ASKED = re.compile(r"\bhow\b.*\b(used|use|using)\b", re.IGNORECASE)


@dataclass(frozen=True)
class RhythmTally:
    round_no: int = 1
    quotes_voiced: dict[str, int] = field(default_factory=dict)
    stories_told: dict[str, int] = field(default_factory=dict)
    figures_introduced: dict[str, int] = field(default_factory=dict)
    figures_asked: frozenset[str] = frozenset()

    @property
    def quote_due(self) -> bool:
        """Three or more rounds since the last voiced quote, or none yet."""
        if not self.quotes_voiced:
            return True
        return self.round_no - max(self.quotes_voiced.values()) >= QUOTE_INTERVAL

    @property
    def figure_gate_closed(self) -> bool:
        """A figure was introduced within the last three rounds, and this
        question is not itself about a figure not yet introduced."""
        if self.figures_asked:
            return False
        return any(self.round_no - r < FIGURE_INTERVAL for r in self.figures_introduced.values())

    def used_round(self, record_id: str) -> tuple[str, int] | None:
        """("voiced" | "told", round) for a quote or story the conversation already used."""
        if record_id in self.quotes_voiced:
            return "voiced", self.quotes_voiced[record_id]
        if record_id in self.stories_told:
            return "told", self.stories_told[record_id]
        return None


def tally_from_transcript(
    transcript: list[dict] | None, *, speaker: str | None = None, question_recorded: bool = False
) -> RhythmTally:
    """The tally for the round about to be answered. `transcript` is the
    session projection's own transcript; `speaker` limits voice turns to one
    world's (the Table keeps a tally per seat); `question_recorded` says the
    transcript already holds this round's participant message (the Table
    does, an interview turn does not yet)."""
    round_no = 0
    quotes: dict[str, int] = {}
    stories: dict[str, int] = {}
    figures: dict[str, int] = {}
    for entry in transcript or []:
        who = entry.get("speaker")
        if who == "participant":
            round_no += 1
            continue
        if who == "facilitator" or (speaker is not None and who != speaker):
            continue
        for element in (entry.get("transparency") or {}).get("elements") or []:
            target = quotes if element.get("kind") == "quote" else stories if element.get("kind") == "story" else None
            if target is not None:
                target.setdefault(element["record_id"], max(round_no, 1))
        for figure in entry.get("figures_used") or []:
            figures.setdefault(figure["id"], max(round_no, 1))
    return RhythmTally(
        round_no=round_no if question_recorded else round_no + 1,
        quotes_voiced=quotes, stories_told=stories, figures_introduced=figures,
    )


def asks_for_the_words(kind: str | None, message: str) -> bool:
    """The question asks for the world's own words, so a quote is due
    whatever the count."""
    if kind in ("what_did", "what_happened"):
        return bool(_WORDS_ASKED.search(message or ""))
    if kind == "what_means":
        return bool(_WORD_USE_ASKED.search(message or ""))
    return False
