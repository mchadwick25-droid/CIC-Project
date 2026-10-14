"""OG-10 (Build/worlds/pahc/Open_Gaps_Tracking.md): does a non-quote record's own
spoken text carry an embedded old-translation quotation - 8 or more words
inside quotation marks - with no modern-English rendering of that wording?
The rule that spoken form must be modern English (`Build/reference/method/
CiC_Record_Native_World_Build_Process_V1.5.md`) is enforced only via
`record_type == "quote"` branches in `engine/m1/gates.py`: a `quote`
record carries its own `modern_rendering` field and is graded on it; every
other spoken record type (story, gravity, force, term, ...) has no such
field in its schema at all (`Build/reference/Redesign-Spec/
Artifact-1-Record-Schema.md` SS4), so an archaic quotation folded into one
of those records' own prose - brackets, editorial interpolations, and all
- reaches a participant exactly as the vendored 19th-century translation
wrote it.

REPORT-ONLY, a registered standing check - the same status `engine.m1.
sentence_completeness` already carries. This module does not grade or
fail anything (no entry in `engine.m1.gates.GATES`) and never rewrites a
record - it only finds and counts. `Build/worlds/pahc/Open_Gaps_Tracking.md`
OG-10 has this module's own current per-record, per-world counts.

SCOPE: every field `engine.m1.spoken_fields.fields_with_role` declares
`voice-diet` or `evidence-head` for a record's own `record_type` - text
that reaches a participant, not citation apparatus like `sources[].locus`,
which is never compiled into what the voice sees or says. `quote` records
are excluded entirely (their own `modern_rendering` field, and
`engine.m1.gates`'s existing quote-specific check, already own this
question for them).

FIELD-BY-FIELD, NOT WHOLE-RECORD: pairing quotes by scanning forward
through a whole record's unrelated fields joined into one blob lets an
odd quote count in one field pair its own opener with a much later,
unrelated field's closer, producing one huge false "span". Walking field
by field, the same shape `engine.prose.all_text()` itself walks, keeps
every pairing inside the prose it actually came from.

QUOTE-MARK FAMILY, NOT MIXED: a real quotation opens and closes with the
same mark family (straight or curly double, or straight or curly single)
- pairing across families (a double open with a single close, or vice
versa) lets a nested quote-within-a-quote of the OTHER family swallow the
outer quotation's own real close. `quoted_spans_by_family` pairs each
family separately rather than reusing `engine.m4.grounding_net.
quoted_span_positions`'s own family-blind scan (built for citation-mark
placement, where a live model's own quoting habits make a cross-family
pair rare; this module scans hand-authored prose across many styles,
where it is not rare).

A possessive apostrophe ("the fathers' grace", "nourishes' the poor
man's") is never specially excluded: any close-shaped mark ends the
nearest still-open span of the same family, whether or not it happens to
look like a possessive. This is right far more often than not - a
possessive sitting BETWEEN two separate quotations never becomes a
candidate close at all, since no open is pending there - but a
possessive sitting INSIDE a still-open span does end it early, same as
any other close-shaped mark would. `Build/worlds/pahc/Open_Gaps_Tracking.md`
OG-10 has this module's own count of how often that actually happens
fleet-wide, and records it as a known, accepted limitation rather than a
second layer of guesswork on top of this rule.

Usage: `python -m engine.m1.embedded_quotations` - writes
`engine/m1/reports/embedded-quotations-report-<date>.json` and prints a
per-world summary.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

from engine.m1.loader import load_world_records
from engine.m1.quote_verbatim import REPORT_WORLDS
from engine.m1.spoken_fields import fields_with_role

REPORTS_DIR = Path(__file__).resolve().parent / "reports"

MIN_QUOTED_WORDS = 8

# Same shape as engine.prose.QUOTE_OPEN/QUOTE_CLOSE, split one family at a
# time. Close detection also accepts an em dash, a slash, or another
# quote mark immediately after (a close can be followed directly by more
# punctuation, not only whitespace or [.,;:!?)]).
_DOUBLE_OPEN = re.compile(r"""(?:^|[\s:,\-(])["“](?=\S)""")
_DOUBLE_CLOSE = re.compile(r"""(?<=\S)["”](?=[\s.,;:!?)/—'’]|$)""")
_SINGLE_OPEN = re.compile(r"""(?:^|[\s:,\-(])['‘](?!(?:[Tt]is|[Tt]was|[Tt]will|[Tt]were)\b)(?=\S)""")
_SINGLE_CLOSE = re.compile(r"""(?<=\S)['’](?=[\s.,;:!?)/—"“]|$)""")

# A span whose own text names the project's build apparatus rather than
# quoting a vendored historical source - Doc_0N/G-cell citations and the
# gravity/force CLASSIFICATION header. Not an old-translation quotation
# at all - tagged, not counted as one.
_BUILD_DOCUMENT_SELF_QUOTE = re.compile(r"\bDoc_0\d\b|\bG\d\b|\bCLASSIFICATION\b")


def _family_spans(text: str, open_re: re.Pattern, close_re: re.Pattern) -> list[tuple[int, int, str]]:
    spans = []
    pos = 0
    while True:
        open_m = open_re.search(text, pos)
        if not open_m:
            return spans
        close_m = close_re.search(text, open_m.end())
        if not close_m:
            return spans
        spans.append((open_m.end() - 1, close_m.end(), text[open_m.end() : close_m.start()]))
        pos = close_m.end()


def quoted_spans_by_family(text: str) -> list[tuple[int, int, str]]:
    """Every paired quotation in `text`, left to right, double and single
    families paired independently then merged in document order - see
    the module docstring's own "QUOTE-MARK FAMILY, NOT MIXED" section."""
    spans = _family_spans(text, _DOUBLE_OPEN, _DOUBLE_CLOSE) + _family_spans(text, _SINGLE_OPEN, _SINGLE_CLOSE)
    return sorted(spans, key=lambda s: s[0])


def word_count(s: str) -> int:
    return len(s.split())


def _field_texts(record: dict) -> list[tuple[str, str]]:
    """(field_key, text) for every spoken (voice-diet or evidence-head)
    string this record's own declared fields carry. A field can hold a
    plain string, a list of strings, or (`demonstration.exchange`) a list
    of `{speaker, text}` dicts - walked generically the same way
    `engine.prose.all_text()` does, just scoped to this record_type's own
    spoken field list first."""
    out: list[tuple[str, str]] = []
    roles = fields_with_role(record.get("record_type"), "voice-diet", "evidence-head")

    def walk(value, key):
        if isinstance(value, str):
            out.append((key, value))
        elif isinstance(value, dict):
            for v in value.values():
                walk(v, key)
        elif isinstance(value, list):
            for item in value:
                walk(item, key)

    for field in roles:
        if field in record:
            walk(record[field], field)
    return out


def find_embedded_quotations(record: dict) -> list[dict]:
    """Every quoted span of `MIN_QUOTED_WORDS` or more inside `record`'s
    own spoken fields - empty for a `quote` record (excluded by the
    caller) or a record with no qualifying span. Each hit carries
    `self_quote_of_build_document`: True for a span naming the project's
    own build apparatus (Doc_0N, a G-cell, CLASSIFICATION) rather than
    quoting a vendored historical source - see the module docstring."""
    hits = []
    for field_key, text in _field_texts(record):
        for _start, _end, inner in quoted_spans_by_family(text):
            words = word_count(inner)
            if words >= MIN_QUOTED_WORDS:
                hits.append({
                    "field": field_key,
                    "span": inner,
                    "words": words,
                    "self_quote_of_build_document": bool(_BUILD_DOCUMENT_SELF_QUOTE.search(inner)),
                })
    return hits


def survey_world(world_key: str, load=load_world_records) -> dict:
    records = load(world_key)
    findings = []
    self_quote_findings = []
    for rid, rec in sorted(records.items()):
        if rec.get("record_type") == "quote":
            continue
        hits = find_embedded_quotations(rec)
        old_translation_hits = [h for h in hits if not h["self_quote_of_build_document"]]
        self_quote_hits = [h for h in hits if h["self_quote_of_build_document"]]
        if old_translation_hits:
            findings.append({"id": rid, "record_type": rec.get("record_type"), "spans": old_translation_hits})
        if self_quote_hits:
            self_quote_findings.append({"id": rid, "record_type": rec.get("record_type"), "spans": self_quote_hits})
    return {
        "world": world_key,
        "non_quote_records": sum(1 for r in records.values() if r.get("record_type") != "quote"),
        "records_with_embedded_quotation": len(findings),
        "span_count": sum(len(f["spans"]) for f in findings),
        "findings": findings,
        "records_with_build_document_self_quote": len(self_quote_findings),
        "self_quote_span_count": sum(len(f["spans"]) for f in self_quote_findings),
        "self_quote_findings": self_quote_findings,
    }


def fleet_report(worlds=REPORT_WORLDS) -> dict:
    per_world = {w: survey_world(w) for w in worlds}
    totals = {
        "non_quote_records": sum(w["non_quote_records"] for w in per_world.values()),
        "records_with_embedded_quotation": sum(w["records_with_embedded_quotation"] for w in per_world.values()),
        "span_count": sum(w["span_count"] for w in per_world.values()),
        "records_with_build_document_self_quote": sum(w["records_with_build_document_self_quote"] for w in per_world.values()),
        "self_quote_span_count": sum(w["self_quote_span_count"] for w in per_world.values()),
    }
    return {"min_quoted_words": MIN_QUOTED_WORDS, "worlds": per_world, "totals": totals}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=REPORTS_DIR / f"embedded-quotations-report-{date.today().isoformat()}.json")
    args = parser.parse_args(argv)

    report = fleet_report()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    t = report["totals"]
    print(
        f"embedded-quotations sweep: {t['records_with_embedded_quotation']}/{t['non_quote_records']} "
        f"non-quote records carry a {MIN_QUOTED_WORDS}+ word embedded quotation, {t['span_count']} spans total "
        f"(plus {t['records_with_build_document_self_quote']} records / {t['self_quote_span_count']} spans "
        f"that self-quote the project's own build apparatus, not an old translation - tagged separately)"
    )
    for w in report["worlds"].values():
        print(
            f"  {w['world']:12} records={w['records_with_embedded_quotation']:3} spans={w['span_count']:4} "
            f"self_quote_records={w['records_with_build_document_self_quote']:3} self_quote_spans={w['self_quote_span_count']:4}"
        )
    print(f"\nfull report written to {args.out}")
    return 0  # report-only: never fails the run on findings


if __name__ == "__main__":
    import sys

    sys.exit(main())
