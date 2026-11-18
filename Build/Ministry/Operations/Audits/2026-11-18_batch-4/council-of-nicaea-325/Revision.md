# Revision: the Council of Nicaea (325)

The one revision under the kit (Process.md, step 5), 2026-11-18. The brief passed review. This revision applies its MINOR findings and the Standard's new opening, setting and ending lines, and changes as little else as it can. Mark's 2026-11-17 order and spine note stands: the question of the Son opens the story and stays the spine, and Easter comes only as the second trouble and in "it also settled".

The earlier brief is kept as `council-of-nicaea-325.brief.v1.txt`.

## The outline

- Added **Essence** and **Also told**, word for word from `Essences.md`, after "The heart of their life".
- Do not say: `Review.md` gives none ("No BLOCKING findings, so no Do not say lines are needed"). Nothing added.

## Review findings

- **M1 (MINOR), the essence's last part at the edge.** Done. I cut "after his bishop had driven him out" from sentence 2, as the review suggests, and moved "in today's Turkey" to the meeting in paragraph 3 (also the setting fix below). I also moved the exile clause, an "also told" part, out of the first-minute summary into the enforcement paragraph, where outline beat 6 holds it (M11). The council's charge is kept, so the two voices stay apart.
- **M2 (MINOR), two hard phrases.**
  - "lent them the public post" is now "let them travel by the imperial post, with horses" (the review's wording; S4, outline beat 4 "the public post and horses").
  - "those who had given way under the emperor Licinius" is now "those who had fallen away under the emperor Licinius" (canon 11, "fell", NC 4124–4128). I left out the review's "from the faith" to hold the length; "fallen away" says it plainly.
- **M3 (MINOR), the 32-word canons sentence.** Split as the review suggests: "And twenty rules, called canons, set the order of the church. They ran from how a bishop is made to mercy for those who had fallen away ..."
- **M4 (MINOR), Carthage wording.** "the bishops of Carthage" is now "the bishops of Africa, meeting at Carthage". "their bishop Caecilian" is now "Caecilian, once their bishop", and the brief now says he sat at Nicaea.

## The Standard's new lines

- **Opening.** The hook is three sentences: Arius's own words, who wrote them and when, and the council's harsher charge. It leads straight into the stake, which opens the essence.
- **Setting.** The old "In 325 the emperor Constantine called bishops to Nicaea, in today's Turkey" stacked year, emperor, city and modern place. The year, emperor and city stay in the essence; "in today's Turkey" now comes with the meeting in paragraph 3.
- **Ending.** It used to end on the African bishops writing east for copies. It now ends on Caecilian, a man who sat at Nicaea, carrying the council's copy home. The order of events stays as the record gives it: they found the rule missing from their copy and wrote east. Then the ending says what that copy held, and who brought it from Nicaea.

## New sentences

Sentences whose wording is neither the outline's nor the old brief's:

- "When his letter to Alexandria failed, Constantine called the bishops to Nicaea, in today's Turkey, and let them travel by the imperial post, with horses." Outline beat 4 (K3, S4); Setting (S1). The post wording is the review's.
- "They ran from how a bishop is made to mercy for those who had fallen away under the emperor Licinius without being forced." Outline beat 7 (M14), split from the old sentence as M3 suggests.
- "He sent Arius into exile, a historian a century later says." Outline beat 6 and Who tells it (M11), moved from the first minute.
- "About ninety years after Nicaea, the bishops of Africa, meeting at Carthage, found a disputed rule missing from their copy, and wrote east for exact copies." What came of it, item 3, and the Carthage connection (I4, NC 32523–32545).
- "Their own copy held the creed and the twenty rules, and they read it aloud as law." Carthage connection: "read that copy aloud as law" (I4).
- "Caecilian, once their bishop, had sat at Nicaea and carried it home." Carthage connection: "Caecilian, who sat at Nicaea, carried home a written copy" (I4); "once their bishop" from M4.

Every other sentence is the old brief's, word for word, apart from the cuts named under M1.

## The essence and the shape

- The essence is complete at word 128: "Later councils set this creed first". "Yet for decades it divided the church", an "also told" part, ends at word 135. Constantine calling the bishops comes at word 81. Arius's exile now comes in the enforcement paragraph.
- **Opens** on Arius's complaint, in his own words, before the council.
- **Ends** on Caecilian, who sat at Nicaea, carrying home the copy of its creed and rules that Africa later read aloud as law.

## Check

`python -m engine.m1.profile_readability .../council-of-nicaea-325.brief.txt`: 551 words, grade 8.0 (names out 7.1), reading ease names out 72.2, 15.7 words a sentence, longest sentence 31 words: pass. The note that grade 8.0 sits at the floor was checked by a listener read. It is not flat: longer sentences still carry the chains of events, and the quotes keep their force.

Length is 551 words, at the council limit of about 550. No sentence was added to fill.

The four faults:
- **One witness told as fact:** the exile, the troubles in Egypt, the count and the Persian oath are all still credited.
- **An editor's view given to the source:** none added. The 381, 451 and 359 dates stand as before.
- **A detail on the wrong event:** the exile moved to beat 6, where the outline holds it. It is not tied to a day of the council. At Carthage, the copy is read and the missing rule found before the letter east, as the record gives it.
- **Force softened:** the curse, the condemnation, the exile and the death penalty in Constantine's letter are all kept.

American spelling is used outside quotes.


## Outline cleanup, 2026-11-18

none

## Adjustment (change order, 2026-11-18)

Fault: the opening repeated the Arius piece's quote ("We are persecuted because we said...") and the brief used Jerome's "the whole world groaned" line, which the Arius piece also uses; too many names for one hearing. Old brief kept as `council-of-nicaea-325.brief.v3.txt`.

Sentences changed (old, then new, then the outline line that holds the new wording):

1. Old: "We are persecuted because we said, 'The Son has a beginning, but God has no beginning.'" Arius, a priest of Alexandria, wrote this in a letter before the council.
   New: "There was a time when he was not." That, the council's own letter said, was what Arius, a priest of Alexandria, taught about the Son.
   Outline: heart, "The council's letter charged him with saying 'there was a time when he was not'" (D-4); beat 1, "The council's letter puts his teaching harder". The hook now opens on the council's letter, and the phrase returns in the creed's curse two sentences on.
2. Old: The council's own letter charged him with more: that the Son came from nothing, that "there was a time when he was not", and that he is "a creature".
   New: It charged him with more: that the Son came from nothing, and that he is "a creature".
   Outline: beat 1, "the Son came from nothing, 'there was a time when he was not', he is 'a creature'" (D-4).
3. Old: Eustathius, who like Athanasius opposed Arius, says a written statement was torn up "in the sight of all".
   New: A third, who also opposed Arius, says a written statement was torn up "in the sight of all".
   Outline: beat 5 (M7); Who tells it, "Eustathius was there; ... both were Arius's foes".
4. Old: Melitius, who had ordained clergy of his own in Egypt, kept his title but could ordain no one.
   New: In Egypt, a leader who had ordained clergy of his own kept his title but could ordain no one.
   Outline: beat 7, "Melitius, who had ordained clergy of his own, kept 'the bare title of his rank' but could ordain no one" (M12).
5. Old: They ran from how a bishop is made to mercy for those who had fallen away under the emperor Licinius without being forced.
   New: They ran from how a bishop is made to mercy for those who had fallen away without being forced.
   Outline: beat 7, "mercy, after years of penance, for those who had given way under Licinius without being forced" (M14).
6. Old: Arius was recalled, and of a council in 359 Jerome wrote, "the whole world groaned, and was astonished to find itself Arian."
   New: Arius was recalled, and the word "of one being" divided those who held it from those who would not.
   Outline: What came of it, item 2, "Arius was recalled ... It divided those who held the word from those who would not" (I3).
7. Old: Caecilian, once their bishop, had sat at Nicaea and carried it home.
   New: One of their own bishops had sat at Nicaea and carried it home.
   Outline: Carthage connection, "Caecilian, who sat at Nicaea, carried home a written copy" (I4); Links, "Caecilian of Carthage".

Names cut: Eustathius, Melitius, Licinius, Jerome, Caecilian. Kept: Arius, Constantine, Eusebius, Athanasius. Alexander was not in the brief before and is not added (length may not grow).

New quoted spans: none. "There was a time when he was not", "a creature" and "of one being" are on the card word for word. The Jerome quote is no longer in the brief; its card entry is left for the card thread.

Every other sentence is unchanged, word for word.

- **Essence** complete at word 112 ("Later councils set this creed first"); "for decades it divided the church" ends at word 119; Constantine calling the bishops at word 64.
- **Opens** on the council's charge against Arius; **ends** on the Carthage bishop who sat at Nicaea and carried the copy home.
- **Length** 556 words before, 535 after (`wc -w`).

Check: `python -m engine.m1.profile_readability .../council-of-nicaea-325.brief.txt`: 530 words, grade 7.3 (names out 6.6), reading ease names out 74.9, 15.1 words a sentence, longest sentence 31 words: pass (note: grade 7.3 is under 8: the listener read checks it is not flat).
