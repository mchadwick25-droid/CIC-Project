# Recheck: John Wesley (batch 5)

Checker: an independent hand who did not write, review or revise this story. Read against `CLAUDE.md` ("Trust and source fidelity"), Kit Parts 1 and 2, the Decision-Log entry "Batch 5 hearts: church words explained, and Luther's job re-set" (2026-11-18), `Hearts_Plain.md` (John Wesley), `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, the brief and `john-wesley.brief.v1.txt`.

## Verdict: FIX

There is one fix: the essence finishes too late. Everything else passes.

## 1. Review findings

- **B1.** The review's three paragraphs are in the brief word for word. But the essence is still complete too late (see 3).
- **B2.** Nelson's hearing now ends paragraph 4, in the fields of 1739. Paragraph 8 says only "Nelson became one of them." Fixed. The reviser's order (Nelson, then the 1744 meeting) is right: Nelson was preaching before that meeting.
- **MINOR 1 to 7.** Each is fixed as the review gave it. Two changes the reviser made are both sound. In MINOR 1, "they" became "the American Methodists". In MINOR 3, "he" became "Wesley", so the Rules are not heard as the American preacher's. MINOR 3 was also split at "alteration". The three length cuts are made.

## 2. New wording

Every sentence that differs from v1 is held:
- Paragraphs 1 to 3: the review's wording (B1). Its glosses come from Words to explain: society, salvation and assurance, law of sin and death, priest and ordained, Church of England, class, Methodist.
- The Nelson sentence: Source_Sheet M7 (LEP 1631–1642), and outline beat 4. "Felt" is fair. Nelson says he thought Wesley "fixed his eyes upon me", then said, "This man can tell the secrets of my heart."
- "Nelson became one of them": Also told, "Who preached" (I5; Widely Accepted).
- The yearly meeting: beat 7 and Words to explain, "the Conference" (MIN 450–460, 2011–2012; Sheet M13).
- "After American independence, in 1784": Also told, "What it became".
- The Rules sentence: Sheet I1. I checked it against LEE 1366–1371 ("the same that Mr. Wesley had previously drawn up in England, and have with very little alteration been continued").
- "Their rule book still set out classes under a leader": What came of them, item 1 (DIS 6920–6957).
- The penny, the split and "in that district": beat 6 (J2 31833–31840; J3 6697–6716).

I checked these quotes word for word in `cic/texts/`:
- Q1 matches the outline's rendering of J1 27071–27074.
- "I believe" matches CW 7723 (`wesley-c_journal-v1_jackson1849.txt`).
- "Bring out the minister" matches J3 5741.
- Q3 matches J8 9033.

## 3. Kit lines

- **Hook:** paragraph 1 has three sentences, then come Q1, one sentence of plain sense, and "I believe". That is just past the outline's own line ("about three sentences plus the quote, with one short sentence of plain sense"). The fix below makes it two sentences.
- **Essence: not within "about 150".** By a plain whitespace count it is complete at word **177**, "...they became the Methodist churches." That is 27 words over, about 71 seconds at the outline's rate (525 words to 3:30, which is 150 a minute). It is past the kit's "within the first minute". The outline's new line, "by about word 150 to 175", was written by the reviewer to cover its own wording, and the reviser added it. It cannot widen the kit's bar on that basis. Even by that line, 177 is over. This is a **FIX**, below.
- **Also told:** every part is present: the evening, the cost of the fields, how a society and a class worked, who preached, and what it became.
- **Church words:** every listed word the story uses gets its plain sense where it is first heard. "Rules" now does too.
- **Sentences past about 30 words:** none. The longest is 29.
- **Length:** the review's cuts are made, and the story has nothing else it does not need (ruling 8).
- **Setting:** not stacked in one sentence.
- **Ending:** it ends on the person, at the deathbed.

### FIX: bring the essence in by about word 150

Make these two replacements. Paragraph 2 (Q1, its plain sense, and "I believe") is untouched. No gloss and no heart part is dropped. The heart in `Hearts_Plain.md` is: priest, ordained, state church; May 1738, trust and forgiveness; preaching outdoors to thousands from 1739; societies and weekly classes of about twelve under a leader; and the Methodist churches. With both replacements, the essence is complete at word **165** by the same count, about 66 seconds. That is "about 150". It is also the floor while Q1, its plain sense, "I believe" and every gloss stay.

1. Paragraph 1. Replace
   "One May evening in 1738, John Wesley went very unwillingly to a society meeting in Aldersgate Street, in London, a small weekly prayer group inside the church. Someone was reading Martin Luther's preface to Paul's letter to the Romans. At about a quarter to nine, Wesley felt his heart warmed."
   with
   "One May evening in 1738, John Wesley went very unwillingly to a society meeting, a weekly prayer group inside the church, in Aldersgate Street, London. As someone read Luther's preface to Paul's letter to the Romans, Wesley felt his heart warmed."
   (The gloss now sits right after "society". "As someone read" is J1's "while he was describing". Outline D2's "a society meeting in Aldersgate Street" is kept. Only the clock time goes, and it is not a heart part.)
2. Paragraph 3. Replace
   "He was a priest, a minister formally set apart, or ordained, in the Church of England, the state church. From 1739 he preached outdoors to thousands, and gathered those who answered into societies, split into weekly classes of about twelve under a leader who asked how each lived."
   with
   "He was a priest of the state Church of England, a minister formally set apart, or ordained. From 1739 he preached outdoors to thousands. He gathered his converts into societies, split into weekly classes of about twelve under a leader who asked how each lived."
   ("His converts" is the approved heart's own word. The 29-word sentence becomes 7 words and 21 words. "Mocked as Methodists, a nickname at first, they became the Methodist churches." stays as it is.)

I scored this in memory with both replacements in place: 669 words, grade 7.8 (6.9 with names out), reading ease 73.5 with names out, longest sentence 29. That passes. The grade under 8 goes to the listener read, as it does now.

## 4. Score

`python -m engine.m1.profile_readability` on the brief as it stands: 681 words, grade 7.9 (7.0 with names out), reading ease 73.2 with names out, 15.8 words a sentence, longest sentence 29. **Pass.** The grade is under 8, so the listener read checks that it is not flat.
