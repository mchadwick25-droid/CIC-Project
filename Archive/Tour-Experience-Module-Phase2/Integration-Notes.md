# Integration Notes — Tour Experience Module (Phase Two)

Still no code, no branch, no integration target chosen — this remains a pre-build
planning thread. **Update, 2026-07-20 (TR-4, TR-5):** two further planning artifacts
now exist alongside the strategy doc — `CiC_L4_Tour_Manifest_Template_V1_0.md` and
`CiC_Tour_Eligibility_Gate_V1_0.md`, both filed in this same folder. Neither touches
`cic-poc`, a branch, or any integration target; both are builder-machine documents
(template + checklist), the category the Hosted-Tour thread's own Integration-Notes.md
already names as "startable with zero live-system risk." The actual `cic-poc`
integration point these two artifacts point toward — a `tour_manifest.py` sibling to
`world_manifest.py` — does not exist yet; confirmed by direct directory listing of
`cic-poc/backend/app/` (2026-07-20), which has `world_manifest.py` but nothing
tour-related. That remains TR-14's own future work, correctly BLOCKED on Increment 1
and Increment 2 per the Task Board.

**Update, 2026-07-20 (later same day):** the concrete design for that future work now
exists — `CiC_Tour_Build_Spec_V0_1_DRAFT.md` — but still no code, no branch. Written
explicitly for later implementation; the actual gate list (Increment 1 + 2, a real
reviewed Tour Manifest, the validation-suite extension) is unchanged. Update this file
again once Phase Two work actually starts touching code.
