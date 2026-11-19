# Era 7 Who scan: independent check notes (Opus)

Read-only check of merged_table.md (282 rows; row numbers below are 0-based table rows, as in the table order: 0 = Luther ... 181 = Rutsky, 182-281 = LISTED). No repo edits, no paid calls.

Method. Every short file name in the six File keys was resolved to its file in cic/texts/ (224 keys, all files exist; one collision: `APOL` means Melanchthon's Apology in G1 and Smotryc'kyj's Apologia in G5). For all 182 WHO/STORY/WANTED rows, every quoted string in the Dates, Evidence, ruling and Source-wanted cells was matched by script against the cited lines (window of plus or minus 4 lines, OCR-normalised), then every miss and every low fuzzy score was opened by hand (Read/sed). Years in the Dates cells were checked against the cited lines the same way. WANTED sources were grepped in cic/texts/ filenames, cic/corpus-map/WORKS.yaml and AUTHOR-IDS.yaml. Earlier-era overlaps were grepped in all six Who_Scan_Era files.

## Summary

WHO / STORY / WANTED set (182 rows):
- CONFIRMED: 144
- CORRECTED: 35 (21 line-number or verbatim fixes; 14 verdict, era, label or Major changes)
- NOT SUPPORTED: 3

LISTED spot-check (39 rows read):
- LISTED stands: 33
- CORRECTED: 6 (two duplicates to merge, one verdict change, three era confirmations)

General note on verbatim quoting. Many quotes silently normalise the OCR (long s, broken hyphens, misread letters). Where the change is only a line-break hyphen or spacing, it is counted CONFIRMED. Where the printed letters differ (for example "Araunros" for "Arminius", "1^28" for "1528"), it is listed below, because the rule is "verbatim, OCR spelling as printed".

## Corrected and not supported rows (WHO / STORY / WANTED)

| Row | Result | Correction |
|---|---|---|
| 10 Hubmaier | CORRECTED | VEDDER 564-565 prints "Doctor Balthasar Ifuebmayr zu IVien auff den zehnten Martii Anno 1^28 verbrennt" (OCR). The tract is "Fabri" (Johann Fabri), not "Faber". VEDDER 1532-1534 gives the birth ("probably 1480 or 1481"), not the death, so the Dates cell should cite 1532-1534 for birth and 563-565 for death. |
| 16 van Braght | CORRECTED (era) | Martyrs Mirror is 1660 (the row's own header quote). By date of work this is era 8. Move, and drop "Major? yes" here. |
| 23 Lubieniecki | CORRECTED (era) | Historia Reformationis Polonicae printed 1685 (LUB 5); era 8 by date. The quote "taken by early death before finishing" is a Library header note (LUB 7), not LUB 11848 (which is the Davidis reference). |
| 30 Knox | CORRECTED | KNOX-1 678-681 give "the 24th of November" and "the age of sixty-seven"; the year 1572 is not on those lines. Tag the year as from elsewhere or cite a line that has it. |
| 39 Baxter | CORRECTED (era) | Kidderminster ministry 1641-1660, main works 1650 onward, Reliquiae 1696. Most of the work is after 1650: flag "era 8?" and do not use him as a Major for era 7 Puritanism without Mark's ruling. |
| 42 Campion | CORRECTED | "filled England with his name" is at CAMP 315-317 ("had filled England with / his name"), not 283-307. |
| 47 Arminius | CORRECTED (verbatim) | ARM 402-403 prints "James ARAUNros was born in Oudewater, a small town near Utrecht in Holland, in the year 1560" (OCR). |
| 49 Grotius | CORRECTED | GROT 756-757 reads "Grotius suffered under the ban laid upon his fellow-Arminians", not "shared the ban". BRANDT 54284 gives "the 12th of May" and "a perpetual Imprifoment"; the year 1619 is not on that line. |
| 50 Duplessis-Mornay pair | CORRECTED | "Coligny was assassinated and du Plessis a fugitive" is at CRUMP 1517-1518, not 2421-2423 (2421 is about Damville: "Coligny was his cousin"). Same wrong cite repeats in row 205 (Coligny). |
| 51 Crespin | CORRECTED (verbatim) | CRES-1 176-177 reads: «J'estoi,» nous dit-il lui-même, «au nombre de ceux qui furent spectateurs de sa mort». The quote drops the editor's interjection without an ellipsis. Death 1572 confirmed at CRES-1 168-169. |
| 52 Leger | CORRECTED (era) | Histoire générale 1669, on the Easter 1655 massacre. Era 8 by date of work; drop "Major? yes" for era 7. |
| 55 Morland | CORRECTED (era) | History of the Evangelical Churches of Piemont, 1658, on the 1655 massacre: era 8 by date. Quote as printed at MORLAND 6019-6021: "to prefent thee with it (O poor Church)- on whom no man beftows anything". |
| 62 Canisius | CORRECTED (verbatim) | CAN-65 2671-2672 prints "Diliges Dominum Deum tuum ex jyiar.ii* / toto corde tuo" (marginal note interleaved by OCR). |
| 67 Lainez | CORRECTED (verbatim) | LAI-1 title line 2 reads "Secundi Praepositi Generalis" (genitive), not "Secundus Praepositus Generalis". |
| 75 Giussano | CORRECTED | GIUS-1 245 ("He was born in 1538 when the Lutheran heresy...") is Borromeo's birth, not Giussano's. It is no evidence for Giussano's own life. The only Giussano evidence is the header (GIUS-1 2: 1548-1623, Oblate of St Ambrose). Verdict WHO (thin own life) on the recorder rule still stands. |
| 76 Bascape | CORRECTED (verbatim) | BASC 1 reads "De vita et rebus gestis Caroli S.R.E. Cardinalis, tituli S. Praxedis, Archiepiscopi Mediolani, libri septem"; the quote drops "tituli S. Praxedis" without an ellipsis. |
| 82 Acosta | CORRECTED | "The Pride and Presumption of the Divell is so great and obstinate" is at ACOS 996. ACOS 986-990 is the Fift Booke heading; 993 is the chapter title ("the Pride and Malice of the Dlvell"). |
| 83 Plasencia | CORRECTED | "Fray Puan de" is at BR34 8168, not 8161-8162. |
| 86 Morga | NOT SUPPORTED | Header lines only; no text line opened. The life the WHO rests on is not shown. The text has candidate lines, e.g. MORGA-BR 565 ("written by Doctor Antonio de Morga, alcalde of the court in the royal...") and 597. Open the editors' preface or Morga's own narrative before WHO. |
| 90 Ragueneau | CORRECTED | "i'en fis le rapport a nos Peres" is at JR35 8059-8060 (printed "i’en / fis le rapport a4 nos Peres"), not 8076-8090. 8080-8088 is the English of the captains' speech (correctly quoted). |
| 91 Cocks | CORRECTED (verdict, judgment) | A merchant's diary with passing remarks on padres; no church role and no life told beyond the diary. The like cases Fletcher (251), Olearius (252) and Dallam (281) are LISTED "held observer". Propose LISTED for consistency, or move all four to one ruling. |
| 93 Lucaris | CORRECTED | The title "Cyrilli Patriarcha Conftantino- politani Confeffio fidei" is at LUC-C 46-47, not 181-184. SMITH-L 1367 reads "Narratio de vita, studiit, gestis, &&."; "et martyrio" is not on that line (header only). Birth line SMITH-L 1375-1376 confirmed ("xiii. die Novembris A. C. 1572, perhibetur"). |
| 95 Maxim the Greek | NOT SUPPORTED | The row itself says the trial and imprisonment were not read. The lines opened (MAX1 2, 4166-4167, 8373) give writing and Athos, not a life. The story test is not yet met in held lines. WHO is likely, but it needs one read of the life section first. |
| 98 Kopystensky | CORRECTED | The editor's note is at RIB4 118552-118554 ("12.— Копыстенсвый, Захамя, авторъ «Палиноди»..."), not 118563-118566. |
| 99 Mohyla | CORRECTED | Mohyla's autograph notes begin at VYSH 2462 ("Собственноручныя записки Петра Могилы"); VYSH 2452 is still Vyshensky's text. |
| 102 Hermogenes | CORRECTED (verdict, judgment) | His held texts are patriarchal letters (AAE2), and his life is a chronicle retelling (NOVL). Filaret (161) has the same kind of record and is STORY under the pope-and-ruler rule. Propose STORY for consistency, or make Filaret WHO. Do not keep one of each. |
| 104 Herberstein | NOT SUPPORTED, plus label error | The evidence is header-only ("church passages near file line 9800, 10325-10334" not opened; own life not read). The label is also wrong by BRIEF: OUTSIDE WITNESS is for historians outside the church. Herberstein is a Catholic imperial envoy, so he is inside Christianity. Propose WHO (thin own life) as a recorder with no label, as for Doukas, after the church passages are opened. |
| 106 Alvares | CORRECTED | ALV 9 says "Ethiopia in 1520 to 1526", not 1520-1527. |
| 114 Archdeacon Thomas | CORRECTED (era and rule) | The Coonan Cross oath (3 Jan 1653), the "Intruso" years (1657-58) and the siege (1661) all fall after 1650, so this is era 8 by date. Also, on the rule for founders known through enemies: the life rests on one hostile eyewitness (SEB). The second witness (WHIT, 1873, Protestant) is a later retelling, not an independent early witness to the teaching. Hand to era 8 as WANTED (the community's own documents), not WHO. Drop "Major? yes". |
| 121 Henry VIII | CORRECTED | INJ2 389 is the First Royal Injunctions heading. The Second Royal Injunctions are at INJ2 74 (contents) and 1852 (heading). |
| 130 Holtby | CORRECTED | The birth sentence is at MORRIS3 5021-5022, not 5013-5016. The contents line is MORRIS3 421 ("III. FATHER RICHARD HOLTBY ON PERSECUTION IN"), correct. The ARCH1 header does not contain "John Holtby, Esq."; that is MORRIS3 91, as the ruling cell says. |
| 135 Louis XIV | CORRECTED (era) | The Revocation is 1685: era 8, not "era?". Remove from era 7. |
| 137 James Fontaine | CORRECTED (era) | Born 1658 (header). All of the work is after 1650: era 8. |
| 138 Jean Migault | CORRECTED (era) | 1645-1706, and the dragonnades narrative is of the 1680s: era 8. |
| 162 Kurbsky | CORRECTED (verbatim) | KURB 507 is blank. The heading is at KURB 505 and prints "ОДЯСТОЛЩ ПВОВАЯ" (OCR). "ЭПИСТОЛIЯ ПЕРВАЯ" is a restored reading, not as printed. |
| 172 Angela Merici | CORRECTED (evidence claim) | "Grepped for 'Ursuline': no hit" is false. Ursulines appear in GIUS-1 2065 ("Establishment of the Ursulines of Santa Sofia"), GIUS-2 1178 and 16029, MARIE1/MARIE2 and JR11. Angela herself is named nowhere (confirmed), so WANTED stands. |
| 180 Kuntsevych | CORRECTED (Major) | WANTED rows cannot be map names. Change "yes" to "no (not a WHO)". Quotes confirmed (SUSZ-J 728). |
| 181 Rutsky | CORRECTED (Major) | Same: "yes" on a WANTED row. AZR4 55958-55964 and 26106 confirmed (OCR). |

Note also row 104 and row 108 (Arab-Faqih) take opposite paths: the Muslim partisan correctly gets no label, but the Catholic envoy gets OUTSIDE WITNESS. Only the second is wrong.

Confirmed (144): Luther, Calvin, Zwingli, Bullinger, Beza, Farel (row 5; see Duplicates), Ursinus/Olevianus, Aurifaber, Arndt, Menno Simons, Sattler, Grebel/Manz, Hutter, Riedemann, Braitmichel/Kräl/Zapf, Schwenckfeld, Niclaes, Servetus, Sozzini, Dávid, Przypkowski, Tyndale, Cranmer, Latimer, Jewel, Hooker, Foxe, Melville/Melvill, Wariston, Rutherford, Calderwood, Spottiswood, Richard Rogers, Sibbes, Shepard, Winthrop, Allen, Southwell, Gerard, Mush, Chauncy, Episcopius, Gilles, Perrin, Olaus Petri, Comenius, Blahoslav, Slavata, Ignatius, Xavier, Bellarmine, Borromeo, Teresa, John of the Cross, Nadal, Salmeron, Borgia, Faber, Polanco, Ribadeneira, Gonçalves da Câmara, Sarpi, Afonso I, Lopes/Pigafetta, Ricci/Trigault, Motolinia, Chirino, Salazar, Marie de l'Incarnation, Le Jeune, Brébeuf, Jeremias II, Meletios Pegas, Potii, Smotryc'kyj, Vyshensky, Macarius, Ivan IV (flag kept), Galawdewos, Castanhoso, Arab-Faqih, Paez, Mendes, Zakaria of Kanaker (era 8 flag kept), Gerlach, Menezes, Ludolf (era 8 flag kept), Anneken Jans, Samuel Ward, Margaret Hoby, Wallington, Elizabeth I, Edward VI, Mary I, Bradford, Houghton group, Clitherow, Owen, Magdalen Montague, Weston, Tyrrell, Hales, Schurman, Henry IV, d'Aubigné, Christian III, Paul III, Pius V, Pius IV, Gregory XIII, Sixtus V, Diogo, Álvaro, Yafindgidono Jorge, Naito/Oumemidono, Jean Ingoro, Melchior Bougendano, Michel Fieoyemon, Jean Tingoro, William Adams, Pantoja, Rada, Membertou, Negabamat, Etinechkavat, Meiachkawat, Chihwatenhwa, Filaret, Afanasii Filippovich, Bermudez, Abdisho IV, Melanchthon (WANTED), Argula von Grumbach, Katharina Schütz Zell, Marie Dentière, Perkins, de Nobili, Gracián, Valignano, Fucan, Xu Guangqi, Guaman Poma, Las Casas, Sahagún.

Checks on the confirmed rows. Ignatius (60): born 1491 at IGN-AUT 2176 and died 31 July 1556 at 2530, as cited. Xavier: COL-1 checked. Calvin: CLET1 1382-1383 ("Bom at Noyon the 10th of July 1509"). Teresa: TERES-L 1726-1728. Sibbes: SIBBES 1540-1541 (Tostock, 1577). Membertou: the register at JR1 5571-5575 itself says "over one hundred years old", so the age is a held claim, not invented. Holtby's date: Morris's own "according to Father Henry More". No invented family, age or anecdote was found in any row. Every family or age detail checked (Luther's miner father, Campion's publisher father, Knox's age 67, Sibbes's parents, Afonso's son Henrique at PAIVA 566-567) is on a held line.

WANTED sources: the 16 named sources are not held. I grepped cic/texts filenames, WORKS.yaml and AUTHOR-IDS.yaml for camerarius, grumbach, zell, dentière, perkins/clarke (only W. K. Lowther Clarke's patristic translations), nobili, merici, gracian/gratian, valign, fucan/habian, guangqi, guaman/poma, casas, sahagun, josaphat/kuncev (only Susza and Guépin, as the rows say), rutsk/velamin. All are absent as stated.

Melanchthon (166). WANTED is correct by the rules: two of his works are held, but no life is held anywhere. A grep for "Bretten" and "Melanchthon was born" finds nothing. Mark should still see that the most important Lutheran after Luther is off the map for want of Camerarius.

## LISTED spot-check (39 rows)

LISTED stands (33). For each, held lines were read or the Library was grepped:
- Wittenberg and Anabaptist: Katharina von Bora (TT has one "Kate" line, 3014; nothing tells her life), Johann Walter (LV6 13169), Bugenhagen (no file of his), Dirk Philips (judgment call stands: the Enchiridion is doctrine), Widman (GB 332, OCR "fiindert ... Mikolsburg").
- Spiritualists: Sudermann, Franck (judgment call stands), Knewstub/Rogers/Wilkinson, Tobias.
- English: Ames, Morgan, Bancroft, Persons (no file; Parsons of St Colette is a namesake, correctly flagged), Garnet, Pole (era 6 has no Pole row; "Pole" hits there are other words).
- Scandinavia: Gustav Vasa (ruler with no own text), Agricola (no file), Laurentius Petri, Glostrup.
- Waldensian, Huguenot, Dutch: Olivetan (MORLAND 5764 and 6019-6021 confirmed), Milton, Coligny (fix the same CRUMP cite as row 50: 1517, not 2421), Teellinck, Voetius, Oldenbarnevelt (BRANDT 53914-53916, OCR).
- Catholic and Carmelite: Ana de Jesús, Luis de Granada, Quiroga.
- East: Skarga (hostile-writer rule; judgment call stands), Artemii, Sulaqa (the quotes are at ASSEM2 11994-11995 and 12034-12036, OCR "elegeriintque fibi ... Hormifda"; LISTED stands under the later-retelling rule), Susenyos, Movses III.

CORRECTED (6):
- 204 Guillaume Farel: a duplicate of row 5 (William Farel, WHO). Merge into row 5.
- 206 Clement Marot: a duplicate of row 193 (Clément Marot). Merge.
- 223 Philip Neri: LISTED does not stand on the stated ground. BACCI is Pietro Giacomo Bacci's Italian Life of 1622 (BACCI 2), written 27 years after Neri's death and in effect the standard early Life. Era 7 treats other early hagiographies as carrying a life: Giussano (1610) and Bascapè (1592) for Borromeo, Ribadeneira for Ignatius, the Quiroga-based Life for John of the Cross. Neri founded the Oratory and has a following. Propose WHO (hagiographic Life, genre marked) as a judgment call for Mark, not LISTED.
- 212 Brandt, 218 Challoner and 219 Dodd: the era flags are right but should not be "era?". Brandt's history is 1671-1704 and Challoner's is 1741, and Dodd's is likewise after 1650, so all three are era 8 or later by date. Remove all three from era 7.

## Duplicates

- Farel: row 5 (William Farel, WHO) and row 204 (Guillaume Farel, LISTED). Same man. Keep one row; the verdict is Judgment call 3 in G1.
- Marot: row 193 (Clément Marot) and row 206 (Clement Marot). Same man, both LISTED. Merge.
- Jean Ingoro (149) and Jean Tingoro (152), both from PAGES. Possibly one man. The Pagès index has an entry "FATTORI TINGORO (Jean), jifiaque" (PAGES 23198) and "TINGORO (lettres de Jean), A, 89 et 90" (25819), but no INGORO entry at all. Both letters are by a "Jean" of the Yatsushiro or Arima Christians. Not resolved: check the index for annex pages 62-63 before profiling both. Row 235 ("the three Jifiaqua", PAGES 3205) may also include Tingoro, since he is indexed as a jifiaque.
- Brébeuf (89) and Chihwatenhwa (160): no duplicate (Brébeuf is only named in the row label).
- Already-merged pairs check out: Ricci/Trigault one row (80), with Pantoja (154) and Xu Guangqi (176) separate; Xavier one row (61); Acosta (82) and Chirino (84) one row each; Herberstein one row (104), under HERB and HERB-NR, two keys for the same file; Duplessis-Mornay/Mornay one row (50); Sakovych one row across two entries (245).
- Earlier eras: none of the 282 people is scored as a row in eras 1-6. Era 6 handed Barbosa, Alvares, Castanhoso, Telles, Gouvea, Menezes, Ludolf and the Houghton group to era 7 by date (Who_Scan_Era6 line 304); they appear here once each, which is correct. Era 6 has rows for Gennadios Scholarios, Bessarion, Joseph of Volotsk, Nil Sorsky and Savonarola, and none of them is rescored here. Maxim the Greek, Erasmus, More and Fisher have no row in any era (Erasmus, More and Fisher are absent from era 7 too; not checked whether the census names them for era 7).

## Verdict / era changes (consolidated)

Era 8 by date of work (after 1650). Move out of era 7:
- Already flagged: 23 Lubieniecki (1685), 111 Zakaria, 115 Ludolf, 135 Louis XIV (1685), 137 Fontaine, 138 Migault, 212 Brandt, 218 Challoner, 219 Dodd, 271-278.
- Not flagged, but should be: 16 van Braght (1660), 52 Leger (1669), 55 Morland (1658), 114 Archdeacon Thomas (1653 onward).
- Era? (mostly after 1650): 39 Baxter.

Before 1517: none found. Alvares (embassy 1520-26), Maxim (in Moscow from 1518) and Luther (1517) are all in era 7.

Verdict changes proposed:
- 114 Archdeacon Thomas: WHO to WANTED, for the era 8 desk, under the rule for founders known through enemies.
- 104 Herberstein: drop the OUTSIDE WITNESS label (he is a Catholic envoy, so an inside writer); WHO (thin own life) once the church passages are read.
- 102 Hermogenes and 161 Filaret: make them consistent. Recommended: both STORY (patriarchs with official letters).
- 91 Cocks: WHO to LISTED, held observer, consistent with 251, 252 and 281 (judgment call).
- 223 Philip Neri: LISTED to WHO (judgment call; Bacci 1622 is an early source).
- 86 Morga and 95 Maxim the Greek: hold WHO until one life line is opened.

## Major? flags

- The Anabaptist Movements has 5 "yes": Menno Simons, Hubmaier, Sattler, Grebel/Manz, van Braght. Keep Menno, Grebel/Manz, Sattler and Hubmaier. Drop van Braght: he is a recorder and era 8 by date.
- No other tradition has more than 4 "yes", but some "yes" rows are ineligible:
  - Josaphat (180) and Rutsky (181) are WANTED, not WHO. Union of Brest is then left with Smotryc'kyj (97), and Potii (96) sits under the variant label "Union of Brest and Ruthenian Greek Catholic Christianity". Normalise the tradition label so the 4-name count is right.
  - Era-8-by-date "yes" rows: van Braght (16), Leger (52; the Waldensian-Reformed Union would then have no Major, with Gilles or Perrin, both thin, the only era 7 candidates), Archdeacon Thomas (114; St Thomas Christians keeps Menezes), and Baxter (39) if moved (Puritanism keeps Sibbes and Shepard).
- At exactly 4: English Reformation (Tyndale, Cranmer, Hooker, Foxe) and Recusant English Catholicism (Allen, Campion, Southwell, Gerard). Both are fine.
