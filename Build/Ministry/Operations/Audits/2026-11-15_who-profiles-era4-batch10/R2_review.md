# Round 2 review: era 4 Who batch 10

Three fresh Opus reviewers that had not seen the drafting or round 1, at full effort, on 2026-11-15. Round 2 rechecked every round 1 fix and read every brief in full, since all seven were tightened to 2:00 after round 1 (Tighten_2-00.md). Part A found 5 blocking and 9 minor points, Part B 3 and 15, Part C 4 and 11.

---

## Era 4 Who batch 10, round 2 review: PART A

**Scope.** `theophanes-the-confessor`, `stephen-the-younger`, `nikephoros-of-constantinople`: every brief in full as new text, the cards (diffed from 66ba54ee through 581b8e13; the tightening changed only `briefLength`), the audio scripts, each one's `records.json` entry, and the README sections on these three, with their census claims checked again against `cic-website/data/world-census.json` on origin/main.

**Method.** I reopened every cited range behind each brief sentence (`sed -n`), and read for who speaks and under what condition. I checked every quoted string in the three records entries by script, whitespace- and hyphen-tolerant: all are found. I walked the whole census JSON for "Theophan", "Nikephoros"/"Nicephor", "Stephen the Younger" and "Auxenti", and read each hit. I edited no repo file. Each replacement below was applied to a scratch copy and scored (`engine.m1.gates.grade_text`).

**Scores now.** Theophanes 328 words, FK 7.33, Flesch 70.15. Stephen 328, FK 7.30, Flesch 66.84. Nikephoros 330, FK 8.22, Flesch 62.19. No sentence runs past 24 words. Audio: all three equal their briefs with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. Pass.

**Scores with every fix below applied.** Theophanes 332, FK 7.49, Flesch 69.37. Stephen 333, FK 7.19, Flesch 67.05. Nikephoros 330, FK 8.48, Flesch 60.35. Audio scripts must be rebuilt after the brief edits.

### Round 1 points: were they fixed?

- **R1-B1 (Theophanes dates).** Fixed. Brief para 2 ("or to 744 by Theophanes's own figures") is true to Goar, THEOPH l.333: "ut ipse numerat, 744, ut melius alii 751 vel alii 752". Brief para 6 has 818 (Goar, l.345: "anno 5, Christi 818"; l.371) and about 820 (Bollandists, PG100 l.1641-1647: "circa annum 720, quo tempore Nicephorus in exsilio superat"). The record's corrected range l.1641-1647 is right. Card `dates`, `uncertain[3]` and `sources.about` agree.
- **R1-B2 (year tables).** Fixed. The "guesses" wording follows "me conjectore" (l.538). Henschen's words are at l.103990-103993.
- **R1-B3 (Nikephoros dates).** Fixed and still right after the tightening. The exile sentence now follows the night scene, all three placings kept. Card `dates` and `uncertain[1]` agree with THEO l.346-353, l.365, PG100 l.102222-102223, l.85132-85139.
- **R1-B4 (the steward Joseph).** Fixed. But see R2-B3 below: the motive the fix kept is one side of a contested claim.
- **R1-M1, M3, M4, M5, M6** (Theophanes). All applied and checked. "Tarasios" now matches the census.
- **R1-M7, M8, M10-M14** (Stephen). All applied. "blinded" fairly renders "effossi oculi" (PG100 l.95763-95764). "where Saint Pelagius's church had stood" follows "templum olim erat" (l.97179).
- **R1-M16, M17** (Nikephoros). Applied. Freese l.5401-5402 holds the quotation, as does the census edge.
- **R1-B5, B6, M18, M19, M21** (README). Applied. See R2-B4, R2-B5 for passages still missing or misdescribed.
- **Not taken.** R1-M2 was made moot by cutting Genesios: right. R1-M9 is moot now that the Stephen brief gives no death date: right. R1-M15: right to leave. "No council stood with them" is true to PG100 l.5462-5464 as far as it goes, and the added clause would cost five words. R1-M20 was superseded by the tightening: right.

### What the tightening did, checked

- **Theophanes.** The Nicaea donkey ride is cut, and the card's `place` keeps "Nicaea, in 787". "angry" is dropped, rightly: the Life says the father was vexed ("ægre tulit") and roused the emperor's anger, l.1248-1249. The merged birth sentence is right. One loss: see R2-B1.
- **Stephen.** All four death placings are cut, so no year is told as settled; the card keeps them. "After exile on the island of Proconnesus and the scene with the coin" keeps the Life's order (Proconnesus, Phiale, coin, Praetorium; PG100 l.95463-95465, l.95529-95540, l.95738-95742). "Constantine was then removing" is fair. The merged chroniclers' sentence is right on substance, but has lost the contrast that makes it a second side, and an article (R2-M2).
- **Nikephoros.** Ignatius's confession and the Holy Apostles burial are cut, and both stay on the card. "his disciple" still marks Ignatius as partisan. The sermon's author is now "Theophanes, a priest and abbot", which no longer tells him from the Confessor (R2-B2). "His Life" now opens a paragraph after a sentence about Leo (R2-M4).

---

## theophanes-the-confessor

**Verdict: one blocking point (R2-B1), one minor.** Every sentence was rechecked against its lines. The ice scene follows THEOPH l.78306-78327, including "quasi triginta ætatis ejusdem juvenes ludibundi ascendimus". The wedding night, the threat to blind him, the three years, Sigriane and Agros, the reply to Leo, the two years and twenty-three days, and the preface's George, "ex proprio penu nil depromentes" and "ex Domini charitate condonet" all hold.

**R2-B1. The Life's hostility to Leo is no longer marked anywhere in the brief (brief para 5).**
- Round 1's fix cut "The Life calls him the wickedest of men." to hold length. That was the brief's only sign that the Life is a partisan witness. Leo's offers, threats and the hero's answer are now told from the Life alone, unmarked. The rule asks for a partisan witness to be marked once. The Stephen brief marks its Life ("writes as a partisan of the images"). The card keeps the marker (`uncertain[4]`), but the brief has to carry it too.
- Source, THEOPH l.2079-2080: "Leonem, inquam, scelestissimum hominem, qui ab Armeniis et Assyriis genus ducens"; the record is claim 25.
- Fix, brief para 5: "The Life gives his answer to Leo's offers." → "The Life, which calls Leo the wickedest of men, gives Theophanes's answer." (+4 words; 12-word sentence. "Theophanes's" removes the "his" that could point at Leo. "to Leo's offers" goes, since "What I refused when young" already implies them.) Brief 332 words.

**R2-M1. "whose author and date are open" (brief para 3).** "Open" is unclear when heard aloud. The next sentence gives the rival names, so the point is a dispute. Fix: "whose author and date are open." → "whose author and date are disputed." (0 words.)

---

## stephen-the-younger

**Verdict: passes; one minor point.** I rechecked the coin dialogue against PG100 l.95535-95536 and l.95700-95726. Also rechecked: Callistus and the cupped hand (l.92804-92857), the 342 monks (l.95760-95765), and the eleven months (l.96041-96043). The feast-day cry, "Ego sum, quem quæritis", the ropes "inter catenas", Philomates's "ingens lignum" from the siphons, and the pit (l.96915-96984, l.97169-97181) hold too. So do the 42 years and disciples (l.88585-88588, l.88776-88785) and "Stephanum juniorem protomartyrem" (THEO l.78708-78709). The partisan marker and "of Constantinople" for both Stephen the Deacon and Nikephoros are in place.

**R2-M2. The chroniclers' charge no longer reads as a second side, and has lost an article (brief para 7).**
- Brief: "Theophanes the Confessor and Patriarch Nikephoros of Constantinople both say Stephen was accused of drawing people into monastic life."
- Records hold "Why he was killed" as contested: the Life against the two chroniclers. After the cut a listener hears two names but not that they give a different charge. The Life gives its own charge: the Praetorium "ut secundum leges judicium Subiret, eo quod imperatoris imaginem coulra leges conculcasset" (PG100 l.95740-95742, the scan). Theophanes: "quod plerosque ad monasticam vitam esset hortatus" (THEO l.78713-78714). Short History: "ad monasticum vitæ genus transſerrent" (PG100 l.81484-81488). "into monastic life" also drops the "the" the earlier text had.
- Fix: "Theophanes the Confessor and Patriarch Nikephoros of Constantinople both say Stephen was accused of drawing people into monastic life." → "Two chroniclers name another charge. Theophanes the Confessor and Patriarch Nikephoros of Constantinople say he was accused of drawing people into the monastic life." (+5; brief 333.)
- Records: add a claim "The Life: sent to the Praetorium \"ut secundum leges judicium Subiret, eo quod imperatoris imaginem coulra leges conculcasset\"", witness PG100 l.95739-95742, Documented.

---

## nikephoros-of-constantinople

**Verdict: two blocking points (R2-B2, R2-B3) and four minor.** The father (PG100 l.2143-2270) holds, and so does Nicaea (l.2685-2692). The 806 layman (l.3476-3531; Fabricius l.302-308) and Theodore's objection (THEO l.87157-87182) hold. So do the steward Joseph (THEO l.87800-87801; PG99 l.5639) and the break until 811 (PG99 l.5801-5816). The debate (l.5317-5539), the night exile (l.8500-8531), the Antirrheticus lines (l.17809-17821) and the nineteen years (l.11733-11736) all hold.

**R2-B2. "a sermon by Theophanes, a priest and abbot" does not tell him from the Confessor (brief para 8).**
- The Confessor is named in para 4. The Bollandists give the Confessor the very same titles, PG100 l.1641-1643: "Acta sancti Theophanis, presbyteri etiam et præpositi, imo et illustris scriptoris". They then say the sermon's author is another man, l.1647 and l.1656 (the scan sets the clause across two columns): "Aljus ergo hic noster Theo- … phanes est et aliquanto junior". Theophanes the Confessor was dead by 818 or about 820, so he could not have told of 847. A listener will take him for the chronicler. The rule: a name that could mean more than one person is told apart at first mention.
- Fix: "says a sermon by Theophanes, a priest and abbot," → "says a sermon by another Theophanes, a priest and abbot," (+1).

**R2-B3. Joseph's restoration: one side of a contested motive (brief para 4).**
- Brief: "A chronology printed with Theodore's works says Nikephoros agreed, fearing the emperor, and Theodore broke communion with him until 811."
- The records hold "Why Nikephoros accepted Joseph" as contested. The Sirmond chronology, PG99 l.5638-5645 (the scan reads "utennque"): "utcumque consentiente novo patriarcha … cum preterea timeret ne imperator quidpiam atrocius adversus Ecclesiam moliretur". Goar, THEO l.87283-87284 (cited in the records as l.87278-87282): "postquam ipse ut imperatoris gratiam iniret ad pristina eum munia instauraverat". The brief gives the chronology's reason with its source, and leaves out Goar's. Telling both would cost about 9 words in a brief at 330. The motive is not the story's point, and the card's `uncertain[4]` gives both sides, so the clean fix is to drop it.
- Fix: "says Nikephoros agreed, fearing the emperor, and Theodore" → "says Nikephoros agreed, and Theodore" (−3). "agreed" is the chronology's "consentiente". Without the motive, the brief tells no contested point here.

**R2-M3. "he seemed to be putting his hand into thorns and thistles" (brief para 1).** The Latin is the patriarch's own feeling, PG100 l.4612 and l.4651-4653: "Videbatur enim sibi vir sanctus … quasi in spinas et tribulos manum injicere". "He seemed" can be heard as how he looked to others. Fix: "he seemed to be putting his hand into thorns and thistles." → "it felt like putting his hand into thorns and thistles." (−1.)

**R2-M4. "His Life" (brief para 2).** The sentence before ends on Leo's head, so "His" can be heard as Leo's. The tightening changed "Nikephoros's Life" to "His Life". Fix: "His Life is by his disciple" → "Nikephoros's Life is by his disciple" (0).

**R2-M5. "Ignatius writes, he told Nikephoros" (brief para 5).** When heard, "he" falls nearest Ignatius. The speaker is Leo (PG100 l.5317-5374). Fix: "Ignatius writes, he told Nikephoros" → "Ignatius writes, the emperor told Nikephoros" (+1).

**R2-M6. First mention (brief para 1).** "Patriarch Nikephoros" stands alone at first mention. Leo IV, the emperor Nikephoros I and a Theophanes pair follow, and the Stephen brief already says "Patriarch Nikephoros of Constantinople". The card name is "Nikephoros of Constantinople". Fix: "Patriarch Nikephoros crowned him" → "Patriarch Nikephoros of Constantinople crowned him" (+2). With R2-B2 through R2-M6 the brief runs 330 words, FK 8.48, Flesch 60.35. That clears the floor of 60, but only just. If R2-M6 is not taken, Flesch is 61.

---

## README

**R2-B4. Stephen bullet: "The coin, the 342 monks and the pit agree." The coin does not.**
- Census, `iconophile-byzantine-monasticism` `documentedStories[0].text`: "Brought before the emperor, Stephen was told that the honor paid to an icon was idolatry. He asked for a coin. … And if he threw it down and stamped on it, would he be punished for insulting metal or for insulting the emperor?"
- The Life gets the coin before he is brought in, PG100 l.95535-95536: "a pio aliquo viro nummum petiit et accepit, quem quidem intra cucullam gestabat". He asks only whether he would be punished, l.95704 and l.95722: "Num si illud humi projiciam et sponte conculcabo, pœnas luam?" No held line has "metal".
- Fix: "The coin, the 342 monks and the pit agree." → "The 342 monks and the pit agree. The coin differs: the Life has him get it from a devout man before he is brought in (PG100 l.95535-95536), not ask for it before the emperor, and he asks only whether he would be punished (l.95704, l.95722), not whether "for insulting metal or for insulting the emperor"."

**R2-B5. Nikephoros bullet: one live passage naming him is missing.**
- Census, `john-climacus` `card.uncertain[1]`: "From Peter's years in Theophanes, Evagrius and Nicephorus, he reckons that if the tale is true John died between 560 and 565." The held notice behind it names our Nikephoros: PG88 (`dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt`) l.41478-41479: "Nicephorus Coust. annos duntaxat 20 Petro tribuit". The scan's "Coust." is "Const.", Nikephoros of Constantinople's chronography. The README bullet lists only `voices[4]` and the edge.
- Fix, after "The edge spells him "Nicephorus", which is on the card." add: "The John Climacus card (`uncertain[1]`) also names him as "Nicephorus", one of three writers whose years for Peter of Jerusalem Philippe Labbe uses; the held notice gives the 20 years (PG88 l.41478-41479, the scan reads "Nicephorus Coust."). It says nothing of his life, and agrees."

**R2-M7. Theophanes bullet: the Paulicians story is not listed.** Census, `paulicians` `documentedStories[0].text`: "The continuator of Theophanes, writing the official history of the dynasty a century later". It is the same kind of mention as Photius's, which the bullet lists. Fix: "Photius's entry names "the chronicle that continues Theophanes"." → "Photius's entry names "the chronicle that continues Theophanes", and the Paulicians story "the continuator of Theophanes"."

**R2-M8. Nikephoros correction: "The brief and card give each placing by name."** Since the tightening, the brief leaves the crowning undated ("When Leo the Armenian took the throne"). Fix: "The brief and card give each placing by name." → "The card gives each placing by name. The brief gives those for the exile and the death, and leaves the crowning undated."

**R2-M9. "Majors and lengths": "The seven now run 326 to 330 words".** This is true now (Ilarion and Peter 326, Keroularios 327, Nicholas, Stephen and Theophanes 328, Nikephoros 330). With R2-B1 and R2-M2, Theophanes runs 332 and Stephen 333. Fix after the fixes: "326 to 330 words" → "326 to 333 words". This is still about 2:00, and no exception line is needed.

**Checked and correct in the README (these three).** The tradition names, "Iconophile Byzantine Monasticism (726 to 843)" and "The Byzantine Imperial Church (Heraclian & Iconoclast Eras)", match the census. The Tarasios and Methodios voices are as quoted. The Stephen bullet's 765 passages (`why`, `longDescription`, `voices[1]`), the Mese, the palace-faction mob, "c. 809", AM 6257 and Auzépy are all as the census has them. The Theophanes bullet's placing lines ("writing in the early ninth century"; "writing for Chalcedon's side") are in the census. The re-score corrections ("a deacon among the monks who knew him"; l.14713; "about 758") are right against the lines. "Patriarch Nikephoros I" is on the card, as the names section says.

---

**Verdict: Part A does not pass round 2 as it stands. Every fix above is exact and fits the length. Counts: 5 blocking (R2-B1 to R2-B5), 9 minor (R2-M1 to R2-M9).**

---

## R2 review, part B: Nicholas Mystikos, Peter of Sicily, Michael Keroularios (era 4 batch 10)

Reviewer: fresh, full effort, round 2 scope. Branch `claude/cft-who-era4-batch10`. Files: the three briefs, cards, audio scripts and `records.json` entries; the README passages on these three; agreement with `era4/batch4/humbert-of-silva-candida.*`.

## How I checked

- Every brief was read in full as new text, sentence by sentence, against its source lines (Letter 32, PG111 l.13775-14460; Mai and Henschen, PG111 l.455-672; de Boor l.4625-4629, l.5618-5621, l.6030-6062, l.6470-6500, l.8326-8350, l.8638-8662, l.8774-8782, l.9272-9284; PG109 l.33512-33548; Mansi l.93958-94000, l.103460-103468; Peter/Gieseler l.145-222, l.596-625, l.700-745, l.778-850, l.955-962, l.1316-1326, l.3822-3860; Rački l.1-3, l.855-867; Psellos/Sathas l.3790-3802, l.4008-4037, l.18036-18054, l.21156-21195, l.22665-22690, l.23815-23835, l.23988-24004; Will l.14776-14784, l.14868-14880, l.15030-15048, l.17210-17242, l.17808-17818, l.18072-18086).
- Every round 1 point was checked in the files (results below). `git diff 3e1ec684 HEAD` shows that the tightening changed only the briefs, the audio and each card's `briefLength`. `records.json` is unchanged since the round 1 fixes, so the round 1 script check of its quotes still holds.
- Audio: all three equal their briefs plus `[calmly] ` at line 1 and `[warmly] ` at the start of the last paragraph. Pass.
- Words and readability now: Nicholas 328, FK 7.13, FRE 69.03. Peter 326, FK 7.05, FRE 65.73. Keroularios 327, FK 6.77, FRE 69.57. No sentence runs past 23 words. With every replacement below applied together by script: Nicholas 328 (FK 7.17, FRE 68.85), Peter 330 (FK 7.14, FRE 65.34), Keroularios 329 (FK 6.84, FRE 69.21). All stay inside the README's "326 to 330". No new sentence runs past 24 words.
- Census: I re-read `cic-website/data/world-census.json` on origin/main for every mention of the three men (movements 75, 79, 102, 320, 617, 618; edges 15, 235, 242, 243).

---

## Nicholas Mystikos

Round 1 fixes: R1-B1, B2, B3, B5, M1, M2, M3, M5 are in place and right as new text. On R1-B5 the worker was right not to take my sentence: the Mansi note doubts Eutychius on the second synod (MANSI l.93994-93998), not on the eastern legates as such. The added "De Boor names Mansi's collection among those that doubted their presence" matches de Boor's note "So von Mansi Coll. conc. XVIII, 242" (DEBOOR l.8646-8656). On R1-M2, the README's new citation is right: "dem Tode der Zoe, der zweiten Gemahlin" (DEBOOR l.4627-4628) and "seiner gleichfalls Zoe genannten vierten Gemahlin" (l.5620). On R1-B4, the worker's "its author" in place of my "Leo" created a new ambiguity (R2-M2).

Tightening: the new sentences were checked against their sources. "Armed guards stood over him in the winter cold" ("Hiemis rigorem ... custodum violentiam? Enses enim et arcus et clypei ... circumdederunt", PG111 l.14403-14406). "The bishops, Nicholas writes, would baptize the boy only if Leo sent Zoe away. Leo swore he had." (l.13991-14001). "Honored as empress" ("quo regis uxorem induci fas est honore", l.14002-14003). The plea ("advocentur veteris Romae aliarumque pontificalium sedium praesules", l.14174-14176). The chronicle's ban ("Eo facinore patriarcha ecclesiae ingressu Leoni interdixit", PG109 l.33534-33536). The close (l.14028-14029, l.14093-14097). All pass. The Thomas sentence now stands three paragraphs from "Nicholas says Leo crowned her himself", but both are attributed and the card's "Who blessed the marriage" sets them side by side, so I accept the move.

**R2-B1. Brief paragraph 7, "The banquet followed on 1 February 907.": a disputed year given with one placing.** This is the year round 1 took out of `knownFor` (R1-B1), because three held placings disagree. De Boor: "ist der Sturz des Nicolaus auf den 1. Februar 907 zu datiren" (DEBOOR l.6030-6031). He reports Krug and Muralt for 908 (l.5798-5799). Mai: "post novennium (aut post annos XI, ut dicitur apud Leunclavium ...) ... sede pulsus est" (PG111 l.663-664). The paragraph opens "By de Boor's reading of the Life", but the banquet sentence stands on its own and gives only his year. The day is not disputed: the chronicles have "prima Februarii" (PG109 l.33541), and de Boor's sequence of 906 refusals already places it. Replacement (6 words, −1): `The banquet followed on 1 February.` The card's `dates` and "The dates" item already carry all three placings.

**R2-M1. Brief paragraph 8, "When Leo died, Nicholas returned and helped rule for the boy Constantine.": two reigns run together.** Nicholas became a guardian only when Alexander, dying, named him: "Alexander imperator mori se praevidens, Nicolao patriarcha, et Stephano Magistro ... procuratoribus institutis, Constantino Leonis filio reliquit imperium" (Henschen quoting Leo the Grammarian, PG111 l.471-525). Heard as written, he rules for the boy from Leo's death in 912. The card's `role` has it right. Replacement (+1): `When Leo died, Nicholas returned and later helped rule for the boy Constantine.`

**R2-M2. Card `uncertain`, "The chronicles": "says the note shows its author lived close to the times he wrote of".** The nearest noun is "the note", so "its author" reads as the note's writer. Combefis means the chronicler: "Fuisse eum supparem illis quorum res gestas prosecutus est, ipsa subscriptio clare indicat" (PG108 l.93203-93205). Replacement for the clause: `and says the note shows the chronicler lived close to the times he wrote of.` (Same length. It avoids naming Leo, the worker's reason for not taking "Leo".)

**R2-M3. Card `uncertain`, "When the legates came": "Nicholas speaks only of Rome".** The brief tells, from Letter 32, that he asked for "Rome and the other great sees" to judge (PG111 l.14174-14176). De Boor's point is narrower: Nicholas reports proposing the other patriarchs, "verschweigt aber wohlweislich, dass dies geschehen sei" (DEBOOR l.8640-8645). As written, the card contradicts the brief. Replacement for that clause: `Nicholas tells only of Rome's legates coming;`

---

## Peter of Sicily

Round 1 fixes: R1-B6, B7, M6, M7, M9, M10, M12 are in place and right. R1-M8's brief sentence was cut by the tightening; the card keeps "Paulicians he talked with". On R1-M11 the worker was right to give Gieseler's whole window, "Petrus scripsit intra annos 869 et 974" (PETER l.219). The wording now crosses the scan rule, though (R2-M8).

Tightening: "boast of sending some of their own" ("garrientes, se ex suis missuros esse in loca Bulgariae", l.797-798) passes. So do "that they curse Mani" (l.959-961; Greek ἀναθεματίζουσι, l.931) and the cut of "at the start of his reign", which the card's `dates` keeps (l.787-788). Two changed sentences now have unclear reference (R2-B2, R2-M4).

**R2-B2. Brief paragraph 6, "Gieseler says Peter is mistaken that they are the same.": "the same" has no referent.** The sentence before is "Peter himself reports that they curse Mani". A listener hears "the same" as the same as Mani, or as nothing. Manichaeans were last named two paragraphs back. This is the profile's main contested point, and as heard it is not stated. Gieseler: "Petrum falli, qui Paulicianos cum Manichaeis re vera eosdem esse contendat" (PETER l.3878-3881). Replacement (9 words, −1): `Gieseler says Peter is wrong to call them Manichaeans.`

**R2-M4. Brief paragraph 2, "He stayed nine months, and the exchange came in Basil's second year.": the pronoun and the verb.** The tightening turned "Peter stayed" into "He stayed" straight after "the emperor Basil I sent him", so the nearest man is Basil. "The exchange came" is also an odd verb for "quod et peractum est secundo anno imperii Basilii" (PETER l.3826-3828). Replacement (+1): `Peter stayed nine months, and the exchange was made in Basil's second year.`

**R2-M5. Brief paragraph 1, "Counting on the new preaching there": open to the wrong reading.** Heard aloud, it can mean they relied on the preaching to help them. Peter says they hoped to gain from its having only just begun: "sperantes eo se adjutum iri, quod divina praedicatio ibi initium modo ceperit" (PETER l.835-836). Replacement (+1): `Since preaching there had only just begun, Peter writes, they thought they could sow their weeds among the hidden wheat.`

**R2-M6. Brief paragraph 2: "He says that is all we know of Peter for certain" now comes before the book.** Gieseler's "Haec omnia sunt, quae de scriptore hujus libelli certo scimus" (PETER l.182) closes a passage on the embassy, its date, the emperor's order and the writing between 868 and 871 (l.148-164). After the tightening merge, "that" covers only the embassy and its year. Then the next paragraph adds the book. Move the sentence to the end of paragraph 3 (0 words), so paragraph 2 ends `... dates the embassy to 868.` and paragraph 3 ends `Gieseler places the writing between 868 and 871. He says that is all we know of Peter for certain.` ("He" is then Gieseler, the subject just before.)

**R2-M7. Brief paragraph 8 and card `legacy.traces[1]`: "Franjo Rački, writing in Zagreb in 1869".** The file header says the paper was "read to the Academy on 28 November 1868" and printed in Rad VII, catalogued 1869 (RACKI l.1-3). It was written by 1868. Brief replacement (+2): `Franjo Rački, in a study printed in Zagreb in 1869, did not know how far the Paulicians carried out the plan.` Card: `Franjo Rački, in a study printed in Zagreb in 1869, used Peter's report of the plan for Bulgaria in tracing how the Paulicians' teaching reached Bulgaria.`

**R2-M8. Card `uncertain`, "The unnamed archbishop": "The scan prints the second year as 974, a slip for 871."** Only the OCR is held, so the rule is "the scan reads". Whether 974 is the editor's slip or an OCR misreading cannot be told from the file. Replacement: `The scan reads the second year as 974, which must be 871.`

---

## Michael Keroularios

Round 1 fixes: R1-B8, B9, M13, M14, M15, M16, M17, M18 are in place and right as new text. On R1-B10 the worker's heading, "Whether he talked with the envoys", was right and mine was wrong: Psellos has them clash with him (PSELL l.22706-22721). The worker's "Euthymios, a bishop there not long before Psellos's own day" (R1-M16) matches "οὐ πόρρω πολὺ τῆς καθ᾽ ἡμᾶς γενεᾶς" (l.23874-23875) better than my wording did.

Tightening: the cuts of the brother, the seal, "he adds", "being", "own", "once" and "that" leave each sentence true to its source. I checked "led away in disgrace, pulled about and mocked" (l.23636-23663); "Isaac held his anger, then suddenly sent him out of the city" ("ἀφῆκεν ἐπισχὼν αὐτῷ τὸν θυμὸν ... ἀπροσδοκήτως ... ἐξάγει τε τῆς πόλεως", l.18042-18045); and "to teach and persuade us to hold their teachings" ("ut docerent ac nobis persuaderent, ut teneremus ipsorum dogmata", WILL l.17813-17815). "They walked into the palace with a cross and staffs ... and would not greet him or bow" joins two moments in Letter I: the discourtesy when they came to him (l.17215-17220) and the entry "cum cruce et baculis intra regiam" (l.17229-17230). Nothing is false, so I let it stand.

**R2-M9. Brief paragraph 8, "Psellos says he was brought from the island of Imbros for trial in Thrace.": the work is not named, and the paragraph before names the history.** Paragraph 7 opens "Psellos's history says". A listener carries that into paragraph 8. But the death on the way to trial is the funeral speech (PSELL l.23818-23870, l.23990-24003). The history says something else: "ὅροις κολάζει περιγραπτοῖς, ἐφ᾽ οἷς δὴ καὶ ἀπέθετο τὴν ζωήν" (l.18045-18046), which the card's "His death" item tells. Replacement (+1): `Psellos's speech says he was brought from the island of Imbros for trial in Thrace.`

**R2-M10. Brief paragraph 6, "The hostile sentence curses Michael and his followers.": the condition is cut.** The curse ends "sint anathema Maranatha ... nisi forte resipuerint" (WILL l.15036-15046). The records (claim 4) and Humbert's brief ("unless they repent") both carry it. Replacement (+3): `The hostile sentence curses Michael and his followers unless they repent.`

**R2-M11. Brief paragraph 2, "Konstantinos Sathas, its editor in 1874": "its" has no near antecedent.** "A funeral speech" is two sentences back, and "the emperor" comes between. Replacement (0 net, "also" dropped): `Konstantinos Sathas, the speech's editor in 1874, says Psellos was forced to write the charge against him.` Offset for R2-M9 and R2-M10 (−1), paragraph 5: `His letters to Peter, patriarch of Antioch, tell of Rome's envoys.` (WILL l.17210-17242 is Letter I's account of the envoys.) With R2-M9, M10 and M11 the brief comes to 329.

**R2-M12. Card `keyWorks[1].about`: "It says he would not meet the envoys".** After R1-B10 the card's own item says they came before him and handed him their letter (WILL l.17236-17237). Letter II says "colloquium congressionemque detrectavimus" (l.18076), talk and conference. Replacement for the clause: `It says he declined to talk or meet with the envoys,`

**R2-M13. Records: two claims now support nothing in the brief or the card.** Claim 9 (the brother's death, PSELL l.21283-21317) and the seal half of claim 12 ("ipsummet invenit adulteratum", WILL l.17239-17240) left the brief in the tightening. Neither is on the card. The tightening log suggested tagging them. Append ` (records only; cut from the brief at the 2:00 tightening)` to claim 9's text, and the same after the seal quote in claim 12. The other way is to drop them.

**Humbert agreement.** Rechecked against `batch4/humbert-of-silva-candida.brief.txt` and `.card.json`. They agree on the three envoys with Humbert first, the July altar scene, the curse, Argyrus, 20 July by Will's reading, and the two letters. With R2-M10, both briefs carry "unless they repent". The three differences the README names are real, and the README states them correctly (l.70). Nothing new.

---

## README (sections on these three)

**R2-B3. "Live census mentions", Nicholas: "The rest agrees." It does not.** The story "The Emperor Turned Away at the Door on Christmas Day" (movement `byzantine-imperial-church-macedonian`) has three more points that the held lines, and this profile's own records, treat as disputed:
1. Its source line gives Letter 32 as "to Pope Anastasius III". Mai: "vel sub Landone pontifice, ut putat Baronius, vel sub Anastasio tertio, ut censet Pagius" (PG111 l.862-865; records contested claim "The pope Letter 32 addresses").
2. Its text says Leo appealed to "Rome and the eastern patriarchs, all of whom allowed a dispensation". The eastern half is contested in the records: de Boor holds the legates came (DEBOOR l.8640-8684), and he names Mansi among those who doubted it (l.8646-8656).
3. Its caveat calls it "the council of 920", and its source gives "Tomos of Union (920)". Mansi prints the year of the world 6428 (MANSI l.103464-103467), but de Boor puts the agreement in 921 (DEBOOR l.4693-4694). The card's first `traces` item gives both.

The bullet's exile sentence also leaves out Mai's placing, which the card carries.

Replace `The census's February 907 is de Boor's; he reports Krug and Muralt for 908 (DEBOOR l.5795-5802). The rest agrees.` with:

`The census's February 907 is de Boor's; he reports Krug and Muralt for 908 (DEBOOR l.5795-5802), and Mai puts the exile nine years after the election of 895, or eleven by Leunclavius (PG111 l.662-664). Its source line names the pope of Letter 32 as Anastasius III; Mai reports Baronius for Lando and Pagi for Anastasius III (PG111 l.862-865). It says the eastern patriarchs allowed a dispensation; de Boor holds that their legates came, and names Mansi among those who doubted it (DEBOOR l.8640-8656). It dates the council to 920; Mansi prints the year of the world 6428 (MANSI l.103464-103467), and de Boor puts the agreement in 921 (DEBOOR l.4693-4694). The rest agrees.`

**R2-M14. "Corrections to the re-score", Keroularios: the death dispute leaves out Psellos's history.** "Psellos has him die on the way to trial in Thrace, Sathas before the court." Round 1 (R1-M17) added the history's third placing to the card ("ἐφ᾽ οἷς δὴ καὶ ἀπέθετο τὴν ζωήν", PSELL l.18045-18046). Replacement: `The death needs the dispute: Psellos's speech has him die on the way to trial in Thrace, his history within the bounds of his exile, and Sathas before the court.`

**R2-M15. "Majors and lengths": the Decision-Log entry it cites is not there.** It cites (Decision-Log, "Who profile length: 2:00 restated, longer only when earned", 2026-11-15). No entry of that name, and no "restated", is in `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md` on this branch or on origin/main. The phrase appears only in commit 581b8e13's message. This affects the whole README, not only Part B. Either the coordinator writes the entry, or the citation becomes `(Mark, 2026-11-15, relayed by the coordinator; the Decision-Log entry is to be written)`.

**Checked and correct:**
- The Keroularios census list: movements 79, 102, 320, 617 and 618, edges 15 and 235. "Three entries and both links spell him 'Michael Cerularius'" is right (102, 320, 617 and edges 15, 235).
- The Peter bullet: movement 75's source note with "adoptionism"; edge 243's "around 870"; edge 242, which agrees.
- The Nicholas bullet's existing points (palace priest, procession and door, Letter 117, the law against a third marriage).
- The length line: the seven briefs run 326 to 330, so "326 to 330 words, about 2:00 each" is true, and it stays true with the replacements above.
- "Who the sources are" and the Humbert note for these three.
- Open-Gaps still has no "Era 4 Who batch 10" entry, as the README's "will be logged" allows. It must exist before approval.

---

## Verdict

Not yet approved to proceed. All fixes are wording or citation changes against lines already read; no new research is needed. Counts: 3 blocking (R2-B1 to R2-B3), 15 minor (R2-M1 to R2-M15).

---

## R2, Part C: ilarion-of-kyiv and README.md (era 4 batch 10)

Reviewer: fresh Opus, full effort, 2026-11-15. Branch `claude/cft-who-era4-batch10`. No repo file edited.

Checks run:
- Lengths (len(text.split())): Ilarion 326, Keroularios 327, Nicholas 328, Nikephoros 330, Peter 326, Stephen 328, Theophanes 328. The README's "326 to 330 words" is right. Every card's `briefLength` reads "about 2 minutes".
- `grade_text` on the Ilarion brief: FK 6.91, Flesch 66.68. Pass.
- Audio equals brief plus `[calmly] ` and `[warmly] `, by script, all seven ids. Pass.
- No narrator sentence in the Ilarion brief runs past 25 words.
- Every quoted string in the Ilarion records, claims and contested sides, checked by script against CROSS, PSRL1, GORSKII, MOUR, PAT and both Susza files, whitespace-tolerant with hyphen breaks joined. All match. The script's only "misses" were apostrophes read as quote marks.
- `git diff 66ba54ee` on the Ilarion card. Every changed field reread against its source.
- Census: `git show origin/main:cic-website/data/world-census.json` (release 43, 2026-11-14), read by script. It is byte-identical to the scratchpad copy. Every passage naming the seven men was pulled and compared with the README bullets.
- Each card's source list compared by script with the files its records cite (finding R2-B1).

### Round 1 Part C points: were they fixed?

| R1 point | State now | Right as new text? |
|---|---|---|
| B1 George by 1072 | Applied in the brief ¶3, card `dates`, records | Yes. CROSS l.12488-12491 reads "6580 (1072) ... the Metropolitan George". |
| B2 death clause | Applied in the brief, card `dates`, `uncertain[0]`, `uncertain[6]`, records, README | Yes. The quote is verbatim at CROSS l.5192-5193. "Later versions" for "later redactions" is fair. |
| M1 Antony | "Later Antony of the Caves came home from Mount Athos and settled by Ilarion's cave." | Yes. Not taking "Soon after" was **right**: CROSS l.11755's "Not many days afterward" opens the layman's journey, not his return. |
| M2 "by the Dnieper" | Applied in the brief and card `place` | Yes (CROSS l.11749 "toward the Dnieper"). |
| M3 ¶4 | Applied; the tightening made it "the edition's foreword notes" | Yes (GORSKII l.796-800). See R2-M2 on "It holds". |
| M4, M5 | M4 applied; M5's sentence was cut by the tightening and kept on the card (`uncertain[4]`) | Yes. |
| M6 consecration witnesses | Susza/Smotrytsky added to card and records; 1826 dissertation added to records | The text is right (SUSZA1864 l.4460, l.4485-4489; SUSZA1666 l.5698-5702). But the card's source list was not updated (R2-B1). Not taking Platon was **right**: Blackmore's note "P. 35, 21" glosses "the canonical dependence of our hierarchy²¹" at Clement's election (MOUR l.2053, l.16339-16344), not Ilarion's. |
| M7 "native" | Applied to the records note and card `uncertain[4]` | The text is right, but "Clement" now has no identifier (R2-B3). |
| M8 Chronicle authorship | Applied | The Cross sentence is right (CROSS l.4819-4822). The Paterik sentence is wrong (R2-B2). |
| M9 role | Applied | Yes. |
| M10 batch 9 | Left as a note | Right. See the note at the end, which adds a new point. |
| M11, M12 | Applied | Yes; all quotes match. |
| B3 census bullet | Applied | Yes, checked against release 43 (see README below). |
| M13-M15, M17, M19, M20 | Applied | Yes, except one gap in M13's Theophanes list (R2-M6). Not taking M20's l.16005 was **right**: "sat till 1058" is at MOUR l.16006. |
| M16 approval line | Left for the worker. The README still says "The coordinator approved this (2026-11-15)". | Still not logged (R2-M8). |
| M18 lengths | Superseded by the tightening and rewritten | The rewrite cites a Decision-Log entry that does not exist (R2-B4). |

---

## ilarion-of-kyiv

### The brief, read in full as new text

The brief holds up against its sources. I checked each sentence:
- **¶1.** CROSS l.11744-11753 and PSRL1 l.6898-6907; the quote is verbatim at CROSS l.11747-11748.
- **¶2.** CROSS l.11741-11742; for Antony, l.11755-11782.
- **¶3.** GORSKII l.741-759; CROSS l.12488-12491.
- **¶4.** GORSKII l.796-800; MOUR l.1489-1501; MOUR header l.1-2; CROSS l.11706-11707.
- **¶5.** GORSKII l.2605-2611, and l.181, where the year 6559 (1051) stands in the Slavonic signature itself.
- **¶6.** GORSKII l.146-157 and l.686-716.
- **¶7.** GORSKII l.1225-1230, l.1335-1337 and l.1854-1860.
- **¶8.** GORSKII l.2239-2262; for "George", l.134-135.

The tightening cut nothing a disputed point needed. The authorship of the Sermon is still told as the foreword's argument. Both sides of the consecration question still stand in ¶4. The thin life is still flagged in ¶3. Mouravieff is still placed as a Russian official.

The two cuts are safe. The Rusin sentence is on the card at `uncertain[4]`. The Irina dating is on the card at `uncertain[2]` and in `dates`.

Two small writing points remain (R2-M1, R2-M2).

### R2-B1. Susza is named on the card but missing from its Sources (card `sources.about`)

Round 1's M6 fix added Jacob Susza and Meletius Smotrytsky to `uncertain[3]`. It also added two records claims that cite `susza_saulus-et-paulus-ruthenae-unionis-lat_martynov1864.txt` and `susza_saulus-et-paulus-lat_rome1666.txt`. Neither file is in the card's `sources`.

I checked all seven cards by script. Ilarion's is the only card whose records cite a file its Sources do not list. A reader has no way to reach the witness the card names.

Append to `sources.about`, after the Paterik entry:
```json
{
  "title": "Saulus et Paulus Ruthenae unionis sanguine Beati Iosaphat transformatus, sive Meletius Smotriscius",
  "author": "Jacob Susza, bishop of Chełm and Belz, in union with Rome",
  "date": "1666",
  "language": "Latin",
  "file": "cic/texts/susza_saulus-et-paulus-lat_rome1666.txt"
},
{
  "title": "Saulus et Paulus Ruthenae unionis sanguine B. Josaphat transformatus, sive Meletius Smotriscius (new edition, ed. Joannes Martinov)",
  "author": "Jacob Susza; Joannes Martinov (ed.)",
  "date": "1864",
  "language": "Latin",
  "file": "cic/texts/susza_saulus-et-paulus-ruthenae-unionis-lat_martynov1864.txt"
}
```
The titles, authors and dates are from each file's header (l.1-4). The 1864 header gives "Bishop of Chelm and Belz in communion with the Roman Church". The 1666 header gives "Bishop of Chelm and Belz, united with the Roman Church".

### R2-B2. "The Caves Paterik's account of the founding tells the same story" is wrong (card `uncertain[7]`; also `uncertain[5]`; records)

This sentence came in with round 1's M8. The Paterik's founding account does not tell the Chronicle's story. It tells an earlier stay of Antony's in Kyiv, before Ilarion's cave:
- PAT l.1088-1092: "Антоше же отьиде въ Рус. И иршде въ градъ, Киевь ... И ‘на Брестовое * приде: и’ обрете печеру и вселисл в ню, юже 0Ъ." ископали варязи,— и в нЪй пребысть въ. велицемъ въздержани." (Antony went to Rus and came to Kyiv. He came to Berestovoye, found a cave the Varangians had dug, and settled in it.)
- PAT l.1094-1097: after Vladimir's death, "Святополкъ ... нача избивали братёо свою; уби святого Бориса: и ГлЪба. АнтоШ же видЪ таковое кровопролише ... пакы бЪжа въ святую гору." (Sviatopolk began to kill his brothers. Antony saw the bloodshed and fled back to the Holy Mountain.)
- Only then does it give the Ilarion passage (PAT l.1098-1106), and Antony's return to "the hill where Ilarion had dug the cave" (l.1110-1111).

So in the Paterik, Antony was at Berestovoye before Ilarion dug his cave. This bears directly on `uncertain[5]`, "Who made him a monk": Simon's letter, in the same Paterik, says Antony tonsured Ilarion. As it stands, `uncertain[5]` gives only the Chronicle's order ("the Chronicle has Ilarion dig the cave before Antony came"). The held witness that puts Antony there first is left out, so the card reads as more settled against Simon than the sources are.

The brief is unaffected. Its "Later Antony of the Caves came home from Mount Athos and settled by Ilarion's cave" follows the Chronicle, and the Paterik agrees on the return.

Card `uncertain[7]`. Replace "The Caves Paterik's account of the founding tells the same story." with:
> The Caves Paterik's account of the founding repeats the passage on Ilarion's cave.

Card `uncertain[5]`. Replace "That Life is not among the sources used here, and the Chronicle has Ilarion dig the cave before Antony came." with:
> That Life is not among the sources used here. The Chronicle has Ilarion dig the cave before Antony came. The Caves Paterik's founding account has Antony in Kyiv once before. He lived at Berestovoye in a cave that Varangians had dug, and fled back to Athos when Sviatopolk began killing his brothers.

Word counts: 10, 10, 11 and 23. All are under 25. "Began killing" renders "нача избивали". "Fled back" renders "пакы бѣжа".

Records:
- Add a claim, Documented. Claim: "The Paterik: before Ilarion's cave, Antony came to Kyiv and to Berestovoye and settled in a cave 'юже 0Ъ." ископали варязи'; after Vladimir's death, seeing Sviatopolk's bloodshed, he 'пакы бЪжа въ святую гору'". Witness: "PAT (kievan-caves-paterik_paterik-kievskago-pecherskago-monastyria-chu_abramovich1911.txt) l.1088-1092, l.1094-1097".
- In the claim citing "PAT ... l.1096-1106", change the range to l.1098-1106. The Ilarion passage starts at l.1098 ("Бого || любивому князю Ярославу"). l.1096-1097 is Sviatopolk and Antony's flight.
- In the contested claim "Who made him a monk", add the side:
  > Caves Paterik: Antony lived at Berestovoye in a Varangian cave before Ilarion dug his, then fled to Athos (PAT l.1088-1097)

The README's census bullet also gains from this (R2-M9).

### R2-B3. "Clement" has no identifier (card `uncertain[4]`)

The sentence "A. N. Mouravieff calls him and Clement the native Russian metropolitans." came in with round 1's M7. "Clement" alone could mean Clement of Rome, of Alexandria or of Ohrid. Clement of Ohrid is a batch 9 Who, so the clash is real on this very map.

The rule is an identifier at first mention in the card. Mouravieff gives one: "Clement a monk of Smolensk" (MOUR l.2064).

Replace with:
> A. N. Mouravieff calls him and Clement of Smolensk, a later metropolitan, the native Russian metropolitans.

That is 16 words. "A later metropolitan" rests on MOUR l.2036-2068: Clement is chosen after the death of Metropolitan Michael, under Isyaslav, a successor of Vsevolod son of Oleg. No year is given, because the held margin date at l.2065 is garbled.

The records note in `absent_details` "'First native-born metropolitan'" also says "Hilarion and Clement". Make it "Hilarion and Clement of Smolensk".

### R2-M1. "All that is known" has lost its object (brief ¶3)

GORSKII l.759 reads "Вотъ все, чтб известно 0бъ Шлар!онз": this is all that is known about Ilarion. The R1 fix dropped "on him", so a listener hears "all that is known" with no object.

Replace "The 1844 Moscow edition of his works quotes the Chronicle's two passages and says this is all that is known." with:
> The 1844 Moscow edition of his works quotes the Chronicle's two passages and says this is all that is known of him.

That is +2 words.

### R2-M2. "It holds" can point back at the chronicler (brief ¶4)

The sentence before has "The chronicler" as its subject, and "the edition's foreword notes" comes in as a tag. Heard aloud, "It" is not sure to mean the foreword.

Replace "It holds that Yaroslav did not mean to cut the Kyiv church's tie to Constantinople." with:
> The foreword holds that Yaroslav did not mean to cut the Kyiv church's tie to Constantinople.

That is +1 word. With R2-M1, the brief comes to 329 words.

### R2-M3. Card `legacy.traces[0]`: "grew from it"

Round 1 changed the brief's "grew from it" to "grew there", because the "it" was unclear. The card still has "The Caves monastery grew from it.", and its "it" could be the hill or the cave.

Replace with:
> The Caves monastery grew there.

### R2-M4. Two names with no context on the card

- `uncertain[6]`, "early in Izyaslav's reign". Replace with "early in the reign of Izyaslav, Yaroslav's son". Source: CROSS l.11787-11788, "Izyaslav his son inherited his domain".
- `legacy.traces[1]`, "citing Sreznevski". Cross gives no first name or role at l.5810, so add none. This one is acceptable as it stands.

### R2-M5. Records: a Russian line in quotation marks

The contested claim on the Sermon's authorship has "'if this guess is right'". That is English for GORSKII l.705, "Если справедлива с1я догадка", in quotation marks. Quotation marks are for held English, so drop them:
> 1844 foreword: Ilarion's, by argument from the shared manuscript, the Kagan title, likeness to the confession, and the 1555 prayer, if, it says, this guess is right (GORSKII l.146-157, l.686-716)

---

## README.md

### What checks out

- **The opening.** 9 + 2 = 11; seven written and four Georgian entries split off. The Georgian list now reads as four. "None is a census person entry" is true: no batch id, nor `hilarion-of-kyiv`, is a movement id in release 43.
- **Majors.** Release 43 has no `major` field, and the re-score's Major column marks all seven "no" (Rescore l.141-155).
- **Lengths.** 326-330 is correct. With no brief claiming an exception, the "longer only where this README names the scene" clause is met. Peter and Ilarion are flagged thin, and Theophanes's open Life is flagged.
- **River counts.** "Eight by the census's own Who rows, nine by era 4 card traditions" matches Open-Gaps 269. The cited titles exist: Open-Gaps 217 (l.2177) and 269 (l.3516).
- **Traditions.** All four sit on "3 Greek East & Orthodoxy". The names are exact: "Iconophile Byzantine Monasticism" (726-843), "The Byzantine Imperial Church (Macedonian Era)" (843-1054), "Kievan Rus' Christianity" (988-1054), and "The Byzantine Church after the Schism" (era 5, 1054-1300). The counts are 3/3/1 + 1, as on the cards.
- **The re-score rows.** Peter's scan row reads "Paulicians (as hostile recorder)" (Who_Scan_Era4 l.111), so the README is right to justify moving him. The scan row puts Keroularios in the Macedonian church, and the README justifies the added second tradition.
- **The Ilarion census bullet,** every clause against release 43:
  - `sources[1].note` reads "metropolitan of Kiev, c. 1049".
  - `statusDescription` reads "Hilarion's Sermon (c. 1049)".
  - `longDescription` has "around 1049" and "first native-born", and "two years later" agrees with 1051.
  - `why` reads "the first substantial theology written by a Rus' author".
  - The 1054-1240 voices are [0], Anthony's "first cave", and [2], "Hilarion of Kyiv ... the earliest surviving work".
  - The "Vladimir's Carts" source is there, as are the edge note's "above the Dnieper" and the Franklin 1991 citation.
  - The held lines cited all check: GORSKII l.224-230, l.4202 ("около 1050 г,"), l.761 and l.686-716; CROSS l.11741-11742, l.11751, l.11774-11775 and l.5800; PSRL1 l.6897; MOUR l.2076-2078.
- **The Keroularios bullet.** The six other places are right. Three entries and both links read "Cerularius"; Macedonian and Humbert read "Keroularios". "Sat till 1058" is at MOUR l.16006.
- **The Nikephoros and Peter bullets.** They match the census strings. The patriarch is named only in `voices[4]` and the Photius edge. Every other "Nikephoros" or "Nicephorus" hit is Phokas, Kallistos or the Hesychast.
- **The file table** matches the card keys and the records' shape.

### R2-B4. The length rule is cited to a Decision-Log entry that does not exist (Majors and lengths)

The README cites "(Decision-Log, 'Who profile length: 2:00 restated, longer only when earned', 2026-11-15)". No such entry is in `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, on this branch or on origin/main. A grep of the whole repo finds "2:00 restated" and "2:00 for all" only in this README. This is the rule the whole tightening rests on, and its only cited record is missing.

The fix is to write the entry in this PR. Under that title, record Mark's choice ("2:00 for all, earn more (Recommended)", 2026-11-15) and the working rule the round 2 brief states: every brief aims at 2:00, about 325 words, longer only where the README names the scene or source a 2:00 version would lose.

If the entry cannot go in this PR, replace the parenthesis with:
> (Mark, 2026-11-15; to be logged in the Decision-Log as "Who profile length: 2:00 restated, longer only when earned")

The README text is otherwise right.

### R2-M6. The Theophanes bullet misses two census passages

- **The Paulicians story** "The Empress's Commissioners in Armeniakon". Its text names "The continuator of Theophanes", its caveat names "Theophanes Continuatus", and `sources[0].work` reads "Theophanes Continuatus IV.16". The README lists Photius's "the chronicle that continues Theophanes", so by the same rule this story belongs in the list.
- **The Melkite story.** The README names only its caveat. Its `sources[1].work` also names him: "Theophanes, Chronicle, AM 6289 (796/7)".

Replace "in the Melkite story caveat;" with:
> in the Melkite story's caveat and sources; in the Paulicians story, as "the continuator of Theophanes" and "Theophanes Continuatus";

Neither changes "No difference": both report what the chronicle says, and neither places Theophanes himself.

### R2-M7. Language and quotations: the new Cross quotation on Ilarion's card is not listed

Ilarion's card `uncertain[6]` now quotes "to connect it with the death of the metropolitan Hilarion" (CROSS l.5192-5193). The README's list of card quotations omits it.

After "Cross's "Metropolitan of Rus" (l.11742)", insert:
> and "to connect it with the death of the metropolitan Hilarion" (l.5192-5193)

The quotation runs across a line break with no hyphen or scan mark, so "No quotation ... crosses a scan mark" still holds.

### R2-M8. The Georgian split's approval is still not on record (opening paragraph)

This carries over from R1-M16, which was left for the worker. "The coordinator approved this (2026-11-15)" has no Decision-Log line. Batch 9's split is logged at l.3412 as "(worker, told to the coordinator, 2026-11-15)".

Either add a Decision-Log line in this PR, for example "**Georgian split** (worker, approved by the coordinator, 2026-11-15)", naming the four entries and "after batch 12". Or change the README to:
> The worker told the coordinator (2026-11-15), who will make them their own batch after batch 12.

### R2-M9. The Ilarion census bullet: the Paterik also tells against Anthony's "first cave"

The bullet answers `kievan-rus-christianity-1054-1240.voices[0]` ("dug the first cave") from the Chronicle alone. The held Paterik gives a second ground: Antony's first cave at Berestovoye was one "the Varangians had dug" (PAT l.1091).

After "(CROSS l.11751, l.11774-11775)", append:
> ; the Caves Paterik has Antony first live in a cave the Varangians had dug (PAT l.1091)

### R2-M10. "Who the sources are", Ilarion: Susza is missing

The card now names Smotrytsky, through Susza, as a witness on the consecration. After the Mouravieff sentence, add:
> Jacob Susza, a bishop in union with Rome, quotes Meletius Smotrytsky in 1666 for the opposite view: Rus would not take the consecration from Michael Cerularius.

That is 25 words. Sources: SUSZA1666 l.5698-5702; SUSZA1864 l.4485-4489.

Also add to the same bullet: "The Caves Paterik's founding account is a second telling of the cave" (PAT l.1086-1111). This goes with R2-B2.

### R2-M11. Card traditions: Nikephoros is not purely "the worker's call"

The README says "Nikephoros in Iconophile Byzantine Monasticism is the worker's call." But the era 4 scan row the re-score carries (Era4:102) already places "Patriarch Nikephoros I" in Iconophile Byzantine Monasticism (Who_Scan_Era4 l.102). The choice agrees with the re-score's row, and the README's weighing of the other placing still stands.

Replace the bold lead with:
> **Nikephoros in Iconophile Byzantine Monasticism follows his scan row (Era4:102), which the re-score carries; the worker weighed the other placing.**

---

## A note for the coordinator (not this batch's files)

R1-M10's batch 9 alignment gains a point from R2-B2. In the held Paterik (l.1086-1097), Antony first lived in a Varangian cave at Berestovoye, went back to Athos, and only later came to Ilarion's cave. Batch 9's Antony and Theodosius profile follows the Chronicle. If its card speaks to the founding order, it may want the Paterik's account named as well. This belongs in the Open-Gaps "Era 4 Who batch 10" entry, as a note for batch 9.

---

**Verdict:** The Ilarion brief is sound as new text and needs only two minor words. The card has three blocking defects, all from round 1 fixes: a missing source, a misreported Paterik, and an unidentified Clement. The README has one: it cites a Decision-Log entry that does not exist. Count: 4 blocking (R2-B1 to R2-B4) and 11 minor (R2-M1 to R2-M11).
