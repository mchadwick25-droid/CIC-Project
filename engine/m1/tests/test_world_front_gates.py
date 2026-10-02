"""The three world_front gates (Website V2 world_front design, approved to
proceed): gate_quote_mark_fidelity (deterministic, fully
implemented and tested here, but not yet added to GATES/run_all - see its
own registration comment in gates.py for why: registering ANY new gate
changes validation/gates-report.json for every already-built world's
committed package, and rebuilding/recommitting those packages is out of
this infrastructure-only pass's scope), flag_cross_record_consistency (a
report, not registered by design - the gate battery's own standing for a
lower-precision, flag-for-review check), and check_mode3_claim_fidelity
(LLM-judged scaffolding, not registered - see its own docstring for why
it deliberately raises NotImplementedError).
"""
import pytest

from engine.m1.gates import (
    GATES,
    check_mode3_claim_fidelity,
    flag_cross_record_consistency,
    gate_quote_mark_fidelity,
)

QUOTE_VERBATIM = {
    "id": "fix.quote.test-verbatim",
    "record_type": "quote",
    "text": "We did not ask what a person had been before the water.",
    "modern_rendering": "We never asked who you were before.",
    "license": "verbatim",
}

QUOTE_PARAPHRASE_ONLY = {
    "id": "fix.quote.test-paraphrase-only",
    "record_type": "quote",
    "text": "A fragile textual tradition, only loosely attested.",
    "modern_rendering": "A shaky tradition, barely recorded.",
    "license": "paraphrase-only",
}

FLEET_QUOTES = {q["id"]: q for q in (QUOTE_VERBATIM, QUOTE_PARAPHRASE_ONLY)}


def _world_front(text: str, grounded_in=None) -> dict:
    return {
        "id": "fix.front.fixture-synthetic",
        "record_type": "world_front",
        "skim": {"tile": {"text": text, "grounded_in": grounded_in or ["fix.quote.test-verbatim"]}},
    }


def test_quote_mark_gate_is_wired_into_the_live_battery():
    """Registered once all 8 built worlds' world_front records
    existed for it to actually check (see gates.py's own comment at the
    GATES dict) - held back at the infrastructure stage only because
    registering it changes validation/gates-report.json for every
    already-built world's committed package, and that package rebuild is
    now done."""
    assert GATES["quote-mark-fidelity"] is gate_quote_mark_fidelity


def test_passes_when_the_quoted_span_matches_modern_rendering():
    good = _world_front('In our own words: "We never asked who you were before."')
    findings = gate_quote_mark_fidelity({good["id"]: good}, FLEET_QUOTES, {})
    assert findings == []


def test_catches_a_quoted_span_pulled_from_the_text_field_instead():
    bad = _world_front('In our own words: "We did not ask what a person had been before the water."')
    findings = gate_quote_mark_fidelity({bad["id"]: bad}, FLEET_QUOTES, {})
    assert len(findings) == 1
    assert "fix.quote.test-verbatim" in findings[0]
    assert "modern_rendering" in findings[0]


def test_catches_paraphrase_only_material_from_either_field():
    bad_text = _world_front('"A fragile textual tradition, only loosely attested."')
    bad_rendering = _world_front('"A shaky tradition, barely recorded."')
    for bad in (bad_text, bad_rendering):
        findings = gate_quote_mark_fidelity({bad["id"]: bad}, FLEET_QUOTES, {})
        assert len(findings) == 1
        assert "paraphrase-only" in findings[0]


def test_stays_silent_on_a_quoted_span_matching_no_known_quote():
    unmatched = _world_front('We say plainly: "Something no record here ever says."')
    findings = gate_quote_mark_fidelity({unmatched["id"]: unmatched}, FLEET_QUOTES, {})
    assert findings == []


def test_ignores_non_world_front_records_entirely():
    story = {
        "id": "fix.story.irrelevant",
        "record_type": "story",
        "text": '"We did not ask what a person had been before the water."',
    }
    findings = gate_quote_mark_fidelity({story["id"]: story}, FLEET_QUOTES, {})
    assert findings == []


def test_cross_record_consistency_flags_a_multi_grounded_unit():
    wf = _world_front("Some claim.", grounded_in=["fix.quote.test-verbatim", "fix.quote.test-paraphrase-only"])
    findings = flag_cross_record_consistency({wf["id"]: wf}, {}, {})
    kinds = {f["kind"] for f in findings}
    assert "multi-grounded-unit" in kinds
    hit = next(f for f in findings if f["kind"] == "multi-grounded-unit")
    assert hit["world_front"] == wf["id"]
    assert set(hit["grounded_in"]) == {"fix.quote.test-verbatim", "fix.quote.test-paraphrase-only"}


def test_cross_record_consistency_flags_an_associated_with_pair():
    """The exact shape of commit fbb6557: two free-text-claim records
    linked by associated-with, narrating the same underlying material."""
    story = {
        "id": "fix.story.sarah-answer-like",
        "record_type": "story",
        "text": "some narration",
        "relations": [{"type": "associated-with", "target": "fix.quote.sarah-like"}],
    }
    quote = {
        "id": "fix.quote.sarah-like",
        "record_type": "quote",
        "text": "some quotation",
        "license": "verbatim",
        "relations": [{"type": "associated-with", "target": "fix.story.sarah-answer-like"}],
    }
    records = {story["id"]: story, quote["id"]: quote}
    findings = flag_cross_record_consistency(records, {}, {})
    pair_findings = [f for f in findings if f["kind"] == "related-pair-shared-material"]
    assert len(pair_findings) == 1
    assert set((pair_findings[0]["record_a"], pair_findings[0]["record_b"])) == {story["id"], quote["id"]}


def test_cross_record_consistency_does_not_flag_analytical_associated_with():
    gravity = {
        "id": "fix.gravity.a",
        "record_type": "gravity",
        "relations": [{"type": "associated-with", "target": "fix.force.b"}],
    }
    force = {
        "id": "fix.force.b",
        "record_type": "force",
        "relations": [{"type": "associated-with", "target": "fix.gravity.a"}],
    }
    records = {gravity["id"]: gravity, force["id"]: force}
    findings = flag_cross_record_consistency(records, {}, {})
    assert findings == []


def test_check_mode3_claim_fidelity_is_explicit_unwired_scaffolding():
    """Deliberately not implemented as a string-match, and deliberately
    not silently a no-op either - calling it says exactly what is missing
    and why (see the function's own docstring / module comment for the
    two real failure cases, commits fbb6557 and 763c48d, that a
    similarity metric provably gets wrong)."""
    with pytest.raises(NotImplementedError):
        check_mode3_claim_fidelity("source field text", "adapted text")
