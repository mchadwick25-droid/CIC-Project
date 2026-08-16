"""Test scaffolding for the runtime package.

Two jobs, both in service of one rule: THESE TESTS MUST NEVER BE A FALSE
BLOCKER. They assert on prompt assembly, which is pure Python. They must
not require the serving stack (torch, FAISS, sentence-transformers), must
not require an API key, and must not touch the network. If the machine
running them cannot satisfy even the light dependencies, the suite skips
rather than fails - a red suite must always mean "the code changed",
never "the box is missing a wheel".

1. Stub the retrieval import chain. app.graph.nodes imports app.rag at
   module scope, which pulls in FAISS and sentence-transformers. Nothing
   on the prompt-assembly path uses them, so they are replaced with empty
   modules purely to let the import succeed. Retrieval itself is stubbed
   per-test via the `prepared` fixture, not here.

2. Provide `prepared` - a fixture that calls the real
   _prepare_representative_turn with retrieval neutralised, so tests
   assert on what the model would actually receive rather than on a
   reimplementation of it.
"""
import sys
import types
from pathlib import Path

import pytest

RUNTIME_ROOT = Path(__file__).resolve().parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

# Light deps only. Absent -> skip the module, never fail it.
pytest.importorskip("langchain_core", reason="langchain-core not installed")
pytest.importorskip("pydantic_settings", reason="pydantic-settings not installed")
pytest.importorskip("langgraph", reason="langgraph not installed")

_HEAVY = [
    "faiss", "torch", "sentence_transformers", "rank_bm25",
    "langchain_community", "langchain_community.vectorstores",
    "langchain_huggingface", "langchain_anthropic", "langchain_aws",
    "langchain_openai",
]
for _name in _HEAVY:
    if _name not in sys.modules:
        _mod = types.ModuleType(_name)
        _mod.__path__ = []
        sys.modules[_name] = _mod

# Attributes the runtime imports by name at module scope.
for _mod_name, _attr in [
    ("langchain_community.vectorstores", "FAISS"),
    ("langchain_huggingface", "HuggingFaceEmbeddings"),
    ("langchain_anthropic", "ChatAnthropic"),
    ("langchain_aws", "ChatAnthropicBedrock"),
    ("langchain_openai", "ChatOpenAI"),
    ("rank_bm25", "BM25Okapi"),
    ("sentence_transformers", "CrossEncoder"),
]:
    if not hasattr(sys.modules[_mod_name], _attr):
        setattr(sys.modules[_mod_name], _attr, object)


class _NoRetrieval:
    """Retrieval returns nothing, so what remains in the prompt is the
    conversation record and the world's own static material - which is
    exactly what these tests are about."""

    def get_context_for_response(self, **_kwargs):
        return "", [], []


@pytest.fixture
def prepared(monkeypatch):
    """Run the real _prepare_representative_turn with retrieval stubbed.

    Returns a callable: prepared(messages, world_ids) -> ctx dict.
    """
    import app.graph.nodes as nodes
    from app.graph.state import ConversationState

    monkeypatch.setattr(nodes, "get_retriever", lambda _w: _NoRetrieval())
    monkeypatch.setattr(nodes, "get_story_retriever", lambda _w: _NoRetrieval())

    def _run(messages, world_ids, **state_kwargs):
        state = ConversationState(
            session_id="test-session",
            messages=messages,
            world_ids=list(world_ids),
            current_world_id=world_ids[0],
            **state_kwargs,
        )
        return nodes._prepare_representative_turn(state)

    return _run
