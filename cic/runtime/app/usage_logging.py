"""Lightweight, purely-additive token-usage logging for every real LLM call
in a representative-turn's pipeline: main response generation, the
blocking safety/routing classifiers, and the RAG retrieval relevance
filters.

Added 2026-07-24 in response to a real pilot-test cost finding
($0.42/question, ~$8-9/hour) with zero token-usage instrumentation
anywhere in the app to diagnose it from - confirmed via grep for
usage_metadata/input_tokens/cache_read/cache_creation across app/ before
this file existed: no hits. This closes that gap.

Deliberately its own standalone module with no dependency on
app.graph.nodes. Several of the call sites that need this -
app.graph.epistemology_bridge, app.graph.modern_term_bridge,
app.graph.closing_sequence, app.rag.batch_evaluate - already import
from app.graph.nodes for other things (get_monitoring_llm,
CLASSIFIER_MAX_TOKENS), but app.graph.nodes itself imports from app.rag
(LexiconRetriever, StoryRetriever), so a reverse import from
app.rag.batch_evaluate back into app.graph.nodes would be circular.
Living here avoids that entirely.

Observation only: never reads a value that would change generation
behavior, never raises past its own log call, and does not touch prompts,
model choice, or any existing code path's output.
"""
import logging

logger = logging.getLogger("cic.llm_usage")
logger.setLevel(logging.INFO)
if not logger.handlers:
    # The app has no logging.basicConfig/handler setup anywhere (checked
    # before adding this file - grep across app/ for basicConfig turned up
    # nothing), so the root logger's default level (WARNING) would
    # otherwise silently swallow every INFO line this module emits,
    # regardless of the logger.setLevel(INFO) call above - a logger's own
    # level only decides whether it PASSES a record to its handlers, not
    # whether anything downstream actually prints it. Attaching a
    # dedicated handler directly to this named logger, scoped to just this
    # logger (not logging.basicConfig, which would reconfigure the root
    # logger and could interfere with however the app is run - uvicorn's
    # own reload workers included), guarantees these lines are actually
    # emitted regardless of what the rest of the app's logging setup does
    # or doesn't do.
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    logger.addHandler(_handler)


def log_llm_usage(
    label: str,
    response,
    model: str,
    *,
    request_id: str | None = None,
    session_id: str | None = None,
) -> None:
    """
    Log token usage for one completed real LLM call.

    label: which call this was - e.g. "main_response", "frame_breaker",
        "relational_safety", "epistemology_bridge", "modern_term_bridge",
        "wind_down", "negative_condition_lexicon",
        "negative_condition_story". The retrieval labels were
        "retrieval_filter_lexicon"/"_story" until S3.4 replaced the batched
        relevance vote with the local cross-encoder; the committed cost
        baseline predates that change and still carries the old labels, so
        a log line bearing one is from before 2026-08-09 by definition.
    response: the LangChain message object returned by .invoke() (an
        AIMessage), or - for a streamed call - the accumulated chunk built
        by summing every AIMessageChunk yielded during the stream (see
        nodes.py's streaming call sites: LangChain's AIMessageChunk.__add__
        merges usage_metadata across chunks, which is how a streamed call
        gets an accurate final count without a second API call).
    model: the model string actually used for this specific call (e.g.
        settings.llm_model for representative/facilitator generation, or
        the literal "claude-haiku-4-5-20251001" get_monitoring_llm and the
        RAG filter_llm constructors currently hardcode) - logged alongside
        the counts because sonnet and haiku are priced very differently
        and a bare token count can't be converted to a dollar figure
        without knowing which model it was billed against.
    request_id / session_id: whatever identifiers are already flowing
        through this call site, passed straight through unchanged, so
        every line produced by one conversation turn can be grouped back
        together after the fact. Both optional - not every call site in
        this codebase has both threaded through it yet, and this module
        does not require adding new plumbing just to populate them.

    Reads usage from two different places on the response object, because
    the fields this task needs aren't all in the same spot:
    - response.usage_metadata - LangChain's standardized, cross-provider
      shape - for input_tokens/output_tokens. Present on both a plain
      .invoke() result and a properly chunk-summed streamed result.
    - response.response_metadata["usage"] - the raw Anthropic API usage
      block, passed through by langchain-anthropic largely unmodified -
      for cache_creation_input_tokens/cache_read_input_tokens
      specifically. These two fields are Anthropic-specific and are NOT
      part of LangChain's standardized usage_metadata shape, which is
      exactly why both places need to be read rather than just one.

    Real bug found and fixed 2026-07-24: response.response_metadata["usage"]
    comes back empty for a streamed call (.stream() + summed
    AIMessageChunks) - confirmed with an isolated diagnostic
    (diag_stream_cache.py) showing a plain .invoke() populates it
    correctly but the app's actual live streaming call path
    (stream_representative_turn/_generate_once in nodes.py - what every
    real user turn goes through) never does, so this function was
    silently logging cache_creation/cache_read as 0 for every real
    production call regardless of whether caching actually happened.
    The real numbers are present in that case, just under a different,
    LangChain-standardized key: usage_metadata["input_token_details"]
    ("cache_creation"/"cache_read", not the longer Anthropic-native field
    names used in the raw usage block). Falls back there only when the
    raw Anthropic block came back empty, so the already-correct
    non-streamed path above is untouched.

    Never raises past this function - a logging failure must never be
    allowed to take down the real call it is only trying to observe.
    Missing or absent fields are logged as 0 rather than the line being
    silently skipped, so a real instrumentation gap at some call site
    shows up as a visible 0 in the log rather than as nothing at all.
    """
    try:
        usage_metadata = getattr(response, "usage_metadata", None) or {}
        input_tokens = usage_metadata.get("input_tokens", 0)
        output_tokens = usage_metadata.get("output_tokens", 0)

        response_metadata = getattr(response, "response_metadata", None) or {}
        raw_usage = response_metadata.get("usage") or {}
        cache_creation = raw_usage.get("cache_creation_input_tokens", 0)
        cache_read = raw_usage.get("cache_read_input_tokens", 0)

        # A cache WRITE is billed at 2x the input rate for a 1h TTL and 1.25x
        # for 5m. cache_creation_input_tokens alone therefore cannot be priced
        # - it is the same number either way. The raw Anthropic block splits
        # it (usage.cache_creation.ephemeral_{1h,5m}_input_tokens) but only on
        # a non-streamed call; every real Representative turn is streamed and
        # gets nothing. So the configured TTL is logged alongside, and the
        # split is captured where the API does supply it.
        _split = raw_usage.get("cache_creation") or {}
        cc_1h = _split.get("ephemeral_1h_input_tokens", 0)
        cc_5m = _split.get("ephemeral_5m_input_tokens", 0)

        # A streamed call (.stream() + summed AIMessageChunks - the actual
        # path every real user turn takes) never populates
        # response_metadata["usage"], so raw_usage is empty here even when
        # real caching happened. The same numbers are still available under
        # LangChain's own standardized usage_metadata shape instead, just
        # under different key names - confirmed via diag_stream_cache.py.
        # Only used as a fallback so the already-correct non-streamed
        # (.invoke()) path above is never overridden.
        if not raw_usage:
            input_token_details = usage_metadata.get("input_token_details") or {}
            cache_creation = input_token_details.get("cache_creation", 0)
            cache_read = input_token_details.get("cache_read", 0)

        # If usage_metadata came back empty (e.g. a hand-accumulated stream
        # object that never got LangChain's own usage_metadata populated
        # on it), fall back to the raw Anthropic usage block's own
        # input/output fields rather than logging zeros for everything
        # when the real numbers are sitting right there under a different
        # key.
        if not usage_metadata and raw_usage:
            input_tokens = raw_usage.get("input_tokens", 0)
            output_tokens = raw_usage.get("output_tokens", 0)

        try:
            from app.config import settings as _settings
            cache_ttl = _settings.prompt_cache_ttl
        except Exception:
            cache_ttl = "?"

        # NB for anyone pricing these lines: input_tokens is LangChain's
        # TOTAL, with cache_read and cache_creation as SUBSETS of it - not
        # additive buckets the way the raw Anthropic block reports them.
        # Uncached input is input_tokens - cache_read - cache_creation.
        # Summing the three charges the cached prefix twice; see
        # tools/cost/analyze_usage_log.py, which does it correctly.
        logger.info(
            "[llm_usage] label=%s model=%s request_id=%s session_id=%s "
            "input_tokens=%s output_tokens=%s cache_creation_input_tokens=%s "
            "cache_read_input_tokens=%s cache_ttl=%s "
            "cache_creation_1h=%s cache_creation_5m=%s",
            label, model, request_id, session_id,
            input_tokens, output_tokens, cache_creation, cache_read,
            cache_ttl, cc_1h, cc_5m,
        )
    except Exception:
        logger.exception("[llm_usage] failed to log usage for label=%s", label)
