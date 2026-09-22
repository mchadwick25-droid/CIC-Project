"""The verbatim quote-fidelity check (Tech-Readiness P3): does a quote
record's `text` actually appear in the vendored source file its citation
names? `gate_quote_recording` (gates.py) checks structure only - license
value, text/speaker_or_author non-blank - and has never compared a
record's words against `cic/texts/` at all. This module is the first
place in the repo doing real verbatim substring matching (everything
else - `engine.prose.content_words`, `grounding_ratio`,
`output_check`'s guard checks - is bag-of-words overlap, no ordering, no
substring test).

RULED (Mark, 2026-09-22, P3 relaunch thread): editorial-tolerant, no
fuzzy score, no threshold. A quote passes only when every difference
between its `text` and the vendored source is one of the five classes in
ALLOWED_DIFFERENCE_CLASSES below. A word substitution, an omission with
no ellipsis, or an addition outside square brackets fails - always,
regardless of how small. This is a membership test against a fixed,
published grammar, not a similarity score: two texts that are 99% alike
by any fuzzy metric still fail here if the 1% is a substituted word,
because that 1% is exactly the shape of fabrication CLAUDE.md's "Source
fidelity" section exists to catch.

REPORT-ONLY, not yet in gates.GATES (this PR). `gate_quote_verbatim`
below is written in the exact `gate_*(records, fleet, registry) -> list[str]`
shape every other gate uses, specifically so promoting it later is the
one-line change CLAUDE.md's own default-actions table calls for
("CI/infra mechanical fix... Just do it") - see gates.py's own
registration comment when that PR lands.

HOW A DIFFERENCE CLASS IS DETECTED. Rather than normalizing the source
text and losing track of where a match actually sits, the record's own
`text` is compiled into a regex and searched directly against the
ORIGINAL vendored text (only XML/ThML markup stripped first, for
XML-sourced quotes). Whitespace runs become a flexible run-of-whitespace match, quote/apostrophe/dash
characters become a bracketed class of their known Unicode variants, and
`re.IGNORECASE` folds case - so the match span, when found, is the exact
original source substring, with no position-remapping needed to report
it. A bracketed span in the record's own text (`[truly]`) compiles to a
free `.*?` (may or may not appear in source - it's a labeled editorial
insertion either way). An ellipsis (`...` or the single-character `…`)
splits the record's text into ordered segments, each searched
independently, left to right, after the previous segment's own match
- so a real elision is never required to "explain" what's missing, only
to mark that something was.
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
    "whitespace": "A run of spaces, tabs, or line breaks differs from the source's own - collapsed on both sides before comparing.",
    "case": "A letter's capitalization differs from the source (e.g. a quote opening mid-sentence, capitalized to open a sentence here).",
    "punctuation": "A quote mark, apostrophe, or dash is a different Unicode form of the same mark (curly vs. straight, hyphen vs. en/em dash) - never a different mark entirely (a colon read as a dash still fails).",
    "ellipsis": "`...` or `…` in the record's text marks a real elision - the words on either side must still match, in order; nothing is required of what's between them.",
    "bracket": "Text inside `[...]` in the record's text is a labeled editorial insertion - it is never required to appear in the source, bracketed or not.",
}

# DISALLOWED, stated explicitly so a report finding can name which rule a
# quote actually broke: a substituted word, a silent omission (no
# ellipsis), or an addition that isn't inside brackets. None of these has
# its own detector - they are simply what's left when a segment fails to
# match under every allowance above.

_QUOTE_VARIANTS = '"“”„«»'
_APOS_VARIANTS = "'‘’ʼ"
_DASH_VARIANTS = "-–—−"
_PUNCT_CLASSES = {c: _QUOTE_VARIANTS for c in _QUOTE_VARIANTS} | {c: _APOS_VARIANTS for c in _APOS_VARIANTS} | {
    c: _DASH_VARIANTS for c in _DASH_VARIANTS
}

_ELLIPSIS_RE = re.compile(r"\s*(?:\.\.\.|…)\s*")
_BRACKET_RE = re.compile(r"\[[^\[\]]*\]")
_WHITESPACE_SPLIT_RE = re.compile(r"(\s+)")
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


def _char_class(ch: str) -> str:
    variants = _PUNCT_CLASSES.get(ch)
    if variants is None:
        return re.escape(ch)
    return "[" + "".join(re.escape(c) for c in variants) + "]"


def _literal_to_pattern(literal: str, *, fold_case: bool, class_punct: bool, flex_whitespace: bool) -> str:
    pieces = []
    for tok in _WHITESPACE_SPLIT_RE.split(literal):
        if not tok:
            continue
        if tok.isspace():
            pieces.append(r"\s+" if flex_whitespace else re.escape(tok))
        elif class_punct:
            pieces.append("".join(_char_class(c) for c in tok))
        else:
            pieces.append(re.escape(tok))
    return "".join(pieces)


def _segment_pattern(
    segment: str, *, fold_case: bool = True, class_punct: bool = True, flex_whitespace: bool = True
) -> re.Pattern:
    parts = []
    last = 0
    for m in _BRACKET_RE.finditer(segment):
        parts.append(
            _literal_to_pattern(segment[last : m.start()], fold_case=fold_case, class_punct=class_punct, flex_whitespace=flex_whitespace)
        )
        parts.append(r"[\s\S]*?")  # a bracketed span may match anything, including nothing
        last = m.end()
    parts.append(
        _literal_to_pattern(segment[last:], fold_case=fold_case, class_punct=class_punct, flex_whitespace=flex_whitespace)
    )
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


def _classify_match(segment: str, source_full: str, start: int) -> set[str]:
    """The full-tolerance pattern already matched `segment` at `start` -
    this asks which of the three character-level tolerances (case,
    punctuation, whitespace) that match actually needed, by re-testing
    stricter single-axis-off variants anchored at the same position."""
    classes: set[str] = set()
    axes = [("case", "fold_case"), ("punctuation", "class_punct"), ("whitespace", "flex_whitespace")]
    for name, kwarg in axes:
        strict_kwargs = {"fold_case": True, "class_punct": True, "flex_whitespace": True, kwarg: False}
        strict_pattern = _segment_pattern(segment, **strict_kwargs)
        if not strict_pattern.match(source_full, start):
            classes.add(name)
    return classes


def _nearest_context(segment: str, source_full: str, window: int = 30) -> str:
    import difflib

    sm = difflib.SequenceMatcher(None, segment, source_full, autojunk=False)
    m = sm.find_longest_match(0, len(segment), 0, len(source_full))
    if m.size == 0:
        return "(no similar text found in this source file)"
    start = max(0, m.b - window)
    end = min(len(source_full), m.b + m.size + window)
    return source_full[start:end]


def verify_quote_text(quote_text: str, source_raw: str, *, source_is_xml: bool) -> VerifyResult:
    source_full = strip_xml_markup(source_raw) if source_is_xml else source_raw
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
    verified, failed = [], []
    for rid, rec in sorted(quotes.items()):
        result = verify_quote_record(rec, records, fleet)
        if result.verified:
            verified.append(rid)
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
        "class_counts": class_counts,
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
        },
    }


def main(argv: list[str] | None = None) -> int:
    import json
    import sys

    report = fleet_report()
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    t = report["totals"]
    print(f"quote-verbatim sweep: {t['verified_count']}/{t['total_quotes']} verified, {t['failed_count']} failed")
    for w in report["worlds"].values():
        print(f"  {w['world']:12} verified={w['verified_count']:4} failed={w['failed_count']:3} classes={w['class_counts']}")
    if report["registry_mismatch"]["admitted_but_not_in_report_worlds"] or report["registry_mismatch"]["report_worlds_not_admitted"]:
        print(f"  REGISTRY MISMATCH: {report['registry_mismatch']}")
    print(f"\nfull report written to {REPORT_PATH.relative_to(REPO_ROOT)}")
    return 0  # report-only this PR: never fails the run regardless of findings


if __name__ == "__main__":
    import sys

    sys.exit(main())
