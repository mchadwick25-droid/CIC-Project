"""Term/concept glosses - the OTHER track VR_1A named, and the original
complaint that started this whole audit (Mark, live site, 2026-08-09: "it
uses complicated words ... catechumen and Didache"). `glosses` has been a
required key on every voice_turn event since the catalog was written
(engine/m4/events.py) and hardcoded to `[]` in every branch that builds
one - this is the first code that populates it.

The old system's approach (cic-poc/backend's `confirmed_glosses.py`) was a
hand-curated, world-by-world allowlist - reviewed and added "one at a
time, per the project owner's own request," specifically to avoid the
Goodhart failure transparency_reach.py's own docstring names: "driving
coverage up by glossing everything would produce a Representative who
lectures." That discipline is honored here differently, not abandoned:
rather than a maintained list of which words to watch for, a gloss only
ever fires on a term the model ALREADY cited - the same [[record.id]] tag
the citation-verification net already checked before any of this text
reached the participant. A term mentioned in passing, uncited, never
glosses; a term the voice grounded a claim in, and said in the same
sentence it tagged, does. This can't over-glean by construction: its
ceiling is exactly the fleet's own citation rate, which is itself
governed (grounding_net's own withhold discipline) - there is no version
of this module that "glosses everything," because it never introduces a
term the voice didn't already choose to cite.

First occurrence only, per session - same discipline, same threading
pattern (already_bridged_ids, caller-supplied) as
engine.m4.name_bridge.find_figures_used.
"""
import re

from engine.m4.citation_cards import resolve_source_card


def _matchable_form(term_record: dict) -> str | None:
    word = term_record.get("world_word")
    if not word:
        return None
    return word.split(" (", 1)[0].strip()


def find_glosses_used(citations: list[dict], repository_records: dict[str, dict], *, already_bridged_ids: set[str] | None = None) -> list[dict]:
    """One entry per cited TERM record whose world_word (head form, before
    any parenthetical - "allegoria (the spiritual sense)" matches on
    "allegoria") appears in the very sentence that cited it, in citation
    order (which is sentence order - engine.m4.grounding_net.check_turn
    walks the turn's sentences in the order they appear), skipping
    anything in already_bridged_ids.

    Deliberately narrower than engine.m4.name_bridge.find_figures_used:
    that module searches the whole turn's text for any figure's name,
    because a name carries meaning independent of being cited. A term's
    definition is only worth surfacing where the voice itself just used
    it AS grounding - so this checks the term's own cited sentence, not
    the whole turn.
    """
    already = set(already_bridged_ids or ())
    out = []
    for citation in citations:
        sentence = citation.get("sentence") or ""
        for record_id in citation.get("record_ids") or []:
            if record_id in already:
                continue
            record = repository_records.get(record_id)
            if record is None or record.get("record_type") != "term":
                continue
            form = _matchable_form(record)
            if not form:
                continue
            match = re.search(rf"\b{re.escape(form)}\b", sentence, re.IGNORECASE)
            if not match:
                continue
            already.add(record_id)
            card = resolve_source_card(record_id, repository_records)
            out.append(
                {
                    "id": record_id,
                    "matched_name": match.group(0),
                    "plain_meaning": record.get("plain_meaning"),
                    "quick_meaning": record.get("quick_meaning"),
                    "translational_sense": (record.get("senses") or {}).get("translational"),
                    "false_friend": record.get("false_friend") or [],
                    "sourced_by": card["sources"] if card else [],
                }
            )
    return out
