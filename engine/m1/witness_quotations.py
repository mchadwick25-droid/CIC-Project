"""Does every quotation inside a doctrinal witness's `text` appear, word for
word, in the vendored source the record cites?

A doctrinal witness's `text` is what a participant reads when the world's
answer record replaces a reply (engine.m4.turn.settle_reply), and the net
shows it as written. Its quotations are not checked at run time. This gate
checks them offline, with no model call, by the same matcher
`engine.m1.quote_verbatim.verify_quote_text` applies to a quote record's
`text`: the same tolerated differences (whitespace, case, quote marks,
ellipsis, bracketed insertions, verse numbers, edition apparatus) and no
others.

A quotation is a paired span of the `text` (engine.m1.embedded_quotations.
quoted_spans_by_family) of WITNESS_QUOTATION_MIN_WORDS or more words, after
the punctuation a sentence puts inside the marks is taken off. Shorter spans
are terms and titles. The vendored files come from the record's source
loci and body, and from its sources' editions (resolve_vendored_paths).

Like gate_quote_verbatim, it skips a record whose `verification_state` is
below verified-direct: such a record has already been through its own
escalation. `sweep` reports those too, apart from the gate's findings.

`WITNESS_QUOTATION_FINDINGS` lists the findings that stand today, one
"record id<TAB>quotation" line each. The test in
engine/m1/tests/test_witness_quotations.py fails on a finding not in it and
on a line whose quotation now verifies.

Usage: `python -m engine.m1.witness_quotations` prints every witness
quotation that does not verify, in every world.
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

from engine.m1.embedded_quotations import quoted_spans_by_family
from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import formation_world_keys
from engine.m1.quote_verbatim import (
    REPO_ROOT,
    TEXTS_DIR,
    _extract_texts_filenames,
    resolve_vendored_paths,
    strip_edition_apparatus,
    verify_quote_text,
)

WITNESS_QUOTATION_MIN_WORDS = 3
REQUIRED_VERIFICATION_STATE = "verified-direct"
WITNESS_QUOTATION_FINDINGS = Path(__file__).resolve().parent / "witness_quotation_findings.txt"
_EDGE_PUNCTUATION = ".,;:!?"


def witness_quotations(record: dict) -> list[str]:
    """The quotations in the record's `text` that the gate checks."""
    found = []
    for _start, _end, inner in quoted_spans_by_family(record.get("text") or ""):
        quotation = " ".join(inner.split()).strip(_EDGE_PUNCTUATION + " ")
        if len(quotation.split()) >= WITNESS_QUOTATION_MIN_WORDS:
            found.append(quotation)
    return found


def witness_source_paths(record: dict, records: dict, fleet: dict) -> list[Path]:
    """The vendored files the record cites: those its source loci and body
    name, then those its sources' editions name."""
    loci = " ".join((source.get("locus") or "") for source in record.get("sources") or [])
    names = _extract_texts_filenames(f"{loci} {record.get('_body') or ''}")
    paths = [TEXTS_DIR / name for name in names]
    paths += [path for path in resolve_vendored_paths(record, records, fleet) if path not in paths]
    return paths


@lru_cache(maxsize=16)
def _vendored_source(path: Path) -> str:
    return strip_edition_apparatus(path.read_text(encoding="utf-8", errors="replace"), path.name)


def quotation_verifies(quotation: str, paths: list[Path]) -> bool:
    for path in paths:
        if not path.exists():
            continue
        source = _vendored_source(path)
        if verify_quote_text(quotation, source, source_is_xml=path.suffix == ".xml").verified:
            return True
    return False


def failing_quotations(record: dict, records: dict, fleet: dict) -> list[str]:
    paths = witness_source_paths(record, records, fleet)
    return [q for q in witness_quotations(record) if not quotation_verifies(q, paths)]


def gate_witness_quotation_verbatim(records, fleet, registry) -> list[str]:
    """gates.py's shape. One finding per quotation that does not verify, in
    a doctrinal witness at verified-direct."""
    witnesses = [
        (rid, record) for rid, record in records.items()
        if record.get("record_type") == "doctrinal_witness"
        and (record.get("confidence") or {}).get("verification_state") == REQUIRED_VERIFICATION_STATE
    ]
    return [f"{rid}\t{quotation}" for rid, record in _by_source(witnesses, records, fleet) for quotation in failing_quotations(record, records, fleet)]


def _by_source(witnesses: list[tuple[str, dict]], records: dict, fleet: dict) -> list[tuple[str, dict]]:
    """The witnesses grouped by the files they cite, so that one cleaned
    source serves every witness that cites it (quote_verbatim keeps only the
    last two)."""
    return sorted(witnesses, key=lambda item: ([str(p) for p in witness_source_paths(item[1], records, fleet)], item[0]))


def known_findings() -> set[str]:
    lines = WITNESS_QUOTATION_FINDINGS.read_text(encoding="utf-8").splitlines()
    return {line for line in lines if line.strip()}


def sweep() -> dict[str, list[str]]:
    """Every witness quotation that does not verify, by world, whatever the
    record's verification state."""
    fleet = load_fleet_records()
    out: dict[str, list[str]] = {}
    for world in formation_world_keys():
        records = load_world_records(world)
        witnesses = [(rid, record) for rid, record in records.items() if record.get("record_type") == "doctrinal_witness"]
        rows = [
            f"{rid}\t{(record.get('confidence') or {}).get('verification_state')}\t{quotation}"
            for rid, record in _by_source(witnesses, records, fleet)
            for quotation in failing_quotations(record, records, fleet)
        ]
        if rows:
            out[world] = rows
    return out


def main(argv: list[str] | None = None) -> int:
    report = sweep()
    for world, rows in report.items():
        print(f"{world}: {len(rows)}")
        for row in rows:
            print(f"  {row}")
    print(f"{sum(map(len, report.values()))} witness quotation(s) do not verify against {REPO_ROOT.name}/cic/texts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
