# World Build Queue

Fleet-wide construction status, separate from `records/worlds.yaml` (which is the governed admission ledger and only reflects a world after it's already built). This file tracks a world *before* that point — queued, mid-build, or blocked — so status is visible at a glance across many concurrent builds without opening each world's own folder.

Statuses: `queued` · `drafting` · `blocked-source` · `blocked-identity` · `blocked-escalation` · `complete` (built, ready for `worlds.yaml` admission)

Update this file as part of any session that changes a world's status — it's a status board, not a replacement for that world's own `Open_Gaps_Tracking.md` or `Decision_Log.md`.

| World | Status | Current stage | Blocked on | Notes |
|---|---|---|---|---|
| Fixture World (fix) | complete | — | — | synthetic, in `worlds.yaml` |
| Alexandrian Christianity (alx) | complete | — | — | admitted, in `worlds.yaml` |
| Desert Monasticism (desert) | complete | — | — | admitted, in `worlds.yaml` |
| Post-Apostolic Household-Church (pahc) | complete | — | — | admitted, in `worlds.yaml` |
| Hieronymian Ascetic-Literary (hal) | complete | — | — | admitted, in `worlds.yaml` |
| Syriac Christianity (syr) | complete | — | — | admitted, in `worlds.yaml` |
| Imperial and Juridical Christianity (ijc) | complete | — | — | admitted, in `worlds.yaml` |
| Cappadocian Christianity (cappadocian) | complete | — | — | admitted, in `worlds.yaml` |
| Donatism (don) | complete | — | — | built, in `worlds.yaml` |
| Second-Century Greek Apologists | drafting | Step-0 merged (candidate) | — | status needs confirming against current `World-Builds/` contents before resuming |
| Latin Apologists | drafting | Step-0 merged (candidate) | — | status needs confirming against current `World-Builds/` contents before resuming |
| Latin Pastoral-Congregational Christianity | queued | not yet started | — | folder exists under `World-Builds/`; confirm actual progress before assuming "queued" |
| Gallic Monastic-Ascetic Christianity | queued | not yet started | — | folder exists under `World-Builds/`; confirm actual progress before assuming "queued" |

Add a row per new world as it's queued. The four rows above with "status needs confirming" weren't independently re-verified stage-by-stage when this file was created — check each world's own folder before trusting the row.
