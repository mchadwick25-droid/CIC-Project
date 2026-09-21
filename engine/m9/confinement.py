"""The confinement battery (Library Access Gate D3 SS1.4) - seven checks,
`locus-within-work` held for a later increment once CM-4 (`locus_ids`)
exists on real data. Each check is `(records, shelf) -> list[str]`, the
same `(records, fleet, registry) -> list[str]` shape `engine/m1/gates.py`
already uses, minus the args this module has no use for. An empty list
means that check passed clean. Names here are the `gate:` ids
fixtures/seeded_defects.yaml uses, matching gates.py's own convention so
the selftest can map one to the other with no separate lookup table.

Nothing in engine/m9/ imports engine/m1/gates.py's internals or is
imported by it - gates.py keeps its own "imports nothing from cic/engine/"
convention intact (D3 SS1.3). `_EDITION_PATH` below is gates.py's own
regex, duplicated rather than imported for the same reason gates.py
itself duplicates cross-boundary logic instead of reaching across a
package line for one constant (see that module's own comment on
_TEXTS_DIR/_EDITION_PATH).
"""
from __future__ import annotations

import re

from engine.m4.grounding_net import _normalize

from .shelf import Shelf

_EDITION_PATH = re.compile(r"cic/texts/([\w\-]+\.(?:txt|xml))")

_UNRESOLVED_KINDS = (None, "unvendored", "absence")


def _emic_citable(records: dict) -> list[tuple[str, dict]]:
    return [
        (rid, rec)
        for rid, rec in records.items()
        if rec.get("register") == "emic" and rec.get("sources")
    ]


def _resolve_row(source_rec: dict, shelf: Shelf) -> dict | None:
    """The row a vendored source record's shelf_row names, or None if it
    doesn't resolve (no kind, unvendored, absence, missing shelf_row, or a
    shelf_row not on this world's shelf) - every one of those is a distinct
    problem some OTHER check already names (source-kind, shelf-row), so
    callers here skip rather than double-report."""
    if source_rec.get("kind") in _UNRESOLVED_KINDS:
        return None
    row_id = source_rec.get("shelf_row")
    if not row_id:
        return None
    return shelf.rows.get(row_id)


def gate_source_kind(records: dict, shelf: Shelf) -> list[str]:
    """kind (schema, D3 SS5) must agree with edition: vendored <=> edition
    names a real cic/texts/ file (anywhere in the library - shelf-row is
    the separate, stronger "and it's on THIS world's shelf" check);
    unvendored <=> it names none; absence <=> it names a real file and
    carries absence_probes. A missing kind is its own finding."""
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "source":
            continue
        kind = rec.get("kind")
        edition = str(rec.get("edition") or "")
        m = _EDITION_PATH.search(edition)
        names_real_file = bool(m and m.group(1) in shelf.vendored_files)

        if kind is None:
            findings.append(f"{rid}: no kind set (vendored | unvendored | absence)")
            continue
        if kind == "vendored" and not names_real_file:
            findings.append(f"{rid}: kind is 'vendored' but edition does not name a real cic/texts/ file")
        elif kind == "unvendored" and (m is not None):
            findings.append(f"{rid}: kind is 'unvendored' but edition names cic/texts/{m.group(1)}")
        elif kind == "absence":
            if not names_real_file:
                findings.append(f"{rid}: kind is 'absence' but edition does not name a real cic/texts/ file")
            if not rec.get("absence_probes"):
                findings.append(f"{rid}: kind is 'absence' but absence_probes is empty")
        elif kind not in ("vendored", "unvendored", "absence"):
            findings.append(f"{rid}: kind {kind!r} is not one of vendored | unvendored | absence")
    return findings


def gate_shelf_row(records: dict, shelf: Shelf) -> list[str]:
    """Every kind: vendored source record carries shelf_row, and it names
    a row on THIS world's own shelf whose source_file is the file the
    record's own edition names."""
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "source" or rec.get("kind") != "vendored":
            continue
        row_id = rec.get("shelf_row")
        if not row_id:
            findings.append(f"{rid}: kind is 'vendored' but shelf_row is not set")
            continue
        row = shelf.rows.get(row_id)
        if row is None:
            findings.append(f"{rid}: shelf_row {row_id!r} does not resolve to a row on this world's shelf")
            continue
        edition = str(rec.get("edition") or "")
        m = _EDITION_PATH.search(edition)
        named_file = m.group(1) if m else None
        if named_file and row.get("source_file") != named_file:
            findings.append(
                f"{rid}: shelf_row {row_id!r} is the row for {row.get('source_file')!r}, "
                f"but edition names cic/texts/{named_file}"
            )
    return findings


def gate_emic_vendored_only(records: dict, shelf: Shelf) -> list[str]:
    """No emic citable record's sources[] names a kind: unvendored or
    kind: absence source record - Q4/Q5 applied."""
    findings = []
    for rid, rec in _emic_citable(records):
        for entry in rec.get("sources") or []:
            source_id = entry.get("source_id")
            source_rec = records.get(source_id)
            if source_rec is None or source_rec.get("record_type") != "source":
                continue  # dangling/non-source reference - the referential gate's own job
            kind = source_rec.get("kind")
            if kind in ("unvendored", "absence"):
                findings.append(f"{rid}: cites {source_id!r}, whose kind is {kind!r} - an emic record may not ground itself in it")
    return findings


def gate_absence_probe(records: dict, shelf: Shelf) -> list[str]:
    """For every kind: absence record, none of its absence_probes strings
    window-matches in the file its own edition names (possibly off this
    world's shelf - Q5's narrow, logged build-time exception; loader.py
    is what actually reads the file, this only checks the text it was
    handed)."""
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "source" or rec.get("kind") != "absence":
            continue
        edition = str(rec.get("edition") or "")
        m = _EDITION_PATH.search(edition)
        if not m:
            continue  # source-kind already reports the missing/bad edition path
        filename = m.group(1)
        text = shelf.units.get(filename)
        if text is None:
            findings.append(f"{rid}: edition names cic/texts/{filename}, but its text was not available to check probes against")
            continue
        haystack = _normalize(text)
        for probe in rec.get("absence_probes") or []:
            words = _normalize(probe).split()
            if not words:
                continue
            window = " ".join(words)
            if window in haystack:
                findings.append(f"{rid}: absence_probes entry {probe!r} DOES window-match in cic/texts/{filename} - the claimed absence is false")
    return findings


def gate_verbatim_in_shelf(records: dict, shelf: Shelf) -> list[str]:
    """Every emic quote with license: verbatim window-matches, byte for
    byte (after _normalize), inside the world's own shelf files - any
    role, file grain (Direction B's bet, Q7-B measured it at 98.2% on
    real data)."""
    findings = []
    haystacks = [shelf.units[f] for f in shelf.files if f in shelf.units]
    normalized_haystacks = [_normalize(h) for h in haystacks]
    for rid, rec in records.items():
        if rec.get("record_type") != "quote" or rec.get("register") != "emic" or rec.get("license") != "verbatim":
            continue
        text = str(rec.get("text") or "")
        words = _normalize(text).split()
        if not words:
            findings.append(f"{rid}: license is 'verbatim' but text is empty")
            continue
        window_words = 6
        windows = (
            [" ".join(words)]
            if len(words) <= window_words
            else [" ".join(words[i : i + window_words]) for i in range(len(words) - window_words + 1)]
        )
        if not any(w in h for h in normalized_haystacks for w in windows):
            findings.append(f"{rid}: license is 'verbatim' but its text does not window-match in any file on this world's shelf")
    return findings


def gate_voicing_pair(records: dict, shelf: Shelf) -> list[str]:
    """For every emic citable record, each cited source record that
    resolves to a row (kind: vendored, a real shelf_row) is either
    role: tradition, or a non-tradition row that clears BOTH gates the
    R-1/R-2/R-3 ruling requires: its voice_of forms a pair with this
    world's own census_id ruled mutual-awareness in PAIRS.yaml, AND the
    row's own documented_exchange is 'confirmed' - a pair makes voicing
    possible, never automatic (CM-8). A source record with no resolvable
    row (unvendored, absence, or a shelf_row that doesn't resolve) is
    skipped here - shelf-row/source-kind already report it, and reporting
    it a second time under this name would double-count the same defect."""
    findings = []
    for rid, rec in _emic_citable(records):
        for entry in rec.get("sources") or []:
            source_id = entry.get("source_id")
            source_rec = records.get(source_id)
            if source_rec is None or source_rec.get("record_type") != "source":
                continue
            row = _resolve_row(source_rec, shelf)
            if row is None:
                continue
            if row.get("role") == "tradition":
                continue
            voice_of = row.get("voice_of")
            if not voice_of:
                findings.append(f"{rid}: cites {source_id!r} (row has role {row.get('role')!r}) but the row carries no voice_of")
                continue
            pair = shelf.pairs.get(frozenset({shelf.census_id, voice_of}))
            if pair is None:
                findings.append(f"{rid}: cites {source_id!r}, whose voice_of {voice_of!r} has no PAIRS.yaml ruling with {shelf.census_id!r}")
                continue
            relation = pair.get("relation")
            if relation != "mutual-awareness":
                findings.append(f"{rid}: cites {source_id!r}; the ({shelf.census_id}, {voice_of}) pair is ruled {relation!r}, not mutual-awareness")
                continue
            if pair.get("confidence") == "needs-ruling":
                findings.append(f"{rid}: cites {source_id!r}; the ({shelf.census_id}, {voice_of}) pair's mutual-awareness ruling is still needs-ruling")
                continue
            documented_exchange = row.get("documented_exchange")
            if documented_exchange != "confirmed":
                findings.append(
                    f"{rid}: cites {source_id!r}; the pair is mutual-awareness but the row's own "
                    f"documented_exchange is {documented_exchange!r}, not confirmed"
                )
    return findings


def gate_shelf_confidence(records: dict, shelf: Shelf) -> list[str]:
    """No emic citable record resolves to a row with confidence:
    needs-ruling (provisional passes and is a report-only observation,
    not a finding here)."""
    findings = []
    for rid, rec in _emic_citable(records):
        for entry in rec.get("sources") or []:
            source_id = entry.get("source_id")
            source_rec = records.get(source_id)
            if source_rec is None or source_rec.get("record_type") != "source":
                continue
            row = _resolve_row(source_rec, shelf)
            if row is None:
                continue
            if row.get("confidence") == "needs-ruling":
                findings.append(f"{rid}: cites {source_id!r}, whose shelf row's confidence is needs-ruling")
    return findings


CHECKS = {
    "source-kind": gate_source_kind,
    "shelf-row": gate_shelf_row,
    "emic-vendored-only": gate_emic_vendored_only,
    "absence-probe": gate_absence_probe,
    "verbatim-in-shelf": gate_verbatim_in_shelf,
    "voicing-pair": gate_voicing_pair,
    "shelf-confidence": gate_shelf_confidence,
}


def run_all(records: dict, shelf: Shelf) -> dict[str, list[str]]:
    return {name: fn(records, shelf) for name, fn in CHECKS.items()}
