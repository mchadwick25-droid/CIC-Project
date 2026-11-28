# Card check: Suetonius

Checked `suetonius.card.json` and `Card_Edits.md` against the brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, `Source_Sheet.md`, `Card.existing.json` and the census entry, with every cited line re-read in its file. Card checker; I did not write the card.

## Verdict: FIX

Seven changes, listed exactly below. Everything else passes.

## What passes

- **Validator.** A scratch copy of the census, with this card, the brief as `longDescription`, a placeholder `secondReading` on Q1, Q2 and Q3, and a renderings copy that lists the brief's four renderings in place of the three old `suetonius` ones: `node tools/validate-census.mjs` gives 0 errors. Both copies are outside the repository.
- **Readability.** `python -m engine.m1.profile_readability` on the card's running text, outside the repository: `card_text.txt: 1485 words, grade 7.0 (names out 5.4), reading ease names out 79.1, 12.9 words a sentence, 0.8 joining words per 100, 31% short sentences, longest sentence 34 words - pass (note: grade 7.0 is under 8: the listener read checks it is not flat)`.
- **Kept fields** (item 2). Each field `Card_Edits.md` marks as kept matches `Card.existing.json` word for word: `otherNames[0]`, `label`, `knownFor`, `placeNote`, `role`, the Lives `keyWorks` entry, the fire item in `uncertain`, both `ownWords`, the Acts and both Apology 3 entries in `about`, and the `printed`, `work`, `englishPrinted`, `uncertain` and line fields kept on Q1, plus the ones kept on Q2.
- **quotationOriginals** (item 4). There are seven, one for each quoted span in the brief: Q1, "Chrestians", "Chrestus", Q2, "Christian", "the anointed one" and Q3. None is left for a dropped span. Each `printed` and `original` stands at its file and lines (ROL 25843–25844, 25907–25909, 28458–28460, 28523–28525 with the listed scan reading; TERT-C 3903, 3905, 3904–3907; anf03 9204, 9206, 9205–9208; anf07 3163, 3177; LAC-L 16813–16814, 16830). Q1, Q2 and Q3 carry no `secondReading`, and each is made from its held original.
- **"checked at card"** (item 5). "Chrestians" matches *Chrestiani pronuntiamur* and the ANF's "you call us “Chrestians”". "Chrestus" matches *Chrestum* and "call Him Chrestus". "Christian" matches *Christianum … nomen* and "The name *Christian*". "the anointed one" matches *id est unctum* and "that is, the Anointed". All four hold.
- **Sources.** Every file the card cites is listed in `sources`. No audit, review or ruling is named, and the spelling is American outside the printed wording.
- **Modern content** (item 1). The removed Rolfe, Thomson–Forester and Paulinus lines are rightly off the card. Rolfe's introduction moves word for word to `modernWorks`. Each `modernWorks` note says what the work covers. The `datesNote` works from the sources' clues (ROL 32023–32025; Domitian's end, S5), and 69, 77, 120 and 121 do not appear.
- **Not found** (item 6). `Card_Edits.md` lists none, and I found none beyond the fixes below.
- **Entry fields** (item 7). The `dates` change, `teaser` unchanged, the `regions` conflict ("Asia Minor" has no held support) and the `modernWorks` list are each justified by their evidence. The entry is not new, so there is no `atlasId` to check.

## FIX

**1. `timeline[0].lines[0]`: the wrong act, at the wrong lines.** Claudius remitted Ilium's tribute forever (ROL 25769–25770, "Iliensibus … tributa in perpetuum remisit"; ROL 25825–25827, "perpetual exemption from tribute"). "Free from every burden" is the condition in the old letter to Seleucus (ROL 25842, 25906–25907), and the cited lines 25904–25907 hold only that letter. The brief has "from tax forever".
- `text`. Old: "Claudius frees the people of old Troy from every burden, because, Suetonius says, they founded the Roman race." New: "Claudius frees the people of old Troy from tax forever, because, Suetonius says, they founded the Roman race."
- `reference`. Old: "Suetonius, Claudius 25.3, cic/texts/suetonius_lives-of-the-caesars-loeb_rolfe1914.txt lines 25904-25907". New: "Suetonius, Claudius 25.3, cic/texts/suetonius_lives-of-the-caesars-loeb_rolfe1914.txt lines 25769-25770"

**2. `briefReferences[0]`: the same act.** Old: "Lives of the Caesars, Claudius 25.3 to 25.4, Latin, with tr. John C. Rolfe: the people of old Troy freed from every burden as founders of the Roman race; the Jews driven from Rome for rioting at the urging of Chrestus; the German envoys allowed to sit with the senators at the theater." New: "Lives of the Caesars, Claudius 25.3 to 25.4, Latin, with tr. John C. Rolfe: the people of old Troy freed from tax forever as founders of the Roman race; the Jews driven from Rome for rioting at the urging of Chrestus; the German envoys allowed to sit with the senators at the theater."

**3. `legacy.remembered[1]`: each complaint given to both men.** Tertullian complains only of "Chrestians" (TERT-C 3904–3905). Lactantius complains only of "Chrestus", and he says "the ignorant", not pagans (LAC-L 16813–16814). The card's own `uncertain[0]` keeps them apart. Old: "Tertullian and, later, Lactantius complained that pagans called Christians Chrestians and Christ Chrestus. Neither names Suetonius." New: "Tertullian complained that pagans called Christians Chrestians, and Lactantius, later, that the ignorant called Christ Chrestus. Neither names Suetonius."

**4. `uncertain[11]`: remove it.** It only says what is missing (Part 1, Craft), and it names Pliny without saying who he was. Pliny is also a connection, and the role leaves connections out for now. Old: "Pliny the Younger. Pliny's letters are not among the texts used here, so nothing from them is told on this card." New: the item removed.

**5. `timeline[3].lines[3]`: an item the outline sends to the card is missing.** Outline, Leave out: "Lactantius's 'Christ is a title of power' … card". It is nowhere on the card. Lactantius, *Divine Institutes* 4.7.4: LAC-L 16770–16772, "nam Christus non proprium nomen est, sed nuncupatio potestatis et regni: sic enim Iudaei reges suos appellabant"; LAC-E 3163.
- `text`. Old: "Lactantius writes that the ignorant call Christ Chrestus by changing one letter. He explains that the Jews anointed their priests and kings with holy oil, so Christ means the anointed one. He does not name Suetonius." New: "Lactantius writes that Christ is a title of power and rule, not a proper name, since the Jews called their kings by it. He says the ignorant call Christ Chrestus by changing one letter. He explains that the Jews anointed their priests and kings with holy oil, so Christ means the anointed one. He does not name Suetonius."
- `reference`. Old: "Lactantius, Divine Institutes 4.7.5 to 4.7.7, cic/texts/lactantius_divinae-institutiones-lat_brandt1890-csel-tei.txt lines 16813-16830". New: "Lactantius, Divine Institutes 4.7.4 to 4.7.7, cic/texts/lactantius_divinae-institutiones-lat_brandt1890-csel-tei.txt lines 16770-16830"

**6. `timeline[2].lines[3].reference`: the span stops at the Book VIII heading.** ROL 36065 is the heading of Book VIII. The life of Domitian runs on to ROL 41018, and *The Lives of Illustrious Men* begins at 41036. Old: "Suetonius, Lives of the Caesars, from the life of Julius to the life of Domitian, cic/texts/suetonius_lives-of-the-caesars-loeb_rolfe1914.txt lines 918-36065". New: "Suetonius, Lives of the Caesars, from the life of Julius to the life of Domitian, cic/texts/suetonius_lives-of-the-caesars-loeb_rolfe1914.txt lines 918-41018"

**7. `timeline[4]`, Jerome: the chronicle line is marked "Date unknown" though the source dates it, and the lines are out of order.** Jerome says his chronicle ends at "the sixth consulship of the Emperor Valens and the second of Valentinianus". He leaves "the remaining period, that of Gratianus and Theodosius" for later (JEP-E 46326–46329). Under "Dates from the sources' own clues", the line takes the record's own phrase. The same lines put it before the fourteenth year of Theodosius, so it comes first.
- Period `when`. Old: "In the fourteenth year of the emperor Theodosius". New: "From the sixth consulship of Valens to the fourteenth year of Theodosius"
- Period `headline`. Old: "Jerome follows his example". New: "Jerome draws on him and follows his example"
- The chronicle line. Old `when`: "Date unknown". New `when`: "At the sixth consulship of the emperor Valens, where his chronicle ends". Old `reference`: "Jerome, preface to the Chronicle, cic/texts/npnf206_jerome-principal-works.xml lines 46321-46325". New `reference`: "Jerome, preface to the Chronicle, cic/texts/npnf206_jerome-principal-works.xml lines 46321-46329". The `text` is unchanged.
- Order. Move the chronicle line to `lines[0]`, ahead of the Lives of Illustrious Men line.

## Noted, no change

- Duchesne (1907) is left out of `modernWorks` because the outline used it only for its own readings, and its held line argues a cause ("troubles causés par la prédication de l'Evangile", R7). This follows the "Modern works on the cards" rule.
- `knownFor` says "Nero punished the Christians". It is narration, not a quote, and Nero 19.3 files these acts as his ("Haec … in unum contuli", ROL 28653–28654). It holds.
