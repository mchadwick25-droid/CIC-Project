# Rendering Review: gallic quote records, round 2 (6 records)

- **Reviewer:** Opus 5.5 (independent; did not draft, render or review any of these records in round 1)
- **Date:** 2026-11-03
- **Subject:** the six gallic renderings round 1 failed

## Method

This is a targeted recheck. For each record, the reviewer reads the edition span in `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (spans as given in the round-1 tables, `<note>` blocks stripped), checks the record's `text` against it, and compares the old and new `modern_rendering` in the working-tree diff. The check covers the round-1 finding first, then the changed sentences against the full bar: every clause rendered, nothing added, one thought per sentence, no sentence past about 25 words (counted by script and by hand), no misleading modern sense, hedges and reported-speech frames kept, and plain readable English. Each rendering is also read against the record's `use_note.not_for`. None of the six records carries a `divergence_note`. For postumianus-you-have-conquered-all-the-eremites, nothing changed, so the reviewer judges the round-1 finding itself from the edition.

## Results

| Record id (gallic.quote.…) | Round 1 finding | Round 2 check | Verdict |
|---|---|---|---|
| benjamin-relied-on-his-own-judgment | P2: "For" explained the wrong clause | The man is now named in the first sentence. "You remember how his life ended" comes next, so "For he left the desert" now explains the end, as in the edition (lines 28106-28110). Every clause is rendered. The longest sentence has 23 words. Repeating "You remember" carries the edition's single "remember" across the split and adds no content. | PASS |
| brictio-called-by-demons-on-the-rock | P1: "I believe" hedge lost; "From there" added | "Knowing how great a frenzy..." now sits inside "I believe they saw...", which matches the edition's "being conscious" (lines 5289-5299). "From there" is gone. The sentence has 24 words. Nothing else changed. | PASS |
| gallus-on-the-tribunes-for-the-spains | P2: 29-word sentence; "the Spains" | The old sentence is now two: "He had many other requests to present ..." and "But his chief request was ... the Spanish provinces" (22 words). The "but" is the edition's own word (line 5117), which sits inside the record's elision. "Besides" is carried by "many other ... chief". "Spanish provinces" now matches the earlier usage. The longest sentence in the whole rendering has 25 words, within the limit. | PASS |
| martin-on-the-christ-with-wounds | P2: 29-word sentence; "come back" added | The rendering now says "foretell that he would come", with no "back" (lines 1809-1813). The condition is split in two, and "He must also openly show..." keeps the wounds inside Martin's "unless". "Look and form" renders "appearance and form". No sentence runs past 20 words. | PASS |
| the-psalm-that-answered-defensor | P1: "It was believed" frame lost on the closing clause; "Martin" added | "Martin" is removed as the object of the opposition. The closing clause is still asserted as fact, though. "They believed this because, in Martin's case, the Lord's praise was perfected..." presents the perfected praise as true, because a "because" clause states its content, and only the "enemy" half gets "as they believed". The new wording also makes the clause the people's reason for believing. In the edition (lines 1104-1108), the "because" explains why the Psalm was a testimony to Defensor. A smaller issue: "opposed most strongly" has no object and reads awkwardly. The verse sentence runs to 27 words. This was unchanged and passed in round 1, but it can be split. | FAIL P1 |
| postumianus-you-have-conquered-all-the-eremites | P1: `text` said to merge two "you have conquered" phrases and drop "O Gaul, said Postumianus" | The edition (lines 4103-4107) reads: "You have conquered, O Gaul," said Postumianus, "you have conquered, although certainly not me, ... but you have conquered all the eremites and anchorites." The record's `text` begins at the second "you have conquered". It matches the edition word for word up to "anchorites.", apart from the capital Y. Nothing is merged and nothing inside the span is dropped. The first "You have conquered, O Gaul" is a separate, repeated phrase outside the span. The speaker is carried by `speaker_or_author`, and the addressee by `use_note.means` ("concedes to Gallus"). The round-1 finding does not stand. The rendering covers every clause: the concession, "not me", "on the contrary ... upholder", "always known and believed", and "but ... all the eremites and anchorites". It adds nothing, and no sentence runs past 13 words. "Hermits" is the right modern word for "eremites". | PASS |

**Out of scope for this check, flagged and not touched.** The `speaker_or_author` of gallic.quote.benjamin-relied-on-his-own-judgment reads "John Cassian, narrating the fall of Brother Benjamin (Second Conference)". The span (line 28106) falls in "Conference II. Second Conference of Abbot Moses" (line 27133), so the words are Abbot Moses's address. The record's own `use_note.not_for` says so. The rendering itself is unaffected, but the metadata field contradicts the use_note and needs a separate fix.

## Failed renderings: corrected text

### the-psalm-that-answered-defensor

Among the bishops who were there, however, one named Defensor is said to have objected most strongly. For this reason, people noticed that he was sharply rebuked at that time in the reading from the prophets. It so happened that the reader whose duty it was to read aloud that day was blocked by the crowd and did not appear. The officials were thrown into confusion as they waited for a man who never came. Then one of the bystanders grabbed the book of Psalms and seized on the first verse he came to. The Psalm went like this. 'From the mouths of babies and infants you have perfected praise because of your enemies, to destroy the enemy and the avenger.' When these words were read, the people raised a shout, and the opposing side was put to shame. People believed that God had ordained the choice of this Psalm, so that Defensor might hear a witness about his own work. In their view, this was so because in Martin's case the Lord's praise was perfected out of the mouths of babies and infants. And at the same time, they held, the enemy was both pointed out and destroyed.

Notes on the correction:

- "In their view, this was so because..." keeps the whole closing clause inside the edition's "It was believed". "This was so" points back to the Psalm being chosen as a testimony to Defensor, which is what the edition's "because" explains.
- "They held" carries the same frame into the "while" clause after the split. It adds no new claim.
- "Objected" replaces "opposed" because the edition names no object ("offered opposition"), and "opposed" needs one.
- The verse now stands as its own sentence (22 words), with "The Psalm went like this." before it.
- Every sentence is 24 words or fewer.
