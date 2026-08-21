"""No live AWS calls here - resolve_model_id is tested against a mocked
control-plane response, normalize_usage against a fake usage object. The
live path (an actual Bedrock round trip) is what engine/provider/preflight.py
exercises, by hand, against a real account - not something CI can run
(spec principle 13: real cost; also needs live credentials CI doesn't have).
"""
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from engine.provider.bedrock import ModelResolutionError, normalize_usage, resolve_model_id

PROFILES = [
    {"inferenceProfileId": "us.anthropic.claude-sonnet-4-5-20250929-v1:0", "inferenceProfileName": "US Claude Sonnet 4.5"},
    {"inferenceProfileId": "us.anthropic.claude-haiku-4-5-20251001-v1:0", "inferenceProfileName": "US Claude Haiku 4.5"},
    {"inferenceProfileId": "us.anthropic.claude-opus-4-1-20250805-v1:0", "inferenceProfileName": "US Claude Opus 4.1"},
]


def _mock_control_plane():
    client = MagicMock()
    client.list_inference_profiles.return_value = {"inferenceProfileSummaries": PROFILES}
    return client


def test_resolve_model_id_exact_single_match():
    with patch("engine.provider.bedrock.boto3.client", return_value=_mock_control_plane()):
        assert resolve_model_id("sonnet-4-5", "us-east-1") == "us.anthropic.claude-sonnet-4-5-20250929-v1:0"


def test_resolve_model_id_no_match_raises_loudly():
    with patch("engine.provider.bedrock.boto3.client", return_value=_mock_control_plane()):
        with pytest.raises(ModelResolutionError):
            resolve_model_id("gpt-4", "us-east-1")


def test_resolve_model_id_ambiguous_match_raises_loudly():
    with patch("engine.provider.bedrock.boto3.client", return_value=_mock_control_plane()):
        with pytest.raises(ModelResolutionError):
            resolve_model_id("claude", "us-east-1")  # matches all three - never silently pick one


def test_normalize_usage_reads_cache_fields():
    usage = SimpleNamespace(input_tokens=10, output_tokens=5, cache_creation_input_tokens=1600, cache_read_input_tokens=0)
    n = normalize_usage(usage)
    assert (n.input_tokens, n.output_tokens, n.cache_creation_input_tokens, n.cache_read_input_tokens) == (10, 5, 1600, 0)
    assert n.cache_engaged is True


def test_normalize_usage_tolerates_missing_cache_fields():
    """The exact silent-absence risk spec SS10 names: a usage shape that
    simply lacks cache_* attributes must normalize to 0, not crash and not
    silently read as 'cache engaged.'"""
    usage = SimpleNamespace(input_tokens=10, output_tokens=5)
    n = normalize_usage(usage)
    assert (n.cache_creation_input_tokens, n.cache_read_input_tokens) == (0, 0)
    assert n.cache_engaged is False
