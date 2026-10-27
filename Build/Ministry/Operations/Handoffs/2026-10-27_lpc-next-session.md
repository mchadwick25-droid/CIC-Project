# Handoff — lpc: where the world stands and what the next session does — 2026-10-27

From session: https://claude.ai/code/session_01JMNsSBvi7aVuNvY1ftggwy · World or workstream: `lpc` (Latin Pastoral-Congregational Christianity, c. 246–430; Representative Datus) · Branch / PR: start a new branch from `origin/main`; the previous branch's PRs (#1174, #1177, #1182, #1183, #1186) are all merged

Read `Build/Ministry/Operations/Handoffs/2026-10-27_lpc-merge-repin-and-rulings.md` for this session's detail, and `Build/Ministry/Operations/Handoffs/2026-10-27_engine-post-draft-sentence-removal-f4-f5.md` for the engine thread's brief. This file says what to do next.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| lpc is at state `building`, pinned to the package 2026-10-27T04-46-29Z (manifest hash starting `33600aec`), built after the canon-questions change | `determinism-check lpc` pass; `records`, `regate`, `claims`, `handoff lpc` pass; the manifest parses on `main` (see the manifest incident in the 2026-10-27 merge handoff) |
| Datus's world-level findings F6 to F13 fixed in the records and in world_core cautions 13 to 17; safety-routing guards removed from the records | `Review-Artifacts/Datus_Findings_Fix_Review_2026-10-27.md`, round 3 Approved to proceed; OG-88 |
| Facilitator check-ins for loss to suicide and for coercion by a person; wording fixed for tables and the long sentence split | PR #1174 with its review; wording change tested with `pytest -k "check_in or facilitator"` over m4, m5, api (47 passed) and m4 plus m5 (1070 passed) |
| Rulings by the project lead, 2026-10-27, all in `lpc_Decision_Log.md`: F4/F5 to an engine thread (OG-90); Permanent Prompt not aligned yet; check-in wording fixed; governance V3.6 text drafted for him; no live rerun yet | Decision Log entries; OG-90, OG-91 |

## 2. Not done

- **lpc is not listed or seated.** It stays `building` until the Facilitator's routing re-test passes and the world clears validation.
- **P2 findings F14 to F26 from the live review.** OG-88 records F6 to F13 as fixed. I did not find a record that F14 to F26 were addressed, and did not check. Root causes the review gives: F14 (Candida called "fallen") is a record fault, the caveat sits only in `absent_detail`; F15 and F19 are voice; F17, F23, F24 and F25 are engine; F16, F18, F20, F21, F22 and F26 name no single cause in my extract, so read the review. The records-side items are this thread's.
- **Live rerun of the validation probes.** Needs the project lead's named test and cap, and he ruled it waits for the F4/F5 engine fix.
- **Carried from the 2026-10-26 handoff, untouched:** the OG-73 story `telling` fields and the first traditions page; the pre-freeze re-sweep; Hydatius, its placement in the Library.
- **OG-84 and OG-85.** The Sermon on the Mount has no Latin vendored; a fleet canon question on suicide is with the project lead. I did not re-check either.

## 3. Re-check before you trust it

- **Cautions 13 to 17 are untested live.** Their effect on Datus's voice is unproven. Do not report them as working.
- **`safety-1.json` in the 27 October reports is not evidence.** It is a copy of the previous probe's report, because that run crashed. Track A (hopelessness) has no recorded result.
- **The F4/F5 root cause is the Opus reviewer's reading,** confirmed only by a read of the code, not by running it. The engine thread owns it.
- **A parallel session pushed to the same branch last time.** Fetch before you push, and merge what is there. After any merge that touches `packages/`, check every changed `manifest.json` parses before pushing.
- **Rebuild if the canon or engine inputs change.** If anything merges to `main` that changes lpc's package inputs (for example another canon change), rebuild, re-pin and determinism-check lpc. Restore every pinned package before the engine and api tests.

## 4. Waiting on Mark

- **Governance V3.6.** Whether and where the two check-in cases enter the document. The draft was shown as an Artifact (https://claude.ai/artifact/8HFgVwaS2juMcrpWj9jVXK); OG-91.
- **Live rerun.** A named test and a cap, once the F4/F5 fix is in.
- **The Permanent Prompt.** The question returns after a live test of cautions 13 to 17 (Decision Log, 2026-10-27).
- **Promotion to live.** His alone, through `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md`.

## 5. Next step

Read the P2 table in `Build/worlds/lpc/Review-Artifacts/Live_Validation_Review_2026-10-27.md` (F14 to F26) and sort each finding into: record fix for this thread, voice fix through world_core, or engine fault to hand on. Then fix the record items, one subagent at a time (Sonnet drafts, Opus writes any modern renderings and reviews), rebuild, re-pin, and run the gates. Log each gap in `Open_Gaps_Tracking.md` and each ruling in the Decision Log.

## 6. Spend

Allowance share used: moderate this session. Metered: none this session. The earlier live test "lpc full validation, 27 October" spent $2.21 of its $6 cap; no further spend is approved.
