# Opus check of the Who scan, era 6 (2026-11-11)

Read-only. No paid calls; nothing in the repo changed. For every WHO, STORY and WANTED row in W1-W4 (103 rows) I ran every quoted phrase against the cited line range in `cic/texts/` (whitespace-normalised, plus or minus 3 lines). I then opened the lines by hand for every miss and for the date and claim cells of most rows. For every WANTED row I grepped file names (cic/texts, cic/corpus-map) and text for the named source. I also spot-checked 36 LISTED rows, including all 15 on the priority list. Line numbers are the file's own lines (as `rg -n` or `sed -n` count them).

**How to read a status.** "CORRECTED (form)" means the row is right, but a quote was normalised away from the printed OCR, or a line number is off by a few lines. "CORRECTED" alone means a fact, a quote, a verdict or an era changes.

**Counts.**
- Main rows (103): 74 CONFIRMED, 29 CORRECTED, 0 NOT SUPPORTED.
- LISTED spot-checks (36): 23 CONFIRMED, 8 CORRECTED, 5 NOT SUPPORTED.
- In total: **97 CONFIRMED / 37 CORRECTED / 5 NOT SUPPORTED** (139 rows).

**Invented person-detail: none found.** Two errors come close:
- W3 Kantakouzenos carries a Latin quote that is in no held volume.
- W3 Gregory the Patriarch reverses Palacký and Gindely.

**Editions named from memory.** Every such edition carries "[suggested; to confirm]" or "[recollection; to confirm]", or is census-named or cited in a held line. I found no untagged edition. One tagged edition looks doubtful: Ewostatewos, Conti Rossini. To my recollection the Gadl is Turaev's CSCO *Acta S. Eustathii* (1905) [recollection; to confirm].

## W1

| Person | Status | Details |
|---|---|---|
| John Wyclif | CONFIRMED | VAUGHAN 1262-1266, 4758-4766 (paralysis 29 Dec, death 31st) read as claimed. Live entry is WHO: no flag. |
| Thomas a Kempis | CORRECTED (form + lines) | Entry 1399 and profession 1406 are BENHAM 497-499, not 506-510 (506-510 is the Bible copied 1439). CHRON 242-243 reads "contains a notice of the author written by a contemporary member of the community", not "with a notice". BUSCH 5413-5415 as printed: "frator Thomas de Kerapis vir probate vite, qui plures devotos tractatulos** composuit, videlicet „qui sequitur me" de imitacione Christi". BENHAM 493 (c.1380) and 522 (d. 1471) confirmed. |
| Richard Rolle | CONFIRMED | HORST 131 ("about, or shortly before, 1300"); death 29 Sep 1349 is HORST 133. UNDERHILL-H 64-65 "c. 1290-1349". COMPER 2129. |
| Julian of Norwich | CONFIRMED | WARRACK 225 (Sloane, 13 May 1373), 342, 356 ("yet in life", 1442), 3819; HARFORD 247 (living 1413). |
| Meister Eckhart | CORRECTED (form) | EVANS 418-419 as printed: "has been ealled the lather of the German mystics" (OCR). The Daniels quote starts at DANIELS 171, not 172. DANIELS 847 as printed: "Ego irater Ekardus ordinis predicatorum prefatus respondeo"; "teste omni vita mea et doctrina" is at 853. EVANS 493-517 dates confirmed. Note: EVANS 495 says it is "argued that he was born before 1200"; the row's "birth unknown" stands. |
| Johannes Tauler | CONFIRMED | WINK 4115 (1290), 7171-7172 (16 June 1361). |
| Henry Suso | CONFIRMED | KNOX 52 (1300), 85-86 (1365, Conversion of St Paul), 10712 (card 1295-1366), 3495-3503. |
| Elsbeth Stagel | CONFIRMED | "beschrieben von Elsbet Stagel" is on STAGEL l.1 (title; l.119 has the OCR "Eisbet Stagel"). STAGEL 855; KNOX 10685 (d. 1360). Recorder, thin own life, flagged. |
| Jan van Ruusbroec | CONFIRMED | RUUS 484 ("born in 1273"), 752-754 (2 Dec 1381), 553-558, 583-584; EVANS 507. |
| Geert Grote | CORRECTED (form + lines) | FOUNDERS 2104 reads 'the " Great," was a citizen', not "called the Great". The dates 1340-1384 are in the GROOTE header l.3. FOUNDERS 394-398 do not carry them (FOUNDERS 399 has 1340 only). |
| Florens Radewijns | CORRECTED (form) | As printed: BUSCH 4517 "Florencius Kadewini prinms rector congregacionis"; BUSCH 4818 "Florencius Radewini primus pater Daveniriensis". The death reasoning is confirmed: FOUNDERS 11548-11554 (Amilius rules 4 years 3 months to 1404) and ZERB 174-175 (the reversed order). |
| Gerard Zerbolt | CORRECTED (form) | ZERB 170-171 as printed: "must have known the subjedl of this memoir". "Life of Gerard of Zutphen" is the FOUNDERS 11172 heading ("THE LIFE OF GERARD OF ZUTPHEN"). ZERB header l.4 has 1367-1398. |
| Johannes Busch | CONFIRMED | BUSCH 1628-1632 (Sülte to 1479, "ca. 1480", "den Ruf eines Heiligen"). |
| Salome Sticken | CONFIRMED | DIEPENVEEN 441-442 (OCR spacing only). Note: 908-910 makes her "meystersche" of seven novices clothed in 1408 (editor 457: the novice-mistress title). The leadership claim rests better on her title "mater" (436, 441). |
| John Brinckerinck | CONFIRMED | FOUNDERS 9256-9262 and 9297-9298; DIEPENVEEN 696. |
| Reginald Pecock | CONFIRMED | PECOCK-1 322-325, 421 (Oriel, fellow 30 Oct 1417), 1135, 1226-1227 (11 Nov 1457). |
| Lydwine of Schiedam | CORRECTED (form) | LYD 251-252 reads "he was born the same year, 1380, and he passed away thirty-eight years after her demise". The row drops the second "he". |
| Sir John Oldcastle | CONFIRMED | FASC 32738-32739. "their leader" is WALS 25653, not 25655. |
| William Sawtrey | CORRECTED (form) | As printed: FASC 31136 "Eco, Willelmus Sautrye, protestor"; FASC 444 "Conclusiones Willehni Sautry ha?retici". FOXE-3 357: "1400. Sir William Sautre, otherwise called Chatris". |
| William Thorpe | CONFIRMED | FOXE-3 20629; the heading "The Examination of William Thorpe, penned with his own Hand" is at 20622 (and 20600). |
| Margery Kempe (WANTED) | CONFIRMED | Not held: no file; text hits only GARDNER, README and REGISTRY. GARDNER 545-547 reads 'absolutely no traces can be discovered of the " Book of Margery Kempe,"'. The verdict (WANTED vs LISTED for a STORY candidate) stays the row's own question 2. |
| Henry Pomerius (WANTED) | CONFIRMED | RUUS 553-558 ("with his mind lifted up into God"), 583-584 (Analecta Bollandiana iv, 1885). Not held: the "Pomerius" hits elsewhere are Julianus Pomerius and a 1628 citation. |
| *LISTED* Walter Hilton | CONFIRMED | UNDERHILL-H 99-106 (OCR "which' his work") and 135-137 (24 Mar 1395-6). LISTED fits the story test and the Guigo II precedent. |
| *LISTED* Nicholas Love | CONFIRMED | LOVE 170-177 and 195-196. "maister of lollardes" is LOVE 18088, as printed "maifter of lollardes". |
| *LISTED* Rulman Merswin | CONFIRMED | SCHMIDT-M 107-111, as printed: "Hulmann Merswin", "Goltesfreunde „im Oberland,"". |
| *LISTED* Nicolaus von Basel | CORRECTED (form) | WINK 1754 reads "a layman who was rich in God's grace". SCHMIDT-M OCR: "grossen gollesfreunde" and "G olles freunde" (263). |
| *LISTED* John Badby | CORRECTED (form) | The contents lines are FOXE-3 369 ("1409. John Badby, artificer, a Martyi-") and 811 ("Burning of Badby"), not 371 and 813. |
| *LISTED* Thomas Netter | CONFIRMED | FASC OCR: "has ncver liitlierto been called iu question". |
| *LISTED* John Purvey | CONFIRMED | "is decisive" is WYCBIB 3118. FASC contents OCR: "hfereses". |
| *LISTED* Ebner and Langmann | CONFIRMED | STRAUCH 656-657: Ebner "(f 1356)". Langmann died 19 years later, so 1375 by inference; the OCR prints "l.fV 5". "umfangreiche Tagebücher" is STRAUCH 669. |
| *LISTED* Grenehalgh / Methley / Horsley | CONFIRMED | UNDERHILL-H 1790-1792 (OCR "incarthusia"), MCCANN 633-634, UNDERHILL-H 124-128. |

## W2

| Person | Status | Details |
|---|---|---|
| Catherine of Siena | CONFIRMED | CATH-L 1256-1259 (25 Mar 1347) and 1388-1389. The 1336-1342 OCR reads "June 1 8th". |
| Bridget of Sweden | CONFIRMED | BIRG-E 1182 (28 July 1373) and 1039-1040 (Order approved by Urban in 1370). |
| Bernardino of Siena | CORRECTED (form) | GLASS 19790-19791 as printed: "nomen lesus in po-pulo exclamabat". ORL 5638 (8 Sep 1380) and BANCHI1 1149-1156 confirmed. |
| Angelo Clareno | CORRECTED (form) | "far more bitter" is the drafter's English. Oliger's Latin at CLAR 2984-2992 reads "longe acerbior". The death is CLAR 1398-1399, as printed "die 1d lunii 1337". |
| Michael of Cesena | CONFIRMED | CARL 2202 ("Anno 1343 [1342]. Electus fuit Generalis anno 1316") and 3703. |
| William of Ockham | CONFIRMED | Dates are tagged. WHO is a judgment call, flagged. |
| Bernard Gui | CONFIRMED | MOLLAT1 403-437 (Royère, c.1261/62; professed 16 Sep 1280; Tuy 26 Aug 1323; Lodève 20 July 1324; Lauroux 30 Dec 1331). |
| Peter of John Olivi | CORRECTED (era + form) | "not a rounded, readable life" translates EHRLE-3 22877-22878: "nicht ein abgerundetes, lesbares Lebensbild". The dates are confirmed: EHRLE-3 22922-22926 and 22986 ("am 14. März 1298"). **Era:** all his work is before 1298, so by the date-of-work rule (era 5 precedents: Yahya, Symeon) he goes to the era 5 supplement. Option (a) in W2 question 1 breaks the rule; recommend (b). |
| Ubertino da Casale | CORRECTED (lines) | The "not require any provision in this world" answer is LEA3 3634-3637, not 3024-3030. The Arbor vitae edition "(Venetiis 1485)" is cited in a held line, EHRLE-2 20809, so it can lose the [suggested] tag. |
| Marsilius of Padua | CONFIRMED | MARS header ("died c. 1342"), 224 (Rector Dec 1312-Mar 1313), 385-386 (John of Jandun d. Sept 1328). |
| Jacopone da Todi | CONFIRMED | JAC-L l.10 content note (quote verbatim). The era flag stands (judgment call). |
| Caterina Vigri | CONFIRMED | Women rule. |
| Nicolaus Glassberger | CONFIRMED | GLASS 128-129: "Quo anno Fr. Nicolaus mortuus sit, non potuimus investigare". Recorder, thin life flagged. |
| Benedetto di maestro Bartolomeo | CONFIRMED | BANCHI1 1249-1264. A judgment call, as the row says. |
| Jean Gerson | CONFIRMED | The three titles are in the GERSON l.10 content note. FIN2 18700: "Peter von Ailli, den sein Schüler Gerson nennt". |
| Ulrich von Richental | CONFIRMED | RICH header (c.1365-1437); 536 (third person in the Constance codex); 1720-1722; 3992. **W2 is the better-supported draft** (see W3, Richental). |
| Boniface VIII (STORY) | CONFIRMED | MIRBT 13546. |
| Clement V (STORY) | CONFIRMED | MIRBT 13628. |
| John XXII (STORY) | CONFIRMED | MIRBT 13777. |
| Martin V (STORY) | CONFIRMED | MIRBT 14008-14010 (Inter cunctas, 22 Feb 1418). |
| Julius II (STORY) | CORRECTED (form) | As printed: MANSI32 53399 "Julius papa 11."; MANSI32 65350 "Julius epifcopus fervus fervorum dei". The words "under Julius II and Leo X" are not at MANSI32 62016-62040; they paraphrase the MANSI32 l.10 content note ("the acts of Julius II and Leo X, 1512-1517"). Drop the quote marks. |
| Nicholas V (STORY) | CONFIRMED | |
| Innocent VIII (STORY) | CONFIRMED | PERRIN-E 5152 ("commissioned by Popes Sixtus IV. and Innocent VIII."). Judgment call as drafted. |
| Leo X (STORY) | CORRECTED | **Delete "BULN 117546 (a later Franciscan entry, 1517 ...)".** "1517." is the entry number in a volume of Eugenius IV and Nicholas V letters, 1431-1455 (BULN l.10). It is not a year and not a Leo X letter. MANSI32 OCR: "per nos ... conclufo". Confirmed: "Ite vos" is not held (0 hits). |
| John of Brunn and Albert (STORY) | CONFIRMED | WATT 5290-5291: "vixi' in libertate spiritus" (OCR apostrophe). Gallus of Neuhaus 1335 at WATT 5153-5155. |
| Raymond of Capua (WANTED) | CORRECTED (evidence) | Add CATH-I 14351-14365: Fiorilli quotes him and notes that "Raimondo delle Vigne, da Capua ... maestro generale" wrote the Latin Life, "il piú autorevole documento antico intorno a Caterina". Add CATH-I 15255-15260 (his prologue to the Libro, in a manuscript description). Not held: the Legenda itself (grep: quotations and citations only). WANTED stands. |
| *LISTED* John of Capistrano | NOT SUPPORTED | "A retelling alone" is wrong. Contemporary non-Franciscan witnesses are held: DOUK 33596 ("Iohanne Capistrano adhortatore Corvinus"); CHALC 25214, 25595-25602 and 47995 (Belgrade, Hunyadi). So are papal letters of his lifetime (BULN 85925-86200 and others). GLASS 23228-23229 names Christopher of Varese "qui scripsit Legendam de ipso Patre": add that to Source wanted. **Proposed: WANTED** (the Life by Nicholas of Fara or Christopher of Varese), judgment call. Alternative: WHO on GLASS + BULN + DOUK/CHALC. |
| *LISTED* Colette of Corbie | NOT SUPPORTED | "GLASS (no hits for Colette)" is wrong: the Latin form is "Coleta". GLASS 22459-22468 is her obituary: 6 March 1447, aged 66, "reformatrix", and hostile ("muliebri levitate usa"). GLASS 20011 and 464 also name her. BULN 5316-5579 holds papal letters of her lifetime, among them "Confirmat reformationem et statuta B. Coletae" (5575). With these, the life is not a retelling alone. **Proposed: WHO** (women rule: she founded and reformed), judgment call. Alternative: WANTED (Pierre de Vaux). |
| *LISTED* Girolamo Savonarola | NOT SUPPORTED | "The only held lines are Lea's" is wrong. BURCH holds his own letter, "Responsio fratris Hierouymi Savonarole ad Alexandrum papam sextum" (BURCH 22493-22500), and the papal brief to him of 16 Oct 1497 (22406, 22490-22491). It also holds Thuasne's notes on his ordeal, imprisonment and death (35349-35440; 14 hits). **Proposed: WHO** (own work + following), judgment call. Alternative: STORY. |
| *LISTED* Jacques de Molay | NOT SUPPORTED | "No own words" is wrong. BAL 7236-7248 prints "Consilium magistri Templi datum Clementi V super negotio Terre Sancte et super unione Templariorum et Hospitalariorum [1306-1307]". It is his own first-person memoir: "Pater sancte, queritis quid michi ...". RHC2 21660-21680 and 21938-21950 are a contemporary Cypriot chronicler (the Templar of Tyre) who relates his execution. **Date:** 18 March 1314 (RHC2 21676), against Lea's 19 March. **Proposed: STORY.** |
| *LISTED* Guillaume Belibaste | CONFIRMED | No file; "Belibast" and "Bélibaste" have 0 text hits. |
| *LISTED* Guiard of Cressonessart | CONFIRMED | LEA3 36045 only. |
| *LISTED* Paoluccio Trinci | CORRECTED (evidence) | Add EHRLE-4 10377-10481. Ehrle's notes say the ministers general name him "Paulutius Vagnotii" in their letters, and quote Wadding on "fratrem Paulutium Fulginatem". The GLASS grep miss is confirmed. LISTED stands. |
| *LISTED* John Mirk | CONFIRMED | "active about 1403" is the ERBE header. PEA 8739 as printed: "per fratrem lohannem. myrcus canonicnm". |
| *LISTED* Gregory XI / Paul II | CONFIRMED | Paul II OCR: "Poli to Kome" (LEA3 8494). |

## W3

| Person | Status | Details |
|---|---|---|
| Gregory Palamas | CONFIRMED | OCR forms in the PALH title. |
| Gregory of Sinai | CORRECTED (lines + form) | The Greek floruit is PG150 69116-69117, not 69105-69110. As printed: "περί που τὸ χιλιοστὸν τριαχοσιοστὸν τριαχοστὸν ἕτος"; Latin at 69162, "circa millesimum trecentesimum tricesimum". The teaching phrase as printed: "νήψεως χαὶ φυλαχῆς vob; xai νοερᾶς προσευχῆς". |
| Barlaam of Calabria | CONFIRMED | PG151 OCR: "ex urbeSeminaria", "nulli su:e zetatis secundus". |
| Gregory Akindynos | CONFIRMED | PG151 26485: "Gregorius. Acindynüs, monachus Grzcus ac theologus". |
| Nicholas Cabasilas | CONFIRMED | PG150 26065-26075 prints "Claruit circa a. 4550" (OCR for 1350). |
| Philotheos Kokkinos | CORRECTED (form) | PG150 530 reads "ab ipso Philotheo patriarcha Cpol", not "ipse Philotheus". ACTA 19508 and PALH 3584 confirmed (OCR). |
| Mark of Ephesus | CONFIRMED | "to all Christians" glosses PG160 97814, "Epistola encyclica ad omnes Christianos de synodo Florentina non suscipienda". |
| Bessarion | CONFIRMED | PG161 466 as printed: "oNcto gratulatoria ad synodum Ferrariiw". |
| Gennadios Scholarios | CONFIRMED | |
| Symeon of Thessalonica | CONFIRMED | PG155 l.2: "Saeculum XV, annus 1430". |
| Sylvester Syropoulos | CORRECTED (quote) | The title (SYR l.1) reads "unum e quinque crucigeris et intimis consiliariis". The row's restoration "c[ausidicis]" is wrong: read "crucigeris". |
| Nikephoros Gregoras | CONFIRMED | Both quotes are the GREG2 and GREG3 l.10 content notes, not line 39212. |
| John VI Kantakouzenos | CORRECTED (quote not supported) | **"consecratione et damnatione comitante Callistum" is not in CANT2 14919-14925** (that passage is the Kral's demand for cities). It is not anywhere in CANT1-3: "comitante" occurs only at CANT3 4039 and 15164, in other contexts. Remove it; CANT2 11787 has "Callistus, qui postea Constantinopolitanae ecclesiae". The claim that he "signed the Hagioritic Tome as the monk Joasaph" is not in the CANT2 content note; only "later the monk Joasaph" is held (header l.2). Remove that claim too. WHO stands on his own History. |
| Doukas | CORRECTED (form) | "in Asia, where he was probably born" is an English rendering of DOUK 503-504, "in Asia ... in qua ipsum natum fuisse verisimile est, vel in Lesbo". The row drops "or in Lesbos". "quid Florentiae actum sit" is DOUK 797. OUTSIDE WITNESS on the Procopius and Agathias precedent is a judgment call. |
| George Sphrantzes | CONFIRMED | Judgment call on the label (same precedent). |
| Sergius of Radonezh | CONFIRMED | MENAION OCR: "слово похвал'но ... Серг1ю"; 5033 "миъ недостойному Пахомю". |
| Epiphanius and Pachomius (pair) | CONFIRMED | |
| Nil Sorsky | CONFIRMED | NIL OCR: "Предаше ... жительствь", "вкратцв жите". |
| Jan Hus | CONFIRMED | HUSLET l.2. MANSI27 OCR: "De falvo condudiu Joannis Hus". |
| Jerome of Prague | CONFIRMED | MANSI27 1017: "HHieronymi Pragenfis ad objeéta"; 54005: "Hieronymus de Praga, ejufdem Joannis focius". PAL-DOC: "Nulls umquam Stoicorum". HOF2 7717: "Jobanne Hus et Magistro Jacobello de Miza". |
| Petr Chelčický | CONFIRMED | SMET OCR: "narozeny kolem r. 1390", "Má-li aověk". |
| Gregory the Patriarch | CORRECTED (reversed attribution) | **No line reads "Gindely hält Br. Gregor für den Verfasser".** GOLL1 1405-1406 reads "Palacký hält Br. Gregor, den Patriarchen der Unität, für der Autor". Gindely (GOLL1 1460-1461) gives the tract to "einen gewissen Gregor, doch nicht den Gründer". Swap the two names. Death 1474 (GOLL1 1452) confirmed. |
| Nicholas of Pelhřimov | CONFIRMED | HOF2 OCR: "tbaboriensis". |
| Peter of Mladoňovice | CONFIRMED | |
| Lawrence of Březová | CONFIRMED | BREZ 1244-1247 as printed: "duby husitské". |
| Ulrich Richental | CORRECTED (label) | The quotes are confirmed (RICH 437, 682, 815-818). **Drop OUTSIDE WITNESS.** He is a Catholic layman of Constance writing on his church's council, which is the Marcellinus Comes precedent ("Recorder, no label"; Decision-Log l.1992). The label is for historians outside the church. **W2's draft is better supported** (WHO, recorder, thin life flagged, home in the Latin papal entry). Merge W3's life lines into it: RICH 815-830 (called to Hus's execution, found him a confessor; Sigmund kept St John's day on his estate; his travels). |
| Gost Radin | CONFIRMED | TRUH 1078-1082 (OCR "hramovjeh'"); 1466 at TRUH 2 and 28. |
| Jan Žižka (STORY) | CONFIRMED | LUTZ-W 214 and 4573. |
| Prokop the Bald (STORY) | CONFIRMED | |
| Ban Kulin (STORY) | CORRECTED (quote + era) | RACKI-7 2355 reads "bosanski ban Kulin prizna vaše vrhovnu vlast krune ugarsko-hrvatske", not "vašu ... kruni ugarskoj". RACKI-7 2462 OCR: "giješno". **Era:** his acts are c.1180-1204 (abjuration 1203), so he is era 5 by date of work. Carry him to the era 5 supplement (no era 5 row exists). |
| George of Poděbrady (STORY) | CONFIRMED | LUTZ-B 240, 10152, 10275. |
| Euthymius of Tarnovo (WANTED) | CONFIRMED | Not held (no file; no Tsamblak or Цамблак hit in the period; the one hit is a 1887 polemic file). |
| Teodosij of Trnovo (WANTED) | CONFIRMED | RACKI-8 3540-3543 attests the Greek Life by Kallistos, found at Rila by Spiridion; it is not held. |
| Stephen of Perm (WANTED) | CONFIRMED | MOUR 3549-3566 read as claimed. Epiphanius's Life is not held. |
| Joseph of Volotsk (WANTED) | CONFIRMED | Goldfrank is not held (0 hits). The Stoglav (7 hits) and NIL (12 hits) carry no life. |
| Kirill of Beloozero (WANTED) | CORRECTED (lines) | "disciples of St. Sergius" is MOUR 4983, not 4415. MOUR 3499-3502 confirmed. |
| Zosima and Savvatii (WANTED) | CONFIRMED | Solovki hits are 17th-century Old Believer files. |
| *LISTED* Jakoubek of Stříbro | CONFIRMED | HOF2 12854 (the enemy's list). No tract of his is held: the HUSKOR 1311-1752 hits are manuscript descriptions; NEJ 248-581 is Nejedlý's modern account. LISTED stands, with WANTED as the row's own alternative. |
| *LISTED* Laonikos Chalkokondyles | NOT SUPPORTED | "No church-matter hits" is wrong. Held passages: PG159 900-955 (the schism, the Fourth Crusade, John VIII "conscendit navem, et in Italiam profectus est" for the council, "conciliumque concelebrantes"); PG159 5007-5041 (Sigismund and the pope); PG159 25214, 25595-25602 and 47995 (Capistrano). **Proposed: WHO (OUTSIDE WITNESS), thin life flagged, judgment call**, to match Doukas and Sphrantzes. |
| *LISTED* Koranda / Příbram / Isidore / Kallistos / Joseph of Methone | CONFIRMED | LUTZ-W 1247 ("the advice of Koranda, a priest of that city"). PG147 304 OCR: "GALLISTUS PATRIARCHA CPOLITANUS". Joseph's English title is the PG159 l.10 content note, not line 56228. |

## W4

| Person | Status | Details |
|---|---|---|
| Tekle Haymanot | CORRECTED (form + era) | AMDA 12140-12143 is French: "le célèbre Abouna Takla Hayomanot" (as printed "le celebrc abo ana takla hayomanot"). The row gives it in English. GADLA-TH 223 ("about A.D. 370"), 2219-2221 and the l.9 header quote are confirmed. **Era:** the only held date is 1270 (13th century), so he is era 5 by date of work. No era 5 row exists (era 5 Yekuno Amlak uses the same GADLA lines), so he goes to the era 5 supplement unless Mark keeps him here. |
| Timothy II and Ebedjesu (pair) | CONFIRMED | "saeculo XIV. ineunte ... Ebediesus sobensis" is MAI 226-229, not 218-224. MAI 11610-11645 OCR: "definivi ego. "Timotheus". |
| Amr ibn Matta and Sliba (pair) | CONFIRMED | BH3 29196-29198 is a two-column run-together: "anno scilicet 1340, ... florebat Amrus Matthaei". AMR 11226-11227 as printed: "Sumina iiumeri jiatrum ... usque ad lioc tempus". |
| Jean Dardel | CONFIRMED | RHC2 323-330 and 864-866. |
| Daniel of Tauris | CONFIRMED | RHC2 18793-18795; "ung Armin prestre, nommé Danyel" at 18821 and 25398-25399. |
| John of Montecorvino | CONFIRMED | |
| Jordanus Catalani | CONFIRMED | |
| al-Umari | CONFIRMED | OUTSIDE WITNESS. |
| al-Maqrizi | CORRECTED (form) | ABUSAL reads "as it were, hung in the air", not "hanging in the air". |
| Amda Seyon (STORY) | CORRECTED (form) | AMDA 21947-21948 as printed: "v4nerait ies pretres et les moines comme le Seigneur lui-meme". The "second-grade OCR" phrase is in AMDA l.9. |
| Levon V (STORY) | CORRECTED (lines) | "soixante ans" is LANG 1602-1603 ("il mourut en 1393, à l'âge de soixante ans"). RHC2 18884 has only the Paris death in 1393. |
| Mar Jacob (STORY) | CONFIRMED | MING 2250-2254. |
| John de' Marignolli (STORY) | CONFIRMED | The quote is census text. |
| Zara Yaqob (WANTED) | CONFIRMED | As printed: ZY 1867 "les livres écrits par Zar'a"; ZY 7093 "Le Livre de Tincar-nation (?)" and 1922; "enfants d'Estifa" is ZY 6720, not 6739. His books are not held. |
| Ewostatewos (WANTED) | CONFIRMED | LUDOLF 15360 ("no less famous than he") and 15388 ("went into Armenia"). No Gadl is held (the Conti Rossini file is Yared and Pantalewon only). See the edition note in the summary. |
| Estifanos (WANTED) | CONFIRMED | ZY 1140, 1336 ("Bévolte", OCR), 1411, 1585, 1667. Getatchew Haile is not held. |
| Grigor Tatevatsi (WANTED) | CORRECTED (verdict) | Neither named source can carry a life. The Book of Questions is writing; "the Life by his pupils, if one exists" names no source. By the coordinator's rule (era 5 Durand and Toros Roslin rows) this is **LISTED** until a life source is named. ORMANIAN 3956-3972 confirmed. |
| Rashid al-Din (WANTED, OUTSIDE WITNESS) | CORRECTED (verdict) | Under the era 5 coordinator's call (Decision-Log l.2117-2120; Who_Scan_Era5 l.170, "no WHO (OUTSIDE WITNESS) row"), Muslim historians named in no census text and not held go to Open-Gaps as wanted sources, with no row. Rashid is in no era 6 census text (grep: 0). **No row; Open-Gaps entry** unless Mark overrules. CATHAY 5638-5700 confirmed. |
| *LISTED* Hayton | CORRECTED (lines) | Birth is HETUM 317 (not 319); the monk in 1305 is 326 (not 332); death "between 1310 and 1320" is 334-335 (not 340). RHC2 2609-2613 confirmed. LISTED is a judgment call; STORY is an arguable alternative (prince, general, canon, envoy to Clement V). |
| *LISTED* Ibn Battuta / Ibn Khaldun / Abu'l-Fida | CORRECTED (no row) | Not held (file grep: none). Not in the era 6 census (grep: 0). Same coordinator call as Rashid: **no LISTED row; Open-Gaps wanted sources.** |
| *LISTED* Kirakos of Virap | CORRECTED (form) | CHAMICH reads "prudent in counsel, sober in words, rigid in the ractice of self-mortification". The row drops "sober in words," without an ellipsis. |
| *LISTED* Petrus (Maronite) / Joel / Nerses Balients | CONFIRMED | OCR forms: MANSI32 "Nos itaqueé fubditus Petrus"; GRIFF; RHC2 "évèque d'Ourmiah"; CHAMICH "secyetly instigated by wNierses". |
