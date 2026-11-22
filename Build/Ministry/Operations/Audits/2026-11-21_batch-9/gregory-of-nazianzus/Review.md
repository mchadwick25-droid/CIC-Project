# Review: Gregory of Nazianzus

Brief: `gregory-of-nazianzus.brief.txt` (326 words; the live approved text with "Apollinarius" changed to "Apollinaris"). Approved before the kit; reviewed under the change order of 2026-11-19. No outline exists, so the source check traces each sentence to `2026-11-16_eight-standard-v1/drafts/gregory-of-nazianzus.refs.md`, the card's `quotationOriginals`, the rendering record `2026-11-16_eight-standard-v1/renderings/eight/comparison.md` (Q11-Q14), and the held files in `cic/texts/`.

## The test, from one hearing

1. **Who:** Gregory of Nazianzus, a bishop from the Cappadocian church, who led the believers loyal to the creed of Nicaea in Constantinople around 380.
2. **What happened:** He preached the Trinity in a small house of prayer called the Anastasia. Earlier, he had refused to fight over Sasima, the see his friend Basil gave him. The emperor put the Arian bishop out. Gregory gave up the see when bishops objected to his election. Later he wrote against Apollinaris that what Christ did not take on, He did not heal.
3. **Why the connection matters:** His teaching on the Trinity and on Christ's full humanity became the church's standard. A pope cited him in 680, and in 553 the emperor Justinian named him "Gregory the Theologian" among the Fathers.

**Essence** (from the census entry and what he is known for): the preacher whose sermons in Constantinople defended the Trinity and helped the faith of Nicaea return to the city, which won him the title "the Theologian"; with Basil, a voice of the Cappadocian church. **Also told:** Sasima and the friendship with Basil; his resignation of the see in 381; the letters to Cledonius against Apollinaris on Christ's human mind; how later writers and councils relied on him.

- Hook leads to the essence: yes. The first paragraph opens on the forty Arian years and the little house of prayer, names Gregory in the second sentence, and has the faith of Nicaea "rose again through Gregory's sermons" by word 81. "He preached the Trinity" comes at word 145. The essence arrives inside the first minute.
- Also told: Sasima, the resignation, Cledonius, Jerome, Agatho and Justinian are all present with their weight. His poetry (the card's "Bishop, preacher and poet") and the council of 381 are not told (see Minor 3 and 4).
- Life told once, in order: yes. The hook and essence reach ahead to 380. The beats then run in order: Sasima (372), Constantinople (380), resignation (381), the Cledonius letters (after 381). No event is told twice. "In Constantinople he preached the Trinity" expands the essence; it does not retell the Anastasia scene. What came of him is ranked rather than dated (680, then Jerome, then 553). This is not a jump back in the life, and it did not lose me on hearing.
- Ending: it ends on Justinian's letter, but the last words are the person's own title, "Gregory the Theologian". That title is why he is on the tree, so I judge the ending holds (see Minor 6).
- Names heard once that neither act nor link: **Cledonius** (Minor 1) and **Sabellius** (Minor 2). Everyone else acts (Theodosius, Agatho, Justinian) or links (Sozomen, Basil, Arius, Apollinaris, Jerome).
- Where I got lost: only for a moment, at "from the church of Cappadocian Christianity" (Minor 5). Nothing reads as a children's book or talks down.

## Scores

- **Voice: 4.** A documentary register, with Gregory's own voice in two quotes chosen for what only his words can do: the piglets and chickens show his temper and his scruple, and the Sabellius and Arius line states his doctrine. One phrase is stiff (Minor 5).
- **Craft: 4.** Fast hook into the essence, the life in order, and stakes told plainly (the emperor's order, the objection to his election). The legacy runs as three short reports at the end. It works, but it is the weakest stretch.
- **Rigor: 4.** Every sentence is held. Sozomen's belief is kept in his voice, and the emperor's order is not tied to Gregory's sermons. Two places where held sources differ, or say more, are not yet carried on the card (Minor 3 and 7).
- **Accessibility: 4.** Grade 9.4 (7.2 names out), reading ease 73.9, 17.0 words a sentence. The longest sentence is 31 words (the Sabellius line with its gloss), which is at the limit. "The see" and "church canons" are the only words a second-language listener may trip on. The narrator glosses the first; the card glosses the second.

## The score

`python -m engine.m1.profile_readability .../gregory-of-nazianzus.brief.txt`: 323 words, grade 9.4 (names out 7.2), reading ease names out 73.9, 17.0 words a sentence, 0.9 joining words per 100, 26% short sentences, longest sentence 31 words. **pass.**

## Source check

Each sentence traced to its source:

| Sentence | Held at | Result |
|---|---|---|
| Arians held the churches for forty years; 380 | Socrates V.7, SS 15049-15057; Sozomen VII.5, SS 40686-40689 | held |
| Nicene believers led by Gregory | Sozomen VII.5, SS 40644-40646 ("presided over") | held |
| Many bishops had called him there | Socrates V.6, SS 14926-14928 | held |
| Little house of prayer; Anastasia; Sozomen's belief | Sozomen VII.5, SS 40646-40660 ("as I believe ... arose from the dead ... through the discourses of Gregory"); "the Resurrection" from the NZ endnote at 40854-40856 | held, credited to Sozomen |
| Basil his closest friend | Oration 43, NZ 41422-41433, 41521-41522 | held |
| Basil made him bishop of Sasima; rival bishop claimed it; refused to fight | Letters 48-49, NZ 45775-45795 ("your Sasima", "the martial Anthimus", "I will not take up arms"); Letter 50, NZ 45825-45838 | held; the doubt over whether he took it up is on the card |
| Quote 1 | Printed NZ 45783-45785; rendering Q11 and Q12 FINAL, `renderings/eight/comparison.md` | verbatim to the FINAL rendering; printed text checked |
| He preached the Trinity; Quote 2 and its gloss | Oration 39.11, NZ 37405-37411 ("fuse God together, or to cut Him up into inequality"); rendering Q13 FINAL | verbatim to the FINAL rendering; gloss is Gregory's next sentence |
| November 380 order; Arian bishop left | Socrates V.7, SS 15005-15057 (26 November); Sozomen VII.5, SS 40666-40689 | held, force kept |
| Bishops objected to his election; he gave up the see | Sozomen VII.7, SS 40811-40832 | held as Sozomen tells it; Socrates differs (Minor 7) |
| Farewell: other churches full again, credit to grace | Oration 42.26, NZ 40853-40868 ("filled with worshippers ... not by me ... but by the grace which was with me") | held |
| Apollinaris: no human mind | Letter 101, NZ 44689-44690; sibling outline beat 4 (Socrates, Sozomen): Widely Accepted | held |
| Not taken on, not healed; joined, saved | Letter 101, NZ 44690-44692 | held, narrator's telling without quotation marks |
| Agatho, three centuries later, human will | Agatho's letter, SC 24722, 25195-25206 | held; Agatho quotes a different work of Gregory, not the Cledonius letter, and the brief does not say which work |
| Jerome, Quote 3 | Jerome, Lives 117, TJ 41567-41568; rendering Q14 FINAL | verbatim to the FINAL rendering |
| 553, Justinian, holy Fathers, Gregory the Theologian | SC 23054-23071 (heading), 23134-23138 | held, but in the letter as condensed with Hefele's digest (SC 23069-23071), not in Justinian's own full wording. Told as narration, not quoted, so this is acceptable. |

Quotes re-checked against `cic/texts/npnf207_cyril-jerusalem-gregory-nazianzen.xml` and `npnf203_theodoret-jerome-gennadius-rufinus.xml`. Each modern wording matches the card's `quotationOriginals` and the FINAL rendering, and each printed original stands at the lines cited. Sibling overlap: `apollinaris-of-laodicea` tells the same Cledonius answer in a clause credited to Gregory. `basil-of-caesarea` tells Sasima from Basil's side. Both are set by the slate and do a different job. Neither uses Gregory's quotes. `Overlap_Report.txt`: clear.

## Verdict

**PASS.** Nothing blocks. The approved wording stands. No Do not say lines are needed: there is no blocking error, and there is no outline.

## Findings

All are MINOR. None requires a change to the brief. Items 1, 2 and 5 are optional wording, since the brief is being re-recorded anyway. Items 3, 4, 7 and 8 belong to the card step.

1. **MINOR. Cledonius is heard once and neither acts nor links.** Optional: "to the priest Cledonius" → "to a priest".
2. **MINOR. Sabellius is heard once, with no page on the tree.** He sits inside Gregory's own words, and the narrator glosses him right away ("the one fusing God together"), so the listener is not lost. No change.
3. **MINOR. Poetry is not told.** The card's role is "Bishop, preacher and poet", but the brief has no room, and it is not lengthened. For the card step: keep "poet" sourced on the card (census `sourcing`: poems held in Greek; the canon poem in English, SC).
4. **MINOR. The council of 381 is not named.** The census teaser leads with it ("took the chair of the great council of 381, then resigned"), and `first-council-of-constantinople-381` is on the tree. The brief tells the objection to his election without saying it came at that council. Adding the council would lengthen the brief, so no change here. For the card step: add a trace from Sozomen VII.7 (SS 40769-40832). Its heading reads "Concerning the Second Holy General Council ... Abdication of Gregory the Theologian". Keep the chair itself as the Prolegomena's (NZ 23167-23184), credited to Browne and Swallow.
5. **MINOR. "from the church of Cappadocian Christianity"** doubles "church" and "Christianity", and catches the ear for a moment. Optional: → "from Cappadocian Christianity". Keep it if the tradition's full name is wanted as heard.
6. **MINOR. The ending is on a later emperor's letter.** It closes on the person's own title, which is the story's point. It passes. No change.
7. **MINOR (card). Socrates and Sozomen differ on the resignation.** Socrates V.7 (SS 15001-15006) has him resign at the emperor's arrival, before the Arian bishop left, because some murmured that he was a stranger. Sozomen VII.7 (SS 40811-40832) has him withdraw at the council because some bishops, especially those of Egypt, objected. The brief follows Sozomen's order and wording, which is fair for the brief. But the kit asks that, where two held sources differ, the card carry what the story has no room for, and the card's What is uncertain does not yet hold this. Add it there, crediting each historian.
8. **MINOR (card). Spelling.** The card's `keyWorks` ("Letters against Apollinarius") and `briefReferences` ("Apollinarius's teaching") still use the variant. Bring them to the tree's "Apollinaris" where they speak in our voice, and leave any quoted printed title as printed.
