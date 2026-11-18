# R1 review: era 4 batch 3

Round 1 ran in two parts, each by a fresh Opus agent that had not seen the drafting, at full effort. The parts follow, unchanged.

## R1 review, part A: Theodore of Tarsus, Willibrord, Leoba, Wilfrid of York (era 4 Who batch 3)

Reviewer: independent Opus, first sight of these drafts (commit 00bc3cd4). I edited no profile file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `CLAUDE.md` in full; `Who_Profile_Pattern.md` checklist 1 to 14; the Decision-Log Who profile entries of 2026-11-12 to 2026-11-14 and their cap rulings; the rulings block of `Who_Scan_Era4.md`; the coordinator calls in the brief (none major; standard length). Form follows era 4 batch 1's `R1_review.md`. Following the earlier rulings, a missing common-name identifier is minor and a false absence is blocking, wherever it sits.

For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt` and the `records.json` entry. I opened every cited line in its vendored file and read it in context, folding OCR noise, double spaces, hyphen breaks and Raine's interleaved side-notes. Files: Giles/Jane 1903 (`bede_ecclesiastical-history-english-people_giles1903.txt`, "GILES"), Plummer 1896 ("PLUMMER"), Raine 1879 (`byrhtferth_vita-s-oswaldi-in-historians-of-the-church-of-york-v1-lat_raine1879.txt`, "RAINE"), Wasserschleben 1851 ("WASS"), Duchesne LP 1 and 2 ("LP1", "LP2"), Alcuin PL 100-101 ("ALC"), Kylie 1911 ("KYLIE"), Bute 1908 ("BUTE"), PL 96, PL 159, PL 195, AASS March 3, the York Prymer, Adam of Bremen, Mansi XI.

Absence searches across all of `cic/texts/`: Theodore with Cantuar/Dorovern; every "Theodor" line in RAINE after Stephen's Life (to find the later Lives); "regina", "Ermenburg", "carcer", "-feld" in RAINE's Fridegod and Eadmer sections; Willibrord/Wilbrord/Willebrord/Wilibrord in every file that holds them (36 files, including the Vita Dagoberti III, AASS, Hoynck van Papendrecht, the Utrecht synod of 1763, Rimbert); Lioba/Leoba/Leobg-/Liobg-/Leuba/Liuba (every hit read); "Wilfrid of Ripon"; "John VI".

Readability is from `engine.m1.gates.grade_text`, run from the repo root. I applied the suggested brief fixes to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/39eb9bee-a8ba-523c-9dfe-f5ca37666176/scratchpad/fixA/`.

**Applies to all four.** A script confirmed that each audio file equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. No tag appears in a brief or card. Every brief fix below has to be carried into the audio. All four cards are in Mark's order and have no null or empty field. Every `sources` file exists and holds the named work. No card sentence runs past 25 words. "No source used here" on the cards is the approved house form (era 3 batches) and is not flagged. The drafts carry no list lines, so the list-line half of item 14 was not checked.

---

### Theodore of Tarsus (344 words, about 2:07; FK 5.9, Flesch 73.5)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Stephen "from Wilfrid's side" in the brief; the card repeats it) |
| 7 | Contested claims both sides | FAIL (A-B2, A-M4) |
| 8 | Common names | FAIL (A-M2, A-M3) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the brief's Bede and Stephen caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records and absences | FAIL (A-B1, A-M5) |

**Sentences checked and found faithful.**
- P1: the vacancy, Hadrian of the Niridian monastery near Naples, Andrew, the respite and Theodore are at GILES l.8734-8763. "born at Tarsus in Cilicia" and "venerable for age, being sixty-six years old" are verbatim (l.8758-8763). The pope's condition, "according to the custom of the Greeks, introduce anything contrary to the true faith", is verbatim (l.8773-8776).
- P2: 668 is at l.8782-8785, and 690 at l.12686-12690.
- P3: the visit and "the canonical custom of celebrating Easter" are at l.8838-8843. "This was the first archbishop whom all the English church obeyed" is verbatim (l.8843-8845).
- P4: Hertford is at l.9271-9378, and 673 at l.9390-9391. "myself, Theodore, the unworthy bishop of the see of Canterbury" is verbatim (l.9277-9279). The ten marked chapters are at l.9301-9305, and chapters I, II and VII at l.9308-9340.
- P5: the preface is at WASS l.11448-11451: "LIBELLI QUEM PATER THEODORUS ... TEMPERAVIT", and "DISCIPULUS UMBRENSIUM". Eoda is at l.11512-11514. "fertur" ("it is said") stands behind "he reports". Wasserschleben's "Theodor hat kein Beichtbuch geschrieben" is at l.1866-1872.
- P6: the king and queen "archiepiscopum Theodorum cum muneribus ... invitaverunt" is at RAINE l.6563-6567. The London confession is at l.8140-8168.
- P7: the dream and the eighty-eight years are at GILES l.12686-12693. "than ever they had done before" is verbatim (l.12703-12705).

**Card.** I checked these against their lines:
- `dates` (l.8782-8785, 8836-8838, 12686-12690; the epitaph's "September's nineteenth day", l.12716) and `place` (l.12694-12696).
- `keyWorks`: Hertford's six named chapters; Hatfield, with Eutyches, the five councils and Pope Martin (l.10268-10335).
- `legacy.traces` 1 to 3 (l.8846-8873; Albinus l.152-156; Tobias l.15081-15085). Trace 4 is at l.9887-9889 and l.11732-11739. Trace 5 is at WASS l.1654-1660.
- `legacy.remembered`: the epitaph (l.12712); BUTE l.2367, 69066-69072, 71005-71045; Eadmer, Life of Bregwin (PL 159 l.26730-26736 for the authorship, l.58274-58277 for the text); Henry of Huntingdon (PL 195 l.62779-62785).
- `uncertain` 5 to 9: Raine's subdivision (RAINE l.1448-1451); the Liber pontificalis note (LP2 l.7107-7131, 7262-7263; WASS l.1673-1680); the four months (PLUMMER l.22321-22326); the two tenure figures (l.8838-8840, 12693).
- `sources.ownWords` 3: Theodore's letter to Ethelred of Mercia is at RAINE l.8215-8250.

#### Findings

- **A-B1 BLOCKING (card `uncertain` 3; records claim "Stephen alone"; item 1; a false absence).** "Stephen alone tells that Theodore, old and ill, called Wilfrid to London and confessed he had wronged him." The same volume holds two later Lives that tell the confession. Fridegod's verse Life has it under the heading "Quomodo a Theodoro archiepiscopo revocatus": "Theodorus, damnare nefas in presule quondam / Commissum cupiens", with Erconwald present, and "Poenitet en, fili" (RAINE l.13902-13945). Eadmer's Life, chapter 44, has "qui delictum quod jam olim in famulum Dei commiserat ... corrigere volens" (l.17912-17920). Raine says Fridegod's poem was made from "flosculis" excerpted from the earlier Life (l.2133-2134) and that Eadmer "occasionally quotes from" Eddi (l.2366-2368). So these are not independent witnesses, but "alone" is false. Fix, card: "Stephen tells that Theodore, old and ill, called Wilfrid to London and confessed he had wronged him. The later Lives by Fridegod and Eadmer, which draw on Stephen, tell it too. In Stephen's account he also wished Wilfrid to succeed him at Canterbury." In the records, rename the claim "Stephen, followed by Fridegod and Eadmer", and add RAINE l.13902-13945 and 17912-17920 as witnesses.

- **A-B2 BLOCKING (card `uncertain` 5; records `contested_claims` 2, "Against"; item 7; a witness put on the wrong side).** The card ends its penitential item: "Charles Plummer notes that Bede never mentions one." The records list Plummer among those against Theodore's authorship. Plummer's argument is about Bede's authorship of a penitential. He speaks of "his penitential", meaning Theodore's, and says Bede's silence "would certainly be strange if he were himself interested in such literature" (PLUMMER l.11097-11101). He adds that the penitential ascribed to Bede draws on "earlier works including Theodore's", and asks why Bede would compile it "when Theodore's work was in existence" (l.11103-11108). Plummer takes the penitential as Theodore's. Bede's silence is already Wasserschleben's point: "ebenso wenig Beda" (WASS l.1663-1667). Fix, card: "Charles Plummer notes that Bede never mentions one." -> "Wasserschleben adds that Bede never mentions one. Charles Plummer notes the same silence but still speaks of the penitential as Theodore's." In the records, move Plummer out of "Against". Either put him under "For", citing l.11097-11108, or keep him as a note that he records the silence while calling the work Theodore's.

- **A-M1 MINOR (brief P4; item 1).** "They covered Easter, bishops keeping to their own dioceses, and a synod each year." "Covered" says the ten chapters were these three; they are three of ten (GILES l.9308-9355). Fix: "Among them were Easter, bishops keeping to their own dioceses, and a synod each year."

- **A-M2 MINOR (brief P6 and card `uncertain` 2; item 8).** "King Egfrid" has no identifier in either text. Bede: "Egfrid, king of the Northumbrians" (GILES l.10285, 15365). Fix, brief: "In 678, Bede says, King Egfrid drove Wilfrid from York," -> "In 678, Bede says, Egfrid, king of the Northumbrians, drove Wilfrid from York,". Fix, card: "Bede says King Egfrid drove Wilfrid out in 678," -> "Bede says Egfrid, king of the Northumbrians, drove Wilfrid out in 678,". (Bede's active "driven from his see by King Egfrid" is in the summary of years, l.15352-15353; IV.12, the line the records cite, is passive. See A-M5.)

- **A-M3 MINOR (card `knownFor`; item 8).** "With Abbot Hadrian he taught pupils at Canterbury". Hadrian is a common name, and the card is a separate text from the brief. Bede: "an abbat, called Hadrian, by nation an African", of a monastery "not far from the city of Naples" (GILES l.8737-8740). Fix: "With Hadrian, an African abbot from near Naples, he taught pupils at Canterbury, and he presided at the synods of Hertford and Hatfield." (23 words.)

- **A-M4 MINOR (card `uncertain` 7; item 7; one side cut short).** "Stephen says Theodore had Chad removed from a see not his own." Stephen goes on to say that Chad, after his penance, was ordained in full through every grade for Lichfield: "per omnes gradus ecclesiasticos ad sedem predictam plene eum ordinaverunt" (RAINE l.5626-5660). As it stands, the item sets "completed his ordination" against "removed", as if Stephen denied the first. Fix: "Stephen says Theodore had Chad removed from a see not his own, and that Chad was later ordained in full for Lichfield." Add the line to the records' Chad side.

- **A-M5 MINOR (records).**
  - (a) The two "four months" claims are tagged Contested, but there is no `contested_claim` for them. Add: claim "Who waited four months for the Roman tonsure", sides "J. A. Giles's English: Hadrian (GILES l.8777-8779)" and "Plummer's Latin: the sentence names no one, and the next is Theodore's ordination (PLUMMER l.22321-22326)".
  - (b) The "Wilfrid's fall, Bede" claim and `contested_claims` 1 cite l.9865-9895, which is passive. Add GILES l.15352-15353 ("driven from his see by King Egfrid"), which carries the card's "King Egfrid drove".

After the fixes (A-M1 and A-M2 in the brief, with A-B4's rename carried into P2 as "Bishop Wilfrid of Ripon"): 348 words, about 2:09, FK 6.0, Flesch 73.3 (scratch copy scored).

Verdict: NOT CLEAR (2 blocking, 5 minor).

---

### Willibrord (342 words, about 2:07; FK 6.0, Flesch 75.9)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-M6, A-M8) |
| 2 | Quotes verbatim | PASS (the note's "quamvis indignus" and "assent" lines; Duchesne's French) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M8, a triad) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Alcuin's Life is marked as late and "full of miracle stories", with Froben's reckoning) |
| 7 | Contested claims both sides | PASS (year and church of consecration, who sent him, Utrecht, the year of death) |
| 8 | Common names | FAIL (A-M7) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (opens on his own note; Bede against Alcuin in P3, Bede against Duchesne in P4) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the Alcuin and Bede caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (A-M10) |

**Sentences checked and found faithful.**
- P1: the note is at LP1 l.173624-173629: 690, "veniebat ultra mare in Francia", 695, "quamvis indignus", Pope Sergius, "agens annum septengentesimum vigesimum octavum". The calendar is at l.173617-173621.
- P2: Northumbria is "provincia Nordanhumbrana" (ALC l.54813-54814). Bede's "is still living ... thirty-six years a bishop" is at GILES l.13052-13055. Froben's "circa annum 796, annis amplius quinquaginta post sancti viri obitum" is at ALC l.52018-52024, and Froben as editor at l.363.
- P3: Wilgis and Ripon are at ALC l.54814-54815 and 54867-54870. "Usque ad vicesimum ... annum" and the twelve years in Ireland are at l.54941-54987. Bede's Egbert, "twelve in number", is at GILES l.12750-12872. Alcuin's "Tricesimo ... tertio ... anno ... navigare cogitavit" is at ALC l.54995-55009.
- P4: Bede's 696, Saint Cecilia, Clement and Utrecht are at GILES l.13024-13039. Duchesne's "Il y a erreur dans les chiffres de Bède" and "C'est évidemment la vraie date" are at LP1 l.173613-173636.
- P5: Fositesland, the cattle killed, three baptized, the lots, one martyr, "Non est Deus, quem colis, sed diabolus", and the return to Pippin are at ALC l.55166-55303.
- P6: Echternach and the burial are at l.55637-55641 and 55794-55798. The homily is at l.56070-56114.

**Card.** I checked these against their lines:
- `keyWorks` (LP1 l.173617-173629).
- `legacy.traces` 1 to 6: GILES l.13036-13045; ALC l.55333-55338, 55637-55641; RAINE l.6719-6723 ("filius ejus in Hripis nutritus"); KYLIE l.1746-1748, 1789-1798; ALC l.55702-55711.
- `legacy.remembered` 1 to 4: ALC l.52018-52029, 54831-54834 (Alcuin's own prologue names Beornrad); BUTE l.87042-87055, 93836-93925; the Prymer at l.5363-5365; ADAM l.19265-19269 ("Hanc in Vita sancti Willebrordi Fosetisland appellari discimus").
- `uncertain` 2 to 7, including Jane's "Wiltaburg = Wiltenburg; not Utrecht" (GILES l.16031) and the Breviary's "before he was seven" (BUTE l.93838-93842).

**Absence check.** The records' "no letter by Willibrord is held" holds. Of the 36 files that name him, none holds a letter or charter of his. Hoynck van Papendrecht names him once, for relics (l.35710). The Vita Dagoberti III names him (Krusch SRM 2 l.40786-40888), but Krusch marks that text "Fictus est". Not used, and rightly. (Held but unused, offered only as an option: the Utrecht synod of 1763 calls its church "a beatissimo Willibrordo fundata", `church-of-utrecht_acta-et-decreta-secundae-synodi-lat_1764.txt` l.86.)

#### Findings

- **A-M6 MINOR (brief P5; item 1; the grammar changes Alcuin's rule).** "No one touched its cattle or drew from its spring except in silence." This reads as if the cattle could be touched in silence. Alcuin: no pagan dared touch the beasts or anything there, nor draw water "nisi tacens" (ALC l.55170-55185). Fix: "No one dared touch its cattle, and water was drawn from its spring only in silence."

- **A-M7 MINOR (brief P5; card `uncertain` 5; item 8).**
  - (a) "King Radbod cast lots" in the brief, and "after Radbod was beaten" in the card, which is the card's first mention, both lack an identifier. Alcuin: "regem Frisonum Radbodum" (ALC l.55188). Fix, brief: "King Radbod cast lots to punish him," -> "Radbod, king of the Frisians, cast lots to punish him,". Fix, card: "after Radbod was beaten" -> "after Radbod, king of the Frisians, was beaten".
  - (b) In the same card item, "under Charles" will be heard as Charlemagne. Alcuin: "filium ejus Carolum", Pippin's son (ALC l.55344-55346). Fix: "under Pippin's son Charles".

- **A-M8 MINOR (brief P6; items 1 and 4).** "Alcuin says Rome, Tours and Paris each have their saints. To his own people, he says, God gave no small help in Willibrord."
  - Alcuin's list is Rome, Milan, Agaunum, Poitiers, Tours, Paris and Reims (ALC l.56070-56108). The three picked make a triad.
  - "Nobis" is the community Willibrord "gathered into this most sacred fold" ("qui nos in hoc sacratissimum ovile congregavit", l.56112-56118), not his people. A listener will hear the English.
  - Fix: "In a sermon for his feast, Alcuin says Rome, Milan, Tours and Paris each honor their own saints. To the monks Willibrord gathered, he says, God gave no small help in him."

- **A-M9 MINOR (card `dates`; item 1; a variant left out).** "Alcuin gives 7 November as the day he died". Froben prints the variant beside it: "[Mab., die sexto Nov. id est viii Idus]" (ALC l.55794-55795). Fix: "Alcuin gives 7 November as the day he died, where Mabillon's text reads 6 November, and gives no year." The brief's "7 November" can stand, as Alcuin's.

- **A-M10 MINOR (records).** Three claims are tagged Contested and have no `contested_claim` behind them.
  - "Jane's note: Wiltenburg; not Utrecht": add Jane as a third side to "Who sent him to Frisia and who gave him Utrecht", or make it a claim of its own.
  - The Breviary's "before he was seven" against Alcuin's "statim ablactatum": add a `contested_claim`, "His age when given to Ripon", with sides BUTE l.93838-93842 and ALC l.54867-54870.
  - The Breviary claim also carries the 738 year, which is covered.

After the fixes (A-M6, A-M7a and A-M8 in the brief): 351 words, about 2:10, FK 6.2, Flesch 75.1 (scratch copy scored).

Verdict: NOT CLEAR (0 blocking, 5 minor).

---

### Leoba (337 words, about 2:05; FK 6.8, Flesch 71.4)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | Named witnesses | PASS (Kylie named at each of his claims) |
| 6 | Partisan witness marked | n/a |
| 7 | Contested claims both sides | PASS (nothing contested; Kylie's unsourced lines are told as his) |
| 8 | Common names | FAIL (A-M12, card only) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (opens on her letter; standard length for a thin record) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the brief's "much of the rest is Kylie's") |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (she led a house and wrote; women ruling) |

**Sentences checked and found faithful.**
- P1: the greeting, "bound to me by ties of kinship", Dynne, "more than eight years since", Aebbe, "long oppressed by infirmities", "I am the only daughter of these my parents", "that the bond of our love may hold firm for ever" and "correct the homely style of this letter" are at KYLIE l.4512-4543. Each quotation is verbatim, folding OCR "1s", "weil", "gitt Lam".
- P2: the heading, "After 732", is at l.4508-4509. Hers is the only letter of hers in the book: index l.8118; contents l.365-375, 486.
- P3: the four lines are at l.4556-4563. "the rules of poetic art" and Eadburga are at l.4545-4550. Kylie's Thanet is at l.1187-1190.
- P7: Kylie's "The friendship born of this letter led her ... to his service" and "mistress of a convent at Bischofsheim" are at l.1191-1198. The heading "Abbess of Bischopsheim" and Torhthat are at l.4570-4583, "assent and approval" at l.4586, and letter XXXVI at l.5873-5905.
- P9: the last charge and the burial are at l.1758-1777. The Martyrology, "eminent for the gift of miracles", is at BUTE l.71414-71416.
- P11: "Keep thee unharmed in His justice eternal." is verbatim (l.4563).

**Card.** I checked these against their lines: `dates` (l.4509, 4572, 5874); `place`; `legacy.traces` 1 to 4 (l.4576-4586, 1200-1204, 5873-5905, 4389-4428); `legacy.remembered` 1 to 3 (BUTE l.71414-71416; KYLIE l.1187-1192; AASS March 3 l.126315-126328, "ex vita S. Liobae quam xxviii Septembris dabimus, constet aliquot ex monasterio Winburnensi venisse"); `uncertain` 1 to 7. PL 96's Lul letter (l.67962-67967) is the Latin of Kylie's XXI.

**Absence check.** I read every Lioba/Leoba/Leobg-/Leuba/Liuba hit in `cic/texts`. Leuba and Liuba are other people (Gregory of Tours' matron, Visigothic kings, a bishop of Braga), and Lioba Morgan is a sixteenth-century nun. Adam of Bremen (Steinberg) and Parsons hold only bibliography lines. Krusch SRM III holds only a manuscript note. No held line gives her death, her burial or another letter of hers. The README's "one letter of hers and three letters to her" holds (KYLIE XXI, XXIV, XXXVI). The records' absences hold.

#### Findings

- **A-M11 MINOR (card `keyWorks` 1 `about`; a typo).** "the rules she learned from Eadburga.. Kylie gives it" has a double full stop. Fix: "the rules she learned from Eadburga. Kylie gives it in English only".

- **A-M12 MINOR (card `legacy.traces` 4; item 8).** "Lul, who calls himself the servant of Boniface's pupils". This is the card's only mention of Lul, a name a general listener does not know. Kylie: "Lul was to follow him in Mainz" (KYLIE l.1751). Fix: "Lul, who later followed Boniface at Mainz, calls himself the servant of Boniface's pupils. He wrote to her as a sister in Christ." (Two sentences; the next sentence stays.)

- **A-M13 MINOR (card `uncertain` 6; item 4; a printer's mark read aloud).** "The Roman Martyrology puts her, in a bracket, in the eighth century." A participant cannot use "in a bracket". The bracket in Bute marks words added to the Martyrology's text (BUTE l.71414-71415). Fix: "The Roman Martyrology, in Bute's English, places her in the eighth century, in words set in brackets as an addition."

The brief needs no change.

Verdict: NOT CLEAR (0 blocking, 3 minor, all on the card).

---

### Wilfrid of York (338 words, about 2:05; FK 5.6, Flesch 78.9)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-M14, A-M15) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Stephen "from Wilfrid's side"; the card gives Raine's "an enthusiastic partizan") |
| 7 | Contested claims both sides | FAIL (A-M18, A-M19) |
| 8 | Common names | FAIL (A-B4, A-M16, A-M17) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (opens on the reading of Agatho's acts at the 704 hearing) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the Stephen and Bede caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records and absences | FAIL (A-B3, A-M20, A-M21) |

**Sentences checked and found faithful.**
- P1: the reading of Agatho's synod, "who that Bishop Wilfrid was?", and "near forty years, ought not to be condemned" are at GILES l.14093-14123. The quotation is verbatim.
- P2: 709 is reckoned from "the same year" as Coenred's going to Rome (l.13877-13880, 13854-13858, 15387-15388). "Incipit de humili excusatione Stephani presbyteri" is at RAINE l.4007-4009.
- P5: the age of fourteen, Lindisfarne, "the way to virtue taught by the Scots was not perfect", Lyon and the executioners are at GILES l.13893-13989. Ripon from Alfrid is at l.13990-13997, with Oswy's son at l.7924-7925.
- P7: "in a corner of the remotest island" and "the universal church of Christ throughout the world" are verbatim (l.8182-8185). The door-keeper is at l.8205-8206, and 664 at l.8236-8238.
- P9: Bede's "driven from his see by King Egfrid" is at l.15352-15353. Stephen's queen is at RAINE l.6528-6530, and Agatho's decree "Wilfrithus episcopus episcopatum, quem nuper habuerat, recipiat" at l.7273-7280. The South Saxons, "enmity of the aforesaid king" and the fishing are at GILES l.9913-9982. Restoration and the second expulsion are at l.14077-14081.
- P11: Undalum is at l.13878-13883, and "Undalum = Oundle" is Jane's note (l.16040). Forty-five years is at l.13880-13881. Psalm 103, "Emitte spiritum tuum ... renovabis faciem terrae", is at RAINE l.10546-10578.

**Card.** I checked these against their lines:
- `dates`: Eadmer's 634 is at RAINE l.15158-15161 and PL 159 l.55314-55316. Stephen's seventy-sixth year and forty-six years are at RAINE l.10652-10653.
- `keyWorks`: "accusare non audeo" is at l.7185-7187, and the York, Ripon and Hexham petition at l.9015-9020.
- `legacy.traces` 1 to 5: GILES l.8874-8879; RAINE l.5766-5768, 5827-5830, 6428-6444; GILES l.9955-9999; RAINE l.6719-6723; MANSI11 l.30615-30625 ("Vvuilfridus humilis episcopus sanctae ecclesiae Eboracensis").
- `legacy.remembered` 1 to 4: GILES l.14228-14232; RAINE l.1495-1533, 1880-1882; BUTE l.2420, 77757; Prymer l.11536.
- `uncertain` 4 to 8: Pope John's letter at RAINE l.9395-9425; Giles's 12 October at l.14187-14188; Plummer's Latin with no day at l.28657-28658; Mabillon at PL 159 l.55040-55047; thirty and forty families at GILES l.13995, 7938-7940. Plummer's "I cannot say" is at PLUMMER l.3326-3333.

#### Findings

- **A-B3 BLOCKING (card `uncertain` 2; records `contested_claims` 1; item 1; a false absence).** "Stephen alone tells of Queen Iurmenburg's envy, the nine months in prison and the synod at Austerfield." The two later Lives in the same volume tell all three.
  - Fridegod's verse Life: "Quomodo Ermenburgis reginae insidias passus est" (RAINE l.12983); the prison, "Quomodo in carcere lucem promeruit" (l.13626-13781); and the council, "Qualiter dolose ad concilium episcoporum vocatus sit" (l.14067-14072).
  - Eadmer's Life: Ermenburg (l.16806, 17337); the prison (l.17385-17632); and the council "in campo qui dicitur Eastrefeld" (l.18189-18191).
  - Both draw on Stephen (Raine l.2133-2134, 2366-2368). So Bede's silence is the point, not Stephen's being alone.
  - Fix: "What Bede leaves out. Stephen tells of Queen Iurmenburg's envy, the nine months in prison and the synod at Austerfield, and Bede tells none of them. The later Lives by Fridegod and Eadmer, which draw on Stephen, repeat them. Charles Plummer says he cannot tell whether Bede kept silent out of regard for Wilfrid or for the kings."
  - In the records, add the Fridegod and Eadmer lines to the Stephen side, marked as dependent on him.

- **A-B4 BLOCKING (display name and id against the approved era 4 batch 1 Hild profile; items 8 and 10; a namesake collision that misleads).** The approved Hild of Whitby texts call this man "Wilfrid of Ripon". The Hild brief P5 has "which Wilfrid of Ripon had argued", and the Hild card has `uncertain` "Her part against Wilfrid of Ripon". The Hild card's `legacy.traces` 1 uses that name to keep him apart from the other Wilfrid: "this Wilfrid bishop of York ... a different man from Wilfrid of Ripon". The Hild records call Hild's pupil "a later Wilfrid of York". This batch names the Whitby Wilfrid "Wilfrid of York". A participant who reads Hild's card and then opens "Wilfrid of York" will take this profile for Hild's pupil, or think the tree contradicts itself. The pattern's namesake rule ("always carry the place or the epithet the record uses") needs one name per man across the tree. Era 4 is not yet on the live tree and this id is new, so the change is free now.
  - Recommended fix: rename the profile "Wilfrid of Ripon", id `wilfrid-of-ripon`. Ripon is where both Bede and Stephen place his first monastery and his burial (GILES l.13881-13883, 14189-14191; RAINE l.10646-10651).
  - Carry the rename:
    - Brief P2: "He was Wilfrid of York, bishop of York in northern England" -> "He was Wilfrid of Ripon, bishop of York in northern England".
    - Card `name`.
    - Theodore brief P2: "Bishop Wilfrid of York" -> "Bishop Wilfrid of Ripon".
    - Theodore card `legacy.traces` 4 and `uncertain` 1: "Wilfrid of York" -> "Wilfrid of Ripon".
    - Willibrord card `legacy.traces` 4: "Stephen's Life of Wilfrid of York" -> "Stephen's Life of Wilfrid of Ripon".
    - The README names paragraph (A-M25).
  - Alternative: keep "Wilfrid of York" and amend the approved Hild brief, card and records by change order. That touches approved text, so it is the coordinator's call.

- **A-M14 MINOR (brief P9; item 1; two sentences without their witness).**
  - (a) "As bishop of York he built great churches at Ripon and Hexham." This is Stephen's (RAINE l.5827-5830, 6428-6444); Bede gives no such account. Fix: "As bishop of York, Stephen says, he built great churches at Ripon and Hexham."
  - (b) "Wilfrid appealed to Rome, and Agatho's synod ordered him restored." Bede says only that he was acquitted and "declared worthy of his bishopric" (GILES l.14047-14049). The order to restore him is the decree Stephen copies (RAINE l.7273-7280). Fix: "Wilfrid appealed to Rome, and Stephen says Agatho's synod ordered him restored."

- **A-M15 MINOR (brief P5; item 1; the verb overstates).** "At Lyon in Gaul he asked to die with the bishop". Bede: "being very desirous, though the bishop opposed it, to die with him" (GILES l.13983-13985). Fix: "he asked to die" -> "he wished to die".

- **A-M16 MINOR (brief P5 and P9; item 8).** "King Oswy" and "King Egfrid" have no identifier. Bede: "Oswy, king of the Northumbrians" (GILES l.8719, 9250), and Egfrid his son (l.9261-9262). Fix, P5: "At home, Alfrid, King Oswy's son," -> "At home, Alfrid, son of Oswy, king of the Northumbrians,". Fix, P9: "In 678, Bede says, King Egfrid drove him from his see." -> "In 678, Bede says, Oswy's son King Egfrid drove him from his see." P7's "King Oswy" then reads as a second mention.

- **A-M17 MINOR (card `keyWorks` 1; item 8).** "he did not dare accuse Theodore, who had been sent from Rome". This is the card's first mention of Theodore. Fix: "he did not dare accuse Archbishop Theodore of Canterbury, who had been sent from Rome." Then `uncertain` 3's "Archbishop Theodore" stands. (Separately, the card's "Pope John VI": the numeral is in no Wilfrid source. Duchesne holds "Jean VI (701-706)", LP1 l.4384, which fits the 704 hearing. No change is needed, but the records should cite LP1 l.4384 for the numeral.)

- **A-M18 MINOR (card `uncertain` 4; item 7; a contrast the source does not bear).** "In Bede, Wilfrid argues from what the whole church does ... In Stephen he argues from the council of Nicaea". Stephen's Wilfrid also says: "Haec ratio disciplinae Apostolicae sedis est, et pene totius mundi" (RAINE l.5143-5150). "Hild is only the host": Stephen has "presente sanctimoniale matre piissima Hilde" (l.5074-5075), so she is present, not the host. Fix: "Whitby. In Bede, Wilfrid argues from what the whole church does, and Hild's party holds with the Scots. In Stephen he argues from the council of Nicaea and the practice of Rome and nearly the whole world. Stephen names Hild only as present." (Each sentence is 20 words or fewer.)

- **A-M19 MINOR (card `uncertain` 9; item 7; a hedge dropped).** "The anonymous Life of Oswald ... has Oswald find them at Ripon." The Life says Oswald found "praesulis beata membra", "the bishop's blessed limbs" (RAINE l.33983-33985). The identification with Wilfrid is Raine's reading: "in the opinion of the writer the bones were those of Wilfrid senior" (l.2441-2443). Fix: "has Oswald find a bishop's remains at Ripon, which Raine takes for Wilfrid's."

- **A-M20 MINOR (card `otherNames`; the batch rule that other names are forms a vendored source spells).** "Wilfrid of Ripon" is in no file in `cic/texts` (searched). It is the worker's identifier, not a spelled form. Bute spells him "Wilfred" (BUTE l.2420). Fix: `otherNames` -> ["Wilfred", "Wilfridus", "Wilfrithus"]. If A-B4's rename is taken, the display name carries "of Ripon", and "Wilfrid of York" is not added for the same reason.

- **A-M21 MINOR (records).**
  - (a) Five claims are tagged Contested with no `contested_claim`. "Ripon as forty families" needs "Ripon's size, thirty or forty families", with sides GILES l.13995 and l.7938-7940. "Nine months in prison" and "Austerfield" are Stephen's statements that no source denies, so retag them Documented as Stephen's (with A-B3's note). "Eadmer's birth year" is not contested by any held line, since Stephen's seventy-sixth year in 709 agrees with it; retag it Inferential-Thin or Documented as Eadmer's.
  - (b) "Bede on the removal" cites the passive IV.12 (l.9865-9884), while the card says "Bede says King Egfrid drove him out". Add GILES l.15352-15353.

After the fixes (A-B4's P2, A-M14, A-M15 and A-M16 in the brief): 348 words, about 2:09, FK 5.8, Flesch 77.9 (scratch copy scored).

Verdict: NOT CLEAR (2 blocking, 8 minor).

---

### README.md

Checked true:
- The eight ids and the scan sources. Muirchu, Tirechan and Cogitosus are at `Who_Scan_Era4.md` l.35-37; Theodore, Willibrord and Leoba at l.32-34; Wilfrid and Cuthbert at `Who_Scan_Supplement.md` l.187-188.
- No id is a census movement id.
- The word range, 337 to 344.
- The standard-length precedents: Palladius 327, John of Ephesus 320 and Gregory of Tours 324 words, each "about 2 minutes".
- Leoba's one letter and three letters to her.
- The Theodore, Cuthbert, Muirchu ("Muirchu-maccu-Machtheni", White 1920 l.3738-3741) and Leoba name notes.
- Census: Leoba is in the Anglo-Saxon movement's people and voices, Willibrord in its long description, and Cuthbert is not named in the Insular movement.
- Datings: White's "not earlier than a.d. 664, possibly about a.d. 670" (l.1389-1390); Stokes's "A.D. 683, apparently" (OCR "G83", l.3224); "before A.D. 699" for Muirchu (l.3595); Basnage's "multo recentiorem" (PL 72 l.58440-58446); Stokes's "Cogitosus (A.D. 800-835)" (l.21226); and Migne's "ANNO DOMINI DXCI ... EODEM TEMPORE. COGITOSUS" (PL 72 l.58417-58436).

#### Findings

- **A-M22 MINOR (paragraph 3; the reason given as a ruling).** "The coordinator ruled on 2026-11-14 that Anglo-Saxon Christianity already has its four majors in Bede, Boniface, Aidan and Hild, and Insular Irish has Adomnán." The brief carries the call that none of the eight is major, but this reason is not logged in the Decision-Log. "Insular Irish" is not a census name. Adomnán's approved card puts Medieval Irish Christianity first, and the three Irish profiles here sit in Medieval Irish. Fix: "The coordinator called none of the eight major (2026-11-14): Anglo-Saxon Christianity already has four majors in Bede, Boniface, Aidan and Hild, and Medieval Irish Christianity has Adomnán of Iona." Log the call in the batch's Decision-Log entry.

- **A-M23 MINOR (the file table, `card.json` row).** "each entry gives a title, an author where one applies, a language and its file". Every `sources` entry in all eight cards also carries `date`. Fix: "each entry gives a title, an author where one applies, a date, a language and its file under `cic/texts/`".

- **A-M24 MINOR (card traditions, first bullet).** "Every held dating of their work falls after 664". White's is "not earlier than 664", and White also reports Bury's "between a.d. 664 and 668" (l.3598-3599). Stokes's 683 is "apparently". Fix: "Every held dating of their work falls in or after 664, where that movement begins: for Tirechan, White's 664 to about 670, Bury's 664 to 668 as White reports it, and Stokes's 683, "apparently"; for Muirchu, before 699."

- **A-M25 MINOR (names paragraph, Wilfrid; follows A-B4 and A-M20).** If the rename is taken, the paragraph reads: "**Wilfrid of Ripon.** Bede and Stephen make him bishop of York, but the approved Hild of Whitby texts already call him Wilfrid of Ripon, and keep "Wilfrid of York" for Hild's pupil, Wilfrid II, who is named only in the records. Ripon is where both put his first monastery and his grave. The id is `wilfrid-of-ripon`." Delete the sentence that says "Wilfrid of Ripon" is kept under other names.

---

### Verdicts

| Profile | Blocking | Minor | Verdict |
|---|---|---|---|
| Theodore of Tarsus | 2 (A-B1, A-B2) | 5 (A-M1 to A-M5) | NOT CLEAR |
| Willibrord | 0 | 5 (A-M6 to A-M10) | NOT CLEAR |
| Leoba | 0 | 3 (A-M11 to A-M13) | NOT CLEAR |
| Wilfrid of York | 2 (A-B3, A-B4) | 8 (A-M14 to A-M21) | NOT CLEAR |
| README.md | 0 | 4 (A-M22 to A-M25) | NOT CLEAR |
| **Total** | **4** | **25** | |

Every quotation in the four briefs and cards matches its vendored file word for word, folding OCR. The two false absences (A-B1, A-B3) come from one cause: Raine's volume 1 holds Fridegod's and Eadmer's Lives of Wilfrid after Stephen's, and the drafting read only Stephen's. A-B4 is a cross-batch naming collision with the approved Hild of Whitby profile. A-B4's fix changes three files in this batch besides Wilfrid's own.


## R1 review, part B: Muirchu maccu Machtheni, Tirechan, Cogitosus, Cuthbert of Lindisfarne (era 4 Who batch 3)

Reviewer: independent Opus, full effort, first sight of these drafts (commit 00bc3cd4). I edited no profile file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `CLAUDE.md`; `Who_Profile_Pattern.md` checklist 1 to 14; the Decision-Log Who entries of 2026-11-12 to 2026-11-14 with the era 4 batch 1 cap ruling; the rulings block of `Who_Scan_Era4.md`; the era 4 batch 1 R1 review for form. For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, the `records.json` entry and the README. I opened every cited line in its vendored file and read it in context, folding OCR noise, double spaces, hyphen breaks and Migne's interleaved columns.

Files: White 1920 (`patrick_writings-and-life-with-muirchu-eng_white1920.txt`, "WHITE"); Stokes 1887 (`stokes_tripartite-life-of-patrick-v2-lat-muirchu-tirechan-confession_1887.txt`, "STOKES"); Duchesne 1910 (`duchesne_histoire-ancienne-de-leglise-tome3-fra_2e-ed1910.txt`, "DUCH3"); Warren 1895 (`antiphonary-of-bangor-pt2-lat_warren1895.txt`); O'Donovan 1856 (`four-masters_..._odonovan1856.txt`, "FOURM"); PL 72 (`john-biclaro-leander-pl72-lat_migne1878.txt`, "PL72"); Robinson's Eugippius 1914 (`eugippius_life-of-saint-severinus_robinson1914.txt`); Giles/Jane 1903 (`bede_ecclesiastical-history-english-people_giles1903.txt`, "GILES"); AASS March 3 (`acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt`, "AASS3"); Plummer 1896; Raine 1879; Bute's Breviary (`roman-breviary_bute1908.txt`, "BUTE"); the York Prymer.

Absence searches across all of `cic/texts/` (1771 files): Muirchu, Murchu, Machtheni, Maccumacht (hits only in White, Stokes, Warren, Duchesne and one garbled Analecta Bollandiana note on Patrick's death year); Tirechan, Tírechán, Tyrech (no other life detail); Cogitosus, Cogitoso, Cogitosi, Coguitosus (no other witness); Basnage and Canisius with first names; Birr, cáin Adamnáin, lex innocentium, synod of Birr (acts not held, as the records say); Cuthbert in Bede's History for any year of his consecration; Ripon / Inhrypum in AASS3 and Giles; Cuthbert in the Breviary and Prymer.

Readability is `engine.m1.gates.grade_text`, run from the repo root. I applied every suggested brief fix to scratch copies and scored them: `/tmp/claude-0/-home-user-CIC-Project/39eb9bee-a8ba-523c-9dfe-f5ca37666176/scratchpad/fixB/<id>.brief.txt`.

**Applies to all four.**
- Audio: I checked by script that each audio file equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. No tag appears in a brief or card. Every brief fix below must be carried into the audio.
- Cards follow Mark's order; no null or empty field; every `sources` file exists and holds the named work. Muirchu, Tirechan and Cogitosus each have one key work; Cuthbert has none, rightly.
- No list lines are in the drafts, so the list-line half of item 14 was not checked. All four pass the Who test (recorders, and Cuthbert on Bede's two Lives and his cult).
- Length. The drafts run 338 to 342 words, about 2:05 to 2:07, a little past the 2:00 (about 325 words) the coordinator set for standard length. The fixes below add context the briefs need, so three of the four grow by 4 to 17 words. Where the drafter can, trims should come from the scene or witness sentences that the card repeats, never from a caveat. I log this here, not as a finding per profile.
- Doc hygiene, not this thread's: `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md` holds unresolved merge markers (`<<<<<<< HEAD`, `=======`, `>>>>>>> origin/main`) around the era 4 batch 1 entries. Flagged for the coordinator; not touched.

---

### Muirchu maccu Machtheni (standard; 342 words, about 2:07; FK 5.6, Flesch 76.1)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-M2, B-M7, B-M9, B-M10) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | FAIL (B-M1: an inner state) |
| 4 | Reading aids | FAIL (B-M1, B-M3, B-M6) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (none partisan beyond White's own Armagh reading, given as his) |
| 7 | Contested claims both sides | FAIL (B-M4: Loiguire's belief) |
| 8 | Common names | FAIL (B-M3: Sletty, Birr synod; B-M5) |
| 9 | One term for one thing | FAIL (B-M5: Aed / Aedh across published profiles) |
| 10 | Story, scene, disputes in place, length | FAIL (B-M4: festival dispute set apart from the fire) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 opens with the brief's "little is told") |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (B-M8) |

**Sentences checked and found faithful.**
- P1: the preface is at WHITE l.3790-3812. "the infantile row- boat of my feeble brain" (hyphen break), "save only that of my father Cogitosus" and "My skill is small; my authorities are uncertain" are verbatim; White's bracket "[or anonymous]" (OCR "[pty anonymous]") is rightly left out of a quotation that stops before it.
- P2: "most ancient Life of the Saint now extant" and the first book before 699 are at l.3591-3596. Duchesne's "dédiée à un évêque qui mourut en 698" is at DUCH3 l.22836-22837. "At the command" is the preface's "in obedience to the command of thy holiness" (l.3807) and the name note's "under the direction of Aedh, Bishop of the city of Slebte" (l.5232-5234).
- P3: Leinster and Birr are at l.3753-3770; Graves's "Coguitosi for cognito si, is now generally accepted" and the Brigid identification are at l.3741-3751.
- P4: the edict, the fire on the plain and the magicians' warning are at l.4383-4407, verbatim; "It is better for me to believe than to die." is at l.4741-4742.
- P5: Aedh's submission and the "literary tribute from Leinster to Armagh" are at l.3772-3777; Bury and Macalister at l.6751-6757.
- P6: l.5416-5419, verbatim.

**Card.** I checked these against their lines: `knownFor`; `dates` (l.3594-3596; DUCH3 l.22836); `place` (l.3753-3768); `keyWorks` (two MSS, l.3603-3612); `traces` 2 (l.1532-1536) and 3 (Warren l.9790-9798 on the Paschal fire; l.10595-10597, "probably had the fourth stanza of St. Sechnal's Hymn"); `remembered` 1 (l.884-886), 2 (l.6342-6343, 6359) and 3 (l.6915-6917); `uncertain` 2, 3, 5 and 6. The records' absences (Stokes's pages 269-271 missing from the held file; the acts of Birr not held) are true. The published Adomnán of Iona card agrees on Birr and on the acts not being held.

#### Findings

- **B-M1 MINOR (brief P1; items 3 and 1; an inner state, and a word changed).** "began by doubting himself" states a feeling the preface does not. What Muirchu does is apologize for his skill, closing "yet the feeling of my love is most pious" (l.3812). "one sure track through the story" changes White's "one sure track of history" (l.3794-3795). Fix: "A writer setting out to tell the life of Saint Patrick began by doubting himself. Many had tried before him, he wrote, and none had found one sure track through the story." -> "A writer setting out to tell the life of Saint Patrick began with an apology for his own skill. Many had tried before him, he wrote, and none had found one sure track of history."

- **B-M2 MINOR (brief P2 and card `uncertain` 3; item 1; hedge dropped, and "gives 698" reads as Duchesne's date for the Life).** White says "The first book, at least, must have been published before A.D. 699" (l.3594-3596). Duchesne gives the year the bishop died, not a date for the Life. Fix: "White dates it before Aed's death in 699, while Louis Duchesne, the French church historian, gives 698." -> "White dates at least the first book before Aedh's death in 699. Louis Duchesne, the French church historian, puts that death in 698." (Spelling per B-M5.)

- **B-M3 MINOR (brief P2-P3; items 4 and 8; a stock opener with no witness, and places with no context).**
  - (a) "Of his own life little is told." is a witnessless passive, and the same sentence opens Tirechan's P3 (B-M13); heard one after the other on the Medieval Irish tree, it reads as a template. Fix: -> "Muirchu says almost nothing about himself." The card's `uncertain` 1 already opens "Little is told of his own life", which still matches.
  - (b) "Sletty" means nothing to a listener. White places it "on the borders of Co. Carlow" (l.3767) and reads Aedh as Leinster's (l.3776-3777). Fix: "He wrote at the command of Aed, bishop of Sletty." -> "He wrote at the command of Aedh, bishop of Sletty, in Leinster."
  - (c) The synod is White's "Synod held at Birr, by Adamnan" (l.3768-3769), and the published Adomnán of Iona card calls it "Adomnán's synod at Birr". Fix: "White makes him a Leinster man, and says he and Aed both signed the acts of a synod at Birr, between 695 and 697." -> "White says he and Aedh both signed the acts of Adomnán's synod at Birr, between 695 and 697." (The Leinster reading stays on the card, `place` and `uncertain` 4, and in P5's "tribute from Leinster"; dropping it here also brings the sentence from 24 to 19 words.)

- **B-M4 MINOR (brief P4-P5; items 7 and 10; a contested point told one way, and a dispute set apart from its scene).**
  - (a) The brief ends the fire on Loiguire's "It is better for me to believe than to die", and the listener hears a conversion. White's note on that very chapter says Tirechan's account "is both more credible than that of Muirchu": Loiguire "was unable to believe" (l.6915-6921), and White's note on Chapter X says he "tolerated Christianity, though he did not embrace it himself" (l.6555-6557). The card has it (`remembered` 3); the brief does not. It is not blocking only because the line is told as Muirchu's.
  - (b) The Bury/Macalister dispute in P5 sits apart from the fire it is about, and as written it lacks the point: Bury says Muirchu "(or his source)" joins two festivals "on neither of which Easter could fall" (l.6751-6753). The card's `uncertain` 6 carries both sides fully, so the brief can leave it there.
  - (c) "Temoria" has no gloss. White: "Temoria = Tara" (l.6548).
  - Fix, P4 and P5 together: "Muirchu tells of Patrick's Easter fire. On that night, he says, no one might light a fire before the king's own at the palace of Temoria. Patrick lit one on the plain. The king's magicians warned that unless it was put out that night, "it will not be put out for ever." At last King Loiguire told his elders, "It is better for me to believe than to die."\n\nWhite says Aed submitted to the claims of Armagh's bishop to head the Irish church. He reads the Life as a tribute from Leinster to Armagh. Professor Bury, in his book on Patrick, held that Muirchu joined two heathen festivals into one by a clever device. R. A. S. Macalister defends Muirchu's account." -> "Muirchu tells of Patrick's Easter fire. On that night, he says, no one might light a fire before the king's own at Temoria, which White calls Tara. Patrick lit one on the plain. The king's magicians warned that unless it was put out that night, "it will not be put out for ever." At last King Loiguire told his elders, "It is better for me to believe than to die."\n\nTirechan, who also wrote on Patrick, says the king was unable to believe, and White finds that account more credible. White also says Aedh submitted to the claim of Armagh's bishop to head the Irish church. He thinks the Life was probably a tribute from Leinster to Armagh."
  - This also restores White's hedge, "it is probable that Muirchu's Life ... was inspired by a desire to offer a literary tribute" (l.3774-3777), which "He reads the Life as a tribute" dropped. Add a `contested_claim` to the records: "Whether Loiguire believed", sides "Muirchu: he believed (WHITE l.4741-4744)" and "Tirechan, preferred by White: he was unable to believe (WHITE l.6915-6921)".
  - Card `uncertain` 6, to match: "held that Muirchu joined the features of two heathen festivals" -> "held that Muirchu, or his source, joined the features of two heathen festivals"; and "R. A. S. Macalister defends Muirchu's account." -> "R. A. S. Macalister, in his study of Tara, defends Muirchu's account." (l.6550-6553).

- **B-M5 MINOR (brief and card throughout; items 8 and 9; one man, two spellings across published profiles).** The approved Adomnán of Iona card names him "Aedh of Sletty", White's form (l.3767, OCR "^dh"). This profile uses "Aed", Stokes's (l.5344). Fix: "Aed" -> "Aedh" in the brief (P2, P3, P5) and on the card (`knownFor`, `dates`, `place`, `keyWorks`, `uncertain` 3 and 5), or log the drift if the coordinator prefers Stokes.

- **B-M6 MINOR (card `knownFor`, `keyWorks`; item 4).**
  - (a) "An Irish writer who wrote a Latin Life" -> "An Irish author of a Latin Life of Saint Patrick, written at the command of Aedh, bishop of Sletty." (the rest of the field as it stands).
  - (b) `keyWorks` "the Easter fire against the king's at Temoria, the contest with the magicians and his death and burial.. White says" -> "the Easter fire lit before the king's at Temoria, the contest with the magicians, and his death and burial. White says" (a double stop, and a phrase that does not parse).

- **B-M7 MINOR (card `uncertain` 1 and README; item 1).** White says the name is "given in the note appended to the Table of Contents of Book i. (printed here at the end of that book)" (l.3738-3740). Fix: "White gives his name from a note at the end of the first book" -> "White gives his name from a note to the first book's table of contents, which he prints at the end of that book". README: "from the note at the end of the first book" -> "from the note to the first book's table of contents".

- **B-M8 MINOR (card `uncertain` 7 and records; items 12 and 1; an item with no uncertainty, and a misused tag).** "The place of the fire. Muirchu sets it at the Graves of the Men of Fecc. White's note places them near Slane." names no doubt and no second side, yet the record is tagged Contested with no `contested_claim`. Fix: delete it from `uncertain`, or fold the gloss into `keyWorks` ("the Easter fire, which Muirchu sets at the Graves of the Men of Fecc, near Slane in White's note"); retag the record Dominant Modern Reconstruction (White's gloss, l.6740-6741).

- **B-M9 MINOR (card `traces` 1; item 1).** "three of the later Latin Lives" — White counts them among "seven ancient Lives" that John Colgan printed at Louvain in 1647, and does not call them Latin or later (l.1468-1474, 1527). Fix: -> "Newport White says three of the seven ancient Lives of Patrick that John Colgan printed in 1647 are largely based on Muirchu."

- **B-M10 MINOR (card `traces` 3 and `uncertain` 4; items 8 and 1).**
  - (a) "a stanza of the Hymn of Sechnall" gives no context. Warren calls it "St. Sechnal's Hymn", the hymn of St. Secundinus (l.10589-10596). Fix: "the Hymn of Sechnall" -> "the hymn of Saint Sechnall, or Secundinus". White makes the same point himself: "Muirchu exhibits familiarity with the Hymn of St. Sechnall" (l.3779-3780), which the card may add.
  - (b) "and places him at Birr" goes past White, who says only that he "subscribed the Acts of the Synod held at Birr" (l.3768-3769). Fix: -> "and says he signed the acts of Adomnán's synod at Birr."

After the fixes (B-M1 to B-M5 in the brief): 342 words, about 2:07, FK 6.2, Flesch 75.0 (scratch copy scored).

**Verdict: REVISE (0 blocking, 10 minor).**

---

### Tirechan (standard; 341 words, about 2:06; FK 7.1, Flesch 70.1)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-M11, B-M12, B-M15) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M13) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS |
| 7 | Contested claims both sides | PASS (the date, White and Bury against Stokes, in P2) |
| 8 | Common names | PASS (Ultan, Ferdomnach, Duchesne identified; see B-M16 on the card) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (B-M17) |

**Sentences checked and found faithful.**
- P1: "Cor autem meum cogitat in me de Patricii dilectione, quia uideo desertores et archiclocos et milites Hiberniae quod odio habent paruchiam Patricii, quia substraxerunt ab eo quod ipsius erat, timentque quoniam, si quaereret heres Patricii paruchiam illius, potest pene totam insolam sibi reddere in paruchiam" (STOKES l.2974-3015, OCR folded). "Paruchia ... the churches under his authority" stands on Stokes's "i.e., the diocese" (l.3060) and White's "sphere of authority of the See of Armagh, the paruchia Patricii" (WHITE l.1403-1404).
- P2: Ferdomnach and 807-846 at WHITE l.1532-1536; "not earlier than a.d. 664, possibly about a.d. 670" at l.1388-1390; Stokes's "A.D. 683, apparently." at STOKES l.3224, on "post mortalitates nouissimas" (l.3187-3189).
- P3: the heading "Tirechan episcopus haec scripsit ex ore uel libro Ultani episcopi cuius ipse alumpnus uel discipulus fuit" (l.2212-2213); the four names "in libro adscripta Patricio apud Ultanum" (l.2214-2215); "Ultano ... qui nutriuit me" (l.2972-2974); Ardbraccan and Tirawley at WHITE l.1390-1393.
- P4: White on the itinerary and purpose at l.1402-1408. Mount Egli at l.594-597 and the well at l.7100-7112, both verbatim.
- P5: "I have seen it with mine own eyes" at l.6825-6828, verbatim; "near Tara" is White's bracket "[of Tara]", and the brief says "in White's English". "Often" holds: in the Latin, Tirechan also says "conspexi illum oculis meis" and "tres patinos quadratos uidi" (STOKES, the Tirechan section, about l.2655 and l.3121).
- P6: "an honest author who had no gift of composi- tion" at WHITE l.1439-1441, verbatim.

**Card.** I checked these against their lines: `knownFor` (l.1391-1393); `dates` (Bury at l.3596-3599); `place`; `keyWorks` (Gwynn via White, l.1423-1431); `traces` 2 (l.1399-1400) and 3 (FOURM l.5409-5410, with two more uses at l.5361 and l.6020, so "boundaries" is right); `remembered` 1 and 2; `uncertain` 2, 3 and 5 (l.1166-1172). Duchesne's Ultan "mort en 656" is at DUCH3 l.22835.

#### Findings

- **B-M11 MINOR (brief P1; item 1; a pronoun that changes the sense, and a group dropped).** "if Patrick's heir claimed them" — the Latin is "si quaereret heres Patricii paruchiam illius", if Patrick's heir sought his paruchia. "Them" points back to the deserters. The list also drops "milites Hiberniae", the warriors of Ireland, and Stokes's index renders "archiclocos" as "archrobbers" (l.20664). Fix: "He saw deserters and robbers in Ireland who hated" -> "He saw deserters, arch-robbers and warriors of Ireland who hated"; and "if Patrick's heir claimed them, he could" -> "if Patrick's heir claimed that paruchia, he could".

- **B-M12 MINOR (brief P6 and card `remembered` 3; item 1; Duchesne's reasoning misread).** The brief makes "the interests of Armagh" a second thing the book holds. Duchesne says that in what can be credited to Tirechan "il n'y a guère que des traditions locales, déjà très embellies par deux siècles de conservation orale", because Irish memory worked hard: "il s'agissait de l'apôtre national, et aussi des intérêts de l'église d'Armagh" (DUCH3 l.22846-22852). Armagh's interest is why the traditions grew. Fix, brief: "saw in it little but local traditions, much embellished, and the interests of Armagh." -> "saw in it little but local traditions, much embellished over two centuries of telling, with Armagh's interests at stake." Card: "finds in it little but local traditions and the interests of Armagh. He says two centuries of telling had much embellished them." -> "finds in it little but local traditions. He says two centuries of telling had much embellished them, since they touched the national apostle and the interests of Armagh."

- **B-M13 MINOR (brief P3; item 4).** "Of his own life little is told." is the same witnessless opener as Muirchu's P3 (B-M3). Fix: -> "Tirechan tells little of himself."

- **B-M14 MINOR (brief P2; item 1).** "takes a plague it mentions" — the Latin is plural, "post mortalitates nouissimas", and the card's `uncertain` 2 already says "plagues". Fix: "takes a plague it mentions to be that of 683" -> "takes the latest plagues it mentions to be those of 683".

- **B-M15 MINOR (card `traces` 1 and `uncertain` 4; item 1; two hedges dropped).**
  - (a) White: the book in Ultan's keeping "would be the earliest attempt to give an account of Patrick of which we have any knowledge" (l.1396-1398). Fix: "White calls the book ... the earliest attempt" -> "White says the book ... would be the earliest attempt".
  - (b) White says the Saul note "was probably due to the scribe" (l.7417-7418). Fix: "White gives the note on Patrick's burial at Saul to Ferdomnach too." -> "White thinks the note on Patrick's burial at Saul probably Ferdomnach's too."
  - (c) In the same item, "Duchesne credits Tirechan with nothing past page 331 of Stokes" gives the participant a page number with no meaning. Fix: -> "Duchesne will not credit Tirechan with the last part of the text, and says both early works had been reworked before the Book of Armagh was copied." (DUCH3 l.22842-22846: "avaient déjà, à cette date, subi quelques retouches ou compléments").

- **B-M16 MINOR (card `uncertain` 6; items 8 and 4).** "the familia of "Clono"" and "Cluain maccu Nois" are opaque, and "asks ... with a question mark" says one thing twice. White spells the place "Clonmacnois" (l.8554). Fix: -> "The church that seized Patrick's places. Tirechan says the community of "Clono" holds many of them by force since the latest plagues. Stokes suggests Clonmacnoise, with a question mark in his note." (STOKES l.3187-3189, 3219.) Spell it "Clonmacnois" if White's form is preferred.

- **B-M17 MINOR (records; formation tags).**
  - (a) Ultan's death, White 657 against Duchesne 656, is on the card (`uncertain` 3) but has no `contested_claim`. Add one: "The year Ultan died", sides "Newport White: 657 (WHITE l.1393-1394)" and "Louis Duchesne: 656 (DUCH3 l.22835)".
  - (b) The Clono record is tagged Contested with no sides; Stokes's query is an uncertain reading, not a dispute. Retag Inferential-Thin.

- **B-M18 MINOR (README; item 1).** "White's 664 to about 670 and Stokes's 683 for Tirechan" misstates White, who gives "not earlier than a.d. 664, possibly about a.d. 670" (l.1388-1390); the 664-668 range is Bury's (l.3596-3599). Fix: -> "White's no earlier than 664, possibly about 670, Bury's 664 to 668, and Stokes's 683 for Tirechan".

Not a finding: the brief never names the work (Memoir, Collections, Memoranda). "Notes" and "book" are plain and consistent enough for a listener, and the card names it.

After the fixes (B-M11 to B-M14 in the brief): 346 words, about 2:08, FK 7.5, Flesch 68.0 (scratch copy scored).

**Verdict: REVISE (0 blocking, 8 minor).**

---

### Cogitosus (standard; 338 words, about 2:05; FK 7.5, Flesch 68.6)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-B1, B-M19, B-M22, B-M24) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M20, B-M23) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS |
| 7 | Contested claims both sides | FAIL (B-B1, on the card) |
| 8 | Common names | FAIL (B-M21) |
| 9 | One term for one thing | FAIL (B-M23: Tirechan's "paruchia" for Cogitosus's "parochia") |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats "a saint's Life, mostly miracles") |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (B-B1, B-M25) |

**Sentences checked and found faithful.**
- P1: the church, PL72 l.59384-59460: the two tombs "a dextris et a sinistris altaris", "coronis aureis et argenteis desuper pendentibus", "decorata pictis tabulatis", "unus paries decoratus, et imaginibus depictus", the bishop's door "ad altare" and the abbess "cum suis puellis et viduis fidelibus", and "populus grandis in ordine ... uno animo Dominum omnipotentem orat".
- P2: "ANNO DOMINI DXCI ... EODEM TEMPORE. COGITOSUS" (l.58415-58436). Basnage: "multo recentiorem credimus illum scriptorem"; Cogitosus heard of the living Brigid's miracles "a majoribus tantum ..., non viderat ipse"; the painted images "quae posteriora redolent saecula" (l.58442-58479, two columns interleaved).
- P3: the prologue, "Cogisti me, fratres", "parvitatis et ignorantiae meae ... minime convenit", "pauca de pluribus, a majoribus et peritissimis tradita" (l.58492-58501).
- P4: headship and "a mari usque ad mare" (l.58506-58510); the hermit "de eremo" (l.58513-58518); "Archiepiscopus ... et abbatissa ... felici successione et ritu perpetuo dominantur" (l.58526-58527); "civitas est refugii tutissima ... in qua servantur thesauri regum" (l.59474-59482).
- P5: White l.3741-3751, and Stokes's index "Cogitosus (A.D. 800-835), 269." (STOKES l.21226).
- P6: "Orate pro me Cogitoso nepote culpabili" (l.59502, OCR "culpabiH"); Basnage's "Qua ratione igitur se nepotem appellaverit, nobis aeque ac Canisio incertum" (l.58451-58455).

**Card.** I checked `keyWorks`; `traces` 1-3; `remembered` 1 (Basnage, "tota miraculis scatet" and "stylus barbariem saeculi quo vixit indicat", l.58442-58447); `uncertain` 1, 3, 4 and 6. The notes signed "Can." in the Life (e.g. l.59521) bear out "Canisius's notes" in `sources`. Consistency: the approved Brigid of Kildare card (era 3 batch 2) tells Basnage, White and Stokes the same way, apart from B-B1 and B-M24.

#### Findings

- **B-B1 BLOCKING (card `uncertain` 5 and records `contested_claims` 2; items 1 and 7; an index read as a witness against the identification).** The card says Stokes's index "lists the father in Muirchu's preface separately, as "Coguitosus"", and the records make that the "Against, by implication" side of whether Cogitosus is Muirchu's father. Both index entries point to the same page. "Cogitosus (A.D. 800-835), 269." (STOKES l.21226) and "Coguitosus, 269." (l.22198) both cite page 269, which the index gives as the start of "Muirchu Maccumachtheni, notes by, 269" (l.21487), that is, the preface. So Stokes's dated "Cogitosus" entry is itself attached to Muirchu's preface. The page is not in the held file (records `absent_details` 3), so no held line shows whether Stokes accepted or rejected the identification. "Separately" tells the participant he rejected it. Fix, card: "The same index lists the father in Muirchu's preface separately, as \"Coguitosus\"." -> "Both his index entries, \"Cogitosus\" and \"Coguitosus\", point to the page with Muirchu's preface, which is not among the held pages." Records: replace the "Against, by implication" side with "Whitley Stokes's index: Cogitosus, A.D. 800-835, entered at p.269, the page of Muirchu's preface, which is not held; his reasoning cannot be read (STOKES l.21226, 22198, 21487)". If that leaves no real second side, drop the second `contested_claim` and keep the date dispute (the first), which stands.

- **B-M19 MINOR (brief P2 and card `knownFor`; item 1; an unsourced superlative).** "is the main source for her" has no held witness. The census voice line says "everything written about her comes long afterwards", and the era 3 Brigid card says "Her life rests on Cogitosus's Life", but no vendored line ranks the sources. Fix, brief: "The writer was Cogitosus, and his Latin Life of Brigid of Kildare is the main source for her." -> "The writer was Cogitosus, who wrote a Latin Life of Brigid of Kildare." Card: "Writer of a Latin Life of Brigid of Kildare, the main source for her." -> "Writer of a Latin Life of Brigid of Kildare."

- **B-M20 MINOR (brief P2; item 4; an unclear "he").** "Basnage ... thought him much later. He did not see Brigid alive, Basnage argues" — the first "He" after Basnage as subject reads as Basnage. Fix: "He did not see Brigid alive, Basnage argues," -> "Cogitosus did not see Brigid alive, Basnage argues,".

- **B-M21 MINOR (brief P2, card `dates` and `uncertain` 6; item 8; namesakes and an unknown name).** Two Basnages are held: Jacques (e.g. Alcuin PL 100-101 l.25609; Robinson's Eugippius l.4384) and Samuel. Robinson names Jacques Basnage as the editor of "the second edition of Canisius ... Thesaurus Monumentorum", the work Migne cites at the head of the note ("Canis., Thesaurus monum. tom. I", PL72 l.58438). Canisius is unexplained on the card. Fix: brief "Basnage, whose note Migne prints," -> "Jacques Basnage, whose note Migne prints,"; card `dates` "Basnage thought him much later." -> "Jacques Basnage thought him much later."; card `uncertain` 6 "as uncertain to him as to Canisius." -> "as uncertain to him as to Henricus Canisius, whose collection Basnage re-edited." Add Robinson's Eugippius to `sources.about` if the identifier needs its file listed.

- **B-M22 MINOR (brief P3 and card `place`; item 1; narrowed).** Cogitosus says the miracles go on "in suo monasterio ubi ejus venerabile requiescit corpus ... quas nos virtutes non solum audivimus, sed etiam oculis nostris vidimus" (l.59334-59338): in her monastery, where her body rests, not at her tomb. The miracle he then tells is of a millstone. Fix, brief: "He has seen miracles at her tomb with his own eyes, he adds." -> "He has seen miracles with his own eyes, he adds, in the monastery where her body lies." Card `place`: "where he says he saw miracles at Brigid's tomb" -> "where he says he saw miracles in the monastery where Brigid's body lies".

- **B-M23 MINOR (brief P4 and P6; items 4 and 9; an undefined term and untranslated Latin).**
  - (a) "paruchia" is undefined in this text and is Tirechan's spelling; Cogitosus writes "parochia" (l.58506). Stokes glosses the word as "Jurisdiction" (STOKES l.20166). Fix: "with its paruchia reaching across Ireland from sea to sea." -> "its jurisdiction reaching across Ireland from sea to sea."
  - (b) The signature is read aloud in Latin, and only "nepos" is then explained. Fix: "to pray for \"Cogitoso nepote culpabili\"." -> "to pray for \"Cogitoso nepote culpabili\", Cogitosus the guilty nepos."

- **B-M24 MINOR (brief P5, card `uncertain` 2 and `remembered` 2; item 1).**
  - (a) Brief: "which would place him before about 700" does not say what the inference rests on; White never gives that date. The records tag it Inferential-Thin, "computed from White's placing of Muirchu at Birr". Fix: "takes that father for Brigid's biographer, which would place him before about 700." -> "takes that father for Brigid's biographer. Since White puts Muirchu in the 690s, that would place Cogitosus before about 700."
  - (b) Card `uncertain` 2: "Basnage writes that he places Cogitosus there following others" ties Basnage's "Cogitosum hic reponimus, aliorum vestigiis insistentes" (l.58442) to Migne's 591. Basnage wrote it for his own edition, and the records' own `absent_details` 4 says the held lines do not show where that was. Fix: -> "Basnage writes that he places Cogitosus where he does following others, not on his own view, for he believes him much later." (The approved Brigid card's "says that placing follows others" has the same reading; log it in Open-Gaps against that card rather than reopen it.)
  - (c) `remembered` 2: "He adds that she sowed the word among all by custom" makes Basnage the source. He is astonished at what Cogitosus says: "Stupendum etiam, virginem saluberrima semina verbi dominici ex more consuetudinis omnibus seminasse" (l.58460-58466). Fix: -> "He is astonished too that, as Cogitosus tells it, she sowed the word among all by custom, and says these things go against the laws."

- **B-M25 MINOR (README; tradition reasoning).** "White's reading puts him before about 700, and Stokes gives 800 to 835, so Medieval Irish goes first": a date before about 700 does not favor Medieval Irish (from 664) over Insular (to 664). The call stands on Basnage and Stokes. Fix: -> "Basnage thought him much later than Brigid and Stokes gives 800 to 835, so Medieval Irish goes first; White's reading, before about 700, falls on either side of 664." Also in records `absent_details` 4, align with B-M24 (b).

After the fixes (B-M19 to B-M24 in the brief): 348 words, about 2:09, FK 7.8, Flesch 65.5 (scratch copy scored).

**Verdict: REVISE (1 blocking, 7 minor).**

---

### Cuthbert of Lindisfarne (standard; 338 words, about 2:05; FK 5.7, Flesch 78.9)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-B3, B-M28, B-M30) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Plummer's judgment of Bede on the card) |
| 7 | Contested claims both sides | FAIL (B-B2) |
| 8 | Common names | FAIL (B-M26) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | FAIL (B-B2: the vision's dispute is not told in place) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats "saints' Lives, full of miracles") |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (B-B2, B-M31) |

**Sentences checked and found faithful.**
- P1: Bede's prose Life, AASS3 l.34310-34352: "remotis in montibus commissorum sibi pecorum agere custodiam", "vidit subito fusum de caelo lumen", the choirs and the soul, "mane facto ... Aidanum ... per id temporis, quo viderat, raptum de corpore", and "commendans suis pecora quae pascebat dominis, monasterium petere decrevit".
- P2: Bollandists and Raine on the earlier Life (AASS3 l.32844-32854; Raine l.1741-1743); Plummer on "ascetic and miraculous" (l.3349-3364).
- P3: horse and spear, Boisil at the door, "hoc unum dixit adstantibus: Ecce servus Dei" (AASS3 l.34437-34446); Melrose on the Tweed and the Scriptures (GILES l.11575-11586); prior after Boisil (AASS3 l.34909-34913; GILES l.11587-11588).
- P4: Eata and the Scots' leaving (GILES l.8254-8257); the move to Lindisfarne (l.11640-11646); "see nothing but heaven" (l.11728-11732).
- P5: Twyford, Theodore, letters, Egfrid, Trumwine, the kneeling and tears (GILES l.11732-11748; AASS3 l.36455-36466).
- P6: two years and the return (GILES l.11798-11801); Herefrid as Bede's witness (AASS3 l.37455-37459); the last words (l.37776-37796; Bute's English at BUTE l.106680-106691).
- P7: GILES l.11905-11921, verbatim.

**Card.** I checked `otherNames` ("Cuthbertus", AASS3 l.34347); `knownFor`; `place` (Ripon: AASS3 l.34606-34615; Farne's distance, GILES l.11568-11571); `traces` 1 (AASS3 l.33667-33671), 2 (l.35625-35641), 3 (GILES l.12099-12105) and 4 (Raine l.1749-1753); `remembered` 1 (l.11960-11962), 2 (Alcuin, AASS3 l.40836-40846), 3 (BUTE l.1734, 61466-61473) and 4 (Prymer l.3963, 11540); `uncertain` 1, 2 (Alcuin and Raine's note, Raine l.27458-27461, 27515-27516; Plummer l.10507-10624), 3, 5 and 6. The namesake records (Bede's pupil; the archbishop of Canterbury) are right.

#### Findings

- **B-B2 BLOCKING (brief P1-P2, card and records; items 7 and 10; a contested point told one way, against an approved profile).** The brief tells Bede's timing as the scene: "In the morning he learned that Aidan ... had died at that hour." The Lindisfarne monk's Life, which the brief names in the next paragraph, says the news came "post paucas dies", some days later (AASS3 l.38829-38832). Era 4 batch 1's R1 made exactly this point blocking on Aidan of Lindisfarne, and the approved Aidan brief and card now tell both sides, with a `contested_claim` ("When Cuthbert learned that the soul he saw was Aidan's"). Fix, brief P2: "A monk of Lindisfarne wrote an earlier Life. Both are saints' Lives, full of miracles." -> "A monk of Lindisfarne wrote an earlier Life, in which the news came some days later. Both are saints' Lives, full of miracles." Card: add to `uncertain`, after item 1: "Aidan's death. Bede's prose Life says Cuthbert learned of it the next morning. The Lindisfarne monk says the news came some days later." Records: copy the Aidan `contested_claim` and its two claims (AASS3 l.34343-34352; l.38813-38832).

- **B-B3 BLOCKING (card `dates` and `uncertain` 4; a false absence).** "The years 685 and 687 are the Bollandists'" and "Bede gives the day ... and two years as bishop". Bede's own History dates the election and consecration. IV.27 opens: "The same year that King Egfrid departed this life, he ... promoted to the bishopric of the church of Lindisfarne the holy and venerable Cuthbert" (GILES l.11559-11568). IV.26 sets Egfrid's death in the year after 684, with Cuthbert "who had been lately ordained bishop" (l.11467, 11480-11488). Bede's chronicle in V.24 reads "In the year 685, Egfrid, king of the Northumbrians, was slain." (l.15365-15366). Easter 685, two years and a death on 20 March give 687, which is what the Bollandists reckon (AASS3 l.32808-32815). Giles's bracketed "[A.D. 685.]" and "[a.d. 687.]" (l.11557, 11816) are the edition's, and should not be cited. Fix, `dates`: "Bede says he was consecrated at Easter, after the synod at Twyford, and died on 20 March after two years as bishop. The Bollandists, who print his Lives, give the years as 685 and 687." -> "Bede says he was made bishop in the year King Egfrid was killed, which Bede gives as 685. He was consecrated at Easter and died on 20 March, after two years as bishop. The Bollandists, who print his Lives, give 687." `uncertain` 4: "The years. Bede gives the day of his death, 20 March, and two years as bishop after an Easter consecration. The years 685 and 687 are the Bollandists'." -> "The year of his death. Bede gives the day, 20 March, and two years as bishop after an Easter consecration in 685. The year 687 is the Bollandists' reckoning." (Or delete the item, since `dates` now carries it.) Records: add a Documented claim for GILES l.11559-11568 and l.15365-15366.

- **B-M26 MINOR (brief P5; item 8).** "King Egfrid" and "Bishop Trumwine" have no identifier. Bede: "Egfrid, king of the Northumbrians" (GILES l.15365) and Trumwine set over "the province of the Picts" (l.9899). Fix: "King Egfrid crossed to Farne with Bishop Trumwine and the brothers." -> "King Egfrid of Northumbria crossed to Farne with Bishop Trumwine and the brothers." (Trumwine may stay bare: he is named once, and "bishop" places him.)

- **B-M27 MINOR (brief P4; item 10; context the last words need).** P4 names "the meeting at Whitby in 664" without saying what it decided, and P6 rests on it ("those who keep Easter at the wrong time"). Bede: the disputation was on the Catholic Easter, and King Oswy ruled for Peter's side (GILES l.8195-8238). Fix: "After the meeting at Whitby in 664, the Scots," -> "After the meeting at Whitby in 664, where King Oswy chose the Roman Easter, the Scots,". (Optional, at the drafter's weight against length.)

- **B-M28 MINOR (brief P6; item 1; narrowed).** The last words condemn those who stray "ab unitate Catholicae pacis, vel Pascha non suo tempore celebrando vel perverse vivendo" (AASS3 l.37779-37783): by keeping Easter at the wrong time or by living wickedly. The brief keeps only Easter. Fix: "and have no fellowship with those who keep Easter at the wrong time." -> "and have no fellowship with those who leave Catholic unity, by keeping Easter at the wrong time or by living wickedly." (Optional if B-M27 is taken and length is tight; then add it to the card.)

- **B-M29 MINOR (held material not used; card `uncertain`).** Bede's prose Life says Eata took Cuthbert among the brothers who founded Ripon (AASS3 l.34606-34615). Bede's History says the king had given Ripon "to those that followed the doctrine of the Scots", who "would rather quit the place than adopt the catholic Easter" (GILES l.13996-14001). The Bollandists join the two and say Eata, Cuthbert and the rest left Ripon over the Catholic Easter (AASS3 l.33598-33602). This is the one held event that puts Cuthbert on the Irish side of the question he condemns at his death. It is not a false absence, since no line of the profile denies it. Fix: add to `uncertain`: "Ripon. Bede says Eata took Cuthbert to found a monastery at Ripon. His History says the founders left rather than take the Roman Easter. The Bollandists count Cuthbert among them; Bede does not say so of him." Add `place` "Ripon" its reason, and add V.19 to the History's `sources` title.

- **B-M30 MINOR (card `traces` 2, `uncertain` 7; items 8 and 1).**
  - (a) `traces` 2 is the card's first "Eata", bare. Fix: "Bede says Eata moved him" -> "Bede says Eata, abbot of Melrose, moved him".
  - (b) `uncertain` 7 gives half the Bollandists' reason and names no uncertainty. They left out the verse Life "quia illud extat excusum, et moles videtur nimium excrescere" (AASS3 l.38586-38591): because it was in print and the volume was growing too large. Fix: delete the item, or -> "The Bollandists left out Bede's verse Life, since it was already in print and their volume was growing too large."

- **B-M31 MINOR (records; formation tag).** "Prose Life names no city" is tagged Contested, and its `contested_claim` sets the History's York against the Life's silence. Silence is not a second side, and the Bollandists agree with the History, "Eboraci a septem Episcopis" (AASS3 l.32808-32810). Retag Documented, drop that `contested_claim`, and keep the card's `uncertain` 5 as a plain note.

Not findings:
- The Roman Breviary also keeps the translation of Cuthbert on 4 September in the diocese of Hexham, with lessons from Simeon of Durham and the bones sentence (BUTE l.2292, 106655-106691), and a Hexham commemoration "Holy Cuthbert, our Protector" (l.6496-6499). Available for `remembered` 3 if wanted.
- Raine also says Eddi gives Wilfrid "the character which had been already ascribed with far more justice to Cuthbert himself" (Raine l.1753-1756). Available for `traces` 4, and of use to the Wilfrid profile.
- The README's "trained at Melrose under men of the Irish mission" holds for Eata, "one of Aidan's twelve boys of the English nation" (GILES l.8263-8266); no held line says so of Boisil. The plural is loose but the call stands.

After the fixes (B-B2, B-M26, B-M27 in the brief; B-M28 not applied): 355 words, about 2:11, FK 6.0, Flesch 78.1 (scratch copy scored).

**Verdict: REVISE (2 blocking, 6 minor).**

---

### Verdicts

| Profile | Blocking | Minor | Verdict |
|---|---|---|---|
| Muirchu maccu Machtheni | 0 | 10 (B-M1 to B-M10) | REVISE |
| Tirechan | 0 | 8 (B-M11 to B-M18) | REVISE |
| Cogitosus | 1 (B-B1) | 7 (B-M19 to B-M25) | REVISE |
| Cuthbert of Lindisfarne | 2 (B-B2, B-B3) | 6 (B-M26 to B-M31) | REVISE |
| **Total** | **3** | **31** | |

The blocking points: a Stokes index entry read as a witness against Cogitosus being Muirchu's father (B-B1); Cuthbert's vision timed from Bede alone, against the approved Aidan profile (B-B2); and the false absence of Bede's own year for Cuthbert's consecration (B-B3). Every quotation in the four briefs matched its vendored file. All four briefs pass `grade_text` before and after the fixes.
