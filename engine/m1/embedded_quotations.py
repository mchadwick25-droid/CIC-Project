"""OG-10 (worlds/pahc/Open_Gaps_Tracking.md; measured fleet-wide in PR #480
comment 5817505651): does a non-quote record's own spoken text carry an
embedded old-translation quotation - 8 or more words inside quotation
marks - with no modern-English rendering of that wording?
The rule that spoken form must be modern English (`reference/method/
CiC_Record_Native_World_Build_Process_V1.5.md`) is enforced only via
`record_type == "quote"` branches in `engine/m1/gates.py`: a `quote`
record carries its own `modern_rendering` field and is graded on it; every
other spoken record type (story, gravity, force, term, ...) has no such
field in its schema at all (`reference/Redesign-Spec/
Artifact-1-Record-Schema.md` SS4), so an archaic quotation folded into one
of those records' own prose - brackets, editorial interpolations, and all
- reaches a participant exactly as the vendored 19th-century translation
wrote it.

REPORT-ONLY. This module does not grade or fail anything (no entry in
`engine.m1.gates.GATES`) and never rewrites a record - it only finds and
counts. `worlds/pahc/Open_Gaps_Tracking.md` OG-10 has this module's own
per-world reproduction of PR #480's fleet-wide count, at record-id
granularity, plus a proposed mechanism (not yet built - see that entry).

SCOPE: every field `engine.m1.spoken_fields.fields_with_role` declares
`voice-diet` or `evidence-head` for a record's own `record_type` - text
that reaches a participant, not citation apparatus like `sources[].locus`,
which is never compiled into what the voice sees or says. `quote` records
are excluded entirely (their own `modern_rendering` field, and
`engine.m1.gates`'s existing quote-specific check, already own this
question for them).

FIELD-BY-FIELD, NOT WHOLE-RECORD: `engine.m4.grounding_net.
quoted_span_positions` pairs the nearest open quote with the nearest close
quote by scanning forward through whatever text it is given - safe within
one field's own prose, but not across a whole record's unrelated fields
joined into one blob (an odd quote count in one field can pair its own
opener with a much later, unrelated field's closer, producing one huge
false "span"). Walking field by field, the same shape
`engine.prose.all_text()` itself walks, keeps every pairing inside the
prose it actually came from.

Usage: `python -m engine.m1.embedded_quotations` - writes
`engine/m1/reports/embedded-quotations-report-<date>.json` and prints a
per-world summary.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from engine.m1.loader import load_world_records
from engine.m1.quote_verbatim import REPORT_WORLDS
from engine.m1.spoken_fields import fields_with_role
from engine.m4.grounding_net import quoted_span_positions

REPORTS_DIR = Path(__file__).resolve().parent / "reports"

MIN_QUOTED_WORDS = 8


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
    caller) or a record with no qualifying span."""
    hits = []
    for field_key, text in _field_texts(record):
        for _start, _end, inner in quoted_span_positions(text):
            words = word_count(inner)
            if words >= MIN_QUOTED_WORDS:
                hits.append({"field": field_key, "span": inner, "words": words})
    return hits


def survey_world(world_key: str, load=load_world_records) -> dict:
    records = load(world_key)
    findings = []
    for rid, rec in sorted(records.items()):
        if rec.get("record_type") == "quote":
            continue
        hits = find_embedded_quotations(rec)
        if hits:
            findings.append({"id": rid, "record_type": rec.get("record_type"), "spans": hits})
    return {
        "world": world_key,
        "non_quote_records": sum(1 for r in records.values() if r.get("record_type") != "quote"),
        "records_with_embedded_quotation": len(findings),
        "span_count": sum(len(f["spans"]) for f in findings),
        "findings": findings,
    }


def fleet_report(worlds=REPORT_WORLDS) -> dict:
    per_world = {w: survey_world(w) for w in worlds}
    totals = {
        "non_quote_records": sum(w["non_quote_records"] for w in per_world.values()),
        "records_with_embedded_quotation": sum(w["records_with_embedded_quotation"] for w in per_world.values()),
        "span_count": sum(w["span_count"] for w in per_world.values()),
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
        f"non-quote records carry a {MIN_QUOTED_WORDS}+ word embedded quotation, {t['span_count']} spans total"
    )
    for w in report["worlds"].values():
        print(f"  {w['world']:12} records={w['records_with_embedded_quotation']:3} spans={w['span_count']:4}")
    print(f"\nfull report written to {args.out}")
    return 0  # report-only: never fails the run on findings


if __name__ == "__main__":
    import sys

    sys.exit(main())
