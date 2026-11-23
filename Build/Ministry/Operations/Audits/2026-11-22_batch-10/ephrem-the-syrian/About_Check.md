# Ephrem the Syrian: check of "What it was about" and "Room for it"

**FIX**

Every cited line was opened. The content of each new explanation holds. Each charge against Mani, Marcion and Bardaisan is Ephrem's, and each is credited to him. The Manichaean confession speaks for Mani's side on the two powers. No held text gives Marcion's or Bardaisan's own side: `cic/texts/` holds no Marcionite or Bardaisanite work, and the Book of the Laws of Countries appears only as a title, in other writers. The one fix needed is in how the credits are heard: three pronouns can be heard as the wrong speaker.

Count by `python -m engine.m1.profile_readability`: the brief as it stands is 338. With the outline's additions it is 410, grade 8.3, pass. With the fixes below it is 412 or 413, grade 8.5, pass. That is under 450, and nothing is cut.

## Findings

### 1. BLOCKING: "he" and "his" can be heard as the wrong speaker (check 3)

Heard once, the three credits blur:
- In "His followers' own prayers", "His" comes straight after "In Ephrem's telling, Mani taught". It can be heard as Ephrem's followers, and Ephrem's own hymns are prayers.
- In "Marcion, he says", "he" comes after a sentence about Mani's followers. It can be heard as Mani.
- In "Bardaisan, he wrote in a hymn, denied", "he" can be heard as Bardaisan himself. Bardaisan was known as a hymn writer, and the next paragraph is about his school's songs. The listener could take Bardaisan as the one who wrote the denial into a hymn, which reverses whose words they are.

Replace these three bullets in **Room for it** with:

  - Add (11 words): `A later prayer of Mani's own followers names the same two powers.`
  - Add (25 words): `Marcion, Ephrem says, taught that a second God, a stranger to this world and above its Maker, came down to lift souls out of it.`
  - Replace `To deny the body's resurrection, he answered,` (7 words) with `In a hymn, Ephrem charged that Bardaisan denied the body would rise. To deny it, he answered,` (17 words), +10. The rest of that sentence, `slanders God's justice and grace.`, stays.

Then change `Words added: 72.` to `Words added: 74.`, and change the **After** line to: `**After:** about 412 by the kit's count (trial text in scratch only, not in the brief): grade 8.5, reading ease names out 79.1, longest sentence 28. Pass.`

"A later prayer" also fixes a second problem. The held confession comes from Central Asia, centuries after Mani. Without "later", "his followers' own prayers" could be heard as coming from his own time.

### 2. MINOR: the citations for Mani and Marcion do not show every claim (check 1)

The claims hold in Mitchell, but not all of them at the cited lines. Line 403 is a discourse heading. "Became mixed" is not at 418/431/719/771; it is at 415, 727 and 819. "A second God" is not at 584/592/1003/1549; it is at 1559 ("another God") and 1603 ("these two Gods"). "Lift souls out" rests on 592 ("those weak Souls whom he brought up") and 1635 ("He came to purify them").

Item 3, replace the witness clause with: `Witnesses: Ephrem, as an enemy and credited as one (Mitchell 415, 418, 431, 719, 727, 771, 819).`
Item 4, replace the witness clause with: `Witness: Ephrem only, as an enemy and credited as one (Mitchell 584, 592, 1003, 1549, 1559, 1603, 1635).`
Item 3, replace "a later Manichaean confession-prayer from Central Asia (Le Coq's English) speaks of" with: `a later Manichaean confession-prayer from Central Asia (Le Coq's English; brief wording "a later prayer") speaks of`

### 3. MINOR: confidence for Bardaisan's own teaching is set too high (check 1)

"Widely Accepted as Bardaisan's teaching" rests on one modern editor, who says only that Bardaisan "seems" to have denied it. In the same note he cites Hort, who says Bardaisan kept the common faith "except on isolated points". This goes on the card, not in the brief, but one hedged editor cannot carry "Widely Accepted".

Item 5, replace the last sentence with: `Documented as Ephrem's charge. As Bardaisan's own teaching, Inferential-Thin: one modern editor's "seems", with Hort's caution beside it, and no work of Bardaisan's own held.`

### 4. MINOR: "rebirth" now sits next to a denial of rising (check 3)

Paragraph 3 keeps "the body's birth, death and rebirth" (Sozomen's "regeneration ... taught by the Greek philosophers", Sozomen 32090-32092). Paragraph 2 will now say Bardaisan denied the body would rise. A listener could take "rebirth" for the resurrection and hear the two as contradicting each other. The wording is approved and matches its source, so no brief change is asked. Add a guard to item 6: `Do not gloss "rebirth" as resurrection or as reincarnation; Sozomen gives only "regeneration ... taught by the Greek philosophers". Listening review: confirm it does not sound like a contradiction of paragraph 2.`

## Fairness and length, as asked

- **Mani:** told fairly. The teaching comes in its own content (two eternal powers, their mixing, the body as the soul's prison). It is credited to Ephrem, and his followers' own text confirms the two powers. "Prison" is Ephrem's wording; at 418 he puts it conditionally, and at 719 he quotes them calling the body "a covering ... from the evil Nature". It is credited as his.
- **Marcion:** told fairly, as Ephrem's account, with no held Marcionite voice. "Stranger" is the term Ephrem gives the Marcionites. "Second God" is Ephrem's framing (1603), and it is credited.
- **Bardaisan:** fair once finding 1 is fixed. "Charged" marks it as an enemy's charge. The editor's softer view stays on the card, as the kit allows.
- **Could any of it be shorter?** Only slightly. Marcion's sentence could drop "to this world and" (4 words), but "a stranger to this world" is what makes the Marcionite term plain. The Mani-followers sentence is the only one-sided-source balance in the paragraph, so it should stay. Mani's "were there from the start" is the heart of his teaching. Each line carries one teaching, and none repeats another. At about 412 of 450, no trim is needed.
- **Leave out (item 10):** sound. Scher 20612-20613 gives only "Satan ... y mit la discorde"; Ibas is in the editor's footnote.
- **Gaps.md:** both scans asked what each rival taught. Items 3 to 5 answer it.
