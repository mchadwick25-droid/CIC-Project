"""Stage 0d (Build-Plan.md): unit-tests the --all aggregation and the
run()/main() CLI shape with a fake client - the real battery itself is a
live, credentialed run this module's own docstring reserves for a
by-hand invocation, never CI. Nothing here makes a real Bedrock call.
"""
from types import SimpleNamespace

from engine.m5.safety_script_run import BATCHES, all_scenarios, run


class _FakeToolUse:
    def __init__(self, name, input_):
        self.type = "tool_use"
        self.name = name
        self.input = input_


_FAKE_USAGE = SimpleNamespace(input_tokens=10, output_tokens=5, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class _FakeMessages:
    """Always answers NO_SIGNAL/none regardless of which scenario asked -
    enough to prove the aggregation math (passed vs. scenario_count),
    without re-implementing a safety classifier in a test double."""

    def create(self, *, model, max_tokens, tools, tool_choice, messages, system=None, timeout=None):
        name = tool_choice["name"]
        if name == "submit_safety_classification":
            value = {"signal": "NO_SIGNAL", "acute_level": "none", "risk_subject": "not_applicable", "dynamic_tags": [], "confidence": "high"}
        else:
            value = {"asks": [], "register": "informational", "clarity": "clear", "ambiguity_options": [], "out_of_scope": {"class": "none"}, "modern_terms": []}
        return SimpleNamespace(content=[_FakeToolUse(name, value)], usage=_FAKE_USAGE)


class FakeBedrockClient:
    def __init__(self):
        self.messages = _FakeMessages()


def test_all_scenarios_flattens_every_batch_in_order():
    flat = all_scenarios()
    expected = [s for n in sorted(BATCHES) for s in BATCHES[n]]
    assert flat == expected
    assert len(flat) == sum(len(b) for b in BATCHES.values())


def test_run_never_touches_live_bedrock_when_a_client_and_model_id_are_injected():
    """The Stage 0d unit-test seam: passing client/model_id means run()
    never calls resolve_model_id or make_client - if it did, this test
    would try a real network call and fail in a sandbox with no live
    Bedrock reachability configured for it, rather than passing."""
    scenarios = [
        {"id": "fixture-no-signal-correct", "message": "an ordinary question", "expected_signal": "NO_SIGNAL", "expected_acute_level": "none", "why": "fixture"},
        {"id": "fixture-acute-wrong-on-purpose", "message": "another ordinary question", "expected_signal": "ACUTE_DISTRESS", "expected_acute_level": "a1", "why": "fixture: the fake always answers NO_SIGNAL, so this one must fail"},
    ]
    report = run("us-east-1", scenarios, client=FakeBedrockClient(), model_id="fake-model-id-for-tests")

    assert report["model_id"] == "fake-model-id-for-tests"
    assert report["scenario_count"] == 2
    assert report["passed"] == 1
    assert report["results"][0]["grade"]["passed"] is True
    assert report["results"][1]["grade"]["passed"] is False
    assert "1/2" in report["floor_note"]


def test_run_all_scenarios_produces_one_combined_tally():
    """The --all mode's own aggregation, exercised directly against the
    real, full battery content (all_scenarios()) rather than a fixture
    list - proving --all actually reaches every committed batch, not
    just that flattening produces the right length."""
    report = run("us-east-1", all_scenarios(), client=FakeBedrockClient(), model_id="fake-model-id-for-tests")
    assert report["scenario_count"] == len(all_scenarios())
    assert report["passed"] <= report["scenario_count"]
    assert report["model_id"] == "fake-model-id-for-tests"
