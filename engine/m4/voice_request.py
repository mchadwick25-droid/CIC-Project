"""The one place a voice call's request is shaped: the system blocks and the
messages array every generation call sends (engine.m4.generation).

Cache layout, front to back:

    system[0]   the engine's shape segment (engine.shape), the same bytes for
                every world, breakpoint 1
    system[1]   the world's compiled prompt, breakpoint 2
    system[2]   the turn directive, uncached, only when the turn has one
    messages    the session history, oldest first, uncached
    final user  the evidence block and the participant's message

The directive changes every turn, so it carries no breakpoint and sits behind
both cached blocks, where it cannot invalidate them. The system channel is the
one measured to win over a competing pressure in the user turn. With
CIC_DIRECTIVE_IN_USER_MESSAGE=1 the directive instead leads the final user
message in a bracketed frame, for a staging comparison.

The history carries no breakpoint. It follows the directive, which changes
every turn, so a cache mark on it would be written every turn and never read,
at 1.25 times the plain input price.
"""
from __future__ import annotations

import os

from engine.shape import shape_text

DIRECTIVE_OPEN = "[Turn instructions from the engine, not from the participant]"
DIRECTIVE_CLOSE = "[End of turn instructions]"

_EPHEMERAL = {"type": "ephemeral"}
DIRECTIVE_IN_USER_MESSAGE_ENV = "CIC_DIRECTIVE_IN_USER_MESSAGE"


def _directive_in_user_message() -> bool:
    return os.environ.get(DIRECTIVE_IN_USER_MESSAGE_ENV) == "1"


def _final_user_content(message: str, turn_directive: str | None):
    if not turn_directive:
        return message
    framed = f"{DIRECTIVE_OPEN}\n{turn_directive}\n{DIRECTIVE_CLOSE}"
    return [{"type": "text", "text": framed}, {"type": "text", "text": message}]


def build_voice_request(
    *, system_prompt: str, message: str, turn_directive: str | None = None, history: list[dict] | None = None,
) -> tuple[list[dict], list[dict]]:
    """Returns (system, messages) for client.messages.stream."""
    system = [{"type": "text", "text": shape_text(), "cache_control": _EPHEMERAL},
              {"type": "text", "text": system_prompt, "cache_control": _EPHEMERAL}]
    in_user_message = _directive_in_user_message()
    if turn_directive and not in_user_message:
        system.append({"type": "text", "text": turn_directive})
    final_content = _final_user_content(message, turn_directive if in_user_message else None)
    messages = [*(history or []), {"role": "user", "content": final_content}]
    return system, messages
