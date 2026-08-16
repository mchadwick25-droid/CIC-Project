"""Shared Amazon Bedrock LLM construction.

Its own module, not defined inside app/graph/nodes.py, so app/rag/retriever.py
and app/rag/story_retriever.py can use it without importing nodes.py - nodes.py
already imports app.rag at module scope (LexiconRetriever, StoryRetriever), so
the reverse import would be circular.
"""
from app.config import settings


def make_bedrock_llm(model_id: str, max_tokens: int | None = None,
                      temperature: float | None = None):
    """Construct a Bedrock-backed chat model for the given model id.

    Uses langchain_aws.ChatAnthropicBedrock rather than ChatBedrockConverse -
    the former subclasses langchain_anthropic.ChatAnthropic and is backed by
    the Anthropic SDK's AnthropicBedrock client, so it keeps the Messages-API
    shape this whole app is built on: the same cache_control blocks, the same
    thinking={"type": "disabled"} kwarg, and - the reason this matters, not
    just a style preference - the same usage_metadata/input_token_details
    shape usage_logging.py already parses. ChatBedrockConverse rewrites
    caching as cachePoint blocks and, per its own source, zeroes
    cache_creation whenever it reports a per-TTL split - the exact silent-0
    failure this project already hit once (2026-07-24, streamed usage) and
    fixed by reading a second field. Do not switch to Converse without
    re-auditing usage_logging.py's field names against it first.

    Credentials come from the standard AWS chain (env vars, ~/.aws/config,
    instance/task role) - nothing AWS-specific is threaded through settings
    beyond the region and the model IDs, so this never sees a raw AWS key.
    """
    if not model_id:
        raise RuntimeError(
            "llm_provider is \"bedrock\" but the Bedrock model id is unset. "
            "Run tools/cost/bedrock_preflight.py against the real account to "
            "find the callable model/inference-profile id for this region, "
            "then set settings.bedrock_generation_model_id / "
            "bedrock_monitoring_model_id (env: BEDROCK_GENERATION_MODEL_ID / "
            "BEDROCK_MONITORING_MODEL_ID). Refusing to guess one - a wrong "
            "id is a silent 400 on every real turn, not a warning."
        )
    from langchain_aws import ChatAnthropicBedrock

    kwargs = {"model": model_id, "region_name": settings.aws_region}
    if temperature is not None:
        kwargs["temperature"] = temperature
    if max_tokens:
        kwargs["max_tokens"] = max_tokens
        kwargs["thinking"] = {"type": "disabled"}
    return ChatAnthropicBedrock(**kwargs)
