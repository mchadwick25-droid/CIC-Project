# Spec 5: the held-out question set

**Model: Sonnet to draft the questions; code to freeze and hash.** Writing needs blindness, not depth, and it repeats across worlds.

**Purpose.** A fixed set of visitor questions, written without sight of the sub-question list or the records, so tuning cannot fit to them.

**Size (Mark's rule, 20 + 1 per 2 million shelf tokens; tokens are shelf bytes divided by four, as in the proposal, markup included; the whole number of 2M blocks).**

| world | shelf tokens (M) | questions | | world | shelf tokens (M) | questions |
|---|---|---|---|---|---|---|
| lpc | 47.5 | 43 | | rzg | 15.2 | 27 |
| ijc | 38.3 | 39 | | syr | 14.4 | 27 |
| cappadocian | 30.5 | 35 | | desert | 10.3 | 25 |
| alx | 27.4 | 33 | | hal | 8.8 | 24 |
| pahc | 20.7 | 30 | | witt | 6.4 | 23 |
| don | 17.4 | 28 | | gallic | 3.7 | 21 |

Total 355. The table matches the proposal's section 15 table, recomputed from the shelves on disk. Counting words instead of tokens would give fewer (lpc 22 instead of 43), because markup bytes count as tokens here; tokens are the approved basis.

**Inputs.** The world's identity and its shelf's list of works (titles and authors only). **Not given:** the sub-question list, the records, the seeds, any earlier bench or test question.

**Outputs.** `Design-Faithful-Build_2026-11-03/Heldout/<world>_questions.yaml` (id, text) and `Heldout/SHA256SUMS`, written once and frozen before any tuning; a change after that is a change order.

**Process.** A drafting helper that has not read the sub-question list or any record writes the questions in the register of a visitor, in the visitor's wording. A code check compares each question with the sub-question wordings and the bench's earlier questions and flags a near-duplicate (word overlap above a set share) for rewriting. Code records the count per world and the hash.

**May touch.** The new `Heldout/` folder. **Must not touch.** The sub-question list, the records, the existing bench.

**Test written first.** (1) The count per world equals 20 + floor(shelf bytes / 4 / 2,000,000), the table above. (2) No question duplicates a sub-question wording or an earlier bench question beyond the overlap limit. (3) The SHA256SUMS file matches the files. (4) The drafting helper's request file holds no sub-question id and no record id.

**Done when.** The tests pass, the set is frozen and hashed, and the counts per world are reported. **Cost:** drafting runs in-plan with no metered spend; nothing is run against a model API.
