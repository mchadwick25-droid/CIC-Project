"""Masked grading. Two checks this stage's gate actually needs (Build-
Blueprint.md SS5, stage 4: "catches a seeded register defect and a seeded
fabrication on the fixture world") - both take ONLY a MaskedTranscript
(masking.py), never the world_key or probe provenance.

source_boundedness is mechanical and reliable: every citation on a masked
transcript must resolve to a real source record, transitively (see
engine.m3.harness._transitive_source_ids), OR name a record in
engine.m1.canon.voice_scaffold_types() - the fleet's second, distinct
citation category (the voice's own sanctioned identity/craft framing,
spec principle 14, never itself historical evidence and never expected to
be). Both are real, non-fabricated citations; only a citation that
resolves to neither is a finding. No model needed, and none would make it
more correct.

register is NOT mechanical in general - spec module M3 says outright that
"Mark's reading is the instrument for register" (spec SS5, threshold
discipline), and the register floor rule (spec O2 statement 6: "the voice
never coins quotable lines of its own - when something deserves to be
quotable, it *is* a quote") is a judgment about voice, not a checkable
property in the general case. What's implemented here is a narrow,
honestly-labeled heuristic stand-in: it flags one recognizable
metaphor-as-definition construction ("X is the Y that...") and checks
whether the flagged text is grounded in a real, sourced quote. It is
DELIBERATELY NARROW - built and tested against exactly the one seeded
register defect this stage's gate names, not offered as a general register
grader. Real register grading is Mark's read (or, later, a model call once
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


def source_boundedness_check(
    transcript: MaskedTranscript, known_source_ids: set[str], voice_scaffold_ids: set[str] = frozenset()
) -> CheckResult:
    assert_blind(transcript)
    citations = transcript["citations"]
    unresolved = [c for c in citations if c not in known_source_ids and c not in voice_scaffold_ids]
    if unresolved:
        return CheckResult(
            check="source_boundedness",
            passed=False,
            findings=[f"probe {transcript['probe_id']}: citation(s) do not resolve to any source record: {unresolved}"],
        )
    # Passing via the scaffold category is still worth naming, not just
    # silently folded into the same "passed" a source-bounded citation
    # gets - a report reader should be able to see WHICH category cleared
    # each citation, not just that something did.
    scaffolded = sorted(set(citations) & voice_scaffold_ids)
    findings = (
        [f"probe {transcript['probe_id']}: citation(s) accepted as voice-scaffold self-attribution, not source evidence: {scaffolded}"]
        if scaffolded
        else []
    )
    return CheckResult(check="source_boundedness", passed=True, findings=findings)


def register_check(transcript: MaskedTranscript, known_quote_texts: set[str]) -> CheckResult:
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
        passed=False,
        findings=[
            f"probe {transcript['probe_id']}: answer contains a metaphor-as-definition construction "
            f"({match.group(0)!r}) not grounded in any sourced quote - register statement 6 requires "
            f"anything quotable to *be* a quote, named and sourced, never coined free"
        ],
    )
