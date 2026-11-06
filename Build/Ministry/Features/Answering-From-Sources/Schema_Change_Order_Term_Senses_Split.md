# Schema change order: two optional senses fields on the term record

Named schema change order. `engine/m1/schemas.py` sets `additionalProperties: false` on a term's `senses`, so a term record cannot carry a new sense until this order lands. It serves `Stage5_Change_Order_Lexicon_Card.md` and Decision-Log 56.

Mark's words, 2026-11-01, relayed by the coordination thread: "b, but we need the modern misunderstanding or a contrast to how people think it means today vs in that world". Coordination's ruling the same day: split at the source, not by sentence in code.

## Why

All 19 lpc term records hold `senses.translational`, a single block of 35 to 101 words that runs how a modern listener hears the word together with what the world means by it ("A modern listener may picture a formal identity document or licence. We mean a compliance certificate ..."). A card that shows the two side by side needs them as two fields.

## What changes

Two optional fields inside `senses` on the `term` record type:

| Field | Type | Meaning |
|---|---|---|
| `heard_today` | string | How people hear the word today: the modern misunderstanding. |
| `meant_here` | string | What the word meant in this world. |

Existing records validate unchanged without them. `senses.translational` stays as it is.

## What goes with it

1. Gate (`gate_glossary_retrofit_complete` in `engine/m1/gates.py`, not a new gate): the two fields come as a pair, and each present field is a non-blank string. A record with neither is unchanged.
2. Card data (a later code change, with the lexicon card build): a gloss carries `heard_today` and `meant_here` when both are present; a term without them carries `senses.translational` as the whole-block fallback. Nothing is split by sentence in code.

## What it does not do

- No record is written by this order. Library fills the fields for the 19 lpc terms under its own authoring step, with the review of term meanings.
- No display change in this order.
- No gate is retired and no other world is touched.

## Done when

The schema and the gate accept the fields; a term without them validates unchanged; one field without the other, or a blank one, is a finding. Tests cover each.
