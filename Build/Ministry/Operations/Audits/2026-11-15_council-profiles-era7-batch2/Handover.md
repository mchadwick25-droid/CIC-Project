# Handover after round 1: era 7 council profiles, batch 2 (2026-11-15)

Written by the first worker (session_01JMNsSD4ANFJ91uXbMro8dp) at a clean break, with its context near the 400k limit. The coordinator is session_01JMNsSCeHv3rWkarHUsXAWg. No blocking point is open; round 1 is reviewed and applied, and rounds 2 and 3 remain.

## The job

Era 7 major councils, batch 2 of 3: Colloquy of Regensburg (1541), Council of Trent (1545-1563), Diet of Augsburg and the Religious Peace (1555), Colloquy of Poissy (1561). Pattern `Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md`; model batch 1 (PR #1672). Length ceiling 2:30, about 400 words (Mark: "Keep 2:30 for councils"), never a target. Full-effort review in every round, by fresh Opus agents. Three rounds at most; every review file counts. Minor round 3 fixes to reader-facing text follow Mark's standing cap ruling of 2026-11-14 (apply as worded, then one targeted check by a fresh Opus agent of only those strings). No paid calls. Push only to `claude/cft-councils-era7-batch2`. No census, site, `cft-website/`, `Who-Profiles/` or `cic/texts/` change. Before merging the PR, send the coordinator one line and wait for its go.

## State

Branch `claude/cft-councils-era7-batch2`, pushed. No PR yet. origin/main not yet merged in since the branch was cut (9f36bfcb, PR #1672).

Files in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/`: the four briefs, entries and audio scripts; `records.json` (merged from `working/records_<id>.json` by `working/merge_records.py`: edit the working files, then re-run it); README extended with a "Batch 2" section and a length line per council. Regenerate audio with `working/mkaudio.py` (batch 2 ids only). Grade with `working/grade.py <brief>`.

| Council | id | Words | Spoken | FK | Flesch | Longest |
|---|---|---|---|---|---|---|
| Colloquy of Regensburg | colloquy-of-regensburg-1541 | 400 | 2:30 | 8.02 | 60.35 | 25 |
| Council of Trent | council-of-trent | 400 | 2:30 | 7.61 | 61.99 | 22 |
| Diet of Augsburg and the Religious Peace | diet-of-augsburg-1555 | 400 | 2:30 | 7.81 | 63.11 | 25 |
| Colloquy of Poissy | colloquy-of-poissy-1561 | 400 | 2:30 | 7.41 | 66.29 | 25 |

All four sit at the ceiling. Each first draft ran over and was cut back; every round 1 reviewer was asked to test the length against the README's reason, and each found the brief earns it (Poissy's named one clause, now cut). Regensburg's Flesch is close to the 60 floor: check it after every fix. Round 2 reviewers should test length again.

## Round 1

Four fresh Opus reviewers, one per council (`R1_review.md`, parts in `working/R1_part*.md`); four fresh Opus fixers (`R1_changes.md`, parts in `working/R1_changes_part*.md`).
- Regensburg 0B/2S/13M. Faber's 12 May letter added as the Catholic eyewitness; Calvin marked as the Protestant side; "crosses" is the 1858 translator's word.
- Trent 1B/4S/10M. B-B1, a false absence: the Lutheran side is not "only through Sarpi and Waterworth"; Pallavicino gives the envoys' demands, and the Smalcald Articles (1537, for Mantua) and the Formula of Concord (1577) are held. A Formula sentence was added to the brief.
- Augsburg 1555 2B/7S/14M. Polanco is not "in the city"; Pallavicino's subjects were not tied to Sarpi's cities; Ferdinand's "cleared him of blame" rested on a word lost in the OCR (now "pleading plain necessity"); Bossert named; Westphalia's "inter illos" kept.
- Poissy 1B/5S/11M. Beza's sentence now carries his concession (believers truly share Christ's body by faith); Sarpi and Pallavicino placed by side; Catherine's "Colloque gracieux" is the September meetings, not the calling.

Sarpi label across the batch: briefs "the Venetian friar Paolo Sarpi" (Regensburg and Trent add "was hostile to the papal court"); entries "A Venetian Servite friar; Catholic but hostile to the papal court."

Two worker commits (a526a9e3, 66525e0f) took in part of the Trent and Augsburg fixers' edits while they ran; the commit after `R1_review.md` holds the final files.

## Still to do

1. **Round 2**, a targeted recheck by four fresh Opus agents at full effort: only what changed, against the round 1 findings, reading every fix as new text against its source line in context (batch 1's round 2 and 3 blocking points came from fix wording). Brief: adapt `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/working/review_brief_r2.md`. Write `R2_recheck.md`, then fixes and `R2_changes.md`.
2. **Round 3**, the last, the same way, if needed (`R3_recheck.md`, `R3_changes.md`). A blocking point open after round 3 goes to the coordinator for Mark's cap ruling.
3. **Decision-Log** entry "Major councils, era 7, batch 2" in the shape of batch 1's (`Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, "Major councils, era 7, batch 1", about l.3602): Decided; the four councils with words, FK, Flesch and main witnesses; worker's calls (rivers as the scan; Who click rule; "Affected" for the traditions shut out of the 1555 peace, since the recess excludes without condemning; the scan's "last serious joint attempt" (Regensburg), "first legal toleration" and "Calvinists left out" (Augsburg) and "hope of a common French church ended" (Poissy) found in no held source and not used; American spelling; Opus drafted); Review; What is still open.
4. **Open-Gaps**: one entry, next free number re-checked on origin/main just before merging (used through 273 on main at the start; others take numbers). Items: the "For Open-Gaps" lists in each `R1_changes` part (and later rounds); the scan-row claims above; census gaps (Strasbourg's church 1541; the French bishops only under the-tridentine-church; the Palatine theologians; the Indian sees at 1562; no place ids for Regensburg, Trent, Bologna, Augsburg, Poissy); census differences (Abdisho's arrival in Rome "the year before", 1561, against the census's 1562; the live Tridentine story gives the closing tears to Massarelli, whose diary is not held); the lost word in Pallavicino l.27571; Sarpi's "268 Bishops" probably a misprint for 168 (page image unchecked); people shown NOT SCORED, owner the coordinator.
5. **Checks** as PR #1672: `working/grade.py`, `python tools/check_live_commentary.py --base origin/main --enforce`, `python tools/check_spelling.py --base origin/main --enforce`, `python tools/check_paths.py`; JSON valid; audio equals brief plus tags. Merge origin/main, check no conflict markers.
6. One draft PR, push once after checks, mark ready; tell the coordinator and wait for its go; merge on green. Then report: words, spoken time and FK/Flesch per profile, and the PR link.

## Lessons

- The entry agents' sentence-by-sentence check of the brief against its sources caught 23 overstatements before review; keep it.
- Read the whole source sentence, with its concessive clause (Beza's "combien qu'il nous fust véritablement offert"), before paraphrasing.
- A modern editor's date, title or footnote is the editor's (Baum-Cunitz's "10 September", Bonnet's dating of Calvin's 1545 letter, Jacobs's canon footnote).
- Search for each side's own held voice before writing that a side "reaches us only through" its opponents (Trent B-B1).
