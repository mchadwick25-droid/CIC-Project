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
from dataclasses import dataclass

from anthropic import APIError, APITimeoutError

from engine.m4.completeness import trim_to_complete_sentence
from engine.m4.voice_request import build_voice_request
from engine.m5.failure import CallOutcome


# The voice call's output ceiling. A reply reaching it is cut by the API, not
# finished by the model; stream_voice_turn below never lets that fragment out.
# Replies run 400-800 words (about 1,024 tokens at the top), so 2,048 is twice
# the longest seen and still inside the call's 90s bound at the measured
# 35-60 tokens a second. The prompt keeps replies short; this ceiling exists
# so that a reply is never stopped by the count.
VOICE_MAX_TOKENS = 2048


@dataclass(frozen=True)
class StreamResult:
    text: str
    empty: bool  # true when the stream produced zero text - the literal case the crisis-append gate item names
    truncated: bool = False  # the API stopped at max_tokens; `text` is cut back to the last finished sentence
    dropped: str = ""  # the unfinished fragment removed from the end of `text`


def stream_voice_turn(
    client, model_id: str, *, system_prompt: str, message: str, turn_directive: str | None = None,
    history: list[dict] | None = None, max_tokens: int = VOICE_MAX_TOKENS, timeout: float = 90.0,
) -> CallOutcome:
    """Returns a CallOutcome whose .value is a StreamResult on success. A
    stream that completes but yields zero text is still status='ok' (it's a
    real, valid model response, just empty) - StreamResult.empty=True is
    exactly the case the caller (engine.m4.turn) must handle without ever
    conditioning crisis-resource append on it.

    The request is shaped by engine.m4.voice_request.build_voice_request: the
    world's compiled prompt is the cached system prefix, the session history
    carries the second cache breakpoint, and the per-turn directive rides at
    the front of the final user message. A world's compiled prompt still has
    to clear Anthropic's cache-eligibility floor (~1024 tokens for
    Sonnet-class) to engage - a short prompt (like the fixture's) legitimately
    shows cache_engaged=False, which is a different fact from "caching is
    broken."
    """
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
            final_message = stream.get_final_message()
            final_usage = final_message.usage
            stop_reason = getattr(final_message, "stop_reason", None)
    except APITimeoutError:
        return CallOutcome(status="timeout")
    except APIError as e:
        return CallOutcome(status="error", value={"error": str(e)})

    full_text = "".join(chunks)
    # stop_reason == "max_tokens" means the count ran out, not the model: the
    # text ends wherever it stood. Cut it back to the last finished sentence
    # so no caller grades, shows or stores a fragment as a reply.
    truncated = stop_reason == "max_tokens"
    dropped = ""
    if truncated:
        full_text, dropped = trim_to_complete_sentence(full_text)
    return CallOutcome(
        status="ok",
        value=StreamResult(text=full_text, empty=(full_text.strip() == ""), truncated=truncated, dropped=dropped),
        raw_usage=final_usage,
    )
