# R1 review: Library era 8 batch 1 (32 files), 2026-11-15

**Verdict: PASS WITH FIXES.** No rights error was found in any of the 32 files. Two wrong facts in headers need fixing before the batch passes (findings 1 and 2); the rest are small.

All line numbers below are this file's own lines ("file line") unless marked OCR. Page images could not be seen; the archive.org catalog dates and byte counts could not be checked.

## Findings

### BLOCKING

**1. Vansleb, Histoire de l'Église d'Alexandrie: the source named for the catalog of patriarchs is wrong.**
- File: `cic/texts/vansleb_histoire-de-l-eglise-d-alexandrie-fra_1677.txt`, header line 9 (repeated in the REGISTRY notes).
- The record says Part VI is "drawn from al-Maqrizi and other Arabic authors".
- The Part VI heading at file lines 14107-14119 reads "tiré de l'e^-hMaracat & de plusieurs autres Autheurs Arabes". The garbled word is "Abulbaracat", which the OCR gives about fifteen times elsewhere (for example file lines 1290, 3735, 12961, 15365 "Patriarches d'Abulbaracat").
- "Macrizi" appears only twice, inside the text (14903, 14915), not in the heading.
- Fix: name Abulbaracat as the heading does, or say only "Arabic authors he names", as the caution already does.

**2. Rhodes, Divers voyages: the author is credited to a title page that does not show him.**
- File: `cic/texts/rhodes_divers-voyages-de-la-chine-et-autres-royaumes-de-l-orient-fra_1682.txt`, header line 2: "Creator: Alexandre de Rhodes (title page)".
- The OCR title page (file lines 44-70) and the second title (130-142) say only "Avec le retour de l'Autheur en Europe". The privilege extract (83-96) names no author.
- "Rhodes" occurs nowhere in the OCR. The only internal trace is "Pere Alexandre" at file line 6301.
- The staging file has no `authors_ruled` entry, unlike the other files whose title pages name no author.
- I could not see the page image. Unless it shows the name, the attribution rests on outside knowledge and the header must say so, with the internal evidence and an `authors_ruled` entry.

### SHOULD FIX

**3. Al-Jabarti: two translators' names are transcribed wrongly.**
- Header lines 1-2 give "Abdulaziz Khalil Bey" and "Gabriel Nicolas Khalil Bey".
- The title page at file line 58 reads "ABDULAZIZ KAHIL BEY - GABRIEL NICOLAS KAIIIL BEY". Take the spelling from the print (check the page image), not "Khalil".

**4. Pallu: the publisher is credited to a title page that does not show it in the OCR.**
- Header line 3: "Paris: chez Charles Angot, rue Saint Jacques, au Lion d'Or (title page)".
- The OCR title page (file lines 51-70) has no publisher line, and "Angot" occurs nowhere in the file.
- If it was read on the page image (leaf n2, as the year was), the header should say so.

**5. Historia cultus Sinensium: four points.**
- **Imprint.** Header line 4 says the OCR does not give the numeral. True of the first title page (file lines 25-51), but the second title page prints "COLONIAE" (15974) and "M. D C C." (15983). Cite it; the year is then confirmed in the file.
- **Label.** The header calls OCR 254-7940 "the Historia in five sections". At file lines 266-283 this is the body of Charmot's Notae of 29 July 1698 ("Patres Societatis ... in hisce Observationibus ... At contra ego contendo"). "Historia cultus Sinensium" there is the volume's running head, not a heading. My reading from a short sample; worth a second look.
- **Staging row 2.** It puts the Jesuit observations (OCR 27431-32074) under `author: charmot`, `role: tradition`. File lines 27443-27472 are the Jesuits' own voice ("sperat Societas"). The note warns of several voices, but the row's author is wrong for that span. Split it or drop the span.
- **Staging evidence and date source.** The Charmot evidence cites "file lines 134-145"; his name stands at file line 158 (heading 138-169). The Mandate's date source says the year 1693 is read "from Launay", but Launay's OCR reads "26 mars 1698" (Launay t1 file line 35031), as the batch's own caution says. Drop Launay or cite a line that reads 1693. The piece dated "decima Novembris 16931" (file 18829) and the garbled "1^3" (file 15927) are the real support.

**6. Rhodes cautions and staging notes: "before the window" contradicts the print dates.**
- CFT-Wants line 733: "All three works come before the entry's window of 1650."
- The prints are 1651, 1652 and 1682. The Cathechismus staging note says "Printed just before this entry's window", which 1651 is not if the window opens in 1650.
- I could not find the entry's window in the corpus-map file. State the window's opening year, and say whether the missions described or the prints are meant.

**7. McCarter: the staging note and caution say something "was not read" that the preface answers.**
- Staging note and CFT-Wants line 700: "Whether he writes from inside the church was not read in the preface."
- File lines 83-89: "the personal knowledge acquired during several years' pastoral labour among the South African Dutch colonists."
- Record that, and rule the role on it.

**8. Roles: two "later accounts" are shelved as `tradition`, against the batch's own practice.**
- The Ceylon Sketch (1848, on the Dutch years) and McCarter (1869, on the Cape church) are `tradition`.
- Launay (1894, a member of the Society) and Pascoe (1901, the Society's own digest) are `context` for the same reason.
- Both rows are `needs-ruling`, so this is a flag for the ruling, not an error.

**9. Parry: the microfilm target carries a permission line the records do not mention.**
- File lines 30-32: "Reproductions may not be made without permission from Columbia University Library."
- The header and Search_Log describe only the photocopying statement, while the Search_Log rule says "no permission notice".
- The imprint is 1895 (file line 388), so the rights hold. Record the line and the call on it.

**10. Rhodes, Divers voyages header carries a tracking reference.**
- Header line 9: "the Wanted_Sources row names a first printing of 1653, which was not looked for in this print."
- That is process talk in a live file, and 1653 is not from the print.

**11. Spelling: "licence" is British.**
- It is used as a noun throughout what the batch wrote: headers (Present State, Cathechismus, both Vieira parts, Barros, both Cartas, Antonil), staging rows, REGISTRY, the seed, CFT-Wants and Search_Log.
- American spelling is "license".

### NOTE

**12.** Vansleb Histoire, header line 4: "the OCR does not give the numeral". File line 63 reads "M. pC. LXXVII." Search_Log line 54 repeats the claim.

**13.** Proyart: the approbation is given as 26 May 1770 (header, staging). File line 13595 does read "26 Mai 1770-", but six years before a 1776 imprint is odd. Check the page image before anyone quotes it.

**14.** Launay t1 header: the first copy of the synod passage reads "14 février 1679" (file 12419); the second reads 1670 (13781). The caution says so; the header does not.

**15.** Rhodes, Tunchinensis: the "privilege (Avignon, 1 May 1651)" at file lines 639-653 is the Jesuit provincial's permission under the Society's privilege, not a royal privilege.

**16.** Cathechismus header: title page "OCR 1-24" and Vietnamese title "at line 16" are about four lines early. They stand at file 17-40 and 32-33 (OCR 5-28 and 20-21).

**17.** Pascoe: the staging note and caution say "the Society's secretary". The title page (file line 90) says "Assistant Secretary", as the header does.

**18.** Al-Jabarti caution: "the other El Djohari passages are a Muslim sheikh". There are at least two men (file 1139, 6716) and a book title (4157).

**19.** Vansleb, Nouvelle relation: the staging note says "journal of 1672-1673", while the journal opens 8 May 1671 (file 400) and the row's date starts 1671. "En 1672 et 1673" in the header title is not in the OCR title page (file 36-60).

**20.** Gobat, staging row for Lee: "title page: 1834". The OCR title page (file 81-109) prints no year; say it was read on the page image.

**21.** Antonil staging: licences cited at "OCR lines 351-419" stand at file 363-422 (OCR 351-410).

## A. Rights check, all 32 files

| # | File (short) | Imprint as read (file line) | Result |
|---|---|---|---|
| 1 | Proyart 1776 | "M. D C C. L X X V I.", Paris/Lyon (52-64) | OK |
| 2 | Pascoe 1901 | "1901." (122) | OK |
| 3 | McCarter 1869 | "1869." (37) | OK |
| 4 | Bruce v2 1790 | "™.DCC.XC," Edinburgh, Ruthven, Robinson (145-154) | Consistent, not independently confirmed (first letter only) |
| 5 | Bruce v3 1790 | "M,DCC, XC," (75) | OK |
| 6 | Butcher v2 1897 | "1897" (60) | OK |
| 7 | Vansleb Histoire 1677 | "M. pC. LXXVII." (63) | OK |
| 8 | Vansleb Nouvelle relation 1677 | "M. D C. L XX V 1 1~" (59) | OK |
| 9 | Vansleb Present State 1678 | "1678." (54) | OK |
| 10 | Al-Jabarti t5 1890 | "1890" (74) | OK |
| 11 | Gobat 1834 | No year in the OCR title page; London, Hatchard, Seeley (81-109) | Consistent, not independently confirmed |
| 12 | Parry 1895 | "1895." (388); see finding 9 | OK |
| 13 | Guidi Versio 1912 | "MDCCCCXIL." (305) | OK (last stroke garbled) |
| 14 | Guidi Textus 1910 | "MDGCGGk" (177) | Consistent, not independently confirmed |
| 15 | Vieira Rosa p1 1686 | "M. DC. LXXXVL" (49) | OK |
| 16 | Vieira Rosa p2 1688 | "Anno M. DC. LXXXVIII" (109) | OK |
| 17 | Barros 1746 | "M. i>.CC.XI,Vi" (60); licences 1745-1746 (812-852) | Consistent, not independently confirmed |
| 18 | Vieira Cartas t1 1735 | "M.DCC.XXXV," (85) | OK |
| 19 | Vieira Cartas t2 1735 | "M.DCC.XXXV." (66) | OK |
| 20 | Antonil 1711 | "Anno de 1 7 1 1." (92) | OK |
| 21 | Code noir 1767 | "M. DCC. LXVII." (106); Prault only in the privilege (236) | OK |
| 22 | Launay t1 1894 | "1894" (49) | OK |
| 23 | Launay t2 1894 | "1894" (66) | OK |
| 24 | Pallu 1682 | "M DC. LXXXfL" (69) | Consistent, not independently confirmed |
| 25 | Rhodes Divers voyages 1682 | "M. DC.' LXXXIL" (68) | OK (final I read as L) |
| 26 | Rhodes Tunchinensis 1652 | "tJM. 7)Cr LJ I." (58); permission 1651 (649) | Consistent, not independently confirmed |
| 27 | Rhodes Cathechismus 1651 | No year on the title page (17-40); licence "Roma 8 Julij 1 6 j i." (90) | Consistent, not independently confirmed; catalog agreement not checkable |
| 28 | Historia cultus 1700 | First title: no imprint in OCR; second title "COLONIAE", "M. D C C." (15974, 15983) | OK by the second title page |
| 29 | Ceylon Sketch 1848 | "Colombo 1848" (94-95) | OK |
| 30 | Baldaeus Dutch 1672 | "Anno 1672." (84; again 62845) | OK |
| 31 | Baldaeus English 1703 | Engraved title "L703", Churchill (671-673); letterpress has no imprint | Consistent, not independently confirmed |
| 32 | Valentijn deel 3 1726 | "£19 GCXXVl" (158); second stuk "MDCCXXVI." (91592) | OK by the second title page |

No PROBLEM.

## B. Files checked in detail

Fourteen files, four or more ranges each; all matched to within a few lines unless a finding says otherwise.

1. **Historia cultus Sinensium.**
   - Charmot's Notae title, 29 July 1698 (file 138-169); Praefatio (183); Sectio prima (266).
   - Brief of Innocent XII (7953-7963); Notationes, 7 October 1698 (8206-8239).
   - Mandate heading (15635-15651), text from "CArolus Maigrot Sacerdos" (15655).
   - Date line "Datum in Oppido Chang Lo ... die vigesima sexta mensis Martii anni Domini 1^3" (15924-15927); signature (15932-15934). The bounds OCR 15623-15921 are right.
   - Second title page (15937-15983); the piece of 10 November 1693 (18828-18834); Jesuit Prima pars (27443).
2. **Al-Jabarti t5.** Year 1202 heading (108-109); obituary "Est mort aussi le chrétien Moallem Ibrahim el Djohari" to "mois de Zilkadé" (9409-9440, OCR 9397-9428 exactly), under 1209; year 1210 heading (9443); "Fin du tome cinquième" (10510). The row's wording is supported by the text.
3. **Code noir.**
   - Edict of March 1685: heading (1284-1296), Article premier (1343), LX (2354).
   - Date "au mois de Mars mil six cens quatre-vingt cinq" and signatures (2392-2399); registration at Saint-Domingue, 6 May 1687 (2401-2405; the OCR reads "1637" here, the heading at 1296 reads 1687). The bounds are right.
   - Louisiana edict: heading (11072-11089), date (12468-12471); privilege of 24 May 1759 (321-323).
4. **Rhodes, Cathechismus.** Licence of Goswinus Nickel with its date line (80-92; OCR 78 for the date, as the staging says); imprimatur (95-98); Dies primus (121); Dies secundus (1851); Dies octavus (21305) and its Vietnamese (21338); Errata (25910).
5. **Launay t1.**
   - Chapitre I, 1658 (631-632); Chapitre IV, 1664-1665 (7514-7516); Monita summary (9413-9428).
   - Synod of Tonkin (12418-12430; twin at 13781-13806).
   - Chapitre XII, 1692-1700 (34505-34506); "M. Maigrot essaya d'arrêter les contestations par un mandement" (34861); articles quoted "Premièrement, nous ordonnons" (35107) to their close (35392); "Fin du tome premier" (49958).
6. **Vieira, Rosa p1.** Sermam I (323); Sermam XIV heading "Na Bahia, a Irmandade dos Pretos de hum Engenho ... Anno de 1633" (40129-40133), exact; "fim" (45962); index (45971).
7. **Bruce v2.** Book IV heading (18114-18124); Facilidas (18130-18133); David "From 1714 to 1719" with the convocation (25635-25671); the Capuchins named, to the stoning (25940-25969); "End of the second volume" (31733).
8. **Butcher v2.** Chapter XXXII (9093); the first Roman Catholic metropolitan, 1741 (12626-12632); the footnote on "Moallem Ibrahim-el Johari" (13304-13311, exact); Chapter XLI (15254); "Johar" elsewhere is the Fatimid general (178-529).
9. **Ceylon Sketch.** Text start (112-124); the placards of 1658 and 1715 (617-647); Vaz from Goa, 1690 (766-770); his death at Kandy, 17 January 1711 (907-908); the regulation of 1806 (1072-1083).
10. **Pallu.** First privilege and approbation naming Bourges (19-48); dedication signed and dated "ce mois d'Avril 1668" (162-168); second privilege and approbation, April 1666 (174-203); Relation begins (209-216).
11. **Baldaeus Dutch.** Privilege, 1669 (136-138); dedication "Geervliet den 15 Aug. 1671" (287-292); Ceylon and its first chapter (30640-30650); a Jaffna church and school (54387-54405); the third part's own title page, 1672 (62809-62847).
12. **Antonil.** Part I (199-207); licences, December 1710 to 6 March 1711 (350-422); the chaplain's duty (873-895); Chapter IX on the slaves (1330-1334).
13. **Rhodes, Tunchinensis.** Permission, Avignon, 1 May 1651 (639-649); Liber primus and Caput I (669-674); Liber II and Caput I (4461-4489); Finis (12691).
14. **Gobat.** The Society's preface (234); Lee's Brief History (675-683); Journal heading and "Feb. 25, 1830" (2835-2843); general remarks (13768-13775).

Spot checks also held in:
- Rhodes, Divers voyages: Part 1 (265-275); departure of October 1618 (386).
- Proyart: Part 2 half-title and chapter (7240-7256); approbation (13585-13596).
- Guidi Versio: Latin note (334-388); Iyasu heading (405); Iyo'as heading (10569); Observation (15804); additions (15814).
- Pascoe: Chapter XXXV (25578); Thompson (25627).
- Parry: the translated Arabic manuscript (20612).
- Valentijn: both title pages.
- Present State: journal opening (163).
- Nouvelle relation: journal opening (399-400).

## C. Staging files and CFT-Wants

- All 32 staging files were read. Apart from findings 2, 5, 6, 7, 8, 19, 20 and 21, the roles, loci and date sources agree with the headers and with the lines checked.
- The CFT-Wants table: every word count, year, language and shelf agrees with the headers and staging rows. The table omits the `needs-ruling` flag on some second rows (Proyart part 1, Lee, Baldaeus part 1 and 3, Valentijn's second stuk); the staging files carry it.
- The cautions on Launay ("26 mars 1698", the year 1679), Butcher, the Code noir (file lines 1284-2405), the Historia (file lines 15635-15933), Bruce and Pallu all match the files.

## D. Search_Log

Two statements disagree with the files: the claim that the OCR of Vansleb's Histoire does not give the year (finding 12), and the description of Parry's microfilm target against the log's own "no permission notice" rule (finding 9). Nothing else in the log contradicts what I read.

## Not checked

- Page images, archive.org catalog dates, rights fields and byte counts.
- Most of the REGISTRY and seed entries beyond the three sampled (they repeat the headers).
- The Ericeira claim in the Cartas headers, and the content ranges of the files not listed in B.
- The window years of the atlas entries.
