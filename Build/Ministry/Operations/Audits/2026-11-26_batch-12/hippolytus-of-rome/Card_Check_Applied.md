# Card check applied: Hippolytus of Rome

## Changes

1. **`hippolytus-of-rome.card.json`, `quotationOriginals[0].uncertain` (Q2).** The old text was found once, as quoted, and replaced word for word with the new text from `Card_Check.md`. Applied.
2. **Entry fields.** The check gives no change to an entry field, so nothing was written under "Entry fields (card check)". Not needed.
3. **`Card_Edits.md`, "The two quotations", Q2.** The restored Greek ("Greek, NG 3705-3708, checked by hand: ..." with its glosses, and the sentence listing the scan's misprints) was replaced by the new `uncertain` text, copied word for word from the check. A lead-in sentence on the damaged scan and line 3706 was kept. No restored Greek (ἀλλ᾽, ἐκ, ἢ, ἀκτῖνα, μία) remains in the card files. Applied.

## Left as found

The last sentence of that Q2 bullet in `Card_Edits.md` still reads "HIP confirms the reading, so the Greek is carried by hand in the entry's `uncertain`, not as `original`." That is now out of step with the new `uncertain` text. I did not change it, since the instruction named only the restored Greek.

## Checks

- `python -m json.tool hippolytus-of-rome.card.json`: valid.
- Running-text score: `Card_Edits.md` names `python -m engine.m1.profile_readability`, but I did not run it (the changed field is a note on the quotation).
