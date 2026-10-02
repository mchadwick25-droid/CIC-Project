"""The one place a voice call's request is shaped: the system blocks and the
messages array every generation call sends (engine.m4.generation).

Cache layout, front to back:

    system[0]   the world's compiled prompt, breakpoint 1
    messages    the session history, oldest first, breakpoint 2 on its last block
    final user  the turn directive, then the evidence block and the participant's message

The directive changes every turn. Anything placed after it in the request is
re-read at full input price every call, so it goes last, in the final user
message, where it cannot invalidate the cached history in front of it. History
is append-only (engine.api.wiring.history_from_transcript and
engine.api.table_wiring.table_history_for both emit fixed pairs), so each call
reads the previous call's cached prefix and writes only the new pair.
"""
from __future__ import annotations

DIRECTIVE_OPEN = "[Turn instructions from the engine, not from the participant]"
DIRECTIVE_CLOSE = "[End of turn instructions]"

_EPHEMERAL = {"type": "ephemeral"}


def _final_user_content(message: str, turn_directive: str | None):
    if not turn_directive:
        return message
    framed = f"{DIRECTIVE_OPEN}\n{turn_directive}\n{DIRECTIVE_CLOSE}"
    return [{"type": "text", "text": framed}, {"type": "text", "text": message}]


def _cached_history(history: list[dict]) -> list[dict]:
    """The history with a cache breakpoint on its last block. Copies; the
    caller's list and dicts are never mutated."""
    if not history:
        return []
    *earlier, last = history
    content = last["content"]
    blocks = [{"type": "text", "text": content}] if isinstance(content, str) else [dict(b) for b in content]
    blocks[-1] = {**blocks[-1], "cache_control": _EPHEMERAL}
    return [*earlier, {**last, "content": blocks}]


def build_voice_request(
    *, system_prompt: str, message: str, turn_directive: str | None = None, history: list[dict] | None = None,
) -> tuple[list[dict], list[dict]]:
    """Returns (system, messages) for client.messages.stream."""
    system = [{"type": "text", "text": system_prompt, "cache_control": _EPHEMERAL}]
    messages = [*_cached_history(history or []), {"role": "user", "content": _final_user_content(message, turn_directive)}]
    return system, messages
