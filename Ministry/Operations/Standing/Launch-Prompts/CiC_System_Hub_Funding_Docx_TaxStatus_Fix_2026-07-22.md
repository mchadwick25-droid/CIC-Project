# Dispatch — Fix stale nonprofit/tax-deductibility claims in Ministry/Funding/ .docx drafts (a real gap in the 2026-07-21 cleanup)

**What this is:** a follow-up correction to the nonprofit-to-PBC cleanup already completed
2026-07-21 (`Ministry/Operations/Standing/Launch-Prompts/CiC_System_Hub_Nonprofit_to_PBC_Cleanup_2026-07-21.md`,
closed the same day — "43 files reviewed, 15 edited, 5 marked superseded, 3 flagged for
Mark"). That sweep was real and thorough, but it ran on a repo-wide **grep**, and grep
cannot see text inside a `.docx` — the content lives zipped inside XML, invisible to a
plain-text search. Confirmed, not guessed: every one of the 43 files listed in that
cleanup's completion entry is `.md` or `.html`. Zero `.docx` files were checked. This
dispatch closes that specific gap.

**Found live, 2026-07-22, in the Funding Strategy thread** (a different active thread,
working through the actual monetization model with Mark — this dispatch is scoped
narrowly to the factual fix below, not to anything that thread is still deciding).

## The two confirmed problems

**1. `Ministry/Funding/CiC_World_Sponsorship_OnePager_V0_1_DRAFT.docx`**

Closing line currently reads: *"Sponsorship is a designated gift (tax-deductible via
the church-fund mechanism now; directly once the nonprofit's determination arrives
~Q1 2027)."*

This is false under the current entity. CiC is Faithways Studio, Inc., a Colorado PBC
(incorporated, Entity ID 20261874960) — no nonprofit filing is happening, no IRS
determination is coming, and PBC gifts have no path to deductibility, retroactive or
otherwise. Same category of claim as the one already corrected on `support.html`
2026-07-21.

**Fix:** replace that sentence with the same honest framing already used on the
corrected `support.html` — contributions are not, and will not become, tax-deductible
under the PBC structure. Don't invent new copy; pull the already-approved language
from `Ministry/Funding/CiC_Go_Live_Cost_Model_V0_1.md` (Part C.3, "where this goes"
language) or match however `support.html`'s giving section now reads.

**2. `Ministry/Funding/CiC_Church_Designated_Fund_OnePager_V0_1_DRAFT.docx`**

This one is more than a sentence fix — flag it rather than silently resolve it, per
the original cleanup prompt's own rule ("anything requiring real judgment gets flagged,
not decided"). The entire document's premise is a church hosting a designated fund
*specifically to bridge donors to future tax-deductibility* once CiC's own 501(c)(3)
lands. Under a PBC, that destination doesn't exist — there's no future determination
to bridge to, so the mechanism this document describes may not make sense in any form
anymore, not just in its wording. Don't rewrite this one — mark it superseded (bucket
2 from the original cleanup's own convention) and flag back to the Funding Strategy
thread / Mark: does a designated-fund-via-a-partner-church mechanism still have a
purpose without a deductibility bridge (e.g., simple pass-through convenience for a
church that wants to give collectively), or should it just be retired.

## Also check, not yet verified either way

Same blind spot could affect the rest of `Ministry/Funding/*.docx` — none of these were
covered by the grep-based sweep and none have been read in full since the PBC pivot:

- `CiC_Growth_Plan_V0_1_DRAFT.docx`
- `CiC_Ministry_Funding_Strategy_v1_0.docx`
- `CiC_Ministry_Proposal_Packet_V0_1_DRAFT.docx`
- `CiC_Org_Funding_Bridge_Memo_V0_1_DRAFT.docx`
- `CiC_Wabash_Pilot_OnePager_V0_1_DRAFT.docx`
- `CiC_Seminary_Alignment_Analysis_V0_1_DRAFT.docx` (partially read 2026-07-22 in the
  Funding Strategy thread — no stale claim spotted in the portion read, but it was not
  read in full; the document is long and table-heavy)

Same three-bucket sort as before: dated decision-log-style content stays untouched,
standalone-obsolete gets a superseded banner, live/mixed content gets a surgical fix.

## Method — handle with real care, this project has been burned by raw Office-file edits before

Do not hand-edit the zipped XML directly. Use this project's own `docx` skill/tooling
for any edit inside a `.docx`, and verify the file opens clean afterward (re-read it
back, don't just trust the write succeeded). `CiC_Phase1_Budget_V0_1_DRAFT.xlsx` was
found corrupted on-disk after a prior raw edit (2026-07-08 entry, Org Funding Decision
Log) — recovered, but it's a real, already-happened failure mode in this exact repo,
not a hypothetical caution.

## Explicitly out of scope

Don't touch the $3,500 sponsorship figure, program mechanics, or any part of the
funding *strategy* itself — that's actively being worked out live with Mark in the
Funding Strategy thread right now. This dispatch is strictly the factual tax/entity-
status correction, same boundary the original cleanup prompt held.

**Also worth holding explicitly (Mark's standing instruction, 2026-07-22):** fixing the
tax-status line does not make either document "finished" or ready to actually send to a
donor or church. Every pre-PBC draft in `Ministry/Funding/` and
`Ministry/Communication/` is source material only until Mark reworks and confirms it —
this dispatch removes one factual error, it does not promote the document's status.
Report the fix as a correction, not as "ready to use."

**One related item, FYI only, not part of this dispatch:** the original cleanup's own
flagged item #2, `CiC_Funder_Landscape_V0_2_2026-07.md`, still needs a real strategic
reassessment (its funder table is mostly grants gated on 501(c)(3) status). That's a
bigger call than a fact patch and belongs to the Funding Strategy thread's own work,
not this dispatch.

## Completion criteria

Same pattern as the 2026-07-21 cleanup's own completion entry: a dated log entry in
`CiC_System_Hub_Decision_Log.md` listing every file touched and which bucket it fell
into, plus the Church-Designated Fund flag carried forward explicitly rather than
quietly resolved.
