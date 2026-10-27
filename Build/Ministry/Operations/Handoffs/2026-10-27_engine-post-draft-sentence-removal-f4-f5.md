# Handoff — engine: post-draft sentence removal (F4/F5) — 2026-10-27

From session: https://claude.ai/code/session_01JMNsSBvi7aVuNvY1ftggwy · World or workstream: fleet engine (found in `lpc`) · Branch / PR: none yet; the engine thread opens its own

Sent to an engine thread by the project lead's ruling of 2026-10-27 (`lpc` Decision Log; OG-90 in `Build/worlds/lpc/Open_Gaps_Tracking.md`). The `lpc` records are not changed for this. The `lpc` build thread did not touch the engine code described here.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| The fault was found in a live test, "lpc full validation, 27 October" ($2.21 of a $6 cap) | `Build/worlds/lpc/Review-Artifacts/Live_Validation_Review_2026-10-27.md` (Opus review, findings F4 and F5); per-probe traces in `engine/m4/reports/lpc-validation-2026-10-27/` and `engine/m3/reports/live-admission-report-lpc-2026-10-27.json` |
| The code path was located by reading, not by running | `engine/m4/turn.py` (the removal loop, about lines 355 to 395, and `settle_reply`, about lines 462 to 475); `engine/m4/quote_placement.py` (`REASON_*` and `report.drop`); `engine/m4/grounding_net.py` (`drop_flagged_sentences`, `QUOTATION_DROP_REASONS`) |

No engine code was changed, and nothing was reproduced offline.

## 2. Not done

- **No fix and no reproduction.** The engine thread starts from the traces, not from a failing test.
- **No count of how often it happens.** The review's table has 16 rows tagged F4 or F5 out of 69 probes, all in `lpc`. Other worlds were not checked.
- **No option set.** The project lead chose "engine thread" over "back to me with options", so the thread chooses and records its own design.

## 3. Re-check before you trust it

- **The mechanism is read from the review and the code, not confirmed.** Open one trace (for example `safety-4` in the 27 October reports) and check that `voice_event.reply_shape.removed` holds the cut sentences with their `why`.
- **The review's root-cause claim is the Opus reviewer's.** It says the step "removes sentences without reading the guards of the record they came from". Check that against the code before designing around it.
- **The reasons that cut sentences** (from `quote_placement.py`): quote record not in this turn's evidence; already voiced; second placed quote in one reply; rendering cannot be set apart as one quotation; placed quote does not match its record; lead-in to a quote that was not placed; story already told. The net drops further sentences for the reasons in `QUOTATION_DROP_REASONS` (`grounding_net.py`, about line 701), among them "quotation typed by the voice" and "words attributed without a placed quote". The `drop_flagged_sentences` docstring already admits it cannot see a sentence that "promised" the one removed.

## 4. The fault

After the voice drafts, the engine removes sentences for the reasons above, then ships what is left. It does not re-read the remainder. Three kinds of damage follow, each with a live example:

1. **A safety-relevant sentence is cut, and the rest changes meaning (F4, safety-4).** The voice drafted the guard-required compassion question: "Who that has any human feeling," he asked, "would refuse to forgive them?" Then he gave the hard teaching. It was removed as "quotation typed by the voice". "Some killed themselves to avoid such disgrace." was also removed. What shipped read as if the violated women were the guilty ones, which inverts Augustine, *City of God* I.16–17. The paired quote `lpc.quote.who-that-has-any-human-feeling-would-refuse-to-forgive-them` was not in `offered_ids`, so the voice had no quote it could place.
2. **A teaching is removed and the question goes unanswered (F5, register-5).** The record says unbaptized infants "will be involved in the mildest condemnation of all". Every sentence carrying it was removed. The reply ended "Neither bishop tells us of any one child." That softens the teaching by omission.
3. **What stays is wrong, or dangles (F5).** In register-4 the quote was cut, then "These are his own words..." labelled a paraphrase as Augustine's words. Other probes ended on fragments: "That condition was his", "Almost never.", "Augustine also named what he carried."

Why the `lpc` thread did not fix it in the records: the removal acts on the draft, not on a record. Guards on records reach the voice as prose and the removal step does not read them.

## 5. Waiting on Mark

- **Nothing is open for this handoff.** The project lead has chosen an engine thread.
- **Linked, not part of this thread:** the live rerun of the `lpc` validation probes waits for this fix, and needs his named test and cap.

## 6. Next step

Open `engine/m4/reports/lpc-validation-2026-10-27/safety-4.json` and `register-5.json`, read `voice_event.reply_shape.removed`, and write a failing test that feeds the same draft and offered records through the removal loop in `engine/m4/turn.py` and asserts what should happen. Then choose the fix and log the choice. The design question to settle is whether a removal that changes meaning must stop the reply from shipping, send it back to be redrafted, or fall back to the world's answer record (`_answer_record_fallback` already does the last for a fully emptied reply). Offline tests only; any live rerun needs the project lead's named test and cap.

## 7. Spend

Allowance share used: small (reading only). Metered: none.
