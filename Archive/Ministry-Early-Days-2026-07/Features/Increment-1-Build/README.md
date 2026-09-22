# Increment 1 Build

**What this is:** the execution thread for Increment 1 — applying the
finalized brand system and the clutter budget to the conversation screen
that already runs, before any new participant feature attaches. Distinct
from `Full-UX-Design/`, which designed it; this folder is where it actually
gets built.

**The spec:** `../Full-UX-Design/Design/CiC_Build_Handoff_Increment1_V1_0.md`
— implementation-ready, not repeated here.

**Current state:** all six commits built and verified against the real app
(2026-07-20) on branch `claude/increment1-build-brand-floor` — see
`Decision-Log.md` for what shipped, the deviations reasoned through along
the way, one pre-existing gap found and flagged (not fixed), and the
merge-timing question handed back to System Hub/Mark. Not merged into
`main`.

**Where deliverables land once integrated:** `cic-poc/frontend/`, on its own
branch until the merge-timing question in the launch prompt is resolved.
