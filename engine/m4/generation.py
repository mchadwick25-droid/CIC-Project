"""The real generation call into M4's turn loop (CiC-Program-Spec.md M4:
"one generation call... stream from first token... deterministic grounding
checks"). Sonnet-class per spec ("the voice model stays Sonnet-class: the
measured price of downgrading was halved grounded citations") - unlike M5's
Haiku-class monitoring calls, this is the actual answer the participant
reads, not a classifier.

Two calls per ordinary turn: (1) a real streaming call for the voice's
free-text answer - token deltas, not tool-use, since the answer itself is
prose the participant reads as it streams (Artifact-5 SS2: "streaming from
first token - no buffering, spec principle 1"); (2) a small forced-tool-use
follow-up naming which repository record ids the answer actually drew on,
which engine.m4.grounding then mechanically checks against the streamed
text before any citation badge is shown (Artifact-5 SS2: "deterministic
grounding checks run before citations is emitted - they gate decoration,
never the text").
"""
from dataclasses import dataclass

from anthropic import APIError, APITimeoutError

from engine.m5.failure import CallOutcome

_CITATIONS_TOOL = {
    "name": "submit_citations",
    "description": "Name which of the provided record ids this answer actually drew on vs. merely had available.",
    "input_schema": {
        "type": "object",
        "properties": {
            "drawn_on": {"type": "array", "items": {"type": "string"}},
            "consulted": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["drawn_on", "consulted"],
    },
}


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


def call_citations(client, model_id: str, *, answer_text: str, available_record_ids: list[str], timeout: float = 4.0) -> CallOutcome:
    if not answer_text.strip():
        # Nothing was said - nothing to cite. Not a call worth making, and
        # not a failure: an empty answer has no citations by construction.
        return CallOutcome(status="ok", value={"drawn_on": [], "consulted": []})

    ids_list = "\n".join(f"- {rid}" for rid in available_record_ids)
    user_content = (
        f"The answer you just gave:\n{answer_text}\n\n"
        f"Record ids that were available to draw on:\n{ids_list}\n\n"
        "Which did you actually draw on (drawn_on) vs. have available but didn't really use (consulted)?"
    )
    try:
        response = client.messages.create(
            model=model_id,
            max_tokens=512,
            tools=[_CITATIONS_TOOL],
            tool_choice={"type": "tool", "name": _CITATIONS_TOOL["name"]},
            messages=[{"role": "user", "content": user_content}],
            timeout=timeout,
        )
    except APITimeoutError:
        return CallOutcome(status="timeout")
    except APIError as e:
        return CallOutcome(status="error", value={"error": str(e)})

    tool_uses = [b for b in response.content if b.type == "tool_use" and b.name == _CITATIONS_TOOL["name"]]
    if not tool_uses:
        return CallOutcome(status="parse_failure", value={"raw": [b.model_dump() for b in response.content]})
    return CallOutcome(status="ok", value=tool_uses[0].input, raw_usage=getattr(response, "usage", None))
