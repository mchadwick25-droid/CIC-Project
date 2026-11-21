# Review: Thomas Cranmer

Batch 8, 2026-11-21, under `roles/reviewer.md` and `Reviewer_Prompt.filled.md`. Story: `thomas-cranmer.brief.txt`. I read it once, straight through, before reading the outline. The prompt's "For Constantine the Great only" section does not apply to this story. Word positions below are running word counts through the story.

## The test, from one hearing

1. **Who:** Thomas Cranmer, archbishop of Canterbury from 1533 under Henry VIII, who led the making of the English Book of Common Prayer.
2. **What happened:** he served Henry: he gave the sentence on the king's marriage, asked for the English Bible and argued against Lambert, who was burned. Under Edward he made the English prayer book of 1549, and the West rose against it. Under Mary he signed papers taking back his teaching, then renounced them at St Mary's and was burned at Oxford in 1556, holding the signing hand in the fire first, as Foxe tells it.
3. **Why the connection matters:** his book replaced a Latin service most people could not follow, and many regional forms, with one English service for the whole country. It was imposed and resisted, and through Elizabeth's book of 1559 it went on to shape worship in English.

No line is blank or wrong.

**My essence, written before reading the outline.** Cranmer, archbishop of Canterbury from 1533 under Henry VIII, led the making of the Book of Common Prayer (1549, 1552). It gave England one shared service in its own language, and through Elizabeth's 1559 book it shaped worship in English. Under Mary he recanted, then withdrew the recantations in public and was burned at Oxford in 1556, putting first into the fire the hand that had signed them (Foxe). **Also told:** the sentence on Henry's first marriage, the English Bible (Tyndale), Lambert, the 1549 rising, the 1552 revision. This matches the approved heart (`Hearts.md`; `Outline.md` lines 5–10).

**Where the essence is complete.** The prayer book and what it changed are told by word 130 ("shape worship in English"). The full approved essence, ending on Foxe and the hand, is complete at **word 186** ("the hand that had signed them"), about 1:15. That is past about 150: **B2**.

**Also told, against the outline.** Present with their weight: the marriage sentence, the Bible with Tyndale credited to editors, Lambert with Foxe's own judgment, the preface, one form for the realm, the rising and his answer, prison, stripped of rank, the papers and the six printed, Foxe's "cannot tell", the fear of death, the renunciation instead of the prepared text, the register, 1559. **Missing:** the 1552 book dropping the word Mass (**B3**), and Foxe making his death part of Protestant memory (**B4**).

**Order.** After the essence the life is told once, in order: Cambridge, 1533, 1537, 1538, 1549, 1553–1556, the morning, the fire. The essence reaches ahead to the papers and the hand, which the kit allows, and the scene itself is told only at the end. It ends on the person, at the fire, in his own and Stephen's words. Good.

**Names.** Cranmer, Henry VIII, Edward VI, Mary, Elizabeth, Foxe, Lambert, Tyndale (link), Stephen. Stephen is heard once and neither acts nor links (**M5**).

**Where I got lost.** For a moment in the essence: Elizabeth's 1559 book is told before Mary, so a listener who does not know the order of the reigns may hear Mary as coming after Elizabeth (**M3**). Nowhere does it read as a children's book or talk down.

## The score

`python -m engine.m1.profile_readability …/thomas-cranmer.brief.txt`:
`703 words, grade 6.6 (names out 5.9), reading ease names out 81.2, 16.0 words a sentence, 0.9 joining words per 100, 14% short sentences, longest sentence 31 words - pass (note: grade 6.6 is under 8: the listener read checks it is not flat)`

**Listener read:** not flat. The sentences carry cause and contrast ("Even Foxe, Cranmer's admirer…", "Yet the bishop's own register…"). Two paragraphs open three sentences running on a date ("In May 1533… In 1537… In 1538…"). That leans toward a chronicle but stays adult. Not a finding.

## Scores

- **Voice: 4.** Adult documentary register, led by the record. Foxe is named with who he was, and his admiration is used against the story's own hero at Lambert. The dated sentence openings in paragraphs 3 and 6 are the only flat stretch.
- **Craft: 3.** A strong opening on the book itself. A clean single line through the life, and an ending that lands on the person. But the essence runs to word 186, the whole runs past 4:30, and the 1552 book is missing.
- **Rigor: 3.** Every quote is verbatim, the two speeches and the register are credited, and the motive is left contested. But the attendance law is moved onto 1549, and one part of the approved heart is missing.
- **Accessibility: 4.** Every listed word that is used gets its plain sense, worked into the sentence. Nothing a grown listener knows is glossed. Two sentences run past 30 words.

## Verdict: REVISE

## Source check

Each sentence traced to `Outline.md`, with `Source_Sheet.md` where needed. Quotes re-checked in `cic/texts/`:
- Quote 1: FOXE8 (`foxe_acts-and-monuments-v8_cattley-townsend1837.txt`) 7403–7404, "my hand offended [oflended], writing contrary to my heart, my hand shall first be punished [pimished] there-for; for, may I come to the fire, it shall be first burned". This is a damaged scan, flagged in the outline, and the outline's rendering is used word for word. It matches.
- Quote 2: KET (`church-of-england_two-liturgies-1549-1552_ketley1844.txt`) 1630–1647, across the page break. It matches the outline's rendering word for word.
- "like a Christmas game": COX (`cranmer_miscellaneous-writings-and-letters_cox1846.txt`) 17555. Verbatim.
- "unworthy right hand" and "Lord Jesus, receive my spirit": FOXE8 7523–7526 ("his unworthy right hand"). Both stand at the outline's Ending (line 94). The story correctly avoids "this unworthy right hand".
- No quoted words outside the outline.

Where held sources differ, the story credits each. The two printed speeches and the register are at paragraph 8. On why he signed, it gives Foxe's "cannot tell" and his own "for fear of death". On the number of papers, it says "a series" and that the bishop printed six. Waltham, where Foxe and Cox differ on the year, is not told. No quoted span hides a cut. The Do not say list holds, except as below.

## Findings

### BLOCKING

**B1. Length: 703 words by the scorer, past about 675 (4:30).** The cut-first list is nearly used up: only item 11 (Dunstable) is still in. The cuts below, with the fixes for B2–B4 and M1–M5, come to **652 words** by the scorer's own count (`grade_profile_text`, run on the text with these changes applied in memory). The longest sentence is then 29 words, and the essence is complete at about word 152. Each cut saves its words without touching a must-keep item, a credited disagreement or a plain sense:
- Cut-first item 11 (Dunstable), with the M1 split: see B2. Saves 8.
- "Then, from 1547, came the boy king and the prayer book. Until then the service was said in Latin" → "Until the prayer book, the service had been said in Latin". Saves 8. The boy king and the book are already in the essence.
- "Cranmer printed their article with his reply, that they asked for Latin" → "Cranmer answered that they asked for Latin". Saves 5.
- ", and the bishop of London printed six of them." → ". The bishop of London printed six." Saves 3.
- "When Edward died in 1553, his Catholic sister Mary became queen." → "…his sister Mary became queen." Saves 1 ("Catholic queen Mary" is already in the essence).
- "He did not read the text prepared for him. Instead he renounced" → "Instead of reading the text prepared for him, he renounced". Saves 2.
- "the university church of St Mary" → "the university church". Saves 3. This is the outline's own plain word.
- "Here the record divides. " → delete. Saves 4. "instead" in the next sentence already marks the turn.
- "The fire was set outside the city's north wall, where" → "The fire was set where". Saves 5.
- "Lambert was condemned for teaching what the church held false, and he was burned." → "…and burned." Saves 2.

**B2. The essence is complete at word 186, past about 150.** The opening quote is 43 words. "He led the making" is told twice, in sentences 5 and 7, and the office under Henry adds a sentence before the essence can reach Mary. Fix:
- Replace "So said the preface of a new English prayer book in 1549. The man who led its making was Thomas Cranmer, archbishop of Canterbury, England's senior bishop. ¶ He held that office from 1533, under King Henry VIII. Under the boy king Edward VI, he led the making of the Book of Common Prayer, a book of prayer for the whole country, its services set out in English." with "So said the preface of the Book of Common Prayer, the new English prayer book for the whole country, in 1549. Thomas Cranmer, archbishop of Canterbury, England's senior bishop, led its making under the boy king Edward VI." This also fixes M2.
- Move the office under Henry to beat 2, where the outline sets "Made archbishop in 1533" (line 55): "Cranmer was a Cambridge scholar drawn into King Henry VIII's wish to end his marriage to his first queen. Made archbishop in 1533, that May he gave sentence, he wrote, that the marriage had never been lawful, because the pope had no power to allow it." Henry and 1533 are still told, at about word 165.
- Shorten "John Foxe, a Protestant who collected the stories of those burned under Mary, tells that he put into the fire first the hand that had signed them." to "John Foxe, a Protestant who wrote the lives of those burned under Mary as martyrs, says he put the hand that signed them into the fire first." This also carries B4.
- Shorten "But under the Catholic queen Mary, he signed a series of papers taking back his teaching, and then, at Oxford in 1556, withdrew them in public and was burned." to "Under the Catholic queen Mary, he signed a series of papers taking back his teaching, then withdrew them in public and was burned at Oxford in 1556."
- With M3's order, the essence is complete at about word 152–154.

Do not say, to add to the outline: "Do not let the opening and the essence run past about 150 words. The opening quote is 43 words, so say 'he led its making' once, and tell 'archbishop from 1533 under Henry VIII' at beat 2 if the essence needs the room."

**B3. The attendance law is moved onto 1549, and the 1552 book is missing.** Paragraph 4 tells the 1549 book with "and the law required everyone to attend". The only held Act requiring every person to attend is the Act of 1552 (KET 13353–13370; E11). The outline gives it to beat 4, 1552, and the sheet records that the 1549 Act is not held. As placed, the story implies that the 1549 rising was against a law of attendance. The approved heart also tells that "the 1552 book went further and dropped the word Mass" (`Outline.md` line 8), and the story never tells it. It names "his book of 1552" in the essence without ever telling there was a second book. Fix:
- "Now the whole realm would have one, in English, and the law required everyone to attend." → "Now the whole realm would have one, in English."
- After "The rising was put down." add: "His revised book of 1552 dropped the word Mass, the old Latin service of holy communion, and a new law required everyone to attend." This is the outline's gloss for the Mass (line 36).

Do not say, to add: "Not 'the law required everyone to attend' told of the 1549 book. The held Act is 1552's (KET 13353–13370); tell it with the 1552 book, which dropped the word Mass."

**B4. Part of the approved heart is left out: Foxe made his death part of English Protestant memory.** This is in "Also told" (line 10; I2). Cut-first item 1 cuts Perkins but says "keep that Foxe told the death as a martyr's". The story says only that Foxe "collected the stories of those burned under Mary". Fix: the Foxe sentence in B2 ("who wrote the lives of those burned under Mary as martyrs"). It credits the martyr frame to Foxe and adds no narrator verdict, which the Do not say list on "a martyr" requires.

Do not say, to add: "Do not drop that Foxe told his death as a martyr's (What came 2; approved heart). It goes in the clause that names Foxe, not to the card." The outline's "or for the card" at line 64 left room for this error.

### MINOR

**M1. Sentence past 30 words (32):** "In May 1533 he sat as judge at Dunstable, and he wrote that he gave sentence that the marriage had never been lawful, because the pope had no power to allow it." The B2 wording fixes it and drops Dunstable (cut-first item 11).

**M2. Held-back name reveal:** "The man who led its making was Thomas Cranmer…" is the "The man was …" hinge. The B2 wording fixes it: "Thomas Cranmer, archbishop of Canterbury, England's senior bishop, led its making under the boy king Edward VI."

**M3. Elizabeth before Mary in the essence.** Move the Elizabeth sentence after the Foxe sentence, and make it "After her, his book of 1552 became Queen Elizabeth's of 1559, which went on to shape worship in English." The essence then follows the reigns in order and ends on what came of the book.

**M4. Sentence past 30 words (31):** "When the fire was lit, Foxe says, he stretched out his arm and held his right hand in the flame, still, so that all could see it burn before his body." Split: "…held his right hand in the flame. He held it still, so that all could see it burn before his body."

**M5. A name heard once that neither acts nor links:** "in the words of Stephen, the first martyr," → "in the words of the first martyr,". The outline allows this (line 89), and it saves 2 words.

**M6. A source finding:** "he asked the king's chief minister for leave to publish an English Bible". The leave was the king's. Cranmer asked Cromwell "to obtain of his grace … a licence that the same may be sold and read of every person" (COX 32950–32954; E5). Smallest fix: "he asked the king's chief minister to win the king's leave to publish an English Bible" (+3 words; the total stays about 655).
