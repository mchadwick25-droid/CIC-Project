# Transparency path check for stories and quotes

First task of the Stage 3 change order. Code read only, 2026-10-29. No model call.

## What reaches the reader today

Engine (`engine/m4/transparency_plan.py`, `engine/m4/citation_cards.py`):
- A cited story gets an element in the transparency plan. Its mark sits at the end of its telling: the end of the last sentence of a contiguous run of sentences citing it. A later run of the same story is a second element with `repeat: true`. A quote's mark follows the quoted words.
- Each element and reference carries the cited record's whole `confidence` envelope verbatim.
- Mark cap: at most max(3, min(8, ceil(sentences / 2))) elements stay inline. Over the cap, terms count outside it, then figures drop, then stories (the latest first), and quotes never drop. A dropped element's record moves to `end_references`, shown at the end of the reply.
- The source card for a story holds record id, type, label (`tellable_as`) and sources. The card for a quote also holds `spoken_rendering` and `speaker`.

App (`cic-poc/frontend/src/components/StoryMark.tsx`, `VoiceTurnBody.tsx`):
- A story or quote element renders as an inline mark. Hover shows the label, each source (citation or work, author) and a plain phrase for `confidence.formation_confidence`. Click shows the label, the quote's spoken rendering, and the source list.

## Against the reported claim

The report was: stories sit under one end-of-answer marker, and tier and confidence data is dropped before the screen. The code shows:
- Not so as a rule. A story is marked inline at the end of its telling. It goes to the end references only when the cap pushes it out.
- Confidence is not dropped before the screen: the whole envelope reaches the app, and the hover shows the formation-confidence phrase. The other envelope fields (citation specificity, verification state, evidentiary weight, divergence note) are not shown.
- A story record carries `narrative_tier` (all seven lpc stories are tier 1) and `narrative_tier_justification`, and `retrieval.tier`. The engine under `engine/m4` never reads `narrative_tier`, so it never reaches the card or the app.
- A story card carries no brief meaning, and the click shows a source list rather than a page for the full story. For a quote, the card carries the spoken rendering but not the edition words.

## Data added in this step (additive, no display change)

`resolve_source_card` now also returns, for a story, `means` (the record's one-line meaning from `use_note.means`) for the hover's brief context, and `narrative_tier`. The app ignores fields it does not read, so nothing on screen changes.

## Held for Mark: edition words on the quote card

The change order's three-layer card shows the edition words. Today a quote card deliberately carries the spoken rendering and the source reference and no original wording; `test_a_quote_card_carries_the_modern_rendering_and_source_reference_and_no_original_wording` asserts it. Adding the edition words reverses that rule, so it is not done here. Mark has left it undecided (2026-10-29): the rule and its test stay as they are, and it is an open question in the Stage 3 order.

## For the still-works check

Existing tests cover today's marks (`VoiceTurnBody.test.tsx`, `StoryMark` use, `test_transparency_plan.py`). The check on lpc compares the same fields before and after the stage 3 change.
