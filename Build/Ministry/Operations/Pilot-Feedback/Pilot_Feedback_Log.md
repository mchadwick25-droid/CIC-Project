# Pilot Feedback Log

Append-only. Entries are numbered; a merged entry's number never changes. Status changes are added as new lines under the entry, never edits.

## Batch 1 — 2026-10-19
Source: one pilot tester (name not given), notes passed on by Mark.

| # | Part of product | What they said | Sort | Status |
|---|---|---|---|---|
| 1 | Participant app: main screen | Main screen does not fit the screen (photo attached; not yet seen). | Quick fix | Open |
| 2 | Participant app: waiting state | While the AI is thinking, animate something so it does not look stalled. | Quick fix | Open |
| 3 | Participant app: reading area | Wondered where the answer went. Reading space was very small. Zoom did not work. | Quick fix | Open |
| 4 | Participant app: text selection | Copy/paste is glitchy: can highlight backwards but not forwards. | Quick fix | Open |
| 5 | Public site: page order | The table app is the biggest element; highlight it at the top instead of the bottom. | Quick fix | Open |
| 6 | World content: table choices | Choices at the table are lesser known and lack Ignatius, Irenaeus, Tertullian, Athanasius, Augustine, Clement. Why? | Bigger issue | Open |
| 7 | World content: scope | Would it make sense to add Jewish rabbis? Josephus? | Bigger issue | Open |
| 8 | Voice and answer behaviour | Asked about Luke 9:27. None of the three had an answer (good: nothing invented), then they described what their group generally represents. Asks whether that is wanted or whether they should just answer. Dislikes 400 words where 4 suffice. | Bigger issue | Open |
| 9 | Funding and product direction | Loves the 300 free tokens. Assumes a paywall comes after. | Bigger issue | Open |
| 10 | Participant app: disclaimer | Loves the disclaimer before conversation. | Praise | No action |
| 11 | Overall | Loves it. Great tool to go right to the source. | Praise | No action |

## Status updates — 2026-10-19
- Mark approved quick fixes 2 to 5 as one batch (item 1 waits for the photo).
- Item 2: built. The waiting note now shows larger animated dots in the table room and the interview room.
- Item 3: built. The table room now brings the newest question to the top so the answer opens below it, as the interview room already did. The zoom fault was the app's height tracking: pinch-zoom shrank it. It now allows for the zoom level.
- Item 4: not fixed. Nothing in the code blocks forward selection; it needs a reproduction (device and browser).
- Item 5: built. The Build a Table card now sits first on the home page, above Church Family Tree.

## Status updates — 2026-10-19 (photos)
- Item 1: Mark sent six iPad photos of the table room and home page and confirmed the table room is the screen that does not fit. In the photo the page is cropped at both edges, which fits a zoomed page. The page that frames the table room sized itself to the zoomed viewport, the same fault as item 3. Fixed in talk.html; not yet confirmed on an iPad.

## Batch 2 — 2026-10-19 (Mark's own observations, divergent phase)
Source: Mark, from his iPad photos. Not sorted yet; Mark is collecting before any build starts.

| # | Part of product | What was observed | Sort | Status |
|---|---|---|---|---|
| 12 | Participant app: under the question box | Five small controls stack below the box (Leave for now, free tokens and Go deeper, This helped, Report a problem, Delete this conversation). Mark finds the visuals struggling and overwhelming. | Not sorted | Collecting |
| 13 | Participant app: visual load | Mark's view: the visuals are overwhelming overall. Conceptual items to follow from Mark. | Not sorted | Collecting |
| 14 | Selection and descriptions: scholarly voices | Mark's view: users want connection with the scholarly voices of each tradition, but those voices appear only late in a description. They should come first in every description, especially at selection (for example, "Alexandria was the first school; its voices of origin were ..."). Overlaps items 6 and 7. | Not sorted | Collecting |
| 15 | Representatives: who they stand for | Mark's view: keep Representative voices, but users do not know who a Representative is or has context for them. The Representative knows the real historical voices. It must be much clearer who the Representative is representing, not only which world. Overlaps item 14 and the safety/no-invention rules (no invented personal history). | Not sorted | Collecting |
| 16 | Product direction: what users come for | Mark's view: a Representative cannot be given an invented personal history, but users want the wisdom of the tradition's own voices, not a general account of a movement. Clarifies items 14 and 15; also bears on item 8 (answers that describe the group instead of answering). | Not sorted | Collecting |
| 17 | Church Family Tree to Table | Mark's view: users want to reach the multi-voice Table from the Church Family Tree. Today clicking a tradition on the tree opens a single conversation. An earlier attempt failed because choosing one tradition jumped straight to table selection; users want to click all three traditions on the tree first. | Not sorted | Collecting |
| 18 | Church Family Tree: audio | Mark's view: the Family Tree audios are too technical. Idea: voice the short intro at the top of the page as the opening voice, then let users continue to the deeper story. Any new audio is a paid bulk run, so the sample-first rule in CLAUDE.md applies. | Not sorted | Collecting |
