# V3: reader harness and human packets

**Owner:** engine thread. **Model:** Sonnet. The work is mechanical and the rubric is written.

**Purpose.** Turn A's and B's answers into blind reader requests. Collect the replies. Report scores per dimension and per arm, set beside the October reviews of A. Build the human source packets.

**Outputs.**
- **Reader requests.**
  - One request per answer, for each of two `judge-reader` helpers: 84 A answers, 84 B answers and 42 B repeats, so 210 answers and 420 reads.
  - Each request holds the rubric from `../Rubric.md`, the question, the answer, the cited records, and the source lines with their context.
  - Each request holds no arm label, no reading card and no October grade.
  - Answers are shuffled with a seed written before the draw.
- **Option set.** If Mark takes the option, a trap-note check follows the blind replies.
- **Score tables.** Per dimension, arm and world:
  - the mean and the distribution;
  - B's noise floor (run 1 against run 2 on the 42 repeats);
  - the older-engine band for A, from `engine/m3/reports/baseline-2026-10-02/`;
  - reader agreement, exact and within one point;
  - error counts by type and severity.
- **October comparison.**
  - On A, the fresh dimension 1–3 and 10 scores set against the second-pass rigor and access grades.
  - Each known A error, marked as repeated or not repeated in B.
- **Human packets.** The same 12 probes per world in both arms, weighted toward quote-placing answers and the T and E registers: 72 answers. Each is a readable page with its source text and a blank error log.

**May touch.** A new `v7_read.py` in `engine/m3/`, its tests, and `../Runs/`.
**Must not touch.** The turn path, the records, and V1's frozen files.

**Tests written first.**
1. No request contains an arm name, a reading card, an October grade, or a run id that reveals the arm.
2. The shuffle reproduces from its seed.
3. Agreement is computed correctly on a fixed example.
4. The human sample has 12 per world, with the same probes in both arms.

**Done when.** The tests pass, and V6's dry-mode answers produce the tables.

**Cost.** None.
