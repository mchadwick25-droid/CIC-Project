"""Zero-cost stand-in for a real LLM, used only when settings.mock_llm is true.

Exists so the app's mechanics - session flow, SSE token streaming, turn
selection/routing, multi-world round-taking, the frontend rendering - can be
exercised end to end without spending real API credits. Never touches the
network. Only duck-types the two methods every call site in this codebase
actually uses (`.invoke(messages)` -> object with `.content`, and
`.stream(messages)` -> iterable of chunks with `.content`), not the full
LangChain BaseChatModel interface.

Safe by construction, not by luck: every classifier and routing function in
this codebase (frame-breaker classification, relational-safety
classification, turn-type/next-speaker routing, drift/convergence
detection, lexicon/story retrieval filtering) is already written to fail
open to a safe default when its expected response format isn't found in the
LLM's reply - see each function's own docstring. The placeholder text below
deliberately contains none of those format markers (TURN_TYPE:, NEXT_SPEAKER:,
FRAME_BREAKER, DRIFT_DETECTED, CONVERGENCE_DETECTED:, N. RETRIEVE:/N. SKIP:),
so every one of those call sites safely takes its documented default path
instead of crashing or hanging - only the actual representative/facilitator
generation calls need a real, visible placeholder response.
"""

from typing import Iterator


class MockChatResult:
    """Duck-types the `.content` attribute every call site reads from an invoke()/stream() result."""

    def __init__(self, content: str):
        self.content = content


class MockChatModel:
    """Drop-in replacement for ChatAnthropic/ChatOpenAI when settings.mock_llm is true."""

    def __init__(self, **_kwargs):
        # Accepts and ignores whatever kwargs the real constructor would take
        # (model, anthropic_api_key, max_tokens, thinking, ...) so it can be
        # swapped in with the exact same call signature at every site below.
        pass

    def _mock_text(self, messages) -> str:
        # Most call sites pass a list of Message objects; batch_evaluate.py's
        # evaluate_batch passes a plain prompt string instead - handle both.
        if isinstance(messages, str):
            last_human = messages
        else:
            last_human = ""
            for m in reversed(list(messages)):
                content = getattr(m, "content", None)
                msg_type = getattr(m, "type", "")
                if content and msg_type in ("human", ""):
                    last_human = content
                    break
        preview = str(last_human)[:80].replace("\n", " ").strip()
        suffix = f' Last message seen: "{preview}"' if preview else ""
        return f"[MOCK RESPONSE - no API call made. This stands in for a real reply so the app can be tested without spending API credits.{suffix}]"

    def invoke(self, messages):
        return MockChatResult(self._mock_text(messages))

    def stream(self, messages) -> Iterator[MockChatResult]:
        text = self._mock_text(messages)
        words = text.split(" ")
        chunk_size = 4
        for i in range(0, len(words), chunk_size):
            yield MockChatResult(" ".join(words[i:i + chunk_size]) + " ")
