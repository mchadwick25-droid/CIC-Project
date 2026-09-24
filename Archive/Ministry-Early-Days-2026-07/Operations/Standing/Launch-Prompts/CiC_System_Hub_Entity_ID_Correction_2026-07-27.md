# Dispatch — Correct the false-incorporation entity ID (20261874960) with the real one (20261918758) across 11 files

**What happened:** the Colorado state registration that produced "Entity ID 20261874960" and was
recorded across this project as confirmed incorporation **never actually completed.** Mark got an
on-screen verification at the time, but no receipt was ever issued. When he called the Secretary
of State's office, they suggested an address mismatch as the likely cause. He refiled from
scratch on 2026-07-27, this time verifying with a real email receipt and a public-record search
before treating it as done.

**The real, confirmed registration, verified two ways (email receipt + public record search),
not a repeat of last time's mistake:**

| Field | Value |
|---|---|
| Entity name | Faithways Studio, Inc. |
| ID Number | **20261918758** |
| Document Number | 20261918758 |
| Event | Articles of Incorporation |
| Status | **Good Standing** |
| Form | DPC-PBC (confirms the Public Benefit Corporation election was captured correctly, not just a generic profit corp) |
| Formation Date | **07/27/2026** |

## Files found citing the old, wrong ID (20261874960) — 11 total, real repo-wide grep, not a guess

1. `Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`
2. `Ministry/Operations/Standing/CiC_Task_Board_2026.md`
3. `Ministry/Operations/Standing/CiC_Dashboard.html`
4. `Ministry/Operations/Standing/CiC_Gantt_Visual.html`
5. `Ministry/Operations/Standing/CiC_Acceleration_Gantt_2026.gan`
6. `cic-website/README.md`
7. `Ministry/Operations/Standing/Launch-Prompts/CiC_System_Hub_Funding_Docx_TaxStatus_Fix_2026-07-22.md`
8. `Ministry/Operations/Standing/Launch-Prompts/CiC_System_Hub_Sync_Update3_2026-07-21.md`
9. `Ministry/Organization/CiC_Nonprofit_Formation_Decision_Log.md`
10. `Ministry/Organization/CiC_PBC_Bylaws_and_Organizational_Resolutions_V0_1.md`
11. `Ministry/Organization/CiC_PBC_IP_Assignment_Agreement_V0_1_DRAFT.md`

## How to sort them — reuse the three-bucket convention already established in this project

(Same convention as the 2026-07-21 nonprofit-to-PBC cleanup and the 2026-07-22 docx tax-status
fix — dated history stays dated history, live trackers get corrected directly, anything
substantive gets real judgment, not a blanket find-and-replace.)

**Bucket 1 — dated decision-log / launch-prompt entries (files 1, 8, 9, and any dated entries
inside file 7): leave the historical narrative as-is, add a dated correction note.** These
recorded what was believed true at the time — that's accurate history of the *belief*, not an
error to erase. Add a short 2026-07-27 addendum: the ID they cite was never real, here is the
actual confirmed one, cross-reference this dispatch.

**Bucket 2 — live status trackers (files 2, 3, 4, 5, 6): correct directly.** These represent
current state, not history — the Task Board, Dashboard, both Gantt files, and the website README
should simply show the real, current ID and formation date. No addendum needed, just fix it.

**Bucket 3 — real operative legal documents (files 10, 11): ALREADY RESOLVED, 2026-07-27, in the
Funding Strategy thread — do not duplicate this work.** Both documents were read in full and did
turn out to have exactly the sequencing problem this dispatch anticipated: the Bylaws &
Organizational Resolutions' Step 1 signature block and the IP Assignment Agreement's own
"Incorporation Date" effective-date clause were both explicitly dated July 21, 2026 / Entity ID
20261874960 — the failed attempt. Both have been corrected in place to July 27, 2026 / Entity ID
20261918758, with a dated correction note preserved in each explaining what changed and why (same
convention as the rest of this dispatch — the error is noted, not silently erased). **Remaining
real-world step, not a document-editing one:** Mark should confirm whether either document was
already physically signed with the old, incorrect date — if so, both need to be re-signed with the
corrected date before being relied on for bank/Stripe account setup, since the Organizational
Resolutions' Step 2 is the specific paragraph authorizing that. No further action needed on these
two files as part of this dispatch.

## Explicitly out of scope

No other content in these files should change — voice, structure, unrelated decisions all stay
untouched. This is strictly the entity-ID/formation-date correction and the sequencing check in
Bucket 3.

## Completion criteria

Same pattern as the 2026-07-21 cleanup and the 2026-07-22 docx fix: a dated log entry in
`CiC_System_Hub_Decision_Log.md` listing every file touched and which bucket it fell into. Bucket
3 (files 10, 11) is already done — see the note above — so this dispatch's real remaining scope is
files 1–9 only.
