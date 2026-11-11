# Round-2 targeted recheck, set B (Methodius, Ephrem, Gregory of Nyssa, Gregory of Nazianzus)

Reviewer: Opus, independent. Scope: only what changed since round 1, checked against the round-1 findings (R1_set1.md, R1_set2.md), plus every claim on the four new cards.

Method: each claim was opened at the file lines with sed -n / grep -n. Files are under /home/user/CIC-Project/cic/texts/. Quotes were checked by exact substring after stripping tags and collapsing whitespace (script: scratchpad/r2/q.py). The candidate replacement briefs were scored with score.py. They are in scratchpad/r2/ (methodius.txt, ephrem.txt, nyssa.txt).

Abbreviations: AN = anf06_gregory-thaumaturgus-...-methodius-arnobius.xml; NJ = npnf203_theodoret-jerome-gennadius-rufinus.xml; SO = npnf202_socrates-sozomen-ecclesiastical-histories.xml; GW = npnf213_gregory-great-ephraim-syrus-aphrahat.xml; PA = palladius_lausiac-history_clarke1918.txt; NY = npnf205_gregory-nyssa-dogmatic-treatises.txt; CL = gregory-nyssa_life-of-macrina_clarke1916.txt; NZ = npnf207_cyril-jerusalem-gregory-nazianzen.xml; JW = npnf206_jerome-principal-works.xml; SC = npnf214_seven-ecumenical-councils.xml.

## Quotes

- Methodius: "may, like a restored temple, be raised up again with the same parts, uninjured and immortal, while sin is utterly and entirely destroyed." against AN 35398-35402. MATCH.
- Ephrem: "See, on your behalf I appoint myself hospitaller." against PA 471. MATCH.
- Nyssa: "the advance has no check" against NY 44061. MATCH.
- Nazianzus: "For that which He has not assumed He has not healed; but that which is united to His Godhead is also saved." against NZ 44690-44692. MATCH. The card's "and not to Sasima as some would falsely persuade you" against NZ 47707-47709. MATCH.
- Methodius, Epiphanius's praise: the file has "a learned man and a most valiant defender of the truth" (AN 29811-29812; Clark quoting Epiphanius, with the Greek at AN 29806-29808). Neither the brief nor the card puts this in quotation marks, so dropping "most" in the brief is a fair paraphrase and not a misquote. The card keeps "most". No finding.

## score.py (current drafts)

| Person | Words | FK | FRE | In band |
|---|---|---|---|---|
| Methodius | 221 | 8.5 | 60.0 | yes, FRE exactly at the floor |
| Ephrem | 270 | 9.7 | 62.2 | yes |
| Nyssa | 292 | 8.7 | 62.9 | yes |
| Nazianzus | 278 | 8.7 | 61.9 | yes |

## A finding that applies to all four cards

**X1. STANDARD: the "uncertain" lines restate the brief word for word.** Mark ruled that "uncertain" repeats the brief's caveat in its own words before it adds detail, and that the card carries the story on rather than restating it. All four cards copy the brief's sentences instead:
- Methodius: "Others put his death under Decius and Valerian, but that cannot be right, since Methodius wrote against Origen long after Origen died." Also "... so he is not a neutral witness."
- Ephrem: "Later Lives add wonders that the early witnesses never mention." Also the Palladius / Sozomen line.
- Nyssa: "But some of his sermons speak of eternal fire with no hint of it, so readers have argued over what he meant."
- Nazianzus: "He likely never served at Sasima. Another bishop held the village with troops, and his father begged him to stay home."

Replacement text is given under each person.

---

## Methodius of Olympus: REVISE

Round-1 findings:
- R1-1 (Clark as witness): resolved. Clark is gone from the audio.
- R1-2 (Socrates's story and Jerome's "against Origen"): resolved. Checked against SO 18135-18156 and NJ 41098-41100.
- R1-3 (long quote sentence): not resolved. The sentence still runs to 28 words, and the quote now opens mid-clause on "may," (see M2).

Checked and sound:
- "Socrates defended Origen and called his critics worthless": SO 18135-18141.
- Olympus, then Tyre: NJ 41096-41097.
- Martyrdom at Chalcis, and "as others affirm" under Decius and Valerian: NJ 41103-41105.
- Origen's "fetter", the body "no chain", "soul and body joined": AN 35866-35895.
- The fig tree in the temple, and death tearing it out: AN 35380-35398.
- Jerome on his "polished and logical style": NJ 41097.
- Theodoret's passage from the sermon on martyrs: NJ 20518-20530.
- "Long after Origen died": AN 29767-29770, told directly.

1. **BLOCKING (minor): a year is put in Jerome's mouth.** The brief says: "He died a martyr at Chalcis, Jerome says, at the end of the last great persecution, around the year 312." Jerome says only "At the end of the recent persecution" (NJ 41102-41103). The year 312 comes from a modern endnote (NJ 41093, "Died 311 or 312") and from Clark (AN 29762). The listener hears it as Jerome's. Replace paragraph 3's second and third sentences with:
   "Jerome says he was bishop of Olympus and later of Tyre, and that he died a martyr at Chalcis at the end of the recent persecution. That was around the year 312."

2. **STANDARD: the quotation is hard to follow aloud and the sentence runs long.** "Then, he writes, the flesh 'may, like a restored temple, be raised up again ...'" is 28 words. Spoken, the bare "may" also sounds like "maybe". Start the quote at a clean clause, which still ends on the strong close. Replace the last two sentences of the theology paragraph ("Death tears the tree out. Then, he writes, ...") with:
   "Death tears the tree out, so that the temple can stand again. The flesh is then raised, he writes, "with the same parts, uninjured and immortal, while sin is utterly and entirely destroyed.""
   The quoted words are a contiguous substring of AN 35400-35402. MATCH. The phrase "so that the temple can stand again" is AN 35392-35393, "so that the temple may be preserved".

3. **STANDARD: a flat ending made of citations.** The brief ends: "Epiphanius called him ... and Jerome praised his style. Theodoret kept a passage from his sermon on martyrs." That is a string of "X said" lines, ending on a fact rather than an image or his own voice. Move the legacy paragraph before the theology paragraph, so the brief ends on the fig tree and his own words. The full order would be: Socrates, then "Little else is certain", then the legacy lines, then "Jerome lists his book On the Resurrection ..." through the quote.
   With M1 and M2 applied, scratchpad/r2/methodius.txt gives 222 words, FK 8.1, FRE 61.9, in band. It also raises FRE off the 60.0 floor.

4. **STANDARD: three problems on the card.**
   - (a) X1 applies. Replace `uncertain` with:
     - "Jerome knew two dates for his death. The later one, around 312, fits his writing against Origen after Origen's death, and the earlier one, under Decius, does not. Some place Chalcis in Syria rather than Greece, because Syria lay nearer his diocese. Epiphanius also calls him Eubulius, which may only be the pen name he used in his Banquet." (AN 29754-29770)
     - "Only Socrates tells of his change of heart, and Socrates admired Origen. He names the dialogue in which Methodius praised him: Xenon." (SO 18135-18156)
   - (b) `legacy_remembered[0]` uses the editors as witnesses ("Yet the editors note that Origen's way of reading Scripture shaped him too"). Tell it through an ancient witness instead: "Remembered chiefly as Origen's opponent. Socrates names him first among the four who reviled Origen." (SO 18141-18145)
     `legacy_remembered[1]` restates the brief's Epiphanius line. Replace it with: "Honored as a martyr. Jerome says he was crowned with martyrdom at Chalcis, and Theodoret calls him the holy Methodius, bishop and martyr." (NJ 41104-41105, 20518-20520)
   - (c) Two lines are tilted.
     - `key_works` On Free Will says "critics doubt it is his". The file says recent critics doubt it, "although the internal evidence must be said to confirm the ancient testimonies which assign it to Methodius" (AN 29777-29780). Jerome lists it "also against Origen" (NJ 41099-41100). Replace the "about" text with: "A treatise Jerome lists as his, also against Origen."
     - `legacy_traces[1]` says his commentaries "survive only in slight fragments". The file says the Porphyry writings are lost except for slight fragments, "as are also his exegetical writings" (AN 29781-29783). Replace the clause with: "His books against Porphyry survive only in slight fragments, and his commentaries are lost."
     - `legacy_traces[0]` restates the brief's praise. Cut it to: "Epiphanius made great use of him in his own refutations of Origen." (AN 29738-29739)

---

## Ephrem the Syrian: REVISE

Round-1 findings:
- R1-1 (Gwynn as witness): resolved in the audio.
- R1-2 (Bardaisan as a living rival): resolved. Checked against GW 11184-11186 and NJ 15058-15060.
- R1-3 (Sozomen "same way"): resolved.
- R1-4 (theology): resolved. Checked against SO 32090-32101, GW 11182-11184 and GW 11205-11217. "Slanders God's justice and grace" is a fair rendering of the Nisibene Hymn 51 lines.
- R1-5 (flat ending): only partly resolved (see E2).
- R1-6 (long sentences): not resolved. There are new sentences of 37, 31 and 28 words (see E1 and E2).

Checked and sound:
- The famine scene, the trust question, "man of God", the quote, some 300 beds, a year, and death after a month: PA 471.
- Jacob, the three sieges, Jovian in 363, and the cell on the Mount: GW 10605-10620.
- Harmonius, Ephrem's fear, and the same melodies: SO 32083-32101.
- Festivals of the martyrs: NJ 15063-15066.
- Read after the Scriptures: NJ 41541-41543.

1. **STANDARD: a 37-word opening sentence.** "Palladius tells what came next: the rich said ..., so Ephrem asked ..., and they said ..." The first fifteen seconds decide whether the rest is heard. Also, "while their wealth sat idle" loses Palladius's point that the wealth was "corrupted for the condemnation of your souls" (PA 471). Replace the whole first paragraph after its first clause with:
   "When famine struck Edessa, Ephrem left his cell and asked the rich why they let people die while their wealth went to ruin. Palladius tells what came next. The rich said they had no one honest enough to run the relief, so Ephrem asked what they thought of him. They said they knew him for a man of God, and he answered: "See, on your behalf I appoint myself hospitaller.""

2. **STANDARD: a citation list and a flat ending, the remainder of R1-5 and R1-6.**
   - "Sozomen says ..., Theodoret says ..., and Jerome says ..." is 31 words and reads as a list of sources.
   - The last sentence (28 words) ends on the few-days quibble and on "later Lives add wonders that the early witnesses never mention". That ends the brief on a note about sources, not on the man.
   - Both details already sit on the card's "uncertain" list. So they leave the audio, and the card then carries them without restating the brief.
   Replace the last two paragraphs with:
   "It worked. From that time on, Sozomen says, the Syrians sang the hymns of Ephrem. In Theodoret's day they still brightened the festivals of the martyrs, and some churches read his writings aloud after the Scriptures.
   Ephrem ran the relief for a year, with some three hundred beds. When the famine ended and the people went home, he returned to his cell, and a month later, Palladius says, he died there."
   Sources: SO 32101, NJ 15065-15066, NJ 41541-41543, PA 471.
   With E1 applied, scratchpad/r2/ephrem.txt gives 269 words, FK 8.4, FRE 66.9, in band.

3. **STANDARD: modern editors as witnesses on the card, and fields mislabeled.**
   - `legacy_traces[2]`: "which Gwynn counts as the nearest-in-time life we have". Tell it directly: "Gregory of Nyssa gave a speech in his praise, the account of his life nearest to his own time." (GW 10659-10661)
   - `legacy_remembered[1]`: "Gwynn calls him the one Syrian known and revered throughout Christendom". An ancient witness says it better: "Honored beyond Syria. Sozomen calls him the greatest ornament of the Catholic Church." (SO 32050-32051)
   - `legacy_remembered[0]`: "are still read" is the 1898 editor's present tense. Change it to "were appointed to be read in its regular worship." (GW 10638-10640)
   - `legacy_traces[0]`: "He says Ephrem wrote three hundred thousand verses" overstates. Sozomen says "It is said that he wrote" (SO 32070-32071). Change it to "He reports it was said that Ephrem wrote three hundred thousand verses".
   - `legacy_traces[3]`, the feigned madness, is a story from his life, but the page shows this field as "What traces to him". Move it to `uncertain` and tell it as Sozomen's story: "Sozomen tells that when men came to carry him off to be a bishop, he ran into the market-place, dragged his clothes and ate in public, until they took him for mad and left. He stayed a deacon all his life." (SO 32127-32137)
   - With E2 applied, the card's `uncertain` lines on the later Lives and on Palladius and Sozomen no longer restate the audio, so X1 is met for Ephrem. If the drafter keeps either caveat in the audio, the card must reword it.

---

## Gregory of Nyssa: REVISE

Round-1 findings:
- R1-1 ("in this life"): resolved. Checked against NY 199-200.
- R1-2 (restoration): resolved in the audio. Checked against NY 1525-1538 and NY 39688-39690. Macrina is the speaker; "said I" comes at NY 39655.
- R1-3 (subject of the quote): resolved. Checked against NY 44046-44061.
- R1-4 (editors as witnesses): resolved in the audio. The Macrina paraphrase (CL 214-218) carries no quotation marks and is faithful. The Nazianzus letter (NZ 46258) checks.
- R1-5 (381): resolved. Checked against NY 864-883.
- R1-6 (theology): resolved. Checked against NY 185-195.

Checked and sound:
- 379 and months after Basil's death: CL 52.
- The exile under Valens: CL 214.
- 372 "in spite of his emphatic protest": NY 708-710.
- The Arian bishops' charge of irregularity, 376 and 378: NY 763-794.
- Macrina's persuasion and Basil's monastery: NY 651-655.
- "Father of Fathers": NY 464. The footnote at NY 942 names the second council of Nicaea.

1. **STANDARD: paragraph 2 confuses the ear.** "Macrina had been the one to bring him back." The listener has not been told he left anything. The next sentence is 34 words and joins Nazianzus's letter and Macrina's persuasion with "and", as if they were one event. The file gives what he left: Nazianzus says he had "cast away the sacred and delightful books which you used once to read to the people" (NZ 46252-46254). Replace the first two sentences of paragraph 2 with:
   "Macrina had turned him around once before. As a young man Gregory gave up reading the Scriptures to the people in order to teach rhetoric. His friend Gregory of Nazianzus wrote to ask why he would rather be called a professor of rhetoric than of Christianity. But it was his sister who persuaded him to join the family's monastery."
   The sentence on 381 is also 31 words. Split it: "In 381 he brought a treatise against Eunomius to the council at Constantinople. Before it closed, the emperor named him one of the bishops by whose communion the Catholic church would be known." (NY 880-883, "Shortly before the close of the Council")

2. **STANDARD: the legacy beat is one line with an abstract witness.** "Later writers called him the Father of Fathers." The witness is "later writers", and that is the whole legacy beat for a major figure. The Library has concrete, ancient material:
   - The council in Trullo, in 692, set its seal on the canons of "Gregory, Bishop of Nyssa" (SC 26715-26747, with the date at SC 1602). His Canonical Epistle to Letoius stands among the canons (SC 43991).
   - The footnote names the second council of Nicaea as the source of "Father of Fathers" (NY 942).
   Replace the first sentence of the last paragraph with:
   "A later council made one of his letters part of church law, and the second council of Nicaea called him the Father of Fathers."
   With N1 and N2 applied, scratchpad/r2/nyssa.txt gives 326 words, FK 8.2, FRE 64.6, in band. It runs past the 200-270 guide. If it must be trimmed, the restoration paragraph's middle sentence can go, because the card carries the restoration debate.

3. **BLOCKING: card lines rest on the editors' word, and one is not borne out.** `legacy_remembered[0]` reads: "the volume's editors list Jerome, Socrates and Theodoret among those who praised him" (NY 455-461). The ancient authors' own words in the files were checked:
   - Jerome says only that Gregory "a few years since read to Gregory Nazianzan and myself a work against Eunomius" (NJ 41712-41714). That is not praise.
   - Socrates, in the files, only names him as "Basil's brother" (SO 14035). He also names him as sharing the patriarchate of Pontus (SO 15175). Neither is praise. Socrates's warm passage (SO 13880-13934) is about Basil and Nazianzus.
   - Theodoret does praise him (NJ 15091-15096, 36815-36818).

   Replace the line with:
   "Theodoret counted him and Basil among the foremost champions of piety in Cappadocia. He wrote that the brothers taught their own age and left their teaching in their writings as a goodly heritage."

   Add Jerome's scene to `legacy_traces` if wanted: "Jerome heard him read his work against Eunomius aloud to Gregory of Nazianzus and himself." (NJ 41712-41714)

4. **STANDARD: the card's legacy_traces are life events, not legacy, and the editors are named as witnesses in `uncertain`.**
   - All four `legacy_traces` lines are things that happened in his life: the Meletius sermon, the court funerals, the Life of Thaumaturgus, and the synod of 394. The page shows this field as "What traces to him".
   - The Pulcheria and Flaccilla line also overstates. It says he praised her "because" of Eunomius, but the file says this was "one of the subjects of Gregory's praise" (NY 899-902).
   Replace `legacy_traces` with:
   - "Theodoret copied a passage from his sermon on Abraham into his collection of witnesses from the Fathers." (NJ 20803-20806)
   - "In 553 the emperor Justinian's letter to the council at Constantinople named him among the holy Fathers whose writings on the true faith it followed." (SC 22849, 23054-23062, 23134-23139)
   - "The council in Trullo, in 692, received his letter to Letoius, bishop of Melitene, among the canons of the church." (SC 1602, 26715-26747, 43991)
   - X1 also applies, and `uncertain` names the editors twice ("The editors answer ...", "the editors doubt it"). Replace it with:
     - "Whether he hoped that all would at last be restored is still argued. Those who doubt it point to his sermons On the Poor, On the Beatitudes and Against Usurers, which speak of eternal punishment. Others answer that a sermon meant to stir its hearers weighs less than a careful dialogue." (NY 1525-1538)
     - "A later tradition says he married a woman named Theosebeia. Nicephorus Callistus first tells it, in the thirteenth century. It seems to rest on a letter of Gregory of Nazianzus that calls a Theosebeia a priest's yokefellow, and none of Gregory's own writings speaks of her as his wife." (NY 606-634, 641-643)
   - `written_about` should then add Theodoret (npnf203) and the Seven Ecumenical Councils volume (npnf214).

---

## Gregory of Nazianzus: REVISE (card only; the brief CLEARS)

Round-1 findings:
- R1-1 (Athens): resolved. Checked against NZ 22612-22615.
- R1-2 (translators as witnesses): resolved. The hazing story is told in Gregory's voice (NZ 41422-41433, "kindling spark of our union", unquoted and faithful). Sasima is told directly (NZ 22983-22997).
- R1-3 (archbishop and resignation): resolved. Checked against NZ 23163-23184.

Every claim in the brief was checked and holds:
- Arians in possession of the churches: NZ 23084-23086.
- The relative's house and Anastasia: NZ 23116-23119.
- The Five Orations and "the Theologian": NZ 23123-23124.
- Sabellian confusion against tritheistic division: NZ 23128-23130.
- Theodosius and Saint Sophia: NZ 23160-23162.
- Enthroned by the council, then Meletius's death and the presidency: NZ 23165-23168.
- The Egyptians: NZ 23171-23175.
- Ordination against his will and flight to Pontus: NZ 22844-22853.
- "a miserable little village ... almost by force", and his indignation: NZ 22983-22985.
- Ephesus and Chalcedon: NZ 23226-23227.
- Jerome's "my instructor in the Scriptures": NJ 41567-41568. That Jerome heard him preach is the editor's statement (NZ 23136-23138), but Jerome's own words in JW 11495-11500 bear it out ("My teacher, Gregory of Nazianzus ... 'I will tell you about it in church'").

The brief scores in band. It ends on his own voice. It clears.

1. **STANDARD: the card's legacy_traces are mostly not legacy, and one rests on a modern writer.**
   - "Nectarius ... was elected in his place" and "Gregory went home, saw Eulalius chosen ..." are life events.
   - "There, the introduction says, his only luxuries were a garden and a fountain" quotes a modern writer as a witness. The file says "says Mr. Crake" (NZ 23235).
   - "Rome had condemned Apollinarius in 377" happened before the letters it is meant to trace.

   Replace `legacy_traces` with:
   - "Rufinus put his works into Latin along with Basil's, as Gennadius reports, and called him that most eloquent man." (NJ 42464-42471)
   - "With Basil he gathered the Philocalia, a book of choice passages from Origen. About Easter in 382 he sent a copy to a friend as a book useful to students of literature." (CL 38; NZ 47436-47450)
   - "In 553 the emperor Justinian's letter to the council at Constantinople named Gregory the Theologian among the holy Fathers it followed." (SC 22849, 23054-23062, 23134-23137)

2. **STANDARD: the card restates the brief instead of continuing it (X1, plus the same problem in legacy_remembered).**
   - `legacy_remembered[0]` ("Honored as the Theologian, the name the Five Orations won him") repeats the brief. Replace it with: "Theodoret remembered him among the great teachers of the imperial city, as Gregory, shining friend and supporter of the truth." (NJ 36808-36810)
   - `legacy_remembered[1]` can carry Jerome's own scene on from the brief: "Jerome called him a most eloquent man and his instructor in the Scriptures, and counted thirty thousand lines of his writing. He remembered asking Gregory about a hard verse, and Gregory teasing that he would explain it in church, where the applause would force Jerome to understand." (NJ 41567-41569; JW 11495-11500)
   - Replace `uncertain` with: "Whether he ever took up Sasima is unclear. It seems he did not, with a rival bishop's troops holding the village and his father pleading with him to stay. His own letters pull two ways. In one he says he was appointed to Sasima, though for a short time he governed Nazianzus out of respect for his father. In another he says he was originally appointed to Nazianzus, "and not to Sasima as some would falsely persuade you"." (NZ 22992-22997, 46434-46437, 47707-47709)
   - `written_about` should then add the Jerome letters volume (npnf206) and npnf214.

---

## Verdicts

- Methodius of Olympus: REVISE. 1 blocking (minor), 3 standard.
- Ephrem the Syrian: REVISE. 3 standard.
- Gregory of Nyssa: REVISE. 1 blocking (card), 3 standard.
- Gregory of Nazianzus: brief CLEARS; card REVISE, 2 standard.
- All quotations MATCH. All four current drafts score in band, and so do the three proposed replacement briefs.
