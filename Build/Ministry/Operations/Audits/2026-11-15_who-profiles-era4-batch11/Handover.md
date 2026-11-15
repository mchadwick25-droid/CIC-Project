# Handover: era 4 Who batch 11

Written 2026-11-15 by the first batch 11 worker (session_01JMNsSAS59areLQcPvJ1w81), at a clean break: round 1 is reviewed and applied. The context passed about 385k, so a fresh session picks up from here, per the coordinator's brief. Report to the coordinator, session_01JMNsSCeHv3rWkarHUsXAWg, with send_message only.

## State

- Branch `claude/cft-who-era4-batch11`, pushed. No pull request yet.
- Eight profiles in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/`: `stepanos-of-taron`, `eulogius-of-cordoba`, `paulus-alvarus`, `theodore-abu-qurrah`, `stephen-of-mar-saba`, `ishoyahb-iii`, `al-tabari`, `ibn-ishaq`. Each has a brief, a card and an audio file. `records.json` holds all eight. The README is written.
- No majors: none of the eight has a census row in release 44, and the re-score marks all "no".
- Coordinator's calls, already applied: Stephen is a WHO as a recorder, "Stephen of Mar Saba", id `stephen-of-mar-saba`, with "Mansur" dropped (no held line gives it). Ishoyahb III sits in The Church of the East on the Silk Road, since St. Thomas Christians of India begins in 849.
- Round 1 (the full review, three parts, fresh Opus agents, full effort) found 23 blocking and 75 minor points: Part A 13 and 27, Part B 1 and 18, Part C 9 and 30. Fresh Opus fixers applied every profile finding; none was refused. One more agent applied the README findings. Files: `R1_review.md`, `R1_changes.md` here, with the README log to be appended to `R1_changes.md` from the scratch file `R1_README_changes.md` if it is not already there (check).
- Briefs after round 1: 333 to 338 words (about 2:03 to 2:05), FK 6.2 to 8.2, Flesch 62 to 76. Lengths are a little above batch 10's 329 to 333; round 2 may tighten by writing tighter.

## What is left

1. **Round 2**: a targeted recheck in three parts (A: Stepanos, Eulogius, Alvarus; B: Abu Qurrah, Stephen, Ishoyahb; C: al-Tabari, Ibn Ishaq, README). Fresh Opus agents at full effort, who read the round 1 review and changes, recheck every changed string against its source as new text, reread every brief in full, and test lengths. Briefs for the agents are in `briefs/` (adapt the round 1 review brief: give each reviewer R1_review.md, R1_changes.md and `git diff` since commit 3e085559, the last pre-review commit). The census of release 44 is `git show origin/main:cic-website/data/world-census.json`. Then R2_review.md and R2_changes.md. Fixers now edit `records.json` directly; run them one at a time, or give each its own scratch copy and merge.
2. **Round 3** if needed; at most three rounds, every review file counts. A blocking point open after round 3 goes to the coordinator for Mark's cap ruling. Minor round 3 fixes to reader-facing text follow Mark's standing cap ruling of 2026-11-14 (apply as worded, then one check of only those strings by a fresh Opus agent, `R4_cap-check.md`).
3. **Finish**: Decision-Log entry for the batch (shape: the batch 10 entry, "Who profiles, era 4 batch 10", 2026-11-15) with any cap ruling; Open-Gaps entry "Era 4 Who batch 11" (2026-11-15), taking the next free number just before merging (used through 272 on main when this batch began; re-check), with the census differences from the README (among them the Mar Saba story's "a relative of John of Damascus", which merges Stephen with Stephen the Wonderworker), the Babai card's "Beth Abe", re-score corrections and Library items. Run `grade_text`, `python tools/check_live_commentary.py --base origin/main --enforce`, `python tools/check_spelling.py --base origin/main --enforce`, `python tools/check_paths.py`, JSON parse, audio equals brief (`briefs/score.py` rebuilds audio and parses JSON; `briefs/quotes.py` checks quoted strings; its two known hits are the folio-marked Evetts quote, which the README names, and a regex artifact on the Ishoyahb card). Merge origin/main, check for conflict markers, open one draft PR, push once, mark ready. Before merging, send the coordinator one line and wait for the go. After merging, send words, spoken time and FK/Flesch per profile.

## Lessons from this batch so far

- The re-score rows were often wrong on lines and sometimes on claims (Stephen's "Mansur", Alvarus's l.68018, Ishoyahb's "early source not held"). The dossiers caught most of it. Keep the "Corrections to the re-score" list current.
- Drafters reached for strong words that no line gives ("legend" for Thomas of Marga's "tradition"; "a bishop, Janah", which is Graf's inference). Read every characterization of a source against the source's own words.
- Paired or linked profiles (Eulogius and Alvarus) must tell a shared dispute the same way, with both sides, in both.
- Every round 1 fix is new text: round 2 should look hardest at the fixes.
