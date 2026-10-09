"""Quotes are placed by code, never typed by the voice.

A participant hears words attributed to a named person or source only when
they are, word for word, the `modern_rendering` of a quote record in this
turn's evidence. The voice marks where a quote goes and which record with
`[[quote:<record id>]]`, written as the last thing in the sentence that
introduces it. `shape_reply` runs on the voice's raw tagged text, before the
grounding net, and returns raw tagged text the net can check:

- a valid marker becomes the lead-in the voice wrote, then the record's
  rendering in curly quotation marks, then the record's ordinary citation
  tag, and the quote ends its paragraph. The lead-in's closing punctuation
  becomes a colon; a lead-in written as the sentence before the marker joins
  it; words after the marker in the same sentence are cut.
- a marker for a record that is not in this turn's evidence, one the
  conversation has already voiced, a second marker in one reply, or a
  record whose rendering cannot be set apart as one quotation, places
  nothing, and the sentence that introduced it goes with it.
- a quotation the voice typed itself (four or more words between quotation
  marks) goes, unless it repeats words the participant said, and so does
  its lead-in.
- an attribution formula ("X said:", "as X wrote,", "in his own words:",
  "according to X:") with a named person or source as its subject, followed
  by words that are not a placed rendering, is treated as an unverified
  quotation: the sentence goes, and when the formula ends in a colon the
  sentence after it goes too.
- markdown headings, rules, block quotes, standalone bold or italic labels
  and bold or italic citation loci are cut; other emphasis marks come off
  and the words stay. The reply is spoken prose.
- a story the conversation has already told keeps its first tagged
  sentence, as a reference back; later sentences tagged to it go.

Deterministic string operations; no model call. The report lists what was
placed and what was removed and why.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from engine.m4.grounding_net import (
    SINGLE_QUOTE_MIN_WORDS,
    QuotationIndex,
    _checked_pairs,
    _normalize,
    quoted_span_positions,
)
from engine.m4.rhythm import MAX_PLACED_QUOTES_PER_REPLY
from engine.prose import quote_aware_sentences

_MARKER = re.compile(r"\[\[\s*quote\s*(?::[^\]\[]*)?(?:\]\]|\Z)", re.IGNORECASE)
_MARKER_ID = re.compile(r"\[\[\s*quote\s*:\s*([a-z0-9_.-]+)\s*\]\]", re.IGNORECASE)
_TAG = re.compile(r"\[\[([a-z0-9_.-]+)\]\]")
_PARAGRAPH_BREAK = re.compile(r"\n\s*\n")
_SENTENCE_END = re.compile(r"[.!?](?=\s|$)")
_WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’-]*")

REASON_NOT_OFFERED = "quote record not in this turn's evidence"
REASON_ALREADY_VOICED = "quote record already voiced in this conversation"
REASON_SECOND_QUOTE = "second placed quote in one reply"
REASON_NOT_SETTABLE = "rendering cannot be set apart as one quotation"
REASON_TYPED_QUOTATION = "quotation typed by the voice"
REASON_ATTRIBUTION = "words attributed without a placed quote"
REASON_ATTRIBUTION_LEAD = "words introduced by an attribution that ends in a colon"
REASON_LEAD_IN = "lead-in to a removed quotation"
REASON_STORY_RETOLD = "story already told in this conversation"


@dataclass(frozen=True)
class PlacementContext:
    """What one reply may place. `offered` is the quote record ids this
    turn's evidence carried; `voiced` the quote ids the conversation has
    already voiced; `told_stories` the story ids it has already told;
    `echo_texts` the words the participant side has said, which a reply may
    repeat in quotation marks."""
    offered: frozenset[str] = frozenset()
    voiced: frozenset[str] = frozenset()
    told_stories: frozenset[str] = frozenset()
    echo_texts: tuple[str, ...] = ()
    max_quotes: int = MAX_PLACED_QUOTES_PER_REPLY


@dataclass
class _Report:
    placed: list[str] = field(default_factory=list)
    removed: list[dict] = field(default_factory=list)

    def drop(self, sentence: str, why: str) -> None:
        self.removed.append({"sentence": _TAG.sub("", sentence).strip(), "why": why})


_PLACEHOLDER = "\u0000{}\u0000"
_BOLD = re.compile(r"(\*\*|__)(?=\S)(.+?)(?<=\S)\1", re.DOTALL)
_ITALIC_STAR = re.compile(r"(?<![\w*])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![\w*])", re.DOTALL)
_ITALIC_UNDERSCORE = re.compile(r"(?<![\w_])_(?=[^\s_])(.+?)(?<=[^\s_])_(?![\w_])", re.DOTALL)
_HEADING = re.compile(r"^\s{0,3}#{1,6}(?:\s|$)")
_RULE = re.compile(r"^\s*(?:[-*_]\s*){3,}$")
_WHOLE_EMPHASIS = re.compile(r"^\s*(?:\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)(?:\*\*|__|\*|_)\s*$")
_LABEL_MAX_WORDS = 12


def _unwrap_emphasis(text: str) -> str:
    """Emphasis marks off, the words kept; a span that carries a locus (a
    digit: "Institutes V.26") is a citation label and goes whole."""
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
    """Spoken prose: headings, rules, block quotes and label lines go;
    inline emphasis marks come off. Record tags are kept intact."""
    tags: list[str] = []

    def hide(match: re.Match) -> str:
        tags.append(match.group(0))
        return _PLACEHOLDER.format(len(tags) - 1)

    text = re.sub(r"\[\[[^\]\[]*\]\]", hide, raw_text)
    lines = []
    for line in text.split("\n"):
        if _HEADING.match(line) or _RULE.match(line) or line.lstrip().startswith(">"):
            continue
        whole = _WHOLE_EMPHASIS.match(line)
        if whole:
            body = whole.group(1).strip()
            if len(body.split()) <= _LABEL_MAX_WORDS and not re.search(r"[.!?][\"'”’)]*$", body):
                continue
        line = _unwrap_emphasis(line)
        lines.append(re.sub(r"[ \t]{2,}", " ", line).rstrip())
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return re.sub(r"\u0000(\d+)\u0000", lambda m: tags[int(m.group(1))], text)


_VERB = (
    r"(?:said|says|say|wrote|writes|write|declared|declares|declare|preached|preaches|preach|taught|teaches|teach|"
    r"put\s+it|puts\s+it|insisted|insists|replied|replies|answered|answers|warned|warns|urged|urges|added|adds|"
    r"explained|explains|confessed|confesses|argued|argues|affirmed|affirms|maintained|maintains|stated|states|"
    r"observed|observes|noted|notes|cried|exclaimed|prayed|prays|asked|asks|told\s+\w+|tells\s+\w+)"
)
_ADVERB = r"(?:\s+(?:(?:this|that|the\s+same)\s+way|it|so|this|that|again|later|then|there|here|well|in\s+\w+|\w+ly)){0,3}"
_FORMULA = re.compile(
    rf"(?P<as>\bas\s+(?P<who>[^.!?:;,]{{1,70}}?)\s+{_VERB}\b{_ADVERB}\s*,)"
    rf"|(?P<verb>\b{_VERB}\b{_ADVERB}\s*:)"
    r"|(?P<words>\bin\s+(?:the\s+words\s+of\s+[^.!?:;]{1,40}|[\w'’]+\s+(?:own\s+)?words|"
    r"(?:his|her|their)\s+(?:own\s+)?words)\s*[:,])"
    r"|(?P<acc>\baccording\s+to\s+[^.!?:;]{1,60}:)",
    re.IGNORECASE,
)
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


def _names_someone(text: str) -> bool:
    for word in _WORD.findall(text):
        lowered = word.lower()
        if lowered in _PERSON_PRONOUNS:
            return True
        if word[:1].isupper() and lowered not in _NON_NAMES:
            return True
    return False


def attribution_formula(sentence: str) -> tuple[re.Match, str] | None:
    """The first attribution formula in `sentence` whose subject is a named
    person or source (or a he/she/they standing for one), with the text
    that follows it. Formulas spoken by "we" or "I" are the world's own voice
    and are not attributions."""
    for match in _FORMULA.finditer(sentence):
        if match.group("as"):
            subject = match.group("who")
        elif match.group("verb"):
            subject = " ".join(sentence[: match.start()].split()[-8:])
        else:
            subject = match.group(0)
        if _names_someone(subject):
            return match, sentence[match.end():]
    return None


def _words(text: str) -> int:
    return len(_normalize(text).split())


def _typed_quotations(sentence: str, echoes: QuotationIndex) -> list[tuple[int, int, str]]:
    return [
        (open_i, close_i, inner)
        for open_i, close_i, inner in _checked_pairs(sentence)
        if _words(inner) >= SINGLE_QUOTE_MIN_WORDS and not echoes.holds(inner)
    ]


def _outside_quotations(sentence: str) -> str:
    text = sentence
    for open_i, close_i, _inner in reversed(_checked_pairs(sentence)):
        text = text[:open_i] + " " + text[close_i + 1:]
    return text


_SPEECH_VERB = re.compile(rf"\b{_VERB}\b", re.IGNORECASE)


def _ends_with_lead(sentence: str) -> bool:
    """A sentence that reads as the introduction to words that follow: it
    ends in a colon, or a named person or source is its subject of a speech
    verb."""
    stripped = _TAG.sub("", sentence).rstrip()
    if stripped.endswith(":"):
        return True
    verb = _SPEECH_VERB.search(stripped)
    return bool(verb) and _names_someone(" ".join(stripped[: verb.start()].split()[-8:]))


def _lead_for_quote(lead: str) -> str:
    lead = lead.strip()
    if not lead:
        return ""
    trailing_tags = ""
    while True:
        match = re.search(r"(\s*\[\[[a-z0-9_.-]+\]\])\s*$", lead)
        if not match:
            break
        trailing_tags = match.group(1) + trailing_tags
        lead = lead[: match.start()]
    lead = re.sub(r"[\s.!?;,:]+$", "", lead)
    return f"{lead}{trailing_tags}:" if lead else ""


def _settable(composed: str, rendering: str) -> bool:
    if len(quote_aware_sentences(composed)) != 1 or _PARAGRAPH_BREAK.search(composed):
        return False
    return any(inner == rendering for _o, _c, inner in quoted_span_positions(_TAG.sub("", composed)))


def shape_reply(raw_text: str, *, repository_records: dict[str, dict], context: PlacementContext) -> dict:
    """The voice's raw tagged text shaped as described in the module
    docstring. Returns {"text", "placed", "removed"}."""
    report = _Report()
    echoes = QuotationIndex({}, list(context.echo_texts))
    paragraphs_out: list[list[str]] = []
    story_seen: dict[str, int] = {}
    drop_next_for: str | None = None
    text = strip_markdown(raw_text or "")

    for paragraph in (p for p in _PARAGRAPH_BREAK.split(text) if p.strip()):
        kept: list[str] = []
        sentences = quote_aware_sentences(paragraph)
        index = 0
        while index < len(sentences):
            sentence = sentences[index]
            index += 1

            marker = _MARKER.search(sentence)
            if marker:
                lead = sentence[: marker.start()].strip()
                rest = sentence[marker.end():]
                reason, record = _placement_verdict(marker.group(0), repository_records, context, len(report.placed))
                composed = None
                if reason is None:
                    if not lead:
                        lead = _take_lead_in(kept, paragraphs_out)
                    rendering = record["modern_rendering"]
                    composed = f"{_lead_for_quote(lead)} \u201c{rendering}\u201d [[{record['id']}]]".strip()
                    if not _settable(composed, rendering):
                        reason, composed = REASON_NOT_SETTABLE, None
                if composed is None:
                    report.drop(f"{lead} {_MARKER.sub('', sentence)}".strip() if lead else sentence, reason)
                    if not lead and (previous := _take_lead_in(kept, paragraphs_out, only_if_lead=True)):
                        report.drop(previous, REASON_LEAD_IN)
                else:
                    kept.append(composed)
                    report.placed.append(record["id"])
                    paragraphs_out.append(kept)
                    kept = []
                tail = re.sub(r"^[\s.,;:!?]+", "", rest)
                if tail:
                    if tail[0].islower() or tail[0].isdigit():
                        ended = _SENTENCE_END.search(tail)
                        tail = tail[ended.end():].strip() if ended else ""
                    if tail:
                        sentences.insert(index, tail)
                continue

            if drop_next_for is not None:
                report.drop(sentence, drop_next_for)
                drop_next_for = None
                continue

            story_tags = [t for t in _TAG.findall(sentence) if t in context.told_stories]
            if story_tags:
                if any(story_seen.get(t, 0) >= 1 for t in story_tags):
                    report.drop(sentence, REASON_STORY_RETOLD)
                    continue
                for t in story_tags:
                    story_seen[t] = story_seen.get(t, 0) + 1

            typed = _typed_quotations(sentence, echoes)
            if typed:
                report.drop(sentence, REASON_TYPED_QUOTATION)
                last_open, last_close, last_inner = max(typed, key=lambda t: t[1])
                after = sentence[last_close + 1:].strip()
                if after and after[0].isupper() and re.search(r"[.!?]\s*$", last_inner):
                    sentences.insert(index, after)
                head = _TAG.sub("", sentence[: last_close + 1])
                if not _outside_quotations(head).strip(" \t.,;:!?-\u2014"):
                    if lead := _take_lead_in(kept, paragraphs_out, only_if_lead=True):
                        report.drop(lead, REASON_LEAD_IN)
                continue

            formula = attribution_formula(_outside_quotations(sentence))
            if formula is not None:
                _match, tail = formula
                if _WORD.search(_TAG.sub("", tail)):
                    report.drop(sentence, REASON_ATTRIBUTION)
                    continue
                report.drop(sentence, REASON_ATTRIBUTION_LEAD)
                drop_next_for = REASON_ATTRIBUTION_LEAD
                continue

            kept.append(sentence)
        if kept:
            paragraphs_out.append(kept)

    shaped = "\n\n".join(" ".join(p) for p in paragraphs_out if p)
    return {"text": shaped, "placed": report.placed, "removed": report.removed}


def _take_lead_in(kept: list[str], paragraphs_out: list[list[str]], *, only_if_lead: bool = False) -> str:
    """The sentence before a quotation that stands alone: the previous
    sentence of this paragraph, or the previous paragraph's last when that
    paragraph is that one sentence or ends in a colon. With `only_if_lead`
    the sentence must also read as an introduction (_ends_with_lead)."""
    if kept:
        if only_if_lead and not _ends_with_lead(kept[-1]):
            return ""
        return kept.pop()
    if paragraphs_out and paragraphs_out[-1]:
        previous = paragraphs_out[-1]
        if len(previous) == 1 or _TAG.sub("", previous[-1]).rstrip().endswith(":"):
            if only_if_lead and not _ends_with_lead(previous[-1]):
                return ""
            lead = previous.pop()
            if not previous:
                paragraphs_out.pop()
            return lead
    return ""


def _placement_verdict(
    marker: str, repository_records: dict[str, dict], context: PlacementContext, placed_so_far: int
) -> tuple[str | None, dict | None]:
    """(reason it cannot be placed, None) or (None, the quote record)."""
    found = _MARKER_ID.fullmatch(marker)
    record_id = found.group(1).lower() if found else None
    record = repository_records.get(record_id) if record_id else None
    if record is None or record.get("record_type") != "quote" or record_id not in context.offered:
        return REASON_NOT_OFFERED, None
    if record_id in context.voiced:
        return REASON_ALREADY_VOICED, None
    if placed_so_far >= context.max_quotes:
        return REASON_SECOND_QUOTE, None
    if not (record.get("modern_rendering") or "").strip():
        return REASON_NOT_OFFERED, None
    return None, record
