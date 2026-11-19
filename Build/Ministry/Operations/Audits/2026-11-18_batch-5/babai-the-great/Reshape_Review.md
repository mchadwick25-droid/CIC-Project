# Reshape review: Babai the Great

Batch 5, 2026-11-19. Targeted review of the reshaped `babai-the-great.brief.txt` against `babai-the-great.brief.v2.txt`, `Reshape.md`, `Outline.md`, the approved heart in `Hearts_Plain.md`, and Decision-Log "Batch 5 hearts…" (2026-11-18), item 10 (target about 3:00 to 3:15).

## The listener's three lines (one hearing, before the other files)

- **Who this was:** Babai, a monk and the abbot of the Great Monastery on Mount Izla near Nisibis, who was not a bishop, yet did the bishops' work for the Church of the East through the close to twenty years the Persian king would let it have no head.
- **What happened:** He drove those the bishops judged heretics out of the monasteries and ruled Izla harshly: monks with wives stripped of the robe and driven out with their families, their huts burned, a gentle monk, Jacob, expelled unjustly, until many left and founded monasteries across the East. He wrote the Book of the Union. In 612 the king refused the bishops a head because they honored Nestorius. In 628 the bishops begged Babai to lead the church; he refused, and, as Thomas tells it, an angel took leave of him. He died about then.
- **Why the connection matters:** His Book of the Union set out the teaching his church kept: two natures, each real and complete, in one Christ, so that Christ died as a man and God did not die. That teaching set the Church of the East apart from its neighbors, his church kept and honored his books, and historians judge that they helped settle its teaching on Christ.

All three lines come clear from one hearing.

## Verdict: PASS

No BLOCKING findings. One MINOR flow fix, optional.

## 1. Nothing essential lost

- **The visit to the monasteries from about 609, with Henana's followers refused communion at Izla until they cursed him.** The approved heart's part ("toured the monasteries for the senior bishops, driving out teachers of condemned beliefs") stands in the essence: the bishops "turned to a man who was not even a bishop", and "he drove out of its monasteries those the bishops judged heretics". Henana's followers are an "Also told" item and a side link, and the outline makes Henana "a clause" at most. The force of the expulsions stays whole in the Izla paragraph, and the conflict over heresy is still told. None of the outline's four connection points rested on this paragraph. Rightly dropped.
- **George crucified in 615, and Babai's account of his life.** A secondary episode ("Two sentences" in the outline); not part of the heart, the connection, or the force of Babai's own acts. Rightly dropped.

## 2. New wording

None. A word-level diff against v2 shows two clean deletions (the 609/Henana paragraph and the 615/George paragraph) and no other change.

## 3. The kit

- Hook: three sentences (the oath, the twenty years, the turn to a man not a bishop). Pass.
- Essence complete at about word 157, "...and historians judge that they helped settle its teaching on Christ." Within the first minute. Pass.
- The life once, in order: essence; Izla in Thomas's order, undated, as the outline sets it; 612; 628. No event told twice now that the visit paragraph, which partly retold the essence, is gone. Pass.
- Church words: bishop, monk, abbot, Church of the East, heretics, the two natures, Nestorius and the Book of the Union each get their plain sense the first time they are heard. Communion, solemn curse and the state religion went out with the dropped paragraphs. Pass.
- Sentence length: the longest is the opening at 32 words ("Thomas of Marga tells how the Persian king Khosrau swore by the Sun, his god, that while he lived, the Christians of his land would have no new head of their church."). It is unchanged from v2, it falls in natural spoken phrases, and it is within "about 30". No change needed.
- Ending on the person: "Babai, by then an old man, died about that time." Pass.
- Quotes: Q1 and Q2 unchanged from v2. Pass.

## 4. Flow

It reads as one told story; the cuts leave no clipped gaps. One join is weaker than before:

- **MINOR (optional).** The Izla paragraph ends with the monks scattering, and the next line returns to the king with no bridge: "In 612, Babai says, the bishops set their faith before the king." In v2 the visit paragraph ("After the last head of the church died...") carried the vacancy forward; without it, the listener is not told why the bishops are before the king. Outline beat 4 (E6, Babai's own account) holds the king's condition. Replace it with:

  > "In 612, Babai says, the king told the bishops to show him first which faith was true, and then they would have a head."

  The next sentence, "In Christ, they wrote, are two natures...", then follows on, and "But while they honored Nestorius..." answers the king's condition. This adds about 10 words (to roughly 3:16) and says no more than the outline. If it is not taken, the story still holds.

## 5. Length

480 words (`wc -w`; 478 by the scorer), about 3 minutes 12 seconds at 150 a minute, against the target of 3:00 to 3:15. Nothing else is still not needed. Thomas's count of eighty-four works echoes the essence's "kept and honored his books", but the outline puts the count in beat 4 and keeps the historians' judgment in the essence, so it stays.

## 6. Readability

`python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-18_batch-5/babai-the-great/babai-the-great.brief.txt`: 478 words, grade 7.2 (names out 6.6), reading ease names out 80.6, 18.4 words a sentence, 0.2 joining words per 100, 0% short sentences, longest sentence 32 words. **Pass**, with the note that grade 7.2 is under 8. On the listener read it is not flat: the sentences carry chains of cause and time, and the world's images stand (the Sun oath, the burned huts, the white horse and fiery sword).
