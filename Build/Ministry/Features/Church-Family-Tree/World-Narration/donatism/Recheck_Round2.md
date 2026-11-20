# donatism: Recheck Round 2

Targeted recheck of the six revised pieces against Review_Round1.md, Revision_Round1.md and Mark's ruling (2026-11-20, Decision-Log "The narrator calls the Donatists' opponents 'Caecilian's church'"). Each `<key>.v1.txt` was word-diffed against `<key>.txt`.

No PRE-EXISTING corrections were made in round 1, so check 2 (record and source line) has nothing to confirm.

| Piece | Verdict | Grade | Ease |
|---|---|---|---|
| story | PASS | 8.4 | 70.8 |
| legacy | PASS | 8.5 | 74.7 |
| docstory-don.story.passio-marculi | PASS | 7.9 | 77.9 |
| docstory-don.story.conference-of-carthage-411 | PASS (after recheck edit) | 7.6 | 75.6 |
| docstory-don.story.tyconius-condemnation | PASS | 7.4 | 78.8 |
| docstory-don.story.acta-purgationis-felicis | PASS | 8.6 | 72.2 |

All six pass `python -m engine.m1.profile_readability` (0 failing). Passio, conference and tyconius score under grade 8; listener read: none is flat.

## Per piece

- **story.** All eight changes match the revision log; no other sentence changed. "Caecilian's church" is first heard after Caecilian is introduced, and its first mention carries the clause "the one later known as the Catholic church". This says what the ruling asks: that it came to be called the Catholic church. The judge's award of the name stays credited to the rescript. "Persecution" is now credited to the Donatists. Own-wording split ("...was washed again. The Donatists did not count it as a second baptism.") adds nothing. Dropping "though" leaves the contrast clear, because the next sentence explains it.
- **legacy.** Both changes as logged. The own-wording clause "Caecilian's church, the one later known as the Catholic church" meets the ruling and adds no claim. Caecilian is not introduced in this piece, but the clause tells the listener which church is meant.
- **passio-marculi.** Both BLOCKING findings answered as worded. "Macarius's persecution" and the seizure, flogging and parade now sit inside "In the Passio's telling" and "It says". The tenses are now past.
- **conference-of-carthage-411.** MINOR 1 and 3 answered as worded. MINOR 2: the reviser kept "the opposing bishops". That names the other church from the Donatist bench, since the scene is told from their side, and it does not meet the ruling. Edit applied (below). The first-mention clause is not added, because the same sentence and the next one already say the name Catholic was claimed by them and given to them by the emperor's order. That carries the ruling's content without repeating it.
- **tyconius-condemnation.** The own-wording "He never went over to Caecilian's church, the one later known as the Catholic church." meets the ruling and adds no claim. The fact that Tyconius stayed is already in the original.
- **acta-purgationis-felicis.** Both joins as logged. "then" was dropped from "was then void". The meaning is unchanged, and the review's wording implied this.

## Edit made

`docstory-don.story.conference-of-carthage-411.txt`, paragraph 3:
- Old: "When the opposing bishops claimed the name Catholic"
- New: "When the bishops of Caecilian's church claimed the name Catholic"

## Quotes and voice

The quoted spans are unchanged character for character. There is no first person in any revised narrator text.

## Vantage sweep, all 11 pieces

There are no remaining instances of "the rival church", "its/their rival", "the other church", "the other side" or "opposing" naming the other church.

The remaining uses of "rival" and "opponent" are checked and allowed:
- "two rival churches" (story 1) applies to both churches.
- "rival primate" (bagai) names the Maximianist.
- "Optatus, an opponent" (story, acta, gesta) describes a person, not a church.

Note for Mark, not a blocking item: story paragraph 2 says "A rival party made Majorinus bishop in his place." That sentence names the Donatist party, not the other church, from Caecilian's side. It is outside this round's findings and was left unchanged.
