"""Masked grading. Two checks this stage's gate actually needs (Build-
Blueprint.md SS5, stage 4: "catches a seeded register defect and a seeded
fabrication on the fixture world") - both take ONLY a MaskedTranscript
(masking.py), never the world_key or probe provenance.

source_boundedness is mechanical and reliable: every citation on a masked
transcript must resolve to a real source record, transitively (see
engine.m3.harness._transitive_source_ids), OR name a record in
engine.m1.canon.evidence_status_types() (a search record, definitionally
sourceless: it documents the looking itself, so citing one grounds an
honest evidence-of-absence claim). Both are real, non-fabricated
citations; a citation that resolves to neither is a finding. No model
needed, and none would make it more correct.

register is NOT mechanical in general - spec module M3 says outright that
human reading is the instrument for register (spec SS5, threshold
discipline), and the register floor rule (spec O2 statement 6: "the voice
never coins quotable lines of its own - when something deserves to be
quotable, it *is* a quote") is a judgment about voice, not a checkable
property in the general case. What's implemented here is a narrow,
honestly-labeled heuristic stand-in: it flags one recognizable
metaphor-as-definition construction ("X is the Y that...") and checks
whether the flagged text is grounded in a real, sourced quote. It is
DELIBERATELY NARROW - built and tested against exactly the one seeded
register defect this stage's gate names, not offered as a general register
grader. Real register grading is a human read (or, later, a model call once
one is configured) - this heuristic exists only so the mechanical harness
has something to run today, and it says so everywhere it appears.
"""
import re
from dataclasses import dataclass, field

from .masking import MaskedTranscript, assert_blind

_COINED_APHORISM_PATTERN = re.compile(r"\b\w+ is the \w+ that\b", re.IGNORECASE)


@dataclass(frozen=True)
class CheckResult:
    check: str
    passed: bool
    findings: list[str] = field(default_factory=list)


# The miscopy floor mirrors the compiler's own measured demo-tag floor
# (engine/m2/builders.py: DEMONSTRATION_TAG_FLOOR 0.4 ratio + 3 shared
# content words, set on a 444-sentence study) - the same two-gate
# discipline, applied to the question "does this sentence's content live
# in ANY of this world's records?".
_MISCOPY_RATIO_FLOOR = 0.4
_MISCOPY_MIN_SHARED = 3


def _sentence_verifies(sentence: str, repository_records: dict) -> list[str]:
    """Record ids whose own text contains this sentence's content at the
    miscopy floor - deterministic, no model call."""
    from engine.prose import all_text, content_words
    words = content_words(sentence)
    if not words:
        return []
    hits = []
    for rid, record in repository_records.items():
        record_words = content_words(all_text(record))
        if not record_words:
            continue
        shared = words & record_words
        ratio = len(shared) / min(len(words), len(record_words))
        if ratio >= _MISCOPY_RATIO_FLOOR and len(shared) >= _MISCOPY_MIN_SHARED:
            hits.append(rid)
    return sorted(hits)


def source_boundedness_check(
    transcript: MaskedTranscript,
    known_source_ids: set[str],
    evidence_status_ids: set[str] = frozenset(),
    repository_records: dict | None = None,
) -> CheckResult:
    assert_blind(transcript)
    citations = transcript["citations"]
    unresolved = [c for c in citations if c not in known_source_ids and c not in evidence_status_ids]
    if unresolved:
        # An unresolvable ADDRESS on a sentence whose content verifies
        # against the world's own records is a MISCOPIED ADDRESS - a
        # review finding routed to the build - not a fabrication. Five
        # battery runs characterized the split: every invented address
        # ever caught sat on an honest or otherwise-grounded sentence
        # (~1%/probe baseline); no run ever produced fabricated CONTENT.
        # The zero-fabrication bar keeps meaning invented CLAIMS: a
        # sentence whose content verifies NOWHERE still fails exactly as
        # before, as does any unresolved id whose carrying sentence can't
        # be located.
        entries = transcript.get("citation_entries") or []
        if repository_records:
            still_fabricated, miscopies = [], []
            for rid in unresolved:
                sentences = [e.get("sentence", "") for e in entries if rid in (e.get("record_ids") or [])]
                verified_against = sorted({hit for s in sentences for hit in _sentence_verifies(s, repository_records)})
                if sentences and verified_against:
                    miscopies.append((rid, verified_against))
                else:
                    still_fabricated.append(rid)
            if not still_fabricated:
                return CheckResult(
                    check="source_boundedness",
                    passed=True,
                    findings=[
                        f"probe {transcript['probe_id']}: MISCOPIED ADDRESS (review, route to build): {rid} does not "
                        f"exist, but its sentence's content verifies against {hits[:4]} - an address error on real "
                        f"content, not a fabrication"
                        for rid, hits in miscopies
                    ],
                )
            unresolved = still_fabricated
        return CheckResult(
            check="source_boundedness",
            passed=False,
            findings=[f"probe {transcript['probe_id']}: citation(s) do not resolve to any source record: {unresolved}"],
        )
    # Passing via a non-source category is still worth naming, not just
    # silently folded into the same "passed" a source-bounded citation
    # gets - a report reader should be able to see WHICH category cleared
    # each citation, not just that something did.
    findings = []
    evidence_status = sorted(set(citations) & evidence_status_ids)
    if evidence_status:
        findings.append(
            f"probe {transcript['probe_id']}: citation(s) accepted as evidence-status disclosure "
            f"(a search record grounding what was looked for and whether it was found), not source evidence: {evidence_status}"
        )
    return CheckResult(check="source_boundedness", passed=True, findings=findings)


def register_check(transcript: MaskedTranscript, known_quote_texts: set[str]) -> CheckResult:
    """ADVISORY, NEVER GATING: a live run flagged a free-composed line
    ("It is the posture that") on a probe that had passed twice, exposing
    that register statement 6 gives direction to keep things at a
    conversation level, not deliberately clever or memorable - something
    coming out memorable because it's good conversation is fine; this
    isn't meant to police what counts as memorable. Good direction that
    doesn't need to be gated.

    So the statement stays exactly where it always worked - in the compiled
    prompt, as the voice's own standing direction - and this heuristic
    keeps DETECTING (the finding still lands on the check, visible to every
    report and to the selftest's seeded-defect proof) but the check passes.
    A regex cannot tell a coined maxim from a line that is memorable
    because the conversation is good, and admission stops pretending it
    can. Real register judgment remains what this module's own header
    always said it was: a human read."""
    assert_blind(transcript)
    text = transcript["answer_text"]
    match = _COINED_APHORISM_PATTERN.search(text)
    if not match:
        return CheckResult(check="register_coined_aphorism_heuristic", passed=True)
    grounded = any(quote and quote in text for quote in known_quote_texts)
    if grounded:
        return CheckResult(check="register_coined_aphorism_heuristic", passed=True)
    return CheckResult(
        check="register_coined_aphorism_heuristic",
        passed=True,
        findings=[
            f"probe {transcript['probe_id']}: ADVISORY (direction, not a gate): "
            f"answer contains a metaphor-as-definition construction ({match.group(0)!r}) not grounded in "
            f"any sourced quote - register statement 6's direction is conversational register, recorded "
            f"here for review, never failing the probe"
        ],
    )
