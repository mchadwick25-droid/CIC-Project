# Card check applied: Clement of Alexandria

File: `clement-of-alexandria.card.json`. All changes found their old text exactly once.

| Change | Where it went | Result |
|---|---|---|
| F1 | `timeline[2].when` | applied |
| F2 | `timeline[0].lines[1].text` | applied |
| F3 | `timeline[2].lines[4].text` | applied |
| F4 | `timeline[2].lines[8].text` and `briefReferences[7]` | applied (both) |
| F5 | `timeline[2].lines[11].text` | applied |
| F6 | `timeline[2].lines[12].text` (line number before F7's insert) | applied |
| F7 | new line in `timeline[2].lines`, after the line on Eusebius's list of books (now `lines[12]`; the Outlines line is now `lines[13]`) | applied |
| F8 | `timeline[3].lines[0].text` | applied |
| F9 | `timeline[5].lines[0].text` and `legacy.traces[3]` | applied (both) |
| F10 | `timeline[5].lines[1].reference` | applied |
| F11 | `sources.about[0].title` | applied |
| F12 | `briefSources[0].title` | applied |
| F13 | new item `briefSources[3]`, after the Eusebius Greek item | applied |
| F14 | `Card_Edits.md`, new section "Entry fields (card check)", five `modernWorks` items | applied |

Totals: 14 applied, 0 not applied.

JSON check: `python3 -m json.tool clement-of-alexandria.card.json > /dev/null` passed.

Readability: not scored. `Card_Edits.md` gives the result of its run but names no command.
