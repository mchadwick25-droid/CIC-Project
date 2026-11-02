# lpc runs held by the Engine thread, 2026-11-01 and 2026-11-02

Each `runN.tar.gz` unpacks to one work folder of the shadow pipeline (`engine.m3.test100`, `test100_bound`, `test100_check`, `test100_log`): `replies/` (helper replies: reader, safety, voice drafts), `pending/` (the exported requests, including the system prompts), `answers/`, `bound/`, `check/` (reads, rewrites, re-reads), `log/` (one record per answer: question, sub-question named, offer, sentence decisions, reads, placements, ending, final text), and where it exists `reading/` (the Opus readings and samples). Helper agents stood in for every model call. `run12` is unpacked as `../lpc/`. Dates are file times in UTC. Question set for every run unless stated: `S3-Test100/lpc_106_questions.yaml` (106) or the subset named in the run's `set.yaml`.

| Run | When | Questions | What it is | Code it ran on | Seed |
|---|---|---|---|---|---|
| run1 | 2026-11-01 02:53 | 106 | Stage 4 first run of the pipeline: 20 abstained, 1 incomplete (Stage4_Report: "the first run abstained on 20 of 105") | not recorded | none |
| run2 | 2026-11-01 03:35 | 106 | An intermediate full run (15 abstained). Not in a report. Purpose not recoverable from the files | not recorded | none |
| run3 | 2026-11-01 03:51 | 7 | Subset run; purpose not recoverable | not recorded | none |
| run4 | 2026-11-01 04:34 | 30 | Subset run (30 answers); purpose not recoverable | not recorded | none |
| run5 | 2026-11-01 05:55 | 106 | The Stage 4 proof run reported in `Stage4_Report.md` (14 abstained of 106, 13%), with its `reading/` | not recorded (before Decision-Log 49) | none recorded |
| run6 | 2026-11-01 06:31 | 17 | Subset run (the round 2 targeted redraft is the likely purpose, not confirmed) | not recorded | none |
| run7 | 2026-11-01 11:46 | 4 | Subset run; purpose not recoverable | not recorded | none |
| run8 | 2026-11-01 22:27 | 106 | The Stage 3 proof run (`Stage3_Report.md`); `reading/` holds the Opus readings of 30 answers, the 30 quote-fit placements, the 21 tellings' faithfulness read, and the first-sentence ratings of the register page | `main` `f8d0487a` (merge of #1443), lpc package `2026-11-01T21-44-01Z` | 20261111 (the 30 read) |
| run9 | 2026-11-01 23:03 | 28 sealed | Draft directive with the plain-writing clause (grade 8.4, ease 65.0 shipped) | `main` `b79eef8c` plus the unpushed commit `88571457` (`run9_directive_patch.diff`) | none |
| run10 | 2026-11-02 02:33 | 2 (q101, q102) | Re-run after Library's routing change (#1447), old directive | `main` `c386bf02` (merge of #1448) | none |
| run11 | 2026-11-02 03:36 | 50 | The first-sentence directive (Decision-Log 63); 17 abstained; `readings.json` and `first_sentences_rated.json` hold the Opus reading of 30 and the first-sentence ratings | `main` `24eb4448` (merge of #1449) | 20261112 (the 30 read, drawn before the run) |
| run12 | 2026-11-02 04:04 | 50 | The multi-record opening (Decision-Log 64); 4 abstained; same 30 read; `../lpc/` | `claude/engine-union-opening` `109c9fa3`, engine identical to `main` `a61c37f2` | 20261112 (same 30 as run11) |

## Blind old-versus-new ratings, 28 sealed

- First version (`analysis/oldnew_*.json`): run12 new against every saved old sentence including those the old gates removed; seed 20261113. Superseded.
- Final version (`../ratings/cw_lpc_*.json`): old = `removed=false` sentences only; seed 20261114; `README.md` in the parent folder has the table.

## Other files in `analysis/`

- `offers_main.json`: offers for all 106 on `main` after #1447 (`offers.py` run, no model call). `offers_before.json`, `offers_after.json`, `offers_hint.json`, `offers_hint2.json`: offer experiments for q101 with a monkeypatched `retrieve_when`, not runs.
- `routing_items.json`, `routing_rated.json`: the sub-question the reader named for each of the 106 questions (from run8) and one Opus reader's judgement of label fit and record fit.
- `register_side_by_side.html`, `pairs.json`: the eight matched questions (earlier drafts, Stage 3, plain-clause) with the blind first-sentence ratings. `first_sentence_run.html` and `union_opening_run.html`: the pages put to Mark for run11 and run12. `stage3_reading_list.html`, `stage3_table.html`: the Stage 3 pages. `faithfulness_report.md`: the tellings read.

## Not held

The Stage 4 first-round reader and safety replies for the full 106 are inside run1 and run5 only; the Opus readings of the Stage 4 proof run's 30 answers are in `run5/reading/`. Nothing from before 2026-11-01 02:53 UTC is held by this thread (the Stage 4 acceptance sheet and report in `Stage4_*.md` are the record of it). Code commits for run1 to run7 were not recorded.
