"""Blind protocol enforcement: what a grader is allowed to see. world_key is
masked so a grader can't halo-effect on which world it's grading (the point
of "blind"); paraphrase_of is masked too, so nothing routes a grader (human
or model) back to a plaintext canon string it could pattern-match against
instead of judging the actual answer. A masked transcript is a plain dict,
not the richer internal objects the harness works with, so "what the grader
sees" is a hard boundary in the type, not just a convention.
"""
from typing import TypedDict


class MaskedTranscript(TypedDict):
    probe_id: str
    cell: str
    probe_text: str
    answer_text: str
    citations: list[str]
    # Per-sentence {sentence, record_ids} entries: blind-safe by
    # construction - sentences are answer_text
    # the transcript already carries, ids are the citations list's own ids
    # - and what lets grading verify a miscopied address's SENTENCE
    # against the records instead of failing it as a fabrication.
    citation_entries: list[dict]


_ALLOWED_KEYS = frozenset(MaskedTranscript.__annotations__)


def mask_for_grading(*, probe_id: str, cell: str, probe_text: str, answer_text: str, citations: list[str], citation_entries: list[dict] | None = None) -> MaskedTranscript:
    return {
        "probe_id": probe_id,
        "cell": cell,
        "probe_text": probe_text,
        "answer_text": answer_text,
        "citations": list(citations),
        "citation_entries": [dict(e) for e in (citation_entries or [])],
    }


def assert_blind(transcript: dict) -> None:
    """Raises if a transcript carries anything beyond the masked shape -
    the enforcement primitive every grader entry point calls first."""
    leaked = set(transcript) - _ALLOWED_KEYS
    if leaked:
        raise ValueError(f"blind protocol violated: transcript carries unmasked keys {sorted(leaked)}")
