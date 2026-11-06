# Answers-the-question verdict, Step 1 (measure only), 2026-11-02

The check is the `answers` entry in the existing read's one JSON reply (`engine/m4/answer_check.py`). It changes nothing that ships.

Inputs: the 112 new answers of the cross-world baseline (alx, syr, rzg, lpc, q001 to q028), read-prompts regenerated with the new read system text (`read/prompts`), replies written by seven read helpers that saw no ratings (`read/replies`), imported through `test100_check import` (`read.jsonl`, field `answers`). Compared with the blind Opus ratings in `Cross-World-Test_2026-11-02/ratings` (`answers_question`).

Target stated before the run: no blind "no" read as "yes" on more than 1 in 10; whole 3x3 table reported.

| blind \ read | yes | partly | no |
|---|---|---|---|
| yes | 44 | 10 | 0 |
| partly | 10 | 25 | 2 |
| no | 2 | 8 | 11 |

n 112, no verdict missing. Blind "no" read as "yes": 2 of 21 (9.5%). Exact agreement 80 of 112 (71%).
Limits: readers are helper agents, not the production model; one read per answer; the blind labels are one Opus reader's.
