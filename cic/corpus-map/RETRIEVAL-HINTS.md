# Writing `retrieval.retrieve_when` — the discipline

Every quote record needs a hint. Without one, a quote contributes nothing
to WHICH cell a question reaches, and surfaces only when its cell is picked
for other reasons — every story carries a hint; a quote should too.

## What a hint is

`retrieval.retrieve_when` is a list of sentences describing the
PARTICIPANT'S SITUATION in which this record should be reached. Its words
are unioned into the vocabulary of every cell in the record's own
`canon_cells`, and that widened vocabulary is scored against the turn's
message. So a hint is not documentation. It is retrieval vocabulary, and
whatever words you put in it are the words that will reach this record.

## The seven rules

1. **Describe the ASK, never the ANSWER.** "participant asks what a monk
   ate" — not "this record shows the diet was bread and salt". The
   participant does not know the answer; their words are the ones that
   have to match.

2. **Never write the question you hope to answer.** Hint words are merged
   into the cell's vocabulary, so a builder who writes their hoped-for
   question can score any cell at 1.0 — writing a hint from a failed
   probe's own wording can make that probe go green for reasons that have
   nothing to do with retrieval getting better. THE TEST: would you have
   written this hint before seeing any probe? If it exists only because a
   probe failed, it is overfitting, and it will look like success.

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
   between `baptise` and `baptism`, or between `think` and `thought`. A
   hint that names the concept without every plausible spelling can still
   miss a participant's own wording (`baptise`, `baptize`, `babies`) — if
   a participant might type two spellings of the word, both go in.

7. **Framing verbs are a cost, not a bonus.** A hint reading "what a
   bishop wrote to settle a dispute" puts `wrote` and `write` into that
   cell's vocabulary, and "Can you write me some code?" then reaches two
   cells. The retrieval tiers can only partly defend against this - a
   one-word query may match a hint word, a two-word query may not,
   precisely because of it. Name the subject; keep the verb plain.

## What a hint cannot do

A hint only widens cells the record already claims in `canon_cells`; it
cannot move a record to a cell it isn't in. Two questions decide what to do
when a real participant question never reaches the record that should
answer it:

1. **Are the record's cells wrong?** Fix them — moving a record to the
   cell it actually answers is worth more than any hint, and no hint can
   substitute for it.
2. **Does the canon have no question carrying that word at all?** Then
   it's a canon gap: add a `[measured]` question to Appendix A of the
   Program Spec. A two-word query can be decided by a lone CANON word but
   not by a lone HINT word, so putting the missing word in a hint leaves
   it stranded — that is a spec change, not a hint fix.

Writing a hint for either case is rule 2 overfitting dressed as a fix.

## Known scoring behavior worth knowing before writing hints

- **Word weight tapers by how common the word is across cells.** A word
  keeps full weight up to four cells (95% of the canon's vocabulary, left
  untouched); past that it tapers as `4/df` with a floor of 0.25 — so a
  word that appears in many cells (e.g. `people`, 17 cells) carries a
  fraction of the weight of a word specific to one cell (e.g. `heart`, one
  cell). This partly enforces rule 7 at the scorer level, not just by
  discipline: a hint whose words are specific to its subject is worth more
  per word than a hint built from common words like `people`, `believe`,
  `know`, `like`.
- **Only the top-scoring cell(s) are kept.** A broad cell can outscore the
  right one on generic shared words even when the record that should
  answer lives in a narrower cell — write the distinctive noun, not the
  generic verb, to keep the right cell on top.
- **The apostrophe is a word character in `engine/prose.py`'s tokenizer**,
  so contractions like `you've` are content words like any noun.
  Contraction stopwords (`isn't`, `you've`, and the rest, except
  possessives of content nouns like `women's`/`world's`, which are
  deliberately not stopped) keep contractions from pulling unrelated cells
  into a match.
- **A follow-up question inherits the cells of the last participant
  message that stood on its own.** A message like "Say more about that."
  or "And then?" carries a back-reference and almost no evidence of its
  own; on its own words it would match whatever generic cell shares its
  few content words, rather than the cell its subject is actually in. This
  is deliberately narrow: it fires only on a back-reference (`this`,
  `that`, `it`) combined with weak evidence of the follow-up's own, not on
  a back-reference alone (most canon questions contain one of those words
  and still name their own subject) and not on a follow-up with no marker
  at all ("Tell me more.", "Did they all think so?" stay out of scope,
  since a looser rule would also catch real questions). A first turn has
  no history and is unchanged by this; chains resolve to the last
  self-standing question, not to each other.

## The cost is real and shows up immediately

Widening hints (or the scoring/follow-up behavior above) to fix one
question can cost ground elsewhere on the benchmark — wider hints displace
candidates that used to rank. Report the regression alongside the gain; a
hint pass with no reported cost has probably not been measured.

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
