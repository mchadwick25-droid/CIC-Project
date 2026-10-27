# Handoff — lpc: main merged, re-pin, and the project lead's rulings — 2026-10-27

From session: https://claude.ai/code/session_01JMNsSBvi7aVuNvY1ftggwy · World or workstream: `lpc` · Branch / PR: `claude/lpc-next-session-2026-10-26`, [PR #1177](https://github.com/mchadwick25-droid/CIC-Project/pull/1177)

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| `main` (with PR #1175, canon questions) merged into the branch; lpc pinned to the package 2026-10-27T04-46-29Z, written by a parallel session on the same branch (OG-89) | `determinism-check lpc` passes; `records lpc`, `regate lpc`, `claims lpc`, `handoff lpc` pass |
| Gates | `check_live_commentary --enforce` rc 0; `check_paths` 0 new; `texts_registry --check-readme` after `--write-readme`; pytest engine/api, m1, m2, m4, m10: 2862 passed (before the check-in wording change) |
| F4/F5 sent to an engine thread (OG-90, Decision Log) | The project lead's ruling, 2026-10-27 |
| Permanent Prompt alignment deferred until cautions 13 to 17 are tested live | The project lead's ruling, Decision Log |
| Check-in wording fixed in `engine/m4/facilitator_turns.py` ("this tradition" removed; coercion text split) | `pytest -k "check_in or facilitator"` over m4, m5, api: 47 passed |
| Governance V3.6 text drafted for the project lead (OG-91) | Shown as an Artifact; not written to the repo |

## 2. Not done

- **lpc stays `building`.** It is not listed or seated anywhere.
- **Full test suites after the wording change.** Only the check-in tests were rerun; CI on PR #1177 is the full run.
- **Facilitator re-test.** Not this thread's work.
- **Live rerun of the validation probes.** Needs the project lead's named test and cap (not yet given).
- **Carried over.** The OG-73 story `telling` fields, the traditions page, the pre-freeze re-sweep, and Hydatius.

## 3. Re-check before you trust it

- **Cautions 13 to 17 are untested live.** Their effect on Datus's voice is unproven.
- **A parallel session pushed to this branch** while this one worked (a re-pin and a path-baseline change). If another appears, merge it, do not overwrite.
- **Manifest incident.** My merge of a parallel session's re-pin left git conflict markers in `packages/lpc/2026-10-27T04-46-29Z/manifest.json`. PR #1177 merged with that file, so `engine.m2.cli restore` failed on `main` with a JSON decode error. [PR #1182](https://github.com/mchadwick25-droid/CIC-Project/pull/1182) restored the clean file (its hash matches the pin in `records/worlds/lpc.yaml`). After any merge that touches `packages/`, check that every changed manifest parses before pushing. I did not see #1182's engine suite finish.
- **`safety-1.json` in the 27 October reports is not evidence.** It copies the previous probe's report.

## 4. Waiting on Mark

- **A live rerun of the validation probes.** Ruled not now: it waits for the engine thread's F4/F5 fix, then needs a named test and cap.
- **Governance V3.6:** whether and where the two check-in cases enter the document (draft in the Artifact).
- **F4/F5:** now with an engine thread; his answer on the fix options comes back through that thread.

## 5. Next step

Merge PR #1177 once CI is green. Then, when the project lead names a live test and cap, rerun the validation probes against the pinned lpc package.

## 6. Spend

Allowance share used: moderate. Metered: none this session (the 27 October test, $2.21 of $6, was the earlier session's).
