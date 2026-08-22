"""The real generation call into M4's turn loop (CiC-Program-Spec.md M4:
"one generation call... stream from first token... deterministic grounding
checks"). Sonnet-class per spec ("the voice model stays Sonnet-class: the
measured price of downgrading was halved grounded citations") - unlike M5's
Haiku-class monitoring calls, this is the actual answer the participant
reads, not a classifier.

ONE call per ordinary turn (LIVE-GENERATION-DESIGN.md, forks signed off
§9.5, 2026-08-22: Fork 1): a real streaming call for the voice's free-text
answer, which now carries its own grounding inline - the compiled prompt's
fleet preamble (§5.2) teaches every world's voice to tag each claim-
bearing sentence with the record id(s) it draws on, before the terminal
punctuation, in the same breath as the answer itself. What used to be a
second, forced-tool-use follow-up guessing which ids the answer drew on
(call_citations, deleted here) is retired outright, not merely unused -
the design's whole case for in-band tags over that shape is that guessing
citations after the fact is exactly the post-hoc grading this design
exists to stop doing. engine.m4.grounding_net.check_turn is what reads the
tags this call's own output carries; engine.m4.grounding's excerpt-match
badge check is untouched and independent (do-not-voice checking), but no
longer has a `claimed_drawn_on` list to badge-check against, because
nothing is ever claimed after the fact anymore.
"""
from dataclasses import dataclass

from anthropic import APIError, APITimeoutError

from engine.m5.failure import CallOutcome


@dataclass(frozen=True)
class StreamResult:
    text: str
    empty: bool  # true when the stream produced zero text - the literal case the crisis-append gate item names


def stream_voice_turn(client, model_id: str, *, system_prompt: str, message: str, max_tokens: int = 1024) -> CallOutcome:
    """Returns a CallOutcome whose .value is a StreamResult on success. A
    stream that completes but yields zero text is still status='ok' (it's a
    real, valid model response, just empty) - StreamResult.empty=True is
    exactly the case the caller (engine.m4.turn) must handle without ever
    conditioning crisis-resource append on it.

    system is the structured cache-eligible shape (Program-Spec SS7: "keep
    the Messages-API client shape... the static prefix is cached"), not a
    plain string - a plain string was stage 5's own gap (caught by stage 6's
    own usage instrumentation work: nothing was ever asking for a cache
    write in the first place, so every cache field was trivially zero for
    the wrong reason). A world's compiled prompt still has to clear
    Anthropic's cache-eligibility floor (~1024 tokens for Sonnet-class) to
    actually engage - a short prompt (like the fixture's) legitimately
    shows cache_engaged=False, and that is a different, honest fact from
    "caching is broken.\""""
    try:
        chunks = []
        system = [{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}]
        with client.messages.stream(
            model=model_id, max_tokens=max_tokens, system=system, messages=[{"role": "user", "content": message}]
        ) as stream:
            for text in stream.text_stream:
                chunks.append(text)
            final_usage = stream.get_final_message().usage
    except APITimeoutError:
        return CallOutcome(status="timeout")
    except APIError as e:
        return CallOutcome(status="error", value={"error": str(e)})

    full_text = "".join(chunks)
    return CallOutcome(status="ok", value=StreamResult(text=full_text, empty=(full_text.strip() == "")), raw_usage=final_usage)
