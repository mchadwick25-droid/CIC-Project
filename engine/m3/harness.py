"""Orchestration: battery -> (masked) answer -> grade, per probe. Only this
module (plus sealed_probes.py) reads probe plaintext; only masking.py's
output ever reaches a grading check.
"""
from dataclasses import asdict, dataclass

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


def run_battery(world_key: str, records: dict[str, dict]) -> list[ProbeResult]:
    answerer = FixtureRecordAnswerer(records)
    known_source_ids = {r["id"] for r in records.values() if r.get("record_type") == "source"}
    known_quote_texts = {r["text"] for r in records.values() if r.get("record_type") == "quote" and r.get("text")}

    results = []
    for seal in protocol.battery():
        probe_id, cell = seal["probe_id"], seal["cell"]
        probe = sealed_probes.read_probe(probe_id)
        try:
            answer = answerer.answer(cell)
        except NoCoverageError as e:
            results.append(ProbeResult(probe_id=probe_id, cell=cell, passed=False, checks=[], error=str(e)))
            continue

        transcript = mask_for_grading(
            probe_id=probe_id, cell=cell, probe_text=probe["text"], answer_text=answer.text, citations=answer.citations
        )
        checks = [
            grading.source_boundedness_check(transcript, known_source_ids),
            grading.register_check(transcript, known_quote_texts),
        ]
        results.append(
            ProbeResult(
                probe_id=probe_id,
                cell=cell,
                passed=all(c.passed for c in checks),
                checks=[asdict(c) for c in checks],
            )
        )
    return results
