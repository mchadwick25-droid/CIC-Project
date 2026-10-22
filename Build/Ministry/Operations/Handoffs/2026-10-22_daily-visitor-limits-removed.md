# Handoff — daily visitor limits removed — 2026-10-22

From session: https://claude.ai/code/session_014kMdzhac3pg4njANzhBJ2m · World or workstream: engine/api free allowance · Branch / PR: claude/remove-daily-visitor-limits-2026-10-22, draft PR (see Pilot_Feedback_Log.md)

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Daily conversation and message counts, Facilitator-only sitting and paid sitting removed from engine/api and engine/m4 | Targeted tests pass (anon_cap, feedback, round, grants, deeper seam, deeper proofs, safety-before-refusals: 156 + 110 passed). Full runs below |
| New tests: six conversations in a day all voiced; failed first reply uses nothing up | `test_deeper_seam.py`, names in the proofs list in `test_deeper_proofs.py` |
| Safety at every limit | `test_a_safety_route_is_answered_at_every_limit` passes with the limits that remain |
| Pilot feedback log entry | `Pilot_Feedback_Log.md`, last section |

## 2. Not done

- `cic-website/privacy.html` cookie section: draft words await Mark (Artifact https://claude.ai/artifact/BGbQsSSHFhpAtU4dYe4fsC).
- Render variables `CIC_API_ANON_DAILY_SESSION_LIMIT` and `CIC_API_ANON_DAILY_TURN_LIMIT` are dashboard-only: Mark deletes them.
- Job 2 (accounts) was taken out of this thread's scope by Mark.

## 3. Re-check before you trust it

- Full suite results with Go Deeper off and on — see the PR description.
- Old docs and audits (`Build/Ministry/Operations/Audits/…Anon-Cap-Safety-Interaction.md`, Go Deeper turn-on runbook) still describe the daily counts as history; not edited.

## 4. Waiting on Mark

- Privacy page words — Artifact above.
- Promotion of main to live, through the promotion runbook. Promote the privacy change with the engine change.
- Clearing the cookie gives a fresh free allowance; only burst limits and the door hold that back now. Say if that needs a limit.

## 5. Next step

Mark approves or edits the privacy words; apply them to `cic-website/privacy.html` and `assets/privacy-go-deeper.js` if needed.

## 6. Spend

Allowance share used: small, Sonnet only. Metered: none.


## Addendum — visitor bound built (same day)

- Branch `claude/visitor-bound-2026-10-22`: the monthly count (100 a visitor, 200 a network), the fixed Facilitator line past it with no model call, the network free window of 5 allowances, and pilot and admin grants at $0 toward the door. Details and dollars: `Pilot_Feedback_Log.md`, "Visitor bound built".
- Mark approved both sets of words (the line and the privacy sentence) on 2026-10-22.
- Check before trusting: the free-voice dollar figure comes from the repo's own measurements ($0.041 to $0.088 a solo round), not the live usage log.
- Waiting on Mark: promotion of main to live, which must carry the privacy sentence with the engine change; his AWS Budget check.


## Addendum 2 — free 3-round rule removed (same day)

- Branch `claude/free-rounds-removed-2026-10-22`: a free conversation is limited by the visitor's tokens and the engine's own caps (10 solo rounds, 3 at a Table). Details, the page words and the cost with its unmeasured part: `Pilot_Feedback_Log.md`, "Free 3-round rule removed".
- Waiting on Mark: promotion of main to live, which must carry the Go Deeper page change with the engine change.
- Check before trusting: the cost per long free round is unmeasured against the live usage log (finding F11).
