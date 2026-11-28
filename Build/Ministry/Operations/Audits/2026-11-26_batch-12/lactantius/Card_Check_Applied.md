# Card check applied: Lactantius (`lactantius`)

Changes are to `lactantius.card.json` unless noted.

| # | Change | Where it went | Result |
|---|---|---|---|
| 1 | Timeline, period 1, line 4 `text`: "Latin" removed | timeline | applied |
| 2 | Timeline, period 1, line 6 `text`: "taught the art of speaking" replaced | timeline | applied |
| 3 | Timeline, period 3, philosophers line `reference` | timeline | applied |
| 4 | Timeline, period 3, Book VII line `reference` | timeline | applied |
| 5 | Timeline, period 3, address line `text`: "hailing him as" | timeline | applied |
| 6 | `uncertain[3]`: "some with the first name Lucius." | uncertain | applied |
| 7 | Calvin letter trace, added after the Calvin item | `legacy.traces` (last item) | applied (exact text given) |
| 8 | Calvin letters source, added after the Calvin item | `sources.about` (last item) | applied (exact text given) |
| 9 | Entry field `legacy` (gloss for "doctor of the Church") | `Card_Edits.md`, heading "Entry fields (card check)" | applied there; not a card field |
| 10 | `Card_Edits.md` "Claims not found": the "ancient doctor" paragraph no longer applies | none | not applied (no exact text given; a removal, and changes nothing on the card) |

Each old text was found exactly once, as quoted.

JSON check: `python -m json.tool lactantius.card.json > /dev/null` passed.

Readability: `Card_Edits.md` names a command only as a run outside the repository (`lactantius-card-text.txt`), not a repo command, so the card was not rescored.
