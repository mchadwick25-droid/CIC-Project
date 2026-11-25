# The three person references, brought to the 2026-11-24 kit

A fix to live texts, run as a batch of its own (Kit, Part 3), for Open-Gaps 406. Basil of Caesarea, Epiphanius of Salamis and John Chrysostom, through the kit's steps on what each changes, then to Mark before anything is frozen, released, recorded or merged.

Mark's words for the batch (Decision-Log, "How a brief's success is measured", 2026-11-24, decision 5): "we are not pursuing perfection, just reliability, appreciation for rigor. we cant pursue loops of minor tweeks."

## Starting files

| Story | Brief | Outline | Source sheet |
|---|---|---|---|
| Basil (`basil-of-caesarea`) | `Brief-Kit/reference/basil-of-caesarea/`, the same as the live `longDescription` | same folder | same folder |
| Epiphanius (`epiphanius-of-salamis`) | `Brief-Kit/reference/epiphanius-of-salamis/`, the same as the live `longDescription` | same folder | same folder |
| Chrysostom (`john-chrysostom`) | batch 10's, from `origin/claude/happy-ritchie-u8wn8l` | batch 10's (see judgment call 1) | none held; the researcher builds one |

`Calibration_Findings.md` in the Basil and Epiphanius folders copies, word for word, the calibration's trust read and two listener reads of each (P04 and P08, `2026-11-24_calibration/run2/`). Chrysostom was not in the calibration; his known faults are those Open-Gaps 406 names.

## Steps

| Step | Basil | Epiphanius | Chrysostom |
|---|---|---|---|
| 1. Research fix pass / new outline | done (`Fixes.md`), plus a length fix | done (`Fixes.md`), plus a length fix | new `Source_Sheet.md` and `Outline.md`, fix pass |
| 1b. Outline check on what changed | `Recheck.md`, `Recheck_Length.md`: applied | `Recheck.md`, `Recheck_Length.md`: applied | `Outline_Check.md`, `Recheck.md`: applied |
| 2. Writer revises failing sentences | done (`Changes.md`) | done | done |
| 3. Trust read, first-time, AI skeptic | `Review.md`: REVISE | `Review.md`: REVISE | `Review.md`: REVISE |
| 4. One revision | `Revision.md`, 723 words | `Revision.md`, 724 words | `Revision.md`, 756 words |
| 5. One fresh read | `Fresh_Read.md`: trust PASS; listener's blocking point fixed by its exact change; 733 words | `Fresh_Read.md`: trust's one softened clause fixed by its exact change; listener PASS; 744 words | `Fresh_Read.md`: trust PASS; listener's bare sentence cut by its exact change; 742 words |
| Mark reads all three | waiting: https://claude.ai/artifact/LyXy1LGWYovdCDG3ADzUgB | waiting | waiting |

## Judgment calls

1. **Chrysostom's outline.** The brief comes from batch 10's branch, whose last modern pass (2026-11-23) changed the brief and added three Do not say lines to the outline there. Main's copy of the outline lacks them. The outline used is the branch's, read only; nothing is pushed to the branch. It is not a Part 2 outline ("This story was approved before the kit and has no outline or source sheet"), so the researcher builds a source sheet and a Part 2 outline for the approved beats, and the outline check reads all of it.
2. **Reference read.** The fresh read's once-per-batch read of the kind's references would read the three old texts this batch replaces. The fresh reads' counts of the three new briefs are the counts proposed for `Brief-Kit/reference/Scores.md`; no separate `Reference_Read.md` is made.

## Open items

- **Basil and Epiphanius run long after the writer's fixes** (Basil 723 words, Epiphanius 762, against about 675). Both outlines' Cut first lists were spent; each went back to the researcher for a length fix pass and a recheck of it before the writer applies the cuts.
- **Chrysostom's essence and length moved.** The researcher kept batch 10's essence and added a second sentence (what it changed: his sermons read for centuries; his followers back only when his body came home), and set the length at about 3:25 (515 words), with a Cut first list back to 450. Both are for Mark's ruling on the page at the stop.

- **Chrysostom's length, provisional.** The outline check found the beats need about 630 words, not 450 or 515 (BLOCKING). The fix pass set about 630; the recheck found the Cut first list reaches only about 650 and a floor of about 580 (530 would cut the record's force or a required explanation), and the outline now says so. The story is written and reviewed at about 650, provisional, for Mark's ruling; if he wants it shorter, the Cut first list takes it to about 580.
- **Epiphanius after the one revision runs 724 words (about 4:50)**, about 50 over the approved 675, every added word answering a review finding (the reasons for the Long Brothers' expulsion and the forced ordination, what Augustine did). The Cut first list is spent. For Mark's ruling on length; no further round was run for it.
- **Chrysostom's writer used the whole Cut first list and the brief still runs 690 words (about 4:36)**, against the provisional 650 and the person kit's "about 675". The outline's estimates ran about 100 words low. Taken to review at 690; for Mark's ruling on length.
- **Basil after the one revision runs 723 words (about 4:50)**, about 50 over 675; the added words answer the review's blocking findings (what the quarrel, the charge and the credit to Macrina were). Cut first is spent. For Mark's ruling on length.
- **Chrysostom's overlap check** lists "SPELLING Comana (the tree has Colman)". Comana is the place where he died (Palladius; Socrates), not a person's name; Colman is an unrelated name on the tree. No change.
- **Fresh-read changes.** A fresh read's exact changes, its one BLOCKING clause included where it gives exact wording, are applied word for word (Kit, Part 3, step 5); a finding with no exact wording is noted, not applied. No further round is run on them.
- **Chrysostom after the one revision runs 756 words (about 5:00).** The listeners' bare-statement finding on his rebukes had no other outline content, so the reviser put back the Gothic general and the Arians (Cut first 15). Over the kit's "about 675"; for Mark's ruling.

- **HOLD (governing thread, 2026-11-24).** An independent blind trust read found four sentences that do not hold (Epiphanius "he feared they would drift from the church"; Chrysostom "behind her curtains" and "read for centuries … came back only when his body came home"; Basil "His accusers had won over the governor"). Release stopped before commit; its edits are in `Release_held.patch` and `Release_held_partial.md`, and the live files are back to main. Reply sent with the Greek of the curtain line (PG52 l.824-825, "ὑπὸ τὰ παραπετάσματα αὑτῆς ἔκρυψε"). Waiting for Mark's ruling.
- **After the hold (2026-11-25).** Mark: "a, second trust read on changed sentences" (into the kit by PR #1802). The curtain line stands (the governing thread withdrew it on the Greek, PG52 l.824-825). Two sentences fixed from their sources (Epiphanius's motive, Letter 51; Basil's accusers, Letter 94; `Changes.md`, "Second-trust fixes"). On "His sermons were read for centuries", Mark: "it is ok to use later sources to show impact if they are reliable"; it stands, on Socrates, the Augsburg Confession and Calvin. A second independent trust read (`Second_Trust.md` per story) reads every sentence that differs from the text before this batch. Then the freeze and counts are redone, the held release patch re-applied, and one pull request opened, merged after #1802.
- **Second trust read results (2026-11-25).** Basil 31 changed sentences: 11 held, 20 summary holds; Chrysostom 37: 26 held, 11 summary holds; Epiphanius 26: 14 held, 10 summary holds, 2 softened, both caught only by this second read and fixed word for word as the reader gave them: (1) the monks' year of complaint was at Jerome's monastery, not Epiphanius's own (Letter 51, J6 10672-10705); (2) Theophilus's letter says he put "a few" monks out of the church, not that he drove them out of Egypt (Letter 90, J6 19717-19748). Epiphanius's card took two follow-up edits to match, checked. Refrozen; `Scores.md` carries both reads. Library gaps logged as Open-Gaps 415.

## Rulings

- **Mark, 2026-11-24, on the page (https://claude.ai/artifact/LyXy1LGWYovdCDG3ADzUgB):** asked the audio length (Basil about 4:53, Epiphanius about 4:58, Chrysostom about 4:57 at 150 words a minute), then: "keep them as they are, approved". This keeps all three lengths, approves Chrysostom's two-sentence essence and the fresh-read counts as the `Scores.md` counts, and approves the three briefs. Where it lives: this batch only. The governing thread confirmed (2026-11-24) that it covers all four asks, and relayed Mark's words there on length: "I talked to the thread and there was nothing to really take out, and that is the first thing, we don't want to leave anything critical out." Mark then ruled in the governing thread that it does not become a kit rule: "no, then we will end up with 8 minute audio for some and thats to long. these i approaved because they were close". The kit's length lines stay; the three lengths stand as approved because they were close to the ceiling, not as a precedent for long briefs.
- **Open, not this batch:** the Epiphanius card writer flagged that his census `dates`, `start`, `end` and `activeYear` rest only on editors' years and feed the timeline (a fleet-level call). Left unchanged.
