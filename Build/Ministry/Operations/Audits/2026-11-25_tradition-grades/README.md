# Tradition grades, 2026-11-25

Mark asked for every tradition brief on the Church Family Tree to be graded: "a, grade all 353 traditions with the idea what must be redone, what should be, what would benifit, what is ok to keep, what is great as is." And: "like a grade, if either has an f score ... it becomes a high priority, then ds then cs etc." And: "traditions are the main thing everything else gives depth and context to the tradtions."

No story, census, card or site file was changed. Every model read ran inside this session on Opus, drawn from the weekly allowance, with no metered spend.

## The set

The set is every census entry in `cic-website/data/world-census.json` that is a tradition (not a person, council or documented story) and has a `longDescription`. That is 346 traditions and the 7 cross-church movements, 353 in all, the 11 built worlds included (`Set.json`). The graded text is the `longDescription`. The texts average 205 words, and 303 of the 353 are under the tradition kit's floor of about 300 words.

## Rigor

Rigor comes from the scans of `../2026-11-23_what-and-why-rank/` (`Ranked_List.json`), where the census `id` is the piece name without `tree/`. No tradition `longDescription` changed between that scan and this audit.

The 11-23 scans read each built world's World-Narration `story.txt`, not its census `longDescription`, and five traditions were never scanned. For these 16, the same scans were run on the `longDescription` (`scans/`):
- two bare-statement readers (`Reader_Prompt.md`);
- one modern-opinion reader (`Modern_Reader_Prompt.md`);
- a third read (`Third_Read_Prompt.md`) on every finding only one reader flagged, every pair two weight-steps apart, and every modern finding.

`scans/merge.py` matches the reads and writes `Held_Findings.json`. Where the two readers agreed and their weights were one step apart, the higher weight is kept.

The rules (from the brief, with Mark's rulings below):
- **F:** a modern guess or reconstruction told in the story (a "guess" finding), or 3 or more modern-opinion findings, or a Crucial modern finding.
- **D:** a Crucial bare statement, or 2 modern findings.
- **C:** 1 modern finding, or any Supporting bare statement. B allows "only Passing findings", so one Supporting bare statement is graded C. 56 briefs are C on that alone.
- **B:** only Passing findings, or none found by the scans.
- **A:** only after a full trust read with the sources open (`roles/reviewer.md`) finds every sentence held or a fair summary. It is run only on briefs that would otherwise be A or B on rigor and A on craft.

**Rigor B means "no fault found by the scans", not "checked sentence by sentence".** The scans looked only for bare statements and modern opinion. They never checked softened summaries, added assumptions or claims with no source.

## Craft

Craft comes from one first-time listener per brief (`Listener_Prompt.md`, from `roles/reviewer.md`, the listener reads). The listener has no church background, has English as a second language, hears the text once and sees no sources. There were 15 batches of about 24 briefs (`packets/`, `listener/`). The listener counts and quotes these blocking faults:
- unfilled test lines;
- an opening that leaves who, where or when missing (one fault);
- bare statements;
- AI tells;
- failing sentences that lose the thread.

The listener also says:
- whether the opening pulls them in;
- where they drift;
- whether they would listen to the end;
- whether the text is a story or a summary.

The rules:
- **F:** would leave, and either has 8 or more blocking faults or is a summary.
- **D:** would leave, or has 8 or more blocking faults.
- **C:** 4 to 7 blocking faults.
- **B:** 1 to 3.
- **A:** none, and would listen to the end.
- **Summary rule (Mark's ruling 1, below):** a summary rather than a story is at most D, and a summary under about 300 words is F.

## Overall

The overall grade is the lower of the two. F: must be redone. D: should be redone. C: would benefit. B: OK to keep. A: great as is. `grade.py` computes every grade from the files here and writes `Grades.csv` and `Grades.json`, sorted F first.

## Calibration

The listener first read four calibration pieces from `../2026-11-24_calibration/pieces/`, under their codes only (`listener/calibration.md`).

| Piece | Read | Under the brief's cut-offs | Expected |
|---|---|---|---|
| P09 ancien régime | would leave, 12 blocking, summary | F | F |
| P02 Wittenberg | would listen, 10 blocking, story | D | D |
| P06 Kongo | would listen, 4 blocking, story | C | C or B |
| P01 Post-Apostolic | would listen, 2 blocking, summary, 80 words | B | F |

P01 missed: it is short enough that the listener stays to the end. The run stopped and the miss was reported to the governing thread. Under Mark's summary rule P01 grades F, so all four sort as expected, and the full run went on.

## Mark's rulings (through the governing thread, 2026-11-25)

Mark: "a, and yes to the scans and guess as F".
1. **Summary rule (option A).** A brief that is a summary rather than a story grades D on craft. A summary that is also under the tradition kit's two-minute floor, about 300 words, grades F.
2. **Scans for the 16.** The 11 built worlds' `longDescription` and latin-pastoral-congregational-christianity, kongo-christianity-afonso-to-1650, kirishitan-japan, china-mission-born-christianity and new-spain-and-andes-mission-born-christianity get the same two scans the 11-23 rank used, and their rigor is graded from those.
3. **Guesses.** A "guess" finding, a reconstruction told in the story, counts as a modern voice told as the record: rigor F.

## Result

See `Grades.csv` and the page for Mark (https://claude.ai/artifact/4ptqjtgCssAcH7ePVFGa8G).

| Overall | Action | Briefs |
|---|---|---|
| F | must be redone | 263 |
| D | should be redone | 11 |
| C | would benefit | 53 |
| B | OK to keep | 26 |
| A | great as is | 0 |

- Rigor: F 56, D 25, C 100, B 172.
- Craft: F 243, D 10, C 46, B 51, A 3.
- The listener called 248 of the 353 a summary rather than a story, and would leave 76. Most of the F grades come from the summary rule: 303 briefs are under about 300 words.

**The trust read.** Only one brief would otherwise grade A or B on rigor and A on craft: athonite-and-comnenian-byzantine-monasticism (`trust/`). Its 11 sentences:
- SUMMARY HOLDS: 5.
- SOFTENED OR CHANGED: 3.
- ASSUMPTION ADDED: 2.
- NOT FOUND: 1.

The reader also judged its heart missing: nothing Comnenian and no ordinary monks, in 152 words. It does not earn an A. The brief's rules give no lower grade for a failed trust read, so its rigor stays at the scans' B and the failure is written into its basis. It is graded B, OK to keep, on rules that never checked its sentences. That is left for Mark.

## Files

- `Set.json`: the 353 briefs.
- `packets/`: what each reader read.
- `listener/`: the listener reads, calibration included.
- `scans/`: the 16 briefs' scans, matching, third read and held findings.
- `trust/`: the trust read.
- `Grades.csv`, `Grades.json`: every grade, with its basis.
- `grade.py`: computes every grade.
