# Review: Hilary of Poitiers (`hilary-of-poitiers`)

Reviewer, batch 9, 2026-11-22. Read against the batch header, `Kit.md`, `Outline.md`, `Source_Sheet.md`, `Outline_Check.md`, `Recheck.md`, and the held texts in `cic/texts/`.

## The three lines, from one hearing

1. **Who:** Hilary, bishop of Poitiers in Gaul in the 350s and 360s, who stood with the faith of Nicaea against the Arian party.
2. **What happened:** after a quarrel with Saturninus of Arles, the emperor Constantius exiled him to Phrygia in 356. There he learned the Eastern debate and wrote On the Trinity and On the Councils. He spoke at Seleucia in 359, was sent home as a troublemaker, and brought the bishops of Gaul who had signed at Ariminum back to Nicaea by taking them back rather than shunning them.
3. **Why it matters:** he explained East and West to each other, Gaul's bishops held to Nicaea, and Martin, later of Tours, came into the church's service through him.

None of the three is blank or wrong.

## Essence, written first

Hilary, bishop of Poitiers, was exiled to Phrygia in 356. There he learned the Eastern bishops' quarrel and wrote On the Trinity against the Arians and On the Councils to explain the Eastern creeds to the West. He came home and led Gaul back to Nicaea, taking the signers of Ariminum back rather than shunning them. Martin of Tours had come to him before the exile. Also to be told: his plea to the "like in substance" bishops; Seleucia and the refused hearing at Constantinople; the Gallic bishops' letter and the excommunications; Milan in 364; his readers in Latin and Greek.

This matches the approved heart (Hearts.md, ruling 1; the outline's essence and Also told), which includes Martin in the essence and Milan and the excommunications in Also told.

## Score

`python -m engine.m1.profile_readability ...hilary-of-poitiers.brief.txt`: 675 words, grade 7.8 (names out 6.4), reading ease names out 77.5, 16.1 words a sentence, longest sentence 28 words. Pass. Grade 7.8 is under 8. On the listener read it is not flat: the sentences link by cause and time, and the run of short sentences in the Martin scene marks a turn.

Length: 675 by the scorer, at the cap. Not BLOCKING as it stands, but every restoration below must be paid for inside it.

| | Score | Reason |
|---|---|---|
| Voice | 4 | An adult narrator's voice throughout. The hook is Hilary's own admission and it does real work. No talking down, no AI cadence. The closing callback leans toward a summing up. |
| Craft | 3 | The hook and core essence land by word 156, and the life runs in order. But Martin, part of the approved essence, arrives only at word 193. Milan, the excommunications and Lucifer's dissent are gone, so the last third goes thin on conflict. |
| Rigor | 3 | All three quotes are verbatim and supported, and the witnesses are credited well. But one invented detail ("young") and the dropped heart and conflict items are rigor failures. |
| Accessibility | 5 | Every word to explain gets its plain sense when first heard (Nicaea, the two "substance" terms, Arian, exorcist, communion, Phrygia, Ariminum). The longest sentence is 28 words. Easy to follow once through. |

## Verdict: REVISE

## Findings

### BLOCKING

**B1. Invented age: "a young man named Martin" (paragraph 3).** No held line gives Martin's age. The checker struck "young" from the outline's essence for that reason (Outline_Check M11; CLAUDE.md, no invented age). Sulpicius says only that he left the army (NPNF211 872-874; CSEL1 6382). Change to "Martin, fresh from the army" (see B2 for the full sentence).
*Do not say line for the outline:* "a young man named Martin" or "the young Martin". Say: "Martin, fresh from the army". No source gives his age.

**B2. Martin, part of the approved essence, comes after the first minute.** The outline's essence ends "Before the exile, Martin, later of Tours, had sought him out and stayed with him." The story's essence paragraph ends at word 156 without him; Martin is first heard at word 193. Fix, at no net cost: end paragraph 2 with "Before the exile, Martin, later bishop of Tours, had already sought him out." (+12). In paragraph 3, replace "Sulpicius says that before the exile, a young man named Martin, fresh from the army, sought Hilary out and stayed with him." with "Sulpicius says that Martin, fresh from the army, stayed with him for a time." (−7). Delete "He would become bishop of Tours." (−6). The essence may reach ahead (Kit Part 3, Story beats), so this is not an event told twice.

**B3. Milan (364) dropped, and it is in the approved heart.** Also told, bullet 5: "His failure at Milan in 364, told only by himself" (PL10 49253-49280). It is not on the Cut first list. Restore it as its own short paragraph before the death, held to beat 7 and its Do not say (the emperor at Milan was Valentinian, so say "the new emperor", never Constantius). For example: "In 364, at Milan, Hilary accused the Arian bishop Auxentius, who then signed a confession that sounded orthodox. The new emperor took communion with him, and Hilary, calling it all a pretense, was ordered out of the city. Only Hilary tells it." (about 40 words).

**B4. The Gallic bishops' excommunications dropped; in the heart and the record's force.** Also told, bullet 4: "they cut off the leaders of the other side" (CSEL65 6918-6920, 6927-6930). The story keeps the letter's quote but drops what the letter did. Saturninus's fall then stands alone and reads as the only sanction. Not on Cut first. Restore after the quote: "They cut off the leaders of the Arian party from communion." (about 10 words). The letter names Auxentius first among them. If the reviser names him here, "Auxentius and other Arian leaders" works, and B3 can then say "Auxentius" without "the Arian bishop".

**B5. Lucifer's opposite line dropped: a disagreement the outline credits.** Beat 6: Lucifer "refused communion even with those who took the signers back; Sulpicius will not say who was right" (NPNF211 11434-11440). Hilary's choice to pardon rather than shun is the heart of his return (Also told, bullet 4). The one contemporary dissent from it, which the witness refuses to judge, has been cut. That leaves only the praise. Not on Cut first. Restore by role, as Names allows: "Another exiled bishop broke even with those who took the signers back. Sulpicius will not say who was right." (about 19 words).

**What pays (the story is at 675 by the scorer; B3 to B5 add about 70, and B2 is net −1).** All six Cut first items are already gone, so the savings come from parts the story does not need:
- Ending: delete "Hilary himself had said where he found the meaning of the creed: in the Gospels and the Apostles." (−18). It repeats the hook and reads as a summing up. Move the Sulpicius quote up so it closes the Gaul paragraph, introduced as "Sulpicius wrote:" (−3, for "writing as a friend," and "said"). End on the death: "Nothing is recorded of how." (outline Ending 1).
- Paragraph 9: "Hilary died in his own country, at Poitiers," becomes "Hilary died at Poitiers," (−4).
- Paragraph 4: "Saturninus then deceived the emperor, Hilary says, and Hilary was sent away. He wrote that a faction had exiled him on false reports." becomes "Saturninus then deceived the emperor, Hilary says, and a faction had him exiled on false reports." (−8). This keeps what Cut first item 5 says to keep.
- Paragraph 5: "It also reached out to Eastern bishops who said the Son is "like in substance" to the Father, his being only like the Father's. Hilary wrote to them as brothers." becomes "In it he also wrote, as to brothers, to the Eastern bishops who said the Son is "like in substance," his being like the Father's." (−7; also fixes M1).
- Paragraphs 1 and 2: "Hilary, a bishop in Gaul," becomes "Hilary, bishop of Poitiers in Gaul," and "Hilary was bishop of Poitiers, and in 356" becomes "In 356" (−5 net).
- Paragraph 2: "and he wrote to explain the Eastern creeds to the West" becomes "and explained the Eastern creeds to the West" (−3).

Together about −48, against about +70. The reviser should use the shortest wordings above and recount with the scorer. If the story still runs past 675, record the remaining words in `Revision.md` as the unresolved part. The heart items B3 to B5 are not to be traded away to reach the cap. The Kit says the record's force is never cut to meet a length. A heart that will not fit the approved length goes to Mark.

*Do not say line for the outline:* "Dropping beat 7 (Milan), the letter's excommunications, or Lucifer's opposite line for length." They are in the heart or are the record's conflict, and are not on Cut first. Cut only from Cut first, in order.

### MINOR

**M1. "his being only like the Father's" (paragraph 5).** The outline's gloss is "his being is like the Father's". "Only" carries Hilary's side's judgment into the narrator's voice. Delete "only" (done by the wording in What pays).
*Do not say line:* "only like the Father's". Say: "his being like the Father's".

**M2. Dropped outline items not on Cut first, outside the heart (named, as the header asks).**
- What came 1: Augustine studied Hilary's formula and called him a man of real authority (NPNF103 9185-9192), and a historian at Constantinople praised his Latin books (NPNF202 10946-10953). The outline ranks this heaviest. Only Theodoret and Cassian were on Cut first. The Teacher shape's impact is in later readers, and the story now has none. Restore one clause for Augustine if words allow after B3 to B5. Otherwise it goes to the card.
- What came 2: Rufinus's "gentle and calm ... most able at persuading", and his books correcting those far off (RUF 28728-28739). Card, if not restored.
- Beat 2: Sulpicius on the exiles' offer to cut off Athanasius if the faith were first examined (NPNF211 11141-11145). The Athanasius link is lost from the audio. Card.
- Beat 6: "the rest were pardoned"; "he condemned Ariminum". Small, and implied by "brought them back to repentance".

**M3. Source sheet citation for the refusal of communion (no story change).** Row 2b cites NPNF209 7775-7777 for "Hilary and the Gallic bishops had denied Saturninus communion". That line (PL10 38615-38618, "negata ipsi usque hoc tempus toto jam triennio communione") says the bishops denied it for three years up to 358-359. It does not say Hilary did it, or that it came before Béziers. The order the story tells is held elsewhere: the Maurist note at PL10 38672-38676 cites Hilary's Against Constantius 2, that he "cum Gallicanis episcopis" withdrew from the communion of Saturninus, Ursacius and Valens after the Milan council. The card should cite Against Constantius 2 (PL10 46205 on) for the story's sentence.

**M4. "That same year, at Ariminum ... had been terrified" (paragraph 7)** steps back a little to set up the signers. It is background, not a retold event, and a listener follows it. No change needed.

### Checked and holding

- Quote 1: PL10 43844-43848 "Regeneratus pridem, et in episcopatu aliquantisper manens, fidem Nicaenam numquam nisi exsulaturus audivi: sed mihi homousii et homoeusii intelligentiam Evangelia et Apostoli intimaverunt"; NPNF209 9881-9884. It matches the outline's rendering and the story word for word.
- Quote 2: CSEL65 6815-6820 "ex litteris enim uestris, quas dilecto fratri et consacerdoti nostro Hilario credidistis, fraudem diaboli et conspirantia aduersus ecclesiam domini haereticorum ingenia cognouimus, ut diuisi in partibus Orientis atque Occidentis diuersis inuicem opinionibus falleremur". It matches the outline and the story word for word.
- Quote 3: CSEL1 5656-5658 "illud apud omnes constitit unius Hilarii beneficio Gallias nostras piaculo haeresis liberatas"; NPNF211 11433-11434. It matches, kept in Sulpicius's voice.
- Martin's deacon, exorcist and monastery (NPNF211 872-890, 977-980; CSEL1 6384-6392). Seleucia, received, the governors (NPNF211 11253-11277). Constantinople, three papers, troublemaker, exile not lifted (NPNF211 11399-11411). Ariminum, terrified by threats (NPNF211 11396-11398). Frequent councils, almost all, Saturninus cast out (NPNF211 11414-11428). Death in the sixth year after return (NPNF211 11441-11442). Béziers and Saturninus's deceit, in Hilary's voice (NPNF209 7773-7789). On the Trinity as twelve books (PL23 60466-60467). On the Councils at the bishops' request (NPNF209 7843-7846) and the plea (NPNF209 9860-9861). All hold, and all are credited as the outline says.
- Every Do not say item is honored: no deacon ordination, no "to learn", no pardon or recall, no Greek, no "alone" in the narrator's voice, no Ligugé, no flat 367.
- Names: Hilary, Constantius, Martin, Sulpicius Severus and Saturninus. Each acts or links. No name is heard once without a role.
- Order after the essence: Martin, Béziers, Phrygia, On the Councils, Seleucia, Constantinople, home, death. Told once, in order. It ends on the person.
