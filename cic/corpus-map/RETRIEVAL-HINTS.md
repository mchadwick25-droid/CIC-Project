# Writing `retrieval.retrieve_when` — the discipline

Added 2026-08-27, when 125 of 125 quote records across six worlds were
found to carry no hint at all while every story carried one. Quotes
therefore contributed nothing to WHICH cell a question reached and
surfaced only when their cell was picked for other reasons.

## What a hint is

`retrieval.retrieve_when` is a list of sentences describing the
PARTICIPANT'S SITUATION in which this record should be reached. Its words
are unioned into the vocabulary of every cell in the record's own
`canon_cells`, and that widened vocabulary is scored against the turn's
message. So a hint is not documentation. It is retrieval vocabulary, and
whatever words you put in it are the words that will reach this record.

## The five rules

1. **Describe the ASK, never the ANSWER.** "participant asks what a monk
   ate" — not "this record shows the diet was bread and salt". The
   participant does not know the answer; their words are the ones that
   have to match.

2. **Never write the question you hope to answer.** Measured, in this
   project, on 2026-08-27: three desert quotes were hinted with wording
   lifted from the probe questions that had failed, and the probe went
   green for reasons that had nothing to do with retrieval getting
   better. Hint words are merged into the cell's vocabulary, so a builder
   who writes their hoped-for question can score any cell at 1.0. THE
   TEST: would you have written this hint before seeing any probe? If it
   exists only because a probe failed, it is overfitting, and it will
   look like success.

3. **Use the participant's words, not the record's.** The record says
   `apatheia`; the participant says "did you stop feeling things". The
   hint's whole job is to bridge that gap, so a hint that repeats the
   record's own vocabulary does nothing the record's text did not
   already do.

4. **Hints cannot move a record between cells.** They only widen cells
   the record already claims in `canon_cells`, and a cell the fleet does
   not define is ignored. If a record is unreachable because its cells
   are wrong, FIX THE CELLS. A hint written to paper over a bad cell
   assignment is a lie about what the record is.

5. **Two or three lines. Different angles, not synonyms.** Scoring is
   word overlap; five restatements of one idea add one idea's worth of
   vocabulary and a lot of noise. Prefer one line on the subject, one on
   the situation that prompts it, one on the adjacent question a
   participant actually asks instead.

6. **Write the participant's SPELLING, not just their concept.** The
   canon and hint tiers compare words literally - there is no stemmer
   between `baptise` and `baptism`, or between `think` and `thought`.
   Measured: pahc.term.baptisma already hinted "baptism, initiation,
   coming to the water", and "Did you baptise babies?" still reached
   nothing, because not one of `baptise`, `baptize` or `babies` was on
   the page. If a participant might type two spellings of the word, both
   go in.

7. **Framing verbs are a cost, not a bonus.** A hint reading "what a
   bishop wrote to settle a dispute" puts `wrote` and `write` into that
   cell's vocabulary, and "Can you write me some code?" then reaches two
   cells. The retrieval tiers can only partly defend against this - a
   one-word query may match a hint word, a two-word query may not,
   precisely because of it. Name the subject; keep the verb plain.

## The structural limit: what a hint cannot do, measured

Added 2026-08-27, after the Evagrius and Macarius reading passes, when the
question was put directly: do newly opened sources INFORM ALONGSIDE the
existing ones, or only fill the gaps their own hints name?

Twelve interior-life questions were probed against desert. Hints written in
participant idiom moved nine of them onto the new records. Three did not
move, and the reason matters more than the number:

    "Does God ever feel like anything, or is it only believed?"
        -> routed to F6-P and C-P. The Macarian records claim F1-I, F1-P.
    "I became a Christian and nothing changed. What is wrong with me?"
        -> routed to F3-I and C-I. The record claims F1-P, F1-T.
    "You talk about the heart a lot. What did you mean by it?"
        -> routed to NO cell at all; `heart` is in no canon question.

None of these is a hint problem, and writing a hint for any of them would
be rule 2 overfitting dressed as a fix. Rule 4 is the reason: **a hint only
widens cells the record already claims.** If the router sends a question to
F6-P and your record is in F1-P, no wording in that record's hints can
reach it - the cell was decided before the record was ever scored.

There are exactly two honest remedies, and the first is usually right:

1. **The record's cells are wrong.** Fix them. In this same pass six
   Evagrius quotes were assigned F5-I - which is ordinary daily life, food,
   work, children - when the eight logismoi and the noonday demon plainly
   answer F4-P, "I can't quiet my own head." Moving them was worth more
   than any hint, and it was rule 4 that caught it.

2. **The canon has no question with that word in it.** Then it is a canon
   gap, and it goes to Appendix A of the Program Spec, not into a hint.
   `heart` is the current instance and is the same shape as `neighbours`
   was: a two-word query can be decided by a lone CANON word but not by a
   lone HINT word, so putting the word in a hint leaves it stranded. That
   is a spec change and belongs to a human.

### What the canon fixed, and what it did not — measured 2026-08-27

Three `[measured]` questions were added to Appendix A for the three cases
above and the canon reseeded (90 -> 93). One was closed outright and two
were not, and the difference is instructive.

CLOSED. "You talk about the heart a lot. What did you mean by it?" went
from NO CELL AT ALL and three ground records to one cell and three of the
new records. That is the `neighbours` pattern exactly: the word existed
nowhere in the canon, so no hint could rescue it, and one canon question
carrying `heart` did. On the locked sixty-question benchmark the same three
questions took the fleet from 461 ground / 64 cells to 466 / 67 — alx and
ijc gained as well as desert, which is the fleet-wide canon doing
fleet-wide work.

NOT CLOSED, and this is a limit of the ROUTER, not of the corpus:

    "Does God ever feel like anything, or is it only believed?"
        F6-P scores 0.5 on `ever`, `god`, `like`. F1-P, which holds the
        new question and the records, does not make the top two.
    "I became a Christian and nothing changed. What is wrong with me?"
        F3-I scores 0.6 on `became`, `christian`, `wrong`.

Adding the participant's word forms to the hints (`feel` beside `felt`,
`changed` beside `same person` — rule 6, and worth doing on its own terms)
changed neither, and the locked sixty did not move either. The reason is
that only the top-scoring cells are kept: **a broad cell can outscore the
right one on generic words.** `ever`, `god`, `like` are not about the hard
places, but F6-P holds enough of them to win, and once it wins, nothing in
a record that lives in F1-P can be reached.

So there is a third remedy beyond the two above, and it is neither a hint
nor a canon question: the cell scorer itself, which currently lets common
words carry a cell. Recorded here rather than acted on — changing how
routing scores is an engine change with fleet-wide blast radius, and it
wants its own measurement, not a patch appended to a hint pass.

## The cost is real and shows up immediately

The same rewrite that moved nine probe questions onto the new records cost
one ground record and one quote on the locked sixty-question benchmark
(462/80 -> 461/79, both in desert). Wider hints displace candidates that
used to rank. Report the regression alongside the gain; a hint pass with no
reported cost has probably not been measured.

## What to do about a record you cannot hint honestly

Leave it. A quote whose only honest retrieval condition is "the
participant asked about this exact thing" is already reachable through
its cell, and a padded hint costs vocabulary precision for every other
record in that cell.

## How to tell whether a batch of hints helped

Write the benchmark FIRST, from the world's own subject matter, before
reading the records you are about to hint. Measure, hint, re-measure.
Report regressions as well as gains — vocabulary bloat is a real cost
and it shows up as cells matching questions they should not.
