"""No-spend local dev server for exercising the real engine/api surface
against the real, approved Facilitator text and a real compiled world
package, with zero Bedrock calls - a fixed FakeBedrockClient standing in for
both roles, same pattern engine/api/tests/conftest.py already proves.

This is a development tool only, never imported by app.py or shipped in
engine/Dockerfile's image. GATE 3's live-turn requirement and GATE 4's real
conversation both still need an explicit per-stage human go-ahead against real
Bedrock credentials (PHASE-1-LAUNCH.md standing rule 3) - this script exists
so the frontend build itself can be clicked through before that spend, not
instead of it.

Run: uvicorn engine.api.dev_server:app --port 8000
"""
from types import SimpleNamespace

from fastapi import FastAPI

from engine.api.app import create_app
from engine.api.config import REPO_ROOT, _DEFAULT_EVENTS_DB, _DEFAULT_USAGE_DB
from engine.m1.registry import load_registry
from engine.m4.store import Store
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.log_store import UsageLogStore

_FAKE_USAGE = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=0, cache_read_input_tokens=0)

_MOCK_REPLY = (
    "[DEV SERVER - no live model was called for this reply.] This is a stand-in answer so the "
    "surface can be clicked through end to end. Ask something with \"are you an ai\" in it to see "
    "the Facilitator's system_nature turn, or something like \"kill myself\" to see the Track A "
    "safety turn."
)

_MOCK_REPLY_WITH_FIGURE = (
    "Origen taught us to read through allegoria, the plain sense and the deeper ones together "
    "[[alx.term.allegoria]]. He was not the only one who read this way, but no one argued it "
    "so far."
)


class _FakeToolUse:
    def __init__(self, name, input_):
        self.type = "tool_use"
        self.name = name
        self.input = input_


class _FakeStreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: SimpleNamespace(usage=_FAKE_USAGE))

    def __exit__(self, *exc):
        return False


def _last_user_text(messages: list[dict]) -> str:
    for message in reversed(messages):
        if message.get("role") == "user":
            content = message["content"]
            return content if isinstance(content, str) else str(content)
    return ""


class _ReactiveFakeMessages:
    """Unlike conftest.py's FakeBedrockClient (fixed canned responses,
    right for a unit test asserting one specific behavior), this inspects
    the actual participant text so a person clicking through the UI can
    reach more than one routing path without editing the script."""

    def create(self, *, model, max_tokens, tools, tool_choice, messages, system=None, timeout=None):
        name = tool_choice["name"]
        text = _last_user_text(messages).lower()
        if name == "submit_reader_output":
            out_of_scope = {"class": "system_nature"} if "are you an ai" in text or "are you a robot" in text else {"class": "none"}
            response = {
                "asks": [{"order": 1, "text": text or "(empty)"}],
                "register": "informational",
                "clarity": "clear",
                "ambiguity_options": [],
                "out_of_scope": out_of_scope,
                "modern_terms": [],
            }
        elif name == "submit_safety_classification":
            crisis_phrases = ("kill myself", "end my life", "better off dead", "suicide")
            signal = "ACUTE_DISTRESS" if any(p in text for p in crisis_phrases) else "NO_SIGNAL"
            response = {
                "signal": signal,
                "acute_level": "a1" if signal == "ACUTE_DISTRESS" else "none",
                "risk_subject": "self" if signal == "ACUTE_DISTRESS" else "not_applicable",
                "dynamic_tags": [],
                "confidence": "high",
            }
        else:
            raise AssertionError(f"unexpected tool_choice {name!r}")
        return SimpleNamespace(content=[_FakeToolUse(name, response)], usage=_FAKE_USAGE)

    def stream(self, *, model, max_tokens, system=None, messages, timeout=None):
        text = _last_user_text(messages).lower()
        reply = _MOCK_REPLY_WITH_FIGURE if "origen" in text else _MOCK_REPLY
        return _FakeStreamCtx([reply])


class ReactiveFakeBedrockClient:
    def __init__(self):
        self.messages = _ReactiveFakeMessages()


def build_dev_app() -> FastAPI:
    registry = load_registry()
    client = ReactiveFakeBedrockClient()
    return create_app(
        voice_client=client,
        voice_model_id="dev-fake-voice",
        safety_client=client,
        safety_model_id="dev-fake-safety",
        store=Store(REPO_ROOT / _DEFAULT_EVENTS_DB),
        usage_store=UsageLogStore(REPO_ROOT / _DEFAULT_USAGE_DB),
        world_loader=LazyWorldLoader(),
        registry=registry,
        default_world_key="alx",
    )


app = build_dev_app()
