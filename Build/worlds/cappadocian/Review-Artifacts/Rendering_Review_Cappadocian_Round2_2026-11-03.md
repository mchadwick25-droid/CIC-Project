# Rendering Review: cappadocian quote records, round 2 (12 records)

- **Reviewer:** Opus 5.5 (independent; did not draft, render or review these records before)
- **Date:** 2026-11-03

## Method (short)

This is a targeted recheck of the twelve records that failed in `Rendering_Review_Cappadocian_Batch1_2026-11-03.md`. For each record, the round-1 finding is read first. Then the record's `text` is read against the edition in `cic/texts/`, and the new `modern_rendering` is read clause by clause against it. `git diff -- records/cappadocian` shows that only the renderings changed in these twelve records. A script splits sentences at end punctuation and counts space-separated words, with quoted matter counted toward its sentence. The bar is: every clause rendered, nothing added, editors' brackets kept marked, elisions kept, one thought per sentence, about 25 words at most, no misleading modern word, and hedges, tense and reported-speech frames kept. Only what changed is rechecked.

Files read: `cic/texts/npnf208_basil-letters-select-works.xml`, `cic/texts/basil_ascetic-works-longer-shorter-rules_clarke1925.txt`, `cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt`, `cic/texts/julian_letters-1-73_wright1923.txt`, `cic/texts/gregory-nyssa_life-of-macrina_clarke1916.txt`, at the spans named in round 1.

## Results

**12 records: 12 PASS, 0 FAIL.**

| Record id (cappadocian.quote.…) | Round 1 finding | Round 2 check | Verdict |
|---|---|---|---|
| basil-against-delaying-baptism | P2: "viaticum" left as unglossed Latin with a misleading modern sense | Now "Do not be left without your provision for the journey", which gives the word's sense here (the traveller's provision) without the deathbed-communion reading. "The bridle of baptism" now follows the edition's order. Longest 16. | PASS |
| basil-canon-on-digamy | P2: bare "polygamy" reads as several spouses at once | Now "It is called polygamy, meaning many marriages, or rather, limited fornication." The gloss adds no claim. It gives the word's own sense in the canon (Greek *polygamia*, many marriages), which the canon itself applies to a third marriage. So it removes the misleading modern sense and adds nothing the edition lacks. "But this is no longer called marriage" follows the edition's "but". Longest 18. | PASS |
| basil-on-antiphonal-psalmody | P2: one 34-word sentence joins the night of psalmody and the dawn psalm | The night of psalmody and the dawn psalm are now separate sentences. "Heedful temper" is now "attentive mind", "prelude of the strain" is now "opening of the chant", and "confirming" is now "strengthen". All keep the edition's sense. Longest 25. | PASS |
| basil-on-his-retreat | P1: "go on about the flowers" drops "multitude" and changes the verb; "scents" adds smell | Now "admire the many flowers and the singing birds" and "the vapors rising from the earth". Both match the edition's "admire the multitude of flowers" and "exhalations". "Happily disposed" is now "well suited", and "a chance hunter" is now "a hunter who happens by". Longest 19. | PASS |
| basil-on-work-and-prayer | P2: one 69-word sentence; "some" becomes "some of you"; "mark of pleasing God" thinned | The passage is now split into ten sentences, longest 23. "Some get out of work" names no addressee. The close is "directed toward the goal of pleasing God", which restores the aim. "The arts we practise" is now "the crafts we practice", which avoids the modern sense of "arts". | PASS |
| basil-to-the-chorepiscopi | P2: one 30-word sentence; "wish in ignorance to buy" becomes "try" | Now "to wish, in ignorance, to buy", so the wish is kept. The sale, the loss of the gift and "sold to Satan" are now separate sentences. "Obtruding the traffic of the huckster" is now "forcing the huckster's trade". Longest 24. | PASS |
| gregory-nyssa-on-becoming-god | P2: sentences of 28, 28 and 37 words | Split into fourteen sentences, longest 25 (the opening). The purpose clause ("so that our nature ... might itself become divine") and the rescue from death are now separate sentences, and the rescue is still stated as the edition states it. The question "why are they scandalized ... when it teaches that God was born among men" is kept as a question in two sentences. | PASS |
| julian-galilaeans | P2: 28-word opening sentence | The condition and the order are now one 22-word sentence, and "expound Matthew and Luke" is a sentence of its own. "Galilaeans" is kept. "Them" in the last sentence still points to Matthew and Luke, as in the edition. Longest 22. | PASS |
| macrina-refuses-remarriage | P1: "to be compelled to consider another" stands outside "she would say"; "fame of her beauty" thinned | Every claim of Macrina's now sits inside a reported-speech frame ("she would say", "she kept insisting", "she held", "she said"), so none reads as Gregory's own judgment. "Drawn by the fame of her beauty" restores "fame". The habitual "would say" follows the edition. Longest 22. | PASS |
| reading-scripture-hexaemeron | P2: 33-word opening sentence with the verse inside; "flying creatures that fly" | The verse now stands as its own sentence, and "birds that may fly" replaces the repetition. "He has foreseen" and "he has divided" keep the edition's perfect tense. Longest 18. | PASS |
| we-look-to-the-east | P2: 33-word opening sentence | Facing east is now its own short sentence. The forgotten reason (Paradise in Eden, in the East) follows in one 22-word sentence. "We do not all know the reason" follows the edition. | PASS |
| what-is-the-written-source | P2: sentences of 28 and 35 words | The condition is now split into two "Suppose ... granted" sentences, then "Then let our opponents grant us, too ...", which keeps the if-then shape. The demand for written evidence and "the other matters we have listed" are now separate sentences. Longest 23. | PASS |

## Observations (not failures)

- **Spelling.** The re-rendered texts use US spelling ("vapors", "travelers", "honored", "practice" as a verb). Several unchanged notes in the same records use UK spelling ("travellers" in basil-on-his-retreat's `use_note.means`, "practised" in basil-on-work-and-prayer's lens note). The writing standard sets no spelling rule, and both forms already appear across the fleet's records. So this is not a failure under the bar. Whether to adopt one convention is a fleet-level choice for Mark, not something a rendering review should settle.
