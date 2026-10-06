"""Shared test fixtures for engine/api. FakeBedrockClient follows the exact
pattern already proven in engine/m4/tests/test_turn.py (reimplemented locally
rather than importing across test trees, per the plan). The world fixture is
loaded the real way - LazyWorldLoader against the actually-committed
records/fix package via records/worlds/fix.yaml - not hand-built, so a real
compiled-prompt/repository shape is exercised, not a guess at one.
"""
from types import SimpleNamespace

import pytest

from engine.api.config import REPO_ROOT
from engine.m1.registry import load_registry
from engine.m4.store import Store
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.log_store import UsageLogStore


class _FakeToolUse:
    def __init__(self, name, input_):
        self.type = "tool_use"
        self.name = name
        self.input = input_


_FAKE_USAGE = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class _FakeStreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: SimpleNamespace(usage=_FAKE_USAGE))

    def __exit__(self, *exc):
        return False


class _FakeMessages:
    def __init__(self, *, safety_response, reader_response, stream_chunks, stream_scripts=None):
        self._responses = {"submit_safety_classification": safety_response, "submit_reader_output": reader_response}
        self._stream_chunks = stream_chunks
        # r27_enforce's own retry tests need a different raw answer on the
        # retry than on the raw attempt - a list of chunk-lists, one per
        # call, popped in order; None (every other test's own default)
        # keeps the original single-script behavior.
        self._stream_scripts = list(stream_scripts) if stream_scripts is not None else None
        # Every generation call's kwargs, recorded so a test can assert what
        # the voice was actually handed (system prefix, history, message).
        self.stream_calls = []

    def create(self, *, model, max_tokens, tools, tool_choice, messages, system=None, timeout=None):
        name = tool_choice["name"]
        # A fresh copy per call, like a real API's fresh JSON per response:
        # run_gate writes its resolved modern_terms into the reader value it
        # received, and a shared dict would leak one turn's resolution into
        # the next call's "response".
        import copy

        return SimpleNamespace(content=[_FakeToolUse(name, copy.deepcopy(self._responses[name]))], usage=_FAKE_USAGE)

    def stream(self, *, model, max_tokens, system=None, messages, timeout=None):
        self.stream_calls.append({"system": system, "messages": messages})
        chunks = self._stream_scripts.pop(0) if self._stream_scripts is not None else self._stream_chunks
        return _FakeStreamCtx(chunks)


class FakeBedrockClient:
    def __init__(self, *, safety_response, reader_response, stream_chunks=(), stream_scripts=None):
        self.messages = _FakeMessages(
            safety_response=safety_response, reader_response=reader_response,
            stream_chunks=stream_chunks, stream_scripts=stream_scripts,
        )


def reader_response(**overrides):
    base = {
        "asks": [{"order": 1, "text": "who was Jesus"}],
        "register": "informational",
        "clarity": "clear",
        "ambiguity_options": [],
        "out_of_scope": {"class": "none"},
        "modern_terms": [],
    }
    base.update(overrides)
    return base


def safety_response(signal="NO_SIGNAL", dynamic_tags=(), acute_level="none", risk_subject="not_applicable"):
    return {"signal": signal, "acute_level": acute_level, "risk_subject": risk_subject,
            "dynamic_tags": list(dynamic_tags), "confidence": "high"}


@pytest.fixture
def registry():
    return load_registry()


@pytest.fixture
def world_loader():
    return LazyWorldLoader()


@pytest.fixture
def loaded_fix_world(world_loader, registry):
    entry = registry["fix"]
    world, _timing = world_loader.load("fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"])
    return world


@pytest.fixture
def store(tmp_path):
    return Store(tmp_path / "events.db")


@pytest.fixture
def usage_store(tmp_path):
    return UsageLogStore(tmp_path / "usage.db")
