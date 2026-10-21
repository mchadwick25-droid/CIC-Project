# Story Tellings Review — Round 1

**Scope:** the new `telling` field drafted for twelve desert story records (records/desert/story/), each checked clause by clause against its vendored source in cic/texts/.
**Reviewers:** two independent Agent invocations, model opus, with no part in the drafting (drafts by sonnet). Reviewer A took the six Vita Antonii, Cassian and Budge Paradise vol. 1 tellings; Reviewer B the six sayings, Kellia, Palladius and Ethiopic-rule tellings.
**Outcome:** ten CLEAR WITH FIXES, sarah-answer CLEAR, kellia-day NOT CLEAR (held back; see Open_Gaps_Tracking.md, the story-tellings entry of 2026-10-14).

---

## Review A: desert story tellings, Round 1

Reviewer A. I checked every clause against the vendored files myself, not against the drafter's quoted passages. Files:
- Vita Antonii: `cic/texts/npnf204_athanasius-select-works-letters.xml` (SS2-3 at 31233-31285; SS8-10 at 31454-31523; SS12-13 at 31548-31590; SS49-50 at 32431-32475; SS89-92 at 33436-33550)
- Cassian, Conf. X: `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (ch. II-III, about 35962-36058)
- Palladius/Budge: `cic/texts/palladius_paradise-v1-syriac_budge1907.txt` (lines 1117-1119)

The drafters' quoted passages match the vendored text in all six files. I re-ran the gate on all six as drafted, and every one passes (numbers below). Nothing in any telling is invented. Only one finding is SUBSTANTIAL: in antony-secret-burial, an order Antony gives is told as something he did himself.

---

## 1. antony-call: CLEAR WITH FIXES

Gate: fk 6.16, fre 80.18, 230 words. Pass.

1. MINOR. The telling says "He went out and gave those things to the poor as well, and he placed his sister..." In the telling, "those things" points back to nothing (the nearest candidate is "a little for his sister", two sentences earlier). The sentence also runs 26 words. Source (xml:31263-65): "went out and gave those things also to the poor." The record's own locus reads this as "giving away the remainder". Fix: "He went out and gave the rest to the poor as well. He placed his sister with known and faithful virgins to be brought up."
2. MINOR. The telling says "three hundred acres of good ground". "Acres" is the translator's word for ἄρουραι (xml:31250-52, translator's note: "The arura was 100 Egyptian cubits square"). Three hundred arourae is roughly 200 modern acres, so the modern unit misleads a little. Fix: "He gave the villagers his family's land, three hundred Egyptian field measures of good ground."
3. MINOR. The telling says "Then he began the discipline outside his house." "The discipline" is a term of art that the telling uses without introducing it. Source (xml:31267-69): "he henceforth devoted himself outside his house to discipline, taking heed to himself and training himself with patience." Fix: "From then on he gave himself to a life of discipline outside his house, training himself with patience."

Rulings on the drafter's questions:
- The apostle-reflection clause stays. Athanasius himself reports what Antony "reflected as he walked" (xml:31237-38). The not_for line rules out an inner life the source does not record, and this one it does record.
- 230 words is acceptable.
- On "those things": fix 1 uses "the rest", which matches the record's locus and the plain sense of the Greek. It does not add the commentators' reading that this was the sum kept for his sister.

## 2. antony-withdrawal: CLEAR WITH FIXES

Gate: fk 5.59, fre 80.95, 232 words. Pass.

1. MINOR (factual). The telling says "He had seen an old hermit there and copied his devotion." Here "there" means near his own village. Source (xml:31279-80): "in the next village an old man who had lived the life of a hermit". Fix: "He had seen an old hermit in the next village and copied his devotion."
2. MINOR. The telling says "the creatures, the bishop wrote, fled". The telling never says Athanasius was a bishop. Fix: "the creatures, Athanasius wrote, fled at once as if someone were chasing them."
3. MINOR. The telling says "with Saracens who were going that way." Today "Saracens" calls up the Crusades. In the Vita (xml:32455) the word means desert nomads. Fix: "with Saracens, desert nomads, who were going that way."

Rulings on the drafter's questions:
- "Left the world in stages" is acceptable. It summarises the order the Vita tells events in, and it supplies no reason for any move.
- The SS49 reason (beset by many people, not allowed to be still) and the voice's counsel are both in the source (xml:32431-32450), so they may stay. This does not breach the not_for line. But the record's own `not_for` ("Supplying Antony's reasons for each move, which the Vita does not give") and its `absent_detail` ("only that he moved on") are wrong about SS49, which does give reasons. This is a record defect to log in Open_Gaps, not a telling defect.
- The record's locus describes SS12-13 as "the crowds gathering outside". The source has acquaintances outside and noise inside the fort (xml:31567-70). The telling follows the source correctly. The locus wording should be logged for correction.
- 232 words is acceptable.

## 3. antony-tomb-combat: CLEAR WITH FIXES

Gate: fk 5.54, fre 77.67, 226 words. Pass.

1. MINOR. The telling says "bring him bread after many days." That reads as a single delivery. Source (xml:31456): "to bring him bread at intervals of many days". Fix: "He asked an acquaintance to bring him bread at long intervals."
2. MINOR. The telling says "Antony answered them". The demons have not spoken, and the source says "as in mockery he said" (xml:31496). Fix: "Antony mocked them:"
3. MINOR. The telling has Antony say "so you come in numbers." That drops the verb in "you attempt to terrify me by numbers" (xml:31497-98). Fix: "But the Lord has made you weak, so you try to frighten me with numbers."
4. MINOR. The telling has the voice say "have not been worsted". "Worsted" is archaic, below B2 comprehension. Fix: "You have endured and have not given way, so I will always help you, and I will make your name known everywhere."

Not_for check: the beasts and the roof keep the source's "seemed" and "as it were", and the whole telling sits under "Athanasius writes". The telling does not claim to know what happened in the tomb. Pass.

Rulings on the drafter's questions:
- The locus is too wide. SS12-13 belongs to antony-withdrawal, and the telling is right not to use it. Log in Open_Gaps that the locus should be narrowed to SS8-10. This is a record change, not a telling change.
- The cuts (the shout, "no blows by man", "attack if you can") are fine. Nothing was cut in a way that changes the meaning.

## 4. antony-secret-burial: CLEAR WITH FIXES

Gate: fk 6.70, fre 77.21, 237 words. Pass.

1. SUBSTANTIAL. The telling says "He gave one sheepskin and the garment he lay on to the bishop Athanasius, the other sheepskin to the bishop Serapion, and the hair garment to the two men." (29 words.) In the source, Antony does not hand anything over. He orders the attendants to do it: "And divide my garments. To Athanasius the bishop give one sheepskin... To Serapion the bishop give the other sheepskin, and keep the hair garment yourselves" (xml:33521-26). The telling turns a command into an act, and Athanasius cannot have been present on the mountain to be handed anything. Fix: "He told them to divide his garments. One sheepskin and the garment he lay on were for the bishop Athanasius. The other sheepskin was for the bishop Serapion, and the two men were to keep the hair garment." (I graded this with the closing lines and it passes: fk 4.79, fre 80.31.)
2. MINOR. The telling says "No one knows to this day where, Athanasius writes, save those two only." "Save" is archaic and the order of the sentence is awkward. Source (xml:33543-44): "no one knows to this day where it was buried, save those two only." Fix: "Athanasius writes that to this day no one knows where he lies, except those two."

Not_for check: the attendants are unnamed, their inner life is not given, and nothing about 561 or relics appears. Leaving out the SS92 "precious treasure" line was right. Pass.

Rulings on the drafter's questions:
- The record's divergence_note says Athanasius "says he received the account from the two attendants and inherited one of the two sheepskins himself (SS91)". The vendored SS91-92 says neither. SS91 has only Antony's order to give him a sheepskin. This is a record defect to log in Open_Gaps (the divergence_note overstates the source). The telling is right not to repeat it.
- Dropping SS91's "to avoid this I entered into the mountain" is acceptable. The link is still clear from the custom just described.
- 237 words is acceptable.

## 5. desert.story.sarapion-anthropomorphite: CLEAR WITH FIXES

Gate: fk 7.67, fre 68.70, 225 words. Pass.

1. MINOR (clarity). The telling never says that Sarapion held the belief. "the teaching seemed new to him" is left unclear, because a reader cannot tell which teaching. Source (xml, ch. III opening): "Among those then who were caught by this mistaken notion was one named Sarapion". Fix: insert after "...would allow the letter to be read.": "Sarapion was one of those who held the old belief." Then go on: "Paphnutius urged him many times, but the new teaching seemed strange to him, never handed down by his predecessors."
2. MINOR. The telling says "the picture of God he used to set before himself leave his heart". This drops "in prayer", which is the point of the scene (xml:36048-49: "which he used to set before himself in prayer"). Fix: "Sarapion felt the picture of God he used to set before himself in prayer leave his heart."
3. MINOR (craft). The closing sentence runs about 38 words and keeps the translator's archaic word order ("whom to worship and address I know not"). It is the only archaic speech in an otherwise modern telling. Fix (keeps every clause): 'He burst into bitter tears, threw himself on the ground, and cried out. "They have taken my God away from me," he said. "Now I have no one to hold on to, and I do not know whom to worship or speak to."' Keeping the verbatim translation is also acceptable if the series policy wants period wording inside quotation marks. In that case split it off as its own sentence after "and cried out."

Not_for check: the telling says "Cassian tells/says", gives nothing about Sarapion's later life, does not conflate him with Serapion of Conference V, and gives no year 399. Pass.

Rulings on the drafter's questions:
- The 27-word sentence that carries the Genesis verse is accepted as a judgment call.
- Leaving out 399 and Cassian's judgment words is correct. The year is in the translator's note, not in Cassian.

## 6. desert.story.virgin-who-hid-athanasius: CLEAR WITH FIXES

Gate: fk 5.71, fre 77.40, 209 words. Pass.

1. MINOR. The telling says "she fled from sight". "From sight" is added, because the source does not say where or how she fled. Source (Budge:1119): "because of her beauty she fled lest she should become the cause of stumbling unto men." Fix: "Because of that beauty she fled, so that she would not cause men to stumble."
2. MINOR (misleading reading). The telling says "he had fled to the woman no one could suspect of harm, since she was young and beautiful." This reads as though her beauty proved she was harmless. Budge's sense is that no one would suspect him of being with her. Source (Budge:1119): "I fled unto that woman concerning whom no man could suspect of harm, for she is young and beautiful." Fix: "He told those who truly loved him that he had fled to the one woman no one would suspect, because she was young and beautiful."

Not_for check: she is unnamed, there is no date, the thirty years are not repeated, no emperor is named, and the "Palladius tells" frame holds throughout. Pass.

Rulings on the drafter's questions:
- "Seventy" is not an internal contradiction in the source. She was about twenty and beautiful when she hid him. Palladius met her decades later, at about seventy. "She is young" is Athanasius speaking at the time of the hiding. The real problem in the text is the thirty-year span, and the record already handles that. Leave "seventy" out anyway: putting it next to "about twenty" invites the reader to count years, which the not_for line forbids.
- The drafter's Notes say the "oaths" line carries the dropped reasons. The telling does not contain the oaths line. The note is wrong, but leaving the line out is fine.
- Ending on "my own life and hers" is acceptable.

---

## Summary

| Story | Gate (fk / fre) | Verdict | Substantial | Minor |
|---|---|---|---|---|
| antony-call | 6.16 / 80.18 | CLEAR WITH FIXES | 0 | 3 |
| antony-withdrawal | 5.59 / 80.95 | CLEAR WITH FIXES | 0 | 3 |
| antony-tomb-combat | 5.54 / 77.67 | CLEAR WITH FIXES | 0 | 4 |
| antony-secret-burial | 6.70 / 77.21 | CLEAR WITH FIXES | 1 (bequest told as an act, not a command) | 1 |
| sarapion-anthropomorphite | 7.67 / 68.70 | CLEAR WITH FIXES | 0 | 3 |
| virgin-who-hid-athanasius | 5.71 / 77.40 | CLEAR WITH FIXES | 0 | 2 |

Record defects to log in Open_Gaps (record changes, not telling changes):
- antony-withdrawal: the `not_for` and `absent_detail` say the Vita gives no reasons for the moves, but SS49 does. The locus's "crowds gathering outside" misdescribes SS13.
- antony-tomb-combat: the locus includes SS12-13, which belongs to the fort episode. Narrow it to SS8-10.
- antony-secret-burial: the divergence_note says Athanasius received the account from the attendants and inherited a sheepskin (SS91). The vendored text says neither.


---

## Review B: desert story tellings, Round 1

Reviewer B. I checked every source passage myself against the vendored files. Budge = cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt. Palladius = cic/texts/palladius_lausiac-history_clarke1918.txt. Vita = cic/texts/npnf204_athanasius-select-works-letters.xml. Ethiopic = cic/texts/pachomius_rules-ethiopic_schodde1885.txt. I ran the readability gate on every draft and on every replacement given below.

| Story | Verdict | Substantial | Minor | Gate (draft) | Gate (with fixes) |
|---|---|---|---|---|---|
| moses-leaking-jug | CLEAR WITH FIXES | 1 | 1 | fk 4.28 / fre 87.6 | fk 4.08 / fre 89.7 |
| sarah-answer | CLEAR | 0 | 1 (optional) | fk 3.06 / fre 90.9 | same |
| arsenius-flee | CLEAR WITH FIXES | 0 | 1 | fk 5.07 / fre 82.4 | fk 5.06 / fre 82.2 |
| kellia-day | NOT CLEAR (replacement given; needs a recheck) | 3 | 2 | fk 8.30 / fre 66.9 | fk 7.32 / fre 72.4 |
| pachomius-founding | CLEAR WITH FIXES | 0 | 3 | fk 7.23 / fre 71.4 | fk 7.25 / fre 71.7 |
| angel-hands-the-tablet | CLEAR WITH FIXES | 1 | 2 | fk 6.35 / fre 75.5 | fk 6.10 / fre 75.9 |

---

## 1. desert.story.moses-leaking-jug — CLEAR WITH FIXES

The source is Budge:1160 (sec. 542). I checked it clause by clause and it matches. The object is a basket of sand, as the not_for requires. "faults" for "shortcomings" and "today" for "this day" keep the meaning. Budge's supplied "[The sands are]" is carried without its brackets. That is acceptable, because it is the translator's own sense of the line. FK 4.3 is low, but the prose doesn't read as choppy. There is no run of three or more very short sentences.

1. SUBSTANTIAL. The opening, "Among us at Scete, the camp of the monks, a brother committed an offence.", tells the council scene as a flat event. The record's not_for rules out "Presenting the council scene as verified single-event history", and absent_detail says the scene "is told as tradition". Budge has no hedge, so nothing is lost by framing it in the world's own voice. The Arsenius draft already does this ("Our sayings tell of"). Fix: replace the first sentence with: "Our sayings tell of a brother at Scete, the camp of the monks, who committed an offence."
2. MINOR. "A congregation gathered about it." reads as if people stood around the offence (Budge:1160 "a congregation was assembled on this matter"). Fix: "A congregation met on the matter."

Rulings on the drafter's notes: (a) Basket of sand, not a jug: correct. (b) Dropping `text`'s "to judge him", its narrated "The sand ran out behind him" and its "The tradition tells": correct, because the source has none of them. Fix 1 above adds a frame in the world's own voice, not a source hedge. (c) "faults" for "shortcomings": accepted. (d) The stale locus ("no vendored edition") is a record defect, not a telling defect. It affects this record, sarah-answer and arsenius-flee. Log it in Open_Gaps_Tracking.md. Separately, the record's own modern_contrast calls the image "a leaking jug", which contradicts its not_for. That is the same record-level fix.

## 2. desert.story.sarah-answer — CLEAR

The source is Budge:2438 (sec. 525), and the telling matches it word for word apart from "ye" to "you". There is no visit, challenge, motive or Greek clause, so the not_for is respected. One sentence is the right length for a one-line source.

1. MINOR (optional). "brethren" is archaic, but it doesn't mislead. "brothers" is plainer for a B2 reader and matches the record's `text` and tellable_as. Either is acceptable.

Ruling, Amma vs Mother: **keep "Amma".** Budge's "Mother" is his English for the honorific title. The world's own term record (records/desert/term/desert.term.geron-abba-amma.md: "abba for a man, amma for a woman") names that same title. Budge transliterates the male title ("Abbâ"), and every telling here writes "Abba". Translating only the female one as "Mother" would make the pair uneven and make her title sound less formal than his. The changed word sits in the narrator's frame, not inside the quoted saying, so no quotation is altered. The quoted words stay Budge's.

Rulings on the drafter's other notes: (a) The record's absent_detail ("the specific visit") and modern_contrast ("men who came to test her") have no support in Budge sec. 525. The telling is right to give neither. These are record-level defects; log them. (b) Also a record-level defect, outside the telling: the record body says its `text` "matches desert.quote.sarah-man-among-you's own modern_rendering exactly: 'It is I who am the man, and you who are the women.'" But `text` and Budge both say "a man ... women". That rendering adds "the" twice, and the claim of an exact match is false. Log it for the quote record. (c) The grade of one sentence only gives an indication: agreed.

## 3. desert.story.arsenius-flee — CLEAR WITH FIXES

The sources are Budge:54 and Budge:56. Both sayings match clause by clause. The two sayings stay separate. The voice stays "a voice" and isn't named as God's. That is correct, because Budge doesn't say whose voice it is, and so the record's own relation note claims more than its source. There is no Latin triad and no biography from the court.

1. MINOR. "They tell a second saying of the time when..." follows "Our sayings tell", so the sayings end up telling a saying. Fix: "A second saying tells of the time when he was living the ascetic life in the monastery."

The final sentence is 26 words, but it is almost all quoted speech, so I let it stand. "fundamental causes that prevent a man from committing sin" is Budge's wording. It is odd, but it doesn't mislead.

Rulings on the drafter's notes: following Budge over `text` ("basic causes", "as a monk", "live in silent contemplation") is correct. Not naming the voice is correct. Ending on the second saying is correct. The stale locus is the same record defect as in story 1.

## 4. desert.story.kellia-day — NOT CLEAR

I checked the sources: Palladius:225 (ch. VII [2], [5]; Nitria), Vita:31286-31291 (ch. 3), Budge:184 (sec. 64), and records/desert/source/desert.source.kellia-excavations.md (`work`, no vendored file).

1. SUBSTANTIAL. "The excavations show that cells at Kellia ranged from single cells to hermitages of several rooms, with oratories attached." The desert communities' "we" voice can't cite modern excavations (1965-1990). This breaks the voice and brings in a modern term, against drafting rule 8. The claim itself is supported by the source record's `work` ("single cells to multi-room hermitages with attached oratories"), so it should be stated in the world's own voice, without "excavations". Fix: see the replacement below.
2. SUBSTANTIAL. "The sayings speak of the Psalms in the cell." Budge:184 never says "cell", and it is one saying, not "the sayings". The drafter flagged this phrase. The claim has no support and should be cut.
3. SUBSTANTIAL. The lentils saying (Budge sec. 64) falls outside the cited locus. The apophthegmata locus is "the constant/near-constant Psalter recitation this world's own tradition attests as the substrate of prayer". Budge is the vendored edition of that source, so sec. 64 is inside the source but not inside the locus. Sec. 64 is a single night: one old man visits a companion, they recite through to morning, and they forget a dish of lentils. It attests one vigil between two men, not a cell's ordinary daily psalmody. It also brings food into the telling, close to the not_for "Adding details such as spare meals". The draft's own retelling also drifts. It says "the lentils they had cooked", but Budge:184 says the companion "cooked a few lentiles". It also gives the Psalms to "an old man", where Budge's "he" is unclear. Fix: drop sec. 64 entirely. Palladius's ninth-hour psalmody, labelled as Nitria, carries the Psalms element and is inside a cited locus. (Record-level: the apophthegmata locus names no specific saying, so it can't be checked. Log it in Open_Gaps_Tracking.md so a specific Budge saying can be named, or the locus removed.)
4. MINOR. "pieced together from separate pieces of evidence": "pieced"/"pieces" is clumsy, as the brief suspected. "No record tells us" is also build-speak in the world's voice. Both are fixed in the replacement.
5. MINOR. Only the Nitria sentence says it is from elsewhere. Antony's work (Vita:31283-31290, "at first he began to abide in places outside the village") was not at Kellia, and the draft doesn't say so. The replacement places it "outside his own village".

Rulings on the brief's questions:
- Does it stay within the four sources and loci? No. Sec. 64 falls outside the locus (finding 3), and "in the cell" has no support at all (finding 2). With both cut, everything left is inside the loci.
- Does it read as a story? No, and it can't fully become one. No source narrates a day, and turning it into one person's morning-to-night would invent both a schedule and a person (not_for 1). The honest shape is a short composed picture that moves from the cell to work, to the ninth hour, to the week's church. That gives the piece the shape of a day without inventing an order of hours. The draft read like a list of citations ("Palladius says ... The saying does not name the place ... Palladius adds"). The replacement keeps one attribution, to Palladius for Nitria, and drops the rest.
- "pieced together from separate pieces": yes, clumsy; replaced.

Replacement telling (134 words; fk 7.32 / fre 72.4). Each clause is traced below.

No account of ours tells one whole day at Kellia from morning to night. What we can give is a day put together from scattered evidence, and some of it comes from other places.

At Kellia a cell might be a single room or a dwelling of several rooms, with places of prayer attached. Outside his own village, at the start of his withdrawal, Antony worked with his hands, because he had heard that he who is idle should not eat.

Palladius tells of Nitria, a settlement like Kellia but not Kellia itself. There all the men worked with their hands at linen, so that all supported themselves. At the ninth hour, he says, anyone standing there could hear psalms rising from each dwelling. They went to the church only on Saturday and Sunday.

Trace: sentences 1-2 come from absent_detail and use_note.means. Sentence 3 comes from kellia-excavations `work` ("single cells to multi-room hermitages with attached oratories"). Sentence 4 comes from Vita:31283-31290. Sentences 5-8 come from Palladius:225 [5] ("All these men work with their hands at linen-manufacture, so that all are self-supporting ... at the ninth hour it is possible to stand and hear how the strains of psalmody rise from each habitation ... They occupy the church only on Saturday and Sunday"). "a settlement like Kellia but not Kellia itself" comes from the record's own locus.

A caution to raise with Mark, not a finding against the draft. The excavated Kellia remains are, to my knowledge, mostly later than 430, and the multi-room hermitages especially. The source record gives no dates for its findings, so I can't check this against anything in the repo. Stated in the world's voice for the years 320-430, the cell sentence may claim the fourth-century layout more firmly than the evidence allows. Recommendation: log it in Open_Gaps_Tracking.md against desert.source.kellia-excavations, and ask whether that record's `work` can be dated.

## 5. desert.story.pachomius-founding — CLEAR WITH FIXES

The source is Palladius:397-405 (ch. XXXII [1], the tablet, [7] and the paragraph after it). The figures are at Palladius:405: "amounting to 7000 men ... the first and great monastery is that where Pachomius himself dwelt ... it has 1300 members". Everything traces. The frame ("Palladius tells/says") holds through the vision, so not_for 1 is met. There is no brother John, no 346, no "nine houses". The tablet is brass, and nothing is merged from the Ethiopic. Source order is followed.

1. MINOR. "The first and greatest was the house where Pachomius himself had lived" overstates the source ("the first and great monastery"). In Pachomian usage, "house" also means a sub-unit inside a monastery, so a reader could take it the wrong way. Fix: "The first and great monastery was the one where Pachomius himself had lived, and he gives it thirteen hundred members."
2. MINOR. "the monasteries that kept this rule numbered seven thousand men" reads like a count. The not_for says "Treating Palladius's population figures as precise counts". The "Palladius says" frame already carries most of this. Fix (it keeps his number and adds no hedge he lacks): "In his own day, Palladius says, the monasteries that kept this rule held seven thousand men."
3. MINOR. "Pachomius objected that the prayers were few." The telling never says the tablet set prayers, so "the prayers" has nothing to refer back to. The tablet's prayer provisions sit at Palladius:397-405. Fix: "Pachomius objected that the prayers it set were few."

The work clause is acceptable: "proportionately to the strength of the eaters appoint to them their labours", rendered as "his work was to match that strength". There are three attributions in the first three sentences ("Palladius tells ... He says ... Palladius says"). They are heavy but not wrong, and I let them stand.

Rulings on the drafter's notes: (a) Not using pachomian-corpus or brother John: correct. Palladius has no such detail, and the not_for forbids presenting it as settled. (b) Dropping the lettered sections, stranger, probation and so on for length: acceptable, because nothing dropped changes the meaning. (c) Following source order for the objection: correct. (d) Keeping the population figures under Palladius's attribution: correct, with fix 2.

## 6. desert.story.angel-hands-the-tablet — CLEAR WITH FIXES

The source is Ethiopic:166-180. The superscription really is the first line of Part I (Ethiopic:166 "[Translation.] PART I.", then 168). The tablet is iron. The province is Thebes, not the Thebaid. There is no Palladius material. The frame ("begins by saying where it came from", "the text tells a story") keeps the not_for against telling the vision as an incident, and nothing dates the framing.

1. SUBSTANTIAL. "Its first words are: in the name of the holy Trinity, this is the ordinance which..." presents itself as the text's first words, but it inserts "this is". Ethiopic:168 reads: "In the name of the holy Trinity. The ordinance which the angel of the Lord commanded to Abba Pachomius." If a telling says "first words", the words must be verbatim. Fix: 'Its first words are: "In the name of the holy Trinity. The ordinance which the angel of the Lord commanded to Abba Pachomius."'
2. MINOR. "The angel said that he had become perfect" drops the source's qualifier (Ethiopic:170 "With regard to thyself thou hast become perfect"). The qualifier limits the perfection to his own life, which is the point of sending him to the "less perfect". Fix: "The angel said that, as for himself, he had become perfect, and that living on in the cave was now needless."
3. MINOR. The final paragraph shifts into the present tense ("answers", "says", "he says") after a past-tense narrative, against the past-tense rule. Fix: "At the end of the provisions, Pachomius answered the angel: "Few are these prayers." The angel said he had commanded it so that the weak also might keep the ordinance without grieving themselves. The perfect do not desire an ordinance for themselves. These things, he said, he had ordained for those who have no advisers."

Rulings on the drafter's notes: (a) The framing approach: accepted. (b) Following the source over `text` ("needless", the single line, "no advisers"): correct. (c) One correction to the notes, though the telling is not affected. The angel's last sentence is not "cut off by a page break". It continues at Ethiopic:180 ("manded them, and may come to the sacred rites openly with shining countenance."). Ending at "no advisers" is still a clean stop at a clause boundary and changes nothing. (d) Not using the translator's header: correct.

The full telling with all three fixes applied gates at fk 6.10 / fre 75.9 (207 words).

---

### Record-level items for Open_Gaps_Tracking.md (not telling defects; I edited nothing)
- moses-leaking-jug, sarah-answer and arsenius-flee: the loci and divergence_notes still say "no vendored edition", but Budge is vendored.
- moses-leaking-jug modern_contrast: "a leaking jug" contradicts its own not_for.
- sarah-answer absent_detail and modern_contrast: the "visit" and the men "who came to test her" have no support in Budge sec. 525.
- desert.quote.sarah-man-among-you: its modern_rendering adds "the man / the women". sarah-answer's body wrongly claims an exact match with that rendering.
- arsenius-flee body: it says "the voice in this saying is God's", but Budge says only "a voice".
- kellia-day apophthegmata locus: it names no specific saying, so it can't be checked.
- desert.source.kellia-excavations: its findings carry no dates. Check them against the record's years, 320-430.
