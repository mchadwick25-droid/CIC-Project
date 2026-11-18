# Opus check of the Who scan, era 8 (1650–1815), 2026-11-12

Read-only on the repo. No paid calls. The scan table was corrected in place; the first-pass draft is not kept.

**Method.** For every WHO, STORY and WANTED row (223 rows), a script ran every quoted phrase against the cited line range in `cic/texts/`, with the group's own file key. The match was whitespace- and punctuation-normalised and allowed 6 lines either side. Every miss (134 phrases in 60 rows) was then opened by hand with `sed -n`. Most misses were the script's fault, not the row's:
- OCR differences (long s read as f, broken ligatures, hyphens across lines);
- quotes taken from a file's header or Content note;
- rows that cite two ranges ("FOX1 404, 543"), where the quote sits in the second one.

For every WANTED row I searched the `cic/texts` file list and the full text for the named source (author, short title, distinctive title words). I also read the story-test sentence of every WHO row. Line numbers are the file's own (`sed -n` / `grep -n`).

## Counts

- Main rows (WHO, STORY, WANTED): **223 checked: 211 confirmed, 12 corrected, 0 not supported.** One claim was not supported: the Mazel quote at CT1 1904. The row was corrected and its verdict stands.
- LISTED spot-checks: **46**. 43 confirmed, 1 corrected (Edmund Jones, merged), 1 rescored (William Lee: LISTED → WHO), 1 merged and removed (Joseph II).
- Duplicates removed: **4 rows** (Benedict XIV, Macarius III Zaim, Joseph II, Edmund Jones). No one in the table was already scored in eras 1–6.
- Invented person-detail: **none found.** The closest cases are a third-person report turned into a first-person quote (Mar Dionysius) and a quote found in no held line (Mazel).
- Rows: 397 → **393**. Final totals: **WHO 128** (of which OUTSIDE WITNESS 5), **STORY 47**, **WANTED 47**, **LISTED 171**. 12 columns in every row.

## Table of changes

| Row | Change | Why |
|---|---|---|
| James Whittaker (WHO) | "TEST 654-657 (contents …)" → "SUMM 654-657" | The contents lines with "Elder William Lee, 38" and "James Whittaker, 42" are in SUMM 650-657. TEST 650-658 is narrative. |
| Petrus Joannes Meindaerts (WHO) | Confidence clear → judgment call | The record is his office and its acts (pastoral letter, synod presidency, consecrations), with no life outside them. That is thin for the story test. WHO kept. |
| Fénelon (WHO) | INN 1150-1161 → 1150-1162 | The quoted letter ends at 1162 ("coûterait cent fois plus à mon cœur"). |
| Mar Dionysius I (WHO) | "I am the father of 54 churches" → he "called himself 'the father of 54 churches in [a] heathen land'" (WHITEHOUSE 19612-19614) | The held line is a third-person report. The first-person wording was not in the source. |
| Macarius III Zaim of Antioch and Paul of Aleppo (WHO, pair) | Merged with the separate "Macarius III Zaim" WHO row (C2 group). Traditions, evidence (PAUL-1 973-978, CHARON 24445-24446) and source tag added. The merged rows' Major? said "no" and "judgment call"; both are recorded. | Same person scored twice. |
| Macarius III Zaim (Macarius of Antioch) (WHO) | Row removed | Duplicate (see above). |
| Antoni I (STORY) | "a footnote says he 'adopted the Catholic religion'" → Brosset's own French, "ayant faibli et adopté la religion catholique", BROS2 14015-14016 | The English was a rendering presented as a quote, with no line given. |
| Benedict XIV (STORY, the C2/D row) | Society of Jesus tradition added; marked merged | Same pope scored twice. |
| Benedict XIV (STORY, the B2 row) | Row removed | Duplicate. Its only evidence (MIRBT 22854-22862) is already in the kept row. |
| Maria Theresa and Joseph II (STORY, pair) | The LISTED "Joseph II (Holy Roman Emperor)" row merged in: three Protestant traditions, FERC75 1171-1173, FERC07 1221-1223 | Same man scored twice, once STORY and once LISTED. |
| Joseph II (Holy Roman Emperor) (LISTED) | Row removed | Duplicate. Note: the two drafters read the ruler rule differently. One gave STORY to a ruler with no held text; the other gave LISTED because no text is held. This is flagged in the kept row for Mark. |
| Thomas Bray (WANTED) | Quote back in printed order: "appointed the Reverend Dr. Bray his Commiffary in Maryland", HUMPH 1424-1425 | The row had the words reordered. |
| Abraham Mazel (WANTED) | CT1 1904 quote ("l'auteur par inspiration et le chef du soulèvement") removed. CT1 2191, 2701 and 3087 do not name him. Replaced by CT1 2898-2900, 3196-3199 ("tel ctait un Abraham Mazel", OCR as printed) and 4053-4056 | **Not supported**: the phrase is in no held line (grep of all three Court volumes and the whole corpus). The verdict stands. Mazel's memoir is still not held. |
| William Lee (LISTED → WHO, judgment call) | Rescored and moved into the WHO block after Whittaker. Dates added: b. 1740 Manchester, d. 21 July 1784 (SUMM 2916-2918, 3136-3137) | The drafter cited "TEST 654", but that contents line is SUMM 654. SUMM 2914-3137 holds a full life: blacksmith, officer in the Oxford Blues, conversion "he gave the following account of himself", the mobs, his death. TEST 374-376 has a second life chapter. He is one of the first elders, so he stands on the same footing as Whittaker. |
| Edmund Jones of Aberystruth (LISTED) | Merged with "Edmund Jones (the 'Old Prophet', Pontypool)". English Old Dissent tradition added | Same man and the same file (`jones-edmund_account-of-the-parish-of-aberystruth_1779`). |
| Edmund Jones (the "Old Prophet") (LISTED) | Row removed | Duplicate. |

## Per-row outcomes: main rows

**Corrected (12):** the rows in the table above. That is Whittaker, Meindaerts, Fénelon, Mar Dionysius I, the Macarius/Paul pair, the dropped Macarius row, Antoni I, Benedict XIV (kept), the dropped Benedict XIV row, Maria Theresa and Joseph II, Thomas Bray and Abraham Mazel.

**Confirmed (211): every other WHO, STORY and WANTED row.** Points worth knowing, with no change made:
- **OCR-only differences** (the row's quote is a fair reading of the print). Fell, Woolman, Mary Fletcher, Coke, Rowland, Acrelius (caps), David George, Philip Henry, Murray, Freeman, Swedenborg, Ziegenbalg, Bengel, Sauer, Christian David, Dober and Nitschmann, Anna Nitschmann, Steenoven, Varlet, Meindaerts, Rabaut, Agnès Arnauld, Marion, Paisius Velichkovsky, Filippov, Mekhitar, Sor Juana, Serra (PALOU-ES 12716-12719, "el dia del Señor San Agustín del añode 1784"), Palóu, Bownas, Churchman, Agnes Beaumont, Leontiev, Carli, Zucchelli, Carey, Fuller, Maigrot, Pedro IV, Njinga.
- **Quotes from a file's Content note**, verified there: Nayler (NAYL 8), Ellwood, Whitefield, McNemar, Spangenberg ("by a bishop who knew him", SPANG 8), Muratori (MUR 9).
- **English renderings of non-English text**, shown in quotes but not misleading:
  - Reitz: "to the Christian-minded reader" renders REITZ2 58, "Den Chriſtlich-geſinnten Leſer".
  - Lombárd: all the MAG61 quotes are marked "rendered". I checked them at MAG61 6932-6935, 7136-7141, 7632-7638 and 7787-7792. One nuance: Fejérvári gave the sermon over him ("beszédében"); the oration (oratio) was Agh István's (MAG61 7790-7791).
  - Njinga: "most beastly" renders CAV's "il più beſtiale".
- **Dates checked by hand:**
  - Hochmann: BRUM 1308-1309, 1364-1368, 1486-1487, 1508-1514. "about 1670" carries a footnote mark, so "no source given" may be too strong.
  - Abraham of Crete: "presided over the Armenian church three years", CHAMICH 22402-22403.
  - Pius VI: Baldassari is "Chapelain ordinaire" at BALD 159.
- **Story test.** These WHO rows pass only through the recorder rule and are correctly flagged: Reitz, Cranz, Loskiel, Oldendorp, La Trobe, Freylinghausen, Makraios, Basilovits, Palóu, Jesse Lee and Belsham. Meindaerts is now a judgment call (see changes). No other WHO rests on doctrine alone.
- **WANTED not-held searches.** No file and no text hit holds a life-telling source for any WANTED row. The search terms included: Confession and Retractions, Spiritual Travels, Lemuel Haynes, Sarah Crosby, Work of Faith, Gracious Dealings, Memoirs of … Watts, Job Orton, Rise and Progress of the New Jerusalem, The Gleaner, History of My Own Time, Ammann, Lebens-Beschreibung, Protten, Marsollier, Bernardo da Gallo, Úrsula de Jesús, Maria Rosa Mystica, Joseph Vaz, Travels to Discover the Source, Jabarti, Chebotarev, Davies vol. 1, Arnold. Held files sit beside some of them but do not carry the life: Occom's sermon, Davies vol. 3, Dutton's letters, Watts' hymns, Doddridge's Rise and Progress, Burnet's two tracts, Wilberforce's Practical View, Hannah More's tracts (CHEAP), Rancé's own treatise, and `henry-philip_diaries-and-letters_lee1882` (Philip's, not Matthew's).
- **Arnold (WANTED).** The named source (the Kirchen- und Ketzer-Historie) is a work, not a life. It still supports WANTED under the recorder rule, as the row argues.

## LISTED spot-checks (46)

Confirmed (43): Robert Barclay, Charles Chauncy, Gilbert Tennent, Peter Bohler, Griffith Jones, Benjamin Seth Youngs, Valentine Rathbun, Isaac Backus, John Rippon, Elhanan Winchester, Hosea Ballou, John Biddle, Joseph Butler, William Law, Joseph Proud, J. E. Gründler, D. E. Jablonski, A. E. Richter, Christian Protten, Pierre Nicole, Jean Racine, Noailles, Fléchier, Louvreleul, Misson, John Lacy, Barruel, John Quick, Deacon Fyodor Ivanov, Yavorsky, Platon Levshin, Chrysanthus Notaras, Antoni II, Athanasius IV Dabbas, Ardzivian, Chamich, Chardin, Claudius Buchanan, Joseph I of Diyarbakir, Gaspar Aquino de Belén, Garcia II of Kongo, Leonard Hansen, João Ferreira de Almeida.

Corrected (1): Edmund Jones (merge). Rescored (1): William Lee → WHO. Merged and removed (1): Joseph II.

Notes on confirmed LISTED rows, with no change made:
- **Fléchier** (FLECH 9, 277 ff.). The file prefixes his Academy eulogy, so a thin life is held. The Gui precedent could make him WHO as a hostile inside recorder of the Camisard war. LISTED is defensible because the eulogy is rhetoric, not a life. Judgment call for Mark.
- **Deacon Fyodor Ivanov.** Subbotin's introduction (FEDOR 20-200) discusses the man as well as the writings. A reading for a life could support WHO or STORY later.
- **Small line slips, harmless because the row also gives the right range:**
  - Rathbun: the quote is at TEST 6074; 304 is the chapter heading.
  - Ardzivian: the quote is at ORMANIAN 4526-4528.
  - Gründler: "John Ernest Grundler" is at ZIEG 12326 and later; 6478 reads "J. E. Grundler".

## Duplicates

- Within the table: Benedict XIV (two rows), Macarius III Zaim (pair row and single row), Joseph II (pair STORY row and LISTED row), Edmund Jones (two names, one file). All are merged as above.
- Watched, not merged:
  - "Lamech and Agrippa" (LISTED) against Peter Miller (WHO). The Library header identifies Agrippa as Miller and the translator denies knowing. The LISTED row already says Miller carries the person.
  - Antoni I and Antoni II are two different men.
- Earlier eras (1–6): I matched each era 8 name (its two longest tokens) against all 867 person rows of Who_Scan_Era1-6. No real matches: only namesakes (Clement, Innocent, Benedict, Thomas, Joseph and the like). Era 7 was not searched, as instructed.

## OUTSIDE WITNESS labels

No label was changed. The labels below are flagged for Mark; all five are already judgment calls and Question 1 of the B/C/D groups.
- **Volney.** Fits the rule: an Enlightenment philosophe with no church tie.
- **Hiob Ludolf.** Fits: a Lutheran scholar outside every Ethiopian party. Caveat: his Ethiopian side rests on one informant (Abba Gregorius).
- **Paul Rycaut.** Doubtful. An Anglican writing on the Greek and Armenian churches at his king's command is, on a strict reading, a rival church's writer. He is not a polemicist, though, and he writes as a diplomat. Keep only if Mark reads "rival church" as partisans only.
- **Tournefort.** Doubtful. A French Catholic royal botanist writing on Orthodox and Armenian worship, so a rival church's member [recollection of his faith; to confirm]. He is a traveller-observer, not a historian. On the brief's own terms this is at best a judgment call.
- **Moreau de Saint-Méry.** Looks wrong. He reports on the Catholic church of Saint-Domingue, which is nominally his own church. He writes from the colonists' side (census), so he is a partisan. Plain WHO, or LISTED, fits the rule better than OUTSIDE WITNESS.
- **Not labelled, and correctly so:** Walsh (Gregory V), de Merck, John Quick, Buchanan, Covel, Thomas Smith, Serpos and Paulinus. Bruce (WANTED) "would be" OUTSIDE WITNESS. That is arguable: he is a Scottish Protestant traveller, not a historian, and hostile to the Catholic party.

## Second pass

I used the same method as the first pass: a scripted quote check against the cited lines (with the rows_E and rows_F file keys added), every miss opened by hand, WANTED sources searched by file name and full text, and duplicates checked against the table and the era 1–6 tables.

### 1. The 23 added rows

**Counts: 23 checked; 21 confirmed, 2 corrected, 0 not supported.**

| Row | Outcome | Note |
|---|---|---|
| Archdeacon Thomas, Mar Thoma I ("of the Coonan Cross") | Corrected: merged and removed | A **duplicate** of the existing WHO row "Mar Thoma I (Archdeacon Thoma; 'Mar Thomas the Great')". The Sebastiani and Vincenzo evidence and the era 7 tag were added to that row. The added row's quotes check out. "nemico di pace" is at VIN 1230, not 848. "l'Intruso" is the Library's Content-note wording (SEB1 and SEB2, line 9), not a quote from the text. |
| Universalist hymn-book and Winchester men (group row) | Corrected | Line numbers fixed. "in 1776" is at CENT 2793, not 515. "sunny side of fifty" is at CENT 662; the row gave no line. "can not be considered strictly as the author" is at CENT 1121-1122. |
| Giuseppe di Santa Maria Sebastiani | Confirmed | "Delegato Apostolico ne' Regni de' Malavari" is in the SEB1 and SEB2 titles (line 1). "l'Intruso" is Content-note wording. SEB2 1608-1612 was not opened beyond the script's check. |
| Jean Léger | Confirmed | The OCR heading "Abbregé de la vie" is at LEG2 29684 (and 32181 in the index). 29754-29760 and 22012 read as claimed. 29781 names the uncle Antoine. |
| Stanisław Lubieniecki | Confirmed | Checked LUB 76-80 (born 23 Aug 1623) and LUB 480-500 (poison, the daughters' deaths). |
| Gerard Brandt the Elder | Confirmed | TID 6280-6283 ("ber. te Hoorn 22 Juli 1660"). The BRA3 title-page quote is at line 2. CAL 1357-1363 reads as claimed. |
| Absalom Jones | Confirmed | All 7 quotes match the ALLEN lines. Judgment call kept. |
| Giuseppe Simone Assemani; Theodore de Cock | Confirmed | OCR only (ASS1 3980 and 4737; HOYNCK 927-928; ACTA 660, 727 and 764-766). |
| Samuel Morland; Jerónimo Lobo; Vincenzo Maria | Confirmed | OCR only. |
| James McGready; Thomas Campbell; Raikes and Stock; Hans Nielsen Hauge; Kosmas Aitolos; Athanasios Parios (WANTED) | Confirmed: not held | Hits found for "M'Gready" (a subscriber in DAV 20759), Raikes (a book advertisement in PREACH 14647, subscribers in CHEAP) and Hauge (HELW2 only). None carries a life. No Kosmas Life in either Synaxaristes volume. SYN1 51549-51551 reads as claimed for Parios. |
| William Wells Jr.; Hieronymus de Bock; Hugo van Heussen; Balaam (Warlaam); Giuseppe Luigi Assemani (LISTED) | Confirmed | OCR only. COLL 43100-43102 has "Assemani senioris" and COLL 43177-43178 "Assemanus iunior". |

**Duplicates.** Archdeacon Thomas = Mar Thoma I (merged). There is no other duplicate inside the table. No added name is scored in eras 1–6: Assemani appears there only as a cited author.

### 2. Rows moved to era 9

There is no live row left for Richard Allen, Gregory V, Yohannan Hormizd or William Carey. Only cross-references remain, and none is a scored row:
- the Absalom Jones row cites Allen's book;
- "Kept apart from his nephews Hormizd and Yeshua-yau" (Elia row) and "Hormizd's elder cousin" (Yeshua-yau row);
- "Carey's companion" (John Thomas row) and the census mention of Carey in the Brainerd row.

These references are harmless. The era 9 scan should know that the Elia and Yeshua-yau rows point to Hormizd.

### 3. The WANTED rows re-tested against the era 7 precedents

Eight verdicts changed, all marked judgment call, with the Source-wanted cell cleared:

| Person | Change | Held lines that carry the life |
|---|---|---|
| Andrew Fuller | WANTED → WHO | His own preface tells his turn from high Calvinism, written 1781 (FULL 279-330). The BMS founding minutes make him secretary (RIP 29368-29373). Held own work + held witness. |
| Matthew Henry | WANTED → WHO | His own Life of his father (HENRY-P 504-510, 8138-8142: Chester). The held `henry-philip_diaries-and-letters_lee1882` gives his baptism (6496-6497), his ordination in 1687 (1967), the Gray's Inn letter (18609-18614) and the Chester letters (19787-19790). |
| Gilbert Burnet | WANTED → WHO | Two works of his own: the clergy manual and the Three Letters from Italy, 1687. Calamy, a contemporary, records his death at 72 and his standing (CAL 12467-12503). |
| Marie Durand | WANTED → STORY | Her own prisoner list (COQ1 21809-21815). Coquerel: jailed for her brother's ministry (COQ1 17740-17745), aged 53 in 1768 (COQ1 22045-22049). The registers: SAG 2504-2511, 8347. A testimony, not a shaper. |
| Abraham Mazel | WANTED → WHO | Two independent held witnesses: Court, who questioned him (CT1 3196-3200, 4053-4056; CT3 10187-10190, 14482-14520), and the London depositions (CRY 3726). Like Marion, a prophet-leader. |
| Antoine Arnauld | WANTED → WHO | Two witnesses: Pascal's letters of 1656 (PASC-M 2391-2398) and the nuns' narratives in Lowndes, which quote seventeenth-century memoirs (LOWN 13949-14040). This uses the founder precedent for the movement's theologian: flagged. |
| Pasquier Quesnel | WANTED → WHO | His own words in the 101 propositions the bull prints (UNIG). The hostile Denzinger note gives his dates (DENZ 23766-23770). Neale tells the life (NEALE 1756-1810). Neale is a late retelling (1858): flagged. |
| Nicodemus the Hagiorite and Macarius of Corinth | WANTED → WHO (pair) | A held Life of Nicodemus by Onouphrios the Iberite, prefixed to the Synaxaristes (SYN1 1095-1230): Naxos, Smyrna, Athos 1775, the Philokalia. Macarius stays thin inside the pair. |

One correction with no verdict change: **Isaac Watts.** The row cited CAL 3781 as "Calamy's account names Watts". That line names Michael Watts, Calamy's father-in-law, a namesake. Isaac appears only in Rutt's notes of 1829 (CAL 9941, 20553, 20925), so WANTED stands.

Re-tested and kept WANTED, because no held line carries a tellable life:
- **Hindmarsh:** minutes and roles only.
- **Bray:** one witness (HUMPH). The FOX2 "Thomas Bray" is a namesake copyist.
- **Hannah More:** her tracts are held, but only a subscriber line names her.
- **Wilberforce:** the other hits are later Wilberforces.
- **Kimpa Vita, da Gallo, Pedro IV, Maigrot, Pallu and Lambert:** Rome's letters and one Launay paragraph.
- **Anne Dutton:** her letters carry no life.
- **Samuel Davies:** volume 3 is sermons only.
- **Muratori, Rancé and Tikhon:** own works held, no life.
- **Doddridge:** two Priestley sentences.
- **Occom:** a one-paragraph advertisement (OCC 74-80). Arguable, but not a life.
- **Ann Griffiths:** the 1900 preface gives dates only.
- **Johanna Eleonora Petersen:** a handful of mentions in her husband's Life.
- **Raikes, McGready, Campbell, Hauge, Kosmas, Parios:** see the table in section 1.

"Thomas of the Coonan Cross" was not a WANTED row: it was the added WHO duplicate of Mar Thoma I, merged in section 1.

### 4. Sort and counts

The table is re-sorted WHO, STORY, WANTED, LISTED, keeping the existing order inside each block. Every row has 12 columns. **411 rows: WHO 139, STORY 51, WANTED 44, LISTED 177.** Check column: 262 Confirmed, 22 Corrected, 127 blank (LISTED rows not spot-checked).
