# Stage 1: the AI domain specialist and the gold set (S1-02, S1-03, S1-04)

Working notes of the specialist and gold set thread. Decisions are in
`../Decision-Log.md`; elapsed time is in `../Stage1_Ledger.md`. Code is in
`Sandbox/Answering-From-Sources/goldset/` and `engine/m3/gate_replay.py`.

## Said plainly: this is weaker than human labelling

Mark ruled there is no human domain specialist (Decision-Log entry 2). The gold
set is labelled by an AI model, and every number measured against it inherits
that model's blind spots. A model can share a misreading with the judges it is
checking, especially when they come from one vendor. It can be confidently
wrong about a Latin idiom, an editor's note or a speaker inside a polemic, in a
way no automated check sees.

How the weakness is contained, mechanism by mechanism:

1. **Tested before trusted.** Seeded defects are planted in the labelling
   stream. The specialist's labels count only after it catches at least 19 of
   20 on a test set it has never seen. The tryout set that picks the model is
   not reused for the qualifying test.
2. **False alarms published beside catches.** Every test set carries 20
   controls, sentences copied from a record's own text and bound to it. A
   labeller that flags everything catches every seed and fails every control;
   both numbers are published together.
3. **Every verdict bound to exact words.** The labeller must copy the words that
   support or refute the sentence and name the block they come from. Code
   rejects any reply whose words are not in that block verbatim; one retry, then
   the line stays unlabelled and counts as a miss.
4. **Blind.** The labeller sees the sentence and its evidence pack only: never
   the question, the gates' decision, any judge's verdict, or which lines are
   seeds.
5. **A second, different model** labels at least a fifth of the gold set
   (S1-03). Every disagreement goes to Mark.
6. **Mark's eyes on the key classes.** Every specialist-versus-judge
   disagreement in false friend, negation and modal shift, generalisation,
   embedded voice and claims about what the period lacks goes to Mark, plus a
   random sample of the rest, within 2 hours a week.
7. **Held-out half sealed** by hash before any judge is tuned; only the trial's
   final scoring reads it (a test in CI enforces this).
8. **Outside referees** stay a second independent reading, and external human
   experts test the built system at the end, before any promotion.

What none of this fixes: a misreading the specialist, the second labeller and
Mark all share. The seeded types cover four failure shapes, not all of them.

## The pieces

| Piece | What it does | State |
|---|---|---|
| `engine/m3/gate_replay.py` | Replays each of the 308 saved drafts through the run's own shaper at the run's own commit, no model call, and keeps every sentence's verdict | Done: 308 of 308 shipped answers reproduced exactly, 11 worlds |
| `goldset/pool.py` | Every draft sentence bound to a record, with its binding and the gates' decision | 3,550 items (lpc 280); 10 not matched to a replay row, left out |
| `goldset/evidence.py` | Evidence pack: bound records as the voice saw them (records at the package's commit), source passage with its division, editors' notes marked, original language where the locus names it, the world's lexicon risk flags | Passage found for 236 of 280 lpc items; far fewer in worlds whose loci give section numbers, not lines (see below) |
| `goldset/labeller.py` | Prompt, reply schema, verbatim-evidence check | Done |
| `goldset/seeds.py` | Seeded defects by fixed rules, controls, three test sets | 60 defects (15 per type) and 60 controls accepted after reading (`Seed_Readings.yaml`) |
| `goldset/stream.py` | Blind stream with seeds planted, key kept apart | Tryout stream (40 lines); first lpc stream (280 items + qualifying set, 320 lines) |
| `goldset/runner.py` | Runs a labeller under the live-test guard; settings and estimate first | Not run: waits for the model choice, a cap and sample approval |
| `goldset/catch_rate.py` | Catch rate and false alarms per test set | Done |
| `goldset/split.py` | Calibration and held-out halves by hash of id; seal | Done |

## Known limits of the tooling

- **Passage location outside lpc.** Most worlds' record loci name a section
  ("Vita Antonii SS3", "Letter XXII, sec. 30"), not file lines. The pack then
  shows the record and says the source was not located. Located: lpc 236/280,
  gallic 365/444, witt 185/310; most others under a third. A locus resolver for
  section references (the proposal's planned `locus_ids` row field would remove
  the need) is the next tooling step before other worlds are labelled.
- **False-friend seeds come from the lexicon flags.** They test whether the
  labeller uses the risk flags it is given, not whether it spots an archaic
  English sense nobody flagged ("prevent" for "go before"). Natural items and
  Mark's adjudication carry that class.
- **Embedded-voice seeds** are the opponents' or outsiders' words inside a
  record, voiced as the tradition's. Nine were written by hand from named
  records, since the fixed rule reaches etic records only.
