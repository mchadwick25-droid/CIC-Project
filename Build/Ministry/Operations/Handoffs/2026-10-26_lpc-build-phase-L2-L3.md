# Handoff — lpc build, Phases L2 and L3 — 2026-10-26

From session: https://claude.ai/code/session_01PdSKYEGnPNVAntVFg5ZReR · World or workstream: `lpc` (Latin Pastoral-Congregational Christianity, c. 246–430) · Branch / PR: `claude/lpc-use-notes-2026-10-25`, https://github.com/mchadwick25-droid/CIC-Project/pull/1145

Stopped at Mark's word (relayed 2026-10-26): usage is now a hard constraint. No batch was left half done.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Sermon batches 1 and 2 (18 quote records) | Opus review and recheck each; merged (PR #1133, #1136) |
| Gapped Formation Precedent corrected in place; P2 pass for OG-59, 63, 64, 65 | Opus review, Revise, then recheck Approved to proceed; merged (PR #1141) |
| Decision 8B: 29 embedded quotations into verified quote records with Opus renderings | `Decision_8B_Quotes_Review_2026-10-25.md` (Revise), `Decision_8B_Quotes_Recheck_2026-10-25.md` (Approved to proceed); merged (PR #1143) |
| World front and facilitator brief, site JSON | `Surface_Records_Review_2026-10-25.md`, `Surface_Records_Recheck_2026-10-25.md` (round 3 Approved to proceed); merged (PR #1143) |
| Doc_10 (Datus): Fable draft, Sonnet revision; voice record `source_anchor` (9 entries) and distress-comparison guard; four demonstrations; world_core caution 13 (`rzg` pointer) | `Doc_10_Review_Round1.md` (Revise), `Doc_10_Review_Round2.md` (Approved to proceed); merged (PR #1143) |
| Retrieval golden set `engine/m4/reports/bench/lpc.json` (15 questions, written before any hinting) | merged (PR #1143) |
| Acclamation force description rewritten to the readability bar (own PR under the 8B scope ruling) | `Acclamation_Force_Readability_Review_2026-10-25.md` (Approved to proceed); merged (PR #1144) |
| Use notes on all 117 voiced records, held in stage `wb_lpc_s2u_use_notes.py` | `Use_Notes_Review_2026-10-26.md` and `Use_Notes_Recheck_2026-10-26.md` (round 3 Approved to proceed); every `means` FK ≤ 10, FRE ≥ 60, ≤ 25 words; in PR #1145 |
| B-1a/B-1b coverage check and six search records | `lpc_B1a_B1b_Coverage_Check.md`; `records lpc --freeze` no longer reports a missing search record; in PR #1145 |
| Gates on the PR #1145 head | `records`, `regate`, `claims`, `handoff` PASS; commentary 0; check_paths 0 new; texts README OK; pytest m1/m10 and quote count 686 passed |

## 2. Not done

- **PR #1145 merge.** CI was running at stop. Merge when green.
- **Commentary-by-passage batch** (Mark's ruling, `lpc_Decision_Log.md`, 2026-10-26). About 12 to 15 passages from the *Expositions on the Psalms*, the *Tractates on John*, the *Ten Homilies on 1 John* and *The Sermon on the Mount*. Each record names its Bible passage in `retrieve_when`. Not started.
- **OG-73 items.**
  - Story `telling` fields for the seven stories.
  - The first traditions page, `cic-website/traditions/latin-pastoral-congregational-christianity.html`, built by hand from another world's frame.
- **Records status.** Every lpc record is `status: draft`. `gate_status_ready` fails a draft record that compiles into the package. Mark the finished records `ready` before packaging.
- **Package build and pin, then validation.**
  - `python -m engine.m2.cli build lpc`, then `determinism-check lpc`.
  - Mark sets `package.location` in `records/worlds/lpc.yaml`.
  - Run the retrieval bench.
  - `validation lpc` reads **full**, because `safety_adjacent` is true. It needs Mark's named live test and cap. He ruled the cap is set after Doc_10, with the exact probe count.
- **Pre-freeze re-sweep** (from the B-1 check):
  - Two English Hefele volumes are vendored but have no Registry row.
  - Decret and Frend are to acquire.
  - Eusebius *Church History* VI.43 and VII.2–9 go to the next Doc_02 revision.
- **Hydatius.** Library placement is still pending (`NEEDS-RULING.md`). After it, the force record may say "May 429, by Hydatius's count".

## 3. Re-check before you trust it

- **The four old agent worktrees** under `.claude/worktrees/` (sermon batches) hold uncommitted changes. They were not inspected and not deleted. Look before removing them.
- **The use-note `means` lines cut to pass the reading bar** read "priest" for *clericus* and "properly read" for "validly read". The round-3 reviewer accepted both. Watch them in validation.
- **The `rzg` pointer** is carried by world_core caution 13. No live turn has tested it.

## 4. Waiting on Mark

- **UN-22 (OG-80).** `use_note.means` reaches the voice but is not readability-graded. The don and rzg notes fail the bar almost throughout. This is a fleet engine decision.
- **Validation.** The live-test name and metered cap, once the package is pinned.
- **Topics with no record** (OG-81): hell, judgment, the dead, infants, suicide. Suicide is Facilitator-governed. Whether lpc adds records for these is open.
- **A passage index** (OG-81). It is a fleet engine work item, not lpc's.

## 5. Next step

Merge https://github.com/mchadwick25-droid/CIC-Project/pull/1145 when CI is green. Then, in a fresh session, start the commentary-by-passage batch on a new branch off `main`, using the sermon-batch method in `wb_lpc_s24.py`, `s25.py`, `s2y` and `s2u`.

## 6. Spend

- **Allowance share used:** this session ran long, with many Opus and Sonnet subagents and one Fable draft. It hit a session limit once on 2026-10-25. Mark reports the weekly allowance about half used by Sunday evening.
- **Metered:** none. No live test and no paid service.
