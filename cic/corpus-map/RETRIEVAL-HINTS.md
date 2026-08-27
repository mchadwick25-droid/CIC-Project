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
