# Card check applied: Origen (`origen`)

| Fix | Where | Result |
|---|---|---|
| 1 remembered line | `legacy.remembered`, new item after "About three centuries after his death, a council..." (index 7) | applied |
| 1 `sources.about` Evagrius entry | after "Anathemas of the Fifth Council" | applied |
| 1 entry `modernWorks` Bidez-Parmentier | `Card_Edits.md`, heading "Entry fields (card check)" (entry field, not card) | applied |
| 2 `uncertain` 12 (index 11) | Hefele sentence removed | applied |
| 3 `uncertain` 8 (index 7) | Jerome sentence added | applied |
| 3 `sources.about` Jerome Apology entry | after "Preface to Job; Against John of Jerusalem" (left as is) | applied |
| 4 `uncertain` 7 (index 6) | "Trebonianus Gallus" to "Gallus" | applied |
| 5 Decius line note | timeline 4, line 1 | applied |
| 5 Ordination line note | timeline 2, line 5 | applied |
| 5 Death line note | timeline 4, line 5 | applied. The old text also occurs inside `uncertain` 7 as part of a longer paragraph; changed only the timeline note, which the check names ("Death line, note"). |
| 6 Epiphanius note | timeline 5, line 7 | applied |

Not applied: none.

JSON check: `python -m json.tool origen.card.json` passed.

Scoring: `Card_Edits.md` names no command, only a result on a file outside the repository, so the card's running text was not rescored.
