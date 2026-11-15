# Library search log: era 7 (1517-1650), 2026-11-15

The search record for the Library thread's fill of the era 7 wants: the era 7 rows of the wanted list (person rows
113-120, outside-witness rows 10-27, council row 22), the two council rows queued in `CFT-Wants.md` (the Marburg
Colloquy and the Diet of Worms), and the Library items of Open-Gaps 273. The vendored files, their state and their
shelves are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 7, filled"). This file says where the
batch searched, what it found, what it did not find, and what it did not take.

Rights rule for this batch: only a printed imprint of 1930 or earlier, read on the title page or on the scan's page
image; a reprint counts by its own date; no NC or ND licence, no permission notice, no access-restricted item.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images) | reachable | all 56 files |
| dbnl.org | reachable, by the eras 4-5 log | not needed |
| gallica, HathiTrust, books.google downloads, MDZ, documentacatholicaomnia | blocked or broken, by the era 5 log | not tried again |

No host was newly refused by the network proxy. archive.org has no full-text search from here, so every search was
by title, author and year.

## Holdings check, before any search

A whitespace-tolerant grep of the full text of every file in `cic/texts/` for 41 name and title patterns (Schütz
Zell, Dentière, the Epistre, Gracián, the Peregrinación, Fucan, Xu Guangqi under six spellings, Guaman Poma, the
Historia de las Indias, the Brevísima, Sahagún, Schirrmacher, Marburg, the Reichstagsakten, Poissy, Aleander, the
Confutatio, Herminjard, Scultetus, Olivetan, Busbecq, Leo Africanus, de Thou, Guicciardini, Machiavelli, Bodin,
Montaigne, Vasari, Usque, Joseph ha-Kohen, ibn Verga, Gans, Evliya, Kâtib Çelebi, Peçevi, Selaniki, Coburg).

Held already:
- **The Colloquy of Poissy (council row 22).** `beza_histoire-ecclesiastique-t1-fra_baum-cunitz1883.txt` has the
  chapter "Le Colloque de Poissy" from about file line 26871, with Beza's speech (about 27890-28704). The councils
  scan says so already; the wanted list's row still said "Not located", and is corrected.

Held and not enough: Trigault (1615) tells Xu Guangqi as a retelling; Foxe's English list of the Marburg articles
breaks off; the held Luther and Zwingli volumes have no report of the Marburg sessions; sixteen files name Las
Casas and none is his; Teresa's Foundations and the Discalced chronicle of 1655 tell Gracián from outside.

## Searches, by group

Four searchers ran in parallel (Sonnet), one per group, each held to one helper script for archive.org and to
`rg` and `sed` on the downloads. None stalled. Each pick was then checked by the Library thread: the title page in
the OCR or on its page image, the byte count against the host's record, the host's rights fields, the wanted
passage. Six corrections came out of that check:
- The Schirrmacher scan is the Gotha printing of 1876, not the reprint the host names (below).
- The fourth Machiavelli volume first picked has no title page; another scan of it, with one, was taken.
- Three drafted titles (Sée, Noack, the Montaigne volumes) were corrected to the title pages' own words.
- The searcher's "Dindseil" on the Corpus Reformatorum title page was read on the image as Bindseil.
- A sentence of Julien Sée's on Luther was first taken for Joseph ha-Kohen's; it is not cited.
- Balan's Monumenta, which no searcher opened, was fetched and read for Aleander's letters.

The review (`R1_review.md`) then settled several points from the texts; `R1_changes.md` lists them.

**The Who rows: Strasbourg, Geneva, Carmel.**
- Katharina Zell: Füsslin's Beyträge, part 5 (Zürich 1753), taken for her letter of 1557 to the citizens of
  Strasbourg and her answer to Rabus; Röhrich's Mittheilungen III (1855) taken for a Life with extracts from her
  letters and her hymn-book preface. Not found: the Entschuldigung of 1524 and the Miserere exposition of 1558.
  Wackernagel's Bibliographie (1855) prints the hymn book's title only, and says his copy lacks the preface; the
  third volume of his Kirchenlied (1864) does not name her; the reprints of both (1961-1990) are out by date. Seen,
  not taken: Lehr's study (1861); a volume of the Corpus Schwenckfeldianorum (host date 1908), not opened.
- Marie Dentière: Herminjard's tome 5 (1878) taken, for no. 785, the Epistre tres utile, which the editor prints
  with passages left out. Jeanne de Jussie's Levain du calvinisme (Fick, Geneva 1853) taken, for an opponent's
  account of her. Not found: the whole Epistre; Rilliet's printing of La guerre et deslivrance (tome 20 of the
  Geneva society's Mémoires, 1881; other tomes are on archive.org, not that one). A second Jussie (Fick 1865) not
  taken.
- Gracián: the Tratado de la redempcion de captivos (Brussels 1609) taken. The Peregrinación de Anastasio was not
  found under five title queries; the edition of 1932-33 is out by date. Mármol's Life (1619) is on archive.org
  with OCR that cannot be read; not taken. Four more of his own tracts in the same Seville scan series (1609-1614)
  were seen and not fetched.
- Herminjard's tome 2 (1868) taken for the Waldensian assembly of 1532 (Open-Gaps 273): it holds Saunier's letter
  to Farel of 5 November 1532 and the editor's notes; no account by one who was there. Tome 3 (1870) was read and
  not taken: it does not print Olivétan's preface. The nine tomes are all on archive.org.
- Scultetus: the scan of 1618 holds the first decade only (1516-1525). Von der Hardt's Historia literaria
  reformationis (1717) reprints the Annales to 1535, but the OCR loses half-lines and the 1532 passage was not
  found. Neither taken.
- The Olivetan Bible: the scan of the 1535 printing carries the French national library's notice on commercial
  reuse, and its black letter cannot be read in the OCR. Held for Mark. Reuss's study (1866) describes the preface
  and does not print it.

**The councils: Marburg, Worms, Augsburg.**
- Schirrmacher, Briefe und Acten (Gotha 1876): one scan. The host's record gives the publisher as B. R. Grüner,
  Amsterdam, the date as 1968, and says "Reprint of the original Gotha, 1876 ed". The scan itself is a library's
  copy of the original: the title page (leaf n7) reads "Gotha. Friedrich Andreas Perthes. 1876." and carries two
  old library stamps and an ink shelf mark; the last text leaf (n622) has the printer's line "Druck von Friedr.
  Andr. Perthes in Gotha"; the binding is old half leather; no reprint leaf stands at the front or the back, and
  the words Amsterdam, Grüner, Nachdruck and 1968 are nowhere in the OCR. Taken on the title page, as the rule
  reads. The Latin report of the sessions is at OCR lines 1210-1836; the articles are not printed in it.
- The Weimar edition, volume 30, part 3 (1910), taken: the reports of Hedio, the Anonymous, Collin, Osiander and
  Brenz, and the articles with their signatures. A second Weimar volume of 1909 was fetched and not read.
- Kidd's Documents (Oxford 1911) taken: Worms nos. 39-46, Marburg nos. 109-110, Augsburg nos. 116-123. Seven
  duplicate scans and two reprints of 1967 not taken.
- Deutsche Reichstagsakten, jüngere Reihe II (Gotha 1896), taken. The host dates it 1893. A duplicate not taken.
- Aleander: Balan's Monumenta reformationis Lutheranae (1884) taken. Kalkoff's German of the dispatches (1886):
  one scan has black letter the OCR cannot read, a second failed to download, a third (1897) has a torn cover and
  cut text; none taken. Hausrath (1897) and Kalkoff's study (1908) not opened.
- The Confutatio: Corpus Reformatorum 27 (1859) taken for the Latin; Reu (Chicago 1930) for the English, with
  other Augsburg sources. Reu's preface is dated 15 December 1930; the title page says 1930, the last year the
  rule admits. A reprint of 1966 not taken.
- Förstemann's Urkundenbuch, volume 2 (Halle 1835), taken; the OCR reads the year as 1839 and the host says 1833.
  It prints the recesses of 22 September and 13 October; the editor leaves out the text of 19 November as well
  enough known. A duplicate with poorer OCR not taken; the first volume not opened.
- Laemmer's Monumenta Vaticana (1861) taken, for Campeggio's letters from Augsburg. A duplicate not taken.
- Luther's Coburg letters: de Wette's part 4 (1827) taken for the original, Currie (1908) for the English. Smith
  and Jacobs, volume 2 (1918), ends in April 1530 and was not taken; Enders's volumes 7 and 8 not taken.
- Not taken: Jacobs's Book of Concord, volume II, an undated upload whose title-page year was not read; Erichson
  (1880), a narrative with poor OCR that does not print Hedio's journal. Not found: the fourth volume of Schuler
  and Schulthess's Zwingli; Köhler (1929); Heppe's facsimile; the seventh Weimar volume.

**The mission worlds.**
- Las Casas: the Historia de las Indias (Madrid, Ginesta, 1875-76), five volumes of one library's set, taken. A
  second set lacks its third volume; Aguilar's edition (1927) was not examined. The Brevísima: the Cádiz printing
  of 1821 taken (title page read on leaf n4), and MacNutt (Cleveland 1909), which prints it in English. Located,
  not taken: The Tears of the Indians (London 1656), with fair OCR. The Spanish Colonie (1583) cannot be read in
  the OCR. Four reprints or microfilms of 1966-1970 not taken.
- Sahagún: Bustamante's three volumes (Mexico 1829-30) and his separate printing of Book XII (1829) taken. The
  French of Jourdanet and Siméon (1880) is located, not taken. Not found: Seler (1927); Nuttall (1927). The
  Colloquios (Pou y Martí, 1924) is named in the album of the Miscellanea Ehrle; the two volumes most likely to
  hold it are marked access-restricted and refused the fetch. Held for Mark.
- Xu Guangqi: the March 1850 number of The Chinese Repository taken, for "Paul Sü's Apology". The scan of the
  whole of volume 19 is a Kraus reprint and was not taken. Nothing else of his in translation was found under
  twelve spellings; the Variétés sinologiques were not opened.
- Fabian Fucan: nothing in a Western language printed by 1930. Two Japanese-only volumes (1923, 1925) and Anesaki's
  concordance (1930, a microform) were seen and not taken.
- Guaman Poma: nothing before the facsimile of 1936. Pietschmann's paper (Göttingen Nachrichten, 1908) is not on
  archive.org; three other volumes of the Nachrichten were searched and do not name him.

**The outside witnesses.**
- Kâtib Çelebi: Mitchell's Maritime Wars (London 1831), chapters I-IV, taken; the year was read on leaf n6. A
  reprint of 2012 not taken.
- Evliya Çelebi: von Hammer's three parts (1834, 1846, 1850) taken. The second is a Digital Library of India scan
  whose title page says "Vol. I, Part I" over the text of Part II. Four duplicates not taken.
- Peçevi, Mustafa Ali, Selaniki: no translation printed by 1930. The Istanbul printing of Peçevi (1866) is in
  Ottoman script the OCR cannot read.
- Joseph ha-Kohen: Bialloblotzky's Chronicles (1835-36) and Sée's Vallée des pleurs (Paris 1881) taken. Wiener's
  German Emek habacha (1858) was fetched and not taken: the black letter is poorly read and the year is garbled.
- Usque: the Coimbra edition of 1906 taken. Editions of 1949 and 1964 are out by date.
- Gedaliah ibn Yahya; David Gans: nothing found under five and six spellings.
- Ibn Verga: Gentius's Latin (Amsterdam 1651) taken; the year was read on leaf n4. Wiener's German (1856) was
  fetched and not taken for its OCR. Two Hebrew scans not taken.
- De Thou: the Latin of 1733 and the French of 1734 are on archive.org in part. Not taken for their length. His De
  vita sua (host date 1621) has poor OCR and no title page in the scan; not taken.
- Guicciardini: Gherardi's Storia d'Italia (Florence 1919), four volumes, taken. Located, not taken: Goddard's
  English (1753-56), Rosini's Italian (1835-37), the Counsels and Reflections (1890).
- Machiavelli: Detmold's four volumes (Boston 1882) taken. The reissue of 1891 not taken.
- Bodin: Knolles's Six Bookes (London 1606; title page read on leaf n4) and Noack's Colloquium heptaplomeres
  (1857) taken. Three facsimiles of 1962 not taken.
- Montaigne: Florio's Essays in the Tudor Translations (London 1892-93), three volumes, taken. A reprint of 1967
  not taken; Cotton's translation located, not taken.
- Vasari: Foster's English (1850-52) and de Vere's (1912-15) are on archive.org in part. Not taken for their
  length.
- Leo Africanus: the Hakluyt Society's three volumes (1896) taken; the year was read on the title leaf of each
  (n7, n8, n8), and none has a reprinter's leaf. Five Burt Franklin reprints (1963) not taken.
- Busbecq: Forster and Daniell's two volumes (London 1881) taken; the second volume's year was read on leaf n12.
  A printing of 1927 was not examined.

## Imprints read on the page image

Where the OCR title page gave no year or a doubtful one, the Library thread viewed the leaf: Herminjard 2 (leaf
n6), Jussie (n13), Gracián (n0), Schirrmacher (n7, and n622 for the printer's line), the Weimar volume (n4), Balan
(n7), Corpus Reformatorum 27 (n11), Förstemann 2 (n4), the Cádiz Brevísima (n4), Kâtib Çelebi (n6), Gentius (n4),
Bodin's Six Bookes (n4), Leo Africanus 1-3 (n7, n8, n8), Busbecq 2 (n12).

## Not found or not filled, by want

- Rows 113-120: Zell's Entschuldigung, hymn-book preface in full and Miserere exposition; the whole of Dentière's
  Epistre and La guerre et deslivrance; Gracián's Peregrinación; anything of Fabian Fucan; more of Xu Guangqi than
  one memorial; Guaman Poma; the Nahuatl of Sahagún's informants and the Colloquios.
- Outside witnesses: Peçevi, Mustafa Ali, Selaniki, Gedaliah ibn Yahya, David Gans. De Thou and Vasari are
  located and not taken.
- Councils and Open-Gaps 273: the text of the recess of 19 November 1530; Scultetus's second decade in a readable
  scan; the Olivetan preface; the Chanforan manuscript (not searched); Jacobs's second volume in a dated scan.
