"""The real generation call into M4's turn loop (CiC-Program-Spec.md M4:
"one generation call... stream from first token... deterministic grounding
checks"). Sonnet-class per spec ("the voice model stays Sonnet-class: the
measured price of downgrading was halved grounded citations") - unlike M5's
Haiku-class monitoring calls, this is the actual answer the participant
reads, not a classifier.

ONE call per ordinary turn (LIVE-GENERATION-DESIGN.md §9.5, Fork 1): a real
streaming call for the voice's free-text
answer, which now carries its own grounding inline - the compiled prompt's
fleet preamble (§5.2) teaches every world's voice to tag each claim-
bearing sentence with the record id(s) it draws on, before the terminal
punctuation, in the same breath as the answer itself. What used to be a
second, forced-tool-use follow-up guessing which ids the answer drew on
(call_citations, deleted here) is retired outright, not merely unused -
the design's whole case for in-band tags over that shape is that guessing
citations after the fact is exactly the post-hoc grading this design
exists to stop doing. engine.m4.grounding_net.check_turn is what reads the
tags this call's own output carries.
"""
import threading
from dataclasses import dataclass
from typing import Callable

from anthropic import APIError, APITimeoutError

try:
    import httpx2 as _http
except ImportError:
    import httpx as _http

# A connection that closes while a reply is streaming raises the HTTP
# library's own transport error, which the SDK does not wrap in APIError.
_TRANSPORT_ERRORS = (_http.TransportError,)

from engine.m4.voice_request import build_voice_request
from engine.m5.failure import CallOutcome


# At most this many voice calls run at once in one process. A slow or
# throttled Bedrock otherwise holds a worker thread per waiting call until
# the server's whole thread pool is taken and every request stalls. A call
# past the limit fails at once, through the same path as a Bedrock error.
# The safety and reader calls never pass through here, so the gate still
# runs on every message.
MAX_CONCURRENT_VOICE_CALLS = 16
_voice_slots = threading.BoundedSemaphore(MAX_CONCURRENT_VOICE_CALLS)
VOICE_CAPACITY_FULL = "voice capacity full"


@dataclass(frozen=True)
class StreamResult:
    text: str
    empty: bool  # true when the stream produced zero text - the literal case the crisis-append gate item names


def stream_voice_turn(
    client, model_id: str, *, system_prompt: str, message: str, turn_directive: str | None = None,
    history: list[dict] | None = None, max_tokens: int = 2048, timeout: float = 90.0,
    on_text: Callable[[str], None] | None = None,
) -> CallOutcome:
    """Returns a CallOutcome whose .value is a StreamResult on success. A
    stream that completes but yields zero text is still status='ok' (it's a
    real, valid model response, just empty) - StreamResult.empty=True is
    exactly the case the caller (engine.m4.turn) must handle without ever
    conditioning crisis-resource append on it.

    The request is shaped by engine.m4.voice_request.build_voice_request: the
    engine's shape segment and then the world's compiled prompt are the cached
    system prefix, the per-turn directive follows them as an uncached system block, and the
    session history carries the last cache breakpoint. A world's compiled prompt still has
    to clear Anthropic's cache-eligibility floor (~1024 tokens for
    Sonnet-class) to engage - a short prompt (like the fixture's) legitimately
    shows cache_engaged=False, which is a different fact from "caching is
    broken."

    on_text receives each chunk of raw model text as it arrives, so a caller
    can show a draft while the reply is still being written. It only observes:
    the returned text and every check on it are unchanged.
    """
    if not _voice_slots.acquire(blocking=False):
        return CallOutcome(status="error", value={"error": VOICE_CAPACITY_FULL})
    try:
        return _stream(
            client, model_id, system_prompt=system_prompt, message=message, turn_directive=turn_directive,
            history=history, max_tokens=max_tokens, timeout=timeout, on_text=on_text,
        )
    finally:
        _voice_slots.release()


def _stream(
    client, model_id: str, *, system_prompt: str, message: str, turn_directive: str | None,
    history: list[dict] | None, max_tokens: int, timeout: float, on_text: Callable[[str], None] | None,
) -> CallOutcome:
    try:
        chunks = []
        system, messages = build_voice_request(
            system_prompt=system_prompt, message=message, turn_directive=turn_directive, history=history,
        )
        # timeout: this is the one call that holds a participant's HTTP
        # request open. Unlike the cheap gate calls (bounded at 4s), it
        # would otherwise have no bound (SDK default: 600s read). 90s is
        # ~3x the worst measured real turn (engine/m8 reports: 10-30s of
        # stream); it exists to cut hung streams loose, never to cut real
        # answers short. The APITimeoutError catch below already handles
        # the outcome - the bound just makes it reachable.
        with client.messages.stream(
            model=model_id, max_tokens=max_tokens, system=system, messages=messages, timeout=timeout,
        ) as stream:
            for text in stream.text_stream:
                chunks.append(text)
                if on_text is not None:
                    on_text(text)
            final_usage = stream.get_final_message().usage
    except APITimeoutError:
        return CallOutcome(status="timeout")
    except APIError as e:
        return CallOutcome(status="error", value={"error": str(e)})
    except _TRANSPORT_ERRORS as e:
        return CallOutcome(status="error", value={"error": f"connection dropped while streaming: {e}"})

    full_text = "".join(chunks)
    return CallOutcome(status="ok", value=StreamResult(text=full_text, empty=(full_text.strip() == "")), raw_usage=final_usage)
