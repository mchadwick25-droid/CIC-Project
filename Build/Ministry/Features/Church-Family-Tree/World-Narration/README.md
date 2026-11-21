# World narration in the tree's voice

The tree's narrator texts for the 11 built worlds: each world's Story, Legacy and documented stories, rewritten from the world's own voice into the narrator's. The tree will show them and play them in its standard voices (Daniel for Story and Legacy, Neo for documented stories). Church in Conversation keeps the original texts in `records/` and its Representative recordings.

Source: Decision-Log, "Built worlds on the tree move to the standard voices, after a rewrite into the narrator's voice" (2026-11-20); Open-Gaps, "Built worlds in the standard voices: rewrite, then record" (2026-11-20).

## What the rewrite does

Mark, 2026-11-20: "change the voice, and link the prose".
- The original's content and order are kept. Every claim keeps its confidence, every witness stays credited, and every quote stays word for word.
- First person ("our communities", "us") and the world's own hedges become the narrator's third person and plain statements of uncertainty, at the same strength.
- Runs of short one-act sentences are joined with cause, contrast and time, only where the original supports the link.
- Only what fails the brief kit's blocking bar is fixed. A piece is not re-told to the kit's full craft.

## Layout

One folder per world, named by its census id. For each piece `<key>` (`story`, `legacy`, `docstory-<story id>`, the keys `worldPieces()` in `Build/tools/generate_world_narration.mjs` gives):

- `<key>.txt` is the narrator text, the file the site thread releases.
- `<key>.orig.txt` is the world's text it was rewritten from, as compiled in `cic-website/data/worlds/<id>.json` on the day of the rewrite. If the record later changes, compare it with this file to see that the rewrite is stale.
- `<key>.sheet.md` holds the original's grounding records with their confidence and notes, and each quoted span with its quote record and source lines in `cic/texts/`.
- `<key>.review.md` is the independent review. Each world also has `Review_Round<n>.md`, the round's summary.

## Steps

1. Sheet, made mechanically from the compiled world and its records.
2. Rewrite (Sonnet), from the sheet and Kit Parts 1 and 2.
3. Review (Opus), by another hand: one hearing, fidelity sentence by sentence against the original, quotes checked in their source files, `python -m engine.m1.profile_readability`.
4. One revision and one targeted recheck. Anything still failing goes to Mark. That makes three rounds at most.

## Status

All 122 pieces passed review on 2026-11-20. The hand-off for recording is in Open-Gaps, "Built worlds in the standard voices: the writing is done, hand-off for recording" (2026-11-20). The roles each step used are in `roles/`.
