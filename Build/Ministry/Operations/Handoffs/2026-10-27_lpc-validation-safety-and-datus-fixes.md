# Handoff — lpc: live validation, safety routing, Datus fixes — 2026-10-27

From session: https://claude.ai/code/session_01GLotrvxvHBTEd81NaezC2i · World or workstream: `lpc` · Branch / PR: `claude/lpc-next-session-2026-10-26`, the open PR for the Datus-findings fix (see the last merged PRs: #1160, #1161, #1166, #1168, #1174)

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Records marked ready; package built and pinned; Representative named in the registry | `records lpc` PASS; determinism-check pass; PRs #1160, #1161, #1166 merged |
| Live test "lpc full validation, 27 October" ($2.21 of the $6 cap) | Reports in `engine/m4/reports/lpc-validation-2026-10-27/` and `engine/m3/reports/live-admission-report-lpc-2026-10-27.json`; Opus review `Review-Artifacts/Live_Validation_Review_2026-10-27.md` (Revise; OG-87) |
| Only built worlds are listed or seated, with or without admission enforcement | PR #1168 merged; engine/api 1054 passed |
| Facilitator check-in for loss to suicide and for coercion by a person, approved by the project lead | PR #1174 merged; Opus review and round-2 recheck (Approved to proceed); 2500 engine tests passed |
| Safety-routing guards removed from lpc records; Datus's findings F6 to F13 fixed in the records and world_core | `Review-Artifacts/Datus_Findings_Fix_Review_2026-10-27.md`; gates pass; package re-pinned to `packages/lpc/2026-10-27T04-46-29Z` |

## 2. Not done

- **lpc stays `building`.** It is not listed or seated anywhere.
- **Facilitator re-test.** The project lead ruled this is not this thread's.
- **F4/F5, engine.** The sentence-removal step damaged answers. This is a fleet engine fault, not yet put to the project lead with options.
- **Not rerun live.** The validation probes have not been rerun since the fixes. Any rerun needs the project lead's named test and cap.
- **Carried from the 2026-10-26 handoff.** The OG-73 story `telling` fields, the traditions page, the pre-freeze re-sweep, and Hydatius.

## 3. Re-check before you trust it

- **The new cautions (13 to 17) are untested live.** Their effect on the voice is unproven.
- **PR #1175 (canon questions) also re-pins lpc.** If it merges after this branch, rebuild and re-pin lpc again.
- **`safety-1.json` in the 27 October reports is not evidence.** It is a copy of the previous probe's report, because that run crashed.

## 4. Waiting on Mark

- **The Permanent Prompt.** Whether to bring it in line with cautions 13 to 17, by change order.
- **The check-in wording.** "this tradition" at tables, and the 29-word coercion sentence.
- **F4/F5.** Whether this goes to an engine thread, or comes back to him with options.
- **The governance document.** `CiC_L3D_Facilitator_Governance_V3.6` should name the two new check-in cases.

## 5. Next step

Merge the open Datus-findings PR once CI is green. Then put F4/F5 to the project lead with options, and take his answers on section 4.

## 6. Spend

Allowance share used: heavy (two long days, many Sonnet and Opus subagents). Metered: $2.21 on "lpc full validation, 27 October" (cap $6); nothing else.
