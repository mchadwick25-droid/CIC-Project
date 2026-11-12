# Opus check notes, supplement scan

Three parts: (1) the main table, (2) the ten hagiographic founders, (3) the follow-up rows.

## Part 1: main table

# Who scan supplement: independent check notes (Opus)

This check covers `draft/table.md` (240 rows in 12 columns across eras 1 to 10), plus `draft/already.md`, `draft/nothel.md` and `draft/notscored.md`. Row names below are the table's first cells. No repo file was edited and no paid call was made. The corrections are written into `draft/table.md` as "[Opus check: ...]" in column 7. Two duplicate rows were deleted, so the table now has 238 rows.

**Method.** Every file key was resolved to its file in cic/texts/. The keys came from the table's own definitions, the file keys of the ten era audits and the filenames named in each row; all resolve. For all 158 WHO, STORY and WANTED rows, a script matched every quoted string against the cited lines. The match allowed a window of plus or minus 4 lines and was tolerant of whitespace, line-break hyphens and XML tags. When a quote missed in the cited file, the script searched the whole Library for it. Every miss was then opened by hand. Dates and claims in the Dates and ruling cells were read at the cited lines.

For the WANTED rows and the "Not held, not scored" list, each name was searched again over all 1,649 file names and contents. The patterns used `\s+` between words, and spelling variants were added (Rilsk/Рилск, Helias/Elias, Uyttenbogaert/Wtenbogaert). Earlier-era overlap was grepped in the first cell of every table row of the ten era audits, Era8_Carry_Rows.md and Councils_Scan.md. Name variants were tried there too, and the hits were then read in full text. Some LISTED rows were also checked against cic-website/data/world-census.json, for the census-text condition of WANTED.

**Summary.** Of the 158 WHO, STORY and WANTED rows opened: 127 CONFIRMED, 27 CORRECTED, 2 NOT SUPPORTED (John of Rila; Mar Dionysius IV), and 2 deleted as duplicates of rows scored in era 6 (Jordanus; Isidore of Kyiv). No invented family, age, date or anecdote was found. Unconfirmed dates are marked "[suggested; to confirm]" or "died before 1990 (common knowledge)" as the rules allow. Eight verdicts change under settled rules (listed below).

Of the 17 WANTED rows, 16 are confirmed not held, with four search-note fixes. One proved held as a later retelling (John of Rila). Of 32 LISTED rows read: 25 stand (4 of them with OCR quote fixes) and 3 change verdict (Bugga, Elias of Cortona, Abelard). The other 4 are open judgment calls (Tecla and Cynehild, Matthias of Kunvald, John of Parma, Jacob of Sarug).

Counts after the check: 238 rows: **WHO 103, STORY 36, LISTED 82, WANTED 17** (before: 240 rows; WHO 103, STORY 38, LISTED 82, WANTED 17).

General note. Many quotes silently normalise OCR. Line-break hyphens, spacing and XML footnote breaks count as CONFIRMED (Avitus, Jacob of Sarug, Mara, the ANF fragments). Changed letters are listed below, under the rule that a quote is verbatim, with the OCR spelling as printed.

## Rows corrected, not supported, deleted, or verdict-changing

| Row | Verdict | Result | What changed (file + line) | Verdict now |
|---|---|---|---|---|
| Polycrates of Ephesus | WHO | CORRECTED | "seems to have presided" is ANF08 72563, not 72522 (fixed in place). | WHO (judgment) |
| Dionysius of Corinth | STORY | CORRECTED + verdict | The cited precedent is wrong: Dionysius of Rome is **LISTED** in era 1 ("One fragment, though it carries real doctrine"). Alexander of Jerusalem is STORY only because his life is told. This row says no tellable life is held, so the era 1 story test gives LISTED. | **LISTED** |
| Theophilus of Caesarea | STORY | CORRECTED + verdict | One synod-letter fragment, and "No life is told". Same ground as Dionysius of Corinth. | **LISTED** |
| Eusebius of Nicomedia | WHO | CORRECTED | THDT 8289, "At the hand of Eusebius of Nicomedia", is the translator's endnote 443, not Theodoret's text. Tag the baptism as an editor's note. | WHO stands |
| Innocent I | WHO | CORRECTED + verdict | Pope rule: official letters make a STORY (rulers, era 3; popes in eras 6, 7 and 9; Pius X). Siricius, with letters and no life, is LISTED in era 2. Damasus is WHO only as a named exception. His part in the Chrysostom case is a tellable tale. | **STORY** |
| Maron | WANTED | CORRECTED | More is held than the row says. Assemani, Bibliotheca Orientalis I, quotes Theodoret, Religious History 16, on Maron's burial (103110-103122). At 103250-103262 it identifies the Maron of Chrysostom's letter 36 (alive in 404) with the founder of the Apamea monastery. That identification is Assemani's reading, so tag it Contested. There is still no life. | WANTED stands |
| Yared | WHO | CORRECTED | The editor's "futile" is YAR 163, printed "nuilta futilia" (OCR). | WHO stands |
| Severinus of Noricum | WHO | CORRECTED | EUG 4863 prints "c. 482, 8 Jan.". Dates cell fixed to "about 482". | WHO stands |
| Findian of Clonard | WHO | CORRECTED | LISM 20390 prints "for sake of the people of the Gael", not "for the sake of the people". | WHO stands |
| Liberatus of Carthage | WHO | CORRECTED | PL68 75330 prints "I H/EFATIO AD BHEVIARIUM LIBERATI." (OCR). | WHO stands |
| Constantius of Lyon | WHO | CORRECTED | CONST 366 prints "insaipsit" (OCR). | WHO stands |
| Hilary of Arles | WHO | CORRECTED | The header quote is HIL 2 (Creator line), not 3 (fixed in place). | WHO stands |
| Symeon the New Theologian | WHO | CORRECTED | PHIL 19938-19940 prints a Cyrillic "Пор-" and "χιλιο--" (OCR). The sense is confirmed. | WHO stands |
| Elipandus and Felix | WHO (pair) | CORRECTED | ALC 25386-25387 prints "vero- / similitudine". Rule point: the 18th-century editors are not an independent witness to the teaching. See judgment call 3. | WHO stands (judgment) |
| Paulus Emeritanus | WHO | CORRECTED | PAUL 698-699 print "DIACONCS." and "pe vita" (OCR). 8611-8613 is the Migne notice, in two-column OCR. | WHO stands |
| Yahya ibn Said | WHO | CORRECTED | PO18 52695 prints "continuotour" (OCR). | WHO stands |
| Elias of Nisibis | WHO | CORRECTED | The title line is ELIAS 49, printed "NiSIBENI", not 51 (fixed in place). | WHO stands |
| John of Rila | WANTED | NOT SUPPORTED + verdict | "Only the Rila monastery in Paisii" is wrong. Paisii's Istoriia (1762) gives a notice of the saint: Tsar Peter's visit (PAISII 5058-5061), and saint no. 7, with the desert life, the relics, four disciples sent to found monasteries and "началникь ... вь Б(')лгарш" (7066-7129). Also RACKI-8 3544, a passing line. Paisii wrote eight centuries later, so the later-retelling rule applies (Vladimir and Olga). | **LISTED** (rescore when the Life or Testament is held) |
| Alexander Henderson | WHO | CORRECTED | "with so full accord" is KIRK 2238 and was not cited. | WHO stands |
| Johannes Uytenbogaert | WHO | CORRECTED | Both cited witnesses are 20th-century Remonstrant books, which are later retellings. Contemporary witnesses are held and should be cited instead: two letters of Lucaris to him (Lucaris letters 77, 9258-9301), Arminius's letters to him (arminius_works-v1 141-145, 16756), Calder's Episcopius (75 lines) and Scott's Dort (33 lines). | WHO stands |
| Estienne Pigarouich | STORY | CORRECTED | JR18 3357 prints "Pigarouik". | STORY stands |
| Mar Dionysius IV | STORY | NOT SUPPORTED + verdict | "Whitehouse names only the earlier Dionysius" is wrong. WHIT 15699-15708 is this man: "the junior native Metran, Mar Dionysius, was left supreme ... the head" of the reactionary party. Also 15804 (Bishop Wilson) and 16823 ("the great rupture"). With Mackenzie, that is two independent witnesses for a church head with no own text, so the era 8 rule applies. Whitehouse's hostility is to be marked. | **WHO (flag: no own text held)** |
| Mar Thomas Athanasius | STORY | CORRECTED | One more passing line: WHIT 18858-18860, "Mar Thomas who resides in the South" (identification Inferential-Thin). | STORY stands |
| József Ferencz | WHO | CORRECTED | UCH 100 prints "Serencz" (OCR). The session is 27 October 1912 (UCH 98). FERC07 2 is the Library's Creator line. | WHO stands |
| Hodge and Warfield | WANTED | CORRECTED | Absence: Warfield's Introductory Essay to NPNF series 1 vol. 5 is held (npnf105 531, 695-696), and the same page names "the immortal Hodges, father and son" (696). It is scholarship, not the 1881 article (the Harnack call). | WANTED stands |
| Evan Roberts | WANTED | CORRECTED | Absence: one unrelated 17th-century hit (henry-philip diaries 18578). | WANTED stands |
| W. T. Stead | WANTED | CORRECTED | Absence: one passing hit, a publisher's blurb quoting Stead (ellwood 15719). | WANTED stands |
| Charles Augustus Briggs | WANTED | CORRECTED | Absence: "Charles A. Briggs Graduate Professor" (salvian 115) names a chair held by Foakes Jackson, not Briggs himself. | WANTED stands |
| Maubant, Chastan, Ferréol and Ridel | STORY (group) | CORRECTED | DAL2 5739 prints "Maiibant" (OCR). "Pottier" has no hit in Dallet, but may be a slip for Pourthié, who has 38 lines in DAL2. Ridel's own account is quoted at DAL2 23301. See judgment call 8. | STORY stands |
| Bugga, abbess | LISTED | Verdict | Boniface's letters show her leading a house: "To the lady Bugga, abbess" (BONI 3126), and "Abbess Bugga" (5275). King Ethelbert's letter in the same collection says she "formerly ... governed well" "the monastery of consecrated women" (6048-6052). Her own letter is held too (2432-2440). This meets the women rule. | **WHO (women rule; thin life flagged)** |
| Elias of Cortona | LISTED | Verdict | The row applies the founders-through-enemies test. He is the head of an order, so the era 8 two-witness rule for heads applies (Dávid, de Nobili, Henderson here). Glassberger's Franciscan chronicle has 89 lines on him, uncited: provincial of Syria (2552), ruled the order after Francis's death (4258), elected minister general in 1232 or 1233 (4470), deposed (4392). The Spirituals in Ehrle are an independent, hostile witness. | **WHO (flag: no own text held; hostile witnesses marked)** |
| Peter Abelard | LISTED | Verdict | He is named in the census (the Victorine entry tells his Story of My Calamities), and the Historia calamitatum carries a life. That meets the WANTED test (the John of Damascus and Innocent III precedents). The wanted source is changed from the Theologia, which carries doctrine only. | **WANTED** |
| Isidore of Kyiv | WHO | DELETED (duplicate) | Already scored in era 6: "Isidore of Kiev (Cardinal Isidore)", LISTED (Who_Scan_Era6.md line 226). The row's "Not in any era scan table" is wrong. See judgment call 5. | removed |
| Jordanus | WHO | DELETED (duplicate) | Already scored in era 6: "Jordanus Catalani of Severac (Dominican, bishop of Columbum)", WHO (Who_Scan_Era6.md line 146), on the same Cathay letters. | removed |

OCR-only quote fixes on LISTED rows that stand: Aed of Sletty (WHITE 3767-3768 print "^dh"); Tecla and Cynehild (BONI 5873 "Bon face"); Laidradus and Nefridius (ALC 17120 "ABRATEM"); Ardo (ALC 113376 "Anian:z").

Confirmed (WHO, STORY and WANTED, 127 rows): all other rows. Among them, these were opened by hand after the script missed on OCR or layout:
- Avitus (two-column OCR, 1567-1570)
- Jacob of Sarug (a footnote splits the quote)
- the Jesuit Relations rows (Biard, Jogues)
- John White, Henri Arnaud, Martin Linner, Bentley, Curzon, Dunlavy, Grosvenor, Kriza
- Olivi (all at the cited lines)
- John of Beth Aphthonia, Julian of Toledo, Lubert and Henry, Sigismund
- Moses the Black (PALL 337: "died in Scete seventy-five years old ... left seventy disciples")
- Sempad (RHC1 67538-67545: dies at sixty-eight)
- Wilfrid (BEDE 13879-13881: "bishop forty-five years")
- Peter Payne and Rokycan (LUTZ-B 9053-9055: the second and third articles at Basel)
- Trychay (MORE 1705-1706: 30 August 1520)
- Zeisberger (HECK 462-465)

## Duplicates

- **Against earlier audits: two rows removed.** Jordanus = era 6 "Jordanus Catalani of Severac" (WHO). Isidore of Kyiv = era 6 "Isidore of Kiev (Cardinal Isidore)" (LISTED). Both rows claimed "checked: not in any era table"; that check missed the "Kiev" and "Catalani" spellings.
- **Checked and not duplicates.** Each pair below is two different people:
  - Paul Tieng Ha-sang and era 9's Chong Yak-chong (Augustin Tieng), his father, and Jean Tieng Iak-iong.
  - Augustin Niou of 1839 and Augustin Niou of 1801.
  - Mar Thomas Athanasius and era 9's Mathew Athanasius.
  - Mar Dionysius IV and era 8's Mar Dionysius I.
  - Mar Kurillos Joyakim and the Mar Kurillos of about 1800.
  - Cuthbert of Lindisfarne and era 4's "Cuthbert, Bede's pupil".
  - Pierus here and Pierius, the namesake noted in notscored.md.
  - Dionysius of Corinth, of Rome (era 1) and Exiguus.
  - Theophilus of Caesarea and Theophilus of Antioch.
  - Gennadius of Marseilles and Gennadius I of Constantinople.
  - Elias of Nisibis and Elias IV.
  - John XXIII Cossa and era 10's John XXIII Roncalli.
  - Pius II (Piccolomini) and the other Piuses of eras 7 to 10.
  - Thomas Cartwright and era 9's Peter Cartwright.
  - Charles M. Sheldon and era 8's Gilbert Sheldon.
  - John Hughes of Liverpool and John Hughes of Pontrobert.
  - Mary M. Dyer and the Quaker martyr Mary Dyer.
  - Calvin Green and Seth Y. Wells, and era 8's Benjamin Seth Youngs.
  - Johannes van Stiphout and era 8's Hieronymus de Bock.
- **Era 9 and era 10 "Other eras" names placed here** (Tile, Mokone, Roberts, Gladden, Briggs, Hodge and Warfield, Lipscomb, McAuley, Thomson, Harnack, Awstin, Stead, Sheldon, the Clarkes, Soh Sang Yun, McKenzie, Ositelu, Dunlavy, Heckewelder, Curzon, Kriza, Ferencz, Bentley, Grosvenor, Evans, Dyer, Hughes): all are in "Other eras" or "Not scored" lists. None has a table row in any audit, so none is a duplicate.
- **Within the supplement:** no two rows are the same person.

## WANTED and "not held" rows that proved held

- **John of Rila** (WANTED): held as a later retelling in Paisii (see above), so LISTED.
- **Maron** (WANTED): Assemani quotes Theodoret's chapter, and identifies the Maron of Chrysostom's letter as the founder. No life is held; WANTED stands.
- **John Fletcher of Madeley** (notscored.md, worker 4: "no file of his own; WANTED does not apply"). He is held in several independent sources:
  - Wesley's Journal (about 250 lines across v2-v8, including the 1785 funeral sermon on Fletcher, v7 6675-7907)
  - the Life of Mary Fletcher (106 lines; 4442 "Mr. Fletcher, of Madeley, is dying")
  - the Conference Minutes (9 lines)
  - Jackson's Lives of Early Methodist Preachers (8 lines)

  The worker's reason is the wrong test for this scan: the supplement exists for shapers whom no census text names. He needs a row (judgment call 6).
- **Joachim Lange** (nothel.md, "one passing line in Ziegenbalg"). Wrong: he is also named in Guericke's Life of Francke (1528, 1718), Burk's Bengel (17712) and Bengel's Gnomon (587, 3129). At Gnomon 3136 a translator's note gives his life ("born in 1670, in the territory of Brandenburgh"). There is still no own work and no shaping story: LISTED at most.
- **John Toeltschig** (nothel.md, "named in lists"). Wrong: about 45 lines, mostly in Wesley's Journal v1 (33 lines; 8723, 10673-10679, the Georgia Moravians) and v2 (7). Also Spangenberg (3) and the Acta Fratrum (1). A minor Moravian elder: LISTED at most.
- **Conrad Weiser** (nothel.md). Also in Woolman's Journal (5445-5516, with an editor's note on his life) and Kriebel (6421-6428). Passing; the outcome stands.
- **Peter the Venerable** (nothel.md). Also four passing lines in the Cluny charters' introduction (cluny_recueil t1 987-1815). The outcome stands.
- **Confirmed not held** (whitespace-tolerant, with variants):
  - the 15 WANTED rows of eras 9 and 10 (the 16 above, without John of Rila)
  - Theodoret's Religious History (only named, npnf203 3648-12639)
  - Orosius's Histories, Verecundus's works, Cyril of Scythopolis's Lives of Sabas and Cyriacus
  - Stethatos's Life of Symeon, Bede's Lives of Cuthbert, Eddius's Life of Wilfrid (Mansi 11 only cites "Eddius"), the Life of Fursey
  - Denis the Carthusian, Dante (no file), Arakel's text, Ole Olesen, George Scott, Pottier (none in Dallet)

## LISTED rows read and results (32)

- **Stand:**
  - Pierus, Theonas, Claudius Apollinaris, Alexander of Lycopolis, Mara bar Serapion, Salvian, Orosius, Maximinus
  - Kebius, Jordanes, Gelasius of Cyzicus, Anan-isho, Aed (OCR fix), Laidradus and Nefridius (OCR fix), Ardo (OCR fix)
  - Berengar (not named in the census, so LISTED is consistent), Urban VI, Thomas Cartwright, al-Duwayhi, Colin, van Stiphout, Dippel, Landgren, the Stundist group
  - Abba Giyorgis (not named in the census)
- **Verdict changed:** Bugga (WHO), Elias of Cortona (WHO), Abelard (WANTED).
- **Open judgment calls:**
  - Tecla and Cynehild (judgment call 9)
  - Matthias of Kunvald (judgment call 4)
  - John of Parma: he is named in the census (the Joachimite entry), and Salimbene or Clareno would carry his life. WANTED is defensible. The row's wanted source (his Sentences or letter) would carry doctrine only. Recommend restating the source.
  - Jacob of Sarug: no census text names him, so LISTED is consistent. Note that a "Source wanted" is filled on a LISTED row.

## Open judgment calls

1. **Hethum II (STORY).** The poem "Moi, Héthoum, roi de nom seulement ... pauvre et chargé de dettes" (RHC1 63702-63704) is a first-person confession.
   - (a) Recommended: WHO, under the personal-confession branch of the ruler rule (era 3; Henry IV, era 5). The row adds a condition the rule does not have ("if it shaped the church").
   - (b) Keep STORY: the poem shows no act of church leadership.
2. **Polycrates of Ephesus (WHO).**
   - (a) Recommended: WHO on the Polycarp footing. His one letter carries his own family, age and side in the Easter dispute, and the editor adds the synod.
   - (b) STORY, like Alexander of Jerusalem.
3. **Elipandus and Felix (WHO pair).** "Teaching two" needs two contemporary witnesses. The 18th-century editors rest on Alcuin.
   - (a) Recommended: keep WHO only if a second contemporary text is held, such as the Frankfurt 794 synodal letters or Paulinus of Aquileia. Cite it.
   - (b) If none is held: WANTED, naming Elipandus's letters in PL96.
4. **Matthias of Kunvald (LISTED).** He is named in the census (the lot of 1467) and signs the Unity decree of 1495 (DEKR 528). Goll tells his consecration.
   - (a) Recommended: WHO (flag: thin), under the two-witness rule for heads: the Unity's own decrees and Goll.
   - (b) WANTED, naming the Brethren's sources on the first elders.
   - (c) Keep LISTED.
5. **Isidore of Kyiv (era 6 row LISTED; the supplement row is removed).** The supplement found his own letters in PG159 (337-339) and Migne's notice of his career (55512-55516).
   - (a) Recommended: send this evidence to the era 6 row as a rescore question (WHO, thin life). It is not a new row.
   - (b) Leave era 6 as LISTED.
6. **John Fletcher of Madeley (no row).**
   - (a) Recommended: add an era 8 row, WHO (flag: no own text held), on Wesley's Journal and Mary Fletcher's Life as two independent witnesses.
   - (b) WANTED, naming his Checks to Antinomianism or Benson's Life.
   - (c) LISTED.
7. **Liberius of Rome (WHO).** Under the pope rule applied to Innocent I, official letters make a STORY. Liberius's letters from exile, the letters of his fall, are personal pleas, and Theodoret gives his words to Constantius.
   - (a) Recommended: keep WHO, as the personal-confession branch, with the fall letters tagged Contested.
   - (b) STORY, for consistency with Innocent I.
8. **Ferréol and Ridel (inside the STORY group row).** Ferréol was vicar apostolic (DAL2 12271), and Ridel's own account is quoted (DAL2 23301).
   - (a) Recommended: split them out. Ferréol is WHO under the head-of-church precedent if letters of his are quoted. Ridel is WHO if his account carries more than one episode.
   - (b) Keep one STORY group row.
9. **Tecla and Cynehild (LISTED pair).** Only the editor (BONI 1199-1200) shows Thecla "ruling two" houses. Boniface addresses them with Lioba but does not say they rule.
   - (a) Recommended: keep LISTED until a Who's line shows her leading.
   - (b) WHO for Thecla under the women rule, if the editor's line is accepted.


## Part 2: hagiographic founders

# Opus check: era 3 founders under the later-retelling rule

Scope: ten era 3 rows in `draft/table_sorted.md`. Rule applied (coordinator ruling, era 4 precedent): a later retelling alone gives LISTED until a held source from near the person's own time carries the person. No repo file was edited and no paid call or network call was made. Searches ran over all of `cic/texts/` with whitespace-tolerant patterns (`\s+`) and spelling variants (Brend-/Brenainn, Ciar-/Kiar-/Ceran, Finn-/Vinni-/Findbar, Senan/Inis Cathaig, Cadoc/Catoc/Cadocus/Nantcarvan, Padarn/Paternus, Carant-/Carann-, Tath-, Bernac-/Brynach, Findchua/Finnchua).

Early sources held and searched: Adomnan's Life of Columba (ADOM, composed c. 697-700 per ADOM header line 16), Bede, Gildas with fragments and Lives (GILD), Muirchu and Tirechan (TRIP2 = stokes_tripartite-life-of-patrick-v2-lat-muirchu-tirechan-confession_1887.txt), the Penitentials (WASS), the Antiphonary of Bangor (BANG), the Annales Cambriae (AC, a 10th-c. compilation per its header line 2), the Life of Samson, Jonas's Life of Columbanus, Gregory of Tours, Venantius, Nennius. Not held: the Annals of Ulster, Tigernach, the Four Masters before 1172, Columbanus's letters (only reported in GILD 15215-15229).

How the late Lives are dated (held lines):
- Lismore (LISM): the manuscript was "compiled from the lost Book of Monaster-boice and other manuscripts, in the latter half of the fifteenth century" (LISM 218-219). Stokes calls the Lives' language "a mixed language", Old-Irish beside late Middle and even Modern forms (LISM 3256-3257). The Library header dates them 12th-15th c. The texts are about 11th-12th c. [suggested; to confirm].
- Rees (REES): the time when the Lives were compiled "is not known, but it was probably about the twelfth century" (REES 322-323). The manuscript of the Brynach and Cadoc Vitae is Cotton Vespasian A. xiv (REES 1082, 1778), written about 1200 [suggested; to confirm]. The Cadoc Vita names Lifris as its author (REES 4236). Lifris wrote about 1100 [suggested; to confirm].

## Per person

| Person | Late Life and date | Early source held | Before | After |
|---|---|---|---|---|
| Senan of Scattery | Lismore Life (manuscript after 1450; text about 11th-12th c. [suggested; to confirm]) | None. TRIP2 24067 "prophesies Senan of Inis Cathaig" is the editor's index to volume I, which is not held. | WHO | **LISTED** |
| Findian of Clonard | Lismore Life (as above) | Held, but the identity is Contested. Adomnan's "bishop Vinnian" (ADOM 5863) and "the venerable bishop Finnian, his former master" (ADOM 9398-9399) are glossed "Probably St. Finnian, of Moville" (ADOM 5879; 9414). Warren reads Adomnan's "magister" as "St. Finnian of Clonard" (BANG 10645-10646). The Penitential of Vinnian is held (WASS). Wasserschleben thinks the Clonard founder "doch wahrscheinlich der Verfasser" (WASS 1443-1447). Williams, after Seebass, says Columbanus's Vennianus "must be, not Finnian, the founder of Clonard" (GILD 15228). | WHO | **LISTED** (flag: Vinnian, the author of the held Penitential, could be scored as his own row) |
| Brenainn of Clonfert (Brendan) | Lismore Life (as above); the Latin Vita in Rees (about the 12th c., REES 322-323) | **Adomnan.** Aidan "ministered for twelve years to Brendan Mocualti" (ADOM 3936). "Brendan Mocu Alti" is one of "four holy founders of monas-teries" who visit Columba (ADOM 10231-10238), and he sees the fiery globe at Mass (ADOM 10246-10251). The translator's note identifies him as the founder of Clonfert, "died 577" (ADOM 10278-10282). He is distinct from Brendan of Birr (ADOM 9370-9376; AC 2501). | WHO | **WHO** (named in the row; confidence Widely Accepted for the founder, Inferential-Thin for the voyage) |
| Ciaran of Clonmacnois | Lismore Life, "Clonmacnois, where this Life of Ciarán was composed" (LISM 22789); manuscript dating as above | **Adomnan and Tirechan.** Columba visits "the Clonoensian monastery of St. Ceran" (ADOM 2735-2736). Tirechan (7th c., about 690 [suggested; to confirm]) has Iustus baptise "Cia)ranum filium artificis" (TRIP2 3470-3471, OCR brackets). He dates Ceran's birth from Patrick's death (TRIP2 3473-3475) and complains of "familia Clono" (TRIP2 3187-3189). The Annales Cambriae "Dormitatio Ciarani." (AC 2406) is a 10th-c. compilation and counts as support only. | WHO | **WHO** (named in the row; Widely Accepted) |
| Cadoc | Vita by Lifris (REES 4236; about 1100 [suggested; to confirm]) | None. The GILD Cadoc lines (23227, 23238-23247) come from the Life of Gildas by Caradoc of Llancarfan (12th c. [suggested; to confirm]) and from Williams's notes. | WHO | **LISTED** |
| Paternus (Padarn) | Rees Vita (about the 12th c.) | None. "S. Paterne" in the Rheims litany (GILD 24044) and "sancti Paterni Vene-" (GILD 21618) are, or may be, Paternus of Vannes. | WHO | **LISTED** |
| Findchua of Bri Gobann | Lismore Life (as above) | None. Adomnan's Fintans (ADOM 2559-2684) are other men. | STORY | **LISTED** |
| Carantoc (Carannog) | Rees Vita (about the 12th c.) | None. "Carantot" (TRIP2 17543, 17625) is in a Book of Leinster tract, 12th c. [suggested; to confirm]. | STORY | **LISTED** |
| Tatheus (Tathan) | Rees Vita (about the 12th c.) | None. The other Tatheus hits are the apostle Thaddeus. | STORY | **LISTED** |
| Bernacus (Brynach) | Rees Vita, from Vespasian A. xiv p. 142 (REES 1082) | None | STORY | **LISTED** |

Era 3 was re-sorted (stable): WHO, STORY, WANTED, LISTED, with Major yes first in each group. Era 3 now has no STORY rows. Net change across the table: WHO −4, STORY −4, LISTED +8.

## Same weakness elsewhere (flagged, not edited)

These rows give WHO although the only witness is a Life written centuries after the person:
- **Yared** (era 3, WHO; YAR = gadla-pantalewon-yared_vitae-sanctorum-antiquiorum-lat_conti-rossini1904.txt). The only witness is the Gadla Yared. The row itself calls it "a medieval composition" and says "the record is late". It is the Illtud type.
- **Pantalewon** (era 3, WHO; same file, YAR 1810-1814). The only witness is the Gadla Pantalewon, a late Ge'ez Life [suggested; to confirm]. It is the Illtud type.

Read and not flagged:
- Maba' Seyon and Gabra Krestos (era 6, STORY pair). Their Life was written after the saints died, but the gap is not shown to be centuries.
- Fursey. Bede is within about a century.
- Germanus, Severinus and Pisentius. Each has a contemporary or near-contemporary Life.
- Cuthbert, Wilfrid, and Cedd and Chad. Each rests on Bede.
- The later-era "Life told by another" rows. These rest on contemporary chronicles, registers or mission histories.


## Part 3: follow-up rows

# Who scan supplement, follow-up pass: independent check notes (Opus)

**Scope.** This check covers the 15 rows marked "(follow-up pass)" in `draft/table_sorted.md`, plus the follow-up note on the Elipandus and Felix row. The worker's calls are in `rows_6.md`. No repo file was edited and no paid call was made. Corrections are written into column 7 as "[Opus check: ...]". All rows keep 12 columns. No verdict changed, so no row moved within its era.

**Method.** A script matched every quoted string against the cited lines. It allowed a window of plus or minus 4 lines and was tolerant of whitespace and line-break hyphens. Every miss was opened by hand; the misses were OCR, two-column editor's notes, or a quote tied to the wrong cite. Dates and claims were read at the cited lines.

**Duplicates.** For all 15 new names, I grepped the first cells of the ten era audits, Era8_Carry_Rows.md and Councils_Scan.md, then the full audit texts, then the rest of the table.

## Summary

All 15 new rows were opened:

- **Confirmed: 8.** Hormisdas, Gelasius I, Symmachus (the pope), John II, Marcus Cassinensis, Anthony Thacher, William Wood and Roger Clap. A clean confirmation note was added to each.
- **Corrected: 7.** None changes the verdict.
  - Ruricius: an OCR quote fix.
  - Niketas Stethatos and John Cotton: the OCR is noted.
  - Richard Mather: a claim is refined.
  - Thomas Dudley and Samuel Whiting: the edge calls are checked, and one cite is moved.
  - John Fletcher: the source of one line is corrected and the death day added.
- **Not supported: 0.**
- **Invented detail:** none found.
- **Duplicates:** none.

The Elipandus and Felix row is **confirmed**. The coordinator's condition is met, and the Dates cell quote was fixed to the printed "vero- similitudine".

## Rows corrected

| Row | Verdict | What changed (file + line) |
|---|---|---|
| Ruricius of Limoges | WHO | FAUS 20030 prints "ae beatissime" (OCR for "ac"). |
| Niketas Stethatos | WHO (thin) | The quotes are confirmed, but OCR as printed: 24493 has a Cyrillic "НМОМ" for ΗΜΩΝ, and 23139-23145 has a broken two-column notice. |
| John Cotton | WHO | 21175 prints "MU. COTTON" (OCR). The death date is in a two-column editor's note (21722-21724). |
| Richard Mather | WHO | Winthrop's April 1636 entry records that the first gathering was turned back (WIN 8403-8405, "not meet, at present"). "Ordained their teacher" is the editor's note (YOUNG 24109-24110). 22534 prints "i635". |
| Thomas Dudley | WHO (judgment) | Edge call: the 1631 letter is a personal narrative, not an official text, so the own-voice branch applies (Winthrop, era 7, is WHO). Church shaping stays flagged as thin. STORY is the alternative. |
| Samuel Whiting | WHO (recorder) | Edge call: the recorder rule fits. The editor says his sketch "forms the foundation of Norton's as well as of Mather's Life" (YOUNG 21824-21827). "very unskilful in church matters" is WIN 9374, not a Young line. |
| John Fletcher of Madeley | WHO (flag) | "Mr. Fletcher is the best that occurs now" (WJ5 25309-25311) is Curnock's footnote quoting a letter, not the Journal text. MFL 7725-7728 gives 14 August 1785 (Dates cell updated). Mary Fletcher is a close but independent witness. |

## Edge calls and judgment notes

- **Popes.** Hormisdas, Gelasius I, Symmachus and John II are STORY under the pope rule as applied to Innocent I. Each holds official letters only, and the Liber Pontificalis supplies a tale. This is consistent.
- **Roger Clap (LISTED).** His memoir is a first-person account of God's providences, one witness. That is the shape the era 8 Hopper and Mitchell rows score STORY. LISTED holds only because the editor cut the religious part (YOUNG 18720-18723).
  - (a) Recommended: keep LISTED.
  - (b) STORY, on the Hopper precedent.
- **Elipandus and Felix (WHO pair): confirmed.** The lines are:
  - Elipandus's own letters in PL96 (71068; 71805-71811, Epistola IV to Alcuin).
  - Heterius and Beatus, Ad Elipandum (73642-73646), Asturian and independent of the Frankish court.
  - Annales regni Francorum for 792 (6416-6430) and 794 (6656-6672).
  - The Frankfurt 794 capitulary (capitulatio 5588-5604), which condemns "erese Elipandi ... et Felicis Orgellitanae".

  So "teaching two" rests on contemporary witnesses, and Elipandus has his own held voice. Felix's Confessio fidei (72728-72730) is a recantation after his condemnation, so it counts as a forced text, not his free voice (as with Berengar's oath).

## Duplicates

None:

- No era table scores any of the 15.
- Era 4's "Merkurios, king of Makuria" is not Pope John II Mercurius.
- Era 8's Mary Bosanquet Fletcher (line 244) and Henry Moore (line 482) are not John Fletcher.
- Era 7's Giles Fletcher is a different man.
- Era 5 names Stethatos only as the author of the wanted Life of Symeon.
- Within the table:
  - Symmachus the pope and Symmachus the prefect are separate rows, cross-noted.
  - Gelasius I and Gelasius of Cyzicus are separate rows.
  - Richard Mather is not Cotton Mather.
  - There is no Winthrop row in the supplement; he is scored in era 7.

