# Card edits: Anatolius of Alexandria and Laodicea

A full new card (batch header, "The card"), built under the role's "A new card". `Card.existing.json` (identical to the census `card` as it stands) was used as a pointer only. Short names (EUS, EUS-gr, RUF, JER, JEP, JCHRON, BEDE, BEDE-lat, BCHRON, COL, COL-lat, LATCAN, SOC, ELIAS, BARH, MICH, BHB, MARON, AASS, PL67-ed) are those of `Source_Sheet.md`; every line cited below was re-read in its file for this card.

Validator: a scratch census (outside the repository) with the final brief as `longDescription` and this card passes `tools/validate-census.mjs` except the four expected `secondReading` errors: all four quotations are six words or more, so `secondReading` is left out for release to set. Every quoted span in the card's prose stands verbatim in a cited file.

Readability (`python -m engine.m1.profile_readability` on a plain file of the card's running text, kept outside the repository): `2528 words, grade 8.4 (names out 6.5), reading ease names out 76.4, 15.5 words a sentence, 0.5 joining words per 100, 20% short sentences, longest sentence 33 words - pass`.

## Fields kept from the starting card

- **otherNames**, word for word: "Anatolius of Alexandria" (JER 40932, Jerome's own phrase), "Anatolius of Laodicea" (JCHRON 44129 "Anatolius Laodicenus"; ELIAS 41059 "Anatolii, episcopi Laodiceae").
- **knownFor**, word for word. Learned Alexandrian: EUS 42684–42690. Led people out of a besieged quarter: EUS 42752–42759 ("through his management they went out of the gates"). Bishop of Laodicea in Syria: JER 40932–40933; EUS 42938–42940. Wrote on fixing Easter's date: EUS 42769–42817. All told in the brief.
- **keyWorks[1].title** "Institutes of Arithmetic", word for word (EUS 42917–42918).
- **keyWorks[0].title** "Paschal Canons", word for word (EUS 42788).
- Kept wording inside rewritten items is listed under each field below.

## Fields changed or new

- **shortDescription** (new, two sentences): the brief's essence, paragraphs 1–2 and 6 (council vote, almost all the besieged, palace quarter, bishop of Laodicea, Easter rule, both sides claiming him).
- **datesNote**. Old: "Made bishop of Laodicea on his way to the synod at Antioch on Paul of Samosata; Jerome of Strido says he flourished under the emperors Probus and Carus". New: no year for birth, siege, bishopric or death (S2, E7); the synod on Paul's case called him to Antioch, and the Laodiceans kept him as he passed through (EUS 42928–42940); Jerome, Probus and Carus (JER 40933–40934); "the later 200s" from the modern dating of those reigns (brief paragraph 3; Polycarp model). "On his way" is McGiffert's (EUS-ed 42673), so Eusebius's own words replace it. "Jerome of Strido" becomes the census name "Jerome" (sheet, Links).
- **placeNote**. Old: "Alexandria; Caesarea in Palestine; Laodicea in Syria". New adds what happened at each: born and the siege (EUS 42684, 42696–42762), second bishop at Caesarea (EUS 42925–42928), bishop at Laodicea in Syria (JER 40933; EUS 42938–42940). Outline Setting: "on the coast" left out.
- **role**. Old: "Scholar, then bishop of Laodicea". New: "Scholar of Alexandria, then bishop at Caesarea in Palestine and at Laodicea in Syria" (EUS 42684–42690, 42925–42940; brief paragraph 7).
- **keyWorks[0].about**. Old: "his rules for fixing Easter by a cycle of nineteen years; Eusebius of Caesarea quotes a long extract". New: Eusebius's "states particularly his opinions on the passover" (EUS 42769–42773); the extract's rule and cycle (EUS 42788–42817); the rule known to the Jews (EUS 42819–42821). Brief paragraph 8.
- **keyWorks[1].about**. Old: "ten books, of which a few fragments survive". New: "ten books on arithmetic, which Eusebius and Jerome name. The Library does not hold them" (EUS 42917–42918; JER 40936–40938; sheet, Not held). "A few fragments survive" rests on McGiffert's note and Fabricius (EUS-ed 42918; ANF6 15414–15416), a modern attribution, so it moves to `uncertain`.
- **keyWorks[2]** (new): the Latin Paschal Canon under his name: allows the feast to the moon's twentieth (LATCAN 15010–15012, 15150–15153); Columbanus quoted its words as Anatolius's (COL 4349–4355; LATCAN 15014–15024); authorship disputed (D4). Brief paragraph 9 ("a Latin Easter book under Anatolius's name").
- **legacy.traces**, rebuilt from held old lines:
  1. Columbanus to Gregory: COL 4320–4355 (Cut first 12, 24; outline What came 1). Brief paragraph 9.
  2. Columbanus to the Gallic synod: COL-lat 20791–20797, narrator's words only (Cut first 2).
  3. Bede III.3: BEDE 5749–5757; "very easily", BEDE-lat 18705–18709 (I1c).
  4. Whitby: BEDE 8117–8121, 8134–8141 (I1d).
  5. Bede's letter "according to Anatolius": kept from the old card with "letter" confirmed, BEDE 15503–15513 (a book of Epistles).
  6. Elias: kept from the old card, wording changed to add the two days, ELIAS 41059–41066; "In the eleventh century" dropped (no held line dates him).
  - Removed: McGiffert's "first Christian … so far as we know" (modern own claim; outline Who tells it, D7). Socrates moved to `uncertain` (Inferential-Thin, I3; the identification is the translator's note, SOC 41699–41700).
- **legacy.remembered**:
  1. Eusebius's praise: kept, with rhetoric added (EUS 42685–42688).
  2. Jerome, wonderful learning and his genius seen from his two works: JER 40934–40938 (old: "Jerome of Strido calls him a man of wonderful learning").
  3. Jerome, Letter 70: JEP 16665–16702 (I2; outline Card only).
  4. Jerome's Chronicle under Probus, copied by Bede's Greater Chronicle: JCHRON 44129–44131; BCHRON 23993–23998 (I2).
  5. Whitby, Colman and Wilfrid: kept; the old "but said Colman's side did not keep his cycle" becomes "did not keep his rules" (BEDE 8136–8137, "do not observe his decrees"; the cycle is told in `traces`).
  6. Barhadbeshabba and Michael the Syrian: BHB 13022–13023; MICH 15951–15952 (I2).
  7. Bar Hebraeus: kept; "in the thirteenth century" dropped (BARH 4961–4965).
  - Removed: the Bollandists' line (a modern report of old calendars, AASS 69809–69811); the work goes to `modernWorks`.
- **uncertain**, rebuilt on old sources, with the modern debate on the Latin book kept as a debate (Review MINOR 7; outline Who tells it):
  1. Report: kept ("They relate", "They say", EUS 42696, 42718), adding no cause and no year (E1).
  2. Cause of the war (new): EUS 42721–42723; RUF EUS-gr 12447–12448; JCHRON 44299–44301.
  3. Rufinus's siege: kept in substance; "in his Latin version of about 402" becomes "a century later" (sheet, Witness kinds); "the third part loyal to Rome", the commander, the parent's and doctor's care, the speech and famine-and-war (RUF EUS-gr 12533–12545, 12654–12658) (Cut first 1).
  4. The school: Eusebius's report and Rufinus (EUS 42688–42690; RUF EUS-gr 12444–12447). Duchesne and McGiffert removed (modern own claims, D3).
  5. Subjects: kept (EUS 42685–42688; JER 40935).
  6. Years: replaces the old items naming Richardson's, Salmond's, Harnack's, Hefele's, Loofs's and McGiffert's years (modern; outline Who tells it; header "Modern works on the cards"). Old witnesses: JER 40933–40934, JCHRON 44129–44131, ELIAS 41059–41060.
  7. The synod: Eusebius's words only (EUS 42928–42940); McGiffert, Harnack, Bardy removed (D6); Paul's teaching as Eusebius's charge (EUS 41838–41840; Review B2).
  8. Death (new): EUS 42942–42944 (E7).
  9. The Easter book's place and time: kept in part; Harnack and Hefele removed (E6).
  10. The nineteen years: Wilfrid against Ceolfrid's letter (BEDE 8137–8139; BEDE 14738–14742, Book 5 chapter 21); Hefele's "discovered" and McGiffert's Metonic cycle removed (D7).
  11. The Latin book: first printed in 1634 (COL-ed 4326–4327, a modern event); the modern disagreement told as a debate, unnamed (D4). Old items naming Ideler, Zahn, Harnack, Hagen, Krusch removed.
  12. Days of the moon: kept (BEDE 8117–8121, 8143–8150; LATCAN 15010–15012; BEDE 5749–5757), adding Wilfrid's "before the full of the moon" (BEDE 8149–8150) and that no old source says which text either drew on (outline Do not say).
  13. Maronite chronicle: kept (MARON 3720–3725); "the 22nd of March in the extract" (McGiffert's conversion, EUS-ed 42794–42798) becomes the extract's own days, Phamenoth 26 and Dystrus 22 (EUS 42789–42801).
  14. Socrates (moved from `legacy`): SOC 41696–41705, without the translator's identification.
  15. Arithmetic fragments (moved from keyWorks): ANF6 15411–15416.
  - Removed as modern only: McGiffert, Duchesne, Harnack on politics and the council; Harnack on Dionysius; McGiffert and Hefele on the cycle's adoption; Bucherius (D1, D8; outline Leave out; Links, Dionysius).
- **sources**. ownWords: the English extract kept; the Greek extract added (EUS-gr 12595–12621); the ANF6 item kept with `disputed`. about: kept Eusebius (title widened to chapters 27, 29, 32), Schwartz with Rufinus, Jerome Lives 73 (author "Jerome"), Bede English (chapters widened to III.3, III.25, V.21, V.23, V.24), Bede Latin, Maronite Chronicle, Socrates, Elias, Bar Hebraeus; added Jerome Letter 70, Jerome's Chronicle, Columbanus (English and Latin), Bede's Greater Chronicle, Barhadbeshabba, Michael the Syrian. Moved to `modernWorks` (Entry fields): Hefele, Harnack (two), Duchesne, Loofs, Bardy, the PL 67 editors, the Bollandists.
- **briefReferences**: rewritten to the final brief, one per beat. Removed as no longer told: McGiffert's first-Christian note and Hefele on the cycle's adoption; the Paschal Canon's twentieth day matching Colman; the authorship debate; Laodicea as a port (Loofs); the bishopric year and siege-year debates; the world-census line; "another man bishop of Laodicea before the persecution"; the king's ruling.
- **quotationOriginals**: one entry for each of the brief's four quoted spans; the old two (no longer quoted in these words) removed.
  1. "I advise sending out of the gates …": printed EUS 42736–42738. Rendered from EUS-gr 12485–12489, a damaged scan (`xci` for καί), the only held Greek print, so English alone.
  2. "like a father and a doctor": printed EUS 42760. Greek πατρὸς καὶ ἰατροῦ δίκην (EUS-gr 12574) in the same damaged scan, so English alone.
  3. "make no small mistake, and no careless one.": printed EUS 42816–42817. Greek EUS-gr 12614, same scan, line damaged (`>aurnv`), so English alone.
  4. "It is agreed that Anatolius …": printed BEDE 8135 (8134 reads "Anatoliuj*", so the print begins at "was"); original BEDE-lat 21582, clean, checked by hand: "sanctissimum, doctissimum, ac laude esse dignissimum" (21581 carries margin text, "Repiyoi", between "uirum" and "sanctissimum", so the original begins at line 21582).
- **briefSources** (new): EUS, EUS-gr, JER, COL, ANF6 (LATCAN), BEDE, BEDE-lat: the old sources the brief draws on.
- **timeline** (new): six periods, every line with work, file and lines.
  1. Learning: EUS 42684–42690; Jerome's and Rufinus's differences as notes (D3).
  2. Siege: EUS 42696–42762; the palace quarter glossed from the translator's note (Cut first 15); Rufinus's differences as notes (D1); deacon's "greatest favor" (Cut first 19); "others of every age" (Cut first 21); honor from those in high office (Cut first 7, 13).
  3. Caesarea and Laodicea: EUS 42764–42767, 42657–42662, 42925–42944, 42683–42684, 41838–41840; JER 40932–40934; Elias as a note. "For a short time they led that church together" (Cut first 8) and "one good man … following another" (Cut first 9).
  4. Writings: EUS 42769–42868, 42917–42918 (Cut first 3, 14; Leave out, the writers he named).
  5. Easter quarrel: COL 4320–4355; COL-lat 20791–20797; BEDE 7956–7967, 8117–8150, 8195–8237, 5749–5757, 15190–15192. Wilfrid's Egyptian count (outline Leave out: card), the king's ruling (Cut first 28; Fresh_Read "who won at Whitby").
  6. Later centuries: JEP, JCHRON, BCHRON, BEDE 15503–15513, BHB, MARON, ELIAS, MICH, BARH (I2, I3).

## Items the outline, review and fresh read send to the card

All on it: Cut first 1, 2, 3, 7, 8, 9, 10 (rest of Wilfrid's sentence, in `remembered` and `timeline` in narrator's words), 12, 13, 14, 15, 19, 21, 24, 26 ("much commended in church history" in `remembered`; Colman's question in `timeline`), 27, 28; Leave out items marked card (Maronite chronicle, Wilfrid's Egyptian count); Card only (Jerome, the chronicles, Barhadbeshabba, Bar Hebraeus, Michael, Elias, Socrates, Bede's letter, D4). The Bollandists' note (I5) goes to `modernWorks` as a modern work. Review MINOR 7 (authorship, D4): `uncertain` 11. Fresh read, who won at Whitby: `timeline` period 5.

## Entry fields

- **teaser**: no change. It matches `knownFor`, which the brief supports.
- **dates** "flourished under Probus and Carus": no conflict (JER 40933–40934).
- **modernWorks** (new; title and author required). The eight works now under the card's `sources` move here word for word, and the works the outline used to clarify or find the old texts are added:
  1. {"title": "History of the Councils of the Church, vol. 1, on the Easter cycle", "author": "Karl Joseph von Hefele", "year": "1872", "note": "A reference history of the church councils to Nicaea, in English, with a section on the Easter cycles."}
  2. {"title": "History of Early Christian Literature: Chronology, vol. 2 (Geschichte der altchristlichen Litteratur, Chronologie)", "author": "Adolf von Harnack", "year": "1904", "note": "A chronology of early Christian writers, in German, with a section on Anatolius and the Latin Easter book under his name."}
  3. {"title": "The Mission and Expansion of Christianity, vol. 2 (Mission und Ausbreitung des Christentums)", "author": "Adolf von Harnack", "year": "1906", "note": "A history of the spread of Christianity in the Roman world, in German, which names Anatolius among the bishops of the third century."}
  4. {"title": "Ancient History of the Church, vol. 1 (Histoire ancienne de l'Église)", "author": "Louis Duchesne", "year": "1907", "note": "A reference history of the early church, in French, with a passage on Anatolius and the siege at Alexandria."}
  5. {"title": "Paul of Samosata: fragments (Paulus von Samosata)", "author": "Friedrich Loofs", "year": "1924", "note": "An edition of the fragments of Paul of Samosata, in German and Greek, with a study of the synods at Antioch."}
  6. {"title": "Paul of Samosata: a historical study (Paul de Samosate)", "author": "Gustave Bardy", "year": "1923", "note": "A historical study of Paul of Samosata and the synods that judged him, in French."}
  7. {"title": "Editors' notes in Patrologia Latina, vol. 67, quoting Bucherius on the Paschal Canon of Anatolius", "author": "Aegidius Bucherius, quoted by the editors", "year": "1865", "note": "Latin editors' notes on the Easter cycles, quoting Bucherius's commentary on the Latin Paschal Canon."}
  8. {"title": "Acta Sanctorum, March, vol. 2, note on Saint Anatolius, bishop of Laodicea", "author": "The Bollandists", "year": "1865", "note": "A Latin collection of saints' lives, whose note lists the old calendars that remember Anatolius."}
  9. {"title": "The Church History of Eusebius (Nicene and Post-Nicene Fathers, Second Series, volume 1)", "author": "Arthur Cushman McGiffert (tr.)", "year": "1890", "note": "English translation of Eusebius's Church History, with notes on the palace quarter of Alexandria, the Egyptian and Macedonian months and the deacon Eusebius."}
  10. {"title": "Eusebius Werke, vol. 2, part 2: Die Kirchengeschichte, books 6 to 10, with Rufinus's Latin", "author": "Eduard Schwartz and Theodor Mommsen (ed.)", "year": "1908", "note": "The Greek text of Eusebius's Church History, with Rufinus's Latin version on the facing pages."}
  11. {"title": "Gregory the Great, Ephraim Syrus, Aphrahat (Nicene and Post-Nicene Fathers, Second Series, volume 13)", "author": "James Barmby (tr.)", "year": "1898", "note": "English translation of Gregory's letters, with Columbanus's letter to him and notes on the Easter question."}
  12. {"title": "Gregory Thaumaturgus, Dionysius the Great, Julius Africanus, Anatolius and Minor Writers, Methodius, Arnobius (Ante-Nicene Fathers, volume 6)", "author": "S. D. F. Salmond (tr.)", "year": "1886", "note": "English translation of the Latin Paschal Canon under Anatolius's name and fragments on arithmetic, with a short notice."}
  13. {"title": "Theodoret, Jerome, Gennadius, Rufinus: Historical Writings (Nicene and Post-Nicene Fathers, Second Series, volume 3)", "author": "Ernest Cushing Richardson (tr.)", "year": "1892", "note": "English translation of Jerome's Lives of Illustrious Men, with notes."}
  14. {"title": "Bede's Ecclesiastical History of the English Nation", "author": "J. A. Giles (tr.), ed. L. C. Jane", "year": "1903", "note": "English translation of Bede's history, with the synod at Whitby."}
  15. {"title": "Venerabilis Baedae Opera Historica, vol. 1", "author": "Charles Plummer (ed.)", "year": "1896", "note": "The Latin text of Bede's history."}

## Conflicts with the census entry

None. The entry carries no `voices`, `legacy`, `why`, `sourcing` or `relationsSummary`.

## Claims not found

None. Every kept claim was found at its lines; claims resting only on modern works were removed or moved, as listed above.
