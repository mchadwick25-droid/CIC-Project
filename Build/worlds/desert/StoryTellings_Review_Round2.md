# Story Tellings Review — Round 2

**Scope:** targeted recheck of the eleven revised tellings (kellia-day held back) against the Round 1 findings, each fix checked against the vendored source.
**Reviewer:** independent Agent invocation, model opus, with no part in the drafting or revision.
**Outcome:** ten CLEAR; sarapion-anthropomorphite NOT CLEAR on one sentence the Round 1 fix introduced. The reviewer gave the replacement sentence and judged no further round needed; it was applied word for word.

---

## Round 2 targeted recheck: desert story tellings

Independent reviewer, Round 2. Scope: the 11 r2 tellings (kellia-day held back). For each one I compared the r1 telling with the r2 text word by word. The only differences are the ones CHANGES.md lists, plus the one consistency edit it declares in antony-tomb-combat. I checked each change against the vendored source myself. Unchanged text was not re-reviewed.

Sources opened:
- Vita Antonii: `cic/texts/npnf204_athanasius-select-works-letters.xml` (31245-31285, 31455-31523, 33505-33548)
- Cassian, Conf. X ch. III: `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (36011-36055)
- Palladius/Budge v1: `cic/texts/palladius_paradise-v1-syriac_budge1907.txt` (1119)
- Budge v2 sayings: `cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt` (54, 56, 1160, 2438)
- Palladius/Clarke: `cic/texts/palladius_lausiac-history_clarke1918.txt` (395-405)
- Ethiopic rule: `cic/texts/pachomius_rules-ethiopic_schodde1885.txt` (166-180)

Gate: `engine.m1.gates.grade_text` run on every r2 file. All pass (fk <= 10, fre >= 60).

---

## antony-call: CLEAR
Gate: fk 6.14 / fre 79.56, 240 words.
- A1 FIXED. "gave the rest to the poor as well" matches xml:31265, "gave those things also to the poor". The sentence is now split in two.
- A2 FIXED. "three hundred Egyptian field measures of good ground" is accurate to ἄρουραι and the translator's note (xml:31249-51).
- A3 FIXED. "From then on he gave himself to a life of discipline outside his house, training himself with patience" matches xml:31272-74.
- New: none.

## antony-withdrawal: CLEAR
Gate: fk 5.87 / fre 79.36, 236 words.
- A1 FIXED. "in the next village" (xml:31279).
- A2 FIXED. "Athanasius wrote".
- A3 FIXED. "Saracens, desert nomads" (xml:32455). The gloss sits in the narrator's frame and is accurate for the period.
- New: none. (Non-blocking: "Athanasius wrote" is past tense, while the rest of the telling uses "tells us" and "says". Either tense is fine.)

## antony-tomb-combat: CLEAR
Gate: fk 5.65 / fre 77.18, 229 words.
- A1 FIXED. "at long intervals" (xml:31457, "at intervals of many days").
- A2 FIXED. "Antony mocked them" (xml:31498, "as in mockery he said").
- A3 FIXED. "so you try to frighten me with numbers" (xml:31501, "you attempt to terrify me by numbers").
- A4 FIXED. "have not given way" (xml:31519).
- The undeclared-by-reviewer edit, "except the acquaintance", is supported. The source's "his comrade alone watching" (xml:31471) is the same man who brought the loaves (xml:31466). New: none.

## antony-secret-burial: CLEAR
Gate: fk 6.06 / fre 79.21, 248 words.
- A1 (SUBSTANTIAL) FIXED. "He told them to divide his garments. One sheepskin and the garment he lay on were for the bishop Athanasius..." This is now a command, matching xml:33521-26, "And divide my garments. To Athanasius the bishop give...". No sentence runs past 25 words.
- A2 FIXED. "Athanasius writes that to this day no one knows where he lies, except those two" (xml:33543-44).
- New: none. The 248 words are above the brief's "about 220", but the extra words come from the required fix. That is not a finding.

## sarapion-anthropomorphite: NOT CLEAR (one new substantial finding; replacement given)
Gate (r2): fk 6.59 / fre 73.26, 243 words. Gate with the fix below: fk 6.64 / fre 72.83, 242 words.
- A1 FIXED in substance. The telling now says that Sarapion held the belief. But the wording of the fix brings in the new finding below.
- A2 FIXED. "in prayer" is restored (xml:36048-49).
- A3 FIXED. The cry is split off and put into plain English, and every clause is kept (xml:36052-54). Leaving out "Alas! wretched man that I am!" is unchanged from r1.
- NEW, SUBSTANTIAL. The r2 text says: "Sarapion was one of those who held the old belief. Paphnutius urged him many times, but the new teaching seemed strange to him". In the narrator's own voice, this calls the human-form belief "the old belief" and Theophilus's teaching "the new teaching". Cassian says the opposite. To him the human-form view is "this mistaken notion" (xml:36013), and the bishop's view is "the faith of the Catholic tradition" (xml:36040). Only to Sarapion did it "seem ... a novelty, ... not ever known to or handed down by his predecessors" (xml:36021-22). The r2 wording takes Sarapion's view as the narrator's fact. It also settles a contested question (which view was older) that the source does not settle. Exact replacement:
  > Sarapion was one of those who held that belief. Paphnutius urged him many times, but the bishop's teaching seemed new to him, never handed down by his predecessors.

  "That belief" points back to "the belief that God has a human form" in the paragraph before. "The bishop's" points back to Theophilus, the bishop of Alexandria. "Seemed new to him" keeps the newness as Sarapion's perception, as Cassian has it.

## virgin-who-hid-athanasius: CLEAR
Gate: fk 5.76 / fre 76.72, 206 words.
- A1 FIXED. "she fled, so that she would not cause men to stumble" (Budge v1:1119).
- A2 FIXED. "the one woman no one would suspect, because she was young and beautiful" gives Budge's sense ("that woman concerning whom no man could suspect of harm, for she is young and beautiful"). The sentence is 25 words, which is at the limit, not past it.
- New: none.

## moses-leaking-jug: CLEAR
Gate: fk 4.08 / fre 89.69, 134 words.
- B1 (SUBSTANTIAL) FIXED. "Our sayings tell of a brother at Scete, the camp of the monks, who committed an offence." The council scene is now framed as tradition, which satisfies not_for 1 (Budge v2:1160).
- B2 FIXED. "A congregation met on the matter" ("assembled on this matter").
- New: none.

## sarah-answer: CLEAR
Gate: fk 3.06 / fre 90.94, 20 words.
- B1 (optional MINOR) not applied. That is acceptable, since the Round 1 reviewer ruled that either reading is fine. The text is unchanged and matches Budge v2:2438.

## arsenius-flee: CLEAR
Gate: fk 5.06 / fre 82.23, 92 words.
- B1 FIXED. "A second saying tells of the time when he was living the ascetic life in the monastery" (Budge v2:56). The two sayings stay separate.
- New: none.

## pachomius-founding: CLEAR
Gate: fk 7.25 / fre 71.72, 193 words.
- B1 FIXED. "The first and great monastery was the one where Pachomius himself had lived" (Clarke ch. XXXII, "the first and great monastery is that where Pachomius himself dwelt ... 1300 members").
- B2 FIXED. "held seven thousand men" ("amounting to 7000 men"), still under "Palladius says".
- B3 FIXED. "the prayers it set were few" ("objected to the angel that the prayers were few", after the prayer provisions of the tablet).
- New: none.

## angel-hands-the-tablet: CLEAR
Gate: fk 6.10 / fre 75.94, 207 words.
- B1 (SUBSTANTIAL) FIXED. The superscription is now quoted verbatim: "In the name of the holy Trinity. The ordinance which the angel of the Lord commanded to Abba Pachomius." (Ethiopic:168).
- B2 FIXED. "as for himself, he had become perfect" ("With regard to thyself thou hast become perfect", Ethiopic:170).
- B3 FIXED. The final paragraph is in the past tense, and every clause matches Ethiopic:176.
- New: none. (Non-blocking: "The angel said that, as for himself, he had become perfect" could, heard aloud, briefly read as the angel speaking of himself. The next clause, "living on in the cave", settles it. "As for his own life" would be clearer, but this is optional.)

---

## Summary

| Story | Gate r2 (fk / fre) | R1 findings | Verdict |
|---|---|---|---|
| antony-call | 6.14 / 79.56 | 3/3 fixed | CLEAR |
| antony-withdrawal | 5.87 / 79.36 | 3/3 fixed | CLEAR |
| antony-tomb-combat | 5.65 / 77.18 | 4/4 fixed | CLEAR |
| antony-secret-burial | 6.06 / 79.21 | 2/2 fixed (incl. substantial) | CLEAR |
| sarapion-anthropomorphite | 6.59 / 73.26 | 3/3 fixed | NOT CLEAR: 1 new substantial ("old belief"/"new teaching"); fix gates 6.64 / 72.83 |
| virgin-who-hid-athanasius | 5.76 / 76.72 | 2/2 fixed | CLEAR |
| moses-leaking-jug | 4.08 / 89.69 | 2/2 fixed (incl. substantial) | CLEAR |
| sarah-answer | 3.06 / 90.94 | optional item not applied (allowed) | CLEAR |
| arsenius-flee | 5.06 / 82.23 | 1/1 fixed | CLEAR |
| pachomius-founding | 7.25 / 71.72 | 3/3 fixed | CLEAR |
| angel-hands-the-tablet | 6.10 / 75.94 | 3/3 fixed (incl. substantial) | CLEAR |

Once the one-sentence Sarapion replacement is applied word for word, that story is CLEAR. A further review round is not needed for it: the replacement is the whole change, and it has been gated.


---

## Appendix: the revision change list the recheck compared against

### Round 2 changes

Finding numbers are the reviewer's own (Review A numbers antony-* and Cassian/Palladius-Budge stories; Review B numbers the rest). Rulings were applied as stated; no other text was changed.

### antony-call

- Finding 1 (MINOR)
  - before: He went out and gave those things to the poor as well, and he placed his sister with known and faithful virgins to be brought up.
  - after: He went out and gave the rest to the poor as well. He placed his sister with known and faithful virgins to be brought up.
- Finding 2 (MINOR)
  - before: He gave his family's land to the villagers, three hundred acres of good ground.
  - after: He gave the villagers his family's land, three hundred Egyptian field measures of good ground.
- Finding 3 (MINOR)
  - before: Then he began the discipline outside his house.
  - after: From then on he gave himself to a life of discipline outside his house, training himself with patience.
- Grade: {'fk': 6.137499999999999, 'fre': 79.5575} (240 words)

### antony-withdrawal

- Finding 1 (MINOR)
  - before: He had seen an old hermit there and
  - after: He had seen an old hermit in the next village and
- Finding 2 (MINOR)
  - before: the bishop wrote, fled at once
  - after: Athanasius wrote, fled at once
- Finding 3 (MINOR)
  - before: with Saracens who were going that way
  - after: with Saracens, desert nomads, who were going that way
- Grade: {'fk': 5.870419303797469, 'fre': 79.35727452531648} (236 words)

### antony-tomb-combat

- Finding 1 (MINOR)
  - before: bring him bread after many days.
  - after: bring him bread at long intervals.
- Finding 2 (MINOR)
  - before: Antony answered them:
  - after: Antony mocked them:
- Finding 3 (MINOR)
  - before: so you come in numbers."
  - after: so you try to frighten me with numbers."
- Finding 4 (MINOR)
  - before: have not been worsted, so
  - after: have not given way, so
- Finding Consistency fix, not a reviewer finding (so "acquaintance" is used throughout this telling)
  - before: except his friend,
  - after: except the acquaintance,
- Grade: {'fk': 5.654636098981079, 'fre': 77.18133309073266} (229 words)

### antony-secret-burial

- Finding 1 (SUBSTANTIAL)
  - before: He gave one sheepskin and the garment he lay on to the bishop Athanasius, the other sheepskin to the bishop Serapion, and the hair garment to the two men.
  - after: He told them to divide his garments. One sheepskin and the garment he lay on were for the bishop Athanasius. The other sheepskin was for the bishop Serapion, and the two men were to keep the hair garment.
- Finding 2 (MINOR)
  - before: No one knows to this day where, Athanasius writes, save those two only.
  - after: Athanasius writes that to this day no one knows where he lies, except those two.
- Grade: {'fk': 6.061451612903227, 'fre': 79.21217741935487} (248 words)

### sarapion-anthropomorphite

- Finding 1 (MINOR)
  - before: Paphnutius urged Sarapion many times, but the teaching seemed new to him,
  - after: Sarapion was one of those who held the old belief. Paphnutius urged him many times, but the new teaching seemed strange to him,
- Finding 2 (MINOR)
  - before: Sarapion felt the picture of God he used to set before himself leave his heart.
  - after: Sarapion felt the picture of God he used to set before himself in prayer leave his heart.
- Finding 3 (MINOR)
  - before: He burst into bitter tears, threw himself on the ground, and cried: "They have taken away my God from me, and I have now none to lay hold of; and whom to worship and address I know not."
  - after: He burst into bitter tears, threw himself on the ground, and cried out. "They have taken my God away from me," he said. "Now I have no one to hold on to, and I do not know whom to worship or speak to."
- Grade: {'fk': 6.5921132897603485, 'fre': 73.25980392156865} (243 words)

### virgin-who-hid-athanasius

- Finding 1 (MINOR)
  - before: Because of that beauty she fled from sight, so that she would not cause men to stumble.
  - after: Because of that beauty she fled, so that she would not cause men to stumble.
- Finding 2 (MINOR)
  - before: He told those who truly loved him that he had fled to the woman no one could suspect of harm, since she was young and beautiful.
  - after: He told those who truly loved him that he had fled to the one woman no one would suspect, because she was young and beautiful.
- Grade: {'fk': 5.756492718446605, 'fre': 76.72318567961165} (206 words)

### moses-leaking-jug

- Finding 1 (SUBSTANTIAL)
  - before: Among us at Scete, the camp of the monks, a brother committed an offence.
  - after: Our sayings tell of a brother at Scete, the camp of the monks, who committed an offence.
- Finding 2 (MINOR)
  - before: A congregation gathered about it.
  - after: A congregation met on the matter.
- Grade: {'fk': 4.07779104477612, 'fre': 89.69370149253733} (134 words)

### sarah-answer

- No change. Reviewer B rated it CLEAR. The only item is the optional "brethren" -> "brothers"; the reviewer does not recommend it (either is acceptable), so it is not applied. Ruling applied: keep "Amma" (already in the telling).
- Grade: {'fk': 3.0599999999999987, 'fre': 90.935} (20 words)

### arsenius-flee

- Finding 1 (MINOR)
  - before: They tell a second saying of the time when
  - after: A second saying tells of the time when
- Grade: {'fk': 5.0552795031055915, 'fre': 82.22760869565218} (92 words)

### pachomius-founding

- Finding 1 (MINOR)
  - before: The first and greatest was the house where Pachomius himself had lived, and he gives it thirteen hundred members.
  - after: The first and great monastery was the one where Pachomius himself had lived, and he gives it thirteen hundred members.
- Finding 2 (MINOR)
  - before: In his own day, Palladius says, the monasteries that kept this rule numbered seven thousand men.
  - after: In his own day, Palladius says, the monasteries that kept this rule held seven thousand men.
- Finding 3 (MINOR)
  - before: that the prayers were few.
  - after: that the prayers it set were few.
- Grade: {'fk': 7.251411917098448, 'fre': 71.71974309153715} (193 words)

### angel-hands-the-tablet

- Finding 1 (SUBSTANTIAL)
  - before: Its first words are: in the name of the holy Trinity, this is the ordinance which the angel of the Lord commanded to Abba Pachomius.
  - after: Its first words are: "In the name of the holy Trinity. The ordinance which the angel of the Lord commanded to Abba Pachomius."
- Finding 2 (MINOR)
  - before: The angel said that he had become perfect, and that
  - after: The angel said that, as for himself, he had become perfect, and that
- Finding 3 (MINOR)
  - before: At the end of the provisions, Pachomius answers the angel: "Few are these prayers." The angel says he commanded it so that the weak also may keep the ordinance without grieving themselves. The perfect do not desire an ordinance for themselves. These things, he says, he ordained for those who have no advisers.
  - after: At the end of the provisions, Pachomius answered the angel: "Few are these prayers." The angel said he had commanded it so that the weak also might keep the ordinance without grieving themselves. The perfect do not desire an ordinance for themselves. These things, he said, he had ordained for those who have no advisers.
- Grade: {'fk': 6.095381642512081, 'fre': 75.94104347826088} (207 words)


### Grade table (gate: fk <= 10, fre >= 60; all pass)

| Story | fk | fre | Words |
|---|---|---|---|
| angel-hands-the-tablet | 6.10 | 75.94 | 207 |
| antony-call | 6.14 | 79.56 | 240 |
| antony-secret-burial | 6.06 | 79.21 | 248 |
| antony-tomb-combat | 5.65 | 77.18 | 229 |
| antony-withdrawal | 5.87 | 79.36 | 236 |
| arsenius-flee | 5.06 | 82.23 | 92 |
| moses-leaking-jug | 4.08 | 89.69 | 134 |
| pachomius-founding | 7.25 | 71.72 | 193 |
| sarah-answer | 3.06 | 90.94 | 20 |
| sarapion-anthropomorphite | 6.59 | 73.26 | 243 |
| virgin-who-hid-athanasius | 5.76 | 76.72 | 206 |

### Consistency check ("his friend" / "acquaintance")

- antony-tomb-combat: the draft said "an acquaintance" twice and "his friend" once. The last was changed to "the acquaintance" (listed above; the one change not tied to a reviewer finding). Now only "acquaintance" is used.
- antony-withdrawal: only "Friends who came" appears; no mixed terms (Review A notes the source word is "acquaintances"; not a reviewer finding, left unchanged).
- virgin-who-hid-athanasius: "neither kinsmen nor friends nor clergy" is a list of kinds of people, not a second name for one person; no inconsistency.
- No other telling uses two terms for one person.
