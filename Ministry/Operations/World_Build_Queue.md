# World Build Queue

Fleet-wide construction status, separate from `records/worlds.yaml` (which is the governed admission ledger and only reflects a world after it's already built). This file tracks a world *before* that point — queued, mid-build, or blocked — so status is visible at a glance across many concurrent builds without opening each world's own folder.

Statuses: `queued` · `drafting` · `blocked-source` · `blocked-identity` · `blocked-escalation` · `complete` (built, ready for `worlds.yaml` admission)

Update this file as part of any session that changes a world's status — it's a status board, not a replacement for that world's own `Open_Gaps_Tracking.md` or `Decision_Log.md`.

**Cost column**: API-rate-equivalent value from that world's build session(s) (via session lookup), not an actual charge — useful for comparing worlds' relative cost and, over time, for measuring whether process changes are actually reducing per-world cost. Fill in when known; leave blank otherwise rather than guessing.

| World | Status | Current stage | Blocked on | Known cost (API-equiv) | Notes |
|---|---|---|---|---|---|
| Fixture World (fix) | complete | — | — | — | synthetic, in `worlds.yaml` |
| Alexandrian Christianity (alx) | complete | — | — | — | admitted, in `worlds.yaml` |
| Desert Monasticism (desert) | complete | — | — | — | admitted, in `worlds.yaml` |
| Post-Apostolic Household-Church (pahc) | complete | — | — | — | admitted, in `worlds.yaml` |
| Hieronymian Ascetic-Literary (hal) | complete | — | — | — | admitted, in `worlds.yaml` |
| Syriac Christianity (syr) | complete | — | — | — | admitted, in `worlds.yaml` |
| Imperial and Juridical Christianity (ijc) | complete | — | — | — | admitted, in `worlds.yaml` |
| Cappadocian Christianity (cappadocian) | complete | — | — | — | admitted, in `worlds.yaml` |
| Donatism (don) | complete | — | — | ~$603 (2 sessions) | built, in `worlds.yaml` |
| Second-Century Greek Apologists | drafting | Step-0 merged (candidate) | — | — | status needs confirming against current `World-Builds/` contents before resuming |
| Latin Apologists | drafting | Step-0 merged (candidate) | — | — | status needs confirming against current `World-Builds/` contents before resuming |
| Latin Pastoral-Congregational Christianity | drafting | not yet in `worlds.yaml`; last build session updated 2026-09-10 | — | ~$825 (2 sessions) | corrected 2026-09-10: was wrongly marked "queued, not started" — real build sessions already exist |
| Gallic Monastic-Ascetic Christianity | drafting | not yet in `worlds.yaml`; last build session updated 2026-09-10 | — | ~$689 (1 session) | corrected 2026-09-10: was wrongly marked "queued, not started" — real build session already exists |

Add a row per new world as it's queued. The two "Apologists" rows still weren't independently re-verified stage-by-stage — check each world's own folder before trusting the row.
