"""The verbatim quote-fidelity check (Tech-Readiness P3): does a quote
record's `text` actually appear in the vendored source file its citation
names? `gate_quote_recording` (gates.py) checks structure only - license
value, text/speaker_or_author non-blank - and has never compared a
record's words against `cic/texts/` at all. This module is the first
place in the repo doing real verbatim substring matching (everything
else - `engine.prose.content_words`, `grounding_ratio`,
`output_check`'s guard checks - is bag-of-words overlap, no ordering, no
substring test).

RULED (Mark, 2026-09-22, P3 relaunch thread, two rulings): editorial-
tolerant, no fuzzy score, no threshold. A quote passes only when every
difference between its `text` and the vendored source is one of the six
classes in ALLOWED_DIFFERENCE_CLASSES below - a sixth, `verse_number`,
added by Mark's second ruling the same day after the first fleet sweep
surfaced it as a real, distinct pattern (inline ANF/NPNF verse/section
numbering, not a fidelity defect). A seventh candidate the same sweep
found - a nested quotation mark rendered as a different mark - was ruled
NOT allowed: that stays a failure, fixed in the record, not accommodated
here. A word substitution, an omission with no ellipsis, or an addition
outside square brackets fails - always, regardless of how small. This is
a membership test against a fixed, published grammar, not a similarity
score: two texts that are 99% alike by any fuzzy metric still fail here
if the 1% is a substituted word, because that 1% is exactly the shape of
fabrication CLAUDE.md's "Source fidelity" section exists to catch.

REPORT-ONLY, not yet in gates.GATES (this PR). `gate_quote_verbatim`
below is written in the exact `gate_*(records, fleet, registry) -> list[str]`
shape every other gate uses, specifically so promoting it later is the
one-line change CLAUDE.md's own default-actions table calls for
("CI/infra mechanical fix... Just do it") - see gates.py's own
registration comment when that PR lands.

HOW A DIFFERENCE CLASS IS DETECTED. Rather than normalizing the source
text and losing track of where a match actually sits, the record's own
`text` is compiled into a regex and searched directly against the
ORIGINAL vendored text (XML/ThML markup stripped first for XML-sourced
quotes, then any word hyphenated across a line break - "eter-\nnity" -
collapsed back to one word, then the four closed apparatus forms
(`strip_apparatus`) dropped, all before any matching happens). Whitespace
runs become a flexible run-of-whitespace match, quote/apostrophe/dash
characters become a bracketed class of their known Unicode variants, and
`re.IGNORECASE` folds case - so the match span, when found, is the exact
(post-collapse) source substring, with no position-remapping needed to
report it. A bracketed span in the record's own text (`[truly]`)
compiles to a free `.*?` (may or may not appear in source - it's a
labeled editorial insertion either way). An ellipsis (`...`, the
single-character `…`, or either wrapped in its own brackets as `[...]`/
`[…]` - one marker, not a bracketed insertion around nothing) splits the
record's text into ordered segments, each searched independently, left
to right, after the previous segment's own match - so a real elision is
never required to "explain" what's missing, only to mark that something
was.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TEXTS_DIR = REPO_ROOT / "cic" / "texts"

# Printed in every report this module produces - the ruling's own words,
# not paraphrased, so a reader never has to trust a summary of what was
# actually allowed.
ALLOWED_DIFFERENCE_CLASSES: dict[str, str] = {
    "whitespace": "A run of spaces, tabs, or line breaks differs from the source's own - collapsed on both sides before comparing. Includes a source that hyphenates a word across a line break (\"eter-\\nnity\") - collapsed to the joined word before comparing, never left as two.",
    "case": "A letter's capitalization differs from the source (e.g. a quote opening mid-sentence, capitalized to open a sentence here).",
    "punctuation": "A quote mark, apostrophe, or dash is a different Unicode form of the same mark (curly vs. straight, hyphen vs. en/em dash) - never a different mark entirely (a colon read as a dash still fails).",
    "ellipsis": "`...` or `…` in the record's text marks a real elision - the words on either side must still match, in order; nothing is required of what's between them. `[...]`/`[…]` (the ellipsis wrapped in its own brackets) is the same single marker, not a bracketed insertion around nothing.",
    "bracket": "Text inside `[...]` in the record's text is a labeled editorial insertion - it is never required to appear in the source, bracketed or not.",
    "verse_number": "An inline Arabic verse or section number in the source edition, standing at a sentence boundary, may be absent from the quote's text - the words on either side must still match, in order. A bare 1-4 digit number followed by a period only; never a wider omission.",
    "apparatus": "A page/column locator the source edition itself inserts mid-sentence, in one of four closed, evidenced forms: a soft hyphen (U+00AD, always invisible, never real content); a tilde-wrapped digit run (`~1~`, this edition's own footnote-number convention); a pipe-plus-digits page marker (`|146`); or a bracketed locator - 3-4 bare digits with an optional trailing capital letter (`[964D]`, never 1-2 digits, which stays a record's own tolerated `[N]` section numbering instead), a `[p. NNN]` page reference, or an abbreviated `[Author. p. NNN, l. N.]` citation. Never a bare, unwrapped digit or symbol with no marker of its own - that stays a failure (see the module docstring's fourth-ruling note).",
}

# RULED (Mark, 2026-09-22, second ruling): class six (verse_number) above
# is allowed; class seven - a nested quotation mark rendered as a
# different mark (e.g. a straight double quote where the source has a
# curly single quote marking an inner quotation) - is NOT. That stays a
# failure and gets fixed in the record, not accommodated here.

# RULED (Mark, 2026-09-22, third ruling, after the #403 triage): two of
# the three patterns the triage flagged (not the stray-backslash one,
# left for the record-fix session) fold into the whitespace/ellipsis
# handling above rather than becoming new classes - each is a source-
# side typesetting/notation quirk, not a difference in what's actually
# said. The third (stray backslash) is a record-authoring bug, out of
# scope for this module.

# FOURTH ROUND (2026-09-23, after PR #413's record-fix pass left 13
# non-escalated failures, all apparatus the gate didn't yet strip): four
# closed, evidenced forms fold into the new `apparatus` class above -
# soft hyphen, tilde-digit, pipe-page, bracket-locator - each confirmed
# against the real vendored file before being added, never guessed. Left
# UNRESOLVED and explicitly NOT covered by `apparatus` above: a bare,
# unwrapped footnote digit or symbol with no marker character of its own
# (` 1 is more useful`, `Paula,276 mother`, `church.1\nAnd`, ` 163 and
# found`, ` ® But for prayer`) - stripping a bare digit globally risks
# silently swallowing a real number that's part of what a quote actually
# says elsewhere in the same file, and no safe, narrow rule for telling
# the two apart was found. Flagged for a ruling, same as every other
# candidate class this module has surfaced - not silently added and not
# silently ignored. See the fleet report for the six records this still
# blocks (five apparatus-only, one - `cappadocian.quote.basil-on-work-
# and-prayer` - already nested-mark-fixed by #413 but blocked here too).

# DISALLOWED, stated explicitly so a report finding can name which rule a
# quote actually broke: a substituted word, a silent omission (no
# ellipsis), or an addition that isn't inside brackets. None of these has
# its own detector - they are simply what's left when a segment fails to
# match under every allowance above.

# R33 (Mark, 2026-09-23, in his own words): "we should be setting
# principles we will have a 100 worlds and cant tell the representitive
# what to say for every quote." A quote whose primary-source text sits
# inside a translator's own `<note>` rather than the running text
# (pahc.quote.two-female-slaves-who-were-called-deaconesses: Pliny's
# letter to Trajan, quoted in full inside a translator's endnote, not in
# Eusebius's own running text) is handled by a gate-level fallback, never
# a per-record pointer: once the running text fails to verify, every
# `<note>` body in the same vendored source file is tried in turn, same
# tolerances as everywhere else. No record ever names which note - this
# supersedes R28 (2026-09-23, PR #423, not merged), which had a quote
# record opt in with its own `source_note_id` field naming the note
# directly; R33 ruled a mechanism at the gate level instead, since a
# hundred-world fleet can't carry a hand-set field on every record this
# pattern might touch. `VerifyResult.verified_in` records which path
# actually verified a quote ("running_text" or "note", with `note_id` set
# for the latter) so a note-verified record is always reported as what it
# is, never folded silently into an ordinary running-text pass.

_QUOTE_VARIANTS = '"“”„«»'
_APOS_VARIANTS = "'‘’ʼ"
_DASH_VARIANTS = "-–—−"
_PUNCT_CLASSES = {c: _QUOTE_VARIANTS for c in _QUOTE_VARIANTS} | {c: _APOS_VARIANTS for c in _APOS_VARIANTS} | {
    c: _DASH_VARIANTS for c in _DASH_VARIANTS
}

# `[...]`/`[…]` (the ellipsis wrapped in its own brackets, no other
# content) is tried first, as a single unit - splitting it the same as a
# bare `...` would otherwise leave a stray unmatched "[" at the end of
# one segment and "]" at the start of the next, both then required as
# literal characters (a real defect this ruling fixes: cappadocian.quote.
# basil-against-eunomius-ant marks its own elision exactly this way).
_ELLIPSIS_RE = re.compile(r"\s*(?:\[(?:\.\.\.|…)\]|\.\.\.|…)\s*")
_BRACKET_RE = re.compile(r"\[[^\[\]]*\]")
_WHITESPACE_SPLIT_RE = re.compile(r"(\s+)")
# A source that hyphenates a word across a line break ("eter-\nnity") -
# ordinary print-typesetting justification, not a content difference.
# Plain hyphen only (not an en/em dash - those mark real punctuation,
# not a word broken mid-line), collapsed before any matching happens so
# the quote's own unbroken word matches directly. Applied as a fixed-
# point loop for the rare case of two consecutive wraps ("a-\nb-\nc").
_LINEWRAP_HYPHEN_RE = re.compile(r"(\w)-\s*\n\s*(\w)")
# An inline verse/section number the source may carry at a word-boundary
# gap in the quote's own text (e.g. "...day. 2. First..." where the
# quote just has "...day. First..."). Bare digits + period only - never
# a wider skip, which is exactly the "no fuzzy score" line the ruling
# draws.
_VERSE_NUMBER_GAP = r"(?:\d{1,4}\.\s+)?"
# Four closed, evidenced apparatus forms (2026-09-23, fourth round) -
# each confirmed against a real vendored file's own break point before
# being added here, not a generic heuristic:
#   - a literal soft hyphen (U+00AD), always invisible, never content
#     (alx.quote.no-sun-no-moon-no-sky's own source: "sup\xadpose").
#   - a tilde-wrapped digit, this edition's own footnote convention,
#     with no surrounding whitespace at all in the raw source
#     (syr.quote.warned-before-baptism: "God~1~before").
#   - a pipe-plus-digits page marker, flanked by real whitespace
#     (desert.quote.pachomius-angel-tablet and others: "|113 And").
#   - a bracketed locator: 3-4 bare digits with an optional trailing
#     capital letter (a Migne-style column reference, "[964D]"), a
#     "[p. NNN]" page reference, or an abbreviated "[Author. p. NNN,
#     l. N.]" citation - all three confirmed against real breaks, not
#     invented shapes. The digit form is deliberately 3-4 digits only,
#     never 1-2: a record's own `[1]`, `[2]`... section numbering inside
#     its OWN quoted text is real content already tolerated by the
#     existing `bracket` class (desert.quote.the-noonday-demon uses
#     exactly this convention) - a 1-2 digit floor here would strip that
#     numbering out of the SOURCE and break the adjacency the quote's own
#     bracket-tolerance depends on. A real Migne/PG column reference is
#     always 3+ digits, so this floor costs nothing evidenced.
_SOFT_HYPHEN_RE = re.compile("­")
_TILDE_DIGIT_RE = re.compile(r"~\d{1,4}~")
_PIPE_PAGE_RE = re.compile(r"\|\d{1,4}\s*")
_BRACKET_LOCATOR_RE = re.compile(
    r"\["
    r"(?:\d{3,4}[A-Z]?"
    r"|p\.\s*\d{1,4}"
    r"|[A-Z][a-z]{0,4}\.\s*p\.\s*\d{1,4}(?:,\s*l\.\s*\d{1,4})?\.?"
    r")\]\s*"
)
_NOTE_BLOCK_RE = re.compile(r"<note\b[^>]*>.*?</note>", re.IGNORECASE | re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")
# A cited path can be hard-wrapped mid-filename in a record's free-text
# body (e.g. "cic/texts/anf01_apostolic-fathers-justin-\nirenaeus.xml" -
# real, seen in pahc.quote.ignatius-truly-born) - whitespace is allowed
# between filename characters and stripped back out of the capture.
_TEXTS_PATH_RE = re.compile(r"cic/texts/((?:[\w.\-]|\s+(?=[\w.\-]))+\.(?:txt|xml))")


def strip_xml_markup(raw: str) -> str:
    """ThML notes carry real prose (endnote text) that must not leak into
    the reading text a quote is checked against; every other tag
    (`<pb/>`, `<scripRef>`, `<index/>`...) is markup only - drop the tag,
    keep whatever text it wrapped."""
    text = _NOTE_BLOCK_RE.sub(" ", raw)
    text = _TAG_RE.sub("", text)
    return text


def collapse_linewrap_hyphens(text: str) -> str:
    """"eter-\\nnity" -> "eternity". A fixed-point loop, not a single
    `sub`, so a word wrapped twice in a row still fully joins."""
    prev = None
    while prev != text:
        prev = text
        text = _LINEWRAP_HYPHEN_RE.sub(r"\1\2", text)
    return text


def strip_apparatus(text: str) -> str:
    """Drop the four closed, evidenced apparatus forms above - soft
    hyphen, tilde-digit, pipe-page, bracket-locator - each a source
    edition's own page/column bookkeeping, never real quoted content.
    Deliberately NOT a bare unwrapped digit or symbol - see the fourth-
    round docstring note on why that stays unhandled here."""
    text = _SOFT_HYPHEN_RE.sub("", text)
    text = _TILDE_DIGIT_RE.sub(" ", text)
    text = _PIPE_PAGE_RE.sub("", text)
    text = _BRACKET_LOCATOR_RE.sub("", text)
    return text


def _char_class(ch: str) -> str:
    variants = _PUNCT_CLASSES.get(ch)
    if variants is None:
        return re.escape(ch)
    return "[" + "".join(re.escape(c) for c in variants) + "]"


def _literal_to_pattern(
    literal: str, *, fold_case: bool, class_punct: bool, flex_whitespace: bool, allow_verse_number: bool
) -> str:
    pieces = []
    for tok in _WHITESPACE_SPLIT_RE.split(literal):
        if not tok:
            continue
        if tok.isspace():
            if flex_whitespace:
                pieces.append(r"\s+" + (_VERSE_NUMBER_GAP if allow_verse_number else ""))
            else:
                pieces.append(re.escape(tok))
        elif class_punct:
            pieces.append("".join(_char_class(c) for c in tok))
        else:
            pieces.append(re.escape(tok))
    return "".join(pieces)


def _segment_pattern(
    segment: str,
    *,
    fold_case: bool = True,
    class_punct: bool = True,
    flex_whitespace: bool = True,
    allow_verse_number: bool = True,
) -> re.Pattern:
    kwargs = dict(fold_case=fold_case, class_punct=class_punct, flex_whitespace=flex_whitespace, allow_verse_number=allow_verse_number)
    parts = []
    last = 0
    for m in _BRACKET_RE.finditer(segment):
        parts.append(_literal_to_pattern(segment[last : m.start()], **kwargs))
        parts.append(r"[\s\S]*?")  # a bracketed span may match anything, including nothing
        last = m.end()
    parts.append(_literal_to_pattern(segment[last:], **kwargs))
    flags = re.DOTALL | (re.IGNORECASE if fold_case else 0)
    return re.compile("".join(parts), flags)


@dataclass
class SegmentResult:
    text: str
    matched: bool
    span: tuple[int, int] | None = None
    classes_used: set[str] = field(default_factory=set)


@dataclass
class VerifyResult:
    verified: bool
    source_file: str | None = None
    classes_used: set[str] = field(default_factory=set)
    failed_segment: str | None = None
    nearest_context: str | None = None
    # R33 (2026-09-23): which pass actually verified this quote -
    # "running_text" (the ordinary path, notes stripped) or "note" (the
    # fallback below matched inside a specific `<note>` body). `note_id`
    # is set only for the latter, and is the note's own `id` attribute
    # when it has one, else its 0-based position among notes in the file.
    verified_in: str = "running_text"
    note_id: str | None = None


def _classify_match(segment: str, source_full: str, start: int) -> set[str]:
    """The full-tolerance pattern already matched `segment` at `start` -
    this asks which of the four character/gap-level tolerances (case,
    punctuation, whitespace, verse_number) that match actually needed, by
    re-testing stricter single-axis-off variants anchored at the same
    position."""
    classes: set[str] = set()
    axes = [
        ("case", "fold_case"),
        ("punctuation", "class_punct"),
        ("whitespace", "flex_whitespace"),
        ("verse_number", "allow_verse_number"),
    ]
    for name, kwarg in axes:
        strict_kwargs = {"fold_case": True, "class_punct": True, "flex_whitespace": True, "allow_verse_number": True, kwarg: False}
        strict_pattern = _segment_pattern(segment, **strict_kwargs)
        if not strict_pattern.match(source_full, start):
            classes.add(name)
    return classes


def _nearest_context(segment: str, source_full: str, window: int = 30) -> str:
    import difflib

    # autojunk=True (the default) is what makes SequenceMatcher usable
    # against a whole vendored file rather than a short string - its
    # "popular element" heuristic is built for exactly this shape
    # (a short needle against a long haystack) and cut this function's
    # own runtime by roughly 9x against a 3.8MB source in testing;
    # False was tried first and made the fleet sweep impractically slow.
    sm = difflib.SequenceMatcher(None, segment, source_full)
    m = sm.find_longest_match(0, len(segment), 0, len(source_full))
    if m.size == 0:
        return "(no similar text found in this source file)"
    start = max(0, m.b - window)
    end = min(len(source_full), m.b + m.size + window)
    return source_full[start:end]


def verify_quote_text(quote_text: str, source_raw: str, *, source_is_xml: bool) -> VerifyResult:
    source_full = strip_xml_markup(source_raw) if source_is_xml else source_raw
    source_full = collapse_linewrap_hyphens(source_full)
    source_full = strip_apparatus(source_full)
    raw_segments = [s for s in _ELLIPSIS_RE.split(quote_text) if s.strip()]
    if not raw_segments:
        return VerifyResult(verified=False, failed_segment=quote_text, nearest_context="(quote text is empty)")

    classes_used: set[str] = set()
    if len(raw_segments) > 1:
        classes_used.add("ellipsis")

    search_from = 0
    for seg in raw_segments:
        seg = seg.strip()
        if _BRACKET_RE.search(seg):
            classes_used.add("bracket")
        pattern = _segment_pattern(seg)
        m = pattern.search(source_full, search_from)
        if not m:
            return VerifyResult(
                verified=False,
                failed_segment=seg,
                nearest_context=_nearest_context(seg, source_full),
            )
        classes_used |= _classify_match(seg, source_full, m.start())
        search_from = m.end()

    return VerifyResult(verified=True, classes_used=classes_used)


_NOTE_TAG_RE = re.compile(r"<note\b([^>]*)>(.*?)</note>", re.IGNORECASE | re.DOTALL)
_NOTE_ID_ATTR_RE = re.compile(r'\bid="([^"]*)"')


def iter_source_notes(source_raw: str):
    """Yield `(note_id, plain_text)` for every `<note>` block in a raw
    vendored source, in document order, tags stripped from each note's
    own body. A note with no `id` attribute of its own is identified by
    its 0-based position among the notes in this file, so the fallback
    below can still name which one verified a quote."""
    for i, m in enumerate(_NOTE_TAG_RE.finditer(source_raw)):
        id_match = _NOTE_ID_ATTR_RE.search(m.group(1))
        note_id = id_match.group(1) if id_match else f"#{i}"
        yield note_id, _TAG_RE.sub("", m.group(2))


def verify_quote_against_notes(quote_text: str, source_raw: str) -> VerifyResult | None:
    """R33's gate-level fallback: once the running text (notes stripped)
    has failed to verify a quote, try every `<note>` body in the same
    source file in turn - the rare case where a translator's endnote,
    not the primary running text, carries the actual primary-source
    quotation. Returns None (never a failing VerifyResult) if no note in
    the file verifies, so the caller's own running-text failure -
    reporting the more informative "nearest context" against the fuller
    running text - is what gets surfaced."""
    for note_id, note_text in iter_source_notes(source_raw):
        result = verify_quote_text(quote_text, note_text, source_is_xml=False)
        if result.verified:
            result.verified_in = "note"
            result.note_id = note_id
            return result
    return None


def resolve_vendored_paths(quote_record: dict, records: dict, fleet: dict) -> list[Path]:
    """The quote's own body prose is the more specific, more commonly
    present citation (`texts_registry.citing_records`' own docstring
    notes a real case where only the quote record, not its source
    record, names the file) - checked first. The source record's
    `edition` field is the fallback, since some quotes cite only via
    `source_id` with no path repeated in their own body."""
    body = quote_record.get("_body") or ""
    names = _extract_texts_filenames(body)
    if not names:
        for src in quote_record.get("sources") or []:
            source_rec = records.get(src.get("source_id")) or fleet.get(src.get("source_id"))
            if source_rec:
                names.extend(_extract_texts_filenames(source_rec.get("edition") or ""))
        names = list(dict.fromkeys(names))
    return [TEXTS_DIR / name for name in names]


def _extract_texts_filenames(text: str) -> list[str]:
    names = [re.sub(r"\s+", "", m.group(1)) for m in _TEXTS_PATH_RE.finditer(text)]
    return list(dict.fromkeys(names))


def verify_quote_record(quote_record: dict, records: dict, fleet: dict) -> VerifyResult:
    paths = resolve_vendored_paths(quote_record, records, fleet)
    if not paths:
        return VerifyResult(verified=False, failed_segment=None, nearest_context="no cic/texts/ file could be resolved from this record's body or its source_id's edition field")

    quote_text = quote_record.get("text") or ""
    best: VerifyResult | None = None
    for path in paths:
        if not path.exists():
            continue
        source_raw = path.read_text(encoding="utf-8", errors="replace")
        result = verify_quote_text(quote_text, source_raw, source_is_xml=path.suffix == ".xml")
        result.source_file = str(path.relative_to(REPO_ROOT))
        if result.verified:
            return result
        note_result = verify_quote_against_notes(quote_text, source_raw)
        if note_result is not None:
            note_result.source_file = str(path.relative_to(REPO_ROOT))
            return note_result
        if best is None:
            best = result
    if best is None:
        return VerifyResult(verified=False, nearest_context=f"none of the resolved files exist on disk: {[str(p) for p in paths]}")
    return best


def gate_quote_verbatim(records, fleet, registry) -> list[str]:
    """Same `gate_*` shape as everything in gates.GATES - not registered
    there yet (report-only, this PR)."""
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "quote":
            continue
        result = verify_quote_record(rec, records, fleet)
        if not result.verified:
            findings.append(
                f"{rid}: does not verify against {result.source_file or '(unresolved source)'} - "
                f"failed segment {result.failed_segment!r}; nearest source text: {result.nearest_context!r}"
            )
    return findings


# --- fleet report (report-only sweep; this module's own CLI) -----------

# The six worlds the 2026-08-28 admission pass already claimed
# verified-direct with a documented cic/texts/ pass, vs. the five that
# have never had one - the split Mark's ruling asked the first report to
# carry. Read off each world's own quote records' confidence.verification_state
# at run time (REPORT_WORLDS below), not hardcoded, so a world's real
# state always wins over this list if the two ever disagree.
AUDITED_WORLDS = ("pahc", "syr", "desert", "hal", "alx", "ijc")
OTHER_WORLDS = ("cappadocian", "don", "gallic", "rzg", "witt")
REPORT_WORLDS = AUDITED_WORLDS + OTHER_WORLDS

REPORT_PATH = Path(__file__).resolve().parent / "reports" / "quote-verbatim-report-2026-09-22.json"


def sweep_world(world_key: str, fleet: dict) -> dict:
    from engine.m1.loader import load_world_records

    records = load_world_records(world_key)
    quotes = {rid: r for rid, r in records.items() if r.get("record_type") == "quote"}
    class_counts = {name: 0 for name in ALLOWED_DIFFERENCE_CLASSES}
    exact_count = 0
    verified, failed, note_verified = [], [], []
    for rid, rec in sorted(quotes.items()):
        result = verify_quote_record(rec, records, fleet)
        if result.verified:
            verified.append(rid)
            if result.verified_in == "note":
                note_verified.append({"id": rid, "source_file": result.source_file, "note_id": result.note_id})
            if result.classes_used:
                for cls in result.classes_used:
                    class_counts[cls] += 1
            else:
                exact_count += 1
        else:
            failed.append(
                {
                    "id": rid,
                    "source_file": result.source_file,
                    "failed_segment": result.failed_segment,
                    "nearest_context": result.nearest_context,
                    "recorded_verification_state": (rec.get("confidence") or {}).get("verification_state"),
                }
            )
    return {
        "world": world_key,
        "total_quotes": len(quotes),
        "verified_count": len(verified),
        "failed_count": len(failed),
        "exact_no_diff_count": exact_count,
        "note_verified_count": len(note_verified),
        "class_counts": class_counts,
        "note_verified": note_verified,
        "failures": failed,
    }


def fleet_report() -> dict:
    from engine.m1.loader import load_fleet_records
    from engine.m1.registry import load_registry

    registry = load_registry()
    admitted = {k for k, v in registry.items() if v.get("state") == "admitted"}
    missing = admitted - set(REPORT_WORLDS)
    extra = set(REPORT_WORLDS) - admitted
    fleet = load_fleet_records()
    worlds = {w: sweep_world(w, fleet) for w in REPORT_WORLDS}
    return {
        "allowed_difference_classes": ALLOWED_DIFFERENCE_CLASSES,
        "audited_worlds": list(AUDITED_WORLDS),
        "other_worlds": list(OTHER_WORLDS),
        "registry_mismatch": {
            "admitted_but_not_in_report_worlds": sorted(missing),
            "report_worlds_not_admitted": sorted(extra),
        },
        "worlds": worlds,
        "totals": {
            "total_quotes": sum(w["total_quotes"] for w in worlds.values()),
            "verified_count": sum(w["verified_count"] for w in worlds.values()),
            "failed_count": sum(w["failed_count"] for w in worlds.values()),
            "note_verified_count": sum(w["note_verified_count"] for w in worlds.values()),
        },
    }


def main(argv: list[str] | None = None) -> int:
    import json
    import sys

    report = fleet_report()
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    t = report["totals"]
    print(
        f"quote-verbatim sweep: {t['verified_count']}/{t['total_quotes']} verified "
        f"({t['note_verified_count']} via a note), {t['failed_count']} failed"
    )
    for w in report["worlds"].values():
        note_tag = f" note_verified={w['note_verified_count']}" if w["note_verified_count"] else ""
        print(f"  {w['world']:12} verified={w['verified_count']:4} failed={w['failed_count']:3}{note_tag} classes={w['class_counts']}")
    if report["registry_mismatch"]["admitted_but_not_in_report_worlds"] or report["registry_mismatch"]["report_worlds_not_admitted"]:
        print(f"  REGISTRY MISMATCH: {report['registry_mismatch']}")
    print(f"\nfull report written to {REPORT_PATH.relative_to(REPO_ROOT)}")
    return 0  # report-only this PR: never fails the run regardless of findings


if __name__ == "__main__":
    import sys

    sys.exit(main())
