"""The model-provider seam (spec principle 16c): "every model call goes
through one provider seam that normalizes usage accounting; a new provider
is admitted only after its preflight proves prompt caching engages and its
real invoice reconciles." This module is that seam for Bedrock specifically
- Messages-API-shaped client only (spec SS7: "the alternative silently
zeroes cache accounting" - i.e. never call bedrock-runtime's raw
invoke_model with a hand-built body; always go through anthropic.AnthropicBedrock,
which speaks the same Messages API shape as the direct Anthropic client).

Credentials are never handled here. AnthropicBedrock (like boto3 itself)
resolves them from the standard chain - environment variables, ~/.aws/credentials,
an attached IAM role - entirely outside this process's control, by design:
this module never reads AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY itself, and
never should.
"""
from dataclasses import dataclass

import boto3
from anthropic import AnthropicBedrock

from engine.provider import guard


class ModelResolutionError(Exception):
    """Raised on zero or ambiguous (>1) matches. Spec SS7: 'refuse to guess
    model IDs - blank fails loudly.' A pattern that matches many profiles is
    exactly as unresolved as one that matches none; both are hard failures,
    never a first-match guess."""


@dataclass(frozen=True)
class NormalizedUsage:
    """One shape for usage data regardless of which Anthropic response
    object it came from (streaming's final usage vs. non-streaming's
    message.usage) - the thing spec SS10 flags as a real risk: 'streaming
    usage fields silently absent (Bedrock client rules, spec SS7).'"""

    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int

    @property
    def cache_engaged(self) -> bool:
        return self.cache_creation_input_tokens > 0 or self.cache_read_input_tokens > 0


def resolve_model_id(pattern: str, region: str) -> str:
    """Lists real inference profiles from the live account and requires
    the pattern to match EXACTLY one. Never falls back to a guessed or
    hand-typed model ID string - Bedrock inference-profile IDs are
    date/version-suffixed in a way nobody should be typing from memory.
    A control-plane listing, no model spend; the guard hears each id it
    resolves so an approved run can name its models before its first call."""
    control_plane = boto3.client("bedrock", region_name=region)
    profiles = control_plane.list_inference_profiles(maxResults=1000)["inferenceProfileSummaries"]
    matches = [
        p
        for p in profiles
        if pattern.lower() in p["inferenceProfileId"].lower() or pattern.lower() in p.get("inferenceProfileName", "").lower()
    ]
    if not matches:
        raise ModelResolutionError(f"no inference profile matched pattern {pattern!r} in region {region}")
    if len(matches) > 1:
        candidates = ", ".join(m["inferenceProfileId"] for m in matches)
        raise ModelResolutionError(f"pattern {pattern!r} matched {len(matches)} profiles, ambiguous: {candidates}")
    guard.note_model(matches[0]["inferenceProfileId"])
    return matches[0]["inferenceProfileId"]


def make_client(region: str) -> AnthropicBedrock:
    """No explicit aws_access_key/aws_secret_key passed - AnthropicBedrock
    falls through to botocore's standard credential resolution chain. The
    conversation path gets the SDK client itself; any other command gets one
    only under an approved live test (engine.provider.guard)."""
    live_test = guard.admit()
    return guard.wrap(AnthropicBedrock(aws_region=region), live_test, provider="bedrock", region=region)


def normalize_usage(usage) -> NormalizedUsage:
    """`usage` is an Anthropic Usage object from either a non-streaming
    Message or a streaming response's final usage - same accessor shape
    either way, per the Messages API (this is exactly the property that
    breaks if bedrock-runtime's raw invoke_model is used instead)."""
    return NormalizedUsage(
        input_tokens=usage.input_tokens,
        output_tokens=usage.output_tokens,
        cache_creation_input_tokens=getattr(usage, "cache_creation_input_tokens", None) or 0,
        cache_read_input_tokens=getattr(usage, "cache_read_input_tokens", None) or 0,
    )
