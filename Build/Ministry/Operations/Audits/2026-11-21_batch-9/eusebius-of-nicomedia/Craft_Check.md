# Craft check: Eusebius of Nicomedia (`eusebius-of-nicomedia`)

**FIX** (one sentence)

File note: the pass reversed the two files. `eusebius-of-nicomedia.brief.txt` still holds the pre-pass text, and the edited text is in `eusebius-of-nicomedia.brief.v2.txt`. This check reads `brief.txt` as before and `.v2` as after. When the edits are applied, the after text belongs in `brief.txt` and the before text in `.v2`.

1. Nothing is added or dropped. All three quotes and the short quoted spans are word for word. Eustathius is now given by role, which the outline allows. In the grain-ship sentence, Socrates is still credited, in "a charge Socrates calls slander". The sentence before also names him as the witness, so the report is not cut loose from its source.
2. "Though" adds a contrast that the outline holds (one says she was bribed; Philostorgius tells her charge as true). No "so" or "because" was added. "That choice set the course of his life" is the fresh read's wording, and the essence that follows bears it out. **One sentence now says more than its source:** "before the bishop of Rome had ruled on Athanasius". Socrates says only that Eusebius "did not live to learn the decision of Julius concerning Athanasius" (SOC 6175-6177). Sozomen says he died "before he had been able to ascertain the sentiments of Julius" (SOC 31174-31175). Neither says the ruling had not yet been made.
3. The essence is complete by about word 115. The life is told once, in order. It ends on the two verdicts on him.
4. The meta line, the name load and the run of "X says" are all better. The Rome sentence is clearer, but it is less exact (point 2).
5. 673 words before and 669 after. `python -m engine.m1.profile_readability` passes on `.v2`: grade 9.2, reading ease 73.7, longest sentence 30.

## Fix

Replace:
> Eusebius died soon after the meeting at Antioch, before the bishop of Rome had ruled on Athanasius.

With:
> Eusebius died soon after the meeting at Antioch, before he learned the bishop of Rome's ruling on Athanasius.

This adds one word, which brings the story to 670. That is still under the 673 it had before the pass.

## Applied (coordinator, 2026-11-22)
The craft pass had written the edited text to `.v2` and left the pre-pass text in `eusebius-of-nicomedia.brief.txt`; the two were swapped, so `.v2` now holds the pre-pass text as the prompt intended, and the fix above was applied word for word to the brief.
