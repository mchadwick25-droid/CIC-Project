# Card check applied: tacitus

Applied to `tacitus.card.json`; the file round-trips unchanged in format (two-space indent).

| Fix | Field | Result |
|---|---|---|
| 1 | `uncertain[7]` (what the verdict means) | applied. The Schanz-Hosius-Krüger, Duchesne and McGiffert sentences were cut; the text now ends after the Ruinart sentence, as given. |
| 2 | `uncertain[8]` (Gibbon, Schiller, McGiffert) | applied. Item removed; `uncertain` now has 12 items. |
| 3 | `uncertain[10]` (readings of the Latin; now index 9 after Fix 2) | applied. Sentence "Duchesne, following Harnack, takes Chrestianos as the true reading; " removed, leaving "Mirbt and Schanz print Christianos." |
| 4 | Entry field `modernWorks[2]` (Yonge) title | applied to `Card_Edits.md`, new section "Entry fields (card check)", not to the card. |
| 5 | `timeline[0].lines[0].reference` | applied. Now ends "lines 2527-2537". |

Every old text was found as quoted. Nothing was not applied.

JSON check: `python -m json.tool tacitus.card.json > /dev/null` passed.

Readability (`python -m engine.m1.profile_readability`, run on the scratchpad copy of the running text with the same three cuts made): 1876 words, grade 8.4 (names out 7.1), reading ease names out 73.5, 16.3 words a sentence, longest sentence 39 words, pass.
