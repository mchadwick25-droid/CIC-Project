"""One declared registry of every record field that ever reaches a
participant or the model that speaks to them, replacing seven
independently-maintained lists that did not all agree with each other:
`engine/m2/builders.py` `build_prompt()`'s own direct field reads and
`_chunk_text()`'s separate ones, `engine/m4/evidence.py` `_head_text()`,
`engine/m4/citation_cards.py` `_LABEL_FIELDS`, `engine/m1/gates.py`
`_PERSPECTIVE_FIELDS` and `_ATTRIBUTION_FIELDS`, and
`engine/m1/cross_world.py` `_PARTICIPANT_FIELDS`.

That disagreement is not hypothetical: `story.tellable_as` and
`voice_craft.identity`/`guard`/`flavor_notes[].note`/
`characteristic_concerns[]` are both on several of these lists and were,
for a real stretch of this project's history, missing from
`gate_readability`'s own checks (`engine/m1/gates.py`) despite being
compiled into every single turn's prompt — the exact hole the
`tellable_as`/voice_craft readability drift slipped through. Reconciling
gate coverage against this registry is a separate, later decision (it
needs Mark's ruling on whether some of these fields should ever be
readability-gated at all, not just added to a check) — this module only
makes the field list itself a single, checkable source of truth so a
gap like that can't happen silently again.

Each field's `role` names the surface it reaches a participant through,
because the same field can reach different surfaces differently:

- "instruction": standing guidance compiled above the ground line
  (`build_prompt()`'s `instruct()`, never `emit()`) — reaches the model as
  guidance on how to speak, never quoted back as the model's own claim
  about the world, and deliberately exempt from the leak-scan patterns in
  `gate_no_build_attribution` that would otherwise flag a real church-
  history sentence that happens to contain a date.
- "voice-diet": compiled into the model's own prompt as ground the voice
  may say back, verbatim or paraphrased — either in `build_prompt()`'s
  cached prefix, or in `_chunk_text()`'s retrieval-chunk files
  (`compiled/chunks/{lexicon,story,ambient,doctrinal_witness}/`).
- "evidence-head": the field `engine/m4/evidence.py`'s per-turn evidence
  block heads a record's entry with when retrieved live — a different,
  dynamic surface from the two above (see that module's own docstring
  for why the split exists).
- "participant-label": text a citation card, mark, or index entry shows
  directly (e.g. a Level-2 hover headline), independent of whether the
  voice itself ever says the words. Several of these are *derived* from
  more than one field (a figure's label picks between two entries in its
  `names` list; a quote's label joins its speaker to its source's `work`)
  — those derivations stay in `engine/m4/citation_cards.py`'s own helper
  functions (`_figure_label`, `_quote_label`), not reimplemented here;
  this registry only declares which fields feed them, so a future field
  those helpers start reading has to be declared too.

A field carrying more than one role is deliberate, not an error — most
fields reach a participant through more than one surface at once.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SpokenField:
    role: str  # "instruction" | "voice-diet" | "evidence-head" | "participant-label"
    note: str = ""


# record_type -> field_name -> SpokenField. Field order within a type
# follows first appearance in build_prompt()/build_fleet_preamble(), so a
# diff against those functions reads in the same order.
SPOKEN_FIELDS: dict[str, dict[str, SpokenField]] = {
    "fleet_voice": {
        "register_statements": SpokenField("instruction", "list of {number, statement}"),
        "register_hold": SpokenField("instruction"),
        "pronoun_rule": SpokenField("instruction"),
        "citation_contract": SpokenField("instruction"),
        "story_quote_reach": SpokenField("instruction"),
        "limit_discipline": SpokenField("instruction"),
    },
    "voice_craft": {
        "identity": SpokenField("instruction"),
        "guard": SpokenField("instruction"),
        "characteristic_concerns": SpokenField("instruction", "list[str]"),
        "flavor_notes": SpokenField("instruction", "list of {segment, note}; .note is the spoken text"),
    },
    "world_core": {
        "horizon": SpokenField("voice-diet"),
        "formation_logic": SpokenField("voice-diet"),
        "thinness": SpokenField("voice-diet"),
        "cautions": SpokenField("voice-diet"),
    },
    "term": {
        "plain_meaning": SpokenField("voice-diet", "build_prompt + _chunk_text + evidence-head"),
        "quick_meaning": SpokenField("voice-diet"),
        "world_word": SpokenField("participant-label", "prompt section header + citation-card label + _chunk_text"),
    },
    "gravity": {
        "name": SpokenField("participant-label", "build_prompt's Gravities list + citation-card label fallback"),
        "description": SpokenField("evidence-head", "also citation-card label fallback"),
    },
    "quote": {
        "modern_rendering": SpokenField("evidence-head"),
        "text": SpokenField("evidence-head", "fallback when modern_rendering absent; verbatim, never readability-graded by design"),
        "speaker_or_author": SpokenField("participant-label", "feeds _quote_label via _quote_speaker_label"),
        "sources": SpokenField("participant-label", "list of {source_id, locus}; feeds _quote_label"),
    },
    "story": {
        "tellable_as": SpokenField("voice-diet", "build_prompt + _chunk_text + evidence-head + citation-card label"),
        "text": SpokenField("voice-diet", "fallback when tellable_as absent; never readability-graded by design"),
    },
    "demonstration": {
        "exchange": SpokenField("voice-diet", "list of {speaker, text}"),
    },
    "doctrinal_witness": {
        "text": SpokenField("voice-diet", "build_prompt + _chunk_text + evidence-head + citation-card label (first sentence)"),
        "positions": SpokenField("evidence-head", "_head_text fallback when text is absent"),
    },
    "honest_limit": {
        "statement": SpokenField("voice-diet", "citation-card label uses first sentence"),
    },
    "force": {
        "name": SpokenField("participant-label"),
        "description": SpokenField("evidence-head", "also citation-card label fallback"),
    },
    "contested_claim": {
        "claim": SpokenField("evidence-head", "also citation-card label"),
    },
    "figure": {
        "names": SpokenField("participant-label", "list of {tag, name}; feeds _figure_label's in-world/scholarly pick"),
        "bridge_line": SpokenField("evidence-head", "compiled into figures.json; read live by engine/m4/name_bridge.py"),
    },
    "source": {
        "work": SpokenField("participant-label", "feeds _quote_label via the cited quote's sources[].source_id"),
    },
    "ambient": {
        "detail": SpokenField("voice-diet", "_chunk_text only"),
    },
}


def fields_with_role(record_type: str, *roles: str) -> list[str]:
    """Field names for a record type carrying any of the given roles, in
    registry declaration order. Passing no roles returns every declared
    field for the type."""
    entries = SPOKEN_FIELDS.get(record_type, {})
    if not roles:
        return list(entries)
    return [name for name, sf in entries.items() if sf.role in roles]


# ---- Relocated consumer lists ---------------------------------------------
# These three are genuinely the same shape as this registry (record_type ->
# list[str] of plain field names, read by a simple isinstance/get loop) and
# move here verbatim - same values as before relocation, byte-for-byte, so
# relocating them changes where they live, not what they do.
#
# Deliberately NOT auto-derived from SPOKEN_FIELDS's roles: doing that would
# have been a real, silent behavior change. fields_with_role("fleet_voice",
# "instruction") includes register_statements/register_hold/
# story_quote_reach, none of which ATTRIBUTION_FIELDS has ever scanned - a
# fresh gap found while writing this registry, not fixed here, because
# fixing it changes what gate_no_build_attribution actually checks, which
# is exactly the kind of change this registry-only PR is not scoped to make
# silently. Filed for Stage 2c (register-profile work) to decide.
#
# `engine/m4/citation_cards.py`'s `_LABEL_FIELDS` is NOT relocated here: it
# maps record_type to a *function* (several doing real cross-record lookups
# - `_figure_label`, `_quote_label`), not a field-name list, so it isn't the
# same shape as this table. Its own fields (figure.names, quote.
# speaker_or_author, quote.sources, source.work, ...) are still declared
# above in SPOKEN_FIELDS and checked for declaration by
# `engine/m1/tests/test_spoken_fields.py`; the label functions' own
# derivation logic is untouched.

# engine/m1/gates.py gate_no_build_attribution's own field scan.
ATTRIBUTION_FIELDS: dict[str, list[str]] = {
    "voice_craft": ["identity", "guard"],
    "world_core": ["horizon", "formation_logic", "thinness", "cautions"],
    "term": ["plain_meaning", "quick_meaning", "world_word"],
    "doctrinal_witness": ["text"],
    "honest_limit": ["statement"],
    "story": ["tellable_as", "text"],
    "fleet_voice": ["pronoun_rule", "citation_contract", "limit_discipline"],
}

# engine/m1/gates.py gate_perspective_leak's own field scan (voice-reproduced
# fields only).
PERSPECTIVE_FIELDS: dict[str, list[str]] = {
    "term": ["plain_meaning", "quick_meaning"],
    "story": ["tellable_as", "text"],
    "ambient": ["detail"],
    "doctrinal_witness": ["text"],
    "honest_limit": ["statement"],
}

# engine/m1/cross_world.py check_participant_field_leaks's own field scan.
PARTICIPANT_FIELDS: dict[str, list[str]] = {
    "figure": ["bridge_line"],
    "term": ["world_word"],
    "story": ["tellable_as"],
    "gravity": ["name"],
    "force": ["name"],
    "contested_claim": ["claim"],
}
