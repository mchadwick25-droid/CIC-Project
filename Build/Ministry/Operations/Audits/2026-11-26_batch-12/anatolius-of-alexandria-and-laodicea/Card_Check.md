# Card check: Anatolius of Alexandria and Laodicea

**Verdict: FIX.** Eight changes, below. Everything else passes: every other Timeline line and headline was read against its file and lines, the keys pass `tools/validate-census.mjs`, the four `quotationOriginals` match the brief's four quoted spans, each `printed` is verbatim at its lines (EUS 42736–42738, 42760, 42816–42817; BEDE 8135), each cited file is in `sources`, no audit is named, the spelling is American, and modern works sit only in `modernWorks`, each `note` saying what it covers. The scorer run on a plain file of the card's running text, kept outside the repository: `2520 words, grade 8.4 (names out 6.4), reading ease names out 76.4, 15.5 words a sentence, 0.5 joining words per 100, 20% short sentences, longest sentence 33 words - pass`.

## FIX

1. **timeline[3].lines[1].text** (the extract leaves out "in the first year", so the line reads as if the new moon fell on Phamenoth 26 every year; EUS 42788–42790).
   - Old: "He sets the new moon of the first month on the 26th of the Egyptian month Phamenoth. That new moon is the beginning of every cycle of nineteen years."
   - New: "In the first year of his cycle, he sets the new moon of the first month on the 26th of the Egyptian month Phamenoth. That new moon is the beginning of every cycle of nineteen years."

2. **timeline[3].lines[4].reference** (Jerome is cited without his file and lines; JER 40936–40938).
   - Old: "Eusebius, Church History VII.32.20; Jerome, Lives of Illustrious Men 73, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 42917-42918"
   - New: "Eusebius, Church History VII.32.20, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 42917-42918; Jerome, Lives of Illustrious Men 73, cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml lines 40936-40938"

3. **timeline[4].lines[5].reference** ("very easily" stands only in the Latin, "facillime", BEDE-lat 18709; Giles has "can discern").
   - Old: "Bede, Ecclesiastical History III.3 and V.23, cic/texts/bede_ecclesiastical-history-english-people_giles1903.txt lines 5749-5757; 15190-15192"
   - New: "Bede, Ecclesiastical History III.3 and V.23, cic/texts/bede_ecclesiastical-history-english-people_giles1903.txt lines 5749-5757; 15190-15192; Latin, cic/texts/bede_opera-historica-v1-historia-abbatum-lat_plummer1896.txt lines 18705-18709"

4. **timeline[4].lines[2]** (Cut first 26 sends Colman's question form and "the bishop who led" to the card, and neither is on it; the year 664 is at BEDE 8236–8237, which this line's reference does not cite).
   - text, old: "A synod meets in the monastery at Whitby, where Abbess Hild presides. Colman, for the Irish side, says Anatolius wrote that Easter was to be kept from the fourteenth to the twentieth."
   - text, new: "A synod meets in the monastery at Whitby, where Abbess Hild presides. Bishop Colman, who leads the Irish side, asks whether Anatolius, a holy man much commended in church history, went against the law and the Gospel when he wrote that Easter was to be kept from the fourteenth to the twentieth."
   - reference, old: "Bede, Ecclesiastical History III.25, cic/texts/bede_ecclesiastical-history-english-people_giles1903.txt lines 7956-7967; 8117-8121"
   - reference, new: "Bede, Ecclesiastical History III.25 to 26, cic/texts/bede_ecclesiastical-history-english-people_giles1903.txt lines 7956-7967; 8117-8121; 8236-8237"

5. **timeline[4].lines[3].reference** (dated 664; the year is at BEDE 8236–8237).
   - Old: "Bede, Ecclesiastical History III.25, cic/texts/bede_ecclesiastical-history-english-people_giles1903.txt lines 8134-8150"
   - New: "Bede, Ecclesiastical History III.25 to 26, cic/texts/bede_ecclesiastical-history-english-people_giles1903.txt lines 8134-8150; 8236-8237"

6. **timeline[4].lines[0].text** (Cut first 12 sends the praise of both Eusebius and Jerome that Columbanus cites; only Jerome's is on the card; COL 4322–4338).
   - Old: "Columbanus, an Irish abbot, writes to Gregory against an Easter on the moon's 21st or 22nd day. He cites Anatolius, a man of wonderful learning, as Jerome says. He quotes words from the Latin Easter book under his name: when the moon rises only at midnight, darkness rules over the light."
   - New: "Columbanus, an Irish abbot, writes to Gregory against an Easter on the moon's 21st or 22nd day. He cites Anatolius, a man of wonderful learning, as Jerome says, whose writings Eusebius set into his Church History. He quotes words from the Latin Easter book under his name: when the moon rises only at midnight, darkness rules over the light."

7. **sources.about**, Bede in Latin, `title` (the card cites this file for III.3 too, BEDE-lat 18705–18709, and `briefSources` names both chapters).
   - Old: "Ecclesiastical History of the English People, Book 3, chapter 25 (Latin, ed. Plummer)"
   - New: "Ecclesiastical History of the English People, Book 3, chapters 3 and 25 (Latin, ed. Plummer)"

8. **uncertain[1], uncertain[5] and datesNote** (an old source's own date clue is left off. Jerome's Chronicle sets the fall of the palace quarter, "per multos annos fuerat obsessum tandem destruitur", in the first year of Claudius, JCHRON 44295–44303. The card uses the same entry for the siege at `uncertain[1]` and then says no old source gives the siege a year. No old source ties that entry to the siege Eusebius tells, so it is stated as Jerome's, with that limit).
   - uncertain[1], old: "Jerome's Chronicle says the palace quarter had been besieged for many years."
   - uncertain[1], new: "Jerome's Chronicle, under the first year of the emperor Claudius, says the palace quarter, besieged for many years, was at last destroyed. No old source says this is the siege Eusebius tells."
   - uncertain[5], old: "No held old source gives a year for his birth, the siege, his becoming bishop or his death."
   - uncertain[5], new: "No held old source gives a year for his birth, his becoming bishop or his death, or ties a year to the siege he lived through."
   - datesNote, old: "No old source gives a year for his birth, for the siege, for his becoming bishop or for his death."
   - datesNote, new: "No old source gives a year for his birth, for his becoming bishop or for his death, or ties a year to the siege he lived through."

## Notes for release (no card change)

- Validator: besides the four expected `secondReading` errors, the scratch census also gives two stale `tools/quote_renderings.json` listings (the old renderings "I advise you to send out of the gates those who are surplus," and "It is agreed that Anatolius was a most holy and most learned") and "not found verbatim" for the four new renderings. Those go in with release's renderings listing. `Card_Edits.md` reports only the four.
- quotationOriginals[3]: `original` starts at line 21582, because the scan sets "Repiyoi" between "uirum" and "sanctissimum" at 21581. It is verbatim but leaves out "Constat … Anatolium uirum". A `tools/quote_scan_readings.json` reading at release would let it start at "Constat".
- No quotation is under six words, so none is marked "checked at card".

## The three Eusebius quotations in English alone

The library holds no second Greek print of Church History VII.32. The only other Eusebius Greek files are the *Life of Constantine* (Heikel) and the *Preparation for the Gospel* (Gifford). Nicephorus Callistus (PG 147) has only his later books. Routh's volume 1 does not carry the passage.
- Quote 1 (EUS-gr 12485–12489) and quote 2 (EUS-gr 12574): there is no other witness, so English alone stands. Quote 2's span reads cleanly at 12574 (πατρὸς καὶ ἰατροῦ δίκην), but no second print confirms it.
- Quote 3: Petavius's note in Migne PG 42 (`epiphanius_panarion-haer-65-80-pg42-grc-lat_migne1863.txt` 75703–75704) quotes "οὐ μιχρῶς, οὐδ᾽ ὡς ἔτυχεν ἁμαρτάνειν φαμέν". Its scan is damaged too (μιχρῶς). Each print corrects the other to οὐ μικρῶς οὐδ᾽ ὡς ἔτυχεν ἁμαρτάνειν, but neither prints that reading clean at its lines. That is a partial witness, not a confirming print, so English alone stands.
