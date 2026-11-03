# V3: the reader harness and human packets

**Owner:** engine thread. **Model:** Sonnet. The work is mechanical and the rubric is already written.

**Purpose.** Turn the run records into blind reader requests, collect the replies, and report the scores per dimension and per arm. It also builds the human source packets.

**Outputs.**
- **Reader requests.** One request per answer for each of two `judge-reader` helpers. Each request holds the rubric from `../Rubric.md`, the question, the answer, the cited records, and the source lines with their context. It holds no arm label and no reading card. Answers are shuffled with a seed written before the draw.
- **Trap check.** After the blind replies are filed, a second request per authored question shows its trap note.
- **Score tables.** Per dimension, arm and world:
  - mean and distribution;
  - the noise floor, which is B run 1 against B run 2;
  - reader agreement, both exact and within one point;
  - error counts by type and severity.
- **Human packets.** 24 questions per arm for A-live and B run 1, 8 per world, weighted toward hard cases 1–7. Each comes as a readable page with the source text, plus a blank error log.

**May touch.** A new `v7_read.py` in `engine/m3/`, its tests, and the run folder under `../Runs/`. **Must not touch.** The engine's turn path, records, and V1's frozen set.

**Tests written first.**
1. No request contains an arm name, a reading card, or a run id that reveals the arm.
2. The shuffle reproduces from its seed.
3. Agreement is computed correctly on a fixed example.
4. The human sample has the stated counts per world and per case.

**Done when.** The tests pass, and a dry-mode run from V6 produces the tables.

**Cost.** None.
