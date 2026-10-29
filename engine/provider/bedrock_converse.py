"""The provider seam for Bedrock models that do not speak the Messages API
(OpenAI, xAI, Moonshot on Bedrock), through Bedrock's Converse API.

Measurement only: no conversation path uses it, and it is handed out only
under an approved live test, exactly like engine.provider.bedrock's client.
The client it builds answers `messages.create` with the Messages-API shape
the guard counts (content blocks with `.text`, and a usage object with the
four token fields), so the cap, the printed settings and the ledger work the
same for every vendor. Prompt caching is not used here: a cache field would
be reported as zero, never guessed.

Credentials come from the standard chain, never read here.
"""
from dataclasses import dataclass

import boto3
from botocore.config import Config

from engine.provider import guard

READ_TIMEOUT_SECONDS = 600


@dataclass(frozen=True)
class ConverseUsage:
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int


@dataclass(frozen=True)
class ConverseText:
    text: str
    type: str = "text"


@dataclass(frozen=True)
class ConverseReply:
    content: list
    usage: ConverseUsage
    stop_reason: str | None
    model: str


def _blocks(content) -> list[dict]:
    if isinstance(content, str):
        return [{"text": content}]
    return [{"text": block["text"]} for block in content if block.get("type", "text") == "text"]


class _ConverseMessages:
    def __init__(self, runtime):
        self._runtime = runtime

    def create(self, *, model: str, max_tokens: int, messages: list[dict], system: str | None = None,
               additional_model_request_fields: dict | None = None) -> ConverseReply:
        request = {
            "modelId": model,
            "messages": [{"role": m["role"], "content": _blocks(m["content"])} for m in messages],
            "inferenceConfig": {"maxTokens": max_tokens},
        }
        if system:
            request["system"] = [{"text": system}]
        if additional_model_request_fields:
            request["additionalModelRequestFields"] = additional_model_request_fields
        response = self._runtime.converse(**request)
        usage = response.get("usage") or {}
        texts = [block["text"] for block in response["output"]["message"]["content"] if "text" in block]
        return ConverseReply(
            content=[ConverseText(text) for text in texts],
            usage=ConverseUsage(
                input_tokens=int(usage.get("inputTokens") or 0),
                output_tokens=int(usage.get("outputTokens") or 0),
                cache_creation_input_tokens=int(usage.get("cacheWriteInputTokens") or 0),
                cache_read_input_tokens=int(usage.get("cacheReadInputTokens") or 0),
            ),
            stop_reason=response.get("stopReason"),
            model=model,
        )


class ConverseClient:
    def __init__(self, runtime):
        self.messages = _ConverseMessages(runtime)


def make_client(region: str):
    """A Converse client under an approved live test; refused without one.
    No retries: a retried request is billed again and the cap counts each
    request once."""
    live_test = guard.admit()
    runtime = boto3.client(
        "bedrock-runtime", region_name=region,
        config=Config(read_timeout=READ_TIMEOUT_SECONDS, retries={"max_attempts": 1, "mode": "standard"}),
    )
    return guard.wrap(ConverseClient(runtime), live_test, provider="bedrock", region=region)
