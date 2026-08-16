"""The quotation ground truth: which sayings has this world actually
licensed a Representative to quote, and did a generated turn quote
anything else?

Same shape, same contract as figure_bridge.py's own registry loader: run
AFTER generation, read a deploy view built by the generic engine
(cic/engine/build_quotes_index.py), never influence what gets said. Two
pure, no-LLM pieces live here - loading the candidate list, and finding
the quotation-marked spans a turn actually contains. The judgment of
whether a found span matches a candidate needs an LLM call and belongs
next to get_monitoring_llm in app/graph/nodes.py, the same split
filter_grounded_citations already keeps from this module's own
find_figures_used.

Detection of WHICH text counts as "quoted" is deterministic (quotation
marks), unlike a citation's connection to the text, which is a judgment.
What matching a found span against a candidate saying MEANS is not
deterministic - a real quotation is routinely paraphrased a word or two
from its licensed text_translation - which is why that half is an LLM
call, not a string comparison, exactly as filter_grounded_citations
already argued for citations over find_glosses_used's plain substring
match.
"""
from __future__ import annotations

import functools
import json
import re

# Straight and curly double quotes. A minimum content length excludes
# scare-quoted single words ("we", "I") that are emphasis, not citation -
# every genuine quotation seen in this build's own live-model testing was
# a full clause or longer.
_QUOTE_SPAN_PATTERN = re.compile(r'["“]([^"”]{8,}?)["”]')


@functools.lru_cache(maxsize=16)
def _registry(world_id: str) -> tuple:
    """Licensed quotes for a world, from data/<world>/quotes.json (built by
    cic/engine/build_quotes_index.py). Returns a tuple of frozen dicts-as-
    tuples-of-items is unnecessary here since callers never mutate entries -
    a tuple of the raw dicts is enough to make the cache itself immutable.

    Fails toward the EMPTY registry - a world whose file is missing,
    unreadable, or not yet built (no quote/ records authored) simply has no
    candidates, exactly as figure_bridge._registry fails toward no bridged
    figures. A missing file is never distinguished from a world with zero
    quotes: both mean "nothing to check against," which the caller in
    nodes.py must treat as automatic UNLICENSED for anything quoted,
    not as "check skipped."
    """
    try:
        from app.config import settings
        path = settings.get_world_config(world_id).data_path / "quotes.json"
        entries = json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return ()
    return tuple(entries)


def licensed_quotes(world_id: str) -> tuple:
    """Public accessor - the candidate list nodes.py judges spans against."""
    return _registry(world_id)


def extract_quoted_spans(response_text: str) -> list[str]:
    """Every quotation-marked span in a generated turn, in order of
    appearance, deduplicated (a voice repeating the same line twice in one
    turn is one grounding question, not two).
    """
    if not response_text:
        return []
    seen: list[str] = []
    for match in _QUOTE_SPAN_PATTERN.finditer(response_text):
        span = match.group(1).strip()
        if span and span not in seen:
            seen.append(span)
    return seen
