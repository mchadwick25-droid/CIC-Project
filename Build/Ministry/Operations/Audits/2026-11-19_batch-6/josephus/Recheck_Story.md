# Recheck: Josephus (story)

Batch 6 independent checker, 2026-11-19. Read against `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `josephus.brief.txt` and `josephus.brief.v1.txt`.

**Verdict: PASS.**

## 1. Review findings

- **B1:** fixed. "which is disputed still" is gone.
- **B2:** fixed. The genuine side is now told.
- **MINOR 1:** fixed. Jerome is given his time.
- **MINOR 2:** fixed. The sentence about 66 is cut.

Both Do not say lines are now in the outline, at l.136–137. No finding is left unfixed.

## 2. New wording

The diff against v1 touches only the review's sentences.

- "Some, he wrote, thought a Christian copyist had added it all, others only part, and a few still held it wholly his own." It is checked against `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` 9182–9194:
  - "considered genuine until the sixteenth century, but since then has been constantly disputed";
  - "(1) It is entirely genuine. This view has at present few supporters";
  - "(2) It is entirely spurious";
  - "(3) It is partly genuine and partly interpolated".
  
  Every view is credited to him with "he wrote", and none goes past what he says. "Still held" is past tense and set in 1890. It is not a present-tense claim. Leaving out Ewald's fourth view tilts nothing, and the review allowed it.
- "Jerome's Latin, later in the fourth century, reads…": What came 3 (Outline l.57) and I3.
- "…and argued over the passage on Jesus.": the essence (l.5).

## Mark's ruling (Decision-Log, "Batch 6 hearts approved…", item 2)

**Holds in the story.**
- The old witnesses are each credited beside their own claim: Origen, Eusebius and Jerome.
- The dispute is credited to "an editor of Eusebius" in 1890.
- McGiffert's views are given on both sides, each credited.
- The narrator takes no side, and nothing claims a current verdict.

The card note and the Library want are outside this story recheck. I found no Josephus entry yet in `Build/worlds/_cross-world/WANTS-REGISTER.md`.

## 3. Kit lines

- Hook: three sentences, with the name in the first.
- Essence complete at word 145, "…the passage on Jesus."
- Every "also told" part is present.
- Every listed word that the story uses gets its plain sense at first hearing: priest, Galilee, Jotapata, Vespasian, the Christ, high priest, providence and Pilate.
- The longest sentence is 31 words, the ending, which the review kept.
- Length is 594 words. Nothing is listed as unneeded.
- The setting comes a clause at a time.
- The story ends on Josephus's own words.

## 4. Score

`python -m engine.m1.profile_readability …/josephus.brief.txt`: 594 words, grade 8.6 (names out 7.6), reading ease names out 72.7, 18.0 words a sentence, longest sentence 31 words. **Pass.**
