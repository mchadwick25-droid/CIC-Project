# Person and council grades, 2026-11-25

Mark asked whether the people and councils that went through the brief kit in batches 3 to 10 are better than what was there, and what grades they would get. He chose: "grade all 260 people and the councils, A–F on rigor and craft, ranked worst first", in its own session that only reads.

No story, census, card, site or kit file was changed. Batch 11, running in another session, was not read or touched. Every model read ran as a subagent inside this session, a fresh reader for each packet, drawn from the weekly allowance, with no metered spend.

The method is the tradition audit's (`../2026-11-25_tradition-grades/`), copied, with each kind's test lines and length floor from its kind kit (`Brief-Kit/kinds/person.md`, `kinds/council.md`) in place of the tradition kit's.

## The set

The set is every census entry in `cic-website/data/world-census.json` whose kind is person or major council and that has a `longDescription`: 260 people and 12 councils, 272 in all (`Set.json`). The graded text is the `longDescription`.

- **Kit batches:** 98, from batches 3 to 10 of `Build/Ministry/Features/Church-Family-Tree/Story-Ledger.md`. Five of them are councils.
- **Before the kit:** 174, seven of them councils.
- **References:** the three frozen person references are marked: Basil of Caesarea and Epiphanius of Salamis (batch 9) and John Chrysostom (batch 10).
- **Length:** kit stories average 579 words, stories before the kit 341. 12 stories, all from before the kit, are under their kind's floor.

`build_set.py` builds the set and the packets.

## Rigor

Rigor comes from the scans of `../2026-11-23_what-and-why-rank/` (`Ranked_List.json`), where a piece is reused when it was read there and its `longDescription` is unchanged since. The text is compared with the census on `main` just before those readings were committed (`80acd0ae`).

- **Reused: 85.** Batches 3 to 9 (84) and one story from before the kit (John Wesley). 24 of these were read in 11-23 by one bare-statement reader, not two, as that rank did. Their findings went through its third read.
- **Scanned here: 187.** The 173 other stories from before the kit and batch 10's twelve were never scanned. Basil of Caesarea and Epiphanius of Salamis changed after their scan. All 187 got the same scans (`scans/`, packets `S01` to `S08`):
  - two bare-statement readers (`Reader_Prompt.md`);
  - one modern-opinion reader (`Modern_Reader_Prompt.md`);
  - a third read (`Third_Read_Prompt.md`) on every finding only one reader flagged, every pair two weight-steps apart, and every modern finding.
- **Matching.** `scans/merge.py` matches the reads and writes `Held_Findings.json`. The two readers agreed on 326 findings, and 896 went to the third read, 744 of them modern. 838 of the 896 held.

The rules are the tradition audit's:
- **F:** a modern guess or reconstruction told in the story, or 3 or more modern-opinion findings, or a Crucial modern finding. A guess whose hedge is only on a date ("probably in 256", "by the usual dating") counts as an ordinary modern finding instead, by Mark's ruling (Decision-Log, "A hedged date counts as one modern finding", 2026-11-26). `Hedged_Dates.json` lists the 17 such findings; a guess that also names an author, a place or a person stays a guess.
- **D:** a Crucial bare statement, or 2 modern findings.
- **C:** 1 modern finding, or any Supporting bare statement.
- **B:** only Passing findings, or none found by the scans.
- **A:** only after a full trust read with the sources open finds every sentence held or a fair summary.

**Rigor B means "no fault found by the scans", not "checked sentence by sentence".** The scans looked only for bare statements and modern opinion. They never checked softened summaries, added assumptions or claims with no source.

## Craft

Craft comes from one first-time listener per packet of 23 stories (`Listener_Prompt.md`, `packets/L01` to `L12`, `listener/`). The prompt is the tradition one, with two changes:
- it reads the person and council kits;
- each kind has its own four test lines. For a person: who this person was, what happened, what it was about, why the connection matters. For a council: what it was, what happened at it, what its main issue was about, why the connection matters.

The rules are the tradition audit's, with each kind's floor for the summary rule:
- **F:** would leave, and either has 8 or more blocking faults or is a summary.
- **D:** would leave, or has 8 or more blocking faults.
- **C:** 4 to 7 blocking faults.
- **B:** 1 to 3.
- **A:** none, and would listen to the end.
- **Summary rule:** a summary rather than a story is at most D, and a summary under the floor is F. The floor is two minutes at the kind kit's pace: about 300 words for a person (450 to three minutes), about 260 for a council (390 to three minutes).

No separate calibration was run: the tradition calibration pieces are traditions. The three references stand in as the anchor. They graded B on craft, with 2, 1 and 1 blocking faults.

## The trust read

Three stories would otherwise be A or B on rigor and A on craft: Gregory of Nyssa, John Wesley and Moses the Black. Each got a full trust read (`roles/reviewer.md`) with the sources open, against the live census text (`trust/`). The batch's `Outline.md` and `Source_Sheet.md` served only as pointers; no earlier review or trust read was opened.

| Story | Sentences | Not holding | Heart | Result |
|---|---|---|---|---|
| John Wesley | 36 | 0 | right, in time | rigor A |
| Moses the Black | 22 | 1: "Around the year 400" rests only on a modern date (Modern only) | right, in time | rigor B, by Mark's ruling |
| Gregory of Nyssa | 17 | 1 softened (S12) | blocking: the Eunomius quarrel and the law of 381 come late | rigor F |

A failed trust read is graded F, by Mark's ruling that Athonite and Comnenian monasticism "takes its failed trust read, F" (Decision-Log, 2026-11-25). That brief failed on 6 of 11 sentences. Moses the Black fails on one date in 22 sentences, a date its outline rated Inferential-Thin and then gave the writer to speak. Mark ruled it B, with the fix noted: cut "Around the year 400," (Decision-Log, "Moses the Black graded B", 2026-11-26). Gregory of Nyssa stays F.

## Overall

The overall grade is the lower of the two. F: must be redone. D: should be redone. C: would benefit. B: OK to keep. A: great as is. `grade.py` computes every grade from the files here and writes `Grades.csv`, `Grades.json` and `Rebuild_Order.csv`.

`Rebuild_Order.csv` ranks all 272 by overall grade, then reach, in Mark's order: the first-visit tour (Josephus is the one person it opens), major (every council counts as major), a home in a built world, a living home. The home is the census `toldWithin`.

## Result

See `Grades.csv` and the page for Mark (https://claude.ai/artifact/KGibkbmL7Rh6hBHdjgqi6g).

| Overall | Action | All | Kit batches (98) | Before the kit (174) |
|---|---|---|---|---|
| F | must be redone | 152 | 24 | 128 |
| D | should be redone | 29 | 14 | 15 |
| C | would benefit | 73 | 44 | 29 |
| B | OK to keep | 17 | 15 | 2 |
| A | great as is | 1 | 1 | 0 |

- Rigor: F 141, D 29, C 70, B 31, A 1. Craft: F 53, D 51, C 74, B 88, A 6.
- **Kit against before the kit, on craft:**
  - The listener called 6 kit stories summaries, and 97 from before the kit.
  - They would leave 1 kit story and 46 from before the kit.
  - Average blocking faults: 3.1 for the kit, 4.3 before it.
  - Kit craft: F 1, D 5, C 37, B 50, A 5.
- **On rigor:**
  - 156 of the 174 stories from before the kit name a modern editor, scholar or "later writers" in the text, with 727 held findings in all. 118 of them are rigor F.
  - In the kit batches 60 of 98 have at least one such finding, with 123 in all, and 23 are rigor F.
- **Guesses.** Before Mark's ruling, 16 of the kit's Fs rested on one guess told as the record, most of them a hedged date: "probably in 256", "in 336 by the usual dating", "The date is disputed". With hedged dates counted as ordinary modern findings, 5 kit stories leave F (29 to 24). 8 kit stories and 15 from before the kit are still F on a guess about an author, a place, a cause or a person.
- **References:** Basil C, Epiphanius C, John Chrysostom B.
- **Councils:** the five kit councils grade F 1 (Ephesus 431), C 4. The seven before the kit grade F 5, C 1, B 1.
- **Openings:** 59 of the kit stories and 137 of those before it lose the listener in the first three sentences, nearly always on when.

## Files

- `Set.json`: the 272 stories, with batch, kind, reference, words, floor, scan source and reach.
- `build_set.py`: builds the set and the packets.
- `packets/`: what each reader read (`L` listener, `S` scans).
- `listener/`: the listener reads.
- `scans/`: the 187 stories' scans, matching, third reads and held findings.
- `trust/`: the three trust reads and the texts they read.
- `Grades.csv`, `Grades.json`: every grade, with its basis.
- `Rebuild_Order.csv`: worst grade first, then reach.
- `Hedged_Dates.json`: the guesses that are hedged dates only, counted as modern findings.
- `grade.py`: computes every grade.
