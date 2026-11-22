# Recheck of the story: Basil of Caesarea (`basil-of-caesarea`)

Checked: `basil-of-caesarea.brief.txt` against `basil-of-caesarea.brief.v1.txt`, `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`.

## Verdict: FIX

One replacement. The rest passes.

## 1. The review's findings

- **B1 (over the cap):** fixed. 673 words by the scorer, under 675. The ledger was applied as given. The story now ends on "Gregory says the whole city poured around Basil as he died." That is the outline's Ending 2 in part (D5). It still ends on the person.
- **B2 (rival bishop, Sasima's cause):** fixed. "A rival bishop once blocked his road with armed men" is held by B4 (Or. 43.58, `npnf207...xml` 42569-42603, "bar the passage with a robber band"). "Basil answered by making..." is held by B5 (42609-42621). The rival is unnamed, by role, as the Names line asks.
- **B3 (opponents' view; the letter):** fixed. "The Spirit, they held, could not be ranked with the Father and the Son" is held by Sp4 (`npnf208...xml` 10556-10558). The source is Basil's report of them, and the paragraph is his scene, so "they held" says no more than he does. Letter 159 is no longer made his reply to the attack.
- **B4 (Gregory's qualifier):** fixed in substance. "In writing" and "he often preached it" are held by Sp7 (Or. 43.68-69, `npnf207...xml` 42946, 42964: "postponed for the time the use of the exact term"; "his often having publicly preached this truth"). The sentence credits Gregory. But see the FIX below: the words are in the wrong place for a listener.
- **M1:** fixed. The 381 sentence opens the impact, with no cause from Basil.
- **M2:** fixed. "His friend Gregory of Nazianzus" in the turn, held by E6 (Rufinus, "collegae"). "Gregory says" in the Pontus paragraph now follows Nazianzus by name, so the listener hears the right Gregory.
- **M3:** listed in `Revision.md` as not fixed, for length. My judgment of each item is below. The Eunomius clause is the one the review flagged as a slate job.
- **M4:** fixed. The 31-word sentence is split.

### The Eunomius clause (M3): not needed

The story does not need it. Leaving it out is right, and nothing should be cut to pay for it.

- **The slate job does not name it.** Mark's job line for Basil is the turn from rhetoric, the rules, the house, the Spirit's place as bishop from 370, and his death before 381. Eunomius is in none of these. So it is neither the essence nor the approved Also told, and the outline's Also told does not list it.
- **The siblings tell it in full.** `eunomius-of-cyzicus` gives Basil's answer as a scene, with Basil's own words ("I would not say that 'unbegotten' is his being"). It names Basil and Gregory of Nyssa as the two who answered him, and Sozomen's judgment of them. `gregory-of-nyssa` tells that Gregory took over the fight after Basil died. One clause here would repeat what those two stories own, in less detail. The listener reaches it through the link `Eunomius of Cyzicus: Basil wrote against him`.
- **The header's "a clause here" permits; it does not require.** It sets the most this story may say about a sibling's subject, so the two stories do not tell the same event twice. The outline puts the clause under What came of them 2, which is ranked and cut to fit.
- **It would cost a heart scene.** 8 words take the story to 681, past the cap, which is BLOCKING. All six cut-first items are already out. So it could only be paid from a part of the heart or a credited witness, and those outrank a sibling clause.

It stays for the card, with I6 (Theodore of Antioch and Sophronius writing against Eunomius "in defence of St. Basil").

The other M3 items (E1, B1's death in his arms, the "never met a bishop" exchange, Sozomen's B3, P2, P4, Sp2-Sp3, Gregory's reason in Sp7, I7, D6) are none of them heart, force, a credited disagreement or the ending. The card should carry them.

## 2. Changed sentences

Every sentence that differs from v1 is held at the lines cited above, or is a shortening of a v1 sentence that was already held. The changes are: the hook without "Then:"; the split rules and lodging sentences; "Gregory of Nazianzus" in the turn; "Gregory says" in Pontus; "Gregory's speech in Basil's memory is praise."; the rival bishop and "Basil answered by making"; "The rich filled it at Basil's urging, Gregory says." (H3, "the common treasury of the wealthy ... in consequence of his exhortations"); the Sp4 sentence and the new lead-in to Quote 3; the Sp7 qualifier; the 381 sentence moved. None says more than its source, and each credits the right witness. The three quotes are unchanged and still match the outline's renderings: Letter 223.2 (`npnf208...xml` 39131-39135), Longer Rule 7 (PG 31, 72547-72549), Letter 159.2 (`npnf208...xml` 33483-33485).

## 3. Shape

- **Hook:** three sentences in his own words, now without the doubled "Then". It leads straight into the essence.
- **Essence:** complete at word 143 ("before a council confessed it"), under 150.
- **Also told:** the rules (Pontus paragraph), the house and the lepers, the Spirit with the opponents' view, his argument and the held-back phrase, and the cost (the official, the quarrel with his bishop, the rival bishop). All present, with their weight.
- **Words to explain:** rhetoric, the ascetic life, the Rules, the words of praise, the emperor's official, the party that ranked the Son below the Father and the double monastery each get their plain sense when first heard. "Doxology" and "Arian" are not used.
- **Sentence length:** longest 30 words, by the scorer.
- **Length:** 673 words, about 4:29, within the outline's 675.
- **Ending:** on the person, with the city around him as he died.
- **Order:** the life is told once, in order. The impact now runs 381, 397, the sixth century, 787.

## 4. Score

`python -m engine.m1.profile_readability .../basil-of-caesarea.brief.txt`: 673 words, grade 7.4 (names out 6.4), reading ease names out 77.3, 15.7 words a sentence, longest sentence 30 words, pass. The grade is under 8. On a listener read it is not flat.

## FIX

In the B4 sentence, "in writing" lands after "God". On one hearing it reads as "the Spirit is God in writing", which joins the qualifier to the wrong words. Move it ahead. Same words, same count (673).

Replace:

> Gregory admits that Basil held back the bare words that the Spirit is God in writing, from caution, though he often preached it.

with:

> Gregory admits that in writing Basil held back the bare words that the Spirit is God, from caution, though he often preached it.

## Applied (coordinator, 2026-11-22)
The replacements above applied word for word to the brief.
