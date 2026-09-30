# Live-surface commentary: promotion cleanup (2026-09-30)

Companion to the promotion PR from `main` into `live`. That PR counts every file changed since `live`, so the commentary check flagged 93 lines in 25 files that no single earlier PR had touched together. Mark decided on 2026-09-30 to clean all of them before promoting.

## What was done

| Group | Lines | Action |
|---|---|---|
| Engine comments and docstrings (dashboard, admin login, anon cap, price tables, audit reader, tests) | 26 | Removed "Mark, <date>" attributions, decision history and ruling-named identifiers in prose. Meaning and code are unchanged. |
| Records: witt `world_core` body, two rzg source records, one rzg gravity | 10 | Replaced build narration with a short statement of fact. The removed wording is kept word for word in `Live_Commentary_Relocated_Notes_2026-09-30.md`. witt and rzg were rebuilt and repinned. |
| Corpus map, reformed cities | 1 | Dropped "a genuinely open gap" from a note on a missing volume. |
| Build/worlds construction documents (witt phases 6 and 7, cappadocian brief and notes, rzg Source Registry) | 29 | Removed dates, ruling numbers and review-round wording. No passage was deleted outside the registry's closing paragraph, which is relocated. |
| Left to the checker rules below | 27 | Atlas status labels (8), Source Registry rows (10), the rzg acquisition manifest (7), file names with dates (2). |

Follow-ons the rzg records carried are logged as rzg Open_Gaps_Tracking item 55.

## Checker changes and their measured effect

`tools/check_live_commentary.py` no longer flags five kinds of line that are not narration. Whole-tree scan against `main`'s checker: 4,122 REWRITE plus ROUTE lines fall to 4,042. No line became newly flagged.

- **A date inside a cited file name** (`live-table-report-witt-rzg-2026-09-19.json`): 14 lines. A date written into prose next to one is still flagged.
- **`"statusWord"` labels** in the atlas and census, such as "Creedal question — not yet resolved": 16 lines. They are public status labels. The same words in prose are still flagged.
- **Source Registry rows:** a date cell with notes ("2026-09-25 (vendored); 2026-09-29 (added to this Registry)") and the status value NOT YET ACQUIRED: 13 lines. A date in a notes cell, or another cue in the row, is still flagged.
- **Source acquisition manifests** are ledgers, like Open_Gaps_Tracking: 37 lines. They record closure dates and open gaps by design.

## Not cleaned

- `Cited paths` on the three lpc citations. The lpc thread owns them.
- gallic's `facilitator_brief` field `formation_strengths[1].text`, which fails `regate` against `live` (FK 15.3, FRE 46.8). The gallic thread owns it.
