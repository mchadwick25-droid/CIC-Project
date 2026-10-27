# Handoff — engine: the other items from the lpc live review (F17, F18, F23, F24) — 2026-10-27

From session: https://claude.ai/code/session_01JMNsSBvi7aVuNvY1ftggwy · World or workstream: fleet engine (found in `lpc`) · Branch / PR: none yet; the engine thread opens its own

For the engine thread that takes F4/F5 (`Build/Ministry/Operations/Handoffs/2026-10-27_engine-post-draft-sentence-removal-f4-f5.md`). These four are smaller, independent of F4/F5, and all P2. Logged as OG-92 in `Build/worlds/lpc/Open_Gaps_Tracking.md`. The `lpc` build thread changed no engine code for them. F25 (a fleet question) is at the end.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| The four items were found in a live test, "lpc full validation, 27 October" ($2.21 of a $6 cap) | `Build/worlds/lpc/Review-Artifacts/Live_Validation_Review_2026-10-27.md` (F17, F18, F23, F24); reports in `engine/m4/reports/lpc-validation-2026-10-27/` and `engine/m3/reports/live-admission-report-lpc-2026-10-27.json` |
| The code behind each was located and, for F24 and F23, partly confirmed by reading | Details in section 4. Nothing was run and no engine code was changed. |

## 2. Not done

- **No reproduction and no fix for any of the four.**
- **F18 and F17 are not confirmed.** Section 4 says what is known.
- **No count across worlds.** The review covers `lpc` only. Whether other worlds show the same faults was not checked.

## 3. Re-check before you trust it

- **Each cause below is a reading of the code and the review, not a run.** Open the named probe report first and see the symptom, then the code.
- **The review's root-cause statements are the Opus reviewer's.** Where the build thread checked one, section 4 says so.

## 4. The items

### F24, doubled quotation marks (best understood)

Symptom: register-8 shipped `““Lay this body anywhere... wherever you are.””`; laundering-2 and register-7 had broken nested marks.

Confirmed by reading: the quote record `lpc.quote.remember-me-at-the-lords-altar` has a `modern_rendering` that itself begins with “ and ends with ”. `engine/m4/quote_placement.py` (about line 152) composes `{lead} “{rendering}” [[id]]`, so the outer marks double. `_settable` then checks that the quoted span equals the rendering.

Also checked: 26 of `lpc`'s quote renderings contain curly quotation marks. Four of them, including this one, start with one: `lpc.quote.remember-me-at-the-lords-altar`, `lpc.quote.believe-and-thou-hast-eaten-already`, `lpc.quote.the-old-man-nailed-to-the-cross-speaks`, `lpc.quote.they-went-out-from-us-but-were-not-of-us`. The rest carry marks inside the text, which `_settable` and the nested-quote handling must also cope with.

The design question for the engine thread: whether a rendering may carry outer marks at all. If not, a record-side fix (strip the outer marks) belongs to the `lpc` thread and a fleet check should reject them; if so, the engine should not wrap again. Ask the project lead before changing the fleet rule on renderings; the `lpc` thread can do the four record edits on request.

### F23, a later event explained (confirmed as design, effect unconfirmed)

Symptom: anachronism-1 explained Chalcedon (451) and its two-natures ruling; the window closes in 430. `output_defects` carried the finding "names the year 451, after the window closes in 430", and grounding marked several sentences "withhold", yet the reply shipped unchanged.

Read: `engine/m4/output_check.py` is written to report and never edit ("REPORTS, NEVER EDITS" in its header), so a horizon finding is a signal only. `_horizon_findings` is at about line 397. The grounding net's own removal loop in `engine/m4/turn.py` (about lines 355 to 395) removes only sentences whose `why` is in `grounding_net.QUOTATION_DROP_REASONS`; other "withhold" reasons are handled in `grounding_net.shown_text`, which I did not read.

To settle: which "withhold" reasons actually remove text, and whether a horizon finding should ever block or trigger a redraft. The review asks whether the net runs observe-only on staging; I found a flag for the uncited-claims check (`CIC_R27_ENFORCE`, `engine/api/config.py` line 174) but did not find one for the horizon finding. That is a design decision for the project lead if the answer is "report only by design".

### F17, weak citations (not confirmed)

Symptom: register-3 cites "five presbyters" and "venom" to `lpc.story.election-of-cyprian`, which has neither (they are in `lpc.force.congregational-acclamation-overriding-preference` and `lpc.quote.ancient-venom-against-my-episcopate`); anachronism-3 cites `lpc.term.heresy` for a council's ruling.

The review's cause: citation attach on word overlap. Pointers: `engine/m4/grounding_net.py`, the tag-overlap branch in `check_turn` (about lines 1330 to 1380, comments mention "the tag-overlap branch"). Not read in full.

### F18, a limit record pasted into unrelated answers (unconfirmed)

Symptom: `lpc.limit.ordinary-interior-life` appears in answers about other subjects (safety-3, Deep Interview turn 7, admission f3-p, f4-t, f6-e, f6-p). The review blames the record's retrieval scope.

Read: that record is assigned to one canon cell only (F5-I). `engine/m4/evidence.py` (about line 860) includes a cell's honest-limit records unconditionally for the matched cell, and a cell match needs just two shared words with the question (`_MIN_ASK_MATCH_WORDS = 2`, about line 100). So a loose cell match is the likelier cause than the record's scope. Not tested. A fleet matter if so. The review also notes the Permanent Prompt's "do not explain the silence" wording is echoed by the voice (a change-order matter, not this thread's).

## 5. Waiting on Mark

- **F24:** whether a quote rendering may carry outer quotation marks.
- **F23:** whether a horizon finding should only report, or block or redraft.
- **F25 (fleet question, not an engine fix):** "Are you an AI?" is answered by the Facilitator's system-nature turn, but Doc_10 section 7 and the Permanent Prompt expect Datus to say one sanctioned sentence. One of the two is stale.

## 6. Next step

Open `engine/m4/reports/lpc-validation-2026-10-27/register-8.json`, read the placed sentence, and write a failing test with `lpc.quote.remember-me-at-the-lords-altar` through `quote_placement.place_quotes`. That is the cheapest of the four to reproduce and settles the rendering question. Offline tests only; any live rerun needs the project lead's named test and cap.

## 7. Spend

Allowance share used: small (reading only). Metered: none.
