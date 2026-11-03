"""The reading context: what each offered quote and story carries into the
evidence block when a world's frame sets `reading_context`. It changes what
an offered item shows, never which items are offered.

The additions:
- the guidance lines, at the head of the block;
- on each quote line not yet voiced, the quote's modern rendering;
- under each record that has one, its "Reads differently today" line: the
  card's `reads_differently_today`, or else the record's `modern_lens_note`;
- under each record with a reading card, the card's other lines;
- under the two highest-ranked offered quotes or stories, their context
  windows (engine.m4.fit_step.context_blocks, or, for a locus that names no
  vendored span, engine.m4.source_windows.context_blocks), marked as
  context, never evidence.

Cards and lens notes are stripped at compile, so they come from the mapping
engine.m4.reading_cards.load_reading_context returns, never from the package.

The budget. The additions run to ADDITIONS_CAP characters or fewer, counted
as the block's length with them less its length without them. Over the cap,
context windows are dropped first, then the card lines other than "Reads
differently today", each from the lowest-ranked record up. The guidance
lines, the renderings and the "Reads differently today" lines are always
kept.

The whole-world signal. whole_world_signal counts the answer's sentences that
speak for the whole world while every record they cite has a card whose
`whose_view` marks a single author. A sentence speaks for the whole world when
it holds one of WHOLE_WORLD_PHRASES, matched as whole words with case ignored.
A `whose_view` marks a single author when it matches one of
SINGLE_AUTHOR_MARKS and none of SHARED_MARKS. The marks are: a named
person's own view ("Origen's scheme", "Clement's picture", "Eusebius's
narrative"), unless "not" stands before it, or a named person arguing
("Origen argues"); one person named by role ("A
bishop's ruling", "One gifted pupil", "An outsider's late memory"); a view
known only through one witness ("known only through him", "Only Dionysius's
side survives"); and a denial of breadth ("not the community's", "not every
reader's", "not most Christians'"). A view said to be shared ("is shared",
"runs through", "widely shared") or the people's ("deferring to his
people's esteem") is not single-author. The count is reported
only; nothing is removed.
"""
import re
from dataclasses import dataclass, field

from engine.m4 import fit_step, source_windows

READING_CONTEXT = "reading_context"
ADDITIONS_CAP = 12000
CONTEXT_ITEMS = 2
CONTEXT_RECORD_TYPES = ("quote", "story")
TEXTS_ROOT = fit_step.REPO_ROOT

GUIDANCE = (
    "Answer what the visitor asked, first and plainly.",
    "Draw the offered sources and our ground together: connect them, explain how belief and practice fit, "
    "and say what we understand them to mean.",
    "Keep apart what a source says, what we understand it to mean, and what was disputed or uncertain, in plain words.",
    "Say whose view a source gives, and how widely it was shared, only as far as its card or record says.",
    "Read the surrounding text to understand a passage; cite the record, not the text around it.",
)

CARD_LABELS = (
    ("setting", "Setting"),
    ("source_says", "The source says"),
    ("historians_conclude", "Historians conclude"),
    ("contributes", "What it adds"),
    ("whose_view", "Whose view"),
    ("open", "Open or disputed"),
)

WHOLE_WORLD_PHRASES = (
    "we held", "we hold", "we believed", "we believe", "we taught", "we teach", "we confessed", "we confess",
    "we kept", "we keep", "we all", "all of us", "our churches", "our church", "our people", "our faith",
    "our tradition", "our community", "the whole church", "every church", "all our",
)

_VIEW_NOUNS = (
    "own", "personal", "view", "views", "argument", "case", "picture", "scheme", "judgment", "judgement", "rhetoric",
    "framing", "speculation", "narrative", "wording", "ruling", "rulings", "account", "tribute", "side", "praise", "memory",
)
_ONE_VOICE = ("teacher", "bishop", "pupil", "author", "writer", "voice", "outsider", "man", "woman")

SINGLE_AUTHOR_MARKS = (
    r"(?<!not )\b[A-Z][a-z]+(?:'s|’s|s') (?:" + "|".join(_VIEW_NOUNS) + r")\b",
    r"(?i:\b(?:one|a|an|the|a single)(?:\s+\w+)?\s+(?:" + "|".join(_ONE_VOICE) + r")(?:'s|’s)?\b)",
    r"\b[A-Z][a-z]+ (?:argues|writes|claims|speculates)\b",
    r"(?i:\bonly\s+(?:through|by)\s+(?:him|her|them)\b)",
    r"\b(?i:only)\s+[A-Z][a-z]+(?:'s|’s)?\s+(?i:side|reports|report|records)\b",
    r"(?i:\bnot\s+(?:automatically\s+)?(?:the\s+community|every|most|the\s+whole|shared|widely\s+shared)\b)",
)
SHARED_MARKS = (
    r"(?i:(?<!not )\bwidely\s+shared\b)", r"(?i:\bis\s+shared\b)", r"(?i:\bshared\s+across\b)", r"(?i:\bruns\s+through\b)",
    r"(?i:\bcommon\s+to\b)", r"(?i:\b(?:his|her|their|the)\s+people(?:'s|’s)\b)",
)


def _phrases(phrases: tuple[str, ...]) -> re.Pattern:
    return re.compile(r"\b(?:" + "|".join(re.escape(p).replace(r"\ ", r"\s+") for p in phrases) + r")\b", re.IGNORECASE)


_WHOLE_WORLD = _phrases(WHOLE_WORLD_PHRASES)
_SINGLE_AUTHOR = re.compile("|".join(SINGLE_AUTHOR_MARKS))
_SHARED = re.compile("|".join(SHARED_MARKS))


def is_on(world) -> bool:
    return world is not None and bool((getattr(world, "frame", None) or {}).get(READING_CONTEXT))


def _clean(text) -> str:
    return " ".join(str(text or "").split())


def _line_chars(lines: list[str]) -> int:
    return sum(len(line) + 1 for line in lines)


@dataclass
class ReadingPlan:
    """What the block gains: the guidance lines, a suffix for each quote line,
    and the lines under each record, after the budget."""
    guidance: list[str]
    renderings: dict[str, str] = field(default_factory=dict)
    today: dict[str, str] = field(default_factory=dict)
    cards: dict[str, list[str]] = field(default_factory=dict)
    context: dict[str, list[str]] = field(default_factory=dict)
    windows: dict[str, list[dict]] = field(default_factory=dict)

    def under(self, record_id: str) -> list[str]:
        today = [self.today[record_id]] if record_id in self.today else []
        return self.cards.get(record_id, []) + today + self.context.get(record_id, [])

    def chars(self) -> int:
        return (
            _line_chars(self.guidance) + sum(len(s) for s in self.renderings.values()) + _line_chars(list(self.today.values()))
            + sum(_line_chars(v) for v in self.cards.values()) + sum(_line_chars(v) for v in self.context.values())
        )

    def summary(self) -> dict:
        """What was added, for the run record: counts, and each context window kept."""
        return {
            "renderings": len(self.renderings),
            "reads_differently_today": len(self.today),
            "card_lines": sum(len(v) for v in self.cards.values()),
            "context_windows": [
                {k: block[k] for k in ("record_id", "file", "lines")} | {"trimmed": bool(block.get("trimmed"))}
                for rid in self.context for block in self.windows.get(rid, [])
            ],
            "chars": self.chars(),
        }


def _voiced(candidate: dict) -> bool:
    return bool(candidate.get("used_in_round") or candidate.get("already_told_this_session"))


def rendering_suffix(record: dict) -> str:
    rendering = _clean(record.get("modern_rendering"))
    return f" | in modern English: {rendering}" if rendering else ""


def today_line(entry: dict | None) -> str:
    """The "Reads differently today" line: the card's, or, with none, the record's lens note."""
    entry = entry or {}
    card = entry.get("reading_card") if isinstance(entry.get("reading_card"), dict) else {}
    today = _clean(card.get("reads_differently_today")) or _clean(entry.get("modern_lens_note"))
    return f"  Reads differently today: {today}" if today else ""


def card_lines(record_id: str, entry: dict | None, offered: set[str]) -> list[str]:
    """The card's lines under a record, other than "Reads differently today".
    `complicated_by` names only the records offered this turn."""
    entry = entry or {}
    card = entry.get("reading_card") if isinstance(entry.get("reading_card"), dict) else {}
    lines = []
    for key, label in CARD_LABELS:
        value = card.get(key)
        if key == "historians_conclude" and isinstance(value, dict):
            text, confidence = _clean(value.get("text")), _clean(value.get("confidence"))
            if text:
                lines.append(f"  {label}" + (f" ({confidence})" if confidence else "") + f": {text}")
        elif isinstance(value, str) and _clean(value):
            lines.append(f"  {label}: {_clean(value)}")
    qualifying = [rid for rid in card.get("complicated_by") or [] if rid in offered and rid != record_id]
    if qualifying:
        lines.append(f"  Complicated by: {', '.join(qualifying)}")
    return lines


def plan_additions(candidates: list[dict], repository_records: dict[str, dict], reading: dict[str, dict]) -> ReadingPlan:
    """The additions for the offered candidates, in offered order, cut to the budget."""
    offered = {c["id"] for c in candidates}
    plan = ReadingPlan(guidance=[f"## {line}" for line in GUIDANCE])
    ranked: list[str] = []
    context_left = CONTEXT_ITEMS
    for candidate in candidates:
        rid = candidate["id"]
        record = repository_records.get(rid) or {}
        record_type = candidate.get("record_type")
        if record_type not in CONTEXT_RECORD_TYPES:
            continue
        ranked.append(rid)
        if record_type == "quote" and not _voiced(candidate) and (suffix := rendering_suffix(record)):
            plan.renderings[rid] = suffix
        if line := today_line(reading.get(rid)):
            plan.today[rid] = line
        if lines := card_lines(rid, reading.get(rid), offered):
            plan.cards[rid] = lines
        if context_left:
            context_left -= 1
            blocks = fit_step.context_blocks(record, TEXTS_ROOT) or source_windows.context_blocks(record, repository_records, TEXTS_ROOT)
            if lines := fit_step.context_lines({"context": blocks}):
                plan.context[rid] = lines
                plan.windows[rid] = blocks
    for tier in (plan.context, plan.cards):
        for rid in reversed(ranked):
            if plan.chars() <= ADDITIONS_CAP:
                return plan
            tier.pop(rid, None)
    return plan


def single_author(entry: dict | None) -> bool:
    card = (entry or {}).get("reading_card")
    view = str(card.get("whose_view") or "") if isinstance(card, dict) else ""
    return bool(_SINGLE_AUTHOR.search(view)) and not _SHARED.search(view)


def whole_world_signal(citation_entries: list[dict], reading: dict[str, dict]) -> dict:
    """The answer's sentences that speak for the whole world while each record
    they cite has a single-author card: their count and the sentences."""
    sentences = [
        entry.get("sentence") or ""
        for entry in citation_entries or []
        if entry.get("record_ids") and _WHOLE_WORLD.search(entry.get("sentence") or "")
        and all(single_author(reading.get(rid)) for rid in entry["record_ids"])
    ]
    return {"count": len(sentences), "sentences": sentences}
