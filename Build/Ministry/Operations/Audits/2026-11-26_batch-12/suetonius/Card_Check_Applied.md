# Card check applied: Suetonius

All changes are in `suetonius.card.json`. Each old text was found exactly as quoted. No entry-field changes were given, so `Card_Edits.md` is unchanged.

1. `timeline[0].lines[0]` `text` ("from tax forever") and `reference` (lines 25769-25770): applied.
2. `briefReferences[0]` ("freed from tax forever"): applied.
3. `legacy.remembered[1]` (each complaint given to its own man): applied.
4. `uncertain[11]` (Pliny item): removed. Applied.
5. `timeline[3].lines[3]` `text` (title-of-power sentence added) and `reference` (4.7.4 to 4.7.7, lines 16770-16830): applied.
6. `timeline[2].lines[3].reference` (lines 918-41018): applied.
7. `timeline[4]`: period `when` and `headline`, chronicle line `when` and `reference` (46321-46329), and the chronicle line moved to `lines[0]`: applied.

Totals: 7 changes (13 field edits), 7 applied, 0 not applied.

JSON check: `python -m json.tool suetonius.card.json` passes.

Readability score: not run. `Card_Edits.md` names the command, but it was run on a plain-text file of the card's running text kept outside the repository, and that file is not available here.
