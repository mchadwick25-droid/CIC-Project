# New era 1 person grades, 2026-11-28

Mark ruled that new work passes at B or with his sign-off, and that everything gets a grading run before he releases it: "i release after the grade, to make sure a c raiting is not just a small thing", "i want to see everything" (Decision-Log, "New work passes at B or with Mark's sign-off", 2026-11-28). This folder grades the 15 new era 1 person briefs on their final text, before release.

No story, card, census or kit file was changed. Every read ran as a fresh Opus subagent inside this session, drawn from the weekly allowance, with no metered spend.

## The set

`build_set.py` builds `Set.json`, `Texts.json`, `Cards.json` and the packets.
- **Josephus:** the census `longDescription` on `main`, already released.
- **Peter of Alexandria:** `claude/cft-story-peter-of-alexandria`, `Build/Ministry/Operations/Audits/2026-11-26_batch-12/peter-of-alexandria/peter-of-alexandria.brief.txt`.
- **The other 13:** `claude/cft-release-batch12-13`, each `Build/Ministry/Operations/Audits/2026-11-26_batch-12/<slug>/<slug>.brief.txt`.

All 15 run 588 to 984 words, above the person floor of about 300.

## Method

The method is `../2026-11-25_person-council-grades/`, copied unchanged. Its prompts are copied here: `Listener_Prompt.md`, and in `scans/` the reader, modern-reader and third-read prompts of `../2026-11-23_what-and-why-rank/`.
- **Scans.** All 15 briefs were scanned here, as one packet (`packets/S01.md`). None reuses an 11-23 scan, since every text has changed since. The scans were two bare-statement readers, one modern-opinion reader, and a third read on what `scans/merge.py` sends there. The readers agreed on 19 findings. 21 went to the third read, 5 of them modern, and 12 of the 21 held.
- **Listener.** One first-time listener read all 15 (`packets/L01.md`, `listener/L01.md`).
- **Hedged date.** One guess is hedged only on a date: Suetonius, "so he wrote after Domitian's death". By Mark's ruling of 2026-11-26 it counts as one modern finding (`Hedged_Dates.json`).
- **Trust read.** The method sends a trust read only to a brief that is otherwise rigor A or B and craft A. None here qualifies, so none was run.
- **Grades.** `grade.py` uses the 25 Nov rules unchanged. It adds each brief's old grade from `../2026-11-25_person-council-grades/Grades.csv`.
- **Reading level.** `Readability.txt` holds the output of `python -m engine.m1.profile_readability` on each final brief.

## Result

The page for Mark: https://claude.ai/artifact/AvZuXHP56nze2REh3uexPF

| Overall | New | Old (25 Nov) |
|---|---|---|
| F | 3 | 10 |
| D | 1 | 5 |
| C | 6 | 0 |
| B | 5 | 0 |

- **F:** Josephus, Tatian and Suetonius. Each is F on rigor for one modern guess told as the record. Suetonius is also a summary, so its craft is D.
- **D:** Methodius of Olympus, a summary on craft.
- **C:** Tacitus, Anatolius, Clement of Alexandria, Hippolytus of Rome, Origen and Lactantius.
- **B:** Pamphilus of Caesarea, Ignatius of Antioch, Peter of Alexandria, Pontius the Deacon and Valentinus.
- **Origen** fails the readability gate, at grade 10.1 and 984 words.

## Files

- `Set.json`, `Texts.json`, `Cards.json`: the set, the graded texts and the card fields.
- `packets/`: what each reader read.
- `scans/`: the reads, `merge.py`, `Merge.json`, the third read and `Held_Findings.json`.
- `listener/`: the listener read.
- `Grades.csv`, `Grades.json`, `Rebuild_Order.csv`: every grade, with its basis and the old grade.
- `Readability.txt`: reading level of each brief.
