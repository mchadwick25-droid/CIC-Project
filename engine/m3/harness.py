"""Orchestration: battery -> (masked) answer -> grade, per probe. Only this
module (plus sealed_probes.py) reads probe plaintext; only masking.py's
output ever reaches a grading check.
"""
from dataclasses import asdict, dataclass

from engine.m1 import canon

from . import grading, protocol, sealed_probes
from .generation import FixtureRecordAnswerer, NoCoverageError
from .masking import mask_for_grading


@dataclass
class ProbeResult:
    probe_id: str
    cell: str
    passed: bool
    checks: list[dict]
    error: str | None = None
    # The answer as graded (2026-08-28): the f2-p register flag arrived with
    # only the regex fragment on record - nothing for Mark's register read,
    # which is the instrument the heuristic stands in for. Grading blindness
    # is untouched (checks still run on the masked transcript only); this
    # rides AFTER grading. Callers persisting reports decide what to keep -
    # live_admission_run keeps it for FAILING probes only, a seal-conscious
    # bound (an answer can paraphrase its sealed probe; the probe text
    # itself is never persisted anywhere).
    answer_text: str | None = None


def _transitive_source_ids(records: dict[str, dict]) -> set[str]:
    """A citation is source-bounded if it names a literal `source` record,
    or if it names some other record (quote/term/gravity/...) whose OWN
    `sources[]` names one - transitively, to arbitrary depth. This is
    grounding, not citation-style: two coherent-but-different citing
    conventions coexist across the fleet (2026-08-26 finding) -
    desert/pahc's demonstrations cite a `source` record directly;
    alx/hal/syr/ijc's cite the intermediate quote/term/gravity record that
    itself cites the source. Both are real grounding chains; only the first
    hop differs. Resolving transitively fixes the false failures on the
    second convention without loosening what counts as grounded: a citation
    that doesn't trace to any real source record, by any path, still fails.
    Mark's decision (2026-08-26, over two costlier alternatives that would
    have meant re-tagging content across four worlds): fix the checker, not
    the data.

    Memoized and cycle-guarded - the corpus is a DAG in the intended case
    (source records carry no sources of their own), but this doesn't trust
    that, since a malformed record shouldn't be able to hang the harness."""
    direct = {r["id"] for r in records.values() if r.get("record_type") == "source"}
    resolved: dict[str, bool] = {}

    def resolves(record_id: str, path: frozenset[str]) -> bool:
        if record_id in direct:
            return True
        if record_id in resolved:
            return resolved[record_id]
        if record_id in path or record_id not in records:
            return False
        cited = (records[record_id].get("sources") or [])
        result = any(resolves(s["source_id"], path | {record_id}) for s in cited)
        resolved[record_id] = result
        return result

    return direct | {record_id for record_id in records if resolves(record_id, frozenset())}


def run_battery(world_key: str, records: dict[str, dict], *, answerer=None) -> list[ProbeResult]:
    """answerer defaults to FixtureRecordAnswerer(records) - the
    deterministic, no-model battery every existing caller (this module's
    own selftest included) still gets unchanged. Pass a real
    engine.m3.generation.LiveModelAnswerer instance to run the identical
    battery/masking/grading pipeline against a real generation call
    instead - the caller who builds and passes that answerer is the one
    who holds the spend authorization, not this function; run_battery
    itself makes no model-provider decision either way."""
    if answerer is None:
        answerer = FixtureRecordAnswerer(records)
    known_source_ids = _transitive_source_ids(records)
    evidence_status_ids = {r["id"] for r in records.values() if r.get("record_type") in canon.evidence_status_types()}
    known_quote_texts = {r["text"] for r in records.values() if r.get("record_type") == "quote" and r.get("text")}

    results = []
    for seal in protocol.battery():
        probe_id, cell = seal["probe_id"], seal["cell"]
        probe = sealed_probes.read_probe(probe_id)
        try:
            answer = answerer.answer(cell, probe["text"])
        except NoCoverageError as e:
            results.append(ProbeResult(probe_id=probe_id, cell=cell, passed=False, checks=[], error=str(e)))
            continue

        transcript = mask_for_grading(
            probe_id=probe_id, cell=cell, probe_text=probe["text"], answer_text=answer.text, citations=answer.citations,
            citation_entries=getattr(answer, "citation_entries", None),
        )
        checks = [
            grading.source_boundedness_check(transcript, known_source_ids, evidence_status_ids=evidence_status_ids,
                                             repository_records=records),
            grading.register_check(transcript, known_quote_texts),
        ]
        results.append(
            ProbeResult(
                probe_id=probe_id,
                cell=cell,
                passed=all(c.passed for c in checks),
                checks=[asdict(c) for c in checks],
                answer_text=answer.text,
            )
        )
    return results
