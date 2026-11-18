# Recheck: Council of Nicaea (325)

Independent recheck, batch 4, 2026-11-18. Read against `CLAUDE.md` (Trust and source fidelity), the Brief-Kit `Standard.md`, `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `council-of-nicaea-325.brief.txt` and `council-of-nicaea-325.brief.v1.txt`.

## Verdict: PASS

## 1. Review findings

The review passed with MINOR findings only. All four are done:

- M1: the attribution clause is trimmed, and the exile now comes in the enforcement paragraph.
- M2: the review's wording "let them travel by the imperial post, with horses" is used. "Given way" is now "fallen away".
- M3: the 32-word canons sentence is split in two.
- M4: the text now reads "the bishops of Africa, meeting at Carthage" and "Caecilian, once their bishop, had sat at Nicaea".

**"Fallen away" without "from the faith".** The meaning holds. Canon 11 concerns "those who have fallen without compulsion ... as happened during the tyranny of Licinius" (`cic/texts/npnf214_seven-ecumenical-councils.xml` 4124–4128; M14). Its "fallen" means the lapsed, people who gave up the faith under pressure. In plain English, "fallen away", with no object, carries that sense. With "mercy" and "without being forced" beside it, the sentence keeps the canon's meaning. It says no more than the source, and it is truer to the source's "fallen" than v1's "given way".

## 2. New wording

- "When his letter to Alexandria failed, Constantine called the bishops to Nicaea, in today's Turkey, and let them travel by the imperial post, with horses": K3, S4 (EUS 64282–64288, "public means of conveyance ... an ample supply of horses"); S1 for "in today's Turkey".
- "They ran from how a bishop is made to mercy for those who had fallen away under the emperor Licinius without being forced": beat 7; M14 (canons 4 and 11).
- "He sent Arius into exile, a historian a century later says": M11 (Socrates, LATER, credited). "He" is the emperor of the sentence before.
- "About ninety years after Nicaea, the bishops of Africa, meeting at Carthage, found a disputed rule missing from their copy, and wrote east for exact copies": I4 (NC 32157, 32490–32533).
- "Their own copy held the creed and the twenty rules, and they read it aloud as law": I4 (NC 32538–32545); the outline's Connection line, "read that copy aloud as law".
- "Caecilian, once their bishop, had sat at Nicaea and carried it home": NC 32523–32525, "brought to our council through Cæcilean of blessed memory, the predecessor of your holiness (who was present at it)".

Every other sentence matches v1 word for word, apart from the M1 cuts. The quotes are unchanged from v1, and the review checked each one against its file.

## 3. Kit lines

- Hook: three sentences. They give Arius's words, who wrote them and when, and the council's charge. Pass.
- Essence (130 for a council): the stake at w66–84, the creed at w97, the condemnation of Arius at w122, and "Later councils set this creed first" complete at w128. Pass.
- Also told, all present: Constantine calling the bishops (w79–85); Arius's exile (w333); "for decades it divided the church" (ends w135). Pass.
- Setting: year, emperor and city come in the essence's short sentence, and "in today's Turkey" comes later with the meeting. It is not stacked. Pass.
- Ending: on Caecilian, who sat at Nicaea, carrying the copy home. Pass.

## 4. Score

`python -m engine.m1.profile_readability council-of-nicaea-325/council-of-nicaea-325.brief.txt`: 551 words, grade 8.0 (names out 7.1), reading ease names out 72.2, 15.7 words a sentence, longest sentence 31 words: pass. At 130 words a minute it runs about 4 minutes 14 seconds, at the council limit of about 550 words.
