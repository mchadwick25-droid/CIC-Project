# Stage 3 change order amendment: a quote's `text` is shown on the card as the edition's words

Named change order. It amends one line of the spoken-field registry (`engine/m1/spoken_fields.py`): the quote record's `text`, which read "verbatim source wording, never voiced or shown".

## Authority

Mark chose quote-card template B on 2026-11-01 (Decision-Log 52), whose second layer, "In the edition", shows the edition's words. The change of Settled row 11 by `Stage3_Change_Order_Amendment_Card_Content.md` already allows the card's content to change.

## What changes

- The registry line now reads: verbatim source wording; never voiced; shown on the quote card as the edition's words; kept on this role so the gates still scan it; never readability-graded by design.
- The rule that the voice never speaks `text` stays. The spoken form is `modern_rendering`.

## What does not change

- `text` is not readability-graded and is not placed in an answer.
- The story record's `text` keeps its line ("never voiced or shown"): the story card does not show it.

## Done when

The registry line is amended and the quote card shows the edition words in the pull request that builds template B.
