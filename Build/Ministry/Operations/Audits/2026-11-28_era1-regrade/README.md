# Era 1 regrade of six, 2026-11-28

Six era 1 person briefs graded on their final text, by the whole-text grading Mark approved on 2026-11-28 ("1 yes"; Decision-Log, "Grading on the whole text, reading level with names out"). Five were fixed after the 28 Nov grading; Cyprian of Carthage is new. No story, card or census file was changed. Every read ran as a fresh Opus subagent inside this session, drawn from the weekly allowance, with no metered spend.

## The set

`build_set.py` writes `Set.json`, `Texts.json` and `packets/`. Each text is `Build/Ministry/Operations/Audits/2026-11-26_batch-12/<slug>/<slug>.brief.txt` on its branch; `Set.json` records the commit read.
- Methodius of Olympus, Suetonius, Hippolytus of Rome, Tacitus: `claude/cft-release-batch12-13`.
- Josephus: `claude/cft-fix-josephus-grade`.
- Cyprian of Carthage: `claude/cft-story-cyprian-of-carthage`.

## Method

The method of `../2026-11-28_era1-new-grades/`, with its prompts copied unchanged.
- **Scans** (`packets/S01.md`): two bare-statement readers, one modern-opinion reader, and the third read on what `scans/merge.py` sends there. The readers agreed on 3 findings; 2 went to the third read, 1 of them modern, and 1 held.
- **Listener** (`packets/L01.md`, `listener/L01.md`): one first-time listener read all six.
- **Kit's bar first.** Each reader was told Mark's 2026-11-28 rule on top of its prompt: exactness that does not touch the heart is not a finding; a real gap the listener needs still is.
- **Hedged date.** Suetonius, "His lives end with that emperor, so he wrote after Domitian's death.", is a guess only on a date, and counts as one hedged-date finding by Mark's ruling of 2026-11-26 (`Hedged_Dates.json`).
- **Trust read.** The method sends a full trust read, sources open, to a brief that is otherwise rigor A or B and craft A, and an A needs one (`../2026-11-25_person-council-grades/README.md`). Josephus (A, A) and Suetonius (B, A) qualify. This run's brief excluded source reads, so none was run: Josephus's A is pending a trust read, and Suetonius's B stands unless one finds a sentence that does not hold.
- **Grades.** `run_whole.py` imports `../2026-11-28_era1-new-grades/grade_whole.py` and calls its own `score()`, weights unchanged. The before grade is that folder's `Grades_Whole.csv` (Josephus was then graded on the released census text).
- **Left by source.** `Left_By_Source.json` lists the findings each story's `Revision.md` left because the old source gives only the act. They are flagged on the page and still counted in the grade.
- **Reading level.** `readability_names_out.py` writes `Readability_Names_Out.json`. All six pass with names out.

## Result

| Story | Rigor | Craft | Overall | Before |
|---|---|---|---|---|
| Hippolytus of Rome | B | C | B | C |
| Tacitus | B | B | B | C |
| Cyprian of Carthage | B | B | B | new |
| Suetonius | B | A | B | D |
| Methodius of Olympus | A | B | A | D |
| Josephus | A | A | A, pending a trust read | C |

None is below B. Two of Hippolytus's three findings and two of Tacitus's three are the ones left because the source gives only the act.

The page for Mark: https://claude.ai/artifact/PXTnWYPjN5T26TSY1Vg4Pg
