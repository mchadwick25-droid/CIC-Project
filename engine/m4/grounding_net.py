"""Live-turn grounding for CITATION-TAGGED output (Live-Generation Design
§6 - see engine/m4/LIVE-GENERATION-DESIGN.md §9.5, all four forks signed
off). Promoted from the design's own companion prototype
(grounding_experimental.py, claude/cic-design-assignment-ecoxh2), which
proved this exact logic against the real alx package (§6.2's run log) -
ported unchanged except this docstring; the calibration history below is
that prototype's own postmortem, kept because it is why the module is
shaped this way, not just how it got here.

What it checks is the design's output contract: the voice generates each
sentence with inline citation tags naming the record(s) that sentence draws
on - ``... the same bread, the same cup [[alx.term.eucharistia]].`` - tags
BEFORE the terminal punctuation, so a naive sentence splitter keeps a tag
inside its own sentence. The runtime strips tags before any participant
sees text; this module is what looks at them first.

Why this is sharper than the record-level experimental gate it descends
from (engine/m1/gates_experimental.gate_grounded_claim): that gate checks a
sentence against the union of EVERYTHING its record cites, so a sentence
can free-ride on words contributed by a source it never actually drew on.
Here every sentence names its own ground, so the grounding ratio is scoped
to exactly the records the sentence itself claims.

Calibrated against the real alx package (the run log is in the design doc):
the fabricated door line, tagged with the two records it originally cited,
comes back 28% grounded -> withheld; the corrected line clears the floor
against its three real sources at 40%; both licensed-quote sentences pass
by verbatim window-match rather than ratio (framing words around a real
quote should never sink a real quote). Three defects the first draft of
THIS module showed against real data, fixed here and worth keeping named
(the same discipline as the m1 module's v1 postmortem):
  1. a "marginal band" between floor/2 and floor let the one known real
     fabrication stream with only its badge withheld - removed; below the
     floor is withheld, full stop, and the quote-verbatim check carries
     the legitimate cases that used to need the band;
  2. the naive sentence splitter broke inside quotations ('...stones!'
     split mid-quote), orphaning a tag from the claim it grounded - the
     splitter now merges sentences until quotes balance;
  3. a sentence-initial figure name ("Clement wrote a whole book...")
     escaped the capitalization heuristic for proper nouns - a compiled
     figure-name lexicon (from the package's own figure records) now
     catches attributions positionally-blind.

Deterministic, no model call, string ops only - cheap enough to run inside
the streaming path per sentence. The claim-detection, scaffold/self-naming
exemptions, stopword list, and grounding floor are imported from the m1
experimental module unchanged: one implementation of "does this sentence
even make a checkable claim," owned once.
"""
import re

from engine.m1.quote_verbatim import normalize_archaic_letterforms
from engine.prose import (
    SCAFFOLD_MARKERS,
    SELF_NAMING_MARKER,
    WITHHOLD_FLOOR,
    all_text,
    claim_markers,
    content_words,
    grounding_ratio,
    quote_aware_sentences,
)

# [[world.type.slug]] - record ids are dotted lowercase tokens; the tag
# grammar deliberately has no spaces so sentence splitting never breaks
# inside a tag.
_TAG = re.compile(r"\[\[([a-z0-9_.-]+)\]\]")

# An opener with no closing "]]" anywhere after it - not a malformed tag
# (engine.m4.output_check's _ANY_TAG already reports those; a different,
# already-handled defect, since that one still has both brackets). This is
# what a generation call cut off mid-tag leaves behind: Bedrock's own
# stream ending inside "[[world.type.slug" with no "]]" ever sent. _TAG's
# grammar requires the close - deliberately, so a tag it resolves and a
# tag strip_tags removes can never disagree about what counts as one - so
# an opener that never closed is never matched by either, and unlike
# _ANY_TAG (which needs no closing bracket to be well-formed, just to be
# present) there is no complete pattern here to widen to catch it. A real
# generation call cut off exactly this way once, while rebuilding a Table
# transcript for transparency markup: one turn's raw text ended inside an
# unclosed "[[don.dw.room-for-diss", which strip_tags' own re.sub below
# left untouched, verbatim, brackets and all.
_DANGLING_TAG = re.compile(r"\[\[(?:\s*quote\s*:\s*)?[a-z0-9_.-]*\Z", re.IGNORECASE)


def _drop_truncated_tail(text: str) -> tuple[str, bool]:
    """Back a generation cut off mid-tag off to the last sentence this turn
    actually finished, so the one shape _TAG's own grammar can never catch
    (an opener with no matching close) never reaches a participant as raw
    "[[..." syntax.

    This module's design always places a tag BEFORE its sentence's
    terminal punctuation (this file's own top docstring), so an opener
    with no close means that sentence's own close was cut too - the same
    truncation event, not two separate defects. An unclosed tag can only
    ever occur at the very end of a raw stream (that is where generation
    stopped), so the one thing known for certain is the last `.`/`!`/`?`
    before it: the last sentence the voice actually finished. Everything
    after that boundary was never confirmed complete and does not stream.

    Returns (text, truncated) rather than truncating quietly - REPORTS,
    NEVER EDITS is this module's own rule, and a report that never fires
    when an edit happens is not honouring it. Ordinary text with no
    dangling opener returns unchanged, truncated=False."""
    match = _DANGLING_TAG.search(text)
    if not match:
        return text, False
    kept = text[: match.start()]
    last_stop = max(kept.rfind("."), kept.rfind("!"), kept.rfind("?"))
    return (kept[: last_stop + 1] if last_stop != -1 else ""), True


# A quote marker, [[quote:<record id>]]: where the voice asks for a quote
# record's rendering to be placed (engine.m4.quote_placement).
QUOTE_MARKER = re.compile(r"\[\[\s*quote\s*(?::[^\]\[]*)?(?:\]\]|\Z)", re.IGNORECASE)
_DISPLAY_TAG = re.compile(rf"\s*(?:\[\[[a-z0-9_.-]+\]\]|(?i:{QUOTE_MARKER.pattern}))")


def strip_tags(text: str) -> str:
    """The display transform: what the participant-facing stream emits.
    Record tags and quote markers both come off."""
    text, _ = _drop_truncated_tail(text)
    return _DISPLAY_TAG.sub("", text)


# The reply is spoken prose. Markdown that reaches a reader shows as literal
# asterisks, a stray rule or a heading, and a bold line naming a work and
# its locus reads as a citation the voice typed. Headings, rules, block
# quotes and short standalone bold or italic label lines come off whole; an
# emphasised span carrying a locus (a digit: "Institutes V.26") is a
# citation label and goes whole; any other emphasis loses its marks and
# keeps its words. Record tags and quote markers pass through untouched.
# engine.m4.output_check still reports any markdown that survives this.
_HIDDEN_TAG = "\u0000{}\u0000"
_BOLD = re.compile(r"(\*\*|__)(?=\S)(.+?)(?<=\S)\1", re.DOTALL)
_ITALIC_STAR = re.compile(r"(?<![\w*])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![\w*])", re.DOTALL)
_ITALIC_UNDERSCORE = re.compile(r"(?<![\w_])_(?=[^\s_])(.+?)(?<=[^\s_])_(?![\w_])", re.DOTALL)
_HEADING = re.compile(r"^\s{0,3}#{1,6}(?:\s|$)")
_RULE = re.compile(r"^\s*(?:[-*_]\s*){3,}$")
_WHOLE_EMPHASIS = re.compile(r"^\s*(?:\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)(?:\*\*|__|\*|_)\s*$")
_LABEL_MAX_WORDS = 12


def _unwrap_emphasis(text: str) -> str:
    def inner(match: re.Match) -> str:
        words = match.group(match.lastindex)
        return "" if re.search(r"\d", words) else words

    previous = None
    while previous != text:
        previous = text
        text = _BOLD.sub(inner, text)
        text = _ITALIC_STAR.sub(inner, text)
        text = _ITALIC_UNDERSCORE.sub(inner, text)
    return text


def strip_markdown(raw_text: str) -> str:
    """The voice's raw tagged text as spoken prose (see the note above)."""
    tags: list[str] = []

    def hide(match: re.Match) -> str:
        tags.append(match.group(0))
        return _HIDDEN_TAG.format(len(tags) - 1)

    text = re.sub(r"\[\[[^\]\[]*(?:\]\]|\Z)", hide, raw_text or "")
    lines = []
    for line in text.split("\n"):
        if _HEADING.match(line) or _RULE.match(line) or line.lstrip().startswith(">"):
            continue
        whole = _WHOLE_EMPHASIS.match(line)
        if whole:
            body = whole.group(1).strip()
            if len(body.split()) <= _LABEL_MAX_WORDS and not re.search(r"[.!?][\"'\u201d\u2019)]*$", body):
                continue
        line = _unwrap_emphasis(line)
        lines.append(re.sub(r"[ \t]{2,}", " ", line).rstrip())
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return re.sub(r"\u0000(\d+)\u0000", lambda m: tags[int(m.group(1))], text)


# Beyond the markdown above, the text is not rewritten, with two exceptions:
# quotation marks round a short span (a term or a phrase) found in no record
# come off, and a sentence that carries words attributed to someone, other
# than a quote placed by code, is dropped (QUOTATION_DROP_REASONS). A
# complete but malformed tag ([[THIN GROUND: ...]]) is not edited here;
# engine.m4.output_check reports it.
_DOUBLE_OPENERS = "\"\u201c"
_CLOSERS = {
    '"': re.compile(r"""(?<=\S)["\u201d](?=[\s.,;:!?)]|$)"""),
    "\u201c": re.compile(r"""(?<=\S)[\"\u201d](?=[\s.,;:!?)]|$)"""),
    "'": re.compile(r"""(?<=\S)['\u2019](?=[\s.,;:!?)]|$)"""),
    "\u2018": re.compile(r"""(?<=\S)['\u2019](?=[\s.,;:!?)]|$)"""),
    "\u00ab": re.compile("\u00bb"),
    "\u2039": re.compile("\u203a"),
    "\u201e": re.compile(r"""(?<=\S)[\u201c\u201d"](?=[\s.,;:!?)]|$)"""),
}
# Guillemets and the low opening mark are never anything but quotation marks
# in English prose; a guillemet may stand apart from its words (« like this »).
_QUOTE_OPEN = re.compile(r"""(?:^|[\s:,\-(])(?:['"\u201c\u2018\u201e]|[\u00ab\u2039]\s?)(?=\S)""")
FOREIGN_QUOTE_MARKS = "\u00ab\u00bb\u2039\u203a\u201e"
_PLURAL_POSSESSIVE = re.compile(r"s['\u2019]\s+[A-Za-z]")


def _closing_mark(text: str, opener: str, start: int) -> int | None:
    """Index of the mark that closes a quotation opened by `opener`: a double
    opener closes only on a double mark, skipping any complete double
    quotation nested inside it; a single opener skips a plural possessive
    (the apostles' teaching) unless nothing else closes it."""
    if opener in _DOUBLE_OPENERS:
        return _closing_double_mark(text, start)
    pos = start
    skipped = None
    while True:
        match = _CLOSERS[opener].search(text, pos)
        if not match:
            return skipped
        index = match.end() - 1
        if not _PLURAL_POSSESSIVE.match(text, index - 1):
            return index
        skipped = index if skipped is None else skipped
        pos = match.end()


def _closing_double_mark(text: str, start: int) -> int | None:
    depth = 0
    for index in range(start, len(text)):
        mark = text[index]
        if mark not in "\"\u201c\u201d":
            continue
        before = text[index - 1] if index else " "
        after = text[index + 1] if index + 1 < len(text) else " "
        opens = mark == "\u201c" or (mark == '"' and (before.isspace() or before in ":,-(\u201c\u2018") and not after.isspace())
        closes = mark == "\u201d" or (mark == '"' and not before.isspace() and (after.isspace() or after in ".,;:!?)\u201d\u2019\"'"))
        if closes and not (opens and mark == '"'):
            if depth == 0:
                return index
            depth -= 1
        elif opens:
            depth += 1
    return None


def _quote_pairs(text: str):
    """(open_index, close_index) of every paired quotation mark, left to
    right."""
    pos = 0
    while True:
        open_m = _QUOTE_OPEN.search(text, pos)
        if not open_m:
            return
        open_i = open_m.end() - 1
        if text[open_i].isspace():
            open_i -= 1
        close_i = _closing_mark(text, text[open_i], open_m.end())
        if close_i is None:
            pos = open_m.end()
            continue
        yield open_i, close_i
        pos = close_i + 1


def quoted_span_positions(text: str) -> list[tuple[int, int, str]]:
    """Every paired quotation in `text`, left to right: (start, end,
    inner) - `start` is the offset of the opening quotation mark, `end` is
    just past the closing quotation mark, `inner` is the quoted words
    between them. engine.m4.transparency_plan places a quote's marker at
    `end`: the marker follows the quoted words."""
    return [(open_i, close_i + 1, text[open_i + 1 : close_i]) for open_i, close_i in _quote_pairs(text)]


def _quoted_spans(text: str) -> list[str]:
    return [inner for _start, _end, inner in quoted_span_positions(text)]


def _normalize(text: str) -> str:
    # Archaic letterforms first (the same mapping engine.m1.quote_verbatim's
    # own verbatim check applies): otherwise the [^a-z0-9\s] strip below silently
    # deletes ſ/þ/ð rather than folding them to their modern spelling,
    # which is a real content loss, not a normalization ("þe" becoming
    # " e" instead of "the"). Applied to both the quoted span and the
    # shelf's own record text below, since both call sites route through
    # this one function - inherently symmetric.
    text, _classes = normalize_archaic_letterforms(text)
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", " ", text.lower())).strip()


def _groundable_text(rec: dict) -> str:
    """The text a generated turn can actually be checked against for
    grounding. A quote record's own `modern_rendering` only - never
    `text` (an archaic or non-English original) - since gate_quote_
    recording (engine/m1/gates.py) and the speakable-form selection in
    evidence.py/builders.py already make modern_rendering the only form
    ever voiced; a generated span matching `text` but not the record's
    own spoken form was never legitimately produced from it. Every other
    record type keeps the wider all_text() - not scoped here, since
    readability, commentary scanning, and the retrieval word-pool all
    still need to see a quote's own `text` for their own, different
    reasons."""
    if rec.get("record_type") == "quote":
        return rec.get("modern_rendering") or ""
    return all_text(rec)


def _span_in_records(span: str, records: list[dict], *, window_words: int = 6) -> bool:
    """Verbatim window-match: a quoted span is grounded when a window of
    it appears verbatim in a tagged record's own text."""
    words = _normalize(span).split()
    if not words:
        return False
    haystacks = [_normalize(_groundable_text(r)) for r in records]
    windows = (
        [" ".join(words)]
        if len(words) <= window_words
        else [" ".join(words[i : i + window_words]) for i in range(len(words) - window_words + 1)]
    )
    return any(w in h for h in haystacks for w in windows)


# Quotation marks claim verbatim words. A span is checked when it is
# double-quoted, or single-quoted and at least this many words long; shorter
# single-quoted spans are scare quotes and terms. A checked span of at least
# this many words is a quotation, and only code places one.
SINGLE_QUOTE_MIN_WORDS = 4

# Records that are not evidence of what the world said: the worked
# demonstration exchanges and the voice-craft notes.
_NOT_QUOTABLE_TYPES = frozenset({"demonstration", "voice_craft"})

_ELLIPSIS = re.compile(r"\.{3}|\u2026")
_WORD_TOKEN = re.compile(r"[a-z0-9]+")

_TITLE_WORDS = frozenset({
    "abba", "abbot", "amma", "bishop", "blessed", "brother", "father", "pope", "saint", "st",
    "the", "and", "of", "in", "at", "on", "for", "to", "as", "from", "with", "our", "his", "her",
    "god", "lord", "christ", "jesus", "spirit", "holy", "first", "second", "third", "forty",
    "book", "rule", "king", "teacher", "chronicle", "index", "council", "persian", "alexandrian", "festal",
})

ATTRIBUTION_WINDOW = 4

_ATTRIBUTION_VERBS = frozenset({
    "said", "says", "say", "wrote", "writes", "write", "declared", "declares", "declare",
    "preached", "preaches", "preach", "told", "tells", "tell", "taught", "teaches", "teach",
    "asked", "answered", "replied", "insisted", "warned", "added", "urged",
})
# Verbs that take someone spoken to as their object: a name after one is the
# addressee, never the speaker.
_ADDRESSEE_VERBS = frozenset({"told", "tells", "tell", "asked", "answered", "replied", "urged", "warned"})
_ATTRIBUTION_PHRASES = frozenset({
    ("put", "it"), ("puts", "it"), ("called", "it"), ("calls", "it"), ("according", "to"),
})

REASON_QUOTATION_NOT_IN_RECORDS = "quotation not in records"
REASON_WORDS_WITHOUT_QUOTE_RECORD = "words attributed without a quote record"


def _name_head(name: str) -> str:
    """The name itself, before any epithet or apparatus: 'Macrina, called the
    Teacher' is Macrina."""
    return re.split(r"[,(;]", name, maxsplit=1)[0].strip()


def _alias_tokens(name: str) -> set[tuple[str, ...]]:
    """The ways a sentence can name a figure called `name`: the whole name,
    and each capitalised word of it that is not a title."""
    aliases: set[tuple[str, ...]] = set()
    name = _name_head(name)
    whole = tuple(_WORD_TOKEN.findall(name.lower()))
    if whole:
        aliases.add(whole)
    for word in name.split():
        token = _WORD_TOKEN.findall(word.lower())
        if len(token) == 1 and len(token[0]) > 2 and word[:1].isupper() and token[0] not in _TITLE_WORDS:
            aliases.add((token[0],))
    return aliases


def _occurrences(tokens: list[str], needle: tuple[str, ...]) -> list[tuple[int, int]]:
    size = len(needle)
    return [(i, i + size) for i in range(len(tokens) - size + 1) if tuple(tokens[i : i + size]) == needle]


class QuotationIndex:
    """What the quotation checks read, built once per turn: the normalised
    text of every quotable record, plus `quotable_texts` (the words the
    participant side of the conversation said, which a reply may repeat in
    quotation marks), and the world's figures with the names that can stand
    for them."""

    def __init__(self, repository_records: dict[str, dict], quotable_texts: list[str] | None = None):
        self._records = repository_records
        self._quotable_texts = quotable_texts or []
        self._haystacks: list[str] | None = None
        self._figures: dict[str, set[tuple[str, ...]]] | None = None

    def _pool(self) -> list[str]:
        if self._haystacks is None:
            self._haystacks = [
                f" {_normalize(all_text(rec))} "
                for rec in self._records.values()
                if rec.get("record_type") not in _NOT_QUOTABLE_TYPES
            ]
            self._haystacks += [f" {_normalize(strip_tags(text))} " for text in self._quotable_texts]
        return self._haystacks

    def holds(self, span: str) -> bool:
        """The span, normalised the way _span_in_records normalises, runs
        word for word inside one record. A span with ellipses is checked
        piece by piece. The whole piece must match: window matching passes a
        long span as soon as one window of it matches."""
        pieces = [" ".join(_normalize(piece).split()) for piece in _ELLIPSIS.split(span)]
        pieces = [piece for piece in pieces if piece]
        if not pieces:
            return False
        return all(any(f" {piece} " in haystack for haystack in self._pool()) for piece in pieces)

    def echoes(self, span: str) -> bool:
        """The span repeats, word for word, words the participant side of the
        conversation said."""
        pieces = [" ".join(_normalize(piece).split()) for piece in _ELLIPSIS.split(span)]
        pieces = [piece for piece in pieces if piece]
        haystacks = [f" {_normalize(strip_tags(text))} " for text in self._quotable_texts]
        return bool(pieces) and all(any(f" {piece} " in haystack for haystack in haystacks) for piece in pieces)

    def names_speaker(self, sentence: str, quote_record: dict) -> bool:
        """`sentence` names the figure a quote record's speaker field stands
        for."""
        tokens = _WORD_TOKEN.findall(sentence.lower())
        figures = self._figure_aliases()
        for fid in self.speaker_ids(quote_record):
            aliases = figures.get(fid) or _alias_tokens(quote_record.get("speaker_or_author") or "")
            if any(_occurrences(tokens, alias) for alias in aliases):
                return True
        return False

    def is_known_name(self, segment: str) -> bool:
        """`segment` is a name of one of the world's figures or quote
        speakers, give or take a title."""
        tokens = tuple(t for t in _WORD_TOKEN.findall(_name_head(segment).lower()) if t not in _TITLE_WORDS)
        if not tokens:
            return False
        return any(
            _occurrences(list(tokens), alias) for aliases in self._figure_aliases().values() for alias in aliases
        )

    def _figure_aliases(self) -> dict[str, set[tuple[str, ...]]]:
        if self._figures is None:
            figures: dict[str, set[tuple[str, ...]]] = {}
            for rec in self._records.values():
                if rec.get("record_type") != "figure":
                    continue
                aliases: set[tuple[str, ...]] = set()
                for entry in rec.get("names") or []:
                    if isinstance(entry, dict) and entry.get("tag") == "in-world":
                        aliases |= _alias_tokens(entry.get("name") or "")
                figures[rec["id"]] = aliases
            for rec in self._records.values():
                speaker = rec.get("speaker_or_author") if rec.get("record_type") == "quote" else None
                if speaker and speaker not in figures and not self._speaker_figures(speaker, figures):
                    figures[_speaker_key(speaker)] = _alias_tokens(speaker)
            self._figures = figures
        return self._figures

    @staticmethod
    def _speaker_figures(speaker: str, figures: dict[str, set[tuple[str, ...]]]) -> set[str]:
        tokens = _WORD_TOKEN.findall(_name_head(speaker).lower())
        return {fid for fid, aliases in figures.items() if any(_occurrences(tokens, alias) for alias in aliases)}

    def speaker_ids(self, quote_record: dict) -> set[str]:
        """The figure ids a quote record's speaker field stands for."""
        speaker = quote_record.get("speaker_or_author") or ""
        figures = self._figure_aliases()
        if speaker in figures:
            return {speaker}
        return self._speaker_figures(speaker, figures) or {_speaker_key(speaker)}

    def attributed_figures(self, sentence: str) -> list[set[str]]:
        """One entry per attribution verb that has a figure for its subject:
        the figure ids that name can stand for. The subject is the nearest
        name before the verb; a name after it counts only when none stands
        before ("according to Ignatius", "said Basil"), never the person
        written or spoken to."""
        tokens = _WORD_TOKEN.findall(sentence.lower())
        verbs = [(i, i + 1) for i, t in enumerate(tokens) if t in _ATTRIBUTION_VERBS]
        verbs += [(i, i + 2) for i in range(len(tokens) - 1) if (tokens[i], tokens[i + 1]) in _ATTRIBUTION_PHRASES]
        if not verbs:
            return []
        names: list[tuple[int, int, set[str]]] = []
        by_alias: dict[tuple[str, ...], set[str]] = {}
        for fid, aliases in self._figure_aliases().items():
            for alias in aliases:
                by_alias.setdefault(alias, set()).add(fid)
        for alias, fids in by_alias.items():
            names += [(start, end, fids) for start, end in _occurrences(tokens, alias)]
        found = []
        for v_start, v_end in sorted(verbs):
            before = [n for n in names if 0 <= v_start - n[1] <= ATTRIBUTION_WINDOW]
            addressed = tokens[v_start] in _ADDRESSEE_VERBS
            after = [] if addressed else [n for n in names if n[0] == v_end]
            pool = [max(before, key=lambda n: n[1])] if before else after
            if pool:
                nearest = max(n[1] - n[0] for n in pool)
                found.append(set().union(*(n[2] for n in pool if n[1] - n[0] == nearest)))
        return found


def _speaker_key(speaker: str) -> str:
    return "speaker:" + " ".join(_WORD_TOKEN.findall(_name_head(speaker).lower()))


def _strip_pairs(text: str) -> str:
    pieces, last = [], 0
    for open_i, close_i in _quote_pairs(text):
        pieces += [text[last:open_i], _strip_pairs(text[open_i + 1 : close_i])]
        last = close_i + 1
    return "".join(pieces) + text[last:]


def _checked_pairs(text: str) -> list[tuple[int, int, str]]:
    """The quotations of `text` that claim verbatim words: (open_index,
    close_index, inner)."""
    checked = []
    for open_i, close_i in _quote_pairs(text):
        inner = text[open_i + 1 : close_i]
        if text[open_i] in "\"\u201c" or len(_normalize(inner).split()) >= SINGLE_QUOTE_MIN_WORDS:
            checked.append((open_i, close_i, inner))
    return checked


def unquote_spans(text: str, spans: list[tuple[int, int, str]]) -> str:
    """`text` with the marks of the given spans (and any quotation nested
    inside them) taken off; every other character is kept."""
    pieces, last = [], 0
    for open_i, close_i, inner in sorted(spans):
        pieces += [text[last:open_i], _strip_pairs(inner)]
        last = close_i + 1
    return "".join(pieces) + text[last:]


REASON_TYPED_QUOTATION = "quotation typed by the voice"
REASON_ATTRIBUTION = "words attributed without a placed quote"
REASON_ATTRIBUTION_LEAD = "introduces words that are not a placed quote"
REASON_UNPLACED_WORDS = "words after an attribution, not a placed quote"
REASON_LEAD_IN = "lead-in to a quotation typed by the voice"
REASON_QUOTE_RECORD_UNPLACED = "quote record's speaker named without its placed quote"
REASON_PLACED_MISMATCH = "placed quote does not match its record"
WHY_PLACED = "quote placed by code, verbatim to its record"

# A sentence withheld for one of these reasons carries words attributed to
# someone that code did not place. It is dropped from the reply, not shown
# with its tag removed.
QUOTATION_DROP_REASONS = frozenset({
    REASON_TYPED_QUOTATION, REASON_ATTRIBUTION, REASON_ATTRIBUTION_LEAD, REASON_UNPLACED_WORDS, REASON_LEAD_IN,
    REASON_QUOTE_RECORD_UNPLACED, REASON_PLACED_MISMATCH, REASON_WORDS_WITHOUT_QUOTE_RECORD,
})

# Attribution formulas. A quotation needs no quotation marks to be one:
# "Athanasius wrote: the Son was never made" puts words in a named mouth as
# surely as a quoted span does.
_VERB = (
    r"(?:said|says|say|wrote|writes|write|declared|declares|declare|preached|preaches|preach|taught|teaches|teach|"
    r"put\s+it|puts\s+it|insisted|insists|replied|replies|answered|answers|warned|warns|urged|urges|added|adds|"
    r"explained|explains|confessed|confesses|argued|argues|affirmed|affirms|maintained|maintains|stated|states|"
    r"observed|observes|noted|notes|cried|exclaimed|prayed|prays|asked|asks|told\s+\w+|tells\s+\w+)"
)
_ADVERB = r"(?:\s+(?:(?:this|that|the\s+same)\s+way|it|so|this|that|again|later|then|there|here|well|in\s+\w+|\w+ly)){0,3}"
_FORMULA = re.compile(
    rf"(?P<as>\bas\s+(?P<who>[^.!?:;,]{{1,70}}?)\s+{_VERB}\b{_ADVERB}\s*,)"
    rf"|(?P<verb>\b{_VERB}\b{_ADVERB}\s*[:,])"
    r"|(?P<words>\bin\s+(?:the\s+words\s+of\s+[^.!?:;]{1,40}|[\w'’]+\s+(?:own\s+)?words|"
    r"(?:his|her|their)\s+(?:own\s+)?words)\s*[:,])"
    r"|(?P<acc>\baccording\s+to\s+[^.!?:;]{1,60}[:,])",
    re.IGNORECASE,
)
_FORWARD = re.compile(
    rf"\b{_VERB}\b(?:\s+[\w'’]+){{0,3}}?\s+(?:(?:this|the\s+following)\s+way|thus|as\s+follows|"
    r"in\s+these\s+words|like\s+this|these\s+words)\s*[.:]?\s*$",
    re.IGNORECASE,
)
_NAME = r"[A-Z][\w'’.-]*(?:\s+(?:of|the|de|von|van|al|bar|ibn|[A-Z][\w'’.-]*)){0,5}"
_NAME_COLON = re.compile(rf"^\s*(?P<name>{_NAME})\s*:")
_TRAILING_NAME = re.compile(
    rf"(?:\s*[—–]\s*|\s--\s*|\s-\s)(?P<name>{_NAME})(?:\s*,[^.!?—–]{{0,80}})?\s*[.!?]?\s*$"
)
_NAME_TITLES = frozenset({
    "saint", "st", "abba", "amma", "abbot", "bishop", "pope", "father", "mother", "brother", "sister", "mar", "rabbi",
})
_SUBORDINATORS = frozenset({
    "when", "after", "before", "while", "since", "because", "if", "although", "though", "once", "until", "whenever",
})
_NON_NAMES = frozenset({
    "we", "our", "ours", "i", "my", "me", "you", "your", "the", "a", "an", "this", "that", "these", "those", "it",
    "its", "there", "here", "as", "in", "on", "at", "of", "for", "to", "so", "and", "but", "or", "then", "when",
    "where", "what", "why", "how", "who", "if", "yet", "still", "now", "even", "often", "sometimes", "some",
    "every", "each", "all", "one", "another", "not", "no", "once", "later", "earlier", "after", "before", "plainly",
    "simply", "clearly", "briefly", "again", "also", "never", "always", "perhaps", "indeed", "thus", "hence",
    "however", "while", "because", "since", "with", "from", "by", "about", "like", "just", "only", "both", "either",
    "neither", "says", "said", "say", "wrote", "write", "writes", "put", "puts", "told", "tells", "teaches",
    "taught", "teach", "declared", "declares", "preached", "preaches", "according", "words", "own",
})
_PERSON_PRONOUNS = frozenset({"he", "she", "they", "his", "her", "their"})
_WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’-]*")
_SPEECH_VERB = re.compile(rf"\b{_VERB}\b", re.IGNORECASE)


def _names_someone(text: str) -> bool:
    for word in _WORD.findall(text):
        lowered = word.lower()
        if lowered in _PERSON_PRONOUNS:
            return True
        if word[:1].isupper() and lowered not in _NON_NAMES:
            return True
    return False


def _subject_before(sentence: str, start: int) -> str:
    """The words before a speech verb that can be its subject: back to the
    last clause break, at most eight words. Empty when a subordinating word
    opens that clause ("When Leo wrote, ..." is not an attribution)."""
    clause = re.split(r"[.!?;:,—–]", sentence[:start])[-1]
    words = clause.split()[-8:]
    if any(w.lower().strip("'’") in _SUBORDINATORS for w in words):
        return ""
    return " ".join(words)


def _is_name(segment: str, index: "QuotationIndex") -> bool:
    words = segment.split()
    if not words or words[0].lower() in _NON_NAMES:
        return False
    return words[0].lower().rstrip(".") in _NAME_TITLES or index.is_known_name(segment)


def reads_as_lead(sentence: str) -> bool:
    """A sentence that reads as the introduction to words that follow: it
    ends in a colon, or a named person or source is the subject of a speech
    verb in it."""
    stripped = _TAG.sub("", sentence).rstrip()
    if stripped.endswith(":"):
        return True
    verb = _SPEECH_VERB.search(stripped)
    return bool(verb) and _names_someone(_subject_before(stripped, verb.start()))


def _attribution(outside: str, index: "QuotationIndex") -> dict | None:
    """The first attribution form in a sentence's text outside its
    quotations, as {"opens", "words"}: whether it introduces what follows
    (a colon, "put it this way."), and whether words follow it in the
    sentence. None when the sentence attributes nothing to anyone. Formulas
    spoken by "we" are the world's own voice, not an attribution."""
    text = _TAG.sub("", outside).strip()
    named_colon = _NAME_COLON.match(text)
    if named_colon and _is_name(named_colon.group("name"), index):
        return {"opens": True, "words": bool(_WORD.search(text[named_colon.end():]))}
    for match in _FORMULA.finditer(text):
        if match.group("as"):
            subject = match.group("who")
        elif match.group("verb"):
            subject = _subject_before(text, match.start())
        else:
            subject = match.group(0) + " " + _subject_before(text, match.start())
        if _names_someone(subject):
            rest = text[match.end():]
            return {"opens": match.group(0).rstrip().endswith(":"), "words": bool(_WORD.search(rest))}
    forward = _FORWARD.search(text)
    if forward and _names_someone(_subject_before(text, forward.start())):
        return {"opens": True, "words": False}
    trailing = _TRAILING_NAME.search(text)
    if trailing and _is_name(trailing.group("name"), index) and _WORD.search(text[: trailing.start()]):
        return {"opens": False, "words": True}
    return None


def _outside_quotations(text: str, spans: list[tuple[int, int, str]]) -> str:
    outside = text
    for open_i, close_i, _inner in sorted(spans, reverse=True):
        outside = outside[:open_i] + " " + outside[close_i + 1 :]
    return outside


def placed_key(text: str) -> str:
    """A placed sentence's text, or a rendering, with its whitespace
    collapsed: the sentence splitter rejoins a rendering's line breaks with
    spaces."""
    return " ".join(text.split())


def _placed_verdict(text: str, tags: list[str], records: dict[str, dict], index: QuotationIndex, record_id: str) -> dict:
    """A sentence code composed around a quote record's rendering: the
    rendering stands in it word for word, tagged with that record, and the
    lead-in attributes it to that record's own speaker and types no other
    quotation."""
    record = records.get(record_id) or {}
    rendering = placed_key(record.get("modern_rendering") or "")
    spans = [span for span in _checked_pairs(text) if placed_key(span[2]) == rendering]
    holds = bool(rendering) and record.get("record_type") == "quote" and record_id in tags and bool(spans)
    if holds:
        others = [span for span in _checked_pairs(text) if placed_key(span[2]) != rendering]
        lead = _outside_quotations(text, spans + others)
        speakers = index.speaker_ids(record)
        holds = not [s for s in others if len(_normalize(s[2]).split()) >= SINGLE_QUOTE_MIN_WORDS] and all(
            fids & speakers for fids in index.attributed_figures(lead)
        )
    if not holds:
        return {"sentence": text, "tags": tags, "verdict": "withhold", "why": REASON_PLACED_MISMATCH}
    return {"sentence": text, "tags": tags, "verdict": "ok", "why": WHY_PLACED, "placed_quote": record_id}


def _quotation_verdict(
    text: str, tags: list[str], records: dict[str, dict], index: QuotationIndex, placed_id: str | None = None,
) -> dict | None:
    """The quotation checks on one sentence: a verdict entry, {"lead_only":
    True} for a sentence that only introduces what follows it (decided in
    context, _apply_quotation_context), or None when the sentence carries
    no quotation and attributes no words.

    Only code places a quotation. A placed sentence is re-verified against
    its record. Otherwise a quotation of SINGLE_QUOTE_MIN_WORDS or more
    words is withheld, unless it repeats the participant side's own words;
    a shorter quoted span found in no record loses its marks; words
    attributed to someone without quotation marks are withheld; and so is a
    sentence tagged with a quote record that names that record's speaker,
    since it gives the quote in other words."""
    if placed_id is not None:
        return _placed_verdict(text, tags, records, index, placed_id)
    checked = _checked_pairs(text)
    outside = _outside_quotations(text, checked)
    foreign_unpaired = any(mark in outside for mark in FOREIGN_QUOTE_MARKS)
    typed = [
        span for span in checked
        if len(_normalize(span[2]).split()) >= SINGLE_QUOTE_MIN_WORDS and not index.echoes(span[2])
    ]
    if typed or foreign_unpaired:
        entry = {"sentence": text, "tags": tags, "verdict": "withhold", "why": REASON_TYPED_QUOTATION}
        if not _TAG.sub("", outside).strip(" \t.,;:!?-—–" + FOREIGN_QUOTE_MARKS):
            entry["stands_alone"] = True
        if any(mark in outside for mark in "«‹„"):
            entry["opens_quote"] = True
        return entry
    missing = [span for span in checked if not index.holds(span[2])]
    if missing:
        return {
            "sentence": unquote_spans(text, missing), "source_sentence": text, "tags": tags, "verdict": "withhold",
            "why": REASON_QUOTATION_NOT_IN_RECORDS, "quotations_not_in_records": [inner for _o, _c, inner in missing],
        }
    quote_records = [records[t] for t in tags if (records.get(t) or {}).get("record_type") == "quote"]
    if checked:
        attributed = index.attributed_figures(outside)
        if attributed:
            speakers: set[str] = set()
            for rec in quote_records:
                speakers |= index.speaker_ids(rec)
            if any(not (fids & speakers) for fids in attributed):
                return {"sentence": text, "tags": tags, "verdict": "withhold", "why": REASON_WORDS_WITHOUT_QUOTE_RECORD}
    attribution = _attribution(outside, index)
    if attribution is not None:
        if attribution["opens"] and not attribution["words"]:
            return {"lead_only": True}
        entry = {"sentence": text, "tags": tags, "verdict": "withhold", "why": REASON_ATTRIBUTION}
        if attribution["opens"]:
            entry["opens_quote"] = True
        return entry
    if any(index.names_speaker(outside, rec) for rec in quote_records):
        return {"sentence": text, "tags": tags, "verdict": "withhold", "why": REASON_QUOTE_RECORD_UNPLACED}
    return None


def _apply_quotation_context(entries: list[dict], sizes: list[int]) -> None:
    """The quotation checks that need a sentence's neighbours, applied in
    place over one turn's verdicts (`sizes`: sentences per paragraph). A
    sentence that opens a quotation (an attribution ending in a colon, "put
    it this way.", an unclosed guillemet) takes the rest of its paragraph
    with it. A sentence that only introduces what follows ("Athanasius
    says plainly:") is kept only when a placed quote follows it; otherwise
    it goes, with the rest of its paragraph, or the next paragraph when it
    ends its own. A typed quotation standing
    alone takes the sentence that introduced it."""
    paragraph_of = [p for p, n in enumerate(sizes) for _ in range(n)]
    starts = [sum(sizes[:p]) for p in range(len(sizes))]

    def withhold(i: int, why: str) -> None:
        if not entries[i].get("placed_quote"):
            entries[i].update(verdict="withhold", why=why)

    for i, entry in enumerate(entries):
        if entry.get("stands_alone") and i > 0:
            j = i - 1
            previous = entries[j].get("source_sentence") or entries[j]["sentence"]
            same = paragraph_of[j] == paragraph_of[i]
            ends_paragraph = sizes[paragraph_of[j]] == 1 or _TAG.sub("", previous).rstrip().endswith(":")
            if (same or ends_paragraph) and reads_as_lead(previous):
                withhold(j, REASON_LEAD_IN)
        if not entry.get("opens_quote"):
            continue
        p = paragraph_of[i]
        end = starts[p] + sizes[p]
        lead_only = entry.get("why") not in QUOTATION_DROP_REASONS
        if i + 1 < end:
            followers = range(i + 1, end)
        elif lead_only and p + 1 < len(sizes):
            followers = range(starts[p + 1], starts[p + 1] + sizes[p + 1])
        else:
            followers = range(0)
        if lead_only:
            if followers and entries[followers[0]].get("placed_quote"):
                continue
            withhold(i, REASON_ATTRIBUTION_LEAD)
        for k in followers:
            if entries[k].get("placed_quote"):
                break
            withhold(k, REASON_UNPLACED_WORDS)


def shown_text(raw_text: str, sentences: list[dict]) -> str:
    """The reply a participant reads: the raw text with its tags stripped
    and, in each sentence the net took the marks off, that sentence's own
    marks-off text."""
    shown = strip_tags(raw_text)
    pieces, cursor = [], 0
    for entry in sentences:
        source = entry.get("source_sentence") or entry.get("sentence") or ""
        position, length = shown.find(source, cursor) if source else -1, len(source)
        if position < 0 and source:
            found = re.compile(r"\s+".join(re.escape(w) for w in source.split())).search(shown, cursor)
            position, length = (found.start(), found.end() - found.start()) if found else (-1, 0)
        if position < 0:
            continue
        pieces += [shown[cursor:position], entry.get("sentence") or ""]
        cursor = position + length
    return "".join(pieces) + shown[cursor:]


def build_figure_lexicon(repository_records: dict[str, dict]) -> set[str]:
    """Lowercased attested figure names from the package's own figure
    records - a positive lexicon, so a sentence-initial 'Clement wrote...'
    counts as a checkable attribution even though the capitalization
    heuristic is blind at position 0."""
    names: set[str] = set()
    for rec in repository_records.values():
        if rec.get("record_type") != "figure":
            continue
        for entry in rec.get("names") or []:
            # names entries are {name, tag}; only the in-world name feeds
            # the lexicon - scholarly forms ("Clement of Alexandria (Titus
            # Flavius Clemens...)") would pull common place/epithet words
            # in as false figure-signals.
            if isinstance(entry, dict) and entry.get("tag") == "in-world":
                for word in (entry.get("name") or "").split():
                    if len(word) > 2:
                        names.add(word.lower())
    return names


_NEXT_SENTENCE = re.compile(r"\s+(?=[A-Z\"'“‘«„])")


def _split_after_closed_quotations(sentence: str) -> list[str]:
    """A quotation that ends its own sentence ('He said "Go home." Then he
    left.') ends the sentence there. The splitter keeps the two together,
    since it breaks at the full stop inside the marks; a quotation nested
    inside another is never split."""
    pieces, last = [], 0
    for _open_i, close_i in _quote_pairs(sentence):
        if sentence[close_i - 1] in ".!?" and _NEXT_SENTENCE.match(sentence, close_i + 1):
            pieces.append(sentence[last : close_i + 1])
            last = close_i + 1
    pieces.append(sentence[last:])
    return [piece.strip() for piece in pieces if piece.strip()]


def parse_tagged(text: str) -> list[dict]:
    """Split tagged output into sentences, each with its own claimed ids."""
    out = []
    for sentence in quote_aware_sentences(text):
        for raw in _split_after_closed_quotations(sentence):
            ids = _TAG.findall(raw)
            out.append({"raw": raw, "text": strip_tags(raw).strip(), "tags": ids})
    return out


def _thin_topic_hits(sentence_lower: str, thin_topics: list[dict] | None) -> list[str]:
    hits = []
    for topic in thin_topics or []:
        kws = [kw for kw in (topic.get("keywords") or []) if kw.lower() in sentence_lower]
        if kws:
            hits.append(f"{kws} ({topic.get('note')})")
    return hits


# The scaffold exemption
# below used to exempt an entire sentence the moment ANY SCAFFOLD_MARKERS
# phrase appeared anywhere in it - so "...our founder wrote against the
# peasants' rising, and that writing is part of our own history EVEN WHEN
# WE CANNOT speak its own words" rode a chronological conflation past the
# net on the strength of four words at its own tail. The fix narrows the
# exemption to the clause that actually carries the honesty-scaffolding
# phrase, not an arbitrary-length sentence attached to it: split on the
# same clause-level punctuation English prose already uses to separate
# independent claims, drop only the clause(s) containing a marker, and
# check what's LEFT the same way any other sentence would be checked. A
# genuinely pure scaffold sentence ("We must be careful here, and honest
# about the shape of what we actually hold.") still exempts cleanly - its
# residual carries no proper noun, number, or enumeration either. A tag
# counts too, on the same basis check_turn's own tag-overlap branch
# already uses ("THE TAG IS THE CLAIM"): a scaffold phrase grammatically
# FUSED with its claim ("We must be honest THAT x [[tag]]") defeats the
# punctuation split, but the tag still forces the check regardless of
# which clause it sits in. This does not change entry["sentence"] or the
# withhold/ok granularity anywhere else in this module: a sentence still
# streams or doesn't as a whole, exactly as the design already works:
# this only changes whether the decision to skip checking it gets made
# honestly.
_CLAUSE_SPLIT = re.compile(r"[,;:]|--|—")


def _scaffold_residual(text: str) -> str:
    clauses = _CLAUSE_SPLIT.split(text)
    kept = [
        c for c in clauses
        if not any(m in c.lower() for m in SCAFFOLD_MARKERS) and SELF_NAMING_MARKER not in c.lower()
    ]
    return " ".join(kept)


def verdict_for_sentence(
    text: str,
    tags: list[str],
    *,
    repository_records: dict[str, dict],
    figure_names: set[str],
    thin_topics: list[dict] | None,
    grounding_floor: float,
    quotation_index: QuotationIndex | None = None,
    placed_quote_id: str | None = None,
) -> dict:
    """One sentence's verdict, so a single constructed (sentence, tags)
    pair can be run directly, without round-tripping through tagged-text
    reconstruction and re-parsing. check_turn_with_paragraph_coverage calls
    it once per parse_tagged() sentence; see check_turn for the verdict
    vocabulary.

    The quotation checks (_quotation_verdict) run first. placed_quote_id
    names the quote record code placed in this sentence, if any. A short
    quoted span found in no record comes back with its marks off, in
    "sentence", and the sentence as written in "source_sentence". A
    sentence that only introduces what follows it carries "opens_quote",
    for the turn-level pass to decide."""
    quotation = _quotation_verdict(
        text, tags, repository_records, quotation_index or QuotationIndex(repository_records), placed_quote_id,
    )
    if quotation is not None and not quotation.get("lead_only"):
        return quotation
    entry = _claim_verdict(
        text, tags, repository_records=repository_records, figure_names=figure_names,
        thin_topics=thin_topics, grounding_floor=grounding_floor,
    )
    if quotation is not None:
        entry["opens_quote"] = True
    return entry


def _claim_verdict(
    text: str, tags: list[str], *, repository_records: dict[str, dict], figure_names: set[str],
    thin_topics: list[dict] | None, grounding_floor: float,
) -> dict:
    lower = text.lower()
    entry = {"sentence": text, "tags": tags, "verdict": "ok", "why": None}

    if any(m in lower for m in SCAFFOLD_MARKERS) or SELF_NAMING_MARKER in lower:
        residual = _scaffold_residual(text)
        # A tag is itself a claim ("this sentence came from that
        # record" - the tag-overlap branch below exists for exactly
        # this), so a tagged sentence needs the same check whether or
        # not a scaffold phrase also sits in it somewhere.
        residual_markers = bool(tags) or bool(claim_markers(residual)) or bool(figure_names & content_words(residual))
        if not residual_markers:
            entry["why"] = "exempt: honesty scaffolding / sanctioned self-naming"
            return entry
        # Something besides the scaffold phrase itself still makes a
        # checkable claim - fall through to the same pipeline every
        # other sentence goes through, over the FULL sentence text
        # (the scaffold clause's own words carry no proper noun,
        # number, or enumeration, so they cannot themselves trip a
        # withhold; whatever fires below is the real content).

    unknown = [t for t in tags if t not in repository_records]
    if unknown:
        entry["verdict"], entry["why"] = "withhold", f"unresolvable record id(s): {unknown}"
        return entry
    tagged_records = [repository_records[t] for t in tags]

    markers = claim_markers(text)
    if not markers and figure_names & content_words(text):
        markers = [f"figure-name:{sorted(figure_names & content_words(text))}"]
    cited_words: set[str] = set()
    for rec in tagged_records:
        cited_words |= content_words(_groundable_text(rec))

    if not markers:
        if not tags:
            entry["why"] = "no checkable claim - interpretive/connective framing"
            return entry
        # THE TAG IS THE CLAIM. claim_markers only sees a proper noun, a
        # number, or a repeated phrase, and over 36 live turns that left
        # 242 of 388 sentences unexamined - the citation contract reads
        # as a guarantee over the turn and was a guarantee over the third
        # of it that happened to name someone or count something.
        #
        # 192 of those unexamined sentences carried a tag. A tag is the
        # voice asserting THIS SENTENCE CAME FROM THAT RECORD, which is
        # checkable by definition, and the net was throwing that
        # assertion away. Honouring it takes the examined share from 32%
        # to 78% without inventing a marker.
        #
        # Gated on overlap, NOT on grounding_floor. That floor was
        # calibrated on name-and-number sentences, which sit lexically
        # close to their source; applied to this population it strips
        # roughly 29 legitimate citations to catch 10 over-tags -
        # "Origen's interpretations mattered because he could show his
        # work" scores 29% and is a real claim, penalised for being long.
        # Zero shared words is the one line here that is not a chosen
        # number: a citation to a record with which the sentence shares
        # not one content word asserts nothing. Seven of the 192 were
        # that, every one framing - "That is what mattered most." tagged
        # to hal.gravity.hebraica-veritas.
        if content_words(text) & cited_words:
            entry["why"] = "tagged claim, shares ground with its own records"
            return entry
        entry["verdict"] = "withhold"
        entry["why"] = "tagged claim sharing no content word with its own tagged records"
        return entry

    if not tags:
        entry["verdict"] = "withhold"
        entry["why"] = f"specific claim ({', '.join(markers)}) with no citation tag"
        return entry

    # the shared implementation, not a second copy of the same formula
    ratio = grounding_ratio(text, cited_words)
    entry["ratio"] = round(ratio, 2)

    if ratio >= grounding_floor:
        entry["why"] = f"grounded {ratio:.0%} in own tagged records"
    else:
        thin = _thin_topic_hits(lower, thin_topics)
        entry["verdict"] = "withhold"
        entry["why"] = (
            f"specific claim ({', '.join(markers)}) only {ratio:.0%} grounded in its own tags"
            + (f"; inside a named thin topic: {'; '.join(thin)}" if thin else "")
        )
    return entry


def check_turn(
    tagged_text: str,
    repository_records: dict[str, dict],
    *,
    thin_topics: list[dict] | None = None,
    grounding_floor: float = WITHHOLD_FLOOR,
    quotable_texts: list[str] | None = None,
    placed: dict[str, str] | None = None,
) -> dict:
    """Per-sentence verdicts over one tagged turn: check_turn_with_paragraph_
    coverage without its paragraph layer.

    Verdicts, mapped to the design's fallback ladder:
      ok       - no checkable claim, or the claim is grounded in its own tags
                 (ratio over the floor, or a quoted span verbatim-matched)
      withhold - the sentence never reaches the stream: unresolvable tag,
                 an untagged specific claim, a quoted span found in no
                 tagged record, a tagged claim whose own sources don't
                 carry it, or a quotation code did not place

    placed maps the text of each sentence code composed around a quote
    record (tags stripped, placed_key) to that record's id.

    This check decides only what may stream at all.

    tagged_text is backed off past any generation cut off mid-tag
    (_drop_truncated_tail) before it is split into sentences at all, the
    same normalization strip_tags applies to the text turn.apply_net
    actually displays - so this function's own sentence list can never
    describe a fragment the participant was never shown. result["truncated"]
    is that normalization's own report, not a silent edit.
    """
    result = check_turn_with_paragraph_coverage(
        tagged_text, repository_records, thin_topics=thin_topics, grounding_floor=grounding_floor,
        quotable_texts=quotable_texts, placed=placed,
    )
    return {key: result[key] for key in ("sentences", "substantive_survives", "truncated")}


# Blank-line blocks - the exact regex
# engine.m4.live_uncited_claims_battery's own _PARAGRAPH_SPLIT already
# proved live across two battery runs (#419, #420). A paragraph is a
# sequence of the same sentences parse_tagged already produces, grouped by
# which blank-line block they fell in - nothing about how a sentence
# itself is found or tagged changes.
_PARAGRAPH_SPLIT = re.compile(r"\n\s*\n")


def split_into_paragraphs(tagged_text: str) -> list[str]:
    paragraphs = [p for p in _PARAGRAPH_SPLIT.split(tagged_text) if p.strip()]
    return paragraphs or [tagged_text]


def drop_flagged_sentences(tagged_text: str, flagged_sentences: set[str]) -> str:
    """Removes each named sentence's own raw span - tag included - from
    tagged_text, whole, and rejoins what is left. The one enforcement
    action a caller may take on a flagged sentence that is not "regenerate
    the whole turn again": reuses this module's own split_into_paragraphs/
    parse_tagged, the same sentence/paragraph boundaries every verdict in
    "sentences" was already computed against, so a sentence named by its
    own exact `verdict_for_sentence`-produced text (parse_tagged's own
    "text" field, tags already stripped) is matched and removed
    unambiguously - no re-splitting, no re-tokenizing, no risk of
    disagreeing with the net about where one sentence ends and the next
    begins.

    Two structural guarantees, not left to chance:
      - a paragraph that loses every one of its own sentences is dropped
        whole, never left behind as an empty blank-line block;
      - a paragraph that keeps at least one sentence keeps its own
        surviving sentences joined by a single space, so removing a
        sentence from the middle never leaves doubled whitespace or an
        orphaned closing quote/tag.

    What this does NOT guarantee: a sentence that grammatically promised
    the one just removed (a paragraph ending "...three things stand out:"
    whose own next sentence was the one dropped) can still read as an
    unfinished promise - a semantic dangling fragment this string-level
    operation has no way to see, as opposed to the structural one
    (broken punctuation, an empty paragraph) it does prevent."""
    kept_paragraphs = []
    for paragraph in split_into_paragraphs(tagged_text):
        kept_sentences = [sent["raw"] for sent in parse_tagged(paragraph) if sent["text"] not in flagged_sentences]
        if kept_sentences:
            kept_paragraphs.append(" ".join(kept_sentences))
    return "\n\n".join(kept_paragraphs)


def check_turn_with_paragraph_coverage(
    tagged_text: str,
    repository_records: dict[str, dict],
    *,
    thin_topics: list[dict] | None = None,
    grounding_floor: float = WITHHOLD_FLOOR,
    quotable_texts: list[str] | None = None,
    placed: dict[str, str] | None = None,
) -> dict:
    """The net's one pass over a tagged turn: every sentence's verdict
    (check_turn's "sentences"/"substantive_survives"/"truncated"), the
    quotation checks that need a sentence's neighbours
    (_apply_quotation_context), and a report-only "paragraph_coverage"
    layer engine.m4.uncited_claims reads. engine.m4.turn.apply_net calls
    this; check_turn is this without the paragraph layer.

    paragraph_coverage is a list, one entry per blank-line paragraph
    (split_into_paragraphs), each:
      sentence_count        - how many of this result's own "sentences"
                               belong to this paragraph (they sit
                               contiguously, in order - a caller partitions
                               the flat sentence list by walking these
                               counts, the same way this function itself
                               does below)
      cited_record_ids       - EFFECTIVE record ids this paragraph's own
                               coverage check uses: the union of every tag
                               in this paragraph's own sentences, UNLESS
                               this is a one-sentence paragraph carrying no
                               tag of its own, in which case it is the
                               immediately PRECEDING paragraph's own
                               cited_record_ids instead (coverage only;
                               see inherited_from_preceding below)
      wholly_uncited         - true when cited_record_ids is empty - this
                               paragraph carries no citation anywhere, not
                               even by inheritance
      inherited_from_preceding - true only for a one-sentence paragraph
                               that borrowed its own cited_record_ids from
                               the paragraph before it
      inherited_verdicts     - {sentence index WITHIN this paragraph:
                               verdict_for_sentence's own result}, one
                               entry per sentence that carries no tag of
                               its own but whose paragraph's own
                               cited_record_ids is non-empty - the exact
                               same function real per-sentence checking
                               already runs, fed this paragraph's own
                               inherited ids instead of that sentence's
                               own (empty) tags. No new checking logic, no
                               new model call: this is the identical
                               verdict_for_sentence a tagged sentence
                               already gets, called a second time for an
                               untagged one, against a different id set.
    """
    tagged_text, truncated = _drop_truncated_tail(tagged_text)
    figure_names = build_figure_lexicon(repository_records)
    quotation_index = QuotationIndex(repository_records, quotable_texts)
    paragraphs_raw = split_into_paragraphs(tagged_text)

    all_sentences: list[dict] = []
    paragraph_coverage: list[dict] = []
    for paragraph_text in paragraphs_raw:
        parsed = parse_tagged(paragraph_text)
        verdicts = [
            verdict_for_sentence(
                sent["text"], sent["tags"],
                repository_records=repository_records,
                figure_names=figure_names,
                thin_topics=thin_topics,
                grounding_floor=grounding_floor,
                quotation_index=quotation_index,
                placed_quote_id=(placed or {}).get(placed_key(sent["text"])),
            )
            for sent in parsed
        ]
        all_sentences.extend(verdicts)

        own_record_ids = sorted({t for sent in parsed for t in sent["tags"]})
        inherited_from_preceding = False
        if len(parsed) == 1 and not own_record_ids and paragraph_coverage and paragraph_coverage[-1]["cited_record_ids"]:
            cited_record_ids = paragraph_coverage[-1]["cited_record_ids"]
            inherited_from_preceding = True
        else:
            cited_record_ids = own_record_ids

        inherited_verdicts: dict[int, dict] = {}
        if cited_record_ids:
            for i, sent in enumerate(parsed):
                if sent["tags"]:
                    continue  # already carries its own real tag - no inheritance needed
                inherited_verdicts[i] = verdict_for_sentence(
                    sent["text"], cited_record_ids,
                    repository_records=repository_records,
                    figure_names=figure_names,
                    thin_topics=thin_topics,
                    grounding_floor=grounding_floor,
                    quotation_index=quotation_index,
                )

        paragraph_coverage.append({
            "sentence_count": len(parsed),
            "cited_record_ids": cited_record_ids,
            "wholly_uncited": not cited_record_ids,
            "inherited_from_preceding": inherited_from_preceding,
            "inherited_verdicts": inherited_verdicts,
        })

    _apply_quotation_context(all_sentences, [entry["sentence_count"] for entry in paragraph_coverage])
    substantive_survives = any(r["verdict"] == "ok" and r["tags"] for r in all_sentences)
    return {
        "sentences": all_sentences,
        "substantive_survives": substantive_survives,
        "truncated": truncated,
        "paragraph_coverage": paragraph_coverage,
    }


def scope_completion(record_ids: list[str], repository_records: dict[str, dict]) -> list[str]:
    """The anti-conflation rule from the design's retrieval section: never
    serve one pole of a recorded tension without the record that names the
    tension. Returns the extra ids the evidence block must carry: any
    gravity/contested_claim record standing in a tension-with or
    disputed-by relation with a retrieved record, walked in BOTH directions
    (relations are reciprocal by schema, but walking both ways means one
    missing back-edge can't silently drop the guard)."""
    wanted_types = {"gravity", "contested_claim"}
    tension_kinds = {"tension-with", "disputed-by"}
    seed = set(record_ids)
    extra: set[str] = set()

    for rid in record_ids:
        rec = repository_records.get(rid)
        for rel in (rec or {}).get("relations") or []:
            target = repository_records.get(rel.get("target"))
            if rel.get("type") in tension_kinds and target and target.get("record_type") in wanted_types:
                extra.add(target["id"])

    for rec in repository_records.values():
        if rec.get("record_type") not in wanted_types:
            continue
        for rel in rec.get("relations") or []:
            if rel.get("type") in tension_kinds and rel.get("target") in seed:
                extra.add(rec["id"])

    return sorted(extra - seed)
