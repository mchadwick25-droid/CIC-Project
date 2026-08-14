"""The name bridge: who was this person the Representative just named?

Mark's read of the live site, 2026-08-09, and the measurement that followed
(scripts/transparency_reach.py): the transparency gap is mostly NAMES, not
vocabulary. A reader meets Aphrahat, Pachomius, Blaesilla, Gushtazad and has
nothing at all. `find_glosses_used` cannot help - `confirmed_glosses` is a
vocabulary table and names were never in its scope.

This is that function's sibling for people. Same shape, same contract, same
place in the graph: run AFTER generation, decorate what was said, never
influence what gets said.

THE GOVERNING RULE, and the reason this is a UI affordance rather than a
prompt instruction: the Representative goes on saying "Aphrahat" the way a
person would. The bridge is the interface's job. Telling the voice to
introduce every name it uses would produce a Representative who lectures -
which is the failure the whole 1A design exists to prevent, and the same
conclusion the `inline: false` gloss case reached on 2026-08-09.

Detection is deterministic substring matching on the figure record's own
attested names, longest-name-first so "Simeon bar Sabbae" wins over "Simeon".
No LLM call: unlike a citation, whose connection to the text is a judgement
(see filter_grounded_citations), a name either appears or it does not.
"""
from __future__ import annotations

import functools
import json
import re


@functools.lru_cache(maxsize=16)
def _registry(world_id: str) -> tuple:
    """Bridged figures for a world, from data/<world>/figure_registry.json
    (built by cic/engine/build_figure_registry.py). Returns a tuple so the cache
    holds something immutable.

    Fails toward the EMPTY registry - a world whose file is missing or
    unreadable simply gets no pills, exactly as it had none before this
    module existed. Same philosophy as evaluate_negative_conditions: a check
    that disappears on error must never leave the participant worse off than
    if it had never been added.
    """
    try:
        from app.config import settings
        path = settings.get_world_config(world_id).data_path / "figure_registry.json"
        entries = json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return ()
    return tuple(entries)


def find_figures_used(world_id: str, response_text: str) -> list[dict]:
    """Which bridged figures this response actually named.

    One entry per FIGURE, not per mention - the UI decorates the first
    occurrence, and a Representative naming Ambrose four times should not
    produce four identical panels.

    `matched` carries the exact surface form found, so the frontend can
    highlight what is on screen rather than guessing at a canonical spelling
    that may not appear - the same defect the gloss path hit when it
    highlighted only `rendered` and rendered nothing for Chloe.
    """
    entries = _registry(world_id)
    if not entries or not response_text:
        return []
    out, claimed = [], []
    for e in entries:
        # longest first: "Simeon bar Sabbae" must win over "Simeon"
        for name in sorted(e.get("names") or [], key=len, reverse=True):
            # floor of 3 matches the registry builder's own short-form floor
            # ("Leo"); a 4-character floor here silently dropped him even
            # though the registry carried him.
            if len(name) < 3:
                continue
            # CASE-SENSITIVE, deliberately: a name is a proper noun, and an
            # ignore-case match put an evangelist panel on "mark the day".
            m = re.search(rf"\b{re.escape(name)}\b", response_text)
            if not m:
                continue
            # a longer figure name already covering this span wins
            if any(s <= m.start() < t for s, t in claimed):
                continue
            claimed.append((m.start(), m.end()))
            out.append({
                "figure_id": e["figure_id"],
                "display_name": e["display_name"],
                "matched": response_text[m.start():m.end()],
                "bridge_line": e["bridge_line"],
            })
            break
    return out
