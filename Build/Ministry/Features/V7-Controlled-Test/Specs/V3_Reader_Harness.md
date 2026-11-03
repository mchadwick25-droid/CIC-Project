# V3: reader harness and human packets

**Owner:** engine thread. **Model:** Sonnet. The work is mechanical and the rubric is written.

**Purpose.** Turn A's and B's answers into blind reader requests. Collect the replies. Report scores per dimension and per arm, set beside the October reviews of A. Build the human source packets.

**Outputs.**
- **Reader requests.**
  - One request per answer for each of two Opus readers: 84 A answers, 84 B answers and 42 B repeats, so 210 answers and 420 reads.
  - Each request holds:
    - the rubric from `../Rubric.md`;
    - the question and the whole answer;
    - every cited record, with its reading card where one exists, marked as project-authored;
    - the source passage with its surrounding division, read from `cic/texts/` at the record's locus;
    - the world's lexicon risk flags.
  - Each request holds no arm label and no October grade.
  - Answers are shuffled with a seed written before the draw.
- **Seeded copies.** At least 10 copies of real answers, each carrying one planted defect from the four kinds in `../Test_Plan.md` §6. They are written by a thread that does not read, and shuffled in among the rest. Their key is sealed by SHA-256 until scoring ends.
- **Adjudication requests.** A third Opus pass gets every item where the two readers disagree by more than one point on a dimension, and every tier 1 or tier 2 finding. It sees both readers' findings and the full context.
- **After scoring.** The October review of each A answer is shown to the readers once their scores are filed, so they can add errors marked "after October review".
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
- **Mark's review data.** The same 12 probes per world in both arms, weighted toward quote-placing answers and the T and E registers: 72 answers.
  - The output is one JSON file that the review page (V9) loads, with the arm hidden.
  - Each item holds the question, the answer, the cited records, and the source lines in context, kept short.

**May touch.** A new `v7_read.py` in `engine/m3/`, its tests, and `../Runs/`.
**Must not touch.** The turn path, the records, and V1's frozen files.

**Tests written first.**
1. No request contains an arm name, an October grade, or a run id that reveals the arm.
   - Reading cards appear on both arms' cited alx records alike, so they reveal nothing.
   - A seeded copy is indistinguishable in form from a real answer.
2. The shuffle reproduces from its seed.
3. Agreement is computed correctly on a fixed example.
4. The human sample has 12 per world, with the same probes in both arms.

**Done when.** The tests pass, and V6's dry-mode answers produce the tables.

**Cost.** None.
