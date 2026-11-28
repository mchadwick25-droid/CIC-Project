# Card check applied: Methodius of Olympus

All edits made to `methodius-of-olympus.card.json` by exact string replacement (each old text found exactly once). The file was re-serialized with two-space indent, so only the changed lines differ.

1. `uncertain[1]`: applied.
1. `timeline[0].lines[2].text`: applied.
1. `timeline[0].lines[2].reference`: applied.
2. `legacy.traces[4]`: applied.
3. `sources.about`, Nikephoros entry: removed, applied.
4. `sources.about`, John of Damascus entry `title`: applied.
5. `quotationOriginals[1].uncertain`, "(lines 35747-35750)": applied.
6. `quotationOriginals[2].work`: applied.
7. `timeline[4].lines[4].reference`, lines 899-924: applied.
8. `modernWorks`, four entries: written to `Card_Edits.md` under "Entry fields (card check)", applied there (entry field, not the card).
9. `uncertain[5]` Rufinus sentence, `sources.about` NP3 `title` and `author`: applied.
10. `uncertain[3]`: applied.

Not applied: none.

JSON check: `python -m json.tool methodius-of-olympus.card.json` passed (valid).
Readability scoring: not re-run (Card_Edits.md names a command, but the check's own re-run is on a plain-text extract; not requested to rebuild it here).
