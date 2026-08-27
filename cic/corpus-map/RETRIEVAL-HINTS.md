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
nor a canon question: the cell scorer itself, which let common words carry
a cell.

FIXED 2026-08-27, in engine/m4/evidence.py, and the shape of the fix
matters to anyone reading this before writing hints. The scorer no longer
counts every shared word equally. A word keeps full weight up to four
cells - which is 95% of the canon's vocabulary, left untouched - and past
that it tapers as 4/df with a floor of 0.25, so `people` (17 cells) is
worth a quarter of `heart` (one cell) rather than the same.

Six weightings were measured over three instruments before one was chosen,
and a textbook idf was among the losers: it fixed the probe but cost a
ground record, a quote and a family-level match. The shipped taper fixes
the same probe at NO measured cost on either instrument - 466 ground / 67
cells / 0 empty / 79 quotes on the locked sixty, and leave-one-out family
accuracy 17/93, both identical to the flat scorer it replaces.

WHAT THIS MEANS FOR HINT WRITING: rule 7's warning about framing verbs is
now partly enforced by the scorer rather than only by discipline. A hint
built from `people`, `believe`, `know` and `like` contributes real
vocabulary but weak evidence, while a hint whose words are specific to its
subject is worth several times more per word than it used to be. Write the
distinctive noun.

### Two defects a live turn found that no probe had

Recorded 2026-08-27, from three billed turns against desert. The first two
were good. The third asked "You've given me two different pictures there.
Did your own people disagree about this?" and the voice answered, at
length and well, about whether women could be elders - a question nobody
had asked.

**CONTRACTIONS WERE EVIDENCE.** The apostrophe is a word character in
engine/prose.py's tokenizer, so `you've` was a content word like any noun.
That turn routed to F6-P on `people` and `you've`, and to F2-E on `given`
and `you've`. Fourteen apostrophe tokens sat in the canon's own cell
vocabularies, `isn't` in four cells. Twelve are now stopwords; `women's`
and `world's` are deliberately not, being possessives of content nouns.
Fixed, at no cost to the locked sixty.

**RETRIEVAL HAS NO MEMORY, AND THE MODEL DOES.** This one is NOT fixed and
is the more important of the two. A follow-up whose subject is `this`,
`that` or `there` carries almost no retrievable content - strip the
pronouns from the question above and you are left with `different`,
`disagree`, `pictures`, `two`, none of which is in any cell. The
conversation was in the prompt (the voice had two prior turns replayed and
plainly understood them), but the GROUND was assembled from the follow-up's
own words alone, and the voice answered from the ground it was handed.

So the failure mode to know about: **a good answer to a question nobody
asked, on any follow-up that refers back rather than restating.** That is
common in real conversation and the corpus cannot hint its way out of it -
no wording in any record helps when the query has no subject in it.

The fix is architectural, not editorial: Stage A would need the prior
turn's cells to fall back on when a message yields none of its own.
match_asks_to_cells takes no history today, so this is an interface change
and wants its own design and measurement. Written up here so the next
person to see a strange follow-up answer knows where to look.

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
