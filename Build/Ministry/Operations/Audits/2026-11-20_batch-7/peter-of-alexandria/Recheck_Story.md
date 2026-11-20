# Story recheck: Peter of Alexandria

Batch 7, 2026-11-20, per `Recheck_Story_Prompt.md`. Read: `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, the brief and `peter-of-alexandria.brief.v1.txt`.

## Verdict: FIX

One fix: a sentence of 32 words in the essence, which the revision created.

## 1. Review findings

- **B1 (Nicaea outside the first minute).** Fixed in substance. The essence now ends on the rival church coming before Nicaea, at word 128, with the plain sense of the council given at first hearing. Paragraph 9's "In 325 that council, at Nicaea, took up this same quarrel." does not tell it twice. The Do not say line is in `Outline.md` (line 134).
- **M1 to M3.** Each is applied as the review gives it.

## 2. New wording (every sentence that differs from v1)

- "...starting a rival church that outlived him and came before the first great council of the whole church, at Nicaea.": outline essence (line 5, "came before the Council of Nicaea") and beat 2 of What came ("the first great council of the whole church").
- "Those who had given way now asked for communion again, to share the Lord's Supper with the church.": outline Also told, beat on the rules. It claims no number, so it says less than v1's "Many".
- "Melitius, a bishop in Upper Egypt,": the Thebaid gloss.
- "Epiphanius, writing seventy years on, says the two were in prison together and split over the fallen.": v1's wording with the hinge removed. The claim stays in Epiphanius's voice.
- "In 325 that council, at Nicaea, took up this same quarrel.": What came 2 (I2; SOC 3203–3212).

There is no new quote. Each says no more than its source.

## 3. The kit lines

- **Hook:** three sentences with Peter's own words, then one sentence of plain sense. He is named at once.
- **Essence:** complete at "at Nicaea.", word 128.
- **Also told:** all present: the rules in his words, the break told from both held sides, Eusebius on the death, and the rules sealed as church law in 692.
- **Words to explain:** each one used gets its plain sense at first hearing: the fourth Easter, the marks of Jesus, communion, ordain, removed, the followers of Melitius and Upper Egypt.
- **Sentences:** one runs past about 30 words (see the fix). The rest are 29 words or fewer.
- **Length:** 636 words by the scorer, about 4:14. That is under the ceiling of about 675 words. Nothing is listed as unneeded.
- **Setting:** not stacked: around 300, 303, 306 and 311 each come in their own clauses.
- **Ending:** on Peter: Athanasius calls him blessed, a bishop and a martyr, and Alexandria keeps his day.

## The fix

Paragraph 2 holds a 32-word sentence. It is the essence's last sentence, heard in the first minute. Replace:

"During the persecution, too, one of his own bishops, Melitius, broke away, starting a rival church that outlived him and came before the first great council of the whole church, at Nicaea."

with:

"During the persecution, too, one of his own bishops, Melitius, broke away, starting a rival church that outlived him. That church came before the first great council of the whole church, at Nicaea."

The split adds two words, so the story is about 638 words. The essence is then complete at about word 130.

## 4. Score

`python -m engine.m1.profile_readability .../peter-of-alexandria.brief.txt`: 636 words, grade 8.2 (names out 7.3), reading ease names out 71.4, longest sentence 32 words, pass.
