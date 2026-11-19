# Revision: Hippolytus of Rome

Batch 6, 2026-11-19, the one revision, per `Reviser_Prompt.md`. Read: `Kit.md` Parts 1 and 2, `Outline.md`, `Review.md`, the brief, and the Decision-Log entries of 2026-11-19 ("Batch 6: era 1 first …" and "Change order: the stories approved before the kit …"). The brief before revision is kept as `hippolytus-of-rome.brief.v1.txt`.

## The outline

`Review.md` gives no Do not say line ("No BLOCKING finding, so no Do not say line is added"). `Outline.md` is unchanged.

## Findings and what I did

- **MINOR 1 (elder, plain sense late).** Done word for word. The opening now reads "Hippolytus, one of the elders who led the church at Rome with its bishop, set down …"; paragraph 2 now reads "In the early two hundreds Hippolytus was a Greek-writing teacher at Rome."
- **MINOR 2 (heresies, plain sense late).** Done word for word: "He wrote a book against the teachings he held false, the Refutation of All Heresies. In it he charged Callistus with …". The review's optional change to paragraph 5 ("traced each of those teachings back to Greek philosophy") was not made. Heard once, "those teachings" comes three paragraphs after its referent and just after "teaching adultery and murder", so a listener could take it for those. The old sentence, "traced each teaching Hippolytus held false back to Greek philosophy", is kept word for word.
- **MINOR 3 (31-word sentence; Zephyrinus).** Done word for word: "Nearly all we know of Callistus comes from this enemy. He says that Callistus, as adviser to the bishop of the day, let the teaching spread …". Zephyrinus is no longer named. Longest sentence is now 28 words.
- **MINOR 4 ("former slave").** Done: "a former slave who" is now "a slave who" (outline beat 3, "a slave who ran a bank").
- **MINOR 5 (cut, 7 words).** Done word for word: "Historians judge that Damasus confused two different splits." The hearsay stays in Damasus's own last line.
- **MINOR 6 (who wrote Latin).** Done word for word: "His Greek books soon dropped out of sight at Rome, where the clergy now wrote Latin."

Every other sentence is kept word for word.

## New sentences

Every changed sentence uses the review's exact wording. None is new wording of my own. Their outline lines:
- "Hippolytus, one of the elders who led the church at Rome with its bishop, set down …": Words to explain, elder; Opening 1.
- "In the early two hundreds Hippolytus was a Greek-writing teacher at Rome.": The essence (S1, S2).
- "He wrote a book against the teachings he held false, the Refutation of All Heresies.": Words to explain, heresies; The essence.
- "Nearly all we know of Callistus comes from this enemy.": Connection ("nearly all we know of Callistus"), What came 1 (I1).
- "He says that Callistus, as adviser to the bishop of the day, let the teaching spread …": beat 3 (E4); Names, Zephyrinus by role.
- "His Greek books soon dropped out of sight at Rome, where the clergy now wrote Latin.": What came 1 (S2), word for word.

## Checks

- **Scorer.** `python -m engine.m1.profile_readability …/hippolytus-of-rome.brief.txt`: 619 words, grade 7.7 (names out 6.1), reading ease names out 78.7, 15.5 words a sentence, 15% short sentences, longest sentence 28 words. Pass, with the note that grade 7.7 is under 8.
- **Listener read (the under-8 note).** Heard once, it is not flat: the enemy's charges keep their force ("adultery and murder", "worshippers of two gods"), the Sardinia echo and Damasus's verse carry the turns, and the drop in grade comes from the split sentences and shorter glosses, not from simpler thought.
- **The four faults.** One witness as fact: every charge against Callistus stays credited ("this enemy", "He says", "He paints him", "Hippolytus says"). Editor's view given to a source: none; "the clergy now wrote Latin" is Duchesne's, as the outline gives it, and no longer said of Rome at large. A detail on the wrong event: "a slave" now matches the bank story's time. Force softened: nothing cut but the repeated hearsay clause; the doubt is still in Damasus's own line.
- **Spelling.** American outside quotes ("harbor", "labor").

## Essence, length

- The essence is complete at word 150, "disputed" (end of paragraph 2), at the limit of the first minute. The two glosses moved it from word 144.
- 619 words by the scorer (622 by `wc -w`), about 4:08 at 150 words a minute. The review set the length the story needs at about 4 minutes (about 610 to 620 words).
